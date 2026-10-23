# Review queue — TX (2026-27)

Pages fetched: 1530; failures: 131. Candidates: 173 (8 without issues, 165 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 18 | 2 | 1 | 4 | 10 | 0 | 129 |
| cost_of_attendance | 14 | 2 | 1 | 4 | 10 | 0 | 133 |
| admissions_tests | 3 | 0 | 0 | 0 | 16 | 1 | 144 |
| common_data_set | 3 | 0 | 0 | 0 | 0 | 17 | 144 |
| merit_scholarships | 10 | 7 | 0 | 0 | 17 | 0 | 130 |
| ap_credit | 5 | 13 | 0 | 4 | 4 | 9 | 129 |
| clep_credit | 4 | 16 | 0 | 5 | 2 | 8 | 129 |
| ib_credit | 3 | 8 | 0 | 3 | 2 | 11 | 137 |
| dual_enrollment | 4 | 15 | 1 | 0 | 12 | 4 | 128 |
| transfer_credit | 2 | 9 | 0 | 2 | 15 | 0 | 136 |
| statewide_articulation | 0 | 0 | 0 | 0 | 4 | 13 | 147 |
| residency | 0 | 0 | 0 | 0 | 16 | 1 | 147 |
| degree_requirements | 11 | 0 | 0 | 0 | 8 | 4 | 141 |
| aid_appeals | 0 | 0 | 0 | 16 | 0 | 1 | 147 |

## Ready for review (8)

### `7bd96a3f1733188f` Austin Community College District — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://students.austincc.edu/financial-aid/explore-your-financial-aid/cost-of-attendance/ (sha256 866954adc742)
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition and fees: 6540 ⟵ “Tuition and fees | $6,540 | $12,570 | $6,540 | $12,570”
  - off_campus_not_with_family:Housing and food: 18240 ⟵ “Housing and food | $18,240 | $18,240 | $8,800 | $8,800”
  - off_campus_not_with_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200 | $1,200 | $1,200”
  - off_campus_not_with_family:Transportation: 1824 ⟵ “Transportation | $1,824 | $1,824 | $1,824 | $1,824”
  - off_campus_not_with_family:Personal expenses: 3584 ⟵ “Personal expenses | $3,584 | $3,584 | $3,584 | $3,584”
  - off_campus_not_with_family:Total: 31388 ⟵ “Total | $31,388 | $37,418 | $21,948 | $27,978”
  - off_campus_not_with_family:Tuition and fees: 12570 ⟵ “Tuition and fees | $6,540 | $12,570 | $6,540 | $12,570”
  - off_campus_not_with_family:Housing and food: 18240 ⟵ “Housing and food | $18,240 | $18,240 | $8,800 | $8,800”
  - off_campus_not_with_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200 | $1,200 | $1,200”
  - off_campus_not_with_family:Transportation: 1824 ⟵ “Transportation | $1,824 | $1,824 | $1,824 | $1,824”
  - off_campus_not_with_family:Personal expenses: 3584 ⟵ “Personal expenses | $3,584 | $3,584 | $3,584 | $3,584”
  - off_campus_not_with_family:Total: 37418 ⟵ “Total | $31,388 | $37,418 | $21,948 | $27,978”
  - with_parents_or_family:Tuition and fees: 6540 ⟵ “Tuition and fees | $6,540 | $12,570 | $6,540 | $12,570”
  - with_parents_or_family:Housing and food: 8800 ⟵ “Housing and food | $18,240 | $18,240 | $8,800 | $8,800”
  - with_parents_or_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200 | $1,200 | $1,200”
  - with_parents_or_family:Transportation: 1824 ⟵ “Transportation | $1,824 | $1,824 | $1,824 | $1,824”
  - with_parents_or_family:Personal expenses: 3584 ⟵ “Personal expenses | $3,584 | $3,584 | $3,584 | $3,584”
  - with_parents_or_family:Total: 21948 ⟵ “Total | $31,388 | $37,418 | $21,948 | $27,978”
  - with_parents_or_family:Tuition and fees: 12570 ⟵ “Tuition and fees | $6,540 | $12,570 | $6,540 | $12,570”
  - with_parents_or_family:Housing and food: 8800 ⟵ “Housing and food | $18,240 | $18,240 | $8,800 | $8,800”
  - with_parents_or_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200 | $1,200 | $1,200”
  - with_parents_or_family:Transportation: 1824 ⟵ “Transportation | $1,824 | $1,824 | $1,824 | $1,824”
  - with_parents_or_family:Personal expenses: 3584 ⟵ “Personal expenses | $3,584 | $3,584 | $3,584 | $3,584”
  - with_parents_or_family:Total: 27978 ⟵ “Total | $31,388 | $37,418 | $21,948 | $27,978”
### `241277cefffb660d` Austin Community College District — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.austincc.edu/blog/2026/01/13/acc-credit-transfer-to-four-year-universities/ (sha256 5a75ec7c81ed)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “ACC students arrive at TWU with their health sciences and core prerequisites, and then complete the last 30 hours of their dental hygiene bachelor’s degree.”
### `8c573a28ec58d935` Lone Star College System — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.lonestar.edu/cost-of-attendance.htm (sha256 3a24426e250e)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition and Fees: 9390 ⟵ “Tuition and Fees | $3,330 | $7,470 | $9,390”
  - column:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96”
  - column:Books and Supplies*: 2450 ⟵ “Books and Supplies* | $2,450 | $2,450 | $2,450”
  - column:Food and Housing: 10960 ⟵ “Food and Housing | $10,960 | $10,960 | $10,960”
  - column:Transportation: 2510 ⟵ “Transportation | $1,510 | $1,510 | $2,510”
  - column:Personal / Misc: 4008 ⟵ “Personal / Misc | $4,008 | $4,008 | $4,008”
  - column:Professional Licensure Fee**: 410 ⟵ “Professional Licensure Fee** | $410 | $410 | $410”
  - column:TOTAL: 29824 ⟵ “TOTAL | $22,764 | $26,904 | $29,824”
### `ce0e3044e1f4ba86` Lone Star College System — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.lonestar.edu/college-departments/dualcredit/dualcredit-tuition.htm (sha256 b255410018f1)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 249 ⟵ “2 Out-of-District Texas Resident means an adult Texas resident living outside the College�s taxing district boundaries on the official enrollment reporting date. It can also mean a non-adult Texas resident whose parents or guardians live outside those boundaries on the official enrollment reporting ”
  - per_credit_hour_charge: 21 ⟵ “*Students participating in the STAR Bundle program for books and supplies will be charged $21 per credit hour.”
### `3cfbba2a6101f8af` Texas A & M University-College Station — credit_policies 2027-28 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.tamu.edu/undergraduate/general-information/admission/ (sha256 7b477134c2ce)
- checks: {"distinct_exams": 15, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS 206 | 3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus with Elementary Functions | 50 | MATH 151 or MATH 171 | 4”
  - equivalencies[CLEP-CHEMISTRY|45]:  ⟵ “Chemistry | 45 | CHEM 119 | 4”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT 209 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 | HIST 105 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present | 50 | HIST 106 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | EPSY 320 or PBSI 225 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 50 | ISTM 209 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics | 50 | ECON 203 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics | 50 | ECON 202 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | 50 | MATH 150 | 4”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | 50 | PBSI 107 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | 50 | SOCI 205 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | HIST 101 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present | 50 | HIST 102 | 3”
### `950eb84d53fe6dfa` The University of Texas Rio Grande Valley — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 35472 ⟵ “Tuition & Fees | 22,372 | 22,372 | 22,372 | 35,472 | 35,472 | 35,472”
  - with_parents_or_family:Living Expenses: 6857 ⟵ “Living Expenses | 6,857 | 14,711 | 18,102 | 6,857 | 14,711 | 18,102”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 6103 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,103 | 6,103 | 6,103 | 6,103 | 6,103 | 6,103”
  - with_parents_or_family:Transportation: 5173 ⟵ “Transportation | 5,173 | 3,131 | 5,173 | 5,173 | 3,131 | 5,173”
  - with_parents_or_family:Miscellaneous: 6160 ⟵ “Miscellaneous | 6,160 | 6,160 | 6,160 | 6,160 | 6,160 | 6,160”
  - with_parents_or_family:Health Insurance: 3707 ⟵ “Health Insurance | 3,707 | 3,707 | 3,707 | 3,707 | 3,707 | 3,707”
  - with_parents_or_family:Total Cost of Attendance: 63472 ⟵ “Total Cost of Attendance | 50,372 | 56,184 | 61,617 | 63,472 | 69,284 | 74,717”
  - on_campus:Tuition & Fees: 35472 ⟵ “Tuition & Fees | 22,372 | 22,372 | 22,372 | 35,472 | 35,472 | 35,472”
  - on_campus:Living Expenses: 14711 ⟵ “Living Expenses | 6,857 | 14,711 | 18,102 | 6,857 | 14,711 | 18,102”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 6103 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,103 | 6,103 | 6,103 | 6,103 | 6,103 | 6,103”
  - on_campus:Transportation: 3131 ⟵ “Transportation | 5,173 | 3,131 | 5,173 | 5,173 | 3,131 | 5,173”
  - on_campus:Miscellaneous: 6160 ⟵ “Miscellaneous | 6,160 | 6,160 | 6,160 | 6,160 | 6,160 | 6,160”
  - on_campus:Health Insurance: 3707 ⟵ “Health Insurance | 3,707 | 3,707 | 3,707 | 3,707 | 3,707 | 3,707”
  - on_campus:Total Cost of Attendance: 69284 ⟵ “Total Cost of Attendance | 50,372 | 56,184 | 61,617 | 63,472 | 69,284 | 74,717”
  - off_campus_not_with_family:Tuition & Fees: 35472 ⟵ “Tuition & Fees | 22,372 | 22,372 | 22,372 | 35,472 | 35,472 | 35,472”
  - off_campus_not_with_family:Living Expenses: 18102 ⟵ “Living Expenses | 6,857 | 14,711 | 18,102 | 6,857 | 14,711 | 18,102”
  - off_campus_not_with_family:Books, Course Materials, Supplies, & Equipment: 6103 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,103 | 6,103 | 6,103 | 6,103 | 6,103 | 6,103”
  - off_campus_not_with_family:Transportation: 5173 ⟵ “Transportation | 5,173 | 3,131 | 5,173 | 5,173 | 3,131 | 5,173”
  - off_campus_not_with_family:Miscellaneous: 6160 ⟵ “Miscellaneous | 6,160 | 6,160 | 6,160 | 6,160 | 6,160 | 6,160”
  - off_campus_not_with_family:Health Insurance: 3707 ⟵ “Health Insurance | 3,707 | 3,707 | 3,707 | 3,707 | 3,707 | 3,707”
  - off_campus_not_with_family:Total Cost of Attendance: 74717 ⟵ “Total Cost of Attendance | 50,372 | 56,184 | 61,617 | 63,472 | 69,284 | 74,717”
### `702540380276e6f9` The University of Texas at El Paso — credit_policies 2026-27 · policy_kind=IB [same] (source_unlabeled)
- source: https://www.utep.edu/admissions/_files/docs/credit-by-exam-ib.pdf (sha256 744ed7bf4284)
- checks: {"distinct_exams": 29, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|4]:  ⟵ “Biology (HL*)                                     4         8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business and Management                           4         3                  BUSN 3 hrs elective”
  - equivalencies[IB-CHEMISTRY-SL|4]:  ⟵ “Chemistry (SL)                                    4         8            CHEM 1407, CHEM 1408”
  - equivalencies[IB-CHEMISTRY-HL|4]:  ⟵ “Chemistry (HL)                                    4         8”
  - equivalencies[IB-COMPUTER-SCIENCE|4]:  ⟵ “Computer Science                                  4         3                            cs 1310”
  - equivalencies[IB-ECONOMICS-SL|4]:  ⟵ “Economics (SL)                                    4         3                         ECON 2303”
  - equivalencies[IB-ECONOMICS-HL|4]:  ⟵ “Economics (HL)                                    4         3            ECON 2303 , ECON 2304”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4]:  ⟵ “Environmental Systems                             4          4             ESCI 1301 , ESCI 1101”
  - equivalencies[IB-FILM|4]:  ⟵ “Film                                              4          3                        TH EA 1390”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography                                         4         3                         GEOG 1310”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History Africa                                    4         3                          HIST 23CR”
  - equivalencies[IB-HISTORY-SL|4]:  ⟵ “History Americas (SL)                             4         3                          HIST 1302”
  - equivalencies[IB-HISTORY-HL|4]:  ⟵ “History Americas (HL)                             4          6             HIST 1301 , HIST 1302”
  - equivalencies[IB-HISTORY-HL|5]:  ⟵ “History Americas (HL)                             5         9”
  - equivalencies[IB-LATIN-HL|4]:  ⟵ “Latin (HL)                              4   6      LATN 2304 , LATN 3301”
  - equivalencies[IB-FRENCH-SL|4]:  ⟵ “French Al or A2 (SL)                    4   12     FREN 2301 , FREN 2302”
  - equivalencies[IB-GERMAN-SL|4]:  ⟵ “German Al or A2 (SL)                    4   12”
  - equivalencies[IB-SPANISH-SL|4]:  ⟵ “Spanish Al or A2 (SL)                   4   12     SPAN 1301 , SPAN 1302”
  - equivalencies[IB-FRENCH-HL|4]:  ⟵ “French Al or A2 (HL)                    4   15     FREN 2301 , FREN 2302”
  - equivalencies[IB-FRENCH-SL|4]:  ⟵ “French B (SL)                           4   6     FREN 1301 , FREN 1302”
  - equivalencies[IB-FRENCH-HL|4]:  ⟵ “French B (HL)                           4   12”
  - equivalencies[IB-GERMAN-HL|4]:  ⟵ “German B (HL)                           4        GERM 1301, GERM 1302”
  - equivalencies[IB-SPANISH-HL|4]:  ⟵ “Spanish B (HL)                              4                     SPAN 1301 , SPAN 1302”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French AB                                  4               3                 FREN 1301”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German AB                                   4              3                GERM 1301”
  - … 7 more rows
### `ddc6b3ee1e0619d0` The University of Texas at El Paso — credit_policies 2026-27 · policy_kind=CLEP [same] (source_unlabeled)
- source: https://www.utep.edu/admissions/_files/docs/clep-examination.pdf (sha256 c4f6d08bdc7a)
- checks: {"distinct_exams": 33, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                                           50               3         ENGL 3 hrs elective”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature                         50               3         ENGL 3 hrs elective”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular                                    50             3*         RWS 1301”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                                             50             3          ENGL 3 hrs elective”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                                                     50             3          HUMN 3 hrs elective**”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language: Levels 1 and 2                               50               6         FREN 1301, FREN 1302”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language: Levels 1 and 2                               50               6         GERM 1301, GERM 1302”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language: Levels 1 and 2                              50               6         SPAN 1301, SPAN 1302”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing: Levels 1 and 2                          50               6         SPAN 1301, SPAN 1302”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                                           50               3         POLS 2310”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I                                50               3         HIST 1301**”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II                               50               3         HIST 1302**”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development                                  50               3         PSYC 2310”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology                        50               3         EDUC 2300”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                                       50               3         PSYC 1301”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                                        50               3         SOCI 1301”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                                  50               3         ECON 2303”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                                  50               3         ECON 2304”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History                                   50               3         No equivalent available”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648             50               3         HIST 3 hr elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present                  50               3         HIST 3 hr elective”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                                       50               6         BIOL 1305, BIOL 1306”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                                      50               4         MATH 1411”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                                                     50               3         CHEM 1305”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                                                50              3         MATH 1309 after Spring 2020”
  - … 9 more rows

## Exceptions (165)

### `520ff4c21614831d` Austin Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://students.austincc.edu/financial-aid/apply-for-financial-aid/family-contribution-appeal/ (sha256 60dedcdba5b9)
- issues: semantic_review_required, conflicting_sources:https://students.austincc.edu/financial-aid/apply-for-financial-aid/dependency-override-request/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “How to Request a SAI Appeal Follow these steps to submit a SAI Appeal (Special Circumstances Form): Complete the financial aid application steps for the current school year.”
### `9235238ab592ade9` Austin Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://students.austincc.edu/financial-aid/apply-for-financial-aid/dependency-override-request/ (sha256 aac26bb57678)
- issues: semantic_review_required, conflicting_sources:https://students.austincc.edu/financial-aid/apply-for-financial-aid/family-contribution-appeal/
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance Appeal | Financial Aid | Austin Community College District Select this link if you are using screen reading or another assistive technology before continuing to enable accessible content on this page.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance Appeal If you were required to provide your parent’s information on the FAFSA form but are unable to do so because of unusual circumstances, ACC may be able to waive the requirement of your parent’s information.”
  - sentence: need_based_special_circumstances ⟵ “The process to request this waiver is called the Unusual Circumstance Appeal (previously called a Dependency Override).”
  - sentence: need_based_special_circumstances ⟵ “Examples of Qualifying Unusual Circumstances An abusive family environment Parental abandonment or estrangement Incarceration or institutionalization of both parents Parents lacking physical or mental capacity This is not a complete list.”
  - sentence: need_based_special_circumstances ⟵ “If you believe you have unusual circumstances, contact a campus Financial Aid Office to discuss your eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Circumstances that Do Not Qualify as Unusual Parents do not support the student or refuse to contribute to the student’s education Parents are unwilling to provide information on the FAFSA or for verification Parents do not claim the student as a dependent for income tax purposes Student demonstrates total self-sufficiency If your Unusual Circumstance Request is denied, then you must e”
### `c28446337854d0bb` Austin Community College District — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://students.austincc.edu/financial-aid/explore-your-financial-aid/cost-of-attendance/ (sha256 866954adc742)
- issues: residency_unknown, conflicting_sources:https://admissions.austincc.edu/tuition-costs/payment-plans/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition and fees: 2550 ⟵ “Tuition and fees | $2,550 | $2,550”
  - off_campus_not_with_family:Housing and food: 18240 ⟵ “Housing and food | $18,240 | $8,800”
  - off_campus_not_with_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200”
  - off_campus_not_with_family:Transportation: 1824 ⟵ “Transportation | $1,824 | $1,824”
  - off_campus_not_with_family:Personal expenses: 3584 ⟵ “Personal expenses | $3,584 | $3,584”
  - off_campus_not_with_family:Total: 27398 ⟵ “Total | $27,398 | $17,958”
  - with_parents_or_family:Tuition and fees: 2550 ⟵ “Tuition and fees | $2,550 | $2,550”
  - with_parents_or_family:Housing and food: 8800 ⟵ “Housing and food | $18,240 | $8,800”
  - with_parents_or_family:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200”
  - with_parents_or_family:Transportation: 1824 ⟵ “Transportation | $1,824 | $1,824”
  - with_parents_or_family:Personal expenses: 3584 ⟵ “Personal expenses | $3,584 | $3,584”
  - with_parents_or_family:Total: 17958 ⟵ “Total | $27,398 | $17,958”
### `f78c9fcb7011ba13` Austin Community College District — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://admissions.austincc.edu/tuition-costs/payment-plans/ (sha256 6dd1b1b85508)
- issues: residency_unknown, conflicting_sources:https://students.austincc.edu/financial-aid/explore-your-financial-aid/cost-of-attendance/
- checks: {"columns": 1, "rows": 2}
  - column:Tuition charges: 1000.0 ⟵ “Tuition charges | 1,000.00”
  - column:Remaining balance: 800.0 ⟵ “Remaining balance | 800.00”
### `13d0c92af039b980` Collin County Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.collin.edu/financialaid/documents/SPECIAL%20CIRCUMSTANCES.pdf (sha256 45916a94ae63)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “Documentation can vary, but typically includes the Collin College Request for Dependency Override Form, a typed letter thoroughly explaining their current situation, plus independent documentation from two separate third parties, which may be a signed statement, or an official document such as a police report, to prove/support their particular circumstance.”
  - sentence: dependency_override ⟵ “Collin College does not accept dependency overrides made by another school.”
  - sentence: dependency_override ⟵ “All students requesting a dependency override must submit the required documentation to the FAO and be assessed at our institution.”
  - sentence: dependency_override ⟵ “STUDENTS WITHOUT PARENT SUPPORT Students whose parents refuse to support them are not eligible for a dependency override, but they may be able to receive unsubsidized Direct loans only.”
### `17f4646f8730d7c2` Collin County Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.collin.edu/financialaid/specialcircumstances (sha256 cfcce66ffdf9)
- issues: semantic_review_required, conflicting_sources:https://www.collin.edu/financialaid/,https://www.collin.edu/financialaid/documents/SPECIAL%20CIRCUMSTANCES.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Voting Information Financial Aid Special Circumstances Special Circumstances Changes Since Filing the FAFSA The last few years have surely been some of the strangest and most challenging that some of us have ever, or may ever see.”
  - sentence: need_based_special_circumstances ⟵ “Once you speak with a financial aid advisor and they determine that you may have a special circumstance, they will place a Special Circumstances form in your My Tasks section of your Workday.”
  - sentence: need_based_special_circumstances ⟵ “View information about other types of special circumstances you may be experiencing.”
### `744b269e566e6cb3` Collin County Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.collin.edu/financialaid/ (sha256 1520b204702c)
- issues: semantic_review_required, conflicting_sources:https://www.collin.edu/financialaid/documents/SPECIAL%20CIRCUMSTANCES.pdf,https://www.collin.edu/financialaid/specialcircumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Continuing Education Financial Aid Exemptions Federal Student Aid SB1528/TASFA Scholarships Special Circumstances Veterans Benefits Tools and Resources Financial aid can be confusing and scary, but we are here to help you navigate the process.”
### `7b8254ced6afad17` Collin County Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.collin.edu/financialaid/documents/SPECIAL%20CIRCUMSTANCES.pdf (sha256 45916a94ae63)
- issues: semantic_review_required, conflicting_sources:https://www.collin.edu/financialaid/,https://www.collin.edu/financialaid/specialcircumstances
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Documentation can vary, but typically includes the Collin College Request for Special Circumstances Form plus any supplemental data and/or documentation to prove/support their particular circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Suggested documentation is listed on the Request for Special Circumstances Form; however, the FAO will accept a variety of documentation provided it sufficiently proves/supports the student’s claim.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances may include, but are not limited to: • Loss of employment • Unusual, uncovered (out-of-pocket) medical/dental expenses paid* • Elementary or secondary school tuition for student’s siblings or dependents • Extraordinary dependent care expenses • Divorce • Death of a dependent student’s parent or independent student’s spouse *Above the IPA of 11% built into the EFC ”
  - sentence: need_based_special_circumstances ⟵ “UNUSUAL CIRCUMSTANCES - DEPENDENCY OVERRIDE The Financial Aid Office may process a dependency override on a case-by-case basis for students with unusual circumstances.”
### `adc9091ccefdbc8c` Collin County Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.collin.edu/financialaid/documents/SPECIAL%20CIRCUMSTANCES.pdf (sha256 45916a94ae63)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “SPECIAL CIRCUMSTANCES The Financial Aid Office may use professional judgement on a case-by-case basis to adjust the student’s COA or the data used to calculate the SAI (i.e., need analysis) for unusual or extenuating circumstance of the student and/or parent.”
  - sentence: professional_judgment ⟵ “For students flagged for verification, all verification requirements must be met before applying professional judgment.”
  - sentence: professional_judgment ⟵ “Professional judgment cannot be used to waive general student eligibility requirements or to circumvent the intent of the law or regulations.”
### `a310509f459772bf` Collin County Community College District — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.collin.edu/studentresources/testing/creditbyexam/clep (sha256 83149598433d)
- issues: rows_without_score, score_column_not_scores
- checks: {"distinct_exams": 24, "equivalencies": 31, "rows_without_score": 4}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|Minimum Score for Credit: 50]:  ⟵ “Financial Accounting | Collin Course Number: ACCT 2301 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|Minimum Score for Credit: 50]:  ⟵ “Introductory Business Law | Collin Course Number: BUSI 2301 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|Minimum Score for Credit: 50]:  ⟵ “Principles of Management | Collin Course Number: BMGT 1327 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|Minimum Score for Credit: 50]:  ⟵ “Principles of Marketing | Collin Course Number: MRKG 1311 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|Minimum Score for Credit: 50]:  ⟵ “Principles of Macroeconomics | Collin Course Number: ECON 2301 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|Minimum Score for Credit: 50]:  ⟵ “Principles of Microeconomics | Collin Course Number: ECON 2302 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | Composition & Literature”
  - equivalencies[CLEP-AMERICAN-LITERATURE|Minimum Score for Credit: 50]:  ⟵ “American Literature | Collin Course Number: ENGL 2327-2328 | Semester Credit Hours: 6 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|Minimum Score for Credit: 50]:  ⟵ “Analyzing & Interpreting Literature | Collin Course Number: ENGL 2341 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|Minimum Score for Credit: 50]:  ⟵ “College Composition** | Collin Course Number: ENGL 1301 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-ENGLISH-LITERATURE|Minimum Score for Credit: 50]:  ⟵ “English Literature | Collin Course Number: ENGL 2322-2323 | Semester Credit Hours: 6 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature | Science & Mathematics”
  - equivalencies[CLEP-BIOLOGY|Minimum Score for Credit: 50]:  ⟵ “Biology | Collin Course Number: BIOL 1406-1407 | Semester Credit Hours: 8 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-CHEMISTRY|Minimum Score for Credit: 50]:  ⟵ “Chemistry | Collin Course Number: CHEM 1411-1412 | Semester Credit Hours: 8 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|Minimum Score for Credit: 50]:  ⟵ “College Algebra | Collin Course Number: MATH 1314 | Semester Credit Hours: 3 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-PRECALCULUS|Minimum Score for Credit: 50]:  ⟵ “Pre-Calculus | Collin Course Number: MATH 2412 | Semester Credit Hours: 4 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-CALCULUS|Minimum Score for Credit: 50]:  ⟵ “Calculus | Collin Course Number: MATH 2413 | Semester Credit Hours: 4 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | Foreign Language”
  - equivalencies[CLEP-FRENCH-LANGUAGE|Minimum Score for Credit: 50]:  ⟵ “French Language | Collin Course Number: FREN 1411-1412 | Semester Credit Hours: 8 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-FRENCH-LANGUAGE|Semester Credit Hours: 59]:  ⟵ “French Language | FREN 1411-1412, 2311-2312 | Collin Course Number: 14 | Semester Credit Hours: 59”
  - equivalencies[CLEP-GERMAN-LANGUAGE|Minimum Score for Credit: 50]:  ⟵ “German Language | Collin Course Number: GERM 1411-1412 | Semester Credit Hours: 8 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-GERMAN-LANGUAGE|Semester Credit Hours: 60]:  ⟵ “German Language | GERM 1411-1412, 2311-2312 | Collin Course Number: 14 | Semester Credit Hours: 60”
  - equivalencies[CLEP-SPANISH-LANGUAGE|Minimum Score for Credit: 50]:  ⟵ “Spanish Language | Collin Course Number: SPAN 1411-1412 | Semester Credit Hours: 8 | Minimum Score for Credit: 50”
  - equivalencies[CLEP-SPANISH-LANGUAGE|Semester Credit Hours: 63]:  ⟵ “Spanish Language | SPAN 1411-1412, 2311-2312 | Collin Course Number: 14 | Semester Credit Hours: 63”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “Spanish Language | History & Social Sciences”
  - … 6 more rows
### `c4578a61de85242c` Dallas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.dallascollege.edu/paying-for-college/financial-aid/keeping-aid/sap/ (sha256 00dde811174b)
- issues: semantic_review_required, conflicting_sources:https://www.dallascollege.edu/paying-for-college/financial-aid/keeping-aid/sap/sap-24-25/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid will send SAP appeal engagement and appeal application instructions via Workday Student Notifications and Task Box.”
### `c74803bf469b9d03` Dallas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.dallascollege.edu/paying-for-college/financial-aid/keeping-aid/sap/sap-24-25/ (sha256 e6b2c7bc530d)
- issues: semantic_review_required, conflicting_sources:https://www.dallascollege.edu/paying-for-college/financial-aid/keeping-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 14}
  - sentence: sap_appeal ⟵ “To be eligible for a SAP appeal, students MUST make a payment plan.”
  - sentence: sap_appeal ⟵ “Students placed on Suspension or Maximum Timeframe Suspension will receive their SAP status notification and appeal application via the Workday Task Box, and it will contain instructions to complete the SAP appeal process.”
  - sentence: sap_appeal ⟵ “SAP appeal deadlines are Dec. 10, 2026, for fall 2026, May 13, 2027, for spring 2027, and Aug. 12, 2027, for summer 2027 by 11:59 p.m.”
  - sentence: sap_appeal ⟵ “SAP Appeal Committee decisions are final; and cannot be disputed.”
  - sentence: sap_appeal ⟵ “If the student fails to meet the Satisfactory Academic Progress policy by their next period of enrollment, then they will become ineligible for all subsequent terms until either they meet the Satisfactory Academic Progress policy, or another successful appeal is granted.”
  - sentence: sap_appeal ⟵ “The decision of the Satisfactory Academic Progress Appeals Review Committee is final.”
### `59bbd0f07d14e931` Dallas College — costs 2025-26 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.dallascollege.edu/paying-for-college/cost-tuition/costs-of-attendance/ (sha256 0ab67da594ac)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 6000 ⟵ “Tuition | $2,376 | $4,056 | $6,000”
  - column:Book & Supplies: 440 ⟵ “Book & Supplies | $440 | $440 | $440”
  - column:Food & Housing: 13532 ⟵ “Food & Housing | $13,532 | $13,532 | $13,532”
  - column:Transportation: 9288 ⟵ “Transportation | $5,588 | $9,756 | $9,288”
  - column:Personal Expenses: 3256 ⟵ “Personal Expenses | $3,256 | $3,256 | $3,256”
  - column:Est Loan Fees: 56 ⟵ “Est Loan Fees | $56 | $56 | $56”
  - column:Total: 32572 ⟵ “Total | $25,248 | $31,096 | $32,572”
### `a80805883d57bf50` Dallas College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.dallascollege.edu/paying-for-college/cost-tuition/costs-of-attendance/ (sha256 0ab67da594ac)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition: 2376 ⟵ “Tuition | $2,376 | $4,056 | $6,000”
  - column:Book & Supplies: 440 ⟵ “Book & Supplies | $440 | $440 | $440”
  - column:Food & Housing: 13532 ⟵ “Food & Housing | $13,532 | $13,532 | $13,532”
  - column:Transportation: 5588 ⟵ “Transportation | $5,588 | $9,756 | $9,288”
  - column:Personal Expenses: 3256 ⟵ “Personal Expenses | $3,256 | $3,256 | $3,256”
  - column:Est Loan Fees: 56 ⟵ “Est Loan Fees | $56 | $56 | $56”
  - column:Total: 25248 ⟵ “Total | $25,248 | $31,096 | $32,572”
  - column:Tuition: 4056 ⟵ “Tuition | $2,376 | $4,056 | $6,000”
  - column:Book & Supplies: 440 ⟵ “Book & Supplies | $440 | $440 | $440”
  - column:Food & Housing: 13532 ⟵ “Food & Housing | $13,532 | $13,532 | $13,532”
  - column:Transportation: 9756 ⟵ “Transportation | $5,588 | $9,756 | $9,288”
  - column:Personal Expenses: 3256 ⟵ “Personal Expenses | $3,256 | $3,256 | $3,256”
  - column:Est Loan Fees: 56 ⟵ “Est Loan Fees | $56 | $56 | $56”
  - column:Total: 31096 ⟵ “Total | $25,248 | $31,096 | $32,572”
### `3304243e3aa9b73a` Houston Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hccs.edu/paying-for-college/financial-aid--scholarships/financial-aid-contact-center/ (sha256 d12c136713c0)
- issues: semantic_review_required, conflicting_sources:https://www.hccs.edu/paying-for-college/financial-aid--scholarships/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If you have questions about your SAP status, the appeal process, or how to keep your financial aid on track, join us for a virtual SAP PREP session!”
  - sentence: sap_appeal ⟵ “During this drop-in session, our Financial Aid team will cover: What SAP is and why it matters How to understand your SAP status The SAP appeal process Important deadlines and required documents Tips for maintaining your financial aid eligibility Live Q&A to answer your questions Session Dates August 6 | 1 p.m. – 4 p.m.”
### `3349ce46d54d267e` Houston Community College — appeals 2013-14 [new] (labeled_in_source)
- source: https://www.hccs.edu/media/hccsedu/content-assets/documents/paying-for-college/financial-aid--scholarships/satisfactory-academic-progress/SAP-Policy_2026-(1).pdf (sha256 9c49fb479e94)
- issues: stale_year_label:2013-14, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “A student on suspension may appeal to reestablish eligibility by submitting a b. “Financial Aid Appeal for Satisfactory Academic Progress” form with supporting documentation to the Financial Aid Office by the census date of each regular term of the semester.”
### `4e87b089f5db5afd` Houston Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hccs.edu/paying-for-college/financial-aid--scholarships/satisfactory-academic-progress/ (sha256 a57e59f064b8)
- issues: semantic_review_required, conflicting_sources:https://www.hccs.edu/paying-for-college/financial-aid--scholarships/financial-aid-contact-center/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Examples of extenuating circumstances include (not limited to): Illness Injury Learning or functional disability Loss of family member Change in work schedule or responsibilities Other unusual event disrupting the academic performance APPEAL INFORMATION Financial Aid SAP Appeals must be based on justifiable reasons or extenuating circumstances that prevented student from meeting SAP requirements.”
  - sentence: sap_appeal ⟵ “If you have any questions or concerns, please feel free to visit your nearest Financial Aid office) If you submitted an appeal for a past semester and then took a break from school, please contact the financial aid office for current decision/consideration. 25/26 SAP Application 26/27 SAP Application Appeal Approved | Probation Status If the appeal is approved, financial aid may be reinstated with”
  - sentence: sap_appeal ⟵ “Full SAP Policy Details of the SAP policy, measurements, and appeal procedures can be viewed here: Satisfactory Academic Progress Policy Not Meeting SAP?”
  - sentence: sap_appeal ⟵ “Tutoring Counseling Financial Coaching Academic Advising Financial Services Deadlines SAP Appeal Submission Deadlines A student who is ineligible for financial aid for failure to meet HCC’s Satisfactory Academic Progress (SAP) requirements may file an initial (first attempt) SAP appeal.”
  - sentence: sap_appeal ⟵ “Initial SAP appeals must be submitted to the Financial Aid Office by the following deadlines: Fall - September 15 Spring - February 15 Summer - July 1 Committee Appeal Timelines and Deadlines Committee (2nd chance) appeals are an option for students whose initial appeal is denied.”
### `5d4f627095215cab` Houston Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.hccs.edu/paying-for-college/tuition--cost/the-financial-aid-cost-of-attendance/ (sha256 74e93a41454f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “In-District Less than Half-time | $2,196 Half-time to Full-time With Parents | $10,552 Half-time to Full-time Without Parents | $33,456 Out-of-District Less than Half-time | $2,772 Half-time to Full-time With Parents | $12,280 Half-time to Full-time Without Parents | $35,184 Out-of-State Less than Half-time | $3,048 Half-time to Full-time With Parents | $12,280 Half-time to Full-time Without Paren”
### `760f4037012c96dc` Houston Community College — appeals 2013-14 [new] (labeled_in_source)
- source: https://www.hccs.edu/media/hccsedu/content-assets/documents/paying-for-college/financial-aid--scholarships/satisfactory-academic-progress/SAP-Policy_2026-(1).pdf (sha256 9c49fb479e94)
- issues: stale_year_label:2013-14, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of mitigating circumstances include student or family illness, severe injury, learning or functional disability, or an unusual circumstance that disrupted the students academic performance.”
### `793c445176e25a08` Houston Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hccs.edu/paying-for-college/financial-aid--scholarships/satisfactory-academic-progress/ (sha256 a57e59f064b8)
- issues: semantic_review_required, conflicting_sources:https://www.hccs.edu/paying-for-college/financial-aid--scholarships/how-to-apply-for-financial-aid/special-circumstances---fafsa/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “We understand there may have been unusual circumstances that led to your current SAP status, but we believe you can excel and overcome any obstacles that you may encounter.”
### `9d16eb2a07fe2c15` Houston Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hccs.edu/paying-for-college/financial-aid--scholarships/how-to-apply-for-financial-aid/special-circumstances---fafsa/ (sha256 a480dd2191d8)
- issues: semantic_review_required, conflicting_sources:https://www.hccs.edu/paying-for-college/financial-aid--scholarships/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “If you or your family have experienced loss in income since filing the FAFSA, then you should submit a Special Circumstances Form to have your financial aid file reviewed.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are for those who have experienced a reduction in income and/or benefits since submitting their FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “A Special Circumstances Request form will allow you to request that HCC uses current or future income/benefits to make changes to your FAFSA and recalculate your eligibility to receive aid.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Special Circumstances an include: Loss of employment Loss of income (EX: Alimony, Child Support, Retirement/pension, Social Security (taxed), worker’s compensation) Separation or Divorce Death of Spouse Medical/Dental Expense Other (EX: Natural Disaster, Secondary tuition, or other unusual cost) If you believe you have experienced a special circumstance Click here to go to the Financia”
  - sentence: need_based_special_circumstances ⟵ “Please note that if you already have a calculated Expected Family Contribution (EFC) of zero (0) then submitting a Special Circumstances Request Form will not change your financial aid award amount.”
  - sentence: need_based_special_circumstances ⟵ “For questions on whether you qualify for a special circumstance, or questions about the process to get your financial aid file reviewed, visit our website for Financial Aid Contact Methods.”
### `acdd1f4350eb31a2` Houston Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hccs.edu/paying-for-college/financial-aid--scholarships/how-to-apply-for-financial-aid/special-circumstances---fafsa/ (sha256 a480dd2191d8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Federal regulations require financial aid administrators to make professional judgments in regard to students who have special circumstances that could affect their ability to pay for their education.”
### `c05cd185d126b016` Houston Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.hccs.edu/paying-for-college/tuition--cost/the-financial-aid-cost-of-attendance/ (sha256 74e93a41454f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Please visit a Financial Aid Office near you to request Professional Judgement for adjustment to the Cost of Attendance.”
### `882a1265fc09da29` Houston Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.hccs.edu/paying-for-college/tuition--cost/the-financial-aid-cost-of-attendance/ (sha256 74e93a41454f)
- issues: arrangement_unlabeled, components_do_not_reconcile, cost_period_semester, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": false, "rows": 8}
  - with_parents_or_family:Tuition & Fees*: 765 ⟵ “Tuition & Fees* | $765 | $1629 | $2043 | $765 | $1629 | $2043”
  - with_parents_or_family:Books & Supplies: 1125 ⟵ “Books & Supplies | $1125 | $1125 | $1125 | $1125 | $1125 | $1125”
  - with_parents_or_family:Food & Housing: 1201 ⟵ “Food & Housing | $1201 | $1201 | $1201 | $12653 | $12653 | $12653”
  - with_parents_or_family:Transportation: 935 ⟵ “Transportation | $935 | $935 | $935 | $935 | $935 | $935”
  - with_parents_or_family:Personal Expenses: 1215 ⟵ “Personal Expenses | $1215 | $1215 | $1215 | $1215 | $1215 | $1215”
  - with_parents_or_family:Est. Loan Fees: 35 ⟵ “Est. Loan Fees | $35 | $35 | $35 | $35 | $35 | $35”
  - with_parents_or_family:Professional Licensure Fee**: 320 ⟵ “Professional Licensure Fee** | $320 | $320 | $320 | $320 | $320 | $320”
  - with_parents_or_family:TOTAL: 5276 ⟵ “TOTAL | $5276 | $6140 | $6554 | $16728 | $17592 | $18006”
  - with_parents_or_family:Tuition & Fees*: 1629 ⟵ “Tuition & Fees* | $765 | $1629 | $2043 | $765 | $1629 | $2043”
  - with_parents_or_family:Books & Supplies: 1125 ⟵ “Books & Supplies | $1125 | $1125 | $1125 | $1125 | $1125 | $1125”
  - with_parents_or_family:Food & Housing: 1201 ⟵ “Food & Housing | $1201 | $1201 | $1201 | $12653 | $12653 | $12653”
  - with_parents_or_family:Transportation: 935 ⟵ “Transportation | $935 | $935 | $935 | $935 | $935 | $935”
  - with_parents_or_family:Personal Expenses: 1215 ⟵ “Personal Expenses | $1215 | $1215 | $1215 | $1215 | $1215 | $1215”
  - with_parents_or_family:Est. Loan Fees: 35 ⟵ “Est. Loan Fees | $35 | $35 | $35 | $35 | $35 | $35”
  - with_parents_or_family:Professional Licensure Fee**: 320 ⟵ “Professional Licensure Fee** | $320 | $320 | $320 | $320 | $320 | $320”
  - with_parents_or_family:TOTAL: 6140 ⟵ “TOTAL | $5276 | $6140 | $6554 | $16728 | $17592 | $18006”
  - column:Tuition & Fees*: 765 ⟵ “Tuition & Fees* | $765 | $1629 | $2043 | $765 | $1629 | $2043”
  - column:Books & Supplies: 1125 ⟵ “Books & Supplies | $1125 | $1125 | $1125 | $1125 | $1125 | $1125”
  - column:Food & Housing: 12653 ⟵ “Food & Housing | $1201 | $1201 | $1201 | $12653 | $12653 | $12653”
  - column:Transportation: 935 ⟵ “Transportation | $935 | $935 | $935 | $935 | $935 | $935”
  - column:Personal Expenses: 1215 ⟵ “Personal Expenses | $1215 | $1215 | $1215 | $1215 | $1215 | $1215”
  - column:Est. Loan Fees: 35 ⟵ “Est. Loan Fees | $35 | $35 | $35 | $35 | $35 | $35”
  - column:Professional Licensure Fee**: 320 ⟵ “Professional Licensure Fee** | $320 | $320 | $320 | $320 | $320 | $320”
  - column:TOTAL: 16728 ⟵ “TOTAL | $5276 | $6140 | $6554 | $16728 | $17592 | $18006”
  - column:Tuition & Fees*: 1629 ⟵ “Tuition & Fees* | $765 | $1629 | $2043 | $765 | $1629 | $2043”
  - … 7 more rows
### `944f52e31c096c51` Houston Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.hccs.edu/paying-for-college/tuition--cost/the-financial-aid-cost-of-attendance/ (sha256 74e93a41454f)
- issues: arrangement_unlabeled, components_do_not_reconcile, cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - with_parents_or_family:Tuition & Fees*: 2043 ⟵ “Tuition & Fees* | $765 | $1629 | $2043 | $765 | $1629 | $2043”
  - with_parents_or_family:Books & Supplies: 1125 ⟵ “Books & Supplies | $1125 | $1125 | $1125 | $1125 | $1125 | $1125”
  - with_parents_or_family:Food & Housing: 1201 ⟵ “Food & Housing | $1201 | $1201 | $1201 | $12653 | $12653 | $12653”
  - with_parents_or_family:Transportation: 935 ⟵ “Transportation | $935 | $935 | $935 | $935 | $935 | $935”
  - with_parents_or_family:Personal Expenses: 1215 ⟵ “Personal Expenses | $1215 | $1215 | $1215 | $1215 | $1215 | $1215”
  - with_parents_or_family:Est. Loan Fees: 35 ⟵ “Est. Loan Fees | $35 | $35 | $35 | $35 | $35 | $35”
  - with_parents_or_family:Professional Licensure Fee**: 320 ⟵ “Professional Licensure Fee** | $320 | $320 | $320 | $320 | $320 | $320”
  - with_parents_or_family:TOTAL: 6554 ⟵ “TOTAL | $5276 | $6140 | $6554 | $16728 | $17592 | $18006”
  - column:Tuition & Fees*: 2043 ⟵ “Tuition & Fees* | $765 | $1629 | $2043 | $765 | $1629 | $2043”
  - column:Books & Supplies: 1125 ⟵ “Books & Supplies | $1125 | $1125 | $1125 | $1125 | $1125 | $1125”
  - column:Food & Housing: 12653 ⟵ “Food & Housing | $1201 | $1201 | $1201 | $12653 | $12653 | $12653”
  - column:Transportation: 935 ⟵ “Transportation | $935 | $935 | $935 | $935 | $935 | $935”
  - column:Personal Expenses: 1215 ⟵ “Personal Expenses | $1215 | $1215 | $1215 | $1215 | $1215 | $1215”
  - column:Est. Loan Fees: 35 ⟵ “Est. Loan Fees | $35 | $35 | $35 | $35 | $35 | $35”
  - column:Professional Licensure Fee**: 320 ⟵ “Professional Licensure Fee** | $320 | $320 | $320 | $320 | $320 | $320”
  - column:TOTAL: 18006 ⟵ “TOTAL | $5276 | $6140 | $6554 | $16728 | $17592 | $18006”
### `f2f6707e2aeb77ad` Houston Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.hccs.edu/media/hccsedu/content-assets/documents/admissions/testing-services/clep---credit-by-exam/clep-ap.pdf (sha256 1b88df0dbc68)
- issues: credits_implausible, score_scale_mismatch
- checks: {"distinct_exams": 31, "equivalencies": 89, "rows_without_score": 0}
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|46]:  ⟵ “Principles of Management                  46    50          BMGT 1327 Principles of Management                    3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|45]:  ⟵ “Financial Accounting                      45    50          ACCT 2301 Prin. of Financial Accounting               3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|51]:  ⟵ “Introductory Business Law                 51    50          BUSG 2305 Business Law/Contracts                      3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing                   50    50          MRKG 1311 Principles of Marketing                     3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|46]:  ⟵ “American Literature                      46  50            ENGL 2327 American Literature I                       3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|46]:  ⟵ “English Literature                       46  50            ENGL 2322-23 British Literature I-II                  6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                          50            ENGL 1301-02 Composition I & II                       6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular                  50            ENGL 1301 Composition I                               3”
  - equivalencies[CLEP-HUMANITIES|3]:  ⟵ “Humanities                               420 50            HUMA 1301 Introduction to Humanities                  3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|39]:  ⟵ “French Language I                        39    50          FREN 1411-12 Beginning French I-II                    8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|45]:  ⟵ “French Language II                       45    59          FREN 2311-12 Intermediate French I-II                14”
  - equivalencies[CLEP-GERMAN-LANGUAGE|36]:  ⟵ “German Language I                        36    50          GERM 1411-12 Beginning German I-II                    8”
  - equivalencies[CLEP-GERMAN-LANGUAGE|42]:  ⟵ “German Language II                       42    60          GERM 2311-12 Intermediate German I-II                14”
  - equivalencies[CLEP-SPANISH-LANGUAGE|45]:  ⟵ “Spanish Language I                       45    50          SPAN 1411-12 Beginning Spanish I-II                   8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language II                      50    63          SPAN 2311-12 Intermediate Spanish I-II               14”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing I                         50          SPAN 1411-12 Beginning Spanish I-II                   8”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|65]:  ⟵ “Spanish with Writing II                        65          SPAN 2311-12 Intermediate Spanish I-II               14”
  - equivalencies[CLEP-CALCULUS|41]:  ⟵ “Calculus                                 41  50            MATH 2413 Calculus I                                  4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|46]:  ⟵ “College Algebra                          46  50            MATH 1314 College Algebra                             3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                                  50            MATH 2412 Precalculus                                 4”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|3]:  ⟵ “College Mathematics                      420 50            MATH 1332 Contemporary Mathematics                    3”
  - equivalencies[CLEP-NATURAL-SCIENCES|3]:  ⟵ “Natural Sciences                         420 50            BIOL 1308 Introductory Biology I                      3”
  - equivalencies[CLEP-BIOLOGY|46]:  ⟵ “Biology                                  46    50          BIOL 1306-07 General Biology I-II                     6”
  - equivalencies[CLEP-CHEMISTRY|47]:  ⟵ “General Chemistry                        47    50          CHEM 1311-12 General Chemistry I-II                   6”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|47]:  ⟵ “American Government                      47    50          GOVT 2305 Federal Government                         3”
  - … 64 more rows
### `1df61167c3f2361d` Lone Star College System — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lonestar.edu/departments/financialaid/SAP%20Appeal%20Instructions.pdf (sha256 640f3b8b9d73)
- issues: semantic_review_required, conflicting_sources:https://www.lonestar.edu/departments/financialaid/2026-2027%20SAP%20Committee%20Appeal.pdf,https://www.lonestar.edu/departments/financialaid/LSCSAPPolicy.pdf,https://www.lonestar.edu/satisfactory-academic-progress.htm
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP APPEAL INSTRUCTIONS SAP SUBMISSION DEADLINES OCTOBER 1- FALL FEBRUARY 15- SPRING JUNE 15- SUMMER Appeal Process A student who does not meet SAP requirements and becomes ineligible for financial aid may submit an SAP appeal.”
  - sentence: sap_appeal ⟵ “Sap appeal statuses Status Action Required No Action Taken No Action: Your appeal is in review More Information Needed Review the comments and submit the additional information requested.”
### `56e24ba453f8ce76` Lone Star College System — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lonestar.edu/FA-ProfessionalJudgment (sha256 147e4d12f176)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances (Income Related) Some circumstances impact a family’s income, financial need, or cost of attendance.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances (Dependency Related) Other unusual circumstances impact a student’s dependency status.”
  - sentence: need_based_special_circumstances ⟵ “If you have no contact with your parents and don't know where they live, or you have left home due to an abusive situation, select "Yes" to the "Do unusual circumstances prevent the student from contacting their parents or would contacting their parents pose a risk to the student?" question on the FAFSA form.”
### `70dc6b2292110e5b` Lone Star College System — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lonestar.edu/departments/financialaid/2026-2027%20SAP%20Committee%20Appeal.pdf (sha256 8673e3f43eb4)
- issues: semantic_review_required, conflicting_sources:https://www.lonestar.edu/departments/financialaid/LSCSAPPolicy.pdf,https://www.lonestar.edu/departments/financialaid/SAP%20Appeal%20Instructions.pdf,https://www.lonestar.edu/satisfactory-academic-progress.htm
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAVE CLEAR PRINT 2026 – 2027 SATISFACTORY ACADEMIC PROGRESS COMMITTEE APPEAL Student ID Number ___________________________ Name ___________________________________________________________________ Date of Birth _________________ Last First M.I. mm/dd/yyyy Students whose initial appeal was denied have the option to submit a second appeal for ﬁnal review by a committee.”
  - sentence: sap_appeal ⟵ “My initial Satisfactory Academic Progress appeal was denied due to a lack of extenuating circumstances or documentation.”
  - sentence: sap_appeal ⟵ “I will not be eligible for ﬁnancial aid until I have regained eligibility by meeting all Satisfactory Academic Progress standards. facc@lonestar.edu | lonestar.edu/ﬁnancial-aid | (281)290-2700 Page 1 of 2 SAP Committee Appeal Name:___________________________________________________ Last First M.I.”
### `cebbf4663149d641` Lone Star College System — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lonestar.edu/satisfactory-academic-progress.htm (sha256 37177a5d92d5)
- issues: semantic_review_required, conflicting_sources:https://www.lonestar.edu/departments/financialaid/2026-2027%20SAP%20Committee%20Appeal.pdf,https://www.lonestar.edu/departments/financialaid/LSCSAPPolicy.pdf,https://www.lonestar.edu/departments/financialaid/SAP%20Appeal%20Instructions.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal Students who lose financial aid for not meeting SAP may appeal by providing information on extenuating circumstances and what has changed to support academic progress.”
  - sentence: sap_appeal ⟵ “Appeals must be submitted by the posted deadlines: Appeal Deadlines | Semester | Appeal | Appeal Committee (Second Appeal) | Academic Plan | Fall Semester | October 1 | October 15 | November 15 | Spring Semester | February 15 | March 1 | April 1 | Summer Semester | June 15 | July 1 | July 15 SAP Appeal Instructions Appeals do not guarantee reinstatement of aid and must be submitted through the Fin”
  - sentence: sap_appeal ⟵ “SAP Appeal Instructions.pdf Verification Steps Satisfactory Academic Progress (SAP) Statuses Students who do not meet SAP standards lose financial aid eligibility and will be notified via MyLoneStar email and the Financial Aid Portal.”
### `df156a64eb629225` Lone Star College System — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lonestar.edu/FA-ProfessionalJudgment (sha256 147e4d12f176)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: professional_judgment ⟵ “Financial Aid Advisors have the authority to use their professional judgment to review your circumstances on a case-by-case basis and make adjustments, if necessary.”
  - sentence: professional_judgment ⟵ “All requests for a professional judgement review are required to have a detailed letter of explanation and supporting documentation.”
  - sentence: professional_judgment ⟵ “The following special circumstances may qualify for a professional judgment review: Reduction of income for student, spouse, or parent due to loss of employment, death, separation, divorce, or other special circumstance.”
  - sentence: professional_judgment ⟵ “With appropriate documentation, a financial aid advisor may make a professional judgment decision to adjust income or cost elements that impact a student’s financial need.”
  - sentence: professional_judgment ⟵ “Unusual circumstances that may qualify for a professional judgment review include: Dysfunctional family situation or parental relationship that has been permanently severed.”
  - sentence: professional_judgment ⟵ “With appropriate documentation, a financial aid advisor may make a professional judgment decision to change a student’s dependency status to independent to qualify for financial aid.”
### `ef4b744f9c46e212` Lone Star College System — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lonestar.edu/departments/financialaid/LSCSAPPolicy.pdf (sha256 ed1652df20a3)
- issues: semantic_review_required, conflicting_sources:https://www.lonestar.edu/departments/financialaid/2026-2027%20SAP%20Committee%20Appeal.pdf,https://www.lonestar.edu/departments/financialaid/SAP%20Appeal%20Instructions.pdf,https://www.lonestar.edu/satisfactory-academic-progress.htm
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Students who submit SAP appeals will be notified of the Appeal Committee’s decision via LSC email and the myLoneStar student portal.”
  - sentence: sap_appeal ⟵ “Post Bac or any students seeking a second degree must submit a SAP appeal (see below) with an Academic Plan (see below) for consideration.”
  - sentence: sap_appeal ⟵ “FINANCIAL AID PROBATION The status assigned to a student who fails to meet SAP standards, has appealed, and had the appeal approved.”
  - sentence: sap_appeal ⟵ “A Satisfactory Academic Progress Appeal Form must be submitted to the appropriate Campus Financial Aid Office.”
  - sentence: sap_appeal ⟵ “If s/he is not meeting the SAP guidelines, an approved Financial Aid SAP appeal is required to receive aid.”
### `9d3c7b9eba477034` Lone Star College System — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lonestar.edu/cost-of-attendance.htm (sha256 3a24426e250e)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - column:Tuition and Fees: 3330 ⟵ “Tuition and Fees | $3,330 | $7,470 | $9,390”
  - column:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96”
  - column:Books and Supplies*: 2450 ⟵ “Books and Supplies* | $2,450 | $2,450 | $2,450”
  - column:Food and Housing: 10960 ⟵ “Food and Housing | $10,960 | $10,960 | $10,960”
  - column:Transportation: 1510 ⟵ “Transportation | $1,510 | $1,510 | $2,510”
  - column:Personal / Misc: 4008 ⟵ “Personal / Misc | $4,008 | $4,008 | $4,008”
  - column:Professional Licensure Fee**: 410 ⟵ “Professional Licensure Fee** | $410 | $410 | $410”
  - column:TOTAL: 22764 ⟵ “TOTAL | $22,764 | $26,904 | $29,824”
  - column:Tuition and Fees: 7470 ⟵ “Tuition and Fees | $3,330 | $7,470 | $9,390”
  - column:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96”
  - column:Books and Supplies*: 2450 ⟵ “Books and Supplies* | $2,450 | $2,450 | $2,450”
  - column:Food and Housing: 10960 ⟵ “Food and Housing | $10,960 | $10,960 | $10,960”
  - column:Transportation: 1510 ⟵ “Transportation | $1,510 | $1,510 | $2,510”
  - column:Personal / Misc: 4008 ⟵ “Personal / Misc | $4,008 | $4,008 | $4,008”
  - column:Professional Licensure Fee**: 410 ⟵ “Professional Licensure Fee** | $410 | $410 | $410”
  - column:TOTAL: 26904 ⟵ “TOTAL | $22,764 | $26,904 | $29,824”
### `127ab8445e725629` Lone Star College System — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_url)
- source: https://www.lonestar.edu/college-departments/dualcredit/images/DC-CostChart-2025-2026.pdf (sha256 860b0f4a1634)
- issues: stale_year_label:2025-26
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 111 ⟵ “College’s Victory Center. Students are charged an in-district tuition rate of $111 per credit hour.”
  - per_credit_hour_charge: 249 ⟵ “boundaries on the official enrollment reporting date. Students are charged an out-of-district tuition rate of $249 per credit hour.”
  - per_credit_hour_charge: 313 ⟵ “rate of $313 per credit hour.”
  - per_credit_hour_charge: 21 ⟵ “*Students participating in the STAR Bundle program for books and supplies will be charged $21 per credit hour. Visit”
### `051690f6fc50d543` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-arts-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf (sha256 8fdab4b39fed)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/college-of-the-mainland/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf,https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-ba-criminal-justice-2025-2026.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts – Criminal Justice to ⟵ “Transfer Degree Map: South Texas College
Associate of Arts – Criminal Justice to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2025 – 2026 Catalog Year
First Year - Freshman”
### `0ea45261c10c976c` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-applied-science-criminal-justice-and-public-safety-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/dallas-college/aas-criminal-justice-and-public-safety-to-baas-w-criminal-justice-concentration-25-26.pdf (sha256 53e135e3651c)
- issues: stale_year_label:2025-26
- checks: {"summary_lines": 0, "terms": 4}
  - program_name: Associate of Applied Science – Criminal Justice and Public Safety to ⟵ “Transfer Degree Map: Dallas College
Associate of Applied Science – Criminal Justice and Public Safety to
Sam Houston State University
Bachelor of Applied Arts and Sciences: Criminal Justice Concentration
4 – Year Suggested Academic Plan for Transfer, 2025 – 2026 Catalog Year
Dallas College”
### `0f0789dde29a89cf` Sam Houston State University — academic_programs 2024-25 · program_key=criminal-and-forensic-science-associate-of-applied-science-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/aas-criminal-and-forensic-science-to-baas-with-criminal-justice-concentration-24-25.pdf (sha256 26fc9e77bb5a)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Criminal and Forensic Science Associate of Applied Science to ⟵ “Transfer Degree Map
Lamar State College Orange
Criminal and Forensic Science Associate of Applied Science to
Sam Houston State University
Bachelor of Applied Arts & Sciences - Criminal Justice Concentration
4 – Year Suggested Academic Plan for Transfer, 2024 - 2025”
### `1530efdf1192ee67` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lee-college/as-to-bs-comp-sci-24-25-lee-college.pdf (sha256 a11c6039908b)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Science to ⟵ “Transfer Degree Map: Lee College
Associate of Science to
Sam Houston State University
Bachelor of Science in Computing Science (Computing Science, CS)
4 – Year Suggested Academic Plan for Transfer, 2024-2025 Catalog Year
First Year - Freshman”
### `1ac6505c984d1d09` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-science-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-institute-of-technology/as-criminal-justice-to-bs-in-criminal-justice-25-26.pdf (sha256 9878a37b388f)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/lee-college/as-to-bs-comp-sci-25-26-lee-college.pdf
- checks: {"summary_lines": 0, "terms": 4}
  - program_name: Associate of Science to ⟵ “Transfer Degree Map: Lamar Institute of Technology
Associate of Science to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2025 – 2026 Catalog Year
First Year - Freshman”
### `1b87efdf599cd1e3` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-arts-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/austin-community-college/aa-criminal-justice-ba-criminal-justice-2024-2025.pdf (sha256 9c420bebf61e)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts Criminal Justice to ⟵ “Transfer Degree Map: Austin Community College
Associate of Arts Criminal Justice to
Sam Houston State University Bachelor of
Arts in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year - Freshman”
### `260e71f80a7175f9` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-arts-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lee-college/aa-to-bs-criminal-justice-2024-2025.pdf (sha256 6e8ffc6e093d)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/austin-community-college/aa-criminal-justice-bs-criminal-justice-2024-2025.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts to ⟵ “Transfer Degree Map: Lee College
Associate of Arts to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year - Freshman”
### `290ab67704efb55d` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-field-of-study-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-criminal-justice-24-25.pdf (sha256 2f3774183c58)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-homeland-security-studies-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-homeland-security-studies-24-25.pdf
- checks: {"summary_lines": 0, "terms": 9}
  - program_name: Associate of Science Field of Study Criminal Justice to ⟵ “Transfer Degree Map:
Associate of Science Field of Study Criminal Justice to
Sam Houston State University
Bachelor of Arts in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year - Freshman”
### `3206829cbe643f9a` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-health-sciences-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-care-administration-24-25.pdf (sha256 da9ea1f69278)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-sciences-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-human-performance-and-wellness-management-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-public-health-24-25.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Science: Health Sciences to ⟵ “Transfer Degree Map: Angelina College
Associate of Science: Health Sciences to
Sam Houston State University
Bachelor of Science in Health Care Administration
4 -Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog
First Year - Freshman”
### `3581eb0c47b21639` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-applied-science-criminal-justice-texas-peace-officer [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/austin-community-college/aas-criminal-justice-tx-peace-officer-to-baas-criminal-justice-concentration-2024-2025.pdf (sha256 c2ed019da45f)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Applied Science - Criminal Justice – Texas Peace Officer ⟵ “Transfer Degree Map: Austin Community College
Associate of Applied Science - Criminal Justice – Texas Peace Officer
Specialization to Sam Houston State University
Bachelor of Applied Arts and Science with Concentration in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Ca”
### `4a5a03d5769d5f11` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-health-sciences-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-public-health-24-25.pdf (sha256 601e4ed2e46d)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-care-administration-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-sciences-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-human-performance-and-wellness-management-24-25.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Science: Health Sciences to ⟵ “Transfer Degree Map: Angelina College
Associate of Science: Health Sciences to
Sam Houston State University
Bachelor of Science in Public Health
4 -Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog
First Year - Freshman”
### `509718cb0e81b30d` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-health-sciences-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-sciences-24-25.pdf (sha256 5da7e35740d2)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-care-administration-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-human-performance-and-wellness-management-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-public-health-24-25.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Science: Health Sciences to ⟵ “Transfer Degree Map: Angelina College
Associate of Science: Health Sciences to
Sam Houston State University
Bachelor of Science in Health Sciences
4 -Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog
First Year - Freshman”
### `512e6244c8711567` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-arts-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lee-college/aa-to-bs-in-criminal-justice-25-26-lee-college.pdf (sha256 f6bc64782272)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/victoria-college/aa-to-bs-in-criminal-justice-2025-2026-victoria-college.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts to ⟵ “Transfer Degree Map: Lee College
Associate of Arts to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2025 – 2026 Catalog Year
First Year - Freshman”
### `5a68f186890f3ee3` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-arts-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-ba-criminal-justice-2025-2026.pdf (sha256 2e74e7e5bac7)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/college-of-the-mainland/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf,https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts – Criminal Justice to ⟵ “Transfer Degree Map: South Texas College
Associate of Arts – Criminal Justice to
Sam Houston State University
Bachelor Arts of in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2025 – 2026 Catalog Year
First Year - Freshman”
### `5b9989027f232228` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-arts-field-of-study-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/aa-criminal-justice-fos-ba-criminal-justice-2025-2026.pdf (sha256 b377a5846553)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/aa-criminal-justice-fos-bs-criminal-justice-2025-2026.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts Field of Study: Criminal Justice to ⟵ “Transfer Degree Map: Angelina College
Associate of Arts Field of Study: Criminal Justice to
Sam Houston State University
Bachelor of Arts in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, Catalog Year 2025 - 2026
First Year - Freshman”
### `5d9e26d08bcef967` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-applied-science-business-management-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/aas-management-to-baas-general-business-concentration-2024-2025.pdf (sha256 664dec7f18be)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Applied Science Business Management to ⟵ “Transfer Degree Map
Lamar State College Orange
Associate of Applied Science Business Management to
Sam Houston State University
Bachelor of Applied Arts & Sciences - General Business Concentration
4 – Year Suggested Academic Plan for Transfer, 2024 - 2025”
### `68280cdd309b8263` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-science-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lee-college/as-to-bs-comp-sci-25-26-lee-college.pdf (sha256 bab0e4a8d16f)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/lamar-institute-of-technology/as-criminal-justice-to-bs-in-criminal-justice-25-26.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Science to ⟵ “Transfer Degree Map: Lee College
Associate of Science to
Sam Houston State University
Bachelor of Science in Computing Science (Computing Science, CS)
4 – Year Suggested Academic Plan for Transfer, 2025-2026 Catalog Year
First Year - Freshman”
### `6a566b599688da1b` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-applied-science-criminal-justice-corrections-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/austin-community-college/aas-criminal-justice-corrections-to-baas-criminal-justice-concentration-2024-2025.pdf (sha256 d63d0507ae81)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Applied Science - Criminal Justice - Corrections to ⟵ “Transfer Degree Map: Austin Community College
Associate of Applied Science - Criminal Justice - Corrections to
Sam Houston State University
Bachelor of Applied Arts and Science with Concentration in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year -”
### `6a6236afb8feaa29` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-field-of-study-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-homeland-security-studies-24-25.pdf (sha256 a23c5888388b)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-homeland-security-studies-24-25.pdf
- checks: {"summary_lines": 0, "terms": 9}
  - program_name: Associate of Science Field of Study Criminal Justice to ⟵ “Transfer Degree Map:
Associate of Science Field of Study Criminal Justice to
Sam Houston State University
Bachelor of Arts in Homeland Security Studies
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year - Freshman”
### `6a6693a832f7067b` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-field-of-study-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-24-25.pdf (sha256 5c1daa43e419)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-homeland-security-studies-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-homeland-security-studies-24-25.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Science Field of Study Criminal Justice to ⟵ “Transfer Degree Map:
Associate of Science Field of Study Criminal Justice to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year - Freshman”
### `80bce93abccda19b` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-health-sciences-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-human-performance-and-wellness-management-24-25.pdf (sha256 b2bba8d161af)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-care-administration-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-sciences-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-public-health-24-25.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Science: Health Sciences to ⟵ “Transfer Degree Map: Angelina College
Associate of Science: Health Sciences to
Sam Houston State University
Bachelor of Science in Human Performance and Wellness Management
4 -Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog
First Year - Freshman”
### `835865bf33f23b08` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-science-field-of-study-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-homeland-security-studies-24-25.pdf (sha256 1ed680bc8091)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-homeland-security-studies-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-24-25.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Science Field of Study Criminal Justice to ⟵ “Transfer Degree Map:
Associate of Science Field of Study Criminal Justice to
Sam Houston State University
Bachelor of Science in Homeland Security Studies
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year - Freshman”
### `8724e71b359cfdb7` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-applied-sciences-accounting-services-management-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/aas-accounting-services-management-to-baas-buad-conc-2024-2025.pdf (sha256 1683e8eb817d)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Applied Sciences Accounting Services Management to ⟵ “Transfer Degree Map
Lamar State College Orange
Associate of Applied Sciences Accounting Services Management to
Sam Houston State University
Bachelor of Applied Arts & Sciences - General Business Concentration
4 – Year Suggested Academic Plan for Transfer, 2024 - 2025”
### `915be1271ce5a8a5` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-arts-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/austin-community-college/aa-criminal-justice-bs-criminal-justice-2024-2025.pdf (sha256 bc881eb71821)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/lee-college/aa-to-bs-criminal-justice-2024-2025.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts to ⟵ “Transfer Degree Map: Austin Community College
Associate of Arts to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year - Freshman”
### `9782b1c90bfd927d` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-arts-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/victoria-college/aa-to-bs-in-criminal-justice-2025-2026-victoria-college.pdf (sha256 4d54c48181b3)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/lee-college/aa-to-bs-in-criminal-justice-25-26-lee-college.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts to ⟵ “Transfer Degree Map: Victoria College
Associate of Arts to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2025 – 2026 Catalog Year
First Year - Freshman”
### `9a42bc84ec687e71` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-applied-science-social-work-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/alamo-colleges-district/aas-social-work-baas-victim-studies-minor-2024-2025.pdf (sha256 65c7a9d9591f)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Applied Science – Social Work to ⟵ “Transfer Degree Map: San Antonio College
Associate of Applied Science – Social Work to
Sam Houston State University
Bachelor of Applied Arts and Sciences with a Minor in Victim Studies
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
First Year - Freshman”
### `af8ada14283e8e04` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-arts-field-of-study-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/aa-criminal-justice-fos-bs-criminal-justice-2025-2026.pdf (sha256 5631e2c4a648)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/aa-criminal-justice-fos-ba-criminal-justice-2025-2026.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts Field of Study: Criminal Justice to ⟵ “Transfer Degree Map: Angelina College
Associate of Arts Field of Study: Criminal Justice to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, Catalog Year 2025 - 2026
First Year - Freshman”
### `b74e53cbf68c6434` Sam Houston State University — academic_programs 2025-26 · program_key=criminal-justice-associate-of-science-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/as-criminal-justice-to-ba-in-criminal-justice-25-26.pdf (sha256 1ff128a9a01c)
- issues: stale_year_label:2025-26
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Criminal Justice Associate of Science to ⟵ “Transfer Degree Map
Lamar State College Orange
Criminal Justice Associate of Science to
Sam Houston State University
Bachelor of Arts in Criminal Justice
4 – Year Suggested Academic Plan for Transfer, Catalog Year 2025 - 2026”
### `c125713ccf62626f` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-applied-science-homeland-security-and-emergency-management [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/central-texas-college/aas-homeland-security-emergency-management-to-baas-homeland-security-minor-2024-2025.pdf (sha256 91fc255cfbc1)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Applied Science – Homeland Security and Emergency Management ⟵ “Transfer Degree Map: Central Texas College
Associate of Applied Science – Homeland Security and Emergency Management
to Sam Houston State University
Bachelor of Applied Arts and Science with a minor in Homeland Security Studies
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catalog Year
”
### `ea4233136fc78231` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-applied-science-emergency-management-and-homeland-security [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-institute-of-technology/aas-emergency-management-homeland-security-to-baas-homeland-security-minor-2024-2025.pdf (sha256 d225672ec2b7)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Applied Science – Emergency Management and Homeland Security ⟵ “Transfer Degree Map: Lamar Institute of Technology
Associate of Applied Science – Emergency Management and Homeland Security
to Sam Houston State University
Bachelor of Applied Arts and Science with a minor in Homeland Security Studies
4 – Year Suggested Academic Plan for Transfer, 2024 – 2025 Catal”
### `f35985bbc7bba312` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-arts-field-of-study-in-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/dallas-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-25-26.pdf (sha256 a9232f59f3a2)
- issues: stale_year_label:2025-26
- checks: {"summary_lines": 0, "terms": 6}
  - program_name: Associate of Arts – Field of Study in Criminal Justice to ⟵ “Transfer Degree Map: Dallas College
Associate of Arts – Field of Study in Criminal Justice to
Sam Houston State University
Bachelor of Science: Criminal Justice
4 – Year Suggested Academic Plan for Transfer, 2025 – 2026 Catalog Year
Dallas College”
### `fac2d5684939aafc` Sam Houston State University — academic_programs 2024-25 · program_key=associate-of-applied-science-entrepreneurship-management-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/aas-entrepreneurship-management-to-baas-w-buad-conc-2024-2025.pdf (sha256 f8212b9d019f)
- issues: stale_year_label:2024-25
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Applied Science Entrepreneurship Management to ⟵ “Transfer Degree Map
Lamar State College Orange
Associate of Applied Science Entrepreneurship Management to
Sam Houston State University
Bachelor of Applied Arts & Sciences - General Business Concentration
4 - Year Suggested Academic Plan for Transfer, 2024 - 2025”
### `fef7204e64e159a4` Sam Houston State University — academic_programs 2025-26 · program_key=associate-of-arts-criminal-justice-to [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/college-of-the-mainland/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf (sha256 ab4bdd821d5c)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-ba-criminal-justice-2025-2026.pdf,https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf
- checks: {"summary_lines": 0, "terms": 8}
  - program_name: Associate of Arts - Criminal Justice to ⟵ “Transfer Degree Map: College of the Mainland
Associate of Arts - Criminal Justice to
Sam Houston State University
Bachelor of Science in Criminal Justice
4 - Year Suggested Academic Plan for Transfer, 2025 - 2026 Catalog Year
First Year - Freshman”
### `6de6e600f06bbd3e` Sam Houston State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.shsu.edu/cost-aid/satisfactory-academic-progress (sha256 50c61c4d60a8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Once you are on financial aid suspension, you will not receive financial aid until you meet the requirements or have an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “Filing a SAP appeal demonstrating mitigating circumstances (with supporting documentation) to be approved for an academic plan until you are meeting the minimum SAP requirements.”
### `0219e419772cef87` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-field-of-study-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-criminal-justice-24-25.pdf (sha256 2f3774183c58)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-homeland-security-studies-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-homeland-security-studies-24-25.pdf
  - terms: 9 ⟵ “First Year Fall | First Year Spring | First Year Summer | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `18ad5f7160afe47c` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-applied-science-criminal-justice-corrections-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/austin-community-college/aas-criminal-justice-corrections-to-baas-criminal-justice-concentration-2024-2025.pdf (sha256 d63d0507ae81)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `192e2d3df53f83c2` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-health-sciences-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-care-administration-24-25.pdf (sha256 da9ea1f69278)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-sciences-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-human-performance-and-wellness-management-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-public-health-24-25.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `20106289e384f5cf` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-health-sciences-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-sciences-24-25.pdf (sha256 5da7e35740d2)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-care-administration-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-human-performance-and-wellness-management-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-public-health-24-25.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `281a9235ae7259fc` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-applied-science-criminal-justice-texas-peace-officer · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/austin-community-college/aas-criminal-justice-tx-peace-officer-to-baas-criminal-justice-concentration-2024-2025.pdf (sha256 c2ed019da45f)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `3d3716ad5b08a806` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-arts-field-of-study-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/aa-criminal-justice-fos-bs-criminal-justice-2025-2026.pdf (sha256 5631e2c4a648)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/aa-criminal-justice-fos-ba-criminal-justice-2025-2026.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `45ed1cbb255d4c32` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-field-of-study-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-homeland-security-studies-24-25.pdf (sha256 1ed680bc8091)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-homeland-security-studies-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-24-25.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `4c87b8f2a847d6d4` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-applied-science-criminal-justice-and-public-safety-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/dallas-college/aas-criminal-justice-and-public-safety-to-baas-w-criminal-justice-concentration-25-26.pdf (sha256 53e135e3651c)
- issues: stale_year_label:2025-26
  - terms: 4 ⟵ “Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `4e4ca797bd5e924e` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-arts-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf (sha256 8fdab4b39fed)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/college-of-the-mainland/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf,https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-ba-criminal-justice-2025-2026.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `566c4cdd2a5f5469` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-arts-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/austin-community-college/aa-criminal-justice-ba-criminal-justice-2024-2025.pdf (sha256 9c420bebf61e)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `570dbe85b540ebf6` Sam Houston State University — degree_requirements 2024-25 · program_key=criminal-and-forensic-science-associate-of-applied-science-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/aas-criminal-and-forensic-science-to-baas-with-criminal-justice-concentration-24-25.pdf (sha256 26fc9e77bb5a)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `5b114a6e1cae01d9` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-applied-sciences-accounting-services-management-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/aas-accounting-services-management-to-baas-buad-conc-2024-2025.pdf (sha256 1683e8eb817d)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `69bc58c8c2d77912` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-arts-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lee-college/aa-to-bs-in-criminal-justice-25-26-lee-college.pdf (sha256 f6bc64782272)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/victoria-college/aa-to-bs-in-criminal-justice-2025-2026-victoria-college.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `6ab5f14ef411e2c7` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-field-of-study-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-homeland-security-studies-24-25.pdf (sha256 a23c5888388b)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-homeland-security-studies-24-25.pdf
  - terms: 9 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Second Year Summer | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `6b42652d908f682a` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-arts-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lee-college/aa-to-bs-criminal-justice-2024-2025.pdf (sha256 6e8ffc6e093d)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/austin-community-college/aa-criminal-justice-bs-criminal-justice-2024-2025.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `76b003e476cf070d` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-arts-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/austin-community-college/aa-criminal-justice-bs-criminal-justice-2024-2025.pdf (sha256 bc881eb71821)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/lee-college/aa-to-bs-criminal-justice-2024-2025.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `7ef2400284272ac1` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-arts-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/victoria-college/aa-to-bs-in-criminal-justice-2025-2026-victoria-college.pdf (sha256 4d54c48181b3)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/lee-college/aa-to-bs-in-criminal-justice-25-26-lee-college.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `849e52b1343e82f9` Sam Houston State University — degree_requirements 2025-26 · program_key=criminal-justice-associate-of-science-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/as-criminal-justice-to-ba-in-criminal-justice-25-26.pdf (sha256 1ff128a9a01c)
- issues: stale_year_label:2025-26
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `8638956cff4ef989` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-science-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lee-college/as-to-bs-comp-sci-25-26-lee-college.pdf (sha256 bab0e4a8d16f)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/lamar-institute-of-technology/as-criminal-justice-to-bs-in-criminal-justice-25-26.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `89baa17dfaf9d421` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-applied-science-homeland-security-and-emergency-management · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/central-texas-college/aas-homeland-security-emergency-management-to-baas-homeland-security-minor-2024-2025.pdf (sha256 91fc255cfbc1)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `8f7f7cf3fa283db2` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-health-sciences-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-human-performance-and-wellness-management-24-25.pdf (sha256 b2bba8d161af)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-care-administration-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-sciences-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-public-health-24-25.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `ae0065947c51b7b5` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-applied-science-emergency-management-and-homeland-security · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-institute-of-technology/aas-emergency-management-homeland-security-to-baas-homeland-security-minor-2024-2025.pdf (sha256 d225672ec2b7)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `be34eb3edfa96102` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-arts-field-of-study-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/aa-criminal-justice-fos-ba-criminal-justice-2025-2026.pdf (sha256 b377a5846553)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/aa-criminal-justice-fos-bs-criminal-justice-2025-2026.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `cdf9ec1a51d1e4f5` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lee-college/as-to-bs-comp-sci-24-25-lee-college.pdf (sha256 a11c6039908b)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `d00beb61662f17bb` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-applied-science-entrepreneurship-management-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/aas-entrepreneurship-management-to-baas-w-buad-conc-2024-2025.pdf (sha256 f8212b9d019f)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `d78cdd936e90848f` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-applied-science-social-work-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/alamo-colleges-district/aas-social-work-baas-victim-studies-minor-2024-2025.pdf (sha256 65c7a9d9591f)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `da47ee5ed5506b22` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-science-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-institute-of-technology/as-criminal-justice-to-bs-in-criminal-justice-25-26.pdf (sha256 9878a37b388f)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/lee-college/as-to-bs-comp-sci-25-26-lee-college.pdf
  - terms: 4 ⟵ “Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `dd332df64d9caba6` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-applied-science-business-management-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/lamar-state-college-orange/aas-management-to-baas-general-business-concentration-2024-2025.pdf (sha256 664dec7f18be)
- issues: stale_year_label:2024-25
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `dfbea49aff65218b` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-arts-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-ba-criminal-justice-2025-2026.pdf (sha256 2e74e7e5bac7)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/college-of-the-mainland/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf,https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `e465803dc3311e20` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-health-sciences-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-public-health-24-25.pdf (sha256 601e4ed2e46d)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-care-administration-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-health-sciences-24-25.pdf,https://www.shsu.edu/admissions/documents/angelina-college/as-health-sciences-to-bs-in-human-performance-and-wellness-management-24-25.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `e5e8fda7637d2c52` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-arts-field-of-study-in-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/dallas-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-25-26.pdf (sha256 a9232f59f3a2)
- issues: stale_year_label:2025-26
  - terms: 6 ⟵ “Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `eae66a8ed641244e` Sam Houston State University — degree_requirements 2025-26 · program_key=associate-of-arts-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/college-of-the-mainland/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf (sha256 ab4bdd821d5c)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-ba-criminal-justice-2025-2026.pdf,https://www.shsu.edu/admissions/documents/south-texas-college/aa-criminal-justice-to-bs-criminal-justice-2025-2026.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `ed174163f9ed3f07` Sam Houston State University — degree_requirements 2024-25 · program_key=associate-of-science-field-of-study-criminal-justice-to · requirement_key=four-year-plan [new] (labeled_in_title)
- source: https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-criminal-justice-24-25.pdf (sha256 5c1daa43e419)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-criminal-justice-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-ba-in-homeland-security-studies-24-25.pdf,https://www.shsu.edu/admissions/documents/houston-city-college/aa-criminal-justice-fos-to-bs-in-homeland-security-studies-24-25.pdf
  - terms: 8 ⟵ “First Year Fall | First Year Spring | Second Year Fall | Second Year Spring | Third Year Fall | Third Year Spring | Fourth Year Fall | Fourth Year Spring”
### `1a7faeb21d719c2a` San Antonio College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/maintaining/satisfactory-academic-progress/ (sha256 ec6b713bcba3)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.alamo.edu/49be5f/siteassets/district/departments/fin-aid/resources/checking-sap-status--submitting-an-appeal.pdf,https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/maintaining/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “How To Check Your SAP Status on ACES Submitting a SAP Appeal If you are placed on financial aid suspension, you have the option to submit an appeal to regain eligibility, recognizing that there may be circumstances that prevented you from meeting the minimum SAP standards.”
  - sentence: sap_appeal ⟵ “SAP Appeals | | Appeals Open | Appeals Close | Availability | Fall 2026 | Jun. 15, 2026 | Nov. 2, 2026 | Open | Spring 2027 | Nov. 3, 2026 | Apr. 1, 2027 | Upcoming Submission Steps First, meet with your Certified Academic Advisor to initiate your appeal.”
  - sentence: sap_appeal ⟵ “Submit Supporting Documents Processing Timeline The review time of a SAP appeal may take 3-4 weeks.”
  - sentence: sap_appeal ⟵ “If approved, SAP appeals allow financial aid eligibility to be renewed.”
  - sentence: sap_appeal ⟵ “If you are placed on financial aid suspension, you may submit a SAP appeal to regain financial aid eligibility for a future semester.”
  - sentence: sap_appeal ⟵ “Please note that SAP appeals are not guaranteed to be reviewed and/or approved before a payment deadline.”
### `30d3545f13915f50` San Antonio College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.alamo.edu/49be5f/siteassets/district/departments/fin-aid/resources/checking-sap-status--submitting-an-appeal.pdf (sha256 d2b396ad028f)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/maintaining/satisfactory-academic-progress/,https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/maintaining/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Checking Satisfactory Academic Progress (SAP) Status & Submitting an Appeal 1.”
  - sentence: sap_appeal ⟵ “If you do not meet SAP standards, you will have the opportunity to regain financial aid eligibility by completing the ‘SAP APPEAL‘ form linked below. 3 Reasons for not meeting SAP: • Below a 2.0 GPA • Complete less than 67% of all courses • Exceeded the maximum hours of your degree plan Note: You can only access the online SAP appeal after you have met with your certified advisor who initiates the”
### `46a39cf9976a3f6f` San Antonio College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/dates-and-priority-deadlines/ (sha256 de3f47190c24)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special & Unusual Circumstances Requests Time Frame to Submit: Requests must be submitted and processed before the last day of the term that you are enrolled in for the 2024-2025 academic year.”
### `75ba18d1564b6ffc` San Antonio College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/dates-and-priority-deadlines/ (sha256 de3f47190c24)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Program of Study (POS) Evaluation Automated Daily Evaluation: July 17 - October 26, 2026 Academic Advisor's Manual Evaluation Deadline: December 12, 2026 Satisfactory Academic Progress (SAP) Appeal Time Frame to Submit: June 15, 2026 - November 2, 2026 Special & Unusual Circumstances Requests Time Frame to Submit: Requests must be submitted and processed before the last day of the term that you ar”
  - sentence: sap_appeal ⟵ “Program of Study (POS) Evaluation Automated Daily Evaluation: October 28, 2025 - March 30, 2026 Academic Advisor's Evaluation Deadline: May 16, 2026 Satisfactory Academic Progress (SAP) Appeal Time Frame to Submit: November 3, 2025 - April 1, 2026 Special & Unusual Circumstances Requests Time Frame to Submit: Requests must be submitted and processed before the last day of the term that you are enr”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Time Frame to Submit: May 1, 2025 - November 1, 2025 Special & Unusual Circumstances Requests Time Frame to Submit: Requests must be submitted and processed before the last day of the term that you are enrolled in for the 2025-2026 academic year.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Time Frame to Submit: No Summer Appeal Process.”
### `a0d42118d6f19b4e` San Antonio College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/maintaining/satisfactory-academic-progress/ (sha256 23f0ce3d3497)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.alamo.edu/49be5f/siteassets/district/departments/fin-aid/resources/checking-sap-status--submitting-an-appeal.pdf,https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/maintaining/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “How To Check Your SAP Status on ACES Submitting a SAP Appeal If you are placed on financial aid suspension, you have the option to submit an appeal to regain eligibility, recognizing that there may be circumstances that prevented you from meeting the minimum SAP standards.”
  - sentence: sap_appeal ⟵ “SAP Appeals | | Appeals Open | Appeals Close | Availability | Fall 2026 | Jun. 15, 2026 | Nov. 2, 2026 | Open | Spring 2027 | Nov. 3, 2026 | Apr. 1, 2027 | Upcoming Submission Steps First, meet with your Certified Academic Advisor to initiate your appeal.”
  - sentence: sap_appeal ⟵ “Submit Supporting Documents Processing Timeline The review time of a SAP appeal may take 3-4 weeks.”
  - sentence: sap_appeal ⟵ “If approved, SAP appeals allow financial aid eligibility to be renewed.”
  - sentence: sap_appeal ⟵ “If you are placed on financial aid suspension, you may submit a SAP appeal to regain financial aid eligibility for a future semester.”
  - sentence: sap_appeal ⟵ “Please note that SAP appeals are not guaranteed to be reviewed and/or approved before a payment deadline.”
### `cd969ab6fea32355` San Antonio College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.alamo.edu/foundation/scholarships/ (sha256 e794fad4255d)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Please complete the Scholarship Appeal Form.”
### `55cc14f87be87b8a` San Antonio College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/cost/ (sha256 683d4fa5a97c)
- issues: shared_site_attribution_review
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees: 3412 ⟵ “Tuition and Fees | $3,412 | $3,412”
  - with_parents_or_family:Housing and Food: 7836 ⟵ “Housing and Food | $7,836 | $14,252”
  - with_parents_or_family:Books, Course Materials, Supplies, and Equipment: 500 ⟵ “Books, Course Materials, Supplies, and Equipment | $500 | $500”
  - with_parents_or_family:Transportation: 2904 ⟵ “Transportation | $2,904 | $2,904”
  - with_parents_or_family:Personal and Miscellaneous: 2802 ⟵ “Personal and Miscellaneous | $2,802 | $2,802”
  - with_parents_or_family:Total Estimated Costs:: 17454 ⟵ “Total Estimated Costs: | $17,454 | $23,870”
  - off_campus_not_with_family:Tuition and Fees: 3412 ⟵ “Tuition and Fees | $3,412 | $3,412”
  - off_campus_not_with_family:Housing and Food: 14252 ⟵ “Housing and Food | $7,836 | $14,252”
  - off_campus_not_with_family:Books, Course Materials, Supplies, and Equipment: 500 ⟵ “Books, Course Materials, Supplies, and Equipment | $500 | $500”
  - off_campus_not_with_family:Transportation: 2904 ⟵ “Transportation | $2,904 | $2,904”
  - off_campus_not_with_family:Personal and Miscellaneous: 2802 ⟵ “Personal and Miscellaneous | $2,802 | $2,802”
  - off_campus_not_with_family:Total Estimated Costs:: 23870 ⟵ “Total Estimated Costs: | $17,454 | $23,870”
### `632e7ed9c86702fc` San Antonio College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.alamo.edu/admission--aid/paying-for-college/financial-aid/cost/ (sha256 683d4fa5a97c)
- issues: shared_site_attribution_review
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees: 9952 ⟵ “Tuition and Fees | $9,952 | $9,952”
  - with_parents_or_family:Housing and Food: 7836 ⟵ “Housing and Food | $7,836 | $14,252”
  - with_parents_or_family:Books, Course Materials, Supplies, and Equipment: 500 ⟵ “Books, Course Materials, Supplies, and Equipment | $500 | $500”
  - with_parents_or_family:Transportation: 2904 ⟵ “Transportation | $2,904 | $2,904”
  - with_parents_or_family:Personal and Miscellaneous: 2802 ⟵ “Personal and Miscellaneous | $2,802 | $2,802”
  - with_parents_or_family:Total Estimated Costs:: 23994 ⟵ “Total Estimated Costs: | $23,994 | $30,410”
  - off_campus_not_with_family:Tuition and Fees: 9952 ⟵ “Tuition and Fees | $9,952 | $9,952”
  - off_campus_not_with_family:Housing and Food: 14252 ⟵ “Housing and Food | $7,836 | $14,252”
  - off_campus_not_with_family:Books, Course Materials, Supplies, and Equipment: 500 ⟵ “Books, Course Materials, Supplies, and Equipment | $500 | $500”
  - off_campus_not_with_family:Transportation: 2904 ⟵ “Transportation | $2,904 | $2,904”
  - off_campus_not_with_family:Personal and Miscellaneous: 2802 ⟵ “Personal and Miscellaneous | $2,802 | $2,802”
  - off_campus_not_with_family:Total Estimated Costs:: 30410 ⟵ “Total Estimated Costs: | $23,994 | $30,410”
### `2eae52d95af6da18` San Jacinto Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/ (sha256 2a09aefa7ba4)
- issues: semantic_review_required, conflicting_sources:https://www.sanjac.edu/admissions/paying-for-college/financial-aid/faqs/,https://www.sanjac.edu/admissions/paying-for-college/financial-aid/managing-your-aid/sap/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/career-and-tech/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/perkins/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Perkins Grant Every year, San Jacinto College awards Perkins grants to students in special circumstances to help them pay for costs associated with career and technical education programs.”
### `3cd1ac93b34cde97` San Jacinto Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/perkins/ (sha256 0f0cb8e7a5dc)
- issues: semantic_review_required, conflicting_sources:https://www.sanjac.edu/admissions/paying-for-college/financial-aid/faqs/,https://www.sanjac.edu/admissions/paying-for-college/financial-aid/managing-your-aid/sap/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/career-and-tech/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Every year, San Jacinto College awards Perkins grants to students in special circumstances, helping them pay for costs associated with career and technical education programs.”
  - sentence: need_based_special_circumstances ⟵ “Perkins grants help students in unique or special circumstances.”
### `43938c0c6c0e5eef` San Jacinto Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sanjac.edu/admissions/paying-for-college/financial-aid/managing-your-aid/sap/ (sha256 d98e0c084a23)
- issues: semantic_review_required, conflicting_sources:https://www.sanjac.edu/admissions/paying-for-college/financial-aid/applying-for-aid/,https://www.sanjac.edu/admissions/paying-for-college/financial-aid/faqs/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If there were justifiable reasons or extenuating circumstances that impacted your ability to meet the GPA or pass rate requirements, you may submit a SAP appeal (with supporting documentation) to the financial aid office for consideration to regain financial aid eligibility.”
  - sentence: sap_appeal ⟵ “SAP appeals are reviewed on a case-by-case basis for sufficient explanation of extenuating circumstance and supporting documentation.”
### `5452af5369a3733c` San Jacinto Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sanjac.edu/admissions/paying-for-college/financial-aid/applying-for-aid/ (sha256 6bc928b5207d)
- issues: semantic_review_required, conflicting_sources:https://www.sanjac.edu/admissions/paying-for-college/financial-aid/faqs/,https://www.sanjac.edu/admissions/paying-for-college/financial-aid/managing-your-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “You can learn more about SAP and the appeals process on the SAP page.”
### `670709149f56796f` San Jacinto Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sanjac.edu/admissions/paying-for-college/financial-aid/managing-your-aid/sap/ (sha256 d98e0c084a23)
- issues: semantic_review_required, conflicting_sources:https://www.sanjac.edu/admissions/paying-for-college/financial-aid/faqs/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/career-and-tech/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/perkins/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Successfully completing a semester can help when reapplying, but special circumstances are considered for GPA and completion rate measurements.”
### `c3872cefa3182941` San Jacinto Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sanjac.edu/admissions/paying-for-college/financial-aid/faqs/ (sha256 5933769876c2)
- issues: semantic_review_required, conflicting_sources:https://www.sanjac.edu/admissions/paying-for-college/financial-aid/managing-your-aid/sap/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/career-and-tech/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/perkins/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “If the FAFSA determines that you are dependent (parental information on the FAFSA) for financial aid purposes, but you have unusual circumstances, please contact the financial aid office or complete the unusual circumstances form.”
  - sentence: need_based_special_circumstances ⟵ “You may submit a request for Special Circumstances with appropriate supporting documentation What happens if I defer or change my schedule?”
  - sentence: need_based_special_circumstances ⟵ “Contact the financial aid office for guidance on appeals or special circumstances.”
### `d133977e1849b039` San Jacinto Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sanjac.edu/admissions/paying-for-college/financial-aid/faqs/ (sha256 5933769876c2)
- issues: semantic_review_required, conflicting_sources:https://www.sanjac.edu/admissions/paying-for-college/financial-aid/applying-for-aid/,https://www.sanjac.edu/admissions/paying-for-college/financial-aid/managing-your-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If your financial situation changes or you fail to meet SAP standards, you may appeal for reconsideration.”
### `d17c2f8dc8f91ce0` San Jacinto Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/career-and-tech/ (sha256 0bc50ec92a49)
- issues: semantic_review_required, conflicting_sources:https://www.sanjac.edu/admissions/paying-for-college/financial-aid/faqs/,https://www.sanjac.edu/admissions/paying-for-college/financial-aid/managing-your-aid/sap/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/,https://www.sanjac.edu/admissions/paying-for-college/grants-scholarships/grants/perkins/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Perkins Grant Funding Opportunities Every year, San Jacinto College provides Perkins grants to support students with unique or special circumstances complete technical education programs.”
### `b6976834212b7093` San Jacinto Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.sanjac.edu/admissions/testing/clep/ (sha256 ac6346b87f9c)
- issues: rows_without_score
- checks: {"distinct_exams": 18, "equivalencies": 21, "rows_without_score": 21}
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | ENGL 1301 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “American Literature | ENGL 2327 & ENGL 2328 | 6”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature | ENGL 2322 & ENGL 2323 | 6”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “College Algebra | MATH 1314 | 3”
  - equivalencies[CLEP-CHEMISTRY|None]:  ⟵ “Chemistry | CHEM 1311/CHEM 1111 | 4”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | MATH 2413 | 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|None]:  ⟵ “French | FREN 2311/FREN 2312 | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|None]:  ⟵ “French | FREN 1411/FREN 1412 | 8”
  - equivalencies[CLEP-GERMAN-LANGUAGE|None]:  ⟵ “German | GERM 2311/GERM 2312 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|None]:  ⟵ “German | GERM 1411/GERM 1412 | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “Spanish | SPAN 2311/SPAN 2312 | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “Spanish | SPAN 1411/SPAN 1412 | 8”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “American Government | GOVT 2305 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “Principles of Macroeconomics | ECON 2301 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | ECON 2302 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introductory Psychology | PSYC 2301 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Introductory Sociology | SOCI 1301 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|None]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | HIST 2311 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|None]:  ⟵ “Western Civilization II: 1648 to Present | HIST 2312 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|None]:  ⟵ “Financial Accounting | ACCT 2301 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “Introductory Business Law | BUSI 2301 | 3”
### `7bcb235f34d21cab` Tarleton State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tarleton.edu/finaid/student_aid_index/ (sha256 d651b17ab41e)
- issues: semantic_review_required, conflicting_sources:https://www.tarleton.edu/finaid/special-circumstances-appeals/,https://www.tarleton.edu/finaid/unusual-circumstance-appeal/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If your SAI is -1500 to 0, you have already been offered the maximum amount of aid you are eligible to receive and should not file a Special Circumstance Appeal.”
### `8bd4ad7a89641318` Tarleton State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tarleton.edu/finaid/special-circumstances-appeals/ (sha256 5c6122a1f6b1)
- issues: semantic_review_required, conflicting_sources:https://www.tarleton.edu/finaid/student_aid_index/,https://www.tarleton.edu/finaid/unusual-circumstance-appeal/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Read More Unusual Circumstance Appeal The Unusual Circumstance Appeal allows students who indicated “yes” to the Student Unusual Circumstance question on the FAFSA to have their dependency status formally reviewed by the financial aid office.”
### `8ce254749cc0a0a7` Tarleton State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tarleton.edu/finaid/unusual-circumstance-appeal/ (sha256 c58c8e83697d)
- issues: semantic_review_required, conflicting_sources:https://www.tarleton.edu/finaid/special-circumstances-appeals/,https://www.tarleton.edu/finaid/student_aid_index/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “This designation means that you are not required to provide parental information on your FAFSA; however, the institution is required to review your circumstance to make a formal determination on your dependency status through an Unusual Circumstance Appeal.”
### `271135c66a2068f7` Tarleton State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tarleton.edu/finaid/cost/undergraduate/ (sha256 7db1f9c443f7)
- issues: residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition and Fees: 10181.0 ⟵ “Tuition and Fees | $10,181.00 | $10,181.00 | $10,181.00”
  - on_campus:Books and Supplies: 1560.0 ⟵ “Books and Supplies | $1,560.00 | $1,560.00 | $1,560.00”
  - on_campus:Housing: 7012.0 ⟵ “Housing | $7,012.00 | $8,840.00 | $1,946.00”
  - on_campus:Food: 5282.0 ⟵ “Food | $5,282.00 | $5,282.00 | $5,282.00”
  - on_campus:Transportation: 1544.0 ⟵ “Transportation | $1,544.00 | $1,544.00 | $1,544.00”
  - on_campus:Personal: 2493.0 ⟵ “Personal | $2,493.00 | $2,493.00 | $2,493.00”
  - on_campus:Loan Fees: 44.0 ⟵ “Loan Fees | $44.00 | $44.00 | $44.00”
  - on_campus:Total ($): 28116.0 ⟵ “Total ($) | $28,116.00 | $29,944.00 | $23,050.00”
  - off_campus_not_with_family:Tuition and Fees: 10181.0 ⟵ “Tuition and Fees | $10,181.00 | $10,181.00 | $10,181.00”
  - off_campus_not_with_family:Books and Supplies: 1560.0 ⟵ “Books and Supplies | $1,560.00 | $1,560.00 | $1,560.00”
  - off_campus_not_with_family:Housing: 8840.0 ⟵ “Housing | $7,012.00 | $8,840.00 | $1,946.00”
  - off_campus_not_with_family:Food: 5282.0 ⟵ “Food | $5,282.00 | $5,282.00 | $5,282.00”
  - off_campus_not_with_family:Transportation: 1544.0 ⟵ “Transportation | $1,544.00 | $1,544.00 | $1,544.00”
  - off_campus_not_with_family:Personal: 2493.0 ⟵ “Personal | $2,493.00 | $2,493.00 | $2,493.00”
  - off_campus_not_with_family:Loan Fees: 44.0 ⟵ “Loan Fees | $44.00 | $44.00 | $44.00”
  - off_campus_not_with_family:Total ($): 29944.0 ⟵ “Total ($) | $28,116.00 | $29,944.00 | $23,050.00”
  - with_parents_or_family:Tuition and Fees: 10181.0 ⟵ “Tuition and Fees | $10,181.00 | $10,181.00 | $10,181.00”
  - with_parents_or_family:Books and Supplies: 1560.0 ⟵ “Books and Supplies | $1,560.00 | $1,560.00 | $1,560.00”
  - with_parents_or_family:Housing: 1946.0 ⟵ “Housing | $7,012.00 | $8,840.00 | $1,946.00”
  - with_parents_or_family:Food: 5282.0 ⟵ “Food | $5,282.00 | $5,282.00 | $5,282.00”
  - with_parents_or_family:Transportation: 1544.0 ⟵ “Transportation | $1,544.00 | $1,544.00 | $1,544.00”
  - with_parents_or_family:Personal: 2493.0 ⟵ “Personal | $2,493.00 | $2,493.00 | $2,493.00”
  - with_parents_or_family:Loan Fees: 44.0 ⟵ “Loan Fees | $44.00 | $44.00 | $44.00”
  - with_parents_or_family:Total ($): 23050.0 ⟵ “Total ($) | $28,116.00 | $29,944.00 | $23,050.00”
### `4743708dc189a58c` Tarleton State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.tarleton.edu/admissions/tsi/ (sha256 4380119a3e78)
- issues: course_column_missing, conflicting_sources:https://catalog.tarleton.edu/admissions/,https://www.tarleton.edu/admissions/course-credit/
- checks: {"distinct_exams": 7, "equivalencies": 7, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “CLEP – American Government |  | 50 | ”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “CLEP – College Composition |  | 50 | 50”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “CLEP – Introductory Psychology |  | 50 | 50”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “CLEP – U.S. History I |  | 50 | ”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “CLEP – U.S. History II |  | 50 | ”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “CLEP – Western Civilization I |  | 50 | ”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “CLEP – Western Civilization II |  | 50 | ”
### `97ae1cdfd6e1932c` Tarleton State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.tarleton.edu/admissions/course-credit/ (sha256 410e05173dc9)
- issues: conflicting_sources:https://catalog.tarleton.edu/admissions/,https://www.tarleton.edu/admissions/tsi/
- checks: {"distinct_exams": 23, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “General Biology | 50 | BIOL 1406: General Biology | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “General Chemistry | 50 | CHEM 1411: General Chemistry I | 4”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | BCIS 1305: Business Computer App. | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics | 50 | ECON 2301: Princ of Economics | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECON 2302: Princ of Economics | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “College French | 50 | FREN 1411 & 1412: Beginning French | 8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|66]:  ⟵ “College French | 66 | FREN 1411, 1412, 2311 & 2312: Beginning & Inter. French | 14”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Intro Business Law | 50 | BUSI 2301: Business Law | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “College German | 50 | GERM 1411, 1412 Beginning German | 8”
  - equivalencies[CLEP-GERMAN-LANGUAGE|66]:  ⟵ “College German | 66 | 1411, 1412, 2311, 2312 Beginning & Inter. German | 14”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Govt | 50 | GOVT 2305: American Govt | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 50 | HIST 2321: World Civilizations I | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II | 50 | HIST 2322: World Civilizations II | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “U.S. History I | 50 | HIST 1301: History of US I | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “U.S. History II | 50 | HIST 1302: History of the US II | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 1314: College Algebra | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MATH 2412: PreCalculus | 4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH 2413: Calculus I | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | MGMT 2301: Principles of Management | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | MKTG 2314: Marketing | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSYC 2301: General Psychology | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOCI 1301: Intro to Sociology | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “College Spanish | 50 | SPAN 1411 & 1412: Beginning Spanish | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|66]:  ⟵ “College Spanish | 66 | SPAN 1411, 1412, 2311 & 2312: Beginning and Inter. Spanish | 14”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | English 1301 & English 1302 | 6”
  - … 1 more rows
### `9a2ecef0a18ae6b0` Tarleton State University — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_heading)
- source: https://catalog.tarleton.edu/admissions/ (sha256 5430aff5bea0)
- issues: conflicting_sources:https://www.tarleton.edu/admissions/course-credit/,https://www.tarleton.edu/admissions/tsi/
- checks: {"distinct_exams": 23, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “BIOL 1406: General Biology | CL01 | CLP Examination | General Biology | 50 | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “CHEM 1411: General Chemistry I | CL02 | CLP Examination | General Chemistry | 50 | 4”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “BCIS 1305: Business Computer App. | CL03 | CLP Examination | Information Systems & Computer Applications | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “ECON 2301: Princ of Economics | CL04 | CLP Examination | Macroeconomics | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “ECON 2302: Princ of Economics | CL05 | CLP Examination | Principles of Microeconomics | 50 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “ENGL 1301 & 1302: College Composition | CL31 | CLP Examination | College Composition | 50 | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “FREN 1411 & 1412: Beginning French | CL76 | CLP Examination | College French | 50 | 8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|66]:  ⟵ “FREN 1411, 1412, 2311 & 2312: Beginning & Inter. French | CL76 | CLP Examination | College French | 66 | 14”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “BLAW 4332: Business Law | CL08 | CLP Examination | Intro Business Law | 50 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “GERM 1411 & 1412: Beginning German | CL75 | CLP Examination | German Language | 50 | 8”
  - equivalencies[CLEP-GERMAN-LANGUAGE|66]:  ⟵ “GERM 1411, 1412, 2311 & 2312: Beginning & Inter. German | CL75 | CLP Examination | College German | 66 | 14”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “GOVT 2305: American Govt | CL10 | CLP Examination | American Govt | 50 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “HIST 2321: Worl History | CL11 | CLP Examination | Western Civilization I | 50 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “HIST 2322: World History | CL12 | CLP Examination | Western Civilization II | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “HIST 1301: History of US I | CL13 | CLP Examination | U.S. History I | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “HIST 1302: History of the US II | CL14 | CLP Examination | U.S. History II | 50 | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “MATH 1314: College Algebra | CL16 | CLP Examination | College Algebra | 50 | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “MATH 1332: Contemporary Mathematics I | CL 32 | CLP Examination | College Mathematics | 50 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “MATH 2412: PreCalculus | CL29 | CLP Examination | Precalculus | 50 | 4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “MATH 2413: Calculus I | CL18 | CLP Examination | Calculus | 50 | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “MGMT 2301: Principles of Management | CL19 | CLP Examination | Principles of Management | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “MKTG 2314: Marketing | CL20 | CLP Examination | Principles of Marketing | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “PSYC 2301: General Psychology | CL21 | CLP Examination | Introductory Psychology | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “SOCI 1301: Intro to Sociology | CL22 | CLP Examination | Introductory Sociology | 50 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “SPAN 1411 & 1412: Beginning Spanish | CL77 | CLP Examination | College Spanish | 50 | 8”
  - … 1 more rows
### `ac995d42ada611c0` Tarleton State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.tarleton.edu/admissions/course-credit/ (sha256 410e05173dc9)
- issues: rows_without_score, conflicting_sources:https://catalog.tarleton.edu/admissions/
- checks: {"distinct_exams": 17, "equivalencies": 23, "rows_without_score": 23}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | 5, 6, 7 | BIOL 1406, 1407 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business & Org. | 5, 6, 7 | FINC 3301, MGMT 3301 | 6”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | 5, 6, 7 | CHEM 1411, 1412 | 8”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | 5, 6, 7 | ECON 2301, 2302 | 6”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French | 5 | FREN 1411, 1412 | 8”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French | 6, 7 | FREN 1411, 1412, 2311, 2312 | 14”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | 5, 6, 7 | GEOG 1303 | 3”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German | 5 | GERM 1411, 1412 | 8”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German | 6, 7 | GERM 1411, 1412, 2311, 2312 | 14”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History, U.S. | 5, 6, 7 | HIST 1301, 1302 | 6”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | 5, 6, 7 | MUSI 1311, 1312 | 5”
  - equivalencies[IB-PHILOSOPHY|None]:  ⟵ “Philosophy | 5, 6, 7 | PHIL 1301 | 3”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Physics | 5, 6, 7 | PHYS 1401, 1402 | 8”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | 5, 6, 7 | PSYC 2301 | 3”
  - equivalencies[IB-SPANISH|None]:  ⟵ “Spanish | 5 | SPAN 1411, 1412 | 8”
  - equivalencies[IB-SPANISH|None]:  ⟵ “Spanish | 6, 7 | SPAN 1411, 1412, 2311, 2312 | 14”
  - equivalencies[IB-THEATRE|None]:  ⟵ “Theatre Arts | 5, 6, 7 | DRAM 1310 | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|None]:  ⟵ “Mathematics - Analysis & Approaches | 5, 6, 7 | MATH 2413, 1325 | 4”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|None]:  ⟵ “Mathematics - Analysis & Approaches | 4 | MATH 2413, 1324 | 4”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|None]:  ⟵ “Mathematics - Applications & Interpretations | 5, 6, 7 | MATH 2413, 1325 | 4”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|None]:  ⟵ “Mathematics - Applications & Interpretations | 4 | MATH 2412, 1324 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | 6, 7 | BCIS 1305 | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|None]:  ⟵ “Mathematics - Analysis & Approaches | 4, 5 | MATH 2412, 1324 | 4”
### `b75d506c78436a8b` Tarleton State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.tarleton.edu/admissions/course-credit/ (sha256 410e05173dc9)
- issues: conflicting_sources:https://catalog.tarleton.edu/admissions/
- checks: {"distinct_exams": 22, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “ARTS 1303 Art History I | AP01 | Advanced Placement | Art History | 3 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “BIOL 1406 General Biology | AP02 | Advanced Placement | Biology | 3 | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “CHEM 1411 General Chemisty I | AP35 | Advanced Placement | Chemistry | 3 | 4”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “CHEM 1411 & 1412 General Chem.I &II | AP35 | Advanced Placement | Chemistry | 4 or 5 | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “BCIS 1305 Business Computer App. | AP28 | Advanced Placement | Computer Science A | 3 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “ECON 2301 Princ of Economics | AP31 | Advanced Placement | Macroeconomics | 3 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “ECON 2302 Princ of Economics | AP30 | Advanced Placement | Microeconomics | 3 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|2]:  ⟵ “FREN 1411 | AP97 | Advanced Placement | French Lang Culture | 2 | 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “FREN 1411, 1412 | AP97 | Advanced Placement | French Lang Culture | 3 | 8”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “FREN 1411,1412,2311 | AP97 | Advanced Placement | French Lang Culture | 4 | 11”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “FREN 1411,1412,2311,2312 | AP97 | Advanced Placement | French Lang Culture | 5 | 14”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “GEOL 1407 Intro to Environmental Sci. | AP26 | Advanced Placement | Environmental Science | 3 | 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|2]:  ⟵ “GERM 1411 | AP98 | Advanced Placement | German Lang Culture | 2 | 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “GERM 1411,1412 | AP98 | Advanced Placement | German Lang Culture | 3 | 8”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “GERM 1411,1412,2311 | AP98 | Advanced Placement | German Lang Culture | 4 | 11”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “GERM 1411,1412,2311,2312 | AP98 | Advanced Placement | German Lang Culture | 5 | 14”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “HIST 2321 World History | AP56 | Advanced Placement | World History | 3 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4 or 5]:  ⟵ “HIST 2321 & 2322 World History | AP56 | Advanced Placement | World History | 4 or 5 | 6”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “HIST 2321 & 2322 World History | AP11 | Advanced Placement | European History | 3 | 6”
  - equivalencies[AP-PSYCHOLOGY|4]:  ⟵ “PSYC 2301 | AP40 | Advanced Placement | Psychology | 4 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “HIST 1301 &1302 History of the US | AP12 | Advanced Placement | US History | 3 | 6”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “MATH 2413 Calculus I | AP13 | Advanced Placement | Calculus AB | 4 or 5 | 4”
  - equivalencies[AP-CALCULUS-BC|3 & #4]:  ⟵ “MATH 2413 Calculus I | AP38 | Advanced Placement | Calculus BC & Absub-score | 3 & #4 | 4”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “MATH 2414 & MATH 2413 | AP33 | Advanced Placement | Calculus II (Calculus BC) | 4 or 5 | 8”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Math 2412 | AP39 | Advanced Placement | PreCalculus 2412 | 4 | 4”
  - … 9 more rows
### `bc58dd57fc469fd2` Tarleton State University — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_heading)
- source: https://catalog.tarleton.edu/admissions/ (sha256 5430aff5bea0)
- issues: score_scale_mismatch, conflicting_sources:https://www.tarleton.edu/admissions/course-credit/
- checks: {"distinct_exams": 17, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|8]:  ⟵ “Biology | 5, 6,7 | BIOL 1406, 1407 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|6]:  ⟵ “Business & Org. | 5, 6, 7 | FINC 3301, MGMT 3301 | 6”
  - equivalencies[IB-CHEMISTRY|8]:  ⟵ “Chemistry | 5, 6, 7 | CHEM 1411, 1402 | 8”
  - equivalencies[IB-ECONOMICS|6]:  ⟵ “Economics | 5, 6, 7 | ECON 2301, 2302 | 6”
  - equivalencies[IB-FRENCH|8]:  ⟵ “French | 5 | FREN 1411, 1412 | 8”
  - equivalencies[IB-FRENCH|14]:  ⟵ “French | 6, 7 | FREN 1411, 1412, 2311, 2312 | 14”
  - equivalencies[IB-GEOGRAPHY|3]:  ⟵ “Geography | 5, 6, 7 | GEOG 1303 | 3”
  - equivalencies[IB-GERMAN|8]:  ⟵ “German | 5 | GERM 1411, 1412 | 8”
  - equivalencies[IB-GERMAN|14]:  ⟵ “German | 6, 7 | GERM 1411, 1412, 2311, 2312 | 14”
  - equivalencies[IB-HISTORY|6]:  ⟵ “History, U.S. | 5, 6, 7 | HIST 1301, 1302 | 6”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4 or 3]:  ⟵ “Math-Analysis & Approaches | 4 | MATH 2412 or MATH 1324 | 4 or 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4 or 3]:  ⟵ “Math-Analysis & Approaches | 5, 6, 7 | MATH 2413 or MATH 1325 | 4 or 3”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|4 or 3]:  ⟵ “Math-Applications & Interpretations | 4 | MATH 2412 or MATH 1324 | 4 or 3”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|4 or 3]:  ⟵ “Math-Applications & Interpretations | 5, 6, 7 | MATH 2413 or MATH 1325 | 4 or 3”
  - equivalencies[IB-MUSIC|5]:  ⟵ “Music | 5, 6, 7 | MUSI 1311, 1312 | 5”
  - equivalencies[IB-PHILOSOPHY|3]:  ⟵ “Philosophy | 5, 6, 7 | PHIL 1301 | 3”
  - equivalencies[IB-PHYSICS|8]:  ⟵ “Physics | 5, 6, 7 | PHYS 1401, 1402 | 8”
  - equivalencies[IB-PSYCHOLOGY|3]:  ⟵ “Psychology | 5, 6, 7 | PSYC 2301 | 3”
  - equivalencies[IB-SPANISH|8]:  ⟵ “Spanish | 5 | SPAN 1411, 1412 | 8”
  - equivalencies[IB-SPANISH|14]:  ⟵ “Spanish | 6, 7 | SPAN 1411, 1412, 2311, 2312 | 14”
  - equivalencies[IB-THEATRE|3]:  ⟵ “Theatre Arts | 5, 6, 7 | DRAM 1310 | 3”
  - equivalencies[IB-CHEMISTRY|8]:  ⟵ “Chemistry | 6, 7 | CHEM 1411, 1412 | 8”
  - equivalencies[IB-COMPUTER-SCIENCE|3]:  ⟵ “Computer Science | 6, 7 | BCIS 1305 | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4 or 3]:  ⟵ “Math-Analysis & Approaches | 4, 5 | MATH 2412 or Math 1324 | 4 or 3”
  - equivalencies[IB-MUSIC|6]:  ⟵ “Music | 7 | MUSI 1311, 1312 | 6”
### `c79d99be02da51aa` Tarleton State University — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_heading)
- source: https://catalog.tarleton.edu/admissions/ (sha256 5430aff5bea0)
- issues: conflicting_sources:https://www.tarleton.edu/admissions/course-credit/
- checks: {"distinct_exams": 21, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “BIOL 1406: General Biology | AP02 | Advanced Placement | Biology | 3 | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “CHEM 1411: General Chemistry I | AP35 | Advanced Placement | Chemistry | 3 | 4”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “CHEM 1411 & 1412: General Chemistry I & II | AP35 | Advanced Placement | Chemistry | 4 or 5 | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “BCIS 1305: Business Computer App. | AP04 | Advanced Placement | Computer Science A or AB | 3 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “ECON 2301: Princ of Economics | AP31 | Advanced Placement | Macroeconomics | 3 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “ECON 2302: Princ of Economics | AP30 | Advanced Placement | Microeconomics | 3 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|2]:  ⟵ “FREN 1411 Beginning French | AP97 | Advanced Placement | French Language & Culture | 2 | 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “FREN 1411 & 1412 Beginning French | AP97 | Advanced Placement | French Language & Culture | 3 | 8”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “FREN 1411, 1412, & 2311 Beginning & Inter. French | AP97 | Advanced Placement | French Language & Culture | 4 | 11”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “FREN 1411, 1412, 2311, & 2312 Beginning & Inter. French | AP97 | Advanced Placement | French Language & Culture | 5 | 14”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “GEOL 1407: Intro to Environmental Science | AP26 | Advanced Placement | Environmental Science | 3 | 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|2]:  ⟵ “GERM 1411 Beginning German | AP98 | Advanced Placement | German Language& Culture | 2 | 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “GERM 1411 & 1412 Beginning German | AP98 | Advanced Placement | German Language& Culture | 3 | 8”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “GERM 1411, 1412 &, 2311 Beginning & Inter. German | AP98 | Advanced Placement | German Language& Culture | 4 | 11”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “GERM 1411, 1412, 2311 & 2312 Beginning & Inter. German | AP98 | Advanced Placement | German Language& Culture | 5 | 14”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “HIST 2321: World History | AP56 | Advanced Placement | World History | 3 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4 or 5]:  ⟵ “HIST 2321 & 2322: World History | AP56 | Advanced Placement | World History | 4 or 5 | 6”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “HIST 2321 & 2322: World History | AP11 | Advanced Placement | European History | 3 | 6”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “HIST 1301 & 1302: History of the US | AP12 | Advanced Placement | American/US History | 3 | 6”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “MATH 2412: Pre-Calculus | AP39 | Advanced Placement | Pre-Calculus | 4 | 4”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “MATH 2413: Calculus I | AP13 | Advanced Placement | Calculus AB | 4 or 5 | 4”
  - equivalencies[AP-CALCULUS-BC|3 and AB Sub-score 4]:  ⟵ “MATH 2413: Calculus I | AP38 | Advanced Placement | Calculus BC | 3 and AB Sub-score 4 | 4”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “MATH 2413, MATH 2414 Calculus I & II | AP33 | Advanced Placement | Calculus BC | 4 or 5 | 8”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “MATH 1342: Statistics | AP34 | Advanced Placement | Statistics | 3 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “MUSC 1311: Music Theory | AP32 | Advanced Placement | Music Theory | 3 | 3”
  - … 8 more rows
### `3a9f2117808af7ae` Texas A & M University-College Station — appeals 2027-28 [new] (labeled_in_source)
- source: https://catalog.tamu.edu/undergraduate/tuition-fees-financial-information/financial-assistance-scholarships/ (sha256 2945bcbc7cf8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “On a case-by-case basis, work study can be offered to students who are enrolled less than half-time through professional judgment.”
### `ec8556afdd64be23` Texas A & M University-College Station — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.tamu.edu/undergraduate/tuition-fees-financial-information/financial-assistance-scholarships/financial-assistance-scholarships.pdf (sha256 a9d75561d3c0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “On a case-by-case basis, work study can be offered to students who are enrolled less than half-time through professional judgment.”
### `41881cb0ee341f0d` Texas A & M University-College Station — credit_policies 2027-28 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.tamu.edu/undergraduate/general-information/admission/ (sha256 7b477134c2ce)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 39, "equivalencies": 40, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | AFST 289 | 3”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “AP Pre-Calculus | 3 | MATH 102 | 3”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research | 3 | See academic advisor | up to 3 hours”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar | 3 | See academic advisor | up to 3 hours”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTS 149 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 113 | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH 142 | 3”
  - equivalencies[AP-CALCULUS-BC|31]:  ⟵ “Calculus BC | 31 | MATH 151 | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 119 | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | 3 | CHIN 101, CHIN 102 | 8”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Governments | 3 | POLS 229 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CSCE 110 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | CSCE 110 | 4”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macroeconomics | 3 | ECON 203 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Microeconomics | 3 | ECON 202 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Lang. and Comp. | 3 | ENGL 104 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Lit. and Comp. | 3 | ENGL 104 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENSS 105 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 102 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | FREN 101, FREN 102 | 8”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | GERM 101, GERM 102 | 8”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 201 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language | 3 | ITAL 101, ITAL 102 | 8”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language | 3 | JAPN 101, JAPN 102 | 8”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | 3 | CLAS 121, CLAS 122 | 8”
  - … 15 more rows
### `e090636e6f7ab574` Texas A & M University-College Station — credit_policies 2027-28 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.tamu.edu/undergraduate/general-information/admission/ (sha256 7b477134c2ce)
- issues: score_column_not_scores
- checks: {"distinct_exams": 37, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-SL|Biology SL]:  ⟵ “Biology SL | 4 | BIOL 113 | 3”
  - equivalencies[IB-BIOLOGY-HL|Biology HL]:  ⟵ “Biology HL | 4 | BIOL 111 | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|Business Management SL]:  ⟵ “Business Management SL | 4 | MGMT 309 | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|Business Management HL]:  ⟵ “Business Management HL | 4 | MGMT 309 | 3”
  - equivalencies[IB-CHEMISTRY-SL|Chemistry SL]:  ⟵ “Chemistry SL | 4 | CHEM 106/CHEM 116 | 4”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry HL]:  ⟵ “Chemistry HL | 4 | CHEM 119 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|Computer Science SL]:  ⟵ “Computer Science SL | 4 | CSCE 111 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|Computer Science HL]:  ⟵ “Computer Science HL | 4 | CSCE 111 | 4”
  - equivalencies[IB-ECONOMICS-SL|Economics SL]:  ⟵ “Economics SL | 4 | ECON 203 | 3”
  - equivalencies[IB-ECONOMICS-HL|Economics HL]:  ⟵ “Economics HL | 4 | ECON 203 | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|Environmental Systems]:  ⟵ “Environmental Systems | 4 | ENSS 105 | 3”
  - equivalencies[IB-FRENCH-SL|French: Lang. A or B SL]:  ⟵ “French: Lang. A or B SL | 4 | FREN 101 | 4”
  - equivalencies[IB-FRENCH-HL|French: Lang. A or B HL]:  ⟵ “French: Lang. A or B HL | 3 | FREN 101 | 4”
  - equivalencies[IB-MUSIC|Fundamentals of Music]:  ⟵ “Fundamentals of Music | 5 | MUSC 102 | 6”
  - equivalencies[IB-GEOGRAPHY-SL|Geography SL]:  ⟵ “Geography SL | 4 | GEOG 201 | 3”
  - equivalencies[IB-GEOGRAPHY-HL|Geography HL]:  ⟵ “Geography HL | 4 | GEOG 201 | 3”
  - equivalencies[IB-GERMAN-SL|German: Lang. A or B SL]:  ⟵ “German: Lang. A or B SL | 4 | GERM 101 | 4”
  - equivalencies[IB-GERMAN-HL|German: Lang. A or B HL]:  ⟵ “German: Lang. A or B HL | 3 | GERM 101 | 4”
  - equivalencies[IB-HISTORY|Islamic History]:  ⟵ “Islamic History | 4 | HIST 221/RELS 221 | 3”
  - equivalencies[IB-LATIN-SL|Latin SL]:  ⟵ “Latin SL | 4 | CLAS 121 | 4”
  - equivalencies[IB-LATIN-HL|Latin HL]:  ⟵ “Latin HL | 3 | CLAS 121 | 4”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|Mathemathics: Analysis & Approaches SL]:  ⟵ “Mathemathics: Analysis & Approaches SL | 6 | MATH 102 | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|Mathematics: Analysis & Approaches HL]:  ⟵ “Mathematics: Analysis & Approaches HL | 4 or 5 | MATH 102 | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|Mathematics Analysis & Approaches HL]:  ⟵ “Mathematics Analysis & Approaches HL | 5 | MATH 150 | 4”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|Mathematics: Analysis & Approaches HL]:  ⟵ “Mathematics: Analysis & Approaches HL | 6 | MATH 102 or MATH 150 or MATH 151 | 3, 4, 4”
  - … 14 more rows
### `a79d7e0020870243` The University of Texas Rio Grande Valley — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.utrgv.edu/ucentral/paying-for-college/financial-aid/satisfactory-academic-progress/index.htm (sha256 3301e91f4ef1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “To view the full UTRGV Satisfactory Academic Progress policy for Undergraduate and Graduate/Professional students, see below: UTRGV Satisfactory Academic Progress Policy for Undergraduate and Graduate Students Financial Aid Satisfactory Academic Progress Appeal (Financial Aid SAP Appeal) At the discretion of each school there is a provision outlined by Federal Regulations where schools can allow s”
  - sentence: sap_appeal ⟵ “If you think you may be eligible to appeal your financial aid SAP status due to experiencing one of the mitigating circumstances mentioned above, please click on this link to submit a Financial Aid SAP Appeal Important Notice : Appeal decisions made by the Office of Financial Aid are final and the U.S.”
### `05bc77812b0f7a78` The University of Texas Rio Grande Valley — costs 2023-24 · residency=out_of_state [changed] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: stale_year_label:2023-24, conflicts_with_verified_record
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
- change books_supplies: `1190` → `6182`
- change on_campus_food_housing: `9662` → `13527`
  - with_parents_or_family:Tuition & Fees: 33711 ⟵ “Tuition & Fees | 20,611 | 20,611 | 20,611 | 33,711 | 33,711 | 33,711”
  - with_parents_or_family:Housing & Food: 4748 ⟵ “Housing & Food | 4,748 | 13,527 | 16,053 | 4,748 | 13,527 | 16,053”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 6182 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,182 | 6,182 | 6,182 | 6,182 | 6,182 | 6,182”
  - with_parents_or_family:Transportation: 3795 ⟵ “Transportation | 3,795 | 2,124 | 3,795 | 3,795 | 2,124 | 3,795”
  - with_parents_or_family:Miscellaneous: 5883 ⟵ “Miscellaneous | 5,883 | 5,883 | 5,883 | 5,883 | 5,883 | 5,883”
  - with_parents_or_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - with_parents_or_family:Total Cost of Attendance: 57757 ⟵ “Total Cost of Attendance | 44,657 | 51,765 | 55,962 | 57,757 | 64,865 | 69,062”
  - on_campus:Tuition & Fees: 33711 ⟵ “Tuition & Fees | 20,611 | 20,611 | 20,611 | 33,711 | 33,711 | 33,711”
  - on_campus:Housing & Food: 13527 ⟵ “Housing & Food | 4,748 | 13,527 | 16,053 | 4,748 | 13,527 | 16,053”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 6182 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,182 | 6,182 | 6,182 | 6,182 | 6,182 | 6,182”
  - on_campus:Transportation: 2124 ⟵ “Transportation | 3,795 | 2,124 | 3,795 | 3,795 | 2,124 | 3,795”
  - on_campus:Miscellaneous: 5883 ⟵ “Miscellaneous | 5,883 | 5,883 | 5,883 | 5,883 | 5,883 | 5,883”
  - on_campus:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - on_campus:Total Cost of Attendance: 64865 ⟵ “Total Cost of Attendance | 44,657 | 51,765 | 55,962 | 57,757 | 64,865 | 69,062”
  - off_campus_not_with_family:Tuition & Fees: 33711 ⟵ “Tuition & Fees | 20,611 | 20,611 | 20,611 | 33,711 | 33,711 | 33,711”
  - off_campus_not_with_family:Housing & Food: 16053 ⟵ “Housing & Food | 4,748 | 13,527 | 16,053 | 4,748 | 13,527 | 16,053”
  - off_campus_not_with_family:Books, Course Materials, Supplies, & Equipment: 6182 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,182 | 6,182 | 6,182 | 6,182 | 6,182 | 6,182”
  - off_campus_not_with_family:Transportation: 3795 ⟵ “Transportation | 3,795 | 2,124 | 3,795 | 3,795 | 2,124 | 3,795”
  - off_campus_not_with_family:Miscellaneous: 5883 ⟵ “Miscellaneous | 5,883 | 5,883 | 5,883 | 5,883 | 5,883 | 5,883”
  - off_campus_not_with_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - off_campus_not_with_family:Total Cost of Attendance: 69062 ⟵ “Total Cost of Attendance | 44,657 | 51,765 | 55,962 | 57,757 | 64,865 | 69,062”
### `074868df96d61e36` The University of Texas Rio Grande Valley — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 34632 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - with_parents_or_family:Living Expenses: 6474 ⟵ “Living Expenses | 6,474 | 13,619 | 16,660 | 6,474 | 13,619 | 16,660”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 6344 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,344 | 6,344 | 6,344 | 6,344 | 6,344 | 6,344”
  - with_parents_or_family:Transportation: 4041 ⟵ “Transportation | 4,041 | 2,404 | 4,041 | 4,041 | 2,404 | 4,041”
  - with_parents_or_family:Miscellaneous: 6146 ⟵ “Miscellaneous | 6,146 | 6,146 | 6,146 | 6,146 | 6,146 | 6,146”
  - with_parents_or_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - with_parents_or_family:Total Cost of Attendance: 61075 ⟵ “Total Cost of Attendance | 47,975 | 53,483 | 58,161 | 61,075 | 66,583 | 71,261”
  - on_campus:Tuition & Fees: 34632 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - on_campus:Living Expenses: 13619 ⟵ “Living Expenses | 6,474 | 13,619 | 16,660 | 6,474 | 13,619 | 16,660”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 6344 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,344 | 6,344 | 6,344 | 6,344 | 6,344 | 6,344”
  - on_campus:Transportation: 2404 ⟵ “Transportation | 4,041 | 2,404 | 4,041 | 4,041 | 2,404 | 4,041”
  - on_campus:Miscellaneous: 6146 ⟵ “Miscellaneous | 6,146 | 6,146 | 6,146 | 6,146 | 6,146 | 6,146”
  - on_campus:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - on_campus:Total Cost of Attendance: 66583 ⟵ “Total Cost of Attendance | 47,975 | 53,483 | 58,161 | 61,075 | 66,583 | 71,261”
  - off_campus_not_with_family:Tuition & Fees: 34632 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - off_campus_not_with_family:Living Expenses: 16660 ⟵ “Living Expenses | 6,474 | 13,619 | 16,660 | 6,474 | 13,619 | 16,660”
  - off_campus_not_with_family:Books, Course Materials, Supplies, & Equipment: 6344 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,344 | 6,344 | 6,344 | 6,344 | 6,344 | 6,344”
  - off_campus_not_with_family:Transportation: 4041 ⟵ “Transportation | 4,041 | 2,404 | 4,041 | 4,041 | 2,404 | 4,041”
  - off_campus_not_with_family:Miscellaneous: 6146 ⟵ “Miscellaneous | 6,146 | 6,146 | 6,146 | 6,146 | 6,146 | 6,146”
  - off_campus_not_with_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - off_campus_not_with_family:Total Cost of Attendance: 71261 ⟵ “Total Cost of Attendance | 47,975 | 53,483 | 58,161 | 61,075 | 66,583 | 71,261”
### `57e406c81cc5dc3f` The University of Texas Rio Grande Valley — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 21532 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - with_parents_or_family:Living Expenses: 6577 ⟵ “Living Expenses | 6,577 | 14,230 | 17,039 | 6,577 | 14,230 | 17,039”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 6337 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,337 | 6,337 | 6,337 | 6,337 | 6,337 | 6,337”
  - with_parents_or_family:Transportation: 4830 ⟵ “Transportation | 4,830 | 3,085 | 4,830 | 4,830 | 3,085 | 4,830”
  - with_parents_or_family:Miscellaneous: 6084 ⟵ “Miscellaneous | 6,084 | 6,084 | 6,084 | 6,084 | 6,084 | 6,084”
  - with_parents_or_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - with_parents_or_family:Total Cost of Attendance: 48798 ⟵ “Total Cost of Attendance | 48,798 | 54,706 | 59,260 | 61,898 | 67,806 | 72,360”
  - on_campus:Tuition & Fees: 21532 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - on_campus:Living Expenses: 14230 ⟵ “Living Expenses | 6,577 | 14,230 | 17,039 | 6,577 | 14,230 | 17,039”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 6337 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,337 | 6,337 | 6,337 | 6,337 | 6,337 | 6,337”
  - on_campus:Transportation: 3085 ⟵ “Transportation | 4,830 | 3,085 | 4,830 | 4,830 | 3,085 | 4,830”
  - on_campus:Miscellaneous: 6084 ⟵ “Miscellaneous | 6,084 | 6,084 | 6,084 | 6,084 | 6,084 | 6,084”
  - on_campus:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - on_campus:Total Cost of Attendance: 54706 ⟵ “Total Cost of Attendance | 48,798 | 54,706 | 59,260 | 61,898 | 67,806 | 72,360”
  - off_campus_not_with_family:Tuition & Fees: 21532 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - off_campus_not_with_family:Living Expenses: 17039 ⟵ “Living Expenses | 6,577 | 14,230 | 17,039 | 6,577 | 14,230 | 17,039”
  - off_campus_not_with_family:Books, Course Materials, Supplies, & Equipment: 6337 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,337 | 6,337 | 6,337 | 6,337 | 6,337 | 6,337”
  - off_campus_not_with_family:Transportation: 4830 ⟵ “Transportation | 4,830 | 3,085 | 4,830 | 4,830 | 3,085 | 4,830”
  - off_campus_not_with_family:Miscellaneous: 6084 ⟵ “Miscellaneous | 6,084 | 6,084 | 6,084 | 6,084 | 6,084 | 6,084”
  - off_campus_not_with_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - off_campus_not_with_family:Total Cost of Attendance: 59260 ⟵ “Total Cost of Attendance | 48,798 | 54,706 | 59,260 | 61,898 | 67,806 | 72,360”
### `76075d4f6c006883` The University of Texas Rio Grande Valley — costs 2022-23 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: stale_year_label:2022-23
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 32739 ⟵ “Tuition & Fees | 19,639 | 19,639 | 19,639 | 32,739 | 32,739 | 32,739”
  - with_parents_or_family:Room & Board: 4419 ⟵ “Room & Board | 4,419 | 12,442 | 14,685 | 4,419 | 12,442 | 14,685”
  - with_parents_or_family:Books & Supplies: 5901 ⟵ “Books & Supplies | 5,901 | 5,901 | 5,901 | 5,901 | 5,901 | 5,901”
  - with_parents_or_family:Transportation: 3387 ⟵ “Transportation | 3,387 | 2,089 | 3,387 | 3,387 | 2,089 | 3,387”
  - with_parents_or_family:Miscellaneous: 5438 ⟵ “Miscellaneous | 5,438 | 5,438 | 5,438 | 5,438 | 5,438 | 5,438”
  - with_parents_or_family:Health Insurance: 3313 ⟵ “Health Insurance | 3,313 | 3,313 | 3,313 | 3,313 | 3,313 | 3,313”
  - with_parents_or_family:Total Cost of Attendance: 55197 ⟵ “Total Cost of Attendance | 42,097 | 48,882 | 52,363 | 55,197 | 61,922 | 65,463”
  - on_campus:Tuition & Fees: 32739 ⟵ “Tuition & Fees | 19,639 | 19,639 | 19,639 | 32,739 | 32,739 | 32,739”
  - on_campus:Room & Board: 12442 ⟵ “Room & Board | 4,419 | 12,442 | 14,685 | 4,419 | 12,442 | 14,685”
  - on_campus:Books & Supplies: 5901 ⟵ “Books & Supplies | 5,901 | 5,901 | 5,901 | 5,901 | 5,901 | 5,901”
  - on_campus:Transportation: 2089 ⟵ “Transportation | 3,387 | 2,089 | 3,387 | 3,387 | 2,089 | 3,387”
  - on_campus:Miscellaneous: 5438 ⟵ “Miscellaneous | 5,438 | 5,438 | 5,438 | 5,438 | 5,438 | 5,438”
  - on_campus:Health Insurance: 3313 ⟵ “Health Insurance | 3,313 | 3,313 | 3,313 | 3,313 | 3,313 | 3,313”
  - on_campus:Total Cost of Attendance: 61922 ⟵ “Total Cost of Attendance | 42,097 | 48,882 | 52,363 | 55,197 | 61,922 | 65,463”
  - off_campus_not_with_family:Tuition & Fees: 32739 ⟵ “Tuition & Fees | 19,639 | 19,639 | 19,639 | 32,739 | 32,739 | 32,739”
  - off_campus_not_with_family:Room & Board: 14685 ⟵ “Room & Board | 4,419 | 12,442 | 14,685 | 4,419 | 12,442 | 14,685”
  - off_campus_not_with_family:Books & Supplies: 5901 ⟵ “Books & Supplies | 5,901 | 5,901 | 5,901 | 5,901 | 5,901 | 5,901”
  - off_campus_not_with_family:Transportation: 3387 ⟵ “Transportation | 3,387 | 2,089 | 3,387 | 3,387 | 2,089 | 3,387”
  - off_campus_not_with_family:Miscellaneous: 5438 ⟵ “Miscellaneous | 5,438 | 5,438 | 5,438 | 5,438 | 5,438 | 5,438”
  - off_campus_not_with_family:Health Insurance: 3313 ⟵ “Health Insurance | 3,313 | 3,313 | 3,313 | 3,313 | 3,313 | 3,313”
  - off_campus_not_with_family:Total Cost of Attendance: 65463 ⟵ “Total Cost of Attendance | 42,097 | 48,882 | 52,363 | 55,197 | 61,922 | 65,463”
### `802f495e4d2d23e6` The University of Texas Rio Grande Valley — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.utrgv.edu/ucentral/tuition-advantage/ (sha256 e70fb940d804)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "rows": 2}
  - column:Cost of Attendance (COA): 15896 ⟵ “Cost of Attendance (COA) | $15,896 | ”
  - column:Available Unmet *Financial Need: 8396 ⟵ “Available Unmet *Financial Need | $8,396 | ”
  - column:Tuition & Mandatory Fees (T&F): 8132 ⟵ “Tuition & Mandatory Fees (T&F) |  | $8,132”
  - column:Less Total Financial Aid Received (Pell, TEXAS Grant, TPEG, SEOG): 0 ⟵ “Less Total Financial Aid Received (Pell, TEXAS Grant, TPEG, SEOG) |  | $0”
  - column:Remaining T&F Balance: 8132 ⟵ “Remaining T&F Balance |  | $8,132”
  - column:**Tuition Advantage Award Amount:: 8132 ⟵ “**Tuition Advantage Award Amount: |  | $8,132”
### `b0675878c59675a3` The University of Texas Rio Grande Valley — costs 2022-23 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: components_do_not_reconcile, residency_unknown, stale_year_label:2022-23
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 19639 ⟵ “Tuition & Fees | 19,639 | 19,639 | 19,639 | 32,739 | 32,739 | 32,739”
  - with_parents_or_family:Room & Board: 4419 ⟵ “Room & Board | 4,419 | 12,442 | 14,685 | 4,419 | 12,442 | 14,685”
  - with_parents_or_family:Books & Supplies: 5901 ⟵ “Books & Supplies | 5,901 | 5,901 | 5,901 | 5,901 | 5,901 | 5,901”
  - with_parents_or_family:Transportation: 3387 ⟵ “Transportation | 3,387 | 2,089 | 3,387 | 3,387 | 2,089 | 3,387”
  - with_parents_or_family:Miscellaneous: 5438 ⟵ “Miscellaneous | 5,438 | 5,438 | 5,438 | 5,438 | 5,438 | 5,438”
  - with_parents_or_family:Health Insurance: 3313 ⟵ “Health Insurance | 3,313 | 3,313 | 3,313 | 3,313 | 3,313 | 3,313”
  - with_parents_or_family:Total Cost of Attendance: 42097 ⟵ “Total Cost of Attendance | 42,097 | 48,882 | 52,363 | 55,197 | 61,922 | 65,463”
  - on_campus:Tuition & Fees: 19639 ⟵ “Tuition & Fees | 19,639 | 19,639 | 19,639 | 32,739 | 32,739 | 32,739”
  - on_campus:Room & Board: 12442 ⟵ “Room & Board | 4,419 | 12,442 | 14,685 | 4,419 | 12,442 | 14,685”
  - on_campus:Books & Supplies: 5901 ⟵ “Books & Supplies | 5,901 | 5,901 | 5,901 | 5,901 | 5,901 | 5,901”
  - on_campus:Transportation: 2089 ⟵ “Transportation | 3,387 | 2,089 | 3,387 | 3,387 | 2,089 | 3,387”
  - on_campus:Miscellaneous: 5438 ⟵ “Miscellaneous | 5,438 | 5,438 | 5,438 | 5,438 | 5,438 | 5,438”
  - on_campus:Health Insurance: 3313 ⟵ “Health Insurance | 3,313 | 3,313 | 3,313 | 3,313 | 3,313 | 3,313”
  - on_campus:Total Cost of Attendance: 48882 ⟵ “Total Cost of Attendance | 42,097 | 48,882 | 52,363 | 55,197 | 61,922 | 65,463”
  - off_campus_not_with_family:Tuition & Fees: 19639 ⟵ “Tuition & Fees | 19,639 | 19,639 | 19,639 | 32,739 | 32,739 | 32,739”
  - off_campus_not_with_family:Room & Board: 14685 ⟵ “Room & Board | 4,419 | 12,442 | 14,685 | 4,419 | 12,442 | 14,685”
  - off_campus_not_with_family:Books & Supplies: 5901 ⟵ “Books & Supplies | 5,901 | 5,901 | 5,901 | 5,901 | 5,901 | 5,901”
  - off_campus_not_with_family:Transportation: 3387 ⟵ “Transportation | 3,387 | 2,089 | 3,387 | 3,387 | 2,089 | 3,387”
  - off_campus_not_with_family:Miscellaneous: 5438 ⟵ “Miscellaneous | 5,438 | 5,438 | 5,438 | 5,438 | 5,438 | 5,438”
  - off_campus_not_with_family:Health Insurance: 3313 ⟵ “Health Insurance | 3,313 | 3,313 | 3,313 | 3,313 | 3,313 | 3,313”
  - off_campus_not_with_family:Total Cost of Attendance: 52363 ⟵ “Total Cost of Attendance | 42,097 | 48,882 | 52,363 | 55,197 | 61,922 | 65,463”
### `cb3bfc5e133f9d8c` The University of Texas Rio Grande Valley — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.utrgv.edu/scholarships/freshman-scholarships/utrgv-luminary-scholars/index.htm (sha256 4240b281d58a)
- issues: residency_unknown, conflicting_sources:https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition & Mandatory Fees: 40000 ⟵ “Tuition & Mandatory Fees | Years 1 – 4 | $10,000 x 4 | $40,000”
  - column:Room & Board: 17000 ⟵ “Room & Board | Years 1 & 2 | $8,500 x 2 | $17,000”
  - column:Graduate Tuition & Mandatory Fees: 18000 ⟵ “Graduate Tuition & Mandatory Fees | Years 5 & 6 | $9,000 x 2 | $18,000”
  - column:Total: 75000 ⟵ “Total | Years 1 – 6 | Combined maximum | $75,000”
### `cbcd8ead992053cb` The University of Texas Rio Grande Valley — costs 2025-26 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 34632 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - with_parents_or_family:Living Expenses: 6577 ⟵ “Living Expenses | 6,577 | 14,230 | 17,039 | 6,577 | 14,230 | 17,039”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 6337 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,337 | 6,337 | 6,337 | 6,337 | 6,337 | 6,337”
  - with_parents_or_family:Transportation: 4830 ⟵ “Transportation | 4,830 | 3,085 | 4,830 | 4,830 | 3,085 | 4,830”
  - with_parents_or_family:Miscellaneous: 6084 ⟵ “Miscellaneous | 6,084 | 6,084 | 6,084 | 6,084 | 6,084 | 6,084”
  - with_parents_or_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - with_parents_or_family:Total Cost of Attendance: 61898 ⟵ “Total Cost of Attendance | 48,798 | 54,706 | 59,260 | 61,898 | 67,806 | 72,360”
  - on_campus:Tuition & Fees: 34632 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - on_campus:Living Expenses: 14230 ⟵ “Living Expenses | 6,577 | 14,230 | 17,039 | 6,577 | 14,230 | 17,039”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 6337 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,337 | 6,337 | 6,337 | 6,337 | 6,337 | 6,337”
  - on_campus:Transportation: 3085 ⟵ “Transportation | 4,830 | 3,085 | 4,830 | 4,830 | 3,085 | 4,830”
  - on_campus:Miscellaneous: 6084 ⟵ “Miscellaneous | 6,084 | 6,084 | 6,084 | 6,084 | 6,084 | 6,084”
  - on_campus:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - on_campus:Total Cost of Attendance: 67806 ⟵ “Total Cost of Attendance | 48,798 | 54,706 | 59,260 | 61,898 | 67,806 | 72,360”
  - off_campus_not_with_family:Tuition & Fees: 34632 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - off_campus_not_with_family:Living Expenses: 17039 ⟵ “Living Expenses | 6,577 | 14,230 | 17,039 | 6,577 | 14,230 | 17,039”
  - off_campus_not_with_family:Books, Course Materials, Supplies, & Equipment: 6337 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,337 | 6,337 | 6,337 | 6,337 | 6,337 | 6,337”
  - off_campus_not_with_family:Transportation: 4830 ⟵ “Transportation | 4,830 | 3,085 | 4,830 | 4,830 | 3,085 | 4,830”
  - off_campus_not_with_family:Miscellaneous: 6084 ⟵ “Miscellaneous | 6,084 | 6,084 | 6,084 | 6,084 | 6,084 | 6,084”
  - off_campus_not_with_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - off_campus_not_with_family:Total Cost of Attendance: 72360 ⟵ “Total Cost of Attendance | 48,798 | 54,706 | 59,260 | 61,898 | 67,806 | 72,360”
### `dfb258d3331ed412` The University of Texas Rio Grande Valley — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: residency_unknown, conflicting_sources:https://www.utrgv.edu/scholarships/freshman-scholarships/utrgv-luminary-scholars/index.htm
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 22372 ⟵ “Tuition & Fees | 22,372 | 22,372 | 22,372 | 35,472 | 35,472 | 35,472”
  - with_parents_or_family:Living Expenses: 6857 ⟵ “Living Expenses | 6,857 | 14,711 | 18,102 | 6,857 | 14,711 | 18,102”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 6103 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,103 | 6,103 | 6,103 | 6,103 | 6,103 | 6,103”
  - with_parents_or_family:Transportation: 5173 ⟵ “Transportation | 5,173 | 3,131 | 5,173 | 5,173 | 3,131 | 5,173”
  - with_parents_or_family:Miscellaneous: 6160 ⟵ “Miscellaneous | 6,160 | 6,160 | 6,160 | 6,160 | 6,160 | 6,160”
  - with_parents_or_family:Health Insurance: 3707 ⟵ “Health Insurance | 3,707 | 3,707 | 3,707 | 3,707 | 3,707 | 3,707”
  - with_parents_or_family:Total Cost of Attendance: 50372 ⟵ “Total Cost of Attendance | 50,372 | 56,184 | 61,617 | 63,472 | 69,284 | 74,717”
  - on_campus:Tuition & Fees: 22372 ⟵ “Tuition & Fees | 22,372 | 22,372 | 22,372 | 35,472 | 35,472 | 35,472”
  - on_campus:Living Expenses: 14711 ⟵ “Living Expenses | 6,857 | 14,711 | 18,102 | 6,857 | 14,711 | 18,102”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 6103 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,103 | 6,103 | 6,103 | 6,103 | 6,103 | 6,103”
  - on_campus:Transportation: 3131 ⟵ “Transportation | 5,173 | 3,131 | 5,173 | 5,173 | 3,131 | 5,173”
  - on_campus:Miscellaneous: 6160 ⟵ “Miscellaneous | 6,160 | 6,160 | 6,160 | 6,160 | 6,160 | 6,160”
  - on_campus:Health Insurance: 3707 ⟵ “Health Insurance | 3,707 | 3,707 | 3,707 | 3,707 | 3,707 | 3,707”
  - on_campus:Total Cost of Attendance: 56184 ⟵ “Total Cost of Attendance | 50,372 | 56,184 | 61,617 | 63,472 | 69,284 | 74,717”
  - off_campus_not_with_family:Tuition & Fees: 22372 ⟵ “Tuition & Fees | 22,372 | 22,372 | 22,372 | 35,472 | 35,472 | 35,472”
  - off_campus_not_with_family:Living Expenses: 18102 ⟵ “Living Expenses | 6,857 | 14,711 | 18,102 | 6,857 | 14,711 | 18,102”
  - off_campus_not_with_family:Books, Course Materials, Supplies, & Equipment: 6103 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,103 | 6,103 | 6,103 | 6,103 | 6,103 | 6,103”
  - off_campus_not_with_family:Transportation: 5173 ⟵ “Transportation | 5,173 | 3,131 | 5,173 | 5,173 | 3,131 | 5,173”
  - off_campus_not_with_family:Miscellaneous: 6160 ⟵ “Miscellaneous | 6,160 | 6,160 | 6,160 | 6,160 | 6,160 | 6,160”
  - off_campus_not_with_family:Health Insurance: 3707 ⟵ “Health Insurance | 3,707 | 3,707 | 3,707 | 3,707 | 3,707 | 3,707”
  - off_campus_not_with_family:Total Cost of Attendance: 61617 ⟵ “Total Cost of Attendance | 50,372 | 56,184 | 61,617 | 63,472 | 69,284 | 74,717”
### `ec2c1c4c69a7c9f6` The University of Texas Rio Grande Valley — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: residency_unknown, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 21532 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - with_parents_or_family:Living Expenses: 6474 ⟵ “Living Expenses | 6,474 | 13,619 | 16,660 | 6,474 | 13,619 | 16,660”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 6344 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,344 | 6,344 | 6,344 | 6,344 | 6,344 | 6,344”
  - with_parents_or_family:Transportation: 4041 ⟵ “Transportation | 4,041 | 2,404 | 4,041 | 4,041 | 2,404 | 4,041”
  - with_parents_or_family:Miscellaneous: 6146 ⟵ “Miscellaneous | 6,146 | 6,146 | 6,146 | 6,146 | 6,146 | 6,146”
  - with_parents_or_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - with_parents_or_family:Total Cost of Attendance: 47975 ⟵ “Total Cost of Attendance | 47,975 | 53,483 | 58,161 | 61,075 | 66,583 | 71,261”
  - on_campus:Tuition & Fees: 21532 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - on_campus:Living Expenses: 13619 ⟵ “Living Expenses | 6,474 | 13,619 | 16,660 | 6,474 | 13,619 | 16,660”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 6344 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,344 | 6,344 | 6,344 | 6,344 | 6,344 | 6,344”
  - on_campus:Transportation: 2404 ⟵ “Transportation | 4,041 | 2,404 | 4,041 | 4,041 | 2,404 | 4,041”
  - on_campus:Miscellaneous: 6146 ⟵ “Miscellaneous | 6,146 | 6,146 | 6,146 | 6,146 | 6,146 | 6,146”
  - on_campus:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - on_campus:Total Cost of Attendance: 53483 ⟵ “Total Cost of Attendance | 47,975 | 53,483 | 58,161 | 61,075 | 66,583 | 71,261”
  - off_campus_not_with_family:Tuition & Fees: 21532 ⟵ “Tuition & Fees | 21,532 | 21,532 | 21,532 | 34,632 | 34,632 | 34,632”
  - off_campus_not_with_family:Living Expenses: 16660 ⟵ “Living Expenses | 6,474 | 13,619 | 16,660 | 6,474 | 13,619 | 16,660”
  - off_campus_not_with_family:Books, Course Materials, Supplies, & Equipment: 6344 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,344 | 6,344 | 6,344 | 6,344 | 6,344 | 6,344”
  - off_campus_not_with_family:Transportation: 4041 ⟵ “Transportation | 4,041 | 2,404 | 4,041 | 4,041 | 2,404 | 4,041”
  - off_campus_not_with_family:Miscellaneous: 6146 ⟵ “Miscellaneous | 6,146 | 6,146 | 6,146 | 6,146 | 6,146 | 6,146”
  - off_campus_not_with_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - off_campus_not_with_family:Total Cost of Attendance: 58161 ⟵ “Total Cost of Attendance | 47,975 | 53,483 | 58,161 | 61,075 | 66,583 | 71,261”
### `faa9c1074af2e4ff` The University of Texas Rio Grande Valley — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.utrgv.edu/som/admissions/tuition-and-financial-aid/cost-of-attendance/index.htm (sha256 a872eedd2894)
- issues: residency_unknown, stale_year_label:2023-24
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 20611 ⟵ “Tuition & Fees | 20,611 | 20,611 | 20,611 | 33,711 | 33,711 | 33,711”
  - with_parents_or_family:Housing & Food: 4748 ⟵ “Housing & Food | 4,748 | 13,527 | 16,053 | 4,748 | 13,527 | 16,053”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 6182 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,182 | 6,182 | 6,182 | 6,182 | 6,182 | 6,182”
  - with_parents_or_family:Transportation: 3795 ⟵ “Transportation | 3,795 | 2,124 | 3,795 | 3,795 | 2,124 | 3,795”
  - with_parents_or_family:Miscellaneous: 5883 ⟵ “Miscellaneous | 5,883 | 5,883 | 5,883 | 5,883 | 5,883 | 5,883”
  - with_parents_or_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - with_parents_or_family:Total Cost of Attendance: 44657 ⟵ “Total Cost of Attendance | 44,657 | 51,765 | 55,962 | 57,757 | 64,865 | 69,062”
  - on_campus:Tuition & Fees: 20611 ⟵ “Tuition & Fees | 20,611 | 20,611 | 20,611 | 33,711 | 33,711 | 33,711”
  - on_campus:Housing & Food: 13527 ⟵ “Housing & Food | 4,748 | 13,527 | 16,053 | 4,748 | 13,527 | 16,053”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 6182 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,182 | 6,182 | 6,182 | 6,182 | 6,182 | 6,182”
  - on_campus:Transportation: 2124 ⟵ “Transportation | 3,795 | 2,124 | 3,795 | 3,795 | 2,124 | 3,795”
  - on_campus:Miscellaneous: 5883 ⟵ “Miscellaneous | 5,883 | 5,883 | 5,883 | 5,883 | 5,883 | 5,883”
  - on_campus:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - on_campus:Total Cost of Attendance: 51765 ⟵ “Total Cost of Attendance | 44,657 | 51,765 | 55,962 | 57,757 | 64,865 | 69,062”
  - off_campus_not_with_family:Tuition & Fees: 20611 ⟵ “Tuition & Fees | 20,611 | 20,611 | 20,611 | 33,711 | 33,711 | 33,711”
  - off_campus_not_with_family:Housing & Food: 16053 ⟵ “Housing & Food | 4,748 | 13,527 | 16,053 | 4,748 | 13,527 | 16,053”
  - off_campus_not_with_family:Books, Course Materials, Supplies, & Equipment: 6182 ⟵ “Books, Course Materials, Supplies, & Equipment | 6,182 | 6,182 | 6,182 | 6,182 | 6,182 | 6,182”
  - off_campus_not_with_family:Transportation: 3795 ⟵ “Transportation | 3,795 | 2,124 | 3,795 | 3,795 | 2,124 | 3,795”
  - off_campus_not_with_family:Miscellaneous: 5883 ⟵ “Miscellaneous | 5,883 | 5,883 | 5,883 | 5,883 | 5,883 | 5,883”
  - off_campus_not_with_family:Health Insurance: 3438 ⟵ “Health Insurance | 3,438 | 3,438 | 3,438 | 3,438 | 3,438 | 3,438”
  - off_campus_not_with_family:Total Cost of Attendance: 55962 ⟵ “Total Cost of Attendance | 44,657 | 51,765 | 55,962 | 57,757 | 64,865 | 69,062”
### `5012893ffd7a8c81` The University of Texas Rio Grande Valley — credit_policies 2025-26 · policy_kind=CLEP [same] (labeled_in_source)
- source: https://www.utrgv.edu/admissions/credit-by-exam/index.htm (sha256 d7310a646023)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 19, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | ENGL 2326 | Introduction to American Literature | 50 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | BIOL 1406 BIOL 1407 | General Biology I (lecture + lab) General Biology II (lecture + lab) | 50 | 8”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | MATH 2413 MATH 2414 | Calculus I Calculus II | 50 | 8”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | CHEM 1311 CHEM 1111 CHEM 1312 CHEM 1112 | General Chemistry I General Chemistry I Lab General Chemistry II General Chemistry II Lab | 50 | 8”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | MATH 1314 | College Algebra | 50 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|53]:  ⟵ “Financial Accounting | ACCT 2301 | Introduction To Financial Accounting | 53 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Lang | FREN 1311 | Beginning French I | 50 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|52]:  ⟵ “French Lang | FREN 1311 FREN 1312 | Beginning French I Beginning French II | 52 | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|65]:  ⟵ “French Lang | FREN 1311 FREN 1312 FREN 2311 | Beginning French I Beginning French II Intermediate French I | 65 | 9”
  - equivalencies[CLEP-FRENCH-LANGUAGE|75]:  ⟵ “French Lang | FREN 1311 FREN 1312 FREN 2311 FREN 2312 | Beginning French I Beginning French II Intermediate French I Intermediate French II | 75 | 12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Lang | GERM 1311 | Beginning German I | 50 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|52]:  ⟵ “German Lang | GERM 1311 GERM 1312 | Beginning German I Beginning German II | 52 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|65]:  ⟵ “German Lang | GERM 1311 GERM 1312 FORL 1311 | Beginning German I Beginning German II Foreign Language I | 65 | 9”
  - equivalencies[CLEP-GERMAN-LANGUAGE|75]:  ⟵ “German Lang | GERM 1311 GERM 1312 FORL 1311 FORL 1312 | Beginning German I Beginning German II Foreign Language I Foreign Language II | 75 | 12”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the U.S. I | HIST 1301 | U.S. History I | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the U.S. II | HIST 1302 | U.S. History II | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Human Growth & Development | PSYC 2314 | Developmental Psychology: Lifespan | 50 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|51]:  ⟵ “Info Sys and Comp Appl | INFS 1301 | Computer Information Systems | 51 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|54]:  ⟵ “Introductory Business Law | BLAW 3337 | Business Law I | 54 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PSYC 2301 | General Psychology | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SOCI 1301 | Introduction to Sociology | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|53]:  ⟵ “Principles of Macroeconomics | ECON 2301 | Principles of Macroeconomics | 53 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|53]:  ⟵ “Principles of Management | MGMT 3361 | Principles of Management | 53 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|53]:  ⟵ “Principles of Marketing | MARK 3300 | Principles of Marketing | 53 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|53]:  ⟵ “Principles of Microeconomics | ECON 2302 | Principles of Microeconomics | 53 | 3”
  - … 4 more rows
### `df7c4b87678eb06a` The University of Texas Rio Grande Valley — credit_policies 2025-26 · policy_kind=AP [same] (labeled_in_source)
- source: https://www.utrgv.edu/admissions/credit-by-exam/index.htm (sha256 d7310a646023)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 31, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | HIST 1076A | General Credit - AP | 3 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art - 2-D Design | ARTS 1311 | Design I | 3 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art - 3-D Design | ARTS 1312 | Design II | 3 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art - Drawing | ARTS 1316 | Drawing I | 3 | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | ARTS 1301 ARTS 1303 | Art Appreciation Art History I Prehistoric to the 14th-Century | 3 | 6”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | BIOL 1406 BIOL 1407 | General Biology I General Biology II | 3 | 8”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3]:  ⟵ “Business with Personal Finance (Starting 2026-2027) | MGMT 1076A | General Credit - AP | 3 | 3”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Pre-Calculus | MATH 2412 | Pre-Calculus | 3 | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | CHEM 1311 CHEM 1111 CHEM 1312 CHEM 1112 | General Chemistry I General Chemistry I Lab General Chemistry II General Chemistry II Lab | 3 | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese, Japanese, Italian or Latin Language and Culture | FORL 1311 FORL 1312 | Foreign Languages I Foreign Languages II | 3 | 6”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | POLS 2330 | Introduction to Globalization | 3 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | CSCI 1101 | Introduction to Computer Science | 3 | 1”
  - equivalencies[AP-CYBERSECURITY|3]:  ⟵ “Cybersecurity (Pilot 2025-2026) | CYBI 1101CYBI 1076A | Introduction to Cyberspace & InformaticsGeneral Credit - AP | 3 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics (Macro) | ECON 2301 | Principles of Macroeconomics | 3 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics (Micro) | ECON 2302 | Principles of Microeconomics | 3 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language | ENGL 1301 | Rhetoric and Composition I | 3 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | ENGL 2341 | Introduction to Literature | 3 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | ENVR 1401 ENVR 1402 | Introduction to Environmental Science I Introduction to Environmental Science II | 3 | 8”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | HIST 1076B | General Credit - AP | 3 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | FREN 1311 FREN 1312 | Beginning French I Beginning French II | 3 | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture | FREN 1311 FREN 1312 FREN 2311 | Beginning French I Beginning French II Intermediate French I | 4 | 9”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language and Culture | FREN 1311 FREN 1312 FREN 2311 FREN 2312 | Beginning French I Beginning French II Intermediate French I Intermediate French II | 5 | 12”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | GERM 1311 | Beginning German I | 3 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language and Culture | GERM 1311 GERM 1312 | Beginning German I Beginning German II | 4 | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language and Culture | GERM 1311 GERM 1312 FORL 1311 | Beginning German I Beginning German II Foreign Language I | 5 | 9”
  - … 13 more rows
### `df91a2fd50397cb7` The University of Texas Rio Grande Valley — credit_policies 2025-26 · policy_kind=IB [same] (labeled_in_source)
- source: https://www.utrgv.edu/admissions/credit-by-exam/index.htm (sha256 d7310a646023)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 45, "equivalencies": 52, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-SL|SL 4]:  ⟵ “Biology Standard Level (SL) | BIOL 1406 BIOL 1407 | General Biology I (lecture + lab) General Biology II (lecture + lab) | 4 | 8”
  - equivalencies[IB-BIOLOGY-HL|HL 4]:  ⟵ “Biology Higher Level (HL) | BIOL 1406 BIOL 1407 | General Biology I (lecture + lab) General Biology II (lecture + lab) | 4 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|SL 4]:  ⟵ “Business Management Standard Level (SL) | MGMT 1075A | General Credit - IB | 4 | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4]:  ⟵ “Business Management Higher Level (HL) | MGMT 1075B | General Credit - IB | 4 | 3”
  - equivalencies[IB-CHEMISTRY-SL|SL 4]:  ⟵ “Chemistry Standard Level (SL) | CHEM 1311 CHEM 1111 CHEM 1312 CHEM 1112 | General Chemistry I General Chemistry I Lab General Chemistry II General Chemistry II Lab | 4 | 8”
  - equivalencies[IB-CHEMISTRY-HL|HL 4]:  ⟵ “Chemistry Higher Level (HL) | CHEM 1311 CHEM 1111 CHEM 1312 CHEM 1112 | General Chemistry I General Chemistry I Lab General Chemistry II General Chemistry II Lab | 4 | 8”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|SL 4]:  ⟵ “Computer Science Standard Level (SL) | CSCI 1101 | Introduction to Computer Science | 4 | 1”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 4]:  ⟵ “Computer Science Higher Level (HL) | CSCI 1380 | Introduction to Programming in Python | 4 | 3”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 6]:  ⟵ “Computer Science Higher Level (HL) | CSCI 1470 CSCI 2380 | Computer Science I Computer Science II | 6 | 7”
  - equivalencies[IB-ECONOMICS-SL|SL 4]:  ⟵ “Economics Standard Level (SL) | ECON 2301 | Principles of Macroeconomics | 4 | 3”
  - equivalencies[IB-ECONOMICS-HL|HL 4]:  ⟵ “Economics Higher Level (HL) | ECON 2301 ECON 2302 | Principles of Macroeconomics Principles of Microeconomics | 4 | 6”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-SL|SL 4]:  ⟵ “English A Language and Literature Standard Level (SL) | ENGL 2341 | Introduction to Literature | 4 | 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|HL 4]:  ⟵ “English A Language and Literature Higher Level (HL) | ENGL 2341 | Introduction to Literature | 4 | 3”
  - equivalencies[IB-ENGLISH-A-LITERATURE-SL|SL 4]:  ⟵ “English A Literature Standard Level (SL) | ENGL 2341 | Introduction to Literature | 4 | 3”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|HL 4]:  ⟵ “English A Literature Higher Level (HL) | ENGL 2341 | Introduction to Literature | 4 | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|SL 4]:  ⟵ “Environmental Systems and Societies Standard Level (SL) | ENVR 1075A | General Credit - IB | 4 | 3”
  - equivalencies[IB-FILM-SL|SL 4]:  ⟵ “Film Standard Level (SL) | FILM 2312 | History of Film | 4 | 3”
  - equivalencies[IB-FILM-HL|HL 4]:  ⟵ “Film Higher Level (HL) | FILM 2312 | History of Film | 4 | 3”
  - equivalencies[IB-FRENCH-SL|SL 4]:  ⟵ “French B Standard Level (SL) | FREN 1311 FREN 1312 | Beginning French I Beginning French II | 4 | 6”
  - equivalencies[IB-FRENCH-HL|HL 4]:  ⟵ “French B Higher Level (HL) | FREN 2311 FREN 2312 | Intermediate French I Intermediate French II | 4 | 6”
  - equivalencies[IB-GEOGRAPHY-SL|SL 4]:  ⟵ “Geography Standard Level (SL) | GEOG 2313 | Principles of Geography Physics Elementary | 4 | 3”
  - equivalencies[IB-GEOGRAPHY-HL|HL 4]:  ⟵ “Geography Higher Level (HL) | HIST 3302 | Geography and Environment in History | 4 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-SL|SL 4]:  ⟵ “Global Politics Standard Level (SL) | POLS 2330 | Introduction to Globalization | 4 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-HL|HL 4]:  ⟵ “Global Politics Higher Level (HL) | POLS 2330 | Introduction to Globalization | 4 | 3”
  - equivalencies[IB-HISTORY-HL|HL 4]:  ⟵ “History: Americas Higher Level (HL) | HIST 1075A | General Credit - IB | 4 | 3”
  - … 27 more rows
### `31d2d51e214c117d` The University of Texas at Arlington — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uta.edu/administration/fao/policies/sap (sha256 4e8f822a2ff8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “Students are able to complete a SAP Appeal at that time.”
  - sentence: sap_appeal ⟵ “Once a student is notified, that student can complete a 2026-2027 Satisfactory Academic Progress (SAP) appeal, students can do so directly in their MyMav Account via the ‘My Forms’ tile on their Student Homepage.”
  - sentence: sap_appeal ⟵ “How to Submit a SAP Appeal If you have specific questions regarding UTA's SAP Policy or the SAP Appeal process, please email SAP@uta.edu.”
  - sentence: sap_appeal ⟵ “SAP appeal decisions may take up to 30 days to be made.”
  - sentence: sap_appeal ⟵ “If it has not been 30 days since the submission of you SAP appeal, please do not email us asking for a status update on your SAP appeal.”
  - sentence: sap_appeal ⟵ “These students will have an unearned GPA and will be required to file a SAP appeal.”
### `4987d6bac88d63b8` The University of Texas at Arlington — appeals 2020-21 [new] (labeled_in_url)
- source: https://cdn.prod.web.uta.edu/-/media/project/website/administration/fao/documents/policies/how_to_submit_2020_2021_sap_appeal_form_08-2026.pdf (sha256 f0df52508a41)
- issues: stale_year_label:2020-21, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “How to Submit a SAP Appeal Form MyMav Fluid – Students OFF-CAMPUS NOTICE: If you are logging in from off-campus using a web-browser, you will be prompted to sign in with a secondary authentication method, such as a phone call, text message, or the mobile phone app.”
### `bf81abc6a8036eb8` The University of Texas at Arlington — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uta.edu/administration/fao/scholarships/scholarship-appeal-process (sha256 0a7c56f770d9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “Students may click on the 'Scholarship Appeal Form' link below to submit their statement and documentation.”
  - sentence: scholarship_retention_appeal ⟵ “SCHOLARSHIP APPEAL FORM Scholarships Overview Scholarships Terms & Conditions Undergraduate Eligibility Policies Overview Renewal Requirements Full-Time Enrollment Change to Less Than Full-Time Graduating Semester PPI Programs Non-Resident Tuition Waiver and Grants Departmental Scholarships Outside Scholarships State Programs UTA Employee Scholarship Graduate Fellowships Overview Federal Fellowshi”
### `40498ad94da2cb62` The University of Texas at Austin — appeals 2026-27 [new] (labeled_in_source)
- source: https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/my-financial-aid-system/ (sha256 3956aa259577)
- issues: semantic_review_required, conflicting_sources:https://onestop.utexas.edu/forms/,https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/managing-aid/,https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/why-financial-aid-changed/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If changes in your or your family members’ lives have impacted you financially, you may be eligible to submit a special circumstance appeal.”
### `45ba2c64e3164738` The University of Texas at Austin — appeals 2026-27 [new] (labeled_in_source)
- source: https://onestop.utexas.edu/forms/ (sha256 85ac6604d725)
- issues: semantic_review_required, conflicting_sources:https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/managing-aid/maintaining-eligibility/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Download Satisfactory Academic Progress (SAP) Appeal Submit this appeal if your financial aid has been suspended due to not meeting SAP requirements.”
### `69a382eb69e5e075` The University of Texas at Austin — appeals 2026-27 [new] (labeled_in_source)
- source: https://onestop.utexas.edu/forms/ (sha256 85ac6604d725)
- issues: semantic_review_required, conflicting_sources:https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/managing-aid/,https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/my-financial-aid-system/,https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/why-financial-aid-changed/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have unusual circumstances that prevent you from providing parental information, you may submit this appeal for consideration.”
### `844140f93e2c0262` The University of Texas at Austin — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/managing-aid/ (sha256 c75f7ed729c5)
- issues: semantic_review_required, conflicting_sources:https://onestop.utexas.edu/forms/,https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/my-financial-aid-system/,https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/why-financial-aid-changed/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Appeals If changes in your or your family’s lives have impacted you financially, you may be eligible to submit a special circumstance appeal.”
### `db1c6f0eb097c619` The University of Texas at Austin — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/managing-aid/maintaining-eligibility/ (sha256 6ce65e81de2b)
- issues: semantic_review_required, conflicting_sources:https://onestop.utexas.edu/forms/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “You can regain financial aid eligibility by meeting all SAP evaluated measures or submitting a successful SAP appeal and receiving approval.”
  - sentence: sap_appeal ⟵ “To appeal, you must submit the Satisfactory Academic Progress (SAP) Appeal form, which requires attaching a personal statement and supporting documents.”
  - sentence: sap_appeal ⟵ “For timely review and processing, you are encouraged to submit a SAP appeal by the following deadlines: | Semester | Priority Deadline | Final Deadline | Summer 2026 | None | August 3, 2026 | Fall 2026 | August 10, 2026 | December 1, 2026 | Spring 2027 | January 5, 2027 | April 23, 2027 Priority Deadline Summer 2026 None Fall 2026 August 10, 2026 Spring 2027 January 5, 2027 Final Deadline Summer 2”
### `e46fb9378a8ffbea` The University of Texas at Austin — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/why-financial-aid-changed/ (sha256 70ae1305f3ff)
- issues: semantic_review_required, conflicting_sources:https://onestop.utexas.edu/forms/,https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/managing-aid/,https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/my-financial-aid-system/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Unexpected events like job loss or medical expenses can impact your financial situation.”
### `mf629b5761e622ed` The University of Texas at Austin — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.utexas.edu/apply/transfer-students/transfer-credit-resources/ (sha256 5d9b14e56af0)
- issues: conflicting_sources:residency_requirement_credits
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 3}
  - residency_requirement_credits: 60 ⟵ “All programs require completion of at least 60 semester hours in residence at UT.”
  - residency_requirement_credits: 60 ⟵ “Student must complete at least 60 semester credit hours of coursework counted toward the degree in residence.”
  - residency_requirement_credits: 24 ⟵ “Completion of at least 24 credit hours in residence at UT Austin by the end of a spring semester.”
### `aebb3c12c801871e` The University of Texas at El Paso — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.utep.edu/admissions/_files/docs/advance-placement-examinations.pdf (sha256 021b37473172)
- issues: credits_implausible
- checks: {"distinct_exams": 37, "equivalencies": 55, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                              3        3                        ART 1300”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art: Studio Art Drawing                  3        3                 ART 3 hrs elective”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art: Studio Art 2-D Design               3        3                 ART 3 hrs elective”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art: Studio Art 3-D Design               3        3                 ART 3 hrs elective”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                  3        6           BIOL 1305, BIOL 1306”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                              3        4                      MATH 1411”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                              3        7        MATH 1411, MATH 1312”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                3        6         CHEM 1305, CHEM 1306”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture             3       12”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language and Culture             4       15           CHIN 2301, CHIN 2302”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language and Culture             5       15           CHIN 2301, CHIN 2302”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics        3        3               POLS 3 hrs elective”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                       3        4                          CS 1401”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles              3        3                          CS 1310”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition         3        6           RWS 1301, RWS 1302”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition       3        6           RWS 1301, RWS 1302”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                    3        4            ESCI 1301, ESCI 1101”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                         3        6                HIST 6 hrs elective”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture            3   12”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture            4   15    FREN 2301, FREN 2302”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language and Culture            5   18    FREN 2301, FREN 2302”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture            3   12”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                        3   3               GEOG 1310”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture           3   6      LING 2303, LING 2304”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4]:  ⟵ “Italian Language and Culture           4   9”
  - … 30 more rows
### `98e80df6253df7a2` University of Houston — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uh.edu/one-stop/financial/ (sha256 ce86092e7a7e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have experienced a change in income due to job loss, medical needs, death of parent or spouse or any other catastrophic event, please come and speak with an advisor at the Welcome Center regarding a Special Circumstance Appeal.”
### `m84212500f5e85a1` University of Houston — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://www.uh.edu/undergraduate-admissions/apply/transfer/transfer-equivalency-guides/_files_2026/earthba.pdf (sha256 b3daba94a144)
- issues: ambiguous_year_labels, conflicting_sources:max_transfer_credits
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 24}
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Because admission to the Hines College is highly selective and competitive, all applicants are advised to carefully curate and craft their portfolios as a best reflection of themselves. *TRANSFER CREDIT LIMIT: A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Other UH options are available – 3000/4000 level BIOL courses. ^Calculus III is one of the three options available to satisfy the major’s final Math requirements (the other options are UH-only MATH 3338, Probability or MATH 3339, Statistics for the Sciences). *Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 18 ⟵ “Up to 18 hours of lower-level courses can be transferred: 9 hours in 2 different concentrations, or 6 hours in 3 different concentrations.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Course Name Hours TCCNS UH Physical Anthropology ANTH 2301 ANTH 2301 Intro to Archaeology ANTH 2302 ANTH 2302 General Anthropology ANTH 2346 ANTH 2346 Cultural Anthropology 3 ANTH 2351 ANTH 2351 Texas History HIST 2301 HIST 2301 World Civilizations I HIST 2321 HIST 2321 World Civilizations II HIST 2322 HIST 2322 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level t”
  - max_transfer_credits: 66 ⟵ “Course Name Hours TCCNS UH Physical Anthropology ANTH 2301 ANTH 2301 Intro to Archaeology ANTH 2302 ANTH 2302 General Anthropology ANTH 2346 ANTH 2346 Cultural Anthropology 3 ANTH 2351 ANTH 2351 Texas History HIST 2301 HIST 2301 World Civilizations I HIST 2321 HIST 2321 World Civilizations II HIST 2322 HIST 2322 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level t”
  - max_transfer_credits: 66 ⟵ “Course Name Hours TCCNS UH Physical Anthropology ANTH 2301 ANTH 2301 Intro to Archaeology ANTH 2302 ANTH 2302 General Anthropology ANTH 2346 ANTH 2346 Cultural Anthropology 3 ANTH 2351 ANTH 2351 Texas History HIST 2301 HIST 2301 World Civilizations I HIST 2321 HIST 2321 World Civilizations II HIST 2322 HIST 2322 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level t”
  - max_transfer_credits: 66 ⟵ “Course Name Hours TCCNS UH Physical Anthropology ANTH 2301 ANTH 2301 Intro to Archaeology ANTH 2302 ANTH 2302 General Anthropology ANTH 2346 ANTH 2346 Cultural Anthropology 3 ANTH 2351 ANTH 2351 Texas History HIST 2301 HIST 2301 World Civilizations I HIST 2321 HIST 2321 World Civilizations II HIST 2322 HIST 2322 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level t”
  - max_transfer_credits: 66 ⟵ “Bachelor of Arts Special Degree Requirements (6 hours)* Six (6) hours of sophomore 2000-level Foreign Language: Six (6) hours of sophomore-level foreign-language courses: 2311 & 2312 in American Sign Language, Arabic, Chinese, French, German, Greek, Hindi, Italian, Japanese, Korean, Latin, Russian, Spanish, or Vietnamese *Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/20”
  - max_transfer_credits: 66 ⟵ “Course Name Hours TCCNS UH Physical Anthropology ANTH 2301 ANTH 2301 Intro to Archaeology ANTH 2302 ANTH 2302 General Anthropology ANTH 2346 ANTH 2346 Cultural Anthropology 3 ANTH 2351 ANTH 2351 Texas History HIST 2301 HIST 2301 World Civilizations I HIST 2321 HIST 2321 World Civilizations II HIST 2322 HIST 2322 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level t”
  - max_transfer_credits: 66 ⟵ “Course Name Hours TCCNS UH Physical Anthropology ANTH 2301 ANTH 2301 Intro to Archaeology ANTH 2302 ANTH 2302 General Anthropology ANTH 2346 ANTH 2346 Cultural Anthropology 3 ANTH 2351 ANTH 2351 Texas History HIST 2301 HIST 2301 World Civilizations I HIST 2321 HIST 2321 World Civilizations II HIST 2322 HIST 2322 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level t”
  - max_transfer_credits: 66 ⟵ “Because admission to the Hines College is highly selective and competitive, all applicants are advised to carefully curate and craft their portfolios as a best reflection of themselves. *TRANSFER CREDIT LIMIT: A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Course Name Hours TCCNS UH Physical Anthropology ANTH 2301 ANTH 2301 Intro to Archaeology ANTH 2302 ANTH 2302 General Anthropology ANTH 2346 ANTH 2346 Cultural Anthropology 3 ANTH 2351 ANTH 2351 Texas History HIST 2301 HIST 2301 World Civilizations I HIST 2321 HIST 2321 World Civilizations II HIST 2322 HIST 2322 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level t”
  - max_transfer_credits: 66 ⟵ “Course Name Hours TCCNS UH Physical Anthropology ANTH 2301 ANTH 2301 Intro to Archaeology ANTH 2302 ANTH 2302 General Anthropology ANTH 2346 ANTH 2346 Cultural Anthropology 3 ANTH 2351 ANTH 2351 Texas History HIST 2301 HIST 2301 World Civilizations I HIST 2321 HIST 2321 World Civilizations II HIST 2322 HIST 2322 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level t”
  - max_transfer_credits: 66 ⟵ “Major Requirements (12 hours) Course Name Hours TCCNS UH Anatomy & Physiology I 4 BIOL 2301/2101 or 2401 BIOL 2301/2101 Anatomy & Physiology II 4 BIOL 2302/2102 or 2402 BIOL 2302/2102 Microbiology for Non-Science Majors OR BIOL 2320/2120 or 2420 OR BIOL 2320/2120 OR 4 Microbiology for Science Majors BIOL 2321/2121 or 2421 BIOL 2321/2121 Transfer Credit Limit A maximum of 66 hours (grades C- or bet”
  - max_transfer_credits: 66 ⟵ “Because admission to the Hines College is highly selective and competitive, all applicants are advised to carefully curate and craft their portfolios as a best reflection of themselves. *TRANSFER CREDIT LIMIT: A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Because admission to the Hines College is highly selective and competitive, all applicants are advised to carefully curate and craft their portfolios as a best reflection of themselves. *TRANSFER CREDIT LIMIT: A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Major Requirements (17 hours) Course Name Hours TCCNS UH Nutrition and Diet Therapy 3 BIOL 1322 NUTR 2332 Anatomy & Physiology I 4 BIOL 2301/2101 or 2401 BIOL 2301/2101 Anatomy & Physiology II 4 BIOL 2302/2102 or 2402 BIOL 2302/2102 College Physics I 3 PHYS 1301 or 1401 PHYS 1301 Precalculus 3 MATH 2312 MATH 2312 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level ”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “TRANSFER CREDIT LIMIT: A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
### `m851ec969a65b33a` University of Houston — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.uh.edu/undergraduate-admissions/apply/transfer/transfer-equivalency-guides/_files_2025/muscbmt.pdf (sha256 341b981a3806)
- issues: conflicting_values:max_transfer_credits, stale_year_label:2025-26
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 33}
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “McGovern College of the Arts 713.743.1010 | www.uh.edu/transfer 713.743.3001 | www.uh.edu/kgmca *Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “To graduate, students must earn at least 36 hours of advanced-level credit. *Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Major Requirements (9-10 hours) Course Name Hours TCCNS UH Principles of Financial Accounting 3 ACCT 2301 ACCT 2301 Principles of Managerial Accounting 3 ACCT 2302 ACCT 2302 Elementary Statistical Methods 3 MATH 1342 MATH 1342 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Major Requirements (12 hours) Course Name Hours TCCNS UH Principles of Financial Accounting 3 ACCT 2301 ACCT 2301 Principles of Managerial Accounting 3 ACCT 2302 ACCT 2302 Math for Business and Social Sciences 3 MATH 1324 MATH 1324 Elementary Statistical Methods 3 MATH 1342 MATH 1342 Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied ”
  - max_transfer_credits: 66 ⟵ “These courses must be from outside the student’s major, and only include those courses approved for NSM majors. **Credits may not be applied toward a degree for both College and University Physics. *Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “All Bilingual Generalist Majors take a Spanish Placement Test at UH to determine their starting level for Spanish language classes. (Continued on Next Page) Office of Admissions College of Education-Office of Undergraduate Studies 713.743.1010 | www.uh.edu/transfer 713.743.5000 | www.coe.uh.edu Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may ”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Applied studio placement is determined by performance in audition. *Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Applied studio placement is determined by performance in audition. *Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - max_transfer_credits: 66 ⟵ “Transfer Credit Limit A maximum of 66 hours (grades C- or better) of 1000/2000 level transfer hours may be applied toward a UH degree.”
  - … 7 more rows
### `29a0741309f4420d` University of Houston-Downtown — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uhd.edu/financial/eligibility/financial-sap-policy.html (sha256 783cc75d2594)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “A status assigned by UHD Office of Scholarships and Financial Aid to a student who fails to make satisfactory academic progress, appeals and has had eligibility for aid reinstated.”
  - sentence: sap_appeal ⟵ “The SAP appeal must address why the student failed SAP, and what has changed in the student’s situation that will allow the student to meet SAP at the next evaluation.”
  - sentence: sap_appeal ⟵ “Application Deadline Please see Satisfactory Academic Progress Appeal Form for deadline dates.”
### `mf899db8dccef4dc` University of Houston-Downtown — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.uhd.edu/documents/admissions/transfer/hcc/20252026/hcc-as-in-biology-to-bs-in-biology-10-28-25.pdf (sha256 ba2c587e2eec)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"], "merged_pages": 15}
  - min_grade: C ⟵ “PHYS with a grade of C or higher) as part of the AAT may transfer the third course in for NS 3310.”
  - min_grade: C ⟵ “PHYS with a grade of C or higher) as part of the AAT may transfer the third course in for NS 3310.”
  - min_grade: C ⟵ “PHYS with a grade of C or higher) as part of the AAT may transfer the third course in for NS 3310.”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science Biology to UH-Downtown Bachelor of Science (Data Science) Transfer Information Program Specific Information: Bachelor of Science – Data Science Program Specific Requirements: • The BS in Data Science at UHD is a 120 credit hour degree program • All degree candidates must have a 2.0 GPA average and a grade of “C” or better in all upper level courses.”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science Chemistry to UH-Downtown Bachelor of Science (Data Science) Transfer Information Program Specific Information: Bachelor of Science – Data Science Program Specific Requirements: • The BS in Data Science at UHD is a 120-credit-hour degree program • All degree candidates must have a 2.0 GPA average and a grade of “C” or better in all upper-level courses.”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science Computer Science to UH-Downtown Bachelor of Science (Computer Science) Transfer Information Program Specific Information: Bachelor of Science – Computer Science Program Specific Requirements: • The BS in Computer Science at UHD is a 120 credit hour degree program. • All The Bachelor of Science Degree in Computer Science requires a grade of “C” or higher in”
  - min_grade: C ⟵ “Updated: 5-23-2024 HCC Associate of Science Geology to UH-Downtown Bachelor of Science (Data Science) Transfer Information Program Specific Information: Bachelor of Science – Data Science Program Specific Requirements: • The BS in Data Science at UHD is a 120 credit hour degree program • All degree candidates must have a 2.0 GPA average and a grade of “C” or better in all upper level course work.”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science Geology to University of Houston-Downtown ` Bachelor of Science in Geosciences Environmental Geology Concentration Transfer Information Program Specific Information: Bachelor of Science – Geosciences – Environmental Geology Program Specific Requirements: • The BS in Geosciences at UHD is a 120 credit hour degree program • All degree candidates must have a ”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science in Biology (Biology Majors) to ` University of Houston-Downtown Bachelor of Science – Biotechnology Transfer Information Program Specific Information: Bachelor of Science – Biotechnology Program Specific Requirements: • The BS in Biotechnology at UHD is a 120 credit hour degree program • All degree candidates must have a 2.0 GPA average and a grade of “C” ”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science in Biology (Biology Majors) to University of Houston-Downtown ` Bachelor of Science in Biology Transfer Information Program Specific Information: Bachelor of Science – Biology Program Specific Requirements: • The BS in Biology at UHD is a 120 credit hour degree program • All degree candidates must have a 2.0 GPA average and a grade of “C” or better in all ”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science in Biology (Biology Majors) to University of ` Houston-Downtown Bachelor of Science in Chemistry Transfer Information Program Specific Information: Bachelor of Science – Chemistry Program Specific Requirements: • The BS in Chemistry at UHD is a 120 credit hour degree program • All degree candidates must have a 2.0 GPA average and a grade of “C” or better i”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science in Biology (Biology Majors) to ` University of Houston-Downtown Bachelor of Science – Physical Sciences w/ Chemistry Concentration Transfer Information Program Specific Information: Bachelor of Science – Physical Sciences Program Specific Requirements: • The BS in Physical Sciences at UHD is a 120 credit hour degree program • All degree candidates must hav”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science in Chemistry (Chemistry Majors) to ` University of Houston-Downtown Bachelor of Science in Chemistry Transfer Information Program Specific Information: Bachelor of Science – Chemistry Program Specific Requirements: • The BS in Chemistry at UHD is a 120 credit hour degree program • All degree candidates must have a 2.0 GPA average and a grade of “C” or bett”
  - min_grade: C ⟵ “Updated: 5-23-2024 HCC Associate of Science Geology to University of Houston-Downtown ` Bachelor of Science in Geosciences Petroleum Geotechnology Concentration Transfer Information Program Specific Information: Bachelor of Science – Geosciences – Petroleum Geotechnology Program Specific Requirements: • The BA in Mathematics at UHD is a 120 credit hour degree program • All degree candidates must h”
  - min_grade: C ⟵ “Updated: 09-2025 HCC Associate of Science in Geology to ` University of Houston-Downtown Bachelor of Science – Physical Sciences w/ Geosciences Concentration Transfer Information Program Specific Information: Bachelor of Science – Physical Sciences Program Specific Requirements: • The BS in Physical Sciences at UHD is a 120 credit hour degree program • All degree candidates must have a 2.0 GPA ave”
### `15d84fcc59afc961` University of North Texas — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.unt.edu/sap.html (sha256 43b34e34d025)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal: The process for students on Financial Aid Suspension to petition for a reconsideration of financial aid due to extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Please be advised – per federal regulations, a SAP appeal cannot be approved after the last day of the applicable term.”
  - sentence: sap_appeal ⟵ “Fall: November 1 Spring: April 1 Summer: June 1 Please see the following page for information regarding the SAP Appeal requirements and process: SAP Appeal Process Repeated Coursework Per Federal Regulation, a student is not eligible for Title IV (federal) financial aid for any course they repeat more than once if they have previously passed the course (i.e., earned a D or better).”

## Re-verification of existing records (233)

- source_not_fetched: data/institutions/actx/credit_policies/2026-27.json ["credit_policies", "ipeds-222576", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/angelina/credit_policies/2026-27.json ["credit_policies", "ipeds-222822", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/abu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-222877", null, "2026-27", {}]
- source_not_fetched: data/institutions/baylor/transfer_policies/2026-27.json ["transfer_policies", "ipeds-223232", null, "2026-27", {}]
- source_not_fetched: data/institutions/clarendoncollege/credit_policies/2026-27.json ["credit_policies", "ipeds-223922", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/clarendoncollege/credit_policies/2026-27.json ["credit_policies", "ipeds-223922", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/com/credit_policies/2026-27.json ["credit_policies", "ipeds-226408", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/com/credit_policies/2026-27.json ["credit_policies", "ipeds-226408", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/com/credit_policies/2026-27.json ["credit_policies", "ipeds-226408", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/concordia/transfer_policies/2026-27.json ["transfer_policies", "ipeds-224004", null, "2026-27", {}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "accounting-bba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-commercial-art-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-commercial-art-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-digital-photography-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-digital-photography-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-graphic-design-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-graphic-design-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-studio-art-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "art-studio-art-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "biblical-studies-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "biology-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "biology-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "biology-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "cell-biology-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "cell-biology-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "christian-ministries-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "christian-studies-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "christian-studies-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "commercial-music-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "commercial-music-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-broadcast-digital-media-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-broadcast-digital-media-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-church-media-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-church-media-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-communication-studies-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-communication-studies-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-graphic-design-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-graphic-design-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-public-relations-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "communication-public-relations-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "computer-information-science-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "computer-information-science-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "computer-information-science-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "computer-science-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "computer-science-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "core-subjects-ec-6-with-science-of-teaching-reading-and-special-education-ec-12-"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "core-subjects-early-childhood-through-grade-6-teacher-certification-bsed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "criminal-justice-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "criminal-justice-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "criminal-justice-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "cybersecurity-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "ec-through-12-certification-physical-education-kinesiology-major-bsed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "english-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "english-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "english-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "entrepreneurship-bba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "environmental-science-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "finance-bba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "grades-4-8-certification-mathematics-bsed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "grades-4-8-certification-science-bsed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "grades-7-through-12-certification-english-language-arts-and-reading-baed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "grades-7-through-12-certification-english-language-arts-and-reading-bsed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "grades-7-through-12-certification-life-science-biology-major-bsed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "grades-7-through-12-certification-mathematics-bsed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "grades-7-through-12-certification-science-natural-sciences-major-bsed"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "health-sciences-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "history-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "history-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "history-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "intercultural-studies-missions-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "intercultural-studies-missions-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "interdisciplinary-studies-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "interdisciplinary-studies-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "interdisciplinary-studies-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "kinesiology-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "kinesiology-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "kinesiology-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "macrobiology-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "macrobiology-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "management-bba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "marketing-bba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "mathematics-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "mathematics-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "music-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "music-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "natural-sciences-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "philosophy-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "philosophy-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "political-science-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "political-science-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "political-science-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "politics-philosophy-and-economics-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "politics-philosophy-and-economics-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "politics-philosophy-and-economics-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "psychology-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "psychology-bas"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "psychology-bs"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "spanish-ba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "sport-management-bba"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "theory-bm"}]
- source_not_fetched: data/institutions/dbu/academic_programs/2026-27.json ["academic_programs", "ipeds-224226", null, "2026-27", {"program_key": "vocal-performance-bm"}]
- source_not_fetched: data/institutions/dbu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-224226", null, "2026-27", {}]
- source_not_fetched: data/institutions/dallasinstitute/credit_policies/2026-27.json ["credit_policies", "ipeds-224271", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/etbu/credit_policies/2026-27.json ["credit_policies", "ipeds-224527", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/etbu/credit_policies/2026-27.json ["credit_policies", "ipeds-224527", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/etbu/credit_policies/2026-27.json ["credit_policies", "ipeds-224527", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/hsutx/credit_policies/2026-27.json ["credit_policies", "ipeds-225247", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/hillcollege/credit_policies/2026-27.json ["credit_policies", "ipeds-225371", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/hillcollege/credit_policies/2026-27.json ["credit_policies", "ipeds-225371", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/hputx/credit_policies/2026-27.json ["credit_policies", "ipeds-225548", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/htu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-225575", null, "2026-27", {}]
- source_not_fetched: data/institutions/jacksonvillecollege/costs/2026-27.json ["costs", "ipeds-225876", null, "2026-27", {"residency": "not_applicable"}]
- source_not_fetched: data/institutions/lamarpa/credit_policies/2026-27.json ["credit_policies", "ipeds-226116", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/letu/awards/2026-27.json ["awards", "ipeds-226231", null, "2026-27", {"award_name": "Presidential Scholarship"}]
- source_not_fetched: data/institutions/letu/awards/2026-27.json ["awards", "ipeds-226231", null, "2026-27", {"award_name": "Dean's Scholarship"}]
- source_not_fetched: data/institutions/letu/awards/2026-27.json ["awards", "ipeds-226231", null, "2026-27", {"award_name": "Founder's Scholarship"}]
- source_not_fetched: data/institutions/letu/awards/2026-27.json ["awards", "ipeds-226231", null, "2026-27", {"award_name": "YellowJacket Scholarship"}]
- source_not_fetched: data/institutions/letu/credit_policies/2026-27.json ["credit_policies", "ipeds-226231", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/letu/credit_policies/2026-27.json ["credit_policies", "ipeds-226231", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/letu/credit_policies/2026-27.json ["credit_policies", "ipeds-226231", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/lcu/awards/2026-27.json ["awards", "ipeds-226383", null, "2026-27", {"award_name": "Scholarships: GPA 4.00"}]
- source_not_fetched: data/institutions/lcu/awards/2026-27.json ["awards", "ipeds-226383", null, "2026-27", {"award_name": "Scholarships: GPA 3.90-3.99"}]
- source_not_fetched: data/institutions/lcu/awards/2026-27.json ["awards", "ipeds-226383", null, "2026-27", {"award_name": "Scholarships: GPA 3.50-3.89"}]
- source_not_fetched: data/institutions/lcu/awards/2026-27.json ["awards", "ipeds-226383", null, "2026-27", {"award_name": "Scholarships: GPA Below 3.5"}]
- source_not_fetched: data/institutions/lcu/credit_policies/2026-27.json ["credit_policies", "ipeds-226383", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/lcu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-226383", null, "2026-27", {}]
- source_not_fetched: data/institutions/midland/credit_policies/2026-27.json ["credit_policies", "ipeds-226806", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/msutexas/awards/2026-27.json ["awards", "ipeds-226833", null, "2026-27", {"award_name": "Regents Valedictorian"}]
- source_not_fetched: data/institutions/msutexas/awards/2026-27.json ["awards", "ipeds-226833", null, "2026-27", {"award_name": "Dual Credit Award"}]
- source_not_fetched: data/institutions/msutexas/awards/2026-27.json ["awards", "ipeds-226833", null, "2026-27", {"award_name": "ISD Valedictorian/Salutatorian\u2020\u2020\u2020"}]
- source_not_fetched: data/institutions/msutexas/credit_policies/2026-27.json ["credit_policies", "ipeds-226833", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/msutexas/credit_policies/2026-27.json ["credit_policies", "ipeds-226833", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/na/awards/2026-27.json ["awards", "ipeds-461795", null, "2026-27", {"award_name": "Stallion Excellence \u2013 Level 1"}]
- source_not_fetched: data/institutions/na/awards/2026-27.json ["awards", "ipeds-461795", null, "2026-27", {"award_name": "Stallion Excellence \u2013 Level 2"}]
- source_not_fetched: data/institutions/na/awards/2026-27.json ["awards", "ipeds-461795", null, "2026-27", {"award_name": "Stallion Excellence \u2013 Level 3"}]
- source_not_fetched: data/institutions/na/transfer_policies/2026-27.json ["transfer_policies", "ipeds-461795", null, "2026-27", {}]
- source_not_fetched: data/institutions/ntcc/credit_policies/2026-27.json ["credit_policies", "ipeds-227225", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ollusa/awards/2026-27.json ["awards", "ipeds-227331", null, "2026-27", {"award_name": "Your Good Grades Guarantee Your OLLU Scholarship: Your GPA 3.75 to 3.99"}]
- source_not_fetched: data/institutions/ollusa/awards/2026-27.json ["awards", "ipeds-227331", null, "2026-27", {"award_name": "Your Good Grades Guarantee Your OLLU Scholarship: Your GPA 2.75 to 2.99"}]
- source_not_fetched: data/institutions/ollusa/awards/2026-27.json ["awards", "ipeds-227331", null, "2026-27", {"award_name": "Your Good Grades Guarantee Your OLLU Scholarship: Your GPA 3.50 to 3.74"}]
- source_not_fetched: data/institutions/ollusa/awards/2026-27.json ["awards", "ipeds-227331", null, "2026-27", {"award_name": "Your Good Grades Guarantee Your OLLU Scholarship: Your GPA 3.25 to 3.49"}]
- source_not_fetched: data/institutions/ollusa/awards/2026-27.json ["awards", "ipeds-227331", null, "2026-27", {"award_name": "Your Good Grades Guarantee Your OLLU Scholarship: Your GPA 3.00 to 3.24"}]
- source_not_fetched: data/institutions/ollusa/awards/2026-27.json ["awards", "ipeds-227331", null, "2026-27", {"award_name": "Your Good Grades Guarantee Your OLLU Scholarship: Your GPA 4.0 and above"}]
- source_not_fetched: data/institutions/ollusa/awards/2026-27.json ["awards", "ipeds-227331", null, "2026-27", {"award_name": "Your Good Grades Guarantee Your OLLU Scholarship: Your GPA 2.50 to 2.74"}]
- source_not_fetched: data/institutions/pvamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-227526", null, "2026-27", {"program_key": "chemical-engineering-bsche", "requirement_key": "major-15-chemistry-electives"}]
- source_not_fetched: data/institutions/smu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-228246", null, "2026-27", {}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Award of Excellence"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Trustee Award"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Presidential Award"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Academic Dean Award"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Achievement Award"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Admission Award ++"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Southwestern Scholar"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Admission Award"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Student Association President"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Senior Class President"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Senior Class Valedictorian"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Student Association Vice President"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Yearbook Editor"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Newspaper Editor"}]
- source_not_fetched: data/institutions/swau/awards/2026-27.json ["awards", "ipeds-228468", null, "2026-27", {"award_name": "Pathfinder Team Leadership Training Certificate (TLTC)"}]
- source_not_fetched: data/institutions/swau/credit_policies/2026-27.json ["credit_policies", "ipeds-228468", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/southwestern/credit_policies/2026-27.json ["credit_policies", "ipeds-228343", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/southwestern/credit_policies/2026-27.json ["credit_policies", "ipeds-228343", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/southwestern/transfer_policies/2026-27.json ["transfer_policies", "ipeds-228343", null, "2026-27", {}]
- source_not_fetched: data/institutions/stmarytx/credit_policies/2026-27.json ["credit_policies", "ipeds-228149", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/stmarytx/credit_policies/2026-27.json ["credit_policies", "ipeds-228149", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/stmarytx/credit_policies/2026-27.json ["credit_policies", "ipeds-228149", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/tccd/credit_policies/2026-27.json ["credit_policies", "ipeds-228547", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/tccd/credit_policies/2026-27.json ["credit_policies", "ipeds-228547", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/texarkanacollege/credit_policies/2026-27.json ["credit_policies", "ipeds-228699", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/texarkanacollege/credit_policies/2026-27.json ["credit_policies", "ipeds-228699", null, "2026-27", {"policy_kind": "AP"}]
- nothing_to_check: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "ecology-and-conservation-biology-bs-ecoinformatics-track", "requirement_key": "sample-plan"}] year=2027-28
- nothing_to_check: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "ecology-and-conservation-biology-bs-ecology-and-conservation-biology-track", "requirement_key": "sample-plan"}] year=2027-28
- nothing_to_check: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "ecology-and-conservation-biology-bs-vertebrate-zoology-track", "requirement_key": "sample-plan"}] year=2027-28
- nothing_to_check: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "horticulture-bs", "requirement_key": "sample-plan"}] year=2027-28
- nothing_to_check: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "environmental-studies-bs", "requirement_key": "sample-plan"}] year=2027-28
- source_not_fetched: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "geology-bs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "geophysics-bs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "global-studies-ba", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/tamu/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228723", null, "2026-27", {"program_key": "applied-mathematics-bs-biological-science-emphasis", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/tamucc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-224147", null, "2026-27", {"program_key": "philosophy-ba", "requirement_key": "major-4-metaphysics-and-epistemology"}]
- source_not_fetched: data/institutions/tamucc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-224147", null, "2026-27", {"program_key": "special-education-bs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/tamuct/credit_policies/2026-27.json ["credit_policies", "ipeds-483036", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "bs-computer-science", "requirement_key": "department-probation-and-withdrawal-departmental-requirements"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "bs-cyber-engineering-technology", "requirement_key": "department-probation-and-withdrawal-major-electives"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "bs-public-health", "requirement_key": "bs-public-health-biomedical-sciences"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "bs-psychology", "requirement_key": "bs-psychology-capstone"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "ba-history-with-teacher-certification", "requirement_key": "general-requirements-major-required-courses"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "ba-english-literature-emphasis-concentration", "requirement_key": "general-requirements-core-curriculum"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "ba-english-writing-media-and-culture-concentration", "requirement_key": "general-requirements-core-curriculum"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "ba-english-writing-media-and-culture-concentration", "requirement_key": "general-requirements-required-major-courses"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "ba-english-with-teacher-certification", "requirement_key": "general-requirements-major-required-courses"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "bs-biology-pre-health-professions-concentration", "requirement_key": "general-requirements-concentration-required-courses"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "bba-accounting", "requirement_key": "bba-accounting-business-core-upper-level"}]
- source_not_fetched: data/institutions/tamusa/degree_requirements/2026-27.json ["degree_requirements", "ipeds-459949", null, "2026-27", {"program_key": "bba-finance", "requirement_key": "general-requirements-business-core-upper-level"}]
- source_not_fetched: data/institutions/tcu/credit_policies/2026-27.json ["credit_policies", "ipeds-228875", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/tcu/credit_policies/2026-27.json ["credit_policies", "ipeds-228875", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/tcu/credit_policies/2026-27.json ["credit_policies", "ipeds-228875", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/tlu/credit_policies/2026-27.json ["credit_policies", "ipeds-228981", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/tlu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-228981", null, "2026-27", {}]
- source_not_fetched: data/institutions/tsu/awards/2026-27.json ["awards", "ipeds-229063", null, "2026-27", {"award_name": "Presidents Transformation"}]
- source_not_fetched: data/institutions/tsu/awards/2026-27.json ["awards", "ipeds-229063", null, "2026-27", {"award_name": "Regents"}]
- source_not_fetched: data/institutions/tsu/awards/2026-27.json ["awards", "ipeds-229063", null, "2026-27", {"award_name": "Tiger Genesis"}]
- source_not_fetched: data/institutions/tsu/awards/2026-27.json ["awards", "ipeds-229063", null, "2026-27", {"award_name": "Tiger P.A.W (Providing A Way)"}]
- source_not_fetched: data/institutions/tsu/credit_policies/2026-27.json ["credit_policies", "ipeds-229063", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/tsc/costs/2026-27.json ["costs", "ipeds-227377", null, "2026-27", {"residency": "in_state"}]
- source_not_fetched: data/institutions/tsc/costs/2026-27.json ["costs", "ipeds-227377", null, "2026-27", {"residency": "out_of_state"}]
- source_not_fetched: data/institutions/txst/awards/2026-27.json ["awards", "ipeds-228459", null, "2026-27", {"award_name": "military benefits"}]
- source_not_fetched: data/institutions/txst/awards/2026-27.json ["awards", "ipeds-228459", null, "2026-27", {"award_name": "international issues"}]
- source_not_fetched: data/institutions/txst/transfer_policies/2026-27.json ["transfer_policies", "ipeds-228459", null, "2026-27", {}]
- source_not_fetched: data/institutions/utdallas/academic_programs/2026-27.json ["academic_programs", "ipeds-228787", null, "2026-27", {"program_key": "economics-ba-bs"}]
- source_not_fetched: data/institutions/utdallas/academic_programs/2026-27.json ["academic_programs", "ipeds-228787", null, "2026-27", {"program_key": "international-political-economy-ba-bs"}]
- source_not_fetched: data/institutions/utdallas/academic_programs/2026-27.json ["academic_programs", "ipeds-228787", null, "2026-27", {"program_key": "biology-ba-bs"}]
- source_not_fetched: data/institutions/utdallas/academic_programs/2026-27.json ["academic_programs", "ipeds-228787", null, "2026-27", {"program_key": "chemistry-ba-bs"}]
- source_not_fetched: data/institutions/utdallas/academic_programs/2026-27.json ["academic_programs", "ipeds-228787", null, "2026-27", {"program_key": "mathematics-ba-bs"}]
- source_not_fetched: data/institutions/utdallas/academic_programs/2026-27.json ["academic_programs", "ipeds-228787", null, "2026-27", {"program_key": "physics-ba-bs"}]
- all_values_found_year_not_labeled: data/institutions/utep/credit_policies/2026-27.json ["credit_policies", "ipeds-228796", null, "2026-27", {"policy_kind": "IB"}]
- all_values_found_year_not_labeled: data/institutions/utep/credit_policies/2026-27.json ["credit_policies", "ipeds-228796", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/utep/degree_requirements/2026-27.json ["degree_requirements", "ipeds-228796", null, "2026-27", {"program_key": "rn-to-bsn-online-degree", "requirement_key": "major-3-electives"}]
- source_not_fetched: data/institutions/uttyler/credit_policies/2026-27.json ["credit_policies", "ipeds-228802", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/tjc/credit_policies/2026-27.json ["credit_policies", "ipeds-229355", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/tjc/credit_policies/2026-27.json ["credit_policies", "ipeds-229355", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/tjc/credit_policies/2026-27.json ["credit_policies", "ipeds-229355", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/udallas/transfer_policies/2026-27.json ["transfer_policies", "ipeds-224323", null, "2026-27", {}]
- source_not_fetched: data/institutions/uhcl/credit_policies/2026-27.json ["credit_policies", "ipeds-225414", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/umhb/credit_policies/2026-27.json ["credit_policies", "ipeds-226471", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/vernoncollege/credit_policies/2026-27.json ["credit_policies", "ipeds-229504", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/wc/credit_policies/2026-27.json ["credit_policies", "ipeds-229799", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/wtamu/credit_policies/2026-27.json ["credit_policies", "ipeds-229814", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/wtamu/credit_policies/2026-27.json ["credit_policies", "ipeds-229814", null, "2026-27", {"policy_kind": "IB"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Austin Community College District: admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Collin County Community College District: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Dallas College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Houston Community College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Lone Star College System: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Sam Houston State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- San Antonio College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- San Jacinto Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Tarleton State University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Texas A & M University-College Station: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- The University of Texas Rio Grande Valley: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- The University of Texas at Arlington: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- The University of Texas at Austin: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- The University of Texas at El Paso: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- University of Houston: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- University of Houston-Downtown: tuition_fees, cost_of_attendance, merit_scholarships
- University of North Texas: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
