# Prep & Price: what works, what is demo-only, what is missing

Updated 2026-10-07. The hosted Supabase project is paused, so nothing below was checked against it after the pause.
"Local backend" means `scripts/local/live_stack.sh test`: plain PostgreSQL 16 with every repository migration,
the app's original demo question bank, PostgREST, and locally signed JWTs. It runs the real SQL, RLS policies and
RPCs. It does not run Supabase Auth, edge functions, email or Stripe.

## Setup (four screens)

The screens are About you, Test and goal, Starting point and Weekly plan. Each question is asked once:
- **Account name:** never asked again.
- **Invited student:** sees only what the guardian didn't supply and that the student may save, usually just the starting point. A household plan and its goals stay guardian-only.
- **Unknown answers:** "Not sure yet" (test or date), no goal score, and "Not yet" or "Don't remember the score" are all complete answers. Scores are never estimated.
- **Weekly plan:** the family sees the proposed first week before accepting. The result screen shows the next assignment and the weekly commitment.
- **Interrupted setup:** resumes in the same browser.
- **Deferred:** majors, cost goals and AP/CLEP details.
- **Language:** English only, so no language picker appears.
- **Not stored in the database yet (CR-26):** exam intent, planned test date, study days, high school and practice-test scores.


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
| Week turnover: "Last week" recap (Mon-Wed; parents get the day strip, students a one-line summary), and a prompt when the new week has no goal ("Use 40 again this week" for whoever may set goals; otherwise who sets it) | yes | yes | recap engine unit-tested; goal set through the same `setWeeklyGoal` path the local backend tests cover |
| Inactivity alert **by email** | choice kept, no email sent | sender built (`send-weekly-digest`, mode `inactivity`), not deployed | yes, end to end with the reference CR-22 SQL and a fake mail endpoint: once per stretch, retried after a failed send. Needs CR-22 applied, deployment and a scheduler. |
| Weekly summary email to parents (Mondays) | opt-in and preview (no email sent) | opt-in behind `VITE_WEEKLY_DIGEST`; sender built, not deployed | yes, same test: dashboard numbers, opted-out guardians excluded, sent once per week, scheduler secret required. Preview uses the same composer as the email. Needs CR-22 applied, deployment and a scheduler. |

**Question content.** 58 original items. Each was reviewed by two independent blind solves plus a key and explanation audit; 3 were fixed and re-reviewed, and one disagreement (a reviewer's arithmetic slip) was worked by hand. Only items whose current content hash was approved are served, in the demo and in the local database. The review is AI review, not human editorial review. The server-side gate (CR-21, migration `20261007140000`, #142) serves only items whose server-computed sha256 matches a recorded approval. The local database seed records approvals through `approve_practice_question`, and is checked end to end. Not applied on hosted.

**Fresh, repeat and progress-check questions.**
- **Practice:** never uses the next check's fresh questions, and labels repeats "Seen before". The session summary says how many questions were new and how many were seen before.
- **Progress checks:** use fresh questions first. A section with repeats is reported as "not a clean comparison", with no verdict.
- **Trends:** "Am I improving?" and the weekly trend use first answers only.
- **Running out:** the student home and the parent dashboard say plainly when no new practice questions are left, and the weekly goal is unchanged.
- **Server:** the session-builder side is CR-23.

## In-app updates vs emails actually sent

| Update | Shown in the app | Emailed today |
| --- | --- | --- |
| Weekly pace, days practised, focus, next check, last week's recap | Parent dashboard and student home | No |
| "Hasn't practised in N days" notice | Parent dashboard, when the parent's alert threshold is reached | No. The sender is built and tested locally, but not deployed (CR-22). |
| Monday weekly summary | Preview on the parent dashboard (behind `VITE_WEEKLY_DIGEST` in live) | No. Same as above. |

The parent dashboard's "Emails sent to you" list comes only from the server's delivery record (`parent_email_deliveries`, CR-22):
- **Demo:** "None. The demo never sends email."
- **Live before CR-22:** "None. Email delivery isn't switched on yet."
- **Inactivity notice:** says "Shown here on the dashboard. Not emailed." unless a recorded delivery exists.

## Content and launch blockers

- **Question volume [blocks the weekly cycle].** 58 reviewed items: ACT 38 (English 10, Math 12, Reading 8, Science 8) and SAT 20. The default weekly goal is 40 questions, so an ACT student who meets one week's goal has seen nearly the whole bank. From week two, sessions serve repeats (least recently seen first). Repeats inflate practice accuracy, and progress checks draw from the same pool.
- **Review depth.** Content review is AI review (two blind solves plus an audit), not human editorial review.
- **No score estimates.** By design, until a scoring model is validated (CR-3).
- **Legal pages.** No privacy policy or terms of service in the app. Students are typically minors, and the app stores practice history and parent contact details.
- **Hosted restore.** These migrations are unapplied: `20261007120000` (cost_projection v2) and `20261007140000` (question review gate). CR-22 is not yet a migration. Reconcile the live migration history first (SUPABASE_PAUSE.md).
- **Email (owner steps).** Verify the Resend domain (`mail.getcimiento.com` DNS) and set `RESEND_API_KEY`. Then deploy `send-weekly-digest` with `DIGEST_CRON_SECRET`, add the weekly and daily schedules, and set `VITE_WEEKLY_DIGEST=true`.
- **Real-account checks (owner).** Sign-up with email confirmation, and the two-browser invitation acceptance on staging.
- **Research data.** CR-10 (exam catalog empty), CR-15 (home state), CR-17 to CR-20 (tuition billing, loans, credit applicability, cost period).

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
