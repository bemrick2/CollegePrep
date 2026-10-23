# Review queue — RI (2026-27)

Pages fetched: 90; failures: 2. Candidates: 5 (2 without issues, 3 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 4 | 0 | 0 | 1 | 0 | 0 | 8 |
| cost_of_attendance | 1 | 0 | 0 | 0 | 1 | 0 | 11 |
| admissions_tests | 1 | 0 | 0 | 0 | 0 | 0 | 12 |
| common_data_set | 1 | 0 | 0 | 0 | 0 | 0 | 12 |
| merit_scholarships | 0 | 0 | 0 | 0 | 1 | 0 | 12 |
| ap_credit | 0 | 0 | 0 | 0 | 1 | 0 | 12 |
| clep_credit | 0 | 0 | 0 | 0 | 1 | 0 | 12 |
| ib_credit | 0 | 0 | 0 | 0 | 0 | 1 | 12 |
| dual_enrollment | 1 | 1 | 0 | 0 | 1 | 0 | 10 |
| transfer_credit | 1 | 5 | 0 | 0 | 0 | 0 | 7 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 1 | 12 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 12 |
| degree_requirements | 1 | 0 | 0 | 0 | 1 | 0 | 11 |
| aid_appeals | 0 | 0 | 0 | 0 | 1 | 0 | 12 |

## Ready for review (2)

### `a915deefbfe79a2f` University of Rhode Island — admissions_metrics 2025-26 [same] (labeled_in_source)
- source: https://web.uri.edu/ir/wp-content/uploads/sites/276/CDS-PDF-2025-2026_fillablePDF.pdf (sha256 21bd459ce8a5)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 28021 ⟵ “Total first-time, first-year (degree-seeking) who applied           4368     23100            553                 0   28021”
  - admits: 20892 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     3179     17302            411                 0   20892”
  - enrolled: 3431 ⟵ “Total first-time, first-year (degree-seeking) enrolled              1284        2113           34                 0   3431”
  - sat_composite_25..75: [1090, 1210, 1310] ⟵ “SAT Composite                     1090                      1210                       1310”
  - sat_math_25..75: [520, 590, 645] ⟵ “SAT Math                           520                       590                       645”
  - act_25..75: [25, 28, 31] ⟵ “ACT Composite                      25                        28                         31”
### `1c3856dba5990249` University of Rhode Island — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://web.uri.edu/admission/transfer/transfer-resources/ (sha256 3d2dd161b39c)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “You will need to earn a grade of “C” or better in order for a class to be considered for transfer.”

## Exceptions (3)

### `63190f917d968c98` University of Rhode Island — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://web.uri.edu/ir/wp-content/uploads/sites/276/CDS-2024-2025-fillable.pdf (sha256 1c923b2db732)
- issues: stale_year_label:2024-25
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 26987 ⟵ “Total first-time, first-year (degree-seeking) who applied          4410      22040            537                  26987”
  - admits: 19475 ⟵ “Total first-time, first-year (degree-seeking) who were admitted    3289      15824            362                  19475”
  - enrolled: 2995 ⟵ “Total first-time, first-year (degree-seeking) enrolled             1287         1679           29                  2995”
  - sat_composite_25..75: [1020, 1170, 1260] ⟵ “SAT Composite                     1020                      1170                       1260”
  - sat_math_25..75: [500, 570, 630] ⟵ “SAT Math                           500                       570                       630”
### `dd522f941dee5bc8` University of Rhode Island — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://web.uri.edu/tuition-billing/annual-undergraduate-tuition-and-fees-2024-25/ (sha256 13355c53c85a)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": true, "rows": 3}
  - column:Tuition: 14630 ⟵ “Tuition | $14,630 | $34,834 | $25,604”
  - column:Required Fees: 2312 ⟵ “Required Fees | $2,312 | $2,312 | $2,312”
  - column:Total: 16942 ⟵ “Total | $16,942 | $37,146 | $27,916”
  - column:Tuition: 34834 ⟵ “Tuition | $14,630 | $34,834 | $25,604”
  - column:Required Fees: 2312 ⟵ “Required Fees | $2,312 | $2,312 | $2,312”
  - column:Total: 37146 ⟵ “Total | $16,942 | $37,146 | $27,916”
  - column:Tuition: 25604 ⟵ “Tuition | $14,630 | $34,834 | $25,604”
  - column:Required Fees: 2312 ⟵ “Required Fees | $2,312 | $2,312 | $2,312”
  - column:Total: 27916 ⟵ “Total | $16,942 | $37,146 | $27,916”
### `f6da6fac986e9049` University of Rhode Island — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://web.uri.edu/admission/regional-tuition-majors/ (sha256 f19bc28d0bfa)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees:: 29844 ⟵ “Tuition and Fees: | $29,844”
  - column:Housing and Food:: 16704 ⟵ “Housing and Food: | $16,704”
  - column:Total:: 46548 ⟵ “Total: | $46,548*”

## Re-verification of existing records (6)

- source_not_fetched: data/institutions/bryant/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217165", null, "2026-27", {}]
- source_not_fetched: data/institutions/ccri/credit_policies/2026-27.json ["credit_policies", "ipeds-217475", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ric/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217420", null, "2026-27", {}]
- source_not_fetched: data/institutions/risd/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217493", null, "2026-27", {}]
- source_not_fetched: data/institutions/salve/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217536", null, "2026-27", {}]
- nothing_to_check: data/institutions/uri/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217484", null, "2026-27", {}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- University of Rhode Island: cost_of_attendance, merit_scholarships, ap_credit, clep_credit, dual_enrollment, residency, degree_requirements, aid_appeals
