# Zero-cost Shorts workflow (Rico & Friends, LYLA Education, parenting)

Decision (owner): **no extra spending.** No Arcads, no Gemini billing, no card, no paid API. Skill: `skills/zero-cost-shorts/` (read its SKILL.md).

Result so far: `outputs/zero-cost/rico-and-friends/final/rico-telur-pelangi_9x16.mp4` — 30 s, 720x1280, 24 fps, English narration (Kokoro `am_michael`), synthesised music + forest ambience + SFX, burned-in captions, official character artwork only. Self-checks: assembly (durations equal, no silent window, music ducked under VO) and OCR text/badge QA (60/60 frames clean).

## What is free and what it costs
All components are local and free (see `zc_setup.py --check`): FFmpeg, Kokoro-82M (Apache-2.0), EDSR super-resolution (Apache-2.0), Baloo 2 font (OFL), RapidOCR (Apache-2.0), numpy audio synthesis (original). One-time download ~400 MB from public GitHub URLs. No usage limits.

## Honest limits
- Quality = storybook motion comic (cut-out animation), not 3D character animation. No walk cycles or lip-sync; poses are limited to what each master sheet shows.
- Friends' sprites are small on the group sheet (~60-170 px) so they are softer than Rico after 4x super-resolution. One PNG per character on a plain background (>=1000 px) would raise quality at zero cost.
- Background is procedurally drawn (clean, simple), not painted art.
- Audio is synthesised and was verified numerically only (levels, timing, ducking, no gaps); judge the sound by ear. The narrator is Kokoro `am_michael`, not ElevenLabs "Brian".
- Only APPROVED library characters can be used (gate enforced). LYLA Education today: Fasha and Kania. Text cards for parenting tips are not implemented yet.
