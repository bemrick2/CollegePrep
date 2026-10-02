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

`scripts/import_supabase.py` maps the ten persisted reference domains (institutions, costs, admissions_metrics, state_aid, awards, appeals, credit_policies, federal_aid, transfer_policies, degree_requirements) by institution key, program/policy keys and academic year into generated database UUIDs. A private ledger preserves complete source records and previous payloads. Transactions reject missing dependencies and older/weaker replacements of verified records. A repeated 400-record live batch produced no duplicates or revisions.

## Import contract

`backend/catalog.py` defines `IMPORT_DOMAINS`, the controlled values that match database check constraints (`CONTROLLED_VALUES`) and the fields the normalized tables require. `scripts/validate_data.py` applies the same contract, so data that passes validation can also be imported. A new data domain or controlled value needs an importer mapping and a migration first. `tests/test_import_contract.py` fails on:

- an unmapped domain
- a domain without an insert statement
- controlled values that drift from the latest migration
- repository data the importer would reject

CI and local checks apply every migration to disposable PostgreSQL and import all repository data twice. They then run `--reconcile-sql` assertions: ledger and normalized counts per domain, the equivalency total, and zero revisions on repeat.

Degree requirements are stored as one `academic_programs` row (keyed by `program_key` and academic year) plus `degree_requirements` rows. A whole-program catalog plan uses `requirement_kind = program_plan`, with the reviewed payload kept in `rule_details`. Transfer rules load into `transfer_policies` (`min_grade`, `max_transfer_credits`, `residency_requirement_credits`, with the payload in `policy_details`).
