---
name: zero-cost-shorts
description: >-
  Zero-cost production of vertical 9:16 YouTube Shorts from the OFFICIAL character artwork in the Character Reference Library, using only free open-source tools (FFmpeg, Kokoro TTS, numpy audio synthesis, OpenCV super-resolution, OCR QA). No paid API, no Arcads, no billing, no account, no card. Cuts sprites from approved master sheets, animates them over a procedural storybook background, adds English narration, music, forest ambience, SFX and burned-in captions, then QA-checks the picture for badges/text. Use when the user wants a Shorts video for Rico & Friends, LYLA Education or other LYLA-library characters at no cost, or says "zero-cost", "gratis", "tanpa biaya", "tanpa API berbayar".
---

# zero-cost-shorts

Produces a finished Shorts video **without spending anything**. It replaces generative AI video with **cut-out animation of the official master-sheet artwork**: characters can never drift off-model, because they are never redrawn.

## Hard rules (zero-cost guardrails — never relax)

1. **No paid or metered service, ever.** No Arcads, no Gemini billing, no OpenAI/Runway/Kling/fal/Replicate/ElevenLabs, no card, no credit purchase. If a step seems to need one, find a free local alternative or say it cannot be done for free.
2. **Characters = official artwork only.** Sprites are cut from master sheets of **APPROVED** characters (`scripts/check-character-library.sh <Project> --character <Name>` must pass; `zc_sprites.py` enforces it). Never redraw, restyle, recolor, or invent a character or a prop that is not on a sheet.
3. **Master sheets are read-only.** Sprites are new derived files with provenance (`manifest.json` records the source sheet and its sha256). The tool asserts the sheets are unchanged.
4. **No badge, logo, watermark or stray text in the picture.** `qa_text_check.py` (OCR) runs on the finished video before captions are added; captions are added only afterwards.
5. **English-only narration** for international audiences (Kokoro). Characters do not speak.
6. **Be honest about limits.** Quality = polished storybook motion comic, not 3D character animation. See "Limits".

## Quickstart

```bash
python3 skills/zero-cost-shorts/scripts/zc_setup.py            # one-time: venvs + free models/fonts (~400 MB, public GitHub URLs)
python3 skills/zero-cost-shorts/scripts/zc_setup.py --check    # status + license + cost/limit table

PY=~/.cache/zero-cost-shorts/venv/bin/python
$PY skills/zero-cost-shorts/scripts/zc_sprites.py skills/zero-cost-shorts/sprite-boxes/rico-and-friends.json --out outputs/zero-cost/rico-and-friends/sprites
$PY skills/zero-cost-shorts/scripts/zc_audio.py tts --script outputs/zero-cost/rico-and-friends/audio/lines.json --voice am_michael --out outputs/zero-cost/rico-and-friends/audio/vo
$PY skills/zero-cost-shorts/scripts/zc_audio.py music --seconds 30 --out outputs/zero-cost/rico-and-friends/audio/music.wav   # also: ambient, sfx --kind ...
$PY skills/zero-cost-shorts/scripts/zc_render.py skills/zero-cost-shorts/templates/rico-telur-pelangi.json --scene s05 --still 3.2 --out preview.png   # check a frame first
$PY skills/zero-cost-shorts/scripts/zc_produce.py skills/zero-cost-shorts/templates/rico-telur-pelangi.production.json   # render + mix + QA + captions
```

## Pipeline

`master sheets (approved)` → **zc_sprites** (cut-out + EDSR x4 + edge clean) → **zc_render** (procedural forest, parallax camera, pose switching, waddle/hop, egg glow, sparkles) → silent clips → **assemble_final** (VO + music + ambience + SFX, ducking, no silent gaps) → **qa_text_check** (OCR) → **zc_captions** (from the measured VO timing) → final `*_9x16.mp4`.

## Reusing it for another project

1. **Sprites:** write `sprite-boxes/<project>.json` (sheet paths + pixel boxes of each pose; `bg_xy` to sample the panel colour; `grabcut_rect` for objects on busy backgrounds). Only approved characters pass the gate.
2. **Scenes:** copy `templates/make_rico_spec.py`, change layers/keyframes/camera/effects; sprite sizes come from the sheet's own comparison panels (`panel_scale`, `height_ratio`), so proportions follow the artwork.
3. **Audio:** write `lines.json` (`[{"id","text"}]`), choose a Kokoro voice (`am_*` American male, `af_*` female, 54 total), and list SFX cues per scene in the production file.
4. **Produce:** `zc_produce.py <production.json>`.

## Limits (read before promising anything)

- **Source-art resolution is the quality ceiling.** Rico's sheet art is large and crisp; the friends' art is small (~60–170 px tall on the sheet), so they are softer after 4x super-resolution. Better source art (one character per PNG on a plain background, 1000 px+) raises quality at zero cost.
- **Poses are limited to what the sheet shows.** Motion is cut-out style: slide, hop, waddle, stretch, hover, pose switches. No walk cycles or lip-sync.
- **Mirroring:** sprites may be flipped horizontally to face the other way (same artwork).
- **Audio is synthesised and has not been heard by the tool's author** — levels and timing are verified numerically; judge the sound by ear.
- **LYLA Education / parenting:** the engine is generic, but only APPROVED characters can be used (today: Fasha and Kania). Other characters need the owner's approval first. Text cards/titles for parenting tips are not yet implemented (captions are).
