# Launch checklist

Consolidated 2026-10-07. Owners:
- **Owner**: Brandon.
- **Research**: database and data workstream.
- **Design**: frontend and product workstream.
- **Content**: content lead, not yet named.
- **Counsel**: a lawyer, not yet engaged.

Status: ⛔ blocked · ⏳ not started · 🚧 in progress · ✅ done.

Hosted deployment is **held** (`.operations/supabase-live-hold.json`). Nothing below that touches hosted happens until the owner lifts the hold.

## A. Hard blockers: no public launch without these

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| A1 | Question bank at or above the launch minimum (≈ 430 ACT / ≈ 410 SAT, or one exam at ≈ 600) | Owner → Content | ⛔ | 58 items exist. Decisions are needed on scope, budget and AI drafting, and a content lead must be named (`CONTENT_PLAN.md` §6, #164, #19). |
| A2 | Human editorial review of every published item, including the existing 58 | Content | ⛔ | All 58 are reviewed by AI only (`human_reviewed: false`). There is no named human approver. |
| A3 | Privacy policy and terms approved | Owner + Counsel | 🚧 | Drafts and 12 decisions are in #165 (`docs/legal/`). Minimum age (13+ recommended), retention, entity and contacts are needed. |
| A4 | Data deletion and export path | Research (procedure) + Design (UI) | ⛔ | No deletion or export function exists. Choose manual with a stated response time, or in-app (`DECISIONS.md` #6). |
| A5 | Hosted Supabase restored, and migration history reconciled before applying anything | Owner (restore) → Research (#122) | ⛔ | Paused. Unapplied on hosted: `20261007120000` cost v2 and `20261007140000` question review (#142), plus CR-22 and CR-23 once they become migrations. |
| A6 | Real-account tests: sign-up with email confirmation, two-browser invitation acceptance, RLS with real tokens | Owner (runs the accounts) + Design (script) | ⛔ | Needs A5. Can't run locally: the local auth is a stub. |
| A7 | Email sending works | Owner | ⛔ | Verify the Resend domain (`mail.getcimiento.com` DNS) and set the `RESEND_API_KEY` secret. |
| A8 | Billing works with live Stripe | Owner | ⛔ | Owner setup in `STRIPE_BILLING.md`, then a real checkout, portal and cancel test. It has only been tested with mocks so far. |
| A9 | Privacy, Terms and age attestation in the app | Design | ⏳ | Waiting on A3 text. Links go in the footer, sign-up, invitation acceptance and email footers. |

## B. Needed for the core weekly loop to be honest in production

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| B1 | CR-23: server holds check items out of practice; `seen_before` and first-answer metrics | Research | ⏳ | The contract is on #37. Today live does this client-side. |
| B2 | CR-22: parent email opt-in, digest and inactivity payloads, delivery log, as a real migration | Research | ⏳ | Reference SQL in `scripts/local/proposals/cr22_parent_emails.sql`. Then the Owner deploys `send-weekly-digest`, adds the schedules and sets `VITE_WEEKLY_DIGEST=true` (after A5 and A7). |
| B3 | "Full" progress check falls back to a mini until a held-out full-length form exists | Design | ⏳ | A full check is capped at 99 per section, which is the whole small bank. Code change, no dependency. |
| B4 | CR-24 rights gate and CR-25 "report a problem" | Research, then Design (UI) | ⏳ | Contracts on #37. |
| B5 | Item statistics review, monthly | Content | ⏳ | Needs live traffic and CR-25. |

## C. Needed for the college-cost side to be complete (can launch labelled as partial)

| # | Item | Owner | Status | Concrete blocker |
|---|---|---|---|---|
| C1 | Verified institution records loaded on hosted | Research | ⛔ | Needs A5. Imports are held. |
| C2 | CR-17 tuition billing basis, CR-18 loan terms, CR-19 credit applicability, CR-20 cost-of-attendance period | Research | ⏳ | Without them, savings stay "potential", which is correct but limited. |
| C3 | CR-10 exam catalog (AP/CLEP plan in live), CR-15 home state, CR-11 award test minimums | Research | ⏳ | The live exam plan is not wired until the catalog exists. |

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
