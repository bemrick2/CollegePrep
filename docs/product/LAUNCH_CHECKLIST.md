# Launch checklist

Consolidated 2026-10-07; status updated 2026-10-21. Owners:
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
- **Local:** checked by unit and component tests, or by `scripts/local/live_stack.sh test`. That runs every migration plus Design's reference SQL, with real SQL, RLS and RPCs: 35 end-to-end tests.
- **Hosted:** checked on the hosted project. **Nothing is hosted-tested since the 2026-10-06 pause.**
- **Blocked by:** what is still in the way.

Simulated tests (fake push service, fake FCM, fake mail) prove the code paths, not delivery.

| Capability | Implemented | Local | Hosted | Blocked by |
|---|---|---|---|---|
| Parent journey: four-screen setup, reload/resume, finished setup never asked again | yes | yes: demo mobile run (resumes at step 3); local backend (resume on another device; #217) | no | CR-26 migration (#218 A1); A5 |
| Invited student: single-use code, guardian's choices on every device, can't change plan or goal | yes | yes (#217) | no | Real two-browser invitation acceptance with email confirmation (A6); invitation email (A7) |
| Student who signs up alone (no household) | yes | yes (#217) | no | A5, A6 |
| Guardian permissions (default co-guardian; view-only guardian) | yes (server rules; the app offers exam-plan editing only to the student or a guardian with set-goals, #219) | yes (#217, #219) | no | #218 C1: the server still lets any guardian write the exam plan and interests. Is that intended? |
| Quick practice vs a separately scheduled benchmark; a started benchmark isn't a result | yes | yes (#217; component tests) | no | CR-26 for the schedule on the account |
| AP/CLEP exam plan on the account (CR-10) | yes, behind `VITE_EXAM_PLAN` (#219) | yes (#219) | no | `20261006180300` unapplied on hosted; #218 C1 |
| Practice reminders: settings, quiet/school hours, limits, snooze, one notification per reminder | yes, behind `VITE_PRACTICE_REMINDERS` | yes, against fakes | no | CR-27 migration (#218 A2); VAPID and FCM secrets; real devices R1–R7 |
| Guardian notice when a linked student turns reminders off | yes | yes, against fake mail; the dashboard shows "Emailed to you" only after a recorded send | no | CR-22 and CR-27 migrations; email domain (A7); R5 |
| Guardian sees the last **recorded** reminder send (not a test), and device permission separately from the in-app switch | yes (#220) | yes | no | as above |
| Parent weekly summary and inactivity emails | yes, behind `VITE_WEEKLY_DIGEST` | yes, against fake mail | no | CR-22 migration; A7; schedules |
| Only reviewed questions served | yes (CR-21 gate) | yes | no | `20261007140000` unapplied; review is AI only (A2) |
| Questions held for the next check never appear in practice | yes: demo; live via an interim client rule (#221), which fills the session with fresh, then review questions | yes (#221: fresh fill, review-only state) | no | CR-23, the server-side holdout (#218 B1) |
| Repeats labeled and never counted as improvement | yes | yes | no | none |
| Honest when fresh questions run out | yes (#221 copy) | yes | no | A1, the bank size (`PRACTICE_READINESS.md`) |
| No ACT/SAT score prediction | yes (`PRACTICE_ESTIMATES_VALIDATED = false`) | yes | n/a | Validated model (CR-3) |
| Human editorial review | ledger, packets and import (#207) | yes | n/a | A named content lead (A2) |

## A. Hard blockers: no public launch without these

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| A1 | Question bank at or above the launch minimum (≈ 430 ACT / ≈ 410 SAT, or one exam at ≈ 600) | Owner → Content | ⛔ | 58 items exist. Sizing for 20/40/60 a week over 12 weeks and a year, per exam, with reserved checks: `QUESTION_BANK_RECOMMENDATION.md`. The recommendation is about 470 unique items (25% review) or about 600 (all fresh) for one exam, 12 weeks at 40. Decisions are needed on scope, budget and AI drafting, and a content lead must be named (`CONTENT_PLAN.md` §6, #164, #19). |
| A2 | Human editorial review of every published item, including the existing 58 | Content | ⛔ | All 58 are reviewed by AI only. Human-approved: 0 of 58. The tooling is ready (#207: ledger, blind packets, sign-off import, rules enforced by tests). There is no named human approver. |
| A3 | Privacy policy and terms approved | Owner + Counsel | 🚧 | Drafts and 12 decisions are in #165 (`docs/legal/`). Minimum age (13+ recommended), retention, entity and contacts are needed. |
| A4 | Data deletion and export path | Research (procedure) + Design (UI) | ⛔ | No deletion or export function exists. Choose manual with a stated response time, or in-app (`DECISIONS.md` #6). |
| A5 | Hosted Supabase restored, and migration history reconciled before applying anything | Owner (restore) → Research (#122) | ⛔ | Paused. Unapplied on hosted: `20261007120000` cost v2 and `20261007140000` question review (#142), plus CR-22 and CR-23 once they become migrations. |
| A6 | Real-account tests: sign-up with email confirmation, two-browser invitation acceptance, RLS with real tokens | Owner (runs the accounts) + Design (script) | ⛔ | Needs A5. The journeys and permissions pass against the local backend (#217). Sign-up, email confirmation and real tokens can't run locally: the local auth is a stub. |
| A7 | Email sending works | Owner | ⛔ | Verify the Resend domain (`mail.getcimiento.com` DNS) and set the `RESEND_API_KEY` secret. |
| A8 | Billing works with live Stripe | Owner | ⛔ | Owner setup in `STRIPE_BILLING.md`, then a real checkout, portal and cancel test. It has only been tested with mocks so far. |
| A9 | Privacy, Terms and age attestation in the app | Design | ⏳ | Waiting on A3 text. Links go in the footer, sign-up, invitation acceptance and email footers. |

## B. Needed for the core weekly loop to be honest in production

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| B1 | CR-23: server holds check items out of practice; `seen_before` and first-answer metrics | Research | ⏳ | Contract on #37, tracked in #218 B1. Until it lands, live holds check items out on the client. Before #221 it didn't: a check could reuse practised questions. |
| B2 | CR-22: parent email opt-in, digest and inactivity payloads, delivery log, as a real migration | Research | ⏳ | Reference SQL in `scripts/local/proposals/cr22_parent_emails.sql`. Then the Owner deploys `send-weekly-digest`, adds the schedules and sets `VITE_WEEKLY_DIGEST=true` (after A5 and A7). |
| B3 | "Full" progress check falls back to a mini until a held-out full-length form exists | Design | 🚧 #167 | Done in code (`FULL_FORM_READY = false`); switch on only when Content delivers a held-out full-length form per exam. |
| B4 | CR-24 rights gate and CR-25 "report a problem" | Research, then Design (UI) | ⏳ | Contracts on #37. |
| B5 | Item statistics review, monthly | Content | ⏳ | Needs live traffic and CR-25. |

## C. Needed for the college-cost side to be complete (can launch labelled as partial)

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| C1 | Verified institution records loaded on hosted | Research | ⛔ | Needs A5. Imports are held. |
| C2 | CR-17 tuition billing basis, CR-18 loan terms, CR-19 credit applicability, CR-20 cost-of-attendance period | Research | ⏳ | Without them, savings stay "potential", which is correct but limited. |
| C3 | CR-10 exam catalog (AP/CLEP plan in live), CR-15 home state, CR-11 award test minimums | Research | ⏳ | The live exam plan is not wired until the catalog exists. |

## R. Real-device acceptance (reminders and parent emails)

Local tests use a fake push service, fake FCM and fake mail. **They are not launch acceptance.** Once hosted is available, run each of the seven checks in `NATIVE_APPS.md` § Acceptance on a real iPhone (web push from the Home Screen web app) and a real Android phone. Repeat them in the native apps for milestone M2.

| # | Check | Owner | Status |
|---|---|---|---|
| R1 | Delivery at the chosen time. Nothing during quiet hours, school hours, after today's practice, or past the limits | Owner (devices) + Design | ⛔ hosted held |
| R2 | One notification per reminder across a phone and a laptop, and across overlapping sender runs | Owner + Design | ⛔ |
| R3 | A tap opens a 5-minute session | Owner + Design | ⛔ |
| R4 | "Remind me later" (notification button, or the home-screen card) pauses for an hour and emails no one | Owner + Design | ⛔ |
| R5 | Turning reminders off in the app: exactly one real guardian email, and the dashboard shows "Emailed to you" only after it's sent | Owner + Design | ⛔ needs A7 |
| R6 | Turning notifications off in device settings shows "blocked" after the next app open, never sooner | Owner + Design | ⛔ |
| R7 | Reinstall or a new device: the old one is retired and the new one gets the next reminder | Owner + Design | ⛔ |

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
- **Savings view:** potential-only savings; accepted, applicable and term-removing credit kept separate (#150).
- **Invitations:** two credentials, 72 h, single use, rate-limited, codes stored hashed.

## Research dependencies

All remaining database contracts are in one list: **#218**. That covers reference SQL waiting for migrations, open contracts, and questions found while integrating.
