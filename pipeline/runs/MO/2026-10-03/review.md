# Review queue — MO (2026-27)

Pages fetched: 4002; failures: 475. Candidates: 427 (158 without issues, 269 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 11 | 14 | 33 | 7 | 5 |
| cost_of_attendance | 0 | 0 | 7 | 6 | 47 | 5 | 5 |
| admissions_tests | 0 | 0 | 0 | 2 | 54 | 9 | 5 |
| common_data_set | 0 | 0 | 0 | 2 | 4 | 59 | 5 |
| merit_scholarships | 0 | 0 | 9 | 10 | 37 | 9 | 5 |
| ap_credit | 0 | 0 | 7 | 9 | 11 | 38 | 5 |
| clep_credit | 0 | 0 | 9 | 7 | 10 | 39 | 5 |
| ib_credit | 0 | 0 | 6 | 7 | 7 | 45 | 5 |
| dual_enrollment | 0 | 0 | 18 | 10 | 15 | 22 | 5 |
| transfer_credit | 0 | 0 | 10 | 4 | 41 | 10 | 5 |
| statewide_articulation | 0 | 0 | 0 | 0 | 15 | 50 | 5 |
| residency | 0 | 0 | 0 | 0 | 22 | 43 | 5 |
| degree_requirements | 0 | 0 | 1 | 0 | 43 | 21 | 5 |
| aid_appeals | 0 | 0 | 0 | 33 | 9 | 23 | 5 |

## Ready for review (158)

### `b23cbbab61c79a14` Calvary University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.calvary.edu/wp-content/uploads/2025/04/Transfer-Credit.pdf (sha256 cad636f1126e)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: B ⟵ “Transfer credit may be granted for courses where: • A grade of B or above was earned, • The courses are equivalent to and meet degree requirements for the focus chosen at Calvary, and • The seminary or graduate school is accredited by an institutional accrediting agency recognized by the Commission on Recognition of Postsecondary Accreditation (CORPA) and listed by the American Council on Educatio”
  - max_transfer_credits: 24 ⟵ “Students coming to Calvary University from non-accredited institutions may receive up to a maximum of 24 credit hours transferred for Bible courses taken at those institutions.”
### `34406595713efb11` College of the Ozarks — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.cofo.edu/transfercredit (sha256 309fa853bd89)
- checks: {"distinct_exams": 14, "equivalencies": 23, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | HL | 4 to 7 | BIO 1004 | 4”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | SL | 4 to 7 | SCI 100 | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|3]:  ⟵ “Business Management | HL | 4 to 7 | BUS 213 | 3”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | HL | 4 to 5 | CHE 141 | 4”
  - equivalencies[IB-CHEMISTRY|8]:  ⟵ “Chemistry | HL | 6 to 7 | CHE 114 and CHE 124 | 8”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | SL | 4 to 7 | CHE 1004 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|3]:  ⟵ “Computer Science | HL | 4 to 7 | CSC 133 | 3”
  - equivalencies[IB-ECONOMICS|6]:  ⟵ “Economics | HL | 4 to 7 | ECN 203 and ECN 213 | 6”
  - equivalencies[IB-ECONOMICS|3]:  ⟵ “Economics | SL | 4 to 5 | ECN 203 | 3”
  - equivalencies[IB-HISTORY|3]:  ⟵ “History (Americas) | HL | 4 to 7 | HTY 253 | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|5]:  ⟵ “Mathematics: Analysis and Approaches | HL | 4 to 5 | MAT 175 | 5”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|10]:  ⟵ “Mathematics: Analysis and Approaches | HL | 6 to 7 | MAT 175 and MTH 205 | 10”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|3]:  ⟵ “Mathematics: Analysis and Approaches | SL | 5 to 7 | MAT 133 | 3”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|3]:  ⟵ “Mathematics: Applications and Interpretation | HL | 4 to 7 | MAT 123 | 3”
  - equivalencies[IB-MUSIC|3]:  ⟵ “Music | HL | 4 to 7 | MUS 103 | 3”
  - equivalencies[IB-PHILOSOPHY|3]:  ⟵ “Philosophy | HL | 4 to 7 | PHI 203 | 3”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics | HL | 4 | PHY 214 | 4”
  - equivalencies[IB-PHYSICS|8]:  ⟵ “Physics | HL | 5 to 7 | PHY 214 and PHY 224 | 8”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics | SL | 4 to 7 | PHY 1004 | 4”
  - equivalencies[IB-PSYCHOLOGY|3]:  ⟵ “Psychology | HL | 4 to 7 | PSY 103 | 3”
  - equivalencies[IB-SPANISH|9]:  ⟵ “Spanish | HL | 5 to 7 | SPA 143 & SPA 153 & SPA 203 | 9”
  - equivalencies[IB-SPANISH|6]:  ⟵ “Spanish | SL | 4 to 7 | SPA 145 & SPA 153 | 6”
  - equivalencies[IB-THEATRE|3]:  ⟵ “Theatre | HL | 4 to 7 | DRM 103 | 3”
### `bac8a41e98921385` College of the Ozarks — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.cofo.edu/transfercredit (sha256 309fa853bd89)
- checks: {"distinct_exams": 25, "equivalencies": 28, "rows_without_score": 0}
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language & Composition | 4 | 3 | ENG 103”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition | 3 | 3 | ENG 163”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIO 1004”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | MAT 175”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 8 | MAT 175 & MAT 205”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus AB sub-score on Calculus BC | 3 | 4 | MAT 175”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHE 1004”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 3 | CSC 133”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 4 | BIO 1034”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1: Algebra-Based | 3 | 4 | PHY 214”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2: Algebra-Based | 3 | 4 | PHY 224”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C: Mechanics | 3 | 4 | PHY 234”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity & Magnetism | 3 | 4 | PHY 244”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus | 3 | 3 | MAT 133”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | 3 | MAT 143”
  - equivalencies[AP-EUROPEAN-HISTORY|5]:  ⟵ “European History | 5 | 6 | HTY 153 and HTY 163”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 | HTY 153 or HTY 163”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | HTY 203”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 3 | ECN 203”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 3 | ECN 213”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | 3 | PSY 103”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government & Politics | 3 | 3 | POL 103”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “U.S. History | 3 | 3 | HTY 253”
  - equivalencies[AP-WORLD-HISTORY-MODERN|5]:  ⟵ “World History: Modern | 5 | 6 | HTY 153 and HTY 163”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History: Modern | 3 | 3 | HTY 153 or HTY 163”
  - … 3 more rows
### `e2fa7336c7fe8a99` College of the Ozarks — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.cofo.edu/transfercredit (sha256 309fa853bd89)
- checks: {"distinct_exams": 26, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 | ENG 163”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | 3 | ENG 163”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|56]:  ⟵ “College Composition | 56 | 3 | ENG 103”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 | ENG 163”
  - equivalencies[CLEP-HUMANITIES|52]:  ⟵ “Humanities | 52 | 3 | Lower Division Elective”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 4 | BIO 1004”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 5 | MAT 175”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 4 | CHE 1004”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | MAT 133”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | MAT 123”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | 3 | Lower Division Elective”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 3 | MAT 153”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|53]:  ⟵ “American Government | 53 | 3 | POL 103”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology | 50 | 3 | Lower Division Elective”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|55]:  ⟵ “Introductory Psychology | 55 | 3 | Lower Division Elective”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | FAM 103”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 50 | 3 | HTY 153”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II | 50 | 3 | HTY 163”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|60]:  ⟵ “Information Systems | 60 | 3 | CSC 113”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 | ECN 203”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 | MGT 213”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 | ECN 213”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 3 | MKT 223”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language: Levels 1 and 2 | 50 | 3 | FRN 103”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “French Language: Levels 1 and 2 | 62 | 6 | FRN 103 and FRN 113”
  - … 4 more rows
### `097be2e0a89ba5ba` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Two-in-Family | $500 | $2,000”
### `32b07bfda0db6d0f` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - award_amount_text: $29,834 (annual full tuition) ⟵ “Presidential Scholarship | $29,834 (annual full tuition) | $119,336”
### `51efd914dcaa471c` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Disciples of Christ (DOC) Award | $1,000 | $4,000”
### `522deb3862261f81` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - award_amount_text: $1,000-2,000 ⟵ “Music/Art Talent Award | $1,000-2,000 | $4,000-8,000”
### `72b9a0341d84b3e2` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “A+ Recognition Award | $1,500 | $6,000”
### `88bd6b484a72c3b3` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - gpa_requirement: 3.22 - 3.72 ⟵ “CC Achievement Scholarship | 3.22 - 3.72”
### `b062d41ac1839c55` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Alumni Legacy Grant | $1,000 | $4,000”
### `c9392238a957e444` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - award_amount_text: $22,376 (75% annual tuition) ⟵ “Provost Scholarship | $22,376 (75% annual tuition) | $89,504”
### `ce03f534310ed0f0` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - gpa_requirement: 2.76 - 3.21 ⟵ “CC Recognition Scholarship | 2.76 - 3.21”
### `e26976bb0ed4cc31` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 and below ⟵ “Navy & Silver Award | 2.75 and below”
### `f4cd0825f19f7ad9` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/scholarships/traditional-students (sha256 4853b8d49c45)
- checks: {"thresholds": null}
  - gpa_requirement: 3.73 and over ⟵ “CC Distinction Scholarship | 3.73 and over”
### `be06ed2ba4a199f0` Columbia College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/college-cost/ (sha256 457fe969de0b)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 29354 ⟵ “Tuition | $14,677 | $29,354 | $33,992”
  - on_campus:Books: 480 ⟵ “Books | $240 | $480 | $720”
  - on_campus:Housing: 6626 ⟵ “Housing | $3,313 | $6,626 | $18,266”
  - on_campus:Food: 5400 ⟵ “Food | $2,700 | $5,400 | -”
  - on_campus:Transportation: 1760 ⟵ “Transportation | $880 | $1,760 | $3,088”
  - on_campus:Personal: 4480 ⟵ “Personal | $2,240 | $4,480 | $8,928”
  - on_campus:Loan Fees: 32 ⟵ “Loan Fees | $16 | $32 | $48”
  - on_campus:Cost of Attendance: 48132 ⟵ “Cost of Attendance | $24,066 | $48,132 | $65,042”
### `12015a2a4e25767a` Columbia College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ccis.edu/_files/admissions/apply-for-college/undergraduate-admission/hs-dual-enrollment-authorization-form-pdf.pdf (sha256 cd8ed07c9964)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “Is an 11th or 12th grader who has a cumulative high school GPA of 2.5 or higher.”
### `m32c64f72a44944d` Columbia College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ccis.edu/admissions/transfer/work-credit/ (sha256 4455bfa3b549)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - min_grade: B ⟵ “A maximum of nine semester hours, with grades of "B" or higher, may be transferred.”
  - residency_requirement_credits: 36 ⟵ “Note: Completion of the corrections academy within the last 36 semester hours of a student’s degree program may reduce the number of hours applied under the Partners in Corrections Program.”
  - residency_requirement_credits: 36 ⟵ “Note: Completion of the police academy within the last 36 semester hours of a student’s degree program may reduce the number of hours applied under the partners in Law Enforcement Program.”
### `0b6fd739b48a20c3` Cottey College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://catalog.cottey.edu/advanced-placement-ap (sha256 48a8552d4087)
- checks: {"distinct_exams": 25, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “2-D Art and Design | 4 | 4 | ART 111 | Pending portfolio review”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “3-D Art and Design | 4 | 4 | ART 112 | Pending portfolio review”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 5 | BIO 107 | ”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3]:  ⟵ “Business with Personal Finance | 3 | 8 | BUS 101, BUS 103 | ”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | MAT 210 | ”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 8 | MAT 210, 220 | ”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 5 | CHE 160 | ”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 10 | CHE 160, CHE 170 | ”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|4]:  ⟵ “Comparative Government & Politics | 4 | 4 | POL 201 | ”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Drawing | 4 | 4 | ART 131 | Pending portfolio review”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Language & Composition | 5 | 4 | WRI 102 | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature & Composition | 4 | 4 | ENG 103 | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | 4 | 4 | ENV 110 | ”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | 4 | HIS 260 | ”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Lang & Culture | 3 | 8 | Satisfies language requirement I and II | ”
  - equivalencies[AP-MACROECONOMICS|4]:  ⟵ “Macroeconomics | 4 | 3 | BUS 285 (if both macroeconomics/microeconomics exams are passed with a 4 or higher). | ”
  - equivalencies[AP-MICROECONOMICS|4]:  ⟵ “Microeconomics | 4 | 3 | BUS 285 (if both macroeconomics/microeconomics exams are passed with a 4 or higher). | ”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 | 4 | 5 | PHY 205 | ”
  - equivalencies[AP-PHYSICS-2|5]:  ⟵ “Physics 2 | 5 | 5 | PHY 206 | ”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Pre-Calculus | 3 | 5 | MAT 120 | ”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | 4 | PSY 101 | ”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language & Culture | 3 | 8 | Satisfies language requirement I and II | ”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | 4 | MAT 130 | ”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “US Government & Politics | 4 | 4 | POL 101 | ”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “US History | 4 | 4 | HIS 111 | ”
  - … 2 more rows
### `597c930894652903` Cottey College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://catalog.cottey.edu/international-baccalaureate-ib (sha256 2c93345e0edf)
- checks: {"distinct_exams": 13, "equivalencies": 14, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-SL|HL 4]:  ⟵ “Biology (SL/HL) | 4 | 5 | BIO 101/L | ”
  - equivalencies[IB-CHEMISTRY-HL|HL 4]:  ⟵ “Chemistry (HL) | 4 | 5 | CHE 160 | Pending lab work review”
  - equivalencies[IB-CHEMISTRY-HL|HL 5]:  ⟵ “Chemistry (HL) | 5 | 10 | CHE 160, CHE 170 | Pending lab work review”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|HL 6]:  ⟵ “English A: Lang & Lit (HL) | 6 | 4 | WRI 102 | ”
  - equivalencies[IB-FRENCH-HL|HL 4]:  ⟵ “French B (HL) | 4 | 8 | Language requirements I & II | ”
  - equivalencies[IB-GEOGRAPHY-SL|HL 4]:  ⟵ “Geography (SL/HL | 4 | 4 | ENV 125 | ”
  - equivalencies[IB-GLOBAL-POLITICS-SL|HL 5]:  ⟵ “Global Politics (SL/HL) | 5 | 4 | POL 151 | ”
  - equivalencies[IB-MUSIC-SL|HL 5]:  ⟵ “Music (SL/HL) | 5 | 4 | MUS 101 | ”
  - equivalencies[IB-PHILOSOPHY-HL|HL 4]:  ⟵ “Philosophy (HL) | 4 | 4 | PHI 205 | Optional Themes: Ethics AND Philosophy and Contemporary Society”
  - equivalencies[IB-PHYSICS-SL|HL 5]:  ⟵ “Physics (SL/HL) | 5 | 5 | PHY 101 | ”
  - equivalencies[IB-PSYCHOLOGY-SL|HL 5]:  ⟵ “Psychology (SL/HL) | 5 | 4 | PSY 101 | ”
  - equivalencies[IB-SPANISH-HL|HL 4]:  ⟵ “Spanish B (HL) | 4 | 8 | Language requirements I & II | ”
  - equivalencies[IB-VISUAL-ARTS-HL|HL 5]:  ⟵ “Visual Arts (HL) | 5 | 4 | ART 111 | Pending portfolio review”
  - equivalencies[IB-VISUAL-ARTS-SL|SL 7]:  ⟵ “Visual Arts (SL) | 7 | 4 | ART 111 | Pending portfolio review”
### `d550e9ea1167b197` Cottey College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.cottey.edu/college-level-examination-program-clep (sha256 fbdbe1424237)
- checks: {"distinct_exams": 10, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 4 | POL 101 | ”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 4 | ENG 103 | Essay Required”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpret Lit | 50 | 4 | ENG 103 | Essay Required”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 5 | MAT 210 | ”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 5 | CHE 160 | Pending lab work review”
  - equivalencies[CLEP-CHEMISTRY|65]:  ⟵ “Chemistry | 65 | 10 | CHE 160, CHE 170 | Pending lab work review”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 4 | MAT 110 | ”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 4 | ENG 103 | Essay Required”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 4 | SOC 101 | ”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 5 | MAT 120 | ”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology | 50 | 4 | PSY 101 | ”
### `m8f8c692de996571` Cottey College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.cottey.edu/transfer-applicants (sha256 3a48a1f0ecf4)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - residency_requirement_credits: 30 ⟵ “NOTE: Transfer students must also meet residency requirements (students must complete 30 of the last 40 credit hours at Cottey).”
  - residency_requirement_credits: 30 ⟵ “Students must complete 30 of the last 40 credit hours at Cottey.”
### `c716bd94e8103496` Culver-Stockton College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://culver.edu/admissions/ap-credit/ (sha256 139dfa3102a1)
- checks: {"distinct_exams": 29, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “American Gov/Politics | 3 | 3 | POS 205”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “American History | 3 | 3 | HIS 107 or HIS 108”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | ART 340 or ART 341”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art - Drawing | 3 | 3 | ART 119”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 3 | BIO 110”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | MAT 120”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 4 | MAT 120”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 3 | CHE 251”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Gov/Politics | 3 | 3 | POS 304”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 3 | Computer Science Elective”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 3 | NAS 108”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 | HIS 380”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Comp | 3 | 3 | ENG 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Comp | 3 | 3 | ENG 202”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | 3 | FRN 106”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Literature | 3 | 3 | French Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | 3 | GER 106”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | GEO 201”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin/Vergil | 3 | 3 | Latin Elective”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 3 | ECO 201”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 3 | ECO 202”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 3 | MUS 101”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | 3 | PSY 101”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C - Mechanics | 3 | 3 | Physics Elective”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language | 3 | 3 | SPN 205 Interm Spanish I”
  - … 5 more rows
### `1c62c3fe579bfd2f` Culver-Stockton College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://culver.edu/admissions/transfer-readmit-students/ (sha256 2f14a5d08f96)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “Thirty of the last 45 semester hours must be earned in residence at Culver-Stockton (with the possible exception of students transferring in the last year from an accredited professional school, such as clinical laboratory science, occupational therapy, etc.) All candidates for a degree must earn at least 40 semester hours in upper-division courses (300-or-400 level courses) and at least 12 hours ”
### `c0afcc9d66da9159` East Central College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.eastcentral.edu/registrar/credit-by-exam/ (sha256 416362b7d7f0)
- checks: {"distinct_exams": 28, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACC 101 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BUS 234 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BUS 151 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | BUS 111 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSY 250 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | EDU ELEC** (elective) | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSY 101 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOS 101 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECO 101 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECO 102 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | CIV 201 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present | 50 | CIV 202 | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | PSC ELEC* | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 | HST ELEC* | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present | 50 | HST ELEC* | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 221 or ENG 222 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | ENG ELEC (elective) | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENG 101 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 210 or ENG 211 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | ENG 101 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | HUM ELEC (elective) | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1 | 50 | HUM ELEC | 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, Level 2 | 59 | HUM ELEC | 12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1 | 50 | HUM ELEC | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language, Level 2 | 60 | HUM ELEC | 12”
  - … 6 more rows
### `m3963dac32ae5584` East Central College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.eastcentral.edu/earlycollege/ (sha256 0bbde05b84b2)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Freshmen must have an overall minimum grade point average of 3.0 (on a 4.0 scale), score at the 90th percentile or above on the ACT or SAT, and a signed letter of recommendation from the school’s counselor, principal, and student’s parent/guardian.”
  - state_grant_accepted: True ⟵ “To apply for the Dual Credit Scholarship, visit Missouri Department of Higher Education & Workforce Development for more information and to apply for funding.”
### `6e7bc45e0f6ca3d5` Fontbonne University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.fontbonne.edu/admission-aid/transfer/transfer-credit-agreements/ (sha256 316f45ac6c8e)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 64 ⟵ “A maximum of 64 hours can be transferred from two-year institutions, though there is no limit on the number of credits transferred from four-year institutions.”
### `m8cc28b55266a168` Kansas City Art Institute — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://www.kcai.edu/admissions-aid/transferring-credit-faqs/ (sha256 b82f8f57cd38)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “KCAI will consider transferring a maximum total of 63 credits in liberal arts and/or studio that meet KCAI’s requirements, with a grade of “C” or better and non-graded courses for which the student earned credits equivalent to a "C" or better: Satisfactory (S), Pass (P) or Credit (C or CR). (Additional documentation may need to be submitted regarding non-grade courses and their grade equivalents i”
  - min_grade: C ⟵ “KCAI will consider transferring a maximum total of 63 credits in liberal arts and/or studio that meet KCAI’s requirements, with a grade of “C” or better and non-graded courses for which the student earned credits equivalent to a "C" or better: Satisfactory (S), Pass (P) or Credit (C or CR). (Additional documentation may need to be submitted regarding non-grade courses and their grade equivalents i”
### `m7e475378d5e231c` Lincoln University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.lincolnu.edu/admissions/dual-credit-and-dual-enrollment/parents.html (sha256 2dfe6b1afca2)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 6, "tiers": 3}
  - eligibility_tier: 3.0 ⟵ “Students in the 11th and 12th grades with an overall minimum grade point average (GPA) of 3.0 (on a 4.0 scale) are automatically eligible for dual credit.”
  - eligibility_tier: 3.0 ⟵ “Students in the 10th grade must have an overall grade point average of 3.0 (on a 4.0 scale), must provide a signed letter of recommendation from their principal and guidance counselor, and provide written permission from a parent or legal guardian.”
  - eligibility_tier: 3.0 ⟵ “Students in the 9th grade must have an overall minimum grade point average of 3.0 (on a 4.0 scale), score at or above the 90th percentile on the ACT or SAT, provide a signed letter of recommendation from their principal and guidance counselor, and provide written permission from a parent or legal gu”
  - per_credit_hour_charge: 150 ⟵ “Tuition for Lincoln Dual Enrollment classes is $150 per credit hour. Additional on-campus fees may apply, such as laboratory fees.”
  - state_grant_accepted: True ⟵ “The Dual Credit/Dual Enrollment Scholarship covers tuition and fees for high school students taking dual credit or dual enrollment coursework. For more information, please visit the MO DHEWD Dual Credit / Dual Enrollment Scholarship page.”
  - per_credit_hour_charge: 150 ⟵ “The tuition for online dual enrollment classes is $150.00 per credit hour. No additional fees are associated with online dual enrollment; however, students will be responsible for purchasing textbooks for the courses.”
  - eligibility_tier: 3.0 ⟵ “Students in 11th and 12th grades with an overall minimum grade point average of 3.0 (on a 4.0 scale) are automatically eligible for dual credit courses.”
  - eligibility_tier: 3.0 ⟵ “Students in the 10th grade must have an overall minimum grade point average of 3.0 (on a 4.0 scale) and must provide a signed letter of recommendation from their principal and guidance counselor and provide written permission from a parent or legal guardian.”
  - eligibility_tier: 3.0 ⟵ “Students in the 9th grade must have an overall minimum grade point average of 3.0 (on a 4.0 scale), score in the 90th percentile or above on the ACT or SAT, and provide a signed letter of recommendation from their principal and guidance counselor and provide written permission from a parent or legal”
  - per_credit_hour_charge: 75 ⟵ “Tuition for dual credit courses is $75.00 per credit hour.  There are no additional fees associated with dual credit courses.”
### `dbe7aab8e8266a4c` Lincoln University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.lincolnu.edu/admissions/transfer/state-tech-college.html (sha256 3c90aa8d729f)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 60 ⟵ “There is a maximum of 60 credit hours eligible for transfer.”
### `cc494ac50d04b2d5` Lindenwood University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lindenwood.edu/student-financial-services/cost-of-attendance/ (sha256 ce5ded391b5a)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 22360 ⟵ “Tuition | $11,180 | $11,180 | $22,360”
  - on_campus:Lion Fee: 1802 ⟵ “Lion Fee | $901 | $901 | $1,802”
  - on_campus:Food and Housing: 13146 ⟵ “Food and Housing | $6,573 | $6,573 | $13,146”
  - on_campus:Books and Supplies: 1400 ⟵ “Books and Supplies | $700 | $700 | $1,400”
  - on_campus:Personal: 3700 ⟵ “Personal | $1,850 | $1,850 | $3,700”
  - on_campus:Transportation: 2520 ⟵ “Transportation | $1,260 | $1,260 | $2,520”
  - on_campus:Loan Fees: 190 ⟵ “Loan Fees | $95 | $95 | $190”
  - on_campus:Total: 45118 ⟵ “Total | $22,559 | $22,559 | $45,118”
### `3b026fdd51f6c392` Lindenwood University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.lindenwood.edu/admissions/early-college-academy/ (sha256 5e07fdc8ebc9)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Juniors and Seniors with an overall minimum grade point average of 3.0 (on a 4.0 scale) are encouraged to enroll.”
  - per_credit_hour_charge: 111 ⟵ “Concurrent Enrollment / Early College Credit: $111 per credit hour”
### `mc5957c0c46e44c6` Lindenwood University — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://www.lindenwood.edu/admissions/ (sha256 f2c71bed14a4)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 90 ⟵ “Students can apply up to 90 hours of transfer credit from regionally accredited institutions toward their degree.”
  - max_transfer_credits: 90 ⟵ “Students can apply up to 90 hours of transfer credit from regionally accredited institutions toward their degree.”
### `ae5301a14ac19341` Logan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.logan.edu/tuition/scholarships (sha256 d4425c4a492c)
- checks: {"thresholds": null}
  - award_amount_text: $350 per credit hour ⟵ “Fountain Scholarship | First-time freshman, 3.5+ unweighted GPA | $350 per credit hour”
  - eligibility_summary: First-time freshman, 3.5+ unweighted GPA ⟵ “Fountain Scholarship | First-time freshman, 3.5+ unweighted GPA | $350 per credit hour”
### `c481849543c0007c` Logan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.logan.edu/tuition/scholarships (sha256 d4425c4a492c)
- checks: {"thresholds": null}
  - award_amount_text: Up to $16,000 — $1,600 per trimester for 10 trimesters ⟵ “Dean's Scholarship | 3.50–3.74 | Up to $16,000 — $1,600 per trimester for 10 trimesters”
  - gpa_requirement: 3.50–3.74 ⟵ “Dean's Scholarship | 3.50–3.74 | Up to $16,000 — $1,600 per trimester for 10 trimesters”
### `d9b797ba3776aba6` Logan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.logan.edu/tuition/scholarships (sha256 3a59e0c3afb9)
- checks: {"thresholds": {"gpa_min": 3.75}}
  - award_amount_text: Up to $18,000 — $1,800 per trimester for 10 trimesters ⟵ “President's Scholarship | 3.75 and above | Up to $18,000 — $1,800 per trimester for 10 trimesters”
  - gpa_requirement: 3.75 and above ⟵ “President's Scholarship | 3.75 and above | Up to $18,000 — $1,800 per trimester for 10 trimesters”
### `f2861f2043762074` Logan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.logan.edu/tuition/scholarships (sha256 3a59e0c3afb9)
- checks: {"thresholds": null}
  - award_amount_text: $400 per credit hour ⟵ “Tower Scholarship | Transfer student, 3.5+ unweighted GPA | $400 per credit hour”
  - eligibility_summary: Transfer student, 3.5+ unweighted GPA ⟵ “Tower Scholarship | Transfer student, 3.5+ unweighted GPA | $400 per credit hour”
### `22b899217b87154a` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: Full Tuition ⟵ “Melissa Brickey Scholarship | Full Tuition | Graduate of De La Salle Middle School (St. Louis, Mo.) and/or one of the public or private high schools within the boundaries of Saint Louis City. | Dec. 1”
  - eligibility_summary: Graduate of De La Salle Middle School (St. Louis, Mo.) and/or one of the public or private high schools within the boundaries of Saint Louis City. ⟵ “Melissa Brickey Scholarship | Full Tuition | Graduate of De La Salle Middle School (St. Louis, Mo.) and/or one of the public or private high schools within the boundaries of Saint Louis City. | Dec. 1”
### `31a68c921d9eecbe` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 annually ⟵ “Cheer / Dance / Mascot | Up to $2,000 annually | Tryouts | May 1”
  - eligibility_summary: Tryouts ⟵ “Cheer / Dance / Mascot | Up to $2,000 annually | Tryouts | May 1”
### `730fc6e600429406` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: Full Tuition ⟵ “Trustee Scholarship* | Full Tuition | GPA >= 3.75 OR ACT/SAT >= 27/1290*** | Dec. 1”
  - eligibility_summary: GPA >= 3.75 OR ACT/SAT >= 27/1290*** ⟵ “Trustee Scholarship* | Full Tuition | GPA >= 3.75 OR ACT/SAT >= 27/1290*** | Dec. 1”
### `ac2286c003fb079b` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships/ (sha256 18d6a1f38a01)
- checks: {"thresholds": null}
  - award_amount_text: Up to Full Tuition, Room & Board (double occupancy in residence hall)* ⟵ “Keith Lovin Leadership Scholarship* | Up to Full Tuition, Room & Board (double occupancy in residence hall)* | Students who demonstrate exceptional leadership, innovation and a commitment to creating positive change in their schools and communities. This scholarship is designed for students who go b”
  - eligibility_summary: Students who demonstrate exceptional leadership, innovation and a commitment to creating positive change in their schools and communities. This scholarship is designed for students who go beyond expectations, challenge the status quo, inspire others and show a passion for making an impact, whether through academics, service, advocacy or entrepreneurship. ⟵ “Keith Lovin Leadership Scholarship* | Up to Full Tuition, Room & Board (double occupancy in residence hall)* | Students who demonstrate exceptional leadership, innovation and a commitment to creating positive change in their schools and communities. This scholarship is designed for students who go b”
### `ce9899772987bb52` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships/ (sha256 18d6a1f38a01)
- checks: {"thresholds": null}
  - award_amount_text: $11,000 annually* ⟵ “Big Red Scholarship | $11,000 annually* | GPA >= 3.0 OR ACT/SAT >= 24/1180*** | Dec. 1”
  - eligibility_summary: GPA >= 3.0 OR ACT/SAT >= 24/1180*** ⟵ “Big Red Scholarship | $11,000 annually* | GPA >= 3.0 OR ACT/SAT >= 24/1180*** | Dec. 1”
### `cfeb6020268b903a` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 annually ⟵ “Pep Band | Up to $2,000 annually | Tryouts | May 1”
  - eligibility_summary: Tryouts ⟵ “Pep Band | Up to $2,000 annually | Tryouts | May 1”
### `d483bd4fe8b8662e` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: $500 - $5,000 annually ⟵ “Design & Visual Art Scholarships** | $500 - $5,000 annually | Submission of a portfolio for review | Mar. 1”
  - eligibility_summary: Submission of a portfolio for review ⟵ “Design & Visual Art Scholarships** | $500 - $5,000 annually | Submission of a portfolio for review | Mar. 1”
### `d650eecee0e64478` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - eligibility_summary: Visit goarmy.com ⟵ “Army ROTC Scholarship | Varies | Visit goarmy.com | Jan. 10”
### `d7de48e8b4bbd392` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: $14,000 annually* ⟵ “Saints Scholarship | $14,000 annually* | GPA >= 3.5 OR ACT/SAT >= 27/1290*** | Dec. 1”
  - eligibility_summary: GPA >= 3.5 OR ACT/SAT >= 27/1290*** ⟵ “Saints Scholarship | $14,000 annually* | GPA >= 3.5 OR ACT/SAT >= 27/1290*** | Dec. 1”
### `df31b2a17655e416` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships/ (sha256 18d6a1f38a01)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 annually ⟵ “eSports | Up to $2,000 annually | Tryouts (Counter Strike-Global Offensive, League of Legends, Hearthstone, Heroes of the Storm & Overwatch) | May 1”
  - eligibility_summary: Tryouts (Counter Strike-Global Offensive, League of Legends, Hearthstone, Heroes of the Storm & Overwatch) ⟵ “eSports | Up to $2,000 annually | Tryouts (Counter Strike-Global Offensive, League of Legends, Hearthstone, Heroes of the Storm & Overwatch) | May 1”
### `e91f39c459b33ae5` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 annually ⟵ “FIRST Robotics Scholarship | $3,000 annually | Participation on a FIRST Robotics Competition (FRC) team or a FIRST Tech Challenge (FTC) team | Jan. 10”
  - eligibility_summary: Participation on a FIRST Robotics Competition (FRC) team or a FIRST Tech Challenge (FTC) team ⟵ “FIRST Robotics Scholarship | $3,000 annually | Participation on a FIRST Robotics Competition (FRC) team or a FIRST Tech Challenge (FTC) team | Jan. 10”
### `ec5c1deb03094820` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 annually ⟵ “Rugby (Men's & Women's) | Up to $2,000 annually | Tryouts | May 1”
  - eligibility_summary: Tryouts ⟵ “Rugby (Men's & Women's) | Up to $2,000 annually | Tryouts | May 1”
### `f115ea879773dd0a` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships (sha256 bf4587a73e8b)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 annually ⟵ “STUNT | Up to $2,000 annually | Tryouts | May 1”
  - eligibility_summary: Tryouts ⟵ “STUNT | Up to $2,000 annually | Tryouts | May 1”
### `f5949e9fd505543c` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships/ (sha256 18d6a1f38a01)
- checks: {"thresholds": null}
  - award_amount_text: $9,000 annually* ⟵ “Maryville Opportunity Award | $9,000 annually* | GPA >= 2.5 OR ACT/SAT >= 22/1110*** | Dec. 1”
  - eligibility_summary: GPA >= 2.5 OR ACT/SAT >= 22/1110*** ⟵ “Maryville Opportunity Award | $9,000 annually* | GPA >= 2.5 OR ACT/SAT >= 22/1110*** | Dec. 1”
### `ffd5e954d39d0693` Maryville University of Saint Louis — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryville.edu/admissions/financial-aid/scholarships/ (sha256 18d6a1f38a01)
- checks: {"thresholds": null}
  - award_amount_text: Full Tuition, Room & Board (double occupancy in residence hall) ⟵ “Presidential Scholarship* | Full Tuition, Room & Board (double occupancy in residence hall) | GPA >= 3.75 OR ACT/SAT >= 27/1290*** | Dec. 1”
  - eligibility_summary: GPA >= 3.75 OR ACT/SAT >= 27/1290*** ⟵ “Presidential Scholarship* | Full Tuition, Room & Board (double occupancy in residence hall) | GPA >= 3.75 OR ACT/SAT >= 27/1290*** | Dec. 1”
### `439e84c7aa4739d5` Maryville University of Saint Louis — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.maryville.edu/admissions/financial-aid/cost-of-attendance-undergraduate/ (sha256 30d6a6c3b466)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition and Fees*: 28366 ⟵ “Tuition and Fees* | $28,366 | $28,366”
  - on_campus:Housing & Meals: 14500 ⟵ “Housing & Meals | $14,500 | $13,200”
  - on_campus:Federal Loan Fees: 714 ⟵ “Federal Loan Fees | $714 | $714”
  - on_campus:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $3,650”
  - on_campus:Transportation: 800 ⟵ “Transportation | $800 | $1200”
  - on_campus:Total: 47130 ⟵ “Total | $47,130 | $47,130”
  - off_campus_not_with_family:Tuition and Fees*: 28366 ⟵ “Tuition and Fees* | $28,366 | $28,366”
  - off_campus_not_with_family:Housing & Meals: 13200 ⟵ “Housing & Meals | $14,500 | $13,200”
  - off_campus_not_with_family:Federal Loan Fees: 714 ⟵ “Federal Loan Fees | $714 | $714”
  - off_campus_not_with_family:Personal Expenses: 3650 ⟵ “Personal Expenses | $2,750 | $3,650”
  - off_campus_not_with_family:Transportation: 1200 ⟵ “Transportation | $800 | $1200”
  - off_campus_not_with_family:Total: 47130 ⟵ “Total | $47,130 | $47,130”
### `51d9ee28d2dd0000` Metropolitan Community College-Kansas City — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.mcckc.edu/admissions/credit-by-exam.aspx (sha256 a30e14acf90b)
- checks: {"distinct_exams": 29, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS 136 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL 222 & 223 | 6”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing &Interpreting Literature | 50 | ENGL 214 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology - General | 50 | BIOL 101 | 5”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus w/ Elem. Functions | 50 | MATH 180 | 5”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM 111 | 5”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 120 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL 101 | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MATH 119 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL 220 & 221 | 6”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT 101 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French - Level 1 | 50 | FREN 101 | 5”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French - Level 2 | 59 | FREN 101 & 102 | 10”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German - Level 1 | 50 | GERM 101 | 5”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German - Level 2 | 60 | GERM 101 & 102 | 10”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | PSYC 243 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Humanities Electives | 6”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | CSIS 110 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | PSYC Elective | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BUSN 270 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSYC 140 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOCI 160 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MATH 150 | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECON 210 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BUSN 200 | 3”
  - … 7 more rows
### `5c7c1793f7c0918a` Metropolitan Community College-Kansas City — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.mcckc.edu/admissions/credit-by-exam.aspx (sha256 a30e14acf90b)
- checks: {"distinct_exams": 15, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 101 | 5”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 111 | 5”
  - equivalencies[IB-COMPUTER-SCIENCE|4]:  ⟵ “Computer Science | 4 | CSIS 110, & CSIS 115 | 6”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | 4 | ECON 210 & ECON 211 | 6”
  - equivalencies[IB-ENGLISH-A-LITERATURE|4]:  ⟵ “English A: Literature | 4 | Literature elective | 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4]:  ⟵ “English A: Language and Literature | 4 | Literature elective | 3”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOG 104 | 4”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History | 4 | HIST 120 & HIST 121 | 6”
  - equivalencies[IB-FRENCH|4]:  ⟵ “Language B - French or Spanish | 4 | FREN 101 or SPAN 101 | 5”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|5]:  ⟵ “Math Analysis and Approaches | 5 | MATH 180 | 5”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|4]:  ⟵ “Math Applications and Interpretations | 4 | MATH 120 | 3”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music | 4 | MUSI 108 & MUSI 110 | 7”
  - equivalencies[IB-PHILOSOPHY|4]:  ⟵ “Philosophy | 4 | PHIL 100 & PHIL 102 | 6”
  - equivalencies[IB-PSYCHOLOGY|4]:  ⟵ “Psychology | 4 | PSYC 140 | 3”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics | 4 | PHYS 101 | 5”
### `6aee886a387943a6` Metropolitan Community College-Kansas City — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mcckc.edu/college-acceleration-program/dual-credit.aspx (sha256 e9f58e36c96f)
- checks: {"fields": [], "tiers": 3}
  - eligibility_tier: 3.0 ⟵ “Juniors and Seniors with a 3.0+ cumulative GPA are eligible without a letter of recommendation.”
  - eligibility_tier: 2.5 ⟵ “Juniors or Seniors must have a 2.5 -2.99 cumulative GPA (requires signature of high”
  - eligibility_tier: 3.0 ⟵ “Sophomores must have a 3.0 cumulative GPA AND signature of high school dual credit”
### `d457f0e49db65dad` Mineral Area College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://mineralarea.edu/future-students/dual-credit/ (sha256 cc9eb15ef3bf)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 3}
  - per_credit_hour_charge: 60 ⟵ “Dual Credit Tuition: $60 per credit hour”
  - eligibility_tier: 3.0 ⟵ “Sophomores – 3.0 GPA or higher &amp; high school recommendations from the principal &amp;”
  - eligibility_tier: 2.5 ⟵ “Juniors – 2.5 GPA or higher &amp; high school recommendation from the counselor”
  - eligibility_tier: 2.5 ⟵ “Seniors – 2.5 GPA &amp; high school recommendation from the counselor.”
  - per_credit_hour_charge: 60 ⟵ “Tuition: $60 per credit hour”
  - per_credit_hour_charge: 15 ⟵ “Fees: Students are responsible for fees including, but not limited to: $30 per semester Dual Enrollment Student-Support fee; $15 per credit hour web-course fee”
  - per_credit_hour_charge: 75 ⟵ “Base Tuition: $75 per credit hour”
  - per_credit_hour_charge: 100 ⟵ “Tier 1 Tuition*: $100 per credit hour”
  - per_credit_hour_charge: 130 ⟵ “Tier 2 Tuition^: $130 per credit hour”
  - per_credit_hour_charge: 15 ⟵ “Fees: Students are responsible for fees including, but not limited to: $15 per credit hour web-course fee”
  - per_credit_hour_charge: 60 ⟵ “The tuition for Dual Credit is $60 per credit hour.  Tuition for Dual Enrollment classes is $75 per credit.  Dual Credit classes do not have course fees and your high school will provide the textbooks and required course materials. Dual Enrollment courses are subject to course fees, this amount vari”
  - per_credit_hour_charge: 75 ⟵ “The tuition for Dual Credit is $60 per credit hour.  Tuition for Dual Enrollment classes is $75 per credit.  Dual Credit classes do not have course fees and your high school will provide the textbooks and required course materials. Dual Enrollment courses are subject to course fees, this amount vari”
### `2fc0b903189e2d0c` Mission University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://mission.edu/admissions/tuition-and-fees-2025-26-2/ (sha256 f665957dd4f7)
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition (FA/SP: 12-18 hours): 16400.0 ⟵ “Tuition (FA/SP: 12-18 hours) | $16,400.00 | $8,200.00”
  - on_campus:Fees: 1750.0 ⟵ “Fees | $1,750.00 | $875.00”
  - on_campus:Living Expenses (Housing and Food): 9200.0 ⟵ “Living Expenses (Housing and Food) | $9,200.00 | $4,600.00”
  - on_campus:Transportation: 1700.0 ⟵ “Transportation | $1,700.00 | $850.00”
  - on_campus:Miscellaneous (Personal expenses): 4265.0 ⟵ “Miscellaneous (Personal expenses) | $4,265.00 | $2,132.00”
  - on_campus:Books, Course Materials, Supplies, and Equipment: 1350.0 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,350.00 | $675.00”
  - on_campus:Loan Fees: 65.0 ⟵ “Loan Fees | $65.00 | $32.50”
  - on_campus:Child/Dependent Care: 4165.0 ⟵ “Child/Dependent Care | $4,165.00 | $2,082.50”
  - on_campus:Total:: 38895.0 ⟵ “Total: | $38,895.00 | $19,447.50”
### `f6549a3f8acc7f12` Mission University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://mission.edu/academics/dual-enrollement/ (sha256 43fd7bcf662d)
- checks: {"fields": ["per_credit_hour_charges", "state_grant_accepted"], "tiers": 0}
  - per_credit_hour_charge: 100 ⟵ “$100.00 per credit hour, plus a $50.00 per semester registration fee.”
  - state_grant_accepted: True ⟵ “Mission University is an eligible postsecondary provider through the Missouri Department of Higher Education and Workforce Development (MO-DHEWD), and qualifying students may be eligible for reimbursement through the dual credit/dual enrollment scholarship. Visit https://dhewd.mo.gov/ppc/grants-scho”
  - per_credit_hour_charge: 100 ⟵ “Mission U offers competitive dual enrollment course pricing at $100.00 per credit hour and just a $50.00 per semester registration fee.”
### `e5540608d46b2d8d` Missouri Baptist University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mobap.edu/ecp/ (sha256 35c70f37e6e5)
- checks: {"fields": ["state_grant_accepted"], "tiers": 0}
  - state_grant_accepted: True ⟵ “The Dual Credit/Dual Enrollment Scholarship covers tuition and fees for qualified high school students taking dual credit or dual enrollment coursework from an approved provider. Apply.”
### `dba202c2db83438e` Missouri Baptist University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mobap.edu/admissions/transfer-students/ (sha256 38ba347572a8)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 24 ⟵ “At least 24 of the last 30 credit hours before graduation must be taken at Missouri Baptist University.”
### `4d70403eccea0bd0` Missouri Southern State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.mssu.edu/student-affairs/financial-aid/estimated-cost-attendance.php (sha256 ebde9fbfd2d6)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition*: 8778 ⟵ “Tuition* | $8,778 | $17,556”
  - on_campus:Fees: 840 ⟵ “Fees | $840 | $840”
  - on_campus:Books and Supplies: 1401 ⟵ “Books and Supplies | $1,401 | $1,401”
  - on_campus:Housing and Food: 10589 ⟵ “Housing and Food | $10,589 | $10,589”
  - on_campus:Transportation: 2070 ⟵ “Transportation | $2,070 | $2,070”
  - on_campus:Miscellaneous: 7319 ⟵ “Miscellaneous | $7,319 | $7,319”
  - on_campus:TOTAL: 30997 ⟵ “TOTAL | $30,997 | $39,775”
### `54bab796e1b7032a` Missouri Southern State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.mssu.edu/student-affairs/financial-aid/estimated-cost-attendance.php (sha256 ebde9fbfd2d6)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition*: 17556 ⟵ “Tuition* | $8,778 | $17,556”
  - on_campus:Fees: 840 ⟵ “Fees | $840 | $840”
  - on_campus:Books and Supplies: 1401 ⟵ “Books and Supplies | $1,401 | $1,401”
  - on_campus:Housing and Food: 10589 ⟵ “Housing and Food | $10,589 | $10,589”
  - on_campus:Transportation: 2070 ⟵ “Transportation | $2,070 | $2,070”
  - on_campus:Miscellaneous: 7319 ⟵ “Miscellaneous | $7,319 | $7,319”
  - on_campus:TOTAL: 39775 ⟵ “TOTAL | $30,997 | $39,775”
### `m9e47b5ac5054b8b` Missouri Southern State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mssu.edu/academics/dual-credit/tuition.php (sha256 0620bd72cf11)
- checks: {"fields": ["max_credit_hours_per_term", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 0}
  - per_credit_hour_charge: 75 ⟵ “Dual Credit and Dual Enrollment courses are offered at a reduced tuition rate of $75 per credit hour, providing an affordable way to earn college credit while still in high school.”
  - max_credit_hours_per_term: 6 ⟵ “The On the Move initiative provides eligible high school students who qualify for free or reduced lunch with up to 6 credit hours of concurrent enrollment tuition waived per semester at MSSU.”
  - max_credit_hours_per_term: 6 ⟵ “Benefit: Up to 6 credit hours of tuition waived per semester”
  - eligibility_tier: 3.0 ⟵ “Students in the 11th and 12th grades with an overall minimum grade point average of 3.0 (on a 4.0 scale) are automatically eligible for dual credit courses.”
  - eligibility_tier: 3.0 ⟵ “Students in the 10th grade must have an overall minimum grade point average of 3.0 (on a 4.0 scale) and must provide a signed letter of recommendation from their principal and guidance counselor and provide written permission from a parent or legal guardian.”
  - eligibility_tier: 3.0 ⟵ “Students in the 9th grade must have an overall minimum grade point average of 3.0 (on a 4.0 scale), score at the 90th percentile or above on the ACT or SAT, and provide a signed letter of recommendation from their principal and guidance counselor and provide written permission from a parent or legal”
### `0309d18e2257e3fb` Missouri University of Science and Technology — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://futurestudents.mst.edu/admissions/transfer/credit-by-exam/ (sha256 1e1a3fe70832)
- checks: {"distinct_exams": 33, "equivalencies": 51, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|African American Studies/3]:  ⟵ “African American Studies/3 | 3 | Humanities Elective”
  - equivalencies[AP-ART-HISTORY|Art History/3]:  ⟵ “Art History/3 | 3 | Art 1180”
  - equivalencies[AP-BIOLOGY|Biology/3]:  ⟵ “Biology/3 | 3 | Biological Sciences 1113”
  - equivalencies[AP-BIOLOGY|Biology/4]:  ⟵ “Biology/4 | 4 | Biological Sciences 1113 & 1219”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|Business with Personal Finance/3]:  ⟵ “Business with Personal Finance/3 | 3 | Business 1001”
  - equivalencies[AP-CALCULUS-AB|Calculus AB/3]:  ⟵ “Calculus AB/3 | 5 | Math 1210”
  - equivalencies[AP-CALCULUS-AB|Calculus AB/4]:  ⟵ “Calculus AB/4 | 4 | Math 1214”
  - equivalencies[AP-CALCULUS-BC|Calculus BC/1, AB Subscore/3]:  ⟵ “Calculus BC/1, AB Subscore/3 | 5 | Math 1210”
  - equivalencies[AP-CALCULUS-BC|Calculus BC/1, AB Subscore/4]:  ⟵ “Calculus BC/1, AB Subscore/4 | 4 | Math 1214”
  - equivalencies[AP-CALCULUS-BC|Calculus BC/3, AB Subscore/1]:  ⟵ “Calculus BC/3, AB Subscore/1 | 5 | Math 1210”
  - equivalencies[AP-CALCULUS-BC|Calculus BC/3, AB Subscore/4]:  ⟵ “Calculus BC/3, AB Subscore/4 | 4 | Math 1214”
  - equivalencies[AP-CALCULUS-BC|Calculus BC/4, AB Subscore/1]:  ⟵ “Calculus BC/4, AB Subscore/1 | 8 | Math 1214 & 1215*”
  - equivalencies[AP-CHEMISTRY|Chemistry/3]:  ⟵ “Chemistry/3 | 4 | Chemistry 1310”
  - equivalencies[AP-CHEMISTRY|Chemistry/4]:  ⟵ “Chemistry/4 | 5 | Chemistry 1310 & 1319”
  - equivalencies[AP-CHEMISTRY|Chemistry/5]:  ⟵ “Chemistry/5 | 8 | Chemistry 1310, 1319 & 1320”
  - equivalencies[AP-COMPUTER-SCIENCE-A|Computer Science A/3]:  ⟵ “Computer Science A/3 | 3 | Comp Sci 1911”
  - equivalencies[AP-COMPUTER-SCIENCE-A|Computer Science A/4]:  ⟵ “Computer Science A/4 | 3 | Comp Sci 1500”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|Computer Science Principles/3]:  ⟵ “Computer Science Principles/3 | 3 | Comp Sci 1911”
  - equivalencies[AP-CYBERSECURITY|Cybersecurity/3]:  ⟵ “Cybersecurity/3 | 3 | Information Science & Technology 3333”
  - equivalencies[AP-DRAWING|Drawing/3]:  ⟵ “Drawing/3 | 3 | Art 1120”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|English Language/3]:  ⟵ “English Language/3 | 3 | English 1120”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|English Literature/3]:  ⟵ “English Literature/3 | 3 | Literature Elective”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|Environmental Science/3]:  ⟵ “Environmental Science/3 | 3 | Biological Sciences 1173”
  - equivalencies[AP-EUROPEAN-HISTORY|European History/3]:  ⟵ “European History/3 | 3 | History 1100, 1200, 1300 or 1310”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|French Language/3]:  ⟵ “French Language/3 | 8 | French 1101 & 1102”
  - … 26 more rows
### `726e19a67155209d` Missouri University of Science and Technology — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://futurestudents.mst.edu/admissions/dual-enrollment/forhighschoolstudents/ (sha256 ad2ac9586d28)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 75 ⟵ “Through the Dual Enrollment Program, the tuition cost for taking the in-person or online version of Math 1214 is offered at a discounted rate of $75 per credit hour, making the total course tuition cost only $300! Students or partnering school districts will be responsible for tuition unless alterna”
  - per_credit_hour_charge: 165 ⟵ “Certain classes offered through the College of Arts, Sciences, and Education (CASE) are offered at a reduced rate of $165 per credit hour. Courses offered at this reduced rate include:”
### `cfc166caee22908f` Missouri University of Science and Technology — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://futurestudents.mst.edu/admissions/transfer/credit-by-exam/ (sha256 1e1a3fe70832)
- checks: {"distinct_exams": 23, "equivalencies": 42, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology/4]:  ⟵ “Biology/4 | 3 | Bio Sci 1113”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business Management/4]:  ⟵ “Business Management/4 | 3 | Bus 1110”
  - equivalencies[IB-CHEMISTRY|Chemistry/4]:  ⟵ “Chemistry/4 | 3 | Chem 1301”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|English A: Language and Literature/4]:  ⟵ “English A: Language and Literature/4 | 3 | English 1160”
  - equivalencies[IB-ENGLISH-A-LITERATURE|English A: Literature/4]:  ⟵ “English A: Literature/4 | 3 | English 1231”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|Environmental Systems and Societies/4]:  ⟵ “Environmental Systems and Societies/4 | 3 | Bio Sci 1173”
  - equivalencies[IB-FILM|Film/4]:  ⟵ “Film/4 | 3 | Art 1185”
  - equivalencies[IB-FRENCH|French Language B/4]:  ⟵ “French Language B/4 | 4 | French 1102”
  - equivalencies[IB-GLOBAL-POLITICS|Global Politics/4]:  ⟵ “Global Politics/4 | 3 | Pol Sci 2400”
  - equivalencies[IB-HISTORY|History/4]:  ⟵ “History/4 | 3 | Social Science Elective”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|Mathematics: Analysis and Approaches/4]:  ⟵ “Mathematics: Analysis and Approaches/4 | 3 | Math 1103”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|Mathematics: Applications and Interpretation/4]:  ⟵ “Mathematics: Applications and Interpretation/4 | 3 | Math 1103”
  - equivalencies[IB-MUSIC|Music/4]:  ⟵ “Music/4 | 3 | Music 1150”
  - equivalencies[IB-PSYCHOLOGY|Psychology/4]:  ⟵ “Psychology/4 | 3 | Psych 1101”
  - equivalencies[IB-SPANISH|Spanish AB initio/4]:  ⟵ “Spanish AB initio/4 | 4 | Spanish 1101”
  - equivalencies[IB-SPANISH|Spanish Language B/4]:  ⟵ “Spanish Language B/4 | 4 | Spanish 1102”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|Social and Cultural Anthropology/4]:  ⟵ “Social and Cultural Anthropology/4 | 3 | Social Science Elective”
  - equivalencies[IB-THEATRE|Theatre/4]:  ⟵ “Theatre/4 | 3 | Theatre 1150”
  - equivalencies[IB-VISUAL-ARTS|Visual Arts/4]:  ⟵ “Visual Arts/4 | 3 | Art 1715”
  - equivalencies[IB-BIOLOGY|Biology/5]:  ⟵ “Biology/5 | 4 | Bio Sci 1113 & 1219”
  - equivalencies[IB-CHEMISTRY|Chemistry/4]:  ⟵ “Chemistry/4 | 4 | Chem 1310”
  - equivalencies[IB-CHEMISTRY|Chemistry/5]:  ⟵ “Chemistry/5 | 5 | Chem 1310 & 1319”
  - equivalencies[IB-CHEMISTRY|Chemistry/6]:  ⟵ “Chemistry/6 | 8 | Chem 1310, 1319 & 1320”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|Cultural Anthropology]:  ⟵ “Cultural Anthropology | 3 | Social Science Elective”
  - equivalencies[IB-ECONOMICS|Economics/4]:  ⟵ “Economics/4 | 3 | Econ 1100 or 1200”
  - … 17 more rows
### `m4e254413d2ae5c8` Missouri University of Science and Technology — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://futurestudents.mst.edu/media/enrollmentmanagement/futurestudents/documents/admissions/transfer/courseguides/crowdercollege/2026transferguidescrowder/2026%20Transfer%20Guide%20Crowder%20IST%20BS.pdf (sha256 2071c55034d1)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 49}
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 68 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “HIST 101 Western Civilization I 3 HISTORY 1100 Early Western Civilization 3 HIST 102 Western Civilization II 3 HISTORY 1200 Modern Western Civilization 3 Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Total HASS Hours 15 Total HASS Hours 15 Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “MATH 202 Calculus III 5 MATH 2222 Calculus III 4 PHYS 190 General Physics I 5 PHYSICS 1135 Engineering Physics I 4 PHYS 210 General Physics II 5 PHYSICS 2135 Engineering Physics II 4 Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 61 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Electives Maximum Free Electives 7 Electives Maximum Free Electives 7 Maximum credit hours to be transferred to Missouri S&T degree requirements. 68 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 67 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “BIOL 110 General Zoology 5 BIO SCI 2353 Zoology Applies to degree as upper-division elective. 3 BIOL 120 General Botany 5 BIO SCI 2383 Plant Biology Applies to degree as upper-division elective. 3 Electives Free Electives 2 Electives Free Electives 2 Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri”
  - residency_requirement_credits: 60 ⟵ “Science, Math, Engineering Other science, mathematics, or engineering course. 3 3 Maximum credit hours to be transferred to Missouri S&T degree requirements. 61 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “ECON 201 Principles of Macroeconomics 3 ECON 1200 Principles of Macroeconomics 3 Electives Maximum Free Electives 11 Electives Maximum Free Electives 11 Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Electives Free Electives Electives Free Electives Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 61 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “MATH 210 Differential Equations 3 MATH 3304 Elementary Differential Equations 3 Electives Maximum Free Electives 6 Electives Maximum Free Electives 6 Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 68 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “CIV 201 European Civilization I 3 HISTORY 1100 Early Western Civilization 3 CIV 202 European Civilization II 3 HISTORY 1200 Modern Western Civilization 3 Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “BIO 122 Principles of Biology II and Lab 5 BIO SCI 1223, 1229 Biodiversity and Lab 4 BIO 110 Ecology 3 BIO SCI 2263 Ecology 3 Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 76 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 61 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “Maximum credit hours to be transferred to Missouri S&T degree requirements. 60 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - residency_requirement_credits: 60 ⟵ “COL 101 Falcon Seminar 1 FR ENG 1100 Study and Careers in Engineering and Computing 1 Electives Maximum Free Electives 7 Electives Maximum Free Electives 7 Maximum credit hours to be transferred to Missouri S&T degree requirements. 68 Missouri S&T residency requirements: The last 60 hours of any Missouri S&T degree must be completed at Missouri S&T.”
  - … 24 more rows
### `447a8b309d426be2` Missouri Valley College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.moval.edu/admissions-financial-aid/tuition-financial-aid/cost-of-attendance/ (sha256 dcbae27a87bf)
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 23500 ⟵ “Tuition | $23,500 | $23,500”
  - on_campus:Enrollment Fee: 200 ⟵ “Enrollment Fee | $200 | $200”
  - on_campus:Fees: 2250 ⟵ “Fees | $2,250 | $2,250”
  - on_campus:Room: 6500 ⟵ “Room | $6,500 | Estimated: $9,500”
  - on_campus:Board: 6250 ⟵ “Board | $6,250”
  - on_campus:Books/Supplies: 3000 ⟵ “Books/Supplies | $3,000 | $3,000”
  - on_campus:Transportation: 3500 ⟵ “Transportation | $3,500 | $4,000”
  - on_campus:Miscellaneous Expenses: 3500 ⟵ “Miscellaneous Expenses | $3,500 | $3,500”
  - on_campus:Total: 48700 ⟵ “Total | $48,700 | $45,950”
  - with_parents_or_family:Tuition: 23500 ⟵ “Tuition | $23,500 | $23,500”
  - with_parents_or_family:Enrollment Fee: 200 ⟵ “Enrollment Fee | $200 | $200”
  - with_parents_or_family:Fees: 2250 ⟵ “Fees | $2,250 | $2,250”
  - with_parents_or_family:Books/Supplies: 3000 ⟵ “Books/Supplies | $3,000 | $3,000”
  - with_parents_or_family:Transportation: 4000 ⟵ “Transportation | $3,500 | $4,000”
  - with_parents_or_family:Miscellaneous Expenses: 3500 ⟵ “Miscellaneous Expenses | $3,500 | $3,500”
  - with_parents_or_family:Total: 45950 ⟵ “Total | $48,700 | $45,950”
### `184bb72760622895` Missouri Valley College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.moval.edu/academics/dual-credit-for-high-school-students/ (sha256 d5e2f6e14476)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 1}
  - per_credit_hour_charge: 85 ⟵ “Missouri Valley College will provide scholarships to reduce tuition costs to $85.00 per credit hour.”
  - eligibility_tier: 3.0 ⟵ “Submit your high school transcript. A minimum GPA of 3.0 (on a 4.0 scale) or its equivalent is required.”
  - per_credit_hour_charge: 85 ⟵ “Missouri Valley College will provide scholarships to reduce tuition costs to $85.00 per credit hour.”
### `82d9a55d4d944034` Ozark Christian College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://cdn.occ.edu/pdfs/CLEP_Credits_Accepted_By_OCC.pdf (sha256 607eb078ef1b)
- checks: {"distinct_exams": 15, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                               50               3              EL 1210 (Not 1211)   English Composition 1 (Not Eng Comp 2)”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                           50               3              XXX                  Science Elective”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                                         50               3              XXX                  Science Elective”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences                                  50               3              XXX                  Science Elective”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics                               50               3              XXX                  Mathematics Elective”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                                   50               3              XXX                  Mathematics Elective”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                                       50               3              XXX                  Mathematics Elective”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                          50               3              XXX                  Mathematics Elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|3]:  ⟵ “Western Civilization 1: Ancient Near East to 1648 50               3              XXX                  History Elective”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization 2: 1648 to the Present       50               3              XXX                  History Elective”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                               50               3              EL 2311              American Literature”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                                50               3              EL 2312              British Literature”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language                                   50               3              XXX                  Humanities/Fine Arts Elective”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language                                   50               3              XXX                  Humanities/Fine Arts Elective”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language                                  50               3              LA 1210              Spanish 1”
### `90ec124e218f905c` Ozark Christian College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://cdn.occ.edu/pdfs/AP_Credits_Accepted_By_OCC.pdf (sha256 ded9690eb09e)
- checks: {"distinct_exams": 32, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                                       3, 4, 5               3                   XXX                           Humanities/Fine Arts Elective”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                           3, 4, 5               3                   XXX                           Science Elective”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                       3, 4, 5               3                   XXX                           Mathematics Elective”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                                       3, 4, 5               3                   XXX                           Mathematics Elective”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                         3, 4, 5               3                   XXX                           Science Elective”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture                        3, 4, 5               3                   XXX                           Humanities/Fine Arts Elective”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                                3, 4, 5               3                   XXX                           General Education Elective”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition                    3, 4, 5               3                   EL 1210                       English Composition 1”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|6]:  ⟵ “English Literature & Composition                  3, 4, 5               6                   EL 2312 and EL 1210           British Literature and English Composition 1”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                                  3, 4, 5               3                   XXX                           History Elective”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture                         3, 4, 5               3                   XXX                           Humanities/Fine Arts Elective”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture                         3, 4, 5               3                   XXX                           Humanities/Fine Arts Elective”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                                   3, 4, 5               3                   XXX                           General Education Elective”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language & Culture***                     3, 4, 5               3                   XXX                           Humanities/Fine Arts Elective”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language & Culture                       3, 4, 5               3                   XXX                           Humanities/Fine Arts Elective”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin                                             3, 4, 5               3                   XXX                           Humanities/Fine Arts Elective”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                                    3, 4, 5               3                   XXX                           General Education Elective”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                                    3, 4, 5               3                   XXX                           General Education Elective”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                                      3, 4, 5               3                   MU1510                        Music Theory 1”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1                                         3, 4, 5               3                   XXX                           Science Elective”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2                                         3, 4, 5               3                   XXX                           Science Elective”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C: Mechanics                              3, 4, 5               3                   XXX                           Science Elective”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity and Magnetism              3, 4, 5               3                   XXX                           Science Elective”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                        3, 4, 5               3                   PC 2210                       Psychology”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language & Culture                        3, 4, 5               3                   XXX                           Humanities/Fine Arts Elective”
  - … 7 more rows
### `a479eb08bc08c684` Ozark Christian College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://occ.edu/academics/dualenrollment (sha256 b25e4e525a39)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “2. Submit the prospective student's most recent high school transcript indicating a grade point average of at least 2.5 on a 4.0 scale. The following Ozark classes are eligible for dual enrollment status:”
### `702bb7977bc21cbf` Park University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.park.edu/tuition-financial-aid/tuition-details/ (sha256 293c1e840c00)
- checks: {"columns": 1, "rows": 6}
  - on_campus:Standard Tuition (12-18 hours): 17000 ⟵ “Standard Tuition (12-18 hours) | $8,500 | $17,000”
  - on_campus:Room – double occupancy: 5700 ⟵ “Room – double occupancy | $2,850 | $5,700”
  - on_campus:Board – all-access meal plan: 4850 ⟵ “Board – all-access meal plan | $2,425 | $4,850”
  - on_campus:First Day Access fee*: 750 ⟵ “First Day Access fee* | $375 | $750”
  - on_campus:University fee1: 1000 ⟵ “University fee1 | $500 | $1,000”
  - on_campus:Health Insurance: 1754 ⟵ “Health Insurance | $877 | $1,754”
### `56b3fb208bd60f6e` Park University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.park.edu/academics/explore-programs/4-plus-1-dual-credit-program/ (sha256 d0842bdf8016)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Park University’s 4+1 program allows bachelor’s seeking students with at least 60 undergraduate credit hours and a GPA of 3.0+ to take graduate coursework for dual credit. The 4+1 program reduces the time necessary to complete a graduate degree from two years to as little as one.”
### `2606e866b8959f69` Rockhurst University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.rockhurst.edu/scholarships (sha256 19846f6e2efd)
- checks: {"thresholds": null}
  - gpa_requirement: Below 2.99 ⟵ “Below 2.99 | $18,000 | Achievement”
### `5e58c697807b5af8` Rockhurst University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.rockhurst.edu/scholarships (sha256 19846f6e2efd)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - gpa_requirement: 4.0 ⟵ “4.0 | $28,000 | Presidential”
### `80cf8ce9fb1cc16a` Rockhurst University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.rockhurst.edu/scholarships (sha256 19846f6e2efd)
- checks: {"thresholds": {"gpa_min": 3.3}}
  - gpa_requirement: 3.3 ⟵ “3.3 | $22,000 | Deans”
### `add75029306d3ac5` Rockhurst University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.rockhurst.edu/scholarships (sha256 19846f6e2efd)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “3.0 | $20,000 | Wisdom”
### `ca564b495aa2ae5d` Rockhurst University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.rockhurst.edu/scholarships (sha256 19846f6e2efd)
- checks: {"thresholds": {"gpa_min": 3.75}}
  - gpa_requirement: 3.75 ⟵ “3.75 | $25,000 | Provost”
### `fb4d52ec4de3fff8` Rockhurst University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.rockhurst.edu/freshman/high-school-college-credit/advanced-placement (sha256 e64d876d6c1b)
- checks: {"distinct_exams": 29, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language/Composition | 4 | 6 hours | EN 1110 College Composition I & EN 1120 College Composition II”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature/Composition | 4 | 6 hours | EN 1140 English Composition & one of the following: EN 2740 World Lit Through the 16th Century, EN 2760 World Lit Since the 16th Century or EN 2960 Journeys, Voyages & Quests”
  - equivalencies[AP-PRECALCULUS|3 (also earns placement in MT 1800)]:  ⟵ “Precalculus | 3 (also earns placement in MT 1800) | 3 hours | MT 1190 Precalculus”
  - equivalencies[AP-CALCULUS-AB|4 (3 earns placement in MT 1800)]:  ⟵ “Calculus AB | 4 (3 earns placement in MT 1800) | 4 hours | MT 1800 Calculus I”
  - equivalencies[AP-CALCULUS-BC|4 (3 earns placement in MT 1810)]:  ⟵ “Calculus BC | 4 (3 earns placement in MT 1810) | 8 hours | MT 1800 Calculus I & MT 1810 Calculus II”
  - equivalencies[AP-STATISTICS|4]:  ⟵ “Statistics | 4 | 3 hours | BIA 2200 Stats & Predictive Analytics or BSS 2100 Stats for Behavioral Sciences”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | 6 hours | AR 1100 Intro to Art History I & AR 1120 Intro to Art History II”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Drawing | 4 | 3 hours | Portfolio to be reviewed”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | 3 hours | MS 1110 Intro to Music Theory”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | 6 hours | HS 1100 Survey of Western Civ I & HS 1500 Survey of Western Civ II”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History | 4 | 6 hours | HS 1701 World Civ to the 17th Century & HS 1702 World Civ Since 1492”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “American/U.S. History | 4 | 6 hours | HS 2100 Intro to US History to 1877 & HS 2500 Intro to US History Since 1877”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | 4 hours | BL 1250 General Biology I & BL1251 General Biology I Lab”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 8 hours | CH 2610 General Chemistry I & CH 2620 General Chemistry I Lab AND CH 2630 General Chemistry II & CH 2640 General Chemistry II Lab”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 | 3 hours | CS 1000 Programming for Analytics”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles | 4 | 3 hours | Computer Science Elective”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics I: Algebra-Based | 3 | 4 hours | PH 2700 Physics for Life Sciences I & PH 2710 Physics for Life Sciences I Lab”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics II: Algebra-Based | 4 | 4 hours | PH 2750 Physics for Life Sciences II & PH 2760 Physics for Life Sciences II Lab”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4 or 5 (5 required for Engineering, Biomedical Physics, and Physics of Medicine majors)]:  ⟵ “Physics C: Mechanics | 4 or 5 (5 required for Engineering, Biomedical Physics, and Physics of Medicine majors) | 4 hours | PH 2850 Physics for Scientists and Engineers I & PH 2860 Physics for Scientists and Engineers I Lab”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|5]:  ⟵ “Physics C: Electricity/Magnetism | 5 | 4 hours | PH 2940 Physics for Scientists and Engineers II & PH 2920 Physics for Scientists and Engineers II Lab”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “American Government & Politics | 4 | 3 hours | PS 1100 Intro to Politics”
  - equivalencies[AP-MACROECONOMICS|4]:  ⟵ “Macroeconomics | 4 | 3 hours | EC 1000 Prin of Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|4]:  ⟵ “Microeconomics | 4 | 3 hours | EC 1100 Prin of Microeconomics”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | 3 hours | PY 1000 Intro to Psychology”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language | 4 | 8 hours | FR 1100 Elementary French I & FR 1150 Elementary French II”
  - … 6 more rows
### `27251357ba177bb6` Rockhurst University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.rockhurst.edu/admissions/transfer/credit (sha256 6c59931a043e)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 64 ⟵ “Rockhurst accepts up to 64 credit hours from two-year junior or community colleges, and has a special Block Transfer program for students with an Associate of Arts degree from an accredited community college.”
### `1c1d55284bb64766` Saint Louis Community College — credit_policies 2028-29 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://stlcc.edu/programs/high-school/dual-credit/ (sha256 21903c12e24c)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 2}
  - per_credit_hour_charge: 25 ⟵ “Save Money: Dual credit classes cost only $25 per credit hour. Most classes are around $75 total.”
  - per_credit_hour_charge: 25 ⟵ “$25 per credit hour.”
  - eligibility_tier: 2.6 ⟵ “Have a 2.6 GPA or higher.”
  - eligibility_tier: 2.0 ⟵ “Have at least a 2.0 unweighted GPA.”
### `4eb81d78f8ff86cb` Saint Louis Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://stlcc.edu/programs/high-school/dual-enrollment/ (sha256 a44a1a4dce4f)
- checks: {"fields": ["min_hs_gpa"], "tiers": 3}
  - eligibility_tier: 2.0 ⟵ “for high school sophomores, juniors and seniors with a 2.0 GPA or higher. To enroll,”
  - eligibility_tier: 2.0 ⟵ “must be a junior with a minimum 2.0 GPA at the start of the program. This ensures”
  - eligibility_tier: 2.0 ⟵ “Have at least a 2.0 unweighted GPA.”
### `f8cf6826b179c784` Saint Louis University — academic_programs 2026-27 · program_key=finance-b-s-b-a-scnu-2-slu [new] (labeled_in_source)
- source: https://catalog.slu.edu/academic-policies/office-admission/undergraduate/2plusslu/scnu/finance/ (sha256 e2b274298b56)
- checks: {"courses": 8, "groups": 1, "groups_skipped": 0}
  - program_name: Finance, B.S.B.A. (SCNU 2+SLU) ⟵ “Finance, B.S.B.A. (SCNU 2+SLU) < Saint Louis University Academic Catalog”
### `3266909c716f3952` Saint Louis University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.slu.edu/financial-aid/tuition-and-costs/cost-of-attendance.php (sha256 649b2f80a267)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 58960 ⟵ “Tuition | $58,960 | $58,960 | $58,960”
  - on_campus:Fees: 1000 ⟵ “Fees | $1,000* | $1,000* | $1,000*”
  - on_campus:Housing - Billable: 16360 ⟵ “Housing - Billable | $16,360 | $600 | $600”
  - on_campus:Housing - Non-billable: 0 ⟵ “Housing - Non-billable | $0 | $15,760 | $7,580”
  - on_campus:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 3220 ⟵ “Transportation | $3,220 | $3,220 | $3,220”
  - on_campus:Miscellaneous: 2880 ⟵ “Miscellaneous | $2,880 | $2,880 | $2,880”
  - on_campus:Total Cost of Attendance: 83710 ⟵ “Total Cost of Attendance | $83,710 | $83,710 | $75,530”
  - off_campus_not_with_family:Tuition: 58960 ⟵ “Tuition | $58,960 | $58,960 | $58,960”
  - off_campus_not_with_family:Fees: 1000 ⟵ “Fees | $1,000* | $1,000* | $1,000*”
  - off_campus_not_with_family:Housing - Billable: 600 ⟵ “Housing - Billable | $16,360 | $600 | $600”
  - off_campus_not_with_family:Housing - Non-billable: 15760 ⟵ “Housing - Non-billable | $0 | $15,760 | $7,580”
  - off_campus_not_with_family:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3220 ⟵ “Transportation | $3,220 | $3,220 | $3,220”
  - off_campus_not_with_family:Miscellaneous: 2880 ⟵ “Miscellaneous | $2,880 | $2,880 | $2,880”
  - off_campus_not_with_family:Total Cost of Attendance: 83710 ⟵ “Total Cost of Attendance | $83,710 | $83,710 | $75,530”
  - with_parents_or_family:Tuition: 58960 ⟵ “Tuition | $58,960 | $58,960 | $58,960”
  - with_parents_or_family:Fees: 1000 ⟵ “Fees | $1,000* | $1,000* | $1,000*”
  - with_parents_or_family:Housing - Billable: 600 ⟵ “Housing - Billable | $16,360 | $600 | $600”
  - with_parents_or_family:Housing - Non-billable: 7580 ⟵ “Housing - Non-billable | $0 | $15,760 | $7,580”
  - with_parents_or_family:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3220 ⟵ “Transportation | $3,220 | $3,220 | $3,220”
  - with_parents_or_family:Miscellaneous: 2880 ⟵ “Miscellaneous | $2,880 | $2,880 | $2,880”
  - with_parents_or_family:Total Cost of Attendance: 75530 ⟵ “Total Cost of Attendance | $83,710 | $83,710 | $75,530”
### `c18330cbb38533bd` Saint Louis University — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.slu.edu/academic-policies/academic-policies-procedures/credit-exam/ (sha256 1fbecc66c7b7)
- checks: {"distinct_exams": 34, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Business | Financial Accounting | ACCT 2200 | 50 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Business | Information Systems | BTM 2000 | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business | Introductory Business Law | MGT 2000 | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Business | Principles of Management | MGT 3000 | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Business | Principles of Marketing | MKT 3000 | 50 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “Composition and Literature | American Literature | ENGL 2020 | 50 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Composition and Literature | Analyzing and Interpreting Literature | ENGL 2020 | 50 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “Composition and Literature | College Composition | ENGL 0900 | 50 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “Composition and Literature | College Composition Modular | ENGL 1500 | 50 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “Composition and Literature | English Literature | ENGL 2020 | 50 | 6”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Composition and Literature | Humanities | UNIV 1ELE | 50 | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “History and Social Sciences | American Government | POLS 1100 | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History and Social Sciences | History of the United States I: Early Colonization to 1877 | HIST 1600 | 50 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History and Social Sciences | History of the United States II: 1865 to the Present | HIST 1610 | 50 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “History and Social Sciences | Human Growth and Development | SWRK 2ELE3 | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “History and Social Sciences | Introductory Psychology | PSY 1010 | 50 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “History and Social Sciences | Introduction to Educational Psychology | EDUC 1ELE | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “History and Social Sciences | Introductory Sociology | SOC 1100 | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “History and Social Sciences | Principles of Macroeconomics | ECON 1ELE3 | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “History and Social Sciences | Principles of Microeconomics | ECON 1ELE3 | 50 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History and Social Sciences | Social Sciences and History | HIST 1ELE & UNIV 1ELE4 | 50 | 6”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “History and Social Sciences | Western Civilization I: Ancient Near East to 1648 | HIST 1ELE1 | 50 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “History and Social Sciences | Western Civilization II: 1648 to the Present | HIST 1ELE1 | 50 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Science & Mathematics | Biology | BIOL 1ELE2 | 50 | 6”
  - equivalencies[CLEP-CALCULUS|64]:  ⟵ “Science & Mathematics | Calculus | MATH 15105 | 64 | 4”
  - … 13 more rows
### `33f2c6e249a2b0c8` Saint Louis University — degree_requirements 2026-27 · program_key=finance-b-s-b-a-scnu-2-slu · requirement_key=finance-electives [new] (labeled_in_source)
- source: https://catalog.slu.edu/academic-policies/office-admission/undergraduate/2plusslu/scnu/finance/ (sha256 e2b274298b56)
  - courses: FIN 3140 ⟵ “FIN 3140 - Insurance”
  - courses: FIN 4130 ⟵ “FIN 4130 - Real Estate”
  - courses: FIN 4160 ⟵ “FIN 4160 - Commercial Real Estate”
  - courses: FIN 4250 ⟵ “FIN 4250 - International Financial Management”
  - courses: FIN 4330 ⟵ “FIN 4330 - Financial Modeling and Analysis”
  - courses: FIN 4440 ⟵ “FIN 4440 - Personal Financial Planning”
  - courses: FIN 4630 ⟵ “FIN 4630 - Applied Portfolio Management”
  - courses: FIN 4810 ⟵ “FIN 4810 - Introduction to Blockchain and Cryptocurrency”
### `5e6000c775ad0445` Southeast Missouri State University — awards 2026-27 [new] (labeled_in_title)
- source: https://semo.edu/student-support/financial-services/financial-aid/se-scholarships-2026 (sha256 adafb1e0af24)
- checks: {"thresholds": null}
  - award_tiers: [{'high school gpa': '4.0', 'amount_text': '$5,000'}, {'high school gpa': '3.85', 'amount_text': '$4,500'}, {'high school gpa': '3.5', 'amount_text': '$3,500'}, {'high school gpa': '3.1', 'amount_text': '$2,500'}, {'high school gpa': '2.9', 'amount_text': '$500'}] ⟵ “high school GPA | Yearly Value || 4.0 | $5,000 || 3.85 | $4,500 || 3.5 | $3,500 || 3.1 | $2,500 || 2.9 | $500”
  - gpa_requirement: Tiered by high school GPA: 4.0 → $5,000; 3.85 → $4,500; 3.5 → $3,500; 3.1 → $2,500; 2.9 → $500 ⟵ “high school GPA | Yearly Value || 4.0 | $5,000 || 3.85 | $4,500 || 3.5 | $3,500 || 3.1 | $2,500 || 2.9 | $500”
### `1471109ed54b30b4` Southeast Missouri State University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://semo.edu/student-support/academic-support/registrar/catalog/policies (sha256 632dbd6936e6)
- checks: {"distinct_exams": 14, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|HL 3+]:  ⟵ “Social & Cultural Anthropology (HL) | AN181 | Cultural Anthropology | 3 | 3+”
  - equivalencies[IB-VISUAL-ARTS-HL|HL 3+]:  ⟵ “Visual Arts (HL) | AR112 | Perspectives in Art | 3 | 3+”
  - equivalencies[IB-BIOLOGY-HL|HL 3+]:  ⟵ “Biology (HL) | BS108 | Biology for Living | 3 | 3+”
  - equivalencies[IB-CHEMISTRY-HL|HL 5+]:  ⟵ “Chemistry (HL) | CH185 & CH184 | General Chemistry I/Lab | 4 | 5+”
  - equivalencies[IB-CHEMISTRY-HL|HL 3+]:  ⟵ “Chemistry (HL) | CH185 & CH186 & CH184 | General Chemistry I & II/Lab | 7 | 3+”
  - equivalencies[IB-ECONOMICS-HL|HL 3+]:  ⟵ “Economics (HL) | EC101 | Economic Problems and Policies | 3 | 3+”
  - equivalencies[IB-FRENCH-HL|HL 3 or 4]:  ⟵ “French Language (HL) | FR100 | French Language & Culture I | 3 | 3 or 4”
  - equivalencies[IB-FRENCH-HL|HL 5+]:  ⟵ “French Language (HL) | FR100 & FR120 | French Language and Culture I & II | 6 | 5+”
  - equivalencies[IB-GEOGRAPHY-HL|HL 3+]:  ⟵ “Geography (HL) | GG180 | Cultural Geography | 3 | 3+”
  - equivalencies[IB-HISTORY-HL|HL 3+]:  ⟵ “Islamic History (HL) | WH125 | Islamic Civilization | 3 | 3+”
  - equivalencies[IB-LATIN-HL|HL 3+]:  ⟵ “Latin, Classical Language (HL) | LT198 | Latin Elective | 3 | 3+”
  - equivalencies[IB-MUSIC-HL|HL 3 or 4]:  ⟵ “Music (HL) | MM100 | Music Fundamentals | 3 | 3 or 4”
  - equivalencies[IB-MUSIC-HL|HL 5+]:  ⟵ “Music (HL) | MM100 and MM105 | Music Fundamentals and Aural Skills 1 | 4 | 5+”
  - equivalencies[IB-PHYSICS-HL|HL 3+]:  ⟵ “Physics (HL) | PH120/PH020 | Introductory Physics I and lab | 5 | 3+”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 3+]:  ⟵ “Psychology (HL) | PY101 | Introduction to Psychology | 3 | 3+”
  - equivalencies[IB-SPANISH-HL|HL 3 or 4]:  ⟵ “Spanish, Language B (HL) | SN100 | Spanish Language and Culture I | 3 | 3 or 4”
  - equivalencies[IB-SPANISH-HL|HL 3+]:  ⟵ “Spanish, Language A2 (HL) | SN100 & SN120 | Spanish Language and Culture I & II | 6 | 3+”
  - equivalencies[IB-THEATRE-HL|HL 3+]:  ⟵ “Theatre Arts (HL) | TH100 | Theatre Appreciation | 3 | 3+”
  - equivalencies[IB-HISTORY-HL|HL 3+]:  ⟵ “History of Africa (HL) | WH100 | African Civilization | 3 | 3+”
### `1ab65e92962962ec` Southeast Missouri State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://semo.edu/student-support/academic-support/registrar/catalog/policies (sha256 632dbd6936e6)
- checks: {"distinct_exams": 33, "equivalencies": 40, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3+]:  ⟵ “African American Studies | US150 | African American Experience in US History I | 3 | 3+”
  - equivalencies[AP-ART-HISTORY|3+]:  ⟵ “Art History | AH198 | Art History Elective | 3 | 3+”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Art Studio Drawing | AR198 | Art Elective | 3 | 3+”
  - equivalencies[AP-2-D-ART-DESIGN|3+]:  ⟵ “Art: Studio Art 2-D Design | AR198 | Art Elective | 3 | 3+”
  - equivalencies[AP-3-D-ART-DESIGN|3+]:  ⟵ “Art: Studio Art 3-D Design | AR198 | Art Elective | 3 | 3+”
  - equivalencies[AP-BIOLOGY|3+]:  ⟵ “Biology | BS108 | Biology for Living | 3 | 3+”
  - equivalencies[AP-CALCULUS-AB|3+]:  ⟵ “Calculus AB | MA140 | Analytical Geometry & Calculus I | 5 | 3+”
  - equivalencies[AP-CALCULUS-BC|3+]:  ⟵ “Calculus BC | MA140/MA145 | Analytical Geometry & Calculus I & II | 9 | 3+”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | CH185 & CH184 | General Chemistry I/Lab | 4 | 3”
  - equivalencies[AP-CHEMISTRY|4+]:  ⟵ “Chemistry | CH185 & CH186 & CH184 | General Chemistry I & II/Lab | 7 | 4+”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3+]:  ⟵ “Computer Science A | CS155 | Computer Science I | 3 | 3+”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3+]:  ⟵ “Computer Science Principles | CS101 | Introduction to Computer Programming | 3 | 3+”
  - equivalencies[AP-MACROECONOMICS|3+]:  ⟵ “Economics: Macroeconomics | EC225 | Principles of Macroeconomics | 3 | 3+”
  - equivalencies[AP-MICROECONOMICS|3+]:  ⟵ “Economics: Microeconomics | EC215 | Principles of Microeconomics | 3 | 3+”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Language & Composition | EN100 | English Composition | 3 | 3+”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3+]:  ⟵ “English Literature & Composition | LI256 | Variety of Literature | 3 | 3+”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science | BS105 | Environmental Biology | 3 | 3+”
  - equivalencies[AP-EUROPEAN-HISTORY|3 or 4]:  ⟵ “European History | EH101 | Early European Civilization | 3 | 3 or 4”
  - equivalencies[AP-EUROPEAN-HISTORY|5]:  ⟵ “European History | EH101 & EH103 | Early European Civilization & Modern European Civilization | 6 | 5”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | FR100 | French Language & Culture I | 3 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4+]:  ⟵ “French Language | FR100 & FR120 | French Language and Culture I & II | 6 | 4+”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | GN100 | German Language and Culture I | 3 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4+]:  ⟵ “German Language | GN100 & GN120 | German Language and Culture I & II | 6 | 4+”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3+]:  ⟵ “Human Geography | GG180 | Cultural Geography | 3 | 3+”
  - equivalencies[AP-LATIN|3+]:  ⟵ “Latin: Vergil | LT198 | Latin Elective | 3 | 3+”
  - … 15 more rows
### `5fa7f23632b6fc39` Southeast Missouri State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://semo.edu/student-support/academic-support/registrar/catalog/policies (sha256 632dbd6936e6)
- checks: {"distinct_exams": 23, "equivalencies": 28, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government (reguires MO Gov't exam) | US Political Systems | PS103 | 3 | 50”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | Biology for Living | BS108 | 3 | 50”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | Applied Calculus | MA139 | 3 | 50”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | General Chemistry I & II plus General Chemistry I Lab | CH184/185/186 | 7 | 50”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | Precalculus A | MA116 | 3 | 50”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|60]:  ⟵ “College Composition | English Composition | EH100 | 3 | 60”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | Mathematical Reasoning and Modeling | MA123 | 3 | 50”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | Principles of Accounting | AC221 | 3 | 50”
  - equivalencies[CLEP-FRENCH-LANGUAGE|45-49]:  ⟵ “French Language: Levels 1 and 2 | French Language and Culture I | FR100 | 3 | 45-49”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50-62]:  ⟵ “French Language: Levels 1 and 2 | French Language and Culture I and II | FR100/120 | 6 | 50-62”
  - equivalencies[CLEP-FRENCH-LANGUAGE|63+]:  ⟵ “French Language: Levels 1 and 2 | French Language and Culture I, II, and III | FR100/120/200 | 9 | 63+”
  - equivalencies[CLEP-GERMAN-LANGUAGE|45-49]:  ⟵ “German Language: Levels 1 and 2 | German Language and Culture I | GN100 | 3 | 45-49”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50+]:  ⟵ “German Language: Levels 1 and 2 | German Language and Culture I and II | GN100/120 | 6 | 50+”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | Psychological Development Across the Life Span | PY220 | 3 | 50”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | Management Information Systems | MI375 | 3 | 50”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | Business Law | BL255 | 3 | 50”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | Introduction to Psychology | PY101 | 3 | 50”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | Introduction to Sociology | SO101 | 3 | 50”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | Precalculus | MA137 | 5 | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | Principles of Macroeconomics | EC225 | 3 | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | Principles of Management | MG301 | 3 | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | Principles of Marketing | MK301 | 3 | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | Principles of Microeconomics | EC215 | 3 | 50”
  - equivalencies[CLEP-SPANISH-LANGUAGE|45-49]:  ⟵ “Spanish Language: Levels 1 and 2 | Spanish Language and Culture I | SN100 | 3 | 45-49”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50-62]:  ⟵ “Spanish Language: Levels 1 and 2 | Spanish Language and Culture I and II | SN100/120 | 6 | 50-62”
  - … 3 more rows
### `1f2e278a632927cd` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: Dean's Scholar Award(3.30-3.79 GPA) ⟵ “Dean's Scholar Award(3.30-3.79 GPA) | $11,000 | $3,500 | $14,500 | $58,000”
  - award_amount_text: $14,500 ⟵ “Dean's Scholar Award(3.30-3.79 GPA) | $11,000 | $3,500 | $14,500 | $58,000”
### `22eac3ca1f5bed94` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: Dean's Scholar Award(3.70-3.84 GPA) ⟵ “Dean's Scholar Award(3.70-3.84 GPA) | $13,000 | $3,500 | $16,500 | $66,000”
  - award_amount_text: $16,500 ⟵ “Dean's Scholar Award(3.70-3.84 GPA) | $13,000 | $3,500 | $16,500 | $66,000”
### `25f1c2a15bbde473` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Missionary Dependent | $1,000 | Available to students who are a dependent of someone currently serving full-time on the mission field for the International Mission Board (IMB), North American Mission Board (NAMB) or another approved missions organization”
  - eligibility_summary: Available to students who are a dependent of someone currently serving full-time on the mission field for the International Mission Board (IMB), North American Mission Board (NAMB) or another approved missions organization ⟵ “Missionary Dependent | $1,000 | Available to students who are a dependent of someone currently serving full-time on the mission field for the International Mission Board (IMB), North American Mission Board (NAMB) or another approved missions organization”
### `2c987f8c0b9a3fa4` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Church Minister Dependent | $1,000 | Available to students who are a dependent of a full-time church-related vocational professional”
  - eligibility_summary: Available to students who are a dependent of a full-time church-related vocational professional ⟵ “Church Minister Dependent | $1,000 | Available to students who are a dependent of a full-time church-related vocational professional”
### `35f1ddef60eb6093` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - eligibility_summary: Scholarships are available to all students regardless of major, based on auditions or tryouts. Contact your admissions counselor for details. These awards can stack on top of your academic award but not other SBU scholarships/grants. ⟵ “Music Scholarships | Varies | Scholarships are available to all students regardless of major, based on auditions or tryouts. Contact your admissions counselor for details. These awards can stack on top of your academic award but not other SBU scholarships/grants.”
### `3a7852889ea59cec` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: Provost's Scholar Award(3.85-3.99 GPA) ⟵ “Provost's Scholar Award(3.85-3.99 GPA) | $14,000 | $3,500 | $17,500 | $70,000”
  - award_amount_text: $17,500 ⟵ “Provost's Scholar Award(3.85-3.99 GPA) | $14,000 | $3,500 | $17,500 | $70,000”
### `46f88dd804a4f7b2` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “Church-Related Vocation | $2,000 | Available to students pursuing a degree in Biblical Studies, Church Ministry, Church Music, or Missions”
  - eligibility_summary: Available to students pursuing a degree in Biblical Studies, Church Ministry, Church Music, or Missions ⟵ “Church-Related Vocation | $2,000 | Available to students pursuing a degree in Biblical Studies, Church Ministry, Church Music, or Missions”
### `634daa4d82693d07` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “A+ Scholarship(Missouri Residents) | $1,000 | Available to incoming freshmen students who have met A+ requirements in the State of Missouri. Your status must be confirmed by your school.”
  - eligibility_summary: Available to incoming freshmen students who have met A+ requirements in the State of Missouri. Your status must be confirmed by your school. ⟵ “A+ Scholarship(Missouri Residents) | $1,000 | Available to incoming freshmen students who have met A+ requirements in the State of Missouri. Your status must be confirmed by your school.”
### `6701fdcd741679a7` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 ⟵ “Church Matching | Up to $500 | SBU will match a scholarship from your church up to $500, renewable up to four years. (Example: Your church gives you a $1,000 scholarship, and SBU will give you a $500 Church Matching Scholarship). Your church does not have to be a Southern Baptist Church.”
  - eligibility_summary: SBU will match a scholarship from your church up to $500, renewable up to four years. (Example: Your church gives you a $1,000 scholarship, and SBU will give you a $500 Church Matching Scholarship). Your church does not have to be a Southern Baptist Church. ⟵ “Church Matching | Up to $500 | SBU will match a scholarship from your church up to $500, renewable up to four years. (Example: Your church gives you a $1,000 scholarship, and SBU will give you a $500 Church Matching Scholarship). Your church does not have to be a Southern Baptist Church.”
### `7012915304b9fbaf` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: Provost's Scholar Award(3.80-3.99 GPA) ⟵ “Provost's Scholar Award(3.80-3.99 GPA) | $12,000 | $3,500 | $15,500 | $62,000”
  - award_amount_text: $15,500 ⟵ “Provost's Scholar Award(3.80-3.99 GPA) | $12,000 | $3,500 | $15,500 | $62,000”
### `82781ff44c211be8` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - eligibility_summary: SBU's 21 NCAA Division II sports offer scholarships for athletes who are recruited by coaches. Contact your admissions counselor for details. These awards can stack on top of your academic awards but not other SBU scholarships/grants. SBU Athletics Directory ⟵ “Athletic Scholarships | Varies | SBU's 21 NCAA Division II sports offer scholarships for athletes who are recruited by coaches. Contact your admissions counselor for details. These awards can stack on top of your academic awards but not other SBU scholarships/grants. SBU Athletics Directory”
### `9c1397a9390bc317` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - eligibility_summary: These awards are based on need using information from the FAFSA. ⟵ “SBU Grant | Varies | These awards are based on need using information from the FAFSA.”
### `a62146a1059d78e8` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: University Scholar Award (3.30-3.49 GPA) ⟵ “University Scholar Award (3.30-3.49 GPA) | $11,000 | $3,500 | $14,500 | $58,000”
  - award_amount_text: $14,500 ⟵ “University Scholar Award (3.30-3.49 GPA) | $11,000 | $3,500 | $14,500 | $58,000”
### `b26856e0c4d60cb4` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: Bearcat Scholar Award I(3.00-3.29 GPA) ⟵ “Bearcat Scholar Award I(3.00-3.29 GPA) | $10,000 | $3,500 | $13,500 | $54,000”
  - award_amount_text: $13,500 ⟵ “Bearcat Scholar Award I(3.00-3.29 GPA) | $10,000 | $3,500 | $13,500 | $54,000”
### `b66db2182d483fd9` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: Presidential Distinguished Scholar(4.0 GPA or above) ⟵ “Presidential Distinguished Scholar(4.0 GPA or above) | $13,000 | $3,500 | $16,500 | $66,000”
  - award_amount_text: $16,500 ⟵ “Presidential Distinguished Scholar(4.0 GPA or above) | $13,000 | $3,500 | $16,500 | $66,000”
### `c06e639fcdcb357e` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - eligibility_summary: Scholarships are available to all students regardless of major, based on auditions or tryouts. Contact your admissions counselor for details. These awards can stack on top of your academic awards but not other SBU scholarships/grants. ⟵ “Club Sports Scholarships | Varies | Scholarships are available to all students regardless of major, based on auditions or tryouts. Contact your admissions counselor for details. These awards can stack on top of your academic awards but not other SBU scholarships/grants.”
### `c2f3ff8227866413` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: Founder's Award (3.50-3.69 GPA) ⟵ “Founder's Award (3.50-3.69 GPA) | $12,000 | $3,500 | $15,500 | $62,000”
  - award_amount_text: $15,500 ⟵ “Founder's Award (3.50-3.69 GPA) | $12,000 | $3,500 | $15,500 | $62,000”
### `d46b78f4f9b912f8` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Sibling Scholarship | $500 | For students who have a brother or sister attending SBU at the same time (siblings who are currently attending will also receive). This award DOES stack with performance awards.”
  - eligibility_summary: For students who have a brother or sister attending SBU at the same time (siblings who are currently attending will also receive). This award DOES stack with performance awards. ⟵ “Sibling Scholarship | $500 | For students who have a brother or sister attending SBU at the same time (siblings who are currently attending will also receive). This award DOES stack with performance awards.”
### `dbda33631f9a586b` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - gpa_requirement: Bearcat Scholar Award II(2.99 GPA or below) ⟵ “Bearcat Scholar Award II(2.99 GPA or below) | $8,000 | $3,500 | $11,500 | $46,000”
  - award_amount_text: $11,500 ⟵ “Bearcat Scholar Award II(2.99 GPA or below) | $8,000 | $3,500 | $11,500 | $46,000”
### `f966228c95a1f68a` Southwest Baptist University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"thresholds": null}
  - eligibility_summary: Scholarships are available to all students regardless of major, based on auditions or tryouts. Contact your admissions counselor for details. These awards can stack on top of your academic awards but not other SBU scholarships/grants. ⟵ “Speech and Debate Scholarships | Varies | Scholarships are available to all students regardless of major, based on auditions or tryouts. Contact your admissions counselor for details. These awards can stack on top of your academic awards but not other SBU scholarships/grants.”
### `6bb4e1d3d3d363cf` Southwest Baptist University — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sbuniv.edu/cost-and-aid/bolivar-financial-aid.php (sha256 26b95998b29d)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (books included): 30500 ⟵ “Tuition (books included) | $15,250 | $30,500”
  - column:Room (base rate): 4000 ⟵ “Room (base rate) | $2,000 | $4,000”
  - column:Board (20-meal plan): 6000 ⟵ “Board (20-meal plan) | $3,000 | $6,000”
  - column:Required Fees: 2000 ⟵ “Required Fees | $1,000 | $2,000”
  - column:Total: 42500 ⟵ “Total | $21,250 | $42,500”
### `1744d5e26b411e08` Southwest Baptist University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.sbuniv.edu/academics/dual-credit.php (sha256 3723b12a3615)
- checks: {"fields": ["per_credit_hour_charges", "state_grant_accepted"], "tiers": 4}
  - per_credit_hour_charge: 75 ⟵ “| $75 per credit hour”
  - eligibility_tier: 3.0 ⟵ “3.0 GPA = automatic eligibility”
  - eligibility_tier: 2.5 ⟵ “2.5–2.99 GPA = requires counselor or principal recommendation”
  - eligibility_tier: 3.0 ⟵ “3.0 GPA + counselor or principal recommendation”
  - eligibility_tier: 3.0 ⟵ “3.0 GPA + 90th percentile ACT/SAT + counselor recommendation + principal recommendation”
  - per_credit_hour_charge: 75 ⟵ “$75 per credit hour”
  - state_grant_accepted: True ⟵ “DHEWD Dual Credit/Dual Enrollment Scholarship: Eligible students may apply for a scholarship”
### `912199f01f29c153` Southwest Baptist University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.sbuniv.edu/admissions/transfer-students.php (sha256 e9697a43005b)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 75 ⟵ “You may transfer up to 75 hours of credit from two-year colleges and up to 94 hours from other accredited institutions toward a degree.”
### `fca96bfcffa818a2` St Charles Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.stchas.edu/programs-courses/dual-credit.php (sha256 ea0c6e0c9747)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 50 ⟵ “Saving on the cost of college tuition ($50/credit hour)”
  - per_credit_hour_charge: 50 ⟵ “Save on the cost of college tuition ($50/credit hour)”
### `me4b011f6c9e45eb` Three Rivers College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://trcc.edu/academics/dual-credit/?faq=will-my-credits-transfer (sha256 f7cf39056497)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 3, "tiers": 3}
  - per_credit_hour_charge: 66 ⟵ “$66 per credit hour. Includes tuition, fees and textbooks/learning materials.”
  - eligibility_tier: 3.0 ⟵ “Eleventh and twelfth grade students with an overall minimum grade point average of 3.0 (on a 4.0 scale) are automatically eligible for dual credit courses. Students with an overall grade point average between 2.5 – 2.99 (on a 4.0 scale) must provide a signed letter of recommendation from their princ”
  - eligibility_tier: 3.0 ⟵ “Tenth grade students must have an overall minimum grade point average of 3.0 (on a 4.0 scale), provide a signed letter of recommendation from their principal and guidance counselor, and provide written permission from a parent or legal guardian.”
  - eligibility_tier: 3.0 ⟵ “Ninth grade students must have an overall minimum grade point average of 3.0 (on a 4.0 scale), score at the 90th percentile or above on the ACT or SAT, provide a signed letter of recommendation from their principal and guidance counselor, and provide written permission from a parent or legal guardia”
  - per_credit_hour_charge: 66 ⟵ “$66 per credit hour. Includes tuition, fees and textbooks/learning materials.”
  - eligibility_tier: 3.0 ⟵ “Eleventh and twelfth grade students with an overall minimum grade point average of 3.0 (on a 4.0 scale) are automatically eligible for dual credit courses. Students with an overall grade point average between 2.5 – 2.99 (on a 4.0 scale) must provide a signed letter of recommendation from their princ”
  - eligibility_tier: 3.0 ⟵ “Tenth grade students must have an overall minimum grade point average of 3.0 (on a 4.0 scale), provide a signed letter of recommendation from their principal and guidance counselor, and provide written permission from a parent or legal guardian.”
  - eligibility_tier: 3.0 ⟵ “Ninth grade students must have an overall minimum grade point average of 3.0 (on a 4.0 scale), score at the 90th percentile or above on the ACT or SAT, provide a signed letter of recommendation from their principal and guidance counselor, and provide written permission from a parent or legal guardia”
  - per_credit_hour_charge: 66 ⟵ “$66 per credit hour. Includes tuition, fees and textbooks/learning materials.”
  - eligibility_tier: 3.0 ⟵ “Eleventh and twelfth grade students with an overall minimum grade point average of 3.0 (on a 4.0 scale) are automatically eligible for dual credit courses. Students with an overall grade point average between 2.5 – 2.99 (on a 4.0 scale) must provide a signed letter of recommendation from their princ”
  - eligibility_tier: 3.0 ⟵ “Tenth grade students must have an overall minimum grade point average of 3.0 (on a 4.0 scale), provide a signed letter of recommendation from their principal and guidance counselor, and provide written permission from a parent or legal guardian.”
  - eligibility_tier: 3.0 ⟵ “Ninth grade students must have an overall minimum grade point average of 3.0 (on a 4.0 scale), score at the 90th percentile or above on the ACT or SAT, provide a signed letter of recommendation from their principal and guidance counselor, and provide written permission from a parent or legal guardia”
### `2a8ebf0be80c4753` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/automatic-scholarships/ (sha256 866c7b763066)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 for students living on campus $1,000 for students living off campus. Scholarship will be renewed based on SAP criteria at the original award amount. This scholarship does NOT stack with Top Scholar or TruPlus ⟵ “Northeast Missouri (NEMO) Scholarship | MUST have graduated from a high school in one of the following counties: Adair, Putnam, Schuyler, Scotland, Knox, Macon, Linn, Sullivan. | $2,000 for students living on campus $1,000 for students living off campus. Scholarship will be renewed based on SAP crit”
  - eligibility_summary: MUST have graduated from a high school in one of the following counties: Adair, Putnam, Schuyler, Scotland, Knox, Macon, Linn, Sullivan. ⟵ “Northeast Missouri (NEMO) Scholarship | MUST have graduated from a high school in one of the following counties: Adair, Putnam, Schuyler, Scotland, Knox, Macon, Linn, Sullivan. | $2,000 for students living on campus $1,000 for students living off campus. Scholarship will be renewed based on SAP crit”
### `5e113b75c625e38c` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/automatic-scholarships/ (sha256 866c7b763066)
- checks: {"thresholds": null}
  - award_amount_text: $500 per year ⟵ “A+ Recognition | Truman-funded and automatically awarded to admitted freshman in recognition of Missouri A+ program completion. Program completion must be verified on the final high school transcript. | $500 per year”
  - eligibility_summary: Truman-funded and automatically awarded to admitted freshman in recognition of Missouri A+ program completion. Program completion must be verified on the final high school transcript. ⟵ “A+ Recognition | Truman-funded and automatically awarded to admitted freshman in recognition of Missouri A+ program completion. Program completion must be verified on the final high school transcript. | $500 per year”
### `88aa4eb2953286db` Truman State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/competitive-scholarships/ (sha256 1a03936c6393)
- checks: {"thresholds": null}
  - award_amount_text: Approximately twelve awards annually. The Pershing scholarship covers the cost of full-time tuition and the average cost of room and board, plus a one-time $4,000 study abroad stipend. SUPERSEDES ALL OTHER TRUMAN FUNDED AWARDS. ⟵ “General John J. Pershing Scholarship | Top candidates have exceptional academic and co-curricular accomplishments and are typically in the top 3% of their HS class with ACT or SAT scores in the top 3% nationally. Application with ACT/SAT test score, including essay AND activities resume, must be com”
  - eligibility_summary: Top candidates have exceptional academic and co-curricular accomplishments and are typically in the top 3% of their HS class with ACT or SAT scores in the top 3% nationally. Application with ACT/SAT test score, including essay AND activities resume, must be complete prior to Dec. 1 for consideration. ⟵ “General John J. Pershing Scholarship | Top candidates have exceptional academic and co-curricular accomplishments and are typically in the top 3% of their HS class with ACT or SAT scores in the top 3% nationally. Application with ACT/SAT test score, including essay AND activities resume, must be com”
### `aeec6fe430fbf3b5` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/ (sha256 080373ca65c9)
- checks: {"thresholds": null}
  - award_amount_text: Varying amounts ⟵ “President’s Honorary | Limited number of awards given to students. | Varying amounts”
  - eligibility_summary: Limited number of awards given to students. ⟵ “President’s Honorary | Limited number of awards given to students. | Varying amounts”
### `af26aab4ada5e246` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/ (sha256 080373ca65c9)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 per year ⟵ “Girls State & Boys State | Admitted students who attended Girls State or Boys State. | $1,000 per year”
  - eligibility_summary: Admitted students who attended Girls State or Boys State. ⟵ “Girls State & Boys State | Admitted students who attended Girls State or Boys State. | $1,000 per year”
### `baaa62df3e3cf18a` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/automatic-scholarships/ (sha256 866c7b763066)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 per year ⟵ “International Baccalaureate (IB) | IB Diploma Candidate status must be noted on HS transcript for consideration. Completion must be verified on official final transcript. | $2,000 per year”
  - eligibility_summary: IB Diploma Candidate status must be noted on HS transcript for consideration. Completion must be verified on official final transcript. ⟵ “International Baccalaureate (IB) | IB Diploma Candidate status must be noted on HS transcript for consideration. Completion must be verified on official final transcript. | $2,000 per year”
### `bbf8cb2902eab4af` Truman State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/competitive-scholarships/ (sha256 1a03936c6393)
- checks: {"thresholds": null}
  - award_amount_text: The Kirk scholarship is $23,000 for out-of-state students and $17,000 for in-state students. This should cover all of the full-time tuition cost and a significant portion of room and board. With the exception of the Bulldog Legacy Award, the Kirk Scholarship SUPERSEDES ALL OTHER TRUMAN FUNDED AWARDS. ⟵ “President John R. Kirk Scholarship | Top candidates have exceptional academic and co-curricular accomplishments and are typically in the top 3% of their HS class with ACT or SAT scores in the top 3% nationally. Application with ACT/SAT test score, including essay AND activities resume, must be compl”
  - eligibility_summary: Top candidates have exceptional academic and co-curricular accomplishments and are typically in the top 3% of their HS class with ACT or SAT scores in the top 3% nationally. Application with ACT/SAT test score, including essay AND activities resume, must be complete prior to Dec. 1 for consideration. ⟵ “President John R. Kirk Scholarship | Top candidates have exceptional academic and co-curricular accomplishments and are typically in the top 3% of their HS class with ACT or SAT scores in the top 3% nationally. Application with ACT/SAT test score, including essay AND activities resume, must be compl”
### `c2563030166fcc4f` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/ (sha256 080373ca65c9)
- checks: {"thresholds": null}
  - award_amount_text: Missouri residents - $1,000 per year Out-of-State residents - $2,000 per year ⟵ “Bulldog Legacy | Admitted students who are children, step-children, or grandchildren of alumni of Truman, or whose sibling currently attends or graduated from Truman. | Missouri residents - $1,000 per year Out-of-State residents - $2,000 per year”
  - eligibility_summary: Admitted students who are children, step-children, or grandchildren of alumni of Truman, or whose sibling currently attends or graduated from Truman. ⟵ “Bulldog Legacy | Admitted students who are children, step-children, or grandchildren of alumni of Truman, or whose sibling currently attends or graduated from Truman. | Missouri residents - $1,000 per year Out-of-State residents - $2,000 per year”
### `cb38879e105f67ba` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/automatic-scholarships/ (sha256 866c7b763066)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 – $10,000 (See the TruMerit Scholarship Chart) ⟵ “TruMerit Scholarship | Automatically awarded to admitted students based on their GPA and test scores. | $2,000 – $10,000 (See the TruMerit Scholarship Chart)”
  - eligibility_summary: Automatically awarded to admitted students based on their GPA and test scores. ⟵ “TruMerit Scholarship | Automatically awarded to admitted students based on their GPA and test scores. | $2,000 – $10,000 (See the TruMerit Scholarship Chart)”
### `e257bae13137b25f` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/ (sha256 080373ca65c9)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 per year ⟵ “TruMusic Scholarship | Automatically awarded to admitted students who are declared Music majors. | $1,000 per year”
  - eligibility_summary: Automatically awarded to admitted students who are declared Music majors. ⟵ “TruMusic Scholarship | Automatically awarded to admitted students who are declared Music majors. | $1,000 per year”
### `e29c601d0d5082ba` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/automatic-scholarships/ (sha256 866c7b763066)
- checks: {"thresholds": null}
  - award_amount_text: MSEP amount for 2026-2027 academic year is estimated at $4,310. MSEP award value, determined annually, reduces out-of-state tuition to 150% of in-state tuition rate, with this scholarship covering the difference. ⟵ “Midwest Student Exchange Program (MSEP) | Automatically awarded to admitted students from IN, KS, MN, NE, ND, OH and WI who do not qualify for an Out-of-State TruMerit Scholarship. | MSEP amount for 2026-2027 academic year is estimated at $4,310. MSEP award value, determined annually, reduces out-of”
  - eligibility_summary: Automatically awarded to admitted students from IN, KS, MN, NE, ND, OH and WI who do not qualify for an Out-of-State TruMerit Scholarship. ⟵ “Midwest Student Exchange Program (MSEP) | Automatically awarded to admitted students from IN, KS, MN, NE, ND, OH and WI who do not qualify for an Out-of-State TruMerit Scholarship. | MSEP amount for 2026-2027 academic year is estimated at $4,310. MSEP award value, determined annually, reduces out-of”
### `f02bc5ca796cb17e` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/automatic-scholarships/ (sha256 866c7b763066)
- checks: {"thresholds": null}
  - award_amount_text: Varying amounts awarded by Office of Financial Aid - FAFSA required. ⟵ “Truman Pathway Grant | Automatically awarded through the Department of Financial Aid to qualifying Missouri residents who are Pell Grant-eligible, incoming freshman pursuing their first bachelor's degree, and who enroll full time. See additional information on eligibility. | Varying amounts awarded ”
  - eligibility_summary: Automatically awarded through the Department of Financial Aid to qualifying Missouri residents who are Pell Grant-eligible, incoming freshman pursuing their first bachelor's degree, and who enroll full time. See additional information on eligibility. ⟵ “Truman Pathway Grant | Automatically awarded through the Department of Financial Aid to qualifying Missouri residents who are Pell Grant-eligible, incoming freshman pursuing their first bachelor's degree, and who enroll full time. See additional information on eligibility. | Varying amounts awarded ”
### `fb494aa27cdb7116` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/ (sha256 080373ca65c9)
- checks: {"thresholds": null}
  - award_amount_text: Limited number of 2025 awards. The HSTL scholarship is $15,000 and only in-state students were eligible. This should cover all of the full-time tuition cost and a significant portion of room and board.With the exception of the Bulldog Legacy Award, the HST Scholarship SUPERSEDES ALL OTHER TRUMAN FUNDED AWARDS. ⟵ “Harry S. Truman Leadership Scholarship | Missouri residents who demonstrate impactful classroom, school and/or community leadership. Designed to invest in the development of tomorrow’s leaders, recognizing the value of diverse contributions in Truman’s community. Application with ACT/SAT test score,”
  - eligibility_summary: Missouri residents who demonstrate impactful classroom, school and/or community leadership. Designed to invest in the development of tomorrow’s leaders, recognizing the value of diverse contributions in Truman’s community. Application with ACT/SAT test score, including essay AND activities resume, must be complete prior to Dec. 1 for consideration. ⟵ “Harry S. Truman Leadership Scholarship | Missouri residents who demonstrate impactful classroom, school and/or community leadership. Designed to invest in the development of tomorrow’s leaders, recognizing the value of diverse contributions in Truman’s community. Application with ACT/SAT test score,”
### `fbe914c4111efd2a` Truman State University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/scholarships/ (sha256 080373ca65c9)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 per year ⟵ “JBA Scholarship | Automatically awarded to students who attended Joseph Baldwin Academy (JBA). | $1,000 per year”
  - eligibility_summary: Automatically awarded to students who attended Joseph Baldwin Academy (JBA). ⟵ “JBA Scholarship | Automatically awarded to students who attended Joseph Baldwin Academy (JBA). | $1,000 per year”
### `2198927516741a4b` Truman State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/tuition-costs/ (sha256 b9b5f95171fe)
- checks: {"columns": 1, "rows": 3}
  - column:*Tuition (2026-27): 10658 ⟵ “*Tuition (2026-27) | $10,658 | $20,297”
  - column:Average Fees: 1170 ⟵ “Average Fees | $1,170 | $1,170”
  - column:Direct Costs Subtotal: 11828 ⟵ “Direct Costs Subtotal | $11,828 | $21,467”
### `e30b7f58ff5e0394` Truman State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.truman.edu/admission-cost/cost-aid/tuition-costs/ (sha256 b9b5f95171fe)
- checks: {"columns": 1, "rows": 3}
  - column:*Tuition (2026-27): 20297 ⟵ “*Tuition (2026-27) | $10,658 | $20,297”
  - column:Average Fees: 1170 ⟵ “Average Fees | $1,170 | $1,170”
  - column:Direct Costs Subtotal: 21467 ⟵ “Direct Costs Subtotal | $11,828 | $21,467”
### `m09194bacd689068` Truman State University — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://international.truman.edu/new-students/costs/ug/ (sha256 78adec1610c3)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - residency_requirement_credits: 28 ⟵ “Requirements for a Bachelor's Degree: Students must earn a minimum of 45 credit hours of credit in Truman coursework, with the last 28 credit hours taken immediately preceding completing the degree requirements.”
  - min_grade: C ⟵ “Students must achieve a grade of C or higher to receive transfer credit for qualified A-Levels.”
### `7c878d69d8059bfe` University of Central Missouri — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ucmo.edu/future-students/tuition-and-costs/index.php (sha256 b90609effbd5)
- checks: {"columns": 1, "rows": 5}
  - column:Tuition & General Fees: 10951 ⟵ “Tuition & General Fees | $10,951 | $20,278”
  - column:Textbooks: 1250 ⟵ “Textbooks | $1,250 | $1,250”
  - column:Residence Hall (double room): 7000 ⟵ “Residence Hall (double room) | $7,000 | $7,000”
  - column:Meal Plan: 4306 ⟵ “Meal Plan | $4,306 | $4,306”
  - column:You Invest: 23507 ⟵ “You Invest | $23,507 | $32,834*”
### `98ec8ef1220f2be5` University of Central Missouri — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ucmo.edu/future-students/tuition-and-costs/index.php (sha256 b90609effbd5)
- checks: {"columns": 1, "rows": 5}
  - column:Tuition & General Fees: 20278 ⟵ “Tuition & General Fees | $10,951 | $20,278”
  - column:Textbooks: 1250 ⟵ “Textbooks | $1,250 | $1,250”
  - column:Residence Hall (double room): 7000 ⟵ “Residence Hall (double room) | $7,000 | $7,000”
  - column:Meal Plan: 4306 ⟵ “Meal Plan | $4,306 | $4,306”
  - column:You Invest: 32834 ⟵ “You Invest | $23,507 | $32,834*”
### `99f58f9bed2ba8ab` University of Missouri-St Louis — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.umsl.edu/admissions/early-credit-student/clep.html (sha256 72d6b58bb36c)
- checks: {"distinct_exams": 31, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POL SCI 1100 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | Transfer Humanities Credit | 3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH 1800 | 5”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 1030 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | Transfer Elective Credit | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | Transfer Proficiency | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “College French Levels 1 & 2 | 50 | FRENCH 1001/1002 | 10”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “College German Levels 1 & 2 | 50 | GERMAN 1001/1002 | 10”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “College Spanish Levels 1 & 2 | 50 | SPANISH 1001/1002 | 10”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL 1120 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | General Elective Credit | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “Freshmen College Composition | 50 | Transfer Proficiency | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “General Biology | 50 | BIOL 1012 | 3”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “General Chemistry | 50 | CHEM 1111A/1121A | 6”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | HIST 1001 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | HIST 1002 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSYCH 1268 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | General Elective Credit | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | ED PSY 3312 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | Elective Credit Until Validated | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSYCH 1003 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC 1010 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | 50 | MATH 1030/1035 | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECON 1002 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECON 1001 | 3”
  - … 8 more rows
### `a8ad351f1dcd439b` University of Missouri-St Louis — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.umsl.edu/dep/index.html (sha256 1c12eaebc8ec)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Successful DEP students will typically have a 3.0 or higher GPA in their core courses. Students who would like to take courses through the Honors College at UMSL must have a 3.2 GPA and/or participate in the Honors program at their high school.”
### `c7cf365fc217b1cd` University of Missouri-St Louis — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.umsl.edu/admissions/early-credit-student/ib.html (sha256 5a4d14f2722a)
- checks: {"distinct_exams": 20, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[IB-FRENCH-SL|SL 4]:  ⟵ “French SL | 4 | French 2101 | 3 | 6 | French 2170 and 2190 | 6”
  - equivalencies[IB-FRENCH-HL|HL 4]:  ⟵ “French HL | 4 | French 2101 | 3 | 5 | French 2170 and 2180 | 6”
  - equivalencies[IB-SPANISH-SL|SL 4]:  ⟵ “Spanish SL | 4 | Spanish 2101 | 3 | 6 | Spanish 2172 and 2190 | 6”
  - equivalencies[IB-SPANISH-HL|HL 4]:  ⟵ “Spanish HL | 4 | Spanish 2101 | 3 | 5 | Spanish 2180 and 2190 | 6”
  - equivalencies[IB-GERMAN-SL|SL 4]:  ⟵ “German SL | 4 | German 2101 | 3 | 6 | German 2170 and 2190 | 6”
  - equivalencies[IB-GERMAN-HL|HL 4]:  ⟵ “German HL | 4 | German 2101 | 3 | 5 | German 2170 and 2180 | 6”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business Management | 4 | BUSINESS ELECTIVE | 3”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | 5 | ECONOMICS 1001 / ECON 1002 | 3”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOGRAPHY / SOC SCI ELECT | 3”
  - equivalencies[IB-HISTORY|5]:  ⟵ “History of the Americas | 5 | HIST SOC SCI / CULT DIVERS | 3”
  - equivalencies[IB-HISTORY|5]:  ⟵ “History of Europe | 5 | HIST 1031 / HIST 1032 | 3”
  - equivalencies[IB-HISTORY|4]:  ⟵ “Twentieth History World | 4 | HISTORY/SOCIAL SCI ELECT | 3”
  - equivalencies[IB-PHILOSOPHY|4]:  ⟵ “Philosophy | 4 | PHIL 1150 | ”
  - equivalencies[IB-PSYCHOLOGY|4]:  ⟵ “Psychology | 4 | PSYCH 1003 | ”
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | 5 | BIOL 1831 | 5”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 1111 / CHEM 1121 | 5”
  - equivalencies[IB-COMPUTER-SCIENCE|4]:  ⟵ “Computer Science | 4 | MATH/SCIENCE ELECT | 3”
  - equivalencies[IB-FILM|4]:  ⟵ “Film | 4 | HUMANITIES ELECT | 3”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music | 4 | MHLT/HUMANITIES/CULTURAL DIV | 6”
  - equivalencies[IB-THEATRE|4]:  ⟵ “Theatre | 4 | THEATRE/HUMANITIES ELECT | 4”
  - equivalencies[IB-VISUAL-ARTS|4]:  ⟵ “Visual Arts | 4 | HUMANITIES ELECT | 3”
  - equivalencies[IB-BIOLOGY|C]:  ⟵ “Biology | C | BIOL 1012 & 1013 (5 credit hours) | BIOL 1821 & 1831 (10 credit hours)”
  - equivalencies[IB-CHEMISTRY|C]:  ⟵ “Chemistry | C | CHEM 1111 (5 credit hours) | CHEM 1111 & 1121 (10 credit hours)”
  - equivalencies[IB-COMPUTER-SCIENCE|C]:  ⟵ “Computer Science | C | No Credit | Computer Science Elective (6 credit hours)”
  - equivalencies[IB-ECONOMICS|C]:  ⟵ “Economics | C | ECON 1000 (3 credit hours) | ECON 1001 & 1002 (3 credit hours)”
  - … 4 more rows
### `50508d5c3cd9f070` Webster University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.webster.edu/admissions/undergraduate/prior-learning.php (sha256 4752ecec4b24)
- checks: {"distinct_exams": 31, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | ROC | General Elective | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ROC | General Elective | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | - | General Elective | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|59]:  ⟵ “College Composition | 59 | WCOM | WRIT 1010 Composition and General Elective | 6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “English Composition Modular | 50 | WCOM | General Elective | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ROC | General Elective | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | ROC | General Elective | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language* | 50 | GLBL and INTC | FREN 1090 Elementary French Level I,FREN 1100 Elementary French Level II | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language* | 59 | GLBL and INTC | FREN 1090 Elementary French Level I,FREN 1100 Elementary French Level II,FREN 2090 Intermediate French Level I | 9”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language* | 50 | GLBL and INTC | GRMN 1090 Elementary German Level I,GRMN 1100 Elementary German Level II | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|59]:  ⟵ “German Language* | 59 | GLBL and INTC | GRMN 1090 Elementary German Level I,GRMN 1100 Elementary German Level II,GRMN 2090 Intermediate German Level I | 9”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language* | 50 | GLBL and INTC | SPAN 1090 Elementary Spanish Level I,SPAN 1100 Elementary Spanish Level II | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|59]:  ⟵ “Spanish Language* | 59 | GLBL and INTC | SPAN 1090 Elementary Spanish Level I,SPAN 1100 Elementary Spanish Level II,SPAN 2090 Intermediate Spanish Level I | 9”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | SSHB | POLT 1060 Introduction to American Politics | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | SSHB | PSYC 2300 Lifespan Development | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology | 50 | SSHB | PSYC 2400 Educational Psychology | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Prin of Macroeconomics | 50 | SSHB | ECON 2030 Principles of MacroeconomicsIf Principles of Microeconomics and Principles of Macroeconomics are taken together, they will satisfy ECON 2000 Survey of Economics, which is required of most majors in the School of Business. See the catalog for requirement”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Prin of Microeconomics | 50 | SSHB | ECON 2020 Principles of MicroeconomicsIf Principles of Microeconomics and Principles of Macroeconomics are taken together, they will satisfy ECON 2000 Survey of Economics, which is required of most majors in the School of Business. See the catalog for requirement”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Intro Psychology | 50 | SSHB | PSYC 1100 Introduction to Psychology | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Intro Sociology | 50 | SSHB | SOCI 1100 Introduction to Sociology | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | SSHB | General Elective | 6”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civ I: Ancient Near East to 1648 | 50 | ROC | General Elective | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civ II: 1648 to Present | 50 | ROC | General Elective | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology** | 50 | PNW | General Elective | 6”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | QL | MATH 1470 Survey of Calculus | 3”
  - … 10 more rows
### `103c5879cbc95a68` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 awarded in addition to Merit-Based awards. ⟵ “Alumni/Sibling Award | Students having a brother or sister attending, or a sibling, parent or grandparent who is an alumnus of Westminster College. | $1,000 awarded in addition to Merit-Based awards.”
  - eligibility_summary: Students having a brother or sister attending, or a sibling, parent or grandparent who is an alumnus of Westminster College. ⟵ “Alumni/Sibling Award | Students having a brother or sister attending, or a sibling, parent or grandparent who is an alumnus of Westminster College. | $1,000 awarded in addition to Merit-Based awards.”
### `21199e25fcbd3928` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: $21,000 ⟵ “Leadership Award | $21,000 | Under 3.00 GPA or under 1100 SAT or under 22 ACT”
  - eligibility_summary: Under 3.00 GPA or under 1100 SAT or under 22 ACT ⟵ “Leadership Award | $21,000 | Under 3.00 GPA or under 1100 SAT or under 22 ACT”
### `3014ac38ef9d5e5b` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: $27,000 ⟵ “Churchill Scholarship | $27,000 | 4.00+ GPA or 1360+ SAT or 30+ ACT”
  - eligibility_summary: 4.00+ GPA or 1360+ SAT or 30+ ACT ⟵ “Churchill Scholarship | $27,000 | 4.00+ GPA or 1360+ SAT or 30+ ACT”
### `45c8baf8c25e6d5a` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 ⟵ “Cheer Scholarship | Cheerleaders who are interested in being a member of our cheer squad may submit the application to be considered for the Cheer Scholarship. | Up to $3,000”
### `50ea7d9c80aa51ac` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: $25,000 ⟵ “Trustee's Scholarship | $25,000 | 3.75-3.99 GPA or 1300-1350 SAT or 28-29 ACT”
  - eligibility_summary: 3.75-3.99 GPA or 1300-1350 SAT or 28-29 ACT ⟵ “Trustee's Scholarship | $25,000 | 3.75-3.99 GPA or 1300-1350 SAT or 28-29 ACT”
### `6f9abbaff7efd170` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: $23,000 ⟵ “Dean's Scholarship | $23,000 | 3.00-3.49 GPA or 1100-1190 SAT or 22-24 ACT”
  - eligibility_summary: 3.00-3.49 GPA or 1100-1190 SAT or 22-24 ACT ⟵ “Dean's Scholarship | $23,000 | 3.00-3.49 GPA or 1100-1190 SAT or 22-24 ACT”
### `75ccf46798ee9526` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 awarded in addition to Merit-Based awards. ⟵ “FAFSA Priority Award | Students must submit the FAFSA by our priority deadline, November 15. | $1,000 awarded in addition to Merit-Based awards.”
  - eligibility_summary: Students must submit the FAFSA by our priority deadline, November 15. ⟵ “FAFSA Priority Award | Students must submit the FAFSA by our priority deadline, November 15. | $1,000 awarded in addition to Merit-Based awards.”
### `9b38a232fbb1b429` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: Varies and may be awarded in addition to Merit-Based awards. ⟵ “Westminster Grant | Students who demonstrate financial need after filing the FAFSA will be considered for this grant. | Varies and may be awarded in addition to Merit-Based awards.”
  - eligibility_summary: Students who demonstrate financial need after filing the FAFSA will be considered for this grant. ⟵ “Westminster Grant | Students who demonstrate financial need after filing the FAFSA will be considered for this grant. | Varies and may be awarded in addition to Merit-Based awards.”
### `c621b5dbbd880494` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 ⟵ “Music Award | Vocalists interested in being a member of our vocal ensembles may submit the Music Questionnaire and audition for a Music Award. | Up to $3,000”
### `e864dbace65f5bfa` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: $24,000 ⟵ “President's Scholarship | $24,000 | 3.50-3.74 GPA or 1200-1290 SAT or 25-27 ACT”
  - eligibility_summary: 3.50-3.74 GPA or 1200-1290 SAT or 25-27 ACT ⟵ “President's Scholarship | $24,000 | 3.50-3.74 GPA or 1200-1290 SAT or 25-27 ACT”
### `ec097f5e0e5823ab` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: 1 full-tuition award offered annually to a top academically achieving freshman student. ⟵ “The G. Robert Muehlhauser Award of Excellence | 1 full-tuition award offered annually to a top academically achieving freshman student. | ”
### `f7c4a375f564373e` Westminster College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/types-aid/scholarships.html (sha256 3dd900c9197c)
- checks: {"thresholds": null}
  - award_amount_text: Varies and may be awarded in lieu of Westminster College's Merit-Based awards. ⟵ “Endowed Scholarship | Named scholarships, funded by alumni and friends of the College, that students can be considered for after they file the FAFSA. | Varies and may be awarded in lieu of Westminster College's Merit-Based awards.”
  - eligibility_summary: Named scholarships, funded by alumni and friends of the College, that students can be considered for after they file the FAFSA. ⟵ “Endowed Scholarship | Named scholarships, funded by alumni and friends of the College, that students can be considered for after they file the FAFSA. | Varies and may be awarded in lieu of Westminster College's Merit-Based awards.”
### `ae2a3f704cd169aa` Westminster College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.wcmo.edu/academics/degree/transferring-credit.html (sha256 eb1fc2158b9b)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Dual credit courses will be considered for transfer as long as the student has received a grade of "C" or better in the course.”
### `3d1a2e408502eb2d` William Jewell College — awards 2026-27 [new] (source_unlabeled)
- source: https://jewell.edu/scholarships/ (sha256 ebbbad02add2)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “Jewell Scholar | 3.25 – 3.49 | $3,000”
  - gpa_requirement: 3.25 – 3.49 ⟵ “Jewell Scholar | 3.25 – 3.49 | $3,000”
### `59c49bdee2eac785` William Jewell College — awards 2026-27 [new] (source_unlabeled)
- source: https://jewell.edu/scholarships/ (sha256 ebbbad02add2)
- checks: {"thresholds": null}
  - test_requirement: Score: ACT 24-27 / SAT 1160-1290 ⟵ “ACT 24-27 / SAT 1160-1290 | $1,000”
  - award_amount_text: $1,000 ⟵ “ACT 24-27 / SAT 1160-1290 | $1,000”
### `614c79873f74b781` William Jewell College — awards 2026-27 [new] (source_unlabeled)
- source: https://jewell.edu/scholarships/ (sha256 ebbbad02add2)
- checks: {"thresholds": null}
  - test_requirement: Score: ACT 28+ / SAT 1300+ ⟵ “ACT 28+ / SAT 1300+ | $2,000”
  - award_amount_text: $2,000 ⟵ “ACT 28+ / SAT 1300+ | $2,000”
### `c08d3feb0a7c07ff` William Jewell College — awards 2026-27 [new] (source_unlabeled)
- source: https://jewell.edu/scholarships/ (sha256 ebbbad02add2)
- checks: {"thresholds": {"gpa_min": 3.75}}
  - award_amount_text: $5,000 ⟵ “Presidential Scholar | 3.75 and above | $5,000”
  - gpa_requirement: 3.75 and above ⟵ “Presidential Scholar | 3.75 and above | $5,000”
### `c876f1563d96006d` William Jewell College — awards 2026-27 [new] (source_unlabeled)
- source: https://jewell.edu/scholarships/ (sha256 ebbbad02add2)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ⟵ “Trustee Scholar | 3.5 – 3.75 | $4,000”
  - gpa_requirement: 3.5 – 3.75 ⟵ “Trustee Scholar | 3.5 – 3.75 | $4,000”

## Exceptions (269)

### `039faa55f016193e` state-MO — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://dhewd.mo.gov/higher-education/cota (sha256 580e049c2cf7)
- issues: semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “The success of our collective student body requires that Missouri institutions operate in a coordinated fashion to ensure that higher education is accessible and affordable.”
### `5b0f0e9e108eef89` state-MO — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://dhewd.mo.gov/ppc/grants-scholarships/dcde/students (sha256 d1ef7a5563d4)
- issues: semantic_review_required
- checks: {"requirements": 14}
  - statements.requirements: 14 ⟵ “Applicants must meet the following requirements: 1.”
### `a53ed8f4aa431af1` state-MO — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://dhewd.mo.gov/ppc/grants-scholarships/dcde (sha256 082b938ab8a3)
- issues: semantic_review_required
- checks: {"requirements": 5}
  - statements.requirements: 5 ⟵ “Financial need is now required for eligibility rather than being used to determine award ranking.”
### `b26168076d69902a` state-MO — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://dhewd.mo.gov/higher-education/mrt (sha256 b91c5e23bc32)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Even students who are not currently attending college may be eligible to complete an associate degree through the Missouri Reverse Transfer program.”
### `c8c5e4ef504e1c9e` state-MO — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://dhewd.mo.gov/higher-education/academic-affairs/core-42 (sha256 1d77558c56c8)
- issues: semantic_review_required
- checks: {"effective": 5, "exceptions": 6, "guarantees": 5, "requirements": 47}
  - statements.guarantees: 5 ⟵ “MOTR Equivalent Course credits are guaranteed to transfer one-to-one and serve the same role (including as prerequisites) as the receiving IHE’s equivalent course.”
  - statements.exceptions: 6 ⟵ “MOTR Equivalent Course designation does not guarantee that the course will satisfy every major, minor, concentration, certification, or program requirement at every CORE 42 Institution of Higher Education (IHE). “CORE 42 Complete” transfers as a block, which means lower-division general education is”
  - statements.requirements: 47 ⟵ “The CCAC is composed of representatives from each participating institution, per SB 997 a majority are required to be faculty members.”
  - statements.effective: 5 ⟵ “Through general education, Missouri IHEs foster student success in their specialized areas of study and toward rewarding lives as educated persons, active citizens, and effective contributors to their own prosperity and to the general welfare of the world in which they live.”
### `d966a21660c9bb86` state-MO — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://dhewd.mo.gov/higher-education/mrt/legislation (sha256 536186169a04)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 2}
  - statements.requirements: 2 ⟵ “Missouri Reverse Transfer Legislation | dhewd.mo.gov Missouri Department of Higher Education and Workforce Development Legislation signed into law in 2012 called for the development of a reverse transfer policy to increase the number of associate degrees for eligible students in Missouri.”
  - statements.exceptions: 1 ⟵ “Several one-to-one agreements between two- and four- year colleges and universities in Missouri existed; however, common guidelines, policies and technology pathways can significantly streamline the process for higher education institutions and students.”
### `9d299a83d875d151` Avila University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.avila.edu/avila-life/sleptiza-center-for-student-excellence/student-financial-services/tuition/ (sha256 293434b1874a)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 12}
  - column:Campus Fee (Traditional Undergraduate Students): 1000 ⟵ “Campus Fee (Traditional Undergraduate Students) | $1,000 | per year”
  - column:Nursing Program Fee – TBSN: 1200 ⟵ “Nursing Program Fee – TBSN | $1,200 | per academic year”
  - column:Nursing Program Fee – ABSN: 1800 ⟵ “Nursing Program Fee – ABSN | $1,800 | per academic year”
  - column:Low Residency Event Fee: 200 ⟵ “Low Residency Event Fee | $200 | per semester”
  - column:International Student Health Insurance: 1260 ⟵ “International Student Health Insurance | $1,260 | per year”
  - column:Rad Tech Program Fee: 440 ⟵ “Rad Tech Program Fee | $440 | per year”
  - column:Rad. Tech. Enrichment/Board Prep: 510 ⟵ “Rad. Tech. Enrichment/Board Prep | $510 | per credit”
  - column:Credential Filing Fee: 35 ⟵ “Credential Filing Fee | $35 | per occurrence”
  - column:Off-Campus Graduate Teaching: 75 ⟵ “Off-Campus Graduate Teaching | $75 | per credit”
  - column:Tuition Remission Fee: 750 ⟵ “Tuition Remission Fee | $750 | —”
  - column:Housing Assessment Fee (Room & Board): 125 ⟵ “Housing Assessment Fee (Room & Board) | $125 | per term”
  - column:Health Services Fee: 30 ⟵ “Health Services Fee | $30 | per semester”
### `6d95c622eb347ebf` Bolivar Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bolivarcollege.edu/wp-content/uploads/2026/07/Practical-Nursing-Tuition-2026-2027.pdf (sha256 173b83aacd6f)
- issues: conflicting_sources:https://www.bolivarcollege.edu/wp-content/uploads/2026/07/Professional-Nursing-Tuition-2026-2027.pdf
- checks: {"columns": 1, "rows": 10}
  - column:Clinical tuition (3 semester track: per semester): 1135.0 ⟵ “Clinical tuition (3 semester track: per semester) | $1,135.00”
  - column:Simulation & skills center fee (per semester): 500.0 ⟵ “Simulation & skills center fee (per semester) | $500.00”
  - column:Science lab fee (per gen ed. science class, per semester): 140.0 ⟵ “Science lab fee (per gen ed. science class, per semester) | $140.00”
  - column:Online Connect Access (includes eBook): 100.0 ⟵ “Online Connect Access (includes eBook) | $100.00”
  - column:Student fee (per semester): 35.0 ⟵ “Student fee (per semester) | $35.00”
  - column:Technology fee (per semester): 370.0 ⟵ “Technology fee (per semester) | $370.00”
  - column:Drug screening (1st semester only): 65.0 ⟵ “Drug screening (1st semester only) | $65.00”
  - column:NCLEX/Fingerprinting/MO Pro (3 semester track - 2nd semester): 275.0 ⟵ “NCLEX/Fingerprinting/MO Pro (3 semester track - 2nd semester) | $275.00”
  - column:(4 semester track - 3rd semester): 275.0 ⟵ “(4 semester track - 3rd semester) | $275.00”
  - column:Student professional liability insurance (3 semester track -1st semester): 25.0 ⟵ “Student professional liability insurance (3 semester track -1st semester) | $25.00”
### `73aaa091ef456cba` Bolivar Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bolivarcollege.edu/wp-content/uploads/2026/07/Professional-Nursing-Tuition-2026-2027.pdf (sha256 0099621cea07)
- issues: conflicting_sources:https://www.bolivarcollege.edu/wp-content/uploads/2026/07/Practical-Nursing-Tuition-2026-2027.pdf
- checks: {"columns": 1, "rows": 8}
  - column:Clinical tuition (per semester): 1935.0 ⟵ “Clinical tuition (per semester) | $1,935.00”
  - column:Simulation & skills center fee (per semester): 500.0 ⟵ “Simulation & skills center fee (per semester) | $ 500.00”
  - column:Science lab fee (per gen ed. science class, per semester): 140.0 ⟵ “Science lab fee (per gen ed. science class, per semester) | $ 140.00”
  - column:Technology fee (per semester): 370.0 ⟵ “Technology fee (per semester) | $ 370.00”
  - column:Student fee (per semester): 35.0 ⟵ “Student fee (per semester) | $ 35.00”
  - column:Drug screening (1st semester only): 65.0 ⟵ “Drug screening (1st semester only) | $ 65.00”
  - column:NCLEX/Fingerprinting/MO Pro (3rd semester only): 275.0 ⟵ “NCLEX/Fingerprinting/MO Pro (3rd semester only) | $ 275.00”
  - column:Student professional liability insurance (1st semester only): 50.0 ⟵ “Student professional liability insurance (1st semester only) | $ 50.00”
### `0a127f7a71f499b0` Calvary University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.calvary.edu/tuition-financial-aid/scholarships/ (sha256 4880790f5506)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: The student must maintain at least a 3.8 CGPA and carry 12 or more credit hours per semester. The student must reapply annually. This scholarship may be received for a maximum of eight semesters. ⟵ “Renewal Criteria | The student must maintain at least a 3.8 CGPA and carry 12 or more credit hours per semester. The student must reapply annually. This scholarship may be received for a maximum of eight semesters.”
### `0ad9f1445a7b6fdc` Calvary University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.calvary.edu/tuition-financial-aid/scholarships/ (sha256 4880790f5506)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: Less than 24 college credit hours: Minimum ACT composite score of 28 (or SAT combined score of 1300) and a minimum post-secondary cumulative GPA of 4.0. More than 24 college credit hours: Minimum post-secondary cumulative GPA of 3.8. ⟵ “Transfer Student Selection Criteria | Less than 24 college credit hours: Minimum ACT composite score of 28 (or SAT combined score of 1300) and a minimum post-secondary cumulative GPA of 4.0. More than 24 college credit hours: Minimum post-secondary cumulative GPA of 3.8.”
### `15e3e88eda61d206` Calvary University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.calvary.edu/tuition-financial-aid/scholarships/ (sha256 4880790f5506)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1400 per semester. ⟵ “Value | $1400 per semester.”
### `c51147fa61ec0143` Calvary University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.calvary.edu/tuition-financial-aid/scholarships/ (sha256 4880790f5506)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: The student must be an in-person student (or online student attending live-streamed classes concurrently) and must complete an in-person Internship/Practicum through Abundant Life Counseling Center. ⟵ “Selection Criteria | The student must be an in-person student (or online student attending live-streamed classes concurrently) and must complete an in-person Internship/Practicum through Abundant Life Counseling Center.”
### `dc480eb6bc73451d` Calvary University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.calvary.edu/tuition-financial-aid/scholarships/ (sha256 4880790f5506)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: Any undergraduate degree-seeking program. ⟵ “Area of Study | Any undergraduate degree-seeking program.”
### `de465617fb882c9c` Calvary University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.calvary.edu/tuition-financial-aid/scholarships/ (sha256 4880790f5506)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: First-time students: Minimum ACT composite score of 28 (or SAT combined score of 1300) and a minimum high school cumulative GPA of 4.0. ⟵ “First Time Student Selection Criteria | First-time students: Minimum ACT composite score of 28 (or SAT combined score of 1300) and a minimum high school cumulative GPA of 4.0.”
### `b5d9e35baaa39b32` Central Methodist University-College of Graduate and Extended Studies — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/faqs.html (sha256 cd290fbf23fc)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Yes, if a student and/or family has unusual circumstances such as involuntary loss of employment, death of a parent and/or spouse, unusually high medical and/or dental expenses, divorce or separation, or other unexpected event that changes a student's financial situation.”
### `c454454eea7c5377` Central Methodist University-College of Graduate and Extended Studies — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/faqs.html (sha256 cd290fbf23fc)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “A professional judgment determination will be made within 30 days after the submission of the required paperwork.”
### `2027bcb0777cb273` Central Methodist University-College of Graduate and Extended Studies — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,000 ⟵ “Eagle Scholarship | <2.5 GPA and <22 ACT (committee approval required for admission) | $8,000”
  - eligibility_summary: <2.5 GPA and <22 ACT (committee approval required for admission) ⟵ “Eagle Scholarship | <2.5 GPA and <22 ACT (committee approval required for admission) | $8,000”
### `274a43139f07a0fc` Central Methodist University-College of Graduate and Extended Studies — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $16,000 ⟵ “President's Scholarship | 3.9 GPA or 29 ACT | $16,000”
  - eligibility_summary: 3.9 GPA or 29 ACT ⟵ “President's Scholarship | 3.9 GPA or 29 ACT | $16,000”
### `322ccb8f349dc5a0` Central Methodist University-College of Graduate and Extended Studies — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “University Scholarship | 3.5 GPA or 27 ACT | $14,000”
  - eligibility_summary: 3.5 GPA or 27 ACT ⟵ “University Scholarship | 3.5 GPA or 27 ACT | $14,000”
### `50571aade6e2fa16` Central Methodist University-College of Graduate and Extended Studies — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $9,000 ⟵ “Dean's Scholarship | 2.5-2.74 GPA and 21 ACT OR 2.5 GPA and Committee Approval | $9,000”
  - eligibility_summary: 2.5-2.74 GPA and 21 ACT OR 2.5 GPA and Committee Approval ⟵ “Dean's Scholarship | 2.5-2.74 GPA and 21 ACT OR 2.5 GPA and Committee Approval | $9,000”
### `625d65872df34b93` Central Methodist University-College of Graduate and Extended Studies — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $11,000 ⟵ “Alumni Scholarship | 2.75 GPA or 22 ACT | $11,000”
  - eligibility_summary: 2.75 GPA or 22 ACT ⟵ “Alumni Scholarship | 2.75 GPA or 22 ACT | $11,000”
### `631dd565b87eafa9` Central Methodist University-College of Graduate and Extended Studies — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $12,000 ⟵ “Trustee's Scholarship | 3.0 GPA or 24 ACT | $12,000”
  - eligibility_summary: 3.0 GPA or 24 ACT ⟵ “Trustee's Scholarship | 3.0 GPA or 24 ACT | $12,000”
### `07ddee637455627d` Central Methodist University-College of Graduate and Extended Studies — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.centralmethodist.edu/admissions/financial-aid/_docs/CGES-Financial-Planning-Guide---cges-24-25.pdf (sha256 8f7fcd7dd270)
- issues: arrangement_unlabeled, stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://centralmethodist.edu/admissions/business-office/tuition-and-fees/index.html
- checks: {"columns": 3, "rows": 24}
  - column:Undergraduate – Online: 275 ⟵ “Undergraduate – Online | $275”
  - column:Accelerated Nursing Program - Columbia: 540 ⟵ “Accelerated Nursing Program - Columbia | $540”
  - column:Undergraduate On-Site: 290 ⟵ “Undergraduate On-Site | $290”
  - column:Hybrid Undergraduate Courses: 275 ⟵ “Hybrid Undergraduate Courses | $275”
  - column:CGES Student Financial Planning Guide: 3 ⟵ “CGES Student Financial Planning Guide | 3”
  - column:Hybrid Graduate Courses: 290 ⟵ “Hybrid Graduate Courses | $290”
  - column:Graduate Tuition - Online: 275 ⟵ “Graduate Tuition - Online | $275”
  - column:Masters of Clinical Counseling: 400 ⟵ “Masters of Clinical Counseling | $400”
  - column:Masters of Education - On-site: 275 ⟵ “Masters of Education - On-site | $275”
  - column:Masters of Education - St. Louis: 275 ⟵ “Masters of Education - St. Louis | $275”
  - column:Masters of Education Mathematics Courses: 390 ⟵ “Masters of Education Mathematics Courses | $390”
  - column:Masters of Nursing: 400 ⟵ “Masters of Nursing | $400”
  - column:Masters of Mathematics: 390 ⟵ “Masters of Mathematics | $390”
  - column:Graduate Tuition - VESI Courses: 290 ⟵ “Graduate Tuition - VESI Courses | $290”
  - column:Foliotek Fee: 120 ⟵ “Foliotek Fee | $120”
  - column:Re-issued Refund Checks: 30 ⟵ “Re-issued Refund Checks | $30”
  - column:Returned Check Fee: 30 ⟵ “Returned Check Fee | $30”
  - column:CGES Student Financial Planning Guide (2): 5 ⟵ “CGES Student Financial Planning Guide | 5”
  - column:CGES Student Financial Planning Guide (3): 7 ⟵ “CGES Student Financial Planning Guide | 7”
  - column:CGES Student Financial Planning Guide (4): 9 ⟵ “CGES Student Financial Planning Guide | 9”
  - column:CGES Student Financial Planning Guide (5): 11 ⟵ “CGES Student Financial Planning Guide | 11”
  - column:CGES Student Financial Planning Guide (6): 13 ⟵ “CGES Student Financial Planning Guide | 13”
  - column:CGES Student Financial Planning Guide (7): 15 ⟵ “CGES Student Financial Planning Guide | 15”
  - column:CGES Student Financial Planning Guide (8): 17 ⟵ “CGES Student Financial Planning Guide | 17”
  - column:May 25: 6 ⟵ “May 25 | None | 6 | June - Nov. | $55”
  - … 31 more rows
### `24d29114fdb11ed4` Central Methodist University-College of Graduate and Extended Studies — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://centralmethodist.edu/admissions/business-office/tuition-and-fees/index.html (sha256 05109df706c6)
- issues: components_do_not_reconcile, stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.centralmethodist.edu/admissions/financial-aid/_docs/CGES-Financial-Planning-Guide---cges-24-25.pdf
- checks: {"columns": 1, "components_reconcile": false, "rows": 28}
  - column:Tuition (12-18 hours per semester): 28670 ⟵ “Tuition (12-18 hours per semester) | $28,670 | $29,530”
  - column:Average Room and Board: 9790 ⟵ “Average Room and Board | $9,790 | $10,080”
  - column:Fees: 790 ⟵ “Fees | $790 | $790”
  - column:Total Average Annual Direct Costs: 39250 ⟵ “Total Average Annual Direct Costs | $39,250 | $40,400”
  - column:Average Book and Supply cost (estimated): 1000 ⟵ “Average Book and Supply cost (estimated) | $1,000 | $1,000”
  - column:Full-time tuition (12-18 hours): 14335 ⟵ “Full-time tuition (12-18 hours) | $14,335 | $14,765”
  - column:Overload tuition (for each hour over 18): 240 ⟵ “Overload tuition (for each hour over 18) | $240 | $250”
  - column:Residence Hall*: 2395 ⟵ “Residence Hall* | $2,395 | $2,465”
  - column:Meal Plan (per semester)^: 2500 ⟵ “Meal Plan (per semester)^ | $2,500 | $2,575”
  - column:Sports Medicine/Athletic Training Fee: 125 ⟵ “Sports Medicine/Athletic Training Fee | $125 | $125”
  - column:Liability Insurance for Clinical Rotations (yearly): 40 ⟵ “Liability Insurance for Clinical Rotations (yearly) | $40 | $40”
  - column:Acceptance Fee (non-refundable): 250 ⟵ “Acceptance Fee (non-refundable) | $250 | $250”
  - column:Credit by Examination: 35 ⟵ “Credit by Examination | $35 | $35”
  - column:Duplicate Diploma: 25 ⟵ “Duplicate Diploma | $25 | $25”
  - column:Education Majors Background Check**: 15.55 ⟵ “Education Majors Background Check** | $15.55 | $15.55”
  - column:ID Card Replacement: 10 ⟵ “ID Card Replacement | $10 | $10”
  - column:Overload Fee (more than 18 hours): 240 ⟵ “Overload Fee (more than 18 hours) | $240 | $250”
  - column:Boot Fee: 25 ⟵ “Boot Fee | $25 | $25”
  - column:Private Music Lessons (per lesson, max $250): 125 ⟵ “Private Music Lessons (per lesson, max $250) | $125 | $125”
  - column:Re-Core & Replace Keys: 75 ⟵ “Re-Core & Replace Keys | $75 | $100”
  - column:Re-issued Payroll or Refund Check**: 30 ⟵ “Re-issued Payroll or Refund Check** | $30 | $30”
  - column:Returned Check: 30 ⟵ “Returned Check | $30 | $30”
  - column:Single Room Charge (per semester): 500 ⟵ “Single Room Charge (per semester) | $500 | $750”
  - column:Sports Medicine/Athletic Training Physical (per semester): 125 ⟵ “Sports Medicine/Athletic Training Physical (per semester) | $125 | $125”
  - column:Substitute Certificate with Background Check (for Student Teaching): 91.75 ⟵ “Substitute Certificate with Background Check (for Student Teaching) | $91.75 | $93.50”
  - … 3 more rows
### `365110946fe4c063` Central Methodist University-College of Graduate and Extended Studies — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.centralmethodist.edu/admissions/financial-aid/cost-of-attendance.html (sha256 35633aa1e925)
- issues: arrangement_unlabeled, cost_period_semester, shared_site_attribution_review, conflicting_sources:https://centralmethodist.edu/admissions/business-office/tuition-and-fees/index.html
- checks: {"columns": 6, "rows": 6}
  - on_campus:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - on_campus:Room and Board: 5040 ⟵ “Room and Board | $5,040 | $5,040 | $4,637 | $4,637 | $1,138 | $1,138”
  - on_campus:Books: 500 ⟵ “Books | $500 | $500 | $500 | $500 | $500 | $500”
  - on_campus:Personal: 3209 ⟵ “Personal | $3,209 | $3,209 | $3,209 | $3,209 | $3,209 | $3,209”
  - on_campus:Transportation: 979 ⟵ “Transportation | $979 | $979 | $979 | $979 | $979 | $979”
  - on_campus:Loan Fees: 40 ⟵ “Loan Fees | $40 | $65 | $40 | $65 | $40 | $65”
  - off_campus_not_with_family:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - off_campus_not_with_family:Room and Board: 5040 ⟵ “Room and Board | $5,040 | $5,040 | $4,637 | $4,637 | $1,138 | $1,138”
  - off_campus_not_with_family:Books: 500 ⟵ “Books | $500 | $500 | $500 | $500 | $500 | $500”
  - off_campus_not_with_family:Personal: 3209 ⟵ “Personal | $3,209 | $3,209 | $3,209 | $3,209 | $3,209 | $3,209”
  - off_campus_not_with_family:Transportation: 979 ⟵ “Transportation | $979 | $979 | $979 | $979 | $979 | $979”
  - off_campus_not_with_family:Loan Fees: 65 ⟵ “Loan Fees | $40 | $65 | $40 | $65 | $40 | $65”
  - with_parents_or_family:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - with_parents_or_family:Room and Board: 4637 ⟵ “Room and Board | $5,040 | $5,040 | $4,637 | $4,637 | $1,138 | $1,138”
  - with_parents_or_family:Books: 500 ⟵ “Books | $500 | $500 | $500 | $500 | $500 | $500”
  - with_parents_or_family:Personal: 3209 ⟵ “Personal | $3,209 | $3,209 | $3,209 | $3,209 | $3,209 | $3,209”
  - with_parents_or_family:Transportation: 979 ⟵ “Transportation | $979 | $979 | $979 | $979 | $979 | $979”
  - with_parents_or_family:Loan Fees: 40 ⟵ “Loan Fees | $40 | $65 | $40 | $65 | $40 | $65”
  - column:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - column:Room and Board: 4637 ⟵ “Room and Board | $5,040 | $5,040 | $4,637 | $4,637 | $1,138 | $1,138”
  - column:Books: 500 ⟵ “Books | $500 | $500 | $500 | $500 | $500 | $500”
  - column:Personal: 3209 ⟵ “Personal | $3,209 | $3,209 | $3,209 | $3,209 | $3,209 | $3,209”
  - column:Transportation: 979 ⟵ “Transportation | $979 | $979 | $979 | $979 | $979 | $979”
  - column:Loan Fees: 65 ⟵ “Loan Fees | $40 | $65 | $40 | $65 | $40 | $65”
  - column:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - … 11 more rows
### `e2d2416b6ff6818e` Central Methodist University-College of Graduate and Extended Studies — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://centralmethodist.edu/admissions/business-office/tuition-and-fees/index.html (sha256 05109df706c6)
- issues: components_do_not_reconcile, shared_site_attribution_review, conflicting_sources:https://www.centralmethodist.edu/admissions/financial-aid/cost-of-attendance.html
- checks: {"columns": 1, "components_reconcile": false, "rows": 28}
  - column:Tuition (12-18 hours per semester): 29530 ⟵ “Tuition (12-18 hours per semester) | $28,670 | $29,530”
  - column:Average Room and Board: 10080 ⟵ “Average Room and Board | $9,790 | $10,080”
  - column:Fees: 790 ⟵ “Fees | $790 | $790”
  - column:Total Average Annual Direct Costs: 40400 ⟵ “Total Average Annual Direct Costs | $39,250 | $40,400”
  - column:Average Book and Supply cost (estimated): 1000 ⟵ “Average Book and Supply cost (estimated) | $1,000 | $1,000”
  - column:Full-time tuition (12-18 hours): 14765 ⟵ “Full-time tuition (12-18 hours) | $14,335 | $14,765”
  - column:Overload tuition (for each hour over 18): 250 ⟵ “Overload tuition (for each hour over 18) | $240 | $250”
  - column:Residence Hall*: 2465 ⟵ “Residence Hall* | $2,395 | $2,465”
  - column:Meal Plan (per semester)^: 2575 ⟵ “Meal Plan (per semester)^ | $2,500 | $2,575”
  - column:Sports Medicine/Athletic Training Fee: 125 ⟵ “Sports Medicine/Athletic Training Fee | $125 | $125”
  - column:Liability Insurance for Clinical Rotations (yearly): 40 ⟵ “Liability Insurance for Clinical Rotations (yearly) | $40 | $40”
  - column:Acceptance Fee (non-refundable): 250 ⟵ “Acceptance Fee (non-refundable) | $250 | $250”
  - column:Credit by Examination: 35 ⟵ “Credit by Examination | $35 | $35”
  - column:Duplicate Diploma: 25 ⟵ “Duplicate Diploma | $25 | $25”
  - column:Education Majors Background Check**: 15.55 ⟵ “Education Majors Background Check** | $15.55 | $15.55”
  - column:ID Card Replacement: 10 ⟵ “ID Card Replacement | $10 | $10”
  - column:Overload Fee (more than 18 hours): 250 ⟵ “Overload Fee (more than 18 hours) | $240 | $250”
  - column:Boot Fee: 25 ⟵ “Boot Fee | $25 | $25”
  - column:Private Music Lessons (per lesson, max $250): 125 ⟵ “Private Music Lessons (per lesson, max $250) | $125 | $125”
  - column:Re-Core & Replace Keys: 100 ⟵ “Re-Core & Replace Keys | $75 | $100”
  - column:Re-issued Payroll or Refund Check**: 30 ⟵ “Re-issued Payroll or Refund Check** | $30 | $30”
  - column:Returned Check: 30 ⟵ “Returned Check | $30 | $30”
  - column:Single Room Charge (per semester): 750 ⟵ “Single Room Charge (per semester) | $500 | $750”
  - column:Sports Medicine/Athletic Training Physical (per semester): 125 ⟵ “Sports Medicine/Athletic Training Physical (per semester) | $125 | $125”
  - column:Substitute Certificate with Background Check (for Student Teaching): 93.5 ⟵ “Substitute Certificate with Background Check (for Student Teaching) | $91.75 | $93.50”
  - … 3 more rows
### `m8c317289648a528` Central Methodist University-College of Graduate and Extended Studies — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://centralmethodist.edu/academics/dual-credit/faqs-first-class.html (sha256 2db7642bc297)
- issues: shared_site_attribution_review
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 0}
  - per_credit_hour_charge: 80 ⟵ “Dual credit class tuition is $80 per credit hour for In-Seat and Zoom. Online tuition is $100 per credit hour. Once a student is enrolled, they will receive a statement monthly until their balance is at $0. Payment can be sent in before the tuition amount appears on the student’s account. It will sh”
  - per_credit_hour_charge: 100 ⟵ “Dual credit class tuition is $80 per credit hour for In-Seat and Zoom. Online tuition is $100 per credit hour. Once a student is enrolled, they will receive a statement monthly until their balance is at $0. Payment can be sent in before the tuition amount appears on the student’s account. It will sh”
  - per_credit_hour_charge: 80 ⟵ “In-seat and ZOOM classes are all $80 per credit hour.”
  - per_credit_hour_charge: 100 ⟵ “Online tuition is $100 per credit hour.”
### `mda917d95b0f0fdb` Central Methodist University-College of Graduate and Extended Studies — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://centralmethodist.edu/academics/registrar/_docs/transferdocs/sfcc/202408-SFCC_CMU_Articulation_Agreementfinal.pdf (sha256 2184038f0a69)
- issues: shared_site_attribution_review
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 5}
  - residency_requirement_credits: 30 ⟵ “Electives (To Complete Min. 120 Hours) BIO206 Microbiology w/Lab 4 BIO305 Microbiology w/Lab 4 Total # Total 152 3 Exercise Science & Athletic Training Program Requirement Candidates for a baccalaureate degree must complete at least 30 of the last 36 hours of credit in residence at Central Methodist University.”
  - residency_requirement_credits: 30 ⟵ “Candidates for a baccalaureate degree must complete at least 30 of the last 36 hours of credit in residence at Central Methodist University.”
  - residency_requirement_credits: 30 ⟵ “Candidates for a baccalaureate degree must complete at least 30 of the last 36 hours of credit in residence at Central Methodist University.”
  - residency_requirement_credits: 30 ⟵ “All students must have 30 hours of 300-level course work from a four-year institution, and 30 of the last 36 hours must be from CMU.”
  - residency_requirement_credits: 30 ⟵ “All students must have 30 hours of 300-level course work from a four-year institution, and 30 of the last 36 hours must be from CMU.”
### `5254ae7de53f5118` Central Methodist University-College of Liberal Arts and Sciences — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/faqs.html (sha256 cd290fbf23fc)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Yes, if a student and/or family has unusual circumstances such as involuntary loss of employment, death of a parent and/or spouse, unusually high medical and/or dental expenses, divorce or separation, or other unexpected event that changes a student's financial situation.”
### `7209ae7517fbb9ca` Central Methodist University-College of Liberal Arts and Sciences — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/faqs.html (sha256 cd290fbf23fc)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “A professional judgment determination will be made within 30 days after the submission of the required paperwork.”
### `1b855ff169a6d6ad` Central Methodist University-College of Liberal Arts and Sciences — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $9,000 ⟵ “Dean's Scholarship | 2.5-2.74 GPA and 21 ACT OR 2.5 GPA and Committee Approval | $9,000”
  - eligibility_summary: 2.5-2.74 GPA and 21 ACT OR 2.5 GPA and Committee Approval ⟵ “Dean's Scholarship | 2.5-2.74 GPA and 21 ACT OR 2.5 GPA and Committee Approval | $9,000”
### `2d96f778de321e69` Central Methodist University-College of Liberal Arts and Sciences — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $12,000 ⟵ “Trustee's Scholarship | 3.0 GPA or 24 ACT | $12,000”
  - eligibility_summary: 3.0 GPA or 24 ACT ⟵ “Trustee's Scholarship | 3.0 GPA or 24 ACT | $12,000”
### `4bd4987b2b9c285e` Central Methodist University-College of Liberal Arts and Sciences — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,000 ⟵ “Eagle Scholarship | <2.5 GPA and <22 ACT (committee approval required for admission) | $8,000”
  - eligibility_summary: <2.5 GPA and <22 ACT (committee approval required for admission) ⟵ “Eagle Scholarship | <2.5 GPA and <22 ACT (committee approval required for admission) | $8,000”
### `a16902d5b8aaf498` Central Methodist University-College of Liberal Arts and Sciences — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $11,000 ⟵ “Alumni Scholarship | 2.75 GPA or 22 ACT | $11,000”
  - eligibility_summary: 2.75 GPA or 22 ACT ⟵ “Alumni Scholarship | 2.75 GPA or 22 ACT | $11,000”
### `b090a13d52f08b13` Central Methodist University-College of Liberal Arts and Sciences — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “University Scholarship | 3.5 GPA or 27 ACT | $14,000”
  - eligibility_summary: 3.5 GPA or 27 ACT ⟵ “University Scholarship | 3.5 GPA or 27 ACT | $14,000”
### `dd79932b559e985d` Central Methodist University-College of Liberal Arts and Sciences — awards 2026-27 [new] (source_unlabeled)
- source: https://www.centralmethodist.edu/admissions/financial-aid/scholarships.html (sha256 d752ae26bc73)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $16,000 ⟵ “President's Scholarship | 3.9 GPA or 29 ACT | $16,000”
  - eligibility_summary: 3.9 GPA or 29 ACT ⟵ “President's Scholarship | 3.9 GPA or 29 ACT | $16,000”
### `07af20049bd7701d` Central Methodist University-College of Liberal Arts and Sciences — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://centralmethodist.edu/admissions/business-office/tuition-and-fees/index.html (sha256 05109df706c6)
- issues: components_do_not_reconcile, shared_site_attribution_review, conflicting_sources:https://www.centralmethodist.edu/admissions/financial-aid/cost-of-attendance.html
- checks: {"columns": 1, "components_reconcile": false, "rows": 28}
  - column:Tuition (12-18 hours per semester): 29530 ⟵ “Tuition (12-18 hours per semester) | $28,670 | $29,530”
  - column:Average Room and Board: 10080 ⟵ “Average Room and Board | $9,790 | $10,080”
  - column:Fees: 790 ⟵ “Fees | $790 | $790”
  - column:Total Average Annual Direct Costs: 40400 ⟵ “Total Average Annual Direct Costs | $39,250 | $40,400”
  - column:Average Book and Supply cost (estimated): 1000 ⟵ “Average Book and Supply cost (estimated) | $1,000 | $1,000”
  - column:Full-time tuition (12-18 hours): 14765 ⟵ “Full-time tuition (12-18 hours) | $14,335 | $14,765”
  - column:Overload tuition (for each hour over 18): 250 ⟵ “Overload tuition (for each hour over 18) | $240 | $250”
  - column:Residence Hall*: 2465 ⟵ “Residence Hall* | $2,395 | $2,465”
  - column:Meal Plan (per semester)^: 2575 ⟵ “Meal Plan (per semester)^ | $2,500 | $2,575”
  - column:Sports Medicine/Athletic Training Fee: 125 ⟵ “Sports Medicine/Athletic Training Fee | $125 | $125”
  - column:Liability Insurance for Clinical Rotations (yearly): 40 ⟵ “Liability Insurance for Clinical Rotations (yearly) | $40 | $40”
  - column:Acceptance Fee (non-refundable): 250 ⟵ “Acceptance Fee (non-refundable) | $250 | $250”
  - column:Credit by Examination: 35 ⟵ “Credit by Examination | $35 | $35”
  - column:Duplicate Diploma: 25 ⟵ “Duplicate Diploma | $25 | $25”
  - column:Education Majors Background Check**: 15.55 ⟵ “Education Majors Background Check** | $15.55 | $15.55”
  - column:ID Card Replacement: 10 ⟵ “ID Card Replacement | $10 | $10”
  - column:Overload Fee (more than 18 hours): 250 ⟵ “Overload Fee (more than 18 hours) | $240 | $250”
  - column:Boot Fee: 25 ⟵ “Boot Fee | $25 | $25”
  - column:Private Music Lessons (per lesson, max $250): 125 ⟵ “Private Music Lessons (per lesson, max $250) | $125 | $125”
  - column:Re-Core & Replace Keys: 100 ⟵ “Re-Core & Replace Keys | $75 | $100”
  - column:Re-issued Payroll or Refund Check**: 30 ⟵ “Re-issued Payroll or Refund Check** | $30 | $30”
  - column:Returned Check: 30 ⟵ “Returned Check | $30 | $30”
  - column:Single Room Charge (per semester): 750 ⟵ “Single Room Charge (per semester) | $500 | $750”
  - column:Sports Medicine/Athletic Training Physical (per semester): 125 ⟵ “Sports Medicine/Athletic Training Physical (per semester) | $125 | $125”
  - column:Substitute Certificate with Background Check (for Student Teaching): 93.5 ⟵ “Substitute Certificate with Background Check (for Student Teaching) | $91.75 | $93.50”
  - … 3 more rows
### `27f4eb983cf01026` Central Methodist University-College of Liberal Arts and Sciences — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://centralmethodist.edu/admissions/business-office/tuition-and-fees/index.html (sha256 05109df706c6)
- issues: components_do_not_reconcile, stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://www.centralmethodist.edu/admissions/financial-aid/_docs/CGES-Financial-Planning-Guide---cges-24-25.pdf
- checks: {"columns": 1, "components_reconcile": false, "rows": 28}
  - column:Tuition (12-18 hours per semester): 28670 ⟵ “Tuition (12-18 hours per semester) | $28,670 | $29,530”
  - column:Average Room and Board: 9790 ⟵ “Average Room and Board | $9,790 | $10,080”
  - column:Fees: 790 ⟵ “Fees | $790 | $790”
  - column:Total Average Annual Direct Costs: 39250 ⟵ “Total Average Annual Direct Costs | $39,250 | $40,400”
  - column:Average Book and Supply cost (estimated): 1000 ⟵ “Average Book and Supply cost (estimated) | $1,000 | $1,000”
  - column:Full-time tuition (12-18 hours): 14335 ⟵ “Full-time tuition (12-18 hours) | $14,335 | $14,765”
  - column:Overload tuition (for each hour over 18): 240 ⟵ “Overload tuition (for each hour over 18) | $240 | $250”
  - column:Residence Hall*: 2395 ⟵ “Residence Hall* | $2,395 | $2,465”
  - column:Meal Plan (per semester)^: 2500 ⟵ “Meal Plan (per semester)^ | $2,500 | $2,575”
  - column:Sports Medicine/Athletic Training Fee: 125 ⟵ “Sports Medicine/Athletic Training Fee | $125 | $125”
  - column:Liability Insurance for Clinical Rotations (yearly): 40 ⟵ “Liability Insurance for Clinical Rotations (yearly) | $40 | $40”
  - column:Acceptance Fee (non-refundable): 250 ⟵ “Acceptance Fee (non-refundable) | $250 | $250”
  - column:Credit by Examination: 35 ⟵ “Credit by Examination | $35 | $35”
  - column:Duplicate Diploma: 25 ⟵ “Duplicate Diploma | $25 | $25”
  - column:Education Majors Background Check**: 15.55 ⟵ “Education Majors Background Check** | $15.55 | $15.55”
  - column:ID Card Replacement: 10 ⟵ “ID Card Replacement | $10 | $10”
  - column:Overload Fee (more than 18 hours): 240 ⟵ “Overload Fee (more than 18 hours) | $240 | $250”
  - column:Boot Fee: 25 ⟵ “Boot Fee | $25 | $25”
  - column:Private Music Lessons (per lesson, max $250): 125 ⟵ “Private Music Lessons (per lesson, max $250) | $125 | $125”
  - column:Re-Core & Replace Keys: 75 ⟵ “Re-Core & Replace Keys | $75 | $100”
  - column:Re-issued Payroll or Refund Check**: 30 ⟵ “Re-issued Payroll or Refund Check** | $30 | $30”
  - column:Returned Check: 30 ⟵ “Returned Check | $30 | $30”
  - column:Single Room Charge (per semester): 500 ⟵ “Single Room Charge (per semester) | $500 | $750”
  - column:Sports Medicine/Athletic Training Physical (per semester): 125 ⟵ “Sports Medicine/Athletic Training Physical (per semester) | $125 | $125”
  - column:Substitute Certificate with Background Check (for Student Teaching): 91.75 ⟵ “Substitute Certificate with Background Check (for Student Teaching) | $91.75 | $93.50”
  - … 3 more rows
### `e92d78952bf5797d` Central Methodist University-College of Liberal Arts and Sciences — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.centralmethodist.edu/admissions/financial-aid/cost-of-attendance.html (sha256 35633aa1e925)
- issues: arrangement_unlabeled, cost_period_semester, shared_site_attribution_review, conflicting_sources:https://centralmethodist.edu/admissions/business-office/tuition-and-fees/index.html
- checks: {"columns": 6, "rows": 6}
  - on_campus:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - on_campus:Room and Board: 5040 ⟵ “Room and Board | $5,040 | $5,040 | $4,637 | $4,637 | $1,138 | $1,138”
  - on_campus:Books: 500 ⟵ “Books | $500 | $500 | $500 | $500 | $500 | $500”
  - on_campus:Personal: 3209 ⟵ “Personal | $3,209 | $3,209 | $3,209 | $3,209 | $3,209 | $3,209”
  - on_campus:Transportation: 979 ⟵ “Transportation | $979 | $979 | $979 | $979 | $979 | $979”
  - on_campus:Loan Fees: 40 ⟵ “Loan Fees | $40 | $65 | $40 | $65 | $40 | $65”
  - off_campus_not_with_family:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - off_campus_not_with_family:Room and Board: 5040 ⟵ “Room and Board | $5,040 | $5,040 | $4,637 | $4,637 | $1,138 | $1,138”
  - off_campus_not_with_family:Books: 500 ⟵ “Books | $500 | $500 | $500 | $500 | $500 | $500”
  - off_campus_not_with_family:Personal: 3209 ⟵ “Personal | $3,209 | $3,209 | $3,209 | $3,209 | $3,209 | $3,209”
  - off_campus_not_with_family:Transportation: 979 ⟵ “Transportation | $979 | $979 | $979 | $979 | $979 | $979”
  - off_campus_not_with_family:Loan Fees: 65 ⟵ “Loan Fees | $40 | $65 | $40 | $65 | $40 | $65”
  - with_parents_or_family:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - with_parents_or_family:Room and Board: 4637 ⟵ “Room and Board | $5,040 | $5,040 | $4,637 | $4,637 | $1,138 | $1,138”
  - with_parents_or_family:Books: 500 ⟵ “Books | $500 | $500 | $500 | $500 | $500 | $500”
  - with_parents_or_family:Personal: 3209 ⟵ “Personal | $3,209 | $3,209 | $3,209 | $3,209 | $3,209 | $3,209”
  - with_parents_or_family:Transportation: 979 ⟵ “Transportation | $979 | $979 | $979 | $979 | $979 | $979”
  - with_parents_or_family:Loan Fees: 40 ⟵ “Loan Fees | $40 | $65 | $40 | $65 | $40 | $65”
  - column:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - column:Room and Board: 4637 ⟵ “Room and Board | $5,040 | $5,040 | $4,637 | $4,637 | $1,138 | $1,138”
  - column:Books: 500 ⟵ “Books | $500 | $500 | $500 | $500 | $500 | $500”
  - column:Personal: 3209 ⟵ “Personal | $3,209 | $3,209 | $3,209 | $3,209 | $3,209 | $3,209”
  - column:Transportation: 979 ⟵ “Transportation | $979 | $979 | $979 | $979 | $979 | $979”
  - column:Loan Fees: 65 ⟵ “Loan Fees | $40 | $65 | $40 | $65 | $40 | $65”
  - column:Tuition and Fees: 15160 ⟵ “Tuition and Fees | $15,160 | $15,160 | $15,160 | $15,160 | $15,160 | $15,160”
  - … 11 more rows
### `ec3e60d174a9c52c` Central Methodist University-College of Liberal Arts and Sciences — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.centralmethodist.edu/admissions/financial-aid/_docs/CGES-Financial-Planning-Guide---cges-24-25.pdf (sha256 8f7fcd7dd270)
- issues: arrangement_unlabeled, stale_year_label:2025-26, shared_site_attribution_review, conflicting_sources:https://centralmethodist.edu/admissions/business-office/tuition-and-fees/index.html
- checks: {"columns": 3, "rows": 24}
  - column:Undergraduate – Online: 275 ⟵ “Undergraduate – Online | $275”
  - column:Accelerated Nursing Program - Columbia: 540 ⟵ “Accelerated Nursing Program - Columbia | $540”
  - column:Undergraduate On-Site: 290 ⟵ “Undergraduate On-Site | $290”
  - column:Hybrid Undergraduate Courses: 275 ⟵ “Hybrid Undergraduate Courses | $275”
  - column:CGES Student Financial Planning Guide: 3 ⟵ “CGES Student Financial Planning Guide | 3”
  - column:Hybrid Graduate Courses: 290 ⟵ “Hybrid Graduate Courses | $290”
  - column:Graduate Tuition - Online: 275 ⟵ “Graduate Tuition - Online | $275”
  - column:Masters of Clinical Counseling: 400 ⟵ “Masters of Clinical Counseling | $400”
  - column:Masters of Education - On-site: 275 ⟵ “Masters of Education - On-site | $275”
  - column:Masters of Education - St. Louis: 275 ⟵ “Masters of Education - St. Louis | $275”
  - column:Masters of Education Mathematics Courses: 390 ⟵ “Masters of Education Mathematics Courses | $390”
  - column:Masters of Nursing: 400 ⟵ “Masters of Nursing | $400”
  - column:Masters of Mathematics: 390 ⟵ “Masters of Mathematics | $390”
  - column:Graduate Tuition - VESI Courses: 290 ⟵ “Graduate Tuition - VESI Courses | $290”
  - column:Foliotek Fee: 120 ⟵ “Foliotek Fee | $120”
  - column:Re-issued Refund Checks: 30 ⟵ “Re-issued Refund Checks | $30”
  - column:Returned Check Fee: 30 ⟵ “Returned Check Fee | $30”
  - column:CGES Student Financial Planning Guide (2): 5 ⟵ “CGES Student Financial Planning Guide | 5”
  - column:CGES Student Financial Planning Guide (3): 7 ⟵ “CGES Student Financial Planning Guide | 7”
  - column:CGES Student Financial Planning Guide (4): 9 ⟵ “CGES Student Financial Planning Guide | 9”
  - column:CGES Student Financial Planning Guide (5): 11 ⟵ “CGES Student Financial Planning Guide | 11”
  - column:CGES Student Financial Planning Guide (6): 13 ⟵ “CGES Student Financial Planning Guide | 13”
  - column:CGES Student Financial Planning Guide (7): 15 ⟵ “CGES Student Financial Planning Guide | 15”
  - column:CGES Student Financial Planning Guide (8): 17 ⟵ “CGES Student Financial Planning Guide | 17”
  - column:May 25: 6 ⟵ “May 25 | None | 6 | June - Nov. | $55”
  - … 31 more rows
### `m1e0fa3b41edd11d` Central Methodist University-College of Liberal Arts and Sciences — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://centralmethodist.edu/academics/dual-credit/faqs-first-class.html (sha256 2db7642bc297)
- issues: shared_site_attribution_review
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 0}
  - per_credit_hour_charge: 80 ⟵ “Dual credit class tuition is $80 per credit hour for In-Seat and Zoom. Online tuition is $100 per credit hour. Once a student is enrolled, they will receive a statement monthly until their balance is at $0. Payment can be sent in before the tuition amount appears on the student’s account. It will sh”
  - per_credit_hour_charge: 100 ⟵ “Dual credit class tuition is $80 per credit hour for In-Seat and Zoom. Online tuition is $100 per credit hour. Once a student is enrolled, they will receive a statement monthly until their balance is at $0. Payment can be sent in before the tuition amount appears on the student’s account. It will sh”
  - per_credit_hour_charge: 80 ⟵ “In-seat and ZOOM classes are all $80 per credit hour.”
  - per_credit_hour_charge: 100 ⟵ “Online tuition is $100 per credit hour.”
### `m73a1cb891481e00` Central Methodist University-College of Liberal Arts and Sciences — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://centralmethodist.edu/academics/registrar/_docs/transferdocs/sfcc/202408-SFCC_CMU_Articulation_Agreementfinal.pdf (sha256 2184038f0a69)
- issues: shared_site_attribution_review
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 5}
  - residency_requirement_credits: 30 ⟵ “Electives (To Complete Min. 120 Hours) BIO206 Microbiology w/Lab 4 BIO305 Microbiology w/Lab 4 Total # Total 152 3 Exercise Science & Athletic Training Program Requirement Candidates for a baccalaureate degree must complete at least 30 of the last 36 hours of credit in residence at Central Methodist University.”
  - residency_requirement_credits: 30 ⟵ “Candidates for a baccalaureate degree must complete at least 30 of the last 36 hours of credit in residence at Central Methodist University.”
  - residency_requirement_credits: 30 ⟵ “Candidates for a baccalaureate degree must complete at least 30 of the last 36 hours of credit in residence at Central Methodist University.”
  - residency_requirement_credits: 30 ⟵ “All students must have 30 hours of 300-level course work from a four-year institution, and 30 of the last 36 hours must be from CMU.”
  - residency_requirement_credits: 30 ⟵ “All students must have 30 hours of 300-level course work from a four-year institution, and 30 of the last 36 hours must be from CMU.”
### `4a2ae43bc5e66f96` City Vision University — appeals 2017-18 [new] (labeled_in_source)
- source: https://www.cityvision.edu/professional-judgment-policy/ (sha256 b2d119e05983)
- issues: stale_year_label:2017-18, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A personal statement explaining your special circumstances and how you came to support yourself.”
### `580e030081bde9d9` City Vision University — appeals 2017-18 [new] (labeled_in_source)
- source: https://www.cityvision.edu/professional-judgment-policy/ (sha256 b2d119e05983)
- issues: stale_year_label:2017-18, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 15}
  - sentence: professional_judgment ⟵ “All Professional Judgment determinations will be documented and will relate to each student’s special circumstances (not to conditions that may exist for a whole class of students).”
  - sentence: professional_judgment ⟵ “As stated in DCL GEN 16-03, one specific circumstance under which Professional Judgment may be appropriate is when a student’s income information from two years previous is significantly different than the student’s income in more recent years.”
  - sentence: professional_judgment ⟵ “This type of Professional Judgment request has become more common starting with the 2017-18 FAFSA, now that the FAFSA uses income information from two years prior to the aid year.”
  - sentence: professional_judgment ⟵ “However, all Professional Judgment requests will be evaluated on a case-by-case basis, not for students with income variance between two tax years as a general class.”
  - sentence: professional_judgment ⟵ “To apply for Professional Judgment, first contact financialaid@cityvision.edu since Traci Hedlund, Director of Financial Aid, will send the forms to be filled out.”
  - sentence: professional_judgment ⟵ “Circumstances for Professional Judgment The following are the circumstances in which students may apply for Professional Judgment at City Vision University: Unemployment or change in employment which has drastically reduced your income (and/or your spouse’s, if you have a spouse).”
### `6305566eabd6a322` City Vision University — appeals 2017-18 [new] (labeled_in_source)
- source: https://www.cityvision.edu/professional-judgment-policy/ (sha256 b2d119e05983)
- issues: stale_year_label:2017-18, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: dependency_override ⟵ “More details on Dependency Overrides are provided below.”
  - sentence: dependency_override ⟵ “Please fax any documentation to 816-760-2084 Dependency Overrides: Students are considered to be dependent unless they meet at least one of the criteria in listed in the table on this page.”
  - sentence: dependency_override ⟵ “Armed Forces (See link above for full definition) A Dependency Override allows a student to be considered independent for income calculation purposes.”
  - sentence: dependency_override ⟵ “Additionally, you currently live separately from your parents and pay all expenses from your own income and assets Students requiring a Dependency Override must complete the Dependency Override Request form.”
  - sentence: dependency_override ⟵ “All documentation must be provided within 30 days of a Dependency Override request, or the request will not be reviewed.”
  - sentence: dependency_override ⟵ “The Director of Financial Aid will make the final determination in requests for dependency overrides.”
### `a0d75d6cb888208e` City Vision University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cityvision.edu/sap/ (sha256 d64b77f450ac)
- issues: semantic_review_required, conflicting_sources:https://www.cityvision.edu/form/sap-appeal-form/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “A student who is denied Federal aid because of a failure to meet Satisfactory Academic Progress standards after the Warning Term has concluded may appeal this determination to the Academic Administration by completing a Student Appeal Form, located here.”
### `f028b6eadf548f10` City Vision University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cityvision.edu/form/sap-appeal-form/ (sha256 8bfb371946c7)
- issues: semantic_review_required, conflicting_sources:https://www.cityvision.edu/sap/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal Policy and Procedure Federal government regulations permit a student who is not making Satisfactory Academic Progress to submit an appeal if one of the following has affected their academic performance: “the death of a relative, an injury or illness of the student, or other special circumstances” – 34 CFR 668.34(a)(9)(ii).”
  - sentence: sap_appeal ⟵ “Your SAP Appeal will be reviewed by the Academic Oversight staff.”
  - sentence: sap_appeal ⟵ “First Name: Last Name: Email Reason for SAP Appeal Submit City Vision University Transforming lives through radically affordable online education.”
### `01726fb9ece76622` City Vision University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.cityvision.edu/course/recovery-coaching-and-peer-support-specialist/ (sha256 41641a5a3984)
- issues: conflicting_sources:https://www.cityvision.edu/course/addiction-counseling-practicum/,https://www.cityvision.edu/course/group-counseling-practices/,https://www.cityvision.edu/course/prior-learning-assessment/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Davila, R.; Griffin, J.; Gamache, P. and Ballard, M. (2018) Behavioral Health Mentor: A Recovery Coach Model for Peer Recovery Support Specialist CreateSpace Independent Publishing Platform, (1 Edition). 170 pages ISBN: 978-1722915902: 9.95 ⟵ “Davila, R.; Griffin, J.; Gamache, P. and Ballard, M. (2018) Behavioral Health Mentor: A Recovery Coach Model for Peer Recovery Support Specialist CreateSpace Independent Publishing Platform, (1 Edition). 170 pages ISBN: 978-1722915902 | $9.”
  - column:Tuition: 850.0 ⟵ “Tuition | $850.00”
  - column:Total Cost of Course:: 859.95 ⟵ “Total Cost of Course: | $859.95”
### `0ca137c232222054` City Vision University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.cityvision.edu/course/addiction-counseling-practicum/ (sha256 ff12d98c88ba)
- issues: components_do_not_reconcile, conflicting_sources:https://www.cityvision.edu/course/group-counseling-practices/,https://www.cityvision.edu/course/prior-learning-assessment/,https://www.cityvision.edu/course/recovery-coaching-and-peer-support-specialist/
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Faulkner, C. A., & Faulkner, S. (2019). Addictions Counseling: A Competency-Based Approach (Illustrated edition). Oxford University Press.: 50.99 ⟵ “Faulkner, C. A., & Faulkner, S. (2019). Addictions Counseling: A Competency-Based Approach (Illustrated edition). Oxford University Press. | $50.99”
  - column:Students taking this course are required to sign up for Professional Liability Insurance. We recommend that students complete the steps here to do this: Instructions to Sign up for NAADAC Student Membership and Insurance at an estimated total cost of $100.: 100 ⟵ “Students taking this course are required to sign up for Professional Liability Insurance. We recommend that students complete the steps here to do this: Instructions to Sign up for NAADAC Student Membership and Insurance at an estimated tot”
  - column:Tuition Cost: 850.0 ⟵ “Tuition Cost | $850.00”
  - column:Total Cost of Course:: 1000.99 ⟵ “Total Cost of Course: | $1000.99”
### `d3ee04c36c4e5975` City Vision University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.cityvision.edu/course/group-counseling-practices/ (sha256 9fa99b529b32)
- issues: conflicting_sources:https://www.cityvision.edu/course/addiction-counseling-practicum/,https://www.cityvision.edu/course/prior-learning-assessment/,https://www.cityvision.edu/course/recovery-coaching-and-peer-support-specialist/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Terence T. Gorski., (2016) Problem-Solving Group Therapy: A Group Leader’s Guide for Developing and Implementing Group Treatment Plans, BookBaby; 1 edition. (Kindle version) ISBN: 9781483590448.: 7.99 ⟵ “Terence T. Gorski., (2016) Problem-Solving Group Therapy: A Group Leader’s Guide for Developing and Implementing Group Treatment Plans, BookBaby; 1 edition. (Kindle version) ISBN: 9781483590448. | $7.99”
  - column:Tuition: 850.0 ⟵ “Tuition | $850.00”
  - column:Total Cost of Course:: 857.99 ⟵ “Total Cost of Course: | $857.99”
### `f84e575f7e0ef99f` City Vision University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.cityvision.edu/course/prior-learning-assessment/ (sha256 22d91e5337a0)
- issues: conflicting_sources:https://www.cityvision.edu/course/addiction-counseling-practicum/,https://www.cityvision.edu/course/group-counseling-practices/,https://www.cityvision.edu/course/recovery-coaching-and-peer-support-specialist/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Council for Adult and Experiential Learning (2015). Earn College Credit for What You Know (5 edition.). Chicago; Dubuque, Iowa: Kendall Hunt Publishing. ISBN: 978-0757596919. 232 pages.: 15.7 ⟵ “Council for Adult and Experiential Learning (2015). Earn College Credit for What You Know (5 edition.). Chicago; Dubuque, Iowa: Kendall Hunt Publishing. ISBN: 978-0757596919. 232 pages. | $15.70”
  - column:Tuition: 850.0 ⟵ “Tuition | $850.00”
  - column:Total Cost of Course: 865.7 ⟵ “Total Cost of Course | $865.70”
### `72de04df44ccecca` College of the Ozarks — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cofo.edu/Admissions/Cost-Financial-Aid (sha256 3720c227150f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “FAFSA help center Unusual Circumstances with your FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “Please contact the financial aid office if you believe you have unusual circumstances which need to be discussed and/or reviewed.”
### `b7d769e3bb9681cb` Columbia College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ccis.edu/tuition-financial-aid/aid-types/ (sha256 1bc82b3bfa8a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Scholarships Awarded based on a variety of needs, achievements and special circumstances.”
### `7c2568d27e31493b` Columbia College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/college-cost/undergraduate-tuition/day-campus-prior-coa (sha256 de594783b802)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition: 25826 ⟵ “Tuition | $12,913 | $25,826 | $29,954”
  - on_campus:Books: 480 ⟵ “Books | $240 | $480 | $720”
  - on_campus:Housing: 5632 ⟵ “Housing | $2,816 | $5,632 | $15,392”
  - on_campus:Food: 3920 ⟵ “Food | $1,960 | $3,920 | -”
  - on_campus:Transportation: 1600 ⟵ “Transportation | $800 | $1,600 | $2,784”
  - on_campus:Personal: 3616 ⟵ “Personal | $1,808 | $3,616 | $7,408”
  - on_campus:Loan Fees: 32 ⟵ “Loan Fees | $16 | $32 | $48”
  - on_campus:Cost of Attendance: 41106 ⟵ “Cost of Attendance | $20,553 | $41,106 | $56,306”
### `fc39d26dbcc90d2f` Columbia College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ccis.edu/tuition-financial-aid/college-cost/ (sha256 457fe969de0b)
- issues: components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - on_campus:Books: 480 ⟵ “Books | $240 | $480 | $720”
  - on_campus:Housing: 6736 ⟵ “Housing | $3,368 | $6,736 | $16,877”
  - on_campus:Food: 4125 ⟵ “Food | $2,062.50 | $4,125 | -”
  - on_campus:Transportation: 1632 ⟵ “Transportation | $816 | $1,632 | $2,864”
  - on_campus:Personal: 3904 ⟵ “Personal | $1,952 | $3,904 | $7,808”
  - on_campus:Loan Fees: 32 ⟵ “Loan Fees | $16 | $32 | $48”
  - on_campus:Cost of Attendance: 44314 ⟵ “Cost of Attendance | $22,157 | $44,314 | $59,850”
### `12d60416686a8b8c` Columbia College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ccis.edu/admissions/transfer/college-credit/ (sha256 7783939ad97d)
- issues: score_column_not_scores
- checks: {"distinct_exams": 41, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|Lower level]:  ⟵ “2D Art & Design | ARTS 140 (3 hrs) | Lower level”
  - equivalencies[AP-3-D-ART-DESIGN|Lower level]:  ⟵ “3D Art & Design | ARTS 141 (3 hrs) | Lower level”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|Lower level]:  ⟵ “African American Studies | AFAM 101 (3 hrs) | Lower level”
  - equivalencies[AP-ART-HISTORY|Lower level]:  ⟵ “Art History | ARTS 111 (3 hrs) and ARTS 112 (3 hrs) | Lower level”
  - equivalencies[AP-BIOLOGY|Lower level]:  ⟵ “Biology | BIOL 110 (4 hrs) | Lower level”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|Lower level]:  ⟵ “Business with Personal Finance | MGMT 150 (3 hrs) and ELEC 144 (3 hrs) | Lower level”
  - equivalencies[AP-CALCULUS-AB|Lower level]:  ⟵ “Calculus AB | MATH 201 (4 hrs) | Lower level”
  - equivalencies[AP-CALCULUS-BC|Lower level]:  ⟵ “Calculus BC | MATH 201 (4 hrs) & MATH 222 (4 hrs) | Lower level”
  - equivalencies[AP-CHEMISTRY|Lower level]:  ⟵ “Chemistry | Score of 3 - CHEM 110 (4 hrs) Score of 4 or 5 - CHEM 110 (3 hrs) & ELEC 144 (5 hrs) | Lower level”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|Lower level]:  ⟵ “Chinese Language & Culture | Score of 3 - CHIN 101 (3 hrs), CHIN 144 (5 hrs) Score of 4 - CHIN 101 (3 hrs), CHIN 102 (3 hrs), CHIN 144 (6 hrs) Score of 5 - CHIN 101 (3 hrs), CHIN 102 (3 hrs), CHIN 144 (10 hrs) | Lower level”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|Lower level]:  ⟵ “Comparative Government and Politics | POSC 250 (3 hrs) | Lower level”
  - equivalencies[AP-COMPUTER-SCIENCE-A|Lower level]:  ⟵ “Computer Science A | CISS 238 (4 hrs) | Lower level”
  - equivalencies[AP-CYBERSECURITY|Lower level]:  ⟵ “Cybersecurity | CYSC 200 (3 hrs) | Lower level”
  - equivalencies[AP-DRAWING|Lower level]:  ⟵ “Drawing | ARTS 120 (3 hrs) | Lower level”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|Lower level]:  ⟵ “English Language and Composition | ENGL 133W (3 hrs) and ENGL 144 (3 hrs) | Lower level”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|Lower level]:  ⟵ “English Literature and Composition | ENGL 133W (3 hrs) and ENGL 144 (3 hrs) | Lower level”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|Lower level]:  ⟵ “Environmental Science | ELEC 144 (3 hrs) | Lower level”
  - equivalencies[AP-EUROPEAN-HISTORY|Lower level]:  ⟵ “European History | HIST 144 (6 hrs) | Lower level”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|Lower level]:  ⟵ “French Language | Score of 3 - FREN 101 (3 hrs), FREN 144 (3 hrs) Score of 4 - FREN 101 (3 hrs), FREN 102 (3 hrs), FREN 144 (3 hrs) Score of 5 - FREN 101 (3 hrs), FREN 102 (3 hrs), FREN 144 (6 hrs) | Lower level”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|Score of 3 or 4: Lower level Score of 5: Upper level]:  ⟵ “German Language | Score of 3 - GERM 101 (3 hrs), GERM 102 (3 hrs), GERM 144 (6 hrs) Score of 4 - GERM 101 (3 hrs), GERM 102 (3 hrs), GERM 144 (10 hrs) Score of 5 - GERM 101 (3 hrs), GERM 102 (3 hrs), GERM 144 (14 hrs) | Score of 3 or 4: Lower level Score of 5: Upper level”
  - equivalencies[AP-HUMAN-GEOGRAPHY|Lower level]:  ⟵ “Human Geography | GEOG 101 (3 hrs) | Lower level”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|Lower level]:  ⟵ “Italian Language & Culture | Score of 3 - ITAL 101 (3 hrs), ITAL 144 (3 hrs) Score of 4 - ITAL 101 (3 hrs), ITAL 102 (3 hrs), ITAL 144 (3 hrs) Score of 5 - ITAL 101 (3 hrs), ITAL 102 (3 hrs), ITAL 144 (6 hrs) | Lower level”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|Lower level]:  ⟵ “Japanese Language & Culture | Score of 3 - JAPA 101 (3 hrs), JAPA 144 (5 hrs) Score of 4 - JAPA 101 (3 hrs), JAPA 102 (3 hrs), JAPA 144 (6 hrs) Score of 5 - JAPA 101 (3 hrs), JAPA 102 (3 hrs), JAPA 144 (10 hrs) | Lower level”
  - equivalencies[AP-LATIN|Lower level]:  ⟵ “Latin | Score of 3 - LATN 144 (6 hrs) Score of 4 - LATN 144 (9 hrs) Score of 5 - LATN 144 (12 hrs) | Lower level”
  - equivalencies[AP-MACROECONOMICS|Lower level]:  ⟵ “Macroeconomics | ECON 293 (3 hrs) | Lower level”
  - … 16 more rows
### `c2623eab335f4c9e` Columbia College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ccis.edu/admissions/transfer/college-credit/ (sha256 7783939ad97d)
- issues: score_column_not_scores, score_scale_mismatch
- checks: {"distinct_exams": 32, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|American Government]:  ⟵ “American Government | POSC 111 (3 hrs) | Lower level”
  - equivalencies[CLEP-AMERICAN-LITERATURE|American Literature]:  ⟵ “American Literature | ENGL 241 (3 hrs) | Lower level”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|Analyzing and Interpreting Literature]:  ⟵ “Analyzing and Interpreting Literature | ENGL 210 (3 hrs) | Lower level”
  - equivalencies[CLEP-BIOLOGY|Biology]:  ⟵ “Biology | BIOL 110 (6 hrs) | Lower level”
  - equivalencies[CLEP-CALCULUS|Calculus]:  ⟵ “Calculus | MATH 201 (4 hrs) | Lower level”
  - equivalencies[CLEP-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | CHEM 110 (6 hrs) | Lower level”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|College Algebra]:  ⟵ “College Algebra | MATH 150 (3 hrs) | Lower level”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|College Composition]:  ⟵ “College Composition | ENGL 133W (3 hrs) & ELEC 144 [1] (3 hrs) | Lower level”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|College Composition Modular]:  ⟵ “College Composition Modular | ENGL 107 [2] (3 hrs) | Lower level”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|College Mathematics]:  ⟵ “College Mathematics | MATH 1CMR (3 hrs) | Lower level”
  - equivalencies[CLEP-ENGLISH-LITERATURE|English Literature]:  ⟵ “English Literature | ENGL 231 (6 hrs) | Lower level”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|Financial Accounting]:  ⟵ “Financial Accounting | ACCT 280 (3 hrs) | Lower level”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language]:  ⟵ “French Language | Level 1: FREN 101 (3 hrs) & FREN 102 (3 hrs)Level 2: FREN 101 (3 hrs), FREN 102 (3 hrs), & FREN 144 (3 hrs) | Lower level”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German Language]:  ⟵ “German Language | Level 1: GERM 101 (3 hrs) & GERM 102 (3 hrs)Level 2: GERM 101 (3 hrs), GERM 102 (3 hrs), & GERM 144 (3 hrs) | Lower level”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|Human Growth and Development]:  ⟵ “Human Growth and Development | PSYC 330 (3 hrs) | Lower level”
  - equivalencies[CLEP-HUMANITIES|Humanities]:  ⟵ “Humanities | ELEC 144 (3 hrs) | Lower level”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|Information Systems]:  ⟵ “Information Systems | CISS 170 (3 hrs) | Lower level”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|Introduction to Educational Psychology]:  ⟵ “Introduction to Educational Psychology | PSYC/EDUC 230 (3 hrs) | Lower level”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|Introductory Business Law]:  ⟵ “Introductory Business Law | MGMT 265 (3 hrs) | Lower level”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|Introductory Psychology]:  ⟵ “Introductory Psychology | PSYC 101 (3 hrs) | Lower level”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|Introductory Sociology]:  ⟵ “Introductory Sociology | SOCI 111 (3 hrs) | Lower level”
  - equivalencies[CLEP-NATURAL-SCIENCES|Natural Sciences]:  ⟵ “Natural Sciences | CHEM/PHYS 108 (3 hrs) & BIOL 108 (3 hrs) | Lower level”
  - equivalencies[CLEP-PRECALCULUS|Precalculus]:  ⟵ “Precalculus | MATH 180 (3 hrs) | Lower level”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|Principles of Macroeconomics]:  ⟵ “Principles of Macroeconomics | ECON 293 (3 hrs) | Lower level”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|Principles of Management]:  ⟵ “Principles of Management | MGMT 230 (3 hrs) | Lower level”
  - … 10 more rows
### `69c7cb10bbbda87a` Cottey College — appeals 2026-27 [new] (source_unlabeled)
- source: https://cottey.edu/financial-aid/special-circumstances/ (sha256 2f06da25f81d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “If a student believes they have extenuating circumstances, they can request the dependency override request form from the financial aid office.”
### `9bdf4d9d4d858016` Cottey College — appeals 2026-27 [new] (source_unlabeled)
- source: https://cottey.edu/financial-aid/special-circumstances/ (sha256 2f06da25f81d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If professional judgment is used to make adjustments to data elements on the FAFSA, the resulting EFC is used for all FSA funds awarded to the student.”
  - sentence: professional_judgment ⟵ “If a student’s FAFSA was selected for verification, the verification must be completed before using professional judgment.”
### `9e8c8c734f9551e9` Cottey College — appeals 2026-27 [new] (labeled_in_source)
- source: https://cottey.edu/financial-aid/ (sha256 82cefaf846e2)
- issues: semantic_review_required, conflicting_sources:https://cottey.edu/financial-aid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Net Price Calculator How to Apply International Student Aid Maintaining Aid FAQ Student Loans Grants and Scholarships Repaying Loans Info and Resources Special Circumstances Work on Campus Estimated Cost of Attendance Military Tuition Assistance Rights & Responsibilities Office of Financial Aid 1000 West Austin, Nevada, Missouri 64772 Phone: (417) 448-1445 Fax: (417) 448-1045 Apply to Cottey Campu”
### `a626037181c6d531` Cottey College — appeals 2026-27 [new] (source_unlabeled)
- source: https://cottey.edu/financial-aid/special-circumstances/ (sha256 2f06da25f81d)
- issues: semantic_review_required, conflicting_sources:https://cottey.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances - Cottey College Skip to content Commencement Information Close Alert Find out more about Commencement 2025: https://cottey.edu/cottey-commencement/ Watch Live Give Online Alumnae P.E.O.”
  - sentence: need_based_special_circumstances ⟵ “The Higher Education Act allows a financial aid administrator (FAA) to make dependency overrides on a case-by-case basis for students with unusual circumstances.”
### `0572ee2a6b3e101d` Cottey College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://cottey.edu/financial-aid/ (sha256 82cefaf846e2)
- issues: conflicting_sources:https://catalog.cottey.edu/student-fees-per-semester,https://cottey.edu/financial-aid/estimated-cost/
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 28400 ⟵ “Tuition | $28,400”
  - column:Room (avg./student): 6200 ⟵ “Room (avg./student) | $6,200”
  - column:Meals: 6200 ⟵ “Meals | $6,200”
  - column:Required Student Fees: 2688 ⟵ “Required Student Fees | $2,688”
  - column:Total direct costs: 43488 ⟵ “Total direct costs | $43,488”
### `a4fa205eafce0074` Cottey College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.cottey.edu/student-fees-per-semester (sha256 e0bd65bfd629)
- issues: cost_period_semester, conflicting_sources:https://cottey.edu/financial-aid/,https://cottey.edu/financial-aid/estimated-cost/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 28400 ⟵ “Tuition | $28,400 | $28,400 | $28,400”
  - on_campus:Housing (avg./student) and Meals: 12400 ⟵ “Housing (avg./student) and Meals | $12,400 | $8,385 | $4,730”
  - on_campus:Required Fees: 2688 ⟵ “Required Fees | $2,688 | $2,688 | $2,688”
  - on_campus:Books & Supplies: 2504 ⟵ “Books & Supplies | $2,504 | $2,504 | $2,504”
  - on_campus:Miscellaneous/Personal ($167/mo x 9 months): 3414 ⟵ “Miscellaneous/Personal ($167/mo x 9 months) | $3,414 | $3,414 | $3,414”
  - on_campus:Transportation: 2504 ⟵ “Transportation | $2,504 | $2,504 | $2,504”
  - on_campus:Total: 51910 ⟵ “Total | $51,910 | $47,895 | $44,240”
  - off_campus_not_with_family:Tuition: 28400 ⟵ “Tuition | $28,400 | $28,400 | $28,400”
  - off_campus_not_with_family:Housing (avg./student) and Meals: 8385 ⟵ “Housing (avg./student) and Meals | $12,400 | $8,385 | $4,730”
  - off_campus_not_with_family:Required Fees: 2688 ⟵ “Required Fees | $2,688 | $2,688 | $2,688”
  - off_campus_not_with_family:Books & Supplies: 2504 ⟵ “Books & Supplies | $2,504 | $2,504 | $2,504”
  - off_campus_not_with_family:Miscellaneous/Personal ($167/mo x 9 months): 3414 ⟵ “Miscellaneous/Personal ($167/mo x 9 months) | $3,414 | $3,414 | $3,414”
  - off_campus_not_with_family:Transportation: 2504 ⟵ “Transportation | $2,504 | $2,504 | $2,504”
  - off_campus_not_with_family:Total: 47895 ⟵ “Total | $51,910 | $47,895 | $44,240”
  - with_parents_or_family:Tuition: 28400 ⟵ “Tuition | $28,400 | $28,400 | $28,400”
  - with_parents_or_family:Housing (avg./student) and Meals: 4730 ⟵ “Housing (avg./student) and Meals | $12,400 | $8,385 | $4,730”
  - with_parents_or_family:Required Fees: 2688 ⟵ “Required Fees | $2,688 | $2,688 | $2,688”
  - with_parents_or_family:Books & Supplies: 2504 ⟵ “Books & Supplies | $2,504 | $2,504 | $2,504”
  - with_parents_or_family:Miscellaneous/Personal ($167/mo x 9 months): 3414 ⟵ “Miscellaneous/Personal ($167/mo x 9 months) | $3,414 | $3,414 | $3,414”
  - with_parents_or_family:Transportation: 2504 ⟵ “Transportation | $2,504 | $2,504 | $2,504”
  - with_parents_or_family:Total: 44240 ⟵ “Total | $51,910 | $47,895 | $44,240”
### `c1c33dc56beca8dd` Cottey College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://cottey.edu/financial-aid/estimated-cost/ (sha256 481266bdd111)
- issues: conflicting_sources:https://catalog.cottey.edu/student-fees-per-semester,https://cottey.edu/financial-aid/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 28400 ⟵ “Tuition | $28,400 | $28,400 | $28,400”
  - on_campus:Room (avg./student) and Meals: 12400 ⟵ “Room (avg./student) and Meals | $12,400 | $8,385 | $4,730”
  - on_campus:Required Fees: 2688 ⟵ “Required Fees | $2,688 | $2,688 | $2,688”
  - on_campus:Books & Supplies: 2504 ⟵ “Books & Supplies | $2,504 | $2,504 | $2,504”
  - on_campus:Miscellaneous/Personal: 3414 ⟵ “Miscellaneous/Personal | $3,414 | $3,414 | $3,414”
  - on_campus:Transportation: 2504 ⟵ “Transportation | $2,504 | $2,504 | $2,504”
  - on_campus:Total: 51910 ⟵ “Total | $51,910 | $47,895 | $44,240”
  - off_campus_not_with_family:Tuition: 28400 ⟵ “Tuition | $28,400 | $28,400 | $28,400”
  - off_campus_not_with_family:Room (avg./student) and Meals: 8385 ⟵ “Room (avg./student) and Meals | $12,400 | $8,385 | $4,730”
  - off_campus_not_with_family:Required Fees: 2688 ⟵ “Required Fees | $2,688 | $2,688 | $2,688”
  - off_campus_not_with_family:Books & Supplies: 2504 ⟵ “Books & Supplies | $2,504 | $2,504 | $2,504”
  - off_campus_not_with_family:Miscellaneous/Personal: 3414 ⟵ “Miscellaneous/Personal | $3,414 | $3,414 | $3,414”
  - off_campus_not_with_family:Transportation: 2504 ⟵ “Transportation | $2,504 | $2,504 | $2,504”
  - off_campus_not_with_family:Total: 47895 ⟵ “Total | $51,910 | $47,895 | $44,240”
  - with_parents_or_family:Tuition: 28400 ⟵ “Tuition | $28,400 | $28,400 | $28,400”
  - with_parents_or_family:Room (avg./student) and Meals: 4730 ⟵ “Room (avg./student) and Meals | $12,400 | $8,385 | $4,730”
  - with_parents_or_family:Required Fees: 2688 ⟵ “Required Fees | $2,688 | $2,688 | $2,688”
  - with_parents_or_family:Books & Supplies: 2504 ⟵ “Books & Supplies | $2,504 | $2,504 | $2,504”
  - with_parents_or_family:Miscellaneous/Personal: 3414 ⟵ “Miscellaneous/Personal | $3,414 | $3,414 | $3,414”
  - with_parents_or_family:Transportation: 2504 ⟵ “Transportation | $2,504 | $2,504 | $2,504”
  - with_parents_or_family:Total: 44240 ⟵ “Total | $51,910 | $47,895 | $44,240”
### `48cf341dbb3e07aa` Culver-Stockton College — appeals 2026-27 [new] (labeled_in_source)
- source: https://culver.edu/wp-content/uploads/2025/10/Special-Circumstance-2026.27.pdf (sha256 6643661a3437)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCES REQUEST 2026-2027 Academic Year The results of your 2026–2027 Free Application for Federal Student Aid (FAFSA) must be on file with the Culver-Stockton College Financial Aid Office prior to any consideration of special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances requests will not be considered for the following reasons: • Voluntary loss/decrease of income* • Leaving a job to go to school* • Excessive consumer debts • Private school tuition • Daycare expenses *If there are extenuating circumstances to the above conditions, they may be considered.”
### `7626c3b11797000d` Culver-Stockton College — appeals 2025-26 [new] (labeled_in_source)
- source: https://culver.edu/wp-content/uploads/2025/01/Special-Circumstance-2025.26.pdf (sha256 16777e0b0ffc)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCES REQUEST 2025-2026 Academic Year The results of your 2025-2026 Free Application for Federal Student Aid must be on file with the Culver- Stockton Financial Aid Office before a special circumstance will be considered.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances requests will not be considered for the following reasons: • Voluntary loss/decrease of income* • Leaving a job to go to school* • Excessive consumer debts • Private school tuition • Daycare expenses *If there are extenuating circumstances to the above conditions, they may be considered.”
### `10c7f7494abdbbbe` Drury University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.drury.edu/financial-aid/professional-judgment/ (sha256 f7cd469c63a9)
- issues: ambiguous_year_labels, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “The circumstances below are generally not considered for a Professional Judgment adjustment: FAFSA information currently reflects an EFC of 0 (2023-24 and prior) or SAI of -1500 (2024-25 and beyond) Consumer debt such as credit cards, car payments, mortgages, and loans Change of marital status during the award year.”
  - sentence: professional_judgment ⟵ “Parents refuse to contribute to college expenses Parents do not claim you as a dependent on their tax return Parents refuse to provide their information on the FAFSA You do not live with your parents Required Documentation Because Professional Judgment requests may result in a change to information on your FAFSA, they must be thoroughly documented.”
  - sentence: professional_judgment ⟵ “The first step in requesting a Professional Judgment review is to submit a detailed personal statement explaining why the FAFSA does not accurately represent your current financial picture.”
  - sentence: professional_judgment ⟵ “While we can discuss Professional Judgment with parents of dependent students who have a current FERPA Information Release, the initial request for Professional Judgment should come from the student.”
  - sentence: professional_judgment ⟵ “Timeline Requests for Professional Judgment will be accepted beginning April 1 for the upcoming academic year and will be reviewed in the order they are received.”
  - sentence: professional_judgment ⟵ “An approved Professional Judgment request does not guarantee eligibility for or receipt of additional aid.”
### `1b31840f69cf15d5` Drury University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.drury.edu/financial-aid/satisfactory-academic-progress-sap/ (sha256 09d4440e09d0)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Successful appeals will be monitored in the same manner as other SAP appeals.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process Academic progress is monitored annually, following the end of the spring semester.”
### `100732f312b5d9f6` Drury University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 abb3fb87a429)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: GPA 3.0+ ⟵ “GPA 3.0+ | TOEFL 80IELTS 6.5SAT/ACT 1110/25 | Presidential $22,000per year”
  - test_requirement: Only 1 Test Required: TOEFL 80IELTS 6.5SAT/ACT 1110/25 ⟵ “GPA 3.0+ | TOEFL 80IELTS 6.5SAT/ACT 1110/25 | Presidential $22,000per year”
  - award_amount_text: Presidential $22,000per year ⟵ “GPA 3.0+ | TOEFL 80IELTS 6.5SAT/ACT 1110/25 | Presidential $22,000per year”
### `5cab271bd4c6be89` Drury University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 a4dac30b62c6)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 21,000 ⟵ “GPA 3.01-3.3 | 21,000 | 21,000 | 18,000 | 18,000 | 18,000”
### `9b112ffbe33e9a3b` Drury University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 a4dac30b62c6)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: GPA 3.0+ ⟵ “GPA 3.0+ | TOEFL 62IELTS 5.5SAT/ACT 1000/21 | Provost $20,000per year”
  - test_requirement: Only 1 Test Required: TOEFL 62IELTS 5.5SAT/ACT 1000/21 ⟵ “GPA 3.0+ | TOEFL 62IELTS 5.5SAT/ACT 1000/21 | Provost $20,000per year”
  - award_amount_text: Provost $20,000per year ⟵ “GPA 3.0+ | TOEFL 62IELTS 5.5SAT/ACT 1000/21 | Provost $20,000per year”
### `b5697d212f176d0a` Drury University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 abb3fb87a429)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 18,000 ⟵ “GPA <=2.5 | 18,000 | 18,000 | 0 | 0 | 0”
### `bf8a7816346fdd83` Drury University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 a4dac30b62c6)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 25,000 ⟵ “GPA 4.0+ | 25,000 | 24,000 | 24,000 | 21,000 | 18,000”
### `c33c776bfd3ddd74` Drury University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 a4dac30b62c6)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 18,000 ⟵ “GPA 2.51-3.0 | 18,000 | 18,000 | 18,000 | 18,000 | 18,000”
### `c57c31def351d215` Drury University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 abb3fb87a429)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 24,000 ⟵ “GPA 3.61-3.8 | 24,000 | 24,000 | 21,000 | 18,000 | 18,000”
### `d719d9809e06280d` Drury University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 a4dac30b62c6)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 24,000 ⟵ “GPA 3.31-3.6 | 24,000 | 21,000 | 21,000 | 18,000 | 18,000”
### `e1ad7b92166a7f65` Drury University — awards 2025-26 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 abb3fb87a429)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: GPA 3.5+ ⟵ “GPA 3.5+ | TOEFL 90IELTS 7.0SAT/ACT 1220/29 | Trustee $24,000per year”
  - test_requirement: Only 1 Test Required: TOEFL 90IELTS 7.0SAT/ACT 1220/29 ⟵ “GPA 3.5+ | TOEFL 90IELTS 7.0SAT/ACT 1220/29 | Trustee $24,000per year”
  - award_amount_text: Trustee $24,000per year ⟵ “GPA 3.5+ | TOEFL 90IELTS 7.0SAT/ACT 1220/29 | Trustee $24,000per year”
### `e4d2be8ed8db4dba` Drury University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 abb3fb87a429)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 25,000 ⟵ “GPA 3.81-3.99 | 25,000 | 24,000 | 21,000 | 21,000 | 18,000”
### `136e48aba98840aa` Drury University — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.drury.edu/wp-content/uploads/files/dual_credit/pdf/DC%20Panther%20Scholars%20Fund%20Process%202024-2025.pdf (sha256 7f09e3e51b44)
- issues: stale_year_label:2024-25, shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “●   Student must have a minimum high school GPA of 3.0 (unweighted)”
### `mdc81a8c2d59577e` Drury University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.drury.edu/wp-content/uploads/files/dual_credit/pdf/DC%20Fall%202026%20OL%20Course%20List.pdf (sha256 20a87ff30ca8)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 6, "tiers": 2}
  - per_credit_hour_charge: 90 ⟵ “Online: Online courses are offered to students in the fall, spring, and summer semesters at $90/credit hour.”
  - per_credit_hour_charge: 70 ⟵ “Seated: Seated dual credit courses are offered at the students’ high school during the school day at $70/credit hour.”
  - eligibility_tier: 3.0 ⟵ “o ALL students, freshmen through senior must have a 3.0 GPA.”
  - eligibility_tier: 3.0 ⟵ “o Students who do not meet the 3.0 GPA are required to complete the DC Permission Form.”
  - eligibility_tier: 3.0 ⟵ “o ALL students, freshmen through senior must have a 3.0 GPA.”
  - eligibility_tier: 3.0 ⟵ “o Students who do not meet the 3.0 GPA are required to complete the DC Permission Form.”
  - eligibility_tier: 3.0 ⟵ “This student has a high school GPA of at least 3.0.”
  - eligibility_tier: 2.0 ⟵ “Degree Requirements: Minimum 62 credit hours; Minimum GPA 2.0.”
  - eligibility_tier: 2.0 ⟵ “Degree Requirements: Minimum 62 credit hours; Minimum GPA of 2.0.”
### `mcf0f34c97cac2b2` Drury University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.drury.edu/admission/transfer-to-drury/ (sha256 7dd542e31a7e)
- issues: conflicting_values:residency_requirement_credits, shared_site_attribution_review
- checks: {"fields": [], "merged_pages": 3}
### `c1404683cf5819de` Drury University-College of Continuing Professional Studies — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.drury.edu/financial-aid/satisfactory-academic-progress-sap/ (sha256 9f8c8fbdeacc)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Successful appeals will be monitored in the same manner as other SAP appeals.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process Academic progress is monitored annually, following the end of the spring semester.”
### `f9a3735f9050a2ff` Drury University-College of Continuing Professional Studies — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.drury.edu/financial-aid/professional-judgment/ (sha256 2b9eacdca65a)
- issues: ambiguous_year_labels, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “The circumstances below are generally not considered for a Professional Judgment adjustment: FAFSA information currently reflects an EFC of 0 (2023-24 and prior) or SAI of -1500 (2024-25 and beyond) Consumer debt such as credit cards, car payments, mortgages, and loans Change of marital status during the award year.”
  - sentence: professional_judgment ⟵ “Parents refuse to contribute to college expenses Parents do not claim you as a dependent on their tax return Parents refuse to provide their information on the FAFSA You do not live with your parents Required Documentation Because Professional Judgment requests may result in a change to information on your FAFSA, they must be thoroughly documented.”
  - sentence: professional_judgment ⟵ “The first step in requesting a Professional Judgment review is to submit a detailed personal statement explaining why the FAFSA does not accurately represent your current financial picture.”
  - sentence: professional_judgment ⟵ “While we can discuss Professional Judgment with parents of dependent students who have a current FERPA Information Release, the initial request for Professional Judgment should come from the student.”
  - sentence: professional_judgment ⟵ “Timeline Requests for Professional Judgment will be accepted beginning April 1 for the upcoming academic year and will be reviewed in the order they are received.”
  - sentence: professional_judgment ⟵ “An approved Professional Judgment request does not guarantee eligibility for or receipt of additional aid.”
### `6c08fee3a5b6738c` Drury University-College of Continuing Professional Studies — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 c321cf9e3bae)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 18,000 ⟵ “GPA 2.51-3.0 | 18,000 | 18,000 | 18,000 | 18,000 | 18,000”
### `8cba843921c7e43f` Drury University-College of Continuing Professional Studies — awards 2025-26 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 c321cf9e3bae)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: GPA 3.5+ ⟵ “GPA 3.5+ | TOEFL 90IELTS 7.0SAT/ACT 1220/29 | Trustee $24,000per year”
  - test_requirement: Only 1 Test Required: TOEFL 90IELTS 7.0SAT/ACT 1220/29 ⟵ “GPA 3.5+ | TOEFL 90IELTS 7.0SAT/ACT 1220/29 | Trustee $24,000per year”
  - award_amount_text: Trustee $24,000per year ⟵ “GPA 3.5+ | TOEFL 90IELTS 7.0SAT/ACT 1220/29 | Trustee $24,000per year”
### `b770d93b904660d2` Drury University-College of Continuing Professional Studies — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 4f671f41e2bc)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 24,000 ⟵ “GPA 3.31-3.6 | 24,000 | 21,000 | 21,000 | 18,000 | 18,000”
### `bb61507f372356c4` Drury University-College of Continuing Professional Studies — awards 2025-26 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 c321cf9e3bae)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: GPA 3.0+ ⟵ “GPA 3.0+ | TOEFL 80IELTS 6.5SAT/ACT 1110/25 | Presidential $22,000per year”
  - test_requirement: Only 1 Test Required: TOEFL 80IELTS 6.5SAT/ACT 1110/25 ⟵ “GPA 3.0+ | TOEFL 80IELTS 6.5SAT/ACT 1110/25 | Presidential $22,000per year”
  - award_amount_text: Presidential $22,000per year ⟵ “GPA 3.0+ | TOEFL 80IELTS 6.5SAT/ACT 1110/25 | Presidential $22,000per year”
### `c44d0d131710f65e` Drury University-College of Continuing Professional Studies — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 4f671f41e2bc)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 21,000 ⟵ “GPA 3.01-3.3 | 21,000 | 21,000 | 18,000 | 18,000 | 18,000”
### `ce7e29b44995d51c` Drury University-College of Continuing Professional Studies — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 c321cf9e3bae)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 18,000 ⟵ “GPA <=2.5 | 18,000 | 18,000 | 0 | 0 | 0”
### `d9f13b7ad25da84a` Drury University-College of Continuing Professional Studies — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 4f671f41e2bc)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 24,000 ⟵ “GPA 3.61-3.8 | 24,000 | 24,000 | 21,000 | 18,000 | 18,000”
### `dea02c27a3879a8a` Drury University-College of Continuing Professional Studies — awards 2025-26 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 c321cf9e3bae)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: High School GPA: GPA 3.0+ ⟵ “GPA 3.0+ | TOEFL 62IELTS 5.5SAT/ACT 1000/21 | Provost $20,000per year”
  - test_requirement: Only 1 Test Required: TOEFL 62IELTS 5.5SAT/ACT 1000/21 ⟵ “GPA 3.0+ | TOEFL 62IELTS 5.5SAT/ACT 1000/21 | Provost $20,000per year”
  - award_amount_text: Provost $20,000per year ⟵ “GPA 3.0+ | TOEFL 62IELTS 5.5SAT/ACT 1000/21 | Provost $20,000per year”
### `e4c6506d83622e00` Drury University-College of Continuing Professional Studies — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 4f671f41e2bc)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 25,000 ⟵ “GPA 4.0+ | 25,000 | 24,000 | 24,000 | 21,000 | 18,000”
### `f164b9c5668f7106` Drury University-College of Continuing Professional Studies — awards 2027-28 [new] (labeled_in_source)
- source: https://www.drury.edu/financial-aid/scholarship-information/ (sha256 4f671f41e2bc)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - test_requirement: ACT 25,000 ⟵ “GPA 3.81-3.99 | 25,000 | 24,000 | 21,000 | 21,000 | 18,000”
### `218262b85373955f` Drury University-College of Continuing Professional Studies — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.drury.edu/wp-content/uploads/files/dual_credit/pdf/DC%20Panther%20Scholars%20Fund%20Process%202024-2025.pdf (sha256 7f09e3e51b44)
- issues: stale_year_label:2024-25, shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “●   Student must have a minimum high school GPA of 3.0 (unweighted)”
### `meded8a4537e54a7` Drury University-College of Continuing Professional Studies — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.drury.edu/wp-content/uploads/files/dual_credit/pdf/DC%20Fall%202026%20OL%20Course%20List.pdf (sha256 20a87ff30ca8)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 6, "tiers": 2}
  - per_credit_hour_charge: 90 ⟵ “Online: Online courses are offered to students in the fall, spring, and summer semesters at $90/credit hour.”
  - per_credit_hour_charge: 70 ⟵ “Seated: Seated dual credit courses are offered at the students’ high school during the school day at $70/credit hour.”
  - eligibility_tier: 3.0 ⟵ “o ALL students, freshmen through senior must have a 3.0 GPA.”
  - eligibility_tier: 3.0 ⟵ “o Students who do not meet the 3.0 GPA are required to complete the DC Permission Form.”
  - eligibility_tier: 3.0 ⟵ “o ALL students, freshmen through senior must have a 3.0 GPA.”
  - eligibility_tier: 3.0 ⟵ “o Students who do not meet the 3.0 GPA are required to complete the DC Permission Form.”
  - eligibility_tier: 3.0 ⟵ “This student has a high school GPA of at least 3.0.”
  - eligibility_tier: 2.0 ⟵ “Degree Requirements: Minimum 62 credit hours; Minimum GPA 2.0.”
  - eligibility_tier: 2.0 ⟵ “Degree Requirements: Minimum 62 credit hours; Minimum GPA of 2.0.”
### `m4748eef522cb7c8` Drury University-College of Continuing Professional Studies — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.drury.edu/admission/transfer-to-drury/ (sha256 a11dc04715aa)
- issues: conflicting_values:residency_requirement_credits, shared_site_attribution_review
- checks: {"fields": [], "merged_pages": 3}
### `6b4dacbb4577c21d` East Central College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eastcentral.edu/finaid/wp-content/uploads/sites/8/2025/05/25.26-Satisfactory-Academic-Progress-Appeal.pdf (sha256 18b88a21cda9)
- issues: semantic_review_required, conflicting_sources:https://www.eastcentral.edu/finaid/minimum-standards-of-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS (SAP) APPEAL Financial Aid Office 1964 Prairie Dell Road, Union, MO 63084 Phone: 636-584-6588 Email: financialaid@eastcentral.edu Name: ______________ _____________________________________Student ID# Last First MI Address: _____________________________________________________ Phone: (_____) _____-_______ Street City State Zip I am requesting Financial Aid Reinstateme”
  - sentence: sap_appeal ⟵ “I certify that the information contained in this SAP appeal form, supporting documentation and statements, is accurate and complete to the best of my knowledge.”
### `f7fefc29eb0434fa` East Central College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eastcentral.edu/finaid/minimum-standards-of-academic-progress/ (sha256 b5c7ae01933f)
- issues: semantic_review_required, conflicting_sources:https://www.eastcentral.edu/finaid/wp-content/uploads/sites/8/2025/05/25.26-Satisfactory-Academic-Progress-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Student’s right to appeal suspension In the event of extenuating circumstances, the student may request to be continued in the financial aid programs by submitting the Satisfactory Academic Progress Financial Aid Suspension Appeal form with all supporting documents to the Financial Aid appeals committee.”
### `2dd4657037009a5a` East Central College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.eastcentral.edu/registrar/credit-by-exam/ (sha256 416362b7d7f0)
- issues: rows_without_score
- checks: {"distinct_exams": 30, "equivalencies": 30, "rows_without_score": 30}
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Macroeconomics | ECO 101 | 3”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Microeconomics | ECO 102 | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|None]:  ⟵ “Comparative Government & Politics | PSC 202 | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|None]:  ⟵ “U.S. Government & Politics | PSC 102* | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Human Geography | GRY 101 | 3”
  - equivalencies[AP-PSYCHOLOGY|None]:  ⟵ “Psychology | PSY 101 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “U.S. History | HST 101* or HST 102* | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|None]:  ⟵ “World History | HST 202 | 3”
  - equivalencies[AP-SEMINAR|None]:  ⟵ “AP Seminar | ENG 101 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language | ENG 101 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “English Literature | ENG ELEC (elective) OR ENG 101 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “French Language | HUM ELEC | 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “German Language | HUM ELEC | 4”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “Japanese Language & Culture | HUM ELEC | 3”
  - equivalencies[AP-LATIN|None]:  ⟵ “Latin: Vergil | HUM ELEC | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|None]:  ⟵ “Spanish Language | SPN 101 | 4”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|None]:  ⟵ “Spanish Literature | HUM ELEC | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “European History | CIV 202 | 3”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | BIO 101 | 3”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | CHM 100 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “Environmental Science | EVR 103 | 3”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB | MTH 190 | 5”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Calculus BC | MTH 210 | 5”
  - equivalencies[AP-STATISTICS|None]:  ⟵ “Statistics | MTH 150 | 3”
  - equivalencies[AP-PHYSICS-1|None]:  ⟵ “Physics 1 | PHY 111/112 | 5”
  - … 5 more rows
### `00feea4d079d96f4` Evangel University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 96d4e24a57b4)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Dependency Override Policy Students who do not meet the federal criteria for independent status may request a professional judgment review to override their dependency status.”
### `08edf5e9dd080c7b` Evangel University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “The student will be provided with the opportunity to appeal this decision to the professional judgment committee.”
  - sentence: professional_judgment ⟵ “Any members of the SAP committee that ruled on the student’s initial determination are not permitted to also serve on the professional judgment committee reviewing the appeal.”
  - sentence: professional_judgment ⟵ “Like professional judgment, all committee decisions are final and not appealable to the Department of Education and the reasons for the decision shall be documented and maintained for possible review.”
### `1f295971bde91b4c` Evangel University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 cf5dab5520da)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Dependency Override Policy Students who do not meet the federal criteria for independent status may request a professional judgment review to override their dependency status.”
### `3ba673c96a584ab2` Evangel University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 96d4e24a57b4)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Below you’ll find downloadable forms related to: Dependency Override Requests Special Circumstance Appeals Unaccompanied & Homeless Youth Verification Instructions: Please review each form’s description carefully to make sure you’re submitting the correct one.”
  - sentence: need_based_special_circumstances ⟵ “These overrides are granted only in rare and exceptional situations—known as “unusual circumstances”—and are evaluated case by case.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Circumstances That May Qualify: Abandonment by parents An abusive family environment that threatens the student’s health or safety Inability to locate parents Other extreme and documented unusual circumstances “Unusual circumstances” refer to situations where it would be inappropriate to expect a parental contribution toward the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Department of Education has clarified that the following do not qualify as unusual circumstances on their own: Parents refuse to contribute to the student’s education Parents are unwilling to provide FAFSA or verification information Parents do not claim the student as a dependent on their taxes The student is financially self-sufficient Important Note: Approval of a dependency override is not aut”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal We understand that the FAFSA doesn’t always reflect your full financial picture.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family have experienced a significant change in circumstances, you may be eligible to submit a Special Circumstance Appeal for additional financial aid consideration.”
### `834b026ccde5af32` Evangel University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/ (sha256 ce48e6d48b25)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You can complete a Special Circumstances Appeal Form with the required documentation of circumstances and submit it to Evangel University’s Office of Financial Aid.”
### `9be99f5c12b84056` Evangel University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf (sha256 8839024c5b7c)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances Appeal Form Do not complete this form unless you have already applied for ﬁnancial aid using the 2026-2027 Free Applica on for Federal Student Aid (FAFSA) and have received a ﬁnancial aid oﬀer from Evangel University.”
  - sentence: need_based_special_circumstances ⟵ “If you have not ﬁled the FAFSA, please complete the online form at: www.FAFSA.gov The Special Circumstances Appeal form allows you to explain changes in your family’s ﬁnancial situa on during the 2025 calendar year and for us to review circumstances not considered when you completed the 2026-2027 FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If you qualify for full Pell (have an SAI of -1500 to 0), you are receiving the highest amount of federal aid available to you and a Special Circumstance Appeal would not result in a change in ﬁnancial aid.”
  - sentence: need_based_special_circumstances ⟵ “Oﬃce of Financial Aid A n: Special Circumstance Appeal Evangel University 1111 North Glenstone Avenue Springﬁeld, Missouri 65802 FAX 417.575.5478 Appeal Categories Select the category that most closely describes your special circumstance. □ Loss or reduc on of employment, loss of military employment or benefits You (and/or your spouse or parent) earned money in 2024 or 2025and had an income reduc ”
  - sentence: need_based_special_circumstances ⟵ “Special circumstance considera on will not be given if this one- me income is a result of an inheritance, job bonus or over me compensa on, pension, capital gain, insurance se lements, or early distribu ons of re rement account.”
  - sentence: need_based_special_circumstances ⟵ “Payment of insurance premiums, regular health maintenance, and rou ne expenses such as eyeglasses, birth control prescrip ons, and elec ve or cosme c procedures (e. g., orthodon c braces) are not considered unusual medical expenses and will not be considered for the special circumstances appeal.”
### `b56e3df45865ff87` Evangel University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 cf5dab5520da)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Below you’ll find downloadable forms related to: Dependency Override Requests Special Circumstance Appeals Unaccompanied & Homeless Youth Verification Instructions: Please review each form’s description carefully to make sure you’re submitting the correct one.”
  - sentence: need_based_special_circumstances ⟵ “These overrides are granted only in rare and exceptional situations—known as “unusual circumstances”—and are evaluated case by case.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Circumstances That May Qualify: Abandonment by parents An abusive family environment that threatens the student’s health or safety Inability to locate parents Other extreme and documented unusual circumstances “Unusual circumstances” refer to situations where it would be inappropriate to expect a parental contribution toward the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Department of Education has clarified that the following do not qualify as unusual circumstances on their own: Parents refuse to contribute to the student’s education Parents are unwilling to provide FAFSA or verification information Parents do not claim the student as a dependent on their taxes The student is financially self-sufficient Important Note: Approval of a dependency override is not aut”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal We understand that the FAFSA doesn’t always reflect your full financial picture.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family have experienced a significant change in circumstances, you may be eligible to submit a Special Circumstance Appeal for additional financial aid consideration.”
### `d2b2ae31405655b0` Evangel University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/ (sha256 fb1b01f813bd)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If a student is required to complete verification as part of the Special Circumstances Appeal process, the deadline for Special Circumstances Appeal will apply.”
### `e814ccd7fa8ccf9c` Evangel University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals Procedures – Students who have been placed on suspension from financial aid due to their failure to comply with the academic progress policy have the right to appeal, if suspension is a result of unusual circumstances, such as illness, death in the family, accidents, or other satisfactory reasons. [34 CFR 668.16(e)(5)(6)] Students that wish to appeal must contact their Financial Aid Counse”
### `f86cc18c19bff06b` Evangel University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 cf5dab5520da)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Forms & Instructions Please download and complete the form below to request a dependency override.”
  - sentence: dependency_override ⟵ “Submit all required supporting documentation as outlined in the form. 🔗 [Dependency Override Request Form (PDF)] Includes required documentation checklist and submission instructions.”
### `3b5818c861fae876` Evangel University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: See undergraduate chart above ⟵ “Online | See undergraduate chart above”
### `529f22efcf976032` Evangel University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 2.0}}
  - gpa_requirement: 2.0 ⟵ “Seminary – Master of Divinity | 2.0”
### `590c9fabf3a6dd59` Evangel University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Graduate | 3.0”
### `86e6ea8864dc48ed` Evangel University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 2.5}}
  - gpa_requirement: 2.5 ⟵ “Seminary – Master of Arts | 2.5”
### `ea6586a977557b96` Evangel University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Seminary – Doctoral | 3.0”
### `eb71c935298b5a82` Evangel University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 1d86a384c7fd)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 16, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “Biology | 5-7 | BIOL 101, 199 | 8 | 4-7 | BIOL 101 & 199 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5-7]:  ⟵ “Business and Management | 5-7 | MGMT 235(3) | 3 | 4-5 | MGMT 235(3) | 3”
  - equivalencies[IB-CHEMISTRY|5-7]:  ⟵ “Chemistry | 5-7 | CHEM 111 | 5 | 4-5 | CHEM 111 | 5”
  - equivalencies[IB-COMPUTER-SCIENCE|5-7]:  ⟵ “Computer Science | 5-7 | CPSC 101 | 3 | 4-7 | CPSC 101 | 3”
  - equivalencies[IB-ECONOMICS|5-7]:  ⟵ “Economics | 5-7 | ECON 212 | 3 | 4-5 | ECON 212 | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|5-7]:  ⟵ “Environmental Systems | 5-7 | ENVR 342 | 3 | 4-7 | ENVR 342 | 3”
  - equivalencies[IB-FILM|5-7]:  ⟵ “Film | 5-7 | COMF 220 | 3 | 4-7 | COMF 220 | 3”
  - equivalencies[IB-GEOGRAPHY|5-7]:  ⟵ “Geography | 5-7 | GEOG 211 | 3 | 4-7 | GEOG 211 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Americas (Group B US Hist Elective) | 5-7 | HIST111 | 3 | 4-7 | HIST111 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Europe (Group A Non-US Hist Elective) | 5-7 | HIST 345 | 3 | 4-7 | HIST 345 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Islamic (Group A Non-US Hist Elective) | 5-7 | HIST 260 | 3 | 4-7 | HIST 260 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-African (Group A Non-US Hist Elective) | 5-7 | HIST 270 | 3 | 4-7 | HIST 270 | 3”
  - equivalencies[IB-MUSIC|5-7]:  ⟵ “Music | 5-7 | MUSC 131 | 2 | 4-5 | MUSC 131 | 2”
  - equivalencies[IB-PHILOSOPHY|5-7]:  ⟵ “Philosophy | 5-7 | PHIL 115 | 3 | 4-7 | PHIL 115 | 3”
  - equivalencies[IB-PHYSICS|5-7]:  ⟵ “Physics | 5-7 | PHYS211 (4) | 4 | 4-5 | PHYS211 (4) | 4”
  - equivalencies[IB-PSYCHOLOGY|5-7]:  ⟵ “Psychology | 5-7 | PSYC 112 | 3 | 4-7 | PSYC 112 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5-7]:  ⟵ “Social and Cultural Anthropology | 5-7 | ANTH 231 | 3 | 4-5 | ANTH 231 | 3”
  - equivalencies[IB-THEATRE|5-7]:  ⟵ “Theatre Arts | 5-7 | THTR 110 (3) | 5 | 4-5 | THTR 110 (3) | 3”
  - equivalencies[IB-VISUAL-ARTS|5-7]:  ⟵ “Visual Arts Option A (Dr. Nelson) | 5-7 | ART 102 OR ART 199 | 3 | 4-7 | ART 102 OR ART 199 | 3”
  - equivalencies[IB-VISUAL-ARTS|5-7]:  ⟵ “Visual Arts Option B (Dr. Nelson) | 5-7 | ART 103 OR ART 199 | 3 | 4-7 | ART 103 OR ART 199 | 3”
  - equivalencies[IB-VISUAL-ARTS|Foreign LanguagesStudents who have earned foreign language credit may be awarded up to the maximum number of foreign language credits (up to 14 credits). Please consult with the Department of Humanities to complete the level-appropriate proficiency exam.]:  ⟵ “Visual Arts Option B (Dr. Nelson) | Foreign LanguagesStudents who have earned foreign language credit may be awarded up to the maximum number of foreign language credits (up to 14 credits). Please consult with the Department of Humanities to complete the level-appropriate proficiency exam.”
### `ee5b638b54ab43e0` Evangel University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 1d86a384c7fd)
- issues: score_scale_mismatch, shared_site_attribution_review
- checks: {"distinct_exams": 13, "equivalencies": 16, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-COMPOSITION|3]:  ⟵ “College Composition | ENGL 111 | Composition | 3”
  - equivalencies[CLEP-HUMANITIES|2]:  ⟵ “Humanities | HUMN 199 | Human Elective | 2”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|3]:  ⟵ “College Mathematics | MATH 122 | Basic Concepts Algebra | 3”
  - equivalencies[CLEP-NATURAL-SCIENCES|3]:  ⟵ “Natural Sciences | GSCI 115 | Physical Science | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|3]:  ⟵ “Social Sciences/History | SOCI 199 | Sociology Elective | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government | GOVT 170 | Intro to American Govt | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|3]:  ⟵ “American Literature | ENGL 199 | Literature Elective | 3”
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus with Elementary Function | MATH 231 | Calculus I | 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra | MATH 129 | College Algebra | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|8]:  ⟵ “College French Level 1 | FREN 115, 116 | Elementary French | 8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|6]:  ⟵ “College French Level 1 | FREN 215, 216 | Intermediate French | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|8]:  ⟵ “College Level German | GRMN 115, 116 | Elementary German | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|8]:  ⟵ “College Level Spanish Level 1 | SPAN 115, 116 | Elementary Spanish | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|6]:  ⟵ “College Level Spanish Level 2 | SPAN 215, 216 | Intermediate Spanish | 6”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature | ENGL 311 | English Lit Survey I | 3”
  - equivalencies[CLEP-HUMANITIES|3]:  ⟵ “Humanities | HUMN 231 | Introduction to Western Humanities | 3”
### `m3abad8a9fbe2529` Evangel University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/admissions/dual-enrollment/ (sha256 84c1d0a16fab)
- issues: shared_site_attribution_review
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 0}
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
### `m630ca9b0deaefc0` Evangel University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 1d86a384c7fd)
- issues: shared_site_attribution_review
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 64 ⟵ “You can transfer up to 64 semester hours of credit from a community or junior college.”
  - max_transfer_credits: 64 ⟵ “You can transfer up to 64 semester hours of credit from a community or junior college.”
### `06463c6d9ab08a0b` Evangel University-College of Online Learning — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 2dd93cca9742)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Dependency Override Policy Students who do not meet the federal criteria for independent status may request a professional judgment review to override their dependency status.”
### `0be355172afb28ea` Evangel University-College of Online Learning — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 9af0e4872905)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Dependency Override Policy Students who do not meet the federal criteria for independent status may request a professional judgment review to override their dependency status.”
### `1c21c59d2b236e90` Evangel University-College of Online Learning — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals Procedures – Students who have been placed on suspension from financial aid due to their failure to comply with the academic progress policy have the right to appeal, if suspension is a result of unusual circumstances, such as illness, death in the family, accidents, or other satisfactory reasons. [34 CFR 668.16(e)(5)(6)] Students that wish to appeal must contact their Financial Aid Counse”
### `440645cd89d0a690` Evangel University-College of Online Learning — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf (sha256 8839024c5b7c)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances Appeal Form Do not complete this form unless you have already applied for ﬁnancial aid using the 2026-2027 Free Applica on for Federal Student Aid (FAFSA) and have received a ﬁnancial aid oﬀer from Evangel University.”
  - sentence: need_based_special_circumstances ⟵ “If you have not ﬁled the FAFSA, please complete the online form at: www.FAFSA.gov The Special Circumstances Appeal form allows you to explain changes in your family’s ﬁnancial situa on during the 2025 calendar year and for us to review circumstances not considered when you completed the 2026-2027 FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If you qualify for full Pell (have an SAI of -1500 to 0), you are receiving the highest amount of federal aid available to you and a Special Circumstance Appeal would not result in a change in ﬁnancial aid.”
  - sentence: need_based_special_circumstances ⟵ “Oﬃce of Financial Aid A n: Special Circumstance Appeal Evangel University 1111 North Glenstone Avenue Springﬁeld, Missouri 65802 FAX 417.575.5478 Appeal Categories Select the category that most closely describes your special circumstance. □ Loss or reduc on of employment, loss of military employment or benefits You (and/or your spouse or parent) earned money in 2024 or 2025and had an income reduc ”
  - sentence: need_based_special_circumstances ⟵ “Special circumstance considera on will not be given if this one- me income is a result of an inheritance, job bonus or over me compensa on, pension, capital gain, insurance se lements, or early distribu ons of re rement account.”
  - sentence: need_based_special_circumstances ⟵ “Payment of insurance premiums, regular health maintenance, and rou ne expenses such as eyeglasses, birth control prescrip ons, and elec ve or cosme c procedures (e. g., orthodon c braces) are not considered unusual medical expenses and will not be considered for the special circumstances appeal.”
### `5ab0f8cd0e1417f7` Evangel University-College of Online Learning — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/ (sha256 fb1b01f813bd)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If a student is required to complete verification as part of the Special Circumstances Appeal process, the deadline for Special Circumstances Appeal will apply.”
### `75ee31c2ac701b8b` Evangel University-College of Online Learning — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “The student will be provided with the opportunity to appeal this decision to the professional judgment committee.”
  - sentence: professional_judgment ⟵ “Any members of the SAP committee that ruled on the student’s initial determination are not permitted to also serve on the professional judgment committee reviewing the appeal.”
  - sentence: professional_judgment ⟵ “Like professional judgment, all committee decisions are final and not appealable to the Department of Education and the reasons for the decision shall be documented and maintained for possible review.”
### `93768ebed2c53754` Evangel University-College of Online Learning — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/ (sha256 ce48e6d48b25)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You can complete a Special Circumstances Appeal Form with the required documentation of circumstances and submit it to Evangel University’s Office of Financial Aid.”
### `b3d6603302751500` Evangel University-College of Online Learning — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 9af0e4872905)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Below you’ll find downloadable forms related to: Dependency Override Requests Special Circumstance Appeals Unaccompanied & Homeless Youth Verification Instructions: Please review each form’s description carefully to make sure you’re submitting the correct one.”
  - sentence: need_based_special_circumstances ⟵ “These overrides are granted only in rare and exceptional situations—known as “unusual circumstances”—and are evaluated case by case.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Circumstances That May Qualify: Abandonment by parents An abusive family environment that threatens the student’s health or safety Inability to locate parents Other extreme and documented unusual circumstances “Unusual circumstances” refer to situations where it would be inappropriate to expect a parental contribution toward the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Department of Education has clarified that the following do not qualify as unusual circumstances on their own: Parents refuse to contribute to the student’s education Parents are unwilling to provide FAFSA or verification information Parents do not claim the student as a dependent on their taxes The student is financially self-sufficient Important Note: Approval of a dependency override is not aut”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal We understand that the FAFSA doesn’t always reflect your full financial picture.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family have experienced a significant change in circumstances, you may be eligible to submit a Special Circumstance Appeal for additional financial aid consideration.”
### `cb78452c55e06d23` Evangel University-College of Online Learning — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 2dd93cca9742)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Below you’ll find downloadable forms related to: Dependency Override Requests Special Circumstance Appeals Unaccompanied & Homeless Youth Verification Instructions: Please review each form’s description carefully to make sure you’re submitting the correct one.”
  - sentence: need_based_special_circumstances ⟵ “These overrides are granted only in rare and exceptional situations—known as “unusual circumstances”—and are evaluated case by case.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Circumstances That May Qualify: Abandonment by parents An abusive family environment that threatens the student’s health or safety Inability to locate parents Other extreme and documented unusual circumstances “Unusual circumstances” refer to situations where it would be inappropriate to expect a parental contribution toward the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Department of Education has clarified that the following do not qualify as unusual circumstances on their own: Parents refuse to contribute to the student’s education Parents are unwilling to provide FAFSA or verification information Parents do not claim the student as a dependent on their taxes The student is financially self-sufficient Important Note: Approval of a dependency override is not aut”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal We understand that the FAFSA doesn’t always reflect your full financial picture.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family have experienced a significant change in circumstances, you may be eligible to submit a Special Circumstance Appeal for additional financial aid consideration.”
### `cd4ad4e452063df7` Evangel University-College of Online Learning — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 9af0e4872905)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Forms & Instructions Please download and complete the form below to request a dependency override.”
  - sentence: dependency_override ⟵ “Submit all required supporting documentation as outlined in the form. 🔗 [Dependency Override Request Form (PDF)] Includes required documentation checklist and submission instructions.”
### `0107c81c99e3f3d9` Evangel University-College of Online Learning — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: See undergraduate chart above ⟵ “Online | See undergraduate chart above”
### `0d68aa66f6fa38e8` Evangel University-College of Online Learning — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Seminary – Doctoral | 3.0”
### `5aa6e976d8de6e62` Evangel University-College of Online Learning — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Graduate | 3.0”
### `85910e5e6ef53107` Evangel University-College of Online Learning — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 2.5}}
  - gpa_requirement: 2.5 ⟵ “Seminary – Master of Arts | 2.5”
### `b8c276fcf81086f3` Evangel University-College of Online Learning — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 2.0}}
  - gpa_requirement: 2.0 ⟵ “Seminary – Master of Divinity | 2.0”
### `cf56ff05ee1f4017` Evangel University-College of Online Learning — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 8c7ef94b0615)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 16, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “Biology | 5-7 | BIOL 101, 199 | 8 | 4-7 | BIOL 101 & 199 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5-7]:  ⟵ “Business and Management | 5-7 | MGMT 235(3) | 3 | 4-5 | MGMT 235(3) | 3”
  - equivalencies[IB-CHEMISTRY|5-7]:  ⟵ “Chemistry | 5-7 | CHEM 111 | 5 | 4-5 | CHEM 111 | 5”
  - equivalencies[IB-COMPUTER-SCIENCE|5-7]:  ⟵ “Computer Science | 5-7 | CPSC 101 | 3 | 4-7 | CPSC 101 | 3”
  - equivalencies[IB-ECONOMICS|5-7]:  ⟵ “Economics | 5-7 | ECON 212 | 3 | 4-5 | ECON 212 | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|5-7]:  ⟵ “Environmental Systems | 5-7 | ENVR 342 | 3 | 4-7 | ENVR 342 | 3”
  - equivalencies[IB-FILM|5-7]:  ⟵ “Film | 5-7 | COMF 220 | 3 | 4-7 | COMF 220 | 3”
  - equivalencies[IB-GEOGRAPHY|5-7]:  ⟵ “Geography | 5-7 | GEOG 211 | 3 | 4-7 | GEOG 211 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Americas (Group B US Hist Elective) | 5-7 | HIST111 | 3 | 4-7 | HIST111 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Europe (Group A Non-US Hist Elective) | 5-7 | HIST 345 | 3 | 4-7 | HIST 345 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Islamic (Group A Non-US Hist Elective) | 5-7 | HIST 260 | 3 | 4-7 | HIST 260 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-African (Group A Non-US Hist Elective) | 5-7 | HIST 270 | 3 | 4-7 | HIST 270 | 3”
  - equivalencies[IB-MUSIC|5-7]:  ⟵ “Music | 5-7 | MUSC 131 | 2 | 4-5 | MUSC 131 | 2”
  - equivalencies[IB-PHILOSOPHY|5-7]:  ⟵ “Philosophy | 5-7 | PHIL 115 | 3 | 4-7 | PHIL 115 | 3”
  - equivalencies[IB-PHYSICS|5-7]:  ⟵ “Physics | 5-7 | PHYS211 (4) | 4 | 4-5 | PHYS211 (4) | 4”
  - equivalencies[IB-PSYCHOLOGY|5-7]:  ⟵ “Psychology | 5-7 | PSYC 112 | 3 | 4-7 | PSYC 112 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5-7]:  ⟵ “Social and Cultural Anthropology | 5-7 | ANTH 231 | 3 | 4-5 | ANTH 231 | 3”
  - equivalencies[IB-THEATRE|5-7]:  ⟵ “Theatre Arts | 5-7 | THTR 110 (3) | 5 | 4-5 | THTR 110 (3) | 3”
  - equivalencies[IB-VISUAL-ARTS|5-7]:  ⟵ “Visual Arts Option A (Dr. Nelson) | 5-7 | ART 102 OR ART 199 | 3 | 4-7 | ART 102 OR ART 199 | 3”
  - equivalencies[IB-VISUAL-ARTS|5-7]:  ⟵ “Visual Arts Option B (Dr. Nelson) | 5-7 | ART 103 OR ART 199 | 3 | 4-7 | ART 103 OR ART 199 | 3”
  - equivalencies[IB-VISUAL-ARTS|Foreign LanguagesStudents who have earned foreign language credit may be awarded up to the maximum number of foreign language credits (up to 14 credits). Please consult with the Department of Humanities to complete the level-appropriate proficiency exam.]:  ⟵ “Visual Arts Option B (Dr. Nelson) | Foreign LanguagesStudents who have earned foreign language credit may be awarded up to the maximum number of foreign language credits (up to 14 credits). Please consult with the Department of Humanities to complete the level-appropriate proficiency exam.”
### `e375084cd86bf74d` Evangel University-College of Online Learning — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 8c7ef94b0615)
- issues: score_scale_mismatch, shared_site_attribution_review
- checks: {"distinct_exams": 13, "equivalencies": 16, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-COMPOSITION|3]:  ⟵ “College Composition | ENGL 111 | Composition | 3”
  - equivalencies[CLEP-HUMANITIES|2]:  ⟵ “Humanities | HUMN 199 | Human Elective | 2”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|3]:  ⟵ “College Mathematics | MATH 122 | Basic Concepts Algebra | 3”
  - equivalencies[CLEP-NATURAL-SCIENCES|3]:  ⟵ “Natural Sciences | GSCI 115 | Physical Science | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|3]:  ⟵ “Social Sciences/History | SOCI 199 | Sociology Elective | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government | GOVT 170 | Intro to American Govt | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|3]:  ⟵ “American Literature | ENGL 199 | Literature Elective | 3”
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus with Elementary Function | MATH 231 | Calculus I | 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra | MATH 129 | College Algebra | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|8]:  ⟵ “College French Level 1 | FREN 115, 116 | Elementary French | 8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|6]:  ⟵ “College French Level 1 | FREN 215, 216 | Intermediate French | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|8]:  ⟵ “College Level German | GRMN 115, 116 | Elementary German | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|8]:  ⟵ “College Level Spanish Level 1 | SPAN 115, 116 | Elementary Spanish | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|6]:  ⟵ “College Level Spanish Level 2 | SPAN 215, 216 | Intermediate Spanish | 6”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature | ENGL 311 | English Lit Survey I | 3”
  - equivalencies[CLEP-HUMANITIES|3]:  ⟵ “Humanities | HUMN 231 | Introduction to Western Humanities | 3”
### `mf2edb0713a28876` Evangel University-College of Online Learning — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/admissions/dual-enrollment/ (sha256 e976ecb34343)
- issues: shared_site_attribution_review
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 0}
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
### `m1ab40e6866dc2bb` Evangel University-College of Online Learning — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 ba2851f62713)
- issues: shared_site_attribution_review
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 64 ⟵ “You can transfer up to 64 semester hours of credit from a community or junior college.”
  - max_transfer_credits: 64 ⟵ “You can transfer up to 64 semester hours of credit from a community or junior college.”
### `08da9d7de6968fe3` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals Procedures – Students who have been placed on suspension from financial aid due to their failure to comply with the academic progress policy have the right to appeal, if suspension is a result of unusual circumstances, such as illness, death in the family, accidents, or other satisfactory reasons. [34 CFR 668.16(e)(5)(6)] Students that wish to appeal must contact their Financial Aid Counse”
### `20955b166c33aad4` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 2469cd7984a7)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Dependency Override Policy Students who do not meet the federal criteria for independent status may request a professional judgment review to override their dependency status.”
### `36493cd181c4eeeb` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/ (sha256 ce48e6d48b25)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You can complete a Special Circumstances Appeal Form with the required documentation of circumstances and submit it to Evangel University’s Office of Financial Aid.”
### `39c72c8ad3a31e3e` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 2469cd7984a7)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Below you’ll find downloadable forms related to: Dependency Override Requests Special Circumstance Appeals Unaccompanied & Homeless Youth Verification Instructions: Please review each form’s description carefully to make sure you’re submitting the correct one.”
  - sentence: need_based_special_circumstances ⟵ “These overrides are granted only in rare and exceptional situations—known as “unusual circumstances”—and are evaluated case by case.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Circumstances That May Qualify: Abandonment by parents An abusive family environment that threatens the student’s health or safety Inability to locate parents Other extreme and documented unusual circumstances “Unusual circumstances” refer to situations where it would be inappropriate to expect a parental contribution toward the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Department of Education has clarified that the following do not qualify as unusual circumstances on their own: Parents refuse to contribute to the student’s education Parents are unwilling to provide FAFSA or verification information Parents do not claim the student as a dependent on their taxes The student is financially self-sufficient Important Note: Approval of a dependency override is not aut”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal We understand that the FAFSA doesn’t always reflect your full financial picture.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family have experienced a significant change in circumstances, you may be eligible to submit a Special Circumstance Appeal for additional financial aid consideration.”
### `4cf4f0feb8010838` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 905b224e7541)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Below you’ll find downloadable forms related to: Dependency Override Requests Special Circumstance Appeals Unaccompanied & Homeless Youth Verification Instructions: Please review each form’s description carefully to make sure you’re submitting the correct one.”
  - sentence: need_based_special_circumstances ⟵ “These overrides are granted only in rare and exceptional situations—known as “unusual circumstances”—and are evaluated case by case.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Circumstances That May Qualify: Abandonment by parents An abusive family environment that threatens the student’s health or safety Inability to locate parents Other extreme and documented unusual circumstances “Unusual circumstances” refer to situations where it would be inappropriate to expect a parental contribution toward the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “Department of Education has clarified that the following do not qualify as unusual circumstances on their own: Parents refuse to contribute to the student’s education Parents are unwilling to provide FAFSA or verification information Parents do not claim the student as a dependent on their taxes The student is financially self-sufficient Important Note: Approval of a dependency override is not aut”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Appeal We understand that the FAFSA doesn’t always reflect your full financial picture.”
  - sentence: need_based_special_circumstances ⟵ “If you or your family have experienced a significant change in circumstances, you may be eligible to submit a Special Circumstance Appeal for additional financial aid consideration.”
### `6d2fc4036e4d3b9e` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf (sha256 8839024c5b7c)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances Appeal Form Do not complete this form unless you have already applied for ﬁnancial aid using the 2026-2027 Free Applica on for Federal Student Aid (FAFSA) and have received a ﬁnancial aid oﬀer from Evangel University.”
  - sentence: need_based_special_circumstances ⟵ “If you have not ﬁled the FAFSA, please complete the online form at: www.FAFSA.gov The Special Circumstances Appeal form allows you to explain changes in your family’s ﬁnancial situa on during the 2025 calendar year and for us to review circumstances not considered when you completed the 2026-2027 FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If you qualify for full Pell (have an SAI of -1500 to 0), you are receiving the highest amount of federal aid available to you and a Special Circumstance Appeal would not result in a change in ﬁnancial aid.”
  - sentence: need_based_special_circumstances ⟵ “Oﬃce of Financial Aid A n: Special Circumstance Appeal Evangel University 1111 North Glenstone Avenue Springﬁeld, Missouri 65802 FAX 417.575.5478 Appeal Categories Select the category that most closely describes your special circumstance. □ Loss or reduc on of employment, loss of military employment or benefits You (and/or your spouse or parent) earned money in 2024 or 2025and had an income reduc ”
  - sentence: need_based_special_circumstances ⟵ “Special circumstance considera on will not be given if this one- me income is a result of an inheritance, job bonus or over me compensa on, pension, capital gain, insurance se lements, or early distribu ons of re rement account.”
  - sentence: need_based_special_circumstances ⟵ “Payment of insurance premiums, regular health maintenance, and rou ne expenses such as eyeglasses, birth control prescrip ons, and elec ve or cosme c procedures (e. g., orthodon c braces) are not considered unusual medical expenses and will not be considered for the special circumstances appeal.”
### `7c7c85d9c2a0ef6c` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 905b224e7541)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Dependency Override Policy Students who do not meet the federal criteria for independent status may request a professional judgment review to override their dependency status.”
### `993489ea0d724abd` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “The student will be provided with the opportunity to appeal this decision to the professional judgment committee.”
  - sentence: professional_judgment ⟵ “Any members of the SAP committee that ruled on the student’s initial determination are not permitted to also serve on the professional judgment committee reviewing the appeal.”
  - sentence: professional_judgment ⟵ “Like professional judgment, all committee decisions are final and not appealable to the Department of Education and the reasons for the decision shall be documented and maintained for possible review.”
### `bf631ec4266e0522` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/ (sha256 905b224e7541)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Forms & Instructions Please download and complete the form below to request a dependency override.”
  - sentence: dependency_override ⟵ “Submit all required supporting documentation as outlined in the form. 🔗 [Dependency Override Request Form (PDF)] Includes required documentation checklist and submission instructions.”
### `c276c431c46ed809` Evangel University-James River Assembly of God Church — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-verification/ (sha256 fb1b01f813bd)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/federal-financial-aid/faq-filing-the-fafsa/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/financial-aid-forms/,https://www.evangel.edu/wp-content/uploads/2026/04/2627_special_circumstance_appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If a student is required to complete verification as part of the Special Circumstances Appeal process, the deadline for Special Circumstances Appeal will apply.”
### `46c3a7b30d0a9c89` Evangel University-James River Assembly of God Church — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 2.0}}
  - gpa_requirement: 2.0 ⟵ “Seminary – Master of Divinity | 2.0”
### `603142182c37ddfa` Evangel University-James River Assembly of God Church — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - gpa_requirement: See undergraduate chart above ⟵ “Online | See undergraduate chart above”
### `939b2b55521b97a4` Evangel University-James River Assembly of God Church — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 2.5}}
  - gpa_requirement: 2.5 ⟵ “Seminary – Master of Arts | 2.5”
### `a803885e7c833d0d` Evangel University-James River Assembly of God Church — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Graduate | 3.0”
### `bafa30bc72dd6249` Evangel University-James River Assembly of God Church — awards 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/financial-aid-and-scholarships/policies-procedures/ (sha256 e77aaf5c95f7)
- issues: shared_site_attribution_review
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Seminary – Doctoral | 3.0”
### `67f0a640734456a1` Evangel University-James River Assembly of God Church — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 59df989a3ad0)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 16, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5-7]:  ⟵ “Biology | 5-7 | BIOL 101, 199 | 8 | 4-7 | BIOL 101 & 199 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5-7]:  ⟵ “Business and Management | 5-7 | MGMT 235(3) | 3 | 4-5 | MGMT 235(3) | 3”
  - equivalencies[IB-CHEMISTRY|5-7]:  ⟵ “Chemistry | 5-7 | CHEM 111 | 5 | 4-5 | CHEM 111 | 5”
  - equivalencies[IB-COMPUTER-SCIENCE|5-7]:  ⟵ “Computer Science | 5-7 | CPSC 101 | 3 | 4-7 | CPSC 101 | 3”
  - equivalencies[IB-ECONOMICS|5-7]:  ⟵ “Economics | 5-7 | ECON 212 | 3 | 4-5 | ECON 212 | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|5-7]:  ⟵ “Environmental Systems | 5-7 | ENVR 342 | 3 | 4-7 | ENVR 342 | 3”
  - equivalencies[IB-FILM|5-7]:  ⟵ “Film | 5-7 | COMF 220 | 3 | 4-7 | COMF 220 | 3”
  - equivalencies[IB-GEOGRAPHY|5-7]:  ⟵ “Geography | 5-7 | GEOG 211 | 3 | 4-7 | GEOG 211 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Americas (Group B US Hist Elective) | 5-7 | HIST111 | 3 | 4-7 | HIST111 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Europe (Group A Non-US Hist Elective) | 5-7 | HIST 345 | 3 | 4-7 | HIST 345 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-Islamic (Group A Non-US Hist Elective) | 5-7 | HIST 260 | 3 | 4-7 | HIST 260 | 3”
  - equivalencies[IB-HISTORY|5-7]:  ⟵ “History-African (Group A Non-US Hist Elective) | 5-7 | HIST 270 | 3 | 4-7 | HIST 270 | 3”
  - equivalencies[IB-MUSIC|5-7]:  ⟵ “Music | 5-7 | MUSC 131 | 2 | 4-5 | MUSC 131 | 2”
  - equivalencies[IB-PHILOSOPHY|5-7]:  ⟵ “Philosophy | 5-7 | PHIL 115 | 3 | 4-7 | PHIL 115 | 3”
  - equivalencies[IB-PHYSICS|5-7]:  ⟵ “Physics | 5-7 | PHYS211 (4) | 4 | 4-5 | PHYS211 (4) | 4”
  - equivalencies[IB-PSYCHOLOGY|5-7]:  ⟵ “Psychology | 5-7 | PSYC 112 | 3 | 4-7 | PSYC 112 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5-7]:  ⟵ “Social and Cultural Anthropology | 5-7 | ANTH 231 | 3 | 4-5 | ANTH 231 | 3”
  - equivalencies[IB-THEATRE|5-7]:  ⟵ “Theatre Arts | 5-7 | THTR 110 (3) | 5 | 4-5 | THTR 110 (3) | 3”
  - equivalencies[IB-VISUAL-ARTS|5-7]:  ⟵ “Visual Arts Option A (Dr. Nelson) | 5-7 | ART 102 OR ART 199 | 3 | 4-7 | ART 102 OR ART 199 | 3”
  - equivalencies[IB-VISUAL-ARTS|5-7]:  ⟵ “Visual Arts Option B (Dr. Nelson) | 5-7 | ART 103 OR ART 199 | 3 | 4-7 | ART 103 OR ART 199 | 3”
  - equivalencies[IB-VISUAL-ARTS|Foreign LanguagesStudents who have earned foreign language credit may be awarded up to the maximum number of foreign language credits (up to 14 credits). Please consult with the Department of Humanities to complete the level-appropriate proficiency exam.]:  ⟵ “Visual Arts Option B (Dr. Nelson) | Foreign LanguagesStudents who have earned foreign language credit may be awarded up to the maximum number of foreign language credits (up to 14 credits). Please consult with the Department of Humanities to complete the level-appropriate proficiency exam.”
### `d442ed47b9c53da5` Evangel University-James River Assembly of God Church — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 d5a6f8529eb0)
- issues: score_scale_mismatch, shared_site_attribution_review
- checks: {"distinct_exams": 13, "equivalencies": 16, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-COMPOSITION|3]:  ⟵ “College Composition | ENGL 111 | Composition | 3”
  - equivalencies[CLEP-HUMANITIES|2]:  ⟵ “Humanities | HUMN 199 | Human Elective | 2”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|3]:  ⟵ “College Mathematics | MATH 122 | Basic Concepts Algebra | 3”
  - equivalencies[CLEP-NATURAL-SCIENCES|3]:  ⟵ “Natural Sciences | GSCI 115 | Physical Science | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|3]:  ⟵ “Social Sciences/History | SOCI 199 | Sociology Elective | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government | GOVT 170 | Intro to American Govt | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|3]:  ⟵ “American Literature | ENGL 199 | Literature Elective | 3”
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus with Elementary Function | MATH 231 | Calculus I | 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra | MATH 129 | College Algebra | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|8]:  ⟵ “College French Level 1 | FREN 115, 116 | Elementary French | 8”
  - equivalencies[CLEP-FRENCH-LANGUAGE|6]:  ⟵ “College French Level 1 | FREN 215, 216 | Intermediate French | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|8]:  ⟵ “College Level German | GRMN 115, 116 | Elementary German | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|8]:  ⟵ “College Level Spanish Level 1 | SPAN 115, 116 | Elementary Spanish | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|6]:  ⟵ “College Level Spanish Level 2 | SPAN 215, 216 | Intermediate Spanish | 6”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature | ENGL 311 | English Lit Survey I | 3”
  - equivalencies[CLEP-HUMANITIES|3]:  ⟵ “Humanities | HUMN 231 | Introduction to Western Humanities | 3”
### `mbcd53150fea5fdd` Evangel University-James River Assembly of God Church — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.evangel.edu/future-students/admissions/dual-enrollment/ (sha256 e9c2ae69d93f)
- issues: shared_site_attribution_review
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 0}
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
  - per_credit_hour_charge: 85 ⟵ “Evangel University’s dual enrollment tuition for 2026-27 is $85 per credit hour. A three-credit hour course will cost $255. Lab fees may apply.”
  - per_credit_hour_charge: 65 ⟵ “Only degree seeking students, admitted to our undergraduate program, can receive financial assistance. Courses are extremely affordable at only $65 per credit hour.”
### `m09333e0b61e0052` Evangel University-James River Assembly of God Church — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.evangel.edu/future-students/office-of-admissions/transfer-credit-evaluations/ (sha256 59df989a3ad0)
- issues: shared_site_attribution_review
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 64 ⟵ “You can transfer up to 64 semester hours of credit from a community or junior college.”
  - max_transfer_credits: 64 ⟵ “You can transfer up to 64 semester hours of credit from a community or junior college.”
### `5d979d72a5162e90` Fontbonne University — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.fontbonne.edu/home/scholarships-tuition/financial-aid-faqs/ (sha256 1fcd741ced05)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students who wish to take a second leave of absence during the calendar year may do so only for special circumstances which include, but are not limited to the following: military reasons, circumstances covered by the Family Medical Leave Act of 1993, ADA accommodations, jury duty, university course cancellation and/or faculty closure, and natural disasters.”
### `ff868577028ca07d` Fontbonne University — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.fontbonne.edu/home/scholarships-tuition/financial-aid-faqs/ (sha256 1fcd741ced05)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The EFC takes into consideration household size, number of people in college, income, and a variety of other factors. (If you are facing extenuating circumstances, please consider submitting a Professional Judgment form to our office).”
### `1d4cf75aae746ea8` Lincoln University — appeals 2022-23 [new] (labeled_in_source)
- source: https://www.lincolnu.edu/admissions/financial-aid/apply-for-aid/index.html (sha256 103b9e4f7204)
- issues: stale_year_label:2022-23, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Determine Your Dependency Status Your depency status determines whose information you must report when you fill out the FAFSA® Visit to Learn More About Dependency Status Unable To Provide Parent Information Learn More About Special Circumstances At any time since you turned age 13, were both your parents deceased, were you in foster care, or were you a dependent or ward of the court?”
  - sentence: need_based_special_circumstances ⟵ “Learn More About Special Circumstances You believe you have a special circumstance and are unable to provide parental information.”
  - sentence: need_based_special_circumstances ⟵ “Your special circumstance may be one of the following possibilities: You're unable to provide parental information.”
### `3a3d6f2f737852e1` Lincoln University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lincolnu.edu/admissions/financial-aid/dependency-override-appeal-request-form3.pdf (sha256 8f74c0265ab6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: dependency_override ⟵ “Dependency Override Appeal Request Form REGULATIONS provide for an appeal process, by which the Office Read this first: Financial aid eligibility is based on of Student Financial Services may decide that a student is the family as the first source of a student’s support. independent for financial aid purposes.”
  - sentence: dependency_override ⟵ “This is called a Dependency According to federal regulations, the following Override and is decided on a case-by-case and year-by-year basis. conditions DO NOT qualify as reasons for a Only adverse family situations will be considered for a dependency Dependency Status Appeal: override.”
  - sentence: dependency_override ⟵ “Mailing Address LU Email City State Zip Home Phone (+ Area Code) Cellphone (+Area Code) WHAT YOU SHOULD DO To be considered for a Dependency Override, you must submit the following along with this form: • Signed student statement.”
  - sentence: dependency_override ⟵ “The letters should clearly describe the adverse situation that may qualify you for a dependency override.”
  - sentence: dependency_override ⟵ “CERTIFICATION I certify the information submitted along with this Dependency Override Appeal Request Form is accurate, true, and complete to the best of my knowledge.”
  - sentence: dependency_override ⟵ “The decision is final and cannot be appealed to Federal Student Aid. • If your appeal is approved- Student Financial Services will submit a correction to the FAFSA Central Processing System with a Dependency Override and your financial aid will be processed based on independent status. • If your appeal is not approved- you MUST provide parent financial information and signatures using FAFSA online”
### `655684e81fe7ffd5` Lincoln University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.lincolnu.edu/admissions/financial-aid/financial-aid-reconsideration-form-2025.pdf (sha256 781206015dbd)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCE FOR CONSIDERATION: The 2025-2026 FASA collects student, spouse, and/or parents income information, as applicable, for January 1, 2023 to December 31, 2023.”
  - sentence: need_based_special_circumstances ⟵ “If there has been a significant change in income since that time for the periods 01/01/2023 - 12/31/2024 for anyone whose income information was used to complete the 2025-2026 FAFSA, you may submit this form for review of the spe3cial circumstance(s) related to the change of income you want considered.”
  - sentence: need_based_special_circumstances ⟵ “Received one-time lump received a one- -Explain how funds were used (include this in your sum payment in time lump sum explanation of the special circumstance you want 2024. payment in 2024. considered). -Provide documentation of the use of the funds. - 2024 Tax Return Transcript - 2025-2026 Standard Verification Worksheet Other - Documentation detailing circumstance.”
  - sentence: need_based_special_circumstances ⟵ “COMPLETE ONLY IF YOU HAVE ONE OF THE TWO CIRCUMSTANCES DESCRIBED: COMPLETE ONLY IF YOUR SPECIAL CIRCUMSTANCE IS FOR MEDICAL/DENTAL EXPENSES PAID IN 2025: $ Medical/Dental Expenses in 2025 COMPLETE ONLY IF YOUR SPECIAL CIRCUMSTANCE IS FOR A ONE- TIME PAYMENT RECEIVED IN 2025: $ Amount of lump sum received in 2025 Signatures (Required) By signing this worksheet, I (we) certify that all the informati”
### `ff8461db86a8d6f5` Lincoln University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lincolnu.edu/admissions/financial-aid/financial-aid-reconsideration-form-2026.pdf (sha256 1152fbbb6717)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCE FOR CONSIDERATION: The 2026-2027 FASA collects student, spouse, and/or parents income information, as applicable, for January 1, 2024 to December 31, 2024.”
  - sentence: need_based_special_circumstances ⟵ “If there has been a significant change in income since that time for the periods 01/01/2024 - 12/31/2025 for anyone whose income information was used to complete the 2026-2027 FAFSA, you may submit this form for review of the special circumstance(s) related to the change of income you want considered.”
  - sentence: need_based_special_circumstances ⟵ “Received one-time lump received a one- -Explain how funds were used (include this in your sum payment in time lump sum explanation of the special circumstance you want 2025. payment in 2025. considered). -Provide documentation of the use of the funds. - 2025 Tax Return Transcript - 2026-2027 Standard Verification Worksheet Other - Documentation detailing circumstance.”
  - sentence: need_based_special_circumstances ⟵ “COMPLETE ONLY IF YOU HAVE ONE OF THE TWO CIRCUMSTANCES DESCRIBED: COMPLETE ONLY IF YOUR SPECIAL CIRCUMSTANCE IS FOR MEDICAL/DENTAL EXPENSES PAID IN 2025: $ Medical/Dental Expenses in 2026 COMPLETE ONLY IF YOUR SPECIAL CIRCUMSTANCE IS FOR A ONE- TIME PAYMENT RECEIVED IN 2026: $ Amount of lump sum received in 2026 Signatures (Required) By signing this worksheet, I (we) certify that all the informati”
### `1b329e8846e733c0` Lincoln University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lincolnu.edu/admissions/financial-aid/2025-2026-cost-of-attendance-budgets.pdf (sha256 4b49bfd92f76)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 56}
  - column:Tuition: 16350 ⟵ “Tuition | 8070 | 16350”
  - column:Fees: 1794 ⟵ “Fees | 1794 | 1794”
  - column:Housing & Food: 11452 ⟵ “Housing & Food | 11452 | 11452”
  - column:Books/Supplies: 2000 ⟵ “Books/Supplies | 2000 | 2000”
  - column:Personal/Transportation: 3468 ⟵ “Personal/Transportation | 3468 | 3468”
  - column:Average Loan Fees: 270 ⟵ “Average Loan Fees | 270 | 270”
  - column:Total: 35334 ⟵ “Total | 27054 | 35334”
  - column:Tuition (2): 16350 ⟵ “Tuition | 8070 | 16350”
  - column:Fees (2): 1794 ⟵ “Fees | 1794 | 1794”
  - column:Housing & Food (2): 7825 ⟵ “Housing & Food | 7825 | 7825”
  - column:Books/Supplies (2): 2000 ⟵ “Books/Supplies | 2000 | 2000”
  - column:Personal/Transportation (2): 3716 ⟵ “Personal/Transportation | 3716 | 3716”
  - column:Average Loan Fees (2): 270 ⟵ “Average Loan Fees | 270 | 270”
  - column:Total (2): 31956 ⟵ “Total | 23675 | 31956”
  - column:Tuition (3): 16350 ⟵ “Tuition | 8070 | 16350”
  - column:Fees (3): 1794 ⟵ “Fees | 1794 | 1794”
  - column:Housing & Food (3): 2965 ⟵ “Housing & Food | 2965 | 2965”
  - column:Books/Supplies (3): 2000 ⟵ “Books/Supplies | 2000 | 2000”
  - column:Personal/Transportation (3): 3468 ⟵ “Personal/Transportation | 3468 | 3468”
  - column:Average Loan Fees (3): 270 ⟵ “Average Loan Fees | 270 | 270”
  - column:Total (3): 26847 ⟵ “Total | 18567 | 26847”
  - column:Tuition (4): 16350 ⟵ “Tuition | 8070 | 16350”
  - column:Fees (4): 4044 ⟵ “Fees | 4044 | 4044”
  - column:Housing & Food (4): 11452 ⟵ “Housing & Food | 11452 | 11452”
  - column:Books/Supplies (4): 2000 ⟵ “Books/Supplies | 2000 | 2000”
  - … 31 more rows
### `7598183f41fbc1a2` Lincoln University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.lincolnu.edu/admissions/financial-aid/2025-2026-cost-of-attendance-budgets.pdf (sha256 4b49bfd92f76)
- issues: multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 60}
  - column:Tuition: 8070 ⟵ “Tuition | 8070 | 16350”
  - column:Fees: 1794 ⟵ “Fees | 1794 | 1794”
  - column:Housing & Food: 11452 ⟵ “Housing & Food | 11452 | 11452”
  - column:Books/Supplies: 2000 ⟵ “Books/Supplies | 2000 | 2000”
  - column:Personal/Transportation: 3468 ⟵ “Personal/Transportation | 3468 | 3468”
  - column:Average Loan Fees: 270 ⟵ “Average Loan Fees | 270 | 270”
  - column:Total: 27054 ⟵ “Total | 27054 | 35334”
  - column:Tuition (2): 8070 ⟵ “Tuition | 8070 | 16350”
  - column:Fees (2): 1794 ⟵ “Fees | 1794 | 1794”
  - column:Housing & Food (2): 7825 ⟵ “Housing & Food | 7825 | 7825”
  - column:Books/Supplies (2): 2000 ⟵ “Books/Supplies | 2000 | 2000”
  - column:Personal/Transportation (2): 3716 ⟵ “Personal/Transportation | 3716 | 3716”
  - column:Average Loan Fees (2): 270 ⟵ “Average Loan Fees | 270 | 270”
  - column:Total (2): 23675 ⟵ “Total | 23675 | 31956”
  - column:Tuition (3): 8070 ⟵ “Tuition | 8070 | 16350”
  - column:Fees (3): 1794 ⟵ “Fees | 1794 | 1794”
  - column:Housing & Food (3): 2965 ⟵ “Housing & Food | 2965 | 2965”
  - column:Books/Supplies (3): 2000 ⟵ “Books/Supplies | 2000 | 2000”
  - column:Personal/Transportation (3): 3468 ⟵ “Personal/Transportation | 3468 | 3468”
  - column:Average Loan Fees (3): 270 ⟵ “Average Loan Fees | 270 | 270”
  - column:Total (3): 18567 ⟵ “Total | 18567 | 26847”
  - column:Tuition (4): 8070 ⟵ “Tuition | 8070 | 16350”
  - column:Fees (4): 4044 ⟵ “Fees | 4044 | 4044”
  - column:Housing & Food (4): 11452 ⟵ “Housing & Food | 11452 | 11452”
  - column:Books/Supplies (4): 2000 ⟵ “Books/Supplies | 2000 | 2000”
  - … 35 more rows
### `5b4bf583f74daf81` Lindenwood University — credit_policies 2025-26 · policy_kind=CLEP [new] (labeled_in_title)
- source: https://www.lindenwood.edu/files/resources/2025-2026-clep-transfer-equivalents.pdf (sha256 4feb6e1c81c9)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 25, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                   50           3           PS 15500       American Government: The Nation   3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                   50           3           GE 11006       GE-Human Culture: Literature      3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature   50           3           GE 11006       GE-Human Culture: Literature      3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                   50           3           ENGL 15000     Composition I                     3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular *         50           3           ENGL 17000     Composition II                    3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                    50           3           GE 11006       GE-Human Culture: Literature      3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language: Level 1              50           semesters) 10200           Elementary French I & II          6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “French Language: Level 2              62           semesters) 20200           Intermediate French I & II        12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language: Level 1              50           semesters) 10200           Elementary German I & II          6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “German Language: Level 2              63           semesters) 20200           Intermediate German I & II        12”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                              50           6             GE 11018        GE-Human Diversity                 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language: Level 1              50            semesters)    10200           Elementary Spanish I & II         6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|66]:  ⟵ “Spanish Language: Level 2              66            semesters)    20200           Intermediate Spanish I & II       12”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting                   50           3           ACCT 21010     Principles of Financial Accounting    3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law              50            3           MGMT 26061 Business Law I                           3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics           50            3           ECON 23030    Principles of Macroeconomics          3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management               50            3           MGMT 26032 Principles of Management                 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing                50            3           MRKT 35010    Principles of Marketing               3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics           50            3           ECON 23020    Principles of Microeconomics          3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology                             50           3            ELECT 20000 Free Elective 20000 Level               3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                50           6            BSC 11000      Principles in Biology                3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                           50            4           MTH 27100       Calculus I                         5”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                          50            6           CHM 23000       General Chemistry I                3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                    50            3           MTH 15100       College Algebra                    3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics                50            6           GE 11015        GE-Math                            3”
  - … 4 more rows
### `9f2153c6d81d318a` Lindenwood University — credit_policies 2025-26 · policy_kind=IB [new] (labeled_in_title)
- source: https://www.lindenwood.edu/files/resources/2025-2026-international-baccalaureate-exam.pdf (sha256 2f81acf3c2a4)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 16, "equivalencies": 16, "rows_without_score": 0}
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4]:  ⟵ “English A: Language and Literature            4      ENGL 15000         Composition I                                  3”
  - equivalencies[IB-ENGLISH-A-LITERATURE|4]:  ⟵ “English A: Literature                         4      GE 11006           GE-Human Culture: Literature                   3”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French                                        4      FRE 10100          Elementary French I                            3”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography                                     4      GEO 10100          World Regional Geography                       3”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German                                        4      GER 10100          Elementary German I                            3”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History                                       4      ELECT 10000        Free Elective 10000 Level                      3”
  - equivalencies[IB-PHILOSOPHY|4]:  ⟵ “Philosophy                                    4      GE 11009           GE-Human Culture: Philosophy                   3”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music                                         4      MUS 16500          Music Appreciation                             3”
  - equivalencies[IB-SPANISH|4]:  ⟵ “Spanish                                       4      SPA 10100          Elementary Spanish I                           3”
  - equivalencies[IB-THEATRE|4]:  ⟵ “Theater Arts                                  4      TA 11700           Introduction to the Theatrical Arts            3”
  - equivalencies[IB-VISUAL-ARTS|4]:  ⟵ “Visual Arts                                   4      AAD 10000          Introduction to Art and Design                 3”
  - equivalencies[IB-BIOLOGY|6]:  ⟵ “Biology                                       6      BSC 11000          Principles in Biology                          3”
  - equivalencies[IB-CHEMISTRY|6]:  ⟵ “Chemistry                                     6      CHM 10500          Chemistry in Society                           3”
  - equivalencies[IB-PHYSICS|6]:  ⟵ “Physics                                       6      PHY 11100          Concepts of Physics                            3”
  - equivalencies[IB-PSYCHOLOGY|6]:  ⟵ “Psychology                                    6      PSY 10000          Principles of Psychology                       3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|6]:  ⟵ “Social Anthropology                           6      ELECT 10000        Free Elective 10000 Level                      3”
### `e31f4b49a1f5153e` Lindenwood University — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_title)
- source: https://www.lindenwood.edu/files/resources/2025-2026-ap-credits.pdf (sha256 a42164bb8a79)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 9, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[AP-RESEARCH|3]:  ⟵ “Research                                 3, 4 or 5 ELECT 10000 Free Elective 10000 Level                                3”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “Seminar                                  3, 4 or 5 ELECT 10000 Free Elective 10000 Level                                3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                    3      BSC 11000      Principles in Biology                3”
  - equivalencies[AP-BIOLOGY|4 or 5]:  ⟵ “Biology                                  4 or 5   BSC 10000      Concepts in Biology                  4”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                3      MTH 15200      Pre-Calculus: Elementary Functions   3”
  - equivalencies[AP-CALCULUS-AB|4 or 5]:  ⟵ “Calculus AB                              4 or 5   MTH 27100      Calculus I                           5”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                                3      MTH  27100     Calculus I                           5”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “Calculus BC                              4 or 5   MTH 27200      Calculus I & II                      10”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                  3      CHM 10500      Chemistry in Society                  3”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “Chemistry                                4 or 5   CHM  23000     General Chemistry 1                   3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                      3      CHM 11100      Environmental Science                 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4 or 5]:  ⟵ “Environmental Science                    4 or 5   BSC 11200      Environmental Biology                 4”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “PreCalculus                                3      MTH 15100      College Algebra                       3”
  - equivalencies[AP-PRECALCULUS|4 or 5]:  ⟵ “PreCalculus                              4 or 5   MTH 15200      Pre-Calculus: Elementary Functions    3”
  - equivalencies[AP-STATISTICS|4 or 5]:  ⟵ “Statistics                               4 or 5   MTH 14100      Basic Statistics                      3”
### `6675ceae1ec0677d` Logan University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.logan.edu/__l5e/assets-v1/27182504-83f2-42a9-aa61-a46cfff32648/Student-Budget-Template.xlsx (sha256 2a366e9cf6e8)
- issues: arrangement_unlabeled, multiple_total_rows
- checks: {"columns": 4, "rows": 6}
  - column:Total: 0 ⟵ “Total | 0”
  - column:Total (2): 0 ⟵ “Total | 0”
  - column:Total (3): 0 ⟵ “Total | 0”
  - column:Total (4): 0 ⟵ “Total | 0”
  - column:Total (5): 0 ⟵ “Total | 0”
  - column:on:: 44869 ⟵ “on: | 44869”
  - column:Employment (Full Time, Part Time): 0 ⟵ “Employment (Full Time, Part Time) | Trimester | 0 | 0 |  | Income:”
  - column:From Student Loans (Net Amount): 0 ⟵ “From Student Loans (Net Amount) | Trimester | 0 | 0 | Income | 0”
  - column:From Scholarships or Grants: 0 ⟵ “From Scholarships or Grants | Trimester | 0 | 0”
  - column:From Work Study (Federal or Non-Federal): 0 ⟵ “From Work Study (Federal or Non-Federal) | Trimester | 0 | 0 | Total Income | 0”
  - column:From Parents: 0 ⟵ “From Parents | Trimester | 0 | 0”
  - column:From Savings: 0 ⟵ “From Savings | Trimester | 0 | 0 | Expenses:”
  - column:Other: 0 ⟵ “Other | Trimester | 0 | 0 | Housing-Related | 0”
  - column:Housing-Related Expenses:: 0 ⟵ “Housing-Related Expenses: | Transportation | 0”
  - column:Rent/Mortgage: 0 ⟵ “Rent/Mortgage | Monthly | 0 | 0 | One-Time | 0”
  - column:Utilities (electric, gas, water, sewer, trash): 0 ⟵ “Utilities (electric, gas, water, sewer, trash) | Monthly | 0 | 0 | Other Expenses | 0”
  - column:Insurance (renter's): 0 ⟵ “Insurance (renter's) | Monthly | 0 | 0”
  - column:TV: 0 ⟵ “TV | Monthly | 0 | 0 | Total Expenses | 0”
  - column:Cell Phone: 0 ⟵ “Cell Phone | Monthly | 0 | 0”
  - column:Internet: 0 ⟵ “Internet | Monthly | 0 | 0 | Remaining: | 0”
  - column:Other (2): 0 ⟵ “Other | Monthly | 0 | 0 | per trimester”
  - column:Tuition and Fees: 0 ⟵ “Tuition and Fees | Trimester | 0 | 0”
  - column:Books (use $40 per class if you don't know): 0 ⟵ “Books (use $40 per class if you don't know) | Trimester | 0 | 0”
  - column:Other (Doctor's bag, iPad): 0 ⟵ “Other (Doctor's bag, iPad) | Trimester | 0 | 0”
  - column:Car Payment: 0 ⟵ “Car Payment | Monthly | 0 | 0”
  - … 61 more rows
### `1ec7d7e3357d7830` Maryville University of Saint Louis — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.maryville.edu/administrative-offices/wp-content/uploads/sites/28/2026/07/CDS_2025-2026_Final_v3.pdf (sha256 c59511f4ff67)
- issues: c1_totals_incomplete
- checks: {"fields": ["act_25", "act_50", "act_75", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 6692 ⟵ “Total first-time, first-year (degree-seeking) who applied                 2910         3089           667             26           6692”
  - enrolled: 835 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                582             216              37              0         835”
  - sat_composite_25..75: [965, 1070, 1165] ⟵ “SAT Composite                                  965                1070               1165”
  - sat_reading_25..75: [490, 530, 615] ⟵ “SAT Evidence-Based Reading and   490                530                615”
  - sat_math_25..75: [465, 510, 590] ⟵ “SAT Math                                        465                510                590”
  - act_25..75: [18, 21, 26] ⟵ “ACT Composite                                   18                 21                 26”
### `ebf6cb370e502c79` Maryville University of Saint Louis — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.maryville.edu/administrative-offices/wp-content/uploads/sites/28/2025/07/CDS_2024-2025_Final.pdf (sha256 68afae06b8a9)
- issues: c1_totals_incomplete, stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - sat_composite_25..75: [963, 1060, 1158] ⟵ “SAT Composite                                 963                  1060               1158”
  - sat_reading_25..75: [480, 530, 590] ⟵ “SAT Evidence-Based Reading and   480                  530                 590”
  - sat_math_25..75: [460, 520, 580] ⟵ “SAT Math                                       460                  520                 580”
  - act_25..75: [18, 21, 25] ⟵ “ACT Composite                                  18                   21                  25”
### `f070f891603899e1` Maryville University of Saint Louis — admissions_metrics 2023-24 [new] (labeled_in_source)
- source: https://www.maryville.edu/administrative-offices/wp-content/uploads/sites/28/2024/07/CDS_2023-2024_Final_v3.pdf (sha256 ff193931f108)
- issues: applications_breakdown_does_not_reconcile, c1_totals_incomplete, stale_year_label:2023-24
- checks: {"fields": ["applications", "enrolled", "entering_fall_year"]}
  - applications: 2 ⟵ “Total first-time, first-year students who applied in Fall 2023          1,338.0      2,577.0          1.0”
  - enrolled: 2023 ⟵ “Total first-time, first-year students enrolled in Fall 2023          277.0        570.0”
### `me0344db320d14f7` Maryville University of Saint Louis — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://online.maryville.edu/admissions/transfer-admission/ (sha256 0e0077cea3c7)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade", "residency_requirement_credits"], "merged_pages": 2}
  - min_grade: C ⟵ “Generally, if you earn credits with a grade of “C” or better at a regionally accredited institution, they will be accepted as transfer credit.”
  - residency_requirement_credits: 30 ⟵ “Additional credits can be accepted from another four-year institution; however, for the completion of the bachelor’s degree, the last 30 credit hours must be taken at Maryville.”
  - min_grade: C- ⟵ “Here are a couple of guidelines that can help you get a better idea of what to expect: Generally, if you earn 100-level credits with a grade of C- or better at a regionally accredited institution, they will be accepted as transfer credit.”
  - min_grade: C- ⟵ “How will my credits transfer to Maryville University? expand_more Generally, if you earn credits with a grade of C- or better at a regionally accredited institution, they will be accepted as transfer credit.”
  - residency_requirement_credits: 30 ⟵ “Sixty credit hours must be completed at a four-year institution, and the last 30 credit hours must be taken at Maryville.”
### `acb4a4f3dfdbc325` Metropolitan Community College-Kansas City — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mcckc.edu/financial-aid/docs/SAPAppeal.pdf (sha256 41f28542f601)
- issues: semantic_review_required, conflicting_sources:https://www.mcckc.edu/financial-aid/sap.aspx
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal Satisfactory Academic Progress ALL FORMS MUST BE COMPLETED IN BLACK INK OR TYPED.”
  - sentence: sap_appeal ⟵ “SAP Appeal Form: Complete and return this two-page form with the required documentation, indicated below. 2.”
  - sentence: sap_appeal ⟵ “Continued on page 2 Satisfactory Academic Progress (SAP) Appeal Page 1 of 2 Rev. 5/9/2022 MCC Student ID: _________________ 3.”
### `acf79e1b0c17efc2` Metropolitan Community College-Kansas City — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mcckc.edu/financial-aid/sap.aspx (sha256 8b9c53ffe9ab)
- issues: semantic_review_required, conflicting_sources:https://www.mcckc.edu/financial-aid/docs/SAPAppeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appealing failure to meet financial aid satisfactory Academic progress Download Financial Aid Appeal Form (PDF) This form is also available at any MCC campus financial aid office.”
### `e2e62fb04bc2e847` Metropolitan Community College-Kansas City — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.mcckc.edu/financial-aid/ (sha256 357070c4d1bd)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Do you have special circumstances?”
  - sentence: need_based_special_circumstances ⟵ “You may be unable to provide parent information because of unusual circumstances outside of your control.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances may include human trafficking, refugee or asylee status, parental incarceration, parental abandonment, an abusive family environment that threatens the student’s health or safety, or the student being unable to locate their parents.”
### `1366cb81524c3bdd` Metropolitan Community College-Kansas City — awards 2024-25 [new] (labeled_in_heading)
- source: https://www.mcckc.edu/financial-aid/types/scholarships.aspx (sha256 fb35d780088e)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 ⟵ “Chancellor | Up to $1,000 | Up to $500 | 3.5-3.74 cumulative GPA or for new incoming freshman, 3.5-3.74 High School GPA or GED/HiSET equivalent | Cumulative 3.5-3.74 GPA”
  - gpa_requirement: 3.5-3.74 cumulative GPA or for new incoming freshman, 3.5-3.74 High School GPA or GED/HiSET equivalent ⟵ “Chancellor | Up to $1,000 | Up to $500 | 3.5-3.74 cumulative GPA or for new incoming freshman, 3.5-3.74 High School GPA or GED/HiSET equivalent | Cumulative 3.5-3.74 GPA”
  - renewal_requirements: Cumulative 3.5-3.74 GPA ⟵ “Chancellor | Up to $1,000 | Up to $500 | 3.5-3.74 cumulative GPA or for new incoming freshman, 3.5-3.74 High School GPA or GED/HiSET equivalent | Cumulative 3.5-3.74 GPA”
### `410bb17dd5d42c45` Metropolitan Community College-Kansas City — awards 2024-25 [new] (labeled_in_heading)
- source: https://www.mcckc.edu/financial-aid/types/scholarships.aspx (sha256 fb35d780088e)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: Up to $750 ⟵ “President | Up to $750 | Up to $375 | 3.0-3.49 cumulative GPA or for new incoming freshman, 3.0-3.49 High School GPA or GED/HiSET equivalent | Cumulative 3.0-3.49 GPA”
  - gpa_requirement: 3.0-3.49 cumulative GPA or for new incoming freshman, 3.0-3.49 High School GPA or GED/HiSET equivalent ⟵ “President | Up to $750 | Up to $375 | 3.0-3.49 cumulative GPA or for new incoming freshman, 3.0-3.49 High School GPA or GED/HiSET equivalent | Cumulative 3.0-3.49 GPA”
  - renewal_requirements: Cumulative 3.0-3.49 GPA ⟵ “President | Up to $750 | Up to $375 | 3.0-3.49 cumulative GPA or for new incoming freshman, 3.0-3.49 High School GPA or GED/HiSET equivalent | Cumulative 3.0-3.49 GPA”
### `ff3975ab9be9f181` Metropolitan Community College-Kansas City — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.mcckc.edu/admissions/credit-by-exam.aspx (sha256 a30e14acf90b)
- issues: rows_without_score
- checks: {"distinct_exams": 35, "equivalencies": 35, "rows_without_score": 35}
  - equivalencies[AP-2-D-ART-DESIGN|None]:  ⟵ “AP | AS2D | 2D Art and Design Portfolio | 3 | 001030 | ART | 100 | Art Fundamentals I | 3”
  - equivalencies[AP-3-D-ART-DESIGN|None]:  ⟵ “AP | AS3D | 3D Art and Design Portfolio | 3 | 001030 | ART | 100 | Art Fundamentals I | 3”
  - equivalencies[AP-DRAWING|None]:  ⟵ “AP | ASD | Drawing Portfolio | 3 | 001037 | ART | 110 | Drawing I | 3”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “AP | BIOL | Biology | 3 | 001002 | BIOL | 101 | General Biology | 5”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “AP | CALAB | Calculus AB | 3 | 001761 | MATH | 180 | Analytic Geometry & Calculus I | 5”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “AP | CALBC | Calculus BC | 3 | 001761 | MATH | 180 | Analytic Geometry & Calculus I | 5”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|None]:  ⟵ “AP | CGPOL | Comparative Govt/Politics | 3 | 006678 | POLS | 135X | Intro Pol Sci-Non MO Const | 3”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “AP | CHEM | Chemistry | 3 | 001317 | CHEM | 111 | General College Chemistry I | 5”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “AP | CHIN | Chinese Language & Culture | 3 | 007744 | CHIN | 101E | Foreign Language Elective | 5”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “AP | CSA | Computer Science A | 3 | 007269 | CSIS | 123 | Programming Fundamentals | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “AP | CSP | Computer Science Principles | 3 | 007269 | CSIS | 123 | Programming Fundamentals | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “AP | ENGC | English Lang & Comp | 3 | 001007 | ENGL | 101 | Composition & Reading I | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “AP | ELITC | English Lit & Comp | 3 | 001428 | ENGL | 218 | Intro to Literature | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “AP | EHIST | European History | 3 | 001749 | HIST | 134 | Modern Western Civilization | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “AP | FRLN | French Language | 3 | 001499 | FREN | 101 | Elementary French I | 5”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “AP | GERMN | German Language | 3 | 001510 | GERM | 101 | Elementary German | 5”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “AP | HGEOG | Human Geography | 3 | 001562 | GEOG | 113 | Cultural/Human Geography | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “AP | ITAL | Italian Language and Culture | 3 | 006363 | FNGL | 1XX | Foreign Language Elective | 5”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “AP | JAPN | Japanese Language & Culture | 3 | 006363 | FNGL | 1XX | Foreign Language Elective | 5”
  - equivalencies[AP-LATIN|None]:  ⟵ “AP | LATIN | Latin (Lit & Vergil) | 3 | 006363 | FNGL | 1XX | Foreign Language Elective | 5”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “AP | EMA | Macroeconomics | 3 | 001197 | ECON | 210 | Macroeconomics | 3”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “AP | EMI | Microeconomics | 3 | 001199 | ECON | 211 | Microeconomics | 3”
  - equivalencies[AP-PHYSICS-1|None]:  ⟵ “AP | PHYS1 | Physics 1 | 3 | 003117 | PHYS | 130 | General Physics I | 3”
  - equivalencies[AP-PHYSICS-2|None]:  ⟵ “AP | PHYS2 | Physics 2 | 3 | 003117 | PHYS | 131 | General Physics II | 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|None]:  ⟵ “AP | PHCM | Physics C - Mech | 3 | 001914 | PHYS | 220 | Engineering Physics I | 5”
  - … 10 more rows
### `663f39c59a3dbcb5` Midwestern Baptist Theological Seminary — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mbts.edu/admissions-tuition/cost-and-aid/cost-of-attendance/ (sha256 d39b7d58b86d)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - column:Tuition & Fees: 10790 ⟵ “Tuition & Fees | $10,790”
  - column:Housing & Food: 10668 ⟵ “Housing & Food | $10,668”
  - column:Books & Supplies: 1016 ⟵ “Books & Supplies | $1,016”
  - column:Personal & Misc: 1286 ⟵ “Personal & Misc | $1,286”
  - column:Transportation: 2934 ⟵ “Transportation | $2,934”
  - column:Total: 26763 ⟵ “Total | $26,763”
### `40bcfd72e32bd0ee` Mineral Area College — appeals 2026-27 [new] (labeled_in_source)
- source: https://mineralarea.edu/future-students/financial-aid/ (sha256 d58410a2acc1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If you have special circumstances that will impact your current income (i.e., change in jobs; lay off from employment; high medical/dental bills not covered by insurance; loss of income) please notify the Financial Aid Office to request a Professional Judgment recalculation.”
### `3fe6cd9fdb60db28` Missouri Baptist University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mobap.edu/tuition-financial-aid/financial-aid-resources/ (sha256 fb1f40ae3645)
- issues: semantic_review_required, conflicting_sources:https://www.mobap.edu/resources/sap-satisfactory-academic-progress-forms/,https://www.mobap.edu/tuition-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Form Request Request digital forms from the Financial Aid Office View Resource SAP (Satisfactory Academic Progress) Forms SAP Appeal Form and Resources View Resource FAQ Quick answers to financial aid questions.”
### `4e0cd61ac724e4d5` Missouri Baptist University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mobap.edu/tuition-financial-aid/ (sha256 4fa72fb9f9f3)
- issues: semantic_review_required, conflicting_sources:https://www.mobap.edu/resources/sap-satisfactory-academic-progress-forms/,https://www.mobap.edu/tuition-financial-aid/financial-aid-resources/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “View Resource Financial Aid Form Request Request digital forms from the Financial Aid Office View Resource SAP (Satisfactory Academic Progress) Forms SAP Appeal Form and Resources View Resource FAFSA Verification Forms Forms for each type of information you are required to verify from your FAFSA.”
### `b12b20b7967bf497` Missouri Baptist University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mobap.edu/resources/sap-satisfactory-academic-progress-forms/ (sha256 a85d1a9cf416)
- issues: semantic_review_required, conflicting_sources:https://www.mobap.edu/tuition-financial-aid/,https://www.mobap.edu/tuition-financial-aid/financial-aid-resources/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Academic Plan These additional resources may be helpful to understanding the Satisfactory Academic Progress rules of MBU and the federal government.”
### `f03e43edd3baa410` Missouri University of Science and Technology — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://futurestudents.mst.edu/admissions/transfer/credit-by-exam/ (sha256 1e1a3fe70832)
- issues: rows_without_score
- checks: {"distinct_exams": 22, "equivalencies": 23, "rows_without_score": 23}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “American Government | 3 | Political Science 1200”
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “American Literature | 6 | English 1221 & 1222”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “Biology | 3 | Biological Sciences 1113”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | 4 | Math 1214”
  - equivalencies[CLEP-CHEMISTRY|None]:  ⟵ “Chemistry | 5 | Chemistry 1310 & 1319”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “College Algebra | 3 | Math 1140”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | 3 | English 1120”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|None]:  ⟵ “College Mathematics | 3 | Math 1110”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature | 6 | English 1211 & 1212”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|None]:  ⟵ “Financial Accounting | 3 | Business 1210”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|None]:  ⟵ “Human Growth & Development | 3 | Psychology 3310”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introduction to Educ Psychology | 3 | Psychology 2300”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “Introductory Business Law | 3 | Business 2910”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introductory Psychology | 3 | Psychology 1101”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Introductory Sociology | 3 | Social Science Elective”
  - equivalencies[CLEP-NATURAL-SCIENCES|None]:  ⟵ “Natural Sciences | 3 | Biological Sciences 1113”
  - equivalencies[CLEP-PRECALCULUS|None]:  ⟵ “Precalculus | 5 | Math 1140 & 1160”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “Principles of Macroeconomics | 3 | Economics 1200”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|None]:  ⟵ “Principles of Management | 3 | Business 1110”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|None]:  ⟵ “Principles of Marketing | 3 | Marketing 3110”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | 3 | Economics 1100”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|None]:  ⟵ “Western Civilization I (Ancient Near East to 1648) | 3 | History 1100”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|None]:  ⟵ “Western Civilization II (1648 to Present) | 3 | History 1200”
### `54ea7949f9d3acab` Missouri Valley College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.moval.edu/wp-content/uploads/2026/06/26-27-Dependency-Status-Appeal-1.pdf (sha256 b89cf08e9661)
- issues: semantic_review_required, conflicting_sources:https://www.moval.edu/wp-content/uploads/2026/06/26-27-Dependency-Status-Appeal-Renewal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “FINANCIAL AID OFFICE 500 East College Street Marshall, MO 65340 (660) 831-4049 | Fax: (660) 831-4003 financialaid@moval.edu 2026-2027 DEPENDENCY STATUS APPEAL In order for the Financial Aid Office to consider your request for a “Dependency Override/Dependency Status Appeal” you must complete this form and provide the following documentation: 1.”
  - sentence: dependency_override ⟵ “A personal letter of appeal explaining the reason for your request for a dependency override.”
  - sentence: dependency_override ⟵ “Housing (rent/mortgage) $ Child Care $ Food $ Utilities $ Credit Card(s) $ Medical/Dental $ Clothing $ Auto (car payments, insurance, maintenance) $ Other personal expenses $ Total Monthly Expenses $ Total Monthly Expenses x 12 $ per year SIGNATURE - REQUIRED I certify that all of the information listed on this form concerning my request for a “Dependency Override” is correct and complete.”
### `7949445e5cb06aa7` Missouri Valley College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.moval.edu/wp-content/uploads/2026/06/26-27-Dependency-Status-Appeal-Renewal.pdf (sha256 572148dc752a)
- issues: semantic_review_required, conflicting_sources:https://www.moval.edu/wp-content/uploads/2026/06/26-27-Dependency-Status-Appeal-1.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “FINANCIAL AID OFFICE 500 East College Street Marshall, MO 65340 (660) 831-4237 | Fax: (660) 831-4003 financialaid@moval.edu 2026-2027 DEPENDENCY STATUS APPEAL RENEWAL Please print clearly.”
  - sentence: dependency_override ⟵ “Date of Birth Phone Number In order for the Financial Aid Office to consider your request for your “Dependency Override” to be renewed for the 2026-2027 award year, you must complete and submit all required documents as listed below: 1.”
  - sentence: dependency_override ⟵ “SIGNATURE - REQUIRED I certify that all of the information listed on this form concerning my request for a “Dependency Override” is correct and complete.”
### `a9231a4bb9bbed99` Missouri Valley College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.moval.edu/admissions-financial-aid/international-students/ (sha256 cbdc05b2a6dc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students are required to notify the International Office of any changes that may affect the Form I-20, including, but not limited to: Change of academic major Change of degree level Inability to complete the program by the listed end date Change in financial support, sponsor, or funding source Any other significant change to the academic program The International Office will review the information”
### `aefcc494c07ab701` Missouri Valley College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.moval.edu/wp-content/uploads/2026/06/26-27-Special-Circumstance-1.pdf (sha256 ffb9f1440afd)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The timeframe for completion is based on the volume of applications received. *Be aware that a Professional Judgement is performed at the discretion of each insti- tution and does not guarantee an increase or change in financial aid at MVC or another institution.”
### `bf7b5bd856e11b54` Missouri Valley College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.moval.edu/wp-content/uploads/2026/06/26-27-Special-Circumstance-1.pdf (sha256 ffb9f1440afd)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “FINANCIAL AID OFFICE 500 East College Street Marshall, MO 65340 (660) 831-4237 | Fax: (660) 831-4003 financialaid@moval.edu SPECIAL CIRCUMSTANCE FORM 2026-2027 Missouri Valley College strives to offer our families the best financial aid packages possible within the limitations of federal, state and college funding levels.”
  - sentence: need_based_special_circumstances ⟵ “If your FAFSA is selected for federal verification, you must complete that process before your special circumstance appeal form can be reviewed.”
### `42adb478f91f390b` Missouri Valley College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.moval.edu/admissions-financial-aid/tuition-financial-aid/cost-of-attendance/ (sha256 dcbae27a87bf)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 22500 ⟵ “Tuition | $22,500 | $22,500”
  - on_campus:Enrollment Fee: 200 ⟵ “Enrollment Fee | $200 | $200”
  - on_campus:Fees: 2000 ⟵ “Fees | $2,000 | $2,000”
  - on_campus:Room: 6000 ⟵ “Room | $6,000 | Estimated: $8,420”
  - on_campus:Board: 5800 ⟵ “Board | $5,800”
  - on_campus:Books/Supplies: 2000 ⟵ “Books/Supplies | $2,000 | $2,000”
  - on_campus:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,910”
  - on_campus:Miscellaneous Expenses: 2400 ⟵ “Miscellaneous Expenses | $2,400 | $2,400”
  - on_campus:Total: 43300 ⟵ “Total | $43,300 | $40,430”
  - with_parents_or_family:Tuition: 22500 ⟵ “Tuition | $22,500 | $22,500”
  - with_parents_or_family:Enrollment Fee: 200 ⟵ “Enrollment Fee | $200 | $200”
  - with_parents_or_family:Fees: 2000 ⟵ “Fees | $2,000 | $2,000”
  - with_parents_or_family:Books/Supplies: 2000 ⟵ “Books/Supplies | $2,000 | $2,000”
  - with_parents_or_family:Transportation: 2910 ⟵ “Transportation | $2,400 | $2,910”
  - with_parents_or_family:Miscellaneous Expenses: 2400 ⟵ “Miscellaneous Expenses | $2,400 | $2,400”
  - with_parents_or_family:Total: 40430 ⟵ “Total | $43,300 | $40,430”
### `79b4eb70cb4e55b3` Missouri Valley College — costs 2022-23 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.moval.edu/admissions-financial-aid/tuition-financial-aid/cost-of-attendance/ (sha256 dcbae27a87bf)
- issues: components_do_not_reconcile, stale_year_label:2022-23
- checks: {"columns": 2, "components_reconcile": false, "rows": 7}
  - on_campus:Tuition: 20850 ⟵ “Tuition | $20,850 | $20,850”
  - on_campus:Fees: 1600 ⟵ “Fees | $1,600 | $1,600”
  - on_campus:Board: 4900 ⟵ “Board | $4,900”
  - on_campus:Books/Supplies: 2000 ⟵ “Books/Supplies | $2,000 | $2,000”
  - on_campus:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,910”
  - on_campus:Miscellaneous Expenses: 2400 ⟵ “Miscellaneous Expenses | $2,400 | $2,400”
  - on_campus:Total: 39550 ⟵ “Total | $39,550 | $38,180”
  - with_parents_or_family:Tuition: 20850 ⟵ “Tuition | $20,850 | $20,850”
  - with_parents_or_family:Fees: 1600 ⟵ “Fees | $1,600 | $1,600”
  - with_parents_or_family:Books/Supplies: 2000 ⟵ “Books/Supplies | $2,000 | $2,000”
  - with_parents_or_family:Transportation: 2910 ⟵ “Transportation | $2,400 | $2,910”
  - with_parents_or_family:Miscellaneous Expenses: 2400 ⟵ “Miscellaneous Expenses | $2,400 | $2,400”
  - with_parents_or_family:Total: 38180 ⟵ “Total | $39,550 | $38,180”
### `a53e79b51eae8d7f` Missouri Valley College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.moval.edu/admissions-financial-aid/tuition-financial-aid/cost-of-attendance/ (sha256 dcbae27a87bf)
- issues: stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 22000 ⟵ “Tuition | $22,000 | $22,000”
  - on_campus:Enrollment Fee: 200 ⟵ “Enrollment Fee | $200 | $200”
  - on_campus:Fees: 1700 ⟵ “Fees | $1,700 | $1,700”
  - on_campus:Room: 5500 ⟵ “Room | $5,500 | Estimated: $8,420”
  - on_campus:Board: 5800 ⟵ “Board | $5,800”
  - on_campus:Books/Supplies: 2000 ⟵ “Books/Supplies | $2,000 | $2,000”
  - on_campus:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,910”
  - on_campus:Miscellaneous Expenses: 2400 ⟵ “Miscellaneous Expenses | $2,400 | $2,400”
  - on_campus:Total: 42000 ⟵ “Total | $42,000 | $39,630”
  - with_parents_or_family:Tuition: 22000 ⟵ “Tuition | $22,000 | $22,000”
  - with_parents_or_family:Enrollment Fee: 200 ⟵ “Enrollment Fee | $200 | $200”
  - with_parents_or_family:Fees: 1700 ⟵ “Fees | $1,700 | $1,700”
  - with_parents_or_family:Books/Supplies: 2000 ⟵ “Books/Supplies | $2,000 | $2,000”
  - with_parents_or_family:Transportation: 2910 ⟵ “Transportation | $2,400 | $2,910”
  - with_parents_or_family:Miscellaneous Expenses: 2400 ⟵ “Miscellaneous Expenses | $2,400 | $2,400”
  - with_parents_or_family:Total: 39630 ⟵ “Total | $42,000 | $39,630”
### `c9591dc6b55156fa` Missouri Valley College — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.moval.edu/admissions-financial-aid/tuition-financial-aid/cost-of-attendance/ (sha256 dcbae27a87bf)
- issues: components_do_not_reconcile, stale_year_label:2023-24
- checks: {"columns": 2, "components_reconcile": false, "rows": 9}
  - on_campus:Tuition: 21300 ⟵ “Tuition | $21,300 | $21,300”
  - on_campus:Enrollment Fee: 200 ⟵ “Enrollment Fee | $200 | $200”
  - on_campus:Fees: 1700 ⟵ “Fees | $1,700 | $1,700”
  - on_campus:Room: 5500 ⟵ “Room | $5,500 | Estimated: $8,420”
  - on_campus:Board: 5000 ⟵ “Board | $5,000”
  - on_campus:Books/Supplies: 2000 ⟵ “Books/Supplies | $2,000 | $2,000”
  - on_campus:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,910”
  - on_campus:Miscellaneous Expenses: 2400 ⟵ “Miscellaneous Expenses | $2,400 | $2,400”
  - on_campus:Total: 39550 ⟵ “Total | $39,550 | $38,180”
  - with_parents_or_family:Tuition: 21300 ⟵ “Tuition | $21,300 | $21,300”
  - with_parents_or_family:Enrollment Fee: 200 ⟵ “Enrollment Fee | $200 | $200”
  - with_parents_or_family:Fees: 1700 ⟵ “Fees | $1,700 | $1,700”
  - with_parents_or_family:Books/Supplies: 2000 ⟵ “Books/Supplies | $2,000 | $2,000”
  - with_parents_or_family:Transportation: 2910 ⟵ “Transportation | $2,400 | $2,910”
  - with_parents_or_family:Miscellaneous Expenses: 2400 ⟵ “Miscellaneous Expenses | $2,400 | $2,400”
  - with_parents_or_family:Total: 38180 ⟵ “Total | $39,550 | $38,180”
### `9a897a6126e2017a` Missouri Western State University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.missouriwestern.edu/finaid/ (sha256 075c16ea3ef4)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Step-by-step Application Process Complete the FAFSA Special Circumstances Calculating Financial Need Aid Opportunities Many opportunities for assistance are available to students who apply.”
### `18b75bb5b513cdc7` Ozark Christian College — appeals 2026-27 [new] (source_unlabeled)
- source: https://occ.edu/tuition-aid/professional-judgment-information (sha256 aed28a048d59)
- issues: semantic_review_required, conflicting_sources:https://occ.edu/tuition-aid,https://occ.edu/tuition-aid
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Students with special or unusual circumstances may choose to submit a Professional Judgment (PJ) appeal to the Office of Student Financial Services requesting their situation be reviewed.”
  - sentence: professional_judgment ⟵ “OCC’s financial aid administrators have the authority to make those determinations by exercising professional judgment (PJ) based on the student's documented circumstance.”
  - sentence: professional_judgment ⟵ “Requesting Professional Judgment Review To request a professional judgment review of a special circumstance (loss of a job, divorce, death of a parent or spouse, etc.) submit the following to Student Financial Services. · Reduction of Income Special Circumstance Form · Letter explaining the reason for the decrease in income and any other information you think would be helpful when reviewing the si”
### `4e7b96ea00f5e790` Ozark Christian College — appeals 2026-27 [new] (source_unlabeled)
- source: https://occ.edu/tuition-aid (sha256 42633dbc88c0)
- issues: semantic_review_required, conflicting_sources:https://occ.edu/tuition-aid,https://occ.edu/tuition-aid/professional-judgment-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment Information New Regulations Loan Reduction for Less-Than-Full-Time Enrollment The One Big Beautiful Bill Act [PDF] was signed into law on July 4, 2025.”
### `74928ef5eba38201` Ozark Christian College — appeals 2026-27 [new] (source_unlabeled)
- source: https://occ.edu/tuition-aid/satisfactory-academic-progress-policy (sha256 064a039e39c6)
- issues: semantic_review_required, conflicting_sources:https://occ.edu/tuition-aid/professional-judgment-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals must be based on unusual circumstances such as long-term illness, death or illness of a family member, etc.”
### `8cbeb670b853cc17` Ozark Christian College — appeals 2026-27 [new] (source_unlabeled)
- source: https://occ.edu/tuition-aid/professional-judgment-information (sha256 aed28a048d59)
- issues: semantic_review_required, conflicting_sources:https://occ.edu/tuition-aid/satisfactory-academic-progress-policy
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances - refers to the financial situations (loss of a job, divorce, death of a parent or spouse, etc.) that justify an aid administrator adjusting data elements in the FAFSA calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances - refers to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration). (This is more commonly referred to as a “Dependency Override.") NOTE: It is possible a student could have circumstances that are both special and”
### `9ac52693853cb356` Ozark Christian College — appeals 2026-27 [new] (source_unlabeled)
- source: https://occ.edu/tuition-aid/satisfactory-academic-progress-policy (sha256 064a039e39c6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Eligibility will be reinstated by achieving both the qualitative and quantitative standards of this policy or by appealing his/her satisfactory academic progress status and the appeal is approved.”
### `bd51041de76110dd` Ozark Christian College — appeals 2026-27 [new] (source_unlabeled)
- source: https://occ.edu/tuition-aid (sha256 3a9d1fccc933)
- issues: semantic_review_required, conflicting_sources:https://occ.edu/tuition-aid,https://occ.edu/tuition-aid/professional-judgment-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment Information New Regulations Loan Reduction for Less-Than-Full-Time Enrollment The One Big Beautiful Bill Act [PDF] was signed into law on July 4, 2025.”
### `b63a1c7225201363` Park University — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_url)
- source: https://www.park.edu/wp-content/uploads/2025/07/2025-2026-AP-List.pdf (sha256 8e85e920a305)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 40, "equivalencies": 40, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies          APAFAM     CBAP0048     3         HIS000               3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History              APARTHIST   CBAP001      3         AR115                3”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design            AP2DAD     CBAP0044     3         AR142                3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design            AP3DAD     CBAP0045     3         AR143                3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                APBIOLOGY   CBAP0003     3          BI101               4”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB              APCALCAB    CBAP0020     3         MA221                4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC               APCALCBC    CBAP0021     3     MA222 & MA000            4/4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                APCHEM     CBAP0004     3                       Score 4 = 8 (earn”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “**Chinese Language & Culture      APCHINLAN   CBAP0033     3         ML000         3=8; 4=12; 5=16”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “^ Comparative Government & Politics APGOVPOL     CBAP0014     3         PO210                3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A            APCOMPSCI   CBAP0041     3         CS000                4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles       APCSPRIN    CBAP0047     3         CS147                3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “^^ Drawing                APDRAW     CBAP0046     3         AR140                3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition      APENGLANG   CBAP0009     3     EN105 & EN000            3/3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition   APENGLIT    CBAP0010     3     EN201 & EN000            3/3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science          APENVSCI    CBAP0035     3          BI111               3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History            APEUHIST    CBAP0016     3         HIS000               6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “**French Language            APFRENCH    CBAP0011     3                        3=6; 4*9; 5=12”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “**German Language             APGERMLAN   CBAP0013     3         ML000         3=6; 4= 9; 5=12”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography              APHUMGEO    CBAP0029     3        GGH110                3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “**Italian Language & Culture     APITALLAN   CBAP0030     3         ML000          3=6; 4=9;5=12”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “**Japanese Language & Culture            APJAPLAN      CBAP0031     3          ML000           3=8;4=12;5=16”
  - equivalencies[AP-LATIN|3]:  ⟵ “**Latin                    APLATLAN      CBAP0018     3          ML000           3=6; 4=9;5=12”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                  APMACRO       CBAP0007     3          EC141                  3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                  APMICRO       CBAP0036     3          EC142                  3”
  - … 15 more rows
### `29bc6e3cf0d39184` Rockhurst University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rockhurst.edu/scholarships/eligibility-scholarship-renewal (sha256 1674cc7da41f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Student Financial Appeals Process A student who fails to make Satisfactory Academic Progress after being on Financial Aid Warning may appeal, in writing, the loss of eligibility.”
### `95bcf0fa950e38ae` Rockhurst University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rockhurst.edu/financialaid/financial-aid-programs-policies (sha256 a82980909053)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Therefore, notification of change in financial circumstances should be made as possible after they occur.”
### `97466e120252bd91` Rockhurst University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.rockhurst.edu/freshman/high-school-college-credit/advanced-placement (sha256 e64d876d6c1b)
- issues: score_column_not_scores
- checks: {"distinct_exams": 9, "equivalencies": 11, "rows_without_score": 0}
  - equivalencies[IB-VISUAL-ARTS|Visual Arts]:  ⟵ “Visual Arts | 5 | 3 | AR1200”
  - equivalencies[IB-HISTORY|History of Europe]:  ⟵ “History of Europe | 5 | 3 | HS 1100 or HS 1500 or HS 1701”
  - equivalencies[IB-HISTORY|History Asia/Oceania]:  ⟵ “History Asia/Oceania | 5 | 3 | HS I attribute”
  - equivalencies[IB-HISTORY|History of the Americas]:  ⟵ “History of the Americas | 5 | 3 | HS 2100 or HS 2500”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 5 | 4 or 8 Depending on placement test | CH 2610/CH2620*And CH 2630/CH 2640* depending on placement test*Placement test and confirmation of lab work required.”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | 5 | 3 | EC 2000”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | 5 | 3 | PY 1000”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|Social Anthropology]:  ⟵ “Social Anthropology | 5 | 3 | SO 1000”
  - equivalencies[IB-FRENCH|French]:  ⟵ “French | 5 | 4 | FR 1100 & FR 1150”
  - equivalencies[IB-GERMAN|German]:  ⟵ “German | 5 | 4 | GR 1100 & GR 1150”
  - equivalencies[IB-SPANISH|Spanish]:  ⟵ “Spanish | 5 | 4 | SP 1100 & SP 1150”
### `2302f02c15a4c0b6` Saint Louis Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://stlcc.edu/docs/financial-aid/26-27-special-circumstances.pdf (sha256 f047e3fde2c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCES 2026-2027 ID # A Name (Last Name) (First Name) (MI) Special Circumstances Notices and Process: The Office of Enrollment Services (Financial Aid) at St.”
  - sentence: need_based_special_circumstances ⟵ “This form allows you to explain unusual circumstances and request a re-evaluation of financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “At any point, additional information can be requested. ▪ If it is determined that you are an eligible applicant with special circumstances, any adjustments made to determine eligibility are valid at this institution only.”
  - sentence: need_based_special_circumstances ⟵ “If you were approved for special circumstances at another institution, you must still submit information and documentation required by St.”
  - sentence: need_based_special_circumstances ⟵ “Department of Education. ▪ It is crucial that students continually check STLCC email for updates and communications regarding this application process. ▪ Special Circumstances approvals do not carry over year to year.”
  - sentence: need_based_special_circumstances ⟵ “If you have an appeal pending, the appeal must be approved first before the special circumstances are reviewed.”
### `a3fcbeb84896eef7` Saint Louis Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://stlcc.edu/docs/financial-aid/26-27-special-circumstances.pdf (sha256 f047e3fde2c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Student Signature Date Home or Cell Phone Number — OFFICE USE ONLY —  Professional Judgement Granted.”
  - sentence: professional_judgment ⟵ “Professional Judgement Denied.”
### `079d138545bd19a4` Saint Louis University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.slu.edu/financial-aid/apply-accept/satisfactory-academic-progress.php (sha256 b21827a8240c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Procedures for Students Terminated from Title IV, State and/or University Scholarship and Award Eligibility A student terminated from receiving federal Title IV/state and/or University scholarship/award programs due to failure to meet the satisfactory academic progress requirements may appeal this termination in accordance with the following guidelines: An Appeal for Termination of Federal ”
### `f78cce384785f7cf` Saint Louis University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.slu.edu/financial-aid/tuition-and-costs/cost-of-attendance.php (sha256 649b2f80a267)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 56960 ⟵ “Tuition | $56,960 | $56,960 | $56,960”
  - on_campus:Fees: 1000 ⟵ “Fees | $1000 | $1000 | $1000”
  - on_campus:Housing - Billable: 15820 ⟵ “Housing - Billable | $15,820 | $600 | $600”
  - on_campus:Housing - Non-billable: 0 ⟵ “Housing - Non-billable | $0 | $15,220 | $6,910”
  - on_campus:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 2986 ⟵ “Transportation | $2,986 | $2,986 | $2,986”
  - on_campus:Miscellaneous: 2880 ⟵ “Miscellaneous | $2,880 | $2,880 | $2,880”
  - on_campus:Loan Fees: 66 ⟵ “Loan Fees | $66 | $66 | $66”
  - on_campus:Total Cost of Attendance: 81002 ⟵ “Total Cost of Attendance | $81,002 | $81,002 | $72,692”
  - off_campus_not_with_family:Tuition: 56960 ⟵ “Tuition | $56,960 | $56,960 | $56,960”
  - off_campus_not_with_family:Fees: 1000 ⟵ “Fees | $1000 | $1000 | $1000”
  - off_campus_not_with_family:Housing - Billable: 600 ⟵ “Housing - Billable | $15,820 | $600 | $600”
  - off_campus_not_with_family:Housing - Non-billable: 15220 ⟵ “Housing - Non-billable | $0 | $15,220 | $6,910”
  - off_campus_not_with_family:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 2986 ⟵ “Transportation | $2,986 | $2,986 | $2,986”
  - off_campus_not_with_family:Miscellaneous: 2880 ⟵ “Miscellaneous | $2,880 | $2,880 | $2,880”
  - off_campus_not_with_family:Loan Fees: 66 ⟵ “Loan Fees | $66 | $66 | $66”
  - off_campus_not_with_family:Total Cost of Attendance: 81002 ⟵ “Total Cost of Attendance | $81,002 | $81,002 | $72,692”
  - with_parents_or_family:Tuition: 56960 ⟵ “Tuition | $56,960 | $56,960 | $56,960”
  - with_parents_or_family:Fees: 1000 ⟵ “Fees | $1000 | $1000 | $1000”
  - with_parents_or_family:Housing - Billable: 600 ⟵ “Housing - Billable | $15,820 | $600 | $600”
  - with_parents_or_family:Housing - Non-billable: 6910 ⟵ “Housing - Non-billable | $0 | $15,220 | $6,910”
  - with_parents_or_family:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 2986 ⟵ “Transportation | $2,986 | $2,986 | $2,986”
  - with_parents_or_family:Miscellaneous: 2880 ⟵ “Miscellaneous | $2,880 | $2,880 | $2,880”
  - … 2 more rows
### `5fe70e7e5f91b80f` Saint Louis University — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.slu.edu/academic-policies/office-admission/undergraduate/credit-for-prior-learning/ (sha256 5df989be16c8)
- issues: conflicting_sources:https://catalog.slu.edu/academic-policies/academic-policies-procedures/credit-exam/
- checks: {"distinct_exams": 31, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4]:  ⟵ “African American Studies | African American Studies | AAM 2000 | 4 | 3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | Principles of Biology | BIOL 1100 | 4 | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | General Chemistry | CHEM 1110, CHEM 1115, CHEM 1120, CHEM 1125 | 5 | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | Chinese Language^ | CHIN 1020 | 3 | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese | Chinese Language^ | CHIN 2010 | 4 | 3”
  - equivalencies[AP-MACROECONOMICS|4 (on both tests)]:  ⟵ “Economics | Principles of Microeconomics & Principles of Macroeconomics | ECON 1900, ECON 1ELE | 4 (on both tests) | 6”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Fine and Performing Arts | Art History | ARTH 1010 | 4 | 3”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Fine and Performing Arts | Studio Art (Drawing) | ART 2000 | 4 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “Fine and Performing Arts | Studio Art (2-D Design) | ART 2100 | 4 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “Fine and Performing Arts | Studio Art (3-D Design) | ART 2120 | 4 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French | French Language^ | FREN 1020 | 3 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French | French Language^ | FREN 2010 | 4 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German | German Language^ | GR 1020 | 3 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German | German Language^ | GR 2010 | 4 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “History | U.S. History | HIST 1600 | 4 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “History | World History | HIST 1120 | 4 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “History | European History | HIST 1120 | 4 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | Italian Lang. & Culture^ | ITAL 1020 | 3 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4]:  ⟵ “Italian | Italian Lang. & Culture^ | ITAL 2010 | 4 | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese | Japanese Language^ | JAP 1ELE | 3 | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4]:  ⟵ “Japanese | Japanese Language^ | JAP 2ELE | 4 | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | Latin Literature^ | LATN 1020 | 3 | 3”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin | Latin Literature^ | LATN 2010 | 4 | 3”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Mathematics | Precalculus | MATH 1400 | 4 | 3”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Mathematics | Calculus AB (or AB subtest of BC)* | MATH 1510 | 4 | 4”
  - … 14 more rows
### `61fc21dd0471f7d5` Saint Louis University — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.slu.edu/academic-policies/office-admission/undergraduate/credit-for-prior-learning/ (sha256 5df989be16c8)
- issues: conflicting_sources:https://catalog.slu.edu/academic-policies/academic-policies-procedures/credit-exam/,https://catalog.slu.edu/academic-policies/office-admission/undergraduate/credit-for-prior-learning/credit-for-prior-learning.pdf
- checks: {"distinct_exams": 23, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[IB-FILM-SL|SL 5]:  ⟵ “The Arts | Film (SL) | FMST 1450 | 5 | 3”
  - equivalencies[IB-FILM-HL|HL 5]:  ⟵ “The Arts | Film (HL) | FMST 1450, CMM 2500 | 5 | 4”
  - equivalencies[IB-MUSIC-HL|HL 5]:  ⟵ “The Arts | Music (HL) | MUSC 1ELE | 5 | 3”
  - equivalencies[IB-THEATRE-HL|HL 5]:  ⟵ “The Arts | Theatre (HL) | THR 1000 | 5 | 3”
  - equivalencies[IB-VISUAL-ARTS-HL|HL 5]:  ⟵ “The Arts | Visual Arts (HL) | ARTH 1000 | 5 | 3”
  - equivalencies[IB-ECONOMICS-HL|HL 5]:  ⟵ “Individuals and societies | Economics (HL) | ECON 1900 | 5 | 3”
  - equivalencies[IB-GEOGRAPHY-HL|HL 5]:  ⟵ “Individuals and societies | Geography (HL) | EAS 1170 | 5 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-HL|HL 6]:  ⟵ “Individuals and societies | Global Politics (HL) | POLS 1600 | 6 | 3”
  - equivalencies[IB-HISTORY-HL|HL 6]:  ⟵ “Individuals and societies | History (HL) | HIST 1ELE | 6 | 6”
  - equivalencies[IB-PHILOSOPHY-HL|HL 6]:  ⟵ “Individuals and societies | Philosophy (HL) | PHIL 1050 | 6 | 3”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 5]:  ⟵ “Individuals and societies | Psychology (HL) | PSY 1010 | 5 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|HL 5]:  ⟵ “Individuals and societies | Social and cultural anthropology (HL) | ANTH 1200 | 5 | 3”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|HL 6]:  ⟵ “Language acquisition | English A Literature (HL) | ENGL 2020 | 6 | 3”
  - equivalencies[IB-FRENCH-HL|HL 4]:  ⟵ “Language acquisition | French Language B^ (HL) | FREN 1010 | 4 | 3”
  - equivalencies[IB-FRENCH-HL|HL 5]:  ⟵ “Language acquisition | French Language B^ (HL) | FREN 1020 | 5 | 3”
  - equivalencies[IB-FRENCH-HL|HL 6]:  ⟵ “Language acquisition | French Language B^ (HL) | FREN 2010 | 6 | 3”
  - equivalencies[IB-GERMAN-HL|HL 4]:  ⟵ “Language acquisition | German Language B^ (HL) | GR 1010 | 4 | 3”
  - equivalencies[IB-GERMAN-HL|HL 5]:  ⟵ “Language acquisition | German Language B^ (HL) | GR 1020 | 5 | 3”
  - equivalencies[IB-GERMAN-HL|HL 6]:  ⟵ “Language acquisition | German Language B^ (HL) | GR 2010 | 6 | 3”
  - equivalencies[IB-LATIN-HL|HL 4]:  ⟵ “Language acquisition | Latin Language B^ (HL) | LATN 1010 | 4 | 3”
  - equivalencies[IB-LATIN-HL|HL 5]:  ⟵ “Language acquisition | Latin Language B^ (HL) | LATN 1020 | 5 | 3”
  - equivalencies[IB-LATIN-HL|HL 6]:  ⟵ “Language acquisition | Latin Language B^ (HL) | LATN 2010 | 6 | 3”
  - equivalencies[IB-SPANISH-HL|HL 4]:  ⟵ “Language acquisition | Spanish Language B^ (HL) | SPAN 1010 | 4 | 3”
  - equivalencies[IB-SPANISH-HL|HL 5]:  ⟵ “Language acquisition | Spanish Language B^ (HL) | SPAN 1020 | 5 | 3”
  - equivalencies[IB-SPANISH-HL|HL 6]:  ⟵ “Language acquisition | Spanish Language B^ (HL) | SPAN 2010 | 6 | 3”
  - … 6 more rows
### `6d0d23e171bb6163` Saint Louis University — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.slu.edu/academic-policies/academic-policies-procedures/credit-exam/ (sha256 1fbecc66c7b7)
- issues: conflicting_sources:https://catalog.slu.edu/academic-policies/office-admission/undergraduate/credit-for-prior-learning/,https://catalog.slu.edu/academic-policies/office-admission/undergraduate/credit-for-prior-learning/credit-for-prior-learning.pdf
- checks: {"distinct_exams": 23, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[IB-FILM-SL|SL 5]:  ⟵ “The Arts | Film (SL) | FMST 1450 | 5 | 3”
  - equivalencies[IB-FILM-HL|HL 5]:  ⟵ “The Arts | Film (HL) | FMST 1450, CMM 2500 | 5 | 4”
  - equivalencies[IB-MUSIC-HL|HL 5]:  ⟵ “The Arts | Music (HL) | MUSC 1ELE | 5 | 3”
  - equivalencies[IB-THEATRE-HL|HL 5]:  ⟵ “The Arts | Theatre (HL) | THR 1000 | 5 | 3”
  - equivalencies[IB-VISUAL-ARTS-HL|HL 5]:  ⟵ “The Arts | Visual Arts (HL) | ARTH 1000 | 5 | 3”
  - equivalencies[IB-ECONOMICS-HL|HL 5]:  ⟵ “Individuals and societies | Economics (HL) | ECON 1900 | 5 | 3”
  - equivalencies[IB-GEOGRAPHY-HL|HL 5]:  ⟵ “Individuals and societies | Geography (HL) | EAS 1170 | 5 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-HL|HL 6]:  ⟵ “Individuals and societies | Global Politics (HL) | POLS 1600 | 6 | 3”
  - equivalencies[IB-HISTORY-HL|HL 6]:  ⟵ “Individuals and societies | History (HL) | HIST 1ELE | 6 | 6”
  - equivalencies[IB-PHILOSOPHY-HL|HL 6]:  ⟵ “Individuals and societies | Philosophy (HL) | PHIL 1050 | 6 | 3”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 5]:  ⟵ “Individuals and societies | Psychology (HL) | PSY 1010 | 5 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|HL 5]:  ⟵ “Individuals and societies | Social and cultural anthropology (HL) | ANTH 1200 | 5 | 3”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|HL 6]:  ⟵ “Language acquisition | English A Literature (HL) | ENGL 2020 | 6 | 3”
  - equivalencies[IB-FRENCH-HL|HL 4]:  ⟵ “Language acquisition | French Language B^ (HL) | FREN 1010 | 4 | 3”
  - equivalencies[IB-FRENCH-HL|HL 5]:  ⟵ “Language acquisition | French Language B^ (HL) | FREN 1020 | 5 | 3”
  - equivalencies[IB-FRENCH-HL|HL 6]:  ⟵ “Language acquisition | French Language B^ (HL) | FREN 2010 | 6 | 3”
  - equivalencies[IB-GERMAN-HL|HL 4]:  ⟵ “Language acquisition | German Language B^ (HL) | GR 1010 | 4 | 3”
  - equivalencies[IB-GERMAN-HL|HL 5]:  ⟵ “Language acquisition | German Language B^ (HL) | GR 1020 | 5 | 3”
  - equivalencies[IB-GERMAN-HL|HL 6]:  ⟵ “Language acquisition | German Language B^ (HL) | GR 2010 | 6 | 3”
  - equivalencies[IB-LATIN-HL|HL 4]:  ⟵ “Language acquisition | Latin Language B^ (HL) | LATN 1010 | 4 | 3”
  - equivalencies[IB-LATIN-HL|HL 5]:  ⟵ “Language acquisition | Latin Language B^ (HL) | LATN 1020 | 5 | 3”
  - equivalencies[IB-LATIN-HL|HL 6]:  ⟵ “Language acquisition | Latin Language B^ (HL) | LATN 2010 | 6 | 3”
  - equivalencies[IB-SPANISH-HL|HL 4]:  ⟵ “Language acquisition | Spanish Language B^ (HL) | SPAN 1010 | 4 | 3”
  - equivalencies[IB-SPANISH-HL|HL 5]:  ⟵ “Language acquisition | Spanish Language B^ (HL) | SPAN 1020 | 5 | 3”
  - equivalencies[IB-SPANISH-HL|HL 6]:  ⟵ “Language acquisition | Spanish Language B^ (HL) | SPAN 2010 | 6 | 3”
  - … 6 more rows
### `a994ba9a2a426c81` Saint Louis University — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.slu.edu/academic-policies/academic-policies-procedures/credit-exam/ (sha256 1fbecc66c7b7)
- issues: conflicting_sources:https://catalog.slu.edu/academic-policies/office-admission/undergraduate/credit-for-prior-learning/
- checks: {"distinct_exams": 33, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4]:  ⟵ “African American Studies | African American Studies | AAM 2000 | 4 | 3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | Principles of Biology | BIOL 1100 | 4 | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | General Chemistry | CHEM 1110, CHEM 1115, CHEM 1120, CHEM 1125 | 5 | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | Chinese Language^ | CHIN 1020 | 3 | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese | Chinese Language^ | CHIN 2010 | 4 | 3”
  - equivalencies[AP-MACROECONOMICS|4 (on both tests)]:  ⟵ “Economics | Principles of Microeconomics & Principles of Macroeconomics | ECON 1900, ECON 1ELE | 4 (on both tests) | 6”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Fine and Performing Arts | Art History | ARTH 1010 | 4 | 3”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Fine and Performing Arts | Studio Art (Drawing) | ART 2000 | 4 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “Fine and Performing Arts | Studio Art (2-D Design) | ART 2100 | 4 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “Fine and Performing Arts | Studio Art (3-D Design) | ART 2120 | 4 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French | French Language^ | FREN 1020 | 3 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French | French Language^ | FREN 2010 | 4 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German | German Language^ | GR 1020 | 3 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German | German Language^ | GR 2010 | 4 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “History | U.S. History | HIST 1600 | 4 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “History | World History | HIST 1120 | 4 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “History | European History | HIST 1120 | 4 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | Italian Lang. & Culture^ | ITAL 1020 | 3 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4]:  ⟵ “Italian | Italian Lang. & Culture^ | ITAL 2010 | 4 | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese | Japanese Language^ | JAP 1ELE | 3 | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4]:  ⟵ “Japanese | Japanese Language^ | JAP 2ELE | 4 | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | Latin Literature^ | LATN 1020 | 3 | 3”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin | Latin Literature^ | LATN 2010 | 4 | 3”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Mathematics | Precalculus | MATH 1400 | 4 | 3”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Mathematics | Calculus AB (or AB subtest of BC)* | MATH 1510 | 4 | 4”
  - … 16 more rows
### `ea4af592ea55c2cc` Saint Louis University — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_title)
- source: https://catalog.slu.edu/academic-policies/office-admission/undergraduate/credit-for-prior-learning/credit-for-prior-learning.pdf (sha256 26ab60ff8e40)
- issues: score_scale_mismatch, conflicting_sources:https://catalog.slu.edu/academic-policies/academic-policies-procedures/credit-exam/,https://catalog.slu.edu/academic-policies/office-admission/undergraduate/credit-for-prior-learning/
- checks: {"distinct_exams": 11, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[IB-BUSINESS-MANAGEMENT|3]:  ⟵ “Business       A Level & AS BIZ 1001 &         A,B         3”
  - equivalencies[IB-GERMAN|6]:  ⟵ “German         A level         GR 1010 &       A,B         6”
  - equivalencies[IB-SPANISH|6]:  ⟵ “Spanish        A level         SPAN 1010 & A,B             6”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology        Principles of   BIOL 1100       4           4”
  - equivalencies[IB-ECONOMICS|6]:  ⟵ “Economics         Principles of ECON 1900,     4 (on both     6   Mathematics Precalculus      MATH 1400     4             3”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “MicroeconomicsECON 1ELE      tests)             Mathematics Calculus         MATH 1510     4             4”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music Theory Aural Skills    MUSC 2271     4             1”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music Theory Music Theory MUSC 2270        4             3”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics       Physics I      PHYS 1220 & 4               4”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics       Physics II     PHYS 1240 & 4               4”
  - equivalencies[IB-FRENCH|3]:  ⟵ “French            French           FREN 1020   3              3”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French            French           FREN 2010   4              3”
  - equivalencies[IB-GERMAN|3]:  ⟵ “German            German           GR 1020     3              3”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German            German           GR 2010     4              3”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History           U.S. History     HIST 1600   4              3”
  - equivalencies[IB-SPANISH|3]:  ⟵ “Spanish       Spanish        SPAN 1020     3             3”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History           World History HIST 1120      4              3”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History           European         HIST 1120   4              3                 Culture^”
  - equivalencies[IB-SPANISH|4]:  ⟵ “Spanish       Spanish        SPAN 2010     4             3”
  - equivalencies[IB-LATIN|3]:  ⟵ “Latin             Latin            LATN 1020   3              3   Business      Financial      ACCT 2200     50            3”
  - equivalencies[IB-BUSINESS-MANAGEMENT|50]:  ⟵ “Business       Information     BTM 2000        50   3   History         Western         HIST 1ELE            50      3”
  - equivalencies[IB-BUSINESS-MANAGEMENT|50]:  ⟵ “Business       Introductory MGT 2000           50   3   Sciences        Ancient Near”
  - equivalencies[IB-BUSINESS-MANAGEMENT|50]:  ⟵ “Business       Principles of MGT 3000          50   3   History         Western          HIST 1ELE           50      3”
  - equivalencies[IB-BUSINESS-MANAGEMENT|50]:  ⟵ “Business       Principles of   MKT 3000        50   3”
  - equivalencies[IB-HISTORY|50]:  ⟵ “History        American        POLS 1100       50   3   World           French          FREN 1010,           50      6”
  - … 7 more rows
### `b15fa29a37f86841` Southeast Missouri State University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://semo.edu/institutional-research/_pdfs/cds-24-25.pdf (sha256 6121af16fd97)
- issues: c1_totals_incomplete, stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - sat_composite_25..75: [1020, 1110, 1210] ⟵ “SAT Composite                             1020               1110             1210”
  - sat_math_25..75: [500, 560, 620] ⟵ “SAT Math                                   500               560              620”
  - act_25..75: [17, 20, 24] ⟵ “ACT Composite                               17                20               24”
### `2e2340535d7627d3` Southeast Missouri State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://semo.edu/student-support/financial-services/_pdfs/sfs-sap-appeal.pdf (sha256 73ad7928a7c0)
- issues: semantic_review_required, conflicting_sources:https://semo.edu/student-support/financial-services/_pdfs/sfs-sap-policy.pdf,https://semo.edu/student-support/financial-services/financial-aid/satisfactory-progress
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “/Unsatisfactory Academic Progress Appeal (Request for Reinstatement of Federal Financial Aid) The Federal Government requires that students who receive federal financial aid maintain Satisfactory Academic Progress (SAP) toward their degree, as outlined in the SAP policy (http://semo.edu/pdf/SFS-SAP-Policy.pdf).”
  - sentence: sap_appeal ⟵ “One University Plaza MS 3740 / Cape Girardeau, MO 63701 sfs@semo.edu / T 573.651.2253 / F 573.651.5006 /Unsatisfactory Academic Progress Appeal (Page 2) (Request for Reinstatement of Federal Financial Aid) 3) CIRCUMSTANCE “A” SUPPLEMENTAL QUESTIONS (discrimination, harassment or retaliation) Yes No Only complete if you marked circumstance “A” (discrimination, harassment or retaliation) in Section ”
### `56d1d49e3a2d389d` Southeast Missouri State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://semo.edu/student-support/financial-services/financial-aid/satisfactory-progress (sha256 fdb2f89f5c26)
- issues: semantic_review_required, conflicting_sources:https://semo.edu/student-support/financial-services/_pdfs/sfs-sap-appeal.pdf,https://semo.edu/student-support/financial-services/_pdfs/sfs-sap-policy.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appealing Unsatisfactory Academic Progress (USAP) All appeals are reviewed by a committee and decision notifications are sent via the student's Southeast email address.”
  - sentence: sap_appeal ⟵ “Appealing for GPA or PACE: If a student loses financial aid eligibility and has extenuating/mitigating circumstances that significantly contributed to their inability to meet the requirements of SAP, they may submit an Unsatisfactory Academic Progress Appeal.”
### `5ebb13984a3ce077` Southeast Missouri State University — appeals 2026-27 [new] (labeled_in_title)
- source: https://semo.edu/student-support/financial-services/financial-aid/se-scholarships-2026 (sha256 adafb1e0af24)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Verification and special circumstances must be completed by July 31.”
### `92acd5a9ea0ab959` Southeast Missouri State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://semo.edu/student-support/financial-services/_pdfs/sfs-sap-policy.pdf (sha256 c4742631e46d)
- issues: semantic_review_required, conflicting_sources:https://semo.edu/student-support/financial-services/_pdfs/sfs-sap-appeal.pdf,https://semo.edu/student-support/financial-services/financial-aid/satisfactory-progress
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “The student will be hours earned by the cumulative number required to use his or her own financial of hours attempted. resources until he or she is again meeting Pace of completion is affected by course Satisfactory Academic Progress standards or incompletes, withdrawals, repetitions and submits a successful appeal. transfer credits.”
  - sentence: sap_appeal ⟵ “The student will be accepts. hours; a minimum 2.00 cumulative GPA is required to use his or her own financial required by the time the student has resources until he or she is again meeting attempted 48 hours or more. (See Satisfactory Academic Progress standards or requirements for Transfer Students). submit a successful appeal.”
  - sentence: sap_appeal ⟵ “The academic plan may be for one semester or several semesters depending on the student’s SAP deficiencies and appeal circumstances.”
  - sentence: sap_appeal ⟵ “SAP APPEAL PROCESS: A student who has been suspended from financial aid may submit an appeal letter and the Appeal Form for Unsatisfactory Academic Progress to the Financial Aid Appeals Committee if extenuating circumstances prevented him or her from meeting the pace, cumulative GPA or maximum timeframe.”
  - sentence: sap_appeal ⟵ “APPEALS FORM: The Unsatisfactory Academic Progress Appeal Form may be found online at http://www.semo.edu/pdf/SFS_sap_appeal.pdf.”
### `c5803676c5c1a4c2` Southwest Baptist University — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_title)
- source: https://www.sbuniv.edu/_resources/documents/dual-credit-handbook-2025.pdf (sha256 a90f22126607)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_hs_gpa"], "tiers": 3}
  - eligibility_tier: 3.0 ⟵ “•   Students in the 11th and 12th grades with an overall minimum grade point average of 3.0”
  - eligibility_tier: 3.0 ⟵ “•   Students in the 10th grade must have an overall minimum grade point average of 3.0,”
  - eligibility_tier: 3.0 ⟵ “•   Students in the 9th grade must have an overall grade point average of 3.0, score at the 90th”
### `3399b0c1c95cc853` State Fair Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.sfccmo.edu/admissions/financial-aid/documents/2026-2027-Special-Circumstance-Request-SPCD27.pdf (sha256 bf2610d9d9de)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances Request(SPCD27) A.”
  - sentence: need_based_special_circumstances ⟵ “TYPE OF SPECIAL CIRCUMSTANCE Family income from the prior tax year is used in determining eligibility for student financial aid in the academic year.”
### `9816674bc7c1167e` State Fair Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.sfccmo.edu/admissions/financial-aid/cost-of-attendance/index.php (sha256 179ccec9e948)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 1, "rows": 20}
  - on_campus:Tuition (15 credits/year): 4305.0 ⟵ “Tuition (15 credits/year) | $4,305.00 | $6,559.00 | $8,814.00”
  - on_campus:Fees Estimate: 1987.0 ⟵ “Fees Estimate | $1,987.00 | $1,987.00 | $1,987.00”
  - on_campus:Housing: 7190.0 ⟵ “Housing | $7,190.00 | $7,190.00 | $7,190.00”
  - on_campus:Food: 5599.0 ⟵ “Food | $5,599.00 | $5,599.00 | $5,599.00”
  - on_campus:Total Direct SFCC Billed Costs: 19081.0 ⟵ “Total Direct SFCC Billed Costs | $19,081.00 | $21,335.00 | $23,590.00”
  - on_campus:Books/Supplies: 397.0 ⟵ “Books/Supplies | $397.00 | $397.00 | $397.00”
  - on_campus:Transportation: 698.0 ⟵ “Transportation | $698.00 | $698.00 | $698.00”
  - on_campus:Loan Fee Estimates: 80.0 ⟵ “Loan Fee Estimates | $80.00 | $80.00 | $80.00”
  - on_campus:Miscellaneous: 2412.0 ⟵ “Miscellaneous | $2,412.00 | $2,412.00 | $2,412.00”
  - on_campus:Total Indirect Costs: 3587.0 ⟵ “Total Indirect Costs | $3,587.00 | $3,587.00 | $3,587.00”
  - on_campus:Tuition (15 credits/year) (2): 4305.0 ⟵ “Tuition (15 credits/year) | $4,305.00 | $6,559.00 | $8,814.00”
  - on_campus:Fees Estimate (2): 1987.0 ⟵ “Fees Estimate | $1,987.00 | $1,987.00 | $1,987.00”
  - on_campus:Total Direct SFCC Billed Costs (2): 6292.0 ⟵ “Total Direct SFCC Billed Costs | $6,292.00 | $8,546.00 | $10,801.00”
  - on_campus:Housing (2): 8544.0 ⟵ “Housing | $8,544.00 | $8,544.00 | $8,544.00”
  - on_campus:Food (2): 7380.0 ⟵ “Food | $7,380.00 | $7,380.00 | $7,380.00”
  - on_campus:Books/Supplies (2): 397.0 ⟵ “Books/Supplies | $397.00 | $397.00 | $397.00”
  - on_campus:Transportation (2): 2132.0 ⟵ “Transportation | $2,132.00 | $2,132.00 | $2,132.00”
  - on_campus:Loan Fee Estimates (2): 80.0 ⟵ “Loan Fee Estimates | $80.00 | $80.00 | $80.00”
  - on_campus:Miscellaneous (2): 2412.0 ⟵ “Miscellaneous | $2,412.00 | $2,412.00 | $2,412.00”
  - on_campus:Total Indirect Costs (2): 20945.0 ⟵ “Total Indirect Costs | $20,945.00 | $20,945.00 | $20,945.00”
### `af193892e0ff4fbd` State Fair Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.sfccmo.edu/admissions/tuition-and-fees/ (sha256 3cdfcd74d165)
- issues: arrangement_unlabeled, conflicting_sources:https://www.sfccmo.edu/admissions/financial-aid/cost-of-attendance/index.php
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - column:Tuition: 3990 ⟵ “Tuition | $3,990 | $6,090”
  - column:Technology Fee: 1350 ⟵ “Technology Fee | $1350 | $1350”
  - column:Books: 1000 ⟵ “Books | $1,000 | $1,000”
  - column:Total: 6340 ⟵ “Total | $6,340 | $8,440”
  - column:Tuition: 6090 ⟵ “Tuition | $3,990 | $6,090”
  - column:Technology Fee: 1350 ⟵ “Technology Fee | $1350 | $1350”
  - column:Books: 1000 ⟵ “Books | $1,000 | $1,000”
  - column:Total: 8440 ⟵ “Total | $6,340 | $8,440”
### `be91ff2b0cf2e345` State Fair Community College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.sfccmo.edu/admissions/financial-aid/cost-of-attendance/index.php (sha256 179ccec9e948)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 20}
  - on_campus:Tuition (15 credits/year): 8814.0 ⟵ “Tuition (15 credits/year) | $4,305.00 | $6,559.00 | $8,814.00”
  - on_campus:Fees Estimate: 1987.0 ⟵ “Fees Estimate | $1,987.00 | $1,987.00 | $1,987.00”
  - on_campus:Housing: 7190.0 ⟵ “Housing | $7,190.00 | $7,190.00 | $7,190.00”
  - on_campus:Food: 5599.0 ⟵ “Food | $5,599.00 | $5,599.00 | $5,599.00”
  - on_campus:Total Direct SFCC Billed Costs: 23590.0 ⟵ “Total Direct SFCC Billed Costs | $19,081.00 | $21,335.00 | $23,590.00”
  - on_campus:Books/Supplies: 397.0 ⟵ “Books/Supplies | $397.00 | $397.00 | $397.00”
  - on_campus:Transportation: 698.0 ⟵ “Transportation | $698.00 | $698.00 | $698.00”
  - on_campus:Loan Fee Estimates: 80.0 ⟵ “Loan Fee Estimates | $80.00 | $80.00 | $80.00”
  - on_campus:Miscellaneous: 2412.0 ⟵ “Miscellaneous | $2,412.00 | $2,412.00 | $2,412.00”
  - on_campus:Total Indirect Costs: 3587.0 ⟵ “Total Indirect Costs | $3,587.00 | $3,587.00 | $3,587.00”
  - on_campus:Tuition (15 credits/year) (2): 8814.0 ⟵ “Tuition (15 credits/year) | $4,305.00 | $6,559.00 | $8,814.00”
  - on_campus:Fees Estimate (2): 1987.0 ⟵ “Fees Estimate | $1,987.00 | $1,987.00 | $1,987.00”
  - on_campus:Total Direct SFCC Billed Costs (2): 10801.0 ⟵ “Total Direct SFCC Billed Costs | $6,292.00 | $8,546.00 | $10,801.00”
  - on_campus:Housing (2): 8544.0 ⟵ “Housing | $8,544.00 | $8,544.00 | $8,544.00”
  - on_campus:Food (2): 7380.0 ⟵ “Food | $7,380.00 | $7,380.00 | $7,380.00”
  - on_campus:Books/Supplies (2): 397.0 ⟵ “Books/Supplies | $397.00 | $397.00 | $397.00”
  - on_campus:Transportation (2): 2132.0 ⟵ “Transportation | $2,132.00 | $2,132.00 | $2,132.00”
  - on_campus:Loan Fee Estimates (2): 80.0 ⟵ “Loan Fee Estimates | $80.00 | $80.00 | $80.00”
  - on_campus:Miscellaneous (2): 2412.0 ⟵ “Miscellaneous | $2,412.00 | $2,412.00 | $2,412.00”
  - on_campus:Total Indirect Costs (2): 20945.0 ⟵ “Total Indirect Costs | $20,945.00 | $20,945.00 | $20,945.00”
### `f71414e3bd8c9547` State Fair Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.sfccmo.edu/admissions/financial-aid/cost-of-attendance/index.php (sha256 179ccec9e948)
- issues: multiple_total_rows, conflicting_sources:https://www.sfccmo.edu/admissions/tuition-and-fees/
- checks: {"columns": 1, "rows": 20}
  - on_campus:Tuition (15 credits/year): 6559.0 ⟵ “Tuition (15 credits/year) | $4,305.00 | $6,559.00 | $8,814.00”
  - on_campus:Fees Estimate: 1987.0 ⟵ “Fees Estimate | $1,987.00 | $1,987.00 | $1,987.00”
  - on_campus:Housing: 7190.0 ⟵ “Housing | $7,190.00 | $7,190.00 | $7,190.00”
  - on_campus:Food: 5599.0 ⟵ “Food | $5,599.00 | $5,599.00 | $5,599.00”
  - on_campus:Total Direct SFCC Billed Costs: 21335.0 ⟵ “Total Direct SFCC Billed Costs | $19,081.00 | $21,335.00 | $23,590.00”
  - on_campus:Books/Supplies: 397.0 ⟵ “Books/Supplies | $397.00 | $397.00 | $397.00”
  - on_campus:Transportation: 698.0 ⟵ “Transportation | $698.00 | $698.00 | $698.00”
  - on_campus:Loan Fee Estimates: 80.0 ⟵ “Loan Fee Estimates | $80.00 | $80.00 | $80.00”
  - on_campus:Miscellaneous: 2412.0 ⟵ “Miscellaneous | $2,412.00 | $2,412.00 | $2,412.00”
  - on_campus:Total Indirect Costs: 3587.0 ⟵ “Total Indirect Costs | $3,587.00 | $3,587.00 | $3,587.00”
  - on_campus:Tuition (15 credits/year) (2): 6559.0 ⟵ “Tuition (15 credits/year) | $4,305.00 | $6,559.00 | $8,814.00”
  - on_campus:Fees Estimate (2): 1987.0 ⟵ “Fees Estimate | $1,987.00 | $1,987.00 | $1,987.00”
  - on_campus:Total Direct SFCC Billed Costs (2): 8546.0 ⟵ “Total Direct SFCC Billed Costs | $6,292.00 | $8,546.00 | $10,801.00”
  - on_campus:Housing (2): 8544.0 ⟵ “Housing | $8,544.00 | $8,544.00 | $8,544.00”
  - on_campus:Food (2): 7380.0 ⟵ “Food | $7,380.00 | $7,380.00 | $7,380.00”
  - on_campus:Books/Supplies (2): 397.0 ⟵ “Books/Supplies | $397.00 | $397.00 | $397.00”
  - on_campus:Transportation (2): 2132.0 ⟵ “Transportation | $2,132.00 | $2,132.00 | $2,132.00”
  - on_campus:Loan Fee Estimates (2): 80.0 ⟵ “Loan Fee Estimates | $80.00 | $80.00 | $80.00”
  - on_campus:Miscellaneous (2): 2412.0 ⟵ “Miscellaneous | $2,412.00 | $2,412.00 | $2,412.00”
  - on_campus:Total Indirect Costs (2): 20945.0 ⟵ “Total Indirect Costs | $20,945.00 | $20,945.00 | $20,945.00”
### `mf28ce017a76a2af` State Fair Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.sfccmo.edu/admissions/dual-credit/documents/26_27__dc_handbook___final__updated.pdf (sha256 e20d8fe052bd)
- issues: multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted"], "merged_pages": 3, "tiers": 6}
  - per_credit_hour_charge: 79 ⟵ “$79 per credit hour”
  - per_credit_hour_charge: 94 ⟵ “$94 per credit hour”
  - state_grant_accepted: True ⟵ “Eligible Missouri high school students may qualify for the Dual Credit/Dual Enrollment Scholarship through the Missouri Department of Higher Education and Workforce Development (MDHEWD).”
  - state_grant_accepted: True ⟵ “Students may be eligible for the Dual Credit/Dual Enrollment Scholarship through DHEWD.”
  - per_credit_hour_charge: 94 ⟵ “Some dual Credit courses may require additional course fees. Locate                   Online Credit Hours:                  @ $94 per credit hour = $”
  - per_credit_hour_charge: 79 ⟵ “the complete list of Dual Credit course fees on the SFCC website.                     Other Credit Hours:                  @ $79 per credit hour = $”
  - eligibility_tier: 3.0 ⟵ “eligibility for dual credit courses is restricted and attest this student meet’s MO DC eligibility criteria including 3.0 GPA and ACT requirements”
  - eligibility_tier: 3.0 ⟵ “for Freshman, 3.0 GPA for Sophomores or 2.5 GPA for Juniors/Seniors.”
  - per_credit_hour_charge: 79 ⟵ “ $79 per credit hour”
  - per_credit_hour_charge: 94 ⟵ “ $94 per credit hour for online classes”
  - state_grant_accepted: True ⟵ “Students may be eligible for the Dual Credit/Dual Enrollment Scholarship through DHEWD.”
  - per_credit_hour_charge: 94 ⟵ “Some dual Credit courses may require additional course fees. Locate                    Online Credit Hours:                 @ $94 per credit hour = $”
  - per_credit_hour_charge: 79 ⟵ “the complete list of Dual Credit course fees on the SFCC website.                      Other Credit Hours:                 @ $79 per credit hour = $”
  - eligibility_tier: 3.0 ⟵ “eligibility for dual credit courses is restricted and attest this student meet’s MO DC eligibility criteria including 3.0 GPA and ACT requirements”
  - eligibility_tier: 3.0 ⟵ “for Freshman, 3.0 GPA for Sophomores or 2.5 GPA for Juniors/Seniors.”
  - eligibility_tier: 3.0 ⟵ “ENGL 101 English                      18 – 36              250 – 300                  480 – 800              92 – 120             cumulative HS GPA 3.0 OR test scores, which                                          51 – 60”
  - eligibility_tier: 3.0 ⟵ “unweighted, cumulative HS GPA of 3.0”
  - eligibility_tier: 3.0 ⟵ “MATH 119 Statistical Reasoning                                                                                                                                     cumulative HS GPA of 3.0”
  - eligibility_tier: 3.0 ⟵ “unweighted GPA        3.0 cumulative,”
### `5ce99de2cb20f39e` State Technical College of Missouri — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://statetechmo.edu/contact-admissions/credit-and-curriculum-transfer/ (sha256 f17a23b730a3)
- issues: ambiguous_year_labels
- checks: {"distinct_exams": 1, "equivalencies": 9, "rows_without_score": 0}
  - equivalencies[AP-CALCULUS-BC|N/A]:  ⟵ “Calculus BC | 3 | N/A | Award General Math Credit | N/A”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | Statistics | 3 | MAT 119 | Elementary Statistics | MATH 110”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | United States History | 3 | HST 105 | American History to 1877 | HST 101”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | Chemistry | 3 | PHY 121 | General Chemistry with Lab I | CHEM 150L”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | Environmental Science | 3 | PHY 103 / 104 | Environmental Science + Lab | PHYS 110LEV”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | Physics I | 3 | PHY 101 / 102 | College Physics + Lab | PHYS 150L”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | Physics C – Mechanics | 3 | PHY 201 | General Physics | PHYS 200L”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | Physics C – Electricity / Magnetism | 3 | N/A | Award General Science Credit | N/A”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | Econ: Microeconomics | 3 | BUS 172 | Principles of Microeconomics | ECON 102”
### `97832e0f34e4bc6e` State Technical College of Missouri — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_heading)
- source: https://statetechmo.edu/contact-admissions/dual-credit-enrollment/information-for-dual-credit-enrollment/ (sha256 5a67f4e78cd3)
- issues: stale_year_label:2024-25
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 88 ⟵ “| $88 per credit hour plus books and course materials”
  - per_credit_hour_charge: 88 ⟵ “| $88 per credit hour plus books and course materials”
### `cddbbb678314923c` State Technical College of Missouri — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://statetechmo.edu/contact-admissions/credit-and-curriculum-transfer/ (sha256 f17a23b730a3)
- issues: ambiguous_year_labels
- checks: {"distinct_exams": 5, "equivalencies": 5, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “MATHEMATICS | College Algebra | 50 | MAT 115 | College Algebra | MAT 130”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “COMMUNICATION | College Composition | 50 | COM 101 | English Composition | ENGL 100”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “SOCIAL SCIENCE | American Government | 50 | PSC 101 | American Government | POSC 101”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “BUSINESS | Principles of Macroeconomics | 50 | BUS 172 | Principles of Macroeconomics | ECON 101”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | Principles of Microeconomics | 50 | BUS 170 | Principles of Microeconomics | ECON 102”
### `085f62cddc675a18` Stephens College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://stephens.edu/admissions-aid/undergraduate-financial-aid/ (sha256 bbf3db17bc49)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://stephens.edu/admissions-aid/special-and-unusual-circumstances/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Forms Special and Unusual Circumstances The Office of Financial Aid understands that students and their families may at times experience unique situations, and, as much as possible, we are here to help!”
  - sentence: need_based_special_circumstances ⟵ “You may pursue a financial aid adjustment based on two categories of unique situations: Special and Unusual Circumstances Tuition & Fees The Office of Financial Aid is always here to help you understand your options for affording your tuition.”
### `36ec1242d806d718` Stephens College — appeals 2026-27 [new] (source_unlabeled)
- source: https://stephens.edu/admissions-aid/special-and-unusual-circumstances/ (sha256 6070322323ad)
- issues: semantic_review_required, conflicting_sources:https://stephens.edu/admissions-aid/undergraduate-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstances - Stephens College Skip to content Visit Give News Events Directory Resources for Prospective Students Faculty & Staff Alumni Current Students Children’s School SearchSearch Menu Close Why Stephens?”
  - sentence: need_based_special_circumstances ⟵ “You may pursue a financial aid adjustment based on two categories of unique situations: Special and Unusual Circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances We recognize that income information presented on the FAFSA may not reflect a family’s current financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Students with documented Special Circumstances that negatively affect their family’s financial situation could be eligible for a financial aid adjustment that could result in additional financial aid.”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances include, but are not limited to: Changes in employment status, income, or assets.”
  - sentence: need_based_special_circumstances ⟵ “You can review the Special Circumstances Forms on our Financial Aid Forms page.”
### `7de5ee3e75ece984` Stephens College — appeals 2026-27 [new] (source_unlabeled)
- source: https://stephens.edu/admissions-aid/special-and-unusual-circumstances/ (sha256 6070322323ad)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Federal regulations allow Stephens College to use professional judgment on a case-by-case basis to determine whether additional aid can be given to a student due to eligible special circumstances that impact their Student Aid Index (SAI).”
### `a22de538ca24fb15` Three Rivers College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://trcc.edu/wp-content/uploads/Tiered-Tuition-2026.pdf (sha256 5a8a5e02fb40)
- issues: arrangement_unlabeled, implausible_amount, multiple_total_rows, residency_unknown
- checks: {"columns": 4, "rows": 13}
  - column:(Base Tuition): 111 ⟵ “(Base Tuition) | $111 | $158 | $59 | $26”
  - column:Tier Two: 115 ⟵ “Tier Two | $115 | $162 | $59 | $26”
  - column:Tier Three: 192 ⟵ “Tier Three | $192 | $239 | $59 | $26”
  - column:Tier Four: 316 ⟵ “Tier Four | $316 | $363 | $59 | $26”
  - column:Tier Five: 959 ⟵ “Tier Five | $959 | $1,006 | $59 | $26”
  - column:trcc.edu: 1 ⟵ “trcc.edu | 1”
  - column:TOTAL: 11 ⟵ “TOTAL | 11 | $1,221”
  - column:TOTAL (2): 13 ⟵ “TOTAL | 13 | $3,288”
  - column:trcc.edu (2): 3 ⟵ “trcc.edu | 3”
  - column:ACCT 211 Principles of: 3 ⟵ “ACCT 211 Principles of | 3 | $345”
  - column:CHEM 111 Introductory: 4 ⟵ “CHEM 111 Introductory | 4 | $444”
  - column:TOTAL (3): 17 ⟵ “TOTAL | 17 | $1,899”
  - column:TOTAL (4): 17 ⟵ “TOTAL | 17 | $4,063”
  - column:(Base Tuition): 158 ⟵ “(Base Tuition) | $111 | $158 | $59 | $26”
  - column:Tier Two: 162 ⟵ “Tier Two | $115 | $162 | $59 | $26”
  - column:Tier Three: 239 ⟵ “Tier Three | $192 | $239 | $59 | $26”
  - column:Tier Four: 363 ⟵ “Tier Four | $316 | $363 | $59 | $26”
  - column:Tier Five: 1006 ⟵ “Tier Five | $959 | $1,006 | $59 | $26”
  - column:BIOL 231: 4 ⟵ “BIOL 231 | Anatomy and | 4 | $444”
  - column:TOTAL: 1221 ⟵ “TOTAL | 11 | $1,221”
  - column:BIOL 231 (2): 4 ⟵ “BIOL 231 | Anatomy and | 4 | $444”
  - column:NURS 116: 9 ⟵ “NURS 116 | Foundations | 9 | $2,844”
  - column:TOTAL (2): 3288 ⟵ “TOTAL | 13 | $3,288”
  - column:ACCT 211 Principles of: 345 ⟵ “ACCT 211 Principles of | 3 | $345”
  - column:CHEM 111 Introductory: 444 ⟵ “CHEM 111 Introductory | 4 | $444”
  - … 22 more rows
### `e38c4e3339b04d47` Three Rivers College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://trcc.edu/pay-for-college/tuition-fees/ (sha256 5a762ee0e86b)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 6, "components_reconcile": false, "rows": 3}
  - column:Tuition & Fees: 5220.0 ⟵ “Tuition & Fees | $5,220.00 | $5,220.00 | $5,220.00 | $6,630.00 | $6,630.00 | $6,630.00”
  - column:Books, course materials, supplies, equipment: 1020.0 ⟵ “Books, course materials, supplies, equipment | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00”
  - column:TOTAL: 20748.0 ⟵ “TOTAL | $20,748.00 | $25,860.00 | $22,998.00 | $22,158.00 | $27,270.00 | $24,408.00”
  - column:Tuition & Fees: 5220.0 ⟵ “Tuition & Fees | $5,220.00 | $5,220.00 | $5,220.00 | $6,630.00 | $6,630.00 | $6,630.00”
  - column:Books, course materials, supplies, equipment: 1020.0 ⟵ “Books, course materials, supplies, equipment | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00”
  - column:TOTAL: 25860.0 ⟵ “TOTAL | $20,748.00 | $25,860.00 | $22,998.00 | $22,158.00 | $27,270.00 | $24,408.00”
  - column:Tuition & Fees: 5220.0 ⟵ “Tuition & Fees | $5,220.00 | $5,220.00 | $5,220.00 | $6,630.00 | $6,630.00 | $6,630.00”
  - column:Books, course materials, supplies, equipment: 1020.0 ⟵ “Books, course materials, supplies, equipment | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00”
  - column:TOTAL: 22998.0 ⟵ “TOTAL | $20,748.00 | $25,860.00 | $22,998.00 | $22,158.00 | $27,270.00 | $24,408.00”
  - column:Tuition & Fees: 6630.0 ⟵ “Tuition & Fees | $5,220.00 | $5,220.00 | $5,220.00 | $6,630.00 | $6,630.00 | $6,630.00”
  - column:Books, course materials, supplies, equipment: 1020.0 ⟵ “Books, course materials, supplies, equipment | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00”
  - column:TOTAL: 22158.0 ⟵ “TOTAL | $20,748.00 | $25,860.00 | $22,998.00 | $22,158.00 | $27,270.00 | $24,408.00”
  - column:Tuition & Fees: 6630.0 ⟵ “Tuition & Fees | $5,220.00 | $5,220.00 | $5,220.00 | $6,630.00 | $6,630.00 | $6,630.00”
  - column:Books, course materials, supplies, equipment: 1020.0 ⟵ “Books, course materials, supplies, equipment | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00”
  - column:TOTAL: 27270.0 ⟵ “TOTAL | $20,748.00 | $25,860.00 | $22,998.00 | $22,158.00 | $27,270.00 | $24,408.00”
  - column:Tuition & Fees: 6630.0 ⟵ “Tuition & Fees | $5,220.00 | $5,220.00 | $5,220.00 | $6,630.00 | $6,630.00 | $6,630.00”
  - column:Books, course materials, supplies, equipment: 1020.0 ⟵ “Books, course materials, supplies, equipment | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00 | $1,020.00”
  - column:TOTAL: 24408.0 ⟵ “TOTAL | $20,748.00 | $25,860.00 | $22,998.00 | $22,158.00 | $27,270.00 | $24,408.00”
### `4de4f11e9db6240b` Truman State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.truman.edu/admission-cost/cost-aid/office-of-financial-aid/independent-appeal/ (sha256 a12dc1a1cd88)
- issues: semantic_review_required, conflicting_sources:https://www.truman.edu/admission-cost/cost-aid/office-of-financial-aid/award-notification-faq/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Dependency Overrides The Higher Education Act allows a financial aid administrator (FAA) to make dependency overrides on a case-by-case basis for students with unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “However, none of the conditions listed below, singly or in combination, qualify as unusual circumstances meriting a dependency override: Parents refuse to contribute to the student’s education; Parents are unwilling to provide information on the FAFSA or for verification; Parents do not claim the student as a dependent for income tax purposes; Student demonstrates total self-sufficiency.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances do include abandonment by parents, an abusive family environment that threatens the student’s health or safety, or the student being unable to locate his parents.”
### `6182dfbc70c3cde2` Truman State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.truman.edu/admission-cost/cost-aid/office-of-financial-aid/independent-appeal/ (sha256 a12dc1a1cd88)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “In such cases, a dependency override might be warranted.”
  - sentence: dependency_override ⟵ “Independent Appeals Please contact the Financial Aid Office if you have questions or think your situation may qualify for a dependency override.”
### `88315e03b726bac1` Truman State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.truman.edu/admission-cost/cost-aid/office-of-financial-aid/independent-appeal/ (sha256 a12dc1a1cd88)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “An independent appeal form will be made available, if appropriate, and documentation will be required before a professional judgment (PJ) can be made.”
### `8961a0eec61834b0` Truman State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.truman.edu/admission-cost/cost-aid/office-of-financial-aid/award-notification-faq/ (sha256 1c9001f6bda2)
- issues: semantic_review_required, conflicting_sources:https://www.truman.edu/admission-cost/cost-aid/office-of-financial-aid/independent-appeal/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “What should I do if my family has experienced a significant change in income since my FAFSA has been filed?”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances include the following: a major change in employment, a layoff/unemployment, a separation or divorce after the original application was filed, the death or disability of a wage earner, a loss of benefits, unusually high medical bills paid but not covered by insurance, or substantial elementary/secondary tuition expenses.”
  - sentence: need_based_special_circumstances ⟵ “If your family has a special circumstance, you may submit a Special Conditions Form to our office.”
### `3d2306644820f385` University of Central Missouri — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.ucmo.edu/future-students/financing-your-education/scholarships/index.php (sha256 ac9601e6dec2)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “However, if the minimum GPA for that scholarship is not met, then the student would be in danger of losing the scholarship renewal for the following year. *There is no appeal process: please ensure you are enrolled in, and complete, at least 12 credit hours each semester. -------------------------------------------------------------------------------------------------------------------------------”
### `1e2639c3c997b35e` University of Health Sciences and Pharmacy in St. Louis — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uhsp.edu/admissions/financial-aid/financial-aid-policies/ (sha256 1a1470918817)
- issues: semantic_review_required, conflicting_sources:https://www.uhsp.edu/admissions/financial-aid/financial-aid-policies/,https://www.uhsp.edu/wp-content/uploads/2026/08/2026-27_prof-judgement-application.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “View Academic Catalog Professional Judgment Application Policy Details the circumstances that may lead to reconsideration of students’ financial aid eligibility.”
  - sentence: professional_judgment ⟵ “Read Professional Judgment Application Policy Take the Next Steps Apply Now About Our Pharm.d.”
### `7ce6263bc5afa544` University of Health Sciences and Pharmacy in St. Louis — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.uhsp.edu/wp-content/uploads/2026/08/2026-27_prof-judgement-application.pdf (sha256 a1bb78ebc889)
- issues: semantic_review_required, conflicting_sources:https://www.uhsp.edu/admissions/financial-aid/financial-aid-policies/,https://www.uhsp.edu/admissions/financial-aid/financial-aid-policies/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgement Application, 2026-27 The University of Health Sciences and Pharmacy (UHSP), as allowed by law, considers life changes that occur after the completion of your Free Application of Federal Student Aid (FAFSA).”
  - sentence: professional_judgment ⟵ “The financial aid office can consider either special or unusual circumstances when reviewing your Professional Judgment.”
### `88b2f0b5bb788037` University of Health Sciences and Pharmacy in St. Louis — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.uhsp.edu/wp-content/uploads/2026/08/2026-27_prof-judgement-application.pdf (sha256 a1bb78ebc889)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances may include changes to family income, assets, etc., recent unemployment, a dislocated worker, or a housing change due to homelessness.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances may include human trafficking, refugee or asylee status, parental abandonment/incarceration, the inability to contact your parents, or if having contact with your parents poses a significant risk.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances are reviewed using a separate institutional form.”
  - sentence: need_based_special_circumstances ⟵ “If you feel you are in an unusual circumstance listed, please contact the financial aid office.”
### `89026da8099ca377` University of Health Sciences and Pharmacy in St. Louis — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uhsp.edu/admissions/financial-aid/financial-aid-policies/ (sha256 3ab5bfed45a2)
- issues: semantic_review_required, conflicting_sources:https://www.uhsp.edu/admissions/financial-aid/financial-aid-policies/,https://www.uhsp.edu/wp-content/uploads/2026/08/2026-27_prof-judgement-application.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “View Academic Catalog Professional Judgment Application Policy Details the circumstances that may lead to reconsideration of students’ financial aid eligibility.”
  - sentence: professional_judgment ⟵ “Read Professional Judgment Application Policy Take the Next Steps Apply Now About Our Pharm.d.”
### `a4911026fa4d3ddb` University of Missouri-St Louis — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umsl.edu/sfs/basics/sap.html (sha256 ae3f93f7386b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “SAP Appeal deadline is generally the midpoint of the term or 7 days from the date of your notification you are not meeting SAP, but other factors can impact your time to appeal, such as the reason for the appeal or the length of your classes.”
  - sentence: sap_appeal ⟵ “STEP 2: Submit your SAP Appeal form together with other supplemental documentation provided in the Kualibuild link General Information Federal regulations require the Office of Student Financial Aid (SFA) to monitor the academic progress of all federal financial aid recipients.”
  - sentence: sap_appeal ⟵ “Graduate students are expected to complete a master’s degree within 54 semester hours. (Cases of graduate students exceeding the maximum time frame of their degree will be reviewed by the Graduate School in regard to a SAP Appeal).”
  - sentence: sap_appeal ⟵ “For more detailed information about the financial aid Appeal process, see: SAP Appeal Roadmap for Undergraduate Students SAP Appeal Roadmap for Graduate Students Other SAP Policies Late Grade Posted Or Grade Change If a student has been notified that their financial aid has been suspended, and a grade is posted late or a professor changes a grade that will make a difference in the student’s academ”
### `fe1274e2de0551ec` University of Missouri-St Louis — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.umsl.edu/sfs/scholarships-grants/freshman-merit.html (sha256 d2dba14685bc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Once notified a student can file an appeal by completing the scholarship appeal form on the Forms page and submitting it to scholarships@umsl.edu.”
### `47b8cc6ebd204cb1` University of Missouri-St Louis — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.umsl.edu/sfs/scholarships-grants/federal-and-state-grants.html (sha256 bd39a3707e38)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,000/semester ⟵ “Half-time enrollment | $1,000/semester”
### `70128bbf5f408735` University of Missouri-St Louis — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.umsl.edu/sfs/scholarships-grants/federal-and-state-grants.html (sha256 bd39a3707e38)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $2,000/semester ⟵ “Full-time enrollment | $2,000/semester”
### `f838a05ce735126a` University of Missouri-St Louis — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.umsl.edu/sfs/scholarships-grants/federal-and-state-grants.html (sha256 bd39a3707e38)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,500/semester ⟵ “Three-quarter enrollment | $1,500/semester”
### `01f15ce585d9bae1` University of Missouri-St Louis — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umsl.edu/sfs/tuition-fees/index.html (sha256 11c06b46d228)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition: 12552 ⟵ “Tuition | $ 8,364 | $ 19,896 | $12,552”
  - off_campus_not_with_family:Books, course materials, supplies, and equipment: 750 ⟵ “Books, course materials, supplies, and equipment | $ 750 | $ 750 | $ 750”
  - off_campus_not_with_family:Food and Housing: 15806 ⟵ “Food and Housing | $ 15,806 | $ 15,806 | $ 15,806”
  - off_campus_not_with_family:Personal: 6864 ⟵ “Personal | $ 6,864 | $ 6,864 | $ 6,864”
  - off_campus_not_with_family:Transportation: 2160 ⟵ “Transportation | $ 2,160 | $ 2,160 | $ 2,160”
  - off_campus_not_with_family:Loan Fees: 132 ⟵ “Loan Fees | $ 132 | $ 132 | $ 132”
  - off_campus_not_with_family:TOTAL: 38264 ⟵ “TOTAL | $ 34,076 | $45,608 | $38,264”
### `6aed50bd98c1b88d` University of Missouri-St Louis — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.umsl.edu/sfs/tuition-fees/index.html (sha256 11c06b46d228)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition and patient care fee: 30560 ⟵ “Tuition and patient care fee | $ 30,560 | $ 50,464”
  - on_campus:Patient Care: 1800 ⟵ “Patient Care | $ 1,800 | $ 1,800”
  - on_campus:Books, course materials, supplies, and equipment: 4300 ⟵ “Books, course materials, supplies, and equipment | $ 4,300 | $ 4,300”
  - on_campus:Food and housing: 15806 ⟵ “Food and housing | $ 15,806 | $ 15,806”
  - on_campus:Personal: 6864 ⟵ “Personal | $ 6,864 | $ 6,864”
  - on_campus:Transportation: 2160 ⟵ “Transportation | $ 2,160 | $ 2,160”
  - on_campus:Loan fees: 342 ⟵ “Loan fees | $ 342 | $ 342”
  - on_campus:TOTAL: 61832 ⟵ “TOTAL | $ 61,832 | $ 81,736”
### `81affed80d083cb9` University of Missouri-St Louis — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umsl.edu/sfs/tuition-fees/index.html (sha256 11c06b46d228)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition and patient care fee: 50464 ⟵ “Tuition and patient care fee | $ 30,560 | $ 50,464”
  - on_campus:Patient Care: 1800 ⟵ “Patient Care | $ 1,800 | $ 1,800”
  - on_campus:Books, course materials, supplies, and equipment: 4300 ⟵ “Books, course materials, supplies, and equipment | $ 4,300 | $ 4,300”
  - on_campus:Food and housing: 15806 ⟵ “Food and housing | $ 15,806 | $ 15,806”
  - on_campus:Personal: 6864 ⟵ “Personal | $ 6,864 | $ 6,864”
  - on_campus:Transportation: 2160 ⟵ “Transportation | $ 2,160 | $ 2,160”
  - on_campus:Loan fees: 342 ⟵ “Loan fees | $ 342 | $ 342”
  - on_campus:TOTAL: 81736 ⟵ “TOTAL | $ 61,832 | $ 81,736”
### `6c0634ebcc7d0c60` University of Missouri-St Louis — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.umsl.edu/admissions/early-credit-student/ap.html (sha256 d537caa0a903)
- issues: merged_score_cells
- checks: {"distinct_exams": 24, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3 3 3]:  ⟵ “Art | Art/Studio-General Art/Studio-History Art/Studio-Drawing | 3 3 3 | ST ART Elective ART HS 1100 ST ART 1140 | 3 3 3”
  - equivalencies[AP-BIOLOGY|3 4/5]:  ⟵ “Biology | Biology | 3 4/5 | BIOL 1012 & BIOL 1013 BIOL 1821 | 4 5”
  - equivalencies[AP-CHEMISTRY|3/4 5]:  ⟵ “Chemistry | Chemistry | 3/4 5 | CHEM 1111 CHEM 1111 & CHEM 1121 | 5 10”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3 3]:  ⟵ “Computer Science | Computer Science A Computer Science Principles | 3 3 | CMP SCI 1250 Transfer Elective Credit | 3 3”
  - equivalencies[AP-MACROECONOMICS|3 3]:  ⟵ “Economics | Macroeconomics Microeconomics | 3 3 | ECON 1002 ECON 1001 | 3 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 3]:  ⟵ “English | English Language and Composition English Literature and Composition | 3 3 | Freshman Composition Proficiency ENGL 1120 | 3 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | Environmental Science | 3 | Physical Science Elective | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Foreign Languages | Chinese Language and Culture | 3 | Chinese 2101 | 5”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 4/5]:  ⟵ “ | French Language and Culture | 3 4/5 | French 2101 French 2170 | 3 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 5]:  ⟵ “ | French Literature | 3 5 | French 2180 French 2180 and 2190 | 3 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3 4/5]:  ⟵ “ | German Language and Culture | 3 4/5 | German 2101 German 2170 | 3 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3 5]:  ⟵ “ | German Literature | 3 5 | German 2180 German 2180 and 2190 | 3 6”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3 5]:  ⟵ “ | Japanese Language and Culture | 3 5 | Japanese 1001 Japanese 1001 and 1002 | 5 10”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3 4/5]:  ⟵ “ | Spanish Language and Culture | 3 4/5 | Spanish 2101 Spanish 2172 | 3 3”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3 5]:  ⟵ “ | Spanish Literature | 3 5 | Spanish 2180 Spanish 2180 and 2190 | 3 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Geography | Human Geography | 3 | GEOG 1001 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3 4/5]:  ⟵ “History | US History | 3 4/5 | HIST 1001 HIST 1001 & HIST 1002 | 3 6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3 4/5]:  ⟵ “ | World History | 3 4/5 | HIST 1075 HIST 1075 & HIST 1076 | 3 6”
  - equivalencies[AP-EUROPEAN-HISTORY|3 4/5]:  ⟵ “ | European History | 3 4/5 | HIST 1031 HIST 1031 & HIST 1032 | 3 6”
  - equivalencies[AP-PRECALCULUS|3 3 3 3 3]:  ⟵ “Math | Precalculus Calculus (AB) Calculus (BC) Calc (BC), AB subscore Statistics | 3 3 3 3 3 | Math 1045 MATH 1045 & MATH 1800 MATH 1045, 1800 & 1900 MATH 1045 & MATH 1800 MATH 1105 | 5 10 15 10 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | Music Theory | 3 | THRY COM 1301 | 3”
  - equivalencies[AP-PHYSICS-1|3 3]:  ⟵ “Physics | Physics 1 Physics 2 | 3 3 | PHYSICS 1011 & PHYSICS 1011L PHYSICS 1012 & PHYSICS 1012L | 4 4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3 4/5]:  ⟵ “ | Physics C: Electricity & Magnetism | 3 4/5 | PHYSICS 1012 & PHYSICS 1012L PHYSICS 2112 & PHYSICS 2112L | 4 5”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3 4/5]:  ⟵ “ | Physics C: Mechanics | 3 4/5 | PHYSICS 1011 & PHYSICS 1011L PHYSICS 2111 & PHYSICS 2111L | 4 5”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | Psychology | 3 | PSYCH 1003 | 3”
  - … 1 more rows
### `6bc857d9e9bd759d` Webster University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.webster.edu/financialaid/resources-policies.php (sha256 454648d52cf1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “This is more commonly referred to as a dependency override.”
### `71c8aa8f37936a7a` Webster University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.webster.edu/financialaid/ (sha256 6aa2846c747f)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.webster.edu/financialaid/resources-policies.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Remaining Eligible Verification Process Special and Unusual Circumstances Tuition Exchange Tuition Refund and Waiver Tuition Remission HEERF Navigation Home Applying for Aid Types of Aid Undergraduate Students Graduate Students Military-Affiliated Students Tuition and Costs Undergraduate Tuition Graduate Tuition Military Tuition Resources and Policies Contact Us/Meet the Team HEERF Office of Finan”
### `954b2b7463339031` Webster University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.webster.edu/financialaid/resources-policies.php (sha256 454648d52cf1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The Office of Financial Aid can provide the terms and condition criteria for renewal, information for SAP and scholarship appeals, and the steps and requirements for withdrawal and return of Title IV funds (R2T4).”
### `e2d345cb4fc2fc94` Webster University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.webster.edu/financialaid/resources-policies.php (sha256 454648d52cf1)
- issues: semantic_review_required, conflicting_sources:https://www.webster.edu/financialaid/
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Contact the Office of Financial Aid if you have any questions or you would like to discuss any unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “All applications selected for verification must complete the verification process prior to our office reviewing special circumstance requests.”
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstances Financial aid depends on your situation — and your situation can change.”
  - sentence: need_based_special_circumstances ⟵ “While most considerations for specific situations are limited, we may be able to give additional consideration for special or unusual circumstances: Special Circumstances refer to the financial situations that justify adjustments to data elements in the Cost of Attendance or in the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify adjustments to a student’s dependency status, based on a unique situation.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The Financial Aid Office has the ability to review and update information on the FAFSA if the data listed is no longer a reflection of the student’s or family’s financial circumstances.”
### `d8a3971bcf56be48` Webster University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.webster.edu/military/military_tuition.php (sha256 8e2596c6f86d)
- issues: arrangement_unlabeled, implausible_amount
- checks: {"columns": 3, "rows": 1}
  - column:Tuition: 250 ⟵ “Tuition | $250 | $750 | $1,500 | $3,750”
  - column:Tuition: 750 ⟵ “Tuition | $250 | $750 | $1,500 | $3,750”
  - column:Books and materials: 125 ⟵ “Books and materials |  | $125 | $250 | $675”
  - column:Estimated total: 875 ⟵ “Estimated total |  | $875 | $1,750 | $4,425”
  - column:Tuition: 3750 ⟵ “Tuition | $250 | $750 | $1,500 | $3,750”
  - column:Books and materials: 675 ⟵ “Books and materials |  | $125 | $250 | $675”
  - column:Estimated total: 4425 ⟵ “Estimated total |  | $875 | $1,750 | $4,425”
### `01b7bca1782c58bb` Webster University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.webster.edu/admissions/undergraduate/prior-learning.php (sha256 4752ecec4b24)
- issues: score_column_not_scores
- checks: {"distinct_exams": 32, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|ROC]:  ⟵ “Art History | ROC | 3, 4, 5 |  | 3”
  - equivalencies[AP-2-D-ART-DESIGN|ARTS]:  ⟵ “Art Studio 2D Design | ARTS | 3, 4, 5 |  | 3”
  - equivalencies[AP-3-D-ART-DESIGN|ARTS]:  ⟵ “Art Studio 3D Design | ARTS | 3, 4, 5 |  | 3”
  - equivalencies[AP-DRAWING|ARTS]:  ⟵ “Drawing | ARTS | 3, 4, 5 |  | 3”
  - equivalencies[AP-BIOLOGY|PNW]:  ⟵ “Biology | PNW | 3, 4 | BIOL 1020/1021 Biology of Animals with Lab | 4”
  - equivalencies[AP-CALCULUS-AB|QL]:  ⟵ “Calculus AB | QL | 3, 4, 5 |  | 5”
  - equivalencies[AP-CALCULUS-BC|QL]:  ⟵ “Calculus BC | QL | 3 | MATH 1610 Calculus I | 5”
  - equivalencies[AP-CHEMISTRY|PNW]:  ⟵ “Chemistry | PNW | 3, 4, 5 |  | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|GLBL and INTC]:  ⟵ “Chinese Language and Culture | GLBL and INTC | 3, 4 | CHIN 1090 Elementary Chinese Level I, CHIN 1100 Elementary Chinese Level II | 6”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|WCOM]:  ⟵ “English Language and Composition | WCOM | 3, 4, 5 |  | 6”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|WCOM and ROC]:  ⟵ “English Literature and Composition | WCOM and ROC | 3, 4, 5 |  | 6”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|PNW]:  ⟵ “Environmental Science | PNW | 3, 4, 5 |  | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|ROC]:  ⟵ “European History | ROC | 3, 4, 5 | HIST 2230 Age of Total War, HIST 2210 Early Modern Europe | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|GLBL and INTC]:  ⟵ “French Language and Culture | GLBL and INTC | 3, 4 | FREN 1090 Elementary French Level I, FREN 1100 Elementary French Level II | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|GLBL and INTC]:  ⟵ “German Language and Culture | GLBL and INTC | 3, 4 | GRMN 1090 Elementary German Level I, GRMN 1100 Elementary German Level II | 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|SSHB]:  ⟵ “Human Geography | SSHB | 3, 4, 5 |  | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|GLBL and INTC]:  ⟵ “Italian Language and Culture | GLBL and INTC | 3, 4 | ITAL 1090 Elementary Italian Level I, ITAL 1100 Elementary Italian Level II | 6”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|GLBL and INTC]:  ⟵ “Japanese Language and Culture | GLBL and INTC | 3, 4 | JAPN 1090 Elementary Japanese Level I, JAPN 1100 Elementary Japanese Level II | 6”
  - equivalencies[AP-LATIN|ROC]:  ⟵ “Latin | ROC | 3, 4 | LATN 1090 Elementary Latin Level I, LATN 1100 Elementary Latin Level II | 6”
  - equivalencies[AP-MACROECONOMICS|SSHB]:  ⟵ “Macroeconomics* | SSHB | 3, 4, 5 | ECON 2030 Principles of Macroeconomics*If taken with AP Microeconomics will satisfy ECON 2000 Survey of Economics, which is required of most majors in the School of Business. See the catalog for requirements for each major. | 3”
  - equivalencies[AP-MICROECONOMICS|SSHB]:  ⟵ “Microeconomics* | SSHB | 3, 4, 5 | ECON 2020 Principles of Microeconomics*If taken with AP Macroeconomics will satisfy ECON 2000 Survey of Economics, which is required of most majors in the School of Business. See the catalog for requirements for each major. | 3”
  - equivalencies[AP-MUSIC-THEORY|ARTS]:  ⟵ “Music Theory | ARTS | 3, 4, 5 | MUSC 1000 Fundamentals of Musicianship | 3”
  - equivalencies[AP-PHYSICS-1|PNW]:  ⟵ “Physics I | PNW | 3, 4, 5 | PHYS 1710/1711 College Physics I with Lab | 4”
  - equivalencies[AP-PHYSICS-2|PNW]:  ⟵ “Physics II | PNW | 3, 4, 5 | PHYS 1720/1721 College Physics II with Lab | 4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|PNW]:  ⟵ “Physics C: Mechanics | PNW | 3, 4, 5 | PHYS 2030/2031 University Physics I with Lab | 4”
  - … 8 more rows
### `04fe05cc06bae132` Webster University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.webster.edu/admissions/undergraduate/prior-learning.php (sha256 4752ecec4b24)
- issues: rows_without_score
- checks: {"distinct_exams": 18, "equivalencies": 18, "rows_without_score": 18}
  - equivalencies[IB-LATIN|None]:  ⟵ “Classical Languages: Latin | LATN 1090 Elementary Latin Level I | ROC | LATN 1100 Elementary Latin Level II | ROC”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business and Management | MNGT 2100 Management Theory and Practices | - | - | -”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | ECON 2030 Principles of Macroeconomics | SSHB | ECON 2000 Survey of Economics | ”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | ANTH 1400 Introduction to Geography: World and Regional | SSHB | - | -”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History of Europe and Islamic World | HIST 2610 | ROC | - | -”
  - equivalencies[IB-PHILOSOPHY|None]:  ⟵ “Philosophy | PHIL 1100 Introduction to Philosophy | ROC | PHIL 2080 | ROC”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | PSYC 1100 Introduction to Psychology | SSHB | PSYC 2000 | SSHB”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|None]:  ⟵ “Social and Cultural Anthropology | ANTH 1100 Introduction to Cultural Anthropology | ROC | ANTH 2000 | ROC”
  - equivalencies[IB-GLOBAL-POLITICS|None]:  ⟵ “Global Politics | POLT 2610 | SSHB | - | -”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | BIOL 1550/1551 Essentials of Biology I with Lab | PNW | BIOL 1560/1561 Essentials of Biology II with Lab | PNW”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | CHEM 1100/1101 General Chemistry I with Lab | PNW | CHEM 1110/1111 General Chemistry II with Lab | PNW”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Physics | PHYS 1710/1711 College Physics I with Lab | PNW | - | PNW”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|None]:  ⟵ “Environmental Systems and Societies | - | PNW | n/a | n/a”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | COSC 1540 Emerging Technologies | - | - | -”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | MUSC 1050 Introduction to Music Appreciation | ARTS |  | ARTS”
  - equivalencies[IB-FILM|None]:  ⟵ “Film | FLST 1000 Film and TV Appreciation | ARTS | - | ARTS”
  - equivalencies[IB-THEATRE|None]:  ⟵ “Theatre | THEA 1050 Theatre Appreciation | ARTS | - | ARTS”
  - equivalencies[IB-VISUAL-ARTS|None]:  ⟵ “Visual Arts | - | ARTS | - | ARTS”
### `mcbbfcc00b384ea8` Webster University — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://www.webster.edu/admissions/transfer/transfer-resources/transfer-guide-st-louis-community-college.php (sha256 a6d0ff88d1ef)
- issues: ambiguous_year_labels, conflicting_values:max_transfer_credits
- checks: {"fields": ["max_transfer_credits", "min_grade"], "merged_pages": 5}
  - residency_requirement_credits: 36 ⟵ “Webster University's minimum residency requirement is the completion of 30 credit hours of the last 36 credit hours prior to graduation.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - max_transfer_credits: 18 ⟵ “Transfer students can apply up to 18 credit hours of approved PSYCH coursework in the psychology major from another Students may transfer in 3 credit hours of approved foreign language coursework to meet the international language requirement of the BA degree.”
### `md803378959a36d4` Webster University — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.webster.edu/admissions/transfer/transfer-resources/transfer-guide-southwestern-illinois-college.php (sha256 22957b75e2f1)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
  - min_grade: D ⟵ “A grade of D or higher is considered passing, but a D will have severe transfer restrictions.”
### `04aff2bf947e87b5` Westminster College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/PDFs/SAPPolicy.pdf (sha256 6be264f5fb8d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “SAP Suspension may be appealed if unusual and/or mitigating circumstances affected academic progress.”
  - sentence: sap_appeal ⟵ “Such circumstances may include a severe illness or injury to the student or an immediate family member, the death of a student’s relative, student activation into military service or other circumstances as deemed appropriate for consideration by the SAP Appeals Committee. 2.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Committee’s decision will be sent to the student by mail or electronic means.”
  - sentence: sap_appeal ⟵ “SAP Appeals Committee decisions cannot be appealed to another source. 7.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee members are the Dean of Student Life, Associate Dean of Faculty, and Registrar.”
### `088b31d750945b39` Westminster College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.wcmo.edu/about/offices/business/student-accounts/fees.html (sha256 17fb6ba2b32b)
- issues: ambiguous_year_labels, conflicting_sources:https://www.wcmo.edu/admissions-aid/costs-financial-aid/cost-attendance.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 34048 ⟵ “Tuition | $34,048”
  - column:Room - Residence Halls, Double: 7084 ⟵ “Room - Residence Halls, Double | $7,084”
  - column:Meals - 19 Meal Plan: 6544 ⟵ “Meals - 19 Meal Plan | $6,544”
  - column:Mandatory Fee: 3144 ⟵ “Mandatory Fee | $3,144”
  - column:Total Annual Charge: 50820 ⟵ “Total Annual Charge | $50,820”
### `78ce96745b931bd8` Westminster College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wcmo.edu/about/offices/business/student-accounts/fees.html (sha256 17fb6ba2b32b)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Tuition - Full-time (12-19 hours): 16528 ⟵ “Tuition - Full-time (12-19 hours) | $16,528 | $33,056 | $17,024 | $34,048”
  - column:Mandatory Fees: 1572 ⟵ “Mandatory Fees | $1,572 | $3,144 | $1,572 | $3,144”
### `cc79a23fa2d52162` Westminster College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wcmo.edu/admissions-aid/costs-financial-aid/cost-attendance.html (sha256 b2cfeb5cbe1d)
- issues: components_do_not_reconcile, conflicting_sources:https://www.wcmo.edu/about/offices/business/student-accounts/fees.html
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - on_campus:Tuition: 34048 ⟵ “Tuition | $34,048”
  - on_campus:Fees: 3144 ⟵ “Fees | $3,144”
  - on_campus:Housing (double occupancy): 7048 ⟵ “Housing (double occupancy) | $7,048”
  - on_campus:Food (19 meal plan): 6544 ⟵ “Food (19 meal plan) | $6,544”
  - on_campus:TOTAL: 50820 ⟵ “TOTAL | $50,820”
### `d2f507ebe397a5e0` William Jewell College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://jewell.edu/tuition-fees/ (sha256 d775200b9e37)
- issues: arrangement_unlabeled
- checks: {"columns": 6, "components_reconcile": true, "rows": 9}
  - column:Tuition (2 semesters): 22160 ⟵ “Tuition (2 semesters) | $22,160 | $22,160 | $22,160 | $22,160 | $22,160 | $22,160”
  - column:Mandatory Fees: 1490 ⟵ “Mandatory Fees | $1,490 | $1,490 | $1,490 | $1,490 | $1,490 | $1,490”
  - column:Food: 6274 ⟵ “Food | $6,274 | $6,274 | $6,274 | $6,274 | $6,274 | $6,274”
  - column:Housing: 7058 ⟵ “Housing | $7,058 | $3,198 | $7,058 | $3,198 | $10,058 | $10,058”
  - column:Transportation: 1800 ⟵ “Transportation | $1,800 | $1,800 | $1,800 | $1,800 | $1,800 | $1,800”
  - column:Books: 840 ⟵ “Books | $840 | $840 | $840 | $840 | $840 | $840”
  - column:Personal: 2310 ⟵ “Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - column:Loan Fees (student – average): 71 ⟵ “Loan Fees (student – average) | $71 | $71 | $71 | $119 | $119 | $119”
  - column:Total: 42003 ⟵ “Total | $42,003 | $38,143 | $42,003 | $38,191 | $45,051 | $45,051”
  - with_parents_or_family:Tuition (2 semesters): 22160 ⟵ “Tuition (2 semesters) | $22,160 | $22,160 | $22,160 | $22,160 | $22,160 | $22,160”
  - with_parents_or_family:Mandatory Fees: 1490 ⟵ “Mandatory Fees | $1,490 | $1,490 | $1,490 | $1,490 | $1,490 | $1,490”
  - with_parents_or_family:Food: 6274 ⟵ “Food | $6,274 | $6,274 | $6,274 | $6,274 | $6,274 | $6,274”
  - with_parents_or_family:Housing: 3198 ⟵ “Housing | $7,058 | $3,198 | $7,058 | $3,198 | $10,058 | $10,058”
  - with_parents_or_family:Transportation: 1800 ⟵ “Transportation | $1,800 | $1,800 | $1,800 | $1,800 | $1,800 | $1,800”
  - with_parents_or_family:Books: 840 ⟵ “Books | $840 | $840 | $840 | $840 | $840 | $840”
  - with_parents_or_family:Personal: 2310 ⟵ “Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - with_parents_or_family:Loan Fees (student – average): 71 ⟵ “Loan Fees (student – average) | $71 | $71 | $71 | $119 | $119 | $119”
  - with_parents_or_family:Total: 38143 ⟵ “Total | $42,003 | $38,143 | $42,003 | $38,191 | $45,051 | $45,051”
  - off_campus_not_with_family:Tuition (2 semesters): 22160 ⟵ “Tuition (2 semesters) | $22,160 | $22,160 | $22,160 | $22,160 | $22,160 | $22,160”
  - off_campus_not_with_family:Mandatory Fees: 1490 ⟵ “Mandatory Fees | $1,490 | $1,490 | $1,490 | $1,490 | $1,490 | $1,490”
  - off_campus_not_with_family:Food: 6274 ⟵ “Food | $6,274 | $6,274 | $6,274 | $6,274 | $6,274 | $6,274”
  - off_campus_not_with_family:Housing: 7058 ⟵ “Housing | $7,058 | $3,198 | $7,058 | $3,198 | $10,058 | $10,058”
  - off_campus_not_with_family:Transportation: 1800 ⟵ “Transportation | $1,800 | $1,800 | $1,800 | $1,800 | $1,800 | $1,800”
  - off_campus_not_with_family:Books: 840 ⟵ “Books | $840 | $840 | $840 | $840 | $840 | $840”
  - off_campus_not_with_family:Personal: 2310 ⟵ “Personal | $2,310 | $2,310 | $2,310 | $2,310 | $2,310 | $2,310”
  - … 29 more rows
### `136187a3e68e58bd` William Woods University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.williamwoods.edu/cost-and-aid/tuition-and-fees/ (sha256 33e2126f8786)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "rows": 11}
  - on_campus:Full Year COA: 54838 ⟵ “Full Year COA | $54,838 | $47,508”
  - on_campus:COA (single semester): 27419 ⟵ “COA (single semester) | $27,419 | $23,754”
  - on_campus:Tuition: 15100 ⟵ “Tuition | $15,100 | $15,100”
  - on_campus:Housing: 3160 ⟵ “Housing | $3,160 | $1,718”
  - on_campus:Food: 3626 ⟵ “Food | $3,626 | $1,473”
  - on_campus:Technical Fee: 340 ⟵ “Technical Fee | $340 | $270”
  - on_campus:Activity/Health Services Fees: 330 ⟵ “Activity/Health Services Fees | $330 | $330”
  - on_campus:Books, Supplies, ETC: 650 ⟵ “Books, Supplies, ETC | $650 | $650”
  - on_campus:Personal: 3182 ⟵ “Personal | $3,182 | $3,182”
  - on_campus:Transportation: 1000 ⟵ “Transportation | $1000 | $1000”
  - on_campus:Federal Loan Fees: 31 ⟵ “Federal Loan Fees | $31 | $31”
  - with_parents_or_family:Full Year COA: 47508 ⟵ “Full Year COA | $54,838 | $47,508”
  - with_parents_or_family:COA (single semester): 23754 ⟵ “COA (single semester) | $27,419 | $23,754”
  - with_parents_or_family:Tuition: 15100 ⟵ “Tuition | $15,100 | $15,100”
  - with_parents_or_family:Housing: 1718 ⟵ “Housing | $3,160 | $1,718”
  - with_parents_or_family:Food: 1473 ⟵ “Food | $3,626 | $1,473”
  - with_parents_or_family:Technical Fee: 270 ⟵ “Technical Fee | $340 | $270”
  - with_parents_or_family:Activity/Health Services Fees: 330 ⟵ “Activity/Health Services Fees | $330 | $330”
  - with_parents_or_family:Books, Supplies, ETC: 650 ⟵ “Books, Supplies, ETC | $650 | $650”
  - with_parents_or_family:Personal: 3182 ⟵ “Personal | $3,182 | $3,182”
  - with_parents_or_family:Transportation: 1000 ⟵ “Transportation | $1000 | $1000”
  - with_parents_or_family:Federal Loan Fees: 31 ⟵ “Federal Loan Fees | $31 | $31”
### `5f930ffed333e2b5` William Woods University — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.williamwoods.edu/academics/undergraduate/william-woods-dual-enrollment-program/ (sha256 c661cbc9ab9e)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 1}
  - per_credit_hour_charge: 75 ⟵ “Eligible students can take college courses at a reduced rate ($75/hr) to fulfill high school requirements while earning college credit.”
  - eligibility_tier: 2.75 ⟵ “A cumulative GPA of 2.75 or higher”
  - per_credit_hour_charge: 75 ⟵ “Dual enrollment courses are offered at a significantly reduced tuition rate of $75.00 per credit hour.”
  - per_credit_hour_charge: 75 ⟵ “The cost per credit hour for dual enrollment students is $75/hr.”
### `m60e3707fb87ff5b` William Woods University — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.williamwoods.edu/admissions/Transfer/transfer-applicants/ (sha256 c7e303e6a149)
- issues: stale_year_label:2025-26
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - residency_requirement_credits: 30 ⟵ “William Woods University does not accept transfer credit as part of a student's last 30 hours.”
  - residency_requirement_credits: 30 ⟵ “William Woods University does not accept transfer credit as part of a student's last 30 hours.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 58; pages by category: admissions_tests 9, ap_credit 4, cost_of_attendance 4, degree_requirements 3, dual_enrollment 6, merit_scholarships 18, statewide_articulation 4, transfer_credit 16, tuition_fees 8

## Blocked by the site (every request refused; needs the browser fallback)

- Hannibal-LaGrange University (`ipeds-177542`)
- Jefferson College (`ipeds-177676`)
- University of Missouri-Kansas City (`ipeds-178402`)
- Moberly Area Community College (`ipeds-178448`)
- North Central Missouri College (`ipeds-179715`)

## Leads: official pages found with no extracted record

- Avila University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Bolivar Technical College: cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- Calvary University: tuition_fees, cost_of_attendance, admissions_tests, clep_credit, dual_enrollment, degree_requirements
- Central Christian College of the Bible: tuition_fees, cost_of_attendance, degree_requirements
- Central Methodist University-College of Graduate and Extended Studies: cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, degree_requirements
- Central Methodist University-College of Liberal Arts and Sciences: cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, degree_requirements
- City Vision University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, degree_requirements
- College of the Ozarks: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Columbia College: admissions_tests, ib_credit, degree_requirements
- Conception Seminary College: degree_requirements
- Cottey College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Cox College: tuition_fees, cost_of_attendance, merit_scholarships, aid_appeals
- Crowder College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Culver-Stockton College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Drury University: tuition_fees, cost_of_attendance, admissions_tests, ib_credit, transfer_credit, degree_requirements
- Drury University-College of Continuing Professional Studies: tuition_fees, cost_of_attendance, admissions_tests, ib_credit, transfer_credit, degree_requirements
- East Central College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Evangel University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit
- Evangel University-College of Online Learning: tuition_fees, cost_of_attendance, admissions_tests, ap_credit
- Evangel University-James River Assembly of God Church: tuition_fees, cost_of_attendance, admissions_tests, ap_credit
- Fontbonne University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, statewide_articulation, degree_requirements
- Kansas City Art Institute: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, statewide_articulation, degree_requirements, aid_appeals
- Lincoln University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, statewide_articulation, residency
- Lindenwood University: admissions_tests, merit_scholarships, degree_requirements, aid_appeals
- Logan University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Maryville University of Saint Louis: dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Metropolitan Community College-Kansas City: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency, degree_requirements
- Midwestern Baptist Theological Seminary: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Mineral Area College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Mission University: admissions_tests, common_data_set, ap_credit, clep_credit, transfer_credit, degree_requirements
- Missouri Baptist University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Missouri Southern State University: admissions_tests, merit_scholarships, clep_credit, transfer_credit, residency, degree_requirements, aid_appeals
- Missouri State University-Springfield: tuition_fees, admissions_tests, dual_enrollment
- Missouri State University-West Plains: cost_of_attendance, merit_scholarships
- Missouri University of Science and Technology: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency, degree_requirements
- Missouri Valley College: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Missouri Western State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- Northwest Missouri State University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Ozark Christian College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Ozarks Technical Community College: tuition_fees, cost_of_attendance, merit_scholarships, transfer_credit, residency, degree_requirements, aid_appeals
- Park University: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, ib_credit, transfer_credit, statewide_articulation, degree_requirements
- Ranken Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Rockhurst University: tuition_fees, cost_of_attendance, admissions_tests, clep_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Saint Louis Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, clep_credit, transfer_credit, residency, degree_requirements
- Saint Louis University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit
- Southeast Missouri Hospital College of Nursing and Health Sciences: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, aid_appeals
- Southeast Missouri State University: tuition_fees, cost_of_attendance, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Southwest Baptist University: cost_of_attendance, admissions_tests, ap_credit, clep_credit, statewide_articulation, residency, degree_requirements
- St Charles Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, residency, degree_requirements
- State Fair Community College: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- State Technical College of Missouri: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements, aid_appeals
- Stephens College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Three Rivers College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- Truman State University: cost_of_attendance, admissions_tests, ib_credit, residency
- University of Central Missouri: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency
- University of Health Sciences and Pharmacy in St. Louis: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- University of Missouri-Columbia: transfer_credit
- University of Missouri-St Louis: admissions_tests, transfer_credit, statewide_articulation, residency
- Washington University in St Louis: cost_of_attendance
- Webster University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- Westminster College: cost_of_attendance, admissions_tests, common_data_set, ap_credit, dual_enrollment, degree_requirements
- William Jewell College: admissions_tests, transfer_credit, statewide_articulation
- William Woods University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency, aid_appeals
