# Remaining work and deployment blocker — October 2, 2026

Repository reference coverage is distinct from production database coverage. The normalized 2023–24 federal batch covers 50 states and DC. Current-year COA/admissions must be verified independently; no old-year figure is silently reused. Monetary gaps and missing policies remain unknown.

## Database setup blocker resolved

The user designated CollegePrep (`butlklkzafvklwasbynr`) in organization `atkukjwwdvhnrxwdhqmb`. Reference schema and all 17,865 source records are loaded, with dated reconciliation in `live-supabase.json`. Other projects were not modified. The full product backend is not complete.

## Verification completed

- Repository integration: 17,865 records validate; generated coverage matches persisted records; all pinned source hashes and ZIP integrity checks pass.
- Twenty-five Python tests pass, including real HTTP requests, explicit-year comparisons, import idempotence, revision retention, rollback, reviewed corrections and appeal denial.
- [Comparison CI](https://github.com/bemrick2/CollegePrep/actions/runs/37012524261): migrations replay in disposable PostgreSQL 17, and comparison, gate, RLS and grant assertions pass. Integration adds full repository import/reconciliation twice and retained-equivalency tests.

## Data gaps

- All 51 current state/DC aid inventories need completion. Tennessee has 22 program records: 16 for 2026-27, 1 for the 2027 entering class and 5 for 2027-28 (1 verified, 21 partially verified). Four inherited verified flags were corrected with explicit reasons because official sources do not establish their aid year. See [the research notes](../research/tennessee-utk-2026-10-02.md). Unlabeled source years and the conflicting TSAA SAI threshold remain unresolved.
- Current institutional costs/COA and admissions, full merit catalogs, AP/CLEP/IB/dual-enrollment equivalencies and their conditions, transfer/residency rules, degree/catalog requirements and qualifying appeal evidence remain largely unpopulated.
- UT Knoxville now has 2026-27 COA by residency, Fall 2025 CDS and Fall 2026 admitted-profile admissions, 15 award records, 7 credit-policy records with 187 equivalencies, 2 transfer-policy records (2026-27 and preserved 2025-26), one Computer Science BS catalog record and 8 appeal records. Coverage is still partial: Fall 2026 enrolled metrics, with-family COA total, maximum transferable hours, the transfer residence conflict and Fall 2027 merit amounts are unresolved. UT states it cannot match other institutions' offers; no qualifying paid add-on path exists.
- Full COA is not derived from incomplete federal components. SAT section percentiles are not summed into a composite percentile. Missing/imputed numeric values are null.

## Backend gaps

- Eleven-domain imports, annual program/requirement dependency checks, and a verified explicit-year comparison RPC are implemented and tested. The reviewed-policy migration extends controlled values and preserves superseded credit rows. Nested fields without columns (term deadlines, living arrangements, award tiers) remain in the private lossless ledger; public comparisons expose only normalized fields. Hosted application deployment remains.
- Student accounts/owned planning data, degree-path/credit optimization, rule-based aid/merit matching, payments and gated purchase flow.
- Production AI-help provider integration, student privacy controls, rate limits and instructional evaluation. The feature remains in scope.
- Scheduled official-source refresh, changed-source review and full domain completion inventories. Annual historical data remain preserved.

The reference database is ready for additional reviewed data. Remaining product implementation and source verification are extensive and are reported rather than guessed. Migration filenames and hashes now match the live history; deployment checks enforce this alignment.
