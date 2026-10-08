# Work deferred until Supabase is reactivated

**Owner decision, 2026-10-08:** the CollegePrep Supabase project stays paused on purpose. Both free active-project slots
are used elsewhere, and the owner has no current plan to upgrade or reactivate it. Development continues through GitHub
and local testing. Nothing on this page starts until the owner decides to reactivate. Resume procedure:
`docs/SUPABASE_PAUSE.md`.

**Restore window:** Supabase's pausing guide says a paused free project can be restored from the dashboard for up to
one year after it was paused. This project was paused 2026-10-06, so that window runs until about **2027-10-06**.
The guide's own heading still says 90 days, so check the dashboard when deciding.
Source: https://supabase.com/docs/guides/platform/free-project-pausing

Nothing below needs paid services. Each row says what's ready in the repo, so resuming doesn't start from scratch.

## Launch-critical (M1)

| Item | Ready in the repo | Needs on resume |
|---|---|---|
| A5: reconcile migration history, then apply pending migrations | `20261007120000` cost v2, `20261007140000` question review, `20261006180300` CR-10 exam plan (all merged) | Research: read live history first (`SUPABASE_PAUSE.md` resume order) |
| A6: real-account tests (sign-up with confirmation, two-browser invitation, RLS with real tokens) | Test script and local stack (`scripts/local/live_stack.sh`, 24 local tests) | Owner runs real accounts |
| B1: CR-23 server-side check-item holdout | Contract on #37; live does it client-side | Research migration |
| B2: CR-22 parent emails | `scripts/local/proposals/cr22_parent_emails.sql`, `send-weekly-digest` function, local end-to-end test | Migration, function deploy, schedules, `VITE_WEEKLY_DIGEST`; plus A7 email domain |
| B4: CR-24 rights gate, CR-25 report a problem | Contracts on #37 | Migrations, then UI |
| CR-26 setup on the account | `scripts/local/proposals/cr26_account_setup.sql`, local tests, UI behind `VITE_ACCOUNT_SETUP` | Migration, flag |
| CR-27 practice reminders | `scripts/local/proposals/cr27_practice_reminders.sql`, edge functions, local fake-push tests | Migration, function deploy, scheduler, VAPID and FCM secrets, real-device checks R1–R7 |
| CR-16 billing entitlement against live Stripe (A8) | Migrations and functions merged (#108), mock-tested | Owner Stripe setup, real checkout, portal and cancel test |
| C1: verified institution records on hosted | Records in `data/` | Live import (Research) |
| D1, D2: production deploy and hosted validation | `APP_STATUS.md` checklist | Hold lifted |
| #18 RLS helper move and foreign-key indexes | n/a | Research migration |

## College planning (M4)

| Item | Ready in the repo | Needs on resume |
|---|---|---|
| P5, #196: CR-28 planning profile, CR-10 exam-plan wiring, CR-15 home state | Contract proposal; inputs work on the device in the demo | Reference SQL plus local tests (can be written now), migration, LiveSource wiring |
| P6: live pilot | Engine and view behind `VITE_PLANNING_PILOT`, tested in the demo | Import verified records; set the flag in a deployed environment (owner) |

## Not deferred (continues now)

These can all proceed without Supabase:
- Research data work in `data/`.
- Pipeline runs and validation.
- Ephemeral local PostgreSQL tests.
- Web typecheck, unit tests and builds.
- Engine and UI work in the demo.
- Reference SQL proposals.
- Content authoring and review tooling.
- Pull requests and CI.
