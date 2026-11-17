#!/usr/bin/env python3
"""Pre-production verification of a pixar-animation-video prompt pack (offline, read-only).

Runs the quality gates against project.json + prompts.json (+ the storyboard document) and writes a
PASS/FAIL report. Makes no API call and generates nothing.

Usage:
  python3 verify_pack.py <pack_dir> [--storyboard story-script-storyboard.md] [--report final-verification-report.md]
Exit code 0 only if every check passes.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ID_STOP = {"yang", "dengan", "untuk", "adalah", "ini", "itu", "pada", "dari", "akan", "mereka", "karena",
           "bersama", "sahabat", "telur", "pagi", "hutan", "menemukan", "datang", "satu", "para", "pun"}


def repo_root(start: Path) -> Path:
    for d in [start.resolve(), *start.resolve().parents]:
        if (d / "CLAUDE.md").is_file() and (d / "references").is_dir():
            return d
    return Path.cwd()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pack_dir", type=Path)
    ap.add_argument("--storyboard", default="story-script-storyboard.md")
    ap.add_argument("--report", default="final-verification-report.md")
    a = ap.parse_args()
    D = a.pack_dir
    root = repo_root(D)
    project = json.loads((D / "project.json").read_text(encoding="utf-8"))
    packj = json.loads((D / "prompts" / "prompts.json").read_text(encoding="utf-8"))
    story = (D / a.storyboard).read_text(encoding="utf-8") if (D / a.storyboard).is_file() else ""
    chars = {c["id"]: c for c in project["characters"]}
    names = {cid: c["name"] for cid, c in chars.items()}
    scenes = project["scenes"]
    pscenes = {s["id"]: s for s in packj["scenes"]}
    results: list[tuple[str, str, bool, str]] = []

    def add(num, title, ok, detail):
        results.append((num, title, bool(ok), detail))

    def prompts_of(sid):
        for r, v in pscenes[sid]["ratios"].items():
            for kind in ("image_prompt", "seedance_prompt", "omni_prompt"):
                yield r, kind, v[kind]

    # 1 six clips match the storyboard
    base = [s for s in scenes if not s.get("optional")]
    ids = [s["id"] for s in scenes]
    total = sum(s["duration"] for s in base)
    rows = {int(m.group(1)): int(m.group(2)) for m in re.finditer(r"\|\s*\**S0(\d)\b[^|]*\|\s*(\d+)\s*s", story)}
    doc_ok = all(rows.get(i + 1) == s["duration"] for i, s in enumerate(scenes))
    add("1", "Six clips, no S07, ~30 s, match the storyboard",
        len(scenes) == 6 and ids == [f"s0{i}" for i in range(1, 7)] and not any(s.get("optional") for s in scenes) and 28 <= total <= 32 and doc_ok,
        f"clips={len(scenes)} ids={ids} total={total}s; durations in storyboard doc match project.json: {doc_ok}")
    # 2 max three characters
    counts = {s["id"]: len(s["characters"]) for s in scenes}
    add("2", "Maximum three characters per clip", max(counts.values()) <= 3, f"characters per clip: {counts}")
    # 3 prompts only contain present characters (and name each present one)
    bad, miss = [], []
    for s in scenes:
        present = {names[c] for c in s["characters"]}
        for r, kind, t in prompts_of(s["id"]):
            for n in set(names.values()) - present:
                if re.search(rf"\b{re.escape(n)}\b", t):
                    bad.append(f"{s['id']} {r} {kind}: {n}")
            if kind != "omni_prompt":
                for n in present:
                    if not re.search(rf"\b{re.escape(n)}\b", t):
                        miss.append(f"{s['id']} {r} {kind}: {n}")
    add("3", "Every prompt names only the characters present in the scene", not bad and not miss,
        f"absent-character mentions: {bad or 'none'}; present characters missing: {miss or 'none'}; prompts scanned: {sum(1 for s in scenes for _ in prompts_of(s['id']))}")
    # 4 English-only speech
    vo_bad = []
    for s in scenes:
        vo = s.get("vo", "")
        if not vo.strip():
            vo_bad.append(f"{s['id']}: empty VO")
        words = set(re.findall(r"[a-zA-Z']+", vo.lower()))
        if words & ID_STOP:
            vo_bad.append(f"{s['id']}: Indonesian word(s) {sorted(words & ID_STOP)}")
        if re.search(r"[^\x00-\x7f]", vo):
            vo_bad.append(f"{s['id']}: non-ASCII characters")
        if s.get("dialogue"):
            vo_bad.append(f"{s['id']}: has dialogue (none planned)")
    prompt_blob = " ".join(t for s in scenes for _, _, t in prompts_of(s["id"])).lower()
    idw = sorted(set(re.findall(r"[a-zA-Z']+", prompt_blob)) & ID_STOP)
    add("4", "All voice-over and dialogue are English", not vo_bad and not idw and project.get("vo_language") == "en" and project.get("silent_characters"),
        f"vo_language={project.get('vo_language')}, silent_characters={project.get('silent_characters')}; VO issues: {vo_bad or 'none'}; Indonesian words in prompts: {idw or 'none'}; "
        f"VO word counts: {[len(s['vo'].split()) for s in scenes]}")
    # 5 no Pip / Moss
    scan_project = {k: v for k, v in project.items() if k != "forbidden_prompt_terms"}  # the guard list itself names the terms
    full = json.dumps(scan_project, ensure_ascii=False) + json.dumps(packj, ensure_ascii=False)
    pm = re.findall(r"\b(pip|moss)\b", full, re.I)
    guarded = {t.lower() for t in project.get("forbidden_prompt_terms", [])} >= {"pip", "moss"}
    add("5", "No Pip or Moss (and the builder guard for them is configured)", not pm and guarded,
        f"matches: {pm or 'none'}; builder guard active for Pip/Moss: {guarded} (the word 'mossy' is a rock description and is not a match)")
    # 6 no LYLA MARVELY in any prompt or lock
    scan = {"prompts": prompt_blob}
    lock_txt = json.dumps({k: project.get(k) for k in ("style_lock", "style_lock_video", "reference_note", "reference_note_video", "extra_negative",
                                                     "video_negative_override", "continuity_lock", "continuity_lock_video", "characters", "settings", "scenes", "audio")}, ensure_ascii=False).lower()
    lm = [k for k, v in {"prompts": prompt_blob, "locks_and_scenes": lock_txt}.items() if re.search(r"marvely", v)]
    add("6", "No LYLA MARVELY badge or text in prompts or locks (QA checklist may name it to reject it)", not lm,
        f"found in: {lm or 'nowhere'}; every prompt also forbids any badge/logo/text/sheet layout: "
        f"{all(re.search(r'badge', t, re.I) for s in scenes for _, k, t in prompts_of(s['id']) if k != 'omni_prompt')}")
    # 7 egg is an object
    egg_bad = []
    for s in scenes:
        for r, kind, t in prompts_of(s["id"]):
            if kind == "omni_prompt":
                continue
            if not re.search(r"still object", t):
                egg_bad.append(f"{s['id']} {r} {kind}: no 'still object' rule")
            for m in re.finditer(r"hatch|crack", t, re.I):
                pre = re.split(r"[.;]", t[:m.start()])[-1].lower()  # same sentence/clause only; a "no" from an earlier sentence does not count
                if not re.search(r"\b(no|never|not|nor|without)\b", pre):
                    egg_bad.append(f"{s['id']} {r} {kind}: '{m.group(0)}' without a nearby negation")
        for key in ("shot", "action", "camera"):
            txt = s.get(key, "")
            # egg given a body part ("egg ... face/eyes/mouth/limbs/arms/legs" within a few words) or hatching/cracking/moving by itself
            if re.search(r"hatch|crack|\begg\W+(?:\w+\W+){0,3}(?:face|eyes|mouth|limbs|arms|legs)|\begg\W+(?:\w+\W+){0,2}(?:rolls|hops|moves|wobbles|jumps)", txt, re.I):
                egg_bad.append(f"{s['id']}: egg given life, a body part or movement in {key}: {txt!r}")
    add("7", "Egg stays an object: no hatching, cracks, face, limbs or self-movement", not egg_bad, f"issues: {egg_bad or 'none'}")
    # 8 locks complete
    lock_bad = []
    for s in scenes:
        n = len(s["characters"])
        for r, v in pscenes[s["id"]]["ratios"].items():
            ip, sp = v["image_prompt"], v["seedance_prompt"]
            if ip.count("CHARACTER LOCK —") != n: lock_bad.append(f"{s['id']} {r}: image CHARACTER LOCK count != {n}")
            if sp.count("exactly as in the master sheet") != n: lock_bad.append(f"{s['id']} {r}: video lock count != {n}")
            for need in ("CONTINUITY LOCK", "SETTING LOCK"):
                if need not in ip: lock_bad.append(f"{s['id']} {r}: image lacks {need}")
            if "CONTINUITY LOCK" not in sp: lock_bad.append(f"{s['id']} {r}: video lacks CONTINUITY LOCK")
            if "Negative:" not in sp or "No " not in ip: lock_bad.append(f"{s['id']} {r}: negative missing")
    add("8", "Character lock, continuity lock, setting lock and negative present in every prompt", not lock_bad, f"issues: {lock_bad or 'none'}")
    # 9 both formats
    fmt_bad = []
    for s in scenes:
        rr = pscenes[s["id"]]["ratios"]
        if set(rr) != {"9:16", "16:9"}: fmt_bad.append(f"{s['id']}: ratios {sorted(rr)}")
        for r, v in rr.items():
            if r not in v["image_prompt"] or r not in v["seedance_prompt"]: fmt_bad.append(f"{s['id']} {r}: ratio not stated")
    add("9", "Vertical 9:16 and horizontal 16:9 available for every clip", not fmt_bad, f"issues: {fmt_bad or 'none'}")
    # 10 generator readiness
    rd_bad, info = [], []
    for s in scenes:
        e = pscenes[s["id"]]
        stills = e["still_reference_files"]
        files = [x for x in stills if not x.startswith("<")]
        if len(stills) > 5: rd_bad.append(f"{s['id']}: {len(stills)} still refs > 5")
        for f in files:
            if not (root / f).is_file(): rd_bad.append(f"{s['id']}: missing file {f}")
        if len(e["reference_plan"]) > 3: rd_bad.append(f"{s['id']}: {len(e['reference_plan'])} video refs > 3")
        if not 4 <= s["duration"] <= 15: rd_bad.append(f"{s['id']}: duration {s['duration']} outside 4-15")
        for r, k, t in prompts_of(s["id"]):
            if re.search(r"TODO|XXX|\{[a-z_]+\}", t): rd_bad.append(f"{s['id']} {r} {k}: unresolved placeholder")
            if not t.strip(): rd_bad.append(f"{s['id']} {r} {k}: empty")
        info.append(max(len(v["seedance_prompt"].split()) for v in e["ratios"].values()))
    add("10", "Image and video prompts are generator-ready (refs within limits, files exist, durations valid, no placeholders)", not rd_bad,
        f"issues: {rd_bad or 'none'}; Seedance prompt words per clip: {info} (guide target 100-260; no documented API limit); "
        f"stills use gpt-image-2 (max 5 refs), videos use seedance-2.0 (max 3 refs, 9:16/16:9 only, 4-15 s); recommended audioEnabled=false")
    # 11 character gate (official sheets)
    gate = subprocess.run([str(root / "scripts/check-character-library.sh"), "Rico-and-Friends"] +
                          [x for c in chars.values() for x in ("--character", c["name"])], capture_output=True, text=True, cwd=root)
    passes = gate.stdout.count("CHARACTER PASS")
    add("11", "Character library gate passes for every character used", gate.returncode == 0 and passes == len(chars), f"{passes}/{len(chars)} CHARACTER PASS, exit={gate.returncode}")
    integ = subprocess.run([str(root / "scripts/check-character-library.sh")], capture_output=True, text=True, cwd=root)
    add("12", "Library integrity (master sheets unchanged: hashes, no missing or duplicate files)", integ.returncode == 0, integ.stdout.strip().splitlines()[-1] if integ.stdout else "no output")
    # 13 nothing generated
    media = [str(p.relative_to(root)) for p in D.rglob("*") if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".mp4", ".mov", ".mp3", ".wav"}]
    logs = subprocess.run(["git", "diff", "--stat", "--", "logs/arcads-api.jsonl"], capture_output=True, text=True, cwd=root).stdout.strip()
    add("13", "Nothing generated and no credits used (no media files in the pack, no new API log entries)", not media and not logs,
        f"media files in pack: {media or 'none'}; uncommitted API log changes: {logs or 'none'}")

    ok = all(r[2] for r in results)
    lines = ["# Final verification report", "", f"Result: **{'ALL CHECKS PASS' if ok else 'FAILURES PRESENT'}** ({sum(r[2] for r in results)}/{len(results)})", "",
             "Generated by `skills/pixar-animation-video/scripts/verify_pack.py` (offline, read-only; no API call).", "",
             "| # | Check | Result | Evidence |", "|---|-------|--------|----------|"]
    for n, t, o, d in results:
        lines.append(f"| {n} | {t} | {'PASS' if o else '**FAIL**'} | {d.replace('|', '/')} |")
    (D / a.report).write_text("\n".join(lines) + "\n", encoding="utf-8")
    for n, t, o, d in results:
        print(f"[{'PASS' if o else 'FAIL'}] {n}. {t}")
        if not o:
            print("       ", d)
    print(f"\n{'ALL CHECKS PASS' if ok else 'FAILURES PRESENT'} — report: {D / a.report}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
