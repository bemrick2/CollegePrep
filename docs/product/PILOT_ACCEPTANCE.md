# College-planning pilot: acceptance package (Tennessee business, Slice 1)

Prepared by Design, 2026-11-03, on main `22040b8f26` plus the branch `design/plan-notes-or-rows`. It is one place
to accept or reject the pilot. Sections owned by Research and Deep Dive state today's facts and who must act.

**What acceptance would approve:** showing the pilot page (`/colleges/plan`, behind `VITE_PLANNING_PILOT`) to pilot
families. **What it doesn't:** any hosted import, migration or deploy (held), turning on deployed flags (off), or
release of the wider app. Deep Dive's completion is not release approval.

## 1. Scope

| School | Programs | Degree plans shown | Credit tables | Cost |
|---|---|---|---|---|
| UTC | 13 business programs | **12 verified eight-term plans** (Accounting; Business Analytics; Economics B.A.; Economics, Financial Economics; Economics, International Public Policy; Entrepreneurship; Finance, Business Finance; Finance, Investments; Management; Management, Healthcare Management; Marketing; Marketing, Professional Sales). No plan for HR. | AP, CLEP, IB, dual enrollment: all **partially verified** | 2026-27 cost of attendance, verified, by living arrangement |
| UTK | 9 B.S.B.A. majors (listing not verified) | none on file | AP, CLEP, IB, Cambridge, Statewide Dual Credit, industry: partially verified (academic year unconfirmed); dual enrollment verified | verified |
| MTSU | business majors | none on file | AP, CLEP, dual enrollment: partially verified | none on file |

## 2. Supported credit mappings

**Today: none.** The engine places exam credit only from a **verified** table, and none of the pilot's AP or CLEP
tables is verified. So no credit is placed into any plan, and no term coverage, time saved or money saved is shown.
Each table is named on the page as "Academic year unconfirmed" or "on file but not yet verified", and is never shown
as "no credit".

- **Owner: Research (#191).** Either verify UTC's AP and CLEP tables, or explicitly exclude the mappings that can't be
  supported. Whatever #191 decides, the engine already enforces two rules:
  - only verified rows are used;
  - an awarded course fills a plan row only when the row names that course in a reviewed structure: a course code,
    an option list, or `any_of` (section 4).
- **What changes once #191 verifies UTC's tables**, from the tested scenario in `web/scripts/roadmap.pilot.test.ts`:
  - **Microeconomics and Macroeconomics** fill their plan rows, 6 hours in all.
  - **English Language** is **partly** placed. ENGL 1020 fills its row. ENGL 1010 isn't placed, because Management
    names it only in "Elective (ENGL 1010 or 1011)*", which has a placement condition (section 3).
  - **Calculus AB and Statistics** are accepted but not in the plan; the page says the substitution isn't published.
  - **Coverage and savings:** no whole term is covered, so neither is shown.

## 3. Displayed placement conditions

A plan's printed notes are shown verbatim, under the row they qualify.
- **The page never shows a bare mark.** A row whose mark has no note on file says "The plan prints “*” here, but no
  note for it is on file."
- **Today's pilot plans have no such row:** all 12 verified UTC plans, 0 unexplained marks.

**The placement condition in 10 of the 12 UTC plans** (all except Economics B.A. and Economics, International
Public Policy), shown under "Elective (ENGL 1010 or 1011)*":

> **Note (\*):** If a student does not place into ENGL 1020 (30+ on ACT English or 670+ on SAT Read/Write), ENGL 1010
> or 1011 is required.
>
> As printed. Credit you bring isn’t matched to this row automatically.

- **The app doesn't apply the condition for the student.** It doesn't compare entered ACT or SAT scores with it, and
  doesn't decide which course the student will take. It shows the condition and leaves the row unfilled.
- **Below the plan,** "Printed with this plan" holds:
  - the source's own notice ("Please refer to the Undergraduate Catalog for further program requirements and course
    descriptions.");
  - any footnote no row cites;
  - the degree checklist, as printed (degree requirements and graduation requirements, e.g. "50% of Business Hours at
    UTC").

## 4. Unresolved "or" rows (regression-tested)

A row whose alternatives exist only in its printed wording is never filled automatically. Examples:
"MATH 1710 or MATH 1730", "Elective (ENGL 1010 or 1011)*", "INM 101or VOK 101", "ENGL 221/MODL 221",
"ART 3700 level or higher …".

| What is enforced | Where it is tested |
|---|---|
| No credit is placed into such a row, for any of the seven printed shapes on file | `web/src/lib/engine/unresolvedOrRows.test.ts` |
| An exam whose course appears only in such a row is reported as "Named among alternatives: not placed automatically", never "applies" and never "not a course this plan lists" | same file, and `planFormats.test.ts` |
| No requirement, whole term, coverage or applicable hours follow from it | same file |
| On UTC Management with every record verified: the row isn't filled, and coverage and savings are null. The control (the same courses as `any_of`) is filled and covers the term | `web/scripts/roadmap.pilot.test.ts` |
| The page shows the row as printed, with its note and the "isn’t matched automatically" line | `web/src/features/planning/CollegePlan.test.tsx` |

**Scale:**
- **Across all verified plans:** in 1,437 of the 3,100, 4,786 rows name courses only in printed alternatives. Before
  this change their wording was parsed into alternatives and could be filled. Now they're never filled, and they
  carry the "isn’t matched automatically" line.
- **Rows that name no course** ("Humanities and Fine Arts or Elective") were never fillable and carry no extra line.
- **In the 12 UTC pilot plans:** 14 labelled rows, including the 10 "Elective (ENGL 1010 or 1011)*" rows.

**Deep Dive's 54 held "or" plans stay held.** This protection is necessary for promoting them, but not sufficient:
plan-level promotion also needs confirmed completeness.

## 5. Known exclusions

- **Plans held, not shown** (Deep Dive): UTC Geology, Hydrogeology, Political Science and 4 plans with uncited
  course notes; the 54 "or" plans; 10 EOU/PDX plans downgraded in #297. None is in the pilot.
- **Data defect in a pilot plan** (Deep Dive): UTC Economics, International Public Policy stores Term 1's row as
  "Writing and Communication (ENGL 1010 or 101". The stored source evidence reads "…(ENGL 1010 or 1011)".
  - Effect: display only. The row is unresolved, so it's never filled, and its credits ("3-4") are as printed.
  - **Must be corrected, or the plan excluded, before acceptance.**
- **EOU page debris stored as course rows** (Deep Dive): EOU is not a pilot school, so the pilot page is unaffected.
  It stays documented cleanup unless Deep Dive finds it affects matching.
- **Not built for the pilot:** prerequisites, course availability and sequencing (so time and money saved are
  withheld); applying placement conditions automatically; Statewide Dual Credit and IB in the engine.
- **UTK and MTSU:** no business plans on file, so the page shows "No degree plan on file", plus their tables' status.

## 6. Final copy (pinned by tests)

| Where | Copy |
|---|---|
| Plan status, UTC Management today | "Partly on file" (plan verified; credit tables not) |
| A row's printed note | "Note (\<mark\>): \<note as printed\>" |
| A mark with no note on file | "The plan prints “\<mark\>” here, but no note for it is on file." |
| An unresolved "or" row | "As printed. Credit you bring isn’t matched to this row automatically." |
| Credit status for such a row | "Named among alternatives: not placed automatically" |
| What's missing, for such a row | "\<School\> awards \<course\> for \<exam\>. This major's plan names it only in a row printed with alternatives (“\<row\>”), so that credit isn't placed there automatically, and no term, coverage or saving counts it. The school decides how it applies." |
| Below the plan | "Printed with this plan"; "Degree checklist, as printed" |
| Unverified credit table | "Academic year unconfirmed" / "\<School\>'s AP credit table is on file but not yet verified: …" |

## 7. Privacy-policy changes for the pilot's fields (for owner and counsel, A3)

The pilot uses inputs the privacy draft (`docs/legal/PRIVACY_POLICY_DRAFT.md`) doesn't list yet:

| Field | Where it is kept today | Proposed policy row |
|---|---|---|
| AP, CLEP and other exams a student plans or has taken, with scores | On the device (`useExamPlan`). With `VITE_EXAM_PLAN` on, in `student_exam_plan` on our servers | "Exams the student plans or has taken (AP, CLEP and similar) and scores, entered by a parent or student, to check them against colleges' published credit tables." |
| Home state | In the browser (`pp-home-state`, CR-15) | "Home state, to show in-state or out-of-state prices." Listed under "Kept only in your browser" until CR-15 moves it. |
| Living arrangement (on campus, off campus, with family) | Not stored: chosen on the page each visit | Not personal data we keep; no row needed while it isn't stored. |

- **Existing rows that already cover the pilot:** grade and graduation year, academic interests, saved colleges.
- **New wording needed:** state that results compare against colleges' **published** tables and plans, and that the
  app doesn't decide placement or award credit.

## 8. Acceptance checklist

| # | Item | Owner | State |
|---|---|---|---|
| 1 | Plan notes and footnotes shown with their rows; no unexplained mark in a pilot plan | Design | done on this branch (tests above) |
| 2 | Unresolved "or" rows can't receive credit, coverage or savings | Design | done on this branch (tests above) |
| 3 | #297's pilot tests and fixture reviewed | Design | done (see the #218 note) |
| 4 | UTC AP/CLEP: verified, or unsupported mappings explicitly excluded (#191) | Research | open |
| 5 | UTC Economics, International Public Policy, Term 1 row corrected or plan excluded | Deep Dive | open |
| 6 | Privacy policy rows for the pilot's fields approved | Owner + counsel | open (section 7) |
| 7 | Pilot shown to families: hosted restore, import of the verified records, flag on | Owner → Research | held |
