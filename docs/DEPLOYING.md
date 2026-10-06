# Deploying the web app

- **Canonical staging** (https://college-optimizer-staging.netlify.app) runs `origin/main` only. Redeploy it after a
  PR merges and main's CI is green.
- **Feature branches** go to https://prep-and-price-preview.netlify.app. Share the per-deploy permanent URL
  (`https://<deploy-id>--prep-and-price-preview.netlify.app`), not the site address, because other branches upload
  there too.

```
scripts/deploy/netlify_export.sh staging origin/main <dir>        # refuses anything that isn't origin/main
scripts/deploy/netlify_export.sh preview origin/<branch> <dir>    # refuses commits that aren't pushed
# Netlify deploy-site for the matching site id, then run the returned upload command from <dir>
scripts/deploy/verify_deploy.sh <site url> <commit that must be included>
```

Every export writes `/build.json` with the commit, ref, target and build time. Don't call a feature "live" until
`verify_deploy.sh` says the site contains its commit.

The preview site runs in demo mode: it has no Supabase variables, and Supabase Auth doesn't allow preview URLs as
callbacks. Test sign-up, invitations and billing on canonical staging after merge.
