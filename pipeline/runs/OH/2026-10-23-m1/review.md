# Review queue — OH (2026-27)

Pages fetched: 630; failures: 111. Candidates: 28 (1 without issues, 27 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 12 | 0 | 0 | 4 | 2 | 0 | 108 |
| cost_of_attendance | 4 | 0 | 0 | 1 | 6 | 0 | 115 |
| admissions_tests | 0 | 0 | 0 | 0 | 7 | 0 | 119 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 7 | 119 |
| merit_scholarships | 7 | 6 | 0 | 0 | 7 | 0 | 106 |
| ap_credit | 4 | 2 | 0 | 1 | 4 | 2 | 113 |
| clep_credit | 1 | 1 | 0 | 1 | 1 | 5 | 117 |
| ib_credit | 2 | 1 | 0 | 1 | 3 | 3 | 116 |
| dual_enrollment | 0 | 3 | 0 | 0 | 3 | 4 | 116 |
| transfer_credit | 4 | 7 | 0 | 1 | 6 | 0 | 108 |
| statewide_articulation | 0 | 0 | 0 | 0 | 7 | 0 | 119 |
| residency | 0 | 0 | 0 | 0 | 6 | 1 | 119 |
| degree_requirements | 5 | 0 | 0 | 0 | 5 | 1 | 115 |
| aid_appeals | 0 | 0 | 0 | 5 | 0 | 2 | 119 |

## Ready for review (1)

### `d8f6788bb12ff5e6` Ohio State University-Main Campus — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://undergrad.osu.edu/cost-and-aid/basic-costs (sha256 19df59876187)
- checks: {"columns": 1, "rows": 2}
  - on_campus:Tuition (includes instructional and general fees): 44271 ⟵ “Tuition (includes instructional and general fees) | Columbus: $14,050Regional campus/ATI: $10,064/10,013 | $44,271*”
  - on_campus:Housing and food: 15738 ⟵ “Housing and food | Columbus: $15,738**Regional campus/ATI: Varies^ | $15,738**”

## Exceptions (27)

### `5523ea44a9181bee` Bowling Green State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bgsu.edu/financial-aid/manage-aid/satisfactory-academic-progress/policy.html (sha256 0f1123d9695d)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.bgsu.edu/financial-aid/manage-aid/satisfactory-academic-progress.html
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Future students Current students Firelands campus Parents/families Faculty/Staff Alumni Apply Visit Give Toggle high contrast Satisfactory Academic Progress Policy BGSU Financial Aid and Scholarships Manage your financial aid Satisfactory Academic Progress Satisfactory Academic Progress Policy Satisfactory Academic Progress Appeal Form Overview Bowling Green State University (BGSU) is required by ”
  - sentence: sap_appeal ⟵ “Eligibility may be regained by eliminating all satisfactory progress deficiencies at the student’s expense until all requirements of this policy are met or by appealing his or her satisfactory academic progress status and the appeal is approved.”
  - sentence: sap_appeal ⟵ “An approved appeal will result in a Satisfactory Academic Progress Academic Plan and may include: Expected GPA to accomplish by the end of the probationary payment period Expected number of credit hours to complete by the end of the probationary payment period The maximum number of additional credit hours allowed as indicated on Academic Advisor Certification Form (for Maximum Timeframe citations)”
  - sentence: sap_appeal ⟵ “Appeal Committee Students who submit a Satisfactory Academic Progress appeal will have their submission reviewed by an appeals committee.”
  - sentence: sap_appeal ⟵ “Summer: July 1 Fall: October 1 Spring: March 1 Policy revised: May 8, 2024 If you wish to appeal your satisfactory academic progress status, based on the above policy, please use the Satisfactory Academic Progress Appeal Form.”
### `7c31ccafce35404a` Bowling Green State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bgsu.edu/financial-aid/manage-aid/satisfactory-academic-progress.html (sha256 86b7bfa0192c)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.bgsu.edu/financial-aid/manage-aid/satisfactory-academic-progress/policy.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Submit a SAP appeal form explaining your situation.”
### `252547b3a623788d` Bowling Green State University-Main Campus — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.bgsu.edu/financial-aid/cost-overview.html (sha256 39fc224b2ab1)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition: 14772 ⟵ “Tuition | $14,772 | $14,772”
  - on_campus:On-campus housing: 6760 ⟵ “On-campus housing | $6,760 | $6,760”
  - on_campus:On-campus food: 4464 ⟵ “On-campus food | $4,464 | $4,464”
  - on_campus:Total estimated costs: 25996 ⟵ “Total estimated costs | $25,996 | $33,984”
### `c66389d4d46994b7` Bowling Green State University-Main Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bgsu.edu/financial-aid/cost-of-attendance.html (sha256 47fbf351740a)
- issues: multiple_total_rows, residency_unknown, shared_site_attribution_review
- checks: {"columns": 1, "rows": 12}
  - on_campus:Tuition: 9176 ⟵ “Tuition | $9,176 | ✓ | ”
  - on_campus:Fees: 680 ⟵ “Fees | $680 | ✓ | ”
  - on_campus:Housing**: 8160 ⟵ “Housing** | $8,160 | ✓ | ”
  - on_campus:Food**: 6016 ⟵ “Food** | $6,016 | ✓ | ”
  - on_campus:Health Insurance: 1940 ⟵ “Health Insurance | $1,940 | ✓ | ”
  - on_campus:Books/Supplies: 710 ⟵ “Books/Supplies | $710 |  | ✓”
  - on_campus:Loan Fees: 102 ⟵ “Loan Fees | $102 |  | ✓”
  - on_campus:Pers/Misc: 2800 ⟵ “Pers/Misc | $2,800 |  | ✓”
  - on_campus:Trans: 920 ⟵ “Trans | $920 |  | ✓”
  - on_campus:TOTAL: 30504 ⟵ “TOTAL | $30,504 |  | ”
  - on_campus:Non-Res Fee: 5326 ⟵ “Non-Res Fee | $5,326 | ✓ | ”
  - on_campus:TOTAL Non-OH RESIDENT: 35830 ⟵ “TOTAL Non-OH RESIDENT | $35,830 |  | ”
### `faa6639d1e4c25b0` Bowling Green State University-Main Campus — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.bgsu.edu/financial-aid/cost-overview.html (sha256 39fc224b2ab1)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - on_campus:Tuition: 14772 ⟵ “Tuition | $14,772 | $14,772”
  - on_campus:Nonresident fee: 7988 ⟵ “Nonresident fee | — | $7,988”
  - on_campus:On-campus housing: 6760 ⟵ “On-campus housing | $6,760 | $6,760”
  - on_campus:On-campus food: 4464 ⟵ “On-campus food | $4,464 | $4,464”
  - on_campus:Total estimated costs: 33984 ⟵ “Total estimated costs | $25,996 | $33,984”
### `29ba48d4d84cf984` Kent State University at Kent — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.kent.edu/fbe-center/scholarships-financial-aid (sha256 5a75f133d388)
- issues: ambiguous_year_labels, semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.kent.edu/fbe-center/SAP,https://www.kent.edu/fbe-center/forms-requests?search=satisfactory%20appeal
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you’re cited but now meet SAP standards, you must still file an appeal for review. learn more SAP Appeal Form Completing Verification for the FAFSA The federal government requires Kent State to verify, or confirm, the data reported by students and their parent(s) on the Free Application for Federal Student Aid (FAFSA).”
### `6f0ea7baf1d5365d` Kent State University at Kent — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.kent.edu/fbe-center/SAP (sha256 dc36d9a8066e)
- issues: ambiguous_year_labels, semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.kent.edu/fbe-center/forms-requests?search=satisfactory%20appeal,https://www.kent.edu/fbe-center/scholarships-financial-aid
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Students who lose student aid eligibility due to this standard can regain eligibility for financial aid by submitting a successful SAP Appeal.”
  - sentence: sap_appeal ⟵ “View the Satisfactory Academic Progress Policy Satisfactory Academic Progress Appeal Process If extenuating circumstances impacted your ability to maintain SAP, you may choose to submit an appeal.”
  - sentence: sap_appeal ⟵ “Step 1: Review Appeal Guidelines If you are not meeting the SAP policy, you may appeal for federal financial aid by submitting a Satisfactory Academic Progress (SAP) Appeal.”
  - sentence: sap_appeal ⟵ “If you’re cited for SAP and you do not appeal, are denied by the committee or are non-compliant with standards, you will lose federal financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Collect your supporting documentation and prepare it to be attached to your online appeal.”
  - sentence: sap_appeal ⟵ “View the Satisfactory Academic Progress Appeal Form(s) If you were cited for Maximum Time Frame, you must also provide a completed Maximum Time Frame form.”
### `a601a24b3d6b1f37` Kent State University at Kent — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.kent.edu/fbe-center/SAP (sha256 dc36d9a8066e)
- issues: ambiguous_year_labels, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Examples of extenuating circumstances are: death of a relative, an injury or illness of the student or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Checklist for Current Students Education Abroad & Financial Aid Enrollment Activity Aid Recalculation Financial Aid Ad Hoc Consortium Agreement Post Undergrad - Grad Non Degree - Undeclared - Combined Students Satisfactory Academic Progress Special Circumstances Summer Financial Aid Information Transfer Students Verification What's Next Be one step closer to joining our Golden Flashe”
### `be55875245a9e231` Kent State University at Kent — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.kent.edu/fbe-center/forms-requests?search=satisfactory%20appeal (sha256 d230acbe9e6b)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.kent.edu/fbe-center/SAP,https://www.kent.edu/fbe-center/scholarships-financial-aid
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You must also submit a Satisfactory Academic Progress Appeals form to be considered for student aid that requires Satisfactory Academic Progress.”
  - sentence: sap_appeal ⟵ “Complete Form + Satisfactory Academic Progress Appeal Form - 2026-2027 Satisfactory Academic Progress Appeal Form - 2026-2027 - (Dynamic Form) This form applies to the Fall 2026 and Spring 2027 semesters.”
### `e9716e03edfad0cd` Kent State University at Kent — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.kent.edu/fbe-center/forms-requests?search=satisfactory%20appeal (sha256 d230acbe9e6b)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Search Category - Any - Billing & Payments Enrollment & Registration Financial Aid Graduation Personal Information Student Records Popular Forms - Any - Verification Registration Exception Satisfactory Academic Progress (SAP) Loans Scholarships Transcript Requests Education Abroad Professional Judgment Reenrollment or Reinstatement + Maximum Time Frame Form - 2026-2027 Maximum Time Frame Form - 20”
### `13b40970aa43bf90` Kent State University at Kent — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.kent.edu/fbe-center/tuition-and-other-costs (sha256 a24ffae1ecd0)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:TUITION/FEES *: 24300 ⟵ “TUITION/FEES * | $13,850 | $24,300 | $7,834”
  - column:BOOKS, COURSE MATERIAL, SUPPLIES, AND EQUIPMENT: 800 ⟵ “BOOKS, COURSE MATERIAL, SUPPLIES, AND EQUIPMENT | $800 | $800 | $800”
  - column:STUDENT HEALTH FEE: 180 ⟵ “STUDENT HEALTH FEE | 180 | 180 | 0”
  - column:HOUSING/FOOD ALLOWANCE **: 14380 ⟵ “HOUSING/FOOD ALLOWANCE ** | $14,380 | $14,380 | $3,748”
  - column:PERSONAL EXPENSES: 2334 ⟵ “PERSONAL EXPENSES | $2,334 | $2,334 | $2,334”
  - column:TRANSPORTATION****: 2620 ⟵ “TRANSPORTATION**** | $2,620 | $2,620 | $2,872”
  - column:LOAN FEES: 68 ⟵ “LOAN FEES | $68 | $68 | $68”
  - column:CAREER SERVICES FEE: 188 ⟵ “CAREER SERVICES FEE | $188 | $188 | $112”
  - column:TOTAL: 44870 ⟵ “TOTAL | $34,420 | $44,870 | $17,768”
### `ec68cb71794c1b23` Kent State University at Kent — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.kent.edu/fbe-center/tuition-and-other-costs (sha256 a24ffae1ecd0)
- issues: arrangement_unlabeled, shared_site_attribution_review
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - column:TUITION/FEES *: 13850 ⟵ “TUITION/FEES * | $13,850 | $24,300 | $7,834”
  - column:BOOKS, COURSE MATERIAL, SUPPLIES, AND EQUIPMENT: 800 ⟵ “BOOKS, COURSE MATERIAL, SUPPLIES, AND EQUIPMENT | $800 | $800 | $800”
  - column:STUDENT HEALTH FEE: 180 ⟵ “STUDENT HEALTH FEE | 180 | 180 | 0”
  - column:HOUSING/FOOD ALLOWANCE **: 14380 ⟵ “HOUSING/FOOD ALLOWANCE ** | $14,380 | $14,380 | $3,748”
  - column:PERSONAL EXPENSES: 2334 ⟵ “PERSONAL EXPENSES | $2,334 | $2,334 | $2,334”
  - column:TRANSPORTATION****: 2620 ⟵ “TRANSPORTATION**** | $2,620 | $2,620 | $2,872”
  - column:LOAN FEES: 68 ⟵ “LOAN FEES | $68 | $68 | $68”
  - column:CAREER SERVICES FEE: 188 ⟵ “CAREER SERVICES FEE | $188 | $188 | $112”
  - column:TOTAL: 34420 ⟵ “TOTAL | $34,420 | $44,870 | $17,768”
  - column:TUITION/FEES *: 7834 ⟵ “TUITION/FEES * | $13,850 | $24,300 | $7,834”
  - column:BOOKS, COURSE MATERIAL, SUPPLIES, AND EQUIPMENT: 800 ⟵ “BOOKS, COURSE MATERIAL, SUPPLIES, AND EQUIPMENT | $800 | $800 | $800”
  - column:STUDENT HEALTH FEE: 0 ⟵ “STUDENT HEALTH FEE | 180 | 180 | 0”
  - column:HOUSING/FOOD ALLOWANCE **: 3748 ⟵ “HOUSING/FOOD ALLOWANCE ** | $14,380 | $14,380 | $3,748”
  - column:PERSONAL EXPENSES: 2334 ⟵ “PERSONAL EXPENSES | $2,334 | $2,334 | $2,334”
  - column:TRANSPORTATION****: 2872 ⟵ “TRANSPORTATION**** | $2,620 | $2,620 | $2,872”
  - column:LOAN FEES: 68 ⟵ “LOAN FEES | $68 | $68 | $68”
  - column:CAREER SERVICES FEE: 112 ⟵ “CAREER SERVICES FEE | $188 | $188 | $112”
  - column:TOTAL: 17768 ⟵ “TOTAL | $34,420 | $44,870 | $17,768”
### `f5e38a378863accc` Kent State University at Kent — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.kent.edu/admissions/transfer-student-requirements (sha256 97097fdfdb00)
- issues: conflicting_values:min_grade, shared_site_attribution_review
- checks: {"fields": []}
### `a8a2837ef0d9ea22` Miami University-Oxford — appeals 2026-27 [new] (source_unlabeled)
- source: https://miamioh.edu/onestop/financial-aid/manage-financial-aid/satisfactory-academic-progress-standards.html (sha256 71970d8b36a9)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “To appeal, the Satisfactory Academic Progress Appeal Form and the following supporting documentation must be submitted: Personal statement with the following information: A detailed account of the valid reason(s) that prevented you from maintaining SAP.”
  - sentence: sap_appeal ⟵ “Additional Information Regarding SAP Change of Major A student’s change of major can be considered as part of a SAP Appeal if the student is appealing as part of the Maximum Time Frame requirement.”
  - sentence: sap_appeal ⟵ “Students should submit the SAP Appeal Form and a statement explaining that they have raised their GPA and/or completion rate to meet the SAP Standards and wish to have their federal aid reinstated.”
  - sentence: sap_appeal ⟵ “If students are not able to re-establish eligibility by making up deficient hours, they may submit a SAP Appeal.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal A student who is not meeting one or more of Miami’s SAP Standards as outlined may submit a SAP Appeal for reconsideration of eligibility for federal aid.”
### `c9dab3419c37ee7e` Miami University-Oxford — appeals 2026-27 [new] (source_unlabeled)
- source: https://miamioh.edu/sc/admission-aid/_widgets/costs-financial-aid/glossary.html (sha256 120beb5165c0)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgement The authority of a school's financial aid administrator to make adjustments to the data elements on the FAFSA and to override a student's dependency status.”
### `42e37f1bcda11723` Miami University-Oxford — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://miamioh.edu/admission-aid/costs-financial-aid/cost-of-attendance.html (sha256 403888e3b4c2)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - on_campus:Tuition and Fees: 18890 ⟵ “Tuition and Fees | $18,890 | $42,882”
  - on_campus:Housing and Food: 17668 ⟵ “Housing and Food | $17,668 | $17,668”
  - on_campus:Total: 36558 ⟵ “Total | $36,558 | $60,550”
### `4bf156de922dd982` Miami University-Oxford — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://miamioh.edu/admission-aid/costs-financial-aid/cost-of-attendance.html (sha256 403888e3b4c2)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 42882 ⟵ “Tuition and Fees | $18,890 | $42,882”
  - column:Housing and Food: 17668 ⟵ “Housing and Food | $17,668 | $17,668”
  - column:Total: 60550 ⟵ “Total | $36,558 | $60,550”
### `7afc6517e76a2973` Ohio University-Main Campus — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.ohio.edu/financial-aid/applications-deadlines/circumstances (sha256 dd95299e9a24)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 13}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances | Ohio University Skip to main content Close Search Info for...”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances/Change of Income Special Circumstances refer to situations that may justify an aid administrator adjusting data elements on the FAFSA or budgeted expense items in the student’s annual Cost of Attendance.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Special Circumstances include loss of an income resource, parental marital status changes after FAFSA filing, or extraordinary expenses, such as medical expenses, or expenses related to the care of a dependent with disabilities.”
  - sentence: need_based_special_circumstances ⟵ “Students who believe they have Special Circumstances that justify an adjustment should reach out to their Financial Aid Advisor with a description of their circumstances after receiving the initial financial aid offer.”
  - sentence: need_based_special_circumstances ⟵ “Students who are selected for Verification must submit all requested documents before Special Circumstances can be reviewed.”
  - sentence: need_based_special_circumstances ⟵ “Families that have Special Circumstances which involve a loss of income may be required to complete our online Change of Income application.”
### `caf0a23ff1f00bf1` Ohio University-Main Campus — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ohio.edu/financial-aid/applications-deadlines/sap (sha256 7d84f3713512)
- issues: ambiguous_year_labels, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Degree must be completed within specified maximum timeframe - 90 semester hours – associate degree 111 semester hours – associate degree in nursing 180 semester hours – bachelor's degree 90 semester hours – master's degree SAP Appeals Students who do not meet SAP requirements may appeal.”
  - sentence: sap_appeal ⟵ “Student and advisor must sign the SAP Appeal Form [PDF ADA] and the academic plan.”
### `5b74d87540cafd94` Ohio University-Main Campus — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ohio.edu/admissions/freshman/costs-aid (sha256 a008c641c723)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and fees: 15018 ⟵ “Tuition and fees | $15,018”
  - column:Room(Classic Double): 8954 ⟵ “Room(Classic Double) | $8,954”
  - column:Meal Plan(Traditional 14): 5582 ⟵ “Meal Plan(Traditional 14) | $5,582”
  - column:TOTAL: 29554 ⟵ “TOTAL | $29,554”
### `fdb937dde9192147` Ohio University-Main Campus — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ohio.edu/admissions/tuition (sha256 29b4fe911b62)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition and fees: 26792 ⟵ “Tuition and fees | $26,792”
  - column:Room(Classic Double): 8954 ⟵ “Room(Classic Double) | $8,954”
  - column:Meal Plan(Traditional 14): 5582 ⟵ “Meal Plan(Traditional 14) | $5,582”
  - column:TOTAL: 41328 ⟵ “TOTAL | $41,328”
### `31f6245df77b8b27` Ohio University-Main Campus — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ohio.edu/admissions/transfer-credits/credit-examination/ap-credit-guide (sha256 18ca62b07458)
- issues: course_column_missing, shared_site_attribution_review
- checks: {"distinct_exams": 39, "equivalencies": 117, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies (10) (AAS) | 3 | AAS 1060 | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4]:  ⟵ “African American Studies (10) (AAS) | 4 | AAS 1060 | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|5]:  ⟵ “African American Studies (10) (AAS) | 5 | AAS 1060 | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History (13) (ARH) | 3 | AH 2110 | 4”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History (13) (ARH) | 4 | AH 2110, AH 2130 | 8”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “Art History (13) (ARH) | 5 | AH 2110, AH 2130 | 8”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art Studio: 2-D Design (15) (ASG)* | 3 | ART 1XXL | 3”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “Art Studio: 2-D Design (15) (ASG)* | 4 | ART 1220 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|5]:  ⟵ “Art Studio: 2-D Design (15) (ASG)* | 5 | ART 1220 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art Studio: 3-D Design (16) (ART3D) | 3 | ART 1210 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “Art Studio: 3-D Design (16) (ART3D) | 4 | ART 1210 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|5]:  ⟵ “Art Studio: 3-D Design (16) (ART3D) | 5 | ART 1210 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio: Drawing (14) (ASD)* | 3 | ART 1XXL | 3”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Art Studio: Drawing (14) (ASD)* | 4 | ART 1220 | 3”
  - equivalencies[AP-DRAWING|5]:  ⟵ “Art Studio: Drawing (14) (ASD)* | 5 | ART 1220 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology (20) (BY) | 3 | BIOS 1700, BIOS 1705 | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology (20) (BY) | 4 | BIOS 1700, BIOS 1705 | 4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology (20) (BY) | 5 | BIOS 1700, BIOS 1705 | 4”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3]:  ⟵ “Business with Personal Finance (67) (BUS) | 3 | BA 1100 | 3”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|4]:  ⟵ “Business with Personal Finance (67) (BUS) | 4 | BA 1100 | 3”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|5]:  ⟵ “Business with Personal Finance (67) (BUS) | 5 | BA 1100 | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB (66) (MAB) | 3 | MATH 2301 | 4”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB (66) (MAB) | 4 | MATH 2301 | 4”
  - equivalencies[AP-CALCULUS-AB|5]:  ⟵ “Calculus AB (66) (MAB) | 5 | MATH 2301 | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC (68) (MBC) | 3 | MATH 2301, MATH 2302 | 8”
  - … 92 more rows
### `66844cdbf3f6f9f4` Ohio University-Main Campus — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ohio.edu/admissions/transfer-credits/credit-examination/college-level-examination-program-clep (sha256 8f4d4e9996ff)
- issues: score_scale_mismatch, shared_site_attribution_review
- checks: {"distinct_exams": 31, "equivalencies": 51, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|63 and above]:  ⟵ “American Government | 63 and above | POLS 1010 | American National Government | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|56-62]:  ⟵ “American Government | 56-62 | OT36 Social Sciences Credit | OT36 Social Sciences Credit | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|53 and above]:  ⟵ “American Literature | 53 and above | OT36 Arts and Humanities | OT36 Arts and Humanities Credit | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|59 and above]:  ⟵ “Analyzing andInterpreting Literature | 59 and above | OT36 Arts and Humanities | OT36 Arts and Humanities Credit | 3”
  - equivalencies[CLEP-BIOLOGY|70 and above]:  ⟵ “Biology | 70 and above | BIOS 1700 | Biological Sciences I: Molecules and Cells | 3”
  - equivalencies[CLEP-BIOLOGY|55-69]:  ⟵ “Biology | 55-69 | BIOS 1030 | Human Biology I: Basic Principles | 3”
  - equivalencies[CLEP-BIOLOGY|50-54]:  ⟵ “Biology | 50-54 | OT36 Natural Sciences Credit without Labs | OT36 Natural Sciences Credit without Labs | 3”
  - equivalencies[CLEP-CALCULUS|64 and above]:  ⟵ “Calculus | 64 and above | MATH 2301 | Calculus I | 4”
  - equivalencies[CLEP-CHEMISTRY|60 and above]:  ⟵ “Chemistry | 60 and above | OT36 Natural Sciences Credit without Labs | OT36 Natural Sciences Credit without Labs | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|63 and above]:  ⟵ “College Algebra | 63 and above | MATH 1200 | College Algebra | 4”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|63 and above]:  ⟵ “College Mathematics | 63 and above | OT36 Mathematics, Statistics, and Logic | OT36 Mathematics, Statistics, and Logic | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|63 and above]:  ⟵ “English Literature | 63 and above | OT36 Arts and Humanities | OT36 Arts and Humanities Credit | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|65 and above]:  ⟵ “Financial Accounting | 65 and above | ACCT 1010 | Foundations of Accounting | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|65 and above]:  ⟵ “French Language | 65 and above | FR 1110 | Elementary French I | 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|FR 1120]:  ⟵ “French Language | FR 1120 | Elementary French II | 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|FR 2110]:  ⟵ “French Language | FR 2110 | Intermediate French I | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|FR 2120]:  ⟵ “French Language | FR 2120 | Intermediate French II | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|55-64]:  ⟵ “French Language | 55-64 | FR 1110 | Elementary French I | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|67 and above]:  ⟵ “German Language | 67 and above | GER 1110 | Elementary German I | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|GER 1120]:  ⟵ “German Language | GER 1120 | Elementary German II | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|GER 2110]:  ⟵ “German Language | GER 2110 | Intermediate German I | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|59-66]:  ⟵ “German Language | 59-66 | GER 1110 | Elementary German I | 4”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|61 and above]:  ⟵ “History of the United States I | 61 and above | HIST 2000 | Survey of United States History, 1600-1877 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|57 and above]:  ⟵ “History of the United States II | 57 and above | HIST 2010 | Survey of United States History, 1865-Present | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|58 and above]:  ⟵ “Human Growth and Development | 58 and above | Psychology Elective Credit (for Psychology majors) or OT36 Social SciencesCredit (for Non-Psychology majors) | Psychology Elective Credit (for Psychology majors) or OT36 Social Sciences Credit (for Non-Psychology majors) | 3”
  - … 26 more rows
### `909850bf3d2c7964` Ohio University-Main Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.ohio.edu/admissions/transfer-credits/credit-examination/international-baccalaureate-credit-guide (sha256 39d42228dee7)
- issues: credits_implausible, shared_site_attribution_review
- checks: {"distinct_exams": 25, "equivalencies": 74, "rows_without_score": 0}
  - equivalencies[IB-FILM|SL 5+]:  ⟵ “Film | IFILS | SL | 5+ | FILM 1800 | 4.0”
  - equivalencies[IB-FILM|HL 4+]:  ⟵ “Film | IFILH | HL | 4+ | FILM 1800 | 4.0”
  - equivalencies[IB-MUSIC|SL 5+]:  ⟵ “Music | IMUSS | SL | 5+ | MUS 1250 | 3.0”
  - equivalencies[IB-MUSIC|HL 4+]:  ⟵ “Music | IMUSH | HL | 4+ | MUS 1250 | 3.0”
  - equivalencies[IB-THEATRE|SL 5+]:  ⟵ “Theatre | ITHES | SL | 5+ | THAR 1710 | 3.0”
  - equivalencies[IB-THEATRE|HL 4+]:  ⟵ “Theatre | ITHEH | HL | 4+ | THAR 1710 | 3.0”
  - equivalencies[IB-VISUAL-ARTS|SL 4]:  ⟵ “Visual Arts | IARTS | SL | 4 | ART 1240 | 3.0”
  - equivalencies[IB-VISUAL-ARTS|SL 5+]:  ⟵ “Visual Arts | IARTS | SL | 5+ | ART 1240 | 3.0”
  - equivalencies[IB-VISUAL-ARTS|HL 4+]:  ⟵ “Visual Arts | IARTH | HL | 4+ | ART 1240 | 3.0”
  - equivalencies[IB-BUSINESS-MANAGEMENT|SL 4+]:  ⟵ “Business Management | IBUMS | SL | 4+ | BA 1XXL | 3.0”
  - equivalencies[IB-BUSINESS-MANAGEMENT|HL 4+]:  ⟵ “Business Management | IBUMH | HL | 4+ | BA 1XXL | 3.0”
  - equivalencies[IB-ECONOMICS|SL 4]:  ⟵ “Economics | IECOS | SL | 4 | ECON 1000 | 3.0”
  - equivalencies[IB-ECONOMICS|SL 5+]:  ⟵ “Economics | IECOS | SL | 5+ | ECON 1030, ECON 1040 | 6.0”
  - equivalencies[IB-ECONOMICS|HL 4+]:  ⟵ “Economics | IECOH | HL | 4+ | ECON 1030, ECON 1040 | 6.0”
  - equivalencies[IB-GLOBAL-POLITICS|SL 4]:  ⟵ “Global Politics | IGLPS | SL | 4 | POLS 1XXL | 3.0”
  - equivalencies[IB-GLOBAL-POLITICS|SL 5+]:  ⟵ “Global Politics | IGLPS | SL | 5+ | POLS 1500 | 3.0”
  - equivalencies[IB-GLOBAL-POLITICS|HL 4+]:  ⟵ “Global Politics | IGLPH | HL | 4+ | POLS 1500 | 3.0”
  - equivalencies[IB-HISTORY|SL 4]:  ⟵ “History | IHISS | SL | 4 | HIST 1XXL | 3.0”
  - equivalencies[IB-HISTORY|SL 5+]:  ⟵ “History | IHISS | SL | 5+ | HIST 1330 | 3.0”
  - equivalencies[IB-HISTORY|HL 4+]:  ⟵ “History Africa and Middle East | IHAMH | HL | 4+ | HIST 1XXL | 3.0”
  - equivalencies[IB-HISTORY|HL 4+]:  ⟵ “History Europe | IHIEH | HL | 4+ | HIST 1210 | 3.0”
  - equivalencies[IB-HISTORY|SL 5+]:  ⟵ “Modern History of Kazakhstan | IKAZS | SL | 5+ | HIST 1XXL | 3.0”
  - equivalencies[IB-PHILOSOPHY|SL 5+]:  ⟵ “Philosophy | IPHIS | SL | 5+ | PHIL 1010 | 3.0”
  - equivalencies[IB-PHILOSOPHY|HL 4+]:  ⟵ “Philosophy | IPHIH | HL | 4+ | PHIL 1010 | 3.0”
  - equivalencies[IB-PSYCHOLOGY|SL 4+]:  ⟵ “Psychology | IPSYS | SL | 4+ | PSY 1010 | 3.0”
  - … 49 more rows
### `ma2410a2e53ff664` Ohio University-Main Campus — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ohio.edu/admissions/transfer-credits (sha256 942fddec81b5)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: D- ⟵ “In general, college level courses taken at a Council for Higher Education (CHEA) recognized institution with accreditation meeting OHIO's transfer policy will transfer to Ohio University with a grade of "D-" or better.”
  - min_grade: D- ⟵ “The following courses generally transfer: Dual enrollment credits in college-level courses completed at a Council for Higher Education (CHEA) recognized institution with accreditation meeting OHIO's transfer policy with a grade of D- or better.”
  - min_grade: D- ⟵ “The following courses generally transfer: Dual enrollment credits in college-level courses completed at a Council for Higher Education (CHEA) recognized institution with accreditation meeting OHIO's transfer policy with a grade of D- or better.”
  - min_grade: D- ⟵ “In general, college level courses taken at a Council for Higher Education (CHEA) recognized institution with accreditation meeting OHIO's transfer policy will transfer to Ohio University with a grade of "D-" or better.”
  - min_grade: D- ⟵ “The following courses generally transfer: Dual enrollment credits in college-level courses completed at a Council for Higher Education (CHEA) recognized institution with accreditation meeting OHIO's transfer policy with a grade of D- or better.”
### `33a5528dfab0db88` Sinclair Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sinclair.edu/admissions/direct-admission-program/ (sha256 2d91a778bcf3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “However, life happens, so there is a SAP Appeal available if your status becomes ineligible.”
  - sentence: sap_appeal ⟵ “You are required to either meet the above SAP requirements or have an approved SAP Appeal on file to qualify for scholarship funding through the Sinclair Direct Promise program.”
### `c2ca14d8afb58b51` Sinclair Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sinclair.edu/admissions/fafsa-workshops/ (sha256 e737dd2f546d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “We offer one-on-one appointments with a Financial Aid Officer for the following topics: Special Circumstance Appeal Income changes, separation, loss of income, and related circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance Appeal Dependency Status questions on the FAFSA do not apply to the student, but the student cannot obtain parent data.”

## Re-verification of existing records (189)

- source_not_fetched: data/institutions/aultmancollege/awards/2026-27.json ["awards", "ipeds-201177", null, "2026-27", {"award_name": "Faculty"}]
- source_not_fetched: data/institutions/aultmancollege/awards/2026-27.json ["awards", "ipeds-201177", null, "2026-27", {"award_name": "Caduceus"}]
- source_not_fetched: data/institutions/aultmancollege/awards/2026-27.json ["awards", "ipeds-201177", null, "2026-27", {"award_name": "Trustee"}]
- source_not_fetched: data/institutions/aultmancollege/awards/2026-27.json ["awards", "ipeds-201177", null, "2026-27", {"award_name": "Dean"}]
- source_not_fetched: data/institutions/aultmancollege/awards/2026-27.json ["awards", "ipeds-201177", null, "2026-27", {"award_name": "Aully"}]
- source_not_fetched: data/institutions/bluffton/credit_policies/2026-27.json ["credit_policies", "ipeds-201371", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/bryantstratton-201469/transfer_policies/2026-27.json ["transfer_policies", "ipeds-201469", null, "2026-27", {}]
- source_not_fetched: data/institutions/capital/awards/2026-27.json ["awards", "ipeds-201548", null, "2026-27", {"award_name": "National Merit Scholarship Program"}]
- source_not_fetched: data/institutions/capital/awards/2026-27.json ["awards", "ipeds-201548", null, "2026-27", {"award_name": "Conservatory Performance Award"}]
- source_not_fetched: data/institutions/capital/awards/2026-27.json ["awards", "ipeds-201548", null, "2026-27", {"award_name": "Music Composition Scholarship"}]
- source_not_fetched: data/institutions/capital/awards/2026-27.json ["awards", "ipeds-201548", null, "2026-27", {"award_name": "Sibling Award"}]
- source_not_fetched: data/institutions/capital/awards/2026-27.json ["awards", "ipeds-201548", null, "2026-27", {"award_name": "Lutheran Heritage Grant"}]
- source_not_fetched: data/institutions/capital/awards/2026-27.json ["awards", "ipeds-201548", null, "2026-27", {"award_name": "Partners in Education"}]
- source_not_fetched: data/institutions/case/degree_requirements/2026-27.json ["degree_requirements", "ipeds-201645", null, "2026-27", {"program_key": "cognitive-science-ba", "requirement_key": "program-requirements-required-courses"}]
- source_not_fetched: data/institutions/case/degree_requirements/2026-27.json ["degree_requirements", "ipeds-201645", null, "2026-27", {"program_key": "sociology-ba", "requirement_key": "program-requirements-required-courses"}]
- source_not_fetched: data/institutions/cedarville/credit_policies/2026-27.json ["credit_policies", "ipeds-201654", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/clarkstate/credit_policies/2026-27.json ["credit_policies", "ipeds-201973", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/ccad/awards/2026-27.json ["awards", "ipeds-202170", null, "2026-27", {"award_name": "Seniors Gold Key and Gold Key portfolios"}]
- source_not_fetched: data/institutions/ccad/awards/2026-27.json ["awards", "ipeds-202170", null, "2026-27", {"award_name": "Seniors American Visions"}]
- source_not_fetched: data/institutions/ccad/awards/2026-27.json ["awards", "ipeds-202170", null, "2026-27", {"award_name": "Seniors Silver Key and Silver Key portfolios"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Abbott Endowed Scholarship in Biological & Physical Sciences"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Abbott Endowed Scholarship in Sports & Exercise Studies"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Accounting & Finance Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Ad Maiora - M. Upshaw Family Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Advance Auto Parts Foundation Future Technicians Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "AEP Sustainable Building Certificate Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Alumni Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Amazon Web Services (AWS) Community Builder Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "American Culinary Federation Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "American Institute of Architects (AIA) Columbus Chapter Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Andrew William \"Chef Mitch\" Mitchell Endowed Culinary Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Angela Atwood Memorial Logistics Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Automotive Maintenance Technology Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Barb Lining Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Barbara Brandt Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Batelle Endowed Scholarship in Math & Science"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Beth McGrath Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Betty Bouwman Dublin Center Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Bob & Mary Frances Restrepo Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Bryant Dealers Habeggar Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Business Career Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Caley-Greer Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Campos Moeller Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Captain Nicholas Rozanski Fire Science and EMS Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Cardinal Health Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Carolyn Kaufman Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Central Ohio Professional Land Surveyors Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "CESO Surveying Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Changing the Narrative Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Chase Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Chase Your Dreams Work Program"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Chef Boiardi Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Chenelle Family Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Chris Sayre Memorial Automotive Technology Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Clarence Carl Chaffee and Popy Golemes Chaffee Scholarship Endowment for Student Excellence"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "College Start Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Columbus State Education Association Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Connie Grossman Dental Hygiene Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Construction Financial Management Association Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Construction Sciences Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Cowher Fund for Career Pathing"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "CSCC Partnership Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Daryl L. Cullison Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "David Mierzejewski Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "DDP Architectural Design Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Deborah Bertsch Endowed Scholarship Fund"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Delaware Campus Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "DesignGroup Construction Trade Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "DLZ/Saralabai Naik Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "DOE Title III Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Dominion Homes Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Dorothy Kroeger Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "DR&HF Robinson Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Dr. Charlie Gallucci Phi Theta Kappa Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Dr. Daniel D. and Joanne H. Hall Legacy Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Dr. David Litt Memorial Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Dr. Rohini Desai Mulchandani Scholarship, Endowed"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Dr. William Dross & IAAP Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Dwight and Renee Smith \"Thanks Be to God\" Foundation Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Earl R. Schaeffer Memorial Social Sciences Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "First Generation Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Frank B. Kroeger Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Frank Hirschvogel Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Fred Boso Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Future Scientists Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "George Floyd Memorial Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Giant Eagle Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Greg Golden Memorial/ERC Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Hamilton Parker/Lewin Family Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Harold Hamler and Margaret Hamler, R.N. Nursing Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Harold M. Nestor Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Hasneara Khanam Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Hazel Nicklaus Annuity Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Henry Family Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Honda of America Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Hourglass Foundation \"More Than One Path\" Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Huntington National Bank Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Huntington Success Program"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "ITService Alliance STEM Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Janet E. Jackson Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Jay Benedict Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "JC Penney Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Jeffrey Lehner Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Jill M Edgington Endowed Nursing Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "John M. McCormac Memorial Endowed Scholarship in EMS"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "John S. Riley II Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Kathryn Croson Respiratory Therapist Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Katz Family Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Kelley D. Shelton Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Kenneth B. Ackerman CSCMP Supply Chain & Logistics Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Key Bank Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Konica Minolta Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Larry Lance Math Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Limited Inc. Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Lt. Alan Washer Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Manifest Solutions Pathways Scholarship, Endowed"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Mary Babcock Estate Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Michael D. Forrest Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Mike Stancil Student Book Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "National Board for Respiratory Care Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Nationwide Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Nurturing the Nursing Profession Endowed Scholarship in Memory of Adgas & Ismail"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Ohio Children's Foundation Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Ohio Department of Education Pre-K Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Opportunity Linden Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Patricia Keats Kasile Memorial Endowed"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Radigan Alaimo Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Real Estate Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Renee Deveaux Phi Theta Kappa Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Robert Harris Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Roberta L. Robinson RN Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Ronald A. Shillingburg Memorial Scholarship Fund"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Ruth & Harry Sabgir Nursing Education Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Southeast, Inc. Scholarship for Re-entry"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Stan Ross Memorial Music Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "State Auto IT Flexible Apprenticeship Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Stephen Wilson Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "The Superior Group Endowed Scholarship for Construction and Skilled Trades"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Sysco Central Ohio Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Tadd & Nancy Seitz Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "The Chef Wiley Bates Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "The I Am One Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Thompson-Haase Memorial"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Timberlake Massage Therapy Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Union Tools Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "UP! App Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "US Bank Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Victor Lucas Non-Custodial Parent Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Vince Borghese Family Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Virginia Carey Memorial Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "Wasserstrom Family Endowed Scholarship"}]
- source_not_fetched: data/institutions/cscc/awards/2026-27.json ["awards", "ipeds-202222", null, "2026-27", {"award_name": "William C. Johannes Veterans Endowed Veterans Award"}]
- source_not_fetched: data/institutions/tri-c/credit_policies/2026-27.json ["credit_policies", "ipeds-202356", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/franciscan/credit_policies/2026-27.json ["credit_policies", "ipeds-205957", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/lakelandcc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-203599", null, "2026-27", {}]
- source_not_fetched: data/institutions/lorainccc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-203748", null, "2026-27", {"program_key": "rn-to-bsn-completion-program-bachelor-of-science-in-nursing", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/malone/transfer_policies/2026-27.json ["transfer_policies", "ipeds-203775", null, "2026-27", {}]
- source_not_fetched: data/institutions/mtc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-203881", null, "2026-27", {}]
- source_not_fetched: data/institutions/msj/transfer_policies/2026-27.json ["transfer_policies", "ipeds-204200", null, "2026-27", {}]
- source_not_fetched: data/institutions/mvnu/credit_policies/2026-27.json ["credit_policies", "ipeds-204194", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/oberlin/transfer_policies/2026-27.json ["transfer_policies", "ipeds-204501", null, "2026-27", {}]
- source_not_fetched: data/institutions/ohiodominican/awards/2026-27.json ["awards", "ipeds-204617", null, "2026-27", {"award_name": "Band"}]
- source_not_fetched: data/institutions/ohiodominican/awards/2026-27.json ["awards", "ipeds-204617", null, "2026-27", {"award_name": "Chorus"}]
- source_not_fetched: data/institutions/ohiodominican/awards/2026-27.json ["awards", "ipeds-204617", null, "2026-27", {"award_name": "Cheerleading"}]
- source_not_fetched: data/institutions/ohiodominican/awards/2026-27.json ["awards", "ipeds-204617", null, "2026-27", {"award_name": "Honors Program"}]
- source_not_fetched: data/institutions/uakron/degree_requirements/2026-27.json ["degree_requirements", "ipeds-200800", null, "2026-27", {"program_key": "biology-bs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uakron/degree_requirements/2026-27.json ["degree_requirements", "ipeds-200800", null, "2026-27", {"program_key": "business-administration-bba", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uakron/degree_requirements/2026-27.json ["degree_requirements", "ipeds-200800", null, "2026-27", {"program_key": "food-and-nutrition-sciences-bs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/walsh/awards/2026-27.json ["awards", "ipeds-206437", null, "2026-27", {"award_name": "Baxter Honors Scholarship"}]
- source_not_fetched: data/institutions/walsh/awards/2026-27.json ["awards", "ipeds-206437", null, "2026-27", {"award_name": "Blouin Scholars Program"}]
- source_not_fetched: data/institutions/walsh/awards/2026-27.json ["awards", "ipeds-206437", null, "2026-27", {"award_name": "Deshayes Scholarship"}]
- source_not_fetched: data/institutions/walsh/awards/2026-27.json ["awards", "ipeds-206437", null, "2026-27", {"award_name": "Vanasse Scholarship"}]
- source_not_fetched: data/institutions/walsh/awards/2026-27.json ["awards", "ipeds-206437", null, "2026-27", {"award_name": "Brothers of Christian Instruction Scholarship"}]
- source_not_fetched: data/institutions/walsh/awards/2026-27.json ["awards", "ipeds-206437", null, "2026-27", {"award_name": "LaMennais Award"}]
- source_not_fetched: data/institutions/walsh/awards/2026-27.json ["awards", "ipeds-206437", null, "2026-27", {"award_name": "Farrell Award"}]
- source_not_fetched: data/institutions/wright/credit_policies/2026-27.json ["credit_policies", "ipeds-206604", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/wright/transfer_policies/2026-27.json ["transfer_policies", "ipeds-206604", null, "2026-27", {}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-business-administration-in-management", "requirement_key": "student-experiences-supply-chain-concentration"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-biological-sciences", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-computer-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-applied-science-in-information-technology", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-applied-science-in-civil-and-construction-engineering-tec", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-geographic-information-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-mathematics", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-applied-science-in-public-health", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-applied-science-in-electrical-engineering-technology", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-applied-science-in-mechanical-engineering-technology", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-engineering-in-civil-engineering", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ysu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-206695", null, "2026-27", {"program_key": "bachelor-of-science-in-business-administration-in-human-resource-management", "requirement_key": "sample-plan"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Bowling Green State University-Main Campus: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Kent State University at Kent: admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Miami University-Oxford: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency
- Ohio State University-Main Campus: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency
- Ohio University-Main Campus: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- Sinclair Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- University of Cincinnati-Main Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
