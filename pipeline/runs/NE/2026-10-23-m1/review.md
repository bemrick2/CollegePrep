# Review queue — NE (2026-27)

Pages fetched: 90; failures: 2. Candidates: 10 (2 without issues, 8 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 4 | 0 | 0 | 0 | 0 | 0 | 27 |
| cost_of_attendance | 3 | 0 | 0 | 0 | 0 | 0 | 28 |
| admissions_tests | 0 | 0 | 0 | 0 | 1 | 0 | 30 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 1 | 30 |
| merit_scholarships | 0 | 4 | 0 | 0 | 1 | 0 | 26 |
| ap_credit | 0 | 3 | 0 | 0 | 0 | 1 | 27 |
| clep_credit | 0 | 2 | 0 | 0 | 0 | 1 | 28 |
| ib_credit | 0 | 1 | 0 | 0 | 0 | 1 | 29 |
| dual_enrollment | 1 | 3 | 0 | 0 | 1 | 0 | 26 |
| transfer_credit | 2 | 4 | 0 | 0 | 1 | 0 | 24 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 1 | 30 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 30 |
| degree_requirements | 4 | 0 | 0 | 0 | 0 | 0 | 27 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 0 | 30 |

## Ready for review (2)

### `104d6cb255acdac0` University of Nebraska-Lincoln — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/2026-2027/ (sha256 77f3d5ce6c64)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 11472 ⟵ “Tuition & Fees | $11,472 | $31,542”
  - on_campus:Housing & Food: 13950 ⟵ “Housing & Food | $13,950 | $13,950”
  - on_campus:Books & Supplies: 1128 ⟵ “Books & Supplies | $1,128 | $1,128”
  - on_campus:Personal Expenses: 2324 ⟵ “Personal Expenses | $2,324 | $2,324”
  - on_campus:Loan Fees (if applicable): 64 ⟵ “Loan Fees (if applicable) | $64 | $64”
  - on_campus:Total: 28938 ⟵ “Total | $28,938 | $49,008”
### `cffd3f47b87a32a4` University of Nebraska-Lincoln — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/2026-2027/ (sha256 77f3d5ce6c64)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 31542 ⟵ “Tuition & Fees | $11,472 | $31,542”
  - on_campus:Housing & Food: 13950 ⟵ “Housing & Food | $13,950 | $13,950”
  - on_campus:Books & Supplies: 1128 ⟵ “Books & Supplies | $1,128 | $1,128”
  - on_campus:Personal Expenses: 2324 ⟵ “Personal Expenses | $2,324 | $2,324”
  - on_campus:Loan Fees (if applicable): 64 ⟵ “Loan Fees (if applicable) | $64 | $64”
  - on_campus:Total: 49008 ⟵ “Total | $28,938 | $49,008”

## Exceptions (8)

### `51c15b4073bdc406` University of Nebraska-Lincoln — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.unl.edu/additional-information/scholarship-appeals/ (sha256 41462a4021a3)
- issues: semantic_review_required, conflicting_sources:https://admissions.unl.edu/cost/financial-aid/guide-to-your-offer/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Who May Request Scholarship Reconsideration Incoming Students You may request a scholarship reconsideration if you experienced significant or unusual circumstances that affected your academic performance or your ability to be fully considered during the selection process.”
### `744acccfe7c77804` University of Nebraska-Lincoln — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.unl.edu/maintaining-eligibility/scholarship-guidelines/ (sha256 e8492a1fc9c2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If your scholarship is not renewed, visit the Scholarships Appeals page to learn about appeal options.”
### `74c3693cadfa06ba` University of Nebraska-Lincoln — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.unl.edu/cost/financial-aid/guide-to-your-offer/ (sha256 1e8435e94fef)
- issues: semantic_review_required, conflicting_sources:https://financialaid.unl.edu/additional-information/scholarship-appeals/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Let Husker Hub know if you experience a sudden change in income or expenses.”
  - sentence: need_based_special_circumstances ⟵ “We may be able to reassess your family's aid eligibility in the event of a special and unusual circumstance, such as loss of income, divorce, death in the family, layoff, etc.”
### `9122329388b1ac3a` University of Nebraska-Lincoln — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.unl.edu/maintaining-eligibility/satisfactory-academic-progress/ (sha256 77f2eaed515b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 15}
  - sentence: sap_appeal ⟵ “SAP Appeal Forms [1] Financial aid includes, but is not limited to, all federal grants, loans and work-study; state grants; and most University of Nebraska need-based grants and scholarships.”
  - sentence: sap_appeal ⟵ “Students who drop or withdraw from courses while on a SAP approved appeal (SAP Academic Plan) may lose their financial aid eligibility in subsequent semesters.”
  - sentence: sap_appeal ⟵ “Should students who are on a SAP approved appeal (SAP Academic Plan) earn an incomplete, they may be in jeopardy of losing financial aid eligibility in subsequent semesters.”
  - sentence: sap_appeal ⟵ “If however, you may have over 90 transfer credit hours and you have been notified that you are not meeting SAP as you have exceeded the maximum time frame allowed, you may want to check with your student services specialist at Husker Hub to learn if a SAP appeal is possible.”
  - sentence: sap_appeal ⟵ “Appeal Process When students are notified that they do not meet the satisfactory academic progress policy requirements, they have the right to appeal that decision.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Committee reviews the appeal and makes the decision to approve or deny the appeal.”
### `c14265461a92dbfc` University of Nebraska-Lincoln — appeals 2025-26 [new] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/ (sha256 83e2ed2dcb73)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If your actual costs exceed the standard COA, for example, due to dependent care, disability-related expenses, study abroad, or cooperative education, you may request an adjustment through a professional judgment review.”
### `6066ba0bbc31f4bf` University of Nebraska-Lincoln — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://admissions.unl.edu/information-for/nebraska-now/ (sha256 7bb7f3b893bd)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Junior Year Fall:: 543 ⟵ “Junior Year Fall: | $543”
  - column:Junior Year Spring:: 543 ⟵ “Junior Year Spring: | $543”
  - column:Senior Year Fall:: 543 ⟵ “Senior Year Fall: | $543”
  - column:Senior Year Spring:: 543 ⟵ “Senior Year Spring: | $543”
  - column:Tuition Savings:: 2172 ⟵ “Tuition Savings: | $2,172”
### `7493cf9c6d5f22de` University of Nebraska-Lincoln — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/2025-2026/ (sha256 01c4b38d3821)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 11100 ⟵ “Tuition & Fees | $11,100 | $30,330”
  - on_campus:Housing & Food: 14210 ⟵ “Housing & Food | $14,210 | $14,210”
  - on_campus:Books & Supplies: 1128 ⟵ “Books & Supplies | $1,128 | $1,128”
  - on_campus:Personal Expenses: 2300 ⟵ “Personal Expenses | $2,300 | $2,300”
  - on_campus:Loan Fees (if applicable): 64 ⟵ “Loan Fees (if applicable) | $64 | $64”
  - on_campus:Total: 28802 ⟵ “Total | $28,802 | $48,032”
### `e892ff07baefba5d` University of Nebraska-Lincoln — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/2025-2026/ (sha256 01c4b38d3821)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 30330 ⟵ “Tuition & Fees | $11,100 | $30,330”
  - on_campus:Housing & Food: 14210 ⟵ “Housing & Food | $14,210 | $14,210”
  - on_campus:Books & Supplies: 1128 ⟵ “Books & Supplies | $1,128 | $1,128”
  - on_campus:Personal Expenses: 2300 ⟵ “Personal Expenses | $2,300 | $2,300”
  - on_campus:Loan Fees (if applicable): 64 ⟵ “Loan Fees (if applicable) | $64 | $64”
  - on_campus:Total: 48032 ⟵ “Total | $28,802 | $48,032”

## Re-verification of existing records (55)

- source_not_fetched: data/institutions/csc/awards/2026-27.json ["awards", "ipeds-180948", null, "2026-27", {"award_name": "President Scholars"}]
- source_not_fetched: data/institutions/csc/awards/2026-27.json ["awards", "ipeds-180948", null, "2026-27", {"award_name": "Eagle Scholars"}]
- source_not_fetched: data/institutions/csc/awards/2026-27.json ["awards", "ipeds-180948", null, "2026-27", {"award_name": "Dean Scholars"}]
- source_not_fetched: data/institutions/csc/awards/2026-27.json ["awards", "ipeds-180948", null, "2026-27", {"award_name": "Community Scholars"}]
- source_not_fetched: data/institutions/csc/awards/2026-27.json ["awards", "ipeds-180948", null, "2026-27", {"award_name": "Innovative Transfer Scholars"}]
- source_not_fetched: data/institutions/csc/credit_policies/2026-27.json ["credit_policies", "ipeds-180948", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/clarksoncollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-180832", null, "2026-27", {}]
- source_not_fetched: data/institutions/cune/credit_policies/2026-27.json ["credit_policies", "ipeds-180984", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/cune/transfer_policies/2026-27.json ["transfer_policies", "ipeds-180984", null, "2026-27", {}]
- source_not_fetched: data/institutions/creighton/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181002", null, "2026-27", {"program_key": "physics-b-s-phy", "requirement_key": "major-2-course-requirements"}]
- source_not_fetched: data/institutions/hastings/awards/2026-27.json ["awards", "ipeds-181127", null, "2026-27", {"award_name": "Crimson"}]
- source_not_fetched: data/institutions/hastings/awards/2026-27.json ["awards", "ipeds-181127", null, "2026-27", {"award_name": "Ambassador"}]
- source_not_fetched: data/institutions/hastings/awards/2026-27.json ["awards", "ipeds-181127", null, "2026-27", {"award_name": "Ringland"}]
- source_not_fetched: data/institutions/hastings/awards/2026-27.json ["awards", "ipeds-181127", null, "2026-27", {"award_name": "Pro Rege"}]
- source_not_fetched: data/institutions/hastings/awards/2026-27.json ["awards", "ipeds-181127", null, "2026-27", {"award_name": "Student Success"}]
- source_not_fetched: data/institutions/mccneb/credit_policies/2026-27.json ["credit_policies", "ipeds-181303", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/mccneb/credit_policies/2026-27.json ["credit_policies", "ipeds-181303", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/mpcc/credit_policies/2026-27.json ["credit_policies", "ipeds-181312", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/ncta/credit_policies/2026-27.json ["credit_policies", "ipeds-181765", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Presidents"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Black & Gold"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Archway"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Wesleyan Honors Academy Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Alumni Legacy Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Great Plains United Methodist Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "TeamMates Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "College Possible"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Upward Bound"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Huge-NWU Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Theatre Scholarships"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "Music Ensemble Participation Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "The Bennett Music Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "The Fosbury Music Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "The Harrod Music Scholarship"}]
- source_not_fetched: data/institutions/nebrwesleyan/awards/2026-27.json ["awards", "ipeds-181446", null, "2026-27", {"award_name": "The Marshall Music Scholarship"}]
- source_not_fetched: data/institutions/unomaha/credit_policies/2026-27.json ["credit_policies", "ipeds-181394", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/unomaha/credit_policies/2026-27.json ["credit_policies", "ipeds-181394", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/unomaha/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181394", null, "2026-27", {"program_key": "biomechanics-bachelor-of-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/unomaha/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181394", null, "2026-27", {"program_key": "creative-writing-bachelor-of-fine-arts", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/unomaha/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181394", null, "2026-27", {"program_key": "criminology-criminal-justice-bachelor-of-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/unomaha/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181394", null, "2026-27", {"program_key": "emergency-management-bsem-bachelor-of-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/unomaha/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181394", null, "2026-27", {"program_key": "kinesiology-bachelor-of-science-in-kinesiology", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/unomaha/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181394", null, "2026-27", {"program_key": "public-health-bachelor-of-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/unomaha/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181394", null, "2026-27", {"program_key": "social-work-bachelor-of-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/unomaha/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181394", null, "2026-27", {"program_key": "computer-engineering-bachelor-of-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/unomaha/transfer_policies/2026-27.json ["transfer_policies", "ipeds-181394", null, "2026-27", {}]
- source_not_fetched: data/institutions/admissions/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181464", null, "2026-27", {"program_key": "computer-engineering-bachelor-of-science-in-computer-engineering", "requirement_key": "plan"}]
- source_not_fetched: data/institutions/admissions/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181464", null, "2026-27", {"program_key": "computer-science-bachelor-of-science-in-computer-science", "requirement_key": "plan"}]
- source_not_fetched: data/institutions/admissions/degree_requirements/2026-27.json ["degree_requirements", "ipeds-181464", null, "2026-27", {"program_key": "software-engineering-bachelor-of-science", "requirement_key": "plan"}]
- source_not_fetched: data/institutions/wsc/credit_policies/2026-27.json ["credit_policies", "ipeds-181783", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/wsc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-181783", null, "2026-27", {}]
- source_not_fetched: data/institutions/york/awards/2026-27.json ["awards", "ipeds-181853", null, "2026-27", {"award_name": "Academic Scholarships: Trustees Scholarship(GPA 3.75+/ACT 33-36/SAT 1490-1600)"}]
- source_not_fetched: data/institutions/york/awards/2026-27.json ["awards", "ipeds-181853", null, "2026-27", {"award_name": "Academic Scholarships: Larsen Scholarship(GPA 3.50-3.74/ACT 30-32/SAT 1390-1480)"}]
- source_not_fetched: data/institutions/york/awards/2026-27.json ["awards", "ipeds-181853", null, "2026-27", {"award_name": "Academic Scholarships: \u200bChildress Scholarship(GPA 3.25-3.49/ACT 27-29/SAT 1280-1380)"}]
- source_not_fetched: data/institutions/york/awards/2026-27.json ["awards", "ipeds-181853", null, "2026-27", {"award_name": "Academic Scholarships: York Scholarship(GPA 3.00-3.24/ACT 24-26/SAT 1160-1270)"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- University of Nebraska-Lincoln: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
