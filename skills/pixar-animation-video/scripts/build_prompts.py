#!/usr/bin/env python3
"""Build per-scene image + video prompts from a project.json (offline, stdlib only).

This script NEVER calls an API and NEVER generates media. It only turns an
approved story/storyboard spec into copy-paste-ready prompts, a character lock
sheet, a continuity checklist, and a request/credit-count summary.

Usage:
  python3 build_prompts.py project.json --out outputs/<slug>/prompts
  python3 build_prompts.py project.json --check      # validate only, write nothing
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SEEDANCE_FORBIDDEN = ["cinematic", "professional", "stunning", "8k", "studio", "perfect"]
PIXAR_AVOID = ["anime", "ghibli", "cel-shaded", "dreamworks", "photorealistic", "live action", "live-action"]
SUPPORTED_RATIOS = {"9:16", "16:9"}          # Seedance 2.0 on Arcads: 9:16 and 16:9 only
SEEDANCE_DURATION = (4, 15)                   # seconds, per arcads reference.md
SEEDANCE_MAX_REFS = 3                         # referenceImages cap for seedance-2.0
GPT_IMAGE_MAX_REFS = 5                        # referenceImages cap for gpt-image-2
WORDS_PER_SECOND = 2.5                        # VO sanity ceiling (not a model limit)

DEFAULT_STYLE_LOCK = (
    "Disney-Pixar 3D animated feature film aesthetic, soft volumetric warm lighting, "
    "subsurface scattering, large expressive eyes with multiple catchlights, stylized but "
    "believable proportions, rich material detail, shallow depth of field with creamy bokeh, "
    "warm cozy color palette"
)

IMAGE_NEGATIVE = (
    "Not photorealistic, not live-action, not anime, not 2D, not cel-shaded, not flat illustration. "
    "No extra fingers, no merged or melted features, no warped props, no extra characters, "
    "no on-screen text, no captions, no subtitles, no watermark, no logos."
)

VIDEO_NEGATIVE = (
    "No live-action or photorealistic look, no anime or 2D look, no extra characters, no extra limbs, "
    "no morphing or melting, no costume or color changes, no scene cuts, no lighting jumps, "
    "no on-screen text, captions or watermark."
)

COMPOSITION = {
    "9:16": "Vertical 9:16 composition; keep the subject centered in the middle 70% of the frame; "
            "leave the top 12% and bottom 20% free of key details (platform UI safe zone).",
    "16:9": "Horizontal 16:9 composition re-framed for widescreen (do NOT crop a vertical image); "
            "use the width for environment and leave room on one side for movement; "
            "keep key details inside the central 80% of the frame.",
}


def neg(project: dict, base: str) -> str:
    extra = project.get("extra_negative", "").strip()
    return f"{base} {extra}" if extra else base


def neg_video(project: dict) -> str:
    extra = (project.get("extra_negative_video") or project.get("extra_negative", "")).strip()
    return f"{VIDEO_NEGATIVE} {extra}" if extra else VIDEO_NEGATIVE


def continuity_line(project: dict, sc: dict, video: bool = False) -> str:
    base = project.get("continuity_lock_video") if video and project.get("continuity_lock_video") else project.get("continuity_lock", [])
    items = list(base) + list(sc.get("continuity_notes", []))
    return ("CONTINUITY LOCK — " + "; ".join(items) + ".\n") if items else ""


def die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def video_lock_text(char: dict) -> str:
    """Compact lock for video prompts: the reference images carry identity, so keep it short."""
    return char.get("short_lock") or lock_text(char)


def lock_text(char: dict) -> str:
    parts = [f"{k}: {v}" for k, v in char.get("lock", {}).items()]
    return f"{char['name']} ({'; '.join(parts)})"


def repo_root(start: Path) -> Path:
    for d in [start.resolve(), *start.resolve().parents]:
        if (d / "CLAUDE.md").is_file() and (d / "references").is_dir():
            return d
    return Path.cwd()


def sheet_path(root: Path, ref: str) -> Path:
    """master_sheet / reference_sheet may be a repo-relative path; free text descriptions never resolve."""
    return root / ref


def validate(project: dict, root: Path | None = None) -> list[str]:
    problems: list[str] = []
    ratios = project.get("ratios", ["9:16", "16:9"])
    bad = [r for r in ratios if r not in SUPPORTED_RATIOS]
    if bad:
        problems.append(f"unsupported ratio(s) {bad}; supported: {sorted(SUPPORTED_RATIOS)}")
    chars = {c["id"]: c for c in project.get("characters", [])}
    sets = {s["id"]: s for s in project.get("settings", [])}
    if root is not None:
        for c in chars.values():
            for ref in ([c["master_sheet"]] if c.get("master_sheet") else []):
                if not sheet_path(root, ref).is_file():
                    problems.append(f"character '{c['id']}': master_sheet file not found on disk: {ref} (never plan with a sheet that does not exist)")
        for sc in project.get("scenes", []):
            ref = sc.get("reference_sheet")
            if ref and not sheet_path(root, ref).is_file():
                problems.append(f"{sc.get('id','?')}: reference_sheet file not found on disk: {ref}")
    if not project.get("scenes"):
        problems.append("no scenes defined")
    seen = set()
    for sc in project.get("scenes", []):
        sid = sc.get("id", "?")
        if sid in seen:
            problems.append(f"{sid}: duplicate scene id")
        seen.add(sid)
        d = sc.get("duration")
        if not isinstance(d, int) or not (SEEDANCE_DURATION[0] <= d <= SEEDANCE_DURATION[1]):
            problems.append(f"{sid}: duration must be an integer {SEEDANCE_DURATION[0]}-{SEEDANCE_DURATION[1]}s (got {d!r})")
        for cid in sc.get("characters", []):
            if cid not in chars:
                problems.append(f"{sid}: unknown character id '{cid}'")
        if sc.get("setting") not in sets:
            problems.append(f"{sid}: unknown setting id '{sc.get('setting')}'")
        cf = sc.get("continuity_from")
        if cf and cf not in {s.get("id") for s in project["scenes"]}:
            problems.append(f"{sid}: continuity_from '{cf}' does not exist")
        vo = sc.get("vo", "")
        if vo and isinstance(d, int):
            words = len(vo.split())
            if words / WORDS_PER_SECOND > d:
                problems.append(f"{sid}: VO has {words} words, likely longer than {d}s (>{WORDS_PER_SECOND} words/s)")
    # forbidden words in user-authored text that flows into Seedance prompts
    blob = json.dumps(project, ensure_ascii=False).lower()
    for w in SEEDANCE_FORBIDDEN:
        if re.search(rf"\b{re.escape(w)}\b", blob):
            problems.append(f"project text contains Seedance-forbidden word '{w}' (rewrite it)")
    for w in PIXAR_AVOID:
        if re.search(rf"\b{re.escape(w)}\b", json.dumps(project.get('style_lock', '')).lower()):
            problems.append(f"style_lock contains '{w}', which pulls away from the Pixar look")
    return problems


def build_image_prompt(project, sc, ratio, chars, sets) -> str:
    style = project.get("style_lock", DEFAULT_STYLE_LOCK)
    cast = " ".join(f"CHARACTER LOCK — {lock_text(chars[c])}." for c in sc.get("characters", []))
    return (
        f"{style}.\n"
        f"{COMPOSITION[ratio]}\n"
        f"{cast}\n"
        f"SETTING LOCK — {sets[sc['setting']]['lock']}.\n"
        f"SCENE — {sc['shot']}. {sc['action']}.\n"
        f"{continuity_line(project, sc)}"
        f"Characters must match the attached reference image(s) exactly: same proportions, "
        f"colors, outfit and facial features.\n"
        f"{neg(project, IMAGE_NEGATIVE)}"
    )


def ref_plan(sc, chars=None) -> list[str]:
    plan = ["img1 = this scene's approved storyboard still (same ratio)"]
    master = next((chars[c] for c in sc.get("characters", []) if chars and chars[c].get("master_sheet")), None)
    if sc.get("reference_sheet"):
        plan.append(f"img2 = MASTER sheet {sc['reference_sheet']} — owner-approved file, never regenerated")
    elif master:
        plan.append(f"img2 = {master['name']} MASTER character sheet ({master['master_sheet']}) — user-supplied, never regenerated")
    else:
        plan.append("img2 = character turnaround/lock sheet (same characters as this scene)")
    if sc.get("continuity_from"):
        plan.append(f"img3 = approved still of {sc['continuity_from']} (continuity anchor)")
    return plan


def still_refs(sc, chars) -> list[str]:
    """Reference files for the STILL (image model; gpt-image-2 accepts max 5)."""
    refs = []
    if sc.get("reference_sheet"):
        refs.append(sc["reference_sheet"])
    for c in sc.get("characters", []):
        m = chars[c].get("master_sheet")
        if m and m not in refs:
            refs.append(m)
    if sc.get("continuity_from"):
        refs.append(f"<approved still of {sc['continuity_from']}, same ratio>")
    return refs


def build_seedance_prompt(project, sc, ratio, chars, sets) -> str:
    style = project.get("style_lock", DEFAULT_STYLE_LOCK)
    cast = " ".join(f"{video_lock_text(chars[c])}." for c in sc.get("characters", []))
    style = project.get("style_lock_video", style)
    setting_text = sets[sc["setting"]].get("video_lock", sets[sc["setting"]]["lock"])
    refs = "@(img1) is the exact first-frame look; @(img2) is the character lock sheet"
    if sc.get("continuity_from"):
        refs += f"; @(img3) is the previous scene ({sc['continuity_from']}) for continuity"
    dur = sc["duration"]
    return (
        f"3D animated film aesthetic, image-to-video animation, {dur} seconds, {ratio}.\n"
        f"Reference use: {refs}.\n"
        f"Subject: {cast}\n"
        f"Setting: {setting_text}.\n"
        f"Action (0-{dur}s): {sc['action']}. One primary motion, smooth and readable.\n"
        f"Camera: {sc['shot']}; {sc['camera']}.\n"
        f"Style: {style}.\n"
        f"{continuity_line(project, sc, video=True)}"
        f"Constraints: characters and setting stay visually identical to the references for the whole clip. "
        f"{neg_video(project)}"
    )


def build_omni_prompt(project, sc, ratio, chars, sets) -> str:
    # Omni wants intent, not over-specification; pin duration + ratio, reference the image, add exclusions.
    names = " and ".join(chars[c]["name"] for c in sc.get("characters", []))
    return (
        f"Animate <image> as a Pixar-style 3D animated scene, {sc['duration']}s, {ratio}. "
        f"{names} in {sets[sc['setting']]['id'].replace('-', ' ')}: {sc['action']}. "
        f"{sc['shot']}, {sc['camera']}. Keep {names} identical to the image throughout; "
        f"same outfit, colors and proportions. One continuous shot. "
        f"Don't add text, captions, extra characters or scene cuts."
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project", type=Path)
    ap.add_argument("--out", type=Path, help="output directory (default: ./prompts next to project.json)")
    ap.add_argument("--check", action="store_true", help="validate only; write nothing")
    args = ap.parse_args()

    project = json.loads(args.project.read_text(encoding="utf-8"))
    problems = validate(project, repo_root(args.project))
    if problems:
        print("Validation problems:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        sys.exit(2)
    print("Validation OK.")
    if args.check:
        return

    chars = {c["id"]: c for c in project["characters"]}
    sets = {s["id"]: s for s in project["settings"]}
    ratios = project.get("ratios", ["9:16", "16:9"])
    out = args.out or args.project.parent / "prompts"
    out.mkdir(parents=True, exist_ok=True)

    result = {"title": project["title"], "ratios": ratios, "characters": [], "scenes": []}
    md = [f"# {project['title']} — prompt pack\n", f"_{project.get('logline', '')}_\n",
          "> Generated offline by build_prompts.py. **No image or video has been generated.** "
          "Nothing below has been sent to any API.\n"]

    md.append("## Character lock sheet\n")
    if project.get("continuity_lock"):
        md.insert(3, "## Global continuity lock\n\n" + "\n".join(f"- {i}" for i in project["continuity_lock"]) + "\n")
    md.insert(3, "## Negative prompts\n\n**Image:** " + neg(project, IMAGE_NEGATIVE) + "\n\n**Video:** " + neg_video(project) + "\n")
    for c in project["characters"]:
        if c.get("master_sheet"):
            result["characters"].append({"id": c["id"], "lock": lock_text(c), "master_sheet": c["master_sheet"], "turnaround_prompt": None})
            md.append(f"### {c['name']} (`{c['id']}`) — MASTER SHEET (design locked)\n\n**Lock:** {lock_text(c)}\n\n"
                      f"**Master sheet file:** `{c['master_sheet']}`  \n_Supplied by the user. Do NOT generate a new turnaround; "
                      f"attach this file as a reference (re-upload for every call — presigned paths are one-time use)._\n")
            continue
        sheet = (
            f"{project.get('style_lock', DEFAULT_STYLE_LOCK)}. Character turnaround sheet on a plain "
            f"soft cream background: front view, 3/4 view, side view and back view of {lock_text(c)}, "
            f"plus three close-up expressions (happy, surprised, worried). Full body visible, consistent "
            f"proportions across all views, no props, no text labels. {IMAGE_NEGATIVE}"
        )
        result["characters"].append({"id": c["id"], "lock": lock_text(c), "turnaround_prompt": sheet})
        md.append(f"### {c['name']} (`{c['id']}`)\n\n**Lock:** {lock_text(c)}\n\n**Turnaround prompt:**\n\n```\n{sheet}\n```\n")

    md.append("## Scenes\n")
    for sc in project["scenes"]:
        sr = still_refs(sc, chars)
        n_img_refs = len(sr)
        if n_img_refs > GPT_IMAGE_MAX_REFS:
            print(f"WARNING: {sc['id']} needs {n_img_refs} still references (gpt-image-2 max {GPT_IMAGE_MAX_REFS})", file=sys.stderr)
        entry = {"id": sc["id"], "still_reference_files": sr, "image_reference_files": n_img_refs, "beat": sc.get("beat"), "duration": sc["duration"],
                 "vo": sc.get("vo", ""), "reference_plan": ref_plan(sc, chars), "ratios": {}}
        md.append(f"### {sc['id']} — {sc.get('beat', '')} ({sc['duration']}s)\n")
        md.append(f"**VO:** {sc.get('vo', '—')}\n\n**Video reference plan (Seedance, max 3):** " + "; ".join(ref_plan(sc, chars)) +
                  "\n\n**Still reference files (gpt-image-2, max 5):** " + "; ".join(f"`{x}`" for x in sr) + "\n")
        for r in ratios:
            ip = build_image_prompt(project, sc, r, chars, sets)
            sp = build_seedance_prompt(project, sc, r, chars, sets)
            op = build_omni_prompt(project, sc, r, chars, sets)
            wc = len(sp.split())
            if wc > 260:
                print(f"WARNING: {sc['id']} {r} Seedance prompt is {wc} words (guide target 100-260); add short_lock / continuity_lock_video / extra_negative_video", file=sys.stderr)
            entry["ratios"][r] = {"image_prompt": ip, "seedance_prompt": sp, "omni_prompt": op}
            md.append(f"#### {sc['id']} · {r}\n\n**Image prompt (gpt-image-2 / Nano Banana):**\n\n```\n{ip}\n```\n\n"
                      f"**Video prompt (Seedance 2.0, image-to-video):**\n\n```\n{sp}\n```\n\n"
                      f"**Video prompt (Gemini Omni Flash — only if available, see SKILL.md):**\n\n```\n{op}\n```\n")
        result["scenes"].append(entry)

    n_scenes, n_ratios = len(project["scenes"]), len(ratios)
    summary = {
        "turnaround_images": sum(1 for c in project["characters"] if not c.get("master_sheet")),
        "scene_stills": n_scenes * n_ratios,
        "scene_clips": n_scenes * n_ratios,
        "total_scene_seconds_per_ratio": sum(s["duration"] for s in project["scenes"]),
        "note": "Counts only. Credit cost is NOT computed here; present it to the user as an estimate "
                "from logs/arcads-api.jsonl or MASTER_CONTEXT.md and confirm in the Arcads platform.",
    }
    result["request_summary"] = summary
    md.append("## Request count (before any generation)\n\n" + "\n".join(f"- {k}: {v}" for k, v in summary.items()) + "\n")

    (out / "prompts.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "prompt-pack.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {out/'prompts.json'} and {out/'prompt-pack.md'}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
