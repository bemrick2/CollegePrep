# National school baseline

The baseline gives every in-scope school (the four-year schools in `pipeline/registry`, see
`docs/coverage/baseline/UNIVERSE.md`) the high-level comparison data, taken from official bulk files rather than a crawl.
It is separate from the school-specific policy layer (merit scholarships, exam credit, appeals, residency) and from degree
detail (Deep Dive). Neither of those is a condition for baseline coverage.

## Files

| Path | What |
|---|---|
| `baseline/schools/<year>/<ST>.csv` | One row per school. Values as NCES published them, and for every field a `__status` and a `__reason` |
| `baseline/fields_of_study/<year>/<ST>.csv` | Awards per CIP 2020 family and level (first majors) |
| `baseline/FIELDS.json` | Each field's source file, variables, NCES title and definition, period, kind, and currency rule |
| `baseline/reference/ipeds_labels.json` | NCES dictionary text and code labels, copied from the pinned `*_Dict.zip` |
| `baseline/policy/pipeline_attempts.json` | Per school and policy topic: the most informative status any pipeline run reached |
| `docs/coverage/baseline/COMPLETENESS.md`, `completeness.json` | School-by-field completeness, enrollment-weighted coverage, the policy layer and degree detail (both separate) |
| `docs/coverage/baseline/UNIVERSE.md`, `universe.json` | Inclusion rule, duplicates, campuses reported with a parent, and changes in the provisional 2024-25 directory |
| `docs/coverage/baseline/policy_queue.csv` | Every school ranked by undergraduate enrollment, with its merit, exam-credit and appeals research status |

## Statuses

Each field has one status:
- `verified_current`
- `available_older`
- `not_published_or_na`
- `not_researched`
- `blocked`

The definitions are in `scripts/build_baseline.py`. The rules behind them:
- A missing or suppressed value is never zero.
- An NCES-imputed value is withheld and marked `not_researched`, with the flag given in the reason.
- A school's own publication may still have the value.
- The NCES cost-of-attendance total is shown only when every component was reported.
- Graduation rates are withheld when any cohort count was imputed.
- Prices and net-price averages are for past years. They are `available_older`, never current prices or personal estimates.
- Net price is an average over aided students, which is a historical figure, not an offer.

## Refreshing

1. Request the files on an `ipeds-source/**` branch. Edit `ipeds-request.json` with a `requests` list of `{year, files}`, or with full `https://nces.ed.gov/` URLs for reference files, and push.
   - `.github/workflows/ipeds-source.yml` downloads each file and pins it under `sources/ipeds/<year>/` with its sha256.
   - A file NCES doesn't serve is recorded under `unavailable` with its HTTP status. That record is how "the latest release" is decided (`verified_current`).
2. If a dictionary changed, run `pip install openpyxl && python3 scripts/refresh_baseline_labels.py`.
3. Run `python3 scripts/build_baseline.py`. CI checks the IPEDS-derived files with `--check`.
4. The completeness report and policy queue also read research records and Deep Dive's STATUS.json. Regenerate them at each checkpoint:
   - `git fetch origin 'refs/heads/pipeline-run/*:refs/remotes/origin/pipeline-run/*' && python3 scripts/harvest_research_status.py`
   - then `python3 scripts/build_baseline.py`
5. To move the baseline to a newer collection year, add its files and update `YEAR`, `NEXT` and the field sources. Keep the old year's rows: they are history.

At this writing, NCES serves the full 2023-24 collection. For 2024-25 it serves only HD2024, IC2024 and C2024_A (provisional). The 2024-25 prices, admissions, enrollment, aid and graduation files are recorded as not yet served.

## Coupling

`--check` regenerates `baseline/schools`, `fields_of_study`, `FIELDS.json` and the universe report from the pinned files and
`pipeline/registry/<ST>.json` (name, key, UNITID, level) plus `docs/coverage/registry_reconciliation.json`. A registry change
that touches those fields needs `python3 scripts/build_baseline.py` in the same PR (about 10 s). Completeness, the policy
queue and the policy layer read research records and are regenerated at checkpoints, not enforced.

A school closed, inactive or missing in the provisional HD2024 is never `verified_current` and never counted complete.
`verified_current` for a statistic means "the latest NCES release" (for example fall 2023 enrollment), decided by a dated
HTTP 404 for the next year's file; re-run the pin workflow for that file when NCES announces a release.

## Validation

`tests/test_baseline.py` covers the rules on synthetic rows: missing values never zero, imputed values withheld, open admission and test-blind policies, prices older than the planning year, a child campus naming its parent, and a closed school flagged. It also checks the committed rows: one per school, statuses known, values only where resolved, and agreement with the existing `data/national/ipeds` import on more than 1,000 values.

An independent spot check against College Navigator is listed in the checkpoint.
