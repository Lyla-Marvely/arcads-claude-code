# pixar-animation-video — usage guide

Workflow for an original Pixar-style 3D animated short (a story, not a product ad), delivered in **9:16 and 16:9**.
Skill: `skills/pixar-animation-video/` (synced to `.claude/skills/` and `.cursor/skills/` by `./scripts/sync-skill.sh`).

## What you get

| Stage | Output | Needs API? |
|-------|--------|-----------|
| Story ideas (3–5) | loglines + recommendation | No |
| Script | per-scene action + VO | No |
| Storyboard | table + `project.json` | No |
| Character lock | lock text + turnaround prompt per character | No (prompt) / Yes (image) |
| Scene image prompts | per scene × per ratio | No (prompt) / Yes (image) |
| Scene video prompts | Seedance 2.0 + Gemini Omni versions, with negatives and continuity | No (prompt) / Yes (video) |
| Stills, clips, final mp4 | media files | **Yes — Arcads, costs credits** |

Everything marked "No" works offline. **No media exists until the workflow reports an Arcads asset id and a saved file for it.**

## Quick start

1. Ask Claude: *"Buat video animasi Pixar-style tentang … 45 detik, 9:16 dan 16:9."* (or `/pixar-animation-video`).
2. Pick an idea → approve the script → approve the storyboard.
3. Build the prompt pack (offline):

   ```bash
   cp skills/pixar-animation-video/templates/project.example.json outputs/my-story/project.json   # edit it
   python3 skills/pixar-animation-video/scripts/build_prompts.py outputs/my-story/project.json --check
   python3 skills/pixar-animation-video/scripts/build_prompts.py outputs/my-story/project.json --out outputs/my-story/prompts
   ```
   Open `outputs/my-story/prompts/prompt-pack.md`.
4. Check requirements **before generating video**:

   ```bash
   ./skills/pixar-animation-video/scripts/check-requirements.sh            # online
   ./skills/pixar-animation-video/scripts/check-requirements.sh --offline  # tools + env only
   ```
   Exit 0 = ready; exit 1 = blocked (the output lists what to fix). Blocked still allows steps 1–3.
5. Approve the credit estimate, then generate: character sheets → stills (per ratio) → clips (per ratio) → optional VO, trim, concat, captions.

## Requirements

| Need | Why | How to verify |
|------|-----|---------------|
| `.env` with `ARCADS_BASIC_AUTH` or `ARCADS_API_KEY` | all generation calls | `check-requirements.sh` (auth test) |
| `PRODUCT_ID` | required by `POST /v2/videos/generate` | from `GET /v1/products`, saved in `.env` |
| `python3`, `curl`, `jq` | prompt builder and generation scripts | `check-requirements.sh` |
| `ffmpeg`, `ffprobe` | trim/concat clips | `check-requirements.sh` (warn only) |
| `npx` + HyperFrames, Whisper | captions (optional) | see `shared/skills/caption-video/prompting/guide.md` |
| ElevenLabs key | VO/music (optional) | see claymation/pixar guides |

The preflight cannot confirm your Arcads plan, per-model access, or credit balance (Arcads has no billing endpoint) — always confirm exact pricing in the Arcads platform. Credit numbers shown by this workflow are **estimates**.

## API facts used (source: `skills/arcads-external-api/reference.md`)

- Stills: `POST /v2/images/generate`, `gpt-image-2` (max 5 reference images) or `nano-banana-2` (max 14); ratios `9:16`, `16:9`.
- Clips: `POST /v2/videos/generate`, `seedance-2.0`; ratios `9:16` / `16:9` only; `duration` 4–15 s; `resolution` 480p/720p; `referenceImages` max 3; **no `startFrame`**.
- Poll: `GET /v1/assets/{id}` (Seedance is **not** under `/v1/videos`).
- Uploads: presigned `filePath` is one-time use → re-upload for each call.
- Gemini Omni Flash: **not** in the documented model list. The repo guide mentions an Arcads MCP tool `arcads_generate_video_omni_flash`; use it only if it actually appears in your session, otherwise the workflow uses Seedance 2.0.

## Two ratios = two compositions

Each scene gets its own still and clip per ratio (re-framed, not cropped), so cost is roughly `scenes × ratios` stills plus `scenes × ratios` clips plus character sheets. Generate one ratio first if you want to limit spend, then the second after you approve the look.

## Optional `project.json` fields

| Field | Effect |
|-------|--------|
| `characters[].master_sheet` | User-supplied character sheet. The builder skips the turnaround prompt and plans it as `img2` (never regenerated). |
| `scenes[].reference_sheet` | Repo-relative path of a master sheet to use as `img2` for that scene (e.g. a group sheet for multi-character scenes). The builder fails if the file does not exist on disk, as it does for `characters[].master_sheet`. It also lists the still reference files per scene (gpt-image-2 max 5). |
| `characters[].short_lock` | Compact lock used in video prompts (identity is carried by reference images). |
| `style_lock_video`, `settings[].video_lock` | Shorter style/setting text for video prompts. |
| `continuity_lock`, `continuity_lock_video`, `scenes[].continuity_notes` | Global and per-scene continuity lines appended to prompts. |
| `extra_negative`, `extra_negative_video` | Project-specific negatives (e.g. "never change the three orange spikes"). |

The builder warns when a Seedance prompt exceeds ~260 words (guide target, not a documented API limit).

## Troubleshooting

| Symptom | Likely cause / fix |
|---------|--------------------|
| `check-requirements.sh` → BLOCKED | missing `.env`/credential: run `./scripts/setup.sh` |
| `400 REFERENCE_FILE_NOT_FOUND` | reused a presigned `filePath`; re-upload per call |
| `404` polling a Seedance job | poll `/v1/assets/{id}`, not `/v1/videos/{id}` |
| Seedance asset `failed` (content checker) | credits are charged at create; rewrite the prompt before retrying |
| Character changes between scenes | regenerate the still with the turnaround sheet + previous still as references; shorten/simplify the action |
| Builder says forbidden word | remove `cinematic/professional/stunning/8k/studio/perfect` from the project text |

## Files

```
skills/pixar-animation-video/
  SKILL.md                      phases, gates, hard rules
  prompting/story-to-script.md  ideas, script, storyboard
  prompting/prompt-formulas.md  locks, image/video prompts, negatives, continuity
  templates/project.example.json
  scripts/build_prompts.py      offline prompt-pack builder + validator
  scripts/check-requirements.sh API/tool preflight (read-only)
```
References reused: `shared/skills/{pixar-style-ad,claymation-ad,gemini-omni-flash,caption-video}`.
