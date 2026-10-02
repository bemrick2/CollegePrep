# Review queue — OR (2026-27)

Pages fetched: 1528; failures: 70. Candidates: 266 (64 without issues, 202 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 4 | 15 | 18 | 1 | 3 |
| cost_of_attendance | 0 | 0 | 2 | 10 | 24 | 2 | 3 |
| admissions_tests | 0 | 0 | 0 | 1 | 32 | 5 | 3 |
| common_data_set | 0 | 0 | 0 | 1 | 1 | 36 | 3 |
| merit_scholarships | 0 | 0 | 3 | 1 | 32 | 2 | 3 |
| ap_credit | 0 | 0 | 4 | 1 | 14 | 19 | 3 |
| clep_credit | 0 | 0 | 2 | 3 | 8 | 25 | 3 |
| ib_credit | 0 | 0 | 3 | 2 | 4 | 29 | 3 |
| dual_enrollment | 0 | 0 | 1 | 2 | 18 | 17 | 3 |
| transfer_credit | 0 | 0 | 5 | 2 | 30 | 1 | 3 |
| statewide_articulation | 0 | 0 | 0 | 0 | 12 | 26 | 3 |
| residency | 0 | 0 | 0 | 0 | 19 | 19 | 3 |
| degree_requirements | 0 | 0 | 2 | 1 | 18 | 17 | 3 |
| aid_appeals | 0 | 0 | 0 | 22 | 6 | 10 | 3 |

## Ready for review (64)

### `66435bb5354d6ee3` Blue Mountain Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/tuition-fees/ (sha256 782a1028f8b5)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition & Required Fees: 9936 ⟵ “Tuition & Required Fees | $7,211 | $7,211 | $9,936”
  - column:Books & Supplies: 1105 ⟵ “Books & Supplies | $1,105 | $1,105 | $1,105”
  - column:Living Expenses: 10800 ⟵ “Living Expenses | $6,450 | $10,800 | $10,800”
  - column:Misc./Personal Expenses: 1200 ⟵ “Misc./Personal Expenses | $1,200 | $1,200 | $1,200”
  - column:Transportation: 1974 ⟵ “Transportation | $1,974 | $1,974 | $1,974”
  - column:TOTAL: 25015 ⟵ “TOTAL | $17,940 | $22,290 | $25,015”
### `0787c596375bacd5` Bushnell University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://bushnell.edu/wp-content/uploads/2026/06/Bushnell-University-AP-Transfer-Guide.pdf (sha256 7959fa09e4e4)
- checks: {"distinct_exams": 38, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3+]:  ⟵ “2-D Art & Design                                         3+       DMG 200                                                     3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design                                         3+       DMG 200                                                     3”
  - equivalencies[AP-ART-HISTORY|3+]:  ⟵ “Art History                                              3+       Pick 2 of History, Social Science, or Diversity Gen Ed      6”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Drawing                                                  3+       General Elective                                            3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                                              3       MUS 100                                                     2”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition*                           3       WR 121                                                      3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition*                        3+       WR 121 & ENG 201                                            6”
  - equivalencies[AP-RESEARCH|3+]:  ⟵ “Research                                                 3+       General Elective                                            3”
  - equivalencies[AP-SEMINAR|3+]:  ⟵ “Seminar                                                  3+       General Elective                                            3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3+]:  ⟵ “Computer Science A                                       3+       SFTE Elective                                               3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3+]:  ⟵ “Computer Science Principles                              3+       SFTE Elective                                               3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                               3       Math Gen Ed                                                 3”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                                               3       MATH 251                                                    4”
  - equivalencies[AP-PRECALCULUS|3+]:  ⟵ “Precalculus                                              3+       MATH 130                                                    3”
  - equivalencies[AP-STATISTICS|3+]:  ⟵ “Statistics                                               3+       MATH 315                                                    3”
  - equivalencies[AP-BIOLOGY|3+]:  ⟵ “Biology                                                  3+       BIOL 111 & 111L & 112 & 112L                                8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                                 3       CHEM 121 & 121L                                             5”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science                                    3+       General Elective                                            3”
  - equivalencies[AP-PHYSICS-1|3+]:  ⟵ “Physics 1                                                3+       PHYS 201 & 201L                                             5”
  - equivalencies[AP-PHYSICS-2|3+]:  ⟵ “Physics 2                                                3+       PHYS 202 & 202L                                             4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3+]:  ⟵ “Physics C: Mechanics                                     3+       PHYS 201 & 201L                                             5”
  - equivalencies[AP-MACROECONOMICS|3+]:  ⟵ “Macroeconomics                         3+   ECON 202                                                  3”
  - equivalencies[AP-MICROECONOMICS|3+]:  ⟵ “Microeconomics                         3+   ECON 201                                                  3”
  - equivalencies[AP-PSYCHOLOGY|3+]:  ⟵ “Psychology                             3+   PSY 200                                                   3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies               3    History Gen Ed                                            3”
  - … 13 more rows
### `m7609dc4b3306dc5` Bushnell University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://bushnell.edu/admissions/undergraduate-admissions/transfer-students/accepted-credit/ (sha256 1486072bcfe3)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “Transferrable courses must be at the 100-level or above, taken at a regionally accredited college (up to 30 transfer credits from a non-regionally accredited college will be accepted), and with a grade of C- or higher.”
  - min_grade: C- ⟵ “College and University Credit Transferrable courses must be at the 100-level or above, taken at a regionally accredited college (up to 30 transfer credits from a non-regionally accredited college may be accepted), and completed with a grade of C- or higher.”
### `585d3a34bf0e3841` Central Oregon Community College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://cocc.edu/departments/admissions/grades-and-student-records/credit-for-prior-learning (sha256 8e387707422b)
- checks: {"distinct_exams": 19, "equivalencies": 72, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|4]:  ⟵ “Art History - Standard Level | 4 | 4 credits, Art Elective”
  - equivalencies[IB-HISTORY|5+]:  ⟵ “Art History - Standard Level | 5+ | 4 credits, Art Elective”
  - equivalencies[IB-HISTORY|4]:  ⟵ “Art History - High Level | 4 | NA”
  - equivalencies[IB-HISTORY|5+]:  ⟵ “Art History - High Level | 5+ | NA”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology - Standard Level | 4 | BI 101”
  - equivalencies[IB-BIOLOGY|5+]:  ⟵ “Biology - Standard Level | 5+ | BI 221Z”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology - High Level | 4 | BI 101, 102, 103”
  - equivalencies[IB-BIOLOGY|5+]:  ⟵ “Biology - High Level | 5+ | BI 221Z, BI 222Z, & BI 223Z”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business Management - Standard Level | 4 | 4 credits, BA Elective”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5+]:  ⟵ “Business Management - Standard Level | 5+ | BA 101Z”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business Management - High Level | 4 | BA 101Z”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry - Standard Level | 4 | CH 221Z”
  - equivalencies[IB-CHEMISTRY|5+]:  ⟵ “Chemistry - Standard Level | 5+ | CH 221Z”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry - High Level | 4 | CH 221Z, 222Z, & 223Z”
  - equivalencies[IB-CHEMISTRY|5+]:  ⟵ “Chemistry - High Level | 5+ | CH 221Z, 222Z, & 223Z”
  - equivalencies[IB-COMPUTER-SCIENCE|4]:  ⟵ “Computer Science - Standard Level | 4 | CS 160”
  - equivalencies[IB-COMPUTER-SCIENCE|5+]:  ⟵ “Computer Science - Standard Level | 5+ | CS 160”
  - equivalencies[IB-COMPUTER-SCIENCE|4]:  ⟵ “Computer Science - High Level | 4 | CS 160 & 4 credits, CS Elective”
  - equivalencies[IB-COMPUTER-SCIENCE|5+]:  ⟵ “Computer Science - High Level | 5+ | CS 160 & CIS 161”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics - Standard Level | 4 | 3 credits, ECON Elective”
  - equivalencies[IB-ECONOMICS|5+]:  ⟵ “Economics - Standard Level | 5+ | EC 201Z”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics - High Level | 4 | 6 credits, ECON Elective”
  - equivalencies[IB-ECONOMICS|5+]:  ⟵ “Economics - High Level | 5+ | EC 201Z, & 202Z”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4]:  ⟵ “Environmental Systems and Societies - Standard Level | 4 | SOC 228”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|5+]:  ⟵ “Environmental Systems and Societies - Standard Level | 5+ | SOC 228”
  - … 47 more rows
### `f20fbe6910fdea2d` Central Oregon Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://cocc.edu/departments/admissions/grades-and-student-records/credit-for-prior-learning (sha256 8e387707422b)
- checks: {"distinct_exams": 35, "equivalencies": 61, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3+]:  ⟵ “AP African American Studies | 3+ | ES 212”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “AP Art History | 3 | ARH 201”
  - equivalencies[AP-ART-HISTORY|4+]:  ⟵ “AP Art History | 4+ | ARH 201, 202”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “AP Biology | 3 | BI 101, 4 credits BI DS Science Lab”
  - equivalencies[AP-BIOLOGY|4+]:  ⟵ “AP Biology | 4+ | BI 101, 102, 103”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “AP Calculus AB | 3 | MTH 251Z”
  - equivalencies[AP-CALCULUS-AB|4+]:  ⟵ “AP Calculus AB | 4+ | MTH 251Z, 252Z”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “AP Calculus BC | 3 | MTH 251Z, 252Z”
  - equivalencies[AP-CALCULUS-BC|4+]:  ⟵ “AP Calculus BC | 4+ | MTH 251Z, 252Z, 253Z”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “AP Chemistry | 3 | CH 104Z, 124Z”
  - equivalencies[AP-CHEMISTRY|4+]:  ⟵ “AP Chemistry | 4+ | CH 221Z, 222Z, 223Z, CH227Z, CH228Z, CH229Z”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “AP Chinese Language and Culture | 3 | CHN 101, 102, 103”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “AP Chinese Language and Culture | 4 | CHN 103, 201, 202”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “AP Chinese Language and Culture | 5 | CHN 201, 202, 203”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3+]:  ⟵ “AP Comparative Government | 3+ | PS 204”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “AP Drawing | 3+ | ART 131”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “AP Environmental Science | 3+ | 4 credits, DS science lab”
  - equivalencies[AP-EUROPEAN-HISTORY|3+]:  ⟵ “AP European History | 3+ | HST 101, 102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “AP French Language | 3 | FR 101, 102, 103”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “AP French Language | 4 | FR 103, 201, 202”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “AP French Language | 5 | FR 201, 202, 203”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “AP German Language | 3 | GER 101, 102, 103”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “AP German Language | 4 | GER 103, 201, 202”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “AP German Language | 5 | GER 201, 202, 203”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3+]:  ⟵ “AP Human Geography | 3+ | GEOG 107”
  - … 36 more rows
### `3b1f280bf2ac51f7` Clackamas Community College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- checks: {"thresholds": null}
  - award_amount_text: $192.00 ⟵ “Transportation | $575.00 | $192.00”
### `c6a265c312b7465d` Clackamas Community College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- checks: {"thresholds": null}
  - award_amount_text: $200.00 ⟵ “Books/Supplies | $600.00 | $200.00”
### `e26fdfa2c26a4d01` Clackamas Community College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- checks: {"thresholds": null}
  - award_amount_text: $150.00 ⟵ “Personal expenses (entertainment, clothes, etc.) | $450.00 | $150.00”
### `6aca751e6f5687a1` George Fox University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.georgefox.edu/college-admissions/scholarships/index.html (sha256 a5cfbc3144c9)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition (12 to 18 credits): 45154 ⟵ “Tuition (12 to 18 credits) | $45,154”
  - column:Housing and Meals: 15080 ⟵ “Housing and Meals | $15,080”
  - column:Standard Fees: 720 ⟵ “Standard Fees | $720”
  - column:Total Tuition and Costs: 60954 ⟵ “Total Tuition and Costs | $60,954”
### `0965a34d739c4fb3` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 2 credits ⟵ “2 credits | 2 credits”
### `141bcd921120c743` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 9 credits ⟵ “13 credits | 9 credits”
### `1973ec7cfe4ad34f` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 7 credits ⟵ “10 credits | 7 credits”
### `65350132b22db686` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 3 credits ⟵ “4 credits | 3 credits”
### `7072ff732935a9bb` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 13 credits ⟵ “19 credits | 13 credits”
### `74717ef54f81d700` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 8 credits ⟵ “12 credits | 8 credits”
### `7f3d3bcee4a5f631` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 2 credits ⟵ “3 credits | 2 credits”
### `865f9af25563df4a` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 11 credits ⟵ “16 credits | 11 credits”
### `ae00a78e98920b50` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 4 credits ⟵ “5 credits | 4 credits”
### `b28bfb159299a788` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 8 credits ⟵ “11 credits | 8 credits”
### `b4a3a4fb9e29c0e6` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 12 credits ⟵ “17 credits | 12 credits”
### `b8eafc6af618fc6c` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 5 credits ⟵ “7 credits | 5 credits”
### `bc29496c453c52ee` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 1 credit ⟵ “1 credit | 1 credit”
### `c0bb6b706a8c2e8c` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 10 credits ⟵ “15 credits | 10 credits”
### `c50871f75a989055` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 6 credits ⟵ “8 credits | 6 credits”
### `cced199f9ec1d974` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 4 credits ⟵ “6 credits | 4 credits”
### `d5fa3643f1ccd0e5` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 14 credits ⟵ “20 credits | 14 credits”
### `dffedc557809be52` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 10 credits ⟵ “14 credits | 10 credits”
### `ec15ee125e1ef64c` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 12 credits ⟵ “18 credits | 12 credits”
### `f2558d85126724b8` Klamath Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- checks: {"thresholds": null}
  - gpa_requirement: 6 credits ⟵ “9 credits | 6 credits”
### `f7a617886a20b7e8` Lewis & Clark College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.lclark.edu/offices/account_services/student_statements/costs/college/ (sha256 187ff9539fd9)
- checks: {"columns": 1, "rows": 13}
  - column:Tuition*: 70658 ⟵ “Tuition* | $35,329 | $70,658”
  - column:Student Body Fee*: 360 ⟵ “Student Body Fee* | $180 | $360”
  - column:Health Insurance: 5655 ⟵ “Health Insurance | $2827.50 | $5,655”
  - column:Room (on campus): 9578 ⟵ “Room (on campus) | $4,789 | $9,578”
  - column:Single Room Premium: 10930 ⟵ “Single Room Premium | $5,465 | $10,930”
  - column:Apartment Premium: 12310 ⟵ “Apartment Premium | $6,155 | $12,310”
  - column:Board (14 Meals plus $200 Flex): 7314 ⟵ “Board (14 Meals plus $200 Flex) | $3,657 | $7,314”
  - column:Board (100 Block plus $250 Flex)*****: 4976 ⟵ “Board (100 Block plus $250 Flex)***** | $2,488 | $4,976”
  - column:Flex Only******: 1708 ⟵ “Flex Only****** | $854 | $1,708”
  - column:Health and Wellness Fee: 74 ⟵ “Health and Wellness Fee | $37 | $74”
  - column:New Student Orientation Fee (Fall incoming first-year & transfer students only): 215 ⟵ “New Student Orientation Fee (Fall incoming first-year & transfer students only) |  | $215”
  - column:Green Power Fee: 20 ⟵ “Green Power Fee | $20 (Fall only) | $20”
  - column:Media Fee: 70 ⟵ “Media Fee | $35 | $70”
### `a17767e3fd493258` Linn-Benton Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.linnbenton.edu/future-students/explore-lb/transfer-center/osu.php (sha256 521849cbccde)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “If it turns out that you are not yet eligible, it's easy to get started at LBCC and then apply to DPP after completing: 24 graded transferable credits WR 121Z with a grade of C or higher MTH 105Z or MTH 111Z with a grade of C or better Earning a minimum GPA of 2.25 Apply Now This application will require the regular OSU application fee (currently $65).”
  - min_grade: C ⟵ “If it turns out that you are not yet eligible, it's easy to get started at LBCC and then apply to DPP after completing: 24 graded transferable credits WR 121Z with a grade of C or higher MTH 105Z or MTH 111Z with a grade of C or better Earning a minimum GPA of 2.25 Apply Now This application will require the regular OSU application fee (currently $65).”
  - min_grade: C ⟵ “For transfer students, OSU is looking at the following criteria: Completed 24 transferable, college-level credits Completed WR 121Z with a grade of C or better Completed MTH 105Z or MTH 111Z with a grade of C or better* Earn a GPA of 2.25 or higher *While completion of college-level math is strongly recommended, transfer students may be admitted to OSU without math if they have met all other requi”
### `f176cfad3a94cb1d` Oregon Coast Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://oregoncoast.edu/cpl/ (sha256 4f160ecefa3f)
- checks: {"distinct_exams": 15, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | PS 201 | 4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introduction to Sociology | 50 | SOC 204, 205 | 8”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|60]:  ⟵ “Principles of Macroeconomics | 60 | EC 202 | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|60]:  ⟵ “Principles of Microeconomics | 60 | EC 201 | 4”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | HST 101 | 4”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | HST 103 | 4”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50 x 2]:  ⟵ “Western Civilization I and II | 50 x 2 | HST 101, 102, 103 | 12”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 2xx | 8”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 2xx | 8”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | WR 121z | 4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MTH 251 | 4”
  - equivalencies[CLEP-CALCULUS|64]:  ⟵ “Calculus | 64 | MTH 251, 252 | 8”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MTH 105z | 4”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MTH 111z | 4”
  - equivalencies[CLEP-PRECALCULUS|61]:  ⟵ “Precalculus | 61 | MTH 111z, 112z | 8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language: Levels 1 & 2 | 50 | FR 1xx | 12”
  - equivalencies[CLEP-FRENCH-LANGUAGE|60]:  ⟵ “French Language: Levels 1 & 2 | 60 | FR 2xx | 12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language: Levels 1 & 2 | 50 | GER 1xx | 12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language: Levels 1 & 2 | 60 | GER 2xx | 12”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language: Levels 1 & 2 | 50 | SPA 1xx | 12”
  - equivalencies[CLEP-SPANISH-LANGUAGE|60]:  ⟵ “Spanish Language: Levels 1 & 2 | 60 | SPA 2xx | 12”
### `ef798fcc8b74a783` Oregon State University-Cascades Campus — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://osucascades.edu/admissions/apply-now/transfer-students/transfer-degrees (sha256 aa07494afbae)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “For transfer students graduating from high school in 1997 and thereafter, OSU has a second language admission requirement: two terms of a college-level second language with an average grade of C- or above, OR two years of the same high school level second language with an average grade of C- or above OR satisfactory performance on an approved second language assessment of proficiency.”
  - min_grade: C- ⟵ “For transfer students graduating from high school in 1997 and thereafter, OSU has a second language admission requirement: two terms of a college-level second language with an average grade of C- or above, OR two years of the same high school level second language with an average grade of C- or above OR satisfactory performance on an approved second language assessment of proficiency.”
### `f6cb693ac09610bb` Portland Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.pcc.edu/beaverton-early-college/ (sha256 0698392465e3)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “Yes, if you have at least a 2.0 cumulative grade point average.”
### `3a6497aacede4047` Portland State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.pdx.edu/admissions/college-level-exam-program (sha256 2dfa1ebd8999)
- checks: {"distinct_exams": 22, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 9 Arts and Letters (AL) elective credits | 50 | Closed to students with more than 90 credits”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French | 12 | 50 | Awards FR 101, 102, 103”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French | 12 | 59 | Awards FR 201, 202, 203”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German | 12 | 50 | Awards GER 101, 102, 103”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German | 12 | 60 | Awards GER 201, 202, 203”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language | 12 | 50 | Awards SPAN 101, 102, 103”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language | 12 | 63 | Awards SPAN 201, 202, 203”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing | 12 | 50 | Awards SPAN 101, 102, 103”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|65]:  ⟵ “Spanish with Writing | 12 | 65 | Awards SPAN 201, 202, 203”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 2; Maximum 4 total from any combination of CLP History exam | 50 | Awards History lower division elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II | 2; Maximum 4 total from any combination of CLP History exam | 50 | Awards History lower division elective”
  - equivalencies[CLEP-BIOLOGY|49]:  ⟵ “Biology | 0 | 49 | Waives BI 221Z, 222Z, 223Z”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 8 | 50 | Awards MTH 251Z, 252Z”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 4 | 50 | Awards MTH 111Z”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | 4 | 50 | Awards MTH 112Z”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 4 | 50 | Awards Math lower division credit (starting 7/2001)”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 8 | 50 | Awards PS 101, 102”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 8 | 50 | Awards PSY 201Z, 202Z”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Introductory Microeconomics | 4 | 50 | Awards EC 201Z”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Introductory Macroeconomics | 4 | 50 | Awards EC 202Z”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology | 0 | 50 | Waives prerequisite for upper division courses”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 4 | 50 | Awards BA 211Z”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 4 | 50 | Awards Business lower division elective credit”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 4 | 50 | Awards Business lower division elective credit”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 4 | 50 | Awards Business lower division elective credit”
  - … 1 more rows
### `4adcf32233fe0a55` Portland State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.pdx.edu/admissions/advanced-placement (sha256 28417114ae4d)
- checks: {"distinct_exams": 37, "equivalencies": 115, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3+]:  ⟵ “2-D Art & Design | 3+ | 4 | ART LD”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art & Design | 3+ | 4 | ART LD”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 4 | ARH 206”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | 8 | ARH 205, 206”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “Art History | 5 | 12 | ARH 204, 205, 206”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Drawing | 3+ | 4 | ART 131”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 4 | MUS 1022”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | 8 | MUS 102, 111, 1142”
  - equivalencies[AP-MUSIC-THEORY|5]:  ⟵ “Music Theory | 5 | 12 | MUS 102, 111, 112, 114, 1152”
  - equivalencies[AP-RESEARCH|3+]:  ⟵ “Research | 3+ | 2 | GEN LD”
  - equivalencies[AP-SEMINAR|3+]:  ⟵ “Seminar | 3+ | 2 | GEN LD”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language & Composition | 3+ | 4 | WR 121Z”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition | 3+ | 4 | ENG 100”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3+]:  ⟵ “African American Studies | 3+ | 4 | BST 202”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics | 3 | 4 | PS LD”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|4+]:  ⟵ “Comparative Government & Politics | 4+ | 4 | PS 204”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3+]:  ⟵ “Human Geography | 3+ | 4 | GEOG 230”
  - equivalencies[AP-MACROECONOMICS|3+]:  ⟵ “Macroeconomics | 3+ | 4 | EC 202Z”
  - equivalencies[AP-MICROECONOMICS|3+]:  ⟵ “Microeconomics | 3+ | 4 | EC 201Z”
  - equivalencies[AP-PSYCHOLOGY|3+]:  ⟵ “Psychology | 3+ | 4 | PSY LD”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government & Politics | 3 | 4 | PS LD”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4+]:  ⟵ “United States Government & Politics | 4+ | 4 | PS 101”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | MTH 251Z”
  - equivalencies[AP-CALCULUS-AB|4+]:  ⟵ “Calculus AB | 4+ | 8 | MTH 251Z, 252Z”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 8 | MTH 251Z, 252Z”
  - … 90 more rows
### `f605a7f1f9105c77` Portland State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.pdx.edu/admissions/international-baccalaureate (sha256 531053a5f04e)
- checks: {"distinct_exams": 25, "equivalencies": 62, "rows_without_score": 0}
  - equivalencies[IB-FILM|4,5,6,7]:  ⟵ “Film | 4,5,6,7 | 4 | FILM LD | 8 | FILM LD”
  - equivalencies[IB-MUSIC|4,5,6,7]:  ⟵ “Music | 4,5,6,7 | 4 | MUS LD | 8 | MUS LD”
  - equivalencies[IB-THEATRE|4,5,6,7]:  ⟵ “Theatre | 4,5,6,7 | 4 | TA LD | 4 | TA LD”
  - equivalencies[IB-VISUAL-ARTS|4,5,6,7]:  ⟵ “Visual Arts | 4,5,6,7 | 4 | ART LD | 4 | ART 131, LD”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4,5,6,7]:  ⟵ “Business and Management | 4,5,6,7 | 4 | BA LD | 4 | BA 101Z”
  - equivalencies[IB-ECONOMICS|4,5,6,7]:  ⟵ “Economics | 4,5,6,7 | 4 | EC 200 | 8 | EC 201Z, 202Z”
  - equivalencies[IB-GEOGRAPHY|4,5,6,7]:  ⟵ “Geography | 4,5,6,7 | 4 | GEOG LD | 8 | GEOG 230, LD”
  - equivalencies[IB-GLOBAL-POLITICS|4]:  ⟵ “Global Politics | 4 | 4 | PS LD | 4 | PS LD”
  - equivalencies[IB-GLOBAL-POLITICS|5,6,7]:  ⟵ “Global Politics | 5,6,7 | 4 | PS LD | 7 | PS 205, LD”
  - equivalencies[IB-HISTORY-SL|4,5,6,7]:  ⟵ “History SL | 4,5,6,7 | 4 | HST LD | --- | ---”
  - equivalencies[IB-HISTORY-HL|4,5,6,7]:  ⟵ “History: Africa & Middle East HL | 4,5,6,7 | --- | --- | 12 | HST LD”
  - equivalencies[IB-PHILOSOPHY|4,5,6,7]:  ⟵ “Philosophy | 4,5,6,7 | 4 | PHL LD | 8 | PHL 201, LD”
  - equivalencies[IB-PSYCHOLOGY|4,5,6,7]:  ⟵ “Psychology | 4,5,6,7 | 4 | PSY LD | 8 | PSY 201Z, 202Z”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4,5,6,7]:  ⟵ “Social and Cultural Anthropology | 4,5,6,7 | 4 | ANTH LD | 4 | ANTH LD”
  - equivalencies[IB-LATIN|4,5,6,7]:  ⟵ “Classical Languages: Latin | 4,5,6,7 | 4 | LAT 103 | 16 | LAT 101, 102, 103, 201”
  - equivalencies[IB-LATIN|Language AB Initio- Any language]:  ⟵ “Classical Languages: Latin | Language AB Initio- Any language | No Second Language credits are awarded for Ab initio IB Language exams”
  - equivalencies[IB-FRENCH|4,5]:  ⟵ “French B | 4,5 | 4 | FR 203 | 12 | 4 FR UD*, 8 FR LD”
  - equivalencies[IB-FRENCH|6,7]:  ⟵ “French B | 6,7 | 4 | FR UD* | 12 | 8 FR UD*, 4 FR LD”
  - equivalencies[IB-GERMAN|4,5]:  ⟵ “German B | 4,5 | 4 | GER 203 | 12 | 4 GER UD*, 8 GER LD”
  - equivalencies[IB-GERMAN|6,7]:  ⟵ “German B | 6,7 | 4 | GER UD* | 12 | 8 GER UD*, 4 GER LD”
  - equivalencies[IB-SPANISH|4,5]:  ⟵ “Spanish B | 4,5 | 4 | SPAN 203 | 12 | 4 SPAN UD*, 8 SPAN LD”
  - equivalencies[IB-SPANISH|6,7]:  ⟵ “Spanish B | 6,7 | 4 | SPAN UD* | 12 | 8 SPAN UD*, 4 SPAN LD”
  - equivalencies[IB-FRENCH|4,5,6,7]:  ⟵ “Literature & Performance (Spanish or French) | 4,5,6,7 | 4 | SPAN UD or FR UD | --- | ---”
  - equivalencies[IB-COMPUTER-SCIENCE|4,5,6,7]:  ⟵ “Computer Science | 4,5,6,7 | 4 | CS 161 [CS LD prior to 202502] | 8 | CS 160, 161[CS LD prior to 202502]”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4,5,6,7]:  ⟵ “Mathematics: Analysis & Approaches | 4,5,6,7 | 4 | MTH 251Z | 12 | MTH 251Z, 252Z, LD”
  - … 37 more rows
### `me9dfa185421c190` Portland State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.pdx.edu/admissions/transfer (sha256 4b4fd02432e7)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “If you are transferring from a U.S. institution of higher education you must complete Writing 121 or its equivalent with a grade of C- or better.”
  - min_grade: C- ⟵ “Completion of 30 or more transferable college quarter credits (20 semester credits) Cumulative grade point average (GPA) of at least 2.25, or 2.00 if you present a transferable associate degree or an Oregon Transfer Module (OTM) Completion of WR121 or equivalent with a grade of C- or better.”
### `1e399703564b54db` Southwestern Oregon Community College — academic_programs 2026-27 · program_key=oregon-transfer-module-otm [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
- checks: {"courses": 205, "groups": 8, "groups_skipped": 0}
  - program_name: Oregon Transfer Module (OTM) ⟵ “Oregon Transfer Module (OTM) < Southwestern Oregon Community College”
### `411aa18a3b2f2da2` Southwestern Oregon Community College — academic_programs 2026-27 · program_key=biology-associate-of-science-transfer [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/biology-AST/ (sha256 d8dabd16933f)
- checks: {"courses": 27, "groups": 1, "groups_skipped": 0}
  - program_name: Biology, Associate of Science Transfer ⟵ “Biology, Associate of Science Transfer < Southwestern Oregon Community College”
### `446a4651d875096f` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=biology-associate-of-science-transfer · requirement_key=aaot-cultural-literacy-courses [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/biology-AST/ (sha256 d8dabd16933f)
  - courses: ANTH 201 ⟵ “ANTH 201 - Physical Anthropology and Evolution”
  - courses: ANTH 202 ⟵ “ANTH 202 - Introduction to Archaeology”
  - courses: ANTH 203 ⟵ “ANTH 203 - Language and Culture”
  - courses: ANTH 221 ⟵ “ANTH 221 - Intro to Cultural Anthropology”
  - courses: ANTH 222 ⟵ “ANTH 222 - Cultural Anthropology II”
  - courses: ANTH 223 ⟵ “ANTH 223 - Cultural Anthropology III”
  - courses: ANTH 224 ⟵ “ANTH 224 - Intro to Medical Anthropology”
  - courses: ANTH 230 ⟵ “ANTH 230 - Native North Americans: Oregon”
  - courses: ANTH 231 ⟵ “ANTH 231 - Native North Americans: PNW”
  - courses: ANTH 232 ⟵ “ANTH 232 - Native North Americans”
  - courses: COMM 220 ⟵ “COMM 220 - Gender And Communication”
  - courses: ENG 107 ⟵ “ENG 107 - World Literature”
  - courses: ENG 108 ⟵ “ENG 108 - World Literature”
  - courses: ENG 109 ⟵ “ENG 109 - World Literature”
  - courses: GEOG 105 ⟵ “GEOG 105 - Cultural Geography”
  - courses: HUM 204 ⟵ “HUM 204 - World Mythology & Religion”
  - courses: HUM 205 ⟵ “HUM 205 - World Mythology & Religion”
  - courses: HUM 206 ⟵ “HUM 206 - World Mythology & Religion”
  - courses: HST 104 ⟵ “HST 104 - History of the Middle East”
  - courses: PSY 216 ⟵ “PSY 216 - Social Psychology”
  - courses: PSY 231 ⟵ “PSY 231 - Human Sexuality”
  - courses: MUS 205 ⟵ “MUS 205 - Intro to Jazz History”
  - courses: MUS 206 ⟵ “MUS 206 - Intro to History of Rock and Roll”
  - courses: SOC 208 ⟵ “SOC 208 - Sociology of Sport”
  - courses: SOC 210 ⟵ “SOC 210 - Marriage and Family”
  - … 2 more rows
### `45b4cecca2583942` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=oregon-transfer-module-otm · requirement_key=supportive-courses [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
  - courses: CIS 120 ⟵ “CIS 120 - Concepts of Computing”
  - courses: CIS 125W ⟵ “CIS 125W - Word Processing Applications Microsoft”
  - courses: HD 100 ⟵ “HD 100 - College Survival Skills & Success Habits”
  - courses: HD 102 ⟵ “HD 102 - College Nuts and Bolts”
  - courses: HD 111 ⟵ “HD 111 - Math Success”
  - courses: HD 112 ⟵ “HD 112 - Study Skills”
  - courses: HD 113 ⟵ “HD 113 - Stop Test Anxiety Now”
  - courses: HD 152 ⟵ “HD 152 - Stress Management”
  - courses: HD 208 ⟵ “HD 208 - Career/Life Plan”
### `75c0f8dbbcf8c041` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=oregon-transfer-module-otm · requirement_key=social-sciences [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
  - courses: ANTH 201 ⟵ “ANTH 201 - Physical Anthropology and Evolution”
  - courses: ANTH 202 ⟵ “ANTH 202 - Introduction to Archaeology”
  - courses: ANTH 203 ⟵ “ANTH 203 - Language and Culture”
  - courses: ANTH 221 ⟵ “ANTH 221 - Intro to Cultural Anthropology”
  - courses: ANTH 222 ⟵ “ANTH 222 - Cultural Anthropology II”
  - courses: ANTH 223 ⟵ “ANTH 223 - Cultural Anthropology III”
  - courses: ANTH 224 ⟵ “ANTH 224 - Intro to Medical Anthropology”
  - courses: ANTH 230 ⟵ “ANTH 230 - Native North Americans: Oregon”
  - courses: ANTH 231 ⟵ “ANTH 231 - Native North Americans: PNW”
  - courses: ANTH 232 ⟵ “ANTH 232 - Native North Americans”
  - courses: CJ 101 ⟵ “CJ 101 - Intro to Criminology”
  - courses: ECON 201Z ⟵ “ECON 201Z - Principles of Microeconomics”
  - courses: ECON 202Z ⟵ “ECON 202Z - Principles of Macroeconomics”
  - courses: ED 169 ⟵ “ED 169 - Overview of Student Special Needs”
  - courses: ED 258 ⟵ “ED 258 - Multicultural Education”
  - courses: GEOG 105 ⟵ “GEOG 105 - Cultural Geography”
  - courses: HST 101 ⟵ “HST 101 - History of Western Civilization”
  - courses: HST 102 ⟵ “HST 102 - History of Western Civilization”
  - courses: HST 103 ⟵ “HST 103 - History of Western Civilization”
  - courses: HST 104 ⟵ “HST 104 - History of the Middle East”
  - courses: HST 195 ⟵ “HST 195 - History of the Vietnam War”
  - courses: HST 201Z ⟵ “HST 201Z - United States History I”
  - courses: HST 202Z ⟵ “HST 202Z - United States History II”
  - courses: HST 203Z ⟵ “HST 203Z - United States History Ill”
  - courses: HST 240 ⟵ “HST 240 - History of Oregon and the South Coast”
  - … 15 more rows
### `7e72ff4d5813523e` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=oregon-transfer-module-otm · requirement_key=communication [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
  - courses: COMM 100Z ⟵ “COMM 100Z - Introduction to Communication”
  - courses: COMM 111Z ⟵ “COMM 111Z - Public Speaking”
  - courses: COMM 218Z ⟵ “COMM 218Z - Interpersonal Communication”
  - courses: COMM 219 ⟵ “COMM 219 - Small Group Discussion”
### `a559f675179e4e9a` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=oregon-transfer-module-otm · requirement_key=laboratory-courses [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
  - courses: BI 101 ⟵ “BI 101 - General Biology”
  - courses: BI 102 ⟵ “BI 102 - General Biology”
  - courses: BI 103 ⟵ “BI 103 - General Biology”
  - courses: BI 112 ⟵ “BI 112 - Cell Biology for Health Occupations”
  - courses: BI 142 ⟵ “BI 142 - Habitats: Marine Biology”
  - courses: BI 221Z ⟵ “BI 221Z - Principles of Biology: Cells”
  - courses: BI 222Z ⟵ “BI 222Z - Principles of Biology: Organisms”
  - courses: BI 223Z ⟵ “BI 223Z - Principles of Biology: Ecology And Evolution”
  - courses: BI 231Z ⟵ “BI 231Z - Human Anatomy & Physiology I”
  - courses: BI 232Z ⟵ “BI 232Z - Human Anatomy & Physiology II”
  - courses: BI 233Z ⟵ “BI 233Z - Human Anatomy & Physiology III”
  - courses: BI 234 ⟵ “BI 234 - Microbiology”
  - courses: CHEM 112Z ⟵ “CHEM 112Z - Chemistry For Health Professions”
  - courses: ENV 235 ⟵ “ENV 235 - Introduction to Soil Science”
  - courses: GS 104 ⟵ “GS 104 - Physical Science”
  - courses: GS 106 ⟵ “GS 106 - Introduction to Earth Science”
  - courses: GS 107 ⟵ “GS 107 - Astronomy”
  - courses: GS 108 ⟵ “GS 108 - Oceanography”
  - courses: NR 260 ⟵ “NR 260 - Watershed Processes”
  - courses: PH 201 ⟵ “PH 201 - General Physics I: Mechanics”
  - courses: PH 202 ⟵ “PH 202 - General Physics II: Heat, Waves, Relativity”
  - courses: PH 203 ⟵ “PH 203 - Gen Physics III: Elect & Magnetism”
  - courses: PH 211 ⟵ “PH 211 - General Physics with Calculus I”
  - courses: PH 212 ⟵ “PH 212 - General Physics with Calculus II”
  - courses: PH 213 ⟵ “PH 213 - General Physics with Calculus III”
### `a83a6de10f73b70c` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=oregon-transfer-module-otm · requirement_key=non-laboratory-courses [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
  - courses: BI 140 ⟵ “BI 140 - Practical Ecology”
  - courses: BI 149 ⟵ “BI 149 - Introduction to Human Genetics”
  - courses: CS 160 ⟵ “CS 160 - Introduction To Computer Science”
  - courses: CS 161 ⟵ “CS 161 - Computer Science I”
  - courses: CS 162 ⟵ “CS 162 - Computer Science II”
  - courses: CS 260 ⟵ “CS 260 - Data Structures”
  - courses: ENV 110 ⟵ “ENV 110 - Introduction Environmental Science”
  - courses: MTH 105Z ⟵ “MTH 105Z - Math in Society (has corequisite of MTH105A)”
  - courses: MTH 111Z ⟵ “MTH 111Z - Precalculus I: Functions (has corequisite of MTH111A)”
  - courses: MTH 112Z ⟵ “MTH 112Z - Precalculus II: Trigonometry”
  - courses: MTH 212 ⟵ “MTH 212 - Fundamentals of Elementary Mathematics II”
  - courses: MTH 213 ⟵ “MTH 213 - Fundamentals of Elementary Mathematics III”
  - courses: MTH 231 ⟵ “MTH 231 - Elements of Discrete Mathematics I”
  - courses: MTH 232 ⟵ “MTH 232 - Elements of Discrete Mathematics II”
  - courses: MTH 241 ⟵ “MTH 241 - Calculus for Bus and Soc Science I”
  - courses: MTH 242 ⟵ “MTH 242 - Calculus for Bus and Soc Science II”
  - courses: MTH 244 ⟵ “MTH 244 - Probability & Statistics II”
  - courses: MTH 251Z ⟵ “MTH 251Z - Differential Calculus”
  - courses: MTH 252Z ⟵ “MTH 252Z - Integral Calculus”
  - courses: MTH 253Z ⟵ “MTH 253Z - Calculus: Sequences and Series”
  - courses: MTH 254 ⟵ “MTH 254 - Vector Calculus I”
  - courses: MTH 255 ⟵ “MTH 255 - Vector Calculus II”
  - courses: MTH 256 ⟵ “MTH 256 - Differential Equations”
  - courses: MTH 260 ⟵ “MTH 260 - Matrix Methods and Linear Algebra”
  - courses: MTH 264 ⟵ “MTH 264 - Introduction to Matrix Algebra and Power Series”
  - … 1 more rows
### `bdfd571cf5803195` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=oregon-transfer-module-otm · requirement_key=arts-and-letters [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
  - courses: ART 115 ⟵ “ART 115 - Basic Design I Intro to Elements of Art and Principles of Design”
  - courses: ART 116 ⟵ “ART 116 - Basic Design II, Color Theory”
  - courses: ART 117 ⟵ “ART 117 - Basic Design III, Intro to 3D Design”
  - courses: ART 131 ⟵ “ART 131 - Introduction to Drawing I”
  - courses: ART 132 ⟵ “ART 132 - Introduction to Drawing II”
  - courses: ART 133 ⟵ “ART 133 - Introduction to Drawing III”
  - courses: ART 191 ⟵ “ART 191 - Beginning Sculpture”
  - courses: ART 192 ⟵ “ART 192 - Beginning Sculpture”
  - courses: ART 204 ⟵ “ART 204 - History of Western Art: Introduction to Art History”
  - courses: ART 205 ⟵ “ART 205 - History of Western Art: Introduction to Art History”
  - courses: ART 206 ⟵ “ART 206 - History of Western Art: Introduction to Art History”
  - courses: ART 244 ⟵ “ART 244 - Bronze Casting”
  - courses: ART 253 ⟵ “ART 253 - Ceramics I”
  - courses: ART 256 ⟵ “ART 256 - Ceramics II”
  - courses: ART 281 ⟵ “ART 281 - Painting I Beginning”
  - courses: ART 282 ⟵ “ART 282 - Painting II Beginning”
  - courses: ART 283 ⟵ “ART 283 - Painting III Beginning”
  - courses: ART 284 ⟵ “ART 284 - Painting I Intermediate”
  - courses: ART 285 ⟵ “ART 285 - Painting II Intermediate”
  - courses: ART 286 ⟵ “ART 286 - Painting III Intermediate”
  - courses: ASL 201 ⟵ “ASL 201 - 2nd Yr American Sign Language I”
  - courses: ASL 202 ⟵ “ASL 202 - 2nd Yr American Sign Language II”
  - courses: ASL 203 ⟵ “ASL 203 - 2nd Yr American Sign Language III”
  - courses: COMM 100Z ⟵ “COMM 100Z - Introduction to Communication”
  - courses: COMM 111Z ⟵ “COMM 111Z - Public Speaking”
  - … 15 more rows
### `c14b013a7e4a2135` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=oregon-transfer-module-otm · requirement_key=cultural-literacy [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
  - courses: ANTH 201 ⟵ “ANTH 201 - Physical Anthropology and Evolution”
  - courses: ANTH 202 ⟵ “ANTH 202 - Introduction to Archaeology”
  - courses: ANTH 203 ⟵ “ANTH 203 - Language and Culture”
  - courses: ANTH 221 ⟵ “ANTH 221 - Intro to Cultural Anthropology”
  - courses: ANTH 222 ⟵ “ANTH 222 - Cultural Anthropology II”
  - courses: ANTH 223 ⟵ “ANTH 223 - Cultural Anthropology III”
  - courses: ANTH 224 ⟵ “ANTH 224 - Intro to Medical Anthropology”
  - courses: ANTH 230 ⟵ “ANTH 230 - Native North Americans: Oregon”
  - courses: ANTH 231 ⟵ “ANTH 231 - Native North Americans: PNW”
  - courses: ANTH 232 ⟵ “ANTH 232 - Native North Americans”
  - courses: COMM 220 ⟵ “COMM 220 - Gender And Communication”
  - courses: ED 258 ⟵ “ED 258 - Multicultural Education”
  - courses: ENG 107 ⟵ “ENG 107 - World Literature”
  - courses: ENG 108 ⟵ “ENG 108 - World Literature”
  - courses: ENG 109 ⟵ “ENG 109 - World Literature”
  - courses: GEOG 105 ⟵ “GEOG 105 - Cultural Geography”
  - courses: HUM 204 ⟵ “HUM 204 - World Mythology & Religion”
  - courses: HUM 205 ⟵ “HUM 205 - World Mythology & Religion”
  - courses: HUM 206 ⟵ “HUM 206 - World Mythology & Religion”
  - courses: HST 104 ⟵ “HST 104 - History of the Middle East”
  - courses: MUS 205 ⟵ “MUS 205 - Intro to Jazz History”
  - courses: MUS 206 ⟵ “MUS 206 - Intro to History of Rock and Roll”
  - courses: PSY 216 ⟵ “PSY 216 - Social Psychology”
  - courses: PSY 231 ⟵ “PSY 231 - Human Sexuality”
  - courses: SOC 208 ⟵ “SOC 208 - Sociology of Sport”
  - … 3 more rows
### `76ea581610cbf920` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount $250 ⟵ “Scholarship Douglas County Gay Archives Scholarship | Amount $250 | Application Deadline Ongoing | Download Application”
### `807ed881d7ad7216` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount $500 ⟵ “Scholarship Vera Shukle Nursing Scholarship | Amount $500 | Application Deadline Ongoing | Download Application”
### `8b6f8665b8c91e6b` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount Varies ⟵ “Scholarship Addictions.com College Scholarship | Amount Varies | Application Deadline July 31 | Apply”
### `d3ce144f9619ea09` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount Up to $2,000 ⟵ “Scholarship Southern Oregon Viticulture & Enology Scholarship | Amount Up to $2,000 | Application Deadline Ongoing | Download Application”
### `e4f45f95082c06d2` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount Varies ⟵ “Scholarship Ford Family Foundation | Amount Varies | Application Deadline TBA | Apply”
### `fc3db0f09e9790ba` Umpqua Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://umpqua.edu/become-a-student/scholarships/ (sha256 23d59d9b4f8c)
- checks: {"thresholds": null}
  - award_amount_text: Amount Up to $5,000 ⟵ “Scholarship Ford Auto Tech Scholarship | Amount Up to $5,000 | Application Deadline Ongoing | Apply”
### `3903afe00d6adfe2` University of Oregon — academic_programs 2026-27 · program_key=bachelor-s-degree-requirements-university-of-oregon-academic-catalog [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/bachelorrequirements/ (sha256 9b1aaf97cbe8)
- checks: {"courses": 20, "groups": 4, "groups_skipped": 0}
  - program_name: Bachelor's Degree Requirements | University of Oregon Academic Catalog ⟵ “Bachelor's Degree Requirements | University of Oregon Academic Catalog”
### `3ade4a5603512720` University of Oregon — degree_requirements 2026-27 · program_key=bachelor-s-degree-requirements-university-of-oregon-academic-catalog · requirement_key=bachelor-of-science-requirements-option-2 [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/bachelorrequirements/ (sha256 9b1aaf97cbe8)
  - courses: MATH 211 ⟵ “MATH 211 - Fundamentals of Elementary Mathematics I”
  - courses: MATH 212 ⟵ “MATH 212 - Fundamentals of Elementary Mathematics II”
  - courses: MATH 213 ⟵ “MATH 213 - Fundamentals of Elementary Mathematics III”
### `426aed2411577e79` University of Oregon — degree_requirements 2026-27 · program_key=bachelor-s-degree-requirements-university-of-oregon-academic-catalog · requirement_key=bachelor-of-science-requirements-option-1 [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/bachelorrequirements/ (sha256 9b1aaf97cbe8)
  - courses: MATH 105Z ⟵ “MATH 105Z - Math in Society”
  - courses: MATH 106 ⟵ “MATH 106 - University Mathematics II”
  - courses: MATH 107 ⟵ “MATH 107 - University Mathematics III”
  - courses: MATH 111Z ⟵ “MATH 111Z - Precalculus I: Functions”
  - courses: STAT 243Z ⟵ “STAT 243Z - Elementary Statistics I”
  - courses: CS 111 ⟵ “CS 111 - Introduction to Web Programming”
  - courses: CS 122 ⟵ “CS 122 - Introduction to Programming and Problem Solving”
### `599e08cfbe6769ce` University of Oregon — degree_requirements 2026-27 · program_key=bachelor-s-degree-requirements-university-of-oregon-academic-catalog · requirement_key=bachelor-of-science-requirements-2 [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/bachelorrequirements/ (sha256 9b1aaf97cbe8)
  - courses: MATH 242 ⟵ “MATH 242 - Calculus for Business and Social Science II”
  - courses: MATH 246 ⟵ “MATH 246 - Calculus for the Biological Sciences I”
  - courses: MATH 251Z ⟵ “MATH 251Z - Differential Calculus”
  - courses: CS 210 ⟵ “CS 210 - Computer Science I”
### `8fb2eae823b5ec86` University of Oregon — degree_requirements 2026-27 · program_key=bachelor-s-degree-requirements-university-of-oregon-academic-catalog · requirement_key=bachelor-of-science-requirements [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/bachelorrequirements/ (sha256 9b1aaf97cbe8)
  - courses: MATH 105Z ⟵ “MATH 105Z - Math in Society”
  - courses: MATH 106 ⟵ “MATH 106 - University Mathematics II”
  - courses: MATH 107 ⟵ “MATH 107 - University Mathematics III”
  - courses: STAT 243Z ⟵ “STAT 243Z - Elementary Statistics I”
  - courses: CS 111 ⟵ “CS 111 - Introduction to Web Programming”
  - courses: CS 122 ⟵ “CS 122 - Introduction to Programming and Problem Solving”
### `0b42aba4066789ec` University of Portland — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://ww1.up.edu/admissions/files/ib-equivalents-2025.pdf (sha256 cca432bbd5f9)
- checks: {"distinct_exams": 19, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|5]:  ⟵ “Biology HL                                                         5           3           100 Level Biology Elective          Science & Problem Solving”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|3]:  ⟵ “Business & Management HL                                       5, 6 or 7       3           100 Level General Elective                     n/a”
  - equivalencies[IB-CHEMISTRY-HL|5]:  ⟵ “Chemistry HL                                                       5           3          100 Level Chemistry Elective         Science & Problem Solving”
  - equivalencies[IB-ECONOMICS-HL|5]:  ⟵ “Economics HL                                                       5           3                     ECN 120                    Science & Problem Solving”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|5]:  ⟵ “English A: Language or English A: Language & Literature HL         5           3                     ENG 112                        Literacy & Dialogue”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French, German, Spanish Language A & B                            4            3                        101                                 n/a”
  - equivalencies[IB-FILM-HL|3]:  ⟵ “Film HL                                                        5, 6 or 7       3                      FA 108                      Aesthetics & Creativity”
  - equivalencies[IB-GEOGRAPHY-HL|3]:  ⟵ “Geography HL                                                   5, 6 or 7       3            100 Level General Elective                      n/a”
  - equivalencies[IB-GLOBAL-POLITICS-HL|3]:  ⟵ “Global Politics HL                                             5, 6 or 7       3                     POL 205                 Global & Historical Consciousness”
  - equivalencies[IB-HISTORY-HL|5]:  ⟵ “History: Americas HL                                               5           3            200 Level History Elective                      n/a”
  - equivalencies[IB-HISTORY-HL|3]:  ⟵ “History: Asia/Oceana HL                                        5, 6 or 7       3            200 Level History Elective       Global & Historical Consciousness”
  - equivalencies[IB-HISTORY-HL|5]:  ⟵ “History: Europe HL                                                 5           3                     HST 221                 Global & Historical Consciousness”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|5]:  ⟵ “Mathematics: Analysis and Approaches HL                            5           3                     MTH 121                    Science & Problem Solving”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|5]:  ⟵ “Mathematics: Applications and Interpretations HL                   5           3                     MTH 161                    Science & Problem Solving”
  - equivalencies[IB-MUSIC-HL|3]:  ⟵ “Music HL                                                       5, 6 or 7       3                      FA 108                      Aesthetics & Creativity”
  - equivalencies[IB-PHILOSOPHY-HL|3]:  ⟵ “Philosophy HL                                                  5, 6, or 7      3                     PHL 150                        Literacy & Dialogue”
  - equivalencies[IB-PHYSICS-HL|5]:  ⟵ “Physics HL                                                         5           4                  PHY 201 & 271                 Science & Problem Solving”
  - equivalencies[IB-PSYCHOLOGY-HL|3]:  ⟵ “Psychology HL                                                  5, 6 or 7       3                     PSY 101                    Science & Problem Solving”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|3]:  ⟵ “Social Anthropology HL                                         5, 6 or 7       3            100 Level General Elective       Global & Historical Consciousness”
  - equivalencies[IB-THEATRE-HL|3]:  ⟵ “Theatre Arts HL                                                 5, 6, 7        3                      FA 108                      Aesthetics & Creativity”
  - equivalencies[IB-VISUAL-ARTS-HL|3]:  ⟵ “Visual Arts HL                                                  5, 6, 7        3                      FA 107                      Aesthetics & Creativity”
### `dcd88a4f12619fc4` University of Portland — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://ww1.up.edu/admissions/files/ap-equivalents-2025.pdf (sha256 96b0706f01ae)
- checks: {"distinct_exams": 35, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4 or 5]:  ⟵ “African American Studies                   4 or 5      3             100 Level Ethnic Studies Elective             Diversity & the Common Good”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History                                4 or 5      3                           FA 107                              Aesthetics & Creativity”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                                      4         4                 100 Level Biology Elective                  Science & Problem Solving”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Calculus AB                                4 or 5      4                         MTH 201                             Science & Problem Solving”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                                  4         4                         MTH 201                             Science & Problem Solving”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “Calculus BC Subgrade                       4 or 5      4                         MTH 201                             Science & Problem Solving”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                                    4         4               100 Level Chemistry Elective                  Science & Problem Solving”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language and Culture                 4         6                      CHN 101 & 102                                      n/a”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4 or 5]:  ⟵ “Computer Science A                         4 or 5      4                       CS 203 & 273                                      n/a”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4 or 5]:  ⟵ “Computer Science Principles                4 or 5      3           200 Level Computer Science Elective                           n/a”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4 or 5]:  ⟵ “English Language and Composition           4 or 5      3                         ENG 107                                         n/a”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4 or 5]:  ⟵ “English Literature and Composition         4 or 5      3                         ENG 112                                 Literacy & Dialogue”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4 or 5]:  ⟵ “Environmental Science                      4 or 5      3                         ENV 182                             Science & Problem Solving”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History                             4         3                         HST 221                          Global & Historical Consciousness”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture                  4         6                      FRN 101 & 102                                      n/a”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Literature                            5         3                 300 Level English Elective               Global & Historical Consciousness”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language and Culture                  4         6                      GRM 101 & 102                                      n/a”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4 or 5]:  ⟵ “Human Geography                            4 or 5      3               100 Level Sociology Elective               Global & Historical Consciousness”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|5]:  ⟵ “(Japanese, Italian)                          5        12                   101, 102, 201 & 202                    Global & Historical Consciousness”
  - equivalencies[AP-LATIN|4 or 5]:  ⟵ “Latin Literature                           4 or 5      3           100 Level Foreign Language Elective                           n/a”
  - equivalencies[AP-LATIN|4 or 5]:  ⟵ “Latin: Vergil                              4 or 5      3           200 Level Foreign Language Elective                           n/a”
  - equivalencies[AP-MACROECONOMICS|4 or 5]:  ⟵ “Macroeconomics                             4 or 5      3                         ECN 120                             Science & Problem Solving”
  - equivalencies[AP-MICROECONOMICS|4 or 5]:  ⟵ “Microeconomics                             4 or 5      3                         ECN 121                             Science & Problem Solving”
  - equivalencies[AP-MUSIC-THEORY|4 or 5]:  ⟵ “Music Theory                               4 or 5      3                         MUS 101                                         n/a”
  - equivalencies[AP-PHYSICS-1|4 or 5]:  ⟵ “Physics 1                                  4 or 5      4                      PHY 201 & 271                          Science & Problem Solving”
  - … 13 more rows
### `846ac8544bb2d4ab` University of Portland — transfer_policies 2027-28 [new] (labeled_in_source)
- source: https://www.up.edu/admissions-aid/transfer-students.html (sha256 a7cb2832f14b)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “University of Portland will evaluate your college coursework for transfer credit if it’s 100-level or above and completed with a grade of C or higher.”
### `545af0ec46a5d543` Western Oregon University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 67800cbdde7d)
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 10350 ⟵ “Tuition | $10,350 | $10,350 | $10,350”
  - on_campus:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - on_campus:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - on_campus:Housing: 7597 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - on_campus:Food: 5387 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - on_campus:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - on_campus:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - on_campus:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - on_campus:Total: 30654 ⟵ “Total | $30,654 | $33,692 | $22,412”
  - off_campus_not_with_family:Tuition: 10350 ⟵ “Tuition | $10,350 | $10,350 | $10,350”
  - off_campus_not_with_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - off_campus_not_with_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - off_campus_not_with_family:Housing: 7805 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - off_campus_not_with_family:Food: 8217 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - off_campus_not_with_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - off_campus_not_with_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - off_campus_not_with_family:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - off_campus_not_with_family:Total: 33692 ⟵ “Total | $30,654 | $33,692 | $22,412”
  - with_parents_or_family:Tuition: 10350 ⟵ “Tuition | $10,350 | $10,350 | $10,350”
  - with_parents_or_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - with_parents_or_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - with_parents_or_family:Housing: 2501 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - with_parents_or_family:Food: 2241 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - with_parents_or_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - with_parents_or_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - … 2 more rows
### `79b4425d99b648f6` Western Oregon University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 67800cbdde7d)
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 30600 ⟵ “Tuition | $30,600 | $30,600 | $30,600”
  - on_campus:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - on_campus:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - on_campus:Housing: 7597 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - on_campus:Food: 5387 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - on_campus:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - on_campus:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - on_campus:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - on_campus:Total: 50904 ⟵ “Total | $50,904 | $53,942 | $42,662”
  - off_campus_not_with_family:Tuition: 30600 ⟵ “Tuition | $30,600 | $30,600 | $30,600”
  - off_campus_not_with_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - off_campus_not_with_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - off_campus_not_with_family:Housing: 7805 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - off_campus_not_with_family:Food: 8217 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - off_campus_not_with_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - off_campus_not_with_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - off_campus_not_with_family:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - off_campus_not_with_family:Total: 53942 ⟵ “Total | $50,904 | $53,942 | $42,662”
  - with_parents_or_family:Tuition: 30600 ⟵ “Tuition | $30,600 | $30,600 | $30,600”
  - with_parents_or_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - with_parents_or_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - with_parents_or_family:Housing: 2501 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - with_parents_or_family:Food: 2241 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - with_parents_or_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - with_parents_or_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - … 2 more rows

## Exceptions (202)

### `042480e03d3c21b5` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf (sha256 a67795237f61)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 3, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Cochairs Rachel Knighten (LCC) and Patricia Gimenez-Eguibar (WOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participa”
  - statements.effective: 3 ⟵ “Beginning Fall 2027, only SPA/SPA/SPAN 101Z, 102Z, and 103Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `151fedb5806c8ca9` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf (sha256 22dd3a949d6e)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Physiology I                                                                                          1 Cochairs Lindsay Biga (OSU) and Jonathan Christie (Chemeketa) **715-025-0070 institutions that do not offer an equivalent of this course are not required ”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `18b1d1169a423c8d` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf (sha256 17e08e38bba8)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf
- checks: {"effective": 3, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Cochairs Rachel Knighten (LCC) and Patricia Gimenez-Eguibar (WOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participa”
  - statements.effective: 3 ⟵ “Beginning Fall 2027, only SPA/SPN/SPAN 101Z, 102Z, and 103Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `1c4a76809143c17c` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf (sha256 e58e0082ee0c)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 3, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Cochairs Rachel Knighten (LCC) and Patricia Gimenez-Eguibar (WOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participa”
  - statements.effective: 3 ⟵ “Beginning Fall 2027, only SPA/SPN/SPAN 101Z, 102Z, and 103Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `1e776707314ba412` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/MTM-Guide-2024-2025.pdf (sha256 4ebf220e2e81)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"effective": 4, "exceptions": 4, "guarantees": 9, "requirements": 51}
  - statements.requirements: 51 ⟵ “All participating community colleges must submit a student facing document, as part of the Transfer Council required MTM documentation; 2.”
  - statements.exceptions: 4 ⟵ “In practice, most faculty subcommittees have 14 or 16 members; however, when university participation in a major is fewer than six universities, the composition of the subcommittee will be smaller.”
  - statements.guarantees: 9 ⟵ “V1. 2024                                   MTM Faculty Subcommittee Guide                                                           16 MTM CURRICULUM ARTICULATION POLICY (CAP) FRAMEWORK A Major Transfer Map (MTM) creates a statewide curriculum agreement that guarantees a student following the MTM wi”
  - statements.effective: 4 ⟵ “The Core Transfer Map (CTM) embedded in the Course Development Template ensures that students will complete at least 30 general education credits, and all universities have updated the CTM crosswalk illustrating how courses from the AAOT approved list will apply towards their general education It is”
### `204307c89d7302f8` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf (sha256 27ca61cd7045)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation Government                                                                                                1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `28817cf273640312` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf (sha256 846504ec6fac)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 2, "exceptions": 2, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Professions                                                                                                1 Cochairs Kenneth Friedrich (PCC) and Christopher Walsh (EOU) **715-025-0070 institutions that do not offer an equivalent of this course are not requi”
  - statements.effective: 2 ⟵ “Annual CCN Chemistry Subcommittee check-ins beginning in Winter 2028 to gather qualitative and/or quantitative data on faculty and student experiences, make requests for institutional and statewide data, discuss challenges, and raise concerns to review the transfer effectiveness of the CCN CH/CHE/CH”
  - statements.exceptions: 2 ⟵ “The scope of annual check-ins will focus on the statewide and collaborative nature of this work to facilitate inclusive and equitable conversations and to identify potential issues that may require future modifications of the CCN recommendations or framework every third year, starting in 2031. 2.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | October 23, 2025 outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-0”
### `28eeb7fa6ada44f9` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf (sha256 61c78404c2d1)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 1, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN History Subcommittee                                                             1 Chairs Niki Theis Coulter and Mason Tattersall **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Communicate historical knowledge and analysis effectively in written and/or verbal forms. 5.”
  - statements.guarantees: 1 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `30f091df6f00942f` state-OR — state_policies 2023-24 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/CCNS-Faculty-Subcommittee-Charge-Revised-October-2025.pdf (sha256 865b8c7faa89)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “The courses must be aligned in such a way so that institutions in this state: ●   Accept a transfer of academic credit for each course...as if the academic credit was earned at the institution that is accepting the transfer of academic credit with respect to: o   The total amount of academic credit ”
### `3e95a00f4e11eac6` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Sociology-MTM-CAP.pdf (sha256 f9858f0b8dc3)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Biology-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Communication-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Computer-Science-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/HDFS-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Psychology-AST-MTM-CAP.pdf
- checks: {"effective": 2, "exceptions": 4, "guarantees": 13, "requirements": 46}
  - statements.requirements: 46 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 13 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 4 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `42da04c8aae777d6` state-OR — state_policies 2018-19 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Elementary%20Education%20MOU%20Updates%204.28.22.pdf (sha256 3a51480106eb)
- issues: stale_year_label:2018-19, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English%20MOU%204.28.22.pdf
- checks: {"effective": 2, "exceptions": 7, "guarantees": 12, "requirements": 16}
  - statements.guarantees: 12 ⟵ “In contrast to other statewide transfer tools that prioritize university general education requirements (i.e., AAOT and ASOT), MTMs specify clear course-taking paths necessary for on-track progress towards a specific major/bachelor’s degree, with a guarantee of transfer from any Oregon community col”
  - statements.requirements: 16 ⟵ “MTMs build on the 30- credit general education foundation defined by the generic Core Transfer Map (CTM), although MTMs may specify particular relevant/required General Education courses as part of the 30-credit CTM The statewide Elementary Education Major Transfer Map (MTM) will use the Associate o”
  - statements.exceptions: 7 ⟵ “However, while CTM-related courses are guaranteed to transfer into general education, degree, or major requirements, students completing an MTM will Students who want to transfer prior to completing the MTM should talk with their community college advisor and an advisor at their target university pr”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the degree/major requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the MTM.”
### `433a81fc5a627d23` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf (sha256 04c8f864b19f)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 24}
  - statements.requirements: 24 ⟵ “2026 Common Course Numbering Articulation and Communication                                                                                               1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | November 20, 2025 exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `45264fc59e7473c3` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Psychology-AST-MTM-CAP.pdf (sha256 60b7defde2f7)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Biology-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Communication-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Computer-Science-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/HDFS-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Sociology-MTM-CAP.pdf
- checks: {"effective": 1, "exceptions": 3, "guarantees": 11, "requirements": 21}
  - statements.requirements: 21 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 11 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 1 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 3 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `4998a23e1a28d29a` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf (sha256 7a7199dc9673)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 24}
  - statements.requirements: 24 ⟵ “2026 Common Course Numbering Articulation Communication                                                                                       1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | November 20, 2025 exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `4c4de6fea55046e6` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Communication-MTM-CAP.pdf (sha256 0d50d7bbbedd)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Biology-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Computer-Science-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/HDFS-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Psychology-AST-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Sociology-MTM-CAP.pdf
- checks: {"effective": 2, "exceptions": 3, "guarantees": 11, "requirements": 27}
  - statements.requirements: 27 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 11 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 3 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `51c6fca11040a2cf` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Elementary-Education-MTM-CAP.pdf (sha256 a966b3b153ff)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/MTM-CAP-Policies.pdf
- checks: {"effective": 1, "exceptions": 4, "guarantees": 12, "requirements": 23}
  - statements.requirements: 23 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 12 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 1 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 4 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `5a4cc49ec6e9d488` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf (sha256 8530be925fd0)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 1, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN History Subcommittee                                                             1 Chairs Niki Theis Coulter and Mason Tattersall **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Communicate historical knowledge and analysis effectively in written and/or verbal forms. 5.”
  - statements.guarantees: 1 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `66ce4923c841a553` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf (sha256 a6931e365a33)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 2, "exceptions": 2, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation 2025 CCN Chemistry Subcommittee                                                             1 Cochairs Kenneth Friedrich (PCC) and Christopher Walsh (EOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to particip”
  - statements.effective: 2 ⟵ “Annual CCN Chemistry Subcommittee check-ins beginning in Winter 2028 to gather qualitative Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | October 23, 2025 and/or quantitative data on faculty and student experiences, make requests for institutional and statewi”
  - statements.exceptions: 2 ⟵ “The scope of annual check-ins will focus on the statewide and collaborative nature of this work to facilitate inclusive and equitable conversations and to identify potential issues that may require future modifications of the CCN recommendations or framework every third year, starting in 2031. 2.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
### `6797bba827b76634` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf (sha256 22e573da3b7a)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Physiology III                                                                                         1 Cochairs Lindsay Biga (OSU) and Jonathan Christie (Chemeketa) **715-025-0070 institutions that do not offer an equivalent of this course are not required”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `69c90c15b924e1a6` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf (sha256 585a89e50b3d)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Physiology II                                                                                         1 Cochairs Lindsay Biga (OSU) and Jonathan Christie (Chemeketa) **715-025-0070 institutions that do not offer an equivalent of this course are not required ”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `6cabf45116ff3c76` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf (sha256 1ac2b8fe59f2)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 2, "exceptions": 2, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation CH/CHE/CHEM 104Z Introduction to Chemistry Cochairs Kenneth Friedrich (PCC) and Christopher Walsh (EOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Annual CCN Chemistry Subcommittee check-ins beginning in Winter 2028 to gather qualitative and/or quantitative data on faculty and student experiences, make requests for institutional Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | October 23, 2025 and statewi”
  - statements.exceptions: 2 ⟵ “The scope of annual check-ins will focus on the statewide and collaborative nature of this work to facilitate inclusive and equitable conversations and to identify potential issues that may require future modifications of the CCN recommendations or framework every third year, starting in 2031. 2.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
### `7047275da8cb6af0` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/MTM-CAP-Policies.pdf (sha256 64ed307c584c)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Elementary-Education-MTM-CAP.pdf
- checks: {"effective": 2, "exceptions": 3, "guarantees": 8, "requirements": 10}
  - statements.requirements: 10 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 8 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 3 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `735649a1876d3e3a` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf (sha256 3b0127cf08db)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation Relations                                                                                             1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `7920678b609f0e06` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf (sha256 ab39640fff75)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation POL/POLS/POSC/PS 204Z Comparative Politics and Government                                                                                                 1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to partici”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `7a090788c46cb0f9` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf (sha256 a8edbd45cdac)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 1, "exceptions": 1, "guarantees": 1, "requirements": 24}
  - statements.requirements: 24 ⟵ “2026 Common Course Numbering Articulation Communication                                                                                       1 **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 1 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning     ”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `7a9d6baa0517f58c` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-CAP.pdf (sha256 6443a6a6a6d6)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Biology-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Communication-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Computer-Science-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/HDFS-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Psychology-AST-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Sociology-MTM-CAP.pdf
- checks: {"effective": 2, "exceptions": 3, "guarantees": 15, "requirements": 31}
  - statements.requirements: 31 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 15 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 3 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `7ece60a291c9dc71` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/HDFS-MTM-CAP.pdf (sha256 245c55ceed15)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Biology-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Communication-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Computer-Science-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Psychology-AST-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Sociology-MTM-CAP.pdf
- checks: {"effective": 8, "exceptions": 4, "guarantees": 14, "requirements": 40}
  - statements.requirements: 40 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 14 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 8 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 4 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `83cf7848cf6ab7ca` state-OR — state_policies 2020-21 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/FINAL%20CS%20MOU%204.28.22.pdf (sha256 5eea5f1a861a)
- issues: stale_year_label:2020-21, semantic_review_required
- checks: {"effective": 2, "exceptions": 4, "guarantees": 15, "requirements": 21}
  - statements.requirements: 21 ⟵ “In contrast to other statewide transfer tools that prioritize university general education requirements (i.e.”
  - statements.guarantees: 15 ⟵ “AAOT and ASOT), MTMs specify clear course-taking paths necessary for on-track progress towards a specific major/bachelor’s degree, with a guarantee of transfer from any Oregon community college to any Oregon public university.”
  - statements.exceptions: 4 ⟵ “However, while CTM-related courses are guaranteed to transfer into general education, degree, or major requirements, students completing an MTM will not be awarded a CTM Students who want to transfer prior to completing the MTM should talk with their community college advisor and an advisor at their”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the degree/major requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the MTM.”
### `8e08aecf9f313e9d` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf (sha256 d9e10c2e7a1b)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Chairs Rachel Knighten, Patricia Giménez-Eguíbar **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Beginning Fall 2028, only SPA/SPA/SPAN 201Z, 202Z, and 203Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | June 18, 2026 exception.”
### `8ee9a52ff2eeea20` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Biology-MTM-CAP.pdf (sha256 8e840e0ab9a4)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Communication-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Computer-Science-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/HDFS-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Psychology-AST-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Sociology-MTM-CAP.pdf
- checks: {"effective": 1, "exceptions": 5, "guarantees": 12, "requirements": 37}
  - statements.requirements: 37 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 12 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 1 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 5 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `9e74aa9cc3f3c12c` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf (sha256 773af631fa3a)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 1, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN History Subcommittee                                                             1 Chairs Niki Theis Coulter and Mason Tattersall **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Communicate historical knowledge and analysis effectively in written and/or verbal forms. 5.”
  - statements.guarantees: 1 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `ad37cf9518d58221` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (ambiguous_year_labels)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-MOU.pdf (sha256 e1bb609999bd)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"effective": 6, "exceptions": 5, "guarantees": 12, "requirements": 26}
  - statements.requirements: 26 ⟵ “In contrast to other statewide transfer tools that prioritize university general education requirements (i.e.”
  - statements.guarantees: 12 ⟵ “AAOT and ASOT), MTMs specify clear course-taking paths necessary for on-track progress towards a specific major/bachelor’s degree, with a guarantee of transfer from any Oregon community college to any Oregon public university.”
  - statements.exceptions: 5 ⟵ “However, while CTM-related courses are guaranteed to transfer into general education, degree, or major requirements, students completing an MTM will not be awarded a CTM Students who want to transfer prior to completing the MTM should talk with their community college advisor and an advisor at their”
  - statements.effective: 6 ⟵ “Eligibility to graduate following the degree/major requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the MTM.”
### `b982623e0a8d0c59` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf (sha256 a3c5469c06e6)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation CCN Spanish Subcommittee                                                              1 Chairs Rachel Knighten, Patricia Giménez-Eguíbar **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Beginning Fall 2028, only SPA/SPA/SPAN 201Z, 202Z, and 203Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | June 18, 2026 exception.”
### `c2915cacaa8a552d` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-124Z.pdf (sha256 3d4597e422af)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-231Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-232Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-BI-BIOL-BIOL-233Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-104Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-112Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-CH-CHE-CHEM-150Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-101Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-102Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2025-CCNAP-for-SPA-SPN-SPAN-103Z.pdf
- checks: {"effective": 2, "exceptions": 2, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2025 Common Course Numbering Articulation Cochairs Kenneth Friedrich (PCC) and Christopher Walsh (EOU) **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.effective: 2 ⟵ “Annual CCN Chemistry Subcommittee check-ins beginning in Winter 2028 to gather qualitative and/or quantitative data on faculty and student experiences, make requests for institutional and statewide data, discuss challenges, and raise concerns to review the transfer effectiveness of the CCN CH/CHE/CH”
  - statements.exceptions: 2 ⟵ “The scope of annual check-ins will focus on the statewide and Common Course Numbering Articulation Policy (CCNAP) | TransferCouncil@hecc.oregon.gov | October 23, 2025 collaborative nature of this work to facilitate inclusive and equitable conversations and to identify potential issues that may requi”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
### `c9b956b42875e56e` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer-Compass-2-page-CTM-MTM-use-after-approval.pdf (sha256 003d5dafaa87)
- issues: semantic_review_required
- checks: {"guarantees": 2, "requirements": 1}
  - statements.requirements: 1 ⟵ “If you haven’t chosen a major yet, and plan on transferring, Core Transfer Maps will help ensure that your general education credits will meet requirements at any of the Oregon public universities or participating The Core Transfer Maps are groups of eight classes that add up to at least 30 credits.”
  - statements.guarantees: 2 ⟵ “When you successfully complete the full set of eight courses at an Oregon community college, they are guaranteed to count toward your core bachelor’s degree requirements.”
### `d4ec890abaabdb44` state-OR — state_policies 2018-19 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English%20MOU%204.28.22.pdf (sha256 07d72801cbee)
- issues: stale_year_label:2018-19, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Elementary%20Education%20MOU%20Updates%204.28.22.pdf
- checks: {"effective": 2, "exceptions": 4, "guarantees": 13, "requirements": 20}
  - statements.requirements: 20 ⟵ “In contrast to other statewide transfer tools that prioritize university general education requirements (i.e.”
  - statements.guarantees: 13 ⟵ “AAOT and ASOT), MTMs specify clear course-taking paths necessary for on-track progress towards a specific major/bachelor’s degree, with a guarantee of transfer from any Oregon community college to any Oregon public university.”
  - statements.exceptions: 4 ⟵ “However, while CTM-related courses are guaranteed to transfer into general education, degree, or major requirements, students completing an MTM will Students who want to transfer prior to completing the MTM should talk with their community college advisor and an advisor at their target university pr”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the degree/major requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the MTM.”
### `d664fdc74a7a411b` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Computer-Science-MTM-CAP.pdf (sha256 4d13dff2c7f3)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Biology-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Communication-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/HDFS-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Psychology-AST-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Sociology-MTM-CAP.pdf
- checks: {"effective": 2, "exceptions": 8, "guarantees": 17, "requirements": 48}
  - statements.requirements: 48 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 17 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 2 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 8 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `d816f673af889868` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/pages/transfer-compass.aspx (sha256 9a42c55827bb)
- issues: semantic_review_required
- checks: {"exceptions": 1, "guarantees": 3, "requirements": 6}
  - statements.guarantees: 3 ⟵ “If you complete the full set courses at an Oregon community college and meet public university admissions requirements, you are guaranteed the courses will transfer as a block to any Oregon public university, and your coursework will count toward that university’s core bachelor’s degree requirements”
  - statements.requirements: 6 ⟵ “This is a 45-credit subset of general education courses that all count as a transferable block toward a university’s core bachelor’s degree requirements.”
  - statements.exceptions: 1 ⟵ “Associates of Arts Oregon Transfer (AAOT) Associate of Science Oregon Transfer Business (ASOT-Business) Associate of Science Oregon Transfer Computer Science (ASOT-Computer Science) Please note: a transfer degree does NOT guarantee admittance to a university or to a program, nor does it assure junio”
### `d951d71f4563c898` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (ambiguous_year_labels)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Common-Course-Numbering-Subcommittees/CCN-Handbook.pdf (sha256 6b75e43b9da9)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"effective": 4, "guarantees": 2, "requirements": 16}
  - statements.requirements: 16 ⟵ “Course alignment must be completed by December 31 of each year.”
  - statements.effective: 4 ⟵ “All approved CCN courses began using the updated policy framework (the CCNAP).”
  - statements.guarantees: 2 ⟵ “Provide input to HECC staff on policy and data questions for a report to the Legislative Assembly, including defining “lost academic credit,” recommending the number of foundational curricula and how they will transfer within and across sectors, and determining the criteria for identifying the prior”
### `deeaca51a8ea4761` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Pages/transfer-faculty-subcommittees.aspx (sha256 e2eaeb19979c)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"exceptions": 3, "requirements": 4}
  - statements.requirements: 4 ⟵ “With legislation passed in 2025 (House Bill 3026), the meetings of the subcommittees listed below are exempt from public meeting law requirements.”
  - statements.exceptions: 3 ⟵ “However, the HECC continues to make meeting information and viewing access available for partners who wish to stay informed on the work.​ CCN Faculty Subcommittee Membership and Role For more information, contact Jane Denison-Furness, jane.denison-furness@hecc.oregon.gov.”
### `e4339a85939e3877` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-203Z.pdf (sha256 e7d371c57e48)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-216Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-219Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-COM-COMM-220Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-113Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-114Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-HST-HIST-115Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-204Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-POL-POLS-POSC-PS-205Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-201Z.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/2026-CCNAP-for-SPA-SPN-SPAN-202Z.pdf
- checks: {"effective": 2, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “2026 Common Course Numbering Articulation SPA/SPN/SPAN 203Z Second-year Spanish III CCN Spanish Subcommittee                                                              1 Chairs Rachel Knighten, Patricia Giménez-Eguíbar **715-025-0070 institutions that do not offer an equivalent of this course are ”
  - statements.effective: 2 ⟵ “Beginning Fall 2028, only SPA/SPA/SPAN 201Z, 202Z, and 203Z should be offered.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
### `ed6fbfc73a4f5177` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/2998/08-State_%20Models_for_Foundational_Curricula.pdf (sha256 2348924f25ec)
- issues: semantic_review_required
- checks: {"guarantees": 2, "requirements": 12}
  - statements.requirements: 12 ⟵ “Regardless, any public institution must accept the core curriculum courses of any other public institution as a block that satisfies the core curriculum requirements of its own institution.”
  - statements.guarantees: 2 ⟵ “Colorado’s Guaranteed Transfer (GT) Pathways General Education Curriculum is designed to transfer as a block, or as individual courses, from all Colorado community colleges and to its public universities, and satisfy degree requirements.1 Colorado’s General Education Council, comprising faculty from”
### `f37beb8096e3fd0b` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/transfer-common-course-numbering/CCNAP-Template.pdf (sha256 b1bc136f5582)
- issues: semantic_review_required
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 25}
  - statements.requirements: 25 ⟵ “[Year] Common Course Numbering Articulation Course Number and Subject Code Course Title **715-025-0070 institutions that do not offer an equivalent of this course are not required to participate in the CCNAP.”
  - statements.guarantees: 2 ⟵ “Additionally, public post-secondary institutions must recognize and abide by all rights and guarantees outlined in Oregon Revised Statute (ORS) 350.423 and Oregon Administrative Rules (OAR) 715-025- Finally, an institution may not offer a course similar in course description and course learning outc”
  - statements.exceptions: 1 ⟵ “CCN course information should be adopted as written without exception.”
  - statements.effective: 1 ⟵ “The CCN Framework was subsequently updated with clarifying examples and implementation guidance and approved by the Transfer Council at its April 18, 2024 meeting.”
### `f818d8ce8d00aff7` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_heading)
- source: https://www.oregon.gov/highered/about/transfer/Pages/common-course-numbering.aspx (sha256 86a301043b69)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Pages/transfer-maps.aspx
- checks: {"exceptions": 1, "guarantees": 1, "requirements": 12}
  - statements.requirements: 12 ⟵ “SB 233 requires the HECC to establish, by rule, a CCN system and system of transfer and articulation, based on recommendations from the Transfer Council.”
  - statements.guarantees: 1 ⟵ “When transferring to an Oregon public college or university, CCN courses will be accepted as if they were taken at the institution students transfer to (that is, the receiving institution).”
  - statements.exceptions: 1 ⟵ “However, we continue to post the schedule of upcoming CCN meetings and video links on the page linked to below.Attend a Transfer Council public meeting or a CCN Subcommittee meeting.”
### `f92f57f47c98b491` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/pages/initiatives.aspx (sha256 050cb5802558)
- issues: semantic_review_required
- checks: {"requirements": 5}
  - statements.requirements: 5 ⟵ “Learn more about the structure and requirements for the programs below in the Community College Program Approval section of our site.”
### `fbdf2b20ba5acf5e` state-OR — state_policies 2027-28 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Pages/transfer-maps.aspx (sha256 e4f3aa5b25f2)
- issues: semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Pages/common-course-numbering.aspx
- checks: {"effective": 3, "guarantees": 4, "requirements": 5}
  - statements.guarantees: 4 ⟵ “If students complete a Major Transfer Map and meet public university admissions requirements, they are guaranteed transfer to a participating Oregon four-year public university with junior standing, and their coursework will count toward a bachelor’s degree in that specific major.”
  - statements.requirements: 5 ⟵ “Many Major Transfer Maps will require students to take specific courses to complete the Core portion of the Major Transfer Map.”
  - statements.effective: 3 ⟵ “This tool is updated annually.”
### `fd4189896a7ec42a` state-OR — state_policies 2024-25 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/English-MTM-CAP.pdf (sha256 cf6cc78e94b4)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Biology-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Business-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Communication-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Computer-Science-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/HDFS-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Psychology-AST-MTM-CAP.pdf,https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Transfer%20MOUs/Sociology-MTM-CAP.pdf
- checks: {"effective": 1, "exceptions": 3, "guarantees": 13, "requirements": 32}
  - statements.requirements: 32 ⟵ “The MTM CAPs identify the optimal and specific set of lower division courses students must take to transfer efficiently into the major at the university.”
  - statements.guarantees: 13 ⟵ “When students complete an MTM, the general education courses in the “Core Transfer Map” portion of the MTM, for which minimum required grades have been earned, are guaranteed to transfer into general education, degree, or major requirements for a bachelor’s degree at any Oregon public university (OR”
  - statements.effective: 1 ⟵ “Eligibility to graduate following the bachelor’s degree requirements in effect at the university during the academic year the student first enrolled in the community college that awarded the Associate of Arts Transfer degree in [MAJOR] or Associate of Science Transfer degree in [MAJOR].”
  - statements.exceptions: 3 ⟵ “Completion of the prescribed curriculum in the MTM CAP does not guarantee admission to a participating receiving institution.”
### `fe80056966bd884d` state-OR — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.oregon.gov/highered/about/transfer/Documents/Transfer-Resources/Core-Transfer-Maps-One-pager.pdf (sha256 c6ed72a42b75)
- issues: semantic_review_required
- checks: {"requirements": 9}
  - statements.requirements: 9 ⟵ “The Core Transfer Maps are broad descriptions of course requirements for students at any Oregon community college or public university.”
### `3d75e5873039926c` Blue Mountain Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/financial-aid/ (sha256 0d8dce04e8a1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “FAFSA Resources Dependency Override Petition: If extenuating family circumstances prevent the student from providing parental information, and the student meets certain criteria, the student can complete a Dependency Override Petition form listed on our website here under Financial Aid.”
### `da38a81403b7f741` Blue Mountain Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/financial-aid/ (sha256 0d8dce04e8a1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Financial Aid How it Works Apply Complete the FAFSA FAFSA Help Find answers to common Questions By completing the FAFSA you will have access to the following types of federal financial aid: Pell, FSEOG, Federal Stafford Loans, Federal Work-Study, and the option for a Professional Judgement (if needed).”
  - sentence: professional_judgment ⟵ “Professional Judgements Professional Judgment (PJ): When submitting the FAFSA, the student’s household income and asset information are used to calculate the Student Aid Index (SAI).”
  - sentence: professional_judgment ⟵ “If your household income and financial situation has changed significantly from the previous year, you may submit a Professional Judgment to request that your current income be used to determine your eligibility.”
  - sentence: professional_judgment ⟵ “BMCC retains the right to refuse certification based on professional judgment.”
### `f111ee180d0c2d47` Blue Mountain Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/financial-aid/ (sha256 0d8dce04e8a1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have questions or special circumstances, contact our office to meet with a Financial Aid Advisor.”
### `27d5f8fa024445ba` Blue Mountain Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://bluecc.edu/cost-aid/tuition-fees/ (sha256 782a1028f8b5)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition & Required Fees: 7211 ⟵ “Tuition & Required Fees | $7,211 | $7,211 | $9,936”
  - column:Books & Supplies: 1105 ⟵ “Books & Supplies | $1,105 | $1,105 | $1,105”
  - column:Living Expenses: 6450 ⟵ “Living Expenses | $6,450 | $10,800 | $10,800”
  - column:Misc./Personal Expenses: 1200 ⟵ “Misc./Personal Expenses | $1,200 | $1,200 | $1,200”
  - column:Transportation: 1974 ⟵ “Transportation | $1,974 | $1,974 | $1,974”
  - column:TOTAL: 17940 ⟵ “TOTAL | $17,940 | $22,290 | $25,015”
  - column:Tuition & Required Fees: 7211 ⟵ “Tuition & Required Fees | $7,211 | $7,211 | $9,936”
  - column:Books & Supplies: 1105 ⟵ “Books & Supplies | $1,105 | $1,105 | $1,105”
  - column:Living Expenses: 10800 ⟵ “Living Expenses | $6,450 | $10,800 | $10,800”
  - column:Misc./Personal Expenses: 1200 ⟵ “Misc./Personal Expenses | $1,200 | $1,200 | $1,200”
  - column:Transportation: 1974 ⟵ “Transportation | $1,974 | $1,974 | $1,974”
  - column:TOTAL: 22290 ⟵ “TOTAL | $17,940 | $22,290 | $25,015”
### `91a756cc5530095c` Blue Mountain Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://bluecc.edu/early-college-credit/ (sha256 d4fee169a66b)
- issues: ambiguous_year_labels
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 30 ⟵ “Dual Credit and Sponsored Dual Credit cost is $30 per credit beginning in the 2023-2024 academic year, a significantly reduced rate to the standard tuition/fees for regular BMCC students (currently $116 per credit for in-state students).”
  - per_credit_hour_charge: 116 ⟵ “Dual Credit and Sponsored Dual Credit cost is $30 per credit beginning in the 2023-2024 academic year, a significantly reduced rate to the standard tuition/fees for regular BMCC students (currently $116 per credit for in-state students).”
  - per_credit_hour_charge: 116 ⟵ “Expanded Options cost is charged at the standard tuition rate of $116 per credit. Contact your school’s ECC Liaison to see if your school pays students’ Expanded Options tuition.”
  - per_credit_hour_charge: 116 ⟵ “Registering for BMCC courses on your own is charged at the standard tuition rate of $116 per credit hour.”
### `a94a5c627afdf978` Bushnell University — appeals 2026-27 [new] (source_unlabeled)
- source: https://bushnell.edu/admissions/undergraduate-admissions/transfer-students/ (sha256 07fece288d13)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “However, students may qualify for a housing exemption if they live with a parent or guardian (with a signed housing agreement), are married, turn 21 by September 1, are enrolled in an online, Professional Studies, or Graduate program, are the parent or legal guardian of a dependent child, or qualify for a medical, financial, or special circumstance exemption.”
### `9fa1a0d14ba8cdee` Central Oregon Community College — academic_programs 2026-27 · program_key=core-transfer-maps-central-oregon-community-college-catalog [new] (labeled_in_source)
- source: https://catalog.cocc.edu/degree-certificate-overview/core-transfer-maps/ (sha256 8e0b375285e7)
- issues: requirement_groups_skipped
- checks: {"courses": 1, "groups": 1, "groups_skipped": 5}
  - program_name: Core Transfer Maps | Central Oregon Community College Catalog ⟵ “Core Transfer Maps | Central Oregon Community College Catalog”
### `849e6a2c4b2f666c` Central Oregon Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://cocc.edu/departments/admissions/grades-and-student-records/credit-for-prior-learning (sha256 8e387707422b)
- issues: rows_without_score
- checks: {"distinct_exams": 23, "equivalencies": 29, "rows_without_score": 29}
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “CLEP American Literature, score 50+ | ENG 253, 254”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “CLEP Biology, score 50+ | BI 101, 102, 103”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “CLEP Calculus with Elem. Function, score 50+ | MTH 251Z”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “CLEP Calculus with Elem. Function, score 60+ | MTH 251Z, 252Z”
  - equivalencies[CLEP-CHEMISTRY|None]:  ⟵ “CLEP Chemistry, score 50+ | CH 221Z, 222Z, 223Z”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “CLEP College Algebra, score 50+ | MTH 111Z”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|None]:  ⟵ “CLEP College Mathematics, score 50+ | MTH 105Z”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “CLEP English Literature, score 50+ | 8 credits DS Arts & Letters”
  - equivalencies[CLEP-FRENCH-LANGUAGE|None]:  ⟵ “French: score 50+ | FR 101, 102, 103”
  - equivalencies[CLEP-FRENCH-LANGUAGE|None]:  ⟵ “French: score 59+ | FR 201, 202, 203”
  - equivalencies[CLEP-GERMAN-LANGUAGE|None]:  ⟵ “German: score 50+ | GER 101, 102, 103”
  - equivalencies[CLEP-GERMAN-LANGUAGE|None]:  ⟵ “German: score 60+ | GER 201, 202, 203”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “Spanish Language: score 50+ | SPAN 101Z, 102Z, 103Z”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “Spanish Language: score 63+ | SPAN 201, 202, 203”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|None]:  ⟵ “Spanish with Writing: Score 50+ | SPAN 101Z, 102Z, 103Z”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|None]:  ⟵ “Spanish with Writing: Score 65+ | SPAN 201, 202, 203”
  - equivalencies[CLEP-NATURAL-SCIENCES|None]:  ⟵ “CLEP General Exam in Natural Sciences, score 50+ | 9 non-lab science credits for 9 non-lab science credits for "additional courses" or electives”
  - equivalencies[CLEP-HUMANITIES|None]:  ⟵ “CLEP Humanities, score 50+ | 8 credits, discipline studies arts and letters”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “CLEP Intro Business Law, score 70+ | business elective”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “CLEP Macroeconomics, score 50+ | EC 202Z”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “CLEP Microeconomics, score 50+ | EC 201Z”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|None]:  ⟵ “CLEP Principles of Management, score 70+ | business elective”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|None]:  ⟵ “CLEP Principles of Marketing, score 70+ | business elective”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “CLEP Sociology, score 50+ | SOC 204Z”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|None]:  ⟵ “CLEP US History I, score 50+ | HST 201Z”
  - … 4 more rows
### `918d207547d9b83e` Central Oregon Community College — degree_requirements 2026-27 · program_key=core-transfer-maps-central-oregon-community-college-catalog · requirement_key=core-transfer-maps-core-transfer-map [new] (labeled_in_source)
- source: https://catalog.cocc.edu/degree-certificate-overview/core-transfer-maps/ (sha256 8e0b375285e7)
- issues: requirement_groups_skipped
  - courses: WR 121Z ⟵ “WR 121Z - Composition I”
### `3862ad06a26fc486` Chemeketa Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chemeketa.edu/cost-aid/financial-aid/ (sha256 53378f46555a)
- issues: semantic_review_required, conflicting_sources:https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_SAPAppealfillableform.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have special circumstances and can provide documentation that something occurred that severed the relationship with your parent(s), and you can provide documentation that you have no contact with your parent(s), contact the Financial Aid Office.”
### `4e9081dc7a1f2ec6` Chemeketa Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_satisfactoryacademicprogress.pdf (sha256 173dc324d4f5)
- issues: semantic_review_required, conflicting_sources:https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_SAPAppealfillableform.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students will not have eligibility for any further federal aid at Chemeketa until they have met Standards of Satisfactory Academic Progress or have been granted an appeal approval. ●​ Incomplete grades have no effect on GPA but do count as attempted coursework for pace of progression standards.”
  - sentence: sap_appeal ⟵ “The decision on the Satisfactory Academic Progress Appeal is FINAL and there are no appeals to this decision unless you wish to provide additional documentation to support your Appeal.”
### `901fccdc91e3de18` Chemeketa Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_SAPAppealfillableform.pdf (sha256 65ee1e2524b2)
- issues: semantic_review_required, conflicting_sources:https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_satisfactoryacademicprogress.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Box 14007 ● Salem, OR 97309 503.399.5018 ● Fax 503.399.5528 financialaid@chemeketa.edu Satisfactory Academic Progress (SAP) Appeal Name: Chemeketa ID#: K ______________________ Degree or certificate you are currently seeking at Chemeketa: _____________________ All appeal requests must be completed in full.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Page 2 of 3 When completing the questions you must be complete in your answers.”
  - sentence: sap_appeal ⟵ “If available, attach documentation of your circumstances and/or explain why you do not have documentation. ________________________________________________________________________ Satisfactory Academic Progress (SAP) Appeal Page 3 of 3 2.”
### `947bff027e18d6f3` Chemeketa Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/cost-and-aid/financialaid_SAPAppealfillableform.pdf (sha256 65ee1e2524b2)
- issues: semantic_review_required, conflicting_sources:https://www.chemeketa.edu/cost-aid/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow appeals to be approved only if you can demonstrate mitigating circumstances, emergencies, or other unusual circumstances that led to your academic difficulties. 1.”
### `95361c29ab0246ab` Chemeketa Community College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.chemeketa.edu/cost-aid/tuition-fees/ (sha256 c4f765dd9793)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees (based on 12 credits): 1752 ⟵ “Tuition & Fees (based on 12 credits) | $1,752 | $3,504 | $5,256 | $7,008”
  - column:Books & Supplies: 400 ⟵ “Books & Supplies | $400 | $800 | $1,200 | $1,600”
  - column:Food & Housing: 7060 ⟵ “Food & Housing | $7,060 | $14,120 | $21,180 | $28,240”
  - column:Transportation: 616 ⟵ “Transportation | $616 | $1,232 | $1,848 | $2,464”
  - column:Personal: 636 ⟵ “Personal | $636 | $1,272 | $1,908 | $2,544”
  - column:Loan Fees: 22 ⟵ “Loan Fees | $22 | $44 | $66 | $88”
  - column:Total Expenses: 10486 ⟵ “Total Expenses | $10,486 | $20,972 | $31,458 | $41,944”
  - column:Tuition & Fees (based on 12 credits): 3504 ⟵ “Tuition & Fees (based on 12 credits) | $1,752 | $3,504 | $5,256 | $7,008”
  - column:Books & Supplies: 800 ⟵ “Books & Supplies | $400 | $800 | $1,200 | $1,600”
  - column:Food & Housing: 14120 ⟵ “Food & Housing | $7,060 | $14,120 | $21,180 | $28,240”
  - column:Transportation: 1232 ⟵ “Transportation | $616 | $1,232 | $1,848 | $2,464”
  - column:Personal: 1272 ⟵ “Personal | $636 | $1,272 | $1,908 | $2,544”
  - column:Loan Fees: 44 ⟵ “Loan Fees | $22 | $44 | $66 | $88”
  - column:Total Expenses: 20972 ⟵ “Total Expenses | $10,486 | $20,972 | $31,458 | $41,944”
  - column:Tuition & Fees (based on 12 credits): 5256 ⟵ “Tuition & Fees (based on 12 credits) | $1,752 | $3,504 | $5,256 | $7,008”
  - column:Books & Supplies: 1200 ⟵ “Books & Supplies | $400 | $800 | $1,200 | $1,600”
  - column:Food & Housing: 21180 ⟵ “Food & Housing | $7,060 | $14,120 | $21,180 | $28,240”
  - column:Transportation: 1848 ⟵ “Transportation | $616 | $1,232 | $1,848 | $2,464”
  - column:Personal: 1908 ⟵ “Personal | $636 | $1,272 | $1,908 | $2,544”
  - column:Loan Fees: 66 ⟵ “Loan Fees | $22 | $44 | $66 | $88”
  - column:Total Expenses: 31458 ⟵ “Total Expenses | $10,486 | $20,972 | $31,458 | $41,944”
  - column:Tuition & Fees (based on 12 credits): 7008 ⟵ “Tuition & Fees (based on 12 credits) | $1,752 | $3,504 | $5,256 | $7,008”
  - column:Books & Supplies: 1600 ⟵ “Books & Supplies | $400 | $800 | $1,200 | $1,600”
  - column:Food & Housing: 28240 ⟵ “Food & Housing | $7,060 | $14,120 | $21,180 | $28,240”
  - column:Transportation: 2464 ⟵ “Transportation | $616 | $1,232 | $1,848 | $2,464”
  - … 3 more rows
### `b7df20f5e763b241` Chemeketa Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.chemeketa.edu/admission/international/estimated-costs/ (sha256 344cf1eb1874)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.chemeketa.edu/cost-aid/financial-aid/
- checks: {"columns": 2, "rows": 5}
  - column:Tuition & Fees: 3950 ⟵ “Tuition & Fees | $3,950 | $11,850”
  - column:Books & Supplies*: 280 ⟵ “Books & Supplies* | $280 | $840”
  - column:Housing & Food**: 2400 ⟵ “Housing & Food** | $2,400 | $7,200”
  - column:Health Insurance: 495 ⟵ “Health Insurance | $495 | $1,980”
  - column:TOTALS: 7125 ⟵ “TOTALS | $7,125 | $21,870”
  - column:Tuition & Fees: 11850 ⟵ “Tuition & Fees | $3,950 | $11,850”
  - column:Books & Supplies*: 840 ⟵ “Books & Supplies* | $280 | $840”
  - column:Housing & Food**: 7200 ⟵ “Housing & Food** | $2,400 | $7,200”
  - column:Health Insurance: 1980 ⟵ “Health Insurance | $495 | $1,980”
  - column:TOTALS: 21870 ⟵ “TOTALS | $7,125 | $21,870”
### `e81bf5b37ddbd5f7` Chemeketa Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.chemeketa.edu/cost-aid/financial-aid/ (sha256 53378f46555a)
- issues: residency_unknown, conflicting_sources:https://www.chemeketa.edu/admission/international/estimated-costs/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition & Fees: 1752 ⟵ “Tuition & Fees | $1,752 | $1,752”
  - off_campus_not_with_family:Books & Supplies: 400 ⟵ “Books & Supplies | $400 | $400”
  - off_campus_not_with_family:Housing & Food: 7060 ⟵ “Housing & Food | $7,060 | $2,356”
  - off_campus_not_with_family:Transportation & Personal: 1252 ⟵ “Transportation & Personal | $1,252 | $1,252”
  - off_campus_not_with_family:Loan fees (if borrowing): 22 ⟵ “Loan fees (if borrowing) | $22 | $22”
  - off_campus_not_with_family:Total: 10486 ⟵ “Total | $10,486 | $5,282”
  - with_parents_or_family:Tuition & Fees: 1752 ⟵ “Tuition & Fees | $1,752 | $1,752”
  - with_parents_or_family:Books & Supplies: 400 ⟵ “Books & Supplies | $400 | $400”
  - with_parents_or_family:Housing & Food: 2356 ⟵ “Housing & Food | $7,060 | $2,356”
  - with_parents_or_family:Transportation & Personal: 1252 ⟵ “Transportation & Personal | $1,252 | $1,252”
  - with_parents_or_family:Loan fees (if borrowing): 22 ⟵ “Loan fees (if borrowing) | $22 | $22”
  - with_parents_or_family:Total: 5282 ⟵ “Total | $10,486 | $5,282”
### `c94138bc69ad6470` Chemeketa Community College — credit_policies 2025-26 · policy_kind=IB [new] (labeled_in_source)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/students/enrollment-services/enrollmentservices_IBEquivalencies2025_26.pdf (sha256 8791548eea41)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 4, "equivalencies": 4, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|5+]:  ⟵ “Art History                            5+              ART 2XX                4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5+]:  ⟵ “Business                 Level          5+              BA 1XX                 4”
  - equivalencies[IB-MUSIC|5+]:  ⟵ “Music            Level      5+         MUS 161           3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4]:  ⟵ “Anthropology                    4          ATH 2XX          4”
### `ec795a52447e0866` Chemeketa Community College — credit_policies 2025-26 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://www.chemeketa.edu/media/content-assets/documents/pdf/students/enrollment-services/enrollmentservices_CLEPExamEquivalencies2025_26.pdf (sha256 12746bfcd2d0)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 11, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[CLEP-HUMANITIES|50+]:  ⟵ “Humanities                      50+                             12               HUM 1XX”
  - equivalencies[CLEP-NATURAL-SCIENCES|50+]:  ⟵ “Natural Sciences                50+                             12               GS LAB”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50+]:  ⟵ “Social Sciences & History       50+                             12               SSC 1XX”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50+]:  ⟵ “American Literature             50+                             8                ENG 253, 254*”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus                        50+                             10               MTH 251Z, 252Z”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50+]:  ⟵ “College Algebra                 50+                             5                MTH 111Z”
  - equivalencies[CLEP-PRECALCULUS|50+]:  ⟵ “Precalculus                     50+                             4                MTH 241”
  - equivalencies[CLEP-ENGLISH-LITERATURE|54+]:  ⟵ “English Literature              54+                             8                ENG 204, 205*”
  - equivalencies[CLEP-BIOLOGY|50+]:  ⟵ “General Biology                 50+                             12               BI 101, 102, 103”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50+]:  ⟵ “Intro. Business Law             50+                             4                BA 226Z”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50+]:  ⟵ “Western Civilization 1 &        50+                             12               HST 1XX, 1XX, 1XX”
### `54824c14341b8925` Clackamas Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships/financial-aid-rights-and-responsibilities (sha256 df7bf10472f4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “REPORT ANY CHANGES IN YOUR FINANCIAL SITUATION If the information provided on your FAFSA has changed significantly for reasons beyond your control since you applied, contact the Office of Financial Aid and Scholarships to find out if you are eligible to submit a Change In Financial Situation appeal.”
  - sentence: need_based_special_circumstances ⟵ “Changes may include: Loss of employment Loss of untaxed income Death of a parent Unusual medical/dental expenses not covered by insurance We do not accept or review Change in Financial Situation appeals until after your current year financial aid eligibility has been determined.”
### `66bac4cda0204e79` Clackamas Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- issues: semantic_review_required, conflicting_sources:https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships/financial-aid-rights-and-responsibilities
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “To access financial aid: Submit all requested documents listed in Self Service Watch your student email and Self Service for award offer notification Review your award offer.”
### `bb707e2ca5ef907e` Clackamas Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships/financial-aid-rights-and-responsibilities (sha256 df7bf10472f4)
- issues: semantic_review_required, conflicting_sources:https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Review your Award Offer and accept any loans you wish to borrow Complete the Entrance Counseling requirement if you're a first time borrower, submit a Master Promissory Note (one time requirement every 10 years). 3.”
### `e0cff2a377df9216` Clackamas Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships/financial-aid-satisfactory-academic-progress-standards (sha256 6a5ad104c55a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Expand all Collapse all Satisfactory Academic Progress Appeal (SAP) process Satisfactory Academic Progress Appeal (SAP) process If students are in disqualified status: They are not eligible for federal financial aid.”
  - sentence: sap_appeal ⟵ “A student may appeal by completing a Satisfactory Academic Progress (SAP) Appeal form.”
### `2360494c54fb0d9b` Clackamas Community College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.clackamas.edu/docs/default-source/admissions-and-financial-aid/financial-aid-forms/2024-25/24-25-cost-of-attendance.pdf?sfvrsn=b6269c68_3 (sha256 d3c887eb6358)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 4, "rows": 12}
  - column:Tuition/fees: 2115 ⟵ “Tuition/fees | $2,115 | $4,230 | $6,345 | $8,460”
  - column:Books: 600 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 575 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 450 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:$3,740: 7480 ⟵ “$3,740 | $7,480 | $11,220 | $14,960”
  - column:Living Expenses: 3618 ⟵ “Living Expenses | $3,618 | $7,236 | $10,854 | $14,472”
  - column:Living Expenses (not: 6699 ⟵ “Living Expenses (not | $6,699 | $13,398 | $20,097 | $26,796”
  - column:Living with parent: 7358 ⟵ “Living with parent | $7,358 | $14,716 | $22,074 | $29,432”
  - column:Not living with parent: 10439 ⟵ “Not living with parent | $10,439 | $20,878 | $31,317 | $41,756”
  - column:Tuition and fees: 2115.0 ⟵ “Tuition and fees | 2115.00 | 705.00”
  - column:Books/Supplies: 600.0 ⟵ “Books/Supplies | 600.00 | 200.00”
  - column:Transportation: 575.0 ⟵ “Transportation | 575.00 | 192.00”
  - column:Personal expenses (entertainment,: 450.0 ⟵ “Personal expenses (entertainment, | 450.00 | 150.00”
  - column:Living Expenses: 3618 ⟵ “Living Expenses | $3,618”
  - column:Living Expenses (not: 6699 ⟵ “Living Expenses (not | $6,699”
  - column:Tuition/fees: 4230 ⟵ “Tuition/fees | $2,115 | $4,230 | $6,345 | $8,460”
  - column:Books: 1200 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 1150 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 900 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:$3,740: 11220 ⟵ “$3,740 | $7,480 | $11,220 | $14,960”
  - column:Living Expenses: 7236 ⟵ “Living Expenses | $3,618 | $7,236 | $10,854 | $14,472”
  - column:Living Expenses (not: 13398 ⟵ “Living Expenses (not | $6,699 | $13,398 | $20,097 | $26,796”
  - column:Living with parent: 14716 ⟵ “Living with parent | $7,358 | $14,716 | $22,074 | $29,432”
  - column:Not living with parent: 20878 ⟵ “Not living with parent | $10,439 | $20,878 | $31,317 | $41,756”
  - column:Tuition and fees: 705.0 ⟵ “Tuition and fees | 2115.00 | 705.00”
  - … 20 more rows
### `36d85d48295e79e2` Clackamas Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.clackamas.edu/admissions-financial-aid/financial-aid-scholarships (sha256 bd70ed67d4a6)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 5}
  - column:Tuition/Fees: 2175 ⟵ “Tuition/Fees | $2,175 | $4,350 | $6,525 | $8,700”
  - column:Books: 600 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 575 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 450 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:Total: 3800 ⟵ “Total | $3,800 | $7,600 | $11,400 | $15,200”
  - column:Tuition/Fees: 4350 ⟵ “Tuition/Fees | $2,175 | $4,350 | $6,525 | $8,700”
  - column:Books: 1200 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 1150 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 900 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:Total: 7600 ⟵ “Total | $3,800 | $7,600 | $11,400 | $15,200”
  - column:Tuition/Fees: 6525 ⟵ “Tuition/Fees | $2,175 | $4,350 | $6,525 | $8,700”
  - column:Books: 1800 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 1725 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 1350 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:Total: 11400 ⟵ “Total | $3,800 | $7,600 | $11,400 | $15,200”
  - column:Tuition/Fees: 8700 ⟵ “Tuition/Fees | $2,175 | $4,350 | $6,525 | $8,700”
  - column:Books: 2400 ⟵ “Books | $600 | $1,200 | $1,800 | $2,400”
  - column:Transportation: 2300 ⟵ “Transportation | $575 | $1,150 | $1,725 | $2,300”
  - column:Personal: 1800 ⟵ “Personal | $450 | $900 | $1,350 | $1,800”
  - column:Total: 15200 ⟵ “Total | $3,800 | $7,600 | $11,400 | $15,200”
### `15d071a0c30d26ad` Clatsop Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.clatsopcc.edu/financial-aid-scholarships/applying-for-aid/ (sha256 6e04fede841a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Dependency Override information for extenuating circumstances: The federal government’s regulations on dependency overrides are strict; however, there may be extenuating circumstances when a student should be considered independent.”
  - sentence: dependency_override ⟵ “Please note that dependency overrides are NOT considered for the following reasons: Parents’ refusal to contribute to student’s education.”
### `93e7b701a1e96546` Clatsop Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.clatsopcc.edu/financial-aid-scholarships/applying-for-aid/ (sha256 6e04fede841a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The formula used to determine eligibility for federal student aid is basically the same for all applicants.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances form – This form is used to request a review of your financial aid eligibility as a result of changes in financial circumstances which occurred after you filed your FAFSA.”
### `2bfef158f49733dd` Clatsop Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.clatsopcc.edu/tuition-fees/ (sha256 5d19509a49cc)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition and fees: 5418 ⟵ “Tuition and fees | $5,418”
  - column:Books and Supplies: 2800 ⟵ “Books and Supplies | $2,800”
  - column:Living, Personal, Travel: 25362 ⟵ “Living, Personal, Travel | $25,362”
  - column:Total Expenses: 33680 ⟵ “Total Expenses | $33,680”
### `ab7f38124ad293c1` Clatsop Community College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.clatsopcc.edu/financial-aid-scholarships/award-information/ (sha256 103144dc6ef1)
- issues: components_do_not_reconcile, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition and fees: 5103 ⟵ “Tuition and fees | $ 5,103”
  - column:Books, Supplies & Computer: 2800 ⟵ “Books, Supplies & Computer | $ 2,800”
  - column:Living, Personal, Travel: 23081 ⟵ “Living, Personal, Travel | $ 23,081”
  - column:Total Expenses: 31084 ⟵ “Total Expenses | $ 31,084”
### `26cfe48fa7f4b4ff` Corban University — appeals 2026-27 [new] (labeled_in_source)
- source: https://engage.corban.edu/register/specialcircumstances26-27 (sha256 fe8cd4192ebc)
- issues: semantic_review_required, conflicting_sources:https://media.corban.edu/hydra/media/files/2025/10/09/special-circumstances-paper-form-26-27.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Federal regulations allow the Financial Aid Office to use professional judgment to make changes to the original information reported on the FAFSA, when a valid reason for the change exists.”
### `313a2e94793fce15` Corban University — appeals 2026-27 [new] (labeled_in_source)
- source: https://media.corban.edu/hydra/media/files/2025/10/09/special-circumstances-paper-form-26-27.pdf (sha256 b585e1db03bf)
- issues: semantic_review_required, conflicting_sources:https://engage.corban.edu/register/specialcircumstances26-27
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Your Special Circumstances appeal cannot be processed without an explanation of your situation.”
### `6b7639a59f928e53` Corban University — appeals 2026-27 [new] (labeled_in_source)
- source: https://engage.corban.edu/register/specialcircumstances26-27 (sha256 fe8cd4192ebc)
- issues: semantic_review_required, conflicting_sources:https://media.corban.edu/hydra/media/files/2025/10/09/special-circumstances-paper-form-26-27.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form 26-27 This website uses resources that are being blocked by your network.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form 26-27 IF YOU HAVE ANY QUESTIONS, PLEASE DIRECT THEM TO: Corban University Financial Aid Office | 5000 Deer Park Drive SE | Salem, OR 97317| Phone: 503.375.7006 |Fax: 503.585.4316|Email: financialaid@corban.edu.”
  - sentence: need_based_special_circumstances ⟵ “Student Information & Circumstance Student First Name Student Last Name Please select the special circumstance(s) that applies: Student’s (and/or spouse’s) income will change significantly from the income listed on the FAFSA.”
### `808a79274d0087cb` Corban University — appeals 2025-26 [new] (labeled_in_source)
- source: https://media.corban.edu/hydra/media/files/2025/03/10/special-circumstances-form-25-26.pdf (sha256 d3a7368ffee7)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://engage.corban.edu/register/specialcircumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Your Special Circumstances appeal cannot be processed without an explanation of your situation.”
### `92db3e60d0736b57` Corban University — appeals 2025-26 [new] (labeled_in_source)
- source: https://engage.corban.edu/register/specialcircumstances (sha256 b1ffb5b3141d)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://media.corban.edu/hydra/media/files/2025/03/10/special-circumstances-form-25-26.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Federal regulations allow the Financial Aid Office to use professional judgment to make changes to the original information reported on the FAFSA, when a valid reason for the change exists.”
### `9e03fcbe407ada7d` Corban University — appeals 2025-26 [new] (labeled_in_source)
- source: https://media.corban.edu/hydra/media/files/2025/03/10/special-circumstances-form-25-26.pdf (sha256 d3a7368ffee7)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://engage.corban.edu/register/specialcircumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Circumstances Form 2025-2026 Academic Year RETURN THIS FORM TO: Corban University Financial Aid Office|5000 Deer Park Drive SE | Salem, OR 97317| Phone: 503.375.7006 |Fax: 503.585.4316|Email: financialaid@corban.edu Federal regulations allow the Financial Aid Office to use professional judgment to make changes to the original information reported on the FAFSA, when a valid reason for the c”
### `e7db3532b3f9a081` Corban University — appeals 2025-26 [new] (labeled_in_source)
- source: https://engage.corban.edu/register/specialcircumstances (sha256 b1ffb5b3141d)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://media.corban.edu/hydra/media/files/2025/03/10/special-circumstances-form-25-26.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form 25-26 This website uses resources that are being blocked by your network.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form 25-26 IF YOU HAVE ANY QUESTIONS, PLEASE DIRECT THEM TO: Corban University Financial Aid Office | 5000 Deer Park Drive SE | Salem, OR 97317| Phone: 503.375.7006 |Fax: 503.585.4316|Email: financialaid@corban.edu.”
  - sentence: need_based_special_circumstances ⟵ “Student Information & Circumstance Student First Name Student Last Name Please select the special circumstance(s) that applies: Student’s (and/or spouse’s) income will change significantly from the income listed on the FAFSA.”
### `f3150c931fa3f2f6` Corban University — appeals 2026-27 [new] (labeled_in_source)
- source: https://media.corban.edu/hydra/media/files/2025/10/09/special-circumstances-paper-form-26-27.pdf (sha256 b585e1db03bf)
- issues: semantic_review_required, conflicting_sources:https://engage.corban.edu/register/specialcircumstances26-27
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Circumstances Form 2026-2027 Academic Year RETURN THIS FORM TO: Corban University Financial Aid Office|5000 Deer Park Drive SE | Salem, OR 97317| Phone: 503.375.7006 |Fax: 503.585.4316|Email: financialaid@corban.edu Federal regulations allow the Financial Aid Office to use professional judgment to make changes to the original information reported on the FAFSA, when a valid reason for the c”
### `1b586ea084409e2e` Corban University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.corban.edu/admissions-aid/apply/real-cost-of-corban-education/ (sha256 2e4560a4d633)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.corban.edu/admissions-aid/tuition-fees/
- checks: {"columns": 2, "components_reconcile": false, "rows": 5}
  - column:Tuition and Fees: 17475 ⟵ “Tuition and Fees | $17,475 | $40,130”
  - column:Room and Board: 18183 ⟵ “Room and Board | $18,183 | $13,960”
  - column:Total Cost: 35658 ⟵ “Total Cost | $35,658 | $54,090”
  - column:Average Financial Aid: 10305 ⟵ “Average Financial Aid | $10,305** | $28,565”
  - column:FINAL COST: 25353 ⟵ “FINAL COST | $25,353 | $25,525”
  - column:Tuition and Fees: 40130 ⟵ “Tuition and Fees | $17,475 | $40,130”
  - column:Room and Board: 13960 ⟵ “Room and Board | $18,183 | $13,960”
  - column:Total Cost: 54090 ⟵ “Total Cost | $35,658 | $54,090”
  - column:Average Financial Aid: 28565 ⟵ “Average Financial Aid | $10,305** | $28,565”
  - column:FINAL COST: 25525 ⟵ “FINAL COST | $25,353 | $25,525”
### `ac3d34a45572ad3c` Corban University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.corban.edu/admissions-aid/tuition-fees/ (sha256 17c7759cb052)
- issues: conflicting_sources:https://www.corban.edu/admissions-aid/apply/real-cost-of-corban-education/
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition (12-18 Credits): 38864 ⟵ “Tuition (12-18 Credits) | $38,864”
  - column:+ Housing (with average housing cost): 7860 ⟵ “+ Housing (with average housing cost) | $7,860”
  - column:+ Food (with largest meal plan): 6100 ⟵ “+ Food (with largest meal plan) | $6,100”
  - column:+ Student Activity Fee*: 1156 ⟵ “+ Student Activity Fee* | $1,156”
  - column:+ Technology Fee: 110 ⟵ “+ Technology Fee | $110”
  - column:= Total Tuition, Food & Housing, and Fees: 54090 ⟵ “= Total Tuition, Food & Housing, and Fees | $54,090”
### `m43630f8e5c4c559` Corban University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.corban.edu/academics/dual-credit-pre-college/dual-credit-partners/ (sha256 6e8ae07e06b7)
- issues: conflicting_values:max_credit_hours_per_term
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 4, "tiers": 1}
  - per_credit_hour_charge: 125 ⟵ “$125 per credit”
  - per_credit_hour_charge: 200 ⟵ “A stipend of $200 per credit hour for courses with five or more students enrolled.”
  - per_credit_hour_charge: 75 ⟵ “Save significantly on college tuition, paying just $75 per credit for dual credit courses.”
  - eligibility_tier: 3.25 ⟵ “Have a cumulative high school GPA of 3.25 or higher.”
  - per_credit_hour_charge: 75 ⟵ “Submit an application to Corban and pay $75 per credit.”
  - eligibility_tier: 3.25 ⟵ “Have a cumulative high school GPA of 3.25 or higher.”
  - per_credit_hour_charge: 75 ⟵ “$75 per credit hour”
  - max_credit_hours_per_term: 14 ⟵ “Earn up to 14 credits total (7 per semester).”
  - per_credit_hour_charge: 75 ⟵ “Pay a special rate of just $75 per credit—an even better value than community college!”
  - eligibility_tier: 2.7 ⟵ “Current high school transcript (minimum 2.7 GPA)”
  - max_credit_hours_per_term: 7 ⟵ “Pre-college students may take a maximum of 7 credits per semester, and up to 14 credits total.”
  - max_credit_hours_per_term: 14 ⟵ “Pre-college students may take a maximum of 7 credits per semester, and up to 14 credits total.”
  - per_credit_hour_charge: 75 ⟵ “$75 per credit hour”
### `8f7695172bd84393` George Fox University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.georgefox.edu/nursing-practice/crna/tuition/index.html (sha256 c909015e6cf8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “No changes will be made during a semester, nor, unless special circumstances make such action necessary, will changes be made during a given academic year.”
### `1353718e02bc680e` Klamath Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/maintaining-your-financial-aid/satisfactory-academic-progress-policy.html (sha256 8fb5e19ff153)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Limitations A student is not limited on the number of times they can appeal due to not meeting Satisfactory Academic Progress standard.”
### `373de39074f2a7a9` Klamath Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/Special-Circumstance-Appeal.pdf (sha256 fc34caf4a842)
- issues: semantic_review_required, conflicting_sources:https://www.klamathcc.edu/en-US/admissions/financial-aid/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstance Appeal This form initiates an appeal process to request a recalculation of financial need based on special conditions.”
### `ca84f7e978656c69` Klamath Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.klamathcc.edu/en-US/admissions/financial-aid/special-circumstances.html (sha256 3504dc785340)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.klamathcc.edu/en-US/admissions/financial-aid/Special-Circumstance-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special circumstance appeals will be considered after you receive your initial award notification for the current aid year.”
  - sentence: need_based_special_circumstances ⟵ “After reviewing your verified special circumstance documentation, your aid package may remain the same, be increased, or reduced according to the financial information that has been submitted.”
  - sentence: need_based_special_circumstances ⟵ “As all files requesting special circumstance consideration will be verified, tax documents and other documents pertaining to the circumstance are required.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance request does not guarantee an adjustment will be made to your aid package. 2026-2027 Special Circumstance Appeal Once you have completed the above form you may submit it to Financial Aid in Founder Hall (building 9) or be email at [email protected].”
### `58ed9430de1084c4` Lane Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/financial-aid/satisfactory-academic-progress (sha256 b47c46b6d52a)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Probation Status means that your SAP Appeal is approved.”
  - sentence: sap_appeal ⟵ “SAP Appeal forms are available online.”
### `05e3276ba95e80d9` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “11/15 | Live Your Dream | $Varies | Women”
### `073a1bf01b7b066b` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “10/15 | American Trucks | $2,500 | Full Time /Trades”
### `16ae6e126cab374e` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “10/01 | Busy Bee's Bee You | $1,500 | US Citizen”
### `1b967281af29fc9b` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “10/31 | Zombie Apocalypse | $2,000 | US Resident”
### `2e0faa8fe6328d66` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “11/15 | Sport Clips Help a Hero | $Varies | US Citizen/Military”
### `3c8a8e5533c79aad` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “10/15 | Extreme Terrain's Student | $2,500 | Science”
### `3df9ed8881a4538a` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “11/30 | American Welding Society | $1,000 | Welding”
### `449b37af4be0dadf` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/31 | American Bullion | $1,000 | Full Time /Trades”
### `4b66e9a664e61f21` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “11/01 | Waggle Human Pet Bond | $1,000 | Full Time”
### `50d7fef454cf742d` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/31 | Chemistry Scholarship | $1,000 | Full Time”
### `515ee7eb588fa5dd` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “11/15 | Bloom Nation | $1,500 | US Citizen/3.0+GPA”
### `5310ec74ca1ee313` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “11/15 | 10 Words or Less Scholarship | $1,500 | Open”
### `53e2f552dfd583c1` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “10/31 | Alma Exley Scholarship | $6,000 | Education/minority”
### `5470a6e9ad7797b2` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “11/29 | ServiceScape | $1,000 | Open”
### `5cb2f30a166a0b2d` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “11/01 | Nick and Helena Patti Scholarship | $Varies | Italian Extraction”
### `60c21c9618cd1d16` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/31 | Delete Cyberbullying | $1,000 | Open”
### `7d2ab4f0b90b6923` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/16 | Prevounce Preventive Health | $1,000 | Health Care”
### `807e0acb8b009674` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “11/01 | Chafee ETV Grant | $Varies | Foster Care”
### `8630108a87c453d5` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/01 | SGS Scholarship | $1,000 | Legal Resident”
### `8c656346f7aa2c51` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “11/15 | Geneva Rock Scholarship | $2,000 | Construction”
### `924fcd4c97137bd4` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “10/15 | CJ Pony Parts Scholarship | $500 | Open”
### `964bb9d69c3cb824` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “10/30 | USBank Scholarship | $Varies | US Resident”
### `af47e05ca579552d` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “11/30 | Education Matters | $5,000 | Open”
### `b7afa5467952c844` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/01 | Custom Patches San Diego | $1,000 | Age 18+”
### `b954a1ddaa64e51c` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “10/15 | American Muscle | $2,500 | Automotive”
### `bfb9f70425e36dac` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “11/01 | American Indian Services | $2,000 | Native American”
### `d10b48ab2b732cb1` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “10/04 | Lounge Lizard Scholarship | $1,000 | Web Design”
### `d9c4a9d899d9d40c` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “10/31 | Financial Goals | $2,000 | Legal Resident”
### `ddedfbb3d5cfb6e9` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “10/31 | American Culinary Federation | $Varies | Culinary”
### `ec7b8154388d0107` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $Varies ⟵ “10/01 | Benjamin Gilman | $Varies | Study Abroad”
### `ef8f7f07e136767a` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “11/15 | James Allen Cox | $2,500 | Sophomore”
### `f8086e2801930ce1` Lane Community College — awards 2024-25 [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/paying-college/scholarships/how-find-scholarships (sha256 de9ac93894b3)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “11/30 | Cappex Easy Money | $1,000 | Open”
### `2e2e2c7f18ac1337` Lane Community College — credit_policies 2024-25 · policy_kind=IB [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/transferring-prior-college-credit-lane/credit-prior-learning (sha256 bcc6a339ca6f)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 38, "equivalencies": 56, "rows_without_score": 0}
  - equivalencies[IB-HISTORY-SL|Art History - SL]:  ⟵ “Art History - SL | 4+ | ARH 1XX | 3 | AL”
  - equivalencies[IB-BIOLOGY-SL|Biology - SL]:  ⟵ “Biology - SL | 4 | BI 101 | 4 | LSCI”
  - equivalencies[IB-BIOLOGY-SL|Biology - SL]:  ⟵ “Biology - SL | 5+ | BI 221Z | 5 | LSCI”
  - equivalencies[IB-BIOLOGY-HL|Biology - HL]:  ⟵ “Biology - HL | 4 | BI 221Z, 222Z | 10 | LSCI”
  - equivalencies[IB-BIOLOGY-HL|Biology - HL]:  ⟵ “Biology - HL | 5+ | BI 221Z, 222Z, 223Z | 15 | LSCI”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|Business Management SL/HL]:  ⟵ “Business Management SL/HL | 4+ | BA 1XX | 4 | NONE”
  - equivalencies[IB-CHEMISTRY-SL|Chemistry - SL]:  ⟵ “Chemistry - SL | 4 | CH 104Z, 124Z | 5 | LSCI”
  - equivalencies[IB-CHEMISTRY-SL|Chemistry - SL]:  ⟵ “Chemistry - SL | 5+ | CH 221Z, 227Z | 5 | LSCI”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry - HL]:  ⟵ “Chemistry - HL | 4 | CH 221Z, 222Z, 227Z, 228Z | 12 | LSCI”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry - HL]:  ⟵ “Chemistry - HL | 5+ | CH 221Z, 222Z, 223Z, 227Z, 228Z, 229Z | 15 | LSCI”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|Computer Science - SL]:  ⟵ “Computer Science - SL | 4+ | CS 161 | 4 | SCI”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|Computer Science - HL]:  ⟵ “Computer Science - HL | 4+ | CS 161, 162 | 8 | SCI”
  - equivalencies[IB-ECONOMICS-SL|Economics- SL]:  ⟵ “Economics- SL | 4+ | ECON 201Z | 4 | SOSC”
  - equivalencies[IB-ECONOMICS-HL|Economics-HL]:  ⟵ “Economics-HL | 4+ | ECON 201Z, 202Z | 8 | SOSC”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|Environmental Systems & Societies - SL]:  ⟵ “Environmental Systems & Societies - SL | 4+ | ENSC 181 | 4 | LSCI”
  - equivalencies[IB-FILM-SL|Film - SL]:  ⟵ “Film - SL | 4+ | FA 264 | 4 | AL, CL”
  - equivalencies[IB-FILM-HL|Film - HL]:  ⟵ “Film - HL | 4+ | FA 264, 276 | 8 | AL, CL”
  - equivalencies[IB-GEOGRAPHY-SL|Geography - SL/HL]:  ⟵ “Geography - SL/HL | 4+ | GEOG 142 | 4 | SOSC; CL”
  - equivalencies[IB-GLOBAL-POLITICS-SL|Global Politics - SL/HL]:  ⟵ “Global Politics - SL/HL | 4+ | PS 205 | 4 | SOSC; CL”
  - equivalencies[IB-HISTORY-SL|History SL/HL]:  ⟵ “History SL/HL | 4+ | HST 2XX | 4 | SOSC”
  - equivalencies[IB-HISTORY-HL|History: Africa - HL]:  ⟵ “History: Africa - HL | 4+ | HST 2XX | 4 | SOSC; CL”
  - equivalencies[IB-HISTORY-HL|History: Americas - HL]:  ⟵ “History: Americas - HL | 4+ | HST 201Z, 202Z, 203Z | 12 | SOSC: CL”
  - equivalencies[IB-HISTORY-HL|History: Asia/Oceania - HL]:  ⟵ “History: Asia/Oceania - HL | 4+ | HST 2XX | 4 | SOSC; CL”
  - equivalencies[IB-HISTORY-HL|History: Europe & Middle East - HL]:  ⟵ “History: Europe & Middle East - HL | 4+ | HST 104, 105, 106 | 12 | SOSC; CL”
  - equivalencies[IB-HISTORY-SL|History: Modern World - SL]:  ⟵ “History: Modern World - SL | 4+ | HST 2XX | 4 | SOSC”
  - … 31 more rows
### `4111259470651d2f` Lane Community College — credit_policies 2024-25 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/transferring-prior-college-credit-lane/credit-prior-learning (sha256 bcc6a339ca6f)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 35, "equivalencies": 59, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3+]:  ⟵ “2-D Art and Design | 3+ | ART 115 | 4 | AL”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art and Design | 3+ | ART 117 | 4 | AL”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARH 206 | 3 | AL”
  - equivalencies[AP-ART-HISTORY|4+]:  ⟵ “Art History | 4+ | ARH 204, 206 | 6 | AL”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BI 101, BI 1XX | 8 | LSCI for BI 101; SCI for BI 1XX”
  - equivalencies[AP-BIOLOGY|4+]:  ⟵ “Biology | 4+ | BI 221Z, BI 223Z | 10 | LSCI”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MTH 251Z | 4 | SCI”
  - equivalencies[AP-CALCULUS-AB|4+]:  ⟵ “Calculus AB | 4+ | MTH 251Z, 252Z | 8 | SCI”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MTH 251Z, 252Z | 8 | SCI”
  - equivalencies[AP-CALCULUS-BC|4+]:  ⟵ “Calculus BC | 4+ | MTH 251Z, 252Z, 253Z | 12 | SCI”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CH 104Z, 124Z | 5 | LSCI”
  - equivalencies[AP-CHEMISTRY|4+]:  ⟵ “Chemistry | 4+ | CH 221Z, 222Z, 223Z, 227Z, 228Z, 229Z | 15 | LSCI”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | CHN 101, 102, 103 | 12 | NONE”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4+]:  ⟵ “Chinese Language & Culture | 4+ | YFL 2X1, 2X2, 2X3 | 12 | AL”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CS 1XX | 4 | NONE”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4+]:  ⟵ “Computer Science A | 4+ | CS 161 | 4 | SCI”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | CS 1XX | 4 | NONE”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4+]:  ⟵ “Computer Science Principles | 4+ | CS 160 | 4 | SCI”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Drawing | 3+ | ART 131 | 4 | AL”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language & Composition | 3+ | WR 121Z | 4 | NONE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition | 3+ | ENG 104Z | 4 | AL”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science | 3+ | ENSC 181 | 4 | LSCI”
  - equivalencies[AP-EUROPEAN-HISTORY|3+]:  ⟵ “European History | 3+ | HST 101, 102 | 8 | SOSC”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3+]:  ⟵ “French: Language & Culture | 3+ | FR 201, 202, 203 | 12 | AL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3+]:  ⟵ “French: Literature | 3+ | FR 2XX | 4 | AL”
  - … 34 more rows
### `e23a46772dfcfe7c` Lane Community College — credit_policies 2024-25 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://www.lanecc.edu/costs-admission/transferring-prior-college-credit-lane/credit-prior-learning (sha256 bcc6a339ca6f)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 21, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences / History | 50 | History | 12 | SOSC”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | Science | 9 | SCI”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Arts & Letters | 9 | AL”
  - equivalencies[CLEP-AMERICAN-LITERATURE|55+]:  ⟵ “American Literature | 55+ | ENG 253 | 4 | AL”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50+]:  ⟵ “Analyzing & Interpreting Literature | 50+ | ENG 104Z | 4 | AL”
  - equivalencies[CLEP-BIOLOGY|50+]:  ⟵ “Biology | 50+ | BI 101, 102, 103 | 12 | LSCI”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus: Elementary | 50+ | MTH 251Z | 4 | SCI”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus w/ Elementary Functions | 50+ | MTH 251Z, 252Z | 8 | SCI”
  - equivalencies[CLEP-CHEMISTRY|50+]:  ⟵ “Chemistry: General | 50+ | CH 221Z, 222Z, 223Z, 227Z, 228Z, 229Z | 15 | LSCI”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|47+]:  ⟵ “College Algebra | 47+ | MTH 111Z | 4 | SCI”
  - equivalencies[CLEP-ENGLISH-LITERATURE|55+]:  ⟵ “English Literature | 55+ | ENG 204 | 4 | AL”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50+]:  ⟵ “French: College French I & II | 50+ | FR 103 | 5 | NONE”
  - equivalencies[CLEP-FRENCH-LANGUAGE|54+]:  ⟵ “French: College French I & II | 54+ | FR 103, 201 | 9 | AL (201 ONLY)”
  - equivalencies[CLEP-FRENCH-LANGUAGE|56+]:  ⟵ “French: College French I & II | 56+ | FR 201, 202 | 8 | AL”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59+]:  ⟵ “French: College French I & II | 59+ | FR 201, 202, 203 | 12 | AL”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60+]:  ⟵ “German: College German I & II | 60+ | YFL 2X1, 2X2, 2X3 | 12 | AL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50+]:  ⟵ “History of the United States I (American History) | 50+ | HST 201Z | 4 | SOSC; CL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50+]:  ⟵ “History of the United States II (American History) | 50+ | HST 203Z | 4 | SOSC; CL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50+ each]:  ⟵ “History of the United States I & II (Both tests) | 50+ each | HST 201Z, 202Z, 203Z | 12 | SOSC; CL”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50+]:  ⟵ “Macroeconomics | 50+ | ECON 202Z | 4 | SOSC”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50+]:  ⟵ “Microeconomics | 50+ | ECON 201Z | 4 | SOSC”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50+]:  ⟵ “Psychology | 50+ | PSY 201Z, 202Z | 8 | SOSC”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|74+]:  ⟵ “Sociology | 74+ | SOC 204Z | 4 | SOSC”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50+]:  ⟵ “Spanish: College Spanish I & II | 50+ | SPAN 103Z | 4 | NONE”
  - equivalencies[CLEP-SPANISH-LANGUAGE|55+]:  ⟵ “Spanish: College Spanish I & II | 55+ | SPAN 103Z, 201 | 8 | AL; CL (201 ONLY)”
  - … 5 more rows
### `569651ea4f72a128` Linfield University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.linfield.edu/assets/files/institutional-research/2025-2026-Common-Data-Set-6-2-2026.pdf (sha256 aa8e0b58fb19)
- issues: c1_totals_incomplete, stale_year_label:2024-25, conflicting_sources:https://www.linfield.edu/assets/files/institutional-research/CDS-2024-2025-PDF-Linfield-04.21.2025.pdf
- checks: {"fields": ["applications", "enrolled", "entering_fall_year"]}
  - applications: 2522 ⟵ “Total first-time, first-year (degree-seeking) who applied                  1424                 992                   74         32          2522”
  - enrolled: 383 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                     244              135                    4             0           383”
### `b778a6eade73a955` Linfield University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.linfield.edu/assets/files/institutional-research/CDS-2024-2025-PDF-Linfield-04.21.2025.pdf (sha256 4e35684e7047)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.linfield.edu/assets/files/institutional-research/2025-2026-Common-Data-Set-6-2-2026.pdf
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 2629 ⟵ “Total first-time, first-year (degree-seeking) who applied          1374       1152             89          14      2629”
  - admits: 2239 ⟵ “Total first-time, first-year (degree-seeking) who were admitted    1213         995            20          11      2239”
  - enrolled: 381 ⟵ “Total first-time, first-year (degree-seeking) enrolled              240         137              4          0       381”
### `32f93abc32bf3f21` Oregon Coast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.oregoncoast.edu/financial-aid-satisfactory-academic-progress-sap-policy (sha256 bb0e4726f33f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The Financial Aid Probation status is based on the professional judgment of the financial aid office where it is determined the student is likely to meet financial aid SAP standards by the end of the next term.”
### `f1e2ea0747b888d1` Oregon Coast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.oregoncoast.edu/financial-aid-satisfactory-academic-progress-sap-policy (sha256 bb0e4726f33f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students who have their financial aid suspended have the right to file a Satisfactory Academic Progress Appeal with the financial aid office.”
  - sentence: sap_appeal ⟵ “Appeal Process In order to complete a financial aid SAP appeal, a student must first meet with their student success coach.”
### `0b4f2c10b709aa62` Oregon Institute of Technology — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.oit.edu/sites/default/files/2026/documents/Financial%20Aid%20Award%20Guide%202026-27_0.pdf (sha256 bbd183b8d61a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “For Fall 541-885-1280 (phone) SUMMER AID term, SAP appeals must be submitted by the end of the business day, 541-885-1024 (fax) Summer is the beginning of the award year.”
### `4d5bc970e13e362b` Oregon Institute of Technology — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.oit.edu/sites/default/files/2026/documents/Financial%20Aid%20Award%20Guide%202026-27_0.pdf (sha256 bbd183b8d61a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “There is an origination fee, and the interest rate Direct Stafford Unsubsidized Loans for Graduate Students aid and bill. academic progress due to special circumstances for the 2025-2026 school year was 6.39%.”
### `52f61a34acb4c047` Oregon Institute of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.oit.edu/college-costs/financial-aid/resources/verification-requests (sha256 8fc2fdb240f2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Verification, Special Circumstances and Additional Info Requests | Oregon Tech Skip to main content Prev Prev Apply Visit Give Quicklinks TECHweb Directory Course Search Current Students Academic Calendar Faculty & Staff Foundation Alumni Library Tech Nest Store (Bookstore) Cashier's Office Search Search About Toggle submenu Oregon's Polytechnic Oregon Tech is a public university recognized as Ore”
### `6e2709b40a85d26d` Oregon Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.oit.edu/sites/default/files/2025/documents/25-26%20SAP%20Appeal%20Form.pdf (sha256 8bfff7fb95d6)
- issues: semantic_review_required, conflicting_sources:https://www.oit.edu/college-costs/financial-aid/resources/satisfactory-academic-progress-sap,https://www.oit.edu/sites/default/files/2026/documents/26-27%20SAP%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL FORM SAP Appeal Deadlines are as follows: Summer Term 2025 -July 1,2025, Fall Term 2025 - October 9, 2026, Winter Term 2026 - January 13, 2026, and Spring Term 2026 - April 7, 2026.”
  - sentence: sap_appeal ⟵ “Standard Repayment amount: ____________________ The outcome of your Satisfactory Academic Progress Appeal will be communicated to you in writing and sent to your OIT e-mail address.”
  - sentence: sap_appeal ⟵ “Second SAP appeals that cite the same reasons as your first appeal will not be approved.”
### `9e26c6bbf8d5e905` Oregon Institute of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.oit.edu/sites/default/files/2026/documents/26-27%20SAP%20Appeal%20Form.pdf (sha256 da2b26062940)
- issues: semantic_review_required, conflicting_sources:https://www.oit.edu/college-costs/financial-aid/resources/satisfactory-academic-progress-sap,https://www.oit.edu/sites/default/files/2025/documents/25-26%20SAP%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL FORM SAP Appeal Deadlines are as follows: Summer Term 2026 –June 30, 2026, Fall Term 2026 - October 9, 2027, Winter Term 2027 - January 12, 2027, and Spring Term 2027 - April 6, 2027.”
  - sentence: sap_appeal ⟵ “Standard Repayment amount: ____________________ The outcome of your Satisfactory Academic Progress Appeal will be communicated to you in writing and sent to your OIT e-mail address.”
  - sentence: sap_appeal ⟵ “Second SAP appeals that cite the same reasons as your first appeal will not be approved.”
### `ab206fe3607729fa` Oregon Institute of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.oit.edu/college-costs/financial-aid/resources/satisfactory-academic-progress-sap (sha256 130f7e7db0b9)
- issues: semantic_review_required, conflicting_sources:https://www.oit.edu/sites/default/files/2025/documents/25-26%20SAP%20Appeal%20Form.pdf,https://www.oit.edu/sites/default/files/2026/documents/26-27%20SAP%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Eligibility may be reinstated if student can reestablish satisfactory academic progress without benefit of financial aid (2.0 and making pace) or appeal and be approved by the financial aid appeal committee.”
  - sentence: sap_appeal ⟵ “Holds may be appealed using a SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “Financial Aid Appeals Process and Timeline If you wish to appeal a hold on your financial aid based on extenuating circumstances, please follow these steps: Obtain a Satisfactory Academic Progress Appeal Form (www.oit.edu/faid/forms) Complete the appeal form according to instructions.”
### `0d31a9994b2fc1c1` Oregon State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.oregonstate.edu/admission-appeals (sha256 b8f2b2fd89d2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Your statement must specifically address: The extraordinary circumstances why you did not meet and exceed Oregon State’s minimum admissions requirements What you have done or are doing to mitigate the impact of your extraordinary circumstances What are your strengths and how they will result in your success at Oregon State Why you have chosen Oregon State University Your academic and/or career goa”
### `33927566d6950ddb` Oregon State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.oregonstate.edu/satisfactory-academic-progress (sha256 95b01dbfe22c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “You will find the link to complete a SAP appeal through your portal.”
### `095ed1d955967402` Oregon State University-Cascades Campus — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 b50de8079fa6)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (15 CR)1: 15246 ⟵ “Tuition and Fees (15 CR)1 | $15,246 | $5,082”
  - column:Living Expenses (Food and Housing)2: 17205 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Estimated Billable Cost Total: 32451 ⟵ “Estimated Billable Cost Total | $32,451 | $10,817”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 2817 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 879 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 4296 ⟵ “Estimated Non-Billable Cost Total | $4,296 | $1,432”
  - column:Estimated TOTAL: 36747 ⟵ “Estimated TOTAL | $36,747 | $12,249”
  - column:Tuition and Fees (15 CR)1: 5082 ⟵ “Tuition and Fees (15 CR)1 | $15,246 | $5,082”
  - column:Living Expenses (Food and Housing)2: 5735 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Estimated Billable Cost Total: 10817 ⟵ “Estimated Billable Cost Total | $32,451 | $10,817”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 939 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 293 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 1432 ⟵ “Estimated Non-Billable Cost Total | $4,296 | $1,432”
  - column:Estimated TOTAL: 12249 ⟵ “Estimated TOTAL | $36,747 | $12,249”
### `2d3f906323b75562` Oregon State University-Cascades Campus — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 b50de8079fa6)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (15 CR)1: 40392 ⟵ “Tuition and Fees (15 CR)1 | $40,392 | $13,464”
  - column:Living Expenses (Food and Housing)2: 17205 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Estimated Billable Cost Total: 57597 ⟵ “Estimated Billable Cost Total | $57,597 | $19,199”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 2817 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 879 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 4296 ⟵ “Estimated Non-Billable Cost Total | $4,296 | $1,432”
  - column:Estimated TOTAL: 61893 ⟵ “Estimated TOTAL | $61,893 | $20,631”
  - column:Tuition and Fees (15 CR)1: 13464 ⟵ “Tuition and Fees (15 CR)1 | $40,392 | $13,464”
  - column:Living Expenses (Food and Housing)2: 5735 ⟵ “Living Expenses (Food and Housing)2 | $17,205 | $5,735”
  - column:Estimated Billable Cost Total: 19199 ⟵ “Estimated Billable Cost Total | $57,597 | $19,199”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 939 ⟵ “Personal and Miscellaneous | $2,817 | $939”
  - column:Transportation: 293 ⟵ “Transportation | $879 | $293”
  - column:Estimated Non-Billable Cost Total: 1432 ⟵ “Estimated Non-Billable Cost Total | $4,296 | $1,432”
  - column:Estimated TOTAL: 20631 ⟵ “Estimated TOTAL | $61,893 | $20,631”
### `86b93b6a87c7bd82` Oregon State University-Cascades Campus — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 b50de8079fa6)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (15 CR)1: 16014 ⟵ “Tuition and Fees (15 CR)1 | $16,014 | $5,338”
  - column:Living Expenses (Food and Housing)2: 18066 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Estimated Billable Cost Total: 34080 ⟵ “Estimated Billable Cost Total | $34,080 | $11,360”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 2958 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 930 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 4488 ⟵ “Estimated Non-Billable Cost Total | $4,488 | $1,496”
  - column:Estimated TOTAL: 38568 ⟵ “Estimated TOTAL | $38,568 | $12,856”
  - column:Tuition and Fees (15 CR)1: 5338 ⟵ “Tuition and Fees (15 CR)1 | $16,014 | $5,338”
  - column:Living Expenses (Food and Housing)2: 6022 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Estimated Billable Cost Total: 11360 ⟵ “Estimated Billable Cost Total | $34,080 | $11,360”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 986 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 310 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 1496 ⟵ “Estimated Non-Billable Cost Total | $4,488 | $1,496”
  - column:Estimated TOTAL: 12856 ⟵ “Estimated TOTAL | $38,568 | $12,856”
### `e5871dcdfdba171b` Oregon State University-Cascades Campus — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.oregonstate.edu/cost-attendance (sha256 b50de8079fa6)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees (15 CR)1: 42459 ⟵ “Tuition and Fees (15 CR)1 | $42,459 | $14,153”
  - column:Living Expenses (Food and Housing)2: 18066 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Estimated Billable Cost Total: 60525 ⟵ “Estimated Billable Cost Total | $60,525 | $20,175”
  - column:Books, Course Materials, Supplies, and Equipment: 600 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 2958 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 930 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 4488 ⟵ “Estimated Non-Billable Cost Total | $4,488 | $1,496”
  - column:Estimated TOTAL: 65013 ⟵ “Estimated TOTAL | $65,013 | $21,671”
  - column:Tuition and Fees (15 CR)1: 14153 ⟵ “Tuition and Fees (15 CR)1 | $42,459 | $14,153”
  - column:Living Expenses (Food and Housing)2: 6022 ⟵ “Living Expenses (Food and Housing)2 | $18,066 | $6,022”
  - column:Estimated Billable Cost Total: 20175 ⟵ “Estimated Billable Cost Total | $60,525 | $20,175”
  - column:Books, Course Materials, Supplies, and Equipment: 200 ⟵ “Books, Course Materials, Supplies, and Equipment | $600 | $200”
  - column:Personal and Miscellaneous: 986 ⟵ “Personal and Miscellaneous | $2,958 | $986”
  - column:Transportation: 310 ⟵ “Transportation | $930 | $310”
  - column:Estimated Non-Billable Cost Total: 1496 ⟵ “Estimated Non-Billable Cost Total | $4,488 | $1,496”
  - column:Estimated TOTAL: 21671 ⟵ “Estimated TOTAL | $65,013 | $21,671”
### `03c5f58f88564756` Pacific Bible College — appeals 2026-27 [new] (source_unlabeled)
- source: https://pacificbible.edu/admissions/financial-aid (sha256 7e7c2fa8fcee)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: professional_judgment ⟵ “Guide to: studentaid.gov/apply-for-aid/fafsa/filling-out/help/before-starting Program Facts Important Links & Information Free Application for Federal Student Aid (FAFSA) Satisfactory Academic Progress Policy Budgeting for Students fastweb Professional Judgement If a student’s income has significantly changed impacting their ability to pay for college (for example: Job loss or layoff due to COVID,”
  - sentence: professional_judgment ⟵ “For more information about Professional Judgments, please see the Financial Aid Coordinator.”
  - sentence: professional_judgment ⟵ “So what IS Professional Judgement?”
  - sentence: professional_judgment ⟵ “FAFSA pulls information from 2 years prior, so if that student has had a job change and their income is significantly less than it was on the tax forms used for their FAFSA, the Financial Aid Coordinator can perform what is called a “Professional Judgement”.”
  - sentence: professional_judgment ⟵ “A Professional Judgment is a process Financial Aid offices perform that provides the ability to make adjustments to information provided by students in their Free Application for Financial Student Aid (FAFSA) applications.”
  - sentence: professional_judgment ⟵ “Professional Judgements are reserved for Special Circumstances that affect the student’s financial situation (such as a job loss/layoff), and for Unusual circumstances that affect the student’s dependency status (such as parental abandonment, etc.).”
### `21e7576773a80877` Pacific Northwest College of Art — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://willamette.edu/cost-aid/tuition (sha256 a63d47dd4885)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "rows": 7}
  - column:Tuition: 28320 ⟵ “Tuition | $28,320 | Per semester”
  - column:Student Activity Fee1: 146 ⟵ “Student Activity Fee1 | $146 | Per semester”
  - column:Meal Plan – Living on campus (14-meal plan): 4270 ⟵ “Meal Plan – Living on campus (14-meal plan) | $4,270 | Per semester”
  - column:Housing – Living on campus3 (Standard double room): 4595 ⟵ “Housing – Living on campus3 (Standard double room) | $4,595 | Per semester”
  - column:Residence Hall Fee: 75 ⟵ “Residence Hall Fee | $75 | Per semester”
  - column:Sub-Total: 37406 ⟵ “Sub-Total | $37,406 | Per semester”
  - column:ANNUAL COST (2 semesters): 74812 ⟵ “ANNUAL COST (2 semesters) | $74,812 | Per Year”
### `a531e8d0145b1607` Pacific University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pacificu.edu/directory/student-affairs/office-financial-aid/undergrad-financial-aid-policies/satisfactory-academic-progress (sha256 0fec719744c9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Probation If students fail to meet satisfactory academic progress standards for a second consecutive term, they may appeal their financial aid suspension.”
  - sentence: sap_appeal ⟵ “Academic Plan If students fail to meet satisfactory academic progress at the end of the probationary period, they may appeal the Financial Aid Suspension.”
### `0737432f46b3a9a9` Pacific University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships/cost-attendance (sha256 baa59eadd31a)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 58348 ⟵ “Tuition & Fees | $58,348”
  - column:Room & Meals*: 16272 ⟵ “Room & Meals* | $16,272”
  - column:Books & Supplies: 1050 ⟵ “Books & Supplies | $1,050”
  - column:Personal Expenses: 1000 ⟵ “Personal Expenses | $1,000”
  - column:Transportation: 800 ⟵ “Transportation | $800”
  - column:Loan Fees: 72 ⟵ “Loan Fees | $72”
  - column:Total: 77542 ⟵ “Total | $77,542”
### `650cba9a8d554bb7` Pacific University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships (sha256 589722718aee)
- issues: conflicting_sources:https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships/cost-attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition & Fees: 60100 ⟵ “Tuition & Fees | $60,100”
  - column:Room & Board: 16834 ⟵ “Room & Board | $16,834”
  - column:Total Direct Cost: 76934 ⟵ “Total Direct Cost | $76,934”
### `b2b3dad0bb41b4df` Pacific University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships/cost-attendance (sha256 baa59eadd31a)
- issues: conflicting_sources:https://www.pacificu.edu/admissions/undergraduate-admissions/estimated-costs-scholarships
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 60100 ⟵ “Tuition & Fees | $60,100”
  - column:Room & Meals*: 16834 ⟵ “Room & Meals* | $16,834”
  - column:Books & Supplies: 1050 ⟵ “Books & Supplies | $1,050”
  - column:Personal Expenses: 1000 ⟵ “Personal Expenses | $1,000”
  - column:Transportation: 800 ⟵ “Transportation | $800”
  - column:Loan Fees: 72 ⟵ “Loan Fees | $72”
  - column:Total: 79856 ⟵ “Total | $79,856”
### `13072604383e8e6a` Portland Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pcc.edu/enroll/paying-for-college/financial-aid/review-award/change-in-situation/ (sha256 9c70dddd953c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Change in income appeal | Enroll at PCC Skip to page content Portland Community College | Portland, Oregon Menu Get Started Programs Class Schedule About Student Life Search Resources Contacts Calendars Give Log in to MyPCC Enroll at PCC PCC / Enroll at PCC / Paying for college / Financial aid / 3.”
  - sentence: need_based_special_circumstances ⟵ “Review and accept award / Change in income appeal If your income has changed since you submitted the FAFSA, let us know.”
  - sentence: need_based_special_circumstances ⟵ “The appeal process Review and complete the Change in Income Appeal.”
### `2c6770773da19ea0` Portland Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.pcc.edu/enroll/paying-for-college/financial-aid/review-award/cost-of-attendance/ (sha256 e03defc4470d)
- issues: arrangement_unlabeled, conflicting_sources:https://www.pcc.edu/international-students/admissions/required-documents/,https://www.pcc.edu/international-students/student-resources/tuition-financial/
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - column:Tuition & fees: 1870 ⟵ “Tuition & fees | $1,870 | $3,740 | $5,610 | $7,480”
  - column:Books & supplies: 596 ⟵ “Books & supplies | $596 | $1,192 | $1,788 | $2,384”
  - column:Food & housing: 5324 ⟵ “Food & housing | $5,324 | $10,648 | $15,972 | $21,296”
  - column:Transportation: 319 ⟵ “Transportation | $319 | $638 | $957 | $1,276”
  - column:Personal: 762 ⟵ “Personal | $762 | $1,524 | $2,286 | $3,048”
  - column:Total expenses: 8871 ⟵ “Total expenses | $8,871 | $17,742 | $26,613 | $35,484”
  - column:Tuition & fees: 3740 ⟵ “Tuition & fees | $1,870 | $3,740 | $5,610 | $7,480”
  - column:Books & supplies: 1192 ⟵ “Books & supplies | $596 | $1,192 | $1,788 | $2,384”
  - column:Food & housing: 10648 ⟵ “Food & housing | $5,324 | $10,648 | $15,972 | $21,296”
  - column:Transportation: 638 ⟵ “Transportation | $319 | $638 | $957 | $1,276”
  - column:Personal: 1524 ⟵ “Personal | $762 | $1,524 | $2,286 | $3,048”
  - column:Total expenses: 17742 ⟵ “Total expenses | $8,871 | $17,742 | $26,613 | $35,484”
  - column:Tuition & fees: 5610 ⟵ “Tuition & fees | $1,870 | $3,740 | $5,610 | $7,480”
  - column:Books & supplies: 1788 ⟵ “Books & supplies | $596 | $1,192 | $1,788 | $2,384”
  - column:Food & housing: 15972 ⟵ “Food & housing | $5,324 | $10,648 | $15,972 | $21,296”
  - column:Transportation: 957 ⟵ “Transportation | $319 | $638 | $957 | $1,276”
  - column:Personal: 2286 ⟵ “Personal | $762 | $1,524 | $2,286 | $3,048”
  - column:Total expenses: 26613 ⟵ “Total expenses | $8,871 | $17,742 | $26,613 | $35,484”
  - column:Tuition & fees: 7480 ⟵ “Tuition & fees | $1,870 | $3,740 | $5,610 | $7,480”
  - column:Books & supplies: 2384 ⟵ “Books & supplies | $596 | $1,192 | $1,788 | $2,384”
  - column:Food & housing: 21296 ⟵ “Food & housing | $5,324 | $10,648 | $15,972 | $21,296”
  - column:Transportation: 1276 ⟵ “Transportation | $319 | $638 | $957 | $1,276”
  - column:Personal: 3048 ⟵ “Personal | $762 | $1,524 | $2,286 | $3,048”
  - column:Total expenses: 35484 ⟵ “Total expenses | $8,871 | $17,742 | $26,613 | $35,484”
### `50cc396d2dc61239` Portland Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.pcc.edu/international-students/admissions/required-documents/ (sha256 3becff22c1e9)
- issues: conflicting_sources:https://www.pcc.edu/enroll/paying-for-college/financial-aid/review-award/cost-of-attendance/,https://www.pcc.edu/international-students/student-resources/tuition-financial/
- checks: {"columns": 1, "rows": 6}
  - column:Tuition*: 13410 ⟵ “Tuition* | $13,410”
  - column:Class and activity fees*: 567 ⟵ “Class and activity fees* | $567”
  - column:Medical insurance**: 2960 ⟵ “Medical insurance** | $2,960”
  - column:Food and lodging PCC does not provide housing. More info: 15453 ⟵ “Food and lodging PCC does not provide housing. More info | $15,453”
  - column:Books and supplies: 1700 ⟵ “Books and supplies | $1,700”
  - column:Transportation: 910 ⟵ “Transportation | $910”
### `69c9984d1eed41b0` Portland Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.pcc.edu/international-students/student-resources/tuition-financial/ (sha256 33d17d632af7)
- issues: conflicting_sources:https://www.pcc.edu/enroll/paying-for-college/financial-aid/review-award/cost-of-attendance/,https://www.pcc.edu/international-students/admissions/required-documents/
- checks: {"columns": 1, "rows": 5}
  - column:Tuition*: 13410 ⟵ “Tuition* | $13,410”
  - column:Medical Insurance**: 2960 ⟵ “Medical Insurance** | $2,960”
  - column:Food and Housing PCC does not provide house. More information: 15453 ⟵ “Food and Housing PCC does not provide house. More information | $15,453”
  - column:Books and Supplies: 1700 ⟵ “Books and Supplies | $1,700”
  - column:Transportation: 910 ⟵ “Transportation | $910”
### `m89feec56beef9f3` Portland Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.pcc.edu/university-transfer/transfer-agreements/psu/ (sha256 ff5ed3fbb969)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “A grade of C- or better must be earned in order for a class to transfer.”
  - min_grade: B ⟵ “To be eligible for transfer to PSU as part of this agreement, a grade of B or higher must be earned in all courses used toward the Physical Activity/Exercise All other courses must have a grade of at least a C or above. (See Credit Transfer Guide).”
### `250dd373e6ce6aef` Reed College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html (sha256 4efbcbe29aa1)
- issues: semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html,https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Reconsideration Requests See our guidelines for requesting a special circumstances review.”
### `2ea565557d7c6d95` Reed College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html (sha256 1d82e675707b)
- issues: semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html,https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Reconsideration Requests Guidelines for requesting a special circumstances review.”
### `7ad47fe6ba8bde7b` Reed College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html (sha256 94b650f62d2b)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html,https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Separation or divorce after the current financial aid applications are filed Death of a parent Non-discretionary expenses, such as: Unreimbursed medical expenses not already accounted for in the need analysis formulas If any of these special circumstances apply to you or your family, you may download and complete one of the forms below, as applicable, for the corresponding aid year for which you a”
### `ac809274f717db58` Reed College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html (sha256 94b650f62d2b)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Budget Adjustment Requests Federal regulations govern the items that may be included in the cost of attendance (budget).”
  - sentence: budget_increase ⟵ “Allowable budget increases are typically funded with additional student loan funds or Parent PLUS loans.”
### `df7dae4abe7492c8` Reed College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html (sha256 16825df1ab3f)
- issues: semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html,https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples may include a death in the family, student injury or illness, or other special circumstances include an explanation of the special, unusual, or extenuating circumstances causing undue hardship that prevented you from making SAP. include an explanation of what has changed in your situation that would allow you to demonstrate SAP by the end of the next semester.”
### `e3a7a8689bea4a44` Reed College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.reed.edu/admission-aid/how-to-apply/special-circumstances.html (sha256 36ad40c7f637)
- issues: semantic_review_required, conflicting_sources:https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/apply-for-financial-aid.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current-students/eligibility.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/current.html,https://www.reed.edu/admission-aid/costs-and-financial-aid/financial-aid/requestsforreconsideration.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances - Admission & Aid - Reed College Skip to site navigation.”
### `570ba43f8a912e3e` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.socc.edu/wp-content/uploads/2026/06/SWOCC-2026-27-Satisfactory-Academic-Progress-SAP-Appeal.pdf (sha256 286f588ddc4f)
- issues: semantic_review_required, conflicting_sources:https://www.socc.edu/get-started/pay-for-college/financial-aid/,https://www.socc.edu/get-started/pay-for-college/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “2026-2027 Satisfactory Academic Progress (SAP) Appeal Student Information Student’s Last Name Student’s First Name Student’s M.I.”
  - sentence: sap_appeal ⟵ “Email: -fao@socc.edu Fax: (541) 888-7492 Page 1 | 6 2026-2027 Satisfactory Academic Progress (SAP) Appeal Writing The Appeal Submit your appeal as soon as possible once you become aware of your status change.”
  - sentence: sap_appeal ⟵ “Email: -fao@socc.edu Fax: (541) 888-7492 Page 2 | 6 2026-2027 Satisfactory Academic Progress (SAP) Appeal Completing The Appeal Please indicate the term and year for which you would like to have your financial aid reinstated: □ Summer 2025_____ □ Fall 2025 ________ □ Winter 2026 _______ □ Spring 2026 _______ Use additional paper, if needed, when answering questions. • You will only be granted two ”
  - sentence: sap_appeal ⟵ “Page 3 | 6 Email: -fao@socc.edu Fax: (541) 888-7492 2026-2027 Satisfactory Academic Progress (SAP) Appeal Include a detailed personal statement (refer to page 2 for details).”
  - sentence: sap_appeal ⟵ “Email: -fao@socc.edu Fax: (541) 888-7492 Page 4 | 6 2026-2027 Satisfactory Academic Progress (SAP) Appeal APPEAL DEADLINES The complete appeal package should include this form, your personal statement and supporting documentation.”
  - sentence: sap_appeal ⟵ “Email: -fao@socc.edu Fax: (541) 888-7492 Page 5 | 6 2026-2027 Satisfactory Academic Progress (SAP) Appeal Statement of Understanding I understand that decisions on appeals are processed on a case-by-case basis.”
### `608bf9643edf9728` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 059e1f8f164e)
- issues: semantic_review_required, conflicting_sources:https://www.socc.edu/get-started/pay-for-college/financial-aid/,https://www.socc.edu/wp-content/uploads/2026/06/SWOCC-2026-27-Satisfactory-Academic-Progress-SAP-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Success Plan If you are placed on suspension and successfully appeal the decision, but your academic situation is such that it would be mathematically impossible for you to regain satisfactory academic progress eligibility during the next semester as required by federal satisfactory academic progress guidelines, the Financial Aid office may, at its sole”
  - sentence: sap_appeal ⟵ “If the "incomplete" grade results in your being placed on financial aid probation or suspension, once completed, you may appeal for a re-evaluation of Satisfactory Academic Progress by submitting the Satisfactory Academic Progress appeal form to the Financial Aid Office at Southwestern Oregon.”
  - sentence: sap_appeal ⟵ “Federal Work-Study Students If you participate in the Federal Work-Study program, are suspended from financial aid due to satisfactory academic progress or maximum timeframe, and your appeal has been denied, you will be ineligible for financial aid and cannot continue working until satisfactory academic progress is re-established.”
### `7c31ea1dbab6f911` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 0246c19e834f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “You are required to have earned academic credit during the award year in which you received Pell Grant or Federal Direct Loan funds at each previously attended institution. · Reconsideration Request Appeal Southwestern Oregon’s Financial Aid office may take your special circumstances into account to make adjustments to your Student Aid Index (SAI) for educational expenses, standard budget, and fin”
  - sentence: need_based_special_circumstances ⟵ “You must have very unusual circumstances to warrant a second appeal.”
### `a12068dcd051a25c` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 059e1f8f164e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The adjustments for a Reconsideration Request Appeal only affect need-based aid. · Dependency Override Appeal A dependency override occurs when a financial aid administrator exercises professional judgment and overrides the Department of Education’s criteria for dependent students.”
### `f245e1ff17f3bd05` Southwestern Oregon Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 0246c19e834f)
- issues: semantic_review_required, conflicting_sources:https://www.socc.edu/get-started/pay-for-college/financial-aid/,https://www.socc.edu/wp-content/uploads/2026/06/SWOCC-2026-27-Satisfactory-Academic-Progress-SAP-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Success Plan If you are placed on suspension and successfully appeal the decision, but your academic situation is such that it would be mathematically impossible for you to regain satisfactory academic progress eligibility during the next semester as required by federal satisfactory academic progress guidelines, the Financial Aid office may, at its sole”
  - sentence: sap_appeal ⟵ “If the "incomplete" grade results in your being placed on financial aid probation or suspension, once completed, you may appeal for a re-evaluation of Satisfactory Academic Progress by submitting the Satisfactory Academic Progress appeal form to the Financial Aid Office at Southwestern Oregon.”
  - sentence: sap_appeal ⟵ “Federal Work-Study Students If you participate in the Federal Work-Study program, are suspended from financial aid due to satisfactory academic progress or maximum timeframe, and your appeal has been denied, you will be ineligible for financial aid and cannot continue working until satisfactory academic progress is re-established.”
### `82552286f30ab3be` Southwestern Oregon Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.socc.edu/get-started/pay-for-college/financial-aid/ (sha256 059e1f8f164e)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 5, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - with_parents_or_family:Books, Course Materials, Supplies and Equipment: 1500 ⟵ “Books, Course Materials, Supplies and Equipment | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - with_parents_or_family:Food and Housing: 7695 ⟵ “Food and Housing | $7,695 | $7,977 | $10,977 | $11,622 | $10,221”
  - with_parents_or_family:Misc. Personal Expenses: 1535 ⟵ “Misc. Personal Expenses | $1,535 | $1,535 | $1,535 | $1,535 | $1,535”
  - with_parents_or_family:Transportation Expenses: 1705 ⟵ “Transportation Expenses | $1,705 | $1,705 | $1,705 | $1,240 | $1,240”
  - with_parents_or_family:Total Cost of Attendance: 20160 ⟵ “Total Cost of Attendance | $20,160 | $20,442 | $23,442 | $23,622 | $22,221”
  - column:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - column:Books, Course Materials, Supplies and Equipment: 1500 ⟵ “Books, Course Materials, Supplies and Equipment | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - column:Food and Housing: 7977 ⟵ “Food and Housing | $7,695 | $7,977 | $10,977 | $11,622 | $10,221”
  - column:Misc. Personal Expenses: 1535 ⟵ “Misc. Personal Expenses | $1,535 | $1,535 | $1,535 | $1,535 | $1,535”
  - column:Transportation Expenses: 1705 ⟵ “Transportation Expenses | $1,705 | $1,705 | $1,705 | $1,240 | $1,240”
  - column:Total Cost of Attendance: 20442 ⟵ “Total Cost of Attendance | $20,160 | $20,442 | $23,442 | $23,622 | $22,221”
  - column:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - column:Books, Course Materials, Supplies and Equipment: 1500 ⟵ “Books, Course Materials, Supplies and Equipment | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - column:Food and Housing: 10977 ⟵ “Food and Housing | $7,695 | $7,977 | $10,977 | $11,622 | $10,221”
  - column:Misc. Personal Expenses: 1535 ⟵ “Misc. Personal Expenses | $1,535 | $1,535 | $1,535 | $1,535 | $1,535”
  - column:Transportation Expenses: 1705 ⟵ “Transportation Expenses | $1,705 | $1,705 | $1,705 | $1,240 | $1,240”
  - column:Total Cost of Attendance: 23442 ⟵ “Total Cost of Attendance | $20,160 | $20,442 | $23,442 | $23,622 | $22,221”
  - column:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - column:Books, Course Materials, Supplies and Equipment: 1500 ⟵ “Books, Course Materials, Supplies and Equipment | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - column:Food and Housing: 11622 ⟵ “Food and Housing | $7,695 | $7,977 | $10,977 | $11,622 | $10,221”
  - column:Misc. Personal Expenses: 1535 ⟵ “Misc. Personal Expenses | $1,535 | $1,535 | $1,535 | $1,535 | $1,535”
  - column:Transportation Expenses: 1240 ⟵ “Transportation Expenses | $1,705 | $1,705 | $1,705 | $1,240 | $1,240”
  - column:Total Cost of Attendance: 23622 ⟵ “Total Cost of Attendance | $20,160 | $20,442 | $23,442 | $23,622 | $22,221”
  - column:Tuition and Fees: 7725 ⟵ “Tuition and Fees | $7,725 | $7,725 | $7,725 | $7,725 | $7,725”
  - … 5 more rows
### `ecdb3e2af1a413fc` Southwestern Oregon Community College — degree_requirements 2026-27 · program_key=oregon-transfer-module-otm · requirement_key=writing [new] (labeled_in_source)
- source: https://ecatalog.socc.edu/programsaz/oregon-transfer-module-otm/ (sha256 02f2254419cb)
- issues: course_alternatives_in_rule_text
  - courses: WR 121Z ⟵ “WR 121Z - Composition I (has corequisite of WR121A)”
  - courses: WR 122Z ⟵ “WR 122Z - Composition II”
### `1433ca05fd80591b` Tillamook Bay Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/ (sha256 afc858298cbd)
- issues: semantic_review_required, conflicting_sources:https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/appeal-process/,https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/determining-satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students will receive notification via TBCC email within 2-4 weeks of appeal submission with one of the following results: Reinstatement on probation Reinstatement on an academic plan with requirements Denial of financial aid Probation Probation is granted upon the approval of a financial aid Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Probation with an Academic Plan Probation with an Academic Plan is granted upon the approval of a Satisfactory Academic Progress Appeal with the condition the student follows an academic plan.”
### `21edeeb5c2323fc1` Tillamook Bay Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/appeal-process/ (sha256 05f3a7c31534)
- issues: semantic_review_required, conflicting_sources:https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/,https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/determining-satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students will receive notification via TBCC email within 2-4 weeks of appeal submission with one of the following results: Reinstatement on probation Reinstatement on an academic plan with requirements Denial of financial aid Probation Probation is granted upon the approval of a financial aid Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Probation with an Academic Plan Probation with an Academic Plan is granted upon the approval of a Satisfactory Academic Progress Appeal with the condition the student follows an academic plan.”
### `c38d993236662f15` Tillamook Bay Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://tillamookbaycc.edu/wp-content/uploads/2025/11/25-26_SAP_Appeal.pdf (sha256 09b5be4a1e51)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “2025-2026 Satisfactory Academic Progress Appeal Please complete this form using blue or black ink Student Name: _________________________________________ ___________________ Last Name First Name/MI Student ID# Address: _____________________________________________ Phone: __________________ Street Address Apt # ______________________________________________________________________ City State Zip Co”
### `e92fa59571c5703d` Tillamook Bay Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/determining-satisfactory-academic-progress/ (sha256 3470cdc81c32)
- issues: semantic_review_required, conflicting_sources:https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/,https://tillamookbaycc.edu/financial-aid-cost/financial-aid/satisfactory-academic-progress/appeal-process/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Process Students may request financial aid reinstatement by completing a Satisfactory Academic Progress Appeal form.”
### `c85d3fcd718db39a` Treasure Valley Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.tvcc.cc/admissions/international_students.cfm (sha256 6ab90709dd0a)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - column:Tuition and Fees*: 12000 ⟵ “Tuition and Fees* | $12,000”
  - column:Books and Supplies: 1500 ⟵ “Books and Supplies | $1,500”
  - column:Personal Expenditures: 1000 ⟵ “Personal Expenditures | $1,000”
  - column:International Student Insurance: 1000 ⟵ “International Student Insurance | $1,000”
  - column:Total Expenses: 24058 ⟵ “Total Expenses | $24,058”
### `23d41a50aaf4ac4e` Umpqua Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://umpqua.edu/become-a-student/financial-aid/ (sha256 301c2711d1c6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Visit ECMC Solutions Special Circumstances Has your family’s financial situation faced an extenuating loss in income compared to what was reported on the FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Request using 2025 income Special Circumstance Request using 2026 income Helpful Links Financial Aid Forms Ask Us Financial Aid Resources FAFSA Resources Financial Wellness Consumer Information Online Drop Box Physical Drop Box FAQ Financial Aid Handbook Loan Facts HEERF Cohort Default Rate Contact Office of Financial Aid 541-440-4602 541-440-4612 financialaid@umpqua.edu 8 a.m”
### `dcd8b5375a0cae20` Umpqua Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://umpqua.edu/become-a-student/cost-of-attendance/ (sha256 e11d148d73b1)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "rows": 6}
  - column:Tuition and Fees: 7077 ⟵ “Tuition and Fees | $7,077 | $7,077”
  - column:Textbooks and Supplies: 1956 ⟵ “Textbooks and Supplies | $1,956 | $1,956”
  - column:Housing and Food: 8955 ⟵ “Housing and Food | $8,955 | $12,726”
  - column:Transportation: 2430 ⟵ “Transportation | $2,430 | $2,430”
  - column:Miscellaneous/Personal: 1740 ⟵ “Miscellaneous/Personal | $1,740 | $1,740”
  - column:Loan Fees*: 50 ⟵ “Loan Fees* | $50 | $50”
  - column:Tuition and Fees: 7077 ⟵ “Tuition and Fees | $7,077 | $7,077”
  - column:Textbooks and Supplies: 1956 ⟵ “Textbooks and Supplies | $1,956 | $1,956”
  - column:Housing and Food: 12726 ⟵ “Housing and Food | $8,955 | $12,726”
  - column:Transportation: 2430 ⟵ “Transportation | $2,430 | $2,430”
  - column:Miscellaneous/Personal: 1740 ⟵ “Miscellaneous/Personal | $1,740 | $1,740”
  - column:Loan Fees*: 50 ⟵ “Loan Fees* | $50 | $50”
### `3ade018dc8d1b744` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/ (sha256 8db817396a6a)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Our evaluation of transfer applications is largely focused on determining if students meet our minimum admission requirements through cumulative GPA and coursework, though we also consider additional factors including special circumstances statements, application materials, grade trends, and academic potential for success.”
  - sentence: need_based_special_circumstances ⟵ “For applicants who do not meet our minimum requirements, we ask that you provide a personal statement (either included in the Special Circumstances portion of your application or uploaded in your UO application status portal) to share how/why you do not meet this requirement, and we will consider this information as part of our evaluation.”
  - sentence: need_based_special_circumstances ⟵ “We encourage transfers to share any relevant information or context if your academic performance was affected by special circumstances like serious illness or documented disability, or to otherwise provide us with information that we would not otherwise gather from your application materials.”
### `3b567ac453c57994` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/ (sha256 49f7b77528b0)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Our evaluation of transfer applications is largely focused on determining if students meet our minimum admission requirements through cumulative GPA and coursework, though we also consider additional factors including special circumstances statements, application materials, grade trends, and academic potential for success.”
  - sentence: need_based_special_circumstances ⟵ “For applicants who do not meet our minimum requirements, we ask that you provide a personal statement (either included in the Special Circumstances portion of your application or uploaded in your UO application status portal) to share how/why you do not meet this requirement, and we will consider this information as part of our evaluation.”
  - sentence: need_based_special_circumstances ⟵ “We encourage transfers to share any relevant information or context if your academic performance was affected by special circumstances like serious illness or documented disability, or to otherwise provide us with information that we would not otherwise gather from your application materials.”
### `925b276649d8e177` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/appeals (sha256 67ca02b93d00)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “In cases that impact federal student aid, HEA Sec. 479(a) authorizes the financial aid administrator to make adjustments on a case-by-case basis to the cost of attendance or the values of the data items required to calculate the student aid index to allow for treatment of special circumstances of an individual eligible applicant.”
### `a1b27cf191179ec7` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/satisfactory_academic_progress (sha256 a45f6aa74736)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uoregon.edu/appeals
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Petitions to cancel disqualification and to be reinstated academically to the University are completely separate processes from a SAP appeal.”
  - sentence: sap_appeal ⟵ “If your disqualification is cancelled or if you are reinstated academically and not meeting SAP requirements, you will still need to separately complete a SAP appeal for consideration of reinstating your financial aid.”
  - sentence: sap_appeal ⟵ “Additionally, we are unable to retroactively review a SAP appeal once a term is complete.”
  - sentence: sap_appeal ⟵ “Appeal Process If you are not making satisfactory academic progress, you will receive a notification at your UO e-mail address.”
  - sentence: sap_appeal ⟵ “We recommend submitting your SAP appeal as soon as possible, preferably well before the term begins; in order to give us time to review, process, and notify you of the decision.”
  - sentence: sap_appeal ⟵ “We are unable to retroactively review a SAP appeal once a term is complete.”
### `c8e8c22a579e2734` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/satisfactory_academic_progress (sha256 a45f6aa74736)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You are allowed to submit an appeal if you have mitigating circumstances, such as: a death of a relative, an injury or illness, or other special circumstances.”
### `d1ffbbe449e5dc16` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/ (sha256 db0b638e6e3f)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Personal statements and letters of recommendation (optional): You may send a personal statement with your application to explain special circumstances in your life that have affected you or your education.”
### `e7c86d34558e3529` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/appeals (sha256 67ca02b93d00)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uoregon.edu/satisfactory_academic_progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Information and the appeal process regarding failure to meet Satisfactory Academic Progress standards can be found on this webpage.”
### `eae441e970fc60b7` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/aidscholarships/ (sha256 96f1781a11eb)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Forbearance may be granted for up to 12 months for reasons such as: experiencing financial difficulties, such as medical expenses or change in income serving in AmeriCorps performing service that would qualify for partial loan forgiveness through the Department of Defense working in a medical or dental internship or residency program having student loan payments that are high in relation to your i”
### `0f31b35d7c3f2904` University of Portland — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/deadlines/index.html (sha256 3ca900e4fb0e)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.up.edu/admissions-aid/office-of-financial-aid/apply/special-circumstance.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The Department of Education does not permit processing special circumstance appeals past the period of enrollment.”
  - sentence: need_based_special_circumstances ⟵ “The Department of Education does not permit processing special circumstance appeals past the period of enrollment.”
### `4fc488cfeae70056` University of Portland — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/deadlines/index.html (sha256 3ca900e4fb0e)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The final deadline to submit loan applications and/or changes for the summer semester is 7 business days before your last scheduled summer class | April 24, 2026 | Deadline for Financial Aid Satisfactory Academic Progress appeals for summer semester | May 11, 2026 | Summer semester tuition due | May 18, 2026 Fall 2027 + Spring 2028 The 2027-2028 academic year includes summer 2027, fall 2027, and s”
  - sentence: sap_appeal ⟵ “The final deadline to submit loan applications and/or changes for the summer semester is 7 business days before your last scheduled summer class | April 23, 2027 | Summer semester tuition due | May 7, 2027 | Deadline for Financial Aid Satisfactory Academic Progress appeals for summer semester | May 10, 2027 Questions?”
### `7647aae25937a6b8` University of Portland — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/apply/special-circumstance.html (sha256 cf8ebc29d97c)
- issues: semantic_review_required, conflicting_sources:https://www.up.edu/admissions-aid/office-of-financial-aid/deadlines/index.html
- checks: {"negative_sentences": 0, "sentences": 14}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the Cost of Attendance or in the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation, more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal Special Circumstance Appeals will be considered after you receive your initial award notification for the current aid year.”
  - sentence: need_based_special_circumstances ⟵ “After reviewing your special circumstance documentation, your aid package may remain the same, be increased, or reduced according to the financial information that has been submitted.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance request does not guarantee an adjustment will be made to your aid package.”
### `8c817edda22cb126` University of Portland — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/apply/special-circumstance.html (sha256 cf8ebc29d97c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “A dependency override does not guarantee an adjustment will be made to your aid package.”
### `e4fbe2cdc9ff468c` University of Portland — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.up.edu/admissions-aid/office-of-financial-aid/costs/2526graduate-cost-of-attendance.html (sha256 da4e80483afb)
- issues: implausible_amount, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Professional Tuition (graduate level nursing, engineering, and business classes): 105 ⟵ “Professional Tuition (graduate level nursing, engineering, and business classes) | $105 | Credit”
  - column:Health Insurance: 1807 ⟵ “Health Insurance | $1,807 * | Semester”
### `43f1faa3cb52cb8b` Warner Pacific University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/wp-content/uploads/2025/01/2025-26-Cost-of-Attendance.pdf (sha256 3eccb3b2775b)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 2, "rows": 8}
  - column:Tuition and fees: 23500.0 ⟵ “Tuition and fees | $23,500.00 | $23,500.00”
  - column:Living Expenses: 14674.0 ⟵ “Living Expenses | $14,674.00 | $17,849.00”
  - column:& Equipment*: 58.0 ⟵ “& Equipment* | $58.00 | $58.00”
  - column:Miscellaneous Personal Expenses: 2377.0 ⟵ “Miscellaneous Personal Expenses | $2,377.00 | $2,377.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 41581.0 ⟵ “Total | $41,581.00 | $45,120.00”
  - column:Tuition and fees: 28860.0 ⟵ “Tuition and fees | $28,860.00 | $28,860.00”
  - column:Living Expenses: 14674.0 ⟵ “Living Expenses | $14,674.00 | $17,849.00”
  - column:& Equipment*: 58.0 ⟵ “& Equipment* | $58.00 | $58.00”
  - column:Miscellaneous Personal Expenses: 2377.0 ⟵ “Miscellaneous Personal Expenses | $2,377.00 | $2,377.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 46941.0 ⟵ “Total | $46,941.00 | $50,480.00”
  - column:Tuition and fees: 8160.0 ⟵ “Tuition and fees | $8,160.00 | $8,160.00”
  - column:Living Expenses: 15648.0 ⟵ “Living Expenses | $15,648.00 | $19,032.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 2544.0 ⟵ “Miscellaneous Personal Expenses | $2,544.00 | $2,544.00”
  - column:Federal Loan Fees: 132.0 ⟵ “Federal Loan Fees | $132.00 | $132.00”
  - column:Transportation: 960.0 ⟵ “Transportation | $960.00 | $1,296.00”
  - column:Total: 27564.0 ⟵ “Total | $27,564.00 | $31,284.00”
  - column:Tuition and fees: 15480.0 ⟵ “Tuition and fees | $15,480.00 | $15,480.00”
  - column:Living Expenses: 15648.0 ⟵ “Living Expenses | $15,648.00 | $19,032.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 2544.0 ⟵ “Miscellaneous Personal Expenses | $2,544.00 | $2,544.00”
  - … 38 more rows
### `63a313f743d1e9d8` Warner Pacific University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/wp-content/uploads/2025/12/2026-27-Cost-of-Attendance.pdf (sha256 780e28b2954b)
- issues: arrangement_unlabeled, multiple_total_rows, shared_site_attribution_review, conflicting_sources:https://www.warnerpacific.edu/admissions-aid/financial-aid/cost-of-attendance/
- checks: {"columns": 2, "rows": 8}
  - column:Tuition and fees: 24850.0 ⟵ “Tuition and fees | $24,850.00 | $24,850.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00 | $19,060.00”
  - column:& Equipment*: 70.0 ⟵ “& Equipment* | $70.00 | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00 | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 43390.0 ⟵ “Total | $43,390.00 | $47,146.00”
  - column:Tuition and fees: 30530.0 ⟵ “Tuition and fees | $30,530.00 | $30,530.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00 | $19,060.00”
  - column:& Equipment*: 70.0 ⟵ “& Equipment* | $70.00 | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00 | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 49070.0 ⟵ “Total | $49,070.00 | $52,826.00”
  - column:Tuition and fees: 14400.0 ⟵ “Tuition and fees | $14,400.00 | $14,400.00”
  - column:Living Expenses: 16704.0 ⟵ “Living Expenses | $16,704.00 | $20,328.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 1944.0 ⟵ “Miscellaneous Personal Expenses | $1,944.00 | $1,944.00”
  - column:Federal Loan Fees: 132.0 ⟵ “Federal Loan Fees | $132.00 | $132.00”
  - column:Transportation: 960.0 ⟵ “Transportation | $960.00 | $1,296.00”
  - column:Total: 34260.0 ⟵ “Total | $34,260.00 | $38,220.00”
  - column:Tuition and fees: 21840.0 ⟵ “Tuition and fees | $21,840.00”
  - column:Living Expenses: 20328.0 ⟵ “Living Expenses | $20,328.00”
  - column:Equipment*: 120.0 ⟵ “Equipment* | $120.00”
  - column:Miscellaneous Personal Expenses: 1944.0 ⟵ “Miscellaneous Personal Expenses | $1,944.00”
  - … 24 more rows
### `b55914932d9d9348` Warner Pacific University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/admissions-aid/financial-aid/cost-of-attendance/ (sha256 4fcf2beb2c2d)
- issues: shared_site_attribution_review, conflicting_sources:https://www.warnerpacific.edu/wp-content/uploads/2025/12/2026-27-Cost-of-Attendance.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and fees: 24850.0 ⟵ “Tuition and fees | $24,850.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00”
  - column:Books, Course Materials, Supplies & Equipment*: 70.0 ⟵ “Books, Course Materials, Supplies & Equipment* | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00”
  - column:Total: 43390.0 ⟵ “Total | $43,390.00”
### `m2c86ef937de539e` Warner Pacific University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.warnerpacific.edu/wp-content/uploads/2024/11/Columbia-Gorge-WPU-GE-Core-Transfer-Guide.pdf (sha256 729d506132d5)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"], "merged_pages": 8}
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
### `93273a111662d976` Warner Pacific University Professional and Graduate Studies — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/admissions-aid/financial-aid/cost-of-attendance/ (sha256 4fcf2beb2c2d)
- issues: shared_site_attribution_review, conflicting_sources:https://www.warnerpacific.edu/wp-content/uploads/2025/12/2026-27-Cost-of-Attendance.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and fees: 24850.0 ⟵ “Tuition and fees | $24,850.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00”
  - column:Books, Course Materials, Supplies & Equipment*: 70.0 ⟵ “Books, Course Materials, Supplies & Equipment* | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00”
  - column:Total: 43390.0 ⟵ “Total | $43,390.00”
### `a4f30b46895d351f` Warner Pacific University Professional and Graduate Studies — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/wp-content/uploads/2025/01/2025-26-Cost-of-Attendance.pdf (sha256 3eccb3b2775b)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 2, "rows": 8}
  - column:Tuition and fees: 23500.0 ⟵ “Tuition and fees | $23,500.00 | $23,500.00”
  - column:Living Expenses: 14674.0 ⟵ “Living Expenses | $14,674.00 | $17,849.00”
  - column:& Equipment*: 58.0 ⟵ “& Equipment* | $58.00 | $58.00”
  - column:Miscellaneous Personal Expenses: 2377.0 ⟵ “Miscellaneous Personal Expenses | $2,377.00 | $2,377.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 41581.0 ⟵ “Total | $41,581.00 | $45,120.00”
  - column:Tuition and fees: 28860.0 ⟵ “Tuition and fees | $28,860.00 | $28,860.00”
  - column:Living Expenses: 14674.0 ⟵ “Living Expenses | $14,674.00 | $17,849.00”
  - column:& Equipment*: 58.0 ⟵ “& Equipment* | $58.00 | $58.00”
  - column:Miscellaneous Personal Expenses: 2377.0 ⟵ “Miscellaneous Personal Expenses | $2,377.00 | $2,377.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 46941.0 ⟵ “Total | $46,941.00 | $50,480.00”
  - column:Tuition and fees: 8160.0 ⟵ “Tuition and fees | $8,160.00 | $8,160.00”
  - column:Living Expenses: 15648.0 ⟵ “Living Expenses | $15,648.00 | $19,032.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 2544.0 ⟵ “Miscellaneous Personal Expenses | $2,544.00 | $2,544.00”
  - column:Federal Loan Fees: 132.0 ⟵ “Federal Loan Fees | $132.00 | $132.00”
  - column:Transportation: 960.0 ⟵ “Transportation | $960.00 | $1,296.00”
  - column:Total: 27564.0 ⟵ “Total | $27,564.00 | $31,284.00”
  - column:Tuition and fees: 15480.0 ⟵ “Tuition and fees | $15,480.00 | $15,480.00”
  - column:Living Expenses: 15648.0 ⟵ “Living Expenses | $15,648.00 | $19,032.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 2544.0 ⟵ “Miscellaneous Personal Expenses | $2,544.00 | $2,544.00”
  - … 38 more rows
### `e49f4911176690dc` Warner Pacific University Professional and Graduate Studies — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.warnerpacific.edu/wp-content/uploads/2025/12/2026-27-Cost-of-Attendance.pdf (sha256 780e28b2954b)
- issues: arrangement_unlabeled, multiple_total_rows, shared_site_attribution_review, conflicting_sources:https://www.warnerpacific.edu/admissions-aid/financial-aid/cost-of-attendance/
- checks: {"columns": 2, "rows": 8}
  - column:Tuition and fees: 24850.0 ⟵ “Tuition and fees | $24,850.00 | $24,850.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00 | $19,060.00”
  - column:& Equipment*: 70.0 ⟵ “& Equipment* | $70.00 | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00 | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 43390.0 ⟵ “Total | $43,390.00 | $47,146.00”
  - column:Tuition and fees: 30530.0 ⟵ “Tuition and fees | $30,530.00 | $30,530.00”
  - column:Living Expenses: 15668.0 ⟵ “Living Expenses | $15,668.00 | $19,060.00”
  - column:& Equipment*: 70.0 ⟵ “& Equipment* | $70.00 | $70.00”
  - column:Miscellaneous Personal Expenses: 1830.0 ⟵ “Miscellaneous Personal Expenses | $1,830.00 | $1,830.00”
  - column:Federal Loan Fees: 72.0 ⟵ “Federal Loan Fees | $72.00 | $114.00”
  - column:Transportation: 900.0 ⟵ “Transportation | $900.00 | $1,222.00”
  - column:Total: 49070.0 ⟵ “Total | $49,070.00 | $52,826.00”
  - column:Tuition and fees: 14400.0 ⟵ “Tuition and fees | $14,400.00 | $14,400.00”
  - column:Living Expenses: 16704.0 ⟵ “Living Expenses | $16,704.00 | $20,328.00”
  - column:& Equipment*: 120.0 ⟵ “& Equipment* | $120.00 | $120.00”
  - column:Miscellaneous Personal Expenses: 1944.0 ⟵ “Miscellaneous Personal Expenses | $1,944.00 | $1,944.00”
  - column:Federal Loan Fees: 132.0 ⟵ “Federal Loan Fees | $132.00 | $132.00”
  - column:Transportation: 960.0 ⟵ “Transportation | $960.00 | $1,296.00”
  - column:Total: 34260.0 ⟵ “Total | $34,260.00 | $38,220.00”
  - column:Tuition and fees: 21840.0 ⟵ “Tuition and fees | $21,840.00”
  - column:Living Expenses: 20328.0 ⟵ “Living Expenses | $20,328.00”
  - column:Equipment*: 120.0 ⟵ “Equipment* | $120.00”
  - column:Miscellaneous Personal Expenses: 1944.0 ⟵ “Miscellaneous Personal Expenses | $1,944.00”
  - … 24 more rows
### `mb3ab929d5ef2aae` Warner Pacific University Professional and Graduate Studies — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.warnerpacific.edu/wp-content/uploads/2024/11/Columbia-Gorge-WPU-GE-Core-Transfer-Guide.pdf (sha256 729d506132d5)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"], "merged_pages": 8}
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
  - min_grade: C- ⟵ “General Education Core Course Transfer Equivalency Chart All core courses must be completed at the college level with a grade of C- or higher.”
### `7a9f38f08aab368d` Western Oregon University — appeals 2026-27 [new] (labeled_in_source)
- source: https://wou.edu/finaid/managing-my-aid/satisfactory-academic-progress/ (sha256 d285b81a7426)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If a SAP Appeal is requested it will also appear on your Home tab.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeals must be submitted by the census date each term to be considered for Financial Aid for that term.”
### `88c7ec87bf6a99e3` Western Oregon University — appeals 2024-25 [new] (labeled_in_title)
- source: https://cdn.wou.edu/finaid/files/2025/07/Financial-Aid-Eligibility-and-SAP-Policy-GR-rev-01.02.2025.pdf (sha256 911c80938c06)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “WOU Financial Aid Office Welcome Center 140, 345 Monmouth Ave N  Monmouth, OR 97361  Tel: 503-838-8475  Fax: 503-838-8200  wou.edu/finaid  finaid@wou.edu Satisfactory Academic Progress Appeal Process If you encounter circumstances that prevent you from making any of the SAP standards listed above, you may submit an appeal to our office.”
  - sentence: sap_appeal ⟵ “Your appeal should include: 1) The Satisfactory Academic Progress Appeal Form 2) Documentation of your circumstance (e.g. medical records). 3) For GPA (Qualitative) or Pace (Quantitative): For Excessive Credit Hours (Max.”
  - sentence: sap_appeal ⟵ “Submit a new SAP appeal detailing the extenuating circumstances that were beyond your control, and which interfered with your ability to academically perform.”
  - sentence: sap_appeal ⟵ “You will be notified of the outcome of your SAP appeal in writing via your WOU e-mail account.”
  - sentence: sap_appeal ⟵ “SAP Appeal Deadline SAP appeals must be submitted and approved two weeks prior to the start of the term for which you are requesting federal aid.”
### `ddb4e1f5e567338d` Western Oregon University — appeals 2025-26 [new] (labeled_in_source)
- source: https://cdn.wou.edu/finaid/files/2025/11/Financial-Aid-Eligibility-and-SAP-Policy-UG-rev-10.22.2025.pdf (sha256 466493864223)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “WOU Financial Aid Office Welcome Center 140, 345 Monmouth Ave N  Monmouth, OR 97361  Tel: 503-838-8475  wou.edu/finaid  finaid@wou.edu Satisfactory Academic Progress Appeal Process If you fail to make SAP, you may submit the Satisfactory Academic Progress Appeal Form and supporting documents to the Financial Aid Office to be considered for additional aid eligibility.”
  - sentence: sap_appeal ⟵ “SAP Appeal forms with complete documentation must be received by Census Date (second Friday each term).”
  - sentence: sap_appeal ⟵ “Appeals received after Census Date will not be considered until the following term (after grades post), and aid will not be paid retroactively upon review of your SAP Appeal.”
  - sentence: sap_appeal ⟵ “You will be notified of the outcome of your SAP appeal in writing via your WOU email account.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeal Form 2.”
### `5a0d270bc8170b26` Western Oregon University — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 67800cbdde7d)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition: 36640 ⟵ “Tuition | $27,480 | $36,640 | $36,640”
  - column:Fees: 1472 ⟵ “Fees | $1,110 | $1,472 | $1,472”
  - column:Loan Origination Fees: 2232 ⟵ “Loan Origination Fees | $1,164 | $2,232 | $2,232”
  - column:Housing: 10408 ⟵ “Housing | $7,806 | $10,408 | $10,408”
  - column:Food: 10956 ⟵ “Food | $8,217 | $10,956 | $10,956”
  - column:Books & Supplies: 300 ⟵ “Books & Supplies | $1,200 | $1,000 | $300”
  - column:Transportation: 1916 ⟵ “Transportation | $1,437 | $1,916 | $1,916”
  - column:Miscellaneous: 3000 ⟵ “Miscellaneous | $2,250 | $3,000 | $3,000”
  - column:Clinical Expenses: 1750 ⟵ “Clinical Expenses | $1,750 | $100 | $1,750”
  - column:Total: 68674 ⟵ “Total | $52,414 | $67,724 | $68,674”
### `7cb8310193cdb14c` Western Oregon University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 67800cbdde7d)
- issues: residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 15525 ⟵ “Tuition | $15,525 | $15,525 | $15,525”
  - on_campus:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - on_campus:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - on_campus:Housing: 7597 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - on_campus:Food: 5387 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - on_campus:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - on_campus:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - on_campus:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - on_campus:Total: 35829 ⟵ “Total | $35,829 | $38,867 | $27,587”
  - off_campus_not_with_family:Tuition: 15525 ⟵ “Tuition | $15,525 | $15,525 | $15,525”
  - off_campus_not_with_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - off_campus_not_with_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - off_campus_not_with_family:Housing: 7805 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - off_campus_not_with_family:Food: 8217 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - off_campus_not_with_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - off_campus_not_with_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - off_campus_not_with_family:Miscellaneous: 2250 ⟵ “Miscellaneous | $2,250 | $2,250 | $2,250”
  - off_campus_not_with_family:Total: 38867 ⟵ “Total | $35,829 | $38,867 | $27,587”
  - with_parents_or_family:Tuition: 15525 ⟵ “Tuition | $15,525 | $15,525 | $15,525”
  - with_parents_or_family:Mandatory Fees: 2283 ⟵ “Mandatory Fees | $2,283 | $2,283 | $2,283”
  - with_parents_or_family:Loan Origination Fees: 78 ⟵ “Loan Origination Fees | $78 | $78 | $78”
  - with_parents_or_family:Housing: 2501 ⟵ “Housing | $7,597 | $7,805 | $2,501”
  - with_parents_or_family:Food: 2241 ⟵ “Food | $5,387 | $8,217 | $2,241”
  - with_parents_or_family:Books & Supplies: 1272 ⟵ “Books & Supplies | $1,272 | $1,272 | $1,272”
  - with_parents_or_family:Transportation: 1437 ⟵ “Transportation | $1,437 | $1,437 | $1,437”
  - … 2 more rows
### `c371e6f706129dcd` Western Oregon University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://wou.edu/finaid/tuition-fees/cost-of-attendance/ (sha256 67800cbdde7d)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition: 36640 ⟵ “Tuition | $27,480 | $36,640 | $36,640”
  - column:Fees: 1472 ⟵ “Fees | $1,110 | $1,472 | $1,472”
  - column:Loan Origination Fees: 2232 ⟵ “Loan Origination Fees | $1,164 | $2,232 | $2,232”
  - column:Housing: 10408 ⟵ “Housing | $7,806 | $10,408 | $10,408”
  - column:Food: 10956 ⟵ “Food | $8,217 | $10,956 | $10,956”
  - column:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,200 | $1,000 | $300”
  - column:Transportation: 1916 ⟵ “Transportation | $1,437 | $1,916 | $1,916”
  - column:Miscellaneous: 3000 ⟵ “Miscellaneous | $2,250 | $3,000 | $3,000”
  - column:Clinical Expenses: 100 ⟵ “Clinical Expenses | $1,750 | $100 | $1,750”
  - column:Total: 67724 ⟵ “Total | $52,414 | $67,724 | $68,674”
### `7dee7d2502e35879` Willamette University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://willamette.edu/cost-aid/tuition (sha256 a63d47dd4885)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "rows": 7}
  - column:Tuition: 28320 ⟵ “Tuition | $28,320 | Per semester”
  - column:Student Activity Fee1: 146 ⟵ “Student Activity Fee1 | $146 | Per semester”
  - column:Meal Plan – Living on campus (14-meal plan): 4270 ⟵ “Meal Plan – Living on campus (14-meal plan) | $4,270 | Per semester”
  - column:Housing – Living on campus3 (Standard double room): 4595 ⟵ “Housing – Living on campus3 (Standard double room) | $4,595 | Per semester”
  - column:Residence Hall Fee: 75 ⟵ “Residence Hall Fee | $75 | Per semester”
  - column:Sub-Total: 37406 ⟵ “Sub-Total | $37,406 | Per semester”
  - column:ANNUAL COST (2 semesters): 74812 ⟵ “ANNUAL COST (2 semesters) | $74,812 | Per Year”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 135; pages by category: admissions_tests 39, ap_credit 16, cost_of_attendance 5, degree_requirements 25, dual_enrollment 1, ib_credit 14, merit_scholarships 16, residency 3, statewide_articulation 30, transfer_credit 28, tuition_fees 3

## Blocked by the site (every request refused; needs the browser fallback)

- New Hope Christian College-Eugene (`ipeds-208725`)
- Mt Hood Community College (`ipeds-209250`)
- Rogue Community College (`ipeds-209940`)

## Leads: official pages found with no extracted record

- Blue Mountain Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Bushnell University: tuition_fees, cost_of_attendance, merit_scholarships, clep_credit, statewide_articulation, degree_requirements
- Central Oregon Community College: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, residency
- Chemeketa Community College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency
- Clackamas Community College: admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, residency
- Clatsop Community College: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Columbia Gorge Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Corban University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit
- Eastern Oregon University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- George Fox University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, degree_requirements
- Klamath Community College: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, degree_requirements
- Lane Community College: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit
- Lewis & Clark College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Linfield University: tuition_fees, cost_of_attendance, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Linn-Benton Community College: tuition_fees, merit_scholarships, degree_requirements
- Mount Angel Seminary: admissions_tests, degree_requirements
- Multnomah University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation
- Oregon Coast Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Oregon Institute of Technology: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Oregon State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency
- Oregon State University-Cascades Campus: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, residency
- Pacific Bible College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit
- Pacific Northwest College of Art: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
- Pacific University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Portland Community College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Portland State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency
- Reed College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Southern Oregon University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Southwestern Oregon Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit
- Tillamook Bay Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Treasure Valley Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, aid_appeals
- Umpqua Community College: cost_of_attendance, common_data_set, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Oregon: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency
- University of Portland: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment
- Warner Pacific University: merit_scholarships, aid_appeals
- Warner Pacific University Professional and Graduate Studies: merit_scholarships, aid_appeals
- Western Oregon University: admissions_tests, merit_scholarships, transfer_credit, residency
- Willamette University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
