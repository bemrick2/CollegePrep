# Remaining work and deployment blocker — October 2, 2026

Repository reference coverage is distinct from production database coverage. The normalized 2023–24 federal batch covers 50 states and DC. Current-year COA/admissions must be verified independently; no old-year figure is silently reused. Monetary gaps and missing policies remain unknown.

## Immediate blocker

No CollegePrep Supabase project is designated. The connected account lists CRE Class, apparent-staging and bellcue-prod, which belong to other products. Designate a CollegePrep project (or explicitly request a new one) before production schema changes or live import. Existing projects were not modified.

## Verification completed

- Fresh checkout: 17,817 records validate; coverage matches persisted records; all pinned source hashes and ZIP integrity checks pass.
- Seven Python tests pass, including real HTTP requests, explicit-year lookup, import idempotence, revision retention, rollback and appeal denial.
- [GitHub CI run](https://github.com/bemrick2/CollegePrep/actions/runs/36987390816): both database migrations apply to disposable PostgreSQL 17, and gate/RLS/grant assertions pass.
- Repeat reference import inserts zero records and reports 17,817 unchanged records.

## Data gaps

- All 51 current state/DC aid inventories need completion; Tennessee has five partial-catalog program records.
- Current institutional costs/COA and admissions, full merit catalogs, AP/CLEP/IB/dual-enrollment equivalencies and their conditions, transfer/residency rules, degree/catalog requirements and qualifying appeal evidence remain largely unpopulated.
- UT Knoxville retains two credit-policy records, ten selected AP equivalencies, one award and four appeal records. This does not establish complete policy coverage. No qualifying paid add-on path has explicit reviewed evidence in the reference adapter.
- Full COA is not derived from incomplete federal components. SAT section percentiles are not summed into a composite percentile. Missing/imputed numeric values are null.

## Backend gaps

- Field-level normalized Supabase importer, live source/row reconciliation, Supabase advisors and production deployment.
- Student accounts/owned planning data, degree-path/credit optimization, rule-based aid/merit matching, payments and gated purchase flow.
- Production AI-help provider integration, student privacy controls, rate limits and instructional evaluation. The feature remains in scope.
- Scheduled official-source refresh, changed-source review and full domain completion inventories. Annual historical data remain preserved.

The backend is not substantially complete. Deployment is blocked; remaining source verification is extensive and is reported rather than guessed.
