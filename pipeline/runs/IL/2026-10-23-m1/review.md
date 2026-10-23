# Review queue — IL (2026-27)

Pages fetched: 360; failures: 13. Candidates: 40 (1 without issues, 39 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 11 | 0 | 0 | 1 | 3 | 0 | 106 |
| cost_of_attendance | 6 | 0 | 0 | 0 | 4 | 0 | 111 |
| admissions_tests | 0 | 0 | 0 | 0 | 4 | 0 | 117 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 4 | 117 |
| merit_scholarships | 5 | 4 | 0 | 0 | 4 | 0 | 108 |
| ap_credit | 3 | 16 | 0 | 0 | 3 | 1 | 98 |
| clep_credit | 0 | 13 | 0 | 0 | 2 | 2 | 104 |
| ib_credit | 0 | 6 | 0 | 0 | 3 | 1 | 111 |
| dual_enrollment | 2 | 3 | 0 | 0 | 1 | 3 | 112 |
| transfer_credit | 1 | 8 | 1 | 0 | 3 | 0 | 108 |
| statewide_articulation | 0 | 0 | 0 | 0 | 3 | 1 | 117 |
| residency | 0 | 0 | 0 | 0 | 4 | 0 | 117 |
| degree_requirements | 8 | 0 | 0 | 0 | 2 | 0 | 111 |
| aid_appeals | 0 | 0 | 0 | 4 | 0 | 0 | 117 |

## Ready for review (1)

### `m3e5d56d0fa11004` DePaul University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://catalog.depaul.edu/student-handbooks/undergraduate/undergraduate-academic-policies/transfer-credit-regulations/transfer-credit-regulations.pdf (sha256 ec0347056bae)
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - residency_requirement_credits: 60 ⟵ “There also is a senior residency requirement, which means that the final 60 credit hours of your degree must be earned from DePaul.”
  - min_grade: C- ⟵ “Students transferring the equivalent of WRD 103 and/or WRD 104 must have received grades of C- or better in these courses in order to fulfill the Liberal Studies requirement.”
  - min_grade: C- ⟵ “Students transferring the equivalent of WRD 103 and/or WRD 104 application deadline listed on the Study Abroad ofﬁce website. must have received grades of C- or better in these courses in order to DePaul will award credit for courses completed through fulﬁll the Liberal Studies requirement. institutions that are formally recognized by their country’s 3.”

## Exceptions (39)

### `171e68a976b26f94` DePaul University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.depaul.edu/tuition-and-aid/financial-aid-and-eligibility/sap (sha256 8fc5cc7012b2)
- issues: semantic_review_required, conflicting_sources:https://www.depaul.edu/tuition-and-aid/financial-aid-forms-and-resources/appeal
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “However, you can regain eligibility in one of two ways: Submit a SAP appeal and have it approved by the SAP Appeal Committee.”
  - sentence: sap_appeal ⟵ “You may need to submit an appeal by completing the Satisfactory Academic Progress Appeal for Returning Students to have your financial aid eligibility reinstated.”
### `4adc9637546e2d32` DePaul University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.depaul.edu/tuition-and-aid/financial-aid-forms-and-resources/appeal (sha256 e20ea3cc78a7)
- issues: semantic_review_required, conflicting_sources:https://www.depaul.edu/tuition-and-aid/financial-aid-and-eligibility/sap
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeals If you have extenuating circumstances that prevented you from meeting the minimum SAP requirements, you may appeal for the reinstatement of your financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Collapsed Current Students accordion Current Students By the deadline established in this SAP FAQ, complete a SAP appeal in Campus Connect.”
  - sentence: sap_appeal ⟵ “Collapsed Returning and Readmitted Students accordion Returning and Readmitted Students Only readmitted students, who were not meeting SAP prior to their absence, can appeal by submitting an online Satisfactory Academic Progress Appeal for Returning Students Form.”
  - sentence: sap_appeal ⟵ “This form cannot be used to apply for summer 2027 financial aid or for Satisfactory Academic Progress (SAP) appeals.”
### `56dd259890dab0d5` DePaul University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.depaul.edu/tuition-and-aid/apply-for-aid (sha256 a918b4c65372)
- issues: semantic_review_required, conflicting_sources:https://www.depaul.edu/tuition-and-aid/financial-aid-forms-and-resources/appeal
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal There are two types of special circumstance appeals: Income/Expense, and Non-Income/Non-Expense For more details and instructions, please visit our Forms page.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance When completing a FAFSA, several questions are asked to determine a student’s dependency status.”
  - sentence: need_based_special_circumstances ⟵ “A parent’s inability or disinterest in assisting a student in paying for college is not in and of itself a reason for a dependency override; however, if you have unusual circumstances, please contact us so we can discuss your situation in greater detail.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special or unusual circumstance appeal does not guarantee an increase in your financial aid.”
### `b2334538b10ef75d` DePaul University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.depaul.edu/tuition-and-aid/financial-aid-forms-and-resources/appeal (sha256 e20ea3cc78a7)
- issues: semantic_review_required, conflicting_sources:https://www.depaul.edu/tuition-and-aid/apply-for-aid
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Collapsed Special Circumstance Appeal Instructions accordion Special Circumstance Appeal Instructions There are two types of special circumstance appeals: Income/Expense Special Circumstance Appeal We understand that your situation may have changed from the income information on your FAFSA to today.”
  - sentence: need_based_special_circumstances ⟵ “Collapsed 2026-27 Special Circumstances Appeal accordion 2026-27 Special Circumstances Appeal Special Circumstance Appeal for the 2026-27 academic year (use your Bluekey login) This form is not available for graduate, law, or international students.”
  - sentence: need_based_special_circumstances ⟵ “If you would like to submit a special circumstance appeal, see the section above.”
### `9bcbd92757acfea7` Illinois State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://policy.illinoisstate.edu/students/2-1-11/ (sha256 78150023a863)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The basis for granting an appeal (for either undergraduate or graduate students) may include death of a relative, injury or illness to the student, or other special circumstances.”
### `ce1cb61e2c45e417` Illinois State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.illinoisstate.edu/satprog/ (sha256 3b4e53257cf6)
- issues: semantic_review_required, conflicting_sources:https://policy.illinoisstate.edu/students/2-1-11/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If your aid is suspended, our office will send notification and a link to the Satisfactory Academic Progress Appeal Form.”
### `e2a97d00ff71ee26` Illinois State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://policy.illinoisstate.edu/students/2-1-11/ (sha256 78150023a863)
- issues: semantic_review_required, conflicting_sources:https://financialaid.illinoisstate.edu/satprog/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Notification of Appeals Undergraduate Students If financial aid eligibility is suspended as a result of failure to meet the completion rate or maximum timeframe standard, the Financial Aid Office notifies the student regarding the Satisfactory Academic Progress Appeal Form.”
  - sentence: sap_appeal ⟵ “If the review of the GPA standard occurs for the summer session and financial aid eligibility is suspended as a result of failure to meet the GPA standard, the Financial Aid Office notifies the student regarding the Satisfactory Academic Progress Appeal Form.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeal Form or Petition for Reinstatement must include reasons for failure to achieve good academic standing and satisfactory academic progress, and what has changed in the student's situation that will allow the student to demonstrate satisfactory academic progress at the next evaluation, and any applicable documentation.”
  - sentence: sap_appeal ⟵ “Graduate Students If financial aid eligibility is suspended as a result of failure to meet the completion rate or maximum timeframe standard, the Financial Aid Office sends a letter to the student including a Satisfactory Academic Progress Appeal Form.”
### `00e958486059e548` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/ (sha256 8b940b5268d0)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Pre-paid Tuition | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid”
### `090344c3f8ca5fe8` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/aid-process/sap-policy/ (sha256 bdc4caf21c98)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “SAP Policy | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Notif”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Notification Payment Summer Financial Aid SAP Policy Change of Financial Situation Other Special Circumstances Rights & Responsibilities Withdrawing vs.”
### `0f80e0cc53ed7311` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/cost/estimating-efc/ (sha256 2603b90937fe)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Estimating EFC | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid N”
### `1260eb2c7de77ee5` University of Illinois Chicago — appeals 2027-28 [new] (labeled_in_heading)
- source: https://financialaid.uic.edu/ (sha256 7f58a47315c6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Notification Payme”
### `174f0db3a6a99eec` University of Illinois Chicago — appeals 2026-27 [new] (source_unlabeled)
- source: https://docs.financialaid.uic.edu/docs/SAP_Policy.pdf (sha256 557b1475cd72)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/sap-policy/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Students seeking a second graduate or professional degree who have exhausted their financial aid eligibility will need to file a SAP appeal to regain eligibility.”
  - sentence: sap_appeal ⟵ “Students must submit documentation of an extenuating circumstance (i.e., doctor’s notice, letter from an academic advisor, etc.) with their SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “Appeals for undergraduate and graduate students will be reviewed by the SAP Appeal Committee, which consists of members from various colleges and departments at UIC.”
  - sentence: sap_appeal ⟵ “If appeals are not submitted in their entirety by the semester deadline (please refer to the Satisfactory Academic Progress Appeal Form), the appeal will not be reviewed until the following semester.”
  - sentence: sap_appeal ⟵ “Students must submit documentation of an extenuating circumstance (i.e., doctor’s notice, letter from an academic advisor, etc.) with their Satisfactory Academic Progress Appeal Form.”
### `44cd0c32a11689bb` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/aid-process/sap-policy/ (sha256 bdc4caf21c98)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://docs.financialaid.uic.edu/docs/SAP_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Click Here for Satisfactory Academic Progress Policy (PDF Version) For questions regarding SAP appeals you can email SAPAppeal@uic.edu and include your University ID Number (UIN).”
  - sentence: sap_appeal ⟵ “If you would like to submit a .pdf of your SAP appeal, send us an email for uploading instructions.”
  - sentence: sap_appeal ⟵ “Fill out form completely Select the appropriate reason for the request DO NOT use a Review Request if you have exceeded 180 credit hours – you would need to use a SAP Appeal for Max Time Frame Please read the form and all directions completely….click here to access the ***Review Request Form*** Timeline and Requirements: Timeline and Requirements: It is required to be an active student at UIC (enr”
  - sentence: sap_appeal ⟵ “FIVE Steps for Successfully Submitting your SAP Appeal: 1.”
  - sentence: sap_appeal ⟵ “Not responding to your advisor may delay your SAP Appeal decision.”
  - sentence: sap_appeal ⟵ “How to find my advisor: Click iAdvise Form Access: Please read the 5 steps for successfully submitting a SAP Appeal BEFORE accessing the form.”
### `525315fd1046452b` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/cost/financial-need/ (sha256 3c92a1b6acf2)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Need | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid N”
### `76fd30e1fcd50839` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Cost of Attendance (COA) | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Finan”
### `7d9117a6b8834188` University of Illinois Chicago — appeals 2026-27 [new] (labeled_in_title)
- source: https://financialaid.uic.edu/forms/2026-2027-forms/ (sha256 0998b8bb86c2)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Forms | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid ”
### `93377e2389a7ce41` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/aid-process/award-notification/ (sha256 29502e73c654)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Notification | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Fin”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Notification Payment Summer Financial Aid SAP Policy Change of Financial Situation Other Special Circumstances Rights & Responsibilities Withdrawing vs.”
### `a734e11ddf3be388` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/cost/ (sha256 7df2d6ba441a)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Cost | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Notificatio”
### `b443a6cc4a282500` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: budget_increase ⟵ “If your actual expenses exceed the estimated variable costs above, you may be eligible to submit a Request for Budget Adjustment.”
  - sentence: budget_increase ⟵ “This applies to costs such as: Off-campus housing exceeding estimates Child care expenses Purchase of a computer Study abroad program costs Disability-related educational expenses To apply, complete the Request for Budget Adjustment Form located on our 2026–2027 Forms Page, and include all required documentation.”
  - sentence: budget_increase ⟵ “If your actual costs exceed the estimated expenses listed above, you may request a Budget Adjustment.”
### `b52237a4ee63c9b1` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/cost/paying-your-bill/ (sha256 f846596e8065)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Paying Your Bill | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid”
### `c596f8fe5cd608d0` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/aid-process/special-circumstances/ (sha256 d85dd27ecbff)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/,https://financialaid.uic.edu/types-of-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Other Special Circumstances | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Fi”
  - sentence: need_based_special_circumstances ⟵ “Reducing Hours Calendar Types of Aid Grants Scholarships Waivers & Assistantships Loans Student Employment Study Abroad Veterans Pre-paid Tuition Forms 2026-2027 Forms 2025-2026 Forms What If’s Glossary of Terms Student Debt Relief Contact Us Student Financial Aid and Scholarships Other Special Circumstances View Menu Student Financial Aid and Scholarships Financial Aid Steps Other Special Circums”
  - sentence: need_based_special_circumstances ⟵ “Other Special Circumstances Copy link Cost of Attendance (Budget) Cost of Attendance (Budget) Each aid applicant is assigned a budget and Cost of Attendance (COA), which is an estimate of expenses they may incur in an academic year.”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Notification Payment Summer Financial Aid SAP Policy Change of Financial Situation Other Special Circumstances Rights & Responsibilities Withdrawing vs.”
### `c768d1bf3f671fb0` University of Illinois Chicago — appeals 2024-25 [new] (labeled_in_source)
- source: https://financialaid.uic.edu/aid-process/apply/ (sha256 de826febfdf0)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Apply | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Notificati”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Notification Payment Summer Financial Aid SAP Policy Change of Financial Situation Other Special Circumstances Rights & Responsibilities Withdrawing vs.”
### `c7721d8943ffda55` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/types-of-aid/scholarships/ (sha256 5716a057b5f5)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/aid-process/award-notification/,https://financialaid.uic.edu/aid-process/sap-policy/,https://financialaid.uic.edu/aid-process/special-circumstances/,https://financialaid.uic.edu/cost/,https://financialaid.uic.edu/cost/cost-attendance-coa/,https://financialaid.uic.edu/cost/estimating-efc/,https://financialaid.uic.edu/cost/financial-need/,https://financialaid.uic.edu/cost/paying-your-bill/,https://financialaid.uic.edu/forms/2026-2027-forms/,https://financialaid.uic.edu/types-of-aid/pre-paid-tuition/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Scholarships | Student Financial Aid and Scholarships | University of Illinois Chicago Search the site Toggle Menu Search Student Financial Aid and Scholarships UIC.edu Campus Map Scholarships The Bursar's Office Campus Care Search Cost Cost of Attendance (COA) Estimating EFC Financial Need Paying Your Bill Financial Aid Steps One Big Beautiful Bill Eligibility Apply Verification Financial Aid Not”
### `cce17247c17d83a7` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/aid-process/special-circumstances/ (sha256 d85dd27ecbff)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uic.edu/cost/cost-attendance-coa/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “If a student’s COA does not accurately reflect their expenses, they may request a reevaluation by submitting a Budget Adjustment Form with supporting documentation.”
  - sentence: budget_increase ⟵ “Budget adjustments may be approved for: Purchase of a personal computer Expenses associated with a disability Child care costs Unusual transportation expenses Room and board expenses Dependency Override Dependency Override Dependency status is based on information provided on the FAFSA.”
### `e51eeb573ad653b2` University of Illinois Chicago — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uic.edu/aid-process/special-circumstances/ (sha256 d85dd27ecbff)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “A student who does not meet FAFSA requirements for independent status can be considered independent by submitting a Dependency Override Request Form with supporting documentation.”
  - sentence: dependency_override ⟵ “Parents’ refusal to provide income information on the FAFSA is not a sufficient reason for dependency override approval.”
### `0ebc11b9771a76f2` University of Illinois Chicago — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2023-24
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 11178 ⟵ “Tuition - In State | $11,178”
  - column:Mandatory Fees: 4797 ⟵ “Mandatory Fees | $4,797”
### `14e54817ec87bfd6` University of Illinois Chicago — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 11652 ⟵ “Tuition - In State | $11,652”
  - column:Mandatory Fees: 5068 ⟵ “Mandatory Fees | $5,068”
### `24f010d42c3d2080` University of Illinois Chicago — costs 2018-19 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2018-19
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 10584 ⟵ “Tuition - In State | $10,584”
  - column:Mandatory Fees: 4286 ⟵ “Mandatory Fees | $4,286”
### `478f8638395a9cda` University of Illinois Chicago — costs 2021-22 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2021-22
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 10776 ⟵ “Tuition - In State | $10,776”
  - column:Mandatory Fees: 4987 ⟵ “Mandatory Fees | $4,987”
### `54e928dd57be1b4e` University of Illinois Chicago — costs 2022-23 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2022-23
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 10970 ⟵ “Tuition - In State | $10,970”
  - column:Mandatory Fees: 4713 ⟵ “Mandatory Fees | $4,713”
### `56dc53bbd418d4f8` University of Illinois Chicago — costs 2019-20 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2019-20
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 10584 ⟵ “Tuition - In State | $10,584”
  - column:Mandatory Fees: 4654 ⟵ “Mandatory Fees | $4,654”
### `64be8cd86d1ac411` University of Illinois Chicago — costs 2016-17 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2016-17
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 10584 ⟵ “Tuition - In State | $10,584”
  - column:Mandatory Fees: 4232 ⟵ “Mandatory Fees | $4,232”
### `a53a02540893ea24` University of Illinois Chicago — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 11178 ⟵ “Tuition - In State | $11,178”
  - column:Mandatory Fees: 4822 ⟵ “Mandatory Fees | $4,822”
### `b0f3cc6f12431d9b` University of Illinois Chicago — costs 2020-21 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2020-21
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 10776 ⟵ “Tuition - In State | $10,776”
  - column:Mandatory Fees: 4911 ⟵ “Mandatory Fees | $4,911”
### `d4252974246654a9` University of Illinois Chicago — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 11424 ⟵ “Tuition - In State | $11,424”
  - column:Mandatory Fees: 4890 ⟵ “Mandatory Fees | $4,890”
### `df4fe88bcbc0b100` University of Illinois Chicago — costs 2017-18 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uic.edu/cost/cost-attendance-coa/ (sha256 8dec19093aa0)
- issues: residency_unknown, stale_year_label:2017-18
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - In State: 10584 ⟵ “Tuition - In State | $10,584”
  - column:Mandatory Fees: 4272 ⟵ “Mandatory Fees | $4,272”
### `78f6078478b0ebda` University of Illinois Chicago — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.uic.edu/undergraduate/requirements-deadlines/transfer-requirements/transfer-faq (sha256 793747b93710)
- issues: conflicting_values:residency_requirement_credits
- checks: {"fields": []}
### `4ce49c1848ea604b` University of Illinois Urbana-Champaign — appeals 2027-28 [new] (labeled_in_heading)
- source: https://www.osfa.illinois.edu/ (sha256 389e79d3e5e6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Changes Financial Aid Changes EFFECTIVE 2026-2027 ACADEMIC YEAR Learn More Special Circumstance Special Circumstance The Office of Student Financial Aid can re-evaluate financial aid eligibility for undergraduates to reflect significant changes in the family financial situation.”
  - sentence: need_based_special_circumstances ⟵ “This process is called a Special Circumstance.”
### `5aeb369b97111dc9` University of Illinois Urbana-Champaign — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.osfa.illinois.edu/process/satisfactory-academic-progress/ (sha256 36700599a691)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “You may continue to attend Illinois at your own expense until you once again meet the SAP criteria or submit an SAP Appeal that’s approved.”
  - sentence: sap_appeal ⟵ “Written Appeal If you’re placed on Financial Aid Suspension, you may file a written appeal by completing an SAP Appeal form that can be found in the forms section of the OSFA website.”
  - sentence: sap_appeal ⟵ “The SAP appeal process also requires you to meet with your college academic advisor to discuss your academic progress and to review your academic plan.”
  - sentence: sap_appeal ⟵ “Your academic advisor is required to complete a section of your SAP appeal form.”
  - sentence: sap_appeal ⟵ “You are required to submit a written SAP Appeal form for each semester that you wish to be considered for financial aid until you meet the SAP requirements.”
  - sentence: sap_appeal ⟵ “The Student Financial Aid Administrator who has been assigned the responsibility of managing the SAP program and the Senior Assistant Director, Senior Associate Director or Director of the Office of Student Financial Aid reviews all SAP appeals.”

## Re-verification of existing records (217)

- source_not_fetched: data/institutions/aurora/credit_policies/2026-27.json ["credit_policies", "ipeds-143118", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/aurora/credit_policies/2026-27.json ["credit_policies", "ipeds-143118", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/aurora/transfer_policies/2026-27.json ["transfer_policies", "ipeds-143118", null, "2026-27", {}]
- source_not_fetched: data/institutions/bhc/credit_policies/2026-27.json ["credit_policies", "ipeds-143279", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/bhc/credit_policies/2026-27.json ["credit_policies", "ipeds-143279", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/blackburn/transfer_policies/2026-27.json ["transfer_policies", "ipeds-143288", null, "2026-27", {}]
- source_not_fetched: data/institutions/bradley/credit_policies/2026-27.json ["credit_policies", "ipeds-143358", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/csu/credit_policies/2026-27.json ["credit_policies", "ipeds-144005", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/clcillinois/credit_policies/2026-27.json ["credit_policies", "ipeds-146472", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/dacc/credit_policies/2026-27.json ["credit_policies", "ipeds-144564", null, "2026-27", {"policy_kind": "AP"}]
- all_values_found_year_not_labeled: data/institutions/depaul/transfer_policies/2026-27.json ["transfer_policies", "ipeds-144740", null, "2026-27", {}]
- source_not_fetched: data/institutions/elgin/credit_policies/2026-27.json ["credit_policies", "ipeds-144944", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "accounting-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "accounting-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "actuarial-science-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "art-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "art-bfa"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "art-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "art-business-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "art-business-bfa"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "audio-and-video-production-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "biochemistry-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "bioinformatics-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "biology-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "biology-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "biology-opt-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "biomedical-science-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "business-administration-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "business-administration-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "business-intelligence-analytics-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "chemistry-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "communication-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "communication-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "communication-sciences-and-disorders-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "communication-sciences-and-disorders-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "computer-science-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "computer-science-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "criminal-justice-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "criminal-justice-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "cybersecurity-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "data-science-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "digital-marketing-communication-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "digital-marketing-communication-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "digital-media-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "digital-media-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "economics-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "economics-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "educating-young-children-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "educating-young-children-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "elementary-special-education-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "elementary-special-education-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "elementary-teacher-education-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "elementary-teacher-education-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "elmhurst-management-program-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "engineering-physics-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "english-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "english-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "entrepreneurship-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "environmental-science-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "environmental-studies-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "exercise-science-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "exercise-science-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "finance-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "finance-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "french-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "french-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "games-and-animation-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "graphic-design-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "graphic-design-bfa"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "health-science-technology-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "history-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "history-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "information-systems-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "jazz-studies-bm"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "latino-studies-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "logistics-and-supply-chain-management-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "management-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "management-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "marketing-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "marketing-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "mathematics-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "middle-grades-english-language-arts-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "middle-grades-mathematics-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "multi-language-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "multimedia-journalism-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "multimedia-journalism-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-business-bm"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-business-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-education-bm-non-certified"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-education-spc12-bm"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-industry-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-performance-bm"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-production-bm"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "music-theory-and-composition-bm"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "musical-theatre-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "neuroscience-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "nursing-bsn-bsnrs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "philosophy-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "philosophy-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "physical-education-bs-non-certified"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "physical-education-ba-non-certified"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "physical-education-spc12-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "physical-education-spc12-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "physics-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "physics-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "physics-se-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "political-science-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "political-science-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "psychology-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "psychology-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "public-health-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "religious-studies-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "secondary-english-language-arts-education-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "secondary-mathematics-education-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "secondary-science-education-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "secondary-science-education-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "social-science-education-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "social-science-education-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "sociology-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "sociology-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "spanish-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "spanish-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "special-education-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "special-education-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "sport-management-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "sport-management-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "theatre-arts-education-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "theatre-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "theatre-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "urban-studies-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "urban-studies-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "world-language-education-ba"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "world-language-education-bs"}]
- source_not_fetched: data/institutions/elmhurst/academic_programs/2026-27.json ["academic_programs", "ipeds-144962", null, "2026-27", {"program_key": "writing-for-the-cinematic-arts-ba"}]
- source_not_fetched: data/institutions/heartland/credit_policies/2026-27.json ["credit_policies", "ipeds-384342", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/heartland/credit_policies/2026-27.json ["credit_policies", "ipeds-384342", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/heartland/credit_policies/2026-27.json ["credit_policies", "ipeds-384342", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/ic/credit_policies/2026-27.json ["credit_policies", "ipeds-145691", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/ic/transfer_policies/2026-27.json ["transfer_policies", "ipeds-145691", null, "2026-27", {}]
- source_not_fetched: data/institutions/jalc/credit_policies/2026-27.json ["credit_policies", "ipeds-146205", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/jalc/credit_policies/2026-27.json ["credit_policies", "ipeds-146205", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/jjc/credit_policies/2026-27.json ["credit_policies", "ipeds-146296", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/jjc/credit_policies/2026-27.json ["credit_policies", "ipeds-146296", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/kcc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-146348", null, "2026-27", {}]
- source_not_fetched: data/institutions/lakelandcollege/credit_policies/2026-27.json ["credit_policies", "ipeds-146506", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/llcc/credit_policies/2026-27.json ["credit_policies", "ipeds-146685", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/luc/credit_policies/2026-27.json ["credit_policies", "ipeds-146719", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/luc/credit_policies/2026-27.json ["credit_policies", "ipeds-146719", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/luc/credit_policies/2026-27.json ["credit_policies", "ipeds-146719", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/monmouthcollege/awards/2026-27.json ["awards", "ipeds-147341", null, "2026-27", {"award_name": "First-Year Students \u2013 Dean\u2019s Scholarships: GPA 4.00 +"}]
- source_not_fetched: data/institutions/monmouthcollege/awards/2026-27.json ["awards", "ipeds-147341", null, "2026-27", {"award_name": "First-Year Students \u2013 Dean\u2019s Scholarships: GPA 3.75-3.99"}]
- source_not_fetched: data/institutions/monmouthcollege/awards/2026-27.json ["awards", "ipeds-147341", null, "2026-27", {"award_name": "First-Year Students \u2013 Dean\u2019s Scholarships: GPA 3.50-3.74"}]
- source_not_fetched: data/institutions/monmouthcollege/awards/2026-27.json ["awards", "ipeds-147341", null, "2026-27", {"award_name": "First-Year Students \u2013 Dean\u2019s Scholarships: GPA 3.25-3.49"}]
- source_not_fetched: data/institutions/monmouthcollege/awards/2026-27.json ["awards", "ipeds-147341", null, "2026-27", {"award_name": "First-Year Students \u2013 Dean\u2019s Scholarships: GPA 3.00-3.24"}]
- source_not_fetched: data/institutions/monmouthcollege/awards/2026-27.json ["awards", "ipeds-147341", null, "2026-27", {"award_name": "First-Year Students \u2013 Dean\u2019s Scholarships: GPA 2.50-2.99"}]
- source_not_fetched: data/institutions/monmouthcollege/credit_policies/2026-27.json ["credit_policies", "ipeds-147341", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/northpark/awards/2026-27.json ["awards", "ipeds-147679", null, "2026-27", {"award_name": "Covenant Grant"}]
- source_not_fetched: data/institutions/northpark/awards/2026-27.json ["awards", "ipeds-147679", null, "2026-27", {"award_name": "Credentialed Covenant Minister Dependent Grant"}]
- source_not_fetched: data/institutions/northpark/awards/2026-27.json ["awards", "ipeds-147679", null, "2026-27", {"award_name": "Legacy Grant"}]
- source_not_fetched: data/institutions/northpark/awards/2026-27.json ["awards", "ipeds-147679", null, "2026-27", {"award_name": "Church Matching Grant"}]
- source_not_fetched: data/institutions/northpark/credit_policies/2026-27.json ["credit_policies", "ipeds-147679", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/northpark/transfer_policies/2026-27.json ["transfer_policies", "ipeds-147679", null, "2026-27", {}]
- source_not_fetched: data/institutions/neiu/credit_policies/2026-27.json ["credit_policies", "ipeds-147776", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/neiu/credit_policies/2026-27.json ["credit_policies", "ipeds-147776", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/niu/awards/2026-27.json ["awards", "ipeds-147703", null, "2026-27", {"award_name": "Freshman Merit Scholarships: GPA Range (4.0 Scale) 4.0"}]
- source_not_fetched: data/institutions/niu/awards/2026-27.json ["awards", "ipeds-147703", null, "2026-27", {"award_name": "Freshman Merit Scholarships: GPA Range (4.0 Scale) 3.90-3.99"}]
- source_not_fetched: data/institutions/niu/awards/2026-27.json ["awards", "ipeds-147703", null, "2026-27", {"award_name": "Freshman Merit Scholarships: GPA Range (4.0 Scale) 3.70-3.89"}]
- source_not_fetched: data/institutions/niu/awards/2026-27.json ["awards", "ipeds-147703", null, "2026-27", {"award_name": "Freshman Merit Scholarships: GPA Range (4.0 Scale) 3.50-3.69"}]
- source_not_fetched: data/institutions/niu/awards/2026-27.json ["awards", "ipeds-147703", null, "2026-27", {"award_name": "Freshman Merit Scholarships: GPA Range (4.0 Scale) 3.25-3.49"}]
- source_not_fetched: data/institutions/niu/awards/2026-27.json ["awards", "ipeds-147703", null, "2026-27", {"award_name": "Freshman Merit Scholarships: GPA Range (4.0 Scale) 3.00-3.24"}]
- source_not_fetched: data/institutions/oakton/credit_policies/2026-27.json ["credit_policies", "ipeds-147800", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/oakton/credit_policies/2026-27.json ["credit_policies", "ipeds-147800", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/quincy/awards/2026-27.json ["awards", "ipeds-148131", null, "2026-27", {"award_name": "In This Section"}]
- source_not_fetched: data/institutions/quincy/credit_policies/2026-27.json ["credit_policies", "ipeds-148131", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/quincy/credit_policies/2026-27.json ["credit_policies", "ipeds-148131", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/quincy/credit_policies/2026-27.json ["credit_policies", "ipeds-148131", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/rockford/transfer_policies/2026-27.json ["transfer_policies", "ipeds-148405", null, "2026-27", {}]
- source_not_fetched: data/institutions/roosevelt/academic_programs/2026-27.json ["academic_programs", "ipeds-148487", null, "2026-27", {"program_key": "digital-marketing-advertising-and-public-relations-ba-to-marketing-communication"}]
- source_not_fetched: data/institutions/roosevelt/academic_programs/2026-27.json ["academic_programs", "ipeds-148487", null, "2026-27", {"program_key": "health-science-administration-ba-mpa-public-administration"}]
- source_not_fetched: data/institutions/roosevelt/credit_policies/2026-27.json ["credit_policies", "ipeds-148487", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "radiography-bs", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "interdisciplinary-theatre-studies-ba", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "music-ba", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "music-and-computing-ba", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "interdisciplinary-music-honors-bma", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "interdisciplinary-music-industry-bma", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "music-composition-bm", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "classical-performance-guitar-bm", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "classical-performance-piano-bm", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "classical-performance-voice-bm", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "acting-bfa", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "musical-theatre-bfa", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "musical-theatre-dance-bfa", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/roosevelt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-148487", null, "2026-27", {"program_key": "organizational-leadership-baol", "requirement_key": "roadmap"}]
- source_not_fetched: data/institutions/saic/transfer_policies/2026-27.json ["transfer_policies", "ipeds-143048", null, "2026-27", {}]
- source_not_fetched: data/institutions/shawneecc/credit_policies/2026-27.json ["credit_policies", "ipeds-148821", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/sic/credit_policies/2026-27.json ["credit_policies", "ipeds-148937", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/siu/credit_policies/2026-27.json ["credit_policies", "ipeds-149222", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/src/credit_policies/2026-27.json ["credit_policies", "ipeds-148991", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/staugustine/transfer_policies/2026-27.json ["transfer_policies", "ipeds-148876", null, "2026-27", {}]
- source_not_fetched: data/institutions/uic/degree_requirements/2026-27.json ["degree_requirements", "ipeds-145600", null, "2026-27", {"program_key": "ba-in-music", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uic/degree_requirements/2026-27.json ["degree_requirements", "ipeds-145600", null, "2026-27", {"program_key": "ba-in-theatre-design-production-and-technology", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uic/degree_requirements/2026-27.json ["degree_requirements", "ipeds-145600", null, "2026-27", {"program_key": "joint-bs-in-chemical-engineering-ms-in-chemical-engineering", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uic/degree_requirements/2026-27.json ["degree_requirements", "ipeds-145600", null, "2026-27", {"program_key": "joint-bs-in-computer-science-ms-in-computer-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uic/degree_requirements/2026-27.json ["degree_requirements", "ipeds-145600", null, "2026-27", {"program_key": "bs-in-biochemistry", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uic/degree_requirements/2026-27.json ["degree_requirements", "ipeds-145600", null, "2026-27", {"program_key": "bs-with-a-major-in-earth-and-environmental-sciences", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uic/degree_requirements/2026-27.json ["degree_requirements", "ipeds-145600", null, "2026-27", {"program_key": "ba-with-a-major-in-political-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/wiu/awards/2026-27.json ["awards", "ipeds-149772", null, "2026-27", {"award_name": "Fraternal Order of Police Book Scholarship"}]
- source_not_fetched: data/institutions/wiu/awards/2026-27.json ["awards", "ipeds-149772", null, "2026-27", {"award_name": "C. Robin Frieden Memorial Scholarship"}]
- source_not_fetched: data/institutions/wiu/awards/2026-27.json ["awards", "ipeds-149772", null, "2026-27", {"award_name": "Marta Mounce Hayes Memorial Scholarship"}]
- source_not_fetched: data/institutions/wiu/awards/2026-27.json ["awards", "ipeds-149772", null, "2026-27", {"award_name": "Kristi Gilbert Memorial Scholarship"}]
- source_not_fetched: data/institutions/wiu/awards/2026-27.json ["awards", "ipeds-149772", null, "2026-27", {"award_name": "Civil Service Dependents Scholarship"}]
- source_not_fetched: data/institutions/wiu/awards/2026-27.json ["awards", "ipeds-149772", null, "2026-27", {"award_name": "Clela Trotter Wilson Scholarship"}]
- source_not_fetched: data/institutions/wiu/credit_policies/2026-27.json ["credit_policies", "ipeds-149772", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/wiu/credit_policies/2026-27.json ["credit_policies", "ipeds-149772", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/harpercollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-149842", null, "2026-27", {}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- DePaul University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, statewide_articulation, residency, degree_requirements
- Illinois State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Illinois Chicago: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency
- University of Illinois Urbana-Champaign: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency
