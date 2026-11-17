#!/usr/bin/env python3
"""Zero-cost scene renderer (no API, no GPU): official sprites + procedural storybook background -> mp4 via FFmpeg.

  python3 zc_render.py spec.json --scene s01 --out clips/s01.mp4          # render one scene (silent)
  python3 zc_render.py spec.json --scene s05 --still 2.5 --out preview.png # one frame, to check the composition

The spec (see templates/) lists sprites (cut from APPROVED master sheets by zc_sprites.py), their keyframes, pose
switches, effects (egg glow, sparkles), and the camera. Characters are only ever the official artwork: nothing is
redrawn, so identity cannot drift. Output is 9:16 (720x1280) at 24 fps by default.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 720, 1280
MARGIN = 1.25                      # world is MARGIN x the screen, so the camera can zoom/pan without empty edges
WW, WH = int(W * MARGIN), int(H * MARGIN)
OX, OY = (WW - W) // 2, (WH - H) // 2


# ----------------------------------------------------------------------------- helpers
def smooth(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def interp(keys: list[dict], t: float, prop: str, default: float) -> float:
    pts = [(k["t"], k[prop]) for k in keys if prop in k]
    if not pts:
        return default
    if t <= pts[0][0]:
        return pts[0][1]
    for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
        if t <= t1:
            return v0 + (v1 - v0) * smooth((t - t0) / max(t1 - t0, 1e-6))
    return pts[-1][1]


def vgrad(w: int, h: int, stops: list[tuple[float, tuple[int, int, int]]]) -> np.ndarray:
    ys = np.linspace(0, 1, h)
    out = np.zeros((h, w, 3), np.float32)
    for c in range(3):
        out[:, :, c] = np.interp(ys, [s[0] for s in stops], [s[1][c] for s in stops])[:, None]
    return out


def to_img(a: np.ndarray) -> Image.Image:
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


# ----------------------------------------------------------------------------- procedural background
def tuft(d: ImageDraw.ImageDraw, rng: random.Random, x: float, y: float, n: int, spread: float, hmin: int, hmax: int, greens) -> None:
    for _ in range(n):
        bx = x + rng.uniform(-spread, spread)
        h = rng.uniform(hmin, hmax)
        w = rng.uniform(5, 11)
        lean = rng.uniform(-18, 18)
        c = rng.choice(greens)
        d.polygon([(bx - w, y), (bx + lean, y - h), (bx + w, y)], fill=c + (255,))


def flower(d: ImageDraw.ImageDraw, rng: random.Random, x: float, y: float, r: float) -> None:
    col = rng.choice([(255, 140, 190), (190, 140, 255), (255, 214, 90), (140, 190, 255), (255, 255, 255)])
    for k in range(5):
        a = k * 2 * math.pi / 5 + rng.uniform(0, 1)
        d.ellipse([x + math.cos(a) * r * 0.9 - r * 0.7, y + math.sin(a) * r * 0.9 - r * 0.7, x + math.cos(a) * r * 0.9 + r * 0.7, y + math.sin(a) * r * 0.9 + r * 0.7], fill=col + (255,))
    d.ellipse([x - r * 0.55, y - r * 0.55, x + r * 0.55, y + r * 0.55], fill=(255, 205, 70, 255))


def build_forest(seed: int = 7) -> tuple[np.ndarray, Image.Image]:
    """Returns (back RGB float world image, front RGBA overlay with grass/flowers drawn over the sprites)."""
    rng = random.Random(seed)
    HY = OY + int(0.50 * H)   # horizon (world y)
    fh = HY / WH
    sky = vgrad(WW, WH, [(0, (118, 188, 214)), (fh * 0.55, (176, 222, 206)), (fh - 0.01, (255, 236, 176)), (fh, (172, 214, 128)), (1.0, (58, 136, 72))])
    base = to_img(sky).convert("RGBA")
    # distant hazy trees
    far = Image.new("RGBA", (WW, WH), (0, 0, 0, 0)); d = ImageDraw.Draw(far)
    for i in range(16):
        x = rng.uniform(-40, WW + 40); w = rng.uniform(46, 110); top = OY + rng.uniform(0.02, 0.2) * H
        d.rounded_rectangle([x - w / 4, top + 120, x + w / 4, HY + 20], radius=12, fill=(66, 132, 100, 255))
        for _ in range(6):
            cx = x + rng.uniform(-w, w); cy = top + rng.uniform(0, 160); r = rng.uniform(46, 96)
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(86, 166, 104, 255))
    base.alpha_composite(far.filter(ImageFilter.GaussianBlur(7)), (0, 0))
    base2 = Image.alpha_composite(base, Image.new("RGBA", base.size, (255, 236, 170, 46)))  # warm golden haze
    # light rays from camera-left
    rays = Image.new("RGBA", (WW, WH), (0, 0, 0, 0)); d = ImageDraw.Draw(rays)
    for i in range(6):
        x0 = rng.uniform(-0.1, 0.5) * WW; w = rng.uniform(40, 110)
        d.polygon([(x0, 0), (x0 + w, 0), (x0 + w + 330, HY + 160), (x0 + 120, HY + 160)], fill=(255, 246, 210, 26))
    base2.alpha_composite(rays.filter(ImageFilter.GaussianBlur(42)), (0, 0))
    # mid-distance canopy with leaf clusters (sharper than the haze) and glowing bokeh
    can = Image.new("RGBA", (WW, WH), (0, 0, 0, 0)); d = ImageDraw.Draw(can)
    for _ in range(70):
        cx = rng.uniform(-40, WW + 40); cy = OY + rng.uniform(-0.02, 0.36) * H; r = rng.uniform(26, 70)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=rng.choice([(54, 140, 80, 255), (72, 164, 88, 255), (40, 116, 70, 255), (110, 184, 96, 255)]))
    base2.alpha_composite(can.filter(ImageFilter.GaussianBlur(2.2)), (0, 0))
    bok = Image.new("RGBA", (WW, WH), (0, 0, 0, 0)); d = ImageDraw.Draw(bok)
    for _ in range(46):
        cx = rng.uniform(0, WW); cy = OY + rng.uniform(0.02, 0.5) * H; r = rng.uniform(16, 60)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=rng.choice([(255, 244, 190, 70), (255, 255, 230, 55), (255, 226, 150, 60)]))
    base2.alpha_composite(bok.filter(ImageFilter.GaussianBlur(5)), (0, 0))
    # mid bushes
    mid = Image.new("RGBA", (WW, WH), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
    for i in range(22):
        cx = rng.uniform(-30, WW + 30); cy = HY + rng.uniform(-30, 20); rx = rng.uniform(60, 130); ry = rng.uniform(40, 80)
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(52, 120, 76, 255))
        d.ellipse([cx - rx * 0.7, cy - ry * 0.95, cx + rx * 0.4, cy - ry * 0.1], fill=(96, 164, 92, 255))
    base2.alpha_composite(mid.filter(ImageFilter.GaussianBlur(3.5)), (0, 0))
    arr = np.array(base2.convert("RGB")).astype(np.float32)
    # ground texture
    noise = cv2.GaussianBlur(np.random.default_rng(seed).normal(0, 1, (WH, WW)).astype(np.float32), (0, 0), 14)
    g = (np.arange(WH)[:, None] > HY)
    arr += (noise * 24)[:, :, None] * g[:, :, None] * np.array([0.7, 1.0, 0.5])
    # trunks framing the sides
    tr = Image.new("RGBA", (WW, WH), (0, 0, 0, 0)); d = ImageDraw.Draw(tr)
    for x, w in ((0.02 * WW, 70), (0.97 * WW, 90)):
        d.polygon([(x - w, 0), (x + w, 0), (x + w * 0.7, HY + 60), (x - w * 0.7, HY + 60)], fill=(86, 66, 52, 255))
    tr = tr.filter(ImageFilter.GaussianBlur(5))
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA"); img.alpha_composite(tr, (0, 0))
    # sunlit meadow patches and fine grass texture on the ground
    patch = Image.new("RGBA", (WW, WH), (0, 0, 0, 0)); pd = ImageDraw.Draw(patch)
    for _ in range(9):
        cx = rng.uniform(0.1, 0.9) * WW; cy = HY + rng.uniform(0.1, 0.55) * H; rx = rng.uniform(120, 260); ry = rng.uniform(40, 90)
        pd.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(214, 238, 140, 70))
    img.alpha_composite(patch.filter(ImageFilter.GaussianBlur(30)), (0, 0))
    d = ImageDraw.Draw(img)
    for _ in range(1500):
        bx = rng.uniform(0, WW); by = rng.uniform(HY + 10, OY + H)
        sc = 0.4 + (by - HY) / H * 1.2
        h_ = rng.uniform(8, 20) * sc; c = rng.choice([(74, 156, 76), (104, 180, 84), (50, 120, 62), (132, 196, 92)])
        d.polygon([(bx - 2 * sc, by), (bx + rng.uniform(-4, 4) * sc, by - h_), (bx + 2 * sc, by)], fill=c + (255,))
    # distant flowers on the ground
    for _ in range(90):
        flower(d, rng, rng.uniform(0, WW), rng.uniform(HY + 30, HY + 0.30 * H), rng.uniform(4, 8))
    # FRONT overlay: tall grass + flowers along the bottom (hides sprite cut-edges), leaf corners
    fr = Image.new("RGBA", (WW, WH), (0, 0, 0, 0)); d = ImageDraw.Draw(fr)
    greens = [(46, 128, 62), (66, 150, 70), (90, 174, 80), (36, 104, 56)]
    for row, (y, hmin, hmax, n) in enumerate([(OY + H + 60, 190, 330, 190), (OY + H - 40, 120, 210, 150)]):
        tuft(d, rng, WW / 2, y, n, WW * 0.6, hmin, hmax, greens)
    for _ in range(26):
        flower(d, rng, rng.uniform(0, WW), OY + rng.uniform(0.93, 0.995) * H, rng.uniform(9, 17))
    for cx in (OY * 0 + OX * 0.4, OX + W * 1.0 - OX * 0.4):  # leafy frame at the top corners (on screen)
        for _ in range(9):
            r = rng.uniform(60, 150); px = cx + rng.uniform(-70, 130) * (1 if cx < WW / 2 else -1); py = OY + rng.uniform(-40, 120)
            d.ellipse([px - r, py - r, px + r, py + r], fill=rng.choice([(36, 108, 58, 240), (52, 134, 70, 240), (28, 90, 52, 240)]))
    return np.array(img.convert("RGB")).astype(np.float32), fr


def make_rock(w: int, h: int, seed: int = 3) -> Image.Image:
    rng = random.Random(seed)
    # dome silhouette (super-ellipse) with slight irregularity
    pts = []
    for k in range(60):
        a = math.pi + k * math.pi / 59
        r = 1 + rng.uniform(-0.035, 0.035)
        pts.append((w / 2 + math.copysign(abs(math.cos(a)) ** 0.8, math.cos(a)) * w / 2 * r, h + math.sin(a) * h * r * 0.98))
    mask = Image.new("L", (w, h), 0); ImageDraw.Draw(mask).polygon(pts + [(w, h), (0, h)], fill=255)
    yy, xx = np.mgrid[0:h, 0:w]
    light = np.clip(1.05 - (xx / w) * 0.45 - (yy / h) * 0.30, 0.45, 1.05)[:, :, None]
    base = np.array([150, 144, 130], np.float32) * light
    noise = cv2.GaussianBlur(np.random.default_rng(seed).normal(0, 1, (h, w)).astype(np.float32), (0, 0), 3)[:, :, None] * 14
    rockc = np.clip(base + noise, 0, 255)
    # moss cap with an irregular boundary
    edge = (0.34 + 0.08 * np.sin(xx / 17.0) + 0.05 * np.sin(xx / 7.3 + 1.1)) * h
    mossmask = np.clip((edge - yy) / 7.0, 0, 1)[:, :, None]
    mosc = np.array([96, 156, 70], np.float32) * (0.85 + 0.25 * light) + np.random.default_rng(seed + 1).normal(0, 9, (h, w, 1))
    rockc = rockc * (1 - mossmask) + mosc * mossmask
    out = np.dstack([np.clip(rockc, 0, 255), np.array(mask)]).astype(np.uint8)
    return Image.fromarray(out).filter(ImageFilter.GaussianBlur(0.7))


def star_sprite(size: int = 64) -> np.ndarray:
    a = np.zeros((size, size), np.float32); c = size / 2
    yy, xx = np.mgrid[0:size, 0:size]
    dx, dy = np.abs(xx - c) / c, np.abs(yy - c) / c
    a = np.clip(1 - (dx ** 0.5 + dy ** 0.5) ** 2 * 0.9, 0, 1) ** 2
    a += np.clip(1 - np.sqrt(dx * dx + dy * dy) * 2.2, 0, 1)
    return np.clip(a, 0, 1)


def glow_sprite(size: int = 512) -> np.ndarray:
    yy, xx = np.mgrid[0:size, 0:size]
    r = np.sqrt((xx - size / 2) ** 2 + (yy - size / 2) ** 2) / (size / 2)
    return np.clip(1 - r, 0, 1) ** 2.2


# ----------------------------------------------------------------------------- sprites
class Sprites:
    def __init__(self, folder: Path):
        self.dir = folder
        self.manifest = json.loads((folder / "manifest.json").read_text())["sprites"]
        self.cache: dict[tuple, np.ndarray] = {}

    def native_h(self, sid: str) -> int:
        return self.manifest[sid]["native_size"][1]

    def get(self, sid: str, height: int, crop_bottom: float = 0.0, flip: bool = False) -> np.ndarray:
        key = (sid, height, round(crop_bottom, 3), flip)
        if key in self.cache:
            return self.cache[key]
        im = Image.open(self.dir / self.manifest[sid]["file"]).convert("RGBA")
        if crop_bottom:
            im = im.crop((0, 0, im.width, int(im.height * (1 - crop_bottom))))
            a = np.array(im); ramp = int(im.height * 0.08)
            a[-ramp:, :, 3] = (a[-ramp:, :, 3] * np.linspace(1, 0, ramp)[:, None]).astype(np.uint8)
            im = Image.fromarray(a)
        if flip:
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
        w = max(1, int(im.width * height / im.height))
        arr = np.array(im.resize((w, int(height)), Image.LANCZOS))
        self.cache[key] = arr
        return arr


def blit(world: np.ndarray, spr: np.ndarray, x: float, y: float, scale: float = 1.0, rot: float = 0.0, alpha: float = 1.0, sy: float = 1.0) -> None:
    """Alpha-blend a sprite anchored at its bottom-centre onto the world at (x, y) (world px)."""
    if alpha <= 0.003:
        return
    h, w = spr.shape[:2]
    A = np.vstack([cv2.getRotationMatrix2D((w / 2, h), -rot, 1.0), [0, 0, 1]]).astype(np.float32)
    B = np.array([[scale, 0, 0], [0, scale * sy, 0], [0, 0, 1]], np.float32)
    Tm = B @ A
    ax, ay = (Tm @ np.array([w / 2, h, 1], np.float32))[:2]
    Tm[0, 2] += x - ax
    Tm[1, 2] += y - ay
    T = Tm[:2]
    corners = np.array([[0, 0, 1], [w, 0, 1], [w, h, 1], [0, h, 1]], np.float32) @ T.T
    x0, y0 = int(max(0, math.floor(corners[:, 0].min()))), int(max(0, math.floor(corners[:, 1].min())))
    x1, y1 = int(min(WW, math.ceil(corners[:, 0].max()))), int(min(WH, math.ceil(corners[:, 1].max())))
    if x1 <= x0 or y1 <= y0:
        return
    T2 = T.copy()
    T2[:, 2] -= [x0, y0]
    warped = cv2.warpAffine(spr, T2, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    a = (warped[:, :, 3:4].astype(np.float32) / 255.0) * alpha
    world[y0:y1, x0:x1] = world[y0:y1, x0:x1] * (1 - a) + warped[:, :, :3].astype(np.float32) * a


def soft_shadow(world: np.ndarray, x: float, y: float, w: float, strength: float = 0.32) -> None:
    ww, hh = int(w), max(6, int(w * 0.16))
    yy, xx = np.mgrid[0:hh, 0:ww]
    a = np.clip(1 - np.sqrt(((xx - ww / 2) / (ww / 2)) ** 2 + ((yy - hh / 2) / (hh / 2)) ** 2), 0, 1) ** 0.8 * strength
    x0, y0 = int(x - ww / 2), int(y - hh / 2)
    xs0, ys0 = max(0, x0), max(0, y0); xs1, ys1 = min(WW, x0 + ww), min(WH, y0 + hh)
    if xs1 <= xs0 or ys1 <= ys0:
        return
    sub = a[ys0 - y0:ys1 - y0, xs0 - x0:xs1 - x0][:, :, None]
    world[ys0:ys1, xs0:xs1] *= (1 - sub * np.array([0.55, 0.6, 0.5]))


# ----------------------------------------------------------------------------- scene
def render_frame(spec: dict, scene: dict, t: float, ctx: dict) -> np.ndarray:
    world = ctx["back"].copy()
    units = spec.get("units", {})
    sprites: Sprites = ctx["sprites"]
    # gather drawables with z
    items = []
    for L in scene.get("layers", []):
        keys = L.get("keys", [])
        x = interp(keys, t, "x", L.get("x", 360)); y = interp(keys, t, "y", L.get("y", 960))
        sc = interp(keys, t, "scale", 1.0); rot = interp(keys, t, "rot", 0.0); al = interp(keys, t, "alpha", 1.0)
        phase = L.get("phase", 0.0)
        bob = L.get("bob")
        sy = 1.0
        if bob:
            s = math.sin(2 * math.pi * bob.get("freq", 2.0) * t + phase)
            if bob.get("active_from", 0) <= t <= bob.get("active_to", 1e9):
                y -= bob.get("amp", 6) * abs(s)
                rot += bob.get("rot", 0) * s
                sy += bob.get("squash", 0) * (1 - abs(s) * 2) * 0.5
        breathe = L.get("breathe", 0.012)
        sy += breathe * math.sin(2 * math.pi * 0.7 * t + phase)
        sy *= interp(keys, t, "stretch", 1.0)
        L_items = []
        if L["type"] == "sprite":
            poses = L["poses"]
            # active pose(s) with crossfade
            cur = None
            for i, p in enumerate(poses):
                if t >= p.get("t", 0):
                    cur = i
            cur = 0 if cur is None else cur
            fade = L.get("crossfade", 0.18)
            draw_list = [(poses[cur], 1.0)]
            if cur > 0 and t - poses[cur].get("t", 0) < fade:
                f = smooth((t - poses[cur].get("t", 0)) / fade)
                draw_list = [(poses[cur - 1], 1 - f), (poses[cur], f)]
            for p, wgt in draw_list:
                if "height" in p:
                    hpx = p["height"]
                elif "height_ratio" in p:  # e.g. the egg vs Rico, exactly as the sheet's own comparison panel draws them
                    hr = p["height_ratio"]
                    hpx = hr["of"] * sprites.native_h(hr["num"]) / sprites.native_h(hr["den"])
                elif "panel_scale" in p:  # proportions as drawn on the sheet's comparison panel
                    hpx = sprites.native_h(p["sprite"]) * units["rico_ref_height_px"] / sprites.native_h(units["rico_ref_sprite"]) * p.get("rel", 1.0)
                else:
                    hpx = 300
                spr = sprites.get(p["sprite"], int(hpx), p.get("crop_bottom", 0.0), p.get("flip", False))
                L_items.append((L.get("z", 5), spr, x + OX + p.get("dx", 0), y + OY + p.get("dy", 0), sc, rot, al * wgt, sy, L.get("shadow", True)))
        elif L["type"] == "rock":
            rk = ctx["rock"]
            L_items.append((L.get("z", 6), rk, x + OX, y + OY, 1.0, 0.0, al, 1.0, False))
        items += L_items
    items.sort(key=lambda it: it[0])
    for z, spr, x, y, sc, rot, al, sy, shadow in items:
        if shadow and al > 0.2:
            soft_shadow(world, x, y, spr.shape[1] * sc * 0.75, 0.30 * al)
        blit(world, spr, x, y, sc, rot, al, sy)
    # effects
    for E in scene.get("effects", []):
        k = E.get("keys", [])
        if E["type"] == "glow":
            inten = interp(k, t, "intensity", 0.5)
            pulse = 1 + 0.08 * math.sin(2 * math.pi * 0.9 * t)
            gs = ctx["glow"]; r = int(E.get("radius", 260) * pulse * MARGIN)
            g = cv2.resize(gs, (2 * r, 2 * r), interpolation=cv2.INTER_LINEAR)
            cx, cy = int(E["x"] + OX), int(E["y"] + OY)
            x0, y0 = max(0, cx - r), max(0, cy - r); x1, y1 = min(WW, cx + r), min(WH, cy + r)
            if x1 > x0 and y1 > y0:
                sub = g[y0 - (cy - r):y1 - (cy - r), x0 - (cx - r):x1 - (cx - r)][:, :, None] * inten
                tint = np.array(E.get("color", (255, 236, 170)), np.float32)
                world[y0:y1, x0:x1] = world[y0:y1, x0:x1] * (1 - sub * 0.35) + tint * sub * 0.9 + world[y0:y1, x0:x1] * sub * 0.0
        elif E["type"] == "sparkles":
            inten = interp(k, t, "intensity", 0.6)
            rng = random.Random(E.get("seed", 1)); st = ctx["star"]
            for i in range(E.get("count", 24)):
                a0 = rng.uniform(0, 2 * math.pi); rad = rng.uniform(0.35, 1.0) * E.get("radius", 220); spd = rng.uniform(-0.25, 0.25)
                ph = rng.uniform(0, 1); size = int(rng.uniform(14, 34) * (1 + inten))
                ang = a0 + spd * t * 2 * math.pi
                px = E["x"] + math.cos(ang) * rad * 1.0 + OX; py = E["y"] + math.sin(ang) * rad * 0.8 - (t * 14 * rng.uniform(0.3, 1) % 80) + OY
                tw = 0.5 + 0.5 * math.sin(2 * math.pi * (1.2 * t + ph))
                a = tw * min(1.0, inten * 1.3)
                s2 = cv2.resize(st, (size, size))[:, :, None]
                x0, y0 = int(px - size / 2), int(py - size / 2)
                if 0 <= x0 < WW - size and 0 <= y0 < WH - size:
                    tint = np.array(rng.choice([(255, 240, 190), (255, 200, 240), (190, 235, 255)]), np.float32)
                    world[y0:y0 + size, x0:x0 + size] = np.clip(world[y0:y0 + size, x0:x0 + size] + tint * s2 * a * 0.9, 0, 255)
    # foreground (grass/flowers over the sprites)
    fg = ctx["front"]
    a = fg[:, :, 3:4].astype(np.float32) / 255.0
    world = world * (1 - a) + fg[:, :, :3].astype(np.float32) * a
    # camera
    cam = scene.get("camera", {}).get("keys", [])
    z = interp(cam, t, "zoom", 1.0); cx = W / 2 + interp(cam, t, "x", 0.0) + OX; cy = H / 2 + interp(cam, t, "y", 0.0) + OY
    cw, ch = W / z, H / z
    M = np.array([[W / cw, 0, -(cx - cw / 2) * W / cw], [0, H / ch, -(cy - ch / 2) * H / ch]], np.float32)
    frame = cv2.warpAffine(world.astype(np.float32), M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    # grade: gentle vignette + warmth
    yy, xx = np.mgrid[0:H, 0:W]
    v = 1 - 0.20 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    frame = frame * v[:, :, None] * np.array([1.03, 1.0, 0.97])
    return np.clip(frame, 0, 255).astype(np.uint8)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("--scene", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--still", type=float, help="render a single PNG frame at this time instead of a video")
    ap.add_argument("--fps", type=int)
    a = ap.parse_args()
    spec = json.loads(Path(a.spec).read_text())
    scene = next(s for s in spec["scenes"] if s["id"] == a.scene)
    fps = a.fps or spec.get("fps", 24)
    root = Path(a.spec).resolve()
    sprites = Sprites(Path(spec["sprites_dir"]))
    back, front = build_forest(spec.get("seed", 7))
    rk = scene.get("rock") or spec.get("rock", {"w": 330, "h": 190})
    ctx = {"back": back, "front": np.array(front), "sprites": sprites, "rock": np.array(make_rock(int(rk["w"]), int(rk["h"]))),
           "glow": glow_sprite(), "star": star_sprite()}
    if a.still is not None:
        Image.fromarray(render_frame(spec, scene, a.still, ctx)).save(a.out)
        print("still ->", a.out)
        return
    n = int(round(scene["duration"] * fps))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", "-c:v", "libx264",
                           "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "medium", "-movflags", "+faststart", a.out], stdin=subprocess.PIPE)
    for i in range(n):
        ff.stdin.write(render_frame(spec, scene, i / fps, ctx).tobytes())
    ff.stdin.close()
    if ff.wait() != 0:
        sys.exit("ffmpeg failed")
    print(f"{a.scene}: {n} frames, {scene['duration']}s -> {a.out}")


if __name__ == "__main__":
    main()
