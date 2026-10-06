#!/usr/bin/env bash
# Prepare an upload for a Netlify deploy, stamped with the exact commit it contains.
#
#   scripts/deploy/netlify_export.sh staging origin/main <outdir>     # canonical staging: origin/main only
#   scripts/deploy/netlify_export.sh preview origin/<branch> <outdir> # anything else: prep-and-price-preview
#
# The upload gets web/public/build.json ({commit, ref, target, built_at}), served at /build.json, so a deploy can
# be checked with verify_deploy.sh before anyone calls a feature "live".
set -euo pipefail
target=${1:?staging|preview}; ref=${2:?git ref}; out=${3:?output dir}
cd "$(git rev-parse --show-toplevel)"
git fetch -q origin main
sha=$(git rev-parse --verify "$ref^{commit}")
case "$target" in
  staging)
    main=$(git rev-parse origin/main)
    if [ "$sha" != "$main" ]; then
      echo "Refusing: canonical staging deploys origin/main only ($main); $ref is $sha. Use 'preview' for branches." >&2
      exit 1
    fi ;;
  preview)
    if ! git branch -r --contains "$sha" | grep -q .; then
      echo "Refusing: $ref ($sha) is not on any pushed branch; push it first so the preview is reproducible." >&2
      exit 1
    fi ;;
  *) echo "target must be staging or preview" >&2; exit 2 ;;
esac
rm -rf "$out" && mkdir -p "$out"
paths="web netlify.toml"
[ -n "$(git ls-tree -d --name-only "$sha" supabase/functions)" ] && paths="$paths supabase/functions"
git archive "$sha" $paths | tar -x -C "$out"
mkdir -p "$out/web/public"
printf '{"commit":"%s","ref":"%s","target":"%s","built_at":"%s"}\n' "$sha" "$ref" "$target" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$out/web/public/build.json"
echo "$target upload for $ref at $sha ready in $out"
