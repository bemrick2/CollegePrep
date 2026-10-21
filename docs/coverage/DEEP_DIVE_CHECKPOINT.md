# Deep Dive checkpoint

This file is how a new Deep Dive session picks up shared reader work and requirement/roadmap depth without redoing finished work. It is updated with every Deep Dive PR. Research keeps its own file, `docs/coverage/RESEARCH_CHECKPOINT.md`.

- **Main at the last refresh:** `46c7f81605` (merge of #216).
- **Ownership on #153 (2026-10-21):**
  - Deep Dive owns the readers for UNL, Utah, SHSU, UWM and UCR.
  - Research owns Colorado State's program column, BYU emphases, Alabama's print-link label, the UTSA and UT Dallas program lists, and the Roosevelt and SF State corrections.

## Numbers

Counted from `data/institutions/*`, verified records only. Program-list coverage is reported separately from requirement and roadmap depth.

| | main `46c7f81` | this PR |
|---|---|---|
| Verified bachelor's program records | 10,145 | 10,309 (+105 UNL, +59 Utah) |
| Verified term-by-term plans (`program_plan`) | 2,843 at 64 schools | 3,019 at 65 schools (+176 UNL) |
| Verified major requirement groups | 14,070 | 14,070 |
| Covered schools (`docs/PROGRAM_DEPTH_COMPLETION.md`) | 65 | 65 (UNL 106/124 = 85%, under the 90% bar) |

## Readers added (each with tests and mutants)

| Reader | Where | What it reads |
|---|---|---|
| `degree_offered/v1` | `programs/extract.py` | CourseLeaf major pages named by the major alone, with the award only in the summary row `Degree Offered: \| Bachelor of Arts or Bachelor of Science` (UNL). Runs only when `department_section/v1` finds nothing. |
| `courseleaf_plantext/v1` | `programs/courseleaf.py` | UNL's '4-Year Plans' tab, which has no table. It reads term headers, course rows (code, title, credits), requirement rows, notes and milestones as printed, and keeps each plan's printed title (option or award plan). |
| `kuali_award_line/v1` | `programs/extract.py` | Utah's '<CODE> Program' pages: the name is the heading, and the award comes from the next line, where the department runs into the award. |

## In flight (run branches)

| Run | Purpose | State |
|---|---|---|
| NE/2026-10-21-d01 | Refetch 13 UNL majors not in the sitemap | Done. Extract with this PR's readers, review, and add to UNL's count. |
| UT/2026-10-21-d01 | Utah list pages 1–29 ('562 results found') and program pages | Pushed. Extract, review the added records, and record the reviewed count. |
| TX/2026-10-21-d01 | SHSU walk from 'Colleges & Academic Departments' | Done. 77 program pages. Pages print 'Undergraduate Catalog' / '2026-2027' as a two-line header, plus a print-menu '2025-2026 Catalog', so the year reads as 2025-26 until the header rule accepts a named catalog line. This is the next reader fix. |
| WI/2026-10-21-d01 | UWM program pages under the college paths | Done. 152 pages, 0 candidates under the `coursedog` platform. The pages are CourseLeaf-style ('Course List' tables, '<Name>, BA' headings): try the config as `courseleaf`. |

## Next executable tasks

1. **SHSU:** accept 'Undergraduate Catalog' / '2026-2027' as a header label. Run a regression over every stored run, because this changes year labels. Then review.
2. **UWM:** re-extract WI/2026-10-21-d01 as CourseLeaf, then review and count against the rendered Programs page.
3. **UNL:** add the refetched majors. The award rows the reader does not read are queued: Architectural Studies BSD + M.Arch, Food Science (BS, MS, PhD in one row) and 'Professional Bachelor of Landscape Architecture'. Read requirement groups by section heading; the pages also print the minor's tables.
4. **Plans already stored but not promoted at covered schools.** A scan on 2026-10-21 found 'Plan of Study Grid' tables on most verified program pages at:
   - Texas A&M: 172 pages, 1 plan on file. 281 `courseleaf_plan/v1` candidates in TX/2026-10-06-cat; 54 key-match verified records.
   - CU Boulder: 89 pages.
   - NYU: 80.
   - Iowa State: 110, captionless.
   - OSU-Cascades: 24.
   - JSU, Louisville and EKU (partial).

   Re-extract each, check that program keys match the verified records, review independently, and promote.
5. **UCR:** the 2026-2027 catalog PDF prints its majors in two-column tables, and plain text separates names from their awards. It needs layout positions (like `courseleaf_plangrid/v1`); never pair rows by guess.

## Blockers (recorded, not evaded)

- **Utah plans and requirements** sit behind the 'Sample Degree Plans' and 'Program Requirements' tabs. The stored rendered pages do not include them.
- **UMD:** 28 majors still have no award on any official UMD page read so far. Awards are not inferred.
- **KU:** the catalog prints no single program list. Plan grids appear on only 13 stored pages.
- **JHU recount:** MD/2026-10-07-cat2 no longer reproduces 17 approved department-page candidates with the current readers. The records stay on file. Bisect shows the first change is `71c0ad91bb` (Review of #211: options of listed degrees held), on Research's side. Research owns JHU in its near tier.

## How to resume

1. `git fetch origin`. Read this file and #153.
2. Fetch run branches: `git fetch origin '+refs/heads/program-run/*:refs/remotes/origin/program-run/*'`. Copy a run into `programs/runs/` with `git archive`.
3. Before a reader change is promoted, extract every stored run the change can touch with main's code and with the branch's code. Compare candidates: nothing may be lost or changed, and every gain must be explained.
4. Review independently, write the reviewed decision, promote, then run:
   - `python3 scripts/retain_evidence.py --push`, then `--verify-store`, then `--check`
   - `update_coverage`, `programs status`, `research_priority`, `validate_data`, `review_provenance`
   - the database check
   - unit tests and `scripts/program_mutation_check.py`
5. Open the PR, merge on green CI, and update this file in the same PR.

Hosted imports, migrations and deployments stay on hold while Supabase is paused.
