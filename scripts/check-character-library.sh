#!/usr/bin/env bash
# Character + brand-asset library check. Read-only; reads library.json and the disk. Generates nothing.
#
#   ./scripts/check-character-library.sh                                   # integrity summary of all projects (exit 1 on any integrity problem)
#   ./scripts/check-character-library.sh Rico-and-Friends                  # gate: exit 0 only if >=1 character is APPROVED (file present, hash ok)
#   ./scripts/check-character-library.sh The-Last-Letter --character Maya # per-character gate; prints the character LOCK + reference files
#   ./scripts/check-character-library.sh LYLA-Anime-Universe --character Maya --character "Lady Aradena"
#                                                                          # universe-aware: Maya resolves to her home project's sheets
#   ./scripts/check-character-library.sh Arsein-Research --brand           # brand gate: APPROVED primary logo (default)
#   ./scripts/check-character-library.sh Arsein-Research --brand --logo alternate
#
# Character assets ('assets') and brand assets ('brand_assets') are tracked separately.
# Character names are NOT unique across projects: always work as <Project>:<Name>.
# Override the library location (tests): CHARACTER_LIBRARY_DIR=/path
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LIB="${CHARACTER_LIBRARY_DIR:-$ROOT/references/character-library}"
exec python3 -I - "$LIB" "$@" <<'PY'
import hashlib, json, sys
from collections import defaultdict
from pathlib import Path

lib = Path(sys.argv[1]); args = sys.argv[2:]
want, brand, logo, chars_wanted = "", False, "primary", []
i = 0
while i < len(args):
    a = args[i]
    if a == "--brand": brand = True
    elif a == "--logo": i += 1; logo = args[i]
    elif a == "--character": i += 1; chars_wanted.append(args[i])
    elif a.startswith("--"): print(f"FAIL: unknown option {a}"); sys.exit(1)
    elif not want: want = a
    else: print(f"FAIL: unexpected argument {a}"); sys.exit(1)
    i += 1
if logo not in ("primary", "alternate"): print("FAIL: --logo must be primary|alternate"); sys.exit(1)

reg_path = lib / "library.json"
if not reg_path.is_file(): print(f"FAIL: {reg_path} not found"); sys.exit(1)
reg = json.loads(reg_path.read_text(encoding="utf-8"))
projects = reg["projects"]; types = set(reg.get("brand_asset_types", {}))
IMG = {".jpg", ".jpeg", ".webp", ".png", ".svg", ".pdf"}
if want and want not in projects:
    print(f"FAIL: unknown project '{want}'. Known: {', '.join(projects)}"); sys.exit(1)

hashes = defaultdict(list)           # sha256 -> files (duplicate detection)
def sha_of(f):
    return hashlib.sha256(f.read_bytes()).hexdigest()

def char_status(a):
    cs = a.get("characters_status")
    return cs if cs else {c: a.get("status") for c in a.get("characters", [])}

def inspect(pn, p):
    r = {"n": 0, "bn": 0, "missing": [], "bad_hash": [], "bad_type": [], "wrong_folder": [], "forbidden": [],
         "unreg": [], "approved_chars": defaultdict(list), "all_chars": defaultdict(list), "official_unmet": [], "brand_ok": defaultdict(int)}
    known = set()
    for kind, items in (("char", p.get("assets", [])), ("brand", p.get("brand_assets", []))):
        for a in items:
            r["n" if kind == "char" else "bn"] += 1
            f = lib / a["file"]; known.add(f.resolve())
            if not (a["file"].startswith(p["folder"] + "/")): r["wrong_folder"].append(a["file"])
            if kind == "brand" and a.get("type") not in types: r["bad_type"].append(f"{a['file']} (type={a.get('type')!r})")
            if not f.is_file(): r["missing"].append(a["file"]); continue
            h = sha_of(f); hashes[h].append(a["file"])
            if a.get("sha256") and h != a["sha256"]: r["bad_hash"].append(a["file"]); continue
            if kind == "char":
                for c, st in char_status(a).items():
                    r["all_chars"][c].append(a["file"])
                    if st == "approved": r["approved_chars"][c].append(a["file"])
                    if c in p.get("forbidden_characters", []): r["forbidden"].append(f"{c} in {a['file']}")
            elif a.get("status") == "approved":
                r["brand_ok"][a.get("type")] += 1
    folder = lib / p["folder"]
    if folder.is_dir():
        for f in folder.rglob("*"):
            if f.is_file() and f.suffix.lower() in IMG and f.resolve() not in known: r["unreg"].append(str(f.relative_to(lib)))
    else: r["missing"].append(f"(folder {p['folder']} missing)")
    for c in p.get("official_characters", []):
        if c not in r["approved_chars"]: r["official_unmet"].append(c)
    return r

res = {n: inspect(n, p) for n, p in projects.items()}
dups = [fs for fs in hashes.values() if len(fs) > 1]
unreg_dups = []
for n, r in res.items():
    for rel in r["unreg"]:
        h = sha_of(lib / rel)
        if h in hashes: unreg_dups.append(f"{rel} is an exact copy of registered {hashes[h][0]}")

# ---- integrity report -------------------------------------------------------
integrity = []
print(f"{'project':22} {'assets':>6} {'appr.chars':>10} {'plan':>4} | {'brand':>5} {'ok':>3} | notes")
show = [want] if want else list(projects)
for n in show:
    r = res[n]; p = projects[n]; notes = []
    for k, lab in (("missing", "MISSING FILES"), ("bad_hash", "HASH MISMATCH"), ("bad_type", "BAD BRAND TYPE"),
                   ("wrong_folder", "WRONG FOLDER"), ("forbidden", "FORBIDDEN CHARACTER"), ("unreg", "UNREGISTERED FILES")):
        if r[k]: notes.append(f"{lab}: {len(r[k])}"); integrity += [f"{n}: {lab}: {x}" for x in r[k]]
    if r["official_unmet"]: notes.append(f"official w/o approved sheet: {', '.join(r['official_unmet'])}")
    if r["n"] == 0 and r["bn"] == 0 and not r["unreg"]: notes.append("empty (nothing uploaded)")
    print(f"{n:22} {r['n']:>6} {len(r['approved_chars']):>10} {len(p.get('planned_sheets', [])):>4} | {r['bn']:>5} {sum(r['brand_ok'].values()):>3} | {'; '.join(notes)}")
for fs in dups:
    integrity.append("DUPLICATE CONTENT: " + " == ".join(fs))
    print("    DUPLICATE CONTENT:", " == ".join(fs))
for u in unreg_dups: integrity.append("UNREGISTERED DUPLICATE: " + u); print("    DUPLICATE:", u)
for x in integrity: print("    !", x)

names = defaultdict(set)
for n, p in projects.items():
    for a in p.get("assets", []):
        for c in a.get("characters", []): names[c].add(n)
shared = {c: sorted(ps) for c, ps in names.items() if len(ps) > 1}
if shared and not want:
    print("\nSame name in several projects (DIFFERENT characters unless the projects share a universe; use <Project>:<Name>):")
    for c, ps in sorted(shared.items()): print(f"    {c}: {', '.join(ps)}")

# ---- gates -----------------------------------------------------------------
def fail(msg): print("\n" + msg); sys.exit(1)
if not want:
    if integrity: fail(f"INTEGRITY FAIL: {len(integrity)} problem(s) above.")
    print("\nINTEGRITY OK: no missing files, hash mismatches, duplicates, wrong-folder assets or unregistered files.")
    sys.exit(0)

r = res[want]; p = projects[want]
proj_bad = [x for x in integrity if x.startswith(want + ":") or x.startswith("DUPLICATE")]
if brand:
    ok = r["brand_ok"].get(f"logo_{logo}", 0) >= 1 and not (r["missing"] or r["bad_hash"] or r["bad_type"])
    if ok: print(f"\nBRAND GATE PASS: {want} has an approved {logo} logo."); sys.exit(0)
    fail(f"BRAND GATE FAIL: {want} has no usable APPROVED {logo} logo. Do not place any logo; never redraw or invent one.")

if chars_wanted:
    uni = projects[want].get("universe"); cand = [want] + [x for x in reg.get("universes", {}).get(uni, {}).get("projects", []) if x != want] if uni else [want]
    rc = 0
    template = reg.get("character_lock_template", "")
    for c in chars_wanted:
        home = next((x for x in cand if c in res[x]["all_chars"]), None)
        if home is None:
            print(f"\nCHARACTER FAIL: '{want}:{c}' not found (searched: {', '.join(cand)}). Do not invent it."); rc = 1; continue
        owners = [x for x in cand if c in res[x]["all_chars"]]
        if len(owners) > 1:
            print(f"\nCHARACTER FAIL: '{c}' exists in several projects of this universe ({', '.join(owners)}); ambiguous."); rc = 1; continue
        hr = res[home]
        if c not in hr["approved_chars"]:
            print(f"\nCHARACTER FAIL: {home}:{c} is registered but NOT approved by the owner. Offline prompts only, labelled 'character unverified'."); rc = 1; continue
        lock = projects[home].get("character_locks", {}).get(c, {})
        files = lock.get("canonical_sheets") or hr["approved_chars"][c]
        extra = lock.get("extra", "")
        where = "" if home == want else f"  (resolved via universe '{uni}' from {home})"
        print(f"\nCHARACTER PASS: {home}:{c}{where}")
        print("  LOCK: " + template.format(character=c, files="; ".join(files), extra=extra).strip())
        for f in files: print(f"  REF : references/character-library/{f}")
        for f in lock.get("excluded_variants", []): print(f"  DO NOT use as primary reference (non-canonical variant): references/character-library/{f}")
    sys.exit(rc)

if r["approved_chars"] and not (r["missing"] or r["bad_hash"]):
    print(f"\nGATE PASS: {want} has approved character(s): {', '.join(sorted(r['approved_chars']))}. "
          f"For each character you use, also run with --character <Name>.")
    sys.exit(0)
fail(f"GATE FAIL: {want} has no usable APPROVED character. Do not run paid generation; offline prompts only, labelled 'character unverified'.")
PY
