# Story ideas → script → storyboard

## 1. Idea generation (give 3–5, then recommend one)

Each idea in this exact shape:

```
Title:
Logline (1 sentence): [Character] wants [goal] but [obstacle], so [action] and learns [change].
Protagonist: original character, one signature visual trait (silhouette/color/prop).
Emotional core: one feeling (wonder, loneliness→friendship, courage, generosity…).
Why it works in 3D animation: one visual set-piece the Pixar look excels at (light, texture, scale, an inanimate object with a face).
Length fit: how many scenes at 4–10 s each.
```

Good Pixar-style premises: inanimate/object protagonists with a human-sized want; small creature in a big world; two opposites forced together; a ritual/routine disrupted by one tiny change. Avoid: dialogue-heavy plots, crowds (more than 3 named characters multiplies drift), long chases across many locations.

## 2. Constraints that keep generation feasible

| Constraint | Value | Why |
|-----------|-------|-----|
| Scene length | 4–15 s (target 5–8 s) | Seedance 2.0 limit on Arcads |
| Total length | 30–60 s default | cost scales linearly with scenes × ratios |
| Named characters | ≤ 3 | identity drift grows fast; ≤3 reference images per Seedance call |
| Locations | 1–2 | the setting lock must stay identical |
| One primary action per scene | yes | multi-action scenes morph |
| VO per scene | ≤ 2.5 words/s × duration | otherwise dead air or rushed VO |
| Dialogue on screen | avoid lip-sync; prefer VO | in-prompt speech is unreliable, VO is overlaid in post |

## 3. Story shape (default 3 acts across 6–8 scenes)

| Beat | Scenes | Purpose |
|------|--------|---------|
| Hook | 1 | Character + want in one image. First 2 s must be visually arresting. |
| Setup | 1–2 | Routine/world; establish the setting lock. |
| Disruption | 1 | The thing that changes. |
| Struggle | 1–2 | One attempt, one setback. |
| Turn | 1 | Insight or kindness. |
| Resolution | 1 | Changed state, warm closing image (hold 1 s). |

## 4. Script format

```
SCENE 03 · 6 s · LOCATION: living-room · CHARACTERS: bimo, lena
ACTION: one sentence, one primary motion.
SHOT/CAMERA: medium shot, slow push in.
VO: "…"  (words: N, max = 2.5 × seconds)
```

Script rules: write VO in the user's language; keep ≤ 12 words per line; no on-screen text; end on a visual, not an explanation.

## 5. Storyboard table (present this for approval)

| # | Dur | Setting | Chars | Shot | Action | Camera | VO | Continuity from |
|---|-----|---------|-------|------|--------|--------|----|-----------------|

Then transcribe it into `project.json`. The builder validates durations (4–15), ratios, character/setting ids, VO length, `continuity_from` links and Seedance-forbidden words before it writes anything.
