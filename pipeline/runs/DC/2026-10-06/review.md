# Review queue — DC (2026-27)

Pages fetched: 551; failures: 24. Candidates: 33 (3 without issues, 30 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 0 | 4 | 3 | 0 | 2 |
| cost_of_attendance | 0 | 0 | 0 | 4 | 3 | 0 | 2 |
| admissions_tests | 0 | 0 | 0 | 0 | 7 | 0 | 2 |
| common_data_set | 0 | 0 | 0 | 0 | 1 | 6 | 2 |
| merit_scholarships | 0 | 0 | 0 | 0 | 6 | 1 | 2 |
| ap_credit | 0 | 0 | 0 | 1 | 4 | 2 | 2 |
| clep_credit | 0 | 0 | 0 | 0 | 0 | 7 | 2 |
| ib_credit | 0 | 0 | 0 | 0 | 3 | 4 | 2 |
| dual_enrollment | 0 | 0 | 1 | 0 | 5 | 1 | 2 |
| transfer_credit | 0 | 0 | 1 | 0 | 6 | 0 | 2 |
| statewide_articulation | 0 | 0 | 0 | 0 | 5 | 2 | 2 |
| residency | 0 | 0 | 0 | 0 | 3 | 4 | 2 |
| degree_requirements | 0 | 0 | 0 | 0 | 2 | 5 | 2 |
| aid_appeals | 0 | 0 | 0 | 6 | 0 | 1 | 2 |

## Ready for review (3)

### `db48d5ebfd227c1a` Howard University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://howard.edu/registrar/transfer-credit-articulation-agreements (sha256 2c405fc91b94)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 60 ⟵ “A maximum of 60 credit hours from an accredited institution can be transferred.”
### `5bb4ea75c6a7b4bc` The Catholic University of America — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.catholic.edu/admission-aid/pre-college-dual-enrollment (sha256 4113cf0f6fd3)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 225 ⟵ “The cost is $225 per credit (3-credit courses will cost $675) and all courses will be taught online. These are regular sections of Catholic University classes and space is limited. Availability will be determined after the University’s students complete their registration process.”
### `f4d6cfc342fa655d` Trinity Washington University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://discover.trinitydc.edu/catalog-26-27/tuition/ (sha256 c189e1bb325e)
- checks: {"columns": 1, "rows": 3}
  - column:Regular Tuition: 640 ⟵ “Regular Tuition | $640”
  - column:Tuition at THEARC: 195 ⟵ “Tuition at THEARC | $195”
  - column:Trinity Experiential Life-Long Learning (TELL) Tuition (One-time TELL portfolio fee: $50): 150 ⟵ “Trinity Experiential Life-Long Learning (TELL) Tuition (One-time TELL portfolio fee: $50) | $150”

## Exceptions (30)

### `2fc962c60e65a616` George Washington University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.gwu.edu/appealing-status-dependent-student (sha256 bcd8eba8e337)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “In order to be considered for a dependency override the student must: File the FAFSA (and Profile if a new undergraduate student) and leave the parental information blank.”
  - sentence: dependency_override ⟵ “If your appeal is successful, we will approve a dependency override and make a correction to the FAFSA.”
### `51b0f64c9d5dca7a` George Washington University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.gwu.edu/policy-satisfactory-academic-progress (sha256 bd8207c51f1b)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.gwu.edu/sap-appeals
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals are considered in cases where there has been a death of a relative, injury or illness of the student, or other special circumstances.”
### `a21a384a1ddd8152` George Washington University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.gwu.edu/sap-appeals (sha256 11aa763c5568)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.gwu.edu/policy-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals are considered in cases where there has been a death of a relative, injury or illness of the student or other special circumstances.”
### `be2af34d27677e24` George Washington University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.gwu.edu/sap-appeals (sha256 11aa763c5568)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.gwu.edu/policy-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeals for Satisfactory Academic Progress | Office of Student Financial Assistance | Enrollment and the Student Experience | The George Washington University Skip to main content Learn More About Student Loan Debt Relief Office of Student Financial Assistance Enrollment and Student Success Apply for Federal Student Loan Debt Relief Main Bootstrap Navigation About Us Affordability Revolutionary Pr”
  - sentence: sap_appeal ⟵ “The appeal must include: A completed SAP Appeal Form that has been reviewed by an academic advisor.”
### `f208dd1c681df8f1` George Washington University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.gwu.edu/policy-satisfactory-academic-progress (sha256 bd8207c51f1b)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.gwu.edu/sap-appeals
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Section 5: Appeals A student may appeal the denial of student financial assistance by writing to the OSFA Satisfactory Academic Progress (SAP) Appeals Committee.”
  - sentence: sap_appeal ⟵ “The appeal must include: A completed SAP appeal form that has been reviewed by an academic advisor.”
### `787d6767061a5f77` George Washington University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.gwu.edu/how-estimate-your-total-cost-attendance-gw (sha256 143bf33dac61)
- issues: conflicting_sources:https://www.gwu.edu/cost-gw-education
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 2026-2027 Academic Year: 72000 ⟵ “Tuition: 2026-2027 Academic Year | $72000 | $72000 | $72000”
  - on_campus:Mandatory Student Fees: 420 ⟵ “Mandatory Student Fees | $420 | $420 | $420”
  - on_campus:Matriculation Fee: 350 ⟵ “Matriculation Fee | $350 | $350 | $350”
  - on_campus:Housing and Food: 18160 ⟵ “Housing and Food | $18,160 | $18,160 | $7,000”
  - on_campus:Books/Supplies: 1450 ⟵ “Books/Supplies | $1,450 | $1,450 | $1,450”
  - on_campus:Personal/Miscellaneous Expenses: 1700 ⟵ “Personal/Miscellaneous Expenses | $1,700 | $1,700 | $1,700”
  - on_campus:Transportation: 1075 ⟵ “Transportation | $1,075 | $1,075 | $1,075”
  - on_campus:Total Estimated Cost of Attendance: 95155 ⟵ “Total Estimated Cost of Attendance | $95,155 | $95,155 | $83,995”
  - on_campus:Total Estimated Direct Cost: 90930 ⟵ “Total Estimated Direct Cost | $90,930 | $90,930 | $79,770”
  - off_campus_not_with_family:Tuition: 2026-2027 Academic Year: 72000 ⟵ “Tuition: 2026-2027 Academic Year | $72000 | $72000 | $72000”
  - off_campus_not_with_family:Mandatory Student Fees: 420 ⟵ “Mandatory Student Fees | $420 | $420 | $420”
  - off_campus_not_with_family:Matriculation Fee: 350 ⟵ “Matriculation Fee | $350 | $350 | $350”
  - off_campus_not_with_family:Housing and Food: 18160 ⟵ “Housing and Food | $18,160 | $18,160 | $7,000”
  - off_campus_not_with_family:Books/Supplies: 1450 ⟵ “Books/Supplies | $1,450 | $1,450 | $1,450”
  - off_campus_not_with_family:Personal/Miscellaneous Expenses: 1700 ⟵ “Personal/Miscellaneous Expenses | $1,700 | $1,700 | $1,700”
  - off_campus_not_with_family:Transportation: 1075 ⟵ “Transportation | $1,075 | $1,075 | $1,075”
  - off_campus_not_with_family:Total Estimated Cost of Attendance: 95155 ⟵ “Total Estimated Cost of Attendance | $95,155 | $95,155 | $83,995”
  - off_campus_not_with_family:Total Estimated Direct Cost: 90930 ⟵ “Total Estimated Direct Cost | $90,930 | $90,930 | $79,770”
  - with_parents_or_family:Tuition: 2026-2027 Academic Year: 72000 ⟵ “Tuition: 2026-2027 Academic Year | $72000 | $72000 | $72000”
  - with_parents_or_family:Mandatory Student Fees: 420 ⟵ “Mandatory Student Fees | $420 | $420 | $420”
  - with_parents_or_family:Matriculation Fee: 350 ⟵ “Matriculation Fee | $350 | $350 | $350”
  - with_parents_or_family:Housing and Food: 7000 ⟵ “Housing and Food | $18,160 | $18,160 | $7,000”
  - with_parents_or_family:Books/Supplies: 1450 ⟵ “Books/Supplies | $1,450 | $1,450 | $1,450”
  - with_parents_or_family:Personal/Miscellaneous Expenses: 1700 ⟵ “Personal/Miscellaneous Expenses | $1,700 | $1,700 | $1,700”
  - with_parents_or_family:Transportation: 1075 ⟵ “Transportation | $1,075 | $1,075 | $1,075”
  - … 2 more rows
### `db950dcaa8c1a2a6` George Washington University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.gwu.edu/cost-gw-education (sha256 71cd7e1b1bd1)
- issues: conflicting_sources:https://financialaid.gwu.edu/how-estimate-your-total-cost-attendance-gw
- checks: {"columns": 2, "rows": 6}
  - on_campus:Tuition: 72000 ⟵ “Tuition | $72,000 | $72,000”
  - on_campus:Mandatory Fees: 420 ⟵ “Mandatory Fees | $420 | $420”
  - on_campus:Matriculation Fee*: 350 ⟵ “Matriculation Fee* | $350 | $0”
  - on_campus:Housing & Food**: 18160 ⟵ “Housing & Food** | $18,160 | $21,520”
  - on_campus:Books, Transportation & Misc. Expenses***: 4225 ⟵ “Books, Transportation & Misc. Expenses*** | $4,225 | $4,225”
  - on_campus:Estimated Costs: 95155 ⟵ “Estimated Costs | $95,155 | $98,165”
  - on_campus:Tuition: 72000 ⟵ “Tuition | $72,000 | $72,000”
  - on_campus:Mandatory Fees: 420 ⟵ “Mandatory Fees | $420 | $420”
  - on_campus:Matriculation Fee*: 0 ⟵ “Matriculation Fee* | $350 | $0”
  - on_campus:Housing & Food**: 21520 ⟵ “Housing & Food** | $18,160 | $21,520”
  - on_campus:Books, Transportation & Misc. Expenses***: 4225 ⟵ “Books, Transportation & Misc. Expenses*** | $4,225 | $4,225”
  - on_campus:Estimated Costs: 98165 ⟵ “Estimated Costs | $95,155 | $98,165”
### `497f5d4c52b5a26d` Georgetown University — appeals 2023-24 [new] (labeled_in_source)
- source: https://meded.georgetown.edu/admissions/financial-aid/sap/ (sha256 8c64e60910c9)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Should a student on Financial Aid Probation fail to satisfy the terms of their probation, the student will be placed on “Financial Aid Suspension” and will no longer be eligible for federal and/or institutional financial aid until The student meets the SAP conditions for their program or The student submits another SAP appeal and is approved for an additional probationary semester Medical Educatio”
### `b8e1eb357bf2f51d` Georgetown University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://meded.georgetown.edu/admissions/financial-aid/costofattendance/ (sha256 63fb100b8e71)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "components_reconcile": true, "rows": 11}
  - column:Tuition: 68778 ⟵ “Tuition | 68,778 | 68,778 | 68,778 | 68,778”
  - column:Fees: 10413 ⟵ “Fees | 10,413 | 8,443 | 7,223 | 7,997”
  - column:Tuition & Fees Subtotal: 79191 ⟵ “Tuition & Fees Subtotal | 79,191* | 77,221 | 76,001 | 76,775”
  - column:Food & Housing: 22250 ⟵ “Food & Housing | 22,250 | 24,475 | 26,700 | 22,250”
  - column:Books, Supplies & Equipment: 2000 ⟵ “Books, Supplies & Equipment | 2,000 | 1,000 | 1,000 | 800”
  - column:Personal Expenses: 3750 ⟵ “Personal Expenses | 3,750 | 4,125 | 4,500 | 3,750”
  - column:Transportation: 2500 ⟵ “Transportation | 2,500 | 3,000 | 5,700 | 4,750”
  - column:Cost of Living Subtotal: 30500 ⟵ “Cost of Living Subtotal | 30,500 | 32,600 | 37,900 | 31,550”
  - column:Health Insurance: 5000 ⟵ “Health Insurance | 5,000** | 4,785** | 4,785** | 4,785**”
  - column:Student Loan Fees: 3263 ⟵ “Student Loan Fees | 3,263**** | 3,452 | 3,553 | 3,553”
  - column:Total: 117954 ⟵ “Total | 117,954 | 118,808 | 122,989 | 119,663”
  - column:Tuition: 68778 ⟵ “Tuition | 68,778 | 68,778 | 68,778 | 68,778”
  - column:Fees: 8443 ⟵ “Fees | 10,413 | 8,443 | 7,223 | 7,997”
  - column:Tuition & Fees Subtotal: 77221 ⟵ “Tuition & Fees Subtotal | 79,191* | 77,221 | 76,001 | 76,775”
  - column:Food & Housing: 24475 ⟵ “Food & Housing | 22,250 | 24,475 | 26,700 | 22,250”
  - column:Books, Supplies & Equipment: 1000 ⟵ “Books, Supplies & Equipment | 2,000 | 1,000 | 1,000 | 800”
  - column:Personal Expenses: 4125 ⟵ “Personal Expenses | 3,750 | 4,125 | 4,500 | 3,750”
  - column:Transportation: 3000 ⟵ “Transportation | 2,500 | 3,000 | 5,700 | 4,750”
  - column:Cost of Living Subtotal: 32600 ⟵ “Cost of Living Subtotal | 30,500 | 32,600 | 37,900 | 31,550”
  - column:Health Insurance: 4785 ⟵ “Health Insurance | 5,000** | 4,785** | 4,785** | 4,785**”
  - column:Licensing Exam Expenses: 750 ⟵ “Licensing Exam Expenses | N/A | 750*** | 750*** | N/A”
  - column:Student Loan Fees: 3452 ⟵ “Student Loan Fees | 3,263**** | 3,452 | 3,553 | 3,553”
  - column:Total: 118808 ⟵ “Total | 117,954 | 118,808 | 122,989 | 119,663”
  - column:Tuition: 68778 ⟵ “Tuition | 68,778 | 68,778 | 68,778 | 68,778”
  - column:Fees: 7223 ⟵ “Fees | 10,413 | 8,443 | 7,223 | 7,997”
  - … 22 more rows
### `0af3981826084426` Howard University — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialservices.howard.edu/financial-aid/satisfactory-academic-progress (sha256 036ad99d986e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “Regaining Financial Aid Eligibility Students who are not eligible for financial aid due to not meeting SAP have the ability to submit an SAP appeal to potentially regain financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Students who have experienced hardships that negatively impacted their academic performance are encouraged to submit an SAP Appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeal Deadlines | Appealing Term | SAP Appeal Priority Deadlines | Summer | June 12 | Fall | July 27 | Spring | December 21 | Final Priority Deadline | April 12 Students who wish to appeal their SAP determination for potential financial aid eligibility reinstatement, must complete and submit all items listed below and return these items as a completed packet to the office of financial aid via”
  - sentence: sap_appeal ⟵ “SAP Appeal Form Standard Howard University Issued form that must be included in all SAP appeal submissions.”
  - sentence: sap_appeal ⟵ “Click Here to View the Virtual SAP Workshop SAP Appeal Review Completed SAP appeals with all the noted requirements will be reviewed within 14 Business days from the date of the submission.”
  - sentence: sap_appeal ⟵ “The Submission of an SAP appeal does not guarantee financial aid reinstatement.”
### `f37de7583377ad4d` The Catholic University of America — appeals 2026-27 [new] (source_unlabeled)
- source: https://financial-aid.catholic.edu/policies/satisfactory-academic-progress-undergraduate.html (sha256 77b70844f686)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “SAP Definitions Appeal An appeal is a process by which a student who is not meeting SAP standards, petitions the school for reconsideration of his eligibility for federal student aid funds.”
  - sentence: sap_appeal ⟵ “However, students failing SAP standards who have had mitigating circumstances may request reinstatement of their financial aid eligibility by completing the SAP Appeal for Financial Aid Reinstatement form and submitting it to the Office of Student Financial Assistance - SAP Appeals Committee.”
  - sentence: sap_appeal ⟵ “The SAP Appeal for Financial Aid Reinstatement Form is available at https://financial-aid.catholic.edu/forms/index.html.”
  - sentence: sap_appeal ⟵ “SAP Appeals Committee and Decision: Students will be sent official notification of the appeals committee decision.”
  - sentence: sap_appeal ⟵ “The decision of the SAP Appeals Committee is final.”
  - sentence: sap_appeal ⟵ “SAP Appeal Deadlines: Students wishing to be considered for SAP Probation, a SAP Appeal form should be submitted four weeks before the first day of classes (as stated in the University Calendar) to ensure a response before the beginning of the upcoming term.”
### `4183381a7a8e352e` The Catholic University of America — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://enrollment-services.catholic.edu/costs/tuition-fees/2026-2027undergraduate.html (sha256 e5bae91b9c7b)
- issues: arrangement_unlabeled, implausible_amount, conflicting_sources:https://www.catholic.edu/admission-aid/tuition-fees
- checks: {"columns": 2, "rows": 4}
  - column:Undergraduate Student Association Fee: 138 ⟵ “Undergraduate Student Association Fee | $138 | $71”
  - column:University Services Fee: 625 ⟵ “University Services Fee | $625 | $375”
  - column:Tuition Refund Plan: 120 ⟵ “Tuition Refund Plan | $120 | TBD†”
  - column:U-Pass Fee: 125 ⟵ “U-Pass Fee | $125 | Not Eligible”
  - column:Undergraduate Student Association Fee: 71 ⟵ “Undergraduate Student Association Fee | $138 | $71”
  - column:University Services Fee: 375 ⟵ “University Services Fee | $625 | $375”
### `631e0f4cd3a3b27c` The Catholic University of America — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://enrollment-services.catholic.edu/costs/prior-terms/2025-2026undergraduate.html (sha256 bd7b442e7191)
- issues: arrangement_unlabeled, implausible_amount, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 3}
  - column:Undergraduate Student Association Fee: 138 ⟵ “Undergraduate Student Association Fee | $138 | $71”
  - column:University Services Fee: 610 ⟵ “University Services Fee | $610 | $365”
  - column:Tuition Refund Plan: 124 ⟵ “Tuition Refund Plan | $124 | TBD†”
  - column:Undergraduate Student Association Fee: 71 ⟵ “Undergraduate Student Association Fee | $138 | $71”
  - column:University Services Fee: 365 ⟵ “University Services Fee | $610 | $365”
### `bd31fd0198553e8a` The Catholic University of America — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.catholic.edu/admission-aid/tuition-fees (sha256 9db98d5154a9)
- issues: conflicting_sources:https://enrollment-services.catholic.edu/costs/tuition-fees/2026-2027undergraduate.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition*: 60500 ⟵ “Tuition* | $60,500”
  - column:Fee Allowance: 1774 ⟵ “Fee Allowance | $1,774”
  - column:Housing Allowance: 12160 ⟵ “Housing Allowance | $12,160”
  - column:Food Allowance: 8780 ⟵ “Food Allowance | $8,780”
  - column:Books, Supplies, Licensure Allowance: 1286 ⟵ “Books, Supplies, Licensure Allowance | $1,286”
  - column:Transportation Allowance: 1068 ⟵ “Transportation Allowance | $1,068”
  - column:Personal Allowance: 2634 ⟵ “Personal Allowance | $2,634”
  - column:Estimated Loan Fees: 1284 ⟵ “Estimated Loan Fees | $1,284”
  - column:Total Cost (before financial aid): 89486 ⟵ “Total Cost (before financial aid) | $89,486”
### `1c61ce5a40e1adfa` Trinity Washington University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www2.trinitydc.edu/affordability-tuition-scholarships-and-financial-aid/ (sha256 1dbe89efc269)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://discover.trinitydc.edu/enrollment/financial-aid/,https://www2.trinitydc.edu/affordability-tuition-scholarships-and-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You have the right to appeal your financial aid award if you feel there are special circumstances that were not originally taken into consideration You have the right to know how Trinity determines whether you are making Satisfactory Academic Progress.”
### `a910b84b4d260f2d` Trinity Washington University — appeals 2026-27 [new] (labeled_in_title)
- source: https://discover.trinitydc.edu/catalog-26-27/financial-aid/ (sha256 0357569b3f7a)
- issues: semantic_review_required, conflicting_sources:https://discover.trinitydc.edu/enrollment/financial-aid/,https://discover.trinitydc.edu/policies/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students may appeal a determination of unsatisfactory academic progress in order to reestablish eligibility for financial aid.”
### `d57910f18789dc16` Trinity Washington University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www2.trinitydc.edu/affordability-tuition-scholarships-and-financial-aid/ (sha256 efc9300c608e)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://discover.trinitydc.edu/enrollment/financial-aid/,https://www2.trinitydc.edu/affordability-tuition-scholarships-and-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You have the right to appeal your financial aid award if you feel there are special circumstances that were not originally taken into consideration You have the right to know how Trinity determines whether you are making Satisfactory Academic Progress.”
### `e9db089951b66b9a` Trinity Washington University — appeals 2024-25 [new] (labeled_in_title)
- source: https://discover.trinitydc.edu/catalog-24-25/financial-aid/ (sha256 352e22e0de0a)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students may appeal a determination of unsatisfactory academic progress in order to reestablish eligibility for financial aid.”
### `eff0d6c43abb672d` Trinity Washington University — appeals 2026-27 [new] (source_unlabeled)
- source: https://discover.trinitydc.edu/policies/satisfactory-academic-progress/ (sha256 d7909f405be4)
- issues: semantic_review_required, conflicting_sources:https://discover.trinitydc.edu/catalog-26-27/financial-aid/,https://discover.trinitydc.edu/enrollment/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students may appeal a determination of unsatisfactory academic progress in order to reestablish eligibility for financial aid.”
### `f067cdd68bbfd12e` Trinity Washington University — appeals 2026-27 [new] (labeled_in_source)
- source: https://discover.trinitydc.edu/enrollment/financial-aid/ (sha256 1e39377e0634)
- issues: semantic_review_required, conflicting_sources:https://www2.trinitydc.edu/affordability-tuition-scholarships-and-financial-aid/,https://www2.trinitydc.edu/affordability-tuition-scholarships-and-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Armed Forces; Have legal dependents other than a spouse; Will be enrolled in a graduate school; Are married; or Can prove to the school extremely unusual circumstances that would warrant a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “You have the right to appeal your financial aid award if you feel there are special circumstances that were not originally taken into consideration You have the right to know how Trinity determines whether you are making Satisfactory Academic Progress.”
### `ff401758bd744898` Trinity Washington University — appeals 2026-27 [new] (labeled_in_source)
- source: https://discover.trinitydc.edu/enrollment/financial-aid/ (sha256 1e39377e0634)
- issues: semantic_review_required, conflicting_sources:https://discover.trinitydc.edu/catalog-26-27/financial-aid/,https://discover.trinitydc.edu/policies/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Download Financial Aid Forms 2026-2027 Financial Aid Forms These should be used for the Fall 2026, Spring 2027, and Summer 2027 semesters. 26-27 Citizenship Affidavit Form 26-27 Dependency Status Documentation 26-27 Satisfactory Academic Progress Appeal Form 26-27 Standard Dependent Verification Worksheet 26-27 Standard Independent Verification Worksheet 26-27 Early Childhood Education Scholarship”
### `e68c28ad65483571` Trinity Washington University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://discover.trinitydc.edu/catalog-24-25/tuition/ (sha256 450f6dc43bcd)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "rows": 3}
  - column:Regular Tuition: 620 ⟵ “Regular Tuition | $620”
  - column:Tuition at THEARC: 195 ⟵ “Tuition at THEARC | $195”
  - column:Trinity Experiential Life-Long Learning (TELL) Tuition (One-time TELL portfolio fee: $50): 150 ⟵ “Trinity Experiential Life-Long Learning (TELL) Tuition (One-time TELL portfolio fee: $50) | $150”
### `ff511d0acb93cd6d` Trinity Washington University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www2.trinitydc.edu/affordability-tuition-scholarships-and-financial-aid/ (sha256 1dbe89efc269)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Regular Tuition: 630 ⟵ “Regular Tuition | $630”
  - column:Tuition at THEARC: 195 ⟵ “Tuition at THEARC | $195”
  - column:Trinity Experiential Life-Long Learning (TELL) Tuition (One-time TELL portfolio fee: $50): 150 ⟵ “Trinity Experiential Life-Long Learning (TELL) Tuition (One-time TELL portfolio fee: $50) | $150”
### `d7b8007348c9dfbf` Trinity Washington University — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_title)
- source: https://discover.trinitydc.edu/catalog-25-26/policies-sps-undergraduate/ (sha256 072062620cc6)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 27, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | 6 | FNAR 101 & 102”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Art/Studio (Drawing or General Portfolio) | 4 | 6 | FNAR 195”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | 4 | BIOL 113”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 | 4 | MATH 125*”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | 4-8 | MATH 225* (at discretion of program chair)”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 4 | CHEM 111”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture | 4 | 6 | HUM 195”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 | 3 | CMSC 195”
  - equivalencies[AP-MICROECONOMICS|4]:  ⟵ “Economics: Micro | 4 | 3 | ECON 101”
  - equivalencies[AP-MACROECONOMICS|4]:  ⟵ “Economics: Macro | 4 | 3 | ECON 102”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language & Composition | 4 | 3 | ENGL 107”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature & Composition | 4 | 3 | Core Literature requirement”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | 4 | 4 | ENVS 101”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | 3 | Core Humanities Requirement”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | 3 | FREN 101”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture | 4 | 9 | FREN 101, 102, & 201”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | 12 | FREN 101, 102, 201, & 202”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture | 3 | 3 | HUM 195”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language & Culture | 4 | 9 | HUM 295”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language & Culture | 5 | 12 | HUM 395”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography | 4 | 3 | GLBL 250”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language & Culture | 3 | 3 | HUM 195”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4]:  ⟵ “Italian Language & Culture | 4 | 9 | HUM 295”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|5]:  ⟵ “Italian Language & Culture | 5 | 12 | HUM 395”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language & Culture | 3 | 3 | HUM 195”
  - … 14 more rows
### `7270de2d9f163867` University of the District of Columbia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.udc.edu/financial-aid/important-forms-and-information (sha256 5ec29d3b0809)
- issues: semantic_review_required, conflicting_sources:https://www.udc.edu/_docs/financial-aid/sap-extension-request-form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Important Information and Policies How to Make Payments Online Student Forms Instructions (View and Complete Tasks) myUDC Portal Direct Deposit Steps Frequently Asked Questions Estimated Financial Aid Review Timeline Award Terms and Conditions Return to Title IV Policy under Award Terms and Conditions Satisfactory Academic Progress (SAP) Appeal Extension Request Virtual Financial Aid Counseling Cl”
### `de6d6d6a068df545` University of the District of Columbia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.udc.edu/_docs/financial-aid/sap-extension-request-form.pdf (sha256 c78f400d7504)
- issues: semantic_review_required, conflicting_sources:https://www.udc.edu/financial-aid/important-forms-and-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Office of Financial Aid 4200 Connecticut Avenue NW Building 39, Room A-133 Washington, DC 20008 Appeal Submission: fadocs@udc.edu Satisfactory Academic Progress (SAP) Appeal Extension Request Submission Deadline: Fall 2026 – Friday, August 21, 2026 Please note: This request form is intended only for students who have an approved SAP appeal and have remained in compliance with the probationary term”
### `07917581a5e69f2b` University of the District of Columbia — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.udc.edu/financial-aid/cost-of-attendance (sha256 5108c92be80d)
- issues: arrangement_unlabeled, stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 10}
  - column:Tuition*: 7776 ⟵ “Tuition* | $7,776 | $7,776 | $8,976 | $8,976 | $16,320 | $16,320”
  - column:Fees*: 370 ⟵ “Fees* | $370 | $370 | $370 | $370 | $370 | $370”
  - column:Housing**: 14096 ⟵ “Housing** | $14,096 | $7,048 | $14,096 | $7,048 | $14,096 | $7,048”
  - column:Food: 3128 ⟵ “Food | $3,128 | $3,128 | $3,128 | $3,128 | $3,128 | $3,128”
  - column:Books, Course Materials, Supplies, Equipment: 1149 ⟵ “Books, Course Materials, Supplies, Equipment | $1,149 | $1,149 | $1,149 | $1,149 | $1,149 | $1,149”
  - column:Transportation: 1935 ⟵ “Transportation | $1,935 | $1,935 | $1,935 | $1,935 | $1,935 | $1,935”
  - column:Health Insurance: 1593 ⟵ “Health Insurance | $1,593 | $1,593 | $1,593 | $1,593 | $1,593 | $1,593”
  - column:Misc./Personal: 2310 ⟵ “Misc./Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - column:Loan Fee: 92 ⟵ “Loan Fee | $92 | $92 | $92 | $92 | $92 | $92”
  - column:Total: 32449 ⟵ “Total | $32,449 | $25,401 | $33,649 | $26,601 | $40,993 | $33,945”
  - with_parents_or_family:Tuition*: 7776 ⟵ “Tuition* | $7,776 | $7,776 | $8,976 | $8,976 | $16,320 | $16,320”
  - with_parents_or_family:Fees*: 370 ⟵ “Fees* | $370 | $370 | $370 | $370 | $370 | $370”
  - with_parents_or_family:Housing**: 7048 ⟵ “Housing** | $14,096 | $7,048 | $14,096 | $7,048 | $14,096 | $7,048”
  - with_parents_or_family:Food: 3128 ⟵ “Food | $3,128 | $3,128 | $3,128 | $3,128 | $3,128 | $3,128”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1149 ⟵ “Books, Course Materials, Supplies, Equipment | $1,149 | $1,149 | $1,149 | $1,149 | $1,149 | $1,149”
  - with_parents_or_family:Transportation: 1935 ⟵ “Transportation | $1,935 | $1,935 | $1,935 | $1,935 | $1,935 | $1,935”
  - with_parents_or_family:Health Insurance: 1593 ⟵ “Health Insurance | $1,593 | $1,593 | $1,593 | $1,593 | $1,593 | $1,593”
  - with_parents_or_family:Misc./Personal: 2310 ⟵ “Misc./Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - with_parents_or_family:Loan Fee: 92 ⟵ “Loan Fee | $92 | $92 | $92 | $92 | $92 | $92”
  - with_parents_or_family:Total: 25401 ⟵ “Total | $32,449 | $25,401 | $33,649 | $26,601 | $40,993 | $33,945”
### `2195674f590695e4` University of the District of Columbia — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.udc.edu/financial-aid/cost-of-attendance (sha256 5108c92be80d)
- issues: arrangement_unlabeled, stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 10}
  - column:Tuition*: 16320 ⟵ “Tuition* | $7,776 | $7,776 | $8,976 | $8,976 | $16,320 | $16,320”
  - column:Fees*: 370 ⟵ “Fees* | $370 | $370 | $370 | $370 | $370 | $370”
  - column:Housing**: 14096 ⟵ “Housing** | $14,096 | $7,048 | $14,096 | $7,048 | $14,096 | $7,048”
  - column:Food: 3128 ⟵ “Food | $3,128 | $3,128 | $3,128 | $3,128 | $3,128 | $3,128”
  - column:Books, Course Materials, Supplies, Equipment: 1149 ⟵ “Books, Course Materials, Supplies, Equipment | $1,149 | $1,149 | $1,149 | $1,149 | $1,149 | $1,149”
  - column:Transportation: 1935 ⟵ “Transportation | $1,935 | $1,935 | $1,935 | $1,935 | $1,935 | $1,935”
  - column:Health Insurance: 1593 ⟵ “Health Insurance | $1,593 | $1,593 | $1,593 | $1,593 | $1,593 | $1,593”
  - column:Misc./Personal: 2310 ⟵ “Misc./Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - column:Loan Fee: 92 ⟵ “Loan Fee | $92 | $92 | $92 | $92 | $92 | $92”
  - column:Total: 40993 ⟵ “Total | $32,449 | $25,401 | $33,649 | $26,601 | $40,993 | $33,945”
  - with_parents_or_family:Tuition*: 16320 ⟵ “Tuition* | $7,776 | $7,776 | $8,976 | $8,976 | $16,320 | $16,320”
  - with_parents_or_family:Fees*: 370 ⟵ “Fees* | $370 | $370 | $370 | $370 | $370 | $370”
  - with_parents_or_family:Housing**: 7048 ⟵ “Housing** | $14,096 | $7,048 | $14,096 | $7,048 | $14,096 | $7,048”
  - with_parents_or_family:Food: 3128 ⟵ “Food | $3,128 | $3,128 | $3,128 | $3,128 | $3,128 | $3,128”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1149 ⟵ “Books, Course Materials, Supplies, Equipment | $1,149 | $1,149 | $1,149 | $1,149 | $1,149 | $1,149”
  - with_parents_or_family:Transportation: 1935 ⟵ “Transportation | $1,935 | $1,935 | $1,935 | $1,935 | $1,935 | $1,935”
  - with_parents_or_family:Health Insurance: 1593 ⟵ “Health Insurance | $1,593 | $1,593 | $1,593 | $1,593 | $1,593 | $1,593”
  - with_parents_or_family:Misc./Personal: 2310 ⟵ “Misc./Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - with_parents_or_family:Loan Fee: 92 ⟵ “Loan Fee | $92 | $92 | $92 | $92 | $92 | $92”
  - with_parents_or_family:Total: 33945 ⟵ “Total | $32,449 | $25,401 | $33,649 | $26,601 | $40,993 | $33,945”
### `322b89772e3418f4` University of the District of Columbia — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.udc.edu/financial-aid/cost-of-attendance (sha256 5108c92be80d)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 10}
  - column:Tuition*: 8976 ⟵ “Tuition* | $7,776 | $7,776 | $8,976 | $8,976 | $16,320 | $16,320”
  - column:Fees*: 370 ⟵ “Fees* | $370 | $370 | $370 | $370 | $370 | $370”
  - column:Housing**: 14096 ⟵ “Housing** | $14,096 | $7,048 | $14,096 | $7,048 | $14,096 | $7,048”
  - column:Food: 3128 ⟵ “Food | $3,128 | $3,128 | $3,128 | $3,128 | $3,128 | $3,128”
  - column:Books, Course Materials, Supplies, Equipment: 1149 ⟵ “Books, Course Materials, Supplies, Equipment | $1,149 | $1,149 | $1,149 | $1,149 | $1,149 | $1,149”
  - column:Transportation: 1935 ⟵ “Transportation | $1,935 | $1,935 | $1,935 | $1,935 | $1,935 | $1,935”
  - column:Health Insurance: 1593 ⟵ “Health Insurance | $1,593 | $1,593 | $1,593 | $1,593 | $1,593 | $1,593”
  - column:Misc./Personal: 2310 ⟵ “Misc./Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - column:Loan Fee: 92 ⟵ “Loan Fee | $92 | $92 | $92 | $92 | $92 | $92”
  - column:Total: 33649 ⟵ “Total | $32,449 | $25,401 | $33,649 | $26,601 | $40,993 | $33,945”
  - with_parents_or_family:Tuition*: 8976 ⟵ “Tuition* | $7,776 | $7,776 | $8,976 | $8,976 | $16,320 | $16,320”
  - with_parents_or_family:Fees*: 370 ⟵ “Fees* | $370 | $370 | $370 | $370 | $370 | $370”
  - with_parents_or_family:Housing**: 7048 ⟵ “Housing** | $14,096 | $7,048 | $14,096 | $7,048 | $14,096 | $7,048”
  - with_parents_or_family:Food: 3128 ⟵ “Food | $3,128 | $3,128 | $3,128 | $3,128 | $3,128 | $3,128”
  - with_parents_or_family:Books, Course Materials, Supplies, Equipment: 1149 ⟵ “Books, Course Materials, Supplies, Equipment | $1,149 | $1,149 | $1,149 | $1,149 | $1,149 | $1,149”
  - with_parents_or_family:Transportation: 1935 ⟵ “Transportation | $1,935 | $1,935 | $1,935 | $1,935 | $1,935 | $1,935”
  - with_parents_or_family:Health Insurance: 1593 ⟵ “Health Insurance | $1,593 | $1,593 | $1,593 | $1,593 | $1,593 | $1,593”
  - with_parents_or_family:Misc./Personal: 2310 ⟵ “Misc./Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - with_parents_or_family:Loan Fee: 92 ⟵ “Loan Fee | $92 | $92 | $92 | $92 | $92 | $92”
  - with_parents_or_family:Total: 26601 ⟵ “Total | $32,449 | $25,401 | $33,649 | $26,601 | $40,993 | $33,945”
### `9056494af4fee42f` University of the District of Columbia — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.udc.edu/admissions/transfer-students/transfer-credit-policy (sha256 7407d9a4092f)
- issues: conflicting_values:residency_requirement_credits
- checks: {"fields": []}

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 270; pages by category: admissions_tests 55, aid_appeals 5, cost_of_attendance 39, dual_enrollment 1, merit_scholarships 2, residency 26, tuition_fees 16

## Blocked by the site (every request refused; needs the browser fallback)

- American University (`ipeds-131159`)
- Gallaudet University (`ipeds-131450`)

## Leads: official pages found with no extracted record

- George Washington University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Georgetown University: admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency
- Howard University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, statewide_articulation
- NewU University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation
- The Catholic University of America: admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation
- Trinity Washington University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- University of the District of Columbia: admissions_tests, common_data_set, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
