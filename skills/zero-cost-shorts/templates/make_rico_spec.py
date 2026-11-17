#!/usr/bin/env python3
"""Generates templates/rico-telur-pelangi.json (the 6-clip 'Telur Pelangi' short). Edit positions here, re-run, re-render."""
import json, sys
from pathlib import Path

EGG = (455, 960); ROCK = (190, 935); RICO = (300, 985)
EGG_H = {"height_ratio": {"of": 300, "num": "egg_size_solo", "den": "rico_size_solo"}}
def friend(sprite, flip=True, **kw): return dict(sprite=sprite, panel_scale=True, flip=flip, **kw)

def egg_layer():
    return {"id": "egg", "type": "sprite", "z": 5, "x": EGG[0], "y": EGG[1], "breathe": 0.0, "poses": [dict(sprite="rainbow_egg", **EGG_H)]}  # the egg never moves by itself
def rock_layer(): return {"id": "rock", "type": "rock", "z": 6, "x": ROCK[0], "y": ROCK[1]}
def rico(poses, keys=None, **kw): return dict({"id": "rico", "type": "sprite", "z": 7, "x": RICO[0], "y": RICO[1], "poses": poses, "keys": keys or []}, **kw)
def glow(keys): return {"type": "glow", "x": EGG[0], "y": EGG[1] - 160, "radius": 300, "keys": keys}
def sparks(keys, n=22, seed=3): return {"type": "sparkles", "x": EGG[0], "y": EGG[1] - 170, "radius": 230, "count": n, "seed": seed, "keys": keys}

scenes = []
# S01 -- Rico peeks over the rock, spots the egg, steps toward it (8 s)
scenes.append({"id": "s01", "duration": 8, "camera": {"keys": [{"t": 0, "zoom": 1.0, "x": 0, "y": 0}, {"t": 8, "zoom": 1.10, "x": 30, "y": -10}]},
  "layers": [egg_layer(),
    {"id": "rico_peek", "type": "sprite", "z": 4, "x": ROCK[0] + 10, "y": 900, "breathe": 0.01,
     "poses": [dict(sprite="rico_peek", height=205, crop_bottom=0.27)],
     "keys": [{"t": 0, "y": 905, "alpha": 1}, {"t": 1.5, "y": 782}, {"t": 2.0, "y": 782, "rot": 0}, {"t": 2.3, "alpha": 1}, {"t": 2.8, "alpha": 0, "y": 790}],
     "bob": {"amp": 0, "rot": 3.0, "freq": 0.9, "active_from": 1.5, "active_to": 2.6}},
    rock_layer(),
    rico([dict(t=0, sprite="rico_surprised", height=265, flip=True), dict(t=4.0, sprite="rico_34front", height=292, flip=True)],
         keys=[{"t": 0, "alpha": 0, "x": 215}, {"t": 2.2, "alpha": 0, "x": 215}, {"t": 2.7, "alpha": 1, "x": 220}, {"t": 3.2, "x": 225}, {"t": 6.2, "x": RICO[0]}, {"t": 8, "x": RICO[0]}],
         bob={"amp": 9, "rot": 3.2, "freq": 2.0, "active_from": 3.3, "active_to": 6.3})],
  "effects": [glow([{"t": 0, "intensity": 0.18}, {"t": 8, "intensity": 0.32}]), sparks([{"t": 0, "intensity": 0.25}, {"t": 8, "intensity": 0.4}], 12)]})
# S02 -- Piko glides in and hovers; Rico waves up at Piko (4 s)
scenes.append({"id": "s02", "duration": 4, "camera": {"keys": [{"t": 0, "zoom": 1.06, "x": 40, "y": 10}, {"t": 4, "zoom": 1.10, "x": 50, "y": 0}]},
  "layers": [egg_layer(), rock_layer(), rico([dict(sprite="rico_wave", height=282, flip=True)]),
    {"id": "piko", "type": "sprite", "z": 9, "x": 585, "y": 640, "phase": 1.0, "poses": [friend("piko_size_panel")],
     "keys": [{"t": 0, "x": 830, "y": 90}, {"t": 1.7, "x": 585, "y": 650}, {"t": 4, "x": 585, "y": 650}],
     "bob": {"amp": 14, "rot": 4, "freq": 1.5, "active_from": 1.7, "active_to": 9}}],
  "effects": [glow([{"t": 0, "intensity": 0.35}, {"t": 4, "intensity": 0.45}]), sparks([{"t": 0, "intensity": 0.4}, {"t": 4, "intensity": 0.5}], 16)]})
# S03 -- Lila and Bimo walk in from the right; Rico smiles (4 s)
scenes.append({"id": "s03", "duration": 4, "camera": {"keys": [{"t": 0, "zoom": 1.08, "x": 30, "y": 30}, {"t": 4, "zoom": 1.08, "x": 30, "y": 30}]},
  "layers": [egg_layer(), rock_layer(), rico([dict(sprite="rico_front", height=300)]),
    {"id": "lila", "type": "sprite", "z": 9, "x": 540, "y": 1012, "phase": 0.5, "poses": [friend("lila_size_panel")],
     "keys": [{"t": 0, "x": 860}, {"t": 2.0, "x": 540}, {"t": 4, "x": 540}], "bob": {"amp": 10, "rot": 4, "freq": 2.2, "active_from": 0, "active_to": 2.1}},
    {"id": "bimo", "type": "sprite", "z": 8, "x": 610, "y": 1058, "phase": 0.0, "poses": [friend("bimo_size_panel")],
     "keys": [{"t": 0, "x": 960}, {"t": 2.3, "x": 610}, {"t": 4, "x": 610}], "bob": {"amp": 10, "rot": 4, "freq": 2.2, "active_from": 0, "active_to": 2.4}}],
  "effects": [glow([{"t": 0, "intensity": 0.45}, {"t": 4, "intensity": 0.5}]), sparks([{"t": 0, "intensity": 0.45}, {"t": 4, "intensity": 0.5}], 16)]})
# S04 -- Tika walks in behind the egg and stretches up to peek; Rico looks up, smiling (4 s)
scenes.append({"id": "s04", "duration": 4, "camera": {"keys": [{"t": 0, "zoom": 1.08, "x": 20, "y": -40}, {"t": 4, "zoom": 1.13, "x": 30, "y": -70}]},
  "layers": [{"id": "tika", "type": "sprite", "z": 3, "x": 548, "y": 935, "phase": 0.3, "poses": [friend("tika_size_panel")],
              "keys": [{"t": 0, "x": 900}, {"t": 1.6, "x": 548}, {"t": 4, "x": 548}, {"t": 0, "stretch": 1.0}, {"t": 2.0, "stretch": 1.0}, {"t": 3.2, "stretch": 1.07}, {"t": 4, "stretch": 1.07}, {"t": 0, "rot": 0}, {"t": 2.0, "rot": 0}, {"t": 3.4, "rot": -4}],
              "bob": {"amp": 6, "rot": 2, "freq": 1.9, "active_from": 0, "active_to": 1.7}},
             egg_layer(), rock_layer(), rico([dict(sprite="rico_wave", height=282, flip=True)])],
  "effects": [glow([{"t": 0, "intensity": 0.5}, {"t": 4, "intensity": 0.55}]), sparks([{"t": 0, "intensity": 0.5}, {"t": 4, "intensity": 0.6}], 16)]})
# S05 -- the egg's glow brightens; Rico, Lila, Bimo smile and hop for joy (5 s)
scenes.append({"id": "s05", "duration": 5, "camera": {"keys": [{"t": 0, "zoom": 1.08, "x": 30, "y": 30}, {"t": 5, "zoom": 1.16, "x": 40, "y": 10}]},
  "layers": [egg_layer(), rock_layer(),
    rico([dict(t=0, sprite="rico_front", height=300), dict(t=1.6, sprite="rico_jump", height=292, flip=True), dict(t=3.0, sprite="rico_front", height=300)],
         keys=[{"t": 1.6, "y": 985}, {"t": 2.2, "y": 955}, {"t": 2.8, "y": 985}]),
    {"id": "lila", "type": "sprite", "z": 9, "x": 548, "y": 1012, "phase": 0.5, "poses": [friend("lila_size_panel")], "bob": {"amp": 9, "rot": 3, "freq": 1.1, "active_from": 1.8, "active_to": 5}},
    {"id": "bimo", "type": "sprite", "z": 8, "x": 610, "y": 1058, "phase": 0.0, "poses": [friend("bimo_size_panel")], "bob": {"amp": 9, "rot": 3, "freq": 1.1, "active_from": 2.2, "active_to": 5}}],
  "effects": [glow([{"t": 0, "intensity": 0.5}, {"t": 3, "intensity": 0.95}, {"t": 5, "intensity": 1.0}]), sparks([{"t": 0, "intensity": 0.5}, {"t": 3, "intensity": 1.0}, {"t": 5, "intensity": 1.1}], 30)]})
# S06 -- soft glow on Rico, Piko, Tika; slow pull-back and a final hold (5 s)
scenes.append({"id": "s06", "duration": 5, "camera": {"keys": [{"t": 0, "zoom": 1.12, "x": 30, "y": -30}, {"t": 4, "zoom": 1.0, "x": 20, "y": 0}, {"t": 5, "zoom": 1.0, "x": 20, "y": 0}]},
  "layers": [{"id": "tika", "type": "sprite", "z": 3, "x": 548, "y": 935, "poses": [friend("tika_size_panel")], "keys": [{"t": 0, "stretch": 1.07, "rot": -4}], "phase": 0.3},
             egg_layer(), rock_layer(), rico([dict(sprite="rico_wave", height=282, flip=True)]),
             {"id": "piko", "type": "sprite", "z": 9, "x": 600, "y": 505, "phase": 1.0, "poses": [friend("piko_size_panel")], "bob": {"amp": 12, "rot": 3, "freq": 1.3, "active_from": 0, "active_to": 9}}],
  "effects": [glow([{"t": 0, "intensity": 1.0}, {"t": 4, "intensity": 0.8}, {"t": 5, "intensity": 0.75}]), sparks([{"t": 0, "intensity": 1.0}, {"t": 5, "intensity": 0.8}], 30)]})

spec = {"title": "Rico & Friends - Telur Pelangi (zero-cost)", "fps": 24, "size": [720, 1280], "seed": 7, "rock": {"w": 360, "h": 220},
        "sprites_dir": "outputs/zero-cost/rico-and-friends/sprites",
        "units": {"rico_ref_sprite": "rico_size_panel", "rico_ref_height_px": 300,
                  "note": "friends are sized from the group sheet's own size-comparison panel (relative to Rico), the egg from Rico's own comparison panel; no numbers are written into prompts"},
        "scenes": scenes}
out = Path(__file__).with_name("rico-telur-pelangi.json")
out.write_text(json.dumps(spec, indent=1)); print("wrote", out)
