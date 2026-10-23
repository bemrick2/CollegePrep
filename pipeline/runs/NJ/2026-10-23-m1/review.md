# Review queue — NJ (2026-27)

Pages fetched: 180; failures: 10. Candidates: 24 (1 without issues, 23 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 6 | 1 | 0 | 1 | 1 | 0 | 64 |
| cost_of_attendance | 2 | 1 | 0 | 1 | 1 | 0 | 68 |
| admissions_tests | 0 | 0 | 0 | 1 | 1 | 0 | 71 |
| common_data_set | 0 | 0 | 0 | 1 | 0 | 1 | 71 |
| merit_scholarships | 0 | 2 | 0 | 0 | 2 | 0 | 69 |
| ap_credit | 0 | 4 | 0 | 0 | 0 | 2 | 67 |
| clep_credit | 0 | 1 | 0 | 0 | 1 | 1 | 70 |
| ib_credit | 0 | 1 | 0 | 0 | 0 | 2 | 70 |
| dual_enrollment | 1 | 5 | 0 | 0 | 2 | 0 | 65 |
| transfer_credit | 1 | 10 | 0 | 0 | 1 | 0 | 61 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 2 | 71 |
| residency | 0 | 0 | 0 | 0 | 2 | 0 | 71 |
| degree_requirements | 3 | 0 | 0 | 0 | 1 | 1 | 68 |
| aid_appeals | 0 | 0 | 0 | 2 | 0 | 0 | 71 |

## Ready for review (1)

### `92289f13e1d125af` Montclair State University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.montclair.edu/admissions-aid/transfer-students (sha256 104f59937d03)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “What Credits Transfer Courses at the 100 level or higher with a grade of C- or higher, and “P,” “CR,” or “S” grades, are accepted for full credit.”
  - min_grade: C- ⟵ “In general, no: only grades of C- or better are accepted in transfer; however there are two exceptions: When a D grade is earned through an associate degree (AA, AS, or AFA) from a community college.”

## Exceptions (23)

### `1d1ed69beef097ec` Montclair State University — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://irdata.montclair.edu/institutionalresearch/CDS/Bloomfield%20CDS%202025-2026.pdf (sha256 fef42be6f7ae)
- issues: conflicting_sources:https://irdata.montclair.edu/institutionalresearch/CDS/CDS%202025-2026.pdf
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 1316 ⟵ “Total first-time, first-year (degree-seeking) who applied                                               1152                141            22             1           1316”
  - admits: 905 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                                          806                 87             9             3            905”
  - enrolled: 139 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                                               129                  4             2             4            139”
### `44d450bc6aab1a74` Montclair State University — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://irdata.montclair.edu/institutionalresearch/CDS/CDS%202025-2026.pdf (sha256 fb766f5faad8)
- issues: conflicting_sources:https://irdata.montclair.edu/institutionalresearch/CDS/Bloomfield%20CDS%202025-2026.pdf
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 26224 ⟵ “Total first-time, first-year (degree-seeking) who applied                                             21206                 3559          1459             0       26224”
  - admits: 23443 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                                       19137                 3086          1220             0       23443”
  - enrolled: 3816 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                                             3590                  175            51             0         3816”
  - sat_composite_25..75: [850, 1000, 1160] ⟵ “SAT Composite                                            850                   1000                  1160”
  - sat_reading_25..75: [430, 520, 600] ⟵ “SAT Evidence-Based Reading and   430                    520                  600”
  - sat_math_25..75: [418, 480, 560] ⟵ “SAT Math                                                 418                    480                  560”
### `58d77dee3ad8cb3a` Montclair State University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://irdata.montclair.edu/institutionalresearch/CDS/CDS%202024-2025.pdf (sha256 f339450adf77)
- issues: applications_breakdown_does_not_reconcile, admits_breakdown_does_not_reconcile, enrolled_breakdown_does_not_reconcile, stale_year_label:2024-25
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 0 ⟵ “Total first-time, first-year who applied                                                                 26257              21495          3602          1160             0”
  - admits: 0 ⟵ “Total first-time, first-year who were admitted                                                           23076              19005          3103           968             0”
  - enrolled: 0 ⟵ “Total first-time, first-year who enrolled                                                                 4109                3854          182            73             0”
  - sat_composite_25..75: [930, 1080, 1200] ⟵ “SAT Composite                                930                             1080                   1200”
  - sat_reading_25..75: [480, 550, 620] ⟵ “SAT Evidence-Based Reading and Writing       480                              550                    620”
  - sat_math_25..75: [430, 520, 590] ⟵ “SAT Math                                     430                              520                    590”
### `02f52339e863e27c` Montclair State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.montclair.edu/admissions-aid/financial-aid (sha256 9caf9e45e23c)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office,https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office/appeals-and-special-circumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Complete the FAFSA with your information and indicate that you have unusual circumstances (there is a check-off box).”
### `74c028d7b593e8ce` Montclair State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office/appeals-and-special-circumstances (sha256 40b68093e9b2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “These cases may qualify for a dependency override.”
### `8691f1f783a7d117` Montclair State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office/appeals-and-special-circumstances (sha256 40b68093e9b2)
- issues: semantic_review_required, conflicting_sources:https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office,https://www.montclair.edu/admissions-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Changes to your family’s financial situation → Special Circumstances (SAI Appeal) Unable to provide parent information → Unusual Circumstances Appeal Not meeting academic progress requirements → Visit Financial Aid Eligibility (SAP) Special Circumstances (SAI Appeal) What Are Special Circumstances?”
  - sentence: need_based_special_circumstances ⟵ “Important to Know About Special Circumstances You must receive your initial financial aid offer before submitting a request Incoming students must: Be accepted Pay their deposit File a FAFSA Unusual Circumstances (Dependency Appeal) What Are Unusual Circumstances?”
  - sentence: need_based_special_circumstances ⟵ “Filing a Request for Review or Unusual Circumstances appeal will not change loan eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Important to Know About Unusual Circumstances Approval is not guaranteed.”
### `ae088b65956234df` Montclair State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office (sha256 2c51f5481b01)
- issues: semantic_review_required, conflicting_sources:https://inside.montclair.edu/resources/red-hawk-central/financial-aid-office/appeals-and-special-circumstances,https://www.montclair.edu/admissions-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “File Your FAFSA More in Financial Aid Office Appeals and Special Circumstances Federal Financial Aid Changes Financial Aid Checklist Financial Aid Eligibility Financial Aid for Study Abroad Grants and Scholarships HEERF Funding and Compliance Reporting Loan Information New Jersey Dream Act Student Handbook for Financial Aid Summer Financial Aid Types of Financial Aid Grants Grants are typically ne”
### `136710e314003b77` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/appeals/income-adjustment.html (sha256 7c7be8c723c2)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “These types of adjustments are made in accordance with our Professional Judgment Policy on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “Once in the system, click on “Request” at the top, right corner of the page then select "Professional Judgment: Special Circumstance EFC/SAI Appeal." If multiple award years are open, please pay special attention to the award year for which you are submitting an appeal.”
### `5b9427babbb8cffe` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/appeals/dependency.html (sha256 db762664e6a5)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Federal guidelines stipulate the following conditions do not solely qualify as circumstances meriting a dependency override: Parent refusal to contribute to the student’s education Parent unwillingness to provide information on the FAFSA or to provide required verification documentation Parent does not claim the student as a dependent for income tax purposes Student demonstrates total self-suffici”
### `6253edd3d46ad129` Rowan University — appeals 2026-27 [new] (labeled_in_source)
- source: https://svm.rowan.edu/admissions-menu/financial-aid/cost-of-attendance.html (sha256 137a4ce22a01)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Cost of Attendance Appeals (Budget Adjustment Appeal) What is a Cost of Attendance (COA) Appeal?”
  - sentence: budget_increase ⟵ “Important Notes Budget adjustments are based on educational necessity, not lifestyle preferences.”
### `6f11882eb5a2f6ec` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html (sha256 4ced4329f0ef)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Select the Reason for your Appeal SAP Appeal for GPA and/or PACE The appeal process requires the student to explain the circumstances that prevented you from meeting SAP requirements.”
  - sentence: sap_appeal ⟵ “SAP Appeal for Maximum Timeframe The appeal process requires a personal statement explaining why you have not yet completed your degree program.”
  - sentence: sap_appeal ⟵ “This form must be uploaded to your SAP appeal in your online portal.”
### `9c6172281ff488b4` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/tuition-free/faq.html (sha256 4903039bed72)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/appeals/dependency.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “If you meet one of the criteria to be considered an independent student on the FAFSA, and so were not required to include parental information on the FAFSA; or you are approved for a dependency status appeal, then we will use your AGI to determine eligibility.”
### `abba3b3bd214671f` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/appeals/ (sha256 6abe1dd46c97)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/dependency.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Status Appeal Students who are unable to provide parents' information on their FAFSA, should consider this appeal.”
### `bc69341d235c45d0` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/tuition-free/faq.html (sha256 4903039bed72)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/income-adjustment.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “When the family circumstances change, you may qualify to have your aid eligibility reconsidered through an appeal process known as professional judgment.”
### `d9c328a69618016e` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/appeals/ (sha256 6abe1dd46c97)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Students who have been notified by our office that are not meeting Satisfactory Academic Progress (SAP), should consider this appeal.”
### `dfa620d7a748f4cf` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/tuition-free/faq.html (sha256 4903039bed72)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “When you re-establish eligibility for financial aid by meeting the standards for Satisfactory Academic Progress (SAP) or successfully appeal your SAP aid suspension, you will regain eligibility for the Rowan Opportunity Program/Garden State Guarantee as well.”
### `f3576f65f02f7c9f` Rowan University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/sap-policy.html (sha256 436e90f8db99)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://sites.rowan.edu/financial-aid/appeals/,https://sites.rowan.edu/financial-aid/eligibility/satisfactory-academic-progress/appeal.html,https://sites.rowan.edu/financial-aid/tuition-free/faq.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Probation Continuing students are placed on financial aid probation after having a SAP appeal completed and approved.”
### `0646eb71f041e0fb` Rowan University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://cmsru.rowan.edu/admissions/financial-aid-services/cost-of-attendance.html (sha256 ff17b67fdfb6)
- issues: conflicting_sources:https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2627.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition*: 78086 ⟵ “Tuition* | $50,680 | $78,086 | ”
  - on_campus:Student Fees*: 2641 ⟵ “Student Fees* | $2,641 | $2,641 | ”
  - on_campus:Direct Loan Origination Fee: 528 ⟵ “Direct Loan Origination Fee | $528 | $528 | ”
  - on_campus:Books & Supplies: 1600 ⟵ “Books & Supplies | $1,600 | $1,600 | ”
  - on_campus:Food & Housing**: 24200 ⟵ “Food & Housing** | $24,200 | $24,200 | ”
  - on_campus:Transportation: 4950 ⟵ “Transportation | $4,950 | $4,950 | ”
  - on_campus:Personal: 2200 ⟵ “Personal | $2,200 | $2,200 | ”
  - on_campus:Total: 114205 ⟵ “Total | $86,799 | $114,205 | ”
### `7999da0b107ca056` Rowan University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2627.html (sha256 0617bc13832d)
- issues: conflicting_sources:https://cmsru.rowan.edu/admissions/financial-aid-services/cost-of-attendance.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition & Fees: 18300 ⟵ “Tuition & Fees | $18,300”
  - column:Books, Course Materials, Supplies, Equipment: 1330 ⟵ “Books, Course Materials, Supplies, Equipment | $1,330”
  - column:Housing: 11897 ⟵ “Housing | $11,897”
  - column:Food: 5693 ⟵ “Food | $5,693”
  - column:Personal Spending: 3080 ⟵ “Personal Spending | $3,080”
  - column:Transportation Expenses: 2322 ⟵ “Transportation Expenses | $2,322”
  - column:Federal Loan Fees: 44 ⟵ “Federal Loan Fees | $44”
  - column:TOTAL: 42666 ⟵ “TOTAL | $42,666”
### `89bb01e9ba8cbb93` Rowan University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2627.html (sha256 0617bc13832d)
- issues: conflicting_sources:https://cmsru.rowan.edu/admissions/financial-aid-services/cost-of-attendance.html
- checks: {"columns": 1, "rows": 8}
  - column:Tuition & Fees: 29664 ⟵ “Tuition & Fees | $29,664”
  - column:Books, Course Materials, Supplies, Equipment: 1330 ⟵ “Books, Course Materials, Supplies, Equipment | $1,330”
  - column:Housing: 11897 ⟵ “Housing | $11,897”
  - column:Food: 5693 ⟵ “Food | $5,693”
  - column:Personal Spending: 3080 ⟵ “Personal Spending | $3,080”
  - column:Transportation Expenses: 2922 ⟵ “Transportation Expenses | $2,922”
  - column:Federal Loan Fees: 44 ⟵ “Federal Loan Fees | $44”
  - column:TOTALS: 54630 ⟵ “TOTALS | $54,630”
### `9ad86e745eea0f2d` Rowan University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://cmsru.rowan.edu/admissions/financial-aid-services/cost-of-attendance.html (sha256 ff17b67fdfb6)
- issues: conflicting_sources:https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2627.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition*: 50680 ⟵ “Tuition* | $50,680 | $78,086 | ”
  - on_campus:Student Fees*: 2641 ⟵ “Student Fees* | $2,641 | $2,641 | ”
  - on_campus:Direct Loan Origination Fee: 528 ⟵ “Direct Loan Origination Fee | $528 | $528 | ”
  - on_campus:Books & Supplies: 1600 ⟵ “Books & Supplies | $1,600 | $1,600 | ”
  - on_campus:Food & Housing**: 24200 ⟵ “Food & Housing** | $24,200 | $24,200 | ”
  - on_campus:Transportation: 4950 ⟵ “Transportation | $4,950 | $4,950 | ”
  - on_campus:Personal: 2200 ⟵ “Personal | $2,200 | $2,200 | ”
  - on_campus:Total: 86799 ⟵ “Total | $86,799 | $114,205 | ”
### `cb59f72f903d8367` Rowan University — costs 2025-26 · residency=out_of_state [same] (labeled_in_source)
- source: https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2526.html (sha256 783ed052ccc2)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 8}
  - column:Tuition & Fees: 28252 ⟵ “Tuition & Fees | 28,252”
  - column:Books, Course Materials, Supplies, Equipment: 1330 ⟵ “Books, Course Materials, Supplies, Equipment | 1,330”
  - column:Housing: 11550 ⟵ “Housing | 11,550”
  - column:Food: 5474 ⟵ “Food | 5,474”
  - column:Personal Spending: 2993 ⟵ “Personal Spending | 2,993”
  - column:Transportation Expenses: 3549 ⟵ “Transportation Expenses | 3,549”
  - column:Federal Loan Fees: 44 ⟵ “Federal Loan Fees | 44”
  - column:TOTALS: 53192 ⟵ “TOTALS | 53,192”
### `e97aed67179863ba` Rowan University — costs 2025-26 · residency=in_state [same] (labeled_in_source)
- source: https://sites.rowan.edu/financial-aid/cost-of-attendance/annual-coa-2526.html (sha256 783ed052ccc2)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition & Fees: 17428 ⟵ “Tuition & Fees | 17,428”
  - column:Books, Course Materials, Supplies, Equipment: 1330 ⟵ “Books, Course Materials, Supplies, Equipment | 1,330”
  - column:Housing: 11550 ⟵ “Housing | 11,550”
  - column:Food: 5474 ⟵ “Food | 5,474”
  - column:Personal Spending: 2993 ⟵ “Personal Spending | 2,993”
  - column:Transportation Expenses: 2345 ⟵ “Transportation Expenses | 2,345”
  - column:Federal Loan Fees: 44 ⟵ “Federal Loan Fees | 44”
  - column:TOTAL: 41164 ⟵ “TOTAL | 41,164”

## Re-verification of existing records (46)

- source_not_fetched: data/institutions/bergen/transfer_policies/2026-27.json ["transfer_policies", "ipeds-183743", null, "2026-27", {}]
- source_not_fetched: data/institutions/caldwell/credit_policies/2026-27.json ["credit_policies", "ipeds-183910", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/caldwell/transfer_policies/2026-27.json ["transfer_policies", "ipeds-183910", null, "2026-27", {}]
- source_not_fetched: data/institutions/ccm/credit_policies/2026-27.json ["credit_policies", "ipeds-184180", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/ccm/credit_policies/2026-27.json ["credit_policies", "ipeds-184180", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/drew/credit_policies/2026-27.json ["credit_policies", "ipeds-184348", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/georgian/awards/2026-27.json ["awards", "ipeds-184773", null, "2026-27", {"award_name": "Trustee Scholarship"}]
- source_not_fetched: data/institutions/georgian/awards/2026-27.json ["awards", "ipeds-184773", null, "2026-27", {"award_name": "Presidential Scholarship"}]
- source_not_fetched: data/institutions/georgian/awards/2026-27.json ["awards", "ipeds-184773", null, "2026-27", {"award_name": "Dean's Scholarship"}]
- source_not_fetched: data/institutions/georgian/awards/2026-27.json ["awards", "ipeds-184773", null, "2026-27", {"award_name": "McAuley Scholarship"}]
- source_not_fetched: data/institutions/georgian/awards/2026-27.json ["awards", "ipeds-184773", null, "2026-27", {"award_name": "GCU Award"}]
- source_not_fetched: data/institutions/georgian/awards/2026-27.json ["awards", "ipeds-184773", null, "2026-27", {"award_name": "Honors Scholarship"}]
- source_not_fetched: data/institutions/georgian/degree_requirements/2026-27.json ["degree_requirements", "ipeds-184773", null, "2026-27", {"program_key": "biology-b-s-including-medical-lab-sci", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/georgian/degree_requirements/2026-27.json ["degree_requirements", "ipeds-184773", null, "2026-27", {"program_key": "computer-science-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/mccc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-185509", null, "2026-27", {}]
- source_not_fetched: data/institutions/middlesexcollege/costs/2026-27.json ["costs", "ipeds-185536", null, "2026-27", {"residency": "out_of_state"}]
- source_not_fetched: data/institutions/middlesexcollege/credit_policies/2026-27.json ["credit_policies", "ipeds-185536", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/monmouth/transfer_policies/2026-27.json ["transfer_policies", "ipeds-185572", null, "2026-27", {}]
- nothing_to_check: data/institutions/montclair/transfer_policies/2026-27.json ["transfer_policies", "ipeds-185590", null, "2026-27", {}]
- source_not_fetched: data/institutions/njit/degree_requirements/2026-27.json ["degree_requirements", "ipeds-185828", null, "2026-27", {"program_key": "bachelor-of-architecture", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/njit/degree_requirements/2026-27.json ["degree_requirements", "ipeds-185828", null, "2026-27", {"program_key": "b-a-in-computer-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/njit/degree_requirements/2026-27.json ["degree_requirements", "ipeds-185828", null, "2026-27", {"program_key": "b-s-general-engineering", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/njit/degree_requirements/2026-27.json ["degree_requirements", "ipeds-185828", null, "2026-27", {"program_key": "b-a-in-information-systems", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/ocean/credit_policies/2026-27.json ["credit_policies", "ipeds-185873", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ramapo/credit_policies/2026-27.json ["credit_policies", "ipeds-186201", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ramapo/transfer_policies/2026-27.json ["transfer_policies", "ipeds-186201", null, "2026-27", {}]
- source_not_fetched: data/institutions/raritanval/credit_policies/2026-27.json ["credit_policies", "ipeds-186645", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/rcbc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-183877", null, "2026-27", {}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Presidential"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Academic Excellence"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Dean\u2019s"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Ignatian"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Pavonia"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Arrupe"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Loyola"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Petrean"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Pavo"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Legacy (Parent or grandparent is an alum of Saint Peter\u2019s University"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Phi Theta Kappa Member"}]
- source_not_fetched: data/institutions/saintpeters/awards/2026-27.json ["awards", "ipeds-186432", null, "2026-27", {"award_name": "Hudson County Community College Alumni Grant"}]
- source_not_fetched: data/institutions/saintpeters/transfer_policies/2026-27.json ["transfer_policies", "ipeds-186432", null, "2026-27", {}]
- source_not_fetched: data/institutions/stevens/credit_policies/2026-27.json ["credit_policies", "ipeds-186867", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/stevens/transfer_policies/2026-27.json ["transfer_policies", "ipeds-186867", null, "2026-27", {}]
- source_not_fetched: data/institutions/ucc/credit_policies/2026-27.json ["credit_policies", "ipeds-187198", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ucc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-187198", null, "2026-27", {}]
- source_not_fetched: data/institutions/wpunj/credit_policies/2026-27.json ["credit_policies", "ipeds-187444", null, "2026-27", {"policy_kind": "AP"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Montclair State University: tuition_fees, cost_of_attendance, merit_scholarships, clep_credit, dual_enrollment, residency
- Rowan University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
