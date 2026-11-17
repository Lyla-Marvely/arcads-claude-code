---
name: pixar-animation-video
description: >-
  End-to-end workflow for an original Pixar-style 3D animated short (story, not a product ad): story ideas, script, scene-by-scene storyboard, character lock sheets, per-scene image prompts, per-scene video prompts, negative prompts and continuity locks, in both 9:16 and 16:9. Checks Arcads API requirements before any video generation and never claims media exists unless an asset id/file proves it. Use when the user asks for a "Pixar animation video", "animated short story", "3D animated story video", "cerita animasi Pixar", "storyboard animasi", or wants story ideas + script + scene prompts for an animated video. For Pixar-style PRODUCT ads use pixar-style-ad instead.
---

# pixar-animation-video (Arcads)

Narrative Pixar-style animated shorts: **idea → script → storyboard → character lock → scene stills → scene clips → assembly**. Sibling of `pixar-style-ad` (which is a 4-beat *product ad*); this one is a story with a character arc, and it outputs **both 9:16 and 16:9**.

## Read order

1. **This file** — phases, gates, hard rules.
2. [prompting/story-to-script.md](prompting/story-to-script.md) — ideas, script, scene beats, storyboard rules.
3. [prompting/prompt-formulas.md](prompting/prompt-formulas.md) — character lock, image prompt, video prompt (Seedance / Omni), negative prompt, continuity lock, 9:16 vs 16:9.
4. Reused references (do not duplicate; read when the phase needs them):
   - `shared/skills/pixar-style-ad/prompting/guide.md` — Pixar look, style lock wording, VO/dead-space rule, caption look, Arcads gotchas.
   - `shared/skills/claymation-ad/prompting/guide.md` — multi-character cast sheet and narrator/VO pipeline (ElevenLabs).
   - `shared/skills/gemini-omni-flash/prompting/guide.md` — only if the Omni path is actually available (see "API requirements").
   - `shared/skills/caption-video/prompting/guide.md` — Whisper + HyperFrames captions on the finished mp4.
   - `skills/arcads-external-api/reference.md` — the authoritative endpoint/field source. **Do not use any endpoint or field that is not documented there.**
5. [docs/pixar-animation-video.md](../../docs/pixar-animation-video.md) — user-facing usage guide.

## Hard rules — never relax

1. **Never claim media was generated unless proven.** A scene is "generated" only if you hold an Arcads asset `id` with `status: generated` and a downloaded file path. Everything else is "prompt only", "submitted", "failed" or "not started". Report per-scene status honestly, including failures and retries.
2. **Do not invent APIs, models, fields or limits.** Use only what `skills/arcads-external-api/reference.md` documents. If something is unverified (e.g. Gemini Omni Flash on Arcads), say so and use the documented fallback.
3. **Run the preflight before any generation call:** `skills/pixar-animation-video/scripts/check-requirements.sh`. If it prints `BLOCKED`, stop at the prompt pack and tell the user what is missing. Story, script, storyboard and prompts can still be delivered offline.
4. **Approval gates.** Get explicit user approval of (a) the chosen idea, (b) the script, (c) the storyboard + character lock text, (d) each character turnaround image, (e) the credit estimate — in that order — before the next paid step.
5. **Credits are estimates.** Arcads has no billing endpoint. Show the request count (`build_prompts.py` prints it), multiply by per-call credits from `logs/arcads-api.jsonl` / `MASTER_CONTEXT.md`, label it an estimate, and tell the user to confirm in the Arcads platform. Seedance charges at create time and does not refund content-checker failures — tighten risky prompts before firing, never blind-retry.
6. **Log every generation call** to `logs/arcads-api.jsonl` (see `logs/README.md`).
7. **Each ratio is composed separately.** Never crop a 9:16 still into 16:9 or vice versa; generate a separate still per scene per ratio and pass that ratio's still to Seedance. Aspect ratios are `9:16` and `16:9` only (Seedance 2.0 limit on Arcads).
8. **No on-screen text inside generated media.** Captions are added in post (caption-video skill). Narration is generated externally (ElevenLabs) and overlaid; do not rely on in-prompt narrator lines. Trim clips to VO length per the dead-space rule in the pixar-style-ad guide.
9. **Original characters only.** Do not name or reproduce existing Pixar/Disney characters, logos or scenes. "Pixar-style" describes a look, not licensed IP; say that if the user asks for a named franchise character.

10. **Character library gate.** For any LYLA-project character, follow `references/character-library/CHARACTER_LIBRARY.md`: set `characters[].master_sheet` to the real file path from that project's folder, run `./scripts/check-character-library.sh <Project-Folder> --character <Name>` for every character used (it prints the lock + reference files; names are not unique across projects, use `<Project>:<Name>`) before Phase 4, and stop paid steps if any exits non-zero. Characters invented for a story (friends, extras) are "PROPOSED", not official; prefer the project's official cast from its master sheets and never redesign them. Rico & Friends: official cast is Rico, Lila, Bimo, Tika, Piko only; Pip and Moss are not official; spell the project "Rico".

## API requirements (verify, don't assume)

Documented in `skills/arcads-external-api/reference.md`:

| Step | Endpoint / model | Limits that matter here |
|------|------------------|-------------------------|
| Reference upload | `POST /v1/file-upload/get-presigned-url` → `PUT presignedUrl` → `filePath` | `filePath` is **one-time use**; re-upload per call or you get `400 REFERENCE_FILE_NOT_FOUND` |
| Stills | `POST /v2/images/generate`, `gpt-image-2` (default for stylized 3D) or `nano-banana-2` | ratios 1:1/16:9/9:16; refs: gpt-image-2 max **5**, nano-banana-2 max 14 |
| Clips | `POST /v2/videos/generate`, `seedance-2.0` | ratio **9:16 or 16:9 only**; `duration` **4–15** s; `resolution` 480p/720p; `referenceImages` max **3**; **no `startFrame`** on Seedance (use `referenceImages`); needs `productId` |
| Polling | `GET /v1/assets/{id}` for stills **and** Seedance clips | **not** `/v1/videos/{id}` (404 for Seedance) |
| Auth | HTTP Basic: `ARCADS_BASIC_AUTH` (already contains `Basic `) or `ARCADS_API_KEY` | — |

**Gemini Omni Flash:** the repo guide says it is callable via an Arcads MCP tool `arcads_generate_video_omni_flash`, but that model is **not** in `CreateVideoDto`'s documented enum. Use it only if that tool is visibly present in this session's tool list; otherwise default to Seedance 2.0 and say Omni was not used. Omni is a good fit for *editing* an existing clip conversationally, not as the default scene generator.

**Single-shot limit:** Seedance clips are ≤15 s. A scene longer than 15 s must be split into two scenes.

## Workflow

### Phase 0 — Brief + preflight
Ask once (skip what the user already gave): audience/platform, total length (default 45–60 s), tone, language of VO (default: the user's language), theme/moral, any must-have character, whether VO/music/captions are wanted. Then run `check-requirements.sh` and, for LYLA-project characters, `./scripts/check-character-library.sh <Project-Folder>`; tell the user the result (ready / blocked / what's unverified).

### Phase 1 — Story ideas
Give **3–5 ideas** (logline, protagonist, want, obstacle, ending, why it suits 3D animation). Follow [story-to-script.md](prompting/story-to-script.md). Recommend one; user picks.

### Phase 2 — Script
Write the script with scene numbers, per-scene duration, action, VO line. Fit VO to duration (≈2.5 words/s max). Approval gate.

### Phase 3 — Storyboard + project.json
Fill `templates/project.example.json` (copy it to `outputs/<slug>/project.json`; `outputs/` is gitignored). Present the storyboard as a table: scene / duration / shot / action / camera / VO / characters. Approval gate.

```bash
python3 skills/pixar-animation-video/scripts/build_prompts.py outputs/<slug>/project.json --check   # validate
python3 skills/pixar-animation-video/scripts/build_prompts.py outputs/<slug>/project.json --out outputs/<slug>/prompts
```
Before calling a pack final, run `python3 skills/pixar-animation-video/scripts/verify_pack.py outputs/<slug>` (13 offline checks, writes `final-verification-report.md`).

This writes `prompt-pack.md` (human-readable) and `prompts.json`: character lock sheets, per-scene image prompts, Seedance + Omni video prompts, per-ratio, plus request counts. **Offline — nothing is generated.** Deliver this pack even if preflight is BLOCKED.

### Phase 4 — Character lock (paid)
Generate one turnaround sheet per character (`turnaround_prompt`) with `gpt-image-2`. User approves each. Save approved images under `outputs/<slug>/characters/`. These become `img2` for every scene. If identity drifts, regenerate before spending on scenes.

### Phase 5 — Scene stills (paid, per ratio)
For each scene × ratio: generate the still from `image_prompt`, passing the character sheet(s) and the previous approved scene's still as `referenceImages` (≤5; re-upload per call). Show stills, approve or retry (max 2 retries per still). Generator: `skills/chatgpt-image-ad/scripts/generate_image.py --prompt … --aspect-ratio 9:16|16:9 --image-ref <path> (repeat, max 5) --out <dir>` (handles presigned upload). It appends ad-oriented edge-safe/no-chrome suffixes by default; pass `--no-safe-zone` for story frames and review the output.

### Phase 6 — Scene clips (paid, per ratio)
Show the credit estimate (rule 5) and wait for confirmation. For each approved still, call `POST /v2/videos/generate` with `model: seedance-2.0`, `prompt = seedance_prompt`, matching `aspectRatio` and `duration`, `referenceImages = [still, character sheet, (previous still)]` (max 3, freshly uploaded), `resolution: 720p` (480p for drafts), `audioEnabled: false` when VO is added in post. An existing batch script, `shared/skills/pixar-style-ad/scripts/generate-seedance.sh`, posts to this endpoint with `referenceImages` and reads env `ASPECT_RATIO`, `AUDIO_ENABLED`, `RESOLUTION` (it expects its own `RUN_DIR` layout and a startframe map from `upload-startframes.sh`; it was not exercised in this session). Reuse it per ratio, or call the endpoint directly following `reference.md`. Poll `GET /v1/assets/{id}`; download; QA each clip against the continuity checklist; max 2 retries per clip.

### Phase 7 — Assembly (optional)
VO (ElevenLabs, per claymation guide), trim each clip to `VO + 0.5 s`, concat with ffmpeg per ratio, then captions via the `caption-video` guide. Re-transcribe after trimming. Deliver one mp4 per ratio.

### Phase 8 — Report
Give the user a per-scene table: scene, ratio, still status, clip status, asset id, file path, retries. State plainly what was and wasn't generated. Append a dated note to `MASTER_CONTEXT.md` Changelog (Decision / What changed / Why) and any new credit costs observed.

## Output layout

```
outputs/<slug>/
  project.json        # story bible + storyboard (source of truth)
  prompts/            # prompt-pack.md, prompts.json  (offline)
  characters/         # approved turnaround images
  stills/<ratio>/     # s01.png ...
  clips/<ratio>/      # s01.mp4 ...
  final/              # <slug>-9x16.mp4, <slug>-16x9.mp4
```
