#!/usr/bin/env python3
"""Cut animation sprites out of APPROVED master sheets (offline, free, no API).

Why: with no paid or GPU generator, the only way to keep every character exactly on-model is to reuse the
official artwork on the master sheets. This tool cuts the characters out of their sheet panels, enlarges them with the
open-source EDSR super-resolution model (Apache-2.0), cleans the edge fringe, and records provenance.

  python3 zc_sprites.py sprite-boxes/rico-and-friends.json --out outputs/zero-cost/rico-and-friends/sprites [--scale 4]

Rules enforced:
  * every character used must pass ./scripts/check-character-library.sh <Project> --character <Name>  (approved only)
  * original sheets are only READ; output sprites are new files (derived working copies) with sha256 provenance
Needs: pillow numpy scipy opencv-contrib-python-headless==4.10.* and the EDSR models (run zc_setup.py).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

MODELS = Path.home() / ".cache/zero-cost-shorts/models/sr"


def repo_root() -> Path:
    d = Path(__file__).resolve()
    for p in d.parents:
        if (p / "CLAUDE.md").is_file() and (p / "references").is_dir():
            return p
    return Path.cwd()


def cut(sheet: Image.Image, box, tol: float = 9.0, min_part: float = 0.25, bg_xy=None) -> Image.Image | None:
    """Flood-fill the panel background from the crop border (Lab distance), keep the main component(s), fill holes."""
    crop = np.array(sheet.crop(tuple(box))).astype(np.uint8)
    lab = cv2.cvtColor(crop, cv2.COLOR_RGB2LAB).astype(np.float32)
    edge = np.concatenate([lab[:3].reshape(-1, 3), lab[-3:].reshape(-1, 3), lab[:, :3].reshape(-1, 3), lab[:, -3:].reshape(-1, 3)])
    bg = np.median(edge, axis=0)
    if bg_xy:  # sample the panel colour from a known empty point instead of the (possibly crowded) crop border
        px = np.array(sheet.crop((bg_xy[0] - 2, bg_xy[1] - 2, bg_xy[0] + 3, bg_xy[1] + 3))).astype(np.uint8)
        bg = np.median(cv2.cvtColor(px, cv2.COLOR_RGB2LAB).astype(np.float32).reshape(-1, 3), axis=0)
    cand = np.linalg.norm(lab - bg, axis=2) < tol
    lbl, _ = ndi.label(cand)
    border = set(np.unique(np.concatenate([lbl[0], lbl[-1], lbl[:, 0], lbl[:, -1]]))) - {0}
    fg = ~np.isin(lbl, list(border))
    fg = ndi.binary_opening(fg, iterations=2)  # removes thin dashed lines / label fragments
    lf, m = ndi.label(fg)
    if m == 0:
        return None
    sizes = ndi.sum(fg, lf, range(1, m + 1))
    fg = np.isin(lf, [i + 1 for i, s in enumerate(sizes) if s >= min_part * sizes.max()])
    fg = ndi.binary_fill_holes(fg)
    alpha = np.clip(cv2.GaussianBlur(ndi.binary_erosion(fg, iterations=1).astype(np.float32), (0, 0), 0.9), 0, 1)
    ys, xs = np.where(alpha > 0.05)
    rgba = np.dstack([crop, (alpha * 255).astype(np.uint8)])
    return Image.fromarray(rgba).crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))


def grabcut_cut(sheet: Image.Image, box, rect, iters: int = 6) -> Image.Image | None:
    """For objects on a photographic/blurred background (e.g. the Rainbow Egg): GrabCut seeded with a rectangle
    (x,y,w,h inside the crop), then keep the largest blob and soften the edge."""
    crop = np.array(sheet.crop(tuple(box))).astype(np.uint8)
    bgr = cv2.cvtColor(crop, cv2.COLOR_RGB2BGR)
    mask = np.zeros(bgr.shape[:2], np.uint8)
    cv2.grabCut(bgr, mask, tuple(rect), np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64), iters, cv2.GC_INIT_WITH_RECT)
    fg = (mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD)
    lf, m = ndi.label(fg)
    if m == 0:
        return None
    sizes = ndi.sum(fg, lf, range(1, m + 1))
    fg = ndi.binary_fill_holes(lf == (1 + int(np.argmax(sizes))))
    fg = ndi.binary_opening(fg, iterations=2)
    alpha = np.clip(cv2.GaussianBlur(ndi.binary_erosion(fg, iterations=1).astype(np.float32), (0, 0), 1.1), 0, 1)
    ys, xs = np.where(alpha > 0.05)
    return Image.fromarray(np.dstack([crop, (alpha * 255).astype(np.uint8)])).crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))


def decontaminate(rgb: np.ndarray, alpha: np.ndarray) -> np.ndarray:
    """Replace edge colours (which still carry the light panel colour) with the nearest fully opaque interior colour."""
    interior = ndi.binary_erosion(alpha > 245, iterations=2)
    if not interior.any():
        return rgb
    idx = ndi.distance_transform_edt(~interior, return_distances=False, return_indices=True)
    return rgb[idx[0], idx[1]]


def superres(img: Image.Image, scale: int) -> Image.Image:
    if scale == 1:
        return img
    a = np.array(img)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(str(MODELS / f"EDSR_x{scale}.pb"))
    sr.setModel("edsr", scale)
    al = a[:, :, 3:4] / 255.0
    base = cv2.cvtColor((a[:, :, :3] * al + 128 * (1 - al)).astype(np.uint8), cv2.COLOR_RGB2BGR)
    up = cv2.cvtColor(sr.upsample(base), cv2.COLOR_BGR2RGB)
    alpha = cv2.resize(a[:, :, 3], (up.shape[1], up.shape[0]), interpolation=cv2.INTER_CUBIC)
    up = decontaminate(up, alpha)
    return Image.fromarray(np.dstack([up, alpha]))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("boxes")
    ap.add_argument("--out", required=True)
    ap.add_argument("--scale", type=int, default=4, choices=[1, 2, 4])
    ap.add_argument("--skip-gate", action="store_true", help="NOT for production: skips the approved-character gate")
    a = ap.parse_args()
    root = repo_root()
    spec = json.loads(Path(a.boxes).read_text())
    project = spec["project"]
    if not a.skip_gate:
        for name in sorted({s["character"] for s in spec["sprites"]}):
            r = subprocess.run([str(root / "scripts/check-character-library.sh"), project, "--character", name], capture_output=True, text=True, cwd=root)
            if r.returncode != 0:
                sys.exit(f"GATE FAIL for {project}:{name}: only APPROVED characters may be used.\n{r.stdout[-300:]}")
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    sheets = {k: Image.open(root / v).convert("RGB") for k, v in spec["sheets"].items()}
    shas = {k: hashlib.sha256((root / v).read_bytes()).hexdigest() for k, v in spec["sheets"].items()}
    manifest = {"project": project, "scale": a.scale, "note": "derived working copies; originals untouched", "sprites": {}}
    for s in spec["sprites"]:
        im = grabcut_cut(sheets[s["sheet"]], s["box"], s["grabcut_rect"]) if s.get("grabcut_rect") else cut(sheets[s["sheet"]], s["box"], tol=s.get("tol", 9.0), min_part=s.get("min_part", 0.25), bg_xy=s.get("bg_xy"))
        if im is None:
            print(f"[skip] {s['id']}: nothing found")
            continue
        up = superres(im, a.scale)
        p = out / f"{s['id']}.png"
        up.save(p)
        manifest["sprites"][s["id"]] = {"character": s["character"], "file": p.name, "size": list(up.size), "source_sheet": spec["sheets"][s["sheet"]],
                                       "source_sheet_sha256": shas[s["sheet"]], "box": s["box"], "native_size": list(im.size), "role": s.get("role", "sprite")}
        print(f"[ok] {s['id']:18} {im.size} -> {up.size}")
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    for k, v in shas.items():  # prove originals unchanged
        assert hashlib.sha256((root / spec["sheets"][k]).read_bytes()).hexdigest() == v
    print(f"\n{len(manifest['sprites'])} sprites -> {out}  (source sheets verified unchanged)")


if __name__ == "__main__":
    main()
