# Tennessee state aid and UT Knoxville research — October 2, 2026

Official-source review of Tennessee state aid programs and University of Tennessee, Knoxville (UNITID 221759) policy data. The evidence manifest, which lists every URL, how it was read and whether it prints an academic year, is at [`sources/official/2026-10-02/evidence.json`](../../sources/official/2026-10-02/evidence.json). No live database, backend code, migration or shared validator was changed.

## How values were handled

- Only THEC/College for TN, tn.gov, UT Knoxville (One Stop, Admissions, IRSA Common Data Set, Undergraduate Catalog) sources were used.
- When a page prints no academic year, the record says so with `academic_year_basis: aid_year_in_force_at_review_source_unlabeled`. New records of this kind are `partially_verified`. The five Tennessee records that were already `verified` stay verified, because the importer refuses verified-to-weaker replacements. Their year label carries the same caveat.
- Recurring deadlines without a printed calendar year are stored as month-day values (`term_deadlines[].deadline_month_day`), not dated.
- Totals are copied as published and never recomputed from components. Missing totals stay null. This applies to off-campus COA and with-family COA.
- Earlier-year records are kept: the 2023-24 IPEDS rows for UT are untouched, and the 2025-26 catalog transfer rules are a separate record.

## Tennessee state aid

| Year | Records | Status |
|---|---|---|
| 2026-27 | HOPE, Aspire, GAMS, Wilder-Naifeh (re-verified, now with renewal rules and term deadlines) | verified |
| 2026-27 | Nontraditional HOPE, HOPE Foster Child Tuition Grant, Dual Enrollment Grant, TSAA, Tennessee Reconnect, TCAT Reconnect, Helping Heroes, Ned McWherter Scholars, Dependent Children, STEP UP, Middle College, Future Teacher | partially_verified |
| 2027 entering class | Tennessee Promise (Class of 2027: application Nov 2, 2026; FAFSA Apr 1, 2027) | verified |
| 2027-28 | HOPE, Aspire, GAMS, TSAA, Wilder-Naifeh from THEC's Class of 2027 senior guide | partially_verified |

Not inventoried: Graduate Nursing Loan Forgiveness and the Reduction in Force Tuition Assistance Benefit, which are outside undergraduate planning. HOPE Access Grant is also excluded. THEC's TELS summary says it was eliminated and closed to new applicants in fall 2021.

## UT Knoxville

| Domain | Records | Key facts |
|---|---|---|
| Costs 2026-27 | 2 (in-state, out-of-state) | Tuition $11,560 / $31,672. Fees $2,464 / $2,806. On-campus COA $36,994 / $57,448. Off-campus COA $39,494 / $58,938 as published. With-family components from CDS G5, no total. |
| Admissions | Fall 2025 enrolled cohort (CDS 2025-26). Fall 2026 admitted profile. | 53,841 applied, 23,464 admitted, 7,143 enrolled. ACT 26/29/31. SAT 1280/1330/1380. Fall 2026: 27,864 admits, admitted ACT mid-50% 28-32. |
| Merit/institutional awards 2026-27 | 15 | Chancellor's (Tennessee, Neyland, Bonham, Roddy, Manning), In-/Out-of-State Volunteer, Orange & White, Provost, Distinguished Tennessean, Next Chapter (2), UT Promise, Tennessee Pledge, Flagship. Each includes its retention rule where one is published. |
| Prior-learning credit | AP, CLEP, IB, Cambridge, Statewide Dual Credit, industry certification | 187 equivalencies, with admit-term conditions kept. |
| Dual enrollment | 1 | Taken at UT: counts in the UT GPA and is not transfer credit. Taken elsewhere: transfer credit, not in the UT GPA. |
| Transfer/residence | 2026-27 (partially_verified). 2025-26 (verified, history). | Minimum grade D-. 15 of the final 30 hours and 25% of hours at UT (2026-27). 2025-26 rule was 60 hours at a senior college plus the last 30 in residence. |
| Degree requirements | Computer Science Major, BS in Computer Science (2026-27 catalog) | 121-123 hours, C or better in CS/ECE/EE/math, uTrack milestones, eight-term plan. |
| Appeals 2026-27 | 8 | Financial-aid hub, special circumstances, scholarship retention, budget increase, dependency, SAP, merit reconsideration (not offered), competing-offer review (not offered). |

### Paid negotiation add-on

The add-on is still **ineligible**. The official Scholarship FAQ says: "UT cannot match scholarship or aid offers from other institutions." Every published appeal is a retention, SAP, dependency, budget or professional-judgment route. None of them is treated as evidence of incoming merit negotiation, and every appeal record has `qualifies_for_paid_addon: false`.

## Unresolved items

1. **TSAA SAI threshold.** The undated program page says SAI ≤ 5000. THEC's Class of 2027 guide says SAI ≤ 3500. The 2026-27 threshold is not independently labeled.
2. **Unlabeled Tennessee program pages.** No College for TN program page prints its aid year except Promise and Future Teacher. A THEC-labeled 2026-27 award schedule would allow these to be upgraded.
3. **Out-of-State Volunteer deadline.** The official page header says December 15, but the body says January 15.
4. **Off-campus COA arithmetic.** The published off-campus totals ($39,494 / $58,938) do not equal the on-campus total with the $12,600 housing estimate substituted ($40,022 / $60,476). The published figures are stored and components are not re-summed.
5. **With-family COA.** UT publishes no total, so only the CDS G5 components are stored.
6. **Transfer residence conflict.** The undated admissions page still says the last 30 hours at UT and the last 60 at a four-year school. The 2026-27 catalog says 15 of the final 30 plus 25%. The record is `partially_verified`.
7. **Maximum transferable hours.** Not stated in the 2026-27 catalog or CDS D13/D14, so it stays null.
8. **Fall 2026 enrolled-class metrics.** Not yet published (expected in CDS 2026-27).
9. **Merit amounts for Fall 2027 entrants.** UT pages give 2026-27 amounts but Fall 2027 application windows. 2027-28 amounts are unpublished.
10. **Manning Scholars amount** and the **Next Chapter retention rules** were not published or captured.
11. **Lower-confidence reading.** Several Tennessee pages and the Fall 2026 release summary were read through a summarizing fetcher (see `method` in the manifest). They should be re-read verbatim before those records are upgraded.
12. **Importer mapping.** `scripts/import_supabase.py` stops with "Domain needs an explicit normalized mapping: degree_requirements". The new degree record, and the unmapped nested fields (term deadlines, living arrangements, award tiers, residency rules), are not live-importable until backend mappings are added. That backend work was out of scope.
