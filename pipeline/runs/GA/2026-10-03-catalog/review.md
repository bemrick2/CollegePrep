# Review queue — GA (2026-27)

Pages fetched: 2352; failures: 144. Candidates: 430 (82 without issues, 348 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 6 | 0 | 0 | 14 | 24 | 0 | 41 |
| cost_of_attendance | 4 | 0 | 0 | 4 | 34 | 1 | 42 |
| admissions_tests | 2 | 0 | 0 | 1 | 39 | 1 | 42 |
| common_data_set | 2 | 0 | 0 | 1 | 5 | 35 | 42 |
| merit_scholarships | 0 | 1 | 2 | 0 | 36 | 3 | 43 |
| ap_credit | 0 | 6 | 0 | 2 | 17 | 18 | 42 |
| clep_credit | 0 | 5 | 0 | 3 | 6 | 30 | 41 |
| ib_credit | 1 | 4 | 0 | 1 | 7 | 31 | 41 |
| dual_enrollment | 3 | 27 | 4 | 2 | 12 | 5 | 32 |
| transfer_credit | 0 | 8 | 1 | 2 | 30 | 4 | 40 |
| statewide_articulation | 0 | 0 | 0 | 0 | 13 | 28 | 44 |
| residency | 0 | 0 | 0 | 0 | 30 | 11 | 44 |
| degree_requirements | 0 | 0 | 1 | 0 | 37 | 3 | 44 |
| aid_appeals | 0 | 0 | 0 | 29 | 5 | 7 | 44 |

## Ready for review (82)

### `4489d264dfcc0f53` Abraham Baldwin Agricultural College — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.abac.edu/admissions/student_accounts/cost-attendance.html (sha256 6b2ab5c762e5)
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
### `d9dd012d011e839f` Abraham Baldwin Agricultural College — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://www.abac.edu/admissions/student_accounts/cost-attendance.html (sha256 6b2ab5c762e5)
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
  - off_campus_not_with_family:Tuition: 3156 ⟵ “Tuition | $3,156 | $3,156 | $3,156”
  - off_campus_not_with_family:Fees: 748 ⟵ “Fees | $ 748 | $ 748 | $ 748”
  - off_campus_not_with_family:Food: 3186 ⟵ “Food | $4,020 | $2,584 | $3,186”
  - off_campus_not_with_family:Housing: 7390 ⟵ “Housing | $7,330 | $3,690 | $7,390”
  - off_campus_not_with_family:Personal Expenses: 2430 ⟵ “Personal Expenses | $2,430 | $2,430 | $2,430”
  - off_campus_not_with_family:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380 | $1,380”
  - off_campus_not_with_family:Loan Fees: 58 ⟵ “Loan Fees | $ 58 | $ 58 | $ 58”
  - … 2 more rows
### `e985a331dc72ca96` Abraham Baldwin Agricultural College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.abac.edu/admissions/applicants/dual-enrollment-applicants.html (sha256 6fe4929675a7)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “At least 3.0 High School Grade Point Average calculated on RHSC courses completed.”
### `845ac186ec8c6d32` Agnes Scott College — costs 2026-27 · residency=not_applicable [same] (labeled_in_source)
- source: https://www.agnesscott.edu/admission/undergraduate-admission/cost-of-attendance.html (sha256 ec149c6f5791)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 53256 ⟵ “Tuition | $53,256”
  - column:Housing & Dining: 14079 ⟵ “Housing & Dining | $14,079”
  - column:Student Activity Fee: 350 ⟵ “Student Activity Fee | $350”
  - column:Orientation Fee: 250 ⟵ “Orientation Fee | $250”
  - column:TOTAL: 67935 ⟵ “TOTAL | $67,935”
### `d7c68b96e10e6c5b` Agnes Scott College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.agnesscott.edu/admission/undergraduate-admission/transfer-nontraditional-students/index.html (sha256 63745a9007e8)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transfer credit is given for grades of C- or better.”
### `m34a0d0394eaaf1f` Albany State University — credit_policies 2026-27 · policy_kind=dual_enrollment [changed] (source_unlabeled)
- source: https://www.asurams.edu/enrollment-management/dual-enrollment/admissions-information/checklist.php (sha256 f805b12bbb8c)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 5, "tiers": 1}
- change dual_enrollment: `{'eligibility_tiers': [{'grades': [], 'line': 'High school academic GPA of 3.0 or higher.', 'min_hs_gpa': 3.0}, {'grades': [], 'line': 'Have at least a 3.0 High School Grade Point Average calculated on the RHSC courses', 'min_hs_gpa': 3.0}, {'grades': [], 'line': 'grade point average of 3.0 in academic subjects or a numerical average of 80.', 'min_hs_gpa': 3.0}], 'min_hs_gpa': 3.0}` → `{'eligibility_tiers': [{'grades': [], 'min_hs_gpa': 3.0, 'line': 'grade point average of 3.0 in academic subjects or a numerical average of 80.'}, {'grades': [], 'min_hs_gpa': 3.0, 'line': 'Have at least a 3.0 High School Grade Point Average calculated on the RHSC courses'}, {'grades': [], 'min_hs_gpa': 3.0, 'line': 'High school academic GPA of 3.0 or higher.'}], 'min_hs_gpa': 3.0}`
- change additional_source_urls: `['https://www.asurams.edu/enrollment-management/dual-enrollment/admissions-information/index.php', 'https://www.asurams.edu/enrollment-management/dual-enrollment/de-admissions-checklist.php', 'https://www.asurams.edu/enrollment-management/dual-enrollment/dual-enrollment-students.php', 'https://www.asurams.edu/enrollment-management/dual-enrollment/index.php']` → `['https://www.asurams.edu/enrollment-management/dual-enrollment/', 'https://www.asurams.edu/enrollment-management/dual-enrollment/admissions-information/', 'https://www.asurams.edu/enrollment-management/dual-enrollment/de-admissions-checklist.php', 'https://www.asurams.edu/enrollment-management/dual-enrollment/dual-enrollment-students.php']`
  - eligibility_tier: 3.0 ⟵ “grade point average of 3.0 in academic subjects or a numerical average of 80.”
  - eligibility_tier: 3.0 ⟵ “Have at least a 3.0 High School Grade Point Average calculated on the RHSC courses”
  - eligibility_tier: 3.0 ⟵ “High school academic GPA of 3.0 or higher.”
  - eligibility_tier: 3.0 ⟵ “High school academic GPA of 3.0 or higher.”
  - eligibility_tier: 3.0 ⟵ “grade point average of 3.0 in academic subjects or a numerical average of 80.”
### `c1a95d4b5eb6c930` Albany Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.albanytech.edu/admissions/dual-enrollment/coursework (sha256 385760938515)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 15 ⟵ “Courses may be taught face-to-face on the Albany Technical College campuses, on the high school campuses, online, hybrid, or via Tandberg distance education. Students will be allowed to take up to 15 credit hours per semester at each college they attend. Students can enroll in Albany Technical Colle”
### `mf656ea383261cb2` Athens Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://athenstech.edu/programs/high-school-programs/dual-enrollment/ (sha256 dc9b4783ae4e)
- checks: {"fields": [], "merged_pages": 2, "tiers": 3}
  - eligibility_tier: 2.0 ⟵ “11th and 12th grade students interested in diploma or certificate programs must submit an overall GPA of 2.0 or higher after the completion of the 10th grade or other admission test score requirements.”
  - eligibility_tier: 2.5 ⟵ “11th and 12th grade students interested in degree programs must submit an overall GPA of 2.5 or higher after the completion of the 10th grade or other admission test score requirements.”
  - eligibility_tier: 2.0 ⟵ “10th grade students interested in diploma or certificate programs must submit an overall GPA of 2.0 or higher after the completion of the 9th grade or other admission test score requirements.”
  - eligibility_tier: 2.0 ⟵ “11th and 12th grade students interested in diploma or certificate programs must submit an overall GPA of 2.0 or higher after the completion of the 10th grade or other admission test score requirements.”
  - eligibility_tier: 2.5 ⟵ “11th and 12th grade students interested in degree programs must submit an overall GPA of 2.5 or higher after the completion of the 10th grade or other admission test score requirements.”
  - eligibility_tier: 2.0 ⟵ “10th grade students interested in diploma or certificate programs must submit an overall GPA of 2.0 or higher after the completion of the 9th grade or other admission test score requirements.”
### `5592cb3365100249` Atlanta Metropolitan State College — credit_policies 2026-27 · policy_kind=CLEP [same] (source_unlabeled)
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
### `6314c64ca93da7d2` Atlanta Metropolitan State College — credit_policies 2026-27 · policy_kind=AP [same] (source_unlabeled)
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
### `ef7974eead405b57` Atlanta Metropolitan State College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.atlm.edu/students/dualenrollment.aspx (sha256 9f88409456ec)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “3.0 GPA on Required High School Curriculum (RHSC) Courses”
### `fbfad7c04f43513a` Atlanta Metropolitan State College — credit_policies 2026-27 · policy_kind=IB [same] (source_unlabeled)
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
### `a8a0378180cfe9bb` Augusta Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.augustatech.edu/dual-enrollment-section.cms (sha256 c1d7c2c9c1cb)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 15 ⟵ “Students are allowed to take up to 15 credit hours per semester, and courses may be taught on campus, online, or via a hybrid model. Students can enroll in Augusta Technical College courses during the Fall, Spring, or Summer semesters.”
### `2e072ea5844755a4` Central Georgia Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (labeled_in_source)
- source: https://www.centralgatech.edu/wp-content/uploads/pdfs/admissions/highschool/DE_PPT_StudentOrientation.pdf (sha256 9bb2eedc48e7)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 107 ⟵ “standard tuition rate of $107 per credit hour.”
### `e3673bba3c0a9aff` Central Georgia Technical College — credit_policies 2026-27 · policy_kind=AP [same] (source_unlabeled)
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
### `mf63eed5c61cc8d8` Clayton  State University — transfer_policies 2026-27 [changed] (source_unlabeled)
- source: https://www.clayton.edu/admissions/undergrad/transfer (sha256 f96c1e2a89e1)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
- change additional_source_urls: `['https://www.clayton.edu/admissions/undergrad/transfer']` → `['https://www.clayton.edu/admissions/undergrad/transfer.php']`
  - min_grade: C ⟵ “A minimum grade of C or better will be accepted for transfer credit (D’s are accepted in some majors and for some lower division courses, please contact the school or college that you are interested in pursuing for more information).”
  - min_grade: C ⟵ “A minimum grade of C or better will be accepted for transfer credit (D’s are accepted in some majors and for some lower division courses, please contact the school or college that you are interested in pursuing for more information).”
### `m236de510ca668fe` Coastal Pines Technical College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://catalog.coastalpines.edu/student-handbook/transfer-credit-guidelines (sha256 17b49f5b5e7a)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “A grade of "C" or higher has been earned for each course transferred.”
  - min_grade: C ⟵ “Credits from one former institution appearing on the transcript of another institution can neither be evaluated nor accepted for credit without an official transcript from the institution of origin. • A desktop review (evaluation of courses for transfer credit) is required. • A grade of "C" or higher has been earned for each course transferred. • Occupationally related technical coursework should ”
### `4774be6a4611087b` College of Athens — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://collegeofathens.edu/dual-enrollment-students/ (sha256 840befd5aa83)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 295 ⟵ “The cost to attend the College of Athens is simple and very reasonably priced at $295 per credit hour as compared to similar institutions.”
### `ab260e2c4249db58` College of Coastal Georgia — credit_policies 2026-27 · policy_kind=AP [same] (source_unlabeled)
- source: https://catalog.ccga.edu/policies/cpl (sha256 2dbc92406a70)
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
### `62641947d4f1aa3b` College of Coastal Georgia — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://catalog.ccga.edu/policies/graduation (sha256 f1c433ba5ce9)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 20 ⟵ “All students must complete 20 of the last 30 semester credit hours preceding graduation at the College.”
  - residency_requirement_credits: 20 ⟵ “Complete the residency requirement: Career Associate students must complete 24 credit hours at the College Associate of Science/Associate of Arts in core curriculum students must complete 20 credit hours at the College All students must complete 20 of the last 30 semester credit hours preceding graduation at the College.”
### `9c7db13b5c361cd6` Dalton State College — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://www.daltonstate.edu/admissions/financial-aid/cost-of-attendance/ (sha256 628eacc87108)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Books, Course Materials and Supplies: 1330 ⟵ “Books, Course Materials and Supplies | $1,330”
  - on_campus:Housing & Food: 10838 ⟵ “Housing & Food | $10,838”
  - on_campus:Loan Fees: 61 ⟵ “Loan Fees | $61”
  - on_campus:Miscellaneous and Personal Expenses: 2430 ⟵ “Miscellaneous and Personal Expenses | $2,430”
  - on_campus:Estimated Tuition & Fees: 4231 ⟵ “Estimated Tuition & Fees | $4,231”
  - on_campus:Estimated Transportation Costs: 1380 ⟵ “Estimated Transportation Costs | $1,380”
  - on_campus:Total:: 20270 ⟵ “Total: | $20,270”
### `9c972d1980a665a2` Dalton State College — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://www.daltonstate.edu/admissions/financial-aid/cost-of-attendance/ (sha256 628eacc87108)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Books, Course Materials and Supplies: 1330 ⟵ “Books, Course Materials and Supplies | $1,330”
  - on_campus:Housing & Food: 10838 ⟵ “Housing & Food | $10,838”
  - on_campus:Loan Fees: 61 ⟵ “Loan Fees | $61”
  - on_campus:Miscellaneous and Personal Expenses: 2430 ⟵ “Miscellaneous and Personal Expenses | $2,430”
  - on_campus:Estimated Tuition & Fees: 10508 ⟵ “Estimated Tuition & Fees | $10,508”
  - on_campus:Estimated Transportation Costs: 1380 ⟵ “Estimated Transportation Costs | $1,380”
  - on_campus:Total:: 26547 ⟵ “Total: | $26,547”
### `me5befd85dc1b99b` Fort Valley State University — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.fvsu.edu/admissions/dual-enrollment (sha256 9439713e1234)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “To be admitted high school juniors and seniors must have a minimum 3.0 GPA based on the in-progress RHSC units.”
  - eligibility_tier: 3.0 ⟵ “To be admitted high school sophomores must have a minimum 3.0 GPA based on the in-progress RHSC units.”
  - eligibility_tier: 3.0 ⟵ “To be admitted high school juniors and seniors must have a minimum 3.0 GPA based on the in-progress RHSC units.”
  - eligibility_tier: 3.0 ⟵ “To be admitted high school sophomores must have a minimum 3.0 GPA based on the in-progress RHSC units.”
### `b647b13572affff7` Georgia Highlands College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.highlands.edu/how-do-i-apply/dual-enrollment/ (sha256 168a7f72ff67)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Must have a high school GPA of 3.0 in core curriculum classes.”
### `0ef786096cfb35c1` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-chemistry-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/chemistry-bs/ (sha256 6812a6769db0)
- checks: {"courses": 2, "groups": 1, "groups_skipped": 0}
  - program_name: Bachelor of Science in Chemistry | Georgia Tech Catalog ⟵ “Bachelor of Science in Chemistry | Georgia Tech Catalog”
### `5f0215e663dff385` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-physics-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/physics-bs/ (sha256 f046807c2452)
- checks: {"courses": 3, "groups": 1, "groups_skipped": 0}
  - program_name: Bachelor of Science in Physics | Georgia Tech Catalog ⟵ “Bachelor of Science in Physics | Georgia Tech Catalog”
### `667177c96f40d007` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-mathematics-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-bs/ (sha256 33dbaa68d4a1)
- checks: {"courses": 2, "groups": 1, "groups_skipped": 0}
  - program_name: Bachelor of Science in Mathematics | Georgia Tech Catalog ⟵ “Bachelor of Science in Mathematics | Georgia Tech Catalog”
### `9cd485672d41ce12` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-biology-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biology-bs/ (sha256 ec9e3c6e4ffa)
- checks: {"courses": 3, "groups": 1, "groups_skipped": 0}
  - program_name: Bachelor of Science in Biology | Georgia Tech Catalog ⟵ “Bachelor of Science in Biology | Georgia Tech Catalog”
### `d3a7cf21f2897e2c` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-computer-science-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/computer-science-bs/ (sha256 b2a29b7803c2)
- checks: {"courses": 5, "groups": 2, "groups_skipped": 0}
  - program_name: Bachelor of Science in Computer Science | Georgia Tech Catalog ⟵ “Bachelor of Science in Computer Science | Georgia Tech Catalog”
### `d8eb7a8419a86870` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-biochemistry-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biochemistry-bs/ (sha256 074af909ef30)
- checks: {"courses": 2, "groups": 1, "groups_skipped": 0}
  - program_name: Bachelor of Science in Biochemistry | Georgia Tech Catalog ⟵ “Bachelor of Science in Biochemistry | Georgia Tech Catalog”
### `f0eacf5f6accc98b` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-civil-engineering-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/civil-engineering-bs/ (sha256 9a81a883aa00)
- checks: {"courses": 7, "groups": 1, "groups_skipped": 0}
  - program_name: Bachelor of Science in Civil Engineering | Georgia Tech Catalog ⟵ “Bachelor of Science in Civil Engineering | Georgia Tech Catalog”
### `52afc911d219cad5` Georgia Institute of Technology-Main Campus — credit_policies 2026-27 · policy_kind=IB [same] (labeled_in_source)
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
### `c2c4adb74e683393` Georgia Institute of Technology-Main Campus — credit_policies 2026-27 · policy_kind=dual_enrollment [changed] (source_unlabeled)
- source: https://admission.gatech.edu/dual-enrollment/distance-math (sha256 d437869a912d)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
- change dual_enrollment: `{'eligibility_tiers': [{'grades': [], 'line': '3.5 unweighted GPA.', 'min_hs_gpa': 3.5}, {'grades': [], 'line': '3.5 unweighted GPA', 'min_hs_gpa': 3.5}], 'min_hs_gpa': 3.5, 'per_credit_hour_charges': [{'amount': 353.93, 'kind': 'tuition', 'line': 'Tuition: $353.93 per credit hour for Georgia residents.'}], 'tuition_per_credit_hour': 353.93}` → `{'eligibility_tiers': [{'grades': [], 'min_hs_gpa': 3.5, 'line': '3.5 unweighted GPA'}], 'min_hs_gpa': 3.5}`
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA”
### `76abba5d4f61398e` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-computer-science-georgia-tech-catalog · requirement_key=research-for-credit [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/computer-science-bs/ (sha256 b2a29b7803c2)
  - courses: CS 2699 ⟵ “CS 2699 - Undergraduate Research (Freshman and Sophomore)”
  - courses: CS 4699 ⟵ “CS 4699 - Undergraduate Research (Junior and Senior)”
  - courses: CS 4980 ⟵ “CS 4980 - Research Capstone Project”
### `bb9124e8997fa361` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-computer-science-georgia-tech-catalog · requirement_key=research-for-pay-audit-only [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/computer-science-bs/ (sha256 b2a29b7803c2)
  - courses: CS 2698 ⟵ “CS 2698 - Undergraduate Research Assistantship (Freshman and Sophomore)”
  - courses: CS 4698 ⟵ “CS 4698 - Undergraduate Research Assistantship (Junior and Senior)”
### `ffb78d0605a9b828` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-civil-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-civil-engineering [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/civil-engineering-bs/ (sha256 9a81a883aa00)
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
  - courses: MATH 2552 ⟵ “MATH 2552 - Differential Equations”
  - courses: PHYS 2211 ⟵ “PHYS 2211 - Principles of Physics I”
  - courses: CHEM 1310 ⟵ “CHEM 1310 - Principles of General Chemistry for Engineers”
  - courses: COE 2001 ⟵ “COE 2001 - Statics”
### `bea7807c60f0d34f` Georgia Military College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.gmc.edu/dual-enrollment/ (sha256 a63c87791ee8)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.0 ⟵ “Juniors or Seniors with a 2.0 or higher GPA”
  - eligibility_tier: 2.0 ⟵ “Minimum cumulative unweighted high school grade point average of 2.0 on a 4.00 scale.”
### `226338685b3f74a5` Georgia Northwestern Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.gntc.edu/dual-enrollment/ (sha256 e7f82bcdebe5)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “Have a high school GPA of 2.0 documented with a high school transcript, OR have acceptable standardized test scores. Transcripts and test scores are generally provided by the high school.”
### `a6c197912b1555fc` Gordon State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.gordonstate.edu/admissions/types-of-students/de-to-fr/index.html (sha256 209ef6f5e679)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “Applicants may be awarded a regular admission with a current high school transcript IF the students has a 2.0 GPA in the RHSC and less than 5 deficiencies.”
### `11fdde3c8c004617` Gordon State College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.gordonstate.edu/admissions/types-of-students/transfer/index.html (sha256 b84edb4103c7)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 42 ⟵ “Transfer Credit Equivalencies No more than 42 semester hours of combined transfer credit from all sources will be accepted towards an associate degree.”
### `9c4d433e9467243f` Gupton Jones College of Funeral Service — credit_policies 2026-27 · policy_kind=AP [same] (source_unlabeled)
- source: https://gupton-jones.edu/admissions/advanced-placement/ (sha256 96cd708b4e2d)
- checks: {"distinct_exams": 8, "equivalencies": 8, "rows_without_score": 0}
  - equivalencies[AP-PRECALCULUS|3+]:  ⟵ “Precalculus | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-CALCULUS-AB|3+]:  ⟵ “Calculus AB | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-CALCULUS-BC|3+]:  ⟵ “Calculus BC | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-STATISTICS|3+]:  ⟵ “Statistics | 3+ | MAT 100 – Mathematics for Business | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language & Composition | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-RESEARCH|3+]:  ⟵ “Research | 3+ | ENG 100 – English Grammar and Composition | 4”
  - equivalencies[AP-SEMINAR|3+]:  ⟵ “Seminar | 3+ | ENG 100 – English Grammar and Composition | 4”
### `9365bab6eb4a5e38` Luther Rice College & Seminary — credit_policies 2026-27 · policy_kind=CLEP [same] (source_unlabeled)
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
### `de947fb21f6a9f88` Luther Rice College & Seminary — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.lutherrice.edu/degree-programs/dual_enrollment (sha256 64f3ca92d76c)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 250 ⟵ “In-State and Out-of-State DE tuition is $750.00 per course ($250/credit hr). Books will be covered in-state but are not covered out-of-state.”
  - per_credit_hour_charge: 250 ⟵ “However, Out-of-State students do not qualify for Georgia state DE funding. Instead, you will pay Luther Rice's listed price of $750.00 per course ($250/credit hr). Books will be covered in-state but are not covered out-of-state.”
### `m4a420f47ac2098a` Middle Georgia State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mga.edu/academics/docs/transfer-agreements/Articulation_Agreement_Georgia_Piedmont_Technical_College.pdf (sha256 caaa03d9cf23)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - residency_requirement_credits: 30 ⟵ “Any stude nt ad mitted to MG SC for the f inal year mu st be in res idence for two semesters and mu st complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
  - residency_requirement_credits: 30 ⟵ “Any student admitted to Middle Georgia State College for the final year must be in residence for two semesters and must complete at least 30 semester hours in residence, including 21 hours of upper division work in the major. 10.”
### `b56a9586172eecfb` Oconee Fall Line Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://oftc.edu/admissions/dual-enrollment-high-school-students/ (sha256 b8b13494c3c1)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.6 ⟵ “| High school GPA 2.6 or higher”
  - eligibility_tier: 2.6 ⟵ “High school GPA 2.6 or higher”
  - eligibility_tier: 2.6 ⟵ “| High school GPA 2.6 or higher”
  - eligibility_tier: 2.6 ⟵ “High school GPA 2.6 or higher”
### `e32cdd7181ee5e29` Piedmont University — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.piedmont.edu/admissions-aid/apply/dual-enrollment-students/ (sha256 8d495fada685)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a 3.0 or higher grade point average (GPA) in their high school coursework.”
### `512d29c5df8d9809` Point University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://point.edu/admissions/dual-enrollment/ (sha256 39aa58bdccfb)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 1}
  - state_grant_accepted: True ⟵ “Even better, students who participate in the Dual Credit Enrollment program may be eligible for a Dual Enrollment Scholarship after graduating from high school if they are admitted to a Point University residential undergraduate program — helping make the transition from high school to college even ”
  - per_credit_hour_charge: 250 ⟵ “Point offers dual-credit enrollment courses on our main campus in West Point, at our off-site locations (Peachtree City and Savannah), online, and at select partnering high schools in Georgia. These courses are available at a discounted rate of $250 per credit hour. For more information, please cont”
  - eligibility_tier: 3.0 ⟵ “High school GPA of 3.0 minimum.”
### `2b2041164df5f0bd` Savannah Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.savannahtech.edu/admissions/dual-enrollment-students/ (sha256 71c587545c2f)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.6 ⟵ “Degree/diploma level programs require a 2.6 GPA and TCC level programs require a 2.0 GPA.  Please have your high school email us your official transcript to [email protected]”
### `87d384e93cdc0223` South Georgia State College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (source_unlabeled)
- source: https://www.sgsc.edu/admissions/dual-enrollment (sha256 519c2ba3c3f7)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Minimum high school GPA of 3.0 or higher, as calculated based on Required High School Curriculum courses”
  - eligibility_tier: 3.0 ⟵ “Minimum high school GPA of 3.0 or higher, as calculated based on Required High School Curriculum (RHSC) courses.”
### `70634214d703c788` Thomas University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.thomasu.edu/become-a-student/admission-process/on-campus/ (sha256 3876c91d7578)
- checks: {"thresholds": null}
  - award_tiers: [{'unweighted gpa': '3.9+', 'amount_text': '$7,000'}, {'unweighted gpa': '3.7 - 3.89', 'amount_text': '$5,000'}, {'unweighted gpa': '3.5 - 3.69', 'amount_text': '$3,000'}] ⟵ “Unweighted GPA | Scholarship || 3.9+ | $7,000 || 3.7 - 3.89 | $5,000 || 3.5 - 3.69 | $3,000”
  - gpa_requirement: Tiered by Unweighted GPA: 3.9+ → $7,000; 3.7 - 3.89 → $5,000; 3.5 - 3.69 → $3,000 ⟵ “Unweighted GPA | Scholarship || 3.9+ | $7,000 || 3.7 - 3.89 | $5,000 || 3.5 - 3.69 | $3,000”
### `031620173a83f368` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Rotary Club of Carrollton Scholarship | The Rotary Club of Carrollton Scholarship are for students who reside in Carroll County. Student must have minimum GPA of 2.5. | $500 | 1”
  - eligibility_summary: The Rotary Club of Carrollton Scholarship are for students who reside in Carroll County. Student must have minimum GPA of 2.5. ⟵ “Rotary Club of Carrollton Scholarship | The Rotary Club of Carrollton Scholarship are for students who reside in Carroll County. Student must have minimum GPA of 2.5. | $500 | 1”
### `0b89f49391f85e73` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Bowdon Hospital Authority Scholarship | Health Sciences or Nursing Programs; Carroll, Coweta, Douglas, Haralson counties and Cleburne or Randolph counties in Alabama residents. Preference to 30108 ZIP Code. | $500 | 2”
  - eligibility_summary: Health Sciences or Nursing Programs; Carroll, Coweta, Douglas, Haralson counties and Cleburne or Randolph counties in Alabama residents. Preference to 30108 ZIP Code. ⟵ “Bowdon Hospital Authority Scholarship | Health Sciences or Nursing Programs; Carroll, Coweta, Douglas, Haralson counties and Cleburne or Randolph counties in Alabama residents. Preference to 30108 ZIP Code. | $500 | 2”
### `104ea6405b933051` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “WellStar Douglas Hospital Scholarship | Students must be enrolled in Health Sciences or Nursing Programs. The Douglas Campus must be students home campus. Student must have a GPA of 2.5 or greater. | $1,000 | 3”
  - eligibility_summary: Students must be enrolled in Health Sciences or Nursing Programs. The Douglas Campus must be students home campus. Student must have a GPA of 2.5 or greater. ⟵ “WellStar Douglas Hospital Scholarship | Students must be enrolled in Health Sciences or Nursing Programs. The Douglas Campus must be students home campus. Student must have a GPA of 2.5 or greater. | $1,000 | 3”
### `10a4f3baf21e7259` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Carrollton Golden K Scholarship | Must be a new student and a Carroll County resident | $1,000 | 2”
  - eligibility_summary: Must be a new student and a Carroll County resident ⟵ “Carrollton Golden K Scholarship | Must be a new student and a Carroll County resident | $1,000 | 2”
### `27712aad025ffdf2` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Mullins Mechanical Pillar Scholarship | The student must be furthering their college education by enrolling at West Georgia Technical College and pursuing a certificate, diploma, or degree in Industrial Systems Technology, Welding and Joining Technology, Engineering Technology, Accounting, Business ”
  - eligibility_summary: The student must be furthering their college education by enrolling at West Georgia Technical College and pursuing a certificate, diploma, or degree in Industrial Systems Technology, Welding and Joining Technology, Engineering Technology, Accounting, Business Management, or Business Technology. The student must have a minimum GPA of 2.5. ⟵ “Mullins Mechanical Pillar Scholarship | The student must be furthering their college education by enrolling at West Georgia Technical College and pursuing a certificate, diploma, or degree in Industrial Systems Technology, Welding and Joining Technology, Engineering Technology, Accounting, Business ”
### `2aa44c8a5c8c43a6` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1000 ⟵ “Doug and Carol Mabry Scholarship Fund | One scholarship will be designated to a Diesel Equipment Technology student, and the other scholarship will be designated to a Welding & Joining Technology student. | $1000 | 2”
  - eligibility_summary: One scholarship will be designated to a Diesel Equipment Technology student, and the other scholarship will be designated to a Welding & Joining Technology student. ⟵ “Doug and Carol Mabry Scholarship Fund | One scholarship will be designated to a Diesel Equipment Technology student, and the other scholarship will be designated to a Welding & Joining Technology student. | $1000 | 2”
### `2c34a42579073628` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Tim B. Clower Scholarship | The Tim B. Clower Scholarship Fund is for students who reside in a home served by GreyStone Power or whose parent or guardian resides in a home served by GreyStone Power. Minimum GPA, 2.5. FALL SEMESTER ONLY | $2,500 | 1”
  - eligibility_summary: The Tim B. Clower Scholarship Fund is for students who reside in a home served by GreyStone Power or whose parent or guardian resides in a home served by GreyStone Power. Minimum GPA, 2.5. FALL SEMESTER ONLY ⟵ “Tim B. Clower Scholarship | The Tim B. Clower Scholarship Fund is for students who reside in a home served by GreyStone Power or whose parent or guardian resides in a home served by GreyStone Power. Minimum GPA, 2.5. FALL SEMESTER ONLY | $2,500 | 1”
### `30d548aa83709bf0` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “The Gene Haas Foundation Scholarship | CNC Technology students and/or NIMS credentials | $2,500 | Varies”
  - eligibility_summary: CNC Technology students and/or NIMS credentials ⟵ “The Gene Haas Foundation Scholarship | CNC Technology students and/or NIMS credentials | $2,500 | Varies”
### `320c833995028386` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Rotary Club of Carrollton-Dawnbreakers Scholarship | The Rotary Club of Carrollton-Dawnbreakers Scholarship are for students who reside in Carroll County. Preference to students who were awarded the Rotary Club of Carrollton-Dawnbreakers GED Scholarship. | $500 | 2”
  - eligibility_summary: The Rotary Club of Carrollton-Dawnbreakers Scholarship are for students who reside in Carroll County. Preference to students who were awarded the Rotary Club of Carrollton-Dawnbreakers GED Scholarship. ⟵ “Rotary Club of Carrollton-Dawnbreakers Scholarship | The Rotary Club of Carrollton-Dawnbreakers Scholarship are for students who reside in Carroll County. Preference to students who were awarded the Rotary Club of Carrollton-Dawnbreakers GED Scholarship. | $500 | 2”
### `3d02e94ad762f56f` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Southwire Machine Tool Technology Scholarship | Machine Tool Technology Program; Carroll Campus only | $500 | 10”
  - eligibility_summary: Machine Tool Technology Program; Carroll Campus only ⟵ “Southwire Machine Tool Technology Scholarship | Machine Tool Technology Program; Carroll Campus only | $500 | 10”
### `3de3d4c78e30dacc` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Coweta-Fayette EMC Scholarship | Open to students attending CEC, Coweta Campus, or Franklin Site | $500 | 1”
  - eligibility_summary: Open to students attending CEC, Coweta Campus, or Franklin Site ⟵ “Coweta-Fayette EMC Scholarship | Open to students attending CEC, Coweta Campus, or Franklin Site | $500 | 1”
### `5f15f3f3602edcef` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Manufacturers Education Foundation Scholarship | Student must be enrolled in one of the following areas of study: Electrical Construction and Maintenance, Electronics and Telecommunications, Engineering Technology, Industrial Systems Technology, Machine Tool Technology, Precision Manufacturing and M”
  - eligibility_summary: Student must be enrolled in one of the following areas of study: Electrical Construction and Maintenance, Electronics and Telecommunications, Engineering Technology, Industrial Systems Technology, Machine Tool Technology, Precision Manufacturing and Maintenance, Welding and Joining Technology. ⟵ “Manufacturers Education Foundation Scholarship | Student must be enrolled in one of the following areas of study: Electrical Construction and Maintenance, Electronics and Telecommunications, Engineering Technology, Industrial Systems Technology, Machine Tool Technology, Precision Manufacturing and M”
### `66e24404db7fb622` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Star Foundation Scholarship | Haralson County and Cleburne or Randolph counties in Alabama residents. | $500 | 1”
  - eligibility_summary: Haralson County and Cleburne or Randolph counties in Alabama residents. ⟵ “Star Foundation Scholarship | Haralson County and Cleburne or Randolph counties in Alabama residents. | $500 | 1”
### `7e6b0978feadea79` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: Varies:Scholarship covers student's remaining balance after financial aid is applied. ⟵ “Microsoft Scholars Program | Student must be enrolled in one of the following areas of study: Computer Support Specialist, Networking Specialist, PC Repair and Network Technician, or Helpdesk Specialist. Student must have a home campus of Douglas. Student must have a minimum GPA of 2.0. Student will”
  - eligibility_summary: Student must be enrolled in one of the following areas of study: Computer Support Specialist, Networking Specialist, PC Repair and Network Technician, or Helpdesk Specialist. Student must have a home campus of Douglas. Student must have a minimum GPA of 2.0. Student will continue to receive the award each semester until program completion as long as aforementioned criteria is maintained. ⟵ “Microsoft Scholars Program | Student must be enrolled in one of the following areas of study: Computer Support Specialist, Networking Specialist, PC Repair and Network Technician, or Helpdesk Specialist. Student must have a home campus of Douglas. Student must have a minimum GPA of 2.0. Student will”
### `81916ba06474db59` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “GreyStone Power Capstone Scholarship | Douglas County resident | $500 | 2”
  - eligibility_summary: Douglas County resident ⟵ “GreyStone Power Capstone Scholarship | Douglas County resident | $500 | 2”
### `8fd63306ebf60833` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Carroll EMC: Robert D. Tisinger Scholarship Fund | Must live in a home served by Carroll EMC or parent/guardian must live in a home served by Carroll EMC | $500 | 15”
  - eligibility_summary: Must live in a home served by Carroll EMC or parent/guardian must live in a home served by Carroll EMC ⟵ “Carroll EMC: Robert D. Tisinger Scholarship Fund | Must live in a home served by Carroll EMC or parent/guardian must live in a home served by Carroll EMC | $500 | 15”
### `94cc15e8747f3a41` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “The Swope Family Fund Pillar Scholarship | Scholarship open to any program of study to students that reside in Coweta County. | $500 | 4”
  - eligibility_summary: Scholarship open to any program of study to students that reside in Coweta County. ⟵ “The Swope Family Fund Pillar Scholarship | Scholarship open to any program of study to students that reside in Coweta County. | $500 | 4”
### `982587ee43fb58cf` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Southwire Precision Manufacturing & Maintenance Scholarship | Precision Manufacturing & Maintenance Program; Carroll Campus only | $500 | 10”
  - eligibility_summary: Precision Manufacturing & Maintenance Program; Carroll Campus only ⟵ “Southwire Precision Manufacturing & Maintenance Scholarship | Precision Manufacturing & Maintenance Program; Carroll Campus only | $500 | 10”
### `a07dc8097e6e39bc` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Kiwanis Club of LaGrange Frear Family Scholarship | The recipient must be a veteran, first responder, or military member, or the spouse or child of a veteran, first responder, or military member, and they must be a resident of Troup, Coweta, Heard, Meriwether, or Harris County. | $500 | 2”
  - eligibility_summary: The recipient must be a veteran, first responder, or military member, or the spouse or child of a veteran, first responder, or military member, and they must be a resident of Troup, Coweta, Heard, Meriwether, or Harris County. ⟵ “Kiwanis Club of LaGrange Frear Family Scholarship | The recipient must be a veteran, first responder, or military member, or the spouse or child of a veteran, first responder, or military member, and they must be a resident of Troup, Coweta, Heard, Meriwether, or Harris County. | $500 | 2”
### `a3cefc453d9a18d3` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “J. Randy Jackson Legacy Scholarship | Must have completed coursework at the thINC Academy and be attending the LaGrange Campus. Must be an incoming student. | $500 | 1”
  - eligibility_summary: Must have completed coursework at the thINC Academy and be attending the LaGrange Campus. Must be an incoming student. ⟵ “J. Randy Jackson Legacy Scholarship | Must have completed coursework at the thINC Academy and be attending the LaGrange Campus. Must be an incoming student. | $500 | 1”
### `a8fa1b8af57715b1` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Holland M. Ware Trade and Industrial Scholarship | Must be pursing a degree in Manufacturing & Production, Installation & Repair Programs; Home Campus must be Coweta, LaGrange, Franklin, or Greenville. | $1,000 | Varies”
  - eligibility_summary: Must be pursing a degree in Manufacturing & Production, Installation & Repair Programs; Home Campus must be Coweta, LaGrange, Franklin, or Greenville. ⟵ “Holland M. Ware Trade and Industrial Scholarship | Must be pursing a degree in Manufacturing & Production, Installation & Repair Programs; Home Campus must be Coweta, LaGrange, Franklin, or Greenville. | $1,000 | Varies”
### `adbb385cb2f408c9` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Parkway Hospital Auxiliary Scholarship | Health Sciences or Nursing Programs; Douglas Co. Resident | $500 | 3”
  - eligibility_summary: Health Sciences or Nursing Programs; Douglas Co. Resident ⟵ “Parkway Hospital Auxiliary Scholarship | Health Sciences or Nursing Programs; Douglas Co. Resident | $500 | 3”
### `c37c82dd5af3cd0c` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Tritt Family Foundation, Inc. Scholarship | Student must have a GPA of at least 3.5 and must be working at least 20 hours per week. The student will automatically receive the scholarship the following semester as long as they continue to maintain a 3.5 GPA. | $500 | 2”
  - eligibility_summary: Student must have a GPA of at least 3.5 and must be working at least 20 hours per week. The student will automatically receive the scholarship the following semester as long as they continue to maintain a 3.5 GPA. ⟵ “Tritt Family Foundation, Inc. Scholarship | Student must have a GPA of at least 3.5 and must be working at least 20 hours per week. The student will automatically receive the scholarship the following semester as long as they continue to maintain a 3.5 GPA. | $500 | 2”
### `c66407dbd71859e8` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Southwire Industrial Systems Technology Scholarship | Industrial Systems Technology Program; Carroll Campus only | $500 | 10”
  - eligibility_summary: Industrial Systems Technology Program; Carroll Campus only ⟵ “Southwire Industrial Systems Technology Scholarship | Industrial Systems Technology Program; Carroll Campus only | $500 | 10”
### `d2aa9df7117df938` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Holland M. Ware Healthcare, Nursing, and Public Services Scholarship | Must be pursuing a degree in Nursing, Business Management, Healthcare Management; Home Campus must be Coweta, LaGrange, Franklin, or Greenville. | $1,000 | Varies”
  - eligibility_summary: Must be pursuing a degree in Nursing, Business Management, Healthcare Management; Home Campus must be Coweta, LaGrange, Franklin, or Greenville. ⟵ “Holland M. Ware Healthcare, Nursing, and Public Services Scholarship | Must be pursuing a degree in Nursing, Business Management, Healthcare Management; Home Campus must be Coweta, LaGrange, Franklin, or Greenville. | $1,000 | Varies”
### `e1a09c6b7e835b10` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - eligibility_summary: This scholarship is open to veterans enrolled in any program of study for certificate, diploma, or degree. Home campus must be Coweta, LaGrange, Greenville, or Franklin. ⟵ “Holland M. Ware Veterans Scholarship | This scholarship is open to veterans enrolled in any program of study for certificate, diploma, or degree. Home campus must be Coweta, LaGrange, Greenville, or Franklin. | Varies | Varies”
### `e305e9b6cbdb4a9e` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - eligibility_summary: Open to students in any automotive related fields of study with a minimum GAP of 2.0. ⟵ “Georgia Automotive Dealers Association Scholarship | Open to students in any automotive related fields of study with a minimum GAP of 2.0. | Varies | Varies”
### `e3ad56aa54a7f6e6` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Abraham Baldwin Chapter NSDAR Scholarship | Open to full time students enrolled in an Allied Healthcare program of study. Must have a minimum 3.0 GPA and be a resident of Carroll, Douglas, Heard, haralson, Coweta, Meriwether, or Troup County. SUMMER SEMESTER ONLY | $500 | 1”
  - eligibility_summary: Open to full time students enrolled in an Allied Healthcare program of study. Must have a minimum 3.0 GPA and be a resident of Carroll, Douglas, Heard, haralson, Coweta, Meriwether, or Troup County. SUMMER SEMESTER ONLY ⟵ “Abraham Baldwin Chapter NSDAR Scholarship | Open to full time students enrolled in an Allied Healthcare program of study. Must have a minimum 3.0 GPA and be a resident of Carroll, Douglas, Heard, haralson, Coweta, Meriwether, or Troup County. SUMMER SEMESTER ONLY | $500 | 1”
### `e72872fcbfe31957` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “WGTC Foundation Scholarship | Open to all students | $500 | 5”
  - eligibility_summary: Open to all students ⟵ “WGTC Foundation Scholarship | Open to all students | $500 | 5”
### `f18bd6dc5d6098cc` West Georgia Technical College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/discover-wgtc/foundation/foundation-scholarship/ (sha256 cdffe2adbbae)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Caterpillar DEM Grant Fund Scholarship | Diesel Equipment Tech & Heavy Diesel Service Tech Programs | $500 | 6”
  - eligibility_summary: Diesel Equipment Tech & Heavy Diesel Service Tech Programs ⟵ “Caterpillar DEM Grant Fund Scholarship | Diesel Equipment Tech & Heavy Diesel Service Tech Programs | $500 | 6”
### `m012da3bfe6bef2b` West Georgia Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [same] (labeled_in_source)
- source: https://www.westgatech.edu/wp-content/uploads/DE.Student.Handbook.2026-2027-ada-7.23.26.pdf (sha256 34a98a81fa79)
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 3}
  - per_credit_hour_charge: 107 ⟵ “application will result in the student being responsible for their tuition balance. At WGTC, tuition is $107 per credit”
  - eligibility_tier: 2.0 ⟵ “If student has a 2.00 high school GPA, no admissions tes�ng or ACT/SAT is required.”
  - eligibility_tier: 2.0 ⟵ “•   11th and 12th graders with a 2.00 high school GPA can enroll in academic core classes or occupational”
  - eligibility_tier: 2.0 ⟵ “If a student does not have a 2.00 high school GPA, students will need acceptable test scores for entry. At WGTC we”
  - max_credit_hours_per_term: 15 ⟵ “Dual Enrollment students may register for a maximum 15 credit hours during the fall, spring, and summer”
  - eligibility_tier: 2.0 ⟵ “Have a high school GPA of 2.0 documented with official high school transcript, OR have acceptable standardized test scores OR ACCUPLACER scores.”
### `a3255fc09759025f` West Georgia Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.westgatech.edu/admissions/registrars-office/policies/ (sha256 951995ce6851)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Previous course work must have been completed with a grade of C (2.0) or better to be considered for transfer credit. 5.”

## Exceptions (348)

### `29b68663d0ab4270` Abraham Baldwin Agricultural College — credit_policies 2024-25 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.abac.edu/academic-policies-and-procedures/college-level-examination-program-clep (sha256 4acaef8977c4)
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
### `8f8c179f8c48c26a` Abraham Baldwin Agricultural College — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://catalog.abac.edu/admissions/de (sha256 e9e6dd35712c)
- issues: stale_year_label:2024-25
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Students must have at least a minimum 3.0 High School Grade Point Average (HSGPA) as calculated by the institution for admission purposes and exempt Learning Support requirements.”
### `a623898b412d518b` Abraham Baldwin Agricultural College — credit_policies 2024-25 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.abac.edu/academic-policies-and-procedures/advanced-placement-ap-program (sha256 0cf8b26f8192)
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
### `cb58fa24ea0ad2a7` Abraham Baldwin Agricultural College — transfer_policies 2024-25 [new] (labeled_in_source)
- source: https://catalog.abac.edu/academic-policies-and-procedures/residency-requirements-for-graduation (sha256 214c0a5a5c12)
- issues: stale_year_label:2024-25, conflicting_values:residency_requirement_credits
- checks: {"fields": []}
### `37835e455a496579` Agnes Scott College — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.agnesscott.edu/assets/documents/institutional-research/cds_2024_2025.pdf (sha256 66b729d28a01)
- issues: applications_breakdown_does_not_reconcile, admits_breakdown_does_not_reconcile, enrolled_breakdown_does_not_reconcile, stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 349 ⟵ “Total first-time, first-year who applied                                                  2090              1000          741           349”
  - admits: 74 ⟵ “Total first-time, first-year who were admitted                                            1299               716          509            74”
  - enrolled: 2 ⟵ “Total first-time, first-year who enrolled                                                  210               149           59             2”
  - sat_composite_25..75: [1160, 1250, 1340] ⟵ “SAT Composite                       1160                       1250               1340”
  - sat_reading_25..75: [620, 670, 700] ⟵ “SAT Evidence-Based Reading and       620                        670                700”
  - sat_math_25..75: [540, 580, 640] ⟵ “SAT Math                             540                        580                640”
  - act_25..75: [25, 27, 31] ⟵ “ACT Composite                        25                         27                 31”
### `a781ef44ea86631b` Agnes Scott College — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.agnesscott.edu/assets/documents/institutional-research/cds_2025_2026.pdf (sha256 d22c312ade05)
- issues: c1_totals_incomplete
- checks: {"fields": ["act_25", "act_50", "act_75", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 2070 ⟵ “Total first-time, first-year (degree-seeking) who applied                 1049                 613               408                    2070”
  - enrolled: 198 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                    145              50                     3                     198”
  - sat_composite_25..75: [1098, 1220, 1280] ⟵ “SAT Composite                                      1098                 1220              1280”
  - sat_reading_25..75: [570, 645, 673] ⟵ “SAT Evidence-Based Reading and   570                  645               673”
  - sat_math_25..75: [510, 580, 613] ⟵ “SAT Math                                           510                  580               613”
  - act_25..75: [25, 28, 31] ⟵ “ACT Composite                                       25                   28                31”
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
### `d1a5ba77b528c56e` Albany Technical College — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.albanytech.edu/college-catalog/current/transfer-credit (sha256 24d82f0d3f55)
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
### `24960f48a4ad1851` Athens Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://athenstech.edu/admissions-financial-aid/tuition-financial-aid/financial-aid-policies/ (sha256 f3066eba701f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “A Request for Appeal of Financial Aid Exclusion form must be submitted explaining the extenuating circumstances, how these circumstances have changed, and their plan to maintain satisfactory academic progress if the appeal is approved.”
### `52886e35a471b9f2` Athens Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: https://athenstech.edu/admissions-financial-aid/tuition-financial-aid/ (sha256 541ff822d7d4)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Athens, GA 30601 Fax to: (706) 425-3086 Email to: Scanned copies to financialaid@athenstech.edu Deliver to: Financial Aid in the H-700 Building, Athens Main Campus Sign Up For A Payment Plan Professional Judgement Dependency Override Appeal Athens Technical College understands that navigating the financial aid process can be daunting, and the Athens Technical College Financial Aid Staff Members ar”
  - sentence: professional_judgment ⟵ “Financial Aid Administrators are authorized to use professional judgement on a case-by-case basis for students with special circumstances that affect a family’s ability to pay for college education that are not reflected in the information provided on the FAFSA.”
  - sentence: professional_judgment ⟵ “In many cases, professional judgement adjustments made to the FAFSA do no result in significant changes to the Student Aid Index (SAI).”
### `83e30854fa16b350` Athens Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: https://athenstech.edu/admissions-financial-aid/tuition-financial-aid/ (sha256 541ff822d7d4)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “Not all requests will qualify for Dependency Override.”
  - sentence: dependency_override ⟵ “A Dependency Override request can take up to 5 to 10 business days to process once all required documentation is provided.”
  - sentence: dependency_override ⟵ “If you have an unusual or extenuating circumstance that you believe warrants you independency status, you will need to complete the Dependency Override Appeal form, along with all required supporting documents.”
### `8762b8abd2f05710` Athens Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: http://athenstech.edu/admissions-financial-aid/tuition-financial-aid/ (sha256 fa9c529be90a)
- issues: stale_year_label:2023-24, semantic_review_required, source_not_https
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “I have questions about some specific Financial Aid policies such as the HOPE Cap or appealing a financial aid exclusion.”
### `879800e27405ca44` Athens Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: http://athenstech.edu/admissions-financial-aid/tuition-financial-aid/ (sha256 fa9c529be90a)
- issues: stale_year_label:2023-24, semantic_review_required, source_not_https
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Federal regulations permit the College to override a student’s dependency status for Federal Financial Aid purposes if unusual circumstances exist and can be documented.”
  - sentence: need_based_special_circumstances ⟵ “The following conditions are NOT considered unusual circumstances: Parents refusal to contribute to the student’s education Parents are unwilling to provide information for the FAFSA or verification Parents do not claim the student as a dependent for income tax purposes Student demonstrates total self-sufficiency Student does not communicate with parents.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal Athens Technical College recognizes that changes may be experienced in the financial situation of a household.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeals are made based on a change of income that is beyond your control.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances that warrant an appeal may include the following: Separation or Divorce Loss or reduction of employment (those due to cause or personal choice are not applicable) Death of parent or spouse Child Support Damage Please contact the Financial Aid Department for a Special Circumstance Appeal form to be upload in your Campus Logic portal.”
  - sentence: need_based_special_circumstances ⟵ “All financial documents used for the current year’s FAFSA and the financial documents for the change in income year will be needed.”
### `dd5422a4685898db` Athens Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://athenstech.edu/admissions-financial-aid/tuition-financial-aid/cost-of-attendance/ (sha256 708372c13e39)
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
### `10f5416712393475` Atlanta Metropolitan State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.atlm.edu/downloads/Tuition_Fees/on-campus-2026-2027-tuition-and-fee-schedule.pdf (sha256 a857b9365520)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, conflicting_sources:https://www.atlm.edu/downloads/Tuition_Fees/e-core%202026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/e-major-2026-2027-tuition-and-fee-schedule.pdf,https://www.atlm.edu/downloads/Tuition_Fees/online-2026-2027-tuition-and-fee-schedule.pdf
- checks: {"columns": 20, "rows": 18}
  - column:Hours: 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 110.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Technology Fee: 40.0 ⟵ “Technology Fee | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00”
  - column:Activity Fee: 60.0 ⟵ “Activity Fee | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00”
  - column:Student Center Fee: 240.0 ⟵ “Student Center Fee | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00”
  - column:Total: 450.0 ⟵ “Total | $ 450.00 | $ 560.00 | $ 670.00 | $ 780.00 | $ 890.00 | $ 1,000.00 | $ 1,110.00 | $ 1,220.00 | $ 1,330.00 | $ 1,440.00 | $ 1,550.00 | $ 1,660.00 | $ 1,770.00 | $ 1,880.00 | $ 1,990.00”
  - column:Hours (2): 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition (2): 435.0 ⟵ “Tuition | $ 435.00 | $ 870.00 | $ 1,305.00 | $ 1,740.00 | $ 2,175.00 | $ 2,610.00 | $ 3,045.00 | $ 3,480.00 | $ 3,915.00 | $ 4,350.00 | $ 4,785.00 | $ 5,220.00 | $ 5,655.00 | $ 6,090.00 | $ 6,525.00”
  - column:Technology Fee (2): 40.0 ⟵ “Technology Fee | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00”
  - column:Activity Fee (2): 60.0 ⟵ “Activity Fee | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00”
  - column:Student Center Fee (2): 240.0 ⟵ “Student Center Fee | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00”
  - column:Total (2): 775.0 ⟵ “Total | $ 775.00 | $ 1,210.00 | $ 1,645.00 | $ 2,080.00 | $ 2,515.00 | $ 2,950.00 | $ 3,385.00 | $ 3,820.00 | $ 4,255.00 | $ 4,690.00 | $ 5,125.00 | $ 5,560.00 | $ 5,995.00 | $ 6,430.00 | $ 6,865.00”
  - column:Hours (3): 1 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition (3): 448.0 ⟵ “Tuition | $ 448.00 | $ 896.00 | $ 1,344.00 | $ 1,792.00 | $ 2,240.00 | $ 2,688.00 | $ 3,136.00 | $ 3,584.00 | $ 4,032.00 | $ 4,480.00 | $ 4,928.00 | $ 5,376.00 | $ 5,824.00 | $ 6,272.00 | $ 6,720.00”
  - column:Technology Fee (3): 40.0 ⟵ “Technology Fee | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00”
  - column:Activity Fee (3): 60.0 ⟵ “Activity Fee | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00”
  - column:Student Center Fee (3): 240.0 ⟵ “Student Center Fee | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00”
  - column:Total (3): 788.0 ⟵ “Total | $ 788.00 | $ 1,236.00 | $ 1,684.00 | $ 2,132.00 | $ 2,580.00 | $ 3,028.00 | $ 3,476.00 | $ 3,924.00 | $ 4,372.00 | $ 4,820.00 | $ 5,268.00 | $ 5,716.00 | $ 6,164.00 | $ 6,612.00 | $ 7,060.00”
  - column:Hours: 2 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
  - column:Tuition: 220.0 ⟵ “Tuition | $ 110.00 | $ 220.00 | $ 330.00 | $ 440.00 | $ 550.00 | $ 660.00 | $ 770.00 | $ 880.00 | $ 990.00 | $ 1,100.00 | $ 1,210.00 | $ 1,320.00 | $ 1,430.00 | $ 1,540.00 | $ 1,650.00”
  - column:Technology Fee: 40.0 ⟵ “Technology Fee | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00 | $ | 40.00”
  - column:Activity Fee: 60.0 ⟵ “Activity Fee | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00 | $ | 60.00”
  - column:Student Center Fee: 240.0 ⟵ “Student Center Fee | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00 | $ 240.00”
  - column:Total: 560.0 ⟵ “Total | $ 450.00 | $ 560.00 | $ 670.00 | $ 780.00 | $ 890.00 | $ 1,000.00 | $ 1,110.00 | $ 1,220.00 | $ 1,330.00 | $ 1,440.00 | $ 1,550.00 | $ 1,660.00 | $ 1,770.00 | $ 1,880.00 | $ 1,990.00”
  - column:Hours (2): 2 ⟵ “Hours | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15”
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
### `c5a319165cb22351` Atlanta Metropolitan State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
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
### `e97991271ed9b8fc` Atlanta Metropolitan State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
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
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Paying for College Paying for College HOPE Career Grant How to Apply for Financial Aid Net Price Calculator VA College Financing Plan (Shopping Sheet) Satisfactory Academic Progress (SAP) Payment Options Refund Policy Resources, Documents and Forms Tuition and Fees Types of Aid Apply for Scholarships External Scholarships Professional Judgment Apply Register Request Info Augusta 3200 Augusta Tech ”
### `c9b3865dead27d46` Augusta Technical College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.augustatech.edu/paying-for-college/satisfactory-academic-progress-sap.cms (sha256 e06c5658745f)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Deadlines: Fall 2026 (August 17, 2026 – December 11, 2026) Spring 2027 (January 11, 2027 – May 7, 2027) Summer 2027 (May 17, 2027 – July 29, 2027) *In order to submit an appeal you must be registered for classes* Appeals for Fall 2026 will be accepted July 14, 2026 – August 14, 2026.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form, SAP Academic Plan, and supporting documentation should be uploaded through your Cougar Web account.”
  - sentence: sap_appeal ⟵ “From here you will see a tab for the SAP appeal with a task indicator indicating that there is a task for you to complete.”
### `md05c1e820a9020f` Augusta Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.augustatech.edu/admissions-and-registration/transfer-student-faqs.cms?contentType=textonly (sha256 d409c99fe965)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “A grade of "C" or higher must be earned for courses to be transferred.”
  - min_grade: C- ⟵ “All academic course work in which a student has earned a grade of “C-” or higher is fully transferable if it fits into the student’s degree plan of study.”
  - min_grade: C ⟵ “A grade of "C" or higher must be earned for courses to be transferred.”
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
### `m6ee568b659ff995` Chattahoochee Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [changed] (labeled_in_source)
- source: https://www.chattahoocheetech.edu/dual-enrollment/dual-enrollment-faq.html (sha256 96aa0e849ccd)
- issues: conflicts_with_verified_record
- checks: {"fields": ["college_gpa_to_continue", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 0}
- change dual_enrollment: `{'max_credit_hours_per_term': 15}` → `{'college_gpa_to_continue': 2.0, 'max_credit_hours_per_term': 15, 'per_credit_hour_charges': [{'amount': 107, 'kind': 'tuition', 'line': 'you will have to pay out of pocket to cover tuition, which is $107 per credit hour.'}], 'tuition_per_credit_hour': 107}`
  - max_credit_hours_per_term: 15 ⟵ “their time in Dual Enrollment. Students are permitted to take up to 15 credit hours per semester. *Note: State Legislation is subject to change, which could impact dual enrollment”
  - per_credit_hour_charge: 107 ⟵ “you will have to pay out of pocket to cover tuition, which is $107 per credit hour.”
  - college_gpa_to_continue: 2.0 ⟵ “You must maintain a 2.0 cumulative college GPA in your Chatt Tech courses to stay in good standing. The cumulative GPA includes”
  - max_credit_hours_per_term: 15 ⟵ “Is only permitted to take up to 15 credit hours per semester total (including all”
### `1920923fea4a687a` Clayton  State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clayton.edu/financial-aid/sap (sha256 3602bda8d258)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “SAP Appeals -- Students who lose their financial aid eligibility may appeal based on mitigating circumstances.”
  - sentence: sap_appeal ⟵ “PROBATION Status -- Students who lose financial aid eligibility and have an SAP Appeal approved are placed on financial aid PROBATION.”
  - sentence: sap_appeal ⟵ “Students in this status may continue to receive aid for one semester or for the amount of time designated in the financial aid academic plan outlined in the SAP Appeal Agreement.”
  - sentence: sap_appeal ⟵ “Failure to meet any part of the academic plan outlined in the SAP Appeal Agreement will result in the appeal being rescinded and the immediate loss of financial aid eligibility.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process All Satisfactory Academic Progress appeals must be submitted electronically via Student Forms.”
  - sentence: sap_appeal ⟵ “Meeting this deadline does not guarantee that funds will be available, only that a decision will be made by the fee payment deadline.) PLEASE NOTE: SAP Appeals will be reviewed once monthly after the Final Fee Payment Deadline.”
### `mc1ded113cd2a33a` Clayton  State University — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.clayton.edu/admissions/undergrad/dual-enrollment (sha256 5cd973617f0d)
- issues: stale_year_label:2024-25
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “grades, who have a core high school GPA of 3.0 or higher, to submit ACT or SAT scores”
  - eligibility_tier: 3.0 ⟵ “Summer 2027, students in the 11th and 12th grades with a core high school GPA of 3.0”
  - eligibility_tier: 3.0 ⟵ “grades, who have a core high school GPA of 3.0 or higher, to submit ACT or SAT scores”
  - eligibility_tier: 3.0 ⟵ “Summer 2027, students in the 11th and 12th grades with a core high school GPA of 3.0”
  - eligibility_tier: 3.0 ⟵ “grades, who have a core high school GPA of 3.0 or higher, to submit ACT or SAT scores”
  - eligibility_tier: 3.0 ⟵ “Summer 2027, students in the 11th and 12th grades with a core high school GPA of 3.0”
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
### `9536a1a9d79d61b8` College of Coastal Georgia — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.ccga.edu/policies/regulations (sha256 9e2cdc30d5f4)
- issues: semantic_review_required, conflicting_sources:https://www.ccga.edu/admissions/financialaid/,https://www.ccga.edu/admissions/financialaid/financial-aid-terms/,https://www.ccga.edu/admissions/financialaid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Note that a student cannot appeal the professional judgment of the faculty member and, in all cases, the policy in the course syllabus shall prevail in determining the grade.”
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
- issues: components_do_not_reconcile, implausible_amount, conflicting_sources:https://www.ccga.edu/admissions/waivers/
- checks: {"columns": 15, "components_reconcile": false, "rows": 11}
  - on_campus:Semester Credit Hr.: 1 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - on_campus:Tuition: 110 ⟵ “Tuition | 110 | 220 | 330 | 440 | 550 | 660 | 770 | 880 | 990 | 1100 | 1210 | 1320 | 1430 | 1540 | 1650”
  - on_campus:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - on_campus:Athletic Fee: 97.5 ⟵ “Athletic Fee | 97.5 | 97.5 | 97.5 | 97.5 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195”
  - on_campus:Technology: 60 ⟵ “Technology | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - on_campus:Access Card: 15 ⟵ “Access Card | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15”
  - on_campus:Campus Center: 145 ⟵ “Campus Center | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145”
  - on_campus:Recreational Fee: 25 ⟵ “Recreational Fee | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25”
  - on_campus:Housing*: 3849 ⟵ “Housing* | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849”
  - on_campus:Residential Meal Plan**: 2396 ⟵ “Residential Meal Plan** | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396”
  - on_campus:Total: 6727.5 ⟵ “Total | 6727.5 | 6837.5 | 6947.5 | 7057.5 | 7295 | 7405 | 7515 | 7625 | 7735 | 7845 | 7955 | 8065 | 8175 | 8285 | 8395”
  - on_campus:Semester Credit Hr.: 2 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - on_campus:Tuition: 220 ⟵ “Tuition | 110 | 220 | 330 | 440 | 550 | 660 | 770 | 880 | 990 | 1100 | 1210 | 1320 | 1430 | 1540 | 1650”
  - on_campus:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - on_campus:Athletic Fee: 97.5 ⟵ “Athletic Fee | 97.5 | 97.5 | 97.5 | 97.5 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195”
  - on_campus:Technology: 60 ⟵ “Technology | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - on_campus:Access Card: 15 ⟵ “Access Card | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15”
  - on_campus:Campus Center: 145 ⟵ “Campus Center | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145”
  - on_campus:Recreational Fee: 25 ⟵ “Recreational Fee | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25”
  - on_campus:Housing*: 3849 ⟵ “Housing* | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849”
  - on_campus:Residential Meal Plan**: 2396 ⟵ “Residential Meal Plan** | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396”
  - on_campus:Total: 6837.5 ⟵ “Total | 6727.5 | 6837.5 | 6947.5 | 7057.5 | 7295 | 7405 | 7515 | 7625 | 7735 | 7845 | 7955 | 8065 | 8175 | 8285 | 8395”
  - on_campus:Semester Credit Hr.: 3 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - on_campus:Tuition: 330 ⟵ “Tuition | 110 | 220 | 330 | 440 | 550 | 660 | 770 | 880 | 990 | 1100 | 1210 | 1320 | 1430 | 1540 | 1650”
  - on_campus:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
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
- issues: components_do_not_reconcile, conflicting_sources:https://www.ccga.edu/admissions/waivers/
- checks: {"columns": 15, "components_reconcile": false, "rows": 11}
  - on_campus:Semester Credit Hr.: 1 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - on_campus:Tuition: 435 ⟵ “Tuition | 435 | 870 | 1305 | 1740 | 2175 | 2610 | 3045 | 3480 | 3915 | 4350 | 4785 | 5220 | 5655 | 6090 | 6525”
  - on_campus:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - on_campus:Athletic Fee: 97.5 ⟵ “Athletic Fee | 97.5 | 97.5 | 97.5 | 97.5 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195”
  - on_campus:Technology: 60 ⟵ “Technology | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - on_campus:Access Card: 15 ⟵ “Access Card | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15”
  - on_campus:Campus Center: 145 ⟵ “Campus Center | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145”
  - on_campus:Recreational Fee: 25 ⟵ “Recreational Fee | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25”
  - on_campus:Housing*: 3849 ⟵ “Housing* | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849”
  - on_campus:Residential Meal Plan**: 2396 ⟵ “Residential Meal Plan** | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396”
  - on_campus:Total: 7052.5 ⟵ “Total | 7052.5 | 7487.5 | 7922.5 | 8357.5 | 8920 | 9355 | 9790 | 10225 | 10660 | 11095 | 11530 | 11965 | 12400 | 12835 | 13270”
  - on_campus:Semester Credit Hr.: 2 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - on_campus:Tuition: 870 ⟵ “Tuition | 435 | 870 | 1305 | 1740 | 2175 | 2610 | 3045 | 3480 | 3915 | 4350 | 4785 | 5220 | 5655 | 6090 | 6525”
  - on_campus:Activity Fee: 30 ⟵ “Activity Fee | 30 | 30 | 30 | 30 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - on_campus:Athletic Fee: 97.5 ⟵ “Athletic Fee | 97.5 | 97.5 | 97.5 | 97.5 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195 | 195”
  - on_campus:Technology: 60 ⟵ “Technology | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60”
  - on_campus:Access Card: 15 ⟵ “Access Card | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15”
  - on_campus:Campus Center: 145 ⟵ “Campus Center | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145 | 145”
  - on_campus:Recreational Fee: 25 ⟵ “Recreational Fee | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25”
  - on_campus:Housing*: 3849 ⟵ “Housing* | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849 | 3849”
  - on_campus:Residential Meal Plan**: 2396 ⟵ “Residential Meal Plan** | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396 | 2396”
  - on_campus:Total: 7487.5 ⟵ “Total | 7052.5 | 7487.5 | 7922.5 | 8357.5 | 8920 | 9355 | 9790 | 10225 | 10660 | 11095 | 11530 | 11965 | 12400 | 12835 | 13270”
  - on_campus:***100% eCore Pays $500 online Learning Fee: 2330 ⟵ “***100% eCore Pays $500 online Learning Fee | Residential Plan B-15 meals/week +$125 Dining Dollars | 2330”
  - on_campus:****Coastal Online Major pays $280 Coastal Online Fee: 2200 ⟵ “****Coastal Online Major pays $280 Coastal Online Fee | Residential Plan C-10 meals/week+$125 Dining Dollars | 2200”
  - on_campus:Semester Credit Hr.: 3 ⟵ “Semester Credit Hr. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | +”
  - … 144 more rows
### `e12013ff05555efc` College of Coastal Georgia — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.ccga.edu/policies/cpl (sha256 2dbc92406a70)
- issues: score_cell_not_a_score
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
### `c59194a05b0d0c68` Dalton State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.daltonstate.edu/wp-content/uploads/2024/01/DSCHousingAppeal-renamed.pdf (sha256 48c280287979)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Change in family income: Written narrative form the student explaining how the family’s income situation has changed since the student signed their current Residence Hall Contract.”
### `90955d49ff8b9cde` Dalton State College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.daltonstate.edu/wp-content/uploads/2026/09/Facts-and-Figures-Fall-2025.pdf (sha256 2b7a8744e606)
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "rows": 213}
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
### `6271eee775fda509` Emory University — appeals 2026-27 [new] (labeled_in_source)
- source: https://studentaid.emory.edu/_includes/documents/site-wide/2627_sap_appeal_form.pdf (sha256 20be7f207c2e)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “B: SPECIAL CIRCUMSTANCES FOR CONSIDERATION — Check any boxes that apply to your appeal request REASON FOR APPEAL REQUIRED SUPPORTING DOCUMENTATION □ Verification of health related reasons.”
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
### `ab94d91a03949c94` Emory University — appeals 2026-27 [new] (labeled_in_source)
- source: https://studentaid.emory.edu/_includes/documents/site-wide/2627_sap_appeal_form.pdf (sha256 20be7f207c2e)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If you would like to submit an appeal to the Office of Financial Aid to have your eligibility to aid reinstated, you will need to submit a complete SAP Appeal Packet.”
  - sentence: sap_appeal ⟵ “Please note that SAP appeals will not be considered until a complete SAP Appeal Packet has been submitted (as described above).”
  - sentence: sap_appeal ⟵ “Submitting a SAP appeal does not ensure that your aid will be reinstated, and therefore you should have a back-up plan, if your appeal is denied.”
### `41e4279a955e30e5` Emory University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://studentaid.emory.edu/undergraduate/types/grants-scholarships/tuition-benefit.html (sha256 de4cd2bc1080)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition Benefit: 0 ⟵ “Tuition Benefit | $0”
  - column:Work Study: 2000 ⟵ “Work Study | $2,000”
  - column:Student Loan: 5500 ⟵ “Student Loan | $5,500”
  - column:Need-based Emory University Grant: 35000 ⟵ “Need-based Emory University Grant | $35,000”
  - column:Total Need-based Aid: 42500 ⟵ “Total Need-based Aid | $42,500”
### `522ff1cc9b547f78` Emory University-Oxford College — appeals 2026-27 [new] (labeled_in_source)
- source: https://studentaid.emory.edu/_includes/documents/site-wide/2627_sap_appeal_form.pdf (sha256 20be7f207c2e)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If you would like to submit an appeal to the Office of Financial Aid to have your eligibility to aid reinstated, you will need to submit a complete SAP Appeal Packet.”
  - sentence: sap_appeal ⟵ “Please note that SAP appeals will not be considered until a complete SAP Appeal Packet has been submitted (as described above).”
  - sentence: sap_appeal ⟵ “Submitting a SAP appeal does not ensure that your aid will be reinstated, and therefore you should have a back-up plan, if your appeal is denied.”
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
### `ad631acd5c4a7b67` Emory University-Oxford College — appeals 2026-27 [new] (labeled_in_source)
- source: https://studentaid.emory.edu/_includes/documents/site-wide/2627_sap_appeal_form.pdf (sha256 20be7f207c2e)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “B: SPECIAL CIRCUMSTANCES FOR CONSIDERATION — Check any boxes that apply to your appeal request REASON FOR APPEAL REQUIRED SUPPORTING DOCUMENTATION □ Verification of health related reasons.”
### `2a8326f940a406c5` Emory University-Oxford College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_unur.pdf (sha256 0af6c79a015c)
- issues: components_do_not_reconcile, shared_site_attribution_review, conflicting_sources:https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_uah.pdf,https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/cost-of-attendance-worksheet.pdf,https://studentaid.emory.edu/undergraduate/types/grants-scholarships/tuition-benefit.html
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - column:Tuition Expenses: 70300 ⟵ “Tuition Expenses | $70,300”
  - column:Fees: 2248 ⟵ “Fees | $2,248”
  - column:Housing Expense room, all utilities, cable TV, and one campus computer: 13222 ⟵ “Housing Expense room, all utilities, cable TV, and one campus computer | $13,222”
  - column:Food Expense billed food charges may be different based on the meal plan: 9184 ⟵ “Food Expense billed food charges may be different based on the meal plan | $9,184”
  - column:Personal Expense expenses will vary by student. You incur these charges: 1620 ⟵ “Personal Expense expenses will vary by student. You incur these charges | $1,620”
  - column:Direct Loan Fees percentage of the loan amount and is deducted at the time of: 88 ⟵ “Direct Loan Fees percentage of the loan amount and is deducted at the time of | $88”
  - column:Estimated Total: 100762 ⟵ “Estimated Total | $100,762”
### `42da34857bd46040` Emory University-Oxford College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_uah.pdf (sha256 9137a2d9d186)
- issues: multiple_total_rows, shared_site_attribution_review, conflicting_sources:https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_unur.pdf,https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/cost-of-attendance-worksheet.pdf,https://studentaid.emory.edu/undergraduate/types/grants-scholarships/tuition-benefit.html
- checks: {"columns": 1, "rows": 16}
  - column:Tuition Expenses: 14000 ⟵ “Tuition Expenses | $14,000”
  - column:Fees: 1758 ⟵ “Fees | $1,758”
  - column:Housing Expense room, all utilities, cable TV, and one campus computer: 13222 ⟵ “Housing Expense room, all utilities, cable TV, and one campus computer | $13,222”
  - column:Food Expense billed food charges may be different based on the meal plan: 9184 ⟵ “Food Expense billed food charges may be different based on the meal plan | $9,184”
  - column:Personal Expense: 1620 ⟵ “Personal Expense | $1,620”
  - column:required textbooks and other course materials. Actual expenses: 2790 ⟵ “required textbooks and other course materials. Actual expenses | $2,790”
  - column:Direct Loan Fees percentage of the loan amount and is deducted at the time of: 88 ⟵ “Direct Loan Fees percentage of the loan amount and is deducted at the time of | $88”
  - column:Estimated Total: 43762 ⟵ “Estimated Total | $43,762”
  - column:Tuition Expenses (2): 3666 ⟵ “Tuition Expenses | $3,666”
  - column:One-Time Fees: 360 ⟵ “One-Time Fees | $360”
  - column:Housing Expense room, all utilities, cable TV, and one campus computer (2): 13222 ⟵ “Housing Expense room, all utilities, cable TV, and one campus computer | $13,222”
  - column:Food Expense billed food charges may be different based on the meal plan (2): 9184 ⟵ “Food Expense billed food charges may be different based on the meal plan | $9,184”
  - column:Personal Expense (2): 1620 ⟵ “Personal Expense | $1,620”
  - column:required textbooks and other course materials. Actual expenses (2): 1900 ⟵ “required textbooks and other course materials. Actual expenses | $1,900”
  - column:Direct Loan Fees percentage of the loan amount and is deducted at the time of (2): 88 ⟵ “Direct Loan Fees percentage of the loan amount and is deducted at the time of | $88”
  - column:Estimated Total (2): 31976 ⟵ “Estimated Total | $31,976”
### `a8015a3dbefe6b0d` Emory University-Oxford College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/cost-of-attendance-worksheet.pdf (sha256 9b3df0c4cd32)
- issues: shared_site_attribution_review, conflicting_sources:https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_uah.pdf,https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_unur.pdf,https://studentaid.emory.edu/undergraduate/types/grants-scholarships/tuition-benefit.html
- checks: {"columns": 1, "rows": 8}
  - column:Tuition: 70300 ⟵ “Tuition | $35,150 | $70,300 | Fixed charge for 12 credit hours or more for which you are billed.”
  - column:Fees: 1148 ⟵ “Fees | $574 | $1,148 | which you are billed. Actual billed charge may be different based on”
  - column:Housing: 13222 ⟵ “Housing | $6,611 | $13,222 | utilities, cable TV and one campus computer connection. Actual”
  - column:Food: 9184 ⟵ “Food | $4,592 | $9,184 | Actual billed charge may be different based on meal plan option”
  - column:Travel: 1100 ⟵ “Travel | $550 | $1,100 | student. This is not charged to the student.”
  - column:Personal: 1620 ⟵ “Personal | $810 | $1,620 | grooming and entertainment. This is not charged to the student.”
  - column:Books: 1286 ⟵ “Books | $643 | $1,286 | required books. Will vary by curriculum.”
  - column:Direct Loan Fees: 88 ⟵ “Direct Loan Fees | $44 | $88 | of Direct Loan origination. The fee is calculated as a percentage of the”
### `c4184add15fda057` Emory University-Oxford College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://studentaid.emory.edu/undergraduate/types/grants-scholarships/tuition-benefit.html (sha256 de4cd2bc1080)
- issues: shared_site_attribution_review, conflicting_sources:https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_uah.pdf,https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_unur.pdf,https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/cost-of-attendance-worksheet.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition Benefit: 0 ⟵ “Tuition Benefit | $0”
  - column:Work Study: 2000 ⟵ “Work Study | $2,000”
  - column:Student Loan: 5500 ⟵ “Student Loan | $5,500”
  - column:Need-based Emory University Grant: 35000 ⟵ “Need-based Emory University Grant | $35,000”
  - column:Total Need-based Aid: 42500 ⟵ “Total Need-based Aid | $42,500”
### `3ce219d3bd3e976c` Fort Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fvsu.edu/about-fvsu/satisfactory-academic-progress-sap (sha256 2a9052b7ff69)
- issues: semantic_review_required, conflicting_sources:https://www.fvsu.edu/about-fvsu/office-of-financial-aid
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Students appealing Maximum Allowable Time Frame must complete and submit the SAP Appeal Form and Academic Progress Plan form together.”
  - sentence: sap_appeal ⟵ “Phase 4: SAP Appeal Students who are on SAP suspension have a right to appeal their status, if they believe they had an extenuating circumstance, which stopped them from performing well academically.”
  - sentence: sap_appeal ⟵ “To appeal students, must log into their Verify My FAFSA page and complete the following by the SAP appeal due date: SAP Appeal Request Form, being specific about dates and signatures Watch and upload the Key Components to the FA SAP Appeal Process Upload a current Academic Advisement Progress Assessment Plan signed by both you and your advisor SAP appeals received after the deadline will not be re”
  - sentence: sap_appeal ⟵ “Most SAP appeals are reviewed within two weeks of submission.”
  - sentence: sap_appeal ⟵ “Phase 5: SAP Appeal Decision SAP Appeals Approvals Students who have successfully submitted their SAP appeal and receive an approval, must be sure they meet the each of the requirements listed below: Maintain a semester GPA of a 2.5 Do not withdraw from a course without speaking to the Office of Financial Aid first Complete either a free 8-week course, or successfully attend any required academic ”
  - sentence: sap_appeal ⟵ “SAP Appeal Denials Students who successfully submitted their SAP appeal and receive a denial will not have any federal or state financial assistance added to their account.”
### `a5c2098df6e35b37` Fort Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fvsu.edu/about-fvsu/professional-judgment (sha256 e5cbcb5ee825)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Fort Valley State University’s Department of Financial Aid allows students to request professional judgment if individuals are experiencing extenuating circumstances that may warrant a reevaluation of financial aid.”
### `bfd107e373e9f1b9` Fort Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fvsu.edu/about-fvsu/satisfactory-academic-progress-sap (sha256 2a9052b7ff69)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other special circumstances outside of the student’s control.”
### `f4bc197b509f72ee` Fort Valley State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.fvsu.edu/about-fvsu/office-of-financial-aid (sha256 bb9e527ac261)
- issues: semantic_review_required, conflicting_sources:https://www.fvsu.edu/about-fvsu/satisfactory-academic-progress-sap
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Watch: What responsibilities do I have regarding “Satisfactory Academic Progress?” Watch: Am I eligible to file an appeal?”
  - sentence: sap_appeal ⟵ “Explore more about financial aid appeals and satisfactory academic progress here.”
### `7a2947f05ae08ce0` Fort Valley State University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fvsu.edu/content/userfiles/files/FVSU_2526_Cost%20of%20Attendances.pdf (sha256 a58b50fe7e84)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 54}
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
  - on_campus:Mandatory Fees (2): 1380 ⟵ “Mandatory Fees | $1,380 | $1,380”
  - on_campus:Housing2 (2): 6812 ⟵ “Housing2 | $6,812 | $7,668”
  - on_campus:Food3: 4728 ⟵ “Food3 | $4,728 | $4,100”
  - on_campus:Transportation (2): 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4 (2): 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses (2): 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - on_campus:Loan Fees5: 120 ⟵ “Loan Fees5 | $120 | $120”
  - on_campus:Total Cost of Attendance (2): 38740 ⟵ “Total Cost of Attendance | $38,740 | $40,318”
  - on_campus:Tuition1 (2): 20370 ⟵ “Tuition1 | $20,370 | $20,370”
  - on_campus:Mandatory Fees (3): 1380 ⟵ “Mandatory Fees | $1,380 | $1,380”
  - on_campus:Housing2 (3): 6812 ⟵ “Housing2 | $6,812 | $7,668”
  - on_campus:Food3 (2): 4782 ⟵ “Food3 | $4,782 | $4,100”
  - on_campus:Transportation (3): 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4 (3): 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses (3): 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - … 83 more rows
### `a447d9748317a03a` Fort Valley State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fvsu.edu/content/userfiles/files/2026-2027%20COA.pdf (sha256 7776c2c54a06)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 2, "rows": 48}
  - on_campus:Tuition: 5280.0 ⟵ “Tuition | $5,280.00 | $5,280.00”
  - on_campus:Mandatory Fees: 1400.0 ⟵ “Mandatory Fees | $1,400.00 | $1,400.00”
  - on_campus:Housing: 7074.0 ⟵ “Housing | $7,074.00 | $8,858.00”
  - on_campus:Food: 4916.0 ⟵ “Food | $4,916.00 | $4,474.00”
  - on_campus:Transportation: 2880.0 ⟵ “Transportation | $2,880.00 | $5,760.00”
  - on_campus:Books & Supplies: 1400.0 ⟵ “Books & Supplies | $1,400.00 | $1,400.00”
  - on_campus:Miscellaneous Expenses: 3078.0 ⟵ “Miscellaneous Expenses | $3,078.00 | $3,078.00”
  - on_campus:Total Cost of Attendance: 26028.0 ⟵ “Total Cost of Attendance | $26,028.00 | $30,250.00”
  - on_campus:Tuition (2): 20400.0 ⟵ “Tuition | $20,400.00 | $20,400.00”
  - on_campus:Mandatory Fees (2): 1400.0 ⟵ “Mandatory Fees | $1,400.00 | $1,400.00”
  - on_campus:Housing (2): 7074.0 ⟵ “Housing | $7,074.00 | $8,858.00”
  - on_campus:Food (2): 4916.0 ⟵ “Food | $4,916.00 | $4,474.00”
  - on_campus:Transportation (2): 2880.0 ⟵ “Transportation | $2,880.00 | $5,760.00”
  - on_campus:Books & Supplies (2): 1400.0 ⟵ “Books & Supplies | $1,400.00 | $1,400.00”
  - on_campus:Miscellaneous Expenses (2): 3078.0 ⟵ “Miscellaneous Expenses | $3,078.00 | $3,078.00”
  - on_campus:Total Cost of Attendance (2): 41148.0 ⟵ “Total Cost of Attendance | $41,148.00 | $45,370.00”
  - on_campus:Tuition (3): 20970.0 ⟵ “Tuition | $20,970.00 | $20,970.00”
  - on_campus:Mandatory Fees (3): 1400.0 ⟵ “Mandatory Fees | $1,400.00 | $1,400.00”
  - on_campus:Housing (3): 7074.0 ⟵ “Housing | $7,074.00 | $8,858.00”
  - on_campus:Food (3): 4916.0 ⟵ “Food | $4,916.00 | $4,474.00”
  - on_campus:Transportation (3): 2880.0 ⟵ “Transportation | $2,880.00 | $5,760.00”
  - on_campus:Books & Supplies (3): 1400.0 ⟵ “Books & Supplies | $1,400.00 | $1,400.00”
  - on_campus:Miscellaneous Expenses (3): 3078.0 ⟵ “Miscellaneous Expenses | $3,078.00 | $3,078.00”
  - on_campus:Total Cost of Attendance (3): 41718.0 ⟵ “Total Cost of Attendance | $41,718.00 | $45,940.00”
  - on_campus:Tuition (4): 4872.0 ⟵ “Tuition | $4,872.00 | $4,872.00”
  - … 71 more rows
### `e3ce5f51cb965f9d` Fort Valley State University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fvsu.edu/content/userfiles/files/FVSU_2425_Cost%20of%20Attendances(2).pdf (sha256 cf163cf07d66)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2024-25, conflicting_sources:https://www.fvsu.edu/content/userfiles/files/2024-2025%20Cost%20of%20Attendance.pdf
- checks: {"columns": 2, "rows": 54}
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
  - on_campus:Mandatory Fees (2): 1350 ⟵ “Mandatory Fees | $1,350 | $1,350”
  - on_campus:Housing2 (2): 6528 ⟵ “Housing2 | $6,528 | $7,668”
  - on_campus:Food3: 4582 ⟵ “Food3 | $4,582 | $4,100”
  - on_campus:Transportation (2): 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4 (2): 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses (2): 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - on_campus:Loan Fees5: 120 ⟵ “Loan Fees5 | $120 | $120”
  - on_campus:Total Cost of Attendance (2): 37890 ⟵ “Total Cost of Attendance | $37,890 | $39,898”
  - on_campus:Tuition1 (2): 19770 ⟵ “Tuition1 | $19,770 | $19,770”
  - on_campus:Mandatory Fees (3): 1350 ⟵ “Mandatory Fees | $1,350 | $1,350”
  - on_campus:Housing2 (3): 6528 ⟵ “Housing2 | $6,528 | $768”
  - on_campus:Food3 (2): 4582 ⟵ “Food3 | $4,582 | $4,100”
  - on_campus:Transportation (3): 1350 ⟵ “Transportation | $1,350 | $2,700”
  - on_campus:Books & Supplies4 (3): 1400 ⟵ “Books & Supplies4 | $1,400 | $1,400”
  - on_campus:Miscellaneous Expenses (3): 3150 ⟵ “Miscellaneous Expenses | $3,150 | $3,150”
  - … 83 more rows
### `e5285dd9359dc5c9` Fort Valley State University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fvsu.edu/content/userfiles/files/2024-2025%20Cost%20of%20Attendance.pdf (sha256 008c0406a551)
- issues: residency_unknown, stale_year_label:2024-25, conflicting_sources:https://www.fvsu.edu/content/userfiles/files/FVSU_2425_Cost%20of%20Attendances(2).pdf
- checks: {"columns": 1, "rows": 82}
  - column:Tuition: 5220.0 ⟵ “Tuition | $ 5,220.00”
  - column:Mandatory Fees: 1350.0 ⟵ “Mandatory Fees | $ 1,350.00”
  - column:Books/Course Materials/Supplies/Equipment: 1400.0 ⟵ “Books/Course Materials/Supplies/Equipment | $ 1,400.00”
  - column:Food: 4582.0 ⟵ “Food | $ 4,582.00”
  - column:Housing: 6528.0 ⟵ “Housing | $ 6,528.00”
  - column:Miscellaneous Living Expenses: 3150.0 ⟵ “Miscellaneous Living Expenses | $ 3,150.00”
  - column:Transportation: 1350.0 ⟵ “Transportation | $ 1,350.00”
  - column:Tuition (2): 5220.0 ⟵ “Tuition | $ 5,220.00”
  - column:Mandatory Fees (2): 1350.0 ⟵ “Mandatory Fees | $ 1,350.00”
  - column:Books/Course Materials/Supplies/Equipment (2): 1400.0 ⟵ “Books/Course Materials/Supplies/Equipment | $ 1,400.00”
  - column:Food (2): 4100.0 ⟵ “Food | $ 4,100.00”
  - column:Housing (2): 7668.0 ⟵ “Housing | $ 7,668.00”
  - column:Miscellaneous Living Expenses (2): 3150.0 ⟵ “Miscellaneous Living Expenses | $ 3,150.00”
  - column:Transportation (2): 2700.0 ⟵ “Transportation | $ 2,700.00”
  - column:Tuition (3): 19410.0 ⟵ “Tuition | $ 19,410.00”
  - column:Mandatory Fees (3): 1350.0 ⟵ “Mandatory Fees | $ 1,350.00”
  - column:Books/Course Materials/Supplies/Equipment (3): 1400.0 ⟵ “Books/Course Materials/Supplies/Equipment | $ 1,400.00”
  - column:Food (3): 4582.0 ⟵ “Food | $ 4,582.00”
  - column:Housing (3): 6528.0 ⟵ “Housing | $ 6,528.00”
  - column:Miscellaneous Living Expenses (3): 3150.0 ⟵ “Miscellaneous Living Expenses | $ 3,150.00”
  - column:Transportation (3): 1350.0 ⟵ “Transportation | $ 1,350.00”
  - column:Tuition (4): 19410.0 ⟵ “Tuition | $ 19,410.00”
  - column:Mandatory Fees (4): 1350.0 ⟵ “Mandatory Fees | $ 1,350.00”
  - column:Books/Course Materials/Supplies/Equipment (4): 1400.0 ⟵ “Books/Course Materials/Supplies/Equipment | $ 1,400.00”
  - column:Food (4): 4100.0 ⟵ “Food | $ 4,100.00”
  - … 57 more rows
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
### `0274e9da12176e71` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped
- checks: {"courses": 32, "groups": 11, "groups_skipped": 2}
  - program_name: Bachelor of Science in Biomedical Engineering | Georgia Tech Catalog ⟵ “Bachelor of Science in Biomedical Engineering | Georgia Tech Catalog”
### `0d4fa867f30808a6` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped
- checks: {"courses": 14, "groups": 10, "groups_skipped": 2}
  - program_name: Bachelor of Science in Economics | Georgia Tech Catalog ⟵ “Bachelor of Science in Economics | Georgia Tech Catalog”
### `0d51c55bbc6247e6` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
- checks: {"courses": 186, "groups": 15, "groups_skipped": 2}
  - program_name: Bachelor of Science in Arts, Entertainment, and Creative Technologies | Georgia Tech Catalog ⟵ “Bachelor of Science in Arts, Entertainment, and Creative Technologies | Georgia Tech Catalog”
### `24f51b1a4f15261a` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
- checks: {"courses": 186, "groups": 14, "groups_skipped": 3}
  - program_name: Bachelor of Science in History, Technology, and Society | Georgia Tech Catalog ⟵ “Bachelor of Science in History, Technology, and Society | Georgia Tech Catalog”
### `3d83ad4cea2a516d` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
- checks: {"courses": 109, "groups": 15, "groups_skipped": 2}
  - program_name: Bachelor of Science in Mathematics and Computing | Georgia Tech Catalog ⟵ “Bachelor of Science in Mathematics and Computing | Georgia Tech Catalog”
### `447634e97b7f451c` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
- checks: {"courses": 50, "groups": 14, "groups_skipped": 2}
  - program_name: Bachelor of Science in Environmental Engineering | Georgia Tech Catalog ⟵ “Bachelor of Science in Environmental Engineering | Georgia Tech Catalog”
### `4ebda5f63804c812` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped
- checks: {"courses": 57, "groups": 11, "groups_skipped": 2}
  - program_name: Bachelor of Science in Economics and International Affairs | Georgia Tech Catalog ⟵ “Bachelor of Science in Economics and International Affairs | Georgia Tech Catalog”
### `52942355e9f6a645` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped
- checks: {"courses": 83, "groups": 8, "groups_skipped": 2}
  - program_name: Bachelor of Science in Environmental Science | Georgia Tech Catalog ⟵ “Bachelor of Science in Environmental Science | Georgia Tech Catalog”
### `6a6c26b3ee3e1166` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped
- checks: {"courses": 12, "groups": 10, "groups_skipped": 3}
  - program_name: Bachelor of Science in Global Economics and Modern Languages | Georgia Tech Catalog ⟵ “Bachelor of Science in Global Economics and Modern Languages | Georgia Tech Catalog”
### `7b9ea38824f69a2b` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped
- checks: {"courses": 36, "groups": 10, "groups_skipped": 4}
  - program_name: Bachelor of Science in International Affairs and Modern Languages | Georgia Tech Catalog ⟵ “Bachelor of Science in International Affairs and Modern Languages | Georgia Tech Catalog”
### `811109f828202915` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped
- checks: {"courses": 28, "groups": 9, "groups_skipped": 2}
  - program_name: Bachelor of Science in Astrophysics | Georgia Tech Catalog ⟵ “Bachelor of Science in Astrophysics | Georgia Tech Catalog”
### `96a0909458f76526` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped
- checks: {"courses": 35, "groups": 10, "groups_skipped": 2}
  - program_name: Bachelor of Science in Aerospace Engineering | Georgia Tech Catalog ⟵ “Bachelor of Science in Aerospace Engineering | Georgia Tech Catalog”
### `9d33e6da4a4dc798` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped
- checks: {"courses": 33, "groups": 10, "groups_skipped": 2}
  - program_name: Bachelor of Science in Industrial Design | Georgia Tech Catalog ⟵ “Bachelor of Science in Industrial Design | Georgia Tech Catalog”
### `a79c5790bd83a02d` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped
- checks: {"courses": 31, "groups": 9, "groups_skipped": 2}
  - program_name: Bachelor of Science in Construction Science and Management | Georgia Tech Catalog ⟵ “Bachelor of Science in Construction Science and Management | Georgia Tech Catalog”
### `f2d73fbb0285e752` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped
- checks: {"courses": 49, "groups": 9, "groups_skipped": 2}
  - program_name: Bachelor of Science in Atmospheric and Oceanic Sciences | Georgia Tech Catalog ⟵ “Bachelor of Science in Atmospheric and Oceanic Sciences | Georgia Tech Catalog”
### `f3902cde5b4ff2ef` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped
- checks: {"courses": 29, "groups": 9, "groups_skipped": 2}
  - program_name: Bachelor of Science in Architecture | Georgia Tech Catalog ⟵ “Bachelor of Science in Architecture | Georgia Tech Catalog”
### `fc2179db8fbaf755` Georgia Institute of Technology-Main Campus — academic_programs 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped
- checks: {"courses": 38, "groups": 11, "groups_skipped": 2}
  - program_name: Bachelor of Science in International Affairs | Georgia Tech Catalog ⟵ “Bachelor of Science in International Affairs | Georgia Tech Catalog”
### `019662966484c8d3` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog · requirement_key=bachelor-of-science-in-environmental-science-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `0591523deca03ef4` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-communicating-in-writ [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `076d940a198dbc6f` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-technology-mathematics-and-sciences [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PHYS 2211 ⟵ “PHYS 2211 - Principles of Physics I 2,3”
  - courses: PHYS 2212 ⟵ “PHYS 2212 - Principles of Physics II”
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus 3”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra 3”
### `0823af55fcb6fe26` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `088c58c122974d94` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `09ca8f1bff23e48c` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: EAS 2655 ⟵ “EAS 2655 - Quantitative Techniques in Earth and Atmospheric Sciences”
  - courses: EAS 2750 ⟵ “EAS 2750 - Physics of the Weather”
  - courses: EAS 3603 ⟵ “EAS 3603 - Thermodynamics of Earth Systems”
  - courses: EAS 4740 ⟵ “EAS 4740 - Atmospheric Chemistry Laboratory”
  - courses: EAS 4801 ⟵ “EAS 4801 - Special Topics (Career Development Seminar)”
  - courses: EAS 4420 ⟵ “EAS 4420 - Environmental Field Methods”
  - courses: EAS 4814 ⟵ “EAS 4814 - Special Topics-Lab (Geophysical Field Methods)”
  - courses: EAS 4610 ⟵ “EAS 4610 - Earth System Modeling”
### `0b068bd5da0e4c31` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biochemistry-georgia-tech-catalog · requirement_key=research-option [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biochemistry-bs/ (sha256 074af909ef30)
- issues: course_alternatives_in_rule_text
  - courses: LMC 4701 ⟵ “LMC 4701 - Undergraduate Research Proposal Writing (complete during the first or second semester of research) 2”
  - courses: LMC 4702 ⟵ “LMC 4702 - Undergraduate Research Thesis Writing (take during the term in which students complete their thesis) 3”
### `0bd58d8256c75b57` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `0cbe275a0eee1324` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-arts-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ARCH 1060 ⟵ “ARCH 1060 - Introduction to Design and the Built Environment”
  - courses: ARCH 3010 ⟵ “ARCH 3010 - Design Strategies”
  - courses: ARCH 3007 ⟵ “ARCH 3007 - Art & Architecture in Greece”
  - courses: ARCH 3008 ⟵ “ARCH 3008 - Art & Architecture in Italy I”
  - courses: ARCH 3009 ⟵ “ARCH 3009 - Art & Architecture in Italy II”
  - courses: ARCH 4143 ⟵ “ARCH 4143 - Museums: History, Theory, Design”
  - courses: ARCH 4833 ⟵ “ARCH 4833 - Special Topics: Architectural Technology”
  - courses: FREN 3697 ⟵ “FREN 3697 - Paris in Cinema/Cinema in Paris”
  - courses: FREN 4011 ⟵ “FREN 4011 - French Art”
  - courses: FREN 4160 ⟵ “FREN 4160 - Arts and Power in Paris: Architecture, Urban Art, Visual Arts, Literature, and More”
  - courses: FREN 4242 ⟵ “FREN 4242 - The French New Wave”
  - courses: GRMN 3055 ⟵ “GRMN 3055 - German Fairy Tales: From the Grimm Brothers to Disney”
  - courses: GRMN 3110 ⟵ “GRMN 3110 - Television & Electronic Culture”
  - courses: GRMN 4010 ⟵ “GRMN 4010 - Perspectives of German Media”
  - courses: GRMN 4025 ⟵ “GRMN 4025 - German Culture & Film”
  - courses: GRMN 4026 ⟵ “GRMN 4026 - German Post-Wall Cinema”
  - courses: ID 2241 ⟵ “ID 2241 - History of Art 1”
  - courses: ID 2242 ⟵ “ID 2242 - History of Art 2”
  - courses: ID 4206 ⟵ “ID 4206 - Culture of Objects: A Seminar on the Design and Culture of Objects”
  - courses: JAPN 4165 ⟵ “JAPN 4165 - Critical Readings in Japanese Culture and Arts”
  - courses: JAPN 4173 ⟵ “JAPN 4173 - Japanese Culture and Society through Anime”
  - courses: JAPN 4813 ⟵ “JAPN 4813 - Special Topics (Sociolinguistics through Manga )”
  - courses: KOR 3415 ⟵ “KOR 3415 - Korea in Media: K-Pop, Film, and Drama”
  - courses: KOR 3813 ⟵ “KOR 3813 - Special Topics (East Asian Cinema Masteworks of Genre)”
  - courses: LMC 2400 ⟵ “LMC 2400 - Introduction to Media Studies”
  - … 15 more rows
### `0cbf45b13dcc5492` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-non-ae-required-courses [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped
  - courses: ME 1670 ⟵ “ME 1670 - Introduction to Engineering Graphics and Design”
  - courses: ECE 3710 ⟵ “ECE 3710 - Circuits and Electronics”
  - courses: ECE 3741 ⟵ “ECE 3741 - Instrumentation and Electronics Lab”
### `0cc5db7b58868eb3` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-wellness-requi [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `0d35361ec7418079` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped
  - courses: ARCH 2016 ⟵ “ARCH 2016 - Architecture Design Studio 2 1”
  - courses: ARCH 2017 ⟵ “ARCH 2017 - Architecture Design Studio 3 1”
  - courses: ARCH 2020 ⟵ “ARCH 2020 - Media + Modeling 2”
  - courses: ARCH 2112 ⟵ “ARCH 2112 - History of Architecture II”
  - courses: ARCH 2211 ⟵ “ARCH 2211 - Construction Technology and Design Integration I”
  - courses: ARCH 3016 ⟵ “ARCH 3016 - Architecture Design Studio 4 1”
  - courses: ARCH 3017 ⟵ “ARCH 3017 - Architecture Design Studio 5 1”
  - courses: ARCH 3231 ⟵ “ARCH 3231 - Environmental Systems and Design Integration I”
  - courses: ARCH 4015 ⟵ “ARCH 4015 - Structures 1”
  - courses: ARCH 4016 ⟵ “ARCH 4016 - Architecture Design Studio 6 1,2”
  - courses: ARCH 4017 ⟵ “ARCH 4017 - Architecture Design Studio 7 1,2”
  - courses: ARCH 3010 ⟵ “ARCH 3010 - Design Strategies”
### `0d51956da411a403` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `0d67e462e1f83bc9` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-technology-mathemat [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1711 ⟵ “MATH 1711 - Finite Mathematics”
### `0d70af855605c485` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-departmental-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped
  - section: grade-requirements-departmental-electives ⟵ “Grade Requirements — Departmental Electives”
### `0dc653a341d7d9da` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped
  - courses: PHYS 2210 ⟵ “PHYS 2210 - Introduction to Astrophysics”
  - courses: PHYS 3201 ⟵ “PHYS 3201 - Classical Mechanics I”
  - courses: PHYS 3122 ⟵ “PHYS 3122 - Electrostatics and Magnetostatics”
  - courses: PHYS 3123 ⟵ “PHYS 3123 - Electrodynamics”
  - courses: PHYS 3141 ⟵ “PHYS 3141 - Thermodynamics”
  - courses: PHYS 3143 ⟵ “PHYS 3143 - Quantum Mechanics I”
  - courses: PHYS 4142 ⟵ “PHYS 4142 - Statistical Mechanics”
  - courses: PHYS 4143 ⟵ “PHYS 4143 - Quantum Mechanics II”
  - courses: PHYS 3022 ⟵ “PHYS 3022 - Stars and Planets”
  - courses: PHYS 3210 ⟵ “PHYS 3210 - Astronomy & Astrophysics Lab”
  - courses: PHYS 4147 ⟵ “PHYS 4147 - Relativity”
  - courses: PHYS 4247 ⟵ “PHYS 4247 - Cosmology and Galaxies”
  - courses: PHYS 4347 ⟵ “PHYS 4347 - Theoretical Astrophysics”
### `147cf16a74a579a9` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-technology-mathematics-and-sciences [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1711 ⟵ “MATH 1711 - Finite Mathematics”
### `153b2ccf62f414d1` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-economics-requirement-6 [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CEE 1070 ⟵ “CEE 1070 - Engineering Graphics for Civil and Environmental Engineering”
  - courses: CEE 1090 ⟵ “CEE 1090 - Exploring Civil and Environmental Engineering”
  - courses: CEE 2040 ⟵ “CEE 2040 - Dynamics”
  - courses: CEE 2090 ⟵ “CEE 2090 - Civil and Environmental Engineering Systems”
  - courses: CEE 2300 ⟵ “CEE 2300 - Environmental Engineering Principles”
  - courses: CEE 3040 ⟵ “CEE 3040 - Fluid Mechanics”
  - courses: CEE 3090 ⟵ “CEE 3090 - Data Analytics in Civil and Environmental Engineering”
  - courses: CEE 3340 ⟵ “CEE 3340 - Environmental Engineering Laboratory”
  - courses: CEE 3770 ⟵ “CEE 3770 - Statistics and Applications”
  - courses: CEE 4090 ⟵ “CEE 4090 - Capstone Design”
  - courses: CEE 4200 ⟵ “CEE 4200 - Hydraulic Engineering”
  - courses: COE 3001 ⟵ “COE 3001 - Mechanics of Deformable Bodies”
### `153e66bf25471b49` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-economics-free-electives ⟵ “Bachelor of Science in Economics — Free Electives”
### `16931576e0d1bfe6` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-technology-mathematics-and-sciences [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PHYS 2211 ⟵ “PHYS 2211 - Principles of Physics I 1”
  - courses: PHYS 2212 ⟵ “PHYS 2212 - Principles of Physics II 2”
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
### `1766ae540d56bd55` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `1809fa74acd3fec2` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `1a41dde513c86a62` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-mathematics-and-quantitative-skill [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `1b27a85cd6232a28` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=international-plan-required-courses [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped
  - courses: INTA 1110 ⟵ “INTA 1110 - Introduction to International Relations 1”
  - courses: INTA 3301 ⟵ “INTA 3301 - International Political Economy 2”
  - courses: INTA 3203 ⟵ “INTA 3203 - Comparative Politics”
  - courses: INTA 4500 ⟵ “INTA 4500 - Pro-Seminar in International Affairs 4”
### `1c4af20d2bfa50b2` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-political-scie [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `1cb3ffa8bea3f100` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
### `1f4b8939e294e999` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-mathematics-an [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1712 ⟵ “MATH 1712 - Survey of Calculus”
### `244b3361bc6ad163` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-econ-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-economics-econ-electives ⟵ “Bachelor of Science in Economics — ECON Electives”
### `27aa9b670cd709ff` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: CS 3001 ⟵ “CS 3001 - Computing, Society, and Professionalism”
  - courses: CS 1332 ⟵ “CS 1332 - Data Structures and Algorithms for Applications”
  - courses: MATH 3406 ⟵ “MATH 3406 - A Second Course in Linear Algebra”
  - courses: MATH 4317 ⟵ “MATH 4317 - Analysis I”
### `28b727bc108fd684` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-astrophysics-free-electives ⟵ “Bachelor of Science in Astrophysics — Free Electives”
### `2b0854a61915d8c8` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped
  - courses: ECON 3110 ⟵ “ECON 3110 - Advanced Microeconomic Analysis 2”
  - courses: ECON 3120 ⟵ “ECON 3120 - Advanced Macroeconomic Analysis 2”
  - courses: ECON 3161 ⟵ “ECON 3161 - Econometric Analysis 2”
  - courses: ECON 4010 ⟵ “ECON 4010 - Career Development Workshop”
### `2b4bd468e24261aa` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `2be6b8325f0205e9` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped
  - courses: INTA 1110 ⟵ “INTA 1110 - Introduction to International Relations 2”
  - courses: INTA 2001 ⟵ “INTA 2001 - International Affairs Discovery Practicum”
  - courses: INTA 3110 ⟵ “INTA 3110 - U.S. Foreign Policy 2”
  - courses: INTA 3203 ⟵ “INTA 3203 - Comparative Politics 2”
  - courses: INTA 3301 ⟵ “INTA 3301 - International Political Economy 2”
  - courses: INTA 4500 ⟵ “INTA 4500 - Pro-Seminar in International Affairs 2”
### `2d457e3e71e71f2c` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-mathematics-and-quantitative-skills [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `2d8a73ed0be8ac7f` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-u-s-society-and-culture [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
  - courses: HTS 2001 ⟵ “HTS 2001 - Early American History”
  - courses: HTS 2002 ⟵ “HTS 2002 - The American Revolution and Constitution”
  - courses: HTS 2006 ⟵ “HTS 2006 - History of the South to 1865”
  - courses: HTS 2007 ⟵ “HTS 2007 - History of the Modern South”
  - courses: HTS 2013 ⟵ “HTS 2013 - Modern America: World War II and After”
  - courses: HTS 2015 ⟵ “HTS 2015 - History of Sports in America”
  - courses: HTS 2017 ⟵ “HTS 2017 - Environmental Sociology”
  - courses: HTS 2052 ⟵ “HTS 2052 - North American Borderlands”
  - courses: HTS 2085 ⟵ “HTS 2085 - Reel History I: US History through Hollywood Films”
  - courses: HTS 2086 ⟵ “HTS 2086 - Semester in the City: Engaging Communities”
  - courses: HTS 3002 ⟵ “HTS 3002 - History of American Business”
  - courses: HTS 3005 ⟵ “HTS 3005 - American Environmental History”
  - courses: HTS 3006 ⟵ “HTS 3006 - United States Labor History”
  - courses: HTS 3009 ⟵ “HTS 3009 - The American Civil War”
  - courses: HTS 3011 ⟵ “HTS 3011 - The City in American History”
  - courses: HTS 3012 ⟵ “HTS 3012 - Urban Sociology”
  - courses: HTS 3015 ⟵ “HTS 3015 - History of the Vietnam War”
  - courses: HTS 3016 ⟵ “HTS 3016 - Women and Gender in the United States”
  - courses: HTS 3018 ⟵ “HTS 3018 - New Religions and Cults in America”
  - courses: HTS 3019 ⟵ “HTS 3019 - The Family, Sexuality, and Social Change in America”
  - courses: HTS 3022 ⟵ “HTS 3022 - Gender and Sports”
  - courses: HTS 3023 ⟵ “HTS 3023 - Slaves without Masters: Free People of Color before 1865”
  - courses: HTS 3024 ⟵ “HTS 3024 - African American History to 1865”
  - courses: HTS 3025 ⟵ “HTS 3025 - African American History since 1865”
  - courses: HTS 3026 ⟵ “HTS 3026 - Sociology of Race and Ethnicity”
  - … 5 more rows
### `2db6dc070650c805` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-institutional-priorit [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
### `3146dbe1b20a35f8` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
  - courses: HTS 3102 ⟵ “HTS 3102 - Social Theory and Social Structure”
  - courses: HTS 1081 ⟵ “HTS 1081 - Engineering in History”
  - courses: HTS 2080 ⟵ “HTS 2080 - Introduction to the History of Disease and Medicine”
  - courses: HTS 2081 ⟵ “HTS 2081 - The Scientific Revolution”
  - courses: HTS 2082 ⟵ “HTS 2082 - Technology and Science in the Industrial Age”
  - courses: HTS 2084 ⟵ “HTS 2084 - Technology and Society”
  - courses: HTS 2100 ⟵ “HTS 2100 - Sci, Tech & Modern World”
  - courses: HTS 3007 ⟵ “HTS 3007 - Sociology of Work, Industry, and Occupations”
  - courses: HTS 3020 ⟵ “HTS 3020 - Gender and Technology”
  - courses: HTS 3021 ⟵ “HTS 3021 - Women in Science and Engineering”
  - courses: HTS 3046 ⟵ “HTS 3046 - Science, Politics, and Culture in Nazi Germany”
  - courses: HTS 3080 ⟵ “HTS 3080 - History of Rocketry”
  - courses: HTS 3081 ⟵ “HTS 3081 - Technology and the Environment”
  - courses: HTS 3084 ⟵ “HTS 3084 - Culture and Technology”
  - courses: HTS 3086 ⟵ “HTS 3086 - Sociology of Medicine and Health”
  - courses: HTS 3087 ⟵ “HTS 3087 - History of Medicine”
  - courses: HTS 3088 ⟵ “HTS 3088 - Race, Medicine & Science”
  - courses: HTS 3089 ⟵ “HTS 3089 - Science, Technology and Sports”
  - courses: HTS 4001 ⟵ “HTS 4001 - Seminar in United States History”
  - courses: HTS 4011 ⟵ “HTS 4011 - Seminar in Sociology”
  - courses: HTS 4031 ⟵ “HTS 4031 - Seminar in European History”
  - courses: HTS 4081 ⟵ “HTS 4081 - Seminar in History of Technology”
  - courses: HTS 4086 ⟵ “HTS 4086 - Seminar in Health, Medicine, and Society”
  - courses: HTS 4091 ⟵ “HTS 4091 - Seminar in Global Issues”
### `31bf1ddbb6e33cc3` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-technology-mathematics-and-sciences [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
### `31f57357ca30bc27` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=prerequisites-and-other-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - courses: PHYS 2211 ⟵ “PHYS 2211 - Principles of Physics I”
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
  - courses: MATH 1554 ⟵ “MATH 1554 - Linear Algebra”
  - courses: MATH 2552 ⟵ “MATH 2552 - Differential Equations”
  - courses: CHEM 1310 ⟵ “CHEM 1310 - Principles of General Chemistry for Engineers”
  - courses: COE 2001 ⟵ “COE 2001 - Statics”
### `32a91fb67f37f4f0` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `3301edbb9db5ec83` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-technology-mathematics-and-sciences [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped
  - courses: PHYS 2211 ⟵ “PHYS 2211 - Principles of Physics I 1,2”
  - courses: PHYS 2212 ⟵ “PHYS 2212 - Principles of Physics II 1,3”
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus 1”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra 1,7”
### `3330ed52701780ba` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped
  - courses: ECON 3110 ⟵ “ECON 3110 - Advanced Microeconomic Analysis 3”
  - courses: ECON 3120 ⟵ “ECON 3120 - Advanced Macroeconomic Analysis 3”
  - courses: ECON 3161 ⟵ “ECON 3161 - Econometric Analysis 3”
### `34181a52127ffba0` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-economics-requirement-8 [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: AE 2010 ⟵ “AE 2010 - Thermodynamics & Fluids Fundamentals 1”
  - courses: AE 2220 ⟵ “AE 2220 - Dynamics 1”
  - courses: COE 3001 ⟵ “COE 3001 - Mechanics of Deformable Bodies”
  - courses: AE 2610 ⟵ “AE 2610 - Introduction to Experimental Methods in Aerospace”
  - courses: AE 2611 ⟵ “AE 2611 - Technical Communications for Aerospace Engineers 1”
  - courses: AE 3330 ⟵ “AE 3330 - Introduction to Aerospace Vehicle Performance”
  - courses: AE 3030 ⟵ “AE 3030 - Aerodynamics”
  - courses: AE 3140 ⟵ “AE 3140 - Structural Analysis”
  - courses: AE 3530 ⟵ “AE 3530 - System Dynamics and Vibration”
  - courses: AE 3531 ⟵ “AE 3531 - Control System Analysis and Design”
  - courses: AE 3610 ⟵ “AE 3610 - Experiments in Fluid and Solid Mechanics”
  - courses: AE 4311 ⟵ “AE 4311 - Aircraft Design I: Conceptual Design”
  - courses: AE 4312 ⟵ “AE 4312 - Aircraft Design II: Preliminary Design”
  - courses: AE 4531 ⟵ “AE 4531 - Aircraft Flight Dynamics”
  - courses: AE 4451 ⟵ “AE 4451 - Jet and Rocket Propulsion”
  - courses: AE 4610 ⟵ “AE 4610 - Dynamics and Control Laboratory”
### `359ff85d1fad9544` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-economics-and-international-affairs-free-electives ⟵ “Bachelor of Science in Economics and International Affairs — Free Electives”
### `36c2cf62eb8b3894` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HTS 2101 ⟵ “HTS 2101 - Historical and Social Research 2”
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877 1,2”
  - courses: SOC 1101 ⟵ “SOC 1101 - Introduction to Sociology 2”
  - courses: HTS 1031 ⟵ “HTS 1031 - Europe Since the Renaissance”
  - courses: HTS 2036 ⟵ “HTS 2036 - Revolutionary Europe: 1789-1914”
  - courses: HTS 2037 ⟵ “HTS 2037 - Twentieth Century Europe: 1914 to Present”
  - courses: HTS 2040 ⟵ “HTS 2040 - History of Islamic Societies”
  - courses: HTS 2041 ⟵ “HTS 2041 - History of the Modern Middle East”
  - courses: HTS 2053 ⟵ “HTS 2053 - Modern Latin American History”
  - courses: HTS 2061 ⟵ “HTS 2061 - Traditional Asia and Its Legacy”
  - courses: HTS 2062 ⟵ “HTS 2062 - Asia in the Modern World”
  - courses: HTS 3028 ⟵ “HTS 3028 - Ancient Greece: Gods, Heroes, and RuinS”
  - courses: HTS 3029 ⟵ “HTS 3029 - Ancient Rome: From Greatness to Ruins”
  - courses: HTS 3030 ⟵ “HTS 3030 - Medieval Europe: 350 to 1400”
  - courses: HTS 3031 ⟵ “HTS 3031 - European Labor History”
  - courses: HTS 3032 ⟵ “HTS 3032 - Modern European Intellectual History”
  - courses: HTS 3033 ⟵ “HTS 3033 - Medieval England”
  - courses: HTS 3035 ⟵ “HTS 3035 - Britain from 1815-1914”
  - courses: HTS 3036 ⟵ “HTS 3036 - Britain Since 1914”
  - courses: HTS 3038 ⟵ “HTS 3038 - The French Revolution”
  - courses: HTS 3039 ⟵ “HTS 3039 - Modern France”
  - courses: HTS 3041 ⟵ “HTS 3041 - Modern Spain”
  - courses: HTS 3046 ⟵ “HTS 3046 - Science, Politics, and Culture in Nazi Germany”
  - courses: HTS 3048 ⟵ “HTS 3048 - Modern Russian History and Society”
  - courses: HTS 3051 ⟵ “HTS 3051 - Women and the Politics of Gender in the Middle East”
  - … 5 more rows
### `39c886c933549aa7` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
### `3bae6bb97f10094b` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-mathematics-and-quantitative-skills [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1712 ⟵ “MATH 1712 - Survey of Calculus”
### `3c83073f1f77f481` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `3de0e6e9e398b973` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `3e4993de9bacf44c` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `3e914e67a9f03d66` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped
  - courses: ECON 2105 ⟵ “ECON 2105 - Principles of Macroeconomics 3”
  - courses: ECON 2106 ⟵ “ECON 2106 - Principles of Microeconomics 3”
### `41ae527ad3a9a1ab` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-field-of-stu [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: AECT 1000 ⟵ “AECT 1000 - The Science and Practice of Creativity”
  - courses: AECT 1500 ⟵ “AECT 1500 - Creative Coding and Emerging Technologies”
  - courses: AECT 2030 ⟵ “AECT 2030 - Leaders in Progress and Service for the Creative Industries”
  - courses: ECE 2806 ⟵ “ECE 2806 - Special Topics (AI First)”
  - courses: ECE 2026 ⟵ “ECE 2026 - Introduction to Signal Processing”
  - courses: AECT 2000 ⟵ “AECT 2000 - Storytelling Studio”
### `420b563e21371f34` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=international-plan [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped
  - courses: INTA 1110 ⟵ “INTA 1110 - Introduction to International Relations 1”
  - courses: INTA 3301 ⟵ “INTA 3301 - International Political Economy 2”
  - courses: INTA 3203 ⟵ “INTA 3203 - Comparative Politics”
  - courses: INTA 4500 ⟵ “INTA 4500 - Pro-Seminar in International Affairs”
  - courses: ML 4500 ⟵ “ML 4500 - Intercultural Seminar”
### `42af28c85e27a710` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-field-of-study-2 [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped
  - courses: ECON 2100 ⟵ “ECON 2100 - Economic Analysis and Policy Problems 1”
  - courses: BC 2610 ⟵ “BC 2610 - Construction Technology I”
  - courses: BC 2620 ⟵ “BC 2620 - Construction Technology II”
  - courses: BC 2631 ⟵ “BC 2631 - Introduction to Construction Management”
  - courses: BC 2632 ⟵ “BC 2632 - Construction Materials and Methods”
  - courses: BC 2634 ⟵ “BC 2634 - Construction Plans and Estimates”
### `4515ed7da939019b` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-arts-practic [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
  - courses: ARCH 1020 ⟵ “ARCH 1020 - Media + Modeling 1”
  - courses: CS 4455 ⟵ “CS 4455 - Video Game Design and Programming”
  - courses: CS 4731 ⟵ “CS 4731 - Game AI”
  - courses: CS 4496 ⟵ “CS 4496 - Computer Animation”
  - courses: ID 2101 ⟵ “ID 2101 - Digital Design Methods”
  - courses: ID 2102 ⟵ “ID 2102 - 3D Modeling”
  - courses: ID 3510 ⟵ “ID 3510 - Introduction to Interactive Product Design”
  - courses: ID 4062 ⟵ “ID 4062 - ID Capstone Design Studio 2”
  - courses: LMC 3402 ⟵ “LMC 3402 - Graphic and Visual Design”
  - courses: LMC 3406 ⟵ “LMC 3406 - Video Production”
  - courses: LMC 3407 ⟵ “LMC 3407 - Advanced Video Production”
  - courses: LMC 3454 ⟵ “LMC 3454 - Producing Black Documentary Film and Podcasts”
  - courses: LMC 4407 ⟵ “LMC 4407 - Video Editing and Postproduction”
  - courses: LMC 4710 ⟵ “LMC 4710 - Game Studio”
  - courses: LMC 4733 ⟵ “LMC 4733 - Mixed Reality Experience Design”
  - courses: LMC 4720 ⟵ “LMC 4720 - Interactive Narrative”
  - courses: MUSI 2015 ⟵ “MUSI 2015 - Laptop Orchestra”
  - courses: MUSI 3541 ⟵ “MUSI 3541 - Electronic Percussion Ensemble”
  - courses: MUSI 3770 ⟵ “MUSI 3770 - Project Studio: Technology”
  - courses: MUSI 4450 ⟵ “MUSI 4450 - Integrating Music Into Multimedia”
  - courses: MUSI 4458 ⟵ “MUSI 4458 - Computer Music Composition”
  - courses: MUSI 4670 ⟵ “MUSI 4670 - Music Interface Design”
  - courses: ARCH 4413 ⟵ “ARCH 4413 - Collage Making”
  - courses: ARCH 4833 ⟵ “ARCH 4833 - Special Topics: Architectural Technology”
  - courses: ID 1418 ⟵ “ID 1418 - Introduction to Sketching and Modeling 1”
  - … 15 more rows
### `45ed840ccefb92b8` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-mathematics-and-quant [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `46210469834ae24e` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-free-electiv [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-arts-entertainment-and-creative-technologies-free-electiv ⟵ “Bachelor of Science in Arts, Entertainment, and Creative Technologies — Free Electives”
### `47b60bce9d1e2332` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `49227d8b2063e32e` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `49c53aa15c335bc5` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 2551 ⟵ “MATH 2551 - Multivariable Calculus”
  - courses: MATH 2552 ⟵ “MATH 2552 - Differential Equations”
  - courses: CHEM 1310 ⟵ “CHEM 1310 - Principles of General Chemistry for Engineers”
  - courses: PHYS 2304 ⟵ “PHYS 2304 - Modern Physics”
  - courses: PHYS 2303 ⟵ “PHYS 2303 - Vibrations and Waves”
### `4bbce305d580fa22` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog · requirement_key=bachelor-of-science-in-environmental-science-mathematics-and-quantitative-skills [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `4f7e59bf2890a44c` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-technology-mathematics-and-science [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PHYS 2211 ⟵ “PHYS 2211 - Principles of Physics I”
  - courses: PHYS 2212 ⟵ “PHYS 2212 - Principles of Physics II”
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
### `4f7e75a2159384ed` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped
  - courses: MATH 2551 ⟵ “MATH 2551 - Multivariable Calculus 1”
  - courses: MATH 2552 ⟵ “MATH 2552 - Differential Equations 1”
  - courses: MSE 2001 ⟵ “MSE 2001 - Principles and Applications of Engineering Materials”
  - courses: CHEM 1310 ⟵ “CHEM 1310 - Principles of General Chemistry for Engineers”
  - courses: AE 1601 ⟵ “AE 1601 - Introduction to Aerospace Engineering 1”
  - courses: COE 2001 ⟵ “COE 2001 - Statics 1”
### `4f8d02fd880ec80a` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BMED 2250 ⟵ “BMED 2250 - Problems in Biomedical Engineering”
  - courses: BMED 2310 ⟵ “BMED 2310 - Intro to Biomedical Engineering Design”
  - courses: BMED 3100 ⟵ “BMED 3100 - Systems Physiology”
  - courses: BMED 3110 ⟵ “BMED 3110 - Quantitative Engineering Physiology Laboratory I”
  - courses: BMED 3310 ⟵ “BMED 3310 - Biotransport”
  - courses: BMED 3410 ⟵ “BMED 3410 - Introduction to Biomechanics”
  - courses: BMED 3520 ⟵ “BMED 3520 - Biomedical Systems and Modeling”
  - courses: BMED 3600 ⟵ “BMED 3600 - Physiology of Cellular and Molecular Systems”
  - courses: BMED 3610 ⟵ “BMED 3610 - Quantitative Engineering Physiology Laboratory II”
  - courses: BMED 4000 ⟵ “BMED 4000 - The Art of Telling Your Story”
  - courses: BMED 4602 ⟵ “BMED 4602 - Capstone Design”
### `50b6f11a2c5c11e6` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
### `50d220c38c7bdd24` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-georgia-tech-catalog · requirement_key=research-option [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-bs/ (sha256 33dbaa68d4a1)
- issues: course_alternatives_in_rule_text
  - courses: LMC 4701 ⟵ “LMC 4701 - Undergraduate Research Proposal Writing (complete during the first or second semester of research) 3”
  - courses: LMC 4702 ⟵ “LMC 4702 - Undergraduate Research Thesis Writing (take during the thesis-writing semester) 4”
### `514393bd03c321fa` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-political-sc [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `521c0961712fd110` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `5329873f6a10072b` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ID 1419 ⟵ “ID 1419 - Introduction to Sketching and Modeling 2”
  - courses: ID 2101 ⟵ “ID 2101 - Digital Design Methods”
  - courses: ID 2102 ⟵ “ID 2102 - 3D Modeling”
  - courses: ID 2202 ⟵ “ID 2202 - History of Modern Industrial Design”
  - courses: ID 2320 ⟵ “ID 2320 - Human Factors in Design”
  - courses: ID 2325 ⟵ “ID 2325 - User Centered Design Methods”
  - courses: ID 2510 ⟵ “ID 2510 - Introduction to Smart Product Design”
  - courses: ID 3031 ⟵ “ID 3031 - Health Design Studio 1”
  - courses: ID 3032 ⟵ “ID 3032 - Health Design Studio 2”
  - courses: ID 3301 ⟵ “ID 3301 - Materials I: Renewables”
  - courses: ID 3302 ⟵ “ID 3302 - Materials and Processes II: Nonrenewables”
  - courses: ID 4061 ⟵ “ID 4061 - ID Capstone Design Studio 1”
  - courses: ID 4062 ⟵ “ID 4062 - ID Capstone Design Studio 2”
  - courses: ID 3320 ⟵ “ID 3320 - Design Methods: User Centered Design”
  - courses: ID 4206 ⟵ “ID 4206 - Culture of Objects: A Seminar on the Design and Culture of Objects”
### `558f87e19882b029` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog · requirement_key=bachelor-of-science-in-environmental-science-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIOS 1107L ⟵ “BIOS 1107L - Biological Principles Laboratory”
  - courses: BIOS 2301 ⟵ “BIOS 2301 - Ecology Laboratory”
  - courses: EAS 4480 ⟵ “EAS 4480 - Environmental Data Analysis”
  - courses: PUBP 4530 ⟵ “PUBP 4530 - Introduction to Geographic Information Systems”
  - courses: PUBP 3315 ⟵ “PUBP 3315 - Environmental Policy and Politics”
  - courses: EAS 4410 ⟵ “EAS 4410 - Climate and Global Change”
  - courses: EAS 4420 ⟵ “EAS 4420 - Environmental Field Methods”
  - courses: BIOS 3380 ⟵ “BIOS 3380 - Microbiology”
  - courses: BIOS 3600 ⟵ “BIOS 3600 - Evolutionary Biology”
  - courses: BIOS 4221 ⟵ “BIOS 4221 - Biological Oceanography”
  - courses: BIOS 4340 ⟵ “BIOS 4340 - Medical Microbiology”
  - courses: BIOS 4401 ⟵ “BIOS 4401 - Experimental Design and Statistical Methods in Biological Sciences”
  - courses: BIOS 4417 ⟵ “BIOS 4417 - Marine Ecology”
  - courses: BIOS 4418 ⟵ “BIOS 4418 - Microbial Physiology”
  - courses: BIOS 4428 ⟵ “BIOS 4428 - Population Dynamics”
  - courses: BIOS 4515 ⟵ “BIOS 4515 - Community Ecology”
  - courses: BIOS 4607 ⟵ “BIOS 4607 - Molecular Biology of Microbes: Disease, Nature, and Biotechnology”
  - courses: BIOS 4620 ⟵ “BIOS 4620 - Aquatic Chemical Ecology”
  - courses: BIOS 4651 ⟵ “BIOS 4651 - Bioethics”
  - courses: BIOS 4690 ⟵ “BIOS 4690 - Independent Research Project”
  - courses: BIOS 4699 ⟵ “BIOS 4699 - Undergraduate Research”
  - courses: BIOS 4803 ⟵ “BIOS 4803 - Special Topics (Conservation Biology)”
  - courses: BIOS 4803 ⟵ “BIOS 4803 - Special Topics (Biology of Terrestrial Vertebrates)”
  - courses: BIOS 4803 ⟵ “BIOS 4803 - Special Topics (Ornithology)”
  - courses: BIOS 4813 ⟵ “BIOS 4813 - Special Topics (Biodiversity on a Changing Planet)”
  - … 15 more rows
### `55e5003b986337b2` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-additional-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - courses: CHEM 1315 ⟵ “CHEM 1315 - Survey of Organic Chemistry for Engineers”
  - courses: EAS 2600 ⟵ “EAS 2600 - Earth Processes”
  - courses: CHBE 2130 ⟵ “CHBE 2130 - Chemical Engineering Thermodynamics I”
  - courses: CHEM 3411 ⟵ “CHEM 3411 - Physical Chemistry I”
  - courses: EAS 3603 ⟵ “EAS 3603 - Thermodynamics of Earth Systems”
  - courses: ME 3322 ⟵ “ME 3322 - Thermodynamics”
### `56b8c2ac5d4ed9c1` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-mathematics-and-quant [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1712 ⟵ “MATH 1712 - Survey of Calculus”
### `582ea3ab16a8269b` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-technology-m [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
### `5a79836834304349` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `5c0751eac556d659` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-arts-tech-et [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
  - courses: MGT 4803 ⟵ “MGT 4803 - Special Topics in Management (Sports and Entertainment Law)”
  - courses: MGT 2106 ⟵ “MGT 2106 - Legal, Social, Ethical Aspects of Business”
  - courses: PHIL 3101 ⟵ “PHIL 3101 - AI Ethics and Policy”
### `5c87e62c01b3ccf4` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `5d3801ade8a2de05` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `6179ed48b533eba7` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-institutiona [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
### `61fdd3d99c4d34e8` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-mathematics-and-quantitative-skills [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus 3”
### `65c4f7ebfb54009f` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `6867df6559ee8915` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-communicating-in-writ [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `6a9fa6ca7535f45b` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-chemistry-georgia-tech-catalog · requirement_key=research-option [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/chemistry-bs/ (sha256 6812a6769db0)
- issues: course_alternatives_in_rule_text
  - courses: LMC 4701 ⟵ “LMC 4701 - Undergraduate Research Proposal Writing (complete during the first or second semester of research) 2”
  - courses: LMC 4702 ⟵ “LMC 4702 - Undergraduate Research Thesis Writing (take during the term in which students complete their thesis) 3”
### `6af07f389717d36d` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-bmed-depth-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-biomedical-engineering-bmed-depth-electives ⟵ “Bachelor of Science in Biomedical Engineering — BMED Depth Electives”
### `6af9aba487960cd8` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
### `6b4fb2aa34cbd2ca` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-mathematics-and-quantitative-skills [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `6cc7e1079c88a88c` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `6cd2f42d43bb7223` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-political-science-and-u-s-histo [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `70ca33b05f8460c5` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-other-engineering-and-science-requ [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CHEM 1315 ⟵ “CHEM 1315 - Survey of Organic Chemistry for Engineers”
  - courses: BMED 2400 ⟵ “BMED 2400 - Introduction to Bioengineering Statistics”
  - courses: MSE 2001 ⟵ “MSE 2001 - Principles and Applications of Engineering Materials”
  - courses: ECE 3710 ⟵ “ECE 3710 - Circuits and Electronics”
  - courses: ECE 3741 ⟵ “ECE 3741 - Instrumentation and Electronics Lab”
### `720f9fb0161ff37e` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-history-technology-and-society-free-electives ⟵ “Bachelor of Science in History, Technology, and Society — Free Electives”
### `7514692311e9f489` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-approved-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - section: program-educational-objectives-approved-electives ⟵ “Program Educational Objectives — Approved Electives”
### `7835b27d6f897384` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog · requirement_key=bachelor-of-science-in-environmental-science-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: INTA 1200 ⟵ “INTA 1200 - American Government in Comparative Perspective”
### `79bcf4059fda2c5e` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-mathematics-and-quantitative-skills [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1712 ⟵ “MATH 1712 - Survey of Calculus”
### `7a609f4d0f707db7` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-international-affairs-free-electives ⟵ “Bachelor of Science in International Affairs — Free Electives”
### `7acf0ea13cbecdb7` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-international-affairs-and-modern-languages-free-electives ⟵ “Bachelor of Science in International Affairs and Modern Languages — Free Electives”
### `7b2f049e1314311e` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-wellness-req [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `7b97e01a89c89266` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-mathematics-and-quantitative-skills [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `7c5a902473e9bce9` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-technology-mathematics-and-sciences [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1711 ⟵ “MATH 1711 - Finite Mathematics”
### `7d0e2ce95f69af78` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `7ea13679b6eb828a` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-communicating-in-wr [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `7ed79986f3668689` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `7fa4a9c2b59efe94` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped
  - courses: BMED 1000 ⟵ “BMED 1000 - Introduction to Biomedical Engineering”
  - courses: BMED 2110 ⟵ “BMED 2110 - Conservation Principles in Biomedical Engineering”
  - courses: COE 2001 ⟵ “COE 2001 - Statics”
  - courses: MATH 2551 ⟵ “MATH 2551 - Multivariable Calculus”
  - courses: MATH 2552 ⟵ “MATH 2552 - Differential Equations”
  - courses: CHEM 1211K ⟵ “CHEM 1211K - Chemical Principles I”
### `7fd9329a19a37498` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-mathematics-and-qua [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1712 ⟵ “MATH 1712 - Survey of Calculus”
### `8186284b1a5dcd26` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `830234a14186d8b4` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-mathematics-and-quantitati [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1712 ⟵ “MATH 1712 - Survey of Calculus”
### `88794f85a08d6b7a` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-technology-mathematics-and-scie [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1554 ⟵ “MATH 1554 - Linear Algebra”
### `8ae376e308e4adbe` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-technical-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped
  - courses: BMED 2400 ⟵ “BMED 2400 - Introduction to Bioengineering Statistics”
  - courses: CP 4510 ⟵ “CP 4510 - Fundamentals of Geographic Information Systems”
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
  - courses: CS 2316 ⟵ “CS 2316 - Data Manipulation for Science and Industry”
  - courses: CS 1331 ⟵ “CS 1331 - Introduction to Object Oriented Programming”
  - courses: EAS 3110 ⟵ “EAS 3110 - Energy, Environment, and Society”
  - courses: EAS 4480 ⟵ “EAS 4480 - Environmental Data Analysis”
  - courses: ID 3103 ⟵ “ID 3103 - Industrial Design Computing I”
  - courses: ME 2016 ⟵ “ME 2016 - Computer Applications”
  - courses: MGT 2210 ⟵ “MGT 2210 - Information Systems and Digital Transformation”
  - courses: MGT 4052 ⟵ “MGT 4052 - Systems Analysis and Design”
### `8ba2982347e3fdd4` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog · requirement_key=bachelor-of-science-in-environmental-science-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CHEM 1212K ⟵ “CHEM 1212K - Chemical Principles II”
  - courses: EAS 1600 ⟵ “EAS 1600 - Introduction to Environmental Science”
  - courses: EAS 2600 ⟵ “EAS 2600 - Earth Processes”
  - courses: BIOS 1207 ⟵ “BIOS 1207 - Biological Principles for Majors”
  - courses: BIOS 1107 ⟵ “BIOS 1107 - Principles of Biology I”
  - courses: BIOS 2300 ⟵ “BIOS 2300 - Ecology”
  - courses: BIOS 2310 ⟵ “BIOS 2310 - Problems in Ecology”
### `8c1b9ea43f2453f0` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
### `8dfd5adfe81163fe` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-construction-science-and-management-free-electives ⟵ “Bachelor of Science in Construction Science and Management — Free Electives”
### `8f067f3f19972ec9` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `8f8fcc1d43e54e4d` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-technology-mathematics-and [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1711 ⟵ “MATH 1711 - Finite Mathematics 6”
### `906d3d42d8c7f33d` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-physics-georgia-tech-catalog · requirement_key=research-option-in-physics [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/physics-bs/ (sha256 f046807c2452)
- issues: course_alternatives_in_rule_text
  - courses: PHYS 4698 ⟵ “PHYS 4698 - Undergraduate Research Assistantship 1”
  - courses: LMC 4701 ⟵ “LMC 4701 - Undergraduate Research Proposal Writing 2”
  - courses: LMC 4702 ⟵ “LMC 4702 - Undergraduate Research Thesis Writing 3”
### `93a18dcf5dcf6994` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `957e3ffbc0b64285` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-design-elective [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - courses: CEE 4310 ⟵ “CEE 4310 - Water Quality Engineering”
  - courses: CEE 4320 ⟵ “CEE 4320 - Hazardous Substance Remediation”
  - courses: CEE 4330 ⟵ “CEE 4330 - Air Pollution Engineering”
  - courses: CEE 4340 ⟵ “CEE 4340 - Environmental Modeling and Health Risk Analysis”
  - courses: CEE 4370 ⟵ “CEE 4370 - Industrial Wastewater Process Engineering and Design”
  - courses: CEE 4395 ⟵ “CEE 4395 - Environmental Systems Design Project”
### `95db56d86b34f434` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-technology-mathematic [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1711 ⟵ “MATH 1711 - Finite Mathematics”
### `9680d9f2ab17cb2f` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-modeling-simulation-data-and-ap [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: MATH 4347 ⟵ “MATH 4347 - Partial Differential Equations I”
  - courses: CX 4220 ⟵ “CX 4220 - Introduction to High Performance Computing”
  - courses: CX 4230 ⟵ “CX 4230 - Computer Simulation”
  - courses: CS 4641 ⟵ “CS 4641 - Machine Learning”
  - courses: CX 4240 ⟵ “CX 4240 - Introduction to Computing for Data Analysis”
  - courses: MATH 4210 ⟵ “MATH 4210 - Mathematical Foundations of Data Science”
  - courses: MATH 3012 ⟵ “MATH 3012 - Applied Combinatorics”
  - courses: MATH 4022 ⟵ “MATH 4022 - Introduction to Graph Theory”
  - courses: MATH 4221 ⟵ “MATH 4221 - Stochastic Processes I”
  - courses: MATH 4222 ⟵ “MATH 4222 - Stochastic Processes II”
  - courses: MATH 4280 ⟵ “MATH 4280 - Introduction to Information Theory”
  - courses: MATH 4318 ⟵ “MATH 4318 - Analysis II”
  - courses: MATH 4320 ⟵ “MATH 4320 - Complex Analysis”
  - courses: MATH 4441 ⟵ “MATH 4441 - Differential Geometry”
  - courses: MATH 4541 ⟵ “MATH 4541 - Dynamics and Bifurcations I”
  - courses: MATH 4580 ⟵ “MATH 4580 - Linear Programming”
  - courses: MATH 4755 ⟵ “MATH 4755 - Mathematical Biology”
  - courses: MATH 4782 ⟵ “MATH 4782 - Quantum Information and Quantum Computing”
  - courses: MATH 4803 ⟵ “MATH 4803 - Special Topics (Advanced Statistical Theory for Machine Learning )”
  - courses: MATH 4803 ⟵ “MATH 4803 - Special Topics (Introduction to Stochastic Calculus )”
  - courses: CS 4644 ⟵ “CS 4644 - Deep Learning”
  - courses: CX 4140 ⟵ “CX 4140 - Computational Modeling Algorithms”
  - courses: CX 4232 ⟵ “CX 4232 - Simulation and Military Gaming”
  - courses: CX 4242 ⟵ “CX 4242 - Data and Visual Analytics”
### `972da83a5c387612` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog · requirement_key=bachelor-of-science-in-environmental-science-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `98984c476a2ef594` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped
  - courses: ARCH 1016 ⟵ “ARCH 1016 - Foundation Studio 1 1”
  - courses: ARCH 1017 ⟵ “ARCH 1017 - Architecture Design Studio 1 1”
  - courses: ARCH 1020 ⟵ “ARCH 1020 - Media + Modeling 1”
  - courses: ARCH 1060 ⟵ “ARCH 1060 - Introduction to Design and the Built Environment”
  - courses: ARCH 2111 ⟵ “ARCH 2111 - History of Architecture I”
### `9997b4388c1eefac` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped
  - courses: ECON 2105 ⟵ “ECON 2105 - Principles of Macroeconomics 2”
  - courses: ECON 2106 ⟵ “ECON 2106 - Principles of Microeconomics 2”
### `9dac74b05c70a455` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-political-science-and-u-s- [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `9e34b20a80a8d7c6` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
### `a0991920aaf61e43` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-technology-mathematics-a [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
### `a1841b5f28bd2667` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped
  - courses: PHYS 2212 ⟵ “PHYS 2212 - Principles of Physics II”
  - courses: MATH 2551 ⟵ “MATH 2551 - Multivariable Calculus”
  - courses: MATH 2552 ⟵ “MATH 2552 - Differential Equations”
  - courses: EAS 1600 ⟵ “EAS 1600 - Introduction to Environmental Science”
  - courses: EAS 2551 ⟵ “EAS 2551 - Introduction to Meteorological Analysis”
### `a236c85648bb537c` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-communities-environment-an [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
  - courses: HTS 2016 ⟵ “HTS 2016 - Social Issues and Public Policy”
  - courses: HTS 2017 ⟵ “HTS 2017 - Environmental Sociology”
  - courses: HTS 2018 ⟵ “HTS 2018 - Food and Society”
  - courses: HTS 2053 ⟵ “HTS 2053 - Modern Latin American History”
  - courses: HTS 2086 ⟵ “HTS 2086 - Semester in the City: Engaging Communities”
  - courses: HTS 3005 ⟵ “HTS 3005 - American Environmental History”
  - courses: HTS 3007 ⟵ “HTS 3007 - Sociology of Work, Industry, and Occupations”
  - courses: HTS 3011 ⟵ “HTS 3011 - The City in American History”
  - courses: HTS 3012 ⟵ “HTS 3012 - Urban Sociology”
  - courses: HTS 3016 ⟵ “HTS 3016 - Women and Gender in the United States”
  - courses: HTS 2017 ⟵ “HTS 2017 - Environmental Sociology”
  - courses: HTS 3019 ⟵ “HTS 3019 - The Family, Sexuality, and Social Change in America”
  - courses: HTS 3020 ⟵ “HTS 3020 - Gender and Technology”
  - courses: HTS 3021 ⟵ “HTS 3021 - Women in Science and Engineering”
  - courses: HTS 3026 ⟵ “HTS 3026 - Sociology of Race and Ethnicity”
  - courses: HTS 3064 ⟵ “HTS 3064 - Sociology of Development”
  - courses: HTS 3071 ⟵ “HTS 3071 - Sociology of Crime”
  - courses: HTS 3072 ⟵ “HTS 3072 - Sociology of Education”
  - courses: HTS 3081 ⟵ “HTS 3081 - Technology and the Environment”
  - courses: HTS 3086 ⟵ “HTS 3086 - Sociology of Medicine and Health”
### `a440a55a1e9c96b3` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1331 ⟵ “CS 1331 - Introduction to Object Oriented Programming”
  - courses: CS 2110 ⟵ “CS 2110 - Computer Organization and Programming”
  - courses: MATH 2551 ⟵ “MATH 2551 - Multivariable Calculus”
  - courses: MATH 2552 ⟵ “MATH 2552 - Differential Equations”
### `a462540c8acc61ac` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - courses: CS 1371 ⟵ “CS 1371 - Computing for Engineers”
### `a640da8ef26bc9b1` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-communicating- [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `a6f93ed13311b993` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-major-requirem [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: INTA 1110 ⟵ “INTA 1110 - Introduction to International Relations”
  - courses: INTA 2001 ⟵ “INTA 2001 - Careers in International Affairs”
  - courses: INTA 3110 ⟵ “INTA 3110 - U.S. Foreign Policy 2”
  - courses: INTA 3203 ⟵ “INTA 3203 - Comparative Politics 2”
  - courses: INTA 3301 ⟵ “INTA 3301 - International Political Economy 2”
  - courses: INTA 4500 ⟵ “INTA 4500 - Pro-Seminar in International Affairs 2”
### `a893c7cf602fae5a` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `a8cd6443b5fa4646` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-political-science-a [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `aa10a83b8df5c571` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped
  - courses: INTA 2010 ⟵ “INTA 2010 - Empirical Methods 2”
  - courses: INTA 2040 ⟵ “INTA 2040 - Science, Technology, and International Affairs 2”
  - courses: BMED 2400 ⟵ “BMED 2400 - Introduction to Bioengineering Statistics”
  - courses: CP 4510 ⟵ “CP 4510 - Fundamentals of Geographic Information Systems”
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
  - courses: CS 1316 ⟵ “CS 1316 - Representing Structure and Behavior”
  - courses: CS 1331 ⟵ “CS 1331 - Introduction to Object Oriented Programming”
  - courses: CS 2316 ⟵ “CS 2316 - Data Manipulation for Science and Industry”
  - courses: EAS 3110 ⟵ “EAS 3110 - Energy, Environment, and Society”
  - courses: EAS 4480 ⟵ “EAS 4480 - Environmental Data Analysis”
  - courses: ECE 2020 ⟵ “ECE 2020 - Digital System Design”
  - courses: ID 3103 ⟵ “ID 3103 - Industrial Design Computing I”
  - courses: LMC 3402 ⟵ “LMC 3402 - Graphic and Visual Design”
  - courses: LMC 3410 ⟵ “LMC 3410 - The Rhetoric of Nonlinear Documents”
  - courses: ME 2016 ⟵ “ME 2016 - Computer Applications”
  - courses: MGT 2210 ⟵ “MGT 2210 - Information Systems and Digital Transformation”
  - courses: MGT 4051 ⟵ “MGT 4051 - Decision Support and Expert Systems”
  - courses: MGT 4052 ⟵ “MGT 4052 - Systems Analysis and Design”
### `ad2c416efebdd81e` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-astrophysics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-astrophysics-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/astrophysics-bs/ (sha256 85a63e286d77)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `af7b81d2710c50cc` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog · requirement_key=bachelor-of-science-in-environmental-science-technology-mathematics-and-sciences [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
### `b04d24b59443e3c6` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-communicatin [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `b11f650f49ffc7b1` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `b15cddb7fd5ad4db` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-cx-math-4640 [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: CX 4641 ⟵ “CX 4641 - Numerical Analysis II”
### `b240b235f92f46fb` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-mathematics- [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `b4a2a34d4bfd073f` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `b52603caa4c0e7b3` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-political-science-and [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `b698d54a124452c7` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-environmental-engineering-technical-elective [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - courses: CEE 4210 ⟵ “CEE 4210 - Hydrology”
  - courses: CEE 3400 ⟵ “CEE 3400 - Introduction to Geotechnical Engineering”
  - courses: CEE 4620 ⟵ “CEE 4620 - Environmental Impact Assessment”
  - courses: CEE 4795 ⟵ “CEE 4795 - Groundwater Hydrology”
### `b6a462208f0ad50b` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-technology-mathematic [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
### `b75aef3d03a39afd` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-research-option [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped
  - courses: CHEM 1212K ⟵ “CHEM 1212K - Chemical Principles II”
  - courses: CHEM 1211K ⟵ “CHEM 1211K - Chemical Principles I”
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
  - courses: CS 1371 ⟵ “CS 1371 - Computing for Engineers”
  - courses: EAS 3110 ⟵ “EAS 3110 - Energy, Environment, and Society”
  - courses: EAS 4300 ⟵ “EAS 4300 - Introduction to Physical and Chemical Oceanography”
  - courses: EAS 4305 ⟵ “EAS 4305 - Physical and Chemical Oceanography”
  - courses: EAS 4410 ⟵ “EAS 4410 - Climate and Global Change”
  - courses: EAS 4450 ⟵ “EAS 4450 - Synoptic Meteorology”
  - courses: EAS 4525 ⟵ “EAS 4525 - Weather Risk and Catastrophe Modeling”
  - courses: EAS 4470 ⟵ “EAS 4470 - Large-scale Atmospheric Circulations”
  - courses: EAS 4740 ⟵ “EAS 4740 - Atmospheric Chemistry Laboratory”
  - courses: EAS 4420 ⟵ “EAS 4420 - Environmental Field Methods”
  - courses: EAS 4480 ⟵ “EAS 4480 - Environmental Data Analysis”
  - courses: EAS 4610 ⟵ “EAS 4610 - Earth System Modeling”
  - courses: EAS 4651 ⟵ “EAS 4651 - Practical Internship”
  - courses: EAS 4670 ⟵ “EAS 4670 - Atmospheric Dynamics II”
  - courses: EAS 4695 ⟵ “EAS 4695 - Undergraduate Internship”
  - courses: EAS 4698 ⟵ “EAS 4698 - Undergraduate Research Assistantship”
  - courses: EAS 4699 ⟵ “EAS 4699 - Undergraduate Research”
  - courses: EAS 4803 ⟵ “EAS 4803 - Special Topics (Tropical Dynamics)”
  - courses: EAS 4803 ⟵ “EAS 4803 - Special Topics (Glacial and Ice Sheet Dynamics)”
  - courses: EAS 4813 ⟵ “EAS 4813 - Special Topics (Mesoscale Meteorology)”
  - courses: EAS 4814 ⟵ “EAS 4814 - Special Topics-Lab (Geophysical Field Methods)”
### `b8aec203d3067376` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-mathematics-and-quantitative-sk [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `bb1907ec91d6e88f` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-technical-elective-focus [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped
  - section: program-educational-objectives-technical-elective-focus ⟵ “Program Educational Objectives — Technical Elective Focus”
### `bbc9f64bf33387bd` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped
  - courses: CS 1371 ⟵ “CS 1371 - Computing for Engineers”
### `bbebeb55be42e554` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `bc42625c4d39d45f` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-mathematical-intelligence-and-d [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: CS 3600 ⟵ “CS 3600 - Introduction to Artificial Intelligence”
  - courses: CS 3630 ⟵ “CS 3630 - Introduction to Perception and Robotics”
  - courses: CS 3790 ⟵ “CS 3790 - Introduction to Cognitive Science”
  - courses: PSYC 3040 ⟵ “PSYC 3040 - Sensation and Perception”
  - courses: CS 4641 ⟵ “CS 4641 - Machine Learning”
  - courses: CX 4240 ⟵ “CX 4240 - Introduction to Computing for Data Analysis”
  - courses: MATH 4210 ⟵ “MATH 4210 - Mathematical Foundations of Data Science”
  - courses: CS 3510 ⟵ “CS 3510 - Design and Analysis of Algorithms”
  - courses: CS 3511 ⟵ “CS 3511 - Design and Analysis of Algorithms, Honors”
  - courses: CX 4140 ⟵ “CX 4140 - Computational Modeling Algorithms”
  - courses: MATH 3012 ⟵ “MATH 3012 - Applied Combinatorics”
  - courses: MATH 4022 ⟵ “MATH 4022 - Introduction to Graph Theory”
  - courses: MATH 4107 ⟵ “MATH 4107 - Introduction to Abstract Algebra I”
  - courses: MATH 4221 ⟵ “MATH 4221 - Stochastic Processes I”
  - courses: MATH 4222 ⟵ “MATH 4222 - Stochastic Processes II”
  - courses: MATH 4280 ⟵ “MATH 4280 - Introduction to Information Theory”
  - courses: MATH 4318 ⟵ “MATH 4318 - Analysis II”
  - courses: MATH 4320 ⟵ “MATH 4320 - Complex Analysis”
  - courses: MATH 4347 ⟵ “MATH 4347 - Partial Differential Equations I”
  - courses: MATH 4441 ⟵ “MATH 4441 - Differential Geometry”
  - courses: MATH 4541 ⟵ “MATH 4541 - Dynamics and Bifurcations I”
  - courses: MATH 4580 ⟵ “MATH 4580 - Linear Programming”
  - courses: MATH 4803 ⟵ “MATH 4803 - Special Topics (Advanced Statistical Theory for Machine Learning)”
  - courses: MATH 4803 ⟵ “MATH 4803 - Special Topics (Introduction to Stochastic Calculus)”
  - courses: MATH 4803 ⟵ “MATH 4803 - Special Topics (Introduction to Geometric Methods in Machine Learning)”
  - … 9 more rows
### `bf39eddf1961a5db` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-theoretical-computer-science-an [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 3012 ⟵ “MATH 3012 - Applied Combinatorics”
  - courses: CS 2050 ⟵ “CS 2050 - Introduction to Discrete Mathematics for Computer Science”
  - courses: CS 3510 ⟵ “CS 3510 - Design and Analysis of Algorithms”
  - courses: CS 4510 ⟵ “CS 4510 - Automata and Complexity Theory”
  - courses: CS 4540 ⟵ “CS 4540 - Advanced Algorithms”
  - courses: MATH 4012 ⟵ “MATH 4012 - Algebraic Structures in Coding Theory”
  - courses: MATH 4022 ⟵ “MATH 4022 - Introduction to Graph Theory”
  - courses: MATH 4032 ⟵ “MATH 4032 - Combinatorial Analysis”
  - courses: MATH 4107 ⟵ “MATH 4107 - Introduction to Abstract Algebra I”
  - courses: MATH 4108 ⟵ “MATH 4108 - Introduction to Abstract Algebra II”
  - courses: MATH 4150 ⟵ “MATH 4150 - Introduction to Number Theory”
  - courses: MATH 4210 ⟵ “MATH 4210 - Mathematical Foundations of Data Science”
  - courses: MATH 4221 ⟵ “MATH 4221 - Stochastic Processes I”
  - courses: MATH 4222 ⟵ “MATH 4222 - Stochastic Processes II”
  - courses: MATH 4280 ⟵ “MATH 4280 - Introduction to Information Theory”
  - courses: MATH 4318 ⟵ “MATH 4318 - Analysis II”
  - courses: MATH 4580 ⟵ “MATH 4580 - Linear Programming”
  - courses: MATH 4803 ⟵ “MATH 4803 - Special Topics (Advanced Statistical Theory for Machine Learning)”
  - courses: CS 3235 ⟵ “CS 3235 - Introduction to Information Security”
  - courses: CS 3600 ⟵ “CS 3600 - Introduction to Artificial Intelligence”
  - courses: CS 3790 ⟵ “CS 3790 - Introduction to Cognitive Science”
  - courses: CS 4641 ⟵ “CS 4641 - Machine Learning”
  - courses: CS 4644 ⟵ “CS 4644 - Deep Learning”
  - courses: CX 4220 ⟵ “CX 4220 - Introduction to High Performance Computing”
  - courses: CX 4240 ⟵ “CX 4240 - Introduction to Computing for Data Analysis”
### `c01aaff3af3ac116` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-political-science-and-u-s-history [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
  - courses: HIST 2112 ⟵ “HIST 2112 - The United States since 1877”
  - courses: INTA 1200 ⟵ “INTA 1200 - American Government in Comparative Perspective”
  - courses: POL 1101 ⟵ “POL 1101 - Government of the United States”
  - courses: PUBP 3000 ⟵ “PUBP 3000 - American Constitutional Issues”
### `c13b1738e0784d39` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biology-georgia-tech-catalog · requirement_key=research-option [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biology-bs/ (sha256 ec9e3c6e4ffa)
- issues: course_alternatives_in_rule_text
  - courses: BIOS 4699 ⟵ “BIOS 4699 - Undergraduate Research”
  - courses: BIOS 4698 ⟵ “BIOS 4698 - Research Assistantship”
  - courses: BIOS 4690 ⟵ “BIOS 4690 - Independent Research Project”
### `c2ceff083c8f4eea` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-institutional-prior [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
### `c624a10ad7c906a9` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-bs/ (sha256 a42622d67c4a)
- issues: requirement_groups_skipped
  - courses: ECON 2105 ⟵ “ECON 2105 - Principles of Macroeconomics 3”
  - courses: ECON 2106 ⟵ “ECON 2106 - Principles of Microeconomics 3”
  - courses: ECON 2250 ⟵ “ECON 2250 - Statistics for Economists”
### `c831c06496d87fac` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped
  - courses: BC 2636 ⟵ “BC 2636 - Construction Safety”
  - courses: BC 3600 ⟵ “BC 3600 - Construction Cost Management”
  - courses: BC 3610 ⟵ “BC 3610 - Construction Law”
  - courses: BC 3630 ⟵ “BC 3630 - Project Management I”
  - courses: BC 3640 ⟵ “BC 3640 - Construction Mechanics”
  - courses: BC 4050 ⟵ “BC 4050 - Building Information Modeling for Multi-disciplinary Integration”
  - courses: BC 4130 ⟵ “BC 4130 - Intg Design Constr & Dev”
  - courses: BC 4600 ⟵ “BC 4600 - Project Management II”
  - courses: BC 4630 ⟵ “BC 4630 - Senior Capstone Project”
  - courses: BC 4660 ⟵ “BC 4660 - Entrepreneurship in Construction”
  - courses: BC 4672 ⟵ “BC 4672 - Mechanical, Electrical and Plumbing Systems for Construction Managers”
  - courses: BC 4680 ⟵ “BC 4680 - Professional Internship”
  - courses: BC 4710 ⟵ “BC 4710 - Green Construction”
  - courses: MGT 2106 ⟵ “MGT 2106 - Legal, Social, Ethical Aspects of Business”
  - courses: MGT 3000 ⟵ “MGT 3000 - Financial and Managerial Accounting”
  - courses: MGT 3078 ⟵ “MGT 3078 - Finance and Investments”
  - courses: MGT 3101 ⟵ “MGT 3101 - Organizational Behavior”
### `c88e4d170c739a51` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1371 ⟵ “CS 1371 - Computing for Engineers”
### `c9e093d63becaab5` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-wellness-requiremen [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `cb08355e665db431` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-global-studies [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
  - courses: HTS 1031 ⟵ “HTS 1031 - Europe Since the Renaissance”
  - courses: HTS 2036 ⟵ “HTS 2036 - Revolutionary Europe: 1789-1914”
  - courses: HTS 2037 ⟵ “HTS 2037 - Twentieth Century Europe: 1914 to Present”
  - courses: HTS 2040 ⟵ “HTS 2040 - History of Islamic Societies”
  - courses: HTS 2041 ⟵ “HTS 2041 - History of the Modern Middle East”
  - courses: HTS 2051 ⟵ “HTS 2051 - Colonial Latin America and the World”
  - courses: HTS 2061 ⟵ “HTS 2061 - Traditional Asia and Its Legacy”
  - courses: HTS 2062 ⟵ “HTS 2062 - Asia in the Modern World”
  - courses: HTS 2053 ⟵ “HTS 2053 - Modern Latin American History”
  - courses: HTS 2100 ⟵ “HTS 2100 - Sci, Tech & Modern World”
  - courses: HTS 3028 ⟵ “HTS 3028 - Ancient Greece: Gods, Heroes, and RuinS”
  - courses: HTS 3029 ⟵ “HTS 3029 - Ancient Rome: From Greatness to Ruins”
  - courses: HTS 3030 ⟵ “HTS 3030 - Medieval Europe: 350 to 1400”
  - courses: HTS 3031 ⟵ “HTS 3031 - European Labor History”
  - courses: HTS 3032 ⟵ “HTS 3032 - Modern European Intellectual History”
  - courses: HTS 3033 ⟵ “HTS 3033 - Medieval England”
  - courses: HTS 3035 ⟵ “HTS 3035 - Britain from 1815-1914”
  - courses: HTS 3036 ⟵ “HTS 3036 - Britain Since 1914”
  - courses: HTS 3038 ⟵ “HTS 3038 - The French Revolution”
  - courses: HTS 3039 ⟵ “HTS 3039 - Modern France”
  - courses: HTS 3041 ⟵ “HTS 3041 - Modern Spain”
  - courses: HTS 3046 ⟵ “HTS 3046 - Science, Politics, and Culture in Nazi Germany”
  - courses: HTS 3048 ⟵ “HTS 3048 - Modern Russian History and Society”
  - courses: HTS 3051 ⟵ “HTS 3051 - Women and the Politics of Gender in the Middle East”
  - courses: HTS 3055 ⟵ “HTS 3055 - Globalization in the Modern Era”
  - … 5 more rows
### `cb6892cecb027763` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-political-science-and-u- [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
  - courses: HIST 2112 ⟵ “HIST 2112 - The United States since 1877”
  - courses: INTA 1200 ⟵ “INTA 1200 - American Government in Comparative Perspective”
  - courses: POL 1101 ⟵ “POL 1101 - Government of the United States”
  - courses: PUBP 3000 ⟵ “PUBP 3000 - American Constitutional Issues”
### `cc4512791fb33ae7` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped
  - section: program-educational-objectives-free-electives ⟵ “Program Educational Objectives — Free Electives”
### `cdadda3edf9b2b75` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-engineering-bs/ (sha256 260180e8bb6e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: COE 2001 ⟵ “COE 2001 - Statics 3”
  - courses: MATH 2551 ⟵ “MATH 2551 - Multivariable Calculus”
  - courses: MATH 2552 ⟵ “MATH 2552 - Differential Equations 3”
  - courses: CHEM 1310 ⟵ “CHEM 1310 - Principles of General Chemistry for Engineers 3”
### `ceec65de27d0a907` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-communicating-in-writing [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped
  - courses: ENGL 1101 ⟵ “ENGL 1101 - English Composition I”
  - courses: ENGL 1102 ⟵ “ENGL 1102 - English Composition II”
### `d0ebac075023e9bd` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-technology-mathematics-and-sciences [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped
  - courses: MATH 1551 ⟵ “MATH 1551 - Differential Calculus”
  - courses: MATH 1553 ⟵ “MATH 1553 - Introduction to Linear Algebra”
### `d164b242e3d722bf` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-technology-m-2 [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
  - courses: CS 2110 ⟵ “CS 2110 - Computer Organization and Programming”
  - courses: CS 2261 ⟵ “CS 2261 - Media Device Architectures”
  - courses: CS 3600 ⟵ “CS 3600 - Introduction to Artificial Intelligence”
  - courses: CS 4455 ⟵ “CS 4455 - Video Game Design and Programming”
  - courses: CS 4496 ⟵ “CS 4496 - Computer Animation”
  - courses: CS 4625 ⟵ “CS 4625 - Intelligent and Interactive Systems”
  - courses: CS 4635 ⟵ “CS 4635 - Knowledge-Based Artificial Intelligence”
  - courses: CS 4641 ⟵ “CS 4641 - Machine Learning”
  - courses: CS 4644 ⟵ “CS 4644 - Deep Learning”
  - courses: CS 4731 ⟵ “CS 4731 - Game AI”
  - courses: ECE 2026 ⟵ “ECE 2026 - Introduction to Signal Processing”
  - courses: ECE 3077 ⟵ “ECE 3077 - Prob/Stats for ECE”
  - courses: ECE 3084 ⟵ “ECE 3084 - Signals and Systems”
  - courses: ECE 3251 ⟵ “ECE 3251 - Optimization for Information Systems”
  - courses: ECE 3710 ⟵ “ECE 3710 - Circuits and Electronics”
  - courses: ECE 4252 ⟵ “ECE 4252 - Fundamentals of Machine Learning (FunML)”
  - courses: ECE 4258 ⟵ “ECE 4258 - Digital Image Processing”
  - courses: ECE 4260 ⟵ “ECE 4260 - Random Signals and Applications”
  - courses: ECE 4270 ⟵ “ECE 4270 - Fundamentals of Digital Signal Processing”
### `d43057c688b15f07` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-econ-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-global-economics-and-modern-languages-econ-electives ⟵ “Bachelor of Science in Global Economics and Modern Languages — ECON Electives”
### `d850e866c8bb3808` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-wellness-requirement [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: APPH 1040 ⟵ “APPH 1040 - Scientific Foundations of Health”
### `d9b70a529f257e5d` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-cx-math-4641 [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: ECE 3084 ⟵ “ECE 3084 - Signals and Systems”
  - courses: ECE 3251 ⟵ “ECE 3251 - Optimization for Information Systems”
  - courses: ISYE 4133 ⟵ “ISYE 4133 - Advanced Optimization”
### `dc8236a30fc71ff4` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-environmental-science-georgia-tech-catalog · requirement_key=bachelor-of-science-in-environmental-science-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/environmental-science-bs/ (sha256 f3ba42be09ad)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
### `df3ef41b26ee0c80` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
### `dfc48ccc86def748` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-technology-mat [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 1711 ⟵ “MATH 1711 - Finite Mathematics”
### `e10f2b5de6ce1c8b` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-entrepreneur [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MGT 4803 ⟵ “MGT 4803 - Special Topics in Management (Start up Lab)”
  - courses: MGT 3101 ⟵ “MGT 3101 - Organizational Behavior”
  - courses: MGT 3150 ⟵ “MGT 3150 - Principles of Management”
  - courses: MGT 4450 ⟵ “MGT 4450 - Project Management”
  - courses: MGT 4670 ⟵ “MGT 4670 - Entrepreneurship”
### `e26d264268adf59c` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-additional-m [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ARCH 3200 ⟵ “ARCH 3200 - Portfolio Design”
  - courses: CS 2110 ⟵ “CS 2110 - Computer Organization and Programming”
  - courses: CS 3790 ⟵ “CS 3790 - Introduction to Cognitive Science”
  - courses: FREN 3110 ⟵ “FREN 3110 - Comics & Graphic Arts”
  - courses: FREN 4013 ⟵ “FREN 4013 - French Literature and the Visual Arts”
  - courses: FREN 4105 ⟵ “FREN 4105 - Francophone Cinema”
  - courses: FREN 4246 ⟵ “FREN 4246 - French and Francophone Films and Media”
  - courses: GT 1000 ⟵ “GT 1000 - Freshman Seminar”
  - courses: ID 2325 ⟵ “ID 2325 - User Centered Design Methods”
  - courses: ID 2401 ⟵ “ID 2401 - Visual Design Thinking”
  - courses: ID 3320 ⟵ “ID 3320 - Design Methods: User Centered Design”
  - courses: LMC 3403 ⟵ “LMC 3403 - Technical Communication, Theory and Practice”
  - courses: LMC 3451 ⟵ “LMC 3451 - Race, Gender, and Digital Media”
  - courses: MGT 2250 ⟵ “MGT 2250 - Management Statistics”
  - courses: MGT 3000 ⟵ “MGT 3000 - Financial and Managerial Accounting”
  - courses: MGT 3103 ⟵ “MGT 3103 - Leadership in a Changing Environment”
  - courses: MGT 3150 ⟵ “MGT 3150 - Principles of Management”
  - courses: MGT 3300 ⟵ “MGT 3300 - Marketing Management I”
  - courses: MGT 3607 ⟵ “MGT 3607 - Business Ethics”
  - courses: MGT 3614 ⟵ “MGT 3614 - Law for Entrepreneurs”
  - courses: MGT 3743 ⟵ “MGT 3743 - Analysis of Emerging Technologies”
  - courses: MGT 4311 ⟵ “MGT 4311 - Digital Marketing”
  - courses: MGT 4726 ⟵ “MGT 4726 - Privacy, Technology, Policy, and Law”
  - courses: MGT 4803 ⟵ “MGT 4803 - Special Topics in Management (Sports and Entertainment Practicum)”
  - courses: MGT 4803 ⟵ “MGT 4803 - Special Topics in Management (Sports and Entertainment Marketing)”
  - … 13 more rows
### `e300e7436a4af7f3` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-georgia-tech-catalog · requirement_key=bachelor-of-science-in-atmospheric-and-oceanic-sciences-mathematics-and-quantita [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ (sha256 99fa5bfbfe61)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus”
### `e403de399e66f94a` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-and-modern-languages-georgia-tech-c · requirement_key=bachelor-of-science-in-international-affairs-and-modern-languages-institutional- [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-modern-language-bs/ (sha256 1af384ea79f6)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
### `e443a4e17b4ed102` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-aerospace-engineering-georgia-tech-catalog · requirement_key=program-educational-objectives-mathematics-and-quantitative-skills [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/aerospace-engineering-bs/ (sha256 ac00804277e5)
- issues: requirement_groups_skipped
  - courses: MATH 1552 ⟵ “MATH 1552 - Integral Calculus 1”
### `e4cc107b2d62bcba` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-global-economics-and-modern-languages-georgia-tech-catalo · requirement_key=bachelor-of-science-in-global-economics-and-modern-languages-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ (sha256 78ca3f38caba)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-global-economics-and-modern-languages-free-electives ⟵ “Bachelor of Science in Global Economics and Modern Languages — Free Electives”
### `e6265c9f94a4d5b1` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-institutional-priority [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
### `e7b246d05a647fb0` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-architecture-georgia-tech-catalog · requirement_key=bachelor-of-science-in-architecture-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/architecture-bs/ (sha256 172bc7fddff6)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-architecture-free-electives ⟵ “Bachelor of Science in Architecture — Free Electives”
### `e81448f48e4cb719` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-cx-math-4803 [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: ISYE 4133 ⟵ “ISYE 4133 - Advanced Optimization”
  - courses: EAS 4610 ⟵ “EAS 4610 - Earth System Modeling”
  - courses: EAS 4630 ⟵ “EAS 4630 - Physics of the Earth”
### `ea0efc0d17615b02` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-biomedical-engineering-georgia-tech-catalog · requirement_key=bachelor-of-science-in-biomedical-engineering-bmed-breadth-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/biomedical-engineering-bs/ (sha256 db06459326ab)
- issues: requirement_groups_skipped
  - section: bachelor-of-science-in-biomedical-engineering-bmed-breadth-electives ⟵ “Bachelor of Science in Biomedical Engineering — BMED Breadth Electives”
### `ebfe22c3766df42f` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-georgia-tech · requirement_key=bachelor-of-science-in-arts-entertainment-and-creative-technologies-major-requir [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ (sha256 a5177aef45cf)
- issues: requirement_groups_skipped
  - courses: AECT 3000 ⟵ “AECT 3000 - Visual Arts and Design Studio I”
  - courses: AECT 3100 ⟵ “AECT 3100 - Sound for Artistic Expression”
  - courses: AECT 3200 ⟵ “AECT 3200 - History and Critique of Arts and Technology”
  - courses: AECT 3400 ⟵ “AECT 3400 - Visual Arts and Design Studio II”
  - courses: AECT 3500 ⟵ “AECT 3500 - Worldbuilding Studio”
  - courses: AECT 4000 ⟵ “AECT 4000 - Senior Capstone for Arts, Entertainment, and Creative Technologies I”
  - courses: AECT 4500 ⟵ “AECT 4500 - Senior Capstone for Arts, Entertainment, and Creative Technologies II”
### `eef225a622653b44` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-political-science-and [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 2111 ⟵ “HIST 2111 - The United States to 1877”
### `ef60c42bd1c8ac12` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-science-technology-and-med [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
  - courses: HTS 1081 ⟵ “HTS 1081 - Engineering in History”
  - courses: HTS 2080 ⟵ “HTS 2080 - Introduction to the History of Disease and Medicine”
  - courses: HTS 2081 ⟵ “HTS 2081 - The Scientific Revolution”
  - courses: HTS 2082 ⟵ “HTS 2082 - Technology and Science in the Industrial Age”
  - courses: HTS 2084 ⟵ “HTS 2084 - Technology and Society”
  - courses: HTS 2100 ⟵ “HTS 2100 - Sci, Tech & Modern World”
  - courses: HTS 3020 ⟵ “HTS 3020 - Gender and Technology”
  - courses: HTS 3021 ⟵ “HTS 3021 - Women in Science and Engineering”
  - courses: HTS 3046 ⟵ “HTS 3046 - Science, Politics, and Culture in Nazi Germany”
  - courses: HTS 3080 ⟵ “HTS 3080 - History of Rocketry”
  - courses: HTS 3081 ⟵ “HTS 3081 - Technology and the Environment”
  - courses: HTS 3082 ⟵ “HTS 3082 - Sociology of Science”
  - courses: HTS 3084 ⟵ “HTS 3084 - Culture and Technology”
  - courses: HTS 3086 ⟵ “HTS 3086 - Sociology of Medicine and Health”
  - courses: HTS 3087 ⟵ “HTS 3087 - History of Medicine”
  - courses: HTS 3088 ⟵ “HTS 3088 - Race, Medicine & Science”
  - courses: HTS 3089 ⟵ “HTS 3089 - Science, Technology and Sports”
### `ef8ecfc6ffe09289` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-mathematics-and-computing-georgia-tech-catalog · requirement_key=bachelor-of-science-in-mathematics-and-computing-cx-math-4803-2 [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/mathematics-computing-bs/ (sha256 7b877e8f6058)
- issues: requirement_groups_skipped
  - courses: ECE 4270 ⟵ “ECE 4270 - Fundamentals of Digital Signal Processing”
  - courses: ECE 4271 ⟵ “ECE 4271 - Applications of Digital Signal Processing”
  - courses: ISYE 4133 ⟵ “ISYE 4133 - Advanced Optimization”
### `f18ca142fcd90a8a` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-history-technology-and-society-georgia-tech-catalog · requirement_key=bachelor-of-science-in-history-technology-and-society-power-inequality-and-socia [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/history-technology-society-bs/ (sha256 2043c64972fc)
- issues: requirement_groups_skipped
  - courses: HTS 2016 ⟵ “HTS 2016 - Social Issues and Public Policy”
  - courses: HTS 2018 ⟵ “HTS 2018 - Food and Society”
  - courses: HTS 2086 ⟵ “HTS 2086 - Semester in the City: Engaging Communities”
  - courses: HTS 3006 ⟵ “HTS 3006 - United States Labor History”
  - courses: HTS 3007 ⟵ “HTS 3007 - Sociology of Work, Industry, and Occupations”
  - courses: HTS 3008 ⟵ “HTS 3008 - Class, Power, and Social Inequality”
  - courses: HTS 3011 ⟵ “HTS 3011 - The City in American History”
  - courses: HTS 3012 ⟵ “HTS 3012 - Urban Sociology”
  - courses: HTS 3016 ⟵ “HTS 3016 - Women and Gender in the United States”
  - courses: HTS 3017 ⟵ “HTS 3017 - Sociology of Gender”
  - courses: HTS 3019 ⟵ “HTS 3019 - The Family, Sexuality, and Social Change in America”
  - courses: HTS 3020 ⟵ “HTS 3020 - Gender and Technology”
  - courses: HTS 3021 ⟵ “HTS 3021 - Women in Science and Engineering”
  - courses: HTS 3022 ⟵ “HTS 3022 - Gender and Sports”
  - courses: HTS 3023 ⟵ “HTS 3023 - Slaves without Masters: Free People of Color before 1865”
  - courses: HTS 3024 ⟵ “HTS 3024 - African American History to 1865”
  - courses: HTS 3025 ⟵ “HTS 3025 - African American History since 1865”
  - courses: HTS 3026 ⟵ “HTS 3026 - Sociology of Race and Ethnicity”
  - courses: HTS 3027 ⟵ “HTS 3027 - The Civil Rights Movement”
  - courses: HTS 3031 ⟵ “HTS 3031 - European Labor History”
  - courses: HTS 3051 ⟵ “HTS 3051 - Women and the Politics of Gender in the Middle East”
  - courses: HTS 3064 ⟵ “HTS 3064 - Sociology of Development”
  - courses: HTS 3067 ⟵ “HTS 3067 - Revolutionary Movements in the Modern World”
  - courses: HTS 3068 ⟵ “HTS 3068 - Social Movements”
  - courses: HTS 3071 ⟵ “HTS 3071 - Sociology of Crime”
  - … 3 more rows
### `f40d80e2d1880808` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped
  - courses: INTA 2010 ⟵ “INTA 2010 - Empirical Methods 2”
  - courses: INTA 2040 ⟵ “INTA 2040 - Science, Technology, and International Affairs 2”
  - courses: BMED 2400 ⟵ “BMED 2400 - Introduction to Bioengineering Statistics”
  - courses: CP 4510 ⟵ “CP 4510 - Fundamentals of Geographic Information Systems”
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
  - courses: CS 1315 ⟵ “CS 1315 - Introduction to Media Computation”
  - courses: CS 1331 ⟵ “CS 1331 - Introduction to Object Oriented Programming”
  - courses: CS 2316 ⟵ “CS 2316 - Data Manipulation for Science and Industry”
  - courses: EAS 3110 ⟵ “EAS 3110 - Energy, Environment, and Society”
  - courses: EAS 4480 ⟵ “EAS 4480 - Environmental Data Analysis”
  - courses: ECE 2020 ⟵ “ECE 2020 - Digital System Design”
  - courses: ID 3103 ⟵ “ID 3103 - Industrial Design Computing I”
  - courses: LMC 3402 ⟵ “LMC 3402 - Graphic and Visual Design”
  - courses: ME 2016 ⟵ “ME 2016 - Computer Applications”
  - courses: MGT 2210 ⟵ “MGT 2210 - Information Systems and Digital Transformation”
  - courses: MGT 4052 ⟵ “MGT 4052 - Systems Analysis and Design”
### `f581b466f2043294` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-field-of-study [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped
  - courses: ID 1011 ⟵ “ID 1011 - Industrial Design Fundamentals 1”
  - courses: ID 1012 ⟵ “ID 1012 - Industrial Design Fundamentals 2”
  - courses: ID 1101 ⟵ “ID 1101 - Introduction to Industrial Design 1”
  - courses: ID 1102 ⟵ “ID 1102 - Introduction to Industrial Design 2”
  - courses: ID 1401 ⟵ “ID 1401 - Introduction to Graphic Communications 1”
  - courses: ID 1402 ⟵ “ID 1402 - Introduction to Graphic Communications 2”
  - courses: ID 1418 ⟵ “ID 1418 - Introduction to Sketching and Modeling 1”
  - courses: ID 2023 ⟵ “ID 2023 - Industrial Design Studio 1”
  - courses: ID 2024 ⟵ “ID 2024 - Industrial Design Studio 2”
  - courses: ID 2242 ⟵ “ID 2242 - History of Art 2”
### `f8099071b08282c2` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-industrial-design-georgia-tech-catalog · requirement_key=grade-requirements-free-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/industrial-design-bs/ (sha256 1745102523ff)
- issues: requirement_groups_skipped
  - section: grade-requirements-free-electives ⟵ “Grade Requirements — Free Electives”
### `f85804502b8ed0ca` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-eia-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped
  - courses: HTS 1031 ⟵ “HTS 1031 - Europe Since the Renaissance”
  - courses: HTS 2036 ⟵ “HTS 2036 - Revolutionary Europe: 1789-1914”
  - courses: HTS 2037 ⟵ “HTS 2037 - Twentieth Century Europe: 1914 to Present”
  - courses: HTS 2040 ⟵ “HTS 2040 - History of Islamic Societies”
  - courses: HTS 2041 ⟵ “HTS 2041 - History of the Modern Middle East”
  - courses: HTS 2061 ⟵ “HTS 2061 - Traditional Asia and Its Legacy”
  - courses: HTS 2062 ⟵ “HTS 2062 - Asia in the Modern World”
  - courses: HTS 3028 ⟵ “HTS 3028 - Ancient Greece: Gods, Heroes, and RuinS”
  - courses: HTS 3029 ⟵ “HTS 3029 - Ancient Rome: From Greatness to Ruins”
  - courses: HTS 3030 ⟵ “HTS 3030 - Medieval Europe: 350 to 1400”
  - courses: HTS 3031 ⟵ “HTS 3031 - European Labor History”
  - courses: HTS 3032 ⟵ “HTS 3032 - Modern European Intellectual History”
  - courses: HTS 3033 ⟵ “HTS 3033 - Medieval England”
  - courses: HTS 3035 ⟵ “HTS 3035 - Britain from 1815-1914”
  - courses: HTS 3036 ⟵ “HTS 3036 - Britain Since 1914”
  - courses: HTS 3038 ⟵ “HTS 3038 - The French Revolution”
  - courses: HTS 3039 ⟵ “HTS 3039 - Modern France”
  - courses: HTS 3041 ⟵ “HTS 3041 - Modern Spain”
  - courses: HTS 3046 ⟵ “HTS 3046 - Science, Politics, and Culture in Nazi Germany”
  - courses: HTS 3051 ⟵ “HTS 3051 - Women and the Politics of Gender in the Middle East”
  - courses: HTS 3061 ⟵ “HTS 3061 - Modern China”
  - courses: HTS 3062 ⟵ “HTS 3062 - Modern Japan”
  - courses: HTS 3064 ⟵ “HTS 3064 - Sociology of Development”
  - courses: HTS 3065 ⟵ “HTS 3065 - History of Global Societies”
  - courses: HTS 3067 ⟵ “HTS 3067 - Revolutionary Movements in the Modern World”
### `f94f5d2df5f17cc0` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-construction-science-and-management-georgia-tech-catalog · requirement_key=bachelor-of-science-in-construction-science-and-management-institutional-priorit [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/construction-science-and-management-bs/ (sha256 870035d98a77)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CS 1301 ⟵ “CS 1301 - Introduction to Computing”
### `fa884ca11a9236f3` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-economics-and-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-economics-and-international-affairs-major-requirements [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/economics-international-affairs-bs/ (sha256 480a92b8fd95)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ECON 2250 ⟵ “ECON 2250 - Statistics for Economists”
  - courses: ECON 3110 ⟵ “ECON 3110 - Advanced Microeconomic Analysis 2”
  - courses: ECON 3120 ⟵ “ECON 3120 - Advanced Macroeconomic Analysis 2”
  - courses: ECON 3161 ⟵ “ECON 3161 - Econometric Analysis 2”
  - courses: ECON 4351 ⟵ “ECON 4351 - International Financial Economics 2”
  - courses: INTA 1110 ⟵ “INTA 1110 - Introduction to International Relations”
  - courses: INTA 2040 ⟵ “INTA 2040 - Science, Technology, and International Affairs”
  - courses: INTA 2001 ⟵ “INTA 2001 - International Affairs Discovery Practicum”
  - courses: INTA 3203 ⟵ “INTA 3203 - Comparative Politics 2”
  - courses: INTA 3110 ⟵ “INTA 3110 - U.S. Foreign Policy”
  - courses: INTA 3301 ⟵ “INTA 3301 - International Political Economy”
  - courses: INTA 4740 ⟵ “INTA 4740 - Seminar in Political Economy 2”
### `fb4f3540a6c7aeb3` Georgia Institute of Technology-Main Campus — degree_requirements 2026-27 · program_key=bachelor-of-science-in-international-affairs-georgia-tech-catalog · requirement_key=bachelor-of-science-in-international-affairs-additional-inta-electives [new] (labeled_in_source)
- source: https://catalog.gatech.edu/programs/international-affairs-bs/ (sha256 4a5a9a903363)
- issues: requirement_groups_skipped
  - courses: ECON 2100 ⟵ “ECON 2100 - Economic Analysis and Policy Problems”
  - courses: ECON 2101 ⟵ “ECON 2101 - The Global Economy”
  - courses: ECON 2105 ⟵ “ECON 2105 - Principles of Macroeconomics”
  - courses: ECON 2106 ⟵ “ECON 2106 - Principles of Microeconomics”
### `1102f725e1e0f110` Georgia Military College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.gmc.edu/financial-aid/ (sha256 2d3d66aa7a0d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Students may appeal their cost of attendance by requesting a Professional Judgement (PJ).”
  - sentence: professional_judgment ⟵ “Changes in Financial Circumstances Parent Professional Judgment Request to Recalculate the Expected Family Contribution for Dependent Students: If the parents’ current expected income is substantially less than it was during the tax year used on the FAFSA due to special circumstances, we may be able to use the parents’ current estimated income to reevaluate eligibility for Federal Student Aid.”
  - sentence: professional_judgment ⟵ “Student Professional Judgment Request to Recalculate the Expected Family Contribution for Independent Students: If the students/spouses expected income is substantially less than it was during the tax year used on the FAFSA due to special circumstances, we may be able to use the students/spouses current estimated income to reevaluate eligibility for Federal Student Aid.”
### `1918282318b277f6` Georgia Military College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.gmc.edu/financial-aid/ (sha256 2d3d66aa7a0d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “The three areas for which we will consider PJ are: Increases in the student’s Cost of Attendance to account for extraordinary expenses a student might incur while attending GMC; Changes in financial circumstances including loss of income, loss of recurring taxed or untaxed income, loss of assets, or unusual medical expenses; Dependency override to change your financial aid dependency status from d”
  - sentence: dependency_override ⟵ “Dependency Status Appeals Petition to be declared an Independent Student for Federal Aid Purposes: The law governing Federal Student Aid (Title IV) categorizes students as “dependent” or “independent” based on the premise the student and parents have the primary responsibility for meeting the student’s educational costs.”
  - sentence: dependency_override ⟵ “If you can document the unusual or unique circumstances governing why you feel you should be declared independent for Title IV Federal Aid purposes, you may petition for a dependency override by completing this form and providing documentation.”
### `589b12316aec9abe` Georgia Military College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.gmc.edu/scholarships/ (sha256 904eab4f5012)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Eligibility Criteria To qualify, students must: • Meet the completion percentage for each enrolled program. • Submit both the GSFApp and the 2025–2026 FAFSA, including all required documentation, by the last day of the term for which they are applying. • Owe a balance to Georgia Military College for direct educational costs (e.g., tuition, fees, books, supplies, meal plans, and housing billed by t”
### `c65e4a1b8759644f` Georgia Military College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.gmc.edu/financial-aid/ (sha256 2d3d66aa7a0d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Cost of Attendance Increases Computer Purchase: Federal regulations permit GMC to consider the cost to purchase a computer when calculating a student’s Cost of Attendance (COA).”
### `36bd3a2ee8dd3091` Georgia Military College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.gmc.edu/tuition-fees/ (sha256 440ebaa793e4)
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
### `04dd064e4b8ea8dd` Georgia Northwestern Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gntc.edu/appeals/equal-opportunity/ (sha256 fe574e872e83)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “GNTC, TCSG and its constituent Technical Colleges do not discriminate on the basis of race, color, creed or religion, national or ethnic origin, sex (including pregnancy, sexual orientation and gender identity), disability, age, political affiliation or belief, genetic information, veteran or military status, marital status or citizenship status (except in those special circumstances permitted or ”
### `114e986faff522f5` Georgia Northwestern Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gntc.edu/appeals/financial-aid/ (sha256 9ac98b9b3af9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Contact Financial Aid for more information.”
### `0d804ac5c50c390e` Gordon State College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.gordonstate.edu/documents/departments/bursars-office/coa_2627.pdf (sha256 e78443a2a35f)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, conflicting_sources:https://www.gordonstate.edu/documents/departments/budgets/fy25-original-budget-packet.pdf,https://www.gordonstate.edu/documents/departments/budgets/fy26-budget-booklet1.pdf
- checks: {"columns": 4, "rows": 18}
  - on_campus:Tuition*: 3300 ⟵ “Tuition* | $3,300 | $3,300 | Tuition* | $4,830 | $4,830”
  - on_campus:Fees: 1028 ⟵ “Fees | $1,028 | $1,028 | Fees | $1,028 | $1,028”
  - on_campus:Housing: 7329 ⟵ “Housing | $7,329 | $13,941 | Housing | $7,329 | $13,941”
  - on_campus:Food: 3650 ⟵ “Food | $3,650 | $4,473 | Food | $3,650 | $4,473”
  - on_campus:Transportation: 5481 ⟵ “Transportation | $5,481 | $5,481 | Transportation | $5,481 | $5,481”
  - on_campus:Books and Supplies: 2043 ⟵ “Books and Supplies | $2,043 | $2,043 | Books and Supplies | $2,043 | $2,043”
  - on_campus:Personal Expenses: 3078 ⟵ “Personal Expenses | $3,078 | $3,078 | Personal Expenses | $3,078 | $3,078”
  - on_campus:Loan Fees: 92 ⟵ “Loan Fees | $92 | $92 | Loan Fees | $92 | $92”
  - on_campus:Total Cost of Attendance: 26001 ⟵ “Total Cost of Attendance | $26,001 | $33,436 | Total Cost of Attendance | $27,531 | $34,966”
  - on_campus:Tuition* (2): 13050 ⟵ “Tuition* | $13,050 | $13,050 | Tuition* | $13,440 | $13,440”
  - on_campus:Fees (2): 1028 ⟵ “Fees | $1,028 | $1,028 | Fees | $1,028 | $1,028”
  - on_campus:Housing**: 7329 ⟵ “Housing** | $7,329 | $13,941 | Housing** | $7,329 | $13,941”
  - on_campus:Food (2): 3650 ⟵ “Food | $3,650 | $4,473 | Food | $3,650 | $4,473”
  - on_campus:Transportation (2): 5481 ⟵ “Transportation | $5,481 | $5,481 | Transportation | $5,481 | $5,481”
  - on_campus:Books and Supplies (2): 2043 ⟵ “Books and Supplies | $2,043 | $2,043 | Books and Supplies | $2,043 | $2,043”
  - on_campus:Personal Expenses (2): 3078 ⟵ “Personal Expenses | $3,078 | $3,078 | Personal Expenses | $3,078 | $3,078”
  - on_campus:Loan Fees***: 92 ⟵ “Loan Fees*** | $92 | $92 | Student Health Insurance*** | $2,981 | $2,981”
  - on_campus:Total Cost of Attendance (2): 35751 ⟵ “Total Cost of Attendance | $35,751 | $43,186 | Total Cost of Attendance | $39,030 | $46,465”
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
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown, conflicting_sources:https://www.gordonstate.edu/documents/departments/budgets/fy25-original-budget-packet.pdf,https://www.gordonstate.edu/documents/departments/bursars-office/coa_2627.pdf
- checks: {"columns": 12, "rows": 2666}
  - column:STATE APPROPRIATIONS: 15739723 ⟵ “STATE APPROPRIATIONS | 15,739,723 | 16,011,237”
  - column:GENERAL OPERATIONS TOTAL: 15739723 ⟵ “GENERAL OPERATIONS TOTAL | 15,739,723 | 16,011,237”
  - column:TOTAL REVENUE: 15739723 ⟵ “TOTAL REVENUE | 15,739,723 | 16,011,237”
  - column:STUDENT TUITION AND FEES: 7450680 ⟵ “STUDENT TUITION AND FEES | 7,450,680 | 7,209,455”
  - column:GENERAL OPERATIONS TOTAL (2): 7450680 ⟵ “GENERAL OPERATIONS TOTAL | 7,450,680 | 7,209,455”
  - column:TOTAL REVENUE (2): 7450680 ⟵ “TOTAL REVENUE | 7,450,680 | 7,209,455”
  - column:OTHER SOURCES: 335250 ⟵ “OTHER SOURCES | 335,250 | 248,604”
  - column:STUDENT TUITION AND FEES (2): 129750 ⟵ “STUDENT TUITION AND FEES | 129,750 | 191,754”
  - column:GENERAL OPERATIONS TOTAL (3): 465000 ⟵ “GENERAL OPERATIONS TOTAL | 465,000 | 440,358”
  - column:TOTAL REVENUE (3): 465000 ⟵ “TOTAL REVENUE | 465,000 | 440,358”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 4200000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 4,200,000 | 4,200,000”
  - column:TOTAL REVENUE (4): 4200000 ⟵ “TOTAL REVENUE | 4,200,000 | 4,200,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (2): 2000000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 2,000,000 | 1,500,000”
  - column:TOTAL REVENUE (5): 2000000 ⟵ “TOTAL REVENUE | 2,000,000 | 1,500,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (3): 600000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 600,000 | 550,000”
  - column:TOTAL REVENUE (6): 600000 ⟵ “TOTAL REVENUE | 600,000 | 550,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (4): 100000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 100,000 | 85,000”
  - column:TOTAL REVENUE (7): 100000 ⟵ “TOTAL REVENUE | 100,000 | 85,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (5): 55000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 55,000 | 41,000”
  - column:TOTAL REVENUE (8): 55000 ⟵ “TOTAL REVENUE | 55,000 | 41,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (6): 90000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 90,000 | 90,000”
  - column:TOTAL REVENUE (9): 90000 ⟵ “TOTAL REVENUE | 90,000 | 90,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (7): 360000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 360,000 | 356,000”
  - column:TOTAL REVENUE (10): 360000 ⟵ “TOTAL REVENUE | 360,000 | 356,000”
  - column:OTHER SOURCES (2): 110000 ⟵ “OTHER SOURCES | 110,000 | 75,000”
  - … 8461 more rows
### `b4f21f5422b0bac7` Gordon State College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.gordonstate.edu/documents/departments/budgets/fy25-original-budget-packet.pdf (sha256 f3fbaac97b1f)
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown, conflicting_sources:https://www.gordonstate.edu/documents/departments/budgets/fy26-budget-booklet1.pdf,https://www.gordonstate.edu/documents/departments/bursars-office/coa_2627.pdf
- checks: {"columns": 11, "rows": 2570}
  - column:STATE APPROPRIATIONS: 13661761 ⟵ “STATE APPROPRIATIONS | 13,661,761 | 15,739,723”
  - column:GENERAL OPERATIONS TOTAL: 13661761 ⟵ “GENERAL OPERATIONS TOTAL | 13,661,761 | 15,739,723”
  - column:TOTAL REVENUE: 13661761 ⟵ “TOTAL REVENUE | 13,661,761 | 15,739,723”
  - column:STUDENT TUITION AND FEES: 7205493 ⟵ “STUDENT TUITION AND FEES | 7,205,493 | 7,450,680”
  - column:GENERAL OPERATIONS TOTAL (2): 7205493 ⟵ “GENERAL OPERATIONS TOTAL | 7,205,493 | 7,450,680”
  - column:TOTAL REVENUE (2): 7205493 ⟵ “TOTAL REVENUE | 7,205,493 | 7,450,680”
  - column:OTHER SOURCES: 320000 ⟵ “OTHER SOURCES | 320,000 | 335,250”
  - column:STUDENT TUITION AND FEES (2): 129750 ⟵ “STUDENT TUITION AND FEES | 129,750 | 129,750”
  - column:GENERAL OPERATIONS TOTAL (3): 449750 ⟵ “GENERAL OPERATIONS TOTAL | 449,750 | 465,000”
  - column:TOTAL REVENUE (3): 449750 ⟵ “TOTAL REVENUE | 449,750 | 465,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999): 4909806 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 4,909,806 | 4,200,000”
  - column:TOTAL REVENUE (4): 4909806 ⟵ “TOTAL REVENUE | 4,909,806 | 4,200,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (2): 1520000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 1,520,000 | 2,000,000”
  - column:TOTAL REVENUE (5): 1520000 ⟵ “TOTAL REVENUE | 1,520,000 | 2,000,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (3): 670444 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 670,444 | 600,000”
  - column:TOTAL REVENUE (6): 670444 ⟵ “TOTAL REVENUE | 670,444 | 600,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (4): 69240 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 69,240 | 100,000”
  - column:TOTAL REVENUE (7): 69240 ⟵ “TOTAL REVENUE | 69,240 | 100,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (5): 48620 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 48,620 | 55,000”
  - column:TOTAL REVENUE (8): 48620 ⟵ “TOTAL REVENUE | 48,620 | 55,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (6): 70000 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 70,000 | 90,000”
  - column:TOTAL REVENUE (9): 70000 ⟵ “TOTAL REVENUE | 70,000 | 90,000”
  - column:DEPARTMENT SALES AND SERVICES (Class 40000-43999) (7): 327270 ⟵ “DEPARTMENT SALES AND SERVICES (Class 40000-43999) | 327,270 | 360,000”
  - column:TOTAL REVENUE (10): 327270 ⟵ “TOTAL REVENUE | 327,270 | 360,000”
  - column:FUNDS FROM PRIOR YEAR: 361990 ⟵ “FUNDS FROM PRIOR YEAR | 361,990 | 0”
  - … 12164 more rows
### `dd241edaedc4125b` Helms College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.helms.edu/admissions-aid/tuition-aid/ (sha256 b53d11c4c06d)
- issues: program_specific_budget
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
- checks: {"columns": 3, "rows": 14}
  - column:Personal Computer: 582 ⟵ “Personal Computer | $582 | Per Year”
  - column:Dependent (living with parent): 40 ⟵ “Dependent (living with parent) | $40 | Per Month”
  - column:Dependent (living with parent) (2): 120 ⟵ “Dependent (living with parent) | $120 | Per Month”
  - column:Dependent (living with parent) (3): 400 ⟵ “Dependent (living with parent) | $400 | Per Month”
  - column:Dependent (living with parent) (4): 7 ⟵ “Dependent (living with parent) | $7 | Per Month”
  - column:Tuition/ On-Campus: 238 ⟵ “Tuition/ On-Campus | $238 | Per Hour”
  - column:Books & Course Materials: 179 ⟵ “Books & Course Materials | $179 | Per Class”
  - column:Tuition/ On-Campus (2): 238 ⟵ “Tuition/ On-Campus | $238 | Per Hour”
  - column:Books & Course Materials (2): 179 ⟵ “Books & Course Materials | $179 | Per Class”
  - column:Tuition/ On-Campus (3): 238 ⟵ “Tuition/ On-Campus | $238 | Per Hour”
  - column:Books & Course Materials (3): 215 ⟵ “Books & Course Materials | $215 | Per Class”
  - column:Tuition/ On-Campus (4): 238 ⟵ “Tuition/ On-Campus | $238 | Per Hour”
  - column:Books & Course Materials (4): 215 ⟵ “Books & Course Materials | $215 | Per Class”
  - column:Books & Course Materials (5): 192 ⟵ “Books & Course Materials | $192 | Per Class”
  - column:Independent/Dependent (not living with parent): 190 ⟵ “Independent/Dependent (not living with parent) | Personal/Misc. | $190 | Per Month”
  - column:Independent/Dependent (not living with parent) (2): 292 ⟵ “Independent/Dependent (not living with parent) | Transportation | $292 | Per Month”
  - column:Independent/Dependent (not living with parent) (3): 1798 ⟵ “Independent/Dependent (not living with parent) | Housing | $1,798 | Per Month”
  - column:Independent/Dependent (not living with parent) (4): 602 ⟵ “Independent/Dependent (not living with parent) | Food | $602 | Per Month”
  - column:All Students (PhD Leadership): 652 ⟵ “All Students (PhD Leadership) | Tuition | $652 | Per Hour”
  - column:All Students (PhD Christian Scripture): 468 ⟵ “All Students (PhD Christian Scripture) | Tuition | $468 | Per Hour”
  - column:All Students (PhD Leadership) (2): 317 ⟵ “All Students (PhD Leadership) | Books & Course Materials | $317 | Per Class”
  - column:All Programs: 195 ⟵ “All Programs | All Students | Fee | $195 | Per Class”
  - column:Associate: 465 ⟵ “Associate | All Students | Tuition/Distance Education | $465 | Per Hour”
  - column:Bachelor: 465 ⟵ “Bachelor | All Students | Tuition/Distance Education | $465 | Per Hour”
  - column:Master: 397 ⟵ “Master | All Students | Tuition/Distance Education | $397 | Per Hour”
  - … 2 more rows
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
  - on_campus:FY25 Tuition: 5220.0 ⟵ “FY25 Tuition | $ 5,220.00”
  - on_campus:Mandatory Fees: 862.0 ⟵ “Mandatory Fees | $ 862.00”
  - on_campus:Housing: 7618.0 ⟵ “Housing | $ 7,618.00”
  - on_campus:Food: 3800.0 ⟵ “Food | $ 3,800.00”
  - on_campus:Books: 1000.0 ⟵ “Books | $ 1,000.00”
  - on_campus:Supplies: 250.0 ⟵ “Supplies | $ 250.00”
  - on_campus:Federal Direct Loan Fees*: 78.0 ⟵ “Federal Direct Loan Fees* | $ 78.00”
  - on_campus:Miscelleneous Expenses: 3150.0 ⟵ “Miscelleneous Expenses | $ 3,150.00”
  - on_campus:Transportation: 1945.0 ⟵ “Transportation | $ 1,945.00”
  - on_campus:Total Cost of Attendance for 2 semesters: 23923.0 ⟵ “Total Cost of Attendance for 2 semesters | $ 23,923.00”
### `1c44b754e078212a` Middle Georgia State University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.mga.edu/financial-aid/cost-of-attendance.php (sha256 74752433b1bd)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:FY25 Tuition: 19410.0 ⟵ “FY25 Tuition | $ 19,410.00”
  - on_campus:Mandatory Fees: 862.0 ⟵ “Mandatory Fees | $ 862.00”
  - on_campus:Housing: 7618.0 ⟵ “Housing | $ 7,618.00”
  - on_campus:Food: 3800.0 ⟵ “Food | $ 3,800.00”
  - on_campus:Books: 1000.0 ⟵ “Books | $ 1,000.00”
  - on_campus:Supplies: 250.0 ⟵ “Supplies | $ 250.00”
  - on_campus:Federal Direct Loan Fees*: 78.0 ⟵ “Federal Direct Loan Fees* | $ 78.00”
  - on_campus:Miscelleneous Expenses: 3150.0 ⟵ “Miscelleneous Expenses | $ 3,150.00”
  - on_campus:Transportation: 3889.0 ⟵ “Transportation | $ 3,889.00”
  - on_campus:Total Cost of Attendance for 2 semesters: 40057.0 ⟵ “Total Cost of Attendance for 2 semesters | $ 40,057.00”
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
### `a25051f50fb00a07` Oconee Fall Line Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://oftc.edu/admissions/financial-aid/ (sha256 b34a33b35819)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “The financial aid administrator, under federal law, has the authority to take these special or unusual circumstances into consideration and make changes to the student’s financial aid application.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are situations that may occur that are not addressed in the application process.”
  - sentence: need_based_special_circumstances ⟵ “Some common special circumstances that may occur are: Separation from employment due to layoff, termination or disability Excessive non-reimbursed medical and/or dental expenses Reduction of untaxed income source such as child support, disability benefits, etc.”
### `ce9baef972ac375f` Oconee Fall Line Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: http://oftc.edu/admissions/financial-aid/ (sha256 ae84288f7d19)
- issues: semantic_review_required, source_not_https
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “Professional Judgment Appeal Professional judgment is the ability of a financial aid administrator to recalculate the student’s financial aid eligibility due to special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “Separation or divorce which occurred after applying for financial aid Death of parent or spouse which occurred after applying for financial aid In order to start the Professional Judgment process, a request must come from the student.”
  - sentence: professional_judgment ⟵ “Once the student has requested that Professional Judgment be performed, the student is given an OFTC Professional Judgment Appeal Form.”
  - sentence: professional_judgment ⟵ “This form has instructions and a list of documents that must be presented to the Financial Aid Office before the Professional Judgment Appeal can be completed.”
  - sentence: professional_judgment ⟵ “The student must complete and submit the FAFSA, the Verification Worksheet, tax transcripts for student and parents (if dependent), Professional Judgment Appeal Form, and documents that support the appeal.”
  - sentence: professional_judgment ⟵ “On the Professional Judgment Appeal Form, the student must provide income earned from different sources up till then and projected total income for the entire year.”
### `e2695524bf9f3ca5` Oconee Fall Line Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://oftc.edu/admissions/financial-aid/ (sha256 b34a33b35819)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If the student does not meet financial aid standards during the warning term, he/she will be placed on suspension. padding settings settings Financial Aid Appeal Process SAP (Satisfactory Academic Progress) Appeal Students must maintain a cumulative GPA of 2.0 or higher on a 4.0 scale that includes all credit courses appearing on the academic transcript.”
  - sentence: sap_appeal ⟵ “Appeals for Satisfactory Academic Progress must be based on specific extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Academic Plan Students will be given an academic plan IF the committee approves the SAP appeal.”
  - sentence: sap_appeal ⟵ “The student would need to submit another SAP Appeal to request their aid be reinstated or students can submit up to 2 SAP Appeal Forms.”
### `e5931e44fa6963cf` Oconee Fall Line Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://oftc.edu/admissions/tuition-fees/ (sha256 0c6a96004abf)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Tuition and Fees: 3380.0 ⟵ “Tuition and Fees | $3,380.00”
  - column:Food and Housing: 10953.0 ⟵ “Food and Housing | $10,953.00”
  - column:Books, Course Materials, Supplies and Equipment: 1558.0 ⟵ “Books, Course Materials, Supplies and Equipment | $1,558.00”
  - column:Transportation: 1005.0 ⟵ “Transportation | $1,005.00”
  - column:Miscellaneous Personal Expenses: 1300.0 ⟵ “Miscellaneous Personal Expenses | $1,300.00”
### `36417dc23106d305` Piedmont University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.piedmont.edu/wp-content/uploads/2026/05/Professional-Judgments-and-Special-Circumstances-Policy.pdf (sha256 19ac2ed8b5ed)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “Professional Judgment/ Special Circumstance Policy Federal regulations allow limited exceptions or adjustments to information reported on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: professional_judgment ⟵ “Such exceptions or adjustments, known as a “Professional Judgment”.”
  - sentence: professional_judgment ⟵ “Professional Judgment requests are considered on a case-by-case basis based on supporting documentation of your circumstances.”
  - sentence: professional_judgment ⟵ “Reasons to submit a Special Circumstances/ Professional Judgment request: • Changes to dependency status • Unusually high medical or dental expenses. • Family members enrolled in college at least half-time in a degree-seeking program. • Changes in a family's reported income. • Death or disability of a wage earner. • Separation/divorce of the student's parents • One-time taxable income.”
  - sentence: professional_judgment ⟵ “Preparatory coursework cannot be included) Note: An approved Professional Judgment Appeal may not result in a change to the students’ financial aid award package.”
  - sentence: professional_judgment ⟵ “To Apply for Professional Judgment/ Special Circumstance: Please send an email to finaid@piedmont.edu and include any supporting documents (with social security numbers, bank accounts, etc. redacted).”
### `3e071c9dc9fc6a8c` Piedmont University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.piedmont.edu/wp-content/uploads/2025/05/COA-2025-26.pdf (sha256 aec7f455b400)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 7, "rows": 16}
  - column:$32,760: 32760 ⟵ “$32,760 | $32,760 | $32,760 | $25,580 | $25,580 | $15,780 | $15,780”
  - column:Books, Course Materials, Supplies,: 1260 ⟵ “Books, Course Materials, Supplies, | $1,260 | $1,260 | $1,260 | 1260 | 1260 | $1,260 | $1,260”
  - column:Living Expenses (Housing & Food): 10668 ⟵ “Living Expenses (Housing & Food) | $10,668 | $7,918 | $13,800 | $10,668 | $7,918 | $10,668 | $7,918”
  - column:Transportation (average): 2000 ⟵ “Transportation (average) | $2,000 | $2,000 | $2,000 | $2,000 | 2000 | $600 | $600”
  - column:Personal/Miscellaneous: 1800 ⟵ “Personal/Miscellaneous | $1,800 | $1,800 | $1,800 | $1,800 | 1800 | $1,800 | $1,800”
  - column:Loan Fees: 96 ⟵ “Loan Fees | $96 | $96 | $96 | $96 | 96 | $96 | $96”
  - column:$48,584: 45834 ⟵ “$48,584 | $45,834 | $51,716 | $41,404 | $38,654 | $30,204 | $27,454”
  - column:Counseling: 2 ⟵ “Counseling | 2 | Education (9 hours) | 3 | Pathology (9 hours) | 3 (6 hours) | 3 | Portion (12 hours) | Direct costs would be tuition and fees.”
  - column:Tuition & Fees: 18480 ⟵ “Tuition & Fees | $18,480 | $15,780 | $21,090 | $14,610 | $14,660 | student may spend for books, course”
  - column:Books, Course Materials, Supplies, (2): 792 ⟵ “Books, Course Materials, Supplies, | $792 | materials, supplies, living expenses,”
  - column:$1,188: 1188 ⟵ “$1,188 | $1,188 | $924 | $756”
  - column:Living Expenses (Housing & Food) (2): 16002 ⟵ “Living Expenses (Housing & Food) | $16,002 | $16,002 | $16,002 | $16,002”
  - column:Transportation (average) (2): 900 ⟵ “Transportation (average) | $900 | $900 | $900 | $900 | $600”
  - column:Personal/Miscellaneous (2): 1500 ⟵ “Personal/Miscellaneous | $1,500 | $1,500 | $1,500 | $1,500 | $1,000”
  - column:Loan Fees (2): 216 ⟵ “Loan Fees | $216 | $216 | $216 | $216 | $144”
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
### `fbbb1e5a2eca77b4` Point University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://point.edu/admissions/tuition-aid/financial-aid/faq-resources (sha256 75697b308494)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If a student or parent has been laid off or terminated, the student can complete a Professional Judgment Request Form and provide proper documentation which will be reviewed for possible adjustments.”
### `5e513589775010ae` Savannah Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.savannahtech.edu/students/registrar/satisfactory-academic-progress/ (sha256 5db2117c254d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A student may appeal Financial Aid Suspension if the student has an unusual circumstance.”
### `cf057333fd75e4ca` Savannah Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.savannahtech.edu/students/registrar/satisfactory-academic-progress/ (sha256 5db2117c254d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Probation Probation is assigned if a student has received an approved SAP Appeal to reinstate financial aid.”
  - sentence: sap_appeal ⟵ “Failure to answer all questions below will result in a rejected SAP Appeal form: Extenuating circumstance(s) such as personal injury or illness, family emergency, death of a close relative, etc.”
  - sentence: sap_appeal ⟵ “Submit Appeal of Financial Aid Suspension Form/Personal Statement/Supporting Documentation Submit a completed/signed Appeal of Financial Aid Suspension form at https://savannahtech.verifymyfafsa.com Complete appeal must be submitted by the SAP Appeal deadline (see website or financial aid office for specific dates).”
### `4c617a8535f8c332` Savannah Technical College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.savannahtech.edu/tuition/tuition-outlook/ (sha256 949997953a93)
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
### `c48952769fced588` Savannah Technical College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.savannahtech.edu/tuition/tuition-outlook/ (sha256 949997953a93)
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
### `1878569f1d7bd9d7` Southern Regional Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://southernregional.edu/college-catalog/current/admissions-information (sha256 46707564122a)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Center Transfer Agreements Transcript Request Home Catalogs 2026-2027 College Catalog and Student Handbook Admissions Information Search Catalog Admissions Information Admissions Policy Southern Regional Technical College does not discriminate on the basis of race, color, creed, national or ethnic origin, gender, religion, disability, age, political affiliation or belief, disabled veteran, veteran”
### `1c4c0d9e5d84bfa7` Southern Regional Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://southernregional.edu/college-catalog/2025-2026-college-catalog/financial-aid (sha256 73b9c8f2b8be)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress requirements must be met or an appeal must be approved in order to receive aid.”
### `4c8e2bc0fea9ad2b` Southern Regional Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://southernregional.edu/college-catalog/2025-2026-college-catalog/financial-aid (sha256 73b9c8f2b8be)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://southernregional.edu/college-catalog/2025-2026-college-catalog/admissions-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals will be considered for extenuating circumstances only, which may include, but are not limited to, the death of a family member, an injury or illness of the student or their immediate family member, or other special circumstances that are generally outside of the control of the student.”
### `95578ee791d431b6` Southern Regional Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://southernregional.edu/college-catalog/2025-2026-college-catalog/admissions-information (sha256 38db6dfa113a)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://southernregional.edu/college-catalog/2025-2026-college-catalog/financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Center Transfer Agreements Transcript Request Home Catalogs 2025-2026 College Catalog and Student Handbook Admissions Information Search Catalog Admissions Information Admissions Policy Southern Regional Technical College does not discriminate on the basis of race, color, creed, national or ethnic origin, gender, religion, disability, age, political affiliation or belief, disabled veteran, veteran”
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
### `19de73b4938717b7` Thomas University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.thomasu.edu/become-a-student/admission-process/on-campus/dual-enrollment/ (sha256 c1022ea6262c)
- issues: multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 2}
  - per_credit_hour_charge: 250 ⟵ “Tuition, books and certain fees are covered for Georgia residents. Non-Georgia residents are charged the rate of $250 per credit hour for tuition.”
  - eligibility_tier: 3.0 ⟵ “GPA         3.0”
  - eligibility_tier: 3.0 ⟵ “Have at least a 3.0 GPA;”
### `42ea5e15ac8d6f9b` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php (sha256 34a725f68a5e)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `448c804100e80277` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php (sha256 0e21e25e7372)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php
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
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Click each link below to find information about each type of appeal, including steps on how to complete the appeal process: Satisfactory Academic Progress Appeal (see below) Professional Judgment: Unusual Circumstances Appeal or Professional Judgment: Special Circumstance - EFC/SAI Calculation Appeal (click here) Satisfactory Academic Progress Appeal Students who fail to meet Satisfactory Academic”
  - sentence: sap_appeal ⟵ “The student should complete a Satisfactory Academic Progress Appeal Form which is available online via our On Line Student Forms Portal.”
  - sentence: sap_appeal ⟵ “Only SAP appeals containing both required statements and documentation will be processed and evaluated.”
  - sentence: sap_appeal ⟵ “If a student’s SAP appeal is approved, and they can come into compliance within one semester, the student will be granted a one semester SAP probation and be eligible for financial aid for one semester.”
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `9652f91e67293b4a` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/sap.php (sha256 beeb1e3c9f50)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php,https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Appeal Process: Students who fail to meet Satisfactory Academic Progress (SAP) may appeal their status based on extenuating circumstances.”
  - sentence: sap_appeal ⟵ “The student should complete a Satisfactory Academic Progress Appeal Form which is available from the Office of Financial Aid web page.”
  - sentence: sap_appeal ⟵ “Only SAP appeals containing both required statements and documentation will be processed and evaluated.”
  - sentence: sap_appeal ⟵ “If a student’s SAP appeal is approved, and they can come into compliance within one semester, the student will be granted a one semester SAP probation and be eligible for financial aid for one semester.”
  - sentence: sap_appeal ⟵ “Valdosta, GA 31698 Phone: 229.333.5935 Monday-Friday 8:00am - 5:00pm Appeals Information Financial Aid Homepage How to Apply Satisfactory Academic Progress Policy Financial Aid Policies & Definitions Application Process FAQs Appeals Information Paying your Bill | Excess Aid Special Circumstances Course Program of Study Process and Policies University Center Entrances #6 & #7 Room 1400 1205 N.”
### `f3f3c2d55bf3ef7a` Valdosta State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.valdosta.edu/admissions/financial-aid/process/student-financial-aid-policies.php (sha256 7b9e42166d92)
- issues: semantic_review_required, conflicting_sources:https://www.valdosta.edu/admissions/financial-aid/process/appeals-information.php,https://www.valdosta.edu/admissions/financial-aid/process/calculator-for-sap-compliance.php,https://www.valdosta.edu/admissions/financial-aid/process/sap.php,https://www.valdosta.edu/admissions/financial-aid/process/special-circumstances-appeals.php
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
- issues: rows_without_score, score_cell_not_a_score
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

## Re-verification of existing records (56)

- all_values_found_year_not_labeled: data/institutions/abac/credit_policies/2026-27.json ["credit_policies", "ipeds-138558", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- nothing_to_check: data/institutions/agnesscott/transfer_policies/2026-27.json ["transfer_policies", "ipeds-138600", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/asurams/credit_policies/2026-27.json ["credit_policies", "ipeds-138716", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/albanytech/credit_policies/2026-27.json ["credit_policies", "ipeds-138682", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- nothing_to_check: data/institutions/athenstech/credit_policies/2026-27.json ["credit_policies", "ipeds-246813", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/atlm/credit_policies/2026-27.json ["credit_policies", "ipeds-138901", null, "2026-27", {"policy_kind": "CLEP"}]
- all_values_found_year_not_labeled: data/institutions/atlm/credit_policies/2026-27.json ["credit_policies", "ipeds-138901", null, "2026-27", {"policy_kind": "AP"}]
- all_values_found_year_not_labeled: data/institutions/atlm/credit_policies/2026-27.json ["credit_policies", "ipeds-138901", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/atlm/credit_policies/2026-27.json ["credit_policies", "ipeds-138901", null, "2026-27", {"policy_kind": "IB"}]
- all_values_found_year_not_labeled: data/institutions/augustatech/credit_policies/2026-27.json ["credit_policies", "ipeds-138956", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/augusta/credit_policies/2026-27.json ["credit_policies", "ipeds-482149", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/augusta/credit_policies/2026-27.json ["credit_policies", "ipeds-482149", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/augusta/credit_policies/2026-27.json ["credit_policies", "ipeds-482149", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/berry/credit_policies/2026-27.json ["credit_policies", "ipeds-139144", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/brenau/credit_policies/2026-27.json ["credit_policies", "ipeds-139199", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/centralgatech/credit_policies/2026-27.json ["credit_policies", "ipeds-483045", null, "2026-27", {"policy_kind": "AP"}]
- nothing_to_check: data/institutions/clayton/transfer_policies/2026-27.json ["transfer_policies", "ipeds-139311", null, "2026-27", {}]
- nothing_to_check: data/institutions/coastalpines/transfer_policies/2026-27.json ["transfer_policies", "ipeds-485458", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/ccga/credit_policies/2026-27.json ["credit_policies", "ipeds-139250", null, "2026-27", {"policy_kind": "AP"}]
- all_values_found_year_not_labeled: data/institutions/ccga/transfer_policies/2026-27.json ["transfer_policies", "ipeds-139250", null, "2026-27", {}]
- source_not_fetched: data/institutions/columbustech/credit_policies/2026-27.json ["credit_policies", "ipeds-139357", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/fvsu/credit_policies/2026-27.json ["credit_policies", "ipeds-139719", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/gcsu/credit_policies/2026-27.json ["credit_policies", "ipeds-139861", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ggc/credit_policies/2026-27.json ["credit_policies", "ipeds-447689", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/highlands/credit_policies/2026-27.json ["credit_policies", "ipeds-139700", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- values_not_found_verbatim: data/institutions/gatech/credit_policies/2026-27.json ["credit_policies", "ipeds-139755", null, "2026-27", {"policy_kind": "dual_enrollment"}] missing=['dual_enrollment.per_credit_hour_charges[0].amount', 'dual_enrollment.tuition_per_credit_hour']
- all_values_found_year_not_labeled: data/institutions/gmc/credit_policies/2026-27.json ["credit_policies", "ipeds-485111", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/gntc/credit_policies/2026-27.json ["credit_policies", "ipeds-139384", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/georgiasouthern/awards/2027-28.json ["awards", "ipeds-139931", null, "2027-28", {"award_name": "Scholarships: Calculated Admissions GPA 3.50 \u2013 3.79"}]
- source_not_fetched: data/institutions/georgiasouthern/awards/2027-28.json ["awards", "ipeds-139931", null, "2027-28", {"award_name": "Scholarships: Calculated Admissions GPA 3.80 \u2013 3.99"}]
- source_not_fetched: data/institutions/georgiasouthern/awards/2027-28.json ["awards", "ipeds-139931", null, "2027-28", {"award_name": "Scholarships: Calculated Admissions GPA 4.00 +"}]
- source_not_fetched: data/institutions/georgiasouthern/credit_policies/2026-27.json ["credit_policies", "ipeds-139931", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/georgiasouthern/transfer_policies/2026-27.json ["transfer_policies", "ipeds-139931", null, "2026-27", {}]
- source_not_fetched: data/institutions/gsw/credit_policies/2026-27.json ["credit_policies", "ipeds-139764", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/gsw/credit_policies/2026-27.json ["credit_policies", "ipeds-139764", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/gsw/credit_policies/2026-27.json ["credit_policies", "ipeds-139764", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/gsw/credit_policies/2026-27.json ["credit_policies", "ipeds-139764", null, "2026-27", {"policy_kind": "IB"}]
- all_values_found_year_not_labeled: data/institutions/gordonstate/transfer_policies/2026-27.json ["transfer_policies", "ipeds-139968", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/gupton-jones/credit_policies/2026-27.json ["credit_policies", "ipeds-139995", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/gwinnetttech/credit_policies/2026-27.json ["credit_policies", "ipeds-140012", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/gwinnetttech/credit_policies/2026-27.json ["credit_policies", "ipeds-140012", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/lagrange/transfer_policies/2026-27.json ["transfer_policies", "ipeds-140234", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/lutherrice/credit_policies/2026-27.json ["credit_policies", "ipeds-135364", null, "2026-27", {"policy_kind": "CLEP"}]
- all_values_found_year_not_labeled: data/institutions/lutherrice/credit_policies/2026-27.json ["credit_policies", "ipeds-135364", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/morehouse/transfer_policies/2026-27.json ["transfer_policies", "ipeds-140553", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/oftc/credit_policies/2026-27.json ["credit_policies", "ipeds-420431", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ogeecheetech/credit_policies/2026-27.json ["credit_policies", "ipeds-366465", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/oglethorpe/transfer_policies/2026-27.json ["transfer_policies", "ipeds-140696", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/piedmont/credit_policies/2026-27.json ["credit_policies", "ipeds-140818", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/savannahstate/credit_policies/2026-27.json ["credit_policies", "ipeds-140960", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- all_values_found_year_not_labeled: data/institutions/sgsc/credit_policies/2026-27.json ["credit_policies", "ipeds-482699", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/sctech/credit_policies/2026-27.json ["credit_policies", "ipeds-139986", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/spelman/transfer_policies/2026-27.json ["transfer_policies", "ipeds-141060", null, "2026-27", {}]
- source_not_fetched: data/institutions/ung/credit_policies/2026-27.json ["credit_policies", "ipeds-482680", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/westga/credit_policies/2026-27.json ["credit_policies", "ipeds-141334", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/wesleyancollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-141325", null, "2026-27", {}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- North Georgia Technical College (`ipeds-140678`)

## Leads: official pages found with no extracted record

- Abraham Baldwin Agricultural College: admissions_tests, merit_scholarships, ib_credit, transfer_credit, residency, degree_requirements, aid_appeals
- Agnes Scott College: cost_of_attendance, merit_scholarships, ap_credit, dual_enrollment, residency, degree_requirements
- Albany State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Albany Technical College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Andrew College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Athens Technical College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, degree_requirements
- Atlanta Metropolitan State College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Atlanta Technical College: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Augusta Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, degree_requirements
- Beulah Heights University: tuition_fees, cost_of_attendance, merit_scholarships, degree_requirements
- Central Georgia Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Chattahoochee Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- Clayton  State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Coastal Pines Technical College: tuition_fees, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements
- College of Athens: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- College of Coastal Georgia: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Dalton State College: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency
- Emory University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Emory University-Oxford College: admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Fort Valley State University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Georgia Highlands College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- Georgia Institute of Technology-Main Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency
- Georgia Military College: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Georgia Northwestern Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Georgia Piedmont Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Gordon State College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, residency, degree_requirements
- Gupton Jones College of Funeral Service: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements, aid_appeals
- Helms College: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Luther Rice College & Seminary: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Middle Georgia State University: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Morris Brown College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- Oconee Fall Line Technical College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Piedmont University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Point University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Savannah Technical College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- South Georgia State College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, transfer_credit, residency, degree_requirements, aid_appeals
- South Georgia Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Southern Regional Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements
- Thomas University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Valdosta State University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency
- West Georgia Technical College: cost_of_attendance, admissions_tests, ap_credit, statewide_articulation, residency, degree_requirements
