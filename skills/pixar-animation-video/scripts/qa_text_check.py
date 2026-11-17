#!/usr/bin/env python3
"""Offline QA gate: detect any text, badge or lettering in generated stills or video frames (no API, no cost).

The pack forbids badges, logos, watermarks and any text in the output. This finds them with OCR so that a
generated image/clip can be rejected automatically before it is shown or used.

Setup (once, no account needed):
  uv venv .venv-qa && uv pip install --python .venv-qa/bin/python rapidocr-onnxruntime pillow numpy
Usage:
  .venv-qa/bin/python qa_text_check.py still_s01.png another.png
  .venv-qa/bin/python qa_text_check.py --video clip_s03.mp4 --every 0.5
Exit code 1 if any text above --min-conf is found (or a --forbid term appears); 0 if every input is clean.
Limits: OCR finds legible lettering; it does not judge character identity (that is Claude's visual review).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("images", nargs="*")
    ap.add_argument("--video")
    ap.add_argument("--every", type=float, default=1.0, help="seconds between sampled frames")
    ap.add_argument("--min-conf", type=float, default=0.5)
    ap.add_argument("--forbid", nargs="*", default=["MARVELY", "LYLA"], help="terms that are always reported as BADGE")
    a = ap.parse_args()
    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError:
        sys.exit("rapidocr-onnxruntime is not installed; see the setup line in this file's docstring")
    ocr = RapidOCR()
    items: list[tuple[str, str]] = [(p, p) for p in a.images]
    tmp = None
    if a.video:
        tmp = tempfile.TemporaryDirectory()
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.video, "-vf", f"fps=1/{a.every}", f"{tmp.name}/f_%04d.png"], check=True)
        for i, f in enumerate(sorted(Path(tmp.name).glob("f_*.png"))):
            items.append((str(f), f"{a.video} @ ~{i * a.every:.1f}s"))
    if not items:
        sys.exit("nothing to check")
    bad = 0
    for path, label in items:
        res, _ = ocr(path)
        found = [(t, float(c)) for _, t, c in (res or []) if float(c) >= a.min_conf]
        badge = [t for t, _ in found if any(term.upper() in t.upper() for term in a.forbid)]
        if found:
            bad += 1
            print(f"[REJECT] {label}: {len(found)} text item(s): {[t for t, _ in found][:6]}" + (f"  <- BADGE/FORBIDDEN TERM: {badge}" if badge else ""))
        else:
            print(f"[clean ] {label}")
    print(f"\n{len(items) - bad}/{len(items)} clean, {bad} rejected")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
