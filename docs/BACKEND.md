# Reference backend

The repository provides a runnable read-only development adapter without a Supabase credential. It does not replace the planned normalized Supabase production database, authentication, billing or student-data storage.

```sh
python scripts/validate_data.py
python -m backend.store --database work/reference.sqlite
python -m backend.api --database work/reference.sqlite --port 8080
```

The server binds only to localhost. GET `/health`, `/v1/coverage`, `/v1/institutions?state=TN&limit=25&offset=0`, and `/v1/institutions/utk?academic_year=2026-27` return JSON. Every school-policy query requires a year. There is no silent fallback to historical costs. Missing domains and null amounts stay explicit. Imports are transactional and idempotent; changed records need `--accept-revisions`, retain previous payloads, and cannot replace verified evidence with a weaker status. Prior academic years remain separate.

Paid add-on eligibility requires an offered verified qualifying path, explicit evidence, matching requested year and verification within 365 days. Generic eligibility, scholarship-retention and professional-judgment appeals alone do not qualify. No school is currently enabled in this adapter.

The designated [CollegePrep project](https://supabase.com/dashboard/project/butlklkzafvklwasbynr) now has the schema and all 17,817 persisted source records loaded into normalized reference tables plus a private lossless ledger. Counts, a repeat import batch, source field comparisons and public access restrictions were verified. See `docs/coverage/live-supabase.json` for the dated evidence. Other connected projects were not modified.

The CLI-generated migrations provide verified-only public reads, deny client writes, add catalog requirement storage and separate SAT sections, and replace the unscoped SQL add-on gate with a fail-closed compatibility view plus an explicit-year view. Database gate/permissions tests passed in disposable PostgreSQL 17 in [GitHub CI](https://github.com/bemrick2/CollegePrep/actions/runs/36987390816), and reference reads/denied privileges were checked in the live project. Security advisors report no notices. Existing clients must use the year-specific view. Source URLs are normalized through `sources.canonical_url`; provenance views expose them for costs/admissions. Unknown current activity and unknown full-tuition/full-ride flags remain null.

## Live reference import

`python scripts/import_supabase.py --output work/import-bulk --batch-size 400` emits admin-only transactional SQL batches. Apply files in order through the authorized Supabase connector or a secure server-side database connection. Do not put admin credentials in GitHub or browser code. Institution dependencies load first. Each batch preserves the complete payload, archives changed same-year records, and rejects older/weaker evidence over verified records. Unsupported domains fail explicitly until a normalized mapping is implemented. The federal mapping currently supports the persisted Pell record only.

The private `ingestion` schema is not exposed through the public API. Public reference reads require verified status; client writes are denied. The development HTTP adapter remains separate from hosted Supabase REST access. Authentication, student planning data, financial calculations, billing and AI-help integration are still product work.

Supabase connector migrations are recorded with deployment-time versions. Their names match repository migrations, but versions differ from repository filenames. Reconcile migration history before using CLI `db push`; do not blindly replay already-applied migrations. This does not affect the loaded tables or CI replay into a fresh database.

## Product plan retained

Practice questions retain an AI-help action. Help teaches concepts through graduated hints, explanations, worked examples and a student retry. Answer disclosure is intentional rather than the default. Provider integration, student privacy controls, rate limits and evaluation of instructional quality remain implementation work. Reference data alone does not implement this feature.
