# Prep & Price: what works, what is demo-only, what is missing

Updated 2026-10-07. The hosted Supabase project is paused, so nothing below was checked against it after the pause.
"Local backend" means `scripts/local/live_stack.sh test`: plain PostgreSQL 16 with every repository migration,
the app's original demo question bank, PostgREST, and locally signed JWTs. It runs the real SQL, RLS policies and
RPCs. It does not run Supabase Auth, edge functions, email or Stripe.

## The student journey

| Step | Demo | Live code | Checked against the local backend |
| --- | --- | --- | --- |
| Parent creates household, adds student, sets plan and weekly goal | yes | yes | yes |
| Student joins with the 10-character code (wrong and reused codes refused, outsider sees nothing) | yes | yes | yes |
| Baseline (starting benchmark), scored by the server from stored attempts | yes | yes | yes |
| Weekly plan: Mon-Sun strip, pace, focus skills, when the next progress check is due | yes | yes | yes (benchmark answers excluded from the week) |
| Short practice sessions with explanations after each answer | yes | yes | yes |
| Progress checks (mini/full benchmark due on schedule; Home links straight to the due one) | yes | yes | Results compare with the baseline and the last check, section by section. A change counts as clear only beyond two standard errors; otherwise "within normal variation". Percent right is labelled as practice and never converted to an ACT/SAT score (`PRACTICE_ESTIMATES_VALIDATED = false`). |
| Parent weekly update: pace, days practised, focus, next check | yes | yes | yes |
| Next-week goal suggestion (server rule, set in one tap by a guardian with goal permission) | yes | yes | yes (one-week history correctly gives no suggestion; a student cannot change the goal) |
| Inactivity alert preference, and in-app "hasn't practised" notice | yes | yes | yes |
| Inactivity alert **by email** | no | no | missing: no sender or schedule exists |
| Weekly digest email to parents | no | no | missing |

**Question content.** 58 original items. Each was reviewed by two independent blind solves plus a key and explanation audit; 3 were fixed and re-reviewed, and one disagreement (a reviewer's arithmetic slip) was worked by hand. Only items whose current content hash was approved are served, in the demo and in the local database. The review is AI review, not human editorial review. Live has no review fields yet (CR-21).

## Colleges and cost

| Feature | Demo | Live | Notes |
| --- | --- | --- | --- |
| Search, verified-school list, aligned Compare table | sample data | yes | Live reads only verified research records; untested locally (no research data in the disposable database) |
| Saved schools and primary target school (CR-12) | yes | yes, as of this change | checked locally with two fictional schools |
| Major interests (CR-13) | browser | yes, as of this change | checked locally, including server rejection of malformed keys |
| AP/CLEP exam plan (CR-10) | browser only | **not wired** | the app keys exams by normalized published names; the backend keys them by `exam_catalog`, which is empty in the repository migrations. Needs the catalog populated (Research) and a name-to-key mapping before it can move. |
| Cost & savings view (CR-4 v2) | yes (same rules, `engine/costProjection.ts`) | yes, on `cost_projection` v2 | Full program priced first, with no credit assumed (academic-year budget × years, plus the family's own year-round living, minus their grants). Credit is shown in three steps: accepted by the school's table; applies to the selected major's verified plan (course by course, `engine/degreeCredit.ts`); removes a term only when a whole plan term is covered. Savings appear only as "potential, if the assumptions hold", net of grants lost for terms not attended. Dependencies: CR-17 to CR-20. **v2 migration is held from hosted pending database review and reconciliation with the live migration history.** |
| Home state for in-state pricing (CR-15) | browser only | no backend | contract request still open |

## Accounts, invitations, billing

| Feature | Status |
| --- | --- |
| Invitation codes and links (two credentials, 72 h, single use, rate-limited) | SQL checked by `supabase/tests/invitation_email.sql` and locally; hosted migration applied before the pause |
| Invitation email (`send-household-invitation`) | deployed before the pause; real sending blocked on Resend domain verification for `mail.getcimiento.com` and the `RESEND_API_KEY` secret (owner steps) |
| Email confirmation on sign-up | Supabase Auth only; never runs locally. Must be checked on hosted |
| Billing (Stripe Checkout/Portal) | edge functions; mocked in unit tests only |

## Needs hosted validation once the project is restored

1. Every migration added since the pause, applied in order. Check the live migration history first (`scripts/check_migration_history.py`).
2. Real Supabase Auth: sign-up with email confirmation, then the two-browser invitation acceptance.
3. Edge functions: invitation email through Resend, billing checkout and portal, AI help.
4. Research data: Compare, verified schools and (once wired) cost projection against real verified records.
5. RLS with real tokens. The local stack uses the same policies, but its `auth.uid()` is a stand-in.

Staging deploys stay on hold until then.
