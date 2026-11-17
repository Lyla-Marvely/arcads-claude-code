#!/usr/bin/env python3
"""Zero-cost audio toolkit: English TTS (Kokoro, Apache-2.0, offline) + procedural music, forest ambience and SFX.

Everything is generated locally with numpy: no account, no API, no download except the one-time Kokoro model
(zc_setup.py). All sounds are original (synthesised), so there is no licensing issue.

  zc_audio.py tts     --script lines.json --voice am_michael --speed 0.95 --out vo/        # [{"id":"s01","text":"..."}]
  zc_audio.py music   --seconds 30 --bpm 104 --out music.wav
  zc_audio.py ambient --seconds 30 --out ambient.wav
  zc_audio.py sfx     --kind chime|swell|footsteps|whoosh|rustle|chirp --seconds 2 --out sfx.wav [--seed N]

NOTE: the author of this tool cannot listen to audio. Levels, durations and clipping are checked numerically;
how it SOUNDS must be judged by a human.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import soundfile as sf

SR = 44100
MODELS = Path.home() / ".cache/zero-cost-shorts/models"


def tvec(sec: float) -> np.ndarray:
    return np.arange(int(sec * SR)) / SR


def hz(note: str) -> float:
    names = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
    n = names[note[0]]
    n += 1 if "#" in note else 0
    octv = int(note[-1])
    return 440.0 * 2 ** ((n + 12 * (octv + 1) - 69) / 12)


def place(buf: np.ndarray, sig: np.ndarray, at: float, gain: float = 1.0) -> None:
    i = int(at * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


def marimba(freq: float, dur: float = 0.6) -> np.ndarray:
    t = tvec(dur)
    y = np.sin(2 * np.pi * freq * t) * np.exp(-t * 7) + 0.35 * np.sin(2 * np.pi * freq * 4 * t) * np.exp(-t * 18) + 0.12 * np.sin(2 * np.pi * freq * 9.2 * t) * np.exp(-t * 40)
    y *= np.minimum(1, t / 0.004)
    return y.astype(np.float32)


def bell(freq: float, dur: float = 1.2) -> np.ndarray:
    t = tvec(dur)
    y = sum(a * np.sin(2 * np.pi * freq * r * t) * np.exp(-t * d) for r, a, d in ((1, 1.0, 3.2), (2.76, 0.5, 5.0), (5.4, 0.28, 8.0), (8.93, 0.14, 12.0)))
    return (y * np.minimum(1, t / 0.002)).astype(np.float32)


def pluck_bass(freq: float, dur: float = 0.5) -> np.ndarray:
    t = tvec(dur)
    return (np.sin(2 * np.pi * freq * t) * np.exp(-t * 6) + 0.25 * np.sin(2 * np.pi * freq * 2 * t) * np.exp(-t * 9)).astype(np.float32)


def noise(sec: float, seed: int) -> np.ndarray:
    return np.random.default_rng(seed).normal(0, 1, int(sec * SR)).astype(np.float32)


def lp(x: np.ndarray, fc: float) -> np.ndarray:
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.zeros_like(x)
    acc = 0.0
    for i, v in enumerate(x):  # one-pole low-pass (short signals only)
        acc = (1 - a) * v + a * acc
        y[i] = acc
    return y


def hp(x: np.ndarray, fc: float) -> np.ndarray:
    return x - lp(x, fc)


def norm(x: np.ndarray, peak: float = 0.85) -> np.ndarray:
    m = float(np.max(np.abs(x))) or 1.0
    return (x / m * peak).astype(np.float32)


# ------------------------------------------------------------------ music
def make_music(seconds: float, bpm: float = 104) -> np.ndarray:
    buf = np.zeros(int(seconds * SR) + SR, np.float32)
    beat = 60.0 / bpm
    bar = 4 * beat
    chords = [("C", ["C3", "G3"], ["C4", "E4", "G4"]), ("G", ["G2", "D3"], ["B3", "D4", "G4"]), ("A", ["A2", "E3"], ["A3", "C4", "E4"]), ("F", ["F2", "C3"], ["A3", "C4", "F4"])]
    mel = {  # eighth-note melodies (None = rest), C-major pentatonic-ish
        0: ["E5", None, "G5", None, "A5", "G5", "E5", None], 1: ["D5", None, "G5", None, "B5", "A5", "G5", None],
        2: ["C5", None, "E5", None, "A5", "G5", "E5", "C5"], 3: ["A4", None, "C5", None, "F5", "E5", "C5", None]}
    n_bars = int(seconds // bar) + 1
    for b in range(n_bars):
        t0 = b * bar
        last = t0 + bar >= seconds - 0.01 or b == n_bars - 1
        name, bass, pad = chords[b % 4] if not last else chords[0]
        # soft pad
        for nt in pad:
            f = hz(nt)
            tt = tvec(bar + 0.3)
            env = np.minimum(1, tt / 0.25) * np.exp(-np.maximum(tt - bar, 0) * 6)
            place(buf, (np.sin(2 * np.pi * f * tt) * env * 0.05).astype(np.float32), t0)
        # bass on beats 1 and 3
        place(buf, pluck_bass(hz(bass[0])), t0, 0.30)
        place(buf, pluck_bass(hz(bass[1])), t0 + 2 * beat, 0.22)
        if last:
            for nt, off in (("G5", 0.0), ("E5", 0.0)):
                place(buf, marimba(hz(nt), 1.6), t0 + off, 0.30)
            place(buf, bell(hz("C6"), 2.5), t0 + beat, 0.18)
            break
        # melody (octave variation every second pass)
        shift = 1 if (b // 4) % 2 == 1 else 0
        for k, nt in enumerate(mel[b % 4]):
            if nt is None:
                continue
            f = hz(nt) * (2 ** shift if nt[-1] == "4" and shift else 1)
            place(buf, marimba(f), t0 + k * beat / 2, 0.30 if k % 2 == 0 else 0.22)
        # glockenspiel sparkle on beats 2 and 4
        for k, nt in enumerate((pad[2], pad[1])):
            place(buf, bell(hz(nt[:-1] + str(int(nt[-1]) + 2)), 0.8), t0 + (1 + 2 * k) * beat, 0.07)
        # shaker on off-beats
        for k in range(8):
            sh = hp(noise(0.05, 100 + b * 8 + k), 5000) * np.exp(-tvec(0.05) * 60)
            place(buf, sh.astype(np.float32), t0 + k * beat / 2 + (beat / 4 if k % 2 else 0), 0.04)
    out = buf[: int(seconds * SR)].copy()
    fade = int(0.8 * SR)
    out[-fade:] *= np.linspace(1, 0, fade)
    return norm(out, 0.8)


# ------------------------------------------------------------------ ambience
def make_ambient(seconds: float, seed: int = 11) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(seconds * SR)
    t = tvec(seconds)
    breeze = lp(noise(seconds, seed), 700) * (0.55 + 0.45 * np.sin(2 * np.pi * 0.13 * t + 1.0))
    breeze = hp(breeze, 120)
    out = norm(breeze, 0.35)
    # leaf rustles
    for _ in range(int(seconds * 1.2)):
        d = rng.uniform(0.15, 0.4)
        r = hp(noise(d, int(rng.integers(0, 10**6))), 3500) * np.exp(-tvec(d) * rng.uniform(6, 12))
        place(out, (r * 0.06).astype(np.float32), rng.uniform(0, seconds - 0.5))
    # birds: short chirp phrases at random times
    for _ in range(int(seconds / 2.2)):
        at = rng.uniform(0.3, seconds - 1.0); f0 = rng.uniform(2300, 3800)
        for s in range(int(rng.integers(2, 5))):
            d = 0.07; tt = tvec(d)
            f = f0 * (1 + 0.35 * np.sin(np.pi * tt / d) * (1 if s % 2 == 0 else -1)) + 120 * np.sin(2 * np.pi * 38 * tt)
            ph = 2 * np.pi * np.cumsum(f) / SR
            place(out, (np.sin(ph) * np.sin(np.pi * tt / d) ** 2 * 0.10).astype(np.float32), at + s * 0.1)
    return norm(out[:n], 0.6)


# ------------------------------------------------------------------ sfx
def make_sfx(kind: str, seconds: float, seed: int = 5) -> np.ndarray:
    rng = np.random.default_rng(seed)
    out = np.zeros(int(seconds * SR), np.float32)
    if kind == "chime":
        for k, nt in enumerate(("E6", "G6", "C7", "E7")):
            place(out, bell(hz(nt), min(1.6, seconds)), k * 0.07, 0.5 / (1 + 0.15 * k))
    elif kind == "swell":  # rising shimmer: bells ascending and getting denser
        for i in range(int(seconds * 7)):
            f = hz("C5") * 2 ** (rng.choice([0, 4, 7, 12, 16, 19, 24]) / 12)
            at = i / 7.0 + rng.uniform(0, 0.08)
            g = 0.14 + 0.5 * (at / seconds) ** 1.5
            place(out, bell(f, 0.9), at, g)
    elif kind == "footsteps":
        step = 0.5
        for i in range(int(seconds / step)):
            d = 0.11
            th = lp(noise(d, int(rng.integers(0, 10**6))), 420) * np.exp(-tvec(d) * 30)
            place(out, norm(th, 0.7), i * step + (0.02 if i % 2 else 0), 0.8)
    elif kind == "whoosh":
        for i in range(int(seconds / 0.28)):
            d = 0.2; tt = tvec(d)
            w = lp(noise(d, int(rng.integers(0, 10**6))), 1400) * np.sin(np.pi * tt / d) ** 2
            place(out, norm(hp(w, 300), 0.5), i * 0.28)
    elif kind == "rustle":
        for _ in range(int(seconds * 5)):
            d = rng.uniform(0.12, 0.3)
            place(out, (hp(noise(d, int(rng.integers(0, 10**6))), 3000) * np.exp(-tvec(d) * 9) * 0.5).astype(np.float32), rng.uniform(0, max(seconds - d, 0.01)))
    elif kind == "chirp":
        for s in range(3):
            d = 0.09; tt = tvec(d)
            f = 3000 * (1 + 0.3 * np.sin(np.pi * tt / d) * (1 if s % 2 == 0 else -1))
            place(out, (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * tt / d) ** 2 * 0.5).astype(np.float32), s * 0.13)
    else:
        raise SystemExit(f"unknown sfx kind {kind}")
    return norm(out, 0.7)


# ------------------------------------------------------------------ tts
def run_tts(script: str, voice: str, speed: float, out: str) -> None:
    from kokoro_onnx import Kokoro
    k = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    lines = json.loads(Path(script).read_text())
    Path(out).mkdir(parents=True, exist_ok=True)
    for ln in lines:
        y, sr = k.create(ln["text"], voice=voice, speed=speed, lang="en-us")
        y = np.asarray(y, np.float32)
        # trim leading/trailing silence so VO timing is exact
        thr = 0.01 * float(np.max(np.abs(y)))
        idx = np.where(np.abs(y) > thr)[0]
        y = y[max(idx[0] - int(0.03 * sr), 0): idx[-1] + int(0.08 * sr)] if len(idx) else y
        p = Path(out) / f"{ln['id']}.wav"
        sf.write(p, y, sr)
        print(f"{ln['id']}: {len(y) / sr:.2f}s -> {p}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tts"); t.add_argument("--script", required=True); t.add_argument("--voice", default="am_michael"); t.add_argument("--speed", type=float, default=0.95); t.add_argument("--out", required=True)
    m = sub.add_parser("music"); m.add_argument("--seconds", type=float, default=30); m.add_argument("--bpm", type=float, default=104); m.add_argument("--out", required=True)
    a = sub.add_parser("ambient"); a.add_argument("--seconds", type=float, default=30); a.add_argument("--seed", type=int, default=11); a.add_argument("--out", required=True)
    s = sub.add_parser("sfx"); s.add_argument("--kind", required=True); s.add_argument("--seconds", type=float, default=1.5); s.add_argument("--seed", type=int, default=5); s.add_argument("--out", required=True)
    g = ap.parse_args()
    if g.cmd == "tts":
        run_tts(g.script, g.voice, g.speed, g.out)
        return
    y = {"music": lambda: make_music(g.seconds, g.bpm), "ambient": lambda: make_ambient(g.seconds, g.seed), "sfx": lambda: make_sfx(g.kind, g.seconds, g.seed)}[g.cmd]()
    sf.write(g.out, y, SR)
    print(f"{g.cmd}: {len(y) / SR:.2f}s peak={float(np.max(np.abs(y))):.2f} -> {g.out}")


if __name__ == "__main__":
    main()
