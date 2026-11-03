# Planning pilot: acceptance package (Slice 1, UTC Management)

One package for accepting the college-planning pilot (`COLLEGE_PLANNING_PILOT.md` §4, `PLANNING_ENGINE.md` flag gate). Each workstream fills its own section; the owner accepts the whole. Started by Deep Dive on 2026-11-03 from main `22040b8f26`.

**Holds.** This package does not lift anything:
- hosted imports, migrations and deploys stay held;
- `VITE_PLANNING_PILOT` stays off in every deployed environment;
- question generation stays paused.

| § | Item | Owner | State |
|---|---|---|---|
| 1 | Degree plans shown, and the conditions printed with them | Deep Dive | **Ready** (below) |
| 2 | Placement conditions displayed next to the rows they qualify | Design | Open: the page doesn't render notes yet |
| 3 | Supported credit mappings (UTC AP/CLEP) | Research (#191), with Design | Open: the tables are partially verified |
| 4 | Unresolved 'or' rows: no automatic credit, coverage or savings | Design (test), Deep Dive (data) | Open: the test isn't written yet |
| 5 | Known exclusions | All | Listed below; each owner confirms |
| 6 | Final copy | Design drafts, owner approves | Open |
| 7 | Privacy-policy changes for the new fields | Design/Research draft, owner approves | Open |
| 8 | Mobile pass, hosted hold, owner sign-off | Design / owner | Open |

## 1. Degree plans (Deep Dive): ready

The pilot fixture (`web/src/features/planning/pilotFixture.json`, rebuilt from `data/institutions`) holds 12 UTC business and economics plans. All 12 are `verified` as of #297 (main `6b81928934`). UTK and MTSU have no plan records in the fixture, and the page says so ("No degree plan on file").

Each UTC plan stores what its Clear Path PDF prints, verbatim:
- the term rows;
- the notice above the plan ("Please refer to the Undergraduate Catalog for further program requirements and course descriptions.");
- the footnotes, with their marks;
- the "Completed:" checklist (`degree_summary`).

An independent reviewer checked all of it (#297).

**Printed conditions on the pilot plans:**

| Plans | Mark | Printed text (verbatim) | Rows it qualifies |
|---|---|---|---|
| Management (Slice 1); Accounting; Business Analytics; Entrepreneurship; Finance: Business Finance; Finance: Investments; Management: Healthcare Management; Marketing; Marketing: Professional Sales; Economics: Financial Economics | `*` | "If a student does not place into ENGL 1020 (30+ on ACT English or 670+ on SAT Read/Write), ENGL 1010 or 1011 is required." | Term 1: "Elective (ENGL 1010 or 1011)*" |
| Economics, B.A. | `*` | "Foreign language sequence may satisfy up to 4 General Education courses, depending on language. Consult catalog for more detail." | Terms 1–4: "Foreign Language 1–4 (…)*" |
| Economics: International Public Policy, B.A. | `*` | "Foreign language sequence may satisfy up to 4 general education courses, depending on language. Consult catalog for more detail." | Term 1: "Foreign Language 1 (Humanities and Fine Arts)*", "Humanities and Fine Arts or Elective*" |
| Economics: International Public Policy, B.A. | `**` | "Consult with advisor about General Education Requirements" | Term 7: the "History of Economic Thought, PSPS 3052 …, or PSPS 3053 …**" row |
| Economics: International Public Policy, B.A. | `***` | "If 2000-level Program Electives are taken, additional 3000-4000 level General Electives must be completed" | Term 6: "Approved Program Elective (3000-4000 level)***" |

**What these conditions mean for the engine (for §2–§4):**
- **The ENGL row is conditional.** The engine reads "Elective (ENGL 1010 or 1011)" as fillable by ENGL 1010 or 1011 (`degreeCredit.ts`). The footnote makes the row apply only to a student who does not place into ENGL 1020. So exam credit shown against that row must carry the condition. The page must not say the row is "satisfied" for a student whose placement is unknown.
- **One 'or' row is in a verified pilot plan:** International Public Policy, term 7. Its alternatives are printed in one row, and the engine scans free-text rows for course codes ("A or B" is any one). It falls within §4's test.
- **Data the engine never uses:** the checklist (`degree_summary`) and the notice. They are for display only, and nothing is computed from them.

## 2. Placement conditions displayed (Design): open

- **Required:** each footnote is shown with the row that prints its mark, and `plan_notes` are shown with the plan. UTC Management's English placement condition must read as a condition, with no unexplained asterisk.
- **Data fields:**
  - `rule_details.footnotes`: `[{marker, text, cited?}]`;
  - `rule_details.plan_notes`: `[{text, location, scope}]`;
  - `rule_details.source_notice`;
  - `rule_details.degree_summary`.

  The same fields exist on CourseLeaf plans (#275/#286).
- **Review:** Deep Dive's edits to the pilot tests and fixture in #297.

## 3. Credit mappings (Research, #191, with Design): open

- **Today:** UTC's AP and CLEP tables are `partially_verified`; the page prints no academic year. So the pilot shows them as "Academic year unconfirmed" and places no credit.
- **Before acceptance**, one of these is needed:
  - #191 verifies the tables;
  - or the pilot explicitly excludes the unsupported mappings.

  Then list here every mapping the pilot will show: exam, score, UTC course, hours, and the plan row it fills.

## 4. Unresolved 'or' rows (Design test; Deep Dive data): open

- **Owner, 2026-11-03:**
  - A regression test must prove that unresolved 'or' rows can't receive automatic credit placement, and can't imply satisfied requirements, coverage or savings.
  - Showing the source wording alone doesn't count.
- **Deep Dive:** the 54 plans held only for 'or' strings stay held. Promoting them needs confirmed completeness plus that tested protection.

## 5. Known exclusions

| Exclusion | Why | Owner |
|---|---|---|
| UTK and MTSU plans | Not on file in the fixture | Deep Dive (expansion: `COLLEGE_PLANNING_PILOT.md` §4) |
| Time or money saved | No completion records (prerequisites, availability, sequencing, remaining requirements) | Product rule |
| UTC AP/CLEP credit placement | Tables partially verified (until §3) | Research |
| Dual-enrollment course equivalencies | None on file; policy only | Research |
| Comparison across schools, HS course advice, account storage | Out of Slice 1 | — |
| Plans held as partially verified (528 nationwide) | Not shown; the page says "on file but not yet verified" | Deep Dive |

## 6. Final copy (Design drafts, owner approves): open

The copy must cover:
- the plan view;
- the condition wording from §2;
- the credit wording from §3;
- the "What isn't on file yet" list.

## 7. Privacy-policy changes (Design/Research draft, owner approves): open

`docs/legal/PRIVACY_POLICY_DRAFT.md` covers:
- student name or nickname, graduation year and grade;
- exam plan, target score and goals;
- academic interests;
- billing reference.

**To confirm for the pilot's fields:**
- the major and school chosen on the plan page;
- home state (`set_household_home_state`, #295);
- planned exams and scores used for credit;
- whether any of these leave the browser.

The draft's line on browser-only data is marked "[[Verify before publishing]]".

## 8. Sign-off

- Mobile pass at 390 px (Design).
- Hosted hold lifted (owner).
- Owner review of the whole package.
