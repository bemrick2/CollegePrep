# Deep Dive checkpoint

This file is how a new Deep Dive session picks up shared reader work and requirement/roadmap depth without redoing finished work. It is updated with every Deep Dive PR. Research keeps its own file, `docs/coverage/RESEARCH_CHECKPOINT.md`.

- **Main at the last refresh:** `8bc64144ea` (merge of #247). This PR (`programs/i229-corrections`) is on top of it.
- **Ownership on #153:**
  - Deep Dive owns:
    - the readers for UNL, Utah, SHSU, UWM and UCR;
    - the CourseLeaf plan readers (`parse_grid`, `plan_item`, `parse_plangrid`);
    - the Course List code pattern (#250);
    - the #229 corrections.
  - **JHU 'Five-Year BM/MM Program':** the owner approved this correction on 2026-10-21. Research makes it in #251, together with the eight BM Performance records, so JHU is recounted once (agreed on #153).
  - Research owns:
    - Colorado State's program column, BYU emphases, Alabama's print-link label, and the UTSA and UT Dallas lists;
    - the Roosevelt and SF State corrections;
    - the JHU title reader for the eight BM Performance entries.

## Numbers

Counted from `data/institutions/*` with verified records only. Plans are `program_plan` records; groups are every other `degree_requirements` record. Program-list coverage is reported separately from requirement and roadmap depth.

| | main `46c7f81` (2026-10-21 start) | main `2c24af0` (#239) | main `8bc6414` | with this PR |
|---|---|---|---|---|
| Verified bachelor's program records (all workstreams) | 10,145 | 10,648 | 10,648 | 10,648 |
| Verified plans | 2,843 at 64 schools | 3,475 at 67 schools | 3,475 at 67 schools | 3,356 at 65 schools |
| Plans downgraded to partially verified | 0 | 0 | 0 | 119 |
| Verified requirement groups | n/a | 15,062 | 15,062 | 15,011 |
| Covered schools (STATUS.json) | 65 | 70 | 70 | 70 |

**Deep Dive gains on 2026-10-21 (merged):**
- 474 program records: UNL 116, Utah 101, UWM 133, SHSU 124.
- 609 plans: #225/#226 224, #238 369, #239 16.

Research's batches are counted separately. Do not add them twice.

## This PR: the #229 corrections (owner-approved 2026-10-21)

See `docs/coverage/I229_CORRECTIONS.md` for the before and after.

- **Plans:** 2,366 verified `courseleaf_plan/v1` plans are replaced in place by reviewed `courseleaf_plan/v3` re-extractions from the same stored page and grid.
  - Decisions: `programs/decisions/*-plans-i229.json`, each with `replaces_promoted`.
  - 119 are downgraded to `partially_verified`, each with a `verification_correction_reason` and a `supabase/corrections.json` entry:
    - LMU 54 and YSU 46, where the reader misses a printed total or header;
    - SLU 6 and 3 others, where a subtotal covers a whole term or year;
    - 10 others.
- **Groups:** of the 144 groups that store a printed hour or unit rule as a course count:
  - 76 replaced (`*-groups-i229.json`);
  - 51 downgraded, including all 12 Oklahoma State residency rules and 21 Stetson unit rules;
  - 17 kept as printed.
- **Reviews:** independent, read-only.
  - Plans: every plan was compared with its stored grid by the reviewer's own reader, and 68 were hand-checked across all 58 schools.
  - Groups: every group was checked against its stored Course List layout.

## Merged readers on 2026-10-21

| PR | What |
|---|---|
| #225, #226, #235 | `degree_offered/v1`, `courseleaf_plantext/v1`, `kuali_award_line/v1`, `printed_catalog_years` |
| #238 | `courseleaf_plan/v2`: year and semester terms, subtotals, totals; Course List hour choices read as credits |
| #239 | decimal course credits kept as printed |
| #241 | `courseleaf_plan/v3`: items with separate code/title/credits fields, `any_of` alternatives, Kent State markers, more total and term labels, track plans labelled by heading; `courseleaf_plan/v1` no longer trusted |

## Open

- **#249** (`programs/shsu-plangrid`): SHSU positional plan grids, single-track plan labels, UNL Course Lists, and #241 review follow-ups. The independent review found two blocking issues; fix them before merging:
  1. UNL 'Select one course each from ACE outcomes 5, 7, and 9 | 9' is read as `choose_count: 1` (18 groups, no issue).
  2. SHSU engineering-technology concentration pages (5) and the two BBA Finance concentrations give their plans the same key and no issue.

  Non-blocking findings from the same review:
  - Mizzou positional plans store codes such as 'AG_S_TCH 1020' as text, and their track plans aren't held;
  - `page_footnotes` overwrites duplicate numbers and keeps one line per footnote;
  - surviving mutants need tests.

  Full notes: the review file in the PR thread.
- **`programs/uwm-courselist`** (local commit `c90e8184dd`, not pushed): the Course List `CODE` accepts subjects of 6–7 letters and of two words, and UWM's GER paragraph no longer reads as a track choice. 2,814 of 46,838 stored tables read differently. Open the PR after #249. Its data audit is #250 (225 verified groups at 7 schools, plus 3,808 not checkable locally).
- **UWM requirement groups:** run `WI/2026-10-22-d01` (branch `program-run/wi-uwm-2026-10-22-d01`) stores Course List layout for 152 pages. Re-extract it with the #250 reader, then review.
- **SHSU plans:** after #249 merges, re-extract `TX/2026-10-21-d02` and review the 190 issue-free plans.
- **CU Boulder track plans:** Geography BS and Classics BA are labelled by #249. Leadership's line names no track, so its plan stays held.

## Next executable tasks

1. Fix #249's blocking findings, rerun its review, then merge.
2. Coordinate national totals with Research from the main commit after this PR and #251 merge.
3. Recover the downgraded plans with reader fixes, then a reviewed replacement:
   - LMU 'Minimum Semester Hours' printed after each year and as the total;
   - YSU 'S.H.' header;
   - subtotals that cover sub-sessions or a whole year;
   - '.5', '3 or 4' and '1 (0)' credits.
4. UWM and UNL requirement groups, after #249 and the #250 reader.
5. #250 audit (owner decision).

## Blockers (recorded, not evaded)

- **Utah:** the tab views are not in the stored pages.
- **UMD:** 28 majors have no award on any official UMD page read so far. Awards are not inferred.
- **KU:** no single official program list was found.
- **UCR:** the PDF tables need layout positions.

## How to resume

1. `git fetch origin`. Read this file, #153, #229, #249 and #250.
2. Fetch the run branches: `git fetch origin '+refs/heads/program-run/*:refs/remotes/origin/program-run/*'`. Copy a run with `git archive`.
3. Before a reader change is promoted, extract the stored runs it can touch with main's code and with the branch's code. Nothing may be lost or changed, and every gain must be explained.
4. Review independently, then write the reviewed decision and promote. Then run:
   - `scripts/retain_evidence.py --push`, then `--verify-store`, then `--check`;
   - `update_coverage`, `programs status`, `research_priority`, `validate_data`, `review_provenance`;
   - the database check, web `vitest` and unit tests;
   - `scripts/program_mutation_check.py`, never at the same time as tests or extractions in the same tree.
5. Open the PR, merge on green CI, and update this file in the same PR.

Hosted imports, migrations and deployments stay on hold while Supabase is paused.
