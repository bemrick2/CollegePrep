# Review queue — ME (2026-27)

Pages fetched: 1599; failures: 126. Candidates: 242 (140 without issues, 102 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 5 | 6 | 11 | 1 | 3 |
| cost_of_attendance | 0 | 0 | 0 | 2 | 19 | 2 | 3 |
| admissions_tests | 0 | 0 | 1 | 0 | 20 | 2 | 3 |
| common_data_set | 0 | 0 | 1 | 0 | 4 | 18 | 3 |
| merit_scholarships | 0 | 0 | 4 | 1 | 16 | 2 | 3 |
| ap_credit | 0 | 0 | 0 | 2 | 12 | 9 | 3 |
| clep_credit | 0 | 0 | 1 | 2 | 8 | 12 | 3 |
| ib_credit | 0 | 0 | 0 | 2 | 2 | 19 | 3 |
| dual_enrollment | 0 | 0 | 1 | 0 | 12 | 10 | 3 |
| transfer_credit | 0 | 0 | 5 | 3 | 14 | 1 | 3 |
| statewide_articulation | 0 | 0 | 0 | 0 | 7 | 16 | 3 |
| residency | 0 | 0 | 0 | 0 | 11 | 12 | 3 |
| degree_requirements | 0 | 0 | 0 | 0 | 15 | 8 | 3 |
| aid_appeals | 0 | 0 | 0 | 8 | 4 | 11 | 3 |

## Ready for review (140)

### `955b46b02ae1dd7e` Bowdoin College — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.bowdoin.edu/ir/pdf/bowdoin-cds_2025-2026.pdf (sha256 d1dfe5ceb33c)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 14045 ⟵ “Total first-time, first-year (degree-seeking) who applied           540         7464          6041              0   14045”
  - admits: 957 ⟵ “Total first-time, first-year (degree-seeking) who were admitted      74         807            76               0    957”
  - enrolled: 515 ⟵ “Total first-time, first-year (degree-seeking) enrolled               51         427            37               0    515”
  - sat_composite_25..75: [1470, 1510, 1540] ⟵ “SAT Composite                     1470                      1510                       1540”
  - sat_math_25..75: [730, 760, 780] ⟵ “SAT Math                           730                       760                       780”
  - act_25..75: [33, 34, 35] ⟵ “ACT Composite                      33                        34                         35”
### `562777f8d06f16bf` College of the Atlantic — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.coa.edu/admissions/tuition-fees/ (sha256 a649f711298e)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 50895 ⟵ “Tuition | $50,895”
  - column:Fees: 549 ⟵ “Fees | $549”
  - column:Housing: 7059 ⟵ “Housing | $7,059”
  - column:Food: 5178 ⟵ “Food | $5,178”
  - column:Total billed costs: 63681 ⟵ “Total billed costs | $63,681”
### `646b2f335e2c3820` College of the Atlantic — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.coa.edu/admissions/apply/transfer-students/ (sha256 bbd6b6b73e80)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “In order to translate your transcript into COA credits, COA will accept credits as follows for all courses in which you received a letter grade of C or better: If you are transferring credit from an institution that uses the semester system, or credit hours, multiply your current credit hours by 0.3 to determine the likely number of COA credits you will have.”
### `146bf0d1d8d536ea` Eastern Maine Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.emcc.edu/admissions/admissions/prepare/transfer-credit/ (sha256 d2b50d7b8c21)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Generally, courses with grades of C (2.0) or better which are judged by Eastern Maine Community College to be equivalent to Eastern Maine Community College course offerings will be transferred.”
### `05e3cc15c4baacce` Saint Joseph's College of Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/scholarships/ (sha256 fb0c395c003f)
- checks: {"thresholds": null}
  - award_amount_text: $18,000 /year ⟵ “Xavier Scholarship | $18,000 /year”
### `42486fc0980b9992` Saint Joseph's College of Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/scholarships/ (sha256 fb0c395c003f)
- checks: {"thresholds": null}
  - award_amount_text: $22,000 /year ⟵ “McAuley Scholarship | $22,000 /year”
### `bed6ba57aabbb304` Saint Joseph's College of Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/scholarships/ (sha256 fb0c395c003f)
- checks: {"thresholds": null}
  - award_amount_text: $20,000 /year ⟵ “Mercy Scholarship | $20,000 /year”
### `cd6e58590568383e` Saint Joseph's College of Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/scholarships/ (sha256 fb0c395c003f)
- checks: {"thresholds": null}
  - award_amount_text: $25,000 /year ⟵ “Presidential Scholarship | $25,000 /year”
### `d13823b6daab2124` Saint Joseph's College of Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/scholarships/ (sha256 fb0c395c003f)
- checks: {"thresholds": null}
  - award_amount_text: $10,000 /year ⟵ “Monk Scholarship | $10,000 /year”
### `c458cbedffbd8967` Saint Joseph's College of Maine — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/paying-your-bill/ (sha256 77845eb966ff)
- checks: {"columns": 1, "rows": 6}
  - column:Student ID Replacement (each occurrence): 20 ⟵ “Student ID Replacement (each occurrence) | $20”
  - column:Late Tuition Payment Fee (per semester late): 350 ⟵ “Late Tuition Payment Fee (per semester late) | $350”
  - column:Payment Plan Late Fee (per semester): 70 ⟵ “Payment Plan Late Fee (per semester) | $70”
  - column:Room + Board Single Room Supplement (per semester): 2010 ⟵ “Room + Board Single Room Supplement (per semester) | $2,010”
  - column:Health Facilities Fee – see FAQ below: 300 ⟵ “Health Facilities Fee – see FAQ below | $300”
  - column:Health Insurance – Can be waived, see FAQ below: 2419 ⟵ “Health Insurance – Can be waived, see FAQ below | $2,419”
### `18f6a04310a5cfa9` Southern Maine Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.smccme.edu/wp-content/uploads/2025/06/College-Level-Examination-Program-CLEP-Comparison.pdf (sha256 335f0e312490)
- checks: {"distinct_exams": 30, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting                                        50           ACCT 105               3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law                                   50           BUSN 260               3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management                                    50           BUSN ELE               3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing                                     50           BUSN 200               3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                                         50           ENGL ELE               3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature                       50           ENGL 115               3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                                         50           ENGL 100               3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular                                 50           ENGL 100               3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|59]:  ⟵ “College Composition (Nursing)                               59           ENGL 100               3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|59]:  ⟵ “College Composition Modular (Nursing)                       59           ENGL 100               3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                                          50           ENGL ELE               3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                                                  50           HUMA ELE               3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                                         50           POLS 105               3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development                                50           PSYC 220               3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology                      50           PSYC 225               3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                                     50           PSYC 100               3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                                      50           SOCI 100               3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                                50           ECON 125               3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Prinicples of Microeconomics                                50           ECON 120               3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History                                 50           SSCI ELE               6”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648           50           HIST ELE               3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present                    50           HIST ELE               3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                                     50           BIOL 100               4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                                    50           MATH 270               4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                                                   50           CHEM 120               4”
  - … 7 more rows
### `17ba4b4d9df77a74` Thomas College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.thomas.edu/admissions-aid/tuition-fees/ (sha256 374ee751d64a)
- checks: {"columns": 1, "rows": 8}
  - column:Tuition (12-18 Credits Per Semester): 32772 ⟵ “Tuition (12-18 Credits Per Semester) | $32,772”
  - column:Fees: 1180 ⟵ “Fees | $1,180”
  - column:Housing: 8088 ⟵ “Housing | $8,088”
  - column:Food (Meal Plan): 7176 ⟵ “Food (Meal Plan) | $7,176”
  - column:Books, Course Materials, Supplies & Equipment: 800 ⟵ “Books, Course Materials, Supplies & Equipment | $800”
  - column:Transportation: 4560 ⟵ “Transportation | $4,560”
  - column:Miscellaneous Personal Expenses: 1200 ⟵ “Miscellaneous Personal Expenses | $1,200”
  - column:Federal Student Loan Fees: 0 ⟵ “Federal Student Loan Fees | $0”
### `070f5debc26ee053` University of Maine at Augusta — awards 2026-27 [new] (source_unlabeled)
- source: https://www.uma.edu/financial/scholarships/uma-10k/ (sha256 c0e814328c8f)
- checks: {"thresholds": null}
  - award_amount_text: Year 3 ⟵ “Year 3 | $3,000 ($1,500/semester)”
### `3306f50f54c5b14b` University of Maine at Augusta — awards 2026-27 [new] (source_unlabeled)
- source: https://www.uma.edu/financial/scholarships/uma-10k/ (sha256 c0e814328c8f)
- checks: {"thresholds": null}
  - award_amount_text: Year 4 ⟵ “Year 4 | $3,000 ($1,500/semester)”
### `9301a8407750e1b5` University of Maine at Augusta — awards 2026-27 [new] (source_unlabeled)
- source: https://www.uma.edu/financial/scholarships/uma-10k/ (sha256 c0e814328c8f)
- checks: {"thresholds": null}
  - award_amount_text: Year 1 ⟵ “Year 1 | $2,000 ($1,000/semester)”
### `de381076f7d61ec7` University of Maine at Augusta — awards 2026-27 [new] (source_unlabeled)
- source: https://www.uma.edu/financial/scholarships/uma-10k/ (sha256 c0e814328c8f)
- checks: {"thresholds": null}
  - award_amount_text: Year 2 ⟵ “Year 2 | $2,000 ($1,000/semester)”
### `9e14552a948b94d7` University of Maine at Augusta — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.uma.edu/admission/transfer/ (sha256 80d0606b02ef)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Grades of “C-” or higher are considered for transfer credit.”
### `13b382c59eeacfb8` University of Maine at Presque Isle — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.umpi.edu/student-financial-services/student-accounts/tuition-a-fees/ (sha256 3f4b6fa7ce06)
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 8370 ⟵ “Tuition | $8,370 | $14,220”
  - column:Mandatory Fees: 1500 ⟵ “Mandatory Fees | $1,500 | $1,500”
  - column:Housing and Food: 11400 ⟵ “Housing and Food | $11,400 | $11,400”
  - column:Annual Estimated Direct Costs: 21270 ⟵ “Annual Estimated Direct Costs | $21,270 | $27,120”
### `6791c47d9de0a04c` University of Maine at Presque Isle — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umpi.edu/student-financial-services/student-accounts/tuition-a-fees/ (sha256 3f4b6fa7ce06)
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 14220 ⟵ “Tuition | $8,370 | $14,220”
  - column:Mandatory Fees: 1500 ⟵ “Mandatory Fees | $1,500 | $1,500”
  - column:Housing and Food: 11400 ⟵ “Housing and Food | $11,400 | $11,400”
  - column:Annual Estimated Direct Costs: 27120 ⟵ “Annual Estimated Direct Costs | $21,270 | $27,120”
### `4e1f0f1187b93f65` University of Maine at Presque Isle — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.umpi.edu/offices/student-records/transfer-credits/ (sha256 7a044e09de9f)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transfer Credit within the UMS All undergraduate courses successfully completed with a grade of C- or higher, including P grades, will transfer from one UMS institution to another.”
  - min_grade: C- ⟵ “Courses taken under a P, S, or CR grade at an institution external to the UMS must have the “Passing” grade defined as being equal to a grade of C- or higher to qualify for transfer within the UMS.”
### `05d59d4ffca5a0d9` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Edward Angel Scholarship for Veterans | Scholarship Overview The Edward Angel Scholarship for veterans provides a $1,000 award to a deserving undergraduate veteran student anywhere in the United States. This nationwide initiative reflects Edward Angel's lifelong commitment to excellence and his desi”
### `07a16dcc498e66c6` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Sabrina Kuykendall Blue Key Business Scholarship​ | Scholarship OverviewThis scholarship is open to undergraduate students currently enrolled in accredited business programs who are actively preparing for careers in business. Whether your interests lie in finance, operations, consulting, entrepreneu”
### `0e8bd91f2a1e14c5` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “Teaching Scholarships | Teaching scholarships are available both regionally and nationwide, and many were created especially for students with specific career goals, cultural identities, histories of military service, and other personal attributes including single parents and adult learners. The sec”
### `125b1ebf71cfa868` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “The Chad Faaborg Scholarship for Entrepreneurs | Scholarship OverviewThe Chad Faaborg Scholarship for Entrepreneurs awards $1,000 to one deserving recipient per application cycle. Unlike many scholarships, this award is intentionally open — there is no minimum GPA requirement and no restriction on m”
### `16d0d585dc1e16da` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: High School, Undergraduate, Graduate ⟵ “BloomNation 'Support Local' Scholarship | About the ScholarshipAt BloomNation, we believe that local businesses are the heart of every community. As a platform dedicated to helping local florists grow and thrive, we're proud to launch the BloomNation Support Local Scholarship for students who share ”
### `222fb39dba7096e5` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Valinda Nwadike Scholarship for Medical Students | Scholarship OverviewThis $1,000 scholarship is paid directly to the winner or their financial aid office. The award cycle runs once per year with a single annual deadline, and the winner is announced within thirty days after that deadline. Eligi”
### `248df8385112fe4f` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “Healthcare Professional Scholarship | At The Law Offices of Joseph J. Bogdan, Inc., our practice is dedicated to serving doctors, pharmacists, nurses, and other healthcare professionals in defense of their licenses and certiﬁcations. Our founding attorney, Joseph Bogdan, is a registered pharmacist i”
### `2959318ff4f06172` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Michael Wiese Engineering Scholarship | Scholarship Overview The Michael Wiese Scholarship for Engineering offers a $1,000 award to an undergraduate student who demonstrates a passion for engineering, innovation, and creative problem-solving. The scholarship is awarded through an essay competition d”
### `2bdb819eafeae312` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Jose Jacob Scholarship for Future Doctors | Scholarship Overview The Dr. Jose Jacob Scholarship for Future Doctors offers a $1,000 award to a deserving undergraduate student who demonstrates a strong commitment to pursuing a career in medicine. Established in honor of Dr. Jose Jacob's distinguis”
### `32a89efc6ce5b657` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “The Reed Atamian Scholarship for Entrepreneurs | Scholarship OverviewThe Reed Atamian Scholarship for Entrepreneurs is a prestigious award designed to support undergraduate students who are pursuing a career in entrepreneurship. In recognition of Reed Atamian's outstanding leadership and contributio”
### `3350cf998b0e8b0e` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “The Sheila Busheri Scholarship for Future Medical Leaders | Scholarship OverviewThe Sheila Busheri Scholarship is a $1,000 award established to support the next generation of healthcare professionals who demonstrate a commitment to excellence and community service. Inspired by the career of Sheila B”
### `3c42dc747124cf6f` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Ranjan Rajbanshi Scholarship for Medical Students | Scholarship OverviewThe Dr. Ranjan Rajbanshi Scholarship for Medical Students was created to recognize and support undergraduate students who are preparing for careers in the medical and healthcare fields. The scholarship reflects Dr. Rajbanshi”
### `3cceee72407aab1b` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: High School, Undergraduate, Graduate ⟵ “Citizens Bank Scholarship | Citizens wants to honor the dedication of students and families pursuing higher learning! Fill out the registration form below to be entered for a chance to win a Grand Prize of $15,000 to use towards school expenses and one of the $2,500 monthly prizes for use towards sc”
### `3f4833b77fbb5dce` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Michael Rasekhi Scholarship for Medical Students | Scholarship OverviewThe Michael Rasekhi Scholarship was established to honor the legacy of Michael Rasekhi, a visionary leader in community health. This scholarship aims to support dedicated students who are on the path to a medical career and who d”
### `4a431d78f90431d4` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Graduate ⟵ “P.E.O. Scholar Award | The Scholar Award is a one-time, competitive, merit-based award is intended to recognize and encourage academic excellence and achievement by women in doctoral-level programs. In addition to recognizing and encouraging excellence in higher education, these awards provide parti”
### `4cd621156a3a16d8` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “Global Scholarships for International Students | Whether you are a current student already studying at an institution or a prospective student, Global Scholarships has scholarships available for you. Search our scholarship database!At Global Scholarships, we are striving to be the best scholarship p”
### `4fdb81a32b2ed4ce` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “The QD Fund for Mental Health | The QD Fund OverviewThe QD Fund awards a $10,000 scholarship through an essay-based application open to undergraduate and graduate students pursuing careers in healthcare and behavioral health fields. Structured in collaboration with QD Apparel (QD Holdings Inc.), a p”
### `542e27ba7685d0cb` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Audrey Saylor Manufacturing Scholarship | Scholarship Overview The Audrey Saylor Scholarship for Manufacturing is a competitive, essay-based financial award designed for forward-thinking undergraduate students. Recognizing the rising costs of higher education, this initiative provides a single, one-”
### `5901bf212db23600` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Graduate ⟵ “P.E.O. International Peace Scholarship Fund | Fostering Global Peace Through EducationThe P.E.O. International Peace Scholarship (IPS) Fund provides scholarships to international women pursuing graduate degrees in the U.S. and Canada to foster global peace through education. IPS recipients carry the”
### `618d5df87f9d4e27` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Charles Principato Grant for Student Athletes | Grant OverviewAthletics provides opportunities to develop leadership, discipline, teamwork, and resilience—qualities that are essential for success in higher education and future careers. This grant recognizes students who embrace these values while st”
### `621c181452a9a64c` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “AES Engineering Scholarship | AES Engineering is pleased to be able to continue offering scholarships to motivated students to help in the furthering of their education.Scholarship CriteriaOur belief is that achieving a high grade point average should not be the only criteria for determining who des”
### `628259caf269e501` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Kevin Kuykendall Scholarship for Entrepreneurs | Scholarship OverviewThe Kevin Kuykendall Scholarship for Entrepreneurs is a $1,000 essay-based award created to support undergraduate students who demonstrate ambition, leadership potential, and a commitment to building a meaningful future in business”
### `6528d40f57bd5933` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Stanley Sy Scholarship | Scholarship OverviewThe Stanley Sy Scholarship is an annual essay contest designed to support undergraduate and medical students who are dedicated to pursuing a career in medicine. Established to honor the legacy of Stanley Peter Sy—a physician whose career spanned six b”
### `66fafe2fb9b88827` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “The Behan Law Group Military Veteran Scholarship | At The Behan Law Group, P.L.L.C., we have great respect for those who dedicate their lives in service to their country and community. Our founding attorney, Michelle Behan, is a U.S. Navy Veteran, and she has been a passionate advocate for Veterans ”
### `773aec2b881706a9` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: High School, Undergraduate, Graduate ⟵ “Love Your Career Scholarship | $1,000 ScholarshipScholarship opportunity for students looking to love their careers!Make plans now to love your career. Scott Jones, founder of JonesTshirts.com is a firm believer in the importance of loving your career. It affects every aspect of your life. Your fami”
### `7b572b2ca8ab543f` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: High School, Undergraduate ⟵ “BigSun Scholarship...2027 | BigSun Scholarship...2027The BigSun Organization is proud to be able to help young athletes succeed in their academic pursuits. In order to do our part we are offering an annual scholarship to a deserving student. All student athletes are eligible regardless of the sport ”
### `7be62f4265733562` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: High School, Undergraduate, Graduate ⟵ “Good Life’s Improving Tomorrow Biannual Scholarship | Good Life’s Improving Tomorrow Biannual ScholarshipGood Life has been San Diego’s trusted property management company since its inception in 2013. And since last year, we have brought our expertise to Orange County. At Good Life, we build relatio”
### `862a871adee7b0d0` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Keith Myers Grant for Entrepreneurs | The Keith Myers Grant for Entrepreneurs is a $1,000 essay-based scholarship created to support undergraduate students who are committed to pursuing careers in entrepreneurship. This grant recognizes forward-thinking students who demonstrate creativity, leadershi”
### `8973c80d83a7992b` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “The Gold Law Firm “Challenge Yourself Scholarship” | In memory of Kevin Maez (1986-2022), Attorney Greg Gold and the Colorado legal team at The Gold Law Firm provide five scholarship awards each semester to first-time college freshmen within the United States. Each award is worth $1,000, and awards ”
### `8c33f63fb3d05fe3` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Kenneth Pettine Scholarship for Disabilities | Scholarship Overview The scholarship was established to support undergraduate students with disabilities who are pursuing higher education and striving to achieve academic and personal success. Through an annual essay contest, one student will recei”
### `8d09dea9175bdf29` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Rodolfo Giraldi Grant Future in Healthcare | The Dr. Rodolfo Giraldi Grant for Healthcare provides financial assistance to undergraduate students pursuing healthcare-related academic paths. The grant is open to students across the United States and is awarded based on the quality of an original ”
### `910eef21c5f8b302` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Steven Muscoreil Scholarship for Future Doctors | Scholarship OverviewThe Dr. Steven Muscoreil Scholarship for Future Doctors is a $1,000 academic award created to support undergraduate students who are committed to pursuing a career in medicine. This scholarship is awarded through a competitive”
### `95ae1bd73d1f65c0` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “Jared Kamrass Scholarship For Public Service | Scholarship OverviewThe Jared Kamrass Scholarship for Public Service was established by Jared Kamrass, a prominent Democratic political strategist and proud Ohioan. This scholarship aims to support and encourage students who share Jared Kamrass's passio”
### `9afcd971e39faf1b` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: High School, Undergraduate, Graduate ⟵ “Discover Scholarship Search | Free scholarship searchWant to easily find more scholarships? Use our college scholarship tool to search over 4 million scholarships worth more than $22 billion. No registration required.How to find scholarshipsStudents can customize their scholarship search to meet the”
### `9e3e239a55abc88b` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Ronald Bernardini Scholarship for Health Professionals | Scholarship OverviewThe Dr. Ronald Bernardini Scholarship for Health Professionals is a $1,000 annual award presented to one outstanding undergraduate student who is actively pursuing a career in the health professions. The scholarship is ”
### `a11b35e9f918a5d6` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Wells Call Annual Scholarship Contest | The Safer Roadways ScholarshipIn an effort to reduce the number of young drivers getting behind the wheel while under the influence, the lawyers at Wells Call are offering a $1500 scholarship to students.OverviewWe are asking students to write an essay of at l”
### `a54cb393ffc0f1c7` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Empowering Future Medical Leaders Dr. Andrew Hummel Scholarship Application | Scholarship OverviewThis scholarship aims to identify and reward students who exhibit a deep passion for healthcare and a commitment to clinical excellence. By participating in our annual essay contest, students have the o”
### `a9a970eaaea09041` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Wade Banker Scholarship for Medical Students | Scholarship Overview The Dr. Wade Banker Scholarship for Medical Students awards $1,000 to one exceptional undergraduate student who is actively preparing for a career in medicine.CriteriaTo be eligible for the Dr. Wade Banker Scholarship, you must ”
### `acf0ee788cc43425` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: High School, Undergraduate ⟵ “CardRates.com Financial Futures Scholarship | CardRates.com is proud to offer the Financial Futures Scholarship to future and current college students majoring in Business, Accounting, Finance, Mathematics, Management, and others preparing for a career in the personal finance industry.Applicants wil”
### `ad8c63803e26c489` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Keith D’Agostino Scholarship for Cancer Survivors | Scholarship OverviewThis annual essay contest provides a $1,000 scholarship to one deserving undergraduate student. The award is intended to help cover the costs of tuition, books, or other essential academic fees. By focusing on the intersection o”
### `b2abe1fe7ca3aee6` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Graduate ⟵ “Kaiser Permanente - Dr. Arturo Garzon Memorial Scholarship for Medical Students | We are proud of Kaiser Permanente’s social mission, research, clinical expertise, and leadership efforts in helping communities thrive. As part of this mission, we recognize the potential of future physicians and their”
### `b45a6f10e972c7e4` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Lynn Puana Scholarship for Medical Students | The Vision & PurposeAs healthcare evolves, so must our approach to patient care. Dr. Lynn Puana’s career has been defined by a transition from reactive treatment to proactive prevention—specifically within the realm of brain health and cellular medic”
### `b80c15dfe82a259f` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “Dr. Yorell Manon-Matos Scholarship for Healthcare Students | Scholarship OverviewThe Scholarship for Healthcare Students is an investment in the future of healthcare, empowering promising individuals to pursue their passions, excel in their academic endeavors, and make a meaningful difference in the”
### `bf76da4e07e6d8f7` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “S&G Scholarship for Veterans | Scholarship Overview The S&G Scholarship for Veterans was established to recognize the sacrifices, discipline, and resilience of military veterans who are pursuing undergraduate education. Transitioning from military service to academic life often requires determinatio”
### `cb6e2acc7ca99a02` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Dr. Ameer E. Hassan and Summer Abu Jemeza Hassan Grant | The Dr. Ameer E. Hassan and Summer Abu Jemeza Hassan Grant is a prestigious opportunity designed to support aspiring healthcare professionals dedicated to making a difference. With awards of $5,000, $2,000, and $1,000, this grant seeks to empo”
### `d5734a32e3d134ea` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “Dr. Timothy Francis Scholarship for Medical Students | Scholarship OverviewThis scholarship is established by Dr. Timothy Francis, a veteran practitioner with over 30 years of clinical experience in chiropractic care, applied kinesiology, and homeopathy. Recognizing the rigorous demands of medical t”
### `d7157007b1281256` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Graduate ⟵ “Kaiser Permanente - Northern California Residency Scholarship | We are proud of Kaiser Permanente’s social mission, research, clinical expertise, and leadership efforts in helping communities thrive. As part of this mission, we recognize the potential of future physicians and their contributions by ”
### `e4f2666e08b69c85` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Live Like Alex Scholarship | Honoring the Legacy of Alex Lawrence JohnsonAt Sumsion Business Law, we believe in investing in the next generation of leaders who live with integrity, service, and a commitment to bettering their communities. To honor the legacy of Alex Lawrence Johnson, we proudly offe”
### `e51490ad44871190` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate ⟵ “Supporting STEM Scholarship | Description of the Supporting STEM Scholarship A single award of $1,000, split evenly between fall and spring semester, will be sent to the financial aid office of the winning applicant’s academic institution where funds will be disbursed. The awarded funds may be used ”
### `eb517c66663093df` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “Value CPR Foundation Scholarship | ValueCPR is proud to present the Value CPR Foundation Scholarship Program for students aspiring to study or currently studying healthcare or education.Every 12 months we award a $1,500 scholarship to students pursuing careers in healthcare or education. We are thri”
### `ecbbdef480ded010` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “Dr. Jacqueline Youtsos Scholarship for Medical Students | Scholarship Overview The Dr. Jacqueline Youtsos Scholarship awards $1,000 to one undergraduate or medical student who demonstrates the same perseverance and patient-first mindset that defined Dr. Youtsos’s own journey from resident to cancer ”
### `ecd39b87c0e47e45` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “THE CROWDER LAW FIRM SCHOLARSHIP | The Crowder Law Firm offers two $1,000 scholarships twice a year to students pursuing higher education who strive to achieve excellent academic performance.All questions can be answered by our scholarship team at scholarship@crowdercriminalfirm.com. Please note tha”
### `ef2a63fbd0b92436` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: Undergraduate, Graduate ⟵ “K Altman Law Scholarship Fall 2027 | About the Fall 2027 ScholarshipK Altman Law has created a Fall 2027 scholarship to support students who want to make a positive impact through higher education.Eligibility CriteriaThis scholarship is open to any student currently enrolled in an accredited undergr”
### `f2708ccb023334c4` University of New England — awards 2026-27 [new] (labeled_in_source)
- source: https://www.une.edu/sfs/scholarships (sha256 3f25a217bb2b)
- checks: {"thresholds": null}
  - eligibility_summary: High School, Undergraduate ⟵ “Acker Warren Youth Mentor Scholarship | At the law firm of Acker Warren P.C., we believe that investing in youth is among the most impactful actions we can take for the future. To reflect this belief, our firm is excited to offer the Acker Warren Youth Mentor Scholarship! Inspired by Attorney Warren”
### `3e9c874c6aed8ddf` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Roberta and Joseph A. Zinni Music Scholarship | Music major.Enrolled full timeMaintain a minimum cumulative GPA of 2.67 | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music major.Enrolled full timeMaintain a minimum cumulative GPA of 2.67 ⟵ “Roberta and Joseph A. Zinni Music Scholarship | Music major.Enrolled full timeMaintain a minimum cumulative GPA of 2.67 | Award: Varies | Deadline: February 28”
### `3ec71986eee1f687` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: The number and amount of the award(s) will be based on available income. ⟵ “Kim Moody ’82 and Family Nursing Scholarship | Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSAUnderrepresented students who have an interest in staying in Maine preferred | Award: The number and amount of the award(s) will be based o”
  - eligibility_summary: Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSAUnderrepresented students who have an interest in staying in Maine preferred ⟵ “Kim Moody ’82 and Family Nursing Scholarship | Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSAUnderrepresented students who have an interest in staying in Maine preferred | Award: The number and amount of the award(s) will be based o”
### `410eef3310cf0ab6` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Robert Russell Music Scholarship | Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) ⟵ “Robert Russell Music Scholarship | Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
### `4141e6493b5c770a` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Edmund S. Muskie Memorial Scholarship | Matriculated into Muskie Program | Award: Varies | Deadline: Priority Deadline May 1”
  - eligibility_summary: Matriculated into Muskie Program ⟵ “Edmund S. Muskie Memorial Scholarship | Matriculated into Muskie Program | Award: Varies | Deadline: Priority Deadline May 1”
### `4ec2eeb184733363` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Jerry Bowder Scholarship | Music MajorEnrolled full timeMaintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music MajorEnrolled full timeMaintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) ⟵ “Jerry Bowder Scholarship | Music MajorEnrolled full timeMaintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) | Award: Varies | Deadline: February 28”
### `5054e49d9a78dbcc` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,000 ⟵ “ConnectED Pathways Scholarship | Students who earned an Associates Degree from a Maine Community CollegeStudents admitted through the ConnectED Pathways programCannot be combined with other Merit Scholarships | Award: $1,000 | Deadline: Associate’s degree must be on record with the Office of Admissi”
  - eligibility_summary: Students who earned an Associates Degree from a Maine Community CollegeStudents admitted through the ConnectED Pathways programCannot be combined with other Merit Scholarships ⟵ “ConnectED Pathways Scholarship | Students who earned an Associates Degree from a Maine Community CollegeStudents admitted through the ConnectED Pathways programCannot be combined with other Merit Scholarships | Award: $1,000 | Deadline: Associate’s degree must be on record with the Office of Admissi”
### `51392acdc46c26c0` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: The number and amount of the award(s) will be based on available income. ⟵ “E. June Clark and Irene Watson Nursing Scholarship | Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCertified nurse assistant or comparable credentials or statusCompleted FAFSA | Award: The number and amount of the award(s) will be based on availab”
  - eligibility_summary: Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCertified nurse assistant or comparable credentials or statusCompleted FAFSA ⟵ “E. June Clark and Irene Watson Nursing Scholarship | Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCertified nurse assistant or comparable credentials or statusCompleted FAFSA | Award: The number and amount of the award(s) will be based on availab”
### `54cee8a440c84c96` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: $6,800 ⟵ “The Osher Scholarship Program | First Year Student from York County (ME) High SchoolCompleted USM application and FAFSAFull-time student with at least 12 credits per fall and spring semesters | Award: $6,800 | Deadline: June 15”
  - eligibility_summary: First Year Student from York County (ME) High SchoolCompleted USM application and FAFSAFull-time student with at least 12 credits per fall and spring semesters ⟵ “The Osher Scholarship Program | First Year Student from York County (ME) High SchoolCompleted USM application and FAFSAFull-time student with at least 12 credits per fall and spring semesters | Award: $6,800 | Deadline: June 15”
### `58628d23ce8756d1` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1000 ⟵ “Charles J. and Judith F. ’87G Micoleau Scholarship | N/A | Award: $1000 | Deadline: Priority Deadline May 1”
### `5a10bc9897f0eb7b` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,500 ⟵ “Office of Graduate Studies Spring Scholarship | Be matriculated in a master's or doctoral degree at USMBe in good academic standing with a GPA of 3.0 or betterBe enrolled in at least 6 graduate credits for the Spring session(s)Have completed the FAFSA (non US citizens need not complete)Not be a Univ”
  - eligibility_summary: Be matriculated in a master's or doctoral degree at USMBe in good academic standing with a GPA of 3.0 or betterBe enrolled in at least 6 graduate credits for the Spring session(s)Have completed the FAFSA (non US citizens need not complete)Not be a University of Maine System employee (though student workers and Graduate Assistants are eligible) ⟵ “Office of Graduate Studies Spring Scholarship | Be matriculated in a master's or doctoral degree at USMBe in good academic standing with a GPA of 3.0 or betterBe enrolled in at least 6 graduate credits for the Spring session(s)Have completed the FAFSA (non US citizens need not complete)Not be a Univ”
### `61642b023b4f8c9c` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Helen Heel Music Scholarship | Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) ⟵ “Helen Heel Music Scholarship | Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
### `62c7669d35b8b6f9` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,000 ⟵ “Christopher ’04 and Lavinia ’04 Gelineau Memorial Scholarship | Cybersecurity, Information Technology, English or Foreign Languages majorPreference may be given to students who are serving in the Maine National Guard,a resident of Maine or Vermont,an immigrant who aspires to US citizenship, and,a me”
  - eligibility_summary: Cybersecurity, Information Technology, English or Foreign Languages majorPreference may be given to students who are serving in the Maine National Guard,a resident of Maine or Vermont,an immigrant who aspires to US citizenship, and,a meaningful experience that may be external to USM. ⟵ “Christopher ’04 and Lavinia ’04 Gelineau Memorial Scholarship | Cybersecurity, Information Technology, English or Foreign Languages majorPreference may be given to students who are serving in the Maine National Guard,a resident of Maine or Vermont,an immigrant who aspires to US citizenship, and,a me”
### `65b95096fecb8159` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: The number and amount of the award(s) will be based on available income. ⟵ “Boyne Family Nursing Scholarship | Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSAStudents interested in providing care for the elderly in health-care deprived areas in Maine preferred | Award: The number and amount of the award(s) w”
  - eligibility_summary: Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSAStudents interested in providing care for the elderly in health-care deprived areas in Maine preferred ⟵ “Boyne Family Nursing Scholarship | Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSAStudents interested in providing care for the elderly in health-care deprived areas in Maine preferred | Award: The number and amount of the award(s) w”
### `67f2c762b35f44cb` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Annual award amount $1,000-$2,000 ⟵ “USM Transfer Residence Hall Scholarship | Must indicate housing interest at time of admissionStudents must take a minimum of 12 credits during Fall and Spring semestersScholarship eligibility requires living on campus. | Award: Annual award amount $1,000-$2,000 | Deadline: April 1”
  - eligibility_summary: Must indicate housing interest at time of admissionStudents must take a minimum of 12 credits during Fall and Spring semestersScholarship eligibility requires living on campus. ⟵ “USM Transfer Residence Hall Scholarship | Must indicate housing interest at time of admissionStudents must take a minimum of 12 credits during Fall and Spring semestersScholarship eligibility requires living on campus. | Award: Annual award amount $1,000-$2,000 | Deadline: April 1”
### `687c681d90d8feaf` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,000 ⟵ “Office of Graduate Studies Summer Scholarship | Be matriculated in a master's or doctoral degree at USMBe in good academic standing with a GPA of 3.0 or betterBe enrolled in at least 3 graduate credits for the summer session(s)Have completed the FAFSA (non US citizens need not complete)Not be a Univ”
  - eligibility_summary: Be matriculated in a master's or doctoral degree at USMBe in good academic standing with a GPA of 3.0 or betterBe enrolled in at least 3 graduate credits for the summer session(s)Have completed the FAFSA (non US citizens need not complete)Not be a University of Maine System employee (though student workers and Graduate Assistants are eligible) ⟵ “Office of Graduate Studies Summer Scholarship | Be matriculated in a master's or doctoral degree at USMBe in good academic standing with a GPA of 3.0 or betterBe enrolled in at least 3 graduate credits for the summer session(s)Have completed the FAFSA (non US citizens need not complete)Not be a Univ”
### `69b8c24a0a209faf` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Typically $1000 ⟵ “Robert W. Berry Memorial Scholarship | School of Business majorMinimum 2.5 GPAInterest in technology and business | Award: Typically $1000 | Deadline: January 11, 2026”
  - eligibility_summary: School of Business majorMinimum 2.5 GPAInterest in technology and business ⟵ “Robert W. Berry Memorial Scholarship | School of Business majorMinimum 2.5 GPAInterest in technology and business | Award: Typically $1000 | Deadline: January 11, 2026”
### `69edacfeb38b3cfb` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Dr. and Mrs. Newell A. Augur, Jr. Scholarship | Music majorMaine State resident preferredMaintain a minimum cumulative GPA. ( 2.67 Undergraduate; 3.00 Graduate)Enrolled full time. (12 cr. Undergraduate; 6 cr. Graduate) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music majorMaine State resident preferredMaintain a minimum cumulative GPA. ( 2.67 Undergraduate; 3.00 Graduate)Enrolled full time. (12 cr. Undergraduate; 6 cr. Graduate) ⟵ “Dr. and Mrs. Newell A. Augur, Jr. Scholarship | Music majorMaine State resident preferredMaintain a minimum cumulative GPA. ( 2.67 Undergraduate; 3.00 Graduate)Enrolled full time. (12 cr. Undergraduate; 6 cr. Graduate) | Award: Varies | Deadline: February 28”
### `8004a7af6fdb35e0` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Music Merit Scholarship | Music majorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music majorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) ⟵ “Music Merit Scholarship | Music majorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
### `8566c408018710fd` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “USM Alumni Association Scholarship | Children, grandchildren, or spouses of USM alumniDemonstrate Financial Need on FAFSAIncoming Admitted Student | Award: Varies | Deadline: May 1”
  - eligibility_summary: Children, grandchildren, or spouses of USM alumniDemonstrate Financial Need on FAFSAIncoming Admitted Student ⟵ “USM Alumni Association Scholarship | Children, grandchildren, or spouses of USM alumniDemonstrate Financial Need on FAFSAIncoming Admitted Student | Award: Varies | Deadline: May 1”
### `878ed551b892470d` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Typically $1300 or more ⟵ “Dean John W. Bay Scholarship | School of Business majorMinimum 3.0 GPAExhibits leadership through volunteerism | Award: Typically $1300 or more | Deadline: January 11, 2026”
  - eligibility_summary: School of Business majorMinimum 3.0 GPAExhibits leadership through volunteerism ⟵ “Dean John W. Bay Scholarship | School of Business majorMinimum 3.0 GPAExhibits leadership through volunteerism | Award: Typically $1300 or more | Deadline: January 11, 2026”
### `8da8ba966147ee8a` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $500 ⟵ “Campbell Family Endowed Scholarship | Undeclared at the time of scholarship decisionMust have at least 12 USM earned creditsA maximum of 83 earned degree creditsA minimum cumulative GPA of 2.5Be a Maine resident and have demonstrated financial need as determined by the FAFSA 2024-2025 | Award: $500 ”
  - eligibility_summary: Undeclared at the time of scholarship decisionMust have at least 12 USM earned creditsA maximum of 83 earned degree creditsA minimum cumulative GPA of 2.5Be a Maine resident and have demonstrated financial need as determined by the FAFSA 2024-2025 ⟵ “Campbell Family Endowed Scholarship | Undeclared at the time of scholarship decisionMust have at least 12 USM earned creditsA maximum of 83 earned degree creditsA minimum cumulative GPA of 2.5Be a Maine resident and have demonstrated financial need as determined by the FAFSA 2024-2025 | Award: $500 ”
### `8e3740b989f23fb5` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Annual range $1,000 to $9,000 ⟵ “President’s Transfer Scholar | Merit ScholarshipCumulative transfer GPA 3.5 and above | Award: Annual range $1,000 to $9,000 | Deadline: April 1”
  - eligibility_summary: Merit ScholarshipCumulative transfer GPA 3.5 and above ⟵ “President’s Transfer Scholar | Merit ScholarshipCumulative transfer GPA 3.5 and above | Award: Annual range $1,000 to $9,000 | Deadline: April 1”
### `906070d19c0464fa` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Typically $1200 or more ⟵ “Gene R. Cohen Entrepreneurial Scholarship | School of Business majorAt least sophomore standingEngaged in Entrepreneurial pursuitsMust be a USA citizen or Permanent resident | Award: Typically $1200 or more | Deadline: January 11, 2026”
  - eligibility_summary: School of Business majorAt least sophomore standingEngaged in Entrepreneurial pursuitsMust be a USA citizen or Permanent resident ⟵ “Gene R. Cohen Entrepreneurial Scholarship | School of Business majorAt least sophomore standingEngaged in Entrepreneurial pursuitsMust be a USA citizen or Permanent resident | Award: Typically $1200 or more | Deadline: January 11, 2026”
### `96e7e15d0034c033` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Edith Speziali Music Scholarship | Music majorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA ( 2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music majorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA ( 2.67 Ugrd; 3.00 Grad) ⟵ “Edith Speziali Music Scholarship | Music majorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA ( 2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
### `9b65795f398e3b2f` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Ellen Chickering Music Scholarship | Music Vocal MajorEnrolled full timeMaintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music Vocal MajorEnrolled full timeMaintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) ⟵ “Ellen Chickering Music Scholarship | Music Vocal MajorEnrolled full timeMaintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) | Award: Varies | Deadline: February 28”
### `9d381f9e5ab1e254` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: The number and amount of the award(s) will be based on available income. ⟵ “Lorelle’s Nursing Scholarship | Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSA | Award: The number and amount of the award(s) will be based on available income. | Deadline: January 31”
  - eligibility_summary: Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSA ⟵ “Lorelle’s Nursing Scholarship | Accelerated Nursing Program (ABSN) Student or student otherwise already holding a Bachelor's DegreeCompleted FAFSA | Award: The number and amount of the award(s) will be based on available income. | Deadline: January 31”
### `a485c2a886d05a80` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Ronald Cole Music Scholarship | Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) ⟵ “Ronald Cole Music Scholarship | Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
### `ab8c1cbb8f05b25d` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $2,350 ⟵ “Constantine Kapothanasis Accounting Scholarship Fund | Accounting majorMinimum 2.0 GPADemonstrates promiseHas a good attitude | Award: $2,350 | Deadline: N/A”
  - eligibility_summary: Accounting majorMinimum 2.0 GPADemonstrates promiseHas a good attitude ⟵ “Constantine Kapothanasis Accounting Scholarship Fund | Accounting majorMinimum 2.0 GPADemonstrates promiseHas a good attitude | Award: $2,350 | Deadline: N/A”
### `b5b221e162204ecf` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Elizabeth S. Hagar Endowed Music Scholarship | Music major.Maintain a minimum cumulative GPA of 2.67Enroll in applied music and appropriate ensembles.Enrolled full time | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music major.Maintain a minimum cumulative GPA of 2.67Enroll in applied music and appropriate ensembles.Enrolled full time ⟵ “Elizabeth S. Hagar Endowed Music Scholarship | Music major.Maintain a minimum cumulative GPA of 2.67Enroll in applied music and appropriate ensembles.Enrolled full time | Award: Varies | Deadline: February 28”
### `b623ba9f970fb964` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Typically $1000 or more ⟵ “Otis Family Scholarship | School of Business majorMaine residentPreference given to Accounting and Finance majors | Award: Typically $1000 or more | Deadline: January 11, 2026”
  - eligibility_summary: School of Business majorMaine residentPreference given to Accounting and Finance majors ⟵ “Otis Family Scholarship | School of Business majorMaine residentPreference given to Accounting and Finance majors | Award: Typically $1000 or more | Deadline: January 11, 2026”
### `b76e769e3e5a6dfd` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Variable amounts up to $3,000 ⟵ “Office of Graduate Studies Scholarship | Be matriculated in a master's or doctoral degree at USM Be in good academic standing with a GPA of 3.0 or better Be enrolled in at least 6 graduate credits per semester Have completed the FAFSA (non US citizens need not complete) Not be a University of Maine ”
  - eligibility_summary: Be matriculated in a master's or doctoral degree at USM Be in good academic standing with a GPA of 3.0 or better Be enrolled in at least 6 graduate credits per semester Have completed the FAFSA (non US citizens need not complete) Not be a University of Maine System employee (though student workers and Graduate Assistants are eligible) ⟵ “Office of Graduate Studies Scholarship | Be matriculated in a master's or doctoral degree at USM Be in good academic standing with a GPA of 3.0 or better Be enrolled in at least 6 graduate credits per semester Have completed the FAFSA (non US citizens need not complete) Not be a University of Maine ”
### `baaf3812dcd84b9f` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,000 or more ⟵ “Peter Feeney Scholarship | Continuing Muskie studentsCompleted 12 creditsFinancial needCommitment to Public Service | Award: $1,000 or more | Deadline: Priority Deadline May 1”
  - eligibility_summary: Continuing Muskie studentsCompleted 12 creditsFinancial needCommitment to Public Service ⟵ “Peter Feeney Scholarship | Continuing Muskie studentsCompleted 12 creditsFinancial needCommitment to Public Service | Award: $1,000 or more | Deadline: Priority Deadline May 1”
### `bb95c16de70c5c2c` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,500 in the first year. Renewable for $1,000 in the second year. ⟵ “Leon and Lisa Gorman Scholarship | Completed Scholarship ApplicationCompleted USM Application for AdmissionCompleted FAFSAMinimum 24 credits earnedPreference 3.0 GPA | Award: $1,500 in the first year. Renewable for $1,000 in the second year. | Deadline: June 15”
  - eligibility_summary: Completed Scholarship ApplicationCompleted USM Application for AdmissionCompleted FAFSAMinimum 24 credits earnedPreference 3.0 GPA ⟵ “Leon and Lisa Gorman Scholarship | Completed Scholarship ApplicationCompleted USM Application for AdmissionCompleted FAFSAMinimum 24 credits earnedPreference 3.0 GPA | Award: $1,500 in the first year. Renewable for $1,000 in the second year. | Deadline: June 15”
### `bc8b6093686d9732` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Annual awards of up to $2,500 per semester or $5,000 per year, may be awarded for each student, as funds are available. ⟵ “ROCC Gratitude Annual Scholarship | Preference will be given to students who self-identify as in recovery for alcohol and/or drug addiction.Undergraduate studentEnrolled Full-Time (minimum 12 credit hours)Maintain a minimum GPA of 2.5Demonstrated Financial Need | Award: Annual awards of up to $2,500”
  - eligibility_summary: Preference will be given to students who self-identify as in recovery for alcohol and/or drug addiction.Undergraduate studentEnrolled Full-Time (minimum 12 credit hours)Maintain a minimum GPA of 2.5Demonstrated Financial Need ⟵ “ROCC Gratitude Annual Scholarship | Preference will be given to students who self-identify as in recovery for alcohol and/or drug addiction.Undergraduate studentEnrolled Full-Time (minimum 12 credit hours)Maintain a minimum GPA of 2.5Demonstrated Financial Need | Award: Annual awards of up to $2,500”
### `bf6fc6705963ed3b` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Music Talent Scholarship | Music majorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music majorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) ⟵ “Music Talent Scholarship | Music majorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
### `c23c623230885e7a` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Boulos Veterans Promise Completion Scholarship | USM VeteranDemonstrate financial needBe in good academic standingWithin 30 credits of completing bachelors degree or within 12 credits of completing graduate degree | Award: Varies | Deadline: Rolling Application”
  - eligibility_summary: USM VeteranDemonstrate financial needBe in good academic standingWithin 30 credits of completing bachelors degree or within 12 credits of completing graduate degree ⟵ “Boulos Veterans Promise Completion Scholarship | USM VeteranDemonstrate financial needBe in good academic standingWithin 30 credits of completing bachelors degree or within 12 credits of completing graduate degree | Award: Varies | Deadline: Rolling Application”
### `c551085ca44415a2` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: Annual range $1,000 to $7,000 ⟵ “USM Scholar Award | Merit Scholarship2.67 – 2.99 GPA (on a 4.0 scale) | Award: Annual range $1,000 to $7,000 | Deadline: April 1”
  - eligibility_summary: Merit Scholarship2.67 – 2.99 GPA (on a 4.0 scale) ⟵ “USM Scholar Award | Merit Scholarship2.67 – 2.99 GPA (on a 4.0 scale) | Award: Annual range $1,000 to $7,000 | Deadline: April 1”
### `caab77231065aa47` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Typically $1000 or more ⟵ “Bank of America Scholarship | School of Business majorMaine resident | Award: Typically $1000 or more | Deadline: January 11, 2026”
  - eligibility_summary: School of Business majorMaine resident ⟵ “Bank of America Scholarship | School of Business majorMaine resident | Award: Typically $1000 or more | Deadline: January 11, 2026”
### `cc7d68ff4f861bc3` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: Awards are multi-year and vary based upon a student’s eligibility for other federal, state, and institutional aid. ⟵ “Promise Scholarship | be an admitted, incoming first-year or transfer undergraduate to USMbe a full-time resident of Mainedemonstrate financial needdemonstrate a commitment to community service and civic engagement (preferred)be a first-generation college student (preferred)be referred from a partne”
  - eligibility_summary: be an admitted, incoming first-year or transfer undergraduate to USMbe a full-time resident of Mainedemonstrate financial needdemonstrate a commitment to community service and civic engagement (preferred)be a first-generation college student (preferred)be referred from a partnering youth-serving organization (preferred) ⟵ “Promise Scholarship | be an admitted, incoming first-year or transfer undergraduate to USMbe a full-time resident of Mainedemonstrate financial needdemonstrate a commitment to community service and civic engagement (preferred)be a first-generation college student (preferred)be referred from a partne”
### `cda9f4c782886521` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Philip and Joan Jagolinzer Scholarship | Completed a class in intermediate accounting or accounting theory at USMMinimum 3.3 GPA overallMinimum 3.4 GPA in accounting courses | Award: Varies | Deadline: N/A”
  - eligibility_summary: Completed a class in intermediate accounting or accounting theory at USMMinimum 3.3 GPA overallMinimum 3.4 GPA in accounting courses ⟵ “Philip and Joan Jagolinzer Scholarship | Completed a class in intermediate accounting or accounting theory at USMMinimum 3.3 GPA overallMinimum 3.4 GPA in accounting courses | Award: Varies | Deadline: N/A”
### `ce1a7a592f2b5515` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: Annual range $2,000 to $10,000 ⟵ “Dirigo Scholar Award | Merit Scholarship3.0 – 3.49 GPA (on a 4.0 scale) | Award: Annual range $2,000 to $10,000 | Deadline: April 1”
  - eligibility_summary: Merit Scholarship3.0 – 3.49 GPA (on a 4.0 scale) ⟵ “Dirigo Scholar Award | Merit Scholarship3.0 – 3.49 GPA (on a 4.0 scale) | Award: Annual range $2,000 to $10,000 | Deadline: April 1”
### `cfaefa7650dd7982` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1000 ⟵ “Maine Insurance Agents Association Scholarship | School of Business student with RMI concentration or RMI minor2.5 GPA or higherCompleted at least 54 credits (junior standing) | Award: $1000 | Deadline: N/A”
  - eligibility_summary: School of Business student with RMI concentration or RMI minor2.5 GPA or higherCompleted at least 54 credits (junior standing) ⟵ “Maine Insurance Agents Association Scholarship | School of Business student with RMI concentration or RMI minor2.5 GPA or higherCompleted at least 54 credits (junior standing) | Award: $1000 | Deadline: N/A”
### `d12ca3a17d862db5` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Up to $5,000 per academic year ⟵ “ReEntry Scholarship Program | Admitted to degree-seeking undergraduate programCumulative 5 year gap in pursuit of first bachelors degreeFinancial Need | Award: Up to $5,000 per academic year | Deadline: June 15th”
  - eligibility_summary: Admitted to degree-seeking undergraduate programCumulative 5 year gap in pursuit of first bachelors degreeFinancial Need ⟵ “ReEntry Scholarship Program | Admitted to degree-seeking undergraduate programCumulative 5 year gap in pursuit of first bachelors degreeFinancial Need | Award: Up to $5,000 per academic year | Deadline: June 15th”
### `d2cb4520acfd4339` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Key Bank Scholarship in Honor of Ken Curtis Fund | Matriculated into Muskie ProgramOutstanding academic recordFull time enrollment | Award: Varies | Deadline: Priority Deadline May 1”
  - eligibility_summary: Matriculated into Muskie ProgramOutstanding academic recordFull time enrollment ⟵ “Key Bank Scholarship in Honor of Ken Curtis Fund | Matriculated into Muskie ProgramOutstanding academic recordFull time enrollment | Award: Varies | Deadline: Priority Deadline May 1”
### `d9cd613409729d49` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Herbert & Sally Carroll Payson Scholarship | Music MajorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music MajorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) ⟵ “Herbert & Sally Carroll Payson Scholarship | Music MajorEnrolled full time (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA of 2.67 (Ugrd); 3.00 (Grad) | Award: Varies | Deadline: February 28”
### `da6501682919ed44` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “William Bingham, II Scholarship | Music MajorEnrolled full timeMaintain a minimum cumulative GPA appropriate to career level | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music MajorEnrolled full timeMaintain a minimum cumulative GPA appropriate to career level ⟵ “William Bingham, II Scholarship | Music MajorEnrolled full timeMaintain a minimum cumulative GPA appropriate to career level | Award: Varies | Deadline: February 28”
### `e26f4acda1c4c627` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $23,500 ⟵ “Joseph and Betty Stocks (’82) Nursing Scholarship | Matriculated Nursing Practitioner studentPreference given to students with families residing in Maine with a desire to work in Maine, especially in Rural areas | Award: $23,500 | Deadline: May 14”
  - eligibility_summary: Matriculated Nursing Practitioner studentPreference given to students with families residing in Maine with a desire to work in Maine, especially in Rural areas ⟵ “Joseph and Betty Stocks (’82) Nursing Scholarship | Matriculated Nursing Practitioner studentPreference given to students with families residing in Maine with a desire to work in Maine, especially in Rural areas | Award: $23,500 | Deadline: May 14”
### `e2fd4d6c7c16d61b` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,000 ⟵ “USM First Year Residence Hall Scholarship | Must indicate housing interest at time of admission.Students must take a minimum of 12 credits during Fall and Spring semesters.Scholarship eligibility requires living on campus. | Award: $1,000 | Deadline: April 1”
  - eligibility_summary: Must indicate housing interest at time of admission.Students must take a minimum of 12 credits during Fall and Spring semesters.Scholarship eligibility requires living on campus. ⟵ “USM First Year Residence Hall Scholarship | Must indicate housing interest at time of admission.Students must take a minimum of 12 credits during Fall and Spring semesters.Scholarship eligibility requires living on campus. | Award: $1,000 | Deadline: April 1”
### `e83deebdc2f1007c` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Madeleine D. Giguère Scholarship | USM degree student (Graduate or Undergraduate)Must express interest in Franco-American communityEnrolled in a minimum of 6 credits per semester | Award: Varies | Deadline: May 1”
  - eligibility_summary: USM degree student (Graduate or Undergraduate)Must express interest in Franco-American communityEnrolled in a minimum of 6 credits per semester ⟵ “Madeleine D. Giguère Scholarship | USM degree student (Graduate or Undergraduate)Must express interest in Franco-American communityEnrolled in a minimum of 6 credits per semester | Award: Varies | Deadline: May 1”
### `e8ded89c3441fab5` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “SMRT Stevens Scholarship | Study in an academic area that supports Architect and Engineering professionsDemonstrate Financial NeedEnroll in at least 6 credits per semester | Award: Varies | Deadline: June 15th”
  - eligibility_summary: Study in an academic area that supports Architect and Engineering professionsDemonstrate Financial NeedEnroll in at least 6 credits per semester ⟵ “SMRT Stevens Scholarship | Study in an academic area that supports Architect and Engineering professionsDemonstrate Financial NeedEnroll in at least 6 credits per semester | Award: Varies | Deadline: June 15th”
### `e8f983d64e7bdcba` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $12,000 ⟵ “Alfond Ambassador Scholarship | Academic excellenceLeasdership potentialShared vision for positively impacting Maine's economic futureDemonstrated dedication to fostering economic growth and innovation in Maine after graduation | Award: $12,000 | Deadline: March 15, 2026”
  - eligibility_summary: Academic excellenceLeasdership potentialShared vision for positively impacting Maine's economic futureDemonstrated dedication to fostering economic growth and innovation in Maine after graduation ⟵ “Alfond Ambassador Scholarship | Academic excellenceLeasdership potentialShared vision for positively impacting Maine's economic futureDemonstrated dedication to fostering economic growth and innovation in Maine after graduation | Award: $12,000 | Deadline: March 15, 2026”
### `e99b958eaea22ea6` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,000 ⟵ “Brian C. Hodgkin Dean’s Scholarship | Computer Science, Engineering, Environmental Science, or Technology majorCompleted FAFSA | Award: $1,000 | Deadline: January 31”
  - eligibility_summary: Computer Science, Engineering, Environmental Science, or Technology majorCompleted FAFSA ⟵ “Brian C. Hodgkin Dean’s Scholarship | Computer Science, Engineering, Environmental Science, or Technology majorCompleted FAFSA | Award: $1,000 | Deadline: January 31”
### `ec50f652f616cb3c` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: Amount Varies ⟵ “USM Access Scholarship | Students must not eligible to file a FAFSA for Federal Student Aid (including loans)First Year, Continuing, or Transfer StudentMatriculated into a degree program at USMPreference Given to Maine Residents | Award: Amount Varies | Deadline: June 15th”
  - eligibility_summary: Students must not eligible to file a FAFSA for Federal Student Aid (including loans)First Year, Continuing, or Transfer StudentMatriculated into a degree program at USMPreference Given to Maine Residents ⟵ “USM Access Scholarship | Students must not eligible to file a FAFSA for Federal Student Aid (including loans)First Year, Continuing, or Transfer StudentMatriculated into a degree program at USMPreference Given to Maine Residents | Award: Amount Varies | Deadline: June 15th”
### `eca09ee919b19757` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,000 per semester ⟵ “Honors Leadership Development Scholarship | Honors MinorMinimum of 3.5 GPACurrently enrolled in Honors classes | Award: $1,000 per semester | Deadline: Priority Deadline November 1st”
  - eligibility_summary: Honors MinorMinimum of 3.5 GPACurrently enrolled in Honors classes ⟵ “Honors Leadership Development Scholarship | Honors MinorMinimum of 3.5 GPACurrently enrolled in Honors classes | Award: $1,000 per semester | Deadline: Priority Deadline November 1st”
### `ed63fd2eebd9ec03` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Sport Management Scholarship | Sport Management majorMinimum 3.0 GPAEnrolled in Sport Management internship for upcoming academic year | Award: Varies | Deadline: N/A”
  - eligibility_summary: Sport Management majorMinimum 3.0 GPAEnrolled in Sport Management internship for upcoming academic year ⟵ “Sport Management Scholarship | Sport Management majorMinimum 3.0 GPAEnrolled in Sport Management internship for upcoming academic year | Award: Varies | Deadline: N/A”
### `ee7f0e5e5b773def` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Annual range $4,000 to $11,000 ⟵ “President’s Scholar Award | Merit ScholarshipAll qualified incoming first-year students are automatically considered3.5 and above GPA (on a 4.0 scale) | Award: Annual range $4,000 to $11,000 | Deadline: April 1”
  - eligibility_summary: Merit ScholarshipAll qualified incoming first-year students are automatically considered3.5 and above GPA (on a 4.0 scale) ⟵ “President’s Scholar Award | Merit ScholarshipAll qualified incoming first-year students are automatically considered3.5 and above GPA (on a 4.0 scale) | Award: Annual range $4,000 to $11,000 | Deadline: April 1”
### `ef2e07b1d5083df8` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $5,000 ⟵ “Marr-Anderson Family Foundation Scholarship | School of Business major or Education major | Award: $5,000 | Deadline: N/A”
  - eligibility_summary: School of Business major or Education major ⟵ “Marr-Anderson Family Foundation Scholarship | School of Business major or Education major | Award: $5,000 | Deadline: N/A”
### `f696dd5b40cb098d` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/?_scholarships_student_type=first-year (sha256 be548270e099)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Peter Martin Music Scholarship | Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) ⟵ “Peter Martin Music Scholarship | Music MajorEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
### `f8e70e612fb23dc9` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: $1,000 each award ⟵ “Mondor Memorial Scholarship | Preference for students self-identifying as in recovery from addictionMinimum 2.25 GPADemonstrated Financial NeedUndergraduate (taking a minimum of 6 credit hours) or graduate (taking a minimum of 3 credit hours) | Award: $1,000 each award | Deadline: Priority deadline ”
  - eligibility_summary: Preference for students self-identifying as in recovery from addictionMinimum 2.25 GPADemonstrated Financial NeedUndergraduate (taking a minimum of 6 credit hours) or graduate (taking a minimum of 3 credit hours) ⟵ “Mondor Memorial Scholarship | Preference for students self-identifying as in recovery from addictionMinimum 2.25 GPADemonstrated Financial NeedUndergraduate (taking a minimum of 6 credit hours) or graduate (taking a minimum of 3 credit hours) | Award: $1,000 each award | Deadline: Priority deadline ”
### `fa464373fe16de29` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Annual award amount of $2,000 to $4,000 ⟵ “Mountains to the Sea Scholarship | Residents of New Hampshire or VermontCompleted USM application and FAFSAFull-time student with at least 12 credits per semesterCannot be combined with other Merit Scholarships | Award: Annual award amount of $2,000 to $4,000 | Deadline: April 1”
  - eligibility_summary: Residents of New Hampshire or VermontCompleted USM application and FAFSAFull-time student with at least 12 credits per semesterCannot be combined with other Merit Scholarships ⟵ “Mountains to the Sea Scholarship | Residents of New Hampshire or VermontCompleted USM application and FAFSAFull-time student with at least 12 credits per semesterCannot be combined with other Merit Scholarships | Award: Annual award amount of $2,000 to $4,000 | Deadline: April 1”
### `fb795e579e074955` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “Churchill Family Music Scholarship | Music major - vocalEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
  - eligibility_summary: Music major - vocalEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) ⟵ “Churchill Family Music Scholarship | Music major - vocalEnrolled full time. (12 cr. Ugrd; 6 cr. Grad)Maintain a minimum cumulative GPA (2.67 Ugrd; 3.00 Grad) | Award: Varies | Deadline: February 28”
### `fe3ddedba0b05344` University of Southern Maine — awards 2026-27 [new] (source_unlabeled)
- source: https://usm.maine.edu/scholarships/ (sha256 6df382aacd9e)
- checks: {"thresholds": null}
  - award_amount_text: Award: Varies ⟵ “College of Education Scholarships | Current matriculated undergraduates who are in a teacher education major or pathwayOr, new or current graduate students who are matriculated in a program within the College of EducationEnrolled in at least six credits in the semester/s in which awarded. | Award: V”
  - eligibility_summary: Current matriculated undergraduates who are in a teacher education major or pathwayOr, new or current graduate students who are matriculated in a program within the College of EducationEnrolled in at least six credits in the semester/s in which awarded. ⟵ “College of Education Scholarships | Current matriculated undergraduates who are in a teacher education major or pathwayOr, new or current graduate students who are matriculated in a program within the College of EducationEnrolled in at least six credits in the semester/s in which awarded. | Award: V”
### `109489a4c968039d` Washington County Community College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://wccc.me.edu/admissions-aid/admissions/transfer-wccc/ (sha256 ac10dc3ce69b)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “In general, students are able to transfer credits to WCCC if: • The credits have been earned within the past ten years • The credits were earned with a grade of “C” or better • The courses are judged by WCCC to be equivalent in nature and content to WCCC’s course offerings.”
### `8bc483d639f61b4d` York County Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.yccc.edu/admissions-aid/paying-for-college/tuition-fees/ (sha256 6c6f36c76bde)
- checks: {"columns": 1, "rows": 2}
  - column:Tuition*: 2880 ⟵ “Tuition* | $2,880 | $4,320 | $5,760”
  - column:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200 | $1,200”
### `a428ca8e93c40767` York County Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.yccc.edu/admissions-aid/paying-for-college/tuition-fees/ (sha256 6c6f36c76bde)
- checks: {"columns": 1, "rows": 2}
  - column:Tuition*: 5760 ⟵ “Tuition* | $2,880 | $4,320 | $5,760”
  - column:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200 | $1,200”
### `3d732a7dd8bf853c` York County Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.yccc.edu/explore/academic-programs/high-school-programs/early-college/ (sha256 4f98d652ee42)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Students must have a cumulative high school GPA of 3.0 or be recommended by their school.”

## Exceptions (102)

### `855faa8dcc28fe32` state-ME — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.famemaine.com/affording-education/make-a-plan/maine-education-career-pathways/maine-college-transfer-agreements/ (sha256 31675636a014)
- issues: semantic_review_required
- checks: {"guarantees": 5, "requirements": 2}
  - statements.guarantees: 5 ⟵ “If you’re a Maine student who earned (or will earn) a high school diploma or equivalent in 2022, 2023, 2024 or 2025, you can attend Maine community college tuition free, but you’ll need to file the FAFSA first.”
  - statements.requirements: 2 ⟵ “FAME is not responsible for the products, services, and content on the Firstmark Services website.”
### `e6fa4b94a5866df8` Bowdoin College — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.bowdoin.edu/ir/pdf/bowdoin_cds_2024-2025.pdf (sha256 412379dad65e)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 13265 ⟵ “Total first-time, first-year (degree-seeking) who applied           475       7443            5347           0     13265”
  - admits: 946 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     65          804            77            0      946”
  - enrolled: 507 ⟵ “Total first-time, first-year (degree-seeking) enrolled              47          418            42            0      507”
  - sat_composite_25..75: [1470, 1510, 1540] ⟵ “SAT Composite                     1470                      1510                       1540”
  - sat_math_25..75: [740, 770, 780] ⟵ “SAT Math                           740                       770                       780”
  - act_25..75: [33, 34, 35] ⟵ “ACT Composite                      33                        34                         35”
### `1d1fb3a12df382f4` Bowdoin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bowdoin.edu/student-aid/cost-of-attendance/index.html (sha256 31f823de90c6)
- issues: conflicting_sources:https://www.bowdoin.edu/admissions/costs-and-aid/index.html
- checks: {"columns": 1, "rows": 7}
  - column:Tuition: 74268 ⟵ “Tuition | $74,268”
  - column:Fees: 700 ⟵ “Fees | $700”
  - column:Housing: 10106 ⟵ “Housing | $10,106”
  - column:Food *: 10326 ⟵ “Food * | $10,326”
  - column:Direct Costs Total: 95400 ⟵ “Direct Costs Total | $95,400”
  - column:Books, Course Materials, Supplies, & Equipment: 840 ⟵ “Books, Course Materials, Supplies, & Equipment | $840”
  - column:Miscellaneous Personal Expenses: 1660 ⟵ “Miscellaneous Personal Expenses | $1,660”
### `ada7e0187406eaa6` Bowdoin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bowdoin.edu/admissions/costs-and-aid/index.html (sha256 c27f74c10a92)
- issues: conflicting_sources:https://www.bowdoin.edu/student-aid/cost-of-attendance/index.html
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 74268 ⟵ “Tuition | $74,268”
  - column:Fees: 700 ⟵ “Fees | $700”
  - column:Housing: 10106 ⟵ “Housing | $10,106”
  - column:Food: 10326 ⟵ “Food | $10,326”
  - column:Direct Costs Total: 95400 ⟵ “Direct Costs Total | $95,400”
### `1bfbb584c6948900` Central Maine Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cmcc.edu/admissions-aid/paying-for-college/your-financial-aid-award/ (sha256 f070ece9aef8)
- issues: semantic_review_required, conflicting_sources:https://www.cmcc.edu/admissions-aid/paying-for-college/applying-for-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A review of the family’s special circumstances can be requested by contacting Student Financial Services.”
### `abd8dfa9701981d3` Central Maine Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cmcc.edu/admissions-aid/paying-for-college/applying-for-financial-aid/ (sha256 73d20c1d25a4)
- issues: semantic_review_required, conflicting_sources:https://www.cmcc.edu/admissions-aid/paying-for-college/your-financial-aid-award/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances If you believe you have special circumstances impacting your financial aid eligibility determination, please contact Student Financial Services at (207) 755-5328 or contact Student Financial Services.”
### `m2cb82351cf92d07` Central Maine Community College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://www.cmcc.edu/wp-content/uploads/2024/10/CMCC-AS-Business-Transfer-to-UMF-BA-Business-Administration-June-2026-SIGNED.pdf (sha256 ee310b3c126e)
- issues: conflicting_sources:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “As long as the coursework you want to transfer is equivalent to our requirements, and passed with a grade of C or better, we will award transfer credit.”
  - min_grade: C- ⟵ “For coursework to transfer to UMF, a student must earn a grade of C- or better.”
  - min_grade: C- ⟵ “Only courses in which a student has earned a grade of C- or higher are considered for transfer.”
### `mfd7ec0fe49f9853` Central Maine Community College — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.cmcc.edu/wp-content/uploads/2026/08/CMCC-AS-Business-Transfer-to-SJC-BS-Business-Administration-August-2026-SIGNED.pdf (sha256 3119a9e1146d)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “For coursework to transfer to SJC, a student must earn a grade of C or better.”
  - min_grade: C ⟵ “Only courses in which a student has earned a grade of C or higher are considered for transfer.”
  - min_grade: C ⟵ “For coursework to transfer to SJC, a student must earn a grade of C or better.”
  - min_grade: C ⟵ “Only courses in which a student has earned a grade of C or higher are considered for transfer.”
### `d8bccfe45aca5fea` Eastern Maine Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.emcc.edu/admissions/paying-for-college/financial-aid/financial-aid-changes/ (sha256 77415676ea2a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Changes sometimes occur during the academic year that can affect the family’s ability to contribute financially toward the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “A review of the family’s special circumstances can be requested by contacting the Financial Aid Office.”
### `64c5f388ac53d12e` Kennebec Valley Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kvcc.me.edu/wp-content/uploads/2026/07/KVCC-Satisfactory-Academic-Progress-Policy-Jan2026.pdf (sha256 9670fd6d5449)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal regulations specify death of a relative, a student injury or illness as reasonable grounds for appeal, though they do allow for “other special circumstances.” Examples of special circumstances could include divorce, loss of benefits or job, a documented disability or other circumstances beyond the reasonable control of the student.”
### `e2de43d0ca55771a` Kennebec Valley Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kvcc.me.edu/wp-content/uploads/2026/07/KVCC-Satisfactory-Academic-Progress-Policy-Jan2026.pdf (sha256 9670fd6d5449)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If the student files an appeal which is approved (See #16 below, Appeals Procedure) the student’s status can be changed to SAP Appealed-Academic Plan/Probation.”
  - sentence: sap_appeal ⟵ “If a student does not meet the standards for SAP: --And the student is returning after having been academically dismissed for failure to meet SAP, he/she must appeal both to the Academic Dean and the Financial Aid office.”
  - sentence: sap_appeal ⟵ “For appeals of failure to meet satisfactory academic progress, students with extenuating circumstances may submit WRITTEN appeals describing (in detail) their personal, medical or other unusual circumstances that warrant reconsideration of actions taken by the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “Students must also submit the KVCC Satisfactory Academic Progress (SAP) Appeal Form.”
### `f6b7183a7cb617bd` Kennebec Valley Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.kvcc.me.edu/admissions-financial-aid/tuition-aid/tuition-fees/ (sha256 f68ebe7511f1)
- issues: ambiguous_year_labels, arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition & Fees: 3866 ⟵ “Tuition & Fees | $3,866 | $3,866”
  - column:Books & Supplies: 1400 ⟵ “Books & Supplies | $1,400 | $1,400”
  - column:Living Expenses (rent and food): 7344 ⟵ “Living Expenses (rent and food) | $7,344 | $3,668”
  - column:Transportation: 2486 ⟵ “Transportation | $2,486 | $2,486”
  - column:Miscellaneous/Personal Exp: 3990 ⟵ “Miscellaneous/Personal Exp | $3,990 | $3,990”
  - column:Total: 19086 ⟵ “Total | $19,086 | $15,430”
  - column:Tuition & Fees: 3866 ⟵ “Tuition & Fees | $3,866 | $3,866”
  - column:Books & Supplies: 1400 ⟵ “Books & Supplies | $1,400 | $1,400”
  - column:Living Expenses (rent and food): 3668 ⟵ “Living Expenses (rent and food) | $7,344 | $3,668”
  - column:Transportation: 2486 ⟵ “Transportation | $2,486 | $2,486”
  - column:Miscellaneous/Personal Exp: 3990 ⟵ “Miscellaneous/Personal Exp | $3,990 | $3,990”
  - column:Total: 15430 ⟵ “Total | $19,086 | $15,430”
### `006fc80829b45545` Maine College of Art & Design — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://meca.edu/student-financial-services/tuition-and-costs-for-undergraduates/ (sha256 2443f1368707)
- issues: components_do_not_reconcile, conflicting_sources:https://meca.edu/student-financial-services/tuition-and-costs-for-mat/,https://meca.edu/student-financial-services/tuition-and-costs-for-salt/
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - column:Tuition: 44760 ⟵ “Tuition | $22,380 | $44,760 | $1,865/per credit hour”
  - column:Technology & Services Fee: 750 ⟵ “Technology & Services Fee | $375 | $750 | $375/ per semester”
  - column:*Lab Fees (Estimate): 675 ⟵ “*Lab Fees (Estimate) | $337.50 | $675 | varies by student”
  - column:**Room & Board (Estimate): 17180 ⟵ “**Room & Board (Estimate) | $8,590 | $17,180 | N/A”
  - column:Total: 67215 ⟵ “Total | $35,532.50 | $67,215 | varies by student”
### `5f7d1629a9ea7055` Maine College of Art & Design — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://meca.edu/student-financial-services/tuition-and-costs-for-mat/ (sha256 b97f590adced)
- issues: ambiguous_year_labels, components_do_not_reconcile, conflicting_sources:https://meca.edu/student-financial-services/tuition-and-costs-for-salt/,https://meca.edu/student-financial-services/tuition-and-costs-for-undergraduates/
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition: 26460 ⟵ “Tuition | $13,230 | $26,460”
  - column:Enrollment Fee: 300 ⟵ “Enrollment Fee | $300 | $300”
  - column:**Estimated Housing Costs: 15930 ⟵ “**Estimated Housing Costs | $7,965 | $15,930”
  - column:Total: 47463 ⟵ “Total | $26,088 | $47,463”
### `c3a88ae71740ef0a` Maine College of Art & Design — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://meca.edu/student-financial-services/tuition-and-costs-for-salt/ (sha256 2dc230155335)
- issues: ambiguous_year_labels, conflicting_sources:https://meca.edu/student-financial-services/tuition-and-costs-for-mat/,https://meca.edu/student-financial-services/tuition-and-costs-for-undergraduates/
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 13280 ⟵ “Tuition | $13,280”
  - column:Enrollment Fee: 300 ⟵ “Enrollment Fee | $300”
  - column:Technology & Services Fee: 200 ⟵ “Technology & Services Fee | $200”
  - column:Orientation Fee: 75 ⟵ “Orientation Fee | $75”
  - column:*Estimated Housing Costs: 6900 ⟵ “*Estimated Housing Costs | $6,900”
### `6d642ff45faf1369` Maine College of Art & Design — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://meca.edu/academics/transfer-credit/ (sha256 3f66e3de64a2)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `0923e19654e2ed39` Maine Maritime Academy — appeals 2026-27 [new] (source_unlabeled)
- source: https://mainemaritime.edu/admissions/wp-content/uploads/sites/4/2024/07/SAP-Appeal-Form.pdf (sha256 05521b2f12a7)
- issues: semantic_review_required, conflicting_sources:https://mainemaritime.edu/admissions/general-admissions/financial-aid/forms/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS (SAP) APPEAL FORM To receive financial aid, all new, transfer, continuing and returning students must demonstrate they are successfully working toward completing their degree program in a timely manner.”
  - sentence: sap_appeal ⟵ “If there were justifiable reasons or extenuating circumstances that made you unable to meet the GPA and completion requirements noted below, you may submit an SAP appeal (with supporting documentation) to the financial aid office to regain financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Registrar Signature: _____________________________________________ Date: __________________ Office of Financial Aid | (207) 326-2339 | 1 Pleasant St | Quick Hall | financialaid@mma.edu SATISFACTORY ACADEMIC PROGRESS (SAP) APPEAL FORM Section 5: Reason for Appeal Special Circumstance Recommended Documentation Severe illness, medical condition, or Signed and dated letter from physician on office let”
### `0990cbf5cbd949e3` Maine Maritime Academy — appeals 2026-27 [new] (source_unlabeled)
- source: https://mainemaritime.edu/admissions/wp-content/uploads/sites/4/2024/07/Institutional-Aid-Scholarship-Appeal-Form.pdf (sha256 b68afe6aced8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Fall _____ Spring _____ Year __________ Section 2: Explanation of Special Circumstances Describe the circumstances that prevented you from meeting the scholarship retention requirements.”
### `634b8fe43fe5bbc1` Maine Maritime Academy — appeals 2026-27 [new] (source_unlabeled)
- source: https://mainemaritime.edu/admissions/wp-content/uploads/sites/4/2024/07/Institutional-Aid-Scholarship-Appeal-Form.pdf (sha256 b68afe6aced8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “SCHOLARSHIP APPEAL FORM If you wish to appeal a scholarship decision, please complete this form and provide detailed reasons for your appeal along with any supporting documentation.”
### `dfdfbc9410e8101d` Maine Maritime Academy — appeals 2026-27 [new] (source_unlabeled)
- source: https://mainemaritime.edu/admissions/general-admissions/financial-aid/forms/ (sha256 2f7c01b0772b)
- issues: semantic_review_required, conflicting_sources:https://mainemaritime.edu/admissions/wp-content/uploads/sites/4/2024/07/SAP-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “This application may be submitted to Maine Maritime Academy’s Office of Financial Aid via email (financialaid@mma.edu) or by mail (1 Pleasant Street Castine, ME 04420) MMA Scholarship Application Appeal Forms Satisfactory Academic Progress Appeal Form Institutional Aid Appeal Form MMA Financial Aid PortalLogin to complete forms and accept awards MMA does its best to meet the need of its students.”
### `df5e099062d53fca` Maine Maritime Academy — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://mainemaritime.edu/admissions/wp-content/uploads/sites/4/2026/04/2026-2027-MMA-Cost-of-Attendance.pdf (sha256 6e16a9996bd0)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 9, "rows": 32}
  - column:General Fees: 552 ⟵ “General Fees | $ ,552 | General Fees | $ ,552 | General Fees | $ ,552”
  - column:Medical Insurance1: 250 ⟵ “Medical Insurance1 | $2,50 | Medical Insurance1 | $2,50 | Medical Insurance1 | $2,50”
  - column:Uniforms & Reg Items*: 1 ⟵ “Uniforms & Reg Items* | $ , 01 | Uniforms & Reg Items* | $ , 01 | Uniforms & Reg Items* | $ , 01”
  - column:$44,960: 51228 ⟵ “$44,960 | $51,228 | $61,264”
  - column:Books: 1200 ⟵ “Books | $1,200 | Books | $1,200 | Books | $1,200”
  - column:Personal/Misc.: 2000 ⟵ “Personal/Misc. | $2,000 | Personal/Misc. | $2,000 | Personal/Misc. | $2,000”
  - column:Travel: 1200 ⟵ “Travel | $1,200 | Travel | $1, 00 | Travel | $2,200”
  - column:Laptop: 1640 ⟵ “Laptop | $1,640 | Laptop | $1,640 | Laptop | $1,640”
  - column:n: 6040 ⟵ “n | $6,040 | n | $6,540 | n | $ ,040”
  - column:General Fees (2): 552 ⟵ “General Fees | $ ,552 | General Fees | $ ,552 | General Fees | $ ,552”
  - column:Medical Insurance1 (2): 250 ⟵ “Medical Insurance1 | $2,50 | Medical Insurance1 | $2,50 | Medical Insurance1 | $2,50”
  - column:$ 1, 21: 589 ⟵ “$ 1, 21 | $ ,589 | $4 ,625”
  - column:Books (2): 1200 ⟵ “Books | $1,200 | Books | $1,200 | Books | $1,200”
  - column:Personal/Misc. (2): 2000 ⟵ “Personal/Misc. | $2,000 | Personal/Misc. | $2,000 | Personal/Misc. | $2,000”
  - column:Travel (2): 1200 ⟵ “Travel | $1,200 | Travel | $1,700 | Travel | $2,200”
  - column:Laptop (2): 1640 ⟵ “Laptop | $1,640 | Laptop | $1,640 | Laptop | $1,640”
  - column:n (2): 6040 ⟵ “n | $6,040 | n | $6,540 | n | $ ,040”
  - column:n a: 418 ⟵ “n a | $418 | $6,268 | $12,5 6 | Graduate | $250”
  - column:Alu n A an a: 600 ⟵ “Alu n A an a | $600”
  - column:LATE OR NON-REGISTRATION OR RE-INSTATEMENT FEE: 100 ⟵ “LATE OR NON-REGISTRATION OR RE-INSTATEMENT FEE | $100”
  - column:$1,22: 2446 ⟵ “$1,22 | $2,446”
  - column:$1,22 (2): 2446 ⟵ “$1,22 | $2,446”
  - column:n a u: 919 ⟵ “n a u | $ ,919 | $ ,8 8 | a | $62 per term | $1,246”
  - column:u: 1292 ⟵ “u | $1,292 | $2,584 | a al | a n n | n n al | n , a n | l ,”
  - column:10: 50 ⟵ “10 | $50 | $1 5 | $ 50 | an | an a | a | ($545 per term) | $1,090”
  - … 100 more rows
### `723610bedd896534` Saint Joseph's College of Maine — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sjcme.edu/wp-content/uploads/2025/10/SJCME-FAFSA_A-Second-Look-Appeal.pdf (sha256 ebbc1d33c9d9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “O  nce we’ve received this, we’ll review the information to see if we can use “professional judgment” to adjust your award.”
### `a882841d4b574162` Saint Joseph's College of Maine — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/financial-aid/ (sha256 f23e02dc7974)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “While maintaining the flexibility to respond to individual student circumstances, the Financial Aid Office also strives for consistency in treatment of students with similar unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “All income adjustments must be used to address special circumstances where the data elements on the ISIR—based on income from the base year—no longer reflect the family’s (or student’s) ability to contribute to the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “In addition, students (and parents) will need to submit a formal request for an assessment of special circumstances.”
### `dfdaf1c78faa2c03` Saint Joseph's College of Maine — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/financial-aid/ (sha256 20d3cdb79b43)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: professional_judgment ⟵ “Professional judgment changes are made when the financial aid administrator judges the standards used to determine the SAI are inappropriate for purposes of calculating eligibility for financial aid due to extenuating circumstances.”
  - sentence: professional_judgment ⟵ “Saint Joseph’s College uses Department of Education software to re-compute the SAI both for corrections to reported data and for changes resulting when professional judgment is exercised.”
  - sentence: professional_judgment ⟵ “Potential Reasons for Exercise of Professional Judgment All professional judgment changes apply only to data element changes and apply to all Title IV programs.”
  - sentence: professional_judgment ⟵ “Satisfactory Academic Progress Financial Aid Specialists will be granted the use of “professional judgment” when participating on the Financial Aid Appeal Committee.”
  - sentence: professional_judgment ⟵ “Drop of Income and Income Adjustments The ability to use professional judgment for adjustments of data elements on the ISIR is granted to the Appeals Committee, Director.”
  - sentence: professional_judgment ⟵ “Third party documentation of changed circumstances should be used, whenever possible, to document the request for professional judgment.”
### `f0cfbce45f076e39` Saint Joseph's College of Maine — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sjcme.edu/wp-content/uploads/2025/10/SJCME-FAFSA_A-Second-Look-Appeal.pdf (sha256 ebbc1d33c9d9)
- issues: semantic_review_required, conflicting_sources:https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/faqs/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “C  omplete our Special Circumstance form, and provide any documents or information we ask for.”
  - sentence: need_based_special_circumstances ⟵ “On the Special Circumstance form, we ask you to provide some details about the situation and may also ask you for some documentation of what’s happening.”
### `fd56402d300394d7` Saint Joseph's College of Maine — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/faqs/ (sha256 6c780b113937)
- issues: semantic_review_required, conflicting_sources:https://www.sjcme.edu/wp-content/uploads/2025/10/SJCME-FAFSA_A-Second-Look-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You can request our Special Circumstances Form to report these changes.”
### `f9124a09f5ac4224` Saint Joseph's College of Maine — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sjcme.edu/admissions/oncampus/tuition-and-aid/financial-aid/ (sha256 f23e02dc7974)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 45744 ⟵ “Tuition and Fees | $45,744”
  - column:Housing and Food: 15846 ⟵ “Housing and Food | $15,846”
  - column:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200”
  - column:Transportation: 500 ⟵ “Transportation | $500”
  - column:Miscellaneous Personal Expenses: 1260 ⟵ “Miscellaneous Personal Expenses | $1,260”
  - column:Total Estimated Cost: 64550 ⟵ “Total Estimated Cost | $64,550”
### `8721052696ace4e6` Saint Joseph's College of Maine — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.sjcme.edu/wp-content/uploads/2026/08/2026-CMCC-and-SJC-Online-Transfer-Agreement.pdf (sha256 2bed43fdcb0c)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “A grade of C or higher is required for transfer credit.”
  - min_grade: C ⟵ “For coursework to transfer to SJC, a student must earn a grade of C or better.”
  - min_grade: C ⟵ “Only courses in which a student has earned a grade of C or higher are considered for transfer.”
### `bb75b7b7210d6d7d` Southern Maine Community College — costs 2019-20 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smccme.edu/about/quick-facts/ (sha256 6458b0b5cd64)
- issues: residency_unknown, stale_year_label:2019-20
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 2703.0 ⟵ “Tuition | $2,703.00”
  - column:Mixed Fees: 1062.0 ⟵ “Mixed Fees | $1,062.00”
  - column:Books & Supplies: 1556.0 ⟵ “Books & Supplies | $1,556.00”
  - column:Room or Residence: 5750.0 ⟵ “Room or Residence | $5,750.00”
  - column:Meals: 3450.0 ⟵ “Meals | $3,450.00”
### `cf9cb758f0f43446` Southern Maine Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.smccme.edu/admissions-aid/tuition-fees/ (sha256 9ef003d79542)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (full-time): 5760 ⟵ “Tuition (full-time) | $2,880 | $5,760”
  - column:Room, Meal Plan & Cable/Internet Fee: 12040 ⟵ “Room, Meal Plan & Cable/Internet Fee | $12,040 | $12,040”
  - column:Average Fees: 1276 ⟵ “Average Fees | $1,276 | $1,276”
### `e23ba827639d47eb` Southern Maine Community College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.smccme.edu/admissions-aid/tuition-fees/ (sha256 9ef003d79542)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (full-time): 2880 ⟵ “Tuition (full-time) | $2,880 | $5,760”
  - column:Room, Meal Plan & Cable/Internet Fee: 12040 ⟵ “Room, Meal Plan & Cable/Internet Fee | $12,040 | $12,040”
  - column:Average Fees: 1276 ⟵ “Average Fees | $1,276 | $1,276”
### `f4dbbeb450e33022` Southern Maine Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smccme.edu/admissions-aid/tuition-fees/ (sha256 e6889f7f6e2b)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 2703.0 ⟵ “Tuition | $2,703.00”
  - column:Mixed Fees: 1062.0 ⟵ “Mixed Fees | $1,062.00”
  - column:Books & Supplies: 1556.0 ⟵ “Books & Supplies | $1,556.00”
  - column:Room or Residence: 5750.0 ⟵ “Room or Residence | $5,750.00”
  - column:Meals: 3450.0 ⟵ “Meals | $3,450.00”
### `f55879942bd32da7` Southern Maine Community College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smccme.edu/admissions-aid/tuition-fees/tuition-calculator/ (sha256 a202ad4e5cdb)
- issues: residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 2703.0 ⟵ “Tuition | $2,703.00”
  - column:Mixed Fees: 1062.0 ⟵ “Mixed Fees | $1,062.00”
  - column:Books & Supplies: 1556.0 ⟵ “Books & Supplies | $1,556.00”
  - column:Room or Residence: 5750.0 ⟵ “Room or Residence | $5,750.00”
  - column:Meals: 3450.0 ⟵ “Meals | $3,450.00”
### `f73a6abb14894533` Southern Maine Community College — costs 2022-23 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smccme.edu/admissions-aid/financial-aid/ (sha256 4a85c8c7801e)
- issues: residency_unknown, stale_year_label:2022-23
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 2703.0 ⟵ “Tuition | $2,703.00”
  - column:Mixed Fees: 1062.0 ⟵ “Mixed Fees | $1,062.00”
  - column:Books & Supplies: 1556.0 ⟵ “Books & Supplies | $1,556.00”
  - column:Room or Residence: 5750.0 ⟵ “Room or Residence | $5,750.00”
  - column:Meals: 3450.0 ⟵ “Meals | $3,450.00”
### `fed4b5a95240244a` Southern Maine Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.smccme.edu/admissions-aid/veterans/ (sha256 b899d0be6b3e)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 2703.0 ⟵ “Tuition | $2,703.00”
  - column:Mixed Fees: 1062.0 ⟵ “Mixed Fees | $1,062.00”
  - column:Books & Supplies: 1556.0 ⟵ “Books & Supplies | $1,556.00”
  - column:Room or Residence: 5750.0 ⟵ “Room or Residence | $5,750.00”
  - column:Meals: 3450.0 ⟵ “Meals | $3,450.00”
### `2710e13869cb427d` Thomas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/ (sha256 b9f6ba5ded50)
- issues: semantic_review_required, conflicting_sources:https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-appeal/,https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/professional-judgement/,https://www.thomas.edu/admissions-aid/financial-aid/student-billing-faq/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgement Disclosure Professional Judgement is a process performed by the financial aid office to re-evaluate, and potentially adjust, FAFSA data based on a student’s specific situation.”
### `51c9b2b0b29bcc29` Thomas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/professional-judgement/ (sha256 dd86bdaf3692)
- issues: semantic_review_required, conflicting_sources:https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-appeal/,https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/,https://www.thomas.edu/admissions-aid/financial-aid/student-billing-faq/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgement: Financial Aid Appeal: Thomas College ME Exciting Upcoming Events!”
  - sentence: professional_judgment ⟵ “Two forms of Professional Judgement are considered at Thomas College.”
### `61db436fcb51533e` Thomas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-appeal/ (sha256 25567864e73b)
- issues: semantic_review_required, conflicting_sources:https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/professional-judgement/,https://www.thomas.edu/admissions-aid/financial-aid/financial-forms-resources/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Student Financial Services Office: AD-104 Suite Phone: 207-859-1110 Email: [email protected] This type of appeal is a formal, documented request asking a college financial aid office to reconsider a student’s eligibility for aid due to special circumstances, such as job loss, high medical bills, or, in some cases, to reinstate aid lost for not meeting academic requirements.”
  - sentence: need_based_special_circumstances ⟵ “Also known as a “special circumstances appeal,” this process requires a letter and supporting documents to justify a change in the aid award.”
### `6c0bd9ecb1476029` Thomas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomas.edu/admissions-aid/financial-aid/student-billing-faq/ (sha256 d54dc07e03d7)
- issues: semantic_review_required, conflicting_sources:https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-appeal/,https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/,https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/professional-judgement/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If your family has been impacted financially, such as job loss, please contact the Office of Student Financial Services at 207-859-1110 to discuss an appeal or professional judgement adjustment to your FAFSA.”
  - sentence: professional_judgment ⟵ “A professional judgement should be considered for situations such as job loss, medical bills not covered by insurance, or other extenuating circumstances that may not be reflected in your current FAFSA.”
### `70955ab1856abda7` Thomas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/professional-judgement/ (sha256 dd86bdaf3692)
- issues: semantic_review_required, conflicting_sources:https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-appeal/,https://www.thomas.edu/admissions-aid/financial-aid/financial-forms-resources/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance – financial situations (loss of a job, high unexpected medical bills, etc.) that justify an aid administrator adjusting data elements in the Cost of Attendance or in the Estimated Family Contribution Calculation.”
  - sentence: need_based_special_circumstances ⟵ “Students who feel they meet the above definition will be asked to submit the following documents to the Senior Director of Student Financial Services: Completed, signed, and dated institutional form to request the unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Students who believe an unusual circumstance exists should contact Student Financial Services at (207) 859-1110 or [email protected].”
### `f9a6aa29fc7ec801` Thomas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-appeal/ (sha256 25567864e73b)
- issues: semantic_review_required, conflicting_sources:https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/,https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/professional-judgement/,https://www.thomas.edu/admissions-aid/financial-aid/student-billing-faq/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Before proceeding with an appeal request, please read this Professional Judgement Disclosure.”
### `ff8832e41ded728a` Thomas College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomas.edu/admissions-aid/financial-aid/financial-forms-resources/ (sha256 144af8a41fdc)
- issues: semantic_review_required, conflicting_sources:https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-appeal/,https://www.thomas.edu/admissions-aid/financial-aid/financial-aid-policies/professional-judgement/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “What How can I appeal my financial aid decision due to special circumstances?”
  - sentence: need_based_special_circumstances ⟵ “If you have encountered special circumstances such as job loss, high medical bills, or, in some cases, to reinstate aid lost for not meeting academic requirements, you may fill out our financial aid appeal form.”
### `5cfe9bd583f60a8c` Unity Environmental University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://unity.edu/pineland/paying-for-college/tuition/ (sha256 9a2480b65fd7)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - column:Tuition (30 credits): 11250 ⟵ “Tuition (30 credits) | $11,250”
  - column:Fees: 1360 ⟵ “Fees | $1,360”
  - column:Course materials: 800 ⟵ “Course materials | $800”
  - column:Insurance: 3340 ⟵ “Insurance | $3,340”
  - column:Your estimated total per year: 16760 ⟵ “Your estimated total per year | $16,760”
### `f8c861d273d1f03f` Unity Environmental University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://unity.edu/distance-education/tuition-and-financial-aid/ (sha256 60a2adc56068)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "rows": 3}
  - column:Annual Tuition (30 credits): 14100 ⟵ “Annual Tuition (30 credits) | $14,100 | $12,690”
  - column:Course Materials: 800 ⟵ “Course Materials | $800 | $800”
  - column:Annual Total* (30 credits): 15000 ⟵ “Annual Total* (30 credits) | $15,000 | $13,590”
  - other:Annual Tuition (30 credits): 12690 ⟵ “Annual Tuition (30 credits) | $14,100 | $12,690”
  - other:Course Materials: 800 ⟵ “Course Materials | $800 | $800”
  - other:Annual Total* (30 credits): 13590 ⟵ “Annual Total* (30 credits) | $15,000 | $13,590”
### `3f1594c0a0580eec` University of Maine at Augusta — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uma.edu/financial/policies/sap/ (sha256 7f54b161e3c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You may submit a satisfactory academic progress appeal.”
  - sentence: sap_appeal ⟵ “THE APPEAL PROCESS Students who are on Financial Aid Suspension due to failure to meet the satisfactory academic progress standards have two options: Appeal your Financial Aid Suspension- complete and submit a Satisfactory Academic Progress Appeal (available on our website) with corresponding documentation for review.”
### `b2fc3f88a19f18ae` University of Maine at Augusta — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uma.edu/financial/policies/sap/ (sha256 7f54b161e3c4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal of Financial Aid Suspension A student placed on Financial Aid Suspension who has experienced undue hardship, (ie. death of a relative of the student; personal injury or prolonged illness of the student; or special circumstances as determined by the institution.), may submit a written appeal, normally within 30 days of notification, to the Office of Financial Aid.”
### `e40b7ab972994077` University of Maine at Augusta — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uma.edu/financial/scholarships/uma-10k/ (sha256 c0e814328c8f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Financial Aid retains the right to use professional judgment when awarding and reviewing scholarship awards.”
### `00c413adab1656eb` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Currently a UMA freshman or sophomore Demonstrated proficiency in math ⟵ “Kenneth C. Ward Scholarship | Currently a UMA freshman or sophomore Demonstrated proficiency in math | No application required, selection made by UMA representatives”
### `01e977dbbe1e8e15` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Named after former President Richard J. Randall, and Mary Elisabeth, Vice President Emerita of Enrollment Management. Must be enrolled in a degree program Minimum G.P.A. of 3.25 ⟵ “Richard J. and Mary Elisabeth Randall Scholarship | Named after former President Richard J. Randall, and Mary Elisabeth, Vice President Emerita of Enrollment Management. Must be enrolled in a degree program Minimum G.P.A. of 3.25 | No application required, selection made by UMA representatives”
### `02f4edeec81bfa79` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Current UMA student with sophomore standing (30 – 45 credits) Plans for a career in government or public service Good academic standing Reside in Augusta area (zip: 04300-04399) Demonstrated financial need* ⟵ “Calumet Educational & Literary Foundation Scholarship Award | Current UMA student with sophomore standing (30 – 45 credits) Plans for a career in government or public service Good academic standing Reside in Augusta area (zip: 04300-04399) Demonstrated financial need* | General Scholarship Applicati”
### `055d03b547eafdc2` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Augusta-based Criminal Justice Major Current or previous military experience Completed at least 30 academic credits ⟵ “M. Richard Cameron Scholarship | Augusta-based Criminal Justice Major Current or previous military experience Completed at least 30 academic credits | General Scholarship Application”
### `057be4504bb3b60c` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Cony High School graduate Demonstrated financial need* ⟵ “Cony High School Scholarship | Cony High School graduate Demonstrated financial need* | General Scholarship Application”
### `0f269d72c11eff3b` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Currently enrolled student Resides in greater Augusta area Academic excellence Involved in community service Demonstrated financial need* ⟵ “Augusta Rotary Club Scholarship | Currently enrolled student Resides in greater Augusta area Academic excellence Involved in community service Demonstrated financial need* | General Scholarship Application”
### `1000155c37a5ff05` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: UMA Bangor campus student Completed a minimum of 30 credits Single parent who has overcome hardship to attend UMA Bangor Demonstrated financial need* ⟵ “Vivian B. Raymond Scholarship Fund | UMA Bangor campus student Completed a minimum of 30 credits Single parent who has overcome hardship to attend UMA Bangor Demonstrated financial need* | No application required, selection made by UMA representatives”
### `1a96d70856567c99` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: UMA Bangor campus student Demonstrated financial need* ⟵ “Bruce Collier Memorial Scholarship | UMA Bangor campus student Demonstrated financial need* | No application required, selection made by UMA representatives”
### `20c1f1b4ba1f9549` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Awarded to student’s from the Greater Portland area ⟵ “Edna L. Higgins Scholarship | Awarded to student’s from the Greater Portland area | No application required, selection made by UMA representatives”
### `26726ad438be1914` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Academic Merit Demonstrated financial need* Completed first two years of Architectural studio courses ⟵ “American Institute of Architects Maine Chapter Scholarship | Academic Merit Demonstrated financial need* Completed first two years of Architectural studio courses | General Scholarship Application”
### `299f3d22d76b6532` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Awarded to student’s from the Greater Portland area Active participation in athletics and recreational activities ⟵ “C. Richard Haskell Scholarship | Awarded to student’s from the Greater Portland area Active participation in athletics and recreational activities | No application required, selection made by UMA representatives”
### `32dba29123f0265a` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: UMA Bangor campus student Majoring in Criminal Justice Good academic standing Demonstrated financial need* ⟵ “Cecil E. Powers Scholarship | UMA Bangor campus student Majoring in Criminal Justice Good academic standing Demonstrated financial need* | No application required, selection made by UMA representatives”
### `3c3c159799250173` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: UMA Music student who exhibits positive attitude, determination, imagination and a creative spirit ⟵ “Patrick J. Sullivan Memorial Scholarship | UMA Music student who exhibits positive attitude, determination, imagination and a creative spirit | General Scholarship Application”
### `3ccaea51794dfa4e` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Pursuing a degree in music Demonstrated talent, ability, and motivation ⟵ “Don Pillsbury Memorial Scholarship | Pursuing a degree in music Demonstrated talent, ability, and motivation | No application required, selection made by UMA representatives”
### `4a693a2097dae5e2` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Dedicated and successful business student in a Bachelor degree Demonstrates a high level of interest in small business GPA of 3.0 or higher ⟵ “SCORE Scholarship | Dedicated and successful business student in a Bachelor degree Demonstrates a high level of interest in small business GPA of 3.0 or higher | No application required, selection made by UMA representatives”
### `5217ef261ef8b822` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Non-traditional student Demonstrated leadership Academic excellence Demonstrated financial need* ⟵ “Augusta Kiwanis Club Scholarship | Non-traditional student Demonstrated leadership Academic excellence Demonstrated financial need* | General Scholarship Application”
### `816bde9fa1246551` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Current Student residing in Augusta area Leadership & service to UMA and wider community Demonstrated financial need* ⟵ “Leadership and Service Scholarship | Current Student residing in Augusta area Leadership & service to UMA and wider community Demonstrated financial need* | General Scholarship Application”
### `8a38e8412fe60526` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Current Student Good academic standing Demonstrate Financial Need ⟵ “Bennett D. Katz Scholarship | Current Student Good academic standing Demonstrate Financial Need | General Scholarship Application”
### `904237b6d5272583` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Participation in the Honors Program ⟵ “President’s Scholarships – Honors Program | Participation in the Honors Program | No application required, selection made by UMA representatives”
### `a5e1f4aadaf18ef9` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Bachelor of Arts in English AND/OR Bachelor of Arts in Interdisciplinary Studies ⟵ “Francis T. and Catherine B. Finnegan Scholarship | Bachelor of Arts in English AND/OR Bachelor of Arts in Interdisciplinary Studies | No application required, selection made by UMA representatives”
### `acdcfa4c3f62cc7f` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Currently enrolled student Single, female Maine Resident Alternates years between Augusta and Bangor campuses Demonstrated financial need* ⟵ “Business & Professional Women’s Club/Maine Futurama Foundation Scholarship | Currently enrolled student Single, female Maine Resident Alternates years between Augusta and Bangor campuses Demonstrated financial need* | General Scholarship Application”
### `addab0711b3a9214` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Serve as President of SGA at UMA, UMA Bangor, LAC, or in the Distance Education division ⟵ “President’s Scholarships – Student Government | Serve as President of SGA at UMA, UMA Bangor, LAC, or in the Distance Education division | No application required, selection made by UMA representatives”
### `b078eaad36efa9ad` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Pursuing an education in art or music Demonstrated talent, ability, and motivation ⟵ “Charles Dana Danforth Scholarship | Pursuing an education in art or music Demonstrated talent, ability, and motivation | Automatically awarded to students who meet criteria”
### `b1b7a6aeb2908514` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Current student Majoring in biology or a related field ⟵ “Celeste Cote Scholarship | Current student Majoring in biology or a related field | Students should contact an MLT faculty member for nomination for the scholarship.”
### `b4cf07c446324c7a` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Must have completed 6 credit hours Cumulative GPA of a minimum of 2.0 Eligible for the Cornerstone Program Demonstrated Financial Aid * ⟵ “Blanche Garrity Perseverance Scholarship | Must have completed 6 credit hours Cumulative GPA of a minimum of 2.0 Eligible for the Cornerstone Program Demonstrated Financial Aid * | For application and deadline contact the Cornerstone Program at UMA Bangor”
### `bb51a552f5acfe0c` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Continuing student Successful completion of at least 1 year in the Business Administration program Service to UMA ⟵ “Richard James Goggin Scholarship | Continuing student Successful completion of at least 1 year in the Business Administration program Service to UMA | General Scholarship Application”
### `bb9b4b361424f281` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Good academic standing, GPA of 2.0 or higher, demonstrated financial need.* Preference given to children, grandchildren or siblings of BIW employees. ⟵ “Bath Iron Works (BIW) Scholarship | Good academic standing, GPA of 2.0 or higher, demonstrated financial need.* Preference given to children, grandchildren or siblings of BIW employees. | Application requests can be made to UMAFA@maine.edu. Complete and submit to the personnel office at BIW for cert”
### `be67131b5a0f1fe3` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Participation in the Emerging Leaders Program ⟵ “President’s Scholarships – Emerging Leader | Participation in the Emerging Leaders Program | No application required, selection made by UMA representatives”
### `c9646b18dae8784a` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Student majoring in Dental Assisting or Dental Hygiene Enrolled full-time Satisfactory Academic Progress Demonstrated financial need* ⟵ “Dental Scholarship | Student majoring in Dental Assisting or Dental Hygiene Enrolled full-time Satisfactory Academic Progress Demonstrated financial need* | Automatically awarded to students who meet criteria”
### `c9f628ccf64b6a5a` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Current Augusta-based student Completed 2 consecutive semesters Demonstrated campus leadership Minimum cumulative GPA of 3.0 ⟵ “Student Government Association – Augusta Based | Current Augusta-based student Completed 2 consecutive semesters Demonstrated campus leadership Minimum cumulative GPA of 3.0 | General Scholarship Application”
### `d46e381d141098ef` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Graduate of a Maine high school Good academic standing Enrolled full-time (12+ credit hours) Augusta or Lewiston-Auburn campus student Majoring in a Business related program such as Accounting, Business Management or Economics Demonstrated financial need* ⟵ “The Maine Higher Education Assistance Foundation Scholarship | Graduate of a Maine high school Good academic standing Enrolled full-time (12+ credit hours) Augusta or Lewiston-Auburn campus student Majoring in a Business related program such as Accounting, Business Management or Economics Demonstrat”
### `d84b0dad5cc79603` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Demonstrated leadership service to UMA and/ or community Completed a minimum of 30 credit hours Minimum GPA of 2.75 ⟵ “Dr. Maya Angelou Leadership & Service Award | Demonstrated leadership service to UMA and/ or community Completed a minimum of 30 credit hours Minimum GPA of 2.75 | General Scholarship Application”
### `da452b0346d9234f` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Awarded to 2 new or continuing UMA students outside of the SGA that embody the commitment to making their community stronger through engagement and leadership. Recipients will be decided by a committee formed by the SGA. ⟵ “SGA Augusta Campus & Community Leaders Scholarship | Awarded to 2 new or continuing UMA students outside of the SGA that embody the commitment to making their community stronger through engagement and leadership. Recipients will be decided by a committee formed by the SGA. | Submit an essay with a m”
### `e65c1c982cb65411` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Strong academic standing Resides in Kennebec Valley area Preference given to part-time students ⟵ “Lloyd J. Jewett Scholarship | Strong academic standing Resides in Kennebec Valley area Preference given to part-time students | General Scholarship Application”
### `eca6d41a3b70ace9` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Currently enrolled student Good academic standing Demonstrated financial need* ⟵ “John Blodgett Scholarship | Currently enrolled student Good academic standing Demonstrated financial need* | General Scholarship Application”
### `ee35f74f9a548448` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Single parents Student’s income falls within eligibility guidelines for AFDC (TANF) plus 20 percent Demonstrated financial need* ⟵ “Martin & Molly Schwartz Scholarship | Single parents Student’s income falls within eligibility guidelines for AFDC (TANF) plus 20 percent Demonstrated financial need* | General Scholarship Application”
### `f0524e259fbd1a0f` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Awarded to a worthy student ⟵ “General Edmund W. Hill Scholarship | Awarded to a worthy student | General Scholarship Application”
### `f43e3128c79e986a` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Enrolled in Jazz program Preference given to high school graduates or residents from Knox, Lincoln, or Waldo county Demonstrated financial need* ⟵ “Dick Cash Scholarship | Enrolled in Jazz program Preference given to high school graduates or residents from Knox, Lincoln, or Waldo county Demonstrated financial need* | Contact the music department”
### `f8a51e82689cadb6` University of Maine at Augusta — awards 2022-23 [new] (labeled_in_source)
- source: https://www.uma.edu/financial/scholarships/ (sha256 e4be1b506c9e)
- issues: stale_year_label:2022-23
- checks: {"thresholds": null}
  - eligibility_summary: Awarded to students from Augusta, Manchester, or Winthrop ⟵ “Lila and Vernon Segal Fund | Awarded to students from Augusta, Manchester, or Winthrop | General Scholarship Application”
### `3ebf642ccdcb8fce` University of Maine at Fort Kent — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.umfk.edu/admissions/financialaid/scholarships-grants/ (sha256 43729d2d501e)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $2,500.00 ⟵ “Bengal Gold (Freshman) | In-State & Canada | High School GPA 3.0 | $2,500.00”
  - eligibility_summary: High School GPA 3.0 ⟵ “Bengal Gold (Freshman) | In-State & Canada | High School GPA 3.0 | $2,500.00”
### `4bbbf5ada5c8501a` University of Maine at Fort Kent — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.umfk.edu/admissions/financialaid/scholarships-grants/ (sha256 43729d2d501e)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,500.00 ⟵ “Bengal Silver (Freshman) | In-State & Canada | High School GPA 2.8 or higher | $1,500.00”
  - eligibility_summary: High School GPA 2.8 or higher ⟵ “Bengal Silver (Freshman) | In-State & Canada | High School GPA 2.8 or higher | $1,500.00”
### `665cf7c59ebc4802` University of Maine at Fort Kent — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.umfk.edu/admissions/financialaid/scholarships-grants/ (sha256 43729d2d501e)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - award_amount_text: $1,500.00 ⟵ “Bengal Transfer | In-State & Canada | Cumulative GPA of 2.8 | $1,500.00”
  - eligibility_summary: Cumulative GPA of 2.8 ⟵ “Bengal Transfer | In-State & Canada | Cumulative GPA of 2.8 | $1,500.00”
### `15855958eb01a0d9` University of Maine at Fort Kent — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.umfk.edu/offices/business/tuition-and-fees/ (sha256 066710402943)
- issues: implausible_amount, residency_unknown, conflicting_sources:https://www.umfk.edu/admissions/financialaid/cost-of-attendance/
- checks: {"columns": 1, "rows": 6}
  - column:In-State Tuition Rate: 279 ⟵ “In-State Tuition Rate | Per Credit Hour | $279”
  - column:Canadian Tuition Rate: 279 ⟵ “Canadian Tuition Rate | Per Credit Hour | $279”
  - column:Out-of-State & International Tuition Rate: 474 ⟵ “Out-of-State & International Tuition Rate | Per Credit Hour | $474”
  - column:RN to BSN Online Tuition Rate: 342 ⟵ “RN to BSN Online Tuition Rate | Per Credit Hour | $342”
  - column:Graduate Program Tuition Rate: 500 ⟵ “Graduate Program Tuition Rate | Per Credit Hour | $500”
  - column:YourPace Program Tuition Rate: 1800 ⟵ “YourPace Program Tuition Rate | Per 8-Week Session | $1,800”
### `a699c9789ae4a09d` University of Maine at Fort Kent — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.umfk.edu/admissions/financialaid/cost-of-attendance/ (sha256 2838e50b16d1)
- issues: ambiguous_year_labels, arrangement_unlabeled, residency_unknown, stacked_header_unparsed, conflicting_sources:https://www.umfk.edu/offices/business/tuition-and-fees/
- checks: {"columns": 7, "rows": 7}
  - column:Tuition & Fees: 10110 ⟵ “Tuition & Fees | $10,110 | $10,110 | $10,110 | $15,960 | $15,960 | $15,960 | $10,260”
  - column:Food & Housing: 3500 ⟵ “Food & Housing | $3,500 | $10,360 | $12,972 | $3,500 | $10,360 | $12,972 | $11,076”
  - column:Books, Course Materials, & Supplies*: 1000 ⟵ “Books, Course Materials, & Supplies* | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Travel*: 2100 ⟵ “Travel* | $2,100 | $2,100 | $2,100 | $2,100 | $2,100 | $2,100 | $2,100”
  - column:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70 | $70 | $70 | $70 | $70”
  - column:Misc./Medical/Dental/Personal*: 1000 ⟵ “Misc./Medical/Dental/Personal* | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Cost of Attendance (per year): 17780 ⟵ “Cost of Attendance (per year) | $17,780 | $24,640 | $27,252 | $23,630 | $30,490 | $33,102 | $25,506”
  - column:Tuition & Fees: 10110 ⟵ “Tuition & Fees | $10,110 | $10,110 | $10,110 | $15,960 | $15,960 | $15,960 | $10,260”
  - column:Food & Housing: 10360 ⟵ “Food & Housing | $3,500 | $10,360 | $12,972 | $3,500 | $10,360 | $12,972 | $11,076”
  - column:Books, Course Materials, & Supplies*: 1000 ⟵ “Books, Course Materials, & Supplies* | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Travel*: 2100 ⟵ “Travel* | $2,100 | $2,100 | $2,100 | $2,100 | $2,100 | $2,100 | $2,100”
  - column:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70 | $70 | $70 | $70 | $70”
  - column:Misc./Medical/Dental/Personal*: 1000 ⟵ “Misc./Medical/Dental/Personal* | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Cost of Attendance (per year): 24640 ⟵ “Cost of Attendance (per year) | $17,780 | $24,640 | $27,252 | $23,630 | $30,490 | $33,102 | $25,506”
  - column:Tuition & Fees: 10110 ⟵ “Tuition & Fees | $10,110 | $10,110 | $10,110 | $15,960 | $15,960 | $15,960 | $10,260”
  - column:Food & Housing: 12972 ⟵ “Food & Housing | $3,500 | $10,360 | $12,972 | $3,500 | $10,360 | $12,972 | $11,076”
  - column:Books, Course Materials, & Supplies*: 1000 ⟵ “Books, Course Materials, & Supplies* | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Travel*: 2100 ⟵ “Travel* | $2,100 | $2,100 | $2,100 | $2,100 | $2,100 | $2,100 | $2,100”
  - column:Loan Fees: 70 ⟵ “Loan Fees | $70 | $70 | $70 | $70 | $70 | $70 | $70”
  - column:Misc./Medical/Dental/Personal*: 1000 ⟵ “Misc./Medical/Dental/Personal* | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Cost of Attendance (per year): 27252 ⟵ “Cost of Attendance (per year) | $17,780 | $24,640 | $27,252 | $23,630 | $30,490 | $33,102 | $25,506”
  - column:Tuition & Fees: 15960 ⟵ “Tuition & Fees | $10,110 | $10,110 | $10,110 | $15,960 | $15,960 | $15,960 | $10,260”
  - column:Food & Housing: 3500 ⟵ “Food & Housing | $3,500 | $10,360 | $12,972 | $3,500 | $10,360 | $12,972 | $11,076”
  - column:Books, Course Materials, & Supplies*: 1000 ⟵ “Books, Course Materials, & Supplies* | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Travel*: 2100 ⟵ “Travel* | $2,100 | $2,100 | $2,100 | $2,100 | $2,100 | $2,100 | $2,100”
  - … 24 more rows
### `18543ebc8c936c38` University of Maine at Presque Isle — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.umpi.edu/student-financial-services/student-accounts/tuition-a-fees/ (sha256 3f4b6fa7ce06)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 13710 ⟵ “Tuition | $8,040 | $13,710”
  - column:Mandatory Fees: 1668 ⟵ “Mandatory Fees | $1,668 | $1,668”
  - column:Housing and Food: 11125 ⟵ “Housing and Food | $11,125 | $11,125”
  - column:Annual Estimated Direct Costs: 26503 ⟵ “Annual Estimated Direct Costs | $20,833 | $26,503”
### `6542e114ae15d792` University of Maine at Presque Isle — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.umpi.edu/student-financial-services/student-accounts/tuition-a-fees/ (sha256 3f4b6fa7ce06)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 8040 ⟵ “Tuition | $8,040 | $13,710”
  - column:Mandatory Fees: 1668 ⟵ “Mandatory Fees | $1,668 | $1,668”
  - column:Housing and Food: 11125 ⟵ “Housing and Food | $11,125 | $11,125”
  - column:Annual Estimated Direct Costs: 20833 ⟵ “Annual Estimated Direct Costs | $20,833 | $26,503”
### `20d20481baf30860` University of New England — credit_policies 2024-25 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://www.une.edu/catalog/2024-2025/undergraduate-catalog/admissions (sha256 12067782440e)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 29, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | Explorations (1) | 3”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | Clear with Department | Varies”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Explorations (2) | 6”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | PSC 101 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 200 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting of Literature | 50 | ENG 199 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “PreCalculus | 50 | MAT 180 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 199 | 3”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “General Chemistry | 50 | CHE 110 | 4”
  - equivalencies[CLEP-CHEMISTRY|65]:  ⟵ “General Chemistry | 65 | CHE 110 and CHE 111 | 8”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introduction | 50 | PSY 105 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | PSY 250 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BUMG 200 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law, Introduction | 50 | BUMG 326 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | BUMK 200 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Introduction | 50 | BUEC 203 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Introduction | 50 | BUEC 204 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC 150 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French: Two (2) Semesters | 50 | FRE 100 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French: Four (4) Semesters | 50 | FRE 100 and 101 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German: Two (2) Semesters | 50 | Exploration (1) | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German: Four (4) Semesters | 50 | Explorations (2) | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish: Two (2) Semesters | 50 | SPA 101 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish: Four (4) Semesters | 50 | SPA 101 and 102 | 6”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MAT 190 | 4”
  - … 9 more rows
### `2bb3fc29b2eb0053` University of New England — credit_policies 2024-25 · policy_kind=IB [new] (labeled_in_source)
- source: https://www.une.edu/catalog/2024-2025/undergraduate-catalog/admissions (sha256 12067782440e)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 16, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[IB-FRENCH|HL 5]:  ⟵ “Language B: French | HL | 5 | FRE 101 Basic French | 3”
  - equivalencies[IB-SPANISH|HL 5]:  ⟵ “Language B: Spanish | HL | 5 | SPA 101 Basic Spanish | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT|HL 5]:  ⟵ “Business and Management | HL | 5 | BUMG 200 Management or Business Elective | 3”
  - equivalencies[IB-ECONOMICS|HL 5]:  ⟵ “Economics | HL | 5 | BUEC 204 Microeconomics or Business Elective | 3”
  - equivalencies[IB-HISTORY|HL 5]:  ⟵ “History | HL | 5 | HIS 199 Explorations | 3”
  - equivalencies[IB-PHILOSOPHY|HL 5]:  ⟵ “Philosophy | HL | 5 | PHI 110 Problems of Knowledge | 3”
  - equivalencies[IB-PSYCHOLOGY|HL 5]:  ⟵ “Psychology | HL | 5 | PSY 105 Intro to Psychology | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|HL 5]:  ⟵ “Social and Cultural Anthropology | HL | 5 | ANT 102 Cultural Anthropology | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|SL 5]:  ⟵ “Environmental Systems and Societies | SL | 5 | ENV 104 Intro to Environmental Issues or ENV 100 and 101 GLC: Intro to Environmental Issues | 3”
  - equivalencies[IB-GLOBAL-POLITICS|HL 5]:  ⟵ “Global Politics | HL | 5 | PSC 100-level Political Science Explorations | 3”
  - equivalencies[IB-BIOLOGY|HL 5]:  ⟵ “Biology | HL | 5 | BIO 104 General Biology or BIO 105 Biology I and 106 Biology II | 4 or 8”
  - equivalencies[IB-CHEMISTRY|HL 5 or 6]:  ⟵ “Chemistry | HL | 5 or 6 | CHE 110 General Chemistry I | 4”
  - equivalencies[IB-CHEMISTRY|HL 7]:  ⟵ “Chemistry | HL | 7 | CHE 110 General Chemistry I and CHE 111 General Chemistry II | 8”
  - equivalencies[IB-PHYSICS|HL 5 or 6]:  ⟵ “Physics | HL | 5 or 6 | PHY 110 Physics I | 4”
  - equivalencies[IB-PHYSICS|HL 7]:  ⟵ “Physics | HL | 7 | PHY 110 Physics I and PHY 111 Physics II | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|HL 5]:  ⟵ “Design Technology | HL | 5 | Business Elective | 3”
  - equivalencies[IB-MUSIC|HL 5]:  ⟵ “Music | HL | 5 | MUS 101 Intro to Music or MUS 115 Music Appreciation | 3”
  - equivalencies[IB-VISUAL-ARTS|HL 5]:  ⟵ “Visual Arts | HL | 5 | ART 106 Two-Dimensional Design | 3”
  - equivalencies[IB-FILM|HL 5]:  ⟵ “Film | HL | 5 | ART 199 Topics in Art | 3”
### `7006f3a5e8fa8703` University of New England — credit_policies 2024-25 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.une.edu/catalog/2024-2025/undergraduate-catalog/admissions (sha256 12067782440e)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 31, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARH 210 or ARH 211 | 3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | BIO 104 | 4”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 | MAT 190 | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MAT 190 | 4”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | MAT 190 and MAT 195 | 8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHE 110 | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHE 110 and CHE 111 | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | ENG 199 - Exploration | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | MAT 225 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language and Composition | 4 | ENG 110 | 4”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature and Composition | 4 | ENG 199 - Exploration | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENV 104 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | HIS 231 - Exploration | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | FRE 100 - Exploration | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language | 5 | FRE 101 and FRE 199 | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | ENG 199 - Exploration | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography | 4 | ENV 200 | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture | 3 | ENG 199 - Exploration | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Vergil | 3 | ENG 198 - Exploration | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | BUEC 203 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | BUEC 204 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | MUS 101 | 3”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1 | 3 | PHY 110 | 4”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2 | 3 | PHY 111 | 4”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1 and 2 | 3 | PHY 110 and PHY 111 | 8”
  - … 13 more rows
### `0c16b08fcb5e327b` University of Southern Maine — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://usm.maine.edu/credit-prior-learning/clep-course-equivalencies-at-usm/ (sha256 8873384d02f5)
- issues: rows_without_score
- checks: {"distinct_exams": 34, "equivalencies": 34, "rows_without_score": 34}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|None]:  ⟵ “Financial Accounting | ACC 210 (3 cr)”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|None]:  ⟵ “Information Systems | GEL 1XX (3 cr)”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “Introduction to Business Law | BUS 2XX (3 cr)”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|None]:  ⟵ “Principles of Management | BUS 1XX (3 cr)”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|None]:  ⟵ “Principles of Marketing | BUS 260 (3 cr)”
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “American Literature | COR 1XX CI (3 cr)”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|None]:  ⟵ “Analyzing and Interpreting Literature | ENG 1XX CI (3 cr)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | ENG 100 WRI 1 (3 cr)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|None]:  ⟵ “College Composition Modular | GEL 1XX (3 cr)”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature | COR 1XX CI (6 cr)”
  - equivalencies[CLEP-HUMANITIES|None]:  ⟵ “Humanities | COR 1XX SCA (3 cr)”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “American Government | POS 101 SCA (3 cr)”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|None]:  ⟵ “History of the United States I | **HTY 131 SCA & CPE (3 cr)”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|None]:  ⟵ “History of the United States II | **HTY 132 SCA (3 cr)”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|None]:  ⟵ “Human Growth and Development | HRD 200 (3 cr)”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|None]:  ⟵ “Introduction to Educational Psychology | HRD 3XX (3 cr)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introductory Psychology | PSY 100 (3 cr)”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Introductory Sociology | SOC 100 SCA (3 cr)”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “Principles of Macroeconomics | ECO 101 SCA & QR (3 cr)”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | ECO 102 SCA & QR (3 cr)”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|None]:  ⟵ “Social Sciences and History | COR 1XX SCA (3 cr)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|None]:  ⟵ “Western Civilization I to 1684 | **HTY 101 SCA & INTL (3 cr)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|None]:  ⟵ “Western Civilization II 1648 to Present | **HTY 102 SCA & INTL (3 cr)”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “Biology | GEL 1XX (6 cr)”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | MAT 152 QR (4 cr)”
  - … 9 more rows
### `23161d06d205e807` University of Southern Maine — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://usm.maine.edu/credit-prior-learning/advanced-placement-ap-course-equivalencies-at-usm/ (sha256 2d1871544e6c)
- issues: rows_without_score
- checks: {"distinct_exams": 40, "equivalencies": 40, "rows_without_score": 40}
  - equivalencies[AP-2-D-ART-DESIGN|None]:  ⟵ “2-D Art and Design | ART 141 CE (3 cr)”
  - equivalencies[AP-3-D-ART-DESIGN|None]:  ⟵ “3-D Art and Design | ART 142 CE (3 cr)”
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “Art History | ARH 1XX CI & INTL (3 cr)”
  - equivalencies[AP-DRAWING|None]:  ⟵ “Drawing | ART 151 CE (3 cr)”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “Music Theory | MUS 110 CE (3 cr) with score of 3 on EITHER written or aural component MUT 110 (3 cr) and MUT 112 (3 cr) with score of 4 or higher on written component MUT 111 (1 cr) and MUT 113 (1 cr) with score of 4 or higher on aural component”
  - equivalencies[AP-SEMINAR|None]:  ⟵ “AP Seminar | COR 1XX EL (3 cr)”
  - equivalencies[AP-RESEARCH|None]:  ⟵ “AP Research | GEL 2XX (3 cr) or **COR 2XX WRI II (3 cr)”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|None]:  ⟵ “Business w/Personal Finance | BUS 1XX (3 cr)”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language and Composition | ENG 100 WRI 1 (3 cr)”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “English Literature and Composition | ENG 100 WRI 1 (3 cr) and ENG 1XX CI (3 cr) with score of 3ENG 100 WRI 1 (3 cr) and ENG 140 CI (3 cr) with score of 4 or higher”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “African American Studies | COR 1XX CPE (3 cr)”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|None]:  ⟵ “Comparative Government and Politics | POS 1XX SCA & INTL (3 cr)”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “European History | HTY 102 SCA & INTL (3 cr)”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Human Geography | GEO 101 SCA & INTL (3 cr)”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Macroeconomics | ECO 101 SCA & QR (3 cr)”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Microeconomics | ECO 102 SCA & QR (3 cr)”
  - equivalencies[AP-PSYCHOLOGY|None]:  ⟵ “Psychology | PSY 100 (3 cr)”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|None]:  ⟵ “United States Government and Politics | POS 101 SCA (3 cr)”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “United States History | HTY 131 SCA & CPE (3 cr) and HTY 132 SCA (3 cr)”
  - equivalencies[AP-WORLD-HISTORY-MODERN|None]:  ⟵ “World History: Modern | HTY 1XX SCA & INTL (3 cr)”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB | MAT 152 QR (4 cr)”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Calculus BC | MAT 152 QR (4 cr) and MAT 153 (4 cr)(MABS subscore 3 or higher = MAT 152 QR with score less than 3 on calculus BC exam)”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “Computer Science Principles | COS 1XX (3 cr)”
  - equivalencies[AP-PRECALCULUS|None]:  ⟵ “Pre-Calculus | MAT 140 (3 cr)”
  - equivalencies[AP-STATISTICS|None]:  ⟵ “Statistics | MAT 120 QR (4 cr) or PSY 201 (3 cr)”
  - … 15 more rows
### `df8107c397583a64` University of Southern Maine — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://usm.maine.edu/credit-prior-learning/international-baccalaureate-ib-course-equivalencies-at-usm/ (sha256 f457dcf6f9ee)
- issues: rows_without_score
- checks: {"distinct_exams": 17, "equivalencies": 27, "rows_without_score": 27}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | COR 1XX EL (3 cr)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business Management | BUS 260 (3 cr) and ACC 210 (3 cr)”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | CHY 1XX (3 cr)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|None]:  ⟵ “English A : Language and Literature | ENG 1XX CI (3 cr)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|None]:  ⟵ “English A: Literature | ENG 1XX CI (3 cr)”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|None]:  ⟵ “Environmental Systems and Societies | ESP 101 (3 cr)”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | GEO 103 SCA & INTL (3 cr)”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History | COR 1XX INTL (3 cr)”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|None]:  ⟵ “MathematicsAnalysis & ApproachesApplication & Interpretation | MAT 1XX QR (4 cr)MAT 1XX QR (4 cr)”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | MUH 105 CI & CPE (3 cr)”
  - equivalencies[IB-PHILOSOPHY|None]:  ⟵ “Philosophy | PHI 2XX CI (3 cr)”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Physics | COR 1XX EL (3 cr)”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | PSY 100 (3 cr)”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|None]:  ⟵ “Social and Cultural Anthropology | COR 1XX SCA (3 cr)”
  - equivalencies[IB-VISUAL-ARTS|None]:  ⟵ “Visual Arts | ART 1XX CE (3 cr)”
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | BIO 105 (3 cr), BIO 106 (1.5 cr), BIO 107 (3 cr), and BIO 108 SE (1.5 cr)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business Management | BUS 260 (3 cr), ACC 210 (3 cr), BUS 200 (3 cr)”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | CHY 1XX (3 cr) with score of 4 or 5CHY 113 SE (3 cr) and CHY 114 SE (1.5 cr) with score of 6CHY 113 SE (3 cr), CHY 114 SE (1.5 cr) and CHY 115 (3 cr) with score of 7”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | ECO 101 SCA (3 cr) and ECO 102 SCA (3 cr)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|None]:  ⟵ “English A: Language and Literature | ENG 140 CI (3 cr)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|None]:  ⟵ “English A: Literature | ENG 140 CI (3 cr)”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | GEO 103 SCA & INTL (3 cr) and GEO 105 INTL (3 cr)”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History (all subjects) | HTY 1XX SCA & INTL (3 cr)”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | MUH 105 CI & CPE (3 cr) and MUS 110 CE (3 cr)”
  - equivalencies[IB-PHILOSOPHY|None]:  ⟵ “Philosophy | PHI 2XX CI (3 cr) and PHI 3XX (3 cr)”
  - … 2 more rows
### `1e8521b8e6d5c85b` Washington County Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://wccc.me.edu/wp-content/uploads/RE-Form-SAP-Appeal-1.pdf (sha256 74294d8bea7d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Filing deadlines: one month before the fall semester or one week before the spring semester.”
  - sentence: sap_appeal ⟵ “RE – Form SAP Appeal Revised: Sept 19, 2019; amd”
### `24e0545572890da8` York County Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.yccc.edu/admissions-aid/paying-for-college/tuition-fees/ (sha256 6c6f36c76bde)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 2}
  - column:Tuition*: 4320 ⟵ “Tuition* | $2,880 | $4,320 | $5,760”
  - column:Books and Supplies: 1200 ⟵ “Books and Supplies | $1,200 | $1,200 | $1,200”
### `73acd4f0ad4f72b6` York County Community College — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.yccc.edu/admissions-aid/apply-to-yccc/transfer-to-yccc/ (sha256 d9c399f98b2f)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Typically, credits from an accredited college or university with a grade of “C” or higher and fit the YCCC degree program will transfer in.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 23; pages by category: admissions_tests 1, cost_of_attendance 2, dual_enrollment 1, merit_scholarships 20, residency 1, transfer_credit 1, tuition_fees 23

## Blocked by the site (every request refused; needs the browser fallback)

- Maine College of Health Professions (`ipeds-161022`)
- Colby College (`ipeds-161086`)
- University of Maine at Farmington (`ipeds-161226`)

## Leads: official pages found with no extracted record

- Bates College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Bowdoin College: cost_of_attendance, merit_scholarships, dual_enrollment, transfer_credit
- Central Maine Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- College of the Atlantic: cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- Eastern Maine Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, statewide_articulation, degree_requirements
- Husson University: tuition_fees, admissions_tests, dual_enrollment, transfer_credit
- Kennebec Valley Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Maine College of Art & Design: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- Maine Maritime Academy: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- Northern Maine Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit
- Saint Joseph's College of Maine: admissions_tests, ap_credit, clep_credit, statewide_articulation, degree_requirements
- Southern Maine Community College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Thomas College: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Unity Environmental University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, degree_requirements
- University of Maine: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- University of Maine at Augusta: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- University of Maine at Fort Kent: cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- University of Maine at Presque Isle: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, residency, degree_requirements
- University of New England: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency, degree_requirements, aid_appeals
- University of Southern Maine: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Washington County Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, statewide_articulation, degree_requirements
- York County Community College: cost_of_attendance, merit_scholarships, ap_credit, clep_credit, residency
