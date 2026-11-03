# Prep & Price: release status (the single checklist)

**As of main `aeb45bbb73` (2026-11-03).** Design owns this document; Research and Deep Dive correct their own rows here
or on #218. It replaces status claims in older summaries. Detailed procedures stay where they are:
`LAUNCH_CHECKLIST.md` (A–H, R steps), `PILOT_ACCEPTANCE.md` (planning pilot), `BANK_INTAKE_2026-10-28.md`
(question bank).

Tags: [Certain] checked in the repository or a tool on this date · [Likely] strong evidence, not directly checked ·
[Guessing] judgement. **Open questions to Research and Deep Dive** are on #218 (comments 6617129058 and 6617177874).
Rows that depend on their answers say "pending reply".

## Verdict

**We are not almost done.** [Certain] Most of the engineering a reduced first release needs is built and tested
locally. But on hosted, **nothing is applied since 2026-10-06 and nothing is acceptance-tested**. **0 questions are
human-approved**, so the app has no question it may serve to students, and no privacy policy or terms are approved.
Those three gaps are mostly owner-gated, not engineering-gated.

**An owner-tested pilot is within reach** once hosted is restored, email is verified and a small reviewed SAT set
exists (§3A). **Public launch** additionally needs a reviewed bank at the launch minimum and approved legal text (§3B).

**One finding changes the critical path** [Certain, from `scripts/apply_migrations.py` and
`make_reserve_migration.py`]:
- the migration applier applies pending migrations in filename order;
- it refuses the assessment-pool migration (`20261022050000`) without a reserve script;
- a reserve script can't be empty and needs individually human-approved items.

So the seven `20261102*` migrations can't reach hosted until human review produces a reserve: account setup (CR-26),
parent emails, reminders, question reports, seen-before, home state and data requests. A fix is proposed to Research
(item P2).

## 1. What works today

Four separate levels, never merged into one.

| Level | What is true [Certain unless tagged] |
|---|---|
| **Implemented locally** | Everything below the Hosted line in §2: household accounts and invitations, guardian roles, four-screen setup, practice and weekly plan, reserved progress checks with server-assigned items, reminders and parent emails against fakes, Stripe against mocks, question intake and review tooling, the data-request procedure, college discovery and comparison, the planning pilot. `scripts/local/live_stack.sh test` (real SQL, RLS and RPCs; stub auth; fake push and mail) runs in CI on every merge. |
| **Merged into main** | All of the above, at `aeb45bbb73`. Web suite: 508 passed (71 skipped) on the #302 head; required CI green on main merges. 40 migrations are in the repo. |
| **Applied to hosted** | Only what was applied before the 2026-10-06 pause: **21 migrations, through `20261006120000`** (`docs/SUPABASE_PAUSE.md`; the manifest `supabase/migration_history.json` lists 20 and must be reconciled). **19 migrations are unapplied.** Five edge functions were deployed: billing-plans, billing-checkout, billing-portal, stripe-webhook, send-household-invitation. Reference data was loaded (5,920 institutions, 9,962 cost records). Canonical staging (Netlify) holds one upload from 2026-10-06 16:09 UTC with no commit recorded; it points at the paused project, so accounts can't work there. |
| **Tested successfully on hosted** | **Reference-data reconciliation only, 2026-10-02** (`docs/coverage/live-supabase.json`): the repository counts matched, anonymous write and ledger access were refused, the security advisor had 0 notices, and a repeat import changed nothing. No app journey, sign-up, invitation, practice, billing, reminder or email has a recorded hosted pass. `docs/acceptance/` doesn't exist. Whether anything else passed before the pause: pending reply (Research). |

**Hosted project state:** `.operations/supabase-live-hold.json` says `hold: true`, and the owner paused the project on
2026-10-06. This session's Supabase connection can't see the CollegePrep project, which is in a different
organization (`atkukjwwdvhnrxwdhqmb`), so its current pause state isn't confirmed from here.

## 2. Release status by area

**Statuses:** Complete · In progress · Blocked · Not required for initial release (the recommended reduced release,
§3).

| Area | Status | Local | Hosted | What's missing (owner) |
|---|---|---|---|---|
| Signup, login, student and guardian permissions, setup | **Blocked** | Implemented and tested locally; role rules tested against the server (#233, #243) | Invitation function deployed pre-pause; role rules, CR-26 setup unapplied; no hosted test | Hosted restore (Owner) → migrations (Research; P2 ordering) → email (Owner, A7) → real-account tests H3.1–3 (Owner runs, Design writes up) |
| College discovery, comparison, tuition, scholarships | **In progress** | Implemented | 2026-10-02 reference data loaded and reconciled; cost v2 and C3 components unapplied | Current-year data is thin: verified 2026-27 costs at 313 schools (416 records), verified 2026-27 awards at 60 schools (392 records); the rest is 2023-24 federal data, labelled as such. Design: the cost-period client fix Research flagged on #218 (never show a semester figure as annual) before any verified semester record ships. #296 (tuition batch 2) is a draft with conflicts; pending reply on whether it's needed for release |
| Degree-plan pilot and exam-credit mappings | **In progress** | Pilot page complete behind `VITE_PLANNING_PILOT` (#302): 12 verified UTC plans; notes shown with their rows; no credit from printed alternatives | Nothing | #191: UTC AP/CLEP tables print no academic year and stay partially verified, so no credit is placed (Research, owner policy). Truncated rows in 2 pilot plans (Deep Dive). Privacy rows (Owner + counsel). Mobile pass (Design). Hosted import and flag (held) |
| Question-bank import, review eligibility, practice | **Blocked** | Intake, packets, sign-off ledger, CR-21 serve-only-approved gate, CR-24 rights gate: all built and tested | Gates unapplied; no reviewed item exists | **A content lead and reviewers (Owner).** Counts below |
| Reserved progress checks | **Blocked** | Built and tested (#248, #279, #291; T1–T12) | Unapplied (pool and assignment migrations) | Human-approved reserve items (A2). ACT English and Reading can't be reserved as built (B6) |
| Reminders and parent emails | **Not required for initial release** (recommended) | Built; tested against fake push and mail | Unapplied; functions not deployed | Optional: CR-22/27 migrations, VAPID/FCM and Resend secrets, real-device R1–R7. Invitation and confirmation email is still required (A7) |
| Billing | **Not required for initial release** (if free; recommended) | Checkout, portal and webhooks tested with mocks | Billing tables and four functions deployed pre-pause; never tested end to end | If paid: Stripe setup (Owner, A8) and server enforcement of paid Prep (Research, A10, #108; today a free account can call paid RPCs directly) |
| Privacy, export, deletion | **Blocked** | Data-request procedure and runbook merged (#294, `20261102070000`); manual route by email | Unapplied | Privacy policy and terms approved (Owner + counsel, A3); runbook §0 decisions (A4); in-app links and age attestation (Design, A9, after A3) |
| Mobile usability | **In progress** | Demo runs at 390 px (setup; planning pilot earlier); no real-device pass | None | Design: a 390 px pass of the release flows on main; Owner: real iPhone/Android check during H3 |
| Migrations, deployment, end-to-end acceptance | **Blocked** | 40 migrations apply cleanly on the local stack in CI | 21 applied, 19 pending; hold on; staging stale | Restore (Owner) → H0 reconcile → H1 on a disposable copy, then hosted (Research) → staging deploy from main → H3 (Owner + Design) |

### Question bank: actual counts [Certain, from `PRACTICE_READINESS.md` and `BANK_INTAKE_2026-10-28.md` on main]

"Publication-eligible" means a current approval recorded as `human:` plus an allowed license (the CR-21 and CR-24
gates). "Usable" means a hosted student could be served it today.

| Exam / section | In app (demo / local) practice + reserve | Imported to hosted | Publication-eligible | Usable on hosted, practice / checks | Delivered drafts that pass the import contract (not imported; 0 approved) | Reservable by passage rule |
|---|---|---|---|---|---|---|
| ACT English | 10 (7 + 3) | pending reply | 0 | 0 / 0 | 691 | 0 (every item shares an essay) |
| ACT Math | 12 (8 + 4) | pending reply | 0 | 0 / 0 | 759 | 759 |
| ACT Reading | 8 (5 + 3) | pending reply | 0 | 0 / 0 | 686 | 0 (every item shares a passage) |
| ACT Science | 8 (5 + 3) | pending reply | 0 | 0 / 0 | **0** | 0 |
| SAT Reading and Writing | 10 (6 + 4) | pending reply | 0 | 0 / 0 | 695 | 695 |
| SAT Math | 10 (6 + 4) | pending reply | 0 | 0 / 0 | 1,000 | 1,000 |
| **Total** | **58 (37 + 21)** | — | **0** | **0 / 0** | **3,831** | — |

**Reconciling the saved banks:**
- **Delivered bank:** 5,843 drafts, on branch `qb/final-reconciled-bank-v2-2026-10-28` (`6b253cf3`, not on main).
  - 3,831 pass the import contract and were taken in as a local dry run.
  - 1,620 ChatGPT drafts lack required fields.
  - 392 are pending, held, duplicates or retired.
- **App bank:** the 58 items are AI-authored and AI-reviewed, with 0 human-approved. Under the rights gate a generated
  item needs a `human:` review, so they're unservable on hosted too.
- **Draft totals are not readiness.** None of the 3,831 counts until a human approves it.

**Launch minimum** (`QUESTION_BANK_RECOMMENDATION.md`): both exams at 8 weeks, ≈ 430 ACT and ≈ 410 SAT; or one exam
at 12 weeks, ≈ 470 with 25% planned review. **ACT can't launch on today's content** [Certain]: there are no ACT Science
drafts, and English and Reading can't supply check items (B6). **SAT can:** 1,695 contract-valid drafts, all on
single-question passages.

## 3. Exact finish line

**Recommended first release (reduced):** free, web only, **SAT only**, English only. These stay off:
- billing (`VITE_BILLING_ENABLED`);
- reminders (`VITE_PRACTICE_REMINDERS`);
- the weekly digest (`VITE_WEEKLY_DIGEST`);
- AI hints;
- the planning pilot (`VITE_PLANNING_PILOT`) until its gate passes;
- the full-length check (`FULL_FORM_READY = false`);
- native apps;
- score prediction.

**It offers:**
- household accounts with guardian roles and student invitations;
- setup and a weekly plan;
- SAT practice from human-approved items;
- starting and mini progress checks from a reviewed reserve;
- the in-app parent summary;
- college discovery and comparison, with data years labelled.

**Owner-tested pilot:** the owner and `qa-` accounts on canonical staging with real Auth and email.

### A. Blockers to an owner-tested pilot

| # | Blocker | Owner | PR / issue | Depends on | Pass condition |
|---|---|---|---|---|---|
| P1 | Restore the hosted project (`butlklkzafvklwasbynr`) | Owner | `SUPABASE_PAUSE.md` | Owner decision O1 | Project `ACTIVE_HEALTHY`; H0 passes: live history = manifest + `20261006120000`; every version to apply is absent live |
| P2 | Let the non-pool migrations apply before a reserve exists | Research | #218 comment 6617177874 | — | `20261102*` can be applied to a copy with no reserve, checks show "Not measured", and `local-backend` stays green. Alternatively Research shows that P5 will produce a reserve first |
| P3 | Apply migrations: copy first, then hosted (H1) | Research | `LAUNCH_CHECKLIST.md` H1 | P1, P2 | Every `supabase/tests/*.sql` passes on the copy; production history lists each version once; import reconciliation shows no differences |
| P4 | Email sending (A7) | Owner | A7 | P1 | Resend domain `mail.getcimiento.com` verified and `RESEND_API_KEY` set; H3.1: the confirmation email arrives and sign-in works only after confirming |
| P5 | A reviewed SAT pilot set | Owner (reviewer) → Design (packets, ledger) | A2, #254 | Owner decision O2 | At least one week of practice plus one starting check, approved per item with `human:` [Guessing on the size: ≈ 60 SAT items, about 48 practice + 8 reserve]; `recordEditorial.ts` ledger shows each approval |
| P6 | Load reviewed items to hosted, with the reserve | Research (import path) + Design (contract) | H2 | P3, P5 | The H2 per-section query shows the planned reserve; `assessment_pool.sql` and `assessment_assignment.sql` pass on the copy. How approved items reach hosted: pending reply (Research) |
| P7 | Deploy staging from main | Research or Design, Owner approves | `DEPLOYING.md` | P3, P6 | `verify_deploy.sh` reports the merge commit on canonical staging |
| P8 | Owner acceptance run | Owner runs, Design writes up | H3.1–3.5, `docs/acceptance/<date>.md` | P4, P6, P7 | Each H3 "Pass" line holds exactly, with evidence recorded |
| P9 | Planning pilot, if it's part of the pilot | Research (#191), Deep Dive (rows), Owner (O5) | `PILOT_ACCEPTANCE.md` §8 | P3 | Checklist items 4–7 done; flag on for staging only |
| P10 | Cost-period client fix | Design | #218 (Research, 2026-11-03 21:25) | — | No semester figure annualized anywhere; tests on each listed path |

### B. Additional blockers to public launch

| # | Blocker | Owner | PR / issue | Depends on | Pass condition |
|---|---|---|---|---|---|
| L1 | SAT bank at the launch minimum (A1) | Owner → Content | A1 | O2 | ≈ 470 SAT items human-approved, publication-eligible, spread across sections and difficulties; count query on hosted |
| L2 | Every published item human-reviewed (A2) | Content | A2 | O2 | 0 published items without a current `human:` approval |
| L3 | Privacy policy and terms approved (A3) | Owner + counsel | #165 | O3 | Signed-off text committed |
| L4 | In-app privacy, terms and age attestation (A9) | Design | A9 | L3 | Links in footer, sign-up, invitation acceptance and emails; component tests |
| L5 | Data-request runbook decisions (A4) | Owner + counsel | #294, `DATA_REQUESTS.md` §0 | L3 | §0 placeholders replaced; one export and one deletion run on a `qa-` household |
| L6 | Support and privacy inbox monitored (D3) | Owner | D3 | — | Monitored address published in the policy |
| L7 | Production deploy and flags (D1, H4) | Owner | D1 | P8, L1–L6 | Production build env shows exactly the flags whose steps passed |
| L8 | Real-device mobile pass | Owner + Design | — | P7 | Release flows on an iPhone and an Android phone, recorded |
| L9 | Only if paid: Stripe (A8) and server enforcement (A10) | Owner; Research → Design | #108 | P3 | H3.8 pass; a free account's direct calls to paid RPCs are refused in tests |

### C. Optional, after release

- **Reminders and parent emails** (R1–R7, H3.9).
- **ACT**, which needs:
  - ACT Science content;
  - whole-passage reserve sets (B6);
  - a passage key in the import contract.
- **The 1,620 ChatGPT drafts**, completed or held.
- **The full-length check.**
- **Native apps.**
- **Paid Prep.**
- **Planning pilot additions:** UTK and MTSU plans, and the plan-reader backlog (`DEEP_DIVE_CHECKPOINT.md`, `app-status`).
- **Broader research:** national program and tuition coverage.
- **Validated score prediction.**

## 4. Owner actions

**Necessary:**

| # | Decision or action | Recommendation |
|---|---|---|
| O1 | When and how to restore hosted. Today the Free plan's active slots are the limit | Restore now. If no Free slot is free, move CollegePrep's organization to a paid plan, which also allows a proper disposable copy for H1. [Likely ≈ $25/month for Pro; check current pricing] |
| O2 | Name the content lead and reviewers | For the pilot, review the ≈ 60-item SAT set yourself. For launch, name a qualified reviewer for ≈ 470 SAT items |
| O3 | Privacy policy, terms and data-request terms, with counsel | Adopt `docs/legal/DECISIONS.md`: 13+, parent attestation, manual deletion and export by email. Fill runbook §0 |
| O4 | First-release scope | Free, web, SAT only, with the flags in §3 off |
| O5 | Exam credit in the planning pilot | Keep UTC credit placement excluded. The page shows plans, costs and tables as "not yet verified", so #191 stops blocking the pilot. Approve UTK's tables moving to partially verified (#191 table, #218 C4) |
| O6 | Email: verify `mail.getcimiento.com` in Resend and set `RESEND_API_KEY` | Do it right after O1 |
| O7 | Run the acceptance accounts (H3) | Two browsers, `qa-` accounts |
| O8 | The abandoned-starting-check rule: no check for 28 days, then a mini (#279) | Accept for release; revisit with data |

**Optional:**
- the Stripe live setup and a live-charge go-ahead (only for a paid launch);
- VAPID/FCM keys and devices for reminders;
- B6 passage sets (only with ACT);
- dropping the two truncated UTC pilot plans if Deep Dive can't fix them quickly;
- the JHU Bachelor of Music record (Research; not release).

## 5. Next steps, in dependency order

**To the owner-tested pilot:**
1. Start in parallel:
   - O1 restore;
   - O6 email;
   - O2 review of a ≈ 60-item SAT set;
   - P2 (Research);
   - P10 and the mobile pass (Design).
2. Then, in order:
   - P3 migrations (copy, then hosted);
   - P6 reviewed items and reserve;
   - P7 staging;
   - P8 owner acceptance.

**To public launch:**
1. In parallel with the pilot:
   - L1/L2 review to ≈ 470 SAT items;
   - L3 legal → L4/L5;
   - L6.
2. After the pilot passes: L8, then L7 production with only the passed flags.

**Effort** (stated only where there's evidence):
- **Engineering left for the reduced release is small** [Likely]: P2, P6's import path, P10, A9 and the write-ups. The
  tooling for each step exists and is tested locally.
- **The long poles are owner-side and not estimable from the repository:**
  - when hosted is restored;
  - reviewer time for ≈ 470 SAT items through stages 3–8 (no throughput data yet);
  - counsel's turnaround.

  [Guessing] With a reviewer in place, review of the SAT launch set is likely weeks, not days.
