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

## Planned importer

The importer will map natural keys such as `institution_key`, state code, program name, policy kind, and academic year into database UUIDs. Import will be idempotent and will log creates, updates, skips, and conflicts.
