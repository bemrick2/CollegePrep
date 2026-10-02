# CollegePrep

Backend and data repository for the college-planning product currently being developed as **Prep & Price**.

## Purpose

CollegePrep combines academic preparation, college-credit planning, school comparison, degree-path optimization, financial-aid/merit analysis, and cost-reduction recommendations.

This repository is the durable source of truth for:

- database schema and migrations
- verified reference data and provenance
- import/normalization/validation tooling
- school/program/state-aid policy data
- AP/CLEP/dual-enrollment/transfer-credit policy data
- merit scholarship and admissions reference data
- financial-aid appeal/reconsideration eligibility
- product rules used by the recommendation engine

## Data quality rules

1. Prefer official government, state, college, or university sources.
2. Never guess missing policy or award data.
3. Every policy-bearing record must include a source URL, academic year (when applicable), verification status, and last-verified date.
4. Stale or unverified records are allowed in storage but must be explicitly flagged.
5. The paid negotiation/appeal add-on may only be offered when the institution actually provides a documented appeal/reconsideration path.
6. Source data and normalized data are kept separate so imports are auditable.
7. Annual refreshes should preserve prior-year history rather than overwriting it.

## Repository structure

```
supabase/migrations/     Database schema
schemas/                 JSON schemas and enumerations
data/                    Versioned verified seed/reference data
scripts/                 Import, normalization, and validation tools
docs/                    Product/data architecture and coverage notes
```

## Current status

Repository initialized October 1, 2026. Nationwide 2023â€“24 IPEDS reference data cover all 50 states and DC, with 5,920 distinct institution identities, 1,924 admissions records and 9,960 tuition/fee records. These are historical observations, not current prices. Original source archives/dictionaries, hashes, normalized records and automated validation are persisted.

A transactional development reference backend and explicit-year read API are runnable; see [backend instructions](docs/BACKEND.md). The designated CollegePrep Supabase project now contains all 17,865 source records, normalized reference tables and a private revision ledger. Counts and source fields were reconciled and repeated import was checked. Supabase advisors report no defects; the remaining notices are by design (signed-in users can call the household/practice RPCs, two server-only tables have no client policies) or informational indexing notes on still-empty tables. Public clients can read verified reference data but cannot edit it. Current institutional and state-policy coverage remains small; no institution or state is marked complete. Practice-question AI help remains in the product plan.

A household, student-account, subscription and ACT/SAT practice schema is live (migration `20261002183112`, deployed by `.github/workflows/deploy-migrations.yml`); see [household practice](docs/HOUSEHOLD_PRACTICE.md).

Coverage reports in `docs/coverage/` are the authoritative persisted-data counts.
