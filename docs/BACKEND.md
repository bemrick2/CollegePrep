# Reference backend

The repository provides a runnable read-only development adapter without a Supabase credential. It does not replace the planned normalized Supabase production database, authentication, billing or student-data storage.

```sh
python scripts/validate_data.py
python -m backend.store --database work/reference.sqlite
python -m backend.api --database work/reference.sqlite --port 8080
```

The server binds only to localhost. GET `/health`, `/v1/coverage`, `/v1/institutions?state=TN&limit=25&offset=0`, and `/v1/institutions/utk?academic_year=2026-27` return JSON. Every school-policy query requires a year. There is no silent fallback to historical costs. Missing domains and null amounts stay explicit. Imports are transactional and idempotent; changed records need `--accept-revisions`, retain previous payloads, and cannot replace verified evidence with a weaker status. Prior academic years remain separate.

Paid add-on eligibility requires an offered verified qualifying path, explicit evidence, matching requested year and verification within 365 days. Generic eligibility, scholarship-retention and professional-judgment appeals alone do not qualify. No school is currently enabled in this adapter.

Production deployment is blocked on designating a CollegePrep Supabase project. The connected projects are unrelated products. Do not use them implicitly. Apply and test schema migrations, validate RLS, build a field-level normalized importer, and compare live counts before reporting deployed coverage.

The CLI-generated `protect_reference_data_and_appeal_gate` migration provides verified-only public reads, denies client writes, adds catalog requirement storage and separate SAT sections, and replaces the unscoped SQL add-on gate with a fail-closed compatibility view plus an explicit-year view. Both migrations and database gate/permissions tests passed in disposable PostgreSQL 17 in [GitHub CI](https://github.com/bemrick2/CollegePrep/actions/runs/36987390816). It is **not deployed to production**: no CollegePrep project is designated. Existing clients must migrate to the year-specific view. Source URLs are normalized through `sources.canonical_url`; API reference payloads retain `source_url` directly. A real Supabase project's advisor checks and normalized data import remain required.

## Product plan retained

Practice questions retain an AI-help action. Help teaches concepts through graduated hints, explanations, worked examples and a student retry. Answer disclosure is intentional rather than the default. Provider integration, student privacy controls, rate limits and evaluation of instructional quality remain implementation work. Reference data alone does not implement this feature.
