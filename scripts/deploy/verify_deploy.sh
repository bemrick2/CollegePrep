#!/usr/bin/env bash
# Confirm what a Netlify URL is serving, and optionally that it contains a given commit (a feature's merge).
#
#   scripts/deploy/verify_deploy.sh https://college-optimizer-staging.netlify.app [<commit-that-must-be-included>]
set -euo pipefail
url=${1:?site url}; need=${2:-}
cd "$(git rev-parse --show-toplevel)"
json=$(curl -fsS "${url%/}/build.json?ts=$(date +%s)") || { echo "No /build.json at $url: deployed without the stamped export" >&2; exit 1; }
commit=$(printf '%s' "$json" | python3 -c 'import json,sys; print(json.load(sys.stdin)["commit"])')
echo "$url serves $commit ($(printf '%s' "$json" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["ref"], d["target"], d["built_at"])'))"
if [ -n "$need" ]; then
  git fetch -q origin
  if git merge-base --is-ancestor "$need" "$commit" 2>/dev/null; then echo "contains $need"; else echo "DOES NOT contain $need" >&2; exit 1; fi
fi
