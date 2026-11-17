#!/usr/bin/env python3
"""One-time, free setup for the zero-cost Shorts kit. No account, no API key, no payment.

  python3 zc_setup.py            # create venvs, download the free models/fonts (once), verify
  python3 zc_setup.py --check    # read-only status report (what is installed, what each part costs and its limits)

Everything is stored under ~/.cache/zero-cost-shorts (outside the repo). Downloads come from public GitHub URLs only.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

CACHE = Path.home() / ".cache/zero-cost-shorts"
GH = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0"
RAW = "https://raw.githubusercontent.com"
ASSETS = [  # (relative path, url, expected size or None)
    ("models/kokoro-v1.0.onnx", f"{GH}/kokoro-v1.0.onnx", 325532387),
    ("models/voices-v1.0.bin", f"{GH}/voices-v1.0.bin", 28214398),
    ("models/sr/EDSR_x4.pb", f"{RAW}/Saafke/EDSR_Tensorflow/master/models/EDSR_x4.pb", 38573255),
    ("models/sr/EDSR_x2.pb", f"{RAW}/Saafke/EDSR_Tensorflow/master/models/EDSR_x2.pb", 38490162),
    ("fonts/Baloo2.ttf", f"{RAW}/google/fonts/main/ofl/baloo2/Baloo2%5Bwght%5D.ttf", None),
    ("fonts/Baloo2-OFL.txt", f"{RAW}/google/fonts/main/ofl/baloo2/OFL.txt", None),
]
MAIN_PKGS = ["kokoro-onnx", "soundfile", "numpy<2.1", "pillow", "scipy", "opencv-contrib-python-headless==4.10.0.84"]
QA_PKGS = ["rapidocr-onnxruntime", "pillow", "numpy"]

LICENSES = [  # component, what it does, license, cost, usage limit
    ("FFmpeg (system)", "animation encode, mixing, captions, assembly", "LGPL/GPL (build is GPL-enabled)", "free", "none"),
    ("Kokoro-82M via kokoro-onnx", "English narration (54 voices)", "model Apache-2.0, code MIT", "free", "none (runs on your CPU)"),
    ("EDSR super-resolution", "enlarges official sprites 4x", "Apache-2.0", "free", "none"),
    ("Baloo 2 font", "kid-friendly captions", "SIL OFL 1.1", "free", "none"),
    ("RapidOCR (onnxruntime)", "detects any text/badge in frames", "Apache-2.0", "free", "none"),
    ("numpy synthesis (zc_audio.py)", "music, ambience, SFX (original, synthesised)", "our code; no samples used", "free", "none; no licensing issue"),
    ("Pillow / OpenCV / SciPy", "sprite cut-out and compositing", "HPND / Apache-2.0 / BSD", "free", "none"),
    ("Official master sheets (your library)", "the ONLY character artwork used", "your IP", "free", "approved characters only (library gate)"),
]


def download(rel: str, url: str, size: int | None) -> str:
    p = CACHE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and (size is None or p.stat().st_size == size):
        return "ok (cached)"
    urllib.request.urlretrieve(url, p)
    if size is not None and p.stat().st_size != size:
        raise SystemExit(f"{rel}: size {p.stat().st_size} != expected {size}")
    return "downloaded"


def venv(name: str, pkgs: list[str]) -> Path:
    d = CACHE / name
    if not (d / "bin/python").exists():
        subprocess.run(["uv", "venv", "-q", str(d)], check=True) if shutil.which("uv") else subprocess.run([sys.executable, "-m", "venv", str(d)], check=True)
    inst = ["uv", "pip", "install", "-q", "--python", str(d / "bin/python")] if shutil.which("uv") else [str(d / "bin/pip"), "install", "-q"]
    subprocess.run(inst + pkgs, check=True)
    return d / "bin/python"


def check() -> int:
    bad = 0
    print("== files")
    for rel, _, size in ASSETS:
        p = CACHE / rel
        ok = p.exists() and (size is None or p.stat().st_size == size)
        bad += not ok
        print(f"  [{'OK' if ok else 'MISSING'}] {rel}")
    print("== ffmpeg filters")
    out = subprocess.run(["ffmpeg", "-hide_banner", "-filters"], capture_output=True, text=True).stdout if shutil.which("ffmpeg") else ""
    for f in ("ass", "drawtext", "zoompan", "overlay", "xfade", "sidechaincompress", "subtitles"):
        ok = f" {f} " in out
        bad += not ok
        print(f"  [{'OK' if ok else 'MISSING'}] {f}")
    print("== venvs")
    for v in ("venv", "venv-qa"):
        ok = (CACHE / v / "bin/python").exists()
        bad += not ok
        print(f"  [{'OK' if ok else 'MISSING'}] {v}")
    print("\n== cost and limits (verify before use: everything below is local and free)")
    print(f"  {'component':36} {'license':34} {'cost':6} usage limit")
    for c, _, lic, cost, lim in LICENSES:
        print(f"  {c:36} {lic:34} {cost:6} {lim}")
    print("\n  No API key, account, card or paid service is used anywhere in this kit.")
    return 1 if bad else 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        sys.exit(check())
    for rel, url, size in ASSETS:
        print(f"{rel}: {download(rel, url, size)}")
    print("venv:", venv("venv", MAIN_PKGS))
    print("venv-qa:", venv("venv-qa", QA_PKGS))
    sys.exit(check())


if __name__ == "__main__":
    main()
