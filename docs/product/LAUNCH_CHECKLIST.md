# Launch checklist

Consolidated 2026-10-07; status updated 2026-10-21 (late evening). Owners:
- **Owner**: Brandon.
- **Research**: database and data workstream.
- **Design**: frontend and product workstream.
- **Content**: content lead, not yet named.
- **Counsel**: a lawyer, not yet engaged.

Status: ⛔ blocked · ⏳ not started · 🚧 in progress · ✅ done.

Hosted deployment is **held** (`.operations/supabase-live-hold.json`). Owner, 2026-10-08: the Supabase project stays paused on purpose (both free slots are used elsewhere), with no reactivation planned yet. Nothing below that touches hosted happens until the owner decides to reactivate it. Everything waiting on it is listed in `SUPABASE_DEFERRED.md`.

## Where each capability stands (2026-10-21)

Columns:
- **Implemented:** in the code on `main` or in an open PR, as noted.
- **Local:** checked by unit and component tests, or by `scripts/local/live_stack.sh test`. That runs every migration plus Design's reference SQL, with real SQL, RLS and RPCs: 57 end-to-end tests on main (58 with #269); each run fails if any test is skipped.
- **Hosted:** checked on the hosted project. **Nothing is hosted-tested since the 2026-10-06 pause.**
- **Blocked by:** what is still in the way.

Simulated tests (fake push service, fake FCM, fake mail) prove the code paths, not delivery.

| Capability | Implemented | Local | Hosted | Blocked by |
|---|---|---|---|---|
| Parent journey: four-screen setup, reload/resume, finished setup never asked again | yes | yes: demo mobile run (resumes at step 3); local backend (resume on another device; #217) | no | CR-26 migration (#218 A1); A5 |
| Invited student: single-use code, guardian's choices on every device, can't change plan or goal | yes | yes (#217) | no | Real two-browser invitation acceptance with email confirmation (A6); invitation email (A7) |
| Student who signs up alone (no household) | yes | yes (#217) | no | A5, A6 |
| Guardian permissions (default co-guardian; view-only guardian) | yes (server rules; the app offers exam-plan editing only to the student or a guardian with set-goals, #219) | yes: through the app (#217, #219) and **directly against the server, every role, tables and RPCs (#233, 14 tests)** | no | #218 C1, C6, C7 enforced on the server by `20261022010000_household_role_rules` (#243; unapplied on hosted) |
| Quick practice vs a separately scheduled benchmark; a started benchmark isn't a result | yes | yes (#217; component tests) | no | CR-26 for the schedule on the account |
| AP/CLEP exam plan on the account (CR-10) | yes, behind `VITE_EXAM_PLAN` (#219) | yes (#219) | no | `20261006180300` unapplied on hosted; #218 C1 rule in `20261022010000` |
| Practice reminders: settings, quiet/school hours, limits, snooze, one notification per reminder | yes, behind `VITE_PRACTICE_REMINDERS` | yes, against fakes | no | CR-27 migration (#218 A2); VAPID and FCM secrets; real devices R1–R7 |
| Guardian notice when a linked student turns reminders off | yes | yes, against fake mail; the dashboard shows "Emailed to you" only after a recorded send | no | CR-22 and CR-27 migrations; email domain (A7); R5 |
| Guardian sees the last **recorded** reminder send (not a test), and device permission separately from the in-app switch | yes (#220) | yes | no | as above |
| Parent weekly summary and inactivity emails | yes, behind `VITE_WEEKLY_DIGEST` | yes, against fake mail | no | CR-22 migration; A7; schedules |
| Only reviewed questions served | yes (CR-21 gate) | yes | no | `20261007140000` unapplied; review is AI only (A2) |
| Questions held for the next check never appear in practice | yes: demo; live via the server's reserved pool (CR-23: #248, migration and client; the #221 client rule is retired) | yes: local backend (`assessmentPool.local.test.ts`, `supabase/tests/assessment_pool.sql`) | no | B1: migration `20261022050000` applied on hosted, reserve marked |
| Repeats labeled and never counted as improvement | yes | yes | no | none |
| Honest when fresh questions run out; shortened or repeated checks labelled, no verdict on repeats | yes | yes (component and local tests) | no | A1, the bank size (`PRACTICE_READINESS.md`) |
| No ACT/SAT score prediction | yes (`PRACTICE_ESTIMATES_VALIDATED = false`) | yes | n/a | Validated model (CR-3) |
| Human editorial review | ledger, packets and import (#207) | yes | n/a | A named content lead (A2) |
| Credit coverage shown apart from time or money saved; savings withheld without completion records | yes (#253, open) | yes | n/a | Records for prerequisites, course availability, sequencing and remaining requirements (none on file) |
| College-planning pilot view (`/colleges/plan`) | yes, behind `VITE_PLANNING_PILOT`; a flag-off build contains no pilot code (#232) | yes: component tests on the stored UTC/UTK/MTSU records; mobile at 390 px | no | Pilot gate not met (`PLANNING_ENGINE.md`): UTC credit tables unverified, UTK/MTSU plans not on file |

## A. Hard blockers: no public launch without these

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| A1 | Question bank at or above the launch minimum (both exams at 8 weeks: ≈ 430 ACT / ≈ 410 SAT; or one exam at 12 weeks: ≈ 470 with 25% review, ≈ 600 all fresh) | Owner → Content | ⛔ | 58 items exist. Sizing for 20/40/60 a week over 12 weeks and a year, per exam, with reserved checks: `QUESTION_BANK_RECOMMENDATION.md`. The recommendation is about 470 unique items (25% review) or about 600 (all fresh) for one exam, 12 weeks at 40. Decisions are needed on scope, budget and AI drafting, and a content lead must be named (`CONTENT_PLAN.md` §6, #164, #19). |
| A2 | Human editorial review of every published item, including the existing 58 | Content | ⛔ | All 58 are reviewed by AI only. Human-approved: 0 of 58. The tooling is ready (#207: ledger, blind packets, sign-off import, rules enforced by tests). There is no named human approver. |
| A3 | Privacy policy and terms approved | Owner + Counsel | 🚧 | Drafts and 12 decisions are in #165 (`docs/legal/`). Minimum age (13+ recommended), retention, entity and contacts are needed. |
| A4 | Data deletion and export path | Research (procedure) + Design (UI) | ⛔ | No deletion or export function exists. Choose manual with a stated response time, or in-app (`DECISIONS.md` #6). |
| A5 | Hosted Supabase restored, and migration history reconciled before applying anything | Owner (restore) → Research (#122) | ⛔ | Paused. Unapplied on hosted (likely, to be confirmed against the live history in H0): `20261006180000`–`20261006180400` (#56), `20261007120000` cost v2, `20261007140000` question review (#142), and every migration since, including `20261022010000` role rules, `20261022040000` C3, including CR-24 (`20261022030000`) and CR-23 (`20261022050000`); CR-22 once it becomes a migration. Order: `docs/SUPABASE_PAUSE.md` step 4. |
| A6 | Real-account tests: sign-up with email confirmation, two-browser invitation acceptance, RLS with real tokens | Owner (runs the accounts) + Design (script) | ⛔ | Needs A5. The journeys and permissions pass against the local backend (#217). Sign-up, email confirmation and real tokens can't run locally: the local auth is a stub. |
| A7 | Email sending works | Owner | ⛔ | Verify the Resend domain (`mail.getcimiento.com` DNS) and set the `RESEND_API_KEY` secret. |
| A8 | Billing works with live Stripe | Owner | ⛔ | Owner setup in `STRIPE_BILLING.md`, then a real checkout, portal and cancel test. It has only been tested with mocks so far. |
| A9 | Privacy, Terms and age attestation in the app | Design | ⏳ | Waiting on A3 text. Links go in the footer, sign-up, invitation acceptance and email footers. |

## B. Needed for the core weekly loop to be honest in production

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| B1 | CR-23: server holds check items out of practice; `seen_before` and first-answer metrics | Research | ⏳ | Part 1 built and tested locally (#248: migration and the client that reads `pool`; #244 added the client-side reserve and insufficient-pool rules); unapplied on hosted (A5). Part 2 (`seen_before` on practice items, first-answer fields) open. **Hosted acceptance after applying:** (1) `supabase/tests/assessment_pool.sql` passes on a branch copy; (2) `select count(*) from practice_questions where pool = 'assessment' and status = 'published' and review_current` per exam version and section matches the chosen reserve, spread across difficulties; (3) with a real student token, `publishedQuestions` returns no reserved item before a check, `start_benchmark` without a version is refused, a check serves only reserved items and a second start before any answer resumes it; (4) a guardian sees `assessment_pool_status` counts and no unattempted reserved item; (5) only then deploy the client (`docs/DEPLOYING.md` gate). **Before a bank larger than one check goes live:** #263 (an open check exposes the whole reserve; reading without attempting isn’t counted as seen). |
| B2 | CR-22: parent email opt-in, digest and inactivity payloads, delivery log, as a real migration | Research | ⏳ | Reference SQL in `scripts/local/proposals/cr22_parent_emails.sql`. Then the Owner deploys `send-weekly-digest`, adds the schedules and sets `VITE_WEEKLY_DIGEST=true` (after A5 and A7). |
| B3 | "Full" progress check falls back to a mini until a held-out full-length form exists | Design | 🚧 #167 | Done in code (`FULL_FORM_READY = false`); switch on only when Content delivers a held-out full-length form per exam. |
| B4 | CR-24 rights gate and CR-25 "report a problem" | Research, then Design (UI) | 🚧 | CR-24 merged (#245, unapplied). CR-25 open. Imported questions follow `QUESTION_IMPORT_CONTRACT.md`; batches arrive on #254 (none yet). |
| B5 | Item statistics review, monthly | Content | ⏳ | Needs live traffic and CR-25. |

## C. Needed for the college-cost side to be complete (can launch labelled as partial)

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| C1 | Verified institution records loaded on hosted | Research | ⛔ | Needs A5. Imports are held. |
| C2 | CR-17 tuition billing basis, CR-18 loan terms, CR-19 credit applicability, CR-20 cost-of-attendance period; records for prerequisites, course offerings and sequencing | Research | ⏳ | Without them, no time or dollar saving is shown (#253): credit coverage only. |
| C3 | CR-10 exam catalog (AP/CLEP plan in live), CR-15 home state, CR-11 award test minimums | Research | ⏳ | The live exam plan is not wired until the catalog exists. |

## H. Hosted acceptance, step by step

Nothing here runs until the owner lifts the hold. **Record the evidence:** for every step, write the date, who ran it, the build or commit, and the evidence (a screenshot, or the SQL output) in `docs/acceptance/<date>.md`. Create the folder on first use.

**Rules for every step:**
- A step passes only when its "Pass" line holds exactly. Local fakes don't count.
- Secrets are read from shell variables (`$DIGEST_CRON_SECRET`, `$REMINDER_CRON_SECRET`, service-role keys). Never write a value into this file, an evidence file, a PR or an issue.
- Steps marked "(needs #N)" depend on a PR that must be merged first.

**H0. Before applying anything (Owner, Research).** `SUPABASE_PAUSE.md`, Resume order:
1. Steps 1–3: resume only the original project and verify accounts, ledger, history, functions and provider retry state.
2. Step 4: read the live `supabase_migrations.schema_migrations` (version, name, statements) and the objects each pending migration would create.
3. Before `20261022030000` (rights gate), list published questions. Each needs an allowed license, attribution where required, and an origin, or must be unpublished by a reviewed change.
4. Step 5, as a reviewed commit:
   - set `hold=false` in `.operations/supabase-live-hold.json`;
   - remove the false job gates in `deploy-migrations.yml` and `deploy-functions.yml`;
   - restore `live-import.yml`'s original `workflow_run` success condition.

**Pass:**
- The live history equals `supabase/migration_history.json` plus `20261006120000`. That version is applied live but missing from the manifest; reconcile it from the recorded live row, never by reapplying it.
- Every version you intend to apply is absent from live, and so are its objects.

**H1. Apply and verify the migrations (Research).**
1. **Disposable copy first, never production first.** Supabase branching needs a paid plan, and the project is on Free. So either restore a `pg_dump` of the live project into local PostgreSQL, or upgrade the plan for branching.
2. On the copy, apply every pending migration in filename order. Then run what the `database` job in `.github/workflows/validate-data.yml` runs, in the same order: every `supabase/tests/*.sql` file it lists, plus `scripts/test_program_import.py | psql`.
3. On production, explicitly dispatch `deploy-migrations.yml`. Don't assume deferred pushes replay.
   - `scripts/apply_migrations.py` applies **every** pending file in filename order, each in its own transaction. It has no option to stop early.
   - So don't dispatch it until the reserve migration from H2 step 2 exists. The applier then runs `20261022050000` and the reserve straight after it in the same run.
   - The workflow also runs on every push to main that touches `supabase/migrations/**`. Keep that push trigger off (or the job gate in place) until H2 is ready. Otherwise any other migration merged first, such as CR-27 or CR-22, would apply `20261022050000` without its reserve.
   - The other route is a reviewed `--until <version>` option on the applier (Research), used to stop at `20261022040000`.
   - Record the applier's printed `applied <file>` lines, and once at the end `select version from supabase_migrations.schema_migrations order by version desc limit 5`.
4. Then dispatch `deploy-functions.yml`, then `live-import.yml`. Run reconciliation and the idempotence pass (`SUPABASE_PAUSE.md` step 4).
5. Validate staging Auth, invitations and sandbox billing (`SUPABASE_PAUSE.md` step 6).

**Pass:**
- every suite passes on the copy;
- the production history lists each applied version exactly once;
- the import reconciliation shows no differences.

**H2. Paired release: the assessment pool (CR-23; Research + Design; `CONTRACT_REQUESTS.md` CR-23 paired release requirements 1–5).** Flags stay off.

This step is **blocked by A2.** The reserve must come from human-reviewed items, and 0 of 58 are reviewed. The 13-item reserve exists only in the local and demo fixtures; on hosted, those 58 items are unservable.

1. **Choose the candidates.** Pick human-reviewed items (CR-21, CR-24), spread across difficulties. Then confirm no student has seen any of them in practice:
   ```sql
   select q.id from practice_questions q
   where q.id = any(:candidates)
     and exists (select 1 from practice_attempts a where a.question_id = q.id and a.benchmark_id is null)
   ```
   **Pass:** no rows.
2. **Apply in one window, migration first.**
   - The reserve is its own reviewed migration (Research), named after `20261022050000`, so the applier runs it in the same dispatch right after the pool column.
   - It sets `pool = 'assessment'` for the listed candidate ids, and fails if any id isn't published, human-reviewed and unseen in practice.
   - No such migration exists yet; it can only be written once A2 has reviewed items.
   - The pool column and the reserve commit in separate transactions. If the reserve fails, `20261022050000` is live with no reserve: no check can be taken, and practice is unaffected. Fix the reserve migration and dispatch again before step 4. Don't deploy the client until the reserve is in.
3. **Check at the database and REST level, before any client changes:**
   - **(a)** `supabase/tests/assessment_pool.sql` passes on the H1 copy with the same migrations, and `scripts/local/live_stack.sh test` passes on main.
   - **(b)** The reserve is planned per exam version and difficulty:
     ```sql
     select exam_version_id, section, difficulty, count(*)
     from practice_questions
     where pool = 'assessment' and status = 'published' and review_current
     group by exam_version_id, section, difficulty
     ```
     It shows the planned reserve.
   - **(c)** Use a real student token, for a student with no live check and no reserved attempts:
     - a `practice_questions?pool=eq.assessment` read returns no rows;
     - `start_benchmark` without `p_exam_version` returns 22023.
4. **Deploy the client in the same window.**
   - Run `scripts/deploy/netlify_export.sh staging origin/main <outdir>`, then upload `<outdir>` to the canonical staging site as `DEPLOYING.md` describes.
   - Then run `scripts/deploy/verify_deploy.sh https://college-optimizer-staging.netlify.app <merge sha of #248>`.
   - **Don't redeploy staging from main before step 2.** Main's client selects `pool`, so against today's hosted schema every practice read fails with 42703.
5. Run H3 step 5.
6. **Before a reserve larger than one check's worth goes live:** resolve #263.
   - While any check is open, the whole reserve is readable.
   - Reading an item without attempting it isn't counted as seen.

**Other pairings:**
- **`20261022010000` role rules:** release with #247, already on main.
- **`20261006180300` exam plan:** release with `VITE_EXAM_PLAN` off until H3 step 4 passes.

**H3. Real accounts on canonical staging, then production (Owner runs the accounts; Design writes up the results).**
- Use real email addresses and two browsers or devices.
- Prefix every test account name with `qa-`, and archive the accounts afterwards.
- The preview site runs in demo mode (no Supabase variables, `DEPLOYING.md`), so it can't test accounts.

1. **Sign-up:** a parent signs up and confirms by the emailed link (A6, A7).
   **Pass:** the confirmation email arrives, and sign-in works only after confirming.
2. **Household:** the parent creates a household and a student. In a second browser for each, the parent invites:
   - (a) a co-guardian with the default permissions;
   - (b) a guardian with view progress only;
   - (c) the student, by invite code.

   **Pass:** each invitation is accepted once, and a second use of the same code is refused.
3. **View-only guardian (#243, #247):**
   - **In the UI,** signed in as (b):
     - the exam plan and interests are read-only, with no edit controls;
     - Remove is absent on a school the parent saved;
     - the invitation list shows no email addresses.
   - **Through the REST API,** with (b)'s token:
     - an insert or update on `student_exam_plan` and on `student_academic_interests` returns 0 rows or 42501;
     - `rpc/remove_household_school` on the parent's school returns 42501;
     - `household_invitations?select=recipient_email` returns 42501 (the column is revoked);
     - `rpc/household_invitation_recipients` returns no rows for (b), and 42501 for the student.

   **Pass:** every result is exactly as listed.
4. **Exam plan on the account.** This needs `exam_catalog` loaded, after C3 and the reviewed data import.
   - Build canonical staging with `VITE_EXAM_PLAN=true`.
   - The student adds AP Calculus AB with a score of 4 on a phone.

   **Pass:**
   - a row appears in `student_exam_plan`;
   - the parent's laptop shows it after a reload;
   - guardian (b) sees it but can't change it.
5. **Practice and checks**, signed in as the student (needs #266):
   1. Run two practice sessions.
   2. Start the starting check and finish it.
   3. Start a second check and finish it.
   4. Start a third check. Through the REST API with the student's token, while it is open:
      - an attempt on a practice question in the check;
      - an attempt on a reserved question with no check (`p_benchmark` null).
   5. Through the REST API with the parent's and guardian (b)'s tokens: `benchmark_questions` and `start_practice_attempt` on the student's open check.
   6. Complete or expire the third check. Then read `practice_questions?pool=eq.assessment` with the student's token.
   7. Leave a fourth check open past 4 hours, or, as the service role on staging, set that check's `practice_benchmarks.started_at` back 5 hours. Then answer in the open tab.

   **Pass:**
   - sessions contain no reserved item (an SQL join of `practice_session_items` to `practice_questions`);
   - every check item is `pool = 'assessment'`;
   - both student API attempts return 22023, and the parent's and guardian's calls return 42501;
   - the read in sub-step 6 returns only reserved items this student has attempted (their ids match `practice_attempts`), and no unattempted reserved item;
   - the expired tab says "This progress check has ended" with "Start a new check", and the earlier answer is stored once;
   - **when the reserve is smaller than a check:**
     - short sections are labelled "Shorter";
     - the history row shows the same label;
     - repeated sections say "Not a clean comparison" and show no verdict;
   - "Am I improving?" gives no verdict between checks with different sections or numbers of answers, or with repeats;
   - the Benchmarks card shows no "+N" change;
   - no screen shows an ACT or SAT score prediction.
6. **Cost & credit** (needs #253). The student has AP scores that earn credit at a saved school with a verified plan.
   **Pass:**
   - coverage is shown as coverage ("That is coverage, not a shorter degree.");
   - "Time and money saved: not shown" names the missing prerequisite, availability, sequencing and remaining-requirement records;
   - no dollar or semester saving appears on Cost & credit, Paths, Compare, the college detail page, the parent dashboard or the pilot plan.
7. **Rights gate:** on the H1 copy, as the service role, publish a question with no license.
   **Pass:** refused with 23514, citing `practice_questions_rights_gate`.
8. **Billing (A8):** follow `STRIPE_BILLING.md` in Stripe test mode, on staging with `VITE_BILLING_ENVIRONMENT=sandbox`.
   **Pass:**
   - checkout makes the entitlement Active;
   - cancelling in the portal shows "Ends <date>";
   - each webhook writes `subscriptions` once.

   One live-mode charge, with a real card refunded the same day, needs the owner's separate go-ahead for live charges. Lifting the Supabase hold doesn't cover it.
9. **Parent emails (A7, B2).** This needs the CR-22 migration applied and `send-weekly-digest` deployed with `DIGEST_CRON_SECRET`, `RESEND_API_KEY` and `DIGEST_FROM_EMAIL` set by name. Opt in one parent, then call the function three times with header `x-digest-secret: $DIGEST_CRON_SECRET`:
   1. body `{"mode":"weekly","week_start":"<last Monday>","dry_run":true}`;
   2. the same without `dry_run`;
   3. the second call again.

   **Pass:**
   - the dry-run text matches the dashboard;
   - exactly one email arrives;
   - the third call reports `already: 1, sent: 0`.

**H4. Flags (Owner, one at a time, each after its step passes):**
- `VITE_EXAM_PLAN` after H3.4.
- `VITE_ACCOUNT_SETUP` after the CR-26 migration and H3.1–2.
- `VITE_PRACTICE_REMINDERS` after CR-27 and R1–R7.
- `VITE_WEEKLY_DIGEST` after CR-22 and H3.9.
- `VITE_BILLING_ENABLED` after H3.8. `VITE_BILLING_ENVIRONMENT=sandbox` stays on staging only.
- `VITE_PLANNING_PILOT` only after the pilot gate (`PLANNING_ENGINE.md`).

**Pass:** each production build's env shows exactly the flags whose steps passed.

## R. Real-device acceptance (reminders and parent emails)

Local tests use a fake push service, fake FCM and fake mail. **They are not launch acceptance.**

**Prerequisites:**
1. The CR-27 and CR-22 migrations are applied. Today they exist only as reference SQL in `scripts/local/proposals/`; Research turns them into migrations (#218 A1–A3).
2. `send-practice-reminders`, `practice-reminder-action` and `send-weekly-digest` are deployed, each scheduled every 15 minutes (reminders, and the digest in `reminders_off` mode).
3. These secrets are set, by name only: `VAPID_PUBLIC_KEY`, `VAPID_PRIVATE_KEY`, `VAPID_SUBJECT`, `REMINDER_ACTION_SECRET`, `REMINDER_CRON_SECRET`, `APP_ORIGINS`, and `FCM_SERVICE_ACCOUNT` for M2.
4. A canonical staging build with `VITE_VAPID_PUBLIC_KEY` and `VITE_PRACTICE_REMINDERS=true`. This flag is on for staging only; production waits for H4.

**Devices:**
- an iPhone on iOS 16.4 or later, with the web app added to the Home Screen and notifications allowed;
- an Android phone with current Chrome;
- a laptop with Chrome.

Repeat everything in the native apps for M2 (`NATIVE_APPS.md` § Acceptance). The student account is the H3 student.

**Timing:**
- Reminder times are quarter-hours (:00, :15, :30, :45), and the sender runs every 15 minutes.
- "The next slot" means the next quarter-hour at least 5 minutes ahead.
- To avoid waiting, call `send-practice-reminders` by hand just after the slot, with header `x-reminder-secret: $REMINDER_CRON_SECRET`.

| # | Check | Steps | Pass | Owner | Status |
|---|---|---|---|---|---|
| R1 | Delivery at the chosen time; never in quiet hours, school hours, after today's practice, or past the limits | (a) Set the next slot; wait. (b) Set quiet hours covering the next slot, and that slot. (c) Same with school hours. (d) Finish today's planned practice, then set the next slot. (e) Set the daily limit to 1 and two slots. | (a) arrives in the first sender run at or after the slot (within 15 min); (b)–(d) nothing arrives; (e) exactly one arrives | Owner (devices) + Design | ⛔ hosted held |
| R2 | One notification per reminder across devices and sender runs | Sign the student in on the iPhone and the laptop, both subscribed. Set the next slot. Just after it, call `send-practice-reminders` twice by hand | Exactly one device shows exactly one notification; `practice_reminder_deliveries` has one row for the slot | Owner + Design | ⛔ |
| R3 | A tap opens a 5-minute session | Tap the R1 notification on each phone | The app opens a 5-minute practice session, and that delivery's `opened_at` is set | Owner + Design | ⛔ |
| R4 | "Remind me later" | Use the notification button (Android, laptop) or the home-screen card (iPhone) | One reminder arrives 60–75 min later; no email is sent to anyone | Owner + Design | ⛔ |
| R5 | Turning reminders off in the app | As the student, turn reminders off and confirm the parent notice | Exactly one email arrives in the parent's real inbox; the dashboard says "Emailed to you …" only after it arrives | Owner + Design | ⛔ needs A7 |
| R6 | Turning notifications off in device settings | Block notifications in iOS or Android settings, then open the app once | The family sees "blocked in device settings (as of …)" only after that open, never before | Owner + Design | ⛔ |
| R7 | Reinstall or a new device | Remove the Home Screen app (iPhone) or clear site data (Android). Wait for one reminder. Then re-add, subscribe, and wait for the next one | After the first reminder, the old row's `notification_devices.gone_at` is set (service-role SQL); the new device gets the next reminder | Owner + Design | ⛔ |

## D. Launch operations

| # | Item | Owner | Status |
|---|---|---|---|
| D1 | Lift the hold, then Netlify production deploy with production env vars | Owner | ⛔ (A1–A9) |
| D2 | Hosted validation pass (`APP_STATUS.md`, "Needs hosted validation") | Design + Research | ⛔ (A5) |
| D3 | Support and privacy contact inbox monitored | Owner | ⏳ |
| D4 | Keep AI hints off, or choose a provider and update the privacy policy | Owner | ✅ off by default |

## Done and verified locally (no action needed)

- **Practice cycle:** baseline → weekly plan → practice → progress checks.
  - New, seen-before and progress-check questions are separated.
  - Repeats never count as improvement.
  - "No new questions left" is shown plainly (#163).
- **Parent dashboard:** last-week recap, this week's goal, and an email preview.
  - Emails are sent only by the edge function, and only when it has a delivery record.
  - The function is tested locally end to end with a fake mail server; it has not been deployed.
- **Cost & credit view:** accepted credit, credit that applies to the plan, and whole-term coverage kept separate (#150). Time and money saved are withheld without completion records (#253).
- **Invitations:** two credentials, 72 h, single use, rate-limited, codes stored hashed.

## Research dependencies

All remaining database contracts are in one list: **#218**. That covers reference SQL waiting for migrations, open contracts, and questions found while integrating.
