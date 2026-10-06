# Review queue — MD (2026-27)

Pages fetched: 3450; failures: 410. Candidates: 490 (57 without issues, 433 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 9 | 15 | 17 | 1 | 4 |
| cost_of_attendance | 0 | 0 | 6 | 8 | 26 | 2 | 4 |
| admissions_tests | 0 | 0 | 2 | 0 | 37 | 3 | 4 |
| common_data_set | 0 | 0 | 2 | 0 | 5 | 35 | 4 |
| merit_scholarships | 0 | 0 | 3 | 0 | 37 | 2 | 4 |
| ap_credit | 0 | 0 | 5 | 7 | 16 | 14 | 4 |
| clep_credit | 0 | 0 | 3 | 7 | 15 | 17 | 4 |
| ib_credit | 0 | 0 | 2 | 6 | 11 | 23 | 4 |
| dual_enrollment | 0 | 0 | 7 | 2 | 22 | 11 | 4 |
| transfer_credit | 0 | 0 | 9 | 1 | 28 | 4 | 4 |
| statewide_articulation | 0 | 0 | 0 | 0 | 25 | 17 | 4 |
| residency | 0 | 0 | 0 | 0 | 38 | 4 | 4 |
| degree_requirements | 0 | 0 | 0 | 1 | 33 | 8 | 4 |
| aid_appeals | 0 | 0 | 0 | 28 | 7 | 7 | 4 |

## Ready for review (57)

### `2e8c70471c48209c` Allegany College of Maryland — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://allegany.edu/financial-aid/cost-to-attend.html (sha256 33c3f8f4b9f2)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 9408 ⟵ “Tuition | $9,408 | $9,408”
  - on_campus:Fees: 704 ⟵ “Fees | $704 | $704”
  - on_campus:Books: 1560 ⟵ “Books | $1,560 | $1,560”
  - on_campus:Housing: 3420 ⟵ “Housing | $3,420 | $10,710”
  - on_campus:Transportation: 2280 ⟵ “Transportation | $2,280 | $2,280”
  - on_campus:Miscellaneous Personal Expenses: 7620 ⟵ “Miscellaneous Personal Expenses | $7,620 | $7,620”
  - on_campus:TOTAL COST: 24992 ⟵ “TOTAL COST | $24,992 | $32,282”
  - on_campus:Tuition: 9408 ⟵ “Tuition | $9,408 | $9,408”
  - on_campus:Fees: 704 ⟵ “Fees | $704 | $704”
  - on_campus:Books: 1560 ⟵ “Books | $1,560 | $1,560”
  - on_campus:Housing: 10710 ⟵ “Housing | $3,420 | $10,710”
  - on_campus:Transportation: 2280 ⟵ “Transportation | $2,280 | $2,280”
  - on_campus:Miscellaneous Personal Expenses: 7620 ⟵ “Miscellaneous Personal Expenses | $7,620 | $7,620”
  - on_campus:TOTAL COST: 32282 ⟵ “TOTAL COST | $24,992 | $32,282”
### `b3fb3a33483ccf92` Allegany College of Maryland — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://allegany.edu/financial-aid/cost-to-attend.html (sha256 33c3f8f4b9f2)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 3264 ⟵ “Tuition | $3,264 | $3,264”
  - on_campus:Fees: 704 ⟵ “Fees | $704 | $704”
  - on_campus:Books: 1560 ⟵ “Books | $1,560 | $1,560”
  - on_campus:Housing: 3420 ⟵ “Housing | $3,420 | $10,710”
  - on_campus:Transportation: 2280 ⟵ “Transportation | $2,280 | $2,280”
  - on_campus:Miscellaneous Personal Expenses: 7620 ⟵ “Miscellaneous Personal Expenses | $7,620 | $7,620”
  - on_campus:TOTAL COST: 18848 ⟵ “TOTAL COST | $18,848 | $26,138”
  - on_campus:Tuition: 3264 ⟵ “Tuition | $3,264 | $3,264”
  - on_campus:Fees: 704 ⟵ “Fees | $704 | $704”
  - on_campus:Books: 1560 ⟵ “Books | $1,560 | $1,560”
  - on_campus:Housing: 10710 ⟵ “Housing | $3,420 | $10,710”
  - on_campus:Transportation: 2280 ⟵ “Transportation | $2,280 | $2,280”
  - on_campus:Miscellaneous Personal Expenses: 7620 ⟵ “Miscellaneous Personal Expenses | $7,620 | $7,620”
  - on_campus:TOTAL COST: 26138 ⟵ “TOTAL COST | $18,848 | $26,138”
### `12f6656020d781aa` Anne Arundel Community College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18438&returnto=18122 (sha256 f566da736fde)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Additional Degree Requirements A grade of C or better is required in each Computer Science Transfer course requirement.”
### `1c4c1671afde4a30` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: Student does not need to be pursuing a degree or other recognized education credentials. ⟵ “Type of degree required | Student does not need to be pursuing a degree or other recognized education credentials.”
### `41add2f339aa9f1c` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: Available for an unlimited number of years. ⟵ “Number of tax years credit available | Available for an unlimited number of years.”
### `4a6745a204d8c9b6` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: Tuition, required enrollment fees, and course-related books, supplies and equipment. ⟵ “Qualified expenses | Tuition, required enrollment fees, and course-related books, supplies and equipment.”
### `753b437b680cd0be` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: $132,000 if married filing jointly; $66,000 if single, head of household, or qualifying widow(er). ⟵ “Limit on modified adjusted gross income (MAGI) | $132,000 if married filing jointly; $66,000 if single, head of household, or qualifying widow(er).”
### `7a4201e9b6efd799` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 ($4,000 if a student in a Midwestern disaster area) credit per return. ⟵ “Maximum credit | Up to $2,000 ($4,000 if a student in a Midwestern disaster area) credit per return.”
### `b0fb6537dd437887` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: Available for one or more courses. ⟵ “Number of courses | Available for one or more courses.”
### `bd862851b9e5de1e` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: Payments made in 2018 for academic periods beginning in 2018 and in the first 3 months of 2019. ⟵ “Payments for academic periods | Payments made in 2018 for academic periods beginning in 2018 and in the first 3 months of 2019.”
### `d51288fbc7f8cd14` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: Available for all years of postsecondary and for courses to acquire or improve job skills. ⟵ “Number of years of postsecondary education | Available for all years of postsecondary and for courses to acquire or improve job skills.”
### `dbf3a5f406161292` Carroll Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/costs-scholarships-aid/continuing-education-cost/non-credit-lifetime-learning-credit/ (sha256 6a9c4a071cef)
- checks: {"thresholds": null}
  - award_amount_text: Felony drug convictions doesn’t make the student ineligible. ⟵ “Felony drug conviction | Felony drug convictions doesn’t make the student ineligible.”
### `99c9a1638bbd8d77` Carroll Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/teens-and-high-school-students/early-college-program/ (sha256 b3a6140ea8b3)
- checks: {"fields": [], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Have a 3.0 GPA (through 10th grade) & submit a transcript”
  - eligibility_tier: 2.0 ⟵ “EC students must maintain a 2.0 GPA. If an EC student’s GPA falls below 2.0, they will be placed on academic probation. They have one semester to raise their GPA. If they do not, they will return to their high school.”
### `f3853c53cdf25d1c` Carroll Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/what-course-credit-do-i-already-have/advanced-placement-tests/ (sha256 e5f120e82596)
- checks: {"distinct_exams": 27, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “ART-101 | 3 | Art-2D | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “ART-110 | 3 | Art-3D | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “ART-120 | 3 | Art Studio-Drawing | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “ART-135; ART-136 | 6 | Art History | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “BIOL-100 | 4 | Biology | 3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “BIOL-101 | 4 | Biology | 4”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “BIOL-101 and BIOL-202 | 8 | Biology | 5”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “CHEM-101 | 4 | Chemistry | 3”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “CHEM-105 | 4 | Chemistry | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “CHEM-105/ CHEM-106 | 8 | Chemistry | 5”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “CIS-105 | 3 | Computer Science Principles | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3 or 4]:  ⟵ “CIS-132 | 3 | Computer Science A | 3 or 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|5]:  ⟵ “CMSC-201 | 4 | Computer Science A | 5”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “ECON-100 | 3 | Micro Economics | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “ECON-102 | 3 | Macro Economics | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “ENGL-101 | 3 | English Language and Comp | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “ENGL-102 | 3 | English Literature and Comp | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “FREN-100, FREN-102 | 6 | French Language and Culture | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “FREN-100/ FREN-102/ FREN-201 | 9 | French Language and Culture | 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “FREN 100/FREN 102/FREN 201/FREN 202 | 12 | French Language and Culture | 5”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “General Elective | 3 | AP Research | 3”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “General Elective | 3 | AP Seminar | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “GEOG-105 | 3 | Human Geography | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “GERM-100/ GERM-102/ GERM-201/ GERM-202 | 12 | German Language and Culture | 3”
  - equivalencies[AP-STATISTICS|4]:  ⟵ “MATH-115 | 4 | Statistics | 4”
  - … 13 more rows
### `0020c556c777b7c0` Carroll Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/graduating-high-school-seniors/earn-college-credit-for-your-high-school-work/ (sha256 e4c67a71f0c8)
- checks: {"fields": ["min_grade"]}
  - min_grade: D ⟵ “Courses with a grade of D or higher typically transfer; however, a minimum C grade is required for ENGL-101- College Writing.”
### `ef384536b267ebb1` Cecil College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.cecil.edu/admissions/academic-credit-for-prior-learning-examinations (sha256 d5c42943bc25)
- checks: {"distinct_exams": 31, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design | 3 | 3 | ART 101 (H)”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design | 3 | 3 | ART 201 (H)”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | ART 141 (H)”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIO 101 (S), BIO 111 or BIO 130 (S), BIO 131 or BIO 132 (S), BIO 133”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | MAT 201 (M)”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 8 | MAT 201 (M), MAT 202 (M)”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHM 103 (S), CHM 113”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 6 | CSC 109, CSC 205”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | 3 | CSC 104 (I)”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing | 3 | 6 | ART 130 (H), ART 230 (H)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | 3 | EGL 101 (E)”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | 6 | EGL 101 (E), EGL 102 (H)”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 4 | ENV 106 (S), ENV 116”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 6 | HST 101 (H), HST 102 (H)”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | 6 | FRN 101 (H), FRN 102 (H)”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | 3 | 6 | Arts/Humanities Elective (H)”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | GEO 102 (SS)”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 3 | ECO 221 (SS)”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 3 | ECO 222 (SS)”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 7 | MUC 143 (H), MUC 110”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1 | 3 | 4 | PHY 181 (SL)”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2 | 3 | 4 | PHY 182 (SL)”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C: Mechanics | 3 | 4 | PHY 217 (SL)”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity and Magnetism | 3 | 4 | PHY 218 (SL)”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus | 3 | 4 | MAT 191 (M)”
  - … 6 more rows
### `m7644b42ecd05be6` Chesapeake College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.chesapeake.edu/program/dual-enrollment/ (sha256 461552c7cd5a)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 2}
  - eligibility_tier: 2.5 ⟵ “Must possess a cumulative GPA of 2.5 or greater and”
  - eligibility_tier: 2.5 ⟵ “See if you’re eligible to participate. You must have completed your sophomore year of high school with a cumulative GPA of at least 2.5, and be enrolled in an eligible high school in our service region. Please see above section for details.”
  - eligibility_tier: 3.0 ⟵ “Dual Enrollment Students with a cumulative 3.0 high school GPA are eligible to take college English.”
  - eligibility_tier: 2.5 ⟵ “• 2.5 or higher cumulative GPA and”
  - eligibility_tier: 2.5 ⟵ “Must possess a cumulative GPA of 2.5 or greater and”
  - eligibility_tier: 2.5 ⟵ “See if you’re eligible to participate. You must have completed your sophomore year of high school with a cumulative GPA of at least 2.5, and be enrolled in an eligible high school in our service region. Please see above section for details.”
### `2b719aa1fa268cc2` College of Southern Maryland — awards 2026-27 [new] (source_unlabeled)
- source: https://www.csmd.edu/costs-aid/scholarships-financial-aid/policies/index.html (sha256 e0a8255a9424)
- checks: {"thresholds": {"gpa_min": 1.5}}
  - gpa_requirement: 1.50 ⟵ “6 to 18 credits | 1.50 | 67%”
### `9b5b5b2f6f124a4a` College of Southern Maryland — awards 2026-27 [new] (source_unlabeled)
- source: https://www.csmd.edu/costs-aid/scholarships-financial-aid/policies/index.html (sha256 e0a8255a9424)
- checks: {"thresholds": {"gpa_min": 2.0}}
  - gpa_requirement: 2.00 ⟵ “45 or more credits | 2.00 | 67%”
### `e76ca2c427d333bd` College of Southern Maryland — awards 2026-27 [new] (source_unlabeled)
- source: https://www.csmd.edu/costs-aid/scholarships-financial-aid/policies/index.html (sha256 e0a8255a9424)
- checks: {"thresholds": {"gpa_min": 1.75}}
  - gpa_requirement: 1.75 ⟵ “19 to 31 credits | 1.75 | 67%”
### `f73ac0ee2f7f6371` College of Southern Maryland — awards 2026-27 [new] (source_unlabeled)
- source: https://www.csmd.edu/costs-aid/scholarships-financial-aid/policies/index.html (sha256 e0a8255a9424)
- checks: {"thresholds": {"gpa_min": 1.85}}
  - gpa_requirement: 1.85 ⟵ “32 to 44 credits | 1.85 | 67%”
### `819f04ed202ce201` College of Southern Maryland — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.csmd.edu/apply-register/credit-for-prior-learning/index.html (sha256 3d311b5160ff)
- checks: {"distinct_exams": 28, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3-5]:  ⟵ “African American Studies | 3-5 | 3 | LAN Elective (can be used to fulfill the Humanities General Education requirement and Cultural and Global Awareness Core Requirement)”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | ART-1030”
  - equivalencies[AP-ART-HISTORY|3-5]:  ⟵ “Art History | 3-5 | 3 | ART-1010”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIO-1010 /BIO-1010L or BIO-1020 /BIO-1020L”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | 8 | Choose Two Courses: BIO-1010 /BIO-1010L or BIO-1020 /BIO-1020L or BIO-1060 /BIO-1060L”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | 8 | Choose Two Courses: BIO-1010 /BIO-1010L , BIO-1020 /BIO-1020L , BIO-1060 /BIO-1060L , BIO-1070 /BIO-1070L”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHE-1200 /CHE-1200L”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “Chemistry | 4 or 5 | 8 | CHE-1200 /CHE-1200L and CHE-1210 /CHE-1210L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | 3 | LAN Elective”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language and Culture | 4-5 | 6 | LAN Elective”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3-5]:  ⟵ “Comparative Government and Politics | 3-5 | 3 | POL-1050”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3-5]:  ⟵ “Computer Science A | 3-5 | 3 | CSC-1100”
  - equivalencies[AP-CYBERSECURITY|3-5]:  ⟵ “Cybersecurity | 3-5 | 3 | ITS-2090”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macro | 3 | 3 | ECN-1200”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Micro | 3 | 3 | ECN-1200”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Sciences | 3-5 | 4 | ENV-1300 /ENV-1300L”
  - equivalencies[AP-EUROPEAN-HISTORY|3 4-5]:  ⟵ “European History | 3 4-5 | 3 6 | Humanities General Education Elective Humanities General Education Elective”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “French Language and Culture | 3-5 | 3 | LAN Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3 4-5]:  ⟵ “German Language and Culture | 3 4-5 | 3 6 | LAN Elective LAN Elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Human Geography | 3-5 | 3 | GRY-1020”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3 4-5]:  ⟵ “Italian Language and Culture | 3 4-5 | 3 6 | LAN Elective LAN Elective”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3 4-5]:  ⟵ “Japanese Language and Culture | 3 4-5 | 3 6 | LAN Elective LAN Elective”
  - equivalencies[AP-LATIN|3 4-5]:  ⟵ “Latin | 3 4-5 | 3 6 | LAN Elective LAN Elective”
  - equivalencies[AP-CALCULUS-AB|3-5]:  ⟵ “CALC AB | 3-5 | 4 | MTH-1200”
  - equivalencies[AP-CALCULUS-BC|3-5]:  ⟵ “CALC BC | 3-5 | 4 | MTH-1200 and MTH-1210”
  - … 9 more rows
### `be73a04dcf005843` College of Southern Maryland — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.csmd.edu/apply-register/credit-for-prior-learning/index.html (sha256 3d311b5160ff)
- checks: {"distinct_exams": 33, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 | ACC-2010”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 | BAD-1210”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BAD-2070”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 3 | BAD-2610”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 3 | BIO Elective”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 3 | CHE-1050”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 | ECN-2025”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 | ECN-2020”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 | ENG-1010”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 3 | ENG-1010”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 | ENG-1020”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 6 | ENG-2010 and ENG-2020”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 | ENG-2200 and ENG-2210”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language - Level I | 50 | 3 | LAN Elective”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “French Language - Level II | 62 | 3 | LAN Elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Far East to 1648 | 50 | 3 | HST-1011”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to present | 50 | 3 | HST Elective”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonizations to 1877 | 50 | 3 | HST-1031”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present | 50 | 3 | HST-1032”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | Humanities General Education Elective”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | 3 | HST Elective”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 50 | 3 | ITS-1010”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language - Level 1 | 50 | 3 | LAN Elective”
  - equivalencies[CLEP-GERMAN-LANGUAGE|62]:  ⟵ “German Language - Level II | 62 | 3 | LAN Elective”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | MTH-1010”
  - … 12 more rows
### `833705befc4d233c` Community College of Baltimore County — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.ccbcmd.edu/Paying-for-College/Tuition-and-Fees/Cost-of-Attendance/index.html (sha256 df4962f2a9b7)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition & fees: 11114 ⟵ “Tuition & fees | $4,536 | $7,708 | $11,114”
  - off_campus_not_with_family:Books, materials & supplies: 1430 ⟵ “Books, materials & supplies | $1,430 | $1,430 | $1,430”
  - off_campus_not_with_family:Loan fees: 112 ⟵ “Loan fees | $112 | $112 | $112”
  - off_campus_not_with_family:Food & housing: 15742 ⟵ “Food & housing | $15,742 | $15,742 | $15,742”
  - off_campus_not_with_family:Personal expenses: 1510 ⟵ “Personal expenses | $1,510 | $1,510 | $1,510”
  - off_campus_not_with_family:Transportation: 2168 ⟵ “Transportation | $2,168 | $2,168 | $2,168”
  - off_campus_not_with_family:Total: 32076 ⟵ “Total | $25,498 | $28,670 | $32,076”
### `f241627d47aec875` Frederick Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.frederick.edu/paying-for-college/tuition-fees/cost-attendance.html (sha256 099ea7c7aba5)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Books, Course Materials, Supplies & Equipment: 1570 ⟵ “Books, Course Materials, Supplies & Equipment | $1,570 | $1,570 | $1,570”
  - off_campus_not_with_family:Living Expenses: Food: 3426 ⟵ “Living Expenses: Food | $3,426 | $3,426 | $3,426”
  - off_campus_not_with_family:Living Expenses: Housing: 7280 ⟵ “Living Expenses: Housing | $7,280 | $7,280 | $7,280”
  - off_campus_not_with_family:Personal Expenses: 7618 ⟵ “Personal Expenses | $7,618 | $7,618 | $7,618”
  - off_campus_not_with_family:Transportation: 2266 ⟵ “Transportation | $2,266 | $2,266 | $2,266”
  - off_campus_not_with_family:Tuition & Fees: 10630 ⟵ “Tuition & Fees | $4,054 | $8,038 | $10,630”
  - off_campus_not_with_family:Total: 32790 ⟵ “Total | $26,214 | $30,198 | $32,790”
### `6b3b40719798aa01` Garrett College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.garrettcollege.edu/images/services/transfer/transfer-to-gc/clep.pdf (sha256 44d0463eee23)
- checks: {"distinct_exams": 29, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting                                   50                   ACC210                3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems                                    50                   CIS105                3         Interdisciplinary/Emerging Issues”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law                              50                   BUS203                3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management                               50                   BUS170                3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing                                50                   BUS201                3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                                    50                  ENG252                 3                Arts & Humanities”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature                  50                  ENG1XX                 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                                    50                  ENG101                 3               English Composition”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular                            50                  ENG101                 3               English Composition”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                                     50                  ENG251                 3                Arts & Humanities”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                                             50                  HUM1XX                 3                Arts & Humanities”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                                    50                 POL140                  3           Social & Behavioral Sciences”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I                         50                 HIS111                  3                Arts & Humanities”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II                        50                 HIS112                  3                Arts & Humanities”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development                           50                 PSY102                  3           Social & Behavioral Sciences”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology                 50                 PSY211                  3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                                50                 PSY101                  3           Social & Behavioral Sciences”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                                 50                 SOC101                  3           Social & Behavioral Sciences”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                           50                 ECN201                  3           Social & Behavioral Sciences”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                           50                 ECN202                  3           Social & Behavioral Sciences”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History                            50             SOC1XX & HIS1XX             6           Social & Behavioral Sciences”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I                                 50                 HIS101                  3                Arts & Humanities”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II                                50                 HIS102                  3                Arts & Humanities”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                                50             BIO101 & BIO102             8                     Science”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus W/ Elementary Functions                       50                 MAT190                  4                   Mathematics”
  - … 4 more rows
### `943ad8ec05b6a5f1` Garrett College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.garrettcollege.edu/images/services/transfer/transfer-to-gc/leap.pdf (sha256 7b61b4b8e405)
- checks: {"distinct_exams": 38, "equivalencies": 47, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies                            3            SOC1XX, Social Science Elective                                     3         Social & Behavioral Sciences”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                                         3            ART103, Art Appreciation                                            3              Arts & Humanities”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art: Drawing                                        3            ART201, Drawing I                                                   3              Arts & Humanities”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                             3            BIO101 & BIO102, General Biology I & II                           4&4                    Science”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                         3            MAT110, Pre-Calculus Math                                           4                 Mathematics”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Calculus AB                                       4 or 5         MAT190, Calculus I                                                  4                 Mathematics”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                                         3            MAT190, Calculus I                                                  4                 Mathematics”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “Calculus BC                                       4 or 5         MAT190 & MAT191, Calculus I & II                                  4&4                 Mathematics”
  - equivalencies[AP-CHEMISTRY|3 or 4]:  ⟵ “Chemistry                                         3 or 4         CHE101, General Chemistry I                                         4                    Science”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry                                           5            CHE101 & CHE102, General Chemistry I & II                         4&4                    Science”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture                        3            ELE1XX, Elective                                                    6              Arts & Humanities”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                                  3            CIS170, Computer Science Programming I                              4      Interdisciplinary/Emerging Issues”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles                         3            CIS130, Programming Logic                                           3      Interdisciplinary/Emerging Issues”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: MACRO                                    3            ECN201, Prin of Economics I (MACRO)                                 3         Social & Behavioral Sciences”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: MICRO                                    3            ECN202, Prin of Economics II (MICRO)                                3         Social & Behavioral Sciences”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition                    3            ENG101, Comp I–Expository Writing                                   3             English Composition”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition                  3            ENG102, Comp II–Intro to Literature                                 3              Arts & Humanities”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                               3            ENV195, Environmental Science                                       3           Science (non laboratory)”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                                    3            HIS1XX, History Elective                                            3              Arts & Humanities”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture                         3            FRN101 & FRN102, Elementary French I & II                         3&3              Arts & Humanities”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Literature                                   3            FRN1XX, French Elective                                             3              Arts & Humanities”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language And Culture                         3            GRM101 & GRM102, Elementary German I & II                         3&3              Arts & Humanities”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                                     3            GEO201, Cultural Geography                                          3         Social & Behavioral Sciences”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture                        3            ELE1XX, Elective                                                    6              Arts & Humanities”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture                       3            ELE1XX, Elective                                                    6              Arts & Humanities”
  - … 22 more rows
### `d5539797309d6186` Garrett College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.garrettcollege.edu/images/services/transfer/transfer-to-gc/ib.pdf (sha256 25f0dbd28160)
- checks: {"distinct_exams": 11, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4-7]:  ⟵ “Anthropology     Social and Cultural Anthropology                     SL, HL        4-7                  ATH230               3             Social & Behavioral Sciences”
  - equivalencies[IB-BIOLOGY|4-7]:  ⟵ “Biology          Biology                                              SL, HL        4-7                  BIO104                                       Science”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4-7]:  ⟵ “Business         Business Management                                  SL, HL        4-7                  BUS101               3”
  - equivalencies[IB-ECONOMICS|4-7]:  ⟵ “Economics        Economics                                            SL, HL         4-7                 ECN201               3             Social & Behavioral Sciences”
  - equivalencies[IB-GEOGRAPHY|4-7]:  ⟵ “Geography        Geography                                            SL, HL         4-7                 GEO1xx               3”
  - equivalencies[IB-HISTORY|4-7]:  ⟵ “History          History                                                             4-7                 HIS121               3                  Arts & Humanities”
  - equivalencies[IB-FRENCH|5-7]:  ⟵ “French or Spanish (A or B)                                          5-7         FRN or SPN 101 & 102         6                  Arts & Humanities”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4]:  ⟵ “Mathematics: Analysis and Approaches                                 4                  MAT110               4                     Mathematics”
  - equivalencies[IB-MUSIC|4-7]:  ⟵ “Music            Music                                                SL, HL         4-7                 MUS1xx               3”
  - equivalencies[IB-PSYCHOLOGY|4-7]:  ⟵ “Psychology       Psychology                                           SL, HL         4-7                 PSY101               3             Social & Behavioral Sciences”
  - equivalencies[IB-THEATRE|4-7]:  ⟵ “Theater          Theatre                                              SL, HL         4-7              THE1xx (GER)            3                  Arts & Humanities”
### `1b1262d8db1ddeed` Garrett College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.garrettcollege.edu/disclosures-transfer-credit.php (sha256 59d4ad19eeda)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “For example, if a native student must earn a grade of “C” or better in a required course, the transfer student shall also be required to earn a “C“ or better to meet the same requirement.”
### `72e6e06479ffba14` Hagerstown Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.hagerstowncc.edu/admission-requirements-application-information-early-college-degree-program (sha256 dfed7c549317)
- checks: {"fields": [], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Minimum 3.0 high school GPA*”
  - eligibility_tier: 3.75 ⟵ “For Biology, Chemistry, Computer Science, Cybersecurity, Engineering Science, Environmental Studies, Mathematics, or Physics - Minimum 3.75 high school GPA”
### `a6c159c2f2f02f5a` Hood College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.hood.edu/admission-aid/admission/dual-enrollment-admission (sha256 e2496e577e59)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “A GPA of 3.0 or higher in the discipline of the course you will be taking”
  - per_credit_hour_charge: 0 ⟵ “$0 per credit *”
### `43b90071077879c4` Loyola University Maryland — awards 2026-27 [new] (source_unlabeled)
- source: https://www.loyola.edu/academics/psychology/admission/scholarships-and-awards.html (sha256 0f5f11114829)
- checks: {"thresholds": null}
  - award_amount_text: $60,000 ⟵ “M.S.-Psy.D. | $60,000 | $15,000 each year for four years split evenly between the fall and spring semesters.”
### `c91df78acb37ddbc` Maryland Institute College of Art — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mica.edu/admissions/financial-aid/tuition-fees/undergraduate-tuition-fees/undergraduate-cost-of-attendance/ (sha256 d1b1d374d4da)
- checks: {"columns": 3, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition: 58310 ⟵ “Tuition | 58,310 | 58,310 | 58,310”
  - on_campus:Student life fee: 1375 ⟵ “Student life fee | 1,375 | 1,375 | 1,375”
  - on_campus:Tech fee: 810 ⟵ “Tech fee | 810 | 810 | 810”
  - on_campus:Housing: 13000 ⟵ “Housing | 13,000 | 15,273 | 3,100”
  - on_campus:Food (Meal plan: $4,300 plus additional food allowance: $4,136): 8436 ⟵ “Food (Meal plan: $4,300 plus additional food allowance: $4,136) | 8,436 | 8,436 | 2,575”
  - on_campus:Books, course materials, supplies and equipment: 1545 ⟵ “Books, course materials, supplies and equipment | 1,545 | 1,545 | 1,545”
  - on_campus:Miscellaneous personal expenses: 1030 ⟵ “Miscellaneous personal expenses | 1,030 | 1,030 | 1,030”
  - on_campus:Transportation: 1030 ⟵ “Transportation | 1,030 | 1,135 | 1,135”
  - on_campus:Federal loan fees*: 900 ⟵ “Federal loan fees* | 900 | 950 | 900”
  - on_campus:Total: 86436 ⟵ “Total | 86,436 | 88,864 | 70,780”
  - off_campus_not_with_family:Tuition: 58310 ⟵ “Tuition | 58,310 | 58,310 | 58,310”
  - off_campus_not_with_family:Student life fee: 1375 ⟵ “Student life fee | 1,375 | 1,375 | 1,375”
  - off_campus_not_with_family:Tech fee: 810 ⟵ “Tech fee | 810 | 810 | 810”
  - off_campus_not_with_family:Housing: 15273 ⟵ “Housing | 13,000 | 15,273 | 3,100”
  - off_campus_not_with_family:Food (Meal plan: $4,300 plus additional food allowance: $4,136): 8436 ⟵ “Food (Meal plan: $4,300 plus additional food allowance: $4,136) | 8,436 | 8,436 | 2,575”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1545 ⟵ “Books, course materials, supplies and equipment | 1,545 | 1,545 | 1,545”
  - off_campus_not_with_family:Miscellaneous personal expenses: 1030 ⟵ “Miscellaneous personal expenses | 1,030 | 1,030 | 1,030”
  - off_campus_not_with_family:Transportation: 1135 ⟵ “Transportation | 1,030 | 1,135 | 1,135”
  - off_campus_not_with_family:Federal loan fees*: 950 ⟵ “Federal loan fees* | 900 | 950 | 900”
  - off_campus_not_with_family:Total: 88864 ⟵ “Total | 86,436 | 88,864 | 70,780”
  - with_parents_or_family:Tuition: 58310 ⟵ “Tuition | 58,310 | 58,310 | 58,310”
  - with_parents_or_family:Student life fee: 1375 ⟵ “Student life fee | 1,375 | 1,375 | 1,375”
  - with_parents_or_family:Tech fee: 810 ⟵ “Tech fee | 810 | 810 | 810”
  - with_parents_or_family:Housing: 3100 ⟵ “Housing | 13,000 | 15,273 | 3,100”
  - with_parents_or_family:Food (Meal plan: $4,300 plus additional food allowance: $4,136): 2575 ⟵ “Food (Meal plan: $4,300 plus additional food allowance: $4,136) | 8,436 | 8,436 | 2,575”
  - … 5 more rows
### `174ff86da21a602b` Maryland Institute College of Art — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mica.edu/admissions/undergraduate-admission/transfer-admission/planning-your-transfer/ (sha256 97ff91574d03)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Up to 60 credits may be transferred and applied toward the MICA B.F.A., and only courses carrying a grade of “C” or better will be considered.”
### `m463fc501d9badf5` McDaniel College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mcdaniel.edu/admissions-cost/undergraduate-admissions/transfer-student-admissions (sha256 a040f3aa62d4)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “You must earn a grade of “C-” or better for the credit to transfer.”
  - residency_requirement_credits: 32 ⟵ “Completion of the last 32 hours, not including the semester in education, in residence at the College.”
### `588c76f5212d8545` Montgomery College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.montgomerycollege.edu/paying-for-college/financial-aid/cost-of-attendance.html (sha256 47dd2d58b030)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition And Fees *: 5168 ⟵ “Tuition And Fees * | $ 5,168 | $ 5,168”
  - with_parents_or_family:Books, Course Materials, Supplies and Equipment **: 756 ⟵ “Books, Course Materials, Supplies and Equipment ** | $756 | $756”
  - with_parents_or_family:Housing & Food **: 5504 ⟵ “Housing & Food ** | $5,504 | $17,200”
  - with_parents_or_family:Transportation **: 3638 ⟵ “Transportation ** | $3,638 | $3,638”
  - with_parents_or_family:Miscellaneous Personal Expenses **: 12238 ⟵ “Miscellaneous Personal Expenses ** | $12,238 | $12,238”
  - with_parents_or_family:TOTAL EST. COST OF ATTENDANCE: 27304 ⟵ “TOTAL EST. COST OF ATTENDANCE | $ 27,304 | $ 39,000”
  - off_campus_not_with_family:Tuition And Fees *: 5168 ⟵ “Tuition And Fees * | $ 5,168 | $ 5,168”
  - off_campus_not_with_family:Books, Course Materials, Supplies and Equipment **: 756 ⟵ “Books, Course Materials, Supplies and Equipment ** | $756 | $756”
  - off_campus_not_with_family:Housing & Food **: 17200 ⟵ “Housing & Food ** | $5,504 | $17,200”
  - off_campus_not_with_family:Transportation **: 3638 ⟵ “Transportation ** | $3,638 | $3,638”
  - off_campus_not_with_family:Miscellaneous Personal Expenses **: 12238 ⟵ “Miscellaneous Personal Expenses ** | $12,238 | $12,238”
  - off_campus_not_with_family:TOTAL EST. COST OF ATTENDANCE: 39000 ⟵ “TOTAL EST. COST OF ATTENDANCE | $ 27,304 | $ 39,000”
### `709094988eb6c4d8` Montgomery College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.montgomerycollege.edu/paying-for-college/financial-aid/cost-of-attendance.html (sha256 47dd2d58b030)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees *: 13702 ⟵ “Tuition and Fees * | $ 13,702 | $ 13,702”
  - with_parents_or_family:Books, Course Materials, Supplies and Equipment **: 756 ⟵ “Books, Course Materials, Supplies and Equipment ** | $756 | $756”
  - with_parents_or_family:Housing & Food **: 5504 ⟵ “Housing & Food ** | $5,504 | $17,200”
  - with_parents_or_family:Transportation **: 3638 ⟵ “Transportation ** | $3,638 | $3,638”
  - with_parents_or_family:Miscellaneous Personal Expenses **: 12238 ⟵ “Miscellaneous Personal Expenses ** | $12,238 | $12,238”
  - with_parents_or_family:TOTAL EST. COST OF ATTENDANCE: 35838 ⟵ “TOTAL EST. COST OF ATTENDANCE | $ 35,838 | $ 47,534”
  - off_campus_not_with_family:Tuition and Fees *: 13702 ⟵ “Tuition and Fees * | $ 13,702 | $ 13,702”
  - off_campus_not_with_family:Books, Course Materials, Supplies and Equipment **: 756 ⟵ “Books, Course Materials, Supplies and Equipment ** | $756 | $756”
  - off_campus_not_with_family:Housing & Food **: 17200 ⟵ “Housing & Food ** | $5,504 | $17,200”
  - off_campus_not_with_family:Transportation **: 3638 ⟵ “Transportation ** | $3,638 | $3,638”
  - off_campus_not_with_family:Miscellaneous Personal Expenses **: 12238 ⟵ “Miscellaneous Personal Expenses ** | $12,238 | $12,238”
  - off_campus_not_with_family:TOTAL EST. COST OF ATTENDANCE: 47534 ⟵ “TOTAL EST. COST OF ATTENDANCE | $ 35,838 | $ 47,534”
### `49ba152c08616b12` Montgomery College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.montgomerycollege.edu/_documents/academics/credit-for-prior-learning/ib-exams-mc-equivalents.pdf (sha256 00eff41b2e8f)
- checks: {"distinct_exams": 17, "equivalencies": 17, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|3]:  ⟵ “Anthropology             Social and Cultural Anthropology              ANTH              Higher         5, 6, 7             ANTH201                3          Y”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology                  Biology                                       BIOL            Standard         5, 6, 7              BIOL101               4          Y”
  - equivalencies[IB-BUSINESS-MANAGEMENT|3]:  ⟵ “Business                 Business and Organization                    BUSI         Standard or Higher   5, 6, 7           BSAD elective            3          N”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry                Chemistry                                     CHEM            Standard         5, 6, 7             CHEM131                4          Y”
  - equivalencies[IB-COMPUTER-SCIENCE|3]:  ⟵ “Computer Science         Computer Science                              CMSC              Higher          6, 7               CMSC 140               3          N”
  - equivalencies[IB-ECONOMICS|3]:  ⟵ “Economics                Economics                                     ECON            Standard         5, 6, 7           ECON elective            3          N”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|3]:  ⟵ “English A: Literature and Language            ENGL            Standard         5, 6, 7           ENGL elective            3         N”
  - equivalencies[IB-FILM|3]:  ⟵ “Film                     Film                                         FILM              Higher          5, 6, 7              FILM110               3          Y”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French                   French                                        FREN            Standard           5                 FREN202                3          Y”
  - equivalencies[IB-GEOGRAPHY|3]:  ⟵ “Geography                Geography                                     GEOG            Standard         5, 6, 7             GEOG105                3          Y”
  - equivalencies[IB-GERMAN|3]:  ⟵ “German                   German                                        GERM            Standard         5, 6, 7             GERM202                3          Y”
  - equivalencies[IB-HISTORY|3]:  ⟵ “History                  Varies                                        HIST            Standard         5, 6, 7            HIST elective           3          N”
  - equivalencies[IB-LATIN|6]:  ⟵ “Latin                    Latin                                         LATN        Standard or Higher   5, 6, 7       LATN101 and LATN102          6          Y”
  - equivalencies[IB-PHILOSOPHY|3]:  ⟵ “Philosophy                       Philosophy        PHIL   Standard   5, 6, 7             PHIL101                 3        Y”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics                          Physics           PHYS   Standard   5, 6, 7            PHYS203                  4       Y”
  - equivalencies[IB-PSYCHOLOGY|3]:  ⟵ “Psychology                       Psychology        PSYC   Standard   5, 6, 7            PSYC102                  3       Y”
  - equivalencies[IB-SPANISH|5]:  ⟵ “Spanish                          Spanish           SPAN   Standard     5          SPAN202 or SPAN203            3-4      Y”
### `3e26e6e0b666ccd6` Morgan State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.morgan.edu/office-of-undergraduate-admission-and-recruitment/how-to-apply/dual-enrollment (sha256 4d8ea28f6c23)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “SMART Scholars who graduate high school with a minimum 2.5 GPA, earn 9 college credits toward a degree, have a minimum 980 SAT score (Critical Reading and Mathematics) or 19 ACT composite, complete the admission online application process and meet all non-academic requirements, will be guaranteed ad”
### `m93a483d83523611` Morgan State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.morgan.edu/office-of-the-registrar/transfer-evaluation-and-articulation-services (sha256 f7e978977821)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 3}
  - residency_requirement_credits: 30 ⟵ “If admitted to Morgan as a degree seeking student you must earn the last 30 credit hours toward your desired degree at Morgan State.”
  - residency_requirement_credits: 30 ⟵ “In all cases, the transfer student must earn the last 30 credit hours toward the desired degree at the university as a full-time or part-time student.”
  - residency_requirement_credits: 30 ⟵ “Current students within their last 30 semester hours OR graduating seniors in their final semester will be prohibited from taking courses at other colleges or universities unless they have obtained authorization for a waiver of the 30- hour rule from their Dean's office.”
### `176e1e62571bbf11` Salisbury University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.salisbury.edu/admissions/financial-aid/cost-of-attendance/ (sha256 8e33aa7bb3d4)
- checks: {"columns": 1, "rows": 4}
  - column:Tuition and Mandatory Fees: 23590 ⟵ “Tuition and Mandatory Fees | $11,466 | $23,590”
  - column:Housing*: 8150 ⟵ “Housing* | $8,150 | $8,150”
  - column:Food**: 6368 ⟵ “Food** | $6,368 | $6,368”
  - column:Direct Costs: 38108 ⟵ “Direct Costs | $25,984 | $38,108”
### `2bfe8a0d6d955e49` Salisbury University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.salisbury.edu/admissions/financial-aid/cost-of-attendance/ (sha256 8e33aa7bb3d4)
- checks: {"columns": 1, "rows": 4}
  - column:Tuition and Mandatory Fees: 11466 ⟵ “Tuition and Mandatory Fees | $11,466 | $23,590”
  - column:Housing*: 8150 ⟵ “Housing* | $8,150 | $8,150”
  - column:Food**: 6368 ⟵ “Food** | $6,368 | $6,368”
  - column:Direct Costs: 25984 ⟵ “Direct Costs | $25,984 | $38,108”
### `37c1ebdbc3e56bbb` Salisbury University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.salisbury.edu/administration/academic-affairs/registrar/records-and-registration/dual-enrollment.aspx (sha256 81bd7d72954c)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 2}
  - eligibility_tier: 2.75 ⟵ “Has an overall unweighted grade point average of at least 2.75”
  - eligibility_tier: 2.75 ⟵ “Has an overall weighted grade point average of at least 2.75”
  - eligibility_tier: 2.75 ⟵ “Has an overall weighted grade point average of at least 2.75”
  - per_credit_hour_charge: 150 ⟵ “The tuition for dual enrollment (inclusive of all fees) is $150 per credit hour.”
  - eligibility_tier: 2.75 ⟵ “Has an overall weighted grade point average of at least 2.75”
  - per_credit_hour_charge: 150 ⟵ “The tuition for dual enrollment (inclusive of all fees) is $150 per credit hour.”
### `e33d3d670ab4f90f` Salisbury University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.salisbury.edu/administration/academic-affairs/registrar/transfer-credit/ (sha256 1efc41f30211)
- checks: {"fields": ["max_transfer_credits", "residency_requirement_credits"]}
  - max_transfer_credits: 70 ⟵ “Bill - Selected Reserves Federal Tuition Assistance Yellow Ribbon Campaign Salute Honor Green Zone Advocate Training Overview Sign Up Now Military Activation Veterans Benefit Certification Request Isakson & Roe Section 1018 Requirements Transfer Credit for Undergraduates General Transfer Policies A maximum of 70 credit hours from two-year institutions and 90 credit hours from four-year institution”
  - residency_requirement_credits: 30 ⟵ “Unless enrolled in an approved cooperative or study abroad program, 30 of the last 37 hours of coursework must be completed at Salisbury University.”
### `33e22c48abddace3` St. Mary's College of Maryland — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.smcm.edu/app/uploads/sites/60/2026/05/CDS_25-26.pdf (sha256 45c5ce5e76e2)
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 2681 ⟵ “Total first-time, first-year (degree-seeking) who applied           2681”
  - admits: 2014 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     2014”
  - enrolled: 352 ⟵ “Total first-time, first-year (degree-seeking) enrolled              352”
### `234d65c289555cb3` St. Mary's College of Maryland — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.smcm.edu/student-financial-assistance/tuition-fees/ (sha256 5b441b6beb3e)
- checks: {"columns": 2, "rows": 10}
  - on_campus:Tuition: 12855 ⟵ “Tuition | $12,855 | $22,855 | $29,909”
  - on_campus:Fees: 3495 ⟵ “Fees | $3,495 | $3,495 | $3,495”
  - on_campus:Housing*: 10390 ⟵ “Housing* | $10,390 | $10,390 | $10,390”
  - on_campus:Meals**: 6990 ⟵ “Meals** | $6,990 | $6,990 | $6,990”
  - on_campus:Billable Charges to SMCM: 33730 ⟵ “Billable Charges to SMCM | $33,730 | $43,730 | $50,784”
  - on_campus:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - on_campus:Transportation: 455 ⟵ “Transportation | $455 | $455 | $1,120”
  - on_campus:Personal Expenses: 1365 ⟵ “Personal Expenses | $1,365 | $1,365 | $1,365”
  - on_campus:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70”
  - on_campus:Comprehensive Cost of Attendance: 36620 ⟵ “Comprehensive Cost of Attendance | $36,620 | $46,620 | $54,339”
  - on_campus:Tuition: 22855 ⟵ “Tuition | $12,855 | $22,855 | $29,909”
  - on_campus:Fees: 3495 ⟵ “Fees | $3,495 | $3,495 | $3,495”
  - on_campus:Housing*: 10390 ⟵ “Housing* | $10,390 | $10,390 | $10,390”
  - on_campus:Meals**: 6990 ⟵ “Meals** | $6,990 | $6,990 | $6,990”
  - on_campus:Billable Charges to SMCM: 43730 ⟵ “Billable Charges to SMCM | $33,730 | $43,730 | $50,784”
  - on_campus:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - on_campus:Transportation: 455 ⟵ “Transportation | $455 | $455 | $1,120”
  - on_campus:Personal Expenses: 1365 ⟵ “Personal Expenses | $1,365 | $1,365 | $1,365”
  - on_campus:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70”
  - on_campus:Comprehensive Cost of Attendance: 46620 ⟵ “Comprehensive Cost of Attendance | $36,620 | $46,620 | $54,339”
### `66481e4b202fa978` St. Mary's College of Maryland — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.smcm.edu/student-financial-assistance/tuition-fees/ (sha256 5b441b6beb3e)
- checks: {"columns": 1, "rows": 10}
  - on_campus:Tuition: 29909 ⟵ “Tuition | $12,855 | $22,855 | $29,909”
  - on_campus:Fees: 3495 ⟵ “Fees | $3,495 | $3,495 | $3,495”
  - on_campus:Housing*: 10390 ⟵ “Housing* | $10,390 | $10,390 | $10,390”
  - on_campus:Meals**: 6990 ⟵ “Meals** | $6,990 | $6,990 | $6,990”
  - on_campus:Billable Charges to SMCM: 50784 ⟵ “Billable Charges to SMCM | $33,730 | $43,730 | $50,784”
  - on_campus:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - on_campus:Transportation: 1120 ⟵ “Transportation | $455 | $455 | $1,120”
  - on_campus:Personal Expenses: 1365 ⟵ “Personal Expenses | $1,365 | $1,365 | $1,365”
  - on_campus:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70”
  - on_campus:Comprehensive Cost of Attendance: 54339 ⟵ “Comprehensive Cost of Attendance | $36,620 | $46,620 | $54,339”
### `m5153bf0cbc3ea58` Stevenson University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.stevenson.edu/admissions-aid/getting-started/transfer-students/ (sha256 653fa679e344)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “The courses and credits completed with a grade of “C” or better at other accredited institutions are generally transferable to Stevenson.”
  - min_grade: C ⟵ “The courses and credits completed with a grade of “C” or better at other accredited institutions are generally transferable to Stevenson.”
### `70c0deec8351bae9` Towson University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.towson.edu/admissions/undergrad/nondegree/highschool.html (sha256 91e87d692c5a)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.5 ⟵ “average GPA of an A or higher, or a weighted GPA of 3.5 or higher. Submitting test”
### `mf8a0ac1efcaf8cf` University of Maryland Eastern Shore — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.umes.edu/transfer-student-services/ (sha256 e12b83fa5d2b)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - residency_requirement_credits: 30 ⟵ “To graduate, students must complete the last 30 semester credit hours at UMES.”
  - residency_requirement_credits: 30 ⟵ “However, to graduate, a student must complete the last 30 semester hours at UMES.”
### `322ed3e005e54d5d` University of Maryland Global Campus — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.umgc.edu/transfers-and-credits/fast-paths-to-credit/credit-by-exam/ap (sha256 f45879904de5)
- checks: {"distinct_exams": 39, "equivalencies": 60, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “AP 2D Art & Design | ARTT Elective | 3, 4, 5 | 3 LL”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, 5]:  ⟵ “AP 3D Art & Design | ARTT Elective | 3, 4, 5 | 3 LL”
  - equivalencies[AP-ART-HISTORY|3, 4, 5]:  ⟵ “AP Art History | ARTH Elective | 3, 4, 5 | 6 LL”
  - equivalencies[AP-BIOLOGY|3, 4, 5]:  ⟵ “AP Biology | BIOL 103 (Satisfies Lecture w/ Lab requirement) | 3, 4, 5 | 4 LL”
  - equivalencies[AP-CALCULUS-AB|3, 4, 5]:  ⟵ “AP Calculus AB | MATH 140 | 3, 4, 5 | 4 LL”
  - equivalencies[AP-CALCULUS-BC|3, 4, 5]:  ⟵ “AP Calculus BC | MATH 140 and MATH 141 | 3, 4, 5 | 8 LL”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “AP Chemistry | CHEM 103 (Satisfies Lecture w/ Lab requirement) | 3 | 4 LL”
  - equivalencies[AP-CHEMISTRY|4, 5]:  ⟵ “AP Chemistry | CHEM 103 and CHEM Elective (Satisfies Lecture w/ Lab requirement) | 4, 5 | 8 LL”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “AP Chinese Language and Culture | CHIN 114, CHIN 115, and CHIN Elective | 3 | 8 LL”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “AP Chinese Language and Culture | CHIN 114, CHIN 115, and CHIN Elective | 4 | 12 LL”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “AP Chinese Language and Culture | CHIN 114, CHIN 115, and CHIN Elective | 5 | 16 LL”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3, 4, 5]:  ⟵ “AP Comparative Government and Politics | GVPT 280 | 3, 4, 5 | 3 LL”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3, 4, 5]:  ⟵ “AP Computer Science A | CMIS 141 | 3, 4, 5 | 4 LL”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “AP Computer Science Principles | CMIS 102 | 3, 4, 5 | 3 LL”
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “AP Drawing | ARTT 110 | 3, 4, 5 | 3 LL”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language and Composition | WRTG 111 and Elective | 3 | 6 LL”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4, 5]:  ⟵ “AP English Language and Composition | WRTG 112 and Elective | 4, 5 | 6 LL”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “AP English Literature and Composition | ENGL 102 | 3 | 3 LL”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4, 5]:  ⟵ “AP English Literature and Composition | ENGL 102 and ENGL 240 | 4, 5 | 6 LL”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3, 4, 5]:  ⟵ “AP Environmental Science | Science Elective (Satisfies Lecture requirement) | 3, 4, 5 | 3 LL”
  - equivalencies[AP-EUROPEAN-HISTORY|3, 4, 5]:  ⟵ “AP European History | HIST 141 and HIST 142 | 3, 4, 5 | 6 LL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “AP French Language | FREN 211 and FREN Elective | 3 | 6 LL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “AP French Language | FREN 211, FREN 212, and FREN Elective | 4 | 9 LL”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “AP French Language | FREN 211, FREN 212, and FREN Elective | 5 | 12 LL”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “AP German Language | GERM 211 and GERM Elective | 3 | 12 LL”
  - … 35 more rows
### `fd4656a679ed0935` University of Maryland Global Campus — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.umgc.edu/transfers-and-credits/fast-paths-to-credit/credit-by-exam/clep (sha256 b6d5d20d96ea)
- checks: {"distinct_exams": 33, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | GVPT 170 | 50 | 3 LL”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | Literature Elective (satisfies Arts & Humanities Gen Ed Requirement) | 50 | 3 LL”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | Literature Elective (satisfies Arts & Humanities Gen Ed Requirement) | 50 | 3 LL”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | BIOL 101 and BIOL Lecture (3 Credits, satisfies Biological & Physical Sciences Gen Ed Requirement) | 50 | 6 LL”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | MATH 140 | 50 | 4 LL”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | CHEM 121 and CHEM Lecture (3 Credits, satisfies Biological & Physical Sciences Gen Ed Requirement) | 50 | 6 LL”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | MATH 107 | 50 | 3 LL”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | WRTG 111 and Elective (3 Credits) | 50 | 6 LL”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | Elective | 50 | 3 LL”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | MATH 105 | 50 | 3 LL”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | Literature Elective (satisfies Arts & Humanities Gen Ed Requirement) | 50 | 6 LL”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | ACCT 220 | 50 | 3 LL”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language (Level 1) | FREN 111 and FREN 112 | 50 | 6 LL”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language (Level 2) | FREN 111, FREN 112, and FREN 211 | 59 | 9 LL”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language (Level 1) | GERM 111 and GERM 112 | 50 | 6 LL”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language (Level 2) | GERM 111, GERM 112, and GERM 211 | 60 | 9 LL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | HIST 156 | 50 | 3 LL”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present | HIST 157 | 50 | 3 LL”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | PSYC 351 | 50 | 3 LL”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | HUMN 100 | 50 | 3 LL”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | IFSM 201 | 50 | 3 LL”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | PSYC Elective (satisfies Behavioral & Social Sciences Gen Ed Requirement) | 50 | 3 LL”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | BMGT 380 | 50 | 3 LL”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PSYC 100 | 50 | 3 LL”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SOCY 100 | 50 | 3 LL”
  - … 12 more rows
### `d4ba9f54d8c3e3d4` University of Maryland-Baltimore County — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/8119-2/ (sha256 174d171c2b58)
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition/Fees: 34183 ⟵ “Tuition/Fees | $14,086 | $34,183”
  - on_campus:Housing: 9428 ⟵ “Housing | $9,248 | $9,428”
  - on_campus:Food: 6490 ⟵ “Food | $6,490 | $6,490”
  - on_campus:Books: 1600 ⟵ “Books | $1,600 | $1,600”
  - on_campus:Transportation: 1900 ⟵ “Transportation | $1,900 | $1,900”
  - on_campus:Other: 7546 ⟵ “Other | $7,546 | $7,546”
  - on_campus:Direct Loan Fee: 142 ⟵ “Direct Loan Fee | $142 | $142”
  - on_campus:PLUS Loan Fee: 1264 ⟵ “PLUS Loan Fee | $1,264 | $1,264”
  - on_campus:Total:: 62553 ⟵ “Total: | $42,456 | $62,553”
### `0edc08cda7c2a508` University of Maryland-College Park — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/tuition-fees/ (sha256 bc797311f4c8)
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 42266.0 ⟵ “Tuition | $42,266.00”
  - column:Additional Differential Tuition for full-time juniors and seniors who are majoring in Business, Engineering, or Computer Science (regardless of residency classification): 3375.0 ⟵ “Additional Differential Tuition for full-time juniors and seniors who are majoring in Business, Engineering, or Computer Science (regardless of residency classification) | $3,375.00”
  - column:Mandatory Fees (includes Tech fee). Maximum charged to all students registered for 9 or more credits: 1820.0 ⟵ “Mandatory Fees (includes Tech fee). Maximum charged to all students registered for 9 or more credits | $1,820.00”
  - column:Board Contract (Resident Dining Plan - Base Plan): 6820.0 ⟵ “Board Contract (Resident Dining Plan - Base Plan) | $6,820.00”
  - column:Room (Standard 2-person w/AC, includes Telecom fee): 10290.0 ⟵ “Room (Standard 2-person w/AC, includes Telecom fee) | $10,290.00”
### `5f9a3a1c98239e89` University of Maryland-College Park — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://academiccatalog.umd.edu/undergraduate/registration-academic-requirements-regulations/transfer-credit/transfer-credit.pdf (sha256 5371db41fc88)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Generally, college-level courses completed at regionally-accredited institutions will be acceptable and awarded transfer credit, provided the course is similar in level, scope, content and expected learning outcomes Applicability of Transfer Courses to to courses offered at the University of Maryland and a grade of "C-" or higher is earned.”
### `0480cd4a0cc89461` Washington College — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.washcoll.edu/people_departments/offices/institutional-research/common_data_sets_cds/common-data-set-2025-2026-use.pdf (sha256 25c09140d714)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 3512 ⟵ “Total first-time, first-year (degree-seeking) who applied                                      1,251               1,852           409             0       3512”
  - admits: 3294 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                                1,165               1,779           350             0       3294”
  - enrolled: 271 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                                       138                 126             7             0         271”
  - sat_composite_25..75: [1080, 1240, 1310] ⟵ “SAT Composite                                       1080                 1240                1310”
  - sat_reading_25..75: [560, 640, 690] ⟵ “SAT Evidence-Based Reading and   560                  640                690”
  - sat_math_25..75: [530, 590, 640] ⟵ “SAT Math                                             530                  590                640”
  - act_25..75: [22, 24, 30] ⟵ “ACT Composite                                        22                    24                 30”
### `007fc99d76b2ce8e` Washington College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.washcoll.edu/people_departments/offices/registrar/transfer-credit.php (sha256 7acf43ca6a3e)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C- ⟵ “Transfer credit is only given for courses taken on a letter grade basis in which a final grade of “C-” or higher is earned.”
  - max_transfer_credits: 72 ⟵ “A maximum of 72 credit hours can be accepted in transfer.”

## Exceptions (433)

### `3253c492b4b9a238` state-MD — state_policies 2024-25 · policy_kind=tuition_residency [new] (labeled_in_source)
- source: https://mhec.maryland.gov/preparing/Pages/24-25-Promise-Scholarship.aspx (sha256 30d8e98c4e7e)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"exceptions": 1, "guarantees": 1, "requirements": 7}
  - statements.requirements: 7 ⟵ “Eligible students can receive up to $5,000 to cover any remaining tuition and mandatory fee expenses after Federal or State financial aid has been applied.”
  - statements.exceptions: 1 ⟵ “Exceptions to submitting a high school transcript: An initial applicant who graduated from high school five or more years before applying for the scholarship is exempt from submitting a high school transcript to document the GPA requirement.”
  - statements.guarantees: 1 ⟵ “No documentation will be accepted through MDCAPS.”
### `6e363a1d074eb969` state-MD — state_policies 2023-24 · policy_kind=tuition_residency [new] (labeled_in_source)
- source: https://mhec.maryland.gov/Documents/Promise%20Conditions%20of%20Award%209.13.23.pdf (sha256 c915b693b3ca)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “At the beginning of each semester, your institution will be asked to certify that you meet the requirements of the award.”
### `8292e0d2038795c8` state-MD — state_policies 2026-27 · policy_kind=tuition_residency [new] (labeled_in_source)
- source: https://mhec.maryland.gov/preparing/SiteAssets/Pages/FinancialAid/CyberSecurity-Scholarship-Program/2026-2027%20Cybersecurity%20Conditions%20of%20Award.pdf (sha256 e960aa81fad6)
- issues: semantic_review_required
- checks: {"requirements": 12}
  - statements.requirements: 12 ⟵ “If you need 120 credits to graduate you must have completed at least 30 credits at the time of application.) o You must be enrolled full-time or part-time. o You must have a 3.0 GPA at the time of application at the institution you are currently enrolled in. o You may not receive the Federal Cyber C”
### `8f662522cb30d2dc` state-MD — state_policies 2026-27 · policy_kind=tuition_residency [new] (labeled_in_source)
- source: https://mhec.maryland.gov/preparing/SiteAssets/Pages/FinancialAid/ProgramDescriptions/prog_delegate/26.27%20Delegate%20Conditions%20of%20Award.pdf (sha256 c195e5be7e0e)
- issues: semantic_review_required, conflicting_sources:https://mhec.maryland.gov/preparing/SiteAssets/Pages/FinancialAid/ProgramDescriptions/prog_senatorial/26.27%20Senatorial%20Conditions%20of%20Award.pdf
- checks: {"requirements": 4}
  - statements.requirements: 4 ⟵ “217 E Redwood Street                                                                                                                            DELEGATE SCHOLARSHIP (410) 767-3300; (800) 974-0203                                                                                                         ”
### `fc5b08cdd7c26aa3` state-MD — state_policies 2026-27 · policy_kind=tuition_residency [new] (labeled_in_source)
- source: https://mhec.maryland.gov/preparing/SiteAssets/Pages/FinancialAid/ProgramDescriptions/prog_senatorial/26.27%20Senatorial%20Conditions%20of%20Award.pdf (sha256 1825584a5772)
- issues: semantic_review_required, conflicting_sources:https://mhec.maryland.gov/preparing/SiteAssets/Pages/FinancialAid/ProgramDescriptions/prog_delegate/26.27%20Delegate%20Conditions%20of%20Award.pdf
- checks: {"requirements": 4}
  - statements.requirements: 4 ⟵ “217 E Redwood Street                                                                                                                     SENATORIAL SCHOLARSHIP (410) 767-3300; (800) 974-0203                                                                                                              ”
### `03a8872f3dcc36f7` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-early-childhood-development-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18460&returnto=18122 (sha256 dc57c78c8099)
- issues: requirement_groups_skipped
- checks: {"courses": 24, "groups": 7, "groups_skipped": 18}
  - program_name: Program Name: Early Childhood Development (A.A.S.) ⟵ “Program Name: Early Childhood Development (A.A.S.) - Anne Arundel Community College”
### `0775044030128d5d` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-homeland-security-management-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18488&returnto=18122 (sha256 a94480b17f64)
- issues: requirement_groups_skipped
- checks: {"courses": 22, "groups": 7, "groups_skipped": 17}
  - program_name: Program Name: Homeland Security Management (A.A.S.) ⟵ “Program Name: Homeland Security Management (A.A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `14759c4ad386c7b5` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-business-administration-transfer-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18423&returnto=18122 (sha256 7472b56e5398)
- issues: requirement_groups_skipped
- checks: {"courses": 11, "groups": 6, "groups_skipped": 18}
  - program_name: Program Name: Business Administration Transfer (A.S.) ⟵ “Program Name: Business Administration Transfer (A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `1aff5299709ec67c` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-engineering-transfer-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18467&returnto=18122 (sha256 d611a13fc853)
- issues: requirement_groups_skipped
- checks: {"courses": 26, "groups": 5, "groups_skipped": 21}
  - program_name: Program Name: Engineering Transfer (A.S.) ⟵ “Program Name: Engineering Transfer (A.S.) - Anne Arundel Community College”
### `1f9c44f0fcbc686a` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-mathematics-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18506&returnto=18122 (sha256 d9f8559fe951)
- issues: requirement_groups_skipped
- checks: {"courses": 28, "groups": 6, "groups_skipped": 18}
  - program_name: Program Name: Mathematics (A.S.) ⟵ “Program Name: Mathematics (A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `3087c75e66e31b61` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
- checks: {"courses": 42, "groups": 9, "groups_skipped": 20}
  - program_name: Program Name: Information Assurance and Cybersecurity (A.A.S.) ⟵ “Program Name: Information Assurance and Cybersecurity (A.A.S.) - Anne Arundel Community College”
### `352cbf9348e7493c` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-cisco-certified-network-associate-ccna-preparation-certificate [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18441&returnto=18122 (sha256 5bec9b5f35ab)
- issues: requirement_groups_skipped
- checks: {"courses": 3, "groups": 2, "groups_skipped": 12}
  - program_name: Program Name: Cisco Certified Network Associate (CCNA) Preparation (certificate) ⟵ “Program Name: Cisco Certified Network Associate (CCNA) Preparation (certificate) - Anne Arundel Community College”
  - total_credits: 12 ⟵ “Total Credit Hours: 12”
### `3ac042860767154b` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-human-services-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18496&returnto=18122 (sha256 914ad51cf333)
- issues: requirement_groups_skipped
- checks: {"courses": 20, "groups": 5, "groups_skipped": 25}
  - program_name: Program Name: Human Services (A.A.S.) ⟵ “Program Name: Human Services (A.A.S.) - Anne Arundel Community College”
### `3bd31e9dcf545695` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-transfer-studies-a-a [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18539&returnto=18122 (sha256 8d2e1432cb25)
- issues: requirement_groups_skipped
- checks: {"courses": 3, "groups": 4, "groups_skipped": 21}
  - program_name: Program Name: Transfer Studies (A.A.) ⟵ “Program Name: Transfer Studies (A.A.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `402fc296163006af` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-paralegal-studies-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18513&returnto=18122 (sha256 c3d16406fe1b)
- issues: requirement_groups_skipped
- checks: {"courses": 16, "groups": 5, "groups_skipped": 20}
  - program_name: Program Name: Paralegal Studies (A.A.S.) ⟵ “Program Name: Paralegal Studies (A.A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total credit hours: 60”
### `50ade31760d4c660` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
- checks: {"courses": 24, "groups": 8, "groups_skipped": 25}
  - program_name: Program Name: Medical Laboratory Technician (A.A.S.) ⟵ “Program Name: Medical Laboratory Technician (A.A.S.) - Anne Arundel Community College”
  - total_credits: 67 ⟵ “Total Credit Hours: 67”
### `52c9ab5e22a557c7` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-electronics-engineering-technology-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18466&returnto=18122 (sha256 f2980187d2c8)
- issues: requirement_groups_skipped
- checks: {"courses": 40, "groups": 7, "groups_skipped": 16}
  - program_name: Program Name: Electronics Engineering Technology (A.A.S.) ⟵ “Program Name: Electronics Engineering Technology (A.A.S.) - Anne Arundel Community College”
  - total_credits: 63 ⟵ “Total Credit Hours: 63”
### `71bccc30020b64c9` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-addiction-counseling-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18401&returnto=18122 (sha256 b9221a538e84)
- issues: requirement_groups_skipped
- checks: {"courses": 19, "groups": 5, "groups_skipped": 24}
  - program_name: Program Name: Addiction Counseling (A.A.S.) ⟵ “Program Name: Addiction Counseling (A.A.S.) - Anne Arundel Community College”
### `7228623d86759a49` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-elementary-education-elementary-special-education-a-a-t [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18462&returnto=18122 (sha256 58a92cce1255)
- issues: requirement_groups_skipped
- checks: {"courses": 21, "groups": 7, "groups_skipped": 17}
  - program_name: Program Name: Elementary Education/Elementary Special Education (A.A.T.) ⟵ “Program Name: Elementary Education/Elementary Special Education (A.A.T.) - Anne Arundel Community College”
  - total_credits: 63 ⟵ “Total Credit Hours: 63”
### `74d5e29755a8e3b5` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-web-and-mobile-application-development-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18454&returnto=18122 (sha256 003ac53181a3)
- issues: requirement_groups_skipped
- checks: {"courses": 18, "groups": 6, "groups_skipped": 18}
  - program_name: Program Name: Web and Mobile Application Development (A.A.S.) ⟵ “Program Name: Web and Mobile Application Development (A.A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `7d35571db91143f9` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-kinesiology-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18486&returnto=18122 (sha256 1d9812f21d5b)
- issues: requirement_groups_skipped
- checks: {"courses": 30, "groups": 6, "groups_skipped": 19}
  - program_name: Program Name: Kinesiology (A.S.) ⟵ “Program Name: Kinesiology (A.S.) - Anne Arundel Community College”
### `8225affb41c588c4` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-nursing-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped
- checks: {"courses": 34, "groups": 9, "groups_skipped": 29}
  - program_name: Program Name: Nursing (A.S.) ⟵ “Program Name: Nursing (A.S.) - Anne Arundel Community College”
### `8cd78ef1e65e0325` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-radiologic-technology-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped
- checks: {"courses": 20, "groups": 8, "groups_skipped": 27}
  - program_name: Program Name: Radiologic Technology (A.A.S.) ⟵ “Program Name: Radiologic Technology (A.A.S.) - Anne Arundel Community College”
### `99f62160c45aaab3` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-surgical-technology-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18523&returnto=18122 (sha256 83c37b6ff24b)
- issues: requirement_groups_skipped
- checks: {"courses": 19, "groups": 5, "groups_skipped": 22}
  - program_name: Program Name: Surgical Technology (A.A.S.) ⟵ “Program Name: Surgical Technology (A.A.S.) - Anne Arundel Community College”
### `b7ffc4a5a9c2c2bf` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-entrepreneurship-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18473&returnto=18122 (sha256 a897f034277e)
- issues: requirement_groups_skipped
- checks: {"courses": 18, "groups": 4, "groups_skipped": 20}
  - program_name: Program Name: Entrepreneurship (A.A.S.) ⟵ “Program Name: Entrepreneurship (A.A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `c8240d421aa70317` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-massage-therapy-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18524&returnto=18122 (sha256 17b5ea90f9b1)
- issues: requirement_groups_skipped
- checks: {"courses": 17, "groups": 4, "groups_skipped": 21}
  - program_name: Program Name: Massage Therapy (A.A.S.) ⟵ “Program Name: Massage Therapy (A.A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `d4f8a0e256634db4` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped
- checks: {"courses": 30, "groups": 10, "groups_skipped": 19}
  - program_name: Program Name: Architecture and Interior Design (A.A.S.) ⟵ “Program Name: Architecture and Interior Design (A.A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `d8074dab7dd441b4` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-mechatronics-engineering-technology-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18472&returnto=18122 (sha256 7beddb2ca1f0)
- issues: requirement_groups_skipped
- checks: {"courses": 40, "groups": 6, "groups_skipped": 17}
  - program_name: Program Name: Mechatronics Engineering Technology (A.A.S.) ⟵ “Program Name: Mechatronics Engineering Technology (A.A.S.) - Anne Arundel Community College”
### `da53c9588e11bbd0` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-physical-therapist-assistant-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18518&returnto=18122 (sha256 393dbc3378ab)
- issues: requirement_groups_skipped
- checks: {"courses": 21, "groups": 5, "groups_skipped": 27}
  - program_name: Program Name: Physical Therapist Assistant (A.A.S.) ⟵ “Program Name: Physical Therapist Assistant (A.A.S.) - Anne Arundel Community College”
### `dfe37b7ad56d02b7` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-early-childhood-education-early-childhood-special-education-a-a-t [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18461&returnto=18122 (sha256 94a982ece7eb)
- issues: requirement_groups_skipped
- checks: {"courses": 21, "groups": 7, "groups_skipped": 17}
  - program_name: Program Name: Early Childhood Education/Early Childhood Special Education (A.A.T.) ⟵ “Program Name: Early Childhood Education/Early Childhood Special Education (A.A.T.) - Anne Arundel Community College”
  - total_credits: 63 ⟵ “Total Credit Hours: 63”
### `e512a36eca912142` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-law-and-jurisprudence-a-a [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18500&returnto=18122 (sha256 cba5e6015d8f)
- issues: requirement_groups_skipped
- checks: {"courses": 25, "groups": 6, "groups_skipped": 17}
  - program_name: Program Name: Law and Jurisprudence (A.A.) ⟵ “Program Name: Law and Jurisprudence (A.A.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `ee726fdda9aeb7ff` Anne Arundel Community College — academic_programs 2026-27 · program_key=program-name-law-enforcement-and-criminal-justice-a-a-s [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18501&returnto=18122 (sha256 6891dce62abe)
- issues: requirement_groups_skipped
- checks: {"courses": 21, "groups": 6, "groups_skipped": 20}
  - program_name: Program Name: Law Enforcement and Criminal Justice (A.A.S.) ⟵ “Program Name: Law Enforcement and Criminal Justice (A.A.S.) - Anne Arundel Community College”
  - total_credits: 60 ⟵ “Total Credit Hours: 60”
### `4277a5a89a782da5` Anne Arundel Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/verification/ (sha256 ba5ab2b2e779)
- issues: semantic_review_required, conflicting_sources:https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/complete-the-fafsa/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/dependency-status/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “More Financial Aid Cost of Attendance Dependency Status Forms General Eligibility Requirements Satisfactory Academic Progress Special Circumstances Verification Noncredit Funding Waivers Return of Title IV Funds It Starts with the FAFSA Grants, loans, scholarships and work study - Financial Aid begins with the FAFSA.”
### `44f89c445c93c4e5` Anne Arundel Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/special-circumstances/ (sha256 c9a91cf66fdf)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustments for the Documented Purchase of a Computer This adjustment does not guarantee more financial aid money to be offered, but it adjusts the overall cost of attendance used to determine financial need for the academic school year.”
  - sentence: budget_increase ⟵ “Complete a Cost of Attendance Increase Form, available at the AACC financial aid office.”
### `9396927004206450` Anne Arundel Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/financial-aid-forms/ (sha256 0d49eaaff00b)
- issues: semantic_review_required, conflicting_sources:https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Forms The Appeal for Reinstatement of Financial Aid is found on MyAACC.”
### `94c23e2eb546cc3d` Anne Arundel Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/dependency-status/ (sha256 7db176d435e5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “However, most students would get more financial aid if their parents complete the FAFSA or if the student is granted a dependency override.”
### `96d8b0c6ffe56f37` Anne Arundel Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/dependency-status/ (sha256 7db176d435e5)
- issues: semantic_review_required, conflicting_sources:https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/complete-the-fafsa/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/special-circumstances/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/verification/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Dependency Appeals for Unusual Circumstances If you have unusual family circumstances that are not covered by the questions of the FAFSA, you may be able appeal to our office for Independent Status.”
  - sentence: need_based_special_circumstances ⟵ “Abusive family environment Abandonment If you have other unusual circumstances that you think might qualify, contact our office to discuss your situation in more detail.”
  - sentence: need_based_special_circumstances ⟵ “Students and families who experienced a significant income reduction from what was originally reported on the FAFSA should inquire about a Special Circumstance Appeal.”
  - sentence: need_based_special_circumstances ⟵ “If this is challenging and no other unusual circumstances apply you can answer "Yes" to the question that asks, "Are the student’s parents unwilling to provide their information, but the student doesn’t have an unusual circumstance that prevents them from contacting the parents or obtaining their information?" Once your FAFSA is received, our office will present more information on this process.”
### `d0c00dea010355c8` Anne Arundel Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/ (sha256 f8e832cc36d5)
- issues: semantic_review_required, conflicting_sources:https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Dec. 1: Priority deadline for Satisfactory Academic Progress (SAP) appeals for the fall term Appeals received after the priority deadline are not guaranteed to be reviewed by the end of the term.”
  - sentence: sap_appeal ⟵ “May 1: Priority deadline for Satisfactory Academic Progress (SAP) appeals for the spring term Appeals received after the priority deadline are not guaranteed to be reviewed by the end of the term.”
  - sentence: sap_appeal ⟵ “Aug. 1: Priority deadline for Satisfactory Academic Progress (SAP) appeals for the summer term Appeals received after the priority deadline are not guaranteed to be reviewed by the end of the term.”
  - sentence: sap_appeal ⟵ “SAP appeals are submitted for the last term you attended, not for the current term you are attending.”
### `d53f42814457e951` Anne Arundel Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/special-circumstances/ (sha256 c9a91cf66fdf)
- issues: semantic_review_required, conflicting_sources:https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/complete-the-fafsa/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/dependency-status/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/verification/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Through the process of a Special Circumstance Review, we consider each situation on a case-by-case basis.”
  - sentence: need_based_special_circumstances ⟵ “Common special circumstances include, but are not limited to: unemployment, decreased annual income and divorce or separation.”
  - sentence: need_based_special_circumstances ⟵ “Please note the special circumstances process is based on several assumptions: We will only begin the adjustment process if we think it will help increase your financial aid awards.”
  - sentence: need_based_special_circumstances ⟵ “Next Steps If you think you have eligible special circumstances: Make sure you received and reviewed your financial aid offer from our office.”
  - sentence: need_based_special_circumstances ⟵ “If we think you might benefit from adjustments, we will email you a Special Circumstances Form to be returned to our office along with all required documentation.”
### `eaeae30b137aa27a` Anne Arundel Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/ (sha256 f8e832cc36d5)
- issues: semantic_review_required, conflicting_sources:https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/complete-the-fafsa/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/dependency-status/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/special-circumstances/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/verification/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “This can only be done in unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “The term unusual circumstances refers to conditions that justify a financial aid administrator making an adjustment to a student's dependency status based on a unique situation, more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Have a change in income from what was originally reported on the FAFSA The FAFSA determines each student's or family's financial need based on their income and benefits that were reported.”
  - sentence: need_based_special_circumstances ⟵ “The term special circumstances refers to the financial situations that justify an aid administrator adjusting elements on the FAFSA to recalculate a financial aid offer.”
  - sentence: need_based_special_circumstances ⟵ “Learn more about special circumstances.”
### `f55c344040f19556` Anne Arundel Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/complete-the-fafsa/ (sha256 aad05324c8a3)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/dependency-status/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/special-circumstances/,https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/financial-aid-and-scholarships/verification/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Changing Your FAFSA If you feel your FAFSA does not accurately reflect your current financial situation, our office may be able to make an adjustment through a special circumstance review once a financial aid offer has been made.”
### `2b0ae936cd1be632` Anne Arundel Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/credit-tuition-and-fees/ (sha256 4ecd4ccc2cdf)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 8}
  - with_parents_or_family:Tuition and Fees: 4586 ⟵ “Tuition and Fees | $4,586 | $4,586”
  - with_parents_or_family:Books, course materials, supplies, and equipment: 672 ⟵ “Books, course materials, supplies, and equipment | $672 | $672”
  - with_parents_or_family:Transportation: 2080 ⟵ “Transportation | $2,080 | $2,080”
  - with_parents_or_family:Housing: 0 ⟵ “Housing | $0 | $7,136”
  - with_parents_or_family:Food: 3072 ⟵ “Food | $3,072 | $3,072”
  - with_parents_or_family:Loan Fees: 298 ⟵ “Loan Fees | $298 | $298”
  - with_parents_or_family:Personal expenses: 6624 ⟵ “Personal expenses | $6,624 | $6,624”
  - with_parents_or_family:Totals: 17332 ⟵ “Totals | $17,332 | $24,468”
  - off_campus_not_with_family:Tuition and Fees: 4586 ⟵ “Tuition and Fees | $4,586 | $4,586”
  - off_campus_not_with_family:Books, course materials, supplies, and equipment: 672 ⟵ “Books, course materials, supplies, and equipment | $672 | $672”
  - off_campus_not_with_family:Transportation: 2080 ⟵ “Transportation | $2,080 | $2,080”
  - off_campus_not_with_family:Housing: 7136 ⟵ “Housing | $0 | $7,136”
  - off_campus_not_with_family:Food: 3072 ⟵ “Food | $3,072 | $3,072”
  - off_campus_not_with_family:Loan Fees: 298 ⟵ “Loan Fees | $298 | $298”
  - off_campus_not_with_family:Personal expenses: 6624 ⟵ “Personal expenses | $6,624 | $6,624”
  - off_campus_not_with_family:Totals: 24468 ⟵ “Totals | $17,332 | $24,468”
### `33fd01309094a271` Anne Arundel Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.aacc.edu/costs-and-paying/credit-costs-and-payment/credit-tuition-and-fees/ (sha256 4ecd4ccc2cdf)
- issues: residency_unknown
- checks: {"columns": 2, "rows": 8}
  - with_parents_or_family:Tuition and Fees: 4826 ⟵ “Tuition and Fees | $4,826 | $4,826”
  - with_parents_or_family:Books, course materials, supplies, and equipment: 672 ⟵ “Books, course materials, supplies, and equipment | $672 | $672”
  - with_parents_or_family:Transportation: 2240 ⟵ “Transportation | $2,240 | $2,240”
  - with_parents_or_family:Housing: 0 ⟵ “Housing | $0 | $7,200”
  - with_parents_or_family:Food: 3392 ⟵ “Food | $3,392 | $3,392”
  - with_parents_or_family:Loan Fees: 306 ⟵ “Loan Fees | $306 | $306”
  - with_parents_or_family:Personal expenses: 7552 ⟵ “Personal expenses | $7,552 | $7,552”
  - with_parents_or_family:Totals: 18988 ⟵ “Totals | $18,988 | $26,188”
  - off_campus_not_with_family:Tuition and Fees: 4826 ⟵ “Tuition and Fees | $4,826 | $4,826”
  - off_campus_not_with_family:Books, course materials, supplies, and equipment: 672 ⟵ “Books, course materials, supplies, and equipment | $672 | $672”
  - off_campus_not_with_family:Transportation: 2240 ⟵ “Transportation | $2,240 | $2,240”
  - off_campus_not_with_family:Housing: 7200 ⟵ “Housing | $0 | $7,200”
  - off_campus_not_with_family:Food: 3392 ⟵ “Food | $3,392 | $3,392”
  - off_campus_not_with_family:Loan Fees: 306 ⟵ “Loan Fees | $306 | $306”
  - off_campus_not_with_family:Personal expenses: 7552 ⟵ “Personal expenses | $7,552 | $7,552”
  - off_campus_not_with_family:Totals: 26188 ⟵ “Totals | $18,988 | $26,188”
### `00bbde8e2d2e1382` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-entrepreneurship-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18473&returnto=18122 (sha256 a897f034277e)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `01545b4508901b80` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-enforcement-and-criminal-justice-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18501&returnto=18122 (sha256 6891dce62abe)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `039a6047907583be` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-human-services-a-a-s · requirement_key=technology-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18496&returnto=18122 (sha256 914ad51cf333)
- issues: requirement_groups_skipped
  - courses: CTA 100 ⟵ “CTA 100 - Computing and Information Technology 3 credit hours OR”
  - courses: CTA 103 ⟵ “CTA 103 - Computer Technology and Artificial Intelligence 3 credit hours”
### `056c8ae7b321e23d` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-paralegal-studies-a-a-s · requirement_key=program-requirements-39-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18513&returnto=18122 (sha256 c3d16406fe1b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: LGS 111 ⟵ “LGS 111 - Introduction to Paralegal Studies 3 credit hours”
  - courses: LGS 112 ⟵ “LGS 112 - Law Office Practice and Technology 3 credit hours”
  - courses: LGS 141 ⟵ “LGS 141 - Electronic Legal Research 1 credit hour”
  - courses: LGS 142 ⟵ “LGS 142 - Evidence and Electronic Discovery 1 credit hour”
  - courses: LGS 143 ⟵ “LGS 143 - Legal Research and Writing 1 3 credit hours”
  - courses: LGS 144 ⟵ “LGS 144 - Legal Research and Writing 2 3 credit hours”
  - courses: LGS 170 ⟵ “LGS 170 - Civil Procedure 3 credit hours”
  - courses: LGS 210 ⟵ “LGS 210 - Legal Ethics 3 credit hours”
  - courses: LGS 215 ⟵ “LGS 215 - Criminal Law 3 credit hours”
  - courses: LGS 253 ⟵ “LGS 253 - Business Law 1 3 credit hours”
  - courses: LGS 160 ⟵ “LGS 160 - Domestic Relations 3 credit hours”
  - courses: LGS 171 ⟵ “LGS 171 - Tort Law 3 credit hours”
### `0682932dd64cea31` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-radiologic-technology-a-a-s · requirement_key=english-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 101A ⟵ “ENG 101A - Academic Writing and Research 1 3 credit hours”
### `06a1c1b5fc6208f7` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-education-early-childhood-special-education-a-a-t · requirement_key=mathematics-8-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18461&returnto=18122 (sha256 94a982ece7eb)
- issues: requirement_groups_skipped
  - courses: MAT 221 ⟵ “MAT 221 - Fundamental Concepts of Mathematics 1 4 credit hours”
  - courses: MAT 222 ⟵ “MAT 222 - Fundamental Concepts of Mathematics 2 4 credit hours”
### `0962bb76875e6267` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-enforcement-and-criminal-justice-a-a-s · requirement_key=program-requirements-24-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18501&returnto=18122 (sha256 6891dce62abe)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CJS 111 ⟵ “CJS 111 - Introduction to Criminal Justice 3 credit hours”
  - courses: CJS 112 ⟵ “CJS 112 - Police Operations 3 credit hours”
  - courses: CJS 113 ⟵ “CJS 113 - Penology 3 credit hours”
  - courses: CJS 121 ⟵ “CJS 121 - Police Administration 3 credit hours”
  - courses: CJS 222 ⟵ “CJS 222 - Investigation and Criminalistics 4 credit hours”
  - courses: CJS 225 ⟵ “CJS 225 - Criminal Justice Ethics 3 credit hours”
  - courses: CJS 260 ⟵ “CJS 260 - Terrorism/Counterterrorism 3 credit hours”
  - courses: HLS 111 ⟵ “HLS 111 - Introduction to Homeland Security 3 credit hours”
  - courses: LGS 215 ⟵ “LGS 215 - Criminal Law 3 credit hours”
### `0af7e8fbfb301601` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=term-2-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped
  - courses: NUR 220 ⟵ “NUR 220 - Nursing of Adult Clients in Health and Illness 2 5 credit hours”
  - courses: NUR 221 ⟵ “NUR 221 - Nursing Care of Children and Families 4 credit hours”
### `0c0feefc51841eaa` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-development-a-a-s · requirement_key=elective-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18460&returnto=18122 (sha256 dc57c78c8099)
- issues: requirement_groups_skipped
  - courses: CTA 100 ⟵ “CTA 100 - Computing and Information Technology 3 credit hours”
### `0f19fe8bd646541e` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=networking-area-of-concentration-requirements-23-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
  - courses: CTP 114 ⟵ “CTP 114 - Introduction to Python with AI 3 credit hours”
  - courses: CTS 130 ⟵ “CTS 130 - Networking 1 4 credit hours”
  - courses: CTS 131 ⟵ “CTS 131 - Networking 2 4 credit hours”
  - courses: CTS 230 ⟵ “CTS 230 - Networking 3 4 credit hours”
  - courses: CTS 233 ⟵ “CTS 233 - Network Programming 4 credit hours”
  - courses: CTS 170 ⟵ “CTS 170 - Digital Forensics 1  3 credit hours”
  - courses: CTS 216 ⟵ “CTS 216 - Network Forensics  4 credit hours”
  - courses: CTS 222 ⟵ “CTS 222 - Linux System Administration  4 credit hours”
  - courses: CTS 236 ⟵ “CTS 236 - Virtualization & Cloud  4 credit hours”
  - courses: STM 213 ⟵ “STM 213 - Professional Skills for STEM  1 credit hour”
### `14474e9da6ddae44` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-web-and-mobile-application-development-a-a-s · requirement_key=mathematics-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18454&returnto=18122 (sha256 003ac53181a3)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MAT 145 ⟵ “MAT 145 - Precalculus 1 3 credit hours”
### `15a1d5e0c00a4f6e` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-massage-therapy-a-a-s · requirement_key=general-education-requirements-25-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18524&returnto=18122 (sha256 17b5ea90f9b1)
- issues: requirement_groups_skipped
  - courses: BIO 230 ⟵ “BIO 230 - Structure and Function of the Human Body 4 credit hours”
  - courses: CTA 100 ⟵ “CTA 100 - Computing and Information Technology 3 credit hours OR”
  - courses: CTA 103 ⟵ “CTA 103 - Computer Technology and Artificial Intelligence 3 credit hours”
### `173b5fa76a8e0608` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-business-administration-transfer-a-s · requirement_key=social-and-behavioral-sciences-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18423&returnto=18122 (sha256 7472b56e5398)
- issues: requirement_groups_skipped
  - courses: ECO 211 ⟵ “ECO 211 - Principles of Economics 1 3 credit hours”
### `1d4a2c2f80a2aef6` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-electronics-engineering-technology-a-a-s · requirement_key=mathematics-3-4-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18466&returnto=18122 (sha256 f2980187d2c8)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MAT 137 ⟵ “MAT 137 - College Algebra 3 credit hours”
  - courses: MAT 145 ⟵ “MAT 145 - Precalculus 1 3 credit hours”
  - courses: MAT 151 ⟵ “MAT 151 - Accelerated Precalculus 4 credit hours”
  - courses: MAT 191 ⟵ “MAT 191 - Calculus and Analytic Geometry 1 4 credit hours”
### `1f5c4b4cb9ed748d` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s · requirement_key=english-composition-3-credits-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `1facce2e19f6cae7` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mathematics-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18506&returnto=18122 (sha256 d9f8559fe951)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `1fb676fb7ad9ce8a` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mechatronics-engineering-technology-a-a-s · requirement_key=mathematics-3-4-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18472&returnto=18122 (sha256 7beddb2ca1f0)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MAT 137 ⟵ “MAT 137 - College Algebra 3 credit hours”
  - courses: MAT 145 ⟵ “MAT 145 - Precalculus 1 3 credit hours OR”
  - courses: MAT 151 ⟵ “MAT 151 - Accelerated Precalculus 4 credit hours OR”
  - courses: MAT 191 ⟵ “MAT 191 - Calculus and Analytic Geometry 1 4 credit hours”
### `2124bfff93f6e13f` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-development-a-a-s · requirement_key=biological-and-physical-sciences-4-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18460&returnto=18122 (sha256 dc57c78c8099)
- issues: requirement_groups_skipped
  - courses: PHS 100 ⟵ “PHS 100 - General Physical Science 4 credit hours”
### `23eff287f21e87a0` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `2571a3bffa5821ad` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-kinesiology-a-s · requirement_key=additional-general-education-requirements-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18486&returnto=18122 (sha256 1d9812f21d5b)
- issues: requirement_groups_skipped
  - courses: HEA 100 ⟵ “HEA 100 - Assessment and Theory of Fitness and Health  3 credit hours”
### `265bfa0b3520cd11` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=security-area-of-concentration-requirements-23-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
  - courses: CTS 130 ⟵ “CTS 130 - Networking 1 4 credit hours”
  - courses: CTS 131 ⟵ “CTS 131 - Networking 2 4 credit hours”
  - courses: CTS 240 ⟵ “CTS 240 - Advanced Network Defense 4 credit hours”
  - courses: CTS 242 ⟵ “CTS 242 - Network Intrusion Detection and Penetration Testing 4 credit hours”
  - courses: CTP 114 ⟵ “CTP 114 - Introduction to Python with AI  3 credit hours”
  - courses: CTP 115 ⟵ “CTP 115 - Introductory Object-Oriented Program Analysis and Design  4 credit hours”
  - courses: CTP 130 ⟵ “CTP 130 - Programming in PHP/MySQL  3 credit hours”
  - courses: CTS 170 ⟵ “CTS 170 - Digital Forensics 1  3 credit hours”
  - courses: CTS 216 ⟵ “CTS 216 - Network Forensics  4 credit hours”
  - courses: CTS 222 ⟵ “CTS 222 - Linux System Administration  4 credit hours”
  - courses: CTS 236 ⟵ “CTS 236 - Virtualization & Cloud  4 credit hours”
  - courses: STM 213 ⟵ “STM 213 - Professional Skills for STEM  1 credit hour”
### `280d9e6d45b03cb6` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-cisco-certified-network-associate-ccna-preparation-certificate · requirement_key=certificate-requirements-12-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18441&returnto=18122 (sha256 5bec9b5f35ab)
- issues: requirement_groups_skipped
  - courses: CTS 130 ⟵ “CTS 130 - Networking 1 4 credit hours”
  - courses: CTS 131 ⟵ “CTS 131 - Networking 2 4 credit hours”
  - courses: CTS 230 ⟵ “CTS 230 - Networking 3 4 credit hours”
### `2f14c3747f725db8` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-cisco-certified-network-associate-ccna-preparation-certificate · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18441&returnto=18122 (sha256 5bec9b5f35ab)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `2f3043d1b96e2e7f` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=mathematics-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped
  - courses: MAT 145 ⟵ “MAT 145 - Precalculus 1  3 credit hours”
### `3098a09eca809b84` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-radiologic-technology-a-a-s · requirement_key=prerequisites [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 231 ⟵ “BIO 231 - Human Biology 1 4 credit hours AND”
  - courses: BIO 232 ⟵ “BIO 232 - Human Biology 2 4 credit hours”
  - courses: BIO 233 ⟵ “BIO 233 - Anatomy and Physiology 1 4 credit hours AND”
  - courses: BIO 234 ⟵ “BIO 234 - Anatomy and Physiology 2 4 credit hours”
  - courses: MAT 137 ⟵ “MAT 137 - College Algebra 3 credit hours”
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
### `31aa58e639a50bb0` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-paralegal-studies-a-a-s · requirement_key=mathematics-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18513&returnto=18122 (sha256 c3d16406fe1b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MAT 100 ⟵ “MAT 100 - The Nature of Mathematics 3 credit hours”
### `323e53ee4126c5bf` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s · requirement_key=english-composition-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours OR”
  - courses: ENG 101A ⟵ “ENG 101A - Academic Writing and Research 1 3 credit hours”
### `328b55973c350bff` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-human-services-a-a-s · requirement_key=second-year-term-1 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18496&returnto=18122 (sha256 914ad51cf333)
- issues: requirement_groups_skipped
  - courses: BIO 101 ⟵ “BIO 101 - Foundations of Biology: Molecules and Cells 4 credit hours OR”
  - courses: BIO 230 ⟵ “BIO 230 - Structure and Function of the Human Body 4 credit hours”
  - courses: HUS 130 ⟵ “HUS 130 - Introduction to Family Counseling 3 credit hours”
  - courses: HUS 234 ⟵ “HUS 234 - Trauma Informed Care 2 credit hours”
### `39442c564412eee8` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-addiction-counseling-a-a-s · requirement_key=additional-general-education-requirements-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18401&returnto=18122 (sha256 b9221a538e84)
- issues: requirement_groups_skipped
  - courses: CTA 100 ⟵ “CTA 100 - Computing and Information Technology ​”
  - courses: CTA 103 ⟵ “CTA 103 - Computer Technology and Artificial Intelligence”
### `3ad0cc95f46c6867` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=program-requirements-39-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped
  - courses: ACH 111 ⟵ “ACH 111 - Graphic Communication 1: Composition and Delineation 3 credit hours”
  - courses: ACH 112 ⟵ “ACH 112 - Graphic Communication 2: Design and Representation 3 credit hours”
  - courses: ACH 121 ⟵ “ACH 121 - Construction Technology 1 3 credit hours”
  - courses: ACH 242 ⟵ “ACH 242 - Health and Sustainability in the Built Environment 3 credit hours Wellness Requirement”
  - courses: ACH 245 ⟵ “ACH 245 - Digital Technologies 1 3 credit hours”
  - courses: ACH 255 ⟵ “ACH 255 - Digital Technologies 2 3 credit hours”
### `3af7ddd31604d332` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=interior-design-capstone-studio [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ACH 203 ⟵ “ACH 203 - Commercial Design Studio 4 credit hours”
  - courses: ACH 205 ⟵ “ACH 205 - Residential Studio 4 credit hours”
### `410fd2122f10c66a` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=additional-general-education-electives-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CTA 100 ⟵ “CTA 100 - Computing and Information Technology 3 credit hours”
  - courses: CTA 103 ⟵ “CTA 103 - Computer Technology and Artificial Intelligence 3 credit hours”
  - courses: UAS 111 ⟵ “UAS 111 - Introduction to Drone Technology 3 credit hours”
### `43badbc4924503b8` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-surgical-technology-a-a-s · requirement_key=first-year-term-1 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18523&returnto=18122 (sha256 83c37b6ff24b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
  - courses: CTA 100 ⟵ “CTA 100 - Computing and Information Technology 3 credit hours”
  - courses: CTA 103 ⟵ “CTA 103 - Computer Technology and Artificial Intelligence 3 credit hours”
  - courses: SGT 100 ⟵ “SGT 100 - Principles of Surgical Technology 1 3 credit hours”
  - courses: SGT 102 ⟵ “SGT 102 - Principles of Surgical Technology 2 6 credit hours”
### `43d3d91f033a0a37` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-electronics-engineering-technology-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18466&returnto=18122 (sha256 f2980187d2c8)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `43da452569f42849` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-development-a-a-s · requirement_key=mathematics-4-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18460&returnto=18122 (sha256 dc57c78c8099)
- issues: requirement_groups_skipped
  - courses: MAT 221 ⟵ “MAT 221 - Fundamental Concepts of Mathematics 1 4 credit hours OR”
  - courses: MAT 222 ⟵ “MAT 222 - Fundamental Concepts of Mathematics 2 4 credit hours”
### `459bcaa04eb99ac2` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-electronics-engineering-technology-a-a-s · requirement_key=additional-general-education-requirements-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18466&returnto=18122 (sha256 f2980187d2c8)
- issues: requirement_groups_skipped
  - courses: CTA 100 ⟵ “CTA 100 - Computing and Information Technology”
  - courses: CTA 103 ⟵ “CTA 103 - Computer Technology and Artificial Intelligence”
  - courses: CTP 115 ⟵ “CTP 115 - Introductory Object-Oriented Program Analysis and Design”
  - courses: CTS 107 ⟵ “CTS 107 - Cyber Essentials”
  - courses: EGR 120 ⟵ “EGR 120 - Introduction to Engineering Design”
  - courses: UAS 111 ⟵ “UAS 111 - Introduction to Drone Technology”
### `45cccabcda79d063` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-massage-therapy-a-a-s · requirement_key=program-requirements-35-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18524&returnto=18122 (sha256 17b5ea90f9b1)
- issues: requirement_groups_skipped
  - courses: MAS 100 ⟵ “MAS 100 - Introduction to Massage 1 credit hour”
  - courses: MAS 108 ⟵ “MAS 108 - The Science of Massage Therapy 4 credit hours”
  - courses: MAS 110 ⟵ “MAS 110 - Fundamentals of Massage Therapy 7 credit hours”
  - courses: MAS 111 ⟵ “MAS 111 - Intermediate Massage Therapy 6 credit hours”
  - courses: MAS 117 ⟵ “MAS 117 - Kinesiology and Clinical Assessment for Massage Therapists 3 credit hours”
  - courses: MAS 118 ⟵ “MAS 118 - Business Fundamentals for Massage Therapists 2 credit hours”
  - courses: MAS 119 ⟵ “MAS 119 - Massage and Bodywork Specialized Modalities 3 credit hours”
  - courses: MAS 120 ⟵ “MAS 120 - Massage Therapy Clinic 1 1 credit hour”
  - courses: MAS 213 ⟵ “MAS 213 - Advanced Massage Therapy 6 credit hours”
  - courses: MAS 220 ⟵ “MAS 220 - Massage Therapy Clinic 2 1 credit hour”
  - courses: MAS 225 ⟵ “MAS 225 - Licensing Exam Prep 1 credit hour”
### `46ceaf6c5f4160d7` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-engineering-transfer-a-s · requirement_key=mathematics-8-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18467&returnto=18122 (sha256 d611a13fc853)
- issues: requirement_groups_skipped
  - courses: MAT 191 ⟵ “MAT 191 - Calculus and Analytic Geometry 1 4 credit hours”
  - courses: MAT 192 ⟵ “MAT 192 - Calculus and Analytic Geometry 2 4 credit hours”
### `484b8e88602755d6` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-web-and-mobile-application-development-a-a-s · requirement_key=biological-and-physical-sciences-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18454&returnto=18122 (sha256 003ac53181a3)
- issues: requirement_groups_skipped
  - courses: BIO 135 ⟵ “BIO 135 - Principles of Nutrition 3 credit hours”
### `49b56f4aaba4adf0` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=term-4 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped
  - courses: NUR 220 ⟵ “NUR 220 - Nursing of Adult Clients in Health and Illness 2 5 credit hours”
  - courses: NUR 221 ⟵ “NUR 221 - Nursing Care of Children and Families 4 credit hours”
### `4b7aa40d2bbce6b4` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-addiction-counseling-a-a-s · requirement_key=english-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18401&returnto=18122 (sha256 b9221a538e84)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `4c4465fd5e5dbfe2` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-physical-therapist-assistant-a-a-s · requirement_key=second-year-fall-term [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18518&returnto=18122 (sha256 393dbc3378ab)
- issues: requirement_groups_skipped
  - courses: PTA 201 ⟵ “PTA 201 - Physical Therapist Assistant 3 4 credit hours”
  - courses: PTA 202 ⟵ “PTA 202 - Physical Therapist Assistant 4 4 credit hours”
  - courses: PTA 203 ⟵ “PTA 203 - Clinical Practice 2 4 credit hours”
### `4d228fa133bb7145` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-web-and-mobile-application-development-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18454&returnto=18122 (sha256 003ac53181a3)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `4d61823edeb6ba74` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-entrepreneurship-a-a-s · requirement_key=social-and-behavioral-sciences-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18473&returnto=18122 (sha256 a897f034277e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ECO 116 ⟵ “ECO 116 - Inside the Global Economy 3 credit hours”
  - courses: ECO 121 ⟵ “ECO 121 - Introduction to Economics 3 credit hours”
  - courses: ECO 211 ⟵ “ECO 211 - Principles of Economics 1 3 credit hours”
### `4f3716718e3517d7` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=term-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 232 ⟵ “BIO 232 - Human Biology 2 4 credit hours”
  - courses: BIO 234 ⟵ “BIO 234 - Anatomy and Physiology 2 4 credit hours”
  - courses: NUR 120 ⟵ “NUR 120 - Foundations for Nursing 7 credit hours”
  - courses: NUR 121 ⟵ “NUR 121 - Basic Physical Assessment 1 credit hour”
  - courses: NUR 122 ⟵ “NUR 122 - Nursing Perspectives 1 1 credit hour”
### `4f9841ed8957dfe5` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-and-jurisprudence-a-a · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18500&returnto=18122 (sha256 cba5e6015d8f)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `555948cf3b24ee45` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-education-early-childhood-special-education-a-a-t · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18461&returnto=18122 (sha256 94a982ece7eb)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `557837a113a1077a` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=term-3-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped
  - courses: NUR 230 ⟵ “NUR 230 - Nursing Management of Clients with Complex Health Problems and Transition into Nursing 9 credit hours”
  - courses: NUR 231 ⟵ “NUR 231 - Nursing Perspectives 2 1 credit hour”
### `584762359a894046` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-surgical-technology-a-a-s · requirement_key=first-year-term-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18523&returnto=18122 (sha256 83c37b6ff24b)
- issues: requirement_groups_skipped
  - courses: SGT 108 ⟵ “SGT 108 - Surgical Procedures 1 4 credit hours”
  - courses: SGT 201 ⟵ “SGT 201 - Surgical Technology Clinical 6 credit hours”
### `58a330d072a2cfc9` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=prerequisites [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 101A ⟵ “ENG 101A - Academic Writing and Research 1 3 credit hours”
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
  - courses: BIO 231 ⟵ “BIO 231 - Human Biology 1 4 credit hours”
  - courses: BIO 232 ⟵ “BIO 232 - Human Biology 2 4 credit hours”
  - courses: BIO 233 ⟵ “BIO 233 - Anatomy and Physiology 1 4 credit hours”
  - courses: BIO 234 ⟵ “BIO 234 - Anatomy and Physiology 2 4 credit hours”
  - courses: PSY 211 ⟵ “PSY 211 - Developmental Psychology 3 credit hours”
  - courses: BIO 223 ⟵ “BIO 223 - General Microbiology 4 credit hours”
### `58b78b50d52cc6c6` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mechatronics-engineering-technology-a-a-s · requirement_key=arts-and-humanities-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18472&returnto=18122 (sha256 7beddb2ca1f0)
- issues: requirement_groups_skipped
  - courses: COM 110 ⟵ “COM 110 - Introduction to Interpersonal Communication 3 credit hours OR”
  - courses: COM 111 ⟵ “COM 111 - Fundamentals of Oral Communication 3 credit hours OR”
  - courses: COM 141 ⟵ “COM 141 - Group Communication and Leadership 3 credit hours”
### `59cfd47e81a148cd` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-massage-therapy-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18524&returnto=18122 (sha256 17b5ea90f9b1)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `59f57b70d276d7ca` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-physical-therapist-assistant-a-a-s · requirement_key=second-year-spring-term [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18518&returnto=18122 (sha256 393dbc3378ab)
- issues: requirement_groups_skipped
  - courses: PTA 204 ⟵ “PTA 204 - Physical Therapist Assistant 5 3 credit hours”
  - courses: PTA 205 ⟵ “PTA 205 - Current Issues and Trends Affecting the Physical Therapist Assistant 1 credit hour”
  - courses: PTA 206 ⟵ “PTA 206 - Clinical Practice 3 4 credit hours”
  - courses: PTA 207 ⟵ “PTA 207 - Clinical Practice 4 4 credit hours”
### `5bfeaea61df05cd1` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-addiction-counseling-a-a-s · requirement_key=biological-and-physical-sciences-4-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18401&returnto=18122 (sha256 b9221a538e84)
- issues: requirement_groups_skipped
  - courses: BIO 101 ⟵ “BIO 101 - Foundations of Biology: Molecules and Cells 4 credit hours OR”
  - courses: BIO 230 ⟵ “BIO 230 - Structure and Function of the Human Body 4 credit hours”
### `5dadc105a3c0de65` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mechatronics-engineering-technology-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18472&returnto=18122 (sha256 7beddb2ca1f0)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `5dc10f6b5c84a7e8` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-kinesiology-a-s · requirement_key=biological-and-physical-sciences-8-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18486&returnto=18122 (sha256 1d9812f21d5b)
- issues: requirement_groups_skipped
  - courses: BIO 101 ⟵ “BIO 101 - Foundations of Biology: Molecules and Cells 4 credit hours”
  - courses: BIO 233 ⟵ “BIO 233 - Anatomy and Physiology 1 4 credit hours”
### `5fe7513608c6bbb2` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-radiologic-technology-a-a-s · requirement_key=first-year-term-1 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped
  - courses: RAD 110 ⟵ “RAD 110 - Radiologic Image Production 2 credit hours”
  - courses: RAD 111 ⟵ “RAD 111 - Radiographic Procedures 1: Positioning and Patient Care 4 credit hours”
  - courses: RAD 112 ⟵ “RAD 112 - Clinical Radiography 1 5 credit hours”
### `60c7e9554029bbdf` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-addiction-counseling-a-a-s · requirement_key=social-and-behavioral-sciences-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18401&returnto=18122 (sha256 b9221a538e84)
- issues: requirement_groups_skipped
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
### `659e5b6f794924ca` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-radiologic-technology-a-a-s · requirement_key=arts-and-humanities-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped
  - courses: COM 111 ⟵ “COM 111 - Fundamentals of Oral Communication 3 credit hours”
### `665ff31baf4ea030` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-business-administration-transfer-a-s · requirement_key=arts-and-humanities-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18423&returnto=18122 (sha256 7472b56e5398)
- issues: requirement_groups_skipped
  - courses: COM 111 ⟵ “COM 111 - Fundamentals of Oral Communication 3 credit hours”
### `6698648a6d825767` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-education-early-childhood-special-education-a-a-t · requirement_key=social-and-behavioral-sciences-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18461&returnto=18122 (sha256 94a982ece7eb)
- issues: requirement_groups_skipped
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
  - courses: GEO 102 ⟵ “GEO 102 - World Regional Geography 3 credit hours”
### `685f9fb4ca70b48b` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mathematics-a-s · requirement_key=electives-9-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18506&returnto=18122 (sha256 d9f8559fe951)
- issues: requirement_groups_skipped
  - courses: BPA 201 ⟵ “BPA 201 - Financial Accounting 3 credit hours”
  - courses: BPA 202 ⟵ “BPA 202 - Managerial Accounting 3 credit hours”
  - courses: CHE 111 ⟵ “CHE 111 - General Chemistry 1 4 credit hours”
  - courses: CHE 112 ⟵ “CHE 112 - General Chemistry 2 4 credit hours”
  - courses: CHE 213 ⟵ “CHE 213 - Organic Chemistry 1 4 credit hours”
  - courses: CHE 214 ⟵ “CHE 214 - Organic Chemistry 2 4 credit hours”
  - courses: CTP 150 ⟵ “CTP 150 - Computer Science 1 4 credit hours”
  - courses: CTP 250 ⟵ “CTP 250 - Computer Science 2 4 credit hours”
  - courses: ECO 211 ⟵ “ECO 211 - Principles of Economics 1 3 credit hours”
  - courses: ECO 212 ⟵ “ECO 212 - Principles of Economics 2 3 credit hours”
  - courses: EGR 209 ⟵ “EGR 209 - Statics 3 credit hours”
  - courses: EGR 222 ⟵ “EGR 222 - Dynamics 3 credit hours”
  - courses: MAT 135 ⟵ “MAT 135 - Statistics 3 credit hours”
  - courses: MAT 223 ⟵ “MAT 223 - Fundamental Concepts of Mathematics 3 4 credit hours”
  - courses: MAT 235 ⟵ “MAT 235 - Introduction to Data Science 4 credit hours”
  - courses: MAT 250 ⟵ “MAT 250 - Introduction to Discrete Structures 3 credit hours”
  - courses: PHY 211 ⟵ “PHY 211 - General Physics 1 4 credit hours”
  - courses: PHY 212 ⟵ “PHY 212 - General Physics 2 4 credit hours”
  - courses: PHY 213 ⟵ “PHY 213 - General Physics 3 4 credit hours”
### `6893ff31b46a59c3` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-education-early-childhood-special-education-a-a-t · requirement_key=arts-and-humanities-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18461&returnto=18122 (sha256 94a982ece7eb)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HUM 101 ⟵ “HUM 101 - Introduction to Fine Arts 3 credit hours”
  - courses: HIS 211 ⟵ “HIS 211 - United States History through the Civil War 3 credit hours”
  - courses: HIS 212 ⟵ “HIS 212 - United States History Since the Civil War 3 credit hours”
### `68c19a276a01d676` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-kinesiology-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18486&returnto=18122 (sha256 1d9812f21d5b)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `7008d04a1438d12f` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=digital-forensics-area-of-concentration-requirements-23-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
  - courses: CJS 111 ⟵ “CJS 111 - Introduction to Criminal Justice 3 credit hours”
  - courses: CTS 170 ⟵ “CTS 170 - Digital Forensics 1 3 credit hours”
  - courses: CTS 207 ⟵ “CTS 207 - Digital Forensics 2 4 credit hours”
  - courses: CTS 209 ⟵ “CTS 209 - Digital Forensics 3 4 credit hours”
  - courses: CTS 242 ⟵ “CTS 242 - Network Intrusion Detection and Penetration Testing 4 credit hours”
  - courses: CTS 216 ⟵ “CTS 216 - Network Forensics  4 credit hours”
  - courses: CTS 236 ⟵ “CTS 236 - Virtualization & Cloud  4 credit hours”
  - courses: CTS 240 ⟵ “CTS 240 - Advanced Network Defense  4 credit hours”
  - courses: STM 213 ⟵ “STM 213 - Professional Skills for STEM  1 credit hour”
### `70afebc0d3fc6942` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-physical-therapist-assistant-a-a-s · requirement_key=first-year-spring-term [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18518&returnto=18122 (sha256 393dbc3378ab)
- issues: requirement_groups_skipped
  - courses: BIO 232 ⟵ “BIO 232 - Human Biology 2 4 credit hours OR”
  - courses: BIO 234 ⟵ “BIO 234 - Anatomy and Physiology 2 4 credit hours”
  - courses: PTA 102 ⟵ “PTA 102 - Physical Therapist Assistant 1 6 credit hours”
  - courses: PTA 106 ⟵ “PTA 106 - Kinesiology 6 credit hours”
### `70b04ae77990b176` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-physical-therapist-assistant-a-a-s · requirement_key=first-year-summer-term [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18518&returnto=18122 (sha256 393dbc3378ab)
- issues: requirement_groups_skipped
  - courses: PSY 211 ⟵ “PSY 211 - Developmental Psychology 3 credit hours”
  - courses: PTA 104 ⟵ “PTA 104 - Physical Therapist Assistant 2 6 credit hours”
  - courses: PTA 105 ⟵ “PTA 105 - Clinical Practice 1 2 credit hours”
### `730264f37d1a5a53` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-human-services-a-a-s · requirement_key=first-year-term-1 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18496&returnto=18122 (sha256 914ad51cf333)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: HUS 100 ⟵ “HUS 100 - Introduction to Human Services 3 credit hours”
  - courses: HUS 101 ⟵ “HUS 101 - Human Service and Addiction Counseling Ethics in Practice 3 credit hours”
  - courses: HUS 141 ⟵ “HUS 141 - Group Dynamics 3 credit hours”
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
### `73c548a1d3327888` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-electronics-engineering-technology-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18466&returnto=18122 (sha256 f2980187d2c8)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `743f42f942f8cc7f` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-elementary-education-elementary-special-education-a-a-t · requirement_key=arts-and-humanities-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18462&returnto=18122 (sha256 58a92cce1255)
- issues: requirement_groups_skipped
  - courses: HUM 101 ⟵ “HUM 101 - Introduction to Fine Arts 3 credit hours”
  - courses: HIS 211 ⟵ “HIS 211 - United States History through the Civil War 3 credit hours OR”
  - courses: HIS 212 ⟵ “HIS 212 - United States History Since the Civil War 3 credit hours”
### `74df7c1ca0f91f42` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-homeland-security-management-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18488&returnto=18122 (sha256 a94480b17f64)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `753410586da482c2` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-education-early-childhood-special-education-a-a-t · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18461&returnto=18122 (sha256 94a982ece7eb)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `7af196851b28a930` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-engineering-transfer-a-s · requirement_key=program-requirements-25-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18467&returnto=18122 (sha256 d611a13fc853)
- issues: requirement_groups_skipped
  - courses: EGR 120 ⟵ “EGR 120 - Introduction to Engineering Design 3 credit hours”
  - courses: MAT 201 ⟵ “MAT 201 - Calculus and Analytic Geometry 3 4 credit hours”
  - courses: MAT 212 ⟵ “MAT 212 - Differential Equations 4 credit hours”
### `7c78677b25c638a7` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=term-1 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 231 ⟵ “BIO 231 - Human Biology 1 4 credit hours”
  - courses: BIO 233 ⟵ “BIO 233 - Anatomy and Physiology 1 4 credit hours”
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 101A ⟵ “ENG 101A - Academic Writing and Research 1 3 credit hours”
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
### `7db88e1b8ef04ed8` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=term-3 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped
  - courses: BIO 223 ⟵ “BIO 223 - General Microbiology 4 credit hours”
  - courses: NUR 130 ⟵ “NUR 130 - Nursing of Adult Clients in Health and Illness 1 5 credit hours”
  - courses: NUR 131 ⟵ “NUR 131 - Maternal, Newborn Nursing and Women’s Health 4 credit hours”
  - courses: PSY 211 ⟵ “PSY 211 - Developmental Psychology 3 credit hours”
### `7dcb61d52f58ff9b` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-and-jurisprudence-a-a · requirement_key=mathematics-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18500&returnto=18122 (sha256 cba5e6015d8f)
- issues: requirement_groups_skipped
  - courses: MAT 133 ⟵ “MAT 133 - Finite Mathematics 3 credit hours OR”
  - courses: MAT 135 ⟵ “MAT 135 - Statistics 3 credit hours”
### `7e24a939d6cc97f6` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=arts-and-humanities-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
  - courses: CTP 194 ⟵ “CTP 194 - Ethics and the Information Age 3 credit hours”
### `80ed2dc265db4cb4` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-education-early-childhood-special-education-a-a-t · requirement_key=program-requirements-29-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18461&returnto=18122 (sha256 94a982ece7eb)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: EDU 132 ⟵ “EDU 132 - Introduction to Early Childhood Development 3 credit hours”
  - courses: EDU 133 ⟵ “EDU 133 - Growth and Development 3 credit hours”
  - courses: EDU 135 ⟵ “EDU 135 - Children’s Health, Nutrition and Safety 3 credit hours”
  - courses: EDU 214 ⟵ “EDU 214 - Introduction to Special Education 3 credit hours”
  - courses: EDU 242 ⟵ “EDU 242 - Foundations of Reading and Language Arts 3 credit hours”
  - courses: EDU 242H ⟵ “EDU 242H - Foundations of Reading and Language Arts - Honors 3 credit hours”
  - courses: EDU 247 ⟵ “EDU 247 - Early Childhood: Methods and Materials 3 credit hours”
  - courses: MAT 223 ⟵ “MAT 223 - Fundamental Concepts of Mathematics 3 4 credit hours”
  - courses: PHS 200 ⟵ “PHS 200 - Earth and Space Science 4 credit hours”
  - courses: PLS 111 ⟵ “PLS 111 - American Government 3 credit hours”
### `812eff3d321a2036` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-entrepreneurship-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18473&returnto=18122 (sha256 a897f034277e)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `8155e0b713af7544` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-human-services-a-a-s · requirement_key=second-year-term-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18496&returnto=18122 (sha256 914ad51cf333)
- issues: requirement_groups_skipped
  - courses: HUS 211 ⟵ “HUS 211 - Crisis Intervention and Counseling 3 credit hours”
  - courses: HUS 216 ⟵ “HUS 216 - Theories of Counseling 3 credit hours”
  - courses: HUS 217 ⟵ “HUS 217 - Fieldwork: Theories of Counseling 3 credit hours”
  - courses: PSY 214 ⟵ “PSY 214 - Introduction to Psychopathology 3 credit hours”
### `821e7357bd7b4016` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=term-1-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped
  - courses: NUR 180 ⟵ “NUR 180 - LPN, Paramedic or Veteran to RN Transition 2 credit hours”
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
### `826eba0e4e59f0d3` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-transfer-studies-a-a · requirement_key=english-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18539&returnto=18122 (sha256 8d2e1432cb25)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `82a20dd4dd0913cd` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-homeland-security-management-a-a-s · requirement_key=program-requirements-24-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18488&returnto=18122 (sha256 a94480b17f64)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CJS 260 ⟵ “CJS 260 - Terrorism/Counterterrorism 3 credit hours”
  - courses: HLS 111 ⟵ “HLS 111 - Introduction to Homeland Security 3 credit hours”
  - courses: HLS 112 ⟵ “HLS 112 - National Security Law 3 credit hours”
  - courses: HLS 114 ⟵ “HLS 114 - Maryland and Terrorism 3 credit hours”
  - courses: HLS 211 ⟵ “HLS 211 - Intelligence Analysis and Security Management 3 credit hours”
  - courses: HLS 220 ⟵ “HLS 220 - Intelligence and U.S. National Security 3 credit hours”
  - courses: HLS 212 ⟵ “HLS 212 - Survey of Weapons of Mass Destruction 3 credit hours”
  - courses: HLS 213 ⟵ “HLS 213 - Transportation and Border Security 3 credit hours”
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
### `830bd4c7968a9849` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-human-services-a-a-s · requirement_key=first-year-term-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18496&returnto=18122 (sha256 914ad51cf333)
- issues: requirement_groups_skipped
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
  - courses: COM 111 ⟵ “COM 111 - Fundamentals of Oral Communication 3 credit hours”
  - courses: HUS 114 ⟵ “HUS 114 - Counseling, Assessment and Case Management 3 credit hours”
  - courses: HUS 115 ⟵ “HUS 115 - Fieldwork: Counseling, Assessment and Case Management 3 credit hours”
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
### `838e76e4f93d7fc3` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-electronics-engineering-technology-a-a-s · requirement_key=arts-and-humanities-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18466&returnto=18122 (sha256 f2980187d2c8)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: COM 110 ⟵ “COM 110 - Introduction to Interpersonal Communication 3 credit hours”
  - courses: COM 111 ⟵ “COM 111 - Fundamentals of Oral Communication 3 credit hours”
  - courses: COM 141 ⟵ “COM 141 - Group Communication and Leadership 3 credit hours”
### `8af6387f15170be4` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-surgical-technology-a-a-s · requirement_key=second-year-term-3 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18523&returnto=18122 (sha256 83c37b6ff24b)
- issues: requirement_groups_skipped
  - courses: SGT 202 ⟵ “SGT 202 - Surgical Procedures 2 4 credit hours”
  - courses: SGT 205 ⟵ “SGT 205 - Surgical Technology Clinical 2 5 credit hours”
  - courses: SGT 206 ⟵ “SGT 206 - Surgical Technology Clinical 3 5 credit hours”
  - courses: SGT 208 ⟵ “SGT 208 - Perspectives of Surgical Technology 2 credits”
### `8b4a0bb340909b0c` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-development-a-a-s · requirement_key=social-and-behavioral-sciences-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18460&returnto=18122 (sha256 dc57c78c8099)
- issues: requirement_groups_skipped
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
### `8dd887c1bd14dcc6` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-business-administration-transfer-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18423&returnto=18122 (sha256 7472b56e5398)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `8dd8d0044f8d17a0` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-surgical-technology-a-a-s · requirement_key=english-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18523&returnto=18122 (sha256 83c37b6ff24b)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours OR”
  - courses: ENG 101A ⟵ “ENG 101A - Academic Writing and Research 1 3 credit hours”
### `8e1769939d9b19d2` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-engineering-transfer-a-s · requirement_key=biological-and-physical-sciences-12-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18467&returnto=18122 (sha256 d611a13fc853)
- issues: requirement_groups_skipped
  - courses: CHE 111 ⟵ “CHE 111 - General Chemistry 1 4 credit hours”
  - courses: PHY 211 ⟵ “PHY 211 - General Physics 1 4 credit hours”
  - courses: PHY 212 ⟵ “PHY 212 - General Physics 2 4 credit hours”
### `8ed6e975e5e33de9` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-development-a-a-s · requirement_key=arts-and-humanities-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18460&returnto=18122 (sha256 dc57c78c8099)
- issues: requirement_groups_skipped
  - courses: COM 111 ⟵ “COM 111 - Fundamentals of Oral Communication 3 credit hours OR”
### `8fe568aa798e3ea9` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-elementary-education-elementary-special-education-a-a-t · requirement_key=program-requirements-29-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18462&returnto=18122 (sha256 58a92cce1255)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: EDU 111 ⟵ “EDU 111 - Foundations of Education 3 credit hours”
  - courses: EDU 133 ⟵ “EDU 133 - Growth and Development 3 credit hours”
  - courses: EDU 135 ⟵ “EDU 135 - Children’s Health, Nutrition and Safety 3 credit hours”
  - courses: EDU 211 ⟵ “EDU 211 - Educational Psychology 3 credit hours”
  - courses: EDU 214 ⟵ “EDU 214 - Introduction to Special Education 3 credit hours”
  - courses: EDU 242 ⟵ “EDU 242 - Foundations of Reading and Language Arts 3 credit hours”
  - courses: EDU 242H ⟵ “EDU 242H - Foundations of Reading and Language Arts - Honors 3 credit hours”
  - courses: MAT 223 ⟵ “MAT 223 - Fundamental Concepts of Mathematics 3 4 credit hours”
  - courses: PHS 200 ⟵ “PHS 200 - Earth and Space Science 4 credit hours”
  - courses: PLS 111 ⟵ “PLS 111 - American Government 3 credit hours”
### `9079e3a50d69ee54` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-homeland-security-management-a-a-s · requirement_key=arts-and-humanities-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18488&returnto=18122 (sha256 a94480b17f64)
- issues: requirement_groups_skipped
  - courses: AMS 100 ⟵ “AMS 100 - Introduction to American Studies 3 credit hours”
### `92e8a34c7f1228f8` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-addiction-counseling-a-a-s · requirement_key=program-requirements-35-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18401&returnto=18122 (sha256 b9221a538e84)
- issues: requirement_groups_skipped
  - courses: PSY 214 ⟵ “PSY 214 - Introduction to Psychopathology 3 credit hours”
  - courses: HUS 101 ⟵ “HUS 101 - Human Service and Addiction Counseling Ethics in Practice 3 credit hours”
  - courses: HUS 102 ⟵ “HUS 102 - Physiological Aspects of Chemical Dependence 3 credit hours”
  - courses: HUS 114 ⟵ “HUS 114 - Counseling, Assessment and Case Management 3 credit hours”
  - courses: HUS 115 ⟵ “HUS 115 - Fieldwork: Counseling, Assessment and Case Management 3 credit hours”
  - courses: HUS 130 ⟵ “HUS 130 - Introduction to Family Counseling 3 credit hours”
  - courses: HUS 140 ⟵ “HUS 140 - Topics in Alcohol and Drug Counseling: Co-occurring Disorders 3 credit hours”
  - courses: HUS 141 ⟵ “HUS 141 - Group Dynamics 3 credit hours”
  - courses: HUS 200 ⟵ “HUS 200 - Addiction Treatment Delivery 3 credit hours”
  - courses: HUS 216 ⟵ “HUS 216 - Theories of Counseling 3 credit hours”
  - courses: HUS 217 ⟵ “HUS 217 - Fieldwork: Theories of Counseling 3 credit hours”
  - courses: HUS 234 ⟵ “HUS 234 - Trauma Informed Care 2 credit hours”
### `93173b1a1920ac0d` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-web-and-mobile-application-development-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18454&returnto=18122 (sha256 003ac53181a3)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `953009c8b8540c47` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-enforcement-and-criminal-justice-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18501&returnto=18122 (sha256 6891dce62abe)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `95961d72751aa43f` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-paralegal-studies-a-a-s · requirement_key=arts-and-humanities-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18513&returnto=18122 (sha256 c3d16406fe1b)
- issues: requirement_groups_skipped
  - courses: LGS 271 ⟵ “LGS 271 - Civil Rights Law 3 credit hours”
### `95d57fc530e065bd` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-radiologic-technology-a-a-s · requirement_key=first-year-term-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped
  - courses: RAD 121 ⟵ “RAD 121 - Radiographic Procedures 2 5 credit hours”
  - courses: RAD 122 ⟵ “RAD 122 - Clinical Radiography 2 5 credit hours”
  - courses: RAD 123 ⟵ “RAD 123 - Imaging Equipment Maintenance and Operation 3 credit hours”
### `99349a08888a9888` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=additional-general-education-requirement-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
  - courses: CTS 107 ⟵ “CTS 107 - Cyber Essentials 3 credit hours”
### `99ee538620e94b74` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-kinesiology-a-s · requirement_key=program-requirements-25-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18486&returnto=18122 (sha256 1d9812f21d5b)
- issues: requirement_groups_skipped
  - courses: BIO 234 ⟵ “BIO 234 - Anatomy and Physiology 2 4 credit hours”
  - courses: HEA 101 ⟵ “HEA 101 - Foundations of Health, Exercise and Sport 3 credit hours”
  - courses: HEA 111 ⟵ “HEA 111 - Personal and Community Health 3 credit hours”
  - courses: HEA 295 ⟵ “HEA 295 - Care and Prevention of Athletic Injuries 3 credit hours”
  - courses: HEA 230 ⟵ “HEA 230 - Personal Trainer Fundamentals 4 credit hours”
### `9a7586ffa209d880` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-transfer-studies-a-a · requirement_key=aca-100-1-credit [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18539&returnto=18122 (sha256 8d2e1432cb25)
- issues: requirement_groups_skipped
  - courses: ACA 100 ⟵ “ACA 100 - Student Success Seminar  OR evidence of completion of 24 college credits.”
### `9b3ef1b460f65cbe` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-nursing-a-s · requirement_key=term-5 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18512&returnto=18122 (sha256 528412051dad)
- issues: requirement_groups_skipped
  - courses: NUR 230 ⟵ “NUR 230 - Nursing Management of Clients with Complex Health Problems and Transition into Nursing 9 credit hours”
  - courses: NUR 231 ⟵ “NUR 231 - Nursing Perspectives 2 1 credit hour”
### `9c32299878bbc7d4` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-enforcement-and-criminal-justice-a-a-s · requirement_key=additional-general-education-requirements-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18501&returnto=18122 (sha256 6891dce62abe)
- issues: requirement_groups_skipped
  - courses: HEA 150 ⟵ “HEA 150 - Advanced First Aid, CPR and AED”
  - courses: EMT 104 ⟵ “EMT 104 - Emergency Medical Care, CPR & AED”
### `9f100f180514e6c2` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-kinesiology-a-s · requirement_key=social-and-behavioral-sciences-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18486&returnto=18122 (sha256 1d9812f21d5b)
- issues: requirement_groups_skipped
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
### `9f500fc9a045275e` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-education-early-childhood-special-education-a-a-t · requirement_key=biological-and-physical-sciences-8-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18461&returnto=18122 (sha256 94a982ece7eb)
- issues: requirement_groups_skipped
  - courses: PHS 100 ⟵ “PHS 100 - General Physical Science 4 credit hours”
  - courses: BIO 100 ⟵ “BIO 100 - Introduction to Biology 4 credit hours”
### `9ff5837103d5aef8` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s · requirement_key=second-year-term-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
  - courses: MLT 206 ⟵ “MLT 206 - Advanced Clinical Chemistry 2 credit hours”
  - courses: MLT 208 ⟵ “MLT 208 - Clinical Review 2 credit hours”
  - courses: MLT 276 ⟵ “MLT 276 - Clinical Hematology Practicum 2 credit hours”
  - courses: MLT 277 ⟵ “MLT 277 - Clinical Chemistry Practicum 2 credit hours”
  - courses: MLT 278 ⟵ “MLT 278 - Clinical Microbiology Practicum 2 credit hours”
  - courses: MLT 279 ⟵ “MLT 279 - Clinical Immunohematology Practicum 2 credit hours”
### `a46d42111fe8d1f8` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-business-administration-transfer-a-s · requirement_key=program-requirements-26-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18423&returnto=18122 (sha256 7472b56e5398)
- issues: requirement_groups_skipped
  - courses: BPA 111 ⟵ “BPA 111 - Introduction to Business 3 credit hours”
  - courses: BPA 201 ⟵ “BPA 201 - Financial Accounting 3 credit hours”
  - courses: BPA 202 ⟵ “BPA 202 - Managerial Accounting 3 credit hours”
  - courses: ECO 212 ⟵ “ECO 212 - Principles of Economics 2 3 credit hours”
  - courses: ECO 232 ⟵ “ECO 232 - Business Statistics 3 credit hours”
  - courses: LGS 253 ⟵ “LGS 253 - Business Law 1 3 credit hours”
### `a5f37205cb6197ae` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-web-and-mobile-application-development-a-a-s · requirement_key=program-electives-11-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18454&returnto=18122 (sha256 003ac53181a3)
- issues: requirement_groups_skipped
  - courses: ART 268 ⟵ “ART 268 - User Experience Design for the Web 3 credit hours”
  - courses: ART 269 ⟵ “ART 269 - Responsive Web Design 3 credit hours”
  - courses: CTP 220 ⟵ “CTP 220 - Content Management Systems 3 credit hours”
  - courses: CTP 230 ⟵ “CTP 230 - Android Programming 4 credit hours”
  - courses: CTP 232 ⟵ “CTP 232 - iPad/iPhone iOS Programming 1 4 credit hours”
### `a6f3ab6a9e305660` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-radiologic-technology-a-a-s · requirement_key=second-year-term-1 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped
  - courses: RAD 231 ⟵ “RAD 231 - Radiographic Procedures 4 3 credit hours”
  - courses: RAD 232 ⟵ “RAD 232 - Clinical Radiography 4 6 credit hours”
### `a84a68d8c30e040f` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mathematics-a-s · requirement_key=mathematics-4-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18506&returnto=18122 (sha256 d9f8559fe951)
- issues: requirement_groups_skipped
  - courses: MAT 191 ⟵ “MAT 191 - Calculus and Analytic Geometry 1 4 credit hours”
### `a97b578eac31222a` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mechatronics-engineering-technology-a-a-s · requirement_key=program-requirements-37-38-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18472&returnto=18122 (sha256 7beddb2ca1f0)
- issues: requirement_groups_skipped
  - courses: EET 130 ⟵ “EET 130 - Introduction to Electronic Circuits 4 credit hours”
  - courses: ENT 260 ⟵ “ENT 260 - Solid Modeling with SolidWorks 3 credit hours”
  - courses: MEC 110 ⟵ “MEC 110 - Mechanical Systems 4 credit hours”
  - courses: MEC 120 ⟵ “MEC 120 - Pneumatics and Hydraulics 4 credit hours”
  - courses: MEC 130 ⟵ “MEC 130 - Programmable Logic Controllers 4 credit hours”
  - courses: MEC 140 ⟵ “MEC 140 - Introduction to Robotics 4 credit hours”
  - courses: MEC 230 ⟵ “MEC 230 - Electric Motor Fundamentals 3 credit hours”
  - courses: MEC 266 ⟵ “MEC 266 - Mechatronic Systems Capstone 4 credit hours”
  - courses: STM 213 ⟵ “STM 213 - Professional Skills for STEM 1 credit hour”
  - courses: CTS 110 ⟵ “CTS 110 - Network Essentials 4 credit hours”
  - courses: EET 109 ⟵ “EET 109 - Circuit Assembly Techniques 2 credit hours”
  - courses: EET 150 ⟵ “EET 150 - Semiconductors and Linear Circuits 4 credit hours”
  - courses: EET 231 ⟵ “EET 231 - Digital-Electronic Circuits 4 credit hours”
  - courses: EET 250 ⟵ “EET 250 - Microprocessors and Microcontrollers 4 credit hours”
  - courses: EET 255 ⟵ “EET 255 - Metrology and Calibration 4 credit hours”
  - courses: EET 260 ⟵ “EET 260 - Electronic Communication Systems 4 credit hours”
  - courses: ENT 241 ⟵ “ENT 241 - Computer-Aided Drafting 3 credit hours”
  - courses: ENT 242 ⟵ “ENT 242 - Advanced Computer-Aided Drafting and Design 3 credit hours”
  - courses: ENT 261 ⟵ “ENT 261 - Rapid Prototyping Techniques 4 credit hours”
  - courses: MAT 146 ⟵ “MAT 146 - Precalculus 2 3 credit hours”
  - courses: MAT 191 ⟵ “MAT 191 - Calculus and Analytic Geometry 1 4 credit hours”
  - courses: PHY 112 ⟵ “PHY 112 - Fundamentals of Physics 2 4 credit hours”
  - courses: PHY 212 ⟵ “PHY 212 - General Physics 2 4 credit hours”
### `afd7f31bd9b72d87` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-homeland-security-management-a-a-s · requirement_key=social-and-behavioral-sciences-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18488&returnto=18122 (sha256 a94480b17f64)
- issues: requirement_groups_skipped
  - courses: GEO 102 ⟵ “GEO 102 - World Regional Geography 3 credit hours”
### `b0cf9ef3cb27c674` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-elementary-education-elementary-special-education-a-a-t · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18462&returnto=18122 (sha256 58a92cce1255)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `b2b770b76f891096` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-homeland-security-management-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18488&returnto=18122 (sha256 a94480b17f64)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `b613262263943e87` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-elementary-education-elementary-special-education-a-a-t · requirement_key=mathematics-8-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18462&returnto=18122 (sha256 58a92cce1255)
- issues: requirement_groups_skipped
  - courses: MAT 221 ⟵ “MAT 221 - Fundamental Concepts of Mathematics 1 4 credit hours”
  - courses: MAT 222 ⟵ “MAT 222 - Fundamental Concepts of Mathematics 2 4 credit hours”
### `b63b44d97bdec240` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=architecture-area-of-concentration-requirements-21-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ACH 122 ⟵ “ACH 122 - Construction Technology 2 3 credit hours”
  - courses: ACH 211 ⟵ “ACH 211 - Architectural Studio 1: Form, Space and Order 4 credit hours”
  - courses: ACH 212 ⟵ “ACH 212 - Architectural Studio 2: Design and Synthesis 4 credit hours”
  - courses: ACH 231 ⟵ “ACH 231 - Professional Practices in Architecture 3 credit hours”
  - courses: ACH 240 ⟵ “ACH 240 - Construction Documentation 4 credit hours”
  - courses: ACH 221 ⟵ “ACH 221 - History of World Architecture: Ancient to Medieval 3 credit hours”
  - courses: ACH 222 ⟵ “ACH 222 - History of World Architecture: Renaissance to Present 3 credit hours”
### `b88ad900773336ca` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=arts-and-humanities-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ACH 221 ⟵ “ACH 221 - History of World Architecture: Ancient to Medieval 3 credit hours”
  - courses: ACH 222 ⟵ “ACH 222 - History of World Architecture: Renaissance to Present 3 credit hours”
### `ba77ac5ff29cad6b` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-web-and-mobile-application-development-a-a-s · requirement_key=program-requirements-31-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18454&returnto=18122 (sha256 003ac53181a3)
- issues: requirement_groups_skipped
  - courses: ART 170 ⟵ “ART 170 - Web Design 1 3 credit hours”
  - courses: CTP 115 ⟵ “CTP 115 - Introductory Object-Oriented Program Analysis and Design 4 credit hours”
  - courses: CTP 118 ⟵ “CTP 118 - Web Development using HTML/CSS 4 credit hours”
  - courses: CTP 130 ⟵ “CTP 130 - Programming in PHP/MySQL 3 credit hours”
  - courses: CTP 135 ⟵ “CTP 135 - Programming in JavaScript and jQuery 4 credit hours”
  - courses: CTP 140 ⟵ “CTP 140 - Database Foundations, SQL/NoSQL 3 credit hours”
  - courses: CTP 150 ⟵ “CTP 150 - Computer Science 1 4 credit hours”
  - courses: CTP 236 ⟵ “CTP 236 - Advanced JavaScript 3 credit hours”
  - courses: CTP 237 ⟵ “CTP 237 - Server-Side Development 3 credit hours”
### `bb16bf888f1a00c5` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-massage-therapy-a-a-s · requirement_key=english-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18524&returnto=18122 (sha256 17b5ea90f9b1)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours OR”
  - courses: ENG 101A ⟵ “ENG 101A - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `c1bacec5b7b3a642` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s · requirement_key=summer [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
  - courses: COM 111 ⟵ “COM 111 - Fundamentals of Oral Communication 3 credit hours”
  - courses: CHE 111 ⟵ “CHE 111 - General Chemistry 1 4 credit hours”
### `c408ae58a41e5d11` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-transfer-studies-a-a · requirement_key=electives-16-18-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18539&returnto=18122 (sha256 8d2e1432cb25)
- issues: requirement_groups_skipped
  - section: electives-16-18-credits ⟵ “Electives: 16-18 credits”
### `c4403441db217b27` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-and-jurisprudence-a-a · requirement_key=arts-and-humanities-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18500&returnto=18122 (sha256 cba5e6015d8f)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: COM 111 ⟵ “COM 111 - Fundamentals of Oral Communication 3 credit hours OR”
  - courses: LGS 271 ⟵ “LGS 271 - Civil Rights Law 3 credit hours”
  - courses: PHL 141 ⟵ “PHL 141 - Introduction to Logic 3 credit hours”
### `c528927300a20d76` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=program-requirements-40-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
  - courses: CTS 110 ⟵ “CTS 110 - Network Essentials 4 credit hours”
  - courses: CTS 120 ⟵ “CTS 120 - Introduction to Linux 4 credit hours”
  - courses: CTS 140 ⟵ “CTS 140 - Network Security Fundamentals 4 credit hours”
  - courses: CTS 234 ⟵ “CTS 234 - Windows Server 4 credit hours”
  - courses: CYB 270 ⟵ “CYB 270 - Cyber Capstone 1 credit hour”
### `c7faa28b378298eb` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-and-jurisprudence-a-a · requirement_key=social-and-behavioral-sciences-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18500&returnto=18122 (sha256 cba5e6015d8f)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
  - courses: LGS 217 ⟵ “LGS 217 - Constitutional Law 3 credit hours AND”
  - courses: HIS 211 ⟵ “HIS 211 - United States History through the Civil War 3 credit hours”
### `c86359b96de5ccf4` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-electronics-engineering-technology-a-a-s · requirement_key=biological-and-physical-sciences-4-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18466&returnto=18122 (sha256 f2980187d2c8)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PHY 111 ⟵ “PHY 111 - Fundamentals of Physics 1 4 credit hours”
  - courses: PHY 211 ⟵ “PHY 211 - General Physics 1 4 credit hours”
### `c92b91f6391f49c6` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s · requirement_key=second-year-term-1 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
  - courses: MLT 202 ⟵ “MLT 202 - Clinical Microbiology 4 credit hours”
  - courses: MLT 203 ⟵ “MLT 203 - Clinical Chemistry 4 credit hours”
  - courses: MLT 204 ⟵ “MLT 204 - Clinical Immunology/Immunohematology 4 credit hours”
  - courses: MLT 205 ⟵ “MLT 205 - Clinical Hematology 4 credit hours”
### `c98cc45f00514f88` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `c98fcf06e45ed759` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mathematics-a-s · requirement_key=core-courses-16-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18506&returnto=18122 (sha256 d9f8559fe951)
- issues: requirement_groups_skipped
  - courses: MAT 192 ⟵ “MAT 192 - Calculus and Analytic Geometry 2 4 credit hours”
  - courses: MAT 201 ⟵ “MAT 201 - Calculus and Analytic Geometry 3 4 credit hours”
  - courses: MAT 202 ⟵ “MAT 202 - Linear Algebra 4 credit hours”
  - courses: MAT 212 ⟵ “MAT 212 - Differential Equations 4 credit hours”
### `ca219812bcd74018` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-elementary-education-elementary-special-education-a-a-t · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18462&returnto=18122 (sha256 58a92cce1255)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `ca5d178e1c9d85ef` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-elementary-education-elementary-special-education-a-a-t · requirement_key=social-and-behavioral-sciences-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18462&returnto=18122 (sha256 58a92cce1255)
- issues: requirement_groups_skipped
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
  - courses: GEO 102 ⟵ “GEO 102 - World Regional Geography 3 credit hours”
### `cae1ef41573fde8a` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s · requirement_key=first-year-term-1 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
  - courses: BIO 231 ⟵ “BIO 231 - Human Biology 1 4 credit hours OR”
  - courses: BIO 233 ⟵ “BIO 233 - Anatomy and Physiology 1 4 credit hours”
  - courses: MLT 125 ⟵ “MLT 125 - Phlebotomy 4 credit hours”
  - courses: MLT 100 ⟵ “MLT 100 - Introduction to the Medical Laboratory 4 credit hours”
### `cd8b9b1cc8518093` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-transfer-studies-a-a · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18539&returnto=18122 (sha256 8d2e1432cb25)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `cdd0f049d0771f12` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-surgical-technology-a-a-s · requirement_key=prerequisites [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18523&returnto=18122 (sha256 83c37b6ff24b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BIO 231 ⟵ “BIO 231 - Human Biology 1 4 credit hours AND”
  - courses: BIO 232 ⟵ “BIO 232 - Human Biology 2 4 credit hours”
  - courses: BIO 233 ⟵ “BIO 233 - Anatomy and Physiology 1 4 credit hours AND”
  - courses: BIO 234 ⟵ “BIO 234 - Anatomy and Physiology 2 4 credit hours”
  - courses: BIO 223 ⟵ “BIO 223 - General Microbiology 4 credit hours”
  - courses: MDA 113 ⟵ “MDA 113 - Medical Terminology 3 credit hours”
### `ce704bf3941adf2f` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-business-administration-transfer-a-s · requirement_key=mathematics-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18423&returnto=18122 (sha256 7472b56e5398)
- issues: requirement_groups_skipped
  - courses: MAT 230 ⟵ “MAT 230 - Elementary Calculus (For Business and Social Sciences) 3 credit hours”
### `cedc3f1bdcfaa610` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-elementary-education-elementary-special-education-a-a-t · requirement_key=biological-and-physical-sciences-8-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18462&returnto=18122 (sha256 58a92cce1255)
- issues: requirement_groups_skipped
  - courses: PHS 100 ⟵ “PHS 100 - General Physical Science 4 credit hours”
  - courses: BIO 100 ⟵ “BIO 100 - Introduction to Biology 4 credit hours”
### `d0369fd3bd968f2a` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-and-jurisprudence-a-a · requirement_key=program-requirements-29-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18500&returnto=18122 (sha256 cba5e6015d8f)
- issues: requirement_groups_skipped
  - courses: HIS 212 ⟵ “HIS 212 - United States History Since the Civil War 3 credit hours”
  - courses: LGS 111 ⟵ “LGS 111 - Introduction to Paralegal Studies 3 credit hours”
  - courses: LGS 112 ⟵ “LGS 112 - Law Office Practice and Technology 3 credit hours”
  - courses: LGS 141 ⟵ “LGS 141 - Electronic Legal Research 1 credit hour”
  - courses: LGS 143 ⟵ “LGS 143 - Legal Research and Writing 1 3 credit hours”
  - courses: LGS 144 ⟵ “LGS 144 - Legal Research and Writing 2 3 credit hours”
  - courses: LGS 210 ⟵ “LGS 210 - Legal Ethics 3 credit hours”
  - courses: LGS 217 ⟵ “LGS 217 - Constitutional Law 3 credit hours”
  - courses: PHL 142 ⟵ “PHL 142 - Ethics 3 credit hours”
  - courses: ECO 121 ⟵ “ECO 121 - Introduction to Economics 3 credit hours”
  - courses: LGS 215 ⟵ “LGS 215 - Criminal Law 3 credit hours”
  - courses: LGS 253 ⟵ “LGS 253 - Business Law 1 3 credit hours”
  - courses: LGS 271 ⟵ “LGS 271 - Civil Rights Law 3 credit hours”
  - courses: PLS 111 ⟵ “PLS 111 - American Government 3 credit hours”
  - courses: PLS 113 ⟵ “PLS 113 - State and Local Government 3 credit hours”
### `d0d7889042e80ccf` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-entrepreneurship-a-a-s · requirement_key=program-requirements-36-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18473&returnto=18122 (sha256 a897f034277e)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: BPA 111 ⟵ “BPA 111 - Introduction to Business 3 credit hours”
  - courses: BPA 120 ⟵ “BPA 120 - Small Business Management 3 credit hours”
  - courses: BPA 127 ⟵ “BPA 127 - Digital Marketing and Analytics 3 credit hours”
  - courses: BPA 104 ⟵ “BPA 104 - Sales & Marketing for Small Business 3 credit hours”
  - courses: BPA 162 ⟵ “BPA 162 - Business Communications 3 credit hours”
  - courses: BPA 200 ⟵ “BPA 200 - Foundations of Accounting 3 credit hours”
  - courses: BPA 201 ⟵ “BPA 201 - Financial Accounting 3 credit hours”
  - courses: BPA 217 ⟵ “BPA 217 - Small Business Accounting 3 credit hours”
  - courses: BPA 275 ⟵ “BPA 275 - Internship in Business 3 credit hours”
  - courses: BPA 103 ⟵ “BPA 103 - Introduction to Entrepreneurship 3 credit hours”
  - courses: BPA 270 ⟵ “BPA 270 - Entrepreneurship: New Venture Planning 3 credit hours”
  - courses: LGS 250 ⟵ “LGS 250 - Legal Issues for Business 3 credit hours”
  - courses: LGS 253 ⟵ “LGS 253 - Business Law 1 3 credit hours”
### `d2f3df77be396d1e` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=mathematics-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MAT 135 ⟵ “MAT 135 - Statistics 3 credit hours”
### `d39fbd1c437cb1f5` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-business-administration-transfer-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18423&returnto=18122 (sha256 7472b56e5398)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `db24cd769012d673` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mathematics-a-s · requirement_key=additional-general-education-requirements-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18506&returnto=18122 (sha256 d9f8559fe951)
- issues: requirement_groups_skipped
  - courses: CTA 103 ⟵ “CTA 103 - Computer Technology and Artificial Intelligence  3 credit hours OR”
  - courses: EGR 120 ⟵ “EGR 120 - Introduction to Engineering Design  3 credit hours”
### `df19ed415a5a4a45` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-electronics-engineering-technology-a-a-s · requirement_key=program-requirements-37-38-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18466&returnto=18122 (sha256 f2980187d2c8)
- issues: requirement_groups_skipped
  - courses: EET 109 ⟵ “EET 109 - Circuit Assembly Techniques 2 credit hours”
  - courses: EET 130 ⟵ “EET 130 - Introduction to Electronic Circuits 4 credit hours”
  - courses: EET 150 ⟵ “EET 150 - Semiconductors and Linear Circuits 4 credit hours”
  - courses: EET 231 ⟵ “EET 231 - Digital-Electronic Circuits 4 credit hours”
  - courses: EET 255 ⟵ “EET 255 - Metrology and Calibration 4 credit hours”
  - courses: EET 260 ⟵ “EET 260 - Electronic Communication Systems 4 credit hours”
  - courses: EET 265 ⟵ “EET 265 - Electronics Technician Capstone 4 credit hours”
  - courses: MEC 130 ⟵ “MEC 130 - Programmable Logic Controllers 4 credit hours”
  - courses: STM 213 ⟵ “STM 213 - Professional Skills for STEM 1 credit hour”
  - courses: CTA 105 ⟵ “CTA 105 - Theory and Troubleshooting Microcomputers 1 3 credit hours”
  - courses: CTA 205 ⟵ “CTA 205 - Theory and Troubleshooting Microcomputers 2 3 credit hours”
  - courses: CTS 110 ⟵ “CTS 110 - Network Essentials 4 credit hours”
  - courses: EET 250 ⟵ “EET 250 - Microprocessors and Microcontrollers 4 credit hours”
  - courses: ENT 241 ⟵ “ENT 241 - Computer-Aided Drafting 3 credit hours”
  - courses: ENT 260 ⟵ “ENT 260 - Solid Modeling with SolidWorks 3 credit hours”
  - courses: MAT 146 ⟵ “MAT 146 - Precalculus 2 3 credit hours”
  - courses: MAT 191 ⟵ “MAT 191 - Calculus and Analytic Geometry 1 4 credit hours”
  - courses: MEC 110 ⟵ “MEC 110 - Mechanical Systems 4 credit hours”
  - courses: MEC 120 ⟵ “MEC 120 - Pneumatics and Hydraulics 4 credit hours”
  - courses: MEC 140 ⟵ “MEC 140 - Introduction to Robotics 4 credit hours”
  - courses: MEC 230 ⟵ “MEC 230 - Electric Motor Fundamentals 3 credit hours”
  - courses: PHY 112 ⟵ “PHY 112 - Fundamentals of Physics 2 4 credit hours”
  - courses: PHY 212 ⟵ “PHY 212 - General Physics 2 4 credit hours”
### `dfef95460cf4b568` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-paralegal-studies-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18513&returnto=18122 (sha256 c3d16406fe1b)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `e3f317ca2b5ba2b3` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mathematics-a-s · requirement_key=english-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18506&returnto=18122 (sha256 d9f8559fe951)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `e4438627aa5a08e9` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-enforcement-and-criminal-justice-a-a-s · requirement_key=social-and-behavioral-sciences-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18501&returnto=18122 (sha256 6891dce62abe)
- issues: requirement_groups_skipped
  - courses: PLS 111 ⟵ “PLS 111 - American Government 3 credit hours”
### `e77b55e7b3463a31` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-paralegal-studies-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18513&returnto=18122 (sha256 c3d16406fe1b)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `e889246e2ee3ea68` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-radiologic-technology-a-a-s · requirement_key=summer [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped
  - courses: RAD 212 ⟵ “RAD 212 - Clinical Radiography 3 6 credit hours”
### `e8a9d75c4a1d24ec` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mechatronics-engineering-technology-a-a-s · requirement_key=additional-general-education-requirements-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18472&returnto=18122 (sha256 7beddb2ca1f0)
- issues: requirement_groups_skipped
  - courses: CTA 100 ⟵ “CTA 100 - Computing and Information Technology  ​”
  - courses: CTA 103 ⟵ “CTA 103 - Computer Technology and Artificial Intelligence”
  - courses: CTP 115 ⟵ “CTP 115 - Introductory Object-Oriented Program Analysis and Design”
  - courses: CTS 107 ⟵ “CTS 107 - Cyber Essentials”
  - courses: EGR 120 ⟵ “EGR 120 - Introduction to Engineering Design”
  - courses: UAS 111 ⟵ “UAS 111 - Introduction to Drone Technology”
### `eae402a264c72c11` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-mechatronics-engineering-technology-a-a-s · requirement_key=biological-and-physical-sciences-4-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18472&returnto=18122 (sha256 7beddb2ca1f0)
- issues: requirement_groups_skipped
  - courses: PHY 111 ⟵ “PHY 111 - Fundamentals of Physics 1 4 credit hours OR”
  - courses: PHY 211 ⟵ “PHY 211 - General Physics 1 4 credit hours”
### `ee41d9bce6e52b98` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `ef93c075c1369ff3` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=social-and-behavioral-sciences-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
### `f0a7f83627caff62` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-homeland-security-management-a-a-s · requirement_key=additional-general-education-requirements-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18488&returnto=18122 (sha256 a94480b17f64)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: EMT 104 ⟵ “EMT 104 - Emergency Medical Care, CPR & AED  3 credit hours”
  - courses: HEA 150 ⟵ “HEA 150 - Advanced First Aid, CPR and AED  3 credit hours”
### `f231ca3509072bb4` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-engineering-transfer-a-s · requirement_key=technical-electives-refer-to-list-below-14-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18467&returnto=18122 (sha256 d611a13fc853)
- issues: requirement_groups_skipped
  - courses: BIO 107 ⟵ “BIO 107 - Environmental Science 4 credit hours”
  - courses: CHE 112 ⟵ “CHE 112 - General Chemistry 2 4 credit hours”
  - courses: CHE 134 ⟵ “CHE 134 - Chemistry Topics for Engineering 1 credit hour”
  - courses: CHE 213 ⟵ “CHE 213 - Organic Chemistry 1 4 credit hours”
  - courses: CHE 214 ⟵ “CHE 214 - Organic Chemistry 2 4 credit hours”
  - courses: EGR 209 ⟵ “EGR 209 - Statics 3 credit hours”
  - courses: EGR 211 ⟵ “EGR 211 - Mechanics of Materials 3 credit hours”
  - courses: EGR 222 ⟵ “EGR 222 - Dynamics 3 credit hours”
  - courses: EGR 235 ⟵ “EGR 235 - Circuit Theory 4 credit hours”
  - courses: EGR 241 ⟵ “EGR 241 - Systems and Signals 4 credit hours”
  - courses: EGR 244 ⟵ “EGR 244 - Digital Logic Design 4 credit hours”
  - courses: EGR 250 ⟵ “EGR 250 - Intermediate Programming for Engineers 3 credit hours”
  - courses: EGR 268 ⟵ “EGR 268 - Thermodynamics 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
  - courses: MAT 202 ⟵ “MAT 202 - Linear Algebra 4 credit hours”
  - courses: MAT 250 ⟵ “MAT 250 - Introduction to Discrete Structures 3 credit hours”
  - courses: PHY 213 ⟵ “PHY 213 - General Physics 3 4 credit hours”
### `f3b7048d70ac3346` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-and-jurisprudence-a-a · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18500&returnto=18122 (sha256 cba5e6015d8f)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `f3eeaf04e1c60c45` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-homeland-security-management-a-a-s · requirement_key=program-electives-12-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18488&returnto=18122 (sha256 a94480b17f64)
- issues: requirement_groups_skipped
  - courses: CJS 206 ⟵ “CJS 206 - Cybercrime 3 credit hours”
  - courses: ECO 116 ⟵ “ECO 116 - Inside the Global Economy 3 credit hours”
  - courses: HLS 225 ⟵ “HLS 225 - Introduction to Intelligence Analytics 3 credit hours”
  - courses: HLS 230 ⟵ “HLS 230 - Intelligence Support to the Policy Maker and Military 3 credit hours”
  - courses: HLS 240 ⟵ “HLS 240 - National Security Challenges of the 21st Century 3 credit hours”
  - courses: ECO 116 ⟵ “ECO 116 - Inside the Global Economy 3 credit hours”
  - courses: HIS 212 ⟵ “HIS 212 - United States History Since the Civil War 3 credit hours”
### `f4d7f1c4673f11eb` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-architecture-and-interior-design-a-a-s · requirement_key=interior-design-area-of-concentration-requirements-21-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18404&returnto=18122 (sha256 c3bbbe6dcef7)
- issues: requirement_groups_skipped
  - courses: ACH 100 ⟵ “ACH 100 - Introduction to Interior Design 1 credit hour”
  - courses: ACH 104 ⟵ “ACH 104 - Interior Finishes and Applications 3 credit hours”
  - courses: ACH 106 ⟵ “ACH 106 - Interior Design Studio 3 credit hours”
  - courses: ACH 201 ⟵ “ACH 201 - History of Interior Design 3 credit hours”
  - courses: ACH 202 ⟵ “ACH 202 - Space Planning 4 credit hours”
  - courses: ACH 204 ⟵ “ACH 204 - Interior Construction Detailing 3 credit hours”
### `f62e9c08d03e0ced` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-radiologic-technology-a-a-s · requirement_key=second-year-term-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18521&returnto=18122 (sha256 deed6452451f)
- issues: requirement_groups_skipped
  - courses: RAD 250 ⟵ “RAD 250 - Radiation Biology, Protection, and Safety 4 credit hours”
  - courses: RAD 252 ⟵ “RAD 252 - Clinical Radiography 5 6 credit hours”
### `f6bc2be586440206` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-physical-therapist-assistant-a-a-s · requirement_key=first-year-fall-term [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18518&returnto=18122 (sha256 393dbc3378ab)
- issues: requirement_groups_skipped
  - courses: BIO 231 ⟵ “BIO 231 - Human Biology 1 4 credit hours OR”
  - courses: BIO 233 ⟵ “BIO 233 - Anatomy and Physiology 1 4 credit hours”
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours OR”
  - courses: ENG 101A ⟵ “ENG 101A - Academic Writing and Research 1 3 credit hours”
  - courses: MAT 137 ⟵ “MAT 137 - College Algebra 3 credit hours”
  - courses: PSY 111 ⟵ “PSY 111 - Introduction to Psychology 3 credit hours”
  - courses: PTA 101 ⟵ “PTA 101 - Introduction to Physical Therapist Assistant 3 credit hours”
### `f7bd610e857b4581` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-law-enforcement-and-criminal-justice-a-a-s · requirement_key=suggestive-elective-requirements-12-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18501&returnto=18122 (sha256 6891dce62abe)
- issues: requirement_groups_skipped
  - courses: CJS 224 ⟵ “CJS 224 - Criminology 3 credit hours”
  - courses: CJS 228 ⟵ “CJS 228 - Practices in Social Work and Counseling with Inmate Populations 3 credit hours”
  - courses: HUS 100 ⟵ “HUS 100 - Introduction to Human Services 3 credit hours”
  - courses: CJS 132 ⟵ “CJS 132 - Juvenile Delinquency 3 credit hours”
  - courses: CJS 231 ⟵ “CJS 231 - Juvenile Justice 3 credit hours”
  - courses: CJS 232 ⟵ “CJS 232 - Juvenile Law 3 credit hours”
  - courses: PSY 211 ⟵ “PSY 211 - Developmental Psychology 3 credit hours”
### `f9bc05424f808269` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s · requirement_key=first-year-term-2 [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
  - courses: BIO 223 ⟵ “BIO 223 - General Microbiology 4 credit hours”
  - courses: SOC 111 ⟵ “SOC 111 - Introduction to Sociology 3 credit hours”
  - courses: MAT 137 ⟵ “MAT 137 - College Algebra 3 credit hours”
  - courses: MLT 101 ⟵ “MLT 101 - Urinalysis and Body Fluids 3 credit hours”
  - courses: MLT 102 ⟵ “MLT 102 - Quality Assurance and Quality Control 1 credit hour”
### `fc0f8ee79dfae75a` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-development-a-a-s · requirement_key=english-composition-6-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18460&returnto=18122 (sha256 dc57c78c8099)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
  - courses: ENG 102 ⟵ “ENG 102 - Academic Writing and Research 2 3 credit hours”
### `fce9f1905b59c034` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-engineering-transfer-a-s · requirement_key=english-composition-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18467&returnto=18122 (sha256 d611a13fc853)
- issues: requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Academic Writing and Research 1 3 credit hours”
### `fd7e4c7f2561c228` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-kinesiology-a-s · requirement_key=program-electives-consult-with-an-advisor-8-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18486&returnto=18122 (sha256 1d9812f21d5b)
- issues: requirement_groups_skipped
  - courses: HEA 113 ⟵ “HEA 113 - Women’s Health 3 credit hours OR”
  - courses: GSS 113 ⟵ “GSS 113 - Women’s Health 3 credit hours”
  - courses: HEA 117 ⟵ “HEA 117 - Healthy Aging For Women 3 credit hours OR”
  - courses: GSS 117 ⟵ “GSS 117 - Healthy Aging for Women 3 credit hours”
  - courses: HEA 137 ⟵ “HEA 137 - Weight Management: Utilizing Healthy Approaches to Diet and Physical Activity 1 credit hour OR”
  - courses: BIO 137 ⟵ “BIO 137 - Weight Management: Utilizing Healthy Approaches to Diet and Physical Activity 1 credit hour”
  - courses: HEA 138 ⟵ “HEA 138 - Nutrition for Fitness and Sport 1 credit hour OR”
  - courses: BIO 138 ⟵ “BIO 138 - Nutrition for Fitness and Sport 1 credit hour”
  - courses: HEA 231 ⟵ “HEA 231 - Health Coach 3 credit hours”
  - courses: BIO 135 ⟵ “BIO 135 - Principles of Nutrition 3 credit hours”
  - courses: SPT 123 ⟵ “SPT 123 - Sports in America 3 credit hours”
  - courses: SPT 232 ⟵ “SPT 232 - Sport Psychology 3 credit hours”
  - courses: BPA 103 ⟵ “BPA 103 - Introduction to Entrepreneurship 3 credit hours”
  - courses: HEA 150 ⟵ “HEA 150 - Advanced First Aid, CPR and AED 3 credit hours”
  - courses: PBH 101 ⟵ “PBH 101 - Introduction to Public Health 3 credit hours”
  - courses: CHE 111 ⟵ “CHE 111 - General Chemistry 1 4 credit hours”
  - courses: PHY 111 ⟵ “PHY 111 - Fundamentals of Physics 1 4 credit hours”
  - courses: HEA 275 ⟵ “HEA 275 - Kinesiology and Public Health Internship 1 credit hour”
### `fe3659601fda48aa` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-early-childhood-development-a-a-s · requirement_key=program-requirements-37-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18460&returnto=18122 (sha256 dc57c78c8099)
- issues: requirement_groups_skipped
  - courses: EDU 131 ⟵ “EDU 131 - Children’s Literature 3 credit hours”
  - courses: EDU 132 ⟵ “EDU 132 - Introduction to Early Childhood Development 3 credit hours”
  - courses: EDU 133 ⟵ “EDU 133 - Growth and Development 3 credit hours”
  - courses: EDU 135 ⟵ “EDU 135 - Children’s Health, Nutrition and Safety 3 credit hours”
  - courses: EDU 214 ⟵ “EDU 214 - Introduction to Special Education 3 credit hours”
  - courses: EDU 229 ⟵ “EDU 229 - Observing and Assessing Young Children 1 credit hour”
  - courses: EDU 230 ⟵ “EDU 230 - Educator Portfolio Development 1 credit hour”
  - courses: EDU 231 ⟵ “EDU 231 - Infant/Toddler Child Care 3 credit hours”
  - courses: EDU 232 ⟵ “EDU 232 - School-Age Child Care 3 credit hours”
  - courses: EDU 235 ⟵ “EDU 235 - Child Care Administration 3 credit hours”
  - courses: EDU 239 ⟵ “EDU 239 - Quality Family and School Partnerships 1 credit hour”
  - courses: EDU 242 ⟵ “EDU 242 - Foundations of Reading and Language Arts 3 credit hours”
  - courses: EDU 247 ⟵ “EDU 247 - Early Childhood: Methods and Materials 3 credit hours”
  - courses: EDU 248 ⟵ “EDU 248 - Instructional Strategies 1 credit hour”
  - courses: ASL 111 ⟵ “ASL 111 - American Sign Language 1 3 credit hours (or higher) OR”
  - courses: SPA 111 ⟵ “SPA 111 - Elementary Spanish 1 3 credit hours”
### `fe4b9511c43c2a22` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-medical-laboratory-technician-a-a-s · requirement_key=program-total [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18511&returnto=18122 (sha256 8f3a385c8fc6)
- issues: requirement_groups_skipped
  - section: program-total ⟵ “”
### `ff14bdd7aecd0aea` Anne Arundel Community College — degree_requirements 2026-27 · program_key=program-name-information-assurance-and-cybersecurity-a-a-s · requirement_key=biological-and-physical-sciences-3-credits [new] (labeled_in_source)
- source: https://catalog.aacc.edu/preview_program.php?catoid=43&poid=18439&returnto=18122 (sha256 70cb44479a9a)
- issues: requirement_groups_skipped
  - courses: BIO 135 ⟵ “BIO 135 - Principles of Nutrition 3 credit hours”
### `1a6d2397512df647` Baltimore City Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.bccc.edu/paying-for-college/financial-aid-scholarships (sha256 e1abece1e670)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.bccc.edu/paying-for-college/financial-aid-scholarships/financial-aid-additional-information/satisfactory-academic-progress-appeals-statement,https://www.bccc.edu/paying-for-college/financial-aid-scholarships/satisfactory-academic-progress-sap-appeal-process
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Connect with your specialist for questions about FAFSA, verification, awards, SAP, appeals, and disbursements.”
  - sentence: sap_appeal ⟵ “Your specialist is here to provide guidance and answer questions regarding the FAFSA, verification requirements, financial aid awards, Satisfactory Academic Progress (SAP), appeals, and disbursement of funds.”
### `8553a724aeca351a` Baltimore City Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.bccc.edu/paying-for-college/financial-aid-scholarships/financial-aid-additional-information/satisfactory-academic-progress-appeals-statement (sha256 893506d07ae0)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.bccc.edu/paying-for-college/financial-aid-scholarships,https://www.bccc.edu/paying-for-college/financial-aid-scholarships/satisfactory-academic-progress-sap-appeal-process
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Instructions for completing the appeal process and the SAP Appeal Form may be obtained from the Financial Aid Office or printed from the Financial Aid web page on the BCCC website, under Financial Aid Forms.”
### `faf1536f69de363c` Baltimore City Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.bccc.edu/paying-for-college/financial-aid-scholarships/satisfactory-academic-progress-sap-appeal-process (sha256 5a471be457e0)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.bccc.edu/paying-for-college/financial-aid-scholarships,https://www.bccc.edu/paying-for-college/financial-aid-scholarships/financial-aid-additional-information/satisfactory-academic-progress-appeals-statement
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students who do not meet the College's Satisfactory Academic Progress (SAP) standards will have the opportunity to appeal their financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Please note that there is a deadline for submitting a SAP Appeal for the Fall 2026 term.”
### `594ba0a7bad8c0b4` Bowie State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bowiestate.edu/admissions-and-aid/financial-aid/financial-aid-process/satisfactory-academic-progress/sap-appeals-workshop.php (sha256 2d60205c2210)
- issues: semantic_review_required, conflicting_sources:https://www.bowiestate.edu/admissions-and-aid/financial-aid/sap-appeal-form.pdf,https://www.bowiestate.edu/admissions-and-aid/financial-aid/types-of-financial-aid/scholarship-opportunities/conroy-scholarship-application-2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “BSU National Alumni Association Goodloe Alumni House Workday Bulldog Connection MyBSU Library Directory Information For Prospective Students Alumni & Friends Parents & Families Community & Business Media Give Satisfactory Academic Progress (SAP) Workshops Submenu Satisfactory Academic Progress Graduate Satisfactory Academic Progress Policy Undergraduate Satisfactory Academic Progress Policy SAP Ap”
  - sentence: sap_appeal ⟵ “As a condition of the Financial Academic Plan that was signed after your SAP Appeal was approved, a workshop must be completed before the end of the Fall semester to be eligible for Spring Financial Aid.”
### `90c17bbd816e09ad` Bowie State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bowiestate.edu/admissions-and-aid/financial-aid/sap-appeal-form.pdf (sha256 40bc1be5aa2a)
- issues: semantic_review_required, conflicting_sources:https://www.bowiestate.edu/admissions-and-aid/financial-aid/financial-aid-process/satisfactory-academic-progress/sap-appeals-workshop.php,https://www.bowiestate.edu/admissions-and-aid/financial-aid/types-of-financial-aid/scholarship-opportunities/conroy-scholarship-application-2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL FORM STUDENT FIRST NAME STUDENT LAST NAME SCHOOL ID Students who are no longer eligible for federal, state or institutional aid as a result of not meeting Satisfactory Academic Progress (SAP) can submit a SAP appeal in an effort to re-establish their student aid eligibility.”
  - sentence: sap_appeal ⟵ “I have reviewed the SAP appeal review periods and decision deadlines outlined in this form and I understand that they are not negotiable.”
  - sentence: sap_appeal ⟵ “If your SAP Appeal is approved, your aid will be reinstated on a probationary basis for the year.”
### `97055c12a879e0d5` Bowie State University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.bowiestate.edu/admissions-and-aid/financial-aid/types-of-financial-aid/scholarship-opportunities/conroy-scholarship-application-2026-27.pdf (sha256 18218c4a2a01)
- issues: semantic_review_required, conflicting_sources:https://www.bowiestate.edu/admissions-and-aid/financial-aid/financial-aid-process/satisfactory-academic-progress/sap-appeals-workshop.php,https://www.bowiestate.edu/admissions-and-aid/financial-aid/sap-appeal-form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please visit the BSU website at Satisfactory Academic Progress Appeal | Bowie State to view the institutional guidelines. 2026 - 2027 Edward T. and Mary A.”
### `09283474c55cff29` Capitol Technology University — appeals 2026-27 [new] (source_unlabeled)
- source: https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/Awards_Process.jnz (sha256 7d24a64f5d2d)
- issues: semantic_review_required, conflicting_sources:https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/,https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/Awards_Process.jnz?portlet=Special_Circumstances
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Get help using 'Special Circumstances' If unexpected or unusual circumstances occur that affect you or your family's ability to meet the Expected Family Contribution (EFC), you may petition the financial aid office to reconsider your aid package.”
  - sentence: need_based_special_circumstances ⟵ “You can locate the appeal form under Financial Aid Forms or click here: Special Circumstance Appeal Form Special Loan Requirements Get help using 'Special Loan Requirements' You must be enrolled at least half-time (half-time status at Capitol Technology University is six credits each semester).”
### `b6d126dceea1404f` Capitol Technology University — appeals 2026-27 [new] (source_unlabeled)
- source: https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/Awards_Process.jnz?portlet=Special_Circumstances (sha256 c4c8366532cf)
- issues: semantic_review_required, conflicting_sources:https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/,https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/Awards_Process.jnz
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You can locate the appeal form under Financial Aid Forms or click here: Special Circumstance Appeal Form Policy statementAbout usContact us Powered by Jenzabar. v2024.2”
### `fd5fd7f3b8285473` Capitol Technology University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/ (sha256 22a663d902ad)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/Awards_Process.jnz,https://mycapitol.captechu.edu/ICS/College_Offices/Financial_Aid_Office/Awards_Process.jnz?portlet=Special_Circumstances
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal Federal financial aid regulations allow the Financial Aid Office at Capitol Technology University to recalculate financial need in cases involving special circumstances that are not reflected on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “Access the Special Circumstance Appeal Form New MDCAPS Feature – Electronic File Upload Tool The Office of Student Financial Assistance (OSFA) within the Maryland Higher Education Commission (MHEC) has introduced a new feature in the Maryland College Aid Processing System (MDCAPS) called the Electronic File Upload Tool.”
### `17f00b21ea15035b` Capitol Technology University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.captechu.edu/admissions-and-financial-aid/undergraduate (sha256 cd1a41175fa2)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "rows": 7}
  - column:Tuition (per semester,12–18 credits): 13500 ⟵ “Tuition (per semester,12–18 credits) | $13500 | $13635”
  - column:Per-credit Tuition (over 18 credits): 1125 ⟵ “Per-credit Tuition (over 18 credits) | $1125 | $1125”
  - column:Student Activity Fee (resident): 189 ⟵ “Student Activity Fee (resident) | $189 | $204”
  - column:Student Activity Fee (commuter): 106 ⟵ “Student Activity Fee (commuter) | $106 | $115”
  - column:Information Technology Fee (per semester): 440 ⟵ “Information Technology Fee (per semester) | $440 | $450”
  - column:International Student Fee (per semester): 824 ⟵ “International Student Fee (per semester) | $824 | $824”
  - column:International Student Application Fee: 50 ⟵ “International Student Application Fee | $50 | $50”
  - column:Tuition (per semester,12–18 credits): 13635 ⟵ “Tuition (per semester,12–18 credits) | $13500 | $13635”
  - column:Per-credit Tuition (over 18 credits): 1125 ⟵ “Per-credit Tuition (over 18 credits) | $1125 | $1125”
  - column:Student Activity Fee (resident): 204 ⟵ “Student Activity Fee (resident) | $189 | $204”
  - column:Student Activity Fee (commuter): 115 ⟵ “Student Activity Fee (commuter) | $106 | $115”
  - column:Information Technology Fee (per semester): 450 ⟵ “Information Technology Fee (per semester) | $440 | $450”
  - column:International Student Fee (per semester): 824 ⟵ “International Student Fee (per semester) | $824 | $824”
  - column:International Student Application Fee: 50 ⟵ “International Student Application Fee | $50 | $50”
### `df1d788e6dec8f98` Capitol Technology University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.captechu.edu/admissions-and-financial-aid/military-and-veterans (sha256 183efd03979d)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - off_campus_not_with_family:Tuition: 7800 ⟵ “Tuition | $7800”
  - off_campus_not_with_family:Fees: 540 ⟵ “Fees | $540”
  - off_campus_not_with_family:Books, Course Materials, Supplies, and Equipment: 410 ⟵ “Books, Course Materials, Supplies, and Equipment | $410”
  - off_campus_not_with_family:Living Expenses: Housing: 13374 ⟵ “Living Expenses: Housing | $13374”
  - off_campus_not_with_family:Living Expenses: Food: 8372 ⟵ “Living Expenses: Food | $8372”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1846 ⟵ “Miscellaneous Personal Expenses | $1846”
  - off_campus_not_with_family:Transportation: 1970 ⟵ “Transportation | $1970”
  - off_campus_not_with_family:Loan Fees: 480 ⟵ “Loan Fees | $480”
  - off_campus_not_with_family:Total Cost of Attendance/Budget: 34792 ⟵ “Total Cost of Attendance/Budget | $34792”
### `e7725190e6b75618` Capitol Technology University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.captechu.edu/admissions-and-financial-aid/military-and-veterans (sha256 183efd03979d)
- issues: components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - off_campus_not_with_family:Tuition: 12000 ⟵ “Tuition | $12000”
  - off_campus_not_with_family:Fees: 480 ⟵ “Fees | $480”
  - off_campus_not_with_family:Books, Course Materials, Supplies, and Equipment: 400 ⟵ “Books, Course Materials, Supplies, and Equipment | $400”
  - off_campus_not_with_family:Living Expenses: Housing: 13036 ⟵ “Living Expenses: Housing | $13036”
  - off_campus_not_with_family:Living Expenses: Food: 8160 ⟵ “Living Expenses: Food | $8160”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 2000 ⟵ “Miscellaneous Personal Expenses | $2000”
  - off_campus_not_with_family:Transportation: 1920 ⟵ “Transportation | $1920”
  - off_campus_not_with_family:Total Cost of Attendance/Budget: 37796 ⟵ “Total Cost of Attendance/Budget | $37796”
### `afaaaa28dded8b47` Carroll Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.carrollcc.edu/wp-content/uploads/Cost-of-Attendance-2025-2026-web.pdf (sha256 726ff50f1079)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 22}
  - column:Tuition & Fees: 5096 ⟵ “Tuition & Fees | 5,096 | 8,631 | 11,851”
  - column:Books & Supplies: 2000 ⟵ “Books & Supplies | 2,000 | 2,000 | 2,000”
  - column:Living Expenses: 2000 ⟵ “Living Expenses | 2,000 | 2,000 | 2,000”
  - column:Transportation: 1500 ⟵ “Transportation | 1,500 | 1,500 | 1,500”
  - column:Miscellaneous: 1000 ⟵ “Miscellaneous | 1,000 | 1,000 | 1,000”
  - column:Total: 11596 ⟵ “Total | 11,596 | 15,131 | 18,351”
  - column:Tuition & Fees (2): 5096 ⟵ “Tuition & Fees | 5,096 | 8,631 | 11,851”
  - column:Books & Supplies (2): 2000 ⟵ “Books & Supplies | 2,000 | 2,000 | 2,000”
  - column:Living Expenses (2): 6000 ⟵ “Living Expenses | 6,000 | 6,000 | 6,000”
  - column:Transportation (2): 2000 ⟵ “Transportation | 2,000 | 2,000 | 2,000”
  - column:Miscellaneous (2): 1500 ⟵ “Miscellaneous | 1,500 | 1,500 | 1,500”
  - column:Total (2): 16596 ⟵ “Total | 16,596 | 20,131 | 23,351”
  - column:Tuition & Fees (3): 1820 ⟵ “Tuition & Fees | 1,820 | 3,082.50 | 4,232.50”
  - column:Books & Supplies (3): 2000 ⟵ “Books & Supplies | 2,000 | 2,000 | 2,000”
  - column:Living Expenses (3): 2000 ⟵ “Living Expenses | 2,000 | 2,000 | 2,000”
  - column:Transportation (3): 1500 ⟵ “Transportation | 1,500 | 1,500 | 1,500”
  - column:Total (3): 7320 ⟵ “Total | 7,320 | 8,582.50 | 9,732.50”
  - column:Tuition & Fees (4): 1820 ⟵ “Tuition & Fees | 1,820 | 3,082.50 | 4,232.50”
  - column:Books & Supplies (4): 2000 ⟵ “Books & Supplies | 2,000 | 2,000 | 2,000”
  - column:Living Expenses (4): 6000 ⟵ “Living Expenses | 6,000 | 6,000 | 6,000”
  - column:Transportation (4): 2000 ⟵ “Transportation | 2,000 | 2,000 | 2,000”
  - column:Total (4): 11820 ⟵ “Total | 11,820 | 13,082.50 | 14,232.50”
  - column:Tuition & Fees: 8631 ⟵ “Tuition & Fees | 5,096 | 8,631 | 11,851”
  - column:Books & Supplies: 2000 ⟵ “Books & Supplies | 2,000 | 2,000 | 2,000”
  - column:Living Expenses: 2000 ⟵ “Living Expenses | 2,000 | 2,000 | 2,000”
  - … 41 more rows
### `61c63983f57d0f84` Carroll Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.carrollcc.edu/admissions-aid/what-course-credit-do-i-already-have/college-level-examination-program/ (sha256 45ac1ea981e7)
- issues: rows_without_score
- checks: {"distinct_exams": 28, "equivalencies": 32, "rows_without_score": 32}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|None]:  ⟵ “ACCT-101 | 3 | Financial Accounting”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “BIOL-101 and BIOL-202 | 8 | Biology”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “BUAD-205 | 3 | Business Law, Introductory”
  - equivalencies[CLEP-CHEMISTRY|None]:  ⟵ “CHEM Elective | 3 | Chemistry”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|None]:  ⟵ “CIS-101 | 3 | Information Systems and Computer Applications”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|None]:  ⟵ “EDUC-225 | 3 | Educational Psychology”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|None]:  ⟵ “ENGL-101-College Writing | 3 | College Composition Modular”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “ENGL-100-FOCUS and ENGL-101-College Writing | 6 | College Composition”
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “ENGL-211-American Literature | 3 | American Literature”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “ENGL-240-British Literature | 3 | English Literature”
  - equivalencies[CLEP-FRENCH-LANGUAGE|None]:  ⟵ “FREN-100/-102 | 6 | French Level 1”
  - equivalencies[CLEP-FRENCH-LANGUAGE|None]:  ⟵ “FREN-100/-102/-201/-202 | 12 | French Level 2 (score of 59)”
  - equivalencies[CLEP-GERMAN-LANGUAGE|None]:  ⟵ “GERM-100/-102 | 6 | German Level 1”
  - equivalencies[CLEP-GERMAN-LANGUAGE|None]:  ⟵ “GERM-100/-102/-201/-202 | 12 | German Level 2 (score of 59)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|None]:  ⟵ “HIST-101 | 3 | Western Civilization I: Ancient Near East to 1648”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|None]:  ⟵ “HIST-102 | 3 | Western Civilization II: 1648 to the Present”
  - equivalencies[CLEP-HUMANITIES|None]:  ⟵ “HUMT Elective | 3 | Humanities (Fine Arts only)”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|None]:  ⟵ “MATH 113 (beginning fall 2024) | 4 | College Mathematics”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “MATH-126 | 4 | College Algebra”
  - equivalencies[CLEP-PRECALCULUS|None]:  ⟵ “MATH-130 | 5 | Precalculus”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “MATH-135 | 4 | Calculus”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|None]:  ⟵ “MKTG-201 | 3 | Marketing, Principles of”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|None]:  ⟵ “MGMT-201 | 3 | Management, Principle of”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “PSLS-100 | 3 | American Government”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “PSYC-101 | 3 | Psychology, Introductory”
  - … 7 more rows
### `dc1484dd4d8c5539` Cecil College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cecil.edu/foundation/foundation-scholarships/faqs-foundation-scholarships (sha256 2837d4d45139)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Students should follow the instructions as prompted to review the scholarship offer and click "Accept" under the appropriate scholarship.”
### `87301564c4485461` Cecil College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.cecil.edu/admissions/academic-credit-for-prior-learning-examinations (sha256 d5c42943bc25)
- issues: rows_without_score
- checks: {"distinct_exams": 28, "equivalencies": 29, "rows_without_score": 29}
  - equivalencies[CLEP-INFORMATION-SYSTEMS|None]:  ⟵ “Information Systems & Computer | 3 | CIS 101 (I)”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “Introduction to Business Law | 3 | BUS 210”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|None]:  ⟵ “Financial Accounting | 3 | ACC 101”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|None]:  ⟵ “Principles of Management | 3 | BUS 131”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|None]:  ⟵ “Principles of Marketing | 3 | BUS 212”
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “American Literature | 6 | EGL 205 (H), EGL 206 (H)”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|None]:  ⟵ “Analyzing & Interpreting Literature | 3 | EGL 102 (H)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | 3 | EGL 101 (E)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|None]:  ⟵ “College Composition Modular | 3 | EGL 101 (E)”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature | 6 | EGL 203 (H), EGL 204 (H)”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature/Composition | 6 | EGL 101 (E), EGL 102 (H)”
  - equivalencies[CLEP-HUMANITIES|None]:  ⟵ “Humanities | 3 | Humanities Elective (H)”
  - equivalencies[CLEP-FRENCH-LANGUAGE|None]:  ⟵ “French Language Level 1 | 6 | FRN 101 (H), FRN 102 (H)”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “Spanish Language Level 1 | 6 | SPN 101 (H), SPN 102 (H)”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “American Government | 3 | POS 201 (SS)”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|None]:  ⟵ “Human Growth and Development | 3 | PSY 201 (SS)”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|None]:  ⟵ “Introduction to Educational Psychology | 3 | PSY 207”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introduction to Psychology | 3 | PSY 101 (SS)”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Introduction to Sociology | 3 | SOC 101 (SS)”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “Principles of Macroeconomics | 3 | ECO 222 (SS)”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | 3 | ECO 221 (SS)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|None]:  ⟵ “Western Civilization I | 3 | HST 101 (H)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|None]:  ⟵ “Western Civilization II | 3 | HST 102 (H)”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “Biology | 3 | BIO 101 (S)”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | 4 | MAT 201 (M)”
  - … 4 more rows
### `bab36d14f17b882a` Cecil College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.cecil.edu/admissions/academic-credit-for-prior-learning-examinations (sha256 d5c42943bc25)
- issues: score_column_not_scores
- checks: {"distinct_exams": 15, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[IB-VISUAL-ARTS|Higher]:  ⟵ “Visual Arts | Higher | 5, 6, 7 | ART 101 | 3”
  - equivalencies[IB-BIOLOGY|Standard]:  ⟵ “Biology | Standard | 5, 6, 7 | BIO 101 | 3”
  - equivalencies[IB-BIOLOGY|Higher]:  ⟵ “Biology | Higher | 5, 6, 7 | BIO 130 | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Standard orHigher]:  ⟵ “Business Organization | Standard orHigher | 5, 6, 7 | BUS 103 | 3”
  - equivalencies[IB-CHEMISTRY|Standard]:  ⟵ “Chemistry | Standard | 5, 6, 7 | None | 0”
  - equivalencies[IB-CHEMISTRY|Higher]:  ⟵ “Chemistry | Higher | 5, 6, 7 | CHM 103 andCHM 113 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|Standard orHigher]:  ⟵ “Computer Science | Standard orHigher | 5, 6, 7 | CSC 104 | 3”
  - equivalencies[IB-ENGLISH-A-LITERATURE|Standard]:  ⟵ “English A Literature | Standard | 5, 6, 7 | EGL 101 | 3”
  - equivalencies[IB-ENGLISH-A-LITERATURE|Higher]:  ⟵ “English A Literature | Higher | 5, 6, 7 | EGL 102 | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|Standard]:  ⟵ “Environmental Systems and Societies | Standard | 5, 6, 7 | ENV 106 | 3”
  - equivalencies[IB-GEOGRAPHY|Standard]:  ⟵ “Geography | Standard | 5, 6, 7 | GEO 101 | 3”
  - equivalencies[IB-GEOGRAPHY|Higher]:  ⟵ “Geography | Higher | 5, 6, 7 | GEO 102 | 3”
  - equivalencies[IB-HISTORY|Standard orHigher]:  ⟵ “World History | Standard orHigher | 5, 6, 7 | HST 111 orHST 102 | 3”
  - equivalencies[IB-HISTORY|Standard orHigher]:  ⟵ “American History | Standard orHigher | 5, 6, 7 | HST 201 orHST 202 | 3”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|Standard orHigher]:  ⟵ “Mathematic Applications and Interpretations | Standard orHigher | 5, 6, 7 | MAT 110 | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|Standard]:  ⟵ “Mathematic Analysis and Approaches | Standard | 5, 6, 7 | MAT 125 andMAT 127 | 8”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|Higher]:  ⟵ “Mathematic Analysis and Approaches | Higher | 5, 6, 7 | MAT 127 andMAT 201 | 8”
  - equivalencies[IB-MUSIC|Standard]:  ⟵ “Music | Standard | 5, 6, 7 | MUC 143 | 3”
  - equivalencies[IB-MUSIC|Higher]:  ⟵ “Music | Higher | 5, 6, 7 | MUC 110 andMUC 143 | 6”
  - equivalencies[IB-MUSIC|Standard]:  ⟵ “Music | Standard | 5, 6, 7 | PHI 101 | 3”
  - equivalencies[IB-MUSIC|Higher]:  ⟵ “Music | Higher | 5, 6, 7 | PHI 101 andPHI 201 | 6”
  - equivalencies[IB-PHYSICS|Standard]:  ⟵ “Physics | Standard | 5, 6, 7 | PHY 181 andPHY 182 | 8”
  - equivalencies[IB-PHYSICS|Higher]:  ⟵ “Physics | Higher | 4, 5, 6, 7 | PHY 181 andPHY 182 | 8”
  - equivalencies[IB-PSYCHOLOGY|Standard]:  ⟵ “Psychology | Standard | 5, 6, 7 | PSY 101 | 3”
  - equivalencies[IB-PSYCHOLOGY|Higher]:  ⟵ “Psychology | Higher | 5, 6, 7 | PSY 101 andPSY Elective | 6”
  - … 2 more rows
### `m2adbae56e9aff1b` Cecil College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://www.cecil.edu/programs-courses/academics/early-college-academy (sha256 53866fcf1118)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - per_credit_hour_charge: 540 ⟵ “| Based on $540 per credit (Fall 2025 average)”
  - eligibility_tier: 3.0 ⟵ “Minimum of 3.0 unweighted grade point average”
### `137a1943edea0801` Cecil College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.cecil.edu/wp-content/documents/articulation-agreements/alvernia-university/alvernia-dual-admissions.pdf (sha256 c0419e2577f3)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `26ec59ad3ad83f34` Chesapeake College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chesapeake.edu/costs-funding/credit/policies-forms/ (sha256 ac100b67dc38)
- issues: semantic_review_required, conflicting_sources:https://www.chesapeake.edu/costs-funding/credit/policies-forms/sap-appeal/
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “To be considered as making satisfactory academic progress, a student must maintain: | Credit Hours Attempted | Minimum GPA | 6 – 15 | 1.5 GPA | 16 – 45 | 1.75 GPA | 46+ | 2.0 GPA After Reading Above – Submit Your SAP Appeal Form Explore SAP FAQs Financial Aid Appeal and Review Process Financial Aid Review Process Financial aid recipients will be reviewed for satisfactory academic progress at the e”
  - sentence: sap_appeal ⟵ “Students may appeal their suspension status by completing the Satisfactory Academic Progress Appeal Form.”
  - sentence: sap_appeal ⟵ “Financial Aid Dismissal Once a student has been granted two appeals and continues to fail Satisfactory Academic Progress, the student will be permanently DISMISSED from financial aid.”
  - sentence: sap_appeal ⟵ “A student may appeal by submitting the Satisfactory Academic Progress Appeal Form to the Director of Financial Aid.”
  - sentence: sap_appeal ⟵ “All appeals MUST include the SAP Appeal Form and the Academic Plan Form.”
  - sentence: sap_appeal ⟵ “This is a status that only the Director can assign resulting from a SAP appeal request that has been approved.”
### `2bdedea82613c435` Chesapeake College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chesapeake.edu/costs-funding/credit/policies-forms/sap-appeal/ (sha256 7bcb511e3754)
- issues: semantic_review_required, conflicting_sources:https://www.chesapeake.edu/costs-funding/credit/policies-forms/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Please read this important information prior to completing the Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Important Information: Students must have a 2026/2027 FAFSA application on file BEFORE your SAP Appeal is reviewed Complete the FAFSA at studentaid.gov.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Form and Academic Plan It has been determined that you are not making satisfactory academic progress.”
### `3b544fb70c8e8c7c` Chesapeake College — appeals 2024-25 [new] (labeled_in_title)
- source: https://ecatalog.chesapeake.edu/mime/media/view/18/2022/2024-2025catalog.pdf (sha256 27f057d3a8fe)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Students may appeal their suspension status by completing the Satisfactory Academic Progress Appeal Form.”
  - sentence: sap_appeal ⟵ “Financial Aid Dismissal Once a student has been granted two appeals and continues to fail Satisfactory Academic Progress, the student will be permanently DISMISSED from financial aid.”
  - sentence: sap_appeal ⟵ “A student may appeal submitting the Satisfactory Academic Progress Appeal Form to the Office of Financial Aid.”
### `69992e768dc265da` Chesapeake College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.chesapeake.edu/costs-funding/credit/financial-aid/aid-process/ (sha256 615afadcc7df)
- issues: semantic_review_required, conflicting_sources:https://www.chesapeake.edu/costs-funding/credit/policies-forms/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you or your family experience special circumstances—like a loss of income, high medical expenses, or a death in the household—be sure to notify the Financial Aid Office.”
### `c0955bfc1f226f64` Chesapeake College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.chesapeake.edu/costs-funding/credit/policies-forms/ (sha256 ac100b67dc38)
- issues: semantic_review_required, conflicting_sources:https://www.chesapeake.edu/costs-funding/credit/financial-aid/aid-process/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students will be permitted to apply for two appeals based on specific circumstances such as; death of a relative, injury or illness of the student or other special circumstances.”
### `f57775f53ddbd52a` Chesapeake College — appeals 2024-25 [new] (labeled_in_title)
- source: https://ecatalog.chesapeake.edu/mime/media/view/18/2022/2024-2025catalog.pdf (sha256 27f057d3a8fe)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Students will be permitted to apply for TWO appeals based on specific circumstances such as; death of a relative, injury or illness of the student or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “A later date of admission may also be imposed on the service member for unusual circumstances, such as the time period required to prepare the service member to resume his or her course of study at the College.”
### `354f288059c95109` Chesapeake College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.chesapeake.edu/costs-funding/credit/tuition-costs/ (sha256 d56e2fabe070)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.chesapeake.edu/about/irpa/facts/,https://www.chesapeake.edu/costs-funding/credit/policies-forms/,https://www.chesapeake.edu/costs-funding/credit/tuition-costs/
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - column:Tuition & Fees: 4836 ⟵ “Tuition & Fees | $4,836 | $3,804 | $2,772 | $1,396”
  - column:Books & Supplies: 1150 ⟵ “Books & Supplies | $1,150 | $1,150 | $650 | $450”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 | $3,600 | $3,600 | $3,600”
  - column:Personal: 600 ⟵ “Personal | $600 | $600 | $600 | 0”
  - column:Living Expenses: 5460 ⟵ “Living Expenses | $5,460 | $5,460 | $5,460 | $5,460”
  - column:TOTAL: 15646 ⟵ “TOTAL | $15,646 | $14,614 | $13,082 | $10,906”
  - column:Tuition & Fees: 3804 ⟵ “Tuition & Fees | $4,836 | $3,804 | $2,772 | $1,396”
  - column:Books & Supplies: 1150 ⟵ “Books & Supplies | $1,150 | $1,150 | $650 | $450”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 | $3,600 | $3,600 | $3,600”
  - column:Personal: 600 ⟵ “Personal | $600 | $600 | $600 | 0”
  - column:Living Expenses: 5460 ⟵ “Living Expenses | $5,460 | $5,460 | $5,460 | $5,460”
  - column:TOTAL: 14614 ⟵ “TOTAL | $15,646 | $14,614 | $13,082 | $10,906”
  - column:Tuition & Fees: 2772 ⟵ “Tuition & Fees | $4,836 | $3,804 | $2,772 | $1,396”
  - column:Books & Supplies: 650 ⟵ “Books & Supplies | $1,150 | $1,150 | $650 | $450”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 | $3,600 | $3,600 | $3,600”
  - column:Personal: 600 ⟵ “Personal | $600 | $600 | $600 | 0”
  - column:Living Expenses: 5460 ⟵ “Living Expenses | $5,460 | $5,460 | $5,460 | $5,460”
  - column:TOTAL: 13082 ⟵ “TOTAL | $15,646 | $14,614 | $13,082 | $10,906”
  - column:Tuition & Fees: 1396 ⟵ “Tuition & Fees | $4,836 | $3,804 | $2,772 | $1,396”
  - column:Books & Supplies: 450 ⟵ “Books & Supplies | $1,150 | $1,150 | $650 | $450”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 | $3,600 | $3,600 | $3,600”
  - column:Personal: 0 ⟵ “Personal | $600 | $600 | $600 | 0”
  - column:Living Expenses: 5460 ⟵ “Living Expenses | $5,460 | $5,460 | $5,460 | $5,460”
  - column:TOTAL: 10906 ⟵ “TOTAL | $15,646 | $14,614 | $13,082 | $10,906”
### `792a62ddab056c36` Chesapeake College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.chesapeake.edu/about/irpa/facts/ (sha256 f886153d5aae)
- issues: implausible_amount, residency_unknown, conflicting_sources:https://www.chesapeake.edu/costs-funding/credit/policies-forms/,https://www.chesapeake.edu/costs-funding/credit/tuition-costs/,https://www.chesapeake.edu/costs-funding/credit/tuition-costs/
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 7352160 ⟵ “Tuition and Fees | $7,352,160 | 26%”
  - column:Federal: 0 ⟵ “Federal | $0 | 0%”
  - column:State: 10442665 ⟵ “State | $10,442,665 | 37%”
  - column:Local: 7710351 ⟵ “Local | $7,710,351 | 27%”
  - column:Other: 2662862 ⟵ “Other | $2,662,862 | 9%”
  - column:Total: 28168038 ⟵ “Total | $28,168,038 | 100%”
### `96cb89591ef6fd75` Chesapeake College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.chesapeake.edu/costs-funding/credit/tuition-costs/ (sha256 0c1afa3343b7)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.chesapeake.edu/about/irpa/facts/,https://www.chesapeake.edu/costs-funding/credit/policies-forms/,https://www.chesapeake.edu/costs-funding/credit/tuition-costs/
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - column:Tuition & Fees: 4836 ⟵ “Tuition & Fees | $4,836 | $3,804 | $2,772 | $1,396”
  - column:Books & Supplies: 1150 ⟵ “Books & Supplies | $1,150 | $1,150 | $650 | $450”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 | $3,600 | $3,600 | $3,600”
  - column:Personal: 600 ⟵ “Personal | $600 | $600 | $600 | 0”
  - column:Living Expenses: 5460 ⟵ “Living Expenses | $5,460 | $5,460 | $5,460 | $5,460”
  - column:TOTAL: 15646 ⟵ “TOTAL | $15,646 | $14,614 | $13,082 | $10,906”
  - column:Tuition & Fees: 3804 ⟵ “Tuition & Fees | $4,836 | $3,804 | $2,772 | $1,396”
  - column:Books & Supplies: 1150 ⟵ “Books & Supplies | $1,150 | $1,150 | $650 | $450”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 | $3,600 | $3,600 | $3,600”
  - column:Personal: 600 ⟵ “Personal | $600 | $600 | $600 | 0”
  - column:Living Expenses: 5460 ⟵ “Living Expenses | $5,460 | $5,460 | $5,460 | $5,460”
  - column:TOTAL: 14614 ⟵ “TOTAL | $15,646 | $14,614 | $13,082 | $10,906”
  - column:Tuition & Fees: 2772 ⟵ “Tuition & Fees | $4,836 | $3,804 | $2,772 | $1,396”
  - column:Books & Supplies: 650 ⟵ “Books & Supplies | $1,150 | $1,150 | $650 | $450”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 | $3,600 | $3,600 | $3,600”
  - column:Personal: 600 ⟵ “Personal | $600 | $600 | $600 | 0”
  - column:Living Expenses: 5460 ⟵ “Living Expenses | $5,460 | $5,460 | $5,460 | $5,460”
  - column:TOTAL: 13082 ⟵ “TOTAL | $15,646 | $14,614 | $13,082 | $10,906”
  - column:Tuition & Fees: 1396 ⟵ “Tuition & Fees | $4,836 | $3,804 | $2,772 | $1,396”
  - column:Books & Supplies: 450 ⟵ “Books & Supplies | $1,150 | $1,150 | $650 | $450”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 | $3,600 | $3,600 | $3,600”
  - column:Personal: 0 ⟵ “Personal | $600 | $600 | $600 | 0”
  - column:Living Expenses: 5460 ⟵ “Living Expenses | $5,460 | $5,460 | $5,460 | $5,460”
  - column:TOTAL: 10906 ⟵ “TOTAL | $15,646 | $14,614 | $13,082 | $10,906”
### `b7b11dcab9721bf3` Chesapeake College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.chesapeake.edu/costs-funding/credit/policies-forms/ (sha256 ac100b67dc38)
- issues: arrangement_unlabeled, cost_period_semester, residency_unknown, stacked_header_unparsed, conflicting_sources:https://www.chesapeake.edu/about/irpa/facts/,https://www.chesapeake.edu/costs-funding/credit/tuition-costs/,https://www.chesapeake.edu/costs-funding/credit/tuition-costs/
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees:: 843 ⟵ “Tuition and Fees: | $ 843 | Federal Pell Grant: | $1562”
  - column:Books and Supplies:: 200 ⟵ “Books and Supplies: | $ 200 | Perkins Loan | $1200”
  - column:Room and Board:: 675 ⟵ “Room and Board: | $ 675 |  | ”
  - column:Transportation:: 367 ⟵ “Transportation: | $ 367 |  | ”
  - column:Personal:: 552 ⟵ “Personal: | $ 552 |  | ”
  - column:Total Cost:: 2637 ⟵ “Total Cost: | $2637 | Total Aid: | $2762”
  - column:Tuition and Fees:: 1562 ⟵ “Tuition and Fees: | $ 843 | Federal Pell Grant: | $1562”
  - column:Books and Supplies:: 1200 ⟵ “Books and Supplies: | $ 200 | Perkins Loan | $1200”
  - column:Total Cost:: 2762 ⟵ “Total Cost: | $2637 | Total Aid: | $2762”
### `6468f2108af02178` College of Southern Maryland — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.csmd.edu/costs-aid/non-credit/workforce-sequence.html (sha256 74805ccd6194)
- issues: semantic_review_required, conflicting_sources:https://www.csmd.edu/_assets/fad/2026-2027-sap-appeal-form.pdf,https://www.csmd.edu/costs-aid/scholarships-financial-aid/forms/index.html,https://www.csmd.edu/costs-aid/scholarships-financial-aid/policies/index.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you have suspended financial aid, contact the CSM Financial Aid Office to complete a Satisfactory Academic Progress Appeal.”
### `69610d29e6c97ba4` College of Southern Maryland — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.csmd.edu/costs-aid/scholarships-financial-aid/policies/index.html (sha256 e0a8255a9424)
- issues: semantic_review_required, conflicting_sources:https://www.csmd.edu/_assets/fad/2026-2027-sap-appeal-form.pdf,https://www.csmd.edu/costs-aid/non-credit/workforce-sequence.html,https://www.csmd.edu/costs-aid/scholarships-financial-aid/forms/index.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “To request an appeal, students must complete a Satisfactory Academic Progress Appeal form, which can be obtained by either downloading it or requesting a hard copy from any of the Financial Assistance Department offices.”
### `7b0000b371eb9e8a` College of Southern Maryland — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.csmd.edu/costs-aid/scholarships-financial-aid/forms/index.html (sha256 c9ec2cda4832)
- issues: semantic_review_required, conflicting_sources:https://www.csmd.edu/_assets/fad/2026-2027-sap-appeal-form.pdf,https://www.csmd.edu/costs-aid/non-credit/workforce-sequence.html,https://www.csmd.edu/costs-aid/scholarships-financial-aid/policies/index.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Non-Verification-Related Financial Assistance Forms Loan Adjustment Form MD Pledge to Remain Drug Free Parent PLUS Loan Request Form Parent PLUS Loan Adjustment Form Satisfactory Academic Progress Appeal Form Social Security Disability Tuition Waiver Professional Judgment Professional judgment refers to the authority of a school’s financial aid administrator to adjust data elements on the FAFSA fo”
### `931e2c200db123ae` College of Southern Maryland — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.csmd.edu/_assets/fad/2026-2027-sap-appeal-form.pdf (sha256 d37ad5a12091)
- issues: semantic_review_required, conflicting_sources:https://www.csmd.edu/costs-aid/non-credit/workforce-sequence.html,https://www.csmd.edu/costs-aid/scholarships-financial-aid/forms/index.html,https://www.csmd.edu/costs-aid/scholarships-financial-aid/policies/index.html
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “2026-2027 Financial Assistance Satisfactory Academic Progress Appeal Student Name: Student ID: Program of Study: _____________________________________________________ To be eligible for financial assistance (federal student aid and most need-based assistance), Federal regulations require students to maintain Satisfactory Academic Progress (SAP) in three areas: cumulative grade point average (GPA),”
  - sentence: sap_appeal ⟵ “If such circumstances can be documented for the specific semester(s) when the deficiencies occurred, the student may submit this completed SAP Appeal Form along with all required documentation.”
  - sentence: sap_appeal ⟵ “Please check the term for which you are submitting a SAP appeal.”
  - sentence: sap_appeal ⟵ “I understand that the Appeals Committee will not accept any SAP appeal that is incomplete or lacks documentation.”
### `bf02b9d821481915` College of Southern Maryland — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.csmd.edu/_assets/fad/26-27-dependency-override-appeal.pdf (sha256 73dc185852aa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “2026-2027 DEPENDENCY OVERRIDE APPEAL Name__________________________________________________ Student ID___________________________ Address________________________________________ City____________________ State_____ Zip________ The U.S.”
  - sentence: dependency_override ⟵ “I was granted a Dependency Override and received financial aid as an independent student in 2025-26: 1.”
  - sentence: dependency_override ⟵ “Provide an updated statement below describing your current situation and relationship with your parent(s): OR I believe my family situation warrants Dependency Override consideration: 1.”
### `da984296bcffeb2f` College of Southern Maryland — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.csmd.edu/_assets/fad/2026-2027-special-circumstances-appeal.pdf (sha256 15c123f053fb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Financial Assistance Department 2026-2027 Special Circumstances Appeal Name: _________________________________________________ Student ID:____________________ On occasion, families experience extenuating circumstances which merit basing their financial assistance eligibility on adjusted income information.”
  - sentence: need_based_special_circumstances ⟵ “Submission of this form does not guarantee a change in your financial aid eligibility or award(s).”
  - sentence: need_based_special_circumstances ⟵ “A fully completed and signed Special Circumstances Appeal Form.”
### `df656bc91cc8a015` College of Southern Maryland — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.csmd.edu/costs-aid/scholarships-financial-aid/forms/index.html (sha256 c9ec2cda4832)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional judgments are made on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “CSM’s Financial Assistance Department will review every professional judgment request and make decisions based on the information and documentation provided.”
### `954f0c71bf4c7f45` College of Southern Maryland — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.csmd.edu/costs-aid/tuition-and-fees/tuition-calculator.html (sha256 1f7f89233f82)
- issues: components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 10050 ⟵ “Tuition and Fees | $10,050 | $10,050”
  - with_parents_or_family:Books, course materials, supplies and equipment: 1000 ⟵ “Books, course materials, supplies and equipment | $1,000 | $1,000”
  - with_parents_or_family:Transportation: 3630 ⟵ “Transportation | $3,630 | $3,630”
  - with_parents_or_family:Miscellaneous personal expenses: 2500 ⟵ “Miscellaneous personal expenses | $2,500 | $2,500”
  - with_parents_or_family:Living Expenses: 5733 ⟵ “Living Expenses | $5,733 | $17,199”
  - with_parents_or_family:Federal Student Loan Fees (average): 75 ⟵ “Federal Student Loan Fees (average) | $75 | $75”
  - with_parents_or_family:Total: 22996 ⟵ “Total | $22,996 | $34,462”
  - off_campus_not_with_family:Tuition and Fees: 10050 ⟵ “Tuition and Fees | $10,050 | $10,050”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1000 ⟵ “Books, course materials, supplies and equipment | $1,000 | $1,000”
  - off_campus_not_with_family:Transportation: 3630 ⟵ “Transportation | $3,630 | $3,630”
  - off_campus_not_with_family:Miscellaneous personal expenses: 2500 ⟵ “Miscellaneous personal expenses | $2,500 | $2,500”
  - off_campus_not_with_family:Living Expenses: 17199 ⟵ “Living Expenses | $5,733 | $17,199”
  - off_campus_not_with_family:Federal Student Loan Fees (average): 75 ⟵ “Federal Student Loan Fees (average) | $75 | $75”
  - off_campus_not_with_family:Total: 34462 ⟵ “Total | $22,996 | $34,462”
### `a216efe098fd6274` College of Southern Maryland — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csmd.edu/costs-aid/tuition-and-fees/tuition-calculator.html (sha256 1f7f89233f82)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 2, "components_reconcile": false, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 4200 ⟵ “Tuition and Fees | $4,200 | $4,200”
  - with_parents_or_family:Books, course materials, supplies and equipment: 1000 ⟵ “Books, course materials, supplies and equipment | $1,000 | $1,000”
  - with_parents_or_family:Transportation: 3630 ⟵ “Transportation | $3,630 | $3,630”
  - with_parents_or_family:Miscellaneous personal expenses: 2500 ⟵ “Miscellaneous personal expenses | $2,500 | $2,500”
  - with_parents_or_family:Living Expenses: 5733 ⟵ “Living Expenses | $5,733 | $17,199”
  - with_parents_or_family:Federal Student Loan Fees (average): 75 ⟵ “Federal Student Loan Fees (average) | $75 | $75”
  - with_parents_or_family:Total: 17146 ⟵ “Total | $17,146 | $28,612”
  - off_campus_not_with_family:Tuition and Fees: 4200 ⟵ “Tuition and Fees | $4,200 | $4,200”
  - off_campus_not_with_family:Books, course materials, supplies and equipment: 1000 ⟵ “Books, course materials, supplies and equipment | $1,000 | $1,000”
  - off_campus_not_with_family:Transportation: 3630 ⟵ “Transportation | $3,630 | $3,630”
  - off_campus_not_with_family:Miscellaneous personal expenses: 2500 ⟵ “Miscellaneous personal expenses | $2,500 | $2,500”
  - off_campus_not_with_family:Living Expenses: 17199 ⟵ “Living Expenses | $5,733 | $17,199”
  - off_campus_not_with_family:Federal Student Loan Fees (average): 75 ⟵ “Federal Student Loan Fees (average) | $75 | $75”
  - off_campus_not_with_family:Total: 28612 ⟵ “Total | $17,146 | $28,612”
### `ec9c4d235420638e` College of Southern Maryland — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.csmd.edu/apply-register/credit-for-prior-learning/index.html (sha256 3d311b5160ff)
- issues: score_column_not_scores
- checks: {"distinct_exams": 18, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|Social and Cultural Anthropology-Higher]:  ⟵ “Anthropology | Social and Cultural Anthropology-Higher | 5,6,7 | 3 | SOC Elective”
  - equivalencies[IB-BIOLOGY|Biology-Standard]:  ⟵ “Biology | Biology-Standard | 5,6,7 | 3 | BIO Elective”
  - equivalencies[IB-BIOLOGY|Biology-Higher]:  ⟵ “Biology | Biology-Higher | 5,6,7 | 4 | BIO-1060 /BIO-1060L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business-Standard & Higher]:  ⟵ “Business | Business-Standard & Higher | 5,6,7 | 3 | BAD Elective”
  - equivalencies[IB-CHEMISTRY|Chemistry-Standard]:  ⟵ “Chemistry | Chemistry-Standard | 5,6,7 | 3 | CHE-1050”
  - equivalencies[IB-CHEMISTRY|Chemistry-Higher]:  ⟵ “Chemistry | Chemistry-Higher | 5,6,7 | 4 | CHE-1200 /CHE-1200L”
  - equivalencies[IB-CHEMISTRY|Chinese-Higher]:  ⟵ “Chemistry | Chinese-Higher | 5 | 3 | LAN Elective”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science-Standard & Higher]:  ⟵ “Computer Science | Computer Science-Standard & Higher | 5,6,7 | 8 | CSC-2591 /CSC-2592”
  - equivalencies[IB-ECONOMICS|Economics-Standard]:  ⟵ “Economics | Economics-Standard | 5,6,7 | 3 | ECN-1200”
  - equivalencies[IB-ECONOMICS|Economics-Higher]:  ⟵ “Economics | Economics-Higher | 5,6,7 | 6 | ECN-1200 /ECN-2025”
  - equivalencies[IB-ECONOMICS|English A Literature-Higher]:  ⟵ “Economics | English A Literature-Higher | 5,6,7 | 3 | ENG Elective”
  - equivalencies[IB-FILM|Film-Higher]:  ⟵ “Film | Film-Higher | 5,6,7 | 3 | ENG Elective”
  - equivalencies[IB-FRENCH|French-Standard]:  ⟵ “French | French-Standard | 5,6,7 | 3 | LAN Elective”
  - equivalencies[IB-FRENCH|French-Higher]:  ⟵ “French | French-Higher | 5,6,7 | 6 | LAN Elective”
  - equivalencies[IB-GEOGRAPHY|Geography-Standard]:  ⟵ “Geography | Geography-Standard | 5,6,7 | 3 | GRY-1020”
  - equivalencies[IB-GEOGRAPHY|Geography-Higher]:  ⟵ “Geography | Geography-Higher | 5,6,7 | 6 | GRY-1020 /GRY Elective”
  - equivalencies[IB-GERMAN|German-Standard]:  ⟵ “German | German-Standard | 5,6,7 | 3 | LAN Elective”
  - equivalencies[IB-GERMAN|German-Higher]:  ⟵ “German | German-Higher | 5 | 3 | LAN Elective”
  - equivalencies[IB-HISTORY|History-Standard]:  ⟵ “History | History-Standard | 5,6,7 | 3 | HST Elective”
  - equivalencies[IB-HISTORY|History-Higher]:  ⟵ “History | History-Higher | 5,6,7 | 6 | HST Elective”
  - equivalencies[IB-LATIN|Latin-Standard or Higher]:  ⟵ “Latin | Latin-Standard or Higher | 5,6,7 | 3 | LAN Elective”
  - equivalencies[IB-MUSIC|Music-Standard]:  ⟵ “Music | Music-Standard | 5,6,7 | 3 | MUS-1020”
  - equivalencies[IB-MUSIC|Music-Higher]:  ⟵ “Music | Music-Higher | 5,6,7 | 3 | MUS-1020”
  - equivalencies[IB-PHILOSOPHY|Philosophy-Standard]:  ⟵ “Philosophy | Philosophy-Standard | 5,6,7 | 3 | PHL-1010”
  - equivalencies[IB-PHILOSOPHY|Philosophy-Higher]:  ⟵ “Philosophy | Philosophy-Higher | 5,6,7 | 6 | PHL-1010 /PHL Elective”
  - … 11 more rows
### `2a5fea3ac1a68615` Community College of Baltimore County — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.ccbcmd.edu/Paying-for-College/Tuition-and-Fees/Cost-of-Attendance/index.html (sha256 df4962f2a9b7)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & fees: 4536 ⟵ “Tuition & fees | $4,536 | $7,708 | $11,114”
  - with_parents_or_family:Books, materials & supplies: 1430 ⟵ “Books, materials & supplies | $1,430 | $1,430 | $1,430”
  - with_parents_or_family:Loan fees: 112 ⟵ “Loan fees | $112 | $112 | $112”
  - with_parents_or_family:Food & housing: 5836 ⟵ “Food & housing | $5,836 | $5,836 | $5,836”
  - with_parents_or_family:Personal expenses: 1510 ⟵ “Personal expenses | $1,510 | $1,510 | $1,510”
  - with_parents_or_family:Transportation: 2168 ⟵ “Transportation | $2,168 | $2,168 | $2,168”
  - with_parents_or_family:Total: 15592 ⟵ “Total | $15,592 | $18,764 | $22,170”
  - with_parents_or_family:Tuition & fees: 7708 ⟵ “Tuition & fees | $4,536 | $7,708 | $11,114”
  - with_parents_or_family:Books, materials & supplies: 1430 ⟵ “Books, materials & supplies | $1,430 | $1,430 | $1,430”
  - with_parents_or_family:Loan fees: 112 ⟵ “Loan fees | $112 | $112 | $112”
  - with_parents_or_family:Food & housing: 5836 ⟵ “Food & housing | $5,836 | $5,836 | $5,836”
  - with_parents_or_family:Personal expenses: 1510 ⟵ “Personal expenses | $1,510 | $1,510 | $1,510”
  - with_parents_or_family:Transportation: 2168 ⟵ “Transportation | $2,168 | $2,168 | $2,168”
  - with_parents_or_family:Total: 18764 ⟵ “Total | $15,592 | $18,764 | $22,170”
### `8a857761bd3e98b1` Coppin State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coppin.edu/satisfactory-academic-progress-sap (sha256 913ebffb37ad)
- issues: semantic_review_required, conflicting_sources:https://www.coppin.edu/sites/default/files/pdf-library/2025-11/Satisfactory-Academic-Progress-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “SAP Appeal Form What are the different SAP statuses?”
  - sentence: sap_appeal ⟵ “What every student should know about the SAP appeals process What should I include in my SAP appeal?”
  - sentence: sap_appeal ⟵ “You may submit an appeal when placed on suspension by completing a Financial Aid Satisfactory Academic Progress (SAP) Appeal.”
  - sentence: sap_appeal ⟵ “Your appeal must include: SAP appeal form Typed personal statement detailing why you failed to meet SAP, and how you will meet SAP the next semester Additional documentation that supports your personal statement Academic and success strategies plan outlining the coursework and any academic services you will use to ensure academic success How do I appeal my SAP status?”
### `d70996d2a0eb0a27` Coppin State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coppin.edu/sites/default/files/pdf-library/2025-11/Satisfactory-Academic-Progress-Appeal-Form.pdf (sha256 ec6d4dd4f1f4)
- issues: semantic_review_required, conflicting_sources:https://www.coppin.edu/satisfactory-academic-progress-sap
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Office of Financial Aid Phone: 410.951.3636 Miles Connor Admin Building, First Floor Satisfactory Academic Progress (SAP) Appeal Application Meeting financial aid Satisfactory Academic Progress (SAP) is a requirement for financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Please note that submitting a SAP appeal does not guarantee approval; there are three outcomes of an appeal of suspension: • Removal of the suspension if it has been incorrectly imposed • Granting approval for one semester on a probationary status • Denial of the appeal Deadlines There are SAP appeal submission deadlines for each semester.”
  - sentence: sap_appeal ⟵ “Please upload your complete SAP appeal package in your EagleLINKS Student Financial Planning (SFP) portal.”
### `52d4f181663038c7` Coppin State University — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.coppin.edu/tuition-and-aid/cost-attendance (sha256 bbbbcf7c05c9)
- issues: cost_period_semester, stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 2516 ⟵ “Tuition | $ 2,516 | $ 5,032”
  - on_campus:Mandatory Fees: 1034 ⟵ “Mandatory Fees | $ 1,034 | $ 2,068”
  - on_campus:Housing (Double Occupancy): 3299 ⟵ “Housing (Double Occupancy) | $ 3,299 | $ 6,598”
  - on_campus:Food (Average): 2704 ⟵ “Food (Average) | $ 2,704 | $ 5,408”
  - on_campus:Books and supplies (2): 950 ⟵ “Books and supplies (2) | $ 950 | $1,900”
  - on_campus:Transportation (2): 900.0 ⟵ “Transportation (2) | $ 900.00 | $ 1,800”
  - on_campus:Personal: 1700 ⟵ “Personal | $ 1,700 | $ 3,400”
  - on_campus:Loan Fees: 200.0 ⟵ “Loan Fees | $ 200.00 | $ 400”
  - on_campus:Total: 13303 ⟵ “Total | $13,303 | $26,406”
  - on_campus:Tuition: 5032 ⟵ “Tuition | $ 2,516 | $ 5,032”
  - on_campus:Mandatory Fees: 2068 ⟵ “Mandatory Fees | $ 1,034 | $ 2,068”
  - on_campus:Housing (Double Occupancy): 6598 ⟵ “Housing (Double Occupancy) | $ 3,299 | $ 6,598”
  - on_campus:Food (Average): 5408 ⟵ “Food (Average) | $ 2,704 | $ 5,408”
  - on_campus:Books and supplies (2): 1900 ⟵ “Books and supplies (2) | $ 950 | $1,900”
  - on_campus:Transportation (2): 1800 ⟵ “Transportation (2) | $ 900.00 | $ 1,800”
  - on_campus:Personal: 3400 ⟵ “Personal | $ 1,700 | $ 3,400”
  - on_campus:Loan Fees: 400 ⟵ “Loan Fees | $ 200.00 | $ 400”
  - on_campus:Total: 26406 ⟵ “Total | $13,303 | $26,406”
### `607f2b896011a88b` Coppin State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.coppin.edu/tuition-and-aid/cost-attendance (sha256 bbbbcf7c05c9)
- issues: cost_period_semester, stale_year_label:2025-26, conflicting_sources:https://www.coppin.edu/tuition-and-aid/tuition-and-fees
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 2565.0 ⟵ “Tuition | $2,565.00 | $5,130.00”
  - on_campus:Mandatory Fees: 1144.0 ⟵ “Mandatory Fees | $1,144.00 | $2,288.00”
  - on_campus:Housing (Double Occupancy): 3464.0 ⟵ “Housing (Double Occupancy) | $3,464.00 | $6,928.00”
  - on_campus:Food (Average): 2786.0 ⟵ “Food (Average) | $2,786.00 | $5,572.00”
  - on_campus:Books and Supplies: 950.0 ⟵ “Books and Supplies | $950.00 | $1,900.00”
  - on_campus:Transportation: 1000.0 ⟵ “Transportation | $1,000.00 | $2,000.00”
  - on_campus:Personal: 1758.0 ⟵ “Personal | $1,758.00 | $3,516.00”
  - on_campus:Loan Fees: 38.0 ⟵ “Loan Fees | $38.00 | $76.00”
  - on_campus:Total Costs (estimated): 13705.0 ⟵ “Total Costs (estimated) | $13,705.00 | $27,410.00”
  - on_campus:Tuition: 5130.0 ⟵ “Tuition | $2,565.00 | $5,130.00”
  - on_campus:Mandatory Fees: 2288.0 ⟵ “Mandatory Fees | $1,144.00 | $2,288.00”
  - on_campus:Housing (Double Occupancy): 6928.0 ⟵ “Housing (Double Occupancy) | $3,464.00 | $6,928.00”
  - on_campus:Food (Average): 5572.0 ⟵ “Food (Average) | $2,786.00 | $5,572.00”
  - on_campus:Books and Supplies: 1900.0 ⟵ “Books and Supplies | $950.00 | $1,900.00”
  - on_campus:Transportation: 2000.0 ⟵ “Transportation | $1,000.00 | $2,000.00”
  - on_campus:Personal: 3516.0 ⟵ “Personal | $1,758.00 | $3,516.00”
  - on_campus:Loan Fees: 76.0 ⟵ “Loan Fees | $38.00 | $76.00”
  - on_campus:Total Costs (estimated): 27410.0 ⟵ “Total Costs (estimated) | $13,705.00 | $27,410.00”
### `70545fdca3854b3b` Coppin State University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.coppin.edu/tuition-and-aid/tuition-and-fees (sha256 b6cdc64ef294)
- issues: cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition per semester (12 or more credits): 6097 ⟵ “Tuition per semester (12 or more credits) | $2,566.50 | $6,097”
  - on_campus:Technology Fee: 100 ⟵ “Technology Fee | $100 | $100”
  - on_campus:Student Activity Fee: 95 ⟵ “Student Activity Fee | $95 | $95”
  - on_campus:College Center Fee: 236 ⟵ “College Center Fee | $236 | $236”
  - on_campus:Auxiliary Construction Fee: 188 ⟵ “Auxiliary Construction Fee | $188 | $188”
  - on_campus:Athletic Fee: 525 ⟵ “Athletic Fee | $525 | $525”
  - on_campus:Health Insurance Fee (Option to waive) *: 1014 ⟵ “Health Insurance Fee (Option to waive) * | $1,014 | $1,014”
  - on_campus:Total Per-Semester Cost (including health insurance fee): 8255.0 ⟵ “Total Per-Semester Cost (including health insurance fee) | $4,724.50 | $8,255.00”
### `d8a953ac53b07422` Coppin State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.coppin.edu/tuition-and-aid/tuition-and-fees (sha256 b6cdc64ef294)
- issues: cost_period_semester
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - on_campus:Tuition & Mandatory Fees: 7363.0 ⟵ “Tuition & Mandatory Fees | $3,762.00 | $7,363.00”
  - on_campus:Health Insurance Fee*: 974.0 ⟵ “Health Insurance Fee* | $974.00 | $974.00”
  - on_campus:Total Cost: 8337.0 ⟵ “Total Cost | $4,736.00 | $8,337.00”
### `dd03aa99a50f9442` Coppin State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.coppin.edu/tuition-and-aid/tuition-and-fees (sha256 b6cdc64ef294)
- issues: cost_period_semester, stale_year_label:2025-26, conflicting_sources:https://www.coppin.edu/tuition-and-aid/cost-attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition per semester (12 or more credits): 2566.5 ⟵ “Tuition per semester (12 or more credits) | $2,566.50 | $6,097”
  - on_campus:Technology Fee: 100 ⟵ “Technology Fee | $100 | $100”
  - on_campus:Student Activity Fee: 95 ⟵ “Student Activity Fee | $95 | $95”
  - on_campus:College Center Fee: 236 ⟵ “College Center Fee | $236 | $236”
  - on_campus:Auxiliary Construction Fee: 188 ⟵ “Auxiliary Construction Fee | $188 | $188”
  - on_campus:Athletic Fee: 525 ⟵ “Athletic Fee | $525 | $525”
  - on_campus:Health Insurance Fee (Option to waive) *: 1014 ⟵ “Health Insurance Fee (Option to waive) * | $1,014 | $1,014”
  - on_campus:Total Per-Semester Cost (including health insurance fee): 4724.5 ⟵ “Total Per-Semester Cost (including health insurance fee) | $4,724.50 | $8,255.00”
### `dfbeef6363fc3606` Coppin State University — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.coppin.edu/tuition-and-aid/cost-attendance (sha256 bbbbcf7c05c9)
- issues: cost_period_semester, stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 5978 ⟵ “Tuition | $ 5,978 | $ 11,956”
  - on_campus:Mandatory Fees: 1034 ⟵ “Mandatory Fees | $ 1,034 | $ 2,068”
  - on_campus:Housing (Double Occupancy): 3299 ⟵ “Housing (Double Occupancy) | $ 3,299 | $ 6,598”
  - on_campus:Food (Average): 2704 ⟵ “Food (Average) | $ 2,704 | $ 5,408”
  - on_campus:Books and supplies (2): 950 ⟵ “Books and supplies (2) | $ 950 | $ 1,900”
  - on_campus:Transportation (2): 900 ⟵ “Transportation (2) | $ 900 | $ 1,800”
  - on_campus:Personal: 1700 ⟵ “Personal | $ 1,700 | $ 3,400”
  - on_campus:Loan Fees: 200 ⟵ “Loan Fees | $ 200 | $ 400”
  - on_campus:Total: 16765 ⟵ “Total | $ 16,765 | $ 33,530”
  - on_campus:Tuition: 11956 ⟵ “Tuition | $ 5,978 | $ 11,956”
  - on_campus:Mandatory Fees: 2068 ⟵ “Mandatory Fees | $ 1,034 | $ 2,068”
  - on_campus:Housing (Double Occupancy): 6598 ⟵ “Housing (Double Occupancy) | $ 3,299 | $ 6,598”
  - on_campus:Food (Average): 5408 ⟵ “Food (Average) | $ 2,704 | $ 5,408”
  - on_campus:Books and supplies (2): 1900 ⟵ “Books and supplies (2) | $ 950 | $ 1,900”
  - on_campus:Transportation (2): 1800 ⟵ “Transportation (2) | $ 900 | $ 1,800”
  - on_campus:Personal: 3400 ⟵ “Personal | $ 1,700 | $ 3,400”
  - on_campus:Loan Fees: 400 ⟵ “Loan Fees | $ 200 | $ 400”
  - on_campus:Total: 33530 ⟵ “Total | $ 16,765 | $ 33,530”
### `dfdb58dd5f786de9` Coppin State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.coppin.edu/tuition-and-aid/tuition-and-fees (sha256 b6cdc64ef294)
- issues: cost_period_semester
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - on_campus:Tuition & Mandatory Fees: 3762.0 ⟵ “Tuition & Mandatory Fees | $3,762.00 | $7,363.00”
  - on_campus:Health Insurance Fee*: 974.0 ⟵ “Health Insurance Fee* | $974.00 | $974.00”
  - on_campus:Total Cost: 4736.0 ⟵ “Total Cost | $4,736.00 | $8,337.00”
### `cf646472b663eb29` Frederick Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.frederick.edu/paying-for-college/tuition-fees/cost-attendance.html (sha256 099ea7c7aba5)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Books, Course Materials, Supplies & Equipment: 1570 ⟵ “Books, Course Materials, Supplies & Equipment | $1,570 | $1,570 | $1,570”
  - off_campus_not_with_family:Living Expenses: Food: 3426 ⟵ “Living Expenses: Food | $3,426 | $3,426 | $3,426”
  - off_campus_not_with_family:Living Expenses: Housing: 7280 ⟵ “Living Expenses: Housing | $7,280 | $7,280 | $7,280”
  - off_campus_not_with_family:Personal Expenses: 7618 ⟵ “Personal Expenses | $7,618 | $7,618 | $7,618”
  - off_campus_not_with_family:Transportation: 2266 ⟵ “Transportation | $2,266 | $2,266 | $2,266”
  - off_campus_not_with_family:Tuition & Fees: 4054 ⟵ “Tuition & Fees | $4,054 | $8,038 | $10,630”
  - off_campus_not_with_family:Total: 26214 ⟵ “Total | $26,214 | $30,198 | $32,790”
  - off_campus_not_with_family:Books, Course Materials, Supplies & Equipment: 1570 ⟵ “Books, Course Materials, Supplies & Equipment | $1,570 | $1,570 | $1,570”
  - off_campus_not_with_family:Living Expenses: Food: 3426 ⟵ “Living Expenses: Food | $3,426 | $3,426 | $3,426”
  - off_campus_not_with_family:Living Expenses: Housing: 7280 ⟵ “Living Expenses: Housing | $7,280 | $7,280 | $7,280”
  - off_campus_not_with_family:Personal Expenses: 7618 ⟵ “Personal Expenses | $7,618 | $7,618 | $7,618”
  - off_campus_not_with_family:Transportation: 2266 ⟵ “Transportation | $2,266 | $2,266 | $2,266”
  - off_campus_not_with_family:Tuition & Fees: 8038 ⟵ “Tuition & Fees | $4,054 | $8,038 | $10,630”
  - off_campus_not_with_family:Total: 30198 ⟵ “Total | $26,214 | $30,198 | $32,790”
### `83f87607c64002dd` Frederick Community College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.frederick.edu/admissions/dual-enrollment.html (sha256 a8b2030b0702)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “have an unweighted cumulative GPA of 2.0 may consider dual enrollment. Assessment”
  - eligibility_tier: 2.0 ⟵ “have an unweighted cumulative GPA of 2.0 may consider dual enrollment. Assessment”
### `f33193e7736c0e62` Frederick Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.frederick.edu/admissions/index.html (sha256 734dfae83d0b)
- issues: course_column_missing
- checks: {"distinct_exams": 3, "equivalencies": 3, "rows_without_score": 0}
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 or better]:  ⟵ “English Language & Composition | 3 or better”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 or better]:  ⟵ “English Literature & Composition | 3 or better”
  - equivalencies[AP-STATISTICS|3 or better]:  ⟵ “Calculus or Statistics | 3 or better”
### `1c7203c4a48968ef` Frostburg State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.frostburg.edu/admissions-and-cost/financial-aid/managing-your-aid/satisfactory-academic-progress.php (sha256 47619b900754)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Additional communications via the FSU student email and academic advisors may also be utilized to alert and guide students through the SAP appeal process.”
  - sentence: sap_appeal ⟵ “As with any unsatisfactory academic progress, the student has the right to appeal the loss of financial aid.”
### `2cdaec9b7741b699` Frostburg State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.frostburg.edu/admissions-and-cost/financial-aid/managing-your-aid/special-circumstances.php (sha256 6759a57f674a)
- issues: semantic_review_required, conflicting_sources:https://www.frostburg.edu/admissions-and-cost/financial-aid/managing-your-aid/satisfactory-academic-progress.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Skip to Main Content Skip to Main Navigation Menu Why FSU?”
  - sentence: need_based_special_circumstances ⟵ “The following situations qualify as special conditions: A change in a student or parents income due to unemployment or a change of profession, divorce or separation A change in household income due to the loss of child support, alimony, social security benefits, disability benefits, or unemployment benefits A non-recurring income that was received for the prior year and recorded on the prior years”
### `3572b5b4a800f9a0` Frostburg State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.frostburg.edu/admissions-and-cost/financial-aid/managing-your-aid/satisfactory-academic-progress.php (sha256 47619b900754)
- issues: semantic_review_required, conflicting_sources:https://www.frostburg.edu/admissions-and-cost/financial-aid/managing-your-aid/special-circumstances.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals will be granted for the following circumstances: Students who demonstrate the following extenuating circumstances: death of a relative, injury or illness of the student, or other special circumstances; The school has determined that the student will be able to meet SAP standards after the subsequent payment period or; An academic plan had been established by the student and/or his or her a”
### `16a56b8bdf67ea99` Frostburg State University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.frostburg.edu/admissions-and-cost/undergraduate/tuition-and-aid.php (sha256 80e3c899c8ff)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 23306 ⟵ “Tuition | $23,306”
  - column:Housing and Meals (depending on type of accommodation): 15296 ⟵ “Housing and Meals (depending on type of accommodation) | $15,296”
  - column:Fees: 3050 ⟵ “Fees | $3,050”
  - column:TOTAL ESTIMATED BILLED EXPENSES: 41652 ⟵ “TOTAL ESTIMATED BILLED EXPENSES | $41,652”
### `8622ae307443505d` Frostburg State University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.frostburg.edu/admissions-and-cost/undergraduate/tuition-and-aid.php (sha256 80e3c899c8ff)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 17198 ⟵ “Tuition | $17,198”
  - column:Housing and Meals (depending on type of accommodation): 15296 ⟵ “Housing and Meals (depending on type of accommodation) | $15,296”
  - column:Fees: 3050 ⟵ “Fees | $3,050”
  - column:TOTAL ESTIMATED BILLED EXPENSES: 35544 ⟵ “TOTAL ESTIMATED BILLED EXPENSES | $35,544”
### `a1c2dfa124ee11eb` Frostburg State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.frostburg.edu/admissions-and-cost/undergraduate/tuition-and-aid.php (sha256 80e3c899c8ff)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 7414 ⟵ “Tuition | $7,414”
  - column:Housing and Meals (depending on type of accommodation): 15296 ⟵ “Housing and Meals (depending on type of accommodation) | $15,296”
  - column:Fees: 3050 ⟵ “Fees | $3,050”
  - column:TOTAL ESTIMATED BILLED EXPENSES: 25760 ⟵ “TOTAL ESTIMATED BILLED EXPENSES | $25,760”
### `79a9abbe267c567a` Goucher College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.goucher.edu/financial-aid/documents/SAP_Appeal.pdf (sha256 9cab69e1a552)
- issues: semantic_review_required, conflicting_sources:https://www.goucher.edu/policies/documents/Satisfactory-Academic-Progress-SAP-Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please provide name and relationship to you: _____ ___________ □ Injury or illness of student or relative. □ Other special circumstance beyond the student’s control.”
### `8b016595afc38209` Goucher College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.goucher.edu/policies/documents/Satisfactory-Academic-Progress-SAP-Policy.pdf (sha256 7f17e34d30f9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “RESOURCES/FAQ Satisfactory Academic Progress Policy (SAP) | Goucher College August 2024 Satisfactory Academic Progress Page 4 Microsoft Word - SAP APPEAL FORM.doc (goucher.edu) V.”
### `bb1b0194bdc07cbb` Goucher College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.goucher.edu/policies/documents/Satisfactory-Academic-Progress-SAP-Policy.pdf (sha256 7f17e34d30f9)
- issues: semantic_review_required, conflicting_sources:https://www.goucher.edu/financial-aid/documents/SAP_Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal Information: In accordance with federal regulations, students may appeal the finding that they failed to maintain satisfactory academic progress under subparagraph (G(c)(2)) above in the event of the death of a relative, an injury or illness of the student or other special circumstance.”
### `134eda82948651b2` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/admissions/financial-aid/resources.php (sha256 9d7eee3cebd1)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “You will only be eligible for Unsubsidized Federal Student Loans, not need-based aid—unless a dependency override is approved by the Financial Aid Office.”
### `2e145ff9d3a40fa7` Harford Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf (sha256 7331d776cfe3)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “An appeal based upon change in financial situation must be supported by a completed Professional Judgment Request Form. b.”
  - sentence: professional_judgment ⟵ “An appeal based upon change in financial situation must be supported by a completed Professional Judgment Request Form.”
### `379ff1c5a8a37ab0` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/admissions/financial-aid/fafsa.php (sha256 428b3bc7de9f)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “For the 2025–26 award year, an independent student is one of the following: born before Jan. 1, 2003 married (and not separated) a graduate or professional student a veteran a member of the armed forces an orphan a ward of the court Someone with legal dependents other than a spouse an emancipated minor someone who is unaccompanied and homeless or self-supporting and at risk of being homeless When ”
  - sentence: dependency_override ⟵ “The dependency override is an important step in seeing how much financial aid they'll be eligible for.”
### `588cdbb03fd7d1b2` Harford Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf (sha256 7331d776cfe3)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “An appeal of scholarship denial based upon financial ineligibility may be supported by a documented change in financial situation and/or evidence that supports a dependency override. a.”
### `711358b8a94afcb7` Harford Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf (sha256 7331d776cfe3)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “An appeal based upon circumstances that make it unreasonable to expect a parental contribution must be supported by a completed Dependency Override Form. 6.”
  - sentence: dependency_override ⟵ “An appeal based upon circumstances that make it unreasonable to expect a parental contribution must be supported by a completed Dependency Override Form.”
### `722efd34c05a2ac3` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/admissions/financial-aid/fafsa.php (sha256 428b3bc7de9f)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Pell Grant - Max/Min Determined by AGI (if required to file a federal tax return) Household size Federal poverty guidelines Professional Judgement & Appeals What constitutes Unusual Circumstances on the FAFSA®?”
  - sentence: professional_judgment ⟵ “If your financial circumstances have significantly changed since the tax year reported on your FAFSA, you may be eligible for a Professional Judgment Appeal.”
### `79614d6e658f87e3` Harford Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/sap-plan.pdf (sha256 f4f64f0ad84e)
- issues: semantic_review_required, conflicting_sources:https://catalog.harford.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “I understand that: • Transitional Studies courses do not count as college-level credit but are included in all SAP • My appeal is not approved until my completed academic plan calculations. is submitted to the Financial Aid Office and reviewed by the Financial Aid Appeals Committee.”
### `7d1f5f135f867cdb` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf (sha256 5a7420877367)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Student's Name: ____________________________ Harford ID:____________________________ Check one condition below that best describes the change in your financial situation.”
### `7ea029c936acc98b` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf (sha256 8e724b5e2f19)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Office 401 Thomas Run Road Bel Air, MD 21015 finaid@harford.edu PJUNCB 2026-2027 UNUSUAL CIRCUMSTANCES Student Name: _________________________________ Harford ID: __________________________ In the 2026-2027 FAFSA, provisional independent status may be granted to dependent students under certain circumstances where it is unreasonable to expect a parental contribution.”
  - sentence: need_based_special_circumstances ⟵ “However, it's important to note that there are criteria established by the Department of Education that do not qualify as "unusual circumstances" warranting a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Part I: UNUSUAL CIRCUMSTANCES: o Left home due to an abusive or threating environment o Are abandoned or estranged by Parents and not have been adopted o Have refugee or Asylee status and are separated from their parents, or their parents are displaced in a foreign country o Are a victim of human trafficking o Student or parent are incarcerated, and contact to parent would pose a risk o Unable to ”
### `9a5cda2575aa22d7` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf (sha256 5a7420877367)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Financial Aid Office 401 Thomas Run Road Bel Air, MD 21015 finaid@harford.edu PJDOCB 2026-2027 PROFESSIONAL JUDGEMENT REQUEST FORM Note: All supporting documentation must be received prior to the appeal being considered.”
### `ab690beb8a2b2230` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/admissions/financial-aid/fafsa.php (sha256 428b3bc7de9f)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances are when a student is unable to contact a parent or where contact with the parent poses a risk to the student.”
  - sentence: need_based_special_circumstances ⟵ “Applicants who indicate on their FAFSA® form that they have unusual circumstances will be granted provisional independent status.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances include human trafficking, legally granted refugee or asylum status, parental abandonment or estrangement, and student or parental incarceration.”
  - sentence: need_based_special_circumstances ⟵ “What you need to know: Students with unusual circumstances will be granted provisional independent status and can complete the FAFSA® form without providing parental information.”
  - sentence: need_based_special_circumstances ⟵ “A financial aid administrator will make the final determination of a student’s unusual circumstances based on the documentation that the student submits to the school, or the financial aid administrator may perform their own personal assessment.”
  - sentence: need_based_special_circumstances ⟵ “If a school approves a student’s unusual circumstances, their independent student status will remain as long as the student stays at the same school and their circumstances don’t change.”
### `b17310df948a37a6` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf (sha256 8e724b5e2f19)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php,https://www.harford.edu/admissions/financial-aid/resources.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “These circumstances, either individually or in combination, are not considered grounds for requesting a dependency override.”
  - sentence: dependency_override ⟵ “On the other hand, the Department of Education has defined specific instances where a dependency override may be appropriate, provided the student provides appropriate documentation.”
  - sentence: dependency_override ⟵ “Legally Grant refugee or Asylee status For students seeking a dependency override, documentation supporting one or more of these circumstances should be submitted to the aid administrator for consideration during the financial aid evaluation process.”
### `b44f79c159a95223` Harford Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/25-26/verification-forms/25-26-professional-judgement-form.pdf (sha256 235db0e461aa)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.harford.edu/_images/admissions/financial-aid/pdfs/25-26/verification-forms/25-26-unusual-circumstance.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Student's Name: ____________________________ Harford ID:____________________________ Check one condition below that best describes the change in your financial situation.”
### `b96dd21abd4dd065` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/admissions/financial-aid/resources.php (sha256 9d7eee3cebd1)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-unusual-circumstance.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Common Situations That May Qualify Loss or Reduction of Income (e.g., Job Loss, Reduced Hours) Divorce or Separation Death of a Parent or Spouse High Medical or Dental Expenses Not Covered by Insurance Other Significant Financial Changes Unusual Circumstances What if I have an unusual circumstance and cannot provide parental information to FAFSA®?”
  - sentence: need_based_special_circumstances ⟵ “If you're facing unusual circumstances that prevent you from providing parental information, you may be eligible for Provisional Independent Student status at Harford Community College.”
  - sentence: need_based_special_circumstances ⟵ “In such cases, you can complete the FAFSA® without parental details and submit an Unusual Circumstances Form instead.”
### `bcf7b83ba1919910` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.harford.edu/admissions/financial-aid/resources.php (sha256 9d7eee3cebd1)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/academics/workforce-career/scholarships/application-for-appeal-of-denial-of-continuing-education-and-training-scholarship-process-and-form.pdf,https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/26-27-professional-judgement-form.pdf,https://www.harford.edu/admissions/financial-aid/fafsa.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If your financial circumstances have significantly changed since the tax year reported on your FAFSA®, you may be eligible for a Professional Judgement Appeal.”
### `c5ffb689675c2895` Harford Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/25-26/verification-forms/25-26-unusual-circumstance.pdf (sha256 aa7dad552951)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.harford.edu/_images/admissions/financial-aid/pdfs/25-26/verification-forms/25-26-professional-judgement-form.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Office 401 Thomas Run Road Bel Air, MD 21015 finaid@harford.edu PJUNC 2025-2026 UNUSUAL CIRCUMSTANCES In the 2025-2026 FAFSA, provisional independent status may be granted to dependent students under certain circumstances where it is unreasonable to expect a parental contribution.”
  - sentence: need_based_special_circumstances ⟵ “However, it's important to note that there are criteria established by the Department of Education that do not qualify as "unusual circumstances" warranting a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Part I: UNUSUAL CIRCUMSTANCES: o Left home due to an abusive or threating environment o Are abandoned or estranged by Parents and not have been adopted o Have refugee or Asylee status and are separated from their parents, or their parents are displaced in a foreign country o Are a victim of human trafficking o Student or parent are incarcerated, and contact to parent would pose a risk o Unable to ”
### `c843287154951dfb` Harford Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.harford.edu/financial-aid/ (sha256 41f7de182786)
- issues: semantic_review_required, conflicting_sources:https://www.harford.edu/_images/admissions/financial-aid/pdfs/26-27/sap-plan.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid SAP Appeal Process Students whose federal or Maryland state financial aid has been terminated due to failure to meet Satisfactory Academic Progress (SAP) standards have the right to appeal the termination.”
  - sentence: sap_appeal ⟵ “Steps to Appeal SAP Termination Initiate the appeal with the Financial Aid Office by submitting the Satisfactory Academic Progress Appeal form.”
  - sentence: sap_appeal ⟵ “Students whose financial aid has been terminated due to failure to meet the required Satisfactory Academic Progress (SAP) standards are typically allowed to appeal this termination once.”
### `cd030dd8fc091b2a` Harford Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/25-26/verification-forms/25-26-professional-judgement-form.pdf (sha256 235db0e461aa)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Financial Aid Office 401 Thomas Run Road Bel Air, MD 21015 finaid@harford.edu PJ/DOC 2025-2026 PROFESSIONAL JUDGEMENT REQUEST FORM Note: All supporting documentation must be received prior to the appeal being considered.”
### `f4adefa6c6062447` Harford Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.harford.edu/_images/admissions/financial-aid/pdfs/25-26/verification-forms/25-26-unusual-circumstance.pdf (sha256 aa7dad552951)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “These circumstances, either individually or in combination, are not considered grounds for requesting a dependency override.”
  - sentence: dependency_override ⟵ “On the other hand, the Department of Education has defined specific instances where a dependency override may be appropriate, provided the student provides appropriate documentation.”
  - sentence: dependency_override ⟵ “Legally Grant refugee or Asylee status For students seeking a dependency override, documentation supporting one or more of these circumstances should be submitted to the aid administrator for consideration during the financial aid evaluation process.”
### `53879dd51bff0fee` Harford Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.harford.edu/financial-aid/ (sha256 41f7de182786)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 6}
  - column:Tuition and Fees: 4205 ⟵ “Tuition and Fees | $4,205”
  - column:Books and Supplies: 1300 ⟵ “Books and Supplies | $1,300”
  - column:Transportation: 2122 ⟵ “Transportation | 2,122”
  - column:Housing and Food: 3572 ⟵ “Housing and Food | $3,572”
  - column:Personal Expenses: 5142 ⟵ “Personal Expenses | $5,142”
  - column:Total1: 16341 ⟵ “Total1 | $16,341”
### `d5cda8cc66465789` Harford Community College — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.harford.edu/credit-by-examination/ (sha256 247a3441198d)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 14, "equivalencies": 65, "rows_without_score": 0}
  - equivalencies[IB-HISTORY|3]:  ⟵ “AP | African America History | General Education - Arts/Humanities (GAH) | 3 | 3”
  - equivalencies[IB-BIOLOGY|3]:  ⟵ “AP | Biology | BIO 100 or BIO 119 | 3 | 4”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “AP | Biology | BIO 120 or BIO 119 | 4 | 4”
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “AP | Biology | BIO 120 and 121 | 5 | 8”
  - equivalencies[IB-CHEMISTRY|3]:  ⟵ “AP | Chemistry | General Elective | 3 | 3”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “AP | Chemistry | CHEM 111 | 4 | 4”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “AP | Chemistry | CHEM 111 and CHEM 112 | 5 | 8”
  - equivalencies[IB-COMPUTER-SCIENCE|3]:  ⟵ “AP | Computer Science A | CSI 131 and CSI 132 | 3 | 8”
  - equivalencies[IB-HISTORY|3]:  ⟵ “AP | European History | HIST 101 and HIST 102 | 3 | 6”
  - equivalencies[IB-FRENCH|3]:  ⟵ “AP | French Language | FR 101, FR 102, FR 201 and FR 202 | 3 | 12”
  - equivalencies[IB-GERMAN|3]:  ⟵ “AP | German Language | GER 101, GER 102, GER 201, and GER 202 | 3 | 12”
  - equivalencies[IB-GEOGRAPHY|3]:  ⟵ “AP | Human Geography | GEOG 102 | 3 | 3”
  - equivalencies[IB-ECONOMICS|3]:  ⟵ “AP | Macroeconomics | ECON 101 | 3 | 3”
  - equivalencies[IB-ECONOMICS|3]:  ⟵ “AP | Microeconomics | ECON 102 | 3 | 3”
  - equivalencies[IB-MUSIC|3]:  ⟵ “AP | Music Theory | MUS 103 | 3 | 4”
  - equivalencies[IB-PSYCHOLOGY|3]:  ⟵ “AP | Psychology | PSY 101 | 3 | 3”
  - equivalencies[IB-PHYSICS|3]:  ⟵ “AP | Physics I | PHYS 101 | 3 | 4”
  - equivalencies[IB-PHYSICS|3]:  ⟵ “AP | Physics II | PHYS 102 | 3 | 4”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “AP | Physics C: Mechanics | PHYS 200 and PHYS 203 or PHYS 201 | 4 | 4”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “AP | Physics C: Elec/Magnetism | PHYS 204 | 4 | 4”
  - equivalencies[IB-SPANISH|3]:  ⟵ “AP | Spanish Language | SPAN 101, SPAN 102, SPAN 201, and SPAN 202 | 3 | 12”
  - equivalencies[IB-SPANISH|3]:  ⟵ “AP | Spanish Literature | SPAN 203 and SPAN 204 | 3 | 6”
  - equivalencies[IB-HISTORY|3]:  ⟵ “AP | U.S. History | HIST 103 and HIST 104 | 3 | 6”
  - equivalencies[IB-HISTORY|3]:  ⟵ “AP | World History | HIST 109 and HIST 110 | 3 | 6”
  - equivalencies[IB-HISTORY|50]:  ⟵ “CLEP | History of US I Colonization to 1877 | HIST 103 | 50 | 3”
  - … 40 more rows
### `1a52f7af85e81b22` Hood College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.hood.edu/media/57351 (sha256 4731412f7368)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Through the use of Professional Judgment, the Office of Financial Aid may be able to make adjustments to your FAFSA to account for financial changes and/or unusual expenses.”
  - sentence: professional_judgment ⟵ “All Professional Judgment requests are determined on a case-by-case basis and are not guaranteed to result in any additional financial aid.”
### `7f51f03802d6d069` Hood College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.hood.edu/net-price-calculator (sha256 09581725fa92)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Results of the calculator are not guaranteed, and special circumstances are reviewed by the Financial Aid Office.”
### `ad1c22ec60b84936` Hood College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hood.edu/admission-aid/financial-aid/apply-financial-aid/financial-aid-code-conduct (sha256 a047ec3fda83)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Avoidance of Conflicts of Interest: Staff members do not accept gifts, compensation, or benefits that could influence—or appear to influence—their professional judgment.”
### `c15c4a5540fef30b` Hood College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hood.edu/media/62281 (sha256 4428c764741b)
- issues: semantic_review_required, conflicting_sources:https://www.hood.edu/media/62276
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “APPEALS PROCESS Students on ﬁnancial aid suspension may submit an online SAP Appeal Form to the Ofﬁce of Financial Aid.”
### `c776e8e12dab417c` Hood College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.hood.edu/media/57351 (sha256 4731412f7368)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “2025-2026 Income Change Appeal Form for 2024 Income Student Name Student Email Student ID Parent(s) Name Parent Email Parent Phone Hood College recognizes that unusual circumstances exist and that standard financial aid forms do not always capture the current financial situations of our students and their families.”
  - sentence: need_based_special_circumstances ⟵ “OR  Other documentation that demonstrates proof of payment.  Other special or unusual circumstance(s) • If your concern is not covered in any of the above options, please submit a signed statement explaining the special or unusual circumstances to the Office of Financial Aid.”
  - sentence: need_based_special_circumstances ⟵ “We understand we must provide all requested documentation for consideration of our family’s special circumstances.”
### `d3019c087b4c8853` Hood College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hood.edu/media/62276 (sha256 4fb471433ccb)
- issues: semantic_review_required, conflicting_sources:https://www.hood.edu/media/62281
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “REINSTATEMENT OF AID Reinstatement of financial aid may be achieved as follows: • The student submits the online SAP Appeal Form, and all required supporting documentation in accordance with the appeals process.”
  - sentence: sap_appeal ⟵ “A student whose financial aid eligibility has been suspended may regain eligibility by either meeting all Satisfactory Academic Progress (SAP) standards or having an appeal approved by the Financial Aid Appeals Committee.”
  - sentence: sap_appeal ⟵ “APPEALS PROCESS Students on financial aid suspension may submit an online SAP Appeal Form to the Office of Financial Aid.”
  - sentence: sap_appeal ⟵ “SAP appeals must be submitted through the online SAP Appeal Form.”
### `d3f5a33d82d02e39` Hood College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.hood.edu/admission-aid/financial-aid/financial-aid-refund-withdrawal-policy (sha256 df6bdbd034db)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition and all fees: 2067 ⟵ “Tuition and all fees | $2,067”
  - column:Federal Pell Grant: 573 ⟵ “Federal Pell Grant | $573”
  - column:College Grant: 192 ⟵ “College Grant | $192”
  - column:Subsidized Federal Direct Loan: 2668 ⟵ “Subsidized Federal Direct Loan | $2,668”
  - column:Total Aid: 3397 ⟵ “Total Aid | $3,397”
  - column:Financial Aid: 3397 ⟵ “Financial Aid | $3,397”
  - column:College Charges Paid: 2067 ⟵ “College Charges Paid | $2,067”
  - column:Amount of excess funds to student: 1330 ⟵ “Amount of excess funds to student | $1,330”
### `73740e79ab896fca` Howard Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.howardcc.edu/admissions-aid/pay-for-college/financial-aid/special-circumstances/ (sha256 aef00af2e686)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances | HowardCC Skip Navigation Menu Search Tools & Resources Maps & Locations Discover HCC Discover HCC Helping You Get There Get a Two-Year College Degree Enter a New Career or Sharpen Skills Explore Personal Interests Resources for High School Students & Parents Adult Learners Veterans & Military Families International & Immigrant Students Alumni & Former Students Businesses & ”
  - sentence: need_based_special_circumstances ⟵ “A counselor will meet with the student and/or family to discuss the special circumstances.”
### `8e24400f0534a82f` Howard Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.howardcc.edu/admissions-aid/pay-for-college/financial-aid/special-circumstances/ (sha256 aef00af2e686)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Financial Aid Contact Us Phone: 443-518-1260 HCC Federal School Code: 008175 Fax: 443-518-4576 Location: RCF 243 Office Hours & More Information Special Circumstances Professional Judgements/Dependency Overrides Students must first submit a Free Application for Federal Student Aid (FAFSA) before requesting an appeal.”
  - sentence: professional_judgment ⟵ “These types of adjustments are made on a case-by-case bases in accordance with HCC’s Professional Judgment Policy.”
### `8ea3fd7a6d804613` Howard Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.howardcc.edu/admissions-aid/pay-for-college/financial-aid/special-circumstances/ (sha256 aef00af2e686)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “For dependency status appeals, student must meet with a financial aid representative and be willing to share personal information.”
### `97f080bb9f36fe9a` Howard Community College — appeals 2016-17 [new] (labeled_in_source)
- source: https://www.howardcc.edu/media/howardcc/admissions-aid/pay-for-college/documents/SAP-Standards-121515.pdf (sha256 d0dd76ed8383)
- issues: stale_year_label:2016-17, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The appeal must include any relevant ment, or other special circumstances.”
### `99121cc820fb696a` Howard Community College — appeals 2016-17 [new] (labeled_in_source)
- source: https://www.howardcc.edu/media/howardcc/admissions-aid/pay-for-college/documents/SAP-Standards-121515.pdf (sha256 d0dd76ed8383)
- issues: stale_year_label:2016-17, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: sap_appeal ⟵ “Students must work Students with this status will be reviewed at the end of the semester, and will be with their academic advisor to prepare an Academic Plan if they intend to submit placed on Financial Aid Restriction if the student has not met the minimum SAP re- an appeal of their Financial Aid Restriction Status. quirements, or did not meet the minimum goals of their Academic Plan, or it is de”
  - sentence: sap_appeal ⟵ “All appeals received will be reviewed by and Conditions Form must be submitted with the appeal. the Financial Aid SAP Appeal Committee.”
  - sentence: sap_appeal ⟵ “To ensure cancellation of all charges, students should the Financial Aid SAP Restriction Appeal form, and any relevant documenta- drop their classes during the 100% refund period.”
  - sentence: sap_appeal ⟵ “The Financial Aid SAP Restriction Appeal Form should include the for classes while in a SAP Restriction status should make other payment following information: arrangement with the Finance Office, including establishment of a pay- 1.”
  - sentence: sap_appeal ⟵ “The student’s specific plans to resolve the situation with any relevant granted, the student will be required to follow the terms of the revised documentation, which demonstrates that the student’s academic per- Financial Aid Academic Plan, in addition to any other terms established formance will improve and meet the minimum standards (i.e. the car by the Financial Aid SAP Appeals Committee. has b”
  - sentence: sap_appeal ⟵ “To locate the SAP Appeal form, select these links at www.howardcc.edu: Admissions & Aid/Financial Aid Services/Satisfactory Academic Process.”
### `30bd4af2be71eb8c` Howard Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.howardcc.edu/admissions-aid/apply-for-admission/advising/transfer-and-completion/test-charts/clep-credit-table/ (sha256 4362b8a94c9d)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 31, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting* | 50 | ACCT-111 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 50 | CMSY-110 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | BMGT-130 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BMGT-145 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BMGT-151 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL-201, ENGL-202 | 6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL-121 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular* | 50 | Arts & Sciences Elec | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL-203 & ENGL-204 | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|5059]:  ⟵ “French | 5059 | FREN-101 &FREN-102 FREN-101, 102 & 201 | 812”
  - equivalencies[CLEP-GERMAN-LANGUAGE|5060]:  ⟵ “German | 5060 | GERM-101 &GERM-102 GERM-101, 102 & 201 | 8 12”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50635065]:  ⟵ “Spanish Language Spanish with Writing | 50635065 | SPAN-101&SPAN-102SPAN-101, 102 & 201 SPAN-101&SPAN-102SPAN-101, 102 & 201 | 8 12 8 12”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | HUMN-101 | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH-141 | 4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH-181 | 4”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Math | 50 | MATH-132 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MATH-143 | 3”
  - equivalencies[CLEP-PRECALCULUS|61]:  ⟵ “Precalculus | 61 | MATH-143, MATH-153 | 6”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL-101 | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM-101 | 4”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | Scientific Reasoning Core (non-lab) | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLI-101 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSYC-200 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | EDUC-260 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECON-101 | 3”
  - … 7 more rows
### `6765109deaba3636` Howard Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.howardcc.edu/admissions-aid/apply-for-admission/advising/transfer-and-completion/test-charts/ap-credit-table/ (sha256 6c95f1f93009)
- issues: merged_score_cells, merged_score_cells
- checks: {"distinct_exams": 40, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design | 3 | 3 | ARTS-101”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design | 3 | 3 | ARTS-102”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | 3 | Social Science GenEd Core”
  - equivalencies[AP-ART-HISTORY|3 4]:  ⟵ “Art History | 3 4 | 3 6 | ARTS-260 ARTS-260 and ARTS-261”
  - equivalencies[AP-BIOLOGY|3 4]:  ⟵ “Biology | 3 4 | 4 8 | BIOL-101 BIOL-141 and BIOL-142”
  - equivalencies[AP-CALCULUS-AB|3 4]:  ⟵ “Calculus AB | 3 4 | 3 4 | MATH-153 MATH-181”
  - equivalencies[AP-CALCULUS-BC|3 4]:  ⟵ “Calculus BC | 3 4 | 3 4 | MATH-181 MATH-181 & 182”
  - equivalencies[AP-CALCULUS-BC|1 or 2 3 4]:  ⟵ “Calculus BC AB Subscore | 1 or 2 3 4 | 3 4 | MATH-153 MATH-181”
  - equivalencies[AP-CHEMISTRY|3 4]:  ⟵ “Chemistry | 3 4 | 4 8 | CHEM-101 CHEM-101 and CHEM-102”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | 8 | CHNS-101 and CHNS-102”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | 3 | 3 | POLI-201”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 4 | CMSY-166”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | 3 | CMSY-110”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing | 3 | 3 | ARTS-103”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | 3 | ENGL-121”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 4]:  ⟵ “English Literature and Composition | 3 4 | 3 6 | ENGL-121 ENGL-121 and ENGL-210”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 4 | ENST-105/ENST-115”
  - equivalencies[AP-EUROPEAN-HISTORY|3 4]:  ⟵ “European History | 3 4 | 3 6 | HIST-123 HIST-122 and HIST-123”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | 8 | FREN-101 and FREN-102”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | 3 | 8 | GERM-101 and GERM-102”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | GEOG-102”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture | 3 | 8 | ITAL-101 and ITAL-102”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture | 3 | 8 | JPNS-101 and JPSN-102”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | 3 | 6 | Arts & Humanities GenEd Core and World Language elective”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 3 | ECON-101”
  - … 16 more rows
### `6427f10178f73d75` Johns Hopkins University — appeals 2026-27 [new] (source_unlabeled)
- source: https://sfs.jhu.edu/undergraduate-satisfactory-academic-progress/ (sha256 ae16cb45bb48)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Appeal Process Students who wish to appeal must submit a completed SAP Appeal Packet at least two weeks before the start of the next semester.”
  - sentence: sap_appeal ⟵ “SAP Appeal Packet The committee will review the appeal and notify students of the decision within fourteen working days after the Appeals Committee meets and makes its determination.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Packet requires the following pieces of information.”
  - sentence: sap_appeal ⟵ “Appeal Deadlines Students who wish to appeal must submit a completed SAP Appeal packet at least 10 business days prior to the end of the semester that you’re not meeting SAP standards.”
### `7360690ecd95c2b0` Johns Hopkins University — appeals 2026-27 [new] (source_unlabeled)
- source: https://sfs.jhu.edu/undergraduate-satisfactory-academic-progress/ (sha256 ae16cb45bb48)
- issues: semantic_review_required, conflicting_sources:https://sfs.jhu.edu/cost-tuition/moving-off-campus/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Mitigating or special circumstances include, but are not limited to, serious illness or injury to student or immediate family member, death of an immediate family member, and significant trauma in a student’s life that impaired their emotional and/or physical health.”
### `dc96c8171e997426` Johns Hopkins University — appeals 2026-27 [new] (source_unlabeled)
- source: https://sfs.jhu.edu/cost-tuition/moving-off-campus/ (sha256 86ed2d606861)
- issues: semantic_review_required, conflicting_sources:https://sfs.jhu.edu/undergraduate-satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Requests for additional aid due to higher off-campus living expenses are only considered when there are special circumstances (e.g., medical reasons, care for a dependent, etc.).”
### `053e6d35e1d93c1f` Loyola University Maryland — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.loyola.edu/department/financial-aid/undergraduate/policies/appeals.html (sha256 8e78a728d847)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Incoming first-year and transfer students interested in appealing their financial aid eligibility or to pursue unusual circumstances may contact the Office of Financial Aid at financialaid@loyola.edu for instructions.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Aid eligibility for the 2026-2027 academic year is based on 2024 income and current asset information.”
  - sentence: need_based_special_circumstances ⟵ “Circumstances that can be taken into consideration include but are not limited to the following: Reduction or loss of income, employment or benefits One-time, non-recurring increase in income Death or disability of parent Divorce or separation Increase in number of dependents enrolled full-time in college for 2026-2027 academic year To initiate a special circumstance aid appeal you must complete t”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Students who are experiencing unusual parental circumstances or conditions may qualify for a dependency override to their FAFSA, making them an independent student for financial aid purposes.”
### `87c54dd5441f6fb3` Loyola University Maryland — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.loyola.edu/department/financial-aid/undergraduate/policies/sap.html (sha256 ba7cedfb5ab2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If the SAP appeal is denied, the student may attend without financial aid to re-establish eligibility.”
  - sentence: sap_appeal ⟵ “Students will be notified of their SAP appeal decision via email at their Loyola email address.”
### `c00e276e85329ba2` Loyola University Maryland — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.loyola.edu/department/financial-aid/undergraduate/tuition-price-affordability/ (sha256 6ec0df24311f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Students who incur costs for university health insurance, dependent care, disability-related expenses, or who are in academic programs that require licensure, certification, or a first credential, and have costs associated with obtaining such qualification may request a cost of attendance adjustment by contacting the Office of Financial Aid.”
### `f4fcd3b33bf9c776` Loyola University Maryland — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.loyola.edu/department/financial-aid/undergraduate/policies/appeals.html (sha256 8e78a728d847)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Reconsideration of Your 2026-2027 Aid Eligibility The Appeal Process is available to all students to request Professional Judgment consideration of special financial and/or unusual circumstances which may influence your or your family's ability to pay for college.”
  - sentence: professional_judgment ⟵ “The following are examples of unusual parental circumstances that would allow an aid administrator to make a professional judgment change to the FAFSA: Death or incapacitation of only parent Parental Abandonment, Abuse Parental Incarceration Parental whereabouts unknown Human Trafficking Refugee or Asylee Status To initiate an unusual circumstances appeal, you must complete the 2026-2027 Unusual C”
  - sentence: professional_judgment ⟵ “To initiate a medical expense appeal you must complete the 2026-2027 Medical Expense Appeal Form. *The appeal will be reviewed after you have been awarded for the 2026-2027 academic year. * Please note that documentation will be requested and required for all Professional Judgment Appeals.”
### `af569f76781e5cb3` Loyola University Maryland — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.loyola.edu/department/financial-aid/undergraduate/tuition-price-affordability/cost-breakdown.html (sha256 4ceee85f824f)
- issues: implausible_amount, conflicting_sources:https://www.loyola.edu/department/financial-aid/undergraduate/tuition-price-affordability/
- checks: {"columns": 1, "rows": 2}
  - column:Full Time (12-20 credits) - Flat Rate: 61810 ⟵ “Full Time (12-20 credits) - Flat Rate | N/A | $30,905 | $30,905 | $61,810”
  - column:Tuition Refund Plan(optional for all full-time students; can be waived starting 6/1): 220 ⟵ “Tuition Refund Plan(optional for all full-time students; can be waived starting 6/1) | N/A | $110 | $110 | $220”
### `c0e3547ec21efda1` Loyola University Maryland — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.loyola.edu/department/financial-aid/undergraduate/tuition-price-affordability/ (sha256 6ec0df24311f)
- issues: conflicting_sources:https://www.loyola.edu/department/financial-aid/undergraduate/tuition-price-affordability/cost-breakdown.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 61810 ⟵ “Tuition | $61,810”
  - on_campus:Living Expense: Housing: 12600 ⟵ “Living Expense: Housing | $12,600”
  - on_campus:Living Expense: Food: 7340 ⟵ “Living Expense: Food | $7,340”
  - on_campus:Books, Course Materials, Supplies, Equipment: 800 ⟵ “Books, Course Materials, Supplies, Equipment | $800”
  - on_campus:Transportation: 500 ⟵ “Transportation | $500”
  - on_campus:Miscellaneous Personal Expenses: 500 ⟵ “Miscellaneous Personal Expenses | $500”
  - on_campus:Student Loan Fees: 70 ⟵ “Student Loan Fees | $70”
  - on_campus:Total: 83620 ⟵ “Total | $83,620”
### `5ba592bd8ca37b33` Maryland Institute College of Art — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mica.edu/admissions/financial-aid/sap-satisfactory-academic-progress/ (sha256 cd9a259526ae)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 13}
  - sentence: sap_appeal ⟵ “Appeal: The SAP appeal is a process by which a student not meeting the SAP standards petitions for reconsideration of financial aid eligibility.”
  - sentence: sap_appeal ⟵ “A lack of awareness of withdrawal policies or requirements for satisfactory academic progress are unacceptable reasons to appeal.”
  - sentence: sap_appeal ⟵ “If a student does not meet the required GPA, withdraws, or fails courses while on an academic plan, they will be suspended from federal financial aid; however, they can submit a new SAP appeal.”
  - sentence: sap_appeal ⟵ “MAXIMUM TIME FRAME: Students may appeal their financial aid evaluation status by submitting an academic plan with their SAP appeal form.”
  - sentence: sap_appeal ⟵ “At this point, the student’s eligibility for federal and state financial aid programs is terminated and is not reinstated unless the student completes a Satisfactory Academic Progress appeal and signs an Academic plan.”
  - sentence: sap_appeal ⟵ “Students who wish to appeal should complete a Satisfactory Academic Progress Appeal Form found on our webpage- MICA SAP Appeal Students must explain the extenuating circumstances that prevented them from meeting SAP standards, what changed will enable them to meet them now, and submit documentation supporting extenuating circumstances.”
### `e5c38fda15247ab9` Maryland Institute College of Art — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mica.edu/admissions/financial-aid/undergraduate-financial-aid/mica-appeals/ (sha256 dfe0da6e0f3d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “All appeals for unusual circumstances are assessed and adjudicated by the staff in the MICA Financial Aid Office.”
### `d6f13c8184663bb3` McDaniel College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mcdaniel.edu/sites/default/files/2024-01/SAP%20policy_0.pdf (sha256 bd6dc9279ced)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If a student has successfully appealed financial aid suspension and is placed on financial aid probation but fails to meet the requirements of the financial aid probation contract/academic plan, the student may not appeal again unless the student has new unusual circumstances that led to academic difficulties.”
### `d9babf1023c5b56b` McDaniel College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mcdaniel.edu/sites/default/files/2024-01/SAP%20policy_0.pdf (sha256 bd6dc9279ced)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If a student chooses to appeal the suspension, the student must complete the Satisfactory Academic Progress Appeal Form, attach documentation that supports the basis of the appeal and submit the form and documentation to the Financial Aid Department.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Financial Aid Probation is a status assigned to a student who has failed to make SAP, successfully appealed and has had eligibility for aid reinstated for a defined period of time.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Financial Aid probation is a status assigned to a student who has failed to make Satisfactory Academic Progress, appealed, and has had eligibility for aid reinstated for a defined period of time.”
### `4f6a3ed91e4f3a9e` Montgomery College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.montgomerycollege.edu/paying-for-college/financial-aid/resources/standards-of-satisfactory-academic-progress.html (sha256 0172693ea5bc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students whose eligibility is terminated are not eligible for financial aid until an appeal is granted or satisfactory academic progress is re-established.”
  - sentence: sap_appeal ⟵ “Students who receive an administrative grade change (not a grade change based on a repeated class) may submit the SAP Appeal for Aid Reestablishment at the time of the grade change.”
### `8afa72f6b717936d` Montgomery College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.montgomerycollege.edu/_documents/academics/credit-for-prior-learning/ap-exams-and-mc-equivalencies.pdf (sha256 5a1a2bf3896f)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 37, "equivalencies": 40, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                           ARTH      3       ARTT127                                               3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                               BIOL      3       BIOL101                                               4”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                           CCAB      3       MATH 165                                              4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                           CCBV      3       MATH165                                               4”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus                           MATP      3       MATH120                                               3”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                             CHEM      3       CHEM109 & CHEM109L                                    4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture            CHLA      3       CHIN102                                               5”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government and Politics          USGV    3, 4, 5   POLI101                                               3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics   CPGV     3.4.5    POLI211                                               3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                    CMSC      3,4     CMSC140                                               3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles           CMSP    3, 4, 5   CMSC110                                               3”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Designn-2D                            AR2D      3       ARTT127                                               3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Design -3D                            AR3D      3       ARTT127                                               3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                               ARDR      3       ARTT127                                               3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition      ENLA      3       ENGL101                                               3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition    ENLI    3, 4, 5   ENGL 190                                              3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science                 EVSC    3, 4, 5   BIOL105 & BIOL106                                     4”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                      EUHI      3       HIST148                                               3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture           FRLA      3       FREN201                                               3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Literature                     FRLI      3       FREN207                                               3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture           GRLA      3       GERM201                                               3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                       HMGE    3, 4, 5   GEOG105                                               3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture          ITLA      3       ITAL102                                               3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture         JAPN      3       JAPN 101 & 102                                        8”
  - equivalencies[AP-LATIN|6]:  ⟵ “Latin                                 LATN    3, 4, 5   LATN 101 & LATN 102                                   6”
  - … 15 more rows
### `62947b6f5ad4908e` Morgan State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.morgan.edu/office-of-financial-aid/applying-for-aid/sap-policy (sha256 21094eb940cc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “This documentation will be reviewed by our office and we will notify you of the decision. back to top ↑ Office of Financial Aid Financial Aid News and Updates Applying For Aid Eligibility Cost of Attendance How To Apply Summer Aid Verification Gateway SAP Policy Special/Unusual Circumstances - Professional Judgement View and Accept Timelines Aid Revisions Terms and Conditions Rights and Responsibi”
### `7c0b61cb645081b3` Morgan State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.morgan.edu/financialaid (sha256 42e9bef064b8)
- issues: semantic_review_required, conflicting_sources:https://www.morgan.edu/office-of-financial-aid/applying-for-aid/sap-policy
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal- Monday, April 27, 2026 PLEASE NOTE: You must submit the required SAP appeal and supporting documents by Monday, April 27, 2026 or risk becoming ineligible for federal aid for the Spring 2026 semester.”
### `92433e98a2bb671f` Morgan State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.morgan.edu/office-of-financial-aid/applying-for-aid/sap-policy (sha256 21094eb940cc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “MSU may grant appeals for students who fail this standard due to personal injury or illness, the death of a relative, or other special circumstances.”
### `c063a00b1447c157` Morgan State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.morgan.edu/office-of-financial-aid/applying-for-aid/sap-policy (sha256 21094eb940cc)
- issues: semantic_review_required, conflicting_sources:https://www.morgan.edu/financialaid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The maximum time frame is based on the stature of limitations required for each educational program. back to top ↑ Failing Satisfactory Academic Progress Requirements/Regaining Federal Student Aid Eligibility Appeals and Probation MSU's Financial Aid SAP policy will permit appeals and probationary periods.”
### `331d62347a25cbb5` Notre Dame of Maryland University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://ndm.edu/about-us/business-office/tuition-fees/ (sha256 60895cdaa71b)
- issues: arrangement_unlabeled, conflicting_sources:https://absn.ndm.edu/admissions/tuition/,https://catalog.ndm.edu/tuition-and-fees-for-2026-2027,https://ndm.edu/about-us/business-office/tuition-fees/
- checks: {"columns": 2, "rows": 3}
  - column:Nursing Credits: 56 ⟵ “Nursing Credits | 56 | 56”
  - column:Tuition (entire nursing curriculum): 60690 ⟵ “Tuition (entire nursing curriculum) | $60,690 | $57,630”
  - column:Tuition + Program Fees: 64786 ⟵ “Tuition + Program Fees | $64,786 | $61,726”
  - on_campus:Nursing Credits: 56 ⟵ “Nursing Credits | 56 | 56”
  - on_campus:Tuition (entire nursing curriculum): 57630 ⟵ “Tuition (entire nursing curriculum) | $60,690 | $57,630”
  - on_campus:Tuition + Program Fees: 61726 ⟵ “Tuition + Program Fees | $64,786 | $61,726”
### `3963ffa707b7440c` Notre Dame of Maryland University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.ndm.edu/tuition-and-fees-for-2026-2027 (sha256 fc6524afb75c)
- issues: arrangement_unlabeled, conflicting_sources:https://absn.ndm.edu/admissions/tuition/,https://ndm.edu/about-us/business-office/tuition-fees/,https://ndm.edu/about-us/business-office/tuition-fees/
- checks: {"columns": 2, "rows": 3}
  - column:Nursing Credits: 56 ⟵ “Nursing Credits | 56 | 56”
  - column:Tuition (entire nursing curriculum): 60690 ⟵ “Tuition (entire nursing curriculum) | $60,690 | $57,630”
  - column:Tuition + Program Fees: 64786 ⟵ “Tuition + Program Fees | $64,786 | $61,726”
  - on_campus:Nursing Credits: 56 ⟵ “Nursing Credits | 56 | 56”
  - on_campus:Tuition (entire nursing curriculum): 57630 ⟵ “Tuition (entire nursing curriculum) | $60,690 | $57,630”
  - on_campus:Tuition + Program Fees: 61726 ⟵ “Tuition + Program Fees | $64,786 | $61,726”
### `4e185b3a5673dfbe` Notre Dame of Maryland University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://absn.ndm.edu/admissions/tuition/ (sha256 d4e01029ee06)
- issues: arrangement_unlabeled, conflicting_sources:https://catalog.ndm.edu/tuition-and-fees-for-2026-2027,https://ndm.edu/about-us/business-office/tuition-fees/,https://ndm.edu/about-us/business-office/tuition-fees/
- checks: {"columns": 2, "rows": 3}
  - column:Nursing Credits: 56 ⟵ “Nursing Credits | 56 | 56”
  - column:Tuition (entire nursing curriculum): 60690 ⟵ “Tuition (entire nursing curriculum) | $60,690 | $57,630”
  - column:Tuition + Program Fees: 64786 ⟵ “Tuition + Program Fees | $64,786 | $61,726”
  - on_campus:Nursing Credits: 56 ⟵ “Nursing Credits | 56 | 56”
  - on_campus:Tuition (entire nursing curriculum): 57630 ⟵ “Tuition (entire nursing curriculum) | $60,690 | $57,630”
  - on_campus:Tuition + Program Fees: 61726 ⟵ “Tuition + Program Fees | $64,786 | $61,726”
### `ad92ec2acf76840c` Notre Dame of Maryland University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://ndm.edu/about-us/business-office/tuition-fees/ (sha256 0007bfd735e2)
- issues: arrangement_unlabeled, conflicting_sources:https://absn.ndm.edu/admissions/tuition/,https://catalog.ndm.edu/tuition-and-fees-for-2026-2027,https://ndm.edu/about-us/business-office/tuition-fees/
- checks: {"columns": 2, "rows": 3}
  - column:Nursing Credits: 56 ⟵ “Nursing Credits | 56 | 56”
  - column:Tuition (entire nursing curriculum): 60690 ⟵ “Tuition (entire nursing curriculum) | $60,690 | $57,630”
  - column:Tuition + Program Fees: 64786 ⟵ “Tuition + Program Fees | $64,786 | $61,726”
  - on_campus:Nursing Credits: 56 ⟵ “Nursing Credits | 56 | 56”
  - on_campus:Tuition (entire nursing curriculum): 57630 ⟵ “Tuition (entire nursing curriculum) | $60,690 | $57,630”
  - on_campus:Tuition + Program Fees: 61726 ⟵ “Tuition + Program Fees | $64,786 | $61,726”
### `m6b2c606ad5bc4fc` Notre Dame of Maryland University — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://ndm.edu/admissions/undergraduate-studies/direct-entry-nursing-transfer-requirements/ (sha256 2de39c780c57)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “School of Nursing – Transfer Credit Statement Generally, college-level courses completed at regionally-accredited institutions will be evaluated and awarded transfer credit if approved, provided the course is similar in level, scope, content and expected learning outcomes to courses offered at Notre Dame of Maryland University School of Nursing and a grade of “C” or higher is earned.”
  - min_grade: C ⟵ “School of Nursing – Transfer Credit Statement Generally, college-level courses completed at regionally-accredited institutions will be evaluated and awarded transfer credit if approved, provided the course is similar in level, scope, content and expected learning outcomes to courses offered at Notre Dame of Maryland University School of Nursing and a grade of “C” or higher is earned.”
### `7f7ea3f7ba74161d` Salisbury University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.salisbury.edu/admissions/financial-aid/policies.aspx (sha256 f3cf6d5bc23b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Students and their families may face situations where the original application information does not accurately reflect their current circumstances and ability to pay for college.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family’s current income situation is significantly less than what is reflected in the financial information from the tax year reported on the FAFSA, please contact our office for more information concerning whether or not you may qualify for special circumstances consideration.”
### `a102a4ff557b3df4` Salisbury University — appeals 2018-19 [new] (labeled_in_source)
- source: https://www.salisbury.edu/admissions/financial-aid/faq-resources.aspx (sha256 a88b8ab569a6)
- issues: stale_year_label:2018-19, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you’re in that situation, here’s the process: When the FAFSA form asks you whether you are able to provide information about your parents, say no. (Note: This option is not available on the FAFSA PDF.) The next screen explains what's considered a special circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Click "NEXT" and then, on the following screen, select the option that says you don’t have a special circumstance but you still can't provide parent information.”
### `bd9562efd51e664a` Salisbury University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.salisbury.edu/admissions/financial-aid/policies.aspx (sha256 f3cf6d5bc23b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If you are placed on ‘probation’ at the end of the spring semester you will remain eligible to receive federal student aid, however if you do not make progress at the end of the summer term you will not be eligible for federal student aid in the Fall term pending any potential SAP appeal.”
  - sentence: sap_appeal ⟵ “The only way to regain aid eligibility without submitting a SAP appeal is by meeting the SAP criteria found in the link(s) below.”
### `2302af0c194e545e` Salisbury University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.salisbury.edu/administration/academic-affairs/registrar/transfer-credit/ (sha256 1efc41f30211)
- issues: rows_without_score, merged_score_cells
- checks: {"distinct_exams": 26, "equivalencies": 26, "rows_without_score": 1}
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50 67]:  ⟵ “Human Growth and Development | 50 67 | 4 4 | PSYC SSC PSYC 200 | PSYC SI PSYC 200”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50 67]:  ⟵ “Introductory Psychology | 50 67 | 4 4 | PSYC SSC PSYC 101 | PSYC SI PSYC 101”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | 4 | HIST ELE | HIST ELE”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | 4 | HIST ELE | HIST ELE”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 4 | ENGL ELE | ENGL ELE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50 67]:  ⟵ “Analyzing and Interpreting Literature | 50 67 | 4 4 | ENGL ELE GENE LIT | ENGL ELE GENE HE”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50 67]:  ⟵ “College Composition | 50 67 | 4 4 | ENGL ELE ENGL 103 | ENGL ELE ENGL 103”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 4 | ENGL ELE | ENGL ELE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 4 | ENGL ELE | ENGL ELE”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 4 | GENE HUM | GENE HIC”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 4 | BIOL 101 ** | BIOL 101 **”
  - equivalencies[CLEP-CALCULUS|50 67]:  ⟵ “Calculus | 50 67 | 3 4 | MATH 160 MATH 201 | MATH 160 MATH 201”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 4 | CHEM 121 | CHEM 121”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 4 | GENE MTH | GENE QA”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | GENE MTH | GENE QA”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | 3 | GENE SCN | GENE STS”
  - equivalencies[CLEP-PRECALCULUS|50 61]:  ⟵ “Precalculus | 50 61 | 3 3 | MATH MTH MATH 135 | MATH QA MATH 135”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50 60]:  ⟵ “Financial Accounting | 50 60 | 3 3 | ACCT ELE ACCT 201 | ACCT ELE ACCT 201”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | 4 | COSC 116 | COSC 116”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | ACCT 248 | ACCT 248”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 | MGMT 320 | MGMT 320”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 3 | MKTG 330 | MKTG 330”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50 62]:  ⟵ “French Languages: Levels 1 and 2 | 50 62 | 4 4 4 | FREN 102 FREN 201 FREN 202 | FREN 102 FREN 201 FREN 202”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50 62]:  ⟵ “German Language: Levels 1 and 2 | 50 62 | 4 4 4 | GERM 102 GERM 201 GERM 202 | GERM 102 GERM 201 GERM 202”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50 62]:  ⟵ “Spanish Language: Levels 1 and 2 | 50 62 | 4 4 4 | SPAN 102 SPAN 201 SPAN 202 | SPAN 102 SPAN 201 SPAN 202”
  - … 1 more rows
### `3d96ba86654ae54b` Salisbury University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.salisbury.edu/admissions/first-year-students/credit-by-exam.aspx (sha256 098c7026d5ea)
- issues: rows_without_score, credits_implausible, conflicting_sources:https://www.salisbury.edu/administration/academic-affairs/registrar/transfer-credit/
- checks: {"distinct_exams": 18, "equivalencies": 22, "rows_without_score": 22}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology (IB score 4) | 44 | BIOL 101BIOL ELE”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology (IB score 5, 6, or 7) | 44 | BIOL 101BIOL SCL”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business and Management | 4 | BUAD 103”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | 44 | CHEM 121CHEM 122”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | 44 | COSC 116COSC ELE”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | 33 | ECON 211ECON 212”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|None]:  ⟵ “Environmental Systems | 3 | ENVH 110”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French A | 44 | FREN 101FREN 102”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French B | 44 | FREN 201FREN 202”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German A | 44 | GERM 101GERM 102”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German B | 44 | GERM 201GERM 202”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | 33 | GEOG 100GEOG ELE”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History of Americas | 4 | HIST HST**”
  - equivalencies[IB-LATIN|None]:  ⟵ “Latin | 44 | LATN 101LATN 102”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | 4 | MUSC HUM”
  - equivalencies[IB-PHILOSOPHY|None]:  ⟵ “Philosophy | 44 | PHIL 101PHIL ELE”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Physics | 44 | PHYS 121PHYS 123”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | 44 | PSYC 101PSYC ELE”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|None]:  ⟵ “Social Anthropology | 4 | ANTH 212”
  - equivalencies[IB-SPANISH|None]:  ⟵ “Spanish A | 44 | SPAN 101SPAN 102”
  - equivalencies[IB-SPANISH|None]:  ⟵ “Spanish B | 44 | SPAN 201SPAN 202”
  - equivalencies[IB-THEATRE|None]:  ⟵ “Theatre Arts | 44 | THEA 100THEA ELE”
### `97e48748e52566ee` Salisbury University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.salisbury.edu/administration/academic-affairs/registrar/transfer-credit/ (sha256 1efc41f30211)
- issues: conflicting_sources:https://www.salisbury.edu/admissions/first-year-students/credit-by-exam.aspx
- checks: {"distinct_exams": 18, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIOL SCL | BIOL HOS”
  - equivalencies[IB-BUSINESS-MANAGEMENT|3]:  ⟵ “Business Management | 3 | 4 | BUAD ELE | BUAD ELE”
  - equivalencies[IB-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHEM SCL | CHEM HOS”
  - equivalencies[IB-COMPUTER-SCIENCE|3]:  ⟵ “Computer Science | 3 | 4 | COSC SCN | COSC STS”
  - equivalencies[IB-ECONOMICS|3]:  ⟵ “Economics | 3 | 3 | ECON SSC | ECON ELE”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|3]:  ⟵ “Environmental Systems | 3 | 4 | ENVH ELE | ENVH ELE”
  - equivalencies[IB-FRENCH|3]:  ⟵ “French A | 3 | 4 | FREN 101 | FREN 101”
  - equivalencies[IB-FRENCH|3]:  ⟵ “French B | 3 | 4 | FREN 201 | FREN 201”
  - equivalencies[IB-GERMAN|3]:  ⟵ “German A | 3 | 4 | GERM 101 | GERM 101”
  - equivalencies[IB-GERMAN|3]:  ⟵ “German B | 3 | 4 | GERM 201 | GERM 201”
  - equivalencies[IB-GEOGRAPHY|3]:  ⟵ “Geography | 3 | 4 | GEOG SSC | GEOG SI”
  - equivalencies[IB-HISTORY|3]:  ⟵ “History of Americas | 3 | 4 | HIST ELE | HIST ELE”
  - equivalencies[IB-LATIN|3]:  ⟵ “Latin | 3 | 4 | LATN 101 | LATN 101”
  - equivalencies[IB-MUSIC|3]:  ⟵ “Music | 3 | 4 | MUSC ELE | MUSC ELE”
  - equivalencies[IB-PHILOSOPHY|3]:  ⟵ “Philosophy | 3 | 4 | PHIL HUM | PHIL ELE”
  - equivalencies[IB-PHYSICS|3]:  ⟵ “Physics | 3 | 4 | PHYS SCL | PHYS HOS”
  - equivalencies[IB-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | 4 | PSYC SSC | PSYC ELE”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|3]:  ⟵ “Social Anthropology | 3 | 4 | ANTH SSC | ANTH ELE”
  - equivalencies[IB-SPANISH|3]:  ⟵ “Spanish A | 3 | 4 | SPAN 101 | SPAN 101”
  - equivalencies[IB-SPANISH|3]:  ⟵ “Spanish B | 3 | 4 | SPAN 201 | SPAN 201”
  - equivalencies[IB-THEATRE|3]:  ⟵ “Theatre Arts | 3 | 4 | THEA HUM | THEA HE”
### `e8becbde9f6a7b81` St. Mary's College of Maryland — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smcm.edu/student-financial-assistance/tuition-fees/ (sha256 5b441b6beb3e)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:St. Mary’s Grant: 3000.0 ⟵ “St. Mary’s Grant | $3,000.00”
  - on_campus:Excellence Scholarship: 5000.0 ⟵ “Excellence Scholarship | $5,000.00”
  - on_campus:DC Tuition Assistance Grant (DCTAG): 15000.0 ⟵ “DC Tuition Assistance Grant (DCTAG) | $15,000.00”
  - on_campus:Direct Subsidized Loan: 3500.0 ⟵ “Direct Subsidized Loan | $3,500.00”
  - on_campus:Direct Unsubsidized Loan: 2000.0 ⟵ “Direct Unsubsidized Loan | $2,000.00”
  - on_campus:Direct PLUS Loan*: 18120.0 ⟵ “Direct PLUS Loan* | $18,120.00”
  - on_campus:TOTAL Amount Awarded: 46620.0 ⟵ “TOTAL Amount Awarded | $46,620.00”
### `c04940755ef90752` St. Mary's College of Maryland — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.smcm.edu/registrar/academic-records/transfer-of-credit/ (sha256 e529446104ba)
- issues: rows_without_score
- checks: {"distinct_exams": 41, "equivalencies": 41, "rows_without_score": 41}
  - equivalencies[AP-2-D-ART-DESIGN|None]:  ⟵ “AP 2-D Art and Design | ART 205 | LEAD Arts | ”
  - equivalencies[AP-3-D-ART-DESIGN|None]:  ⟵ “AP 3-D Art and Design | ART 205 | LEAD Arts | ”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “AP African American Studies | AADS Lower Division Elective | Does not fulfill LEAD Breadth Requirement | ”
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “AP Art History | ARTH 250 | LEAD Humanities | ”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “AP Biology | BIOL 101 | LEAD Natural Science with Lab | ”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|None]:  ⟵ “AP Business with Personal Finance | BADM-101 | Does not fulfill LEAD Breadth Requirement | ”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “AP Calculus AB | MATH 151 | LEAD Mathematics | ”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “AP Calculus BC | MATH 152 ***Update Note If a student scores a 3, 4, or 5 on the BC part of exam, receive credit for MATH-152. If less than a 3, but 3-5 on the AB subscore, get MATH-151. They DO NOT GET BOTH. | LEAD Mathematics | ”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “AP Chemistry | CHEM 103 | Does not fulfill LEAD Breadth Requirement | ”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “AP Chinese Language and Culture | ILCC 102 | Language Study or LEAD Cultural Literacy | ”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|None]:  ⟵ “AP Comparative Government and Politics | POSC Lower Level Elective | Does not fulfill LEAD Breadth Requirement | ”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “AP Computer Science A | COSC 120 | LEAD Mathematics | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “AP Computer Science Principles | COSC Lower Division Elective | Does not fulfill LEAD Breadth Requirement | ”
  - equivalencies[AP-CYBERSECURITY|None]:  ⟵ “AP Cybersecurity | COSC Lower Division Elective | Does not fulfill LEAD Breadth Requirement | ”
  - equivalencies[AP-DRAWING|None]:  ⟵ “AP Drawing | ART 204 | LEAD Arts | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “AP English Language & Composition | ENGL 102 | Does not fulfill LEAD Breadth Requirement | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “AP English Literature & Composition | ENGL 106 | LEAD Humanities | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “AP Environmental Science | ENST 250 | LEAD Natural Science with Lab | ”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “AP European History | HIST 105 | LEAD Humanities | ”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “AP French Language and Culture | ILCF 102 | Language Study or LEAD Cultural Literacy | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “AP German Language and Culture | LNGU 102 | Language Study or LEAD Cultural Literacy | ”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “AP Human Geography | College Lower Level Elective | Does not fulfill LEAD Breadth Requirement | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “AP Italian Language and Culture | LNGU 102 | Language Study or LEAD Cultural Literacy | ”
  - equivalencies[AP-LATIN|None]:  ⟵ “AP Latin | LNGU 102 | Language Study or LEAD Cultural Literacy | ”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “AP Macroeconomics | ECON 103 | LEAD Social and Behavioral Sciences | ”
  - … 16 more rows
### `00fe511350db3d83` Stevenson University — appeals 2017-18 [new] (labeled_in_source)
- source: https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/apply-for-aid/ (sha256 eda3ca3a1ac0)
- issues: stale_year_label:2017-18, semantic_review_required, conflicting_sources:https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/apply-for-aid/?tab=step-2,https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/faq/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you or your family have unusual circumstances that might affect your need for student aid, submit the Special Conditions form to the Financial Aid Office for consideration.”
### `2dfc5b4ae08decb0` Stevenson University — appeals 2017-18 [new] (labeled_in_source)
- source: https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/apply-for-aid/?tab=step-2 (sha256 77a1322191bb)
- issues: stale_year_label:2017-18, semantic_review_required, conflicting_sources:https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/apply-for-aid/,https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/faq/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you or your family have unusual circumstances that might affect your need for student aid, submit the Special Conditions form to the Financial Aid Office for consideration.”
### `3e4bce0c896721ef` Stevenson University — appeals 2026-27 [new] (labeled_in_url)
- source: https://www.stevenson.edu/wp-content/uploads/2026-2027-SAP-Appeal-Form-Fall-1.pdf (sha256 7259312e9a7e)
- issues: semantic_review_required, conflicting_sources:https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/forms/,https://www.stevenson.edu/wp-content/uploads/FA-SAP-Policy-Undergraduate-FINAL-AUGUST-2024.pdf,https://www.stevenson.edu/wp-content/uploads/SAP-Appeal-Form-25-26-1.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Form Student Name: Type Name Here Student ID #:Type ID here We understand that unexpected events can impact a student’s studies.”
  - sentence: sap_appeal ⟵ “For students who lost financial aid eligibility due to not meeting the Satisfactory Academic Progress requirements have the right to appeal.”
  - sentence: sap_appeal ⟵ “Student Signature: ____________________________________________________ Date: _____________________ SAP Appeal Form Office of Financial Aid Rev. 05/18/2026, Page 2”
### `41350f928043d230` Stevenson University — appeals 2017-18 [new] (labeled_in_source)
- source: https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/faq/ (sha256 24eef8329b79)
- issues: stale_year_label:2017-18, semantic_review_required, conflicting_sources:https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/apply-for-aid/,https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/apply-for-aid/?tab=step-2
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you or your family have unusual circumstances that might affect your need for student aid, submit a Special Conditions Form to the Financial Aid Office for consideration.”
### `42d9ea626292a27a` Stevenson University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.stevenson.edu/admissions-aid/tuition-fees/ (sha256 4358b9864b3f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Students who incur costs for eligible study abroad programs, disability-related expenses, dependent care or cooperative education costs, may request a cost of attendance adjustment by contacting the Office of Financial Aid.”
### `8790601e079ae61a` Stevenson University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/forms/ (sha256 91580eb57b2a)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.stevenson.edu/wp-content/uploads/2026-2027-SAP-Appeal-Form-Fall-1.pdf,https://www.stevenson.edu/wp-content/uploads/FA-SAP-Policy-Undergraduate-FINAL-AUGUST-2024.pdf,https://www.stevenson.edu/wp-content/uploads/SAP-Appeal-Form-25-26-1.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “This is not to be used for SAP appeals, professional judgment, Academic reinstatement, or any other appeals.”
  - sentence: sap_appeal ⟵ “Stevenson Aid Appeal Form (New Freshman) Stevenson Aid Appeal Form (Transfers) Stevenson Aid Appeal Form (Returning Students) Asset Information Worksheet Dependency Override Dependency Override Renewal Form Dependent Household Worksheet Independent Household Worksheet Identity Statement of Education Purpose Non-Tax Filer Form Satisfactory Academic Progress (SAP) Appeal Form Special Conditions Form”
  - sentence: sap_appeal ⟵ “This is not to be used for SAP appeals, professional judgment, Academic reinstatement, or any other appeals.”
  - sentence: sap_appeal ⟵ “Stevenson Aid Appeal Form (New Freshman) Stevenson Aid Appeal Form (Transfers) Stevenson Aid Appeal Form (Returning Students) Asset Information Form Dependency Override Form Dependency Override Renewal Form Dependent Verification Form Independent Verification Form Satisfactory Academic Progress (SAP) Appeal Form Special Conditions Form Tax Information Request Instructions Unaccompanied Homeless Yo”
### `98e2ba567f714e54` Stevenson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stevenson.edu/wp-content/uploads/SAP-Appeal-Form-25-26-1.pdf (sha256 b1712c7983e8)
- issues: semantic_review_required, conflicting_sources:https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/forms/,https://www.stevenson.edu/wp-content/uploads/2026-2027-SAP-Appeal-Form-Fall-1.pdf,https://www.stevenson.edu/wp-content/uploads/FA-SAP-Policy-Undergraduate-FINAL-AUGUST-2024.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Form Student Name: Type Name Here Student ID #:Type ID here We understand that unexpected events can impact a student’s studies.”
  - sentence: sap_appeal ⟵ “For students who lost financial aid eligibility due to not meeting the Satisfactory Academic Progress requirements have the right to appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeal Form Office of Financial Aid Rev. 05/15/2025, Page 2 SAP Appeal Form Office of Financial Aid Rev. 05/15/2025, Page 3”
### `d94c2e244ddb1154` Stevenson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stevenson.edu/wp-content/uploads/FA-SAP-Policy-Undergraduate-FINAL-AUGUST-2024.pdf (sha256 1ef9e663c297)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If extenuating circumstances exist and the student would like to appeal the loss of a State grant or scholarship, they must do so directly to the OSFA at MHEC.”
### `ef57a08bf3ae74dd` Stevenson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stevenson.edu/wp-content/uploads/FA-SAP-Policy-Undergraduate-FINAL-AUGUST-2024.pdf (sha256 1ef9e663c297)
- issues: semantic_review_required, conflicting_sources:https://www.stevenson.edu/admissions-aid/scholarships-financial-aid/forms/,https://www.stevenson.edu/wp-content/uploads/2026-2027-SAP-Appeal-Form-Fall-1.pdf,https://www.stevenson.edu/wp-content/uploads/SAP-Appeal-Form-25-26-1.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The student must submit an SAP Appeal Form in writing to the Financial Aid Appeals Committee.”
### `81a964eca9c9eec1` Stevenson University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stevenson.edu/admissions-aid/tuition-fees/ (sha256 4358b9864b3f)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - on_campus:Tuition: 38970 ⟵ “Tuition | $19,485 | $38,970”
  - on_campus:Fees: General Services, Student Activities, Technology: 2856 ⟵ “Fees: General Services, Student Activities, Technology | $1,428 | $2,856”
  - on_campus:Accident Insurance (prices subject to change): 85 ⟵ “Accident Insurance (prices subject to change) | $85 | $85”
  - on_campus:Room – SU Suite (Double): 9896 ⟵ “Room – SU Suite (Double) | $4,948 | $9,896”
  - on_campus:Meal Plan A Block: 6032 ⟵ “Meal Plan A Block | $3,016 | $6,032”
  - on_campus:TOTAL: 57824 ⟵ “TOTAL | $28,947 | $57,824”
### `7f19487f186bfcbb` Stevenson University — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_url)
- source: https://www.stevenson.edu/wp-content/uploads/AP-Course-Equivs_2025_2026.pdf (sha256 48223c17adea)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 26, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “ART History                                     3, 4, 5            3                                   ART 106”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art: Drawing                             3, 4, 5            3                                   ART 116”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Studio Art: 2D Design                           3, 4, 5            3     ART 110 or PHOTO 141 based on consultation with department chair”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Studio Art: 3D Design                           3, 4, 5            3                                   ART 113”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition                  3, 4, 5            3                                 ENG 151”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition                3, 4, 5            3                                 ENG 152”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research                                     3, 4, 5            3                             General Elective”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar                                      3, 4, 5            3                                INDSC 199”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                                  3, 4, 5            3                                   EC 201”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                                  3, 4, 5            3                                   EC 202”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “AP European History                              3, 4              3                                  HIST 211”
  - equivalencies[AP-EUROPEAN-HISTORY|5]:  ⟵ “AP European History                                5               6                       History Elective and HIST 211”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                      3, 4, 5            3                                  PSY 101”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                        3               4                                MATH 147”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB                                      4, 5              4                                MATH 220”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                                        3               4                                MATH 220”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles                     3, 4, 5            3                       Information Systems Elective”
  - equivalencies[AP-STATISTICS|4]:  ⟵ “Statistics                                      3, 4, 5            4                                MATH 136”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                           3                4                               BIO 104”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                         3                3                         Chemistry Elective”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                             3                3                              ENV 150”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                            4, 5              3                              ENV 275”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “AP Physics 1: Algebra Based                       3                3                      Physics Elective (non-lab)”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “AP Physics 1: Algebra Based                                             4, 5            4             PHYS 210”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “AP Physics 2: Algebra Based                                              3              3       Physics Elective (lab)”
  - … 14 more rows
### `966f2b873f5ce34d` Stevenson University — credit_policies 2025-26 · policy_kind=CLEP [new] (labeled_in_title)
- source: https://www.stevenson.edu/wp-content/uploads/CLEP-Equivalences_2025_2026.pdf (sha256 03f519c06268)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 24, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting                    50                      3          ACC 140 or ACC 215”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems                     50                      3                  IS 199”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law               50                      3                LAW 208”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management                50                      3                MGT 204”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing                 50                      3                MKT 206”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development            50                      3                 PSY 108”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                             50                      3                MATH 147”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                     50                      3                ENG 281”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                      50                      3                ENG 281”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II:        50                      3                HIST 110”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                              50                      3               HUM 199TR”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                                        50                            11            See Below*”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                                       50                             4            MATH 220”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                                                      50                             3           CHEM 198TR”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                                                50                             4            MATH 137”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics                                            50                             3            MATH 135”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences                                               50                             3            PHYS 198TR”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                                            50                             3            POSCI 102”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                                        50                             3              PSY 101”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                                         50                             3             SOC 101”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                                   50                             3              EC 201”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                                   50                             3              EC 202”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature                          50                             3             ENG 152”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                                            50                             3             ENG 151”
### `1305dc4efc92e5cb` Towson University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.towson.edu/admissions/financialaid/forms/2026-forms.html (sha256 f35b5d6fc165)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Nancy Grasmick Leadership Institute Sponsorship & Advertising Opportunities Hiring TU Students Visit TUApply NowRequest Information Give to TU Calendars & Events Directories HomeAdmissions & AidFinancial AidForms & Online Services2025-2026 Forms 2025-2026 Forms Sub-menu Forms & Online Services 2026-2027 Forms 2025-2026 Forms FAFSA Verification Identity Verification Satisfactory Academic Progress (”
### `209384993fc59530` Towson University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.towson.edu/admissions/financialaid/forms/sap-appeal.html (sha256 0eda38679b1d)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.towson.edu/admissions/financialaid/forms/,https://www.towson.edu/admissions/financialaid/forms/2027-forms.html,https://www.towson.edu/admissions/financialaid/guide/requirements/sap.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “To appeal to continue receiving aid for additional terms, suspended students must submit this Online SAP Appeal Form.”
### `788927149973648f` Towson University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.towson.edu/admissions/financialaid/forms/ (sha256 4f05b090c7da)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.towson.edu/admissions/financialaid/forms/2027-forms.html,https://www.towson.edu/admissions/financialaid/forms/sap-appeal.html,https://www.towson.edu/admissions/financialaid/guide/requirements/sap.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Nancy Grasmick Leadership Institute Sponsorship & Advertising Opportunities Hiring TU Students Visit TUApply NowRequest Information Give to TU Calendars & Events Directories HomeAdmissions & AidFinancial AidForms & Online Services Forms & Online Services Sub-menu Forms & Online Services 2026-2027 Forms 2025-2026 Forms FAFSA Verification Identity Verification Satisfactory Academic Progress (SAP) Ap”
### `a082a0153fa25b28` Towson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.towson.edu/admissions/financialaid/guide/requirements/sap.html (sha256 b9b9a248e7af)
- issues: semantic_review_required, conflicting_sources:https://www.towson.edu/admissions/financialaid/forms/,https://www.towson.edu/admissions/financialaid/forms/2027-forms.html,https://www.towson.edu/admissions/financialaid/forms/sap-appeal.html
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal Process Suspended students may appeal to request aid for additional terms.”
  - sentence: sap_appeal ⟵ “If you have received a financial aid SAP suspension notice from the TU Financial Aid Office, to appeal your suspension, you must use this Online SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “Denied SAP Appeals If your appeal is denied, you will remain permanently ineligible for financial aid at TU unless you continue to attend TU without aid and improve your overall record enough to meet all the required cumulative SAP standards.”
### `a67c9a2461dae2b4` Towson University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.towson.edu/admissions/financialaid/forms/2027-forms.html (sha256 fc97cb2aad0c)
- issues: semantic_review_required, conflicting_sources:https://www.towson.edu/admissions/financialaid/forms/,https://www.towson.edu/admissions/financialaid/forms/sap-appeal.html,https://www.towson.edu/admissions/financialaid/guide/requirements/sap.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Nancy Grasmick Leadership Institute Sponsorship & Advertising Opportunities Hiring TU Students Visit TUApply NowRequest Information Give to TU Calendars & Events Directories HomeAdmissions & AidFinancial AidForms & Online Services2026-2027 Forms 2026-2027 Forms Sub-menu Forms & Online Services 2026-2027 Forms 2025-2026 Forms FAFSA Verification Identity Verification Satisfactory Academic Progress (”
### `b25f1ff63330dda2` Towson University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.towson.edu/admissions/financialaid/forms/documents/2627depappealr.pdf (sha256 cc3646c774cc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you can answer yes to question 7 about Unusual Circumstances, the online form won’t require your parent’s data, and they will forward your request for independent status to us for our review and approval.”
### `5b5f5a8c5174ab1d` Towson University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/financialaid/forms/documents/priorcoa.pdf (sha256 7fb8a0f0be3c)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 52}
  - column:Total Units Count: 24 ⟵ “Total Units Count | 24 | 18 | 12”
  - column:Tuition & Fees: 12186 ⟵ “Tuition & Fees | 12,186 | 9,342 | 6,228”
  - column:Room & Board: 16666 ⟵ “Room & Board | 16,666 | 16,666 | 16,666”
  - column:Books: 960 ⟵ “Books | 960 | 720 | 480”
  - column:Personal: 970 ⟵ “Personal | 970 | 970 | 970”
  - column:Transportation: 2460 ⟵ “Transportation | 2,460 | 2,460 | 2,460”
  - column:Loan Fees: 280 ⟵ “Loan Fees | 280 | 280 | 280”
  - column:Total: 33522 ⟵ “Total | 33,522 | 30,438 | 27,084”
  - column:Tuition & Fees (2): 31332 ⟵ “Tuition & Fees | 31,332 | 23,724 | 15,816”
  - column:Room & Board (2): 16666 ⟵ “Room & Board | 16,666 | 16,666 | 16,666”
  - column:Books (2): 960 ⟵ “Books | 960 | 720 | 480”
  - column:Personal (2): 970 ⟵ “Personal | 970 | 970 | 970”
  - column:Transportation (2): 2460 ⟵ “Transportation | 2,460 | 2,460 | 2,460”
  - column:Loan Fees (2): 280 ⟵ “Loan Fees | 280 | 280 | 280”
  - column:Total (2): 52668 ⟵ “Total | 52,668 | 44,820 | 36,672”
  - column:Tuition & Fees (3): 12186 ⟵ “Tuition & Fees | 12,186 | 9,342 | 6,228”
  - column:Room & Board (3): 3170 ⟵ “Room & Board | 3,170 | 3,170 | 3,170”
  - column:Books (3): 960 ⟵ “Books | 960 | 720 | 480”
  - column:Personal (3): 970 ⟵ “Personal | 970 | 970 | 970”
  - column:Transportation (3): 2460 ⟵ “Transportation | 2,460 | 2,460 | 2,460”
  - column:Loan Fees (3): 280 ⟵ “Loan Fees | 280 | 280 | 280”
  - column:Total (3): 20026 ⟵ “Total | 20,026 | 16,942 | 13,588”
  - column:Total Units Count (2): 18 ⟵ “Total Units Count | 18 | 12”
  - column:Tuition & Fees (4): 13302 ⟵ “Tuition & Fees | 13,302 | 8,868”
  - column:Books (4): 720 ⟵ “Books | 720 | 480”
  - … 101 more rows
### `6352d97c6242e573` Towson University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/tuition/cost.html (sha256 8053b6bc11a1)
- issues: arrangement_unlabeled, conflicting_sources:https://www.towson.edu/admissions/tuition/,https://www.towson.edu/student-university-billing/tuition/projected.html
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 12690 ⟵ “Tuition and Fees | $12,690 | $32,948 | $12,690 | $32,948”
  - column:Housing and Food Allowance: 16366 ⟵ “Housing and Food Allowance | $16,366 | $16,366 | $3,182 | $3,182”
  - column:Books and Supplies: 960 ⟵ “Books and Supplies | $ 960 | $ 960 | $ 960 | $ 960”
  - column:Transportation Expenses: 2534 ⟵ “Transportation Expenses | $ 2,534 | $ 2,534 | $2,534 | $2,534”
  - column:Personal Expenses: 970 ⟵ “Personal Expenses | $ 970 | $ 970 | $ 970 | $ 970”
  - column:Loan Fees Allowance: 262 ⟵ “Loan Fees Allowance | $ 262 | $ 262 | $ 262 | $ 262”
  - column:Total: 33782 ⟵ “Total | $ 33,782 | $54,040 | $20,598 | $40,856”
  - with_parents_or_family:Tuition and Fees: 12690 ⟵ “Tuition and Fees | $12,690 | $32,948 | $12,690 | $32,948”
  - with_parents_or_family:Housing and Food Allowance: 3182 ⟵ “Housing and Food Allowance | $16,366 | $16,366 | $3,182 | $3,182”
  - with_parents_or_family:Books and Supplies: 960 ⟵ “Books and Supplies | $ 960 | $ 960 | $ 960 | $ 960”
  - with_parents_or_family:Transportation Expenses: 2534 ⟵ “Transportation Expenses | $ 2,534 | $ 2,534 | $2,534 | $2,534”
  - with_parents_or_family:Personal Expenses: 970 ⟵ “Personal Expenses | $ 970 | $ 970 | $ 970 | $ 970”
  - with_parents_or_family:Loan Fees Allowance: 262 ⟵ “Loan Fees Allowance | $ 262 | $ 262 | $ 262 | $ 262”
  - with_parents_or_family:Total: 20598 ⟵ “Total | $ 33,782 | $54,040 | $20,598 | $40,856”
### `65863b19c1ea971e` Towson University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/tuition/cost.html (sha256 8053b6bc11a1)
- issues: arrangement_unlabeled, conflicting_sources:https://www.towson.edu/admissions/tuition/,https://www.towson.edu/student-university-billing/tuition/projected.html
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 32948 ⟵ “Tuition and Fees | $12,690 | $32,948 | $12,690 | $32,948”
  - column:Housing and Food Allowance: 16366 ⟵ “Housing and Food Allowance | $16,366 | $16,366 | $3,182 | $3,182”
  - column:Books and Supplies: 960 ⟵ “Books and Supplies | $ 960 | $ 960 | $ 960 | $ 960”
  - column:Transportation Expenses: 2534 ⟵ “Transportation Expenses | $ 2,534 | $ 2,534 | $2,534 | $2,534”
  - column:Personal Expenses: 970 ⟵ “Personal Expenses | $ 970 | $ 970 | $ 970 | $ 970”
  - column:Loan Fees Allowance: 262 ⟵ “Loan Fees Allowance | $ 262 | $ 262 | $ 262 | $ 262”
  - column:Total: 54040 ⟵ “Total | $ 33,782 | $54,040 | $20,598 | $40,856”
  - with_parents_or_family:Tuition and Fees: 32948 ⟵ “Tuition and Fees | $12,690 | $32,948 | $12,690 | $32,948”
  - with_parents_or_family:Housing and Food Allowance: 3182 ⟵ “Housing and Food Allowance | $16,366 | $16,366 | $3,182 | $3,182”
  - with_parents_or_family:Books and Supplies: 960 ⟵ “Books and Supplies | $ 960 | $ 960 | $ 960 | $ 960”
  - with_parents_or_family:Transportation Expenses: 2534 ⟵ “Transportation Expenses | $ 2,534 | $ 2,534 | $2,534 | $2,534”
  - with_parents_or_family:Personal Expenses: 970 ⟵ “Personal Expenses | $ 970 | $ 970 | $ 970 | $ 970”
  - with_parents_or_family:Loan Fees Allowance: 262 ⟵ “Loan Fees Allowance | $ 262 | $ 262 | $ 262 | $ 262”
  - with_parents_or_family:Total: 40856 ⟵ “Total | $ 33,782 | $54,040 | $20,598 | $40,856”
### `85c873d8344d4339` Towson University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/tuition/ (sha256 ae050a6a1042)
- issues: conflicting_sources:https://www.towson.edu/admissions/tuition/cost.html,https://www.towson.edu/student-university-billing/tuition/projected.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Full-time Tuition and Fees (12-15 units/term): 32948 ⟵ “Full-time Tuition and Fees (12-15 units/term) | $12,690 | $32,948”
  - column:Premium On-Campus Housing: 10076 ⟵ “Premium On-Campus Housing | $10,076 | $10,076”
  - column:Silver Dining Plan Cost: 6290 ⟵ “Silver Dining Plan Cost | $ 6,290 | $ 6,290”
  - column:Total Estimated TU Costs: 49314 ⟵ “Total Estimated TU Costs | $29,056 | $49,314”
### `90a29ce031654bdb` Towson University — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.towson.edu/student-university-billing/tuition/projected.html (sha256 8f7d11a6ea39)
- issues: arrangement_unlabeled, cost_period_semester, conflicting_sources:https://www.towson.edu/admissions/tuition/,https://www.towson.edu/admissions/tuition/cost.html
- checks: {"columns": 4, "rows": 4}
  - column:Tuition and Mandatory Fees¹: 15666 ⟵ “Tuition and Mandatory Fees¹ | $15,666 | $16,465 | $17,305 | $18,188”
  - column:Housing (multiple occupancy): 4336 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3455 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 23457 ⟵ “Total³ (student residing on campus) | $23,457 | $24,567 | $25,732 | $26,905”
  - column:Tuition and Mandatory Fees¹: 16465 ⟵ “Tuition and Mandatory Fees¹ | $15,666 | $16,465 | $17,305 | $18,188”
  - column:Housing (multiple occupancy): 4509 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3593 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 24567 ⟵ “Total³ (student residing on campus) | $23,457 | $24,567 | $25,732 | $26,905”
  - column:Tuition and Mandatory Fees¹: 17305 ⟵ “Tuition and Mandatory Fees¹ | $15,666 | $16,465 | $17,305 | $18,188”
  - column:Housing (multiple occupancy): 4690 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3737 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 25732 ⟵ “Total³ (student residing on campus) | $23,457 | $24,567 | $25,732 | $26,905”
  - column:Tuition and Mandatory Fees¹: 18188 ⟵ “Tuition and Mandatory Fees¹ | $15,666 | $16,465 | $17,305 | $18,188”
  - column:Housing (multiple occupancy): 4831 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3886 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 26905 ⟵ “Total³ (student residing on campus) | $23,457 | $24,567 | $25,732 | $26,905”
### `be74237f9dd7ee46` Towson University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.towson.edu/student-university-billing/tuition/projected.html (sha256 8f7d11a6ea39)
- issues: arrangement_unlabeled, cost_period_semester, conflicting_sources:https://www.towson.edu/admissions/tuition/,https://www.towson.edu/admissions/tuition/cost.html
- checks: {"columns": 4, "rows": 4}
  - column:Tuition and Mandatory Fees¹: 6092 ⟵ “Tuition and Mandatory Fees¹ | $6,092 | $6,276 | $6,483 | $6,697”
  - column:Housing (multiple occupancy): 4336 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3455 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 14426 ⟵ “Total³ (student residing on campus) | $14,426 | $14,378 | $14,910 | $15,414”
  - column:Tuition and Mandatory Fees¹: 6276 ⟵ “Tuition and Mandatory Fees¹ | $6,092 | $6,276 | $6,483 | $6,697”
  - column:Housing (multiple occupancy): 4509 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3593 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 14378 ⟵ “Total³ (student residing on campus) | $14,426 | $14,378 | $14,910 | $15,414”
  - column:Tuition and Mandatory Fees¹: 6483 ⟵ “Tuition and Mandatory Fees¹ | $6,092 | $6,276 | $6,483 | $6,697”
  - column:Housing (multiple occupancy): 4690 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3737 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 14910 ⟵ “Total³ (student residing on campus) | $14,426 | $14,378 | $14,910 | $15,414”
  - column:Tuition and Mandatory Fees¹: 6697 ⟵ “Tuition and Mandatory Fees¹ | $6,092 | $6,276 | $6,483 | $6,697”
  - column:Housing (multiple occupancy): 4831 ⟵ “Housing (multiple occupancy) | $4,336 | $4,509 | $4,690 | $4,831”
  - column:All Access Gold Plan²: 3886 ⟵ “All Access Gold Plan² | $3,455 | $3,593 | $3,737 | $3,886”
  - column:Total³ (student residing on campus): 15414 ⟵ “Total³ (student residing on campus) | $14,426 | $14,378 | $14,910 | $15,414”
### `f00ee4562a5938ed` Towson University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.towson.edu/admissions/tuition/ (sha256 ae050a6a1042)
- issues: conflicting_sources:https://www.towson.edu/admissions/tuition/cost.html,https://www.towson.edu/student-university-billing/tuition/projected.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Full-time Tuition and Fees (12-15 units/term): 12690 ⟵ “Full-time Tuition and Fees (12-15 units/term) | $12,690 | $32,948”
  - on_campus:Premium On-Campus Housing: 10076 ⟵ “Premium On-Campus Housing | $10,076 | $10,076”
  - on_campus:Silver Dining Plan Cost: 6290 ⟵ “Silver Dining Plan Cost | $ 6,290 | $ 6,290”
  - on_campus:Total Estimated TU Costs: 29056 ⟵ “Total Estimated TU Costs | $29,056 | $49,314”
### `1afe41f2de2e7f2f` University of Baltimore — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/policies/special-circumstances.cfm (sha256 73b31f5f0c68)
- issues: semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm,https://www.ubalt.edu/admission-and-aid/financial-aid/policies/cost-of-attendance.cfm,https://www.ubalt.edu/admission-and-aid/financial-aid/policies/dependency_appeals.cfm
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Below are examples of special circumstances that may be considered: Loss or significant reduction of employment, wages, or unemployment compensation Loss of benefits (e.g.”
  - sentence: need_based_special_circumstances ⟵ “Social Security benefits or child support) Widowed, separated or divorced since filing the FAFSA If a student has circumstances for our office to consider, submit the completed Special Circumstance Form with all required documentation.”
  - sentence: need_based_special_circumstances ⟵ “If a student is in one of the situations below, completing the Special Circumstance process will not result in an increase in financial aid eligibility: Student Aid Index (SAI) is already '0' or lower.”
### `222c7ef9da79b826` University of Baltimore — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/policies/sap.cfm (sha256 7e9ec83dafc9)
- issues: semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Only ONE SAP appeal per SEMESTER will be reviewed.”
  - sentence: sap_appeal ⟵ “Students can appeal their Not Meets status by completing a Satisfactory Academic Progress Appeal.”
### `3d862593294658bc` University of Baltimore — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm (sha256 13b3810be9c2)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/policies/dependency_appeals.cfm
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “With this option your inter-institutional registration will count towards your loan enrollment requirement for your student loans. ***Please submit only clear copies of documentation to the Office of Financial Aid; any unclear or unreadable copies will be returned*** Back to Top Dependency Override The federal government believes that students and their parents have the primary responsibility to p”
  - sentence: dependency_override ⟵ “These practices may include making dependency overrides in situations when a student’s parent cannot be located or where an otherwise dependent student has been a victim of domestic violence and is no longer residing with his/her parents.”
  - sentence: dependency_override ⟵ “A dependency override can be made only to change a student’s status from dependent to independent.”
  - sentence: dependency_override ⟵ “Students who wish to apply for a Dependency Override must submit the following documentation: 2025-2026 2025-2026 Dependency Appeal Form 2026-2027 2026-2027 Dependency Appeal Form ***Please submit only clear copies of documentation to the Office of Financial Aid; any unclear or unreadable copies will be returned*** Back to Top Disability Documentation (Borrower Acknowledgement Form) 2025-2026 (Fal”
### `4343c98bef4a461a` University of Baltimore — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm (sha256 13b3810be9c2)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/policies/sap.cfm
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you have been asked to complete an SAP appeal, it is located under the My Payments & Financial Aid section in MyUBalt.”
### `8e167d1ed3207d89` University of Baltimore — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm (sha256 13b3810be9c2)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/policies/budget_appeal.cfm
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: budget_increase ⟵ “If asset information was left blank on the FAFSA but was required because the student did not qualify for simplified needs analysis, an asset information form will need to be completed. 2026-2027 Asset Form ***Please submit only clear copies of documentation to the Office of Financial Aid; any unclear or unreadable copies will be returned*** Back to Top Budget Increase - Cost of Attendance (COA) I”
  - sentence: budget_increase ⟵ “In rare cases, student may submit the form below to have their budget increased.”
  - sentence: budget_increase ⟵ “Only one budget increase request is permitted per academic year.”
  - sentence: budget_increase ⟵ “Having a budget increased does not necessarily mean the student will have additional financial aid offered.”
  - sentence: budget_increase ⟵ “Cost of Attendance Increase Request How to View Your COA For additional assistance, please review the of webpage for COA Increase Request policy. ***Please submit only clear copies of documentation to the Office of Financial Aid; any unclear or unreadable copies will be returned*** Back to Top Citizenship 2025-2026 If the U.S.”
### `923d26fc83c4b90c` University of Baltimore — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/policies/cost-of-attendance.cfm (sha256 4a17dac31c68)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm,https://www.ubalt.edu/admission-and-aid/financial-aid/policies/dependency_appeals.cfm,https://www.ubalt.edu/admission-and-aid/financial-aid/policies/special-circumstances.cfm
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Bogomolny LibraryLaw Library Home admission-and-aid financial-aid policies Cost of Attendance Section Menu Satisfactory Academic Progress Cost of Attendance Emergency Loan Net Price Calculator Guidelines to Course Program of Study Study Abroad Verification Withdrawal Policy Other Types of Aid Overawards Cost of Attendance Increase Request Special Circumstances Dependency Appeals Census Date and Fi”
### `9cc21c236715cb09` University of Baltimore — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm (sha256 13b3810be9c2)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Financial Aid administrators cannot use professional judgment to consider a student independent solely on the basis of the student’s previous independent status or because the student is “self-supporting.” The dependency override may not be used to make an otherwise ineligible student eligible for federal aid, or because the parents are unwilling to provide financial data or support.”
  - sentence: professional_judgment ⟵ “This request reflects the professional judgment of the Office of Financial Aid at the University of Baltimore only.”
### `c2ab5527b78fe54e` University of Baltimore — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/policies/dependency_appeals.cfm (sha256 6707f1f4a7a0)
- issues: semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm,https://www.ubalt.edu/admission-and-aid/financial-aid/policies/cost-of-attendance.cfm,https://www.ubalt.edu/admission-and-aid/financial-aid/policies/special-circumstances.cfm
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid and Scholarships has the authority, through Section 480(d)(7) of the Higher Education Act, to change a student’s dependency status on a case‐by‐case basis for students with unusual circumstances.”
### `c5d597cda25b29bc` University of Baltimore — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/policies/budget_appeal.cfm (sha256 ad8890a04e32)
- issues: semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “If the student meets the needed requirements, please complete a Cost of Attendance Increase Request and submit it to Secure Documents.”
### `c5d9c83cb82910ce` University of Baltimore — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/policies/dependency_appeals.cfm (sha256 6707f1f4a7a0)
- issues: semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “Federal regulations specifically prohibit schools from processing a dependency override for any of the following reasons: Parents refuse to contribute to the student's education.”
  - sentence: dependency_override ⟵ “These practices may include making dependency overrides in situations when a student’s parent cannot be located or where an otherwise dependent student has been a victim of domestic violence and is no longer residing with his/her parents.”
  - sentence: dependency_override ⟵ “A dependency override can be made only to change a student’s status from dependent to independent.”
### `d16c8a4278d323bc` University of Baltimore — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/financial-aid-resources/forms.cfm (sha256 13b3810be9c2)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.ubalt.edu/admission-and-aid/financial-aid/policies/cost-of-attendance.cfm,https://www.ubalt.edu/admission-and-aid/financial-aid/policies/dependency_appeals.cfm,https://www.ubalt.edu/admission-and-aid/financial-aid/policies/special-circumstances.cfm
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Back to Top Special Circumstance The Special Circumstance Form can be used if you or your family has experienced an unusual circumstance that may affect your ability to pay for your education at the University of Baltimore.”
  - sentence: need_based_special_circumstances ⟵ “This form does not increase the amount of the student budget. 2025-2026 Special Circumstance Form 2026-2027 Special Circumstance Form ***Please submit only clear copies of documentation to the Office of Financial Aid; any unclear or unreadable copies will be returned*** Back to Top Statement of Educational Purpose and Certification of Identity Effective June 6, 2025, students will no longer be req”
### `939474a8246afe7a` University of Baltimore — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/financial-aid/types-of-aid/scholarships-and-grants/bob-parsons-scholarship.cfm (sha256 d52991727bca)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 4}
  - column:Full Time In-state Tuition and Fees, per year, estimated:: 9000 ⟵ “Full Time In-state Tuition and Fees, per year, estimated: | $9,000”
  - column:Your Pell Grant Award covers:: 4000 ⟵ “Your Pell Grant Award covers: | $4,000”
  - column:The Bob Parsons Scholarship Fund will pay:: 5000 ⟵ “The Bob Parsons Scholarship Fund will pay: | $5,000”
  - column:You pay:: 0.0 ⟵ “You pay: | $0.00*”
### `410b60221da818a6` University of Baltimore — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/transfer-admissions/transfer-your-credits/index.cfm (sha256 7a727f51e4fa)
- issues: score_scale_mismatch, conflicting_sources:https://www.ubalt.edu/admission-and-aid/undergraduate-admissions/high-school-credits.cfm
- checks: {"distinct_exams": 27, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 | Arts and Humanities General Education”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 | General Elective”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 3 | Biological and Physical Sciences (Non-Lab) General Education”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 3 | Mathematics General Education MATH 111 (College Algebra)”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 3 | Biological and Physical Sciences (Non-Lab) General Education”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | Mathematics General Education”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|59]:  ⟵ “College Algebra | 59 | 3 | MATH 111 (College Algebra)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular (with essay) | 50 | 3 | English Composition General Education”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular (without essay) | 50 | 3 | General Elective”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | General Elective”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|Foreign Languages—French Language, Levels 1 and 2]:  ⟵ “College Mathematics | Foreign Languages—French Language, Levels 1 and 2”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|Foreign Languages—German Language, Levels 1 and 2]:  ⟵ “College Mathematics | Foreign Languages—German Language, Levels 1 and 2”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|Foreign Languages—Spanish Language, Levels 1 and 2]:  ⟵ “College Mathematics | Foreign Languages—Spanish Language, Levels 1 and 2”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | 3 | Arts And Humanities General Education”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | 3 | Arts And Humanities General Education”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PSYC 205 (Human Development)”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | General Elective”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 50 | 3 | Interdisciplinary and Emerging Issues (IT Fluency) General Education, INSS100 (Computer Information Systems)”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|52]:  ⟵ “Introduction to Educational Psychology | 52 | 3 | Psychology Major Elective”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BULA 151 (Business Law I)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|58]:  ⟵ “Introductory Psychology | 58 | 3 | PSYC 100 (Introduction to Psychology)”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | 3 | General Elective”
  - … 12 more rows
### `746f93cf06a86916` University of Baltimore — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/transfer-admissions/transfer-your-credits/index.cfm (sha256 7a727f51e4fa)
- issues: conflicting_sources:https://www.ubalt.edu/admission-and-aid/undergraduate-admissions/high-school-credits.cfm
- checks: {"distinct_exams": 27, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | Arts and Humanities General Education”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology (see below) | 3 | 4 | Biological and Physical Sciences (Lab) General Education”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 3 | Mathematics General Education”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 3 | Mathematics General Education”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry (see below) | 3 | 4 | Biological and Physical Sciences (Lab) General Education”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | 3 | General Elective”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 3 | General Elective”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics (see below) | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics (see below) | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language | 3 | 3 | General Elective”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature | 3 | 4 | Arts and Humanities General Education”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science (see below) | 3 | 4 | Biological and Physical Sciences (Lab) General Education”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 | Arts and Humanities General Education”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | 3 | General Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | 3 | General Elective”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government & Politics (see below) | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture | 3 | 3 | General Elective”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | 3 | 3 | General Elective”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 3 | General Elective”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology (see below) | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language | 3 | 3 | General Elective”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “Spanish Literature | 3 | 3 | Arts and Humanities General Education”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics (see below) | 3 | 3 | Mathematics General Education”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “U.S. History | 3 | 3 | Arts and Humanities General Education”
  - … 13 more rows
### `9b1fcffa2fcd6f6c` University of Baltimore — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/transfer-admissions/transfer-your-credits/index.cfm (sha256 7a727f51e4fa)
- issues: rows_without_score
- checks: {"distinct_exams": 14, "equivalencies": 14, "rows_without_score": 14}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | BPS | SL: BIOL 111 / HL: BIOL 101 + BIOL 111 | SL: 4 / HL: 6”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business and Management | SBS | MGMT101 (Introduction to Management) | 3”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | BPS | SL: CHEM 101 / HL: CHEM 101 + Non Lab Science | SL: 4 / HL: 6”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | BPS | SL: Lab Science / HL: Lab Science + Non Lab Science | SL: 4 / HL: 6”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | SBS | ECON200 (The Economic Way of Thinking) | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|None]:  ⟵ “Environmental Systems | BPS NonLab | ENVS201 (Environmental Sustainability) | 3”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | SBS | CSCE200 (Understanding Community) | 3”
  - equivalencies[IB-GLOBAL-POLITICS|None]:  ⟵ “Global Politics | SBS | PPIA210 (Introduction to International Studies) | 3”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History: 20th Century World | AH | HIST290 (History Elective) | 3”
  - equivalencies[IB-LATIN|None]:  ⟵ “Latin | AH | ENGL311 (Classical Foundations) | 3”
  - equivalencies[IB-PHILOSOPHY|None]:  ⟵ “Philosophy | AH | PHIL101 (Introduction to Philosophy) | 3”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Physics | BPS | SL: Lab Science / HL: Lab Science + Non Lab Science | SL: 4 / HL: 6”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | SBS | PSYC100 (Introduction to Psychology) | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|None]:  ⟵ “Social & Cultural Anthropology | SBS | ANTH110 (Cultural Anthropology) | 3”
### `a429cca85ebd193b` University of Baltimore — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/undergraduate-admissions/high-school-credits.cfm (sha256 f240bc4231a8)
- issues: score_scale_mismatch, conflicting_sources:https://www.ubalt.edu/admission-and-aid/transfer-admissions/transfer-your-credits/index.cfm
- checks: {"distinct_exams": 29, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 | Arts and Humanities General Education”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 | General Elective”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 3 | Biological and Physical Sciences (Non-Lab) General Education”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 3 | Mathematics General Education MATH 111 (College Algebra)”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 3 | Biological and Physical Sciences (Non-Lab) General Education”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | Mathematics General Education”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular (with essay) | 50 | 3 | English Composition General Education”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular (without essay) | 50 | 3 | General Elective”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | General Elective”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 | Arts and Humanities General Education”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 | ACCT 201 (Introduction to Financial Accounting) Financial Accounting may not be acceptable for students intending to take the CPA examination; consult the Accounting Department.”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|Foreign Languages—French Language, Levels 1 and 2]:  ⟵ “Financial Accounting | Foreign Languages—French Language, Levels 1 and 2”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|Foreign Languages—German Language, Levels 1 and 2]:  ⟵ “Financial Accounting | Foreign Languages—German Language, Levels 1 and 2”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|Foreign Languages—Spanish Language, Levels 1 and 2]:  ⟵ “Financial Accounting | Foreign Languages—Spanish Language, Levels 1 and 2”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | 3 | Arts And Humanities General Education”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | 3 | Arts And Humanities General Education”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PSYC 205 (Human Development)”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | General Elective”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 50 | 3 | Interdisciplinary and Emerging Issues (IT Fluency) General Education”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|52]:  ⟵ “Introduction to Educational Psychology | 52 | 3 | Psychology Major Elective”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|56]:  ⟵ “Introductory Business Law | 56 | 3 | BULA 151 (Business Law I)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | 3 | General Elective”
  - … 8 more rows
### `fc58f393fd98456d` University of Baltimore — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/undergraduate-admissions/high-school-credits.cfm (sha256 f240bc4231a8)
- issues: conflicting_sources:https://www.ubalt.edu/admission-and-aid/transfer-admissions/transfer-your-credits/index.cfm
- checks: {"distinct_exams": 27, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | Arts and Humanities General Education”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology* | 3 | 4 | Biological and Physical Sciences (Lab) General Education”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 3 | Mathematics General Education”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 3 | Mathematics General Education”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry* | 3 | 4 | Biological and Physical Sciences (Lab) General Education”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | 3 | General Elective”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 3 | General Elective”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics* | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics* | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language | 3 | 3 | General Elective”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language | 4 | 3 | WRIT101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature | 3 | 4 | Arts and Humanities General Education”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science* | 3 | 4 | Biological and Physical Sciences (Lab) General Education”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 | Arts and Humanities General Education”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | 3 | General Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | 3 | General Elective”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government & Politics* | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture | 3 | 3 | General Elective”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin Vergil | 3 | 3 | General Elective”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 3 | General Elective”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology* | 3 | 3 | Social and Behavioral Sciences General Education”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language | 3 | 3 | General Elective”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “Spanish Literature | 3 | 3 | Arts and Humanities General Education”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics* | 3 | 3 | Mathematics General Education”
  - … 14 more rows
### `2eb90966bcf84d53` University of Baltimore — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ubalt.edu/admission-and-aid/transfer-admissions/transfer-your-credits/index.cfm (sha256 7a727f51e4fa)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `70badbd5685acdd6` University of Maryland Eastern Shore — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/09/20-25-UMES-Policy-for-Satisfactory-Academic-Progress-SAP_REVISED-1.pdf (sha256 d6b72d687db3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “Students deemed not to be making Satisfactory Academic Progress will be notified via UMES email and may file an appeal with the Office of Financial Aid.”
  - sentence: sap_appeal ⟵ “Students will also be notified via UMES email as to the outcome of their SAP appeal.”
  - sentence: sap_appeal ⟵ “Students who have questions about Satisfactory Academic Progress may send an email to financialaid@umes.edu Appeal Process Students have the right to appeal a decision of ineligibility to continue to receive financial assistance.”
  - sentence: sap_appeal ⟵ “When a student submits a SAP Appeal, the student must explain why they failed to make SAP and the student must also explain what has changed in the student’s situation that will allow them to meet SAP requirements at the next evaluation.”
  - sentence: sap_appeal ⟵ “All SAP Appeals will be reviewed by the Committee, which consists of a minimum of three Financial Aid Counselors and at least one team member from the Center for Access & Academic Success [CAAS].”
  - sentence: sap_appeal ⟵ “Each Committee member’s role is to evaluate the student’s history, review the SAP Appeal information [which includes a formal Financial Aid Appeal Form; a typed, signed personal statement from the student; documentation to support circumstances cited in the personal statement; and, a CAAS Academic Improvement Plan, which is completed one-on-one with the student and a CAAS Counselor] in accordance ”
### `7a0c5fcfbd3cea30` University of Maryland Eastern Shore — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/satisfactory-academic-progress-sap/ (sha256 bcc5677eb3b6)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Submitting an Appeal Students who wish to appeal the determination that satisfactory academic progress has not been maintained, may do so by submitting an appeal form, a personal statement, all supporting documentation and approved academic improvement plan from CAAS and or advisor, to the Office of Student Financial Aid within ten (10) days of the date of notification that aid has been suspended.”
### `c6cf50bfc1242bfb` University of Maryland Eastern Shore — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umes.edu/admissions/wp-content/uploads/sites/44/2026/10/APPEAL.pdf (sha256 91904569819d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “HBCU INITIATIVE(ACCESS ADVANTAGE) APPEAL FORM Students who lose scholarship eligibility have the right to appeal when extenuating circumstances contribute to the loss of eligibility.”
### `1cdcb79aa67296dd` University of Maryland Eastern Shore — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf (sha256 1a30c4def70f)
- issues: multiple_total_rows, residency_unknown, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 18}
  - column:Tuition: 9173 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees: 430 ⟵ “Fees | $430 | $430 | $430”
  - column:Housing: 9520 ⟵ “Housing | $9,520 | $9,520 | $9,520”
  - column:Food: 5570 ⟵ “Food | $5,570 | $5,570 | $5,570”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL:: 31129 ⟵ “TOTAL: | $28,057 | $40,297 | $31,129”
  - column:Tuition (2): 9173 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (2): 430 ⟵ “Fees | $430 | $430 | $430”
  - column:Housing (2): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (2): 5570 ⟵ “Food | $5,570 | $5,570 | $5,570”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL: (2): 25463 ⟵ “TOTAL: | $22,391 | $34,631 | $25,463”
### `1d94109125102f33` University of Maryland Eastern Shore — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf (sha256 d7f114387471)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 21827 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees: 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation: 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 46138 ⟵ “TOTAL: | $37,341 | $46,138 | $40,538”
  - column:Tuition (2): 21827 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees (2): 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation (2): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 48502 ⟵ “TOTAL: | $39,705 | $48,502 | $42,902”
  - column:Tuition (3): 21827 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees (3): 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation (3): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `1da4c94e8dbcdb35` University of Maryland Eastern Shore — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf (sha256 5e2654abd8a9)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 8904 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees: 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 28674 ⟵ “TOTAL: | $24,426 | $28,674 | $26,382”
  - column:Tuition (2): 8904 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees (2): 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 31038 ⟵ “TOTAL: | $26,790 | $31,038 | $28,746”
  - column:Tuition (3): 8904 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees (3): 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `22a28c3706cf6f7b` University of Maryland Eastern Shore — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf (sha256 574a21f28862)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 18341 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees: 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL:: 40317 ⟵ “TOTAL: | $28,077 | $40,317 | $31,149”
  - column:Tuition (2): 18341 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (2): 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL: (2): 42681 ⟵ “TOTAL: | $30,441 | $42,681 | $33,513”
  - column:Tuition (3): 18341 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (3): 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing (3): 3333 ⟵ “Housing | $3,333 | $3,333 | $3,333”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `2c42bb7119252db8` University of Maryland Eastern Shore — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf (sha256 574a21f28862)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 6101 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees: 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL:: 28077 ⟵ “TOTAL: | $28,077 | $40,317 | $31,149”
  - column:Tuition (2): 6101 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (2): 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL: (2): 30441 ⟵ “TOTAL: | $30,441 | $42,681 | $33,513”
  - column:Tuition (3): 6101 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (3): 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing (3): 3333 ⟵ “Housing | $3,333 | $3,333 | $3,333”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `43910c3411dd58f5` University of Maryland Eastern Shore — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf (sha256 2e24d3b55b76)
- issues: multiple_total_rows, residency_unknown, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 9918 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees: 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 31314 ⟵ “TOTAL: | $28,380 | $34,752 | $31,314”
  - column:Tuition (2): 9918 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees (2): 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 33678 ⟵ “TOTAL: | $30,744 | $37,116 | $33,678”
  - column:Tuition (3): 9918 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees (3): 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `51f11f142281b0e5` University of Maryland Eastern Shore — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf (sha256 2e24d3b55b76)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 6984 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees: 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 28380 ⟵ “TOTAL: | $28,380 | $34,752 | $31,314”
  - column:Tuition (2): 6984 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees (2): 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 30744 ⟵ “TOTAL: | $30,744 | $37,116 | $33,678”
  - column:Tuition (3): 6984 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees (3): 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `716e362f4806069b` University of Maryland Eastern Shore — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf (sha256 5e2654abd8a9)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 4656 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees: 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 24426 ⟵ “TOTAL: | $24,426 | $28,674 | $26,382”
  - column:Tuition (2): 4656 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees (2): 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 26790 ⟵ “TOTAL: | $26,790 | $31,038 | $28,746”
  - column:Tuition (3): 4656 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees (3): 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `80102af9229503ec` University of Maryland Eastern Shore — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf (sha256 a0397c54b296)
- issues: residency_unknown, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 50283 ⟵ “Tuition | $31,699 | $62,167 | $50,283”
  - column:Fees: 2541 ⟵ “Fees | $2,541 | $2,541 | $2,541”
  - column:Housing: 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 4400 ⟵ “Books and Supplies | $4,400 | $4,400 | $4,400”
  - column:Transportation: 4050 ⟵ “Transportation | $4,050 | $4,050 | $4,050”
  - column:Personal & Misc: 3100 ⟵ “Personal & Misc | $3,100 | $3,100 | $3,100”
  - column:Loan Fees: 570 ⟵ “Loan Fees | $570 | $570 | $570”
  - column:TOTAL:: 79268 ⟵ “TOTAL: | $60,684 | $91,152 | $79,268”
### `89b692f725bf4eb6` University of Maryland Eastern Shore — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf (sha256 a0397c54b296)
- issues: conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 31699 ⟵ “Tuition | $31,699 | $62,167 | $50,283”
  - column:Fees: 2541 ⟵ “Fees | $2,541 | $2,541 | $2,541”
  - column:Housing: 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 4400 ⟵ “Books and Supplies | $4,400 | $4,400 | $4,400”
  - column:Transportation: 4050 ⟵ “Transportation | $4,050 | $4,050 | $4,050”
  - column:Personal & Misc: 3100 ⟵ “Personal & Misc | $3,100 | $3,100 | $3,100”
  - column:Loan Fees: 570 ⟵ “Loan Fees | $570 | $570 | $570”
  - column:TOTAL:: 60684 ⟵ “TOTAL: | $60,684 | $91,152 | $79,268”
### `94175fe235742915` University of Maryland Eastern Shore — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf (sha256 d7f114387471)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 13030 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees: 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation: 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 37341 ⟵ “TOTAL: | $37,341 | $46,138 | $40,538”
  - column:Tuition (2): 13030 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees (2): 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation (2): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 39705 ⟵ “TOTAL: | $39,705 | $48,502 | $42,902”
  - column:Tuition (3): 13030 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees (3): 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation (3): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `a321c4d024fd35b1` University of Maryland Eastern Shore — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf (sha256 2e24d3b55b76)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 13356 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees: 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 34752 ⟵ “TOTAL: | $28,380 | $34,752 | $31,314”
  - column:Tuition (2): 13356 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees (2): 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 37116 ⟵ “TOTAL: | $30,744 | $37,116 | $33,678”
  - column:Tuition (3): 13356 ⟵ “Tuition | $6,984 | $13,356 | $9,918”
  - column:Fees (3): 1818 ⟵ “Fees | $1,818 | $1,818 | $1,818”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `a8b055892aa31b50` University of Maryland Eastern Shore — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf (sha256 5e2654abd8a9)
- issues: multiple_total_rows, residency_unknown, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 6612 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees: 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 26382 ⟵ “TOTAL: | $24,426 | $28,674 | $26,382”
  - column:Tuition (2): 6612 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees (2): 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 28746 ⟵ “TOTAL: | $26,790 | $31,038 | $28,746”
  - column:Tuition (3): 6612 ⟵ “Tuition | $4,656 | $8,904 | $6,612”
  - column:Fees (3): 1212 ⟵ “Fees | $1,212 | $1,212 | $1,212”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `b709b6a7fe8d934c` University of Maryland Eastern Shore — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf (sha256 d7f114387471)
- issues: multiple_total_rows, residency_unknown, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 16227 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees: 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation: 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL:: 40538 ⟵ “TOTAL: | $37,341 | $46,138 | $40,538”
  - column:Tuition (2): 16227 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees (2): 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation (2): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 268 ⟵ “Loan Fees | $268 | $268 | $268”
  - column:TOTAL: (2): 42902 ⟵ “TOTAL: | $39,705 | $48,502 | $42,902”
  - column:Tuition (3): 16227 ⟵ “Tuition | $13,030 | $21,827 | $16,227”
  - column:Fees (3): 2323 ⟵ “Fees | $2,323 | $2,323 | $2,323”
  - column:Housing (3): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 3700 ⟵ “Books and Supplies | $3,700 | $3,700 | $3,700”
  - column:Transportation (3): 3700 ⟵ “Transportation | $3,700 | $3,700 | $3,700”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `d1e84c5c75a71185` University of Maryland Eastern Shore — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf (sha256 574a21f28862)
- issues: multiple_total_rows, residency_unknown, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 27}
  - column:Tuition: 9173 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees: 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing: 6666 ⟵ “Housing | $6,666 | $6,666 | $6,666”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL:: 31149 ⟵ “TOTAL: | $28,077 | $40,317 | $31,149”
  - column:Tuition (2): 9173 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (2): 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing (2): 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food (2): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL: (2): 33513 ⟵ “TOTAL: | $30,441 | $42,681 | $33,513”
  - column:Tuition (3): 9173 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (3): 3580 ⟵ “Fees | $3,580 | $3,580 | $3,580”
  - column:Housing (3): 3333 ⟵ “Housing | $3,333 | $3,333 | $3,333”
  - column:Food (3): 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies (3): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (3): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (3): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - … 2 more rows
### `db2a1fa923894545` University of Maryland Eastern Shore — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf (sha256 1a30c4def70f)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 18}
  - column:Tuition: 18341 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees: 430 ⟵ “Fees | $430 | $430 | $430”
  - column:Housing: 9520 ⟵ “Housing | $9,520 | $9,520 | $9,520”
  - column:Food: 5570 ⟵ “Food | $5,570 | $5,570 | $5,570”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL:: 40297 ⟵ “TOTAL: | $28,057 | $40,297 | $31,129”
  - column:Tuition (2): 18341 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (2): 430 ⟵ “Fees | $430 | $430 | $430”
  - column:Housing (2): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (2): 5570 ⟵ “Food | $5,570 | $5,570 | $5,570”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL: (2): 34631 ⟵ “TOTAL: | $22,391 | $34,631 | $25,463”
### `ee81d333c191d412` University of Maryland Eastern Shore — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf (sha256 a0397c54b296)
- issues: conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 62167 ⟵ “Tuition | $31,699 | $62,167 | $50,283”
  - column:Fees: 2541 ⟵ “Fees | $2,541 | $2,541 | $2,541”
  - column:Housing: 9030 ⟵ “Housing | $9,030 | $9,030 | $9,030”
  - column:Food: 5294 ⟵ “Food | $5,294 | $5,294 | $5,294”
  - column:Books and Supplies: 4400 ⟵ “Books and Supplies | $4,400 | $4,400 | $4,400”
  - column:Transportation: 4050 ⟵ “Transportation | $4,050 | $4,050 | $4,050”
  - column:Personal & Misc: 3100 ⟵ “Personal & Misc | $3,100 | $3,100 | $3,100”
  - column:Loan Fees: 570 ⟵ “Loan Fees | $570 | $570 | $570”
  - column:TOTAL:: 91152 ⟵ “TOTAL: | $60,684 | $91,152 | $79,268”
### `f3b0c65131fefef8` University of Maryland Eastern Shore — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Virtual_Campus_2026-2027_like_old.pdf (sha256 1a30c4def70f)
- issues: multiple_total_rows, conflicting_sources:https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Pharmacy_2026-2027_like_old-1.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctor_of_Physical_Therapy_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Doctoral_Programs_2026-2027_like_old-2.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_Physician_Assistant_2026-2027_like_old.pdf,https://www.umes.edu/financialaid/wp-content/uploads/sites/45/2026/06/UMES_COA_UGRD_Main_Campus_2026-2027_like_old.pdf
- checks: {"columns": 1, "rows": 18}
  - column:Tuition: 6101 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees: 430 ⟵ “Fees | $430 | $430 | $430”
  - column:Housing: 9520 ⟵ “Housing | $9,520 | $9,520 | $9,520”
  - column:Food: 5570 ⟵ “Food | $5,570 | $5,570 | $5,570”
  - column:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation: 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc: 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees: 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL:: 28057 ⟵ “TOTAL: | $28,057 | $40,297 | $31,129”
  - column:Tuition (2): 6101 ⟵ “Tuition | $6,101 | $18,341 | $9,173”
  - column:Fees (2): 430 ⟵ “Fees | $430 | $430 | $430”
  - column:Housing (2): 3854 ⟵ “Housing | $3,854 | $3,854 | $3,854”
  - column:Food (2): 5570 ⟵ “Food | $5,570 | $5,570 | $5,570”
  - column:Books and Supplies (2): 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - column:Transportation (2): 2680 ⟵ “Transportation | $2,680 | $2,680 | $2,680”
  - column:Personal & Misc (2): 2360 ⟵ “Personal & Misc | $2,360 | $2,360 | $2,360”
  - column:Loan Fees (2): 106 ⟵ “Loan Fees | $106 | $106 | $106”
  - column:TOTAL: (2): 22391 ⟵ “TOTAL: | $22,391 | $34,631 | $25,463”
### `29a0e10b7feb0df8` University of Maryland Global Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umgc.edu/tuition-financial-assistance/scholarships/maryland-completion (sha256 6a373cee89b5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If you lose continuing eligibility for the Completion Scholarship due to extenuating circumstances you may submit an appeal to request reinstatement of your eligibility.”
### `64e26c3a8611da67` University of Maryland Global Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umgc.edu/admission/requirements (sha256 1d178c815bbf)
- issues: semantic_review_required, conflicting_sources:https://www.umgc.edu/admission/requirements/special-circumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Admission for Special Circumstances Get admission advice for special circumstances before applying to UMGC.”
### `6a5daea4205d48fc` University of Maryland Global Campus — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.umgc.edu/current-students/finances/financial-aid/financial-aid-policies/satisfactory-academic-progress (sha256 35de62cb72e1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “She would not be eligible to submit a SAP appeal because she would not be able to meet SAP requirements by the end of her next term of half-time enrollment. (For an appeal to be considered, students must be able to reach the minimum SAP requirements within 6 credits.”
  - sentence: sap_appeal ⟵ “She would be eligible to submit a SAP appeal, since she would be able to meet SAP requirements by the end of her next term of half-time enrollment. (If this student successfully completed her next 6 credits, her cumulative completion rate would be above the 50% requirement: 15/27 = 55%) If the student submits a SAP appeal and it is approved, she would be placed on probation status and eligible to ”
  - sentence: sap_appeal ⟵ “Please note: SAP appeals are only accepted from students who will be able to meet all cumulative SAP requirements within one probationary term of half-time enrollment, including being mathematically capable of completing their academic program within the maximum timeframe limit.”
  - sentence: sap_appeal ⟵ “SAP appeals should be submitted via our secure document submission page.”
  - sentence: sap_appeal ⟵ “Please note: SAP appeals are separate from and unrelated to academic appeals seeking grade changes or refunds, which are not processed by the Financial Aid Office.”
### `ecc658e0f0f92234` University of Maryland Global Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umgc.edu/admission/requirements/special-circumstances (sha256 1d8d81d32779)
- issues: semantic_review_required, conflicting_sources:https://www.umgc.edu/admission/requirements
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Admission for Special Circumstances | UMGC Skip Navigation Current Students Locations U.S.”
### `7cbaac3aa7bc5719` University of Maryland Global Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umgc.edu/tuition-financial-assistance/tuition/cost-of-attendance (sha256 b3dab3b6b771)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition + Fees: Undergraduate, Maryland Resident: 4140 ⟵ “Tuition + Fees: Undergraduate, Maryland Resident | $4,140”
  - column:Annual Allowances: Amount for Undergraduate Living on Own: 28392 ⟵ “Annual Allowances: Amount for Undergraduate Living on Own | $28,392”
  - column:John's Annual Cost of Attendance: 32532 ⟵ “John's Annual Cost of Attendance | $32,532”
### `124812d1d97b8548` University of Maryland Global Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.umgc.edu/transfers-and-credits/fast-paths-to-credit/credit-by-exam/international-baccalaureate (sha256 0c580770829f)
- issues: score_column_not_scores
- checks: {"distinct_exams": 19, "equivalencies": 47, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology (Higher-Level)]:  ⟵ “Biology (Higher-Level) | 5 | 4 lower-level elective credits”
  - equivalencies[IB-BIOLOGY|Biology (Higher-Level)]:  ⟵ “Biology (Higher-Level) | 6 or 7 | BIOL 103 and 4 lower-level biology elective credits”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business Management (Higher-Level)]:  ⟵ “Business Management (Higher-Level) | 5, 6, or 7 | BMGT 110”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business Management (Standard-Level)]:  ⟵ “Business Management (Standard-Level) | 5, 6, or 7 | BMGT 110”
  - equivalencies[IB-CHEMISTRY|Chemistry (Higher-Level)]:  ⟵ “Chemistry (Higher-Level) | 5 | CHEM 103”
  - equivalencies[IB-CHEMISTRY|Chemistry (Higher-Level)]:  ⟵ “Chemistry (Higher-Level) | 6 or 7 | CHEM 103 and 2 lower-level chemistry elective credits”
  - equivalencies[IB-CHEMISTRY|Chemistry (Standard-Level)]:  ⟵ “Chemistry (Standard-Level) | 5 | CHEM 103”
  - equivalencies[IB-CHEMISTRY|Chemistry (Standard-Level)]:  ⟵ “Chemistry (Standard-Level) | 6 or 7 | CHEM 103 and 2 lower-level chemistry elective credits”
  - equivalencies[IB-LATIN|Classical Languages: Latin (Higher-Level)]:  ⟵ “Classical Languages: Latin (Higher-Level) | 5, 6, or 7 | 4 lower-level LATN elective credits”
  - equivalencies[IB-LATIN|Classical Languages: Latin (Standard-Level)]:  ⟵ “Classical Languages: Latin (Standard-Level) | 5, 6, or 7 | 4 lower-level LATN elective credits”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science (Higher-Level)]:  ⟵ “Computer Science (Higher-Level) | 6 or 7 | 3 lower-level computing elective credits”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science (Standard-Level)]:  ⟵ “Computer Science (Standard-Level) | N/A | Not transferable”
  - equivalencies[IB-ECONOMICS|Economics (Higher-Level)]:  ⟵ “Economics (Higher-Level) | 6 or 7 | ECON 201 and ((course.econ.203!id))”
  - equivalencies[IB-ECONOMICS|Economics (Standard-Level)]:  ⟵ “Economics (Standard-Level) | 6 or 7 | ECON 201”
  - equivalencies[IB-ENGLISH-A-LITERATURE|English A: Literature (Higher-Level)]:  ⟵ “English A: Literature (Higher-Level) | N/A | Not transferable”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|Environmental Systems and Societies (Standard-Level)]:  ⟵ “Environmental Systems and Societies (Standard-Level) | N/A | Not transferable”
  - equivalencies[IB-FILM|Film (Higher-Level)]:  ⟵ “Film (Higher-Level) | 5, 6, or 7 | 3 lower-level humanities elective credits”
  - equivalencies[IB-FILM|Film (Standard-Level)]:  ⟵ “Film (Standard-Level) | N/A | Not transferable”
  - equivalencies[IB-GEOGRAPHY|Geography (Higher-Level)]:  ⟵ “Geography (Higher-Level) | 5, 6, or 7 | GEOG 100”
  - equivalencies[IB-GEOGRAPHY|Geography (Standard-Level)]:  ⟵ “Geography (Standard-Level) | 5, 6, or 7 | GEOG 100”
  - equivalencies[IB-GLOBAL-POLITICS|Global Politics (Higher-Level)]:  ⟵ “Global Politics (Higher-Level) | 6 or 7 | 3 lower-level political science elective credits”
  - equivalencies[IB-GLOBAL-POLITICS|Global Politics (Standard-Level)]:  ⟵ “Global Politics (Standard-Level) | 6 or 7 | 3 lower-level political science elective credits”
  - equivalencies[IB-HISTORY|History (Higher-Level)]:  ⟵ “History (Higher-Level) | 5, 6, or 7 | 3 lower-level history elective credits”
  - equivalencies[IB-HISTORY|History (Standard-Level)]:  ⟵ “History (Standard-Level) | N/A | Not transferable”
  - equivalencies[IB-HISTORY|History: Africa (Higher-Level)]:  ⟵ “History: Africa (Higher-Level) | 5 | 3 lower-level history elective credits”
  - … 22 more rows
### `066f20d37480e4a1` University of Maryland-Baltimore County — appeals 2026-27 [new] (source_unlabeled)
- source: https://scholarships.umbc.edu/currentscholars/discontinuationappeals/ (sha256 9e281b1ef37f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “Kuhn Library Lower Level, Pondside Hours Sun Closed Mon 8:30 am – 4:30 pm Tue 8:30 am – 4:30 pm Wed 8:30 am – 4:30 pm Thu 8:30 am – 4:30 pm Fri 8:30 am – 4:30 pm Sat Closed Contact Contact Us Scholarships on myUMBC Scholarships on Instagram Scholarship Discontinuation Appeals Academic Reviews The Merit Scholarship Unit reviews scholars’ academic standing at the end of each fall and spring semester”
  - sentence: scholarship_retention_appeal ⟵ “If there are extenuating circumstances as to why you were unable to meet your merit scholarship requirements, you will have the opportunity to appeal the loss of your scholarship for Fall 2026: Spring 2026 Discontinuation Appeals open June 8th and is due June 28th, at 11:59pm EST.”
  - sentence: scholarship_retention_appeal ⟵ “Documentation Guidance When appealing the loss of your scholarship due to extenuating circumstances, it is important to provide clear, official, and complete documentation to support your case.”
### `19996af629baa1e7` University of Maryland-Baltimore County — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/sap/ (sha256 d1da2d4da187)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/sap-appeals-advisor-faqs/,https://financialaid.umbc.edu/sap/appeals/,https://financialaid.umbc.edu/sap/faqs/,https://financialaid.umbc.edu/sap/sap-status/,https://financialaid.umbc.edu/special-circumstances/,https://financialaid.umbc.edu/wp-content/uploads/sites/320/2025/08/SAPcardflyer2.0.pdf,https://scholarships.umbc.edu/currentscholars/discontinuationappeals/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Additional Information SAP Status SAP Appeal Process SAP Frequently Asked Questions SAP Appeals- Advisor FAQs Location Albin O.”
### `3f6c62f32125dbb6` University of Maryland-Baltimore County — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/sap/faqs/ (sha256 b600b08a63e4)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/sap-appeals-advisor-faqs/,https://financialaid.umbc.edu/sap/,https://financialaid.umbc.edu/sap/appeals/,https://financialaid.umbc.edu/sap/sap-status/,https://financialaid.umbc.edu/special-circumstances/,https://financialaid.umbc.edu/wp-content/uploads/sites/320/2025/08/SAPcardflyer2.0.pdf,https://scholarships.umbc.edu/currentscholars/discontinuationappeals/
- checks: {"negative_sentences": 0, "sentences": 14}
  - sentence: sap_appeal ⟵ “Restriction: Lasts until the student is found to be meeting SAP standards during a status calculation or there is an approved SAP appeal is on file.”
  - sentence: sap_appeal ⟵ “Probation: If given a probationary SAP appeal approval, probation lasts until until the end of the semester in which the student appealed.”
  - sentence: sap_appeal ⟵ “For more information, check out the SAP Status and SAP Appeal Process pages!”
  - sentence: sap_appeal ⟵ “Please contact your Financial Aid Counselor if you have any specific questions about deviating from the Academic Plan on your SAP appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process When do I know I need to appeal for SAP?”
  - sentence: sap_appeal ⟵ “What is the SAP Appeal Process?”
### `45283d3085d2f76b` University of Maryland-Baltimore County — appeals 2026-27 [new] (source_unlabeled)
- source: https://scholarships.umbc.edu/currentscholars/discontinuationappeals/ (sha256 9e281b1ef37f)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/sap-appeals-advisor-faqs/,https://financialaid.umbc.edu/sap/,https://financialaid.umbc.edu/sap/appeals/,https://financialaid.umbc.edu/sap/faqs/,https://financialaid.umbc.edu/sap/sap-status/,https://financialaid.umbc.edu/special-circumstances/,https://financialaid.umbc.edu/wp-content/uploads/sites/320/2025/08/SAPcardflyer2.0.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Failure Scholarship Discontinuation Appeals are not the same as Satisfactory Academic Progress (SAP) Appeals.”
  - sentence: sap_appeal ⟵ “Learn more about the SAP Appeal process and deadlines here. myUMBC Alert Type Aid Impacted Appeal To Submit Questions?”
  - sentence: sap_appeal ⟵ “Contact… Scholarship Discontinuation UMBC Merit Scholarships (General, Transfer, Scholar Programs) Scholarship Discontinuation Appeal Scholarships Unit Satisfactory Academic Progress (SAP) Failure Federal, State, and Institutional Need-Based Financial Aid SAP Appeal Financial Aid Unit UMBC is committed to creating an accessible, inclusive, and welcoming environment for all students, staff, and vis”
### `50df7972fa879d2a` University of Maryland-Baltimore County — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/dependency-appeal/ (sha256 b5d965795cc2)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “A student who has unusual circumstances, reference above, may pursue the Dependency Appeal.”
  - sentence: need_based_special_circumstances ⟵ “If you indicted ‘yes’ on the FAFSA regarding unusual circumstances, but your circumstances do not warrant an appeal, you can update your FAFSA to indicate ‘no.’ This will allow you to proceed with entering parental information in order to have your FAFSA processed and considered for financial aid.”
### `656bd86759842377` University of Maryland-Baltimore County — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/sap-appeals-advisor-faqs/ (sha256 ca4169234b9a)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/sap/,https://financialaid.umbc.edu/sap/appeals/,https://financialaid.umbc.edu/sap/faqs/,https://financialaid.umbc.edu/sap/sap-status/,https://financialaid.umbc.edu/special-circumstances/,https://financialaid.umbc.edu/wp-content/uploads/sites/320/2025/08/SAPcardflyer2.0.pdf,https://scholarships.umbc.edu/currentscholars/discontinuationappeals/
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: sap_appeal ⟵ “Kuhn Library Pondside Hours Sun Closed Mon 8:30 am – 4:30 pm Tue 8:30 am – 4:30 pm Wed 8:30 am – 4:30 pm Thu 8:30 am – 4:30 pm Fri 8:30 am – 4:30 pm Sat Closed Contact Contact Us Financial Aid on Twitter SAP Appeals: Advisor FAQs Information for Academic Advisors about SAP and SAP appeals.”
  - sentence: sap_appeal ⟵ “SAP Appeals Students who are not meeting SAP standards have the opportunity to appeal for financial aid eligibility if there were unexpected circumstances that prevented them from meeting SAP standards.”
  - sentence: sap_appeal ⟵ “Detailed information on the appeal process is found under SAP Appeal Process.”
  - sentence: sap_appeal ⟵ “FAQs Why was I sent a student’s SAP appeal/Academic Plan?”
  - sentence: sap_appeal ⟵ “As part of their SAP appeal, students must complete an academic plan outlining their intended coursework for each semester until they graduate.”
  - sentence: sap_appeal ⟵ “A student sent me a SAP Appeal form to review, but I’m not their advisor.”
### `7000f5e2376c2cb3` University of Maryland-Baltimore County — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/sap/appeals/ (sha256 214ecd6b56c7)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/sap-appeals-advisor-faqs/,https://financialaid.umbc.edu/sap/,https://financialaid.umbc.edu/sap/faqs/,https://financialaid.umbc.edu/sap/sap-status/,https://financialaid.umbc.edu/special-circumstances/,https://financialaid.umbc.edu/wp-content/uploads/sites/320/2025/08/SAPcardflyer2.0.pdf,https://scholarships.umbc.edu/currentscholars/discontinuationappeals/
- checks: {"negative_sentences": 0, "sentences": 17}
  - sentence: sap_appeal ⟵ “Kuhn Library Pondside Hours Sun Closed Mon 8:30 am – 4:30 pm Tue 8:30 am – 4:30 pm Wed 8:30 am – 4:30 pm Thu 8:30 am – 4:30 pm Fri 8:30 am – 4:30 pm Sat Closed Contact Contact Us Financial Aid on Twitter SAP Appeal Process What is a SAP Appeal?”
  - sentence: sap_appeal ⟵ “Note: the submission of a SAP appeal does not guarantee that the student’s appeal will be approved and their aid eligibility reinstated.”
  - sentence: sap_appeal ⟵ “Decisions made by the SAP Appeals Committee are final and cannot be appealed.”
  - sentence: sap_appeal ⟵ “Submitting the SAP Appeal form How to Submit a SAP Appeal Form SAP Appeal forms are submitted to the Financial Aid office virtually via DocuSign.”
  - sentence: sap_appeal ⟵ “Students will receive a notification when their SAP appeal form is received by our office.”
  - sentence: sap_appeal ⟵ “See the section below, as well as the Submitting a Successful SAP Appeal section, for more information on completing the form.”
### `7893667dbd74d395` University of Maryland-Baltimore County — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/sap/sap-status/ (sha256 5fd80c2f6a77)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/sap-appeals-advisor-faqs/,https://financialaid.umbc.edu/sap/,https://financialaid.umbc.edu/sap/appeals/,https://financialaid.umbc.edu/sap/faqs/,https://financialaid.umbc.edu/special-circumstances/,https://financialaid.umbc.edu/wp-content/uploads/sites/320/2025/08/SAPcardflyer2.0.pdf,https://scholarships.umbc.edu/currentscholars/discontinuationappeals/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Students may wish to pursue a private loan to assist with payment of school-related charges if: the student does not have a circumstance that warrants a SAP appeal or the student missed the appeal deadline date for the current semester of enrollment or the student submitted a SAP appeal and it was not approved Additional information about private (alternative) loans can be found here.”
  - sentence: sap_appeal ⟵ “SAP Probation Students whose SAP appeal has been approved will receive a status of SAP Probation for one semester.”
  - sentence: sap_appeal ⟵ “Students who experienced a new unexpected circumstance are able to submit a new SAP appeal for consideration.”
  - sentence: sap_appeal ⟵ “Students who have filed more than one SAP appeal should be aware that repeated failure to improve performance reduces the likelhood of being approved.”
### `87e80d99399e0e6a` University of Maryland-Baltimore County — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.umbc.edu/wp-content/uploads/sites/320/2025/08/SAPcardflyer2.0.pdf (sha256 cb18a4fbbef5)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/sap-appeals-advisor-faqs/,https://financialaid.umbc.edu/sap/,https://financialaid.umbc.edu/sap/appeals/,https://financialaid.umbc.edu/sap/faqs/,https://financialaid.umbc.edu/sap/sap-status/,https://financialaid.umbc.edu/special-circumstances/,https://scholarships.umbc.edu/currentscholars/discontinuationappeals/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The status could be useful during advising appointments or when providing insight on a student’s SAP Appeal.”
### `de599efdbcd7c59d` University of Maryland-Baltimore County — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/special-circumstances/ (sha256 69bd4890b144)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/dependency-appeal/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Kuhn Library Pondside Hours Sun Closed Mon 8:30 am – 4:30 pm Tue 8:30 am – 4:30 pm Wed 8:30 am – 4:30 pm Thu 8:30 am – 4:30 pm Fri 8:30 am – 4:30 pm Sat Closed Contact Contact Us Financial Aid on Twitter Special Circumstances Students may experience special circumstances that require appeal or additional consideration.”
  - sentence: need_based_special_circumstances ⟵ “Students who have unusual circumstances that wish to appeal for independent status may be eligible to complete the Dependency Appeal for consideration.”
### `ebe3aa11a09ea53c` University of Maryland-Baltimore County — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/special-circumstances/ (sha256 69bd4890b144)
- issues: semantic_review_required, conflicting_sources:https://financialaid.umbc.edu/sap-appeals-advisor-faqs/,https://financialaid.umbc.edu/sap/,https://financialaid.umbc.edu/sap/appeals/,https://financialaid.umbc.edu/sap/faqs/,https://financialaid.umbc.edu/sap/sap-status/,https://financialaid.umbc.edu/wp-content/uploads/sites/320/2025/08/SAPcardflyer2.0.pdf,https://scholarships.umbc.edu/currentscholars/discontinuationappeals/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal– UMBC is required to monitor its student’s academic progress to ensure that they maintain a minimum standard GPA and make steady progress toward degree completion.”
  - sentence: sap_appeal ⟵ “Students who are not meeting SAP are able to appeal for financial aid consideration Dependency Appeal– Students are classified as dependent or independent based on the information submitted on the FAFSA application.”
### `ff552d40f503a2b1` University of Maryland-Baltimore County — appeals 2026-27 [new] (source_unlabeled)
- source: https://scholarships.umbc.edu/accepting-your-transfer-merit-scholarship/ (sha256 36741c0aa296)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “STEP 4: Review the award offer, details, and terms and conditions.”
### `864f26fe7db44cdf` University of Maryland-Baltimore County — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.umbc.edu/8119-2/ (sha256 174d171c2b58)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 9}
  - on_campus:Tuition/Fees: 14086 ⟵ “Tuition/Fees | $14,086 | $34,183”
  - on_campus:Housing: 9248 ⟵ “Housing | $9,248 | $9,428”
  - on_campus:Food: 6490 ⟵ “Food | $6,490 | $6,490”
  - on_campus:Books: 1600 ⟵ “Books | $1,600 | $1,600”
  - on_campus:Transportation: 1900 ⟵ “Transportation | $1,900 | $1,900”
  - on_campus:Other: 7546 ⟵ “Other | $7,546 | $7,546”
  - on_campus:Direct Loan Fee: 142 ⟵ “Direct Loan Fee | $142 | $142”
  - on_campus:PLUS Loan Fee: 1264 ⟵ “PLUS Loan Fee | $1,264 | $1,264”
  - on_campus:Total:: 42456 ⟵ “Total: | $42,456 | $62,553”
### `0b79cf4f12472ce5` University of Maryland-College Park — appeals 2026-27 [new] (labeled_in_source)
- source: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/ (sha256 6d019794e6a1)
- issues: semantic_review_required, conflicting_sources:https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/office-student-financial-aid.pdf,https://financialaid.umd.edu/resources-policies/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Change in Financial Situation Students are responsible for notifying the Office of Student Financial Aid of any changes to their financial circumstances during the year.”
### `6788948f054a95f3` University of Maryland-College Park — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.umd.edu/resources-policies/satisfactory-academic-progress (sha256 e90abb252bf2)
- issues: semantic_review_required, conflicting_sources:https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/,https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/office-student-financial-aid.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The Committee may waive these guidelines and consider cases of unusual hardship, personal injury, death of a relative, or other special circumstances.”
### `6842f7af4514ffca` University of Maryland-College Park — appeals 2026-27 [new] (labeled_in_source)
- source: https://admissions.umd.edu/tuition/transfer-merit-scholarships (sha256 880767b02ff4)
- issues: semantic_review_required, conflicting_sources:https://admissions.umd.edu/tuition/freshman-merit-scholarships
- checks: {"negative_sentences": 1, "sentences": 1}
  - sentence: competing_offer_review ⟵ “Students cannot appeal their merit scholarship decisions, and the university does not match scholarship offers from other institutions.”
### `9296ec4a5fcc569b` University of Maryland-College Park — appeals 2026-27 [new] (source_unlabeled)
- source: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/office-student-financial-aid.pdf (sha256 15602a46a326)
- issues: semantic_review_required, conflicting_sources:https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/office-student-financial-aid/,https://financialaid.umd.edu/resources-policies/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Ofﬁce of Student Financial Aid 1 OFFICE OF STUDENT Change in Financial Situation Students are responsible for notifying the Ofﬁce of Student Financial Aid FINANCIAL AID of any changes to their ﬁnancial circumstances during the year.”
### `cc08ded4ead559da` University of Maryland-College Park — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.umd.edu/resources-policies/satisfactory-academic-progress (sha256 e90abb252bf2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “Students on SAP suspension may re-establish eligibility by submitting an SAP appeal form for reconsideration.”
  - sentence: sap_appeal ⟵ “This letter will include instructions on how to submit a SAP appeal.”
  - sentence: sap_appeal ⟵ “The SAP appeal should describe the unusual circumstances that caused you not to meet the SAP requirements and must detail what has changed that will allow you to meet these requirements in the future.”
  - sentence: sap_appeal ⟵ “Please review the SAP Appeal Form for details.”
  - sentence: sap_appeal ⟵ “If you believe you should have received the SAP appeal letter from our office but did not, please review the SAP Appeal Form, which must be submitted along with the SAP Academic Plan and a letter from a third party.”
  - sentence: sap_appeal ⟵ “Once completed, you can submit these documents via email (umdfinaid@umd.edu), in-person, or by mail: 0115 Mitchell Building Attn: Satisfactory Academic Progress Committee 7999 Regents Drive University of Maryland College Park, MD 20742 Appeal Outcomes SAP Appeals may be approved, approved with conditions or denied.”
### `dd056e2e10661a3e` University of Maryland-College Park — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.umd.edu/tuition/freshman-merit-scholarships (sha256 da73b15a780f)
- issues: semantic_review_required, conflicting_sources:https://admissions.umd.edu/tuition/transfer-merit-scholarships
- checks: {"negative_sentences": 1, "sentences": 1}
  - sentence: competing_offer_review ⟵ “Students cannot appeal their merit scholarship decisions and the university does not match offers from other institutions.”
### `237a5e765bc907a2` University of Maryland-College Park — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/tuition-fees/ (sha256 bc797311f4c8)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 11015.0 ⟵ “Tuition | $11,015.00”
  - column:Additional Differential Tuition for full-time juniors and seniors who are majoring in Business, Engineering, or Computer Science (regardless of residency classification): 3375.0 ⟵ “Additional Differential Tuition for full-time juniors and seniors who are majoring in Business, Engineering, or Computer Science (regardless of residency classification) | $3,375.00”
  - column:Mandatory Fees (includes Tech fee). Maximum charged to all students registered for 9 or more credits: 1820.0 ⟵ “Mandatory Fees (includes Tech fee). Maximum charged to all students registered for 9 or more credits | $1,820.00”
  - column:Board (Resident Dining Plan - Base Plan): 6820.0 ⟵ “Board (Resident Dining Plan - Base Plan) | $6,820.00”
  - column:Room (Standard 2-person w/AC, includes Telecom fee): 10290.0 ⟵ “Room (Standard 2-person w/AC, includes Telecom fee) | $10,290.00”
### `ad900a6ed0f33b90` Washington College — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.washcoll.edu/people_departments/offices/institutional-research/common_data_sets_cds/common-data-set-2024-2025.pdf (sha256 0e9082940e39)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 4048 ⟵ “Total first-time, first-year (degree-seeking) who applied          1067       2595            386                  4048”
  - admits: 2303 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     859         1329          115                  2303”
  - enrolled: 265 ⟵ “Total first-time, first-year (degree-seeking) enrolled              118         135            12                   265”
  - sat_composite_25..75: [1155, 1290, 1340] ⟵ “SAT Composite                     1155                      1290                       1340”
  - sat_math_25..75: [560, 610, 680] ⟵ “SAT Math                           560                       610                       680”
  - act_25..75: [27, 31, 31] ⟵ “ACT Composite                      27                        31                         31”
### `c8f932bd9461c094` Washington College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.washcoll.edu/_images/2.0_admissions/2.3_financial_aid/Satisfactory%20Academic%20Progress%20Appeal%20Form.pdf (sha256 dbc8a8324ff8)
- issues: semantic_review_required, conflicting_sources:https://www.washcoll.edu/_images/2.0_admissions/2.3_financial_aid/currentsappolicy.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SECTION B: If your failure to maintain satisfactory academic progress was due to maximum timeframe requirements, complete the following steps to appeal for Federal aid eligibility (incomplete appeals will be denied): Part 1: Letter of Explanation - Provide a typed letter detailing the reason(s) why you have attempted over 165 hours (including transfer work) and have not completed your degree progr”
### `da1a038324bde21c` Washington College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.washcoll.edu/_images/2.0_admissions/2.3_financial_aid/currentsappolicy.pdf (sha256 e250688fd8eb)
- issues: semantic_review_required, conflicting_sources:https://www.washcoll.edu/_images/2.0_admissions/2.3_financial_aid/Satisfactory%20Academic%20Progress%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Define terms used in discussing the evaluation of satisfactory academic progress including the terms appeal, probation, academic plan, and maximum timeframe. 11.”
  - sentence: sap_appeal ⟵ “SAP Appeal Procedures Washington College will consider appeals for any student that meets one or more of the following: • Serious physical or mental illness of the student • Serious physical or mental illness of the student’s immediate family member • Death of the student’s immediate family member • Other extreme circumstances Appeals must include; 1.”
### `46d874e88335c435` Washington College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.washcoll.edu/financial-aid/cost.php (sha256 0c1cbf2817de)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - column:Tuition* and Fees**: 58704 ⟵ “Tuition* and Fees** | $58,704 | $58,182”
  - column:Housing (average room cost): 9350 ⟵ “Housing (average room cost) | $9,350 | $10,094”
  - column:Food (platinum meal plan): 9232 ⟵ “Food (platinum meal plan) | $9,232 | $9,232”
  - column:Transportation: 1192 ⟵ “Transportation | $1,192 | $1,192”
  - column:Personal: 1960 ⟵ “Personal | $1,960 | $1,960”
  - column:Books, Course Materials, Supplies, and Equipment: 938 ⟵ “Books, Course Materials, Supplies, and Equipment | $938 | $938”
  - column:Loan Fees: 66 ⟵ “Loan Fees | $66 | $66”
  - column:Total Cost of Attendance: 81442 ⟵ “Total Cost of Attendance | $81,442 | $81,664”
  - column:Total Direct Costs: 77286 ⟵ “Total Direct Costs | $77,286 | $77,508”
  - column:Tuition* and Fees**: 58182 ⟵ “Tuition* and Fees** | $58,704 | $58,182”
  - column:Housing (average room cost): 10094 ⟵ “Housing (average room cost) | $9,350 | $10,094”
  - column:Food (platinum meal plan): 9232 ⟵ “Food (platinum meal plan) | $9,232 | $9,232”
  - column:Transportation: 1192 ⟵ “Transportation | $1,192 | $1,192”
  - column:Personal: 1960 ⟵ “Personal | $1,960 | $1,960”
  - column:Books, Course Materials, Supplies, and Equipment: 938 ⟵ “Books, Course Materials, Supplies, and Equipment | $938 | $938”
  - column:Loan Fees: 66 ⟵ “Loan Fees | $66 | $66”
  - column:Total Cost of Attendance: 81664 ⟵ “Total Cost of Attendance | $81,442 | $81,664”
  - column:Total Direct Costs: 77508 ⟵ “Total Direct Costs | $77,286 | $77,508”
### `3c50c4cd2428ff36` Wor-Wic Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.worwic.edu/wp-content/uploads/CLEP-Equivalencies-2025.pdf (sha256 bce1e9d8568b)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 18, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting          50      3      ACT 101             Principles of Accounting I”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law        50      3      BMT 205                   Business Law”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management         50      3      BMT 220      Project Management & Professionalism”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing        50      3      BMT 102                     Marketing”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition           50      3      ENG 101           Fundamentals of English I”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Lit     50      3      ENG 151           Fundamentals of English II”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level I        50      6     FRN 101/102      Fundamentals of French I and II”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level I        50      6     SPN 101/102      Fundamentals of Spanish I and II”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government            50      3      POL 101              American Government”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development          50      3      PSY 251         Human Growth & Development”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology     50      3      EDU 156             Educational Psychology”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology         50      3      PSY 101           Introduction to Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology         50      3      SOC 101            Introduction to Sociology”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics       50      3      ECO 151         Principles of Macroeconomics”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics       50      3      ECO 201          Principles of Microeconomics”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra             50     3      MTH 121                 Precalculus I”
  - equivalencies[CLEP-PRECALCULUS|3]:  ⟵ “Precalculus             50-66    3      MTH 121                 Precalculus I”
  - equivalencies[CLEP-PRECALCULUS|67+]:  ⟵ “Precalculus              67+     4      MTH 122                 Precalculus II”
  - equivalencies[CLEP-CALCULUS|3]:  ⟵ “Calculus               58-66    3      MTH 160                Applied Calculus”
  - equivalencies[CLEP-CALCULUS|67+]:  ⟵ “Calculus                67+     4      MTH 201                  Calculus I”
### `943e00a9c242f217` Wor-Wic Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.worwic.edu/wp-content/uploads/AP-List-2024.pdf (sha256 7e9cd56d6979)
- issues: conflicting_sources:https://www.worwic.edu/wp-content/uploads/AP-List.pdf
- checks: {"distinct_exams": 16, "equivalencies": 16, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                            3             3            ART-101          Introduction to Art History”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                     3             3            CMP-135          Introduction to Programming”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                         3              3           ECO-151          Principles of Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                         3              3           ECO-201          Principles of Microeconomics”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                  3              4           ENV-101          Environmental Science”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History: Modern                  3              6         HIS-101/151        World Civilizations I and II”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “U.S. History                           3              3           HIS-201          American History I”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                       3              3           HIS-ELEC         History Elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                        3              3          GEO-102           Human Geography”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                            4              4          MTH-202           Calculus II”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                           3              3          MUS-101           Music Appreciation”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1: Algebra-Based               4              4           PHY-121          General Physics I”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2: Algebra-Based               4              4           PHY-122          General Physics II”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics                   4              4           PHY-141          Principles of Physics I”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                             3              3           PSY-101          Introduction to Psychology”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                             3              3           MTH-152          Statistics”
### `9d7dc445acc110ef` Wor-Wic Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.worwic.edu/wp-content/uploads/AP-List.pdf (sha256 ef512cd2036b)
- issues: conflicting_sources:https://www.worwic.edu/wp-content/uploads/AP-List-2024.pdf
- checks: {"distinct_exams": 18, "equivalencies": 18, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                             3           3          ART-101      Introduction to Art History”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                          3           3          ECO-151      Principles of Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                          3           3          ECO-201      Principles of Microeconomics”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                   3           4          ENV-101      Environmental Science”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture             3           6        FRN-101/102    Fundamentals of French I and II”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government and Politics            3           3          POL-101      American Government”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History: Modern                   3           6        HIS-101/151    World Civilizations I and II”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “U.S. History                            3           3          HIS-201      American History I”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                        3           3          HIS-ELEC     History Elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                         3           3          GEO-102      Human Geography”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                             4           4         MTH-202       Calculus II”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                            3           3         MUS-101       Music Appreciation”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1: Algebra-Based                4           4          PHY-121      General Physics I”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2: Algebra-Based                4           4          PHY-122      General Physics II”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics                    4           4          PHY-141      Principles of Physics I”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                     3              3             PSY-101        Introduction to Psychology”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4]:  ⟵ “Spanish Language and Culture                   4              3            SPN-201         Intermediate Spanish I”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                                     3              3            MTH-152         Statistics”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 270; pages by category: admissions_tests 45, aid_appeals 18, cost_of_attendance 70, degree_requirements 1, dual_enrollment 1, merit_scholarships 38, residency 7, transfer_credit 1, tuition_fees 19

## Blocked by the site (every request refused; needs the browser fallback)

- Washington Adventist University (`ipeds-162210`)
- Mount St. Mary's University (`ipeds-163462`)
- Prince George's Community College (`ipeds-163657`)
- Yeshiva College of the Nations Capital (`ipeds-434937`)

## Leads: official pages found with no extracted record

- Allegany College of Maryland: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Anne Arundel Community College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, residency
- Bais HaMedrash and Mesivta of Baltimore: admissions_tests
- Baltimore City Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency
- Bowie State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- Capitol Technology University: admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, residency, degree_requirements
- Carroll Community College: tuition_fees, cost_of_attendance, admissions_tests, statewide_articulation, residency, degree_requirements
- Cecil College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- Chesapeake College: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- College of Southern Maryland: admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Community College of Baltimore County: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Coppin State University: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Frederick Community College: admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Frostburg State University: cost_of_attendance, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Garrett College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements, aid_appeals
- Goucher College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Hagerstown Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Harford Community College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Hood College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency
- Howard Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- Johns Hopkins University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Loyola University Maryland: admissions_tests, ap_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- Maryland Institute College of Art: admissions_tests, merit_scholarships, residency, degree_requirements
- McDaniel College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, residency, degree_requirements
- Montgomery College: admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Morgan State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Ner Israel Rabbinical College: tuition_fees, cost_of_attendance, merit_scholarships
- Notre Dame of Maryland University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements, aid_appeals
- Salisbury University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, statewide_articulation, residency, degree_requirements
- St. John's College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, aid_appeals
- St. Mary's College of Maryland: cost_of_attendance, merit_scholarships, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Stevenson University: cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Towson University: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- United States Naval Academy: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements
- University of Baltimore: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Maryland Eastern Shore: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Maryland Global Campus: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Maryland-Baltimore County: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Maryland-College Park: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Washington College: merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- Women's Institute of Torah Seminary and College: tuition_fees, degree_requirements
- Wor-Wic Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
