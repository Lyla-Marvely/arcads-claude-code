# Rico & Friends — Telur Pelangi (rev. 2) — prompt pack

_Rico menemukan Telur Pelangi; sahabatnya datang satu per satu, dan mereka sepakat menjaganya bersama-sama. Telur tetap sebuah objek._

> Generated offline by build_prompts.py. **No image or video has been generated.** Nothing below has been sent to any API.

## Negative prompts

**Image:** Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.

**Video:** No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.

## Global continuity lock

- every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features
- Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet
- the SCALE LOCK ratios never change between scenes
- the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character
- same clearing in every scene, warm golden daylight from camera-left, no time-of-day change
- only the characters listed for the scene appear, no other creatures
- no scene cuts inside a clip; each clip is one continuous shot
- Rico is always on the left of the egg, facing it

## Character lock sheet

### Rico (`rico`) — MASTER SHEET (design locked)

**Lock:** Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet)

**Master sheet file:** `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`  
_Supplied by the user. Do NOT generate a new turnaround; attach this file as a reference (re-upload for every call — presigned paths are one-time use)._

### Lila (`lila`) — MASTER SHEET (design locked)

**Lock:** Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet)

**Master sheet file:** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`  
_Supplied by the user. Do NOT generate a new turnaround; attach this file as a reference (re-upload for every call — presigned paths are one-time use)._

### Bimo (`bimo`) — MASTER SHEET (design locked)

**Lock:** Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet)

**Master sheet file:** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`  
_Supplied by the user. Do NOT generate a new turnaround; attach this file as a reference (re-upload for every call — presigned paths are one-time use)._

### Tika (`tika`) — MASTER SHEET (design locked)

**Lock:** Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet)

**Master sheet file:** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`  
_Supplied by the user. Do NOT generate a new turnaround; attach this file as a reference (re-upload for every call — presigned paths are one-time use)._

### Piko (`piko`) — MASTER SHEET (design locked)

**Lock:** Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet)

**Master sheet file:** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`  
_Supplied by the user. Do NOT generate a new turnaround; attach this file as a reference (re-upload for every call — presigned paths are one-time use)._

## Scenes

### s01 — hook (8s)

**VO:** Pagi itu di hutan, Rico menemukan sebuah telur pelangi yang berkilau.

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = Rico MASTER character sheet (references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png) — user-supplied, never regenerated

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`

#### s01 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock. Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Rico enters on the left of the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 8 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-8s): Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes. One primary motion, smooth and readable.
Camera: wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock; slow, steady push in, no cuts.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Rico enters on the left of the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 8s, 9:16. Rico in forest clearing: Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes. wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock, slow, steady push in, no cuts. Keep Rico identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s01 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock. Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Rico enters on the left of the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 8 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-8s): Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes. One primary motion, smooth and readable.
Camera: wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock; slow, steady push in, no cuts.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Rico enters on the left of the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 8s, 16:9. Rico in forest clearing: Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes. wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock, slow, steady push in, no cuts. Keep Rico identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

### s02 — arrival 1 (4s)

**VO:** Piko terbang menghampiri.

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = MASTER sheet references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png — owner-approved file, never regenerated; img3 = approved still of s01 (continuity anchor)

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`; `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`; `<approved still of s01, same ratio>`

#### s02 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium two-shot at the egg: Rico on the left of the egg, Piko hovering above and to the right. Piko glides in from above and hovers near the egg while Rico looks up at her with delight.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Piko about 0.75 (the smallest body, wide wings); Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; the egg is in the same spot as in s01; Piko hovers above-right of the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 4 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s01) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-4s): Piko glides in from above and hovers near the egg while Rico looks up at her with delight. One primary motion, smooth and readable.
Camera: medium two-shot at the egg: Rico on the left of the egg, Piko hovering above and to the right; static framing with a very gentle push in.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Piko 0.75; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; the egg is in the same spot as in s01; Piko hovers above-right of the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 4s, 9:16. Rico and Piko in forest clearing: Piko glides in from above and hovers near the egg while Rico looks up at her with delight. medium two-shot at the egg: Rico on the left of the egg, Piko hovering above and to the right, static framing with a very gentle push in. Keep Rico and Piko identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s02 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium two-shot at the egg: Rico on the left of the egg, Piko hovering above and to the right. Piko glides in from above and hovers near the egg while Rico looks up at her with delight.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Piko about 0.75 (the smallest body, wide wings); Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; the egg is in the same spot as in s01; Piko hovers above-right of the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 4 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s01) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-4s): Piko glides in from above and hovers near the egg while Rico looks up at her with delight. One primary motion, smooth and readable.
Camera: medium two-shot at the egg: Rico on the left of the egg, Piko hovering above and to the right; static framing with a very gentle push in.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Piko 0.75; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; the egg is in the same spot as in s01; Piko hovers above-right of the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 4s, 16:9. Rico and Piko in forest clearing: Piko glides in from above and hovers near the egg while Rico looks up at her with delight. medium two-shot at the egg: Rico on the left of the egg, Piko hovering above and to the right, static framing with a very gentle push in. Keep Rico and Piko identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

### s03 — arrival 2 (4s)

**VO:** Lila dan Bimo menyusul.

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = MASTER sheet references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png — owner-approved file, never regenerated; img3 = approved still of s02 (continuity anchor)

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`; `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`; `<approved still of s02, same ratio>`

#### s03 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium three-shot: Rico on the left of the egg, Lila and Bimo on its right. Lila and Bimo walk in from frame-right and stop beside the egg, looking at it with wonder while Rico smiles at them.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Lila about 0.9; Bimo about 0.9; Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Lila and Bimo stand on the right of the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 4 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s02) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-4s): Lila and Bimo walk in from frame-right and stop beside the egg, looking at it with wonder while Rico smiles at them. One primary motion, smooth and readable.
Camera: medium three-shot: Rico on the left of the egg, Lila and Bimo on its right; static framing.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Lila 0.9; Bimo 0.9; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Lila and Bimo stand on the right of the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 4s, 9:16. Rico and Lila and Bimo in forest clearing: Lila and Bimo walk in from frame-right and stop beside the egg, looking at it with wonder while Rico smiles at them. medium three-shot: Rico on the left of the egg, Lila and Bimo on its right, static framing. Keep Rico and Lila and Bimo identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s03 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium three-shot: Rico on the left of the egg, Lila and Bimo on its right. Lila and Bimo walk in from frame-right and stop beside the egg, looking at it with wonder while Rico smiles at them.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Lila about 0.9; Bimo about 0.9; Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Lila and Bimo stand on the right of the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 4 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s02) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-4s): Lila and Bimo walk in from frame-right and stop beside the egg, looking at it with wonder while Rico smiles at them. One primary motion, smooth and readable.
Camera: medium three-shot: Rico on the left of the egg, Lila and Bimo on its right; static framing.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Lila 0.9; Bimo 0.9; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Lila and Bimo stand on the right of the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 4s, 16:9. Rico and Lila and Bimo in forest clearing: Lila and Bimo walk in from frame-right and stop beside the egg, looking at it with wonder while Rico smiles at them. medium three-shot: Rico on the left of the egg, Lila and Bimo on its right, static framing. Keep Rico and Lila and Bimo identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

### s04 — arrival 3 (4s)

**VO:** Tika pun datang.

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = MASTER sheet references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png — owner-approved file, never regenerated; img3 = approved still of s03 (continuity anchor)

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`; `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`; `<approved still of s03, same ratio>`

#### s04 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — tight medium two-shot: Rico on the left of the egg, Tika's head and long neck above and behind it. Tika's long neck lowers into the frame from above and she gazes at the egg while Rico looks up at her, smiling.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Tika about 1.4 (the tallest); Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Tika's head is above and behind the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 4 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s03) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-4s): Tika's long neck lowers into the frame from above and she gazes at the egg while Rico looks up at her, smiling. One primary motion, smooth and readable.
Camera: tight medium two-shot: Rico on the left of the egg, Tika's head and long neck above and behind it; static framing with a very slow push in.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Tika 1.4; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Tika's head is above and behind the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 4s, 9:16. Rico and Tika in forest clearing: Tika's long neck lowers into the frame from above and she gazes at the egg while Rico looks up at her, smiling. tight medium two-shot: Rico on the left of the egg, Tika's head and long neck above and behind it, static framing with a very slow push in. Keep Rico and Tika identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s04 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — tight medium two-shot: Rico on the left of the egg, Tika's head and long neck above and behind it. Tika's long neck lowers into the frame from above and she gazes at the egg while Rico looks up at her, smiling.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Tika about 1.4 (the tallest); Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Tika's head is above and behind the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 4 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s03) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-4s): Tika's long neck lowers into the frame from above and she gazes at the egg while Rico looks up at her, smiling. One primary motion, smooth and readable.
Camera: tight medium two-shot: Rico on the left of the egg, Tika's head and long neck above and behind it; static framing with a very slow push in.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Tika 1.4; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Tika's head is above and behind the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 4s, 16:9. Rico and Tika in forest clearing: Tika's long neck lowers into the frame from above and she gazes at the egg while Rico looks up at her, smiling. tight medium two-shot: Rico on the left of the egg, Tika's head and long neck above and behind it, static framing with a very slow push in. Keep Rico and Tika identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

### s05 — glow 1 (5s)

**VO:** Mereka sepakat, telur ini harus dijaga bersama.

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = MASTER sheet references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png — owner-approved file, never regenerated; img3 = approved still of s04 (continuity anchor)

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`; `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`; `<approved still of s04, same ratio>`

#### s05 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium three-shot: Rico on the left of the egg, Lila and Bimo on its right. the egg's rainbow shimmer glows brighter and warmly lights the faces of Rico, Lila and Bimo, who smile at each other.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Lila about 0.9; Bimo about 0.9; Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Lila and Bimo on the right of the egg; the egg glows brighter but keeps its shape and size.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 5 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s04) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-5s): the egg's rainbow shimmer glows brighter and warmly lights the faces of Rico, Lila and Bimo, who smile at each other. One primary motion, smooth and readable.
Camera: medium three-shot: Rico on the left of the egg, Lila and Bimo on its right; static framing with a very slow push in.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Lila 0.9; Bimo 0.9; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Lila and Bimo on the right of the egg; the egg glows brighter but keeps its shape and size.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 5s, 9:16. Rico and Lila and Bimo in forest clearing: the egg's rainbow shimmer glows brighter and warmly lights the faces of Rico, Lila and Bimo, who smile at each other. medium three-shot: Rico on the left of the egg, Lila and Bimo on its right, static framing with a very slow push in. Keep Rico and Lila and Bimo identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s05 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium three-shot: Rico on the left of the egg, Lila and Bimo on its right. the egg's rainbow shimmer glows brighter and warmly lights the faces of Rico, Lila and Bimo, who smile at each other.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Lila about 0.9; Bimo about 0.9; Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Lila and Bimo on the right of the egg; the egg glows brighter but keeps its shape and size.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 5 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s04) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-5s): the egg's rainbow shimmer glows brighter and warmly lights the faces of Rico, Lila and Bimo, who smile at each other. One primary motion, smooth and readable.
Camera: medium three-shot: Rico on the left of the egg, Lila and Bimo on its right; static framing with a very slow push in.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Lila 0.9; Bimo 0.9; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Lila and Bimo on the right of the egg; the egg glows brighter but keeps its shape and size.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 5s, 16:9. Rico and Lila and Bimo in forest clearing: the egg's rainbow shimmer glows brighter and warmly lights the faces of Rico, Lila and Bimo, who smile at each other. medium three-shot: Rico on the left of the egg, Lila and Bimo on its right, static framing with a very slow push in. Keep Rico and Lila and Bimo identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

### s06 — glow 2 (5s)

**VO:** Karena sahabat sejati selalu menjaga hal berharga, bersama-sama.

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = MASTER sheet references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png — owner-approved file, never regenerated; img3 = approved still of s05 (continuity anchor)

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`; `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`; `<approved still of s05, same ratio>`

#### s06 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium-wide shot: Rico on the left of the egg, Piko hovering above-right, Tika's neck lowered behind the egg. the egg's shimmer glows softly on Rico, Piko and Tika as they smile, and Rico looks around happily.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Piko about 0.75 (the smallest body, wide wings); Tika about 1.4 (the tallest); Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Piko hovers above-right, Tika's neck is lowered behind the egg; same glow level as the end of s05.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 5 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s05) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-5s): the egg's shimmer glows softly on Rico, Piko and Tika as they smile, and Rico looks around happily. One primary motion, smooth and readable.
Camera: medium-wide shot: Rico on the left of the egg, Piko hovering above-right, Tika's neck lowered behind the egg; slow, smooth pull back, ending on a one-second hold.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Piko 0.75; Tika 1.4; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Piko hovers above-right, Tika's neck is lowered behind the egg; same glow level as the end of s05.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 5s, 9:16. Rico and Piko and Tika in forest clearing: the egg's shimmer glows softly on Rico, Piko and Tika as they smile, and Rico looks around happily. medium-wide shot: Rico on the left of the egg, Piko hovering above-right, Tika's neck lowered behind the egg, slow, smooth pull back, ending on a one-second hold. Keep Rico and Piko and Tika identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s06 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium-wide shot: Rico on the left of the egg, Piko hovering above-right, Tika's neck lowered behind the egg. the egg's shimmer glows softly on Rico, Piko and Tika as they smile, and Rico looks around happily.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Piko about 0.75 (the smallest body, wide wings); Tika about 1.4 (the tallest); Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; Piko hovers above-right, Tika's neck is lowered behind the egg; same glow level as the end of s05.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 5 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s05) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-5s): the egg's shimmer glows softly on Rico, Piko and Tika as they smile, and Rico looks around happily. One primary motion, smooth and readable.
Camera: medium-wide shot: Rico on the left of the egg, Piko hovering above-right, Tika's neck lowered behind the egg; slow, smooth pull back, ending on a one-second hold.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Piko 0.75; Tika 1.4; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; Piko hovers above-right, Tika's neck is lowered behind the egg; same glow level as the end of s05.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 5s, 16:9. Rico and Piko and Tika in forest clearing: the egg's shimmer glows softly on Rico, Piko and Tika as they smile, and Rico looks around happily. medium-wide shot: Rico on the left of the egg, Piko hovering above-right, Tika's neck lowered behind the egg, slow, smooth pull back, ending on a one-second hold. Keep Rico and Piko and Tika identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

### s07 — optional group hold (4s) — OPTIONAL (not in the baseline)

**VO:** 

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = MASTER sheet references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png — owner-approved file, never regenerated; img3 = approved still of s06 (continuity anchor)

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`; `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`; `<approved still of s06, same ratio>`

#### s07 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — wide static group shot: the five friends arranged like the Pose Grup Referensi on the group master sheet, around the egg. almost no movement: the egg glows softly and the friends smile and blink gently.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Lila about 0.9; Bimo about 0.9; Tika about 1.4 (the tallest); Piko about 0.75 (the smallest body, wide wings); Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; same positions as the end of s06, arranged like the group sheet; same glow level as the end of s06.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 4 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s06) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-4s): almost no movement: the egg glows softly and the friends smile and blink gently. One primary motion, smooth and readable.
Camera: wide static group shot: the five friends arranged like the Pose Grup Referensi on the group master sheet, around the egg; locked-off static framing, four-second hold.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Lila 0.9; Bimo 0.9; Tika 1.4; Piko 0.75; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; same positions as the end of s06, arranged like the group sheet; same glow level as the end of s06.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 4s, 9:16. Rico and Lila and Bimo and Tika and Piko in forest clearing: almost no movement: the egg glows softly and the friends smile and blink gently. wide static group shot: the five friends arranged like the Pose Grup Referensi on the group master sheet, around the egg, locked-off static framing, four-second hold. Keep Rico and Lila and Bimo and Tika and Piko identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s07 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — wide static group shot: the five friends arranged like the Pose Grup Referensi on the group master sheet, around the egg. almost no movement: the egg glows softly and the friends smile and blink gently.
SCALE LOCK (relative to Rico's height; identical in every scene) — Rico 1.0; Lila about 0.9; Bimo about 0.9; Tika about 1.4 (the tallest); Piko about 0.75 (the smallest body, wide wings); Rainbow Egg about 1.25 (a bit taller than Rico).
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and distinguishing features; Rico keeps his turquoise body, cream belly, amber eyes and three orange head spikes exactly as on his sheet; the SCALE LOCK ratios never change between scenes; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed beside the mossy rock in every scene; it is only an object and never hatches, cracks, moves by itself or becomes a character; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only the characters listed for the scene appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico is always on the left of the egg, facing it; same positions as the end of s06, arranged like the group sheet; same glow level as the end of s06.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Reference sheets contain badges, titles, labels and text panels. Use them ONLY for each character's appearance. Never reproduce any badge, logo, title, label, text or sheet layout in the output.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and distinguishing features exactly as the master sheets; no extra, missing or changed features; no new characters or new baby dinosaurs; no accessories added; no badge, logo, watermark or text of any kind anywhere in the frame; the Rainbow Egg is only an object: it has no face, eyes, mouth or limbs, never moves by itself, never hatches or cracks and never turns into a character.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 4 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s06) for continuity.
Reference sheets contain badges and text: use them only for character appearance; never reproduce any badge, logo or text.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-4s): almost no movement: the egg glows softly and the friends smile and blink gently. One primary motion, smooth and readable.
Camera: wide static group shot: the five friends arranged like the Pose Grup Referensi on the group master sheet, around the egg; locked-off static framing, four-second hold.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
SCALE LOCK (Rico = 1.0, fixed in every scene) — Rico 1.0; Lila 0.9; Bimo 0.9; Tika 1.4; Piko 0.75; Rainbow Egg 1.25.
CONTINUITY LOCK — characters exactly as the master sheets, Rico with three orange head spikes; egg: same look, size and spot, only an object, never hatches; Rico left of the egg; one continuous shot; same positions as the end of s06, arranged like the group sheet; same glow level as the end of s06.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No new characters; no badge, logo or text; the egg has no face or limbs.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 4s, 16:9. Rico and Lila and Bimo and Tika and Piko in forest clearing: almost no movement: the egg glows softly and the friends smile and blink gently. wide static group shot: the five friends arranged like the Pose Grup Referensi on the group master sheet, around the egg, locked-off static framing, four-second hold. Keep Rico and Lila and Bimo and Tika and Piko identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

## QA checklist (apply to every still and clip)

- [ ] Identity: faces, eyes, colors and markings match the master sheets (compare side by side).
- [ ] Rico has exactly three orange head spikes plus the same turquoise body, cream belly and amber eyes.
- [ ] Lila and Bimo: three horns and the right frill color; Tika: long neck and spots; Piko: wide wings and blue crest.
- [ ] Scale lock: ratios match in every scene (Rico 1.0, egg about 1.25, Tika tallest, Piko smallest). No size drift between scenes.
- [ ] Egg: same look, size and spot; no face, eyes or limbs; never moves by itself, hatches or cracks.
- [ ] No badge, logo, watermark or text of any kind; in particular NO 'LYLA MARVELY' badge or lettering (reject and retry if it appears).
- [ ] Only the characters listed for the scene appear (max 3 per clip); no other creatures.
- [ ] Stage layout and screen direction match the continuity lock.
- [ ] Correct aspect ratio (9:16 or 16:9), composed separately, not cropped.
- [ ] Max 2 retries per asset, then ask the owner. Consistency beats clip count: split the shot instead of retrying a crowded one.

## Request count (before any generation)

- turnaround_images: 0
- scene_stills: 12
- scene_clips: 12
- total_scene_seconds_per_ratio: 30
- optional_scenes_not_counted: ['s07']
- optional_extra_stills_and_clips: 2
- max_characters_in_any_baseline_clip: 3
- note: Counts only. Credit cost is NOT computed here; present it to the user as an estimate from logs/arcads-api.jsonl or MASTER_CONTEXT.md and confirm in the Arcads platform.
