# Review queue — NE (2026-27)

Pages fetched: 1824; failures: 222. Candidates: 174 (56 without issues, 118 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 4 | 7 | 12 | 2 | 4 |
| cost_of_attendance | 0 | 0 | 3 | 5 | 16 | 1 | 4 |
| admissions_tests | 0 | 0 | 0 | 0 | 23 | 2 | 4 |
| common_data_set | 0 | 0 | 0 | 0 | 7 | 18 | 4 |
| merit_scholarships | 0 | 0 | 4 | 0 | 19 | 2 | 4 |
| ap_credit | 0 | 0 | 3 | 3 | 8 | 11 | 4 |
| clep_credit | 0 | 0 | 2 | 2 | 7 | 14 | 4 |
| ib_credit | 0 | 0 | 1 | 1 | 1 | 22 | 4 |
| dual_enrollment | 0 | 0 | 4 | 0 | 13 | 8 | 4 |
| transfer_credit | 0 | 0 | 10 | 0 | 13 | 2 | 4 |
| statewide_articulation | 0 | 0 | 0 | 0 | 7 | 18 | 4 |
| residency | 0 | 0 | 0 | 0 | 11 | 14 | 4 |
| degree_requirements | 0 | 0 | 0 | 0 | 18 | 7 | 4 |
| aid_appeals | 0 | 0 | 0 | 16 | 4 | 5 | 4 |

## Ready for review (56)

### `813a38da745da411` Bellevue University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bellevue.edu/tuition-and-aid/tuition-rates-and-fees/ (sha256 19d3bc4e535b)
- checks: {"columns": 1, "rows": 10}
  - column:Tuition and Fees*: 13293 ⟵ “Tuition and Fees* | $13,293”
  - column:Course Material: 1290 ⟵ “Course Material | $1,290”
  - column:Housing and Meals**: 11235 ⟵ “Housing and Meals** | $11,235”
  - column:Transportation: 1100 ⟵ “Transportation | $1,100”
  - column:Other: 4400 ⟵ “Other | $4,400”
  - column:Tuition and Fees* (2): 13293 ⟵ “Tuition and Fees* | $13,293”
  - column:Course Material (2): 1290 ⟵ “Course Material | $1,290”
  - column:Housing and Meals: 12372 ⟵ “Housing and Meals | $12,372”
  - column:Transportation (2): 1100 ⟵ “Transportation | $1,100”
  - column:Other (2): 4400 ⟵ “Other | $4,400”
### `8b3bb1acdc78e4cf` Central Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://cccneb.edu/programs/high-school/early-college/tuition/ (sha256 05593559fc10)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 118 ⟵ “CCC full tuition/fees rate for 2026-2027 = $102 + $16 = $118/credit hour”
### `d0e28e8bc7f479e0` Central Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://cccneb.edu/programs/academic-transfer/ (sha256 1cfd41068ab7)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “The degree requires 60 credit hours, and most schools require a course grade of C or higher to transfer.”
  - min_grade: C ⟵ “The degree requires 60 credit hours, and most schools require a course grade of C or higher to transfer.”
### `3ad651f0b681c986` Chadron State College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.csc.edu/start/financial-aid/scholarships/ (sha256 96d97fb3899d)
- checks: {"thresholds": null}
  - award_amount_text: $2,000/year ⟵ “Dean Scholars | 3.25 to 3.49 Cumulative Unweighted GPA | $2,000/year”
  - eligibility_summary: 3.25 to 3.49 Cumulative Unweighted GPA ⟵ “Dean Scholars | 3.25 to 3.49 Cumulative Unweighted GPA | $2,000/year”
### `82848a4d9733b2fd` Chadron State College — awards 2026-27 [new] (labeled_entering_class)
- source: https://www.csc.edu/start/financial-aid/scholarships/ (sha256 96d97fb3899d)
- checks: {"thresholds": null}
  - award_amount_text: $2,500/year ⟵ “Innovative Transfer Scholars | 3.0 to 3.94 Cumulative GPA | $2,500/year”
  - eligibility_summary: 3.0 to 3.94 Cumulative GPA ⟵ “Innovative Transfer Scholars | 3.0 to 3.94 Cumulative GPA | $2,500/year”
### `89c26c21a18d8c60` Chadron State College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.csc.edu/start/financial-aid/scholarships/ (sha256 96d97fb3899d)
- checks: {"thresholds": null}
  - award_amount_text: $8,000/year ⟵ “President Scholars | 3.75 to 4.0 Cumulative Unweighted GPA | $8,000/year”
  - eligibility_summary: 3.75 to 4.0 Cumulative Unweighted GPA ⟵ “President Scholars | 3.75 to 4.0 Cumulative Unweighted GPA | $8,000/year”
### `a68b79daeebb8b2a` Chadron State College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.csc.edu/start/financial-aid/scholarships/ (sha256 96d97fb3899d)
- checks: {"thresholds": null}
  - award_amount_text: $4,000/year ⟵ “Eagle Scholars | 3.5 to 3.74 Cumulative Unweighted GPA | $4,000/year”
  - eligibility_summary: 3.5 to 3.74 Cumulative Unweighted GPA ⟵ “Eagle Scholars | 3.5 to 3.74 Cumulative Unweighted GPA | $4,000/year”
### `ee641f868c4781e1` Chadron State College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.csc.edu/start/financial-aid/scholarships/ (sha256 96d97fb3899d)
- checks: {"thresholds": null}
  - award_amount_text: $1,500/year ⟵ “Community Scholars | 3.00 to 3.24 Cumulative Unweighted GPA | $1,500/year”
  - eligibility_summary: 3.00 to 3.24 Cumulative Unweighted GPA ⟵ “Community Scholars | 3.00 to 3.24 Cumulative Unweighted GPA | $1,500/year”
### `m5819e85e7592219` Chadron State College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.csc.edu/admissions/dualcredit/important-information/ (sha256 4ddccc414d00)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - per_credit_hour_charge: 60 ⟵ “Pay a low, flat rate of $60 per credit hour or $180 per three-credit course.  ACE scholarships are available for low-income students who qualify.”
  - eligibility_tier: 3.0 ⟵ “Student had attained a GPA of at least 3.0 (on a 4.0 scale)”
### `07885da35566c1ef` Clarkson College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.clarksoncollege.edu/tuition-financial-aid/cost-of-attendance (sha256 3a1a04dd7807)
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition & Technology Fees: 17284 ⟵ “Tuition & Technology Fees | $17,284 | $17,284 | $17,284”
  - with_parents_or_family:Living Expenses / Housing / Food: 3540 ⟵ “Living Expenses / Housing / Food | $3,540 | $19,290 | $11,640”
  - with_parents_or_family:Books & Supplies: 913 ⟵ “Books & Supplies | $913 | $913 | $913”
  - with_parents_or_family:Transportation: 1773 ⟵ “Transportation | $1,773 | $1,773 | $1,773”
  - with_parents_or_family:Personal Expenses: 933 ⟵ “Personal Expenses | $933 | $933 | $933”
  - with_parents_or_family:Total: 24443 ⟵ “Total | $24,443 | $40,193 | $32,543”
  - off_campus_not_with_family:Tuition & Technology Fees: 17284 ⟵ “Tuition & Technology Fees | $17,284 | $17,284 | $17,284”
  - off_campus_not_with_family:Living Expenses / Housing / Food: 19290 ⟵ “Living Expenses / Housing / Food | $3,540 | $19,290 | $11,640”
  - off_campus_not_with_family:Books & Supplies: 913 ⟵ “Books & Supplies | $913 | $913 | $913”
  - off_campus_not_with_family:Transportation: 1773 ⟵ “Transportation | $1,773 | $1,773 | $1,773”
  - off_campus_not_with_family:Personal Expenses: 933 ⟵ “Personal Expenses | $933 | $933 | $933”
  - off_campus_not_with_family:Total: 40193 ⟵ “Total | $24,443 | $40,193 | $32,543”
  - on_campus:Tuition & Technology Fees: 17284 ⟵ “Tuition & Technology Fees | $17,284 | $17,284 | $17,284”
  - on_campus:Living Expenses / Housing / Food: 11640 ⟵ “Living Expenses / Housing / Food | $3,540 | $19,290 | $11,640”
  - on_campus:Books & Supplies: 913 ⟵ “Books & Supplies | $913 | $913 | $913”
  - on_campus:Transportation: 1773 ⟵ “Transportation | $1,773 | $1,773 | $1,773”
  - on_campus:Personal Expenses: 933 ⟵ “Personal Expenses | $933 | $933 | $933”
  - on_campus:Total: 32543 ⟵ “Total | $24,443 | $40,193 | $32,543”
### `fba6993245e930ec` Clarkson College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.clarksoncollege.edu/enrollment/transfer-resources (sha256 db74baaff062)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “It is important for students transferring credit to Clarkson College to submit a final official transcript after completing all coursework from other accredited institutions and receive a grade of "C-" or higher.”
### `m5c320c0bdf546ef` Concordia University-Nebraska — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.cune.edu/application/files/4217/0438/9068/Dual_Credit_Policies_Abbr..pdf (sha256 d4c6e6bcff2f)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 2, "tiers": 2}
  - per_credit_hour_charge: 300 ⟵ “Subject Area Mastery Scholarships: Concordia Nebraska provides scholarships up to $300/credit in any accredited program for teachers to earn the requisite graduate hours to offer dual credit in their content area.”
  - eligibility_tier: 3.0 ⟵ “Juniors/Seniors: 3.0 GPA automatic or 2.50-2.99 GPA with parent permission”
  - eligibility_tier: 3.0 ⟵ “To be eligible to take dual credit through CUNE, juniors and seniors must have a minimum 3.0 GPA, or a 2.50-2.99 GPA”
  - eligibility_tier: 3.0 ⟵ “with parent permission. Freshmen and sophomores with a minimum 3.0 GPA are eligible by parent permission, with the”
  - per_credit_hour_charge: 10 ⟵ “registration window will be assessed a $10/credit late fee. Students may not register after the final late registration”
### `8c08387373e9e820` Concordia University-Nebraska — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.cune.edu/transfer-concordia/transferring-credits-concordia-and-credit-exam (sha256 0971f43d0eb2)
- checks: {"fields": ["min_grade", "residency_requirement_credits"]}
  - min_grade: C- ⟵ “Only courses with a grade of C- or above will be accepted for transfer credit College Level Advanced Placement (CLEP), Advanced Placement (AP), International Baccalaureate (IB) and Military Credits are reviewed and considered for equivalent placement at Concordia.”
  - residency_requirement_credits: 30 ⟵ “Students seeking a bachelor's degree must complete a minimum of 30 hours in residence, at least 15 of which must be in their major.”
### `1677ad36c91ab6b1` Hastings College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hastings.edu/admissions/cost-aid/types-of-aid/ (sha256 826d0e306af3)
- checks: {"thresholds": {"gpa_min": 3.9}}
  - gpa_requirement: 3.90 and above ⟵ “Crimson | 3.90 and above | $19,000”
### `489db35f3b3ee442` Hastings College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hastings.edu/admissions/cost-aid/types-of-aid/ (sha256 826d0e306af3)
- checks: {"thresholds": null}
  - gpa_requirement: 3.75-3.899 ⟵ “Ambassador | 3.75-3.899 | $17,000”
### `5bf7c6511224add6` Hastings College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hastings.edu/admissions/cost-aid/types-of-aid/ (sha256 826d0e306af3)
- checks: {"thresholds": null}
  - gpa_requirement: < 2.64 ⟵ “Student Success | < 2.64 | $11,000”
### `7346f71d075f9159` Hastings College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hastings.edu/admissions/cost-aid/types-of-aid/ (sha256 826d0e306af3)
- checks: {"thresholds": null}
  - gpa_requirement: 2.65-2.999 ⟵ “Pro Rege | 2.65-2.999 | $13,000”
### `ecb4c3feefa15089` Hastings College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hastings.edu/admissions/cost-aid/types-of-aid/ (sha256 826d0e306af3)
- checks: {"thresholds": null}
  - gpa_requirement: 3.00-3.749 ⟵ “Ringland | 3.00-3.749 | $16,000”
### `4d165be2c57eea09` Hastings College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.hastings.edu/admissions/cost-aid/cost-of-attendance/ (sha256 cd5e959fe3e5)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition & Fees: 41244 ⟵ “Tuition & Fees | $20,622 | $41,244”
  - column:Housing & Food: 13200 ⟵ “Housing & Food | $6,600 | $13,200”
  - column:Total: 54444 ⟵ “Total | $27,222 | $54,444”
### `3c1d796b0e9df6f6` Metropolitan Community College Area — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.mccneb.edu/CMSPages/GetAzureFile.aspx?path=~%5Cmcc_13%5Cmedia%5Cpdfs-and-docs%5Cprior-learning-assessment%5Cclep_credit-equivalency_fall-2025.pdf&hash=6e4c05d645d12062227a5c4edf944a9ffe73bf4921d646ae92a36aefe5cf8c64 (sha256 43111bd5e81e)
- checks: {"distinct_exams": 25, "equivalencies": 28, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                 50              4.5               POLS 2050”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and                 50                 4.5             PSYC 1120”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology             50                 4.5             PSYC 1010”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology             50                 4.5             SOCI 1010”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I:           50                 4.5             HIST 1110”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II:          50                 4.5             HIST 1120”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature – if             50              9.0            ENGL 2510 & ENGL”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting            50                 4.5             ENGL 2450”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition               50                 4.5             ENGL 1010”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature               50                 4.5             ENGL 2620”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                   50                 6.0             HUMS 1100”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                   50              6.0               BIOS 1010”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                   50              7.5              MATH 2410”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                   50              6.0              CHEM 1010”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                50              4.5              MATH 1425”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics              50              4.5              MATH 1240”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences               50              6.0               SCIE 1010”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                 50              4.5              MATH 1425”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting             50              8.0            ACCT 1100 & ACCT”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law          50                 4.5             BSAD 1100”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management           50                 4.5             BSAD 2100”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing          50                 4.5             BSAD 1010”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language I               50              7.5               FREN 1110”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language II               50              7.5               FREN 1120”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language I                50              7.5              GERM 1010”
  - … 3 more rows
### `97cc803520baf3a8` Metropolitan Community College Area — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.mccneb.edu/CMSPages/GetAzureFile.aspx?path=~%5Cmcc_13%5Cmedia%5Cpdfs-and-docs%5Cprior-learning-assessment%5Cap_credit-equivalency-fall-2025.pdf&hash=9df19141f294b2dcfc779b2b7bb553a5d451785a41cc5fad9bb5f04ecc1133a3 (sha256 18c711b92000)
- checks: {"distinct_exams": 34, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design             3          4.5                 ARTS 1020”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design             3          4.5                 ARTS 1030”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                        3          4.5                 ARTS 1010”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                    3          4.5                 ARTS 1110”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                   3          4.5                 MUSC 1050”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and          3           4.5                 ENGL 1010”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and        3           4.5                 ENGL 2450”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies      3           4.5                 HIST 1050”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History              3           4.5                 HIST 2050”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography               3           4.5                 GEOG 1050”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                3           4.5                 ECON 1100”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                    3           4.5                 PSYC 1010”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government      3           4.5                 POLS 2050”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History         3           9.0                 HIST 1010 and HIST”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History: Modern         3           9.0                 HIST 1110 and HIST”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                        3               7.5                 MATH 2410”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                        3               15.0                MATH 2410 & MATH”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                 3               4.5                 INFO 1499”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles        3               4.5                 INFO 1020”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus                        3               5.0                 MATH 1425”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                         3               4.5                 MATH 1410”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                            3               6.0                 BIOS 1010”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                          3               6.0                 CHEM 1010”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science              3               4.5                 BIOS 1250”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics I: Algebra-Based           3               7.5                 PHYS 110A-B-C”
  - … 9 more rows
### `b61d5d5ce622065d` Mid-Plains Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.mpcc.edu/admissions/transfer/advanced_placement_transfer_credit.pdf (sha256 09be51a9426f)
- checks: {"distinct_exams": 8, "equivalencies": 8, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                                      ARTS 1050 - Intro to Art History & Criticism I                           4, 5          3”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                                        CHEM 1090 - General Chemistry I                                          3, 4, 5       4”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics - Macro                                ECON 2110 - Principles of Economics - Macro                              4, 5          3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics - Micro                                ECON 2120 - Principles of Economics - Micro                              4, 5          3”
  - equivalencies[AP-CALCULUS-AB|5]:  ⟵ “Mathematics - Calculus AB                        MATH 1600 - Analytic Geometry and Calculus I                             3, 4, 5       5”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                                     MUSC 1300 - Music Theory 1                                               4, 5          3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                       PSYC 1810 - Introduction to Psychology                                   4, 5          3”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                                       MATH 1200 - Elements of Statistics                                       3, 4, 5       3”
### `m0fa39471cec47cf` Mid-Plains Community College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.mpcc.edu/course-catalog/programs/academic-transfer/ (sha256 cd5ba759a745)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - min_grade: C ⟵ “Most colleges only accept classes with a grade of “C” or better and will not transfer in more than 66 credits from a two-year college.”
  - max_transfer_credits: 60 ⟵ “Most four-year colleges will accept up to 60 semester credit hours of freshman and sophomore-level credits earned at a community college and require at least a “C” in each course transferred.”
### `mbb34edae3be9e65` Nebraska College of Technical Agriculture — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://ncta.unl.edu/academics/dual-credit-high-school-students/ (sha256 a347bf6a5806)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 1}
  - per_credit_hour_charge: 78 ⟵ “NCTA's reduced tuition for dual credit is $78.00 per credit hour.”
  - eligibility_tier: 3.0 ⟵ “Interested students should have a 3.0 GPA. If a  student does not meet this requirement, he or she will need a counselor's approval to take a dual credit course.”
  - per_credit_hour_charge: 78 ⟵ “Reduced tuition ($78.00 per credit hour)”
  - per_credit_hour_charge: 78 ⟵ “NCTA's reduced tuition for dual credit is $78.00 per credit hour.”
### `03005a86b805b2ed` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $1,000, renewable ⟵ “Alumni Legacy Scholarship | $1,000, renewable | Not applicable”
### `3ca1419880ab1eb7` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “College Possible | $1,000 | Not applicable”
### `46cd19b2590beaec` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $3,000 ⟵ “Theatre Scholarships | $500 to $3,000 | Audition dates vary”
### `66ffebe01d7fe270` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: 100% of your WHA tuition ⟵ “Wesleyan Honors Academy Scholarship | 100% of your WHA tuition | Not applicable”
### `8048a53162149a5d` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $26,000 ⟵ “Presidents | $26,000 | 3.5-3.74”
  - gpa_requirement: 3.5-3.74 ⟵ “Presidents | $26,000 | 3.5-3.74”
### `88d1242a436372b2` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $3,000 ⟵ “Music Ensemble Participation Scholarship | $500 to $3,000 | Audition dates vary”
### `9dd130bb464d4c89` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $3,000 ⟵ “The Marshall Music Scholarship | $500 to $3,000 | Audition dates vary”
### `b0f3ff01707db115` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $24,000 ⟵ “Black & Gold | $24,000 | 3.0-3.49”
  - gpa_requirement: 3.0-3.49 ⟵ “Black & Gold | $24,000 | 3.0-3.49”
### `b70788bb806c9348` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $3,000 ⟵ “The Bennett Music Scholarship | $500 to $3,000 | Audition dates vary”
### `c7fc88885a1cd070` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: Full tuition, fees, room and board ⟵ “Huge-NWU Scholarship | Full tuition, fees, room and board | December 1, 2026”
### `d622a8c450de9970` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $2,000, renewable ⟵ “Great Plains United Methodist Scholarship | $500 to $2,000, renewable | Not applicable”
### `da724c1a0b208058` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: up to $20,000 ⟵ “Archway | up to $20,000 | up to 2.99”
  - gpa_requirement: up to 2.99 ⟵ “Archway | up to $20,000 | up to 2.99”
### `dc0e135ebb8a8a2f` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $3,000 ⟵ “The Fosbury Music Scholarship | $500 to $3,000 | Audition dates vary”
### `ddf1904a91c78e93` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “TeamMates Scholarship | $1,000 | Not applicable”
### `e7bd9507a2a7e4c9` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $3,000 ⟵ “The Harrod Music Scholarship | $500 to $3,000 | Audition dates vary”
### `f5e56be9c230a353` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/first-year-scholarships (sha256 8f0f1ea22fa0)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Upward Bound | $1,000 | Not applicable”
### `m090236aaf068021` Nebraska Wesleyan University — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.nebrwesleyan.edu/cc/2026-2027/transfer-student (sha256 93aaac03a943)
- checks: {"fields": ["max_transfer_credits", "min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “Transfer classes with grades of “C-” or above are evaluated on a course-by-course basis.”
  - min_grade: C- ⟵ “The following are required: Application for admission - complete NWU's online app or the Common App Good standing at current college or university (or institution last attended if no longer enrolled) Minimum 2.00 GPA (calculated from all institutions attended) Transferring Credit: NWU requires a minimum grade of C- or above.”
  - max_transfer_credits: 64 ⟵ “No more than 64 semester credit hours will transfer from two-year institutions.”
### `04124544aea4f55a` Northeast Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/tuition/ (sha256 25a77a8a48c7)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 4650 ⟵ “Tuition | $3,360 | $3,360 | $4,650”
  - on_campus:Fees: 630 ⟵ “Fees | $630 | $630 | $630”
  - on_campus:Loan Fees (if applicable): 53 ⟵ “Loan Fees (if applicable) | $53 | $53 | $53”
  - on_campus:Books (est.): 1142 ⟵ “Books (est.) | $1,145 | $1,142 | $1,142”
  - on_campus:Living Expenses - On CampusHousing and Food*: 10546 ⟵ “Living Expenses - On CampusHousing and Food* | $10,546 | $10,546 | $10,546”
  - on_campus:Travel: 832 ⟵ “Travel | $832 | $832 | $832”
  - on_campus:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - on_campus:Total: 18978 ⟵ “Total | $17,688 | $17,688 | $18,978”
### `4dd889f605c7cb47` Northeast Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://northeast.edu/support-services/advisement/transfer-guide (sha256 18864a175e8a)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “The generally accepted requirements for transfer to another college include: Grades of "C" or higher in a transferable course.”
### `19ad858c7eceb31f` Southeast Community College Area — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.southeast.edu/admissions/admissions-requirements.php (sha256 9b7bb16364c2)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Department of Education, will be evaluated to determine if the student meets college entrance requirements through evidence of three (3) or more hours of transfer credit from an accredited postsecondary institution with a grade of “C” or better in each of the areas of English and/or math.”
### `mac84953dacc6fc2` University of Nebraska at Kearney — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.unk.edu/undergraduate/admissions/transfer-credit/ (sha256 776aace2a293)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 66 ⟵ “Total semester credit hours transferred from each institution previously attended are recorded on the student's UNK transcript. (Note: A maximum of 66 semester credit hours may be transferred from two-year junior or community colleges.) UNK does not issue copies of another institution's transcript.”
  - max_transfer_credits: 66 ⟵ “Total semester credit hours transferred from each institution previously attended are recorded on the student's UNK transcript. (Note: A maximum of 66 semester credit hours may be transferred from two-year junior or community colleges.) 6.”
### `60517bba4da926fa` University of Nebraska at Omaha — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.unomaha.edu/registrar/students/before-you-enroll/transfer-credit/clep-credit.php (sha256 834ec246a165)
- checks: {"distinct_exams": 20, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50+]:  ⟵ “American Government | PSCI 1100 | 50+ | 3”
  - equivalencies[CLEP-BIOLOGY|55+]:  ⟵ “Biology | BIOL 1020 | 55+ | 4”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus | MATH 1950 | 50+ | 5”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|45-51 52+]:  ⟵ “College Algebra | MATH 1220 MATH 1320 | 45-51 52+ | 3 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50+]:  ⟵ “College Mathematics | Quantitative Literacy MavEd General Education Equivalent | 50+ | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50+]:  ⟵ “Financial Accounting | ACCT Lower Level Elective Credit | 50+ | 3”
  - equivalencies[CLEP-CHEMISTRY|50+]:  ⟵ “General Chemistry * | CHEM 1180, CHEM 1184 | 50+ | 3 OR 4”
  - equivalencies[CLEP-CHEMISTRY|50+]:  ⟵ “General Chemistry * | CHEM 1190 | 50+ | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50+]:  ⟵ “Human Growth and Development | Social Science MavEd General Education Equivalent | 50+ | 3”
  - equivalencies[CLEP-HUMANITIES|50+]:  ⟵ “Humanities (General Exam) | HUMN Lower Level Elective Credit | 50+ | 6”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50+]:  ⟵ “Introduction to Educational Psychology | Social Science MavEd General Education Equivalent | 50+ | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|53+]:  ⟵ “Introductory Psychology | PSYC 1010 | 53+ | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50+]:  ⟵ “Introductory Sociology | SOC 1010 | 50+ | 3”
  - equivalencies[CLEP-NATURAL-SCIENCES|50+]:  ⟵ “Natural Sciences | Natural Science Lecture MavEd General Education Equivalent | 50+ | 6”
  - equivalencies[CLEP-PRECALCULUS|50+]:  ⟵ “Pre-Calculus | MATH 1340 | 50+ | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50+]:  ⟵ “Principles of Macroeconomics | ECON 2220 | 50+ | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50+]:  ⟵ “Principles of Management | MGMT Lower Level Elective Credit | 50+ | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50+]:  ⟵ “Principles of Marketing | MKT 2210 | 50+ | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50+]:  ⟵ “Principles of Microeconomics | ECON 2200 | 50+ | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50+]:  ⟵ “Western Civilization I | Humanities OR Cultural Knowledge MavEd General Education Equivalent** (Previously Global Diversity/Humanities Fine Art General Education elective) | 50+ | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50+]:  ⟵ “Western Civilization II | Humanities OR Cultural Knowledge MavEd General Education Equivalent** (Previously Global Diversity/Humanities Fine Art General Education elective) | 50+ | 3”
### `f4e51822b49478cd` University of Nebraska at Omaha — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.unomaha.edu/registrar/students/before-you-enroll/transfer-credit/international-baccalaureate-program.php (sha256 d92a11d1d7a6)
- checks: {"distinct_exams": 22, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5-7]:  ⟵ “Anthropology | SL | 5-7 | 3 | ANTH Lower Level Elective Credit”
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “Biology | SL | 5-7 | 5 | BIOL 1020”
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “Biology | HL | 5-7 | 5 & 3 | BIOL 1020 & BIOL Lower Level Elective Credit”
  - equivalencies[IB-CHEMISTRY|5-7]:  ⟵ “Chemistry | HL | 5-7 | 4 & 4 | CHEM 1180 & 1184 & CHEM 1190 & 1194”
  - equivalencies[IB-ECONOMICS|4-7]:  ⟵ “Economics | SL | 4-7 | 5 | ECON Lower Level Elective Credit”
  - equivalencies[IB-FRENCH-SL|SL 5-7]:  ⟵ “French(Ab initio or French B SL) | SL | 5-7 | 9 | FREN 1210, FREN 1220, and FREN 2210”
  - equivalencies[IB-FRENCH-HL|HL 5-7]:  ⟵ “French(French B HL) | HL | 5-7 | 15 | FREN 1210, FREN 1220, FREN 2210, FREN 2220, and FREN 2240”
  - equivalencies[IB-GEOGRAPHY|5-7]:  ⟵ “Geography | SL | 5-7 | 3 | GEOG 1020”
  - equivalencies[IB-GEOGRAPHY|5-7]:  ⟵ “Geography | HL | 5-7 | 3 & 3 | GEOG 1020 & GEOG Lower Level Elective Credit”
  - equivalencies[IB-GERMAN-SL|SL 5-7]:  ⟵ “German(Ab initio or German B SL) | SL | 5-7 | 9 | GERM 1210, GERM 1220, and GERM 2210”
  - equivalencies[IB-GERMAN-HL|HL 5-7]:  ⟵ “German(German B HL) | HL | 5-7 | 15 | GERM 1210, GERM 1220, GERM 2210, GERM 2220, and GERM 2240”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History | SL | 5-7 | 3 | HIST Lower Level Elective Credit”
  - equivalencies[IB-LATIN-SL|SL 5-7]:  ⟵ “Latin(Ab initio or Latin B SL) | SL | 5-7 | 3 | FLNG Lower Level Elective Credit”
  - equivalencies[IB-LATIN-HL|HL 5-7]:  ⟵ “Latin(Latin B HL) | HL | 5-7 | 6 | FLNG Lower Level Elective Credit”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|5-7]:  ⟵ “Math Analysis and Approaches | SL | 5-7 | 5 | MATH 1340”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|5-7]:  ⟵ “Math Analysis and Approaches | HL | 5-7 | 5 | MATH 1950”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|5-7]:  ⟵ “Math Applications and Interpretations | SL | 5-7 | 5 | MATH 1340”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|5-7]:  ⟵ “Math Applications and Interpretations | HL | 5-7 | 5 | MATH 1950”
  - equivalencies[IB-MUSIC|4-7]:  ⟵ “Music | SL | 4-7 | 4 | MUS Lower Level Elective Credit”
  - equivalencies[IB-PHILOSOPHY|5-7]:  ⟵ “Philosophy | SL | 5-7 | 3 | PHIL 1010”
  - equivalencies[IB-PHILOSOPHY|5-7]:  ⟵ “Philosophy | HL | 5-7 | 3 & 3 | PHIL 1010 & PHIL Lower Level Elective Credit”
  - equivalencies[IB-PHILOSOPHY|PASS]:  ⟵ “Philosophy | TOK | PASS | 3 | PHIL 1210”
  - equivalencies[IB-PHYSICS|5-7]:  ⟵ “Physics | SL | 5-7 | 3 | PHYS Lower Level Elective Credit”
  - equivalencies[IB-PSYCHOLOGY|5-7]:  ⟵ “Psychology | SL | 5-7 | 3 | PSYC 1010”
  - equivalencies[IB-PSYCHOLOGY|5-7]:  ⟵ “Psychology | HL | 5-7 | 3 & 3 | PSYC 1010 &PSYC Lower Level Elective Credit”
  - … 4 more rows
### `9e868d2251ec2d9b` University of Nebraska at Omaha — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.unomaha.edu/undergraduate-admissions/apply/transfer/transferring-credit.php (sha256 f73994b8806d)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C- ⟵ “A grade of C- or higher must be earned in a course for it to be accepted for transfer.”
  - max_transfer_credits: 64 ⟵ “A maximum of 64 semester hours can be transferred to UNO from a two-year institution.”
### `68597830bf5ebf95` University of Nebraska-Lincoln — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/2026-2027/ (sha256 cd3b8a5402b0)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 11472 ⟵ “Tuition & Fees | $11,472 | $31,542”
  - on_campus:Housing & Food: 13950 ⟵ “Housing & Food | $13,950 | $13,950”
  - on_campus:Books & Supplies: 1128 ⟵ “Books & Supplies | $1,128 | $1,128”
  - on_campus:Personal Expenses: 2324 ⟵ “Personal Expenses | $2,324 | $2,324”
  - on_campus:Loan Fees (if applicable): 64 ⟵ “Loan Fees (if applicable) | $64 | $64”
  - on_campus:Total: 28938 ⟵ “Total | $28,938 | $49,008”
### `8df3e2d0de8a1a94` University of Nebraska-Lincoln — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/2026-2027/ (sha256 cd3b8a5402b0)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 31542 ⟵ “Tuition & Fees | $11,472 | $31,542”
  - on_campus:Housing & Food: 13950 ⟵ “Housing & Food | $13,950 | $13,950”
  - on_campus:Books & Supplies: 1128 ⟵ “Books & Supplies | $1,128 | $1,128”
  - on_campus:Personal Expenses: 2324 ⟵ “Personal Expenses | $2,324 | $2,324”
  - on_campus:Loan Fees (if applicable): 64 ⟵ “Loan Fees (if applicable) | $64 | $64”
  - on_campus:Total: 49008 ⟵ “Total | $28,938 | $49,008”
### `d4203312b9c9bcd0` Wayne State College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.wsc.edu/records-registration/credit-by-exam (sha256 2612d2dd50aa)
- checks: {"distinct_exams": 24, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ART 244 Art History Survey I | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIO 102 Biology for General Studies (no lab required) | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MAT 140 Calculus I | 5”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MAT 240 Calculus II | 5”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHE 102 Chemistry for General Studies (no lab required) | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | Computer science elective (CSC course) | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CSC 160 Programming Fundamentals II | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics - Macro | 3 | ECO 202 Principles of Macroeconomics | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics - Micro | 3 | ECO 203 Principles of Microeconomics | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Lang/Comp | 3 | ENG 102 Composition Skills | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Lit/Comp | 3 | ENG 102 Composition Skills and ENG 150 Topics in Literature | 6”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIS 171 World Civilications II | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French | 3 | FRE 110 Elementary French I and FRE 120 Elementary French II | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German | 3 | GER 110 Elementary German I and GER 120 Elementary German II | 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | Geography elective (GEO course) | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | 3 | MLC 110 Elementary Language I and MLC 120 Elementary Language II | 6”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | 3 | MLC 110 Elementary Language I and MLC 120 Elementary Language II | 6”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | MUS 101 Music Theory I | 3”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics I | 3 | PHY 201 General Physics I and PHY 321 Physics Laboratory I | 4”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSY 101 General Psychology | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish | 3 | SPA 110 Elementary Spanish I and SPA 120 Elementary Spanish II | 6”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | MAT 180 Applied Probability and Statistics | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “U.S. History | 3 | HIS 150 History of the United States for General Studies, and History elective (HIS course) | 6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History | 3 | HIS 120 World History for General Studies | 3”
### `m28f75f50e04985c` Wayne State College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.wsc.edu/transfer (sha256 103148eccba8)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 3}
  - max_transfer_credits: 66 ⟵ “In general, you may transfer up to 66 credit hours from any accredited community college (unless you are following a transfer pathway that allows for additional transfer credits).”
  - min_grade: C- ⟵ “Note: Only transfer grades of "C-" or above will be accepted.”
  - min_grade: C- ⟵ “Note: Only transfer grades of "C-" or above will be accepted.”
### `04d501be1fc82313` York University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.york.edu/financial-aid/scholarships.php (sha256 120529fe4946)
- checks: {"thresholds": null}
  - test_requirement: Larsen Scholarship(GPA 3.50-3.74/ACT 30-32/SAT 1390-1480) ⟵ “Larsen Scholarship(GPA 3.50-3.74/ACT 30-32/SAT 1390-1480) | $5,000”
  - award_amount_text: $5,000 ⟵ “Larsen Scholarship(GPA 3.50-3.74/ACT 30-32/SAT 1390-1480) | $5,000”
### `74ccbeef22f8046a` York University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.york.edu/financial-aid/scholarships.php (sha256 120529fe4946)
- checks: {"thresholds": null}
  - test_requirement: ​Childress Scholarship(GPA 3.25-3.49/ACT 27-29/SAT 1280-1380) ⟵ “​Childress Scholarship(GPA 3.25-3.49/ACT 27-29/SAT 1280-1380) | $4,000”
  - award_amount_text: $4,000 ⟵ “​Childress Scholarship(GPA 3.25-3.49/ACT 27-29/SAT 1280-1380) | $4,000”
### `8ab96bb7f25b0713` York University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.york.edu/financial-aid/scholarships.php (sha256 120529fe4946)
- checks: {"thresholds": null}
  - test_requirement: York Scholarship(GPA 3.00-3.24/ACT 24-26/SAT 1160-1270) ⟵ “York Scholarship(GPA 3.00-3.24/ACT 24-26/SAT 1160-1270) | $3,500”
  - award_amount_text: $3,500 ⟵ “York Scholarship(GPA 3.00-3.24/ACT 24-26/SAT 1160-1270) | $3,500”
### `ca069a94b7f07609` York University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.york.edu/financial-aid/scholarships.php (sha256 120529fe4946)
- checks: {"thresholds": null}
  - test_requirement: Trustees Scholarship(GPA 3.75+/ACT 33-36/SAT 1490-1600) ⟵ “Trustees Scholarship(GPA 3.75+/ACT 33-36/SAT 1490-1600) | $6,500”
  - award_amount_text: $6,500 ⟵ “Trustees Scholarship(GPA 3.75+/ACT 33-36/SAT 1490-1600) | $6,500”

## Exceptions (118)

### `9ed3ebd76f737de0` Central Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://cccneb.edu/wp-content/uploads/2026/06/2025-26-prof-judgment-income-reduction.pdf (sha256 dadec3246cbc)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “2025-26 Professional Judgment Income Reduction Request Student Name _________________________________________ CCC ID# _____________________________ A 2025-26 Free Application for Federal Student Aid (FAFSA) result must be received before an income adjustment will be considered due to a change in an economic situation.”
### `b0ab89f767995c02` Central Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://cccneb.edu/admissions-aid/financial-aid/student-rights/sap/ (sha256 2e71963e049f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals: A student may appeal their financial aid suspension if extenuating circumstances (death of a family member, injury or illness of the student, or other special circumstances) exist.”
### `13328fef1b3c44bb` Clarkson College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.clarksoncollege.edu/academic-information-policies/professional-judgement (sha256 4e461fa25c10)
- issues: semantic_review_required, conflicting_sources:https://www.clarksoncollege.edu/tuition-financial-aid/financial-aid/applying-for-financial-aid/index
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Professional judgment is considered only on a case-by-case basis when the student can demonstrate the existence of a special circumstance.”
  - sentence: professional_judgment ⟵ “The Financial Aid and Scholarships Office Director and/or Financial Aid and Scholarships Counselors must complete the verification process on the student’s FAFSA prior to exercising professional judgment, regardless of whether the application was selected for verification by the Central Processing System (CPS) or by the institution.”
  - sentence: professional_judgment ⟵ “Procedure: The student must submit a written request for professional judgment/special circumstance review to his or her Financial Aid Counselor.”
  - sentence: professional_judgment ⟵ “The financial aid professional judgment/special circumstance appeal process does not fall under the College’s grievance policy; therefore, in accordance with the HEA, the Director of Financial Aid and Scholarships’ decision is final.”
### `35a5f5b29affc10d` Clarkson College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clarksoncollege.edu/tuition-financial-aid/financial-aid/applying-for-financial-aid/index (sha256 8548d2474e0f)
- issues: semantic_review_required, conflicting_sources:https://catalog.clarksoncollege.edu/academic-information-policies/professional-judgement
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Clarkson College Financial Aid counselors may use professional judgment to adjust a student’s cost of attendance or financial aid award based on special or unusual circumstances.”
### `7935a401a9b73001` Clarkson College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clarksoncollege.edu/tuition-financial-aid/frequently-asked-questions (sha256 27330f3c744e)
- issues: semantic_review_required, conflicting_sources:https://www.clarksoncollege.edu/tuition-financial-aid/financial-aid/applying-for-financial-aid/index
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you feel there has been a significant income or family change since you completed the FAFSA, a special circumstance form can be submitted with supporting documents.”
### `a48cc94ed7c895cb` Clarkson College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clarksoncollege.edu/tuition-financial-aid/financial-aid/applying-for-financial-aid/index (sha256 8548d2474e0f)
- issues: semantic_review_required, conflicting_sources:https://www.clarksoncollege.edu/tuition-financial-aid/frequently-asked-questions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students may request a special circumstance appeal on a case-by-case basis.”
### `d42ee990b2152aa7` Clarkson College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.clarksoncollege.edu/academic-information-policies/satisfactory-academic-progress-for-FA (sha256 89ccd050d865)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students must submit the Financial Aid Satisfactory Academic Progress Appeal form sent with the notice of suspension.”
### `017f326ac5877ecf` Concordia University-Nebraska — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cune.edu/today/students/academic-support/academic-policies/satisfactory-academic-progress-policy (sha256 4e7aa3ab8568)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal Any student wishing to appeal the suspension of his/her financial aid eligibility, based on provisions in this "Satisfactory Academic Progress Policy," may appeal by completing the financial aid suspension appeal form and submitting the appeal to the financial aid office of Concordia University.”
  - sentence: sap_appeal ⟵ “If SAP appeal is approved, the school has determined that the student: Will be able to make SAP standards by the end of next payment period or Will be placed on an established academic plan that will ensure the student is able to meet SAP standards by a specific point in time.”
### `28ac6a7d280754df` Concordia University-Nebraska — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cune.edu/undergraduate-costs/fafsa/fafsa-professional-judgement (sha256 4334c8514cc5)
- issues: semantic_review_required, conflicting_sources:https://www.cune.edu/undergraduate-costs/fafsa
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: professional_judgment ⟵ “A professional judgment will be determined, and the student will be notified via email.”
  - sentence: professional_judgment ⟵ “Required Documentation for all Professional Judgment Requests All Professional Judgment Requests must include the following documents.”
  - sentence: professional_judgment ⟵ “Additional documents may be required depending upon the type of circumstance for which you are requesting professional judgment review.”
  - sentence: professional_judgment ⟵ “Please review the Professional Judgment Request Form for additional documents required.”
  - sentence: professional_judgment ⟵ “Professional Judgment Request Form (PDF) Letter of Explanation - Write a detailed description of the special circumstances that affect your financial situation.”
  - sentence: professional_judgment ⟵ “Additional documents specific to your special circumstance – See the professional judgment request form for additional documents you may need to submit.”
### `bfb1a365f2763dcf` Concordia University-Nebraska — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cune.edu/undergraduate-costs/fafsa (sha256 0565e415ddce)
- issues: semantic_review_required, conflicting_sources:https://www.cune.edu/undergraduate-costs/fafsa/fafsa-professional-judgement
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Renew your FAFSA FAFSA Professional Judgment You may apply for adjustments to your FAFSA award amount based on special circumstances.”
  - sentence: professional_judgment ⟵ “Apply for professional judgement 800 N.”
### `e8dd1e842576e2a5` Concordia University-Nebraska — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cune.edu/undergraduate-costs/fafsa/fafsa-professional-judgement (sha256 4334c8514cc5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to financial changes to the household which affect the financial data recorded on the student’s FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to conditions that justify a student being considered independent rather than dependent.”
  - sentence: need_based_special_circumstances ⟵ “However, none of the conditions listed below, singly or in combination, qualify as unusual circumstances meriting a dependency override.”
### `e927bd2ac6ce2fea` Concordia University-Nebraska — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.cune.edu/undergraduate-costs/fafsa/fafsa-renewal (sha256 809d26c5e9a3)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Verify your FAFSA FAFSA Professional Judgment You may apply for adjustments to your FAFSA award amount based on special circumstances.”
  - sentence: professional_judgment ⟵ “Apply for professional judgement 800 N.”
### `2c71a142dd0268d0` Concordia University-Nebraska — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cune.edu/undergraduate-costs (sha256 806d52dae5a1)
- issues: multiple_total_rows, conflicting_sources:https://www.cune.edu/today/students/student-financial-services/tuition-indirect-costs,https://www.cune.edu/undergraduate-costs
- checks: {"columns": 1, "rows": 7}
  - column:Tuition: 43000 ⟵ “Tuition | $43,000”
  - column:Basic Housing: 5250 ⟵ “Basic Housing | $5,250”
  - column:Meal Plan: 6700 ⟵ “Meal Plan | $6,700”
  - column:Student Services Fee: 800 ⟵ “Student Services Fee | $800”
  - column:Student Accident Insurance: 160 ⟵ “Student Accident Insurance | $160”
  - column:Total Tuition, Housing and Food: 55910 ⟵ “Total Tuition, Housing and Food | $55,910”
  - column:Average Total Cost: 21410 ⟵ “Average Total Cost | $21,410”
### `475b5b0b45bc6859` Concordia University-Nebraska — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cune.edu/undergraduate-costs (sha256 947d33a04e8a)
- issues: multiple_total_rows, conflicting_sources:https://www.cune.edu/today/students/student-financial-services/tuition-indirect-costs,https://www.cune.edu/undergraduate-costs
- checks: {"columns": 1, "rows": 7}
  - column:Tuition: 43000 ⟵ “Tuition | $43,000”
  - column:Basic Housing: 5250 ⟵ “Basic Housing | $5,250”
  - column:Meal Plan: 6700 ⟵ “Meal Plan | $6,700”
  - column:Student Services Fee: 800 ⟵ “Student Services Fee | $800”
  - column:Student Accident Insurance: 160 ⟵ “Student Accident Insurance | $160”
  - column:Total Tuition, Housing and Food: 55910 ⟵ “Total Tuition, Housing and Food | $55,910”
  - column:Average Total Cost: 21410 ⟵ “Average Total Cost | $21,410”
### `6fae82442622fdab` Concordia University-Nebraska — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cune.edu/today/students/student-financial-services/tuition-indirect-costs (sha256 41f92186b9fb)
- issues: conflicting_sources:https://www.cune.edu/undergraduate-costs,https://www.cune.edu/undergraduate-costs
- checks: {"columns": 3, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition: 43000 ⟵ “Tuition | $43,000 | $43,000 | $43,000”
  - on_campus:Fees: 960 ⟵ “Fees | $960 | $960 | $960”
  - on_campus:Housing and Food: 11950 ⟵ “Housing and Food | $11,950 | $0 | $0”
  - on_campus:Total Direct Costs: 55910 ⟵ “Total Direct Costs | $55,910 | $43,960 | $43,960”
  - off_campus_not_with_family:Tuition: 43000 ⟵ “Tuition | $43,000 | $43,000 | $43,000”
  - off_campus_not_with_family:Fees: 960 ⟵ “Fees | $960 | $960 | $960”
  - off_campus_not_with_family:Housing and Food: 0 ⟵ “Housing and Food | $11,950 | $0 | $0”
  - off_campus_not_with_family:Total Direct Costs: 43960 ⟵ “Total Direct Costs | $55,910 | $43,960 | $43,960”
  - with_parents_or_family:Tuition: 43000 ⟵ “Tuition | $43,000 | $43,000 | $43,000”
  - with_parents_or_family:Fees: 960 ⟵ “Fees | $960 | $960 | $960”
  - with_parents_or_family:Housing and Food: 0 ⟵ “Housing and Food | $11,950 | $0 | $0”
  - with_parents_or_family:Total Direct Costs: 43960 ⟵ “Total Direct Costs | $55,910 | $43,960 | $43,960”
### `cbeac2ab2657e4ac` Concordia University-Nebraska — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cune.edu/undergraduate-costs/scholarships/church-work-scholarships (sha256 d49636671dfd)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Fall 2025 tuition: 41500 ⟵ “Fall 2025 tuition | $41,500”
  - column:Average tuition balance after all aid: 1996 ⟵ “Average tuition balance after all aid | $1,996”
### `377088eca54fc034` Concordia University-Nebraska — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.cune.edu/transfer-concordia/transferring-credits-concordia-and-credit-exam (sha256 0971f43d0eb2)
- issues: rows_without_score
- checks: {"distinct_exams": 15, "equivalencies": 15, "rows_without_score": 15}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “American Government | PS 111 American Government”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “Biology | Biology General Ed Credit”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “College Algebra | MATH 132 Intermediate Algebra”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | MATH 184 Calculus I”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|None]:  ⟵ “College Composition Modular | ENG 102 Experiences in Writing”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | ENG 102 plus 3 elective credits”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|None]:  ⟵ “Analyzing and Interpreting Literature | ENG 201 Introduction to Literature”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|None]:  ⟵ “History of the United States II | HIST 115 American Civilization”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|None]:  ⟵ “Human Growth and Development | PSY 221 Lifespan Development”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introductory Psychology | PSY 101 Introduction to Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Introductory Sociology | SOC 101 Introduction to Sociology”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “Principles of Macroeconomics | ECON 101 Principles of Macroeconomics”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | ECON 102 Principles of Microeconomics”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|None]:  ⟵ “Principles of Marketing | BUS 261 Marketing”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “Spanish (with a score of 66 or higher) | SPAN 201 or 202 Intermediate Spanish”
### `df080dde1dff0c74` Concordia University-Nebraska — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.cune.edu/transfer-concordia/transferring-credits-concordia-and-credit-exam (sha256 0971f43d0eb2)
- issues: rows_without_score, score_scale_mismatch
- checks: {"distinct_exams": 18, "equivalencies": 31, "rows_without_score": 2}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5-7]:  ⟵ “Anthropology | SL | 5-7 | GE Soc Sci | 3”
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “Biology | SL | 5-7 | BIO 111 | 4”
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “Biology | HL | 5-7 | BIO 111 & BIO 2xx | 8”
  - equivalencies[IB-CHEMISTRY|5-7]:  ⟵ “Chemistry | HL | 5-7 | CHEM 115 & 116 | 8”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science |  |  | TBD | ”
  - equivalencies[IB-ECONOMICS|4-7]:  ⟵ “Economics | SL/HL | 4-7 | GE Soc Sci | 5”
  - equivalencies[IB-FILM|None]:  ⟵ “Film |  |  | TBD | ”
  - equivalencies[IB-FRENCH|5-7]:  ⟵ “French | SL | 5-7 | Elect | 3”
  - equivalencies[IB-FRENCH|5-7]:  ⟵ “French | HL | 5-7 | Elect x 2 | 6”
  - equivalencies[IB-GEOGRAPHY|5-7]:  ⟵ “Geography | SL | 5-7 | GEOG 101 | 3”
  - equivalencies[IB-GEOGRAPHY|5-7]:  ⟵ “Geography | HL | 5-7 | GEOG 101 & GEOG elect | 6”
  - equivalencies[IB-GERMAN|5-7]:  ⟵ “German | SL | 5-7 | Elect | 3”
  - equivalencies[IB-GERMAN|5-7]:  ⟵ “German | HL | 5-7 | Elect x 2 | 6”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History | SL | 5-7 | HIST 131 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History | HL | 5-7 | HIST 115 and 131 or 132 | 6”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “Islamic History | SL | 5-7 | Hist elect | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “Islamic History | HL | 5-7 | Hist elect x 2 | 6”
  - equivalencies[IB-LATIN|5-7]:  ⟵ “Latin | SL | 5-7 | LAT 102 | 3”
  - equivalencies[IB-LATIN|5-7]:  ⟵ “Latin | HL | 5-7 | LAT 102 & Lat elect | 6”
  - equivalencies[IB-MUSIC|4-7]:  ⟵ “Music | SL | 4-7 | TBD | ”
  - equivalencies[IB-MUSIC|13-20]:  ⟵ “Music | HL | 13-20 | MU 100 | 3”
  - equivalencies[IB-PHILOSOPHY|5-7]:  ⟵ “Philosophy | SL | 5-7 | GE Soc Sci | 3”
  - equivalencies[IB-PHILOSOPHY|5-7]:  ⟵ “Philosophy | HL | 5-7 | GE Soc Sci & elect | 6”
  - equivalencies[IB-PHYSICS|5-7]:  ⟵ “Physics | SL | 5-7 | PHYS 109 | 4”
  - equivalencies[IB-PHYSICS|5-7]:  ⟵ “Physics | HL | 5-7 | PHYS 109 & Phys elect | 7”
  - … 6 more rows
### `df5cacb2b08a84e0` Concordia University-Nebraska — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.cune.edu/transfer-concordia/transferring-credits-concordia-and-credit-exam (sha256 0971f43d0eb2)
- issues: rows_without_score
- checks: {"distinct_exams": 33, "equivalencies": 38, "rows_without_score": 38}
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “Art History | ART 271 Art History I | 3”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology (with a score of 3 or 4) | BIO 111 General Biology I | 4”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology (with a score of 5) | BIO 111 General Biology I and BIO 112 General Biology II | 8”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry (with a score of 3 or 4) | CHEM 115 General Chemistry | 4”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry (with a score of 5) | CHEM 115 General Chemistry and CHEM 116 General Inorganic | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “Chinese Language and Culture | Free elective, foreign language or global multicultural | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “Computer Science Principles | CS 131 Computer Programming I | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “Computer Science A | CS 131 Computer Programming I | 3”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Macroeconomics | ECON 101 Prin. of Macroeconomics | 3”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Microeconomics | ECON 102 Prin. of Microeconomics | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language & Comp | ENG 102 Experiences in Writing | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “English Literature & Comp | ENG 201 Intro to Literature | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “Environmental Science | ESCI/GEOG/SCI 315 Environmental Sci. | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “French Language and Culture | Free elective, foreign language or global multicultural | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “German Language and Culture | Free elective, foreign language or global multicultural | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Human Geography | GEOG 202 World Regional Geography | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “Italian Language and Culture | Free elective, foreign language or global multicultural | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “Japanese Language and Culture | Free elective, foreign language or global multicultural | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “United States History | HIST 115 United States History | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “European History | HIST 132 World Civilization II | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|None]:  ⟵ “World History | HIST 131 World Civilization and HIST 132 World Civilization II | 6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|None]:  ⟵ “World History: Modern | HIST 132 World Civilization II | 3”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB | MATH 184 Calculus I | 4”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Calculus BC | MATH 184 Calculus I and MATH 186 Calculus II | 8”
  - equivalencies[AP-PRECALCULUS|None]:  ⟵ “Precalculus | MATH 151 Precalculus | 3”
  - … 13 more rows
### `076106ef31dfa95b` Creighton University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.creighton.edu/sites/default/files/Appeal-for-Independent-Student-Status-2026-2027.pdf (sha256 a4f04059a876)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “I understand this request is subject to the professional judgment of the Financial Aid Office and their decision is final.”
### `b01c631b2a6699e2` Creighton University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.creighton.edu/sites/default/files/Appeal-for-Independent-Student-Status-2025-2026.pdf (sha256 19322bb1b301)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “I understand this request is subject to the professional judgment of the Financial Aid Office and their decision is final.”
### `1194c098750ccab7` Metropolitan Community College Area — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.mccneb.edu/getting-started/tuition-financial-aid/financial-aid/types-of-aid (sha256 fad2e58d33ed)
- issues: semantic_review_required, conflicting_sources:https://www.mccneb.edu/getting-started/tuition-financial-aid/financial-aid/satisfactory-academic-progress-(sap)
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Criteria: Denied SAP appeals Denied all funding options Degree seeking Registered classes are in declared program of study Pass all registered classes with C grade or better Finisher Grant - This grant assists students who have 24 credit hours or less remaining in their first degree at MCC.”
### `506aeb120d2ff1b2` Metropolitan Community College Area — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.mccneb.edu/getting-started/tuition-financial-aid/financial-aid/frequently-asked-questions (sha256 8bf0cbb99efe)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “You may request a Special Circumstance form from the Financial Aid office that will allow our office to reevaluate your financial aid eligibility due to unemployment, loss of benefits, divorce or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “When completing the FAFSA form, the student will be asked if their parents are unwilling to provide their information, but the student doesn’t have an unusual circumstance that prevents them from contacting or obtaining their parents’ information.”
  - sentence: need_based_special_circumstances ⟵ “If you have special circumstances which make it impossible for your parents to complete the application, contact the Financial Aid office and discuss it with them.”
### `82b427d55db35246` Metropolitan Community College Area — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mccneb.edu/getting-started/tuition-financial-aid/financial-aid/satisfactory-academic-progress-(sap) (sha256 9404260e90c4)
- issues: semantic_review_required, conflicting_sources:https://www.mccneb.edu/getting-started/tuition-financial-aid/financial-aid/types-of-aid
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP appeals are reviewed quarterly according to the published deadlines.”
  - sentence: sap_appeal ⟵ “From there, the SAP appeal form is available by clicking on the SAP Appeal Form link under “Helpful Links.” Student appeals are available for all students requesting Federal Financial Aid and applicable Nebraska State Tuition Waiver eligible students.”
### `a749ea652d82f884` Metropolitan Community College Area — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mccneb.edu/getting-started/tuition-financial-aid/financial-aid/satisfactory-academic-progress-(sap) (sha256 9404260e90c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment The Higher Education Act (HEA) Section 479A establishes authority for the financial aid administrator to exercise professional judgement discretion to make adjustments on a case-by-case basis in a number of areas when an applicant, parent, or spouse has special or unusual circumstances.”
### `fa8ec376de97215d` Metropolitan Community College Area — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.mccneb.edu/getting-started/tuition-financial-aid/financial-aid/frequently-asked-questions (sha256 8bf0cbb99efe)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “If you have been declared independent by a financial aid administrator in the past, or if you think your special situation merits a review, request to meet with a Financial Aid specialist to see if you qualify to complete a Request for Dependency Override Form.”
### `59ac15a363ca54e2` Mid-Plains Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mpcc.edu/current-students/add_drop_withdrawal_and_billing_appeal_process.php (sha256 fc56adcde175)
- issues: semantic_review_required, conflicting_sources:https://www.mpcc.edu/cost-and-aid/tuition-payment-options.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The request should include: student’s name and current contact information (telephone, USPS address, e-mail address), specific details defining what the student would like to have happen and why, including all of the following that apply: course name(s), code(s) and location(s), instructor information, campus location for housing, what the desired appeal outcome would be, and justification as to w”
### `62499436f6fcd80b` Mid-Plains Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.mpcc.edu/cost-and-aid/financial-aid/financial-aid.php (sha256 ce89c84e91ad)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances If you have had a change in circumstances that affects your or your family’s ability to pay for college, we encourage you to contact us.”
  - sentence: need_based_special_circumstances ⟵ “Example of special circumstances include loss of employment, unusually high medical expenses not covered by insurance, or other changes in the family’s income or assets.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances If you have unusual circumstances that prevent you from submitting parental information on the FAFSA, we encourage you to contact us.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances would include you or your parents are incarcerated, situations of parental abandonment or endangerment, or if your circumstances resulted in you not having a safe, stable place to live.”
### `68a725d8ece6d4da` Mid-Plains Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mpcc.edu/cost-and-aid/tuition-payment-options.php (sha256 1c69a88e0552)
- issues: semantic_review_required, conflicting_sources:https://www.mpcc.edu/current-students/add_drop_withdrawal_and_billing_appeal_process.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Also, documentation that provides evidence that unusual circumstances prevented the student from taking action within standard deadlines.”
### `0530c69e82ef521d` Mid-Plains Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.mpcc.edu/admissions/files/clep_transfer_credit.pdf (sha256 c3cdab72aa00)
- issues: credits_implausible, score_scale_mismatch, course_column_missing
- checks: {"distinct_exams": 7, "equivalencies": 7, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “POLS 1000 American Govt & Politics                  3       American Government                                       50”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “PSYC 1810 - Introduction to Psychology              3       Introductory Psychology                                   50”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|3]:  ⟵ “SOCI 1010 - Introduction to Sociology               3       Introductory Sociology                                    50”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “MATH 1150 - College Algebra                         3       College Algebra                                           50”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|3]:  ⟵ “BSAD 2710 - Business Law I                          3       Introductory Business Law                                 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “BSAD 2540 - Principles of Management                3       Principles of Management                                  50”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|3]:  ⟵ “BSAD 2340 - Introduction to Marketing               3       Principles of Marketing                                   50”
### `3d155c3acf7ba1b1` Midland University — appeals 2022-23 [new] (labeled_in_source)
- source: https://2223grad.catalog.midlandu.edu/policies/sap (sha256 13d10c661adc)
- issues: stale_year_label:2022-23, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If the standard is not met, a SAP appeal is required and must be approved before federal aid can be offered.”
  - sentence: sap_appeal ⟵ “Notification to Students Once a completed SAP appeal has been submitted, the Financial Aid Office will notify the student via email regarding the status of the appeal, including the terms of approval or denial.”
### `4e23cafc414e2538` Midland University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://2526grad.catalog.midlandu.edu/policies/sap (sha256 6b614d96e59e)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If the standard is not met, a SAP appeal is required and must be approved before federal aid can be offered.”
  - sentence: sap_appeal ⟵ “Notification to Students Once a completed SAP appeal has been submitted, the Financial Aid Office will notify the student via email regarding the status of the appeal, including the terms of approval or denial.”
### `82a76bebb9f8ce06` Midland University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.midlandu.edu/academics/registrars-office/academic-appeals/ (sha256 bfe3df873850)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Grades and other academic judgments are within the province and professional judgment of the faculty.”
### `bfbd1d6ccd6afaf8` Midland University — appeals 2023-24 [new] (labeled_in_source)
- source: https://2223undergrad.catalog.midlandu.edu/policies/sap (sha256 d23adc5b1f74)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If the standard is not met, a SAP appeal is required and must be approved before federal aid can be offered.”
  - sentence: sap_appeal ⟵ “Notification to Students Once a completed SAP appeal has been submitted, the Financial Aid Office will notify the student via email regarding the status of the appeal, including the terms of approval or denial.”
### `e9ba8b4939eaefc6` Nebraska College of Technical Agriculture — appeals 2026-27 [new] (source_unlabeled)
- source: https://ncta.unl.edu/special-circumstance/ (sha256 a8a0d0fbd782)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances When special circumstances occur that affect your or your family's ability to pay educational expenses, you are encouraged to notify the OSFA.”
  - sentence: need_based_special_circumstances ⟵ “A Special Circumstances Application is available to apply for an adjustment based on certain situations.”
  - sentence: need_based_special_circumstances ⟵ “Another special circumstance that may occur is related to a family's unusually high medical or dental expenses not covered by insurance.”
### `1c29e7c8981b31fa` Nebraska College of Technical Agriculture — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://ncta.unl.edu/credit-prior-learning/ (sha256 438353a1ad8e)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 7, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|5, 4]:  ⟵ “Biology | 5, 4 | BIO 1104: General Biology & Lab | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHM 1014: Chemistry in Context I | 4”
  - equivalencies[AP-CHEMISTRY|5, 4]:  ⟵ “Chemistry | 5, 4 | CHM 1104: General Chemistry I | 4”
  - equivalencies[AP-MACROECONOMICS|5, 4, 3]:  ⟵ “Macroeconomics | 5, 4, 3 | ECN 1303: Macroeconomics | 3”
  - equivalencies[AP-MICROECONOMICS|5, 4, 3]:  ⟵ “Microeconomics | 5, 4, 3 | ECN 1203: Microeconomics | 3”
  - equivalencies[AP-PSYCHOLOGY|5, 4, 3]:  ⟵ “Psychology | 5, 4, 3 | PSY 1103: Human Relations | 3”
  - equivalencies[AP-STATISTICS|5, 4, 3]:  ⟵ “Statistics | 5, 4, 3 | MTH 2203: Intro to Stats | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|5, 4]:  ⟵ “U.S. History | 5, 4 | HTY 1303: American History After 1877 | 3”
  - equivalencies[AP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIO 1104: General Biology & Lab | 4”
  - equivalencies[AP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHM 1104: General Chemistry I | 4”
  - equivalencies[AP-PSYCHOLOGY|53]:  ⟵ “Introductory Psychology | 53 | PSY 1103: Human Relations | 3”
  - equivalencies[AP-MACROECONOMICS|49]:  ⟵ “Principles of Macroeconomics | 49 | ECN 1303: Macroeconomics | 3”
  - equivalencies[AP-MICROECONOMICS|49]:  ⟵ “Principles of Microeconomics | 49 | ECN 1203: Microeconomics | 3”
### `474c68bebac802df` Nebraska Indian Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.thenicc.edu/admissions/cost-of-attendance.php (sha256 1b488bac5216)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - column:Tuition: 4080.0 ⟵ “Tuition | $4,080.00 | $4,080.00”
  - column:Housing: 8856.0 ⟵ “Housing | $8,856.00 | $6,072.00”
  - column:Utilities: 2457.0 ⟵ “Utilities | $2,457.00 | $1,791.00”
  - column:Food: 9585.0 ⟵ “Food | $9,585.00 | $5,337.00”
  - column:Travel: 711.0 ⟵ “Travel | $711.00 | $711.00”
  - column:Personal: 4014.0 ⟵ “Personal | $ 4,014.00 | $2,748.00”
  - column:Classroom Supplies: 400.0 ⟵ “Classroom Supplies | $400.00 | $400.00”
  - column:TOTAL COST OF ATTENDANCE: 30103.0 ⟵ “TOTAL COST OF ATTENDANCE | $30,103.00 | $21,139.00”
  - column:Tuition: 4080.0 ⟵ “Tuition | $4,080.00 | $4,080.00”
  - column:Housing: 6072.0 ⟵ “Housing | $8,856.00 | $6,072.00”
  - column:Utilities: 1791.0 ⟵ “Utilities | $2,457.00 | $1,791.00”
  - column:Food: 5337.0 ⟵ “Food | $9,585.00 | $5,337.00”
  - column:Travel: 711.0 ⟵ “Travel | $711.00 | $711.00”
  - column:Personal: 2748.0 ⟵ “Personal | $ 4,014.00 | $2,748.00”
  - column:Classroom Supplies: 400.0 ⟵ “Classroom Supplies | $400.00 | $400.00”
  - column:TOTAL COST OF ATTENDANCE: 21139.0 ⟵ “TOTAL COST OF ATTENDANCE | $30,103.00 | $21,139.00”
### `d1a17fc8e70783cf` Nebraska Methodist College of Nursing & Allied Health — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.methodistcollege.edu/satisfactory-academic-progress (sha256 312cdc9cf394)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Reasons for an appeal may include: death of a relative, injury or illness of the student, or other special circumstances.”
### `3f3ffa3a3ea65ae7` Nebraska Methodist College of Nursing & Allied Health — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.methodistcollege.edu/cost-of-attendance (sha256 fcc043b7b64a)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "components_reconcile": true, "rows": 10}
  - column:Tuition: 40184 ⟵ “Tuition | $40,184 | $40,184 | $40,184 | $40,184”
  - column:Fees: 4740 ⟵ “Fees | $4,740 | $4,740 | $4,740 | $4,740”
  - column:Campus Housing: 8696 ⟵ “Campus Housing | $8,696 | $12,276 | -- | --”
  - column:Food & Meals: 4920 ⟵ “Food & Meals | $4,920 | $4,920 | $4,920 | $2,760”
  - column:Books & Supplies: 2890 ⟵ “Books & Supplies | $2,890 | $2,890 | $2,890 | $2,890”
  - column:Transportation: 4827 ⟵ “Transportation | $4,827 | $4,827 | $4,827 | $4,827”
  - column:Misc. Personal Expenses: 3480 ⟵ “Misc. Personal Expenses | $3,480 | $3,480 | $3,480 | $3,480”
  - column:Federal Loan Fees: 159 ⟵ “Federal Loan Fees | $159 | $159 | $159 | $159”
  - column:Estimated Total Full-time Costs: 69896 ⟵ “Estimated Total Full-time Costs | $69,896 | $73,476 | $76,440 | $62,040”
  - column:Subtotal Direct Costs: 53620 ⟵ “Subtotal Direct Costs | $53,620 | $57,200 | $44,924 | $44,924”
  - column:Tuition: 40184 ⟵ “Tuition | $40,184 | $40,184 | $40,184 | $40,184”
  - column:Fees: 4740 ⟵ “Fees | $4,740 | $4,740 | $4,740 | $4,740”
  - column:Campus Housing: 12276 ⟵ “Campus Housing | $8,696 | $12,276 | -- | --”
  - column:Food & Meals: 4920 ⟵ “Food & Meals | $4,920 | $4,920 | $4,920 | $2,760”
  - column:Books & Supplies: 2890 ⟵ “Books & Supplies | $2,890 | $2,890 | $2,890 | $2,890”
  - column:Transportation: 4827 ⟵ “Transportation | $4,827 | $4,827 | $4,827 | $4,827”
  - column:Misc. Personal Expenses: 3480 ⟵ “Misc. Personal Expenses | $3,480 | $3,480 | $3,480 | $3,480”
  - column:Federal Loan Fees: 159 ⟵ “Federal Loan Fees | $159 | $159 | $159 | $159”
  - column:Estimated Total Full-time Costs: 73476 ⟵ “Estimated Total Full-time Costs | $69,896 | $73,476 | $76,440 | $62,040”
  - column:Subtotal Direct Costs: 57200 ⟵ “Subtotal Direct Costs | $53,620 | $57,200 | $44,924 | $44,924”
  - column:Tuition: 40184 ⟵ “Tuition | $40,184 | $40,184 | $40,184 | $40,184”
  - column:Fees: 4740 ⟵ “Fees | $4,740 | $4,740 | $4,740 | $4,740”
  - column:Food & Meals: 4920 ⟵ “Food & Meals | $4,920 | $4,920 | $4,920 | $2,760”
  - column:Off-campus Housing: 15240 ⟵ “Off-campus Housing | -- | -- | $15,240 | $3,000”
  - column:Books & Supplies: 2890 ⟵ “Books & Supplies | $2,890 | $2,890 | $2,890 | $2,890”
  - … 15 more rows
### `01a284bf1ffeab2d` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: £500 ⟵ “BUTEX | £500 | Applications will reopen on May 1, 2026”
### `11fb74f54ffa50a7` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: All program costs ⟵ “Critical Language Scholarships | All program costs | See Critical Language website”
### `174cac95efad039f` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $200-$2,850 ⟵ “Education Abroad Grant (Semester and Year-long programs) | $200-$2,850 | Spring: October 29; Fall or year: March 25”
### `19bc2832bc5fcbd4` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: All expenses paid ⟵ “DAAD Rise | All expenses paid | See DAAD Rise website”
### `28c6deef10913521` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $4,500 ⟵ “ATJ Bridging (American Teachers of Japanese) | Up to $4,500 | March 15”
### `53f9abdc0fb7af99` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Full cost of one year in Germany ⟵ “Congress-Bundestag Youth Exchange | Full cost of one year in Germany | See Congress Bundestag website”
### `6e6d4ce703605477` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $400 ⟵ “Nick Lee Scholarship | $400 | Spring: October 23; Fall/Year-long: February 19”
### `6eaff7f0ddcb767b` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 ⟵ “Gilman Scholarship | Up to $5,000 | Thursday, October 1, 2026 at 11:59 p.m. Pacific Time.”
### `74025be0e0978e5c` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Determined yearly ⟵ “UM HEF Yamagata | Determined yearly | March 1”
### `79969bd41ebfc31c` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Amount varies, up to full cost of attendance ⟵ “Toshizo Watanabe Scholarship | Amount varies, up to full cost of attendance | 2026 - Spring 2027 is scheduled to open in January 2026”
### `845ef78e4f8080b3` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Full cost of two years master's degree ⟵ “Rotary World Peace Scholarship | Full cost of two years master's degree | District deadlines are as early as March; check with the local club”
### `9294203e6aa7e365` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $200-$1,000 ⟵ “Education Abroad Grant (Winter and Summer programs) | $200-$1,000 | Winter: October 29; Summer: March 25”
### `98206c51f47e329d` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Full cost of two years of graduate study at Oxford, plus airfare ⟵ “Rhodes Scholarship | Full cost of two years of graduate study at Oxford, plus airfare | 11:59 PM U.S. Eastern Time on the first Wednesday of October each year”
### `a5050f77f0ca4e0a` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Full cost of studying at Cambridge ⟵ “Gates Cambridge Scholarship | Full cost of studying at Cambridge | Wednesday, October 15, 2025 (Full application must be submitted by 23:59 GMT)”
### `ad0a11c9e11a47e0` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 ⟵ “Gilman-McCain Scholarship | Up to $5,000 | Thursday, February 25, 2027 at 11:59 p.m. Pacific Time.”
### `ad5a24754e1fdc9e` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Full cost of study/research program, including airfare ⟵ “Fulbright Scholarships | Full cost of study/research program, including airfare | Tuesday, October 7th, 5pm Eastern Time”
### `af6da5ec261c9e98` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $27,000 ⟵ “Rotary Ambassadorial Scholarship | Up to $27,000 | See Rotary website, usually the beginning of June”
### `b0252243c77a7dc8` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Fully funded ⟵ “Humanity in Action (HIA) | Fully funded | See HIA website”
### `b4bf9d555c4d5233` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Full-time paid position, amount varies ⟵ “JET Program | Full-time paid position, amount varies | Application deadline is usually in the middle of November for the following year’s JET program.”
### `c7ef8c06f908e421` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Full cost of two years of undergraduate or graduate study leading to a British University degree, plus airfare ⟵ “Marshall Scholarship | Full cost of two years of undergraduate or graduate study leading to a British University degree, plus airfare | See Marshall website”
### `d2b34abe0cc4888b` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Phi Kappa Phi Scholarship | $1,000 | See Phi Kappa Phi Study Abroad Scholarship website”
### `d8da3f994134a9d1` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Round-trip airfare, tuition and fees at host institution, accommodation, and in some cases, a small daily allowance for meals ⟵ “UK Summer Fulbright Scholarship | Round-trip airfare, tuition and fees at host institution, accommodation, and in some cases, a small daily allowance for meals | February 3, 2025, expect same time for 2026”
### `d9f33b84a027cb26` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: 60,000 yen to 100,000 yen per month ⟵ “JASSO (Japan Student Services Organization) | 60,000 yen to 100,000 yen per month | April”
### `e16e39cc4c0dc6c4` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $150-$400 ⟵ “Hattie Johns and Helen Johns Fulton Endowed Scholarship | $150-$400 | Spring: October 23; Fall/Year-long or Summer: February 19”
### `ed55dab90cda7031` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Full cost of study at St. John's College, University of Cambridge, including airfare ⟵ “Davies-Jackson Scholarship | Full cost of study at St. John's College, University of Cambridge, including airfare | See Davies-Jackson website”
### `f1f034c8ec5b33ec` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: $10,000 (Academic Year); $5,000 (fall/spring semester); prorated by no. of weeks, minimum $1,250 (summer) ⟵ “Fund for Education Abroad Scholarship | $10,000 (Academic Year); $5,000 (fall/spring semester); prorated by no. of weeks, minimum $1,250 (summer) | Due February 4, 2026 at 12 p.m. EST”
### `faa9fc314c4e8d8f` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $20,000 ⟵ “Boren Scholarship | Up to $20,000 | Boren Fellowship: January 21, 2026, Boren Scholarship: January 28, 2026”
### `fcd7de8a40950eaa` Nebraska Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/financial-aid-office/undergraduate-aid/study-abroad-scholarships (sha256 fdd26b53c9ac)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Summer Award: up to $3,000; Semester Award: up to $5,000; Academic/Calendar Year Award: up to $7,000 ⟵ “Freeman-ASIA Scholarship | Summer Award: up to $3,000; Semester Award: up to $5,000; Academic/Calendar Year Award: up to $7,000 | April 7, 2026”
### `0f1d08c10459dcac` Nebraska Wesleyan University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.nebrwesleyan.edu/admissions/tuition-and-fees (sha256 829ce1714d1f)
- issues: ambiguous_year_labels
- checks: {"columns": 5, "components_reconcile": true, "rows": 11}
  - on_campus:Tuition: 45944 ⟵ “Tuition | 45,944 | 45,944 | 45,944 | 45,944 | 45,944”
  - on_campus:- Student fee: 1392 ⟵ “- Student fee | 1,392 | 1,392 | 1,392 | 1,392 | 1,392”
  - on_campus:- Technology fee: 120 ⟵ “- Technology fee | 120 | 120 | 120 | 120 | 120”
  - on_campus:- Matriculation fee: 176 ⟵ “- Matriculation fee | 176 | 176 | - | - | -”
  - on_campus:Housing/Food: 13652 ⟵ “Housing/Food | 13,652 | - | 14,570 | - | -”
  - on_campus:Books: 1000 ⟵ “Books | 1,000 | 1,000 | 1,000 | 1,000 | 1,000”
  - on_campus:Personal expenses: 2500 ⟵ “Personal expenses | 2,500 | 2,500 | 2,500 | 2,500 | 2,500”
  - on_campus:Transportation: 1000 ⟵ “Transportation | 1,000 | 1,000 | 1,000 | 1,000 | 1,000”
  - on_campus:TOTAL COST OF ATTENDANCE: 65784 ⟵ “TOTAL COST OF ATTENDANCE | $65,784 | $55,132 | $66,526 | $54,956 | $66,526”
  - on_campus:Total Direct Expenses: 61284 ⟵ “Total Direct Expenses | $61,284 | $47,632 | $62,026 | $47,456 | $47,456”
  - on_campus:Total Indirect Expenses: 4500 ⟵ “Total Indirect Expenses | $4,500 | $7,500 | $4,500 | $7,500 | $19,070”
  - with_parents_or_family:Tuition: 45944 ⟵ “Tuition | 45,944 | 45,944 | 45,944 | 45,944 | 45,944”
  - with_parents_or_family:- Student fee: 1392 ⟵ “- Student fee | 1,392 | 1,392 | 1,392 | 1,392 | 1,392”
  - with_parents_or_family:- Technology fee: 120 ⟵ “- Technology fee | 120 | 120 | 120 | 120 | 120”
  - with_parents_or_family:- Matriculation fee: 176 ⟵ “- Matriculation fee | 176 | 176 | - | - | -”
  - with_parents_or_family:Housing/Food: 3000 ⟵ “Housing/Food | - | 3,000 | - | 3,000 | 14,570”
  - with_parents_or_family:Books: 1000 ⟵ “Books | 1,000 | 1,000 | 1,000 | 1,000 | 1,000”
  - with_parents_or_family:Personal expenses: 2500 ⟵ “Personal expenses | 2,500 | 2,500 | 2,500 | 2,500 | 2,500”
  - with_parents_or_family:Transportation: 1000 ⟵ “Transportation | 1,000 | 1,000 | 1,000 | 1,000 | 1,000”
  - with_parents_or_family:TOTAL COST OF ATTENDANCE: 55132 ⟵ “TOTAL COST OF ATTENDANCE | $65,784 | $55,132 | $66,526 | $54,956 | $66,526”
  - with_parents_or_family:Total Direct Expenses: 47632 ⟵ “Total Direct Expenses | $61,284 | $47,632 | $62,026 | $47,456 | $47,456”
  - with_parents_or_family:Total Indirect Expenses: 7500 ⟵ “Total Indirect Expenses | $4,500 | $7,500 | $4,500 | $7,500 | $19,070”
  - on_campus:Tuition: 45944 ⟵ “Tuition | 45,944 | 45,944 | 45,944 | 45,944 | 45,944”
  - on_campus:- Student fee: 1392 ⟵ “- Student fee | 1,392 | 1,392 | 1,392 | 1,392 | 1,392”
  - on_campus:- Technology fee: 120 ⟵ “- Technology fee | 120 | 120 | 120 | 120 | 120”
  - … 27 more rows
### `1753de493997b2c7` Northeast Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs (sha256 84404fd0a77d)
- issues: semantic_review_required, conflicting_sources:https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you feel that special circumstances exist, please contact the Northeast Financial Aid Office. **Independent status is NOT determined by your wish to be financially independent of your parents nor based on your parents' unwillingness to finance your college education.”
### `18f5e14f66ef52d9` Northeast Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs (sha256 6f4f683d1d9c)
- issues: semantic_review_required, conflicting_sources:https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Be meeting Satisfactory Academic Progress (SAP) standards, which are reviewed after the spring semester, or successfully appeal your SAP status as soon as possible, if needed.”
### `2642e8c1cccfbe81` Northeast Community College — appeals 2023-24 [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/financial-aid/special-circumstance (sha256 a4d5df83251e)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Federal regulations provide Financial Aid Administrators the authority to use professional judgment on a case-by-case basis, to adjust the cost of attendance or the values of the items used in calculating the SAI (Student Aid Index) to reflect a student's special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “Steps to Complete Log into Student Forms Click 'Manage Requests' Click + button under applicable aid year for Professional Judgment: Professional Judgment: Special Circumstance - COA Appeal Enter reason for request and hit submit Open request, complete form and upload supporting documentation What to Expect A Special Circumstance review typically takes between 3-4 weeks from the date when all nece”
### `52d22007e0f719de` Northeast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress (sha256 7f4c853f65d8)
- issues: semantic_review_required, conflicting_sources:https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A student may appeal their financial aid suspension if extenuating circumstances (death of a relative, injury or illness of the student, or other special circumstance) exist.”
### `6f912d1ff53bb52b` Northeast Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/financial-aid/ (sha256 50ca94980e7d)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Future Students Upcoming Deadlines Net Price Calculator FAFSA Application Scholarships Student Forms Financial Aid FAQs Helpful Resources Request for Special Circumstance Cost of Attendance Award Notification College Financing Plan Personal Finance Basics Consumer Information and Guidelines Pay My Bill Onward.”
### `89e028337534d4dc` Northeast Community College — appeals 2023-24 [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/financial-aid/special-circumstance (sha256 a4d5df83251e)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Future Students Upcoming Deadlines Net Price Calculator Special and/or Unusual circumstances may occur when a student's current financial or dependency situation is no longer accurately reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “An Unusual Circumstance request will be processed as quickly as practicable, but a determination will be made no later than 60 days after the student enrolls.”
  - sentence: need_based_special_circumstances ⟵ “Beginning with the 2023-24 award year, any student who was approved for a dependency override and made independent for financial aid due to unusual circumstances will continue to be independent for each subsequent award year at Northeast unless the student informs us that their circumstances have changed, or we have conflicting information about the student's independence.”
### `a341a4c482b48e34` Northeast Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs (sha256 84404fd0a77d)
- issues: semantic_review_required, conflicting_sources:https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Be meeting Satisfactory Academic Progress (SAP) standards, which are reviewed after the spring semester, or successfully appeal your SAP status as soon as possible, if needed.”
### `ab461c69584e0fc7` Northeast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress (sha256 7f4c853f65d8)
- issues: semantic_review_required, conflicting_sources:https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Steps to Complete Log into Student Forms Click 'Manage Requests' Click + button under applicable aid year for Satisfactory Academic Progress (SAP) Appeal Enter reason for request and hit submit Open request, complete form and upload supporting documentation Additional Information Transitional Classes Students may receive financial aid for a maximum of 30 credits of transitional classes.”
### `c6e3c756cd86f050` Northeast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress (sha256 febe9250d730)
- issues: semantic_review_required, conflicting_sources:https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Steps to Complete Log into Student Forms Click 'Manage Requests' Click + button under applicable aid year for Satisfactory Academic Progress (SAP) Appeal Enter reason for request and hit submit Open request, complete form and upload supporting documentation Additional Information Transitional Classes Students may receive financial aid for a maximum of 30 credits of transitional classes.”
### `d41594582485ed8f` Northeast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress (sha256 febe9250d730)
- issues: semantic_review_required, conflicting_sources:https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A student may appeal their financial aid suspension if extenuating circumstances (death of a relative, injury or illness of the student, or other special circumstance) exist.”
### `ffe12808e38afe90` Northeast Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs (sha256 6f4f683d1d9c)
- issues: semantic_review_required, conflicting_sources:https://northeast.edu/costs-aid/financial-aid/financial-aid-faqs,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress,https://northeast.edu/costs-aid/financial-aid/standards-of-satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you feel that special circumstances exist, please contact the Northeast Financial Aid Office. **Independent status is NOT determined by your wish to be financially independent of your parents nor based on your parents' unwillingness to finance your college education.”
### `16723655c3fe2ece` Northeast Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/tuition/ (sha256 25a77a8a48c7)
- issues: components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - on_campus:Tuition: 3360 ⟵ “Tuition | $3,360 | $3,360 | $4,650”
  - on_campus:Fees: 630 ⟵ “Fees | $630 | $630 | $630”
  - on_campus:Loan Fees (if applicable): 53 ⟵ “Loan Fees (if applicable) | $53 | $53 | $53”
  - on_campus:Books (est.): 1145 ⟵ “Books (est.) | $1,145 | $1,142 | $1,142”
  - on_campus:Living Expenses - On CampusHousing and Food*: 10546 ⟵ “Living Expenses - On CampusHousing and Food* | $10,546 | $10,546 | $10,546”
  - on_campus:Travel: 832 ⟵ “Travel | $832 | $832 | $832”
  - on_campus:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - on_campus:Total: 17688 ⟵ “Total | $17,688 | $17,688 | $18,978”
  - on_campus:Tuition: 3360 ⟵ “Tuition | $3,360 | $3,360 | $4,650”
  - on_campus:Fees: 630 ⟵ “Fees | $630 | $630 | $630”
  - on_campus:Loan Fees (if applicable): 53 ⟵ “Loan Fees (if applicable) | $53 | $53 | $53”
  - on_campus:Books (est.): 1142 ⟵ “Books (est.) | $1,145 | $1,142 | $1,142”
  - on_campus:Living Expenses - On CampusHousing and Food*: 10546 ⟵ “Living Expenses - On CampusHousing and Food* | $10,546 | $10,546 | $10,546”
  - on_campus:Travel: 832 ⟵ “Travel | $832 | $832 | $832”
  - on_campus:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - on_campus:Total: 17688 ⟵ “Total | $17,688 | $17,688 | $18,978”
### `1e7e661b20c1d773` Northeast Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/tuition/ (sha256 25a77a8a48c7)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 4590 ⟵ “Tuition | $3,300 | $3,300 | $4,590”
  - on_campus:Fees: 630 ⟵ “Fees | $630 | $630 | $630”
  - on_campus:Loan Fees (if applicable): 17 ⟵ “Loan Fees (if applicable) | $17 | $17 | $17”
  - on_campus:Books (est.): 1356 ⟵ “Books (est.) | $1,356 | $1,356 | $1,356”
  - on_campus:Living Expenses - On CampusHousing and Food*: 10211 ⟵ “Living Expenses - On CampusHousing and Food* | $10,211 | $10,211 | $10,211”
  - on_campus:Travel: 562 ⟵ “Travel | $562 | $562 | $562”
  - on_campus:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - on_campus:Total: 18491 ⟵ “Total | $17,201 | $17,201 | $18,491”
### `662ed9008471247f` Northeast Community College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/tuition/ (sha256 25a77a8a48c7)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 3300 ⟵ “Tuition | $3,300 | $3,300 | $4,590”
  - on_campus:Fees: 630 ⟵ “Fees | $630 | $630 | $630”
  - on_campus:Loan Fees (if applicable): 17 ⟵ “Loan Fees (if applicable) | $17 | $17 | $17”
  - on_campus:Books (est.): 1356 ⟵ “Books (est.) | $1,356 | $1,356 | $1,356”
  - on_campus:Living Expenses - On CampusHousing and Food*: 10211 ⟵ “Living Expenses - On CampusHousing and Food* | $10,211 | $10,211 | $10,211”
  - on_campus:Travel: 562 ⟵ “Travel | $562 | $562 | $562”
  - on_campus:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - on_campus:Total: 17201 ⟵ “Total | $17,201 | $17,201 | $18,491”
  - on_campus:Tuition: 3300 ⟵ “Tuition | $3,300 | $3,300 | $4,590”
  - on_campus:Fees: 630 ⟵ “Fees | $630 | $630 | $630”
  - on_campus:Loan Fees (if applicable): 17 ⟵ “Loan Fees (if applicable) | $17 | $17 | $17”
  - on_campus:Books (est.): 1356 ⟵ “Books (est.) | $1,356 | $1,356 | $1,356”
  - on_campus:Living Expenses - On CampusHousing and Food*: 10211 ⟵ “Living Expenses - On CampusHousing and Food* | $10,211 | $10,211 | $10,211”
  - on_campus:Travel: 562 ⟵ “Travel | $562 | $562 | $562”
  - on_campus:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - on_campus:Total: 17201 ⟵ “Total | $17,201 | $17,201 | $18,491”
### `e11c078a81670f64` Northeast Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://northeast.edu/costs-aid/financial-aid/cost-of-attendance (sha256 1acfd1a02bf7)
- issues: residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees: 3990 ⟵ “Tuition & Fees | $3,990 | $3,990 | $3,990”
  - on_campus:Loan Fees: 53 ⟵ “Loan Fees | $53 | $53 | $53”
  - on_campus:Housing & Meals: 10546 ⟵ “Housing & Meals | $10,546 | $9,065 | $3,217”
  - on_campus:Books & Supplies: 1142 ⟵ “Books & Supplies | $1,142 | $1,142 | $1,142”
  - on_campus:Travel: 832 ⟵ “Travel | $832 | $1,686 | $1,686”
  - on_campus:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - on_campus:Total:: 17688 ⟵ “Total: | $17,688 | $17,061 | $11,213”
  - off_campus_not_with_family:Tuition & Fees: 3990 ⟵ “Tuition & Fees | $3,990 | $3,990 | $3,990”
  - off_campus_not_with_family:Loan Fees: 53 ⟵ “Loan Fees | $53 | $53 | $53”
  - off_campus_not_with_family:Housing & Meals: 9065 ⟵ “Housing & Meals | $10,546 | $9,065 | $3,217”
  - off_campus_not_with_family:Books & Supplies: 1142 ⟵ “Books & Supplies | $1,142 | $1,142 | $1,142”
  - off_campus_not_with_family:Travel: 1686 ⟵ “Travel | $832 | $1,686 | $1,686”
  - off_campus_not_with_family:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - off_campus_not_with_family:Total:: 17061 ⟵ “Total: | $17,688 | $17,061 | $11,213”
  - with_parents_or_family:Tuition & Fees: 3990 ⟵ “Tuition & Fees | $3,990 | $3,990 | $3,990”
  - with_parents_or_family:Loan Fees: 53 ⟵ “Loan Fees | $53 | $53 | $53”
  - with_parents_or_family:Housing & Meals: 3217 ⟵ “Housing & Meals | $10,546 | $9,065 | $3,217”
  - with_parents_or_family:Books & Supplies: 1142 ⟵ “Books & Supplies | $1,142 | $1,142 | $1,142”
  - with_parents_or_family:Travel: 1686 ⟵ “Travel | $832 | $1,686 | $1,686”
  - with_parents_or_family:Miscellaneous: 1125 ⟵ “Miscellaneous | $1,125 | $1,125 | $1,125”
  - with_parents_or_family:Total:: 11213 ⟵ “Total: | $17,688 | $17,061 | $11,213”
### `217a8116f152c310` Southeast Community College Area — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.southeast.edu/paying-for-scc/index.php (sha256 9e69635c0aff)
- issues: cost_period_semester
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 1512 ⟵ “Tuition | $1,260 | $1,512”
  - column:Fees (Facility + Student Activity): 264 ⟵ “Fees (Facility + Student Activity) | $264 | $264”
### `4cfdcfe55cfe9f94` Southeast Community College Area — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.southeast.edu/paying-for-scc/index.php (sha256 9e69635c0aff)
- issues: cost_period_semester
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 1260 ⟵ “Tuition | $1,260 | $1,512”
  - column:Fees (Facility + Student Activity): 264 ⟵ “Fees (Facility + Student Activity) | $264 | $264”
### `07c486b4dedc11a3` University of Nebraska at Kearney — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unk.edu/offices/financial_aid/satisfactory-academic-progress.php (sha256 e33bea56a32e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “If you feel that there were special circumstances that impacted your ability to do well in the classroom, you can appeal your SAP suspension.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances may include illness, injury, personal struggle, or family difficulty.”
### `769931fc85d81af7` University of Nebraska at Kearney — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unk.edu/offices/financial_aid/satisfactory-academic-progress.php (sha256 e33bea56a32e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP Appeal Forms University Academic Suspension: A student on this suspension cannot enroll in classes at UNK.”
  - sentence: sap_appeal ⟵ “Visit the UNK Satisfactory Academic Progress Appeal Forms page to learn more about the appeal process.”
### `0371cb4fdcd70de9` University of Nebraska at Omaha — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php (sha256 46b18e5c89d7)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/index.php
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “To be eligible for a Special Circumstance or Unusual Circumstance Appeal, you must be admitted to UNO in a degree-seeking program and have filed a FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If you are selected for verification, this process must be completed before a Special Circumstance can be considered.”
  - sentence: need_based_special_circumstances ⟵ “Common Reasons to Submit a Special or Unusual Circumstance Special Circumstance: Income Reduction Appeal Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an aid administrator adjusting data elements in the cost of attendance (COA) or in the Student Aid Index (SAI) calculation.”
  - sentence: need_based_special_circumstances ⟵ “Abusive (physically and/or mentally) family environment Abandonment Parents cannot be located/no contact with any parent Other reasons A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal Process Step 1: Contact Our Office Email us to request a Special or Unusual Circumstance Appeal.”
  - sentence: need_based_special_circumstances ⟵ “After reviewing your situation, a Financial Support Counselor will assign a Special/Unusual Circumstance Questionnaire to your MavLINK To-Do List.”
### `152b409d53aad908` University of Nebraska at Omaha — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/index.php (sha256 01befbd27137)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstances Special and/or Unusual Circumstances may occur when your current financial or dependency situation is no longer accurately reflected on your FAFSA application.”
### `1ce9786e3e6cf7ae` University of Nebraska at Omaha — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/first-year-student.php (sha256 0749d597d877)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/current-student.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/disbursement-information.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/transfer-student.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Apply for Aid Net Price Calculator Special and Unusual Circumstances - Professional Judgment Financial Support and Scholarships Summer Aid Graduate Student | Financial Aid Current Students | Financial Aid Transfer Student Disbursement Information Contact Us Please have your NUID number available.”
### `2cda6bd29fc22664` University of Nebraska at Omaha — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/tools-and-resources/satisfactory-academic-progress.php (sha256 4c6ac1050a31)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “For students utilizing the NE Waiver of Tuition, you will need to complete the SAP appeal process in order to reinstate eligibility.”
### `517cb2ca6e935cb6` University of Nebraska at Omaha — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/disbursement-information.php (sha256 06e21a4affe9)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “This is due to cost of attendance adjustments that need to be made that may cause a change in your Parent PLUS loan eligibility.”
### `625461fe74826caf` University of Nebraska at Omaha — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/summer-aid.php (sha256 cb1b93513115)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Apply for Aid Net Price Calculator Special and Unusual Circumstances - Professional Judgment Financial Support and Scholarships Summer Aid Graduate Student | Financial Aid Current Students | Financial Aid Transfer Student Disbursement Information Additional Resources Satisfactory Academic Progress Contact Us Please have your NUID number available.”
### `633bc22f8a07aee9` University of Nebraska at Omaha — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/transfer-student.php (sha256 2a0bd13173e6)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/current-student.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/disbursement-information.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/first-year-student.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Apply for Aid Net Price Calculator Special and Unusual Circumstances - Professional Judgment Financial Support and Scholarships Summer Aid Graduate Student | Financial Aid Current Students | Financial Aid Transfer Student Disbursement Information Contact Us Please have your NUID number available.”
### `7705b1ff4d6929b6` University of Nebraska at Omaha — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/disbursement-information.php (sha256 06e21a4affe9)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/current-student.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/first-year-student.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/transfer-student.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Apply for Aid Net Price Calculator Special and Unusual Circumstances - Professional Judgment Financial Support and Scholarships Summer Aid Graduate Student | Financial Aid Current Students | Financial Aid Transfer Student Disbursement Information Be informed!”
### `91109602656d067b` University of Nebraska at Omaha — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php (sha256 46b18e5c89d7)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/current-student.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/disbursement-information.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/first-year-student.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/transfer-student.php
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Section 479A of the HEA gives an institution’s FAA (Financial Aid Administrator) the authority to use professional judgment to adjust, on a case-by-case basis, the cost of attendance or the values of the items used in calculating the SAI (Student Aid Index) to reflect a student’s special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “Apply for Aid Net Price Calculator Special and Unusual Circumstances - Professional Judgment Financial Support and Scholarships Summer Aid Graduate Student | Financial Aid Current Students | Financial Aid Transfer Student Disbursement Information Be informed!”
### `95512cae2e2449fa` University of Nebraska at Omaha — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php (sha256 46b18e5c89d7)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/disbursement-information.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustments Computer purchase Dependent care (e.g. daycare) expenses Extended Family Support Circumstances We Do Not Consider Different university offering more aid Consumer debt, including credit card debt and car payments Parent's inability or unwillingness to borrow Federal Direct Parent PLUS Loans Parent refuses to provide financial support for higher education Parent refuse”
  - sentence: budget_increase ⟵ “If a student already has a Student Aid Index (SAI) of 0 - cost of attendance adjustments may be considered Graduate students: Cost of attendance adjustments may be considered Post-baccalaureate students (students who already have a bachelor's degree): No grant eligibility.”
  - sentence: budget_increase ⟵ “Cost of attendance adjustments may be considered.”
### `989a9f40978f3206` University of Nebraska at Omaha — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/current-student.php (sha256 09ca5daa4892)
- issues: semantic_review_required, conflicting_sources:https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/disbursement-information.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/first-year-student.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/special-circumstances.php,https://www.unomaha.edu/admissions/financial-support-and-scholarships/apply-for-aid/transfer-student.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Apply for Aid Net Price Calculator Special and Unusual Circumstances - Professional Judgment Financial Support and Scholarships Summer Aid Graduate Student | Financial Aid Current Students | Financial Aid Transfer Student Disbursement Information Most Competitive Tuition Rates in the Region UNO has the lowest tuition and fees of 10 Eastern Nebraska four-year institutions.”
### `014d7a64410bdccb` University of Nebraska at Omaha — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.unomaha.edu/undergraduate-admissions/tuition-and-aid/estimated-cost-of-attendance.php (sha256 e1b2a5af01dd)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees: 26400 ⟵ “Tuition and Fees | $9,880 | $14,528 | $26,400”
  - on_campus:Housing and Food: 13548 ⟵ “Housing and Food | $13,548 | $13,548 | $13,548”
  - on_campus:Books and Supplies: 1264 ⟵ “Books and Supplies | $1,264 | $1,264 | $1,264”
  - on_campus:Subtotal: 41212 ⟵ “Subtotal | $24,692 | $29,340 | $41,212”
  - on_campus:Personal Expenses: 2540 ⟵ “Personal Expenses | $2,540 | $2,540 | $2,540”
  - on_campus:Transportation: 1700 ⟵ “Transportation | $1,700 | $1,700 | $1,700”
  - on_campus:Total: 45452 ⟵ “Total | $28,932 | $33,580 | $45,452”
### `818407ceca8feefb` University of Nebraska at Omaha — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.unomaha.edu/undergraduate-admissions/tuition-and-aid/estimated-cost-of-attendance.php (sha256 e1b2a5af01dd)
- issues: ambiguous_year_labels, residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees: 14528 ⟵ “Tuition and Fees | $9,880 | $14,528 | $26,400”
  - on_campus:Housing and Food: 13548 ⟵ “Housing and Food | $13,548 | $13,548 | $13,548”
  - on_campus:Books and Supplies: 1264 ⟵ “Books and Supplies | $1,264 | $1,264 | $1,264”
  - on_campus:Subtotal: 29340 ⟵ “Subtotal | $24,692 | $29,340 | $41,212”
  - on_campus:Personal Expenses: 2540 ⟵ “Personal Expenses | $2,540 | $2,540 | $2,540”
  - on_campus:Transportation: 1700 ⟵ “Transportation | $1,700 | $1,700 | $1,700”
  - on_campus:Total: 33580 ⟵ “Total | $28,932 | $33,580 | $45,452”
### `81e33cf59d988908` University of Nebraska at Omaha — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.unomaha.edu/undergraduate-admissions/tuition-and-aid/estimated-cost-of-attendance.php (sha256 e1b2a5af01dd)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees: 9880 ⟵ “Tuition and Fees | $9,880 | $14,528 | $26,400”
  - on_campus:Housing and Food: 13548 ⟵ “Housing and Food | $13,548 | $13,548 | $13,548”
  - on_campus:Books and Supplies: 1264 ⟵ “Books and Supplies | $1,264 | $1,264 | $1,264”
  - on_campus:Subtotal: 24692 ⟵ “Subtotal | $24,692 | $29,340 | $41,212”
  - on_campus:Personal Expenses: 2540 ⟵ “Personal Expenses | $2,540 | $2,540 | $2,540”
  - on_campus:Transportation: 1700 ⟵ “Transportation | $1,700 | $1,700 | $1,700”
  - on_campus:Total: 28932 ⟵ “Total | $28,932 | $33,580 | $45,452”
### `99dc664d766696c9` University of Nebraska at Omaha — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.unomaha.edu/registrar/students/before-you-enroll/transfer-credit/advanced-placement-credit.php (sha256 e9ffe39f8c9d)
- issues: credits_implausible
- checks: {"distinct_exams": 36, "equivalencies": 46, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3+]:  ⟵ “2-D Art and Design | 3+ | ART 1210 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “3-D Art and Design | 3+ | ART 1110 | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3+]:  ⟵ “African American Studies | 3+ | BLST Lower Level Elective Credit | 3”
  - equivalencies[AP-ART-HISTORY|4+]:  ⟵ “Art History | 4+ | ART 2050 and 2060 | 6”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology (Effective through 2016 AP Exam) | 3 | BIOL 1450 | 5”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology (Effective through 2016 AP Exam) | 4-5 | BIOL 1450 and 1750 | 10”
  - equivalencies[AP-BIOLOGY|4+]:  ⟵ “Biology (Effective 2020 AP Exam - Current) | 4+ | BIOL 1450 | 5”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|4+]:  ⟵ “Business with Personal Finance | 4+ | FNBK 2280 | 3”
  - equivalencies[AP-CALCULUS-AB|3+]:  ⟵ “Calculus AB | 3+ | MATH 1950 | 5”
  - equivalencies[AP-CALCULUS-BC|3+]:  ⟵ “Calculus BC | 3+ | MATH 1950 and 1960 | 9”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry (Effective through 2014 AP Exam) | 3 | CHEM 1180 + 1184 | 4”
  - equivalencies[AP-CHEMISTRY|4-5]:  ⟵ “Chemistry (Effective through 2014 AP Exam) | 4-5 | CHEM 1180 + 1184 + 1190 | 7”
  - equivalencies[AP-CHEMISTRY|4+]:  ⟵ “Chemistry (Effective 2015 AP Exam - Current) | 4+ | CHEM 1180 + 1184 | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3+]:  ⟵ “Chinese Language & Culture | 3+ | CHIN 1110 | 5”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|4+]:  ⟵ “Comparative Government & Politics | 4+ | PSCI 2500 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3+]:  ⟵ “Computer Science A | 3+ | CIST 1400 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4+]:  ⟵ “Computer Science Principles | 4+ | CSCI 1200 | 3”
  - equivalencies[AP-CYBERSECURITY|3+]:  ⟵ “Cybersecurity | 3+ | CYBR 1100 | 3”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Drawing | 3+ | ART 1100 | 3”
  - equivalencies[AP-DRAWING|English Language & Composition or English Literature & Composition]:  ⟵ “Drawing | English Language & Composition or English Literature & Composition | 3 | Places into ENGL 1150”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Drawing | 4 | Places into ENGL 1160 •Check with the English Department regarding procedures for earning retroactive credit”
  - equivalencies[AP-DRAWING|5]:  ⟵ “Drawing | 5 | Places into 2000 level English •Check with the English Department regarding procedures for earning retroactive credit”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science | 3+ | GEOG 1050 | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|3+]:  ⟵ “European History | 3+ | Humanities OR Cultural Knowledge MavEd General Education Equivalent* (Previously Global Diversity/Humanities Fine Art General Education elective) | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4+]:  ⟵ “French Language & Culture | 4+ | FREN 1210, 1220, 2210, 2220, and 2240 | 15”
  - … 21 more rows
### `038e5cf41f54ba9f` University of Nebraska-Lincoln — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.unl.edu/maintaining-eligibility/satisfactory-academic-progress/ (sha256 c960c81ec8c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 15}
  - sentence: sap_appeal ⟵ “SAP Appeal Forms [1] Financial aid includes, but is not limited to, all federal grants, loans and work-study; state grants; and most University of Nebraska need-based grants and scholarships.”
  - sentence: sap_appeal ⟵ “Students who drop or withdraw from courses while on a SAP approved appeal (SAP Academic Plan) may lose their financial aid eligibility in subsequent semesters.”
  - sentence: sap_appeal ⟵ “Should students who are on a SAP approved appeal (SAP Academic Plan) earn an incomplete, they may be in jeopardy of losing financial aid eligibility in subsequent semesters.”
  - sentence: sap_appeal ⟵ “If however, you may have over 90 transfer credit hours and you have been notified that you are not meeting SAP as you have exceeded the maximum time frame allowed, you may want to check with your student services specialist at Husker Hub to learn if a SAP appeal is possible.”
  - sentence: sap_appeal ⟵ “Appeal Process When students are notified that they do not meet the satisfactory academic progress policy requirements, they have the right to appeal that decision.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Committee reviews the appeal and makes the decision to approve or deny the appeal.”
### `2b9f276327a867cf` University of Nebraska-Lincoln — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.unl.edu/additional-information/scholarship-appeals/ (sha256 360a0e33c6cb)
- issues: semantic_review_required, conflicting_sources:https://admissions.unl.edu/cost/financial-aid/guide-to-your-offer/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Who May Request Scholarship Reconsideration Incoming Students You may request a scholarship reconsideration if you experienced significant or unusual circumstances that affected your academic performance or your ability to be fully considered during the selection process.”
### `4fef1a130d851911` University of Nebraska-Lincoln — appeals 2025-26 [new] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/ (sha256 59c5f638dff2)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If your actual costs exceed the standard COA, for example, due to dependent care, disability-related expenses, study abroad, or cooperative education, you may request an adjustment through a professional judgment review.”
### `6de50c72f932c35d` University of Nebraska-Lincoln — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.unl.edu/maintaining-eligibility/scholarship-guidelines/ (sha256 a2d43bf4e915)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If your scholarship is not renewed, visit the Scholarships Appeals page to learn about appeal options.”
### `a996da2dbee9b7d6` University of Nebraska-Lincoln — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.unl.edu/cost/financial-aid/guide-to-your-offer/ (sha256 24dcb3e8186a)
- issues: semantic_review_required, conflicting_sources:https://financialaid.unl.edu/additional-information/scholarship-appeals/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Let Husker Hub know if you experience a sudden change in income or expenses.”
  - sentence: need_based_special_circumstances ⟵ “We may be able to reassess your family's aid eligibility in the event of a special and unusual circumstance, such as loss of income, divorce, death in the family, layoff, etc.”
### `3c4ebd4ed731fe67` University of Nebraska-Lincoln — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/2025-2026/ (sha256 053b2f999cc9)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 11100 ⟵ “Tuition & Fees | $11,100 | $30,330”
  - on_campus:Housing & Food: 14210 ⟵ “Housing & Food | $14,210 | $14,210”
  - on_campus:Books & Supplies: 1128 ⟵ “Books & Supplies | $1,128 | $1,128”
  - on_campus:Personal Expenses: 2300 ⟵ “Personal Expenses | $2,300 | $2,300”
  - on_campus:Loan Fees (if applicable): 64 ⟵ “Loan Fees (if applicable) | $64 | $64”
  - on_campus:Total: 28802 ⟵ “Total | $28,802 | $48,032”
### `3d2069693a7b9d54` University of Nebraska-Lincoln — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://admissions.unl.edu/information-for/nebraska-now/ (sha256 2c30499aad5d)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Junior Year Fall:: 543 ⟵ “Junior Year Fall: | $543”
  - column:Junior Year Spring:: 543 ⟵ “Junior Year Spring: | $543”
  - column:Senior Year Fall:: 543 ⟵ “Senior Year Fall: | $543”
  - column:Senior Year Spring:: 543 ⟵ “Senior Year Spring: | $543”
  - column:Tuition Savings:: 2172 ⟵ “Tuition Savings: | $2,172”
### `7806da8759c2b204` University of Nebraska-Lincoln — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.unl.edu/cost/estimated-cost-attendance/2025-2026/ (sha256 053b2f999cc9)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 30330 ⟵ “Tuition & Fees | $11,100 | $30,330”
  - on_campus:Housing & Food: 14210 ⟵ “Housing & Food | $14,210 | $14,210”
  - on_campus:Books & Supplies: 1128 ⟵ “Books & Supplies | $1,128 | $1,128”
  - on_campus:Personal Expenses: 2300 ⟵ “Personal Expenses | $2,300 | $2,300”
  - on_campus:Loan Fees (if applicable): 64 ⟵ “Loan Fees (if applicable) | $64 | $64”
  - on_campus:Total: 48032 ⟵ “Total | $28,802 | $48,032”
### `4fb845c5e5517720` Wayne State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wsc.edu/financial-aid/applying-financial-aid/5 (sha256 9071ae0e1a9d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If approved, professional judgement will be used to make changes to the specific data elements within the FAFSA that in turn may impact a student’s Student Aid Index (SAI) and/or level of financial need.”
### `69275671eeac4831` Wayne State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wsc.edu/financial-aid/first-responder-dependent-education-benefit (sha256 977ae0911825)
- issues: semantic_review_required, conflicting_sources:https://www.wsc.edu/financial-aid/applying-financial-aid/5
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Contact Financial Aid For additional assistance, please contact the Financial Aid Office: Address: Hahn Administration, 104 Telephone: 402-375-7229 Email: [email protected] Applying for Financial Aid How to Apply for Aid Eligibility Requirements Financial Aid Disbursements and Refunds FAFSA Verification Process FAFSA Special Circumstances Financial Aid FAQs Cost and Payment Information Cost of Att”
### `7581204d90b6f12c` Wayne State College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wsc.edu/financial-aid/applying-financial-aid/5 (sha256 9071ae0e1a9d)
- issues: semantic_review_required, conflicting_sources:https://www.wsc.edu/financial-aid/first-responder-dependent-education-benefit
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Submit a Special Circumstances Request Special Circumstances Consideration Wayne State College reserves the right to consider special circumstance requests for students and/or their parents who have experienced a significant and prolonged decline in family income due to extenuating circumstances beyond their control.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstance requests are reviewed on a case-by-case basis as every request is unique.”
  - sentence: need_based_special_circumstances ⟵ “Examples of circumstances that may be considered include the following: Loss of employment Other loss of income Separation or divorce (parents' marital status) Death of a parent or spouse High unreimbursed medical and/or dental expenses that were not reported in federal taxes Dependency override Student marital status change Special circumstance requests will not be considered for the following re”
  - sentence: need_based_special_circumstances ⟵ “Before submitting a special circumstance appeal request, the student must have already completed the FAFSA, and if their FAFSA was selected for verification, the verification requirements must be submitted before a special circumstance appeal will be reviewed.”
  - sentence: need_based_special_circumstances ⟵ “If you have received your aid package and you believe that you have experienced a circumstance that warrants consideration, please complete the Financial Aid Special Circumstances Form here.”
  - sentence: need_based_special_circumstances ⟵ “How long does the special circumstance request process take?”
### `8bfe8708613a6370` Western Nebraska Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wncc.edu/admissions-aid/financial-aid/policies (sha256 14cdfdf2e8fc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “More information regarding scholarship eligibility can be found on our Scholarships page. | Professional Judgment and Appeal Options The WNCC Financial Aid Office has established appeal procedures to allow for adjustments to a student’s Free Application for Federal Student Aid (FAFSA) when the student has experienced special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “Under federal financial aid regulations, financial aid administrators may utilize “professional judgment” to make adjustments to a student’s FAFSA data elements on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “Students may appeal to have these “professional judgment” situations considered by submitting to the WNCC Financial Aid Office the appropriate appeal form along with substantiating documents that support the circumstance.”
  - sentence: professional_judgment ⟵ “Students who believe they may qualify for a Professional Judgment appeal may contact the WNCC Financial Aid Office to initiate a conversation about their situation.”
  - sentence: professional_judgment ⟵ “Not all requests for professional judgment will result in an increase in financial aid eligibility.”
  - sentence: professional_judgment ⟵ “Professional judgment decisions made by the WNCC Financial Aid Office are not appealable to the U.S.”
### `aa85ed0fd22d2ecc` Western Nebraska Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wncc.edu/admissions-aid/financial-aid/policies (sha256 14cdfdf2e8fc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Show AllHide All Special Circumstances Special Circumstances refer to financial changes to the household which affect the financial data reported on the student’s FAFSA.”
### `c3d1a5548c98f10a` Western Nebraska Community College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.wncc.edu/admissions-aid/tuition-fees/index (sha256 6eb512ff47da)
- issues: ambiguous_year_labels, cost_period_semester
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 3945 ⟵ “Tuition | $3,945”
  - on_campus:Fees: 555 ⟵ “Fees | $555”
  - on_campus:Books, Course Materials, Supplies, and Equipment: 1500 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,500”
  - on_campus:Housing: 3651 ⟵ “Housing | $3,651”
  - on_campus:Food: 5974 ⟵ “Food | $5,974”
  - on_campus:Personal: 1616 ⟵ “Personal | $1,616”
  - on_campus:Transportation: 1227 ⟵ “Transportation | $1,227”
  - on_campus:TOTAL: 18468 ⟵ “TOTAL | $18,468”
### `fd96f328261f420e` Western Nebraska Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.wncc.edu/admissions-aid/tuition-fees/index (sha256 6eb512ff47da)
- issues: ambiguous_year_labels, cost_period_semester, residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 3345 ⟵ “Tuition | $3,345”
  - on_campus:Fees: 555 ⟵ “Fees | $555”
  - on_campus:Books, Course Materials, Supplies, and Equipment: 1500 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,500”
  - on_campus:Housing: 3651 ⟵ “Housing | $3,651”
  - on_campus:Food: 5974 ⟵ “Food | $5,974”
  - on_campus:Personal: 1616 ⟵ “Personal | $1,616”
  - on_campus:Transportation: 1227 ⟵ “Transportation | $1,227”
  - on_campus:TOTAL: 17868 ⟵ “TOTAL | $17,868”
### `a81051402e68e36b` York University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.york.edu/financial-aid/scholarships.php (sha256 120529fe4946)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “This Need Based Application gives you the opportunity to share more details about your circumstances so we can see if you may qualify for additional aid or a Professional Judgment (an adjustment to your FAFSA information).”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 1; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- Bryan College of Health Sciences (`ipeds-180878`)
- Doane University (`ipeds-181020`)
- Peru State College (`ipeds-181534`)
- College of Saint Mary (`ipeds-181604`)

## Leads: official pages found with no extracted record

- Bellevue University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, degree_requirements, aid_appeals
- Central Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Chadron State College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, transfer_credit, degree_requirements, aid_appeals
- Clarkson College: admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Concordia University-Nebraska: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, degree_requirements
- Creighton University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Hastings College: cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit
- Little Priest Tribal College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Metropolitan Community College Area: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Mid-Plains Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- Midland University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Nebraska College of Technical Agriculture: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, degree_requirements
- Nebraska Indian Community College: admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, degree_requirements
- Nebraska Methodist College of Nursing & Allied Health: admissions_tests, common_data_set, merit_scholarships, ap_credit, ib_credit, transfer_credit
- Nebraska Wesleyan University: admissions_tests, statewide_articulation, degree_requirements, aid_appeals
- Northeast Community College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, residency, degree_requirements
- Southeast Community College Area: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, dual_enrollment, degree_requirements
- Summit Christian College: cost_of_attendance
- Union Adventist University: transfer_credit
- University of Nebraska at Kearney: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, residency
- University of Nebraska at Omaha: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- University of Nebraska-Lincoln: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Wayne State College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Western Nebraska Community College: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, degree_requirements
- York University: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit
