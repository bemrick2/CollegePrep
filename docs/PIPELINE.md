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
| Promote | `python -m pipeline promote --state TN --decisions pipeline/decisions/TN-<run>.json` | anywhere | records in `data/`, evidence in `sources/pipeline/` |
| Retain | `python scripts/retain_evidence.py --push` | anywhere | `retention.json` beside each evidence archive; cited pages and layout documents in the `evidence-store` branch |

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
  When several schools in a state share a domain (KCTCS: `henderson.kctcs.edu`, `jefferson.kctcs.edu`, …)
  each is limited to its own seed hosts; a host used by several schools' seeds (the system site) is
  matched exactly and its pages carry `shared_site_attribution_review`.
- Catalog program pages (Acalog `preview_program.php`, Courseleaf `catalog.*/undergraduate/<college>/<dept>/<program>/`)
  have their own page budget; Courseleaf `/graduate/` paths are skipped.
- Spends a page budget (default 45) on links ranked by research topic (`pipeline/topics.py`).
  Depth limit 3, except a strong document link (PDF/XLSX scoring ≥ 25, e.g. a current-year AP/IB
  equivalency PDF) may be fetched one level deeper. Single-course catalog pages (`catalog.*/<subj>/<num>`,
  Acalog `preview_course`) are never followed. Analytics query parameters (`_gl`, `utm_*`, `fbclid`, …)
  are dropped, and on an https site an `http://` link is the same page as its `https://` twin.
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
| `dual_enrollment/v1` | dual enrollment / dual credit → `credit_policies` (`policy_kind: dual_enrollment`) | Eligibility tiers (grades, HS GPA, ACT/SAT alternatives, hour caps), per-credit-hour charges as printed, state grant/scholarship use only from explicit statements; FAQ questions ignored. Pages of one school merge field by field; disagreements are exceptions. |
| `catalog_program/v1` | degree requirements → `academic_programs` + `degree_requirements` | Acalog and Courseleaf program pages, bachelor/associate only, printed catalog year required. Groups in `requirement_group/v1`; Courseleaf table subtotals are never the degree total; "or" alternatives → `course_alternatives_in_rule_text`. |
| `program_map/v1` | four-year plans / academic maps (PDF) → `academic_programs` + `degree_requirements` | Year-labeled program PDFs (UTC Clear Path, MTSU Academic Map, TN Tech Degree Map). The two-column term layout is split by the header's column positions; wrapped cells and hours on their own line are rejoined. Each term keeps its printed subtotal; items are course objects only when the item is one course, otherwise the printed text. The hour summary ("120 Total Hours", "30 Hours at UTC") becomes credit/residency rows. Unlabeled documents are skipped. A program already curated from the same document keeps its curated `program_key` (review adopts it). |
| `state_policy/v1` | statewide articulation, transfer guarantee, dual admission, dual enrollment, tuition residency → `state_policies` | Statewide sources only. Statements copied verbatim and grouped by keyword; every candidate is `semantic_review_required`. Reports, dashboards and minutes are skipped. |

Statewide pages feed only state-level extractors; institution extractors never see them.
Residency in cost tables: a state name means in-state only when it is the school's own state
(`residency_names_another_state` otherwise, e.g. reciprocity rates).

### Academic year
A year label in the title wins; otherwise one label must dominate the page. A PDF/XLSX whose text prints
no year but whose file name carries exactly one (`2025-26-Dual-Enrollment-Agreement-Form.pdf`) takes that
year with basis `labeled_in_url` (promoted as `partially_verified`, flagged stale if older). Unlabeled pages are
recorded as the year in force at review with `academic_year_basis:
aid_year_in_force_at_review_source_unlabeled` (never `verified`, enforced by validation). Mixed
labels → `ambiguous_year_labels` exception. Older labels are kept as that year (history) and flagged.

### Exception queue
A candidate with any issue is an exception, never promoted silently: `conflicting_sources`
(two documents disagree on the same record), `conflicts_with_verified_record`, `ambiguous_year_labels`,
`stale_year_label:*`, `residency_unknown`, `column_alignment_uncertain`, `components_do_not_reconcile`,
`cost_period_semester`, `c1_totals_incomplete`, `*_implausible`, `rows_without_score`, `extractor_error:*`,
`shared_site_attribution_review`, `residency_names_another_state`, `course_alternatives_in_rule_text`,
`semantic_review_required`, `conflicting_values:*`, `multicolumn_layout_review` (side-by-side columns
interleaved into one tier line), `merged_score_cells` (two score tiers in one table row),
`zero_counts_with_enrollment` (CDS applied/admitted read as 0 while students enrolled).

### Re-verification
`verify.json` re-checks every non-verified curated record whose source was fetched: each number and
course string must appear verbatim in the raw text. `all_values_found_year_labeled` is an upgrade
proposal (for example, records that were downgraded only because a summarising tool read them).

### Promotion
Decisions file `pipeline/decisions/<STATE>-<run>.json` (one per reviewed run) lists `approve`, `reject` and `upgrade` entries
with reasons. Status rule: year-labeled source with no open issues → `verified`; unlabeled, or
issues explicitly accepted (`accept_issues`) → `partially_verified`. A verified record is never
replaced by weaker or older evidence (same rule as the database importer). Evidence is archived in
`sources/pipeline/<STATE>/<run>/evidence.json`. Promotion goes through a normal PR; merging runs the
live import.

## Adding a state
1. `pipeline/registry/states/<ST>.json`: statewide official seeds (coordinating board, aid agency,
   system office, residency regulation, transfer site). Seeds that 404 are reported by the crawl.
2. `python -m pipeline --state <ST> registry` (scope rule unchanged; the registry test checks every
   committed registry is current).
3. Push `pipeline/run-request.json` (`{"state": "<ST>"}`) to a `pipeline-run/<st>-<date>` branch;
   the workflow crawls and commits the run. Fix failures in shared extractors, never per state.

Batch 1 beyond Tennessee: Kentucky (46 schools, centralized community-college system on one domain),
Oregon (41, no community-college system), Nevada (7, one governing system).

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
- The documents a promoted record cites are retained in the append-only `evidence-store` branch (by git blob id) and listed in
  `retention.json`; CI fails while any cited page or layout document is unretained, so a deleted run branch loses nothing.

## Costs: what the totals mean
`total_cost_of_attendance` is filled only when the school's table includes indirect costs (books,
transportation, personal) or the total row is labelled cost of attendance. A total of tuition, fees,
room and board alone is stored as `total_direct_cost`. When components are printed per semester and
the annual total separately, the annual printed total is used and per-semester rows stay in
`components` only.
In a "Fall | Spring | Total" table the Total column is the academic year; in a headerless table whose
third column is the sum of the first two in every row, the third column is the year.

## Sites that refuse automated requests
Seven Tennessee schools return 403 or bot challenges to every request from Actions runners. The
crawler records this and never evades it. The fallback is the built-in browser on the owner's linked
computer, which needs a one-time approval per site; until then these schools are reported as
`fetch_failed` in coverage and listed in the queue.
