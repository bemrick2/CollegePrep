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

Repository initialized October 1, 2026. National coverage is being built and verified incrementally. Coverage reports in `docs/coverage/` should be treated as the authoritative progress record.
