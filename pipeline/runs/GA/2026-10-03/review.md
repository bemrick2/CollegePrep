# Review queue — GA (2026-27)

Pages fetched: 5298; failures: 842. Candidates: 376 (127 without issues, 249 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 9 | 24 | 42 | 1 | 9 |
| cost_of_attendance | 0 | 0 | 6 | 7 | 60 | 3 | 9 |
| admissions_tests | 0 | 0 | 3 | 0 | 68 | 5 | 9 |
| common_data_set | 0 | 0 | 3 | 0 | 11 | 62 | 9 |
| merit_scholarships | 0 | 0 | 4 | 1 | 64 | 7 | 9 |
| ap_credit | 0 | 0 | 6 | 4 | 24 | 42 | 9 |
| clep_credit | 0 | 0 | 7 | 2 | 13 | 54 | 9 |
| ib_credit | 0 | 0 | 5 | 2 | 9 | 60 | 9 |
| dual_enrollment | 0 | 0 | 40 | 2 | 24 | 10 | 9 |
| transfer_credit | 0 | 0 | 12 | 3 | 56 | 5 | 9 |
| statewide_articulation | 0 | 0 | 0 | 0 | 29 | 47 | 9 |
| residency | 0 | 0 | 0 | 0 | 49 | 27 | 9 |
| degree_requirements | 0 | 0 | 0 | 0 | 61 | 15 | 9 |
| aid_appeals | 0 | 0 | 0 | 54 | 7 | 15 | 9 |

## Ready for review (127)

### `65249684547d3252` Abraham Baldwin Agricultural College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.abac.edu/admissions/student_accounts/cost-attendance.html (sha256 53c8713fd438)
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 12136 ⟵ “Tuition | $12,136 | $12,136 | $12,136”
  - on_campus:Fees: 748 ⟵ “Fees | $ 748 | $ 748 | $ 748”
  - on_campus:Food: 4020 ⟵ “Food | $ 4,020 | $ 2,584 | $ 3,186”
  - on_campus:Housing: 7330 ⟵ “Housing | $ 7,330 | $ 3,690 | $ 7,390”
  - on_campus:Personal Expenses: 2430 ⟵ “Personal Expenses | $ 2,430 | $ 2,430 | $ 2,430”
  - on_campus:Transportation: 1380 ⟵ “Transportation | $ 1,380 | $ 1,380 | $ 1,380”
  - on_campus:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - on_campus:Books, Course Materials, Supplies & Equipment: 1330 ⟵ “Books, Course Materials, Supplies & Equipment | $ 1,330 | $ 1,330 | $ 1,330”
  - on_campus:Total: 29432 ⟵ “Total | $29,432 | $24,356 | $28,658”
  - with_parents_or_family:Tuition: 12136 ⟵ “Tuition | $12,136 | $12,136 | $12,136”
  - with_parents_or_family:Fees: 748 ⟵ “Fees | $ 748 | $ 748 | $ 748”
  - with_parents_or_family:Food: 2584 ⟵ “Food | $ 4,020 | $ 2,584 | $ 3,186”
  - with_parents_or_family:Housing: 3690 ⟵ “Housing | $ 7,330 | $ 3,690 | $ 7,390”
  - with_parents_or_family:Personal Expenses: 2430 ⟵ “Personal Expenses | $ 2,430 | $ 2,430 | $ 2,430”
  - with_parents_or_family:Transportation: 1380 ⟵ “Transportation | $ 1,380 | $ 1,380 | $ 1,380”
  - with_parents_or_family:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - with_parents_or_family:Books, Course Materials, Supplies & Equipment: 1330 ⟵ “Books, Course Materials, Supplies & Equipment | $ 1,330 | $ 1,330 | $ 1,330”
  - with_parents_or_family:Total: 24356 ⟵ “Total | $29,432 | $24,356 | $28,658”
  - off_campus_not_with_family:Tuition: 12136 ⟵ “Tuition | $12,136 | $12,136 | $12,136”
  - off_campus_not_with_family:Fees: 748 ⟵ “Fees | $ 748 | $ 748 | $ 748”
  - off_campus_not_with_family:Food: 3186 ⟵ “Food | $ 4,020 | $ 2,584 | $ 3,186”
  - off_campus_not_with_family:Housing: 7390 ⟵ “Housing | $ 7,330 | $ 3,690 | $ 7,390”
  - off_campus_not_with_family:Personal Expenses: 2430 ⟵ “Personal Expenses | $ 2,430 | $ 2,430 | $ 2,430”
  - off_campus_not_with_family:Transportation: 1380 ⟵ “Transportation | $ 1,380 | $ 1,380 | $ 1,380”
  - off_campus_not_with_family:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - … 2 more rows
### `66da7c628b242363` Abraham Baldwin Agricultural College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.abac.edu/admissions/applicants/dual-enrollment-applicants.html (sha256 63b6010f6992)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “At least 3.0 High School Grade Point Average calculated on RHSC courses completed.”
### `845ac186ec8c6d32` Agnes Scott College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.agnesscott.edu/admission/undergraduate-admission/cost-of-attendance.html (sha256 ec149c6f5791)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 53256 ⟵ “Tuition | $53,256”
  - column:Housing & Dining: 14079 ⟵ “Housing & Dining | $14,079”
  - column:Student Activity Fee: 350 ⟵ “Student Activity Fee | $350”
  - column:Orientation Fee: 250 ⟵ “Orientation Fee | $250”
  - column:TOTAL: 67935 ⟵ “TOTAL | $67,935”
### `d7c68b96e10e6c5b` Agnes Scott College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.agnesscott.edu/admission/undergraduate-admission/transfer-nontraditional-students/index.html (sha256 63745a9007e8)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transfer credit is given for grades of C- or better.”
### `m34a0d0394eaaf1f` Albany State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.asurams.edu/enrollment-management/dual-enrollment/admissions-information/checklist.php (sha256 f805b12bbb8c)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 5, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “High school academic GPA of 3.0 or higher.”
  - eligibility_tier: 3.0 ⟵ “Have at least a 3.0 High School Grade Point Average calculated on the RHSC courses”
  - eligibility_tier: 3.0 ⟵ “grade point average of 3.0 in academic subjects or a numerical average of 80.”
  - eligibility_tier: 3.0 ⟵ “grade point average of 3.0 in academic subjects or a numerical average of 80.”
  - eligibility_tier: 3.0 ⟵ “High school academic GPA of 3.0 or higher.”
### `248d7ecf962e29e7` Albany Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.albanytech.edu/admissions/dual-enrollment/coursework (sha256 7f9619b5d2a2)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 15 ⟵ “Courses may be taught face-to-face on the Albany Technical College campuses, on the high school campuses, online, hybrid, or via Tandberg distance education. Students will be allowed to take up to 15 credit hours per semester at each college they attend. Students can enroll in Albany Technical Colle”
### `ma1cb3308ee4fe2a` Athens Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://athenstech.edu/programs/high-school-programs/dual-enrollment/ (sha256 d8d61c150e55)
- checks: {"fields": [], "merged_pages": 2, "tiers": 3}
  - eligibility_tier: 2.0 ⟵ “11th and 12th grade students interested in diploma or certificate programs must submit an overall GPA of 2.0 or higher after the completion of the 10th grade or other admission test score requirements.”
  - eligibility_tier: 2.5 ⟵ “11th and 12th grade students interested in degree programs must submit an overall GPA of 2.5 or higher after the completion of the 10th grade or other admission test score requirements.”
  - eligibility_tier: 2.0 ⟵ “10th grade students interested in diploma or certificate programs must submit an overall GPA of 2.0 or higher after the completion of the 9th grade or other admission test score requirements.”
  - eligibility_tier: 2.0 ⟵ “11th and 12th grade students interested in diploma or certificate programs must submit an overall GPA of 2.0 or higher after the completion of the 10th grade or other admission test score requirements.”
  - eligibility_tier: 2.5 ⟵ “11th and 12th grade students interested in degree programs must submit an overall GPA of 2.5 or higher after the completion of the 10th grade or other admission test score requirements.”
  - eligibility_tier: 2.0 ⟵ “10th grade students interested in diploma or certificate programs must submit an overall GPA of 2.0 or higher after the completion of the 9th grade or other admission test score requirements.”
### `5592cb3365100249` Atlanta Metropolitan State College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.atlm.edu/students/clep-test-equivalents.aspx (sha256 a4da786f9a60)
- checks: {"distinct_exams": 18, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 |  | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL 2130 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL 1107K | 4”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “Freshman College Composition w/Essay | 50 | ENGL 1101 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French, Level I | 50 | FREN 1001 & FREN 1002 | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French, Level II | 59 | FREN 1001 & FREN 1002 & FREN 2001 & FREN 2002 | 12”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish I | 50 | SPAN 1001 & SPAN 1002 | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish II | 63 | SPAN 1001 & SPAN 1002 & SPAN 2002 & SPAN 2002 | 12”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PYSC 2103 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introduction to Psychology | 50 | PSYC 1101 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “U.S. History I: Early Colonization to 1877 | 50 | HIST 2111 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “U.S. History II: 1865 to the Present | 50 | HIST 2112 | 3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH 2201 | 3”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM 1211K | 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 1111 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MATH 1113 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECON 2105 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECON 2106 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BUSA 2201 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | BUSA 2205 | 3”
### `6314c64ca93da7d2` Atlanta Metropolitan State College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.atlm.edu/students/AP-scores.aspx (sha256 d865e8b68cac)
- checks: {"distinct_exams": 19, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History | 4-5 |  | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 1107K | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 1107K & BIOL 1108K | 8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 1151K | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 1211K & CHEM 1212K | 8”
  - equivalencies[AP-MACROECONOMICS|3-5]:  ⟵ “Macroeconomics | 3-5 | ECON 2105 | 3”
  - equivalencies[AP-MICROECONOMICS|3-5]:  ⟵ “Microeconomics | 3-5 | ECON 2106 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3-5]:  ⟵ “English Language and Composition | 3-5 | ENGL 1101 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Language and Composition | 5 | ENGL 1102 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | FREN 1002 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4-5]:  ⟵ “French Language and Culture | 4-5 | FREN 2001 & FREN 2002 | 6”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language and Culture | 3 | SPAN 1002 | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4-5]:  ⟵ “Spanish Language and Culture | 4-5 | SPAN 2001 & SPAN 2002 | 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Human Geography | 3-5 | GEOG 1105 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History | 3 | HIST 2111 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|4-5]:  ⟵ “United States History | 4-5 | HIST 2111 & HIST 2112 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History: Modern | 3 | HIST 1111 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4-5]:  ⟵ “World History: Modern | 4-5 | HIST 1111 & HIST 1112 | 6”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History | 3-5 | HIST 1111 | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH 1113 | 3”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MATH 1113 | 3”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 | MATH 2201 | 4”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | MATH 2201 & MATH 2202 | 8”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | MATH 1401 | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3-5]:  ⟵ “Comparative Government and Politics | 3-5 | POLS 1101 | 3”
  - … 5 more rows
### `ef7974eead405b57` Atlanta Metropolitan State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.atlm.edu/students/dualenrollment.aspx (sha256 9f88409456ec)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “3.0 GPA on Required High School Curriculum (RHSC) Courses”
### `fbfad7c04f43513a` Atlanta Metropolitan State College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.atlm.edu/students/ib-course-equivalents.aspx (sha256 1f25286e0bf6)
- checks: {"distinct_exams": 8, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[IB-FRENCH|HL4 - HL5]:  ⟵ “Language and Literature French | HL4 - HL5 | FREN 1002 | 3”
  - equivalencies[IB-FRENCH|HL6]:  ⟵ “Language and Literature French | HL6 | FREN 1002 & FREN 2001 | 6”
  - equivalencies[IB-FRENCH|HL7]:  ⟵ “Language and Literature French | HL7 | FREN 1002 & FREN 2001 & FREN 2002 | 9”
  - equivalencies[IB-FRENCH|SL5]:  ⟵ “Language and Literature French | SL5 | FREN 1002 | 3”
  - equivalencies[IB-FRENCH|SL6 - SL7]:  ⟵ “Language and Literature French | SL6 - SL7 | FREN 1002 & FREN 2001 | 6”
  - equivalencies[IB-SPANISH|HL4 - HL5]:  ⟵ “Language and Literature Spanish | HL4 - HL5 | SPAN 1002 | 3”
  - equivalencies[IB-SPANISH|HL6]:  ⟵ “Language and Literature Spanish | HL6 | SPAN 1002 & SPAN 2001 | 6”
  - equivalencies[IB-SPANISH|HL7]:  ⟵ “Language and Literature Spanish | HL7 | SPAN 1002 & SPAN 2001 | 6”
  - equivalencies[IB-SPANISH|SL5]:  ⟵ “Language and Literature Spanish | SL5 | SPAN 1002 | 3”
  - equivalencies[IB-SPANISH|SL6 - SL7]:  ⟵ “Language and Literature Spanish | SL6 - SL7 | SPAN 1002 & SPAN 2001 | 6”
  - equivalencies[IB-ECONOMICS|HL4 - HL7]:  ⟵ “Economics | HL4 - HL7 | ECON 2105 or ECON 2106 | 3”
  - equivalencies[IB-ECONOMICS|SL5 - SL7]:  ⟵ “Economics | SL5 - SL7 | ECON 2105 or ECON 2106 | 3”
  - equivalencies[IB-PSYCHOLOGY|HL4 - HL7]:  ⟵ “Psychology | HL4 - HL7 | PSYC 1101 | 3”
  - equivalencies[IB-PSYCHOLOGY|SL5 - SL7]:  ⟵ “Psychology | SL5 - SL7 | PSYC 1101 | 3”
  - equivalencies[IB-COMPUTER-SCIENCE|HL4]:  ⟵ “Computer Science | HL4 | CSCI 1301 | 3”
  - equivalencies[IB-COMPUTER-SCIENCE|HL5 - HL7]:  ⟵ “Computer Science | HL5 - HL7 | CSCI 1301 & CSCI 1302 | 6”
  - equivalencies[IB-COMPUTER-SCIENCE|SL5 - SL6]:  ⟵ “Computer Science | SL5 - SL6 | CSCI 1301 | 3”
  - equivalencies[IB-COMPUTER-SCIENCE|SL7]:  ⟵ “Computer Science | SL7 | CSCI 1301 & CSCI 1302 | 6”
  - equivalencies[IB-BIOLOGY|HL4 - HL5]:  ⟵ “Biology | HL4 - HL5 | BIOL 1101K | 4”
  - equivalencies[IB-BIOLOGY|HL6]:  ⟵ “Biology | HL6 | BIOL 1101K | 4”
  - equivalencies[IB-BIOLOGY|HL7]:  ⟵ “Biology | HL7 | BIOL 1107K & BIOL 1108K | 8”
  - equivalencies[IB-BIOLOGY|SL5 - SL7]:  ⟵ “Biology | SL5 - SL7 | 1101K | 4”
  - equivalencies[IB-CHEMISTRY|HL4 - HL5]:  ⟵ “Chemistry | HL4 - HL5 | CHEM 1151K | 4”
  - equivalencies[IB-CHEMISTRY|HL6]:  ⟵ “Chemistry | HL6 | CHEM 1211K | 4”
  - equivalencies[IB-CHEMISTRY|HL7]:  ⟵ “Chemistry | HL7 | CHEM 1211K & CHEM 1212K | 8”
  - … 5 more rows
### `44990ac1b0d90e76` Atlanta Metropolitan State College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.atlm.edu/academics/transfer-evaluation-and-credit-by-examination.aspx (sha256 2dc65288cb64)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “A grade of C or higher must have been earned in Composition courses in order to receive transfer credit for ENGL 1101 and ENGL 1102.”
### `a8a0378180cfe9bb` Augusta Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.augustatech.edu/dual-enrollment-section.cms (sha256 c1d7c2c9c1cb)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 15 ⟵ “Students are allowed to take up to 15 credit hours per semester, and courses may be taught on campus, online, or via a hybrid model. Students can enroll in Augusta Technical College courses during the Fall, Spring, or Summer semesters.”
### `3eb59f68777eccdf` Augusta University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.augusta.edu/finaid/costofattendance.php (sha256 48184067c434)
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Books, Course Materials, Supplies & Equipment: 1330.0 ⟵ “Books, Course Materials, Supplies & Equipment | $1,330.00”
  - column:Fees: 1350.0 ⟵ “Fees | $1,350.00”
  - column:Food: 4574.0 ⟵ “Food | $4,574.00”
  - column:Housing: 8564.0 ⟵ “Housing | $8,564.00”
  - column:Student Loan Fee: 96.0 ⟵ “Student Loan Fee | $96.00”
  - column:Miscellaneous: 3078.0 ⟵ “Miscellaneous | $3,078.00”
  - column:Transportation: 1828 ⟵ “Transportation | $1,828”
  - column:Tuition Only: 7134.0 ⟵ “Tuition Only | $7,134.00”
  - column:Total: 27954.0 ⟵ “Total | $27,954.00”
### `74ffbb421ae7edf1` Augusta University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.augusta.edu/finaid/costofattendance.php (sha256 48184067c434)
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Books, Course Materials, Supplies & Equipment: 1330.0 ⟵ “Books, Course Materials, Supplies & Equipment | $1,330.00”
  - column:Fees: 1350.0 ⟵ “Fees | $1,350.00”
  - column:Food: 4574.0 ⟵ “Food | $4,574.00”
  - column:Housing: 8564.0 ⟵ “Housing | $8,564.00”
  - column:Student Loan Fee: 96.0 ⟵ “Student Loan Fee | $96.00”
  - column:Miscellaneous: 3078.0 ⟵ “Miscellaneous | $3,078.00”
  - column:Transportation: 1828.0 ⟵ “Transportation | $1,828.00”
  - column:Tuition Only: 24568.0 ⟵ “Tuition Only | $24,568.00”
  - column:Total: 45388.0 ⟵ “Total | $45,388.00”
### `353f371b3e0af1c0` Augusta University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.augusta.edu/admissions/credit-by-exam.php (sha256 3817e91bd277)
- checks: {"distinct_exams": 15, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “BIOL 1107-1108 (no lab credit) | 6 | 50 | Biology”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “BUSA 4210 | 3 | 50 | Introductory Business Law”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “ECON 2106 | 3 | 50 | Principles of Microeconomics”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “ECON 2105 | 3 | 50 | Principles of Macroeconomics”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “EDUC 2102 | 3 | 50 | Human Growth and Development”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “FREN 1001-1002(2) | 6 | 50 | French Language”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “GRMN 1001-1002(2) | 6 | 50 | German Language”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “SPAN 1001-1002(2) | 6 | 50 | Spanish Language”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “FREN 1001-2002 | 12 | 59 | French Language”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “GRMN 1001-2002 | 12 | 60 | German Language”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “SPAN 1001-2002 | 12 | 63 | Spanish Language”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “MGMT 3500 | 3 | 50 | Introduction to Management”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “MKTG 3700 | 3 | 50 | Introduction to Marketing”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “MATH 1111 | 3 | 50 | College Algebra”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “Elective (Non-Core) | 3 | 50 | College Math”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|47]:  ⟵ “POLS 1101 | 3 | 47 | American Government(3)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “PSYC 1101 | 3 | 50 | Introduction to Psychology”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “PSYC 2103 | 3 | 50 | Human Growth and Development”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “SOCI 1101 | 3 | 50 | Introduction to Sociology”
### `5af5e7dbfc2f7fc6` Augusta University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.augusta.edu/admissions/credit-by-exam.php (sha256 3817e91bd277)
- checks: {"distinct_exams": 23, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3]:  ⟵ “ART 1211 | 3 | 3 | Studio Art Drawing Portfolio”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “ART 1520 | 3 | 3 | 2D Design Portfolio”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “BIOL 1102 (with lab) | 4 | 4 | Environmental Science”
  - equivalencies[AP-BIOLOGY|4 or 5]:  ⟵ “BIOL 1107-1108 (with labs) | 8 | 4 or 5 | Biology”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “INQR 1000 and ELEC AU | 3 | 3 | Seminar”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “Elective | 3 | 3 | Research”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “CHEM 1211 (with lab) | 4 | 4 | Chemistry”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “CHEM 1211-1212 (with labs) | 8 | 5 | Chemistry”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “CSCI 1301 | 4 | 3 | Computer Science A”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “ECON 2106 | 3 | 3 | Microeconomics”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “ECON 2105 | 3 | 3 | Macroeconomics”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “GEOG 1111 | 3 | 3 | Human Geography”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “HIST 1112 | 3 | 3 | World History”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “HIST 1112 | 3 | 3 | European History”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “HIST 2111 or 2112 | 3 | 4 | U.S. History (2)”
  - equivalencies[AP-UNITED-STATES-HISTORY|5]:  ⟵ “HIST 2111 and 2112 | 6 | 5 | U.S. History (2)”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “MATH 2011 | 4 | 3 | Calculus AB or BC”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “MATH 2011 and 2012 | 8 | 4 | Calculus BC”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “MATH 1401 | 3 | 3 | Elementary Statistics”
  - equivalencies[AP-MUSIC-THEORY|4, 5]:  ⟵ “MUSI 1101 | 2 | 4, 5 | Music Theory”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “MUSI 1201 | 2 | 3 | Music Theory”
  - equivalencies[AP-MUSIC-THEORY|4,5]:  ⟵ “MUSI 1211 | 2 | 4,5 | Music Theory”
  - equivalencies[AP-PHYSICS-1|4 or 5]:  ⟵ “PHYS 1111 (with lab) | 4 | 4 or 5 | Physics 1”
  - equivalencies[AP-PHYSICS-2|4 or 5]:  ⟵ “PHYS 1112 (with lab) | 4 | 4 or 5 | Physics 2”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “PHYS 1111 (with lab) | 4 | 3 | Physics C: Mechanics”
  - … 4 more rows
### `f26cc9b30cdd0656` Augusta University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.augusta.edu/admissions/credit-by-exam.php (sha256 3817e91bd277)
- checks: {"distinct_exams": 12, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4]:  ⟵ “ANTH 1101 or 2011 | 3 | 4 | Social and Cultural Anthropology”
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “BIOL 1101 & BIOL 1102 | 8 | 5-7 | IB Biology Standard Level (w. diploma)”
  - equivalencies[IB-BIOLOGY|4-5]:  ⟵ “BIOL 1101 & BIOL 1102 | 8 | 4-5 | IB Biology Higher Level”
  - equivalencies[IB-BIOLOGY|6-7]:  ⟵ “BIOL 1107 & BIOL 1108 | 8 | 6-7 | IB Biology Higher Level”
  - equivalencies[IB-CHEMISTRY-SL|5]:  ⟵ “CHEM 1151 | 4 | 5 | IB Chemistry SL (w. diploma)”
  - equivalencies[IB-CHEMISTRY-SL|6 or 7]:  ⟵ “CHEM 1211 | 4 | 6 or 7 | IB Chemistry SL (w. diploma)”
  - equivalencies[IB-CHEMISTRY-HL|5 or 6]:  ⟵ “CHEM 1211 | 4 | 5 or 6 | IB Chemistry HL”
  - equivalencies[IB-CHEMISTRY-HL|7]:  ⟵ “CHEM 1211 & CHEM 1212 | 8 | 7 | IB Chemistry HL”
  - equivalencies[IB-ECONOMICS-HL|5-6]:  ⟵ “ECON 2105 or ECON 2106 | 3 | 5-6 | HL Economics (with syllabus evaluation and approval)”
  - equivalencies[IB-ECONOMICS-HL|6-7]:  ⟵ “ECON 2015 and/or ECON 2016 | 3 | 6-7 | HL Economics (with syllabus evaluation and approval)”
  - equivalencies[IB-ECONOMICS-SL|5-7]:  ⟵ “ECON 2105 or ECON 2106 | 3 | 5-7 | SL Economics (w. diploma and syllabus evaluation and approval)”
  - equivalencies[IB-HISTORY|4]:  ⟵ “HIST 1111 or 1112 | 3 | 4 | History of the Islamic World”
  - equivalencies[IB-HISTORY|4]:  ⟵ “HIST 2111 and 2112 | 6 | 4 | History/Americas(1)”
  - equivalencies[IB-PHILOSOPHY|4]:  ⟵ “PHIL 2010 | 3 | 4 | Philosophy”
  - equivalencies[IB-PHYSICS-HL|4]:  ⟵ “PHYS 1111 | 4 | 4 | IB Physics HL”
  - equivalencies[IB-PHYSICS-HL|5-7]:  ⟵ “PHYS 1111 and 1112 | 8 | 5-7 | IB Physics HL”
  - equivalencies[IB-PHYSICS-SL|5]:  ⟵ “PHSC 1011 | 4 | 5 | IB Physics SL (w. diploma)”
  - equivalencies[IB-PHYSICS-SL|6-7]:  ⟵ “PHYS 1111 | 4 | 6-7 | IB Physics SL (w. diploma)”
  - equivalencies[IB-PSYCHOLOGY-HL|4 -7]:  ⟵ “PSYC 1101 | 3 | 4 -7 | IB Psychology HL”
  - equivalencies[IB-PSYCHOLOGY-SL|5-7]:  ⟵ “PSYC 1101 | 3 | 5-7 | IB Psychology SL (w. Diploma)”
### `m020c1ef97247770` Augusta University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.augusta.edu/admissions/dual-enrollment/index.php (sha256 c0f859d954a7)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Standardized test scores are required for students with a minimumn GPA of 3.0 but”
  - eligibility_tier: 3.0 ⟵ “Standardized test scores are required for students with a minimumn GPA of 3.0 but”
### `46b549471b9aa3a0` Berry College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.berry.edu/admission/_images/Publications/AcademicCreditBrochure.pdf (sha256 3d314459063c)
- checks: {"distinct_exams": 13, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5+]:  ⟵ “Biology                          HL       5+         BIO111                4”
  - equivalencies[IB-CHEMISTRY|4-5]:  ⟵ “Chemistry                        HL       4-5        CHM102                4”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics                        HL       5          ECO110                3”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French B                         HL       5          FRE101                4”
  - equivalencies[IB-MUSIC|5]:  ⟵ “Music                            HL       5          MUS101                3”
  - equivalencies[IB-PHYSICS|5-7]:  ⟵ “Physics                          HL       5-7        PHY111 &              8”
  - equivalencies[IB-PSYCHOLOGY|5]:  ⟵ “Psychology                       HL       5          PSY101                3”
  - equivalencies[IB-SPANISH|5]:  ⟵ “Spanish B                        HL       5          SPA101                4”
  - equivalencies[IB-THEATRE|5]:  ⟵ “Theatre Arts                     HL       5          THE201                3”
  - equivalencies[IB-VISUAL-ARTS|5]:  ⟵ “Visual Arts                      HL       5          ART999                3”
  - equivalencies[IB-HISTORY|4-5]:  ⟵ “History                       4-5    HIS 120                                          3        HIS 120 A”
  - equivalencies[IB-HISTORY|1-2]:  ⟵ “Art-History of Art        1-2    No Credit                             0     ART HST A                                  5     HIS 154 and HIS 155                              6       HIS 154 & HIS”
  - equivalencies[IB-BIOLOGY|1-2]:  ⟵ “Biology                   1-2    No Credit                             0      BIO NC1    Human Geography               4-5    Elective Credit Only                             3           ELE”
  - equivalencies[IB-CHEMISTRY|1-2]:  ⟵ “Chemistry                 1-2    No Credit                             0     CHM NC1”
  - equivalencies[IB-COMPUTER-SCIENCE|1-3]:  ⟵ “Computer Science-A        1-3    No Credit                             0     CSC ABN                                   4-5    Music elective (not theory)                      3        MUS 999 A”
  - equivalencies[IB-ECONOMICS|1-3]:  ⟵ “Economics-Micro           1-3    No Credit                             0      ECO NC1                                  3-4    3 hours of elective music credit                 3       MUS 999 B”
  - equivalencies[IB-PHYSICS|1-3]:  ⟵ “Physics 1                     1-3    No Credit                                        0        PHY NC1”
  - equivalencies[IB-FRENCH|1-3]:  ⟵ “(French, German,                                                              GER NC1    Physics C- Electricity and    1-3    No Credit                                        0        PHY NC4”
  - equivalencies[IB-SPANISH|4-5]:  ⟵ “Spanish)                                                                      SPA NC1    Magnetism                     4-5    PHY 212                                          4        PHY 212 A”
  - equivalencies[IB-LATIN|1-2]:  ⟵ “Latin                     1-2    No Credit                             0      FLA NC1”
### `a508d1bcee318f1a` Brenau University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.brenau.edu/admissions/military-veteran/ (sha256 1586c2fcb719)
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - off_campus_not_with_family:Tuition: 6000 ⟵ “Tuition | $6,000 | $6,000”
  - off_campus_not_with_family:I&I Fees: 150 ⟵ “I&I Fees | $150 | $150”
  - off_campus_not_with_family:University Service Fee: 750 ⟵ “University Service Fee | $750 | $750”
  - off_campus_not_with_family:Books & Supplies: 1320 ⟵ “Books & Supplies | $1,320 | $1,320”
  - off_campus_not_with_family:Housing: 15680 ⟵ “Housing | $15,680 | $13,430”
  - off_campus_not_with_family:Transportation & Other Fees: 2765 ⟵ “Transportation & Other Fees | $2,765 | $3,180”
  - off_campus_not_with_family:Total: 26665 ⟵ “Total | $26,665 | $25,830”
  - on_campus:Tuition: 6000 ⟵ “Tuition | $6,000 | $6,000”
  - on_campus:I&I Fees: 150 ⟵ “I&I Fees | $150 | $150”
  - on_campus:University Service Fee: 750 ⟵ “University Service Fee | $750 | $750”
  - on_campus:Comprehensive Fee (if Applicable): 1000 ⟵ “Comprehensive Fee (if Applicable) | - | $1,000”
  - on_campus:Books & Supplies: 1320 ⟵ “Books & Supplies | $1,320 | $1,320”
  - on_campus:Housing: 13430 ⟵ “Housing | $15,680 | $13,430”
  - on_campus:Transportation & Other Fees: 3180 ⟵ “Transportation & Other Fees | $2,765 | $3,180”
  - on_campus:Total: 25830 ⟵ “Total | $26,665 | $25,830”
### `06de2f5205e39fc5` Brenau University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.brenau.edu/admissions/dual-enrollment/ (sha256 4112250fa37d)
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Official high school transcript must show a minimum cumulative GPA of 3.0.”
  - max_credit_hours_per_term: 12 ⟵ “Students may enroll in up to 12 hours per semester. Dual Enrollment options are available for spring, summer and fall semesters at Brenau.”
### `2e072ea5844755a4` Central Georgia Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.centralgatech.edu/wp-content/uploads/pdfs/admissions/highschool/DE_PPT_StudentOrientation.pdf (sha256 9bb2eedc48e7)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 1}
  - per_credit_hour_charge: 107 ⟵ “standard tuition rate of $107 per credit hour.”
  - eligibility_tier: 4.0 ⟵ “one course and makes an A. He/she will have a 4.0 GPA, but a 50% pass rate (two”
### `e3673bba3c0a9aff` Central Georgia Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.centralgatech.edu/PLA/CreditByCompetencyExamTable.pdf (sha256 1896b66a12ec)
- checks: {"distinct_exams": 22, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “AP Art History                                 3     3 hours ARTS 1101                      Art Appreciation”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “AP Music Theory                                3     3 hours MUSC 1101                      Music Appreciation”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language and Composition            3     3 hours ENGL 1101                      Composition and Rhetoric”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “AP English Literature and Composition          3     3 hours ENGL 1102                      Literature and Composition”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “AP Macroeconomics                              3     3 hours ECON 2105                      Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “AP Microeconomics                              3     3 hours ECON 2106                      Microeconomics”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “AP Psychology                                  3     3 hours PSYC 1101                      Introductory Psychology”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “AP United States History                        3    3 hours HIST 2111        U.S. History I”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “AP World History                                3    3 hours HIST 1111        World History I”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “AP Spanish Language and Culture                 3    3 hours SPAN 1101”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “AP Spanish Literature and Culture               3    3 hours SPAN 1101”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “AP Biology                                      3    6 hours     AND          AND”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “AP Chemistry                                    3    6 hours     AND          AND”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “AP Physics 1: Algebra-Based                     3    4 hours     AND          AND”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “AP Physics 2: Algebra-Based                     3    4 hours     AND          AND”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “AP PreCalculus                                  3    3 hours MATH 1113        PreCalculus”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “AP Calculus AB                                 3   3 hours MATH 1131                        Calculus I”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “AP Calculus BC                                 3   3 hours             MATH 1132            Calculus II”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “AP Computer Science A                          3   4 hours             CIST 2371            Java Programming I”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “AP Computer Science Principles                 3   3 hours             CIST 1305            Program Design and Development”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “AP Statistics                                  3   3 hours             MATH 1127            Introduction to Statistics”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|50]:  ⟵ “American Government                          50       3 hours POLS 1101                       American Government”
  - equivalencies[AP-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                        50    3 hours PSYC 1101                        Introductory Psychology”
  - equivalencies[AP-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                   50    3 hours ECON 2105                        Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                   50    3 hours ECON 2106                        Microeconomics”
  - … 4 more rows
### `df0ca05b7fac50a4` Chattahoochee Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.chattahoocheetech.edu/dual-enrollment/index.html (sha256 2a823da97c75)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 15 ⟵ “their time in Dual Enrollment. Students are permitted to take up to 15 credit hours per semester. *Note: State Legislation is subject to change, which could impact dual enrollment”
### `m92d4a96cbd85941` Clayton  State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.clayton.edu/admissions/undergrad/transfer.php (sha256 df334c04e3c4)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “A minimum grade of C or better will be accepted for transfer credit (D’s are accepted in some majors and for some lower division courses, please contact the school or college that you are interested in pursuing for more information).”
  - min_grade: C ⟵ “A minimum grade of C or better will be accepted for transfer credit (D’s are accepted in some majors and for some lower division courses, please contact the school or college that you are interested in pursuing for more information).”
### `d236de510ca668fe` Coastal Pines Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.coastalpines.edu/student-handbook/transfer-credit-guidelines (sha256 17b49f5b5e7a)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “A grade of "C" or higher has been earned for each course transferred.”
### `4774be6a4611087b` College of Athens — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://collegeofathens.edu/dual-enrollment-students/ (sha256 840befd5aa83)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 295 ⟵ “The cost to attend the College of Athens is simple and very reasonably priced at $295 per credit hour as compared to similar institutions.”
### `27cfa5266af7bbbb` College of Coastal Georgia — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.ccga.edu/policies/cpl (sha256 4c088277d34e)
- checks: {"distinct_exams": 32, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT 2101 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECON 2105 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECON 2106 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | MGMT 3100 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | TELC 2000 (general elective credit) | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | ITEC 2100 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | MKTG 3100 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL 1101 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | ENGL 1101 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL 2121 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL 2130 | 3”
  - equivalencies[CLEP-HUMANITIES|Score]:  ⟵ “Humanities | Score | Equivalent Course | Credit Hours”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | TELC 1000 (general elective credit) | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1 | 50 | FREN 1001, 1002 | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, Level 2 | 59 | FREN 1001, 1002, 2001 | 9”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1 | 50 | GRMN 1001, 1002 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language, Level 2 | 60 | GRMN 1001, 1002, 2001 | 9”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1 | 50 | SPAN 1001, 1002 | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language, Level 2 | 63 | SPAN 1001, 1002, 2001 | 9”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing, Level 1 | 50 | SPAN 1001, 1002 | 6”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|65]:  ⟵ “Spanish with Writing, Level 2 | 65 | SPAN 1001, 1002, 2001, 2002 | 12”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|Score]:  ⟵ “History and Social Sciences | Score | Equivalent Course | Credit Hours”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS 1101 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 | HIST 2111 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | 50 | HIST 2112 | 3”
  - … 12 more rows
### `949f3357d6d0ba34` College of Coastal Georgia — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://catalog.ccga.edu/policies/cpl (sha256 4c088277d34e)
- checks: {"distinct_exams": 36, "equivalencies": 60, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art | Art History | 3 | ARHI 2300 | 3”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “. | Art History | 4 or 5 | ARHI 2300 & ARHI 2400 | 6”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4 or 5]:  ⟵ “. | Studio Art-2D Design | 3, 4 or 5 | ARTS 1060 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4 or 5]:  ⟵ “. | Studio Art-3D Design | 3, 4 or 5 | ARTS 1080 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “. | Studio Art - Drawing | 3 | ARTS 1050 | 3”
  - equivalencies[AP-DRAWING|4 or 5]:  ⟵ “. | Studio Art - Drawing | 4 or 5 | ARTS 1050 & 1070 | 6”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | Biology | 3 | non-STEM biology | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “. | Biology | 4 | BIOL 1107/L or non-STEM | 4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “. | Biology | 5 | BIOL 1107/L & BIOL 1108/L | 8”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “Capstone | Research | 3 | Transfer Elective Credit | 3”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “ | Seminar | 3 | Transfer Elective Credit | 3”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | Chemistry | 3 | CHEM 1100/L | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “. | Chemistry | 4 | CHEM 1211/L or CHEM 1100/L | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “. | Chemistry | 5 | CHEM 1211/L & CHEM 1212/L | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science | Computer Science A | 3 | CSCI 1301 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “. | Computer Science Principles | 3 | CSCI 1301 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “. | Both Computer Science A and Computer Science Principles | 3 | CSCI 1301 & 1302 | 6”
  - equivalencies[AP-MACROECONOMICS|3, 4, or 5]:  ⟵ “Economics | Macroeconomics | 3, 4, or 5 | ECON 2105 | 3”
  - equivalencies[AP-MICROECONOMICS|3, 4, or 5]:  ⟵ “. | Microeconomics | 3, 4, or 5 | ECON 2106 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 or 4]:  ⟵ “English | English Lit. & Comp. | 3 or 4 | ENGL 1101 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|5]:  ⟵ “. | English Lit. & Comp. | 5 | ENGL 1101 & 1102 | 6”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 or 4]:  ⟵ “. | English Lang. & Comp. | 3 or 4 | ENGL 1101 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “. | English Lang. & Comp. | 5 | ENGL 1101 & 1102 | 6”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3, 4, or 5]:  ⟵ “Environmental Science | Environmental Science | 3, 4, or 5 | ENVS 2202 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3, 4, or 5]:  ⟵ “Geography | Human Geography | 3, 4, or 5 | GEOG 1101 | 3”
  - … 35 more rows
### `abdabe633805859e` College of Coastal Georgia — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.ccga.edu/policies/graduation (sha256 167aae532cba)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “All students must complete 20 of the last 30 semester credit hours preceding graduation at the College.”
  - residency_requirement_credits: 30 ⟵ “Complete the residency requirement: Career Associate students must complete 24 credit hours at the College Associate of Science/Associate of Arts in core curriculum students must complete 20 credit hours at the College All students must complete 20 of the last 30 semester credit hours preceding graduation at the College.”
### `99e581076718effd` Columbus Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.columbustech.edu/dual-enrollment/ (sha256 f7df6c173b57)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.0 ⟵ “If a public or private high school student has a 2.00 high school GPA, no admissions testing or ACT/SAT is required to be admitted to Columbus Technical College. The 2.00 cumulative high school GPA is the qualifying test score for these students.”
  - eligibility_tier: 2.0 ⟵ “If a student is a home study student or a public/private school student who does not have a 2.00 high school GPA, they will need a qualifying score on a standardized test such as the PSAT, ACT or SAT. Students who have not yet taken one of those exams can be scheduled to come to CTC to take the Accu”
### `f08e655b19ef57b6` Covenant College — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.covenant.edu/pdf/IR/common-dataset.pdf (sha256 b325533bd9ee)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 0 ⟵ “Total first-time, first-year (degree-seeking) who applied                                                            0”
  - admits: 0 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                                                      0”
  - enrolled: 324 ⟵ “Total first-time, first-year (degree-seeking) enrolled               81         236             7                   324”
  - sat_composite_25..75: [1150, 1270, 1360] ⟵ “SAT Composite                     1150                      1270                       1360”
  - sat_math_25..75: [560, 600, 670] ⟵ “SAT Math                           560                       600                       670”
  - act_25..75: [24, 28, 30] ⟵ “ACT Composite                      24                        28                         30”
### `1e4a1f6bc6bed213` Dalton State College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.daltonstate.edu/admissions/financial-aid/cost-of-attendance/ (sha256 f18d1cc2e412)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Books, Course Materials and Supplies: 1330 ⟵ “Books, Course Materials and Supplies | $1,330”
  - column:Housing & Food: 8614 ⟵ “Housing & Food | $8,614”
  - column:Loan Fees: 61 ⟵ “Loan Fees | $61”
  - column:Miscellaneous and Personal Expenses: 2430 ⟵ “Miscellaneous and Personal Expenses | $2,430”
  - column:Estimated Tuition & Fees: 4231 ⟵ “Estimated Tuition & Fees | $4,231”
  - column:Estimated Transportation Costs: 2070 ⟵ “Estimated Transportation Costs | $2,070”
  - column:Total:: 18736 ⟵ “Total: | $18,736”
### `5f476d6a2a267067` Dalton State College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.daltonstate.edu/admissions/financial-aid/cost-of-attendance/ (sha256 f18d1cc2e412)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Books, Course Materials and Supplies: 1330 ⟵ “Books, Course Materials and Supplies | $1,330”
  - column:Housing & Food: 8614 ⟵ “Housing & Food | $8,614”
  - column:Loan Fees: 61 ⟵ “Loan Fees | $61”
  - column:Miscellaneous and Personal Expenses: 2430 ⟵ “Miscellaneous and Personal Expenses | $2,430”
  - column:Estimated Tuition & Fees: 10508 ⟵ “Estimated Tuition & Fees | $10,508”
  - column:Estimated Transportation Costs: 2070 ⟵ “Estimated Transportation Costs | $2,070”
  - column:Total:: 25013 ⟵ “Total: | $25,013”
### `03e8d1462eef5674` Dalton State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.daltonstate.edu/admissions/admission-requirements/dual-enrollment/ (sha256 e8c7e2229a01)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “All students must meet Satisfactory Academic Progress (SAP) to be eligible for Dual Enrollment. SAP will be determined upon acceptance and reviewed at the end of every term. SAP is defined as a minimum cumulative course completion rate of 67% and a minimum GPA of 2.0. Failure to meet SAP in any term”
### `meae09b456436588` Fort Valley State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.fvsu.edu/admissions/dual-enrollment (sha256 d7f3fc606916)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “To be admitted high school juniors and seniors must have a minimum 3.0 GPA based on the in-progress RHSC units.”
  - eligibility_tier: 3.0 ⟵ “To be admitted high school sophomores must have a minimum 3.0 GPA based on the in-progress RHSC units.”
  - eligibility_tier: 3.0 ⟵ “To be admitted high school juniors and seniors must have a minimum 3.0 GPA based on the in-progress RHSC units.”
  - eligibility_tier: 3.0 ⟵ “To be admitted high school sophomores must have a minimum 3.0 GPA based on the in-progress RHSC units.”
### `82bc1ed8830e995c` Georgia College & State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.gcsu.edu/financialaid/hope-zell-miller-scholarships (sha256 4808486df29b)
- checks: {"thresholds": null}
  - gpa_requirement: Hours from which you withdraw ⟵ “Hours from which you withdraw | Hours that you drop during the drop/add period”
### `b28e49188e8fae5a` Georgia College & State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.gcsu.edu/financialaid/hope-zell-miller-scholarships (sha256 4808486df29b)
- checks: {"thresholds": null}
  - gpa_requirement: Courses you repeat, no matter how many times you attempt them. ⟵ “Courses you repeat, no matter how many times you attempt them. | Grades earned through tests, examinations, and course challenges (ie. CLEP, AP Exams)”
### `e6d51b54b7a74395` Georgia College & State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.gcsu.edu/financialaid/hope-zell-miller-scholarships (sha256 4808486df29b)
- checks: {"thresholds": null}
  - gpa_requirement: Credits from internships ⟵ “Credits from internships | ”
### `4b53ee81a4cfd2b4` Georgia College & State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.gcsu.edu/admissions/dual-enrollment (sha256 cbeea272e937)
- checks: {"fields": ["alt_min_sat", "min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “CRITERIA A -  Have a minimum 580 Evidence-based Reading/Writing and 560 Math on the SAT OR 23 English & 22 Math on the ACT OR a minimum 52 CLT Verbal Reasoning + Grammar/Writing Scores and a 23 CLT Quantitative Reasoning Score, AND a High School academic GPA of 3.0 or higher (as calculated by the Of”
### `95b119938e787200` Georgia Gwinnett College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ggc.edu/admission-aid/financial-aid/student-consumer-info (sha256 27bb65020d11)
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and mandatory fees: 5394 ⟵ “Tuition and mandatory fees | $5,394 | $17,814 | $5,394 | $17,814 | $5,394 | $17,814”
  - on_campus:Housing and meals: 15810 ⟵ “Housing and meals | $15,810 | $15,810 | $10,500 | $10,500 | $15,130 | $15,130”
  - on_campus:Books, course materials, supplies and equipment: 1670 ⟵ “Books, course materials, supplies and equipment | $1,670 | $1,670 | $1,670 | $1,670 | $1,670 | $1,670”
  - on_campus:Transportation: 2880 ⟵ “Transportation | $2,880 | $2,880 | $2,880 | $2,880 | $2,880 | $2,880”
  - on_campus:Miscellaneous personal expenses: 3080 ⟵ “Miscellaneous personal expenses | $3,080 | $3,080 | $3,080 | $3,080 | $3,080 | $3,080”
  - on_campus:Total for 2026-2027 academic year: 28834 ⟵ “Total for 2026-2027 academic year | $28,834 | $41,254 | $23,524 | $35,944 | $28,154 | $40,574”
  - on_campus:Tuition and mandatory fees: 5394 ⟵ “Tuition and mandatory fees | $5,394 | $17,814 | $5,394 | $17,814 | $5,394 | $17,814”
  - on_campus:Housing and meals: 10500 ⟵ “Housing and meals | $15,810 | $15,810 | $10,500 | $10,500 | $15,130 | $15,130”
  - on_campus:Books, course materials, supplies and equipment: 1670 ⟵ “Books, course materials, supplies and equipment | $1,670 | $1,670 | $1,670 | $1,670 | $1,670 | $1,670”
  - on_campus:Transportation: 2880 ⟵ “Transportation | $2,880 | $2,880 | $2,880 | $2,880 | $2,880 | $2,880”
  - on_campus:Miscellaneous personal expenses: 3080 ⟵ “Miscellaneous personal expenses | $3,080 | $3,080 | $3,080 | $3,080 | $3,080 | $3,080”
  - on_campus:Total for 2026-2027 academic year: 23524 ⟵ “Total for 2026-2027 academic year | $28,834 | $41,254 | $23,524 | $35,944 | $28,154 | $40,574”
  - off_campus_not_with_family:Tuition and mandatory fees: 5394 ⟵ “Tuition and mandatory fees | $5,394 | $17,814 | $5,394 | $17,814 | $5,394 | $17,814”
  - off_campus_not_with_family:Housing and meals: 15130 ⟵ “Housing and meals | $15,810 | $15,810 | $10,500 | $10,500 | $15,130 | $15,130”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1670 ⟵ “Books, course materials, supplies and equipment | $1,670 | $1,670 | $1,670 | $1,670 | $1,670 | $1,670”
  - off_campus_not_with_family:Transportation: 2880 ⟵ “Transportation | $2,880 | $2,880 | $2,880 | $2,880 | $2,880 | $2,880”
  - off_campus_not_with_family:Miscellaneous personal expenses: 3080 ⟵ “Miscellaneous personal expenses | $3,080 | $3,080 | $3,080 | $3,080 | $3,080 | $3,080”
  - off_campus_not_with_family:Total for 2026-2027 academic year: 28154 ⟵ “Total for 2026-2027 academic year | $28,834 | $41,254 | $23,524 | $35,944 | $28,154 | $40,574”
### `ec9947c3e68145b6` Georgia Gwinnett College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ggc.edu/admission-aid/financial-aid/student-consumer-info (sha256 27bb65020d11)
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and mandatory fees: 17814 ⟵ “Tuition and mandatory fees | $5,394 | $17,814 | $5,394 | $17,814 | $5,394 | $17,814”
  - on_campus:Housing and meals: 15810 ⟵ “Housing and meals | $15,810 | $15,810 | $10,500 | $10,500 | $15,130 | $15,130”
  - on_campus:Books, course materials, supplies and equipment: 1670 ⟵ “Books, course materials, supplies and equipment | $1,670 | $1,670 | $1,670 | $1,670 | $1,670 | $1,670”
  - on_campus:Transportation: 2880 ⟵ “Transportation | $2,880 | $2,880 | $2,880 | $2,880 | $2,880 | $2,880”
  - on_campus:Miscellaneous personal expenses: 3080 ⟵ “Miscellaneous personal expenses | $3,080 | $3,080 | $3,080 | $3,080 | $3,080 | $3,080”
  - on_campus:Total for 2026-2027 academic year: 41254 ⟵ “Total for 2026-2027 academic year | $28,834 | $41,254 | $23,524 | $35,944 | $28,154 | $40,574”
  - on_campus:Tuition and mandatory fees: 17814 ⟵ “Tuition and mandatory fees | $5,394 | $17,814 | $5,394 | $17,814 | $5,394 | $17,814”
  - on_campus:Housing and meals: 10500 ⟵ “Housing and meals | $15,810 | $15,810 | $10,500 | $10,500 | $15,130 | $15,130”
  - on_campus:Books, course materials, supplies and equipment: 1670 ⟵ “Books, course materials, supplies and equipment | $1,670 | $1,670 | $1,670 | $1,670 | $1,670 | $1,670”
  - on_campus:Transportation: 2880 ⟵ “Transportation | $2,880 | $2,880 | $2,880 | $2,880 | $2,880 | $2,880”
  - on_campus:Miscellaneous personal expenses: 3080 ⟵ “Miscellaneous personal expenses | $3,080 | $3,080 | $3,080 | $3,080 | $3,080 | $3,080”
  - on_campus:Total for 2026-2027 academic year: 35944 ⟵ “Total for 2026-2027 academic year | $28,834 | $41,254 | $23,524 | $35,944 | $28,154 | $40,574”
  - off_campus_not_with_family:Tuition and mandatory fees: 17814 ⟵ “Tuition and mandatory fees | $5,394 | $17,814 | $5,394 | $17,814 | $5,394 | $17,814”
  - off_campus_not_with_family:Housing and meals: 15130 ⟵ “Housing and meals | $15,810 | $15,810 | $10,500 | $10,500 | $15,130 | $15,130”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1670 ⟵ “Books, course materials, supplies and equipment | $1,670 | $1,670 | $1,670 | $1,670 | $1,670 | $1,670”
  - off_campus_not_with_family:Transportation: 2880 ⟵ “Transportation | $2,880 | $2,880 | $2,880 | $2,880 | $2,880 | $2,880”
  - off_campus_not_with_family:Miscellaneous personal expenses: 3080 ⟵ “Miscellaneous personal expenses | $3,080 | $3,080 | $3,080 | $3,080 | $3,080 | $3,080”
  - off_campus_not_with_family:Total for 2026-2027 academic year: 40574 ⟵ “Total for 2026-2027 academic year | $28,834 | $41,254 | $23,524 | $35,944 | $28,154 | $40,574”
### `me10bb3db1cd4b59` Georgia Gwinnett College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ggc.edu/admission-aid/undergraduate-admission/dual-enrollment-admission (sha256 bfd223c3211d)
- checks: {"fields": [], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Meet the minimum 3.0 GPA.”
  - eligibility_tier: 2.7 ⟵ “2.7 GPA* with at least 2 RHSC English units successfully completed** or”
  - eligibility_tier: 3.0 ⟵ “Meet the minimum 3.0 GPA.”
  - eligibility_tier: 2.7 ⟵ “2.7 GPA* with at least 2 RHSC English units successfully completed** or”
### `b647b13572affff7` Georgia Highlands College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.highlands.edu/how-do-i-apply/dual-enrollment/ (sha256 168a7f72ff67)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Must have a high school GPA of 3.0 in core curriculum classes.”
### `52afc911d219cad5` Georgia Institute of Technology-Main Campus — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.gatech.edu/academics/undergraduate/credit-tests-scores/international-baccalaureate-exams/ (sha256 41ae4b3bfa0c)
- checks: {"distinct_exams": 28, "equivalencies": 28, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|4-5]:  ⟵ “Biology HL | 4-5 | BIOS 1107 and BIOS 1107L”
  - equivalencies[IB-BIOLOGY-SL|6-7]:  ⟵ “Biology SL | 6-7 | BIOS 1107 and BIOS 1107L”
  - equivalencies[IB-CHEMISTRY-HL|5-7]:  ⟵ “Chemistry HL | 5-7 | CHEM 1310”
  - equivalencies[IB-CHEMISTRY-SL|6-7]:  ⟵ “Chemistry SL | 6-7 | CHEM 1XXX (4)”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|5-7]:  ⟵ “Computer Science HL | 5-7 | CS 1301”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|6-7]:  ⟵ “Computer Science SL | 6-7 | CS 1XXX (3)”
  - equivalencies[IB-ECONOMICS-HL|5-7]:  ⟵ “Economics HL | 5-7 | ECON 2105 and ECON 2106*”
  - equivalencies[IB-ECONOMICS-SL|6-7]:  ⟵ “Economics SL | 6-7 | ECON 2100”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|5-7]:  ⟵ “English A: Language and Literature HL | 5-7 | LMC 2060”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-SL|5-7]:  ⟵ “English A: Language and Literature SL | 5-7 | LMC 2060”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|4-7]:  ⟵ “English A: Literature HL | 4-7 | ENGL 1101”
  - equivalencies[IB-ENGLISH-A-LITERATURE-SL|6-7]:  ⟵ “English A: Literature SL | 6-7 | ENGL 1101”
  - equivalencies[IB-FILM-HL|7]:  ⟵ “Film HL | 7 | LMC 3406”
  - equivalencies[IB-FILM-SL|6-7]:  ⟵ “Film SL | 6-7 | LMC 2500”
  - equivalencies[IB-FRENCH-HL|4]:  ⟵ “**Foreign Language B HL (Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, Spanish) | 4 | 1001 and 1002”
  - equivalencies[IB-FRENCH-SL|5]:  ⟵ “**Foreign Language B SL (Arabic, Chinese, French, German, Hebrew, Hindi, Japanese, Korean, Portuguese, Russian, Spanish) | 5 | 1001 and 1002”
  - equivalencies[IB-GEOGRAPHY-HL|5-7]:  ⟵ “Geography HL | 5-7 | SS 1XXX (3)”
  - equivalencies[IB-GEOGRAPHY-SL|6-7]:  ⟵ “Geography SL | 6-7 | SS 1XXX (3)”
  - equivalencies[IB-GLOBAL-POLITICS-HL|5-7]:  ⟵ “Global Politics HL | 5-7 | INTA 1050 and INTA 3101”
  - equivalencies[IB-GLOBAL-POLITICS-SL|6-7]:  ⟵ “Global Politics SL | 6-7 | INTA 1050”
  - equivalencies[IB-HISTORY-SL|6-7]:  ⟵ “History SL | 6-7 | HTS 1XXX (3)”
  - equivalencies[IB-HISTORY-HL|5-7]:  ⟵ “History of Africa and the Middle East HL | 5-7 | HTS 2XXX (3)”
  - equivalencies[IB-LATIN-HL|4-7]:  ⟵ “Latin B HL | 4-7 | LATN 2XXX (6)”
  - equivalencies[IB-PHILOSOPHY-HL|7]:  ⟵ “Philosophy HL | 7 | PHIL 2010”
  - equivalencies[IB-PHYSICS-HL|7]:  ⟵ “Physics HL | 7 | PHYS 1111K”
  - … 3 more rows
### `m2c4adb74e683393` Georgia Institute of Technology-Main Campus — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://admission.gatech.edu/dual-enrollment/distance-math (sha256 d437869a912d)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 7, "tiers": 1}
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA.”
  - per_credit_hour_charge: 353.93 ⟵ “Tuition: $353.93 per credit hour for Georgia residents.”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
### `37abf7fe08c0dfb9` Georgia Military College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.gmc.edu/dual-enrollment/ (sha256 5d15c86a062f)
- checks: {"fields": [], "tiers": 3}
  - eligibility_tier: 4.0 ⟵ “The GMC staff is most efficient and friendly every step of the way… When it comes to dual enrollment, GMC earns a 4.0 GPA.”
  - eligibility_tier: 2.0 ⟵ “Juniors or Seniors with a 2.0 or higher GPA”
  - eligibility_tier: 2.0 ⟵ “Minimum cumulative unweighted high school grade point average of 2.0 on a 4.00 scale.”
### `813a27f6bf4ec6ec` Georgia Northwestern Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.gntc.edu/dual-enrollment/ (sha256 610dd9d01ebb)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “Have a high school GPA of 2.0 documented with a high school transcript, OR have acceptable standardized test scores. Transcripts and test scores are generally provided by the high school.”
### `34f7b00ff184e043` Georgia Southern University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.georgiasouthern.edu/admissions-aid/tuition-and-scholarships/cost-of-attendance (sha256 5e6b8635b12e)
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 5670 ⟵ “Tuition | $5,670 | $21,300”
  - column:Fees: 1448 ⟵ “Fees | $1,448 | $1,448”
  - column:Living Expenses (Housing and Food): 13150 ⟵ “Living Expenses (Housing and Food) | $13,150 | $13,150”
### `78bb420bd63c4ee0` Georgia Southern University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.georgiasouthern.edu/admissions-aid/tuition-and-scholarships/cost-of-attendance (sha256 5e6b8635b12e)
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 21300 ⟵ “Tuition | $5,670 | $21,300”
  - column:Fees: 1448 ⟵ “Fees | $1,448 | $1,448”
  - column:Living Expenses (Housing and Food): 13150 ⟵ “Living Expenses (Housing and Food) | $13,150 | $13,150”
### `mc67ab027ed25f20` Georgia Southern University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.georgiasouthern.edu/admissions-aid/dual-enrollment/prospective-students (sha256 97f6777a414d)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 1}
  - state_grant_accepted: True ⟵ “Dual enrolled students must complete the GAfutures Dual Enrollment Scholarship Application each academic year to receive the Dual Enrollment Scholarship that covers tuition and non-course-related fees.”
  - eligibility_tier: 3.0 ⟵ “Have a high school academic unweighted GPA of 3.0 or higher (as calculated by the Office of Admissions).”
  - eligibility_tier: 2.0 ⟵ “A student is considered to be in Good Academic Standing if they have an institutional grade point average (GPA) of 2.0 or higher.”
### `40d7df54f58c4e63` Georgia Southern University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.georgiasouthern.edu/admissions-aid/transfer/transfer-requirements (sha256 aa27d873a5f8)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “They must earn the last 30 semester hours of work at Georgia Southern (Statesboro, Armstrong and/or Liberty campuses) unless an exception allows them to be a transient (visiting) student at another institution.”
### `050e52c67e90bdfe` Georgia Southwestern State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.gsw.edu/admissions/undergraduate/dual-enrollment/ (sha256 982a8e655c5c)
- checks: {"fields": ["min_hs_gpa"], "tiers": 3}
  - eligibility_tier: 3.0 ⟵ “Earn a minimum 3.0 GPA (academic courses only)”
  - eligibility_tier: 3.0 ⟵ “High School GPA: 3.0”
  - eligibility_tier: 3.0 ⟵ “High School GPA: 3.0”
  - eligibility_tier: 3.0 ⟵ “| GPA: 3.0 with 2 RHSC English units completed prior to enrollment.”
### `0fadba6afe7600b3` Georgia Southwestern State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.gsw.edu/registrar/advanced-credit (sha256 4ad8d3b92d53)
- checks: {"distinct_exams": 27, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL 2130 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL 2120 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL 1101 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | ENGL 2110 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language Level 1 and 2 | 50 | FREN 1002 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language Level 1 and 2 | 59 | FREN 2001, 2002 | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language Level 1 and 2 | 50 | SPAN 1002 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language Level 1 and 2 | 63 | SPAN 2001. 2002 | 6”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS 1101 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | PSYC 2103 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSYC 1101 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOCI 1101 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECON 2105 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECON 2106 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 | HIST 2111 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present | 50 | HIST 2112 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | HIST 1111 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | HIST 1112 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL 2107K | 4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH 1120 | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM 1211K, 1211L | 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 1111 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MATH 1113 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT 2101 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | CIS 1000 | 3”
  - … 4 more rows
### `3ee79ac02a79d6b6` Georgia Southwestern State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.gsw.edu/registrar/advanced-credit (sha256 4ad8d3b92d53)
- checks: {"distinct_exams": 24, "equivalencies": 28, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTC 1100 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 1103, 1103L | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 2107K | 4”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH 1113, 1120 | 7”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MATH 1113, 1120, 2221 | 11”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 1211, 1211L | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CSCI 1301 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | ENGL 1101 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | ENGL 1102 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 1112 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVS 1100 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | FREN 1001 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture | 4 | FREN 1001, 1002 | 6”
  - equivalencies[AP-DRAWING|4]:  ⟵ “ART: Drawing | 4 | ARTF 1010 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “ART: 2-D Art and Design | 4 | ARTF 1020 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | ECON 2105 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | ECON 2106 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | MUSC 1201 | 3”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | MUSC 1201, 1202 | 6”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics | 4 | PHYS 2211K | 4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|5]:  ⟵ “Physics C: Electricity and Magnetism | 5 | PHYS 2212K | 4”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus | 3 | MATH 1113 | 3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSYC 1101 | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language and Culture | 3 | SPAN 1001 | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|5]:  ⟵ “Spanish Language and Culture | 5 | SPAN 1001, 1002 | 6”
  - … 3 more rows
### `4cf8d80d561302bd` Georgia Southwestern State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.gsw.edu/registrar/advanced-credit (sha256 4ad8d3b92d53)
- checks: {"distinct_exams": 11, "equivalencies": 18, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|6]:  ⟵ “Biology (HL) | 6 | BIOL 2107K, 2108K | 8”
  - equivalencies[IB-CHEMISTRY-HL|4]:  ⟵ “Chemistry (HL) | 4 | CHEM 1020 | 3”
  - equivalencies[IB-CHEMISTRY-HL|5]:  ⟵ “Chemistry (HL) | 5 | CHEM 1211K | 4”
  - equivalencies[IB-CHEMISTRY-HL|6 or higher]:  ⟵ “Chemistry (HL) | 6 or higher | CHEM 1211K, 1212 | 8”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|5 or higher]:  ⟵ “Computer Science (HL) | 5 or higher | CSCI 1301 | 3”
  - equivalencies[IB-ECONOMICS-HL|5 or higher]:  ⟵ “Economics (HL) | 5 or higher | ECON 2105 | 3”
  - equivalencies[IB-HISTORY-HL|5 or higher]:  ⟵ “History - Europe (HL) | 5 or higher | HIST 1111 | 3”
  - equivalencies[IB-FRENCH-HL|5]:  ⟵ “Language A: Language and Literature - French (HL) | 5 | FREN 1002 | 3”
  - equivalencies[IB-FRENCH-HL|6]:  ⟵ “Language A: Language and Literature - French (HL) | 6 | FREN 1002, 2001 | 6”
  - equivalencies[IB-FRENCH-HL|7]:  ⟵ “Language A: Language and Literature - French (HL) | 7 | FREN 1002, 2001, 2002 | 9”
  - equivalencies[IB-MUSIC-HL|5 or higher]:  ⟵ “Music (HL) | 5 or higher | MUSC 1100 | 3”
  - equivalencies[IB-PSYCHOLOGY-HL|5 or higher]:  ⟵ “Psychology (HL) | 5 or higher | PSYC 1101 | 3”
  - equivalencies[IB-SPANISH-HL|5]:  ⟵ “Language A: Language and Literature - Spanish (HL) | 5 | SPAN 1002 | 3”
  - equivalencies[IB-SPANISH-HL|6]:  ⟵ “Language A: Language and Literature - Spanish (HL) | 6 | SPAN 1002, 2001 | 6”
  - equivalencies[IB-SPANISH-HL|7]:  ⟵ “Language A: Language and Literature - Spanish (HL) | 7 | SPAN 1002, 2001, 2002 | 9”
  - equivalencies[IB-THEATRE-HL|5 or higher]:  ⟵ “Theatre (HL) | 5 or higher | THEA 1100 | 3”
  - equivalencies[IB-HISTORY-HL|5 or higher]:  ⟵ “History - Americas (HL) | 5 or higher | HIST 2111 | 3”
  - equivalencies[IB-VISUAL-ARTS-HL|5 or higher]:  ⟵ “Visual Arts (HL) | 5 or higher | ARTC 1100 | 3”
### `863f0adc70ddd2ab` Gordon State College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.gordonstate.edu/academics/Exceptional%20Students/college-level-examination-program-clep/index.html (sha256 79634a0f81c2)
- checks: {"distinct_exams": 33, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 credits | ENGL 2131, 2132”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 6 credits | 2000-level elective credit”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 6 credits | ENGL 1101, 1102”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular - supplemental essay not required | 50 | 3 credits | ENGL 1101”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 6 credits | ENGL 2121, 2122”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 6 credits | HUMN 1501, 1502”
  - equivalencies[CLEP-HUMANITIES|Foreign Languages]:  ⟵ “Humanities | Foreign Languages”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50 62]:  ⟵ “French Language, Level 1 French Language, Level 2 | 50 62 | 6 credits 12 credits | FREN 1101, 1102 FREN 1101, 1102, 2001, 2002”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50 63]:  ⟵ “German Language, Level 1 German Language, Level 2 | 50 63 | 6 credits 12 credits | 1000 level elective credit 2000 level elective credit”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50 66]:  ⟵ “Spanish Language, Level 1 Spanish Language, Level 2 | 50 66 | 6 credits 12 credits | SPAN 1101, 1102 SPAN 1101, 1102, 2001, 2002”
  - equivalencies[CLEP-SPANISH-LANGUAGE|History and Social Sciences]:  ⟵ “Spanish Language, Level 1 Spanish Language, Level 2 | History and Social Sciences”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 credits | POLS 1101”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | 3 credits | PSYC 2103”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | 3 credits | 2000-level elective in social science”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 credits | ECON 2105”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 credits | ECON 2106”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 credits | PSYC 1101”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 credits | SOCI 1101”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | 3 credits | 2000-level elective in social sciences”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “US History I: Early Colonization to 1877 | 50 | 3 credits | HIST 2111”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “US History II: 1865 to the Present | 50 | 3 credits | HIST 2112”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | 3 credits | HIST 1121”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | 3 credits | HIST 1122”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|Science and Mathematics]:  ⟵ “Western Civilization II: 1648 to the Present | Science and Mathematics”
  - equivalencies[CLEP-BIOLOGY|50 55]:  ⟵ “Biology | 50 55 | 4 credits 6 credits | BIOL 1107 BIOL 1107 and 2 credits 2000-level elective in science”
  - … 12 more rows
### `a6c197912b1555fc` Gordon State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.gordonstate.edu/admissions/types-of-students/de-to-fr/index.html (sha256 209ef6f5e679)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “Applicants may be awarded a regular admission with a current high school transcript IF the students has a 2.0 GPA in the RHSC and less than 5 deficiencies.”
### `11fdde3c8c004617` Gordon State College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.gordonstate.edu/admissions/types-of-students/transfer/index.html (sha256 b84edb4103c7)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 42 ⟵ “Transfer Credit Equivalencies No more than 42 semester hours of combined transfer credit from all sources will be accepted towards an associate degree.”
### `bbd35954b7ad10d8` Gupton Jones College of Funeral Service — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://gupton-jones.edu/admissions/advanced-placement/ (sha256 38859b681c96)
- checks: {"distinct_exams": 8, "equivalencies": 8, "rows_without_score": 0}
  - equivalencies[AP-PRECALCULUS|3+]:  ⟵ “Precalculus | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-CALCULUS-AB|3+]:  ⟵ “Calculus AB | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-CALCULUS-BC|3+]:  ⟵ “Calculus BC | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-STATISTICS|3+]:  ⟵ “Statistics | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language & Composition | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-RESEARCH|3+]:  ⟵ “Research | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-SEMINAR|3+]:  ⟵ “Seminar | 3+ | ENG 100 – English Grammar and Composition | 4”
### `aa4e39ad2a0b9565` Gwinnett Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://gwinnetttech.edu/admissions-financial-aid/assessment-center/clep-exam/ (sha256 331bd5da7435)
- checks: {"distinct_exams": 20, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 4 | ACCT 1100”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law, Intro to | 50 | 3 | MKTG 1130”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of | 50 | 3 | MGMT 1100”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | 50 | 3 | MKTG 1100”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 | ENGL 2130”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 | ENGL 1101”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 3 | ENGL 1101”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 | ENGL 1102”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | POLS 1101”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | 3 | PSYC 2103”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | HUMN 1101”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles of | 50 | 3 | ECON 2105”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles of | 50 | 3 | ECON 2106”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | 50 | 3 | PSYC 1101”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | 50 | 3 | SOCI 1101”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 4 | BIOL 1111 & Lab”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 4 | MATH 1131”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 4 | CHEM 1211 & Lab”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | MATH 1111”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 3 | MATH 1113”
### `m3ff5b67faffdb8f` Gwinnett Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://gwinnetttech.edu/wp-content/uploads/2026/06/5839_DualEnrollmentChecklist_June23_2026.pdf (sha256 116813540541)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 2.6 ⟵ “Degree programs: 2.6 cumulative GPA”
  - eligibility_tier: 2.6 ⟵ “Degree programs: 2.6 cumulative GPA”
  - max_credit_hours_per_term: 15 ⟵ “Dual Enrollment funding is available for up to 15 credits a semester, not to exceed 30 credits in total. Speak with your high school counselor for advisement.”
### `d41404c2c73bb2c0` Helms College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.helms.edu/admissions-aid/tuition-aid/ (sha256 3e48334b9b39)
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 14317 ⟵ “Tuition | $14,317”
  - column:Books & Supplies: 986 ⟵ “Books & Supplies | $986”
  - column:Uniforms: 60 ⟵ “Uniforms | $60”
  - column:Student Kit: 60 ⟵ “Student Kit | $60”
  - column:Credentialing Exam: 280 ⟵ “Credentialing Exam | $280”
  - column:Drug Screen: 50 ⟵ “Drug Screen | $50”
  - column:Background Check: 50 ⟵ “Background Check | $50”
  - column:Immunizations: 120 ⟵ “Immunizations | $120”
  - column:Total Cost: 15923 ⟵ “Total Cost | $15,923”
### `53af591f2347d2c7` Kennesaw State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.kennesaw.edu/admissions/undergraduate/admission-requirements/transfer.php (sha256 8926310947c3)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transferable Credit 30 semester or 50 quarter hours of transferable credit. *Note: Transfer applicants are encouraged to have completed ENGL 1101 and MATH 1101 courses equivalent to Core IMPACTS with grades of "C" or better.”
### `ad7016b42e8c409e` LaGrange College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.lagrange.edu/ADMISSIONS/UNDERGRADUATE/transfer-students.html (sha256 3792e2bf24d9)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C ⟵ “PLEASE NOTE: You must have a grade of “C” or better in each course considered for transfer credit.”
  - max_transfer_credits: 60 ⟵ “Up to 60 semester hours may be transferred from an accredited two-year college.”
### `ba294598cdcdbefe` Life University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.life.edu/admissions/cost-of-attendance/ (sha256 d66bec6d83ea)
- checks: {"columns": 1, "rows": 3}
  - column:Quarterly Student Fees*: 497 ⟵ “Quarterly Student Fees* | $497”
  - column:Tuition Per Standard Program Length***: 55800 ⟵ “Tuition Per Standard Program Length*** | $55,800”
  - column:Average Cost of Attendance per Academic year: 28401 ⟵ “Average Cost of Attendance per Academic year | $28,401”
### `9365bab6eb4a5e38` Luther Rice College & Seminary — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.lutherrice.edu/content/userfiles/files/CLEP%20Transfer%20of%20Credit%20Matrix(1).pdf (sha256 e4cb275b79a5)
- checks: {"distinct_exams": 21, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature       50                       3 hours                 EN 2101”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and             50                       3 hours                 EN 2104 or EN 2105”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition       50                       6 hours                 EN 1101, EN 1102”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition       50                       3 hours                 EN 1101”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature        50                       3 hours                 EN 2105”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                50                       3 hours                 Open Elective”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government       50                       3 hours                 PS 1101”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and          50                       3 hours                 PY 1702”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology    50                       3 hours                 Open Elective”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and       50                       3 hours                 Open Elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I    50                       3 hours                 HI 1101”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II   50                       3 hours                 HI 1102”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                        50                            3 hours                        SC 1501”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                       50                            3 hours                        MA 1600”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                      50                            3 hours                        SC 1501”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                50                            3 hours                        MA 1600”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics            50                            3 hours                        MA 1600”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences               50                            3 hours                        SC 1501”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                    50                            3 hours                        MA 1600”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting           50                            3 hours                        Open Elective”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems            50                            3 hours                        Open Elective”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing        50                            3 hours                        Open Elective”
### `de947fb21f6a9f88` Luther Rice College & Seminary — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.lutherrice.edu/degree-programs/dual_enrollment (sha256 64f3ca92d76c)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 250 ⟵ “In-State and Out-of-State DE tuition is $750.00 per course ($250/credit hr). Books will be covered in-state but are not covered out-of-state.”
  - per_credit_hour_charge: 250 ⟵ “However, Out-of-State students do not qualify for Georgia state DE funding. Instead, you will pay Luther Rice's listed price of $750.00 per course ($250/credit hr). Books will be covered in-state but are not covered out-of-state.”
### `m15963b3eacc65ff` Middle Georgia State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mga.edu/academics/docs/transfer-agreements/Articulation_Agreement_AAS_Computer_Info_Systems_BSIT_CGTC.pdf (sha256 999c3ebcd6ba)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 12}
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGA for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 8.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGSC for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGSC College for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGSC for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
  - residency_requirement_credits: 30 ⟵ “Any stude nt ad mitted to MG SC for the f inal year mu st be in res idence for two semesters and mu st complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to Middle Georgia State College for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGSC for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGSC for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGA for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper-division work in the major. 7.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGA for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 27 hours of upper level course work in the major. 9.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGA for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 8.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGA for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 8.”
### `3d30ec2679ab21e6` Morehouse College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://morehouse.edu/hubfs/DIRE/Transfer%20Admission.pdf (sha256 de5f01af1e86)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C ⟵ “Course credit from another institution of higher education is transferable if: (1) the prior college/university is accredited, (2) a grade of C or better is earned in the course, and (3) the course is evaluated as comparable to a class already offered at Morehouse College D9.”
  - max_transfer_credits: 60 ⟵ “A maximum of 60 credit hours (or the equivalent) is transferable to Morehouse.”
### `b75dfbbb7674f2ed` Oconee Fall Line Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://oftc.edu/admissions/dual-enrollment-high-school-students/ (sha256 d835f71ed4b1)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.6 ⟵ “| High school GPA 2.6 or higher”
  - eligibility_tier: 2.6 ⟵ “High school GPA 2.6 or higher”
  - eligibility_tier: 2.6 ⟵ “| High school GPA 2.6 or higher”
  - eligibility_tier: 2.6 ⟵ “High school GPA 2.6 or higher”
### `5ac5fe2e61ac32ba` Ogeechee Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ogeecheetech.edu/admissions/high-school-students (sha256 fc42244c5fda)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 15 ⟵ “Dual Enrollment students can enroll in up to 15 credit hours per semester. Earn college credit and save money on future college costs!*”
### `6feb39f3c6f9e31b` Oglethorpe University — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://oglethorpe.edu/wp-content/uploads/2026/04/Common-Data-Set-2025-2026.pdf (sha256 77e2777ca6bd)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 2736 ⟵ “Total first-time, first-year (degree-seeking) who applied          2090         413            37           196    2736”
  - admits: 2457 ⟵ “Total first-time, first-year (degree-seeking) who were admitted    1913         365            33           146    2457”
  - enrolled: 395 ⟵ “Total first-time, first-year (degree-seeking) enrolled              333         53              2            7      395”
  - sat_composite_25..75: [1120, 1210, 1280] ⟵ “SAT Composite                     1120                      1210                       1280”
  - sat_math_25..75: [520, 580, 640] ⟵ “SAT Math                           520                       580                       640”
  - act_25..75: [24, 25, 27] ⟵ “ACT Composite                      24                        25                         27”
### `8b9c7b3e2d189ef6` Oglethorpe University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://oglethorpe.edu/admission/apply/transfer/ (sha256 07d2f982acee)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 32 ⟵ “A minimum of 32 semester hours must be completed in residence at Oglethorpe including at least half of the semester hours required for the student’s chosen major to earn an Oglethorpe degree.”
  - residency_requirement_credits: 32 ⟵ “A minimum of 32 semester hours must be completed in residence at Oglethorpe including at least half of the semester hours required for the student’s chosen major to earn an Oglethorpe degree.”
### `c18c71ca617b8a14` Piedmont University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.piedmont.edu/admissions-aid/apply/dual-enrollment-students/ (sha256 ffd8c44cc615)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a 3.0 or higher grade point average (GPA) in their high school coursework.”
### `80eb01e1eb280ea8` Point University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://point.edu/admissions/dual-enrollment/ (sha256 feddb4de8d4c)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 1}
  - state_grant_accepted: True ⟵ “Even better, students who participate in the Dual Credit Enrollment program may be eligible for a Dual Enrollment Scholarship after graduating from high school if they are admitted to a Point University residential undergraduate program — helping make the transition from high school to college even ”
  - per_credit_hour_charge: 250 ⟵ “Point offers dual-credit enrollment courses on our main campus in West Point, at our off-site locations (Peachtree City and Savannah), online, and at select partnering high schools in Georgia. These courses are available at a discounted rate of $250 per credit hour. For more information, please cont”
  - eligibility_tier: 3.0 ⟵ “High school GPA of 3.0 minimum.”
### `e186f66c3f4470ae` Savannah State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://savannahstate.edu/undergraduate/dualenrollment/ (sha256 f514d824a6b9)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “All interested 10th, 11th, and 12th grade high school scholars must meet the 3.0 GPA requirement in all core academic courses and eligibility requirements to receive state funding.”
### `c7c7fa5453f694dd` Savannah Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.savannahtech.edu/admissions/dual-enrollment-students/ (sha256 26b01feba3e1)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.6 ⟵ “Degree/diploma level programs require a 2.6 GPA and TCC level programs require a 2.0 GPA.  Please have your high school email us your official transcript to [email protected]”
  - eligibility_tier: 4.0 ⟵ “As a dual enrollment student from Long County High School, Rhett Dozier earned an Associate of Science degree in Information Technology from Savannah Technical College with a 4.0 GPA.”
### `c15a90cc26ab690b` Shorter University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.shorter.edu/admissions/dualenrollment.php (sha256 c4512eed1bc0)
- checks: {"fields": ["alt_min_act", "max_credit_hours_per_term", "min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Dual Enrollment students are recommended to have at least a 3.00 GPA with a 21 ACT”
  - max_credit_hours_per_term: 15 ⟵ “The cost for coursework up to 15 credit hours per semester or 30 credit hours maximum”
### `87d384e93cdc0223` South Georgia State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.sgsc.edu/admissions/dual-enrollment (sha256 519c2ba3c3f7)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Minimum high school GPA of 3.0 or higher, as calculated based on Required High School Curriculum courses”
  - eligibility_tier: 3.0 ⟵ “Minimum high school GPA of 3.0 or higher, as calculated based on Required High School Curriculum (RHSC) courses.”
### `c4df278465b051d2` Southern Crescent Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.sctech.edu/admissions/dual-enrollment/ (sha256 6d80cd385ee7)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.0 ⟵ “Have a High School GPA of 2.0 or higher”
  - eligibility_tier: 2.0 ⟵ “High School GPA 2.0 or higher”
  - eligibility_tier: 2.0 ⟵ “High School GPA 2.0 or higher”
### `ad72e20d68b67c4e` Southern Regional Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: http://southernregional.edu/dual-enrollment-entrance-exam-and-scores (sha256 581118e312dd)
- checks: {"fields": [], "tiers": 2}
  - eligibility_tier: 2.6 ⟵ “HOPE GPA: 2.6 or higher (after 10th grade completion)”
  - eligibility_tier: 2.0 ⟵ “HOPE GPA: 2.0 or higher (after 10th grade completion)”
### `20749b1745716bd3` Spelman College — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.spelman.edu/_1_Docs-and-Files/about/institutional-research/common-data-set/cds_2025-2026_spelman_college_1.26.2026.pdf (sha256 fb4c14161f5c)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 11533 ⟵ “Total first-time, first-year (degree-seeking) who applied                                                                                     11533”
  - admits: 2743 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                                                                                2743”
  - enrolled: 648 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                          147                496            5             0          648”
  - sat_composite_25..75: [1100, 1220, 1300] ⟵ “SAT Composite                                 1100                1220               1300”
  - sat_reading_25..75: [570, 630, 670] ⟵ “SAT Evidence-Based Reading and   570                630                670”
  - sat_math_25..75: [520, 580, 630] ⟵ “SAT Math                                       520                580                630”
  - act_25..75: [22, 25, 28] ⟵ “ACT Composite                                   22                 25                 28”
### `321b6f3b5d84448a` Spelman College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.spelman.edu/academics/summer-programs/early-college-program.html (sha256 3cb57936c37b)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “ECP is an intense academic program that offers college credit courses in English and Biology for current high school juniors and seniors. A cumulative 3.0 GPA along with a minimum GPA of 3.0 in English and Science courses is required.”
### `afea627275b3109e` Spelman College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.spelman.edu/admissions/transfer-applicants/transfer-credit-policy.html (sha256 07e2b691a0ad)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Giving Make a Gift Alumnae Engagement Institutional Advancement Overview Advancement Leadership Spelman Forward Transfer Credit Policy Home > Admissions > Transfer Applicants > Transfer Credit Policy Transfer Credit Policy The College will award transfer credit for comparable work in which the student has earned grades of “C” or better, provided that the institution at which the credit was earned ”
### `70634214d703c788` Thomas University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.thomasu.edu/become-a-student/admission-process/on-campus/ (sha256 3876c91d7578)
- checks: {"thresholds": null}
  - award_tiers: [{'unweighted gpa': '3.9+', 'amount_text': '$7,000'}, {'unweighted gpa': '3.7 - 3.89', 'amount_text': '$5,000'}, {'unweighted gpa': '3.5 - 3.69', 'amount_text': '$3,000'}] ⟵ “Unweighted GPA | Scholarship || 3.9+ | $7,000 || 3.7 - 3.89 | $5,000 || 3.5 - 3.69 | $3,000”
  - gpa_requirement: Tiered by Unweighted GPA: 3.9+ → $7,000; 3.7 - 3.89 → $5,000; 3.5 - 3.69 → $3,000 ⟵ “Unweighted GPA | Scholarship || 3.9+ | $7,000 || 3.7 - 3.89 | $5,000 || 3.5 - 3.69 | $3,000”
### `19de73b4938717b7` Thomas University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.thomasu.edu/become-a-student/admission-process/on-campus/dual-enrollment/ (sha256 c1022ea6262c)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 2}
  - per_credit_hour_charge: 250 ⟵ “Tuition, books and certain fees are covered for Georgia residents. Non-Georgia residents are charged the rate of $250 per credit hour for tuition.”
  - eligibility_tier: 3.0 ⟵ “GPA         3.0”
  - eligibility_tier: 3.0 ⟵ “Have at least a 3.0 GPA;”
### `m917f309625155a6` University of Georgia — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.uga.edu/apply/transfer-applicants/transfer-faqs/ (sha256 5e1d3a0c2463)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - residency_requirement_credits: 60 ⟵ “As a prospective transfer student, it is important to note that to earn a UGA baccalaureate degree, at least 45 of the last 60 semester credit hours must be completed in residence at UGA.”
  - residency_requirement_credits: 60 ⟵ “As a prospective transfer student, it is important to note that to earn a UGA baccalaureate degree, at least 45 of the last 60 semester credit hours must be completed in residence at UGA.”
### `6cdb1ae57c99f164` University of North Georgia — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://ung.edu/military-college-admissions/application-process/dual-enrolled-high-school-student.php (sha256 a0c41d21bfbf)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.25 ⟵ “The student must present a cumulative grade point average (GPA) of 3.25 or higher in their Required High School Curriculum (RHSC) coursework (PDF), and the transcript must show evidence that the student is on track toward the completion of the USG RHSC requirements and high school graduation.”
### `29182a3c4e1aa69a` University of North Georgia — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://ung.edu/military-college-admissions/application-process/transfer-student.php (sha256 8c337dc61dc6)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Note that you are required to earn a grade of "C" or better in English 1101 and 1102 (or equivalents) in order for these courses to transfer.”
### `303603550f924e1e` University of West Georgia — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westga.edu/isap/waivers.php (sha256 292cd75f398e)
- checks: {"thresholds": null}
  - gpa_requirement: 3.0+ GPA ⟵ “Academic (50% waiver) | 3.0+ GPA | 3.0+ GPA”
### `9765d58d92887915` University of West Georgia — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westga.edu/isap/waivers.php (sha256 292cd75f398e)
- checks: {"thresholds": null}
  - gpa_requirement: 3.5+ GPA ⟵ “Presidential (100% waiver) | 3.5+ GPA | 3.5+ GPA”
### `c38386feea283a02` University of West Georgia — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westga.edu/isap/waivers.php (sha256 292cd75f398e)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75+ GPA ⟵ “Merit (25% waiver) | 2.75+ GPA | 2.75+ GPA”
### `c9aa9ba89a289aa5` University of West Georgia — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westga.edu/isap/waivers.php (sha256 292cd75f398e)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25+ GPA ⟵ “Scholastic (75% waiver) | 3.25+ GPA | 3.25+ GPA”
### `md605f05c932b4fe` University of West Georgia — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.westga.edu/undergraduate-admissions/go-west-early-carrolldual-enrollment.php (sha256 e29d7a357879)
- checks: {"fields": ["max_credit_hours_per_term"], "merged_pages": 2, "tiers": 0}
  - max_credit_hours_per_term: 15 ⟵ “The Georgia Student Finance Commission provides tuition and mandatory fees for dual enrollment students enrolled in up to 15 credit hours per semester in courses selected from an approved list. **Please note that dual enrollment students must maintain Satisfactory Academic Progress (SAP) to receive ”
  - max_credit_hours_per_term: 15 ⟵ “The Georgia Student Finance Commission provides tuition and mandatory fees for dual enrollment students enrolled in up to 15 credit hours per semester in courses selected from an approved list. **Please note that dual enrollment students must maintain Satisfactory Academic Progress (SAP) to receive ”
### `d50f7d363b5d3ff7` Wesleyan College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.wesleyancollege.edu/admission/undergraduate/transfer.cfm (sha256 c77135d41c1d)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “In general, transfer credits must come from an accredited institution, be from degree-level coursework, and have a grade of “C” or higher.”
### `031620173a83f368` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Rotary Club of Carrollton Scholarship | The Rotary Club of Carrollton Scholarship are for students who reside in Carroll County. Student must have minimum GPA of 2.5. | $500 | 1”
### `0b89f49391f85e73` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Bowdon Hospital Authority Scholarship | Health Sciences or Nursing Programs; Carroll, Coweta, Douglas, Haralson counties and Cleburne or Randolph counties in Alabama residents. Preference to 30108 ZIP Code. | $500 | 2”
### `104ea6405b933051` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “WellStar Douglas Hospital Scholarship | Students must be enrolled in Health Sciences or Nursing Programs. The Douglas Campus must be students home campus. Student must have a GPA of 2.5 or greater. | $1,000 | 3”
### `10a4f3baf21e7259` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Carrollton Golden K Scholarship | Must be a new student and a Carroll County resident | $1,000 | 2”
### `27712aad025ffdf2` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Mullins Mechanical Pillar Scholarship | The student must be furthering their college education by enrolling at West Georgia Technical College and pursuing a certificate, diploma, or degree in Industrial Systems Technology, Welding and Joining Technology, Engineering Technology, Accounting, Business ”
### `2aa44c8a5c8c43a6` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1000 ⟵ “Doug and Carol Mabry Scholarship Fund | One scholarship will be designated to a Diesel Equipment Technology student, and the other scholarship will be designated to a Welding & Joining Technology student. | $1000 | 2”
### `2c34a42579073628` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Tim B. Clower Scholarship | The Tim B. Clower Scholarship Fund is for students who reside in a home served by GreyStone Power or whose parent or guardian resides in a home served by GreyStone Power. Minimum GPA, 2.5. FALL SEMESTER ONLY | $2,500 | 1”
### `30d548aa83709bf0` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “The Gene Haas Foundation Scholarship | CNC Technology students and/or NIMS credentials | $2,500 | Varies”
### `320c833995028386` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Rotary Club of Carrollton-Dawnbreakers Scholarship | The Rotary Club of Carrollton-Dawnbreakers Scholarship are for students who reside in Carroll County. Preference to students who were awarded the Rotary Club of Carrollton-Dawnbreakers GED Scholarship. | $500 | 2”
### `3d02e94ad762f56f` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Southwire Machine Tool Technology Scholarship | Machine Tool Technology Program; Carroll Campus only | $500 | 10”
### `3de3d4c78e30dacc` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Coweta-Fayette EMC Scholarship | Open to students attending CEC, Coweta Campus, or Franklin Site | $500 | 1”
### `5f15f3f3602edcef` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Manufacturers Education Foundation Scholarship | Student must be enrolled in one of the following areas of study: Electrical Construction and Maintenance, Electronics and Telecommunications, Engineering Technology, Industrial Systems Technology, Machine Tool Technology, Precision Manufacturing and M”
### `66e24404db7fb622` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Star Foundation Scholarship | Haralson County and Cleburne or Randolph counties in Alabama residents. | $500 | 1”
### `7e6b0978feadea79` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: Varies:Scholarship covers student's remaining balance after financial aid is applied. ⟵ “Microsoft Scholars Program | Student must be enrolled in one of the following areas of study: Computer Support Specialist, Networking Specialist, PC Repair and Network Technician, or Helpdesk Specialist. Student must have a home campus of Douglas. Student must have a minimum GPA of 2.0. Student will”
### `81916ba06474db59` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “GreyStone Power Capstone Scholarship | Douglas County resident | $500 | 2”
### `8fd63306ebf60833` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Carroll EMC: Robert D. Tisinger Scholarship Fund | Must live in a home served by Carroll EMC or parent/guardian must live in a home served by Carroll EMC | $500 | 15”
### `94cc15e8747f3a41` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “The Swope Family Fund Pillar Scholarship | Scholarship open to any program of study to students that reside in Coweta County. | $500 | 4”
### `982587ee43fb58cf` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Southwire Precision Manufacturing & Maintenance Scholarship | Precision Manufacturing & Maintenance Program; Carroll Campus only | $500 | 10”
### `a07dc8097e6e39bc` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Kiwanis Club of LaGrange Frear Family Scholarship | The recipient must be a veteran, first responder, or military member, or the spouse or child of a veteran, first responder, or military member, and they must be a resident of Troup, Coweta, Heard, Meriwether, or Harris County. | $500 | 2”
### `a3cefc453d9a18d3` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “J. Randy Jackson Legacy Scholarship | Must have completed coursework at the thINC Academy and be attending the LaGrange Campus. Must be an incoming student. | $500 | 1”
### `a8fa1b8af57715b1` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Holland M. Ware Trade and Industrial Scholarship | Must be pursing a degree in Manufacturing & Production, Installation & Repair Programs; Home Campus must be Coweta, LaGrange, Franklin, or Greenville. | $1,000 | Varies”
### `adbb385cb2f408c9` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Parkway Hospital Auxiliary Scholarship | Health Sciences or Nursing Programs; Douglas Co. Resident | $500 | 3”
### `c37c82dd5af3cd0c` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Tritt Family Foundation, Inc. Scholarship | Student must have a GPA of at least 3.5 and must be working at least 20 hours per week. The student will automatically receive the scholarship the following semester as long as they continue to maintain a 3.5 GPA. | $500 | 2”
### `c66407dbd71859e8` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Southwire Industrial Systems Technology Scholarship | Industrial Systems Technology Program; Carroll Campus only | $500 | 10”
### `d2aa9df7117df938` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Holland M. Ware Healthcare, Nursing, and Public Services Scholarship | Must be pursuing a degree in Nursing, Business Management, Healthcare Management; Home Campus must be Coweta, LaGrange, Franklin, or Greenville. | $1,000 | Varies”
### `e3ad56aa54a7f6e6` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Abraham Baldwin Chapter NSDAR Scholarship | Open to full time students enrolled in an Allied Healthcare program of study. Must have a minimum 3.0 GPA and be a resident of Carroll, Douglas, Heard, haralson, Coweta, Meriwether, or Troup County. SUMMER SEMESTER ONLY | $500 | 1”
### `e72872fcbfe31957` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “WGTC Foundation Scholarship | Open to all students | $500 | 5”
### `f18bd6dc5d6098cc` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Caterpillar DEM Grant Fund Scholarship | Diesel Equipment Tech & Heavy Diesel Service Tech Programs | $500 | 6”
### `m012da3bfe6bef2b` West Georgia Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.westgatech.edu/wp-content/uploads/DE.Student.Handbook.2026-2027-ada-7.23.26.pdf (sha256 34a98a81fa79)
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 3}
  - per_credit_hour_charge: 107 ⟵ “application will result in the student being responsible for their tuition balance. At WGTC, tuition is $107 per credit”
  - eligibility_tier: 2.0 ⟵ “If student has a 2.00 high school GPA, no admissions tes�ng or ACT/SAT is required.”
  - eligibility_tier: 2.0 ⟵ “•   11th and 12th graders with a 2.00 high school GPA can enroll in academic core classes or occupational”
  - eligibility_tier: 2.0 ⟵ “If a student does not have a 2.00 high school GPA, students will need acceptable test scores for entry. At WGTC we”
  - max_credit_hours_per_term: 15 ⟵ “Dual Enrollment students may register for a maximum 15 credit hours during the fall, spring, and summer”
  - eligibility_tier: 2.0 ⟵ “Have a high school GPA of 2.0 documented with official high school transcript, OR have acceptable standardized test scores OR ACCUPLACER scores.”
### `m3255fc09759025f` West Georgia Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/admissions/registrars-office/policies/ (sha256 951995ce6851)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Previous course work must have been completed with a grade of C (2.0) or better to be considered for transfer credit. 5.”
  - max_transfer_credits: 62 ⟵ “The agreement supports multiple UWG’s bachelor’s programs, with up to 62 credit hours transferring for students who complete the Associate of Science in General Studies. “A thriving community is built on collaboration,” concluded Dr.”

## Exceptions (249)

### `be2270577f1342da` Abraham Baldwin Agricultural College — appeals 2024-25 [new] (labeled_in_source)
- source: https://catalog.abac.edu/financialaid/appealprocess (sha256 16cc073ef422)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “All students must complete the Satisfactory Academic Progress Appeal form and submit all the documentation requested on the form.”
### `0cdb4676a8525775` Abraham Baldwin Agricultural College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.abac.edu/admissions/student_accounts/cost-attendance.html (sha256 53c8713fd438)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 3156 ⟵ “Tuition | $3,156 | $3,156 | $3,156”
  - on_campus:Fees: 748 ⟵ “Fees | $ 748 | $ 748 | $ 748”
  - on_campus:Food: 4020 ⟵ “Food | $4,020 | $2,584 | $3,186”
  - on_campus:Housing: 7330 ⟵ “Housing | $7,330 | $3,690 | $7,390”
  - on_campus:Personal Expenses: 2430 ⟵ “Personal Expenses | $2,430 | $2,430 | $2,430”
  - on_campus:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380 | $1,380”
  - on_campus:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - on_campus:Books, Course Materials, Supplies & Equipment: 1330 ⟵ “Books, Course Materials, Supplies & Equipment | $1,330 | $1,330 | $1,330”
  - on_campus:Total: 20452 ⟵ “Total | $20,452 | $15,376 | $19,678”
  - with_parents_or_family:Tuition: 3156 ⟵ “Tuition | $3,156 | $3,156 | $3,156”
  - with_parents_or_family:Fees: 748 ⟵ “Fees | $ 748 | $ 748 | $ 748”
  - with_parents_or_family:Food: 2584 ⟵ “Food | $4,020 | $2,584 | $3,186”
  - with_parents_or_family:Housing: 3690 ⟵ “Housing | $7,330 | $3,690 | $7,390”
  - with_parents_or_family:Personal Expenses: 2430 ⟵ “Personal Expenses | $2,430 | $2,430 | $2,430”
  - with_parents_or_family:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380 | $1,380”
  - with_parents_or_family:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - with_parents_or_family:Books, Course Materials, Supplies & Equipment: 1330 ⟵ “Books, Course Materials, Supplies & Equipment | $1,330 | $1,330 | $1,330”
  - with_parents_or_family:Total: 15376 ⟵ “Total | $20,452 | $15,376 | $19,678”
  - column:Tuition: 3156 ⟵ “Tuition | $3,156 | $3,156 | $3,156”
  - column:Fees: 748 ⟵ “Fees | $ 748 | $ 748 | $ 748”
  - column:Food: 3186 ⟵ “Food | $4,020 | $2,584 | $3,186”
  - column:Housing: 7390 ⟵ “Housing | $7,330 | $3,690 | $7,390”
  - column:Personal Expenses: 2430 ⟵ “Personal Expenses | $2,430 | $2,430 | $2,430”
  - column:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380 | $1,380”
  - column:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - … 2 more rows
### `30727bc2effd044b` Abraham Baldwin Agricultural College — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://catalog.abac.edu/admissions/de (sha256 e90b3bfd92a8)
- issues: stale_year_label:2024-25
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Students must have at least a minimum 3.0 High School Grade Point Average (HSGPA) as calculated by the institution for admission purposes and exempt Learning Support requirements.”
### `7c329ffd1f6af2e7` Abraham Baldwin Agricultural College — credit_policies 2024-25 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.abac.edu/academic-policies-and-procedures/college-level-examination-program-clep (sha256 dca888868f26)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 34, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | course/course | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | No Credit | —”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | course | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | course | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | course/course | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | course | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language - Level 1 Proficiency | 50 | LANG 11XX, LANG 12XX | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language - Level 2 Proficiency | 59 | LANG 11XX, LANG 12XX, LANG 21XX* | 9”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language - Level 1 Proficiency | 50 | LANG 11XX, LANG 12XX | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language - Level 2 Proficiency | 60 | LANG 11XX, LANG 12XX, LANG 21XX* | 9”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language - Level 1 Proficiency | 50 | course, course | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language - Level 2 Proficiency | 63 | course, course, course | 9”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing - Level 1 Proficiency | 50 | course, course | 6”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|65]:  ⟵ “Spanish with Writing - Level 2 Proficiency | 65 | course, course, course, course | 12”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | course*** | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | course*** | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | course*** | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | course | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | No Credit | —”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | course | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | course | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | course | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | course | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | No Credit | —”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 50 | Area E Elective ** | 3”
  - … 13 more rows
### `c4e526c681534667` Abraham Baldwin Agricultural College — credit_policies 2024-25 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.abac.edu/pages/GvTLNxZAmBzLqYbqLZcE (sha256 7097c46ddbd8)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 33, "equivalencies": 54, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art and Design Program: 2-D Art and Design | 3 | ARTS 1020 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art and Design Program: 3-D Art and Design | 3 | ARTS 1030 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art and Design Program: Drawing | 3 | ARTS 1010 | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | course | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL1011K | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | course/course | 4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | course/course, course/course | 8”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | course, course | 8”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | course, course | 8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | course/course | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | course/course, course/course | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | LANG 12XX** | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language and Culture | 4 | LANG 12XX, LANG 21XX ** | 6”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language and Culture | 5 | LANG 12XX, LANG 21XX, LANG 22XX ** | 9”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | course | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | course | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | course | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | course | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Lang/Comp | 3 | course | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Lang/Comp | 5 | course, course | 6”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Lit/Comp | 3 | course | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|5]:  ⟵ “English Lit/Comp | 5 | course, course | 6”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | course/course | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | ELECTIVE IN CORE IMPACTS SOCIAL SCIENCES* | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | LANG 12XX ** | 3”
  - … 29 more rows
### `m20d5d3bfe66fd46` Abraham Baldwin Agricultural College — transfer_policies 2024-25 [new] (labeled_in_source)
- source: https://catalog.abac.edu/academic-policies-and-procedures/residency-requirements-for-graduation (sha256 3a3678a05bf9)
- issues: conflicting_values:residency_requirement_credits, stale_year_label:2024-25
- checks: {"fields": [], "merged_pages": 2}
### `3329572f938dccdd` Agnes Scott College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.agnesscott.edu/admission/undergraduate-admission/scholarships-financial-aid/finaid-faqs.html (sha256 90361863dcf0)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If there are extenuating circumstances the FAFSA doesn’t take into account, such as medical expenses, unemployment or a change in financial situation between years, reach out to your admission counselor or the Office of Financial Aid to walk through our appeal process.”
### `05fbd9ad8fa488f5` Agnes Scott College — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.agnesscott.edu/assets/documents/admission/undergraduate/fa24-by-the-numbers-final.pdf (sha256 07fd122f98db)
- issues: arrangement_unlabeled, stale_year_label:2023-24
- checks: {"columns": 2, "rows": 4}
  - column:in student: 11 ⟵ “in student | 11”
  - column:Tuition: 47820 ⟵ “Tuition | $47,820”
  - column:Room and Board: 13375 ⟵ “Room and Board | $13,375”
  - column:Student Activity Fee: 330 ⟵ “Student Activity Fee | $330”
  - column:Average class size is 15: 61525 ⟵ “Average class size is 15 | Total | $61,525”
### `3b3225ae42c506b9` Albany State University — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.asurams.edu/enrollment-management/financial-aid/2425%20SAP%20Policy_FINAL.pdf (sha256 c28490308b6d)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “SAP Appeals Students who lose their financial aid eligibility may appeal based on mitigating circumstances.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process  Please log into asurams.studentforms.com.”
  - sentence: sap_appeal ⟵ “Please note that you MUST be an admitted student to begin the SAP appeal process.”
  - sentence: sap_appeal ⟵ “Once logged in you will see an outstanding task titled “SAP Appeal”.”
  - sentence: sap_appeal ⟵ “Incomplete appeals may result in automatic denial.  Appeals will be reviewed by the SAP Appeals Committee.”
  - sentence: sap_appeal ⟵ “PROBATION Status Students who lose financial aid eligibility, but have an approved SAP appeal are placed on financial aid PROBATION.”
### `3d8c6058a2c2b788` Albany State University — appeals 2022-23 [new] (labeled_in_source)
- source: https://www.asurams.edu/enrollment-management/financial-aid/docs/22_23%20SAP%20Policy_FINAL.pdf.pdf (sha256 b5ad049aea6d)
- issues: stale_year_label:2022-23, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “SAP Appeals Students who lose their financial aid eligibility may appeal based on mitigating circumstances.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process  Please log into asurams.studentforms.com.”
  - sentence: sap_appeal ⟵ “Please note that you MUST be an admitted student to begin the SAP appeal process.”
  - sentence: sap_appeal ⟵ “Once logged in you will see an outstanding task titled “SAP Appeal”.”
  - sentence: sap_appeal ⟵ “Incomplete appeals may result in automatic denial.  Appeals will be reviewed by the SAP Appeals Committee.”
  - sentence: sap_appeal ⟵ “PROBATION Status Students who lose financial aid eligibility, but have an approved SAP appeal are placed on financial aid PROBATION.”
### `5a2c1d433984e91b` Albany State University — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.asurams.edu/enrollment-management/financial-aid/23_24%20SAP%20Policy_newFINAL.pdf (sha256 2d625be45b92)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “SAP Appeals Students who lose their financial aid eligibility may appeal based on mitigating circumstances.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process  Please log into asurams.studentforms.com.”
  - sentence: sap_appeal ⟵ “Please note that you MUST be an admitted student to begin the SAP appeal process.”
  - sentence: sap_appeal ⟵ “Once logged in you will see an outstanding task titled “SAP Appeal”.”
  - sentence: sap_appeal ⟵ “Incomplete appeals may result in automatic denial.  Appeals will be reviewed by the SAP Appeals Committee.”
  - sentence: sap_appeal ⟵ “PROBATION Status Students who lose financial aid eligibility, but have an approved SAP appeal are placed on financial aid PROBATION.”
### `fffe30bb1d3938f8` Albany State University — appeals 2021-22 [new] (labeled_in_source)
- source: https://www.asurams.edu/enrollment-management/financial-aid/docs/21_22%20SAP%20Policy_FINAL.pdf (sha256 35ded319cf0d)
- issues: stale_year_label:2021-22, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “Albany, GA 31707 Telephone: 229.500.4358 Fax: 229.500.4946 SAP Appeals Students who lose their financial aid eligibility may appeal based on mitigating circumstances.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process  Please log into asurams.verifymyfafsa.com.”
  - sentence: sap_appeal ⟵ “Please note that you MUST be an admitted student to begin the SAP appeal process.”
  - sentence: sap_appeal ⟵ “Once logged in you will see an outstanding task titled “SAP Appeal”.”
  - sentence: sap_appeal ⟵ “Incomplete appeals may result in automatic denial.  Appeals will be reviewed by the SAP Appeals Committee.”
  - sentence: sap_appeal ⟵ “PROBATION Status Students who lose financial aid eligibility, but have an approved SAP appeal are placed on financial aid PROBATION.”
### `7a5c87c9cfc6a318` Albany Technical College — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.albanytech.edu/college-catalog/current/transfer-credit (sha256 48bfff4e08e5)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Only grades of “C” or better are accepted as transfer grades.”
### `49832c6a685607e0` Andrew College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.andrewcollege.edu/tuition-room-and-board/ (sha256 d536ae2feabc)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 4}
  - column:Tuition: 9802.0 ⟵ “Tuition | $9802.00 | $9,802.00 | $19,604.00”
  - column:Room (starting point): 3088.0 ⟵ “Room (starting point) | $3,088.00 | $3,088.00 | $6,176.00”
  - column:Board: 3350.0 ⟵ “Board | $3,350.00 | $3,350.00 | $6,700.00”
  - column:Total: 16240.0 ⟵ “Total | $16,240.00 | $16,240.00 | $32,480.00”
  - column:Tuition: 9802.0 ⟵ “Tuition | $9802.00 | $9,802.00 | $19,604.00”
  - column:Room (starting point): 3088.0 ⟵ “Room (starting point) | $3,088.00 | $3,088.00 | $6,176.00”
  - column:Board: 3350.0 ⟵ “Board | $3,350.00 | $3,350.00 | $6,700.00”
  - column:Total: 16240.0 ⟵ “Total | $16,240.00 | $16,240.00 | $32,480.00”
  - column:Tuition: 19604.0 ⟵ “Tuition | $9802.00 | $9,802.00 | $19,604.00”
  - column:Room (starting point): 6176.0 ⟵ “Room (starting point) | $3,088.00 | $3,088.00 | $6,176.00”
  - column:Board: 6700.0 ⟵ “Board | $3,350.00 | $3,350.00 | $6,700.00”
  - column:Total: 32480.0 ⟵ “Total | $16,240.00 | $16,240.00 | $32,480.00”
### `780e544c32dcecf6` Athens Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: https://athenstech.edu/admissions-financial-aid/tuition-financial-aid/ (sha256 9ed7ede0af21)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “Not all requests will qualify for Dependency Override.”
  - sentence: dependency_override ⟵ “A Dependency Override request can take up to 5 to 10 business days to process once all required documentation is provided.”
  - sentence: dependency_override ⟵ “If you have an unusual or extenuating circumstance that you believe warrants you independency status, you will need to complete the Dependency Override Appeal form, along with all required supporting documents.”
### `947829378ce44d80` Athens Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: http://athenstech.edu/admissions-financial-aid/tuition-financial-aid/ (sha256 1642145c9460)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “I have questions about some specific Financial Aid policies such as the HOPE Cap or appealing a financial aid exclusion.”
### `e9288efae9f61eb0` Athens Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://athenstech.edu/admissions-financial-aid/tuition-financial-aid/financial-aid-policies/ (sha256 1240f87b1f71)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “A Request for Appeal of Financial Aid Exclusion form must be submitted explaining the extenuating circumstances, how these circumstances have changed, and their plan to maintain satisfactory academic progress if the appeal is approved.”
### `f38b6b88f4c2b781` Athens Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: http://athenstech.edu/admissions-financial-aid/tuition-financial-aid/ (sha256 1642145c9460)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Federal regulations permit the College to override a student’s dependency status for Federal Financial Aid purposes if unusual circumstances exist and can be documented.”
  - sentence: need_based_special_circumstances ⟵ “The following conditions are NOT considered unusual circumstances: Parents refusal to contribute to the student’s education Parents are unwilling to provide information for the FAFSA or verification Parents do not claim the student as a dependent for income tax purposes Student demonstrates total self-sufficiency Student does not communicate with parents.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal Athens Technical College recognizes that changes may be experienced in the financial situation of a household.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeals are made based on a change of income that is beyond your control.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances that warrant an appeal may include the following: Separation or Divorce Loss or reduction of employment (those due to cause or personal choice are not applicable) Death of parent or spouse Child Support Damage Please contact the Financial Aid Department for a Special Circumstance Appeal form to be upload in your Campus Logic portal.”
  - sentence: need_based_special_circumstances ⟵ “All financial documents used for the current year’s FAFSA and the financial documents for the change in income year will be needed.”
### `fb0f20ad20862575` Athens Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: https://athenstech.edu/admissions-financial-aid/tuition-financial-aid/ (sha256 9ed7ede0af21)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Athens, GA 30601 Fax to: (706) 425-3086 Email to: Scanned copies to financialaid@athenstech.edu Deliver to: Financial Aid in the H-700 Building, Athens Main Campus Sign Up For A Payment Plan Professional Judgement Dependency Override Appeal Athens Technical College understands that navigating the financial aid process can be daunting, and the Athens Technical College Financial Aid Staff Members ar”
  - sentence: professional_judgment ⟵ “Financial Aid Administrators are authorized to use professional judgement on a case-by-case basis for students with special circumstances that affect a family’s ability to pay for college education that are not reflected in the information provided on the FAFSA.”
  - sentence: professional_judgment ⟵ “In many cases, professional judgement adjustments made to the FAFSA do no result in significant changes to the Student Aid Index (SAI).”
### `bb3fae757e88073f` Athens Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://athenstech.edu/admissions-financial-aid/tuition-financial-aid/cost-of-attendance/ (sha256 144b764a669c)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Tuition and Fees: 3662 ⟵ “Tuition and Fees | $3,662”
  - column:Food and Housing: 12056 ⟵ “Food and Housing | $12,056”
  - column:Books and Supplies: 900 ⟵ “Books and Supplies | $900”
  - column:Transportation: 2880 ⟵ “Transportation | $2,880”
  - column:Miscellaneous Personal Expenses: 3186 ⟵ “Miscellaneous Personal Expenses | $3,186”
### `881f19335047ea12` Atlanta Metropolitan State College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.atlm.edu/students/financial-aid.aspx (sha256 c7cb02589891)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Net Price Calculator Check the Net Price Calculator Course Program of Study (CPoS) FAQs Review the CPoS Faqs Satisfactory Academic Progress (SAP) Policy and Appeals Process View the Satisfactory Academic Progress (SAP) Policy Appeals Process A student who has lost eligibility for financial aid due to Satisfactory Academic Progress may feel that there were unforeseeable circumstances that prevented”
  - sentence: sap_appeal ⟵ “Go to www.atlm.edu and select MyATLM Enter your User Name and Password Select Student Resources and Campus Logic Select Manage Request and select SAP Appeal Please be sure to follow the instructions carefully and accurately.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Committee will review the Appeal and will determine whether the appeal is granted.”
### `10f5416712393475` Atlanta Metropolitan State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.atlm.edu/downloads/Tuition_Fees/on-campus-2026-2027-tuition-and-fee-schedule.pdf (sha256 a857b9365520)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, conflicting_sources:https://www.atlm.edu/downloads/Tuition_Fees/e-core%202026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/e-major-2026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/online-2026-2027-tuition-and-fee-schedule.pdf
- checks: {"columns": 20, "rows": 6}
  - column:Hours: 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 110.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Technology Fee: 40.0 ⟵ “Technology Fee | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00”
  - column:Activity Fee: 60.0 ⟵ “Activity Fee | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00”
  - column:Student Center Fee: 240.0 ⟵ “Student Center Fee | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00”
  - column:Total: 450.0 ⟵ “Total | $ 450.00 | $ 560.00 | $ 670.00 | $ 780.00 | $ 890.00 | $ 1,000.00 | $ 1,110.00 | $ 1,220.00 | $ 1,330.00 | $ 1,440.00 | $ 1,550.00 | $ 1,660.00 | $ 1,770.00 | $ 1,880.00 | $ 1,990.00”
  - column:Hours: 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 435.0 ⟵ “Tuition | $ 435.00 | $ 870.00 | $ 1,305.00 | $ 1,740.00 | $ 2,175.00 | $ 2,610.00 | $ 3,045.00 | $ 3,480.00 | $ 3,915.00 | $ 4,350.00 | $ 4,785.00 | $ 5,220.00 | $ 5,655.00 | $ 6,090.00 | $ 6,525.00”
  - column:Technology Fee: 40.0 ⟵ “Technology Fee | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00”
  - column:Activity Fee: 60.0 ⟵ “Activity Fee | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00”
  - column:Student Center Fee: 240.0 ⟵ “Student Center Fee | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00”
  - column:Total: 775.0 ⟵ “Total | $ 775.00 | $ 1,210.00 | $ 1,645.00 | $ 2,080.00 | $ 2,515.00 | $ 2,950.00 | $ 3,385.00 | $ 3,820.00 | $ 4,255.00 | $ 4,690.00 | $ 5,125.00 | $ 5,560.00 | $ 5,995.00 | $ 6,430.00 | $ 6,865.00”
  - column:Hours: 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 448.0 ⟵ “Tuition | $ 448.00 | $ 896.00 | $ 1,344.00 | $ 1,792.00 | $ 2,240.00 | $ 2,688.00 | $ 3,136.00 | $ 3,584.00 | $ 4,032.00 | $ 4,480.00 | $ 4,928.00 | $ 5,376.00 | $ 5,824.00 | $ 6,272.00 | $ 6,720.00”
  - column:Technology Fee: 40.0 ⟵ “Technology Fee | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00”
  - column:Activity Fee: 60.0 ⟵ “Activity Fee | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00”
  - column:Student Center Fee: 240.0 ⟵ “Student Center Fee | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00”
  - column:Total: 788.0 ⟵ “Total | $ 788.00 | $ 1,236.00 | $ 1,684.00 | $ 2,132.00 | $ 2,580.00 | $ 3,028.00 | $ 3,476.00 | $ 3,924.00 | $ 4,372.00 | $ 4,820.00 | $ 5,268.00 | $ 5,716.00 | $ 6,164.00 | $ 6,612.00 | $ 7,060.00”
  - column:Hours: 2 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 220.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Technology Fee: 40.0 ⟵ “Technology Fee | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00”
  - column:Activity Fee: 60.0 ⟵ “Activity Fee | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00”
  - column:Student Center Fee: 240.0 ⟵ “Student Center Fee | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00”
  - column:Total: 560.0 ⟵ “Total | $ 450.00 | $ 560.00 | $ 670.00 | $ 780.00 | $ 890.00 | $ 1,000.00 | $ 1,110.00 | $ 1,220.00 | $ 1,330.00 | $ 1,440.00 | $ 1,550.00 | $ 1,660.00 | $ 1,770.00 | $ 1,880.00 | $ 1,990.00”
  - column:Hours: 2 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - … 245 more rows
### `a39605d0d2a98df5` Atlanta Metropolitan State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.atlm.edu/downloads/Tuition_Fees/e-core%202026-2027-tuition-and-fee-schedule.pdf (sha256 a99093744b99)
- issues: arrangement_unlabeled, components_do_not_reconcile, implausible_amount, residency_unknown, conflicting_sources:https://www.atlm.edu/downloads/Tuition_Fees/e-major-2026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/on-campus-2026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/online-2026-2027-tuition-and-fee-schedule.pdf
- checks: {"columns": 15, "components_reconcile": false, "rows": 4}
  - column:Hours: 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 161.0 ⟵ “Tuition | $ 161.00 | $ 322.00 | $ 483.00 | $ 644.00 | $ 805.00 | $ 966.00 | $ 1,127.00 | $ 1,288.00 | $ 1,449.00 | $ 1,610.00 | $ 1,771.00 | $ 1,932.00 | $ 2,093.00 | $ 2,254.00 | $ 2,415.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 351.0 ⟵ “Total | $ 351.00 | $ 512.00 | $ 673.00 | $ 834.00 | $ 995.00 | $ 1,156.00 | $ 1,317.00 | $ 1,478.00 | $ 1,639.00 | $ 1,800.00 | $ 1,961.00 | $ 2,122.00 | $ 2,283.00 | $ 2,444.00 | $ 2,605.00”
  - column:Hours: 2 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 322.0 ⟵ “Tuition | $ 161.00 | $ 322.00 | $ 483.00 | $ 644.00 | $ 805.00 | $ 966.00 | $ 1,127.00 | $ 1,288.00 | $ 1,449.00 | $ 1,610.00 | $ 1,771.00 | $ 1,932.00 | $ 2,093.00 | $ 2,254.00 | $ 2,415.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 512.0 ⟵ “Total | $ 351.00 | $ 512.00 | $ 673.00 | $ 834.00 | $ 995.00 | $ 1,156.00 | $ 1,317.00 | $ 1,478.00 | $ 1,639.00 | $ 1,800.00 | $ 1,961.00 | $ 2,122.00 | $ 2,283.00 | $ 2,444.00 | $ 2,605.00”
  - column:Hours: 3 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 483.0 ⟵ “Tuition | $ 161.00 | $ 322.00 | $ 483.00 | $ 644.00 | $ 805.00 | $ 966.00 | $ 1,127.00 | $ 1,288.00 | $ 1,449.00 | $ 1,610.00 | $ 1,771.00 | $ 1,932.00 | $ 2,093.00 | $ 2,254.00 | $ 2,415.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 673.0 ⟵ “Total | $ 351.00 | $ 512.00 | $ 673.00 | $ 834.00 | $ 995.00 | $ 1,156.00 | $ 1,317.00 | $ 1,478.00 | $ 1,639.00 | $ 1,800.00 | $ 1,961.00 | $ 2,122.00 | $ 2,283.00 | $ 2,444.00 | $ 2,605.00”
  - column:Hours: 4 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 644.0 ⟵ “Tuition | $ 161.00 | $ 322.00 | $ 483.00 | $ 644.00 | $ 805.00 | $ 966.00 | $ 1,127.00 | $ 1,288.00 | $ 1,449.00 | $ 1,610.00 | $ 1,771.00 | $ 1,932.00 | $ 2,093.00 | $ 2,254.00 | $ 2,415.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 834.0 ⟵ “Total | $ 351.00 | $ 512.00 | $ 673.00 | $ 834.00 | $ 995.00 | $ 1,156.00 | $ 1,317.00 | $ 1,478.00 | $ 1,639.00 | $ 1,800.00 | $ 1,961.00 | $ 2,122.00 | $ 2,283.00 | $ 2,444.00 | $ 2,605.00”
  - column:Hours: 5 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 805.0 ⟵ “Tuition | $ 161.00 | $ 322.00 | $ 483.00 | $ 644.00 | $ 805.00 | $ 966.00 | $ 1,127.00 | $ 1,288.00 | $ 1,449.00 | $ 1,610.00 | $ 1,771.00 | $ 1,932.00 | $ 2,093.00 | $ 2,254.00 | $ 2,415.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 995.0 ⟵ “Total | $ 351.00 | $ 512.00 | $ 673.00 | $ 834.00 | $ 995.00 | $ 1,156.00 | $ 1,317.00 | $ 1,478.00 | $ 1,639.00 | $ 1,800.00 | $ 1,961.00 | $ 2,122.00 | $ 2,283.00 | $ 2,444.00 | $ 2,605.00”
  - column:Hours: 6 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 966.0 ⟵ “Tuition | $ 161.00 | $ 322.00 | $ 483.00 | $ 644.00 | $ 805.00 | $ 966.00 | $ 1,127.00 | $ 1,288.00 | $ 1,449.00 | $ 1,610.00 | $ 1,771.00 | $ 1,932.00 | $ 2,093.00 | $ 2,254.00 | $ 2,415.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 1156.0 ⟵ “Total | $ 351.00 | $ 512.00 | $ 673.00 | $ 834.00 | $ 995.00 | $ 1,156.00 | $ 1,317.00 | $ 1,478.00 | $ 1,639.00 | $ 1,800.00 | $ 1,961.00 | $ 2,122.00 | $ 2,283.00 | $ 2,444.00 | $ 2,605.00”
  - column:Hours: 7 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - … 35 more rows
### `c5a319165cb22351` Atlanta Metropolitan State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.atlm.edu/downloads/Tuition_Fees/online-2026-2027-tuition-and-fee-schedule.pdf (sha256 58efe57b304b)
- issues: arrangement_unlabeled, components_do_not_reconcile, implausible_amount, residency_unknown, conflicting_sources:https://www.atlm.edu/downloads/Tuition_Fees/e-core%202026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/e-major-2026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/on-campus-2026-2027-tuition-and-fee-schedule.pdf
- checks: {"columns": 15, "components_reconcile": false, "rows": 4}
  - column:Hours: 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 110.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 300.0 ⟵ “Total | $ 300.00 | $ 410.00 | $ 520.00 | $ 630.00 | $ 740.00 | $ 850.00 | $ 960.00 | $ 1,070.00 | $ 1,180.00 | $ 1,290.00 | $ 1,400.00 | $ 1,510.00 | $ 1,620.00 | $ 1,730.00 | $ 1,840.00”
  - column:Hours: 2 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 220.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 410.0 ⟵ “Total | $ 300.00 | $ 410.00 | $ 520.00 | $ 630.00 | $ 740.00 | $ 850.00 | $ 960.00 | $ 1,070.00 | $ 1,180.00 | $ 1,290.00 | $ 1,400.00 | $ 1,510.00 | $ 1,620.00 | $ 1,730.00 | $ 1,840.00”
  - column:Hours: 3 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 330.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 520.0 ⟵ “Total | $ 300.00 | $ 410.00 | $ 520.00 | $ 630.00 | $ 740.00 | $ 850.00 | $ 960.00 | $ 1,070.00 | $ 1,180.00 | $ 1,290.00 | $ 1,400.00 | $ 1,510.00 | $ 1,620.00 | $ 1,730.00 | $ 1,840.00”
  - column:Hours: 4 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 440.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 630.0 ⟵ “Total | $ 300.00 | $ 410.00 | $ 520.00 | $ 630.00 | $ 740.00 | $ 850.00 | $ 960.00 | $ 1,070.00 | $ 1,180.00 | $ 1,290.00 | $ 1,400.00 | $ 1,510.00 | $ 1,620.00 | $ 1,730.00 | $ 1,840.00”
  - column:Hours: 5 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 550.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 740.0 ⟵ “Total | $ 300.00 | $ 410.00 | $ 520.00 | $ 630.00 | $ 740.00 | $ 850.00 | $ 960.00 | $ 1,070.00 | $ 1,180.00 | $ 1,290.00 | $ 1,400.00 | $ 1,510.00 | $ 1,620.00 | $ 1,730.00 | $ 1,840.00”
  - column:Hours: 6 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 660.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 850.0 ⟵ “Total | $ 300.00 | $ 410.00 | $ 520.00 | $ 630.00 | $ 740.00 | $ 850.00 | $ 960.00 | $ 1,070.00 | $ 1,180.00 | $ 1,290.00 | $ 1,400.00 | $ 1,510.00 | $ 1,620.00 | $ 1,730.00 | $ 1,840.00”
  - column:Hours: 7 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - … 35 more rows
### `e97991271ed9b8fc` Atlanta Metropolitan State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.atlm.edu/downloads/Tuition_Fees/e-major-2026-2027-tuition-and-fee-schedule.pdf (sha256 9007a1de3300)
- issues: arrangement_unlabeled, components_do_not_reconcile, implausible_amount, residency_unknown, conflicting_sources:https://www.atlm.edu/downloads/Tuition_Fees/e-core%202026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/on-campus-2026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/online-2026-2027-tuition-and-fee-schedule.pdf
- checks: {"columns": 15, "components_reconcile": false, "rows": 4}
  - column:Hours: 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 201.0 ⟵ “Tuition | $ 201.00 | $ 402.00 | $ 603.00 | $ 804.00 | $ 1,005.00 | $ 1,206.00 | $ 1,407.00 | $ 1,608.00 | $ 1,809.00 | $ 2,010.00 | $ 2,211.00 | $ 2,412.00 | $ 2,613.00 | $ 2,814.00 | $ 3,015.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 391.0 ⟵ “Total | $ 391.00 | $ 592.00 | $ 793.00 | $ 994.00 | $ 1,195.00 | $ 1,396.00 | $ 1,597.00 | $ 1,798.00 | $ 1,999.00 | $ 2,200.00 | $ 2,401.00 | $ 2,602.00 | $ 2,803.00 | $ 3,004.00 | $ 3,205.00”
  - column:Hours: 2 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 402.0 ⟵ “Tuition | $ 201.00 | $ 402.00 | $ 603.00 | $ 804.00 | $ 1,005.00 | $ 1,206.00 | $ 1,407.00 | $ 1,608.00 | $ 1,809.00 | $ 2,010.00 | $ 2,211.00 | $ 2,412.00 | $ 2,613.00 | $ 2,814.00 | $ 3,015.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 592.0 ⟵ “Total | $ 391.00 | $ 592.00 | $ 793.00 | $ 994.00 | $ 1,195.00 | $ 1,396.00 | $ 1,597.00 | $ 1,798.00 | $ 1,999.00 | $ 2,200.00 | $ 2,401.00 | $ 2,602.00 | $ 2,803.00 | $ 3,004.00 | $ 3,205.00”
  - column:Hours: 3 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 603.0 ⟵ “Tuition | $ 201.00 | $ 402.00 | $ 603.00 | $ 804.00 | $ 1,005.00 | $ 1,206.00 | $ 1,407.00 | $ 1,608.00 | $ 1,809.00 | $ 2,010.00 | $ 2,211.00 | $ 2,412.00 | $ 2,613.00 | $ 2,814.00 | $ 3,015.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 793.0 ⟵ “Total | $ 391.00 | $ 592.00 | $ 793.00 | $ 994.00 | $ 1,195.00 | $ 1,396.00 | $ 1,597.00 | $ 1,798.00 | $ 1,999.00 | $ 2,200.00 | $ 2,401.00 | $ 2,602.00 | $ 2,803.00 | $ 3,004.00 | $ 3,205.00”
  - column:Hours: 4 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 804.0 ⟵ “Tuition | $ 201.00 | $ 402.00 | $ 603.00 | $ 804.00 | $ 1,005.00 | $ 1,206.00 | $ 1,407.00 | $ 1,608.00 | $ 1,809.00 | $ 2,010.00 | $ 2,211.00 | $ 2,412.00 | $ 2,613.00 | $ 2,814.00 | $ 3,015.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 994.0 ⟵ “Total | $ 391.00 | $ 592.00 | $ 793.00 | $ 994.00 | $ 1,195.00 | $ 1,396.00 | $ 1,597.00 | $ 1,798.00 | $ 1,999.00 | $ 2,200.00 | $ 2,401.00 | $ 2,602.00 | $ 2,803.00 | $ 3,004.00 | $ 3,205.00”
  - column:Hours: 5 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 1005.0 ⟵ “Tuition | $ 201.00 | $ 402.00 | $ 603.00 | $ 804.00 | $ 1,005.00 | $ 1,206.00 | $ 1,407.00 | $ 1,608.00 | $ 1,809.00 | $ 2,010.00 | $ 2,211.00 | $ 2,412.00 | $ 2,613.00 | $ 2,814.00 | $ 3,015.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 1195.0 ⟵ “Total | $ 391.00 | $ 592.00 | $ 793.00 | $ 994.00 | $ 1,195.00 | $ 1,396.00 | $ 1,597.00 | $ 1,798.00 | $ 1,999.00 | $ 2,200.00 | $ 2,401.00 | $ 2,602.00 | $ 2,803.00 | $ 3,004.00 | $ 3,205.00”
  - column:Hours: 6 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 1206.0 ⟵ “Tuition | $ 201.00 | $ 402.00 | $ 603.00 | $ 804.00 | $ 1,005.00 | $ 1,206.00 | $ 1,407.00 | $ 1,608.00 | $ 1,809.00 | $ 2,010.00 | $ 2,211.00 | $ 2,412.00 | $ 2,613.00 | $ 2,814.00 | $ 3,015.00”
  - column:Online Learning Fee: 190.0 ⟵ “Online Learning Fee | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00 | $ 190.00”
  - column:Total: 1396.0 ⟵ “Total | $ 391.00 | $ 592.00 | $ 793.00 | $ 994.00 | $ 1,195.00 | $ 1,396.00 | $ 1,597.00 | $ 1,798.00 | $ 1,999.00 | $ 2,200.00 | $ 2,401.00 | $ 2,602.00 | $ 2,803.00 | $ 3,004.00 | $ 3,205.00”
  - column:Hours: 7 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - … 35 more rows
### `67da6da08479bfc3` Atlanta Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.atlantatech.edu/financial-aid/satisfactory-academic-progress/ (sha256 6e7f6894a5d5)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If your information is rejected by the SAP Committee you may re-submit appeal with the appropriate supporting documents, however, your information will be reviewed during the next scheduled SAP appeals committee meeting.”
  - sentence: sap_appeal ⟵ “SAP Appeal Letter Requirements Expand Your SAP appeal letter should address the following: 1.”
  - sentence: sap_appeal ⟵ “The steps you will take to ensure you continue to meet Satisfactory Academic Progress in the future semester(s). ** Failure to answer all questions below will result in a rejected SAP Appeal form ** NEED ASSISTANCE?”
### `0da1729692ffc42a` Augusta Technical College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.augustatech.edu/paying-for-college/satisfactory-academic-progress-sap.cms (sha256 e06c5658745f)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Contact Financial Aid at finaid@augustatech.edu Satisfactory Academic Progress (SAP) Satisfactory Academic Progress (SAP) HOPE Career Grant How to Apply for Financial Aid Net Price Calculator VA College Financing Plan (Shopping Sheet) Satisfactory Academic Progress (SAP) Payment Options Refund Policy Resources, Documents and Forms Tuition and Fees Types of Aid Apply for Scholarships External Schol”
### `220919a8646ace41` Augusta Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.augustatech.edu/paying-for-college/paying-for-college.cms (sha256 967a80cd38a2)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.augustatech.edu/paying-for-college/professional-judgement.cms
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Paying for College Paying for College HOPE Career Grant How to Apply for Financial Aid Net Price Calculator VA College Financing Plan (Shopping Sheet) Satisfactory Academic Progress (SAP) Payment Options Refund Policy Resources, Documents and Forms Tuition and Fees Types of Aid Apply for Scholarships External Scholarships Professional Judgment Apply Register Request Info Augusta 3200 Augusta Tech ”
### `7d6372fec8a7cea3` Augusta Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augustatech.edu/paying-for-college/professional-judgement.cms (sha256 64fe88a1c6e7)
- issues: semantic_review_required, conflicting_sources:https://www.augustatech.edu/paying-for-college/paying-for-college.cms
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Student Resources Home Menu Search Professional Judgment Homepage Paying for College Professional Judgment Overview There may be special or unusual circumstances that negatively impact your ability to pay for college and you believe these circumstances are not accurately reflected on your Free Application for Federal Student Aid (FAFSA), you should speak with a financial aid administrator (FAA).”
  - sentence: professional_judgment ⟵ “Professional Judgment Professional Judgment HOPE Career Grant How to Apply for Financial Aid Net Price Calculator VA College Financing Plan (Shopping Sheet) Satisfactory Academic Progress (SAP) Payment Options Refund Policy Resources, Documents and Forms Tuition and Fees Types of Aid Apply for Scholarships External Scholarships Professional Judgment Apply Register Request Info Augusta 3200 Augusta”
### `c9b3865dead27d46` Augusta Technical College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.augustatech.edu/paying-for-college/satisfactory-academic-progress-sap.cms (sha256 e06c5658745f)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Deadlines: Fall 2026 (August 17, 2026 – December 11, 2026) Spring 2027 (January 11, 2027 – May 7, 2027) Summer 2027 (May 17, 2027 – July 29, 2027) *In order to submit an appeal you must be registered for classes* Appeals for Fall 2026 will be accepted July 14, 2026 – August 14, 2026.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form, SAP Academic Plan, and supporting documentation should be uploaded through your Cougar Web account.”
  - sentence: sap_appeal ⟵ “From here you will see a tab for the SAP appeal with a task indicator indicating that there is a task for you to complete.”
### `d94707edce6ac5a9` Augusta Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augustatech.edu/paying-for-college/professional-judgement.cms (sha256 64fe88a1c6e7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Override Appeal Form The Dependency Override Appeal can be completed on CougarNet.”
### `e82f57d2ca0a4387` Augusta Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augustatech.edu/paying-for-college/professional-judgement.cms (sha256 64fe88a1c6e7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The Special Circumstances request can be completed on CougarNet.”
  - sentence: need_based_special_circumstances ⟵ “There are limitations on what we can do, but the results depend on the circumstances that you indicate on the Special Circumstances Request form.”
  - sentence: need_based_special_circumstances ⟵ “How to Request a Special Circumstance: EFC/SAI Calculation From your browser type in https://augustatech.studentforms.com (works best in Chrome) and login using your Cougar Web username and password .”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances may include: Change in employment status, income, or assets Change in housing status (i.e. homelessness) Medical, dental, or nursing home expenses not covered by insurance Child or dependent care expenses Other changes or adjustments that impact the student’s ability to pay for college. ***This is not an exhaustive list.”
  - sentence: need_based_special_circumstances ⟵ “The Dependency Override Appeal is an option for students who have unusual circumstances which may qualify them for independent status for FAFSA purposes.”
  - sentence: need_based_special_circumstances ⟵ “How to Request Unusual Circumstance: Dependency Override From your web browser type in https://augustatech.studentforms.com (works best in Chrome) and login using your Cougar Web username and password.”
### `md05c1e820a9020f` Augusta Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.augustatech.edu/admissions-and-registration/transfer-student-faqs.cms?contentType=textonly (sha256 d409c99fe965)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “A grade of "C" or higher must be earned for courses to be transferred.”
  - min_grade: C- ⟵ “All academic course work in which a student has earned a grade of “C-” or higher is fully transferable if it fits into the student’s degree plan of study.”
  - min_grade: C ⟵ “A grade of "C" or higher must be earned for courses to be transferred.”
### `16f3f594fcde3d64` Augusta University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.augusta.edu/finaid/professionaljudgment/index.php (sha256 ec460ad68f22)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “With limitations, and on a case-by-case basis, the FAAs may make adjustments to the data on the FAFSA. 2026-2027 Special Circumstance Request 2026-2027 Request for Independent Status Augusta University's Professional Judgement Policy Contact Us Financial Aid Summerville Campus Fanning Hall 706-737-1524 osfa@augusta.edu Mailing: 1120 15th Street, Fanning Hall, Augusta GA 30912 2500 Walton Way, Augu”
### `7248cbd24317d933` Augusta University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augusta.edu/finaid/documents/sap_appealform_updated10092023.pdf (sha256 cf4bb744dfa8)
- issues: semantic_review_required, conflicting_sources:https://www.augusta.edu/finaid/documents/standardssapnewrevf.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Augusta, GA 30912 Phone: 706-737-1524 Fax: 706-737-1777 osfa@augusta.edu SATISFACTORY ACADEMIC PROGRESS (SAP) APPEAL FORM Name: Student ID: Major: Email: Check the term for which you are submitting this appeal: Fall Spring Summer Check ✔ the corresponding circumstance which best indicates your reason for submitting the SAP Appeal.”
  - sentence: sap_appeal ⟵ “Student Certification I, , understand that this appeal is subject to review by the SAP Appeals Committee and that approval or denial of this appeal will be based on the information included (and/or attached).”
### `95f2b044d76f02fd` Augusta University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.augusta.edu/finaid/professionaljudgment/index.php (sha256 ec460ad68f22)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The following are not considered special circumstances: Private school costs Consumer debt, including student loan debt Any estimated future circumstances Independent Status Request Form The Independent Status Request form is an option for students who have unusual circumstances that may qualify them for independent status.”
### `b887a47cc5d5d6b0` Augusta University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augusta.edu/finaid/documents/standardssapnewrevf.pdf (sha256 47c7f68a7b69)
- issues: semantic_review_required, conflicting_sources:https://www.augusta.edu/finaid/documents/sap_appealform_updated10092023.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Students who submit SAP appeals are also notified of the Appeals Committee’s decision via institutional email.”
  - sentence: sap_appeal ⟵ “If this occurs and the student wishes to appeal the suspension from financial aid eligibility, a Satisfactory Academic Progress Appeal Form must be submitted.”
  - sentence: sap_appeal ⟵ “Students appealing Maximum Allowable Time Frame must complete and submit the SAP Appeal Form along with an academic plan.”
  - sentence: sap_appeal ⟵ “Any exceptions due to extenuating circumstances must be granted through the SAP appeal process. o Qualitative Standards -­‐ The Professional programs evaluate students at the end of each academic year.”
### `8d30a426b3936f3d` Berry College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.berry.edu/scholarships-and-aid/maintaining-aid (sha256 e29f5dcb5889)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The form to submit an appeal (SAP Appeal Form), and additional information, can be found in the students' financial aid portal at financialaid.berry.edu.”
### `bae8618dba9bd195` Berry College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.berry.edu/scholarships-and-aid/faq (sha256 20871319e767)
- issues: semantic_review_required, conflicting_sources:https://www.berry.edu/scholarships-and-aid/maintaining-aid
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “The Office of Financial Aid at Berry College may use the authority dispensed by the Higher Education Act of 1965, as amended, to exercise professional judgment and adjust certain data elements on the FAFSA under limited unusual circumstances.”
  - sentence: professional_judgment ⟵ “Your counselor will assess the impact of these circumstances in your financial aid eligibility, as well as provide advice about the process and application for professional judgment if applicable.”
  - sentence: professional_judgment ⟵ “Divorce of parents or student Death of parent or spouse Loss of employment and continued unemployment beyond four months Loss of other income or benefits (such as social security or child support) Excessive and unusual documented medical expenses paid out of pocket There might be other circumstances which, while affecting your family’s financial circumstances, may not qualify as unusual for the pu”
### `c4dcb0c191d59d9c` Berry College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.berry.edu/scholarships-and-aid/maintaining-aid (sha256 e29f5dcb5889)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “This discretion is used to address limited special or unusual circumstances, contingent upon adequate documentation provided by the student applicant.”
### `c69b4e9c734a84d1` Berry College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.berry.edu/scholarships-and-aid/maintaining-aid (sha256 e29f5dcb5889)
- issues: semantic_review_required, conflicting_sources:https://www.berry.edu/scholarships-and-aid/faq
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Professional Judgment Financial aid administrators may use the authority dispensed by the Higher Education Act of 1965, as amended, to exercise professional judgment on a case-by case basis to adjust data items required to calculate a student applicant’s financial need.”
  - sentence: professional_judgment ⟵ “A financial aid counselor may assess the impact of these circumstances on your eligibility for financial aid and provide guidance on the professional judgment process when applicable.”
  - sentence: professional_judgment ⟵ “Following a review of all requested information, students can expect a resolution and adjustment to their financial aid based on professional judgment within two weeks.”
### `1fb402ec6a2169f9` Berry College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.berry.edu/scholarships-and-aid/cost-of-attendance (sha256 ec4dde804b59)
- issues: ambiguous_year_labels, components_do_not_reconcile
- checks: {"columns": 3, "components_reconcile": false, "rows": 11}
  - on_campus:Tuition: 44190 ⟵ “Tuition | $44,190 | $44,190 | $44,190”
  - on_campus:Technology Fee: 150 ⟵ “Technology Fee | $150 | $150 | $150”
  - on_campus:Activity Fee: 225 ⟵ “Activity Fee | $225 | $225 | $225”
  - on_campus:Orientation Fee: 200 ⟵ “Orientation Fee | $200 | $200 | $200”
  - on_campus:Living Expenses: Housing: 8120 ⟵ “Living Expenses: Housing | $8,120 |  | ”
  - on_campus:Living Expenses: Food: 6860 ⟵ “Living Expenses: Food | $6,860 | $1,180 | $1,180”
  - on_campus:Books, Course Materials, Supplies and Equipment: 1000 ⟵ “Books, Course Materials, Supplies and Equipment | $1,000 | $1,000 | $1,000”
  - on_campus:Personal Expenses: 1154 ⟵ “Personal Expenses | $1,154 | $1,154 | $1,154”
  - on_campus:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,980 | $1,980”
  - on_campus:Federal Loan Disbursement Fees: 70 ⟵ “Federal Loan Disbursement Fees | $70 | $70 | $70”
  - on_campus:2026-27 Total Estimated COA: 62769 ⟵ “2026-27 Total Estimated COA | $62,769 | $58,509 | $53,963”
  - off_campus_not_with_family:Tuition: 44190 ⟵ “Tuition | $44,190 | $44,190 | $44,190”
  - off_campus_not_with_family:Technology Fee: 150 ⟵ “Technology Fee | $150 | $150 | $150”
  - off_campus_not_with_family:Activity Fee: 225 ⟵ “Activity Fee | $225 | $225 | $225”
  - off_campus_not_with_family:Orientation Fee: 200 ⟵ “Orientation Fee | $200 | $200 | $200”
  - off_campus_not_with_family:Living Expenses: Food: 1180 ⟵ “Living Expenses: Food | $6,860 | $1,180 | $1,180”
  - off_campus_not_with_family:Housing: 6818 ⟵ “Housing |  | $6,818 | $2,272”
  - off_campus_not_with_family:Food: 2922 ⟵ “Food |  | $2,922 | $2,922”
  - off_campus_not_with_family:Books, Course Materials, Supplies and Equipment: 1000 ⟵ “Books, Course Materials, Supplies and Equipment | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:Personal Expenses: 1154 ⟵ “Personal Expenses | $1,154 | $1,154 | $1,154”
  - off_campus_not_with_family:Transportation: 1980 ⟵ “Transportation | $1,000 | $1,980 | $1,980”
  - off_campus_not_with_family:Federal Loan Disbursement Fees: 70 ⟵ “Federal Loan Disbursement Fees | $70 | $70 | $70”
  - off_campus_not_with_family:2026-27 Total Estimated COA: 58509 ⟵ “2026-27 Total Estimated COA | $62,769 | $58,509 | $53,963”
  - with_parents_or_family:Tuition: 44190 ⟵ “Tuition | $44,190 | $44,190 | $44,190”
  - with_parents_or_family:Technology Fee: 150 ⟵ “Technology Fee | $150 | $150 | $150”
  - … 10 more rows
### `bc9b8243e4cf08cc` Beulah Heights University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://beulah.edu/admissions/financial-aid-scholarships/ (sha256 92a5bafba8a9)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: professional_judgment ⟵ “Professional Judgement Professional Judgment refers to the authority of a school’s financial aid administrator to adjust, on a case-by-case basis with adequate documentation, elements on the Free Application for Federal Student Aid (FAFSA®) form.”
  - sentence: professional_judgment ⟵ “When some unusual situations or circumstances impact your federal student aid eligibility, federal regulations give a financial aid administrator discretion or professional judgment on a case-by-case basis and with adequate documentation to make adjustments to the data elements on the Free Application for Federal Student Aid (FAFSA®) form that impact your Student Aid Index (SAI), to gain a more ac”
  - sentence: professional_judgment ⟵ “The Department of Education does not have the authority to override a school's professional judgment decision.”
  - sentence: professional_judgment ⟵ “The financial aid administrator can exercise professional judgment in determining a student’s need for federal student financial aid.”
  - sentence: professional_judgment ⟵ “The FAFSA Simplification Act distinguishes between different categories of professional judgment by amending section 479A of the HEA.”
  - sentence: professional_judgment ⟵ “Please refer to the university's Financial Aid Policy to learn more about professional judgment.”
### `d7f3e2399f9a326c` Beulah Heights University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://beulah.edu/admissions/financial-aid-scholarships/ (sha256 92a5bafba8a9)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “The office can make necessary adjustments to the student’s cost of attendance of the values of the data items required to calculate the expected student or parent contribution (or both) to allow for the treatment of an individual eligible applicant with special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an aid administrator adjusting data elements in the COA or the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator adjusting a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
### `d9aa30245e80524e` Brenau University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.brenau.edu/admissions/financial-aid/satisfactory-academic-progress/ (sha256 0b8eabcc6c53)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Financial Aid Probation is the status assigned to a student who failed to make satisfactory academic progress, but submitted a qualifying appeal, and had eligibility for financial aid reinstated.”
  - sentence: sap_appeal ⟵ “In the event it will be mathematically impossible for a student who submitted a qualifying SAP appeal to meet SAP standards in one semester, they may be required to adhere to an Academic Plan designed to ensure SAP compliance by a specific point in time.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress (SAP) Appeal Form and a typewritten explanation of the extenuating circumstance(s) must be submitted to the Financial Aid Office within 14 days of being notified of the Financial Aid Suspension status.”
  - sentence: sap_appeal ⟵ “In addition to the SAP Appeal Form, a typewritten financial aid appeal MUST include these two components: An explanation of the extenuating circumstances that resulted in the student’s failure to make SAP.”
### `8848fa922dedc395` Brenau University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.brenau.edu/admissions/financial-aid/promise/ (sha256 63c9ef93b592)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Total aid before Brenau Promise: 35492 ⟵ “Total aid before Brenau Promise | $35,492”
  - column:Tuition and I&I Development fee: 31775 ⟵ “Tuition and I&I Development fee | $31,775”
  - column:Extra funds: 3717 ⟵ “Extra funds | $3,717”
  - column:Brenau Promise aid: 0 ⟵ “Brenau Promise aid | $0”
### `b3cddc86e1c6e569` Brewton-Parker College — appeals 2026-27 [new] (source_unlabeled)
- source: https://bpc.edu/admissions-aid/finances/financial-aid-2/satisfactory-academic-progress/ (sha256 15476587ecaa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Suspension Appeal Process A student may appeal a financial aid suspension by filing an appeal with the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “Any student who loses financial aid eligibility may appeal the decision by following the “SAP Suspension Appeal Process” described below, or by attending school, using their own resources, until the cumulative GPA prescribed for the student’s grade level has been achieved.”
  - sentence: sap_appeal ⟵ “Any student who loses financial aid eligibility may appeal the decision by following the “SAP Suspension Appeal Process” described below, or by attending school, using their own resources, until the 70 percent pace has been achieved.”
### `e2b333852e5e7b30` Brewton-Parker College — appeals 2026-27 [new] (source_unlabeled)
- source: https://bpc.edu/admissions-aid/finances/financial-aid-2/ (sha256 bcf185ce3a0b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “To discuss a cost of attendance adjustment, connect with us by completing the Request to Meet with a Financial Aid Team Member Form Please note that an approved COA adjustment may not result in additional financial aid due to program fund limits and the availability of funds.”
### `cb8ad2e74c637912` Brewton-Parker College — credit_policies 2019-20 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://bpc.edu/degree-programs/dual-enrollment-2/ (sha256 35fab4ddccc6)
- issues: stale_year_label:2019-20
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “High School Transcript with a GPA of 2.5 or higher”
### `71a2c287e59c0d7e` Central Georgia Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.centralgatech.edu/wp-content/uploads/pdfs/admissions/highschool/DE_SAP_Appeal.pdf (sha256 00039fcd299d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS (SAP) APPEAL FORM Student Information Last Name First Name Middle Student ID Number (or Social Security Number) Phone Number Email Address Which semester do you plan to return to CGTC:  Fall 20____  Spring 20____  Summer 20____ Appeal Information You must meet each of the following requirements in order for your appeal to be considered by the SAP Appeals Committee”
  - sentence: sap_appeal ⟵ “All other students should use the Financial Aid Forms portal to file a SAP appeal.”
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS (SAP) APPEAL FORM (continued) Circumstances (Continued) Please provide a statement describing the circumstances that caused you to fall below the minimum SAP standards.”
### `aabd9e4c46d2737c` Central Georgia Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.centralgatech.edu/wp-content/uploads/pdfs/admissions/highschool/DE_SAP_Appeal.pdf (sha256 00039fcd299d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “I certify that documents submitted with this form are true, complete, and have not been altered. ______ __ Student’s Signature Date Revised 02/06/2024 As set forth in its student catalog, Central Georgia Technical College does not discriminate on the basis of race, color, creed, national or ethnic origin, gender, religion, disability, age, political affiliation or belief, genetic information, vete”
### `377a994b1c6cafa2` Chattahoochee Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chattahoocheetech.edu/financial-aid-office/satisfactory-academic-progress-appeal.html (sha256 43f638abdc8f)
- issues: semantic_review_required, conflicting_sources:https://www.chattahoocheetech.edu/financial-aid-office/docs/sap-policy.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Appeal Form Maximum Time Frame (MTF) Only: please fill out this MTF SAP Appeal Form in addition to your appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeal Tips Appeal Statement Tips for Maximum Time frame: This statement should explain in a detailed timeline what extenuating circumstances beyond the student’s control happened to cause them to have accrued the amount of attempted credit hours that caused the student to exceed the maximum time frame.”
### `a4c13e9c6f958620` Chattahoochee Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.chattahoocheetech.edu/financial-aid-office/docs/sap-policy.pdf (sha256 9437e9778bbf)
- issues: semantic_review_required, conflicting_sources:https://www.chattahoocheetech.edu/financial-aid-office/satisfactory-academic-progress-appeal.html
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Appeals: Any student on SAP suspension may appeal to the Financial Aid Appeals Committee.”
  - sentence: sap_appeal ⟵ “Effective Semester SAP Students Can Regain Financial Aid Eligibility: If otherwise eligible, a student may be awarded financial aid for the semester in which the student regained SAP or for which an appeal was approved.”
  - sentence: sap_appeal ⟵ “Deadlines: The deadline for submitting an appeal will be noted on the Satisfactory Academic Progress section of the website.”
  - sentence: sap_appeal ⟵ “SAP Appeals are reviewed by the Financial Aid Appeals Committee and the decision of the committee is final.”
  - sentence: sap_appeal ⟵ “Decisions are sent ~3-4 business days after the appeals deadline and will come from faac@chattahoocheetech.edu. *Financial Aid may be reinstated more than once, however, SAP Appeals submitted after an approval must be submitted with a new extenuating circumstance than the one submitted with the previous approved appeal.”
### `a4d3317bb8069e2b` Chattahoochee Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chattahoocheetech.edu/financial-aid-office/professional-judgement.html (sha256 2d319cd5a447)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Federal regulations permit the College to override a student’s dependency status for Federal Financial Aid purposes if unusual circumstances exist and can be documented.”
  - sentence: need_based_special_circumstances ⟵ “The following conditions are NOT considered unusual circumstances: Parents refusal to contribute to the student’s education Parents are unwilling to provide information for the FAFSA or verification Parents do not claim the student as a dependent for income tax purposes Student demonstrates total self-sufficiency Student does not communicate with parents If you have an unusual or extenuating circu”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal Chattahoochee Technical College recognizes that changes may be experienced in the financial situation of a household.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeals are made based on a change of income that is beyond your control.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances that warrant an appeal may include the following: Separation or Divorce Loss or reduction of employment (those due to cause or personal choice are not applicable) Death of parent or spouse Child Support change Complete and submit the Special Circumstance Appeal form, along with all required supporting documents to the FA Special Circumstance Appeal Submission Form”
  - sentence: need_based_special_circumstances ⟵ “All financial documents used for the current year’s FAFSA and the financial documents for the change in income year will be needed.”
### `a651af1309db9675` Chattahoochee Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chattahoocheetech.edu/financial-aid-office/professional-judgement.html (sha256 2d319cd5a447)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Financial Aid Administrators are authorized to use professional judgment on a case-by-case basis for students with special circumstances that affect a family’s ability to pay for college education that are not reflected in the information provided on the FAFSA.”
  - sentence: professional_judgment ⟵ “In many cases, professional judgment adjustments made to the FAFSA do not result in significant changes to the Student Aid Index (SAI).”
### `c90ef035b67d44a7` Chattahoochee Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chattahoocheetech.edu/financial-aid-office/professional-judgement.html (sha256 2d319cd5a447)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Not all requests will qualify for a Dependency Override.”
  - sentence: dependency_override ⟵ “A Dependency Override request can take up to 5 business days to process once all required documentation is provided.”
### `e27a7895a585e7d0` Clark Atlanta University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cau.edu/admissions/undergraduate-admissions/new-student-information/external-scholarships (sha256 31c88976fd04)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Dates of when supporting documentation i.e., special circumstances letter (for need based or emergency scholarships) and/or when additional supporting documentation was submitted.”
  - sentence: need_based_special_circumstances ⟵ “Follow up should include a thank you card or note thanking the coordinator for reviewing your application, introductory video (business casual attire), special circumstance letter, phone and email follow up to check status.”
  - sentence: need_based_special_circumstances ⟵ “Keep a copy of essays, headshots (business casual attire), transcripts, tests score (SAT/ACT), resumes, letters of recommendation and special circumstances letters in an electronic and hard copy files.”
### `30f99834c36667c1` Clark Atlanta University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cau.edu/admissions/tuition-aid-scholarships/tuition-and-fees (sha256 bf3d3b95d766)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.cau.edu/sites/default/files/2026-07/Undergraduate%20Fee%20Sheet%202026-2027%20Updated%203.26.26%20Final.pdf
- checks: {"columns": 3, "rows": 12}
  - column:Tuition (12–18 hours): 13981 ⟵ “Tuition (12–18 hours) | $13,981 | $13,981 | $27,962”
  - column:Library Assessment: 418 ⟵ “Library Assessment | $418 | $418 | $836”
  - column:Athletic Fee: 94 ⟵ “Athletic Fee | $94 | $94 | $188”
  - column:Student Center Fee: 134 ⟵ “Student Center Fee | $134 | $134 | $268”
  - column:Technology Fee: 225 ⟵ “Technology Fee | $225 | $225 | $450”
  - column:Health Center Fee: 200 ⟵ “Health Center Fee | $200 | $200 | $400”
  - column:Student Activity Fee: 230 ⟵ “Student Activity Fee | $230 | $230 | $460”
  - column:Sustainability Fee: 18 ⟵ “Sustainability Fee | $18 | $18 | $36”
  - column:IncludED Book Fee: 470 ⟵ “IncludED Book Fee | $470 | $470 | $940”
  - column:Total (without insurance): 15770 ⟵ “Total (without insurance) | $15,770 | $15,770 | $31,540”
  - column:Student Insurance**: 547 ⟵ “Student Insurance** | $547 | $771 | $1,318”
  - column:Total (with insurance): 16317 ⟵ “Total (with insurance) | $16,317 | $16,541 | $32,858”
  - column:Tuition (12–18 hours): 13981 ⟵ “Tuition (12–18 hours) | $13,981 | $13,981 | $27,962”
  - column:Library Assessment: 418 ⟵ “Library Assessment | $418 | $418 | $836”
  - column:Athletic Fee: 94 ⟵ “Athletic Fee | $94 | $94 | $188”
  - column:Student Center Fee: 134 ⟵ “Student Center Fee | $134 | $134 | $268”
  - column:Technology Fee: 225 ⟵ “Technology Fee | $225 | $225 | $450”
  - column:Health Center Fee: 200 ⟵ “Health Center Fee | $200 | $200 | $400”
  - column:Student Activity Fee: 230 ⟵ “Student Activity Fee | $230 | $230 | $460”
  - column:Sustainability Fee: 18 ⟵ “Sustainability Fee | $18 | $18 | $36”
  - column:IncludED Book Fee: 470 ⟵ “IncludED Book Fee | $470 | $470 | $940”
  - column:Total (without insurance): 15770 ⟵ “Total (without insurance) | $15,770 | $15,770 | $31,540”
  - column:Student Insurance**: 771 ⟵ “Student Insurance** | $547 | $771 | $1,318”
  - column:Total (with insurance): 16541 ⟵ “Total (with insurance) | $16,317 | $16,541 | $32,858”
  - column:Tuition (12–18 hours): 27962 ⟵ “Tuition (12–18 hours) | $13,981 | $13,981 | $27,962”
  - … 11 more rows
### `cf20e31438831cab` Clark Atlanta University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cau.edu/sites/default/files/2026-07/Undergraduate%20Fee%20Sheet%202026-2027%20Updated%203.26.26%20Final.pdf (sha256 1ad3b3732735)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.cau.edu/admissions/tuition-aid-scholarships/tuition-and-fees
- checks: {"columns": 3, "rows": 23}
  - column:Tuition 12-18 hours: 13981 ⟵ “Tuition 12-18 hours | $13,981 | $13,981 | $27,962”
  - column:Library Assessment: 418 ⟵ “Library Assessment | $418 | $418 | $836”
  - column:Athletic Fee: 94 ⟵ “Athletic Fee | $94 | $94 | $188”
  - column:Student Center Fee: 134 ⟵ “Student Center Fee | $134 | $134 | $268”
  - column:Technology Fee: 225 ⟵ “Technology Fee | $225 | $225 | $450”
  - column:Student Health Fee: 200 ⟵ “Student Health Fee | $200 | $200 | $400”
  - column:Student Activity Fee: 230 ⟵ “Student Activity Fee | $230 | $230 | $460”
  - column:Sustainability Fee: 18 ⟵ “Sustainability Fee | $18 | $18 | $36”
  - column:IncludED Book Fee: 470 ⟵ “IncludED Book Fee | $470 | $470 | $940”
  - column:Total w/o insurance: 15770 ⟵ “Total w/o insurance | $15,770 | $15,770 | $31,540”
  - column:Student Insurance ***: 547 ⟵ “Student Insurance *** | $547 | $771 | $1,318”
  - column:Total with insurance: 16317 ⟵ “Total with insurance | $16,317 | $16,541 | $32,858”
  - column:Pfeiffer, Holmes Hall: 4164 ⟵ “Pfeiffer, Holmes Hall | $ 4,164 | $8,328 | Double Room”
  - column:Beckwith Hall: 2471 ⟵ “Beckwith Hall | $2,471 | $4,942 | 10 Meals per week + $250 dining bucks”
  - column:$4,758: 9516 ⟵ “$4,758 | $9,516 | Single Room”
  - column:Silver 3: 1088 ⟵ “Silver 3 | $1,088 | $2,176 | 60 Meals per semester + $150 dining bucks”
  - column:Brawley Hall: 5045 ⟵ “Brawley Hall | $ 5,045 | $10,090 | Single Room”
  - column:$714: 1428 ⟵ “$714 | $1,428”
  - column:The Suites*: 5336 ⟵ “The Suites* | $ 5,336 | $10,672 | Single Room”
  - column:Dining Bucks 250: 250 ⟵ “Dining Bucks 250 | $250 | $500 | $250 dining bucks”
  - column:The Suites*: 4972 ⟵ “The Suites* | $ 4,972 | $9,944 | Double Room”
  - column:Dining Bucks 100: 100 ⟵ “Dining Bucks 100 | $100 | $200”
  - column:Heritage Commons*: 6096 ⟵ “Heritage Commons* | $ 6,096 | $12,192 | Four Bedroom | $100 dining bucks”
  - column:Heritage Commons*: 7844 ⟵ “Heritage Commons* | $ 7,844 | $15,688 | Two Bedroom”
  - column:**Yugo: 7144 ⟵ “**Yugo | $ 7,144 | $14,288 | All Units”
  - … 37 more rows
### `aea0d0f267d070d9` Clayton  State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clayton.edu/financial-aid/sap.php (sha256 5a5ff3611ea4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “SAP Appeals -- Students who lose their financial aid eligibility may appeal based on mitigating circumstances.”
  - sentence: sap_appeal ⟵ “PROBATION Status -- Students who lose financial aid eligibility and have an SAP Appeal approved are placed on financial aid PROBATION.”
  - sentence: sap_appeal ⟵ “Students in this status may continue to receive aid for one semester or for the amount of time designated in the financial aid academic plan outlined in the SAP Appeal Agreement.”
  - sentence: sap_appeal ⟵ “Failure to meet any part of the academic plan outlined in the SAP Appeal Agreement will result in the appeal being rescinded and the immediate loss of financial aid eligibility.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process All Satisfactory Academic Progress appeals must be submitted electronically via Student Forms.”
  - sentence: sap_appeal ⟵ “Meeting this deadline does not guarantee that funds will be available, only that a decision will be made by the fee payment deadline.) PLEASE NOTE: SAP Appeals will be reviewed once monthly after the Final Fee Payment Deadline.”
### `m8c9bd5b1445b2ce` Clayton  State University — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.clayton.edu/admissions/undergrad/dual-enrollment (sha256 4229a31042a7)
- issues: stale_year_label:2024-25
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “grades, who have a core high school GPA of 3.0 or higher, to submit ACT or SAT scores”
  - eligibility_tier: 3.0 ⟵ “Summer 2027, students in the 11th and 12th grades with a core high school GPA of 3.0”
  - eligibility_tier: 3.0 ⟵ “grades, who have a core high school GPA of 3.0 or higher, to submit ACT or SAT scores”
  - eligibility_tier: 3.0 ⟵ “Summer 2027, students in the 11th and 12th grades with a core high school GPA of 3.0”
  - eligibility_tier: 3.0 ⟵ “grades, who have a core high school GPA of 3.0 or higher, to submit ACT or SAT scores”
  - eligibility_tier: 3.0 ⟵ “Summer 2027, students in the 11th and 12th grades with a core high school GPA of 3.0”
### `26ec3c9a545eab9d` College of Coastal Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.ccga.edu/policies/regulations (sha256 8c98715c311a)
- issues: semantic_review_required, conflicting_sources:https://www.ccga.edu/admissions/financialaid/,https://www.ccga.edu/admissions/financialaid/financial-aid-terms/,https://www.ccga.edu/admissions/financialaid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Note that a student cannot appeal the professional judgment of the faculty member and, in all cases, the policy in the course syllabus shall prevail in determining the grade.”
### `44f0f9e5878446c1` College of Coastal Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ccga.edu/admissions/financialaid/satisfactory-academic-progress/ (sha256 f649b62d0dfe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Note: Students who leave the College of Coastal Georgia and are not making Satisfactory Academic Progress will continue to be not making Satisfactory Academic Progress until either they appeal to have their aid reinstated or pay for their classes out of pocket to get back into good standing.”
  - sentence: sap_appeal ⟵ “Once the student’s academic standing is upgraded from suspension, the student may file a Satisfactory Academic Progress Appeal, if they meet the requirements established by the Satisfactory Academic Progress Policy.”
### `5cf7615302fa1718` College of Coastal Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ccga.edu/admissions/financialaid/special-circumstances/ (sha256 02cb10245cf4)
- issues: semantic_review_required, conflicting_sources:https://www.ccga.edu/admissions/financialaid/,https://www.ccga.edu/admissions/financialaid/financial-aid-terms/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Dependency Override This Special Circumstance is designed to assist dependent students who have documentable situations to support them being without parents.”
  - sentence: need_based_special_circumstances ⟵ “Should a student feel they would like to be considered for a “Special Circumstance,” they should contact their financial aid counselor.”
### `948ca88b78b0666b` College of Coastal Georgia — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ccga.edu/admissions/financialaid/ (sha256 b3d3473b5016)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Review your award offer For entering freshmen, the College beings to mail out award letters for the next academic year on May 1.”
### `9bbc9df9dba99ea9` College of Coastal Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ccga.edu/admissions/financialaid/financial-aid-terms/ (sha256 afde47e1a966)
- issues: semantic_review_required, conflicting_sources:https://www.ccga.edu/admissions/financialaid/,https://www.ccga.edu/admissions/financialaid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Forbearances are granted at the lender’s discretion, usually in cases of extreme financial hardship or other unusual circumstances when the borrower does not qualify for a deferment.”
### `cbea80dc50ae4052` College of Coastal Georgia — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ccga.edu/admissions/financialaid/ (sha256 b3d3473b5016)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.ccga.edu/admissions/financialaid/financial-aid-terms/,https://www.ccga.edu/admissions/financialaid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Forbearances are granted at the lender’s discretion, usually in cases of extreme financial hardship or other unusual circumstances when the borrower does not qualify for a deferment.”
### `d3e26d04e3ddcc5c` College of Coastal Georgia — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ccga.edu/admissions/financialaid/ (sha256 b3d3473b5016)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://catalog.ccga.edu/policies/regulations,https://www.ccga.edu/admissions/financialaid/financial-aid-terms/,https://www.ccga.edu/admissions/financialaid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgement For need-based federal aid programs, the financial aid administrator can adjust the EFC, adjust the COA, or change the dependency status (with documentation) when extenuating circumstances exist.”
  - sentence: professional_judgment ⟵ “This delegation of authority from the federal government to the financial aid administrator is called Professional Judgment (PJ).”
### `daeed8ca63869911` College of Coastal Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ccga.edu/admissions/financialaid/special-circumstances/ (sha256 02cb10245cf4)
- issues: semantic_review_required, conflicting_sources:https://catalog.ccga.edu/policies/regulations,https://www.ccga.edu/admissions/financialaid/,https://www.ccga.edu/admissions/financialaid/financial-aid-terms/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “These adjustments are known as either “Special Circumstances” or “Professional Judgement,” and are considered on a case-by-case basis based on supporting documentation of the circumstances.”
### `e99e1e86fb4cdf5e` College of Coastal Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ccga.edu/admissions/financialaid/financial-aid-terms/ (sha256 afde47e1a966)
- issues: semantic_review_required, conflicting_sources:https://catalog.ccga.edu/policies/regulations,https://www.ccga.edu/admissions/financialaid/,https://www.ccga.edu/admissions/financialaid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment (PJ) For need-based federal aid programs, the financial aid administrator can adjust the EFC, adjust the COA, or change the dependency status (with documentation) when extenuating circumstances exist.”
  - sentence: professional_judgment ⟵ “This delegation of authority from the federal government to the financial aid administrator is called Professional Judgment (PJ).”
### `ede093b636afaaae` College of Coastal Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ccga.edu/admissions/financialaid/special-circumstances/ (sha256 02cb10245cf4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Examples of these situations include the following: Cases of parental abuse Parental neglect Parental abandonment Parental incarceration A Dependency Override cannot be considered for a parent’s refusal to provide information on the FAFSA.”
  - sentence: dependency_override ⟵ “In addition, a student that is under 24 but is self-sufficient is not a case for a Dependency Override.”
### `19e640e712e052df` College of Coastal Georgia — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ccga.edu/admissions/waivers/ (sha256 da080add85d6)
- issues: conflicting_sources:https://www.ccga.edu/wp-content/uploads/2026/06/2026-2027-Tuition-and-Fees.xlsx
- checks: {"columns": 1, "rows": 9}
  - column:Tuition cost for 15 hours: 6525.0 ⟵ “Tuition cost for 15 hours | $1,650.00 | $6,525.00 | $6,720.00”
  - column:Technology Fee: 60.0 ⟵ “Technology Fee | $60.00 | $60.00 | $60.00”
  - column:Student Activity Fee: 60.0 ⟵ “Student Activity Fee | $60.00 | $60.00 | $60.00”
  - column:Athletics Fee: 195.0 ⟵ “Athletics Fee | $195.00 | $195.00 | $195.00”
  - column:Campus Center Fee: 145.0 ⟵ “Campus Center Fee | $145.00 | $145.00 | $145.00”
  - column:Access Card Fee: 15.0 ⟵ “Access Card Fee | $15.00 | $15.00 | $15.00”
  - column:Recreation & Intramural Fee: 25.0 ⟵ “Recreation & Intramural Fee | $25.00 | $25.00 | $25.00”
  - column:Tuition & Fees Per Semester: 7025.0 ⟵ “Tuition & Fees Per Semester | $2,150.00 | $7,025.00 | $7,220.00”
  - column:Tuition & Fees Per Year:: 14050.0 ⟵ “Tuition & Fees Per Year: | $4,300.00 | $14,050.00 | $14,440.00”
### `4115decd19a70588` College of Coastal Georgia — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ccga.edu/admissions/waivers/ (sha256 da080add85d6)
- issues: arrangement_unlabeled, conflicting_sources:https://www.ccga.edu/wp-content/uploads/2026/06/2026-2027-Tuition-and-Fees.xlsx
- checks: {"columns": 2, "rows": 9}
  - column:Tuition cost for 15 hours: 1650.0 ⟵ “Tuition cost for 15 hours | $1,650.00 | $6,525.00 | $6,720.00”
  - column:Technology Fee: 60.0 ⟵ “Technology Fee | $60.00 | $60.00 | $60.00”
  - column:Student Activity Fee: 60.0 ⟵ “Student Activity Fee | $60.00 | $60.00 | $60.00”
  - column:Athletics Fee: 195.0 ⟵ “Athletics Fee | $195.00 | $195.00 | $195.00”
  - column:Campus Center Fee: 145.0 ⟵ “Campus Center Fee | $145.00 | $145.00 | $145.00”
  - column:Access Card Fee: 15.0 ⟵ “Access Card Fee | $15.00 | $15.00 | $15.00”
  - column:Recreation & Intramural Fee: 25.0 ⟵ “Recreation & Intramural Fee | $25.00 | $25.00 | $25.00”
  - column:Tuition & Fees Per Semester: 2150.0 ⟵ “Tuition & Fees Per Semester | $2,150.00 | $7,025.00 | $7,220.00”
  - column:Tuition & Fees Per Year:: 4300.0 ⟵ “Tuition & Fees Per Year: | $4,300.00 | $14,050.00 | $14,440.00”
  - column:Tuition cost for 15 hours: 6720.0 ⟵ “Tuition cost for 15 hours | $1,650.00 | $6,525.00 | $6,720.00”
  - column:Technology Fee: 60.0 ⟵ “Technology Fee | $60.00 | $60.00 | $60.00”
  - column:Student Activity Fee: 60.0 ⟵ “Student Activity Fee | $60.00 | $60.00 | $60.00”
  - column:Athletics Fee: 195.0 ⟵ “Athletics Fee | $195.00 | $195.00 | $195.00”
  - column:Campus Center Fee: 145.0 ⟵ “Campus Center Fee | $145.00 | $145.00 | $145.00”
  - column:Access Card Fee: 15.0 ⟵ “Access Card Fee | $15.00 | $15.00 | $15.00”
  - column:Recreation & Intramural Fee: 25.0 ⟵ “Recreation & Intramural Fee | $25.00 | $25.00 | $25.00”
  - column:Tuition & Fees Per Semester: 7220.0 ⟵ “Tuition & Fees Per Semester | $2,150.00 | $7,025.00 | $7,220.00”
  - column:Tuition & Fees Per Year:: 14440.0 ⟵ “Tuition & Fees Per Year: | $4,300.00 | $14,050.00 | $14,440.00”
### `7571d93c6c718f91` College of Coastal Georgia — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ccga.edu/wp-content/uploads/2026/06/2026-2027-Tuition-and-Fees.xlsx (sha256 ed5ca2dc43df)
- issues: arrangement_unlabeled, components_do_not_reconcile, implausible_amount, conflicting_sources:https://www.ccga.edu/admissions/waivers/
- checks: {"columns": 15, "components_reconcile": false, "rows": 11}
  - column:Semester Credit Hr.: 1 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - column:Tuition: 110 ⟵ “Tuition | 110 | 220 | 330 | 440 | 550 | 660 | 770 | 880 | 990 | 1100 | 1210 | 1320 | 1430 | 1540 | 1650”
  - column:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - column:Athletic Fee: 97.5 ⟵ “Athletic Fee | 97.5 | 97.5 | 97.5 | 97.5 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195”
  - column:Technology: 60 ⟵ “Technology | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - column:Access Card: 15 ⟵ “Access Card | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15”
  - column:Campus Center: 145 ⟵ “Campus Center | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145”
  - column:Recreational Fee: 25 ⟵ “Recreational Fee | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25”
  - column:Housing*: 3849 ⟵ “Housing* | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849”
  - column:Residential Meal Plan**: 2396 ⟵ “Residential Meal Plan** | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396”
  - column:Total: 6727.5 ⟵ “Total | 6727.5 | 6837.5 | 6947.5 | 7057.5 | 7295 | 7405 | 7515 | 7625 | 7735 | 7845 | 7955 | 8065 | 8175 | 8285 | 8395”
  - column:Semester Credit Hr.: 2 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - column:Tuition: 220 ⟵ “Tuition | 110 | 220 | 330 | 440 | 550 | 660 | 770 | 880 | 990 | 1100 | 1210 | 1320 | 1430 | 1540 | 1650”
  - column:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - column:Athletic Fee: 97.5 ⟵ “Athletic Fee | 97.5 | 97.5 | 97.5 | 97.5 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195”
  - column:Technology: 60 ⟵ “Technology | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - column:Access Card: 15 ⟵ “Access Card | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15”
  - column:Campus Center: 145 ⟵ “Campus Center | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145”
  - column:Recreational Fee: 25 ⟵ “Recreational Fee | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25”
  - column:Housing*: 3849 ⟵ “Housing* | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849”
  - column:Residential Meal Plan**: 2396 ⟵ “Residential Meal Plan** | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396”
  - column:Total: 6837.5 ⟵ “Total | 6727.5 | 6837.5 | 6947.5 | 7057.5 | 7295 | 7405 | 7515 | 7625 | 7735 | 7845 | 7955 | 8065 | 8175 | 8285 | 8395”
  - column:Semester Credit Hr.: 3 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - column:Tuition: 330 ⟵ “Tuition | 110 | 220 | 330 | 440 | 550 | 660 | 770 | 880 | 990 | 1100 | 1210 | 1320 | 1430 | 1540 | 1650”
  - column:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - … 140 more rows
### `81b877a2fe345620` College of Coastal Georgia — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ccga.edu/admissions/financialaid/cost-of-attendance/ (sha256 28687711437d)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 6, "rows": 8}
  - off_campus_not_with_family:Books, Materials, Supplies, Equipment: 1850 ⟵ “Books, Materials, Supplies, Equipment | $1,850 | $1,850 | $1,850 | $1,850 | $1,850 | $1,850”
  - off_campus_not_with_family:Food: 2630 ⟵ “Food | $2,630 | $2,630 | $7,056 | $7,056 | $1,450 | $1,450”
  - off_campus_not_with_family:Fees: 1328 ⟵ “Fees | $1,328 | $1,328 | $1,328 | $1,328 | $1,328 | $1,328”
  - off_campus_not_with_family:Miscellaneous, Personal: 6450 ⟵ “Miscellaneous, Personal | $6,450 | $6,450 | $6,450 | $6,450 | $6,450 | $6,450”
  - off_campus_not_with_family:Housing: 6436 ⟵ “Housing | $6,436 | $6,436 | $7,828 | $7,828 | $3,082 | $3,082”
  - off_campus_not_with_family:Transportation: 1918 ⟵ “Transportation | $1,918 | $1,918 | $1,918 | $1,918 | $1,918 | $1,918”
  - off_campus_not_with_family:Tuition: 3300 ⟵ “Tuition | $3,300 | $13,050 | $3,300 | $13,050 | $3,300 | $13,050”
  - off_campus_not_with_family:Totals: 23912 ⟵ “Totals | $23,912 | $33,662 | $29,730 | $39,480 | $19,378 | $29,128”
  - on_campus:Books, Materials, Supplies, Equipment: 1850 ⟵ “Books, Materials, Supplies, Equipment | $1,850 | $1,850 | $1,850 | $1,850 | $1,850 | $1,850”
  - on_campus:Food: 2630 ⟵ “Food | $2,630 | $2,630 | $7,056 | $7,056 | $1,450 | $1,450”
  - on_campus:Fees: 1328 ⟵ “Fees | $1,328 | $1,328 | $1,328 | $1,328 | $1,328 | $1,328”
  - on_campus:Miscellaneous, Personal: 6450 ⟵ “Miscellaneous, Personal | $6,450 | $6,450 | $6,450 | $6,450 | $6,450 | $6,450”
  - on_campus:Housing: 6436 ⟵ “Housing | $6,436 | $6,436 | $7,828 | $7,828 | $3,082 | $3,082”
  - on_campus:Transportation: 1918 ⟵ “Transportation | $1,918 | $1,918 | $1,918 | $1,918 | $1,918 | $1,918”
  - on_campus:Tuition: 13050 ⟵ “Tuition | $3,300 | $13,050 | $3,300 | $13,050 | $3,300 | $13,050”
  - on_campus:Totals: 33662 ⟵ “Totals | $23,912 | $33,662 | $29,730 | $39,480 | $19,378 | $29,128”
  - with_parents_or_family:Books, Materials, Supplies, Equipment: 1850 ⟵ “Books, Materials, Supplies, Equipment | $1,850 | $1,850 | $1,850 | $1,850 | $1,850 | $1,850”
  - with_parents_or_family:Food: 7056 ⟵ “Food | $2,630 | $2,630 | $7,056 | $7,056 | $1,450 | $1,450”
  - with_parents_or_family:Fees: 1328 ⟵ “Fees | $1,328 | $1,328 | $1,328 | $1,328 | $1,328 | $1,328”
  - with_parents_or_family:Miscellaneous, Personal: 6450 ⟵ “Miscellaneous, Personal | $6,450 | $6,450 | $6,450 | $6,450 | $6,450 | $6,450”
  - with_parents_or_family:Housing: 7828 ⟵ “Housing | $6,436 | $6,436 | $7,828 | $7,828 | $3,082 | $3,082”
  - with_parents_or_family:Transportation: 1918 ⟵ “Transportation | $1,918 | $1,918 | $1,918 | $1,918 | $1,918 | $1,918”
  - with_parents_or_family:Tuition: 3300 ⟵ “Tuition | $3,300 | $13,050 | $3,300 | $13,050 | $3,300 | $13,050”
  - with_parents_or_family:Totals: 29730 ⟵ “Totals | $23,912 | $33,662 | $29,730 | $39,480 | $19,378 | $29,128”
  - column:Books, Materials, Supplies, Equipment: 1850 ⟵ “Books, Materials, Supplies, Equipment | $1,850 | $1,850 | $1,850 | $1,850 | $1,850 | $1,850”
  - … 23 more rows
### `86ac3baf3b5b13c1` College of Coastal Georgia — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ccga.edu/admissions/financialaid/cost-of-attendance/ (sha256 28687711437d)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 6, "rows": 8}
  - off_campus_not_with_family:Books, Materials, Supplies, Equipment: 1850 ⟵ “Books, Materials, Supplies, Equipment | $1,850 | $1,850 | $1,850 | $1,850 | $1,850 | $1,850”
  - off_campus_not_with_family:Food: 2530 ⟵ “Food | $2,530 | $2,530 | $6,888 | $6,888 | $1,310 | $1,310”
  - off_campus_not_with_family:Fees: 1328 ⟵ “Fees | $1,328 | $1,328 | $1,328 | $1,328 | $1,328 | $1,328”
  - off_campus_not_with_family:Miscellaneous, Personal: 5656 ⟵ “Miscellaneous, Personal | $5,656 | $5,656 | $5,656 | $5,656 | $5,656 | $5,656”
  - off_campus_not_with_family:Housing: 6196 ⟵ “Housing | $6,196 | $6,196 | $7,510 | $7,510 | $3,054 | $3,054”
  - off_campus_not_with_family:Transportation: 1778 ⟵ “Transportation | $1,778 | $1,778 | $1,778 | $1,778 | $1,778 | $1,778”
  - off_campus_not_with_family:Tuition: 3270 ⟵ “Tuition | $3,270 | $12,660 | $3,270 | $12,660 | $3,270 | $12,660”
  - off_campus_not_with_family:Totals: 22608 ⟵ “Totals | $22,608 | $31,998 | $28,280 | $37,670 | $18,246 | $27,636”
  - on_campus:Books, Materials, Supplies, Equipment: 1850 ⟵ “Books, Materials, Supplies, Equipment | $1,850 | $1,850 | $1,850 | $1,850 | $1,850 | $1,850”
  - on_campus:Food: 2530 ⟵ “Food | $2,530 | $2,530 | $6,888 | $6,888 | $1,310 | $1,310”
  - on_campus:Fees: 1328 ⟵ “Fees | $1,328 | $1,328 | $1,328 | $1,328 | $1,328 | $1,328”
  - on_campus:Miscellaneous, Personal: 5656 ⟵ “Miscellaneous, Personal | $5,656 | $5,656 | $5,656 | $5,656 | $5,656 | $5,656”
  - on_campus:Housing: 6196 ⟵ “Housing | $6,196 | $6,196 | $7,510 | $7,510 | $3,054 | $3,054”
  - on_campus:Transportation: 1778 ⟵ “Transportation | $1,778 | $1,778 | $1,778 | $1,778 | $1,778 | $1,778”
  - on_campus:Tuition: 12660 ⟵ “Tuition | $3,270 | $12,660 | $3,270 | $12,660 | $3,270 | $12,660”
  - on_campus:Totals: 31998 ⟵ “Totals | $22,608 | $31,998 | $28,280 | $37,670 | $18,246 | $27,636”
  - with_parents_or_family:Books, Materials, Supplies, Equipment: 1850 ⟵ “Books, Materials, Supplies, Equipment | $1,850 | $1,850 | $1,850 | $1,850 | $1,850 | $1,850”
  - with_parents_or_family:Food: 6888 ⟵ “Food | $2,530 | $2,530 | $6,888 | $6,888 | $1,310 | $1,310”
  - with_parents_or_family:Fees: 1328 ⟵ “Fees | $1,328 | $1,328 | $1,328 | $1,328 | $1,328 | $1,328”
  - with_parents_or_family:Miscellaneous, Personal: 5656 ⟵ “Miscellaneous, Personal | $5,656 | $5,656 | $5,656 | $5,656 | $5,656 | $5,656”
  - with_parents_or_family:Housing: 7510 ⟵ “Housing | $6,196 | $6,196 | $7,510 | $7,510 | $3,054 | $3,054”
  - with_parents_or_family:Transportation: 1778 ⟵ “Transportation | $1,778 | $1,778 | $1,778 | $1,778 | $1,778 | $1,778”
  - with_parents_or_family:Tuition: 3270 ⟵ “Tuition | $3,270 | $12,660 | $3,270 | $12,660 | $3,270 | $12,660”
  - with_parents_or_family:Totals: 28280 ⟵ “Totals | $22,608 | $31,998 | $28,280 | $37,670 | $18,246 | $27,636”
  - column:Books, Materials, Supplies, Equipment: 1850 ⟵ “Books, Materials, Supplies, Equipment | $1,850 | $1,850 | $1,850 | $1,850 | $1,850 | $1,850”
  - … 23 more rows
### `99fbf50c7997c76f` College of Coastal Georgia — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ccga.edu/wp-content/uploads/2026/06/2026-2027-Tuition-and-Fees.xlsx (sha256 ed5ca2dc43df)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.ccga.edu/admissions/waivers/
- checks: {"columns": 15, "components_reconcile": false, "rows": 11}
  - column:Semester Credit Hr.: 1 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - column:Tuition: 435 ⟵ “Tuition | 435 | 870 | 1305 | 1740 | 2175 | 2610 | 3045 | 3480 | 3915 | 4350 | 4785 | 5220 | 5655 | 6090 | 6525”
  - column:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - column:Athletic Fee: 97.5 ⟵ “Athletic Fee | 97.5 | 97.5 | 97.5 | 97.5 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195”
  - column:Technology: 60 ⟵ “Technology | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - column:Access Card: 15 ⟵ “Access Card | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15”
  - column:Campus Center: 145 ⟵ “Campus Center | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145”
  - column:Recreational Fee: 25 ⟵ “Recreational Fee | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25”
  - column:Housing*: 3849 ⟵ “Housing* | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849”
  - column:Residential Meal Plan**: 2396 ⟵ “Residential Meal Plan** | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396”
  - column:Total: 7052.5 ⟵ “Total | 7052.5 | 7487.5 | 7922.5 | 8357.5 | 8920 | 9355 | 9790 | 10225 | 10660 | 11095 | 11530 | 11965 | 12400 | 12835 | 13270”
  - column:Semester Credit Hr.: 2 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - column:Tuition: 870 ⟵ “Tuition | 435 | 870 | 1305 | 1740 | 2175 | 2610 | 3045 | 3480 | 3915 | 4350 | 4785 | 5220 | 5655 | 6090 | 6525”
  - column:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - column:Athletic Fee: 97.5 ⟵ “Athletic Fee | 97.5 | 97.5 | 97.5 | 97.5 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195”
  - column:Technology: 60 ⟵ “Technology | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - column:Access Card: 15 ⟵ “Access Card | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15”
  - column:Campus Center: 145 ⟵ “Campus Center | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145”
  - column:Recreational Fee: 25 ⟵ “Recreational Fee | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25”
  - column:Housing*: 3849 ⟵ “Housing* | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849”
  - column:Residential Meal Plan**: 2396 ⟵ “Residential Meal Plan** | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396”
  - column:Total: 7487.5 ⟵ “Total | 7052.5 | 7487.5 | 7922.5 | 8357.5 | 8920 | 9355 | 9790 | 10225 | 10660 | 11095 | 11530 | 11965 | 12400 | 12835 | 13270”
  - column:***100% eCore Pays $500 online Learning Fee: 2330 ⟵ “***100% eCore Pays $500 online Learning Fee | Residential Plan B-15 meals/week +$125 Dining Dollars | 2330”
  - column:****Coastal Online Major pays $280 Coastal Online Fee: 2200 ⟵ “****Coastal Online Major pays $280 Coastal Online Fee | Residential Plan C-10 meals/week+$125 Dining Dollars | 2200”
  - column:Semester Credit Hr.: 3 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - … 144 more rows
### `de412afc8b55e080` Covenant College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.covenant.edu/admissions/costs/faq.html (sha256 6511c41d7f56)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “What if I have special or unusual circumstances?”
  - sentence: need_based_special_circumstances ⟵ “If you think your FAFSA does not reflect your current situation, or you have special or unusual circumstances, such as excessive medical expenses, a change in salary, or private school costs for siblings, please email financialaid@covenant.edu for special consideration.”
### `013d4dd4a292f2e5` Covenant College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.covenant.edu/admissions/costs/tuition-fees.html (sha256 d3834710089d)
- issues: conflicting_sources:https://www.covenant.edu/about/facts.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Books, Course Materials, Supplies & Equipment *: 1170 ⟵ “Books, Course Materials, Supplies & Equipment * | $1,170”
  - column:Fees: 1328 ⟵ “Fees | $1,328”
  - column:Loans fees average 4 yrs *: 80 ⟵ “Loans fees average 4 yrs * | $80”
  - column:Miscellaneous, apparel, personal care: 3132 ⟵ “Miscellaneous, apparel, personal care | $3,132”
  - column:Living expenses - Housing and Food **: 13770 ⟵ “Living expenses - Housing and Food ** | $13,770”
  - column:Transportation ***: 920 ⟵ “Transportation *** | $920”
  - column:Tuition: 44050 ⟵ “Tuition | $44,050”
  - column:Total budget - not actual charges to be assessed: 64450 ⟵ “Total budget - not actual charges to be assessed | $64,450”
### `41dee1b617190ad0` Covenant College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.covenant.edu/admissions/costs/tuition-fees.html (sha256 d3834710089d)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Books, Course Materials, Supplies & Equipment *: 1170 ⟵ “Books, Course Materials, Supplies & Equipment * | $1,170”
  - column:Fees: 1278 ⟵ “Fees | $1,278”
  - column:Loans fees average 4 yrs *: 106 ⟵ “Loans fees average 4 yrs * | $106”
  - column:Miscellaneous, apparel, personal care: 3136 ⟵ “Miscellaneous, apparel, personal care | $3,136”
  - column:Living expenses - Housing and Food **: 13250 ⟵ “Living expenses - Housing and Food ** | $13,250”
  - column:Transportation ***: 920 ⟵ “Transportation *** | $920”
  - column:Tuition: 42390 ⟵ “Tuition | $42,390”
  - column:Total budget - not actual charges to be assessed: 62250 ⟵ “Total budget - not actual charges to be assessed | $62,250”
### `eb0105f22dfa9950` Covenant College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.covenant.edu/about/facts.html (sha256 c58a13f533d4)
- issues: conflicting_sources:https://www.covenant.edu/admissions/costs/tuition-fees.html
- checks: {"columns": 1, "rows": 3}
  - column:Undergraduate Tuition:: 44050 ⟵ “Undergraduate Tuition: | $44,050”
  - column:Room and Board(Average):: 13770 ⟵ “Room and Board(Average): | $13,770”
  - column:Estimated Cost of Attendance(Varies between students):: 64450 ⟵ “Estimated Cost of Attendance(Varies between students): | $64,450”
### `c59194a05b0d0c68` Dalton State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.daltonstate.edu/wp-content/uploads/2024/01/DSCHousingAppeal-renamed.pdf (sha256 48c280287979)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Change in family income: Written narrative form the student explaining how the family’s income situation has changed since the student signed their current Residence Hall Contract.”
### `90955d49ff8b9cde` Dalton State College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.daltonstate.edu/wp-content/uploads/2026/09/Facts-and-Figures-Fall-2025.pdf (sha256 2b7a8744e606)
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "rows": 140}
  - column:First-Time Full-Time Freshmen: 937 ⟵ “First-Time Full-Time Freshmen | 937 | 21.1%”
  - column:All New Students: 1864 ⟵ “All New Students | 1864 | 33.5%”
  - column:First-Time Freshman: 1173 ⟵ “First-Time Freshman | 1173 | 21.1%”
  - column:New Dual Enrollment Students: 488 ⟵ “New Dual Enrollment Students | 488 | 8.8%”
  - column:New Transfers (in all class levels): 243 ⟵ “New Transfers (in all class levels) | 243 | 4.4%”
  - column:Other New Non-Degree-Seeking Students: 10 ⟵ “Other New Non-Degree-Seeking Students | 10 | 0.2%”
  - column:Dual Enrollment Students: 649 ⟵ “Dual Enrollment Students | 649 | 11.7%”
  - column:Freshmen: 1879 ⟵ “Freshmen | 1879 | 33.7%”
  - column:Sophomores: 1188 ⟵ “Sophomores | 1188 | 21.3%”
  - column:Juniors: 794 ⟵ “Juniors | 794 | 14.3%”
  - column:Seniors: 1049 ⟵ “Seniors | 1049 | 18.8%”
  - column:Other Non-Degree-Seeking Students: 11 ⟵ “Other Non-Degree-Seeking Students | 11 | 0.2%”
  - column:Associate Degree Students: 2030 ⟵ “Associate Degree Students | 2030 | 36.4%”
  - column:Bachelor's Degree Students: 2792 ⟵ “Bachelor's Degree Students | 2792 | 50.1%”
  - column:Career Certificate Students: 79 ⟵ “Career Certificate Students | 79 | 1.4%”
  - column:Non-Degree-Seeking Students: 671 ⟵ “Non-Degree-Seeking Students | 671 | 12.0%”
  - column:Minority Students: 2702 ⟵ “Minority Students | 2702 | 48.5%”
  - column:Male: 1968 ⟵ “Male | 1968 | 35.3%”
  - column:Female: 3602 ⟵ “Female | 3602 | 64.7%”
  - column:Full-Time Enrollment: 3043 ⟵ “Full-Time Enrollment | 3043 | 54.6%”
  - column:Age less than 18 years: 575 ⟵ “Age less than 18 years | 575 | 10.3%”
  - column:Age 18-24 years: 4040 ⟵ “Age 18-24 years | 4040 | 72.5%”
  - column:Age 25 years and older: 955 ⟵ “Age 25 years and older | 955 | 17.1%”
  - column:First-Time Full-Time Freshmen Enrolled in Learning Support: 483 ⟵ “First-Time Full-Time Freshmen Enrolled in Learning Support | 483 | 8.7%”
  - column:First Generation Students: 2654 ⟵ “First Generation Students | 2654 | 47.6%”
  - … 353 more rows
### `m031c84cd63e26d8` Dalton State College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: http://catalog.daltonstate.edu/programs/transferrules/ (sha256 7e5e8397411d)
- issues: conflicting_values:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Provided that native and transfer students are treated equally, institutions may impose additional reasonable expectations, such as a grade of “C” or better in Core IMPACTS courses.”
### `9a25fed9b0bed8ca` Emory University — appeals 2025-26 [new] (labeled_in_source)
- source: https://studentaid.emory.edu/undergraduate/manage/special-circumstances.html (sha256 ec2106bad181)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Changes In Your Finances/Special Circumstances If you experience a substantial change in your financial resources – such as loss of employment, natural disaster, death of a parent, extraordinary medical expenses, or unexpected tuition expenses – or experience changes concerning your living conditions that impact your dependency status – such as human trafficking, refugee or asylee status, parental”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance appeal does not automatically ensure your request will be approved.”
  - sentence: need_based_special_circumstances ⟵ “Changes In Your Dependency/Unusual Circumstances If you experience a substantial change in your living conditions that impact your dependency status – such as human trafficking, refugee or asylee status, parental abandonment or incarceration - you can complete and submit a Special Circumstances Appeal Form, along with any supporting documents.”
  - sentence: need_based_special_circumstances ⟵ “How to submit a unusual circumstance appeal Your completed Appeal Packet should be submitted by email, USPS, or fax (fax is the preferred method) and include: A completed Unusual Circumstance Appeal Form Any supporting documents you believe are relevant to explain your situation You may be asked to provide additional information after your initial completed Appeal Packet is submitted.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance appeal does not automatically ensure your request will be approved.”
  - sentence: need_based_special_circumstances ⟵ “What doesn't qualify as an unusual circumstance?”
### `41e4279a955e30e5` Emory University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://studentaid.emory.edu/undergraduate/types/grants-scholarships/tuition-benefit.html (sha256 de4cd2bc1080)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition Benefit: 0 ⟵ “Tuition Benefit | $0”
  - column:Work Study: 2000 ⟵ “Work Study | $2,000”
  - column:Student Loan: 5500 ⟵ “Student Loan | $5,500”
  - column:Need-based Emory University Grant: 35000 ⟵ “Need-based Emory University Grant | $35,000”
  - column:Total Need-based Aid: 42500 ⟵ “Total Need-based Aid | $42,500”
### `a20d0a3b31bce65b` Emory University-Oxford College — appeals 2025-26 [new] (labeled_in_source)
- source: https://studentaid.emory.edu/undergraduate/manage/special-circumstances.html (sha256 ec2106bad181)
- issues: stale_year_label:2025-26, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Changes In Your Finances/Special Circumstances If you experience a substantial change in your financial resources – such as loss of employment, natural disaster, death of a parent, extraordinary medical expenses, or unexpected tuition expenses – or experience changes concerning your living conditions that impact your dependency status – such as human trafficking, refugee or asylee status, parental”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance appeal does not automatically ensure your request will be approved.”
  - sentence: need_based_special_circumstances ⟵ “Changes In Your Dependency/Unusual Circumstances If you experience a substantial change in your living conditions that impact your dependency status – such as human trafficking, refugee or asylee status, parental abandonment or incarceration - you can complete and submit a Special Circumstances Appeal Form, along with any supporting documents.”
  - sentence: need_based_special_circumstances ⟵ “How to submit a unusual circumstance appeal Your completed Appeal Packet should be submitted by email, USPS, or fax (fax is the preferred method) and include: A completed Unusual Circumstance Appeal Form Any supporting documents you believe are relevant to explain your situation You may be asked to provide additional information after your initial completed Appeal Packet is submitted.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a special circumstance appeal does not automatically ensure your request will be approved.”
  - sentence: need_based_special_circumstances ⟵ “What doesn't qualify as an unusual circumstance?”
### `c4184add15fda057` Emory University-Oxford College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://studentaid.emory.edu/undergraduate/types/grants-scholarships/tuition-benefit.html (sha256 de4cd2bc1080)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition Benefit: 0 ⟵ “Tuition Benefit | $0”
  - column:Work Study: 2000 ⟵ “Work Study | $2,000”
  - column:Student Loan: 5500 ⟵ “Student Loan | $5,500”
  - column:Need-based Emory University Grant: 35000 ⟵ “Need-based Emory University Grant | $35,000”
  - column:Total Need-based Aid: 42500 ⟵ “Total Need-based Aid | $42,500”
### `5b3aaee5853e750a` Fort Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fvsu.edu/about-fvsu/professional-judgment (sha256 24f02bcabea6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Fort Valley State University’s Department of Financial Aid allows students to request professional judgment if individuals are experiencing extenuating circumstances that may warrant a reevaluation of financial aid.”
### `6b8cbecc7b5eebfd` Fort Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fvsu.edu/about-fvsu/satisfactory-academic-progress-sap (sha256 b025fc0d4cb8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other special circumstances outside of the student’s control.”
### `863f46580b021b56` Fort Valley State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.fvsu.edu/about-fvsu/office-of-financial-aid (sha256 46f3d3399f03)
- issues: semantic_review_required, conflicting_sources:https://www.fvsu.edu/about-fvsu/satisfactory-academic-progress-sap
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Watch: What responsibilities do I have regarding “Satisfactory Academic Progress?” Watch: Am I eligible to file an appeal?”
  - sentence: sap_appeal ⟵ “Explore more about financial aid appeals and satisfactory academic progress here.”
### `9c1369e144bb6ebb` Fort Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fvsu.edu/about-fvsu/satisfactory-academic-progress-sap (sha256 b025fc0d4cb8)
- issues: semantic_review_required, conflicting_sources:https://www.fvsu.edu/about-fvsu/office-of-financial-aid
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Students appealing Maximum Allowable Time Frame must complete and submit the SAP Appeal Form and Academic Progress Plan form together.”
  - sentence: sap_appeal ⟵ “Phase 4: SAP Appeal Students who are on SAP suspension have a right to appeal their status, if they believe they had an extenuating circumstance, which stopped them from performing well academically.”
  - sentence: sap_appeal ⟵ “To appeal students, must log into their Verify My FAFSA page and complete the following by the SAP appeal due date: SAP Appeal Request Form, being specific about dates and signatures Watch and upload the Key Components to the FA SAP Appeal Process Upload a current Academic Advisement Progress Assessment Plan signed by both you and your advisor SAP appeals received after the deadline will not be re”
  - sentence: sap_appeal ⟵ “Most SAP appeals are reviewed within two weeks of submission.”
  - sentence: sap_appeal ⟵ “Phase 5: SAP Appeal Decision SAP Appeals Approvals Students who have successfully submitted their SAP appeal and receive an approval, must be sure they meet the each of the requirements listed below: Maintain a semester GPA of a 2.5 Do not withdraw from a course without speaking to the Office of Financial Aid first Complete either a free 8-week course, or successfully attend any required academic ”
  - sentence: sap_appeal ⟵ “SAP Appeal Denials Students who successfully submitted their SAP appeal and receive a denial will not have any federal or state financial assistance added to their account.”
### `7a2947f05ae08ce0` Fort Valley State University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fvsu.edu/content/userfiles/files/FVSU_2526_Cost%20of%20Attendances.pdf (sha256 a58b50fe7e84)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 12}
  - on_campus:Tuition 1: 5220 ⟵ “Tuition 1 | $5,220 | $5,220”
  - on_campus:Mandatory Fees: 1380 ⟵ “Mandatory Fees | $1,380 | $1,380”
  - on_campus:Housing2: 6812 ⟵ “Housing2 | $6,812 | $7,668”
  - on_campus:Food: 4728 ⟵ “Food | $4,728 | $4,100”
  - on_campus:Transportation: 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4: 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses: 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - on_campus:Loan Fees 5: 120 ⟵ “Loan Fees 5 | $120 | $120”
  - on_campus:Total Cost of Attendance: 24160 ⟵ “Total Cost of Attendance | $24,160 | $25,738”
  - on_campus:Tuition1: 19800 ⟵ “Tuition1 | $19,800 | $19,800”
  - on_campus:Mandatory Fees: 1380 ⟵ “Mandatory Fees | $1,380 | $1,380”
  - on_campus:Housing2: 6812 ⟵ “Housing2 | $6,812 | $7,668”
  - on_campus:Food3: 4728 ⟵ “Food3 | $4,728 | $4,100”
  - on_campus:Transportation: 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4: 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses: 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - on_campus:Loan Fees5: 120 ⟵ “Loan Fees5 | $120 | $120”
  - on_campus:Total Cost of Attendance: 38740 ⟵ “Total Cost of Attendance | $38,740 | $40,318”
  - on_campus:Tuition1: 20370 ⟵ “Tuition1 | $20,370 | $20,370”
  - on_campus:Mandatory Fees: 1380 ⟵ “Mandatory Fees | $1,380 | $1,380”
  - on_campus:Housing2: 6812 ⟵ “Housing2 | $6,812 | $7,668”
  - on_campus:Food3: 4782 ⟵ “Food3 | $4,782 | $4,100”
  - on_campus:Transportation: 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4: 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses: 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - … 83 more rows
### `a447d9748317a03a` Fort Valley State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fvsu.edu/content/userfiles/files/2026-2027%20COA.pdf (sha256 7776c2c54a06)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 2, "rows": 8}
  - on_campus:Tuition: 5280.0 ⟵ “Tuition | $5,280.00 | $5,280.00”
  - on_campus:Mandatory Fees: 1400.0 ⟵ “Mandatory Fees | $1,400.00 | $1,400.00”
  - on_campus:Housing: 7074.0 ⟵ “Housing | $7,074.00 | $8,858.00”
  - on_campus:Food: 4916.0 ⟵ “Food | $4,916.00 | $4,474.00”
  - on_campus:Transportation: 2880.0 ⟵ “Transportation | $2,880.00 | $5,760.00”
  - on_campus:Books & Supplies: 1400.0 ⟵ “Books & Supplies | $1,400.00 | $1,400.00”
  - on_campus:Miscellaneous Expenses: 3078.0 ⟵ “Miscellaneous Expenses | $3,078.00 | $3,078.00”
  - on_campus:Total Cost of Attendance: 26028.0 ⟵ “Total Cost of Attendance | $26,028.00 | $30,250.00”
  - on_campus:Tuition: 20400.0 ⟵ “Tuition | $20,400.00 | $20,400.00”
  - on_campus:Mandatory Fees: 1400.0 ⟵ “Mandatory Fees | $1,400.00 | $1,400.00”
  - on_campus:Housing: 7074.0 ⟵ “Housing | $7,074.00 | $8,858.00”
  - on_campus:Food: 4916.0 ⟵ “Food | $4,916.00 | $4,474.00”
  - on_campus:Transportation: 2880.0 ⟵ “Transportation | $2,880.00 | $5,760.00”
  - on_campus:Books & Supplies: 1400.0 ⟵ “Books & Supplies | $1,400.00 | $1,400.00”
  - on_campus:Miscellaneous Expenses: 3078.0 ⟵ “Miscellaneous Expenses | $3,078.00 | $3,078.00”
  - on_campus:Total Cost of Attendance: 41148.0 ⟵ “Total Cost of Attendance | $41,148.00 | $45,370.00”
  - on_campus:Tuition: 20970.0 ⟵ “Tuition | $20,970.00 | $20,970.00”
  - on_campus:Mandatory Fees: 1400.0 ⟵ “Mandatory Fees | $1,400.00 | $1,400.00”
  - on_campus:Housing: 7074.0 ⟵ “Housing | $7,074.00 | $8,858.00”
  - on_campus:Food: 4916.0 ⟵ “Food | $4,916.00 | $4,474.00”
  - on_campus:Transportation: 2880.0 ⟵ “Transportation | $2,880.00 | $5,760.00”
  - on_campus:Books & Supplies: 1400.0 ⟵ “Books & Supplies | $1,400.00 | $1,400.00”
  - on_campus:Miscellaneous Expenses: 3078.0 ⟵ “Miscellaneous Expenses | $3,078.00 | $3,078.00”
  - on_campus:Total Cost of Attendance: 41718.0 ⟵ “Total Cost of Attendance | $41,718.00 | $45,940.00”
  - on_campus:Tuition: 4872.0 ⟵ “Tuition | $4,872.00 | $4,872.00”
  - … 71 more rows
### `e3ce5f51cb965f9d` Fort Valley State University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fvsu.edu/content/userfiles/files/FVSU_2425_Cost%20of%20Attendances(2).pdf (sha256 cf163cf07d66)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2024-25, conflicting_sources:https://www.fvsu.edu/content/userfiles/files/2024-2025%20Cost%20of%20Attendance.pdf
- checks: {"columns": 2, "rows": 12}
  - on_campus:Tuition 1: 5220 ⟵ “Tuition 1 | $5,220 | $5,220”
  - on_campus:Mandatory Fees: 1350 ⟵ “Mandatory Fees | $1,350 | $1,350”
  - on_campus:Housing2: 6528 ⟵ “Housing2 | $6,528 | $7,668”
  - on_campus:Food: 4582 ⟵ “Food | $4,582 | $4,100”
  - on_campus:Transportation: 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4: 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses: 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - on_campus:Loan Fees 5: 120 ⟵ “Loan Fees 5 | $120 | $120”
  - on_campus:Total Cost of Attendance: 23700 ⟵ “Total Cost of Attendance | $23,700 | $25,708”
  - on_campus:Tuition1: 19410 ⟵ “Tuition1 | $19,410 | $19,410”
  - on_campus:Mandatory Fees: 1350 ⟵ “Mandatory Fees | $1,350 | $1,350”
  - on_campus:Housing2: 6528 ⟵ “Housing2 | $6,528 | $7,668”
  - on_campus:Food3: 4582 ⟵ “Food3 | $4,582 | $4,100”
  - on_campus:Transportation: 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4: 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses: 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - on_campus:Loan Fees5: 120 ⟵ “Loan Fees5 | $120 | $120”
  - on_campus:Total Cost of Attendance: 37890 ⟵ “Total Cost of Attendance | $37,890 | $39,898”
  - on_campus:Tuition1: 19770 ⟵ “Tuition1 | $19,770 | $19,770”
  - on_campus:Mandatory Fees: 1350 ⟵ “Mandatory Fees | $1,350 | $1,350”
  - on_campus:Housing2: 6528 ⟵ “Housing2 | $6,528 | $768”
  - on_campus:Food3: 4582 ⟵ “Food3 | $4,582 | $4,100”
  - on_campus:Transportation: 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4: 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses: 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - … 83 more rows
### `e5285dd9359dc5c9` Fort Valley State University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fvsu.edu/content/userfiles/files/2024-2025%20Cost%20of%20Attendance.pdf (sha256 008c0406a551)
- issues: residency_unknown, stale_year_label:2024-25, conflicting_sources:https://www.fvsu.edu/content/userfiles/files/FVSU_2425_Cost%20of%20Attendances(2).pdf
- checks: {"columns": 1, "rows": 9}
  - column:Tuition: 5220.0 ⟵ “Tuition | $ 5,220.00”
  - column:Mandatory Fees: 1350.0 ⟵ “Mandatory Fees | $ 1,350.00”
  - column:Books/Course Materials/Supplies/Equipment: 1400.0 ⟵ “Books/Course Materials/Supplies/Equipment | $ 1,400.00”
  - column:Food: 4582.0 ⟵ “Food | $ 4,582.00”
  - column:Housing: 6528.0 ⟵ “Housing | $ 6,528.00”
  - column:Miscellaneous Living Expenses: 3150.0 ⟵ “Miscellaneous Living Expenses | $ 3,150.00”
  - column:Transportation: 1350.0 ⟵ “Transportation | $ 1,350.00”
  - column:Tuition: 5220.0 ⟵ “Tuition | $ 5,220.00”
  - column:Mandatory Fees: 1350.0 ⟵ “Mandatory Fees | $ 1,350.00”
  - column:Books/Course Materials/Supplies/Equipment: 1400.0 ⟵ “Books/Course Materials/Supplies/Equipment | $ 1,400.00”
  - column:Food: 4100.0 ⟵ “Food | $ 4,100.00”
  - column:Housing: 7668.0 ⟵ “Housing | $ 7,668.00”
  - column:Miscellaneous Living Expenses: 3150.0 ⟵ “Miscellaneous Living Expenses | $ 3,150.00”
  - column:Transportation: 2700.0 ⟵ “Transportation | $ 2,700.00”
  - column:Tuition: 19410.0 ⟵ “Tuition | $ 19,410.00”
  - column:Mandatory Fees: 1350.0 ⟵ “Mandatory Fees | $ 1,350.00”
  - column:Books/Course Materials/Supplies/Equipment: 1400.0 ⟵ “Books/Course Materials/Supplies/Equipment | $ 1,400.00”
  - column:Food: 4582.0 ⟵ “Food | $ 4,582.00”
  - column:Housing: 6528.0 ⟵ “Housing | $ 6,528.00”
  - column:Miscellaneous Living Expenses: 3150.0 ⟵ “Miscellaneous Living Expenses | $ 3,150.00”
  - column:Transportation: 1350.0 ⟵ “Transportation | $ 1,350.00”
  - column:Tuition: 19410.0 ⟵ “Tuition | $ 19,410.00”
  - column:Mandatory Fees: 1350.0 ⟵ “Mandatory Fees | $ 1,350.00”
  - column:Books/Course Materials/Supplies/Equipment: 1400.0 ⟵ “Books/Course Materials/Supplies/Equipment | $ 1,400.00”
  - column:Food: 4100.0 ⟵ “Food | $ 4,100.00”
  - … 57 more rows
### `52fd63e167c265c6` Georgia College & State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gcsu.edu/financialaid/zell-miller-scholarship-faq (sha256 01c3ad9bea06)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “GSFC must receive your appeal within 45 days of your denial of HOPE Scholarship from Georgia College.”
### `6e9efe0c0f05d358` Georgia College & State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.gcsu.edu/financialaid/cost-attendance (sha256 b42a12839b54)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees: 30950 ⟵ “Tuition and Fees | $30,950 | $30,950 | $30,950”
  - on_campus:Food: 4907 ⟵ “Food | $4,907 | $3,263 | $720”
  - on_campus:Housing: 8282 ⟵ “Housing | $8,282 | $6,934 | $1,818”
  - on_campus:Books, Course Material, Supplies & Equipment: 2000 ⟵ “Books, Course Material, Supplies & Equipment | $2,000 | $2,000 | $2,000”
  - on_campus:Transportation: 2157 ⟵ “Transportation | $2,157 | $2,157 | $2,157”
  - on_campus:Miscellaneous Personal Expenses: 7317 ⟵ “Miscellaneous Personal Expenses | $7,317 | $7,317 | $7,317”
  - on_campus:Total: 55613 ⟵ “Total | $55,613 | $52,621 | $44,962”
  - off_campus_not_with_family:Tuition and Fees: 30950 ⟵ “Tuition and Fees | $30,950 | $30,950 | $30,950”
  - off_campus_not_with_family:Food: 3263 ⟵ “Food | $4,907 | $3,263 | $720”
  - off_campus_not_with_family:Housing: 6934 ⟵ “Housing | $8,282 | $6,934 | $1,818”
  - off_campus_not_with_family:Books, Course Material, Supplies & Equipment: 2000 ⟵ “Books, Course Material, Supplies & Equipment | $2,000 | $2,000 | $2,000”
  - off_campus_not_with_family:Transportation: 2157 ⟵ “Transportation | $2,157 | $2,157 | $2,157”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 7317 ⟵ “Miscellaneous Personal Expenses | $7,317 | $7,317 | $7,317”
  - off_campus_not_with_family:Total: 52621 ⟵ “Total | $55,613 | $52,621 | $44,962”
  - column:Tuition and Fees: 30950 ⟵ “Tuition and Fees | $30,950 | $30,950 | $30,950”
  - column:Food: 720 ⟵ “Food | $4,907 | $3,263 | $720”
  - column:Housing: 1818 ⟵ “Housing | $8,282 | $6,934 | $1,818”
  - column:Books, Course Material, Supplies & Equipment: 2000 ⟵ “Books, Course Material, Supplies & Equipment | $2,000 | $2,000 | $2,000”
  - column:Transportation: 2157 ⟵ “Transportation | $2,157 | $2,157 | $2,157”
  - column:Miscellaneous Personal Expenses: 7317 ⟵ “Miscellaneous Personal Expenses | $7,317 | $7,317 | $7,317”
  - column:Total: 44962 ⟵ “Total | $55,613 | $52,621 | $44,962”
### `9ff81bf1580fbc6f` Georgia College & State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.gcsu.edu/financialaid/cost-attendance (sha256 b42a12839b54)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees: 9282 ⟵ “Tuition and Fees | $9,282 | $9,282 | $9,282”
  - on_campus:Food: 4907 ⟵ “Food | $4,907 | $3,263 | $720”
  - on_campus:Housing: 8282 ⟵ “Housing | $8,282 | $6,934 | $1,818”
  - on_campus:Books, Course Material, Supplies & Equipment: 2000 ⟵ “Books, Course Material, Supplies & Equipment | $2,000 | $2,000 | $2,000”
  - on_campus:Transportation: 2157 ⟵ “Transportation | $2,157 | $2,157 | $2,157”
  - on_campus:Miscellaneous Personal Expenses: 7317 ⟵ “Miscellaneous Personal Expenses | $7,317 | $7,317 | $7,317”
  - on_campus:Total: 33945 ⟵ “Total | $33,945 | $30,953 | $23,294”
  - off_campus_not_with_family:Tuition and Fees: 9282 ⟵ “Tuition and Fees | $9,282 | $9,282 | $9,282”
  - off_campus_not_with_family:Food: 3263 ⟵ “Food | $4,907 | $3,263 | $720”
  - off_campus_not_with_family:Housing: 6934 ⟵ “Housing | $8,282 | $6,934 | $1,818”
  - off_campus_not_with_family:Books, Course Material, Supplies & Equipment: 2000 ⟵ “Books, Course Material, Supplies & Equipment | $2,000 | $2,000 | $2,000”
  - off_campus_not_with_family:Transportation: 2157 ⟵ “Transportation | $2,157 | $2,157 | $2,157”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 7317 ⟵ “Miscellaneous Personal Expenses | $7,317 | $7,317 | $7,317”
  - off_campus_not_with_family:Total: 30953 ⟵ “Total | $33,945 | $30,953 | $23,294”
  - column:Tuition and Fees: 9282 ⟵ “Tuition and Fees | $9,282 | $9,282 | $9,282”
  - column:Food: 720 ⟵ “Food | $4,907 | $3,263 | $720”
  - column:Housing: 1818 ⟵ “Housing | $8,282 | $6,934 | $1,818”
  - column:Books, Course Material, Supplies & Equipment: 2000 ⟵ “Books, Course Material, Supplies & Equipment | $2,000 | $2,000 | $2,000”
  - column:Transportation: 2157 ⟵ “Transportation | $2,157 | $2,157 | $2,157”
  - column:Miscellaneous Personal Expenses: 7317 ⟵ “Miscellaneous Personal Expenses | $7,317 | $7,317 | $7,317”
  - column:Total: 23294 ⟵ “Total | $33,945 | $30,953 | $23,294”
### `6148b4ddcf381db4` Georgia Gwinnett College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ggc.edu/admission-aid/financial-aid/financial-aid-award-status (sha256 a59c0696a06e)
- issues: semantic_review_required, conflicting_sources:https://www.ggc.edu/admission-aid/financial-aid/missing-financial-aid-documents,https://www.ggc.edu/admission-aid/financial-aid/professional-judgment-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Citizenship Status Student Consumer Information Professional Judgment Information CONTACT US Contact us Financial Aid Services Location: Building D Phone: 678.407.5701 [email protected] Address Financial Aid Services, Bldg.”
### `6562fe7b0eb11557` Georgia Gwinnett College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ggc.edu/admission-aid/financial-aid/missing-financial-aid-documents (sha256 96a1ef4cf72c)
- issues: semantic_review_required, conflicting_sources:https://www.ggc.edu/admission-aid/financial-aid/financial-aid-award-status,https://www.ggc.edu/admission-aid/financial-aid/professional-judgment-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Citizenship Status Student Consumer Information Professional Judgement Information Contact Us Contact us Financial Aid Services Location: Building D Phone: 678.407.5701 [email protected] Address Financial Aid Services, Bldg.”
### `83f3a60a8f0fac14` Georgia Gwinnett College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ggc.edu/admission-aid/financial-aid/professional-judgment-information (sha256 782db71b0136)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Homelessness or Self-Supporting and at Risk of Homelessness Special Circumstances Cost of Attendance Unusual circumstances allows Financial Aid Services to make determinations that allow a dependent student to be considered independent.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances are not considered based solely on parents' refusal to contribute to the student’s education, parents unwillingness to provide information on the FAFSA or for the verification process, parents do not claim the student as a dependent for income tax purposes or the student is self-sufficient.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances allow changes to data elements that affect the federal methodology used to calculate the student aid index (SAI).”
### `a24f24dc4232bb00` Georgia Gwinnett College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ggc.edu/admission-aid/financial-aid/professional-judgment-information (sha256 782db71b0136)
- issues: semantic_review_required, conflicting_sources:https://www.ggc.edu/admission-aid/financial-aid/financial-aid-award-status,https://www.ggc.edu/admission-aid/financial-aid/missing-financial-aid-documents
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Such adjustments or exceptions are known as professional judgments and are considered on a case-by-case basis using a statement of explanation by the student and supporting documentation of the situation.”
  - sentence: professional_judgment ⟵ “A current FAFSA must be completed before professional judgments can be considered.”
  - sentence: professional_judgment ⟵ “Decisions based on professional judgements are made at the sole discretion of Financial Aid Services and cannot be appealed beyond this office.”
  - sentence: professional_judgment ⟵ “Eligibility for Financial Aid Satisfactory Academic Progress Standards (SAP) Professional Judgment Considerations If you believe you have a professional judgment situation or have additional questions about professional judgments, email [email protected] and include the last 6 digits of your student ID number followed by “Professional Judgment” in the subject line.”
### `a67159f1dd3300e7` Georgia Gwinnett College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ggc.edu/admission-aid/financial-aid/professional-judgment-information (sha256 782db71b0136)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Cost of attendance adjustments allow for an increase in components of the cost of attendance if there is significant increase in these expenses.”
### `fd27214a794cf7e7` Georgia Gwinnett College — appeals 2022-23 [new] (labeled_in_source)
- source: https://www.ggc.edu/admission-aid/undergraduate-financial-aid (sha256 52feb71892bb)
- issues: stale_year_label:2022-23, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Citizenship Status Student Consumer Information Professional Judgment Information Contact Us Contact us Financial Aid Services Location: Building D Phone: 678.407.5701 [email protected] Address Financial Aid Services, Bldg.”
### `03f7c3ba1f3e0d89` Georgia Gwinnett College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ggc.edu/admission-aid/financial-aid/student-consumer-info (sha256 27bb65020d11)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and mandatory fees: 17334 ⟵ “Tuition and mandatory fees | $5,364 | $17,334 | $5,364 | $17,334 | $5,364 | $17,334”
  - on_campus:Housing and meals: 15530 ⟵ “Housing and meals | $15,530 | $15,530 | $10,010 | $10,010 | $14,590 | $14,590”
  - on_campus:Books, course materials, supplies and equipment: 1660 ⟵ “Books, course materials, supplies and equipment | $1,660 | $1,660 | $1,660 | $1,660 | $1,660 | $1,660”
  - on_campus:Transportation: 2740 ⟵ “Transportation | $2,740 | $2,740 | $2,740 | $2,740 | $2,740 | $2,740”
  - on_campus:Miscellaneous personal expenses: 3150 ⟵ “Miscellaneous personal expenses | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - on_campus:Total for 2025-2026 academic year: 40414 ⟵ “Total for 2025-2026 academic year | $28,444 | $40,414 | $22,924 | $34,894 | $27,504 | $39,474”
  - on_campus:Tuition and mandatory fees: 17334 ⟵ “Tuition and mandatory fees | $5,364 | $17,334 | $5,364 | $17,334 | $5,364 | $17,334”
  - on_campus:Housing and meals: 10010 ⟵ “Housing and meals | $15,530 | $15,530 | $10,010 | $10,010 | $14,590 | $14,590”
  - on_campus:Books, course materials, supplies and equipment: 1660 ⟵ “Books, course materials, supplies and equipment | $1,660 | $1,660 | $1,660 | $1,660 | $1,660 | $1,660”
  - on_campus:Transportation: 2740 ⟵ “Transportation | $2,740 | $2,740 | $2,740 | $2,740 | $2,740 | $2,740”
  - on_campus:Miscellaneous personal expenses: 3150 ⟵ “Miscellaneous personal expenses | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - on_campus:Total for 2025-2026 academic year: 34894 ⟵ “Total for 2025-2026 academic year | $28,444 | $40,414 | $22,924 | $34,894 | $27,504 | $39,474”
  - off_campus_not_with_family:Tuition and mandatory fees: 17334 ⟵ “Tuition and mandatory fees | $5,364 | $17,334 | $5,364 | $17,334 | $5,364 | $17,334”
  - off_campus_not_with_family:Housing and meals: 14590 ⟵ “Housing and meals | $15,530 | $15,530 | $10,010 | $10,010 | $14,590 | $14,590”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1660 ⟵ “Books, course materials, supplies and equipment | $1,660 | $1,660 | $1,660 | $1,660 | $1,660 | $1,660”
  - off_campus_not_with_family:Transportation: 2740 ⟵ “Transportation | $2,740 | $2,740 | $2,740 | $2,740 | $2,740 | $2,740”
  - off_campus_not_with_family:Miscellaneous personal expenses: 3150 ⟵ “Miscellaneous personal expenses | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - off_campus_not_with_family:Total for 2025-2026 academic year: 39474 ⟵ “Total for 2025-2026 academic year | $28,444 | $40,414 | $22,924 | $34,894 | $27,504 | $39,474”
### `171fa8d1a6bde4e5` Georgia Gwinnett College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.ggc.edu/admission-aid/financial-aid/student-consumer-info (sha256 27bb65020d11)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and mandatory fees: 5364 ⟵ “Tuition and mandatory fees | $5,364 | $17,334 | $5,364 | $17,334 | $5,364 | $17,334”
  - on_campus:Housing and meals: 15530 ⟵ “Housing and meals | $15,530 | $15,530 | $10,010 | $10,010 | $14,590 | $14,590”
  - on_campus:Books, course materials, supplies and equipment: 1660 ⟵ “Books, course materials, supplies and equipment | $1,660 | $1,660 | $1,660 | $1,660 | $1,660 | $1,660”
  - on_campus:Transportation: 2740 ⟵ “Transportation | $2,740 | $2,740 | $2,740 | $2,740 | $2,740 | $2,740”
  - on_campus:Miscellaneous personal expenses: 3150 ⟵ “Miscellaneous personal expenses | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - on_campus:Total for 2025-2026 academic year: 28444 ⟵ “Total for 2025-2026 academic year | $28,444 | $40,414 | $22,924 | $34,894 | $27,504 | $39,474”
  - on_campus:Tuition and mandatory fees: 5364 ⟵ “Tuition and mandatory fees | $5,364 | $17,334 | $5,364 | $17,334 | $5,364 | $17,334”
  - on_campus:Housing and meals: 10010 ⟵ “Housing and meals | $15,530 | $15,530 | $10,010 | $10,010 | $14,590 | $14,590”
  - on_campus:Books, course materials, supplies and equipment: 1660 ⟵ “Books, course materials, supplies and equipment | $1,660 | $1,660 | $1,660 | $1,660 | $1,660 | $1,660”
  - on_campus:Transportation: 2740 ⟵ “Transportation | $2,740 | $2,740 | $2,740 | $2,740 | $2,740 | $2,740”
  - on_campus:Miscellaneous personal expenses: 3150 ⟵ “Miscellaneous personal expenses | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - on_campus:Total for 2025-2026 academic year: 22924 ⟵ “Total for 2025-2026 academic year | $28,444 | $40,414 | $22,924 | $34,894 | $27,504 | $39,474”
  - off_campus_not_with_family:Tuition and mandatory fees: 5364 ⟵ “Tuition and mandatory fees | $5,364 | $17,334 | $5,364 | $17,334 | $5,364 | $17,334”
  - off_campus_not_with_family:Housing and meals: 14590 ⟵ “Housing and meals | $15,530 | $15,530 | $10,010 | $10,010 | $14,590 | $14,590”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1660 ⟵ “Books, course materials, supplies and equipment | $1,660 | $1,660 | $1,660 | $1,660 | $1,660 | $1,660”
  - off_campus_not_with_family:Transportation: 2740 ⟵ “Transportation | $2,740 | $2,740 | $2,740 | $2,740 | $2,740 | $2,740”
  - off_campus_not_with_family:Miscellaneous personal expenses: 3150 ⟵ “Miscellaneous personal expenses | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - off_campus_not_with_family:Total for 2025-2026 academic year: 27504 ⟵ “Total for 2025-2026 academic year | $28,444 | $40,414 | $22,924 | $34,894 | $27,504 | $39,474”
### `9b7142de9eb32b93` Georgia Gwinnett College — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ggc.edu/admission-aid/financial-aid/student-consumer-info (sha256 27bb65020d11)
- issues: stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and mandatory fees: 17004 ⟵ “Tuition and mandatory fees | $5,364 | $17,004 | $5,364 | $17,004 | $5,364 | $17,004”
  - on_campus:Housing and meals: 15220 ⟵ “Housing and meals | $15,220 | $15,220 | $9,560 | $9,560 | $14,180 | $14,180”
  - on_campus:Books, course materials, supplies and equipment: 1420 ⟵ “Books, course materials, supplies and equipment | $1,420 | $1,420 | $1,420 | $1,420 | $1,420 | $1,420”
  - on_campus:Transportation: 2700 ⟵ “Transportation | $2,700 | $2,700 | $2,700 | $2,700 | $2,700 | $2,700”
  - on_campus:Miscellaneous personal expenses: 3380 ⟵ “Miscellaneous personal expenses | $3,380 | $3,380 | $3,380 | $3,380 | $3,380 | $3,380”
  - on_campus:Total for 2025-2026 academic year: 39724 ⟵ “Total for 2025-2026 academic year | $28,024 | $39,724 | $22,424 | $34,064 | $27,044 | $38,684”
  - on_campus:Tuition and mandatory fees: 17004 ⟵ “Tuition and mandatory fees | $5,364 | $17,004 | $5,364 | $17,004 | $5,364 | $17,004”
  - on_campus:Housing and meals: 9560 ⟵ “Housing and meals | $15,220 | $15,220 | $9,560 | $9,560 | $14,180 | $14,180”
  - on_campus:Books, course materials, supplies and equipment: 1420 ⟵ “Books, course materials, supplies and equipment | $1,420 | $1,420 | $1,420 | $1,420 | $1,420 | $1,420”
  - on_campus:Transportation: 2700 ⟵ “Transportation | $2,700 | $2,700 | $2,700 | $2,700 | $2,700 | $2,700”
  - on_campus:Miscellaneous personal expenses: 3380 ⟵ “Miscellaneous personal expenses | $3,380 | $3,380 | $3,380 | $3,380 | $3,380 | $3,380”
  - on_campus:Total for 2025-2026 academic year: 34064 ⟵ “Total for 2025-2026 academic year | $28,024 | $39,724 | $22,424 | $34,064 | $27,044 | $38,684”
  - off_campus_not_with_family:Tuition and mandatory fees: 17004 ⟵ “Tuition and mandatory fees | $5,364 | $17,004 | $5,364 | $17,004 | $5,364 | $17,004”
  - off_campus_not_with_family:Housing and meals: 14180 ⟵ “Housing and meals | $15,220 | $15,220 | $9,560 | $9,560 | $14,180 | $14,180”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1420 ⟵ “Books, course materials, supplies and equipment | $1,420 | $1,420 | $1,420 | $1,420 | $1,420 | $1,420”
  - off_campus_not_with_family:Transportation: 2700 ⟵ “Transportation | $2,700 | $2,700 | $2,700 | $2,700 | $2,700 | $2,700”
  - off_campus_not_with_family:Miscellaneous personal expenses: 3380 ⟵ “Miscellaneous personal expenses | $3,380 | $3,380 | $3,380 | $3,380 | $3,380 | $3,380”
  - off_campus_not_with_family:Total for 2025-2026 academic year: 38684 ⟵ “Total for 2025-2026 academic year | $28,024 | $39,724 | $22,424 | $34,064 | $27,044 | $38,684”
### `a2f426da7652eaae` Georgia Gwinnett College — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.ggc.edu/admission-aid/financial-aid/student-consumer-info (sha256 27bb65020d11)
- issues: components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": false, "rows": 6}
  - on_campus:Tuition and mandatory fees: 5364 ⟵ “Tuition and mandatory fees | $5,364 | $17,004 | $5,364 | $17,004 | $5,364 | $17,004”
  - on_campus:Housing and meals: 15220 ⟵ “Housing and meals | $15,220 | $15,220 | $9,560 | $9,560 | $14,180 | $14,180”
  - on_campus:Books, course materials, supplies and equipment: 1420 ⟵ “Books, course materials, supplies and equipment | $1,420 | $1,420 | $1,420 | $1,420 | $1,420 | $1,420”
  - on_campus:Transportation: 2700 ⟵ “Transportation | $2,700 | $2,700 | $2,700 | $2,700 | $2,700 | $2,700”
  - on_campus:Miscellaneous personal expenses: 3380 ⟵ “Miscellaneous personal expenses | $3,380 | $3,380 | $3,380 | $3,380 | $3,380 | $3,380”
  - on_campus:Total for 2025-2026 academic year: 28024 ⟵ “Total for 2025-2026 academic year | $28,024 | $39,724 | $22,424 | $34,064 | $27,044 | $38,684”
  - on_campus:Tuition and mandatory fees: 5364 ⟵ “Tuition and mandatory fees | $5,364 | $17,004 | $5,364 | $17,004 | $5,364 | $17,004”
  - on_campus:Housing and meals: 9560 ⟵ “Housing and meals | $15,220 | $15,220 | $9,560 | $9,560 | $14,180 | $14,180”
  - on_campus:Books, course materials, supplies and equipment: 1420 ⟵ “Books, course materials, supplies and equipment | $1,420 | $1,420 | $1,420 | $1,420 | $1,420 | $1,420”
  - on_campus:Transportation: 2700 ⟵ “Transportation | $2,700 | $2,700 | $2,700 | $2,700 | $2,700 | $2,700”
  - on_campus:Miscellaneous personal expenses: 3380 ⟵ “Miscellaneous personal expenses | $3,380 | $3,380 | $3,380 | $3,380 | $3,380 | $3,380”
  - on_campus:Total for 2025-2026 academic year: 22424 ⟵ “Total for 2025-2026 academic year | $28,024 | $39,724 | $22,424 | $34,064 | $27,044 | $38,684”
  - off_campus_not_with_family:Tuition and mandatory fees: 5364 ⟵ “Tuition and mandatory fees | $5,364 | $17,004 | $5,364 | $17,004 | $5,364 | $17,004”
  - off_campus_not_with_family:Housing and meals: 14180 ⟵ “Housing and meals | $15,220 | $15,220 | $9,560 | $9,560 | $14,180 | $14,180”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1420 ⟵ “Books, course materials, supplies and equipment | $1,420 | $1,420 | $1,420 | $1,420 | $1,420 | $1,420”
  - off_campus_not_with_family:Transportation: 2700 ⟵ “Transportation | $2,700 | $2,700 | $2,700 | $2,700 | $2,700 | $2,700”
  - off_campus_not_with_family:Miscellaneous personal expenses: 3380 ⟵ “Miscellaneous personal expenses | $3,380 | $3,380 | $3,380 | $3,380 | $3,380 | $3,380”
  - off_campus_not_with_family:Total for 2025-2026 academic year: 27044 ⟵ “Total for 2025-2026 academic year | $28,024 | $39,724 | $22,424 | $34,064 | $27,044 | $38,684”
### `2ec91d8f285a9843` Georgia Highlands College — appeals 2026-27 [new] (source_unlabeled)
- source: https://sites.highlands.edu/financial-aid/satisfactory-academic-progress-2/satisfactory-academic-progress/ (sha256 85f4adbe99e4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: sap_appeal ⟵ “SAP Appeals If you are placed on Financial Aid Suspension, you may be eligible to file a SAP Appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeals must have documentation of extenuating circumstances beyond your control that contributed to your inability to maintain Satisfactory Academic Progress.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Committee will only review and render a decision on COMPLETE Appeals where all relevant documentation has been provided.”
  - sentence: sap_appeal ⟵ “Log onto highlands.studentforms.com to request a SAP Appeal if you think you may have extenuating circumstances to qualify.”
  - sentence: sap_appeal ⟵ “The system will add a SAP Appeal link and once it appears, you can input an electronic written statement explaining your circumstances.”
  - sentence: sap_appeal ⟵ “SAP Appeals are reviewed monthly by the SAP Appeal Committee.”
### `9cc67e55b8d24fa8` Georgia Institute of Technology-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://finaid.gatech.edu/manage-aid/academic-progress (sha256 bbb39a989b1a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If a grade change would positively affect a student’s financial aid eligibility, the student may submit a SAP Appeal to the Office of Scholarships and Financial Aid.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process Students who fail to meet SAP requirements may submit a SAP appeal to request reinstatement of financial aid.”
  - sentence: sap_appeal ⟵ “Step 2: Initiate Your SAP Appeal Click Manage Request in the portal.”
  - sentence: sap_appeal ⟵ “Select SAP Appeal for the appropriate aid year.”
### `2b5e7394ee46245e` Georgia Institute of Technology-Main Campus — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.gatech.edu/academics/undergraduate/credit-tests-scores/advanced-placement-exams/ (sha256 eecad63896f5)
- issues: rows_without_score
- checks: {"distinct_exams": 33, "equivalencies": 34, "rows_without_score": 34}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “African American Studies | AP Score: 4 or 5 = HTS 1XXX | 3”
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “Art History | AP Score: 4 or 5 ID 2242 | 3”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | AP Score: 4 or 5 = BIOS 1107 and BIOS 1107L | 4”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Mathematics - Calculus AB | AP Score: 4 or 5 = MATH 1551 4 | 2”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Mathematics - Calculus BC | AP Score: 4 or 5 = MATH 1551 & MATH 15524 | 6”
  - equivalencies[AP-PRECALCULUS|None]:  ⟵ “Mathematics - Precalculus | AP Score: 4 or 5 = MATH 1113 | 4”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry - Effective Summer 2010 | AP Score: 4 = CHEM 1211K | 4”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | AP Score: 5 = CHEM 1310 | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “Chinese Language and Culture | AP Score: 3 = CHIN 1001 and CHIN 1002 5 | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “Computer Science Principles | AP Score: 4 or 5 = CS 1XXX | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language and Composition | AP Score: 4 or 5 = ENGL 1101 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “English Literature and Composition | AP Score: 4 or 5 = ENGL 1101 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “Environmental Science | AP Score: 4 or 5 = EAS 1600 | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “European History | AP Score: 4 or 5 = HTS 1031 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “French Language and Culture | AP Score: 3 = FREN 1001 and FREN 1002 5 | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “German Language and Culture | AP Score: 3 = GRMN 1001 & GRMN 1002 5 | 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Human Geography | AP Score: 4 or 5 = SS 1XXX | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “Italian Language and Culture | No Credit Awarded | 0”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “Japanese Language and Culture | AP Score: 3 = JAPN 1001 and JAPN 1002 5 | 8”
  - equivalencies[AP-LATIN|None]:  ⟵ “Latin (Language and Culture) | AP Score: 4 or 5 = LATN 2XXX | 6”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Economics (Macroeconomics) | AP Score: 4 or 5 = ECON 2105 | 3”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Economics (Microeconomics) | AP Score: 4 or 5 = ECON 2106 | 3”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “Music Theory | AP Score: 4 or 5 = MUSI 2700 | 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|None]:  ⟵ “Physics C, Part I: Mechanics | AP Score: 5 = PHYS 22113 | 4”
  - equivalencies[AP-PHYSICS-1|None]:  ⟵ “Physics 1: Algebra-Based | AP Score: 4 or 5 = PHYS 1111K | 4”
  - … 9 more rows
### `77d4f0fa6a65154c` Georgia Military College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.gmc.edu/scholarships/ (sha256 82e4e91814d1)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Eligibility Criteria To qualify, students must: • Meet the completion percentage for each enrolled program. • Submit both the GSFApp and the 2025–2026 FAFSA, including all required documentation, by the last day of the term for which they are applying. • Owe a balance to Georgia Military College for direct educational costs (e.g., tuition, fees, books, supplies, meal plans, and housing billed by t”
### `7a96b98092fbfa15` Georgia Military College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.gmc.edu/financial-aid/ (sha256 b5d19032c6f7)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “The three areas for which we will consider PJ are: Increases in the student’s Cost of Attendance to account for extraordinary expenses a student might incur while attending GMC; Changes in financial circumstances including loss of income, loss of recurring taxed or untaxed income, loss of assets, or unusual medical expenses; Dependency override to change your financial aid dependency status from d”
  - sentence: dependency_override ⟵ “Dependency Status Appeals Petition to be declared an Independent Student for Federal Aid Purposes: The law governing Federal Student Aid (Title IV) categorizes students as “dependent” or “independent” based on the premise the student and parents have the primary responsibility for meeting the student’s educational costs.”
  - sentence: dependency_override ⟵ “If you can document the unusual or unique circumstances governing why you feel you should be declared independent for Title IV Federal Aid purposes, you may petition for a dependency override by completing this form and providing documentation.”
### `aaca37c0e7353961` Georgia Military College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.gmc.edu/financial-aid/ (sha256 b5d19032c6f7)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Students may appeal their cost of attendance by requesting a Professional Judgement (PJ).”
  - sentence: professional_judgment ⟵ “Changes in Financial Circumstances Parent Professional Judgment Request to Recalculate the Expected Family Contribution for Dependent Students: If the parents’ current expected income is substantially less than it was during the tax year used on the FAFSA due to special circumstances, we may be able to use the parents’ current estimated income to reevaluate eligibility for Federal Student Aid.”
  - sentence: professional_judgment ⟵ “Student Professional Judgment Request to Recalculate the Expected Family Contribution for Independent Students: If the students/spouses expected income is substantially less than it was during the tax year used on the FAFSA due to special circumstances, we may be able to use the students/spouses current estimated income to reevaluate eligibility for Federal Student Aid.”
### `cfabd5c2f1feb141` Georgia Military College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.gmc.edu/financial-aid/ (sha256 b5d19032c6f7)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Cost of Attendance Increases Computer Purchase: Federal regulations permit GMC to consider the cost to purchase a computer when calculating a student’s Cost of Attendance (COA).”
### `cdde2b4681ca8837` Georgia Military College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.gmc.edu/tuition-fees/ (sha256 1444d5d2057b)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Application Fee: 35 ⟵ “Application Fee | $35”
  - column:Uniform Fee: 1040 ⟵ “Uniform Fee | $1,040”
  - column:Tuition: 3323 ⟵ “Tuition | $3,323”
  - column:Book & Materials Fee: 190 ⟵ “Book & Materials Fee | $190”
  - column:Cadet Fee: 412 ⟵ “Cadet Fee | $412”
  - column:Room: 912 ⟵ “Room | $912”
  - column:Board: 1695 ⟵ “Board | $1,695”
  - column:Total Per Term: 6532 ⟵ “Total Per Term | $6,532”
### `6ee2d3a3e38d1b55` Georgia Military College — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.gmc.edu/wp-content/uploads/2026/02/2025-2026-Catalog-Mid-Year-Update-Feb-2026.pdf (sha256 0d9a981c53e9)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “GMC may award transfer course credit for work completed at other colleges and universities in which a grade of “C” (2.0) or better was earned.”
  - min_grade: C ⟵ “GMC may award transfer course credit for work completed at other colleges and universities in which a grade of “C” (2.0) or better was earned.”
  - min_grade: C ⟵ “Written Communication Competency In Area A1, students must successfully complete ENG 101 and ENG 102 with a grade of "C" or better or receive equivalent alternative credit or transfer credit from an accredited institution.”
### `0f6b2e93f3368b74` Georgia Northwestern Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gntc.edu/appeals/financial-aid/ (sha256 26f0c615091c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Contact Financial Aid for more information.”
### `7965ba61e8cc9332` Georgia Northwestern Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gntc.edu/appeals/equal-opportunity/ (sha256 48b283e940f1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “GNTC, TCSG and its constituent Technical Colleges do not discriminate on the basis of race, color, creed or religion, national or ethnic origin, sex (including pregnancy, sexual orientation and gender identity), disability, age, political affiliation or belief, genetic information, veteran or military status, marital status or citizenship status (except in those special circumstances permitted or ”
### `88e03266eef5ab99` Georgia Southern University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.georgiasouthern.edu/admissions-aid/financial-aid/policies/satisfactory-academic-progress-sap (sha256 b06680faebce)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Dates: Students in violation of satisfactory academic progress standards who want to be considered for financial aid eligibility must submit documentation by certain deadlines, as indicated below.”
### `63e07146b6889019` Georgia Southwestern State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gsw.edu/financial-aid/satisfactory-academic-progress/ (sha256 03a9b45e26c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Appeals Process GSW has established an SAP Financial Aid Appeals Process to assist students who have failed to maintain an SAP due to mitigating circumstances (which has now been resolved or stabilized).”
  - sentence: sap_appeal ⟵ “Students may be awarded Federal Pell Grants, Federal Perkins Loans, Federal Supplemental Educational Opportunity Grants (FSEOG), Federal Work-Study, Federal Direct (Subsidized, Unsubsidized, and Parent PLUS) loans, HOPE Scholarship, Zell Miller Scholarship, etc. for the semester in which the student is now making an SAP, the semester for which an SAP appeal has been approved, or for the next perio”
### `62427e9ecd804ddf` Georgia Southwestern State University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.gsw.edu/student-account/files/cost-of-attendance-budgets.pdf (sha256 00a655664064)
- issues: multiple_total_rows
- checks: {"columns": 3, "rows": 7}
  - on_campus:Tuition and Fees: 6344 ⟵ “Tuition and Fees | 6344 | 6344 | 6344”
  - on_campus:and Housing): 11064 ⟵ “and Housing) | 11064 | 15220 | 10200”
  - on_campus:Miscellaneous: 2430 ⟵ “Miscellaneous | 2430 | 2430 | 2430”
  - on_campus:Transportation: 1380 ⟵ “Transportation | 1380 | 1380 | 1380”
  - on_campus:Supplies/Equipment: 1330 ⟵ “Supplies/Equipment | 1330 | 1330 | 1330”
  - on_campus:Loan fees: 100 ⟵ “Loan fees | 100 | 100 | 100”
  - on_campus:Total: 22648 ⟵ “Total | 22648 | 26804 | 21784”
  - on_campus:Tuition and Fees: 21464 ⟵ “Tuition and Fees | 21464 | 21464 | 21464”
  - on_campus:and Housing): 11064 ⟵ “and Housing) | 11064 | 15220 | 10200”
  - on_campus:Miscellaneous: 2430 ⟵ “Miscellaneous | 2430 | 2430 | 2430”
  - on_campus:Transportation: 1380 ⟵ “Transportation | 1380 | 1380 | 1380”
  - on_campus:Supplies/Equipment: 1330 ⟵ “Supplies/Equipment | 1330 | 1330 | 1330”
  - on_campus:Loan fees: 100 ⟵ “Loan fees | 100 | 100 | 100”
  - on_campus:Total: 37768 ⟵ “Total | 37768 | 41924 | 36904”
  - on_campus:Tuition and Fees: 4718 ⟵ “Tuition and Fees | 4718 | 4718 | 4718”
  - on_campus:and Housing): 11064 ⟵ “and Housing) | 11064 | 15220 | 10200”
  - on_campus:Miscellaneous: 2430 ⟵ “Miscellaneous | 2430 | 2430 | 2430”
  - on_campus:Transportation: 1380 ⟵ “Transportation | 1380 | 1380 | 1380”
  - on_campus:Supplies/Equipment: 1330 ⟵ “Supplies/Equipment | 1330 | 1330 | 1330”
  - on_campus:Loan fees: 100 ⟵ “Loan fees | 100 | 100 | 100”
  - on_campus:Total: 21022 ⟵ “Total | 21022 | 25178 | 20158”
  - on_campus:Tuition and Fees: 16292 ⟵ “Tuition and Fees | 16292 | 16292 | 16292”
  - on_campus:and Housing): 11064 ⟵ “and Housing) | 11064 | 15220 | 10200”
  - on_campus:Miscellaneous: 2430 ⟵ “Miscellaneous | 2430 | 2430 | 2430”
  - on_campus:Transportation: 1380 ⟵ “Transportation | 1380 | 1380 | 1380”
  - … 59 more rows
### `ccdf75cd6f4ffdd4` Georgia Southwestern State University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.gsw.edu/financial-aid/gsw-affordability (sha256 5f200ffe4d23)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 9, "rows": 3}
  - column:Tuition: 2640 ⟵ “Tuition | $2,640 | $2,640 | $2,835 | $2,895 | $2,835 | $2,835 | $2,835 | $2,880 | $3,886”
  - column:Mandatory Fees: 532 ⟵ “Mandatory Fees | $532 | $431 | $818 | $590 | $800 | $724 | $705 | $594 | $755”
  - column:Meal Plan (Highest Plan): 2230 ⟵ “Meal Plan (Highest Plan) | $2,230 | $2,000 | $2,260 | $2,627 | $2,660 | $2,741 | $2,917 | $2,450 | $2,768”
  - column:Tuition: 2640 ⟵ “Tuition | $2,640 | $2,640 | $2,835 | $2,895 | $2,835 | $2,835 | $2,835 | $2,880 | $3,886”
  - column:Mandatory Fees: 431 ⟵ “Mandatory Fees | $532 | $431 | $818 | $590 | $800 | $724 | $705 | $594 | $755”
  - column:Meal Plan (Highest Plan): 2000 ⟵ “Meal Plan (Highest Plan) | $2,230 | $2,000 | $2,260 | $2,627 | $2,660 | $2,741 | $2,917 | $2,450 | $2,768”
  - column:Yearly Savings by Attending GSW: 1137 ⟵ “Yearly Savings by Attending GSW | Best Value | $1,137 | $2,353 | $3,559 | $3,645 | $3,705 | $4,048 | $4,107 | $7,171”
  - column:Tuition: 2835 ⟵ “Tuition | $2,640 | $2,640 | $2,835 | $2,895 | $2,835 | $2,835 | $2,835 | $2,880 | $3,886”
  - column:Mandatory Fees: 818 ⟵ “Mandatory Fees | $532 | $431 | $818 | $590 | $800 | $724 | $705 | $594 | $755”
  - column:Meal Plan (Highest Plan): 2260 ⟵ “Meal Plan (Highest Plan) | $2,230 | $2,000 | $2,260 | $2,627 | $2,660 | $2,741 | $2,917 | $2,450 | $2,768”
  - column:Yearly Savings by Attending GSW: 2353 ⟵ “Yearly Savings by Attending GSW | Best Value | $1,137 | $2,353 | $3,559 | $3,645 | $3,705 | $4,048 | $4,107 | $7,171”
  - column:Tuition: 2895 ⟵ “Tuition | $2,640 | $2,640 | $2,835 | $2,895 | $2,835 | $2,835 | $2,835 | $2,880 | $3,886”
  - column:Mandatory Fees: 590 ⟵ “Mandatory Fees | $532 | $431 | $818 | $590 | $800 | $724 | $705 | $594 | $755”
  - column:Meal Plan (Highest Plan): 2627 ⟵ “Meal Plan (Highest Plan) | $2,230 | $2,000 | $2,260 | $2,627 | $2,660 | $2,741 | $2,917 | $2,450 | $2,768”
  - column:Yearly Savings by Attending GSW: 3559 ⟵ “Yearly Savings by Attending GSW | Best Value | $1,137 | $2,353 | $3,559 | $3,645 | $3,705 | $4,048 | $4,107 | $7,171”
  - column:Tuition: 2835 ⟵ “Tuition | $2,640 | $2,640 | $2,835 | $2,895 | $2,835 | $2,835 | $2,835 | $2,880 | $3,886”
  - column:Mandatory Fees: 800 ⟵ “Mandatory Fees | $532 | $431 | $818 | $590 | $800 | $724 | $705 | $594 | $755”
  - column:Meal Plan (Highest Plan): 2660 ⟵ “Meal Plan (Highest Plan) | $2,230 | $2,000 | $2,260 | $2,627 | $2,660 | $2,741 | $2,917 | $2,450 | $2,768”
  - column:Yearly Savings by Attending GSW: 3645 ⟵ “Yearly Savings by Attending GSW | Best Value | $1,137 | $2,353 | $3,559 | $3,645 | $3,705 | $4,048 | $4,107 | $7,171”
  - column:Tuition: 2835 ⟵ “Tuition | $2,640 | $2,640 | $2,835 | $2,895 | $2,835 | $2,835 | $2,835 | $2,880 | $3,886”
  - column:Mandatory Fees: 724 ⟵ “Mandatory Fees | $532 | $431 | $818 | $590 | $800 | $724 | $705 | $594 | $755”
  - column:Meal Plan (Highest Plan): 2741 ⟵ “Meal Plan (Highest Plan) | $2,230 | $2,000 | $2,260 | $2,627 | $2,660 | $2,741 | $2,917 | $2,450 | $2,768”
  - column:Yearly Savings by Attending GSW: 3705 ⟵ “Yearly Savings by Attending GSW | Best Value | $1,137 | $2,353 | $3,559 | $3,645 | $3,705 | $4,048 | $4,107 | $7,171”
  - column:Tuition: 2835 ⟵ “Tuition | $2,640 | $2,640 | $2,835 | $2,895 | $2,835 | $2,835 | $2,835 | $2,880 | $3,886”
  - column:Mandatory Fees: 705 ⟵ “Mandatory Fees | $532 | $431 | $818 | $590 | $800 | $724 | $705 | $594 | $755”
  - … 10 more rows
### `0d804ac5c50c390e` Gordon State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.gordonstate.edu/documents/departments/bursars-office/coa_2627.pdf (sha256 e78443a2a35f)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, conflicting_sources:https://www.gordonstate.edu/documents/departments/budgets/fy24_original-budget-packet.pdf,https://www.gordonstate.edu/documents/departments/budgets/fy25-original-budget-packet.pdf,https://www.gordonstate.edu/documents/departments/budgets/fy26-budget-booklet1.pdf
- checks: {"columns": 4, "rows": 11}
  - on_campus:Tuition*: 3300 ⟵ “Tuition* | $3,300 | $3,300 | Tuition* | $4,830 | $4,830”
  - on_campus:Fees: 1028 ⟵ “Fees | $1,028 | $1,028 | Fees | $1,028 | $1,028”
  - on_campus:Housing: 7329 ⟵ “Housing | $7,329 | $13,941 | Housing | $7,329 | $13,941”
  - on_campus:Food: 3650 ⟵ “Food | $3,650 | $4,473 | Food | $3,650 | $4,473”
  - on_campus:Transportation: 5481 ⟵ “Transportation | $5,481 | $5,481 | Transportation | $5,481 | $5,481”
  - on_campus:Books and Supplies: 2043 ⟵ “Books and Supplies | $2,043 | $2,043 | Books and Supplies | $2,043 | $2,043”
  - on_campus:Personal Expenses: 3078 ⟵ “Personal Expenses | $3,078 | $3,078 | Personal Expenses | $3,078 | $3,078”
  - on_campus:Loan Fees: 92 ⟵ “Loan Fees | $92 | $92 | Loan Fees | $92 | $92”
  - on_campus:Total Cost of Attendance: 26001 ⟵ “Total Cost of Attendance | $26,001 | $33,436 | Total Cost of Attendance | $27,531 | $34,966”
  - on_campus:Tuition*: 13050 ⟵ “Tuition* | $13,050 | $13,050 | Tuition* | $13,440 | $13,440”
  - on_campus:Fees: 1028 ⟵ “Fees | $1,028 | $1,028 | Fees | $1,028 | $1,028”
  - on_campus:Housing**: 7329 ⟵ “Housing** | $7,329 | $13,941 | Housing** | $7,329 | $13,941”
  - on_campus:Food: 3650 ⟵ “Food | $3,650 | $4,473 | Food | $3,650 | $4,473”
  - on_campus:Transportation: 5481 ⟵ “Transportation | $5,481 | $5,481 | Transportation | $5,481 | $5,481”
  - on_campus:Books and Supplies: 2043 ⟵ “Books and Supplies | $2,043 | $2,043 | Books and Supplies | $2,043 | $2,043”
  - on_campus:Personal Expenses: 3078 ⟵ “Personal Expenses | $3,078 | $3,078 | Personal Expenses | $3,078 | $3,078”
  - on_campus:Loan Fees***: 92 ⟵ “Loan Fees*** | $92 | $92 | Student Health Insurance*** | $2,981 | $2,981”
  - on_campus:Total Cost of Attendance: 35751 ⟵ “Total Cost of Attendance | $35,751 | $43,186 | Total Cost of Attendance | $39,030 | $46,465”
  - off_campus_not_with_family:Tuition*: 3300 ⟵ “Tuition* | $3,300 | $3,300 | Tuition* | $4,830 | $4,830”
  - off_campus_not_with_family:Fees: 1028 ⟵ “Fees | $1,028 | $1,028 | Fees | $1,028 | $1,028”
  - off_campus_not_with_family:Housing: 13941 ⟵ “Housing | $7,329 | $13,941 | Housing | $7,329 | $13,941”
  - off_campus_not_with_family:Food: 4473 ⟵ “Food | $3,650 | $4,473 | Food | $3,650 | $4,473”
  - off_campus_not_with_family:Transportation: 5481 ⟵ “Transportation | $5,481 | $5,481 | Transportation | $5,481 | $5,481”
  - off_campus_not_with_family:Books and Supplies: 2043 ⟵ “Books and Supplies | $2,043 | $2,043 | Books and Supplies | $2,043 | $2,043”
  - off_campus_not_with_family:Personal Expenses: 3078 ⟵ “Personal Expenses | $3,078 | $3,078 | Personal Expenses | $3,078 | $3,078”
  - … 47 more rows
### `390dede60813f526` Gordon State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.gordonstate.edu/documents/departments/budgets/fy26-budget-booklet1.pdf (sha256 c911e507161c)
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown, conflicting_sources:https://www.gordonstate.edu/documents/departments/budgets/fy24_original-budget-packet.pdf,https://www.gordonstate.edu/documents/departments/budgets/fy25-original-budget-packet.pdf,https://www.gordonstate.edu/documents/departments/bursars-office/coa_2627.pdf
- checks: {"columns": 12, "rows": 300}
  - column:STATE APPROPRIATIONS: 15739723 ⟵ “STATE APPROPRIATIONS | 15,739,723 | 16,011,237”
  - column:GENERAL OPERATIONS TOTAL: 15739723 ⟵ “GENERAL OPERATIONS TOTAL | 15,739,723 | 16,011,237”
  - column:TOTAL REVENUE: 15739723 ⟵ “TOTAL REVENUE | 15,739,723 | 16,011,237”
  - column:STUDENT TUITION AND FEES: 7450680 ⟵ “STUDENT TUITION AND FEES | 7,450,680 | 7,209,455”
  - column:GENERAL OPERATIONS TOTAL: 7450680 ⟵ “GENERAL OPERATIONS TOTAL | 7,450,680 | 7,209,455”
  - column:TOTAL REVENUE: 7450680 ⟵ “TOTAL REVENUE | 7,450,680 | 7,209,455”
  - column:OTHER SOURCES: 335250 ⟵ “OTHER SOURCES | 335,250 | 248,604”
  - column:STUDENT TUITION AND FEES: 129750 ⟵ “STUDENT TUITION AND FEES | 129,750 | 191,754”
  - column:GENERAL OPERATIONS TOTAL: 465000 ⟵ “GENERAL OPERATIONS TOTAL | 465,000 | 440,358”
  - column:TOTAL REVENUE: 465000 ⟵ “TOTAL REVENUE | 465,000 | 440,358”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 4200000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 4,200,000 | 4,200,000”
  - column:TOTAL REVENUE: 4200000 ⟵ “TOTAL REVENUE | 4,200,000 | 4,200,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 2000000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 2,000,000 | 1,500,000”
  - column:TOTAL REVENUE: 2000000 ⟵ “TOTAL REVENUE | 2,000,000 | 1,500,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 600000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 600,000 | 550,000”
  - column:TOTAL REVENUE: 600000 ⟵ “TOTAL REVENUE | 600,000 | 550,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 100000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 100,000 | 85,000”
  - column:TOTAL REVENUE: 100000 ⟵ “TOTAL REVENUE | 100,000 | 85,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 55000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 55,000 | 41,000”
  - column:TOTAL REVENUE: 55000 ⟵ “TOTAL REVENUE | 55,000 | 41,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 90000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 90,000 | 90,000”
  - column:TOTAL REVENUE: 90000 ⟵ “TOTAL REVENUE | 90,000 | 90,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 360000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 360,000 | 356,000”
  - column:TOTAL REVENUE: 360000 ⟵ “TOTAL REVENUE | 360,000 | 356,000”
  - column:OTHER SOURCES: 110000 ⟵ “OTHER SOURCES | 110,000 | 75,000”
  - … 8461 more rows
### `b4f21f5422b0bac7` Gordon State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.gordonstate.edu/documents/departments/budgets/fy25-original-budget-packet.pdf (sha256 f3fbaac97b1f)
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown, conflicting_sources:https://www.gordonstate.edu/documents/departments/budgets/fy24_original-budget-packet.pdf,https://www.gordonstate.edu/documents/departments/budgets/fy26-budget-booklet1.pdf,https://www.gordonstate.edu/documents/departments/bursars-office/coa_2627.pdf
- checks: {"columns": 11, "rows": 378}
  - column:STATE APPROPRIATIONS: 13661761 ⟵ “STATE APPROPRIATIONS | 13,661,761 | 15,739,723”
  - column:GENERAL OPERATIONS TOTAL: 13661761 ⟵ “GENERAL OPERATIONS TOTAL | 13,661,761 | 15,739,723”
  - column:TOTAL REVENUE: 13661761 ⟵ “TOTAL REVENUE | 13,661,761 | 15,739,723”
  - column:STUDENT TUITION AND FEES: 7205493 ⟵ “STUDENT TUITION AND FEES | 7,205,493 | 7,450,680”
  - column:GENERAL OPERATIONS TOTAL: 7205493 ⟵ “GENERAL OPERATIONS TOTAL | 7,205,493 | 7,450,680”
  - column:TOTAL REVENUE: 7205493 ⟵ “TOTAL REVENUE | 7,205,493 | 7,450,680”
  - column:OTHER SOURCES: 320000 ⟵ “OTHER SOURCES | 320,000 | 335,250”
  - column:STUDENT TUITION AND FEES: 129750 ⟵ “STUDENT TUITION AND FEES | 129,750 | 129,750”
  - column:GENERAL OPERATIONS TOTAL: 449750 ⟵ “GENERAL OPERATIONS TOTAL | 449,750 | 465,000”
  - column:TOTAL REVENUE: 449750 ⟵ “TOTAL REVENUE | 449,750 | 465,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 4909806 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 4,909,806 | 4,200,000”
  - column:TOTAL REVENUE: 4909806 ⟵ “TOTAL REVENUE | 4,909,806 | 4,200,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 1520000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 1,520,000 | 2,000,000”
  - column:TOTAL REVENUE: 1520000 ⟵ “TOTAL REVENUE | 1,520,000 | 2,000,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 670444 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 670,444 | 600,000”
  - column:TOTAL REVENUE: 670444 ⟵ “TOTAL REVENUE | 670,444 | 600,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 69240 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 69,240 | 100,000”
  - column:TOTAL REVENUE: 69240 ⟵ “TOTAL REVENUE | 69,240 | 100,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 48620 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 48,620 | 55,000”
  - column:TOTAL REVENUE: 48620 ⟵ “TOTAL REVENUE | 48,620 | 55,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 70000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 70,000 | 90,000”
  - column:TOTAL REVENUE: 70000 ⟵ “TOTAL REVENUE | 70,000 | 90,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 327270 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 327,270 | 360,000”
  - column:TOTAL REVENUE: 327270 ⟵ “TOTAL REVENUE | 327,270 | 360,000”
  - column:FUNDS FROM PRIOR YEAR: 361990 ⟵ “FUNDS FROM PRIOR YEAR | 361,990 | 0”
  - … 12164 more rows
### `dc56a22c77648b6f` Gordon State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.gordonstate.edu/documents/departments/budgets/fy24_original-budget-packet.pdf (sha256 e5d730981458)
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown, conflicting_sources:https://www.gordonstate.edu/documents/departments/budgets/fy25-original-budget-packet.pdf,https://www.gordonstate.edu/documents/departments/budgets/fy26-budget-booklet1.pdf,https://www.gordonstate.edu/documents/departments/bursars-office/coa_2627.pdf
- checks: {"columns": 11, "rows": 280}
  - column:STATE APPROPRIATIONS: 13548238 ⟵ “STATE APPROPRIATIONS | 13,548,238 | 13,661,761”
  - column:GENERAL OPERATIONS TOTAL: 13548238 ⟵ “GENERAL OPERATIONS TOTAL | 13,548,238 | 13,661,761”
  - column:TOTAL REVENUE: 13548238 ⟵ “TOTAL REVENUE | 13,548,238 | 13,661,761”
  - column:STUDENT TUITION AND FEES: 6781470 ⟵ “STUDENT TUITION AND FEES | 6,781,470 | 7,205,493”
  - column:GENERAL OPERATIONS TOTAL: 6781470 ⟵ “GENERAL OPERATIONS TOTAL | 6,781,470 | 7,205,493”
  - column:TOTAL REVENUE: 6781470 ⟵ “TOTAL REVENUE | 6,781,470 | 7,205,493”
  - column:OTHER SOURCES: 325000 ⟵ “OTHER SOURCES | 325,000 | 320,000”
  - column:STUDENT TUITION AND FEES: 205800 ⟵ “STUDENT TUITION AND FEES | 205,800 | 129,750”
  - column:GENERAL OPERATIONS TOTAL: 530800 ⟵ “GENERAL OPERATIONS TOTAL | 530,800 | 449,750”
  - column:TOTAL REVENUE: 530800 ⟵ “TOTAL REVENUE | 530,800 | 449,750”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 4976814 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 4,976,814 | 4,909,806”
  - column:TOTAL REVENUE: 4976814 ⟵ “TOTAL REVENUE | 4,976,814 | 4,909,806”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 1488000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 1,488,000 | 1,520,000”
  - column:TOTAL REVENUE: 1488000 ⟵ “TOTAL REVENUE | 1,488,000 | 1,520,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 650000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 650,000 | 670,444”
  - column:TOTAL REVENUE: 650000 ⟵ “TOTAL REVENUE | 650,000 | 670,444”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 77396 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 77,396 | 69,240”
  - column:TOTAL REVENUE: 77396 ⟵ “TOTAL REVENUE | 77,396 | 69,240”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 44500 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 44,500 | 48,620”
  - column:TOTAL REVENUE: 44500 ⟵ “TOTAL REVENUE | 44,500 | 48,620”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 35000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 35,000 | 70,000”
  - column:TOTAL REVENUE: 35000 ⟵ “TOTAL REVENUE | 35,000 | 70,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 390000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 390,000 | 327,270”
  - column:TOTAL REVENUE: 390000 ⟵ “TOTAL REVENUE | 390,000 | 327,270”
  - column:FUNDS FROM PRIOR YEAR: 430359 ⟵ “FUNDS FROM PRIOR YEAR | 430,359 | 361,990”
  - … 9776 more rows
### `11f26711674d52c8` Gwinnett Technical College — appeals 2024-25 [new] (labeled_in_source)
- source: https://gwinnetttech.edu/admissions-financial-aid/financial-aid/verification/ (sha256 7ccc98981b80)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “We also use CampusLogic for Satisfactory Academic Progress and Professional Judgment Appeals.”
### `83cf0286d26ba7e5` Gwinnett Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gwinnetttech.edu/admissions-financial-aid/financial-aid/satisfactory-academic-progress/ (sha256 2f975e521920)
- issues: semantic_review_required, conflicting_sources:https://gwinnetttech.edu/admissions-financial-aid/financial-aid/faqs-and-how-tos/,https://gwinnetttech.edu/wp-content/uploads/2025/12/SAPPolicyUpdatedSpring2023.pdf,https://gwinnetttech.edu/wp-content/uploads/2026/08/2026-2027-Dual-Enrollment-SAP-appeal-fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “SAP appeals will be completed through the Campus Logic portal at www.gwinnetttech.verifymyfafsa.com.”
  - sentence: sap_appeal ⟵ “You will need to log into Campus Logic, complete the SAP appeal within your tasks, upload your supporting documents, as well as your required Academic Plan.”
  - sentence: sap_appeal ⟵ “Your SAP appeal will not be reviewed until all items are submitted.”
  - sentence: sap_appeal ⟵ “Effective Spring 2025, students with approved SAP appeals will be allowed only one(1) additional opportunity to appeal if they fail to meet the terms of their probation.”
  - sentence: sap_appeal ⟵ “SAP Appeal Tips Please use the tips below for preparing the SAP Appeal.”
  - sentence: sap_appeal ⟵ “Education Plan Your SAP appeal will not be considered complete until the Education Plan is uploaded to Campus Logic.”
### `ad9e322d154f3772` Gwinnett Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gwinnetttech.edu/admissions-financial-aid/financial-aid/faqs-and-how-tos/ (sha256 c33c4c6551d1)
- issues: semantic_review_required, conflicting_sources:https://gwinnetttech.edu/admissions-financial-aid/financial-aid/satisfactory-academic-progress/,https://gwinnetttech.edu/wp-content/uploads/2025/12/SAPPolicyUpdatedSpring2023.pdf,https://gwinnetttech.edu/wp-content/uploads/2026/08/2026-2027-Dual-Enrollment-SAP-appeal-fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “We also use CampusLogic for Satisfactory Academic Progress and Professional Judgment Appeals.”
  - sentence: sap_appeal ⟵ “You must submit a SAP appeal if your status is Suspension or Maximum Timeframe.”
  - sentence: sap_appeal ⟵ “SAP appeals will be completed through the Campus Logic portal at www.gwinnetttech.verifymyfafsa.com.”
  - sentence: sap_appeal ⟵ “You will need to log into Campus Logic, complete the SAP appeal within your tasks, upload your supporting documents, as well as your required Academic Plan.”
  - sentence: sap_appeal ⟵ “Your SAP appeal will not be reviewed until all items are submitted.”
### `c3d34ae3e927cd5d` Gwinnett Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://gwinnetttech.edu/wp-content/uploads/2026/08/2026-2027-Dual-Enrollment-SAP-appeal-fillable.pdf (sha256 d0df9225f0ca)
- issues: semantic_review_required, conflicting_sources:https://gwinnetttech.edu/admissions-financial-aid/financial-aid/faqs-and-how-tos/,https://gwinnetttech.edu/admissions-financial-aid/financial-aid/satisfactory-academic-progress/,https://gwinnetttech.edu/wp-content/uploads/2025/12/SAPPolicyUpdatedSpring2023.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “All SAP Appeal documents must be submitted to the Financial Aid Office at one time.”
  - sentence: sap_appeal ⟵ “The SAP Appeal process takes up to two weeks.”
  - sentence: sap_appeal ⟵ “My documents will be reviewed by the SAP Appeals Committee; their decision is final.”
### `c87735b605d2f78c` Gwinnett Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://gwinnetttech.edu/admissions-financial-aid/financial-aid/ (sha256 65492505ea4a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Appeal A special circumstances appeal allows the Financial Aid Office to modify Financial Aid awards based on Special Circumstances.”
  - sentence: need_based_special_circumstances ⟵ “The special circumstances appeal provides the Financial Aid Administrator (“FAA”) discretion on a case-by-case basis to modify FAFSA reported parent/student financial data when there are “special circumstances”.”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances include: Recent unemployment of family member/s.”
### `d54cca342c4e4c6a` Gwinnett Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://gwinnetttech.edu/admissions-financial-aid/financial-aid/ (sha256 65492505ea4a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “We also use CampusLogic for Satisfactory Academic Progress and Professional Judgment Appeals.”
### `d7803d486db0e6b9` Gwinnett Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://gwinnetttech.edu/admissions-financial-aid/financial-aid/ (sha256 65492505ea4a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment and qualifying factors for special circumstances form the basis of the financial aid appeal process.”
### `fef6627392e2769d` Gwinnett Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gwinnetttech.edu/wp-content/uploads/2025/12/SAPPolicyUpdatedSpring2023.pdf (sha256 040b4458e2cf)
- issues: semantic_review_required, conflicting_sources:https://gwinnetttech.edu/admissions-financial-aid/financial-aid/faqs-and-how-tos/,https://gwinnetttech.edu/admissions-financial-aid/financial-aid/satisfactory-academic-progress/,https://gwinnetttech.edu/wp-content/uploads/2026/08/2026-2027-Dual-Enrollment-SAP-appeal-fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: sap_appeal ⟵ “Eligibility for continued financial aid will only be re-established as follows: a) the student subsequently meets the Satisfactory Academic Progress standards; or b) the student successfully appeals and is placed on Academic Plan status.”
  - sentence: sap_appeal ⟵ “Appeal Process Completion Rate and Cumulative GPA Appeals: Students placed on Suspension may appeal their Financial Aid status by submitting an electronically signed SAP Appeal Form through Dynamic Forms.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress - 3 Updated 02/23/2023 LAWRENCEVILLE I ALPHARETTA-NORTH FULTON Maximum Time Frame Appeal (updated starting Fall 2021): Students who are ineligible due to maximum hours should submit an electronically signed SAP Maximum Time Frame appeal through Dynamic Forms.”
  - sentence: sap_appeal ⟵ “Published on the Gwinnett Technical Website are SAP Appeal tips for students to utilize in preparing their appeal.”
  - sentence: sap_appeal ⟵ “Once an appeal is submitted to the Financial Aid Office it will be reviewed by the Satisfactory Academic Progress Appeals Committee.”
  - sentence: sap_appeal ⟵ “Committee members will review the appeal based upon the SAP appeal criteria.”
### `ef3cc74654ce6de2` Gwinnett Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://gwinnetttech.edu/admissions-financial-aid/financial-aid/cost-of-attendance/ (sha256 a7b0b58fd84e)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Tuition and Fees: 3524 ⟵ “Tuition and Fees | $3524”
  - column:Food and Housing: 27081 ⟵ “Food and Housing | $27081”
  - column:Books, Course Materials, Supplies & Equipment: 2676 ⟵ “Books, Course Materials, Supplies & Equipment | $2676”
  - column:Transportation: 2010 ⟵ “Transportation | $2010”
  - column:Miscellaneous Personal Expenses: 2600 ⟵ “Miscellaneous Personal Expenses | $2600”
### `424f062baa3f2808` Gwinnett Technical College — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://gwinnetttech.edu/admissions-financial-aid/dual-enrollment/accepted/ (sha256 a30ef6749869)
- issues: stale_year_label:2024-25
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 15 ⟵ “Dual Enrollment funding is available for up to 15 credits a semester, not to exceed 30 credits in total. Speak with your high school counselor for advisement.”
### `45e18e52571d521a` Kennesaw State University — appeals 2027-28 [new] (labeled_in_source)
- source: https://campus.kennesaw.edu/current-students/financial-aid/policies/awarding-policy.php (sha256 91701127c0d7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If your SAP status is Failure and you cannot mathematically attain SAP requirements, an appeal will not be permissible.”
  - sentence: sap_appeal ⟵ “How do you regain eligibility? | SAP Appeal – If mitigating circumstances during a specific term of enrollment prevented you from meeting the requirements, you may file a SAP Appeal.”
  - sentence: sap_appeal ⟵ “The appeal form must be submitted to the Office of Scholarships and Financial Aid within the prescribed dates as noted on the SAP Appeal Form.”
### `676a217aab13ad7b` Kennesaw State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://campus.kennesaw.edu/current-students/financial-aid/docs/financial-cost-worksheet.pdf (sha256 15aa852c1dd6)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "rows": 4}
  - column:Tuition: 2880 ⟵ “Tuition | $2,880 | $2,880 | $5,760”
  - column:Fees: 594 ⟵ “Fees | $594 | $594 | $1,188”
  - column:Books (May be less with Day One: 750 ⟵ “Books (May be less with Day One | $750 | $750 | $1,500”
  - column:Subtotal: 4224 ⟵ “Subtotal | $4,224 | $4,224 | $8,448”
  - column:Tuition: 2880 ⟵ “Tuition | $2,880 | $2,880 | $5,760”
  - column:Fees: 594 ⟵ “Fees | $594 | $594 | $1,188”
  - column:Books (May be less with Day One: 750 ⟵ “Books (May be less with Day One | $750 | $750 | $1,500”
  - column:Subtotal: 4224 ⟵ “Subtotal | $4,224 | $4,224 | $8,448”
  - column:Tuition: 5760 ⟵ “Tuition | $2,880 | $2,880 | $5,760”
  - column:Fees: 1188 ⟵ “Fees | $594 | $594 | $1,188”
  - column:Books (May be less with Day One: 1500 ⟵ “Books (May be less with Day One | $750 | $750 | $1,500”
  - column:Subtotal: 8448 ⟵ “Subtotal | $4,224 | $4,224 | $8,448”
### `65243f29a3fea0ea` Life University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.life.edu/wp-content/uploads/2026/05/26.27-Special-Circumstances.pdf (sha256 34f2a19f2cf5)
- issues: semantic_review_required, conflicting_sources:https://www.life.edu/admissions/financial-aid/forms/,https://www.life.edu/admissions/financial-aid/forms/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Appeal 2026-2027 Student’s Name_________________________________________________ Student ID Number________________________ Email Address (parent or student)__________________________________________________________________________ Last 4 Digits of Student SSN (If ID Number Unknown)___________________________________________________________ Certification Statement I certify th”
### `7454ec2c3c095239` Life University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.life.edu/admissions/financial-aid/forms/ (sha256 39b52745c8d1)
- issues: semantic_review_required, conflicting_sources:https://www.life.edu/admissions/financial-aid/forms/,https://www.life.edu/wp-content/uploads/2026/05/26.27-Special-Circumstances.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Appeal/PJ Form | This form is for students to request consideration of a special/unusual circumstance to be reviewed by our office.”
  - sentence: need_based_special_circumstances ⟵ “Dependency Override/Unusual Circumstances Appeal Form | This form is for students to request a change in their financial aid dependency status from dependent to independent.”
### `8d8d55e65a586da7` Life University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.life.edu/admissions/financial-aid/forms/ (sha256 90b5e95e68c6)
- issues: semantic_review_required, conflicting_sources:https://www.life.edu/admissions/financial-aid/forms/,https://www.life.edu/wp-content/uploads/2026/05/26.27-Special-Circumstances.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Appeal/PJ Form | This form is for students to request consideration of a special/unusual circumstance to be reviewed by our office.”
  - sentence: need_based_special_circumstances ⟵ “Dependency Override/Unusual Circumstances Appeal Form | This form is for students to request a change in their financial aid dependency status from dependent to independent.”
### `a2002bc1c8fc8186` Life University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.life.edu/satisfactory-academic-progress-sap-policy/ (sha256 ffbe464581cc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals must be submitted in writing using the SAP Appeal Form obtained by speaking with a Financial Aid Counselor and MUST include supporting third party documentation.”
### `f0c3b17896c5e6d2` Life University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.life.edu/admissions/financial-aid/forms/ (sha256 39b52745c8d1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Budget Increase Policy and Request | This form is for students wanting to request an increase to their cost of attendance for emergency expenses incurred out-of-pocket.”
  - sentence: budget_increase ⟵ “The Budget Increase Reference Sheet details what you will need to submit for each category.”
### `2067b685dc06c59a` Luther Rice College & Seminary — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.lutherrice.edu/tuition-and-aid/satisfactory-academic-progress (sha256 529e28f2d8e8)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.lutherrice.edu/tuition-and-aid/financial-aid-faq
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Conditions for an appeal can include personal injury, death of a relative, or other special circumstances.”
### `2c39457bf4b5ca02` Luther Rice College & Seminary — appeals 2024-25 [new] (labeled_in_title)
- source: https://www.lutherrice.edu/content/userfiles/files/Finance/2024-25%20PROFESSIONAL%20JUDGMENT%20FORM.pdf (sha256 e4c8e5b8f1db)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The letters of support should also include how they know you, how long they have known you, and contact information.  Loss of income or change in source of income (Check all that apply): □ Parent □ Student □ Student’s Spouse Loss or significant change in income: Parent/Student/Student’s Spouse: Submit proof of prior-year income and current-year expected income.”
  - sentence: need_based_special_circumstances ⟵ “These costs cannot be provided by other agencies.  Other extenuating circumstances: Submit a letter explaining your special circumstances.”
### `60257cb1ea85db40` Luther Rice College & Seminary — appeals 2024-25 [new] (labeled_in_title)
- source: https://www.lutherrice.edu/content/userfiles/files/Finance/2024-25%20PROFESSIONAL%20JUDGMENT%20FORM.pdf (sha256 e4c8e5b8f1db)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “2024-2025 PROFESSIONAL JUDGMENT FORM (Students with Special or Unusual Circumstances) Luther Rice Financial Aid Office will evaluate appeals on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “Student Name: _________________________________________________ Student ID: _________________________ Indicate the reason for requesting Professional Judgment consideration.”
  - sentence: professional_judgment ⟵ “All Professional Judgment requests must complete the FAFSA and verification process, if selected, by submitting all required verification papers along with copies of 2022 Federal tax return and W-2 information.”
### `df0cc64d25e9a4ce` Luther Rice College & Seminary — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.lutherrice.edu/tuition-and-aid/satisfactory-academic-progress (sha256 529e28f2d8e8)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “A student that previously received an SAP appeal before May 4, 2015 will be eligible to apply for another appeal within that same degree level if he becomes ineligible due to a failure to make SAP.”
### `ec52f89e94b9fcd2` Luther Rice College & Seminary — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lutherrice.edu/tuition-and-aid/financial-aid-faq (sha256 c4403f538c7b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “PROFESSIONAL JUDGMENT Professional Judgments (PJ) The Financial Aid Office facilitates a Professional Judgment application for a student if the situation (e.g., dependency override, income reduction, medical expenses etc.) dictates that an adjustment should be made to the student’s financial aid information.”
  - sentence: professional_judgment ⟵ “Types of Professional Judgments Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the estimated Cost of Attendance (COA) or in the EFC calculation.”
  - sentence: professional_judgment ⟵ “To request an appeal, please complete, sign, and submit the Professional Judgment Form with a letter of explanation and the required documentation found in each description, to the Financial Aid Office via My Secure File Transfer within MyCampus If you would rather mail or fax your documents, the contact information is below.”
### `f1bd0fe2d02d5413` Luther Rice College & Seminary — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lutherrice.edu/tuition-and-aid/financial-aid-faq (sha256 c4403f538c7b)
- issues: semantic_review_required, conflicting_sources:https://www.lutherrice.edu/tuition-and-aid/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have one or both a special circumstance and an unusual circumstance.”
### `67331878aca34e34` Luther Rice College & Seminary — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.lutherrice.edu/tuition-and-aid/cost-of-attendance (sha256 dce9af40ae76)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "rows": 4}
  - column:Personal Computer: 582 ⟵ “Personal Computer | $582 | Per Year”
  - column:Dependent (living with parent): 40 ⟵ “Dependent (living with parent) | $40 | Per Month”
  - column:Dependent (living with parent): 120 ⟵ “Dependent (living with parent) | $120 | Per Month”
  - column:Dependent (living with parent): 400 ⟵ “Dependent (living with parent) | $400 | Per Month”
  - column:Dependent (living with parent): 7 ⟵ “Dependent (living with parent) | $7 | Per Month”
  - column:Tuition/ On-Campus: 238 ⟵ “Tuition/ On-Campus | $238 | Per Hour”
  - column:Books & Course Materials: 179 ⟵ “Books & Course Materials | $179 | Per Class”
  - column:Tuition/ On-Campus: 238 ⟵ “Tuition/ On-Campus | $238 | Per Hour”
  - column:Books & Course Materials: 179 ⟵ “Books & Course Materials | $179 | Per Class”
  - column:Tuition/ On-Campus: 238 ⟵ “Tuition/ On-Campus | $238 | Per Hour”
  - column:Books & Course Materials: 215 ⟵ “Books & Course Materials | $215 | Per Class”
  - column:Tuition/ On-Campus: 238 ⟵ “Tuition/ On-Campus | $238 | Per Hour”
  - column:Books & Course Materials: 215 ⟵ “Books & Course Materials | $215 | Per Class”
  - column:Books & Course Materials: 192 ⟵ “Books & Course Materials | $192 | Per Class”
  - column:Independent/Dependent (not living with parent): 190 ⟵ “Independent/Dependent (not living with parent) | Personal/Misc. | $190 | Per Month”
  - column:Independent/Dependent (not living with parent): 292 ⟵ “Independent/Dependent (not living with parent) | Transportation | $292 | Per Month”
  - column:Independent/Dependent (not living with parent): 1798 ⟵ “Independent/Dependent (not living with parent) | Housing | $1,798 | Per Month”
  - column:Independent/Dependent (not living with parent): 602 ⟵ “Independent/Dependent (not living with parent) | Food | $602 | Per Month”
  - column:All Students (PhD Leadership): 652 ⟵ “All Students (PhD Leadership) | Tuition | $652 | Per Hour”
  - column:All Students (PhD Christian Scripture): 468 ⟵ “All Students (PhD Christian Scripture) | Tuition | $468 | Per Hour”
  - column:All Students (PhD Leadership): 317 ⟵ “All Students (PhD Leadership) | Books & Course Materials | $317 | Per Class”
  - column:All Programs: 195 ⟵ “All Programs | All Students | Fee | $195 | Per Class”
  - column:Associate: 465 ⟵ “Associate | All Students | Tuition/Distance Education | $465 | Per Hour”
  - column:Bachelor: 465 ⟵ “Bachelor | All Students | Tuition/Distance Education | $465 | Per Hour”
  - column:Master: 397 ⟵ “Master | All Students | Tuition/Distance Education | $397 | Per Hour”
  - … 2 more rows
### `7e90c36e9dbb3269` Mercer University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.mercer.edu/cost-of-attendance/working-adults-undergraduate/ (sha256 fbc9087c7154)
- issues: arrangement_unlabeled, conflicting_sources:https://financialaid.mercer.edu/cost-of-attendance/residential-undergraduate/
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - column:Tuition: 6984.0 ⟵ “Tuition | $6,984.00 | $6,984.00 | $13,968.00”
  - column:Fees: 250.0 ⟵ “Fees | $250.00 | $250.00 | $500.00”
  - column:Books & Supplies: 792.0 ⟵ “Books & Supplies | $792.00 | $792.00 | $1,584.00”
  - column:Housing*: 7074.0 ⟵ “Housing* | $7,074.00 | $7,074.00 | $14,148.00”
  - column:Food: 2326.5 ⟵ “Food | $2,326.50 | $2,326.50 | $4,653.00”
  - column:Transportation: 1962.0 ⟵ “Transportation | $1,962.00 | $1,962.00 | $3,924.00”
  - column:Personal: 1062.0 ⟵ “Personal | $1062.00 | $1062.00 | $2,124.00”
  - column:Total Estimated Cost of Attendance: 20450.5 ⟵ “Total Estimated Cost of Attendance | $20,450.50 | $20,450.50 | $40,973.00”
  - column:Tuition: 6984.0 ⟵ “Tuition | $6,984.00 | $6,984.00 | $13,968.00”
  - column:Fees: 250.0 ⟵ “Fees | $250.00 | $250.00 | $500.00”
  - column:Books & Supplies: 792.0 ⟵ “Books & Supplies | $792.00 | $792.00 | $1,584.00”
  - column:Housing*: 7074.0 ⟵ “Housing* | $7,074.00 | $7,074.00 | $14,148.00”
  - column:Food: 2326.5 ⟵ “Food | $2,326.50 | $2,326.50 | $4,653.00”
  - column:Transportation: 1962.0 ⟵ “Transportation | $1,962.00 | $1,962.00 | $3,924.00”
  - column:Personal: 1062.0 ⟵ “Personal | $1062.00 | $1062.00 | $2,124.00”
  - column:Total Estimated Cost of Attendance: 20450.5 ⟵ “Total Estimated Cost of Attendance | $20,450.50 | $20,450.50 | $40,973.00”
  - column:Tuition: 13968.0 ⟵ “Tuition | $6,984.00 | $6,984.00 | $13,968.00”
  - column:Fees: 500.0 ⟵ “Fees | $250.00 | $250.00 | $500.00”
  - column:Books & Supplies: 1584.0 ⟵ “Books & Supplies | $792.00 | $792.00 | $1,584.00”
  - column:Housing*: 14148.0 ⟵ “Housing* | $7,074.00 | $7,074.00 | $14,148.00”
  - column:Food: 4653.0 ⟵ “Food | $2,326.50 | $2,326.50 | $4,653.00”
  - column:Transportation: 3924.0 ⟵ “Transportation | $1,962.00 | $1,962.00 | $3,924.00”
  - column:Personal: 2124.0 ⟵ “Personal | $1062.00 | $1062.00 | $2,124.00”
  - column:Average Loan Fees**: 72.0 ⟵ “Average Loan Fees** |  |  | $72.00”
  - column:Total Estimated Cost of Attendance: 40973.0 ⟵ “Total Estimated Cost of Attendance | $20,450.50 | $20,450.50 | $40,973.00”
### `976dabc8cdbb86c1` Mercer University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.mercer.edu/cost-of-attendance/residential-undergraduate-24-25/ (sha256 a6fe9f89e4ac)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition*: 42012 ⟵ “Tuition* | $42,012”
  - column:Facility & Technology Fee: 300 ⟵ “Facility & Technology Fee | $300”
  - column:Housing**: 7412 ⟵ “Housing** | $7,412”
  - column:Food**: 7744 ⟵ “Food** | $7,744”
  - column:Total Estimated Annual Direct Costs: 57468 ⟵ “Total Estimated Annual Direct Costs | $57,468”
### `a4271a092d00333b` Mercer University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.mercer.edu/cost-of-attendance/residential-undergraduate/ (sha256 f9ec8d139654)
- issues: conflicting_sources:https://financialaid.mercer.edu/cost-of-attendance/working-adults-undergraduate/
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition*: 44784 ⟵ “Tuition* | $44,784”
  - column:Facility & Technology Fee: 500 ⟵ “Facility & Technology Fee | $500”
  - column:Housing**: 8046 ⟵ “Housing** | $8,046”
  - column:Food**: 7866 ⟵ “Food** | $7,866”
  - column:Total Estimated Annual Direct Costs: 61196 ⟵ “Total Estimated Annual Direct Costs | $61,196”
### `f85c215f02b4f195` Mercer University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.mercer.edu/cost-of-attendance/residential-undergraduate-25-26/ (sha256 b9ce088bd4ce)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition*: 43270 ⟵ “Tuition* | $43,270”
  - column:Facility & Technology Fee: 300 ⟵ “Facility & Technology Fee | $300”
  - column:Housing**: 7587 ⟵ “Housing** | $7,587”
  - column:Food**: 7758 ⟵ “Food** | $7,758”
  - column:Total Estimated Annual Direct Costs: 58915 ⟵ “Total Estimated Annual Direct Costs | $58,915”
### `3580d84f4f429c7f` Middle Georgia State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mga.edu/financial-aid/appeals/special-circumstances-appeal.php (sha256 00636a386f24)
- issues: semantic_review_required, conflicting_sources:https://www.mga.edu/financial-aid/appeals/unusual-circumstance-appeal.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The following conditions may result in an SAI adjustment: Loss of employment due to no fault of your own An unintentional reduction in work hours Overall reduction in your family’s total income due to death, divorce or other personal circumstances Other changes or adjustments that impact a student's cost or ability to pay for college If you meet any of the above criteria, you may apply to have you”
### `3fcd062af38923b8` Middle Georgia State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mga.edu/financial-aid/appeals/satisfactory-academic-progress-appeal.php (sha256 2ed066ee80ed)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you are not meeting all components of the SAP Policy, you have the opportunity to submit a SAP Appeal.”
### `7907cbcc10ac2ad2` Middle Georgia State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mga.edu/financial-aid/appeals/unusual-circumstance-appeal.php (sha256 7dfe3373f3d3)
- issues: semantic_review_required, conflicting_sources:https://www.mga.edu/financial-aid/appeals/special-circumstances-appeal.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The Office of Financial Aid will exercise professional judgment in determining if extenuating circumstances exist based on information and documentation provided from the student.”
### `c8217934dbc0a293` Middle Georgia State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mga.edu/financial-aid/appeals/unusual-circumstance-appeal.php (sha256 7dfe3373f3d3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances include the following scenarios but are not limited to: Documented parental abandonment.”
  - sentence: need_based_special_circumstances ⟵ “Parental incarceration or institutionalization due to mental incapacity NOTE: The following factors are not considered an unusual circumstance: Parents refuse to contribute to your education.”
  - sentence: need_based_special_circumstances ⟵ “Submitting An Unusual Circumstance Appeal You can submit an Unusual Circumstances Appeal to explain your unique situation using the following instructions: Submitting an Appeal.”
  - sentence: need_based_special_circumstances ⟵ “Other relevant data that explains your special circumstance.”
### `02f72abc4390945c` Middle Georgia State University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mga.edu/financial-aid/cost-of-attendance.php (sha256 74752433b1bd)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:FY25 Tuition: 5220.0 ⟵ “FY25 Tuition | $ 5,220.00”
  - column:Mandatory Fees: 862.0 ⟵ “Mandatory Fees | $ 862.00”
  - column:Housing: 7618.0 ⟵ “Housing | $ 7,618.00”
  - column:Food: 3800.0 ⟵ “Food | $ 3,800.00”
  - column:Books: 1000.0 ⟵ “Books | $ 1,000.00”
  - column:Supplies: 250.0 ⟵ “Supplies | $ 250.00”
  - column:Federal Direct Loan Fees*: 78.0 ⟵ “Federal Direct Loan Fees* | $ 78.00”
  - column:Miscelleneous Expenses: 3150.0 ⟵ “Miscelleneous Expenses | $ 3,150.00”
  - column:Transportation: 1945.0 ⟵ “Transportation | $ 1,945.00”
  - column:Total Cost of Attendance for 2 semesters: 23923.0 ⟵ “Total Cost of Attendance for 2 semesters | $ 23,923.00”
### `1c44b754e078212a` Middle Georgia State University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.mga.edu/financial-aid/cost-of-attendance.php (sha256 74752433b1bd)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:FY25 Tuition: 19410.0 ⟵ “FY25 Tuition | $ 19,410.00”
  - column:Mandatory Fees: 862.0 ⟵ “Mandatory Fees | $ 862.00”
  - column:Housing: 7618.0 ⟵ “Housing | $ 7,618.00”
  - column:Food: 3800.0 ⟵ “Food | $ 3,800.00”
  - column:Books: 1000.0 ⟵ “Books | $ 1,000.00”
  - column:Supplies: 250.0 ⟵ “Supplies | $ 250.00”
  - column:Federal Direct Loan Fees*: 78.0 ⟵ “Federal Direct Loan Fees* | $ 78.00”
  - column:Miscelleneous Expenses: 3150.0 ⟵ “Miscelleneous Expenses | $ 3,150.00”
  - column:Transportation: 3889.0 ⟵ “Transportation | $ 3,889.00”
  - column:Total Cost of Attendance for 2 semesters: 40057.0 ⟵ “Total Cost of Attendance for 2 semesters | $ 40,057.00”
### `0af48f560d0d2415` Middle Georgia State University — transfer_policies 2024-25 [new] (labeled_in_source)
- source: https://www.mga.edu/academics/docs/transfer-agreements/MGA_TCSG_MOU.pdf (sha256 1ff225f71528)
- issues: stale_year_label:2024-25
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “Any student admitted to MGA for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 8.”
### `c23b4f731cfc3372` Morehouse College — appeals 2026-27 [new] (source_unlabeled)
- source: https://morehouse.edu/aid/financial-aid/scholarships (sha256 940881fad86b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “AUTOMATIC SCHOLARSHIP MATCH (NEWLY ADMITTED STUDENTS) Newly admitted Freshmen students will be automatically considered for scholarships based on their existing admissions application, except in special circumstances where they may be contacted directly for further information or directed to the scholarship portal.”
### `1aca45fcaa64c77e` Morehouse College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://morehouse.edu/aid/student-accounts/cost-of-attendance-2025-2026 (sha256 b8b02cedbae0)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - off_campus_not_with_family:Tuition: 30122.0 ⟵ “Tuition | $30,122.00 | $12,422.00”
  - off_campus_not_with_family:Student Fees: 4012.0 ⟵ “Student Fees | $4,012.00 | $4,012.00”
  - off_campus_not_with_family:Food: 4012.0 ⟵ “Food | $4,012.00 | $4,012.00”
  - off_campus_not_with_family:Housing: 12150.0 ⟵ “Housing | $12,150.00 | $12,150.00”
  - off_campus_not_with_family:Books & Supplies: 2000.0 ⟵ “Books & Supplies | $2,000.00 | $1,000.00”
  - off_campus_not_with_family:Transportation: 2736.0 ⟵ “Transportation | $2,736.00 | $1,368.00”
  - off_campus_not_with_family:Loan Fees: 200.0 ⟵ “Loan Fees | $200.00 | $-”
  - off_campus_not_with_family:Personal/Miscellaneous Fees: 3756.0 ⟵ “Personal/Miscellaneous Fees | $3,756.00 | $-”
  - off_campus_not_with_family:Total Estimated Cost: 58988.0 ⟵ “Total Estimated Cost | $58,988.00 | $34,964.00”
  - off_campus_not_with_family:Tuition: 12422.0 ⟵ “Tuition | $30,122.00 | $12,422.00”
  - off_campus_not_with_family:Student Fees: 4012.0 ⟵ “Student Fees | $4,012.00 | $4,012.00”
  - off_campus_not_with_family:Food: 4012.0 ⟵ “Food | $4,012.00 | $4,012.00”
  - off_campus_not_with_family:Housing: 12150.0 ⟵ “Housing | $12,150.00 | $12,150.00”
  - off_campus_not_with_family:Books & Supplies: 1000.0 ⟵ “Books & Supplies | $2,000.00 | $1,000.00”
  - off_campus_not_with_family:Transportation: 1368.0 ⟵ “Transportation | $2,736.00 | $1,368.00”
  - off_campus_not_with_family:Total Estimated Cost: 34964.0 ⟵ “Total Estimated Cost | $58,988.00 | $34,964.00”
### `6d326904209b42cf` Morehouse College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://morehouse.edu/aid/student-accounts/cost-of-attendance (sha256 9dfe3958f891)
- issues: ambiguous_year_labels
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - off_campus_not_with_family:Tuition: 31026.0 ⟵ “Tuition | $31,026.00 | $12,794.00”
  - off_campus_not_with_family:Student Fees: 4258.0 ⟵ “Student Fees | $4,258.00 | $4258.00”
  - off_campus_not_with_family:Food: 4092.0 ⟵ “Food | $4,092.00 | $4,092.00”
  - off_campus_not_with_family:Housing: 11520.0 ⟵ “Housing | $11,520.00 | $11,520.00”
  - off_campus_not_with_family:Books & Supplies: 2000.0 ⟵ “Books & Supplies | $2,000.00 | $1,000.00”
  - off_campus_not_with_family:Transportation: 2880.0 ⟵ “Transportation | $2,880.00 | $2,880.00”
  - off_campus_not_with_family:Loan Fees: 200.0 ⟵ “Loan Fees | $200.00 | $-”
  - off_campus_not_with_family:Personal/Miscellaneous Fees: 3684.0 ⟵ “Personal/Miscellaneous Fees | $3,684.00 | $-”
  - off_campus_not_with_family:Total Estimated Cost: 59660.0 ⟵ “Total Estimated Cost | $59,660.00 | $36,544.00”
  - off_campus_not_with_family:Tuition: 12794.0 ⟵ “Tuition | $31,026.00 | $12,794.00”
  - off_campus_not_with_family:Student Fees: 4258.0 ⟵ “Student Fees | $4,258.00 | $4258.00”
  - off_campus_not_with_family:Food: 4092.0 ⟵ “Food | $4,092.00 | $4,092.00”
  - off_campus_not_with_family:Housing: 11520.0 ⟵ “Housing | $11,520.00 | $11,520.00”
  - off_campus_not_with_family:Books & Supplies: 1000.0 ⟵ “Books & Supplies | $2,000.00 | $1,000.00”
  - off_campus_not_with_family:Transportation: 2880.0 ⟵ “Transportation | $2,880.00 | $2,880.00”
  - off_campus_not_with_family:Total Estimated Cost: 36544.0 ⟵ “Total Estimated Cost | $59,660.00 | $36,544.00”
### `bd5f09cc520d3e4a` Morehouse College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://morehouse.edu/aid/student-accounts/cost-of-attendance/2024-2025-cost-of-attendance (sha256 5e4e56952493)
- issues: components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": false, "rows": 9}
  - off_campus_not_with_family:Tuition: 28984.0 ⟵ “Tuition | $28,984.00 | $11,544.00”
  - off_campus_not_with_family:Student Fees: 3929.0 ⟵ “Student Fees | $3,929.00 | $3,929.00”
  - off_campus_not_with_family:Food: 3858.0 ⟵ “Food | $3,858.00 | $3,858.00”
  - off_campus_not_with_family:Housing: 12420.0 ⟵ “Housing | $12,420.00 | $12,420.00”
  - off_campus_not_with_family:Books & Supplies: 2000.0 ⟵ “Books & Supplies | $2,000.00 | $1,000.00”
  - off_campus_not_with_family:Transportation: 2736.0 ⟵ “Transportation | $2,736.00 | $1,368.00”
  - off_campus_not_with_family:Loan Fees: 200.0 ⟵ “Loan Fees | $200.00 | $0.00”
  - off_campus_not_with_family:Personal/Miscellaneous Fees: 1306.0 ⟵ “Personal/Miscellaneous Fees | $1,306.00 | $0.00”
  - off_campus_not_with_family:Total Estimated Cost: 55413.0 ⟵ “Total Estimated Cost | $55,413.00 | $34,519.00”
  - off_campus_not_with_family:Tuition: 11544.0 ⟵ “Tuition | $28,984.00 | $11,544.00”
  - off_campus_not_with_family:Student Fees: 3929.0 ⟵ “Student Fees | $3,929.00 | $3,929.00”
  - off_campus_not_with_family:Food: 3858.0 ⟵ “Food | $3,858.00 | $3,858.00”
  - off_campus_not_with_family:Housing: 12420.0 ⟵ “Housing | $12,420.00 | $12,420.00”
  - off_campus_not_with_family:Books & Supplies: 1000.0 ⟵ “Books & Supplies | $2,000.00 | $1,000.00”
  - off_campus_not_with_family:Transportation: 1368.0 ⟵ “Transportation | $2,736.00 | $1,368.00”
  - off_campus_not_with_family:Loan Fees: 0.0 ⟵ “Loan Fees | $200.00 | $0.00”
  - off_campus_not_with_family:Personal/Miscellaneous Fees: 0.0 ⟵ “Personal/Miscellaneous Fees | $1,306.00 | $0.00”
  - off_campus_not_with_family:Total Estimated Cost: 34519.0 ⟵ “Total Estimated Cost | $55,413.00 | $34,519.00”
### `84fbef34e91ff791` Morris Brown College — appeals 2024-25 [new] (labeled_in_source)
- source: https://morrisbrown.edu/financial-aid/ (sha256 d57b8615bc52)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Refers to the financial situations that justify an aid administrator adjusting data elements in the Cost of Attendance (COA) or Expected Family Contribution (EFC) calculation (SAI starting in 2024-2025).”
### `8bc5d133baa34c9e` Morris Brown College — appeals 2024-25 [new] (labeled_in_source)
- source: https://morrisbrown.edu/financial-aid/ (sha256 d57b8615bc52)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “Financial Aid Suspension is a status assigned to a student who has not met the requirements for Satisfactory Academic Progress and has not been granted an appeal or a student who was on Financial Aid Probation and failed to meet Satisfactory Academic Progress or the requirements of the established academic plan and will not be eligible to receive Title IV funds.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation is a status assigned to a student who fails to make satisfactory academic progress for a subsequent payment period and who has appealed and has had eligibility for aid reinstated.”
  - sentence: sap_appeal ⟵ “These may include, but are not limited to, the following: Student illness or injury Family member illness, injury, or death Students who appeal must complete MBC’s SAP Appeal Request Form within 14 days of notification of suspension.”
  - sentence: sap_appeal ⟵ “Appeals are reviewed by MBC’s SAP Appeal Committee prior to the start of the upcoming semester.”
  - sentence: sap_appeal ⟵ “As part of the appeal process, the SAP Appeal Committee may implement any of these three options: Approval- based on circumstances and the student can mathematically meet the general SAP standards by the end of the probationary period.”
  - sentence: sap_appeal ⟵ “APPEAL PROCEDURES: How to appeal: Complete a SAP appeal form (the link to the DocuSign form is included in the Notification) Appeal is due to the Financial Aid Office within fourteen (14) calendar days of notification.”
### `cb0e23c9e2217ae1` Morris Brown College — appeals 2024-25 [new] (labeled_in_source)
- source: https://morrisbrown.edu/financial-aid/ (sha256 d57b8615bc52)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “This section walks you through FAFSA submission, eligibility requirements, and professional judgment requests for special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “Visit FAFSA Assistance Professional Judgments Students may pursue an adjustment to their financial aid based on special and/or unusual circumstances.”
  - sentence: professional_judgment ⟵ “Morris Brown College will review and use professional judgment to make adjustments to student’s financial aid that request them, provided sufficient documentation is gathered to support the decision.”
  - sentence: professional_judgment ⟵ “There are two types of Professional Judgments: Unusual Circumstances Refers to conditions that justify an aid administrator making an adjustment to a student’s dependency status.”
### `718414bd6946d8c6` North Georgia Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://northgatech.edu/wp-content/uploads/2026/07/SAP-FAQ-web.pdf (sha256 c047864f30e7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “For more information on SAP appeals, please contact a Financial Aid Advisor.”
### `bd6944512bdb3fc9` North Georgia Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://northgatech.edu/wp-content/uploads/2026/07/SAP-FAQ-web.pdf (sha256 c047864f30e7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “As set forth in the student catalog, North Georgia Technical College does not discriminate on the basis of race, color, creed, national or ethnic origin, gender identification, religion, disability, age, political affiliation or belief, genetic information, disabled veteran, veteran status, or citizenship status (except in those special circumstances permitted or mandated by law).”
### `411af010e2aa55ca` Oconee Fall Line Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://oftc.edu/admissions/financial-aid/ (sha256 5b4ae6fd77d1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If the student does not meet financial aid standards during the warning term, he/she will be placed on suspension. padding settings settings Financial Aid Appeal Process SAP (Satisfactory Academic Progress) Appeal Students must maintain a cumulative GPA of 2.0 or higher on a 4.0 scale that includes all credit courses appearing on the academic transcript.”
  - sentence: sap_appeal ⟵ “Appeals for Satisfactory Academic Progress must be based on specific extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Academic Plan Students will be given an academic plan IF the committee approves the SAP appeal.”
  - sentence: sap_appeal ⟵ “The student would need to submit another SAP Appeal to request their aid be reinstated or students can submit up to 2 SAP Appeal Forms.”
### `677c6684505c80f7` Oconee Fall Line Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://oftc.edu/admissions/financial-aid/ (sha256 5b4ae6fd77d1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “Professional Judgment Appeal Professional judgment is the ability of a financial aid administrator to recalculate the student’s financial aid eligibility due to special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “Separation or divorce which occurred after applying for financial aid Death of parent or spouse which occurred after applying for financial aid In order to start the Professional Judgment process, a request must come from the student.”
  - sentence: professional_judgment ⟵ “Once the student has requested that Professional Judgment be performed, the student is given an OFTC Professional Judgment Appeal Form.”
  - sentence: professional_judgment ⟵ “This form has instructions and a list of documents that must be presented to the Financial Aid Office before the Professional Judgment Appeal can be completed.”
  - sentence: professional_judgment ⟵ “The student must complete and submit the FAFSA, the Verification Worksheet, tax transcripts for student and parents (if dependent), Professional Judgment Appeal Form, and documents that support the appeal.”
  - sentence: professional_judgment ⟵ “On the Professional Judgment Appeal Form, the student must provide income earned from different sources up till then and projected total income for the entire year.”
### `c62ae29150e639db` Oconee Fall Line Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: http://oftc.edu/admissions/financial-aid/ (sha256 8b49893ea6ff)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “The financial aid administrator, under federal law, has the authority to take these special or unusual circumstances into consideration and make changes to the student’s financial aid application.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are situations that may occur that are not addressed in the application process.”
  - sentence: need_based_special_circumstances ⟵ “Some common special circumstances that may occur are: Separation from employment due to layoff, termination or disability Excessive non-reimbursed medical and/or dental expenses Reduction of untaxed income source such as child support, disability benefits, etc.”
### `bd5782751384fe07` Oconee Fall Line Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://oftc.edu/admissions/tuition-fees/ (sha256 fc7a7315e702)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Tuition and Fees: 3380.0 ⟵ “Tuition and Fees | $3,380.00”
  - column:Food and Housing: 10953.0 ⟵ “Food and Housing | $10,953.00”
  - column:Books, Course Materials, Supplies and Equipment: 1558.0 ⟵ “Books, Course Materials, Supplies and Equipment | $1,558.00”
  - column:Transportation: 1005.0 ⟵ “Transportation | $1,005.00”
  - column:Miscellaneous Personal Expenses: 1300.0 ⟵ “Miscellaneous Personal Expenses | $1,300.00”
### `2be31a4aee3a8ac7` Ogeechee Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ogeecheetech.edu/admissions/academic-standing (sha256 5fc8eafe2bbc)
- issues: semantic_review_required, conflicting_sources:https://www.ogeecheetech.edu/financial-aid/financial-aid-fast-facts
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Academic Appeal Ogeechee Technical College Faculty and Administrative Staff have the right and responsibility to exercise professional judgment in making decisions about student performance and progress.”
### `4372a6dbdfc54cb5` Ogeechee Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ogeecheetech.edu/financial-aid/sap (sha256 e1a4570950d6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “The SAP Appeals Reviewer will review the appeals.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Reviewer will notify the student of the decision.”
  - sentence: sap_appeal ⟵ “PROBATION - OT: Financial aid probation is a status assigned to a student who fails to make satisfactory academic progress (after a warning period) and who has appealed and has his/her Financial Aid reinstated for one term.”
  - sentence: sap_appeal ⟵ “PROBATION - AP(ACADEMIC PLAN): Financial aid AP-probation is a status assigned to a student who fails to make satisfactory academic progress (after a warning period) and who has appealed and who has completed an academic plan and has his/her Financial Aid reinstated for more than one term, but not to exceed three terms.”
### `77ba88d70ce66b00` Ogeechee Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ogeecheetech.edu/financial-aid/financial-aid-fast-facts (sha256 290560e26567)
- issues: semantic_review_required, conflicting_sources:https://www.ogeecheetech.edu/admissions/academic-standing
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Click HERE for a Professional Judgment/Financial Aid Appeal.”
### `63d2d693b08f4ede` Oglethorpe University — admissions_metrics 2021-22 [new] (labeled_in_source)
- source: https://oglethorpe.edu/wp-content/uploads/2024/12/CDS-2021-2022-Oglethorpe-University.pdf (sha256 b3a861836750)
- issues: stale_year_label:2021-22
- checks: {"fields": ["act_25", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_75", "sat_math_25", "sat_math_75", "sat_reading_25", "sat_reading_75"]}
  - applications: 2277 ⟵ “Total first-time, first-year (degree-seeking) who applied                         2277”
  - admits: 1851 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                   1851”
  - enrolled: 404 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                        404”
  - sat_composite_25..75: [1080, 1270] ⟵ “SAT Composite                                 1080                1270”
  - sat_reading_25..75: [540, 660] ⟵ “SAT Evidence-Based Reading and   540                 660”
  - sat_math_25..75: [530, 620] ⟵ “SAT Math                                    530                 620”
  - act_25..75: [24, 30] ⟵ “ACT Composite                                24                  30”
### `2b49bd9473362c52` Oglethorpe University — appeals 2026-27 [new] (source_unlabeled)
- source: https://oglethorpe.edu/academics/bulletin/institutional-policies-procedures-and-requirements/ (sha256 ec614d0de828)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Faculty members are strongly advised to exercise their best professional judgment concerning student-faculty relationships and to consider that intimate relations with students, even of a non-sexual nature, can be fraught with difficulties and the appearance of impropriety. 3.4.4.”
### `9312911aa8ecbee0` Oglethorpe University — appeals 2026-27 [new] (source_unlabeled)
- source: https://oglethorpe.edu/academics/bulletin/institutional-policies-procedures-and-requirements/ (sha256 ec614d0de828)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Requests for exceptions to this requirement may be granted under special circumstances.”
### `998256f0e54acb44` Oglethorpe University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://oglethorpe.edu/admission/apply/placements-and-credits/advanced-placement/ (sha256 a8a1301d9de4)
- issues: rows_without_score
- checks: {"distinct_exams": 35, "equivalencies": 35, "rows_without_score": 35}
  - equivalencies[AP-2-D-ART-DESIGN|None]:  ⟵ “ | Studio Art (2-D, 3-D, or Drawing) | 4 | Elective credit in art (studio)”
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “ | Art History | 4 | Elective credit in art (history)”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “ | Music Theory | 4 | Elective credit in music”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “ | English Language and Composition | 4 | Elective credit”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “ | English Literature and Composition | 4 | Elective credit”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “ | African American Studies | 4 | AAS 100 Introduction to African American Studies”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|None]:  ⟵ “ | Comparative Government and Politics | 4 | Elective credit in politics”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “ | European History | 4 | Elective credit in history”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “ | Human Geography | 4 | Elective credit”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “ | Macroeconomics | 4 | ECO 122 Principles of Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “ | Microeconomics | 4 | ECO 120 Principles of Microeconomics”
  - equivalencies[AP-PSYCHOLOGY|None]:  ⟵ “ | Psychology | 4 | PSY 101 Introduction to Psychology”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|None]:  ⟵ “ | United States Government and Politics | 4 | POL 101 Introduction to American Politics”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “ | United States History | 4 | Elective credit in history”
  - equivalencies[AP-WORLD-HISTORY-MODERN|None]:  ⟵ “ | World History | 4 | Elective credit in history”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “ | Calculus AB | 4 | MAT 131 Calculus I”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “ | Calculus BC | 4 | MAT 132 Calculus II”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “ | Computer Science A | 4 | CSC 201 Introduction to Programming”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “ | Computer Science Principles | 4 | Elective credit”
  - equivalencies[AP-PRECALCULUS|None]:  ⟵ “ | Precalculus | 4 | MAT-125 Precalculus”
  - equivalencies[AP-STATISTICS|None]:  ⟵ “ | Statistics | 4 | MAT 111 Statistics”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “ | Biology | 5 | GEN 102 Natural Science: Biological Science”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “ | Chemistry | 5 | CHM 101 General Chemistry I, CHM 101L General Chemistry I Lab”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “ | Environmental Science | 4 | Elective credit”
  - equivalencies[AP-PHYSICS-1|None]:  ⟵ “ | Physics 1 | 5 | PHY 101 General Physics I, PHY 101L Intro Physics Lab I”
  - … 10 more rows
### `f4465814cddef9d8` Oglethorpe University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://oglethorpe.edu/admission/apply/placements-and-credits/international-baccalaureate-ib-diploma/ (sha256 363cced5edaf)
- issues: rows_without_score
- checks: {"distinct_exams": 12, "equivalencies": 12, "rows_without_score": 12}
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | 4 | Elective credit in economics”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | 4 | Elective credit”
  - equivalencies[IB-GLOBAL-POLITICS|None]:  ⟵ “Global Politics | 4 | Elective credit in politics”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History | 4 | Elective credit in history”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | 4 | PSY 101 Introduction to Psychology”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | 5 | GEN 102 Natural Science: Biological Science”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | 5 | CHM 101 General Chemistry InCHM 101L General Chemistry I Lab”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | 4 | CSC 201 Introduction to Programming”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Physics | 6 | PHY 201 College Physics PHY 101L Intro Physics Lab I”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|None]:  ⟵ “Environmental Systems and Societies | 4 | Elective credit”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | 4 | Elective credit in music”
  - equivalencies[IB-VISUAL-ARTS|None]:  ⟵ “Visual Arts | 4 | Elective credit in art”
### `bb089052d5d57263` Paine College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://paine.edu/apply/ (sha256 59b03a4d47a6)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "rows": 6}
  - on_campus:Tuition: 13467.0 ⟵ “Tuition | $13,467.00 | $13,467.00 | $13,467.00 | $7,800.00”
  - on_campus:Technology and Admin: 1890.0 ⟵ “Technology and Admin | $1,890.00 | $1,890.00 | $1,890.00 | $500.00”
  - on_campus:Books: 1500.0 ⟵ “Books | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00”
  - on_campus:Room: 3136.0 ⟵ “Room | $3,136.00 | $0.00 | $0.00 | $0.00”
  - on_campus:Board: 5375.0 ⟵ “Board | $5,375.00 | $0.00 | $0.00 | $0.00”
  - on_campus:Totals: 25368.0 ⟵ “Totals | $25,368.00 | $16,857.00 | $16,857.00 | $9,800.00”
  - off_campus_not_with_family:Tuition: 13467.0 ⟵ “Tuition | $13,467.00 | $13,467.00 | $13,467.00 | $7,800.00”
  - off_campus_not_with_family:Technology and Admin: 1890.0 ⟵ “Technology and Admin | $1,890.00 | $1,890.00 | $1,890.00 | $500.00”
  - off_campus_not_with_family:Books: 1500.0 ⟵ “Books | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00”
  - off_campus_not_with_family:Room: 0.0 ⟵ “Room | $3,136.00 | $0.00 | $0.00 | $0.00”
  - off_campus_not_with_family:Board: 0.0 ⟵ “Board | $5,375.00 | $0.00 | $0.00 | $0.00”
  - off_campus_not_with_family:Totals: 16857.0 ⟵ “Totals | $25,368.00 | $16,857.00 | $16,857.00 | $9,800.00”
  - with_parents_or_family:Tuition: 13467.0 ⟵ “Tuition | $13,467.00 | $13,467.00 | $13,467.00 | $7,800.00”
  - with_parents_or_family:Technology and Admin: 1890.0 ⟵ “Technology and Admin | $1,890.00 | $1,890.00 | $1,890.00 | $500.00”
  - with_parents_or_family:Books: 1500.0 ⟵ “Books | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00”
  - with_parents_or_family:Room: 0.0 ⟵ “Room | $3,136.00 | $0.00 | $0.00 | $0.00”
  - with_parents_or_family:Board: 0.0 ⟵ “Board | $5,375.00 | $0.00 | $0.00 | $0.00”
  - with_parents_or_family:Totals: 16857.0 ⟵ “Totals | $25,368.00 | $16,857.00 | $16,857.00 | $9,800.00”
  - column:Tuition: 7800.0 ⟵ “Tuition | $13,467.00 | $13,467.00 | $13,467.00 | $7,800.00”
  - column:Technology and Admin: 500.0 ⟵ “Technology and Admin | $1,890.00 | $1,890.00 | $1,890.00 | $500.00”
  - column:Books: 1500.0 ⟵ “Books | $1,500.00 | $1,500.00 | $1,500.00 | $1,500.00”
  - column:Room: 0.0 ⟵ “Room | $3,136.00 | $0.00 | $0.00 | $0.00”
  - column:Board: 0.0 ⟵ “Board | $5,375.00 | $0.00 | $0.00 | $0.00”
  - column:Totals: 9800.0 ⟵ “Totals | $25,368.00 | $16,857.00 | $16,857.00 | $9,800.00”
### `3e071c9dc9fc6a8c` Piedmont University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.piedmont.edu/wp-content/uploads/2025/05/COA-2025-26.pdf (sha256 aec7f455b400)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 7, "rows": 11}
  - column:$32,760: 32760 ⟵ “$32,760 | $32,760 | $32,760 | $25,580 | $25,580 | $15,780 | $15,780”
  - column:Books, Course Materials, Supplies,: 1260 ⟵ “Books, Course Materials, Supplies, | $1,260 | $1,260 | $1,260 | 1260 | 1260 | $1,260 | $1,260”
  - column:Living Expenses (Housing & Food): 10668 ⟵ “Living Expenses (Housing & Food) | $10,668 | $7,918 | $13,800 | $10,668 | $7,918 | $10,668 | $7,918”
  - column:Transportation (average): 2000 ⟵ “Transportation (average) | $2,000 | $2,000 | $2,000 | $2,000 | 2000 | $600 | $600”
  - column:Personal/Miscellaneous: 1800 ⟵ “Personal/Miscellaneous | $1,800 | $1,800 | $1,800 | $1,800 | 1800 | $1,800 | $1,800”
  - column:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96 | $96 | 96 | $96 | $96”
  - column:$48,584: 45834 ⟵ “$48,584 | $45,834 | $51,716 | $41,404 | $38,654 | $30,204 | $27,454”
  - column:Counseling: 2 ⟵ “Counseling | 2 | Education (9 hours) | 3 | Pathology (9 hours) | 3 (6 hours) | 3 | Portion (12 hours) | Direct costs would be tuition and fees.”
  - column:Tuition & Fees: 18480 ⟵ “Tuition & Fees | $18,480 | $15,780 | $21,090 | $14,610 | $14,660 | student may spend for books, course”
  - column:Books, Course Materials, Supplies,: 792 ⟵ “Books, Course Materials, Supplies, | $792 | materials, supplies, living expenses,”
  - column:$1,188: 1188 ⟵ “$1,188 | $1,188 | $924 | $756”
  - column:Living Expenses (Housing & Food): 16002 ⟵ “Living Expenses (Housing & Food) | $16,002 | $16,002 | $16,002 | $16,002”
  - column:Transportation (average): 900 ⟵ “Transportation (average) | $900 | $900 | $900 | $900 | $600”
  - column:Personal/Miscellaneous: 1500 ⟵ “Personal/Miscellaneous | $1,500 | $1,500 | $1,500 | $1,500 | $1,000”
  - column:Loan Fees: 216 ⟵ “Loan Fees | $216 | $216 | $216 | $216 | $144”
  - column:$38,286: 35586 ⟵ “$38,286 | $35,586 | $40,632 | $33,984 | $27,864”
  - column:$32,760: 32760 ⟵ “$32,760 | $32,760 | $32,760 | $25,580 | $25,580 | $15,780 | $15,780”
  - column:Books, Course Materials, Supplies,: 1260 ⟵ “Books, Course Materials, Supplies, | $1,260 | $1,260 | $1,260 | 1260 | 1260 | $1,260 | $1,260”
  - column:Living Expenses (Housing & Food): 7918 ⟵ “Living Expenses (Housing & Food) | $10,668 | $7,918 | $13,800 | $10,668 | $7,918 | $10,668 | $7,918”
  - column:Transportation (average): 2000 ⟵ “Transportation (average) | $2,000 | $2,000 | $2,000 | $2,000 | 2000 | $600 | $600”
  - column:Personal/Miscellaneous: 1800 ⟵ “Personal/Miscellaneous | $1,800 | $1,800 | $1,800 | $1,800 | 1800 | $1,800 | $1,800”
  - column:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96 | $96 | 96 | $96 | $96”
  - column:$48,584: 51716 ⟵ “$48,584 | $45,834 | $51,716 | $41,404 | $38,654 | $30,204 | $27,454”
  - column:Tuition & Fees: 15780 ⟵ “Tuition & Fees | $18,480 | $15,780 | $21,090 | $14,610 | $14,660 | student may spend for books, course”
  - column:$1,188: 924 ⟵ “$1,188 | $1,188 | $924 | $756”
  - … 57 more rows
### `be4740aa3335201d` Point University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://point.edu/admissions/tuition-aid/financial-aid/faq-resources (sha256 0fca1c6ef109)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If a student or parent has been laid off or terminated, the student can complete a Professional Judgment Request Form and provide proper documentation which will be reviewed for possible adjustments.”
### `0f5d571721b98a4e` Savannah State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://give.savannahstate.edu/scholarship-information-for-students (sha256 d3392fc40389)
- issues: semantic_review_required, conflicting_sources:https://savannahstate.edu/financial-aid/professional-judgement/special-circumstances/,https://savannahstate.edu/financial-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “University and Foundation Scholarships are not refundable, unless for special circumstances.”
### `310c3a757f6a9d9d` Savannah State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://savannahstate.edu/financial-aid/sap/ (sha256 195f33d22992)
- issues: semantic_review_required, conflicting_sources:https://give.savannahstate.edu/scholarship-information-for-students,https://savannahstate.edu/financial-aid/professional-judgement/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals will be considered for extenuating circumstances only, which may include, but are not limited to, the death of an immediate family member (guardian, child, spouse, parent (this does not include in-laws)), an injury or illness of the student or their immediate family member, or other special circumstances that are generally outside of the control of the student.”
### `4543ee60052e88d2` Savannah State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://savannahstate.edu/financial-aid/professional-judgement/special-circumstances/ (sha256 89ef40e5b4fb)
- issues: semantic_review_required, conflicting_sources:https://give.savannahstate.edu/scholarship-information-for-students,https://savannahstate.edu/financial-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Please be sure the student’s FAFSA has been completed and all required documentation submitted before completing a Special Circumstances Appeal Form.”
  - sentence: need_based_special_circumstances ⟵ “To submit an appeal for Special Circumstances, please log onto your Student Forms portal Note: First time users will need to create an account.”
### `4d9c03e9c8156c3b` Savannah State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://savannahstate.edu/financial-aid/professional-judgement/special-circumstances/ (sha256 89ef40e5b4fb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “This Professional Judgment Special Circumstances Appeal allows you to request a change in the input data in the Student Aid Index (SAI) calculation due to unusual circumstances.”
### `bd9eca1336438e96` Savannah State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://savannahstate.edu/financial-aid/about-your-award/ (sha256 db13a9edf800)
- issues: semantic_review_required, conflicting_sources:https://savannahstate.edu/financial-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “However, aid will not disburse until your SAP appeal is approved.”
### `fae0560b102a27a7` Savannah State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://savannahstate.edu/financial-aid/sap/ (sha256 195f33d22992)
- issues: semantic_review_required, conflicting_sources:https://savannahstate.edu/financial-aid/about-your-award/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students who are not making SAP must complete an appeal.”
  - sentence: sap_appeal ⟵ “Submit an Appeal Students who are not making SAP must complete an appeal in order to regain eligibility for financial aid.”
### `c37933e3f3f807a7` Savannah Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.savannahtech.edu/students/registrar/satisfactory-academic-progress/ (sha256 f56b14385ac8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A student may appeal Financial Aid Suspension if the student has an unusual circumstance.”
### `cc047778efb9e39d` Savannah Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.savannahtech.edu/students/registrar/satisfactory-academic-progress/ (sha256 f56b14385ac8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Probation Probation is assigned if a student has received an approved SAP Appeal to reinstate financial aid.”
  - sentence: sap_appeal ⟵ “Failure to answer all questions below will result in a rejected SAP Appeal form: Extenuating circumstance(s) such as personal injury or illness, family emergency, death of a close relative, etc.”
  - sentence: sap_appeal ⟵ “Submit Appeal of Financial Aid Suspension Form/Personal Statement/Supporting Documentation Submit a completed/signed Appeal of Financial Aid Suspension form at https://savannahtech.verifymyfafsa.com Complete appeal must be submitted by the SAP Appeal deadline (see website or financial aid office for specific dates).”
### `49b33188ceb7e8f0` Savannah Technical College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.savannahtech.edu/tuition/tuition-outlook/ (sha256 dfd1f6864d8a)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition: 3852 ⟵ “Tuition | $3,852 | $3,852 | $7,704 | $7,704”
  - column:Fees: 1143 ⟵ “Fees | $1,143 | $1,143 | $1,143 | $1,143”
  - column:Books & Supplies: 2200 ⟵ “Books & Supplies | $2,200 | $2,200 | $2,200 | $2,200”
  - column:Housing & Meals: 5496 ⟵ “Housing & Meals | $5,496 | $22,668 | $5,496 | $22,668”
  - column:Misc. Expenses: 2148 ⟵ “Misc. Expenses | $2,148 | $2,148 | $2,148 | $2,148”
  - column:Transportation: 2052 ⟵ “Transportation | $2,052 | $2,052 | $2,052 | $2,052”
  - column:Total: 16891 ⟵ “Total | $16,891 | $34,063 | $20,743 | $37,915”
  - column:Tuition: 3852 ⟵ “Tuition | $3,852 | $3,852 | $7,704 | $7,704”
  - column:Fees: 1143 ⟵ “Fees | $1,143 | $1,143 | $1,143 | $1,143”
  - column:Books & Supplies: 2200 ⟵ “Books & Supplies | $2,200 | $2,200 | $2,200 | $2,200”
  - column:Housing & Meals: 22668 ⟵ “Housing & Meals | $5,496 | $22,668 | $5,496 | $22,668”
  - column:Misc. Expenses: 2148 ⟵ “Misc. Expenses | $2,148 | $2,148 | $2,148 | $2,148”
  - column:Transportation: 2052 ⟵ “Transportation | $2,052 | $2,052 | $2,052 | $2,052”
  - column:Total: 34063 ⟵ “Total | $16,891 | $34,063 | $20,743 | $37,915”
### `eeb5b888e7d8bb89` Savannah Technical College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.savannahtech.edu/tuition/tuition-outlook/ (sha256 dfd1f6864d8a)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition: 7704 ⟵ “Tuition | $3,852 | $3,852 | $7,704 | $7,704”
  - column:Fees: 1143 ⟵ “Fees | $1,143 | $1,143 | $1,143 | $1,143”
  - column:Books & Supplies: 2200 ⟵ “Books & Supplies | $2,200 | $2,200 | $2,200 | $2,200”
  - column:Housing & Meals: 5496 ⟵ “Housing & Meals | $5,496 | $22,668 | $5,496 | $22,668”
  - column:Misc. Expenses: 2148 ⟵ “Misc. Expenses | $2,148 | $2,148 | $2,148 | $2,148”
  - column:Transportation: 2052 ⟵ “Transportation | $2,052 | $2,052 | $2,052 | $2,052”
  - column:Total: 20743 ⟵ “Total | $16,891 | $34,063 | $20,743 | $37,915”
  - column:Tuition: 7704 ⟵ “Tuition | $3,852 | $3,852 | $7,704 | $7,704”
  - column:Fees: 1143 ⟵ “Fees | $1,143 | $1,143 | $1,143 | $1,143”
  - column:Books & Supplies: 2200 ⟵ “Books & Supplies | $2,200 | $2,200 | $2,200 | $2,200”
  - column:Housing & Meals: 22668 ⟵ “Housing & Meals | $5,496 | $22,668 | $5,496 | $22,668”
  - column:Misc. Expenses: 2148 ⟵ “Misc. Expenses | $2,148 | $2,148 | $2,148 | $2,148”
  - column:Transportation: 2052 ⟵ “Transportation | $2,052 | $2,052 | $2,052 | $2,052”
  - column:Total: 37915 ⟵ “Total | $16,891 | $34,063 | $20,743 | $37,915”
### `3249c6b71fb91abc` South Georgia State College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.sgsc.edu/content/userfiles/files/Registrar/SGSC_CLEP_Equivalencies_8-2024.pdf (sha256 35e1959fb314)
- issues: credits_implausible
- checks: {"distinct_exams": 26, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government               50      POLS 1101*”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877           50      HIST 2111*”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present           50      HIST 2112*”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development                 50      PSYC 2103”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology             50      PSYC 1101”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology            50      SOCI 1101”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics             50      ECON 2105”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics            50      ECON 2106”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1864             50      HIST 1121”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present            50      HIST 1122”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature           50      ENGL 2131”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition           50      ENGL 1101”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular            50      ENGL 1101”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature          50      ENGL 2121”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities           50      HUMN 2111”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology        50      BIOL 2107K”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus        50      MATH 2253”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry         50      CHEM 1211K”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra        50      MATH 1111”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus        50      MATH 1113”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting              50      ACCT 2101”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications               50      CISY 1105”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business law              50      BUSA 2270”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language          50      FREN 1001              59        FREN 1001”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language          50      SPAN 1001              63        SPAN 1001”
  - … 1 more rows
### `612bfde63f73a7e3` South Georgia Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.southgatech.edu/uploads/files/85/03/8503e1f26cced8b3032f792632674f31.pdf (sha256 296e5905571a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Office of Student Financial Aid Satisfactory Academic Progress (SAP) Appeal Application Student Information Full Name (First, MI, Last): ___________________________________________________________ Student ID: __________________________ Email: ____________________________________ If you believe you have extenuating circumstances (circumstances that prevented your from meeting SAP) that may warrant ”
  - sentence: sap_appeal ⟵ “Circumstances that May Warrant a SAP appeal: • Death or serious illness or injury to an immediate family member • Extended hospitalization or medical condition of student • Victim of a violent crime or natural disaster • Automobile accident • Other documented situations B.”
  - sentence: sap_appeal ⟵ “You will be contacted via email regarding the status of your SAP appeal.”
  - sentence: sap_appeal ⟵ “Please Select from the Following: Have you previously completed a Satisfactory Academic Progress (SAP) appeal?”
### `77c8f45fb949e76b` Southern Crescent Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sctech.edu/financial-aid/ (sha256 cc36dee991b1)
- issues: semantic_review_required, conflicting_sources:https://www.sctech.edu/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Schedule Satisfactory Academic Progress Appeal Deadlines Complete SAP appeals must be submitted by the applicable deadline.”
### `f8173bd4133d34a6` Southern Crescent Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sctech.edu/financial-aid/satisfactory-academic-progress/ (sha256 9d9c088e48f2)
- issues: semantic_review_required, conflicting_sources:https://www.sctech.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “View FAQ Submit Online CampusLogic Submit SAP appeals and upload documentation securely.”
  - sentence: sap_appeal ⟵ “Select one GPA below 2.0 Completion Rate below 66.66% GPA and Completion Rate below standards Exceeded Maximum Timeframe Check Next Step Previous Back to Menu Next: Appeal Types SAP Appeals & Academic Plans Students on Financial Aid Suspension may submit an appeal through CampusLogic.”
  - sentence: sap_appeal ⟵ “Previous Back to Menu Next: Deadlines SAP Appeal Deadlines | Semester | Priority Deadline | Final Deadline | Fall | August 9, 2026 | October 3, 2026 | Spring | January 3, 2027 | February 13, 2027 | Summer | May 1, 2027 | May 1, 2027 Priority Deadline: Appeals submitted by the Priority Deadline receive priority review.”
  - sentence: sap_appeal ⟵ “Back to Menu Access CampusLogic Southern Crescent Technical College uses CampusLogic to securely collect SAP appeal information and supporting documentation.”
  - sentence: sap_appeal ⟵ “Submit Academic Progress Appeals Submit Maximum Timeframe Appeals Upload supporting documentation Monitor appeal status Review outstanding requirements All SAP Appeals must be submitted through CampusLogic.”
### `4174e79b5fbc9058` Southern Regional Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: http://southernregional.edu/college-catalog/current/admissions-information (sha256 286cfca5e029)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Center Transfer Agreements Transcript Request Home Catalogs 2026-2027 College Catalog and Student Handbook Admissions Information Search Catalog Admissions Information Admissions Policy Southern Regional Technical College does not discriminate on the basis of race, color, creed, national or ethnic origin, gender, religion, disability, age, political affiliation or belief, disabled veteran, veteran”
### `6c43f94dc16e85ce` Southern Regional Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://southernregional.edu/college-catalog/2025-2026-college-catalog/financial-aid (sha256 e2bf3a08592b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress requirements must be met or an appeal must be approved in order to receive aid.”
### `7c1c0fe0b56787bb` Southern Regional Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://southernregional.edu/college-catalog/2025-2026-college-catalog/admissions-information (sha256 c92d3b7b9bf4)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://southernregional.edu/college-catalog/2025-2026-college-catalog/financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Center Transfer Agreements Transcript Request Home Catalogs 2025-2026 College Catalog and Student Handbook Admissions Information Search Catalog Admissions Information Admissions Policy Southern Regional Technical College does not discriminate on the basis of race, color, creed, national or ethnic origin, gender, religion, disability, age, political affiliation or belief, disabled veteran, veteran”
### `aacb57afd45e02d0` Southern Regional Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://southernregional.edu/college-catalog/2025-2026-college-catalog/financial-aid (sha256 e2bf3a08592b)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://southernregional.edu/college-catalog/2025-2026-college-catalog/admissions-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals will be considered for extenuating circumstances only, which may include, but are not limited to, the death of a family member, an injury or illness of the student or their immediate family member, or other special circumstances that are generally outside of the control of the student.”
### `e039c05c394fca2b` Spelman College — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.spelman.edu/_1_Docs-and-Files/about/institutional-research/common-data-set/cds-2024-2025-final-3-4-251.pdf (sha256 4d6e818a8e3a)
- issues: enrolled_breakdown_does_not_reconcile, stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 12023 ⟵ “Total first-time, first-year who applied                                          12023”
  - admits: 2990 ⟵ “Total first-time, first-year who were admitted                                     2990”
  - enrolled: 2 ⟵ “Total first-time, first-year who enrolled                                          705                149            554             2”
  - sat_composite_25..75: [1128, 1240, 1303] ⟵ “SAT Composite                              1128            1240            1303”
  - sat_math_25..75: [518, 590, 640] ⟵ “SAT Math                                    518             590             640”
  - act_25..75: [22, 25, 29] ⟵ “ACT Composite                                22                25                29”
### `565662ca3c773a5e` Thomas University — appeals 2018-19 [new] (labeled_in_source)
- source: https://www.thomasu.edu/cost/about-financial-aid/financial-aid-eligibility/ (sha256 83a40472e960)
- issues: stale_year_label:2018-19, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Revision Request Form: Use this form to make changes to your financial aid such as enrollment changes for future terms and increasing and decreasing your Stafford Loans. 2018/2019 Cost of Attendance Increase form: You may have your estimated cost of attendance increased for costs resulting from special circumstances that were not included in the original financial aid calculation.”
### `5a3ee5b1e642238d` Thomas University — appeals 2018-19 [new] (labeled_in_source)
- source: https://www.thomasu.edu/cost/about-financial-aid/financial-aid-eligibility/ (sha256 83a40472e960)
- issues: stale_year_label:2018-19, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The Department of Education allows for an institution to use professional judgment to change certain elements of the FAFSA application if adequate documentation can be provided.”
### `7492f823515568ea` Thomas University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.thomasu.edu/cost/about-financial-aid/ (sha256 9c597df0b79f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Conditions Appeal: A formal request to have a financial aid administrator review your aid eligibility and possibly use Professional Judgment to adjust the figures.”
### `e835788d78f47433` Thomas University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.thomasu.edu/cost/about-financial-aid/ (sha256 9c597df0b79f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you have a special circumstance (reduction in income, etc.) that you would like to be considered in regards to your financial aid award, please contact the Office of Financial Aid to discuss your situation.”
  - sentence: need_based_special_circumstances ⟵ “For example, if you believe the financial information on your financial aid application does not reflect your family's current ability to pay (e.g., because of the death of a parent, unemployment or other unusual circumstances), you should definitely make an appeal.”
### `c7cd57e7d85d0e78` Toccoa Falls College — appeals 2026-27 [new] (source_unlabeled)
- source: https://utf.edu/admissions/financial-aid/ (sha256 2a9533087e68)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Scholarships & Aid Applying for Aid Tuition & Fees Net Price Calculator Financial Resources Scholarships & Aid Work-Study FAFSA® Simplification Financial Aid Portal Financial Aid Awarding Process FAFSA Loans Student Accounts Special & Unusual Circumstances We’re Here to Help We understand financial aid can be the most difficult component to choosing a university.”
### `2b422f1d3235ded5` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,000 per year ⟵ “Dual Enrollment Scholarship | $1,000 per year | Earn at least 6 credit hours, or complete 2 courses of Dual Enrollment credit through TMU prior to high school/home study graduation”
### `34a0453c7acc98ca` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,000 per year ⟵ “Dependent of a Baptist Minister | $1,000 per year | Student must be a dependent of parent/spouse Parent/spouse must be an ordained or a licensed Baptist Minister, full-time missionary through a Baptist mission board or full-time with the GBMB. Complete application with parent/spouse’s signature each”
### `647d9debdb0e8207` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per year ⟵ “Bear Award | $3,000 per year | Below 3.0 Unweighted HS GPA”
### `7132c3c86fdab2bf` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: 10% Tuition Discount ⟵ “Sibling Discount | 10% Tuition Discount | Student must be a sibling of currently enrolled student at TMU”
### `7caa51242a2fecd4` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $500 per year ⟵ “Georgia Baptist Membership Scholarship | $500 per year | Member or attendee of a Georgia Baptist Church”
### `7d49b540c45ecafe` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: Determined by Head Coach ⟵ “Athletic Scholarship | Determined by Head Coach | Demonstrated Abilities Renewed annually by Athletic Dept.”
### `91dc9c922d3db64d` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $9,000 per year ⟵ “Presidential Scholar | $9,000 per year | 4.0 + Unweighted HS GPA”
### `ad2cd57c70a3cac6` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $5,000 per year ⟵ “Dean Scholar | $5,000 per year | 3.0 + Unweighted HS GPA”
### `b51b7fa363779f2b` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,500 per year ⟵ “Home School Graduate Scholarship | $1,500 per year | Graduate from a Home School program”
### `bdff5296a6474014` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $6,500 per year ⟵ “Vice Presidential Scholar | $6,500 per year | 3.4 + Unweighted HS GPA”
### `c6d7e371e0d591ee` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $8,000 per year ⟵ “Trustee Scholar | $8,000 per year | 3.7 + Unweighted HS GPA”
### `c98cd1399a151133` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: Determined by Chair of School of Music ⟵ “Music Scholarship | Determined by Chair of School of Music | Demonstrated Abilities Renewed annually by Music Dept.”
### `d795a064464d8fdd` Truett McConnell University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://tmu.edu/admissions/scholarships-aid/ (sha256 2b8b69096d77)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,000 per year ⟵ “Christian School Graduate Scholarship | $1,000 per year | Graduate from a Christian High School”
### `1156c1da33e1408e` University of North Georgia — appeals 2025-26 [new] (labeled_in_source)
- source: https://ung.edu/cost-aid/financial-aid/index.php (sha256 be2cf8913ea7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Circumstances and Professional Judgment Contact Us Request Information Quick Facts Campus Maps & Directions Student Consumer Information UNG Listens Campus Safety Emergency Information Employment/HR UNG Policies & Procedures Title IX Campus Hazing Transparency Report UNG Alumni Association UNG Foundation Ethics & Compliance Hotline Human Trafficking Notice Equal Empl.”
### `1885f47a68c642a0` University of North Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://ung.edu/cost-aid/financial-aid/special-circumstances-and-professional-judgment.php (sha256 dfcd3ed7ac1e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Special Circumstances and Professional Judgment Skip to Main Content Skip to Main Navigation Skip to Footer Info For...”
  - sentence: professional_judgment ⟵ “While the Free Application for Federal Student Aid (FAFSA) determines financial aid eligibility based on data from two years prior, the Professional Judgment process exists to re-evaluate a student’s aid based on certain significant changes.”
  - sentence: professional_judgment ⟵ “Job loss due to cause or personal choice Standard living expenses (i.e., utilities, car payments) Mortgage payments Personal debt Bankruptcy Who is not eligible for a Professional Judgment?”
  - sentence: professional_judgment ⟵ “Possible changes include: Costs associated with a student’s disability Childcare expenses for a dependent child of student One-time purchase of a computer for educational use One-time cost of professional licensure required for student’s major How to Apply for Professional Judgement If you meet one of the significant changes outlined in the Change to Student Aid Index (SAI) or the Change to Cost o”
### `5c801c6fcd4fe3f0` University of North Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://ung.edu/cost-aid/financial-aid/satisfactory-academic-progress.php (sha256 bb9ede5c52fe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “SAP Appeal Plan – A student who was unable to meet the stipulations under the SAP Academic Plan will no longer be eligible for financial aid, but will retain the right to appeal the determination based on extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Students must complete the SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “Deadlines for Financial Aid Appeals Fall Semester: November 1 Spring Semester: April 1 Summer Semester: July 1 Review of Financial Aid Appeals Financial Aid Appeals will be reviewed by the financial aid director with guidance from an SAP Appeal Committee comprised of Student Affairs and Academic Affairs personnel.”
  - sentence: sap_appeal ⟵ “Regaining Financial Aid Eligibility Once eligibility for financial aid has been denied by the SAP Appeal Committee, a student can only regain financial aid eligibility by meeting the SAP standards.”
### `aa7ecdfe94bc2019` University of North Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://ung.edu/cost-aid/financial-aid/special-circumstances-and-professional-judgment.php (sha256 dfcd3ed7ac1e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Graduate students (only eligible for Cost of Attendance adjustments in the form of loans).”
### `099fe3dc799337e9` University of North Georgia — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://ung.edu/undergraduate-admissions/how-to-apply/dual-enrollment.php (sha256 7de0356ebfbc)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.25 ⟵ “The student must present a cumulative grade point average (GPA) of 3.25 or higher in their Required High School Curriculum (RHSC) coursework (PDF), and the transcript must show evidence that the student is on track toward the completion of the USG RHSC requirements and high school graduation.”
### `aedbd30e873a3511` University of West Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.westga.edu/student-services/financialaid/satisfactory-academic-progress.php (sha256 87bf4cf0d4fb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: sap_appeal ⟵ “Examples of extenuating circumstances for which a student may file a SAP Appeal may include a student's injury or illness, serious illness or death of an immediate family member, or other special circumstances.”
  - sentence: sap_appeal ⟵ “Each SAP Appeal will be reviewed individually and decisions are made on a case-by-case basis as outlined in the procedures given below.”
  - sentence: sap_appeal ⟵ “The SAP Appeal process requires the submission of a written statement by the student outlining the extenuating circumstances which led to their academic difficulties, how the circumstances have changed, and the student's plan for improving their academic status.”
  - sentence: sap_appeal ⟵ “SAP appeals will be reviewed by a UWG committee comprised of F.A. staff.”
  - sentence: sap_appeal ⟵ “A student who wishes to appeal the decision of the SAP Appeal Committee may submit a request for a review by the 2nd Appeal Committee.”
  - sentence: sap_appeal ⟵ “If a student's SAP appeal is granted by either the SAP Appeal Committee, 2nd Appeal Committee, or the Director of Financial Aid, the student will gain eligibility for continued federal, state, or institutional financial aid eligibility for one semester only.”
### `4fd935879dfe9738` University of West Georgia — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.westga.edu/assets/studentaccounts/docs/fy25_tuitionchart-undergraduate.pdf (sha256 d1d4ccc15008)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 23, "rows": 1}
  - column:Enrolled Hours: 1 ⟵ “Enrolled Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Enrolled Hours: 1 ⟵ “Enrolled Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Enrolled Hours: 1 ⟵ “Enrolled Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Enrolled Hours: 2 ⟵ “Enrolled Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 187.0 ⟵ “Tuition | $ | 187.00 | $ | 374.00 | $ | 561.00 | $ | 748.00 | $ | 935.00 | $ | 1,122.00 | $ | 1,309.00 | $ | 1,496.00 | $ | 1,683.00 | $ | 1,870.00 | $ | 2,057.00 | $ | 2,244.00 | $ | 2,431.00 | $ | 2,618.00 | $ | 2,805.00”
  - column:Activity Fee: 11.8 ⟵ “Activity Fee | $ | 11.80 | $ | 23.60 | $ | 35.40 | $ | 47.20 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00”
  - column:Athletic Complex Fee: 26.0 ⟵ “Athletic Complex Fee | $ | 26.00 | $ | 52.00 | $ | 78.00 | $ | 104.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00”
  - column:Athletic Fee: 39.0 ⟵ “Athletic Fee | $ | 39.00 | $ | 78.00 | $ | 117.00 | $ | 156.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00”
  - column:Campus Center Fee: 28.8 ⟵ “Campus Center Fee | $ | 28.80 | $ | 57.60 | $ | 86.40 | $ | 115.20 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00”
  - column:Health Fee: 20.2 ⟵ “Health Fee | $ | 20.20 | $ | 40.40 | $ | 60.60 | $ | 80.80 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00”
  - column:International Education Fee: 5.0 ⟵ “International Education Fee | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00”
  - column:Technology Fee: 55.0 ⟵ “Technology Fee | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00”
  - column:Transportation Fee: 111.0 ⟵ “Transportation Fee | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00”
  - column:Total: 483.8 ⟵ “Total | $ | 483.80 | $ | 796.60 | $ | 1,109.40 | $ | 1,422.20 | $ | 1,735.00 | $ | 1,922.00 | $ | 2,109.00 | $ | 2,296.00 | $ | 2,483.00 | $ | 2,670.00 | $ | 2,857.00 | $ | 3,044.00 | $ | 3,231.00 | $ | 3,418.00 | $ | 3,605.00”
  - column:Enrolled Hours: 2 ⟵ “Enrolled Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition - Base Rate: 187.0 ⟵ “Tuition - Base Rate | $ | 187.00 | $ | 374.00 | $ | 561.00 | $ | 748.00 | $ | 935.00 | $ | 1,122.00 | $ | 1,309.00 | $ | 1,496.00 | $ | 1,683.00 | $ | 1,870.00 | $ | 2,057.00 | $ | 2,244.00 | $ | 2,431.00 | $ | 2,618.00 | $ | 2,805.00”
  - column:Out of State Tuition Prem.: 488.0 ⟵ “Out of State Tuition Prem. | $ | 488.00 | $ | 976.00 | $ | 1,464.00 | $ | 1,952.00 | $ | 2,440.00 | $ | 2,928.00 | $ | 3,416.00 | $ | 3,904.00 | $ | 4,392.00 | $ | 4,880.00 | $ | 5,368.00 | $ | 5,856.00 | $ | 6,344.00 | $ | 6,832.00 | $ | 7”
  - column:Activity Fee: 11.8 ⟵ “Activity Fee | $ | 11.80 | $ | 23.60 | $ | 35.40 | $ | 47.20 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00 | $ | 59.00”
  - column:Athletic Complex Fee: 26.0 ⟵ “Athletic Complex Fee | $ | 26.00 | $ | 52.00 | $ | 78.00 | $ | 104.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00 | $ | 130.00”
  - column:Athletic Fee: 39.0 ⟵ “Athletic Fee | $ | 39.00 | $ | 78.00 | $ | 117.00 | $ | 156.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00 | $ | 195.00”
  - column:Campus Center Fee: 28.8 ⟵ “Campus Center Fee | $ | 28.80 | $ | 57.60 | $ | 86.40 | $ | 115.20 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00 | $ | 144.00”
  - column:Health Fee: 20.2 ⟵ “Health Fee | $ | 20.20 | $ | 40.40 | $ | 60.60 | $ | 80.80 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00 | $ | 101.00”
  - column:International Education Fee: 5.0 ⟵ “International Education Fee | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00 | $ | 5.00”
  - column:Technology Fee: 55.0 ⟵ “Technology Fee | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00 | $ | 55.00”
  - column:Transportation Fee: 111.0 ⟵ “Transportation Fee | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00 | $ | 111.00”
  - … 500 more rows
### `42ea5e15ac8d6f9b` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php (sha256 34a725f68a5e)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php,https://www.valdosta.edu/admissions/financial-aid/process/tips-when-applying-for-financial-aid.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `448c804100e80277` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php (sha256 0e21e25e7372)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php,https://www.valdosta.edu/admissions/financial-aid/process/tips-when-applying-for-financial-aid.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `7d4b5cfa4cb85c39` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php (sha256 0e21e25e7372)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Please read before starting either appeal at https://valdosta.studentforms.com: Professional Judgement: Special Circumstance - SAI Calculation Appeal (Changes in family income) If a family has experienced a significant change in income from what was reported on FAFSA, a Special Circumstance Appeal may be a good option.”
  - sentence: professional_judgment ⟵ “Professional Judgment: Unusual Circumstance Appeal Students that are not; at least 24 years old, married, serving in the military, or have any children of their own - must typically provide parent information on the FAFSA.”
  - sentence: professional_judgment ⟵ “From there, chose either “Professional Judgment: Unusual Circumstance Appeal ” or “Professional Judgment: Special Circumstance - SAI Calculation Appeal” from the drop-down bar.”
### `8dd67172f0336996` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php (sha256 75b7c3cf388e)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php,https://www.valdosta.edu/admissions/financial-aid/process/tips-when-applying-for-financial-aid.php
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Click each link below to find information about each type of appeal, including steps on how to complete the appeal process: Satisfactory Academic Progress Appeal (see below) Professional Judgment: Unusual Circumstances Appeal or Professional Judgment: Special Circumstance - EFC/SAI Calculation Appeal (click here) Satisfactory Academic Progress Appeal Students who fail to meet Satisfactory Academic”
  - sentence: sap_appeal ⟵ “The student should complete a Satisfactory Academic Progress Appeal Form which is available online via our On Line Student Forms Portal.”
  - sentence: sap_appeal ⟵ “Only SAP appeals containing both required statements and documentation will be processed and evaluated.”
  - sentence: sap_appeal ⟵ “If a student’s SAP appeal is approved, and they can come into compliance within one semester, the student will be granted a one semester SAP probation and be eligible for financial aid for one semester.”
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `9652f91e67293b4a` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/sap.php (sha256 beeb1e3c9f50)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php,https://www.valdosta.edu/admissions/financial-aid/process/tips-when-applying-for-financial-aid.php
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Appeal Process: Students who fail to meet Satisfactory Academic Progress (SAP) may appeal their status based on extenuating circumstances.”
  - sentence: sap_appeal ⟵ “The student should complete a Satisfactory Academic Progress Appeal Form which is available from the Office of Financial Aid web page.”
  - sentence: sap_appeal ⟵ “Only SAP appeals containing both required statements and documentation will be processed and evaluated.”
  - sentence: sap_appeal ⟵ “If a student’s SAP appeal is approved, and they can come into compliance within one semester, the student will be granted a one semester SAP probation and be eligible for financial aid for one semester.”
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `ca299f0c4736de57` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/tips-when-applying-for-financial-aid.php (sha256 79d07c4e35cc)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `f3f3c2d55bf3ef7a` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php (sha256 7b9e42166d92)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php,https://www.valdosta.edu/admissions/financial-aid/process/tips-when-applying-for-financial-aid.php
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Appeal Process: Students who fail to meet Satisfactory Academic Progress (SAP) may appeal their status based on extenuating circumstances.”
  - sentence: sap_appeal ⟵ “The student should complete a Satisfactory Academic Progress Appeal Form which is available from the Office of Financial Aid web page.”
  - sentence: sap_appeal ⟵ “Only SAP appeals containing both required statements and documentation will be processed and evaluated.”
  - sentence: sap_appeal ⟵ “If a student’s SAP appeal is approved, and they can come into compliance within one semester, the student will be granted a one semester SAP probation and be eligible for financial aid for one semester.”
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `f44d6b901a60aa66` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php (sha256 0e21e25e7372)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “There can be some exceptions to this, that would warrant completing an Unusual Circumstance Appeal.”
  - sentence: need_based_special_circumstances ⟵ “Proof of incarceration Obituary or Death Certificate Other appropriate documentation and written signed statements ***Please note that parent refusal to provide information on the FAFSA or a student being financially self-sufficient, is not a valid reason to submit an Unusual Circumstance Appeal.”
### `62f2743fc1362e1c` Valdosta State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/undergraduate/advanced-placement-equivalencies.php (sha256 2c8f03794794)
- issues: rows_without_score
- checks: {"distinct_exams": 13, "equivalencies": 23, "rows_without_score": 3}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|ANTHROPOLOGY, SOCIAL]:  ⟵ “ANTHROPOLOGY, SOCIAL | 4 or higher | ANTH 1102 | Intro to Anthropology | 3”
  - equivalencies[IB-BIOLOGY|BIOLOGY]:  ⟵ “BIOLOGY | 4 or 5 | BIOL 1010, 1020L | Intro to Biology I and lab | 4”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “ |  | BIOL 1030, 1040L | Intro to Biology II and lab | 4”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “ |  | or BIOL 1107K | Unifying Prn of Biology | 4”
  - equivalencies[IB-CHEMISTRY|CHEMISTRY]:  ⟵ “CHEMISTRY | 4 | CHEM 1211, 1211L | Principles Chemistry I and lab | 4”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “ |  | CHEM 1212, 1212L | Principles Chemistry II and lab | 4”
  - equivalencies[IB-ECONOMICS|ECONOMICS]:  ⟵ “ECONOMICS | 4 or higher | ECON 2106 or 2105 | Prn Microeconomics or Macroeconomics | 3”
  - equivalencies[IB-FRENCH|FRENCH]:  ⟵ “FRENCH | 4 | FREN 1002 & 2001 | Bgng French II & Intermed French I | 6”
  - equivalencies[IB-FRENCH|FRENCH]:  ⟵ “FRENCH | 5 or higher | FREN 1002 & 2001 & 2002 | Bgng French II, Intermed French I & II | 9”
  - equivalencies[IB-GEOGRAPHY|GEOGRAPHY]:  ⟵ “GEOGRAPHY | 4 or higher | GEOG 1102 | World Regional Geography | 3”
  - equivalencies[IB-GERMAN|GERMAN]:  ⟵ “GERMAN | 4 | GRMN 1002 & 2001 | Bgng German II & Intermed German I | 6”
  - equivalencies[IB-GERMAN|GERMAN]:  ⟵ “GERMAN | 5 or higher | GRMN 1002 & 2001 & 2002 | Bgng German II, Intermed German I & II | 9”
  - equivalencies[IB-HISTORY|HISTORY, AMERICAS*]:  ⟵ “HISTORY, AMERICAS* | 4 | HIST 2111 | US History to 1865 | 3”
  - equivalencies[IB-HISTORY|HISTORY, AMERICAS*]:  ⟵ “HISTORY, AMERICAS* | 5 or higher | HIST 2111 & 2112 | US History to 1865, US History sn 1865 | 6”
  - equivalencies[IB-HISTORY|HISTORY, EUROPE]:  ⟵ “HISTORY, EUROPE | 4 or higher | HIST 1012 | History of Civilization II | 3”
  - equivalencies[IB-LATIN|LATIN]:  ⟵ “LATIN | 4 | LATN 1002 & 2001 | Bgng Latin II & Intermed Latin I | 6”
  - equivalencies[IB-LATIN|LATIN]:  ⟵ “LATIN | 5 or higher | LATN 1002 & 2001 & 2002 | Bgng Latin II, Intermed Latin I & II | 9”
  - equivalencies[IB-PHYSICS|PHYSICS]:  ⟵ “PHYSICS | 4 | PHYS 1111K | Introductory Physics I | 4”
  - equivalencies[IB-PHYSICS|PHYSICS]:  ⟵ “PHYSICS | 5 or higher | PHYS 1111K & 1112K | Introductory Physics I & II | 8”
  - equivalencies[IB-PSYCHOLOGY|PSYCHOLOGY]:  ⟵ “PSYCHOLOGY | 4 or higher | PSYC 2500 | Fundamentals of Psychology | 3”
  - equivalencies[IB-SPANISH|SPANISH]:  ⟵ “SPANISH | 4 | SPAN 1002 & 2001 | Bgng Spanish II & Intermed Spanish I | 6”
  - equivalencies[IB-SPANISH|SPANISH]:  ⟵ “SPANISH | 5 or higher | SPAN 1002 & 2001 & 2002 | Bgng Spanish II, Intermed Spanish I & II | 9”
  - equivalencies[IB-THEATRE|THEATRE ARTS]:  ⟵ “THEATRE ARTS | 4 or higher | THEA 1100 | Theatre Appreciation | 3”
### `e35e907884e305c1` Valdosta State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/undergraduate/advanced-placement-equivalencies.php (sha256 2c8f03794794)
- issues: rows_without_score
- checks: {"distinct_exams": 3, "equivalencies": 4, "rows_without_score": 1}
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 or 4]:  ⟵ “English Lang or Lit & Comp |  | 3 or 4 |  | ENGL 1101 |  | 3 | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Lang or Lit & Comp |  | 5 |  | ENGL 1101 & 1102 | 6 | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3 or higher]:  ⟵ “Environmental Science |  | 3 or higher |  | GEOL elective | 3 | ”
  - equivalencies[AP-STATISTICS|None]:  ⟵ “Statistics |  |  |  | 3 or higher |  | MATH 1401 |  | 3 | ”
### `6e38603a60d74f53` Wesleyan College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wesleyancollege.edu/admission/undergraduate/upload/Your-Financial-Aid-Award-Next-Steps.pdf (sha256 2ae54ab378c7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Talk to Us If your family’s financial situation has changed since you filed the FAFSA—such as a job loss, a reduction in income, a divorce, a death in the family, or another significant life event—you may be eligible for a Professional Judgment Review.”
### `c1d890d2d1a02fcb` Wesleyan College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wesleyancollege.edu/admission/undergraduate/Scholarships-and-Financial-Aid-Home.cfm (sha256 a79d7186fb03)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Q: What if my family’s financial situation changes, or we have special circumstances?”
  - sentence: need_based_special_circumstances ⟵ “Our counselors are compassionate and will guide you through the appeal or special circumstance consideration process.”
### `0b4bceeb3847adbc` Wesleyan College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wesleyancollege.edu/admission/tuition.cfm (sha256 3299779ca7b1)
- issues: arrangement_unlabeled, conflicting_sources:https://www.wesleyancollege.edu/admission/tuition.cfm,https://www.wesleyancollege.edu/admission/undergraduate/online/upload/Online-Program-Cost-of-Attendance-2026-2027.pdf
- checks: {"columns": 3, "components_reconcile": true, "rows": 5}
  - column:Tuition: 13225 ⟵ “Tuition | $13,225 | $13,225 | $26,450”
  - column:Institutional Fees: 700 ⟵ “Institutional Fees | $700 | $700 | $1,400”
  - column:Housing (Double): 3450 ⟵ “Housing (Double) | $3,450 | $3,450 | $6,900”
  - column:Food: 2860 ⟵ “Food | $2,860 | $2,860 | $5,720”
  - column:Total Estimated Direct Costs: 20235 ⟵ “Total Estimated Direct Costs | $20,235 | $20,235 | $40,470”
  - column:Tuition: 13225 ⟵ “Tuition | $13,225 | $13,225 | $26,450”
  - column:Institutional Fees: 700 ⟵ “Institutional Fees | $700 | $700 | $1,400”
  - column:Housing (Double): 3450 ⟵ “Housing (Double) | $3,450 | $3,450 | $6,900”
  - column:Food: 2860 ⟵ “Food | $2,860 | $2,860 | $5,720”
  - column:Total Estimated Direct Costs: 20235 ⟵ “Total Estimated Direct Costs | $20,235 | $20,235 | $40,470”
  - column:Tuition: 26450 ⟵ “Tuition | $13,225 | $13,225 | $26,450”
  - column:Institutional Fees: 1400 ⟵ “Institutional Fees | $700 | $700 | $1,400”
  - column:Housing (Double): 6900 ⟵ “Housing (Double) | $3,450 | $3,450 | $6,900”
  - column:Food: 5720 ⟵ “Food | $2,860 | $2,860 | $5,720”
  - column:Total Estimated Direct Costs: 40470 ⟵ “Total Estimated Direct Costs | $20,235 | $20,235 | $40,470”
### `0e611bbc5d7e5a00` Wesleyan College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wesleyancollege.edu/admission/tuition.cfm (sha256 728624f0fe1f)
- issues: arrangement_unlabeled, conflicting_sources:https://www.wesleyancollege.edu/admission/tuition.cfm,https://www.wesleyancollege.edu/admission/undergraduate/online/upload/Online-Program-Cost-of-Attendance-2026-2027.pdf
- checks: {"columns": 3, "components_reconcile": true, "rows": 5}
  - column:Tuition: 13225 ⟵ “Tuition | $13,225 | $13,225 | $26,450”
  - column:Institutional Fees: 700 ⟵ “Institutional Fees | $700 | $700 | $1,400”
  - column:Housing (Double): 3450 ⟵ “Housing (Double) | $3,450 | $3,450 | $6,900”
  - column:Food: 2860 ⟵ “Food | $2,860 | $2,860 | $5,720”
  - column:Total Estimated Direct Costs: 20235 ⟵ “Total Estimated Direct Costs | $20,235 | $20,235 | $40,470”
  - column:Tuition: 13225 ⟵ “Tuition | $13,225 | $13,225 | $26,450”
  - column:Institutional Fees: 700 ⟵ “Institutional Fees | $700 | $700 | $1,400”
  - column:Housing (Double): 3450 ⟵ “Housing (Double) | $3,450 | $3,450 | $6,900”
  - column:Food: 2860 ⟵ “Food | $2,860 | $2,860 | $5,720”
  - column:Total Estimated Direct Costs: 20235 ⟵ “Total Estimated Direct Costs | $20,235 | $20,235 | $40,470”
  - column:Tuition: 26450 ⟵ “Tuition | $13,225 | $13,225 | $26,450”
  - column:Institutional Fees: 1400 ⟵ “Institutional Fees | $700 | $700 | $1,400”
  - column:Housing (Double): 6900 ⟵ “Housing (Double) | $3,450 | $3,450 | $6,900”
  - column:Food: 5720 ⟵ “Food | $2,860 | $2,860 | $5,720”
  - column:Total Estimated Direct Costs: 40470 ⟵ “Total Estimated Direct Costs | $20,235 | $20,235 | $40,470”
### `64957638f1c1230c` Wesleyan College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wesleyancollege.edu/admission/undergraduate/online/upload/Online-Program-Cost-of-Attendance-2026-2027.pdf (sha256 fb23d418b7ed)
- issues: arrangement_unlabeled, conflicting_sources:https://www.wesleyancollege.edu/admission/tuition.cfm,https://www.wesleyancollege.edu/admission/tuition.cfm
- checks: {"columns": 2, "rows": 1}
  - column:GA Tuition Equalization: 1100 ⟵ “GA Tuition Equalization | $1,100”
  - column:Credit: 350 ⟵ “Credit | 6 credit hours | $350”
  - column:Credit: 350 ⟵ “Credit | 12 credit hours | $350”
### `d22be4215122bffc` Wesleyan College — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wesleyancollege.edu/admission/nursing/upload/25-26-Nursing-Program-COA_Revised.pdf (sha256 e646435b4d34)
- issues: components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - on_campus:Tuition:: 26450 ⟵ “Tuition: | $26,450 | $26,450”
  - on_campus:Food & Housing:: 12620 ⟵ “Food & Housing: | $12,620 | $0”
  - on_campus:Nursing Program Fees:: 2200 ⟵ “Nursing Program Fees: | $2,200 | $2,200”
  - on_campus:Institutional Fees:: 1400 ⟵ “Institutional Fees: | $1,400 | $1,400”
  - on_campus:Estimated Total:: 42670 ⟵ “Estimated Total: | $42,670 | $30,050”
  - on_campus:GA Tuition Equalization: 1100 ⟵ “GA Tuition Equalization | $1,100”
  - on_campus:HOPE Scholarship: 5970 ⟵ “HOPE Scholarship | $5,970”
  - on_campus:Zell Miller Scholarship: 5970 ⟵ “Zell Miller Scholarship | $5,970”
  - with_parents_or_family:Tuition:: 26450 ⟵ “Tuition: | $26,450 | $26,450”
  - with_parents_or_family:Food & Housing:: 0 ⟵ “Food & Housing: | $12,620 | $0”
  - with_parents_or_family:Nursing Program Fees:: 2200 ⟵ “Nursing Program Fees: | $2,200 | $2,200”
  - with_parents_or_family:Institutional Fees:: 1400 ⟵ “Institutional Fees: | $1,400 | $1,400”
  - with_parents_or_family:Estimated Total:: 30050 ⟵ “Estimated Total: | $42,670 | $30,050”
### `b4cb3db1d71fff18` West Georgia Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/financial-aid/faq/satisfactory-academic-progress-course-repeats-and-withdrawals-faq/ (sha256 af3fddc45fc7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “A: Students placed on financial aid suspension, who had a mitigating circumstance(s) that occurred during a specific semester, can appeal the loss of financial aid eligibility by filing an SAP Appeal.”
### `8bd485bb3e2789ca` West Georgia Technical College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.westgatech.edu/financial-aid/cost-of-attendance/ (sha256 bac3c1cb8f8a)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "rows": 9}
  - column:Tuition: 3210 ⟵ “Tuition | 3210 | 6420 | 3210 | 6420”
  - column:Fees: 842 ⟵ “Fees | 842 | 842 | 842 | 842”
  - column:Books and Supplies: 1520 ⟵ “Books and Supplies | 1520 | 1520 | 1520 | 1520”
  - column:Housing: 5009 ⟵ “Housing | 5009 | 5009 | 6793 | 6793”
  - column:Food: 2500 ⟵ “Food | 2500 | 2500 | 2500 | 2500”
  - column:Transportation: 2010 ⟵ “Transportation | 2010 | 2010 | 2010 | 2010”
  - column:Miscellaneous: 1250 ⟵ “Miscellaneous | 1250 | 1250 | 1250 | 1250”
  - column:Student Loan Fees: 63 ⟵ “Student Loan Fees | 63 | 63 | 106 | 106”
  - column:Estimated COA: 16404 ⟵ “Estimated COA | 16404 | 19614 | 18231 | 21441”
  - column:Tuition: 6420 ⟵ “Tuition | 3210 | 6420 | 3210 | 6420”
  - column:Fees: 842 ⟵ “Fees | 842 | 842 | 842 | 842”
  - column:Books and Supplies: 1520 ⟵ “Books and Supplies | 1520 | 1520 | 1520 | 1520”
  - column:Housing: 5009 ⟵ “Housing | 5009 | 5009 | 6793 | 6793”
  - column:Food: 2500 ⟵ “Food | 2500 | 2500 | 2500 | 2500”
  - column:Transportation: 2010 ⟵ “Transportation | 2010 | 2010 | 2010 | 2010”
  - column:Miscellaneous: 1250 ⟵ “Miscellaneous | 1250 | 1250 | 1250 | 1250”
  - column:Student Loan Fees: 63 ⟵ “Student Loan Fees | 63 | 63 | 106 | 106”
  - column:Estimated COA: 19614 ⟵ “Estimated COA | 16404 | 19614 | 18231 | 21441”
  - column:Tuition: 3210 ⟵ “Tuition | 3210 | 6420 | 3210 | 6420”
  - column:Fees: 842 ⟵ “Fees | 842 | 842 | 842 | 842”
  - column:Books and Supplies: 1520 ⟵ “Books and Supplies | 1520 | 1520 | 1520 | 1520”
  - column:Housing: 6793 ⟵ “Housing | 5009 | 5009 | 6793 | 6793”
  - column:Food: 2500 ⟵ “Food | 2500 | 2500 | 2500 | 2500”
  - column:Transportation: 2010 ⟵ “Transportation | 2010 | 2010 | 2010 | 2010”
  - column:Miscellaneous: 1250 ⟵ “Miscellaneous | 1250 | 1250 | 1250 | 1250”
  - … 11 more rows

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 18; pages by category: admissions_tests 3, cost_of_attendance 1, dual_enrollment 3, merit_scholarships 13, residency 1, transfer_credit 1, tuition_fees 8

## Blocked by the site (every request refused; needs the browser fallback)

- Columbus State University (`ipeds-139366`)
- Emmanuel University (`ipeds-139630`)
- Georgia State University (`ipeds-139940`)
- Lanier Technical College (`ipeds-140243`)
- Reinhardt University (`ipeds-140872`)
- Savannah College of Art and Design (`ipeds-140951`)
- Georgia State University-Perimeter College (`ipeds-244437`)
- Southeastern Technical College (`ipeds-368911`)
- Reformed University (`ipeds-490230`)

## Leads: official pages found with no extracted record

- Abraham Baldwin Agricultural College: admissions_tests, merit_scholarships, ib_credit, transfer_credit, residency, degree_requirements
- Agnes Scott College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, residency, degree_requirements
- Albany State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Albany Technical College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Andrew College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Athens Technical College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, degree_requirements
- Atlanta Metropolitan State College: cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Atlanta Technical College: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Augusta Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, degree_requirements
- Augusta University: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Berry College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Beulah Heights University: tuition_fees, cost_of_attendance, merit_scholarships, degree_requirements
- Brenau University: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Brewton-Parker College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- Central Georgia Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Chattahoochee Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- Clark Atlanta University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Clayton  State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Coastal Pines Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements, aid_appeals
- College of Athens: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- College of Coastal Georgia: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Columbus Technical College: tuition_fees, admissions_tests, transfer_credit, residency
- Covenant College: merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Dalton State College: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, residency, degree_requirements
- East Georgia State College: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency
- Emory University: cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Emory University-Oxford College: cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Fort Valley State University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Georgia College & State University: admissions_tests, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- Georgia Gwinnett College: admissions_tests, common_data_set, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Georgia Highlands College: tuition_fees, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Georgia Institute of Technology-Main Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Georgia Military College: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Georgia Northwestern Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Georgia Piedmont Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Georgia Southern University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency
- Georgia Southwestern State University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- Gordon State College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, residency, degree_requirements
- Gupton Jones College of Funeral Service: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements, aid_appeals
- Gwinnett Technical College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Helms College: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Herzing University-Atlanta: tuition_fees, cost_of_attendance, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Kennesaw State University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- LaGrange College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment
- Life University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Luther Rice College & Seminary: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Mercer University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Middle Georgia State University: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Morehouse College: admissions_tests, common_data_set, merit_scholarships, clep_credit, statewide_articulation, degree_requirements
- Morris Brown College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- North Georgia Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Oconee Fall Line Technical College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Ogeechee Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency
- Oglethorpe University: tuition_fees, cost_of_attendance, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation
- Paine College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Piedmont University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
- Point University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Savannah State University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Savannah Technical College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Shorter University: cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- South Georgia State College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, transfer_credit, residency, degree_requirements, aid_appeals
- South Georgia Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Southern Crescent Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- Southern Regional Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Spelman College: tuition_fees, cost_of_attendance, merit_scholarships, ap_credit, statewide_articulation
- Thomas University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Toccoa Falls College: tuition_fees, dual_enrollment
- Truett McConnell University: tuition_fees, cost_of_attendance, dual_enrollment
- University of Georgia: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- University of North Georgia: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, residency, degree_requirements
- University of West Georgia: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency
- Valdosta State University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Wesleyan College: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, degree_requirements
- West Georgia Technical College: cost_of_attendance, admissions_tests, ap_credit, statewide_articulation, residency, degree_requirements
- Wiregrass Georgia Technical College: tuition_fees, cost_of_attendance, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Young Harris College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
