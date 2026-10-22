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
- **Local:** checked by unit and component tests, or by `scripts/local/live_stack.sh test`. That runs every migration plus Design's reference SQL, with real SQL, RLS and RPCs: 56 end-to-end tests with #248.
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
| Reserved check questions never appear in practice; checks use only reserved questions | yes: server `20261022050000_assessment_pool` plus the client, both on #248 (open). Demo mirrors it | yes: `assessmentPool.local.test.ts` (practice can't read, get or attempt reserved items; a check refuses practice items; other roles refused) | no | #248 merge; paired release (CONTRACT_REQUESTS CR-23); a human-reviewed reserve (A1, A2) |
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
| A5 | Hosted Supabase restored, and migration history reconciled before applying anything | Owner (restore) → Research (#122) | ⛔ | Paused. The live history ends at `20261006104254`. Probably unapplied (verify per `SUPABASE_PAUSE.md` step 4): `20261006120000`–`20261006180400`, `20261007120000`, `20261007140000`, `20261022010000` role rules, `20261022030000` rights gate, `20261022040000` cost components, and `20261022050000` assessment pool once #248 merges. Steps: §H. |
| A6 | Real-account tests: sign-up with email confirmation, two-browser invitation acceptance, RLS with real tokens | Owner (runs the accounts) + Design (script) | ⛔ | Needs A5. The journeys and permissions pass against the local backend (#217). Sign-up, email confirmation and real tokens can't run locally: the local auth is a stub. |
| A7 | Email sending works | Owner | ⛔ | Verify the Resend domain (`mail.getcimiento.com` DNS) and set the `RESEND_API_KEY` secret. |
| A8 | Billing works with live Stripe | Owner | ⛔ | Owner setup in `STRIPE_BILLING.md`, then a real checkout, portal and cancel test. It has only been tested with mocks so far. |
| A9 | Privacy, Terms and age attestation in the app | Design | ⏳ | Waiting on A3 text. Links go in the footer, sign-up, invitation acceptance and email footers. |

## B. Needed for the core weekly loop to be honest in production

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| B1 | CR-23: reserved assessment pool on the server; `seen_before` and first-answer metrics | Research + Design | 🚧 #248 | Part 1 (pool, checks, repeats) and the client are on #248. Part 2 (`seen_before` on practice items, first-answer estimates) is open. The reserve count RPC `assessment_pool_status` is requested. |
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

Nothing here runs until the owner lifts the hold. For every step, record the date, who ran it, the build or commit, and the evidence (a screenshot, or the SQL output) in `docs/acceptance/<date>.md`. A step passes only when its "Pass" line holds exactly. Local fakes don't count.

**H0. Before applying anything (Owner, Research):**
1. Restore the project per `SUPABASE_PAUSE.md`, steps 1–3.
2. Read the live migration history (step 4). Apply a version only when the live history lacks it and its objects are absent.
3. Before `20261022030000` (rights gate), list published questions. Each needs an allowed license, attribution where required, and an origin, or must be unpublished by a reviewed change.
4. **Pass:** the live history matches `supabase/migration_history.json` plus the versions you intend to apply, and nothing else.

**H1. Apply and verify the migrations (Research):**
1. Apply in filename order on a Supabase branch first, never production first.
2. On the branch, run every `supabase/tests/*.sql` file the CI `database` job runs, in the same order.
3. Then apply to production in the same order. After each one, record `select version from supabase_migrations.schema_migrations order by version desc limit 1`.
4. **Pass:** every SQL suite passes on the branch, and the production history lists each version exactly once.

**H2. Paired releases (Research + Design).** A migration and the client that reads it ship together, with flags still off:
- **`20261022050000` assessment pool:** release it with the #248 client, and mark the reserve (`pool = 'assessment'`) in the same apply. Choose the reserve only from human-reviewed items (A2), and never from items a student has seen in practice (CONTRACT_REQUESTS CR-23).
- **`20261022010000` role rules:** release with #247 (already on main).
- **`20261006180300` exam plan:** release with `VITE_EXAM_PLAN` still off until H3 step 4 passes.
- **Pass:**
  - after the deploy, a signed-in student's `practice_questions` read returns no `pool = 'assessment'` row;
  - `select section, count(*) from practice_questions where pool = 'assessment' and status = 'published' and review_current group by section` shows the planned reserve.

**H3. Real accounts on production (Owner runs the accounts; Design writes up the results).** Use real email addresses and two browsers or devices. Prefix every test account name with `qa-`, and archive them afterwards.
1. **Sign-up:** a parent signs up and confirms by the emailed link (A6, A7). **Pass:** the confirmation email arrives, and sign-in works only after confirming.
2. **Household:** the parent creates a household and a student, and invites (a) a co-guardian with default permissions, (b) a guardian with view progress only, and (c) the student by invite code, each in a second browser. **Pass:** each invitation is accepted once, and a second use of the same code is refused.
3. **View-only guardian.** Signed in as guardian (b):
   - the exam plan and interests are read-only, with no edit controls;
   - Remove is absent on a school the parent saved;
   - the invitation list shows no email addresses.

   Then the same three writes and the address read via the REST API with (b)'s token. **Pass:** each write returns zero rows or 42501, and the read returns no address.
4. **Exam plan on the account:** the student adds AP Calculus AB with score 4 on a phone. **Pass:** the parent's laptop shows it after a reload. Then set `VITE_EXAM_PLAN=true` for a preview deploy only.
5. **Practice and checks.** Signed in as the student:
   - Run two practice sessions.
   - Start the starting check and finish it.
   - Start a second check.
   - Via the REST API with the student's token: an attempt on a practice question inside the open check, and an attempt on a reserved question with no check.

   **Pass:**
   - sessions contain no reserved item (SQL join on `practice_session_items`);
   - the check's items are all `pool = 'assessment'`;
   - both API attempts return 22023;
   - a short section is labelled "Shorter";
   - the second check's repeated sections say "Not a clean comparison" and show no verdict.
6. **Rights gate:** as the service role on a branch copy, publish a question with no license. **Pass:** refused.
7. **Billing (A8):** follow `STRIPE_BILLING.md` in Stripe test mode, then once in live mode with a real card refunded the same day. **Pass:** checkout, portal and cancel each change the entitlement exactly once.
8. **Parent emails (A7, B2):**
   - Opt in one parent and run `send-weekly-digest` in dry-run mode.
   - Then run it for real once.
   - Then run it again.

   **Pass:**
   - the dry-run content matches the dashboard;
   - exactly one email arrives;
   - running it again sends nothing.

**H4. Flags (Owner, one at a time, each after its step passes):**
- `VITE_EXAM_PLAN` after H3.4.
- `VITE_ACCOUNT_SETUP` after the CR-26 migration and H3.1–2.
- `VITE_PRACTICE_REMINDERS` after CR-27 and R1–R7.
- `VITE_WEEKLY_DIGEST` after CR-22 and H3.8.
- `VITE_PLANNING_PILOT` only after the pilot gate (`PLANNING_ENGINE.md`).
- **Pass:** each production build's env shows exactly the flags whose steps passed.

## R. Real-device acceptance (reminders and parent emails)

Local tests use a fake push service, fake FCM and fake mail. **They are not launch acceptance.**

**Devices:**
- an iPhone on iOS 16.4 or later, with the web app added to the Home Screen and notifications allowed;
- an Android phone with current Chrome;
- a laptop with Chrome.

Repeat everything in the native apps for milestone M2 (`NATIVE_APPS.md` § Acceptance). The student account is the H3 student. Set reminders to 2 minutes from now unless a step says otherwise.

| # | Check | Steps | Pass | Owner | Status |
|---|---|---|---|---|---|
| R1 | Delivery at the chosen time; never in quiet hours, school hours, after today's practice, or past the limits | (a) Set a time 2 min ahead; wait. (b) Set quiet hours covering now and a time inside them. (c) Same with school hours. (d) Finish today's planned practice, then set a time 2 min ahead. (e) Set the daily limit to 1 and two times. | (a) arrives within 2 min of the time; (b)–(d) nothing arrives; (e) exactly one arrives | Owner (devices) + Design | ⛔ hosted held |
| R2 | One notification per reminder across devices and sender runs | Sign the student in on the iPhone and laptop, both subscribed. Set a time 2 min ahead, and trigger `send-practice-reminders` twice within the same minute | Exactly one device shows exactly one notification; the delivery log has one row | Owner + Design | ⛔ |
| R3 | A tap opens a 5-minute session | Tap the R1 notification on each phone | The app opens a 5-minute practice session; the delivery is marked opened | Owner + Design | ⛔ |
| R4 | "Remind me later" | Use the notification button (Android, laptop) or the home-screen card (iPhone) | One reminder arrives 60 ± 2 min later; no email is sent to anyone | Owner + Design | ⛔ |
| R5 | Turning reminders off in the app | As the student, turn reminders off and confirm the parent notice | Exactly one email arrives in the parent's real inbox; the dashboard says "Emailed to you …" only after it arrived | Owner + Design | ⛔ needs A7 |
| R6 | Turning notifications off in device settings | Block notifications in iOS or Android settings, then open the app once | The family sees "blocked in device settings (as of …)" only after that open, never before | Owner + Design | ⛔ |
| R7 | Reinstall or a new device | Remove and re-add the Home Screen app (iPhone) or clear site data (Android); subscribe again; set a time 2 min ahead | The new device gets it; the old subscription is retired after the push service rejects it | Owner + Design | ⛔ |

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
- **Cost & credit view:** accepted credit, credit in the major's plan and whole-term coverage kept separate. Time and money saved are withheld without completion records (#253).
- **Invitations:** two credentials, 72 h, single use, rate-limited, codes stored hashed.

## Research dependencies

All remaining database contracts are in one list: **#218**. That covers reference SQL waiting for migrations, open contracts, and questions found while integrating.
