# Reference backend

The repository provides a runnable read-only development adapter without a Supabase credential. It does not replace the planned normalized Supabase production database, authentication, billing or student-data storage.

```sh
python scripts/validate_data.py
python -m backend.store --database work/reference.sqlite
python -m backend.api --database work/reference.sqlite --port 8080
```

The server binds only to localhost. GET `/health`, `/v1/coverage`, `/v1/institutions?state=TN&limit=25&offset=0`, and `/v1/institutions/utk?academic_year=2026-27` return JSON. Every school-policy query requires a year. There is no silent fallback to historical costs. Missing domains and null amounts stay explicit. Imports are transactional and idempotent; changed records need `--accept-revisions`, retain previous payloads, and cannot replace verified evidence with a weaker status. Prior academic years remain separate.

Paid add-on eligibility requires an offered verified qualifying path, explicit evidence, matching requested year and verification within 365 days. Generic eligibility, scholarship-retention and professional-judgment appeals alone do not qualify. No school is currently enabled in this adapter.

The designated [CollegePrep project](https://supabase.com/dashboard/project/butlklkzafvklwasbynr) now has the schema and all 17,865 persisted source records loaded into normalized reference tables plus a private lossless ledger. Counts, a repeat import batch, source field comparisons and public access restrictions were verified. See `docs/coverage/live-supabase.json` for the dated evidence. Other connected projects were not modified.

The CLI-generated migrations provide verified-only public reads, deny client writes, add catalog requirement storage and separate SAT sections, and replace the unscoped SQL add-on gate with a fail-closed compatibility view plus an explicit-year view. Database gate/permissions tests passed in disposable PostgreSQL 17 in [GitHub CI](https://github.com/bemrick2/CollegePrep/actions/runs/36987390816), and reference reads/denied privileges were checked in the live project. Security advisors report no notices. Existing clients must use the year-specific view. Source URLs are normalized through `sources.canonical_url`; provenance views expose them for costs/admissions. Unknown current activity and unknown full-tuition/full-ride flags remain null.

## Live reference import

`python scripts/import_supabase.py --output work/import-bulk --batch-size 400` emits admin-only transactional SQL batches. Apply files in order through the authorized Supabase connector or a secure server-side database connection. Do not put admin credentials in GitHub or browser code. Institution dependencies load first. Each batch preserves the complete payload, archives changed same-year records, and rejects older/weaker evidence over verified records. Unsupported domains or controlled values fail explicitly; validation enforces the same import contract (see `docs/INGESTION.md`). Add `--reconcile-sql <file>` to emit post-import count assertions for a fresh database. The federal mapping currently supports the persisted Pell record only.

A documented correction to an inherited verification status requires both `--accept-corrections` and a nonempty `verification_correction_reason` in the incoming record. The previous payload remains in the revision ledger; older evidence still fails. Local imports also require `--accept-revisions`. Unlabeled annual evidence cannot be marked verified. This corrects four inherited Tennessee aid flags rather than keeping an unsupported verified status.

Credit-equivalency imports retain superseded rows with `is_current=false`. Public reads and comparisons expose only current rows under verified parents. A null-safe unique key prevents repeat imports from duplicating equivalencies with unknown course equivalents or score thresholds. Full prior policy payloads remain in the private revision ledger.

The private `ingestion` schema is not exposed through the public API. Public reference reads require verified status; client writes are denied. Program, transfer and degree imports are implemented; see [the data contract](PROGRAM_DATA.md). Authentication, student planning data, financial calculations, billing and AI-help integration are still product work.

## School comparisons

The Supabase RPC `compare_institutions` takes `p_institution_keys` (1â€“20 distinct keys) and `p_academic_year` (required, exact match). Call it with a publishable client key, for example `supabase.rpc('compare_institutions', {p_institution_keys: ['utk'], p_academic_year: '2026-27'})`. It uses the caller's permissions and verified official records. No admin key is required.

Each requested school has `found`, a sourced identity, eight domain arrays, `missing_domains`, and `can_offer_paid_addon`. Unknown schools have `found: false`; empty domains mean no verified record for that year, not that a benefit or requirement does not exist. Institution identity has a separate historical `identity_academic_year`; it does not establish current operation. Credit equivalencies inherit the parent policy's year and provenance. Degree requirements include their stable parent program key. A nonempty domain is partial coverage, not a complete school catalog. State and federal aid require separate eligibility evaluation and are not implied by the school's location.

The local adapter offers `GET /v1/compare?institution_key=utk&institution_key=other&academic_year=2026-27` with the same request limits and verified-record filtering. Synthetic PostgreSQL tests check public and authenticated reads, annual isolation, missing schools/data, provenance, nested equivalencies, and the paid appeal gate.

Repository migration filenames and the hash manifest now match the live connector history. Run `python scripts/check_migration_history.py --live` before deployment; the automated importer checks for drift. See [migration instructions](MIGRATIONS.md).

## Product plan retained

Practice questions retain an AI-help action. Help teaches concepts through graduated hints, explanations, worked examples and a student retry. Answer disclosure is intentional rather than the default. Provider integration, student privacy controls, rate limits and evaluation of instructional quality remain implementation work. Reference data alone does not implement this feature.
