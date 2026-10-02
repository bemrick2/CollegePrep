# Data model

The backend is normalized around institutions, time-sensitive policy records, and source provenance.

## Core identity

**institutions** stores stable school identity and basic URLs. IPEDS UNITID is the preferred external identifier for U.S. institutions when available.

## Time-sensitive records

The following tables are versioned by academic year or entering class year rather than overwritten:

- institution_costs
- admissions_metrics
- state_aid_programs
- institutional_awards
- credit_policies / credit_equivalencies
- transfer_policies
- appeal_policies

This lets the recommendation engine distinguish a current rule from a prior-year rule and makes annual refreshes auditable.

## Provenance

Every policy-bearing row points to **sources**. A source records the canonical URL, publisher, authority level, retrieval time, and where possible the effective date / academic year.

The app should never silently convert an unverified record into a verified one.

## Verification states

- **verified** — checked against an authoritative source and current for the stated period.
- **partially_verified** — some fields are confirmed, but the record still contains unresolved items.
- **unverified** — imported or staged, not yet source-checked.
- **stale** — once-current information that is beyond the refresh window.
- **not_applicable** — intentionally not relevant.

## Negotiation / appeal add-on rule

The database exposes `institution_negotiation_addon_eligibility`.

The paid negotiation/reconsideration feature is available only if the school has a **verified**, documented and offered route of one of these kinds:

- merit reconsideration
- competing-offer review
- financial-aid appeal

A generic federal professional-judgment/special-circumstances process by itself does **not** automatically qualify the school for the paid negotiation add-on.

The migration requires `qualifies_for_paid_addon`, `qualifying_path_evidence`, matching academic year and verification within 365 days. The replacement gate is `institution_negotiation_addon_eligibility_by_year`. A missing row means ineligible. The legacy unscoped view fails closed. Disposable PostgreSQL gate and permission tests pass in CI; production deployment and Supabase advisor checks remain blocked on a designated CollegePrep database.

## Practice-question AI help

Practice content is separated into blueprints by exam family, subject, domain, skill, and difficulty. The UI can place an AI-help action beside a question, but help should teach the concept and reasoning rather than simply disclose the answer by default.

## Annual refresh

Annual refresh jobs should update current records and retain history. The minimum refreshed domains are:

1. tuition/fees and cost of attendance
2. admissions metrics
3. state aid and deadlines
4. institutional merit awards
5. AP/CLEP/IB/dual-enrollment credit policies
6. transfer/residency rules
7. degree/catalog requirements
8. appeal/reconsideration policies
