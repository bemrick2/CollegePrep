# Review queue — HI (2026-27)

Pages fetched: 884; failures: 64. Candidates: 60 (9 without issues, 51 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 4 | 2 | 6 | 0 | 3 |
| cost_of_attendance | 0 | 0 | 3 | 1 | 8 | 0 | 3 |
| admissions_tests | 0 | 0 | 0 | 0 | 12 | 0 | 3 |
| common_data_set | 0 | 0 | 0 | 0 | 4 | 8 | 3 |
| merit_scholarships | 0 | 0 | 0 | 0 | 11 | 1 | 3 |
| ap_credit | 0 | 0 | 1 | 3 | 5 | 3 | 3 |
| clep_credit | 0 | 0 | 1 | 1 | 5 | 5 | 3 |
| ib_credit | 0 | 0 | 1 | 1 | 2 | 8 | 3 |
| dual_enrollment | 0 | 0 | 0 | 0 | 8 | 4 | 3 |
| transfer_credit | 0 | 0 | 0 | 1 | 11 | 0 | 3 |
| statewide_articulation | 0 | 0 | 0 | 0 | 6 | 6 | 3 |
| residency | 0 | 0 | 0 | 0 | 9 | 3 | 3 |
| degree_requirements | 0 | 0 | 0 | 0 | 11 | 1 | 3 |
| aid_appeals | 0 | 0 | 0 | 9 | 1 | 2 | 3 |

## Ready for review (9)

### `dd6010c3bd9e97bb` Chaminade University of Honolulu — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://chaminade.edu/financial-aid/cost-of-attendance/undergrad/ (sha256 083e41a5f325)
- checks: {"columns": 3, "rows": 3}
  - on_campus:Tuition: 33950 ⟵ “Tuition | $33,950 | $33,950 | $33,950”
  - on_campus:Books & Supplies: 3000 ⟵ “Books & Supplies | $3,000 | $3,000 | $3,000”
  - on_campus:Room & Board*: 19510 ⟵ “Room & Board* | $19,510 | $18,000 | $2,700”
  - off_campus_not_with_family:Tuition: 33950 ⟵ “Tuition | $33,950 | $33,950 | $33,950”
  - off_campus_not_with_family:Books & Supplies: 3000 ⟵ “Books & Supplies | $3,000 | $3,000 | $3,000”
  - off_campus_not_with_family:Room & Board*: 18000 ⟵ “Room & Board* | $19,510 | $18,000 | $2,700”
  - with_parents_or_family:Tuition: 33950 ⟵ “Tuition | $33,950 | $33,950 | $33,950”
  - with_parents_or_family:Books & Supplies: 3000 ⟵ “Books & Supplies | $3,000 | $3,000 | $3,000”
  - with_parents_or_family:Room & Board*: 2700 ⟵ “Room & Board* | $19,510 | $18,000 | $2,700”
### `4764687b35562ac1` Kapiolani Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.kapiolani.hawaii.edu/wp-content/uploads/Advanced-Placement-Examinations.pdf (sha256 0321ccb0294e)
- checks: {"distinct_exams": 19, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3-5]:  ⟵ “2-D Art & Design                                3-5       3 credits of ART DA”
  - equivalencies[AP-3-D-ART-DESIGN|3-5]:  ⟵ “3-D Art & Design                                3-5       3 credits of ART DA”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3-5]:  ⟵ “Business with Personal Finance                  3-5       3 credits of Elective for AA Degree (ELCT 999)”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                      3        3 credits of Elective for AA Degree (ELCT 999)”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3-5]:  ⟵ “Comparative Government and Politics   3-5   3 credits of POLS 110”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3-5]:  ⟵ “Computer Science A                    3-5   4 credits of ICS 111”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3-5]:  ⟵ “Computer Science Principles           3-5   3 credits of Elective for AA Degree (ELCT 999)”
  - equivalencies[AP-CYBERSECURITY|3-5]:  ⟵ “Cybersecurity                         3-5   3 credits of Elective for AA Degree (ELCT 999)”
  - equivalencies[AP-DRAWING|3-5]:  ⟵ “Drawing                               3-5   3 credits of ART DA”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science                 3-5   3 credits of OCN DB”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “French Language & Culture         3-5   3 credits of FR 202”
  - equivalencies[AP-MUSIC-THEORY|3-5]:  ⟵ “Music Theory                      3-5   3 credits of MUS 108”
  - equivalencies[AP-PHYSICS-1|3-5]:  ⟵ “Physics 1: Algebra-Based          3-5   4 credits of PHYS 151 & 151L”
  - equivalencies[AP-PHYSICS-2|3-5]:  ⟵ “Physics 2: Algebra-Based                3-5   4 credits of PHYS 152 & 152L”
  - equivalencies[AP-PSYCHOLOGY|3-5]:  ⟵ “Psychology                              3-5   3 credits of PSY 100”
  - equivalencies[AP-RESEARCH|3-5]:  ⟵ “Research                                3-5   3 credits of Elective for AA Degree (ELCT 999)”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|4]:  ⟵ “Spanish Literature & Culture            4     3 credits of SPAN DL”
  - equivalencies[AP-STATISTICS|3-5]:  ⟵ “Statistics                              3-5   3 credits of MATH 115”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3-5]:  ⟵ “United States Government and Politics   3-5   3 credits of POLS 130”
### `854741122a6617fe` Kapiolani Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.kapiolani.hawaii.edu/wp-content/uploads/College-Level-Examination-Program-CLEP.pdf (sha256 e7e768f1c0ea)
- checks: {"distinct_exams": 21, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “AMERICAN GOVERNMENT                       50    3 credits for POLS 130”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “AMERICAN LITERATURE                       50    3 credits for ENG 270”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “BIOLOGY                                   50    6 credits of BIOL 171 & 172”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “CHEMISTRY                                 50    6 credits for CHEM 100”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “COLLEGE ALGEBRA                           50    3 credits for MATH 103”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “COLLEGE COMPOSITION                       50    3 credits for ENG 100”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “COLLEGE COMPOSITION MODULAR               50    3 credits for ELCT 999”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “*COLLEGE MATHEMATICS                      50    6 credits for ELCT 999”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “ENGLISH LITERATURE                        50    3 credits for ENG DL”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “FINANCIAL ACCOUNTING                      50    3 credits for ACC 201”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “HISTORY OF THE UNITED STATES I                   50         3 credits for HIST 281”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “HISTORY OF THE UNITED STATES II                  50         3 credits for HIST 282”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “HUMAN GROWTH & DEVELOPMENT                       50         3 credits for PSY 240”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “*HUMANITIES                                      50         3 credits for OTHA DH”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “INTRODUCTORY BUSINESS LAW                        50         3 credits for BLAW 200”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “INTRODUCTORY PSYCHOLOGY                          50         3 credits for PSY 100”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “INTRODUCTORY SOCIOLOGY                           50         3 credits for SOC 100”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “PRECALCULUS                                      50         3 credits for MATH 140”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “PRINCIPLES OF MACROECONOMICS                     50         3 credits for ECON 131”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “PRINCIPLES OF MANAGEMENT                         50         3 credits for MGT 120”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “PRINCIPLES OF MICROECONOMICS                     50         3 credits for ECON 130”
### `fb872b1e33652955` Kapiolani Community College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.kapiolani.hawaii.edu/wp-content/uploads/International-Baccalaureate-factsheet.pdf (sha256 4eb7cb854023)
- checks: {"distinct_exams": 12, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5-7]:  ⟵ “ANTHROPOLOGY                                   5-7        3 credits of ANTH 152”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|5-7]:  ⟵ “ENGLISH A: LANGUAGE & LITERATURE               5-7        6 credits of ENG 100 & ENG 271”
  - equivalencies[IB-ENGLISH-A-LITERATURE|5-7]:  ⟵ “ENGLISH A: LITERATURE                          5-7        6 credits of ENG 271 & ENG 272”
  - equivalencies[IB-FILM|5-7]:  ⟵ “FILM                                           5-7        3 credits of ART DA”
  - equivalencies[IB-FRENCH|4-7]:  ⟵ “FRENCH A or B                                  4-7        3 credits of FR 202”
  - equivalencies[IB-GLOBAL-POLITICS|5-7]:  ⟵ “GLOBAL POLITICS                    5-7    3 credits of POLS 120”
  - equivalencies[IB-MUSIC|5-7]:  ⟵ “MUSIC                                                    5-7            3 credits of MUS 106”
  - equivalencies[IB-PHILOSOPHY|4-7]:  ⟵ “PHILOSOPHY                                               4-7            3 credits of PHIL 100”
  - equivalencies[IB-PSYCHOLOGY|5-7]:  ⟵ “PSYCHOLOGY                                               5-7            3 credits for PSY 100”
  - equivalencies[IB-SPANISH|5-7]:  ⟵ “SPANISH A or B                                           5-7            3 credits for SPAN 202”
  - equivalencies[IB-THEATRE|5-7]:  ⟵ “THEATRE                                                  5-7            3 credits of THEA 101”
  - equivalencies[IB-VISUAL-ARTS|5-7]:  ⟵ “VISUAL ARTS                                              5-7            3 credits of Diversification: Arts (DA)”
### `2f667a693763d98a` University of Hawaii at Manoa — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/admissions/financing/index.html (sha256 2ee10aa73f69)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Total:: 55760 ⟵ “Total: | $33,728 | $39,608 | $55,760”
  - on_campus:Tuition: 33792 ⟵ “Tuition | $11,760 | $17,640 | $33,792”
  - on_campus:University Fee: 914 ⟵ “University Fee | $914 | $914 | $914”
  - on_campus:Books & Supplies: 1330 ⟵ “Books & Supplies | $1,330 | $1,330 | $1,330”
  - on_campus:Housing/Food: 15690 ⟵ “Housing/Food | $15,690 | $15,690 | $15,690”
  - on_campus:Personal Expense: 2698 ⟵ “Personal Expense | $2,698 | $2,698 | $2,698”
  - on_campus:Transportation: 1336 ⟵ “Transportation | $1,336 | $1,336 | $1,336”
### `6037cf4335794acb` University of Hawaii at Manoa — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/admissions/financing/index.html (sha256 2ee10aa73f69)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Total:: 33728 ⟵ “Total: | $33,728 | $39,608 | $55,760”
  - on_campus:Tuition: 11760 ⟵ “Tuition | $11,760 | $17,640 | $33,792”
  - on_campus:University Fee: 914 ⟵ “University Fee | $914 | $914 | $914”
  - on_campus:Books & Supplies: 1330 ⟵ “Books & Supplies | $1,330 | $1,330 | $1,330”
  - on_campus:Housing/Food: 15690 ⟵ “Housing/Food | $15,690 | $15,690 | $15,690”
  - on_campus:Personal Expense: 2698 ⟵ “Personal Expense | $2,698 | $2,698 | $2,698”
  - on_campus:Transportation: 1336 ⟵ “Transportation | $1,336 | $1,336 | $1,336”
### `f7fddada9be94049` University of Hawaii-West Oahu — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://westoahu.hawaii.edu/financial-aid/cost-of-attendance/ (sha256 48d3d2a875e8)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition: 20592 ⟵ “Tuition | $20,592 | $20,592”
  - with_parents_or_family:Student Fees: 240 ⟵ “Student Fees | $240 | $240”
  - with_parents_or_family:Books and Supplies: 1450 ⟵ “Books and Supplies | $1,450 | $1,450”
  - with_parents_or_family:Living Expenses (Food & Housing): 8284 ⟵ “Living Expenses (Food & Housing) | $8,284 | $18,882”
  - with_parents_or_family:Transportation: 2672 ⟵ “Transportation | $2,672 | $2,672”
  - with_parents_or_family:Personal/Misc Expense: 2784 ⟵ “Personal/Misc Expense | $2,784 | $2,784”
  - with_parents_or_family:Total: 36022 ⟵ “Total | $36,022 | $46,620”
  - off_campus_not_with_family:Tuition: 20592 ⟵ “Tuition | $20,592 | $20,592”
  - off_campus_not_with_family:Student Fees: 240 ⟵ “Student Fees | $240 | $240”
  - off_campus_not_with_family:Books and Supplies: 1450 ⟵ “Books and Supplies | $1,450 | $1,450”
  - off_campus_not_with_family:Living Expenses (Food & Housing): 18882 ⟵ “Living Expenses (Food & Housing) | $8,284 | $18,882”
  - off_campus_not_with_family:Transportation: 2672 ⟵ “Transportation | $2,672 | $2,672”
  - off_campus_not_with_family:Personal/Misc Expense: 2784 ⟵ “Personal/Misc Expense | $2,784 | $2,784”
  - off_campus_not_with_family:Total: 46620 ⟵ “Total | $36,022 | $46,620”
### `7bcb2d8915602ad9` Windward Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://windward.hawaii.edu/paying-for-college/financial-aid/cost-of-attendance/ (sha256 6cb63267c63f)
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition: 8280 ⟵ “Tuition | $3,144 | $8,280 | $3,144 | $8,280”
  - with_parents_or_family:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50”
  - with_parents_or_family:Books/Supplies: 1450 ⟵ “Books/Supplies | $1,450 | $1,450 | $1,450 | $1,450”
  - with_parents_or_family:Transportation: 3458 ⟵ “Transportation | $3,458 | $3,458 | $3,458 | $3,458”
  - with_parents_or_family:Meals/Housing: 7948 ⟵ “Meals/Housing | $7,948 | $7,948 | $24,016 | $24,016”
  - with_parents_or_family:Personal Expenses: 2842 ⟵ “Personal Expenses | $2,842 | $2,842 | $2,842 | $2,842”
  - with_parents_or_family:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70 | $70”
  - with_parents_or_family:Total: 24098 ⟵ “Total | $18,962 | $24,098 | $35,030 | $40,166”
  - off_campus_not_with_family:Tuition: 8280 ⟵ “Tuition | $3,144 | $8,280 | $3,144 | $8,280”
  - off_campus_not_with_family:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50”
  - off_campus_not_with_family:Books/Supplies: 1450 ⟵ “Books/Supplies | $1,450 | $1,450 | $1,450 | $1,450”
  - off_campus_not_with_family:Transportation: 3458 ⟵ “Transportation | $3,458 | $3,458 | $3,458 | $3,458”
  - off_campus_not_with_family:Meals/Housing: 24016 ⟵ “Meals/Housing | $7,948 | $7,948 | $24,016 | $24,016”
  - off_campus_not_with_family:Personal Expenses: 2842 ⟵ “Personal Expenses | $2,842 | $2,842 | $2,842 | $2,842”
  - off_campus_not_with_family:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70 | $70”
  - off_campus_not_with_family:Total: 40166 ⟵ “Total | $18,962 | $24,098 | $35,030 | $40,166”
### `7d249b05fca7949d` Windward Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://windward.hawaii.edu/paying-for-college/financial-aid/cost-of-attendance/ (sha256 6cb63267c63f)
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition: 3144 ⟵ “Tuition | $3,144 | $8,280 | $3,144 | $8,280”
  - with_parents_or_family:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50”
  - with_parents_or_family:Books/Supplies: 1450 ⟵ “Books/Supplies | $1,450 | $1,450 | $1,450 | $1,450”
  - with_parents_or_family:Transportation: 3458 ⟵ “Transportation | $3,458 | $3,458 | $3,458 | $3,458”
  - with_parents_or_family:Meals/Housing: 7948 ⟵ “Meals/Housing | $7,948 | $7,948 | $24,016 | $24,016”
  - with_parents_or_family:Personal Expenses: 2842 ⟵ “Personal Expenses | $2,842 | $2,842 | $2,842 | $2,842”
  - with_parents_or_family:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70 | $70”
  - with_parents_or_family:Total: 18962 ⟵ “Total | $18,962 | $24,098 | $35,030 | $40,166”
  - off_campus_not_with_family:Tuition: 3144 ⟵ “Tuition | $3,144 | $8,280 | $3,144 | $8,280”
  - off_campus_not_with_family:Fees: 50 ⟵ “Fees | $50 | $50 | $50 | $50”
  - off_campus_not_with_family:Books/Supplies: 1450 ⟵ “Books/Supplies | $1,450 | $1,450 | $1,450 | $1,450”
  - off_campus_not_with_family:Transportation: 3458 ⟵ “Transportation | $3,458 | $3,458 | $3,458 | $3,458”
  - off_campus_not_with_family:Meals/Housing: 24016 ⟵ “Meals/Housing | $7,948 | $7,948 | $24,016 | $24,016”
  - off_campus_not_with_family:Personal Expenses: 2842 ⟵ “Personal Expenses | $2,842 | $2,842 | $2,842 | $2,842”
  - off_campus_not_with_family:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70 | $70”
  - off_campus_not_with_family:Total: 35030 ⟵ “Total | $18,962 | $24,098 | $35,030 | $40,166”

## Exceptions (51)

### `1a28350ddea0984d` Chaminade University of Honolulu — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://catalog.chaminade.edu/financialinformation/financialinformationug/financialaid/sap (sha256 a6b61f62bb75)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://catalog.chaminade.edu/financialinformation/financialinformationgrdo/financialaid/sap,https://chaminade.edu/financial-aid/financial-aid-awarding-policy/,https://chaminade.edu/financial-aid/financial-aid-resources/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “These requirements apply to all students as one determinant of eligibility for financial aid. ● SAP is calculated at the end of each academic year after grades have been posted to academic history by the Records Office. ● If your SAP status is Failure after the check is performed, you will not qualify for financial aid for the following term. ● If your SAP status is Failure and you cannot mathemat”
  - sentence: sap_appeal ⟵ “What happens when you do not meet the requirements? ● You are no longer eligible for federal financial aid – including federal FAFSA work study, loans, grants, or scholarships. ● Because you do not qualify for financial aid, you must pay your tuition and fees by the payment deadline or your registration may be subject to cancellation for the term. ● You are notified via the Self-Service Portal whe”
  - sentence: sap_appeal ⟵ “How do you regain eligibility? ● SAP Appeal – If mitigating circumstances during a specific term of enrollment prevented you from meeting the requirements, you may file an SAP Appeal.”
  - sentence: sap_appeal ⟵ “Examples include a medical doctor, clergy, professionals, professors, etc. ● The appeal form must be submitted to the Financial Aid Office within the prescribed dates as noted on the SAP Appeal Form.”
### `1dcac6efad9794a5` Chaminade University of Honolulu — appeals 2026-27 [new] (labeled_in_source)
- source: https://chaminade.edu/financial-aid/financial-aid-awarding-policy/ (sha256 aefeb49ec873)
- issues: semantic_review_required, conflicting_sources:https://catalog.chaminade.edu/financialinformation/financialinformationgrdo/financialaid/sap,https://catalog.chaminade.edu/financialinformation/financialinformationug/financialaid/sap,https://chaminade.edu/financial-aid/financial-aid-resources/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If your SAP status is Failure and you cannot mathematically attain SAP requirements, an appeal will not be permissible.”
  - sentence: sap_appeal ⟵ “You are notified via the Self-Service Portal when you have failed SAP and you can appeal by either following the link for instructions, or by contacting the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “SAP Appeal – If mitigating circumstances during a specific term of enrollment prevented you from meeting the requirements, you may file an SAP Appeal.”
  - sentence: sap_appeal ⟵ “The appeal form must be submitted to the Financial Aid Office within the prescribed dates as noted on the SAP Appeal Form.”
### `1f920cea22ed781e` Chaminade University of Honolulu — appeals 2026-27 [new] (source_unlabeled)
- source: https://chaminade.edu/financial-aid/professional-judgment-process-and-appeals/ (sha256 7fef2065d98a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Cost of Attendance (COA) Adjustment Appeal When additional education-related expenses beyond a student’s standard COA are incurred, they may request a COA adjustment by completing a Cost of Attendance Adjustment Request.”
### `3304596abbb1a11d` Chaminade University of Honolulu — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://catalog.chaminade.edu/financialinformation/financialinformationgrdo/financialaid/sap (sha256 dc9d66de4c30)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://catalog.chaminade.edu/financialinformation/financialinformationug/financialaid/sap,https://chaminade.edu/financial-aid/financial-aid-awarding-policy/,https://chaminade.edu/financial-aid/financial-aid-resources/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “These requirements apply to all students as one determinant of eligibility for financial aid. ● SAP is calculated at the end of each academic year after grades have been posted to academic history by the Records Office. ● If your SAP status is Failure after the check is performed, you will not qualify for financial aid for the following term. ● If your SAP status is Failure and you cannot mathemat”
  - sentence: sap_appeal ⟵ “What happens when you do not meet the requirements? ● You are no longer eligible for federal financial aid – including federal FAFSA work study, loans, grants, or scholarships. ● Because you do not qualify for financial aid, you must pay your tuition and fees by the payment deadline or your registration may be subject to cancellation for the term. ● You are notified via the Self-Service Portal whe”
  - sentence: sap_appeal ⟵ “How do you regain eligibility? ● SAP Appeal – If mitigating circumstances during a specific term of enrollment prevented you from meeting the requirements, you may file an SAP Appeal.”
  - sentence: sap_appeal ⟵ “Examples include a medical doctor, clergy, professionals, professors, etc. ● The appeal form must be submitted to the Financial Aid Office within the prescribed dates as noted on the SAP Appeal Form.”
### `4ad2795929ed98b7` Chaminade University of Honolulu — appeals 2026-27 [new] (source_unlabeled)
- source: https://chaminade.edu/financial-aid/Dependency%20Override%20Appeal%20Policy/ (sha256 ea45ac501e97)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “We do recognize that there are special circumstances in which students are not able to obtain parents’ information.”
### `6aadb3e579408892` Chaminade University of Honolulu — appeals 2026-27 [new] (source_unlabeled)
- source: https://chaminade.edu/financial-aid/professional-judgment-process-and-appeals/ (sha256 7fef2065d98a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: professional_judgment ⟵ “However, Federal regulations provide financial aid administrators with the authority to use their discretion or professional judgment to adjust, on a case-by-case basis and with adequate documentation, the data elements used on the Free Application for Federal Student Aid (FAFSA) that impact the Student Aid Index (SAI) to get a better picture of a student and their family’s ability to pay for coll”
  - sentence: professional_judgment ⟵ “Important to Note: A Professional Judgement review does not guarantee additional funding.”
  - sentence: professional_judgment ⟵ “All other discretionary expenses If the Student Aid Index (SAI) calculated from the FAFSA is zero To Request a Professional Judgment You must have a completed FAFSA submitted before an appeal can be considered To request an appeal, please call our office, explaining the qualifying reason you are requesting an appeal to be considered for review.”
  - sentence: professional_judgment ⟵ “Professional Judgment decisions are final.”
  - sentence: professional_judgment ⟵ “Congress delegated the authority to make professional judgment adjustments to the data elements on the Free Application for Federal Student Aid (FAFSA) to the college financial aid office and its assigned staff.”
### `7d0a8872b5b51ca5` Chaminade University of Honolulu — appeals 2026-27 [new] (source_unlabeled)
- source: https://chaminade.edu/financial-aid/Dependency%20Override%20Appeal%20Policy/ (sha256 ea45ac501e97)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “Students that are unable to complete the FAFSA with parental information can request a Dependency Override by contacting Student Financial Services.”
  - sentence: dependency_override ⟵ “Student Financial Services will review the Dependency Override request once all documentation has been received.”
  - sentence: dependency_override ⟵ “Student Financial Services reviews each request for Dependency Override on a case-by-case basis and students are required to complete the request on an annual basis since the override cannot be automatically renewed each year.”
### `cbeaf1257573de6e` Chaminade University of Honolulu — appeals 2024-25 [new] (labeled_in_source)
- source: https://chaminade.edu/financial-aid/undergraduate-scholarships-aid/ (sha256 1ace0befbea7)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment Process and Appeals The Higher Education Act establishes the Federal methodology (FM) formula used for determining eligibility for federal student financial aid programs.”
  - sentence: professional_judgment ⟵ “However, Federal regulations provide financial aid administrators with the authority to use their discretion or professional judgment to adjust, on a case-by-case basis and with adequate documentation, the data elements used on the Free Application for Federal Student Aid (FAFSA) that impact the Student Aid Index (SAI) to get a better picture of a student and their family’s ability to pay for coll”
### `d37002b111b7d11f` Chaminade University of Honolulu — appeals 2026-27 [new] (source_unlabeled)
- source: https://chaminade.edu/financial-aid/financial-aid-resources/satisfactory-academic-progress/ (sha256 27bf6041bc0f)
- issues: semantic_review_required, conflicting_sources:https://catalog.chaminade.edu/financialinformation/financialinformationgrdo/financialaid/sap,https://catalog.chaminade.edu/financialinformation/financialinformationug/financialaid/sap,https://chaminade.edu/financial-aid/financial-aid-awarding-policy/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP appeals may be submitted to the Office of Financial Aid in Clarence T.C.”
### `9a794b15fa5065e0` Chaminade University of Honolulu — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://chaminade.edu/financial-aid/cost-of-attendance/online/ (sha256 f3c067c406d2)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "rows": 3}
  - column:Tuition: 12000 ⟵ “Tuition | $12,000 | $20,880 | $28,800”
  - column:Books & Supplies: 2000 ⟵ “Books & Supplies | $2,000 | $2,000 | $2,000”
  - column:Room & Board*: 21600 ⟵ “Room & Board* | $21,600 | $21,600 | $21,600”
  - other:Tuition: 20880 ⟵ “Tuition | $12,000 | $20,880 | $28,800”
  - other:Books & Supplies: 2000 ⟵ “Books & Supplies | $2,000 | $2,000 | $2,000”
  - other:Room & Board*: 21600 ⟵ “Room & Board* | $21,600 | $21,600 | $21,600”
  - column:Tuition: 28800 ⟵ “Tuition | $12,000 | $20,880 | $28,800”
  - column:Books & Supplies: 2000 ⟵ “Books & Supplies | $2,000 | $2,000 | $2,000”
  - column:Room & Board*: 21600 ⟵ “Room & Board* | $21,600 | $21,600 | $21,600”
### `807483fe4e64264b` Chaminade University of Honolulu — transfer_policies 2026-27 [new] (ambiguous_year_labels)
- source: https://catalog.chaminade.edu/academic-programs/psychology/psyd/transfer (sha256 eaeb25ba4b45)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_grade"]}
  - min_grade: B ⟵ “For a course to be considered eligible for transfer credit, the following conditions must be met: · The course must have been taken no more than 5 years before entry to HSPP. · The course grade must be a grade of “B” or higher. · The course must have been a graduate-level course, taken for graduate-level credit from a regionally accredited college or university.”
### `6984a2f8cef915a5` Hawaii Pacific University — appeals 2026-27 [new] (source_unlabeled)
- source: https://forms.hpu.edu/view.php?id=70136 (sha256 fb57af8d4e85)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Merit Scholarship Appeal Merit Scholarship Appeal Merit Scholarship Appeal Please note that we cannot guarantee that a submission of an appeal will result in an increase to your aid award.”
### `c082512745db113e` Hawaii Pacific University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.hpu.edu/financial-aid/additional-aid-appeals.html (sha256 b030be9b94de)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Note: *There is no guarantee that your financial aid award package will increase as a result of pursuing an appeal. *If your FAFSA shows your Student Aid Index (SAI) is less than or equal to 0, you have been awarded the maximum amount of federal aid and are ineligible to apply for a Professional Judgment Appeal.”
  - sentence: professional_judgment ⟵ “Important Dates: 2025-2026 Professional Judgment (PJ) Deadline: 04/01/2026 - CLOSED 2026-2027 Professional Judgment (PJ) Deadline: 04/01/2027 Reviews for 2026-2027 PJs & Institutional Aid Appeals Will Begin: 05/01/2026 PLEASE GATHER ALL THE REQUESTED DOCUMENTS BELOW PRIOR TO SUBMISSION TO PREVENT DELAYS IN THE REVIEW PROCESS.”
  - sentence: professional_judgment ⟵ “Required Documents for Appeals 2026-2027 Professional Judgment A signed copy of the 2024 Federal 1040 Tax Return (parent(s) taxes for dependent students and student's taxes (spouse if applicable) for independent students).”
  - sentence: professional_judgment ⟵ “APPEAL SUBMISSION LINKS PROFESSIONAL JUDGMENT APPEAL FOR SPECIAL CIRCUMSTANCES E.g., Significant Income Adjustments (retirement, reductions, loss of employment, divorce/seperation), etc. not initially reported on the FAFSA. 2026-2027 Professional Judgment Appeal 2026-2027 INSTITUTIONAL AID APPEAL Request a review for additional institutional aid to assist with tuition.”
### `b21a15a81fe203a1` Hawaii Pacific University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.hpu.edu/financial-aid/cost-of-attendance.html (sha256 faec5e81bbd1)
- issues: arrangement_unlabeled, stacked_header_unparsed
- checks: {"columns": 6, "components_reconcile": true, "rows": 9}
  - column:Tuition: 44616 ⟵ “Tuition | $44,616 | $44,616 | $44,616 |  | $37,536 | $37,536 | $37,536”
  - column:Fees: 1070 ⟵ “Fees | $1,070 | $1,070 | $1,070 |  | $1,070 | $1,070 | $1,070”
  - column:Books*: 800 ⟵ “Books* | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $132 | $132 | $132 |  | $132 | $132 | $132”
  - column:Personal Expenses: 800 ⟵ “Personal Expenses | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:PLUS Loan Fees**: 846 ⟵ “PLUS Loan Fees** | $846 | $846 | $846 |  | $846 | $846 | $846”
  - column:Food & Housing***: 22024 ⟵ “Food & Housing*** | $22,024 | $22,024 | $7,344 |  | $22,024 | $22,024 | $7,344”
  - column:Transportation: 2600 ⟵ “Transportation | $2,600 | $2,600 | $1,300 |  | $2,600 | $2,600 | $1,300”
  - column:TOTAL: 72888 ⟵ “TOTAL | $72,888 | $72,888 | $56,908 |  | $65,808 | $65,808 | $49,828”
  - column:Tuition: 44616 ⟵ “Tuition | $44,616 | $44,616 | $44,616 |  | $37,536 | $37,536 | $37,536”
  - column:Fees: 1070 ⟵ “Fees | $1,070 | $1,070 | $1,070 |  | $1,070 | $1,070 | $1,070”
  - column:Books*: 800 ⟵ “Books* | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $132 | $132 | $132 |  | $132 | $132 | $132”
  - column:Personal Expenses: 800 ⟵ “Personal Expenses | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:PLUS Loan Fees**: 846 ⟵ “PLUS Loan Fees** | $846 | $846 | $846 |  | $846 | $846 | $846”
  - column:Food & Housing***: 22024 ⟵ “Food & Housing*** | $22,024 | $22,024 | $7,344 |  | $22,024 | $22,024 | $7,344”
  - column:Transportation: 2600 ⟵ “Transportation | $2,600 | $2,600 | $1,300 |  | $2,600 | $2,600 | $1,300”
  - column:TOTAL: 72888 ⟵ “TOTAL | $72,888 | $72,888 | $56,908 |  | $65,808 | $65,808 | $49,828”
  - column:Tuition: 44616 ⟵ “Tuition | $44,616 | $44,616 | $44,616 |  | $37,536 | $37,536 | $37,536”
  - column:Fees: 1070 ⟵ “Fees | $1,070 | $1,070 | $1,070 |  | $1,070 | $1,070 | $1,070”
  - column:Books*: 800 ⟵ “Books* | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $132 | $132 | $132 |  | $132 | $132 | $132”
  - column:Personal Expenses: 800 ⟵ “Personal Expenses | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:PLUS Loan Fees**: 846 ⟵ “PLUS Loan Fees** | $846 | $846 | $846 |  | $846 | $846 | $846”
  - column:Food & Housing***: 7344 ⟵ “Food & Housing*** | $22,024 | $22,024 | $7,344 |  | $22,024 | $22,024 | $7,344”
  - … 29 more rows
### `ed7ff879a5cf78f1` Hawaii Pacific University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.hpu.edu/financial-aid/archives/cost-of-attendance-25-26.html (sha256 ed31bef130af)
- issues: arrangement_unlabeled, stacked_header_unparsed, stale_year_label:2025-26
- checks: {"columns": 6, "components_reconcile": true, "rows": 9}
  - column:BOOKS*: 800 ⟵ “BOOKS* | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:FEES: 950 ⟵ “FEES | $950 | $950 | $950 |  | $950 | $950 | $950”
  - column:LOAN FEES: 82 ⟵ “LOAN FEES | $82 | $82 | $82 |  | $82 | $82 | $82”
  - column:PERSONAL: 800 ⟵ “PERSONAL | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:PLUS LOAN FEES*: 1100 ⟵ “PLUS LOAN FEES* | $1,100** | $1,100** | $1,100** |  | $1,100** | $1,100** | $1,100**”
  - column:FOOD and HOUSING: 20976 ⟵ “FOOD and HOUSING | $20,976 | $6,994 | $20,976 |  | $20,976 | $6,994 | $20,976”
  - column:TRANSPORTATION: 2600 ⟵ “TRANSPORTATION | $2,600 | $1,300 | $2,600 |  | $2,600 | $1,300 | $2,600”
  - column:TUITION: 42528 ⟵ “TUITION | $42,528 | $42,528 | $42,528 |  | $35,784 | $35,784 | $35,784”
  - column:TOTAL: 69836 ⟵ “TOTAL | $69,836 | $54,554 | $69,836 |  | $63,092 | $47,810 | $63,092”
  - column:BOOKS*: 800 ⟵ “BOOKS* | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:FEES: 950 ⟵ “FEES | $950 | $950 | $950 |  | $950 | $950 | $950”
  - column:LOAN FEES: 82 ⟵ “LOAN FEES | $82 | $82 | $82 |  | $82 | $82 | $82”
  - column:PERSONAL: 800 ⟵ “PERSONAL | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:PLUS LOAN FEES*: 1100 ⟵ “PLUS LOAN FEES* | $1,100** | $1,100** | $1,100** |  | $1,100** | $1,100** | $1,100**”
  - column:FOOD and HOUSING: 6994 ⟵ “FOOD and HOUSING | $20,976 | $6,994 | $20,976 |  | $20,976 | $6,994 | $20,976”
  - column:TRANSPORTATION: 1300 ⟵ “TRANSPORTATION | $2,600 | $1,300 | $2,600 |  | $2,600 | $1,300 | $2,600”
  - column:TUITION: 42528 ⟵ “TUITION | $42,528 | $42,528 | $42,528 |  | $35,784 | $35,784 | $35,784”
  - column:TOTAL: 54554 ⟵ “TOTAL | $69,836 | $54,554 | $69,836 |  | $63,092 | $47,810 | $63,092”
  - column:BOOKS*: 800 ⟵ “BOOKS* | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:FEES: 950 ⟵ “FEES | $950 | $950 | $950 |  | $950 | $950 | $950”
  - column:LOAN FEES: 82 ⟵ “LOAN FEES | $82 | $82 | $82 |  | $82 | $82 | $82”
  - column:PERSONAL: 800 ⟵ “PERSONAL | $800 | $800 | $800 |  | $800 | $800 | $800”
  - column:PLUS LOAN FEES*: 1100 ⟵ “PLUS LOAN FEES* | $1,100** | $1,100** | $1,100** |  | $1,100** | $1,100** | $1,100**”
  - column:FOOD and HOUSING: 20976 ⟵ “FOOD and HOUSING | $20,976 | $6,994 | $20,976 |  | $20,976 | $6,994 | $20,976”
  - column:TRANSPORTATION: 2600 ⟵ “TRANSPORTATION | $2,600 | $1,300 | $2,600 |  | $2,600 | $1,300 | $2,600”
  - … 29 more rows
### `fe5862d3f6173f54` Hawaii Pacific University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.hpu.edu/financial-aid/archives/cost-of-attendance-24-25.html (sha256 dd6305ff01f0)
- issues: arrangement_unlabeled, stacked_header_unparsed, stale_year_label:2024-25
- checks: {"columns": 4, "components_reconcile": true, "rows": 9}
  - column:BOOKS*: 972 ⟵ “BOOKS* | $972 | $972 |  | $872 | $872”
  - column:FEES: 3620 ⟵ “FEES | $3620 | $3620 |  | $600 | $600”
  - column:LOAN FEES: 82 ⟵ “LOAN FEES | $82 | $82 |  | $82 | $82”
  - column:PERSONAL: 800 ⟵ “PERSONAL | $800 | $800 |  | $800 | $800”
  - column:PLUS LOAN FEES*: 1100 ⟵ “PLUS LOAN FEES* | $1,100** | $1,100** |  | $1,100** | $1,100**”
  - column:FOOD and HOUSING: 21050 ⟵ “FOOD and HOUSING | $21,050 | $21,050 |  | $21,050 | $21,050”
  - column:TRANSPORTATION: 2600 ⟵ “TRANSPORTATION | $2,600 | $600 |  | $2,600 | $600”
  - column:TUITION: 40152 ⟵ “TUITION | $40,152 | $40,152 |  | $33,792 | $33,792”
  - column:TOTAL: 70376 ⟵ “TOTAL | $70,376 | $68,376 |  | $60,896 | $58,896”
  - column:BOOKS*: 972 ⟵ “BOOKS* | $972 | $972 |  | $872 | $872”
  - column:FEES: 3620 ⟵ “FEES | $3620 | $3620 |  | $600 | $600”
  - column:LOAN FEES: 82 ⟵ “LOAN FEES | $82 | $82 |  | $82 | $82”
  - column:PERSONAL: 800 ⟵ “PERSONAL | $800 | $800 |  | $800 | $800”
  - column:PLUS LOAN FEES*: 1100 ⟵ “PLUS LOAN FEES* | $1,100** | $1,100** |  | $1,100** | $1,100**”
  - column:FOOD and HOUSING: 21050 ⟵ “FOOD and HOUSING | $21,050 | $21,050 |  | $21,050 | $21,050”
  - column:TRANSPORTATION: 600 ⟵ “TRANSPORTATION | $2,600 | $600 |  | $2,600 | $600”
  - column:TUITION: 40152 ⟵ “TUITION | $40,152 | $40,152 |  | $33,792 | $33,792”
  - column:TOTAL: 68376 ⟵ “TOTAL | $70,376 | $68,376 |  | $60,896 | $58,896”
  - column:BOOKS*: 872 ⟵ “BOOKS* | $972 | $972 |  | $872 | $872”
  - column:FEES: 600 ⟵ “FEES | $3620 | $3620 |  | $600 | $600”
  - column:LOAN FEES: 82 ⟵ “LOAN FEES | $82 | $82 |  | $82 | $82”
  - column:PERSONAL: 800 ⟵ “PERSONAL | $800 | $800 |  | $800 | $800”
  - column:PLUS LOAN FEES*: 1100 ⟵ “PLUS LOAN FEES* | $1,100** | $1,100** |  | $1,100** | $1,100**”
  - column:FOOD and HOUSING: 21050 ⟵ “FOOD and HOUSING | $21,050 | $21,050 |  | $21,050 | $21,050”
  - column:TRANSPORTATION: 2600 ⟵ “TRANSPORTATION | $2,600 | $600 |  | $2,600 | $600”
  - … 11 more rows
### `2f6d45ee888776e6` Hawaii Pacific University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.hpu.edu/undergraduate-admissions/transfer/ap/index.html (sha256 1de25581a92d)
- issues: score_column_not_scores, score_scale_mismatch, course_column_missing
- checks: {"distinct_exams": 3, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[AP-MUSIC-THEORY|MUS 2400: Music Theory]:  ⟵ “MUSIC THEORY | 4, 5 | MUS 2400: Music Theory | 3”
  - equivalencies[AP-MUSIC-THEORY|3, 4, 5]:  ⟵ “MUSIC THEORY | STUDIO ART 2-D DESIGN | 3, 4, 5 | Meets the General Education Creative Arts Core Curriculum requirement | 3”
  - equivalencies[AP-MUSIC-THEORY|CSCI 2911: Computer Science I AND CSCI 2916: Computer Science I Lab]:  ⟵ “MUSIC THEORY | 4, 5 | CSCI 2911: Computer Science I AND CSCI 2916: Computer Science I Lab | 4”
  - equivalencies[AP-MUSIC-THEORY|4, 5]:  ⟵ “MUSIC THEORY | COMP. SCI. PRINCIPLES | 4, 5 | CSCI 1611: Gentle Intro to Programming | 3”
  - equivalencies[AP-MUSIC-THEORY|WRI 1100: Analyzing and Writing Arguments]:  ⟵ “MUSIC THEORY | 4 | WRI 1100: Analyzing and Writing Arguments | 3”
  - equivalencies[AP-MUSIC-THEORY|WRI 1100: Analyzing and Writing Arguments AND WRI 1XXX]:  ⟵ “MUSIC THEORY | 5 | WRI 1100: Analyzing and Writing Arguments AND WRI 1XXX | 6”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “MUSIC THEORY | ENGLISH LIT & COMP. | 3 | WRI 1050: English Fundamentals | 3”
  - equivalencies[AP-MUSIC-THEORY|WRI 1150: Literature and Argument]:  ⟵ “MUSIC THEORY | 4 | WRI 1150: Literature and Argument | 3”
  - equivalencies[AP-MUSIC-THEORY|WRI 1100: Analyzing and Writing Arguments AND ENG 2000: The Art of Literature]:  ⟵ “MUSIC THEORY | 5 | WRI 1100: Analyzing and Writing Arguments AND ENG 2000: The Art of Literature | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “LANGUAGES Note: German, Italian, and Latin are not offered at HPU | CHINESE LANG & CULTURE | 3, 4, 5 | CHIN 2200: Intermediate Mandarin II | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|MATH 1150: Pre-Calculus I and II Accelerated]:  ⟵ “LANGUAGES Note: German, Italian, and Latin are not offered at HPU | 4, 5 | MATH 1150: Pre-Calculus I and II Accelerated | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “LANGUAGES Note: German, Italian, and Latin are not offered at HPU | CALCULUS AB | 3 | MATH 1150: Pre-Calculus I and II Accelerated | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|MATH 2214: Calculus I]:  ⟵ “LANGUAGES Note: German, Italian, and Latin are not offered at HPU | 4, 5 | MATH 2214: Calculus I | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4, 5]:  ⟵ “LANGUAGES Note: German, Italian, and Latin are not offered at HPU | CALCULUS BC | 4, 5 | MATH 2214: Calculus I AND MATH 2215: Calculus II | 6”
  - equivalencies[AP-PSYCHOLOGY|3, 4, 5]:  ⟵ “PSYCHOLOGY | PSYCHOLOGY | 3, 4, 5 | PSY 1000: Introduction to Psychology | 3”
  - equivalencies[AP-PSYCHOLOGY|BIOL 2050: Gen. Biology I AND BIOL 2051: Gen. Biology I Lab]:  ⟵ “PSYCHOLOGY | 4 | BIOL 2050: Gen. Biology I AND BIOL 2051: Gen. Biology I Lab | 5”
  - equivalencies[AP-PSYCHOLOGY|BIOL 2050: Gen. Biology I, BIOL 2051: Gen. Biology I Lab, BIOL 2052: Gen. Biology II, AND BIOL 2053: Gen. Biology II Lab]:  ⟵ “PSYCHOLOGY | 5 | BIOL 2050: Gen. Biology I, BIOL 2051: Gen. Biology I Lab, BIOL 2052: Gen. Biology II, AND BIOL 2053: Gen. Biology II Lab | 10”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “PSYCHOLOGY | CHEMISTRY | 3 | CHEM 1000: Introductory Chemistry | 3”
  - equivalencies[AP-PSYCHOLOGY|CHEM 2050: Gen. Chemistry I AND CHEM 2051: Gen. Chemistry I Lab]:  ⟵ “PSYCHOLOGY | 4 | CHEM 2050: Gen. Chemistry I AND CHEM 2051: Gen. Chemistry I Lab | 4”
  - equivalencies[AP-PSYCHOLOGY|CHEM 2050: Gen. Chemistry I, CHEM 2051: Gen. Chemistry I Lab, CHEM 2052: Gen. Chemistry II, AND CHEM 2053: Gen. Chemistry II Lab]:  ⟵ “PSYCHOLOGY | 5 | CHEM 2050: Gen. Chemistry I, CHEM 2051: Gen. Chemistry I Lab, CHEM 2052: Gen. Chemistry II, AND CHEM 2053: Gen. Chemistry II Lab | 8”
  - equivalencies[AP-PSYCHOLOGY|4, 5]:  ⟵ “PSYCHOLOGY | PHYSICS C: MECHANICS | 4, 5 | PHYS 2050: General Physics I AND PHYS 2051: Gen. Physics I Lab | 4”
### `6c2c6b7944436c44` Hawaii Pacific University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.hpu.edu/undergraduate-admissions/transfer/clep.html (sha256 ce8bf0f2e9ae)
- issues: score_column_not_scores, score_scale_mismatch
- checks: {"distinct_exams": 32, "equivalencies": 48, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “AMERICAN GOVERNMENT | 50 | PSCI 1400 AMERICAN POLITICS | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “WESTERN CIVILIZATION I: ANCENT NEAR EAST TO 1648 | 50 | HIST 1001 TRADITIONS & ENCOUNTERS: WORLD CULTURES TO 1500 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “WESTERN CIVILIZATION II: 1648 TO THE PRESENT | 50 | HIST 1002 GLOBAL CROSSROADS, 1500 TO THE PRESENT | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “HUMAN GROWTH & DEVELOPMENT | 50 | PSY 3400 LIFESPAN DEVELOPMENT PSYCHOLOGY | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “INTRO EDUCATIONAL PSYCHOLOGY | 50 | ED 3120 EDUCATIONAL PSYCHOLOGY FOR ELEMENTARY EDUCATION | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “INTRODUCTORY PSYCHOLOGY | 50 | PSY 1000 INTRODUCTION TO PSYCHOLOGY | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “PRINCIPLES OF MACROECONOMICS | 50 | ECON 2015 PRINCIPLES OF MACROECONOMICS | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “PRINCIPLES OF MICROECONOMICS | 50 | ECON 2010 PRINCIPLES OF MICROECONOMICS | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “SOCIAL SCIENCES & HISTORY | 50 | HIST 1001 TRADITIONS & ECOUNTERS: WORLD CULTURES TO 1500 – OR | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|PSCI 1400 AMERICAN POLITICS]:  ⟵ “SOCIAL SCIENCES & HISTORY | PSCI 1400 AMERICAN POLITICS | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “INTRODUCTORY SOCIOLOGY | 50 | SOC 1000 INTRODUCTION TO SOCIOLOGY | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “AMERICAN LITERATURE | 50 | AMST 2000 TOPICS IN AMERICAN STUDIES -OR- | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|ENG 2000 THE ART OF LITERATURE]:  ⟵ “AMERICAN LITERATURE | ENG 2000 THE ART OF LITERATURE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “ANALYZING & INTERPRETING LITERATURE | 50 | ENG 2000 THE ART OF LITERATURE | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “COLLEGE COMPOSITION | 50 | WRI 1050 INTRODUCTION TO ACADEMIC WRITING & | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|WRI 1100 WRITING & ANALYZING ARGUMENTS]:  ⟵ “COLLEGE COMPOSITION | WRI 1100 WRITING & ANALYZING ARGUMENTS | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “COLLEGE COMPOSITION MODULAR | 50 | WRI 1050 INTRODUCTION TO ACADEMIC WRITING | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “ENGLISH LITERATURE | 50 | ENG 2000 THE ART OF LITERATURE | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “HUMANITIES | 50 | HUM 1000 THE HUMAN CONDITION | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “BIOLOGY | 50 | BIOL 2050 GENERAL BIOLOGY I & | 3”
  - equivalencies[CLEP-BIOLOGY|BIOL 2052 GENERAL BIOLOGY II]:  ⟵ “BIOLOGY | BIOL 2052 GENERAL BIOLOGY II | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “COLLEGE ALGEBRA | 50 | MATH 1105 INTERMEDIATE ALGEBRA | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “PRECALCULUS | 50 | MATH 1130 PRECALCULUS I | 3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “CALCULUS | 50 | MATH 2214 CALCULUS I | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “COLLEGE MATHEMATICS | 50 | MATH 1101 FUNDAMENTALS OF COLLEGE MATH | 3”
  - … 23 more rows
### `134100af47877b21` Kapiolani Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.kapiolani.hawaii.edu/pay-for-college/financial-aid/financial-aid-sap-policy/ (sha256 49447fd64994)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appealing Financial Aid Suspension Appeal Process A student who is not meeting Satisfactory Academic Progress requirements may appeal for eligibility if extenuating circumstances prevented them from meeting the minimum standards.”
  - sentence: sap_appeal ⟵ “Students must complete and submit a Satisfactory Academic Progress Appeal Form to the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “To file an appeal, you must complete the Satisfactory Academic Progress (SAP) Appeal Form: 2026-27 Satisfactory Academic Progress (SAP) Appeal Form (Fall 2026, Spring 2027 and/or Summer 2027) Financial Aid Probation If an appeal is approved, the student is placed on Financial Aid Probation and given an academic plan that includes requirements they must meet each term.”
### `ca637a76f527a0f3` Kapiolani Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.kapiolani.hawaii.edu/wp-content/uploads/2026-2027-Cost-of-Attendance.pdf (sha256 41a8bc8f2e9f)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 1, "rows": 58}
  - column:Tuition: 3144 ⟵ “Tuition | $3,144”
  - column:Fees: 150 ⟵ “Fees | $150”
  - column:Books/Supplies: 1450 ⟵ “Books/Supplies | $1,450”
  - column:Total Direct Costs: 4744 ⟵ “Total Direct Costs | $4,744”
  - column:Transportation: 3458 ⟵ “Transportation | $3,458”
  - column:Housing & Utilities: 5625 ⟵ “Housing & Utilities | $5,625”
  - column:Food: 2323 ⟵ “Food | $2,323”
  - column:Personal/Misc: 2842 ⟵ “Personal/Misc | $2,842”
  - column:Total Indirect Costs: 14248 ⟵ “Total Indirect Costs | $14,248”
  - column:TOTAL COSTS: Resident Living with Parents/Family: 18992 ⟵ “TOTAL COSTS: Resident Living with Parents/Family | $18,992”
  - column:Tuition (2): 3144 ⟵ “Tuition | $3,144”
  - column:Fees (2): 150 ⟵ “Fees | $150”
  - column:Books/Supplies (2): 1450 ⟵ “Books/Supplies | $1,450”
  - column:Total Direct Costs (2): 4744 ⟵ “Total Direct Costs | $4,744”
  - column:Transportation (2): 3458 ⟵ “Transportation | $3,458”
  - column:Housing & Utilities (2): 17046 ⟵ “Housing & Utilities | $17,046”
  - column:Food (2): 6970 ⟵ “Food | $6,970”
  - column:Personal/Misc (2): 2842 ⟵ “Personal/Misc | $2,842”
  - column:Total Indirect Costs (2): 30316 ⟵ “Total Indirect Costs | $30,316”
  - column:TOTAL COSTS: Resident Living Off-Campus: 35060 ⟵ “TOTAL COSTS: Resident Living Off-Campus | $35,060”
  - column:Tuition (3): 8280 ⟵ “Tuition | $8,280”
  - column:Fees (3): 150 ⟵ “Fees | $150”
  - column:Books/Supplies (3): 1450 ⟵ “Books/Supplies | $1,450”
  - column:Total Direct Costs (3): 9880 ⟵ “Total Direct Costs | $9,880”
  - column:Transportation (3): 3458 ⟵ “Transportation | $3,458”
  - … 33 more rows
### `af4e355f0907eaa1` Kauai Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kauai.hawaii.edu/satisfactory-academic-progress-requirements (sha256 128699834f17)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Requirements Click for PDF version of the SAP policy For the Satisfactory Academic Progress Appeal Form visit the forms page.”
  - sentence: sap_appeal ⟵ “Student’s must complete and submit a Satisfactory Academic Progress Appeal Form to the Financial Aid Office.”
### `69f9642f6c00f56a` University of Hawaii Maui College — appeals 2021-22 [new] (labeled_in_source)
- source: https://maui.hawaii.edu/financial/sap-satisfactory-academic-progress (sha256 d39ff68a3af3)
- issues: stale_year_label:2021-22, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeal Form (Online Form) Appeals Processing The appeal form (along with all supporting documentation) must be completed before the appeal will be reviewed by the committee.”
### `4d2f8ba1850c8965` University of Hawaii at Hilo — appeals 2026-27 [new] (source_unlabeled)
- source: https://hilo.hawaii.edu/financialaid/SatisfactoryAcademicProgress.php (sha256 3cc84dc2e0b3)
- issues: semantic_review_required, conflicting_sources:https://hilo.hawaii.edu/documents/financialaid/SAPAppealForm-Revised5.2026.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Process A student who is placed on Financial Aid Suspension may appeal the denial of financial aid.”
  - sentence: sap_appeal ⟵ “The appeal must be made by submitting a completed UH Hilo SAP Appeal Form to the Financial Aid Office no later than 10 days after receipt of the notice of Financial Aid Suspension.”
### `90d5bcc6bf5d9abc` University of Hawaii at Hilo — appeals 2026-27 [new] (source_unlabeled)
- source: https://hilo.hawaii.edu/documents/financialaid/SAPAppealForm-Revised5.2026.pdf (sha256 a116b7e661cd)
- issues: semantic_review_required, conflicting_sources:https://hilo.hawaii.edu/financialaid/SatisfactoryAcademicProgress.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Print Clear Form UH Hilo Financial Aid Office Satisfactory Academic Progress (SAP) Appeal Form __________________________ UH ID Number/Username Last Name First Name M.I Phone Number (include area code) Federal regulations require students to maintain satisfactory academic progress to be eligible for financial aid.”
### `48105fb7dfaa8afd` University of Hawaii at Hilo — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://hilo.hawaii.edu/financialaid/CostofAttendance2526.php (sha256 32ba5cfb45b6)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 10}
  - column:Tuition: 41040 ⟵ “Tuition | 41,040 | 41,040 | 41,040”
  - column:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - column:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - column:Miscellaneous Expenses: 2778 ⟵ “Miscellaneous Expenses | 2,778 | 2,778 | 2,778”
  - column:Transportation: 1426 ⟵ “Transportation | 1,426 | 2,850 | 2,850”
  - column:Loan Fees: 1220 ⟵ “Loan Fees | 1,220 | 1,220 | 1,220”
  - column:Medical Insurance: 5460 ⟵ “Medical Insurance | 5,460 | 5,460 | 5,460”
  - column:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - column:Semester Total: 33471 ⟵ “Semester Total | $ 33,471 | $ 32,071 | $ 39,690”
  - column:Academic Year Total: 66942 ⟵ “Academic Year Total | $ 66,942 | $ 64,142 | $ 79,380”
  - with_parents_or_family:Tuition: 41040 ⟵ “Tuition | 41,040 | 41,040 | 41,040”
  - with_parents_or_family:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - with_parents_or_family:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - with_parents_or_family:Housing: 5394 ⟵ “Housing | 3,544 2 | 5,394 | 16,180”
  - with_parents_or_family:Food: 2224 ⟵ “Food | 8,298 3 | 2,224 | 6,676”
  - with_parents_or_family:Miscellaneous Expenses: 2778 ⟵ “Miscellaneous Expenses | 2,778 | 2,778 | 2,778”
  - with_parents_or_family:Transportation: 2850 ⟵ “Transportation | 1,426 | 2,850 | 2,850”
  - with_parents_or_family:Loan Fees: 1220 ⟵ “Loan Fees | 1,220 | 1,220 | 1,220”
  - with_parents_or_family:Medical Insurance: 5460 ⟵ “Medical Insurance | 5,460 | 5,460 | 5,460”
  - with_parents_or_family:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - with_parents_or_family:Semester Total: 32071 ⟵ “Semester Total | $ 33,471 | $ 32,071 | $ 39,690”
  - with_parents_or_family:Academic Year Total: 64142 ⟵ “Academic Year Total | $ 66,942 | $ 64,142 | $ 79,380”
  - off_campus_not_with_family:Tuition: 41040 ⟵ “Tuition | 41,040 | 41,040 | 41,040”
  - off_campus_not_with_family:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - off_campus_not_with_family:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - … 9 more rows
### `48caf049b9195fff` University of Hawaii at Hilo — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://hilo.hawaii.edu/financialaid/CostofAttendance2526.php (sha256 32ba5cfb45b6)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 10}
  - column:Tuition: 24096 ⟵ “Tuition | 24,096 | 24,096 | 24,096”
  - column:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - column:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - column:Miscellaneous Expenses: 2778 ⟵ “Miscellaneous Expenses | 2,778 | 2,778 | 2,778”
  - column:Transportation: 1426 ⟵ “Transportation | 1,426 | 2,850 | 2,850”
  - column:Loan Fees: 1220 ⟵ “Loan Fees | 1,220 | 1,220 | 1,220”
  - column:Medical Insurance: 5460 ⟵ “Medical Insurance | 5,460 | 5,460 | 5,460”
  - column:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - column:Semester Total: 24999 ⟵ “Semester Total | $ 24,999 | $ 23,599 | $ 31,218”
  - column:Academic Year Total: 49998 ⟵ “Academic Year Total | $ 49,998 | $ 47,198 | $ 62,436”
  - with_parents_or_family:Tuition: 24096 ⟵ “Tuition | 24,096 | 24,096 | 24,096”
  - with_parents_or_family:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - with_parents_or_family:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - with_parents_or_family:Housing: 5394 ⟵ “Housing | 3,544 2 | 5,394 | 16,180”
  - with_parents_or_family:Food: 2224 ⟵ “Food | 8,298 3 | 2,224 | 6,676”
  - with_parents_or_family:Miscellaneous Expenses: 2778 ⟵ “Miscellaneous Expenses | 2,778 | 2,778 | 2,778”
  - with_parents_or_family:Transportation: 2850 ⟵ “Transportation | 1,426 | 2,850 | 2,850”
  - with_parents_or_family:Loan Fees: 1220 ⟵ “Loan Fees | 1,220 | 1,220 | 1,220”
  - with_parents_or_family:Medical Insurance: 5460 ⟵ “Medical Insurance | 5,460 | 5,460 | 5,460”
  - with_parents_or_family:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - with_parents_or_family:Semester Total: 23599 ⟵ “Semester Total | $ 24,999 | $ 23,599 | $ 31,218”
  - with_parents_or_family:Academic Year Total: 47198 ⟵ “Academic Year Total | $ 49,998 | $ 47,198 | $ 62,436”
  - off_campus_not_with_family:Tuition: 24096 ⟵ “Tuition | 24,096 | 24,096 | 24,096”
  - off_campus_not_with_family:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - off_campus_not_with_family:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - … 9 more rows
### `61d519e07df2c736` University of Hawaii at Hilo — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://hilo.hawaii.edu/financialaid/CostofAttendance2627.php (sha256 72aa6af7fc46)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "rows": 10}
  - column:Tuition: 41040 ⟵ “Tuition | 41,040 | 41,040 | 41,040”
  - column:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - column:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - column:Miscellaneous Expenses: 2786 ⟵ “Miscellaneous Expenses | 2,786 | 2,786 | 2,786”
  - column:Transportation: 1490 ⟵ “Transportation | 1,490 | 2,978 | 2,978”
  - column:Loan Fees: 1386 ⟵ “Loan Fees | 1,386 | 1,386 | 1,386”
  - column:Medical Insurance: 5366 ⟵ “Medical Insurance | 5,366 | 5,366 | 5,366”
  - column:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - column:Semester Total: 33717 ⟵ “Semester Total | $ 33,717 | $ 32,290 | $ 40,152”
  - column:Academic Year Total: 67434 ⟵ “Academic Year Total | $ 67,434 | $ 64,580 | $ 80,304”
  - with_parents_or_family:Tuition: 41040 ⟵ “Tuition | 41,040 | 41,040 | 41,040”
  - with_parents_or_family:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - with_parents_or_family:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - with_parents_or_family:Housing: 5682 ⟵ “Housing | 3,908 2 | 5,682 | 17,046”
  - with_parents_or_family:Food: 2182 ⟵ “Food | 8,298 3 | 2,182 | 6,542”
  - with_parents_or_family:Miscellaneous Expenses: 2786 ⟵ “Miscellaneous Expenses | 2,786 | 2,786 | 2,786”
  - with_parents_or_family:Transportation: 2978 ⟵ “Transportation | 1,490 | 2,978 | 2,978”
  - with_parents_or_family:Loan Fees: 1386 ⟵ “Loan Fees | 1,386 | 1,386 | 1,386”
  - with_parents_or_family:Medical Insurance: 5366 ⟵ “Medical Insurance | 5,366 | 5,366 | 5,366”
  - with_parents_or_family:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - with_parents_or_family:Semester Total: 32290 ⟵ “Semester Total | $ 33,717 | $ 32,290 | $ 40,152”
  - with_parents_or_family:Academic Year Total: 64580 ⟵ “Academic Year Total | $ 67,434 | $ 64,580 | $ 80,304”
  - off_campus_not_with_family:Tuition: 41040 ⟵ “Tuition | 41,040 | 41,040 | 41,040”
  - off_campus_not_with_family:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - off_campus_not_with_family:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - … 9 more rows
### `6797ca796d1b2932` University of Hawaii at Hilo — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://hilo.hawaii.edu/financialaid/CostofAttendance2526.php (sha256 32ba5cfb45b6)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 10}
  - column:Tuition: 36144 ⟵ “Tuition | 36,144 | 36,144 | 36,144”
  - column:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - column:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - column:Miscellaneous Expenses: 2778 ⟵ “Miscellaneous Expenses | 2,778 | 2,778 | 2,778”
  - column:Transportation: 1426 ⟵ “Transportation | 1,426 | 2,850 | 2,850”
  - column:Loan Fees: 1220 ⟵ “Loan Fees | 1,220 | 1,220 | 1,220”
  - column:Medical Insurance: 5460 ⟵ “Medical Insurance | 5,460 | 5,460 | 5,460”
  - column:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - column:Semester Total: 31023 ⟵ “Semester Total | $ 31,023 | $ 29,623 | $ 37,242”
  - column:Academic Year Total: 62046 ⟵ “Academic Year Total | $ 62,046 | $ 59,246 | $ 74,484”
  - with_parents_or_family:Tuition: 36144 ⟵ “Tuition | 36,144 | 36,144 | 36,144”
  - with_parents_or_family:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - with_parents_or_family:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - with_parents_or_family:Housing: 5394 ⟵ “Housing | 3,544 2 | 5,394 | 16,180”
  - with_parents_or_family:Food: 2224 ⟵ “Food | 8,298 3 | 2,224 | 6,676”
  - with_parents_or_family:Miscellaneous Expenses: 2778 ⟵ “Miscellaneous Expenses | 2,778 | 2,778 | 2,778”
  - with_parents_or_family:Transportation: 2850 ⟵ “Transportation | 1,426 | 2,850 | 2,850”
  - with_parents_or_family:Loan Fees: 1220 ⟵ “Loan Fees | 1,220 | 1,220 | 1,220”
  - with_parents_or_family:Medical Insurance: 5460 ⟵ “Medical Insurance | 5,460 | 5,460 | 5,460”
  - with_parents_or_family:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - with_parents_or_family:Semester Total: 29623 ⟵ “Semester Total | $ 31,023 | $ 29,623 | $ 37,242”
  - with_parents_or_family:Academic Year Total: 59246 ⟵ “Academic Year Total | $ 62,046 | $ 59,246 | $ 74,484”
  - off_campus_not_with_family:Tuition: 36144 ⟵ “Tuition | 36,144 | 36,144 | 36,144”
  - off_campus_not_with_family:Fees 1: 770 ⟵ “Fees 1 | 770 | 770 | 770”
  - off_campus_not_with_family:Books & Supplies: 1406 ⟵ “Books & Supplies | 1,406 | 1,406 | 1,406”
  - … 9 more rows
### `d67f59597a6f5756` University of Hawaii at Hilo — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://hilo.hawaii.edu/financialaid/CostofAttendance2627.php (sha256 72aa6af7fc46)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "rows": 10}
  - column:Tuition: 24096 ⟵ “Tuition | 24,096 | 24,096 | 24,096”
  - column:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - column:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - column:Miscellaneous Expenses: 2786 ⟵ “Miscellaneous Expenses | 2,786 | 2,786 | 2,786”
  - column:Transportation: 1490 ⟵ “Transportation | 1,490 | 2,978 | 2,978”
  - column:Loan Fees: 1386 ⟵ “Loan Fees | 1,386 | 1,386 | 1,386”
  - column:Medical Insurance: 5366 ⟵ “Medical Insurance | 5,366 | 5,366 | 5,366”
  - column:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - column:Semester Total: 25245 ⟵ “Semester Total | $ 25,245 | $ 23,818 | $ 31,680”
  - column:Academic Year Total: 50490 ⟵ “Academic Year Total | $ 50,490 | $ 47,636 | $ 63,360”
  - with_parents_or_family:Tuition: 24096 ⟵ “Tuition | 24,096 | 24,096 | 24,096”
  - with_parents_or_family:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - with_parents_or_family:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - with_parents_or_family:Housing: 5682 ⟵ “Housing | 3,908 2 | 5,682 | 17,046”
  - with_parents_or_family:Food: 2182 ⟵ “Food | 8,298 3 | 2,182 | 6,542”
  - with_parents_or_family:Miscellaneous Expenses: 2786 ⟵ “Miscellaneous Expenses | 2,786 | 2,786 | 2,786”
  - with_parents_or_family:Transportation: 2978 ⟵ “Transportation | 1,490 | 2,978 | 2,978”
  - with_parents_or_family:Loan Fees: 1386 ⟵ “Loan Fees | 1,386 | 1,386 | 1,386”
  - with_parents_or_family:Medical Insurance: 5366 ⟵ “Medical Insurance | 5,366 | 5,366 | 5,366”
  - with_parents_or_family:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - with_parents_or_family:Semester Total: 23818 ⟵ “Semester Total | $ 25,245 | $ 23,818 | $ 31,680”
  - with_parents_or_family:Academic Year Total: 47636 ⟵ “Academic Year Total | $ 50,490 | $ 47,636 | $ 63,360”
  - off_campus_not_with_family:Tuition: 24096 ⟵ “Tuition | 24,096 | 24,096 | 24,096”
  - off_campus_not_with_family:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - off_campus_not_with_family:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - … 9 more rows
### `dfc285c508df347f` University of Hawaii at Hilo — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://hilo.hawaii.edu/financialaid/CostofAttendance2627.php (sha256 72aa6af7fc46)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "rows": 10}
  - column:Tuition: 36144 ⟵ “Tuition | 36,144 | 36,144 | 36,144”
  - column:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - column:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - column:Miscellaneous Expenses: 2786 ⟵ “Miscellaneous Expenses | 2,786 | 2,786 | 2,786”
  - column:Transportation: 1490 ⟵ “Transportation | 1,490 | 2,978 | 2,978”
  - column:Loan Fees: 1386 ⟵ “Loan Fees | 1,386 | 1,386 | 1,386”
  - column:Medical Insurance: 5366 ⟵ “Medical Insurance | 5,366 | 5,366 | 5,366”
  - column:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - column:Semester Total: 31269 ⟵ “Semester Total | $ 31,269 | $ 29,842 | $ 37,704”
  - column:Academic Year Total: 62538 ⟵ “Academic Year Total | $ 62,538 | $ 59,684 | $ 75,408”
  - with_parents_or_family:Tuition: 36144 ⟵ “Tuition | 36,144 | 36,144 | 36,144”
  - with_parents_or_family:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - with_parents_or_family:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - with_parents_or_family:Housing: 5682 ⟵ “Housing | 3,908 2 | 5,682 | 17,046”
  - with_parents_or_family:Food: 2182 ⟵ “Food | 8,298 3 | 2,182 | 6,542”
  - with_parents_or_family:Miscellaneous Expenses: 2786 ⟵ “Miscellaneous Expenses | 2,786 | 2,786 | 2,786”
  - with_parents_or_family:Transportation: 2978 ⟵ “Transportation | 1,490 | 2,978 | 2,978”
  - with_parents_or_family:Loan Fees: 1386 ⟵ “Loan Fees | 1,386 | 1,386 | 1,386”
  - with_parents_or_family:Medical Insurance: 5366 ⟵ “Medical Insurance | 5,366 | 5,366 | 5,366”
  - with_parents_or_family:Pharmacy Fee: 1000 ⟵ “Pharmacy Fee | 1,000 | 1,000 | 1,000”
  - with_parents_or_family:Semester Total: 29842 ⟵ “Semester Total | $ 31,269 | $ 29,842 | $ 37,704”
  - with_parents_or_family:Academic Year Total: 59684 ⟵ “Academic Year Total | $ 62,538 | $ 59,684 | $ 75,408”
  - off_campus_not_with_family:Tuition: 36144 ⟵ “Tuition | 36,144 | 36,144 | 36,144”
  - off_campus_not_with_family:Fees 1: 710 ⟵ “Fees 1 | 710 | 710 | 710”
  - off_campus_not_with_family:Books & Supplies: 1450 ⟵ “Books & Supplies | 1,450 | 1,450 | 1,450”
  - … 9 more rows
### `29b5a5ba0b85b4ab` University of Hawaii at Hilo — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://hilo.hawaii.edu/admissions/advanced_placement.php (sha256 6e6d7e678a2d)
- issues: credits_implausible
- checks: {"distinct_exams": 38, "equivalencies": 55, "rows_without_score": 0}
  - equivalencies[AP-SEMINAR|3-5]:  ⟵ “AP Seminar | 3-5 | LOW | 3”
  - equivalencies[AP-RESEARCH|3-5]:  ⟵ “AP Research | 3-5 | LOW | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3-5]:  ⟵ “Studio Art: FP 2D Design | 3-5 | ART LOW | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3-5]:  ⟵ “Studio Art: FP 3D Design | 3-5 | ART LOW | 3”
  - equivalencies[AP-DRAWING|3-5]:  ⟵ “Studio Art: FP Beginning Drawing | 3-5 | ART LOW | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101-101L | 4”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology | 4-5 | BIOL 171-171L BIOL 172-172L | 4 and4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 151 | 3”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 161-161L | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 161-161L andCHEM 162-162L | 44”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3-5]:  ⟵ “Computer Science A | 3-5 | CS 150 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3-5]:  ⟵ “Computer Science Principles | 3-5 | CS 100 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | ECON 100 | 3”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics | 4-5 | ECON 130 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | ECON 100 | 3”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics | 4-5 | ECON 131 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Language & Composition | 4-5 | ENG 100 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Composition | 4-5 | ENG 100 HUM LOW | 3 or 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science | 3-5 | ENSC 100 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Human Geography | 3-5 | GEOG 103 | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3-4]:  ⟵ “African American Studies | 3-4 | HIST LOW | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|5]:  ⟵ “African American Studies | 5 | HIST LOW | 6”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST LOW | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4-5]:  ⟵ “European History | 4-5 | HIST LOW | 6”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History | 3 | HIST LOW | 3”
  - … 30 more rows
### `6f6c1d6d46d325f1` University of Hawaii at Manoa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://manoa.hawaii.edu/fas/understanding-your-offer/ (sha256 e7eac9a56045)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://manoa.hawaii.edu/fas/forms/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “LEARN MORE ABOUT DISBURSEMENT & REFUNDS Special Circumstances If you or anyone in your household (spouse, parent, or both parents) has been affected financially by extenuating circumstances (loss of a job, death of a spouse/parent, divorce/legal separation, etc.), please visit the Forms page and complete the necessary Professional Judgement Appeal form.”
### `703bccf56c6fb0b6` University of Hawaii at Manoa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://manoa.hawaii.edu/fas/financial-aid-policies/satisfactory-academic-progress-sap-policy/ (sha256 e4e8a8de004e)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://manoa.hawaii.edu/fas/forms/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Submit a Satisfactory Academic Progress (SAP) Appeal Form and include the following: Extenuating circumstances, such as serious personal illness or injury, death or illness of a family member, unexpected employment or work issues or other extenuating circumstances, which prevented you from meeting UH Mānoa’s Financial Aid SAP.”
  - sentence: sap_appeal ⟵ “For students whose SAP appeal is approved, a SAP Academic Plan will be sent to you.”
### `a5f4a35c7ac1b129` University of Hawaii at Manoa — appeals 2026-27 [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/fas/forms/ (sha256 a0ebed22538f)
- issues: semantic_review_required, conflicting_sources:https://manoa.hawaii.edu/fas/understanding-your-offer/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Spring 2027 deadline: April 16, 2027. 2026-2027 Dependent Student Professional Judgement Form for a dependent student to use if you or your parents’ finances have changed significantly. 2026-2027 Independent Student Professional Judgement Form for an independent student to use if you or your family’s finances have changed significantly.”
### `af035808e5eac967` University of Hawaii at Manoa — appeals 2026-27 [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/fas/forms/ (sha256 a0ebed22538f)
- issues: semantic_review_required, conflicting_sources:https://manoa.hawaii.edu/fas/financial-aid-policies/satisfactory-academic-progress-sap-policy/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Forms 2026-2027 Satisfactory Academic Progress Appeal To be completed by students who have not met the requirements to sustain their financial aid and wish to appeal.”
### `ecf669900a686dfb` University of Hawaii at Manoa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://manoa.hawaii.edu/fas/understanding-your-offer/ (sha256 e7eac9a56045)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “You may include additional educational costs such as a computer expense, airfare, childcare or medical expenses, please reach out to finaid@hawaii.edu to request the Cost of Attendance Increase form.”
### `0eaa7048b0614c37` University of Hawaii at Manoa — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/fas/cost/2025-2026-cost-of-attendance/ (sha256 979950efa801)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition (12 credits): 11520 ⟵ “Tuition (12 credits) | $11,520 | $11,520 | $11,520”
  - with_parents_or_family:Fees: 882 ⟵ “Fees | $882 | $882 | $882”
  - with_parents_or_family:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404 | $1,404”
  - with_parents_or_family:Housing: 4520 ⟵ “Housing | $4,520 | $7,852 | $13,558”
  - with_parents_or_family:Food: 6068 ⟵ “Food | $6,068 | $7,364 | $6,676”
  - with_parents_or_family:Personal Expenses: 2778 ⟵ “Personal Expenses | $2,778 | $2,778 | $2,778”
  - with_parents_or_family:Transportation: 2556 ⟵ “Transportation | $2,556 | $1,278 | $2,556”
  - with_parents_or_family:Total: 29728 ⟵ “Total | $29,728 | $33,078 | $39,374”
  - on_campus:Tuition (12 credits): 11520 ⟵ “Tuition (12 credits) | $11,520 | $11,520 | $11,520”
  - on_campus:Fees: 882 ⟵ “Fees | $882 | $882 | $882”
  - on_campus:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404 | $1,404”
  - on_campus:Housing: 7852 ⟵ “Housing | $4,520 | $7,852 | $13,558”
  - on_campus:Food: 7364 ⟵ “Food | $6,068 | $7,364 | $6,676”
  - on_campus:Personal Expenses: 2778 ⟵ “Personal Expenses | $2,778 | $2,778 | $2,778”
  - on_campus:Transportation: 1278 ⟵ “Transportation | $2,556 | $1,278 | $2,556”
  - on_campus:Total: 33078 ⟵ “Total | $29,728 | $33,078 | $39,374”
  - off_campus_not_with_family:Tuition (12 credits): 11520 ⟵ “Tuition (12 credits) | $11,520 | $11,520 | $11,520”
  - off_campus_not_with_family:Fees: 882 ⟵ “Fees | $882 | $882 | $882”
  - off_campus_not_with_family:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404 | $1,404”
  - off_campus_not_with_family:Housing: 13558 ⟵ “Housing | $4,520 | $7,852 | $13,558”
  - off_campus_not_with_family:Food: 6676 ⟵ “Food | $6,068 | $7,364 | $6,676”
  - off_campus_not_with_family:Personal Expenses: 2778 ⟵ “Personal Expenses | $2,778 | $2,778 | $2,778”
  - off_campus_not_with_family:Transportation: 2556 ⟵ “Transportation | $2,556 | $1,278 | $2,556”
  - off_campus_not_with_family:Total: 39374 ⟵ “Total | $29,728 | $33,078 | $39,374”
### `349af12502752d7b` University of Hawaii at Manoa — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/admissions/financing/index.html (sha256 2ee10aa73f69)
- issues: residency_unknown, conflicting_sources:https://manoa.hawaii.edu/fas/cost/2026-2027-cost-of-attendance/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Total:: 39608 ⟵ “Total: | $33,728 | $39,608 | $55,760”
  - column:Tuition: 17640 ⟵ “Tuition | $11,760 | $17,640 | $33,792”
  - column:University Fee: 914 ⟵ “University Fee | $914 | $914 | $914”
  - column:Books & Supplies: 1330 ⟵ “Books & Supplies | $1,330 | $1,330 | $1,330”
  - column:Housing/Food: 15690 ⟵ “Housing/Food | $15,690 | $15,690 | $15,690”
  - column:Personal Expense: 2698 ⟵ “Personal Expense | $2,698 | $2,698 | $2,698”
  - column:Transportation: 1336 ⟵ “Transportation | $1,336 | $1,336 | $1,336”
### `3d6c49c0e3c1eb48` University of Hawaii at Manoa — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/fas/cost/2026-2027-cost-of-attendance/ (sha256 afacc285848e)
- issues: residency_unknown, conflicting_sources:https://manoa.hawaii.edu/admissions/financing/index.html
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition (12 credits): 11760 ⟵ “Tuition (12 credits) | $11,760 | $11,760 | $11,760”
  - with_parents_or_family:Fees: 914 ⟵ “Fees | $914 | $914 | $914”
  - with_parents_or_family:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - with_parents_or_family:Housing: 4600 ⟵ “Housing | $4,600 | $8,222 | $13,478”
  - with_parents_or_family:Food: 6148 ⟵ “Food | $6,148 | $7,468 | $6,762”
  - with_parents_or_family:Personal Expenses: 2698 ⟵ “Personal Expenses | $2,698 | $2,698 | $2,698”
  - with_parents_or_family:Transportation: 2670 ⟵ “Transportation | $2,670 | $1,336 | $2,670”
  - with_parents_or_family:Total: 30120 ⟵ “Total | $30,120 | $33,728 | $39,612”
  - on_campus:Tuition (12 credits): 11760 ⟵ “Tuition (12 credits) | $11,760 | $11,760 | $11,760”
  - on_campus:Fees: 914 ⟵ “Fees | $914 | $914 | $914”
  - on_campus:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - on_campus:Housing: 8222 ⟵ “Housing | $4,600 | $8,222 | $13,478”
  - on_campus:Food: 7468 ⟵ “Food | $6,148 | $7,468 | $6,762”
  - on_campus:Personal Expenses: 2698 ⟵ “Personal Expenses | $2,698 | $2,698 | $2,698”
  - on_campus:Transportation: 1336 ⟵ “Transportation | $2,670 | $1,336 | $2,670”
  - on_campus:Total: 33728 ⟵ “Total | $30,120 | $33,728 | $39,612”
  - off_campus_not_with_family:Tuition (12 credits): 11760 ⟵ “Tuition (12 credits) | $11,760 | $11,760 | $11,760”
  - off_campus_not_with_family:Fees: 914 ⟵ “Fees | $914 | $914 | $914”
  - off_campus_not_with_family:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - off_campus_not_with_family:Housing: 13478 ⟵ “Housing | $4,600 | $8,222 | $13,478”
  - off_campus_not_with_family:Food: 6762 ⟵ “Food | $6,148 | $7,468 | $6,762”
  - off_campus_not_with_family:Personal Expenses: 2698 ⟵ “Personal Expenses | $2,698 | $2,698 | $2,698”
  - off_campus_not_with_family:Transportation: 2670 ⟵ “Transportation | $2,670 | $1,336 | $2,670”
  - off_campus_not_with_family:Total: 39612 ⟵ “Total | $30,120 | $33,728 | $39,612”
### `5045196cb7bb736c` University of Hawaii-West Oahu — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://westoahu.hawaii.edu/financial-aid/applying-for-aid/ (sha256 5759f825ab6d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “If you need further assistance, please navigate to the Reviewing Your Award Offer page for instructions on how to complete this step. 4.”
### `ebada36db843a112` University of Hawaii-West Oahu — appeals 2026-27 [new] (source_unlabeled)
- source: https://westoahu.hawaii.edu/policies/satisfactory-academic-progress/ (sha256 adff4689971b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment Aid administrators are allowed to exercise professional judgment and enable a student, who otherwise is not making satisfactory academic progress, to continue to receive aid for cause, provided this is done on a case by case basis.Professional judgment should only be considered if the student should meet any of the following conditions: 1) medical illness; 2) personal injury;”
### `fdb9890be5d59680` University of Hawaii-West Oahu — appeals 2026-27 [new] (source_unlabeled)
- source: https://westoahu.hawaii.edu/policies/satisfactory-academic-progress/ (sha256 adff4689971b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “As such, the following stipulates the SAP policy and SAP appeal process.”
### `46a9fdaad1b6172d` University of Hawaii-West Oahu — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://westoahu.hawaii.edu/financial-aid/cost-of-attendance/ (sha256 48d3d2a875e8)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition: 7488 ⟵ “Tuition | $7,488 | $7,488”
  - with_parents_or_family:Student Fees: 240 ⟵ “Student Fees | $240 | $240”
  - with_parents_or_family:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404”
  - with_parents_or_family:Living Expenses (Food & Housing): 8394 ⟵ “Living Expenses (Food & Housing) | $8,394 | $19,062”
  - with_parents_or_family:Transportation: 2558 ⟵ “Transportation | $2,558 | $2,558”
  - with_parents_or_family:Personal/Misc Expense: 2778 ⟵ “Personal/Misc Expense | $2,778 | $2,778”
  - with_parents_or_family:Total: 22862 ⟵ “Total | $22,862 | $33,530”
  - off_campus_not_with_family:Tuition: 7488 ⟵ “Tuition | $7,488 | $7,488”
  - off_campus_not_with_family:Student Fees: 240 ⟵ “Student Fees | $240 | $240”
  - off_campus_not_with_family:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404”
  - off_campus_not_with_family:Living Expenses (Food & Housing): 19062 ⟵ “Living Expenses (Food & Housing) | $8,394 | $19,062”
  - off_campus_not_with_family:Transportation: 2558 ⟵ “Transportation | $2,558 | $2,558”
  - off_campus_not_with_family:Personal/Misc Expense: 2778 ⟵ “Personal/Misc Expense | $2,778 | $2,778”
  - off_campus_not_with_family:Total: 33530 ⟵ “Total | $22,862 | $33,530”
### `913eabf121d79229` University of Hawaii-West Oahu — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://westoahu.hawaii.edu/financial-aid/cost-of-attendance/ (sha256 48d3d2a875e8)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition: 7632 ⟵ “Tuition | $7,632 | $7,632”
  - with_parents_or_family:Student Fees: 240 ⟵ “Student Fees | $240 | $240”
  - with_parents_or_family:Books and Supplies: 1450 ⟵ “Books and Supplies | $1,450 | $1,450”
  - with_parents_or_family:Living Expenses (Food & Housing): 8284 ⟵ “Living Expenses (Food & Housing) | $8,284 | $18,882”
  - with_parents_or_family:Transportation: 2672 ⟵ “Transportation | $2,672 | $2,672”
  - with_parents_or_family:Personal/Misc Expense: 2784 ⟵ “Personal/Misc Expense | $2,784 | $2,784”
  - with_parents_or_family:Total: 23062 ⟵ “Total | $23,062 | $33,660”
  - off_campus_not_with_family:Tuition: 7632 ⟵ “Tuition | $7,632 | $7,632”
  - off_campus_not_with_family:Student Fees: 240 ⟵ “Student Fees | $240 | $240”
  - off_campus_not_with_family:Books and Supplies: 1450 ⟵ “Books and Supplies | $1,450 | $1,450”
  - off_campus_not_with_family:Living Expenses (Food & Housing): 18882 ⟵ “Living Expenses (Food & Housing) | $8,284 | $18,882”
  - off_campus_not_with_family:Transportation: 2672 ⟵ “Transportation | $2,672 | $2,672”
  - off_campus_not_with_family:Personal/Misc Expense: 2784 ⟵ “Personal/Misc Expense | $2,784 | $2,784”
  - off_campus_not_with_family:Total: 33660 ⟵ “Total | $23,062 | $33,660”
### `c0cd79522b7a1e20` University of Hawaii-West Oahu — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://westoahu.hawaii.edu/financial-aid/cost-of-attendance/ (sha256 48d3d2a875e8)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition: 20448 ⟵ “Tuition | $20,448 | $20,448”
  - with_parents_or_family:Student Fees: 240 ⟵ “Student Fees | $240 | $240”
  - with_parents_or_family:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404”
  - with_parents_or_family:Living Expenses (Food & Housing): 8394 ⟵ “Living Expenses (Food & Housing) | $8,394 | $19,062”
  - with_parents_or_family:Transportation: 2558 ⟵ “Transportation | $2,558 | $2,558”
  - with_parents_or_family:Personal/Misc Expense: 2778 ⟵ “Personal/Misc Expense | $2,778 | $2,778”
  - with_parents_or_family:Total: 35822 ⟵ “Total | $35,822 | $46,490”
  - off_campus_not_with_family:Tuition: 20448 ⟵ “Tuition | $20,448 | $20,448”
  - off_campus_not_with_family:Student Fees: 240 ⟵ “Student Fees | $240 | $240”
  - off_campus_not_with_family:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404”
  - off_campus_not_with_family:Living Expenses (Food & Housing): 19062 ⟵ “Living Expenses (Food & Housing) | $8,394 | $19,062”
  - off_campus_not_with_family:Transportation: 2558 ⟵ “Transportation | $2,558 | $2,558”
  - off_campus_not_with_family:Personal/Misc Expense: 2778 ⟵ “Personal/Misc Expense | $2,778 | $2,778”
  - off_campus_not_with_family:Total: 46490 ⟵ “Total | $35,822 | $46,490”
### `57acc2dc6f223318` University of Hawaii-West Oahu — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://westoahu.hawaii.edu/admissions/transfer-students/transfer-credits/ap-exam-breakdown/ (sha256 d7fbf38d7816)
- issues: conflicting_sources:https://westoahu.hawaii.edu/wp-content/uploads/docs/admissions/AP_Exam_Breakdown.pdf
- checks: {"distinct_exams": 34, "equivalencies": 48, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3-4]:  ⟵ “Art History | 3-4 | ART ELEC | 3”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “Art History | 5 | ART DA | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101 and BIOL 101L | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 171 and BIOL 171L | 4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | BIOL 171, BIOL 171L, BIOL 172 and BIOL 172L | 8”
  - equivalencies[AP-CALCULUS-AB|3-5]:  ⟵ “Calculus AB | 3-5 | MATH 241 | 4”
  - equivalencies[AP-CALCULUS-BC|3-5]:  ⟵ “Calculus BC | 3-5 | MATH 242 | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 100 and CHEM 100L | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 161 and CHEM 161L | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 161, CHEM 161L, CHEM 162, and CHEM 162L | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3-5]:  ⟵ “Chinese Language and Culture | 3-5 | CHN ELEC | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3-5]:  ⟵ “Comparative Government and Politics | 3-5 | POLS DS | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A | 4-5 | ICS 111 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3-5]:  ⟵ “Computer Science Principles | 3-5 | ICS ELEC | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | ENG ELEC | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Language and Composition | 4-5 | ENG 100 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3-5]:  ⟵ “English Literature and Composition | 3-5 | ENG 100 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science | 3-5 | ENSC DB | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST ELEC | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4-5]:  ⟵ “European History | 4-5 | HIST 231 and HIST 232 | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “French Language and Culture | 3-5 | FR ELEC | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3-5]:  ⟵ “German Language and Culture | 3-5 | GER ELEC | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Human Geography | 3-5 | GEOG FGC | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3-5]:  ⟵ “Japanese Language and Culture | 3-5 | JPNS 101 and JPNS 102 | 8”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | ECON ELEC | 3”
  - … 23 more rows
### `863ab6603b5166cd` University of Hawaii-West Oahu — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://westoahu.hawaii.edu/wp-content/uploads/docs/admissions/AP_Exam_Breakdown.pdf (sha256 213b91ec0328)
- issues: conflicting_sources:https://westoahu.hawaii.edu/admissions/transfer-students/transfer-credits/ap-exam-breakdown/
- checks: {"distinct_exams": 33, "equivalencies": 47, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3-4]:  ⟵ “Art History                         3-4           ART ELEC                              3”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “Art History                           5           ART DA                                3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                               3           BIOL 101 and BIOL 101L                4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                               4           BIOL 171 and BIOL 171L                4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology                               5           BIOL 171, BIOL 171L, BIOL             8”
  - equivalencies[AP-CALCULUS-AB|3-5]:  ⟵ “Calculus AB                         3-5           MATH 241                              4”
  - equivalencies[AP-CALCULUS-BC|3-5]:  ⟵ “Calculus BC                         3-5           MATH 242                              4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                             3           CHEM 100 and CHEM 100L                4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                             4           CHEM 161 and CHEM 161L                4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry                             5           CHEM 161, CHEM 161L,                  8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3 -5]:  ⟵ “Chinese Language and                3 -5          CHN ELEC                              3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3 -5]:  ⟵ “Comparative Government              3 -5          POLS DS                               3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A                  4-5           ICS 111                               4”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and                  3           ENG ELEC                              3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Language and         4-5     ENG 100                       3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3-5]:  ⟵ “English Literature and       3-5     ENG 100                      3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science        3-5     ENSC DB                      3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History               3     HIST ELEC                    3”
  - equivalencies[AP-EUROPEAN-HISTORY|4-5]:  ⟵ “European History             4-5     HIST 231 and HIST 232        6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “French Language and          3-5     FR ELEC                      3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3-5]:  ⟵ “German Language and          3-5     GER ELEC                     3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Human Geography              3-5     GEOG FGC                     3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3-5]:  ⟵ “Japanese Language and        3-5     JPNS 101 and JPNS 102        8”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                 3     ECON ELEC                    3”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics               4-5     ECON 131                     3”
  - … 22 more rows
### `be6576c1e2dae76a` University of Hawaii-West Oahu — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://westoahu.hawaii.edu/admissions/transfer-students/transfer-credits/ib-breakdown/ (sha256 167270a36e0b)
- issues: conflicting_sources:https://westoahu.hawaii.edu/wp-content/uploads/docs/registrar/IB-Credit-by-Exam.pdf
- checks: {"distinct_exams": 13, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5, 6, 7]:  ⟵ “Anthropology | 5, 6, 7 | ANTH 152 | 3”
  - equivalencies[IB-BIOLOGY|5, 6, 7]:  ⟵ “Biology | 5, 6, 7 | BIOL 171, 171L, 172, 172L | 8”
  - equivalencies[IB-CHEMISTRY|5, 6, 7]:  ⟵ “Chemistry | 5, 6, 7 | CHEM 161, 161L, 162, 162L | 8”
  - equivalencies[IB-COMPUTER-SCIENCE|4, 5]:  ⟵ “Computer Science | 4, 5 | Lower Division Elective | 3”
  - equivalencies[IB-COMPUTER-SCIENCE|6, 7]:  ⟵ “Computer Science | 6, 7 | ICS 111 | 3”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | 4 | ECON 130 | 3”
  - equivalencies[IB-ECONOMICS|5, 6, 7]:  ⟵ “Economics | 5, 6, 7 | ECON 130 and 131 | 6”
  - equivalencies[IB-GEOGRAPHY|5, 6, 7]:  ⟵ “Geography | 5, 6, 7 | Lower Division Elective | 6”
  - equivalencies[IB-HISTORY|5, 6, 7]:  ⟵ “History | 5, 6, 7 | Diversification Humanities (DH) | 6”
  - equivalencies[IB-MUSIC|5, 6, 7]:  ⟵ “Music | 5, 6, 7 | MUS 106 | 3”
  - equivalencies[IB-PHILOSOPHY|5, 6, 7]:  ⟵ “Philosophy | 5, 6, 7 | PHIL 100 | 3”
  - equivalencies[IB-PHYSICS|5, 6, 7]:  ⟵ “Physics | 5, 6, 7 | PHYS 151, 151L, 152, 152L | 8”
  - equivalencies[IB-PSYCHOLOGY|5, 6, 7]:  ⟵ “Psychology | 5, 6, 7 | PSY 100 | 3”
  - equivalencies[IB-THEATRE|5, 6, 7]:  ⟵ “Theatre Arts | 5, 6, 7 | Diversification Arts (DA) | 3”
  - equivalencies[IB-VISUAL-ARTS|5, 6, 7]:  ⟵ “Visual Arts | 5, 6, 7 | Diversification Arts (DA) | 3”
### `e334b31b1d243ace` University of Hawaii-West Oahu — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://westoahu.hawaii.edu/wp-content/uploads/docs/registrar/IB-Credit-by-Exam.pdf (sha256 8763aa29bd64)
- issues: conflicting_sources:https://westoahu.hawaii.edu/admissions/transfer-students/transfer-credits/ib-breakdown/
- checks: {"distinct_exams": 7, "equivalencies": 9, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|3]:  ⟵ “Anthropology                5, 6, 7   ANTH 152                                3”
  - equivalencies[IB-COMPUTER-SCIENCE|3]:  ⟵ “Computer Science            4, 5      Lower Division Elective                 3”
  - equivalencies[IB-COMPUTER-SCIENCE|3]:  ⟵ “Computer Science            6, 7      ICS 111                                 3”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics                   4         ECON 130                                3”
  - equivalencies[IB-ECONOMICS|6]:  ⟵ “Economics                   5, 6, 7   ECON 130 and 131                        6”
  - equivalencies[IB-GEOGRAPHY|6]:  ⟵ “Geography                   5, 6, 7   Lower Division Elective                 6”
  - equivalencies[IB-MUSIC|3]:  ⟵ “Music                       5, 6, 7   MUS 106                                 3”
  - equivalencies[IB-PHILOSOPHY|3]:  ⟵ “Philosophy                  5, 6, 7   PHIL 100                                3”
  - equivalencies[IB-PSYCHOLOGY|3]:  ⟵ “Psychology                  5, 6, 7   PSY 100                                 3”
### `0492683546b2cc7b` Windward Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.windward.hawaii.edu/financial-aid-satisfactory-academic-progress-policy (sha256 be1e987a5226)
- issues: semantic_review_required, conflicting_sources:https://windward.hawaii.edu/paying-for-college/financial-aid/satisfactory-academic-progress-policy/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “When it reverts to a letter grade, it will be calculated at the next financial aid evaluation period unless the student requests a review through SAP Appeal.”
  - sentence: sap_appeal ⟵ “Student’s must complete and submit a Satisfactory Academic Progress Appeal Form to the Financial Aid Office.”
### `7257c897dbc97186` Windward Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://windward.hawaii.edu/paying-for-college/financial-aid/satisfactory-academic-progress-policy/ (sha256 bad4f73e3eab)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://catalog.windward.hawaii.edu/financial-aid-satisfactory-academic-progress-policy
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Student’s must complete and submit a Satisfactory Academic Progress Appeal Form to the Financial Aid Office.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 0; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- Honolulu Community College (`ipeds-141680`)
- Leeward Community College (`ipeds-141811`)
- Brigham Young University-Hawaii (`ipeds-230047`)

## Leads: official pages found with no extracted record

- Chaminade University of Honolulu: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Hawaii Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency, degree_requirements, aid_appeals
- Hawaii Pacific University: admissions_tests, merit_scholarships, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Hawaii Tokai International College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Kapiolani Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Kauai Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Pacific Rim Christian University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- University of Hawaii Maui College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Hawaii at Hilo: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Hawaii at Manoa: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- University of Hawaii-West Oahu: admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Windward Community College: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
