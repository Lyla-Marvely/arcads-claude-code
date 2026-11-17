#!/usr/bin/env python3
"""One-command zero-cost production: render scenes -> mix audio -> QA (text/badge) -> captions -> final Shorts mp4.

  python3 zc_produce.py production.json [--reuse-clips] [--no-captions]

production.json (see templates/*.production.json) points at: the scene spec, the per-scene voice-over files,
music/ambient beds and SFX cues (seconds from the start of a scene). Every step is local and free.
Exit code 0 only if the assembly self-checks AND the text/badge QA pass.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sh(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    print("  $", " ".join(str(c) for c in cmd)[:200])
    return subprocess.run([str(c) for c in cmd], **kw)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("production")
    ap.add_argument("--reuse-clips", action="store_true", help="do not re-render clips that already exist")
    ap.add_argument("--no-captions", action="store_true")
    a = ap.parse_args()
    P = json.loads(Path(a.production).read_text())
    spec = json.loads(Path(P["spec"]).read_text())
    out = Path(P["out_dir"]); (out / "clips").mkdir(parents=True, exist_ok=True)
    py = sys.executable
    ids = P.get("scenes") or [s["id"] for s in spec["scenes"]]
    dur = {s["id"]: s["duration"] for s in spec["scenes"]}

    print("[1/5] render scenes (silent)")
    for sid in ids:
        clip = out / "clips" / f"{sid}.mp4"
        if a.reuse_clips and clip.exists():
            print(f"  reuse {clip}")
            continue
        if sh([py, HERE / "zc_render.py", P["spec"], "--scene", sid, "--out", clip]).returncode != 0:
            sys.exit(f"render failed for {sid}")

    starts, t = {}, 0.0
    for sid in ids:
        starts[sid] = t
        t += dur[sid]
    total = t

    print("[2/5] mix audio and assemble")
    sfx = [f"{c['file']}@{starts[c['scene']] + c['at']:.3f}" for c in P.get("sfx", [])]
    base = out / (P["name"] + "_nocaptions.mp4")
    cmd = [py, HERE.parent.parent / "pixar-animation-video/scripts/assemble_final.py", "--clips", *[out / "clips" / f"{s}.mp4" for s in ids], "--vo", *[Path(P["vo_dir"]) / f"{s}.wav" for s in ids],
           "--music", P["music"], "--out", base, "--size", f"{spec['size'][0]}x{spec['size'][1]}", "--fps", str(spec.get("fps", 24))]
    if P.get("ambient"):
        cmd += ["--ambient", P["ambient"]]
    if sfx:
        cmd += ["--sfx", *sfx]
    if sh(cmd).returncode != 0:
        sys.exit("assembly self-checks FAILED")

    print("[3/5] QA: any text, badge or logo in the picture?")
    qa_py = str(Path(P.get("qa_python", "~/.cache/zero-cost-shorts/venv-qa/bin/python")).expanduser())
    r = sh([qa_py, HERE.parent.parent / "pixar-animation-video/scripts/qa_text_check.py", "--video", base, "--every", "0.5"])
    if r.returncode != 0:
        sys.exit("QA FAILED: text/badge detected in the picture (captions are added only after this check)")

    final = out / (P["name"] + ("_9x16.mp4" if not a.no_captions else "_9x16_nocaptions.mp4"))
    if a.no_captions:
        base.replace(final)
        print(f"[4/5][5/5] skipped captions -> {final}")
        return
    print("[4/5] captions from the voice-over timing")
    ass = out / (P["name"] + ".ass")
    lines = Path(P["lines"])
    r = sh([py, HERE / "zc_captions.py", "--lines", lines, "--vo-dir", P["vo_dir"], "--starts", ",".join(f"{k}={v}" for k, v in starts.items()), "--out", ass,
            "--font", P.get("caption_font", "Baloo 2")])
    if r.returncode != 0:
        sys.exit("captions failed")
    print("[5/5] burn captions")
    fonts = str(Path(P.get("fonts_dir", "~/.cache/zero-cost-shorts/fonts")).expanduser())
    r = sh(["ffmpeg", "-v", "error", "-y", "-i", base, "-vf", f"ass={ass}:fontsdir={fonts}", "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p",
            "-c:a", "copy", "-movflags", "+faststart", final])
    if r.returncode != 0:
        sys.exit("caption burn failed")
    print(f"\nDONE {final}  ({total:.1f}s, 9:16)")


if __name__ == "__main__":
    main()
