# Prep & Price: release status (the single checklist)

**As of main `aeb45bbb73` (2026-11-03).** Design owns this document; Research and Deep Dive correct their own rows here
or on #218. It replaces status claims in older summaries. Detailed procedures stay where they are:
`LAUNCH_CHECKLIST.md` (A–H, R steps), `PILOT_ACCEPTANCE.md` (planning pilot), `BANK_INTAKE_2026-10-28.md`
(question bank).

Tags: [Certain] checked in the repository or a tool on this date · [Likely] strong evidence, not directly checked ·
[Guessing] judgement. **Open questions to Research and Deep Dive** are on #218 (2026-11-03, 22:31 and 22:40 UTC).
Rows that depend on their answers say "pending reply". This document was fact-checked against the repository by an
independent reviewer before merge.

## Verdict

**We are not almost done.** [Likely] The application code for a reduced first release is largely built and tested
locally. What is missing is mostly owner-gated:
- **Hosted:** nothing has been applied since 2026-10-06, and nothing is acceptance-tested.
- **Questions:** 0 are human-approved, so the app has no question it may serve to a student.
- **Legal:** no privacy policy or terms are approved.

**Two engineering problems are on the critical path** [Certain, from `scripts/apply_migrations.py`,
`scripts/check_migration_history.py` and the migrations]:
1. **The newest migrations are gated behind human review.**
   - The applier applies pending migrations strictly in filename order.
   - It refuses the assessment-pool migration (`20261022050000`) without a reserve script.
   - A reserve can't be empty and needs individually human-approved, published items.

   So none of the seven `20261102*` migrations can reach hosted before human review produces a reserve. Those are
   account setup (CR-26), parent emails, reminders, question reports, seen-before, home state and data requests. Three
   of them also use the pool's tables (question reports, seen-before, data requests), so this can't be solved by
   reordering alone. It needs an owner decision (O9, §4).
2. **There is no defined path for getting reviewed questions onto hosted.** The 2026-10-06 audit found 0 published
   questions and 0 exam versions on hosted (`STRIPE_BILLING.md`). How approved items get there is pending reply
   (Research).

**An owner-tested pilot** needs every row of §3A, not only a restore. **Public launch** additionally needs a reviewed
bank at the launch minimum and approved legal text (§3B).

## 1. What works today

Four separate levels, never merged into one.

| Level | What is true [Certain unless tagged] |
|---|---|
| **Implemented locally** | Household accounts and invitations, guardian roles, four-screen setup, practice and the weekly plan, reserved progress checks with server-assigned items, reminders and parent emails (against fakes), Stripe (against mocks), question intake and review tooling, the data-request procedure, college discovery and comparison, the planning pilot. `scripts/local/live_stack.sh test` (real SQL, RLS and RPCs; stub auth; fake push and mail) runs in CI when web or database paths change. |
| **Merged into main** | All of the above, at `aeb45bbb73`. The web suite passed 508 (71 skipped) on the #302 head. There are 40 migrations in the repository. |
| **Applied to hosted** | Only what was applied before the 2026-10-06 pause: **21 migrations, through `20261006120000`** (`SUPABASE_PAUSE.md`; the manifest lists 20 and must be reconciled). **19 are unapplied.** Five edge functions are deployed: billing-plans, billing-checkout, billing-portal, stripe-webhook and send-household-invitation. Staging Auth is configured for `college-optimizer-staging.netlify.app`. What hosted holds now is unknown: the 2026-10-02 reconciliation counted 17,865 source records, and the pause audit recorded 25,651 in the ledger. Canonical staging serves one upload from 2026-10-06 16:09 UTC with no commit recorded, pointing at the paused project. |
| **Tested successfully on hosted** | **Before the pause, recorded:** (1) reference-data reconciliation on 2026-10-02 (`docs/coverage/live-supabase.json`); (2) on 2026-10-06 on staging, a sign-up → confirmation email → return, and a sandbox checkout, portal and cancel at period end, with production isolation checked (`STRIPE_BILLING.md`, "Staging Auth confirmation and sandbox billing"). Both predate 19 migrations and are not the H3 acceptance tests. **Since the pause: nothing.** No practice, check, invitation acceptance, guardian-role, reminder or parent-email journey has a hosted pass. `docs/acceptance/` doesn't exist. |

**Hosted project state:** `.operations/supabase-live-hold.json` says `hold: true`. The owner paused the project on
2026-10-06. This session's Supabase connection can't see the CollegePrep project, which is in a different
organization, so its current state isn't confirmed from here.

**One live item to reconcile on resume:** a sandbox subscription was left active until 2026-11-06, and webhook retries
may be pending (`SUPABASE_PAUSE.md`).

## 2. Release status by area

**Statuses:** Complete · In progress · Blocked · Not required for initial release (meaning the recommended reduced
release, §3).

| Area | Status | Local | Hosted | What's missing (owner) |
|---|---|---|---|---|
| Signup, login, student and guardian permissions, setup | **Blocked** | Implemented and tested locally; role rules tested against the server (#233, #243) | Sign-up with email confirmation passed on staging 2026-10-06; role rules and CR-26 setup unapplied; invitation acceptance untested | Restore (Owner) → migrations (Research; O9) → email (Owner, A7) → H3.1–3. `VITE_ACCOUNT_SETUP` must be on for setup to be saved to the account |
| College discovery, comparison, tuition, scholarships | **In progress** | Implemented | 2026-10-02 reference data reconciled; cost v2 and C3 components unapplied; current contents unknown | Current-year data is thin: verified 2026-27 costs at 313 schools (416 records) and awards at 60 schools (392 records); the rest is 2023-24 federal data, labelled by year. The per-semester fix (Design, #305, in review). #296 (tuition batch 2, draft): Research to say whether release needs it |
| Degree-plan pilot and exam-credit mappings | **In progress** | Pilot page complete behind `VITE_PLANNING_PILOT` (#302) | Nothing | #191 (Research; O5); truncated rows in 2 pilot plans (Deep Dive); privacy rows (Owner + counsel); mobile pass (Design) |
| Question-bank import, review eligibility, practice | **Blocked** | Intake, packets, sign-off ledger, the serve-only-approved gate (CR-21) and the rights gate (CR-24) built and tested | 0 published questions, 0 exam versions (2026-10-06 audit); gates unapplied | Content lead and reviewers (Owner, O2); a hosted import path (Research) |
| Reserved progress checks | **Blocked** | Built and tested (#248, #279, #291; T1–T12) | Unapplied | Human-approved reserve items, or O9. ACT English and Reading can't be reserved as built (B6) |
| Reminders and parent emails | **Not required for initial release** (recommended) | Built; tested against fake push and mail | Unapplied; functions not deployed | Optional: CR-22/27 migrations, VAPID/FCM, Resend secrets, real devices (R1–R7). Invitation and confirmation email is still required (A7) |
| Billing | **Not required for initial release** if free (recommended) | Tested with mocks | Sandbox checkout, portal and cancel passed on staging 2026-10-06; live never tested | If paid: Stripe live (Owner, A8) and server enforcement (Research, A10, #108; today a free account can call paid RPCs directly) |
| Privacy, export, deletion | **Blocked** | Data-request procedure and runbook merged (#294) | Unapplied | Privacy and terms approved (Owner + counsel, A3); runbook §0 (A4); in-app links and age attestation (Design, A9, after A3) |
| Mobile usability | **In progress** | 390 px demo runs (setup; the planning pilot earlier) | None | Design: a 390 px pass of the release flows on main (P11); Owner: real phones during H3 (L8) |
| Migrations, deployment, end-to-end acceptance | **Blocked** | 40 migrations apply on the local stack in CI | 21 applied, 19 pending; hold on; staging stale | P1–P8. Before lifting the hold, remove the push trigger from `deploy-migrations.yml` (H1.3); otherwise a merge would apply migrations to production without the copy-first step |
| Operations: backups, monitoring, production callbacks | **Not started** | — | The pause is not a tested backup (`SUPABASE_PAUSE.md`) | Owner: a backup and restore decision (PITR window, A4). Design/Research: error monitoring. Owner: production Auth callback URLs (`STRIPE_BILLING.md`) |

### Question bank: actual counts [Certain, from `PRACTICE_READINESS.md`, `BANK_INTAKE_2026-10-28.md`, `STRIPE_BILLING.md` on main]

"Publication-eligible" means a current approval recorded as `human:` plus an allowed license (the CR-21 and CR-24
gates). "Usable" means a hosted student could be served it today.

| Exam / section | In the app (demo / local): practice + reserve | On hosted (2026-10-06) | Publication-eligible | Usable on hosted (practice / checks) | Delivered drafts passing the import contract (not imported; 0 approved) | Reservable under the passage rule |
|---|---|---|---|---|---|---|
| ACT English | 10 (7 + 3) | 0 | 0 | 0 / 0 | 691 | 0 (every item shares an essay) |
| ACT Math | 12 (8 + 4) | 0 | 0 | 0 / 0 | 759 | 759 |
| ACT Reading | 8 (5 + 3) | 0 | 0 | 0 / 0 | 686 | 0 (every item shares a passage) |
| ACT Science | 8 (5 + 3) | 0 | 0 | 0 / 0 | **0** | 0 |
| SAT Reading and Writing | 10 (6 + 4) | 0 | 0 | 0 / 0 | 695 | 695 |
| SAT Math | 10 (6 + 4) | 0 | 0 | 0 / 0 | 1,000 | 1,000 |
| **Total** | **58 (37 + 21)** | **0** | **0** | **0 / 0** | **3,831** | — |

**Reconciling the saved banks:**
- **The delivered bank** has 5,843 drafts on branch `qb/final-reconciled-bank-v2-2026-10-28` (`6b253cf3`, not on
  main):
  - 3,831 pass the import contract and were taken in as a local dry run;
  - 1,620 ChatGPT drafts lack required fields;
  - 392 are pending, held, duplicates or retired.
- **The app's 58 items** are AI-authored and AI-reviewed, with 0 human-approved. Under the rights gate they would also
  be unservable on hosted.
- **No draft counts toward readiness until a person approves it.**

**Launch minimum** (`QUESTION_BANK_RECOMMENDATION.md`): one exam at 12 weeks with 25% review needs about 470 ACT or
448 SAT approved items; both exams at 8 weeks need about 430 ACT plus 410 SAT.
- **ACT:** today's content can't support an ACT launch [Certain]. There are no ACT Science drafts, and ACT English
  and Reading can't supply check items (B6).
- **SAT:** SAT is the only exam the delivered content could support. It has 1,695 contract-valid drafts, all on
  single-question passages, none approved yet.

## 3. Exact finish line

**Recommended first release (reduced):** free, web only, SAT only, English only.

**Flags:**
- **On:** `VITE_ACCOUNT_SETUP` (after CR-26 and H3.1–2).
- **Off:**
  - `VITE_BILLING_ENABLED`;
  - `VITE_PRACTICE_REMINDERS`;
  - `VITE_WEEKLY_DIGEST`;
  - `VITE_EXAM_PLAN`;
  - `VITE_PLANNING_PILOT`, until its gate passes.
- **Also off:** AI hints, the full-length check (`FULL_FORM_READY = false`), native apps and score prediction.

**What the release offers:**
- household accounts with guardian roles and student invitations;
- setup and a weekly plan;
- SAT practice from human-approved items;
- starting and mini progress checks from a reviewed reserve;
- the in-app parent summary;
- college discovery and comparison, with data years labelled.

**Owner-tested pilot:** the owner and `qa-` accounts on canonical staging, with real Auth and email.

### A. Blockers to an owner-tested pilot

| # | Blocker | Owner | PR / issue | Depends on | Pass condition |
|---|---|---|---|---|---|
| P1 | Restore the hosted project and reconcile it | Owner → Research | `SUPABASE_PAUSE.md` | O1 | Project `ACTIVE_HEALTHY`. H0: the live history equals the manifest plus `20261006120000`, and every version to apply is absent live. Sandbox subscription and webhook retries reconciled. Push trigger removed from `deploy-migrations.yml` before `hold=false` |
| P2 | Decide how the pool migration ships | Owner (O9) → Research | #218 | — | Under O9(a): a reviewed "no reserve yet" release of `20261022050000` + `20261023010000` passes `assessment_pool.sql` and `assessment_assignment.sql` on a copy, with checks showing "Not measured". Under O9(b): the reserve exists first (P5, P6a) |
| P3a | Apply migrations up to `20261022040000` (copy first, then hosted) | Research | H1 | P1 | The suites pass on the copy; the production history lists each version once; import reconciliation shows no differences |
| P5 | A reviewed SAT pilot set | Owner (reviewer) → Design (packets, ledger) | A2, #254 | O2 | About 56 SAT items approved per item with `human:` in the ledger: one week of practice (≈ 48) plus 8 reserve, which gives a shortened 8-of-18 starting check [Guessing on what is enough for a pilot] |
| P6a | Get approved items onto hosted | Research (path) + Design (contract) | pending reply | P3a, P5 | Approved items are published on hosted; a per-section count matches the ledger |
| P3b | Apply the pool, assignment and `20261102*` migrations | Research | H1/H2 | P2, P3a (+ P6a under O9(b)) | The full suites pass on the copy; production history has all 40 once; the H2 reserve query shows the planned reserve, or none under O9(a) |
| P4 | Email sending (A7) | Owner | A7 | P1 | Resend domain `mail.getcimiento.com` verified, `RESEND_API_KEY` set; H3.1 passes |
| P7 | Deploy staging from main | Research or Design; Owner approves | `DEPLOYING.md` | P3b | `verify_deploy.sh` reports the merge commit on canonical staging |
| P8 | Owner acceptance run | Owner runs, Design writes up | H3.1–3.3, 3.5, 3.6, 3.7; `docs/acceptance/<date>.md` | P4, P6a, P7 | Every listed H3 "Pass" line holds exactly, with evidence. (H3.4 exam plan is out of scope.) |
| P9 | Planning pilot, if included | Research (#191), Deep Dive, Owner (O5) | `PILOT_ACCEPTANCE.md` §8 | P3b | Checklist items 4–7 done; flag on for staging only |
| P10 | Per-semester costs never shown as annual | Design | #305 | — | Merged with tests on every listed path |
| P11 | Mobile pass at 390 px of the release flows | Design | — | — | Screenshots of setup, practice, check, parent summary and college pages on main at 390 px; no horizontal scroll or clipped controls; recorded in `docs/acceptance/` |

### B. Additional blockers to public launch

| # | Blocker | Owner | PR / issue | Depends on | Pass condition |
|---|---|---|---|---|---|
| L1 | SAT bank at the launch minimum (A1) | Owner → Content | A1 | O2 | At least 448 SAT items human-approved and published on hosted, both sections, a reserve of at least one starting check; count query recorded |
| L2 | Every published item human-reviewed (A2) | Content | A2 | O2 | 0 published items without a current `human:` approval (query recorded) |
| L3 | Privacy policy and terms approved (A3) | Owner + counsel | #165 | O3 | Signed-off text committed |
| L4 | In-app privacy, terms and age attestation (A9) | Design | A9 | L3 | Links in the footer, sign-up, invitation acceptance and emails; component tests |
| L5 | Data-request decisions (A4) | Owner + counsel | #294, `DATA_REQUESTS.md` §0 | L3, P3b | §0 placeholders replaced; one export and one deletion run on a `qa-` household, recorded |
| L6 | Support and privacy inbox monitored (D3) | Owner | D3 | — | The address is published in the policy and monitored |
| L7 | Backups, monitoring and production callbacks | Owner (backup plan, callbacks); Research (restore test); Design (error monitoring) | — | P1 | One restore from backup to a copy succeeds; production Auth callbacks allowlisted; client errors reported somewhere watched |
| L8 | Real-device pass | Owner + Design | — | P7 | The P8 flows on an iPhone and an Android phone, with screenshots in `docs/acceptance/` |
| L9 | Production deploy and flags (D1, H4) | Owner | D1 | P8, L1–L8 | The production build's env shows exactly the flags whose steps passed |
| L10 | Only if paid: Stripe live (A8) and server enforcement (A10) | Owner; Research → Design | #108 | P3b | H3.8 passes; a free account's direct calls to paid RPCs are refused in tests |

### C. Optional, after release

- Reminders and parent emails (R1–R7, H3.9).
- ACT. It needs:
  - Science content;
  - whole-passage reserve sets (B6);
  - a passage key in the import contract.
- The exam plan on the account (H3.4).
- The 1,620 ChatGPT drafts.
- The full-length check.
- Native apps.
- Paid Prep.
- Planning-pilot additions: UTK and MTSU plans, and the plan-reader backlog.
- Broader national program and tuition research.
- Validated score prediction.

## 4. Owner actions

**Necessary:**

| # | Decision or action | Recommendation |
|---|---|---|
| O1 | Restore hosted (today limited by the Free plan's active slots) | Restore now. If no Free slot is free, put CollegePrep's organization on a paid plan, which also gives backups and a proper copy for H1 [Likely ≈ $25/month for Pro; check current pricing] |
| O2 | Name the content lead and reviewers | Pilot: review the ≈ 56-item SAT set yourself. Launch: name a qualified reviewer for ≥ 448 SAT items |
| O3 | Privacy policy, terms and data-request terms, with counsel | Adopt `docs/legal/DECISIONS.md`: 13+, parent attestation, manual deletion and export by email. Fill in runbook §0 |
| O4 | First-release scope | Free, web, SAT only, with the flags in §3 |
| O5 | Exam credit in the planning pilot | Keep UTC credit placement excluded (plans and costs shown, tables shown as "not yet verified"), so #191 stops blocking. Approve moving UTK's tables to partially verified (#191, #218 C4) |
| O6 | Email | Verify `mail.getcimiento.com` in Resend and set `RESEND_API_KEY`, right after O1 |
| O7 | Run the acceptance accounts (H3) | Two browsers, `qa-` accounts |
| O8 | Abandoned starting check: no check for 28 days, then a mini (#279) | Accept for release |
| O9 | How the assessment pool ships: (a) apply it with an explicitly empty reserve, so checks show "Not measured" until reviewed items exist; or (b) keep the rule that the pool ships only with a reserve, which keeps account setup, reports, home state and data requests off hosted until review produces one | **(a)**. The client already handles "no reserve". It unblocks every later migration, including the data-request procedure. Keep reserve candidates unpublished until the reserve is made, so practice can't expose them. This reverses the CR-23 release rule in `DEPLOYING.md`, so it needs your approval |

**Optional:**
- Stripe live setup and a live-charge go-ahead (paid launch only).
- VAPID/FCM keys and devices for reminders.
- B6 passage sets (ACT only).
- Dropping the two truncated UTC pilot plans if Deep Dive can't fix them quickly.
- The JHU Bachelor of Music record (Research; not release).

## 5. Next steps, in dependency order

**To the owner-tested pilot:**
1. Start these in parallel:
   - O1 restore;
   - O9 decision;
   - O6 email;
   - O2 review of ≈ 56 SAT items;
   - P10 and P11 (Design);
   - Research's hosted import path.
2. Then, in order:
   - P1 reconcile;
   - P3a;
   - P2 (rehearsed on a copy);
   - P6a;
   - P3b;
   - P7 staging;
   - P8 owner acceptance.

**To public launch:**
1. Alongside the pilot:
   - L1/L2: review to ≥ 448 SAT items;
   - L3, then L4 and L5;
   - L6;
   - L7.
2. After the pilot passes: L8, then L9 production with only the passed flags.

**Effort** (only where there is evidence):
- **Design's remaining work is small and defined:** P10 is in review, then P11, A9 and the acceptance write-ups.
- **Research's work** is P2/P3 on a copy plus an import path. The tooling for H1 and H2 exists and is tested locally,
  but the import path doesn't exist yet. Pending reply for an estimate.
- **The long poles can't be estimated from the repository:**
  - when hosted is restored;
  - reviewer time for ≥ 448 SAT items through review stages 3–8 (no throughput data yet);
  - counsel's turnaround.

  [Guessing] With a reviewer in place, the SAT launch set is likely weeks of review, not days.
