# Personalized college planning: Phase 1 audit and Tennessee pilot plan

Written 2026-10-08. Tracking issue: #198. Hosted Supabase is paused and hosted deployment is held
(`.operations/supabase-live-hold.json`). Nothing in this plan applies a migration, imports data, deploys a function,
or changes an env flag until the owner lifts the hold.

Every finding below comes from the repository as of `846222eec`, which means the code, `supabase/migrations` and
`data/`. Hosted state was not inspected because it's paused, so anything said about "live" describes what the code
does once hosted is back, not what is serving today.

## 1. What exists (audit)

Status key:
- **Working:** in the code, tested, and serves verified records.
- **Partial:** works for part of the area.
- **Demo:** browser-only or fixture-only.
- **Missing:** nothing exists.

| Area | Status | What exists | What doesn't |
|---|---|---|---|
| **Student academic profile** | Partial | <ul><li>`students`: graduation year, grade, time zone.</li><li>`student_planning_preferences`: test, target, goals.</li><li>`student_test_scores`.</li><li>`student_academic_interests` (CR-13): live and tested.</li><li>Setup fields (CR-26): reference SQL only.</li></ul> | <ul><li>High school courses, dual enrollment taken or planned, GPA band.</li><li>Home state: CR-15, kept in the browser.</li><li>The exam plan: the CR-10 table is in migration `20261006180300`, but the frontend still keeps it on the device (`useExamPlan.ts`).</li></ul> |
| **High school academic planning** | Missing | None. | <ul><li>No TN graduation-requirement data.</li><li>No admission course-requirement data.</li><li>No course-recommendation code.</li></ul> |
| **College and major comparison** | Working (verified records only) | `Compare`, `CollegeDetail`, `ExploreMajors` and `programFit.ts` (offered, by CIP or name; "not listed" ≠ "not offered"). | <ul><li>Live needs hosted.</li><li>The demo snapshot has UTK plus IPEDS baseline schools only: **no UTC or MTSU**.</li><li>Admission type and internal transfer (CR-14) are shown as unverified questions.</li></ul> |
| **AP / CLEP / dual-enrollment equivalencies** | Partial | <ul><li>`examCredit.ts` matches AP and CLEP against each school's published table, by normalized name (CR-10 keys exist in schema, not used yet).</li><li>`CollegePaths` shows the results.</li><li>`costLevers.ts` lists dual-enrollment policy as a lever.</li></ul> | <ul><li>IB and Statewide Dual Credit tables exist in data but the engine ignores them (#197).</li><li>No dual-enrollment course equivalencies anywhere.</li></ul> |
| **Degree requirements and prerequisites** | Partial | <ul><li>`degreeCredit.ts` checks three things separately: is the credit accepted; does the awarded course appear in the major's verified term plan; does it cover a whole term.</li><li>`planItems.ts` (#171) reads every stored plan format.</li></ul> | <ul><li>**Prerequisites: missing**, in both data and code.</li><li>Gen-ed category matching: designations exist only as note text.</li><li>Alternatives printed inside a course title are missed (#192).</li></ul> |
| **Tuition, housing, scholarships, aid** | Working, partial | <ul><li>`cost_projection` v2 (server, plus a demo copy).</li><li>`residency.ts` for in-state vs out-of-state.</li><li>`merit.ts`: single published test minimums only.</li><li>`costLevers.ts`.</li><li>Federal and state aid tables.</li><li>Family-entered aid in Savings.</li></ul> | <ul><li>Living-arrangement costs are stored (UTK, UTC) but not shown.</li><li>Tuition billing basis (CR-17), loan terms (CR-18) and COA period (CR-20) are open.</li><li>Award tiers and ranges show as "read the criteria".</li></ul> |
| **Personalized recommendations** | Partial | <ul><li>`actions.ts` (parent actions), `planSummary.ts` (one headline opportunity) and `costLevers.ts`.</li><li>All score- and cost-oriented.</li></ul> | No recommendation of which exams, courses or dual-enrollment classes to take for a target major. |
| **Graduation timeline and savings** | Partial | `termsSaving` / `potentialSaving`: a potential saving only when whole plan terms are covered, net of grants lost. | <ul><li>No timeline model.</li><li>Hours short of a whole term are shown but never turned into dollars (correct until CR-17).</li></ul> |

## 2. Pilot data: what the three schools have

Counts come from `data/institutions/{utk,utc,mtsu}`. The app shows `verified` records only (`compare_institutions`,
`costProjection.ts`), so verification status decides what a student would see.

| | **UTC** | **UTK** | **MTSU** |
|---|---|---|---|
| **Business programs listed** | 13 (accounting, analytics, economics ×3, entrepreneurship, finance ×2, HR, management ×2, marketing ×2) | 9 B.S.B.A. majors | at least 5 B.B.A. |
| **Business degree plans** | **12 eight-term plans, verified** (no HR plan) | **None** (1 plan stored, for computer science) | **None** |
| **AP / CLEP tables** | 57 / 36 rows, **partially verified**: the page prints no year | 60 / 19, **verified**; **hours missing on every row** | 32 / 19, **partially verified** |
| **IB / other tables** | IB 25, partially verified | IB 33, Cambridge 57, Statewide Dual Credit 14, all verified | None |
| **Dual enrollment** | Policy only: grades 11–12, 3.0 GPA, state grant accepted. 0 course equivalencies | Policy only: points to the Banner tool | Policy only: 3.0 GPA or 22 ACT; $206.85 per credit hour |
| **Cost of attendance 2026-27** | Stored with living arrangements, **partially verified**: read via a summary, not the raw PDF | Verified, with living arrangements | **None** |
| **Merit awards** | 4, **partially verified** (same reason) | 23, mostly verified | **None** |
| **State aid** | HOPE, Aspire, GAMS, TSAA: all partially verified. **No Dual Enrollment Grant record** | (same) | (same) |
| **TN Transfer Pathways** | `state_policies` table exists; **no TN rows** | | |

**What a student would see at UTC today:**
- **Verified, and would show:** the Management plan.
- **Partially verified, so hidden:** exam credit and cost.

### Credit check: the existing engine on the pilot persona

I ran the current engine (`examCredit` → `degreeCredit`) on a fictional student with these planned scores:

| Exam | Score |
|---|---|
| AP Microeconomics | 3 |
| AP Macroeconomics | 3 |
| AP English Language | 4 |
| AP Calculus AB | 3 |
| AP Statistics | 3 |
| CLEP College Algebra | 55 |

It used the stored UTC Management plan. The engine treats UTC's tables as if verified, for illustration only.

**Accepted and applies to the plan, 15 of 22 hours:**

| Credit | Plan row it fills |
|---|---|
| ECON 1020 | term 3 |
| ECON 1010 | term 4 |
| ENGL 1010 | term 1 elective row |
| ENGL 1020 | term 2 |
| MATH 1130 | term 1 |

**Accepted, not in plan:**
- **AP Calculus AB → MATH 1950:** the plan's math row is "MATH 1130 or MATH 1830".
- **AP Statistics → MATH 2100:** the plan lists DATA 2130.

Whether UTC lets these substitute isn't published in our data. The engine correctly reports them as not applying, never as applying (#191).

**Terms fully covered: 0.** So the honest output has no graduation-timeline claim and no dollar saving. It shows 15 hours that fill named plan rows.

The engine already behaves correctly on this case.

**UTK:** the same exams match, but hours are null on every row and there's no business plan. Acceptance can be shown; applicability and hours can't.

**Data defects found:**
- UTC `entrepreneurship-b-s-b-a` has truncated rows ("Individual and Global Citizenshi").
- UTC prints alternatives inside titles; the reader misses them (#192).
- UTK and UTC disagree on whether an unlabeled-year page can be `verified`. This needs a Research decision (#191).

Two time-basis issues apply to every value:
- **Catalog year:** a 9th grader in fall 2026 would enter college around fall 2030, but every requirement is the 2026-27 catalog.
- **Prices and awards:** every price and award is the 2026-27 or 2027-28 published figure.

So the pilot labels each value with the year it was published. It never projects one forward or calls it the student's own figure.

## 3. Gap analysis

### Functionality

| Gap | Size | Needs the database? |
|---|---|---|
| A roadmap that composes credit, plan coverage and cost into one per-school answer with evidence on each line | Medium | No: pure engine over existing record shapes (#194) |
| Alternatives printed inside plan titles | Small | No (#192) |
| IB and Statewide Dual Credit matching | Small | No (#197) |
| Living-arrangement cost display | Small | No (records already carry it) |
| Student-and-parent plan view | Medium | No for demo; yes for saving inputs to an account (#195, #196) |
| Storing high school courses, dual enrollment and GPA band | Medium | **Yes**: CR-28 proposal; waits for hosted and the privacy policy (#196) |
| Wiring the CR-10 exam plan to the account | Small | **Yes**: the migration exists, hosted state unknown (#196) |
| Prerequisite chains | Large | Data first; no source data exists |
| High school course recommendations | Large | Data first: TN requirements are not stored (#193) |
| Timeline beyond whole-term removal | Medium | Needs CR-17 billing basis and course-level hours |

### Institutional data (Research)

| Data | Status |
|---|---|
| **Slice 1 (UTC Management)** | Verify the existing tables, cost and awards; answer the two substitution questions (#191). |
| **Slices 2–3** | UTK business plans and row hours; MTSU plans, cost and awards; dual-enrollment course equivalencies; the Dual Enrollment Grant; TN Transfer Pathways; TN high school requirements (#193). |

## 4. MVP pilot definition

**Slice 1:** one student, one school, one major. The pilot is the persona above at **UTC, Management (B.S.B.A.)**:
- The persona is a fictional Tennessee 9th grader, class of 2030, interested in business.
- UTC was chosen because it is the only pilot school with verified business degree plans and a living-arrangement cost record.
- Management was chosen over Accounting because it has a gen-ed hours record and is the broadest fit for "interested in business".

**What the student and parent see:**
1. Their inputs: grade, graduation year, home state, interest, planned exams.
2. For each planned exam:
   - UTC's published course, minimum score and hours;
   - whether that course **applies to the Management plan**, and which term it fills;
   - otherwise **accepted, fit unknown**, or **elective only**.
3. Dual-enrollment eligibility as UTC publishes it. No course equivalencies until Research has them.
4. Plan coverage:
   - the hours that apply;
   - the terms fully covered;
   - a graduation-timeline statement only when a whole term is covered.
5. UTC's published 2026-27 cost of attendance by living arrangement, labeled as 2026-27. A potential saving only per the shared whole-term rule.
6. "What we don't know yet", generated from the missing items, e.g. "UTC doesn't publish whether MATH 1950 substitutes for MATH 1830 in this plan".

**Out of slice 1:**
- High school course recommendations, prerequisites and award-stacking.
- Any comparison across schools.
- Account storage.

**Exit criteria (before the flag can be on anywhere outside local demo):**
- Every value shown traces to a `verified` record. Tests assert each line against the stored file.
- #191 P0 items are resolved.
- Owner review of the copy.
- Mobile pass.
- The hosted hold is lifted.
- Privacy policy covers any new field.

**Expansion order:**
1. UTK, same major (needs #193 plans and hours).
2. MTSU.
3. Dual-enrollment course equivalencies.
4. A three-school comparison.
5. Then other business majors at UTC. Their plans already exist, so they're cheap once slice 1 works.

## 5. Technical plan

- **Engine:** `web/src/lib/engine/planning/roadmap.ts` composes existing pure modules.
  - It reuses `examCredit`, `degreeCredit`, `planItems`, `costProjection`, `residency` and `merit`.
  - It doesn't add a second copy of any rule.
  - Each output line carries `source_url`, `verification_status`, `last_verified_at` and the published year, plus a state: `verified`, `estimate` (with method) or `missing` (with what's missing).
- **Data in demo:** a pilot fixture generated from `data/institutions/utc`, used in tests.
  - DemoSource serves it only after #191, and only under the flag.
  - Nothing is promoted or imported by this work.
- **UI:** `web/src/features/planning/`, behind `VITE_PLANNING_PILOT` (default off, unset in every deployed env).
  - It reuses the CollegePaths and Savings components.
  - No change to practice, progress, reminders or onboarding.
- **Account storage (later):**
  - CR-28: `student_hs_courses`, plus the CR-15 home state and an optional GPA band.
  - It uses the existing `can_view_student` / `can_edit_student_plans` permission model.
  - Reference SQL goes in `scripts/local/proposals/` with local tests. Research owns the migration.
  - It's applied only after hosted reconciliation (A5).
- **Isolation:** the pilot is separate code, behind a separate flag, with no launch dependency.
  - Launch checklist items A and B don't wait on it.
  - It doesn't wait on them, except for the hosted hold and the privacy policy.

## 6. Work items

| # | Item | Owner | Database? |
|---|---|---|---|
| #191 | Slice 1 data: verify UTC credit tables, cost, awards; substitution questions; plan text defects | Research | Files only |
| #192 | Plan reader: alternatives printed inside titles | Design | No |
| #194 | Roadmap engine and UTC Management fixture | Design | No |
| #197 | IB and Statewide Dual Credit matching | Design | No |
| #195 | College-plan view behind `VITE_PLANNING_PILOT` | Design | No (demo) |
| #193 | Slices 2–3 data: UTK, MTSU, dual enrollment, TN pathways, TN high school requirements | Research | Files only |
| #196 | CR-28 planning profile proposal; CR-10 wiring | Research + Design | **Yes: waits for hosted** |
