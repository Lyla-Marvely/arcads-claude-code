#!/usr/bin/env python3
"""Build burned-in captions (ASS) from the voice-over files themselves: no speech recognition model, no download.

Because the narration is generated here, the exact text and the exact audio length of every line are known.
Each line is split into short phrases and the phrases share the line's measured duration in proportion to their length.

  python3 zc_captions.py --lines lines.json --vo-dir vo/ --starts s01=0,s02=8,... --out captions.ass [--lead 0.25]
Then burn:  ffmpeg -i in.mp4 -vf "ass=captions.ass:fontsdir=~/.cache/zero-cost-shorts/fonts" -c:a copy out.mp4
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import soundfile as sf


def ts(t: float) -> str:
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def phrases(text: str, max_chars: int = 26) -> list[str]:
    parts = [p.strip() for p in re.split(r"(?<=[.,!?;:])\s+", text.strip()) if p.strip()]
    out: list[str] = []
    for p in parts:
        if len(p) <= max_chars or " " not in p:
            out.append(p)
            continue
        words, cur = p.split(), ""
        for w in words:
            if cur and len(cur) + 1 + len(w) > max_chars:
                out.append(cur)
                cur = w
            else:
                cur = f"{cur} {w}".strip()
        if cur:
            out.append(cur)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lines", required=True)
    ap.add_argument("--vo-dir", required=True)
    ap.add_argument("--starts", required=True, help="id=seconds,... start of each scene on the final timeline")
    ap.add_argument("--out", required=True)
    ap.add_argument("--lead", type=float, default=0.25)
    ap.add_argument("--font", default="Baloo 2")
    ap.add_argument("--size", type=int, default=70)
    ap.add_argument("--margin-v", type=int, default=210, help="distance from the TOP (px of 1280): keeps captions clear of the Shorts UI at the bottom")
    ap.add_argument("--play", default="720x1280")
    a = ap.parse_args()
    starts = {k: float(v) for k, v in (kv.split("=") for kv in a.starts.split(","))}
    W, H = a.play.split("x")
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Kid,{a.font},{a.size},&H00FFFFFF,&H000000FF,&H00502A14,&H64000000,-1,0,0,0,100,100,0,0,1,7,3,8,40,40,{a.margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = []
    for ln in json.loads(Path(a.lines).read_text()):
        wav = Path(a.vo_dir) / f"{ln['id']}.wav"
        info = sf.info(str(wav))
        dur = info.frames / info.samplerate
        ph = phrases(ln["text"])
        total = sum(len(p) for p in ph)
        t = starts[ln["id"]] + a.lead
        for p in ph:
            d = dur * len(p) / total
            ev.append(f"Dialogue: 0,{ts(t)},{ts(t + d)},Kid,,0,0,0,,{{\\fad(60,60)}}{p.replace(chr(10), ' ')}")
            t += d
    Path(a.out).write_text(head + "\n".join(ev) + "\n", encoding="utf-8")
    print(f"{len(ev)} caption events -> {a.out}")


if __name__ == "__main__":
    main()
