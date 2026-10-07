# CollegePrep temporary live-database hold

Owner authorization October 6, 2026: Apparent is the priority. Pause only
CollegePrep butlklkzafvklwasbynr to free the second active Free slot; preserve
all project data/configuration. Never delete it, reset credentials or substitute
another database. Research/crawling/development/GitHub commits continue.

## Suspended writers

- live-import.yml: repository reference imports and reconciliation/idempotence.
- deploy-migrations.yml: pending live DDL and migration-history writes.
- deploy-functions.yml: Supabase Edge Function deployment.
- scripts/live_import.sh and apply_migrations.py: refuse manual live writes
  before reading connection configuration while .operations/supabase-live-hold.json
  has hold=true. Migration dry-run and offline SQL generation remain available.
- Runtime Auth, practice/account/billing/invitation database writes become
  unavailable while the project is paused. Existing function definitions and
  configuration are retained. External webhook retries may need reconciliation
  on resume; do not create new checkout/invitation acceptance tests while paused.

Research pipeline/program research workflows, data validation and ephemeral
PostgreSQL tests, web typecheck/unit/build, PRs and commits remain enabled.
Web builds/deploys do not import/migrate the live database. No Netlify project
is deleted and no provider callback or payment setting is changed.
All other agents/manual SQL clients must honor this hold: reviewed records and
pending migrations belong in GitHub; do not apply via MCP/psql during the hold.
This repository guard cannot revoke a separately running external agent's access.

## Preservation and pre-pause evidence

Audited main c87cca08bff0007bbcea71a0d4b9f2fcb0a6693f has 1,946 data/research
files; pending program PR107 head c642b33854795e82e32d27c4060a6e17e66e6eee is
persisted in GitHub. Other open research/code PRs remain preserved. No uncommitted
external agent workspace can be attested by this session.
Live exact reference ledger count: 25,651; revision count: 6,036. These are
preserved in the database, not reconstructed from the current reviewed snapshot.
Live schema includes 21 migrations through 20261006120000; source has that file.
The committed history manifest presently lists 20: reconcile its verified
metadata on resume rather than reapplying invitation DDL.
Existing Auth/account/billing state is present and must be preserved; Storage
object count was zero. Five deployed Edge Functions: billing-plans,
billing-checkout, billing-portal, stripe-webhook, send-household-invitation.
No pg_cron or pg_net extension appeared in the installed extension inventory.
At audit, the only in-progress Actions run was nonlive data validation for PR107;
no live writer was in progress. Recheck running/queued writers before pausing.

Supabase's supported pause keeps data/configuration and allows resume for up to
one year. This is a reversible managed pause, not deletion or a tested independent
logical backup. No real resume test is claimed before the slot is released.
Official basis: https://supabase.com/docs/guides/platform/free-project-pausing

## Resume order

1. Finish Apparent recovery, preserve safe results, dispose of its explicitly
   disposable target and verify the Free slot is available again.
2. Resume ONLY butlklkzafvklwasbynr; wait for ACTIVE_HEALTHY. Never recreate it.
3. Verify the original accounts, ledger/revisions, schema/migration history,
   functions/config and provider retry state before allowing new live work.
4. Re-read the ACTUAL live migration history first (owner instruction
   2026-10-06 18:52 CT): list supabase_migrations.schema_migrations (version,
   name, statements) and the objects each pending migration would create.
   Compare that with supabase/migration_history.json and supabase/migrations/.
   The pre-pause evidence (this file, the manifest, a pre-pause query) only makes
   it likely that #56's five migrations 20261006180000-20261006180400
   (cost_projection, primary_school, award_test_criteria, exam_keys_and_plan,
   student_academic_interests) and later ones are unapplied. Do not deploy them,
   and do not edit migration_history.json, on that evidence alone. Apply a
   version only when the live history lacks it AND its objects are absent;
   reconcile the invitation entry (20261006120000) from the recorded live row,
   never by reapplying its DDL. Then import latest reviewed GitHub data and run
   reconciliation/idempotence.
5. In a reviewed commit set hold=false, remove false job gates from migration
   and function workflows, and restore live-import's original workflow_run
   success condition. Explicitly dispatch migrations/functions/import in order;
   do not assume deferred pushes replay automatically.
6. Validate staging Auth, invitations and sandbox billing. Research stays enabled
   throughout. Document observed resume outcomes; no credential reset required.

Status at creation: writer holds committed before pause; actual project pause
and new Apparent resource creation must be recorded separately after verification.
