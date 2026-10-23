# Review queue — MO (2026-27)

Pages fetched: 90; failures: 1. Candidates: 3 (1 without issues, 2 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 10 | 0 | 0 | 0 | 1 | 0 | 60 |
| cost_of_attendance | 7 | 0 | 0 | 0 | 1 | 0 | 63 |
| admissions_tests | 0 | 0 | 0 | 0 | 1 | 0 | 70 |
| common_data_set | 0 | 0 | 0 | 0 | 1 | 0 | 70 |
| merit_scholarships | 5 | 4 | 0 | 0 | 1 | 0 | 61 |
| ap_credit | 0 | 6 | 0 | 0 | 0 | 1 | 64 |
| clep_credit | 1 | 5 | 0 | 0 | 0 | 1 | 64 |
| ib_credit | 0 | 4 | 0 | 0 | 0 | 1 | 66 |
| dual_enrollment | 2 | 15 | 0 | 0 | 0 | 0 | 54 |
| transfer_credit | 2 | 5 | 0 | 0 | 1 | 0 | 63 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 1 | 70 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 70 |
| degree_requirements | 3 | 0 | 0 | 0 | 1 | 0 | 67 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 0 | 70 |

## Ready for review (1)

### `m294dca6a74e057c` Saint Louis Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [changed] (labeled_in_source)
- source: https://stlcc.edu/docs/programs/dual-enrollment/dual-credit-student-handbook-09-01-26.pdf (sha256 09deaf690935)
- checks: {"fields": ["max_credit_hours_per_term", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 5}
- change dual_enrollment: `{'eligibility_tiers': [{'grades': [], 'line': 'Have a 2.6 GPA or higher.', 'min_hs_gpa': 2.6}, {'grades': ['10', '11', '12'], 'line': 'Have at least a 2.0 unweighted GPA.', 'min_hs_gpa': 2.0}, {'grades': ['10', '11', '12'], 'line': 'for high school sophomores, juniors and seniors with a 2.0 GPA or higher. To enroll,', 'min_hs_gpa': 2.0}, {'grades': ['11'], 'line': 'must be a junior with a minimum 2.0 GPA at the start of the program. This ensures', 'min_hs_gpa': 2.0}], 'per_credit_hour_charges': [{'amount': 25, 'kind': 'other', 'line': 'Save Money: Dual credit classes cost only $25 per credit hour. Most classes are around $75 total.'}, {'amount': 25, 'kind': 'other', 'line': '$25 per credit hour.'}]}` → `{'eligibility_tiers': [{'grades': [], 'min_hs_gpa': 2.6, 'line': 'Have a 2.6 GPA or higher.'}, {'grades': ['10', '11', '12'], 'min_hs_gpa': 2.0, 'line': 'Have at least a 2.0 unweighted GPA.'}, {'grades': ['10', '11', '12'], 'min_hs_gpa': 2.0, 'line': 'Students must be in 10th, 11th or 12th grade, with a cumulative, unweighted GPA of 2.0+ to be'}, {'grades': [], 'min_hs_gpa': 2.6, 'line': 'lunch eligible and who have a 2.6 GPA or higher. The scholarship covers up to 6 credit hours of', 'max_credit_hours_per_term': 6}, {'grades': [], 'min_hs_gpa': 2.5, 'line': 'Last year of high school English grades averaged A AND have a 2.5 GPA or higher'}, {'grades': [], 'min_hs_gpa': 2.6, 'line': 'GPA of 2.6 or higher and counselor grants written permission after reviewing all'}, {'grades': [], 'min_hs_gpa': 2.6, 'line': 'The Jump Start scholarship is automatically awarded to students who have a 2.6 GPA or'}, {'grades': ['10', '11', '12'], 'min_hs_gpa': 2.0, 'line': 'for high school sophomores, juniors and seniors with a 2.0 GPA or higher. To enroll,'}, {'grades': ['11'], 'min_hs_gpa': 2.0, 'line': 'must be a junior with a minimum 2.0 GPA at the start of the program. This ensures'}], 'max_credit_hours_per_term': 6, 'per_credit_hour_charges': [{'amount': 25, 'kind': 'other', 'line': 'Save Money: Dual credit classes cost only $25 per credit hour. Most classes are around $75 total.'}, {'amount': 25, 'kind': 'other', 'line': '$25 per credit hour.'}, {'amount': 25, 'kind': 'tuition', 'line': "At just $25/credit hour, STLCC's dual credit tuition"}, {'amount': 25, 'kind': 'other', 'line': 'STLCC dual credit courses cost $25 per credit hour. The MTH 140 course has a special price and'}, {'amount': 25, 'kind': 'other', 'line': 'Dual credit classes cost just $25 per credit hour. An average class is 3-4 credits, meaning your'}], 'tuition_per_credit_hour': 25}`
- change additional_source_urls: `['https://stlcc.edu/programs/high-school/dual-enrollment/']` → `['https://stlcc.edu/programs/high-school/dual-credit/', 'https://stlcc.edu/programs/high-school/dual-enrollment/']`
  - per_credit_hour_charge: 25 ⟵ “Save Money: Dual credit classes cost only $25 per credit hour. Most classes are around $75 total.”
  - per_credit_hour_charge: 25 ⟵ “$25 per credit hour.”
  - eligibility_tier: 2.6 ⟵ “Have a 2.6 GPA or higher.”
  - eligibility_tier: 2.0 ⟵ “Have at least a 2.0 unweighted GPA.”
  - per_credit_hour_charge: 25 ⟵ “At just $25/credit hour, STLCC's dual credit tuition”
  - eligibility_tier: 2.0 ⟵ “Students must be in 10th, 11th or 12th grade, with a cumulative, unweighted GPA of 2.0+ to be”
  - per_credit_hour_charge: 25 ⟵ “STLCC dual credit courses cost $25 per credit hour. The MTH 140 course has a special price and”
  - eligibility_tier: 2.6 ⟵ “lunch eligible and who have a 2.6 GPA or higher. The scholarship covers up to 6 credit hours of”
  - eligibility_tier: 2.5 ⟵ “Last year of high school English grades averaged A AND have a 2.5 GPA or higher”
  - eligibility_tier: 2.6 ⟵ “GPA of 2.6 or higher and counselor grants written permission after reviewing all”
  - eligibility_tier: 2.5 ⟵ “Last year of high school English grades averaged A AND have a 2.5 GPA or higher”
  - per_credit_hour_charge: 25 ⟵ “Dual credit classes cost just $25 per credit hour. An average class is 3-4 credits, meaning your”
  - eligibility_tier: 2.6 ⟵ “The Jump Start scholarship is automatically awarded to students who have a 2.6 GPA or”
  - max_credit_hours_per_term: 6 ⟵ “up to 6 credit hours ($150) for free each semester.”
  - eligibility_tier: 2.0 ⟵ “for high school sophomores, juniors and seniors with a 2.0 GPA or higher. To enroll,”
  - eligibility_tier: 2.0 ⟵ “must be a junior with a minimum 2.0 GPA at the start of the program. This ensures”
  - eligibility_tier: 2.0 ⟵ “Have at least a 2.0 unweighted GPA.”

## Exceptions (2)

### `2302f02c15a4c0b6` Saint Louis Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://stlcc.edu/docs/financial-aid/26-27-special-circumstances.pdf (sha256 f047e3fde2c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCES 2026-2027 ID # A Name (Last Name) (First Name) (MI) Special Circumstances Notices and Process: The Office of Enrollment Services (Financial Aid) at St.”
  - sentence: need_based_special_circumstances ⟵ “This form allows you to explain unusual circumstances and request a re-evaluation of financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “At any point, additional information can be requested. ▪ If it is determined that you are an eligible applicant with special circumstances, any adjustments made to determine eligibility are valid at this institution only.”
  - sentence: need_based_special_circumstances ⟵ “If you were approved for special circumstances at another institution, you must still submit information and documentation required by St.”
  - sentence: need_based_special_circumstances ⟵ “Department of Education. ▪ It is crucial that students continually check STLCC email for updates and communications regarding this application process. ▪ Special Circumstances approvals do not carry over year to year.”
  - sentence: need_based_special_circumstances ⟵ “If you have an appeal pending, the appeal must be approved first before the special circumstances are reviewed.”
### `a3fcbeb84896eef7` Saint Louis Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://stlcc.edu/docs/financial-aid/26-27-special-circumstances.pdf (sha256 f047e3fde2c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Student Signature Date Home or Cell Phone Number — OFFICE USE ONLY —  Professional Judgement Granted.”
  - sentence: professional_judgment ⟵ “Professional Judgement Denied.”

## Re-verification of existing records (72)

- source_not_fetched: data/institutions/calvary/transfer_policies/2026-27.json ["transfer_policies", "ipeds-176789", null, "2026-27", {}]
- source_not_fetched: data/institutions/cofo/credit_policies/2026-27.json ["credit_policies", "ipeds-178697", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/cofo/credit_policies/2026-27.json ["credit_policies", "ipeds-178697", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/ccis/credit_policies/2026-27.json ["credit_policies", "ipeds-177065", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/cottey/credit_policies/2026-27.json ["credit_policies", "ipeds-177117", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/cottey/credit_policies/2026-27.json ["credit_policies", "ipeds-177117", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/cottey/transfer_policies/2026-27.json ["transfer_policies", "ipeds-177117", null, "2026-27", {}]
- source_not_fetched: data/institutions/culver/credit_policies/2026-27.json ["credit_policies", "ipeds-177144", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/culver/transfer_policies/2026-27.json ["transfer_policies", "ipeds-177144", null, "2026-27", {}]
- source_not_fetched: data/institutions/eastcentral/credit_policies/2026-27.json ["credit_policies", "ipeds-177250", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/fontbonne/transfer_policies/2026-27.json ["transfer_policies", "ipeds-177418", null, "2026-27", {}]
- source_not_fetched: data/institutions/lincolnu/credit_policies/2026-27.json ["credit_policies", "ipeds-177940", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/lincolnu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-177940", null, "2026-27", {}]
- source_not_fetched: data/institutions/logan/awards/2026-27.json ["awards", "ipeds-177986", null, "2026-27", {"award_name": "President's Scholarship"}]
- source_not_fetched: data/institutions/logan/awards/2026-27.json ["awards", "ipeds-177986", null, "2026-27", {"award_name": "Tower Scholarship"}]
- source_not_fetched: data/institutions/logan/awards/2026-27.json ["awards", "ipeds-177986", null, "2026-27", {"award_name": "Dean's Scholarship"}]
- source_not_fetched: data/institutions/logan/awards/2026-27.json ["awards", "ipeds-177986", null, "2026-27", {"award_name": "Fountain Scholarship"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Big Red Scholarship"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Maryville Opportunity Award"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Presidential Scholarship*"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Keith Lovin Leadership Scholarship*"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "eSports"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Saints Scholarship"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Trustee Scholarship*"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Melissa Brickey Scholarship"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Design & Visual Art Scholarships**"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "FIRST Robotics Scholarship"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Cheer / Dance / Mascot"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Pep Band"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "Rugby (Men's & Women's)"}]
- source_not_fetched: data/institutions/maryville/awards/2026-27.json ["awards", "ipeds-178059", null, "2026-27", {"award_name": "STUNT"}]
- source_not_fetched: data/institutions/mcckc/credit_policies/2026-27.json ["credit_policies", "ipeds-177995", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/mcckc/credit_policies/2026-27.json ["credit_policies", "ipeds-177995", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/mcckc/credit_policies/2026-27.json ["credit_policies", "ipeds-177995", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/mineralarea/credit_policies/2026-27.json ["credit_policies", "ipeds-178217", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/mobap/credit_policies/2026-27.json ["credit_policies", "ipeds-178244", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/mobap/transfer_policies/2026-27.json ["transfer_policies", "ipeds-178244", null, "2026-27", {}]
- source_not_fetched: data/institutions/mssu/credit_policies/2026-27.json ["credit_policies", "ipeds-178341", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/mst/credit_policies/2026-27.json ["credit_policies", "ipeds-178411", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/mst/credit_policies/2026-27.json ["credit_policies", "ipeds-178411", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/mst/credit_policies/2026-27.json ["credit_policies", "ipeds-178411", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/mst/transfer_policies/2026-27.json ["transfer_policies", "ipeds-178411", null, "2026-27", {}]
- source_not_fetched: data/institutions/moval/credit_policies/2026-27.json ["credit_policies", "ipeds-178369", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/occ/credit_policies/2026-27.json ["credit_policies", "ipeds-178679", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/rockhurst/awards/2026-27.json ["awards", "ipeds-179043", null, "2026-27", {"award_name": "Presidential"}]
- source_not_fetched: data/institutions/rockhurst/awards/2026-27.json ["awards", "ipeds-179043", null, "2026-27", {"award_name": "Provost"}]
- source_not_fetched: data/institutions/rockhurst/awards/2026-27.json ["awards", "ipeds-179043", null, "2026-27", {"award_name": "Deans"}]
- source_not_fetched: data/institutions/rockhurst/awards/2026-27.json ["awards", "ipeds-179043", null, "2026-27", {"award_name": "Wisdom"}]
- source_not_fetched: data/institutions/rockhurst/awards/2026-27.json ["awards", "ipeds-179043", null, "2026-27", {"award_name": "Achievement"}]
- source_not_fetched: data/institutions/rockhurst/credit_policies/2026-27.json ["credit_policies", "ipeds-179043", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/rockhurst/transfer_policies/2026-27.json ["transfer_policies", "ipeds-179043", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/stlcc/credit_policies/2026-27.json ["credit_policies", "ipeds-179308", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/slu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-179159", null, "2026-27", {"program_key": "project-management-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/slu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-179159", null, "2026-27", {"program_key": "civil-engineering-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/semo/credit_policies/2026-27.json ["credit_policies", "ipeds-179557", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/semo/credit_policies/2026-27.json ["credit_policies", "ipeds-179557", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/semo/credit_policies/2026-27.json ["credit_policies", "ipeds-179557", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/sbuniv/credit_policies/2026-27.json ["credit_policies", "ipeds-179326", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/sbuniv/transfer_policies/2026-27.json ["transfer_policies", "ipeds-179326", null, "2026-27", {}]
- source_not_fetched: data/institutions/stchas/credit_policies/2026-27.json ["credit_policies", "ipeds-262031", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/trcc/credit_policies/2026-27.json ["credit_policies", "ipeds-179645", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/truman/awards/2026-27.json ["awards", "ipeds-178615", null, "2026-27", {"award_name": "General John J. Pershing Scholarship"}]
- source_not_fetched: data/institutions/truman/awards/2026-27.json ["awards", "ipeds-178615", null, "2026-27", {"award_name": "President John R. Kirk Scholarship"}]
- source_not_fetched: data/institutions/truman/transfer_policies/2026-27.json ["transfer_policies", "ipeds-178615", null, "2026-27", {}]
- source_not_fetched: data/institutions/umsl/credit_policies/2026-27.json ["credit_policies", "ipeds-178420", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/umsl/credit_policies/2026-27.json ["credit_policies", "ipeds-178420", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/umsl/credit_policies/2026-27.json ["credit_policies", "ipeds-178420", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/jewell/awards/2026-27.json ["awards", "ipeds-179955", null, "2026-27", {"award_name": "Jewell Scholar"}]
- source_not_fetched: data/institutions/jewell/awards/2026-27.json ["awards", "ipeds-179955", null, "2026-27", {"award_name": "Trustee Scholar"}]
- source_not_fetched: data/institutions/jewell/awards/2026-27.json ["awards", "ipeds-179955", null, "2026-27", {"award_name": "Presidential Scholar"}]
- source_not_fetched: data/institutions/jewell/awards/2026-27.json ["awards", "ipeds-179955", null, "2026-27", {"award_name": "First-Year Academic Scholarships: Score ACT 24-27 / SAT 1160-1290"}]
- source_not_fetched: data/institutions/jewell/awards/2026-27.json ["awards", "ipeds-179955", null, "2026-27", {"award_name": "First-Year Academic Scholarships: Score ACT 28+ / SAT 1300+"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Saint Louis Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency, degree_requirements
