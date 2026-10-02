# Data ingestion

CollegePrep uses a two-stage data workflow:

1. **Versioned seed/reference JSON in GitHub** for auditability, review, and history.
2. **Supabase/Postgres normalized tables** for application queries.

## Rules

- Official sources first.
- Preserve academic-year history.
- Never overwrite a verified current record with weaker evidence.
- A missing value stays null/unknown; it is never guessed.
- Every verified policy record must have `source_url` and `last_verified_at`.
- A policy may be stored as `partially_verified` while unresolved fields remain.
- Negative findings (for example, "school does not negotiate merit") require more caution than positive findings.

## Reference importer

`scripts/import_ipeds.py` normalizes pinned official 2023–24 survey archives, rejects imputed measurements as verified values, partitions by state/year and records source hashes. `backend.store` loads all reference domains into a transactional development database, preserves revisions and academic years, and refuses verified-to-weaker replacements. `scripts/update_coverage.py` derives repository counts, with CI preventing drift. See `docs/IPEDS.md` and `docs/BACKEND.md` for reproduction.

## Normalized Supabase importer

`scripts/import_supabase.py` maps the eleven persisted reference domains (institutions, costs, admissions_metrics, state_aid, awards, appeals, credit_policies, federal_aid, academic_programs, transfer_policies, degree_requirements) by institution key, program/policy keys and academic year into generated database UUIDs. A private ledger preserves complete source records and previous payloads. Transactions reject missing dependencies and older/weaker replacements of verified records. A repeated 400-record live batch produced no duplicates or revisions.

## Import contract

`backend/catalog.py` defines `IMPORT_DOMAINS`, the controlled values that match database check constraints (`CONTROLLED_VALUES`) and the fields the normalized tables require. `scripts/validate_data.py` applies the same contract, so data that passes validation can also be imported. A new data domain or controlled value needs an importer mapping and a migration first. `tests/test_import_contract.py` fails on:

- an unmapped domain
- a domain without an insert statement
- controlled values that drift from the latest migration
- repository data the importer would reject

CI and local checks apply every migration to disposable PostgreSQL and import all repository data twice. They then run `--reconcile-sql` assertions: ledger and normalized counts per domain, the equivalency total, and zero revisions on repeat.

Program, degree-requirement and transfer records follow [the program data contract](PROGRAM_DATA.md). An `academic_programs` record (keyed by `program_key` and academic year) must exist before its `degree_requirements`. A whole catalog plan uses `requirement_kind = program_plan`, with the plan in `rule_details`. Transfer records load into `transfer_policies` with the full reviewed payload in `policy_details`.

## Automated live import

`.github/workflows/live-import.yml` runs `scripts/live_import.sh` after data or importer changes reach `main`, and can also be started by hand (workflow_dispatch). The script:

1. validates the repository
2. runs `supabase/checks/live_preflight.sql`, which stops if a required migration is missing
3. applies every import batch
4. reconciles ledger and normalized counts against the repository
5. runs a second pass and fails if the revision count or the last import time changes

Imports never run on pull requests, so PR code never sees the database secret. Imports run one at a time.

The job needs the repository secret `SUPABASE_DB_URL`: an admin Postgres connection string from the Supabase project's connection settings. Use the Session pooler string, because GitHub-hosted runners may not reach the direct database host. Without the secret, the job posts a notice and skips. Migrations are not applied by this job; apply them first, and the preflight check enforces the order. The workflow uses the `supabase-live` environment, so required reviewers can be added in GitHub settings if desired.

To run it locally against any migrated database: `DATABASE_URL=... scripts/live_import.sh`.

