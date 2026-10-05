# Review queue — MN (2026-27)

Pages fetched: 5250; failures: 385. Candidates: 531 (258 without issues, 273 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 9 | 26 | 29 | 1 | 4 |
| cost_of_attendance | 0 | 0 | 4 | 20 | 40 | 1 | 4 |
| admissions_tests | 0 | 0 | 0 | 0 | 62 | 3 | 4 |
| common_data_set | 0 | 0 | 0 | 0 | 10 | 55 | 4 |
| merit_scholarships | 0 | 0 | 11 | 0 | 50 | 4 | 4 |
| ap_credit | 0 | 0 | 6 | 8 | 33 | 18 | 4 |
| clep_credit | 0 | 0 | 4 | 8 | 31 | 22 | 4 |
| ib_credit | 0 | 0 | 5 | 5 | 17 | 38 | 4 |
| dual_enrollment | 0 | 0 | 5 | 1 | 19 | 40 | 4 |
| transfer_credit | 0 | 0 | 16 | 1 | 47 | 1 | 4 |
| statewide_articulation | 0 | 0 | 0 | 0 | 39 | 26 | 4 |
| residency | 0 | 0 | 0 | 0 | 35 | 30 | 4 |
| degree_requirements | 0 | 0 | 1 | 0 | 50 | 14 | 4 |
| aid_appeals | 0 | 0 | 0 | 42 | 10 | 13 | 4 |

## Ready for review (258)

### `6725385ef81c92a9` Anoka-Ramsey Community College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.anokaramsey.edu/admissions/financial-aid/grants-loans-and-scholarships.html (sha256 92d839b16a5e)
- checks: {"thresholds": null}
  - award_amount_text: Fall Semester ⟵ “April 1 | April 30 | Fall Semester”
### `f041ee5c0066d141` Anoka-Ramsey Community College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.anokaramsey.edu/admissions/financial-aid/grants-loans-and-scholarships.html (sha256 92d839b16a5e)
- checks: {"thresholds": null}
  - award_amount_text: Spring Semester ⟵ “October 1 | October 31 | Spring Semester”
### `d1143404f00ea08b` Augsburg University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.augsburg.edu/studentfinancial/tuition/undergraduate-day/ (sha256 bc791d78bfe6)
- checks: {"columns": 1, "rows": 2}
  - column:Tuition – Full Time (12-19 credits per term): 47600 ⟵ “Tuition – Full Time (12-19 credits per term) | $23,800 | $47,600”
  - column:Standard Fees Technology, Student Activity, Wellness, and Campus Greening – (12-19 credits per term): 899 ⟵ “Standard Fees Technology, Student Activity, Wellness, and Campus Greening – (12-19 credits per term) | $449.50 | $899”
### `4a21489c03ae47f6` Augsburg University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.augsburg.edu/pro/transfer/ (sha256 4e54120ef24a)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Your credits will transfer if: From a regionally accredited institution College level coursework Liberal Arts/non-technical Grade of C- or higher Most applicants transfer in with as many credits as they have taken.”
### `ac21705526bf8e24` Bethel University — academic_programs 2026-27 · program_key=b-s-in-special-education [new] (labeled_in_source)
- source: https://catalog.bethel.edu/academic-programs/college-of-arts-sciences-and-education/undergraduate-programs/education/online-special-education-residency-bs/ (sha256 459e74bb13f7)
- checks: {"courses": 20, "groups": 1, "groups_skipped": 0}
  - program_name: B.S. in Special Education ⟵ “B.S. in Special Education - Residency | Bethel University Catalog”
### `0f7e292059841b4e` Bethel University — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.bethel.edu/academic-information/academic-policies/transferring-credits/ap-clep-ib/ (sha256 79e2eb917691)
- checks: {"distinct_exams": 26, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3-5]:  ⟵ “Art | Studio Art: Drawing Portfolio | 3-5 | 4 | ART 202A”
  - equivalencies[AP-2-D-ART-DESIGN|3-5]:  ⟵ “ | Studio Art: 2D Design Portfolio | 3-5 | 4 | ART 110”
  - equivalencies[AP-3-D-ART-DESIGN|3-5]:  ⟵ “ | Studio Art: 3D Design Portfolio | 3-5 | 4 | ART 110”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | Biology | 3 | 4 | BIO1--D: Laboratory Science”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “ | Biology | 4 | 8 | BIO 124/BIO 124D (4 credits); BIO1--D: Lab Science (4 credits)”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “ | Biology | 5 | 8 | BIO 124/BIO 124D; BIO 128/BIO 128D”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | Chemistry | 3 | 4 | CHE1--D: Laboratory Science”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “ | Chemistry | 4 | 4 | CHE 113/CHE 113D”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “ | Chemistry | 5 | 8 | CHE 113/CHE 113D & CHE 214/CHE 215”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science | Computer Science A | 3 | 2 | COS 101”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “ | Computer Science A | 4-5 | 4 | COS 111”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “ | Computer Science Principles | 3 | 2 | COS1--Computer Science elective”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “ | Computer Science Principles | 4-5 | 2 | COS 101”
  - equivalencies[AP-MACROECONOMICS|3-5]:  ⟵ “Economics | Macroeconomics | 3-5 | 2 | ECO 203”
  - equivalencies[AP-MICROECONOMICS|3-5]:  ⟵ “ | Microeconomics | 3-5 | 2 | ECO 202”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environment | Environmental Science | 3-5 | 4 | ENS 104/ENS 104D”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “French | French Language | 3-5 | 8 | LAN101 Introductory Second Language I; LAN102S Introductory Second Language II”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “ | French Literature | 3-5 | 4 | LAN2: Language3 Elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Geography | Human Geography | 3-5 | 3 | GEO1: Geography Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3-5]:  ⟵ “German | German Language | 3-5 | 8 | LAN 101 Introductory Language I course, LAN 102S Introduction to Second Language II”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “History | U.S. History | 3 | 3 | HIS2: History Elective”
  - equivalencies[AP-UNITED-STATES-HISTORY|4-5]:  ⟵ “ | U.S. History | 4-5 | 6 | HIS 200L (4 credits); HIS2: History Elective (2 credits)”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “ | European History | 3-5 | 6 | HIS2: History Elective”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3-5]:  ⟵ “ | World History | 3-5 | 6 | HIS2: History Elective”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Mathematics | Calculus AB | 3 | 4 | MAT1--M: Mathematics Elective (Can be BUS 100 for BA in Business and BS in Actuarial Science and Finance majors)”
  - … 16 more rows
### `e16493b155d6bd65` Bethel University — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.bethel.edu/academic-information/academic-policies/transferring-credits/ap-clep-ib/ (sha256 79e2eb917691)
- checks: {"distinct_exams": 36, "equivalencies": 42, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL 4 or 5]:  ⟵ “Biology | Biology (HL) | 4 or 5 | 4 | BIO 100/BIO 100D”
  - equivalencies[IB-BIOLOGY-HL|6 or higher]:  ⟵ “ | Biology (HL) | 6 or higher | 8 | BIO 124/BIO 124D; BIO 128/BIO 128D”
  - equivalencies[IB-BIOLOGY-SL|5 or Higher]:  ⟵ “ | Biology (SL) | 5 or Higher | 4 | BIO1-D: Laboratory Science”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|4 or Higher]:  ⟵ “Business Management | Business Management (HL) | 4 or Higher | 6 | BUS1: Business Elective”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|5 or Higher]:  ⟵ “ | Business Management (SL) | 5 or Higher | 3 | BUS1: Business Elective”
  - equivalencies[IB-CHEMISTRY-HL|4 or Higher]:  ⟵ “Chemistry | Chemistry (HL) | 4 or Higher | 6 | CHE1-D: Laboratory Science”
  - equivalencies[IB-CHEMISTRY-SL|5 or Higher]:  ⟵ “ | Chemistry (SL) | 5 or Higher | 3 | CHE1-D: Laboratory Science”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|4 or Higher]:  ⟵ “Computer Science | Computer Science (HL) | 4 or Higher | 6 | COS1: Computer Science Elective”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|5 or Higher]:  ⟵ “ | Computer Science (SL) | 5 or Higher | 3 | COS1: Computer Science Elective”
  - equivalencies[IB-ECONOMICS-HL|4 or Higher]:  ⟵ “Economics | Economics (HL) | 4 or Higher | 6 | ECO1: Economics Elective”
  - equivalencies[IB-ECONOMICS-SL|5 or Higher]:  ⟵ “ | Economics (SL) | 5 or Higher | 3 | ECO1: Economics Elective”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-HL|5 or Higher]:  ⟵ “Environmental Systems | Environmental Systems (HL) | 5 or Higher | 4 | ENS 104/ENS 104D”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|6 or Higher]:  ⟵ “ | Environmental Systems (SL) | 6 or Higher | 4 | ENS 104/ENS 104D”
  - equivalencies[IB-GEOGRAPHY-HL|4 or Higher]:  ⟵ “Geography | Geography (HL) | 4 or Higher | 4 | GEO 120”
  - equivalencies[IB-GEOGRAPHY-SL|5 or Higher]:  ⟵ “ | Geography (SL) | 5 or Higher | 4 | GEO 120”
  - equivalencies[IB-HISTORY-SL|5 or Higher]:  ⟵ “History | History (SL) | 5 or Higher | 3 | HIS1: History Elective”
  - equivalencies[IB-HISTORY-HL|4 or Higher]:  ⟵ “ | History of Africa (HL) | 4 or Higher | 6 | Contact Department Chair”
  - equivalencies[IB-HISTORY-HL|4 or Higher]:  ⟵ “ | History of the Americas (HL) | 4 or Higher | 4 | HIS1-L: Contemporary Western Life & Thought”
  - equivalencies[IB-SPANISH-SL|5 or Higher]:  ⟵ “ | Spanish A2 (SL) | 5 or Higher | 3 | SPA2: Spanish Elective”
  - equivalencies[IB-FRENCH-HL|4 or Higher]:  ⟵ “ | French (HL) | 4 or Higher | 8 | LAN 102S Introduction to Second Language II”
  - equivalencies[IB-FRENCH-SL|5 or Higher]:  ⟵ “ | French (SL) | 5 or Higher | 4 | LAN 102S Introduction to Second Language II”
  - equivalencies[IB-GERMAN-HL|4 or Higher]:  ⟵ “ | German (HL) | 4 or Higher | 8 | LAN102S Introduction to Second Language II”
  - equivalencies[IB-GERMAN-SL|5 or Higher]:  ⟵ “ | German (SL) | 5 or Higher | 4 | LAN102S Introduction to Second Language II”
  - equivalencies[IB-SPANISH-HL|4 or Higher]:  ⟵ “ | Spanish (HL) | 4 or Higher | 8 | SPA 102S”
  - equivalencies[IB-SPANISH-SL|5 or Higher]:  ⟵ “ | Spanish (SL) | 5 or Higher | 4 | SPA 102S”
  - … 17 more rows
### `ed3d241750234958` Bethel University — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.bethel.edu/academic-information/academic-policies/transferring-credits/ap-clep-ib/ (sha256 79e2eb917691)
- checks: {"distinct_exams": 27, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “Composition and Literature | American Literature | 50 | 4 | ENJ 103”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “ | Analyzing & Interpreting Literature | 50 | 4 | ENJ 100”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “ | College Composition (with Essay) | 50 | 4 | GES 161 Composition”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “ | College Composition Modular | 50 | 3 | ENJ1--A: Artistic Experience”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “ | English Literature | 50 | 4 | ENJ 102”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “ | Humanities | 50 | 4 | GES1: General Studies Elective”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “Science and Math | College Algebra | 50 | 2 | MAT1--M: Mathematics”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “ | Biology | 50 | 3 | BIO1: Biology Elective”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “ | Calculus | 50 | 4 | MAT 124M”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “ | Chemistry | 50 | 4 | CHE1: Chemistry Elective”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “ | College Math | 50 | 4 | MAT1-M: Mathematics”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “ | Natural Sciences | 50 | 3 | GES1: General Education Elective”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “ | Precalculus | 50 | 4 | MAT 121M”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “Foreign Languages | Level 1 French | 50 | 8 | LAN101 Introductory Language I; LAN102S Introductory Second Language II”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “ | Level 2 French | 62 | 14 | LAN101 Introductory Language I; LAN102S Introductory Second Language II; LAN 201 Intermediate Language I; LAN 202 Intermediate Language II”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “ | Level 1 German | 50 | 8 | LAN 101 Introductory Language I course, LAN 102S Introductory Second Language II”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “ | Level 2 German | 63 | 11 | LAN 101 Introductory Language I course, LAN 102S Introductory Second Language II, LAN 201 Intermediate Language course”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “ | Level 1 Spanish | 50 | 8 | SPA 101; SPA 102S”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “ | Level 2 Spanish | 63 | 14 | SPA 101; SPA 102S; SPA 201S; SPA 202SU”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “History & Social Science | American Government | 50 | 3 | POS 100”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “ | Human Growth & Development | 50 | 3 | PSY 203”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “ | MacroEconomics, Prin | 50 | 2 | ECO 203”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “ | MicroEconomics, Prin | 50 | 2 | ECO 202”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “ | Psychology, Intro | 50 | 4 | PSY 101; PSY 102”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “ | Sociology, Intro | 50 | 4 | SOC 101”
  - … 5 more rows
### `m922f47ad2d8c24b` Bethel University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.bethel.edu/undergrad/admissions/early-college/pseo/ (sha256 b440872558ba)
- checks: {"fields": ["alt_min_act", "min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 3, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Either have a GPA of at least 3.0 or submit a qualifying test score (ACT composite score of 24+ or 75th percentile on a standardized test)”
  - per_credit_hour_charge: 250 ⟵ “PSEO students between their junior and senior year of high school may take summer PSEO classes at the reduced early college rate of $250/credit. Most summer courses run during one half of the summer term, while others may run the entire length of the summer term. Courses vary in length and may overl”
  - eligibility_tier: 3.0 ⟵ “Either have a GPA of at least 3.0 or submit a qualifying test score (ACT composite score of 24+ or 75th percentile on a standardized test)”
  - eligibility_tier: 3.0 ⟵ “Either have a GPA of at least 3.0 or submit a qualifying test score (ACT composite score of 24+ or 75th percentile on a standardized test)”
  - per_credit_hour_charge: 265 ⟵ “Students between their junior and senior year of high school make take summer courses at the reduced early college rate of $265/credit. Most summer courses run during one half of the summer term, while others may run the entire length of the summer term. Courses vary in length and may overlap. Email”
  - eligibility_tier: 3.0 ⟵ “Either have a GPA of at least 3.0 or submit a qualifying test score (ACT composite score of 24+ or 75th percentile on a standardized test)”
### `1080f6010e7b7497` Bethel University — degree_requirements 2026-27 · program_key=b-s-in-special-education · requirement_key=admission-requirements-major-in-special-education-residency-b-s [new] (labeled_in_source)
- source: https://catalog.bethel.edu/academic-programs/college-of-arts-sciences-and-education/undergraduate-programs/education/online-special-education-residency-bs/ (sha256 459e74bb13f7)
  - courses: SPED 205 ⟵ “SPED 205 - Introduction to Special Education”
  - courses: SPED 309 ⟵ “SPED 309 - Introduction to Academic and Behavior Support”
  - courses: SPED 322 ⟵ “SPED 322 - Teaching Reading (including Field Experience)”
  - courses: SPED 401 ⟵ “SPED 401 - Characteristics of Students with Mild-Moderate Disabilities (and Field Experience)”
  - courses: SPED 410 ⟵ “SPED 410 - Norm-Referenced Assessment”
  - courses: SPED 418 ⟵ “SPED 418 - Instructional Strategies for Students with Mild-Moderate Disabilities”
  - courses: SPED 432 ⟵ “SPED 432 - Responsive Intervention and Assessment”
  - courses: SPED 442 ⟵ “SPED 442 - Introduction to Student Mental Health and Systems of Comprehensive Support”
  - courses: SPED 454 ⟵ “SPED 454 - Classroom-based Assessment”
  - courses: SPED 470 ⟵ “SPED 470 - Assessment Field Experience”
  - courses: SPED 474 ⟵ “SPED 474 - Consultation and Collaboration in Programming for Students with Disabilities”
  - courses: SPED 480 ⟵ “SPED 480 - ABS Student Teaching”
  - courses: TEAC 395 ⟵ “TEAC 395 - School-Wide Field Experience”
  - courses: TEAC 468 ⟵ “TEAC 468 - Education Residency Seminar I”
  - courses: TEAC 469 ⟵ “TEAC 469 - Education Residency Seminar II”
  - courses: TEAC 470 ⟵ “TEAC 470 - Education Residency Seminar III”
  - courses: TEAC 521 ⟵ “TEAC 521 - Foundations of Education”
  - courses: TEAC 524 ⟵ “TEAC 524 - Educational Psychology”
  - courses: TEAC 526 ⟵ “TEAC 526 - General Methods of Instruction”
  - courses: TEAC 528 ⟵ “TEAC 528 - Diversity, Equity, and Inclusion in Education”
### `12532761f18ff8bc` Bethel University — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.bethel.edu/academic-information/academic-policies/transferring-credits/ (sha256 3e9701272a74)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Undergraduate Transfer Credit Only courses in which students earn a grade of C- or better may be transferred to Bethel.”
### `0c73e31cf9fdf13d` Century College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.century.edu/admissions/next-steps/transfer-credit-policy/ (sha256 0765ef07448b)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “While D grades transfer, some specialized/ occupational/technical programs require courses to have a grade of C or higher to fulfill requirements.”
### `40afa8014e8cf98a` Concordia College at Moorhead — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/admission/the-truth-about-our-costs/ (sha256 0e0aa66e2604)
- checks: {"thresholds": null}
  - test_requirement: ACT Score: 22-23 ⟵ “22-23 | $14,500 | 3.01-3.34”
  - gpa_requirement: High School GPA: 3.01-3.34 ⟵ “22-23 | $14,500 | 3.01-3.34”
  - award_amount_text: $14,500 ⟵ “22-23 | $14,500 | 3.01-3.34”
### `73d00dd224863cf6` Concordia College at Moorhead — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/admission/the-truth-about-our-costs/ (sha256 0e0aa66e2604)
- checks: {"thresholds": null}
  - test_requirement: ACT Score: 30-32 ⟵ “30-32 | $18,500 | 3.85-3.96”
  - gpa_requirement: High School GPA: 3.85-3.96 ⟵ “30-32 | $18,500 | 3.85-3.96”
  - award_amount_text: $18,500 ⟵ “30-32 | $18,500 | 3.85-3.96”
### `adbd976cc18eef44` Concordia College at Moorhead — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/admission/the-truth-about-our-costs/ (sha256 0e0aa66e2604)
- checks: {"thresholds": null}
  - test_requirement: ACT Score: 26-27 ⟵ “26-27 | $16,500 | 3.55-3.69”
  - gpa_requirement: High School GPA: 3.55-3.69 ⟵ “26-27 | $16,500 | 3.55-3.69”
  - award_amount_text: $16,500 ⟵ “26-27 | $16,500 | 3.55-3.69”
### `c1f949318953e421` Concordia College at Moorhead — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/admission/the-truth-about-our-costs/ (sha256 0e0aa66e2604)
- checks: {"thresholds": null}
  - test_requirement: ACT Score: 24-25 ⟵ “24-25 | $15,500 | 3.35-3.54”
  - gpa_requirement: High School GPA: 3.35-3.54 ⟵ “24-25 | $15,500 | 3.35-3.54”
  - award_amount_text: $15,500 ⟵ “24-25 | $15,500 | 3.35-3.54”
### `954636375a55db75` Concordia College at Moorhead — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/admission/pseo-and-dual-enrollment/ (sha256 3be9ac0c12e3)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 590 ⟵ “$590 per credit”
### `8e5ff291b76f19bb` Concordia College at Moorhead — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/admission/transfer-students/cobber-completion-plan/ (sha256 9e431bba63d5)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “All transfer courses must individually meet the transfer credit policy, including a standard letter grade of C- or better, to transfer and count toward the overall credits needed for graduation.”
### `1a016fbc206c5f77` Concordia University-Saint Paul — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csp.edu/tuition-and-financial-aid/ (sha256 6a56f06b4489)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition (12-19 credits): 21700 ⟵ “Tuition (12-19 credits) | $21,700 | ($10,850 per semester)”
  - column:Residence Hall / Food Services: 13650 ⟵ “Residence Hall / Food Services | $13,650 | ($6,825 per semester)”
  - column:Total: 35350 ⟵ “Total | $35,350 | ($17,675 per semester)”
### `m31dae271c07c9c9` Crown College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.crown.edu/academics/pseo/dual-enrollment/ (sha256 93886a9561e7)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 1}
  - per_credit_hour_charge: 255 ⟵ “Tuition is $255/Credit”
  - per_credit_hour_charge: 255 ⟵ “$255/credit x 3 credits = $765 total”
  - eligibility_tier: 3.0 ⟵ “Students must have a minimum 3.0 high school GPA”
  - eligibility_tier: 3.0 ⟵ “minimum 3.0 high school GPA”
  - per_credit_hour_charge: 255 ⟵ “$255/Credit                                                              To apply, students must”
### `903968681db3f219` Dakota County Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.dctc.edu/admissions/transfer-to-dctc/clep-equivalency-chart/ (sha256 9f9bd9c730ba)
- checks: {"distinct_exams": 33, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | Goal 6 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | ENGL 1550 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL 1150 Goal 1 | 6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | Goal 1 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | Goal 6 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | HUMA 1100 | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | Goal 5 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | HIST 1100 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | HIST 1200 (Goal 5 Only) | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | PSYC 1350 (Goal 5 Only) | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology | 50 | Goal 5 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BUSN 1110 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSYC 1105 (Goal 5 Only) | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOCY 1110 (Goal 5 Only) | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECON 1200 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECON 1100 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | Goal 5 | 6”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 50 | Goal 5 Goal 8 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II | 50 | Goal 5 Goal 8 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT 1010 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BUSN 1000 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | MKTC 1000 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL1500 | 6”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | Goal 4 | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM 1500 | 6”
  - … 12 more rows
### `b78100c187bb46e3` Dakota County Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.dctc.edu/admissions/transfer-to-dctc/ap-equivalency-chart/ (sha256 2b05d15e2da5)
- checks: {"distinct_exams": 42, "equivalencies": 42, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | Goal 6 | 6”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing | 3 | Goal 6 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2D Art & Design | 3 | Goal 6 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Studio Art: 3-D Design Portfolio | 3 | Goal 6 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | Goal 6 | Score 3 = 3 Credits Score 4 or 5 = 6 Credits”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition | 3 | ENGL 1150 | 6”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition | 3 | ENGL 1150 ENGL 1550 | 6”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | Goal 5 Goal 7 | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics | 3 | Goal 5 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | Goal 5 Goal 8 | 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | Goal 5 | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government & Politics | 3 | Goal 5 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “U.S. History | 3 | HIST 1100 HIST 1200 | 6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History | 3 | Hist 1361 Goal 5 and 8 | 6”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | ECON 1200 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | ECON 1100 | 3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSYC 1105 | 3”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “Research | 3 | Goal 2 | Score 3 = 3 Credits Score 4 or 5 = 6 Credits”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “Seminar | 3 | Goal 2 | Score 3 = 3 Credits Score 4 or 5 = 6 Credits”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3]:  ⟵ “Personal Finance | 3 | Technical Elective | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | Goal 4 | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | Goal 4 | 8”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | MATS 1251 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | ISTC 1300 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | ISTC Elective | 3”
  - … 17 more rows
### `1858445a321a0075` Dunwoody College of Technology — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://dunwoody.edu/pdfs/DCT-Registrar-AP-Transfers-May2025.pdf (sha256 eecbe8f47383)
- checks: {"distinct_exams": 39, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art & Design                 3         3           HUMANITIES”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art & Design                 3         3           HUMANITIES”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies         3         3           HUMANITIES”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                      3         3           HISTORY OF DESIGN (ARTS1250)”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                          3         3           NATURAL SCIENCE W/ LAB”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                      3         4           CALCULUS I (MATH1811)”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                      3         8           CALCULUS I (MATH1810/MATH1811) and”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “Research                         3         3           COMMUNICATIONS W/ WRITING”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “Seminar                          3         3           COMMUNICATIONS W/ WRITING”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                        3         4           CHEMISTRY W/ LAB (CHEM2110)”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture     3         6           HUMANITIES and/or SOCIAL SCIENCE”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and       3         3           SOCIAL SCIENCE”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles      3         2           INTRO TO OPERATING SYSTEMS (CNTS1102)”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                          3         3           HUMANITIES”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and             3         3           COMMUNICATIONS W/ WRITING”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and           3         6           HUMANITIES and/or”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science            3         3           NATURAL SCIENCE (WITHOUT LAB)”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                 3         3           SOCIAL SCIENCE”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture      3         6           HUMANITIES and/or SOCIAL SCIENCE”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture      3         6           HUMANITIES and/or SOCIAL SCIENCE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                  3         3           SOCIAL SCIENCE”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture     3         6           HUMANITIES and/or SOCIAL SCIENCE”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture    3         6           HUMANITIES and/or SOCIAL SCIENCE”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin                            3         3           HUMANITIES”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                   3         3           INTRO TO ECONOMICS (SSCI1100)”
  - … 16 more rows
### `m4f6bb85f3722c73` Dunwoody College of Technology — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.dunwoody.edu/catalog-student-handbook/admissions/transfer-students-transfer-credit/ (sha256 d0591d8a5789)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “A minimum letter grade of "C" or better or a "P" grade (Spring2020-COVID or articulated on the awarding institution's transcript key) is required for transfer.”
  - min_grade: C ⟵ “A minimum letter grade of "C" or better or a "P" grade Construction & Maintenance degree program may only receive credit for up to (Spring2020-COVID or articulated on the awarding institution's one-third of the program's courses. transcript key) is required for transfer. c.”
### `1900236355b3d699` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year/talent (sha256 22ebf8e9d8aa)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 ⟵ “Digital and studio art scholarships | Up to $3,000 | Selection made by digital and studio art faculty. Portfolio, artist statement, and digital and studio art major declaration required.”
  - eligibility_summary: Selection made by digital and studio art faculty. Portfolio, artist statement, and digital and studio art major declaration required. ⟵ “Digital and studio art scholarships | Up to $3,000 | Selection made by digital and studio art faculty. Portfolio, artist statement, and digital and studio art major declaration required.”
### `2a52bca3cfd83ed5` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year/talent (sha256 22ebf8e9d8aa)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 ⟵ “Theatre scholarships | Up to $3,000 | Selection based on audition and/or interview (if interest is not related to acting). Theatre arts majors, minors, and participants in tech design, stage crew, and theatre-related programs are eligible to apply.”
  - eligibility_summary: Selection based on audition and/or interview (if interest is not related to acting). Theatre arts majors, minors, and participants in tech design, stage crew, and theatre-related programs are eligible to apply. ⟵ “Theatre scholarships | Up to $3,000 | Selection based on audition and/or interview (if interest is not related to acting). Theatre arts majors, minors, and participants in tech design, stage crew, and theatre-related programs are eligible to apply.”
### `57290db09e758160` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year (sha256 121b0b8c6fae)
- checks: {"thresholds": null}
  - award_amount_text: $28,000–$30,000 ⟵ “Achievement Scholarship | $28,000–$30,000”
### `5d7c618a5352148e` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year/talent (sha256 22ebf8e9d8aa)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 ⟵ “Writing scholarship | Up to $3,000 | Selection made by English faculty. Writing sample required. Open to any student with an aptitude for writing and/or writing potential.”
  - eligibility_summary: Selection made by English faculty. Writing sample required. Open to any student with an aptitude for writing and/or writing potential. ⟵ “Writing scholarship | Up to $3,000 | Selection made by English faculty. Writing sample required. Open to any student with an aptitude for writing and/or writing potential.”
### `60f099955333eb4d` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year (sha256 121b0b8c6fae)
- checks: {"thresholds": null}
  - award_amount_text: 100% of first-year tuition is covered for qualified students. Get more info ON THE Piper Promise ⟵ “Piper Promise Grant | 100% of first-year tuition is covered for qualified students. Get more info ON THE Piper Promise”
### `7bfd8b24b236cfff` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year/talent (sha256 22ebf8e9d8aa)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 ⟵ “Business scholarships | Up to $3,000 | Selection made by business faculty. Business or economics major required.”
  - eligibility_summary: Selection made by business faculty. Business or economics major required. ⟵ “Business scholarships | Up to $3,000 | Selection made by business faculty. Business or economics major required.”
### `9729937d97d4eb0f` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year (sha256 121b0b8c6fae)
- checks: {"thresholds": null}
  - award_amount_text: $35,000 ⟵ “Presidential Scholarship | $35,000”
### `b1cef2e2616628bd` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year (sha256 121b0b8c6fae)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 for children, grandchildren, and siblings of Hamline graduates and those families who will have two or more students concurrently enrolled in the undergraduate program. ⟵ “Hamline Heritage Award | $3,000 for children, grandchildren, and siblings of Hamline graduates and those families who will have two or more students concurrently enrolled in the undergraduate program.”
### `bea3891b0ce52d54` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year (sha256 121b0b8c6fae)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 for first-generation college students (students whose parents have not earned a degree from a 4-year college or university). ⟵ “Hamline Firsts Award | $3,000 for first-generation college students (students whose parents have not earned a degree from a 4-year college or university).”
### `dff675c9f1dbea43` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year (sha256 121b0b8c6fae)
- checks: {"thresholds": null}
  - award_amount_text: $32,000 ⟵ “Honors Scholarship | $32,000”
### `e52f87b0f47dab2a` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year/talent (sha256 22ebf8e9d8aa)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 ⟵ “Science/STEM scholarships | Up to $3,000 | Open to any student with a demonstrated interest in, or aptitude for, a science/STEM major.”
  - eligibility_summary: Open to any student with a demonstrated interest in, or aptitude for, a science/STEM major. ⟵ “Science/STEM scholarships | Up to $3,000 | Open to any student with a demonstrated interest in, or aptitude for, a science/STEM major.”
### `f4c2f1c31f229c1c` Hamline University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/financial-aid/grants-scholarships/first-year/talent (sha256 22ebf8e9d8aa)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 ⟵ “Music scholarships | Up to $5,000 | Selection based on audition (by invitation). Music majors, minors, and participants in music programs are eligible to apply.”
  - eligibility_summary: Selection based on audition (by invitation). Music majors, minors, and participants in music programs are eligible to apply. ⟵ “Music scholarships | Up to $5,000 | Selection based on audition (by invitation). Music majors, minors, and participants in music programs are eligible to apply.”
### `34c8ef1d8d343aea` Hamline University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.hamline.edu/sites/default/files/2025-02/Cost_Comparison_Worksheet_FY24_access.pdf (sha256 e878cc9da0d4)
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 48784 ⟵ “Tuition | $48,784*”
  - column:Fees: 1520 ⟵ “Fees | $1,520”
  - column:On-campus housing and food: 12400 ⟵ “On-campus housing and food | $12,400”
  - column:Books: 740 ⟵ “Books | $740**”
### `45a9dac65507d1d4` Hamline University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/admission/transferring-credit-high-school (sha256 d27c79b1e713)
- checks: {"distinct_exams": 13, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | 5 | General credit | N2”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business Management | 4 | General credit | ”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 1130, CHEM 1140 | N2”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | 4 | ECON 1100 | G, S”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | General credit | ”
  - equivalencies[IB-GLOBAL-POLITICS|4]:  ⟵ “Global Politics | 4 | Elective credit | G, S”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of the Americas | 4 | Elective credit | S”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music | 4 | General credit | F”
  - equivalencies[IB-PHILOSOPHY|5]:  ⟵ “Philosophy | 5 | PHIL 1120 | H”
  - equivalencies[IB-PHYSICS|5]:  ⟵ “Physics | 5 | PHYS 1150, PHYS 1160 | N2”
  - equivalencies[IB-PSYCHOLOGY|4]:  ⟵ “Psychology | 4 | PSY 1330 | S”
  - equivalencies[IB-THEATRE|4]:  ⟵ “Theatre | 4 | PPC 1120 | F”
  - equivalencies[IB-VISUAL-ARTS|4]:  ⟵ “Visual Arts | 4 | General credit | F”
### `5b29ad3d384aeef2` Hamline University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.hamline.edu/admission-aid/admission/transferring-credit-high-school (sha256 d27c79b1e713)
- checks: {"distinct_exams": 30, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | Elective credit | F, H”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Art—Drawing | 4 | General credit | F”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “Art—2D Design | 4 | General credit | F”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “Art—3D Design | 4 | General credit | F”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | General credit | N2”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 | MATH 1170 | M, R”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | MATH 1170 and MATH 1180 | M, R”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | General credit | N2”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | General credit | G”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 | Elective credit | R”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles | 4 | General credit | R”
  - equivalencies[AP-MACROECONOMICS|4]:  ⟵ “Economics: Macro | 4 | Elective credit | S”
  - equivalencies[AP-MICROECONOMICS|4]:  ⟵ “Economics: Micro | 4 | Elective credit | S”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language and Composition | 4 | General credit | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature and Composition | 4 | ENCM 1400 | H”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ECST 1100 | N2”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | FREN 3210 | G”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language | 4 | FREN 3220 | G”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | GERM 3210 | G”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language | 4 | GERM 3220 | G”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography | 4 | Elective credit | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4]:  ⟵ “Italian Language and Culture | 4 | General credit | G”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin | 4 | General credit | ”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | MUS 3410 | ”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics I | 3 | General credit | N2”
  - … 8 more rows
### `9462b058bdcdeedd` Inver Hills Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://inverhills.edu/admissions/enrollment-academic-options/adult-learners/credit-for-prior-learning/ap-course-equivalencies/ (sha256 0f79d0f203ed)
- checks: {"distinct_exams": 33, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History (f) | 3 | ART 1106 or 1107 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Drawing (f) | 3 | ART 1114 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Studio 2-D Design (f) | 3 | ART 1120 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Studio 3-D Design (f) | 3 | ART 1196 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology (f) | 3 | BIO 1120 | 4”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB (f) | 3 | MATH 1120 | 3”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f) | 4-5 | MATH 1133 | 5”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC (f) | 3 | MATH 1133 | 5”
  - equivalencies[AP-CALCULUS-BC|4-5]:  ⟵ “Calculus BC (f) | 4-5 | MATH 1133, 1134 | 10”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 1061 | 5”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 1061, 1062 | 10”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A (s) | 3 | CS 1110 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | Elective | 4”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics (s) | 3 | ECON 1105 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics (s) | 3 | ECON 1106 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Languages, Composition (f) | 3 | ENG 1108 | 4”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature, Composition (f) | 3 | ENG 1140 | 4”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science (s) | 3 | General elective | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language (f) | 3 | Goal 6b, 8 | 5”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language (f) | 3 | FREN 1101 | 5”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language (f) | 3 | GERM 1101 | 5”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government (s) | 3 | POLS 1101 | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government, Politics (s) | 3 | POLS 1111 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History (f) | 3 | History elective | 8”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History (f) | 3 | HIST1114, 1115 | 8”
  - … 11 more rows
### `a75a0ca2143b771a` Inver Hills Community College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.inverhills.edu/admissions/enrollment-academic-options/adult-learners/credit-for-prior-learning/ib-equivalencies/ (sha256 7468065ab114)
- checks: {"distinct_exams": 20, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL 4-7]:  ⟵ “Biology (HL) | 4-7 | BIOL 1120 | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4-7]:  ⟵ “Business and Management (HL) | 4-7 | BUS 1101 | 3”
  - equivalencies[IB-CHEMISTRY-HL|HL 4-7]:  ⟵ “Chemistry (HL) | 4-7 | CHEM 1061 | 5”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 4-7]:  ⟵ “Computer Science (HL) | 4-7 | CS 1118 | 4”
  - equivalencies[IB-ECONOMICS-HL|HL 4-7]:  ⟵ “Economics (HL) | 4-7 | ECON 1105 and 1106 | 8”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-HL|HL 4-7]:  ⟵ “Environmental Systems (HL) | 4-7 | BIOL 1116 | 2”
  - equivalencies[IB-GEOGRAPHY-HL|HL 4-7]:  ⟵ “Geography (HL) | 4-7 | Goal 5; counts toward two requirements | 8”
  - equivalencies[IB-HISTORY-HL|HL 4-7]:  ⟵ “History of Africa (HL) | 4-7 | Goals 5 and 8 | 8”
  - equivalencies[IB-HISTORY-HL|HL 4-7]:  ⟵ “History of the Americas (HL) | 4-7 | Goals 5 and 8; counts toward two requirements | 8”
  - equivalencies[IB-HISTORY|4-7]:  ⟵ “History of Europe | 4-7 | Goals 5 and 8; counts toward two requirements | 8”
  - equivalencies[IB-HISTORY-HL|HL 4-7]:  ⟵ “History of the Islamic World (HL) | 4-7 | General elective | 8”
  - equivalencies[IB-FRENCH-HL|HL 4-7]:  ⟵ “French (HL) | 4-7 | FREN 1101 & 1102 | 10”
  - equivalencies[IB-GERMAN-HL|HL 4-7]:  ⟵ “German (HL) | 4-7 | GERM 1101 & 1102 | 10”
  - equivalencies[IB-SPANISH-HL|HL 4-7]:  ⟵ “Spanish (HL) | 4-7 | SPAN 1101 & 1102 | 10”
  - equivalencies[IB-MUSIC-HL|HL 4-7]:  ⟵ “Music (HL) | 4-7 | MUSC 1110 and MUSC elective | 8”
  - equivalencies[IB-MUSIC-SL|SL 4-7]:  ⟵ “Music Composition (SL) | 4-7 | MUSC 1145 | 3”
  - equivalencies[IB-PHILOSOPHY-HL|HL 4-7]:  ⟵ “Philosophy (HL) | 4-7 | PHIL 1110 and PHIL elective | 8”
  - equivalencies[IB-PHYSICS-HL|HL 4-7]:  ⟵ “Physics (HL) | 4-7 | PHYS 1030 (36) | 4”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 4-7]:  ⟵ “Psychology (HL) | 4-7 | Goal 5; counts for two requirements | 8”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|HL 4-7]:  ⟵ “Social Anthropology (HL) | 4-7 | SOC 1100 and ANTH elective | 8”
  - equivalencies[IB-THEATRE-HL|HL 4-7]:  ⟵ “Theatre Arts (HL) | 4-7 | Goal 6a; counts for two requirements | 8”
  - equivalencies[IB-VISUAL-ARTS-HL|HL 4-7]:  ⟵ “Visual Arts (HL) | 4-7 | ART 1100, ART elective | 8”
### `d3f6cae7c44a243b` Lake Superior College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.lsc.edu/current-students/records-registration/transfer-into-lsc/common-questions-about-transferring-into-lsc/ (sha256 10b494306fa4)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Health programs require a grade of C or better in all courses, therefore grades of C- or below do not transfer.”
### `012637cab7360488` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Intro to Educational Psychology | 50 | 4 | Goal 5: History and the Social and Behavioral Sciences”
### `01fe5ed21932424d` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 40 ⟵ “Information Systems | 40 | 4 | Elective”
### `0faa2495b74ab474` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 65 ⟵ “Spanish with Writing Level 2 | 65 | 9 | Goal 8: Global Perspective”
### `0fc8109b644931b9` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Analyze and Interpret Literature | 50 | 3 | Goal 6: The Humanities and Fine Arts”
### `111528f7f684001c` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “French – College Level 1 | 50 | 6 | Goal 8: Global Perspective”
### `16ddba508bb6cbab` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Precalculus | 50 | 4 | Goal 4: Mathematical or Logical Reasoning”
### `26d70a992ca443f7` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Financial Accounting | 50 | 4 | Elective”
### `29f8931889ac861f` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Humanities | 50 | 3 | Goal 6: The Humanities and Fine Arts”
### `2f0534fd1018ee22` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “College Mathematics | 50 | 4 | Goal 4: Mathematical or Logical Reasoning”
### `34348d81a22a26b4` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 60 ⟵ “German – College Level 2 (January 2008–December 2014) | 60 | 12 | Goal 8: Global Perspective”
### `3e8aaa0bfc99ebc9` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Human Growth & Development | 50 | 3 | Goal 5: History and the Social and Behavioral Sciences”
### `3eb2576f3789029f` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Principles of Accounting (May 1–July 2007) | 50 | 6 | Elective”
### `3f0cc5d946704209` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “College Mathematics (May 2001–April 2023) | 50 | 6 | Goal 4: Mathematical or Logical Reasoning”
### `4997e89233d87aff` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “College Composition Modular | 50 | 3 | Goal 1: Communication”
### `4c0bc904e573ee49` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Biology | 50 | 6 | Goal 3: Natural Sciences”
### `533a56ac759056a0` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Principles of Microeconomics | 50 | 3 | Goal 5: History and the Social and Behavioral Sciences”
### `57935cfb03a7ad0d` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Principles of Macroeconomics | 50 | 3 | Goal 5: History and the Social and Behavioral Sciences”
### `5fd44ef2c9dc50a8` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Natural Sciences | 50 | 6 | Goal 3: Natural Sciences”
### `64ccf3fa6a735963` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Principles of Management | 50 | 4 | Elective”
### `674e894f0cdcc269` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 60 ⟵ “German – College Level 2 | 60 | 9 | Goal 8: Global Perspective”
### `755b4794a869290f` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Introductory Business Law | 50 | 4 | Elective”
### `82c3e870823d0547` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 63 ⟵ “Spanish – College Level 2 (August 2007–December 2014) | 63 | 12 | Goal 8: Global Perspective”
### `8a20773d369d3312` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Western Civilization I | 50 | 3 | Goal 5: History and the Social and Behavioral Sciences”
### `8b829536b598ca7d` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “College Algebra | 50 | 4 | Goal 4: Mathematical or Logical Reasoning”
### `a0cae3f9080fe9ab` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Information Systems (CLEP 0022) *5 year sunset* | 50 | 4 | Elective”
### `a960746ce2d03e95` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 59 ⟵ “French – College Level 2 (January 2008–December 2014) | 59 | 12 | Goal 8: Global PerspectiveGoal 6: The Humanities and Fine Arts | ”
### `a9c9d1b7c2f29690` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Calculus | 50 | 4 | Goal 4: Mathematical or Logical Reasoning”
### `b096f58d000676ea` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Information Systems and Computer Apps (May 2007–December 2010) | 50 | 3 | Elective”
### `b0e5458412970e85` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “American Literature | 50 | 3 | Goal 6: The Humanities and Fine Arts”
### `b1bba841c1585d16` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Introductory Psychology | 50 | 4 | Goal 5: History and the Social and Behavioral Sciences”
### `b22a6395f98bc616` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Information Systems (CLEP 0022 through December 2010) | 50 | 3 | Elective”
### `ba454b2d1c94f984` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “College Composition | 50 | 6 | Goal 1: Communication”
### `c0bc06b3c96116a3` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “English Literature | 50 | 3 | Goal 6: The Humanities and Fine Arts”
### `c22179e96c88ce43` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Principles of Marketing | 50 | 4 | Elective”
### `d256dcf3aba3dce4` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Social Sciences and History | 50 | 6 | Goal 5: History and the Social and Behavioral Sciences”
### `d270f0f10fc6cbc1` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 63 ⟵ “Spanish – College Level 2 | 63 | 9 | Goal 8: Global Perspective”
### `da4d9ccefa8e0516` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “History of the US I: to 1877 | 50 | 3 | Goal 5: History and the Social and Behavioral Sciences”
### `dbdfc803b88b6ca7` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “American Government | 50 | 4 | Goal 9: Ethical and Civic Responsibility Goal 5: History and the Social and Behavioral Sciences”
### `e95c5ae0c922a53e` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “History of the US: 1865 – Present | 50 | 3 | Goal 5: History and the Social and Behavioral Sciences”
### `ef211aefd61b465b` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Western Civilization II | 50 | 3 | Goal 5: History and the Social and Behavioral Sciences”
### `f0869a9dfd443b0d` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Chemistry | 50 | 6 | Goal 3: Natural Sciences”
### `f0da335676ad2537` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Introductory Sociology | 50 | 3 | Goal 7: Human Diversity Goal 5: History and the Social and Behavioral Sciences”
### `f29f4342fbe6e5de` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 59 ⟵ “French – College Level 2 | 59 | 9 | Goal 8: Global PerspectiveGoal 6: The Humanities and Fine Arts”
### `f5fc08df350bfe4d` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Spanish with Writing Level 1 | 50 | 6 | Goal 8: Global Perspective”
### `f89ca5c698584921` Metropolitan State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- checks: {"thresholds": null}
  - test_requirement: 50 ⟵ “Spanish – College Level 1 | 50 | 6 | Goal 8: Global Perspective”
### `m9492cb3cc333f32` Minneapolis College of Art and Design — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mcad.edu/index%2ephp/admissions-aid/undergraduate-admissions-and-aid/transfer-mcad (sha256 807273027045)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Transfer-Credit Evaluation While we are selective with transfer credits, we may accept up to 30 liberal arts credits and up to 33 studio arts credits with a grade of “C” or better from other regionally-accredited post-secondary institutions and pre-college programs.”
  - min_grade: C ⟵ “Transfer-Credit Evaluation While we are selective with transfer credits, we may accept up to 30 liberal arts credits and up to 33 studio arts credits with a grade of “C” or better from other regionally-accredited post-secondary institutions and pre-college programs.”
### `b275adc0a0ad284c` Minnesota North College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://minnesotanorth.edu/admissions/types-of-students/transfer-students/ (sha256 ff3f576d56ed)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “While D grades transfer, some specialized/occupational/technical programs require courses to have a grade of C or higher to fulfill requirements.”
### `9d2cb9b355f4e6b9` Minnesota West Community and Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mnwest.edu/admissions-and-aid/pseo-dual-enrollment/ (sha256 5aa57a4309d1)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 3}
  - eligibility_tier: 2.0 ⟵ “HS GPA of 2.0 or higher”
  - eligibility_tier: 2.0 ⟵ “If the 2.0 GPA isn’t met, a petition form may be completed with an academic advisor”
  - eligibility_tier: 2.6 ⟵ “Course requirements for reading-based courses (2.6 GPA) and math-based courses (2.8”
  - max_credit_hours_per_term: 16 ⟵ “Each semester, you may register for up to 16 credits. You must be enrolled less than”
### `cf6a999eccf41f9d` Minnesota West Community and Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mnwest.edu/admissions-and-aid/transfer-services/transfer-in.php (sha256 48a5b2a67c9f)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Students planning to transfer and who have made the proper selection of course work, and maintained grades of "C" or better, may expect to transfer without loss of credit.”
### `m9e40b6b5b4c4f98` Northwestern Health Sciences University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.nwhealth.edu/admissions/transfer-students/massage-therapy/ (sha256 71d017812632)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Courses may transfer to Northwestern if you have received grades of C or better.”
  - min_grade: C ⟵ “Courses may transfer to Northwestern if you have received grades of C or better.”
### `5d2b8bbfaaa806e5` Pine Technical & Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://pine.edu/academics/transfer/ (sha256 f336a472c61c)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Generally, transfer credit is considered only for courses that fulfill Pine Technical and Community College graduation and program requirements, and have been completed with a grade of C or better.”
### `525411855638e335` Rochester Community and Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.rctc.edu/academics/credit-for-prior-learning/ (sha256 f8677db88ad3)
- checks: {"distinct_exams": 29, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | POLS 1615 | 5 & 9”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 | ENGL 2273 & 2274 | 6 & 7”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | 3 | ENGL elective | 6”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 3 | BIOL elective | na”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 5 | MATH 1127 | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 4 | CHEM elective | na”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | MATH 1115 | 4”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 4 | ENGL 1117 | 1”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 4 | ENGL 1117 | 1”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | MATH 1111 | 4”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 | ENGL elective | 6”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 4 | ACCT 2217 | na”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language Level 1 & 2 | 50 | 4 | FREN 1101 | 6 & 8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “French Language | 62 | 8 | FREN 1101 & 1102 | 6 & 8”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language Level 1 & 2 | 50 | 4 | Elective | 6 & 8”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “German Language | 63 | 8 | Elective | 6 & 8”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PSYC 2626 | 5 & 7”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | HUM elective | 6”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | 3 | COMP elective | na”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Intro Business Law | 50 | 3 | BUS 2210 | na”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology | 50 | 3 | PSYC elective | 5”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Intro to Psychology | 50 | 4 | PSYC 2618 | 5 & 7”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Intro to Sociology | 50 | 3 | SOC 1614 | 5 & 7”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | 3 | elective | na”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 4 | MATH 1117 | 4”
  - … 7 more rows
### `1dc125494e02c2cd` Rochester Community and Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.rctc.edu/academics/transfer/minnesota-transfer-curriculum/ (sha256 a21eed0530ea)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “While D grades transfer, some specialized/occupational/technical programs require courses to have a grade of C or higher to fulfill requirements.”
### `a73b196af2491807` Saint Cloud State University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.stcloudstate.edu/financialaid/cost-of-attendance.aspx (sha256 d9be5373f0ab)
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 9960 ⟵ “Tuition | $4,980 | $9,960 | $21,132”
  - column:Fees: 1496 ⟵ “Fees | $748 | $1,496 | $1,496”
  - column:Tuition and Fees Total: 11456 ⟵ “Tuition and Fees Total | $5,728 | $11,456 | $11,456”
  - column:Housing and Meal Plan: 11306 ⟵ “Housing and Meal Plan | $5,653 | $11,306 | $11,306”
  - column:Books and Supplies: 1400 ⟵ “Books and Supplies | $700 | $1,400 | $1,400”
  - column:Transportation: 1566 ⟵ “Transportation | $783 | $1,566 | $2,088”
  - column:Personal Expenses: 2592 ⟵ “Personal Expenses | $1,296 | $2,592 | $2,592”
  - column:Federal Loan Fees (average): 92 ⟵ “Federal Loan Fees (average) | $46 | $92 | $92”
  - column:Total:: 28412 ⟵ “Total: | $14,206 | $28,412 | $28,934”
### `b7d606357512f8d2` Saint Mary's University of Minnesota — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.smumn.edu/admissions/undergraduate/college-credit-in-high-school/dual-credit-online (sha256 19760e8d0842)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Minimum GPA of 3.0”
  - eligibility_tier: 3.0 ⟵ “Meet Saint Mary’s academic criteria, minimum 3.0 GPA”
### `e4e48daa1d5b256f` Southwest Minnesota State University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.smsu.edu/admission/free-tuition.html (sha256 26319ba23d08)
- checks: {"thresholds": null}
  - award_tiers: [{'cumulative high school gpa': '3.90 or Higher', 'amount_text': '$3,500'}, {'cumulative high school gpa': '3.60–3.89', 'amount_text': '$3,000'}, {'cumulative high school gpa': '3.30–3.59', 'amount_text': '$2,500'}, {'cumulative high school gpa': '3.00–3.29', 'amount_text': '$2,000'}, {'cumulative high school gpa': '2.75–2.99', 'amount_text': '$1,000'}] ⟵ “Cumulative High School GPA | Award for One Academic Year || 3.90 or Higher | $3,500 || 3.60–3.89 | $3,000 || 3.30–3.59 | $2,500 || 3.00–3.29 | $2,000 || 2.75–2.99 | $1,000”
  - gpa_requirement: Tiered by Cumulative High School GPA: 3.90 or Higher → $3,500; 3.60–3.89 → $3,000; 3.30–3.59 → $2,500; 3.00–3.29 → $2,000; 2.75–2.99 → $1,000 ⟵ “Cumulative High School GPA | Award for One Academic Year || 3.90 or Higher | $3,500 || 3.60–3.89 | $3,000 || 3.30–3.59 | $2,500 || 3.00–3.29 | $2,000 || 2.75–2.99 | $1,000”
### `b92a1727223dcd1a` Southwest Minnesota State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.smsu.edu/campuslife/financialaid/budget.html (sha256 58f7a0f6bbb0)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition and Fees (at 12-18 credits): 5758 ⟵ “Tuition and Fees (at 12-18 credits) | $5,758”
  - column:Housing and Food Estimate: 5925 ⟵ “Housing and Food Estimate | $5,925”
  - column:Books, materials, supplies and equipment (Approximate Cost for Undergraduate Students): 600 ⟵ “Books, materials, supplies and equipment (Approximate Cost for Undergraduate Students) | $600”
  - column:Total Estimated Charges for One Semester: 12283 ⟵ “Total Estimated Charges for One Semester | $12,283”
  - column:Total Direct Costs: 11683 ⟵ “Total Direct Costs | $11,683”
### `1854d05c4680f145` St Catherine University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stkate.edu/admission-and-aid/financial-aid/cost-of-attendance (sha256 2fd17cc52d87)
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition (based on banded rate): 53888 ⟵ “Tuition (based on banded rate) | $52,320 | $53,888”
  - on_campus:Student Activity Fee: 294 ⟵ “Student Activity Fee | $294 | $294”
  - on_campus:Technology Fee: 600 ⟵ “Technology Fee | $600 | $600”
  - on_campus:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 1000 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,000 | $1,000”
  - on_campus:Housing: 8350 ⟵ “Housing | $8,000 | $8350”
  - on_campus:Food: 4742 ⟵ “Food | $4,650 | $4,742”
  - on_campus:Personal Expenses, Miscellaneous: 2468 ⟵ “Personal Expenses, Miscellaneous | $2,420 | $2,468”
  - on_campus:Transportation: 460 ⟵ “Transportation | $460 | $460”
  - on_campus:TOTAL: 71872 ⟵ “TOTAL | $69,814 | $71,872”
### `30b94411cf32c8ee` St Catherine University — transfer_policies 2026-27 [new] (labeled_in_heading)
- source: https://catalog.stkate.edu/policies/stu-acad/undg/transfer-credit/transfer/courses/ (sha256 eaf147776fb5)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “To be accepted, transfer course work must be taken at the college level from an institutionally accredited college or university and must carry a grade of C- or better.”
### `b01622b0760ff1b9` St Cloud Technical and Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://sctcc.edu/about-us/leadership/policies-and-procedures/s38-transfer-credit-policy (sha256 0cfa16e748d3)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Please note that while D grades may transfer, some programs require a grade of C or higher for all courses to fulfill requirements.”
### `0c19aa5fc6121299` St Olaf College — awards 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/merit-scholarships/ (sha256 9251430a3930)
- checks: {"thresholds": null}
  - award_amount_text: $3,000-4,000 ⟵ “Campus Living Scholarship* | $3,000-4,000 | No additional steps are necessary. All new students receiving an Academic Merit Scholarship will also receive the Campus Living Scholarship.”
### `27268271cd42f65f` St Olaf College — awards 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/merit-scholarships/ (sha256 9251430a3930)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 for new students ⟵ “Theater Scholarships | $5,000 for new students | Requires additional application. Please click the link for more information.”
### `39cd3edef5030fa6` St Olaf College — awards 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/merit-scholarships/ (sha256 9251430a3930)
- checks: {"thresholds": null}
  - award_amount_text: $2,000-$12,000 ⟵ “Music Scholarships | $2,000-$12,000 | Requires additional application. Please click the link for more information.”
### `82ab76dbf9642748` St Olaf College — awards 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/merit-scholarships/ (sha256 9251430a3930)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 for new students ⟵ “Dance Scholarships | $5,000 for new students | Requires additional application. Please click the link for more information.”
### `b29267a2affb1761` St Olaf College — awards 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/merit-scholarships/ (sha256 9251430a3930)
- checks: {"thresholds": null}
  - award_amount_text: $17,000-$34,000 ⟵ “Academic Scholarships*(Buntrock, Regents, Presidential, Dean’s, Faculty, St. Olaf and Transfer Scholarships) | $17,000-$34,000 | No additional steps are necessary. All students will be automatically considered for academic scholarships.”
### `c8844820bcd067ec` St Olaf College — awards 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/merit-scholarships/ (sha256 9251430a3930)
- checks: {"thresholds": null}
  - award_amount_text: $5,000-$35,000 ⟵ “Transfer Student Scholarships | $5,000-$35,000 | No additional steps are necessary. Only available to transfer students.”
### `fbfcb5b27ca639a0` St Olaf College — awards 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/merit-scholarships/ (sha256 9251430a3930)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 for new students ⟵ “Art Scholarships | $5,000 for new students | Requires additional application. Please click the link for more information.”
### `8423e755126e5a0b` St Olaf College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://wp.stolaf.edu/stuacct/compfee-2/ (sha256 2b5d8515b0d9)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 65700 ⟵ “Tuition | $32,850 | $32,850 | $65,700”
  - column:Housing*: 7150 ⟵ “Housing* | $3,575 | $3,575 | $7,150”
  - column:Meal Plan**: 7850 ⟵ “Meal Plan** | $3,925 | $3,925 | $7,850”
  - column:Activities Fee***: 500 ⟵ “Activities Fee*** | $250 | $250 | $500”
  - column:Total: 81200 ⟵ “Total | $40,600 | $40,600 | $81,200”
### `145519754688093c` The College of Saint Scholastica — awards 2026-27 [new] (labeled_in_source)
- source: https://www.css.edu/admissions-and-aid/financial-aid/scholarships-and-grants/first-year-student-scholarships-and-grants/ (sha256 9ebc1aa90770)
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: 2.5 – 2.749 ⟵ “2.5 – 2.749 | $24,000”
  - award_amount_text: $24,000 ⟵ “2.5 – 2.749 | $24,000”
### `7f72406ed68f803d` The College of Saint Scholastica — awards 2026-27 [new] (labeled_in_source)
- source: https://www.css.edu/admissions-and-aid/financial-aid/scholarships-and-grants/first-year-student-scholarships-and-grants/ (sha256 9ebc1aa90770)
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: 3.85 – 3.999 ⟵ “3.85 – 3.999 | $28,000”
  - award_amount_text: $28,000 ⟵ “3.85 – 3.999 | $28,000”
### `8766abbb52d2ff85` The College of Saint Scholastica — awards 2026-27 [new] (labeled_in_source)
- source: https://www.css.edu/admissions-and-aid/financial-aid/scholarships-and-grants/first-year-student-scholarships-and-grants/ (sha256 9ebc1aa90770)
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: 3.25 – 3.849 ⟵ “3.25 – 3.849 | $27,000”
  - award_amount_text: $27,000 ⟵ “3.25 – 3.849 | $27,000”
### `94997a583a1eaf46` The College of Saint Scholastica — awards 2026-27 [new] (labeled_in_source)
- source: https://www.css.edu/admissions-and-aid/financial-aid/scholarships-and-grants/first-year-student-scholarships-and-grants/ (sha256 9ebc1aa90770)
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: 2.75 – 3.249 ⟵ “2.75 – 3.249 | $26,000”
  - award_amount_text: $26,000 ⟵ “2.75 – 3.249 | $26,000”
### `ed9c277d948b5abe` The College of Saint Scholastica — awards 2026-27 [new] (labeled_in_source)
- source: https://www.css.edu/admissions-and-aid/financial-aid/scholarships-and-grants/first-year-student-scholarships-and-grants/ (sha256 9ebc1aa90770)
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: 4.0 and above ⟵ “4.0 and above | $30,000”
  - award_amount_text: $30,000 ⟵ “4.0 and above | $30,000”
### `172c162e004fc1a3` The College of Saint Scholastica — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://resources.css.edu/admissions/docs/clep_exam_information.pdf (sha256 8feddd2404e8)
- checks: {"distinct_exams": 28, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                              50               4       Social Sciences        n/a”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                              50               4       Literature             n/a”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature              50               4       Literature             n/a”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                          50               4       Natural Science        n/a”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                         50               4       Mathematics            n/a”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                                        50               4       Natural Science        CHM 1110”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                                  50               4       Mathematics            n/a”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                               50              4        Literature             n/a”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting                             50              4        n/a                    ACC 2210”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language Level I                          50              8        World Language         n/a”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language Level II                         59              8        World Language         n/a”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language Level I                          50              8        World Language         n/a”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language Level II                         60              8        World Language         n/a”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I                   50              4        History                n/a”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II                  50              4        History                n/a”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development                       50              4        Social Sciences        PSY 2208”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Apps              50              4        n/a                    CIS 3205”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology           50              4        n/a                    n/a”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law                        50              4        n/a                    n/a”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                          50              4        Social Sciences        n/a”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                           50              4        Social Sciences        SOC 1125”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences                                 50              4        Natural Science        n/a”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                                      50              4        Mathematics            n/a”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management                         50              4        n/a                    MGT 2120”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing                          50              4        n/a                    MKT 2320”
  - … 6 more rows
### `afa26dd6389956ae` University of Minnesota-Crookston — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://crk.umn.edu/financial-aid-and-scholarships/cost-attendance (sha256 d5145a09fd79)
- checks: {"columns": 1, "rows": 3}
  - on_campus:Tuition/fees: 14364 ⟵ “Tuition/fees | $14,364”
  - on_campus:Books/supplies*: 800 ⟵ “Books/supplies* | $800”
  - on_campus:Housing/food: 11806 ⟵ “Housing/food | $11,806”
### `ec43fa73d47e0c25` University of Minnesota-Duluth — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://onestop.d.umn.edu/finances/costs/cost-attendance (sha256 d11a1515a1bd)
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition*: 13985 ⟵ “Tuition* | $13,985 | $13,985”
  - on_campus:Required fees*: 1825 ⟵ “Required fees* | $1,825 | $1,825”
  - on_campus:Housing**: 5810 ⟵ “Housing** | $5,810 | $6,975”
  - on_campus:Food**: 6500 ⟵ “Food** | $6,500 | $4,285”
  - on_campus:Books, course materials, supplies and equipment**: 760 ⟵ “Books, course materials, supplies and equipment** | $760 | $760”
  - on_campus:Miscellaneous personal expenses: 2000 ⟵ “Miscellaneous personal expenses | $2,000 | $2,000”
  - on_campus:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,000”
  - on_campus:Federal loan fees: 110 ⟵ “Federal loan fees | $110 | $110”
  - on_campus:Total (fall and spring): 31990 ⟵ “Total (fall and spring) | $31,990 | $30,940”
  - off_campus_not_with_family:Tuition*: 13985 ⟵ “Tuition* | $13,985 | $13,985”
  - off_campus_not_with_family:Required fees*: 1825 ⟵ “Required fees* | $1,825 | $1,825”
  - off_campus_not_with_family:Housing**: 6975 ⟵ “Housing** | $5,810 | $6,975”
  - off_campus_not_with_family:Food**: 4285 ⟵ “Food** | $6,500 | $4,285”
  - off_campus_not_with_family:Books, course materials, supplies and equipment**: 760 ⟵ “Books, course materials, supplies and equipment** | $760 | $760”
  - off_campus_not_with_family:Miscellaneous personal expenses: 2000 ⟵ “Miscellaneous personal expenses | $2,000 | $2,000”
  - off_campus_not_with_family:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,000”
  - off_campus_not_with_family:Federal loan fees: 110 ⟵ “Federal loan fees | $110 | $110”
  - off_campus_not_with_family:Total (fall and spring): 30940 ⟵ “Total (fall and spring) | $31,990 | $30,940”
### `f6378878f61cfb52` University of Minnesota-Duluth — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://onestop.d.umn.edu/finances/costs/cost-attendance (sha256 d11a1515a1bd)
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition*: 13985 ⟵ “Tuition* | $13,985 | $13,985 | $13,985”
  - on_campus:Required fees*: 1825 ⟵ “Required fees* | $1,825 | $1,825 | $1,825”
  - on_campus:Housing**: 5810 ⟵ “Housing** | $5,810 | $6,975 | $2,700”
  - on_campus:Food**: 6500 ⟵ “Food** | $6,500 | $4,285 | $1,250”
  - on_campus:Books, course materials, supplies and equipment**: 760 ⟵ “Books, course materials, supplies and equipment** | $760 | $760 | $760”
  - on_campus:Miscellaneous personal expenses: 2000 ⟵ “Miscellaneous personal expenses | $2,000 | $2,000 | $2,000”
  - on_campus:Transportation: 330 ⟵ “Transportation | $330 | $330 | $950”
  - on_campus:Federal loan fees: 110 ⟵ “Federal loan fees | $110 | $110 | $110”
  - on_campus:Total (fall and spring): 31320 ⟵ “Total (fall and spring) | $31,320 | $30,270 | $23,580”
  - off_campus_not_with_family:Tuition*: 13985 ⟵ “Tuition* | $13,985 | $13,985 | $13,985”
  - off_campus_not_with_family:Required fees*: 1825 ⟵ “Required fees* | $1,825 | $1,825 | $1,825”
  - off_campus_not_with_family:Housing**: 6975 ⟵ “Housing** | $5,810 | $6,975 | $2,700”
  - off_campus_not_with_family:Food**: 4285 ⟵ “Food** | $6,500 | $4,285 | $1,250”
  - off_campus_not_with_family:Books, course materials, supplies and equipment**: 760 ⟵ “Books, course materials, supplies and equipment** | $760 | $760 | $760”
  - off_campus_not_with_family:Miscellaneous personal expenses: 2000 ⟵ “Miscellaneous personal expenses | $2,000 | $2,000 | $2,000”
  - off_campus_not_with_family:Transportation: 330 ⟵ “Transportation | $330 | $330 | $950”
  - off_campus_not_with_family:Federal loan fees: 110 ⟵ “Federal loan fees | $110 | $110 | $110”
  - off_campus_not_with_family:Total (fall and spring): 30270 ⟵ “Total (fall and spring) | $31,320 | $30,270 | $23,580”
  - with_parents_or_family:Tuition*: 13985 ⟵ “Tuition* | $13,985 | $13,985 | $13,985”
  - with_parents_or_family:Required fees*: 1825 ⟵ “Required fees* | $1,825 | $1,825 | $1,825”
  - with_parents_or_family:Housing**: 2700 ⟵ “Housing** | $5,810 | $6,975 | $2,700”
  - with_parents_or_family:Food**: 1250 ⟵ “Food** | $6,500 | $4,285 | $1,250”
  - with_parents_or_family:Books, course materials, supplies and equipment**: 760 ⟵ “Books, course materials, supplies and equipment** | $760 | $760 | $760”
  - with_parents_or_family:Miscellaneous personal expenses: 2000 ⟵ “Miscellaneous personal expenses | $2,000 | $2,000 | $2,000”
  - with_parents_or_family:Transportation: 950 ⟵ “Transportation | $330 | $330 | $950”
  - … 2 more rows
### `mb954e2b0f735da0` University of Minnesota-Duluth — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.d.umn.edu/apply/transfer-students (sha256 de3b9032f58a)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: D ⟵ “UMD requires a minimum letter grade of “D” or higher to honor transfer credit for a course.”
  - min_grade: D ⟵ “UMD requires a minimum letter grade of “D” or higher to honor transfer credit for a course.”
### `739c0b066f9b9bc9` University of Minnesota-Morris — awards 2026-27 [new] (source_unlabeled)
- source: https://morris.umn.edu/costs-aid/scholarships/academic-achievement-awards (sha256 99702a6b97cf)
- checks: {"thresholds": null}
  - award_amount_text: $20,000 over four years ($5,000 per year) ⟵ “Tier 1 | 3.90 - 4.00 | $20,000 over four years ($5,000 per year)”
  - gpa_requirement: 3.90 - 4.00 ⟵ “Tier 1 | 3.90 - 4.00 | $20,000 over four years ($5,000 per year)”
### `9677f6680d42fb33` University of Minnesota-Morris — awards 2026-27 [new] (source_unlabeled)
- source: https://morris.umn.edu/costs-aid/scholarships/academic-achievement-awards (sha256 99702a6b97cf)
- checks: {"thresholds": null}
  - award_amount_text: $8,000 over four years ($2,000 per year) ⟵ “Tier 3 | 3.50 - 3.74 | $8,000 over four years ($2,000 per year)”
  - gpa_requirement: 3.50 - 3.74 ⟵ “Tier 3 | 3.50 - 3.74 | $8,000 over four years ($2,000 per year)”
### `cf5f7a54cbf6910c` University of Minnesota-Morris — awards 2026-27 [new] (source_unlabeled)
- source: https://morris.umn.edu/costs-aid/scholarships (sha256 9b2eab47eb3c)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 over four years ($1,000 per year) ⟵ “Tier 4 | 3.25 - 3.49 | $4,000 over four years ($1,000 per year)”
  - gpa_requirement: 3.25 - 3.49 ⟵ “Tier 4 | 3.25 - 3.49 | $4,000 over four years ($1,000 per year)”
### `e02e045223665856` University of Minnesota-Morris — awards 2026-27 [new] (source_unlabeled)
- source: https://morris.umn.edu/costs-aid/scholarships/scholarship-search (sha256 c21071850f23)
- checks: {"thresholds": null}
  - award_amount_text: $14,000 over four years ($3,500 per year) ⟵ “Tier 2 | 3.75 - 3.89 | $14,000 over four years ($3,500 per year)”
  - gpa_requirement: 3.75 - 3.89 ⟵ “Tier 2 | 3.75 - 3.89 | $14,000 over four years ($3,500 per year)”
### `a9c0573018f223fb` University of Minnesota-Morris — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://morris.umn.edu/admissions/transferring-credit/international-baccalaureate-ib (sha256 7c706b3b568c)
- checks: {"distinct_exams": 13, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “Biology | 5-7 | 8 |  | Sci, Sci-L”
  - equivalencies[IB-CHEMISTRY|5-7]:  ⟵ “Chemistry | 5-7 | 10 | Substitutes for CHEM 1101 and 1102 | Sci, Sci-L”
  - equivalencies[IB-COMPUTER-SCIENCE|5-7]:  ⟵ “Computer Science | 5-7 | 8 |  | M/SR”
  - equivalencies[IB-ECONOMICS|5-7]:  ⟵ “Economics | 5-7 | 8 | Substitutes for ECON 1101 | SS”
  - equivalencies[IB-FRENCH|5-7]:  ⟵ “French | 5-7 | 10 | Substitutes for FREN 2001, 2002; FL proficiency, 2 credits HUM | WL, GP, HUM”
  - equivalencies[IB-GERMAN|5-7]:  ⟵ “German | 5-7 | 10 | Substitutes for GER 2001, 2002; FL proficiency, 2 credits HUM | WL, GP, HUM”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History – America | 5-7 | 8 |  | HIST”
  - equivalencies[IB-MUSIC|5-7]:  ⟵ “Music | 5-7 | 8 | 5 credits ArtP, 3 credits FA | ArtP, FA”
  - equivalencies[IB-PHILOSOPHY|5-7]:  ⟵ “Philosophy | 5-7 | 8 |  | HUM”
  - equivalencies[IB-PHYSICS|5-7]:  ⟵ “Physics | 5-7 | 8 | Substitutes for PHYS 1101 and 1102 | Sci, Sci-L”
  - equivalencies[IB-PSYCHOLOGY|5-7]:  ⟵ “Psychology | 5-7 | 8 | Substitutes for PSY 1051 | SS”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5-7]:  ⟵ “Social and Cultural Anthropology | 5-7 | 8 |  | SS”
  - equivalencies[IB-SPANISH|5-7]:  ⟵ “Spanish | 5-7 | 10 | Substitutes for SPAN 2001, 2002, 3111; WL proficiency | WL, GP, HUM”
### `f6903e15bee9f095` University of Minnesota-Morris — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://morris.umn.edu/admissions/transferring-credit/advanced-placement-ap (sha256 e5c748c74529)
- checks: {"distinct_exams": 28, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | 4 | Elective in African and Black American Studies Minor | HDE”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 4 |  | FA”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio – Drawing | 3 | 4 | Portfolio evaluation required for use in major | ArtP”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art Studio – 2-D Design | 3 | 2 | Portfolio evaluation required for use in major | ArtP”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art Studio – 3-D Design | 3 | 2 | Portfolio evaluation required for use in major | ArtP”
  - equivalencies[AP-BIOLOGY|4 or 5]:  ⟵ “Biology | 4 or 5 | 4 + 4 | Substitutes for Biology 1111 and four additional credits | Sci & Sci-L”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 8 | Biology with Lab; may not count in major | Sci-L”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 5 | Substitutes for CHEM 1101 | Sci-L”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “Chemistry | 4 or 5 | 5 + 5 | Substitutes for CHEM 1101 – 1102 | Sci-L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Lang/Culture | 3 | 4 + 4 | Proficiency for WL, eight 2000- level credits | FL, GP”
  - equivalencies[AP-COMPUTER-SCIENCE-A|5]:  ⟵ “Computer Science A | 5 | 2 | Score of five substitutes for CSCI 1301 | M/SR”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3 or 4]:  ⟵ “Computer Science A | 3 or 4 | 2 | Students should speak with a CSCI faculty member | M/SR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4 or 5]:  ⟵ “English Language/Comp | 4 or 5 | 4 | Substitutes for ENGL 1007 | WLA”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language/Comp | 3 | 4 | 1000-level English elective | GE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4 or 5]:  ⟵ “English Lit/Comp | 4 or 5 | 4 | Substitutes for ENGL 1007 | WLA”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Lit/Comp | 3 | 4 | 1000-level English elective | HUM”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 4 | 1000-level environmental science elective | SE”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Lang/Culture | 3 | 4 + 4 | Proficiency for WL; Substitutes for FREN 2001, 2002 | WL, GP”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Literature | 3 | 4 + 4 + 2 | Proficiency for WL; Substitutes for FREN 2001, 2002 and two credits HUM | WL, GP, HUM”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | 4 + 4 | Proficiency for WL; Substitutes for 2001, 2002 | WL, GP”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Lang/Culture | 3 | 4 + 4 | Proficiency for WL; Substitutes for ITAL 2001 and four additional credits | WL,GP”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | 3 | 4 | Proficiency for WL | WL”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 4 | 1000-level economics course (combined with Microeconomics sub ECON 1101) | SS”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 4 | 1000-level economics course (combined with Macroeconomics sub ECON 1101) | SS”
  - equivalencies[AP-CALCULUS-AB|3 or 4]:  ⟵ “Math, Calculus AB | 3 or 4 | 4 | Substitutes for MATH 1021, Survey; with approval may substitute for 1101 | M/SR”
  - … 16 more rows
### `11af5442245990cb` University of Minnesota-Morris — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://morris.umn.edu/admissions/transferring-credit (sha256 94f635f02a01)
- checks: {"fields": ["min_grade"]}
  - min_grade: D ⟵ “Transfer coursework may be accepted from institutions that are regionally accredited; from institutions that provide courses that are intended for transfer to baccalaureate programs; if it’s comparable in nature, content, and level to courses offered by UMN Morris; applicable to the bachelor of arts; or, with the grade of D or above, subject to the restrictions of Morris's degree requirements.”
### `49470dce3d74043b` University of Minnesota-Rochester — awards 2026-27 [new] (source_unlabeled)
- source: https://r.umn.edu/admissions/scholarships-overview (sha256 0b8f2a6de3ae)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “3.00 - 3.24 | Opportunity Grant | $1,000”
  - gpa_requirement: 3.00 - 3.24 ⟵ “3.00 - 3.24 | Opportunity Grant | $1,000”
### `8bd0006ce858b146` University of Minnesota-Rochester — awards 2026-27 [new] (source_unlabeled)
- source: https://r.umn.edu/admissions/scholarships-overview (sha256 04197f1e39cb)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $5,000 ⟵ “4.00 | UMR Scholar | $5,000”
  - gpa_requirement: 4.00 ⟵ “4.00 | UMR Scholar | $5,000”
### `b6610c393b4b34ea` University of Minnesota-Rochester — awards 2026-27 [new] (source_unlabeled)
- source: https://r.umn.edu/admissions/scholarships-overview (sha256 04197f1e39cb)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ⟵ “3.75 - 3.99 | Academic Achievement | $4,000”
  - gpa_requirement: 3.75 - 3.99 ⟵ “3.75 - 3.99 | Academic Achievement | $4,000”
### `c876144822c9c2fe` University of Minnesota-Rochester — awards 2026-27 [new] (source_unlabeled)
- source: https://r.umn.edu/admissions/scholarships-overview (sha256 0b8f2a6de3ae)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “3.50 - 3.74 | Academic Merit Grant | $3,000”
  - gpa_requirement: 3.50 - 3.74 ⟵ “3.50 - 3.74 | Academic Merit Grant | $3,000”
### `d400fcf51ce7e2ad` University of Minnesota-Rochester — awards 2026-27 [new] (source_unlabeled)
- source: https://r.umn.edu/admissions/scholarships-overview (sha256 04197f1e39cb)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “3.25 - 3.49 | Raptor Grant | $2,000”
  - gpa_requirement: 3.25 - 3.49 ⟵ “3.25 - 3.49 | Raptor Grant | $2,000”
### `0189fef1cbb03fb0` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Mathematical Thinking core requirement ⟵ “Mathematics, Further | A, B, or C | MATH 2142 (4 credits) | Mathematical Thinking core requirement”
  - test_requirement: A, B, or C ⟵ “Mathematics, Further | A, B, or C | MATH 2142 (4 credits) | Mathematical Thinking core requirement”
### `023be2b141fab824` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Literature requirement ⟵ “English A Literature HL | 5-7 | 8 credits in ENGL 1999 | Literature requirement”
  - test_requirement: English A Literature HL ⟵ “English A Literature HL | 5-7 | 8 credits in ENGL 1999 | Literature requirement”
### `0a846e7e1969eb85` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 each year for four years ⟵ “Cheryl L. Quinn and Robert J. Buck Scholarship | $3,000 each year for four years | Academic meritDemonstrated financial need”
  - eligibility_summary: Academic meritDemonstrated financial need ⟵ “Cheryl L. Quinn and Robert J. Buck Scholarship | $3,000 each year for four years | Academic meritDemonstrated financial need”
### `0cafce42e493ef91` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: 15 awards of $3,000 - $7,000 per year for up to four years ⟵ “Department of Dance Scholarships | 15 awards of $3,000 - $7,000 per year for up to four years | Audition-based selection plus financial need and/or academic merit”
  - eligibility_summary: Audition-based selection plus financial need and/or academic merit ⟵ “Department of Dance Scholarships | 15 awards of $3,000 - $7,000 per year for up to four years | Audition-based selection plus financial need and/or academic merit”
### `0d1b0c05dcae4688` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: No Liberal Education requirement awarded ⟵ “Business Management HL | 5-7 | 4 credits in MGMT 1999 | No Liberal Education requirement awarded”
  - test_requirement: Business Management HL ⟵ “Business Management HL | 5-7 | 4 credits in MGMT 1999 | No Liberal Education requirement awarded”
### `10f3d98cf228409f` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: 21 awards of $3,000 - $7,000 per year for up to four years ⟵ “Theatre Arts BFA Acting Scholarships | 21 awards of $3,000 - $7,000 per year for up to four years | Financial needAcademic merit”
  - eligibility_summary: Financial needAcademic merit ⟵ “Theatre Arts BFA Acting Scholarships | 21 awards of $3,000 - $7,000 per year for up to four years | Financial needAcademic merit”
### `129762c2e6584f76` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $500-$2,000 single year awards ⟵ “Division of Agricultural Education, Communication and Marketing Scholarship | $500-$2,000 single year awards | Agricultural Education or Agricultural Communication and Marketing majorDemonstrated leadership and community involvementAcademic achievement and potential”
  - eligibility_summary: Agricultural Education or Agricultural Communication and Marketing majorDemonstrated leadership and community involvementAcademic achievement and potential ⟵ “Division of Agricultural Education, Communication and Marketing Scholarship | $500-$2,000 single year awards | Agricultural Education or Agricultural Communication and Marketing majorDemonstrated leadership and community involvementAcademic achievement and potential”
### `138549a17f658ae3` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 each year for four years ⟵ “John and Nancy Peyton Scholarship | $3,000 each year for four years | Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human DevelopmentAcademic potentialFinancial aid considered”
  - eligibility_summary: Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human DevelopmentAcademic potentialFinancial aid considered ⟵ “John and Nancy Peyton Scholarship | $3,000 each year for four years | Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human DevelopmentAcademic potentialFinancial aid considered”
### `1c29514dafc6f10e` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 - $2,500 for one year ⟵ “Victor Gilbertson Scholarship | $1,000 - $2,500 for one year | Academic potentialPreference given to architecture majors”
  - eligibility_summary: Academic potentialPreference given to architecture majors ⟵ “Victor Gilbertson Scholarship | $1,000 - $2,500 for one year | Academic potentialPreference given to architecture majors”
### `1ec740a9c2f6a416` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: No Liberal Education Award ⟵ “Accounting | A, B, or C | ACCT 2050 (4 credits) & ACCT 3001 (3 credits) | No Liberal Education Award”
  - test_requirement: A, B, or C ⟵ “Accounting | A, B, or C | ACCT 2050 (4 credits) & ACCT 3001 (3 credits) | No Liberal Education Award”
### `1fd2eeeea983e92c` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $3,000 each year for four years ⟵ “James & Erma Cabak Scholarship | Approximately $3,000 each year for four years | Based on financial needMN residents with preference for students from Pine or Clearwater Counties”
  - eligibility_summary: Based on financial needMN residents with preference for students from Pine or Clearwater Counties ⟵ “James & Erma Cabak Scholarship | Approximately $3,000 each year for four years | Based on financial needMN residents with preference for students from Pine or Clearwater Counties”
### `2192dc938d7c0985` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Fulfills CLA second language requirement; does NOT fulfill Writing Intensive requirement ⟵ “German HL | 5-7 | 4 credits in GER 3011W | Fulfills CLA second language requirement; does NOT fulfill Writing Intensive requirement”
  - test_requirement: German HL ⟵ “German HL | 5-7 | 4 credits in GER 3011W | Fulfills CLA second language requirement; does NOT fulfill Writing Intensive requirement”
### `226252fc2ad2a957` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 each year for four years ⟵ “College of Education and Human Development Barto Undergraduate Excellence Scholarship | $3,000 each year for four years | Strong academic achievement, demonstrated leadership, creativity, and community involvement”
  - eligibility_summary: Strong academic achievement, demonstrated leadership, creativity, and community involvement ⟵ “College of Education and Human Development Barto Undergraduate Excellence Scholarship | $3,000 each year for four years | Strong academic achievement, demonstrated leadership, creativity, and community involvement”
### `2565bcfc22027419` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Eileen (Teigum) Russell Scholarship | $5,000 each year for four years | Demonstrated Financial Need”
  - eligibility_summary: Demonstrated Financial Need ⟵ “Eileen (Teigum) Russell Scholarship | $5,000 each year for four years | Demonstrated Financial Need”
### `25af0e98d3666915` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: No Liberal Education requirement awarded ⟵ “Information Global Technology HL | 5-7 | 4 credits in CSCI 1001 | No Liberal Education requirement awarded”
  - test_requirement: Information Global Technology HL ⟵ “Information Global Technology HL | 5-7 | 4 credits in CSCI 1001 | No Liberal Education requirement awarded”
### `2b34eaefcf84adfb` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $5,000 for two years ⟵ “Mechanical Engineering Matched Scholarship and Robert & Margaret Bredeson Scholarship | Approximately $5,000 for two years | For students interested in mechanical engineering”
  - eligibility_summary: For students interested in mechanical engineering ⟵ “Mechanical Engineering Matched Scholarship and Robert & Margaret Bredeson Scholarship | Approximately $5,000 for two years | For students interested in mechanical engineering”
### `2e0dc725207c9eb9` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: No Liberal Education Award ⟵ “English Language | A, B, or C | ENGL 1001 (4 credits) & ENGL 1999 (3 credits) | No Liberal Education Award”
  - test_requirement: A, B, or C ⟵ “English Language | A, B, or C | ENGL 1001 (4 credits) & ENGL 1999 (3 credits) | No Liberal Education Award”
### `2fdff36f254c5937` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Frank & Carol Trestman Family Undergraduate Scholarship | $5,000 each year for four years | Academic Performance”
  - eligibility_summary: Academic Performance ⟵ “Frank & Carol Trestman Family Undergraduate Scholarship | $5,000 each year for four years | Academic Performance”
### `32616614d2b9a321` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: No Liberal Education Award ⟵ “Geography | A, B, or C | GEOG 1999 (4 credits) | No Liberal Education Award”
  - test_requirement: A, B, or C ⟵ “Geography | A, B, or C | GEOG 1999 (4 credits) | No Liberal Education Award”
### `364e452ad2d0779e` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Social Science core requirement ⟵ “Psychology | A, B, or C | PSY 1001 (4 credits) & PSY 1999 (4 credits) | Social Science core requirement”
  - test_requirement: A, B, or C ⟵ “Psychology | A, B, or C | PSY 1001 (4 credits) & PSY 1999 (4 credits) | Social Science core requirement”
### `3977b5dd9d706350` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $10,000 each year for four years ⟵ “Lee S. Whitson Scholarship | Approximately $10,000 each year for four years | Based on financial need”
  - eligibility_summary: Based on financial need ⟵ “Lee S. Whitson Scholarship | Approximately $10,000 each year for four years | Based on financial need”
### `3a159ae9419fe99d` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Greater Minnesota Fund | $5,000 each year for four years | Academic PromiseMinnesota students from outside the metro areaDemonstrated financial need”
  - eligibility_summary: Academic PromiseMinnesota students from outside the metro areaDemonstrated financial need ⟵ “Greater Minnesota Fund | $5,000 each year for four years | Academic PromiseMinnesota students from outside the metro areaDemonstrated financial need”
### `3ae7c98813d03ebd` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Mathematical Thinking core requirement ⟵ “Mathematics | A, B, or C | MATH 1271 (4 credits) & MATH 1272 (4 credits) | Mathematical Thinking core requirement”
  - test_requirement: A, B, or C ⟵ “Mathematics | A, B, or C | MATH 1271 (4 credits) & MATH 1272 (4 credits) | Mathematical Thinking core requirement”
### `3b0026623a6c44cf` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000-$16,000 per year, multiple year awards ⟵ “Diversity in Food and Natural Resources Scholarship (DFNRS) | $1,000-$16,000 per year, multiple year awards | High academic achievement and potentialDemonstrated leadership and community involvementStudent must remain enrolled in the College of Food, Agricultural and Natural Resource Sciences”
  - eligibility_summary: High academic achievement and potentialDemonstrated leadership and community involvementStudent must remain enrolled in the College of Food, Agricultural and Natural Resource Sciences ⟵ “Diversity in Food and Natural Resources Scholarship (DFNRS) | $1,000-$16,000 per year, multiple year awards | High academic achievement and potentialDemonstrated leadership and community involvementStudent must remain enrolled in the College of Food, Agricultural and Natural Resource Sciences”
### `3ecbb394020ac9fa` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 for four years ⟵ “Suzanna Ashmore Nelson Memorial Scholarship | $3,000 for four years | Demonstrated financial needPreference given to students who are first generation college students”
  - eligibility_summary: Demonstrated financial needPreference given to students who are first generation college students ⟵ “Suzanna Ashmore Nelson Memorial Scholarship | $3,000 for four years | Demonstrated financial needPreference given to students who are first generation college students”
### `3ecc545fba413025` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/college-level-examination-program-awards (sha256 a4a0b5b97e0e)
- checks: {"thresholds": null}
  - test_requirement: 60 ⟵ “Principles of Microeconomics | 60 | 4 credits in Econ 1101 | Social Science core requirement”
  - eligibility_summary: Social Science core requirement ⟵ “Principles of Microeconomics | 60 | 4 credits in Econ 1101 | Social Science core requirement”
### `4121cc909adb0da2` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: 2 Social Sciences core requirements ⟵ “Economics HL | 5-7 | 4 credits in ECON 1101 and 4 credits in ECON 1102 | 2 Social Sciences core requirements”
  - test_requirement: Economics HL ⟵ “Economics HL | 5-7 | 4 credits in ECON 1101 and 4 credits in ECON 1102 | 2 Social Sciences core requirements”
### `4244d7e6dc970158` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 each year for four years ⟵ “Dale and Elaine Timmers Scholarship for Greater Minnesota Students | $3,000 each year for four years | Demonstrated financial need”
  - eligibility_summary: Demonstrated financial need ⟵ “Dale and Elaine Timmers Scholarship for Greater Minnesota Students | $3,000 each year for four years | Demonstrated financial need”
### `42d13a7aa9b169e7` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: No Liberal Education requirement awarded ⟵ “Computer Science HL | 5-7 | 4 credits in CSCI 1103 and 4 credits in CSCI 1999 | No Liberal Education requirement awarded”
  - test_requirement: Computer Science HL ⟵ “Computer Science HL | 5-7 | 4 credits in CSCI 1103 and 4 credits in CSCI 1999 | No Liberal Education requirement awarded”
### `459363b7e8ce38d0` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 - $3,000 for one year ⟵ “John Koepke Scholarship | $2,000 - $3,000 for one year | Academic promiseDemonstrated financial need Preference given to landscape architecture majors”
  - eligibility_summary: Academic promiseDemonstrated financial need Preference given to landscape architecture majors ⟵ “John Koepke Scholarship | $2,000 - $3,000 for one year | Academic promiseDemonstrated financial need Preference given to landscape architecture majors”
### `47c8f5237362c0d7` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Social Sciences requirement ⟵ “Psychology HL | 5-7 | 4 credits PSY 1001 and PSY 1999 | Social Sciences requirement”
  - test_requirement: Psychology HL ⟵ “Psychology HL | 5-7 | 4 credits PSY 1001 and PSY 1999 | Social Sciences requirement”
### `4c169f1fffe930a2` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000-$6,000 per year, single and multiple year awards ⟵ “Thomas H. Canfield Memorial Scholarship | $1,000-$6,000 per year, single and multiple year awards | Animal Science major, interest in poultry or production agriculture”
  - eligibility_summary: Animal Science major, interest in poultry or production agriculture ⟵ “Thomas H. Canfield Memorial Scholarship | $1,000-$6,000 per year, single and multiple year awards | Animal Science major, interest in poultry or production agriculture”
### `4ead887d1ac40e0b` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $3,000 - $5,000 each year for four years ⟵ “3M Scholarship | Approximately $3,000 - $5,000 each year for four years | Preference for students interested in mechanical engineering, chemical engineering, electrical engineering, chemistry, computer sciencePreference for students from Minnesota, Iowa, North Dakota, South Dakota, or Wisconsin”
  - eligibility_summary: Preference for students interested in mechanical engineering, chemical engineering, electrical engineering, chemistry, computer sciencePreference for students from Minnesota, Iowa, North Dakota, South Dakota, or Wisconsin ⟵ “3M Scholarship | Approximately $3,000 - $5,000 each year for four years | Preference for students interested in mechanical engineering, chemical engineering, electrical engineering, chemistry, computer sciencePreference for students from Minnesota, Iowa, North Dakota, South Dakota, or Wisconsin”
### `52037b5659636464` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 each year for four years ⟵ “Harold Paul and Mary Sisson Dey Morris Scholarship | $2,000 each year for four years | Academic meritDemonstrated financial need”
  - eligibility_summary: Academic meritDemonstrated financial need ⟵ “Harold Paul and Mary Sisson Dey Morris Scholarship | $2,000 each year for four years | Academic meritDemonstrated financial need”
### `546818777740e2ed` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $10,000 for four years ⟵ “3M Coleman Scholarship | Approximately $10,000 for four years | For students interested in civil, environmental or geo-engineering”
  - eligibility_summary: For students interested in civil, environmental or geo-engineering ⟵ “3M Coleman Scholarship | Approximately $10,000 for four years | For students interested in civil, environmental or geo-engineering”
### `54ef32866e9aa4ac` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Valdemar & Marilyn Olson Undergraduate Scholarship | $5,000 each year for four years | Interest in International Business”
  - eligibility_summary: Interest in International Business ⟵ “Valdemar & Marilyn Olson Undergraduate Scholarship | $5,000 each year for four years | Interest in International Business”
### `55dd99114831dbcc` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000-$3,000 per year, single year awards ⟵ “Department of Forest Resources Scholarships | $1,000-$3,000 per year, single year awards | Forest and Natural Resources Management majorProfessional promise and needAcademic achievement”
  - eligibility_summary: Forest and Natural Resources Management majorProfessional promise and needAcademic achievement ⟵ “Department of Forest Resources Scholarships | $1,000-$3,000 per year, single year awards | Forest and Natural Resources Management majorProfessional promise and needAcademic achievement”
### `560d03731b4ecb3e` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: No Liberal Education Award ⟵ “Computer Science | A, B, or C | CSCI 1999 (8 credits) | No Liberal Education Award”
  - test_requirement: A, B, or C ⟵ “Computer Science | A, B, or C | CSCI 1999 (8 credits) | No Liberal Education Award”
### `567a02fd4aee969a` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $10,000 for four years ⟵ “Dakota Aggregates Scholarship | Approximately $10,000 for four years | For students interested in civil, environmental or geo-engineering or earth science or environmental geosciences”
  - eligibility_summary: For students interested in civil, environmental or geo-engineering or earth science or environmental geosciences ⟵ “Dakota Aggregates Scholarship | Approximately $10,000 for four years | For students interested in civil, environmental or geo-engineering or earth science or environmental geosciences”
### `5b6559e8131d5f35` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Social Science core requirement & Global Perspective theme requirement ⟵ “Economics | A, B, or C | ECON 1101 (4 credits) & ECON 1102 (4 credits) | Social Science core requirement & Global Perspective theme requirement”
  - test_requirement: A, B, or C ⟵ “Economics | A, B, or C | ECON 1101 (4 credits) & ECON 1102 (4 credits) | Social Science core requirement & Global Perspective theme requirement”
### `5c3b71c43171ed55` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $10,000 each year for four years ⟵ “Glen E. Ullyot Scholarship | Approximately $10,000 each year for four years | Preference for students from South Dakota”
  - eligibility_summary: Preference for students from South Dakota ⟵ “Glen E. Ullyot Scholarship | Approximately $10,000 each year for four years | Preference for students from South Dakota”
### `5c8e74099eb9f3b8` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Full tuition each year for four years ⟵ “Robert K. Anderson Scholarship | Full tuition each year for four years | Based on financial needMN residents with preference for students from Crow Wing County”
  - eligibility_summary: Based on financial needMN residents with preference for students from Crow Wing County ⟵ “Robert K. Anderson Scholarship | Full tuition each year for four years | Based on financial needMN residents with preference for students from Crow Wing County”
### `5d40e878e3d336c1` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Monica Tsang and James Weatherbee Merit Scholarship in Biology | $5,000 each year for four years | Academic merit”
  - eligibility_summary: Academic merit ⟵ “Monica Tsang and James Weatherbee Merit Scholarship in Biology | $5,000 each year for four years | Academic merit”
### `5edb98ce5f2985da` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 each year for four years ⟵ “Ruth S. Brown Scholarship | $3,000 each year for four years | Academic PromiseStrong and verified interest in Family Social ScienceFirst GenerationDemonstrated financial need”
  - eligibility_summary: Academic PromiseStrong and verified interest in Family Social ScienceFirst GenerationDemonstrated financial need ⟵ “Ruth S. Brown Scholarship | $3,000 each year for four years | Academic PromiseStrong and verified interest in Family Social ScienceFirst GenerationDemonstrated financial need”
### `5f078c8aaa6c4110` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Biological Sciences /Lab core requirement ⟵ “Biology | A, B, or C | BIOL 1009 (4 credits) | Biological Sciences /Lab core requirement”
  - test_requirement: A, B, or C ⟵ “Biology | A, B, or C | BIOL 1009 (4 credits) | Biological Sciences /Lab core requirement”
### `61b787e171de5596` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 - $3,000 per year, single and multiple-year awards (up to four years) ⟵ “Legacy Scholarship | $2,000 - $3,000 per year, single and multiple-year awards (up to four years) | Academic achievementDemonstrated financial need Apparel design, graphic design, interior design, product design, or retail and consumer studies majors”
  - eligibility_summary: Academic achievementDemonstrated financial need Apparel design, graphic design, interior design, product design, or retail and consumer studies majors ⟵ “Legacy Scholarship | $2,000 - $3,000 per year, single and multiple-year awards (up to four years) | Academic achievementDemonstrated financial need Apparel design, graphic design, interior design, product design, or retail and consumer studies majors”
### `626e45a62b0c6c88` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “John & Jane Mooty Undergraduate Scholarship | $5,000 each year for four years | Demonstrated Financial Need”
  - eligibility_summary: Demonstrated Financial Need ⟵ “John & Jane Mooty Undergraduate Scholarship | $5,000 each year for four years | Demonstrated Financial Need”
### `66d74de51186828b` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Mathematical Thinking requirement ⟵ “Math HL Applications & Interpretation | 5-7 | 4 credits in MATH 1271 and 4 credits in STAT 3011 | Mathematical Thinking requirement”
  - test_requirement: Math HL Applications & Interpretation ⟵ “Math HL Applications & Interpretation | 5-7 | 4 credits in MATH 1271 and 4 credits in STAT 3011 | Mathematical Thinking requirement”
### `6e10ed781784e0bd` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 each year for four years ⟵ “Faculty and Staff Legacy Scholarship | $2,000 each year for four years | Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human Development”
  - eligibility_summary: Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human Development ⟵ “Faculty and Staff Legacy Scholarship | $2,000 each year for four years | Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human Development”
### `6e1dcf710ffc8c2d` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 each year for four years ⟵ “Piechowski & Oberto-Medina Scholarship | $2,000 each year for four years | First generation in collegePermanent residents or refugees/asylees”
  - eligibility_summary: First generation in collegePermanent residents or refugees/asylees ⟵ “Piechowski & Oberto-Medina Scholarship | $2,000 each year for four years | First generation in collegePermanent residents or refugees/asylees”
### `70dc5aa772f25d2b` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $7,500 each year for four years ⟵ “Donald M. Anderson Undergraduate Scholarship | $7,500 each year for four years | MN ResidentsAcademic Performance”
  - eligibility_summary: MN ResidentsAcademic Performance ⟵ “Donald M. Anderson Undergraduate Scholarship | $7,500 each year for four years | MN ResidentsAcademic Performance”
### `751f29609ba54847` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 - $5,000 per year, single and multiple year awards ⟵ “Lofgren Scholarships | $1,000 - $5,000 per year, single and multiple year awards | Preference given to students from the Iron Range and northeastern MinnesotaBased on academic merit and demonstrated financial needStudent must enroll and pursue a major in the College of Food, Agricultural and Natural”
  - eligibility_summary: Preference given to students from the Iron Range and northeastern MinnesotaBased on academic merit and demonstrated financial needStudent must enroll and pursue a major in the College of Food, Agricultural and Natural Resource Sciences ⟵ “Lofgren Scholarships | $1,000 - $5,000 per year, single and multiple year awards | Preference given to students from the Iron Range and northeastern MinnesotaBased on academic merit and demonstrated financial needStudent must enroll and pursue a major in the College of Food, Agricultural and Natural”
### `75499dc1ed85f150` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Contact the Office of Admissions ⟵ “Other Subjects HL | 5-7 | Contact the Office of Admissions | Contact the Office of Admissions”
  - test_requirement: Other Subjects HL ⟵ “Other Subjects HL | 5-7 | Contact the Office of Admissions | Contact the Office of Admissions”
### `75fa6027a4da41cd` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Fulfills CLA second language requirement; does NOT fulfill Writing Intensive requirement ⟵ “Spanish A HL | 5-7 | 4 credits in SPAN 3015W | Fulfills CLA second language requirement; does NOT fulfill Writing Intensive requirement”
  - test_requirement: Spanish A HL ⟵ “Spanish A HL | 5-7 | 4 credits in SPAN 3015W | Fulfills CLA second language requirement; does NOT fulfill Writing Intensive requirement”
### `763e4df95eba958d` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Campbell Scholarship for Education | $5,000 each year for four years | Academic achievementDemonstrated financial needPursuing any education major: Early Childhood, Elementary or Special Education”
  - eligibility_summary: Academic achievementDemonstrated financial needPursuing any education major: Early Childhood, Elementary or Special Education ⟵ “Campbell Scholarship for Education | $5,000 each year for four years | Academic achievementDemonstrated financial needPursuing any education major: Early Childhood, Elementary or Special Education”
### `7648b7781812c9df` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Arts and Humanities core requirement ⟵ “Music | A, B, or C | MUS 1021 | Arts and Humanities core requirement”
  - test_requirement: A, B, or C ⟵ “Music | A, B, or C | MUS 1021 | Arts and Humanities core requirement”
### `773f5f6af8cc0c45` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 each year for four years ⟵ “McCutcheon Family Scholarship | $1,500 each year for four years | First generation in collegeDemonstrated financial need”
  - eligibility_summary: First generation in collegeDemonstrated financial need ⟵ “McCutcheon Family Scholarship | $1,500 each year for four years | First generation in collegeDemonstrated financial need”
### `7791df62c50b4ab3` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “CEHD Legacy Award | $5,000 each year for four years | Strong academic achievement and community involvementFamily Social Science major or Youth Studies majorFinancial aid considered”
  - eligibility_summary: Strong academic achievement and community involvementFamily Social Science major or Youth Studies majorFinancial aid considered ⟵ “CEHD Legacy Award | $5,000 each year for four years | Strong academic achievement and community involvementFamily Social Science major or Youth Studies majorFinancial aid considered”
### `784852eaf1b74fe0` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000-$3,000 per year, single and multiple year awards ⟵ “Department of Bioproducts and Biosystems Engineering Scholarships | $2,000-$3,000 per year, single and multiple year awards | Pre-Bioproducts and Biosystems Engineering (CFANS), Bioproducts and Biosystems Engineering (CSE), or Sustainable Systems Management majorAcademic achievement and potential”
  - eligibility_summary: Pre-Bioproducts and Biosystems Engineering (CFANS), Bioproducts and Biosystems Engineering (CSE), or Sustainable Systems Management majorAcademic achievement and potential ⟵ “Department of Bioproducts and Biosystems Engineering Scholarships | $2,000-$3,000 per year, single and multiple year awards | Pre-Bioproducts and Biosystems Engineering (CFANS), Bioproducts and Biosystems Engineering (CSE), or Sustainable Systems Management majorAcademic achievement and potential”
### `7b583d376545eb52` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $7,500 each year for four years ⟵ “Duane and Susan Ottenstroer Undergraduate Scholarship | $7,500 each year for four years | Academic PerformanceDemonstrated Financial Need”
  - eligibility_summary: Academic PerformanceDemonstrated Financial Need ⟵ “Duane and Susan Ottenstroer Undergraduate Scholarship | $7,500 each year for four years | Academic PerformanceDemonstrated Financial Need”
### `7b87b673cbdfdb1b` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 for four years ⟵ “Perry and Carol Hackett Genetics Scholarship | $1,500 for four years | Academic meritPlan to major in Genetics, Cell Biology and Development”
  - eligibility_summary: Academic meritPlan to major in Genetics, Cell Biology and Development ⟵ “Perry and Carol Hackett Genetics Scholarship | $1,500 for four years | Academic meritPlan to major in Genetics, Cell Biology and Development”
### `81974e3abe0498ad` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: 24 single-year awards of $3,000 ⟵ “Rev. Dr. Martin Luther King Jr. Program Living Learning Community | 24 single-year awards of $3,000 | Incoming freshman students who have opted to join the MLK Program and be housed in the MLK LLC”
  - eligibility_summary: Incoming freshman students who have opted to join the MLK Program and be housed in the MLK LLC ⟵ “Rev. Dr. Martin Luther King Jr. Program Living Learning Community | 24 single-year awards of $3,000 | Incoming freshman students who have opted to join the MLK Program and be housed in the MLK LLC”
### `85c8dfb237e8732f` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Biological Sciences/lab requirement ⟵ “Biology HL | 5-7 | 4 credits in Biology 1009 (General Biology) | Biological Sciences/lab requirement”
  - test_requirement: Biology HL ⟵ “Biology HL | 5-7 | 4 credits in Biology 1009 (General Biology) | Biological Sciences/lab requirement”
### `85d82f879a257fe8` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: 140 multi-year awards of $2,000 - $4,000 per year, for up to four years ⟵ “Incoming Freshman Collegiate Scholarships | 140 multi-year awards of $2,000 - $4,000 per year, for up to four years | Financial need and/or academic merit”
  - eligibility_summary: Financial need and/or academic merit ⟵ “Incoming Freshman Collegiate Scholarships | 140 multi-year awards of $2,000 - $4,000 per year, for up to four years | Financial need and/or academic merit”
### `8839c7dce2002d53` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 each year for four years ⟵ “Dorothy W. Hilligos Scholarship | $1,000 each year for four years | Academic promiseFrom any of these areas: Hibbing, Chisholm, Grand Rapids, Coleraine, Cook, Tower, Ely, Owatonna, Nashwauk, Keewatin, Cherry”
  - eligibility_summary: Academic promiseFrom any of these areas: Hibbing, Chisholm, Grand Rapids, Coleraine, Cook, Tower, Ely, Owatonna, Nashwauk, Keewatin, Cherry ⟵ “Dorothy W. Hilligos Scholarship | $1,000 each year for four years | Academic promiseFrom any of these areas: Hibbing, Chisholm, Grand Rapids, Coleraine, Cook, Tower, Ely, Owatonna, Nashwauk, Keewatin, Cherry”
### `8909e484ea28f38c` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 for four years ⟵ “CBS Alumni and Friends Scholarship | $1,500 for four years | Academic merit”
  - eligibility_summary: Academic merit ⟵ “CBS Alumni and Friends Scholarship | $1,500 for four years | Academic merit”
### `8e62957c9666a161` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: 12 awards of $500 - $3,000 per year for up to four years ⟵ “Marching Band Scholarships | 12 awards of $500 - $3,000 per year for up to four years | Audition-based selection plus financial need and/or academic merit”
  - eligibility_summary: Audition-based selection plus financial need and/or academic merit ⟵ “Marching Band Scholarships | 12 awards of $500 - $3,000 per year for up to four years | Audition-based selection plus financial need and/or academic merit”
### `8fda85a1f5613b8f` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 - $2,500 for one year ⟵ “Carl J. Remick Scholarship | $1,000 - $2,500 for one year | Academic promisePreference given to architecture majors”
  - eligibility_summary: Academic promisePreference given to architecture majors ⟵ “Carl J. Remick Scholarship | $1,000 - $2,500 for one year | Academic promisePreference given to architecture majors”
### `90f308b2a05b49e6` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $10,000 each year for four years ⟵ “John and Jane Clark Scholarship | $10,000 each year for four years | Demonstrated Financial Need”
  - eligibility_summary: Demonstrated Financial Need ⟵ “John and Jane Clark Scholarship | $10,000 each year for four years | Demonstrated Financial Need”
### `936533ee4d83bc04` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Cost of attendance each year for four years ⟵ “Sezzle Scholarship | Cost of attendance each year for four years | Based on financial needPreference for students interested in computer science, computer engineering, and data sciencesPreference for students from Minnesota, North Dakota, South Dakota, Wisconsin”
  - eligibility_summary: Based on financial needPreference for students interested in computer science, computer engineering, and data sciencesPreference for students from Minnesota, North Dakota, South Dakota, Wisconsin ⟵ “Sezzle Scholarship | Cost of attendance each year for four years | Based on financial needPreference for students interested in computer science, computer engineering, and data sciencesPreference for students from Minnesota, North Dakota, South Dakota, Wisconsin”
### `94089a31066959bc` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Burnham Endowed Scholarship | $5,000 each year for four years | Greater MNDemonstrated Financial NeedLeadership or Community Involvement”
  - eligibility_summary: Greater MNDemonstrated Financial NeedLeadership or Community Involvement ⟵ “Burnham Endowed Scholarship | $5,000 each year for four years | Greater MNDemonstrated Financial NeedLeadership or Community Involvement”
### `94a7c04365e026cf` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Land-Grant Legacy Scholarship | $5,000 each year for four years | Students admitted from greater Minnesota (outside the seven-county metro area)Student must enroll and pursue a major in the College of Food, Agricultural and Natural Resource Sciences”
  - eligibility_summary: Students admitted from greater Minnesota (outside the seven-county metro area)Student must enroll and pursue a major in the College of Food, Agricultural and Natural Resource Sciences ⟵ “Land-Grant Legacy Scholarship | $5,000 each year for four years | Students admitted from greater Minnesota (outside the seven-county metro area)Student must enroll and pursue a major in the College of Food, Agricultural and Natural Resource Sciences”
### `9ad4cbbfb6c6eab7` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Fulfills CLA second language requirement ⟵ “French HL | 5-7 | 3 credits in FREN 3015 | Fulfills CLA second language requirement”
  - test_requirement: French HL ⟵ “French HL | 5-7 | 3 credits in FREN 3015 | Fulfills CLA second language requirement”
### `9b4da29bbc1698c0` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Mathematical Thinking requirement ⟵ “Math HL Analysis & Approaches | 5-7 | 4 credits in MATH 1271 and 4 credits in MATH 1272 | Mathematical Thinking requirement”
  - test_requirement: Math HL Analysis & Approaches ⟵ “Math HL Analysis & Approaches | 5-7 | 4 credits in MATH 1271 and 4 credits in MATH 1272 | Mathematical Thinking requirement”
### `9d3dd79ce1601d5c` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $2,000 - $5,000 for two or four years ⟵ “Department of Civil, Environmental and Geo-Engineering Scholarships | Approximately $2,000 - $5,000 for two or four years | For freshmen and transfer students interested in civil, environmental or geo-engineering”
  - eligibility_summary: For freshmen and transfer students interested in civil, environmental or geo-engineering ⟵ “Department of Civil, Environmental and Geo-Engineering Scholarships | Approximately $2,000 - $5,000 for two or four years | For freshmen and transfer students interested in civil, environmental or geo-engineering”
### `9f75d4cd0dfd085e` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/college-level-examination-program-awards (sha256 a4a0b5b97e0e)
- checks: {"thresholds": null}
  - test_requirement: 60 ⟵ “Principles of Macroeconomics | 60 | 4 credits in Econ 1102 | Social Science core requirement”
  - eligibility_summary: Social Science core requirement ⟵ “Principles of Macroeconomics | 60 | 4 credits in Econ 1102 | Social Science core requirement”
### `a1d9a851525ba891` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $2000 for two years ⟵ “Stefan & Elaine Dunda Scholarship | Approximately $2000 for two years | Based on financial needFor MN students from the Iron Range”
  - eligibility_summary: Based on financial needFor MN students from the Iron Range ⟵ “Stefan & Elaine Dunda Scholarship | Approximately $2000 for two years | Based on financial needFor MN students from the Iron Range”
### `aee7707bb54efdf0` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 for four years ⟵ “CBS Freshman Scholarship | $2,500 for four years | Academic meritDemonstrated financial need”
  - eligibility_summary: Academic meritDemonstrated financial need ⟵ “CBS Freshman Scholarship | $2,500 for four years | Academic meritDemonstrated financial need”
### `af8bdcd5174d1e28` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Physical Sciences/lab requirement ⟵ “Physics HL | 5-7 | 4 credits PHYS 1301 and 4 credits in PHYS 1302 | Physical Sciences/lab requirement”
  - test_requirement: Physics HL ⟵ “Physics HL | 5-7 | 4 credits PHYS 1301 and 4 credits in PHYS 1302 | Physical Sciences/lab requirement”
### `afc54daa4e203ce6` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000-$5,000 per year, single and multiple year awards ⟵ “College of Food, Agricultural and Natural Resource Sciences Scholarships | $1,000-$5,000 per year, single and multiple year awards | Competitive high school class rank and ACT/SATRecord of leadership and academic achievementStudent must remain enrolled in the College of Food, Agricultural and Natura”
  - eligibility_summary: Competitive high school class rank and ACT/SATRecord of leadership and academic achievementStudent must remain enrolled in the College of Food, Agricultural and Natural Resource Sciences ⟵ “College of Food, Agricultural and Natural Resource Sciences Scholarships | $1,000-$5,000 per year, single and multiple year awards | Competitive high school class rank and ACT/SATRecord of leadership and academic achievementStudent must remain enrolled in the College of Food, Agricultural and Natura”
### `b0bb71cc86660882` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 - $3,000 for one year ⟵ “Sylvia and Sam Druy Scholarship | $1,000 - $3,000 for one year | Academic promisePreference given to retail and consumer studies majors”
  - eligibility_summary: Academic promisePreference given to retail and consumer studies majors ⟵ “Sylvia and Sam Druy Scholarship | $1,000 - $3,000 for one year | Academic promisePreference given to retail and consumer studies majors”
### `b1e1d23126ff9ae9` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $500-$3,000 per year, single and multiple year awards ⟵ “Department of Agronomy & Plant Genetics Scholarship | $500-$3,000 per year, single and multiple year awards | Plant Science, Sustainable Agriculture and Food Systems majorAcademic achievement and potential”
  - eligibility_summary: Plant Science, Sustainable Agriculture and Food Systems majorAcademic achievement and potential ⟵ “Department of Agronomy & Plant Genetics Scholarship | $500-$3,000 per year, single and multiple year awards | Plant Science, Sustainable Agriculture and Food Systems majorAcademic achievement and potential”
### `b497d71962a0ea31` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 for one year ⟵ “Howard and Venetia Johnson Scholarship | $2,000 for one year | Preference of graduates from Minneapolis North High School or any Minneapolis public high school who want to obtain a degree from CEHD”
  - eligibility_summary: Preference of graduates from Minneapolis North High School or any Minneapolis public high school who want to obtain a degree from CEHD ⟵ “Howard and Venetia Johnson Scholarship | $2,000 for one year | Preference of graduates from Minneapolis North High School or any Minneapolis public high school who want to obtain a degree from CEHD”
### `b54c5111f3ff4af1` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000-$5,000 single and multiple year awards ⟵ “Department of Food Science & Nutrition Scholarships | $1,000-$5,000 single and multiple year awards | Food Science or Nutrition MajorAcademic Achievement”
  - eligibility_summary: Food Science or Nutrition MajorAcademic Achievement ⟵ “Department of Food Science & Nutrition Scholarships | $1,000-$5,000 single and multiple year awards | Food Science or Nutrition MajorAcademic Achievement”
### `b57b306169afd63a` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Urban Scholarship Fund | $5,000 each year for four years | Academic promiseDemonstrated financial needPreference for students who have graduated from a Minneapolis or St. Paul public high school”
  - eligibility_summary: Academic promiseDemonstrated financial needPreference for students who have graduated from a Minneapolis or St. Paul public high school ⟵ “Urban Scholarship Fund | $5,000 each year for four years | Academic promiseDemonstrated financial needPreference for students who have graduated from a Minneapolis or St. Paul public high school”
### `b96007a5e0bf9b53` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 for four years ⟵ “Dvergsten and Bauermeister Scholarship | $1,500 for four years | Academic meritDemonstrated financial need”
  - eligibility_summary: Academic meritDemonstrated financial need ⟵ “Dvergsten and Bauermeister Scholarship | $1,500 for four years | Academic meritDemonstrated financial need”
### `b9a9ea506241a690` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $8,000 each year for four years ⟵ “Robert L. Wortz Scholarship | $8,000 each year for four years | Demonstrated financial need”
  - eligibility_summary: Demonstrated financial need ⟵ “Robert L. Wortz Scholarship | $8,000 each year for four years | Demonstrated financial need”
### `ba5d8a1c9a71d36f` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 - $3,000 per year, single and multiple-year awards (up to four years) ⟵ “Augustus Searle Scholarship | $1,500 - $3,000 per year, single and multiple-year awards (up to four years) | Apparel design, graphic design, interior design, product design, or retail and consumer studies majors”
  - eligibility_summary: Apparel design, graphic design, interior design, product design, or retail and consumer studies majors ⟵ “Augustus Searle Scholarship | $1,500 - $3,000 per year, single and multiple-year awards (up to four years) | Apparel design, graphic design, interior design, product design, or retail and consumer studies majors”
### `bb5f9b843a5958ee` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 each year for four years ⟵ “Sadie and Wayne Luchsinger Scholarship | $2,500 each year for four years | Academic meritPlan to major in biochemistry”
  - eligibility_summary: Academic meritPlan to major in biochemistry ⟵ “Sadie and Wayne Luchsinger Scholarship | $2,500 each year for four years | Academic meritPlan to major in biochemistry”
### `bba2a43679f581ea` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Arts and Humanities core requirement ⟵ “Art & Design | A, B, or C | ARTS 1101 (4 credits) & ARTS 1102 (4 credits) | Arts and Humanities core requirement”
  - test_requirement: A, B, or C ⟵ “Art & Design | A, B, or C | ARTS 1101 (4 credits) & ARTS 1102 (4 credits) | Arts and Humanities core requirement”
### `bbe56257de5d789a` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Historical Perspectives requirement & Global Perspectives requirement ⟵ “History HL | 5-7 | 8 credits in HIST 1999 | Historical Perspectives requirement & Global Perspectives requirement”
  - test_requirement: History HL ⟵ “History HL | 5-7 | 8 credits in HIST 1999 | Historical Perspectives requirement & Global Perspectives requirement”
### `bc85820cefaa8eb9` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 each year for four years ⟵ “CBS Advancement of Biology Scholarship | $2,500 each year for four years | Demonstrated financial need”
  - eligibility_summary: Demonstrated financial need ⟵ “CBS Advancement of Biology Scholarship | $2,500 each year for four years | Demonstrated financial need”
### `bd869f97e666f84d` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $2,000 each year for four years ⟵ “John Dexheimer and Carla Haugen Scholarship | Approximately $2,000 each year for four years | Preference for students who are the first generation of their family attending a four-year college.Students from Johnson or Harding High Schools in St. Paul or in the county of Lac Qui Parle, MN.”
  - eligibility_summary: Preference for students who are the first generation of their family attending a four-year college.Students from Johnson or Harding High Schools in St. Paul or in the county of Lac Qui Parle, MN. ⟵ “John Dexheimer and Carla Haugen Scholarship | Approximately $2,000 each year for four years | Preference for students who are the first generation of their family attending a four-year college.Students from Johnson or Harding High Schools in St. Paul or in the county of Lac Qui Parle, MN.”
### `be4455c7b2ce60a3` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: 150 multi-year awards of $2,000 - $4,000 per year for up to three years ⟵ “Incoming Transfer Student Collegiate Scholarships | 150 multi-year awards of $2,000 - $4,000 per year for up to three years | Financial need and/or academic merit”
  - eligibility_summary: Financial need and/or academic merit ⟵ “Incoming Transfer Student Collegiate Scholarships | 150 multi-year awards of $2,000 - $4,000 per year for up to three years | Financial need and/or academic merit”
### `c028000a2d86f17d` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 for one year ⟵ “David Grantham Burbee Memorial Scholarship | $2,500 for one year | Academic meritPlan to major in biochemistryDemonstrated financial need”
  - eligibility_summary: Academic meritPlan to major in biochemistryDemonstrated financial need ⟵ “David Grantham Burbee Memorial Scholarship | $2,500 for one year | Academic meritPlan to major in biochemistryDemonstrated financial need”
### `c4b5d51f6e3e2438` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $10,000 each year for four years ⟵ “Robert F. Hartmann/Nordby Scholarship and Robert E. Rice | Approximately $10,000 each year for four years | Based on financial needFor students interested in electrical or computer engineering”
  - eligibility_summary: Based on financial needFor students interested in electrical or computer engineering ⟵ “Robert F. Hartmann/Nordby Scholarship and Robert E. Rice | Approximately $10,000 each year for four years | Based on financial needFor students interested in electrical or computer engineering”
### `c6dc41f4143566d4` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $2,000 - 4,000 each year for four years ⟵ “Richard Kramer Scholarship, Robert Fridgen Scholarship, and George & Margaret Hentges Scholarship | Approximately $2,000 - 4,000 each year for four years | Based on financial needPreference given to students from Minneapolis North High School or Minneapolis Public Schools”
  - eligibility_summary: Based on financial needPreference given to students from Minneapolis North High School or Minneapolis Public Schools ⟵ “Richard Kramer Scholarship, Robert Fridgen Scholarship, and George & Margaret Hentges Scholarship | Approximately $2,000 - 4,000 each year for four years | Based on financial needPreference given to students from Minneapolis North High School or Minneapolis Public Schools”
### `c905bcdcd0de974a` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Arts/Humanities requirement ⟵ “Art HL | 5-7 | 4 Credits in ARTS 1999 and 4 credits in ARTS 1001 | Arts/Humanities requirement”
  - test_requirement: Art HL ⟵ “Art HL | 5-7 | 4 Credits in ARTS 1999 and 4 credits in ARTS 1001 | Arts/Humanities requirement”
### `c9da6ae44e9a5004` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $5,000 - $10,000 each year for two to four years ⟵ “3M Impact Scholarship | Approximately $5,000 - $10,000 each year for two to four years | ”
### `cbee2b72d1e6f9dc` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $4000 for one year ⟵ “Wayland Noland Scholarship | Approximately $4000 for one year | For students interested in chemistry”
  - eligibility_summary: For students interested in chemistry ⟵ “Wayland Noland Scholarship | Approximately $4000 for one year | For students interested in chemistry”
### `d1792dc514b9e1ae` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 each year for four years ⟵ “David V. Taylor Scholarship | $2,000 each year for four years | Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human DevelopmentAcademic potentialFinancial aid considered”
  - eligibility_summary: Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human DevelopmentAcademic potentialFinancial aid considered ⟵ “David V. Taylor Scholarship | $2,000 each year for four years | Preference given to students admitted into the President's Emerging Scholars Program, or the TRIO Student Support Services Program in the College of Education and Human DevelopmentAcademic potentialFinancial aid considered”
### `d46fe4b761380e53` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 each year for four years ⟵ “Marie K. and David L. Goblirsch Scholarship | $1,000 each year for four years | Academic meritDemonstrated financial need”
  - eligibility_summary: Academic meritDemonstrated financial need ⟵ “Marie K. and David L. Goblirsch Scholarship | $1,000 each year for four years | Academic meritDemonstrated financial need”
### `d891297852de2a62` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: 38 awards of $3,000 - $7,000 per year for up to four years ⟵ “School of Music Scholarships | 38 awards of $3,000 - $7,000 per year for up to four years | Audition-based selection plus financial need and/or academic merit”
  - eligibility_summary: Audition-based selection plus financial need and/or academic merit ⟵ “School of Music Scholarships | 38 awards of $3,000 - $7,000 per year for up to four years | Audition-based selection plus financial need and/or academic merit”
### `d9eec3a15232ac2b` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Physical Science/Lab core requirement; Does NOT fulfill Writing Intensive requirement ⟵ “Physics | A, B, or C | PHYS 1301, 1302 & 2303 (12 credits) | Physical Science/Lab core requirement; Does NOT fulfill Writing Intensive requirement”
  - test_requirement: A, B, or C ⟵ “Physics | A, B, or C | PHYS 1301, 1302 & 2303 (12 credits) | Physical Science/Lab core requirement; Does NOT fulfill Writing Intensive requirement”
### `da04c5a45191193b` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: Literature core requirement ⟵ “Literature in English | A, B, or C | ENGL 1999A (4 credits) & ENGL 1999B (4 credits) | Literature core requirement”
  - test_requirement: A, B, or C ⟵ “Literature in English | A, B, or C | ENGL 1999A (4 credits) & ENGL 1999B (4 credits) | Literature core requirement”
### `dccf0cc26a02fd2e` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/college-level-examination-program-awards (sha256 a4a0b5b97e0e)
- checks: {"thresholds": null}
  - test_requirement: 60 ⟵ “College Mathematics | 60 | 3 credits in Math 1999 | Mathematical Thinking core requirement”
  - eligibility_summary: Mathematical Thinking core requirement ⟵ “College Mathematics | 60 | 3 credits in Math 1999 | Mathematical Thinking core requirement”
### `e331272630f2da9a` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 each year for four years ⟵ “CEHD Access Scholarship | $3,000 each year for four years | Demonstrated financial need”
  - eligibility_summary: Demonstrated financial need ⟵ “CEHD Access Scholarship | $3,000 each year for four years | Demonstrated financial need”
### `ea2453162cfe0b24` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 for one year ⟵ “RS Wright CEHD Freshman Scholarship | $1,000 for one year | Strong academic achievement and community involvementCommitment to completing a CEHD degree”
  - eligibility_summary: Strong academic achievement and community involvementCommitment to completing a CEHD degree ⟵ “RS Wright CEHD Freshman Scholarship | $1,000 for one year | Strong academic achievement and community involvementCommitment to completing a CEHD degree”
### `ec08bb07f49cc2aa` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $8,500 each year for four years ⟵ “Jennifer Houle Memorial Undergraduate Scholarship | $8,500 each year for four years | Academic PerformanceLeadership”
  - eligibility_summary: Academic PerformanceLeadership ⟵ “Jennifer Houle Memorial Undergraduate Scholarship | $8,500 each year for four years | Academic PerformanceLeadership”
### `ec15028cc80fb12f` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 for one year ⟵ “Elde Baskin Scholarship in Biology | $2,500 for one year | Demonstrated Financial NeedPreference given to students who are first-generation college students”
  - eligibility_summary: Demonstrated Financial NeedPreference given to students who are first-generation college students ⟵ “Elde Baskin Scholarship in Biology | $2,500 for one year | Demonstrated Financial NeedPreference given to students who are first-generation college students”
### `ee85e90c612d2c25` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Thomas Leary Scholarship | $5,000 each year for four years | MN ResidentsDemonstrated Financial NeedCommunity Involvement”
  - eligibility_summary: MN ResidentsDemonstrated Financial NeedCommunity Involvement ⟵ “Thomas Leary Scholarship | $5,000 each year for four years | MN ResidentsDemonstrated Financial NeedCommunity Involvement”
### `ee88caf2b3dd017f` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $500-$3,000 single year awards ⟵ “Department of Horticultural Science Scholarships | $500-$3,000 single year awards | Plant Science, Sustainable Agriculture and Food Systems majorRecord of leadership and academic achievement”
  - eligibility_summary: Plant Science, Sustainable Agriculture and Food Systems majorRecord of leadership and academic achievement ⟵ “Department of Horticultural Science Scholarships | $500-$3,000 single year awards | Plant Science, Sustainable Agriculture and Food Systems majorRecord of leadership and academic achievement”
### `ef2a36ac14a2f2b0` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/level-course-awards (sha256 9e69836db648)
- checks: {"thresholds": null}
  - award_amount_text: No Liberal Education Award ⟵ “Information Technology | A, B, or C | CSCI 1999 (4 credits) | No Liberal Education Award”
  - test_requirement: A, B, or C ⟵ “Information Technology | A, B, or C | CSCI 1999 (4 credits) | No Liberal Education Award”
### `f1bf2634713d44fb` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 each year for four years ⟵ “Schmalz Family Undergraduate Scholarship | $5,000 each year for four years | Academic Performance”
  - eligibility_summary: Academic Performance ⟵ “Schmalz Family Undergraduate Scholarship | $5,000 each year for four years | Academic Performance”
### `f1ec132bb7f0fd04` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $8,500 each year for four years ⟵ “David and Shirley Hubers Undergraduate Scholarship | $8,500 each year for four years | Demonstrated Financial Need”
  - eligibility_summary: Demonstrated Financial Need ⟵ “David and Shirley Hubers Undergraduate Scholarship | $8,500 each year for four years | Demonstrated Financial Need”
### `f1f31df00d7b1f6e` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 each year for four years ⟵ “Clare and Jerome Ritter Scholarship | $3,000 each year for four years | Academic merit”
  - eligibility_summary: Academic merit ⟵ “Clare and Jerome Ritter Scholarship | $3,000 each year for four years | Academic merit”
### `f4982d87c952b0e7` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 each year for four years ⟵ “Jean Morris Helms Scholarship | $2,000 each year for four years | Academic promiseKinesiology majorDemonstrated financial need”
  - eligibility_summary: Academic promiseKinesiology majorDemonstrated financial need ⟵ “Jean Morris Helms Scholarship | $2,000 each year for four years | Academic promiseKinesiology majorDemonstrated financial need”
### `f8fb1d7d873df42b` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: $3,500 for four years ⟵ “Cynthia A. Rask Biological Sciences Scholarship | $3,500 for four years | Academic meritDemonstrated financial need”
  - eligibility_summary: Academic meritDemonstrated financial need ⟵ “Cynthia A. Rask Biological Sciences Scholarship | $3,500 for four years | Academic meritDemonstrated financial need”
### `f905098c99550718` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"thresholds": null}
  - award_amount_text: Literature requirement & First-year Writing requirement ⟵ “English Language & Literature HL | 5-7 | 4 credits WRIT 1301 and 4 credits in ENGL 1999 | Literature requirement & First-year Writing requirement”
  - test_requirement: English Language & Literature HL ⟵ “English Language & Literature HL | 5-7 | 4 credits WRIT 1301 and 4 credits in ENGL 1999 | Literature requirement & First-year Writing requirement”
### `fa8c3f081552d8d3` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: Approximately $9,000 each year for four years ⟵ “Norman Family Scholarship | Approximately $9,000 each year for four years | Based on financial needPreference for students from Red Wing High School, or high schools in Goodhue or Wabasha counties”
  - eligibility_summary: Based on financial needPreference for students from Red Wing High School, or high schools in Goodhue or Wabasha counties ⟵ “Norman Family Scholarship | Approximately $9,000 each year for four years | Based on financial needPreference for students from Red Wing High School, or high schools in Goodhue or Wabasha counties”
### `fd787afea2a3df71` University of Minnesota-Twin Cities — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/cost-aid/scholarships/college-specific-scholarships (sha256 f90f3a49dd01)
- checks: {"thresholds": null}
  - award_amount_text: 114 awards of $2,000 for spring semester ⟵ “Dean's First-Year Research and Creative Scholars (DFRACS) Scholarships | 114 awards of $2,000 for spring semester | Incoming freshman or fall transfer students with academic merit and interest in research or creative projects”
  - eligibility_summary: Incoming freshman or fall transfer students with academic merit and interest in research or creative projects ⟵ “Dean's First-Year Research and Creative Scholars (DFRACS) Scholarships | 114 awards of $2,000 for spring semester | Incoming freshman or fall transfer students with academic merit and interest in research or creative projects”
### `3476924780800304` University of Minnesota-Twin Cities — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/international-baccalaureate-course-awards (sha256 eacc6162d812)
- checks: {"distinct_exams": 14, "equivalencies": 14, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL 5-7]:  ⟵ “Biology HL | 5-7 | 4 credits in Biology 1009 (General Biology) | Biological Sciences/lab requirement”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 5-7]:  ⟵ “Business Management HL | 5-7 | 4 credits in MGMT 1999 | No Liberal Education requirement awarded”
  - equivalencies[IB-CHEMISTRY-HL|HL 5-7]:  ⟵ “Chemistry HL | 5-7 | 3 credits in CHEM 1061, 3 credits in CHEM 1062, 1 credit in CHEM Lab 1065, and 1 credit in CHEM Lab 1066 | Physical Sciences/lab requirement”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 5-7]:  ⟵ “Computer Science HL | 5-7 | 4 credits in CSCI 1103 and 4 credits in CSCI 1999 | No Liberal Education requirement awarded”
  - equivalencies[IB-ECONOMICS-HL|HL 5-7]:  ⟵ “Economics HL | 5-7 | 4 credits in ECON 1101 and 4 credits in ECON 1102 | 2 Social Sciences core requirements”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|HL 5-7]:  ⟵ “English A Literature HL | 5-7 | 8 credits in ENGL 1999 | Literature requirement”
  - equivalencies[IB-FRENCH-HL|HL 5-7]:  ⟵ “French HL | 5-7 | 3 credits in FREN 3015 | Fulfills CLA second language requirement”
  - equivalencies[IB-GERMAN-HL|HL 5-7]:  ⟵ “German HL | 5-7 | 4 credits in GER 3011W | Fulfills CLA second language requirement; does NOT fulfill Writing Intensive requirement”
  - equivalencies[IB-HISTORY-HL|HL 5-7]:  ⟵ “History HL | 5-7 | 8 credits in HIST 1999 | Historical Perspectives requirement & Global Perspectives requirement”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|HL 5-7]:  ⟵ “Math HL Applications & Interpretation | 5-7 | 4 credits in MATH 1271 and 4 credits in STAT 3011 | Mathematical Thinking requirement”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|HL 5-7]:  ⟵ “Math HL Analysis & Approaches | 5-7 | 4 credits in MATH 1271 and 4 credits in MATH 1272 | Mathematical Thinking requirement”
  - equivalencies[IB-PHYSICS-HL|HL 5-7]:  ⟵ “Physics HL | 5-7 | 4 credits PHYS 1301 and 4 credits in PHYS 1302 | Physical Sciences/lab requirement”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 5-7]:  ⟵ “Psychology HL | 5-7 | 4 credits PSY 1001 and PSY 1999 | Social Sciences requirement”
  - equivalencies[IB-SPANISH-HL|HL 5-7]:  ⟵ “Spanish A HL | 5-7 | 4 credits in SPAN 3015W | Fulfills CLA second language requirement; does NOT fulfill Writing Intensive requirement”
### `769c73e952a3aef7` Winona State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.winona.edu/financial-aid/paying-for-college/scholarships/ (sha256 a6db26e6073b)
- checks: {"thresholds": null}
  - gpa_requirement: GPA (based on a 4.0 scale): 3.90-3.99 cumulative high school GPA ⟵ “3.90-3.99 cumulative high school GPA | $2,500”
  - award_amount_text: $2,500 ⟵ “3.90-3.99 cumulative high school GPA | $2,500”
### `b4401fe18a128761` Winona State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.winona.edu/financial-aid/paying-for-college/scholarships/ (sha256 a6db26e6073b)
- checks: {"thresholds": null}
  - gpa_requirement: GPA (based on a 4.0 scale): 3.30-3.79 cumulative high school GPA ⟵ “3.30-3.79 cumulative high school GPA | $1,000”
  - award_amount_text: $1,000 ⟵ “3.30-3.79 cumulative high school GPA | $1,000”
### `bd8b9b54c95b53c3` Winona State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.winona.edu/financial-aid/paying-for-college/scholarships/ (sha256 a6db26e6073b)
- checks: {"thresholds": null}
  - gpa_requirement: GPA (based on a 4.0 scale): 3.80-3.89 cumulative high school GPA ⟵ “3.80-3.89 cumulative high school GPA | $1,500”
  - award_amount_text: $1,500 ⟵ “3.80-3.89 cumulative high school GPA | $1,500”
### `def6f76603b84f78` Winona State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.winona.edu/financial-aid/paying-for-college/scholarships/ (sha256 a6db26e6073b)
- checks: {"thresholds": null}
  - gpa_requirement: GPA (based on a 4.0 scale): 4.00 cumulative high school GPA ⟵ “4.00 cumulative high school GPA | $3,500”
  - award_amount_text: $3,500 ⟵ “4.00 cumulative high school GPA | $3,500”

## Exceptions (273)

### `5bf9d521ea8bd63d` Anoka Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.anokatech.edu/student-services/satisfactory-academic-progress-sap-standards/ (sha256 e9a1773dd6a7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “SAP Resources and Information SAP Appeal Resources Printing Your Academic Record/Transcript: A guide for accessing and printing your unofficial academic transcript within eServices.”
  - sentence: sap_appeal ⟵ “SAP Appeal Deadlines The final deadline to appeal to attend Summer Semester 2026 is noon (12 pm) on Wednesday, May 27, 2026.”
  - sentence: sap_appeal ⟵ “SAP Appeal Form Review the documents under SAP Appeal Resources prior to submitting your SAP Appeal.”
  - sentence: sap_appeal ⟵ “Submit SAP Appeal Quick Links Records & Registration Counseling Services Financial Aid & FAFSA Student Services Contact Izy Mortenson, Success Coach izy.mortenson@anokatech.edu 763-576-4037 Danni Munro, Success Coach danni.munro@anokatech.edu 763-576-4002 Counseling 763-576-7860 Records & Registration 763-576-7740 Financial Aid 763-576-7730 On this page: Take the Next Step Apply Programs Financial”
### `807d5b0ee52661fa` Anoka Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.anokatech.edu/financial-aid-fafsa/ (sha256 49bff03f588b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “If the student feels that the parent information is not relevant or the parents are unable to be located, the student may apply for a dependency override with proper documentation.”
  - sentence: dependency_override ⟵ “None of the following conditions, either singly or in combination, will qualify a student for a dependency override: Parents refuse to contribute to child’s education.”
### `af0cb178e4af2f2d` Anoka Technical College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.anokatech.edu/media/xcjjt4ub/2024-2025-technical-scholarship-application.pdf (sha256 9d5c2f4d15f9)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial need and any special circumstances.  Letter of reference from an instructor, academic counselor, or public works professional, indicating knowledge of the applicant’s interest in a career in the field of public works.”
### `c4a7cd7790547451` Anoka Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.anokatech.edu/financial-aid-fafsa/scholarships-grants-loans/ (sha256 d39e2b257593)
- issues: semantic_review_required, conflicting_sources:https://www.anokatech.edu/financial-aid-fafsa/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Scholarship criteria includes scholastic achievement, financial need and special circumstances, educational and career goals and instructor recommendations.”
### `dc78534deeb228f1` Anoka Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.anokatech.edu/financial-aid-fafsa/ (sha256 49bff03f588b)
- issues: semantic_review_required, conflicting_sources:https://www.anokatech.edu/financial-aid-fafsa/scholarships-grants-loans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “It is our policy to select all students applying for a consideration of special circumstances for verification.”
### `b4c7f050c9659115` Anoka Technical College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.anokatech.edu/tuition-fees/budget-estimate-cost/ (sha256 fb606fd010bc)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 5225 ⟵ “Tuition & Fees | $5,225”
  - column:Books & Supplies: 1520 ⟵ “Books & Supplies | $1,520”
  - column:Living Expenses (Food & Housing): 15840 ⟵ “Living Expenses (Food & Housing) | $15,840”
  - column:Miscellaneous Personal Expenses: 2600 ⟵ “Miscellaneous Personal Expenses | $2,600”
  - column:Transportation: 2010 ⟵ “Transportation | $2,010”
  - column:Loan Fees: 70 ⟵ “Loan Fees | $70”
  - column:Total: 27265 ⟵ “Total | $27,265”
### `986499d9fff7026f` Anoka-Ramsey Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.anokaramsey.edu/admissions/financial-aid/index.html (sha256 b7112c60d7c6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “If the student feels that the parent information is not relevant or the parents are unable to be located, the student may apply for a dependency override with proper documentation.”
  - sentence: dependency_override ⟵ “None of the following conditions, either singly or in combination, will qualify a student for a dependency override: Parents refuse to contribute to child’s education.”
### `b221c123c37f2ffe` Anoka-Ramsey Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.anokaramsey.edu/admissions/financial-aid/index.html (sha256 b7112c60d7c6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “It is our policy to select all students applying for a consideration of special circumstances for verification.”
### `82dd11b5b4d53aa5` Anoka-Ramsey Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.anokaramsey.edu/admissions/tuition-and-fees/budget-estimate-cost.html (sha256 379584a5b424)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 6500 ⟵ “Tuition and Fees | $6,500”
  - column:Books and Supplies: 1520 ⟵ “Books and Supplies | $1,520”
  - column:Living Expenses (food and housing): 15840 ⟵ “Living Expenses (food and housing) | $15,840”
  - column:Miscellaneous Personal Expenses: 2600 ⟵ “Miscellaneous Personal Expenses | $2,600”
  - column:Transportation: 2010 ⟵ “Transportation | $2,010”
  - column:Total: 28470 ⟵ “Total | $28,470”
### `2c8a4a77442b77c4` Augsburg University — appeals 2026-27 [new] (labeled_in_title)
- source: https://web.augsburg.edu/enroll/Forms/2627/2627SCIndependent.pdf (sha256 429a1299a404)
- issues: semantic_review_required, conflicting_sources:https://web.augsburg.edu/enroll/Forms/2627/2627SCDependent.pdf,https://www.augsburg.edu/studentfinancial/financial-aid/specialcircumstances/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstance Application - Independent Students Student’s Last Name:_______________________________ Student’s First Name:____________________________________ Augsburg ID:______________________________________ Augsburg E-mail:_______________________________________ Student’s Phone:___________________________________ 1.”
  - sentence: need_based_special_circumstances ⟵ “Attach a written statement explaining your special circumstance in detail. *Additional documentation may be necessary.”
  - sentence: need_based_special_circumstances ⟵ “Attach a written statement explaining your special circumstance in detail.”
### `7c88f3ca33e673af` Augsburg University — appeals 2025-26 [new] (labeled_in_title)
- source: https://web.augsburg.edu/enroll/Forms/2526/2526SCIndependent.pdf (sha256 fb839a18cff6)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://web.augsburg.edu/enroll/Forms/2526/2526SCDependent.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “2025-2026 Special Circumstance Application - Independent Students Student’s Last Name:_______________________________ Student’s First Name:____________________________________ Augsburg ID:______________________________________ Augsburg E-mail:_______________________________________ Student’s Phone:___________________________________ 1.”
  - sentence: need_based_special_circumstances ⟵ “Attach a written statement explaining your special circumstance in detail. *Additional documentation may be necessary.”
  - sentence: need_based_special_circumstances ⟵ “Attach a written statement explaining your special circumstance in detail.”
### `8bdb0bde5394e813` Augsburg University — appeals 2026-27 [new] (labeled_in_title)
- source: https://web.augsburg.edu/enroll/Forms/2627/2627SCDependent.pdf (sha256 7138872750a0)
- issues: semantic_review_required, conflicting_sources:https://web.augsburg.edu/enroll/Forms/2627/2627SCIndependent.pdf,https://www.augsburg.edu/studentfinancial/financial-aid/specialcircumstances/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstance Application - Dependent Students Student’s Last Name:________________________________ Student’s First Name:_________________________________ Parent’s Last Name:_________________________________ Parent’s First Name:__________________________________ Augsburg ID:_______________________________________ Parent’s E-mail:_____________________________________ 1.”
  - sentence: need_based_special_circumstances ⟵ “Attach a written statement explaining your special circumstance in detail. *Additional documentation may be necessary.”
  - sentence: need_based_special_circumstances ⟵ “Attach a written statement explaining your special circumstance in detail.”
### `8d63bd522a25ea93` Augsburg University — appeals 2025-26 [new] (labeled_in_title)
- source: https://web.augsburg.edu/enroll/Forms/2526/2526SCDependent.pdf (sha256 d4064f8d57a0)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://web.augsburg.edu/enroll/Forms/2526/2526SCIndependent.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “2025-2026 Special Circumstance Application - Dependent Students Student’s Last Name:________________________________ Student’s First Name:_________________________________ Parent’s Last Name:_________________________________ Parent’s First Name:__________________________________ Augsburg ID:_______________________________________ Parent’s E-mail:_____________________________________ 1.”
  - sentence: need_based_special_circumstances ⟵ “Attach a written statement explaining your special circumstance in detail. *Additional documentation may be necessary.”
  - sentence: need_based_special_circumstances ⟵ “Attach a written statement explaining your special circumstance in detail.”
### `b81e340c4ff2441e` Augsburg University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augsburg.edu/studentfinancial/policies/sap-policy/ (sha256 4b43669fd9a4)
- issues: semantic_review_required, conflicting_sources:https://web.augsburg.edu/enroll/Forms/SAP_Appeal_Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students may appeal their Financial Aid Suspension by submitting the SAP Appeal Form within 7 days of notification or by the due date given on the notification letter.”
### `b98e01058aeb2fa6` Augsburg University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augsburg.edu/studentfinancial/financial-aid/scholarships/ (sha256 7391e98d2686)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Any increase to a student’s COA is a professional judgment and, thus, requires appropriate documentation and review by a counselor.”
### `c0122838307c3ee2` Augsburg University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.augsburg.edu/studentfinancial/financial-aid/specialcircumstances/ (sha256 1c8af8ee0575)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://web.augsburg.edu/enroll/Forms/2627/2627SCDependent.pdf,https://web.augsburg.edu/enroll/Forms/2627/2627SCIndependent.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Application A special circumstance is when the information provided on the FAFSA form is not reflective of the family’s financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance requests are considered each spring through summer prior to the start of the upcoming academic year.”
  - sentence: need_based_special_circumstances ⟵ “In order for your Special Circumstance to be reviewed you must submit an application as well as all additional requested information.”
  - sentence: need_based_special_circumstances ⟵ “Students in this situation should: Indicate this situation on their FAFSA, and Submit the Special Circumstance Application for Dependent Students Without Parental Support OR provide a signed and dated letter from their parent stating their refusal to provide support and/or complete the FAFSA Students who are unable to provide a signed/dated letter from their parent may provide documentation from a”
  - sentence: need_based_special_circumstances ⟵ “The student and parent will be e-mailed a Special Circumstance Form.”
### `d8d56d671fe33af8` Augsburg University — appeals 2026-27 [new] (source_unlabeled)
- source: https://web.augsburg.edu/enroll/Forms/SAP_Appeal_Form.pdf (sha256 10a1a930d777)
- issues: semantic_review_required, conflicting_sources:https://www.augsburg.edu/studentfinancial/policies/sap-policy/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Form Your appeal will be decided by the SAP Committee.”
  - sentence: sap_appeal ⟵ “Sign Satisfactory Academic Progress Suspension Appeal Form 2.”
### `3238b60464642de1` Bemidji State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bemidjistate.edu/mybsu/finances/aid/ (sha256 f4792a70e020)
- issues: residency_unknown
- checks: {"columns": 1, "components_per_semester": true, "components_reconcile": true, "rows": 6}
  - column:Tuition*: 5077 ⟵ “Tuition* | $ 5,077”
  - column:Fees: 658 ⟵ “Fees | $ 658”
  - column:Books and supplies: 445 ⟵ “Books and supplies | $ 445”
  - column:Housing and Food**: 6301 ⟵ “Housing and Food** | $ 6,301”
  - column:Miscellaneous personal expenses: 1500 ⟵ “Miscellaneous personal expenses | $ 1,500”
  - column:Total Annual COA: 27962 ⟵ “Total Annual COA | $ 27,962”
### `a99830e1673fad89` Bemidji State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.bemidjistate.edu/admissions/transfer/transfer-credits/ap-and-clep-equivalencies/ (sha256 e576a4802b7b)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 32, "equivalencies": 55, "rows_without_score": 0}
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature & Composition | 3 | 3 | Composition (ENGL 1151) | 1”
  - equivalencies[CLEP-ENGLISH-LITERATURE|4 or 5]:  ⟵ “English Literature & Composition | 4 or 5 | 6 | Composition (ENGL 1151), Argument and Exposition (ENGL 2152) | 1”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3, 4, or 5]:  ⟵ “Macroeconomics | 3, 4, or 5 | 3 | Macroeconomics and the Business Cycle (ECON 2100) | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3, 4, or 5]:  ⟵ “Microeconomics | 3, 4, or 5 | 3 | Markets and Resource Allocation (ECON 2000) | 5, 9”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3, 4, or 5]:  ⟵ “Psychology | 3, 4, or 5 | 4 | Introductory Psychology (PSY 1100) | 5”
  - equivalencies[CLEP-PRECALCULUS|3, 4, or 5]:  ⟵ “Precalculus | 3, 4, or 5 | 5 | Precalculus (MATH1470) | 4”
  - equivalencies[CLEP-CALCULUS|3, 4, or 5]:  ⟵ “Calculus AB | 3, 4, or 5 | 5 | Calculus I (MATH 2471) | 4”
  - equivalencies[CLEP-CALCULUS|3, 4, or 5]:  ⟵ “Calculus BC | 3, 4, or 5 | 10 | Calculus I (MATH 2471), Calculus II (MATH 2472) | 4”
  - equivalencies[CLEP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | Human Biology (BIOL 1110) | 3”
  - equivalencies[CLEP-BIOLOGY|4 or 5]:  ⟵ “Biology | 4 or 5 | 8 | Cellular Principles (BIOL 1400), Diversity of Life (BIOL 1500) | 3”
  - equivalencies[CLEP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | General Chemistry I (CHEM 1111) | 3”
  - equivalencies[CLEP-CHEMISTRY|4 or 5]:  ⟵ “Chemistry | 4 or 5 | 8 | General Chemistry I (CHEM 1111), General Chemistry II (CHEM 1112) | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|3]:  ⟵ “German Language & Culture | 3 | 4 | Elementary German I (GER 1111) | ”
  - equivalencies[CLEP-GERMAN-LANGUAGE|4. 5]:  ⟵ “German Language & Culture | 4. 5 | 8 | Elementary German I (GER 1111), Elementary German II (GER 1112) | ”
  - equivalencies[CLEP-SPANISH-LANGUAGE|3]:  ⟵ “Spanish Language & Culture | 3 | 8 | Elementary Spanish I (SPAN 1111), Elementary Spanish II (SPAN 1112) | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|4]:  ⟵ “Spanish Language & Culture | 4 | 11 | Elementary Spanish I (SPAN 1111), Elementary Spanish II (SPAN 1112), Intermediate Spanish I (SPAN 2211) | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|5]:  ⟵ “Spanish Language & Culture | 5 | 15 | Elementary Spanish I (SPAN 1111), Elementary Spanish II (SPAN 1112), Intermediate Spanish I (SPAN 2211), Intermediate Spanish II (SPAN 2212) | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|3]:  ⟵ “Spanish Literature & Culture | 3 | 3 | SPAN 3910 | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|4 or 5]:  ⟵ “Spanish Literature & Culture | 4 or 5 | 6 | SPAN 3910 | 8”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 | UNIV 1910 | 6, 7”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | 3 | UNIV 1910 | 6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 | Composition (ENGL 1151) | 1”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|54]:  ⟵ “College Composition | 54 | 6 | Composition (ENGL 1151), Argument and Exposition (ENGL 2152) | 1”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 3 | Composition (ENGL 1151) | 1”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|54]:  ⟵ “College Composition Modular | 54 | 6 | Composition (ENGL 1151), Argument and Exposition (ENGL 2152) | 1”
  - … 30 more rows
### `2053841552486a11` Bethel University — academic_programs 2026-27 · program_key=b-s-in-actuarial-science-and-finance [new] (labeled_in_source)
- source: https://catalog.bethel.edu/academic-programs/school-of-business/undergraduate/business/actuarial-science-and-finance-bs/ (sha256 c718670dc947)
- issues: requirement_groups_skipped
- checks: {"courses": 26, "groups": 1, "groups_skipped": 1}
  - program_name: B.S. in Actuarial Science and Finance ⟵ “B.S. in Actuarial Science and Finance | Bethel University Catalog”
### `29e6096f9fb91802` Bethel University — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.bethel.edu/tuition/financial-aid/ (sha256 e196d237dbea)
- issues: semantic_review_required, conflicting_sources:https://www.bethel.edu/adult-undergrad/financial-aid/eligibility/academic-progress
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Appeal forms are available at Special Circumstances Financial Aid webpage.”
  - sentence: need_based_special_circumstances ⟵ “However, there may be special circumstances, like a program change or an illness, that would prevent students from completing their programs of study within the normal time frame.”
  - sentence: need_based_special_circumstances ⟵ “To accommodate these special circumstances, students may continue receiving aid until they either (a) complete graduation requirements for their program of study, or (b) attempt 150% of the number of credits (including transfer credits, advanced placement or CLEP credits) required for their program of study, or (c) reach the point where they cannot earn the number of credits necessary to complete ”
### `46030e36fd51ddaa` Bethel University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bethel.edu/adult-undergrad/financial-aid/eligibility/academic-progress (sha256 3f145fb274d7)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://catalog.bethel.edu/tuition/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “However, special circumstances (e.g., program changes or illness) may prevent students from completing their program within this timeframe.”
### `da195d381386dabe` Bethel University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bethel.edu/adult-undergrad/financial-aid/eligibility/academic-progress (sha256 3f145fb274d7)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal of financial aid termination Students who fail to meet satisfactory academic progress standards and lose financial aid eligibility may appeal this decision.”
  - sentence: sap_appeal ⟵ “Students who cannot demonstrate satisfactory academic progress within one term will be required to submit an academic plan as part of their appeal.”
### `1a1f5fc578193d69` Bethel University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bethel.edu/undergrad/financial-aid/tuition-costs/tuition-26-27 (sha256 0ebf4ea9f8c1)
- issues: components_do_not_reconcile, conflicting_sources:https://catalog.bethel.edu/tuition/undergraduate-tuition-and-finances/tuition-payment-options/,https://www.bethel.edu/adult-undergrad/financial-aid/tuition-costs/refunds,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/cost-of-attendance-26-27,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/refunds
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - column:Tuition and fees (12-18 credits fall, 12-23 credits spring): 26700 ⟵ “Tuition and fees (12-18 credits fall, 12-23 credits spring) | $26,700”
  - column:Room (new student rate): 7200 ⟵ “Room (new student rate) | $7,200”
  - column:Food: 6548 ⟵ “Food | $6,548”
  - column:Student activity fee (if full-time): 300 ⟵ “Student activity fee (if full-time) | $300”
  - column:Total direct costs: 40750 ⟵ “Total direct costs | $40,750”
### `531bf2a6c4239ae8` Bethel University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.bethel.edu/adult-undergrad/financial-aid/tuition-costs/refunds (sha256 413363a8bd32)
- issues: ambiguous_year_labels, arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://catalog.bethel.edu/tuition/undergraduate-tuition-and-finances/tuition-payment-options/,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/cost-of-attendance-26-27,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/refunds,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/tuition-26-27
- checks: {"columns": 3, "rows": 8}
  - column:Tuition: 21380 ⟵ “Tuition | $21,380 | 90% | ($19,242) | $2,138”
  - column:Room: 3145 ⟵ “Room | $3,145 | 90% | ($2,831) | $314”
  - column:Class Fee (e.g., lab): 65 ⟵ “Class Fee (e.g., lab) | $65 | 0% | $0 | $65”
  - column:Meal Plan: 2830 ⟵ “Meal Plan | $2,830 | 90% | $(2,547) | $283”
  - column:Student Activity Fee: 85 ⟵ “Student Activity Fee | $85 | 0% | $0 | $85”
  - column:Total Charges: 27505 ⟵ “Total Charges | $27,505 |  | ($24,620) | $2,885”
  - column:Total Charges (2): 27505 ⟵ “Total Charges | $27,505 |  | ($24,620) | $2,885”
  - column:Difference*: 4207 ⟵ “Difference* | $4,207 |  | ($6,957) | ($2,750)”
  - column:Class Fee (e.g., lab): 0 ⟵ “Class Fee (e.g., lab) | $65 | 0% | $0 | $65”
  - column:Student Activity Fee: 0 ⟵ “Student Activity Fee | $85 | 0% | $0 | $85”
  - column:Federal Stafford Loan: 2750 ⟵ “Federal Stafford Loan | ($2,750) | 100% | $2,750 | $0”
  - column:Federal Pell Grant: 2470 ⟵ “Federal Pell Grant | ($3,175) | 78% | $2,470 | ($705)”
  - column:Minnesota State Grant: 2880 ⟵ “Minnesota State Grant | ($3,248) | 89% | $2,880 | ($368)”
  - column:Bethel Royal Merit Scholarship: 6840 ⟵ “Bethel Royal Merit Scholarship | ($7,600) | 90% | $6,840 | ($760)”
  - column:Bethel Grant: 2723 ⟵ “Bethel Grant | ($3,025) | 90% | $2,723 | ($302)”
  - column:Private Scholarship: 0 ⟵ “Private Scholarship | ($500) | 0% | $0 | ($500)”
  - column:Sub-total: 17663 ⟵ “Sub-total | ($20,298) | 87% | $17,663 | ($2,635)”
  - column:Total Payments on Account: 17663 ⟵ “Total Payments on Account | ($23,298) |  | $17,663 | ($5,635)”
  - column:Tuition: 2138 ⟵ “Tuition | $21,380 | 90% | ($19,242) | $2,138”
  - column:Room: 314 ⟵ “Room | $3,145 | 90% | ($2,831) | $314”
  - column:Class Fee (e.g., lab): 65 ⟵ “Class Fee (e.g., lab) | $65 | 0% | $0 | $65”
  - column:Meal Plan: 283 ⟵ “Meal Plan | $2,830 | 90% | $(2,547) | $283”
  - column:Student Activity Fee: 85 ⟵ “Student Activity Fee | $85 | 0% | $0 | $85”
  - column:Total Charges: 2885 ⟵ “Total Charges | $27,505 |  | ($24,620) | $2,885”
  - column:Federal Stafford Loan: 0 ⟵ “Federal Stafford Loan | ($2,750) | 100% | $2,750 | $0”
  - … 1 more rows
### `98af0723d4b1d549` Bethel University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.bethel.edu/tuition/undergraduate-tuition-and-finances/tuition-payment-options/ (sha256 19a5200bd0b9)
- issues: arrangement_unlabeled, conflicting_sources:https://www.bethel.edu/adult-undergrad/financial-aid/tuition-costs/refunds,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/cost-of-attendance-26-27,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/refunds,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/tuition-26-27
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - column:Tuition: 13350.0 ⟵ “Tuition | $13,350.00 | 90% | ($12,015.00) | $1,335.00”
  - column:Housing: 3600.0 ⟵ “Housing | $3,600.00 | 90% | ($3,240.00) | $360.00”
  - column:Meal Plan: Navy A: 3275.0 ⟵ “Meal Plan: Navy A | $3,275.00 | 90% | ($2,947.50) | $327.50”
  - column:Student Activity Fee: 150.0 ⟵ “Student Activity Fee | $150.00 | 0% | 0 | $150.00”
  - column:Class Fee (e.g., Lab): 85.0 ⟵ “Class Fee (e.g., Lab) | $85.00 | 0% | 0 | $85.00”
  - column:Total Charges: 20460.0 ⟵ “Total Charges | $20,460.00 |  | ($18,202.50) | $2,257.50”
  - column:Student Activity Fee: 0 ⟵ “Student Activity Fee | $150.00 | 0% | 0 | $150.00”
  - column:Class Fee (e.g., Lab): 0 ⟵ “Class Fee (e.g., Lab) | $85.00 | 0% | 0 | $85.00”
  - column:Tuition: 1335.0 ⟵ “Tuition | $13,350.00 | 90% | ($12,015.00) | $1,335.00”
  - column:Housing: 360.0 ⟵ “Housing | $3,600.00 | 90% | ($3,240.00) | $360.00”
  - column:Meal Plan: Navy A: 327.5 ⟵ “Meal Plan: Navy A | $3,275.00 | 90% | ($2,947.50) | $327.50”
  - column:Student Activity Fee: 150.0 ⟵ “Student Activity Fee | $150.00 | 0% | 0 | $150.00”
  - column:Class Fee (e.g., Lab): 85.0 ⟵ “Class Fee (e.g., Lab) | $85.00 | 0% | 0 | $85.00”
  - column:Total Charges: 2257.5 ⟵ “Total Charges | $20,460.00 |  | ($18,202.50) | $2,257.50”
### `b0e215512b70ef09` Bethel University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bethel.edu/undergrad/financial-aid/tuition-costs/refunds (sha256 8e118e002e8d)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://catalog.bethel.edu/tuition/undergraduate-tuition-and-finances/tuition-payment-options/,https://www.bethel.edu/adult-undergrad/financial-aid/tuition-costs/refunds,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/cost-of-attendance-26-27,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/tuition-26-27
- checks: {"columns": 3, "rows": 8}
  - column:Tuition: 21380 ⟵ “Tuition | $21,380 | 90% | ($19,242) | $2,138”
  - column:Room: 3145 ⟵ “Room | $3,145 | 90% | ($2,831) | $314”
  - column:Class Fee (e.g., lab): 65 ⟵ “Class Fee (e.g., lab) | $65 | 0% | $0 | $65”
  - column:Meal Plan: 2830 ⟵ “Meal Plan | $2,830 | 90% | $(2,547) | $283”
  - column:Student Activity Fee: 85 ⟵ “Student Activity Fee | $85 | 0% | $0 | $85”
  - column:Total Charges: 27505 ⟵ “Total Charges | $27,505 |  | ($24,620) | $2,885”
  - column:Total Charges (2): 27505 ⟵ “Total Charges | $27,505 |  | ($24,620) | $2,885”
  - column:Difference*: 4207 ⟵ “Difference* | $4,207 |  | ($6,957) | ($2,750)”
  - column:Class Fee (e.g., lab): 0 ⟵ “Class Fee (e.g., lab) | $65 | 0% | $0 | $65”
  - column:Student Activity Fee: 0 ⟵ “Student Activity Fee | $85 | 0% | $0 | $85”
  - column:Federal Stafford Loan: 2750 ⟵ “Federal Stafford Loan | ($2,750) | 100% | $2,750 | $0”
  - column:Federal Pell Grant: 2470 ⟵ “Federal Pell Grant | ($3,175) | 78% | $2,470 | ($705)”
  - column:Minnesota State Grant: 2880 ⟵ “Minnesota State Grant | ($3,248) | 89% | $2,880 | ($368)”
  - column:Bethel Royal Merit Scholarship: 6840 ⟵ “Bethel Royal Merit Scholarship | ($7,600) | 90% | $6,840 | ($760)”
  - column:Bethel Grant: 2723 ⟵ “Bethel Grant | ($3,025) | 90% | $2,723 | ($302)”
  - column:Private Scholarship: 0 ⟵ “Private Scholarship | ($500) | 0% | $0 | ($500)”
  - column:Sub-total: 17663 ⟵ “Sub-total | ($20,298) | 87% | $17,663 | ($2,635)”
  - column:Total Payments on Account: 17663 ⟵ “Total Payments on Account | ($23,298) |  | $17,663 | ($5,635)”
  - column:Tuition: 2138 ⟵ “Tuition | $21,380 | 90% | ($19,242) | $2,138”
  - column:Room: 314 ⟵ “Room | $3,145 | 90% | ($2,831) | $314”
  - column:Class Fee (e.g., lab): 65 ⟵ “Class Fee (e.g., lab) | $65 | 0% | $0 | $65”
  - column:Meal Plan: 283 ⟵ “Meal Plan | $2,830 | 90% | $(2,547) | $283”
  - column:Student Activity Fee: 85 ⟵ “Student Activity Fee | $85 | 0% | $0 | $85”
  - column:Total Charges: 2885 ⟵ “Total Charges | $27,505 |  | ($24,620) | $2,885”
  - column:Federal Stafford Loan: 0 ⟵ “Federal Stafford Loan | ($2,750) | 100% | $2,750 | $0”
  - … 1 more rows
### `cdb3929a99e34b6e` Bethel University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bethel.edu/undergrad/financial-aid/tuition-costs/cost-of-attendance-26-27 (sha256 723741164af2)
- issues: conflicting_sources:https://catalog.bethel.edu/tuition/undergraduate-tuition-and-finances/tuition-payment-options/,https://www.bethel.edu/adult-undergrad/financial-aid/tuition-costs/refunds,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/refunds,https://www.bethel.edu/undergrad/financial-aid/tuition-costs/tuition-26-27
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition/fees (est.): 27000 ⟵ “Tuition/fees (est.) | $27,000 | $27,000 | $27,000”
  - on_campus:Housing (est.): 7200 ⟵ “Housing (est.) | $7,200 | $4,490 | 0”
  - on_campus:Food allowance (est.): 6550 ⟵ “Food allowance (est.) | $6,550 | $6,130 | $6,130”
  - on_campus:Books/supplies/equipment (est., not billable): 1240 ⟵ “Books/supplies/equipment (est., not billable) | $1,240 | $1,240 | $1,240”
  - on_campus:Misc. personal expenses (est., not billable): 2210 ⟵ “Misc. personal expenses (est., not billable) | $2,210 | $5,722 | $4,492”
  - on_campus:Transportation (est., not billable): 560 ⟵ “Transportation (est., not billable) | $560 | $1,836 | $1,842”
  - on_campus:Fed/loan/course/misc fees (est., not billable) View full list of course fees: 390 ⟵ “Fed/loan/course/misc fees (est., not billable) View full list of course fees | $390 | $390 | $390”
  - on_campus:Total (fall and spring): 45150 ⟵ “Total (fall and spring) | $45,150 | $46,808 | $41,094”
  - off_campus_not_with_family:Tuition/fees (est.): 27000 ⟵ “Tuition/fees (est.) | $27,000 | $27,000 | $27,000”
  - off_campus_not_with_family:Housing (est.): 4490 ⟵ “Housing (est.) | $7,200 | $4,490 | 0”
  - off_campus_not_with_family:Food allowance (est.): 6130 ⟵ “Food allowance (est.) | $6,550 | $6,130 | $6,130”
  - off_campus_not_with_family:Books/supplies/equipment (est., not billable): 1240 ⟵ “Books/supplies/equipment (est., not billable) | $1,240 | $1,240 | $1,240”
  - off_campus_not_with_family:Misc. personal expenses (est., not billable): 5722 ⟵ “Misc. personal expenses (est., not billable) | $2,210 | $5,722 | $4,492”
  - off_campus_not_with_family:Transportation (est., not billable): 1836 ⟵ “Transportation (est., not billable) | $560 | $1,836 | $1,842”
  - off_campus_not_with_family:Fed/loan/course/misc fees (est., not billable) View full list of course fees: 390 ⟵ “Fed/loan/course/misc fees (est., not billable) View full list of course fees | $390 | $390 | $390”
  - off_campus_not_with_family:Total (fall and spring): 46808 ⟵ “Total (fall and spring) | $45,150 | $46,808 | $41,094”
  - with_parents_or_family:Tuition/fees (est.): 27000 ⟵ “Tuition/fees (est.) | $27,000 | $27,000 | $27,000”
  - with_parents_or_family:Housing (est.): 0 ⟵ “Housing (est.) | $7,200 | $4,490 | 0”
  - with_parents_or_family:Food allowance (est.): 6130 ⟵ “Food allowance (est.) | $6,550 | $6,130 | $6,130”
  - with_parents_or_family:Books/supplies/equipment (est., not billable): 1240 ⟵ “Books/supplies/equipment (est., not billable) | $1,240 | $1,240 | $1,240”
  - with_parents_or_family:Misc. personal expenses (est., not billable): 4492 ⟵ “Misc. personal expenses (est., not billable) | $2,210 | $5,722 | $4,492”
  - with_parents_or_family:Transportation (est., not billable): 1842 ⟵ “Transportation (est., not billable) | $560 | $1,836 | $1,842”
  - with_parents_or_family:Fed/loan/course/misc fees (est., not billable) View full list of course fees: 390 ⟵ “Fed/loan/course/misc fees (est., not billable) View full list of course fees | $390 | $390 | $390”
  - with_parents_or_family:Total (fall and spring): 41094 ⟵ “Total (fall and spring) | $45,150 | $46,808 | $41,094”
### `e76951ad478ca236` Bethel University — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bethel.edu/undergrad/financial-aid/tuition-costs/cost-of-attendance-27-28 (sha256 1a27bc41b2f1)
- issues: conflicting_sources:https://www.bethel.edu/undergrad/financial-aid/tuition-costs/tuition-27-28
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition/fees (est.): 28080 ⟵ “Tuition/fees (est.) | $28,080 | $28,080 | $28,080”
  - on_campus:Housing (est.): 7560 ⟵ “Housing (est.) | $7,560 | $4,630 | 0”
  - on_campus:Food allowance (est.): 6875 ⟵ “Food allowance (est.) | $6,875 | $6,320 | $6,320”
  - on_campus:Books/supplies/equipment (est., not billable): 1280 ⟵ “Books/supplies/equipment (est., not billable) | $1,280 | $1,280 | $1,280”
  - on_campus:Misc. personal expenses (est., not billable): 2280 ⟵ “Misc. personal expenses (est., not billable) | $2,280 | $5,898 | $4,630”
  - on_campus:Transportation (est., not billable): 580 ⟵ “Transportation (est., not billable) | $580 | $1,892 | $1,898”
  - on_campus:Fed/loan/course/misc fees (est., not billable) View full list of course fees: 390 ⟵ “Fed/loan/course/misc fees (est., not billable) View full list of course fees | $390 | $390 | $390”
  - on_campus:Total (fall and spring): 47045 ⟵ “Total (fall and spring) | $47,045 | $48,490 | $42,598”
  - off_campus_not_with_family:Tuition/fees (est.): 28080 ⟵ “Tuition/fees (est.) | $28,080 | $28,080 | $28,080”
  - off_campus_not_with_family:Housing (est.): 4630 ⟵ “Housing (est.) | $7,560 | $4,630 | 0”
  - off_campus_not_with_family:Food allowance (est.): 6320 ⟵ “Food allowance (est.) | $6,875 | $6,320 | $6,320”
  - off_campus_not_with_family:Books/supplies/equipment (est., not billable): 1280 ⟵ “Books/supplies/equipment (est., not billable) | $1,280 | $1,280 | $1,280”
  - off_campus_not_with_family:Misc. personal expenses (est., not billable): 5898 ⟵ “Misc. personal expenses (est., not billable) | $2,280 | $5,898 | $4,630”
  - off_campus_not_with_family:Transportation (est., not billable): 1892 ⟵ “Transportation (est., not billable) | $580 | $1,892 | $1,898”
  - off_campus_not_with_family:Fed/loan/course/misc fees (est., not billable) View full list of course fees: 390 ⟵ “Fed/loan/course/misc fees (est., not billable) View full list of course fees | $390 | $390 | $390”
  - off_campus_not_with_family:Total (fall and spring): 48490 ⟵ “Total (fall and spring) | $47,045 | $48,490 | $42,598”
  - with_parents_or_family:Tuition/fees (est.): 28080 ⟵ “Tuition/fees (est.) | $28,080 | $28,080 | $28,080”
  - with_parents_or_family:Housing (est.): 0 ⟵ “Housing (est.) | $7,560 | $4,630 | 0”
  - with_parents_or_family:Food allowance (est.): 6320 ⟵ “Food allowance (est.) | $6,875 | $6,320 | $6,320”
  - with_parents_or_family:Books/supplies/equipment (est., not billable): 1280 ⟵ “Books/supplies/equipment (est., not billable) | $1,280 | $1,280 | $1,280”
  - with_parents_or_family:Misc. personal expenses (est., not billable): 4630 ⟵ “Misc. personal expenses (est., not billable) | $2,280 | $5,898 | $4,630”
  - with_parents_or_family:Transportation (est., not billable): 1898 ⟵ “Transportation (est., not billable) | $580 | $1,892 | $1,898”
  - with_parents_or_family:Fed/loan/course/misc fees (est., not billable) View full list of course fees: 390 ⟵ “Fed/loan/course/misc fees (est., not billable) View full list of course fees | $390 | $390 | $390”
  - with_parents_or_family:Total (fall and spring): 42598 ⟵ “Total (fall and spring) | $47,045 | $48,490 | $42,598”
### `f5c35f3dcc55b3b2` Bethel University — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bethel.edu/undergrad/financial-aid/tuition-costs/tuition-27-28 (sha256 d52c4fb5489f)
- issues: conflicting_sources:https://www.bethel.edu/undergrad/financial-aid/tuition-costs/cost-of-attendance-27-28
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (12-18 credits fall, 12-23 credits spring): 27480 ⟵ “Tuition (12-18 credits fall, 12-23 credits spring) | $27,480”
  - column:Housing: 7560 ⟵ “Housing | $7,560”
  - column:Meal plans (Navy A full year): 6875 ⟵ “Meal plans (Navy A full year) | $6,875”
  - column:Student experience fee: 600 ⟵ “Student experience fee | $600”
  - column:Total direct costs: 42515 ⟵ “Total direct costs | $42,515”
### `0b0e0206b268be8f` Bethel University — credit_policies 2025-26 · policy_kind=CLEP [new] (labeled_in_url)
- source: https://www.bethel.edu/undergrad/academic-affairs/files/clep-equivalencies-2025-2026.pdf (sha256 a583ccc78969)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 23, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature    50        4         ENJ 100 How Stories Change the”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition (with Essay)       50        4         GES 161 Inquiry Seminar : Writing”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular            50        3         ENJ1--A: Artistic Experience”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                     50        4         ENJ 102 British Literature II”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                             50        4         GES1: General Studies Elective”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                50        3         BIO1: Biology Elective”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                               50        4         MAT 124M Calculus I”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                              50        4         CHE1: Chemistry Elective”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Math                           50        4         MAT1--M: Mathematics”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences                       50        3         GES1: General Education Elective”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                            50        4         MAT 121M Precalculus”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “Level 2 French                         62        14        LAN 101 Introductory Language I;”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “Level 1 German                         50        8         Intermediate”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “Level 2 German                         63        11        LAN 101: Introductory Language I”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Level 1 Spanish                        50        8         SPA 101 Introductory Spanish I”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Level 2 Spanish                        63        14        SPA 101 Introductory Spanish I ; SPA”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development             50        3         PSY 203 Lifespan Development”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “MacroEconomics, Prin                   50        2         ECO203 Principles of”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “MicroEconomics, Prin                   50        2         Macroeconomic”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Intro                      50        4         Microeconomics”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Intro                       50        4         Psychology”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civ 1: Ancient Near East -     50        3         HIS2: History Elective”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law, Intro                    50        2         BUS2: Business Elective”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Prin                       50        4         BUS 230 Managing Operations and”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing                              50        4         BUS 220 Principles of Marketing”
### `6f29eb306956e099` Bethel University — credit_policies 2025-26 · policy_kind=IB [new] (labeled_in_url)
- source: https://www.bethel.edu/undergrad/academic-affairs/files/ib-equivalencies-2025-2026.pdf (sha256 d35c4eaa73c1)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 36, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|4 or 5]:  ⟵ “Biology                 Biology (HL)                        4 or 5        4         BIO 100/100D Principles of Biology”
  - equivalencies[IB-BIOLOGY-HL|6 or Higher]:  ⟵ “Biology (HL)                        6 or Higher   8         BIO 124/124D Integrative Biology: Genes, Cells, Change &”
  - equivalencies[IB-BIOLOGY-SL|5 or Higher]:  ⟵ “Biology (SL)                        5 or Higher   4         BIO1-D: Laboratory Science”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4 or Higher]:  ⟵ “Business Management     Business Management (HL)            4 or Higher   6         BUS1: Business Elective”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|5 or Higher]:  ⟵ “Business Management (SL)            5 or Higher   3         BUS1: Business Elective”
  - equivalencies[IB-CHEMISTRY|4 or Higher]:  ⟵ “Chemistry               Chemistry (HL)                      4 or Higher   6         CHE1-D: Laboratory Science”
  - equivalencies[IB-CHEMISTRY-SL|5 or Higher]:  ⟵ “Chemistry (SL)                      5 or Higher   3         CHE1-D: Laboratory Science”
  - equivalencies[IB-COMPUTER-SCIENCE|4 or Higher]:  ⟵ “Computer Science        Computer Science (HL)               4 or Higher   6         COS1: Computer Science Elective”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|5 or Higher]:  ⟵ “Computer Science (SL)               5 or Higher   3         COS1: Computer Science Elective”
  - equivalencies[IB-ECONOMICS|4 or Higher]:  ⟵ “Economics               Economics (HL)                      4 or Higher   6         ECO1: Economics Elective”
  - equivalencies[IB-ECONOMICS-SL|5 or Higher]:  ⟵ “Economics (SL)                      5 or Higher   3         ECO1: Economics Elective”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|5 or Higher]:  ⟵ “Environmental Systems   Environmental Systems (HL)          5 or Higher   4         ENS 104/104D Environment and Humanity”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|6 or Higher]:  ⟵ “Environmental Systems (SL)          6 or Higher   4         ENS 104/104D Environment and Humanity”
  - equivalencies[IB-GEOGRAPHY|4 or Higher]:  ⟵ “Geography               Geography (HL)                      4 or Higher   4         GEO 120 Introduction to Geography”
  - equivalencies[IB-GEOGRAPHY-SL|5 or Higher]:  ⟵ “Geography (SL)                      5 or Higher   4         GEO 120 Introduction to Geography”
  - equivalencies[IB-HISTORY|5 or Higher]:  ⟵ “History                 History (SL)                        5 or Higher   3         HIS1: History Elective”
  - equivalencies[IB-HISTORY-HL|4 or Higher]:  ⟵ “History of Africa (HL)              4 or Higher   6         Contact Department Chair”
  - equivalencies[IB-SPANISH-SL|5 or Higher]:  ⟵ “Spanish A2 (SL)                     5 or Higher   3         SPA2: Spanish Elective”
  - equivalencies[IB-FRENCH-HL|4 or Higher]:  ⟵ “French (HL)                         4 or Higher   8         LAN 102S Introduction to Second Language II”
  - equivalencies[IB-FRENCH-SL|5 or Higher]:  ⟵ “French (SL)                         5 or Higher   4         LAN 102S Introduction to Second Language II”
  - equivalencies[IB-GERMAN-HL|4 or Higher]:  ⟵ “German (HL)                         4 or Higher   8         LAN102S Introduction to Second Language II”
  - equivalencies[IB-GERMAN-SL|5 or Higher]:  ⟵ “German (SL)                         5 or Higher   4         LAN102S Introduction to Second Language II”
  - equivalencies[IB-SPANISH-HL|4 or Higher]:  ⟵ “Spanish (HL)                        4 or Higher   8         SPA 102S Introductory Spanish II”
  - equivalencies[IB-SPANISH-SL|5 or Higher]:  ⟵ “Spanish (SL)                        5 or Higher   4         SPA 102S Introductory Spanish II”
  - equivalencies[IB-GERMAN-SL|5 or Higher]:  ⟵ “German (SL)                         5 or Higher   4         LAN 101 Introductory Language I course”
  - … 14 more rows
### `7cd1605aded8e883` Bethel University — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_url)
- source: https://www.bethel.edu/undergrad/academic-affairs/files/ap-equivalencies-2025-2026.pdf (sha256 506435700a1f)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 22, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3-5]:  ⟵ “Studio Art: 2D Design Portfolio         3-5            4         ART110 Foundations: The Elements and”
  - equivalencies[AP-3-D-ART-DESIGN|3-5]:  ⟵ “Studio Art: 3D Design Portfolio         3-5            4         ART110 Foundations: The Elements and”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                   Biology                                 3              4         BIO1--D: Laboratory Science”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                                 4              8         BIO 124/124D Integrative Biology: Genes, Cells,”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology                                 5              8         BIO 124/124D Integrative Biology: Genes, Cells,”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                 Chemistry                               3              4         CHE1--D: Laboratory Science”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                               4              4         CHE 113/CHE 113D General Chemistry I”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry                               5              8         CHE 113/CHE 113D General Chemistry I (4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A                      4-5            4         COS 111 Introduction to Programming”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles             3              2         COS1--Computer Science Elective”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles             4-5            2         COS 101 Introduction to Procedural”
  - equivalencies[AP-MICROECONOMICS|3-5]:  ⟵ “Microeconomics                          3-5            2         ECO 202 Principles of Microeconomics”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “French                    French Language                         3-5            8         LAN 101 Introductory Language I & LAN 102S”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3-5]:  ⟵ “French Literature                       3-5            4         LAN1: Second Language Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3-5]:  ⟵ “German                    German Language                         3-5            8         LAN 101 Introductory Language I & LAN 102S”
  - equivalencies[AP-UNITED-STATES-HISTORY|4-5]:  ⟵ “U.S. History                            4-5            6         HIS 200L History of the United States (4 credits)”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History                        3-5            6         HIS2: History Elective”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3-5]:  ⟵ “World History                           3-5            6         HIS2: History Elective”
  - equivalencies[AP-LATIN|3-5]:  ⟵ “Latin                     Virgil                                  3-5            8         LAN 101 Introductory Language I & LAN 102S”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB                             4-5            4         MAT 124M Calculus I”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                             3              6         MAT 124M Calculus I (4 credits) & MAT1--M:”
  - equivalencies[AP-CALCULUS-BC|4-5]:  ⟵ “Calculus BC                             4-5            8         MAT 124M Calculus I & MAT 125 Calculus II”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                             Less than 3,   4         MAT1-M: Mathematics Elective”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC                             Less than 3,   4         MAT 124M Calculus I”
  - equivalencies[AP-STATISTICS|3-5]:  ⟵ “Statistics                              3-5            4         MAT 207M Statistical Analysis”
  - … 8 more rows
### `7f4109692c6ea706` Bethel University — degree_requirements 2026-27 · program_key=b-s-in-actuarial-science-and-finance · requirement_key=b-s-in-actuarial-science-and-finance-major-in-actuarial-science-and-finance-b-s [new] (labeled_in_source)
- source: https://catalog.bethel.edu/academic-programs/school-of-business/undergraduate/business/actuarial-science-and-finance-bs/ (sha256 c718670dc947)
- issues: requirement_groups_skipped
  - courses: BUS 210 ⟵ “BUS 210 - Financial Accounting”
  - courses: BUS 220 ⟵ “BUS 220 - Principles of Marketing”
  - courses: BUS 230 ⟵ “BUS 230 - Managing Organizations and People”
  - courses: BUS 317 ⟵ “BUS 317 - Business Analytics”
  - courses: BUS 344 ⟵ “BUS 344 - Managerial Finance”
  - courses: BUS 352 ⟵ “BUS 352 - Financial Modeling & Valuation”
  - courses: BUS 361 ⟵ “BUS 361 - Business Law”
  - courses: BUS 440 ⟵ “BUS 440 - Capital Markets”
  - courses: BUS 470 ⟵ “BUS 470 - Finance Seminar”
  - courses: COS 111 ⟵ “COS 111 - Introduction to Programming”
  - courses: COS 211 ⟵ “COS 211 - Data Structures”
  - courses: COS 277 ⟵ “COS 277 - Software Development Fundamentals”
  - courses: COS 313 ⟵ “COS 313 - Database Systems”
  - courses: ECO 202 ⟵ “ECO 202 - Principles of Microeconomics”
  - courses: ECO 203 ⟵ “ECO 203 - Principles of Macroeconomics”
  - courses: MAT 124M ⟵ “MAT 124M - Calculus 1”
  - courses: MAT 125 ⟵ “MAT 125 - Calculus 2”
  - courses: MAT 211 ⟵ “MAT 211 - Linear Algebra”
  - courses: MAT 223 ⟵ “MAT 223 - Multivariable Calculus”
  - courses: MAT 242 ⟵ “MAT 242 - Introduction to Proofs”
  - courses: MAT 309 ⟵ “MAT 309 - Financial Mathematics”
  - courses: MAT 332 ⟵ “MAT 332 - Probability and Statistics”
  - courses: MAT 333 ⟵ “MAT 333 - Advanced Probability and Statistics”
  - courses: MAT 376 ⟵ “MAT 376 - Operations Research”
  - courses: BUS 416 ⟵ “BUS 416 - Machine Learning and Artificial Intelligence for Business”
  - … 1 more rows
### `ed15c78f91dc7692` Carleton College — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.carleton.edu/financial-aid/our-approach/ (sha256 6e3937875fc9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have special circumstances (like a recent job loss or high medical bills) that the forms don’t cover, your family can ask for an additional review.”
### `9195220cf988df3c` Carleton College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.carleton.edu/financial-aid/cost/ (sha256 9cec541fa64a)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 9}
  - column:Tuition: 75186 ⟵ “Tuition | $75,186”
  - column:Student Activity Fee*: 480 ⟵ “Student Activity Fee* | $480”
  - column:Housing: 10194 ⟵ “Housing | $10,194”
  - column:Food: 9120 ⟵ “Food | $9,120”
  - column:Comprehensive Fee: 94980 ⟵ “Comprehensive Fee | $94,980”
  - column:Estimated books and personal costs**: 2040 ⟵ “Estimated books and personal costs** | $2,040”
  - column:Travel (average): 850 ⟵ “Travel (average) | $850”
  - column:Total Cost of Attendance: 97870 ⟵ “Total Cost of Attendance | $97,870”
  - column:Health Insurance***: 2355 ⟵ “Health Insurance*** | $2,355”
### `b753e42d9a0ef546` Century College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.century.edu/cost-financial-aid/financial-aid/apply-financial-aid/ (sha256 6eaa7747c8e4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Other Information For financial aid information about summer semester, taking course(s) at another college/university, and other special circumstances, check out the information below.”
  - sentence: need_based_special_circumstances ⟵ “Change of Income - Special Circumstances Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an aid administrator adjusting data elements in the COA or in the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “You may be eligible to apply for a Change of Income – Special Circumstance Review.”
  - sentence: need_based_special_circumstances ⟵ “Death, separation, divorce, unemployment, loss of employment, unusual medical/dental care expenses, or loss of non-taxable income or benefits are all examples of unusual circumstances that may affect your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Dependency Status - Unusual Circumstance Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abuse or abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “The student must then contact the Financial Aid Office to complete the appropriate steps for requesting a review of their Request for Review of Dependency Status – Unusual Circumstances.”
### `df9a3717942ca04f` Century College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.century.edu/cost-financial-aid/tuition-rates-fees/cost-attendance/ (sha256 946a3361038a)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees*: 6916 ⟵ “Tuition and Fees* | $3,458 | $3,458 | $6,916”
  - column:Books, Course Materials,Supplies and Equipment: 800 ⟵ “Books, Course Materials,Supplies and Equipment | $400 | $400 | $800”
  - column:Total Direct Costs: 7716 ⟵ “Total Direct Costs | $3,858 | $3,498 | $7,716”
### `b223c10649c89b2f` College of Saint Benedict — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.csbsju.edu/financialaid/wp-content/uploads/sites/76/2025/09/26-27-Special-Circumstances-Form-Fillable.pdf (sha256 a94da76e48ea)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/,https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances Application STUDENT INFORMATION Last Name: First Name: M.I.”
  - sentence: need_based_special_circumstances ⟵ “Check ☐ SPECIAL CIRCUMSTANCE REQUIRED DOCUMENTATION Reason Private Elementary/Secondary School  Tuition statement OR letter from the school indicating tuition charges Tuition minus financial aid and/or discounts for child(ren) at that school.”
  - sentence: need_based_special_circumstances ⟵ “Consumer debt is not eligible for consideration under special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Check SPECIAL CIRCUMSTANCE REQUIRED DOCUMENTATION Reason Loss of Employment/Reduced Wages • Statement explaining the reason for loss of income, including dates of change • Signed copy of 2024 federal tax return Financial aid eligibility for 2026-27 is based • Complete Estimated Income Chart (below).”
### `beca8ae9d8432d1a` College of Saint Benedict — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/ (sha256 07a621e50f82)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/,https://www.csbsju.edu/financialaid/wp-content/uploads/sites/76/2025/09/26-27-Special-Circumstances-Form-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances We recognize that the FAFSA does not always provide a clear picture of your family’s financial situation.”
  - sentence: need_based_special_circumstances ⟵ “You may complete the CSB+SJU Special Circumstances Form to report family financial information that might impact your aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Circumstances that may be considered include the following: Private Elementary/Secondary School Tuition Loss of Employment/Reduced Wages High Medical/Dental Expenses Marital Separation/Divorce One-Time Income Educational Loan Payments Please note that initiating a special circumstance request may result in your FAFSA being selected for verification.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances forms will be reviewed within 10 working days of receipt.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances Form Secure Upload Verification Information The verification process aims to ensure the effectiveness of the federal student aid programs.”
### `e6df0b9cf2fc8c8d` College of Saint Benedict — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/ (sha256 dcafcefdf959)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/,https://www.csbsju.edu/financialaid/wp-content/uploads/sites/76/2025/09/26-27-Special-Circumstances-Form-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances We recognize that the FAFSA does not always provide a clear picture of your family’s financial situation.”
  - sentence: need_based_special_circumstances ⟵ “You may complete the CSB+SJU Special Circumstances Form to report family financial information that might impact your aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Circumstances that may be considered include the following: Private Elementary/Secondary School Tuition Loss of Employment/Reduced Wages High Medical/Dental Expenses Marital Separation/Divorce One-Time Income Educational Loan Payments Please note that initiating a special circumstance request may result in your FAFSA being selected for verification.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances forms will be reviewed within 10 working days of receipt.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances Form Secure Upload Verification Information The verification process aims to ensure the effectiveness of the federal student aid programs.”
### `2a96c3ce105b3f01` College of Saint Benedict — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/student-accounts/educational-costs-3/ (sha256 c6971da6c88c)
- issues: shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/financialaid/costs/
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 58430 ⟵ “Tuition | $29,215 | $58,430”
  - column:Fees: 1352 ⟵ “Fees | $676 | $1,352”
  - column:Meals: 6820 ⟵ “Meals | $3,410 | $6,820”
  - column:Books: 1000 ⟵ “Books | $500 | $1,000”
### `8c17512682c21cb9` College of Saint Benedict — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/financialaid/costs/ (sha256 b2aa9ce14a39)
- issues: shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/student-accounts/educational-costs-3/
- checks: {"columns": 1, "rows": 3}
  - column:Full-Time Tuition and Required Fees: 59782 ⟵ “Full-Time Tuition and Required Fees | $59,782”
  - column:On Campus Housing & Food (First Year): 13350 ⟵ “On Campus Housing & Food (First Year) | $13,350”
  - column:On Campus Housing & Food (Returning}: 14340 ⟵ “On Campus Housing & Food (Returning} | $14,340”
### `92efd113c2459967` College of Saint Benedict — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/student-accounts/educational-costs-3/ (sha256 c6971da6c88c)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 56450 ⟵ “Tuition | $28,225 | $56,450”
  - column:Fees: 1248 ⟵ “Fees | $624 | $1,248”
  - column:Meals: 6620 ⟵ “Meals | $3,310 | $6,620”
  - column:Books: 1000 ⟵ “Books | $500 | $1,000”
### `eb23c1e601a3c48f` College of Saint Benedict — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/ (sha256 67209389323f)
- issues: arrangement_unlabeled, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/financialaid/costs/,https://www.csbsju.edu/student-accounts/educational-costs-3/
- checks: {"columns": 2, "rows": 4}
  - column:Tuition and fees:: 59782 ⟵ “Tuition and fees: | $59,782 | $59,782”
  - column:Housing and food:: 13350 ⟵ “Housing and food: | $13,350 | $13,350”
  - column:Estimated book costs for the year:: 1000 ⟵ “Estimated book costs for the year: | $1,000 | $1,000”
  - column:Personal/miscellaneous expenses: 1500 ⟵ “Personal/miscellaneous expenses | $1,500 | $1,500”
  - column:Tuition and fees:: 59782 ⟵ “Tuition and fees: | $59,782 | $59,782”
  - column:Housing and food:: 13350 ⟵ “Housing and food: | $13,350 | $13,350”
  - column:Estimated book costs for the year:: 1000 ⟵ “Estimated book costs for the year: | $1,000 | $1,000”
  - column:Personal/miscellaneous expenses: 1500 ⟵ “Personal/miscellaneous expenses | $1,500 | $1,500”
### `edb7c11b1186f871` College of Saint Benedict — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/ (sha256 807b272dc79f)
- issues: arrangement_unlabeled, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/financialaid/costs/,https://www.csbsju.edu/student-accounts/educational-costs-3/
- checks: {"columns": 2, "rows": 4}
  - column:Tuition and fees:: 59782 ⟵ “Tuition and fees: | $59,782 | $59,782”
  - column:Housing and food:: 13350 ⟵ “Housing and food: | $13,350 | $13,350”
  - column:Estimated book costs for the year:: 1000 ⟵ “Estimated book costs for the year: | $1,000 | $1,000”
  - column:Personal/miscellaneous expenses: 1500 ⟵ “Personal/miscellaneous expenses | $1,500 | $1,500”
  - column:Tuition and fees:: 59782 ⟵ “Tuition and fees: | $59,782 | $59,782”
  - column:Housing and food:: 13350 ⟵ “Housing and food: | $13,350 | $13,350”
  - column:Estimated book costs for the year:: 1000 ⟵ “Estimated book costs for the year: | $1,000 | $1,000”
  - column:Personal/miscellaneous expenses: 1500 ⟵ “Personal/miscellaneous expenses | $1,500 | $1,500”
### `17303053265d9d19` College of Saint Benedict — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf (sha256 7cd8d78a1578)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf
- checks: {"distinct_exams": 11, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|60]:  ⟵ “Financial Accounting                                       60    ACFN 111                                     4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|60]:  ⟵ “Introductory Business Law                                  60    ACFN 335                                     2              SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|60]:  ⟵ “Principles of Management                                   60    GBUS 202                                     4”
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4              HE”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOAN 111                                     4             SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4            SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4            SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8            SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123                                     4           NW ,QR”
### `21b87f144ef67b8d` College of Saint Benedict — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf (sha256 ec34eb51a7d1)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf
- checks: {"distinct_exams": 8, "equivalencies": 9, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOCI 111                                     4            SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8           SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123 (NS)                                4             NW”
### `288b73b965cecbce` College of Saint Benedict — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf (sha256 0d5b98f88b92)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf
- checks: {"distinct_exams": 30, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 100                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang & Composition (f)        4-5    ENGL 211                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 101                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142                                                          4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152                                                          4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100                                                          4              HE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography (s)                   4-5 COLG 105ZA (Elective credit only)                                 4”
  - … 6 more rows
### `2cf8094f7475e0ef` College of Saint Benedict — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf (sha256 0b27fbdaee02)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf
- checks: {"distinct_exams": 30, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 100                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Lang & Composition (f)         5     ENGL 211                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 101                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142                                                          4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152                                                          4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100                                                          4              HE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography (s)                   4-5 COLG 105ZA (Elective credit only)                                 4”
  - … 6 more rows
### `5fc404fa78395a56` College of Saint Benedict — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf (sha256 c2c586dc1d1c)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf
- checks: {"distinct_exams": 11, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|60]:  ⟵ “Financial Accounting                                       60    ACFN 111                                     4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|60]:  ⟵ “Introductory Business Law                                  60    ACFN 335                                     2             SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|60]:  ⟵ “Principles of Management                                   60    GBUS 202                                     4”
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOCI 111                                     4            SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8           SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123                                     4             NW”
### `780057783fc5e86b` College of Saint Benedict — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf (sha256 5b5cbfd01846)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf
- checks: {"distinct_exams": 30, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 101                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Lang & Composition (f)         5     ENGL 211                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 122                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142                                                          4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152                                                          4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100                                                          4              HE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography (s)                   4-5 COLG 105ZA (Elective credit only)                                 4”
  - … 6 more rows
### `b56e8fbd23dade53` College of Saint Benedict — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf (sha256 c259de2a1fb7)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf
- checks: {"distinct_exams": 30, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 101                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Lang & Composition (f)         5     ENGL 211                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 122                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142Z                                                         4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152Z                                                         4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100Z                                                         4              HE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography (s)                   4-5 COLG 105ZA (Elective credit only)                                 4”
  - … 6 more rows
### `cd1081c35b9fb8e8` College of Saint Benedict — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf (sha256 b77fadd5b31c)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf
- checks: {"distinct_exams": 8, "equivalencies": 9, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOCI 111                                     4            SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8           SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123 (NS)                                4             NW”
### `f17a066c884e8fc5` College of Saint Benedict — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf (sha256 eb32d45291f7)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf
- checks: {"distinct_exams": 11, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|60]:  ⟵ “Financial Accounting                                       60    ACFN 111                                     4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|60]:  ⟵ “Introductory Business Law                                  60    ACFN 335                                     2              SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|60]:  ⟵ “Principles of Management                                   60    GBUS 202                                     4”
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4              HE”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOAN 111                                     4             SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4            SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4            SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8            SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123                                     4           NW ,QR”
### `f8ebddfbaf3ee9a8` College of Saint Benedict — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf (sha256 0b5232ea2bbb)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf
- checks: {"distinct_exams": 31, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 100                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-CYBERSECURITY|4-5]:  ⟵ “Computer Science Cybersecurity        4-5    CSCI 300AZ Cybersecurity                                       2”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang & Composition (f)        4-5    ENGL 105                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 101                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142                                                          4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152                                                          4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100                                                          4              HE”
  - … 7 more rows
### `812c2cd48454efc7` Concordia College at Moorhead — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.concordiacollege.edu/tuition-aid/concordia-scholarships/community-achievement-scholarship/ (sha256 26c4cf1440be)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Finally, explain how your college education will equip you to bring about the transformation you desire." 500-word short answer essay answering this prompt: "Please describe any personal hardships, unusual circumstances you have had to overcome, or other aspects of your life story that you think we should consider in reviewing your application.”
### `c61e8bbb46175b2f` Concordia College at Moorhead — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/tuition-aid/scholarships/ (sha256 ed5e09eb2b2c)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - test_requirement: ACT Score: 28-29 ⟵ “28-29 | $17,500 | 3.7-3.84”
  - gpa_requirement: High School GPA: 3.7-3.84 ⟵ “28-29 | $17,500 | 3.7-3.84”
  - award_amount_text: $17,500 ⟵ “28-29 | $17,500 | 3.7-3.84”
### `dbfd89b225f81654` Concordia College at Moorhead — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/tuition-aid/scholarships/ (sha256 ed5e09eb2b2c)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - test_requirement: ACT Score: <=21 ⟵ “<=21 | $13,500 | <=3.00”
  - gpa_requirement: High School GPA: <=3.00 ⟵ “<=21 | $13,500 | <=3.00”
  - award_amount_text: $13,500 ⟵ “<=21 | $13,500 | <=3.00”
### `edb7950a2706cdc1` Concordia College at Moorhead — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concordiacollege.edu/tuition-aid/scholarships/ (sha256 ed5e09eb2b2c)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - test_requirement: ACT Score: >=33 ⟵ “>=33 | $19,500 | >=3.97”
  - gpa_requirement: High School GPA: >=3.97 ⟵ “>=33 | $19,500 | >=3.97”
  - award_amount_text: $19,500 ⟵ “>=33 | $19,500 | >=3.97”
### `05f7c3726ee10706` Concordia University-Saint Paul — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csp.edu/tuition-and-financial-aid/ (sha256 6a56f06b4489)
- issues: conflicting_sources:https://catalog.csp.edu/university-information/tuition-fees/
- checks: {"columns": 1, "rows": 6}
  - column:Tuition & Fees *: 7677.0 ⟵ “Tuition & Fees * | $7,677.00”
  - column:Housing & Food: 5886.0 ⟵ “Housing & Food | $5,886.00”
  - column:Books, Supplies, & Equipment: 1000.0 ⟵ “Books, Supplies, & Equipment | $1,000.00”
  - column:Transportation: 585.0 ⟵ “Transportation | $585.00”
  - column:Personal Expenses: 576.0 ⟵ “Personal Expenses | $576.00”
  - column:Program & Course Fees: 2294.0 ⟵ “Program & Course Fees | $2,294.00”
### `95e926133e666885` Concordia University-Saint Paul — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.csp.edu/university-information/tuition-fees/ (sha256 58a59f798126)
- issues: arrangement_unlabeled, conflicting_sources:https://www.csp.edu/tuition-and-financial-aid/
- checks: {"columns": 2, "rows": 3}
  - column:Tuition: 13600 ⟵ “Tuition | $13,600 | $27,200”
  - column:Residence Hall / Food Services: 6500 ⟵ “Residence Hall / Food Services | $6,500 | $13,000”
  - column:Totals: 20100 ⟵ “Totals | $20,100 | $40,200”
  - column:Tuition: 27200 ⟵ “Tuition | $13,600 | $27,200”
  - column:Residence Hall / Food Services: 13000 ⟵ “Residence Hall / Food Services | $6,500 | $13,000”
  - column:Totals: 40200 ⟵ “Totals | $20,100 | $40,200”
### `344a6715c994d910` Crown College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.crown.edu/admissions/transfer/ (sha256 f15eb4a1f5ac)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `54f94d223f13a425` Dakota County Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.dctc.edu/admissions/pay-for-college/financial-aid/forms-links/unusual-circumstances-dependency-override-appeal/ (sha256 5345639abb12)
- issues: semantic_review_required, conflicting_sources:https://www.dctc.edu/admissions/pay-for-college/financial-aid/forms-links/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Please note by federal law the following situations in and of themselves would not be considered an unusual circumstance for a dependency status appeal: Parents unwillingness to complete the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances may exist if you: Left home due to an abusive or threatening environment.”
  - sentence: need_based_special_circumstances ⟵ “Instructions: Complete this form and provide ALL of the documentation requested on the back of this form to support your unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Third Party Statement: Submit a signed letter from an objective third-party individual who has personal knowledge of your unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Personal Supporting Letter: Submit a letter from someone who can verify their knowledge of the unusual circumstances.”
### `c6b965320ad8b8e3` Dakota County Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.dctc.edu/admissions/pay-for-college/financial-aid/forms-links/ (sha256 b85e5c450399)
- issues: semantic_review_required, conflicting_sources:https://www.dctc.edu/admissions/pay-for-college/financial-aid/forms-links/unusual-circumstances-dependency-override-appeal/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Bill Program Application Form Parent Refusal Form Postsecondary Child Care Grant Program Third Party Payment Form Unusual Circumstances/Dependency Status Override Work Study Application Financial Aid Links Release of Information to 3rd Parties My Federal Loan Data FAFSA on the Web Federal Student Aid ID College Board: Paying for College Contact Information Students with questions regarding financi”
### `374f956f4dddea83` Dakota County Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.dctc.edu/admissions/pay-for-college/tuition-fees/ (sha256 7acdf7b1535f)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "rows": 12}
  - column:Tuition for Classroom Instruction: 212.01 ⟵ “Tuition for Classroom Instruction | $212.01 | $32.65 | $244.66”
  - column:Tuition for Online Courses: 221.1 ⟵ “Tuition for Online Courses | $221.10 | $32.65 | $253.75”
  - column:Tuition for Hybrid Courses: 221.1 ⟵ “Tuition for Hybrid Courses | $221.10 | $32.65 | $253.75”
  - column:Dental Assistant: 234.03 ⟵ “Dental Assistant | $234.03 | $32.65 | $266.68”
  - column:Electrical Construction & Maintenance: 219.96 ⟵ “Electrical Construction & Maintenance | $219.96 | $32.65 | $252.61”
  - column:Electrical Lineworker: 216.21 ⟵ “Electrical Lineworker | $216.21 | $32.65 | $248.86”
  - column:Heavy Construction Equipment Technology: 217.7 ⟵ “Heavy Construction Equipment Technology | $217.70 | $32.65 | $250.35”
  - column:Heavy Duty Truck Technology: 217.7 ⟵ “Heavy Duty Truck Technology | $217.70 | $32.65 | $250.35”
  - column:Medical Assistant: 230.74 ⟵ “Medical Assistant | $230.74 | $32.65 | $263.39”
  - column:Practical Nursing: 272.25 ⟵ “Practical Nursing | $272.25 | $32.65 | $304.90”
  - column:Veterinary Technician: 417.77 ⟵ “Veterinary Technician | $417.77 | $32.65 | $450.42”
  - column:Welding Technology: 223.37 ⟵ “Welding Technology | $223.37 | $32.65 | $256.02”
  - column:Tuition for Classroom Instruction: 32.65 ⟵ “Tuition for Classroom Instruction | $212.01 | $32.65 | $244.66”
  - column:Tuition for Online Courses: 32.65 ⟵ “Tuition for Online Courses | $221.10 | $32.65 | $253.75”
  - column:Tuition for Hybrid Courses: 32.65 ⟵ “Tuition for Hybrid Courses | $221.10 | $32.65 | $253.75”
  - column:Dental Assistant: 32.65 ⟵ “Dental Assistant | $234.03 | $32.65 | $266.68”
  - column:Electrical Construction & Maintenance: 32.65 ⟵ “Electrical Construction & Maintenance | $219.96 | $32.65 | $252.61”
  - column:Electrical Lineworker: 32.65 ⟵ “Electrical Lineworker | $216.21 | $32.65 | $248.86”
  - column:Heavy Construction Equipment Technology: 32.65 ⟵ “Heavy Construction Equipment Technology | $217.70 | $32.65 | $250.35”
  - column:Heavy Duty Truck Technology: 32.65 ⟵ “Heavy Duty Truck Technology | $217.70 | $32.65 | $250.35”
  - column:Medical Assistant: 32.65 ⟵ “Medical Assistant | $230.74 | $32.65 | $263.39”
  - column:Practical Nursing: 32.65 ⟵ “Practical Nursing | $272.25 | $32.65 | $304.90”
  - column:Veterinary Technician: 32.65 ⟵ “Veterinary Technician | $417.77 | $32.65 | $450.42”
  - column:Welding Technology: 32.65 ⟵ “Welding Technology | $223.37 | $32.65 | $256.02”
  - column:Tuition for Classroom Instruction: 244.66 ⟵ “Tuition for Classroom Instruction | $212.01 | $32.65 | $244.66”
  - … 11 more rows
### `72eee8fd38a17dd0` Dakota County Technical College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.dctc.edu/admissions/transfer-to-dctc/ib-equivalency-chart/ (sha256 0ffd455abf21)
- issues: score_column_not_scores
- checks: {"distinct_exams": 24, "equivalencies": 62, "rows_without_score": 0}
  - equivalencies[IB-ENGLISH-A-LITERATURE|Standard]:  ⟵ “English A: Literature | Standard | 4 | Goal 6 | 2 Credits”
  - equivalencies[IB-ENGLISH-A-LITERATURE|Higher]:  ⟵ “English A: Literature | Higher | 4 | ENGL 1550 | 3 cr / 6 cr”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|Standard]:  ⟵ “English A: Language & Literature | Standard | 4 | Goal 6 | 2 Credits”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|Higher]:  ⟵ “English A: Language & Literature | Higher | 4 | ENGL 1550 | 3 cr / 6 cr”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|Higher]:  ⟵ “English A: Language & Literature | Higher | 4 | Goal 1 Goal 6 | 3 cr / 6 cr”
  - equivalencies[IB-FRENCH|Standard]:  ⟵ “French A: Literature | Standard | 4 | Goal 6 Goal 8 | 2 Credits”
  - equivalencies[IB-FRENCH|Higher]:  ⟵ “French A: Literature | Higher | 4 | Goal 6 Goal 8 | 3 cr / 6 cr”
  - equivalencies[IB-FRENCH|Standard]:  ⟵ “French B | Standard | 4 | Goal 8 | 2 Credits”
  - equivalencies[IB-FRENCH|Higher]:  ⟵ “French B | Higher | 4 | Goal 8 | 3 cr / 6 cr”
  - equivalencies[IB-GERMAN|Standard]:  ⟵ “German A: Literature | Standard | 4 | Goal 6 Goal 8 | 2 Credits”
  - equivalencies[IB-GERMAN|Higher]:  ⟵ “German A: Literature | Higher | 4 | Goal 6 Goal 8 | 3 cr / 6 cr”
  - equivalencies[IB-GERMAN|Standard]:  ⟵ “German B | Standard | 4 | Goal 8 | 2 Credits”
  - equivalencies[IB-GERMAN|Higher]:  ⟵ “German B | Higher | 4 | Goal 8 | 3 cr / 6 cr”
  - equivalencies[IB-SPANISH|Standard]:  ⟵ “Spanish A: Literature | Standard | 4 | Goal 6 Goal 8 | 2 Credits”
  - equivalencies[IB-SPANISH|Higher]:  ⟵ “Spanish A: Literature | Higher | 4 | Goal 6 Goal 8 | 3 cr / 6 cr”
  - equivalencies[IB-SPANISH|Standard]:  ⟵ “Spanish B | Standard | 4 | Goal 8 | 2 Credits”
  - equivalencies[IB-SPANISH|Higher]:  ⟵ “Spanish B | Higher | 4 | Goal 8 | 3 cr / 6 cr”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Standard]:  ⟵ “Business Management | Standard | 4 | Business Elective | 2 Credits”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Higher]:  ⟵ “Business Management | Higher | 4 | BUSN 1000 Business Elective | 3 cr / 6 cr”
  - equivalencies[IB-ECONOMICS|Standard]:  ⟵ “Economics | Standard | 4 | Goal 5 | 2 Credits”
  - equivalencies[IB-ECONOMICS|Higher (w/o Diploma)]:  ⟵ “Economics | Higher (w/o Diploma) | 5 | Goal 5 | 3 Credits”
  - equivalencies[IB-ECONOMICS|Higher (w/Diploma)]:  ⟵ “Economics | Higher (w/Diploma) | 4 | ECON 1100 ECON 1200 | 6 Credits”
  - equivalencies[IB-GEOGRAPHY|Standard]:  ⟵ “Geography | Standard | 4 | Goal 5 | 2 Credits”
  - equivalencies[IB-GEOGRAPHY|Higher]:  ⟵ “Geography | Higher | 4 | Goal 5 | 3 cr / 6 cr”
  - equivalencies[IB-GLOBAL-POLITICS|Standard]:  ⟵ “Global Politics | Standard | 4 | Goal 5 Goal 8 | 2 Credits”
  - … 37 more rows
### `488a37a3e2189a46` Dakota County Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.dctc.edu/admissions/transfer-to-dctc/ (sha256 8caf9a4ac3aa)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `6f4f2ed9e3510584` Dunwoody College of Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.dunwoody.edu/catalog-student-handbook/academic-policies/grading-system-sap/grading-system-sap.pdf (sha256 d2f22127465c)
- issues: semantic_review_required, conflicting_sources:https://catalog.dunwoody.edu/catalog-student-handbook/academic-policies/grading-system-sap/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Financial Aid Under Warning Status • A student placed on Academic Warning will have one semester of Appeal Determination ﬁnancial aid to bring their status into compliance with the deﬁnition The Dean of Student Affairs/Academic Dean will make a determination of satisfactory academic progress, both GPA and Pace. on accepting or denying the appeal within ten days.”
  - sentence: sap_appeal ⟵ “The ﬁrst semester of the plan is the probationary term. to their ﬁnancial aid suspension once all ﬁnal grades have been The student’s performance at the end of the semester will be evaluated to submitted for the previous semester. determine the student’s progress. • Included in this notiﬁcation will be the information on the student’s • If the student has met the Satisfactory Academic Progress sta”
  - sentence: sap_appeal ⟵ “Academic Probation Appeal form, which includes the Academic Success Plan. • If the student has not met the Satisfactory Academic Progress standards, but has met the standards established in their Academic Student Appeal Process Plan the Academic Probation status will continue and be evaluated at A student who does not attain the satisfactory academic standard has the end of the next semester. the ”
  - sentence: sap_appeal ⟵ “In order to execute the appeal, the • If the student has not met the Satisfactory Academic Progress student needs to complete the following elements.”
  - sentence: sap_appeal ⟵ “With the academic program staff, the student will develop an Academic Success Plan including courses to be taken and resources Grading System and Satisfactory Academic Progress 5 that there is no guarantee that the student who undertakes an appeal will be reinstated into Dunwoody or to receiving ﬁnancial aid.”
### `7cb4a8227f11bc98` Dunwoody College of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.dunwoody.edu/catalog-student-handbook/academic-policies/grading-system-sap/ (sha256 7eb0948bb1fa)
- issues: semantic_review_required, conflicting_sources:https://catalog.dunwoody.edu/catalog-student-handbook/academic-policies/grading-system-sap/grading-system-sap.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “A student will have until the Friday of Week 2 of the current semester to complete a SAP appeal.”
  - sentence: sap_appeal ⟵ “Academic Probation A student, who has successfully appealed their Satisfactory Academic Progress financial aid suspension, will move forward and execute the Academic Plan.”
### `b5c3934acf3f04c3` Dunwoody College of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://dunwoody.edu/admission-aid/tuition-aid/apply-financial-aid/ (sha256 db8e235ad5e3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “When there are unusual situations or circumstances that impact your federal student aid eligibility, federal regulations give a financial aid administrator discretion or professional judgment on a case-by-case basis and with adequate documentation to make adjustments to the data elements on the Free Application for Federal Student Aid (FAFSA®) form that impact your Student Aid Index (SAI) to gain ”
### `d07c3e82680c8323` Dunwoody College of Technology — appeals 2026-27 [new] (labeled_in_source)
- source: https://dunwoody.edu/admission-aid/tuition-aid/apply-financial-aid/ (sha256 523ad433dedc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an aid administrator adjusting data elements in the COA or in the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “For information on how to request additional loan amounts or other financial aid—or If you feel as if you qualify for either a Special Circumstance or Unusual Circumstance review—please email financialaid@dunwoody.com for more information.”
### `7a20f1cbcfaae90c` Dunwoody College of Technology — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://dunwoody.edu/admission-aid/tuition-aid/ (sha256 7e7b861dcdef)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 9}
  - column:Tuition Average: 27704 ⟵ “Tuition Average |  | $27,704”
  - column:Average Books & Supplies: 744 ⟵ “Average Books & Supplies |  | $744”
  - column:Average Fees: 710 ⟵ “Average Fees |  | $710”
  - column:Food: 3898 ⟵ “Food |  | $3,898”
  - column:Housing, on campus: 11766 ⟵ “Housing, on campus |  | $11,766”
  - column:Housing, off campus: 12106 ⟵ “Housing, off campus |  | $12,106”
  - column:Transportation: 2000 ⟵ “Transportation |  | $2,000”
  - column:Miscellaneous: 2200 ⟵ “Miscellaneous |  | $2,200”
  - column:Direct Plus Loan Fees: 402 ⟵ “Direct Plus Loan Fees |  | $402”
### `af75015fea919bbd` Dunwoody College of Technology — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://dunwoody.edu/pdfs/DCT-Registrar-CLEP-Transfers-May2025.pdf (sha256 9f608cb7e07f)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 11, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus                                            4              CALCULUS I (MATH1810/MATH1811)”
  - equivalencies[CLEP-CHEMISTRY|3]:  ⟵ “Chemistry                                           3              INTRO TO CHEMISTRY (WITHOUT LAB) (CHEM2000)”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra                                     3              ALGEBRA I (MATH1010)”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra-Trigonometry                        3              ALGEBRA I (MATH1010) or”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|6]:  ⟵ “College Composition                                 6              TECHNICAL WRITING (WRIT2010) (3cr) and”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|3]:  ⟵ “Financial Accounting                                3              PRINCIPLES OF ACCOUNTING (MGMT1000)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Introductory Psychology                             3              PSYCHOLOGY OF HUMAN BEHAVIOR (SSCI1000)”
  - equivalencies[CLEP-PRECALCULUS|3]:  ⟵ “Precalculus                                         3              PRECALCULUS (MATH1700)”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Principles of Management                            3              PRINCIPLES OF MANAGEMENT (MGMT3112)”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|3]:  ⟵ “Principles of Marketing                             3              PRINCIPLES OF MARKETING (MGMT1100)”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Principles of Macroeconomics                        3              INTRO TO MACRO & MICRO ECONOMICS (SSCI1100)”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3]:  ⟵ “Principles of Microeconomics                        3              INTRO TO MACRO & MICRO ECONOMICS (SSCI1100)”
### `089a9f55db48efc1` Gustavus Adolphus College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gustavus.edu/admission-aid/financial-aid/policies-resources/policy-library (sha256 e7c364c334f8)
- issues: semantic_review_required, conflicting_sources:https://gustavus.edu/admission-aid/financial-aid/faq
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “A letter of special circumstance should be sent to Gustavus if your parents will be providing more than 50% of support to a sibling enrolled in medical or law school.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office provides a Special Circumstance/Appeal process, which allows us to review changes to a family’s financial situation based on new information.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance/Appeal Process Please complete the Special Circumstances/Appeal Form if any of the following circumstances apply to your situation: Excessive Medical Expenses—If your family had high amounts of medical or dental expenses that were not covered by insurance or a health savings account, we may be able to consider these payments.”
  - sentence: need_based_special_circumstances ⟵ “Acceptable reasons for an appeal include the following: Medical Family problems Death of a relative Other special, significant or unusual circumstances Documentation verifying the situation may be requested.”
  - sentence: need_based_special_circumstances ⟵ “Except under certain special circumstances, student loan debt cannot be eliminated or forgiven.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office provides a Special Circumstance/Appeal process, which allows us to review changes to a family’s financial situation based on new information.”
### `2da764f53e63b575` Gustavus Adolphus College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gustavus.edu/admission-aid/financial-aid/policies-resources/policy-library (sha256 e7c364c334f8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The Appeal Grant is awarded based upon a professional judgment decision that has been made by a financial aid professional based upon US government guidelines.”
### `6ad68cc07810abcb` Gustavus Adolphus College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gustavus.edu/admission-aid/financial-aid/policies-resources/policy-library (sha256 e7c364c334f8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Probation: This is the status assigned to a student who, in the previous semester, was on warning status and subsequently again failed to achieve satisfactory academic progress but whose appeal to have eligibility restored has been granted.”
  - sentence: sap_appeal ⟵ “Students may have their suspended aid restored under the following circumstances: A student may appeal their financial aid SAP suspension by performing the SAP appeal process.”
  - sentence: sap_appeal ⟵ “Financial Aid SAP Suspension Appeal Conditions A student must use one of the following methods to submit a request for reinstatement of financial aid: The electronic appeal submission form A signed and dated letter of appeal explaining why financial aid should be reinstated.”
  - sentence: sap_appeal ⟵ “Special Circumstances/Appeal Form Click here for the Electronic Appeal Form Click here for the PDF Appeal Form Satisfactory Academic Progress SAP Details and Impacts on Financial Aid Satisfactory Academic Progress (SAP) standards ensure that you are successfully completing your coursework and can continue to receive financial aid.”
  - sentence: sap_appeal ⟵ “Probation: This is the status assigned to a student who, in the previous semester, was on warning status and subsequently again failed to achieve satisfactory academic progress but whose appeal to have eligibility restored has been granted.”
  - sentence: sap_appeal ⟵ “Students may have their suspended aid restored under the following circumstances: A student may appeal their financial aid SAP suspension by performing the SAP appeal process.”
### `6e47bf6849b029fe` Gustavus Adolphus College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gustavus.edu/admission-aid/financial-aid/policies-resources/policy-library (sha256 e7c364c334f8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Dependency Override—Married Students/Students Getting Married Gustavus strongly recommends waiting to file the FAFSA until after getting married.”
  - sentence: dependency_override ⟵ “Dependency Override—Married Students/Students Getting Married Gustavus strongly recommends waiting to file the FAFSA until after getting married.”
### `aafbd3548218be9b` Gustavus Adolphus College — appeals 2026-27 [new] (source_unlabeled)
- source: https://apply.gustavus.edu/register/?id=0d6c9b28-2365-4374-9d68-ae999a02574d (sha256 76507de96e66)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Preview HD code Preview scholarship amount Preview scholarship name personstatus ApplicantInquiryProspect personguid Submit Reach far.”
### `bb586913e90b6aea` Gustavus Adolphus College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gustavus.edu/admission-aid/financial-aid/faq (sha256 ec5c71365867)
- issues: semantic_review_required, conflicting_sources:https://gustavus.edu/admission-aid/financial-aid/policies-resources/policy-library
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Except under certain special circumstances, student loan debt cannot be eliminated or forgiven.”
### `16afdf4de0f6ae8a` Gustavus Adolphus College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://gustavus.edu/admission/majors/credit.php (sha256 9c7b2e586baf)
- issues: rows_without_score
- checks: {"distinct_exams": 19, "equivalencies": 20, "rows_without_score": 20}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|None]:  ⟵ “Anthropology | S/A-111 | GLAFC”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business & Management | B/E-00 | ”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | MCS-177 | QUANT”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|None]:  ⟵ “English A: Lang & Lit | ENG-100 | HUMN”
  - equivalencies[IB-ENGLISH-A-LITERATURE|None]:  ⟵ “English A: Literature | ENG-100 | HUMN”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French Language | FRE-202 | Fulfills the Non-English Language requirement. GLAFC”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “General Biology | BIO-110/111 | NTSCI”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “General Chemistry | CHE-110/111 | NTSCI”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German Language | GER-202 | Fulfills the Non-English Language requirement. GLAFC”
  - equivalencies[IB-GLOBAL-POLITICS|None]:  ⟵ “Global Politics | POL-130 | HBSI”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History of Africa | HIS-00 | HUMN”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Intro Geography | GEG-101 | GLAFC”
  - equivalencies[IB-PHILOSOPHY|None]:  ⟵ “Intro Philosophy | PHI-108 | HUMN”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Intro Physics | PHY-00 | ”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Intro Psychology | PSY-100 | HBSI”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Macroeconomics | B/E-00 | A score of 4 or higher on both Macroeconomics and Microeconomics gives B/E-107. Meet with the Department Chair if only one IB course was completed and a course substitution is needed.”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Macroeconomics + Microeconomics | B/E-107 | HBSI”
  - equivalencies[IB-SPANISH|None]:  ⟵ “Spanish Language | SPA-00 | Fulfills the Non-English Language requirement”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Survey of Music | MUS-00 | ARTSC”
  - equivalencies[IB-THEATRE|None]:  ⟵ “Theatre Arts | T/D-00 | ARTSC”
### `d7afc62f191b8509` Gustavus Adolphus College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://gustavus.edu/admission/majors/credit.php (sha256 9c7b2e586baf)
- issues: rows_without_score
- checks: {"distinct_exams": 40, "equivalencies": 42, "rows_without_score": 42}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “African American Studies | AFS-00 | USIDG”
  - equivalencies[AP-2-D-ART-DESIGN|None]:  ⟵ “2-D Art and Design | ART-00 | ARTSC”
  - equivalencies[AP-3-D-ART-DESIGN|None]:  ⟵ “3-D Art and Design | ART-00 | ARTSC”
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “Art History | ART-101 | GLAFC”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | BIO-110 & 111 | NTSCI”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB | MCS-121 | QUANT”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Calculus BC | MCS-122 | QUANT”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | CHE-110 & 111 | NTSCI”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “Chinese Language and Culture | MLC-00 | Score of 4 or higher fulfills NELC”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|None]:  ⟵ “Comparative Government and Politics | POL-150 | HBSI”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “Computer Science A | MCS-177 | QUANT”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “Computer Science Principles | MCS-00 | ”
  - equivalencies[AP-DRAWING|None]:  ⟵ “Drawing | ART-110 | ARTSC”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language and Composition | ENG-110 | HUMN”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “English Literature and Composition | ENG-100 | HUMN”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “Environmental Science | ENV-00 | ”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “European History | HIS-120 | HUMN”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “French Language and Culture | FRE-202 | GLAFC. Score of 4 or higher fulfills NELC”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “German Language and Culture | GER-202 | GLAFC. Score of 4 or higher fulfills NELC”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Human Geography | GEG-101 | GLAFC”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “Italian Language and Culture | MLC-00 | Score of 4 or higher fulfills NELC”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “Japanese Language and Culture | JPN-202 | Score of 4 or higher fulfills NELC”
  - equivalencies[AP-LATIN|None]:  ⟵ “Latin | LAT-201 | GLAFC. Score of 4 or higher fulfills NELC”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Macroeconomics | B/E-00 | A score of 4 or higher on both AP-MACEC and AP-MICEC gives B/E-107. Meet with the Department Chair if only one AP course was completed and a course substitution is needed.”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Microeconomics | B/E-00 | A score of 4 or higher on both AP-MACEC and AP-MICEC gives B/E-107. Meet with the Department Chair if only one AP course was completed and a course substitution is needed.”
  - … 17 more rows
### `6c58a589578725ad` Inver Hills Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.inverhills.edu/cost-aid/financial-aid/ (sha256 142e4aef84df)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Learn More Financial aid forms Consortium Agreement Minnesota State Colleges & Universities Federal Direct Parent PLUS Loan Request Form Financial Aid Appeal-Satisfactory Academic Progress Financing Your Education Checklist Minnesota G.I.”
### `475766ceea5bae58` Lake Superior College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lsc.edu/policies-procedures/291__academic-standing--financial-aid-satisfactory-academic-progress/ (sha256 20066555defe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Extenuating Circumstance: Death in the family, student’s injury or illness or other special circumstances as determined by the institution.”
### `6036d4b4882a1bba` Lake Superior College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lsc.edu/current-students/course-info/grades/satisfactory-academic-progress-sap/ (sha256 991651809e71)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “In most cases, students will not regain Financial Aid eligibility until they have successfully completed at least 6 credits at their own expense and demonstrated satisfactory academic progress or have successfully appealed for Financial Aid eligibility through the Suspension Appeal process.”
### `56da942ee4170b8c` Leech Lake Tribal College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.lltc.edu/financial-aid/ (sha256 5e13313c635b)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.lltc.edu/wp-content/uploads/2024/08/20240803-FA-Dependency-override-appeal-form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Financial Aid Dependency Override Appeal Form Withdrawals When a student who is a Title IV recipient withdraws, there are two policies related to finance that the student should be familiar with.”
### `664dd14df08f7473` Leech Lake Tribal College — appeals 2024-25 [new] (labeled_in_title)
- source: https://www.lltc.edu/wp-content/uploads/2024/08/20240803-FA-Dependency-override-appeal-form.pdf (sha256 77cd5d9448d9)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.lltc.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “It is used after you have filed your FAFSA and included that you have special circumstances which prevent you from providing parental information.”
  - sentence: need_based_special_circumstances ⟵ “We understand the sensitive nature of these circumstances; therefore, all documentation received by our office will be kept confidential. 2024-2025 Student Dependency Override Request Form ________________________________________ ________________________________________ Student Name Email _______________________________________ ________________________________________ Student ID Telephone ________”
### `6a4e017f02914133` Leech Lake Tribal College — appeals 2024-25 [new] (labeled_in_title)
- source: https://www.lltc.edu/wp-content/uploads/2024/08/20240803-FA-Dependency-override-appeal-form.pdf (sha256 77cd5d9448d9)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.lltc.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: dependency_override ⟵ “2024-2025 Dependency Override Appeal Federal Financial aid regulations assume that a student’s family has primary responsibility for meeting educational costs.”
  - sentence: dependency_override ⟵ “This appeal is used to request dependency override for federal financial aid.”
  - sentence: dependency_override ⟵ “The Dependency Override process is used to address on a case-by-case basis a student who claims to be independent but does not meet the federal criteria.”
  - sentence: dependency_override ⟵ “The below lists provide information and explains the procedure used to determine a student's eligibility for a "Dependency Override." A Financial Aid Administrator will review the student's appeal by examining the supporting documentation provided by the student and will either approve or deny the student’s request and notify the student in writing.”
  - sentence: dependency_override ⟵ “Conditions for a dependency override for an adjustment to a student's dependency status based on a unique situation include: • Human Trafficking • Refugee or Asylee status • Parental abuse or abandonment • Incarceration Dependency Override Appeal Process: 1.”
  - sentence: dependency_override ⟵ “Complete the student dependency override request form. 3.”
### `945ccddf0062e60d` Leech Lake Tribal College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.lltc.edu/financial-aid/ (sha256 5e13313c635b)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.lltc.edu/wp-content/uploads/2024/08/20240803-FA-Dependency-override-appeal-form.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “The changes to the inputs are dictated by the impact of the special circumstances on the family’s income and assets.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an aid administrator adjusting data elements in the COA or in the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
### `b76b67b70d97e5b1` Leech Lake Tribal College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.lltc.edu/financial-aid/ (sha256 5e13313c635b)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgement Professional Judgment refers to the authority of a college’s financial aid office to make adjustments to the data elements on the FAFSA (special circumstances) and/or to adjust a student’s dependency status (unusual circumstances) on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “The FAFSA Simplification Act distinguishes between different categories of professional judgment by amending section 479A of the HEA.”
### `2638093ad653e910` Macalester College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.macalester.edu/admissions/financial-aid/ (sha256 193e399ac294)
- issues: conflicting_sources:https://www.macalester.edu/financial-aid/tuition/
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 74394 ⟵ “Tuition | $74,394”
  - column:Residence Hall: 9268 ⟵ “Residence Hall | $9,268”
  - column:Meal Plan: 8162 ⟵ “Meal Plan | $8,162”
  - column:Activity Fee: 230 ⟵ “Activity Fee | $230”
  - column:Comprehensive Fee (sum of above): 92154 ⟵ “Comprehensive Fee (sum of above) | $92,154”
### `85f64148b51468b7` Macalester College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.macalester.edu/financial-aid/tuition/ (sha256 4ea52d575372)
- issues: conflicting_sources:https://www.macalester.edu/admissions/financial-aid/
- checks: {"columns": 1, "rows": 5}
  - column:Tuition & Required Course Materials*:: 74394 ⟵ “Tuition & Required Course Materials*: | $74,394”
  - column:Residence Hall:: 9268 ⟵ “Residence Hall: | $9,268”
  - column:Meal Plan:: 8162 ⟵ “Meal Plan: | $8,162”
  - column:Activity Fee:: 330 ⟵ “Activity Fee: | $330”
  - column:Comprehensive Fee (sum of above):: 92154 ⟵ “Comprehensive Fee (sum of above): | $92,154”
### `205c791a774cb371` Martin Luther College — appeals 2026-27 [new] (labeled_in_title)
- source: https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2025/12/2026-2027-Tuition-Paid.pdf (sha256 058080375109)
- issues: semantic_review_required, conflicting_sources:https://mlc-wels.edu/financial-aid/eligibility/,https://mlc-wels.edu/financial-aid/special-circumstances/,https://mlc-wels.edu/financial-aid/special-circumstances/?s=,https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2026/02/2026-2027-Marital-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances: Tuition Paid in 2025 ________________________________ MLC Student’s Name Families that pay $1500 or more for tuition for an MLC sibling at a private elementary/high school or any higher education institution (public or private college/university) should submit this form.”
### `2562a99f6c92ea99` Martin Luther College — appeals 2026-27 [new] (labeled_in_url)
- source: https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2026/02/2026-2027-Marital-Appeal.pdf (sha256 872c3e546cc0)
- issues: semantic_review_required, conflicting_sources:https://mlc-wels.edu/financial-aid/eligibility/,https://mlc-wels.edu/financial-aid/special-circumstances/,https://mlc-wels.edu/financial-aid/special-circumstances/?s=,https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2025/12/2026-2027-Tuition-Paid.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “2026‐2027 Special Circumstance: Appeal for Change in Student Marital Status Students whose marital status changes (married or divorced) after submitting their FAFSA may submit this appeal.”
### `293ef5e91212f20e` Martin Luther College — appeals 2026-27 [new] (labeled_in_source)
- source: https://mlc-wels.edu/financial-aid/special-circumstances/ (sha256 81986ec79651)
- issues: semantic_review_required, conflicting_sources:https://mlc-wels.edu/financial-aid/eligibility/,https://mlc-wels.edu/financial-aid/special-circumstances/?s=,https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2025/12/2026-2027-Tuition-Paid.pdf,https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2026/02/2026-2027-Marital-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office provides a Special Circumstance Appeal process, which allows us to review changes to a family’s financial situation based on new information.”
  - sentence: need_based_special_circumstances ⟵ “If one of the situations below applies to you or your family, please complete the appropriate Special Circumstances Form.”
  - sentence: need_based_special_circumstances ⟵ “Expenses for tuition only (EXCLUDES fees, books, room, board, etc.) Does not include tuition for current MLC student Incomplete forms will not be processed Submissions must be made using the official form below Submissions of documents not using the form will not be considered 2026-2027 Academic Year Special Circumstances 2026-27: Tuition Paid Medical Expenses If your family had high amounts of me”
  - sentence: need_based_special_circumstances ⟵ “Expenses paid by family and not reimbursed by insurance or by employer’s pre-tax plan Documentation showing the amount paid (out of pocket) must be provided As a guideline – it takes at least $5000 in medical expenses paid (for a family of 4) to provide eligibility for additional financial aid Incomplete forms will not be processed Please submit the special circumstances form below 2026-2027 Acade”
  - sentence: need_based_special_circumstances ⟵ “Provide your phone number on the special circumstances form.”
  - sentence: need_based_special_circumstances ⟵ “Since every situation is different, the Director of Financial Aid will contact you in order to confirm what specific additional documentation is required. 2026-2027 Academic Year Special Circumstances 2026-27: Loss of Income Dependency Override – Married Students/Students Getting Married MLC strongly recommends waiting to file the FAFSA until after getting married.”
### `985393738e61a599` Martin Luther College — appeals 2026-27 [new] (labeled_in_source)
- source: https://mlc-wels.edu/financial-aid/special-circumstances/?s= (sha256 c354406582da)
- issues: semantic_review_required, conflicting_sources:https://mlc-wels.edu/financial-aid/eligibility/,https://mlc-wels.edu/financial-aid/special-circumstances/,https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2025/12/2026-2027-Tuition-Paid.pdf,https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2026/02/2026-2027-Marital-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office provides a Special Circumstance Appeal process, which allows us to review changes to a family’s financial situation based on new information.”
  - sentence: need_based_special_circumstances ⟵ “If one of the situations below applies to you or your family, please complete the appropriate Special Circumstances Form.”
  - sentence: need_based_special_circumstances ⟵ “Expenses for tuition only (EXCLUDES fees, books, room, board, etc.) Does not include tuition for current MLC student Incomplete forms will not be processed Submissions must be made using the official form below Submissions of documents not using the form will not be considered 2026-2027 Academic Year Special Circumstances 2026-27: Tuition Paid Medical Expenses If your family had high amounts of me”
  - sentence: need_based_special_circumstances ⟵ “Expenses paid by family and not reimbursed by insurance or by employer’s pre-tax plan Documentation showing the amount paid (out of pocket) must be provided As a guideline – it takes at least $5000 in medical expenses paid (for a family of 4) to provide eligibility for additional financial aid Incomplete forms will not be processed Please submit the special circumstances form below 2026-2027 Acade”
  - sentence: need_based_special_circumstances ⟵ “Provide your phone number on the special circumstances form.”
  - sentence: need_based_special_circumstances ⟵ “Since every situation is different, the Director of Financial Aid will contact you in order to confirm what specific additional documentation is required. 2026-2027 Academic Year Special Circumstances 2026-27: Loss of Income Dependency Override – Married Students/Students Getting Married MLC strongly recommends waiting to file the FAFSA until after getting married.”
### `9aca2630618d81a8` Martin Luther College — appeals 2026-27 [new] (labeled_in_source)
- source: https://mlc-wels.edu/financial-aid/scholarships/mlc-scholarships/?s= (sha256 2f08370edd0e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Return to Main Scholarship Page Review Merit Scholarship requirements and other available funding.”
### `b0ebd1b24eec77a1` Martin Luther College — appeals 2026-27 [new] (labeled_in_source)
- source: https://mlc-wels.edu/financial-aid/special-circumstances/?s= (sha256 c354406582da)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: dependency_override ⟵ “MLC will consider a dependency override for students that have entered in to marriage after filing the FAFSA.”
  - sentence: dependency_override ⟵ “Students that filed the FAFSA prior to becoming married should complete the dependency override request form, provided by the link button below, and submit it to the Financial Aid office.”
  - sentence: dependency_override ⟵ “For the 2026-2027 academic year 26-27 Dependency Override Request Form Dependency Override – Students Experiencing Hardships If a student is in an abusive family situation which creates extreme hardship preventing attendance to college, a dependency override may be considered.”
  - sentence: dependency_override ⟵ “PLEASE NOTE: Parental willingness to give information or financial help to student, whether or not the parents claim the student on their federal tax return, and whether or not the student lives with the parent DO NOT make a student eligible for a dependency override by themselves.”
  - sentence: dependency_override ⟵ “For the 2026-2027 academic year Dependency Override Policy Submit Documentation Securely to Our Office To securely supply requested documents to Martin Luther College, you may fax, mail, hand deliver, or use the secure electronic link available HERE (select the ‘Secure Upload’ option and follow the instructions).”
### `d2a6c6e4749590e3` Martin Luther College — appeals 2026-27 [new] (source_unlabeled)
- source: https://mlc-wels.edu/financial-aid/eligibility/ (sha256 746fe375556d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Probation: This is the status assigned to a student who, in the previous semester, was on warning status and subsequently again failed to achieve satisfactory academic progress but whose appeal to have eligibility restored has been granted.”
### `ed0abc29d9d2518f` Martin Luther College — appeals 2026-27 [new] (source_unlabeled)
- source: https://mlc-wels.edu/financial-aid/eligibility/ (sha256 746fe375556d)
- issues: semantic_review_required, conflicting_sources:https://mlc-wels.edu/financial-aid/special-circumstances/,https://mlc-wels.edu/financial-aid/special-circumstances/?s=,https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2025/12/2026-2027-Tuition-Paid.pdf,https://mlc-wels.edu/financial-aid/wp-content/uploads/sites/7/2026/02/2026-2027-Marital-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Additional Factors The following are considered when evaluating a student’s satisfactory academic progress: Withdrawn Classes: Under special circumstances, a student may drop a course with the approval of the dean after the first two weeks of the semester and up to two weeks after midterm.”
  - sentence: need_based_special_circumstances ⟵ “Acceptable reasons for an appeal include the following: Medical Family problems Death of a relative Other special, significant or unusual circumstances Documentation verifying the situation may be requested.”
### `72e7aec8cdd6dbdf` Martin Luther College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://mlc-wels.edu/financial-aid/cost-of-attendance/?s= (sha256 b35b36feb0d5)
- issues: conflicting_sources:https://mlc-wels.edu/academics/tuition-and-payments,https://mlc-wels.edu/financial-aid/cost-of-attendance/
- checks: {"columns": 3, "components_reconcile": true, "rows": 3}
  - on_campus:Tuition: 19220 ⟵ “Tuition | $19,220 | $19,220 | $19,220”
  - on_campus:Food and Housing: 9350 ⟵ “Food and Housing | $9,350 | $9,350 | $4,675”
  - on_campus:TOTAL Fixed Cost: 28570 ⟵ “TOTAL Fixed Cost | $28,570 | $28,570 | $23,895”
  - off_campus_not_with_family:Tuition: 19220 ⟵ “Tuition | $19,220 | $19,220 | $19,220”
  - off_campus_not_with_family:Food and Housing: 9350 ⟵ “Food and Housing | $9,350 | $9,350 | $4,675”
  - off_campus_not_with_family:TOTAL Fixed Cost: 28570 ⟵ “TOTAL Fixed Cost | $28,570 | $28,570 | $23,895”
  - with_parents_or_family:Tuition: 19220 ⟵ “Tuition | $19,220 | $19,220 | $19,220”
  - with_parents_or_family:Food and Housing: 4675 ⟵ “Food and Housing | $9,350 | $9,350 | $4,675”
  - with_parents_or_family:TOTAL Fixed Cost: 23895 ⟵ “TOTAL Fixed Cost | $28,570 | $28,570 | $23,895”
### `7e05fc3079847682` Martin Luther College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://mlc-wels.edu/academics/tuition-and-payments (sha256 a72496758086)
- issues: conflicting_sources:https://mlc-wels.edu/financial-aid/cost-of-attendance/,https://mlc-wels.edu/financial-aid/cost-of-attendance/?s=
- checks: {"columns": 1, "rows": 2}
  - column:Tuition (in-state or out-of-state): 19220 ⟵ “Tuition (in-state or out-of-state) | $9,610 | $19,220”
  - column:Housing and Food: 9350 ⟵ “Housing and Food | $4,675 | $9,350”
### `bb1ea67412496ca4` Martin Luther College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://mlc-wels.edu/academics/tuition-and-payments-2025-26 (sha256 e8351c8eb435)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Tuition (in-state or out-of-state): 18660 ⟵ “Tuition (in-state or out-of-state) | $9,330 | $18,660”
  - column:Housing and Food: 8720 ⟵ “Housing and Food | $4,360 | $8,720”
### `f4f529b3d9cdfa45` Martin Luther College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://mlc-wels.edu/financial-aid/cost-of-attendance/ (sha256 7f4ed4158cac)
- issues: conflicting_sources:https://mlc-wels.edu/academics/tuition-and-payments,https://mlc-wels.edu/financial-aid/cost-of-attendance/?s=
- checks: {"columns": 3, "components_reconcile": true, "rows": 3}
  - on_campus:Tuition: 19220 ⟵ “Tuition | $19,220 | $19,220 | $19,220”
  - on_campus:Food and Housing: 9350 ⟵ “Food and Housing | $9,350 | $9,350 | $4,675”
  - on_campus:TOTAL Fixed Cost: 28570 ⟵ “TOTAL Fixed Cost | $28,570 | $28,570 | $23,895”
  - off_campus_not_with_family:Tuition: 19220 ⟵ “Tuition | $19,220 | $19,220 | $19,220”
  - off_campus_not_with_family:Food and Housing: 9350 ⟵ “Food and Housing | $9,350 | $9,350 | $4,675”
  - off_campus_not_with_family:TOTAL Fixed Cost: 28570 ⟵ “TOTAL Fixed Cost | $28,570 | $28,570 | $23,895”
  - with_parents_or_family:Tuition: 19220 ⟵ “Tuition | $19,220 | $19,220 | $19,220”
  - with_parents_or_family:Food and Housing: 4675 ⟵ “Food and Housing | $9,350 | $9,350 | $4,675”
  - with_parents_or_family:TOTAL Fixed Cost: 23895 ⟵ “TOTAL Fixed Cost | $28,570 | $28,570 | $23,895”
### `d39bcd35163eda72` Mayo Clinic College of Medicine and Science — appeals 2026-27 [new] (source_unlabeled)
- source: https://college.mayo.edu/media/mccms/content-assets/about/college-profile/consumer-information-and-disclosures/Satisfactory_Academic_Progress_(SAP)_for_Financial_Aid_Recipients.pdf (sha256 cbc2c634e907)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Students on FA SAP suspension may appeal for the reinstatement of their financial aid.”
  - sentence: sap_appeal ⟵ “Students on FA SAP suspension may appeal for reinstatement of their financial aid.”
  - sentence: sap_appeal ⟵ “Students on FA SAP suspension may appeal for reinstatement of their financial aid.”
  - sentence: sap_appeal ⟵ “Related Procedures N/A Related Documents Deficiencies and Unsatisfactory Progress Policy (MCGSBS) Satisfactory Academic Progress Policy (MCSHS) Satisfactory Academic Progress Policy (MCASOM) Warning, Probation, Dismissal, and Appeal Policy (MCCMS) Definitions N/A References N/A Owner David Dahlen Contact Anne Dahlen Date Current Version November 21, 2025”
### `e517925aae2dad53` Mayo Clinic College of Medicine and Science — appeals 2026-27 [new] (source_unlabeled)
- source: https://college.mayo.edu/media/mccms/content-assets/about/college-profile/consumer-information-and-disclosures/Satisfactory_Academic_Progress_(SAP)_for_Financial_Aid_Recipients.pdf (sha256 cbc2c634e907)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “The student may appeal this determination if there are extenuating circumstances such as a death in the family, student injury, illness or other special circumstances. o Student must submit the appeal, including explanation as to why MCSHS standards were not met, in writing to MCCMS Director of Financial Aid.”
  - sentence: need_based_special_circumstances ⟵ “The student may appeal this determination if there are extenuating circumstances such as a death in the family, student injury, illness or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “The student may appeal this determination if there are extenuating circumstances such as a death in the family, student injury, illness or other special circumstances.”
### `22f002f7f860a757` Metropolitan State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/finances/aid/policies/sap (sha256 ddb73fd36cbe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Form Maximum Time Frame Appeal Submit this appeal form if you have reached max time frame and have a hold.”
### `960adddb8149d200` Metropolitan State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/finances/aid/policies/sap (sha256 ddb73fd36cbe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Circumstances outside of a student's control that affect academic performance include, but are not limited to: Death of a family member or close relative or friend, Car accident, Effects of physical or mental illness Unemployment or other sudden and unexpected change in financial situation Divorce or separation from a spouse Military deployment of student or student's spouse.”
### `d746bc4c1762ae80` Metropolitan State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.metrostate.edu/finances/aid/policies/sap (sha256 ddb73fd36cbe)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Extraordinary Circumstances The Director of Financial Aid, using his or her professional judgment supported by adequate documentation, may place a student on immediate financial aid suspension: A.”
### `10ee4d456245f727` Metropolitan State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/ib-course-awards/a-f (sha256 132f681c2eb0)
- issues: course_column_missing, conflicting_sources:https://www.metrostate.edu/admissions/ib-course-awards/g-l,https://www.metrostate.edu/admissions/ib-course-awards/m-z
- checks: {"distinct_exams": 12, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[IB-MUSIC|HL 4]:  ⟵ “Arts 001 Music Higher Level | 6 | 4 | Goal 6: The Humanities and Fine Arts*Diploma Award”
  - equivalencies[IB-MUSIC|SL 4]:  ⟵ “Arts 002 Music Standard Level Solo | 2 | 4 | Goal 6: The Humanities and Fine Arts*Diploma Award”
  - equivalencies[IB-THEATRE|HL 4]:  ⟵ “Arts 008 Theatre Arts Higher Level | 6 | 4 | Goal 6: The Humanities and Fine Arts*Diploma Award”
  - equivalencies[IB-THEATRE|SL 4]:  ⟵ “Arts 009 Theatre Arts Standard Level | 2 | 4 | Goal 6: The Humanities and Fine Arts*Diploma Award”
  - equivalencies[IB-FILM|HL 4]:  ⟵ “Arts 012 Film Higher Level | 2 | 4 | Goal 6: The Humanities and Fine Arts*Diploma Award”
  - equivalencies[IB-BIOLOGY|HL 4]:  ⟵ “Biology 001 Higher Level | 6 | 4 | Goal 3: Natural Sciences”
  - equivalencies[IB-BIOLOGY|SL 4]:  ⟵ “Biology 002 Standard Level | 2 | 4 | Goal 3: Natural Sciences”
  - equivalencies[IB-BUSINESS-MANAGEMENT|HL 4]:  ⟵ “Business Management 003 Higher Level | 6 | 4 | Elective”
  - equivalencies[IB-BUSINESS-MANAGEMENT|SL 4]:  ⟵ “Business Management 004 Standard Level | 2 | 4 | Elective”
  - equivalencies[IB-CHEMISTRY|HL 4]:  ⟵ “Chemistry 003 Higher Level | 6 | 4 | Goal 3: Natural Sciences”
  - equivalencies[IB-CHEMISTRY|SL 4]:  ⟵ “Chemistry 004 Standard Level | 2 | 4 | Goal 3: Natural Sciences”
  - equivalencies[IB-COMPUTER-SCIENCE|HL 4]:  ⟵ “Computer Science 001 Higher Level | 6 | 4 | Elective”
  - equivalencies[IB-ECONOMICS|HL 4]:  ⟵ “Economics 005 Higher Level | 6 | 4 | Goal 5: History and the Social and Behavioral Sciences”
  - equivalencies[IB-ECONOMICS|SL 4]:  ⟵ “Economics 006 Standard Level | 2 | 4 | Goal 5: History and the Social and Behavioral Sciences”
  - equivalencies[IB-ENGLISH-A-LITERATURE|HL 4]:  ⟵ “English A: Literature Higher Level | 6 | 4 | Goal 6: The Humanities and Fine Arts*Diploma Award”
  - equivalencies[IB-ENGLISH-A-LITERATURE|SL 4]:  ⟵ “English A: Literature Standard Level | 3 | 4 | Goal 6: The Humanities and Fine Arts | ”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4]:  ⟵ “Essay 003 Sociology Cultural Anthropology | 2 | 4 | Goal 1: Communication”
  - equivalencies[IB-PHYSICS|HL 4]:  ⟵ “Experience Science 008 Physics Higher Level | 6 | 4 | Goal 3: Natural Sciences*Diploma Award”
  - equivalencies[IB-PHYSICS|SL 4]:  ⟵ “Experience Science 009 Physics Standard Level | 2 | 4 | Goal 3: Natural Sciences*Diploma Award”
  - equivalencies[IB-FRENCH|HL 4]:  ⟵ “French 052 A1 Higher Level | 6 | 4 | Goal 3: Natural Sciences*Diploma Award”
  - equivalencies[IB-FRENCH|SL 4]:  ⟵ “French 053 A1 Standard Level | 2 | 4 | Goal 6: The Humanities and Fine Arts”
### `12495889448e5827` Metropolitan State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/ib-course-awards/g-l (sha256 aa24101a7eb3)
- issues: course_column_missing, conflicting_sources:https://www.metrostate.edu/admissions/ib-course-awards/a-f,https://www.metrostate.edu/admissions/ib-course-awards/m-z
- checks: {"distinct_exams": 3, "equivalencies": 6, "rows_without_score": 0}
  - equivalencies[IB-GEOGRAPHY|HL 4]:  ⟵ “Geography 007 Higher Level | 6 | 4 | Goal 5: History and the Social and Behavioral Sciences, Goal 10: People and the Environment”
  - equivalencies[IB-GEOGRAPHY|SL 4]:  ⟵ “Geography 008 Standard Level | 2 | 4 | Goal 5: History and the Social and Behavioral Sciences, Goal 10: People and the Environment”
  - equivalencies[IB-GERMAN|HL 4]:  ⟵ “German 059 A1 Higher Level | 6 | 4 | Goal 6: The Humanities and Fine Arts”
  - equivalencies[IB-GERMAN|SL 4]:  ⟵ “German 060 A1 Standard Level | 2 | 4 | Goal 6: The Humanities and Fine Arts”
  - equivalencies[IB-HISTORY|SL 4]:  ⟵ “History 009 Standard Level | 2 | 4 | Goal 5: History and the Social and Behavioral Sciences, Goal 8: Global Perspective”
  - equivalencies[IB-HISTORY|HL 4]:  ⟵ “History 025 Higher Level | 6 | 4 | Goal 5: History and the Social and Behavioral Sciences, Goal 8: Global Perspective”
### `196c6d124e5350d1` Metropolitan State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/ap-course-awards (sha256 f10e942ce780)
- issues: course_column_missing
- checks: {"distinct_exams": 37, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | 3 | Goal 5: History and the Social and Behavioral Sciences, Goal 7A: Human Diversity”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research | 3 | 3 | Goal 1: Communication”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar | 3 | 3 | Elective”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | Goal 6: The Humanities and Fine Arts”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 5 | Goal 3: Natural Sciences”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | Goal 4: Mathematical or Logical Reasoning”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 8 | Goal 4: Mathematical or Logical Reasoning”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 10 | Goal 3: Natural Sciences”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | 3 | Goal 8: Global Perspective”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government | 3 | 3 | Goal 5: History and the Social and Behavioral Sciences, Goal 8: Global Perspective”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 8 | Elective”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | 4 | Elective”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | 3 | Goal 1: Communication”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | 3 | Goal 6: The Humanities and Fine Arts”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 3 | Goal 3: Natural Sciences, Goal 10: People and the Environment”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 | Goal 5: History and the Social and Behavioral Sciences, Goal 8: Global Perspective”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | 3 | Goal 8: Global Perspective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture | 3 | 3 | Goal 8: Global Perspective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | Goal 5: History and the Social and Behavioral Sciences, Goal 10: People and the Environment”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture | 3 | 3 | Goal 8: Global Perspective”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture | 3 | 3 | Goal 8: Global Perspective”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | 3 | 3 | Goal 6: Humanities and the Fine Arts”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 3 | Goal 5: History and the Social and Behavioral Sciences”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 3 | Goal 5: History and the Social and Behavioral Sciences”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 3 | Goal 6: Humanities and the Fine Arts”
  - … 12 more rows
### `3db7bc38f6cc707b` Metropolitan State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/ib-course-awards/m-z (sha256 ff9e352748ee)
- issues: course_column_missing, conflicting_sources:https://www.metrostate.edu/admissions/ib-course-awards/a-f,https://www.metrostate.edu/admissions/ib-course-awards/g-l
- checks: {"distinct_exams": 5, "equivalencies": 10, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|HL 4]:  ⟵ “Social and Cultural Anthropology 002 Higher Level | 2 | 4 | Goal 5: History and the Social and Behavioral Sciences”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|SL 4]:  ⟵ “Social and Cultural Anthropology 002 Standard Level | 2 | 4 | Goal 5: History and the Social and Behavioral Sciences”
  - equivalencies[IB-PHILOSOPHY|HL 4]:  ⟵ “Social Science 019 Philosophy Higher Level | 6 | 4 | Goal 6: The Humanities and Fine Arts*Diploma Award”
  - equivalencies[IB-PSYCHOLOGY|HL 4]:  ⟵ “Social Science 021 Psychology Higher Level | 2 | 4 | Goal 6: The Humanities and Fine Arts*Diploma Award”
  - equivalencies[IB-PSYCHOLOGY|SL 4]:  ⟵ “Social Science 022 Psychology Standard Level | 2 | 4 | Goal 5: History and the Social and Behavioral Sciences*Individual Course Award”
  - equivalencies[IB-SPANISH|HL 4]:  ⟵ “Spanish 159 A1 Higher Level | 2 | 4 | Goal 6: The Humanities and Fine Arts”
  - equivalencies[IB-SPANISH|SL 4]:  ⟵ “Spanish 160 A1 Standard Level | 2 | 4 | Goal 6: The Humanities and Fine Arts”
  - equivalencies[IB-SPANISH|4]:  ⟵ “Spanish 352 Language and Literature | 2 | 4 | Goal 8: Global Perspective”
  - equivalencies[IB-VISUAL-ARTS|HL 4]:  ⟵ “Visual Arts 005 Higher Level | 6 | 4 | Goal 6: The Humanities and Fine Arts”
  - equivalencies[IB-VISUAL-ARTS|SL 4]:  ⟵ “Visual Arts 006 Standard Level | 2 | 4 | Goal 6: The Humanities and Fine Arts”
### `986aa24ae05328f6` Metropolitan State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.metrostate.edu/admissions/clep-course-awards (sha256 fb34d5f8b4a0)
- issues: score_column_not_scores, score_scale_mismatch, course_column_missing
- checks: {"distinct_exams": 6, "equivalencies": 14, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|College Mathematics (May 2001–April 2023)]:  ⟵ “College Mathematics (May 2001–April 2023) | 50 | 6 | Goal 4: Mathematical or Logical Reasoning”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French – College Level 1]:  ⟵ “French – College Level 1 | 50 | 6 | Goal 8: Global Perspective”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French – College Level 2]:  ⟵ “French – College Level 2 | 59 | 9 | Goal 8: Global PerspectiveGoal 6: The Humanities and Fine Arts”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French – College Level 2 (January 2008–December 2014)]:  ⟵ “French – College Level 2 (January 2008–December 2014) | 59 | 12 | Goal 8: Global PerspectiveGoal 6: The Humanities and Fine Arts | ”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German – College Level 2]:  ⟵ “German – College Level 2 | 60 | 9 | Goal 8: Global Perspective”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German – College Level 2 (January 2008–December 2014)]:  ⟵ “German – College Level 2 (January 2008–December 2014) | 60 | 12 | Goal 8: Global Perspective”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|Information Systems (CLEP 0022 through December 2010)]:  ⟵ “Information Systems (CLEP 0022 through December 2010) | 50 | 3 | Elective”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|Information Systems and Computer Apps (May 2007–December 2010)]:  ⟵ “Information Systems and Computer Apps (May 2007–December 2010) | 50 | 3 | Elective”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|Information Systems (CLEP 0022) *5 year sunset*]:  ⟵ “Information Systems (CLEP 0022) *5 year sunset* | 50 | 4 | Elective”
  - equivalencies[CLEP-SPANISH-LANGUAGE|Spanish – College Level 1]:  ⟵ “Spanish – College Level 1 | 50 | 6 | Goal 8: Global Perspective”
  - equivalencies[CLEP-SPANISH-LANGUAGE|Spanish – College Level 2]:  ⟵ “Spanish – College Level 2 | 63 | 9 | Goal 8: Global Perspective”
  - equivalencies[CLEP-SPANISH-LANGUAGE|Spanish – College Level 2 (August 2007–December 2014)]:  ⟵ “Spanish – College Level 2 (August 2007–December 2014) | 63 | 12 | Goal 8: Global Perspective”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|Spanish with Writing Level 1]:  ⟵ “Spanish with Writing Level 1 | 50 | 6 | Goal 8: Global Perspective”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|Spanish with Writing Level 2]:  ⟵ “Spanish with Writing Level 2 | 65 | 9 | Goal 8: Global Perspective”
### `c53df29bce25a344` Minneapolis College of Art and Design — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.mcad.edu/index%2ephp/admissions-aid/financial-aid/apply-aid (sha256 9e43b9dad28f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Submit the FAFSA Verification Process Financial Aid Award Notification Accept Financial Aid Award Other Financing Options Pay Remaining Semester Balance Special Circumstances Financial Aid Appeal Process Step 1: Submit the Free Application for Federal Student Aid (FAFSA) Complete the Free Application for Federal Student Aid (FAFSA) each academic year to receive priority for need-based financial ai”
  - sentence: need_based_special_circumstances ⟵ “Step 7: Special Circumstances Financial Aid Appeal Process MCAD understands that special circumstances occur which may affect a student's financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “The following are examples of special circumstances: Significant loss or reduction of employment, wages, or unemployment compensation.”
  - sentence: need_based_special_circumstances ⟵ “Loss of child support Please contact the Financial Aid Office to discuss your special circumstances situation(s) and to receive the form.”
### `17b37d24d0823e64` Minneapolis College of Art and Design — transfer_policies 2020-21 [new] (labeled_in_source)
- source: https://www.mcad.edu/sites/default/files/2021-07/Watkins%20to%20MCAD%20Fact%20Sheet%20and%20Guide%20-%20%20Transfer%20Student%20February%202020.pdf (sha256 df099da78152)
- issues: stale_year_label:2020-21
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “MCAD will consider transferring in any Watkins liberal arts or studio arts credits that meet our curriculum requirements with a grade of C or better (no C-).”
  - min_grade: C ⟵ “Credit will only transfer from regionally-accredited institutions with a class grade of C or better.”
### `4186c0a3b68a0a56` Minneapolis College of Art and Design — transfer_policies 2019-20 [new] (labeled_in_source)
- source: https://www.mcad.edu/sites/default/files/2021-07/OCAC%20to%20MCAD%20Fact%20Sheet%20Transfer%20Student%20February%202019.pdf (sha256 8b1b8a2dfb4b)
- issues: stale_year_label:2019-20
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “MCAD will consider transferring in any OCAC liberal arts or studio arts credits that meet our curriculum requirements with a grade of C or better.”
  - min_grade: C ⟵ “Credit will only transfer from regionally-accredited institutions with a class grade of C or better.”
### `f99d5654a5fd5494` Minneapolis College of Art and Design — transfer_policies 2024-25 [new] (labeled_in_source)
- source: https://www.mcad.edu/sites/default/files/2024-06/UArts%20to%20MCAD%20UG%20Fact%20Sheet%20Transfer%20Student%20June%202024.pdf (sha256 055598b62769)
- issues: stale_year_label:2024-25
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “MCAD will consider transferring in any‬ ‭UArts liberal arts or studio arts credits that meet our curriculum requirements with a grade of C or better.”
### `m50b7338d8e15dc2` Minneapolis College of Art and Design — transfer_policies 2022-23 [new] (labeled_in_source)
- source: https://www.mcad.edu/sites/default/files/2022-05/SFAI%20to%20MCAD%20UG%20Fact%20Sheet%20Transfer%20Student%20May%202022.pdf (sha256 48ca1807d7d2)
- issues: stale_year_label:2022-23
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “MCAD will consider transferring in any SFAI liberal arts or studio arts credits that meet our curriculum requirements with a grade of C or better.”
  - min_grade: C ⟵ “MCAD will consider transferring in any SFAI liberal arts or studio arts credits that meet our MFA curriculum requirements with a grade of C or better.”
  - min_grade: C ⟵ “MCAD will consider transferring in any SFAI liberal arts or studio arts credits that meet our curriculum requirements with a grade of C or better.”
### `60856828f78e1e24` Minneapolis Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://minneapolis.edu/satisfactory-academic-progress-help (sha256 9379f4ca9d43)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If you are not satisfied with this decision, you have the right to request a second review of your appeal by the Satisfactory Academic Progress Committee.”
  - sentence: sap_appeal ⟵ “If you are not satisfied with this decision, you have the right to request a second review of your appeal by the Satisfactory Academic Progress Committee.”
### `0a26e9f313b847e2` Minnesota North College — appeals 2026-27 [new] (labeled_in_source)
- source: https://minnesotanorth.edu/admissions/financial-aid/ (sha256 fbe67efe5c3b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Document Uploader Forms Consortium Credit Request Max Time Frame Petition Special Circumstances Request Academic and Financial Aid Suspension Appeal Loan Adjustment Form Federal Loan Instructions Unusual Enrollment Petition Grants & Scholarships A variety of financial aid sources are available to help you pay for college or career school.”
### `1da6dd84dfb9d43b` Minnesota North College — appeals 2023-24 [new] (labeled_in_source)
- source: https://minnesotanorth.edu/admissions/financial-aid/financial-aid-faqs/ (sha256 98ef0aea89aa)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “A Professional Judgement Appeal is an option for households that have experienced a loss of income greater than 15%, or major unreimbursed medical/dental expenses (those not covered by medical insurance and greater than 10% of total income) since the tax year requested on the FAFSA.”
### `d7d1fc0b76e1437b` Minnesota North College — appeals 2023-24 [new] (labeled_in_source)
- source: https://minnesotanorth.edu/admissions/financial-aid/financial-aid-faqs/ (sha256 98ef0aea89aa)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Dependent students that do not have unusual circumstances, but whose parents are unwilling to provide information or tax data for FAFSA completion, may still be eligible for an unsubsidized loan.”
### `849d3457b35d4a64` Minnesota North College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://minnesotanorth.edu/admissions/tuition-costs/ (sha256 f2c5a09fe498)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition & Fees*: 6649.0 ⟵ “Tuition & Fees* | $6,649.00”
  - column:Books: 660.0 ⟵ “Books | $660.00”
  - column:Total Direct Costs: 7309.0 ⟵ “Total Direct Costs | $7,309.00”
  - column:Food and Housing: 8066.0 ⟵ “Food and Housing | $8,066.00”
  - column:Transportation**: 2096.0 ⟵ “Transportation** | $2,096.00”
  - column:Miscellaneous Expenses***: 2525.0 ⟵ “Miscellaneous Expenses*** | $2,525.00”
  - column:Average Student Loan Cost: 44.0 ⟵ “Average Student Loan Cost | $44.00”
  - column:Budget Total: 20040.0 ⟵ “Budget Total | $20,040.00”
### `4534810b7fcb0704` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/ (sha256 cc0df28e18a5)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12414 ⟵ “Approximate Tuition/Fees: | $12,414”
  - column:Books/Supplies:: 500 ⟵ “Books/Supplies: | $500”
  - column:Estimated Total:: 12914 ⟵ “Estimated Total: | $12,914”
### `4f5234cdb6841f44` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/ (sha256 47ff8c3168b2)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12414 ⟵ “Approximate Tuition/Fees: | $12,414”
  - column:Books/Supplies:: 530 ⟵ “Books/Supplies: | $530”
  - column:Estimated Total:: 12944 ⟵ “Estimated Total: | $12,944”
### `569b90ee80c00375` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/ (sha256 c4bf80f1b8ce)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12414 ⟵ “Approximate Tuition/Fees: | $12,414”
  - column:Books/Supplies:: 700 ⟵ “Books/Supplies: | $700”
  - column:Estimated Total:: 13114 ⟵ “Estimated Total: | $13,114”
### `5ad917a5fc311e52` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/ (sha256 ff6e84e01f88)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12414 ⟵ “Approximate Tuition/Fees: | $12,414”
  - column:Books/Supplies:: 540 ⟵ “Books/Supplies: | $540”
  - column:Estimated Total:: 12954 ⟵ “Estimated Total: | $12,954”
### `72707cdca7e130f1` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/ (sha256 72267299729f)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12414 ⟵ “Approximate Tuition/Fees: | $12,414”
  - column:Books/Supplies:: 800 ⟵ “Books/Supplies: | $800”
  - column:Estimated Total:: 13214 ⟵ “Estimated Total: | $13,214”
### `826927616a4d77ec` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/ (sha256 9524d5165267)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12414 ⟵ “Approximate Tuition/Fees: | $12,414”
  - column:Books/Supplies:: 585 ⟵ “Books/Supplies: | $585”
  - column:Estimated Total:: 12999 ⟵ “Estimated Total: | $12,999”
### `8358d64f52c916d9` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/ (sha256 80e05139e787)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 13914 ⟵ “Approximate Tuition/Fees: | $13,914”
  - column:Books/Supplies:: 700 ⟵ “Books/Supplies: | $700”
  - column:Estimated Total:: 14614 ⟵ “Estimated Total: | $14,614”
### `e3663eaf35dc1b39` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/ (sha256 8770049fe392)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12414 ⟵ “Approximate Tuition/Fees: | $12,414”
  - column:Books/Supplies:: 600 ⟵ “Books/Supplies: | $600”
  - column:Estimated Total:: 13014 ⟵ “Estimated Total: | $13,014”
### `e4cd9b37ea2b3325` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/ (sha256 8c27cb7fb04c)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12932 ⟵ “Approximate Tuition/Fees: | $12,932”
  - column:Books/Supplies:: 620 ⟵ “Books/Supplies: | $620”
  - column:Estimated Total:: 13552 ⟵ “Estimated Total: | $13,552”
### `f6ec798596c4af75` Minnesota State College Southeast — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southeastmn.edu:443/programs/english-transfer-pathway/english-transfer-pathway/ (sha256 7b574771355f)
- issues: residency_unknown, conflicting_sources:https://www.southeastmn.edu:443/programs/accounting-transfer-pathway/accounting-transfer-pathway/,https://www.southeastmn.edu:443/programs/business-transfer-pathway/business-transfer-pathway/,https://www.southeastmn.edu:443/programs/criminal-justice/criminal-justice-transfer-pathway/,https://www.southeastmn.edu:443/programs/early-childhood-education/early-childhood-transfer-pathway/,https://www.southeastmn.edu:443/programs/economics-transfer-pathway/economics-transfer-pathway/,https://www.southeastmn.edu:443/programs/political-science-transfer-pathway/political-science-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/pre-social-work-transfer-pathway/pre-social-work-transfer-pathway-as/,https://www.southeastmn.edu:443/programs/psychology-transfer-pathway/psychology-transfer-pathway-aa/,https://www.southeastmn.edu:443/programs/sociology-transfer-pathway/sociology-transfer-pathway-aa/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Approximate Tuition/Fees:: 12414 ⟵ “Approximate Tuition/Fees: | $12,414”
  - column:Books/Supplies:: 800 ⟵ “Books/Supplies: | $800”
  - column:Estimated Total:: 13214 ⟵ “Estimated Total: | $13,214”
### `6e76cb2f51bc3507` Minnesota State Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.minnesota.edu/about/policies-and-procedures/satisfactory-academic-progress-sap-academic-and-financial-aid (sha256 9b09683b9ced)
- issues: semantic_review_required, conflicting_sources:https://www.minnesota.edu/help-topics/satisfactory-academic-progress-appeal
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Students who have been suspended may regain eligibility through the College’s Satisfactory Academic Progress (SAP) appeal process or returning after the suspension period.”
  - sentence: sap_appeal ⟵ “Probation Status The status of a student who: A) Returns after an academic suspension period; B) Has successfully appealed a satisfactory academic progress suspension; C) Transfers to Minnesota State Community and Technical College after an academic suspension period at another Minnesota State system institution.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal A form completed by the student requesting to be reinstated as a student in probationary status after having been placed on academic suspension.”
  - sentence: sap_appeal ⟵ “The link to the Satisfactory Academic Progress Appeal form can be found at Forms.”
  - sentence: sap_appeal ⟵ “If at the end of that term the student is either reinstated to good academic standing or academically suspended and may submit a Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “The College follows the Minnesota State system 2.9.1 Academic Standing and Financial Aid Satisfactory Academic Progress Procedure to consider appeals for reinstatement and to consider admittance for students on suspension from other Minnesota State system institutions.”
### `df592a2a52ddfa32` Minnesota State Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.minnesota.edu/help-topics/satisfactory-academic-progress-appeal (sha256 c3e6a1104e4f)
- issues: semantic_review_required, conflicting_sources:https://www.minnesota.edu/about/policies-and-procedures/satisfactory-academic-progress-sap-academic-and-financial-aid
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If this can be documented for the specific semester(s) when deficiencies occurred, you may submit the Satisfactory Academic Progress Appeal form along with all required documentation.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress appeals and all supporting documentation must be received by Student Services-Processing Center no later than one week prior to the beginning of the new semester for which you are requesting reinstatement.”
### `15534480c675f26a` Minnesota State Community and Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://tuition.minnesota.edu/programs/465 (sha256 eecf5687481e)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, conflicting_sources:https://www.minnesota.edu/tuition-and-expenses
- checks: {"columns": 2, "components_reconcile": false, "rows": 1}
  - column:Total Tuitions: 9766.0 ⟵ “Total Tuitions | $9,766.00”
  - column:PNSG Tuition: 9766.0 ⟵ “PNSG Tuition | $244.15/Credit* | $9,766.00”
### `ea3684e43415839f` Minnesota State Community and Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.minnesota.edu/tuition-and-expenses (sha256 92f2f43f2d61)
- issues: residency_unknown, conflicting_sources:https://tuition.minnesota.edu/programs/465
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Housing and Meals: 9350 ⟵ “Housing and Meals | $4,675 | $9,350”
  - column:Books and Supplies: 2140 ⟵ “Books and Supplies | $1,070 | $2,140”
  - column:Personal (includes loan fees): 1490 ⟵ “Personal (includes loan fees) | $745 | $1,490”
  - column:Transportation: 2500 ⟵ “Transportation | $1,250 | $2,500”
  - column:Tuition: 6270 ⟵ “Tuition | $3,135 | $6,270”
  - column:Fees: 484 ⟵ “Fees | $242 | $484”
  - column:Total Cost of Attendance: 22234 ⟵ “Total Cost of Attendance | $11,117 | $22,234”
### `1a59afed58d84733` Minnesota State University Moorhead — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.mnstate.edu/cost-aid/financial-aid/awards (sha256 4101448be5a6)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “This review is called a professional judgment appeal.”
### `808c95255e979d27` Minnesota State University Moorhead — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.mnstate.edu/cost-aid/financial-aid/awards (sha256 4101448be5a6)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “There are two types of appeals: Special Circumstance appeals refer to changes to a student's or parent financial circumstances since the FAFSA was filed.”
  - sentence: need_based_special_circumstances ⟵ “Submit a Special Circumstances Form if this applies to you.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances appeals refer to conditions that justify changes to a your dependency status such as human trafficking, parental abandonment, or incarceration.”
### `3fe2e4f32767c0f5` Normandale Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.normandale.edu/admissions/paying-for-college/scholarships-and-aid/financial-aid-forms.html (sha256 11c82c9da8bb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Parents will not provide information for the FAFSA or verification Parents do not claim the student as a dependent for income tax purposes Student demonstrates self-sufficiency Process for Requesting a Dependency Override: For petitions you must complete the appropriate form and provide the documentation listed before we can review your request. 2026-27 Petition for Dependency Override Please use ”
  - sentence: dependency_override ⟵ “For petitions you must complete the appropriate year form and provide the documentation listed before we can review your request. 2026-27 Petition for Dependency Override Please use the Financial Aid Secure Document Submitter to submit your Petition and additional documentation.”
### `4677237ae62958bb` Normandale Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.normandale.edu/admissions/paying-for-college/scholarships-and-aid/financial-aid-forms.html (sha256 11c82c9da8bb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Petitions for Unusual or Special Circumstances What is a dependency override?”
  - sentence: need_based_special_circumstances ⟵ “Excluding parent information to get Unsubsidized Loan only Change in financial situation since 2022 - Petition for Special Circumstances Unusual Circumstances/Dependency Override Request (additional flexibilities for assisting students with unusual circumstances) Beginning with the 2024-2025 Award year both first time and renewal applicants who indicated they have an unusual circumstance on their ”
  - sentence: need_based_special_circumstances ⟵ “If you are requesting a reconsideration of your dependent status through Dependency Override: We recognize that students can experience unusual circumstances in their household that may require additional consideration.”
  - sentence: need_based_special_circumstances ⟵ “There must be unusual circumstances in the household to be considered for a Dependency Override.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances do not include: Parents refuse to contribute to the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “If you selected Unusual Circumstances on your FAFSA and in error, you must correct your responses to the FAFSA Student Personal Circumstances to "None of these apply." Then, include your parents'/contributors information and signature.”
### `48dc60521a2fd9b9` Normandale Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.normandale.edu/current-students/student-services/registration/academic-progress/complete-policy-statement.html (sha256 2ba07d142aa5)
- issues: semantic_review_required, conflicting_sources:https://www.normandale.edu/admissions/paying-for-college/scholarships-and-aid/financial-aid-forms.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals and Probation Appeals A student who fails to make satisfactory academic progress and is suspended has the right to appeal based on special, unusual or extenuating circumstances causing undue hardship such as death in the family, student's injury or illness or other special circumstances as determined by the college.”
### `7109771192c3ff86` Normandale Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.normandale.edu/admissions/paying-for-college/scholarships-and-aid/financial-aid-forms.html (sha256 11c82c9da8bb)
- issues: semantic_review_required, conflicting_sources:https://www.normandale.edu/current-students/student-services/registration/academic-progress/complete-policy-statement.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Student Document Submitter (Login using your StarID and password) Parent Document Submitter (Login not required, please have student tech ID or StarId ready to include) Satisfactory Academic Progress Appeal Note: forms are not year-specific.”
### `8352983ac2a65776` Normandale Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.normandale.edu/admissions/paying-for-college/index.html (sha256 1cc1d9b49fd7)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 8}
  - column:Tuition and Fees (based on 15 credits per term for 2 term academic year): 6566 ⟵ “Tuition and Fees (based on 15 credits per term for 2 term academic year) | $3,283 | $3,283 | $6,566”
  - column:Books and Supplies: 1000 ⟵ “Books and Supplies | $500 | $500 | $1,000”
  - column:Total Direct Costs: 7566 ⟵ “Total Direct Costs | $3,783 | $3,783 | $7,566”
  - column:Housing: 7146 ⟵ “Housing | $3,573 | $3,573 | $7,146”
  - column:Food: 3.063 ⟵ “Food | $1,532 | $1,531 | $3.063”
  - column:Transportation(to/from campus, fuel, insurance, vehicle maintenance, etc.): 2080 ⟵ “Transportation(to/from campus, fuel, insurance, vehicle maintenance, etc.) | $1,040 | $1,040 | $2,080”
  - column:Personal Expenses (includes costs of utilities, toiletries, internet, loan fees, certifications, etc): 6617 ⟵ “Personal Expenses (includes costs of utilities, toiletries, internet, loan fees, certifications, etc) | $3,308 | $3,309 | $6,617”
  - column:Total Est. Indirect Costs: 18906 ⟵ “Total Est. Indirect Costs | $9,453 | $9,453 | $18,906”
### `fde070b7f9efa48d` Normandale Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.normandale.edu/admissions/paying-for-college/index.html (sha256 1cc1d9b49fd7)
- issues: components_do_not_reconcile, multiple_total_rows, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - column:Tuition and Fees (based on MN resident rate, 15 credits per term for 2 term academic year): 6858 ⟵ “Tuition and Fees (based on MN resident rate, 15 credits per term for 2 term academic year) | $3,429 | $3,429 | $6,858”
  - column:Books and Supplies: 1000 ⟵ “Books and Supplies | $500 | $500 | $1,000”
  - column:Total Direct Costs: 7858 ⟵ “Total Direct Costs | $3,929 | $3,929 | $7,858”
  - column:Housing: 7211 ⟵ “Housing | $3,606 | $3,605 | $7,211”
  - column:Food: 3393 ⟵ “Food | $1,696 | $1,697 | $3,393”
  - column:Transportation(to/from campus, fuel, insurance, vehicle maintenance, etc.): 2243 ⟵ “Transportation(to/from campus, fuel, insurance, vehicle maintenance, etc.) | $1,122 | $1,121 | $2,243”
  - column:Personal Expenses (includes costs of utilities, toiletries, internet, loan fees, certifications, etc): 7546 ⟵ “Personal Expenses (includes costs of utilities, toiletries, internet, loan fees, certifications, etc) | $3,773 | $3,773 | $7,546”
### `1b21a50d546cc64b` Normandale Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.normandale.edu/academics/degrees-certificates/catalog-files/Elementary%20Education%20Foundations%20Transfer%20Pathway%20AS.pdf (sha256 0c4af96aa537)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `98b749fbe7d38cfe` North Central University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.northcentral.edu/financial-aid/tuition-and-fees/ (sha256 c311ce942538)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition & Fees (est.): 14850 ⟵ “Tuition & Fees (est.) | $14,850”
  - on_campus:Housing (est.): 4030 ⟵ “Housing (est.) | $4,030”
  - on_campus:Food Allowance (est.): 5580 ⟵ “Food Allowance (est.) | $5,580”
  - on_campus:Books/Supplies/Equipment (est., not billable): 900 ⟵ “Books/Supplies/Equipment (est., not billable) | $900”
  - on_campus:Misc. Personal Expenses (est., not billable): 3000 ⟵ “Misc. Personal Expenses (est., not billable) | $3,000”
  - on_campus:Transportation (est., not billable): 350 ⟵ “Transportation (est., not billable) | $350”
  - on_campus:Loan Fees (est., not billable): 140 ⟵ “Loan Fees (est., not billable) | $140”
  - on_campus:Total (Fall and Spring): 28850 ⟵ “Total (Fall and Spring) | $28,850”
### `6d7e9eef824e7374` North Central University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.northcentral.edu/wp-content/uploads/2025/12/clep-examinations.pdf (sha256 1dafc8f6ddf1)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 22, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|3]:  ⟵ “Financial Accounting                                     (60)                  BUS 267 Principles of Accounting I                       3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Principles of Macroeconomics                             (60)                  ECON 256 Principles of Macroeconomics                    3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3]:  ⟵ “Principles of Microeconomics                             (60)                  ECON 251 Principles of Microeconomics                    3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|3]:  ⟵ “American Literature                                      (50)                English Elective                                           3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature                                       (50)                English Elective                                           3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|3]:  ⟵ “College Composition (includes essays)                      (60)              ENG 124 Rhetoric & Research                                     3”
  - equivalencies[CLEP-HUMANITIES|2]:  ⟵ “Humanities                                               (50)                   Fine Arts Elective                                      2”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|3]:  ⟵ “History of the United States II                          (50)                  HIST 226 American History II                             3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|3]:  ⟵ “Western Civilization I                                   (50)                  History Elective                                         3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|3]:  ⟵ “Western Civilization II                                  (50)                  History Elective                                         3”
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus                                                 (50)                  MATH 280 Calculus I                                      4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra                                          (50)                  MATH 125 College Algebra I                               3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|3]:  ⟵ “College Mathematics                                      (50)                  MATH 115 Liberal Arts Mathematics                        3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|4]:  ⟵ “French Language Level I                                  (50)                  Modern Language Elective                                 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|4]:  ⟵ “German Language Level I                                  (50)                  Modern Language Elective                                 4”
  - equivalencies[CLEP-SPANISH-LANGUAGE|4]:  ⟵ “Spanish Language Level I                                 (50)                  Modern Language Elective                                 4”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Introductory Psychology                                  (50)                  PSYC 125 General Psychology                              3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|3]:  ⟵ “Introductory Sociology                                   (50)                  SWK 126 Introduction to Sociology                        3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|3]:  ⟵ “Intro to Educational Psychology                             (50)                     EDUC 359 Educational Psychology                             3”
  - equivalencies[CLEP-BIOLOGY|3]:  ⟵ “Biology                                                  (50)                  SCI 118 Biology                                          3”
  - equivalencies[CLEP-CHEMISTRY|3]:  ⟵ “Chemistry                                                (50)                  Science Elective                                         3”
  - equivalencies[CLEP-NATURAL-SCIENCES|3]:  ⟵ “Natural Sciences                                         (50)                  Science Elective                                         3”
### `a73d9f6ad5795e05` North Central University — credit_policies 2023-24 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.northcentral.edu/wp-content/uploads/2025/12/ap_exam_chart.pdf (sha256 fa3ea2034b79)
- issues: stale_year_label:2023-24
- checks: {"distinct_exams": 26, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                                        3            Fine Arts elective                                   3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Drawing                                     3            Fine Arts elective                                   3”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Studio Art 2-D Design                              3            Fine Arts elective                                   3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Studio Art 3-D Design                              3            Fine Arts elective                                   3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                                 3            CSCI 160 Intro to Prog. w/ Mobile Dev                3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles                        3            CSCI-180 Intro to Programming                        3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                                     3            ECON 256 Principles of Macroeconomics                3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                                     3            ECON 251 Principles of Microeconomics                3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Lang & Composition                         3            ENG 124 College Rhetoric and Research                3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Comp.                         3            ENG English Elective 215 or higher                   3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                                   3            HIST History Elective                                3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History                              3            HIST 225 American History I                          3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History: Modern                              3            HIST History Elective                                3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government & Politics                         3            GOVT Government elective                             3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                         3            PSYC 125 General Psychology                          3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                                    3            Global Studies Electives                             3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                            3            SCI 118 Biology                                      4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                          3            SCI Science Elective                                 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                              3            SCI 230 Environmental Science                        3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                        3            MATH 280 Calculus I                                  4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                                    3             MATH 280 Calculus I                                  4”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1                                      3             SCI Science Elective                                 3”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2                                      3             SCI Science Elective                                 3”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C-Electricity & Mag.                   3             SCI Science Elective                                 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C-Mechanics                            3             SCI Science Elective                                 3”
  - … 1 more rows
### `75bc9b9a82e06e31` North Hennepin Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/financial-aid-policies-procedures (sha256 e89627f25366)
- issues: semantic_review_required, conflicting_sources:https://www.nhcc.edu/admissions-aid/paying-college/how-apply-financial-aid,https://www.nhcc.edu/admissions-aid/paying-college/types-financial-aid,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/how-apply-financial-aid,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/types-financial-aid
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeals Financial aid eligibility is based on parental and/or student prior-prior year income.”
  - sentence: need_based_special_circumstances ⟵ “If a family has special circumstances, regulations allow us the option to review the financial aid application.”
  - sentence: need_based_special_circumstances ⟵ “Possible reasons for a special circumstance review include: unemployment, divorce, death of a spouse or parent, loss of child support, loss of Social Security benefits, or loss of other income benefits.”
  - sentence: need_based_special_circumstances ⟵ “Start the appeal process by completing the Appeal Special Circumstances form.”
  - sentence: need_based_special_circumstances ⟵ “The financial aid administrator’s decision on a special circumstance review is final.”
### `7984d266ecc1e62f` North Hennepin Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/how-apply-financial-aid (sha256 cb41d7b74141)
- issues: semantic_review_required, conflicting_sources:https://www.nhcc.edu/admissions-aid/paying-college/how-apply-financial-aid,https://www.nhcc.edu/admissions-aid/paying-college/types-financial-aid,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/financial-aid-policies-procedures,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/types-financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Depending on your situation, you may qualify for a special circumstance appeal.”
### `936a2c1f730c55ff` North Hennepin Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nhcc.edu/admissions-aid/paying-college/how-apply-financial-aid (sha256 611014d0397a)
- issues: semantic_review_required, conflicting_sources:https://www.nhcc.edu/admissions-aid/paying-college/types-financial-aid,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/financial-aid-policies-procedures,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/how-apply-financial-aid,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/types-financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Depending on your situation, you may qualify for a special circumstance appeal.”
### `9c5c48896c3578b2` North Hennepin Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nhcc.edu/admissions-aid/paying-college/types-financial-aid (sha256 1f268938c52b)
- issues: semantic_review_required, conflicting_sources:https://www.nhcc.edu/admissions-aid/paying-college/how-apply-financial-aid,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/financial-aid-policies-procedures,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/how-apply-financial-aid,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/types-financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Aid for Students with Special Circumstances Several aid programs support students based on life circumstances, public service or other affiliations.”
### `ac5cb92b6db0943e` North Hennepin Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/types-financial-aid (sha256 027415623da3)
- issues: semantic_review_required, conflicting_sources:https://www.nhcc.edu/admissions-aid/paying-college/how-apply-financial-aid,https://www.nhcc.edu/admissions-aid/paying-college/types-financial-aid,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/financial-aid-policies-procedures,https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/how-apply-financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Aid for Students with Special Circumstances Several aid programs support students based on life circumstances, public service or other affiliations.”
### `d7aa3424b46fb1cf` North Hennepin Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nhcc.edu/admissions-aid/paying-college/how-apply-financial-aid (sha256 611014d0397a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Review Award Offer Once your application is complete, you will receive an award offer.”
### `a694676f1de1dc7a` North Hennepin Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nhcc.edu/index%2Ephp/admissions-aid/paying-college/college-costs (sha256 391d6286f47e)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 1, "rows": 7}
  - column:Tuition/Fees: 6812 ⟵ “Tuition/Fees | $3,406 | 3,406 | 6,812”
  - column:Books and Supplies: 750 ⟵ “Books and Supplies | $375 | $375 | $750”
  - column:Total Direct Costs: 7562 ⟵ “Total Direct Costs | $3,781 | $3,781 | $7,562”
  - column:Housing and Food: 16262 ⟵ “Housing and Food | $8,131 | $8,131 | $16,262”
  - column:Transportation: 2204 ⟵ “Transportation | $1,102 | $1,102 | $2,204”
  - column:Personal/Miscellaneous: 4076 ⟵ “Personal/Miscellaneous | $2,038 | $2,038 | $4,076”
  - column:Total Estimated Indirect Costs: 22542 ⟵ “Total Estimated Indirect Costs | $11,271 | 11,271 | $22,542”
### `9c662a9124cb6a48` North Hennepin Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.nhcc.edu/sites/default/files/2024-02/CLEPEquivalenciesFeb2024.pdf (sha256 2fe996468383)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 30, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|4]:  ⟵ “Financial Accounting                                   ACCT 2111                   n/a             4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|3]:  ⟵ “Business Law, Introductory                             BUS 1300                    n/a             3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|3]:  ⟵ “Information Systems                                    CIS 1101                    n/a             3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Management, Principles of                              BUS 2200                    n/a             3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|3]:  ⟵ “Marketing, Principles of                               BUS 2600                    n/a             3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|6]:  ⟵ “American Literature                                    ENGL 2450                    6              3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|6]:  ⟵ “Analyzing & Interpreting Literature                    ENGL 2150                    6              3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|1]:  ⟵ “College Composition                                    ENGL 1201, 1202              1              6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|1]:  ⟵ “College Composition Modular                            ENGL 1201                    1              3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature                                     ENGL 2550                   6, 8            3”
  - equivalencies[CLEP-HUMANITIES|6]:  ⟵ “Humanities                                             Elective                     6              3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|6]:  ⟵ “French Language, Level 1                               Elective                     8              6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|6]:  ⟵ “German Language, Level 1                               Elective                     8              6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|6]:  ⟵ “Spanish Language, Level 1                              SPAN 1101                    8              6”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|5]:  ⟵ “Spanish with Writing Level 1                           SPAN 2201                    8              5”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government                                    POLS 1100                   5, 9            3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|5]:  ⟵ “Educational Psychology, Intro                          Elective                     5              3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|5]:  ⟵ “Human Growth & Development                             PSYC 1250                    5              4”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Macroeconomics, Principles of                          ECON 1060                   5, 8            3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|5]:  ⟵ “Microeconomics, Principles of                          ECON 1070                    5              3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|5]:  ⟵ “Psychology, Introductory                               PSYC 1150                    5              3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|5]:  ⟵ “Sociology, Introductory                                SOC 1110                     5              3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|3]:  ⟵ “Western Civ I: Ancient to 1648                         HIST 1110                   5, 8            3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|3]:  ⟵ “Western Civ II: 1648 to Present                        HIST 1120                   5, 8            3”
  - equivalencies[CLEP-BIOLOGY|3]:  ⟵ “Biology                                                (Non-lab Elective)           3              6”
  - … 5 more rows
### `2f2de177eb81f207` Northland Community and Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.northlandcollege.edu/academics/programs/criminal-justice-transfer-pathway-as/costs/ (sha256 fb699649defc)
- issues: components_do_not_reconcile, residency_unknown, conflicting_sources:https://www.northlandcollege.edu/admissions/tuition-fees/
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Books: 0 ⟵ “Books | $0”
  - column:Tuition – non TTCJ credits: 0 ⟵ “Tuition – non TTCJ credits | $0”
  - column:Tuition – TTCJ credits: 0 ⟵ “Tuition – TTCJ credits | $0”
  - column:Student Association Fee: 23.8 ⟵ “Student Association Fee | $23.80”
  - column:Student Life Fee: 448.8 ⟵ “Student Life Fee | $448.80”
  - column:Technology Fee: 646.0 ⟵ “Technology Fee | $646.00”
  - column:Supplies: 0 ⟵ “Supplies | $0”
  - column:Total: 0 ⟵ “Total | $0”
### `3ad764c6e6801b1e` Northland Community and Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.northlandcollege.edu/admissions/tuition-fees/ (sha256 87a6e6fcee24)
- issues: components_do_not_reconcile, residency_unknown, conflicting_sources:https://www.northlandcollege.edu/academics/programs/criminal-justice-transfer-pathway-as/costs/
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - column:Tuition: 6264.0 ⟵ “Tuition | $6264.00”
  - column:Student Life Fee: 205.8 ⟵ “Student Life Fee | $205.80”
  - column:Technology Fee: 356.1 ⟵ “Technology Fee | $356.10”
  - column:Student Association Fee: 18.3 ⟵ “Student Association Fee | $18.30”
  - column:Health Services Fee: 15.3 ⟵ “Health Services Fee | $15.30”
  - column:Estimated Total: 6965.4 ⟵ “Estimated Total | $6,965.40”
### `ea58ce2b69ff63a9` Northwest Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.ntcmn.edu/foundation/scholarships/workforce/ (sha256 6d7c0838fb8e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If unable to attend the ceremony, special circumstances can be considered by NTC.”
### `3e953cde5993b831` Northwest Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ntcmn.edu/myntc/financial-aid/award-notice/ (sha256 9422cea6ec33)
- issues: residency_unknown
- checks: {"columns": 1, "components_per_semester": true, "components_reconcile": true, "rows": 7}
  - column:Tuition: 3250 ⟵ “Tuition | $ 3,250”
  - column:Fees: 244 ⟵ “Fees | $ 244”
  - column:Books course materials, supplies, equipment: 800 ⟵ “Books course materials, supplies, equipment | $ 800”
  - column:Housing and Food (Housing = $3871/sem) (Food = $2430/sem): 6301 ⟵ “Housing and Food (Housing = $3871/sem) (Food = $2430/sem) | $ 6,301”
  - column:Transportation: 650 ⟵ “Transportation | $ 650”
  - column:Miscellaneous personal expenses: 850 ⟵ “Miscellaneous personal expenses | $ 850”
  - column:Total Annual Budget (2 x $12,095): 24190 ⟵ “Total Annual Budget (2 x $12,095) | $ 24,190”
### `290379bd2b868b56` Northwestern Health Sciences University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nwhealth.edu/admissions/tuition-fees/radiologic-technology/ (sha256 c38c07238ebf)
- issues: conflicting_sources:https://www.nwhealth.edu/admissions/tuition-fees/functional-and-integrative-nutrition/,https://www.nwhealth.edu/admissions/tuition-fees/integrative-care/,https://www.nwhealth.edu/admissions/tuition-fees/radiation-therapy/
- checks: {"columns": 1, "rows": 3}
  - column:Tuition Per Trimester: 5390 ⟵ “Tuition Per Trimester | $5,390”
  - column:Application Fee: 50 ⟵ “Application Fee | $50”
  - column:University Fee (per trimester): 290 ⟵ “University Fee (per trimester) | $290”
### `4e852168f84c0221` Northwestern Health Sciences University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nwhealth.edu/admissions/tuition-fees/radiation-therapy/ (sha256 9d6602b9c48f)
- issues: components_do_not_reconcile, conflicting_sources:https://www.nwhealth.edu/admissions/tuition-fees/functional-and-integrative-nutrition/,https://www.nwhealth.edu/admissions/tuition-fees/integrative-care/,https://www.nwhealth.edu/admissions/tuition-fees/radiologic-technology/
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - column:Total required program credits: 79 ⟵ “Total required program credits | 79”
  - column:Tuition Per Trimester: 5304 ⟵ “Tuition Per Trimester | $5,304”
  - column:Application Fee: 50 ⟵ “Application Fee | $50”
  - column:University Fee (per on-campus trimester): 290 ⟵ “University Fee (per on-campus trimester) | $290”
  - column:University Fee (per online trimester): 175 ⟵ “University Fee (per online trimester) | $175”
  - column:VERT Licensing Fee (1x charge in T3): 1080 ⟵ “VERT Licensing Fee (1x charge in T3) | $1080”
### `5f88062201afe3ad` Northwestern Health Sciences University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nwhealth.edu/admissions/tuition-fees/functional-and-integrative-nutrition/ (sha256 0f227cf21df7)
- issues: components_do_not_reconcile, conflicting_sources:https://www.nwhealth.edu/admissions/tuition-fees/integrative-care/,https://www.nwhealth.edu/admissions/tuition-fees/radiation-therapy/,https://www.nwhealth.edu/admissions/tuition-fees/radiologic-technology/
- checks: {"columns": 1, "components_reconcile": false, "rows": 3}
  - column:Total Credits: 36 ⟵ “Total Credits | 36”
  - column:Tuition: 19620 ⟵ “Tuition | $19,620”
  - column:University Fee (per trimester): 190 ⟵ “University Fee (per trimester) | $190”
### `c825ae2213b52214` Northwestern Health Sciences University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nwhealth.edu/admissions/tuition-fees/integrative-care/ (sha256 bf839b988cba)
- issues: components_do_not_reconcile, conflicting_sources:https://www.nwhealth.edu/admissions/tuition-fees/functional-and-integrative-nutrition/,https://www.nwhealth.edu/admissions/tuition-fees/radiation-therapy/,https://www.nwhealth.edu/admissions/tuition-fees/radiologic-technology/
- checks: {"columns": 1, "components_reconcile": false, "rows": 3}
  - column:Total Credits: 30 ⟵ “Total Credits | 30”
  - column:Tuition: 16350 ⟵ “Tuition | $16,350”
  - column:University Fee (per trimester): 190 ⟵ “University Fee (per trimester) | $190”
### `6c709a33d0822211` Pine Technical & Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://pine.edu/wp-lib/wp-content/uploads/2024/04/FY24-SAP-Policy-and-Procedure-PTCC.pdf (sha256 a8717071eedb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Probation status The status of a student who has successfully appealed a satisfactory academic progress suspension and regained financial aid eligibility for one evaluation period, after which the student must either meet the college or university cumulative GPA and completion percentage standards, or successfully complete the requirements of an academic plan developed for that student by the coll”
  - sentence: sap_appeal ⟵ “The student must initiate the appeal by completing and submitting the SAP Appeal form.”
  - sentence: sap_appeal ⟵ “An appeal may be approved only if the PTCC Satisfactory Academic Progress Committee: 4 a) Has determined that the student should be able to meet SAP standards at the end of the next evaluation period; or b) Develops an academic plan with the student that, if followed, will ensure the student is able to meet SAP standards by a specific point in time.”
  - sentence: sap_appeal ⟵ “The initial consideration of appeals will be completed by the Satisfactory Academic Progress committee.”
  - sentence: sap_appeal ⟵ “The initial consideration of appeals will be completed by the Satisfactory Academic Progress committee.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will make a decision on the merits of the appeal and will notify students in writing (letter or email) with the results of the appeal. 2.”
### `bbb5bd277749cb01` Pine Technical & Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://pine.edu/paying-for-college/financial-aid/ (sha256 489568d6b0e3)
- issues: semantic_review_required, conflicting_sources:https://pine.edu/paying-for-college/understanding-your-financial-aid-award/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “It is our policy to select all students applying for a consideration of special circumstances for verification.”
### `c9604e057bcbaf8a` Pine Technical & Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://pine.edu/paying-for-college/financial-aid/ (sha256 489568d6b0e3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “If the student feels that the parent information is not relevant or the parents are unable to be located, the student may apply for a dependency override with proper documentation.”
  - sentence: dependency_override ⟵ “None of the following conditions, either singly or in combination, will qualify a student for a dependency override: Parents refuse to contribute to child’s education.”
### `e4d5a107392deb8d` Pine Technical & Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://pine.edu/paying-for-college/understanding-your-financial-aid-award/ (sha256 26579ff652a8)
- issues: semantic_review_required, conflicting_sources:https://pine.edu/paying-for-college/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Decreases in Income, Excessive Out-of-Pocket Expenses, and Unusual Circumstances Certain circumstances and costs can impact financial aid eligibility.”
### `449cd227135d879a` Pine Technical & Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://pine.edu/wp-lib/wp-content/uploads/2025/06/Tuition-and-Fee-Information-2025-2026-6-26-25-v2.pdf (sha256 e86123126667)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 14, "rows": 6}
  - column:Resident‐Rate Tuition: 181.92 ⟵ “Resident‐Rate Tuition | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:Student Activity/Life: 5.4 ⟵ “Student Activity/Life | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40”
  - column:Technology: 13.0 ⟵ “Technology | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00”
  - column:Statewide Student Assoc: 0.61 ⟵ “Statewide Student Assoc | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61”
  - column:Non‐Resident Rate: 181.92 ⟵ “Non‐Resident Rate | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:credit: 32.95 ⟵ “credit | $32.95”
  - column:Resident‐Rate Tuition: 216.07 ⟵ “Resident‐Rate Tuition | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:Student Activity/Life: 5.4 ⟵ “Student Activity/Life | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40”
  - column:Technology: 13.0 ⟵ “Technology | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00”
  - column:Statewide Student Assoc: 0.61 ⟵ “Statewide Student Assoc | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61”
  - column:Non‐Resident Rate: 216.07 ⟵ “Non‐Resident Rate | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:Resident‐Rate Tuition: 183.97 ⟵ “Resident‐Rate Tuition | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:Student Activity/Life: 5.4 ⟵ “Student Activity/Life | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40”
  - column:Technology: 13.0 ⟵ “Technology | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00”
  - column:Statewide Student Assoc: 0.61 ⟵ “Statewide Student Assoc | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61”
  - column:Non‐Resident Rate: 183.97 ⟵ “Non‐Resident Rate | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:Resident‐Rate Tuition: 219.28 ⟵ “Resident‐Rate Tuition | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:Student Activity/Life: 5.4 ⟵ “Student Activity/Life | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40”
  - column:Technology: 13.0 ⟵ “Technology | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00”
  - column:Statewide Student Assoc: 0.61 ⟵ “Statewide Student Assoc | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61 | $0.61”
  - column:Non‐Resident Rate: 219.28 ⟵ “Non‐Resident Rate | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:TUITION & FEES: 13 ⟵ “TUITION & FEES | FY2026 Base | CMAE | COCP | EMS | 13 | Welding WELD”
  - column:Resident‐Rate Tuition: 226.42 ⟵ “Resident‐Rate Tuition | $181.92 | $216.07 | $183.97 | $219.28 | $226.42 | $226.92 | $222.87 | $216.92 | $205.72 | $219.97 | $202.92 | $279.92 | $186.63 | $217.92”
  - column:Student Activity/Life: 5.4 ⟵ “Student Activity/Life | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40 | $5.40”
  - column:Technology: 13.0 ⟵ “Technology | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00 | $13.00”
  - … 47 more rows
### `f835a504e45eda0f` Pine Technical & Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://pine.edu/paying-for-college/cost-of-attendance/ (sha256 b4b473757a07)
- issues: ambiguous_year_labels, components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - column:Tuition and Fees: 6569 ⟵ “Tuition and Fees | $6,569”
  - column:Books and Supplies: 2500 ⟵ “Books and Supplies | $2,500”
  - column:Living Expenses (Food/Housing): 10401 ⟵ “Living Expenses (Food/Housing) | $10,401”
  - column:Transportation: 2200 ⟵ “Transportation | $2,200”
  - column:Personal Expenses: 7401 ⟵ “Personal Expenses | $7,401”
  - column:Loan Fees: 9 ⟵ “Loan Fees | $9”
  - column:Total: 29071 ⟵ “Total | $29,071”
### `f8e20e0ed03fbd82` Pine Technical & Community College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://pine.edu/admissions/college-credit-in-high-school/concurrent-enrollment-students/ (sha256 f8babe602e4c)
- issues: stale_year_label:2025-26
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa"], "tiers": 3}
  - eligibility_tier: 2.5 ⟵ “Have a high school GPA of 2.5 or higher, and”
  - eligibility_tier: 3.0 ⟵ “Have a high school GPA of 3.0 or higher for general education courses or a GPA of 2.5 or higher for career and technical education courses, and”
  - eligibility_tier: 3.0 ⟵ “Have a high school grade point average of 3.0 or higher for liberal arts and CTE courses, and”
  - college_gpa_to_continue: 2.0 ⟵ “PTCC and Federal and State law require you make satisfactory progress (SAP) towards a degree, diploma or certificate to attend the College and remain eligible to receive financial aid. To maintain good academic standing, you must maintain a 2.0 cumulative grade point average (GPA) and a 67% cumulati”
### `27c2e4ead059eb56` Ridgewater College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://ridgewater.edu/admission-aid/paying-for-college/special-and-unusual-circumstances/ (sha256 84cc710cc754)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://ridgewater.edu/student-services-activities/student-rights-responsibilities/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “There are two categories of unique situations: special and unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special Circumstances are financial situations that support a change to the Cost of Attendance or Student Aid Index (SAI) calculation.”
  - sentence: need_based_special_circumstances ⟵ “Submitting a Special or Unusual Circumstance request does not guarantee an adjustment will be made to your aid offer or dependency status.”
### `31d802a683ea0582` Ridgewater College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ridgewater.edu/student-services-activities/student-rights-responsibilities/satisfactory-academic-progress/ (sha256 dc2ad165d028)
- issues: semantic_review_required, conflicting_sources:https://ridgewater.edu/student-services-activities/student-rights-responsibilities/satisfactory-academic-progress/appeal/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeals To see how to appeal, please visit the SAP Appeal page.”
  - sentence: sap_appeal ⟵ “Probation Status Students who are suspended due to unsatisfactory academic progress (from this or any other Minnesota State institution) have the right to appeal based on an error of record or on extenuating/unusual circumstances.”
### `3aeab5cd700e67a3` Ridgewater College — appeals 2026-27 [new] (labeled_in_heading)
- source: https://ridgewater.edu/admission-aid/paying-for-college/cost-of-attendance/ (sha256 b1cad74c9d6d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “If you have expenses that are not taken into account in the standard budget, you may submit a Cost of Attendance Budget Increase Form.”
### `80e660a5eec9ffdf` Ridgewater College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ridgewater.edu/student-services-activities/student-rights-responsibilities/satisfactory-academic-progress/ (sha256 dc2ad165d028)
- issues: semantic_review_required, conflicting_sources:https://ridgewater.edu/admission-aid/paying-for-college/special-and-unusual-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of extenuating circumstances that may be considered for an appeal include, but are not limited to, death of a relative, illness, hospitalization, injury of the student, or other unusual circumstances the student believes should be given consideration.”
### `a071f03ff3b56bc5` Ridgewater College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ridgewater.edu/student-services-activities/student-rights-responsibilities/satisfactory-academic-progress/appeal/ (sha256 f6e49860182c)
- issues: semantic_review_required, conflicting_sources:https://ridgewater.edu/student-services-activities/student-rights-responsibilities/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “How to Complete and Submit Your SAP Suspension Appeal Step 1 Have all the following required documents ready to upload before you begin working on your SAP Suspension Appeal Form.”
  - sentence: sap_appeal ⟵ “Step 2 Once you have all your documents ready, submit your appeal by doing the following: Open the SAP Suspension Appeal Form.”
### `a174706554aae23b` Ridgewater College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://ridgewater.edu/admission-aid/paying-for-college/cost-of-attendance/ (sha256 b1cad74c9d6d)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 6700 ⟵ “Tuition & Fees | $3,350 | $3,350 | $6,700”
  - column:Books & Supplies: 1236 ⟵ “Books & Supplies | $618 | $618 | $1,236”
  - column:Housing & Food: 10874 ⟵ “Housing & Food | $5,437 | $5,437 | $10,874”
  - column:Transportation: 2646 ⟵ “Transportation | $1,323 | $1,323 | $2,646”
  - column:Miscellaneous Personal Expense: 2430 ⟵ “Miscellaneous Personal Expense | $1,215 | $1,215 | $2,430”
  - column:Loan Fees: 84 ⟵ “Loan Fees | $42 | $42 | $84”
  - column:Total: 23970 ⟵ “Total | $11,985 | $11,985 | $23,970”
### `c00c8d3bd5a17362` Ridgewater College — transfer_policies 2026-27 [new] (ambiguous_year_labels)
- source: https://ridgewater.edu/admission-aid/incoming-transfer-students/ (sha256 769459b25bb9)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Students must have earned a grade of C- or better for the credits to transfer.”
### `1e86dc2a5a96f78a` Riverland Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.riverland.edu/tuition-aid/financial-aid/forms-worksheets/2026-2027-application-for-professional-judgment-dependent-student/ (sha256 dd6921f65334)
- issues: semantic_review_required, conflicting_sources:https://www.riverland.edu/tuition-aid/financial-aid/forms-worksheets/2026-2027-application-for-professional-judgment-independent-student/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “2026-2027 Application for Professional Judgment- Dependent Student According to federal laws and regulations, a family’s 2024 income is used to assess financial need for the 2026-2027 school year.”
  - sentence: professional_judgment ⟵ “Note: Your professional judgment application will be returned if all requested information outlined is not provided.”
  - sentence: professional_judgment ⟵ “Turnaround time for professional judgment appeals is 2-4 weeks.”
### `4fa6ed8b71c733af` Riverland Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.riverland.edu/tuition-aid/financial-aid/forms-worksheets/2026-2027-application-for-professional-judgment-dependent-student/ (sha256 dd6921f65334)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “If a family’s 2025 or 2026 income is lower, due to special circumstances, a financial aid administrator may be able to use 2025 or 2026 income to assess financial need.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances, if accepted, may result in an increase in need-based loans, student employment, or in certain cases, additional grant assistance.”
  - sentence: need_based_special_circumstances ⟵ “SECTION 4: CHANGE IN INCOME All listed documents must be submitted.”
### `625631f1b584ad26` Riverland Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.riverland.edu/tuition-aid/financial-aid/sap/ (sha256 8336cfa800dc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Submit Your Appeal Complete the SAP Appeal Form Use the online form to submit your appeal.”
### `ac4017288da6d737` Riverland Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.riverland.edu/tuition-aid/financial-aid/forms-worksheets/2026-2027-application-for-professional-judgment-independent-student/ (sha256 44fc8baffac2)
- issues: semantic_review_required, conflicting_sources:https://www.riverland.edu/tuition-aid/financial-aid/forms-worksheets/2026-2027-application-for-professional-judgment-dependent-student/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “2026-2027 Application for Professional Judgment- Independent Student According to federal laws and regulations, a family’s 2024 income is used to assess financial need for the 2026-2027 school year.”
  - sentence: professional_judgment ⟵ “Note: Your professional judgment application will be returned if all requested information outlined is not provided.”
  - sentence: professional_judgment ⟵ “Turnaround time for professional judgment appeals is 2-4 weeks.”
### `5cfd53174b7c6332` Riverland Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.riverland.edu/tuition-aid/tuition/cost-of-attending-riverland/ (sha256 2aadcecc5199)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 7808.0 ⟵ “Tuition and Fees | $7,808.00”
  - column:Books, Supplies and Materials: 1600.0 ⟵ “Books, Supplies and Materials | $1,600.00”
  - column:Housing and Food *: 11020.0 ⟵ “Housing and Food * | $11,020.00”
  - column:Personal Expenses: 4500.0 ⟵ “Personal Expenses | $4,500.00”
  - column:Transportation: 3000.0 ⟵ “Transportation | $3,000.00”
  - column:Total Estimated Cost of Attendance: 27928.0 ⟵ “Total Estimated Cost of Attendance | $27,928.00”
### `04945e31eda8b0e0` Rochester Community and Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.rctc.edu/financialaid/forms/appeal-form-instructions/ (sha256 5020da25e364)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Your Suspension You may appeal your satisfactory academic progress (SAP) status if extenuating circumstances interfered with your ability to meet RCTC’s SAP standards.”
### `36cf189425e86e8b` Rochester Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rctc.edu/policies/education/grade-appeal/ (sha256 3c399894501d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Definitions Arbitrariness: The final class grade awarded represents a departure from accepted academic norms as to demonstrate that the instructor did not exercise proper professional judgment, or the instructor deviated from the evaluation criteria established by the grading policy described in the class syllabus.”
### `bcde952e44670f0f` Rochester Community and Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.rctc.edu/eservices/tuition/tuition-and-fees-table/ (sha256 b025de8eef1a)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 6}
  - column:Tuition and Fees: 6972.0 ⟵ “Tuition and Fees | $6,972.00”
  - column:Books, Supplies and Materials: 1800.0 ⟵ “Books, Supplies and Materials | $1,800.00”
  - column:Housing and Food: 9000.0 ⟵ “Housing and Food | $9,000.00”
  - column:Personal Expenses: 5584.0 ⟵ “Personal Expenses | $5,584.00”
  - column:Transportation: 2900.0 ⟵ “Transportation | $2,900.00”
  - column:Estimated Cost of Attendance: 26256.0 ⟵ “Estimated Cost of Attendance | $26,256.00”
### `94a8d3143c81ddf8` Rochester Community and Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.rctc.edu/academics/courses/advanced-placement/ (sha256 7d14e79d0e3e)
- issues: conflicting_sources:https://www.rctc.edu/academics/credit-for-prior-learning/
- checks: {"distinct_exams": 31, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | 3 | Elective”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | ART 1110”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Studio Art: 2-D Design | 3 | 3 | ART 1121”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Studio Art: 3-D Design | 3 | 3 | ART 1124”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art: Drawing | 3 | 3 | ART 1134”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIOL 1220”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 5 | MATH 1127”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 10 | MATH 1127 & 1128”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHEM 1127”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 8 | CHEM 1127 & 1128”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | 3 | CHIN 1001”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 3 | Elective”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 4 | ECON 2215”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 4 | ECON 2214”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language + Composition | 3 | 4 | ENGL 1117”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature + Composition | 3 | 8 | ENGL 1117 & 1118”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 3 | Elective”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 | HIST 1614”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language + Culture | 3 | 4 | FREN 1102”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | GEOG 1614”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 3 | MUSC 1001”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1 | 3 | 5 | PHYS 1117”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2 | 3 | 5 | PHYS 1118”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C Electricity & Magnetism | 3 | 5 | PHYS 1127”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C Mechanics | 3 | 5 | PHYS 1128”
  - … 7 more rows
### `ca8f5bbddbca7d83` Rochester Community and Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.rctc.edu/academics/credit-for-prior-learning/ (sha256 f8677db88ad3)
- issues: conflicting_sources:https://www.rctc.edu/academics/courses/advanced-placement/
- checks: {"distinct_exams": 29, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | ART 1110”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Studio Art: 2-D Design | 3 | 3 | ART 1121”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Studio Art: 3-D Design | 3 | 3 | ART 1124”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art: Drawing | 3 | 3 | ART 1134”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIOL 1220”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 5 | MATH 1127”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 10 | MATH 1127 & 1128”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHEM 1127”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 8 | CHEM 1127 & 1128”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | 3 | CHIN 1001”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 3 | elective”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 4 | ECON 2215”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 4 | ECON 2214”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language + Composition | 3 | 4 | ENGL 1117”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature + Composition | 3 | 8 | ENGL 1117 & 1118”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 3 | elective”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 | HIST 1614”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language + Culture | 3 | 4 | FREN 1102”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | GEOG 1614”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 3 | MUSC 1001”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1 | 3 | 5 | PHYS 1117”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2 | 3 | 5 | PHYS 1118”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C Electricity & Magnetism | 3 | 5 | PHYS 1127”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C Mechanics | 3 | 5 | PHYS 1128”
  - equivalencies[AP-PSYCHOLOGY|4]:  ⟵ “Psychology | 4 | 4 | PSYC 2618”
  - … 5 more rows
### `12095f8ace186444` Saint Cloud State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stcloudstate.edu/financialaid/policies/sap.aspx (sha256 b184cd63e375)
- issues: semantic_review_required, conflicting_sources:https://www.stcloudstate.edu/financialaid/cost-of-attendance.aspx,https://www.stcloudstate.edu/financialaid/default.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-appeal-process.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-faqs.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-progress-policy.aspx
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Related Information SAP Policy SAP Appeal Form Frequently Asked Questions SAP Appeal Deadlines A student's appeal must be submitted by the below date for consideration.”
  - sentence: sap_appeal ⟵ “Spring 2027 Satisfactory Academic Progress notifications will be sent out on May 14, 2027 Appeals are due by May 31, 2027.”
### `12eaf1b06eced310` Saint Cloud State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stcloudstate.edu/financialaid/policies/sap-appeal-process.aspx (sha256 3863fc1504e6)
- issues: semantic_review_required, conflicting_sources:https://www.stcloudstate.edu/financialaid/cost-of-attendance.aspx,https://www.stcloudstate.edu/financialaid/default.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-faqs.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-progress-policy.aspx,https://www.stcloudstate.edu/financialaid/policies/sap.aspx
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form | St.”
  - sentence: sap_appeal ⟵ “Financial Aid SAP Appeal Form Once logged into the appeal form, you will check the box "to have this appeal shared with the Financial Aid Office..." and then the second line will appear.”
### `369ae62b2d6d7fe2` Saint Cloud State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stcloudstate.edu/financialaid/policies/sap-faqs.aspx (sha256 d16aa2ac72b0)
- issues: semantic_review_required, conflicting_sources:https://www.stcloudstate.edu/financialaid/cost-of-attendance.aspx,https://www.stcloudstate.edu/financialaid/default.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-appeal-process.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-progress-policy.aspx,https://www.stcloudstate.edu/financialaid/policies/sap.aspx
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Cloud State University Financial Aid Office Types of Aid Financial Aid Process Forms One Big Beautiful Bill Changes Policies Satisfactory Academic Progress Satisfactory Academic Progress Appeal Process Satisfactory Academic Progress Appeal Form Satisfactory Academic Progress FAQs Cost of Attendance Professional Judgement Student Employment Accelerated Online Programs Mission and Vision Contact Us ”
  - sentence: sap_appeal ⟵ “Financial Aid Appeal Form Is there a deadline to submit a SAP appeal?”
  - sentence: sap_appeal ⟵ “Yes, please see SAP appeal deadlines.”
  - sentence: sap_appeal ⟵ “Students who are not meeting SAP and do not meet the stated deadline will not have their financial aid SAP appeal considered for the current term.”
  - sentence: sap_appeal ⟵ “If I decide not to appeal my SAP status or if my appeal is denied, how can I pay my bill?”
### `3c1fad285760ba7d` Saint Cloud State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stcloudstate.edu/financialaid/cost-of-attendance.aspx (sha256 d9be5373f0ab)
- issues: semantic_review_required, conflicting_sources:https://www.stcloudstate.edu/financialaid/default.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-appeal-process.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-faqs.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-progress-policy.aspx,https://www.stcloudstate.edu/financialaid/policies/sap.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Cloud State University Financial Aid Office Types of Aid Financial Aid Process Forms One Big Beautiful Bill Changes Policies Satisfactory Academic Progress Satisfactory Academic Progress Appeal Process Satisfactory Academic Progress Appeal Form Satisfactory Academic Progress FAQs Cost of Attendance Professional Judgement Student Employment Accelerated Online Programs Mission and Vision Contact Us ”
### `48ee75e3fedc05d6` Saint Cloud State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stcloudstate.edu/financialaid/policies/sap-progress-policy.aspx (sha256 e452349bd4d7)
- issues: semantic_review_required, conflicting_sources:https://www.stcloudstate.edu/financialaid/cost-of-attendance.aspx,https://www.stcloudstate.edu/financialaid/default.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-appeal-process.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-faqs.aspx,https://www.stcloudstate.edu/financialaid/policies/sap.aspx
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Process | St.”
  - sentence: sap_appeal ⟵ “Appeals If a student’s financial aid eligibility has been suspended due to not maintaining satisfactory academic progress, the student has the right to appeal based on the following: death of a relative an injury, illness, or hospitalization of the student a student who transferred credits to SCSU that were earned through military service which are not applicable to any specific course or degree r”
### `d68a086a3b23d614` Saint Cloud State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.stcloudstate.edu/financialaid/default.aspx (sha256 0153e37b473a)
- issues: semantic_review_required, conflicting_sources:https://www.stcloudstate.edu/financialaid/cost-of-attendance.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-appeal-process.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-faqs.aspx,https://www.stcloudstate.edu/financialaid/policies/sap-progress-policy.aspx,https://www.stcloudstate.edu/financialaid/policies/sap.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Cloud State University Financial Aid Office Types of Aid Financial Aid Process Forms One Big Beautiful Bill Changes Policies Satisfactory Academic Progress Satisfactory Academic Progress Appeal Process Satisfactory Academic Progress Appeal Form Satisfactory Academic Progress FAQs Cost of Attendance Professional Judgement Student Employment Accelerated Online Programs Mission and Vision Contact Us ”
### `63dd17247c56ad6d` Saint Cloud State University — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.stcloudstate.edu/financialaid/cost-of-attendance.aspx (sha256 d9be5373f0ab)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 9}
  - column:Tuition: 21132 ⟵ “Tuition | $4,980 | $9,960 | $21,132”
  - column:Fees: 1496 ⟵ “Fees | $748 | $1,496 | $1,496”
  - column:Tuition and Fees Total: 11456 ⟵ “Tuition and Fees Total | $5,728 | $11,456 | $11,456”
  - column:Housing and Meal Plan: 11306 ⟵ “Housing and Meal Plan | $5,653 | $11,306 | $11,306”
  - column:Books and Supplies: 1400 ⟵ “Books and Supplies | $700 | $1,400 | $1,400”
  - column:Transportation: 2088 ⟵ “Transportation | $783 | $1,566 | $2,088”
  - column:Personal Expenses: 2592 ⟵ “Personal Expenses | $1,296 | $2,592 | $2,592”
  - column:Federal Loan Fees (average): 92 ⟵ “Federal Loan Fees (average) | $46 | $92 | $92”
  - column:Total:: 28934 ⟵ “Total: | $14,206 | $28,412 | $28,934”
### `ma427e71f48faca1` Saint Cloud State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.stcloudstate.edu/academics/minnesota-transfer-curriculum (sha256 38a2a006a74b)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “All credits earned with a grade of "C-" or higher from a regionally accredited university or college-level institution are considered for credit transfer.”
  - min_grade: C ⟵ “All credits earned with a grade of "C" or higher from a regionally accredited university or college-level institution are considered for credit transfer.”
### `2f4d12f1a0d52064` Saint Johns University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/ (sha256 23ed8c5fce04)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/,https://www.csbsju.edu/financialaid/wp-content/uploads/sites/76/2025/09/26-27-Special-Circumstances-Form-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances We recognize that the FAFSA does not always provide a clear picture of your family’s financial situation.”
  - sentence: need_based_special_circumstances ⟵ “You may complete the CSB+SJU Special Circumstances Form to report family financial information that might impact your aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Circumstances that may be considered include the following: Private Elementary/Secondary School Tuition Loss of Employment/Reduced Wages High Medical/Dental Expenses Marital Separation/Divorce One-Time Income Educational Loan Payments Please note that initiating a special circumstance request may result in your FAFSA being selected for verification.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances forms will be reviewed within 10 working days of receipt.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances Form Secure Upload Verification Information The verification process aims to ensure the effectiveness of the federal student aid programs.”
### `4b3f4fdbdb212347` Saint Johns University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/ (sha256 8766a489e25a)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/,https://www.csbsju.edu/financialaid/wp-content/uploads/sites/76/2025/09/26-27-Special-Circumstances-Form-Fillable.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances We recognize that the FAFSA does not always provide a clear picture of your family’s financial situation.”
  - sentence: need_based_special_circumstances ⟵ “You may complete the CSB+SJU Special Circumstances Form to report family financial information that might impact your aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Circumstances that may be considered include the following: Private Elementary/Secondary School Tuition Loss of Employment/Reduced Wages High Medical/Dental Expenses Marital Separation/Divorce One-Time Income Educational Loan Payments Please note that initiating a special circumstance request may result in your FAFSA being selected for verification.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances forms will be reviewed within 10 working days of receipt.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances Form Secure Upload Verification Information The verification process aims to ensure the effectiveness of the federal student aid programs.”
### `9e12e99d32fd39fe` Saint Johns University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.csbsju.edu/financialaid/wp-content/uploads/sites/76/2025/09/26-27-Special-Circumstances-Form-Fillable.pdf (sha256 a94da76e48ea)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/,https://www.csbsju.edu/admission/cost-aid-scholarships/applying-for-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances Application STUDENT INFORMATION Last Name: First Name: M.I.”
  - sentence: need_based_special_circumstances ⟵ “Check ☐ SPECIAL CIRCUMSTANCE REQUIRED DOCUMENTATION Reason Private Elementary/Secondary School  Tuition statement OR letter from the school indicating tuition charges Tuition minus financial aid and/or discounts for child(ren) at that school.”
  - sentence: need_based_special_circumstances ⟵ “Consumer debt is not eligible for consideration under special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Check SPECIAL CIRCUMSTANCE REQUIRED DOCUMENTATION Reason Loss of Employment/Reduced Wages • Statement explaining the reason for loss of income, including dates of change • Signed copy of 2024 federal tax return Financial aid eligibility for 2026-27 is based • Complete Estimated Income Chart (below).”
### `53dd723c10eee7e8` Saint Johns University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/ (sha256 f47c42e6ae35)
- issues: arrangement_unlabeled, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/financialaid/costs/,https://www.csbsju.edu/student-accounts/educational-costs-3/
- checks: {"columns": 2, "rows": 4}
  - column:Tuition and fees:: 59782 ⟵ “Tuition and fees: | $59,782 | $59,782”
  - column:Housing and food:: 13350 ⟵ “Housing and food: | $13,350 | $13,350”
  - column:Estimated book costs for the year:: 1000 ⟵ “Estimated book costs for the year: | $1,000 | $1,000”
  - column:Personal/miscellaneous expenses: 1500 ⟵ “Personal/miscellaneous expenses | $1,500 | $1,500”
  - column:Tuition and fees:: 59782 ⟵ “Tuition and fees: | $59,782 | $59,782”
  - column:Housing and food:: 13350 ⟵ “Housing and food: | $13,350 | $13,350”
  - column:Estimated book costs for the year:: 1000 ⟵ “Estimated book costs for the year: | $1,000 | $1,000”
  - column:Personal/miscellaneous expenses: 1500 ⟵ “Personal/miscellaneous expenses | $1,500 | $1,500”
### `58ce6d8c3b55f975` Saint Johns University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/student-accounts/educational-costs-3/ (sha256 c6971da6c88c)
- issues: shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/financialaid/costs/
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 58430 ⟵ “Tuition | $29,215 | $58,430”
  - column:Fees: 1352 ⟵ “Fees | $676 | $1,352”
  - column:Meals: 6820 ⟵ “Meals | $3,410 | $6,820”
  - column:Books: 1000 ⟵ “Books | $500 | $1,000”
### `82f0054c0ab05bac` Saint Johns University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/ (sha256 7fc053214fd6)
- issues: arrangement_unlabeled, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/financialaid/costs/,https://www.csbsju.edu/student-accounts/educational-costs-3/
- checks: {"columns": 2, "rows": 4}
  - column:Tuition and fees:: 59782 ⟵ “Tuition and fees: | $59,782 | $59,782”
  - column:Housing and food:: 13350 ⟵ “Housing and food: | $13,350 | $13,350”
  - column:Estimated book costs for the year:: 1000 ⟵ “Estimated book costs for the year: | $1,000 | $1,000”
  - column:Personal/miscellaneous expenses: 1500 ⟵ “Personal/miscellaneous expenses | $1,500 | $1,500”
  - column:Tuition and fees:: 59782 ⟵ “Tuition and fees: | $59,782 | $59,782”
  - column:Housing and food:: 13350 ⟵ “Housing and food: | $13,350 | $13,350”
  - column:Estimated book costs for the year:: 1000 ⟵ “Estimated book costs for the year: | $1,000 | $1,000”
  - column:Personal/miscellaneous expenses: 1500 ⟵ “Personal/miscellaneous expenses | $1,500 | $1,500”
### `d6f72d3c2e26eb7d` Saint Johns University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/financialaid/costs/ (sha256 b2aa9ce14a39)
- issues: shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/admission/cost-aid-scholarships/tuition-and-costs/,https://www.csbsju.edu/student-accounts/educational-costs-3/
- checks: {"columns": 1, "rows": 3}
  - column:Full-Time Tuition and Required Fees: 59782 ⟵ “Full-Time Tuition and Required Fees | $59,782”
  - column:On Campus Housing & Food (First Year): 13350 ⟵ “On Campus Housing & Food (First Year) | $13,350”
  - column:On Campus Housing & Food (Returning}: 14340 ⟵ “On Campus Housing & Food (Returning} | $14,340”
### `d7a0ae8093d381d8` Saint Johns University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.csbsju.edu/student-accounts/educational-costs-3/ (sha256 c6971da6c88c)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 56450 ⟵ “Tuition | $28,225 | $56,450”
  - column:Fees: 1248 ⟵ “Fees | $624 | $1,248”
  - column:Meals: 6620 ⟵ “Meals | $3,310 | $6,620”
  - column:Books: 1000 ⟵ “Books | $500 | $1,000”
### `11395d100cefad6f` Saint Johns University — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf (sha256 0b27fbdaee02)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf
- checks: {"distinct_exams": 30, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 100                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Lang & Composition (f)         5     ENGL 211                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 101                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142                                                          4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152                                                          4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100                                                          4              HE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography (s)                   4-5 COLG 105ZA (Elective credit only)                                 4”
  - … 6 more rows
### `24562a023ddd2421` Saint Johns University — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf (sha256 eb32d45291f7)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf
- checks: {"distinct_exams": 11, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|60]:  ⟵ “Financial Accounting                                       60    ACFN 111                                     4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|60]:  ⟵ “Introductory Business Law                                  60    ACFN 335                                     2              SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|60]:  ⟵ “Principles of Management                                   60    GBUS 202                                     4”
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4              HE”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOAN 111                                     4             SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4            SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4            SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8            SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123                                     4           NW ,QR”
### `47180223b2fd7e4c` Saint Johns University — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf (sha256 7cd8d78a1578)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf
- checks: {"distinct_exams": 11, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|60]:  ⟵ “Financial Accounting                                       60    ACFN 111                                     4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|60]:  ⟵ “Introductory Business Law                                  60    ACFN 335                                     2              SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|60]:  ⟵ “Principles of Management                                   60    GBUS 202                                     4”
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4              HE”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOAN 111                                     4             SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4            SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4            SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8            SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123                                     4           NW ,QR”
### `6cb546f84614361e` Saint Johns University — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf (sha256 0d5b98f88b92)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf
- checks: {"distinct_exams": 30, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 100                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang & Composition (f)        4-5    ENGL 211                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 101                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142                                                          4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152                                                          4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100                                                          4              HE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography (s)                   4-5 COLG 105ZA (Elective credit only)                                 4”
  - … 6 more rows
### `8514e5d7f56e759f` Saint Johns University — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf (sha256 c2c586dc1d1c)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf
- checks: {"distinct_exams": 11, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|60]:  ⟵ “Financial Accounting                                       60    ACFN 111                                     4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|60]:  ⟵ “Introductory Business Law                                  60    ACFN 335                                     2             SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|60]:  ⟵ “Principles of Management                                   60    GBUS 202                                     4”
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 101                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOCI 111                                     4            SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8           SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123                                     4             NW”
### `b70afbf0c941cb5c` Saint Johns University — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf (sha256 c259de2a1fb7)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf
- checks: {"distinct_exams": 30, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 101                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Lang & Composition (f)         5     ENGL 211                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 122                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142Z                                                         4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152Z                                                         4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100Z                                                         4              HE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography (s)                   4-5 COLG 105ZA (Elective credit only)                                 4”
  - … 6 more rows
### `c96f8ebe3b1b59fe` Saint Johns University — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf (sha256 ec34eb51a7d1)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf
- checks: {"distinct_exams": 8, "equivalencies": 9, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOCI 111                                     4            SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8           SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123 (NS)                                4             NW”
### `cebfdc2e6861ac0b` Saint Johns University — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2024-2025.pdf (sha256 b77fadd5b31c)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/12/CLEP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2026-2027.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/05/CLEP_AdmissionYear_2027-2028.pdf
- checks: {"distinct_exams": 8, "equivalencies": 9, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|53]:  ⟵ “American Literature                                        53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature                        53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-ENGLISH-LITERATURE|53]:  ⟵ “English Literature                                         53    ENGL 122                                     4              HE”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|60]:  ⟵ “History of the United States II: 1865 to Present           60    HIST 101                                     4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|67]:  ⟵ “Introductory Sociology                                     67    SOCI 111                                     4            SW”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                               50    ECON 100                                     4           SW, QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Macro & Microeconomics (s)                                 50    50 on both tests ECON 100 & 111              8           SW, QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                                                  63    CHEM 123 (NS)                                4             NW”
### `d2541cb4184b2051` Saint Johns University — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf (sha256 0b5232ea2bbb)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf
- checks: {"distinct_exams": 31, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 100                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-CYBERSECURITY|4-5]:  ⟵ “Computer Science Cybersecurity        4-5    CSCI 300AZ Cybersecurity                                       2”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4-5]:  ⟵ “English Lang & Composition (f)        4-5    ENGL 105                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 101                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142                                                          4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152                                                          4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100                                                          4              HE”
  - … 7 more rows
### `ebd069c1b8b26497` Saint Johns University — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2024-2025.pdf (sha256 5b5cbfd01846)
- issues: ambiguous_year_labels, shared_site_attribution_review, conflicting_sources:https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2023-2024.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2025/10/AP_AdmissionYear_2025-2026.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/06/AP_AdmissionYear_2026_202768.pdf,https://www.csbsju.edu/student-records/wp-content/uploads/sites/106/2026/09/AP_AdmissionYear_2027-2028-v2.pdf
- checks: {"distinct_exams": 30, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4-5]:  ⟵ “Art History (f)                       4-5                                                                   4              AE”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Studio Art Drawing (f)                4-5    ART 214                                                        4              AE”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 2-D Design (f)             4-5    ART 118                                                        4              AE”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “Studio Art 3-D Design (f)             4-5                                                                   4              AE”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (f)                           4-5    BIOL 101                                                       4            NW, QR”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus                           4-5    MATH 115                                                       2”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB (f)                       4-5    MATH 119                                                       4              AS”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4-5]:  ⟵ “Computer Science A (f)                4-5    CSCI 160                                                       4            AS, QR”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles (f)       4-5    CSCI 150                                                       4            AS, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macroeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MICROECONOMICS|4-5]:  ⟵ “Microeconomics (s)                    4-5    ECON 100                                                       4            SW, QR”
  - equivalencies[AP-MACROECONOMICS|4-5]:  ⟵ “Macro & Microeconomics (s)            4-5    4-5 on both tests ECON 100 & 111                               8            SW, QR”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Lang & Composition (f)         5     ENGL 211                                                       4              HE”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Comp. (f)        4-5    ENGL 122                                                       4              HE”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4-5]:  ⟵ “Environmental Science (s)             4-5    ENVR 175                                                       4              NW”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Chinese Language & Culture (f)        4-5    CHIN 212                                                       4             LANG”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language/Culture (f)            5     FREN 311                                                       4             LANG”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language (f)                    5     GERM 300                                                       4             LANG”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4-5]:  ⟵ “Japanese Language & Culture (f)       4-5    JAPN 212                                                       4             LANG”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin: Vergil or Literature (f)        5     LATN 211                                                       4             LANG”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “U.S. Government & Politics (s)        4-5 POLS 111                                                          4              SW”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History (f)                  4-5 HIST 142                                                          4              HE”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History (f)             4-5 HIST 152                                                          4              HE”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History (f)                     4-5 HIST 100                                                          4              HE”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography (s)                   4-5 COLG 105ZA (Elective credit only)                                 4”
  - … 6 more rows
### `1261cc6272ad10b5` Saint Mary's University of Minnesota — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.smumn.edu/admissions/undergraduate/financial-aid/forms-and-policies/ (sha256 ee6dac6076fa)
- issues: semantic_review_required, conflicting_sources:https://www.smumn.edu/admissions/fafsa-verification/,https://www.smumn.edu/wp-content/uploads/2025/12/5901_SpecCirc_DependentStudent_26-27_ONLINE.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Signed and dated forms should be sent or faxed to: Office of the Registrar Saint Mary’s University of Minnesota 700 Terrace Heights #37 Winona, MN 55987-1399 Fax: 507–457–6698 Special Circumstances If you or your family’s financial circumstances have changed since filing your FAFSA, please fill out the following form, and submit it to the financial aid office.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances-Dependent (PDF) Exit Counseling The Federal Stafford Loan and Federal Direct Loan Exit Counseling is used when a student has borrowed in a federal loan program and has dropped below half time status (please see definition listed below).”
### `2df07caf385e238d` Saint Mary's University of Minnesota — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.smumn.edu/admissions/fafsa-verification/ (sha256 105f31355f2a)
- issues: semantic_review_required, conflicting_sources:https://www.smumn.edu/admissions/undergraduate/financial-aid/forms-and-policies/,https://www.smumn.edu/wp-content/uploads/2025/12/5901_SpecCirc_DependentStudent_26-27_ONLINE.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “For verification purposes, the only documentation allowed in lieu of IRS Data Retrieval with unchanged data is an IRS Tax Return Transcript, unless there is an allowed special circumstance.”
### `3dcb7b4223fa3c3c` Saint Mary's University of Minnesota — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.smumn.edu/wp-content/uploads/2025/12/5901_SpecCirc_DependentStudent_26-27_ONLINE.pdf (sha256 ddf451351433)
- issues: semantic_review_required, conflicting_sources:https://www.smumn.edu/admissions/fafsa-verification/,https://www.smumn.edu/admissions/undergraduate/financial-aid/forms-and-policies/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCES 2026-2027 (DEPENDENT STUDENT) Student Name: __________________________________________________ SMUMN ID: _______________________ Parent Name(s): ___________________________________________________________________________________ Parent Email Address: ______________________________________________________________________________ Parent Daytime Phone Number: ___________________”
  - sentence: need_based_special_circumstances ⟵ “Imported information from the IRS in the FAFSA does not exempt you from submitting the documentation listed below, unless specifically stated.*  Letter or email explaining the special circumstances situation and the outcome you are hoping for with this appeal.  Documentation listed below that best fits your circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Parent 1: $_________________  Documentation of death Parent 2: $_________________  Documentation of year-to-date  Letter from previous employer stating earnings for deceased parent last date of employment  Severance information, if applicable  Individuals with self-employment, or other non-W2 income from the tax return, need to document their financial changes in the special circumstance lett”
### `c58038f82b30fea8` Saint Mary's University of Minnesota — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.smumn.edu/admissions/undergraduate/financial-aid/ (sha256 f3f467542706)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “You may be able to request a professional judgment review of your FAFSA to see if additional aid is availableor see the Special Financial Circumstances form on our Forms and Policies page.”
### `c8d274e4e26697d5` Saint Mary's University of Minnesota — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smumn.edu/admissions/undergraduate/tuition-fees/ (sha256 fe13246a68d0)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "rows": 15}
  - column:Tuition: 23840 ⟵ “Tuition | Per semester | $23,840 | $47,680 / year”
  - column:Housing*: 3345 ⟵ “Housing* | Standard room | $3,345 | $6,690 / year”
  - column:Food: 2625 ⟵ “Food | Meal plan | $2,625 | $5,250 / year”
  - column:Physician Assistant (PA) Program Tuition: 26225 ⟵ “Physician Assistant (PA) Program Tuition | Per semester | $26,225 | $52,450 / year”
  - column:Tuition (2): 1590 ⟵ “Tuition | $1,590 per credit | $1,590 | $9,540 for 6 credits”
  - column:Instruction Fee: 1590 ⟵ “Instruction Fee | Extra coursework | $1,590 | Per credit”
  - column:Foreign Study Fee: 1050 ⟵ “Foreign Study Fee | London / Other locations | $1,050 | Per trip”
  - column:Late Registration: 50 ⟵ “Late Registration | Missed deadline | $50 | Per instance”
  - column:NSF / Returned Payment: 20 ⟵ “NSF / Returned Payment | Check or ACH | $20 | Per return”
  - column:PACC: 100 ⟵ “PACC | Program for advanced college credit | $100 | Per credit”
  - column:PSEO: 0 ⟵ “PSEO | Postsecondary enrollment option | $0 | Per credit”
  - column:Gilmore Creek, Residencia Santiago Miller: 200 ⟵ “Gilmore Creek, Residencia Santiago Miller | Additional charge | $200 | Per year”
  - column:Bishops, LaSalle Hall, Hillside, Brother Leopold (Double Suites), Saint Yon’s (Doubles): 400 ⟵ “Bishops, LaSalle Hall, Hillside, Brother Leopold (Double Suites), Saint Yon’s (Doubles) | Additional charge | $400 | Per year”
  - column:Brother William, Brother Leopold (Singles, Single Suites, Double/Mixed Apartments), Saint Yon’s (Singles, Single Suites, Mixed Apartments): 600 ⟵ “Brother William, Brother Leopold (Singles, Single Suites, Double/Mixed Apartments), Saint Yon’s (Singles, Single Suites, Mixed Apartments) | Additional charge | $600 | Per year”
  - column:Brother Leopold (Single Apartments), Saint Yon’s (Single Apartments): 800 ⟵ “Brother Leopold (Single Apartments), Saint Yon’s (Single Apartments) | Additional charge | $800 | Per year”
  - column:Loan Fees**: 48 ⟵ “Loan Fees** | If loans used | — | $48”
### `0039af3098bc6c9a` Saint Paul College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.saintpaul.edu/admissions/forms/ (sha256 73bcc9f4eb01)
- issues: semantic_review_required, conflicting_sources:https://www.saintpaul.edu/admissions/financial-aid/,https://www.saintpaul.edu/admissions/how-to-pay-for-college/,https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Special-Cir-Income-Adjust.pdf,https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Unusial-Cir-DO-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgement Appeal – Unusual Circumstances 2026 – 2027 Professional Judgement Appeal – Unusual Circumstances Income Adjustment Appeal This appeal is for when a student’s current income (and/or parent’s income for dependent students) is significantly lower than the income reported on the FAFSA from circumstances outside their control.”
  - sentence: professional_judgment ⟵ “Professional Judgement Appeal – Special Circumstances Income Adjustment 2026 – 2027 Professional Judgement Appeal – Special Circumstances Income Adjustment Loan Adjustment Request Submit an increase to a loan request, reduce a future loan disbursement, or reinstate previously canceled loans.”
### `40cf275788cc522c` Saint Paul College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.saintpaul.edu/wp-content/uploads/2024/07/2024-2025_PJ-Unusual-Circumstance.pdf (sha256 a29929a7efd0)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Professional Judgement Appeal - STUDENT ID #: Unusual Circumstances Student Information/Resource Statement 2024 - 2025 Academic Year DISCLAIMER: CONTENT WARNING FOR POTENTIALLY TRAUMATIC MATERIAL We encourage you to approach this content with caution.”
  - sentence: professional_judgment ⟵ “Student Name: Student ID# Last First MI The Professional Judgement Appeal - Unusual Circumstances process is used to address on a case-by-case basis a student who claims to be independent but does not meet the federal criteria.”
  - sentence: professional_judgment ⟵ “All decisions on dependency overrides are made based on Professional Judgment by the Financial Aid Office at Saint Paul College.”
  - sentence: professional_judgment ⟵ “Professional Judgement STEP 3 Personal Supporting Letter (Required) Appeal - Unusual One original letter from someone who can verify their first- hand knowledge of the students special circumstances.”
### `5f0a19b6efd2b81e` Saint Paul College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Special-Cir-Income-Adjust.pdf (sha256 e738f8bc8ef9)
- issues: semantic_review_required, conflicting_sources:https://www.saintpaul.edu/admissions/financial-aid/,https://www.saintpaul.edu/admissions/forms/,https://www.saintpaul.edu/admissions/how-to-pay-for-college/,https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Unusial-Cir-DO-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgement Appeal Student ID # Special Circumstances Income Adjustment 2026 - 2027 Academic Year Please print clearly.”
### `650bad274b1672a7` Saint Paul College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.saintpaul.edu/admissions/how-to-pay-for-college/ (sha256 4e28f61a3658)
- issues: semantic_review_required, conflicting_sources:https://www.saintpaul.edu/admissions/financial-aid/,https://www.saintpaul.edu/admissions/forms/,https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Special-Cir-Income-Adjust.pdf,https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Unusial-Cir-DO-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If a student has unusual expenses that may affect his or her ability to pay for school, the student should complete the Professional Judgement Appeal – Special Circumstances Income Adjustment.”
  - sentence: professional_judgment ⟵ “Professional Judgement Appeal – Special Circumstances Income Adjustment What is financial need?”
### `8021a85a67e0cb99` Saint Paul College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Unusial-Cir-DO-Appeal.pdf (sha256 a88a0b918191)
- issues: semantic_review_required, conflicting_sources:https://www.saintpaul.edu/admissions/financial-aid/,https://www.saintpaul.edu/admissions/forms/,https://www.saintpaul.edu/admissions/how-to-pay-for-college/,https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Special-Cir-Income-Adjust.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Professional Judgement Appeal - Student ID # Unusual Circumstances Student Information/Resource Statement 2026 - 2027 Academic Year DISCLAIMER: CONTENT WARNING FOR POTENTIALLY TRAUMATIC MATERIAL We encourage you to approach this content with caution.”
  - sentence: professional_judgment ⟵ “Student Name: Student ID# Last First MI The Professional Judgement Appeal - Unusual Circumstances process is used to address on a case-by-case basis a student who claims to be independent but does not meet the federal criteria.”
  - sentence: professional_judgment ⟵ “All decisions on dependency overrides are made based on Professional Judgment by the Financial Aid Office at Saint Paul College.”
  - sentence: professional_judgment ⟵ “Professional Judgement STEP 3 Personal Supporting Letter (Required) Appeal - Unusual One original letter from someone who can verify their first- Circumstances hand knowledge of the students special circumstances.”
### `81bc15c6f36b7340` Saint Paul College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.saintpaul.edu/admissions/financial-aid/ (sha256 52915a9b90c5)
- issues: semantic_review_required, conflicting_sources:https://www.saintpaul.edu/admissions/forms/,https://www.saintpaul.edu/admissions/how-to-pay-for-college/,https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Special-Cir-Income-Adjust.pdf,https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Unusial-Cir-DO-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If a student has unusual expenses that may affect his or her ability to pay for school, the student should complete the Professional Judgement Appeal – Special Circumstances Income Adjustment.”
  - sentence: professional_judgment ⟵ “Professional Judgement Appeal – Special Circumstances Income Adjustment What is financial need?”
### `b0d2bad5e900f2a0` Saint Paul College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.saintpaul.edu/admissions/forms/ (sha256 73bcc9f4eb01)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Consortium Agreement eForm Dependency Override Appeal This appeal is used when a dependent student doesn’t meet the federal “independent” status criteria on their FAFSA application but would like their unique circumstances reviewed to be considered an independent student for financial aid purposes.”
### `be6bfa47407a4025` Saint Paul College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.saintpaul.edu/wp-content/uploads/2026/04/2026-2027_PJ-Special-Cir-Income-Adjust.pdf (sha256 e738f8bc8ef9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Student Name: Tech ID#: Last First Street Address: City: State: Zip: Phone: Student Email: @my.saintpaul.edu Saint Paul College recognizes that Federal Student Aid is based on annual gross income from two previous tax years and special circumstances may occur after the FAFSA application was completed.”
  - sentence: need_based_special_circumstances ⟵ “If you, your spouse or parent(s) have experienced a significant decrease in income since 2024 due to a special circumstance, you may be eligible for an income adjustment to your FAFSA.”
### `e3ebec6c7e14af1d` Saint Paul College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.saintpaul.edu/admissions/forms/ (sha256 73bcc9f4eb01)
- issues: semantic_review_required, conflicting_sources:https://www.saintpaul.edu/student-services/appealing-academic-suspension/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Release of Information eForm Satisfactory Academic Progress (SAP) Appeal eForm Submit this eform to appeal your academic and/or financial aid suspension.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal eForm Transfer Evaluation Appeal Form Students may dispute transfer decisions through an appeal process by logging into your eServices account (choose Academic Records, then Transfer Review, then Add Request). eServices Tuition Appeal eForm Submit this eForm to request to have courses dropped after the drop deadline or to request to have courses withdraw”
  - sentence: sap_appeal ⟵ “Academic Probation Agreement eForm Appeal Academic/Financial Aid Suspension – Satisfactory Academic Progress (SAP) Appeal eForm Submit this eform to appeal your academic and/or financial aid suspension.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal eForm Third Attempt Request eForm Submit this eform to request to register for a course for a third time.”
### `f9319396b5d9debd` Saint Paul College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.saintpaul.edu/student-services/appealing-academic-suspension/ (sha256 a8f01feb2eab)
- issues: semantic_review_required, conflicting_sources:https://www.saintpaul.edu/admissions/forms/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Appealing due to catastrophic extenuating circumstances Students who believe they failed to achieve satisfactory academic progress due to extenuating circumstances may file an appeal prior to taking the required two terms off.”
  - sentence: sap_appeal ⟵ “The student must submit the Satisfactory Academic Progress (SAP) Appeal eForm in order to be considered for reinstatement, even after sitting out the required two terms following suspension.”
  - sentence: sap_appeal ⟵ “Students who have served their suspension period must appeal for reinstatement by submitting the required suspension appeal paperwork along with a letter detailing the following: What led to the academic suspension How your life circumstances have changed to support your efforts to be successful in school What you will do differently to ensure academic success if your appeal is granted Satisfactor”
  - sentence: sap_appeal ⟵ “The student must submit the Satisfactory Academic Progress (SAP) Appeal eForm in order to be considered for reinstatement, even after sitting out the required two terms following suspension.”
  - sentence: sap_appeal ⟵ “Students seeking admission to Saint Paul College who have attended another college or university and do not meet Saint Paul College’s Satisfactory Academic Progress Standards must appeal for admission.”
### `4e6c5b2f70dd3503` Saint Paul College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.saintpaul.edu/admissions/financial-aid/award-information/ (sha256 c2ce96b26c52)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 6077 ⟵ “Tuition | $3,038 | $3,038 | $6,077”
  - column:Fees: 860 ⟵ “Fees | $430 | $430 | $860”
  - column:Books/Supplies: 1200 ⟵ “Books/Supplies | $600 | $600 | $1,200”
  - column:Room/Board: 10396 ⟵ “Room/Board | $5,198 | $5,198 | $10,396”
  - column:Personal/Miscellaneous Expenses: 6426 ⟵ “Personal/Miscellaneous Expenses | $3,213 | $3,213 | $6,426”
  - column:Transporation: 1400 ⟵ “Transporation | $700 | $700 | $1,400”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $66 | $66 | $132”
  - column:TOTAL FOR TERMS: 26490 ⟵ “TOTAL FOR TERMS | $13,245 | $13,245 | $26,490”
### `e5fccfeda1be2521` Saint Paul College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.saintpaul.edu/admissions/financial-aid/award-information/ (sha256 c2ce96b26c52)
- issues: components_do_not_reconcile, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 5705 ⟵ “Tuition | $2,853 | $2,853 | $5,705”
  - column:Fees: 850 ⟵ “Fees | $425 | $425 | $850”
  - column:Books/Supplies: 1200 ⟵ “Books/Supplies | $600 | $600 | $1,200”
  - column:Food & Housing: 10396 ⟵ “Food & Housing | $5,198 | $5,198 | $10,396”
  - column:Personal/Misc Expenses: 6426 ⟵ “Personal/Misc Expenses | $3,213 | $3,213 | $6,426”
  - column:Transporation: 1400 ⟵ “Transporation | $700 | $700 | $1,400”
  - column:Loan Fees: 132 ⟵ “Loan Fees | $66 | $66 | $132”
  - column:TOTAL: 26110 ⟵ “TOTAL | $13,055 | $13,055 | $26,110”
### `41aae57cd375003d` South Central College — appeals 2026-27 [new] (labeled_in_source)
- source: https://southcentral.edu/Financial-Aid/financial-aid-home.html (sha256 d46072f27a22)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “Review Your Award Offer Your financial aid award offer will be available in eServices once your file is complete.”
### `bd59533777f9c2c5` South Central College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://southcentral.edu/Financial-Aid/financial-aid-home.html (sha256 d46072f27a22)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition and Fees: 6910 ⟵ “Tuition and Fees | $3,455 | $3,455 | $6,910”
  - column:Books, Course Materials, Supplies, and Equipment*: 1200 ⟵ “Books, Course Materials, Supplies, and Equipment* | $600 | $600 | $1,200”
  - column:Direct Costs (Tuition + Fees + Books): 8110 ⟵ “Direct Costs (Tuition + Fees + Books) | $4,055 | $4,055 | $8,110”
  - column:Food and Housing: 10480 ⟵ “Food and Housing | $5,240 | $5,240 | $10,480”
  - column:Transportation: 2200 ⟵ “Transportation | $1,100 | $1,100 | $2,200”
  - column:Personal / Miscellaneous: 3960 ⟵ “Personal / Miscellaneous | $1,980 | $1,980 | $3,960”
  - column:Indirect Costs: 16640 ⟵ “Indirect Costs | $8,320 | $8,320 | $16,640”
  - column:Total Direct + Indirect Costs: 24750 ⟵ “Total Direct + Indirect Costs | $12,375 | $12,375 | $24,750”
### `b2abc5320d0b83f4` Southwest Minnesota State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.smsu.edu/campuslife/financialaid/applying-for-financial-aid.html (sha256 1aa9df0e109b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Contact SMSU Financial Aid with questions or special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Changes to Financial Information Contact the Financial Aid Office if information previously submitted on your financial aid forms changes or if you experience a significant change in financial circumstances.”
### `89371568cb92dd4e` Southwest Minnesota State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smsu.edu/admission/paying-for-college.html (sha256 834e81663f8f)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition & Fees: 11516 ⟵ “Tuition & Fees | $11,516”
  - column:Housing & Food: 11850 ⟵ “Housing & Food | $11,850”
  - column:Books, Materials, Supplies, Equipment: 1200 ⟵ “Books, Materials, Supplies, Equipment | $1,200”
  - column:Transportation, Personal Expenses, Loan fees: 3652 ⟵ “Transportation, Personal Expenses, Loan fees | $3,652”
  - column:TOTAL: 28218 ⟵ “TOTAL | $28,218”
### `cd19b00f91ae8bf5` St Catherine University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.stkate.edu/admission-and-aid/financial-aid/cost-of-attendance (sha256 2fd17cc52d87)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition (based on banded rate): 52320 ⟵ “Tuition (based on banded rate) | $52,320 | $53,888”
  - on_campus:Student Activity Fee: 294 ⟵ “Student Activity Fee | $294 | $294”
  - on_campus:Technology Fee: 600 ⟵ “Technology Fee | $600 | $600”
  - on_campus:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70”
  - on_campus:Books, Course Materials, Supplies, & Equipment: 1000 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,000 | $1,000”
  - on_campus:Housing: 8000 ⟵ “Housing | $8,000 | $8350”
  - on_campus:Food: 4650 ⟵ “Food | $4,650 | $4,742”
  - on_campus:Personal Expenses, Miscellaneous: 2420 ⟵ “Personal Expenses, Miscellaneous | $2,420 | $2,468”
  - on_campus:Transportation: 460 ⟵ “Transportation | $460 | $460”
  - on_campus:TOTAL: 69814 ⟵ “TOTAL | $69,814 | $71,872”
### `c94cc2837c1c58b1` St Cloud Technical and Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://sctcc.edu/index%2Ephp/program-costs (sha256 bde8a5406047)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees:: 6740 ⟵ “Tuition and Fees: | $6,740 | $5,055 | $3,370”
  - column:Estimated Housing:: 6390 ⟵ “Estimated Housing: | $6,390 | $6,390 | $6,390”
  - column:Estimated Food:: 3290 ⟵ “Estimated Food: | $3,290 | $3,290 | $3,290”
  - column:Estimated Books and Supplies:: 1300 ⟵ “Estimated Books and Supplies: | $1,300 | $975 | $650”
  - column:Estimated Transportation:: 1200 ⟵ “Estimated Transportation: | $1,200 | $1,200 | $1,200”
  - column:Estimated Personal Expenses:: 3000 ⟵ “Estimated Personal Expenses: | $3,000 | $3,000 | $3,000”
  - column:TOTAL Cost Est:: 21920 ⟵ “TOTAL Cost Est: | $21,920 | $19,910 | $17,900”
  - column:Tuition and Fees:: 5055 ⟵ “Tuition and Fees: | $6,740 | $5,055 | $3,370”
  - column:Estimated Housing:: 6390 ⟵ “Estimated Housing: | $6,390 | $6,390 | $6,390”
  - column:Estimated Food:: 3290 ⟵ “Estimated Food: | $3,290 | $3,290 | $3,290”
  - column:Estimated Books and Supplies:: 975 ⟵ “Estimated Books and Supplies: | $1,300 | $975 | $650”
  - column:Estimated Transportation:: 1200 ⟵ “Estimated Transportation: | $1,200 | $1,200 | $1,200”
  - column:Estimated Personal Expenses:: 3000 ⟵ “Estimated Personal Expenses: | $3,000 | $3,000 | $3,000”
  - column:TOTAL Cost Est:: 19910 ⟵ “TOTAL Cost Est: | $21,920 | $19,910 | $17,900”
  - column:Tuition and Fees:: 3370 ⟵ “Tuition and Fees: | $6,740 | $5,055 | $3,370”
  - column:Estimated Housing:: 6390 ⟵ “Estimated Housing: | $6,390 | $6,390 | $6,390”
  - column:Estimated Food:: 3290 ⟵ “Estimated Food: | $3,290 | $3,290 | $3,290”
  - column:Estimated Books and Supplies:: 650 ⟵ “Estimated Books and Supplies: | $1,300 | $975 | $650”
  - column:Estimated Transportation:: 1200 ⟵ “Estimated Transportation: | $1,200 | $1,200 | $1,200”
  - column:Estimated Personal Expenses:: 3000 ⟵ “Estimated Personal Expenses: | $3,000 | $3,000 | $3,000”
  - column:TOTAL Cost Est:: 17900 ⟵ “TOTAL Cost Est: | $21,920 | $19,910 | $17,900”
### `01aeafa552a43274` St Olaf College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/ (sha256 3312e7b0131d)
- issues: semantic_review_required, conflicting_sources:https://wp.stolaf.edu/financialaid,https://wp.stolaf.edu/financialaid/files/2026/01/Special-Circumstance-Request-1.pdf,https://wp.stolaf.edu/financialaid/merit-scholarships/,https://wp.stolaf.edu/financialaid/outside-scholarships/,https://wp.stolaf.edu/financialaid/special-circumstances/,https://wp.stolaf.edu/financialaid/st-olaf-merit-based-aid-renewal/,https://wp.stolaf.edu/financialaid/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Olaf Financial Aid Withdrawal Policies Graduating Seniors Student Loan Repayment Book An Appointment Financing Study Abroad Appeals and Special Circumstances Find & Upload Forms Financial Literacy Consumer Disclosures Admissions Cost of Attendance Frequently Asked Questions Contact Financial Aid Tomson 120 1520 St.”
  - sentence: need_based_special_circumstances ⟵ “Examples may include a death in the family, student injury or illness, or other special circumstances as approved by St.”
### `060eb663fa9f8a32` St Olaf College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/transfer-students/ (sha256 4949bf9d137f)
- issues: semantic_review_required, conflicting_sources:https://wp.stolaf.edu/financialaid,https://wp.stolaf.edu/financialaid/files/2026/01/Special-Circumstance-Request-1.pdf,https://wp.stolaf.edu/financialaid/merit-scholarships/,https://wp.stolaf.edu/financialaid/outside-scholarships/,https://wp.stolaf.edu/financialaid/special-circumstances/,https://wp.stolaf.edu/financialaid/st-olaf-merit-based-aid-renewal/,https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Olaf Financial Aid Withdrawal Policies Graduating Seniors Student Loan Repayment Book An Appointment Financing Study Abroad Appeals and Special Circumstances Find & Upload Forms Financial Literacy Consumer Disclosures Admissions Cost of Attendance Frequently Asked Questions Contact Financial Aid Tomson 120 1520 St.”
### `1a8b3213ab82727f` St Olaf College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/files/2026/01/Special-Circumstance-Request-1.pdf (sha256 4176adf3b871)
- issues: semantic_review_required, conflicting_sources:https://wp.stolaf.edu/financialaid,https://wp.stolaf.edu/financialaid/merit-scholarships/,https://wp.stolaf.edu/financialaid/outside-scholarships/,https://wp.stolaf.edu/financialaid/special-circumstances/,https://wp.stolaf.edu/financialaid/st-olaf-merit-based-aid-renewal/,https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/,https://wp.stolaf.edu/financialaid/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Olaf College Special Circumstance Request ssss ______ Student Name Student’s ID # (if known) dddd Special circumstances are situations beyond a student’s or family’s control that impacts the information reported on the FAFSA.”
### `541591a324570b51` St Olaf College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/ (sha256 3312e7b0131d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “They also need to complete a SAP appeal if their coursework does not meet SAP standards (explained in the appeal process above).”
  - sentence: sap_appeal ⟵ “Complete the SAP appeal process as explained above to appeal the maximum time frame standard.”
### `5c7edc66c7ffc202` St Olaf College — appeals 2026-27 [new] (labeled_in_source)
- source: https://wp.stolaf.edu/financialaid/special-circumstances/ (sha256 098916a40070)
- issues: semantic_review_required, conflicting_sources:https://wp.stolaf.edu/financialaid,https://wp.stolaf.edu/financialaid/files/2026/01/Special-Circumstance-Request-1.pdf,https://wp.stolaf.edu/financialaid/merit-scholarships/,https://wp.stolaf.edu/financialaid/outside-scholarships/,https://wp.stolaf.edu/financialaid/st-olaf-merit-based-aid-renewal/,https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/,https://wp.stolaf.edu/financialaid/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: need_based_special_circumstances ⟵ “Appeals and Special Circumstances – Financial Aid Skip to main content Resources Menu Financial Aid resources for Future Students Current Students Alumni & Families Faculty/Staff Support St.”
  - sentence: need_based_special_circumstances ⟵ “Olaf Search sitewide: Tools Expand Mobile Menu Financial Aid Global Navigation About Academics Admissions On the Hill Appeals and Special Circumstances Financial Aid Menu Types of Aid Merit Scholarships Need-Based Grants Loans Outside Scholarships Student Employment Terms and Conditions of Your Award Applying for Financial Aid Prospective Students How to Apply for Financial Aid Affording a St.”
  - sentence: need_based_special_circumstances ⟵ “Olaf Financial Aid Withdrawal Policies Graduating Seniors Student Loan Repayment Book An Appointment Financing Study Abroad Appeals and Special Circumstances Find & Upload Forms Financial Literacy Consumer Disclosures Admissions Cost of Attendance Frequently Asked Questions Contact Financial Aid Tomson 120 1520 St.”
  - sentence: need_based_special_circumstances ⟵ “P 507-786-3019 E finaid@stolaf.edu Financial Aid Appeals and Special Circumstances We understand that a financial aid application cannot account for everything going on in a family’s financial situation.”
  - sentence: need_based_special_circumstances ⟵ “The following circumstances are automatically considered when evaluating your financial aid: Federal, state, and other taxes “Typical” medical expenses (usually around 5% of total income) Routine household expenses Routine vehicle and travel expenses Tuition expenses for children in private school reported on the CSS Profile Multiple children in college pursuing first-time undergraduate degrees Pr”
  - sentence: need_based_special_circumstances ⟵ “Please submit all Special Circumstance documentation through our secure upload portal.”
### `8bce1fc2d16c0010` St Olaf College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid (sha256 b5793f297654)
- issues: semantic_review_required, conflicting_sources:https://wp.stolaf.edu/financialaid/files/2026/01/Special-Circumstance-Request-1.pdf,https://wp.stolaf.edu/financialaid/merit-scholarships/,https://wp.stolaf.edu/financialaid/outside-scholarships/,https://wp.stolaf.edu/financialaid/special-circumstances/,https://wp.stolaf.edu/financialaid/st-olaf-merit-based-aid-renewal/,https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/,https://wp.stolaf.edu/financialaid/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Olaf Financial Aid Withdrawal Policies Graduating Seniors Student Loan Repayment Book An Appointment Financing Study Abroad Appeals and Special Circumstances Find & Upload Forms Financial Literacy Consumer Disclosures Admissions Cost of Attendance Frequently Asked Questions Contact Financial Aid Tomson 120 1520 St.”
### `b77c22331b8768d3` St Olaf College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/merit-scholarships/ (sha256 9251430a3930)
- issues: semantic_review_required, conflicting_sources:https://wp.stolaf.edu/financialaid,https://wp.stolaf.edu/financialaid/files/2026/01/Special-Circumstance-Request-1.pdf,https://wp.stolaf.edu/financialaid/outside-scholarships/,https://wp.stolaf.edu/financialaid/special-circumstances/,https://wp.stolaf.edu/financialaid/st-olaf-merit-based-aid-renewal/,https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/,https://wp.stolaf.edu/financialaid/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Olaf Financial Aid Withdrawal Policies Graduating Seniors Student Loan Repayment Book An Appointment Financing Study Abroad Appeals and Special Circumstances Find & Upload Forms Financial Literacy Consumer Disclosures Admissions Cost of Attendance Frequently Asked Questions Contact Financial Aid Tomson 120 1520 St.”
### `ceab481fb5851d36` St Olaf College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/outside-scholarships/ (sha256 4795529948fe)
- issues: semantic_review_required, conflicting_sources:https://wp.stolaf.edu/financialaid,https://wp.stolaf.edu/financialaid/files/2026/01/Special-Circumstance-Request-1.pdf,https://wp.stolaf.edu/financialaid/merit-scholarships/,https://wp.stolaf.edu/financialaid/special-circumstances/,https://wp.stolaf.edu/financialaid/st-olaf-merit-based-aid-renewal/,https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/,https://wp.stolaf.edu/financialaid/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Olaf Financial Aid Withdrawal Policies Graduating Seniors Student Loan Repayment Book An Appointment Financing Study Abroad Appeals and Special Circumstances Find & Upload Forms Financial Literacy Consumer Disclosures Admissions Cost of Attendance Frequently Asked Questions Contact Financial Aid Tomson 120 1520 St.”
### `cf872e7cc682eb7e` St Olaf College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wp.stolaf.edu/financialaid/st-olaf-merit-based-aid-renewal/ (sha256 e42fd16b53c4)
- issues: semantic_review_required, conflicting_sources:https://wp.stolaf.edu/financialaid,https://wp.stolaf.edu/financialaid/files/2026/01/Special-Circumstance-Request-1.pdf,https://wp.stolaf.edu/financialaid/merit-scholarships/,https://wp.stolaf.edu/financialaid/outside-scholarships/,https://wp.stolaf.edu/financialaid/special-circumstances/,https://wp.stolaf.edu/financialaid/terms-and-conditions-of-your-award/,https://wp.stolaf.edu/financialaid/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Olaf Financial Aid Withdrawal Policies Graduating Seniors Student Loan Repayment Book An Appointment Financing Study Abroad Appeals and Special Circumstances Find & Upload Forms Financial Literacy Consumer Disclosures Admissions Cost of Attendance Frequently Asked Questions Contact Financial Aid Tomson 120 1520 St.”
### `0834149bbd04a2b4` St Olaf College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://wp.stolaf.edu/stuacct/compfee-2/ (sha256 2b5d8515b0d9)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 62700 ⟵ “Tuition | $31,350 | $31,350 | $62,700”
  - column:Housing*: 6820 ⟵ “Housing* | $3,410 | $3,410 | $6,820”
  - column:Meal Plan**: 7480 ⟵ “Meal Plan** | $3,740 | $3,740 | $7,480”
  - column:Total: 77000 ⟵ “Total | $38,500 | $38,500 | $77,000”
### `3c176651287e1103` The College of Saint Scholastica — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://resources.css.edu/admissions/docs/ap_exam_awards.pdf (sha256 cdabf2603b6a)
- issues: course_column_missing
- checks: {"distinct_exams": 37, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2D Art & Design                            3          4               n/a                            n/a”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3D Art & Design                            3          4               n/a                            n/a”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies                   3          4               n/a                            n/a”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                                3          4               n/a                          n/a”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                    3          4               n/a                          n/a”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calc AB Subscore                           3          4               n/a                          n/a”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                  3          4               n/a                          n/a”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture                 3          4               n/a                          n/a”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                         3          4               n/a                          n/a”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles                3          4               n/a                          n/a”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                                    3          4               n/a                          n/a”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition             3          4               n/a                          n/a”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition           3          4                 n/a                        n/a”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                      3          4                 n/a                        n/a”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                           3          4                 n/a                        n/a”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture                  3          4                 n/a                        n/a”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture                  3          4                 n/a                        n/a”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                            3          4                 n/a                        n/a”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language & Culture                 3          4                 n/a                        n/a”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language & Culture                3          4                 n/a                        n/a”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin                                      3          4                 n/a                        n/a”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                             3          4                 n/a                        n/a”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                             3          4                 n/a                        n/a”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                               3          4                 n/a                        n/a”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity & Magnetism         3          4                 n/a                       n/a”
  - … 12 more rows
### `e0e7845c99a3efdd` The College of Saint Scholastica — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://resources.css.edu/admissions/docs/ib_exam_awards.pdf (sha256 3fb6e545a1c1)
- issues: course_column_missing
- checks: {"distinct_exams": 23, "equivalencies": 23, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4-7]:  ⟵ “Higher Level Anthropology, Social &             4-7             4        n/a                      n/a”
  - equivalencies[IB-BIOLOGY|4-7]:  ⟵ “Higher Level Biology                             4-7            4        Natural Science          n/a”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4-7]:  ⟵ “Higher Level Business & Management               4-7            4        n/a                      n/a”
  - equivalencies[IB-CHEMISTRY|4-7]:  ⟵ “Higher Level Chemistry                           4-7            4        n/a                      n/a”
  - equivalencies[IB-LATIN|4-7]:  ⟵ “Higher Level Classical Languages-Latin           4-7            4        n/a                      n/a”
  - equivalencies[IB-COMPUTER-SCIENCE|4-7]:  ⟵ “Higher Level Computer Science                    4-7            4        n/a                      n/a”
  - equivalencies[IB-ECONOMICS|4-7]:  ⟵ “Higher Level Economics                           4-7            4        n/a                      n/a”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4-7]:  ⟵ “Higher Level English A: Language &               4-7            4        n/a                      n/a”
  - equivalencies[IB-ENGLISH-A-LITERATURE|4-7]:  ⟵ “Higher Level English A: Literature               4-7            4        n/a                      n/a”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4-7]:  ⟵ “Higher Level Environmental Systems &             4-7            4        n/a                      n/a”
  - equivalencies[IB-FILM|4-7]:  ⟵ “Higher Level Film                                4-7            4        n/a                      n/a”
  - equivalencies[IB-FRENCH|4-7]:  ⟵ “Higher Level French A2                           4-7            4        n/a                      n/a”
  - equivalencies[IB-GERMAN|4-7]:  ⟵ “Higher Level German                              4-7            4        n/a                      n/a”
  - equivalencies[IB-GLOBAL-POLITICS|4-7]:  ⟵ “Higher Level Global Politics                     4-7            4        n/a                      n/a”
  - equivalencies[IB-GEOGRAPHY|4-7]:  ⟵ “Higher Level Geography                           4-7            4        n/a                      n/a”
  - equivalencies[IB-HISTORY|4-7]:  ⟵ “Higher Level History                             4-7            4        n/a                      n/a”
  - equivalencies[IB-MUSIC|4-7]:  ⟵ “Higher Level Music                         4-7         4       n/a                 n/a”
  - equivalencies[IB-PHILOSOPHY|4-7]:  ⟵ “Higher Level Philosophy                    4-7         4       n/a                 n/a”
  - equivalencies[IB-PHYSICS|4-7]:  ⟵ “Higher Level Physics                       4-7         4       n/a                 n/a”
  - equivalencies[IB-PSYCHOLOGY|4-7]:  ⟵ “Higher Level Psychology                    4-7         4       n/a                 n/a”
  - equivalencies[IB-SPANISH|4-7]:  ⟵ “Higher Level Spanish A2                    4-7         4       n/a                 n/a”
  - equivalencies[IB-THEATRE|4-7]:  ⟵ “Higher Level Theatre Arts                  4-7         4       n/a                 n/a”
  - equivalencies[IB-VISUAL-ARTS|4-7]:  ⟵ “Higher Level Visual Arts                   4-7         4       n/a                 n/a”
### `66ac9a726bb02015` University of Minnesota-Crookston — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.crk.umn.edu/finances/financial-aid/satisfactory-academic-progress (sha256 4ce8a9443a6f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “SAP appeal If you are not meeting SAP standards, you'll receive an email notice before the beginning of the next term.”
  - sentence: sap_appeal ⟵ “You may submit a Satisfactory Academic Progress Appeal form for the specific aid year you are appealing (find it on the Forms page).”
  - sentence: sap_appeal ⟵ “Questions For questions about SAP or the appeal process, contact the Office of Financial Aid and Scholarships.”
  - sentence: sap_appeal ⟵ “Probation You will be placed on financial aid satisfactory progress probation if a SAP appeal is approved.”
  - sentence: sap_appeal ⟵ “If you do not attain the required GPA and/or cumulative completed credits percentage, but you do successfully follow the academic plan submitted with your SAP appeal, you may submit a follow-up appeal showing you have met the terms of your academic plan.”
### `7239d2ed3f71c9ce` University of Minnesota-Crookston — appeals 2026-27 [new] (source_unlabeled)
- source: https://crk.umn.edu/admissions/high-school-transfer-counselors (sha256 756201817474)
- issues: semantic_review_required, conflicting_sources:https://onestop.crk.umn.edu/finances/financial-aid/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “They explain unusual circumstances and highlight outstanding strengths.”
### `7d4dec8ecd31e8fa` University of Minnesota-Crookston — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.crk.umn.edu/finances/financial-aid/satisfactory-academic-progress (sha256 4ce8a9443a6f)
- issues: semantic_review_required, conflicting_sources:https://crk.umn.edu/admissions/high-school-transfer-counselors
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you failed to meet these standards due to unusual circumstances, you have the right to appeal your SAP suspension status.”
### `4dc989b2ef57dce0` University of Minnesota-Duluth — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.d.umn.edu/finances/financial-aid/appeals-and-financial-aid-revisions (sha256 612d4665b9f0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Expand all + Special Circumstances appeal Special circumstances include events such as a loss of a job, separation or divorce, death, disability, or outstanding medical expenses.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family have a special circumstance, your financial aid eligibility may be reevaluated, and you should contact One Stop Student Services. + Cost of attendance appeal If you have expenses during the academic year that are higher than the University’s Cost of Attendance, we may be able to increase your financial aid eligibility through a Cost of Attendance (COA) adjustment.”
### `7d62add8075c0ae7` University of Minnesota-Duluth — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.d.umn.edu/info/satisfactory-academic-progress-appeal (sha256 c72ee4796768)
- issues: semantic_review_required, conflicting_sources:https://onestop.d.umn.edu/finances/financial-aid/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “View the Satisfactory Academic Progress Appeal form Use this form if...”
### `90a02143b718e7de` University of Minnesota-Duluth — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.d.umn.edu/finances/financial-aid/satisfactory-academic-progress (sha256 1e8537df7016)
- issues: semantic_review_required, conflicting_sources:https://onestop.d.umn.edu/info/satisfactory-academic-progress-appeal
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “SAP appeal If you are not meeting SAP standards, you'll receive an email notice before the beginning of the next term.”
  - sentence: sap_appeal ⟵ “In order to maximize your financial aid eligibility, submit a Satisfactory Academic Progress Appeal form no later than 30 days before the end of the term you receive notice.”
  - sentence: sap_appeal ⟵ “Questions For questions about SAP or the appeal process, contact One Stop.”
  - sentence: sap_appeal ⟵ “Probation You will be placed on financial aid satisfactory progress probation if a SAP appeal is approved.”
  - sentence: sap_appeal ⟵ “If you do not attain the required GPA and/or cumulative completed credits percentage, but you do successfully follow the academic plan submitted with your SAP appeal, you may submit a follow-up appeal showing you have met the terms of your academic plan.”
### `e74168f879646072` University of Minnesota-Duluth — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.d.umn.edu/costs-aid/scholarships (sha256 ecef2a44840f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Please email our office or contact an Admissions Counselor to request a copy of the scholarship appeal form.”
### `2d16ca5126a697df` University of Minnesota-Duluth — costs 2027-28 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.d.umn.edu/costs-and-aid (sha256 10a3e051e77f)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - on_campus:Tuition & Fees: 15810 ⟵ “Tuition & Fees | $15,810 | $15,810 | $21,780”
  - on_campus:Housing & Food: 12310 ⟵ “Housing & Food | $12,310 | $12,310 | $12,310”
  - on_campus:DIRECT COSTS Subtotal: 28120 ⟵ “DIRECT COSTS Subtotal | $28,120 | $28,120 | $34,090”
  - on_campus:Total Additional Expenses: 3870 ⟵ “Total Additional Expenses | $3,200 | $3,870 | $4,870”
  - on_campus:COST OF ATTENDANCE* Total: 31990 ⟵ “COST OF ATTENDANCE* Total | $31,320 | $31,990 | $38,960”
### `d697f3d503193226` University of Minnesota-Duluth — costs 2027-28 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.d.umn.edu/costs-and-aid (sha256 10a3e051e77f)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 5}
  - column:Tuition & Fees: 15810 ⟵ “Tuition & Fees | $15,810 | $15,810 | $21,780”
  - column:Housing & Food: 12310 ⟵ “Housing & Food | $12,310 | $12,310 | $12,310”
  - column:DIRECT COSTS Subtotal: 28120 ⟵ “DIRECT COSTS Subtotal | $28,120 | $28,120 | $34,090”
  - column:Total Additional Expenses: 3200 ⟵ “Total Additional Expenses | $3,200 | $3,870 | $4,870”
  - column:COST OF ATTENDANCE* Total: 31320 ⟵ “COST OF ATTENDANCE* Total | $31,320 | $31,990 | $38,960”
  - column:Tuition & Fees: 21780 ⟵ “Tuition & Fees | $15,810 | $15,810 | $21,780”
  - column:Housing & Food: 12310 ⟵ “Housing & Food | $12,310 | $12,310 | $12,310”
  - column:DIRECT COSTS Subtotal: 34090 ⟵ “DIRECT COSTS Subtotal | $28,120 | $28,120 | $34,090”
  - column:Total Additional Expenses: 4870 ⟵ “Total Additional Expenses | $3,200 | $3,870 | $4,870”
  - column:COST OF ATTENDANCE* Total: 38960 ⟵ “COST OF ATTENDANCE* Total | $31,320 | $31,990 | $38,960”
### `5d8be8907581ac59` University of Minnesota-Morris — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://morris.umn.edu/costs-aid/costs-glance (sha256 3aa1f6ab5c7a)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition*: 14314 ⟵ “Tuition* | $14,314 | $14,314 | $16,692”
  - on_campus:Required fees*: 1580 ⟵ “Required fees* | $1,580 | $1,580 | $1,580”
  - on_campus:Housing**: 6250 ⟵ “Housing** | $6,250 | $6,250 | $6,250”
  - on_campus:Food**: 6428 ⟵ “Food** | $6,428 | $6,428 | $6,428”
  - on_campus:Direct costs subtotal: 28572 ⟵ “Direct costs subtotal | $28,572 | $28,572 | $30,950”
  - on_campus:Additional expenses: 3350 ⟵ “Additional expenses | $3,350 | $3,350 | $4,470”
  - on_campus:Total cost of attendance: 31922 ⟵ “Total cost of attendance | $31,922 | $31,922 | $35,420”
  - column:Tuition*: 14314 ⟵ “Tuition* | $14,314 | $14,314 | $16,692”
  - column:Required fees*: 1580 ⟵ “Required fees* | $1,580 | $1,580 | $1,580”
  - column:Housing**: 6250 ⟵ “Housing** | $6,250 | $6,250 | $6,250”
  - column:Food**: 6428 ⟵ “Food** | $6,428 | $6,428 | $6,428”
  - column:Direct costs subtotal: 28572 ⟵ “Direct costs subtotal | $28,572 | $28,572 | $30,950”
  - column:Additional expenses: 3350 ⟵ “Additional expenses | $3,350 | $3,350 | $4,470”
  - column:Total cost of attendance: 31922 ⟵ “Total cost of attendance | $31,922 | $31,922 | $35,420”
  - column:Tuition*: 16692 ⟵ “Tuition* | $14,314 | $14,314 | $16,692”
  - column:Required fees*: 1580 ⟵ “Required fees* | $1,580 | $1,580 | $1,580”
  - column:Housing**: 6250 ⟵ “Housing** | $6,250 | $6,250 | $6,250”
  - column:Food**: 6428 ⟵ “Food** | $6,428 | $6,428 | $6,428”
  - column:Direct costs subtotal: 30950 ⟵ “Direct costs subtotal | $28,572 | $28,572 | $30,950”
  - column:Additional expenses: 4470 ⟵ “Additional expenses | $3,350 | $3,350 | $4,470”
  - column:Total cost of attendance: 35420 ⟵ “Total cost of attendance | $31,922 | $31,922 | $35,420”
### `9011313e14499449` University of Minnesota-Rochester — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.r.umn.edu/finances/financial-aid/satisfactory-academic-progress (sha256 3b5d5c7a452c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “SAP appeal If you are not meeting SAP standards, you'll receive an email notice before the beginning of the next term.”
  - sentence: sap_appeal ⟵ “You may submit a Satisfactory Academic Progress Appeal (UMN login required) no later than 30 days before the end of the term you receive notice.”
  - sentence: sap_appeal ⟵ “Questions For questions about SAP or the appeal process, contact One Stop.”
  - sentence: sap_appeal ⟵ “Probation You will be placed on financial aid satisfactory progress probation if a SAP appeal is approved.”
  - sentence: sap_appeal ⟵ “If you do not attain the required GPA and/or cumulative completed credits percentage, but you do successfully follow the academic plan submitted with your SAP appeal, you may submit a follow-up appeal showing you have met the terms of your academic plan.”
### `b78b801ef8091226` University of Minnesota-Rochester — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.r.umn.edu/finances/financial-aid/satisfactory-academic-progress (sha256 3b5d5c7a452c)
- issues: semantic_review_required, conflicting_sources:https://onestop.r.umn.edu/finances/financial-aid/appeals-and-financial-aid-revisions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you failed to meet these standards due to unusual circumstances, you have the right to appeal your SAP suspension status.”
### `e9af9dab17835fef` University of Minnesota-Rochester — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.r.umn.edu/finances/financial-aid/appeals-and-financial-aid-revisions (sha256 2216b0386108)
- issues: semantic_review_required, conflicting_sources:https://onestop.r.umn.edu/finances/financial-aid/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Expand all + Special Circumstances appeal Special circumstances include events such as a loss of a job, separation or divorce, death, disability, or outstanding medical expenses.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family have a special circumstance, you can fill out the Special Circumstances Appeal Intake form by selecting the appropriate aid year and dependency status below.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Appeal Intake Form - Dependent Student Special Circumstances Appeal Intake Form- Independent Student + Cost of attendance appeal If you have expenses during the academic year that are higher than the University’s Cost of Attendance, we may be able to increase your financial aid eligibility through a Cost of Attendance (COA) adjustment.”
  - sentence: need_based_special_circumstances ⟵ “Some appeals lead to increased aid in the form of a loan offer or no change at all. + Unusual circumstances The following instances may require you to contact One Stop Student Services to determine if you should submit an appeal or additional information regarding your financial aid eligibility and dependency status.”
### `3140ace28cd6fca7` University of Minnesota-Rochester — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://r.umn.edu/admissions/undergraduate-admissions/bachelor-science-health-science-admission/advanced-placement (sha256 fe37b5e62ad2)
- issues: score_column_not_scores, score_scale_mismatch
- checks: {"distinct_exams": 9, "equivalencies": 10, "rows_without_score": 0}
  - equivalencies[IB-ECONOMICS|60]:  ⟵ “Principles of Microeconomics | 60 | 4 credits towards degree | 4 credits towards degree | Social Sciences Area”
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | 5-7 | 4 credits in BIOL 2311 | 4 credits in BIOL 2311 | Laboratory Sciences Area”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business Management]:  ⟵ “Business Management | 5-7 | 4 credits towards degree | 4 credits towards degree | ”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 5-7 | 4 credits towards degree AND 4 credits in CHEM 2335 & 2336 | 4 credits towards degree AND 4 credits in CHEM 2335 & 2336 AND Satisfies CHEMISTRY Admissions Req | Laboratory Sciences Area”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | 5-7 | 8 credits towards degree | 8 credits towards degree | ”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | 5-7 | 8 credits towards degree | 8 credits towards degree | Social Sciences Area”
  - equivalencies[IB-HISTORY|History]:  ⟵ “History | 5-7 | 8 credits towards degree | 8 credits towards degree | Challenges Throughout History”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | 5-7 | 4 credits in PHYS 1251, 4 credits in PHYS 2251 | 4 credits in PHYS 1251, 4 credits in PHYS 2251 AND Satisfies PHYSICS Admissions Requirement | Laboratory Sciences Area”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | 5-7 | 3 credits in PSY 1511, 5 credits towards degree | 3 credits in PSY 1511, 5 credits towards degree AND Satisfies PSYCHOLOGY Admission Req | Social Sciences Area”
  - equivalencies[IB-THEATRE|Theatre]:  ⟵ “Theatre | 5-7 | 8 credits towards degree | 8 credits towards degree | Humanities Area”
### `cddd5ee86b95c482` University of Minnesota-Rochester — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://r.umn.edu/admissions/undergraduate-admissions/bachelor-science-health-science-admission/advanced-placement (sha256 fe37b5e62ad2)
- issues: course_column_missing
- checks: {"distinct_exams": 20, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, 5]:  ⟵ “African American Studies | 3, 4, 5 | 3 credits toward degree | 3 credits toward degree | Humanities Area; Challenges in Social Structures Theme”
  - equivalencies[AP-ART-HISTORY|3,4,5]:  ⟵ “Art History | 3,4,5 | 4 credits toward degree | 4 credits toward degree | Humanities Area”
  - equivalencies[AP-BIOLOGY|3, 4, 5]:  ⟵ “Biology | 3, 4, 5 | 4 credits in BIOL 2311 | 4 credits in BIOL 2311 | Laboratory Sciences Area”
  - equivalencies[AP-CALCULUS-AB|3, 4, 5]:  ⟵ “Calculus AB | 3, 4, 5 | 4 credits in MATH 1171 | 4 credits in MATH 1171 AND satisfies MATH Admissions Req | Mathematical Thinking Area”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 4 credits in MATH 1171 | 4 credits in MATH 1171 AND Satisfies MATH Admissions Req | Mathematical Thinking Area”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | 8 credits in MATH 1171, 2171 | 8 credits in MATH 1171, 2171 Satisfies MATH Admissions Req | Mathematical Thinking Area”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 credits toward degree | 4 credits toward degree AND Satisfies CHEM Admissions Req | Laboratory Sciences Area”
  - equivalencies[AP-CHEMISTRY|4, 5]:  ⟵ “Chemistry | 4, 5 | 4 credits toward degree AND 4 credits in CHEM 2335 & 2336 | 4 credits toward degree AND 4 credits in CHEM 2335 & 2336 AND Satisfies CHEMISTRY Admissions Req | Laboratory Sciences Area”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3,4,5]:  ⟵ “Computer Science A | 3,4,5 | 4 credits toward degree | 4 credits toward degree | Mathematical Thinking Area”
  - equivalencies[AP-MICROECONOMICS|3,4,5]:  ⟵ “Economics-Micro | 3,4,5 | 4 credits toward degree | 4 credits toward degree | Social Sciences Area”
  - equivalencies[AP-MACROECONOMICS|3,4,5]:  ⟵ “Economics-Macro | 3,4,5 | 4 credits toward degree | 4 credits toward degree | Social Sciences Area”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3,4,5]:  ⟵ “English Language and Composition | 3,4,5 | 4 credits in WRIT 1501 | 4 credits in WRIT 1501 AND Satisfies WRITING Admission Req | Writing Area”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3,4,5]:  ⟵ “English Literature & Composition | 3,4,5 | 4 credits in WRIT 1501 AND 3 credits toward degree | 4 credits in WRIT 1501, 3 credits toward degree AND Satisfies WRITING Admission Req | Writing Area”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3,4,5]:  ⟵ “Environmental Science | 3,4,5 | 3 credits towards degree | 3 credits toward degree | Laboratory Sciences Area”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3,4,5]:  ⟵ “French Literature | 3,4,5 | 3 credits towards degree | 3 credits toward degree | ”
  - equivalencies[AP-LATIN|3,4,5]:  ⟵ “Latin (Vergil) | 3,4,5 | 4 credits towards degree | 4 credits toward degree | ”
  - equivalencies[AP-MUSIC-THEORY|5]:  ⟵ “Music Theory | 5 | 5 credits towards degree | 5 credits towards degree | ”
  - equivalencies[AP-PHYSICS-1|3,4,5]:  ⟵ “Physics I | 3,4,5 | 4 credits towards degree | Satisfies PHYSICS Admission Req | Laboratory Sciences Area”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3,4,5]:  ⟵ “Physics C (Mechanics) | 3,4,5 | 4 credits in PHYS 1251 | 4 credits in PHYS 1251 AND Satisfies PHYSICS Admission Req | Laboratory Sciences Area”
  - equivalencies[AP-PSYCHOLOGY|4,5]:  ⟵ “Psychology | 4,5 | 3 credits in PSY 1511 | 3 credits in PSY 1511 AND Satisfies PSYCHOLOGY Admission Req. | Social Sciences Area”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|4,5]:  ⟵ “Spanish Literature | 4,5 | 3 credits towards degree | 3 credits towards degree | Humanities Area”
  - equivalencies[AP-STATISTICS|3,4,5]:  ⟵ “Statistics | 3,4,5 | 3 credits in MATH 1161 | 3 credits in MATH 1161 AND Satisfies STATISTICS Admission Req | Mathematical Thinking Area”
### `e38f39e126d9e961` University of Minnesota-Twin Cities — appeals 2026-27 [new] (source_unlabeled)
- source: https://onestop.umn.edu/finances/financial-aid/satisfactory-academic-progress (sha256 b0bff223bc47)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “SAP appeal If you are not meeting SAP standards, you'll receive an email notice before the beginning of the next term.”
  - sentence: sap_appeal ⟵ “In order to maximize your financial aid eligibility, your Satisfactory Academic Progress Appeal (UMN login required) should be submitted at least two weeks prior to the end of the term in which you are seeking an adjustment.”
  - sentence: sap_appeal ⟵ “Questions For questions about SAP or the appeal process, contact One Stop.”
  - sentence: sap_appeal ⟵ “Probation You will be placed on financial aid satisfactory progress probation if a SAP appeal is approved.”
  - sentence: sap_appeal ⟵ “If you do not attain the required GPA and/or cumulative completed credits percentage, but you do successfully follow the academic plan submitted with your SAP appeal, you may submit a follow-up appeal showing you have met the terms of your academic plan.”
### `59302bd1b2f71369` University of Minnesota-Twin Cities — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.tc.umn.edu/cost-aid/cost-aid-scholarships/cost-attendance (sha256 b006cdaccfff)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 9}
  - on_campus:Tuition & Fees 4: 43348 ⟵ “Tuition & Fees 4 | $19,312 | $19,312 | $43,348”
  - on_campus:Book & Supplies: 1000 ⟵ “Book & Supplies | $1,000 | $1,000 | $1,000”
  - on_campus:Housing & Food 4: 15552 ⟵ “Housing & Food 4 | $6,374 | $15,552 | $15,552”
  - on_campus:Transportation: 1700 ⟵ “Transportation | $200 | $200 | $1,700”
  - on_campus:Personal/Misc 5: 2000 ⟵ “Personal/Misc 5 | $2,000 | $2,000 | $2,000”
  - on_campus:Loan Fee: 162 ⟵ “Loan Fee | $162 | $162 | $162”
  - on_campus:Total (add an average of $828 if you are living off campus): 63762 ⟵ “Total (add an average of $828 if you are living off campus) | $29,048 | $38,226 | $63,762 *”
  - on_campus:Surcharge for CSOM students and CSE students 6: 3100 ⟵ “Surcharge for CSOM students and CSE students 6 | $3,100 | $3,100 | $3,100”
  - on_campus:Total with CSOM/CSE surcharge: 66862 ⟵ “Total with CSOM/CSE surcharge | $32,148 | $41,326 | $66,862”
### `7210ce7074ab3d6f` University of Minnesota-Twin Cities — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.tc.umn.edu/cost-aid/cost-aid-scholarships/cost-attendance (sha256 b006cdaccfff)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 9}
  - on_campus:Tuition & Fees 4: 19312 ⟵ “Tuition & Fees 4 | $19,312 | $19,312 | $43,348”
  - on_campus:Book & Supplies: 1000 ⟵ “Book & Supplies | $1,000 | $1,000 | $1,000”
  - on_campus:Housing & Food 4: 15552 ⟵ “Housing & Food 4 | $6,374 | $15,552 | $15,552”
  - on_campus:Transportation: 200 ⟵ “Transportation | $200 | $200 | $1,700”
  - on_campus:Personal/Misc 5: 2000 ⟵ “Personal/Misc 5 | $2,000 | $2,000 | $2,000”
  - on_campus:Loan Fee: 162 ⟵ “Loan Fee | $162 | $162 | $162”
  - on_campus:Total (add an average of $828 if you are living off campus): 38226 ⟵ “Total (add an average of $828 if you are living off campus) | $29,048 | $38,226 | $63,762 *”
  - on_campus:Surcharge for CSOM students and CSE students 6: 3100 ⟵ “Surcharge for CSOM students and CSE students 6 | $3,100 | $3,100 | $3,100”
  - on_campus:Total with CSOM/CSE surcharge: 41326 ⟵ “Total with CSOM/CSE surcharge | $32,148 | $41,326 | $66,862”
### `a231d58147e3bb89` University of Minnesota-Twin Cities — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://admissions.tc.umn.edu/cost-aid/cost-aid-scholarships/cost-attendance (sha256 b006cdaccfff)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 1, "rows": 9}
  - with_parents_or_family:Tuition & Fees 4: 19312 ⟵ “Tuition & Fees 4 | $19,312 | $19,312 | $43,348”
  - with_parents_or_family:Book & Supplies: 1000 ⟵ “Book & Supplies | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:Housing & Food 4: 6374 ⟵ “Housing & Food 4 | $6,374 | $15,552 | $15,552”
  - with_parents_or_family:Transportation: 200 ⟵ “Transportation | $200 | $200 | $1,700”
  - with_parents_or_family:Personal/Misc 5: 2000 ⟵ “Personal/Misc 5 | $2,000 | $2,000 | $2,000”
  - with_parents_or_family:Loan Fee: 162 ⟵ “Loan Fee | $162 | $162 | $162”
  - with_parents_or_family:Total (add an average of $828 if you are living off campus): 29048 ⟵ “Total (add an average of $828 if you are living off campus) | $29,048 | $38,226 | $63,762 *”
  - with_parents_or_family:Surcharge for CSOM students and CSE students 6: 3100 ⟵ “Surcharge for CSOM students and CSE students 6 | $3,100 | $3,100 | $3,100”
  - with_parents_or_family:Total with CSOM/CSE surcharge: 32148 ⟵ “Total with CSOM/CSE surcharge | $32,148 | $41,326 | $66,862”
### `789091398a567e3c` University of Minnesota-Twin Cities — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://admissions.tc.umn.edu/college-level-examination-program-awards (sha256 a4a0b5b97e0e)
- issues: course_column_missing
- checks: {"distinct_exams": 3, "equivalencies": 3, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|60]:  ⟵ “College Mathematics | 60 | 3 credits in Math 1999 | Mathematical Thinking core requirement”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|60]:  ⟵ “Principles of Microeconomics | 60 | 4 credits in Econ 1101 | Social Science core requirement”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|60]:  ⟵ “Principles of Macroeconomics | 60 | 4 credits in Econ 1102 | Social Science core requirement”
### `b1e520cebf05748f` University of St Thomas — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.stthomas.edu/financial-aid/undergraduate/index.html (sha256 55a3011d0dc9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Aid Packages Can Be Reevaluated If your family experiences a substantial change in financial circumstances, we will reevaluate your aid package and provide additional financial resources if you qualify.”
### `191f1c195998defe` White Earth Tribal and Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wetcc.edu/wp-content/uploads/2026/06/700.12.01-Financial-Aid-Satisfactory-Academic-Progress-Policy-2.pdf (sha256 7cea0ce4f192)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students who will take more than one term to meet SAP must appeal after every semester until they meet SAP requirements.”
  - sentence: sap_appeal ⟵ “Students who do not meet SAP at the end of an SAP probationary period must submit a SAP appeal. 5.18.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 1; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- Bethany Lutheran College (`ipeds-173142`)
- Hennepin Technical College (`ipeds-173708`)
- University of Northwestern-St Paul (`ipeds-174491`)
- Oak Hills Christian College (`ipeds-174525`)

## Leads: official pages found with no extracted record

- Alexandria Technical & Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Anoka Technical College: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Anoka-Ramsey Community College: admissions_tests, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency
- Augsburg University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, degree_requirements
- Bemidji State University: tuition_fees, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Bethany Global University: tuition_fees, cost_of_attendance
- Bethel University: admissions_tests, merit_scholarships, residency
- Bethlehem College & Seminary: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit
- Carleton College: admissions_tests, transfer_credit
- Central Lakes College-Brainerd: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements, aid_appeals
- Century College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- College of Saint Benedict: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- Concordia College at Moorhead: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, degree_requirements
- Concordia University-Saint Paul: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, degree_requirements
- Crown College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Dakota County Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Dunwoody College of Technology: cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, statewide_articulation, residency, degree_requirements
- Fond du Lac Tribal and Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Gustavus Adolphus College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Hamline University: cost_of_attendance, admissions_tests, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Herzing University-Minneapolis: tuition_fees, cost_of_attendance, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Inver Hills Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Lake Superior College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, degree_requirements
- Leech Lake Tribal College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit
- Macalester College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, degree_requirements
- Martin Luther College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, degree_requirements
- Mayo Clinic College of Medicine and Science: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency
- Metropolitan State University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, degree_requirements
- Minneapolis College of Art and Design: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency
- Minneapolis Community and Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Minnesota North College: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment
- Minnesota State College Southeast: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Minnesota State Community and Technical College: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Minnesota State University Moorhead: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Minnesota State University-Mankato: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, transfer_credit, residency, degree_requirements
- Minnesota West Community and Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, degree_requirements, aid_appeals
- Normandale Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- North Central University: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- North Hennepin Community College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, degree_requirements
- Northland Community and Technical College: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Northwest Technical College: tuition_fees, admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Northwestern Health Sciences University: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation
- Pine Technical & Community College: admissions_tests, merit_scholarships, ap_credit, statewide_articulation, degree_requirements
- Red Lake Nation College: transfer_credit
- Ridgewater College: admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Riverland Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation
- Rochester Community and Technical College: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Saint Cloud State University: admissions_tests, merit_scholarships, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Saint Johns University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- Saint Mary's University of Minnesota: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Saint Paul College: admissions_tests, common_data_set, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- South Central College: tuition_fees, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Southwest Minnesota State University: admissions_tests, common_data_set, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- St Catherine University: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- St Cloud Technical and Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, statewide_articulation, degree_requirements, aid_appeals
- St Olaf College: cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit
- The College of Saint Scholastica: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, degree_requirements
- University of Minnesota-Crookston: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Minnesota-Duluth: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, residency, degree_requirements
- University of Minnesota-Morris: admissions_tests, clep_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- University of Minnesota-Rochester: tuition_fees, cost_of_attendance, admissions_tests, clep_credit, transfer_credit, residency, degree_requirements
- University of Minnesota-Twin Cities: cost_of_attendance, admissions_tests, ap_credit, transfer_credit, residency, degree_requirements
- University of St Thomas: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, degree_requirements
- White Earth Tribal and Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- Winona State University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
