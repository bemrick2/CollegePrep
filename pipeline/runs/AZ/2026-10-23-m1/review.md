# Review queue — AZ (2026-27)

Pages fetched: 270; failures: 6. Candidates: 30 (0 without issues, 30 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 1 | 0 | 0 | 1 | 2 | 0 | 28 |
| cost_of_attendance | 1 | 0 | 0 | 3 | 0 | 0 | 28 |
| admissions_tests | 0 | 0 | 0 | 0 | 3 | 0 | 29 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 3 | 29 |
| merit_scholarships | 1 | 1 | 0 | 0 | 3 | 0 | 27 |
| ap_credit | 0 | 0 | 0 | 0 | 2 | 1 | 29 |
| clep_credit | 0 | 0 | 0 | 0 | 2 | 1 | 29 |
| ib_credit | 0 | 0 | 0 | 0 | 2 | 1 | 29 |
| dual_enrollment | 0 | 3 | 0 | 0 | 2 | 1 | 26 |
| transfer_credit | 0 | 2 | 0 | 2 | 1 | 0 | 27 |
| statewide_articulation | 0 | 0 | 0 | 0 | 2 | 1 | 29 |
| residency | 0 | 0 | 0 | 0 | 3 | 0 | 29 |
| degree_requirements | 0 | 0 | 0 | 0 | 3 | 0 | 29 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 2 | 29 |

## Ready for review (0)


## Exceptions (30)

### `42e361cc8910b85b` Arizona State University Campus Immersion — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admission.asu.edu/cost-aid/non-resident-transfer (sha256 c31ae0352f2d)
- issues: shared_site_attribution_review, conflicting_sources:https://admission.asu.edu/cost-aid/non-resident-first-year,https://admission.asu.edu/cost-aid/transfer
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Base tuition: 35715 ⟵ “Base tuition | $35,715”
  - column:Tuition surcharge: 350 ⟵ “Tuition surcharge | $350”
  - column:Advanced Technology Fee: 200 ⟵ “Advanced Technology Fee | $200”
  - column:Undergraduate College Fees*: 2190 ⟵ “Undergraduate College Fees* | $2,190”
  - column:Student initiated fees: 807 ⟵ “Student initiated fees | $807”
  - column:On-campus housing and food**: 18819 ⟵ “On-campus housing and food** | $18,819”
  - column:Books, course materials, supplies and equipment: 1320 ⟵ “Books, course materials, supplies and equipment | $1,320”
  - column:Travel: 1650 ⟵ “Travel | $1,650”
  - column:Personal: 2343 ⟵ “Personal | $2,343”
  - column:Total: 63394 ⟵ “Total | $63,394”
### `8f6ebeebd541fa6a` Arizona State University Campus Immersion — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admission.asu.edu/cost-aid/transfer (sha256 8fa64b7f21f4)
- issues: shared_site_attribution_review, conflicting_sources:https://admission.asu.edu/cost-aid/non-resident-first-year,https://admission.asu.edu/cost-aid/non-resident-transfer
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Base tuition: 12177 ⟵ “Base tuition | $12,177”
  - column:Tuition surcharge: 350 ⟵ “Tuition surcharge | $350”
  - column:Advanced Technology fee: 200 ⟵ “Advanced Technology fee | $200”
  - column:Undergraduate College fee: 1280 ⟵ “Undergraduate College fee | $1,280”
  - column:Student initiated fees: 807 ⟵ “Student initiated fees | $807”
  - column:On-campus housing andfood**: 15456 ⟵ “On-campus housing andfood** | $15,456”
  - column:Books, course materials,supplies and equipment: 1320 ⟵ “Books, course materials,supplies and equipment | $1,320”
  - column:Travel: 1650 ⟵ “Travel | $1,650”
  - column:Personal: 2343 ⟵ “Personal | $2,343”
  - column:Total: 35583 ⟵ “Total | $35,583”
### `af0df765bea22b2a` Arizona State University Campus Immersion — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admission.asu.edu/cost-aid/non-resident-first-year (sha256 edb2b579a31c)
- issues: shared_site_attribution_review, conflicting_sources:https://admission.asu.edu/cost-aid/non-resident-transfer,https://admission.asu.edu/cost-aid/transfer
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Base tuition: 35715 ⟵ “Base tuition | $35,715”
  - column:Tuition surcharge: 350 ⟵ “Tuition surcharge | $350”
  - column:Advanced Technology Fee: 200 ⟵ “Advanced Technology Fee | $200”
  - column:Undergraduate College Fees*: 2190 ⟵ “Undergraduate College Fees* | $2,190”
  - column:Student initiated fees: 807 ⟵ “Student initiated fees | $807”
  - column:On-campus housing and food**: 18819 ⟵ “On-campus housing and food** | $18,819”
  - column:Books, course materials, supplies and equipment: 1320 ⟵ “Books, course materials, supplies and equipment | $1,320”
  - column:Travel: 1650 ⟵ “Travel | $1,650”
  - column:Personal: 2343 ⟵ “Personal | $2,343”
  - column:Total: 63394 ⟵ “Total | $63,394”
### `e4669c9bcb78a1de` Arizona State University Campus Immersion — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admission.asu.edu/cost-aid/resident-first-year (sha256 aecc150d6283)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Base tuition: 12177 ⟵ “Base tuition | $12,177”
  - column:Tuition surcharge: 350 ⟵ “Tuition surcharge | $350”
  - column:Advanced Technology fee: 200 ⟵ “Advanced Technology fee | $200”
  - column:Undergraduate College fee*: 1280 ⟵ “Undergraduate College fee* | $1,280”
  - column:Student initiated fees: 807 ⟵ “Student initiated fees | $807”
  - column:On-campus housing and food**: 18819 ⟵ “On-campus housing and food** | $18,819”
  - column:Books, course materials, supplies and equipment.: 1320 ⟵ “Books, course materials, supplies and equipment. | $1,320”
  - column:Travel: 1650 ⟵ “Travel | $1,650”
  - column:Personal: 2343 ⟵ “Personal | $2,343”
  - column:Total: 38946 ⟵ “Total | $38,946”
### `1da1f9f5104f4dd9` Arizona State University Campus Immersion — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admission.asu.edu/apply/international/transfer (sha256 3323d0618d6d)
- issues: shared_site_attribution_review
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 64 ⟵ “You can transfer a maximum of 64 credit hours from a regionally accredited community, junior or two-year college for courses in which you have earned a “C” (4.00 = “A”) or better.”
### `08fc6e01071492ca` Arizona State University Digital Immersion — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admission.asu.edu/cost-aid/non-resident-first-year (sha256 edb2b579a31c)
- issues: shared_site_attribution_review, conflicting_sources:https://admission.asu.edu/cost-aid/non-resident-transfer,https://admission.asu.edu/cost-aid/transfer
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Base tuition: 35715 ⟵ “Base tuition | $35,715”
  - column:Tuition surcharge: 350 ⟵ “Tuition surcharge | $350”
  - column:Advanced Technology Fee: 200 ⟵ “Advanced Technology Fee | $200”
  - column:Undergraduate College Fees*: 2190 ⟵ “Undergraduate College Fees* | $2,190”
  - column:Student initiated fees: 807 ⟵ “Student initiated fees | $807”
  - column:On-campus housing and food**: 18819 ⟵ “On-campus housing and food** | $18,819”
  - column:Books, course materials, supplies and equipment: 1320 ⟵ “Books, course materials, supplies and equipment | $1,320”
  - column:Travel: 1650 ⟵ “Travel | $1,650”
  - column:Personal: 2343 ⟵ “Personal | $2,343”
  - column:Total: 63394 ⟵ “Total | $63,394”
### `3f61c4ecb62d0561` Arizona State University Digital Immersion — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admission.asu.edu/cost-aid/transfer (sha256 8fa64b7f21f4)
- issues: shared_site_attribution_review, conflicting_sources:https://admission.asu.edu/cost-aid/non-resident-first-year,https://admission.asu.edu/cost-aid/non-resident-transfer
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Base tuition: 12177 ⟵ “Base tuition | $12,177”
  - column:Tuition surcharge: 350 ⟵ “Tuition surcharge | $350”
  - column:Advanced Technology fee: 200 ⟵ “Advanced Technology fee | $200”
  - column:Undergraduate College fee: 1280 ⟵ “Undergraduate College fee | $1,280”
  - column:Student initiated fees: 807 ⟵ “Student initiated fees | $807”
  - column:On-campus housing andfood**: 15456 ⟵ “On-campus housing andfood** | $15,456”
  - column:Books, course materials,supplies and equipment: 1320 ⟵ “Books, course materials,supplies and equipment | $1,320”
  - column:Travel: 1650 ⟵ “Travel | $1,650”
  - column:Personal: 2343 ⟵ “Personal | $2,343”
  - column:Total: 35583 ⟵ “Total | $35,583”
### `d9e2fd1f75d39f27` Arizona State University Digital Immersion — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admission.asu.edu/cost-aid/resident-transfer (sha256 3973958b2639)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Base tuition: 12177 ⟵ “Base tuition | $12,177”
  - column:Tuition surcharge: 350 ⟵ “Tuition surcharge | $350”
  - column:Advanced Technology fee: 200 ⟵ “Advanced Technology fee | $200”
  - column:Undergraduate College fee*: 1280 ⟵ “Undergraduate College fee* | $1,280”
  - column:Student initiated fees: 807 ⟵ “Student initiated fees | $807”
  - column:On-campus housing and food**: 18819 ⟵ “On-campus housing and food** | $18,819”
  - column:Books, course materials, supplies and equipment.: 1320 ⟵ “Books, course materials, supplies and equipment. | $1,320”
  - column:Travel: 1650 ⟵ “Travel | $1,650”
  - column:Personal: 2343 ⟵ “Personal | $2,343”
  - column:Total: 38946 ⟵ “Total | $38,946”
### `ee1ff2f5bdac80ea` Arizona State University Digital Immersion — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admission.asu.edu/cost-aid/non-resident-transfer (sha256 c31ae0352f2d)
- issues: shared_site_attribution_review, conflicting_sources:https://admission.asu.edu/cost-aid/non-resident-first-year,https://admission.asu.edu/cost-aid/transfer
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Base tuition: 35715 ⟵ “Base tuition | $35,715”
  - column:Tuition surcharge: 350 ⟵ “Tuition surcharge | $350”
  - column:Advanced Technology Fee: 200 ⟵ “Advanced Technology Fee | $200”
  - column:Undergraduate College Fees*: 2190 ⟵ “Undergraduate College Fees* | $2,190”
  - column:Student initiated fees: 807 ⟵ “Student initiated fees | $807”
  - column:On-campus housing and food**: 18819 ⟵ “On-campus housing and food** | $18,819”
  - column:Books, course materials, supplies and equipment: 1320 ⟵ “Books, course materials, supplies and equipment | $1,320”
  - column:Travel: 1650 ⟵ “Travel | $1,650”
  - column:Personal: 2343 ⟵ “Personal | $2,343”
  - column:Total: 63394 ⟵ “Total | $63,394”
### `e8997b31123cf6bc` Arizona State University Digital Immersion — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admission.asu.edu/apply/international/transfer (sha256 3323d0618d6d)
- issues: shared_site_attribution_review
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 64 ⟵ “You can transfer a maximum of 64 credit hours from a regionally accredited community, junior or two-year college for courses in which you have earned a “C” (4.00 = “A”) or better.”
### `052f704a1d2ac09c` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://registrar.arizona.edu/records-enrollment/petitions-appeals/tuition-appeals (sha256 99ddbc5b3057)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/appeals,https://financialaid.arizona.edu/policies/appeals,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you are in need of emergency funding, visit the Office of Scholarship and Financial Aid to learn about one-time special circumstance funding.”
### `304393f6e7998cf0` University of Arizona — appeals 2024-25 [new] (labeled_in_title)
- source: https://financialaid.arizona.edu/types-of-aid/scholarships/2024-2025-terms-and-conditions (sha256 bd58e945df1e)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Students who fail to meet SAP Standards will be notified of an option to submit a SAP Appeal to regain financial aid eligibility for the following semester.”
  - sentence: sap_appeal ⟵ “Students with extenuating circumstances preventing them from meeting the SAP renewal criteria by the end of the semester may submit a Satisfactory Academic Progress (SAP) Appeal by the deadline.”
  - sentence: sap_appeal ⟵ “Students who fail to meet SAP Standards will be notified of an option to submit a SAP Appeal to regain financial aid eligibility for the following semester.”
  - sentence: sap_appeal ⟵ “Students with extenuating circumstances preventing them from meeting the SAP renewal criteria by the end of the semester may submit a Satisfactory Academic Progress (SAP) Appeal by the deadline.”
### `3075968d45da8b9b` University of Arizona — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.arizona.edu/policies/appeals (sha256 7b6bd3b895b4)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/appeals,https://financialaid.arizona.edu/policies/sap,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal decisions or failure to meet Satisfactory Academic Progress.”
  - sentence: sap_appeal ⟵ “Additional Appeals To learn more about additional appeal options, such as the Satisfactory Academic Progress (SAP) appeal and the Merit Tuition Scholarship and Arizona Assurance Appeal and Deferment Request, review the appeals section of our forms page.”
### `3e8a8b637ab8ba49` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf (sha256 902ec0ee7123)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/appeals,https://financialaid.arizona.edu/policies/appeals,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf,https://registrar.arizona.edu/records-enrollment/petitions-appeals/tuition-appeals
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of extenuating circumstances and relevant documentation include but are not limited to: Extenuating Circumstance Examples of Supporting Documentation Death of a family member or person of significance Copy of an obituary or death certificate Other unusual circumstances that are beyond the student’s Written statement from professional advisor or other professional control third-party (on l”
### `4700d101ded92e63` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf (sha256 25b1e96b6fd3)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/appeals,https://financialaid.arizona.edu/policies/appeals,https://financialaid.arizona.edu/policies/sap,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: sap_appeal ⟵ “For the full policy, visit: https://financialaid.arizona.edu/policies/sap This Academic Plan Appeal is only to be submitted for students who are not meeting the Maximum Timeframe standard (and GPA/Pace).”
  - sentence: sap_appeal ⟵ “If you are meeting Maximum Timeframe, but are not meeting GPA or Pace, STOP HERE and complete the Satisfactory Academic Progress (SAP) Appeal (under the Satisfactory Academic Progress Appeal Forms section of the SAP Policy page).”
  - sentence: sap_appeal ⟵ “STOP HERE and complete the Satisfactory Academic Progress (SAP) Appeal. ☐ Complete section 1 of the SAP Appeal. ☐ If applicable, gather supporting documentation to attach to your appeal.”
  - sentence: sap_appeal ⟵ “Submission Deadline: It is recommended that you submit your SAP Appeal as soon as you are notified that you have been placed in SAP Suspension.”
  - sentence: sap_appeal ⟵ “The final deadline to submit the Fall 2026 SAP Appeal is December 4, 2026.”
  - sentence: sap_appeal ⟵ “NOTE: The Colleges of Law, Medicine, College of Veterinary Medicine, and Pharmacy have their own qualitative and quantitative standards for assessing Satisfactory Academic Progress and processes for reviewing appeals.”
### `53c3b78ba6618148` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.arizona.edu/policies/sap (sha256 710a2a6a39a5)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/appeals,https://financialaid.arizona.edu/policies/appeals,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “However, you may submit a SAP appeal to regain eligibility.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal If you’re placed on Financial Aid Suspension, you may file SAP Appeal to request reconsideration of your eligibility for financial aid funds.”
  - sentence: sap_appeal ⟵ “The SAP appeal process also requires you to meet with your college academic advisor to discuss your academic progress and to review your academic plan.”
  - sentence: sap_appeal ⟵ “Your academic advisor is required to complete a section of your SAP appeal form.”
  - sentence: sap_appeal ⟵ “Financial Aid SAP Academic Plan Status If your SAP appeal is approved, you will be placed on a probation status of Academic Plan for one semester.”
  - sentence: sap_appeal ⟵ “You may appeal this status by submitting a new SAP Appeal (with new extenuating circumstances) in order for your aid eligibility to be re-reviewed.”
### `58c8d2aca4f3b979` University of Arizona — appeals 2024-25 [new] (labeled_in_title)
- source: https://financialaid.arizona.edu/types-of-aid/scholarships/2024-2025-terms-and-conditions (sha256 bd58e945df1e)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 15}
  - sentence: scholarship_retention_appeal ⟵ “Students who submit their request before the priority deadline will be processed prior to the first day of classes, which may prevent late fees. 3.Students with extenuating circumstances preventing them from meeting the standard renewal requirements by the conclusion of the academic year may submit a Scholarship Appeal Form and supporting documents (by the deadline) for review by the Scholarship A”
  - sentence: scholarship_retention_appeal ⟵ “Students with extenuating circumstances preventing them from meeting the standard renewal requirements by the conclusion of the academic year may submit a Scholarship Appeal Form and supporting documents (by the deadline) for review by the Scholarship Appeals Committee.”
  - sentence: scholarship_retention_appeal ⟵ “Students who submit their request before the priority deadline will be processed prior to the first day of classes, which may prevent late fees. 3.Students with extenuating circumstances preventing them from meeting the standard renewal requirements by the conclusion of the academic year may submit a Scholarship Appeal Form and supporting documents (by the deadline) for review by the Scholarship A”
  - sentence: scholarship_retention_appeal ⟵ “Students who submit their request before the priority deadline will be processed prior to the first day of classes, which may prevent late fees. 3.Students with extenuating circumstances preventing them from meeting the standard renewal requirements by the conclusion of the academic year may submit a Scholarship Appeal Form and supporting documents (by the deadline) for review by the Scholarship A”
  - sentence: scholarship_retention_appeal ⟵ “Students who submit their request before the priority deadline will be processed prior to the first day of classes, which may prevent late fees. 3.Students with extenuating circumstances preventing them from meeting the standard renewal requirements by the conclusion of the academic year may submit a Scholarship Appeal Form and supporting documents (by the deadline) for review by the Scholarship A”
  - sentence: scholarship_retention_appeal ⟵ “Students with extenuating circumstances preventing them from meeting the standard renewal requirements by the conclusion of the academic year may submit a Scholarship Appeal Form and supporting documents (by the deadline) for review by the Scholarship Appeals Committee.”
### `9c064138ca55360a` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.arizona.edu/appeals (sha256 a3e9e04ed7a2)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/policies/appeals,https://financialaid.arizona.edu/policies/sap,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Learn More Satisfactory Academic Progress (SAP) Appeal Students must maintain Satisfactory Academic Progress (SAP) standards to remain eligible for financial aid.”
  - sentence: sap_appeal ⟵ “If an extenuating circumstance prevented you from maintaining these standards, you may submit a SAP appeal.”
### `b3bffa7108d43b21` University of Arizona — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.arizona.edu/policies/appeals (sha256 7b6bd3b895b4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “Valid Circumstances Abandonment by parents An abusive family environment that threatens the student's health or safety The student is unable to locate their parents In such cases a dependency override might be warranted.”
  - sentence: dependency_override ⟵ “If you do not have circumstances that would qualify for a dependency override, you must correct your FAFSA to include your parent’s information.”
  - sentence: dependency_override ⟵ “Students experiencing these types of extenuating circumstances may qualify to submit either a FAFSA Data Appeal, Cost of Attendance Appeal or a Dependency Override Appeal, depending on their specific situation.”
### `c154d28c2b748e2d` University of Arizona — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.arizona.edu/policies/appeals (sha256 7b6bd3b895b4)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/appeals,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf,https://registrar.arizona.edu/records-enrollment/petitions-appeals/tuition-appeals
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “OSFA may be able to update your dependency status if you have qualifying unusual circumstances and documentation to support it.”
  - sentence: need_based_special_circumstances ⟵ “Qualifying Dependency Override Special Circumstances Invalid Circumstances The conditions listed below, alone or in combination, do not qualify as unusual circumstances meriting a dependency override: Parents refuse to contribute to the student's education.”
  - sentence: need_based_special_circumstances ⟵ “If you believe that you have other unusual circumstances that do not fall under the qualifying circumstances above, then you will be required to explain your circumstances and provide the required documentation.”
  - sentence: need_based_special_circumstances ⟵ “Reasons for requesting a FAFSA Data Appeal If you or your family's financial situation has changed since filing the FAFSA due to special circumstances or if there are certain expenses not reflected on the FAFSA, you may request to submit a FAFSA Data Appeal.”
  - sentence: need_based_special_circumstances ⟵ “The following financial situations are examples of special circumstances that can be considered: Loss of employment Reduction in earnings Paid medical costs not covered by insurance Death of a parent Tax Liens K-12 Private Education Tuition Educational costs associated with paying for more than 1 student in college Supporting documentation must be submitted with each appeal in order to verify the ”
  - sentence: need_based_special_circumstances ⟵ “The following are not considered special circumstances: Pending reduction in income due to fluctuating commissions or consumer debt Refusal of a parent to provide financial support to the student To begin the process of submitting a FAFSA Data Appeal, please contact OSFA to request an appeal.”
### `c155bd96b99db11d` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf (sha256 25b1e96b6fd3)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/appeals,https://financialaid.arizona.edu/policies/appeals,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf,https://registrar.arizona.edu/records-enrollment/petitions-appeals/tuition-appeals
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of extenuating circumstances and relevant documentation include but are not limited to: Extenuating Circumstance Examples of Supporting Documentation Death of a family member or person of significance Copy of an obituary or death certificate Other unusual circumstances that are beyond the Written statement from professional advisor or other student’s control professional third-party (on l”
### `cbf44f7944d8d37a` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.arizona.edu/appeals (sha256 a3e9e04ed7a2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Merit Scholarship Appeal Students who did not meet the renewal requirements for their merit tuition scholarships due to extenuating circumstances may submit a Merit Tuition Scholarship Appeal.”
### `e0a0b2017d115937` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf (sha256 902ec0ee7123)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/appeals,https://financialaid.arizona.edu/policies/appeals,https://financialaid.arizona.edu/policies/sap,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “Student ID: Satisfactory Academic Progress (SAP) Appeal For GPA and/or Pace Fall 2026 First Name: M.I.”
  - sentence: sap_appeal ⟵ “In these cases, students may submit a SAP appeal to the Office of Scholarships & Financial Aid (OSFA).”
  - sentence: sap_appeal ⟵ “For the full policy, visit: https://financialaid.arizona.edu/policies/sap This appeal is to be submitted for students who are not meeting GPA or Pace standards.”
  - sentence: sap_appeal ⟵ “If you are not meeting Maximum Timeframe, STOP and complete the Maximum Timeframe Academic Plan Appeal. ☐ Complete section 1 of the SAP Appeal. ☐ If applicable, gather supporting documentation to attach to your appeal. ☐ Meet with your Academic Advisor to review Section 2, which requires the advisor’s signature. ☐ Sign and certify in Section 3. ☐ Submit your completed appeal to OSFA by deadline. •”
  - sentence: sap_appeal ⟵ “Submission Deadline: It is recommended that you submit your SAP Appeal as soon as you are notified that you have been placed in SAP Suspension.”
  - sentence: sap_appeal ⟵ “The final deadline to submit the Fall 2026 SAP Appeal is December 4, 2026.”
### `f06855995b93f0af` University of Arizona — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.arizona.edu/appeals (sha256 a3e9e04ed7a2)
- issues: semantic_review_required, conflicting_sources:https://financialaid.arizona.edu/policies/appeals,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP-Appeal-Form-GPA-Pace-Fillable.pdf,https://financialaid.arizona.edu/sites/default/files/2026-07/Fall-2026-SAP_Maximum-Timeframe-Academic-Plan-Appeal-Fillable.pdf,https://registrar.arizona.edu/records-enrollment/petitions-appeals/tuition-appeals
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “LEARN MORE Special Circumstances Appeals If there is a significant change to the financial information on your FAFSA or your expenses are higher than average, you may be eligible to complete a Family Contribution Appeal or Cost of Attendance Appeal.”
  - sentence: need_based_special_circumstances ⟵ “LEARN MORE Unusual Circumstances Appeal Student support systems come in all shapes and sizes.”
  - sentence: need_based_special_circumstances ⟵ “Students who have experienced unusual circumstances with their parent(s), including abandonment and abuse, may be eligible to complete a Dependency Override (DO) appeal.”
### `fa6c218c545ffaf7` University of Arizona — appeals 2024-25 [new] (labeled_in_title)
- source: https://financialaid.arizona.edu/types-of-aid/scholarships/2024-2025-terms-and-conditions (sha256 bd58e945df1e)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: competing_offer_review ⟵ “Offers are non-negotiable and are not increased to match offers from other institutions and remain the same as the initial offer for continuing students, even if a student improves their GPA at Arizona.”
  - sentence: competing_offer_review ⟵ “Offers are non-negotiable and are not increased to match offers from other institutions.”
  - sentence: competing_offer_review ⟵ “Offers are non-negotiable and are not increased to match offers from other institutions and remain the same as the initial offer for continuing students, even if a student improves their GPA at Arizona.”
  - sentence: competing_offer_review ⟵ “Offers are non-negotiable and are not increased to match offers from other institutions.”
  - sentence: competing_offer_review ⟵ “Offers are non-negotiable and are not increased to match offers from other institutions and remain the same as the initial offer for continuing students, even if a student improves their GPA at Arizona.”
  - sentence: competing_offer_review ⟵ “Offers are non-negotiable and are not increased to match offers from other institutions.”
### `242a4126533a921f` University of Arizona — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.arizona.edu/cost/incoming (sha256 86cd067de296)
- issues: arrangement_unlabeled, residency_unknown, stacked_header_unparsed
- checks: {"columns": 5, "rows": 7}
  - column:Tuition & Fees: 13900 ⟵ “Tuition & Fees | $13,900 | $13,900 | $13,900 | $44,400 | $44,400”
  - column:Living Expenses - Housing & Food: 3140 ⟵ “Living Expenses - Housing & Food | $3,140 | $17,770 | $13,100 | $17,770 | $13,100”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600 | $600”
  - column:Travel: 2450 ⟵ “Travel | $2,450 | $2,450 | $2,450 | $2,450 | $2,450”
  - column:Miscellaneous: 2550 ⟵ “Miscellaneous | $2,550 | $2,550 | $2,550 | $2,550 | $2,550”
  - column:Estimateper Semester: 11320 ⟵ “Estimateper Semester | $11,320 | $18,635 | $16,300 | $33,385 | $31,550”
  - column:Estimated totalper Year: 22640 ⟵ “Estimated totalper Year | $22,640 | $37,270 | $32,600 | $67,770 | $63,100”
  - column:Tuition & Fees: 13900 ⟵ “Tuition & Fees | $13,900 | $13,900 | $13,900 | $44,400 | $44,400”
  - column:Living Expenses - Housing & Food: 17770 ⟵ “Living Expenses - Housing & Food | $3,140 | $17,770 | $13,100 | $17,770 | $13,100”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600 | $600”
  - column:Travel: 2450 ⟵ “Travel | $2,450 | $2,450 | $2,450 | $2,450 | $2,450”
  - column:Miscellaneous: 2550 ⟵ “Miscellaneous | $2,550 | $2,550 | $2,550 | $2,550 | $2,550”
  - column:Estimateper Semester: 18635 ⟵ “Estimateper Semester | $11,320 | $18,635 | $16,300 | $33,385 | $31,550”
  - column:Estimated totalper Year: 37270 ⟵ “Estimated totalper Year | $22,640 | $37,270 | $32,600 | $67,770 | $63,100”
  - column:Tuition & Fees: 13900 ⟵ “Tuition & Fees | $13,900 | $13,900 | $13,900 | $44,400 | $44,400”
  - column:Living Expenses - Housing & Food: 13100 ⟵ “Living Expenses - Housing & Food | $3,140 | $17,770 | $13,100 | $17,770 | $13,100”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600 | $600”
  - column:Travel: 2450 ⟵ “Travel | $2,450 | $2,450 | $2,450 | $2,450 | $2,450”
  - column:Miscellaneous: 2550 ⟵ “Miscellaneous | $2,550 | $2,550 | $2,550 | $2,550 | $2,550”
  - column:Estimateper Semester: 16300 ⟵ “Estimateper Semester | $11,320 | $18,635 | $16,300 | $33,385 | $31,550”
  - column:Estimated totalper Year: 32600 ⟵ “Estimated totalper Year | $22,640 | $37,270 | $32,600 | $67,770 | $63,100”
  - column:Tuition & Fees: 44400 ⟵ “Tuition & Fees | $13,900 | $13,900 | $13,900 | $44,400 | $44,400”
  - column:Living Expenses - Housing & Food: 17770 ⟵ “Living Expenses - Housing & Food | $3,140 | $17,770 | $13,100 | $17,770 | $13,100”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600 | $600”
  - column:Travel: 2450 ⟵ “Travel | $2,450 | $2,450 | $2,450 | $2,450 | $2,450”
  - … 10 more rows
### `5b2fc0343065426b` University of Arizona — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.arizona.edu/types-of-aid/scholarships/2024-2025-terms-and-conditions (sha256 bd58e945df1e)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "rows": 5}
  - column:Base Tuition: 10000 ⟵ “Base Tuition | $10,000”
  - column:QTR (75% reduction): 7500 ⟵ “QTR (75% reduction) | $ 7,500”
  - column:Tuition Due: 2500 ⟵ “Tuition Due | $ 2,500”
  - column:All-AZ Academic**: 2500 ⟵ “All-AZ Academic** | $ 2,500”
  - column:Tuition Due(after award applied): 0 ⟵ “Tuition Due(after award applied) | $ 0”
### `604d3aa0cb4c62b6` University of Arizona — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.arizona.edu/cost/az-online (sha256 06d119c6d102)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees*: 13000 ⟵ “Tuition & Fees* | $13,000 | $13,000 | $13,000 | $13,000”
  - with_parents_or_family:Living Expenses - Housing and Food: 3050 ⟵ “Living Expenses - Housing and Food | $3,050 | $17,300 | $12,750 | N/A”
  - with_parents_or_family:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600”
  - with_parents_or_family:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | N/A”
  - with_parents_or_family:Miscellaneous: 2500 ⟵ “Miscellaneous | $2,500 | $2,500 | $2,500 | N/A”
  - with_parents_or_family:Loan Fee**: 0 ⟵ “Loan Fee** | $0 | $0 | $0 | N/A”
  - with_parents_or_family:TOTAL: 21550 ⟵ “TOTAL | $21,550 | $35,800 | $31,250 | $13,600”
  - on_campus:Tuition & Fees*: 13000 ⟵ “Tuition & Fees* | $13,000 | $13,000 | $13,000 | $13,000”
  - on_campus:Living Expenses - Housing and Food: 17300 ⟵ “Living Expenses - Housing and Food | $3,050 | $17,300 | $12,750 | N/A”
  - on_campus:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600”
  - on_campus:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | N/A”
  - on_campus:Miscellaneous: 2500 ⟵ “Miscellaneous | $2,500 | $2,500 | $2,500 | N/A”
  - on_campus:Loan Fee**: 0 ⟵ “Loan Fee** | $0 | $0 | $0 | N/A”
  - on_campus:TOTAL: 35800 ⟵ “TOTAL | $21,550 | $35,800 | $31,250 | $13,600”
  - off_campus_not_with_family:Tuition & Fees*: 13000 ⟵ “Tuition & Fees* | $13,000 | $13,000 | $13,000 | $13,000”
  - off_campus_not_with_family:Living Expenses - Housing and Food: 12750 ⟵ “Living Expenses - Housing and Food | $3,050 | $17,300 | $12,750 | N/A”
  - off_campus_not_with_family:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600”
  - off_campus_not_with_family:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | N/A”
  - off_campus_not_with_family:Miscellaneous: 2500 ⟵ “Miscellaneous | $2,500 | $2,500 | $2,500 | N/A”
  - off_campus_not_with_family:Loan Fee**: 0 ⟵ “Loan Fee** | $0 | $0 | $0 | N/A”
  - off_campus_not_with_family:TOTAL: 31250 ⟵ “TOTAL | $21,550 | $35,800 | $31,250 | $13,600”
  - column:Tuition & Fees*: 13000 ⟵ “Tuition & Fees* | $13,000 | $13,000 | $13,000 | $13,000”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600”
  - column:TOTAL: 13600 ⟵ “TOTAL | $21,550 | $35,800 | $31,250 | $13,600”
### `7dd03d51ceade1c2` University of Arizona — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.arizona.edu/cost/current-undergraduate (sha256 9cba159ea962)
- issues: arrangement_unlabeled, residency_unknown, stacked_header_unparsed, stale_year_label:2025-26
- checks: {"columns": 5, "rows": 7}
  - column:Tuition & Fees: 13900 ⟵ “Tuition & Fees | $13,900 | $13,900 | $13,900 | $43,100 | $43,100”
  - column:Living Expenses - Housing & Food: 3050 ⟵ “Living Expenses - Housing & Food | $3,050 | $17,300 | $12,750 | $17,300 | $12,750”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600 | $600”
  - column:Travel: 2400 ⟵ “Travel | $2,400 | $2,400 | $2,400 | $2,400 | $2,400”
  - column:Miscellaneous: 2500 ⟵ “Miscellaneous | $2,500 | $2,500 | $2,500 | $2,500 | $2,500”
  - column:Estimateper Semester: 11225 ⟵ “Estimateper Semester | $11,225 | $18,350 | $16,075 | $32,950 | $30,675”
  - column:Estimated totalper Year: 22450 ⟵ “Estimated totalper Year | $22,450 | $36,700 | $32,150 | $65,900 | $61,350”
  - column:Tuition & Fees: 13900 ⟵ “Tuition & Fees | $13,900 | $13,900 | $13,900 | $43,100 | $43,100”
  - column:Living Expenses - Housing & Food: 17300 ⟵ “Living Expenses - Housing & Food | $3,050 | $17,300 | $12,750 | $17,300 | $12,750”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600 | $600”
  - column:Travel: 2400 ⟵ “Travel | $2,400 | $2,400 | $2,400 | $2,400 | $2,400”
  - column:Miscellaneous: 2500 ⟵ “Miscellaneous | $2,500 | $2,500 | $2,500 | $2,500 | $2,500”
  - column:Estimateper Semester: 18350 ⟵ “Estimateper Semester | $11,225 | $18,350 | $16,075 | $32,950 | $30,675”
  - column:Estimated totalper Year: 36700 ⟵ “Estimated totalper Year | $22,450 | $36,700 | $32,150 | $65,900 | $61,350”
  - column:Tuition & Fees: 13900 ⟵ “Tuition & Fees | $13,900 | $13,900 | $13,900 | $43,100 | $43,100”
  - column:Living Expenses - Housing & Food: 12750 ⟵ “Living Expenses - Housing & Food | $3,050 | $17,300 | $12,750 | $17,300 | $12,750”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600 | $600”
  - column:Travel: 2400 ⟵ “Travel | $2,400 | $2,400 | $2,400 | $2,400 | $2,400”
  - column:Miscellaneous: 2500 ⟵ “Miscellaneous | $2,500 | $2,500 | $2,500 | $2,500 | $2,500”
  - column:Estimateper Semester: 16075 ⟵ “Estimateper Semester | $11,225 | $18,350 | $16,075 | $32,950 | $30,675”
  - column:Estimated totalper Year: 32150 ⟵ “Estimated totalper Year | $22,450 | $36,700 | $32,150 | $65,900 | $61,350”
  - column:Tuition & Fees: 43100 ⟵ “Tuition & Fees | $13,900 | $13,900 | $13,900 | $43,100 | $43,100”
  - column:Living Expenses - Housing & Food: 17300 ⟵ “Living Expenses - Housing & Food | $3,050 | $17,300 | $12,750 | $17,300 | $12,750”
  - column:Books, course materials, supplies, and equipment: 600 ⟵ “Books, course materials, supplies, and equipment | $600 | $600 | $600 | $600 | $600”
  - column:Travel: 2400 ⟵ “Travel | $2,400 | $2,400 | $2,400 | $2,400 | $2,400”
  - … 10 more rows
### `80b6b7d1da6368d9` University of Arizona — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.arizona.edu/types-of-aid/scholarships/2024-2025-terms-and-conditions (sha256 bd58e945df1e)
- issues: residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 5}
  - column:Base Tuition: 10000 ⟵ “Base Tuition | $10,000”
  - column:QTR (75% reduction): 7500 ⟵ “QTR (75% reduction) | $ 7,500”
  - column:Tuition Due: 2500 ⟵ “Tuition Due | $ 2,500”
  - column:Wildcat Tuition Award**: 2500 ⟵ “Wildcat Tuition Award** | $ 2,500”
  - column:Tuition Due(after award applied): 0 ⟵ “Tuition Due(after award applied) | $ 0”

## Re-verification of existing records (12)

- source_not_fetched: data/institutions/azwestern/credit_policies/2026-27.json ["credit_policies", "ipeds-104160", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/cochise/transfer_policies/2026-27.json ["transfer_policies", "ipeds-104425", null, "2026-27", {}]
- source_not_fetched: data/institutions/eac/credit_policies/2026-27.json ["credit_policies", "ipeds-104577", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/erau/transfer_policies/2026-27.json ["transfer_policies", "ipeds-104586", null, "2026-27", {}]
- source_not_fetched: data/institutions/npc/awards/2026-27.json ["awards", "ipeds-105349", null, "2026-27", {"award_name": "AZ Ahead NAU Scholarship"}]
- source_not_fetched: data/institutions/npc/awards/2026-27.json ["awards", "ipeds-105349", null, "2026-27", {"award_name": "Dan E. Leeds Fire & Emergency Services Scholarship"}]
- source_not_fetched: data/institutions/npc/awards/2026-27.json ["awards", "ipeds-105349", null, "2026-27", {"award_name": "Martia and Louis Smith Memorial Art Scholarship"}]
- source_not_fetched: data/institutions/npc/awards/2026-27.json ["awards", "ipeds-105349", null, "2026-27", {"award_name": "NPCFF CASO Student Scholarship"}]
- source_not_fetched: data/institutions/npc/awards/2026-27.json ["awards", "ipeds-105349", null, "2026-27", {"award_name": "President's Scholars"}]
- source_not_fetched: data/institutions/npc/awards/2026-27.json ["awards", "ipeds-105349", null, "2026-27", {"award_name": "Show Low Eastern Star"}]
- source_not_fetched: data/institutions/npc/awards/2026-27.json ["awards", "ipeds-105349", null, "2026-27", {"award_name": "Visual Arts Scholarship"}]
- source_not_fetched: data/institutions/npc/credit_policies/2026-27.json ["credit_policies", "ipeds-105349", null, "2026-27", {"policy_kind": "dual_enrollment"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Arizona State University Campus Immersion: tuition_fees, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Arizona State University Digital Immersion: tuition_fees, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- University of Arizona: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
