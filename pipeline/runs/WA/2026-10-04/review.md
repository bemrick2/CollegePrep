# Review queue — WA (2026-27)

Pages fetched: 3786; failures: 394. Candidates: 238 (45 without issues, 193 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 8 | 22 | 17 | 1 | 12 |
| cost_of_attendance | 0 | 0 | 6 | 14 | 27 | 1 | 12 |
| admissions_tests | 0 | 0 | 0 | 0 | 46 | 2 | 12 |
| common_data_set | 0 | 0 | 0 | 0 | 5 | 43 | 12 |
| merit_scholarships | 0 | 0 | 4 | 2 | 41 | 1 | 12 |
| ap_credit | 0 | 0 | 5 | 5 | 20 | 18 | 12 |
| clep_credit | 0 | 0 | 4 | 1 | 14 | 29 | 12 |
| ib_credit | 0 | 0 | 4 | 8 | 11 | 25 | 12 |
| dual_enrollment | 0 | 0 | 0 | 0 | 18 | 30 | 12 |
| transfer_credit | 0 | 0 | 8 | 2 | 36 | 2 | 12 |
| statewide_articulation | 0 | 0 | 0 | 0 | 18 | 30 | 12 |
| residency | 0 | 0 | 0 | 0 | 35 | 13 | 12 |
| degree_requirements | 0 | 0 | 0 | 0 | 36 | 12 | 12 |
| aid_appeals | 0 | 0 | 0 | 35 | 7 | 6 | 12 |

## Ready for review (45)

### `09b93219ad37cd89` Bellingham Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.btc.edu/FutureStudents/AcademicCreditforPriorLearning.html (sha256 b48f56da517a)
- checks: {"distinct_exams": 13, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL& 160 | 5”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH& 151 | 5”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MATH& 151, MATH& 152 | 5”
  - equivalencies[AP-CALCULUS-BC|5]:  ⟵ “Calculus BC | 5 | MATH& 151,MATH& 152 | 10”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM& 121, CHEM& 161 | 5”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM& 121, CHEM& 161, CHEM& 162 | 5”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics (Microeconomics) | 3 | ECON& 201 | 5”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics (Macroeconomics) | 3 | ECON& 202 | 5”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1 | 3 | Elective - Science Distribution | 5”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 | 4 | PHYS& 114 | 5”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C (Mechanics) | 3 | Elective - Science Distribution | 5”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C (Mechanics) | 4 | PHYS& 221 | 5”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish: Language & Culture | 3 | SPAN& 121 | 5”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4]:  ⟵ “Spanish: Language & Culture | 4 | SPAN& 121, SPAN& 122 | 5”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|5]:  ⟵ “Spanish: Language & Culture | 5 | SPAN& 121, SPAN& 122 | 5”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | Elective - Social Science | 5”
  - equivalencies[AP-PSYCHOLOGY|4]:  ⟵ “Psychology | 4 | PSYC& 100 | 5”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | MATH& 146 | 5”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “US Government & Politics | 3 | Elective - Social Science | 5”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “US Government & Politics | 4 | POLS& 202 | 5”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “US History | 3 | HIST& 146, HIST& 147, HIST& 148 | 5”
  - equivalencies[AP-UNITED-STATES-HISTORY|5]:  ⟵ “US History | 5 | HIST& 146, HIST& 147, HIST& 148 | 5”
### `5279807476ca8edd` Bellingham Technical College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.btc.edu/FutureStudents/AcademicCreditforPriorLearning.html (sha256 b48f56da517a)
- checks: {"distinct_exams": 9, "equivalencies": 9, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | 5 | BIOL& 160 | General Biology with Lab | ”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM& 121 or CHEM& 161 or 162 | Introduction to Chemistry | ”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | 5 | ECON 201 | Social Science Elective | ”
  - equivalencies[IB-GEOGRAPHY|5]:  ⟵ “Geography | 5 | GEOG 900 | Social Science Elective | GEOG& 100”
  - equivalencies[IB-HISTORY|5]:  ⟵ “any History | 5 | HIST& 146 | Social Science Elective | ”
  - equivalencies[IB-MUSIC|5]:  ⟵ “Music | 5 | MUSC 900 | Humanities Elective | MUSC& 105”
  - equivalencies[IB-PHILOSOPHY|5]:  ⟵ “Philosophy | 5 | PHIL 900 | Humanities Elective | ”
  - equivalencies[IB-PHYSICS|5]:  ⟵ “Physics | 5 | PHYS& 221 | Natural Science Elective | ”
  - equivalencies[IB-PSYCHOLOGY|4]:  ⟵ “Psychology | 4 | PSYC& 100 | General Psychology | ”
### `85141b8123c4cb23` Bellingham Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.btc.edu/FutureStudents/AcademicCreditforPriorLearning.html (sha256 b48f56da517a)
- checks: {"distinct_exams": 21, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT 141 | Financial Accounting I”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL& 160 | General Biology with Lab”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BUS 900 | Business Elective”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BUS 900 | Business Elective”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM& 121 or CHEM& 161 or 162 | Introduction to Chemistry or General Chemistry I w/ Lab”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MATH& 107 | Math in Society”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH& 141 | Precalculus I”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus or | 50 | MATH& 142 | Precalculus II”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH& 151 | Calculus I”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSYC& 100 | General Psychology”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSYC& 200 | Lifespan Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC& 101 | Introduction to Sociology”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 | HIST& 147 | United States History”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present | 50 | HIST 900 | Social Science Elective”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | HIST 900 | Social Science Elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | HIST 900 | Social Science Elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | HIST 900 | Social Science Elective”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | ENGL 900 | Humanities Elective”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL 900 | Humanities Elective”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | HUM 900 | Humanities Elective”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | BIOL 900 | Natural Science Elective”
### `36eb3d87a51c495e` Cascadia College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.cascadia.edu/transfer-services (sha256 1781fe62fe1d)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “For transfer purposes, a student must have a minimum grade of C or better (2.0 or above) in each course completed from this list.”
### `1667dffeb9896889` Clark College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.clark.edu/degree-certificate-requirements/transfer-overview/ (sha256 367fc32c265b)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “For transfer purposes, a student must have a minimum grade of C (2.0) or higher in each course completed from this list.”
### `7582bd65706bbc69` Columbia Basin College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.columbiabasin.edu/i-am/current-hawk/pay-for-college/financial-aid/cost-of-attendence.html (sha256 39702e90e6a4)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition & Fees: 2079 ⟵ “Tuition & Fees | $2,079 | $2,079”
  - with_parents_or_family:Books & Supplies: 176 ⟵ “Books & Supplies | $176 | $176”
  - with_parents_or_family:Housing & Food: 3148 ⟵ “Housing & Food | $3,148 | $6,086”
  - with_parents_or_family:Transportation: 860 ⟵ “Transportation | $860 | $932”
  - with_parents_or_family:Personal Expenses: 656 ⟵ “Personal Expenses | $656 | $656”
  - with_parents_or_family:Total: 6919 ⟵ “Total | $6,919 | $9,929”
### `e92b03bc77a9608c` Columbia Basin College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.columbiabasin.edu/_documents/handbooks-guides-reports-plans/ap-test-equivalencies-4-2024-accessible.pdf (sha256 9e5394b3d87c)
- checks: {"distinct_exams": 4, "equivalencies": 4, "rows_without_score": 0}
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles     4                       CS 101 (5)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A              4              CS& 141 (5) and CS 236 (5)”
  - equivalencies[AP-RESEARCH|4]:  ⟵ “Research                                                                         4                                                                                  Elective (5)”
  - equivalencies[AP-SEMINAR|4]:  ⟵ “Seminar                                                                          4                                                                                  Elective (5)”
### `03d2011067f7ec75` Columbia Basin College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.columbiabasin.edu/learn/transfer-opportunities/provisos-and-requirements.html (sha256 bb87942cc41c)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Requirements: one year of study in the same world language at the college level, and one of the three interdisciplinary Western Civilization Core courses (Core 150, Core 250, Core 350) effective fall term 2012 we will accept in transfer only courses that have a grade of “C” or higher. contact Email:advising@columbiabasin.edu Phone:509-542-5505 Address:2600 N. 20th Ave., Pasco, WA 99301 Scroll Top ”
### `7d05ac691ebc8c51` Cornish College of the Arts — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.cornish.edu/records-and-registration/transfer/ (sha256 ea5e4a529380)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer credit may be awarded for college-level, non-remedial coursework with a grade of C or better from regionally-accredited colleges or universities.”
### `e565976453eecb46` Grays Harbor College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ghc.edu/admissions/placement/college-level-examination-program-clep (sha256 d8303e9f2ed1)
- checks: {"distinct_exams": 17, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS& 202 (5) | Social Sciences”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL& 240 (5) | Humanities/Fine Arts”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL& 100 (5) | Sciences”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH& 151 (5) | Quantitative Skills”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “College French Level 1 | 50 | FRCH& 121 (5) | Humanities/Fine Arts”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “College French Level 2 | 59 | FRCH& 122 (5) | Humanities/Fine Arts”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “College German Level 1 | 50 | GERM& 121 (5) | Humanities/Fine Arts”
  - equivalencies[CLEP-GERMAN-LANGUAGE|62]:  ⟵ “College German Level 2 | 62 | GERM& 122 (5) | Humanities/Fine Arts”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “College Spanish Level 1 | 50 | SPAN& 121 (5) | Humanities/Fine Arts”
  - equivalencies[CLEP-SPANISH-LANGUAGE|62]:  ⟵ “College Spanish Level 2 | 62 | SPAN& 122 (5) | Humanities/Fine Arts”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | HIST& 146 (5) | Social Sciences”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | HIST& 167 (5) | Social Sciences”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | PSYC& 200 (5) | Social Sciences”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSYC& 100 (5) | Social Sciences”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC& 101 (5) | Social Sciences”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MATH& 141 (5) | Quantitative Skills”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECON& 202 (5) | Social Sciences”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECON& 201 (5) | Social Sciences”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | HIST& 116 (5) | Social Sciences”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present | 50 | HIST& 117 (5) | Social Sciences”
### `m33503c87cefe11b` Green River College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.greenriver.edu/international/programs/university-transfer/university-transfer-pathway/florida-institute-of-technology.html (sha256 e9a09af5140f)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “Completion of a Green River College Associate Degree that is compatible with a Florida Tech academic program or at least 45 transferable credits (grades of C- or higher) English Requirement: English&126 with a grade of 2.5 or better, IBT TOEFL 79, or IELTS 6.5 Minimum Green River Grade Point Average (GPA) is 2.5 Students with at least 45 transferable Green River College quarter credits and a min c”
  - min_grade: C- ⟵ “English Requirement:Students who complete a transferable Associate degree with 8 credits of college level writing, including ENGL 101, with grades of C- or higher, will not be required to submit TOEFL scores if their cumulative GPA is 2.5 or higher.”
### `b6f631596c93e13a` Lower Columbia College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://lowercolumbia.edu/pay-for-college/tuition/_assets/documents/26-27_COA-BAS.xlsx (sha256 d69886810268)
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - on_campus:TUITION & FEES**: 2819.72 ⟵ “TUITION & FEES** | 2819.72 | 8459.16 | 2819.72 | 8459.16 | 3703.78 | 11111.34 | 3703.78 | 11111.34”
  - on_campus:BOOKS & SUPPLIES: 254 ⟵ “BOOKS & SUPPLIES | 254 | 762 | 254 | 762 | 254 | 762 | 254 | 762”
  - on_campus:HOUSING: 4216 ⟵ “HOUSING | 1278 | 3834 | 4216 | 12648 | 1278 | 3834 | 4216 | 12648”
  - on_campus:FOOD: 1870 ⟵ “FOOD | 1870 | 5610 | 1870 | 5610 | 1870 | 5610 | 1870 | 5610”
  - on_campus:PERSONAL: 656 ⟵ “PERSONAL | 656 | 1968 | 656 | 1968 | 656 | 1968 | 656 | 1968”
  - on_campus:TRANSPORTATION: 932 ⟵ “TRANSPORTATION | 932 | 2796 | 932 | 2796 | 932 | 2796 | 932 | 2796”
  - on_campus:LOAN FEES***: 25 ⟵ “LOAN FEES*** | 25 | 75 | 25 | 75 | 25 | 75 | 25 | 75”
  - on_campus:TOTAL: 10772.72 ⟵ “TOTAL | 7834.7199999999993 | 23504.16 | 10772.72 | 32318.16 | 8718.7800000000007 | 26156.34 | 11656.78 | 34970.339999999997”
  - on_campus:TUITION & FEES**: 8459.16 ⟵ “TUITION & FEES** | 2819.72 | 8459.16 | 2819.72 | 8459.16 | 3703.78 | 11111.34 | 3703.78 | 11111.34”
  - on_campus:BOOKS & SUPPLIES: 762 ⟵ “BOOKS & SUPPLIES | 254 | 762 | 254 | 762 | 254 | 762 | 254 | 762”
  - on_campus:HOUSING: 12648 ⟵ “HOUSING | 1278 | 3834 | 4216 | 12648 | 1278 | 3834 | 4216 | 12648”
  - on_campus:FOOD: 5610 ⟵ “FOOD | 1870 | 5610 | 1870 | 5610 | 1870 | 5610 | 1870 | 5610”
  - on_campus:PERSONAL: 1968 ⟵ “PERSONAL | 656 | 1968 | 656 | 1968 | 656 | 1968 | 656 | 1968”
  - on_campus:TRANSPORTATION: 2796 ⟵ “TRANSPORTATION | 932 | 2796 | 932 | 2796 | 932 | 2796 | 932 | 2796”
  - on_campus:LOAN FEES***: 75 ⟵ “LOAN FEES*** | 25 | 75 | 25 | 75 | 25 | 75 | 25 | 75”
  - on_campus:TOTAL: 32318.16 ⟵ “TOTAL | 7834.7199999999993 | 23504.16 | 10772.72 | 32318.16 | 8718.7800000000007 | 26156.34 | 11656.78 | 34970.339999999997”
### `2e081b129eeaa116` Lower Columbia College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://lowercolumbia.edu/credit-prior-learning/alt-options/_assets/documents/ib-test-scores-course-equivalencies.pdf (sha256 ce25ec2419f0)
- checks: {"distinct_exams": 4, "equivalencies": 4, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|4]:  ⟵ “African History                       4            Distribution Credit (5)—Social Science or Humanities based on”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business & Management              4            Business or management elective (5)”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics                             4            Elective (5)”
  - equivalencies[IB-GLOBAL-POLITICS|4]:  ⟵ “Global Politics                       4            Political science elective (5)”
### `4be20401b1ccd521` Lower Columbia College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://lowercolumbia.edu/credit-prior-learning/alt-options/ap/ (sha256 7da2c23fc72d)
- checks: {"distinct_exams": 35, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art: Art History | 3 | ART& 100 (5)”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art: Studio Art - Drawing | 3 | Humanities Distribution (5)”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art: 2D Design | 3 | Humanities Distribution (5)”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art: 3D Design | 3 | Humanities Distribution (5)”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL& 100 or BIOL& 160 (5) (credit awarded will be based on requirements for degree plan)”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH& 151 (5)”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MATH& 152 (5)”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM& 161 (5) (CHEM&121 may be awarded if required for degree plan)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | CHIN& 121 (5)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | Elective (5)”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | Elective (5)”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Micro | 3 | ECON& 201 (5)”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macro | 3 | ECON& 202 (5)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVS&100 (5)”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST& 117 (5)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | Humanities/foreign language at the 100 level (5)”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture | 3 | Humanities/foreign language at the 100 level (5)”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “US Government & Politics | 3 | POLS& 202 (5)”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics | 3 | POLS& 101 (5)”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | Elective (5)”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language & Culture | 3 | Humanities/foreign language at the 100 level (5)”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language | 3 | Humanities/foreign language at the 100 level (5)”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin Literature | 3 | Humanities Distribution (5)”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Virgil | 3 | Elective (5)”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | MUSC& 141 (5)”
  - … 11 more rows
### `247f0c50d074153a` North Seattle College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://northseattle.edu/financial-aid/cost-attendance (sha256 c1152e4932d3)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and Fees*: 4935 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - on_campus:Food and Housing: 19473 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - on_campus:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - on_campus:Transportation: 3069 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - on_campus:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - on_campus:Total Expected Cost of Attendance: 29913 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `bfb2e79f130a9e7c` North Seattle College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://northseattle.edu/financial-aid/cost-attendance (sha256 c1152e4932d3)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and Fees*: 4935 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - on_campus:Food and Housing: 10072 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - on_campus:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - on_campus:Transportation: 2832 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - on_campus:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - on_campus:Total Expected Cost of Attendance: 20275 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `a71df8499aa23702` Pacific Lutheran University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.plu.edu/transfer-guide/audit/ (sha256 67eb0055ed47)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “PLU only accepts transferable courses with grades of C- (1.5) or higher.”
### `92acada832213346` Renton Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://rtc.edu/student-life/student-services/enrollment-services/transfer-to-rtc/clep-score-equivalencies.php (sha256 ed4499a1218f)
- checks: {"distinct_exams": 32, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Business | Financial Accounting | 50 | ACCT&201 | 5”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|63]:  ⟵ “Business | Financial Accounting | 63 | ACCT&201 and ACCT&202 | 10”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Business | Information Systems | 50 | BUS 900 | 5”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business | Introductory Business Law | 50 | BUS&201 | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Business | Principles of Management | 50 | BUS 180 | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Business | Principles of Marketing | 50 | BUS 130 | 5”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Composition & Literature | Analyzing and Interpreting Literature | 50 | ENGL&111 | 5”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “Composition & Literature | College Composition | 50 | ENGL&101 | 5”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Composition & Literature | Humanities | 50 | HUM&101 | 5”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “Composition & Literature | American Literature | 50 | ENGL 900 | 5”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “Composition & Literature | English Literature | 50 | ENGL 900 | 5”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Foreign Languages | Spanish Language | 50 | SPAN&121 | 5”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Foreign Languages | Spanish Language | 63 | SPAN&122 and SPAN&123 | 10”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “Foreign Languages | French Language | 50 | HUM 900 | 15”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “Foreign Languages | German Language | 50 | HUM 900 | 15”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “History & Social Sciences | American Government | 50 | POLS&202 | 5”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History & Social Sciences | History of the United States I: Early Colonization to 1877 | 50 | HIST&136 | 5”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History & Social Sciences | History of the United States II: 1865 to the Present | 50 | HIST&137 | 5”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “History & Social Sciences | Human Growth and Development | 50 | PSYC&200 | 5”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “History & Social Sciences | Introductory Psychology | 50 | PSYC&100 | 5”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “History & Social Sciences | Introductory Sociology | 50 | SOC&101 | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “History & Social Sciences | Principles of Macroeconomics | 50 | ECON&202 | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “History & Social Sciences | Principles of Microeconomics | 50 | ECON&201 | 5”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “History & Social Sciences | Introduction to Educational Psychology | 50 | PSYC 900 | 5”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History & Social Sciences | Social Sciences and History | 50 | SOC 900 | 10”
  - … 9 more rows
### `f178d10d8e9ad9b8` Saint Martin's University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.stmartin.edu/admissions-financial-aid/scholarships (sha256 30b8e258239d)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '4.0 - 3.9', 'amount_text': "$30,000 Chancellor's"}, {'gpa': '3.89 - 3.70', 'amount_text': "$29,000 President's"}, {'gpa': '3.69 - 3.45', 'amount_text': "$27,000 Dean's"}, {'gpa': '3.44 - 3.10', 'amount_text': '$26,000 Faculty'}, {'gpa': '3.09 - 2.50', 'amount_text': '$22,000 University'}] ⟵ “GPA | Scholarship award || 4.0 - 3.9 | $30,000 Chancellor's || 3.89 - 3.70 | $29,000 President's || 3.69 - 3.45 | $27,000 Dean's || 3.44 - 3.10 | $26,000 Faculty || 3.09 - 2.50 | $22,000 University”
  - gpa_requirement: Tiered by GPA: 4.0 - 3.9 → $30,000 Chancellor's; 3.89 - 3.70 → $29,000 President's; 3.69 - 3.45 → $27,000 Dean's; 3.44 - 3.10 → $26,000 Faculty; 3.09 - 2.50 → $22,000 University ⟵ “GPA | Scholarship award || 4.0 - 3.9 | $30,000 Chancellor's || 3.89 - 3.70 | $29,000 President's || 3.69 - 3.45 | $27,000 Dean's || 3.44 - 3.10 | $26,000 Faculty || 3.09 - 2.50 | $22,000 University”
### `4836de918f4427b9` Saint Martin's University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.stmartin.edu/admissions-financial-aid/undergraduate/applying-saint-martins/transfer-students-undergrad/transferring-credits (sha256 1a5d7f6c2216)
- checks: {"distinct_exams": 28, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3 or better]:  ⟵ “Art History | 3 or better | COR 240A | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3 or better]:  ⟵ “Art: 2D | 3 or better | COR 240A | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3 or better]:  ⟵ “Art: 3D | 3 or better | COR 240A | 3”
  - equivalencies[AP-DRAWING|3 or better]:  ⟵ “Art: Drawing | 3 or better | ART 295 | 3”
  - equivalencies[AP-BIOLOGY|3 or better]:  ⟵ “Biology | 3 or better | BIO 141 | 4”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “Calculus BC | 4 or 5 | MTH 171/MTH 172 | 8”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MTH 171 | 4”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Calculus AB | 4 or 5 | MTH 171 | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHM 141 | 4”
  - equivalencies[AP-CHEMISTRY|3 and 1 yr AP Chem]:  ⟵ “Chemistry | 3 and 1 yr AP Chem | CHM 141L | 1”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “Chemistry | 4 or 5 | CHM 141/CHM 142 | 8”
  - equivalencies[AP-CHEMISTRY|4 or 5 and 1 yr AP Chem]:  ⟵ “Chemistry | 4 or 5 and 1 yr AP Chem | CHM 141L/CHM 142L | 10”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3 or better]:  ⟵ “Chinese | 3 or better | COR 140C | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3 or better]:  ⟵ “Computer Science A | 3 or better | CSC180 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4 or 5]:  ⟵ “Computer Science Principles | 4 or 5 | CSC101 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4 or 5]:  ⟵ “European History | 4 or 5 | COR 250H | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 or better]:  ⟵ “French | 3 or better | COR 140F | 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3 or better]:  ⟵ “German | 3 or better | COR 140 | 4”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3 or better]:  ⟵ “Italian | 3 or better | COR 140 | 4”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3 or better]:  ⟵ “Japanese | 3 or better | COR 140 | 4”
  - equivalencies[AP-LATIN|3 or better]:  ⟵ “Latin | 3 or better | COR 140 | 4”
  - equivalencies[AP-MUSIC-THEORY|3 or better]:  ⟵ “Music Theory | 3 or better | MUS 108 | 3”
  - equivalencies[AP-PHYSICS-1|3 or better]:  ⟵ “Physics 1 | 3 or better | PHY 141 | 4”
  - equivalencies[AP-PHYSICS-2|3 or better]:  ⟵ “Physics 2 | 3 or better | PHY 142 | 4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3 or better]:  ⟵ “Physics C: Mechanics | 3 or better | PHY171 | 4”
  - … 7 more rows
### `3695c57fd55648ac` Seattle Central College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://seattlecentral.edu/enrollment-and-funding/financial-aid-and-funding/financial-aid/cost-attendance (sha256 ae6fee486add)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and Fees*: 4935 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - on_campus:Food and Housing: 19473 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - on_campus:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - on_campus:Transportation: 3069 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - on_campus:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - on_campus:Total Expected Cost of Attendance: 29913 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `d038042c4cfb0a63` Seattle Central College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://seattlecentral.edu/enrollment-and-funding/financial-aid-and-funding/financial-aid/cost-attendance (sha256 ae6fee486add)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and Fees*: 4935 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - on_campus:Food and Housing: 10072 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - on_campus:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - on_campus:Transportation: 2832 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - on_campus:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - on_campus:Total Expected Cost of Attendance: 20275 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `31f56737ceec5ac0` Seattle University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.seattleu.edu/academics/all-programs/social-work-msw/tuition-and-scholarships/ (sha256 301f3c8b9f8c)
- checks: {"thresholds": null}
  - eligibility_summary: Point in Application Cycle: A month before class starts ⟵ “A month before class starts | Etynre-Scheingold and GA”
### `b9c28d7164abcbfc` Seattle University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.seattleu.edu/academics/all-programs/social-work-msw/tuition-and-scholarships/ (sha256 301f3c8b9f8c)
- checks: {"thresholds": null}
  - eligibility_summary: Point in Application Cycle: During application process ⟵ “During application process | WAC Conditional BH scholarship”
### `d56d907a38b26124` Seattle University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.seattleu.edu/academics/all-programs/social-work-msw/tuition-and-scholarships/ (sha256 301f3c8b9f8c)
- checks: {"thresholds": null}
  - eligibility_summary: Point in Application Cycle: At admission offer ⟵ “At admission offer | SU Graduate Scholarship”
### `e3d01f7dd13d6bd4` Seattle University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.seattleu.edu/academics/all-programs/social-work-msw/tuition-and-scholarships/ (sha256 301f3c8b9f8c)
- checks: {"thresholds": null}
  - eligibility_summary: Point in Application Cycle: Upon acceptance of admission ⟵ “Upon acceptance of admission | AOCAY”
### `a19f9f68f97a6a15` South Seattle College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://southseattle.edu/financial-aid/cost-attend (sha256 78423ffdd741)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and Fees*: 4935 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - on_campus:Food and Housing: 19473 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - on_campus:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - on_campus:Transportation: 3069 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - on_campus:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - on_campus:Total Expected Cost of Attendance: 29913 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `d41c9e44ed0c0bfc` South Seattle College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://southseattle.edu/financial-aid/cost-attend (sha256 78423ffdd741)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and Fees*: 4935 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - on_campus:Food and Housing: 10072 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - on_campus:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - on_campus:Transportation: 2832 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - on_campus:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - on_campus:Total Expected Cost of Attendance: 20275 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `8aaa1bbcf3642928` Spokane Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://scc.spokane.edu/How-to-Pay-for-College/How-Much-Does-it-Cost/Annual-Cost-of-Attendance (sha256 da20bebf4276)
- checks: {"columns": 2, "rows": 6}
  - with_parents_or_family:Tuition & Fees: 7692 ⟵ “Tuition & Fees | $7,692 | $7,692”
  - with_parents_or_family:Books & Supplies: 1248 ⟵ “Books & Supplies | $1,248 | $1,248”
  - with_parents_or_family:Food & Housing: 9444 ⟵ “Food & Housing | $9,444 | $18,258”
  - with_parents_or_family:Transportation: 2580 ⟵ “Transportation | $2,580 | $2,796”
  - with_parents_or_family:Personal Expenses: 1.968 ⟵ “Personal Expenses | $1.968 | $1,968”
  - with_parents_or_family:TOTALS: 22932 ⟵ “TOTALS | $22,932 | $31,962”
  - off_campus_not_with_family:Tuition & Fees: 7692 ⟵ “Tuition & Fees | $7,692 | $7,692”
  - off_campus_not_with_family:Books & Supplies: 1248 ⟵ “Books & Supplies | $1,248 | $1,248”
  - off_campus_not_with_family:Food & Housing: 18258 ⟵ “Food & Housing | $9,444 | $18,258”
  - off_campus_not_with_family:Transportation: 2796 ⟵ “Transportation | $2,580 | $2,796”
  - off_campus_not_with_family:Personal Expenses: 1968 ⟵ “Personal Expenses | $1.968 | $1,968”
  - off_campus_not_with_family:TOTALS: 31962 ⟵ “TOTALS | $22,932 | $31,962”
### `c5e6f0df1138a266` Spokane Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://scc.spokane.edu/How-to-Pay-for-College/How-Much-Does-it-Cost/Annual-Cost-of-Attendance (sha256 da20bebf4276)
- checks: {"columns": 2, "rows": 6}
  - with_parents_or_family:Tuition & Fees: 5781 ⟵ “Tuition & Fees | $5,781 | $5,781”
  - with_parents_or_family:Books & Supplies: 1248 ⟵ “Books & Supplies | $1,248 | $1,248”
  - with_parents_or_family:Food & Housing: 9444 ⟵ “Food & Housing | $9,444 | $18,258”
  - with_parents_or_family:Transportation: 2580 ⟵ “Transportation | $2,580 | $2,796”
  - with_parents_or_family:Personal Expenses: 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - with_parents_or_family:TOTALS: 21021 ⟵ “TOTALS | $21,021 | $30,051”
  - off_campus_not_with_family:Tuition & Fees: 5781 ⟵ “Tuition & Fees | $5,781 | $5,781”
  - off_campus_not_with_family:Books & Supplies: 1248 ⟵ “Books & Supplies | $1,248 | $1,248”
  - off_campus_not_with_family:Food & Housing: 18258 ⟵ “Food & Housing | $9,444 | $18,258”
  - off_campus_not_with_family:Transportation: 2796 ⟵ “Transportation | $2,580 | $2,796”
  - off_campus_not_with_family:Personal Expenses: 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - off_campus_not_with_family:TOTALS: 30051 ⟵ “TOTALS | $21,021 | $30,051”
### `41a83eda270ce8cd` Spokane Falls Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://sfcc.spokane.edu/How-to-Pay-for-College/How-Much-Does-it-Cost/Annual-Cost-of-Attendance (sha256 f8955349d0fe)
- checks: {"columns": 2, "rows": 6}
  - with_parents_or_family:Tuition & Fees: 7692 ⟵ “Tuition & Fees | $7,692 | $7,692”
  - with_parents_or_family:Books & Supplies: 1248 ⟵ “Books & Supplies | $1,248 | $1,248”
  - with_parents_or_family:Food & Housing: 9444 ⟵ “Food & Housing | $9,444 | $18,258”
  - with_parents_or_family:Transportation: 2580 ⟵ “Transportation | $2,580 | $2,796”
  - with_parents_or_family:Personal Expenses: 1.968 ⟵ “Personal Expenses | $1.968 | $1,968”
  - with_parents_or_family:TOTALS: 22932 ⟵ “TOTALS | $22,932 | $31,962”
  - off_campus_not_with_family:Tuition & Fees: 7692 ⟵ “Tuition & Fees | $7,692 | $7,692”
  - off_campus_not_with_family:Books & Supplies: 1248 ⟵ “Books & Supplies | $1,248 | $1,248”
  - off_campus_not_with_family:Food & Housing: 18258 ⟵ “Food & Housing | $9,444 | $18,258”
  - off_campus_not_with_family:Transportation: 2796 ⟵ “Transportation | $2,580 | $2,796”
  - off_campus_not_with_family:Personal Expenses: 1968 ⟵ “Personal Expenses | $1.968 | $1,968”
  - off_campus_not_with_family:TOTALS: 31962 ⟵ “TOTALS | $22,932 | $31,962”
### `d7ea14fad34d942d` Spokane Falls Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://sfcc.spokane.edu/How-to-Pay-for-College/How-Much-Does-it-Cost/Annual-Cost-of-Attendance (sha256 f8955349d0fe)
- checks: {"columns": 2, "rows": 6}
  - with_parents_or_family:Tuition & Fees: 5781 ⟵ “Tuition & Fees | $5,781 | $5,781”
  - with_parents_or_family:Books & Supplies: 1248 ⟵ “Books & Supplies | $1,248 | $1,248”
  - with_parents_or_family:Food & Housing: 9444 ⟵ “Food & Housing | $9,444 | $18,258”
  - with_parents_or_family:Transportation: 2580 ⟵ “Transportation | $2,580 | $2,796”
  - with_parents_or_family:Personal Expenses: 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - with_parents_or_family:TOTALS: 21021 ⟵ “TOTALS | $21,021 | $30,051”
  - off_campus_not_with_family:Tuition & Fees: 5781 ⟵ “Tuition & Fees | $5,781 | $5,781”
  - off_campus_not_with_family:Books & Supplies: 1248 ⟵ “Books & Supplies | $1,248 | $1,248”
  - off_campus_not_with_family:Food & Housing: 18258 ⟵ “Food & Housing | $9,444 | $18,258”
  - off_campus_not_with_family:Transportation: 2796 ⟵ “Transportation | $2,580 | $2,796”
  - off_campus_not_with_family:Personal Expenses: 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - off_campus_not_with_family:TOTALS: 30051 ⟵ “TOTALS | $21,021 | $30,051”
### `d0ba1b7bfe2d1dfd` University of Washington-Seattle Campus — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://admit.washington.edu/apply/transfer/exams-for-credit/ap/ (sha256 6f7663289860)
- checks: {"distinct_exams": 36, "equivalencies": 74, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3,4,5]:  ⟵ “African American Studies || African American Studies | 3,4,5 | AFRAM 102 | 5 | SSc, DIV”
  - equivalencies[AP-DRAWING|3,4,5]:  ⟵ “Art: Studio Art – Drawing | 3,4,5 | ART 102 | 5 | A&H”
  - equivalencies[AP-2-D-ART-DESIGN|3,4,5]:  ⟵ “Art: Studio Art – 2D Design | 3,4,5 | ART 103 | 5 | A&H”
  - equivalencies[AP-3-D-ART-DESIGN|3,4,5]:  ⟵ “Art: Studio Art – 3D Design | 3,4,5 | ART 104 | 5 | A&H”
  - equivalencies[AP-BIOLOGY|4,5]:  ⟵ “Biology || Biology | 4,5 | BIOL 161, 162 | 5,5 | NSc”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology || Biology | 3 | BIOL 161 | 5 | NSc”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry || Chemistry | 5 | CHEM 142, 152, 162 | 5,5,5 | NSc, RSN”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry || Chemistry | 4 | CHEM 142, 152 | 5,5 | NSc, RSN”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry || Chemistry | 3 | CHEM 142 | 5 | NSc, RSN”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese || Chinese Language & Culture | 5 | CHIN 133, 231, 232 | 5,5,5 | A&H*, FL”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese || Chinese Language & Culture | 4 | CHIN 133, 231 | 5,5 | A&H*, FL”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese || Chinese Language & Culture | 3 | CHIN 133 | 5 | FL”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3,4,5]:  ⟵ “Computer Science A | 3,4,5 | CSE 121 | 4 | NSc, RSN”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3,4,5]:  ⟵ “Computer Science Principles | 3,4,5 | CSE 110 | 5 | NSc, RSN”
  - equivalencies[AP-MICROECONOMICS|4,5]:  ⟵ “Economics: Micro | 4,5 | ECON 200 | 5 | SSc, RSN”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Micro | 3 | ECON 190 | 5 | SSc”
  - equivalencies[AP-MACROECONOMICS|4,5]:  ⟵ “Economics: Macro | 4,5 | ECON 201 | 5 | SSc, RSN”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macro | 3 | ECON 191 | 5 | SSc”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3,4,5]:  ⟵ “English Language & Composition | 3,4,5 | ENGL 106 | 5 | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3,4,5]:  ⟵ “English Literature & Composition | 3,4,5 | ENGL 106 | 5 | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3,4,5]:  ⟵ “Environmental Sciences || Environmental Sciences | 3,4,5 | ESRM 100 | 5 | SSc/NSc”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French || French Language | 5 | FRENCH 201, 202, 203 | 5,5,5 | A&H, FL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French || French Language | 4 | FRENCH 201, 202 | 5,5 | A&H, FL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French || French Language | 3 | FRENCH 201 | 5 | A&H, FL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French || French Literature (exam no longer offered) | 5 | FRENCH 298 | 15 | A&H”
  - … 49 more rows
### `5c5bd984d13db097` University of Washington-Seattle Campus — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admit.washington.edu/apply/transfer/cadr/ (sha256 d72359cef384)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “The course must be completed with a grade of C (2.0) or better, even though it does not transfer to the UW as college credit and the grade earned in the course is not used in computing the Transfer GPA.”
### `4f0744228b0228f5` University of Washington-Tacoma Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.tacoma.uw.edu/admissions/international-baccalaureate-ib-credits (sha256 e9409847fbb1)
- checks: {"distinct_exams": 4, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|HL 4, 5, 6, 7]:  ⟵ “English A Language and Literature | HL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LITERATURE|HL 4, 5, 6, 7]:  ⟵ “English A Literature | HL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|SL 4, 5, 6, 7]:  ⟵ “English A Language and Literature | SL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LITERATURE|SL 4, 5, 6, 7]:  ⟵ “English A Literature | SL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|HL 6, 7]:  ⟵ “Mathematics: analysis and approaches | HL | 6, 7 | MATH 124 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|HL 4, 5]:  ⟵ “Mathematics: analysis and approaches | HL | 4, 5 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|HL 5, 6, 7]:  ⟵ “Mathematics: applications and interpretations | HL | 5, 6, 7 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|HL 4]:  ⟵ “Mathematics: applications and interpretations | HL | 4 | MATH 108 (5 CR.) | NSc”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL 6, 7]:  ⟵ “Mathematics: analysis and approaches | SL | 6, 7 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL 4, 5]:  ⟵ “Mathematics: analysis and approaches | SL | 4, 5 | MATH 109 (5 CR.) | NSc”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|SL 5, 6, 7]:  ⟵ “Mathematics: applications and interpretations | SL | 5, 6, 7 | MATH 108 (5 CR.) | NSc”
### `281371c963cea06b` Walla Walla University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wallawalla.edu/admissions-and-aid/student-financial-services/financial-aid/scholarships/freshman-scholarships (sha256 451625abd72b)
- checks: {"thresholds": null}
  - award_tiers: [{'act score': '31+', 'amount_text': '$15,000'}, {'act score': '29-30', 'amount_text': '$13,000'}, {'act score': '25-28', 'amount_text': '$11,000'}, {'act score': '24', 'amount_text': '$10,000'}, {'act score': '23', 'amount_text': '$9,000'}] ⟵ “ACT Score | Amount || 31+ | $15,000 || 29-30 | $13,000 || 25-28 | $11,000 || 24 | $10,000 || 23 | $9,000”
  - test_requirement: Tiered by ACT Score: 31+ → $15,000; 29-30 → $13,000; 25-28 → $11,000; 24 → $10,000; 23 → $9,000 ⟵ “ACT Score | Amount || 31+ | $15,000 || 29-30 | $13,000 || 25-28 | $11,000 || 24 | $10,000 || 23 | $9,000”
### `5a4e168f68f8b155` Walla Walla University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wallawalla.edu/admissions-and-aid/student-financial-services/financial-aid/scholarships/freshman-scholarships (sha256 451625abd72b)
- checks: {"thresholds": null}
  - award_tiers: [{'sat score*': '1440+', 'amount_text': '$15,000'}, {'sat score*': '1360-1430', 'amount_text': '$13,000'}, {'sat score*': '1220-1350', 'amount_text': '$11,000'}, {'sat score*': '1190-1210', 'amount_text': '$10,000'}, {'sat score*': '1150-1180', 'amount_text': '$9,000'}] ⟵ “SAT Score* | Amount || 1440+ | $15,000 || 1360-1430 | $13,000 || 1220-1350 | $11,000 || 1190-1210 | $10,000 || 1150-1180 | $9,000”
  - test_requirement: Tiered by SAT Score*: 1440+ → $15,000; 1360-1430 → $13,000; 1220-1350 → $11,000; 1190-1210 → $10,000; 1150-1180 → $9,000 ⟵ “SAT Score* | Amount || 1440+ | $15,000 || 1360-1430 | $13,000 || 1220-1350 | $11,000 || 1190-1210 | $10,000 || 1150-1180 | $9,000”
### `6668b7544eb01ca5` Walla Walla University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.wallawalla.edu/admissions-and-aid/student-financial-services/financial-aid/scholarships/freshman-scholarships (sha256 451625abd72b)
- checks: {"thresholds": null}
  - award_tiers: [{'high school gpa': '3.9-4.0', 'amount_text': '$15,000'}, {'high school gpa': '3.75-3.89', 'amount_text': '$13,000'}, {'high school gpa': '3.50-3.74', 'amount_text': '$11,000'}, {'high school gpa': '3.25-3.49', 'amount_text': '$10,000'}, {'high school gpa': '3.00-3.24', 'amount_text': '$9,000'}] ⟵ “High school GPA | Amount || 3.9-4.0 | $15,000 || 3.75-3.89 | $13,000 || 3.50-3.74 | $11,000 || 3.25-3.49 | $10,000 || 3.00-3.24 | $9,000”
  - gpa_requirement: Tiered by High school GPA: 3.9-4.0 → $15,000; 3.75-3.89 → $13,000; 3.50-3.74 → $11,000; 3.25-3.49 → $10,000; 3.00-3.24 → $9,000 ⟵ “High school GPA | Amount || 3.9-4.0 | $15,000 || 3.75-3.89 | $13,000 || 3.50-3.74 | $11,000 || 3.25-3.49 | $10,000 || 3.00-3.24 | $9,000”
### `4a637426d17ddb8e` Washington State University — awards 2026-27 [new] (source_unlabeled)
- source: https://ip.wsu.edu/future-students/tuition-fees/scholarships-funding/ (sha256 05f22d2d3c1b)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 per academic year tuition waiver ⟵ “Level 1 | $4,000 per academic year tuition waiver | Offered to students with cumulative GPA of 3.60 or higher”
  - eligibility_summary: Offered to students with cumulative GPA of 3.60 or higher ⟵ “Level 1 | $4,000 per academic year tuition waiver | Offered to students with cumulative GPA of 3.60 or higher”
### `d24dbbaf4d54feb9` Washington State University — awards 2026-27 [new] (source_unlabeled)
- source: https://ip.wsu.edu/future-students/tuition-fees/scholarships-funding/ (sha256 05f22d2d3c1b)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 per academic year tuition waiver ⟵ “Level 2 | $2,000 per academic year tuition waiver | Offered to students with cumulative GPA of 3.0 to 3.59”
  - eligibility_summary: Offered to students with cumulative GPA of 3.0 to 3.59 ⟵ “Level 2 | $2,000 per academic year tuition waiver | Offered to students with cumulative GPA of 3.0 to 3.59”
### `6c503bfb8e068049` Washington State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://admission.wsu.edu/apply/application-process/clep-credits/ (sha256 19ec659d31b0)
- checks: {"distinct_exams": 30, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | Political Science 101 | 3 | SSCI”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | History 110 | 3 | HUM”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | History 111 | 3 | HUM”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | Human Development 101 | 3 | SSCI”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psych | 50 | Psychology Elective | 3 | Not applicable”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | Psychology 105 | 3 | SSCI”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | Sociology elective | 3 | SSCI”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | Economics 102 | 3 | SSCI”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | Economics 101 | 3 | SSCI”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | History Elective | 6 | HUM, SSCI”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | History 101 | 3 | HUM”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648-Present | 50 | History 102 | 3 | HUM”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | English Elective, English 210 | 6 | HUM”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | English Elective, English 108 | 6 | HUM”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | English Elective, English 101 | 6 | WRTG”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | English Elective | 6 | Not applicable”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | English Elective | 6 | HUM”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Humanities 101, Humanities Elective | 6 | HUM”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | Biology 101, Biology Elective (no labs granted) | 6 | BSCI”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | Mathematics 171 | 4 | QUAN”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | Chemistry Elective (no lab granted) | 6 | PSCI”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | Mathematics 103 | 3 | Not applicable”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | Mathematics Elective | 6 | Not applicable”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | Biology Elective, Physical Science Elective (no labs granted) | 6 | BSCI, PSCI”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | Mathematics 106, 108 (Precalculus Sequence) | 5 | Not applicable”
  - … 5 more rows
### `b8cdbe8b41ef6f54` Washington State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admission.wsu.edu/apply/application-process/washington-45/ (sha256 cec6faf52351)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “SOME IMPORTANT NOTES For transfer purposes, a student must have a minimum grade of C or better (2.0 or above) in each course completed from this list.”
### `9062110595d1126d` Wenatchee Valley College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://wvc.edu/_resources/images/students/access/registration/prior-learning-assessment/ib-test-scores-course-equivalencies.pdf (sha256 25d99fb9f7d3)
- checks: {"distinct_exams": 16, "equivalencies": 16, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|4]:  ⟵ “African History             4        Elective (5)”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology                   4        Elective (5)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business &                4        Elective (5)”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry                 4        Elective (5)”
  - equivalencies[IB-COMPUTER-SCIENCE|4]:  ⟵ “Computer Science          4        Elective (5)”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics                 4        Elective (5)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|4]:  ⟵ “English A Literature      4        Elective (5)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4]:  ⟵ “English A Language &      4        Elective (5)”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography                 4        Elective (5)”
  - equivalencies[IB-GLOBAL-POLITICS|4]:  ⟵ “Global Politics           4        Elective (5)”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music                     4        Elective (5)”
  - equivalencies[IB-PHILOSOPHY|4]:  ⟵ “Philosophy                4        Elective (5)”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics                   4        Elective (5)”
  - equivalencies[IB-PSYCHOLOGY|4]:  ⟵ “Psychology                4        Elective (5)”
  - equivalencies[IB-THEATRE|4]:  ⟵ “Theatre                   4        Elective (5)”
  - equivalencies[IB-VISUAL-ARTS|4]:  ⟵ “Visual Arts               4        Elective (5)”
### `8e7fe8ec9e367e8c` Western Washington University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.wwu.edu/scholarships (sha256 bee33f09f7c1)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:New Student Enrollment Fee: 450 ⟵ “New Student Enrollment Fee | $450”
  - column:Tuition and Fees: 27717 ⟵ “Tuition and Fees | $27,717”
  - column:Additional Required Fees: 1449 ⟵ “Additional Required Fees | $1,449”
  - column:Housing and Meals: 16893 ⟵ “Housing and Meals | $16,893”
  - column:Books and Supplies: 1224 ⟵ “Books and Supplies | $1,224”
  - column:Transportation: 2691 ⟵ “Transportation | $2,691”
  - column:Personal and Miscellaneous: 1968 ⟵ “Personal and Miscellaneous | $1,968”
  - column:Total Cost of Attendance: 52392 ⟵ “Total Cost of Attendance | $52,392”
### `e8f79e56b012f5e7` Western Washington University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.wwu.edu/cost (sha256 7d04b325c1e7)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:New Student Enrollment Fee: 450 ⟵ “New Student Enrollment Fee | $450”
  - on_campus:Tuition and Fees: 8808 ⟵ “Tuition and Fees | $8,808”
  - on_campus:Additional Required Fees: 1449 ⟵ “Additional Required Fees | $1,449”
  - on_campus:Housing and Meals: 16893 ⟵ “Housing and Meals | $16,893”
  - on_campus:Books and Supplies: 1224 ⟵ “Books and Supplies | $1,224”
  - on_campus:Transportation: 2691 ⟵ “Transportation | $2,691”
  - on_campus:Personal and Miscellaneous: 1968 ⟵ “Personal and Miscellaneous | $1,968”
  - on_campus:Total Cost of Attendance: 33483 ⟵ “Total Cost of Attendance | $33,483”

## Exceptions (193)

### `8d74d9cd8fdc359b` Bellingham Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.btc.edu/files/Documents/Forms/StudentFinancialResources/26-27_SAP%20Policy.pdf (sha256 83a2cae45d9f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals must provide specific details regarding the unusual circumstances that prevented the student from completing their coursework and a plan for success.”
### `22c38cef4d888c87` Bellingham Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.btc.edu/CurrentStudents/FinancialResources/financialaid.html (sha256 a05a91c09238)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition & Fees: 6000 ⟵ “Tuition & Fees | $6,000”
  - column:Books & supplies: 528 ⟵ “Books & supplies | $528”
  - column:TOTAL:: 6528 ⟵ “TOTAL: | $6528”
### `831279b11c54185b` Big Bend Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bigbend.edu/unusual-special-circumstances.html (sha256 9c81dd821a4c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependent Students without Parent Support If you are a dependent student whose parents refuse to provide support, you are not eligible for a dependency override, but may be able to receive a dependent level Direct Unsubsidized Loan only.”
### `97e9cfffdcaf86f6` Big Bend Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bigbend.edu/unusual-special-circumstances.html (sha256 9c81dd821a4c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an adjustment to data elements in the COA or in the EFC or SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abuse or abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Dependency Changes / Unusual Circumstances The FAFSA Simplification Act provides clarification for Financial Aid Administrators (FAAs) to assist applicants with unusual circumstances to change dependency status on the FAFSA form to reflect students’ situations more accurately (dependency overrides).”
  - sentence: need_based_special_circumstances ⟵ “Dependency override Under HEA Sec. 480(d)(9), the FAFSA Simplification Act incorporated additional unusual circumstances to consider when you are unable to contact a parent or where contact with parents poses a risk to you.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances do include (but are not limited to): Human trafficking; Legally granted refugee or asylum status; Parental abandonment or estrangement; or Student or parental incarceration.”
### `9ac4f0f0dde4e6f7` Big Bend Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bigbend.edu/student-center/satisfactory-academic-progress-policy.html (sha256 531dad5571c6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “To appeal, please work with your academic advisor and complete the SAP Maximum Timeframe Appeal to re-instate financial aid funding.”
  - sentence: sap_appeal ⟵ “Appeal for Financial Aid Reinstatement: Financial Aid Satisfactory Academic Progress (SAP) Appeal: Suspended students can submit an appeal if they failed to make SAP due to extraordinary circumstances.”
  - sentence: sap_appeal ⟵ “All students are limited to three (3) SAP Appeals.”
### `a0909eb7e863bc1d` Big Bend Community College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.bigbend.edu/student-center/cost-of-attendance.html (sha256 fe4f7877b6e7)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "rows": 6}
  - on_campus:Tuition/Fees: 5670 ⟵ “Tuition/Fees | $5,670 | $5,670”
  - on_campus:Books/Supplies: 528 ⟵ “Books/Supplies | $528 | $528”
  - on_campus:Food/Housing: 10731 ⟵ “Food/Housing | $10,731 | $17,702”
  - on_campus:Transportation: 2790 ⟵ “Transportation | $2,790 | $2,790”
  - on_campus:Personal/Misc: 1908 ⟵ “Personal/Misc | $1,908 | $1,908”
  - on_campus:Totals: 21627 ⟵ “Totals | $21,627 | $28,598”
  - off_campus_not_with_family:Tuition/Fees: 5670 ⟵ “Tuition/Fees | $5,670 | $5,670”
  - off_campus_not_with_family:Books/Supplies: 528 ⟵ “Books/Supplies | $528 | $528”
  - off_campus_not_with_family:Food/Housing: 17702 ⟵ “Food/Housing | $10,731 | $17,702”
  - off_campus_not_with_family:Transportation: 2790 ⟵ “Transportation | $2,790 | $2,790”
  - off_campus_not_with_family:Personal/Misc: 1908 ⟵ “Personal/Misc | $1,908 | $1,908”
  - off_campus_not_with_family:Totals: 28598 ⟵ “Totals | $21,627 | $28,598”
### `e65ba65f81b73154` Big Bend Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.bigbend.edu/student-center/cost-of-attendance.html (sha256 fe4f7877b6e7)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "rows": 6}
  - on_campus:Tuition/Fees: 6255 ⟵ “Tuition/Fees | $6,255 | $6,255”
  - on_campus:Books/Supplies: 528 ⟵ “Books/Supplies | $528 | $528”
  - on_campus:Food/Housing: 10731 ⟵ “Food/Housing | $10,731 | $17,702”
  - on_campus:Transportation: 2790 ⟵ “Transportation | $2,790 | $2,790”
  - on_campus:Personal/Misc: 1908 ⟵ “Personal/Misc | $1,908 | $1,908”
  - on_campus:Totals: 22212 ⟵ “Totals | $22,212 | $29,183”
  - off_campus_not_with_family:Tuition/Fees: 6255 ⟵ “Tuition/Fees | $6,255 | $6,255”
  - off_campus_not_with_family:Books/Supplies: 528 ⟵ “Books/Supplies | $528 | $528”
  - off_campus_not_with_family:Food/Housing: 17702 ⟵ “Food/Housing | $10,731 | $17,702”
  - off_campus_not_with_family:Transportation: 2790 ⟵ “Transportation | $2,790 | $2,790”
  - off_campus_not_with_family:Personal/Misc: 1908 ⟵ “Personal/Misc | $1,908 | $1,908”
  - off_campus_not_with_family:Totals: 29183 ⟵ “Totals | $22,212 | $29,183”
### `2c1312188e1d38b9` Cascadia College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.cascadia.edu/student-resources/international-programs/future-students/default.aspx (sha256 f49180786766)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 4}
  - column:Tuition: 3881 ⟵ “Tuition | $3,881 | $11,643 | $7,260 | $21,780”
  - column:Room and Board: 3333 ⟵ “Room and Board | $3,333 | $10,000 | $3,000 | $9,000”
  - column:Other Fees*: 1119 ⟵ “Other Fees* | $1,119 | $3,357 | $1,110 | $3,331”
  - column:Total Cost of Attendance: 8333 ⟵ “Total Cost of Attendance | $8,333 | $25,000 | $11,370 | $34,111”
  - column:Tuition: 11643 ⟵ “Tuition | $3,881 | $11,643 | $7,260 | $21,780”
  - column:Room and Board: 10000 ⟵ “Room and Board | $3,333 | $10,000 | $3,000 | $9,000”
  - column:Other Fees*: 3357 ⟵ “Other Fees* | $1,119 | $3,357 | $1,110 | $3,331”
  - column:Total Cost of Attendance: 25000 ⟵ “Total Cost of Attendance | $8,333 | $25,000 | $11,370 | $34,111”
  - column:Tuition: 7260 ⟵ “Tuition | $3,881 | $11,643 | $7,260 | $21,780”
  - column:Room and Board: 3000 ⟵ “Room and Board | $3,333 | $10,000 | $3,000 | $9,000”
  - column:Other Fees*: 1110 ⟵ “Other Fees* | $1,119 | $3,357 | $1,110 | $3,331”
  - column:Total Cost of Attendance: 11370 ⟵ “Total Cost of Attendance | $8,333 | $25,000 | $11,370 | $34,111”
  - column:Tuition: 21780 ⟵ “Tuition | $3,881 | $11,643 | $7,260 | $21,780”
  - column:Room and Board: 9000 ⟵ “Room and Board | $3,333 | $10,000 | $3,000 | $9,000”
  - column:Other Fees*: 3331 ⟵ “Other Fees* | $1,119 | $3,357 | $1,110 | $3,331”
  - column:Total Cost of Attendance: 34111 ⟵ “Total Cost of Attendance | $8,333 | $25,000 | $11,370 | $34,111”
### `127e5157a7c127ff` Cascadia College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://catalog.cascadia.edu/advanced-placement-ap-credits-chart (sha256 85ab3bcd76b0)
- issues: course_column_missing, conflicting_sources:https://www.cascadia.edu/student-resources/academic-support/credit.aspx
- checks: {"distinct_exams": 32, "equivalencies": 54, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, 5]:  ⟵ “African American Studies | 3, 4, 5 | Humanities or Social Science Electives (ex: HUMAN 9XXX) (5 credits)”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “Art: Drawing | 3, 4, 5 | ART 121 (5 credits)”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “Art: 2-D or 3-D Design | 3, 4, 5 | Humanities Electives (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[AP-BIOLOGY|3, 4, 5]:  ⟵ “Biology | 3, 4, 5 | BIOL 120 (5 credits)”
  - equivalencies[AP-CALCULUS-AB|3, 4, 5]:  ⟵ “Calculus AB | 3, 4, 5 | MATH& 151 (5 credits)”
  - equivalencies[AP-CALCULUS-BC|3, 4, 5]:  ⟵ “Calculus BC | 3, 4, 5 | MATH& 151 and MATH&152 (10 credits)”
  - equivalencies[AP-CHEMISTRY|3, 4]:  ⟵ “Chemistry | 3, 4 | CHEM& 121 (5 credits) or CHEM&161 (6 credits)”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM& 121 (5 credits) or CHEM& 161 and CHEM& 162 (12 credits)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | CHIN& 121 (5 credits)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture | 4 | CHIN& 121 and CHIN& 122 (10 credits)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture | 5 | CHIN& 121, CHIN& 122, and CHIN& 123 (15 credits)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | IT-CS 115 (5 credits)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “Computer Science A | 4, 5 | IT-CS 142 (5 credits)”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | Computer Science Elective (ex: C/T 9XX) (5 credits)”
  - equivalencies[AP-MICROECONOMICS|3, 4, 5]:  ⟵ “Economics: Micro | 3, 4, 5 | ECON& 201 (5 credits)”
  - equivalencies[AP-MACROECONOMICS|3, 4, 5]:  ⟵ “Economics: Macro | 3, 4, 5 | ECON& 202 (5 credits)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition | 3 | English Elective (ex: ENGL 9XX) (5 credits)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4, 5]:  ⟵ “English Language & Composition | 4, 5 | ENGL& 101 (5 credits)”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, 5]:  ⟵ “English Literature & Composition | 3, 4, 5 | English Elective (ex: ENGL 9XX) (5 credits)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | Environmental Science Elective (ENVS 9XX) (5 credits)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4, 5]:  ⟵ “Environmental Science | 4, 5 | ENVS& 101 (5 credits)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | FRCH& 121 (5 credits)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture | 4 | FRCH& 121 and FRCH& 122 (10 credits)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | FRCH& 121, FRCH& 122, and FRCH& 123 (15 credits)”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | 3 | Language Elective (ex: LANG 9XX) (5 credits)”
  - … 29 more rows
### `4bb17cc571e15021` Cascadia College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.cascadia.edu/student-resources/academic-support/credit.aspx (sha256 de776c713d4b)
- issues: conflicting_sources:https://catalog.cascadia.edu/international-baccalaureate-ib-credit-table
- checks: {"distinct_exams": 22, "equivalencies": 42, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|4, 5, 6, 7]:  ⟵ “African History | 4, 5, 6, 7 | History Elective (ex: HIST 9XX) (5 credits)”
  - equivalencies[IB-HISTORY|4, 5, 6, 7]:  ⟵ “American History | 4, 5, 6, 7 | HIST&146 or HIST&147 or HIST&148 (5 credits)”
  - equivalencies[IB-FRENCH|4]:  ⟵ “Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish A | 4 | Humanities Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-FRENCH|5, 6, 7]:  ⟵ “Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish A | 5, 6, 7 | Humanities Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-FRENCH|4]:  ⟵ “Arabic B, Chinese B, French B, Japanese B, Russian B, Spanish B | 4 | Humanities Elective: World Language (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-FRENCH|5, 6, 7]:  ⟵ “Arabic B, Chinese B, French B, Japanese B, Russian B, Spanish B | 5, 6, 7 | Humanities Elective: World Language (ex: HUMAN 9XX) (10 credits)”
  - equivalencies[IB-BIOLOGY|4, 5, 6, 7]:  ⟵ “Biology | 4, 5, 6, 7 | Biology Elective (ex: BIOL 950) (5 credits)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4, 5, 6, 7]:  ⟵ “Business and Management | 4, 5, 6, 7 | Restricted Elective (ex: V/T 900) (5 credits)”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM& 121 (5 credits)”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM& 121 (5 credits) or CHEM& 161 (6 credits)”
  - equivalencies[IB-CHEMISTRY|6, 7]:  ⟵ “Chemistry | 6, 7 | CHEM& 121 (5 credits) or CHEM& 161 (6 credits) or CHEM& 162 (6 credits)”
  - equivalencies[IB-COMPUTER-SCIENCE|4, 5, 6, 7]:  ⟵ “Computer Science | 4, 5, 6, 7 | IT-CS 115 (5 credits)”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | 4 | Economics Elective (ECON 9XX) (5 credits)”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | 5 | ECON& 201 (5 credits)”
  - equivalencies[IB-ECONOMICS|6, 7]:  ⟵ “Economics | 6, 7 | CHEM& 121 (5 credits) or CHEM& 161 (6 credits) or CHEM& 162 (6 credits)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|4]:  ⟵ “English A Literature | 4 | Humanities Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|5, 6, 7]:  ⟵ “English A Literature | 5, 6, 7 | ENGL& 111 (5 credits)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4]:  ⟵ “English A Language & Literature | 4 | Humanities Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|5, 6, 7]:  ⟵ “English A Language & Literature | 5, 6, 7 | ENGL& 101 (5 credits)”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4, 5, 6, 7]:  ⟵ “Environmental Systems and Societies | 4, 5, 6, 7 | Natural Science Elective (5 credits)”
  - equivalencies[IB-FILM|4, 5, 6, 7]:  ⟵ “Film | 4, 5, 6, 7 | Humanities Elective (5 credits)”
  - equivalencies[IB-GEOGRAPHY|4, 5, 6, 7]:  ⟵ “Geography | 4, 5, 6, 7 | Social Science Elective (ex: SOSCI 9XX) (5 credits)”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | Political Science Elective (ex: POLS 9XX) (5 credits)”
  - equivalencies[IB-GLOBAL-POLITICS|5, 6]:  ⟵ “Global Politics | 5, 6 | MATH& 142 (5 credits)”
  - equivalencies[IB-GLOBAL-POLITICS|7]:  ⟵ “Global Politics | 7 | MATH& 151 (5 credits)”
  - … 17 more rows
### `73075251cd40dd8a` Cascadia College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.cascadia.edu/student-resources/academic-support/credit.aspx (sha256 de776c713d4b)
- issues: course_column_missing, conflicting_sources:https://catalog.cascadia.edu/advanced-placement-ap-credits-chart
- checks: {"distinct_exams": 32, "equivalencies": 54, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, 5]:  ⟵ “African American Studies | 3, 4, 5 | Humanities or Social Science Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “Art: Drawing | 3, 4, 5 | ART 121 (5 credits)”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “Art: 2-D or 3-D Design | 3, 4, 5 | Humanities Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[AP-BIOLOGY|3, 4, 5]:  ⟵ “Biology | 3, 4, 5 | BIOL 120 (5 credits)”
  - equivalencies[AP-CALCULUS-AB|3, 4, 5]:  ⟵ “Calculus AB | 3, 4, 5 | MATH& 151 (5 credits)”
  - equivalencies[AP-CALCULUS-BC|3, 4, 5]:  ⟵ “Calculus BC | 3, 4, 5 | MATH& 151 and MATH&152 (10 credits)”
  - equivalencies[AP-CHEMISTRY|3, 4]:  ⟵ “Chemistry | 3, 4 | CHEM& 121 (5 credits) or CHEM&161 (6 credits)”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM& 121 (5 credits) or CHEM& 161 and CHEM& 162 (12 credits)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | CHIN& 121(5 credits)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture | 4 | CHIN& 121 and CHIN& 122 (10 credits)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture | 5 | CHIN& 121, CHIN& 122, and CHIN& 123 (15 credits)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | IT-CS 115 (5 credits)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “Computer Science A | 4, 5 | IT-CS 142 (5 credits)”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | Computer Science Elective (ex: C/T 9XX) (5 credits)”
  - equivalencies[AP-MICROECONOMICS|3, 4, 5]:  ⟵ “Economics: Micro | 3, 4, 5 | ECON& 201 (5 credits)”
  - equivalencies[AP-MACROECONOMICS|3, 4, 5]:  ⟵ “Economics: Macro | 3, 4, 5 | ECON& 202 (5 credits)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition | 3 | English Elective (ex: ENGL 9XX) (5 credits)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4, 5]:  ⟵ “English Language & Composition | 4, 5 | ENGL& 101 (5 credits)”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, 5]:  ⟵ “English Literature & Composition | 3, 4, 5 | English Elective (ex: ENGL 9XX) (5 credits)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | Environmental Science Elective (ENVS 9XX) (5 credits)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4, 5]:  ⟵ “Environmental Science | 4, 5 | ENVS& 101 (5 credits)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | FRCH& 121 (5 credits)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture | 4 | FRCH& 121 and FRCH& 122 (10 credits)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | FRCH& 121, FRCH& 122, and FRCH& 123 (15 credits)”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | 3 | Language Elective (ex: LANG 9XX) (5 credits)”
  - … 29 more rows
### `9491ce0a1a35523a` Cascadia College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://catalog.cascadia.edu/international-baccalaureate-ib-credit-table (sha256 8157f9e57f15)
- issues: conflicting_sources:https://www.cascadia.edu/student-resources/academic-support/credit.aspx
- checks: {"distinct_exams": 22, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|4, 5, 6, 7]:  ⟵ “African History | 4, 5, 6, 7 | History Elective (ex: HIST 9XX) (5 credits)”
  - equivalencies[IB-HISTORY|4, 5, 6, 7]:  ⟵ “American History | 4, 5, 6, 7 | HIST&146 or HIST&147 or HIST&148 (5 credits)”
  - equivalencies[IB-FRENCH|5, 6, 7]:  ⟵ “Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish A | 5, 6, 7 | Humanities Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-FRENCH|5, 6]:  ⟵ “Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish A | 5, 6 | Humanities Elective: World Language (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-FRENCH|7]:  ⟵ “Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish A | 7 | Humanities Elective: World Language (ex: HUMAN 9XX) (10 credits)”
  - equivalencies[IB-BIOLOGY|4, 5, 6, 7]:  ⟵ “Biology | 4, 5, 6, 7 | Biology Elective (ex: BIOL 950) (5 credits)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4, 5, 6, 7]:  ⟵ “Business and Management | 4, 5, 6, 7 | Restricted Elective (ex: V/T 900) (5 credits)”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM& 121 (5 credits)”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM& 121 (5 credits) or CHEM& 161 (6 credits)”
  - equivalencies[IB-CHEMISTRY|6, 7]:  ⟵ “Chemistry | 6, 7 | CHEM& 121 (5 credits) or CHEM& 161 (6 credits) or CHEM& 162 (6 credits)”
  - equivalencies[IB-COMPUTER-SCIENCE|4, 5, 6, 7]:  ⟵ “Computer Science | 4, 5, 6, 7 | IT-CS 115 (5 credits)”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | 4 | Economics Elective (ex: ECON 9XX) (5 credits)”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | 5 | ECON& 201 (5 credits)”
  - equivalencies[IB-ECONOMICS|6, 7]:  ⟵ “Economics | 6, 7 | ECON& 201 and ECON& 202 (10 credits)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|4]:  ⟵ “English A Literature | 4 | Humanities Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|5, 6, 7]:  ⟵ “English A Literature | 5, 6, 7 | ENGL& 111 (5 credits)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4]:  ⟵ “English A Language & Literature | 4 | Humanities Elective (ex: HUMAN 9XX) (5 credits)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|5, 6, 7]:  ⟵ “English A Language & Literature | 5, 6, 7 | ENGL& 101 (5 credits)”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4, 5, 6, 7]:  ⟵ “Environmental Systems and Societies | 4, 5, 6, 7 | Natural Science Elective (5 credits)”
  - equivalencies[IB-FILM|4, 5, 6, 7]:  ⟵ “Film | 4, 5, 6, 7 | Humanities Elective (5 credits)”
  - equivalencies[IB-GEOGRAPHY|4, 5, 6, 7]:  ⟵ “Geography | 4, 5, 6, 7 | Social Science Elective (ex: SOSCI 9XX) (5 credits)”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | Political Science Elective (ex: POLS 9XX) (5 credits)”
  - equivalencies[IB-GLOBAL-POLITICS|5, 6]:  ⟵ “Global Politics | 5, 6 | MATH& 142 (5 credits)”
  - equivalencies[IB-GLOBAL-POLITICS|7]:  ⟵ “Global Politics | 7 | MATH& 151 (5 credits)”
  - equivalencies[IB-GLOBAL-POLITICS|5, 6, 7]:  ⟵ “Global Politics | 5, 6, 7 | MATH& 151 (5 credits)”
  - … 16 more rows
### `ff45987d330dd5d9` Centralia College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.centralia.edu/funding/cost/annual-cost.aspx (sha256 0795b2372069)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - on_campus:Total: 19428 ⟵ “Total | $19,428 | $28,185”
  - on_campus:Tuition & Fees (estimate)*: 5265 ⟵ “Tuition & Fees (estimate)* | $5,265 | $5,265”
  - on_campus:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528”
  - on_campus:Food & Housing: 9153 ⟵ “Food & Housing | $9,153 | $17,694”
  - on_campus:Transportation: 2574 ⟵ “Transportation | $2,574 | $2,790”
  - on_campus:Miscellaneous/Personal: 1908 ⟵ “Miscellaneous/Personal | $1,908 | $1,908”
  - on_campus:Total: 28185 ⟵ “Total | $19,428 | $28,185”
  - on_campus:Tuition & Fees (estimate)*: 5265 ⟵ “Tuition & Fees (estimate)* | $5,265 | $5,265”
  - on_campus:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528”
  - on_campus:Food & Housing: 17694 ⟵ “Food & Housing | $9,153 | $17,694”
  - on_campus:Transportation: 2790 ⟵ “Transportation | $2,574 | $2,790”
  - on_campus:Miscellaneous/Personal: 1908 ⟵ “Miscellaneous/Personal | $1,908 | $1,908”
### `d6f08d279ec116f8` City University of Seattle — appeals 2024-25 [new] (labeled_in_source)
- source: https://cityu.edu/admissions-us/financial-aid/ (sha256 c6e1e4a35395)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Though the processor uses a standard formula to determine a family’s student aid index, CityU can consider unusual or special circumstances when evaluating your eligibility for aid.”
  - sentence: need_based_special_circumstances ⟵ “If you feel you have an unusual circumstance such as extraordinary medical expenses, recent unemployment or a direct educational expense not reflected in your COA, please contact your Financial Aid Counselor.”
  - sentence: need_based_special_circumstances ⟵ “Special and/or Unusual Circumstances Appeal Students may contact the CityU Student Financial Services Office to request an adjustment based on special or unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to financial situations (e.g., loss of a job, reduction in pay, additional expenses outside of the standard cost of attendance, etc.) that justify an aid administrator adjusting data elements in the student’s cost of attendance or in their SAI (student aid index) calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abuse or abandonment, incarceration), more commonly referred to as a dependency override.”
### `2052911722d24ce4` Clark College — appeals 2026-27 [new] (labeled_in_url)
- source: https://www.clark.edu/enroll/paying-for-college/financial-aid/documents/2026-27-sap-policy.pdf (sha256 d55989f5c099)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “In cases of students’ illness, injury, a death in the family, or other unusual circumstances, students may appeal to regain financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Typed and signed personal statement explaining the unusual circumstances, what has changed, and the steps taken to ensure academic success in the future 3.”
  - sentence: need_based_special_circumstances ⟵ “Typed and signed personal statement explaining the unusual circumstances that resulted in not meeting SAP, what has changed, and the steps taken to ensure academic success in the future, as well as the reason for needing additional credits to complete the program of study 3.”
### `7ffd1fa4c30f1bca` Clark College — appeals 2026-27 [new] (labeled_in_url)
- source: https://www.clark.edu/enroll/paying-for-college/financial-aid/documents/2026-27-sap-policy.pdf (sha256 d55989f5c099)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Failure to maintain good academic standing may be the result of circumstances beyond the student’s control.”
  - sentence: sap_appeal ⟵ “Students are limited to two (2) SAP appeals at Clark College.”
  - sentence: sap_appeal ⟵ “A current academic advisement report completed and signed by the student and program advisor Maximum Timeframe and SAP Suspension Appeal When students are suspended from financial aid due to reaching 150% of credits required for their program and failure to meet the cumulative GPA and/or pace of progression requirements, there is an option to file an appeal to address both issues: The appeal must ”
### `947fdd464b04e181` Clark College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.clark.edu/enroll/paying-for-college/documents/Cost_of_Attendance.pdf (sha256 4e6a544167cc)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "rows": 28}
  - column:Tuition & Fees: 5187 ⟵ “Tuition & Fees | $5,187 | $5,187”
  - column:Loan Fees: 58 ⟵ “Loan Fees | $58 | $58”
  - column:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528”
  - column:Food & Housing: 9444 ⟵ “Food & Housing | $9,444 | $18,258”
  - column:Transportation: 2580 ⟵ “Transportation | $2,580 | $2,796”
  - column:Personal Expenses: 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - column:TOTALS: 19765 ⟵ “TOTALS | $19,765 | $28,795”
  - column:Tuition & Fees (2): 11535 ⟵ “Tuition & Fees | $11,535 | $11,535”
  - column:Loan Fees (2): 58 ⟵ “Loan Fees | $58 | $58”
  - column:Books & Supplies (2): 528 ⟵ “Books & Supplies | $528 | $528”
  - column:Food & Housing (2): 9444 ⟵ “Food & Housing | $9,444 | $18,258”
  - column:Transportation (2): 2580 ⟵ “Transportation | $2,580 | $2,896”
  - column:Personal Expenses (2): 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - column:TOTALS (2): 26113 ⟵ “TOTALS | $26,113 | $35,243”
  - column:Tuition & Fees (3): 8130 ⟵ “Tuition & Fees | $8,130 | $8,130”
  - column:Loan Fees (3): 58 ⟵ “Loan Fees | $58 | $58”
  - column:Books & Supplies (3): 528 ⟵ “Books & Supplies | $528 | $528”
  - column:Food & Housing (3): 9444 ⟵ “Food & Housing | $9,444 | $18,258”
  - column:Transportation (3): 2580 ⟵ “Transportation | $2,580 | $2,796”
  - column:Personal Expenses (3): 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - column:TOTALS (3): 22708 ⟵ “TOTALS | $22,708 | $31,738”
  - column:Tuition & Fees (4): 22032 ⟵ “Tuition & Fees | $22,032 | $22,032”
  - column:Loan Fees (4): 58 ⟵ “Loan Fees | $58 | $58”
  - column:Books & Supplies (4): 528 ⟵ “Books & Supplies | $528 | $528”
  - column:Food & Housing (4): 9444 ⟵ “Food & Housing | $9,444 | $18,258”
  - … 31 more rows
### `0ef03dec1d924aad` Clover Park Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cptc.edu/financial-aid/forms (sha256 ee936df56389)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “INDEP AGGREGATE VERIFICATION WORKSHEET.pdf Professional Judgment (PJ): 26-27 Special Circumstance_Professional Judgment.pdf 2025-2026 CPTC Financial aid Forms Copied!”
### `35a84433173d8ea5` Clover Park Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cptc.edu/financial-aid/satisfactory-academic-progress-requirements (sha256 11a5d924f00b)
- issues: semantic_review_required, conflicting_sources:https://www.cptc.edu/financial-aid/forms,https://www.cptc.edu/sites/default/files/26-27%20Satisfactory%20Academic%20Progress%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “AFTER your grades have been posted for the quarter, you must notify the Student Aid & Scholarships Office that you earned reinstatement by submitting a Satisfactory Academic Progress appeal form.”
### `e619eea19e3d0658` Clover Park Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cptc.edu/financial-aid/forms (sha256 ee936df56389)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.cptc.edu/financial-aid/satisfactory-academic-progress-requirements,https://www.cptc.edu/sites/default/files/26-27%20Satisfactory%20Academic%20Progress%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Copy a link to this accordion panel 26-27 Institutional Form.pdf 26-27 Award Revision Request Form.pdf 26-27 Direct Loan Worksheet.pdf 26-27 Dependency Override.pdf 26-27 Request for Credits Additional Timeframe Appeal.pdf 26-27 CPTC Consortium Agreement.pdf 26-27 Satisfactory Academic Progress Appeal Form.pdf Selected Verification Forms: 26-27 V1.”
  - sentence: sap_appeal ⟵ “Copy a link to this accordion panel 25-26 Consortium Agreement.docx 25-26 Dependency Override.docx 25-26 Federal Direct Loan Worksheet.docx 25-26 Institutional form.docx 25-26 Request for Credits appeal.docx 25-26 Request to Revise Financial Aid Award.docx 25-26 SAP Appeal Form.docx Click above and you will find a selection of forms that may need to be submitted as part of your financial aid proce”
### `e6fe128baa3cf783` Clover Park Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cptc.edu/sites/default/files/26-27%20Satisfactory%20Academic%20Progress%20Appeal%20Form.pdf (sha256 af6e72987cbf)
- issues: semantic_review_required, conflicting_sources:https://www.cptc.edu/financial-aid/forms,https://www.cptc.edu/financial-aid/satisfactory-academic-progress-requirements
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “SW Bldg 17, Room 130 Lakewood, WA 98499-4004 Phone: 253.589.5660 Email: finaid@cptc.edu School Code: 015984 STUDENT AID & SCHOLARSHIPS Satisfactory Academic Progress Suspension Appeal You have been suspended from financial aid because you did not successfully complete the required number of credits AND/OR your GPA did not meet requirements.”
  - sentence: sap_appeal ⟵ “All of the following must be completed and attached at time of submission, otherwise your suspension appeal will be considered incomplete: 1) The Satisfactory Academic Progress Suspension Appeal form 2) Supporting documentation from another source such as a letter from clergy, doctor, teacher, or medical bills/records, or police/insurance report on official letterhead and with all appropriate sign”
  - sentence: sap_appeal ⟵ “Repayments are not waived when a Satisfactory Academic Progress appeal is approved. 4) Incomplete grades do not count toward credits completed for financial aid purposes.”
  - sentence: sap_appeal ⟵ “SW Bldg. 17, Room 130 Lakewood, WA 98499-4004 Phone: 253.589.5660 Email: finaid@cptc.edu School Code: 015984 STUDENT AID & SCHOLARSHIPS Satisfactory Academic Progress Suspension Appeal **Appeals with no supporting documentation will be denied.”
  - sentence: sap_appeal ⟵ “I have fully read, understand, and agree to all aspects of the Satisfactory Academic Progress Appeal as stated above, including that regardless of the decision of my appeal request I am ultimately responsible for paying my tuition and fees due to Clover Park Technical College.”
  - sentence: sap_appeal ⟵ “STUDENT AID & SCHOLARSHIPS Satisfactory Academic Progress Suspension Appeal For Office Use Only: Action taken on appeal: ( ) Approved _________________________________________________________________ ( ) Denied ____________________________________________________________________ Signature of Financial Aid Officer________________________________ Date _____________________ NOTES: Appeal Denied  Gen”
### `ffeaf4a2d4cb33e4` Clover Park Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cptc.edu/sites/default/files/26-27%20Satisfactory%20Academic%20Progress%20Appeal%20Form.pdf (sha256 af6e72987cbf)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you feel that this was the result of unusual circumstances beyond your control, you may appeal your suspension status.”
  - sentence: need_based_special_circumstances ⟵ “Some examples of unusual circumstances may include, but are not limited to: death in immediate family, hospitalization/serious illness which required doctor’s care, or disasters. **If you had a previous appeal approved, any subsequent appeal(s) will be held to a higher standard and will be subject to tighter scrutiny.”
### `9c10259924569488` Clover Park Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cptc.edu/tuition (sha256 df344b7c6c12)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - column:Tuition: 5091 ⟵ “Tuition | $5,091 | $5,091 | $5,091”
  - column:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528 | $528”
  - column:Housing: 3834 ⟵ “Housing | $3,834 | $12,648 | $12,648”
  - column:Food: 5610 ⟵ “Food | $5,610 | $5,610 | $5,610”
  - column:Transportation: 2580 ⟵ “Transportation | $2,580 | $2,796 | $2,796”
  - column:Personal: 1968 ⟵ “Personal | $1,968 | $1,968 | $1,968”
  - column:Loan Fees: 72 ⟵ “Loan Fees | $72 | $72 | $72”
  - column:Total: 19683 ⟵ “Total | $19,683 | $28,713 | $28,713”
  - with_parents_or_family:Tuition: 5091 ⟵ “Tuition | $5,091 | $5,091 | $5,091”
  - with_parents_or_family:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528 | $528”
  - with_parents_or_family:Housing: 12648 ⟵ “Housing | $3,834 | $12,648 | $12,648”
  - with_parents_or_family:Food: 5610 ⟵ “Food | $5,610 | $5,610 | $5,610”
  - with_parents_or_family:Transportation: 2796 ⟵ “Transportation | $2,580 | $2,796 | $2,796”
  - with_parents_or_family:Personal: 1968 ⟵ “Personal | $1,968 | $1,968 | $1,968”
  - with_parents_or_family:Loan Fees: 72 ⟵ “Loan Fees | $72 | $72 | $72”
  - with_parents_or_family:Total: 28713 ⟵ “Total | $19,683 | $28,713 | $28,713”
  - off_campus_not_with_family:Tuition: 5091 ⟵ “Tuition | $5,091 | $5,091 | $5,091”
  - off_campus_not_with_family:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528 | $528”
  - off_campus_not_with_family:Housing: 12648 ⟵ “Housing | $3,834 | $12,648 | $12,648”
  - off_campus_not_with_family:Food: 5610 ⟵ “Food | $5,610 | $5,610 | $5,610”
  - off_campus_not_with_family:Transportation: 2796 ⟵ “Transportation | $2,580 | $2,796 | $2,796”
  - off_campus_not_with_family:Personal: 1968 ⟵ “Personal | $1,968 | $1,968 | $1,968”
  - off_campus_not_with_family:Loan Fees: 72 ⟵ “Loan Fees | $72 | $72 | $72”
  - off_campus_not_with_family:Total: 28713 ⟵ “Total | $19,683 | $28,713 | $28,713”
### `49f38ca875a046cd` Columbia Basin College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.columbiabasin.edu/financialaid (sha256 0bb086e83126)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If your or your family’s (for dependent students) financial situation has changed, you may be eligible to submit a Special Circumstances petition for your aid to be reviewed for possible adjustments.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances include loss or change of employment, divorce, death in the family, etc.”
### `5ad7707c143a0761` Columbia Basin College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.columbiabasin.edu/i-am/current-hawk/pay-for-college/financial-aid/cost-of-attendence.html (sha256 39702e90e6a4)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 6}
  - with_parents_or_family:Tuition & Fees: 2803 ⟵ “Tuition & Fees | $2,803 | $2,803”
  - with_parents_or_family:Books & Supplies: 176 ⟵ “Books & Supplies | $176 | $176”
  - with_parents_or_family:Housing & Food: 3418 ⟵ “Housing & Food | $3,418 | $6,086”
  - with_parents_or_family:Transportation: 860 ⟵ “Transportation | $860 | $932”
  - with_parents_or_family:Personal Expenses: 656 ⟵ “Personal Expenses | $656 | $656”
  - with_parents_or_family:Total: 7643 ⟵ “Total | $7,643 | $10,653”
  - column:Tuition & Fees: 2803 ⟵ “Tuition & Fees | $2,803 | $2,803”
  - column:Books & Supplies: 176 ⟵ “Books & Supplies | $176 | $176”
  - column:Housing & Food: 6086 ⟵ “Housing & Food | $3,418 | $6,086”
  - column:Transportation: 932 ⟵ “Transportation | $860 | $932”
  - column:Personal Expenses: 656 ⟵ “Personal Expenses | $656 | $656”
  - column:Total: 10653 ⟵ “Total | $7,643 | $10,653”
### `8d9b4811d2e78d93` Columbia Basin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.columbiabasin.edu/i-am/current-hawk/pay-for-college/financial-aid/cost-of-attendence.html (sha256 39702e90e6a4)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition & Fees: 2079 ⟵ “Tuition & Fees | $2,079 | $2,079”
  - column:Books & Supplies: 176 ⟵ “Books & Supplies | $176 | $176”
  - column:Housing & Food: 6086 ⟵ “Housing & Food | $3,148 | $6,086”
  - column:Transportation: 932 ⟵ “Transportation | $860 | $932”
  - column:Personal Expenses: 656 ⟵ “Personal Expenses | $656 | $656”
  - column:Total: 9929 ⟵ “Total | $6,919 | $9,929”
### `130b0c4de439a14e` Cornish College of the Arts — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cornish.edu/tuition-financial-aid/faq/ (sha256 87d0fc9ad4cb)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “This is commonly referred to as a dependency override.”
### `714f76cfe367fdf0` Cornish College of the Arts — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cornish.edu/wp-content/uploads/2025/03/PJ-25-26.pdf (sha256 e6a8f8485865)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “This form is for those students and families with a special circumstance who may qualify for a reevaluation of financial aid.”
  - sentence: need_based_special_circumstances ⟵ “Submitting this form does NOT guarantee a change in financial aid.”
### `77397be59b63d6a5` Cornish College of the Arts — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cornish.edu/wp-content/uploads/2025/03/PJ-25-26.pdf (sha256 e6a8f8485865)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Professional Judgment Review Form 2025–2026 Name: Student ID#: Student Email: | p: 206.726.5063 | f: 206.726.5109 | e: finaid@cornish.edu What is a Professional Judgment Review?”
  - sentence: professional_judgment ⟵ “A Special Circumstances/Professional Judgment Review is a justifiable and documented request for recalculation of your Student Aid Index (SAI) from the FAFSA, or your student budget, based on unusual or extenuating circumstances not reflected in your original FAFSA submission.”
  - sentence: professional_judgment ⟵ “We cannot process a Professional Judgment Review without required documentation.”
  - sentence: professional_judgment ⟵ “I understand that any false or misleading statement will be cause for denial of a Professional Judgment Review or a reduction of my financial aid award and could re- sult in my owing a repayment of my financial aid.”
### `99a307feb98e04c8` Cornish College of the Arts — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cornish.edu/tuition-financial-aid/faq/ (sha256 87d0fc9ad4cb)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: professional_judgment ⟵ “Professional Judgment Review Professional Judgment Review Financial aid is calculated based on information submitted on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: professional_judgment ⟵ “Your parent contributors refuse to contribute to your college expenses Your parent contributors refuse to supply the necessary information for FAFSA or FAFSA verification completion You parent contributors don’t claim you as a dependent for federal tax filing You demonstration complete financial self-sufficiency Students may apply for either one of these Professional Judgments or both.”
  - sentence: professional_judgment ⟵ “A Professional Judgment Form is for those students who have experienced an unusual or extenuating circumstance warranting a reevaluation of financial aid.”
  - sentence: professional_judgment ⟵ “Submitting a Professional Judgment Form does not guarantee a change in aid.”
  - sentence: professional_judgment ⟵ “You will be notified by email within 7 business days of when the Professional Judgment form was received and if any additional information is needed.”
  - sentence: professional_judgment ⟵ “You will be notified by a financial aid administrator regarding the outcome of your Professional Judgment form.”
### `afbbb134f4b80045` Cornish College of the Arts — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cornish.edu/tuition-financial-aid/faq/ (sha256 87d0fc9ad4cb)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “You will want to respond to the email sent to you if you lose eligibility and fill out the SAP appeal form explaining your situation and your plan to return to meeting standards, along with documentation, if applicable, to explain the mitigating circumstances that caused you to fall below minimum standards.”
### `c1c3605dc9787c81` Cornish College of the Arts — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cornish.edu/tuition-financial-aid/faq/ (sha256 87d0fc9ad4cb)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A Special Circumstance may include: Parent contributor’s change in employment status Significant reduction in income or benefits Outstanding medical expenses not covered by insuranceDeath in the family Cornish also recognizes that an individual may experience Unusual Circumstances, where the financial aid administrator can make an adjustment to the student’s dependency status.”
### `5662c016712cb6a9` Everett Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.everettcc.edu/paying-for-college/tuition-and-fees/ (sha256 d812f2df94e4)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition and Fees: 4935 ⟵ “Tuition and Fees | $4,935 | $11,283”
  - off_campus_not_with_family:Books and Supplies: 528 ⟵ “Books and Supplies | $528 | $528”
  - off_campus_not_with_family:Housing and Food: 18498 ⟵ “Housing and Food | $18,498 | $18,498”
  - off_campus_not_with_family:Transportation: 1710 ⟵ “Transportation | $1,710 | $1,710”
  - off_campus_not_with_family:Personal Expenses: 1908 ⟵ “Personal Expenses | $1,908 | $1,908”
  - off_campus_not_with_family:Total: 27579 ⟵ “Total | $27,579 | $33,927”
### `93cd08a60cd9a33e` Everett Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.everettcc.edu/paying-for-college/tuition-and-fees/ (sha256 d812f2df94e4)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition and Fees: 11283 ⟵ “Tuition and Fees | $4,935 | $11,283”
  - off_campus_not_with_family:Books and Supplies: 528 ⟵ “Books and Supplies | $528 | $528”
  - off_campus_not_with_family:Housing and Food: 18498 ⟵ “Housing and Food | $18,498 | $18,498”
  - off_campus_not_with_family:Transportation: 1710 ⟵ “Transportation | $1,710 | $1,710”
  - off_campus_not_with_family:Personal Expenses: 1908 ⟵ “Personal Expenses | $1,908 | $1,908”
  - off_campus_not_with_family:Total: 33927 ⟵ “Total | $27,579 | $33,927”
### `4b70a927b121cf0d` Grays Harbor College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.ghc.edu/wp-content/uploads/2026/07/GHC-FA-SAP-POLICY-2026-2027.pdf (sha256 b02240b22281)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Appeal Students placed on Financial Aid Suspension or who have reached the Maximum Timeframe may submit an appeal if they failed to make satisfactory academic progress due to an extraordinary circumstance or those beyond the student’s control.”
  - sentence: sap_appeal ⟵ “Students are limited to submitting three (3) non-consecutive Satisfactory Academic Progress Appeals regardless of program changes.”
### `5c7ee1a558442be6` Grays Harbor College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.ghc.edu/wp-content/uploads/2026/02/2025-26-SAP-Handbook.pdf (sha256 3765bd3cd227)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Appeal Students placed on Financial Aid Suspension or who have reached the Maximum Timeframe may submit an appeal if they failed to make satisfactory academic progress due to an extraordinary circumstance or those beyond the student’s control.”
  - sentence: sap_appeal ⟵ “Students are limited to submitting three (3) non-consecutive Satisfactory Academic Progress Appeals regardless of program changes.”
### `bb16d86f0d8926ce` Grays Harbor College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ghc.edu/financialaid/cost-attendance (sha256 d92f0f47dbb5)
- issues: residency_unknown
- checks: {"columns": 2, "rows": 5}
  - with_parents_or_family:Tuition & Fees: 5778 ⟵ “Tuition & Fees | 5778 | 5778”
  - with_parents_or_family:Books: 525 ⟵ “Books | 525 | 528”
  - with_parents_or_family:Room & Board: 9444 ⟵ “Room & Board | 9444 | 18258”
  - with_parents_or_family:Transportation: 2580 ⟵ “Transportation | 2580 | 2796”
  - with_parents_or_family:Personal: 1968 ⟵ “Personal | 1968 | 1968”
  - with_parents_or_family:Tuition & Fees: 5778 ⟵ “Tuition & Fees | 5778 | 5778”
  - with_parents_or_family:Books: 528 ⟵ “Books | 525 | 528”
  - with_parents_or_family:Room & Board: 18258 ⟵ “Room & Board | 9444 | 18258”
  - with_parents_or_family:Transportation: 2796 ⟵ “Transportation | 2580 | 2796”
  - with_parents_or_family:Personal: 1968 ⟵ “Personal | 1968 | 1968”
### `48baf18bc455437d` Great Northern University — appeals 2026-27 [new] (source_unlabeled)
- source: https://gnu.edu/admissions/financial-aid/ (sha256 29651ed02588)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “In addition, if you have any special circumstances you would like us to know about, you can fill out and submit this Special Circumstances Review form and/or Unusual Circumstances Review form.”
### `c14970d715dabf50` Lower Columbia College — appeals 2026-27 [new] (source_unlabeled)
- source: https://lowercolumbia.edu/pay-for-college/financial-aid/maintain-eligibility/ (sha256 7c3b2abb1c95)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “When a student is suspended and the appeal is approved, the student will be sent a communication with the terms of their SAP appeal.”
### `496a55a3b54113e4` Lower Columbia College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://lowercolumbia.edu/pay-for-college/tuition/_assets/documents/26-27_COA-BAS.xlsx (sha256 d69886810268)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - column:TUITION & FEES**: 2819.72 ⟵ “TUITION & FEES** | 2819.72 | 8459.16 | 2819.72 | 8459.16 | 3703.78 | 11111.34 | 3703.78 | 11111.34”
  - column:BOOKS & SUPPLIES: 254 ⟵ “BOOKS & SUPPLIES | 254 | 762 | 254 | 762 | 254 | 762 | 254 | 762”
  - column:HOUSING: 1278 ⟵ “HOUSING | 1278 | 3834 | 4216 | 12648 | 1278 | 3834 | 4216 | 12648”
  - column:FOOD: 1870 ⟵ “FOOD | 1870 | 5610 | 1870 | 5610 | 1870 | 5610 | 1870 | 5610”
  - column:PERSONAL: 656 ⟵ “PERSONAL | 656 | 1968 | 656 | 1968 | 656 | 1968 | 656 | 1968”
  - column:TRANSPORTATION: 932 ⟵ “TRANSPORTATION | 932 | 2796 | 932 | 2796 | 932 | 2796 | 932 | 2796”
  - column:LOAN FEES***: 25 ⟵ “LOAN FEES*** | 25 | 75 | 25 | 75 | 25 | 75 | 25 | 75”
  - column:TOTAL: 7834.719999999999 ⟵ “TOTAL | 7834.7199999999993 | 23504.16 | 10772.72 | 32318.16 | 8718.7800000000007 | 26156.34 | 11656.78 | 34970.339999999997”
  - column:TUITION & FEES**: 8459.16 ⟵ “TUITION & FEES** | 2819.72 | 8459.16 | 2819.72 | 8459.16 | 3703.78 | 11111.34 | 3703.78 | 11111.34”
  - column:BOOKS & SUPPLIES: 762 ⟵ “BOOKS & SUPPLIES | 254 | 762 | 254 | 762 | 254 | 762 | 254 | 762”
  - column:HOUSING: 3834 ⟵ “HOUSING | 1278 | 3834 | 4216 | 12648 | 1278 | 3834 | 4216 | 12648”
  - column:FOOD: 5610 ⟵ “FOOD | 1870 | 5610 | 1870 | 5610 | 1870 | 5610 | 1870 | 5610”
  - column:PERSONAL: 1968 ⟵ “PERSONAL | 656 | 1968 | 656 | 1968 | 656 | 1968 | 656 | 1968”
  - column:TRANSPORTATION: 2796 ⟵ “TRANSPORTATION | 932 | 2796 | 932 | 2796 | 932 | 2796 | 932 | 2796”
  - column:LOAN FEES***: 75 ⟵ “LOAN FEES*** | 25 | 75 | 25 | 75 | 25 | 75 | 25 | 75”
  - column:TOTAL: 23504.16 ⟵ “TOTAL | 7834.7199999999993 | 23504.16 | 10772.72 | 32318.16 | 8718.7800000000007 | 26156.34 | 11656.78 | 34970.339999999997”
### `d96a4e09e17b7f5a` Lower Columbia College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://lowercolumbia.edu/pay-for-college/tuition/_assets/documents/24-25_COA-BAS.pdf (sha256 9cc554280c73)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://lowercolumbia.edu/pay-for-college/tuition/_assets/documents/26-27_COA-BAS.xlsx
- checks: {"columns": 8, "components_reconcile": true, "rows": 8}
  - column:TUITION & FEES**: 2642 ⟵ “TUITION & FEES** | $2,642 | $7,925 | $2,642 | $7,925 | $3,470 | $10,410 | $3,470 | $10,410”
  - column:BOOKS & SUPPLIES: 254 ⟵ “BOOKS & SUPPLIES | $254 | $762 | $254 | $762 | $254 | $762 | $254 | $762”
  - column:HOUSING: 1200 ⟵ “HOUSING | $1,200 | $3,600 | $3,994 | $11,982 | $1,200 | $3,600 | $3,994 | $11,982”
  - column:FOOD: 1776 ⟵ “FOOD | $1,776 | $5,328 | $1,776 | $5,328 | $1,776 | $5,328 | $1,776 | $5,328”
  - column:PERSONAL: 616 ⟵ “PERSONAL | $616 | $1,848 | $616 | $1,848 | $616 | $1,848 | $616 | $1,848”
  - column:TRANSPORTATION: 892 ⟵ “TRANSPORTATION | $892 | $2,676 | $966 | $2,898 | $892 | $2,676 | $966 | $2,898”
  - column:LOAN FEES***: 25 ⟵ “LOAN FEES*** | $25 | $75 | $25 | $75 | $25 | $75 | $25 | $75”
  - column:TOTAL: 7405 ⟵ “TOTAL | $7,405 | $22,214 | $10,273 | $30,818 | $8,233 | $24,699 | $11,101 | $33,303”
  - column:TUITION & FEES**: 7925 ⟵ “TUITION & FEES** | $2,642 | $7,925 | $2,642 | $7,925 | $3,470 | $10,410 | $3,470 | $10,410”
  - column:BOOKS & SUPPLIES: 762 ⟵ “BOOKS & SUPPLIES | $254 | $762 | $254 | $762 | $254 | $762 | $254 | $762”
  - column:HOUSING: 3600 ⟵ “HOUSING | $1,200 | $3,600 | $3,994 | $11,982 | $1,200 | $3,600 | $3,994 | $11,982”
  - column:FOOD: 5328 ⟵ “FOOD | $1,776 | $5,328 | $1,776 | $5,328 | $1,776 | $5,328 | $1,776 | $5,328”
  - column:PERSONAL: 1848 ⟵ “PERSONAL | $616 | $1,848 | $616 | $1,848 | $616 | $1,848 | $616 | $1,848”
  - column:TRANSPORTATION: 2676 ⟵ “TRANSPORTATION | $892 | $2,676 | $966 | $2,898 | $892 | $2,676 | $966 | $2,898”
  - column:LOAN FEES***: 75 ⟵ “LOAN FEES*** | $25 | $75 | $25 | $75 | $25 | $75 | $25 | $75”
  - column:TOTAL: 22214 ⟵ “TOTAL | $7,405 | $22,214 | $10,273 | $30,818 | $8,233 | $24,699 | $11,101 | $33,303”
  - column:TUITION & FEES**: 2642 ⟵ “TUITION & FEES** | $2,642 | $7,925 | $2,642 | $7,925 | $3,470 | $10,410 | $3,470 | $10,410”
  - column:BOOKS & SUPPLIES: 254 ⟵ “BOOKS & SUPPLIES | $254 | $762 | $254 | $762 | $254 | $762 | $254 | $762”
  - column:HOUSING: 3994 ⟵ “HOUSING | $1,200 | $3,600 | $3,994 | $11,982 | $1,200 | $3,600 | $3,994 | $11,982”
  - column:FOOD: 1776 ⟵ “FOOD | $1,776 | $5,328 | $1,776 | $5,328 | $1,776 | $5,328 | $1,776 | $5,328”
  - column:PERSONAL: 616 ⟵ “PERSONAL | $616 | $1,848 | $616 | $1,848 | $616 | $1,848 | $616 | $1,848”
  - column:TRANSPORTATION: 966 ⟵ “TRANSPORTATION | $892 | $2,676 | $966 | $2,898 | $892 | $2,676 | $966 | $2,898”
  - column:LOAN FEES***: 25 ⟵ “LOAN FEES*** | $25 | $75 | $25 | $75 | $25 | $75 | $25 | $75”
  - column:TOTAL: 10273 ⟵ “TOTAL | $7,405 | $22,214 | $10,273 | $30,818 | $8,233 | $24,699 | $11,101 | $33,303”
  - column:TUITION & FEES**: 7925 ⟵ “TUITION & FEES** | $2,642 | $7,925 | $2,642 | $7,925 | $3,470 | $10,410 | $3,470 | $10,410”
  - … 39 more rows
### `eeb83f2f645459a6` Lower Columbia College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://lowercolumbia.edu/pay-for-college/tuition/_assets/documents/26-27_COA-BAS.xlsx (sha256 d69886810268)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://lowercolumbia.edu/pay-for-college/tuition/_assets/documents/24-25_COA-BAS.pdf
- checks: {"columns": 4, "components_reconcile": true, "rows": 8}
  - column:TUITION & FEES**: 3703.78 ⟵ “TUITION & FEES** | 2819.72 | 8459.16 | 2819.72 | 8459.16 | 3703.78 | 11111.34 | 3703.78 | 11111.34”
  - column:BOOKS & SUPPLIES: 254 ⟵ “BOOKS & SUPPLIES | 254 | 762 | 254 | 762 | 254 | 762 | 254 | 762”
  - column:HOUSING: 1278 ⟵ “HOUSING | 1278 | 3834 | 4216 | 12648 | 1278 | 3834 | 4216 | 12648”
  - column:FOOD: 1870 ⟵ “FOOD | 1870 | 5610 | 1870 | 5610 | 1870 | 5610 | 1870 | 5610”
  - column:PERSONAL: 656 ⟵ “PERSONAL | 656 | 1968 | 656 | 1968 | 656 | 1968 | 656 | 1968”
  - column:TRANSPORTATION: 932 ⟵ “TRANSPORTATION | 932 | 2796 | 932 | 2796 | 932 | 2796 | 932 | 2796”
  - column:LOAN FEES***: 25 ⟵ “LOAN FEES*** | 25 | 75 | 25 | 75 | 25 | 75 | 25 | 75”
  - column:TOTAL: 8718.78 ⟵ “TOTAL | 7834.7199999999993 | 23504.16 | 10772.72 | 32318.16 | 8718.7800000000007 | 26156.34 | 11656.78 | 34970.339999999997”
  - column:TUITION & FEES**: 11111.34 ⟵ “TUITION & FEES** | 2819.72 | 8459.16 | 2819.72 | 8459.16 | 3703.78 | 11111.34 | 3703.78 | 11111.34”
  - column:BOOKS & SUPPLIES: 762 ⟵ “BOOKS & SUPPLIES | 254 | 762 | 254 | 762 | 254 | 762 | 254 | 762”
  - column:HOUSING: 3834 ⟵ “HOUSING | 1278 | 3834 | 4216 | 12648 | 1278 | 3834 | 4216 | 12648”
  - column:FOOD: 5610 ⟵ “FOOD | 1870 | 5610 | 1870 | 5610 | 1870 | 5610 | 1870 | 5610”
  - column:PERSONAL: 1968 ⟵ “PERSONAL | 656 | 1968 | 656 | 1968 | 656 | 1968 | 656 | 1968”
  - column:TRANSPORTATION: 2796 ⟵ “TRANSPORTATION | 932 | 2796 | 932 | 2796 | 932 | 2796 | 932 | 2796”
  - column:LOAN FEES***: 75 ⟵ “LOAN FEES*** | 25 | 75 | 25 | 75 | 25 | 75 | 25 | 75”
  - column:TOTAL: 26156.34 ⟵ “TOTAL | 7834.7199999999993 | 23504.16 | 10772.72 | 32318.16 | 8718.7800000000007 | 26156.34 | 11656.78 | 34970.339999999997”
  - column:TUITION & FEES**: 3703.78 ⟵ “TUITION & FEES** | 2819.72 | 8459.16 | 2819.72 | 8459.16 | 3703.78 | 11111.34 | 3703.78 | 11111.34”
  - column:BOOKS & SUPPLIES: 254 ⟵ “BOOKS & SUPPLIES | 254 | 762 | 254 | 762 | 254 | 762 | 254 | 762”
  - column:HOUSING: 4216 ⟵ “HOUSING | 1278 | 3834 | 4216 | 12648 | 1278 | 3834 | 4216 | 12648”
  - column:FOOD: 1870 ⟵ “FOOD | 1870 | 5610 | 1870 | 5610 | 1870 | 5610 | 1870 | 5610”
  - column:PERSONAL: 656 ⟵ “PERSONAL | 656 | 1968 | 656 | 1968 | 656 | 1968 | 656 | 1968”
  - column:TRANSPORTATION: 932 ⟵ “TRANSPORTATION | 932 | 2796 | 932 | 2796 | 932 | 2796 | 932 | 2796”
  - column:LOAN FEES***: 25 ⟵ “LOAN FEES*** | 25 | 75 | 25 | 75 | 25 | 75 | 25 | 75”
  - column:TOTAL: 11656.78 ⟵ “TOTAL | 7834.7199999999993 | 23504.16 | 10772.72 | 32318.16 | 8718.7800000000007 | 26156.34 | 11656.78 | 34970.339999999997”
  - column:TUITION & FEES**: 11111.34 ⟵ “TUITION & FEES** | 2819.72 | 8459.16 | 2819.72 | 8459.16 | 3703.78 | 11111.34 | 3703.78 | 11111.34”
  - … 7 more rows
### `a52f572bfb890c40` North Seattle College — appeals 2026-27 [new] (labeled_in_source)
- source: https://northseattle.edu/financial-aid (sha256 62b96b72e394)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Get Your Funding Back If your financial aid has been cancelled for not meeting Satisfactory Academic Progress (SAP), you may appeal to reinstate your aid.”
### `cdd1394435058780` North Seattle College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://northseattle.edu/financial-aid/cost-attendance (sha256 c1152e4932d3)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees*: 5520 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - column:Food and Housing: 19473 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - column:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - column:Transportation: 3069 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - column:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - column:Total Expected Cost of Attendance: 30498 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
  - column:Tuition and Fees*: 5520 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - column:Food and Housing: 10072 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - column:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - column:Transportation: 2832 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - column:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - column:Total Expected Cost of Attendance: 20860 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `2e2b0b2c43054101` Northwest Indian College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.nwic.edu/student-life/northwest-indian-college-financial-aid/ (sha256 79a59ba2e206)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “If a budget adjustment is needed, please complete a Budget Modification Request available on JICS under Financial Aid.”
### `3133e1b45e096496` Northwest Indian College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.nwic.edu/student-life/northwest-indian-college-financial-aid/ (sha256 79a59ba2e206)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students who have more than two successive quarters of non satisfactory academic progress or have already received an approved appeal in their NWIC career may not appeal and must successfully complete a quarter of at least 6 credits on their own.”
### `da771c27e161f4ed` Northwest School of Wooden Boat Building — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://nwswb.edu/tuition-fees/ (sha256 b1d9ebdac8a9)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - column:Tuition & Instructional Materials Fees: 27800 ⟵ “Tuition & Instructional Materials Fees | $27,800 | $23,850 | $1,450 | ”
  - column:Tools, Books, Supplies: 1700 ⟵ “Tools, Books, Supplies | $1,700 | $2,000 | Not applicable”
  - column:Housing/Food: 25960 ⟵ “Housing/Food | $25,960 | $19,470 | Not applicable”
  - column:Transportation: 4092 ⟵ “Transportation | $4,092 | $3, 069 | Not applicable”
  - column:Miscellaneous & Personal: 2544 ⟵ “Miscellaneous & Personal | $2,544 | $1,908 | Not applicable”
  - column:Estimated Total Cost of Attendance: 62096 ⟵ “Estimated Total Cost of Attendance | $62,096 | $50,297 | $1,450”
  - column:Tuition & Instructional Materials Fees: 23850 ⟵ “Tuition & Instructional Materials Fees | $27,800 | $23,850 | $1,450 | ”
  - column:Tools, Books, Supplies: 2000 ⟵ “Tools, Books, Supplies | $1,700 | $2,000 | Not applicable”
  - column:Housing/Food: 19470 ⟵ “Housing/Food | $25,960 | $19,470 | Not applicable”
  - column:Miscellaneous & Personal: 1908 ⟵ “Miscellaneous & Personal | $2,544 | $1,908 | Not applicable”
  - column:Estimated Total Cost of Attendance: 50297 ⟵ “Estimated Total Cost of Attendance | $62,096 | $50,297 | $1,450”
  - column:Tuition & Instructional Materials Fees: 1450 ⟵ “Tuition & Instructional Materials Fees | $27,800 | $23,850 | $1,450 | ”
  - column:Estimated Total Cost of Attendance: 1450 ⟵ “Estimated Total Cost of Attendance | $62,096 | $50,297 | $1,450”
### `700703f97fa868d6` Northwest University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.northwestu.edu/financial-aid-undergraduate/gpa-credit-requirements (sha256 e68e15bfc1cb)
- issues: ambiguous_year_labels, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Appeals, Financial Aid Probation, and Academic Plans The Financial Aid Administrator has the ability to use professional judgment to reinstate state aid on a case-by-case basis due to extenuating circumstances.”
### `1ac3825be0d87302` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 3.00-3.24 ⟵ “3.00-3.24 | $10,000/yr”
  - award_amount_text: $10,000/yr ⟵ “3.00-3.24 | $10,000/yr”
### `224b1b6e85ddc8d7` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 3.50-3.74 ⟵ “3.50-3.74 | $14,000/yr”
  - award_amount_text: $14,000/yr ⟵ “3.50-3.74 | $14,000/yr”
### `4b6a8d8c43ad6d8f` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “Top 10 placement at National competition | $3,000”
### `572b9c4d5a004d40` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “National participation | $2,000”
### `8e8c7219967bc6a8` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “Award of Merit (National) | $5,000”
### `aec236c11a65f6fd` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 3.75-3.99 ⟵ “3.75-3.99 | $16,000/yr”
  - award_amount_text: $16,000/yr ⟵ “3.75-3.99 | $16,000/yr”
### `b9236762b6bb527e` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Regional or District participation | $1,000”
### `c3592574e16ab8ed` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,000 (category that does not relate to an NU degree or program) ⟵ “Excellent or higher (National) | $2,000 (category that does not relate to an NU degree or program)”
### `dcd01ba901b6bc3a` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 4.0 ⟵ “4.0 | $18,000/yr”
  - award_amount_text: $18,000/yr ⟵ “4.0 | $18,000/yr”
### `e5a03926dce74149` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Superior (District or Regional) | $1,000”
### `e95b401c07dd795a` Northwest University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 3.25-3.49 ⟵ “3.25-3.49 | $12,000/yr”
  - award_amount_text: $12,000/yr ⟵ “3.25-3.49 | $12,000/yr”
### `397a60175952b915` Northwest University — transfer_policies 2027-28 [new] (labeled_in_source)
- source: https://www.northwestu.edu/admissions/transfer-students (sha256 afad0b011b10)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Official transfer credit is determined after admission and receipt of all required official transcripts. **All transfer courses must be completed with a grade of C- or above.”
  - min_grade: C- ⟵ “California: Associate Degree Transfer (ADT) with Associate of Arts (AA-T) or Associate of Science (AS-T) from California community colleges. *All transfer courses must be completed with a grade of C- or above.”
### `80aeea914b4e2ed1` Northwest University-Center for Online and Extended Education — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.northwestu.edu/financial-aid-undergraduate/gpa-credit-requirements (sha256 e68e15bfc1cb)
- issues: ambiguous_year_labels, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Appeals, Financial Aid Probation, and Academic Plans The Financial Aid Administrator has the ability to use professional judgment to reinstate state aid on a case-by-case basis due to extenuating circumstances.”
### `33cafb6d8db532b5` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 3.25-3.49 ⟵ “3.25-3.49 | $12,000/yr”
  - award_amount_text: $12,000/yr ⟵ “3.25-3.49 | $12,000/yr”
### `4a708525b68e7c20` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Superior (District or Regional) | $1,000”
### `6c20f98fa34dd3d7` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 4.0 ⟵ “4.0 | $18,000/yr”
  - award_amount_text: $18,000/yr ⟵ “4.0 | $18,000/yr”
### `73cc70555960d176` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 3.50-3.74 ⟵ “3.50-3.74 | $14,000/yr”
  - award_amount_text: $14,000/yr ⟵ “3.50-3.74 | $14,000/yr”
### `74d76db05c2541e9` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Regional or District participation | $1,000”
### `7d5ff5cd8798a172` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “Award of Merit (National) | $5,000”
### `9c61741e312736ae` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 3.00-3.24 ⟵ “3.00-3.24 | $10,000/yr”
  - award_amount_text: $10,000/yr ⟵ “3.00-3.24 | $10,000/yr”
### `a55b7acc61a21dd2` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “National participation | $2,000”
### `ac0d8ad1f97ca84d` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,000 (category that does not relate to an NU degree or program) ⟵ “Excellent or higher (National) | $2,000 (category that does not relate to an NU degree or program)”
### `c986c5dbd3bd297e` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “Top 10 placement at National competition | $3,000”
### `d440edf314fc4c01` Northwest University-Center for Online and Extended Education — awards 2027-28 [new] (labeled_in_title)
- source: https://www.northwestu.edu/financial-aid-undergraduate/scholarships (sha256 31406cc225ce)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative High School Grade Point Average (Unweighted): 3.75-3.99 ⟵ “3.75-3.99 | $16,000/yr”
  - award_amount_text: $16,000/yr ⟵ “3.75-3.99 | $16,000/yr”
### `ad6f0f1c8be4fdbf` Northwest University-Center for Online and Extended Education — transfer_policies 2027-28 [new] (labeled_in_source)
- source: https://www.northwestu.edu/admissions/transfer-students (sha256 c1498b7336a5)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Official transfer credit is determined after admission and receipt of all required official transcripts. **All transfer courses must be completed with a grade of C- or above.”
  - min_grade: C- ⟵ “California: Associate Degree Transfer (ADT) with Associate of Arts (AA-T) or Associate of Science (AS-T) from California community colleges. *All transfer courses must be completed with a grade of C- or above.”
### `4b83375e945a4fe0` Olympic College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.olympic.edu:443/fund-your-education/financial-aid (sha256 8f6443d16693)
- issues: semantic_review_required, conflicting_sources:https://www.olympic.edu:443/fund-your-education/financial-aid/financial-aid-policies-procedures/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP can be appealed for continued financial aid eligibility beyond normal limits.”
### `8f9ffe4d5935aadc` Olympic College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.olympic.edu:443/fund-your-education/financial-aid/financial-aid-policies-procedures/satisfactory-academic-progress (sha256 2e0499601ce8)
- issues: semantic_review_required, conflicting_sources:https://www.olympic.edu:443/fund-your-education/financial-aid
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “To regain eligibility, students must: Submit an SAP appeal explaining the extenuating circumstances that affected academic performance and provide supporting documentation.”
  - sentence: sap_appeal ⟵ “Financial Aid APPEALS Students who do not meet SAP may appeal the loss of their eligibility by submitting a request to the financial aid office.”
### `d0fd9ddd9ef0ee87` Olympic College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.olympic.edu:443/fund-your-education/financial-aid (sha256 8f6443d16693)
- issues: residency_unknown
- checks: {"columns": 2, "rows": 8}
  - with_parents_or_family:Tuition and Fees: 5092 ⟵ “Tuition and Fees | $5,092 | $5,092”
  - with_parents_or_family:Books and Supplies: 528 ⟵ “Books and Supplies | $528 | $528”
  - with_parents_or_family:Housing: 3834 ⟵ “Housing | $3,834 | $12,648”
  - with_parents_or_family:Food: 5610 ⟵ “Food | $5,610 | $5,610”
  - with_parents_or_family:Personal Expenses: 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - with_parents_or_family:Transportation: 2580 ⟵ “Transportation | $2,580 | $2,796”
  - with_parents_or_family:Loan Fees**: 58 ⟵ “Loan Fees** | $58 | $58”
  - with_parents_or_family:TOTALS:: 19670 ⟵ “TOTALS: | $19,670 | $28,700”
  - off_campus_not_with_family:Tuition and Fees: 5092 ⟵ “Tuition and Fees | $5,092 | $5,092”
  - off_campus_not_with_family:Books and Supplies: 528 ⟵ “Books and Supplies | $528 | $528”
  - off_campus_not_with_family:Housing: 12648 ⟵ “Housing | $3,834 | $12,648”
  - off_campus_not_with_family:Food: 5610 ⟵ “Food | $5,610 | $5,610”
  - off_campus_not_with_family:Personal Expenses: 1968 ⟵ “Personal Expenses | $1,968 | $1,968”
  - off_campus_not_with_family:Transportation: 2796 ⟵ “Transportation | $2,580 | $2,796”
  - off_campus_not_with_family:Loan Fees**: 58 ⟵ “Loan Fees** | $58 | $58”
  - off_campus_not_with_family:TOTALS:: 28700 ⟵ “TOTALS: | $19,670 | $28,700”
### `205e433924380899` Olympic College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.olympic.edu/student-life-support/enrollment-services/transfer-students/transfer-olympic-college/transfer (sha256 2f3047533a24)
- issues: credits_implausible
- checks: {"distinct_exams": 38, "equivalencies": 61, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3-5]:  ⟵ “African American Studies | 3-5 | 5 | HUMAN 925 | Humanities / Social Science”
  - equivalencies[AP-ART-HISTORY|3 - 5]:  ⟵ “Art History | 3 - 5 | 5 | ART&100 | Humanities”
  - equivalencies[AP-DRAWING|3 - 5]:  ⟵ “Art Studio: Drawing | 3 - 5 | 5 | ART 920 | Humanities”
  - equivalencies[AP-2-D-ART-DESIGN|3 - 5]:  ⟵ “Art: 2D Design | 3 - 5 | 5 | ART 920 | Humanities”
  - equivalencies[AP-3-D-ART-DESIGN|3 - 5]:  ⟵ “Art: 3D Design | 3 - 5 | 5 | ART 920 | Humanities”
  - equivalencies[AP-BIOLOGY|3 - 5]:  ⟵ “Biology | 3 - 5 | 5 | BIOL&160 | Natural Science w/ Lab”
  - equivalencies[AP-CALCULUS-AB|3 - 5]:  ⟵ “Calculus AB | 3 - 5 | 5 | MATH&151 | Quantitative Skills / Natural Science”
  - equivalencies[AP-CALCULUS-BC|3 - 5]:  ⟵ “Calculus BC | 3 - 5 | 10 | MATH&151 (5), MATH&152 (5) | Quantitative Skills / Natural Science”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 12.5 | CHEM&121 (6), CHEM&141 (5), CHEM&151 (1.5 | Natural Science w/ Lab”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 19 | CHEM&121 (6), CHEM&141 (5), CHEM&151 (1.5), CHEM&142 (5), CHEM&152 (1.5) | Natural Science w/ Lab”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | 25 | CHEM&121 (6), CHEM&141 (5), CHEM&151 (1.5), CHEM&142 (5), CHEM&152 (1.5), CHEM&143 (3), CHEM&153 (3) | Natural Science w/ Lab”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3 - 4]:  ⟵ “Chinese Language & Culture | 3 - 4 | 5 | FLANG 920 | Humanities (World Language)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture | 5 | 10 | FLANG 920 | Humanities (World Language)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3-5]:  ⟵ “Computer Science A | 3-5 | 5 | CS&141 | Natural Science”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3-5]:  ⟵ “Computer Science Principles | 3-5 | 5 | CS 940 | Natural Science”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition | 3 | 5 | ENGL 900 | Academic Elective”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Language & Composition | 4-5 | 5 | ENGL&101 | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition | 3 | 5 | ENGL 920 | Humanities”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Composition | 4-5 | 5 | ENGL&101 or ENGL&111 | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 5 | ENVS 940 | Natural Science”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science | 4-5 | 5 | ENVS&101 | Natural Science”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 5 | HIST&116 | Social Science”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | 10 | HIST&116 (5), HIST&117 (5) | Social Science”
  - equivalencies[AP-EUROPEAN-HISTORY|5]:  ⟵ “European History | 5 | 15 | HIST&116 (5), HIST&117 (5), HIST&118 (5) | Social Science”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | 5 | FRCH&121 | Humanities (World Language)”
  - … 36 more rows
### `368140220e56f489` Olympic College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.olympic.edu/student-life-support/enrollment-services/transfer-students/transfer-olympic-college/transfer (sha256 2f3047533a24)
- issues: credits_implausible, score_column_not_scores
- checks: {"distinct_exams": 24, "equivalencies": 44, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|African History]:  ⟵ “African History | 4 - 7 | 5 | HIST 925 | Social Science / Humanities”
  - equivalencies[IB-HISTORY|American History]:  ⟵ “American History | 4 - 7 | 10 | HIST&136 (5), HIST&137 (5) | Social Science”
  - equivalencies[IB-FRENCH|Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish A]:  ⟵ “Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish A | 5 - 7 | 5 | HUMAN 920 | Humanities”
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | 4 - 7 | 5 | BIOL&160 | Natural Science w/ Lab”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business Management]:  ⟵ “Business Management | 4 - 7 | 5 | BMGMT 800 | Restricted Elective”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 4 | 6 | CHEM&121 | Natural Science w/ Lab”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 5 | 12.5 | CHEM&121 (6), CHEM&141 (5), CHEM&151 (1.5) | Natural Science w/ Lab”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 6 | 19 | CHEM&121 (6), CHEM&141 (5), CHEM&151 (1.5), CHEM&142 (5), CHEM&152 (1.5) | Natural Science w/ Lab”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 7 | 25 | CHEM&121 (6), CHEM&141 (5), CHEM&151 (1.5), CHEM&142 (5), CHEM&152 (1.5), CHEM&143 (3), CHEM&153 (3) | Natural Science w/ Lab”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | 4 - 7 | 5 | CS&141 | Natural Science”
  - equivalencies[IB-HISTORY|East/Southeast Asia and Oceania History]:  ⟵ “East/Southeast Asia and Oceania History | 4 - 7 | 5 | HIST 925 | Social Science / Humanities”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | 4 | 5 | ECON 900 | Academic Elective”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | 5 | 5 | ECON&201 | Social Science”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | 6 - 7 | 10 | ECON&201 (5), ECON&202 (5) | Social Science”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|English A Language & Literature]:  ⟵ “English A Language & Literature | 4 | 5 | ENGL 920 | Humanities”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|English A Language & Literature]:  ⟵ “English A Language & Literature | 5 - 7 | 5 | ENGL&101 | ”
  - equivalencies[IB-ENGLISH-A-LITERATURE|English A Literature]:  ⟵ “English A Literature | 4 | 5 | ENGL 900 | Academic Elective”
  - equivalencies[IB-ENGLISH-A-LITERATURE|English A Literature]:  ⟵ “English A Literature | 5 - 7 | 5 | ENGL&111 | Humanities”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|Environmental Systems & Societies]:  ⟵ “Environmental Systems & Societies | 4 - 7 | 5 | ENVS 940 | Natural Science”
  - equivalencies[IB-HISTORY|European History]:  ⟵ “European History | 4 - 7 | 15 | HIST&116 (5), HIST&117 (5), HIST&118 (5) | Social Science”
  - equivalencies[IB-FILM|Film]:  ⟵ “Film | 4 - 7 | 5 | FILM 800 | Restricted Elective”
  - equivalencies[IB-FRENCH|French B]:  ⟵ “French B | 5 | 5 | FRCH&121 | Humanities (World Language)”
  - equivalencies[IB-FRENCH|French B]:  ⟵ “French B | 6 | 10 | FRCH&121 (5), FRCH&122 (5) | Humanities (World Language)”
  - equivalencies[IB-FRENCH|French B]:  ⟵ “French B | 7 | 15 | FRCH&121 (5), FRCH&122 (5), FRCH&123 (5) | Humanities (World Language)”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | 4 - 7 | 5 | GEOG&200 | Social Science / Humanities”
  - … 19 more rows
### `a7eca1bf18227bf2` Olympic College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.olympic.edu/student-life-support/enrollment-services/transfer-students/transfer-olympic-college/transfer (sha256 2f3047533a24)
- issues: credits_implausible
- checks: {"distinct_exams": 26, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 4.5 | POLS&202 | Social Science”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 4.5 | ENGL&244 | Humanities”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | 4.5 | ENGL&111 | Humanities”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 9.0 | BIOL 940 | Natural Science”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 6.0 | Math&151 | Natural Science / Quantitative”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | - | Math 99 | Only use for course prerequisites”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 9.0 | ENGL&101 | ”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 4.5 | ENGL 920 | Humanities”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 4.5 | ACCT& 201 | Academic Elective”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1 | 50 | 9.0 | FRCH&121 | Humanities (World Language)”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, Level 2 | 59 | 18.0 | FRCH&121 (6), FRCH&122 (6), FRCH&123 (6) | Humanities (World Language)”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1 | 50 | 9.0 | GERM&121 | Humanities (World Language)”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language, Level 2 | 60 | 18.0 | GERM&121 (6), GERM&122 (6), GERM&123 (6) | Humanities (World Language)”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | 4.5 | PSYC&200 | Social Science”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 4.5 | HUMAN 920 | Humanities”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Intro Business Law | 50 | 4.5 | BUS& 201 | Academic Elective”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology | 50 | 4.5 | PSYC 930 | Social Science”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Intro to Psychology | 50 | 4.5 | PSYC& 100 | Social Science”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Intro to Sociology | 50 | 4.5 | SOC& 101 | Social Science”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | 9.0 | SCI 940 | Natural Science”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 4.5 | ECON& 202 | Social Science”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 4.5 | BMGMT 282 | Restricted Elective”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 4.5 | BMGMT 180 | Restricted Elective”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 4.5 | ECON& 201 | Social Science”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences & History | 50 | 9.0 | SOCSC 930 | Social Science”
  - … 4 more rows
### `20c512d9cd55c2f1` Pacific Lutheran University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.plu.edu/financial-services/students/cost/2025-26-cost-information/ (sha256 13610edc4f92)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.plu.edu/financial-services/students/cost/2026-27-cost-information-2/
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition*:: 50720 ⟵ “Tuition*: | $50,720”
  - column:Housing & Food*:: 13710 ⟵ “Housing & Food*: | $13,710”
  - column:Wellness Access Plan*:: 500 ⟵ “Wellness Access Plan*: | $500”
  - column:J-Term Fee*: 460 ⟵ “J-Term Fee* | $460”
  - column:Technology Fee*: 280 ⟵ “Technology Fee* | $280”
  - column:Student Resource & Activity Fee*: 40 ⟵ “Student Resource & Activity Fee* | $40”
  - column:Diversity, Justice & Sustainability Fee*:: 20 ⟵ “Diversity, Justice & Sustainability Fee*: | $20”
  - column:Books & Supplies:: 810 ⟵ “Books & Supplies: | $810”
  - column:Personal:: 2080 ⟵ “Personal: | $2,080”
  - column:Transportation: 748 ⟵ “Transportation | $748”
  - column:Total:: 69368 ⟵ “Total: | $69,368”
### `36d0858723b261b8` Pacific Lutheran University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.plu.edu/financial-services/students/cost/2026-27-cost-information-2/ (sha256 be2183f68db1)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.plu.edu/financial-services/students/cost/2025-26-cost-information/
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition*:: 50720 ⟵ “Tuition*: | $50,720”
  - column:Housing & Food*:: 14670 ⟵ “Housing & Food*: | $14,670”
  - column:Wellness Access Plan*:: 510 ⟵ “Wellness Access Plan*: | $510”
  - column:J-Term Fee*: 920 ⟵ “J-Term Fee* | $920”
  - column:Technology Fee*: 290 ⟵ “Technology Fee* | $290”
  - column:Student Resource & Activity Fee*: 40 ⟵ “Student Resource & Activity Fee* | $40”
  - column:Diversity, Justice & Sustainability Fee*:: 20 ⟵ “Diversity, Justice & Sustainability Fee*: | $20”
  - column:Books & Supplies:: 834 ⟵ “Books & Supplies: | $834”
  - column:Personal:: 2142 ⟵ “Personal: | $2,142”
  - column:Transportation: 770 ⟵ “Transportation | $770”
  - column:Total:: 70916 ⟵ “Total: | $70,916”
### `387a7614629e588e` Pacific Lutheran University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.plu.edu/financial-services/students/cost/2026-27-cost-information-2/ (sha256 be2183f68db1)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.plu.edu/financial-services/students/cost/2025-26-cost-information/
- checks: {"columns": 1, "components_reconcile": true, "rows": 12}
  - column:Tuition*:: 54080 ⟵ “Tuition*: | $54,080”
  - column:Housing & Food*:: 14670 ⟵ “Housing & Food*: | $14,670”
  - column:Wellness Access Plan*:: 510 ⟵ “Wellness Access Plan*: | $510”
  - column:J-Term Fee*: 920 ⟵ “J-Term Fee* | $920”
  - column:Technology Fee*: 290 ⟵ “Technology Fee* | $290”
  - column:Matriculation Fee* (one time fee upon entrance to PLU): 290 ⟵ “Matriculation Fee* (one time fee upon entrance to PLU) | $290”
  - column:Student Resource & Activity Fee*: 40 ⟵ “Student Resource & Activity Fee* | $40”
  - column:Diversity, Justice & Sustainability Fee*:: 20 ⟵ “Diversity, Justice & Sustainability Fee*: | $20”
  - column:Books & Supplies:: 834 ⟵ “Books & Supplies: | $834”
  - column:Personal:: 2142 ⟵ “Personal: | $2,142”
  - column:Transportation: 770 ⟵ “Transportation | $770”
  - column:Total:: 74566 ⟵ “Total: | $74,566”
### `bd4888e483277773` Pacific Lutheran University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.plu.edu/financial-services/students/cost/2025-26-cost-information/ (sha256 13610edc4f92)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.plu.edu/financial-services/students/cost/2026-27-cost-information-2/
- checks: {"columns": 1, "components_reconcile": true, "rows": 12}
  - column:Tuition*:: 52256 ⟵ “Tuition*: | $52,256”
  - column:Housing & Food*:: 13710 ⟵ “Housing & Food*: | $13,710”
  - column:Wellness Access Plan*:: 500 ⟵ “Wellness Access Plan*: | $500”
  - column:J-Term Fee*: 460 ⟵ “J-Term Fee* | $460”
  - column:Technology Fee*: 280 ⟵ “Technology Fee* | $280”
  - column:Matriculation Fee* (one time fee upon entrance to PLU): 275 ⟵ “Matriculation Fee* (one time fee upon entrance to PLU) | $275”
  - column:Student Resource & Activity Fee*: 40 ⟵ “Student Resource & Activity Fee* | $40”
  - column:Diversity, Justice & Sustainability Fee*:: 20 ⟵ “Diversity, Justice & Sustainability Fee*: | $20”
  - column:Books & Supplies:: 810 ⟵ “Books & Supplies: | $810”
  - column:Personal:: 2080 ⟵ “Personal: | $2,080”
  - column:Transportation: 748 ⟵ “Transportation | $748”
  - column:Total:: 71179 ⟵ “Total: | $71,179”
### `b8945e56295b8609` Pierce College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pierce.ctc.edu/pay-college/tuition/refunds.html (sha256 f170a9b6fb7d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Canceled classes.”
### `6b9bd8c85bd1d161` Renton Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://rtc.edu/paying-for-college/financial-aid/satisfactory-progress.php (sha256 45c06838d1df)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Regain Eligibility for Financial Aid Students who are suspended from financial aid have two (2) options to regain their eligibility: Satisfactory Academic Progress (SAP) Appeal: students have the right to appeal their financial aid suspension.”
  - sentence: sap_appeal ⟵ “The self-reinstatement evaluation must be requested by selecting the option on the SAP appeal form.”
### `c399af19d28bc4d3` Renton Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://rtc.edu/paying-for-college/financial-aid/estimated-cost-of-attendance.php (sha256 548ec891d8e3)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition & Fees: 6486 ⟵ “Tuition & Fees | $6,486 | $9,525”
  - off_campus_not_with_family:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528”
  - off_campus_not_with_family:Room & Board*: 18258 ⟵ “Room & Board* | $18,258 | $18,258”
  - off_campus_not_with_family:Transportation: 2796 ⟵ “Transportation | $2,796 | $2,796”
  - off_campus_not_with_family:Miscellaneous/Personal: 1968 ⟵ “Miscellaneous/Personal | $1,968 | $1,968”
  - off_campus_not_with_family:Total: 30036 ⟵ “Total | $30,036 | $33,075”
  - off_campus_not_with_family:Tuition & Fees: 9525 ⟵ “Tuition & Fees | $6,486 | $9,525”
  - off_campus_not_with_family:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528”
  - off_campus_not_with_family:Room & Board*: 18258 ⟵ “Room & Board* | $18,258 | $18,258”
  - off_campus_not_with_family:Transportation: 2796 ⟵ “Transportation | $2,796 | $2,796”
  - off_campus_not_with_family:Miscellaneous/Personal: 1968 ⟵ “Miscellaneous/Personal | $1,968 | $1,968”
  - off_campus_not_with_family:Total: 33075 ⟵ “Total | $30,036 | $33,075”
### `6aaf3320bcbc7a85` Renton Technical College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://rtc.edu/student-life/student-services/enrollment-services/transfer-to-rtc/ib-test-score-equivalencies.php (sha256 c1ed20c3439b)
- issues: course_column_missing
- checks: {"distinct_exams": 22, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|4]:  ⟵ “African History | 4 | Distribution Credit (5)—Social Science or Humanities based on institutional placement of History discipline”
  - equivalencies[IB-FRENCH|5]:  ⟵ “Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish A | 5 | Humanities distribution (5)”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL&100, BIOL&160 (5)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business & Management | 4 | Business or management elective (5)”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM&121 (5)”
  - equivalencies[IB-COMPUTER-SCIENCE|4]:  ⟵ “Computer Science | 4 | CS& 141 or first transfer-level computer programming course (5)”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | 4 | Elective (5)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|4]:  ⟵ “English A Literature | 4 | Humanities distribution (5)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4]:  ⟵ “English A Language & Literature | 4 | Humanities distribution (5)”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4]:  ⟵ “Environmental Systems and Societies | 4 | ENVS&100 (5) or natural science distribution (5)”
  - equivalencies[IB-FILM|4]:  ⟵ “Film | 4 | Humanities distribution (5)”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOG&200 (5)”
  - equivalencies[IB-GLOBAL-POLITICS|4]:  ⟵ “Global Politics | 4 | Political science elective (5)”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|SL 4-5]:  ⟵ “Mathematics: Applications and Interpretation | SL 4-5 | College-level math distribution (5)”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL 4-5]:  ⟵ “Mathematics: Analysis and Approaches | SL 4-5 | MATH&107 (5)”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music | 4 | MUSC&105 (5)”
  - equivalencies[IB-PHILOSOPHY|4]:  ⟵ “Philosophy | 4 | PHIL&101 (5)”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics | 4 | PHYS&114 and PHYS&115 (10)”
  - equivalencies[IB-PSYCHOLOGY|4]:  ⟵ “Psychology | 4 | PSYC&100 (5)”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4]:  ⟵ “Social & Cultural Anthropology | 4 | ANTH&206 (5)”
  - equivalencies[IB-THEATRE|4]:  ⟵ “Theatre | 4 | DRMA&101 (5) or Humanities distribution (5)”
  - equivalencies[IB-VISUAL-ARTS|4]:  ⟵ “Visual Arts | 4 | ART&100 (5)”
### `7526809ebcf014d1` Renton Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://rtc.edu/student-life/student-services/enrollment-services/transfer-to-rtc/advanced-placement-test-score-equivalencies.php (sha256 d12317c8727b)
- issues: course_column_missing
- checks: {"distinct_exams": 37, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | Humanities or Social Sciences Distribution (5) | Yes”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art: Art History | 3 | ART& 100 (5) | Yes”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art: Studio Art – Drawing | 3 | Humanities Distribution (5) | Yes”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art: 2D Design | 3 | Humanities Distribution (5) | Yes”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art: 3D Design | 3 | Humanities Distribution (5) | Yes”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL& 100, BIOL& 160 (5) | Yes”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | Math& 151 (5) | Yes”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | Math& 151 (5) and MATH& 152 (5) | Yes”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM& 121, CHEM& 161 (5) | Yes”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | CHIN& 121 (5) | Yes”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | Elective (5) | Yes”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | Computer Science elective (5) | Yes”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Micro | 3 | ECON& 201 (5) | Yes”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macro | 3 | ECON& 202 (5) | Yes”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVS& 100 (5) | Yes”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST& 116, HIST& 117, HIST& 118 (5) | Yes”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | FRCH& 121 (5) | Yes”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture | 3 | GERM& 121 (5) | Yes”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “US Government & Politics | 3 | POLS& 202 (5) | Yes”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics | 3 | POLS& 101 (5) | Yes”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG& 200 (5) | Yes”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language & Culture | 3 | ITAL& 121, Humanities Distribution (5) | Yes”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language | 3 | JAPN& 121 (5) | Yes”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin Literature | 3 | Humanities Distribution (5) | No”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | MUSC& 121 + MUSC& 131, MUSC& 141 (5) | Yes”
  - … 12 more rows
### `01d32848abf0032d` Saint Martin's University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/resources-and-forms/special-circumstances-and-cost-attendance-appeals (sha256 b19d2b22fa2b)
- issues: semantic_review_required, conflicting_sources:https://www.stmartin.edu/documents/26-27-sap-appeal,https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-dependent,https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-independent,https://www.stmartin.edu/documents/sap-appeal-form-25-26
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances and cost of attendance appeals | Saint Martin's University Skip to main site navigation Skip to main content Saint Martin's University Apply Request Information Visit Give Open the search panel Open the main menu Search Saint Martin's University Information For...”
  - sentence: need_based_special_circumstances ⟵ “A community that cares Academic excellence Transformative outcomes Living & learning in the Pacific Northwest Mission & vision University leadership Saint Martin's at a glance Work at Saint Martin's Special circumstances and cost of attendance appeals Admissions & Financial Aid Undergraduate Financial aid Resources and forms Special circumstances and cost of attendance appeals Financial aid awards”
  - sentence: need_based_special_circumstances ⟵ “Some examples of special circumstances include: Loss of income (wages, benefits, etc.) due to unemployment, retirement, disability or becoming a full-time student.”
  - sentence: need_based_special_circumstances ⟵ “Contact the Office of Financial Aid to discuss the changes in your financial situation before you submit a Special Circumstance Appeal.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstance appeal form – Dependent student Special circumstance appeal form – Independent student Next Cost of attendance appeals Cost of attendance appeals Cost of attendance appeals The Cost of Attendance includes average amounts for standard educational expenses incurred by students who attend Saint Martin’s University during the academic year.”
### `50735d08c29a152c` Saint Martin's University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-independent (sha256 9c7d738a5b67)
- issues: semantic_review_required, conflicting_sources:https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/resources-and-forms/special-circumstances-and-cost-attendance-appeals,https://www.stmartin.edu/documents/26-27-sap-appeal,https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-dependent,https://www.stmartin.edu/documents/sap-appeal-form-25-26
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 SPECIAL CIRCUMSTANCES APPEAL – INDEPENDENT Directions - If you have extenuating circumstances that the standard federal formula of analyzing need does not consider, please complete this form and return it to our office.”
  - sentence: need_based_special_circumstances ⟵ “Type of Special Circumstance (x) Check all that apply and submit the required documents.”
### `695a0f2b7a8b4658` Saint Martin's University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.stmartin.edu/documents/special-circumstances-appeal-form-independent-student-25-26 (sha256 0da08e2c55ed)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.stmartin.edu/documents/dependency-override-appeal-form-25-26,https://www.stmartin.edu/documents/special-circumstances-appeal-form-dependent-student-25-26
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “2025-2026 SPECIAL CIRCUMSTANCES APPEAL – INDEPENDENT Directions - If you have extenuating circumstances that the standard federal formula of analyzing need does not consider, please complete this form and return it to our office.”
  - sentence: need_based_special_circumstances ⟵ “Type of Special Circumstance (x) Check all that apply and submit the required documents.”
### `6f56a96b4e30718b` Saint Martin's University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stmartin.edu/documents/26-27-sap-appeal (sha256 27fc2ef0159d)
- issues: semantic_review_required, conflicting_sources:https://www.stmartin.edu/documents/sap-appeal-form-25-26
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Return this form to: Office of Financial Aid Old Main 250 Email: Finaid@stmartin.edu Phone: (360) 688-2150 Upload via Secure File Upload: Satisfactory Academic Progress Appeal Form The Office of Financial Aid has notified you that you are not meeting satisfactory academic progress standards required to receive student financial aid.”
  - sentence: sap_appeal ⟵ “Any extenuating circumstances that caused you to be placed on SAP Must Appeal; 2.”
### `7db0c7a4802d2b28` Saint Martin's University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.stmartin.edu/documents/dependency-override-appeal-form-25-26 (sha256 b0c3bb53e08a)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.stmartin.edu/documents/special-circumstances-appeal-form-dependent-student-25-26,https://www.stmartin.edu/documents/special-circumstances-appeal-form-independent-student-25-26
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The definition of a dependency override is a dependent student’s inability to submit parental information on the Free Application for Federal Student Aid (FAFSA) due to an unusual circumstance.”
### `870c60309fa7ec47` Saint Martin's University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stmartin.edu/documents/26-27-sap-appeal (sha256 27fc2ef0159d)
- issues: semantic_review_required, conflicting_sources:https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/resources-and-forms/special-circumstances-and-cost-attendance-appeals,https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-dependent,https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-independent,https://www.stmartin.edu/documents/sap-appeal-form-25-26
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The Office of Financial Aid considers appeals based on a variety of extenuating circumstances (e.g., personal illness or injury, death of an immediate family member, or other unusual circumstances beyond your control).”
### `872e28532c749484` Saint Martin's University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stmartin.edu/documents/sap-appeal-form-25-26 (sha256 879a9744614e)
- issues: semantic_review_required, conflicting_sources:https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/resources-and-forms/special-circumstances-and-cost-attendance-appeals,https://www.stmartin.edu/documents/26-27-sap-appeal,https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-dependent,https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-independent
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The Office of Financial Aid considers appeals based on a variety of extenuating circumstances (e.g., personal illness or injury, death of an immediate family member, or other unusual circumstances beyond your control).”
### `9c28931b6f20e7c7` Saint Martin's University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stmartin.edu/documents/sap-appeal-form-25-26 (sha256 879a9744614e)
- issues: semantic_review_required, conflicting_sources:https://www.stmartin.edu/documents/26-27-sap-appeal
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Return this form to: Office of Financial Aid Old Main 250 Email: Finaid@stmartin.edu Phone: (360) 688-2150 Upload via Secure Dropbox: Satisfactory Academic Progress Appeal Form Saint Martin’s University Office of Financial Aid has notified you that your academic progress does not meet the level required to receive student financial aid; however, you have the right to appeal your status.”
  - sentence: sap_appeal ⟵ “Any extenuating circumstances that caused you to be placed on SAP Must Appeal; 2.”
### `bc779c74ec906df1` Saint Martin's University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-dependent (sha256 746bc7c1775a)
- issues: semantic_review_required, conflicting_sources:https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/resources-and-forms/special-circumstances-and-cost-attendance-appeals,https://www.stmartin.edu/documents/26-27-sap-appeal,https://www.stmartin.edu/documents/26-27-special-circumstance-appeal-independent,https://www.stmartin.edu/documents/sap-appeal-form-25-26
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 SPECIAL CIRCUMSTANCES APPEAL – DEPENDENT Directions - If you have special circumstances that the standard federal formula of analyzing need does not consider, please complete this form and return it to our office.”
  - sentence: need_based_special_circumstances ⟵ “TYPE OF SPECIAL CIRCUMSTANCE (x) Check all that apply and submit the required documents.”
### `cf54d7ce55cdf5c5` Saint Martin's University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/resources-and-forms/special-circumstances-and-cost-attendance-appeals (sha256 b19d2b22fa2b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Families do have an opportunity to request an increase in their Cost of Attendance for one of the following reasons: Additional course-related expenses One-time purchase of computer Technology needed for coursework Child care expenses Medical/dental expenses not covered by insurance Automobile expenses (repair, insurance, maintenance) If a budget increase is approved, it is unlikely that it will b”
### `d04017ee516f0260` Saint Martin's University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.stmartin.edu/documents/special-circumstances-appeal-form-dependent-student-25-26 (sha256 c152ce8664dd)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.stmartin.edu/documents/dependency-override-appeal-form-25-26,https://www.stmartin.edu/documents/special-circumstances-appeal-form-independent-student-25-26
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “2025-2026 SPECIAL CIRCUMSTANCES APPEAL – DEPENDENT Directions - If you have extenuating circumstances that the standard federal formula of analyzing need does not consider, please complete this form and return it to our office.”
  - sentence: need_based_special_circumstances ⟵ “TYPE OF SPECIAL CIRCUMSTANCE (x) Check all that apply and submit the required documents.”
### `fef12a74c8f01bf1` Saint Martin's University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.stmartin.edu/documents/dependency-override-appeal-form-25-26 (sha256 b0c3bb53e08a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “Office of Financial Aid 5000 Abbey Way SE 250 Old Main Lacey WA 98503 Phone: (360) 688-2150 finaid@stmartin.edu 2025-2026 DEPENDENCY OVERRIDE APPEAL _________________________________________________________________________________ NAME _________________________________ St.”
  - sentence: dependency_override ⟵ “Martin's Student ID# ______________________ The US Department of Education has given the Office of Student Financial Aid guidance regarding situations that merit a dependency override.”
  - sentence: dependency_override ⟵ “All Dependency Override requests are reviewed and processed in the date and order in which they were received by our office.”
### `8381d538e098c77e` Saint Martin's University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/cost-attendance (sha256 bdd10f7109a8)
- issues: conflicting_sources:https://www.stmartin.edu/admissions-financial-aid/tuition-and-fees
- checks: {"columns": 4, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition and Fees: 48264 ⟵ “Tuition and Fees | $48,264 | $48,264 | $48,264 | $6,000”
  - on_campus:Housing: 7295 ⟵ “Housing | $7,295 | $7,378 | $14,756 | $0”
  - on_campus:Food: 9856 ⟵ “Food | $9,856 | $5,000 | $5,000 | $5,000”
  - on_campus:Books, course materials, supplies, and equipment: 1693 ⟵ “Books, course materials, supplies, and equipment | $1,693 | $1,693 | $1,693 | $1,693”
  - on_campus:Miscellaneous personal expenses: 2016 ⟵ “Miscellaneous personal expenses | $2,016 | $2,016 | $2,016 | $2,016”
  - on_campus:Loan Fees: 66 ⟵ “Loan Fees | $66 | $66 | $66 | $66”
  - on_campus:Transportation: 2430 ⟵ “Transportation | $2,430 | $2,430 | $2,430 | $2,430”
  - on_campus:Total: 71620 ⟵ “Total | $71,620 | $66,847 | $74,225 | $17,205”
  - with_parents_or_family:Tuition and Fees: 48264 ⟵ “Tuition and Fees | $48,264 | $48,264 | $48,264 | $6,000”
  - with_parents_or_family:Housing: 7378 ⟵ “Housing | $7,295 | $7,378 | $14,756 | $0”
  - with_parents_or_family:Food: 5000 ⟵ “Food | $9,856 | $5,000 | $5,000 | $5,000”
  - with_parents_or_family:Books, course materials, supplies, and equipment: 1693 ⟵ “Books, course materials, supplies, and equipment | $1,693 | $1,693 | $1,693 | $1,693”
  - with_parents_or_family:Miscellaneous personal expenses: 2016 ⟵ “Miscellaneous personal expenses | $2,016 | $2,016 | $2,016 | $2,016”
  - with_parents_or_family:Loan Fees: 66 ⟵ “Loan Fees | $66 | $66 | $66 | $66”
  - with_parents_or_family:Transportation: 2430 ⟵ “Transportation | $2,430 | $2,430 | $2,430 | $2,430”
  - with_parents_or_family:Total: 66847 ⟵ “Total | $71,620 | $66,847 | $74,225 | $17,205”
  - off_campus_not_with_family:Tuition and Fees: 48264 ⟵ “Tuition and Fees | $48,264 | $48,264 | $48,264 | $6,000”
  - off_campus_not_with_family:Housing: 14756 ⟵ “Housing | $7,295 | $7,378 | $14,756 | $0”
  - off_campus_not_with_family:Food: 5000 ⟵ “Food | $9,856 | $5,000 | $5,000 | $5,000”
  - off_campus_not_with_family:Books, course materials, supplies, and equipment: 1693 ⟵ “Books, course materials, supplies, and equipment | $1,693 | $1,693 | $1,693 | $1,693”
  - off_campus_not_with_family:Miscellaneous personal expenses: 2016 ⟵ “Miscellaneous personal expenses | $2,016 | $2,016 | $2,016 | $2,016”
  - off_campus_not_with_family:Loan Fees: 66 ⟵ “Loan Fees | $66 | $66 | $66 | $66”
  - off_campus_not_with_family:Transportation: 2430 ⟵ “Transportation | $2,430 | $2,430 | $2,430 | $2,430”
  - off_campus_not_with_family:Total: 74225 ⟵ “Total | $71,620 | $66,847 | $74,225 | $17,205”
  - other:Tuition and Fees: 6000 ⟵ “Tuition and Fees | $48,264 | $48,264 | $48,264 | $6,000”
  - … 7 more rows
### `cb97e46f8ba6436f` Saint Martin's University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/cost-attendance (sha256 bdd10f7109a8)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.stmartin.edu/admissions-financial-aid/tuition-and-fees
- checks: {"columns": 4, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition and fees: 46856 ⟵ “Tuition and fees | $46,856 | $46,856 | $46,856 | $6,000”
  - on_campus:Housing (On Campus: average rate of all available housing options): 7072 ⟵ “Housing (On Campus: average rate of all available housing options) | $7,072 | $7,122 | $14,243 | $0”
  - on_campus:Food (On Campus: Gold meal plan): 8080 ⟵ “Food (On Campus: Gold meal plan) | $8,080 | $4,850 | $4,850 | $4,850”
  - on_campus:Books, course materials, supplies and equipment*: 1298 ⟵ “Books, course materials, supplies and equipment* | $1,298 | $1,298 | $1,298 | $1,298”
  - on_campus:Miscellaneous personal expenses: 1957 ⟵ “Miscellaneous personal expenses | $1,957 | $1,957 | $1,957 | $1,957”
  - on_campus:Loan fees: 74 ⟵ “Loan fees | $74 | $74 | $74 | $74”
  - on_campus:Transportation: 2439 ⟵ “Transportation | $2,439 | $2,439 | $2,439 | $2,439”
  - on_campus:TOTAL: 67776 ⟵ “TOTAL | $67,776 | $64,596 | $71,717 | $16,618”
  - with_parents_or_family:Tuition and fees: 46856 ⟵ “Tuition and fees | $46,856 | $46,856 | $46,856 | $6,000”
  - with_parents_or_family:Housing (On Campus: average rate of all available housing options): 7122 ⟵ “Housing (On Campus: average rate of all available housing options) | $7,072 | $7,122 | $14,243 | $0”
  - with_parents_or_family:Food (On Campus: Gold meal plan): 4850 ⟵ “Food (On Campus: Gold meal plan) | $8,080 | $4,850 | $4,850 | $4,850”
  - with_parents_or_family:Books, course materials, supplies and equipment*: 1298 ⟵ “Books, course materials, supplies and equipment* | $1,298 | $1,298 | $1,298 | $1,298”
  - with_parents_or_family:Miscellaneous personal expenses: 1957 ⟵ “Miscellaneous personal expenses | $1,957 | $1,957 | $1,957 | $1,957”
  - with_parents_or_family:Loan fees: 74 ⟵ “Loan fees | $74 | $74 | $74 | $74”
  - with_parents_or_family:Transportation: 2439 ⟵ “Transportation | $2,439 | $2,439 | $2,439 | $2,439”
  - with_parents_or_family:TOTAL: 64596 ⟵ “TOTAL | $67,776 | $64,596 | $71,717 | $16,618”
  - off_campus_not_with_family:Tuition and fees: 46856 ⟵ “Tuition and fees | $46,856 | $46,856 | $46,856 | $6,000”
  - off_campus_not_with_family:Housing (On Campus: average rate of all available housing options): 14243 ⟵ “Housing (On Campus: average rate of all available housing options) | $7,072 | $7,122 | $14,243 | $0”
  - off_campus_not_with_family:Food (On Campus: Gold meal plan): 4850 ⟵ “Food (On Campus: Gold meal plan) | $8,080 | $4,850 | $4,850 | $4,850”
  - off_campus_not_with_family:Books, course materials, supplies and equipment*: 1298 ⟵ “Books, course materials, supplies and equipment* | $1,298 | $1,298 | $1,298 | $1,298”
  - off_campus_not_with_family:Miscellaneous personal expenses: 1957 ⟵ “Miscellaneous personal expenses | $1,957 | $1,957 | $1,957 | $1,957”
  - off_campus_not_with_family:Loan fees: 74 ⟵ “Loan fees | $74 | $74 | $74 | $74”
  - off_campus_not_with_family:Transportation: 2439 ⟵ “Transportation | $2,439 | $2,439 | $2,439 | $2,439”
  - off_campus_not_with_family:TOTAL: 71717 ⟵ “TOTAL | $67,776 | $64,596 | $71,717 | $16,618”
  - other:Tuition and fees: 6000 ⟵ “Tuition and fees | $46,856 | $46,856 | $46,856 | $6,000”
  - … 7 more rows
### `dc1dcda2514d74bc` Saint Martin's University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stmartin.edu/admissions-financial-aid/tuition-and-fees (sha256 969c0a674fcb)
- issues: components_do_not_reconcile, conflicting_sources:https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/cost-attendance
- checks: {"columns": 2, "components_reconcile": false, "rows": 4}
  - on_campus:Tuition: 48264 ⟵ “Tuition | $48,264 | $48,264”
  - on_campus:Housing (average rate - varies by room type; details in tuition and fee breakdown section below): 7295 ⟵ “Housing (average rate - varies by room type; details in tuition and fee breakdown section below) | $7,295 | $14,756”
  - on_campus:Food (highest rate - varies by meal plan; details in tuition and fee breakdown section below): 9856 ⟵ “Food (highest rate - varies by meal plan; details in tuition and fee breakdown section below) | $9,856 | $5,000”
  - on_campus:Total: 66557.5 ⟵ “Total | $66,557.50 | $68,962.50”
  - off_campus_not_with_family:Tuition: 48264 ⟵ “Tuition | $48,264 | $48,264”
  - off_campus_not_with_family:Housing (average rate - varies by room type; details in tuition and fee breakdown section below): 14756 ⟵ “Housing (average rate - varies by room type; details in tuition and fee breakdown section below) | $7,295 | $14,756”
  - off_campus_not_with_family:Food (highest rate - varies by meal plan; details in tuition and fee breakdown section below): 5000 ⟵ “Food (highest rate - varies by meal plan; details in tuition and fee breakdown section below) | $9,856 | $5,000”
  - off_campus_not_with_family:Total: 68962.5 ⟵ “Total | $66,557.50 | $68,962.50”
### `fdb37fdf29328e2d` Saint Martin's University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stmartin.edu/admissions-financial-aid/tuition-and-fees (sha256 969c0a674fcb)
- issues: components_do_not_reconcile, stale_year_label:2025-26, conflicting_sources:https://www.stmartin.edu/admissions-financial-aid/undergraduate/financial-aid/cost-attendance
- checks: {"columns": 2, "components_reconcile": false, "rows": 5}
  - on_campus:Tuition: 46856 ⟵ “Tuition | $46,856 | $46,856”
  - on_campus:Housing (average rate - varies by room type; details in tuition and fee breakdown section below): 7072 ⟵ “Housing (average rate - varies by room type; details in tuition and fee breakdown section below) | $7,072 | $14,243”
  - on_campus:Food (highest rate - varies by meal plan; details in tuition and fee breakdown section below): 9570 ⟵ “Food (highest rate - varies by meal plan; details in tuition and fee breakdown section below) | $9,570 | $4,850”
  - on_campus:SMU Textbook Program* (varies by course load, example given for 15-credit load per semester): 712.5 ⟵ “SMU Textbook Program* (varies by course load, example given for 15-credit load per semester) | $712.50 | $712.50”
  - on_campus:Total: 64610.5 ⟵ “Total | $64,610.50 | $66,861.50”
  - off_campus_not_with_family:Tuition: 46856 ⟵ “Tuition | $46,856 | $46,856”
  - off_campus_not_with_family:Housing (average rate - varies by room type; details in tuition and fee breakdown section below): 14243 ⟵ “Housing (average rate - varies by room type; details in tuition and fee breakdown section below) | $7,072 | $14,243”
  - off_campus_not_with_family:Food (highest rate - varies by meal plan; details in tuition and fee breakdown section below): 4850 ⟵ “Food (highest rate - varies by meal plan; details in tuition and fee breakdown section below) | $9,570 | $4,850”
  - off_campus_not_with_family:SMU Textbook Program* (varies by course load, example given for 15-credit load per semester): 712.5 ⟵ “SMU Textbook Program* (varies by course load, example given for 15-credit load per semester) | $712.50 | $712.50”
  - off_campus_not_with_family:Total: 66861.5 ⟵ “Total | $64,610.50 | $66,861.50”
### `7ca16eb7cb7e426a` Saint Martin's University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.stmartin.edu/admissions-financial-aid/undergraduate/applying-saint-martins/transfer-students-undergrad/transferring-credits (sha256 1a5d7f6c2216)
- issues: rows_without_score
- checks: {"distinct_exams": 18, "equivalencies": 18, "rows_without_score": 18}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | Core science w/ lab | 4”
  - equivalencies[IB-CHEMISTRY-SL|None]:  ⟵ “Chemistry- SL | CHM 141/141L | 5”
  - equivalencies[IB-CHEMISTRY-HL|None]:  ⟵ “Chemistry- HL | CHM 141/141L and CHM 142/142L | 10”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | CSC 101 | 3”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | Core social and behavioral foundations | 3”
  - equivalencies[IB-FILM|None]:  ⟵ “Film | Core fine arts | 3”
  - equivalencies[IB-FRENCH-SL|None]:  ⟵ “French Language and Lit- SL | FRN 101 | 3”
  - equivalencies[IB-FRENCH-HL|None]:  ⟵ “French Language and Lit- HL | FRN 101 and FRN 102 | 6”
  - equivalencies[IB-GERMAN-HL|None]:  ⟵ “German Language and Lit- HL | Core 1 year World Language | 6”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | GPH 210 | 3”
  - equivalencies[IB-GLOBAL-POLITICS|None]:  ⟵ “Global Politics | PLS 152 | 3”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History, world | Core non-U.S. history | 3”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | Core fine arts | 3”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Physics | Core science w/ lab | 4”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | PSY 101 | 3”
  - equivalencies[IB-SPANISH-SL|None]:  ⟵ “Spanish Language and Lit- SL | SPN 101 | 3”
  - equivalencies[IB-SPANISH-HL|None]:  ⟵ “Spanish Language and Lit- HL | SPN 101 and SPN 102 | 6”
  - equivalencies[IB-THEATRE|None]:  ⟵ “Theater | Core fine arts | 3”
### `bfb1aa9d51623327` Seattle Central College — appeals 2026-27 [new] (labeled_in_source)
- source: https://seattlecentral.edu/enrollment-and-funding/financial-aid-and-funding/financial-aid (sha256 488a52d25f10)
- issues: semantic_review_required, conflicting_sources:https://seattlecentral.edu/enrollment-and-funding/financial-aid-and-funding/financial-aid/student-responsibilities
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Get Your Funding Back If your financial aid has been cancelled for not meeting Satisfactory Academic Progress (SAP), you may appeal to reinstate your aid.”
### `d41f2246fcc5c8f2` Seattle Central College — appeals 2026-27 [new] (source_unlabeled)
- source: https://seattlecentral.edu/enrollment-and-funding/financial-aid-and-funding/financial-aid/student-responsibilities (sha256 19f707ece916)
- issues: semantic_review_required, conflicting_sources:https://seattlecentral.edu/enrollment-and-funding/financial-aid-and-funding/financial-aid
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Financial Aid Student Responsibilities Get Your Funding Back If your financial aid has been cancelled for not meeting Satisfactory Academic Progress (SAP), you may appeal to reinstate your aid.”
  - sentence: sap_appeal ⟵ “Probation – students on probation have had a “SAP Appeal” or “Appeal for Reinstatement of Aid” approved and are expected to be eligible at the end of the term.”
  - sentence: sap_appeal ⟵ “Conditional Probation – students on conditional probation have had a “SAP Appeal” or “Appeal for Reinstatement of Aid” approved and are required to follow specified conditions of their reinstatement.”
  - sentence: sap_appeal ⟵ “Education plans (academic plans) are included in the SAP appeal process.”
  - sentence: sap_appeal ⟵ “Students on probation have had an “SAP Appeal” approved and are expected to be eligible at the end of the term.”
### `3e4855cb03b1ae11` Seattle Central College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://seattlecentral.edu/enrollment-and-funding/financial-aid-and-funding/financial-aid/cost-attendance (sha256 ae6fee486add)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees*: 5520 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - column:Food and Housing: 19473 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - column:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - column:Transportation: 3069 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - column:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - column:Total Expected Cost of Attendance: 30498 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
  - column:Tuition and Fees*: 5520 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - column:Food and Housing: 10072 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - column:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - column:Transportation: 2832 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - column:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - column:Total Expected Cost of Attendance: 20860 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `401c35d278ec2ed9` Seattle University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.seattleu.edu/admissions-aid/financial-aid--scholarships/financial-aid/frequently-asked-questions/ (sha256 533ed866dc2d)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.seattleu.edu/student-financial-services/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeals Satisfactory Academic Progress (SAP) for financial aid eligibility is reviewed annually at the end of spring term.”
  - sentence: sap_appeal ⟵ “If the student and counselor determine that submitting an appeal is the best next step, the student will be given a Satisfactory Academic Progress Appeal Form on which to provide the following information: An explanation of the special circumstances that prevented the student from meeting satisfactory academic progress requirements for financial aid and What has changed in the student's situation ”
### `e6692481b2079465` Seattle University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.seattleu.edu/admissions-aid/financial-aid--scholarships/financial-aid/frequently-asked-questions/ (sha256 533ed866dc2d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “There are two categories of unique situations: special and unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are financial situations that support a change to the cost of attendance or SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances include, but are not limited to: Changes in employment status, income, or assets.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances are conditions that support a change to a student's dependency status based on a unique situation.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances include, but are not limited to: Human trafficking.”
  - sentence: need_based_special_circumstances ⟵ “Please note that unusual circumstances do not include: Parents refusal to contribute to student's education.”
### `fe97be14f3270b3a` Seattle University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.seattleu.edu/student-financial-services/ (sha256 b0ef37d69219)
- issues: semantic_review_required, conflicting_sources:https://www.seattleu.edu/admissions-aid/financial-aid--scholarships/financial-aid/frequently-asked-questions/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “They also review and process Satisfactory Academic Progress appeals, Special & Unusual Circumstances appeals, as well as manage specific populations and programs.”
### `affa322cc2705d21` Seattle University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.seattleu.edu/admissions-aid/financial-aid--scholarships/financial-aid/veterans-benefits--resources/ (sha256 f059d6d68e0b)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - column:Tuition (flat rate for 12-18 credits): 19800 ⟵ “Tuition (flat rate for 12-18 credits) | $19,800 | $19,800.00 | $19,800.00”
  - column:Technology Fee (full-time): 214.0 ⟵ “Technology Fee (full-time) | $214.00 | $214.00 | $214.00”
  - column:Wellness Fee (full-time): 172.0 ⟵ “Wellness Fee (full-time) | $172.00 | $172.00 | $172.00”
  - column:Activity Fee: 66 ⟵ “Activity Fee | $66 | $66 | $66”
  - column:Matriculation Fee: 175.0 ⟵ “Matriculation Fee | $175.00 |  | ”
  - column:Total: 20427.0 ⟵ “Total | $20,427.00 | $20,252.00 | $20,252.00”
  - column:Tuition (flat rate for 12-18 credits): 19800.0 ⟵ “Tuition (flat rate for 12-18 credits) | $19,800 | $19,800.00 | $19,800.00”
  - column:Technology Fee (full-time): 214.0 ⟵ “Technology Fee (full-time) | $214.00 | $214.00 | $214.00”
  - column:Wellness Fee (full-time): 172.0 ⟵ “Wellness Fee (full-time) | $172.00 | $172.00 | $172.00”
  - column:Activity Fee: 66 ⟵ “Activity Fee | $66 | $66 | $66”
  - column:Total: 20252.0 ⟵ “Total | $20,427.00 | $20,252.00 | $20,252.00”
  - column:Tuition (flat rate for 12-18 credits): 19800.0 ⟵ “Tuition (flat rate for 12-18 credits) | $19,800 | $19,800.00 | $19,800.00”
  - column:Technology Fee (full-time): 214.0 ⟵ “Technology Fee (full-time) | $214.00 | $214.00 | $214.00”
  - column:Wellness Fee (full-time): 172.0 ⟵ “Wellness Fee (full-time) | $172.00 | $172.00 | $172.00”
  - column:Activity Fee: 66 ⟵ “Activity Fee | $66 | $66 | $66”
  - column:Total: 20252.0 ⟵ “Total | $20,427.00 | $20,252.00 | $20,252.00”
### `0a7552a6796159e2` Shoreline Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Satisfactory%20Academic%20Progress%20Appeal%20Form_Apr25.pdf (sha256 4cf11cb472c5)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Appeal%20to%20Exceed%20Maximum%20Time%20Frame_Apr25.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Special%20Conditions%20Appeal%20Change%20in%20Family%20Status.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Example: 35 completed credits / 50 attempted credits = 70% completion rate My appeal is based on: (Check all that apply) ☐ Unusual Circumstances ☐ Improved completion rate to at least 67% ☐ Raised cumulative GPA to at least 2.0 ☐ Attended one or more quarters on own AND are currently meeting overall SAP standards ☐ Unusual enrollment history Use this form to appeal the cancellation of your financi”
### `1542777848c89887` Shoreline Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/default.aspx (sha256 8612fb2d0ed1)
- issues: semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/conditions-of-award.aspx,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Appeal%20to%20Exceed%20Maximum%20Time%20Frame_May26.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Satisfactory%20Academic%20Progress%20Appeal%20Form_May26.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/sap-current-students.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Learn more about exit counseling Change of Income If you or your family have experienced a dramatic change in income or a loss of resources that was not reflected on your current FAFSA or WASFA, you may submit a Special Circumstances request to have your financial aid eligibility re-evaluated.”
### `15b7a6e07e388409` Shoreline Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/conditions-of-award.aspx (sha256 dcc6751a7c53)
- issues: semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/default.aspx,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Appeal%20to%20Exceed%20Maximum%20Time%20Frame_May26.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Satisfactory%20Academic%20Progress%20Appeal%20Form_May26.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/sap-current-students.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Change in Income If you or your family have experienced a dramatic change in income or a loss of resources(s) that was not reflected on your current FAFSA you may contact the Financial Aid Office to re-evaluate your financial aid eligibility based on your current income.”
### `30ee5d379d198f23` Shoreline Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Special%20Conditions%20Appeal%20Change%20in%20Family%20Status.pdf (sha256 b5a538e438f6)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Appeal%20to%20Exceed%20Maximum%20Time%20Frame_Apr25.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Satisfactory%20Academic%20Progress%20Appeal%20Form_Apr25.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Office Special Circumstances Appeal 2025-26 Change in Family Status The Financial Aid Office understands the FAFSA does not always accurately reflect your family’s ability to contribute to educational expenses.”
  - sentence: need_based_special_circumstances ⟵ “In some cases, appeals for additional aid are considered for a change in financial or household circumstance.”
  - sentence: need_based_special_circumstances ⟵ “To request a review of your financial aid eligibility, submit a Special Circumstances Appeal.”
### `3cd23bfe0ae2d59a` Shoreline Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/sap-current-students.aspx (sha256 bbd1a1c49590)
- issues: semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Satisfactory%20Academic%20Progress%20Appeal%20Form_May26.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal your financial aid cancellation You may appeal your cancellation by submitting a Satisfactory Academic Progress Appeal.”
### `66950e5e445fa627` Shoreline Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Satisfactory%20Academic%20Progress%20Appeal%20Form_Apr25.pdf (sha256 4cf11cb472c5)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “2025-2026 Financial Aid Office Satisfactory Academic Progress (SAP) Appeal Form Last Name First Name ctcLink #: I am submitting this appeal for: (Check one) ☐ Fall ☐ Winter ☐ Spring ☐ Summer Year: _________ Last year & quarter I attended SCC was: __________ ls your current cumulative GPA a 2.0 or higher and your overall completion rate at least 67%? ☐ Yes ☐ No Cumulative GPA: Completion rate: % *T”
### `7702dce34eaa8284` Shoreline Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Appeal%20to%20Exceed%20Maximum%20Time%20Frame_May26.pdf (sha256 74e8ba4bbc15)
- issues: semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/conditions-of-award.aspx,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/default.aspx,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Satisfactory%20Academic%20Progress%20Appeal%20Form_May26.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/sap-current-students.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you had unusual circumstances or program change that prevented you from completing a program within the allowed time frame, you may appeal for additional quarters of aid.”
### `8c9c82024c87eeaa` Shoreline Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Appeal%20to%20Exceed%20Maximum%20Time%20Frame_Apr25.pdf (sha256 89b4699b484e)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Satisfactory%20Academic%20Progress%20Appeal%20Form_Apr25.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2025-2026/2025_2026%20Special%20Conditions%20Appeal%20Change%20in%20Family%20Status.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you had unusual circumstances or program change that prevented you from completing a program within the allowed time frame, you may appeal for additional quarters of aid.”
### `95b016dd83c95678` Shoreline Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Satisfactory%20Academic%20Progress%20Appeal%20Form_May26.pdf (sha256 5babd057588b)
- issues: semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/conditions-of-award.aspx,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/default.aspx,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Appeal%20to%20Exceed%20Maximum%20Time%20Frame_May26.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/sap-current-students.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Example: 35 completed credits / 50 attempted credits = 70% completion rate My appeal is based on: (Check all that apply) ☐ Unusual Circumstances ☐ Improved completion rate to at least 67% ☐ Raised cumulative GPA to at least 2.0 ☐ Attended one or more quarters on own AND are currently meeting overall SAP standards ☐ Unusual enrollment history Use this form to appeal the cancellation of your financi”
### `c76bdc68d1b934af` Shoreline Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/sap-current-students.aspx (sha256 bbd1a1c49590)
- issues: semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/conditions-of-award.aspx,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/default.aspx,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Appeal%20to%20Exceed%20Maximum%20Time%20Frame_May26.pdf,https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Satisfactory%20Academic%20Progress%20Appeal%20Form_May26.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “If you had unusual circumstances that prevented you from completing a program within the allowed time frame, you may appeal for additional quarters of aid by submitting the Maximum Credit Limit appeal form.”
  - sentence: need_based_special_circumstances ⟵ “We consider mitigating or unusual circumstances that prevented you from successfully completing the quarter.”
  - sentence: need_based_special_circumstances ⟵ “Generally situations that include roommates, housing and transportation issues are not considered extreme or unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Documentation may include, but is not limited to, a letter from your health care provider, legal paperwork, receipts, other documents that support your mitigating or unusual circumstances. 1B.”
### `ce496184031c212b` Shoreline Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/forms/2026-2027/2026_2027%20Satisfactory%20Academic%20Progress%20Appeal%20Form_May26.pdf (sha256 5babd057588b)
- issues: semantic_review_required, conflicting_sources:https://www.shoreline.edu/apply-and-aid/funding-and-aid/financial-aid/sap-current-students.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “2026-2027 Financial Aid Satisfactory Academic Progress (SAP) Appeal Form Last Name First Name ctcLink #: I am submitting this appeal for: (Check one) ☐ Summer 2026 ☐ Fall 2026 ☐ Winter 2027 ☐ Spring 2027 Last quarter & year I attended SCC was: __________ ls your current cumulative GPA a 2.0 or higher and your overall completion rate at least 67%? ☐ Yes ☐ No Cumulative GPA: Completion rate: % *To c”
### `0f8e7f778a48a0e5` Shoreline Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.shoreline.edu/placement/ap-ib-scores.aspx (sha256 1775c626013d)
- issues: course_column_missing
- checks: {"distinct_exams": 32, "equivalencies": 62, "rows_without_score": 0}
  - equivalencies[AP-PRECALCULUS|4 or 5]:  ⟵ “A/P Pre-Calculus | 4 or 5 | MATH &141 and MATH &142 (10 credits) | Placement into Math& 151”
  - equivalencies[AP-PRECALCULUS|Score of 3]:  ⟵ “A/P Pre-Calculus | Score of 3 | MATH &141 (5 credits) | Placement into Math& 142”
  - equivalencies[AP-CALCULUS-AB|5]:  ⟵ “Calculus AB | 5 | MATH& 151 and 152 (10 credits) | Placement into MATH& 163”
  - equivalencies[AP-CALCULUS-AB|3 or 4]:  ⟵ “Calculus AB | 3 or 4 | MATH& 151 (5 credits) | Placement into MATH& 152”
  - equivalencies[AP-CALCULUS-AB|1 or 2]:  ⟵ “Calculus AB | 1 or 2 | No credit | Use another method for placement”
  - equivalencies[AP-CALCULUS-BC|3, 4 or 5]:  ⟵ “Calculus BC | 3, 4 or 5 | MATH& 151 and 152 (10 credits) | Placement into MATH& 163”
  - equivalencies[AP-CALCULUS-BC|1 or 2]:  ⟵ “Calculus BC | 1 or 2 | No credit | Use another method for placement”
  - equivalencies[AP-STATISTICS|3, 4, or 5]:  ⟵ “Statistics | 3, 4, or 5 | MATH& 146 (5 credits) | Use another method for placement into the calculus sequence (MATH& 151, 152, 163),”
  - equivalencies[AP-STATISTICS|1 or 2]:  ⟵ “Statistics | 1 or 2 | No credit | Use another method for math placement”
  - equivalencies[AP-ART-HISTORY|3, 4, or 5]:  ⟵ “Art: Art History | 3, 4, or 5 | ART& 100 (5 credits)”
  - equivalencies[AP-DRAWING|4 or 5]:  ⟵ “Art: Studio Art - Drawing | 4 or 5 | Humanities Distribution or Elective (5 credits)”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art: Studio Art - Drawing | 3 | Elective (5 credits)”
  - equivalencies[AP-2-D-ART-DESIGN|4 or 5]:  ⟵ “Art: 2D Design | 4 or 5 | Humanities Distribution or Elective (5 credits)”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art: 2D Design | 3 | Elective (5 credits)”
  - equivalencies[AP-3-D-ART-DESIGN|4 or 5]:  ⟵ “Art: 3D Design | 4 or 5 | Humanities Distribution or Elective (5 credits)”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art: 3D Design | 3 | Elective (5 credits)”
  - equivalencies[AP-MUSIC-THEORY|4 or 5]:  ⟵ “Music Theory | 4 or 5 | MUSC& 141 (5 credits); Placement into MUSC& 142”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | Humanities Distribution or Elective (5 credits); Use another method for placement”
  - equivalencies[AP-MICROECONOMICS|3, 4, or 5]:  ⟵ “Economics: Micro | 3, 4, or 5 | ECON& 201 (5 credits); placement into ECON& 202”
  - equivalencies[AP-MACROECONOMICS|3, 4, or 5]:  ⟵ “Economics: Macro | 3, 4, or 5 | ECON& 202 (5 credits)”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3, 4, or 5]:  ⟵ “Human Geography | 3, 4, or 5 | GEOG& 200 (5 credits)”
  - equivalencies[AP-PSYCHOLOGY|4 or 5]:  ⟵ “Psychology | 4 or 5 | PSYC& 100 (5 credits)”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | Elective (5 credits)”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, or 5]:  ⟵ “A/P African American Studies | 3, 4, or 5 | 5 credits of either Social Science or Humanities distribution credit”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|5]:  ⟵ “Government: Comparative Government & Politics | 5 | POLS& 101 and POLS& 201 (10 credits)”
  - … 37 more rows
### `386001775d0cc08a` Shoreline Community College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.shoreline.edu/placement/ap-ib-scores.aspx (sha256 1775c626013d)
- issues: score_column_not_scores
- checks: {"distinct_exams": 21, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[IB-ENGLISH-A-LITERATURE|English A Literature: 5, 6, 7]:  ⟵ “English A Literature: 5, 6, 7 | 5 credits equivalent to ENGL& 111, placement into ENGL&101”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|English A Language & Literature: 5, 6, 7]:  ⟵ “English A Language & Literature: 5, 6, 7 | 5 credits equivalent to ENGL&101, placement into ENGL&102”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|English A Literature or Language & Literature: 4]:  ⟵ “English A Literature or Language & Literature: 4 | 5 elective credits, use another method for placement”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|SL 4-5]:  ⟵ “Mathematics: Applications and Interpretation | SL 4-5 | 5 elective MATH credits”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL 4-5]:  ⟵ “Mathematics: Analysis and Approaches | SL 4-5 | 5 credits equivalent to MATH& 107, placement into MATH& 141”
  - equivalencies[IB-FRENCH|Language A: Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish]:  ⟵ “Language A: Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish | 4 | Elective (5 credits)”
  - equivalencies[IB-FRENCH|Language A: Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish]:  ⟵ “Language A: Arabic A, Chinese A, French A, Japanese A, Russian A, Spanish | 5, 6, 7 | Humanities distribution (5 credits)”
  - equivalencies[IB-FRENCH|Language B: Arabic B, Chinese B, French B, Japanese B, Russian B, Spanish B]:  ⟵ “Language B: Arabic B, Chinese B, French B, Japanese B, Russian B, Spanish B | 4 | Elective (5 credits)”
  - equivalencies[IB-FRENCH|Language B: French B, Japanese B, Spanish B]:  ⟵ “Language B: French B, Japanese B, Spanish B | 4 | Elective (5 credits)”
  - equivalencies[IB-FRENCH|French B]:  ⟵ “French B | 5 | FRCH &121 (5 credits)”
  - equivalencies[IB-FRENCH|French B]:  ⟵ “French B | 6 | FRCH &121, 122 (10 credits)”
  - equivalencies[IB-FRENCH|French B]:  ⟵ “French B | 7 | FRCH &121, &122, &123 (15 credits)”
  - equivalencies[IB-SPANISH|Spanish B]:  ⟵ “Spanish B | 5 | SPAN &121 (5 credits)”
  - equivalencies[IB-SPANISH|Spanish B]:  ⟵ “Spanish B | 6 | SPAN &121 and &122 (10 credits)”
  - equivalencies[IB-SPANISH|Spanish B]:  ⟵ “Spanish B | 7 | SPAN &121, &122, &123 (15 credits)”
  - equivalencies[IB-HISTORY|5, 6, 7]:  ⟵ “American History | 5, 6, 7 | HIST& 136, HIST& 137, HIST& 146, HIST& 147, or HIST& 148 (5 credits)”
  - equivalencies[IB-BIOLOGY|5, 6, 7]:  ⟵ “Biology | 5, 6, 7 | 5 biology credits, noted on transcript, counts toward Natural Science (Lab) distribution requirement”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5, 6, 7]:  ⟵ “Business & Management | 5, 6, 7 | Elective (5 credits)”
  - equivalencies[IB-CHEMISTRY|5, 6, 7]:  ⟵ “Chemistry | 5, 6, 7 | CHEM &121 (5 credits)”
  - equivalencies[IB-COMPUTER-SCIENCE|5, 6, 7]:  ⟵ “Computer Science | 5, 6, 7 | Elective (5 credits)”
  - equivalencies[IB-HISTORY|5, 6, 7]:  ⟵ “East/Southeast & Oceania History | 5, 6, 7 | EASIA 218 (5 credits)”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | 5 | ECON& 201 (5 credits)”
  - equivalencies[IB-ECONOMICS|6, 7]:  ⟵ “Economics | 6, 7 | ECON& 201 and ECON& 202 (10 credits)”
  - equivalencies[IB-HISTORY|5, 6, 7]:  ⟵ “European History | 5, 6, 7 | HIST& 116, HIST& 117, OR HIST& 118 (5 credits)”
  - equivalencies[IB-GEOGRAPHY|5, 6, 7]:  ⟵ “Geography | 5, 6, 7 | GEOG& 200 (5 credits)”
  - … 8 more rows
### `250350f3006f544c` Skagit Valley College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.skagit.edu/admissions-tuition/paying-for-college/cost-of-attendance.html (sha256 c1527f9ee183)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition & Fees: 6150 ⟵ “Tuition & Fees | $6,150 | $6,150”
  - column:Books & Supplies: 555 ⟵ “Books & Supplies | $555 | $555”
  - column:Living Expenses: 19200 ⟵ “Living Expenses | $19,200 | $9900”
  - column:Transportation: 2925 ⟵ “Transportation | $2,925 | $2,700”
  - column:Personal/Miscellaneous: 2070 ⟵ “Personal/Miscellaneous | $2,070 | $2,070”
  - column:Total: 30900 ⟵ “Total | $30,900 | $21,375”
  - column:Tuition & Fees: 6150 ⟵ “Tuition & Fees | $6,150 | $6,150”
  - column:Books & Supplies: 555 ⟵ “Books & Supplies | $555 | $555”
  - column:Living Expenses: 9900 ⟵ “Living Expenses | $19,200 | $9900”
  - column:Transportation: 2700 ⟵ “Transportation | $2,925 | $2,700”
  - column:Personal/Miscellaneous: 2070 ⟵ “Personal/Miscellaneous | $2,070 | $2,070”
  - column:Total: 21375 ⟵ “Total | $30,900 | $21,375”
### `2a05711c352f3215` South Puget Sound Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://pnp.spscc.edu/policies/stsv106 (sha256 16e4911c022c)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional judgements can be made on a case-by-case basis.”
### `97efc3aa525f0f76` South Puget Sound Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://pnp.spscc.edu/policies/stsv106 (sha256 16e4911c022c)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Students placed on Maximum Timeframe Suspension may appeal in accordance with the SAP Appeal procedures outlined in this policy.”
  - sentence: sap_appeal ⟵ “Appeal Timelines, Requirements, Outcomes, and Deadlines Timeline The Financial Aid Appeals Committee reviews all SAP Appeals submitted to the Financial Aid office.”
  - sentence: sap_appeal ⟵ “Appealable Reasons Extenuating Circumstances SAP appeals are typically considered when a student's academic progress is negatively impacted by unforeseen and documented circumstances.”
  - sentence: sap_appeal ⟵ “In these situations, students may be required to follow an approved Academic Plan following a successful SAP appeal.”
  - sentence: sap_appeal ⟵ “Upon receipt of a Change of Records SAP Appeal, the Financial Aid Office will review the updated academic record and re-determine SAP eligibility for the affected term.”
### `51c20810050f3cbb` South Seattle College — appeals 2026-27 [new] (labeled_in_source)
- source: https://southseattle.edu/financial-aid (sha256 6ffcd451864d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Get Your Funding Back If your financial aid has been cancelled for not meeting Satisfactory Academic Progress (SAP), you may appeal to reinstate your aid.”
### `717955da1da68b5b` South Seattle College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://southseattle.edu/financial-aid/cost-attend (sha256 78423ffdd741)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees*: 5520 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - column:Food and Housing: 19473 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - column:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - column:Transportation: 3069 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - column:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - column:Total Expected Cost of Attendance: 30498 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
  - column:Tuition and Fees*: 5520 ⟵ “Tuition and Fees* | $4,935 | $4,935 | $5,520 | $5,520”
  - column:Food and Housing: 10072 ⟵ “Food and Housing | $19,473 | $10,072 | $19,473 | $10,072”
  - column:Books, Course Materials, Supplies and Equipment: 528 ⟵ “Books, Course Materials, Supplies and Equipment | $528 | $528 | $528 | $528”
  - column:Transportation: 2832 ⟵ “Transportation | $3,069 | $2,832 | $3,069 | $2,832”
  - column:Miscellaneous Personal Expenses: 1908 ⟵ “Miscellaneous Personal Expenses | $1,908 | $1,908 | $1,908 | $1,908”
  - column:Total Expected Cost of Attendance: 20860 ⟵ “Total Expected Cost of Attendance | $29,913 | $20,275 | $30,498 | $20,860”
### `2916a6ea80c53e3a` Spokane Falls Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://sfcc.spokane.edu/How-to-Pay-for-College/Right-to-Know-Academic-Policies (sha256 884121f349a9)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://sfcc.spokane.edu/How-to-Pay-for-College/One-Big-Beautiful-Bill-Act,https://sfcc.spokane.edu/How-to-Pay-for-College/One-Big-Beautiful-Bill-Act/2024-25-FAFSA-FAQs
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Annual Cost of Attendance Cashier's Office Paying Your Tuition and Payment Plans Waivers Student Fees Explained Tax Credits How to Pay, Non-Financial Aid Receiving Your Money - Disbursements Right to Know - Academic Policies Financial Aid Special and Unusual Circumstances Tools and Links Financial Wellness Contact Financial Aid 3410 W.”
### `2a4ba2664d801b85` Spokane Falls Community College — appeals 2024-25 [new] (labeled_in_title)
- source: https://sfcc.spokane.edu/How-to-Pay-for-College/One-Big-Beautiful-Bill-Act/2024-25-FAFSA-FAQs (sha256 d0dea6ed6c95)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://sfcc.spokane.edu/How-to-Pay-for-College/One-Big-Beautiful-Bill-Act,https://sfcc.spokane.edu/How-to-Pay-for-College/Right-to-Know-Academic-Policies
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students who don't qualify as independent but aren't able to provide their parent(s)' information on the FAFSA® due to unusual circumstances can still submit the application and will be given provisional independent status.”
### `b29406b6a6d1c5c8` Spokane Falls Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://sfcc.spokane.edu/How-to-Pay-for-College/One-Big-Beautiful-Bill-Act (sha256 e331c02d0324)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://sfcc.spokane.edu/How-to-Pay-for-College/One-Big-Beautiful-Bill-Act/2024-25-FAFSA-FAQs,https://sfcc.spokane.edu/How-to-Pay-for-College/Right-to-Know-Academic-Policies
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Annual Cost of Attendance Cashier's Office Paying Your Tuition and Payment Plans Waivers Student Fees Explained Tax Credits How to Pay, Non-Financial Aid Receiving Your Money - Disbursements Right to Know - Academic Policies Financial Aid Special and Unusual Circumstances Tools and Links Financial Wellness Please Note This information reflects the most current guidance available and is subject to ”
### `c4accceaac094afb` Spokane Falls Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://sfcc.spokane.edu/How-to-Pay-for-College/Right-to-Know-Academic-Policies (sha256 884121f349a9)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Appeal Students placed on Financial Aid Suspension may submit an Appeal if they failed to make satisfactory academic progress due to extraordinary circumstances.”
  - sentence: sap_appeal ⟵ “Credits Completed or GPA Requirement Complete the Financial Aid Satisfactory Academic Progress Appeal.”
### `721f49f85bfc1a18` Tacoma Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tacomacc.edu/costs-admission/financial-aid/determiningfinancialneed (sha256 ab663372e4f9)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition/Fees* (12 credits): 5033 ⟵ “Tuition/Fees* (12 credits) | $ 5,033”
  - off_campus_not_with_family:Books and Supplies: 528 ⟵ “Books and Supplies | $ 528”
  - off_campus_not_with_family:Housing**: 12266 ⟵ “Housing** | $ 12,266”
  - off_campus_not_with_family:Food**: 5436 ⟵ “Food** | $ 5,436”
  - off_campus_not_with_family:Personal: 1908 ⟵ “Personal | $ 1,908”
  - off_campus_not_with_family:Transportation: 2790 ⟵ “Transportation | $ 2,790”
  - off_campus_not_with_family:Total***: 27961 ⟵ “Total*** | $ 27,961”
### `3603e94f36e26038` The Evergreen State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evergreen.edu/admissions-and-aid/financial-aid (sha256 490bc1b38645)
- issues: semantic_review_required, conflicting_sources:https://www.evergreen.edu/admissions-and-aid/financial-aid/applying-financial-aid,https://www.evergreen.edu/sites/default/files/2023-10/SAP_%20Policy%20_UG.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have a special circumstance, contact our office for more information.”
### `3bffab22d14bf22f` The Evergreen State College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evergreen.edu/admissions-and-aid/financial-aid/applying-financial-aid (sha256 35d055f26e0c)
- issues: semantic_review_required, conflicting_sources:https://www.evergreen.edu/admissions-and-aid/financial-aid,https://www.evergreen.edu/sites/default/files/2023-10/SAP_%20Policy%20_UG.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have a special circumstance, please contact our office for more information.”
### `41376b5acfbac07f` The Evergreen State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evergreen.edu/sites/default/files/2023-06/SAP-petition-cover-sheet.pdf (sha256 4b0caaba7b14)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appealing a Satisfactory Academic Progress Hold at Evergreen.”
  - sentence: sap_appeal ⟵ “RESOLUTION: Read the SAP Policy http://www.evergreen.edu/financialaid/docs/SAP-UG.pdf and if you feel that extenuating circumstances prevented you from making SAP you may appeal your case to the Professional Judgment Committee.”
### `7b25dafec4f124d9` The Evergreen State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evergreen.edu/sites/default/files/2023-10/SAP_%20Policy%20_UG.pdf (sha256 3c6b023e574f)
- issues: semantic_review_required, conflicting_sources:https://www.evergreen.edu/admissions-and-aid/financial-aid,https://www.evergreen.edu/admissions-and-aid/financial-aid/applying-financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The appeal must include a written statement from the student based on the unusual circumstances that caused the student to fail SAP.”
### `983cfc41e1e6b688` The Evergreen State College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evergreen.edu/admissions-and-aid/financial-aid/applying-financial-aid (sha256 35d055f26e0c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Your petition will be reviewed by the Professional Judgment Committee in your Financial Aid Office.”
### `b981505782ea3596` The Evergreen State College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.evergreen.edu/admissions-and-aid/cost-attendance/western-undergraduate-exchange (sha256 a71202f5ac87)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition and Fees: 32927 ⟵ “Tuition and Fees | $32,927”
  - column:WUE Award: 17555 ⟵ “WUE Award | $17,555”
  - column:Remaining Total: 15442 ⟵ “Remaining Total | $15,442”
### `6b139886525b069a` University of Puget Sound — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pugetsound.edu/satisfactory-academic-progress-sap-financial-aid-appeal-form (sha256 517f78b449eb)
- issues: semantic_review_required, conflicting_sources:https://www.pugetsound.edu/student-financial-services-current-undergraduate-students/eligibility-award-conditions/satisfactory
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Financial Aid Appeal Form | University of Puget Sound Skip to main content Utility Menu Visit Apply Give For you For You Future undergraduate students Future graduate students Current undergraduate students Current graduate students Parents & Families Faculty & Staff Community My Puget Sound Homepage link Mega menu button About Toggle submenu About Puget Sound ”
  - sentence: sap_appeal ⟵ “Events Community Resources Alumni News & Awards Contact Us For you For You Toggle submenu Future undergraduate students Future graduate students Current undergraduate students Current graduate students Parents & Families Faculty & Staff Community My Puget Sound Top Utility Menu Visit Apply Give Satisfactory Academic Progress (SAP) Financial Aid Appeal Form Puget Sound ID Number Name First Last Pug”
### `854cb523864c4ea9` University of Puget Sound — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.pugetsound.edu/student-financial-services-current-undergraduate-students/eligibility-award-conditions/satisfactory (sha256 5856cb773345)
- issues: semantic_review_required, conflicting_sources:https://www.pugetsound.edu/satisfactory-academic-progress-sap-financial-aid-appeal-form
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Eligibility for financial aid will be reinstated upon a successful appeal or when the student meets satisfactory academic progress requirements.”
### `39d88d29fdc74a3b` University of Puget Sound — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.pugetsound.edu/student-financial-services-parents/tuition-fees (sha256 fd9976986270)
- issues: conflicting_sources:https://www.pugetsound.edu/academics/school-occupational-therapy/ot-tuition-costs,https://www.pugetsound.edu/admission/student-financial-services/tuition-fees
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition (Full-Time Enrollment): 67550 ⟵ “Tuition (Full-Time Enrollment) | $33,775 | $33,775 | $67,550”
  - column:Comprehensive Student Fee: 638 ⟵ “Comprehensive Student Fee | $319 | $319 | $638”
  - column:Housing on Campus: 9854 ⟵ “Housing on Campus | $4,927 | $4,927 | $9,854”
  - column:Food on Campus: 8180 ⟵ “Food on Campus | $4,090 | $4,090 | $8,180”
  - column:Books & Supplies: 1000 ⟵ “Books & Supplies | $500 | $500 | $1,000”
  - column:Transportation: 1420 ⟵ “Transportation | $710 | $710 | $1,420”
  - column:Personal / Miscellaneous: 2124 ⟵ “Personal / Miscellaneous | $1,062 | $1,062 | $2,124”
  - column:Total: 90766 ⟵ “Total | $45,383 | $45,383 | $90,766”
### `568cca1369b0693a` University of Puget Sound — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.pugetsound.edu/academics/school-occupational-therapy/ot-tuition-costs (sha256 4b174515afc0)
- issues: arrangement_unlabeled, conflicting_sources:https://www.pugetsound.edu/admission/student-financial-services/tuition-fees,https://www.pugetsound.edu/student-financial-services-parents/tuition-fees
- checks: {"columns": 4, "rows": 5}
  - column:Tuition: 68280 ⟵ “Tuition | 68,280 | 59,745 | 19,285 | 147,310”
  - column:Comprehensive Student Fee(includes Distance Education fee): 294 ⟵ “Comprehensive Student Fee(includes Distance Education fee) | 294 | 294 | 294 | 882”
  - column:Books and Supplies: 1000 ⟵ “Books and Supplies | 1,000 | 1,000 | 100 | 2,100”
  - column:Loan Fees: 216 ⟵ “Loan Fees | 216* | 216* | 216* | 648”
  - column:Transportation: 500 ⟵ “Transportation | 500 | 500 | 500 | 1,500”
  - column:Tuition: 59745 ⟵ “Tuition | 68,280 | 59,745 | 19,285 | 147,310”
  - column:Comprehensive Student Fee(includes Distance Education fee): 294 ⟵ “Comprehensive Student Fee(includes Distance Education fee) | 294 | 294 | 294 | 882”
  - column:Books and Supplies: 1000 ⟵ “Books and Supplies | 1,000 | 1,000 | 100 | 2,100”
  - column:Loan Fees: 216 ⟵ “Loan Fees | 216* | 216* | 216* | 648”
  - column:Transportation: 500 ⟵ “Transportation | 500 | 500 | 500 | 1,500”
  - column:Tuition: 19285 ⟵ “Tuition | 68,280 | 59,745 | 19,285 | 147,310”
  - column:Comprehensive Student Fee(includes Distance Education fee): 294 ⟵ “Comprehensive Student Fee(includes Distance Education fee) | 294 | 294 | 294 | 882”
  - column:Books and Supplies: 100 ⟵ “Books and Supplies | 1,000 | 1,000 | 100 | 2,100”
  - column:Loan Fees: 216 ⟵ “Loan Fees | 216* | 216* | 216* | 648”
  - column:Transportation: 500 ⟵ “Transportation | 500 | 500 | 500 | 1,500”
  - column:Tuition: 147310 ⟵ “Tuition | 68,280 | 59,745 | 19,285 | 147,310”
  - column:Comprehensive Student Fee(includes Distance Education fee): 882 ⟵ “Comprehensive Student Fee(includes Distance Education fee) | 294 | 294 | 294 | 882”
  - column:Books and Supplies: 2100 ⟵ “Books and Supplies | 1,000 | 1,000 | 100 | 2,100”
  - column:Loan Fees: 648 ⟵ “Loan Fees | 216* | 216* | 216* | 648”
  - column:Transportation: 1500 ⟵ “Transportation | 500 | 500 | 500 | 1,500”
  - column:Total: 152440 ⟵ “Total |  |  |  | 152,440”
### `de08094d3191f8f2` University of Puget Sound — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.pugetsound.edu/admission/student-financial-services/tuition-fees (sha256 eb9a34390b94)
- issues: conflicting_sources:https://www.pugetsound.edu/academics/school-occupational-therapy/ot-tuition-costs,https://www.pugetsound.edu/student-financial-services-parents/tuition-fees
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition (Full-Time Enrollment): 67550 ⟵ “Tuition (Full-Time Enrollment) | $33,775 | $33,775 | $67,550”
  - column:Comprehensive Student Fee: 638 ⟵ “Comprehensive Student Fee | $319 | $319 | $638”
  - column:Housing on Campus: 9854 ⟵ “Housing on Campus | $4,927 | $4,927 | $9,854”
  - column:Food on Campus: 8180 ⟵ “Food on Campus | $4,090 | $4,090 | $8,180”
  - column:Books & Supplies: 1000 ⟵ “Books & Supplies | $500 | $500 | $1,000”
  - column:Transportation: 1420 ⟵ “Transportation | $710 | $710 | $1,420”
  - column:Personal / Miscellaneous: 2124 ⟵ “Personal / Miscellaneous | $1,062 | $1,062 | $2,124”
  - column:Total: 90766 ⟵ “Total | $45,383 | $45,383 | $90,766”
### `e86ee4d9a6a00c9b` University of Washington-Bothell Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwb.edu/financial-aid/satisfactory-academic-progress/satisfactory-academic-progress (sha256 27f028ffbf0f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “How to Re-Establish Eligibility If you did not meet the progress requirements because you had special circumstances, you may file an appeal with our office.”
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate unusual circumstances beyond your control that are not likely to recur in the immediate future.”
  - sentence: need_based_special_circumstances ⟵ “How to reestablish eligibility If you did not meet the progress requirements because you had special circumstances you may file an appeal with our office.”
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate unusual circumstances beyond your control that are not likely to recur in the immediate future.”
### `36c01c09e74fbdf4` University of Washington-Seattle Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.washington.edu/financialaid/ (sha256 691eb166ad99)
- issues: semantic_review_required, conflicting_sources:https://www.washington.edu/financialaid/cost-of-attendance/,https://www.washington.edu/financialaid/key-policies-information/appeals-special-circumstances/,https://www.washington.edu/financialaid/key-policies-information/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Cost of Attendance Apply for & Receive Aid Key Dates FAQs Key Policies & Info Appeals & Special Circumstances Featured forms Satisfactory Academic Progress To be eligible for financial aid, students must maintain satisfactory academic progress standards.”
  - sentence: need_based_special_circumstances ⟵ “If you had special circumstances and didn’t meet the requirements, you may file an appeal.”
### `3a47b8267faaf728` University of Washington-Seattle Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.washington.edu/financialaid/key-policies-information/appeals-special-circumstances/ (sha256 f1b4bf9de4ed)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals Process, By Circumstance Appeals By Circumstance Satisfactory Academic Progress If you did not meet the satisfactory academic progress requirements because you had special circumstances you may file an appeal with our office.”
### `680c9ccdb9ef6f63` University of Washington-Seattle Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.washington.edu/financialaid/cost-of-attendance/ (sha256 d79da0847e06)
- issues: semantic_review_required, conflicting_sources:https://www.washington.edu/financialaid/,https://www.washington.edu/financialaid/key-policies-information/appeals-special-circumstances/,https://www.washington.edu/financialaid/key-policies-information/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If your financial aid offer is not enough to cover your expenses, you have several options: Talk to one of our counselors to see if any adjustments can be made to your aid offer If your and your family’s financial situation has changed since you completed the FAFSA, then you can let our office know by completing Revision Request for Change in Financial Situation If you incur expenses during the sc”
### `70a9a91309858e1c` University of Washington-Seattle Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.washington.edu/financialaid/key-policies-information/appeals-special-circumstances/ (sha256 f1b4bf9de4ed)
- issues: semantic_review_required, conflicting_sources:https://www.washington.edu/financialaid/,https://www.washington.edu/financialaid/cost-of-attendance/,https://www.washington.edu/financialaid/key-policies-information/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate unusual circumstances beyond your control that are not likely to recur in the immediate future.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances: If you cannot provide parent information due to unusual family circumstances, you may appeal to apply for aid without parental information.”
  - sentence: need_based_special_circumstances ⟵ “For this purpose, an unusual circumstance includes, but is not limited to, a permanent, irreconcilable break in the relationship with the parent(s) due to abuse, abandonment, or extreme mistreatment.”
  - sentence: need_based_special_circumstances ⟵ “Changes to your aid offer Change Parent’s Contribution If your parents are not able to make the contribution calculated for them, they may provide us with more comprehensive information about their situation and ask for a recalculation on the Revision Request for Change in Financial Situation (see Undergraduate forms or Graduate forms).”
  - sentence: need_based_special_circumstances ⟵ “Change Student’s Contribution If you are not able to make the expected contribution or if you no longer have the earnings, benefits, or other support you reported, explain on the Revision Request for Change in Financial Situations (see Undergraduate forms or Graduate forms).”
### `dc9868840b62c7f2` University of Washington-Seattle Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.washington.edu/financialaid/key-policies-information/satisfactory-academic-progress/ (sha256 82db02e48398)
- issues: semantic_review_required, conflicting_sources:https://www.washington.edu/financialaid/,https://www.washington.edu/financialaid/cost-of-attendance/,https://www.washington.edu/financialaid/key-policies-information/appeals-special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “How to re-establish eligibility If you did not meet the progress requirements because you had special circumstances, you may file an appeal with our office.”
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate unusual circumstances beyond your control that are not likely to recur in the immediate future.”
  - sentence: need_based_special_circumstances ⟵ “How to re-establish eligibility If you did not meet the progress requirements because you had special circumstances, you may file an appeal with our office.”
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate unusual circumstances beyond your control that are not likely to recur in the immediate future.”
### `84452af320907f77` University of Washington-Seattle Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://admit.washington.edu/costs/coa/ (sha256 3f6a19836688)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 3, "rows": 8}
  - with_parents_or_family:Books & course supplies: 900 ⟵ “Books & course supplies | $900 | $900 | $900”
  - with_parents_or_family:Housing & food: 6156 ⟵ “Housing & food | $6,156 | $18,858 | $23,199”
  - with_parents_or_family:Personal/miscellaneous: 2508 ⟵ “Personal/miscellaneous | $2,508 | $2,508 | $2,508”
  - with_parents_or_family:Transportation: 1074 ⟵ “Transportation | $1,074 | $1,074 | $1,581”
  - with_parents_or_family:Resident tuition: 13406 ⟵ “Resident tuition | $13,406 | $13,406 | $13,406”
  - with_parents_or_family:Resident total costs: 24044 ⟵ “Resident total costs | $24,044 | $36,746 | $41,594”
  - with_parents_or_family:Non-resident tuition: 44460 ⟵ “Non-resident tuition | $44,460 | $44,460 | $44,460”
  - with_parents_or_family:Non-resident total costs: 55098 ⟵ “Non-resident total costs | $55,098 | $67,800 | $72,648”
  - column:Books & course supplies: 900 ⟵ “Books & course supplies | $900 | $900 | $900”
  - column:Housing & food: 18858 ⟵ “Housing & food | $6,156 | $18,858 | $23,199”
  - column:Personal/miscellaneous: 2508 ⟵ “Personal/miscellaneous | $2,508 | $2,508 | $2,508”
  - column:Transportation: 1074 ⟵ “Transportation | $1,074 | $1,074 | $1,581”
  - column:Resident tuition: 13406 ⟵ “Resident tuition | $13,406 | $13,406 | $13,406”
  - column:Resident total costs: 36746 ⟵ “Resident total costs | $24,044 | $36,746 | $41,594”
  - column:Non-resident tuition: 44460 ⟵ “Non-resident tuition | $44,460 | $44,460 | $44,460”
  - column:Non-resident total costs: 67800 ⟵ “Non-resident total costs | $55,098 | $67,800 | $72,648”
  - column:Books & course supplies: 900 ⟵ “Books & course supplies | $900 | $900 | $900”
  - column:Housing & food: 23199 ⟵ “Housing & food | $6,156 | $18,858 | $23,199”
  - column:Personal/miscellaneous: 2508 ⟵ “Personal/miscellaneous | $2,508 | $2,508 | $2,508”
  - column:Transportation: 1581 ⟵ “Transportation | $1,074 | $1,074 | $1,581”
  - column:Resident tuition: 13406 ⟵ “Resident tuition | $13,406 | $13,406 | $13,406”
  - column:Resident total costs: 41594 ⟵ “Resident total costs | $24,044 | $36,746 | $41,594”
  - column:Non-resident tuition: 44460 ⟵ “Non-resident tuition | $44,460 | $44,460 | $44,460”
  - column:Non-resident total costs: 72648 ⟵ “Non-resident total costs | $55,098 | $67,800 | $72,648”
### `693fb8aa843b4f9d` University of Washington-Seattle Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admit.washington.edu/apply/first-year/exams-for-credit/ib/ (sha256 d0268d5af07d)
- issues: conflicting_sources:https://admit.washington.edu/apply/first-year/exams-for-credit/ib-archive/,https://admit.washington.edu/apply/transfer/exams-for-credit/ib/
- checks: {"distinct_exams": 4, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|HL 4, 5, 6, 7]:  ⟵ “English A Language and Literature | HL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LITERATURE|HL 4, 5, 6, 7]:  ⟵ “English A Literature | HL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|SL 4, 5, 6, 7]:  ⟵ “English A Language and Literature | SL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LITERATURE|SL 4, 5, 6, 7]:  ⟵ “English A Literature | SL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|HL 6, 7]:  ⟵ “Mathematics: analysis and approaches | HL | 6, 7 | MATH 124 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|HL 4, 5]:  ⟵ “Mathematics: analysis and approaches | HL | 4, 5 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|HL 5, 6, 7]:  ⟵ “Mathematics: applications and interpretations | HL | 5, 6, 7 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|HL 4]:  ⟵ “Mathematics: applications and interpretations | HL | 4 | MATH 108 (5 CR.) | NSc”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL 6, 7]:  ⟵ “Mathematics: analysis and approaches | SL | 6, 7 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL 4, 5]:  ⟵ “Mathematics: analysis and approaches | SL | 4, 5 | MATH 109 (5 CR.) | NSc”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|SL 5, 6, 7]:  ⟵ “Mathematics: applications and interpretations | SL | 5, 6, 7 | MATH 108 (5 CR.) | NSc”
### `8a3f13d80869f3b3` University of Washington-Seattle Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admit.washington.edu/apply/transfer/exams-for-credit/ib/ (sha256 5ecb57b5268a)
- issues: conflicting_sources:https://admit.washington.edu/apply/first-year/exams-for-credit/ib-archive/,https://admit.washington.edu/apply/first-year/exams-for-credit/ib/
- checks: {"distinct_exams": 4, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|HL 4, 5, 6, 7]:  ⟵ “English A Language and Literature | HL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LITERATURE|HL 4, 5, 6, 7]:  ⟵ “English A Literature | HL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|SL 4, 5, 6, 7]:  ⟵ “English A Language and Literature | SL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-ENGLISH-A-LITERATURE|SL 4, 5, 6, 7]:  ⟵ “English A Literature | SL | 4, 5, 6, 7 | ENGL 107 (5 CR.) | ”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|HL 6, 7]:  ⟵ “Mathematics: analysis and approaches | HL | 6, 7 | MATH 124 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|HL 4, 5]:  ⟵ “Mathematics: analysis and approaches | HL | 4, 5 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|HL 5, 6, 7]:  ⟵ “Mathematics: applications and interpretations | HL | 5, 6, 7 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|HL 4]:  ⟵ “Mathematics: applications and interpretations | HL | 4 | MATH 108 (5 CR.) | NSc”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL 6, 7]:  ⟵ “Mathematics: analysis and approaches | SL | 6, 7 | MATH 120 (5 CR.) | NSc, RSN”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL 4, 5]:  ⟵ “Mathematics: analysis and approaches | SL | 4, 5 | MATH 109 (5 CR.) | NSc”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|SL 5, 6, 7]:  ⟵ “Mathematics: applications and interpretations | SL | 5, 6, 7 | MATH 108 (5 CR.) | NSc”
### `ad45b7fc76ed39aa` University of Washington-Seattle Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admit.washington.edu/apply/first-year/exams-for-credit/ib-archive/ (sha256 2b79f6239ca6)
- issues: rows_without_score, conflicting_sources:https://admit.washington.edu/apply/first-year/exams-for-credit/ib/,https://admit.washington.edu/apply/transfer/exams-for-credit/ib/
- checks: {"distinct_exams": 16, "equivalencies": 28, "rows_without_score": 2}
  - equivalencies[IB-HISTORY|7,6,5]:  ⟵ “African History | 7,6,5 | HIST 108 (5 cr.) | Counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-HISTORY|7,6,5]:  ⟵ “American History | 7,6,5 | HSTAA 101 (5 cr.) | Counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|7,6,5]:  ⟵ “Anthropology | 7,6,5 | ANTH 202 (5 cr.) | Counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-BIOLOGY|7,6,5]:  ⟵ “Biology | 7,6,5 | BIOL 161-162 (10 cr.) | Counts toward Natural World general education requirement for graduation.”
  - equivalencies[IB-BUSINESS-MANAGEMENT|7,6,5]:  ⟵ “Business and Management | 7,6,5 | No credit | ”
  - equivalencies[IB-CHEMISTRY|7]:  ⟵ “Chemistry | 7 | CHEM 142, 152, 162 (5, 5, 5) | General chemistry for science and engineering majors. Counts toward Natural World general education requirement for graduation. CHEM 142 also satisfies Quantitative and Symbolic Reasoning graduation requirement. Note Students with IB scores of 5, 6, or ”
  - equivalencies[IB-CHEMISTRY|6]:  ⟵ “Chemistry | 6 | CHEM 142, 152 (5, 5) | General chemistry for science and engineering majors. Counts toward Natural World general education requirement for graduation. CHEM 142 also satisfies Quantitative and Symbolic Reasoning graduation requirement. Note Students with IB scores of 5, 6, or 7 on the”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 142 (5) | General chemistry for science and engineering majors. Counts toward Natural World general education requirement for graduation. Note Students with IB scores of 5, 6, or 7 on the Higher Level Chemistry exam who plan to major in chemistry or biochemistry are strongly enc”
  - equivalencies[IB-COMPUTER-SCIENCE|7,6,5]:  ⟵ “Computer Science | 7,6,5 | CSE 100 (5 cr.) | Satisfies Quantitative and Symbolic Reasoning graduation requirement.”
  - equivalencies[IB-HISTORY|7,6,5]:  ⟵ “East/Southeast Asia and Oceania History | 7,6,5 | HSTAS 108 (5 cr.) | Counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-ECONOMICS|7,6]:  ⟵ “Economics | 7,6 | ECON 200, 201 (10 cr.) | Satisfies Quantitative and Symbolic Reasoning graduation requirement and/or counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | 5 | ECON 200 (5 cr.) | Satisfies Quantitative and Symbolic Reasoning graduation requirement or counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-HISTORY|7,6,5]:  ⟵ “European History | 7,6,5 | HIST 113 (5 cr.) | Counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French A |  | No credit | ”
  - equivalencies[IB-FRENCH|7]:  ⟵ “French B | 7 | FRENCH 201, 202, 203 (15 cr.) | Satisfies foreign language requirement, and credits count toward Visual, Literary, and Performing Arts general education requirement for graduation.”
  - equivalencies[IB-FRENCH|6]:  ⟵ “French B | 6 | FRENCH 201, 202 (10 cr.) | ”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French B | 5 | FRENCH 201 (5 cr.) | ”
  - equivalencies[IB-GEOGRAPHY|7,6,5]:  ⟵ “Geography | 7,6,5 | GEOG 100 (5 cr.) | Counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-LATIN|7,6,5]:  ⟵ “Latin | 7,6,5 | LATIN 305, 306, 307 (15 cr.) | Satisfies foreign language requirement, and credits count toward Visual, Literary, and Performing Arts general education requirement for graduation.”
  - equivalencies[IB-MUSIC|7,6,5]:  ⟵ “Music | 7,6,5 | MUSIC 120 (5 cr.) | Counts toward Visual, Literary, and Performing Arts general education requirement for graduation.”
  - equivalencies[IB-PHILOSOPHY|7,6,5]:  ⟵ “Philosophy | 7,6,5 | No credit | ”
  - equivalencies[IB-PHYSICS|7,6,5]:  ⟵ “Physics | 7,6,5 | PHYS 114/117, 115/118, 116/119 (15 cr.) | Satisfies Natural World general education requirement for graduation. PHYS 114 also satisfies Quantitative and Symbolic Reasoning basic skills requirement for graduation.”
  - equivalencies[IB-PSYCHOLOGY|7,6,5]:  ⟵ “Psychology | 7,6,5 | PSYCH 101 (5 cr.) | Counts toward Individuals & Societies general education requirement for graduation.”
  - equivalencies[IB-SPANISH|None]:  ⟵ “Spanish A |  | No credit | ”
  - equivalencies[IB-SPANISH|7]:  ⟵ “Spanish B | 7 | SPAN 201, 202, 203 (15 cr.) | Satisfies foreign language requirement, and credits count toward general education requirement for graduation.”
  - … 3 more rows
### `0c082e865ef03a79` University of Washington-Tacoma Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tacoma.uw.edu/finaid/sap (sha256 0d798f006277)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate unusual circumstances beyond your control that are not likely to recur in the immediate future.”
### `a514267d19e63595` University of Washington-Tacoma Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tacoma.uw.edu/finaid/sap (sha256 0d798f006277)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal If you did not meet the progress requirements because you had special circumstances, you may file a Satisfactory Academic Progress appeal with our office.”
### `11beb4bde6e285d8` University of Washington-Tacoma Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tacoma.uw.edu/finaid/cost-attendance (sha256 762464978f4d)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 3, "rows": 8}
  - with_parents_or_family:Textbooks & course supplies: 900 ⟵ “Textbooks & course supplies | $900 | $900 | $900”
  - with_parents_or_family:Housing/food: 6156 ⟵ “Housing/food | $6,156 | $17,631 | $21,354”
  - with_parents_or_family:Personal & miscellaneous: 2508 ⟵ “Personal & miscellaneous | $2,508 | $2,508 | $2,508”
  - with_parents_or_family:Transportation: 1074 ⟵ “Transportation | $1,074 | $1,074 | $1,581”
  - with_parents_or_family:Resident Tuition*: 13881 ⟵ “Resident Tuition* | $13,881 | $13,881 | $13,881”
  - with_parents_or_family:Resident Total Costs: 24519 ⟵ “Resident Total Costs | $24,519 | $35,994 | $40,224”
  - with_parents_or_family:Non-Resident Tuition*: 45111 ⟵ “Non-Resident Tuition* | $45,111 | $45,111 | $45,111”
  - with_parents_or_family:Non-Resident Total Costs: 55749 ⟵ “Non-Resident Total Costs | $55,749 | $67,224 | $71,454”
  - column:Textbooks & course supplies: 900 ⟵ “Textbooks & course supplies | $900 | $900 | $900”
  - column:Housing/food: 17631 ⟵ “Housing/food | $6,156 | $17,631 | $21,354”
  - column:Personal & miscellaneous: 2508 ⟵ “Personal & miscellaneous | $2,508 | $2,508 | $2,508”
  - column:Transportation: 1074 ⟵ “Transportation | $1,074 | $1,074 | $1,581”
  - column:Resident Tuition*: 13881 ⟵ “Resident Tuition* | $13,881 | $13,881 | $13,881”
  - column:Resident Total Costs: 35994 ⟵ “Resident Total Costs | $24,519 | $35,994 | $40,224”
  - column:Non-Resident Tuition*: 45111 ⟵ “Non-Resident Tuition* | $45,111 | $45,111 | $45,111”
  - column:Non-Resident Total Costs: 67224 ⟵ “Non-Resident Total Costs | $55,749 | $67,224 | $71,454”
  - column:Textbooks & course supplies: 900 ⟵ “Textbooks & course supplies | $900 | $900 | $900”
  - column:Housing/food: 21354 ⟵ “Housing/food | $6,156 | $17,631 | $21,354”
  - column:Personal & miscellaneous: 2508 ⟵ “Personal & miscellaneous | $2,508 | $2,508 | $2,508”
  - column:Transportation: 1581 ⟵ “Transportation | $1,074 | $1,074 | $1,581”
  - column:Resident Tuition*: 13881 ⟵ “Resident Tuition* | $13,881 | $13,881 | $13,881”
  - column:Resident Total Costs: 40224 ⟵ “Resident Total Costs | $24,519 | $35,994 | $40,224”
  - column:Non-Resident Tuition*: 45111 ⟵ “Non-Resident Tuition* | $45,111 | $45,111 | $45,111”
  - column:Non-Resident Total Costs: 71454 ⟵ “Non-Resident Total Costs | $55,749 | $67,224 | $71,454”
### `0665e56314c6cf46` Walla Walla University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wallawalla.edu/admissions-and-aid/student-financial-services/financial-aid (sha256 9da343c36712)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “If you feel that the FAFSA results don't reflect your unique financial situation, you can dispute them through a process called "professional judgement." This process gives the WWU financial aid office the authority to take into account your unique financial circumstances and compensate for them.”
  - sentence: professional_judgment ⟵ “If you believe that the SAI doesn't accurately reflect your specific financial situation, call us to talk about the professional judgement process and what additional documentation is required.”
  - sentence: professional_judgment ⟵ “Some of the situations WWU can consider as part of a professional judgement: There are other children in elementary or secondary school that parents paid tuition.”
### `1114e0cff8a21d20` Walla Walla University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wallawalla.edu/admissions-and-aid/student-financial-services/financial-aid/how-to-apply/satisfactory-academic-progress-sap-requirements (sha256 5a9b74efb44a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “FINANCIAL AID PROBATION - The status assigned to a student who fails to make satisfactory academic progress and who has appealed and been approved to receive financial aid the following quarter enrolled.”
  - sentence: sap_appeal ⟵ “In future terms, if a student fails SAP, they may appeal the Financial Aid Committee.”
  - sentence: sap_appeal ⟵ “Graduate Student SAP Policy Graduate Student SAP Policy Satisfactory Academic Progress (SAP) Appeal Form - Submit Online Overview Students must maintain satisfactory academic progress toward degree completion to receive financial aid from Federal, State, or WWU programs.”
  - sentence: sap_appeal ⟵ “FINANCIAL AID PROBATION - The status assigned to a student who fails to make satisfactory academic progress and who has appealed and been approved to receive financial aid the following quarter enrolled.”
### `f8f906dda9b8af9b` Walla Walla University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.wallawalla.edu/admissions-and-aid/student-financial-services/your-student-account/tuition-refunds (sha256 af377412ffda)
- issues: arrangement_unlabeled, conflicting_sources:https://www.wallawalla.edu/admissions-and-aid/student-financial-services/estimated-expenses
- checks: {"columns": 2, "rows": 3}
  - column:First, tuition is calculated for 13 credits: 10224 ⟵ “First, tuition is calculated for 13 credits | $10,224 | $10,224.00”
  - column:Next, tuition for 11 credits is calculated (11 x $852): 9372 ⟵ “Next, tuition for 11 credits is calculated (11 x $852) | 9,372 | ”
  - column:The difference between 13 hours and 11 hours of tuition: 852 ⟵ “The difference between 13 hours and 11 hours of tuition | 852 | ”
  - column:First, tuition is calculated for 13 credits: 10224.0 ⟵ “First, tuition is calculated for 13 credits | $10,224 | $10,224.00”
  - column:TOTAL TUITION CHARGE FOR THIS STUDENT: 9585.0 ⟵ “TOTAL TUITION CHARGE FOR THIS STUDENT |  | $9,585.00”
  - column:NET TUITION ADJUSTMENT FOR THIS TRANSACTION ($9,585.00 less $7,242.00 previous charged): 2616.0 ⟵ “NET TUITION ADJUSTMENT FOR THIS TRANSACTION ($9,585.00 less $7,242.00 previous charged) |  | $2,616.00”
### `fbd6961d9641f6e1` Walla Walla University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wallawalla.edu/admissions-and-aid/student-financial-services/estimated-expenses (sha256 e846c2c30999)
- issues: arrangement_unlabeled, conflicting_sources:https://www.wallawalla.edu/admissions-and-aid/student-financial-services/your-student-account/tuition-refunds
- checks: {"columns": 2, "components_reconcile": true, "rows": 11}
  - on_campus:Tuition (full-time,12-16 hours): 35460 ⟵ “Tuition (full-time,12-16 hours) | $35,460 | $35,460”
  - on_campus:General Fee (includes ASWWU Dues): 1458 ⟵ “General Fee (includes ASWWU Dues) | $1,458 | $1,458”
  - on_campus:Residence Hall Rent*: 5658 ⟵ “Residence Hall Rent* | $5,658 | -”
  - on_campus:Estimated Meal Plan: 5238 ⟵ “Estimated Meal Plan | $5,238 | -”
  - on_campus:Addiitional Food Outside of Meal Plan: 588 ⟵ “Addiitional Food Outside of Meal Plan | $588 | ”
  - on_campus:Estimated Loan Fees: 60 ⟵ “Estimated Loan Fees | $60 | $60”
  - on_campus:Estimated Books: 765 ⟵ “Estimated Books | $765 | $765”
  - on_campus:Estimated Misc/Personal Expenses: 1800 ⟵ “Estimated Misc/Personal Expenses | $1,800 | $1,800”
  - on_campus:Estimated Transportation: 1677 ⟵ “Estimated Transportation | $1,677 | $1,677”
  - on_campus:Total Cost of Attendance: 52704 ⟵ “Total Cost of Attendance | $52,704 | $52,704”
  - on_campus:Total Estimated WWU Charges: 47814 ⟵ “Total Estimated WWU Charges | $47,814 | $36,918”
  - column:Tuition (full-time,12-16 hours): 35460 ⟵ “Tuition (full-time,12-16 hours) | $35,460 | $35,460”
  - column:General Fee (includes ASWWU Dues): 1458 ⟵ “General Fee (includes ASWWU Dues) | $1,458 | $1,458”
  - column:Off-Campus Housing: 5658 ⟵ “Off-Campus Housing |  | $5,658”
  - column:Off-Campus Food: 5826 ⟵ “Off-Campus Food |  | $5,826”
  - column:Estimated Loan Fees: 60 ⟵ “Estimated Loan Fees | $60 | $60”
  - column:Estimated Books: 765 ⟵ “Estimated Books | $765 | $765”
  - column:Estimated Misc/Personal Expenses: 1800 ⟵ “Estimated Misc/Personal Expenses | $1,800 | $1,800”
  - column:Estimated Transportation: 1677 ⟵ “Estimated Transportation | $1,677 | $1,677”
  - column:Total Cost of Attendance: 52704 ⟵ “Total Cost of Attendance | $52,704 | $52,704”
  - column:Total Estimated WWU Charges: 36918 ⟵ “Total Estimated WWU Charges | $47,814 | $36,918”
### `0bf1aeb90614062b` Washington State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.wsu.edu/special-circumstances-appeal/ (sha256 2e09bd948f14)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.wsu.edu/sap-handbook/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “What is a Professional Judgement Request?”
  - sentence: professional_judgment ⟵ “A professional judgment request is when the FAFSA or WASFA does not accurately reflect you and your family’s current financial situation or budget expenses.”
  - sentence: professional_judgment ⟵ “To correct this, you may apply for two types of professional judgement: Special Circumstances Appeals and Academic Year Revision Requests.”
### `3ab5fcdca2b87e2b` Washington State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.wsu.edu/sap-handbook/ (sha256 99e915d0fd93)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 14}
  - sentence: sap_appeal ⟵ “If the student falls below the requirement they will be disqualified and may file a SAP appeal. 2.1.3 Maximum Time Frame Regulation The federal policy states that for an undergraduate program measured in credit hours, a period no longer than 150 percent of the published length of the program is the maximum timeframe. (FSA Handbook, pg. 1.10).”
  - sentence: sap_appeal ⟵ “If the appeal is approved, then the student will receive aid until they receive their first baccalaureate degree. 4.2.3 Submitting a SAP Appeal The appeal process is completed entirely online through SubmitSFSDocs.wsu.edu.”
  - sentence: sap_appeal ⟵ “Not all circumstances will warrant an exception to the SAP policy. 4.2.5 Appeal Approval If a student’s appeal is approved, they will be sent an academic plan stating the conditions they must meet to retain eligibility.”
  - sentence: sap_appeal ⟵ “For the situation where a student is eligible for financial aid at the beginning of the term has not had all their aid disbursed but then becomes academically deficient at the end of the term: This student would need to file a SAP appeal in order to receive future financial aid consideration.”
  - sentence: sap_appeal ⟵ “Considerations Additional Considerations If a student has completed the online SAP appeal process and is denied financial aid funding, yet the student believes they have extenuating circumstances that were not addressed in the original appeal, the student may submit additional and/or new documentation detailing these circumstances to sapappeal@wsu.edu for committee review.”
  - sentence: sap_appeal ⟵ “Students will then be notified if they met satisfactory academic progress and if an appeal needs to be submitted by them for aid consideration.”
### `73916481b64cd853` Washington State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.wsu.edu/special-circumstances-appeal/ (sha256 2e09bd948f14)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Schedule A from the tax return for your chosen appeal time frame *Please note: If your SAI is “0”, then you will be considered for a budget increase for an additional loan, if eligible, with the maximum limit of $1,500 after accounting for the Income Protection Allowance (IPA).”
### `83cfe9bc36a74d79` Washington State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.wsu.edu/sap-handbook/ (sha256 99e915d0fd93)
- issues: semantic_review_required, conflicting_sources:https://financialaid.wsu.edu/special-circumstances-appeal/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “When a student loses FSA eligibility because he failed to make satisfactory progress, if the school permits appeals, he may appeal that result on the basis of: his injury or illness, the death of a relative, or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “When a student loses FSA eligibility because he failed to make satisfactory progress, if the school permits appeals, he may appeal that result on the basis of: his injury or illness, the death of a relative, or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “When a student loses FSA eligibility because he failed to make satisfactory progress, if the school permits appeals, he may appeal that result on the basis of: his injury or illness, the death of a relative, or other special circumstances.”
### `ab958387b9b41dc3` Washington State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.wsu.edu/sap-handbook/ (sha256 99e915d0fd93)
- issues: semantic_review_required, conflicting_sources:https://financialaid.wsu.edu/special-circumstances-appeal/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If a student in a maximum time-frame deficiency submits an appeal and the appeal is approved per professional judgment, the academic plan terms will only allow funding for the classes that required based on the student’s advisor statement.”
  - sentence: professional_judgment ⟵ “If a student in a maximum time-frame disqualification submits an appeal and the appeal is approved per professional judgment, the academic plan terms will only allow funding for the required classes based on the student’s adviser statement.”
### `ace1e73eb04c7f78` Washington State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.wsu.edu/special-circumstances-appeal/ (sha256 2e09bd948f14)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.wsu.edu/sap-handbook/
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances & Revision Requests | Student Financial Services | Washington State University Skip to content Washington State University Student Financial Aid information, updates and tools for the WSU community.”
  - sentence: need_based_special_circumstances ⟵ “News & Updates Events & Outreach For Parents Special Circumstances & Revision Requests Need immediate assistance?”
  - sentence: need_based_special_circumstances ⟵ “Revision requests and special circumstances appeals may take 10-20 business days to process.”
  - sentence: need_based_special_circumstances ⟵ “Revision Request Examples You may qualify for an Academic Year Revision in the following circumstances: Automotive repairs Childcare expenses Disability-related expenses Graduate student enrolled below full time Non-resident graduate without assistantship Rent Special Fees (ie: EMBA/online MBA or winter session fees) Transportation Travel Apply for a Revision Request Special Circumstances Appeals ”
  - sentence: need_based_special_circumstances ⟵ “In some cases, we are able to make adjustments based on special circumstances that have occurred between your submitted tax data and the present day.”
  - sentence: need_based_special_circumstances ⟵ “You may submit multiple special circumstances in your appeal (“change in income”, “parent in college”, etc.), but no more than one will be accepted for a given year.”
### `a5487516111d8b6d` Washington State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://admission.wsu.edu/apply/application-process/ap-credits/ (sha256 90b44509a6f5)
- issues: course_column_missing
- checks: {"distinct_exams": 37, "equivalencies": 109, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | CES 131 | 3 | ”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4]:  ⟵ “African American Studies | 4 | CES 131 | 3 | ”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|5]:  ⟵ “African American Studies | 5 | CES 131 | 3 | ”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art Drawing | 3 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Studio Art Drawing | 4 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-DRAWING|5]:  ⟵ “Studio Art Drawing | 5 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Studio Art 2D Design | 3 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “Studio Art 2D Design | 4 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-2-D-ART-DESIGN|5]:  ⟵ “Studio Art 2D Design | 5 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Studio Art 3D Design | 3 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “Studio Art 3D Design | 4 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-3-D-ART-DESIGN|5]:  ⟵ “Studio Art 3D Design | 5 | Fine Arts Elective | 3 | ARTS”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | Biology Elective (1 lab granted) | 4 | BSCI”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | Biology 106, 107 (2 labs granted) (For Science and pre-prof majors) | 8 | BSCI”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | Biology 106, 107 (2 labs granted) (For Science and pre-prof majors) | 8 | BSCI”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3]:  ⟵ “Business with Personal Finance | 3 | Finance 223 | 3 | QUAN”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|4]:  ⟵ “Business with Personal Finance | 4 | Finance 223 | 3 | QUAN”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|5]:  ⟵ “Business with Personal Finance | 5 | Finance 223 | 3 | QUAN”
  - equivalencies[AP-CALCULUS-AB|2]:  ⟵ “Calculus AB | 2 | Placement into Mathematics 140 (For Life Scientists) or Mathematics 171 (For Science/Engineering majors) or Mathematics 202 (For Business and Economics) | N/A | Not applicable”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | Mathematics 171 (For Science/Engineering majors) | 4 | QUAN”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 | Mathematics 171 (For Science/Engineering majors) | 4 | QUAN”
  - equivalencies[AP-CALCULUS-AB|5]:  ⟵ “Calculus AB | 5 | Mathematics 171 (For Science/Engineering majors) | 4 | QUAN”
  - equivalencies[AP-CALCULUS-BC|2]:  ⟵ “Calculus BC | 2 | (With subgrade score of 3, 4, 5) Mathematics 171 (For Science/Engineering majors) | 4 | QUAN”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | Mathematics 171, 172 (For Science/Engineering majors) | 8 | QUAN”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | Mathematics 171, 172 (For Science/Engineering majors) | 8 | QUAN”
  - … 84 more rows
### `ebceb77b56ac98a0` Washington State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admission.wsu.edu/apply/application-process/ib-credits/ (sha256 34cd9a062aa8)
- issues: course_column_missing
- checks: {"distinct_exams": 25, "equivalencies": 68, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|HL 4+]:  ⟵ “Biology | HL 4+ | Biology 106, 107 (2 labs granted) (Sequence for Science/Health majors) | 8 | BSCI”
  - equivalencies[IB-BIOLOGY|SL 4+]:  ⟵ “Biology | SL 4+ | Biology 102 | 4 | BSCI”
  - equivalencies[IB-BUSINESS-MANAGEMENT|HL 4+]:  ⟵ “Business & Management | HL 4+ | Management Elective | 6 | Not applicable”
  - equivalencies[IB-BUSINESS-MANAGEMENT|SL 4+]:  ⟵ “Business & Management | SL 4+ | Management Elective | 3 | Not applicable”
  - equivalencies[IB-CHEMISTRY|HL 6, 7]:  ⟵ “Chemistry | HL 6, 7 | Chemistry 105, 106 (2 labs granted) | 8 | PSCI”
  - equivalencies[IB-CHEMISTRY|HL 4, 5]:  ⟵ “Chemistry | HL 4, 5 | Chemistry 105 | 4 | PSCI”
  - equivalencies[IB-CHEMISTRY|SL 5+]:  ⟵ “Chemistry | SL 5+ | Chemistry 105 | 4 | PSCI”
  - equivalencies[IB-CHEMISTRY|SL 4]:  ⟵ “Chemistry | SL 4 | Chemistry 101 | 4 | PSCI”
  - equivalencies[IB-CHEMISTRY|HL 4]:  ⟵ “Chemistry | HL 4 | Foreign Languages and Cultures 100, 200 | 8 | Not applicable”
  - equivalencies[IB-CHEMISTRY|SL 4+]:  ⟵ “Chemistry | SL 4+ | Foreign Languages and Cultures 100 | 4 | Not applicable”
  - equivalencies[IB-COMPUTER-SCIENCE|HL 4+]:  ⟵ “Computer Science | HL 4+ | Computer Science 111, Elective | 6 | QUAN”
  - equivalencies[IB-COMPUTER-SCIENCE|SL 4+]:  ⟵ “Computer Science | SL 4+ | Computer Science 111 | 3 | QUAN”
  - equivalencies[IB-ECONOMICS|HL 5+]:  ⟵ “Economics | HL 5+ | Economics 101, 102 | 6 | SSCI”
  - equivalencies[IB-ECONOMICS|HL 4]:  ⟵ “Economics | HL 4 | Economics Elective | 6 | SSCI”
  - equivalencies[IB-ECONOMICS|SL 4+]:  ⟵ “Economics | SL 4+ | Economics Elective | 3 | SSCI”
  - equivalencies[IB-ENGLISH-A-LITERATURE|HL 4+]:  ⟵ “English A: Literature | HL 4+ | English 101, 108 | 6 | WRTG, HUM”
  - equivalencies[IB-ENGLISH-A-LITERATURE|SL 4+]:  ⟵ “English A: Literature | SL 4+ | English 108 | 3 | HUM”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|HL 4+]:  ⟵ “English A: Language & Literature | HL 4+ | English 101, 108 | 6 | WRTG, HUM”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|SL 4+]:  ⟵ “English A: Language & Literature | SL 4+ | English 108 | 3 | HUM”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|HL 4+]:  ⟵ “Environmental Systems and Societies | HL 4+ | School of the Environment 110, 1XX | 7 | BSCI”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|SL 4+]:  ⟵ “Environmental Systems and Societies | SL 4+ | School of the Environment 110 | 4 | BSCI”
  - equivalencies[IB-FILM|HL 5+]:  ⟵ “Film | HL 5+ | English 150, Elective | 6 | ARTS”
  - equivalencies[IB-FILM|HL 4]:  ⟵ “Film | HL 4 | UCORE Elective | 6 | ARTS”
  - equivalencies[IB-FILM|SL 4+]:  ⟵ “Film | SL 4+ | UCORE Elective | 3 | ARTS”
  - equivalencies[IB-FRENCH|SL 4+]:  ⟵ “French AB Initio | SL 4+ | French 120 | 3 | HUM”
  - … 43 more rows
### `0dd0357541ac803b` Wenatchee Valley College — appeals 2026-27 [new] (labeled_in_source)
- source: https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/special-circumstances.html (sha256 14b26a32d597)
- issues: semantic_review_required, conflicting_sources:https://wvc.edu/apply/fund-your-education/financial-aid/award-information.html,https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/index.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the Student Aid Index (SAI) or the Cost of Attendance (COA).”
  - sentence: need_based_special_circumstances ⟵ “At WVC, the Financial Aid office has the Revision Request form that student's can use to request a Special Circumstances decision.”
  - sentence: need_based_special_circumstances ⟵ “How else can Special Circumstances help me?”
### `2fb7e41ed4bc8550` Wenatchee Valley College — appeals 2026-27 [new] (labeled_in_source)
- source: https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/special-circumstances.html (sha256 14b26a32d597)
- issues: semantic_review_required, conflicting_sources:https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/index.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Special Circumstances can also allow financial aid administrators may use professional judgment to modify or adjust one or more of the components that compromise the student’s COA.”
  - sentence: professional_judgment ⟵ “Download the Additional Expense Form Additional Considerations It is important to keep in mind that when the financial administrator uses Professional Judgment (PJ) for adjusting unusual expenses, they must consider the income protection allowance (IPA) which is included in the SAI calculation.”
### `4414a0781f763d5c` Wenatchee Valley College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wvc.edu/apply/fund-your-education/financial-aid/media/documents/forms/Wenatchee%20Valley%20College%20SAP%20Rules%20and%20Requirements.pdf (sha256 2145ff53a4f9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students appealing will need to submit the Satisfactory Academic Progress (SAP) Appeal Form.”
  - sentence: sap_appeal ⟵ “Appeal Forms Both the SAP and MAC Appeal Forms can be found in multiple ways.”
### `4670d1ec51452ff1` Wenatchee Valley College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/index.html (sha256 eb2dc2532958)
- issues: semantic_review_required, conflicting_sources:https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “There are multiple processes under the "Professional Judgment" umbrella that aim to account for extenuating circumstances happening for the student, or their family, that are not properly reflected in the FAFSA/WASFA.”
### `681e4e2647073c32` Wenatchee Valley College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/index.html (sha256 eb2dc2532958)
- issues: semantic_review_required, conflicting_sources:https://wvc.edu/apply/fund-your-education/financial-aid/award-information.html,https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances This process updates a student's dependency status based on their unique situation.”
  - sentence: need_based_special_circumstances ⟵ “Examples include, but are not limited to: leaving an abusive home being abandoned by parent(s) incarcerated parent(s) being unable to contact/locate parent(s) Learn more about Unusual Circumstances Special Circumstances The FAFSA/WASFA uses income information from 2 years prior, which isn't always reflective of a student or families current situation.”
  - sentence: need_based_special_circumstances ⟵ “This process updates FAFSA/WASFA information to reflect recent financial changes, such as: Job loss Death in the family Reduction of hours Retirement Large medical expenses not covered by insurance Childcare expenses Change in marital status (separation/divorce) Learn more about Special Circumstances Unaccompanied Homeless Youth (UHY) Determination Student's experiencing homelessness and not in cu”
### `d662d7865e89edc0` Wenatchee Valley College — appeals 2026-27 [new] (labeled_in_source)
- source: https://wvc.edu/apply/fund-your-education/financial-aid/award-information.html (sha256 3363916698c5)
- issues: semantic_review_required, conflicting_sources:https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/index.html,https://wvc.edu/apply/fund-your-education/financial-aid/professional-judgment/special-circumstances.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you have received your award letter and wish to find out about requesting adjustments, additional funding or special circumstances, go to our 2026-2027 Forms page, and choose the appropriate link for more information on each of the following items.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances: If you believe you have special circumstances that are not reflected in your Financial Aid Notification, please visit our forms page and review the information regarding special circumstances.”
### `c578e78365e84952` Wenatchee Valley College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://wvc.edu/apply/fund-your-education/financial-aid/cost-to-attend.html (sha256 0d0d37b899b5)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:*Tuition & Fees: 4890 ⟵ “*Tuition & Fees | $4,890 | $5,466 | $11,160”
  - on_campus:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528 | $528”
  - on_campus:Housing & Food: 9156 ⟵ “Housing & Food | $9,156 | $9,156 | $9,156”
  - on_campus:Transportation: 2574 ⟵ “Transportation | $2,574 | $2,574 | $2,574”
  - on_campus:Misc.: 1908 ⟵ “Misc. | $1,908 | $1,908 | $1,908”
  - on_campus:Total: 19056 ⟵ “Total | $19,056 | $19,632 | $25,326”
### `fa671c2ec07f909a` Wenatchee Valley College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://wvc.edu/apply/fund-your-education/financial-aid/cost-to-attend.html (sha256 0d0d37b899b5)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:*Tuition & Fees: 8259 ⟵ “*Tuition & Fees | $8,259 | $8,874 | $22,191”
  - on_campus:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528 | $528”
  - on_campus:Housing & Food: 9156 ⟵ “Housing & Food | $9,156 | $9,156 | $9,156”
  - on_campus:Transportation: 2574 ⟵ “Transportation | $2,574 | $2,574 | $2,574”
  - on_campus:Misc.: 1908 ⟵ “Misc. | $1,908 | $1,908 | $1,908”
  - on_campus:Total: 22425 ⟵ “Total | $22,425 | $23,040 | $36,357”
  - on_campus:*Tuition & Fees: 8874 ⟵ “*Tuition & Fees | $8,259 | $8,874 | $22,191”
  - on_campus:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528 | $528”
  - on_campus:Housing & Food: 9156 ⟵ “Housing & Food | $9,156 | $9,156 | $9,156”
  - on_campus:Transportation: 2574 ⟵ “Transportation | $2,574 | $2,574 | $2,574”
  - on_campus:Misc.: 1908 ⟵ “Misc. | $1,908 | $1,908 | $1,908”
  - on_campus:Total: 23040 ⟵ “Total | $22,425 | $23,040 | $36,357”
  - column:*Tuition & Fees: 22191 ⟵ “*Tuition & Fees | $8,259 | $8,874 | $22,191”
  - column:Books & Supplies: 528 ⟵ “Books & Supplies | $528 | $528 | $528”
  - column:Housing & Food: 9156 ⟵ “Housing & Food | $9,156 | $9,156 | $9,156”
  - column:Transportation: 2574 ⟵ “Transportation | $2,574 | $2,574 | $2,574”
  - column:Misc.: 1908 ⟵ “Misc. | $1,908 | $1,908 | $1,908”
  - column:Total: 36357 ⟵ “Total | $22,425 | $23,040 | $36,357”
### `58ea0bfeed63a5c0` Western Washington University — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.wwu.edu/returning (sha256 d85f3c59847f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “There are special circumstances for students enrolled in Outreach and Continuing Education supported location programs, too.”
### `8f45316bea3f9fd7` Western Washington University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://admissions.wwu.edu/international/tuition-scholarships (sha256 3e657f4d2722)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:New Student Enrollment Fee: 450 ⟵ “New Student Enrollment Fee | $450”
  - column:Tuition(10-18 credits): 27717 ⟵ “Tuition(10-18 credits) | $27,717”
  - column:Fees(Mandatory fees include: International Service Fee, Health Service, Non-AcademicBuilding, Recreation Center, Technology, RenewableEnergy and Transportation.): 1974 ⟵ “Fees(Mandatory fees include: International Service Fee, Health Service, Non-AcademicBuilding, Recreation Center, Technology, RenewableEnergy and Transportation.) | $1,974”
  - column:Housing & Meals(Based on a double room & Unlimited Meal Plan): 16893 ⟵ “Housing & Meals(Based on a double room & Unlimited Meal Plan) | $16,893”
  - column:Books & Supplies*: 1224 ⟵ “Books & Supplies* | $1,224”
  - column:Transportation*: 2691 ⟵ “Transportation* | $2,691”
  - column:Personal & Miscellaneous*: 1968 ⟵ “Personal & Miscellaneous* | $1,968”
  - column:Emergency Health Insurance(required): 1502 ⟵ “Emergency Health Insurance(required) | $1,502”
  - column:Total: 54419 ⟵ “Total | $54,419”
### `2b544a6bddbd6985` Western Washington University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admissions.wwu.edu/apply/ap-ib-cic (sha256 4c507e2dc02e)
- issues: rows_without_score
- checks: {"distinct_exams": 53, "equivalencies": 117, "rows_without_score": 5}
  - equivalencies[IB-BIOLOGY|3]:  ⟵ “AP | Biology | 3 |  | Biology 101 (4 credits) | Lab Science”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “AP | Biology | 4 |  | Biology 204 (5 credits) | Lab Science”
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “AP | Biology | 5 |  | Biology 204 (5 credits), Biology 205 (5 credits) | Lab Science”
  - equivalencies[IB-BIOLOGY-HL|HL 4+]:  ⟵ “IB | Biology (HL) | 4+ |  | Biology 101, Biology electives (8 credits Lab Science), Biology electives (7 credits Non-Lab Science) | Lab Science, Non-Lab Science”
  - equivalencies[IB-BIOLOGY-SL|SL 4+]:  ⟵ “IB | Biology (SL) | 4+ |  | Biology 101, Biology electives (8 credits Lab Science) | Lab Science”
  - equivalencies[IB-BIOLOGY|A]:  ⟵ “CIE | Biology | A |  | BIOL 204, 205, BIOL electives (15 credits) | Lab Science”
  - equivalencies[IB-BIOLOGY|AS]:  ⟵ “CIE | Biology | AS |  | BIOL 204, BIOL electives (7.5 credits) | Lab Science”
  - equivalencies[IB-BUSINESS-MANAGEMENT|A]:  ⟵ “CIE | Business | A |  | MGMT electives (15 credits) | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT|AS]:  ⟵ “CIE | Business | AS |  | MGMT electives (7.5 credits) | ”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4+]:  ⟵ “IB | Business Management (HL) | 4+ |  | Management electives (4 credits) | ”
  - equivalencies[IB-CHEMISTRY|3+]:  ⟵ “AP | Chemistry | 3+ |  | Chemistry 161, 162 (10 credits) | Lab Science”
  - equivalencies[IB-CHEMISTRY-HL|HL 4–5]:  ⟵ “IB | Chemistry (HL) | 4–5 |  | Chemistry 161 (5 credits) | Lab Science”
  - equivalencies[IB-CHEMISTRY-HL|HL 6]:  ⟵ “IB | Chemistry (HL) | 6 |  | Chemistry 161, 162 (10 credits) | Lab Science”
  - equivalencies[IB-CHEMISTRY-HL|HL 7]:  ⟵ “IB | Chemistry (HL) | 7 |  | Chemistry 161, 162, 163 (15 credits) | Lab Science”
  - equivalencies[IB-CHEMISTRY-SL|SL 4+]:  ⟵ “IB | Chemistry (SL) | 4+ |  | Chemistry elective (3 credits) | ”
  - equivalencies[IB-CHEMISTRY|A]:  ⟵ “CIE | Chemistry | A |  | CHEM 161, 162, 163 (15 credits) | Lab Science”
  - equivalencies[IB-CHEMISTRY|AS]:  ⟵ “CIE | Chemistry | AS |  | CHEM electives (7.5 credits) | Lab Science”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 4+]:  ⟵ “IB | Computer Science (HL) | 4+ |  | CSCI 141 (4 Credits), CSCI 145 (4 Credits) | Quantitative & Symbolic Reasoning”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|SL 4+]:  ⟵ “IB | Computer Science (SL) | 4+ |  | CSCI 141 (4 Credits) | Quantitative & Symbolic Reasoning”
  - equivalencies[IB-COMPUTER-SCIENCE|A]:  ⟵ “CIE | Computer Science | A |  | CSCI 101, CSCI 120, CSCI electives (15 credits) | ”
  - equivalencies[IB-COMPUTER-SCIENCE|AS]:  ⟵ “CIE | Computer Science | AS |  | CSCI 120, CSCI electives (7.5 credits) | ”
  - equivalencies[IB-COMPUTER-SCIENCE|3+]:  ⟵ “AP | Computer Science A | 3+ |  | Computer Science 141 (4 credits) | Quantitative & Symbolic Reasoning”
  - equivalencies[IB-COMPUTER-SCIENCE|3+]:  ⟵ “AP | Computer Science Principles | 3+ |  | General electives (3 credits) | ”
  - equivalencies[IB-ECONOMICS-HL|HL 4]:  ⟵ “IB | Economics (HL) | 4 |  | Economics 101 (4 credits) | Social Sciences”
  - equivalencies[IB-ECONOMICS-HL|HL 5+]:  ⟵ “IB | Economics (HL) | 5+ |  | Economics 206 and 207 (10 credits) | Social Sciences”
  - … 92 more rows
### `149f8e08102ceb5c` Whitman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-forms (sha256 e480a19a022a)
- issues: semantic_review_required, conflicting_sources:https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-faq,https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/how-to-apply-for-financial-aid,https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/the-whitman-10-percent-promise
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “CSS Profile Waiver Request for the Noncustodial Parent: Allows a student to request that the noncustodial parent’s financial information be excluded from financial aid consideration due to special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Provisional Independent Status Clarification Form: Provides information to determine if you qualify for independent status on your FAFSA, due to unusual circumstances.”
### `61d36de63551032d` Whitman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-faq (sha256 c4f386eb3df8)
- issues: semantic_review_required, conflicting_sources:https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-forms,https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/how-to-apply-for-financial-aid,https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/the-whitman-10-percent-promise
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “I have special circumstances that aren’t adequately reflected in my financial aid application.”
  - sentence: need_based_special_circumstances ⟵ “If you have unusual or special circumstances, we invite you to provide additional detail in the Special Circumstances section of your CSS Profile so that we can take that information into account as we review your financial aid application.”
  - sentence: need_based_special_circumstances ⟵ “Once we have information from you about your family’s special circumstances, we will let you know if we have any questions about the information you’ve provided or if we need any additional information.”
### `80aed6280650c182` Whitman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/how-to-apply-for-financial-aid (sha256 33c92eb94ab2)
- issues: semantic_review_required, conflicting_sources:https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-faq,https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-forms,https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/the-whitman-10-percent-promise
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If your family has experienced special or unusual circumstances—like a job loss, unexpected medical expenses or other financial challenges—you can request a re-evaluation of your aid offer.”
### `b13ad7de7952aca8` Whitman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-forms (sha256 e480a19a022a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Additional Financial Aid Forms Depending on your circumstances, you or your family may need these additional forms: Request for Computer Purchase Budget Adjustment Form: One time during college you may request an increase in your cost of attendance to include the purchase of a computer, which may make it possible for you to receive additional outside scholarship funding or increase your educationa”
### `b22ae3488ccfbc3d` Whitman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/the-whitman-10-percent-promise (sha256 b55355c6b7cf)
- issues: semantic_review_required, conflicting_sources:https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-faq,https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/financial-aid-forms,https://www.whitman.edu/admission-and-aid/financial-aid-and-costs/how-to-apply-for-financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “No financial aid documents Be considered for merit aid Submit the FAFSA Get the Whitman 10% Promise Submit the FAFSA + CSS Profile Receive a full financial aid analysis—helpful if your family has special circumstances (such as multiple college students or income fluctuations) The Bottom Line Three things your family can count on with the Whitman 10% Promise.”
### `15459ee29fcff016` Whitworth University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.whitworth.edu/cms/administration/financial-aid/satisfactory-academic-progress-requirements/ (sha256 cb5288c1258b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Reinstatement of Eligibility Financial Aid Appeal Process Students who are no longer eligible to receive financial aid after the completion of their financial-aid-warning semester because of lack of satisfactory academic progress may submit a Financial Aid Satisfactory Academic Progress Appeal to the Financial Aid Appeal Committee, care of the financial aid office.”
  - sentence: sap_appeal ⟵ “The appeal consists of three items: Satisfactory Academic Progress Appeal Online Form to be completed by the student Academic Plan for Success completed and reviewed by academic affairs Documentation from a doctor or relative who has knowledge of the circumstances that were beyond the student's control Incomplete satisfactory academic progress appeals will not be accepted.”
  - sentence: sap_appeal ⟵ “The Financial Aid Satisfactory Academic Progress Appeal Form is available online.”
  - sentence: sap_appeal ⟵ “You must complete and submit an online Satisfactory Academic Progress Appeal Form to the Financial Aid Appeal Committee.”
  - sentence: sap_appeal ⟵ “If you begin the semester prior to your satisfactory academic progress appeal being approved, you will be responsible for all charges without the benefit of financial aid if the appeal is denied.”
  - sentence: sap_appeal ⟵ “If you are unable to meet the satisfactory academic progress requirements after your warning semester, you may wish to submit a satisfactory academic progress appeal along with documentation from your doctor and an academic plan for success that the associate dean of academic affairs has created with you to assure your success.”
### `19fc0cdfe5b128d3` Whitworth University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.whitworth.edu/cms/administration/financial-aid/satisfactory-academic-progress-requirements/ (sha256 cb5288c1258b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If you meet the minimum requirements for other aid, your offer will be reevaluated and any unmet need as a result of losing the scholarship will be reconsidered if no appeal is granted.”
### `955c72126a0d9099` Whitworth University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.whitworth.edu/cms/administration/financial-aid/scholarships/ (sha256 91fd98eef148)
- issues: semantic_review_required, conflicting_sources:https://www.whitworth.edu/cms/administration/financial-aid/satisfactory-academic-progress-requirements/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Need-Based Undergraduate Grants Undergraduate Students International Students Parents Adult Online Students Graduate Students Related Links Contact Information Application Process Financial Aid Forms FAFSA Federal Student Aid ID Federal Student Aid How to Complete Federal Verification Disbursement Information Special & Unusual Circumstances Balance Your Bucs Military & Veterans Consumer Informatio”
### `b83bde4076613517` Whitworth University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.whitworth.edu/cms/administration/financial-aid/satisfactory-academic-progress-requirements/ (sha256 cb5288c1258b)
- issues: semantic_review_required, conflicting_sources:https://www.whitworth.edu/cms/administration/financial-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Undergraduate Students International Students Parents Adult Online Students Graduate Students Related Links Contact Information Application Process Financial Aid Forms FAFSA Federal Student Aid ID Federal Student Aid How to Complete Federal Verification Disbursement Information Special & Unusual Circumstances Balance Your Bucs Military & Veterans Consumer Information Satisfactory Academic Progress”
### `d7853b45dd515628` Whitworth University — appeals 2027-28 [new] (labeled_in_heading)
- source: https://www.whitworth.edu/cms/administration/financial-aid/whitworth-scholarships-for-first-year-students/ (sha256 5afdfd1d1aa5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Undergraduate Students International Students Parents Adult Online Students Graduate Students Related Links Contact Information Application Process Financial Aid Forms FAFSA Federal Student Aid ID Federal Student Aid How to Complete Federal Verification Disbursement Information Special & Unusual Circumstances Balance Your Bucs Military & Veterans Consumer Information Satisfactory Academic Progress”
### `899199a03cd8ee16` Whitworth University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.whitworth.edu/cms/academics/doctor-of-physical-therapy/admissions/tuition-and-expenses/ (sha256 c4b24e497521)
- issues: arrangement_unlabeled, cost_period_semester
- checks: {"columns": 2, "rows": 2}
  - column:Credits: 10 ⟵ “Credits | 10 | 9”
  - column:Tuition: 12100 ⟵ “Tuition | $12,100 | $10,890”
  - column:Credits: 9 ⟵ “Credits | 10 | 9”
  - column:Tuition: 10890 ⟵ “Tuition | $12,100 | $10,890”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 1; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- Bellevue College (`ipeds-234669`)
- Central Washington University (`ipeds-234827`)
- Eastern Washington University (`ipeds-235097`)
- Edmonds College (`ipeds-235103`)
- Gonzaga University (`ipeds-235316`)
- Highline College (`ipeds-235431`)
- Bates Technical College (`ipeds-235671`)
- Peninsula College (`ipeds-236258`)
- Seattle Pacific University (`ipeds-236577`)
- Whatcom Community College (`ipeds-237039`)
- Yakima Valley College (`ipeds-237109`)
- Faith International University (`ipeds-443049`)

## Leads: official pages found with no extracted record

- Bellingham Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Big Bend Community College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Cascadia College: admissions_tests, merit_scholarships, clep_credit, residency, degree_requirements, aid_appeals
- Centralia College: admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- City University of Seattle: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Clark College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Clover Park Technical College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Columbia Basin College: admissions_tests, merit_scholarships, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Cornish College of the Arts: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, residency
- Everett Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Grays Harbor College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Green River College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation
- Heritage University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
- Lake Washington Institute of Technology: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Lower Columbia College: admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- North Seattle College: admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency
- Northwest Indian College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Northwest School of Wooden Boat Building: merit_scholarships, degree_requirements
- Northwest University: tuition_fees, cost_of_attendance, admissions_tests, degree_requirements
- Northwest University-Center for Online and Extended Education: tuition_fees, cost_of_attendance, admissions_tests, degree_requirements
- Olympic College: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Pacific Lutheran University: admissions_tests, merit_scholarships, statewide_articulation, aid_appeals
- Pacific Northwest Christian College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Pierce College District: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Renton Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Saint Martin's University: admissions_tests, transfer_credit, residency
- Seattle Central College: admissions_tests, merit_scholarships, transfer_credit, residency
- Seattle University: cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Shoreline Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Skagit Valley College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- South Puget Sound Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- South Seattle College: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Spokane Community College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency, aid_appeals
- Spokane Falls Community College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency
- Tacoma Community College: admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, residency
- The Evergreen State College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- University of Puget Sound: admissions_tests, merit_scholarships, transfer_credit
- University of Washington-Bothell Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, residency, degree_requirements
- University of Washington-Seattle Campus: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- University of Washington-Tacoma Campus: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- Walla Walla Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Walla Walla University: admissions_tests, common_data_set, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Washington State University: tuition_fees, cost_of_attendance, admissions_tests, statewide_articulation, residency, degree_requirements
- Wenatchee Valley College: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Western Washington University: admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Whitman College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, transfer_credit, residency, degree_requirements
- Whitworth University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
