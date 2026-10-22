# National baseline and scholarships: Research checkpoint

How a new Research session resumes the national school-level work (owner priority, 2026-10-22 04:40 CT) and the
scholarship work (04:41 CT). Program-list and degree-depth work is in `docs/coverage/RESEARCH_CHECKPOINT.md`. Degree
requirements belong to Deep Dive (#153).

## State (branch `research/national-baseline`, PR #259)

| Measure | Value |
|---|---|
| In-scope schools (four-year registry) | 2,119 (`UNIVERSE.md`) |
| Complete baseline (every essential field resolved) | 1,865; 97.0% enrollment-weighted |
| With every field current | 0 (IPEDS prices are 2023-24, net price 2022-23) |
| Closed or inactive in provisional HD2024 | 15, flagged |
| Current school-published tuition (2026-27+, verified) | 181 schools, 6.2% of undergraduates |
| Merit: verified / partially verified records | 73 / 83 schools |
| Merit: no published score formula (stated by the school) | 2 (UCF, UF) |
| Merit: candidate never reviewed / rejected in review | 30 / 69 |
| Merit: official page found, nothing structured | 1,389 |
| Merit: searched, not found / inaccessible / not researched | 125 / 272 / 76 |
| Merit records with an ACT/SAT criterion | 39 schools, 2.4% of undergraduates |
| Reviewed merit statements (superscore, test-optional, no fixed criteria) | 8 schools (`baseline/policy/merit_research.json`) |

Field-level detail is in `COMPLETENESS.md`. The queue of every school, ranked by enrollment, is in `policy_queue.csv`.

## Done

- **IPEDS pin workflow.** Handles several years per request, takes reference URLs, and records unserved files as `unavailable`.
- **Pinned files:**
  - the full 2023-24 collection needed for the baseline;
  - provisional HD2024, IC2024 and C2024_A;
  - FLAGS2023/2024;
  - the CIP 2020 list.
  - Files recorded as not yet served: the rest of 2024-25 and all of 2025-26.
- **`scripts/build_baseline.py`.** Builds 11 essential fields, each with status and reason, plus fields of study, `FIELDS.json` (NCES definitions), and the universe report.
  - Checked in CI; build takes about 10 s.
- **Policy layer.** Harvested from the 66 pipeline run branches together with their review decisions (`harvest_research_status.py`).
- **Merit statement scanner.** `scan_merit_statements.py` reads archived pages: 100 schools in 100 s, producing 643 candidate sentences.
  - 8 schools reviewed and recorded with retained evidence.
  - Context matters: an FSU sentence about BOG 6.005 transfer admits was excluded.

## Gaps

- **Baseline fields not researched:**
  - test scores: 160 (80 test-optional schools reported none);
  - graduation rate: 123;
  - tuition: 89 (NCES flags A/A, mostly non-academic-year reporters);
  - admissions: 79;
  - cost of attendance: 24.
  - These need the school's own Common Data Set or pages.
- **College Scorecard not yet pinned.** IPEDS covers every requested field. Scorecard would add earnings and debt, which aren't requested yet. Its bulk filename changes per release, so it needs a pinned URL from a search result.
- **Current-year prices.** Only 181 schools have verified 2026-27 tuition. Everything else shows 2023-24 IPEDS figures, labelled older.
- **Policy layer beyond merit.**
  - Residency is a state-level policy, so it isn't counted per school.
  - The aid-appeals status counts candidates, but 848 schools have candidates that were rejected in review.
- **No independent check against College Navigator yet.** It is part of the #259 review.

## Blockers

- Hosted imports and migrations are held. The baseline is files only, with no Supabase mapping yet. A reviewed migration and import mapping can be written and merged, but not applied.
- NCES hasn't served the 2024-25 prices, admissions, enrollment, aid or graduation files.
- 272 schools are inaccessible to the crawl (bot challenges or fetch failures). These are recorded, never evaded.

## Next batches

1. **Merit candidates never reviewed (30 schools).** Review them in their runs' decision files and promote, starting with BYU-Idaho, Minnesota, Broward, Nevada-Reno, MTSU, UNF, FGCU, EKU and Fordham.
2. **Merit statements, schools ranked 101–500.** Run `scan_merit_statements.py --limit-schools 500` and review in context. Record `no_published_score_formula`, superscore and test-optional findings.
3. **Merit grids from "source found" pages (1,389).**
   - Profile which page layouts the `merit_table/v1` reader misses at the 100 largest schools, then build readers for the common ones (tiered ACT/GPA grids, award lists with criteria).
   - Promote through the reviewed pipeline.
   - Track score- and GPA-linked coverage separately.
4. **Baseline gaps.** For the test-score and graduation gaps at large schools, check each school's Common Data Set (sections C9/B4). Record each value with its year; never infer one.
5. **Supabase mapping.** Write a migration and an import for the baseline table, with tests. Merge it; don't apply it.
6. **Current prices.** Rank schools without verified 2026-27 tuition by enrollment. Re-run the pipeline cost readers on them, or fetch their cost pages.

## Throughput (first bulk pass)

- **Bulk baseline:** 2,119 schools in one ~3-minute pin workflow run plus a 10-second build. All remaining baseline gaps (about 470 school-fields) need school-level sources. At 3–5 minutes each with review, that's roughly 25–40 hours.
- **Merit statements:** scanning takes about 1 s per school. In-context review took about 4 minutes per school for the first 8. At that rate, the 1,389 source-found schools come to roughly 90 hours. Readers for the common grid layouts should cut most of that.
