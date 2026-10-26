# Deploying the web app

- **Canonical staging** (https://college-optimizer-staging.netlify.app) runs `origin/main` only. Redeploy it after a
  PR merges and main's CI is green.
  - **Gate (CR-23):** once #248 merges, main's client selects `practice_questions.pool`. Don't redeploy staging from main until
    migration `20261022050000_assessment_pool` is applied to staging's Supabase project; otherwise every practice read
    fails (42703). Hosted migrations are held (`.operations/supabase-live-hold.json`), so staging stays on its current
    deploy until the owner lifts the hold and applies it (`docs/SUPABASE_PAUSE.md` step 4).
  - **CR-23 reserve release (#263, #218).** Hosted migrations stay held until the owner lifts the hold
    (`.operations/supabase-live-hold.json` `hold: true`). Nothing below runs before that, and no step lifts it. Only
    items that the content lead has individually approved by a named human review (`review_method` matching
    `human: <reviewer>`) can become eligible for checks. Generated, `fixture:` or automatically checked items never
    qualify, and neither does an item any student has seen or one whose passage another question uses.
    - **The reserve is a script, not a migration.** It lives outside `supabase/migrations/` (for example
      `supabase/reserve/`). CI applies every migration to an empty database, where a reserve would always fail, and a
      merged migration could be applied without its pair. `scripts/apply_migrations.py --reserve <file>` runs it.
    - **Nothing applies early on push.** `deploy-migrations.yml` also runs on pushes to `supabase/migrations/**`. Today
      the job is disabled (`if: ${{ false }}`, the hold). Even when enabled, the applier refuses the assessment-pool
      migration `20261022050000` unless `--reserve` is given, and it refuses the whole run, applying nothing, so a
      push-triggered run applies no migration while the pool is pending. When the owner lifts the hold, they re-enable
      the job and run the steps below by `workflow_dispatch` only. Before that, they confirm with `--dry-run` that a
      plain run is refused.
    1. Apply the earlier migrations and stop before the pool: `python scripts/apply_migrations.py --until 20261022040000`
       (in the workflow: dispatch *Deploy Supabase migrations* with `until = 20261022040000`). Run it with `--dry-run`
       first; it lists what would apply and what stays pending. An unknown version is refused before anything runs.
    2. The content lead approves reserve candidates individually (`approve_practice_question(id, 'human: <reviewer>')`,
       per `docs/product/QUESTION_IMPORT_CONTRACT.md`). Each item needs its own recorded human review; there is no
       bulk eligibility.
    3. Generate the reserve script from the approved ids, review it, and commit it under `supabase/reserve/`:
       `python scripts/make_reserve_migration.py --exam-version <version_key> --items <file of "uuid section" lines> --out supabase/reserve/<date>_<exam>.sql`.
       The generator refuses an empty list and any path under `supabase/migrations/`. Commit only a script built from
       real approved items, never one from fixtures.
    4. In one dispatch, with `until = 20261023010000` and `reserve = supabase/reserve/<file>.sql`, the applier runs
       `20261022050000_assessment_pool`, `20261023010000_benchmark_item_assignment` and the reserve script in **one
       transaction**. It commits only if every listed item qualifies: it exists in that exam version and in a planned
       section, is published, passes the rights gate, has a current approved review naming a human reviewer, has never
       been attempted, planned into a practice session or assigned to a check, and has a passage no other question uses.
       Otherwise everything rolls back: no migration is recorded and nothing is marked. Fix the list, regenerate the
       script and dispatch again. Run it with `--dry-run` first. Don't deploy the client until it has applied and the
       hosted acceptance steps (`docs/product/LAUNCH_CHECKLIST.md` §H) pass.
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
