#!/usr/bin/env bash
# Preflight for the pixar-animation-video workflow. Run BEFORE any image/video generation.
# Read-only: makes at most ONE authenticated GET (/v1/products) and generates nothing.
#
#   ./check-requirements.sh            # local tools + env + auth check
#   ./check-requirements.sh --offline  # local tools + env only (no network)
#
# Exit code: 0 = ready for generation, 1 = a blocking requirement is missing.
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || (cd "$(dirname "$0")/../../.." && pwd))"
OFFLINE=0; [[ "${1:-}" == "--offline" ]] && OFFLINE=1
BLOCK=0
ok()   { printf '  [ OK ] %s\n' "$1"; }
warn() { printf '  [WARN] %s\n' "$1"; }
fail() { printf '  [FAIL] %s\n' "$1"; BLOCK=1; }

if [[ -f "$ROOT/.env" ]]; then set -a; source "$ROOT/.env"; set +a; fi
BASE="${ARCADS_BASE_URL:-https://external-api.arcads.ai}"

echo "1) Local tools"
for t in python3 curl jq; do command -v "$t" >/dev/null && ok "$t" || fail "$t missing (required for generation scripts)"; done
for t in ffmpeg ffprobe; do command -v "$t" >/dev/null && ok "$t" || warn "$t missing — needed only to stitch/trim clips (not for generation)"; done
command -v npx >/dev/null && ok "npx (HyperFrames captions possible)" || warn "npx missing — only needed for the optional caption step"

echo "2) Credentials (.env)"
AUTH_HEADER=""
if [[ -f "$ROOT/.env" ]]; then ok ".env found"; else fail ".env missing — run ./scripts/setup.sh"; fi
if [[ -n "${ARCADS_BASIC_AUTH:-}" && "$ARCADS_BASIC_AUTH" != *"your_base64_encoded_credentials_here"* ]]; then
  AUTH_HEADER="Authorization: $ARCADS_BASIC_AUTH"; ok "ARCADS_BASIC_AUTH set (value not printed)"
elif [[ -n "${ARCADS_API_KEY:-}" && "$ARCADS_API_KEY" != "your_key_here" ]]; then
  AUTH_HEADER="Authorization: Basic $(printf '%s:' "$ARCADS_API_KEY" | base64)"; ok "ARCADS_API_KEY set (value not printed)"
else
  fail "no Arcads credential (ARCADS_BASIC_AUTH or ARCADS_API_KEY)"
fi
[[ -n "${PRODUCT_ID:-}" ]] && ok "PRODUCT_ID set" || warn "PRODUCT_ID not set — /v2/videos/generate requires productId; fetch one from GET /v1/products and save it to .env"
[[ -n "${PROJECT_ID:-}" ]] && ok "PROJECT_ID set" || warn "PROJECT_ID not set — optional, groups assets in one Arcads folder"

echo "3) Arcads API reachability + auth"
if [[ $OFFLINE -eq 1 ]]; then
  warn "skipped (--offline) — auth NOT verified"
elif [[ -z "$AUTH_HEADER" ]]; then
  warn "skipped — no credential to test"
else
  code="$(curl -sS -o /dev/null -w '%{http_code}' -H "$AUTH_HEADER" "$BASE/v1/products" 2>/dev/null || echo 000)"
  if [[ "$code" == "200" ]]; then ok "GET /v1/products -> 200 (auth works)"; else fail "GET /v1/products -> HTTP $code (auth/network problem)"; fi
fi

cat <<'TXT'

4) What this check CAN and CANNOT confirm
  Confirmed by this script : local tools, credential presence, auth (when online).
  NOT confirmed by it      : that a given model is enabled on your Arcads plan, your credit balance
                             (Arcads has no billing endpoint), or Gemini Omni Flash availability.
  Documented in this repo (skills/arcads-external-api/reference.md):
    - Images : POST /v2/images/generate  (gpt-image-2 max 5 refs; nano-banana-2 max 14; ratios 1:1, 16:9, 9:16)
    - Video  : POST /v2/videos/generate  model "seedance-2.0" (ratios 9:16 and 16:9 only; duration 4-15s;
               480p/720p; referenceImages max 3; NO startFrame on Seedance)
    - Poll   : GET /v1/assets/{id} for images AND seedance-2.0 (NOT /v1/videos/{id})
    - Upload : POST /v1/file-upload/get-presigned-url -> PUT -> filePath (ONE-TIME USE; re-upload per call)
  Gemini Omni Flash: the repo guide names an Arcads MCP tool `arcads_generate_video_omni_flash`, but it is
    NOT in reference.md's model enum. Treat it as unavailable unless that tool is actually present in the
    session's tool list. Default to Seedance 2.0.
TXT

echo
if [[ $BLOCK -eq 0 ]]; then echo "RESULT: ready for generation (after the user confirms the credit estimate)."; else echo "RESULT: BLOCKED — fix the [FAIL] items above. Prompt/script/storyboard work is still possible offline."; fi
exit $BLOCK
