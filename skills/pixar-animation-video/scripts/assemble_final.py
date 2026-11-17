#!/usr/bin/env python3
"""Provider-neutral final assembly with ffmpeg only (offline, no API, no cost).

Takes approved clips + per-clip voice-over + one music bed (+ optional ambient and SFX) and produces one
finished video whose audio never goes empty, with the music/ambient ducked under the voice-over.

  python3 assemble_final.py --clips clips/s01.mp4 clips/s02.mp4 ... \
      --vo vo/s01.wav vo/s02.wav ... --music music.wav [--ambient forest.wav] \
      [--sfx sfx/shimmer.wav@2.5 ...] --out final/rico-9x16.mp4

Rules implemented (from the pack's audio direction):
  * VO line i starts `--lead` seconds (default 0.25) after clip i starts and must fit inside the clip.
  * Music and ambient are ONE continuous bed over the whole video (looped/trimmed, faded out at the end).
  * Music/ambient are ducked under every VO line (sidechain), so music never covers the voice-over.
  * Clips are re-encoded to one common size/fps so clips from any generator join cleanly.
Exit code 0 only if the self-checks pass (durations match, VO fits, no silent window).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> str:
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        sys.exit(f"ffmpeg/ffprobe failed (rc={p.returncode}): {' '.join(cmd[:6])} ...\n{p.stderr[-600:]}")
    return p.stderr + p.stdout


def duration(path: str) -> float:
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).strip().splitlines()[-1])


def mean_db(path: str, start: float, length: float) -> float:
    p = subprocess.run(["ffmpeg", "-v", "info", "-ss", f"{start}", "-t", f"{length}", "-i", path, "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    for line in p.stderr.splitlines():
        if "mean_volume" in line:
            return float(line.split("mean_volume:")[1].split("dB")[0])
    return -91.0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--clips", nargs="+", required=True)
    ap.add_argument("--vo", nargs="+", required=True, help="one voice-over file per clip, same order")
    ap.add_argument("--music", required=True)
    ap.add_argument("--ambient")
    ap.add_argument("--sfx", nargs="*", default=[], help="file@start_seconds on the final timeline")
    ap.add_argument("--out", required=True)
    ap.add_argument("--lead", type=float, default=0.25)
    ap.add_argument("--size", default="720x1280", help="WxH of the output (9:16 default; use 1280x720 for 16:9)")
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--music-gain", type=float, default=0.35)
    ap.add_argument("--ambient-gain", type=float, default=0.5)
    a = ap.parse_args()
    if len(a.clips) != len(a.vo):
        sys.exit(f"{len(a.clips)} clips but {len(a.vo)} voice-over files; they must match one to one")
    W, H = a.size.split("x")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    work = out.parent / (out.stem + "_work"); work.mkdir(exist_ok=True)

    cdur = [duration(c) for c in a.clips]
    starts = [sum(cdur[:i]) for i in range(len(cdur))]
    total = sum(cdur)
    vdur = [duration(v) for v in a.vo]
    over = [f"clip {i+1}: VO {v:.2f}s + lead {a.lead}s > clip {c:.2f}s" for i, (v, c) in enumerate(zip(vdur, cdur)) if v + a.lead > c + 1e-6]
    if over:
        sys.exit("VO does not fit its clip (trim the clip to VO+0.5s only if it is LONGER than needed; here the VO is longer):\n  " + "\n  ".join(over))

    # 1) video: normalize and join
    vin = sum([["-i", c] for c in a.clips], [])
    vf = "".join(f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={a.fps},setsar=1,format=yuv420p[v{i}];" for i in range(len(a.clips)))
    vf += "".join(f"[v{i}]" for i in range(len(a.clips))) + f"concat=n={len(a.clips)}:v=1:a=0[v]"
    video = str(work / "video.mp4")
    run(["ffmpeg", "-v", "error", "-y", *vin, "-filter_complex", vf, "-map", "[v]", "-c:v", "libx264", "-crf", "18", "-preset", "medium", video])

    # 2) voice-over track on the final timeline
    ain = sum([["-i", v] for v in a.vo], [])
    parts = "".join(f"[{i}:a]aresample=44100,aformat=channel_layouts=mono,adelay={int((s + a.lead) * 1000)}|{int((s + a.lead) * 1000)}[a{i}];" for i, s in enumerate(starts))
    parts += "".join(f"[a{i}]" for i in range(len(a.vo))) + f"amix=inputs={len(a.vo)}:normalize=0:duration=longest,apad=whole_dur={total},atrim=0:{total}[vo]"
    vo_track = str(work / "vo_track.wav")
    run(["ffmpeg", "-v", "error", "-y", *ain, "-filter_complex", parts, "-map", "[vo]", "-ar", "44100", "-ac", "1", vo_track])

    # 3) one continuous bed: music (+ ambient), looped/trimmed to the total length, faded out
    bed_in = ["-stream_loop", "-1", "-i", a.music] + (["-stream_loop", "-1", "-i", a.ambient] if a.ambient else [])
    bf = f"[0:a]aresample=44100,aformat=channel_layouts=mono,volume={a.music_gain}[mu];"
    if a.ambient:
        bf += f"[1:a]aresample=44100,aformat=channel_layouts=mono,volume={a.ambient_gain}[am];[mu][am]amix=inputs=2:normalize=0:duration=longest[b0];"
        last = "b0"
    else:
        last = "mu"
    bf += f"[{last}]atrim=0:{total},afade=t=out:st={max(total - 1.0, 0)}:d=1.0[bed]"
    bed = str(work / "bed.wav")
    run(["ffmpeg", "-v", "error", "-y", *bed_in, "-filter_complex", bf, "-map", "[bed]", "-t", f"{total}", "-ar", "44100", "-ac", "1", bed])

    # 4) duck the bed under the VO, add VO and SFX
    ducked = str(work / "ducked.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", bed, "-i", vo_track, "-filter_complex",
         "[0][1]sidechaincompress=threshold=0.02:ratio=10:attack=20:release=300[d]", "-map", "[d]", "-t", f"{total}", "-ar", "44100", "-ac", "1", ducked])
    sfx_in, sfx_f, labels = [], "", ["[0:a]", "[1:a]"]
    for j, s in enumerate(a.sfx):
        f, _, at = s.rpartition("@")
        ms = int(float(at) * 1000)
        sfx_in += ["-i", f]
        sfx_f += f"[{j + 2}:a]aresample=44100,aformat=channel_layouts=mono,volume=0.6,adelay={ms}|{ms}[s{j}];"
        labels.append(f"[s{j}]")
    mix = str(work / "mix.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", ducked, "-i", vo_track, *sfx_in, "-filter_complex",
         sfx_f + "".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,alimiter=limit=0.95[m]", "-map", "[m]", "-t", f"{total}", "-ar", "44100", "-ac", "1", mix])

    # 5) mux
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", mix, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", str(out)])

    # self-checks
    checks = {}
    vd = duration(str(out))
    streams = run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,duration", "-of", "json", str(out)])
    sj = json.loads(streams)["streams"]
    durs = {s["codec_type"]: float(s["duration"]) for s in sj}
    checks["video_and_audio_durations_match"] = abs(durs.get("video", 0) - durs.get("audio", 0)) < 0.15 and abs(vd - total) < 0.3
    silent = [round(t * 0.5, 1) for t in range(int(total / 0.5)) if mean_db(str(out), t * 0.5, 0.5) < -50.0]
    checks["no_silent_0.5s_window"] = not silent
    bed_in_vo = mean_db(ducked, starts[0] + a.lead + 0.2, max(vdur[0] - 0.4, 0.3))
    bed_raw = mean_db(bed, starts[0] + a.lead + 0.2, max(vdur[0] - 0.4, 0.3))
    checks["music_ducked_under_vo"] = bed_in_vo < bed_raw - 3.0
    report = {"out": str(out), "total_seconds": round(total, 3), "clips": len(a.clips), "vo_seconds": [round(v, 2) for v in vdur],
              "silent_windows": silent, "bed_db_raw_vs_ducked_in_first_vo": [round(bed_raw, 1), round(bed_in_vo, 1)], "checks": checks}
    (work / "report.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
