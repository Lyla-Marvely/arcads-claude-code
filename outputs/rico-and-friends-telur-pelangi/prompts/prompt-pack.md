# Rico & Friends — Telur Pelangi — prompt pack

_Rico menemukan Telur Pelangi yang berkilau di hutan; satu per satu sahabatnya datang, dan mereka sepakat menjaganya bersama-sama._

> Generated offline by build_prompts.py. **No image or video has been generated.** Nothing below has been sent to any API.

## Negative prompts

**Image:** Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and spikes, horns, frill, neck and wings exactly as the master sheets; no extra or missing spikes or horns; no new characters or new baby dinosaurs; the egg must not hatch, crack or change; no accessories added; no logos, badges or text copied from the master sheets.

**Video:** No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No extra or missing spikes or horns; no new characters; the egg never hatches.

## Global continuity lock

- every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and spikes, horns, frill, neck and wings
- Rico keeps his turquoise body, cream belly, amber eyes and orange spikes (three orange head spikes) exactly as on his sheet
- relative scale as on the group sheet size comparison: Tika tallest, Rico taller than Bimo and Lila, Bimo and Lila similar, Piko the smallest body with wide wings
- the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed by the mossy rock in every scene, and never hatches, cracks or changes shape
- same clearing in every scene, warm golden daylight from camera-left, no time-of-day change
- only these five characters appear, no other creatures
- no scene cuts inside a clip; each clip is one continuous shot

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

### s01 — hook (10s)

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
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and spikes, horns, frill, neck and wings; Rico keeps his turquoise body, cream belly, amber eyes and orange spikes (three orange head spikes) exactly as on his sheet; relative scale as on the group sheet size comparison: Tika tallest, Rico taller than Bimo and Lila, Bimo and Lila similar, Piko the smallest body with wide wings; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed by the mossy rock in every scene, and never hatches, cracks or changes shape; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only these five characters appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico enters the frame behind the rock, left of the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and spikes, horns, frill, neck and wings exactly as the master sheets; no extra or missing spikes or horns; no new characters or new baby dinosaurs; the egg must not hatch, crack or change; no accessories added; no logos, badges or text copied from the master sheets.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 10 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-10s): Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes. One primary motion, smooth and readable.
Camera: wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock; slow, steady push in, no cuts.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
CONTINUITY LOCK — all five exactly as the master sheets, Rico with three orange head spikes; Tika tallest, Piko smallest body; same egg, same spot, never hatches; Rico enters the frame behind the rock, left of the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No extra or missing spikes or horns; no new characters; the egg never hatches.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 10s, 9:16. Rico in forest clearing: Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes. wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock, slow, steady push in, no cuts. Keep Rico identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s01 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock. Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes.
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and spikes, horns, frill, neck and wings; Rico keeps his turquoise body, cream belly, amber eyes and orange spikes (three orange head spikes) exactly as on his sheet; relative scale as on the group sheet size comparison: Tika tallest, Rico taller than Bimo and Lila, Bimo and Lila similar, Piko the smallest body with wide wings; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed by the mossy rock in every scene, and never hatches, cracks or changes shape; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only these five characters appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; Rico enters the frame behind the rock, left of the egg.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and spikes, horns, frill, neck and wings exactly as the master sheets; no extra or missing spikes or horns; no new characters or new baby dinosaurs; the egg must not hatch, crack or change; no accessories added; no logos, badges or text copied from the master sheets.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 10 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-10s): Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes. One primary motion, smooth and readable.
Camera: wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock; slow, steady push in, no cuts.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
CONTINUITY LOCK — all five exactly as the master sheets, Rico with three orange head spikes; Tika tallest, Piko smallest body; same egg, same spot, never hatches; Rico enters the frame behind the rock, left of the egg.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No extra or missing spikes or horns; no new characters; the egg never hatches.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 10s, 16:9. Rico in forest clearing: Rico peeks over the mossy rock, spots the Rainbow Egg shimmering in the flowers, his amber eyes go wide, then he steps out toward it with curious steps as sunlight catches his orange spikes. wide establishing shot of the clearing that slowly pushes in to a medium shot of Rico peeking over the mossy rock, slow, steady push in, no cuts. Keep Rico identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

### s02 — gathering (10s)

**VO:** Satu per satu, para sahabat datang. Mereka sepakat, telur ini harus dijaga bersama.

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = MASTER sheet references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png — owner-approved file, never regenerated; img3 = approved still of s01 (continuity anchor)

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`; `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`; `<approved still of s01, same ratio>`

#### s02 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium-wide shot of the clearing around the egg. Piko glides in from above and hovers near the egg, Lila and Bimo walk in from left and right, Tika's long neck lowers into frame, and all five gather around the Rainbow Egg with wonder.
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and spikes, horns, frill, neck and wings; Rico keeps his turquoise body, cream belly, amber eyes and orange spikes (three orange head spikes) exactly as on his sheet; relative scale as on the group sheet size comparison: Tika tallest, Rico taller than Bimo and Lila, Bimo and Lila similar, Piko the smallest body with wide wings; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed by the mossy rock in every scene, and never hatches, cracks or changes shape; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only these five characters appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; egg in the same spot as the end of s01.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and spikes, horns, frill, neck and wings exactly as the master sheets; no extra or missing spikes or horns; no new characters or new baby dinosaurs; the egg must not hatch, crack or change; no accessories added; no logos, badges or text copied from the master sheets.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 10 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s01) for continuity.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-10s): Piko glides in from above and hovers near the egg, Lila and Bimo walk in from left and right, Tika's long neck lowers into frame, and all five gather around the Rainbow Egg with wonder. One primary motion, smooth and readable.
Camera: medium-wide shot of the clearing around the egg; gentle, nearly static framing with a very slow drift to the right.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
CONTINUITY LOCK — all five exactly as the master sheets, Rico with three orange head spikes; Tika tallest, Piko smallest body; same egg, same spot, never hatches; egg in the same spot as the end of s01.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No extra or missing spikes or horns; no new characters; the egg never hatches.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 10s, 9:16. Rico and Piko and Lila and Bimo and Tika in forest clearing: Piko glides in from above and hovers near the egg, Lila and Bimo walk in from left and right, Tika's long neck lowers into frame, and all five gather around the Rainbow Egg with wonder. medium-wide shot of the clearing around the egg, gentle, nearly static framing with a very slow drift to the right. Keep Rico and Piko and Lila and Bimo and Tika identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s02 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — medium-wide shot of the clearing around the egg. Piko glides in from above and hovers near the egg, Lila and Bimo walk in from left and right, Tika's long neck lowers into frame, and all five gather around the Rainbow Egg with wonder.
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and spikes, horns, frill, neck and wings; Rico keeps his turquoise body, cream belly, amber eyes and orange spikes (three orange head spikes) exactly as on his sheet; relative scale as on the group sheet size comparison: Tika tallest, Rico taller than Bimo and Lila, Bimo and Lila similar, Piko the smallest body with wide wings; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed by the mossy rock in every scene, and never hatches, cracks or changes shape; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only these five characters appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; egg in the same spot as the end of s01.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and spikes, horns, frill, neck and wings exactly as the master sheets; no extra or missing spikes or horns; no new characters or new baby dinosaurs; the egg must not hatch, crack or change; no accessories added; no logos, badges or text copied from the master sheets.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 10 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s01) for continuity.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-10s): Piko glides in from above and hovers near the egg, Lila and Bimo walk in from left and right, Tika's long neck lowers into frame, and all five gather around the Rainbow Egg with wonder. One primary motion, smooth and readable.
Camera: medium-wide shot of the clearing around the egg; gentle, nearly static framing with a very slow drift to the right.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
CONTINUITY LOCK — all five exactly as the master sheets, Rico with three orange head spikes; Tika tallest, Piko smallest body; same egg, same spot, never hatches; egg in the same spot as the end of s01.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No extra or missing spikes or horns; no new characters; the egg never hatches.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 10s, 16:9. Rico and Piko and Lila and Bimo and Tika in forest clearing: Piko glides in from above and hovers near the egg, Lila and Bimo walk in from left and right, Tika's long neck lowers into frame, and all five gather around the Rainbow Egg with wonder. medium-wide shot of the clearing around the egg, gentle, nearly static framing with a very slow drift to the right. Keep Rico and Piko and Lila and Bimo and Tika identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

### s03 — resolution (10s)

**VO:** Karena sahabat sejati selalu menjaga hal berharga, bersama-sama.

**Video reference plan (Seedance, max 3):** img1 = this scene's approved storyboard still (same ratio); img2 = MASTER sheet references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png — owner-approved file, never regenerated; img3 = approved still of s02 (continuity anchor)

**Still reference files (gpt-image-2, max 5):** `references/character-library/Rico-and-Friends/rico-and-friends__group__master-sheet__v1.png`; `references/character-library/Rico-and-Friends/rico-and-friends__rico__master-sheet__v1.png`; `<approved still of s02, same ratio>`

#### s03 · 9:16

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; leave the top 12% and bottom 20% free of key details (platform UI safe zone).
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — wide shot of all five friends in a group arrangement like the Pose Grup Referensi on the group master sheet, around the egg. the egg's rainbow shimmer glows brighter and lights the friends' faces, they smile at each other, Rico looks around happily; the shot holds on the group.
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and spikes, horns, frill, neck and wings; Rico keeps his turquoise body, cream belly, amber eyes and orange spikes (three orange head spikes) exactly as on his sheet; relative scale as on the group sheet size comparison: Tika tallest, Rico taller than Bimo and Lila, Bimo and Lila similar, Piko the smallest body with wide wings; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed by the mossy rock in every scene, and never hatches, cracks or changes shape; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only these five characters appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; same positions as the end of s02.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and spikes, horns, frill, neck and wings exactly as the master sheets; no extra or missing spikes or horns; no new characters or new baby dinosaurs; the egg must not hatch, crack or change; no accessories added; no logos, badges or text copied from the master sheets.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 10 seconds, 9:16.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s02) for continuity.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-10s): the egg's rainbow shimmer glows brighter and lights the friends' faces, they smile at each other, Rico looks around happily; the shot holds on the group. One primary motion, smooth and readable.
Camera: wide shot of all five friends in a group arrangement like the Pose Grup Referensi on the group master sheet, around the egg; slow, smooth pull back, ending on a one-second hold.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
CONTINUITY LOCK — all five exactly as the master sheets, Rico with three orange head spikes; Tika tallest, Piko smallest body; same egg, same spot, never hatches; same positions as the end of s02.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No extra or missing spikes or horns; no new characters; the egg never hatches.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 10s, 9:16. Rico and Piko and Lila and Bimo and Tika in forest clearing: the egg's rainbow shimmer glows brighter and lights the friends' faces, they smile at each other, Rico looks around happily; the shot holds on the group. wide shot of all five friends in a group arrangement like the Pose Grup Referensi on the group master sheet, around the egg, slow, smooth pull back, ending on a one-second hold. Keep Rico and Piko and Lila and Bimo and Tika identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

#### s03 · 16:9

**Image prompt (gpt-image-2 / Nano Banana):**

```
Pixar-style 3D animated feature film look, soft golden sunlight, lush magical fantasy forest, vibrant saturated colors, glossy detailed scales and skin, large expressive eyes with catchlights, shallow depth of field with creamy bokeh.
Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); use the width for environment and leave room on one side for movement; keep key details inside the central 80% of the frame.
CHARACTER LOCK — Rico (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby fantasy dinosaur, as on the sheet; colors: turquoise body, cream belly, amber eyes, orange spikes, exactly as the sheet; spikes: three orange head spikes plus the orange spikes and dots shown on the sheet, same count, positions, size and hue; feet_tail: three toes and a short curved tail, as on the sheet). CHARACTER LOCK — Piko (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby pterodactyl, as on the sheet; features: blue body, wide wings and a blue crest, exactly as the sheet). CHARACTER LOCK — Lila (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: pink body, three horns and a light-pink frill, exactly as the sheet). CHARACTER LOCK — Bimo (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby triceratops, as on the sheet; features: yellow body, three horns and a yellow frill, exactly as the sheet). CHARACTER LOCK — Tika (design_source: the attached MASTER character sheet(s); copy exactly, do not redesign or reinterpret; species: baby brachiosaurus, as on the sheet; features: purple body, long neck and spotted pattern, exactly as the sheet).
SETTING LOCK — sunlit magical forest clearing, soft golden daylight through tall trees from camera-left, lush grass and colorful wildflowers in pink, purple and blue, a large mossy rock at center, the Rainbow Egg resting in a flower bed beside the rock, a small red-capped mushroom house with a softly lit window far away in the soft-focus background, warm and cozy.
SCENE — wide shot of all five friends in a group arrangement like the Pose Grup Referensi on the group master sheet, around the egg. the egg's rainbow shimmer glows brighter and lights the friends' faces, they smile at each other, Rico looks around happily; the shot holds on the group.
CONTINUITY LOCK — every character is copied EXACTLY from the attached master sheets: same colors, faces, eyes and spikes, horns, frill, neck and wings; Rico keeps his turquoise body, cream belly, amber eyes and orange spikes (three orange head spikes) exactly as on his sheet; relative scale as on the group sheet size comparison: Tika tallest, Rico taller than Bimo and Lila, Bimo and Lila similar, Piko the smallest body with wide wings; the Rainbow Egg looks exactly as on Rico's sheet (iridescent rainbow shell), keeps the same size and the same spot in the flower bed by the mossy rock in every scene, and never hatches, cracks or changes shape; same clearing in every scene, warm golden daylight from camera-left, no time-of-day change; only these five characters appear, no other creatures; no scene cuts inside a clip; each clip is one continuous shot; same positions as the end of s02.
Characters must match the attached reference image(s) exactly: same proportions, colors, outfit and facial features.
Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. No extra fingers, no merged or melted features, no warped props, no extra characters, no on-screen text, no captions, no subtitles, no watermark, no logos. Do not redesign any character: keep each character's colors, face, eyes and spikes, horns, frill, neck and wings exactly as the master sheets; no extra or missing spikes or horns; no new characters or new baby dinosaurs; the egg must not hatch, crack or change; no accessories added; no logos, badges or text copied from the master sheets.
```

**Video prompt (Seedance 2.0, image-to-video):**

```
3D animated film aesthetic, image-to-video animation, 10 seconds, 16:9.
Reference use: @(img1) is the exact first-frame look; @(img2) is the character lock sheet; @(img3) is the previous scene (s02) for continuity.
Subject: Rico, exactly as in the master sheet (turquoise body, cream belly, amber eyes, three orange head spikes). Piko, exactly as in the master sheet (blue baby pterodactyl, wide wings, blue crest). Lila, exactly as in the master sheet (pink baby triceratops, three horns, light-pink frill). Bimo, exactly as in the master sheet (yellow baby triceratops, three horns, yellow frill). Tika, exactly as in the master sheet (purple baby brachiosaurus, long neck, spots).
Setting: sunlit fantasy forest clearing, golden light from camera-left, mossy rock, Rainbow Egg in flowers beside it.
Action (0-10s): the egg's rainbow shimmer glows brighter and lights the friends' faces, they smile at each other, Rico looks around happily; the shot holds on the group. One primary motion, smooth and readable.
Camera: wide shot of all five friends in a group arrangement like the Pose Grup Referensi on the group master sheet, around the egg; slow, smooth pull back, ending on a one-second hold.
Style: Pixar-style 3D animated film look, soft golden sunlight, vibrant fantasy forest.
CONTINUITY LOCK — all five exactly as the master sheets, Rico with three orange head spikes; Tika tallest, Piko smallest body; same egg, same spot, never hatches; same positions as the end of s02.
Constraints: characters and setting stay visually identical to the references for the whole clip. No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, no on-screen text, captions or watermark. No extra or missing spikes or horns; no new characters; the egg never hatches.
```

**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**

```
Animate <image> as a Pixar-style 3D animated scene, 10s, 16:9. Rico and Piko and Lila and Bimo and Tika in forest clearing: the egg's rainbow shimmer glows brighter and lights the friends' faces, they smile at each other, Rico looks around happily; the shot holds on the group. wide shot of all five friends in a group arrangement like the Pose Grup Referensi on the group master sheet, around the egg, slow, smooth pull back, ending on a one-second hold. Keep Rico and Piko and Lila and Bimo and Tika identical to the image throughout; same outfit, colors and proportions. One continuous shot. Don't add text, captions, extra characters or scene cuts.
```

## Request count (before any generation)

- turnaround_images: 0
- scene_stills: 6
- scene_clips: 6
- total_scene_seconds_per_ratio: 30
- note: Counts only. Credit cost is NOT computed here; present it to the user as an estimate from logs/arcads-api.jsonl or MASTER_CONTEXT.md and confirm in the Arcads platform.
