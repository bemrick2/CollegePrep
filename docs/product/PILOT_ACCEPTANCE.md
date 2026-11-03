# College-planning pilot: acceptance package (Tennessee business, Slice 1)

One place to accept or reject the pilot (`COLLEGE_PLANNING_PILOT.md` §4, `PLANNING_ENGINE.md` flag gate). Started by
Deep Dive on 2026-11-03 from main `22040b8f26` (#300); merged with Design's package from `design/plan-notes-or-rows`
(#302). Each owner keeps its own section current; the owner accepts the whole.

**What acceptance would approve:** showing the pilot page (`/colleges/plan`, behind `VITE_PLANNING_PILOT`) to pilot
families. **What it doesn't:** any hosted import, migration or deploy (held), turning on deployed flags (off), or
release of the wider app. Deep Dive's completion is not release approval.

## 1. Scope

| School | Programs | Degree plans shown | Credit tables | Cost |
|---|---|---|---|---|
| UTC | 13 business programs | **12 verified eight-term plans** (Accounting; Business Analytics; Economics B.A.; Economics, Financial Economics; Economics, International Public Policy; Entrepreneurship; Finance, Business Finance; Finance, Investments; Management; Management, Healthcare Management; Marketing; Marketing, Professional Sales). No plan for HR. | AP, CLEP, IB, dual enrollment: all **partially verified** | 2026-27 cost of attendance, verified, by living arrangement |
| UTK | 9 B.S.B.A. majors (listing not verified) | none on file | AP, CLEP, IB, Cambridge, Statewide Dual Credit, industry: partially verified (academic year unconfirmed); dual enrollment verified | verified |
| MTSU | business majors | none on file | AP, CLEP, dual enrollment: partially verified | none on file |

### Degree plans (Deep Dive): ready

The pilot fixture (`web/src/features/planning/pilotFixture.json`, rebuilt from `data/institutions`) holds the 12 UTC
plans, all `verified` as of #297 (main `6b81928934`). Each stores what its Clear Path PDF prints, verbatim: the term
rows; the notice above the plan; the footnotes, with their marks; and the "Completed:" checklist (`degree_summary`).
An independent reviewer checked all of it (#297). Two plans have truncated rows to fix (section 5).

**Printed conditions on the pilot plans** (each now shown under the row that prints its mark, section 3):

| Plans | Mark | Printed text (verbatim) | Rows it qualifies |
|---|---|---|---|
| Management; Accounting; Business Analytics; Entrepreneurship; Finance: Business Finance; Finance: Investments; Management: Healthcare Management; Marketing; Marketing: Professional Sales; Economics: Financial Economics | `*` | "If a student does not place into ENGL 1020 (30+ on ACT English or 670+ on SAT Read/Write), ENGL 1010 or 1011 is required." | Term 1: "Elective (ENGL 1010 or 1011)*" |
| Economics, B.A. | `*` | "Foreign language sequence may satisfy up to 4 General Education courses, depending on language. Consult catalog for more detail." | Terms 1–4: "Foreign Language 1–4 (…)*" |
| Economics: International Public Policy, B.A. | `*` | "Foreign language sequence may satisfy up to 4 general education courses, depending on language. Consult catalog for more detail." | Term 1: "Foreign Language 1 (Humanities and Fine Arts)*", "Humanities and Fine Arts or Elective*" |
| Economics: International Public Policy, B.A. | `**` | "Consult with advisor about General Education Requirements" | Term 7: the "History of Economic Thought, PSPS 3052 …, or PSPS 3053 …**" row |
| Economics: International Public Policy, B.A. | `***` | "If 2000-level Program Electives are taken, additional 3000-4000 level General Electives must be completed" | Term 6: "Approved Program Elective (3000-4000 level)***" |

The checklist and the notice are display only; nothing is computed from them.

## 2. Supported credit mappings

**Today: none.** The engine places exam credit only from a **verified** table, and none of the pilot's AP or CLEP
tables is verified. So no credit is placed into any plan, and no term coverage, time saved or money saved is shown.
Each table is named on the page as "Academic year unconfirmed" or "on file but not yet verified", and is never shown
as "no credit".

- **Owner: Research (#191).** Either verify UTC's AP and CLEP tables, or explicitly exclude the mappings that can't be
  supported. Whatever #191 decides, the engine already enforces two rules:
  - only verified rows are used;
  - an awarded course fills a plan row only from the row's own course code, a choice option's own code, `any_of`, or
    free text that is exactly one course or a plain combination ("BIOL 1113& BIOL 1111"; every course required).
    Anything else printed in wording never fills a row: "A or B", "A/B", comma lists, a code qualified by an exclusion,
    note or level ("excluding MUS 156", "COMM 400-Level"), alternatives printed in a course's title ("MATH 1130
    College Algebra, MATH 1830: …, or MATH 1950: …"), and choice options printed that way (section 4).
- **What changes once #191 verifies UTC's tables**, from the tested scenario in `web/scripts/roadmap.pilot.test.ts`:
  - **Microeconomics and Macroeconomics** fill their plan rows, 6 hours in all.
  - **English Language** is **partly** placed. ENGL 1020 fills its row. ENGL 1010 isn't placed, because Management
    names it only in "Elective (ENGL 1010 or 1011)*", which has a placement condition (section 3).
  - **Calculus AB and Statistics** are accepted but not in Management's plan; the page says the substitution isn't
    published.
  - **Other pilot plans differ.** In Economics B.A., UTC awards MATH 1950 for Calculus AB, and the plan prints MATH 1950
    only as an alternative in its MATH 1130 row's title. That credit is reported as "Named among alternatives: not
    placed automatically" and counts toward no row, term, coverage or saving (tested in `roadmap.pilot.test.ts`).
  - **Coverage and savings:** no whole term is covered, so neither is shown.

## 3. Displayed placement conditions

A plan's printed notes are shown verbatim, under the row they qualify. A mark with no note on file is said to be
one: "The plan prints “*” here, but no note for it is on file."
- **Pilot plans:** all 12 verified UTC plans cite every mark they print; 0 unexplained marks, 0 bare marks.
- **Elsewhere (not in the pilot):** across 3,099 verified plans, 1 row has an unexplained mark. In plans that print no
  footnotes at all, symbols aren't read as marks, so a few rows still show a symbol as printed with no note (8 found by
  a narrow scan; the 2026-11-03 review's broader count, before the spaced-mark fix, was 176 rows in 15 plans). Not a
  pilot blocker; on the reader backlog.

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

## 4. Unresolved "or" rows and other printed alternatives (regression-tested)

Courses that exist only in a row's printed wording are never filled automatically. Three places they occur:
- **Free-text rows:** "MATH 1710 or MATH 1730", "Elective (ENGL 1010 or 1011)*", "INM 101or VOK 101",
  "ENGL 221/MODL 221", "ART 3700 level or higher …", and comma lists with no "or" ("two courses from: CHEM 3353,
  CHEM 3363, and CHEM 4333"), and a code qualified by an exclusion, note or level ("Select any ensemble, excluding
  MUS 156", "Human Behavior (May not use COMM 200S)", "COMM 400-Level"). Only a single code, or a plain combination
  ("BIOL 1113& BIOL 1111"), is read from free text; a combination counts only when every course is awarded.
- **Alternatives printed in a course's title** (UTC Clear Path): "MATH 1130 College Algebra or MATH 1830: …". Only
  the row's own code (MATH 1130) fills it; the page adds "Credit for MATH 1830, printed here as an alternative, isn’t
  matched to this row automatically." Excluded courses ("or higher, excluding MS 204", "except 1493") are never read
  as alternatives.
- **Free-text choice options:** the same rule applies to each option. "ENGL 103 or ENGL 104" is never completed; an
  option with its own code, stored as `any_of`, or printed as one course or a plain combination, is.

| What is enforced | Where it is tested |
|---|---|
| No credit is placed into such a row, for each of the thirteen printed free-text shapes on file | `web/src/lib/engine/unresolvedOrRows.test.ts` |
| A coded row's title alternatives, and free-text choice options, are never filled; the row's own code and coded options are (controls) | same file; `planFormats.test.ts`; `storedPlans.test.ts` (UTC General Biology) |
| An exam whose course appears only in such a row is reported as "Named among alternatives: not placed automatically", never "applies" and never "not a course this plan lists" | same file, and `planFormats.test.ts` |
| No requirement, whole term, coverage or applicable hours follow from it | same file |
| On UTC Management with every record verified: the row isn't filled, and coverage and savings are null. The control (the same courses as `any_of`) is filled and covers the term | `web/scripts/roadmap.pilot.test.ts` |
| On UTC Economics B.A. with every record verified: AP Calculus AB (MATH 1950, a title alternative) isn't placed and covers nothing; CLEP College Algebra (MATH 1130, the row's own code) is placed | same file |
| The page shows the row as printed, with its note and the "isn’t matched automatically" line; a course row names its printed alternatives | `web/src/features/planning/CollegePlan.test.tsx` |

**Scale (2026-11-03 scan of 3,099 verified plans):**
- **Free-text rows that name courses:** 5,439 rows in the plans of 1,336 programs. Before this change their wording
  was parsed into alternatives and could be filled; now they're never filled and carry the "isn’t matched
  automatically" line. The count is an upper bound: it includes cross-listings ("CHEM 3210/3210L") and a few
  mis-read codes, which are left unfilled (the safe direction).
- **Course and choice rows with printed alternatives:** 306 rows in the plans of 207 programs.
- **Rows that name no course** ("Humanities and Fine Arts or Elective") were never fillable and carry no extra line.
- **In the 12 UTC pilot plans:** 14 labelled free-text rows (including the 10 "Elective (ENGL 1010 or 1011)*" rows)
  and 30 course rows with printed alternatives.

**Deep Dive's held "or" plans stay held** (54 by Deep Dive's count in #218; not separately sourced in the repo). This protection is necessary for promoting them, but not sufficient:
plan-level promotion also needs confirmed completeness.

## 5. Known exclusions

- **Plans held, not shown** (Deep Dive): UTC Geology, Hydrogeology, Political Science and 4 plans with uncited
  course notes; the held "or" plans; 10 EOU/PDX plans downgraded in #297. None is in the pilot.
- **Truncated rows in two pilot plans** (Deep Dive): rows cut off mid-word or missing their closing parenthesis.
  - UTC Economics, International Public Policy: "Writing and Communication (ENGL 1010 or 101", "Natural Science
    without La", "ENGL 1020:Rhetoric and Composition 2 (Writing and Communication", the Microeconomics, Macroeconomics
    and Comparative Government titles, and the "Approved … Elective (3000-4000 level" rows.
  - UTC Entrepreneurship: "Natural Science without La", "ENGL 1020:Rhetoric and Composition 2 (Writing and
    Communication", the Microeconomics, Macroeconomics and Public Speaking titles, and "Approved Program Elective
    (3000-4000 Level".
  - Evidence: the repo's evidence entry for the IPP plan holds only term summaries, and its page file isn't in the
    repo, so the full wording can't be checked from the repo. (The wording "…(ENGL 1010 or 1011)" appears in the
    evidence for a different UTC plan, CS Data Science & AI; an earlier draft of this package misattributed it.)
  - Effect on matching: none found. The truncated free-text rows either name no course or name a single course
    (ENGL 1020) that is filled correctly; "(ENGL 1010 or 101" is unresolved and never filled. The defect is in what
    families read.
  - **Each must be corrected from the source page, or the plan excluded, before acceptance.**
- **EOU page debris stored as course rows** (Deep Dive): EOU is not a pilot school, so the pilot page is unaffected.
  It stays documented cleanup unless Deep Dive finds it affects matching.
- **Plans held as partially verified nationwide** (528, Deep Dive): not shown; the page says "on file but not yet
  verified".
- **Dual-enrollment course equivalencies** (Research): none on file; policy only.
- **Out of Slice 1:** comparison across schools, high-school course advice, account storage of plan choices.
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
| A course row with printed alternatives | "Credit for \<courses\>, printed here as an alternative (or alternatives), isn’t matched to this row automatically." |
| Credit status for such a row | "Named among alternatives: not placed automatically" |
| What's missing, for such a row | "\<School\> awards \<course\> for \<exam\>. This major's plan names it only in a row printed with alternatives (“\<row\>”), so that credit isn't placed there automatically, and no term, coverage or saving counts it. The school decides how it applies." |
| Below the plan | "Printed with this plan"; "Degree checklist, as printed" |
| Unverified credit table | "Academic year unconfirmed" / "\<School\>'s AP credit table is on file but not yet verified: …" |

## 7. Privacy-policy changes for the pilot's fields (for owner and counsel, A3)

The pilot uses inputs the privacy draft (`docs/legal/PRIVACY_POLICY_DRAFT.md`) doesn't list yet:

| Field | Where it is kept today | Proposed policy row |
|---|---|---|
| AP, CLEP and other exams a student plans or has taken, with scores | On the device (`useExamPlan`). With `VITE_EXAM_PLAN` on, in `student_exam_plan` on our servers | "Exams the student plans or has taken (AP, CLEP and similar) and scores, entered by a parent or student, to check them against colleges' published credit tables." |
| Home state | Today in the browser (`pp-home-state`). #295 (CR-15) adds `households.home_state` / `students.home_state`, written by `set_household_home_state`; not live while the hosted hold stands | "Home state, entered by a parent or guardian, to show in-state or out-of-state published prices. It is your answer, not a residency determination." Under "Kept only in your browser" until the client uses CR-15; then under account data. |
| Living arrangement (on campus, off campus, with family) | Not stored: chosen on the page each visit | Not personal data we keep; no row needed while it isn't stored. |
| School and major chosen on the plan page | Not stored: page state only | No row needed while it isn't stored. |

- **Existing rows that already cover the pilot:** grade and graduation year, academic interests, saved colleges.
- **New wording needed:** state that results compare against colleges' **published** tables and plans, and that the
  app doesn't decide placement or award credit.

## 8. Acceptance checklist

| # | Item | Owner | State |
|---|---|---|---|
| 1 | Plan notes and footnotes shown with their rows; no unexplained mark in a pilot plan | Design | done on this branch (tests above) |
| 2 | Courses that appear only in printed wording (free-text rows, title alternatives, free-text options) can't receive credit, coverage or savings | Design | done on this branch (tests above) |
| 3 | #297's pilot tests and fixture reviewed | Design | done (see the #218 note) |
| 4 | UTC AP/CLEP: verified, or unsupported mappings explicitly excluded (#191) | Research | open |
| 5 | Truncated rows in UTC Economics, International Public Policy and UTC Entrepreneurship corrected, or those plans excluded | Deep Dive | open |
| 6 | Privacy policy rows for the pilot's fields approved | Owner + counsel | open (section 7) |
| 7 | Mobile pass at 390 px | Design | open |
| 8 | Pilot shown to families: hosted restore, import of the verified records, flag on, owner sign-off | Owner → Research | held |
