# Remaining work and deployment blocker — October 2, 2026

Repository reference coverage is distinct from production database coverage. The normalized 2023–24 federal batch covers 50 states and DC. Current-year COA/admissions must be verified independently; no old-year figure is silently reused. Monetary gaps and missing policies remain unknown.

## Database setup blocker resolved

The user designated CollegePrep (`butlklkzafvklwasbynr`) in organization `atkukjwwdvhnrxwdhqmb`. Reference schema and all 17,817 source records are loaded, with dated reconciliation in `live-supabase.json`. Other projects were not modified. The full product backend is not complete.

## Verification completed

- Fresh checkout: 17,817 records validate; coverage matches persisted records; all pinned source hashes and ZIP integrity checks pass.
- Seven Python tests pass, including real HTTP requests, explicit-year lookup, import idempotence, revision retention, rollback and appeal denial.
- [GitHub CI run](https://github.com/bemrick2/CollegePrep/actions/runs/36987390816): both database migrations apply to disposable PostgreSQL 17, and gate/RLS/grant assertions pass.
- Repeat reference import inserts zero records and reports 17,817 unchanged records.

## Data gaps

- All 51 current state/DC aid inventories need completion. Tennessee now has 23 program records: 16 for 2026-27, 1 for the 2027 entering class and 5 for 2027-28 (5 verified, 17 partially verified). See [the Tennessee/UTK research notes](../research/tennessee-utk-2026-10-02.md). Unlabeled source years and the conflicting TSAA SAI threshold are still unresolved.
- Current institutional costs/COA and admissions, full merit catalogs, AP/CLEP/IB/dual-enrollment equivalencies and their conditions, transfer/residency rules, degree/catalog requirements and qualifying appeal evidence remain largely unpopulated.
- UT Knoxville now has 2026-27 COA by residency, Fall 2025 CDS and Fall 2026 admitted-profile admissions, 15 award records, 7 credit-policy records with 187 equivalencies, 2 transfer-policy records (2026-27 and preserved 2025-26), one Computer Science BS catalog record and 8 appeal records. Coverage is still partial: Fall 2026 enrolled metrics, with-family COA total, maximum transferable hours, the transfer residence conflict and Fall 2027 merit amounts are unresolved. UT states it cannot match other institutions' offers; no qualifying paid add-on path exists.
- Full COA is not derived from incomplete federal components. SAT section percentiles are not summed into a composite percentile. Missing/imputed numeric values are null.

## Backend gaps

- Eleven-domain imports, annual program/requirement dependency checks, live reconciliation and an explicit-year school-comparison RPC are implemented. UT Knoxville now has sourced transfer-policy and Computer Science program/degree records; other schools' transfer and degree domains are still empty. Migrations `20261002130818`, `20261002131409` and `20261002150000` add the program catalog, comparison RPC and new controlled values; see `live-supabase.json` for what is applied live. Nested fields without columns (term deadlines, living arrangements, award tiers) stay in the lossless ledger and JSON payloads. Hosted product/application deployment remains.
- Student accounts/owned planning data, degree-path/credit optimization, rule-based aid/merit matching, payments and gated purchase flow.
- Production AI-help provider integration, student privacy controls, rate limits and instructional evaluation. The feature remains in scope.
- Scheduled official-source refresh, changed-source review and full domain completion inventories. Annual historical data remain preserved.

The reference database is ready for additional reviewed data. Remaining product implementation and source verification are extensive and are reported rather than guessed. Reconcile connector-generated migration versions with repository filenames before a future CLI database push.
