# Review queue — DE (2026-27)

Pages fetched: 90; failures: 22. Candidates: 1 (1 without issues, 0 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| cost_of_attendance | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| admissions_tests | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 1 | 5 |
| merit_scholarships | 0 | 1 | 0 | 0 | 1 | 0 | 4 |
| ap_credit | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| clep_credit | 0 | 0 | 0 | 0 | 0 | 1 | 5 |
| ib_credit | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| dual_enrollment | 0 | 2 | 0 | 0 | 0 | 0 | 4 |
| transfer_credit | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| statewide_articulation | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| degree_requirements | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| aid_appeals | 0 | 0 | 0 | 0 | 0 | 1 | 5 |

## Ready for review (1)

### `m35fe1ff83da96c4` University of Delaware — credit_policies 2026-27 · policy_kind=dual_enrollment [changed] (source_unlabeled)
- source: https://www.pcs.udel.edu/early-college-credit-program/ (sha256 ea0e06b2c8f9)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 4, "tiers": 1}
- change dual_enrollment: `{'eligibility_tiers': [{'grades': [], 'line': 'a high school grade point average of 3.6 or above', 'min_hs_gpa': 3.6}], 'min_hs_gpa': 3.6}` → `{'eligibility_tiers': [{'grades': [], 'min_hs_gpa': 3.6, 'line': 'a high school grade point average of 3.6 or above'}, {'grades': ['11', '12'], 'min_hs_gpa': 2.8, 'line': 'Have a 2.8 GPA or higher'}]}`
  - eligibility_tier: 3.6 ⟵ “a high school grade point average of 3.6 or above”
  - eligibility_tier: 2.8 ⟵ “Have a 2.8 GPA or higher”
  - eligibility_tier: 3.6 ⟵ “a high school grade point average of 3.6 or above”
  - eligibility_tier: 3.6 ⟵ “a high school grade point average of 3.6 or above”

## Exceptions (0)


## Re-verification of existing records (27)

- source_not_fetched: data/institutions/desu/credit_policies/2026-27.json ["credit_policies", "ipeds-130934", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/udel/credit_policies/2026-27.json ["credit_policies", "ipeds-130943", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Wilmington University Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "College of Education & Liberal Arts Dean's Merit Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "College of Business & Technology Dean's Merit Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "College of Sciences & Engineering Dean's Merit Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "College of Social & Behavioral Sciences Dean's Merit Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "College of Nursing & Health Sciences Dean's Merit Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "William and Mary Bescherer Memorial Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "STAR Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "AmeriCorps Matching Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Aspiring Teachers Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Quinn Family Memorial Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Dr. Stephanie Battis Memorial Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Mig Reardon Memorial Nursing Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Linda Thomas Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Phi Theta Kappa (PTK) Recognition Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Wilmington Manor Lions Club Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Bettye J. and Ralph E. Bailey Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Sandra L. and Thomas S. Shaw Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Future of Nursing Excellence Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Dr. Jack P. Varsalona Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "STEP Path\u2122 Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Career-Based Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Educator Support Scholarship"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Scholarship Incentive Program"}]
- source_not_fetched: data/institutions/wilmu/awards/2026-27.json ["awards", "ipeds-131113", null, "2026-27", {"award_name": "Neighborhood Scholarship"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- University of Delaware: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
