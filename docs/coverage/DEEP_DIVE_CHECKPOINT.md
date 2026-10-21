# Deep Dive checkpoint

This file is how a new Deep Dive session picks up shared reader work and requirement/roadmap depth without redoing finished work. It is updated with every Deep Dive PR. Research keeps its own file, `docs/coverage/RESEARCH_CHECKPOINT.md`.

- **Main at the last refresh:** `754fd330f9` (merge of #235).
- **Ownership on #153 (2026-10-21):**
  - Deep Dive owns the readers for UNL, Utah, SHSU, UWM and UCR, and the CourseLeaf plan-grid reader (`parse_grid`, #229).
  - Research owns Colorado State's program column, BYU emphases, Alabama's print-link label, the UTSA and UT Dallas lists, and the Roosevelt and SF State corrections.

## Numbers

Counted from `data/institutions/*` on main `754fd33`, verified records only. Program-list coverage is reported separately from requirement and roadmap depth.

| | main `46c7f81` (session start) | main `754fd33` |
|---|---|---|
| Verified bachelor's program records (all workstreams) | 10,145 | 10,648 |
| Verified term-by-term plans (`program_plan`) | 2,843 at 64 schools | 3,090 at 66 schools |
| Verified major requirement groups | 14,070 | 14,122 |
| Covered schools | 65 | 70 |

**Deep Dive gains in this session (merged).** Research's batches 5 and 6 added the rest; do not count these twice.

| PR | School | Records | Plans | Count |
|---|---|---|---|---|
| #225, #226 | UNL | 116 | 196 | 116/124, covered |
| #225, #235 | Utah | 101 | 0 (behind tabs) | 101/101, covered |
| #226 | UWM | 133 | 28 | 133/133, covered |
| #228 | SHSU | 124 | 0 | no list (script-only) |
| **Total** | | **474** | **224** | |

## Readers added or changed (each with tests and mutants)

| Reader | Where | What it reads |
|---|---|---|
| `degree_offered/v1` | `programs/extract.py` | CourseLeaf major pages with the award only in `Degree Offered:` (UNL). |
| `courseleaf_plantext/v1` | `programs/courseleaf.py` | UNL's table-less '4-Year Plans': terms, course and requirement rows, notes, milestone rows (kept as text), and the plan titles. |
| `kuali_award_line/v1` | `programs/extract.py` | Utah '<CODE> Program' pages, where the award is on the line after the heading. |
| `printed_catalog_years` | `programs/extract.py` | The 'Undergraduate Catalog' / '<year>' two-line header (SHSU), never inside an archive menu. |

## In progress (branch `programs/covered-plans`, not pushed yet)

- **`courseleaf_plan/v2`.** It fixes the v1 plan-grid defects in #229:
  - year and semester rows become their own terms;
  - more header-cell variants are read;
  - subtotals become `credit_hours`, and the printed total goes into `rule_text` with its label;
  - unknown label rows put a plan on hold;
  - a plan follows the program record read from the same page.
  - v2 is not trusted by autoreview.
- **Course Lists:**
  - `COUNT` no longer reads 'Select 6 hours' or 'Select 6 SCH' as a course count;
  - placeholder codes such as 'XXXX 1201' are not courses.
- **Plans waiting for review:** 376 new plan candidates for verified programs with no plan on file.
  - By school: Texas A&M 120, CU Boulder 71, JSU 69, West Chester 23, OSU 19, UNI 18, UT Austin 15, ODU 12, Temple 10, Oregon 5, TAMUK 5, UNO 3, SRU 3, Idaho 2, Clayton 1.
  - A mechanical check against the stored grids is clean except UNO's misspelled 'Third Semeseter' term (now held).
- **Next steps:**
  1. Regress over all 194 stored runs.
  2. Independent review.
  3. Promote the plans for programs with no plan on file. v1 plans already on file are never replaced without the owner's decision on #229.

## Next executable tasks

1. Finish `programs/covered-plans` (above) and open its PR.
2. **#229 (owner decision).** Replace the 1,806 defective v1 plans and the 71 hour-choice groups with reviewed re-extractions under correction entries. Do nothing until the owner approves.
3. **SHSU:**
   - requirement groups (262 candidates in TX/2026-10-21-d02) after the Course List fix and a fresh review;
   - plan grids (205 stored grid documents);
   - a count from the department pages.
   - The two Finance concentration records whose keys are cut at 80 characters stay held.
4. **UNL:** requirement groups by section heading (the pages also print the minor's tables); 8 unrecorded majors are queued with reasons.
5. **UWM:** 11 plans with 'Semester N' rows (now read by v2) need review; requirement groups (644 `catalog_program/v1`) need review.
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
