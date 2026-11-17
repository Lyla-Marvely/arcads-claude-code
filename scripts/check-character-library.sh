#!/usr/bin/env bash
# Character Reference Library gate. Read-only; reads library.json and the disk. Generates nothing.
#
#   ./scripts/check-character-library.sh                   # summary of all projects
#   ./scripts/check-character-library.sh Rico-and-Friends  # gate: exit 0 only if >=1 APPROVED asset whose file exists
#
# Override the library location (tests): CHARACTER_LIBRARY_DIR=/path
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LIB="${CHARACTER_LIBRARY_DIR:-$ROOT/references/character-library}"
exec python3 -I - "$LIB" "${1:-}" <<'PY'
import hashlib, json, sys
from pathlib import Path

lib, want = Path(sys.argv[1]), sys.argv[2]
reg_path = lib / "library.json"
if not reg_path.is_file():
    print(f"FAIL: {reg_path} not found"); sys.exit(1)
reg = json.loads(reg_path.read_text(encoding="utf-8"))
projects = reg["projects"]
IMG = {".jpg", ".jpeg", ".webp", ".png"}
problems = []

def inspect(name, p):
    folder = lib / p["folder"]
    out = {"registered": 0, "approved": 0, "missing": [], "bad_hash": [], "unregistered": []}
    reg_files = set()
    for a in p.get("assets", []):
        out["registered"] += 1
        f = lib / a["file"]
        reg_files.add((lib / a["file"]).resolve())
        if not f.is_file():
            out["missing"].append(a["file"]); continue
        if a.get("sha256") and hashlib.sha256(f.read_bytes()).hexdigest() != a["sha256"]:
            out["bad_hash"].append(a["file"])
        if a.get("status") == "approved":
            out["approved"] += 1
    if folder.is_dir():
        for f in folder.rglob("*"):
            if f.is_file() and f.suffix.lower() in IMG and f.resolve() not in reg_files:
                out["unregistered"].append(str(f.relative_to(lib)))
    else:
        out["missing"].append(f"(folder {p['folder']} missing)")
    return out

if want and want not in projects:
    print(f"FAIL: unknown project '{want}'. Known: {', '.join(projects)}"); sys.exit(1)

names = [want] if want else list(projects)
res = {n: inspect(n, projects[n]) for n in names}
print(f"{'project':22} registered approved planned  notes")
for n, r in res.items():
    notes = []
    if r["missing"]: notes.append(f"MISSING FILES: {len(r['missing'])}")
    if r["bad_hash"]: notes.append(f"HASH MISMATCH: {len(r['bad_hash'])}")
    if r["unregistered"]: notes.append(f"UNREGISTERED IMAGES: {len(r['unregistered'])}")
    if r["registered"] == 0 and not r["unregistered"]: notes.append("empty (nothing uploaded)")
    planned = len(projects[n].get("planned_sheets", []))
    print(f"{n:22} {r['registered']:>10} {r['approved']:>8} {planned:>7}  {'; '.join(notes)}")
    for k in ("missing", "bad_hash", "unregistered"):
        for f in r[k]: print(f"    {k}: {f}")

if want:
    r = res[want]
    ok = r["approved"] >= 1 and not r["missing"] and not r["bad_hash"]
    if ok:
        print(f"\nGATE PASS: {want} has {r['approved']} approved master sheet(s).")
        sys.exit(0)
    print(f"\nGATE FAIL: {want} has no usable APPROVED master sheet. Do not run paid generation; "
          f"offline prompts only, labelled 'character unverified'.")
    sys.exit(1)
PY
