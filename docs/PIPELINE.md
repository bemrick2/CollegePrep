# Official-source research pipeline

Collects current-year institutional policy from official sources with deterministic code, so
Claude time goes to review, exceptions and extractor work rather than page-by-page research.
Tennessee is the proving ground. Code: `pipeline/`. Tests: `tests/test_pipeline.py`.

## Stages

| Stage | Command | Runs where | Output |
| --- | --- | --- | --- |
| Registry | `python -m pipeline registry --state TN` | anywhere | `pipeline/registry/TN.json` (committed) |
| Crawl | `python -m pipeline crawl --state TN --run DIR` | GitHub Actions (needs open internet) | `DIR/manifest.jsonl`, `DIR/pages/*.json.gz` |
| Review | `python -m pipeline review --state TN --run DIR` | anywhere | `candidates.json`, `verify.json`, `review.md`, `coverage.json` |
| Promote | `python -m pipeline promote --state TN --decisions pipeline/decisions/TN.json` | anywhere | records in `data/`, evidence in `sources/pipeline/` |

`run` = crawl + review. The workflow `.github/workflows/research-pipeline.yml` runs crawl and
review and commits the run directory to a `pipeline-run/**` branch. It never imports data.

### Registry
Seeds come from the pinned IPEDS HD file: each school's reported website, admissions and
financial-aid URLs (net-price calculators are excluded because vendors host many of them).
Scope rule: active, degree-granting, undergraduate, public or private nonprofit, 2- or 4-year,
with a 2023-24 IPEDS first-time-undergraduate price or admissions record. Tennessee: 59 schools.
Statewide seeds (aid agency, board of regents, transfer pathways) are hand-maintained in
`pipeline/registry/states/<STATE>.json`. URLs already cited by curated records are added as seeds so
every run re-checks them.

### Crawl
- Follows links only on the school's own registrable domains; skips logins, news, events, social and media.
- Spends a page budget (default 45) on links ranked by research topic (`pipeline/topics.py`).
- Honours robots.txt (unreachable robots → host skipped), one request per host per second,
  identifying user agent, 15 MB cap, retries on 5xx/429/timeouts. Blocked pages are recorded, not evaded.
- HTML → text, tables, headings, links; PDF → `pdftotext -layout` plus fillable-form values (pypdf);
  XLSX → cell text. Documents are stored content-addressed by SHA-256.
- **Resumable and idempotent:** every fetch is appended to `manifest.jsonl`; a re-run with the same
  run directory skips fetched URLs and rebuilds the frontier from stored links.

### Extractors
All emit `verification_status: unverified` candidates with a verbatim snippet for every value.

| Extractor | Category → domain | Notes |
| --- | --- | --- |
| `credit_table/v1` | AP, CLEP, IB → `credit_policies` | Rows only count when the exam cell matches the canonical catalog (`pipeline/exams.py`); score and course cells copied as printed; ≥3 matching rows required. |
| `cost_table/v1` | tuition/fees, COA → `costs` | HTML tables and PDF layout text. Columns mapped to residency and living arrangement from headers. Printed totals copied; component sums only produce `components_reconcile`. |
| `common_data_set/v1` | CDS C1/C9 → `admissions_metrics` | Only explicit total lines (no summing of gender rows); score percentiles must be in range and ordered. |
| `merit_table/v1` | merit scholarships → `awards` | Award lists, GPA tier tables and GPA × test grids; numeric `thresholds` only from clean single-number cells; transfer and need-based tables skipped. |
| `appeal_sentences/v1` | appeals → `appeals` | Sentences describing appeal routes and negative statements ("cannot match offers"); never sets paid add-on eligibility; every candidate needs review. |
| `transfer_sentences/v1` | transfer/residence → `transfer_policies` | Minimum transfer grade, transfer-hour cap, residence hours; different values on one page are an exception. |

Categories without an extractor yet (dual enrollment, tuition residency rules, statewide
articulation, degree requirements) are measured as `source_found` leads. See the
GitHub issues labelled `area:pipeline`.

### Academic year
A year label in the title wins; otherwise one label must dominate the page. Unlabeled pages are
recorded as the year in force at review with `academic_year_basis:
aid_year_in_force_at_review_source_unlabeled` (never `verified`, enforced by validation). Mixed
labels → `ambiguous_year_labels` exception. Older labels are kept as that year (history) and flagged.

### Exception queue
A candidate with any issue is an exception, never promoted silently: `conflicting_sources`
(two documents disagree on the same record), `conflicts_with_verified_record`, `ambiguous_year_labels`,
`stale_year_label:*`, `residency_unknown`, `column_alignment_uncertain`, `components_do_not_reconcile`,
`cost_period_semester`, `c1_totals_incomplete`, `*_implausible`, `rows_without_score`, `extractor_error:*`.

### Re-verification
`verify.json` re-checks every non-verified curated record whose source was fetched: each number and
course string must appear verbatim in the raw text. `all_values_found_year_labeled` is an upgrade
proposal (for example, records that were downgraded only because a summarising tool read them).

### Promotion
Decisions file `pipeline/decisions/<STATE>.json` lists `approve`, `reject` and `upgrade` entries
with reasons. Status rule: year-labeled source with no open issues → `verified`; unlabeled, or
issues explicitly accepted (`accept_issues`) → `partially_verified`. A verified record is never
replaced by weaker or older evidence (same rule as the database importer). Evidence is archived in
`sources/pipeline/<STATE>/<run>/evidence.json`. Promotion goes through a normal PR; merging runs the
live import.

## Coverage
`coverage.json` gives each institution × category one status, in order of strength:
`verified_current`, `partially_verified_current`, `candidate_ready`, `candidate_exception`,
`source_found`, `not_found`, `fetch_failed`, with state and category rollups. Promoted run
summaries are copied to `docs/coverage/pipeline/<STATE>.json`.

## Running it
- **New run:** create a branch `pipeline-run/<state>-<date>` with `pipeline/run-request.json`
  (`{"state": "TN", "budget": 45, "run_date": "YYYY-MM-DD", "only": []}`) and push. Push again to resume.
- **Manual/scheduled:** workflow_dispatch (state, only, budget) or the weekly Monday schedule.
- Run branches are working branches; only decisions, promoted data and coverage summaries are merged.

## Costs: what the totals mean
`total_cost_of_attendance` is filled only when the school's table includes indirect costs (books,
transportation, personal) or the total row is labelled cost of attendance. A total of tuition, fees,
room and board alone is stored as `total_direct_cost`. When components are printed per semester and
the annual total separately, the annual printed total is used and per-semester rows stay in
`components` only.

## Sites that refuse automated requests
Seven Tennessee schools return 403 or bot challenges to every request from Actions runners. The
crawler records this and never evades it. The fallback is the built-in browser on the owner's linked
computer, which needs a one-time approval per site; until then these schools are reported as
`fetch_failed` in coverage and listed in the queue.
