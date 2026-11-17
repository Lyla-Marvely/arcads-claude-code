#!/usr/bin/env bash
# Character + brand-asset library check. Read-only; reads library.json and the disk. Generates nothing.
#
#   ./scripts/check-character-library.sh                          # summary of all projects
#   ./scripts/check-character-library.sh Rico-and-Friends         # character gate: exit 0 only if >=1 APPROVED master sheet whose file exists
#   ./scripts/check-character-library.sh Arsein-Research --brand  # brand gate: exit 0 only if >=1 APPROVED logo_primary whose file exists
#
# Character assets ('assets') and brand assets ('brand_assets') are tracked separately.
# Override the library location (tests): CHARACTER_LIBRARY_DIR=/path
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LIB="${CHARACTER_LIBRARY_DIR:-$ROOT/references/character-library}"
exec python3 -I - "$LIB" "${1:-}" "${2:-}" <<'PY'
import hashlib, json, sys
from pathlib import Path

lib, want, flag = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
reg_path = lib / "library.json"
if not reg_path.is_file():
    print(f"FAIL: {reg_path} not found"); sys.exit(1)
reg = json.loads(reg_path.read_text(encoding="utf-8"))
projects = reg["projects"]
types = set(reg.get("brand_asset_types", {}))
IMG = {".jpg", ".jpeg", ".webp", ".png", ".svg", ".pdf"}
SKIP = {"readme.md"}

def check_list(items, kind):
    out = {"n": 0, "approved": 0, "missing": [], "bad_hash": [], "bad_type": [], "files": set()}
    for a in items:
        out["n"] += 1
        f = lib / a["file"]; out["files"].add(f.resolve())
        if kind == "brand" and a.get("type") not in types:
            out["bad_type"].append(f"{a['file']} (type={a.get('type')!r})")
        if not f.is_file():
            out["missing"].append(a["file"]); continue
        if a.get("sha256") and hashlib.sha256(f.read_bytes()).hexdigest() != a["sha256"]:
            out["bad_hash"].append(a["file"])
        if a.get("status") == "approved":
            out["approved"] += 1
    return out

def inspect(p):
    ch = check_list(p.get("assets", []), "char")
    br = check_list(p.get("brand_assets", []), "brand")
    known = ch["files"] | br["files"]
    folder = lib / p["folder"]
    unreg = []
    if folder.is_dir():
        for f in folder.rglob("*"):
            if f.is_file() and f.suffix.lower() in IMG and f.resolve() not in known:
                unreg.append(str(f.relative_to(lib)))
    else:
        ch["missing"].append(f"(folder {p['folder']} missing)")
    # approved logo_primary count
    prim = sum(1 for a in p.get("brand_assets", []) if a.get("type") == "logo_primary" and a.get("status") == "approved"
               and (lib / a["file"]).is_file())
    return ch, br, unreg, prim

if want and want not in projects:
    print(f"FAIL: unknown project '{want}'. Known: {', '.join(projects)}"); sys.exit(1)
if flag not in ("", "--brand"):
    print(f"FAIL: unknown option '{flag}' (only --brand)"); sys.exit(1)

names = [want] if want else list(projects)
res = {n: inspect(projects[n]) for n in names}
print(f"{'project':22} {'chars':>5} {'ok':>3} {'plan':>4} | {'brand':>5} {'ok':>3} | notes")
for n, (ch, br, unreg, prim) in res.items():
    p = projects[n]
    notes = []
    for label, o in (("char", ch), ("brand", br)):
        if o["missing"]: notes.append(f"{label} MISSING FILES: {len(o['missing'])}")
        if o["bad_hash"]: notes.append(f"{label} HASH MISMATCH: {len(o['bad_hash'])}")
    if br["bad_type"]: notes.append(f"BAD BRAND TYPE: {len(br['bad_type'])}")
    if unreg: notes.append(f"UNREGISTERED FILES: {len(unreg)}")
    if ch["n"] == 0 and br["n"] == 0 and not unreg: notes.append("empty (nothing uploaded)")
    plan = len(p.get("planned_sheets", []))
    print(f"{n:22} {ch['n']:>5} {ch['approved']:>3} {plan:>4} | {br['n']:>5} {br['approved']:>3} | {'; '.join(notes)}")
    for label, o in (("char", ch), ("brand", br)):
        for k in ("missing", "bad_hash", "bad_type"):
            for f in o[k]: print(f"    {label} {k}: {f}")
    for f in unreg: print(f"    unregistered: {f}")

if want:
    ch, br, unreg, prim = res[want]
    if flag == "--brand":
        ok = prim >= 1 and not br["missing"] and not br["bad_hash"] and not br["bad_type"]
        if ok:
            print(f"\nBRAND GATE PASS: {want} has {prim} approved primary logo(s)."); sys.exit(0)
        print(f"\nBRAND GATE FAIL: {want} has no usable APPROVED primary logo. Do not place any logo; "
              f"never redraw or invent one."); sys.exit(1)
    ok = ch["approved"] >= 1 and not ch["missing"] and not ch["bad_hash"]
    if ok:
        print(f"\nGATE PASS: {want} has {ch['approved']} approved master sheet(s)."); sys.exit(0)
    print(f"\nGATE FAIL: {want} has no usable APPROVED master sheet. Do not run paid generation; "
          f"offline prompts only, labelled 'character unverified'."); sys.exit(1)
PY
