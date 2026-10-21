# Deep Dive checkpoint

This file is how a new Deep Dive session picks up shared reader work and requirement/roadmap depth without redoing finished work. It is updated with every Deep Dive PR. Research keeps its own file, `docs/coverage/RESEARCH_CHECKPOINT.md`.

- **Main at the last refresh:** `e78d6c3471` (merge of #238); this PR (`programs/decimal-credits`) on top of it.
- **Ownership on #153 (2026-10-21):**
  - Deep Dive owns the readers for UNL, Utah, SHSU, UWM and UCR, and the CourseLeaf plan-grid reader (`parse_grid`, #229).
  - Research owns Colorado State's program column, BYU emphases, Alabama's print-link label, the UTSA and UT Dallas lists, and the Roosevelt and SF State corrections.

## Numbers

Counted from `data/institutions/*` on main `754fd33`, verified records only. Program-list coverage is reported separately from requirement and roadmap depth.

| | main `46c7f81` (session start) | main `754fd33` | main `e78d6c3` (#238) | with this PR |
|---|---|---|---|---|
| Verified bachelor's program records (all workstreams) | 10,145 | 10,648 | 10,648 | 10,648 |
| Verified term-by-term plans (`program_plan`) | 2,843 at 64 schools | 3,090 at 66 schools | 3,459 at 67 schools | 3,475 at 67 schools |
| Verified major requirement groups | 14,070 | 14,122 | 14,122 | 14,122 |
| Covered schools | 65 | 70 | 70 | 70 |

**Deep Dive gains in this session (merged).** Research's batches 5 and 6 added the rest; do not count these twice.

| PR | School | Records | Plans | Count |
|---|---|---|---|---|
| #225, #226 | UNL | 116 | 196 | 116/124, covered |
| #225, #235 | Utah | 101 | 0 (behind tabs) | 101/101, covered |
| #226 | UWM | 133 | 28 | 133/133, covered |
| #228 | SHSU | 124 | 0 | no list (script-only) |
| #238 | 15 schools (`courseleaf_plan/v2`) | 0 | 369 | |
| **Total merged** | | **474** | **593** | |
| this PR | West Chester 3, UWM 13 | 0 | 16 | |

## Readers added or changed (each with tests and mutants)

| Reader | Where | What it reads |
|---|---|---|
| `degree_offered/v1` | `programs/extract.py` | CourseLeaf major pages with the award only in `Degree Offered:` (UNL). |
| `courseleaf_plantext/v1` | `programs/courseleaf.py` | UNL's table-less '4-Year Plans': terms, course and requirement rows, notes, milestone rows (kept as text), and the plan titles. |
| `kuali_award_line/v1` | `programs/extract.py` | Utah '<CODE> Program' pages, where the award is on the line after the heading. |
| `printed_catalog_years` | `programs/extract.py` | The 'Undergraduate Catalog' / '<year>' two-line header (SHSU), never inside an archive menu. |

## Merged in #238 (`courseleaf_plan/v2`)

- v2 replaces v1 for every new plan (#229 has the v1 defects). It reads:
  - year and semester rows as their own terms;
  - header-cell variants;
  - subtotals as `credit_hours`;
  - the printed total, with its label, as `rule_text`;
  - 'Autumn' terms.
- It holds unknown label rows and unknown term headers.
- A course titled 'Total ...' stays a course.
- v2 is not trusted by autoreview, so every v2 plan needs a reviewed decision.
- Course Lists: hour/SCH/unit/SH/hrs/cr choices are credits, never course counts, and placeholder codes are not courses.
- 369 reviewed plans promoted.
- Held: 4 CU Boulder plans printed for one track or scenario: Classics, Geography (Physical), Leadership and APS.

## This PR (`programs/decimal-credits`)

- **Decimal course credits are kept as printed** ('1.5', '0.5', '1-1.5'), as strings, following the existing range convention.
  - Regression over all 8,427 stored grids: the only change is 6,760 decimal credits now kept, on 429 grids, mostly West Chester, EKU, Minnesota and CU.
  - No promoted plan changes.
- **Promoted 16 reviewed plans**, each checked cell by cell against its grid:
  - 3 West Chester B.M. plans: Instrumental, Jazz and Vocal Performance. These were held in #238 only for decimals.
  - 13 UWM plans (`Semester N` rows), for programs with no plan on file.
- **Held, UWM:**
  - Biochemistry BS: the grid fits only the General option.
  - Chemistry BA and BS: one shared grid; the Biochemical Option's changes are only in a footnote, and CHEM 582 is printed in both Year 4 terms.

## Next executable tasks

1. **Plan naming:** name a single grid's plan by its printed heading, so the 4 CU Boulder track plans can be reviewed. Also:
   - store two-part plan items with explicit code/title/credits fields: 'CODE | Title' with blank credits reads the same as 'Title | 3';
   - keep 'or' joins with a missing space ('INM 101or VOK 101') readable;
   - `CREDIT_CELL` in Course Lists still rejects decimals.
2. **#229 (owner decision).** Replace the 1,806 defective v1 plans and the 71 hour-choice groups with reviewed re-extractions under correction entries. Do nothing until the owner approves.
3. **SHSU:**
   - requirement groups (262 candidates in TX/2026-10-21-d02) after the Course List fix and a fresh review;
   - plan grids: SHSU is not CourseLeaf. Its grids print two semesters side by side, glue footnote digits onto 4-digit codes ('BIOL 24031' is BIOL 2403 with note 1), and misalign the subtotal row. A dedicated reader is needed; never split footnotes by guess;
   - a count from the department pages.
   - The two Finance concentration records whose keys are cut at 80 characters stay held.
4. **UNL:** requirement groups by section heading (the pages also print the minor's tables); 8 unrecorded majors are queued with reasons.
5. **UWM:** plans are done for every issue-free v2 grid in WI/2026-10-21-d01 (13 promoted, 3 held). 12 pages with several grids stay held (`multiple_plan_grids`). Requirement groups (644 `catalog_program/v1`) still need review.
6. **Utah:** plans and requirements sit behind tabs. A rendered fetch of the tab views is needed.
7. **UCR:** the PDF's two-column majors tables need layout positions. Never pair rows by guess.
8. **Design (#230):** plan notes, plan titles, and the year/semester term structure from v2.

## Blockers (recorded, not evaded)

- **Utah:** the tab views are not in the stored pages.
- **UMD:** 28 majors have no award on any official UMD page read so far. Awards are not inferred.
- **KU:** no single official program list was found.
- **JHU recount:** 17 department-page approvals are not reproduced since `71c0ad91bb`. The records stay on file. Research owns this.
- **UCR:** layout.

## How to resume

1. `git fetch origin`. Read this file, #153 and #229.
2. Fetch run branches: `git fetch origin '+refs/heads/program-run/*:refs/remotes/origin/program-run/*'`. Copy a run with `git archive`.
3. Before a reader change is promoted, extract the stored runs it can touch with main's code and with the branch's code. Nothing may be lost or changed, and every gain must be explained.
4. Review independently, then write the reviewed decision and promote. Then run:
   - `python3 scripts/retain_evidence.py --push`, then `--verify-store`, then `--check`
   - `update_coverage`, `programs status`, `research_priority`, `validate_data`, `review_provenance`
   - the database check, web `vitest`, unit tests and `scripts/program_mutation_check.py`
5. Open the PR, merge on green CI, and update this file in the same PR.

Hosted imports, migrations and deployments stay on hold while Supabase is paused.
