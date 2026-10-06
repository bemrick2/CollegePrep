# Program & Degree Deep Dive

A separate workstream from the national first-pass pipeline (`pipeline/`). Its job is depth on academic programs
for the pilot states (Tennessee, Oregon): complete current-catalog program lists, program requirements and
degree maps, and the CR-14 fields (admission to the major, internal transfer, undeclared policy, CIP,
major-specific scholarships, catalog completeness).

Same standards as the national pipeline: official sources only, verbatim evidence, explicit academic year,
never infer absence, reviewed promotion by PR, regression tests and mutation checks.

## Flow

1. **Targets** — `programs/targets/<STATE>.json`, built by `python -m programs.build_targets`. Each school has its
   official hosts, catalog platform (`acalog`, `courseleaf`, `smartcatalog`, `coursedog`, `kuali`, `drupal`) and
   current-catalog id/path, program-list pages, degree-map indexes and program-admission policy pages. Schools not
   yet configured run in `discover` mode to locate their catalog; the next targets revision configures them from
   what the run found.
2. **Retrieval** — push `programs/run-request.json` (`{"state": "OR", "run_id": "2026-10-05-b"}`) to a
   `program-run/**` branch. `.github/workflows/program-research.yml` crawls (`python -m programs crawl`) and
   extracts (`python -m programs extract`), then commits `programs/runs/<STATE>/<run_id>/` back to that branch.
   Runs are resumable and never merged to main (`programs/runs/` is git-ignored).
   * Reuses `pipeline.crawl.Fetcher` (robots.txt, per-host delay, challenge backoff; bot challenges are recorded,
     never evaded), `Run`, `parse_document`, and the `catalog_program/v1` and `program_map/v1` extractors.
   * JavaScript catalogs (`"render": "browser"`) are rendered with headless Chromium in the job.
   * Program pages are fetched bachelor-first from the official list (cap 450 per school).
3. **Outputs per run** — `program_lists.json` (every listed program, text as printed), `candidates.jsonl`
   (academic_programs + degree_requirements), `evidence.jsonl` (verbatim CR-14 sentences with document hashes),
   `summary.json`, `review.md`.
4. **Review and promotion** — decisions in `programs/decisions/<STATE>-<run>.json`; `python -m programs promote`
   writes `data/` and archives evidence to `sources/programs/<STATE>/<run>/evidence.json`.
5. **Audit** — `python -m programs audit` writes `docs/coverage/programs/TN-OR.{json,md}`.

## CR-14 field rules (see also docs/PROGRAM_DATA.md)

* `admission_type`: `direct` when first-year students who meet published criteria (or are admitted to the
  college at entry) start in the major; `pre_major` when students start outside the major and must apply or meet
  progression criteria; `open` only when the institution states the major can simply be declared. When a school
  has a selective first-year path (by invitation or competitive review) beside a standard pre-major path, the
  value is the standard path and `admission_details.paths` lists both with their quotes.
* Every field carries its verbatim quote, official https source and document hash. No quote, no field.
* `program_catalogs.programs_complete = true` only when every bachelor program on the official list has a verified
  record (`listed_program_keys`); `validate_data.py` enforces it. Otherwise the product says "not in our verified
  list", never "not offered".

## Coordination

No edits to `pipeline/` or `scripts/mutation_check.py`. Shared-file touch points are additive and listed in the PR:
`backend/catalog.py` (new `program_catalogs` domain), `scripts/import_supabase.py` (new columns/table mapping),
`scripts/validate_data.py` (two hook lines), `.github/workflows/validate-data.yml` (two steps).
