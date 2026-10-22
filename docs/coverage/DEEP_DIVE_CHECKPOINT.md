# Deep Dive checkpoint

This file is how a new Deep Dive session picks up degree-requirement, roadmap and specialised-reader work without redoing finished work. It is updated with every Deep Dive PR. Research keeps its own file, `docs/coverage/RESEARCH_CHECKPOINT.md`.

- **Main at the last refresh:** `af5868f99a` (merge of #255). This PR (`programs/shsu-unl-depth`) is on top of it.
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

| | main `46c7f81` (2026-10-21 start) | main `2c24af0` | main `af5868f` (after #252) | with this PR |
|---|---|---|---|---|
| Verified bachelor's program records (all workstreams) | 10,145 | 10,648 | 10,648 | 10,648 |
| Verified plans | 2,843 at 64 schools | 3,475 at 67 schools | 3,356 at 65 schools | 3,441 at 66 schools |
| Partially verified plans | 0 | 0 | 119 (#229 downgrades) | 180 (+61 CU track plans, see below) |
| Verified requirement groups | n/a | 15,062 | 15,011 | 15,307 |
| Covered schools (STATUS.json, baseline) | 65 | 70 | 70 | 70 |

## This PR

- **SHSU:** 85 plans read by position from the `#plangrid` layout (#249) and 174 Course List groups.
- **UNL:** 122 Course List groups (#249 wiring).
- **CU Boulder:** 61 track plans, each labelled by its printed heading.
  - They are promoted `partially_verified`, because `pipeline/promote.py` gives that status to every record approved with an accepted issue, here `plan_heading_label`.
  - Making a reviewer-confirmed label non-blocking would be a shared-code decision. It's the next item for this area.
- **Independent reviews:**
  - Plans: 171 reviewed, 146 approved, 25 held.
    - SHSU 22: the stored label is a stray section heading such as 'Applied Music Fees'.
    - CU 3: Classics, labelled by a sentence; Women and Gender Studies and Biomedical Engineering, labelled by section headings.
  - Groups: 375 reviewed, 296 approved, 79 held.
    - UNL 0-credit rows dropped and lists split: 17.
    - Partial sections: 3.
    - Minor, business-core, ACE or college groups labelled as major: 56.
    - Other: 3.

## Merged on 2026-10-21/22

| PR | What |
|---|---|
| #238, #239 | `courseleaf_plan/v2`; decimal credits |
| #241 | `courseleaf_plan/v3`: item fields, `any_of`, markers, more total and term labels, heading labels; v1 no longer trusted |
| #249 | SHSU positional plangrid with printed-sum checks; single-track labels; UNL Course Lists; per-area counts and shared plan keys held |
| #252 | #229 corrections: 2,366 plans and 76 groups replaced; 119 plans and 51 groups downgraded (`docs/coverage/I229_CORRECTIONS.md`) |
| #255 | recovery readers: YSU 'S.H.', LMU total, SLU sessions; subtotals spanning terms held |

## Open

- **#250 (`programs/uwm-courselist`):** the Course List reader for 6–8 letter, two-word and '&' subjects.
  - The first review was blocking: long-subject complex rows were dropped. That's fixed in `08c2e931fe`, and the re-review is in progress.
  - When it merges, re-extract the runs from the #250 issue (UWM `WI/2026-10-22-d01`, UW-Madison, UNI, UC Irvine, Missouri, SF State), have them reviewed, and audit the 225 verified groups listed in #250. That audit needs owner approval.
- **#229 recovery (119 plans):** the readers are merged in #255. Re-extract LMU (`CA/2026-10-07-cat`), YSU (`OH/2026-10-07-cat`), SLU and the others, then review.
  - Re-promoting a downgraded record needs an explicit, reviewed override in `programs/promote.py`. `kept_record` refuses any record whose key is in `supabase/corrections.json`, deliberately.

## Next executable tasks

1. Merge #250 after re-review and CI, then re-extract and review the affected schools.
2. #229 recovery: a reviewed promote override for corrected records, then re-promotion of the recovered plans.
3. Reader follow-ups found by today's reviews:
   - a single-grid `courseleaf_plangrid` label should be the program, not the nearest heading (22 SHSU holds);
   - UNL 0-credit rows dropped from Course Lists, which splits lists (17 holds);
   - categorise college-core and ACE tables instead of labelling them as major (56 holds).
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
