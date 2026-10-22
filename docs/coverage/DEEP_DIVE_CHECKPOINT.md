# Deep Dive checkpoint

This file is how a new Deep Dive session picks up degree-requirement, roadmap and specialised-reader work without redoing finished work. It is updated with every Deep Dive PR. Research keeps its own file, `docs/coverage/RESEARCH_CHECKPOINT.md`.

- **Main at the last refresh:** `b2c83c42d2` (merge of #261). This PR (`programs/plan-choices`) is on top of it.
- **Owner's split (2026-10-22):** Research does nationwide school-level baseline coverage. Deep Dive does degree requirements, roadmaps and specialised catalog readers. Degree-detail completeness is reported separately from school-level comparison readiness. Deep Dive helps with shared extraction tools when that unlocks baseline or policy coverage, and avoids bulk-data work.
- **Ownership on #153 (posted 2026-10-22):**
  - **Deep Dive:**
    - requirement groups and roadmaps;
    - the CourseLeaf plan readers (`parse_grid`, `plan_item`, `parse_plangrid`) and the Course List reader (#250);
    - #229 recovery.
  - **Research:**
    - program-list coverage and recounts;
    - baseline costs, aid, admissions and policies;
    - the registry;
    - the JHU corrections (#251);
    - the grouping rule for concentration-only lists and the dual-degree rule (Deep Dive agreed, with conditions, on #153; CU Denver needs its own owner approval).

## Numbers

These are verified records counted from `data/institutions/*`. Plans are `program_plan` records; groups are every other `degree_requirements` record.

| | main `46c7f81` (2026-10-21 start) | main `2c24af0` | main `af5868f` (after #252) | main `9ccbc6a` (#258) | main `b2c83c4` (#261) | with this PR |
|---|---|---|---|---|---|---|
| Verified bachelor's program records (all workstreams) | 10,145 | 10,648 | 10,648 | 10,648 | 10,665 (with Research #251) | 10,665 |
| Verified plans | 2,843 at 64 schools | 3,475 at 67 schools | 3,356 at 65 schools | 3,441 at 66 schools | 3,502 at 68 schools | 3,511 at 68 schools |
| Partially verified plans | 0 | 0 | 119 (#229 downgrades) | 180 (+61 CU track plans) | 119 (58 #229 + 61 CU) | 110 (49 #229 + 61 CU) |
| Verified requirement groups | n/a | 15,062 | 15,011 | 15,307 | 15,307 | 15,307 |
| Covered schools (STATUS.json, baseline) | 65 | 70 | 70 | 70 | 73 (Research) | 73 |

## This PR: printed choice blocks in plans

- **Reader:** `choice_blocks` in `programs/courseleaf.py`. A printed 'Select/Choose <N> [courses] of|from the following[:]' header with a credit cell, followed by two or more blank-credit course rows, becomes one item: `{choose, text, credits, options}`. That is the plangrid shape `web/src/lib/engine/planItems.ts` already reads (#230).
  - Before this change, every option read as a required course.
  - The options run to the next row that prints credits, or to the term's end. Every row in that run must be a course row, either read into fields or kept as a printed course string such as 'ANSC 326/FSTC 326' or 'GEOL 101& GEOL 102'. Otherwise the block stays flat, so it is never cut short.
  - `verify` checks each option.
- **Regression over the 10,061 stored grids:** 1,961 blocks in 902 grids. Flattening every new item gives back the old items exactly.
- **Independent review, read-only, own parser, two rounds:**
  - The first round found blocks cut short at printed-string options; that was fixed.
  - The second round covered 349 records: 342 approved, 7 held.
  - The 7 holds are blocks left flat because a label or note row follows them. Those records stay as on file. The follow-up is to end the run at a non-course row that is directly followed by another header.
- **Promoted 342 reviewed re-reads:** `programs/decisions/*-plans-choices.json`, with `replaces_promoted`.
  - 233 are grouping only.
  - 99 also turn courseleaf_plan/v2 printed strings into fields (Texas A&M 78, JSU, ODU, Temple, SRU).
  - 9 LMU plans held by the #229 correction for flat choice blocks are re-verified with `replaces_correction`.
- **Shared plan keys checked:** all 14 verified plans whose key two pages share came from the program's main page, not a concentration page.
  - Texas A&M Environmental Studies BS is printed under two colleges, which is Research's program-list question.

## Merged on 2026-10-21/22

| PR | What |
|---|---|
| #238, #239 | `courseleaf_plan/v2`; decimal credits |
| #241 | `courseleaf_plan/v3`: item fields, `any_of`, markers, more total and term labels, heading labels; v1 no longer trusted |
| #249 | SHSU positional plangrid with printed-sum checks; single-track labels; UNL Course Lists; per-area counts and shared plan keys held |
| #252 | #229 corrections: 2,366 plans and 76 groups replaced; 119 plans and 51 groups downgraded (`docs/coverage/I229_CORRECTIONS.md`) |
| #255 | recovery readers: YSU 'S.H.', LMU total, SLU sessions; subtotals spanning terms held |
| #258 | SHSU 85 plans and 174 groups, UNL 122 groups, CU 61 track plans (partially verified) |

## Open

- **#250 data (reader merged in #260):** re-extract the runs named in #250 (UWM `WI/2026-10-22-d01`, UW-Madison, UNI, UC Irvine, Missouri, SF State), have them reviewed, and promote.
  - The audit of the 225 verified groups listed in #250 needs owner approval.
- **#229 remainder:** 49 plans and 51 groups stay partially verified with their corrections (9 LMU plans were recovered here). Recovering them needs reader work:
  - multi-row 'or' alternatives;
  - blank-name and 'or' separator rows (YSU);
  - session headings with empty credit cells (LMU);
  - subtotals spanning terms (SLU 1, Marshall, UNC, UVU);
  - Dunwoody, Lorain and Akron label rows.
  - The 15 YSU/LMU plans held only because an 'or' row is a printed string could be approved if verbatim alternatives are accepted. That's a policy call for review, not a data defect.

## Next executable tasks

1. #250: re-extract and review the schools #260's reader affects.
2. Plan reader:
   - multi-row 'or' rows;
   - choice headers with a footnote digit ('Select one of the following: 1', about 75 records);
   - ending a choice run at a label or note row (7 holds).
   Then recover the remaining #229 plans with `replaces_correction`.
3. Reader follow-ups from the #258 reviews:
   - a single-grid `courseleaf_plangrid` label should be the program, not the nearest heading (22 SHSU holds);
   - UNL 0-credit rows are dropped from Course Lists (17 holds);
   - categorise college-core and ACE tables (56 holds);
   - read hyphenated Course List subjects (`CSCI-UA 101`, `BUSN-P316`), which needs its own review.
4. Depth at high-enrolment schools, ranked by IPEDS entering students:
   - Texas A&M and CU Boulder groups;
   - plans for Penn State, Illinois, UF, UC Davis and UC Irvine.
   Check existing readers first.
5. Coordinate national totals with Research from the same main commit.

## Blockers (recorded, not evaded)

- **Utah, BYU:** tab and Kuali views not stored.
- **UMD:** 28 majors print no award.
- **KU:** no single official list.
- **UCR:** PDF layout.

## How to resume

1. `git fetch origin`. Read this file, #153, #229, #250, and the open Deep Dive PRs.
2. Fetch the run branches: `git fetch origin '+refs/heads/program-run/*:refs/remotes/origin/program-run/*'`. Copy a run with `git archive`.
3. Before a reader change is promoted, extract the stored runs it can touch with main's code and with the branch's code, and explain every change.
4. Review independently, then promote. Then run:
   - retention (`--push`, `--verify-store`, `--check`);
   - `update_coverage`, `programs status`, `research_priority`, `validate_data`, `review_provenance`;
   - the database check, web `vitest` and unit tests;
   - `scripts/program_mutation_check.py`, never at the same time as tests or extractions in the same tree.
5. Open the PR, merge on green CI, and update this file in the same PR.

Hosted imports, migrations and deployments stay on hold.
