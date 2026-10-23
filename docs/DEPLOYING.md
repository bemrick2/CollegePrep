# Deploying the web app

- **Canonical staging** (https://college-optimizer-staging.netlify.app) runs `origin/main` only. Redeploy it after a
  PR merges and main's CI is green.
  - **Gate (CR-23):** once #248 merges, main's client selects `practice_questions.pool`. Don't redeploy staging from main until
    migration `20261022050000_assessment_pool` is applied to staging's Supabase project; otherwise every practice read
    fails (42703). Hosted migrations are held (`.operations/supabase-live-hold.json`), so staging stays on its current
    deploy until the owner lifts the hold and applies it (`docs/SUPABASE_PAUSE.md` step 4).
  - **CR-23 reserve release (#263, #218).** Hosted migrations stay held until the owner lifts the hold
    (`.operations/supabase-live-hold.json` `hold: true`); nothing below runs before that, and no step lifts it. Only
    items that the content lead has individually approved by a human review (`review_method` starting `human:`) can
    become eligible for checks. Generated, `fixture:` or automatically checked items never qualify, and neither does
    an item any student has seen. Order:
    1. Apply the earlier migrations and stop before the pool: `python scripts/apply_migrations.py --until 20261022040000`
       (in the workflow: dispatch *Deploy Supabase migrations* with `until = 20261022040000`). Run it with `--dry-run`
       first; it lists what would apply and what stays pending. An unknown version is refused before anything runs.
    2. The content lead approves reserve candidates individually (`approve_practice_question(id, 'human: <reviewer>')`,
       per `docs/product/QUESTION_IMPORT_CONTRACT.md`). Approve whole batches only by recording each item's own human
       review; there is no bulk eligibility.
    3. Generate the reserve migration from the approved ids and review it like any migration:
       `python scripts/make_reserve_migration.py --exam-version <version_key> --items <file of "uuid section" lines> --version <next version>`.
       It refuses an empty list. At apply time it raises and marks nothing unless every id exists in that exam version
       and section, is published and passes the rights gate, has a current approved review with a `human:` method, and
       has never been attempted, planned into a practice session or assigned to a check. Commit only a reserve migration
       built from real approved items, never from fixtures.
    4. In one dispatch (no `until`), apply `20261022050000_assessment_pool`, `20261023010000_benchmark_item_assignment`
       and the reserve migration. Each runs in its own transaction. If the reserve migration fails, the two schema
       migrations stay applied, checks read "not measured", and nothing is marked. Fix the list, regenerate the
       reserve migration and dispatch again. Don't deploy the client until it has applied and the hosted acceptance steps
       (`docs/product/LAUNCH_CHECKLIST.md` §H) pass.
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
