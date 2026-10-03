# Review queue — MS (2026-27)

Pages fetched: 2124; failures: 371. Candidates: 176 (79 without issues, 97 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 4 | 10 | 16 | 0 | 2 |
| cost_of_attendance | 0 | 0 | 4 | 4 | 20 | 2 | 2 |
| admissions_tests | 0 | 0 | 0 | 0 | 29 | 1 | 2 |
| common_data_set | 0 | 0 | 0 | 0 | 5 | 25 | 2 |
| merit_scholarships | 0 | 0 | 6 | 0 | 23 | 1 | 2 |
| ap_credit | 0 | 0 | 2 | 2 | 6 | 20 | 2 |
| clep_credit | 0 | 0 | 1 | 1 | 7 | 21 | 2 |
| ib_credit | 0 | 0 | 1 | 0 | 4 | 25 | 2 |
| dual_enrollment | 0 | 0 | 11 | 2 | 11 | 6 | 2 |
| transfer_credit | 0 | 0 | 1 | 0 | 25 | 4 | 2 |
| statewide_articulation | 0 | 0 | 0 | 0 | 3 | 27 | 2 |
| residency | 0 | 0 | 0 | 0 | 20 | 10 | 2 |
| degree_requirements | 0 | 0 | 0 | 0 | 21 | 9 | 2 |
| aid_appeals | 0 | 0 | 0 | 18 | 6 | 6 | 2 |

## Ready for review (79)

### `50ce27fd0fe5bd55` Alcorn State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.alcorn.edu/financial-aid/cost-of-attendance-coa-budget/ (sha256 17c00cff15e2)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - off_campus_not_with_family:Books: 1200.0 ⟵ “Books | $1,200.00 | $1,200.00”
  - off_campus_not_with_family:Fees: 730.0 ⟵ “Fees | $730.00 | $730.00”
  - off_campus_not_with_family:Food: 4693.0 ⟵ “Food | $4,693.00 | $4,693.00”
  - off_campus_not_with_family:Housing: 7581.0 ⟵ “Housing | $7581.00 | $7581.00”
  - off_campus_not_with_family:Personal Expenses: 1606.0 ⟵ “Personal Expenses | $1,606.00 | $1,606.00”
  - off_campus_not_with_family:Transportation: 1710.0 ⟵ “Transportation | $1,710.00 | $1,710.00”
  - off_campus_not_with_family:Tuition: 9105.0 ⟵ “Tuition | $8,105.00 | $9,105.00”
  - off_campus_not_with_family:Total Cost of Attendance: 26625.0 ⟵ “Total Cost of Attendance | $25,625.00 | $26,625.00”
### `d7012f70b6dbd938` Alcorn State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.alcorn.edu/financial-aid/cost-of-attendance-coa-budget/ (sha256 17c00cff15e2)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - off_campus_not_with_family:Books: 1200.0 ⟵ “Books | $1,200.00 | $1,200.00”
  - off_campus_not_with_family:Fees: 730.0 ⟵ “Fees | $730.00 | $730.00”
  - off_campus_not_with_family:Food: 4693.0 ⟵ “Food | $4,693.00 | $4,693.00”
  - off_campus_not_with_family:Housing: 7581.0 ⟵ “Housing | $7581.00 | $7581.00”
  - off_campus_not_with_family:Personal Expenses: 1606.0 ⟵ “Personal Expenses | $1,606.00 | $1,606.00”
  - off_campus_not_with_family:Transportation: 1710.0 ⟵ “Transportation | $1,710.00 | $1,710.00”
  - off_campus_not_with_family:Tuition: 8105.0 ⟵ “Tuition | $8,105.00 | $9,105.00”
  - off_campus_not_with_family:Total Cost of Attendance: 25625.0 ⟵ “Total Cost of Attendance | $25,625.00 | $26,625.00”
### `5de4cca16d7f3434` Copiah-Lincoln Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.colin.edu/program/dual-enrollment/ (sha256 edd9ebfe5853)
- checks: {"fields": ["state_grant_accepted"], "tiers": 0}
  - state_grant_accepted: True ⟵ “The 2023 Mississippi Legislature approved Senate Bill 2487 cited as the Mississippi Dual Enrollment/Dual Credit Scholarship Program Act of 2023. The scholarship program awards eligible public or charter school high school juniors or seniors six hours of dual enrollment/credit funding.”
### `90f80127eca4ab3d` Hinds Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hindscc.edu/admissions/costs-aid/scholarships/act-scholarships (sha256 877e7cf598cc)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ($1,000 per semester) ⟵ “ACT Faculty Scholarship | 20—23 | $4,000 ($1,000 per semester)”
  - test_requirement: ACT 20—23 ⟵ “ACT Faculty Scholarship | 20—23 | $4,000 ($1,000 per semester)”
### `c24a3377b57a7250` Hinds Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hindscc.edu/admissions/costs-aid/scholarships/act-scholarships (sha256 877e7cf598cc)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ($1,500 per semester) ⟵ “ACT Dean’s Scholarship | 24—27 | $6,000 ($1,500 per semester)”
  - test_requirement: ACT 24—27 ⟵ “ACT Dean’s Scholarship | 24—27 | $6,000 ($1,500 per semester)”
### `eba9c8a4bece080a` Hinds Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hindscc.edu/admissions/costs-aid/scholarships/act-scholarships (sha256 877e7cf598cc)
- checks: {"thresholds": {"act_min": 28}}
  - award_amount_text: $12,000 ($3,000 per semester) ⟵ “ACT Presidential Scholarship | 28 and above | $12,000 ($3,000 per semester)”
  - test_requirement: ACT 28 and above ⟵ “ACT Presidential Scholarship | 28 and above | $12,000 ($3,000 per semester)”
### `3c17110f2f4f94d3` Hinds Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.hindscc.edu/admissions/dual-enrollment (sha256 14d1f23f2c51)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “A high school GPA of 3.0 or higher is required to take academic courses (face-to-face or online).”
  - eligibility_tier: 2.0 ⟵ “A high school GPA of 2.0 or higher, plus sophomore status or higher, is required to take career/technical classes.”
  - per_credit_hour_charge: 50 ⟵ “Students taking dual credit courses through a partnership between Hinds and their high school receive a discounted rate of tuition called the Dual Credit Participation fee, which is $50 per credit hour. Textbook fees still apply at a rate of $30/credit hour.”
  - per_credit_hour_charge: 30 ⟵ “Students taking dual credit courses through a partnership between Hinds and their high school receive a discounted rate of tuition called the Dual Credit Participation fee, which is $50 per credit hour. Textbook fees still apply at a rate of $30/credit hour.”
### `m1b8842ce7e369ec` Holmes Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://holmescc.edu/dual-enrollment-dual-credit/dual-enrollment-dual-credit-faq/ (sha256 4818d4fcf153)
- checks: {"fields": ["state_grant_accepted"], "merged_pages": 3, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “The student must have a minimum 3.0 cumulative GPA on a 4.0 scale for high school work completed. (Prerequisites and co-requisites as stipulated in the Holmes bulletin will be followed.)”
  - eligibility_tier: 2.0 ⟵ “Have a minimum overall high school GPA of 2.0 on a 4.0 scale.”
  - eligibility_tier: 3.0 ⟵ “Must have a minimum overall 3.0 GPA on a 4.0 scale.”
  - eligibility_tier: 2.0 ⟵ “Must have a minimum overall 2.0 GPA on a 4.0 scale.”
  - state_grant_accepted: False ⟵ “State Grants (including MTAG and MESG) not available.”
  - eligibility_tier: 3.0 ⟵ “The student must have a minimum 3.0 cumulative GPA on a 4.0 scale for high school work completed. (Prerequisites and co-requisites as stipulated in the Holmes bulletin will be followed.)”
  - eligibility_tier: 2.0 ⟵ “The student must have a minimum overall high school GPA of 2.0 on a 4.0 scale.”
### `2eeda2cc237d98d2` Itawamba Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.iccms.edu/Scholarships (sha256 277556c72083)
- checks: {"thresholds": null}
  - test_requirement: Academic Excellence 22-23 ACT ⟵ “Academic Excellence 22-23 ACT | $3,300 (up to $825 per semester)”
  - award_amount_text: $3,300 (up to $825 per semester) ⟵ “Academic Excellence 22-23 ACT | $3,300 (up to $825 per semester)”
### `35d8b5340664b15d` Itawamba Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.iccms.edu/Scholarships (sha256 277556c72083)
- checks: {"thresholds": null}
  - test_requirement: Dean's 24-27 ACT or National Merit Semifinalist ⟵ “Dean's 24-27 ACT or National Merit Semifinalist | $6,600 (up to $1,650 per semester)”
  - award_amount_text: $6,600 (up to $1,650 per semester) ⟵ “Dean's 24-27 ACT or National Merit Semifinalist | $6,600 (up to $1,650 per semester)”
### `d04a4ff890377ee6` Itawamba Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.iccms.edu/Scholarships (sha256 277556c72083)
- checks: {"thresholds": null}
  - test_requirement: Merit Award 18-21 ACT ⟵ “Merit Award 18-21 ACT | $2,000 (up to $500 per semester)”
  - award_amount_text: $2,000 (up to $500 per semester) ⟵ “Merit Award 18-21 ACT | $2,000 (up to $500 per semester)”
### `286755e717146ef0` Itawamba Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.iccms.edu/dualcredit (sha256 82f786a7ea2a)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a minimum overall high school GPA of 3.0 on a 4.0 scale as documented by an official high school transcript on all high school courses and”
### `35e75c8518e05a4f` Mississippi College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.mc.edu/academics/academic-resources/clep (sha256 cda6d7554542)
- checks: {"distinct_exams": 22, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 hrs. | ENG. 101”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 hrs. | ENG. 212”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 hrs. | ENG. 213”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1 | 50 | 6 hrs. | FRE. 101-102”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, Level 2 | 59 | 12 hrs. | FRE 101-102, 201-202”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1 | 50 | 6 hrs. | GER. 101-102”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “German Language, Level 2 | 63 | 12 hrs. | GER. 101-102, 201-202”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1 | 50 | 6 hrs. | SPA. 101-102”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language, Level 2 | 63 | 12 hrs. | SPA 101-102, 201-202”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 hrs. | PLS. 201****”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 hrs. | PSY. 201”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 hrs. | PSY. 314”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 hrs. | ECO. 231”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 hrs. | ECO 232”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 hrs. | SOC. 205”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | 3 hrs. | HIS. 101”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | 3 hrs. | HIS. 102”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 hrs. | MAT. 111”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 8 hrs. | BIO. 111/110-112/113”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 8 hrs. | CHE. 141-142”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | 3 hrs. | CSC 114”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 hrs. | MGT. 371”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 hrs. | ACC. 201”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 hrs. | GBU. 358”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 3 hrs. | MKT. 381”
### `59ad6f598c41a160` Mississippi College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.mc.edu/academics/academic-resources/international-baccalaureate-credit (sha256 71165ecd53d3)
- checks: {"distinct_exams": 6, "equivalencies": 6, "rows_without_score": 0}
  - equivalencies[IB-CHEMISTRY|N/A]:  ⟵ “Chemistry | N/A | None Accepted”
  - equivalencies[IB-BIOLOGY|6]:  ⟵ “Biology | 6 | Subsidiary/Standard Level: BIO: 101 (3 hrs) 103 (3 hrs) 104 (1 hr)”
  - equivalencies[IB-ECONOMICS|6]:  ⟵ “Economics | 6 | Subsidiary/Standard and Higher Levels: ECO 231-ECO 232 (6 hrs) Note: Subsidiary/Standard Level contains both micro and macro economics”
  - equivalencies[IB-FRENCH|5]:  ⟵ “Foreign Languages (French, German, Latin, Spanish) | 5 | Subsidiary/Standard Level: 101-102 (6 hrs); Higher Level: 201-202 (6 hrs)”
  - equivalencies[IB-HISTORY|5]:  ⟵ “History | 5 | Higher Level: HIS 102 (3 hrs) [Americas]”
  - equivalencies[IB-PHYSICS|5]:  ⟵ “Physics | 5 | Subsidiary/standard Level: PHY 104 (3 hrs); Higher Level: PHY 151 - PHY 152 (8 hrs)”
### `6d157825bc121ecb` Mississippi College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.mc.edu/academics/academic-resources/advanced-placement-credit (sha256 fcfb40082ebe)
- checks: {"distinct_exams": 35, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ART 407-408 History of Art I & II | 6 hrs.”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | MUS 101 Theory I and MUS 105 Aural Skills | 4 hrs.”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language and Composition (see NOTE 2) | 4 | ENG 101 English Composition | 3 hrs.”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature and Composition (see NOTE 2) | 4 | ENG 212 Survey of British Literature | 3 hrs.”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|4]:  ⟵ “Comparative Government & Politics | 4 | PLS 320 Comparative Governments | 3 hrs.”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | HIS 102 History of Western Civilization | 3 hrs.”
  - equivalencies[AP-HUMAN-GEOGRAPHY|N/A]:  ⟵ “Human Geography | N/A | Not Accepted | N/A”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | ECO 231 Principles of Macroeconomics | 3 hrs.”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | ECO 232 Principles of Microeconomics | 3 hrs.”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSY 201 Introduction to Psychology | 3 hrs.”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4]:  ⟵ “United States Government & Politics | 4 | PLS 201 American National Government | 3 hrs.”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “United States History | 4 | HIS 211-212 History of the United States | 6 hrs.”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History: Modern | 4 | HIS 103 World Civilization I | 3 hrs.”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 | MAT 121 Calculus with Analytic Geometry I | 3 hrs.”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | MAT 121-122 Calculus with Analytic Geometry I & II | 6 hrs.”
  - equivalencies[AP-COMPUTER-SCIENCE-A|N/A]:  ⟵ “Computer Science A | N/A | Not Accepted | N/A”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|N/A]:  ⟵ “Computer Science Principles | N/A | Not Accepted | N/A”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Precalculus | 4 | MAT 119 Precalculus | 3 hrs.”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | MAT 207 Elementary Statistics | 3 hrs.”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIO 111/110--112/113 Biology I & II | 8 hrs.”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHE 141-142 General Chemistry I & II | 8 hrs.”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|N/A]:  ⟵ “Environmental Science | N/A | Not Accepted | N/A”
  - equivalencies[AP-PHYSICS-1|4 (on each)]:  ⟵ “Physics 1 & 2 Algebra-Based (both are required) | 4 (on each) | PHY 151-152 General Physics I & II | 8 hrs.”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|N/A]:  ⟵ “Physics C Electricity and Magnetism | N/A | Not Accepted | N/A”
  - equivalencies[AP-PHYSICS-C-MECHANICS|N/A]:  ⟵ “Physics C Mechanics | N/A | Not Accepted | N/A”
  - … 10 more rows
### `96e6d81e89518d90` Mississippi College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mc.edu/admissions/undergraduate/transfers/faq (sha256 37dbe49b73b7)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 33 ⟵ “The last 33 semester hours must be taken at MC.”
### `m0861bf6c7398810` Mississippi Delta Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.msdelta.edu/programs/dual-enrollment/counselor-guidelines.php (sha256 d1b0227e9f6c)
- checks: {"fields": [], "merged_pages": 2, "tiers": 4}
  - eligibility_tier: 3.0 ⟵ “Academic Courses: minimum overall 3.0 GPA on a 4.0 scale on all high school courses and with successful”
  - eligibility_tier: 3.0 ⟵ “overall 3.0 GPA on all high school courses and a minimum composite ACT score of 30”
  - eligibility_tier: 2.0 ⟵ “Minimum high school GPA of 2.0 on a 4.0 scale; may be classified as a sophomore; and”
  - eligibility_tier: 3.0 ⟵ “o   Have a minimum overall high school GPA of 3.0 on a 4.0 scale; and”
  - eligibility_tier: 3.0 ⟵ “Minimum grade point average of 3.0 on a 4.0 scale”
  - eligibility_tier: 3.0 ⟵ “with a 3.0 GPA on all high school courses AND a minimum ACT score of 30 or the equivalent”
  - eligibility_tier: 2.0 ⟵ “Have a minimum high school GPA of 2.0 on a 4.0 scale”
### `38ee23f262f113ba` Mississippi Gulf Coast Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://mgccc.edu/paying-for-college/scholarships/high-school-equivalency-hse-scholarships/ (sha256 ddf08c50aa1b)
- checks: {"thresholds": null}
  - test_requirement: GED Score: College Ready. Minimum score of 165 or higher on each section ⟵ “College Ready. Minimum score of 165 or higher on each section | College & Career Ready** 64-100 | A (3.5 – 4.0) | $1,080 during one semester”
  - award_amount_text: $1,080 during one semester ⟵ “College Ready. Minimum score of 165 or higher on each section | College & Career Ready** 64-100 | A (3.5 – 4.0) | $1,080 during one semester”
### `8b83046b095ef468` Mississippi Gulf Coast Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://mgccc.edu/paying-for-college/scholarships/high-school-equivalency-hse-scholarships/ (sha256 ddf08c50aa1b)
- checks: {"thresholds": null}
  - test_requirement: GED Score: Minimum score of 145 - 164 on each section ⟵ “Minimum score of 145 - 164 on each section | 45 - 63 | B (2.5 – 3.499) or C (1.5 – 2.499) | $540 during one semester”
  - award_amount_text: $540 during one semester ⟵ “Minimum score of 145 - 164 on each section | 45 - 63 | B (2.5 – 3.499) or C (1.5 – 2.499) | $540 during one semester”
### `f02953fe1ad3b548` Mississippi Gulf Coast Community College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://mgccc.edu/paying-for-college/financial-aid/cost-of-attendance/ (sha256 a68255784638)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees*: 4300 ⟵ “Tuition & Fees* | $4,300 | $4,300 | $4,300”
  - on_campus:Food & Housing: 6258 ⟵ “Food & Housing | $6,258 | $4,240 | $7,800”
  - on_campus:Books & Supplies: 1875 ⟵ “Books & Supplies | $1,875 | $1,875 | $1,875”
  - on_campus:Transportation: 2540 ⟵ “Transportation | $2,540 | $4,500 | $4,500”
  - on_campus:Out of State Fee*: 1000 ⟵ “Out of State Fee* | $1,000 | $1,000 | $1,000”
  - on_campus:Miscellaneous: 1000 ⟵ “Miscellaneous | $1,000 | $1,000 | $1,000”
  - on_campus:TOTAL BUDGET: 16973 ⟵ “TOTAL BUDGET | $16,973 | $16,915 | $20,475”
  - with_parents_or_family:Tuition & Fees*: 4300 ⟵ “Tuition & Fees* | $4,300 | $4,300 | $4,300”
  - with_parents_or_family:Food & Housing: 4240 ⟵ “Food & Housing | $6,258 | $4,240 | $7,800”
  - with_parents_or_family:Books & Supplies: 1875 ⟵ “Books & Supplies | $1,875 | $1,875 | $1,875”
  - with_parents_or_family:Transportation: 4500 ⟵ “Transportation | $2,540 | $4,500 | $4,500”
  - with_parents_or_family:Out of State Fee*: 1000 ⟵ “Out of State Fee* | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:Miscellaneous: 1000 ⟵ “Miscellaneous | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:TOTAL BUDGET: 16915 ⟵ “TOTAL BUDGET | $16,973 | $16,915 | $20,475”
  - off_campus_not_with_family:Tuition & Fees*: 4300 ⟵ “Tuition & Fees* | $4,300 | $4,300 | $4,300”
  - off_campus_not_with_family:Food & Housing: 7800 ⟵ “Food & Housing | $6,258 | $4,240 | $7,800”
  - off_campus_not_with_family:Books & Supplies: 1875 ⟵ “Books & Supplies | $1,875 | $1,875 | $1,875”
  - off_campus_not_with_family:Transportation: 4500 ⟵ “Transportation | $2,540 | $4,500 | $4,500”
  - off_campus_not_with_family:Out of State Fee*: 1000 ⟵ “Out of State Fee* | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:Miscellaneous: 1000 ⟵ “Miscellaneous | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:TOTAL BUDGET: 20475 ⟵ “TOTAL BUDGET | $16,973 | $16,915 | $20,475”
### `92de47214dde3ed9` Mississippi University for Women — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.muw.edu/admissions/dualenrollment/requirements/ (sha256 feb541d905ed)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “Have a minimum overall high school GPA of 3.00 on a 4.0 scale”
  - eligibility_tier: 3.0 ⟵ “Have a minimum high school GPA of 3.00 GPA on a 4.00 scale”
### `11001ee386d9b606` Mississippi Valley State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mvsu.edu/sites/default/files/dual.pdf (sha256 9a760e050c96)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “•  Obtain at least a 2.5 grade point average on 4.0 scale on all high school courses, as”
### `2fa29495f117231c` Northeast Mississippi Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.nemcc.edu/admissions/apply/dual-enrollment/index.html (sha256 f953014c65cf)
- checks: {"fields": ["min_hs_gpa"], "tiers": 3}
  - eligibility_tier: 3.0 ⟵ “You must have your counselor (or guardian/custodian if homeschooled) send a high school transcript that documents that you are in junior or senior standing with a GPA of 3.0 or higher on a 4.0 scale.”
  - eligibility_tier: 3.0 ⟵ “Prospective students must submit a high school transcript that documents a junior or senior standing with a grade point average of 3.0 or higher on a 4.0 scale.”
  - eligibility_tier: 2.0 ⟵ “Those interested in enrolling in career/technical courses as dual enrollment students must have a 2.0 GPA and sophomore standing.”
### `3fac8cd34be8903c` Northeast Mississippi Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://catalog.nemcc.edu/admissions/credit-by-exam.html (sha256 61d5c572c0f8)
- checks: {"distinct_exams": 5, "equivalencies": 6, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIO 1134”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language/Comp | 3 | 3 | ENG 1113”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 3 | MAT 1513 or MAT 1613”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 6 | MAT 1523 or MAT 1623”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “U.S. History | 3 | 3 | HIS 2213”
  - equivalencies[AP-UNITED-STATES-HISTORY|4/5]:  ⟵ “U.S. History | 4/5 | 6 | HIS 2213/HIS 2223”
### `m2f186891f55693b` Northeast Mississippi Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.nemcc.edu/admissions/index.html (sha256 c011b0e6bd32)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 45 ⟵ “A maximum of 45 semester hours of transfer credit may be applied toward a degree program.”
  - max_transfer_credits: 45 ⟵ “A maximum of 45 semester hours of transfer credit may be applied toward a degree program.”
### `139acf8ee9340369` Northwest Mississippi Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.northwestms.edu/financial-aid (sha256 2663fa8c36a0)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 4980 ⟵ “Tuition and Fees | $4,980 | $7,780”
  - column:Books and Supplies: 2250 ⟵ “Books and Supplies | $2,250 | $2,250”
  - column:Housing: 4600 ⟵ “Housing | $4,600 | $6,660”
  - column:Travel: 2000 ⟵ “Travel | $2,000 | $2,650”
  - column:Misc and Personal: 1615 ⟵ “Misc and Personal | $1,615 | $2,115”
  - column:Total: 15445 ⟵ “Total | $15,445 | $21,455”
### `8d6456fb13307972` Northwest Mississippi Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.northwestms.edu/financial-aid (sha256 2663fa8c36a0)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 7780 ⟵ “Tuition and Fees | $4,980 | $7,780”
  - column:Books and Supplies: 2250 ⟵ “Books and Supplies | $2,250 | $2,250”
  - column:Housing: 6660 ⟵ “Housing | $4,600 | $6,660”
  - column:Travel: 2650 ⟵ “Travel | $2,000 | $2,650”
  - column:Misc and Personal: 2115 ⟵ “Misc and Personal | $1,615 | $2,115”
  - column:Total: 21455 ⟵ “Total | $15,445 | $21,455”
### `m8a5ea8e86f7d079` Northwest Mississippi Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.northwestms.edu/admissions/dual-enrollment-admissions (sha256 b42a8e5ca2c0)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Dual enrolled students must have completed a minimum of fourteen (14) core high school units and a minimum overall high school GPA of 3.0 or have an ACT composite score of thirty (30) or above and a minimum overall high school GPA of 3.0 or above.”
  - eligibility_tier: 3.0 ⟵ “Dual enrolled students must have completed a minimum of fourteen (14) core high school units or have an ACT composite score of thirty (30) or above and a GPA of 3.0 or above.”
### `m719044170735a59` Pearl River Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://prcc.edu/academics/dual-enrollment/middle_college/ (sha256 7505e2ed9439)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 1}
  - per_credit_hour_charge: 40 ⟵ “Payment for Dual Enrollment courses is required when submitting course roster and student paperwork by the required deadline. Submit one check/purchase order for $40 per credit hour per student, payable to PRCC.”
  - per_credit_hour_charge: 65 ⟵ “A:    All Academic Dual Enrollment classes are $65 per credit hour.  This covers the tuition, fees, and ebook.”
  - per_credit_hour_charge: 40 ⟵ “Payment for Dual Enrollment courses is required when submitting course roster and student paperwork by the required deadline. Submit one check/purchase order for $40 per credit hour per student, payable to PRCC.”
  - per_credit_hour_charge: 65 ⟵ “A:    All Academic Dual Enrollment classes are $65 per credit hour.  This covers the tuition, fees, and ebook.”
  - eligibility_tier: 3.0 ⟵ “Have a minimum overall high school GPA of 3.0 on a 4.0 scale;”
  - per_credit_hour_charge: 65 ⟵ “For the first semester, the tuition is $65 per credit hour. Students typically take 15-16 hours the first semester, which would be $975-$1040. Textbooks/eBooks are included.”
### `50a12f5640886c9c` Tougaloo College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tougaloo.edu/admissions/scholarships (sha256 628e79332b54)
- checks: {"thresholds": null}
  - test_requirement: ACT 601-977-7896 ⟵ “Music | Awarded at discretion of Music Department | 601-977-7896”
### `81f83d6f0305b3b6` Tougaloo College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tougaloo.edu/admissions/scholarships (sha256 628e79332b54)
- checks: {"thresholds": null}
  - test_requirement: ACT 601-977-7700 ⟵ “Athletics | Awarded at discretion of Athletic Department | 601-977-7700”
### `8b547614d3322125` Tougaloo College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tougaloo.edu/admissions/scholarships (sha256 628e79332b54)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - gpa_requirement: 3.5+ ⟵ “Presidential Academic Scholarship | Full Tuition + Room & Board | 3.5+ | ACT: 27+ / SAT: 1220+ | 3.5 GPA, 15+ hrs, Good Conduct, Renewal Contract”
  - test_requirement: ACT ACT: 27+ / SAT: 1220+ ⟵ “Presidential Academic Scholarship | Full Tuition + Room & Board | 3.5+ | ACT: 27+ / SAT: 1220+ | 3.5 GPA, 15+ hrs, Good Conduct, Renewal Contract”
  - renewal_requirements: 3.5 GPA, 15+ hrs, Good Conduct, Renewal Contract ⟵ “Presidential Academic Scholarship | Full Tuition + Room & Board | 3.5+ | ACT: 27+ / SAT: 1220+ | 3.5 GPA, 15+ hrs, Good Conduct, Renewal Contract”
### `a608edc037a5de1e` Tougaloo College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tougaloo.edu/admissions/scholarships (sha256 628e79332b54)
- checks: {"thresholds": {"gpa_min": 3.25}}
  - gpa_requirement: 3.25+ ⟵ “Eagle Academic Scholarship | Full Tuition | 3.25+ | Valedictorian or Salutatorian | 3.25 GPA, 15+ hrs, Good Conduct, Renewal Contract”
  - test_requirement: ACT Valedictorian or Salutatorian ⟵ “Eagle Academic Scholarship | Full Tuition | 3.25+ | Valedictorian or Salutatorian | 3.25 GPA, 15+ hrs, Good Conduct, Renewal Contract”
  - renewal_requirements: 3.25 GPA, 15+ hrs, Good Conduct, Renewal Contract ⟵ “Eagle Academic Scholarship | Full Tuition | 3.25+ | Valedictorian or Salutatorian | 3.25 GPA, 15+ hrs, Good Conduct, Renewal Contract”
### `c6a84b268a68d1be` Tougaloo College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tougaloo.edu/admissions/scholarships (sha256 628e79332b54)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0+ ⟵ “Servant Leader Academic Scholarship | Half Tuition | 3.0+ | ACT: 21+ / SAT: 1050+ | 3.0 GPA, 15+ hrs, Good Conduct, Renewal Contract”
  - test_requirement: ACT ACT: 21+ / SAT: 1050+ ⟵ “Servant Leader Academic Scholarship | Half Tuition | 3.0+ | ACT: 21+ / SAT: 1050+ | 3.0 GPA, 15+ hrs, Good Conduct, Renewal Contract”
  - renewal_requirements: 3.0 GPA, 15+ hrs, Good Conduct, Renewal Contract ⟵ “Servant Leader Academic Scholarship | Half Tuition | 3.0+ | ACT: 21+ / SAT: 1050+ | 3.0 GPA, 15+ hrs, Good Conduct, Renewal Contract”
### `4cafc0b84da9911c` University of Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://olemiss.edu/finaid/types-of-aid/sumners-scholarship/ (sha256 d9a28958f8be)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 per semester ⟵ “Half-Time | $2,500 per semester | $5,000 per academic year”
### `9c830bb212fb2579` University of Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://olemiss.edu/finaid/types-of-aid/sumners-scholarship/ (sha256 d9a28958f8be)
- checks: {"thresholds": null}
  - award_amount_text: $3,750 per semester ⟵ “3/4 Time | $3,750 per semester | $7,500 per academic year”
### `c5587671ec8793be` University of Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://olemiss.edu/finaid/types-of-aid/scholarships/non-resident/entering-freshman/awards-automatic-consideration/nr-freshman-merit/ (sha256 b71efbf81c50)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '3.0-3.49', 'test': '24-25 ACT1160-1220 SAT', 'amount_text': '$4,000'}, {'gpa': '3.0-3.49', 'test': '26-27 ACT1230-1290 SAT', 'amount_text': '$5,000'}, {'gpa': '3.0-3.49', 'test': '28-29 ACT1300-1350 SAT', 'amount_text': '$8,000'}, {'gpa': '3.0-3.49', 'test': '30-31 ACT1360-1410 SAT', 'amount_text': '$10,000'}, {'gpa': '3.0-3.49', 'test': '32+ ACT1420+ SAT', 'amount_text': '$15,000'}, {'gpa': '3.5-3.74', 'test': '24-25 ACT1160-1220 SAT', 'amount_text': '$7,000'}, {'gpa': '3.5-3.74', 'test': '26-27 ACT1230-1290 SAT', 'amount_text': '$8,000'}, {'gpa': '3.5-3.74', 'test': '28-29 ACT1300-1350 SAT', 'amount_text': '$10,000'}, {'gpa': '3.5-3.74', 'test': '30-31 ACT1360-1410 SAT', 'amount_text': '$15,000'}, {'gpa': '3.5-3.74', 'test': '32+ ACT1420+ SAT', 'amount_text': '$20,790'}, {'gpa': '3.75-4.0', 'test': '24-25 ACT1160-1220 SAT', 'amount_text': '$9,000'}, {'gpa': '3.75-4.0', 'test': '26-27 ACT1230-1290 SAT', 'amount_text': '$10,000'}, {'gpa': '3.75-4.0', 'test': '28-29 ACT1300-1350 SAT', 'amount_text': '$12,000'}, {'gpa': '3.75-4.0', 'test': '30-31 ACT1360-1410 SAT', 'amount_text': '$18,000'}, {'gpa': '3.75-4.0', 'test': '32+ ACT1420+ SAT', 'amount_text': '$20,790'}] ⟵ “High School GPA | No Test Score | 24-25 ACT1160-1220 SAT | 26-27 ACT1230-1290 SAT | 28-29 ACT1300-1350 SAT | 30-31 ACT1360-1410 SAT | 32+ ACT1420+ SAT || 3.0-3.49 | $3,000 | $4,000 | $5,000 | $8,000 | $10,000 | $15,000 || 3.5-3.74 | $5,000 | $7,000 | $8,000 | $10,000 | $15,000 | $20,790 || 3.75-4.0 ”
  - test_requirement: Tiers by High School GPA and 24-25 ACT1160-1220 SAT, 26-27 ACT1230-1290 SAT… ⟵ “High School GPA | No Test Score | 24-25 ACT1160-1220 SAT | 26-27 ACT1230-1290 SAT | 28-29 ACT1300-1350 SAT | 30-31 ACT1360-1410 SAT | 32+ ACT1420+ SAT || 3.0-3.49 | $3,000 | $4,000 | $5,000 | $8,000 | $10,000 | $15,000 || 3.5-3.74 | $5,000 | $7,000 | $8,000 | $10,000 | $15,000 | $20,790 || 3.75-4.0 ”
### `dfda3c5acc306c64` University of Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://olemiss.edu/finaid/types-of-aid/sumners-scholarship/ (sha256 d9a28958f8be)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 per semester ⟵ “Full Time | $5,000 per semester | $10,000 per academic year”
### `135d388460ecd81e` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 27 - 28 ACT Score ⟵ “27 - 28 ACT Score | $6,000 annually”
  - award_amount_text: $6,000 annually ⟵ “27 - 28 ACT Score | $6,000 annually”
### `165fca950696b91d` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 20 ACT Score ⟵ “20 ACT Score | $1,500 annually”
  - award_amount_text: $1,500 annually ⟵ “20 ACT Score | $1,500 annually”
### `1960a37b659323bc` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 31; SAT Test Score: 1390-1410 ⟵ “31 | 1390-1410 | $10,000”
  - award_amount_text: $10,000 ⟵ “31 | 1390-1410 | $10,000”
### `21e0c51bb419f465` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 26-29; SAT Test Score: 1230-1350 ⟵ “26-29 | 1230-1350 | $2,500”
  - award_amount_text: $2,500 ⟵ “26-29 | 1230-1350 | $2,500”
### `22a0ed7e41b9b001` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.0 - 3.24 GPA: 23 - 25 ACT Score ⟵ “23 - 25 ACT Score | $1,500 annually”
  - award_amount_text: $1,500 annually ⟵ “23 - 25 ACT Score | $1,500 annually”
### `27abfe0655399f14` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 25 - 26 ACT Score ⟵ “25 - 26 ACT Score | $5,250 annually”
  - award_amount_text: $5,250 annually ⟵ “25 - 26 ACT Score | $5,250 annually”
### `2ee6748bcb479b0b` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.0 - 3.24 GPA: 32 - 36 ACT Score ⟵ “32 - 36 ACT Score | $4,500 annually”
  - award_amount_text: $4,500 annually ⟵ “32 - 36 ACT Score | $4,500 annually”
### `2f6424311b5344fe` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 22 ACT Score ⟵ “22 ACT Score | $3,000 annually”
  - award_amount_text: $3,000 annually ⟵ “22 ACT Score | $3,000 annually”
### `310b9da8e3fe6f8c` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 21 ACT Score ⟵ “21 ACT Score | $2,500 annually”
  - award_amount_text: $2,500 annually ⟵ “21 ACT Score | $2,500 annually”
### `36c3add1f56b91cc` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 30 ACT Score ⟵ “30 ACT Score | $9,000 annually”
  - award_amount_text: $9,000 annually ⟵ “30 ACT Score | $9,000 annually”
### `3d98ad71935d773f` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 25-26; SAT Test Score: 1200-1250 ⟵ “25-26 | 1200-1250 | $5,250”
  - award_amount_text: $5,250 ⟵ “25-26 | 1200-1250 | $5,250”
### `3e70f62c559f2880` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 32-36; SAT Test Score: 1420-1600 ⟵ “32-36 | 1420-1600 | $4,500”
  - award_amount_text: $4,500 ⟵ “32-36 | 1420-1600 | $4,500”
### `4a2420043bea3ede` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 20 ACT Score ⟵ “20 ACT Score | $1,500 annually”
  - award_amount_text: $1,500 annually ⟵ “20 ACT Score | $1,500 annually”
### `61de0fa8bbdaf46a` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 30; SAT Test Score: 1360-1380 ⟵ “30 | 1360-1380 | $9,000”
  - award_amount_text: $9,000 ⟵ “30 | 1360-1380 | $9,000”
### `6434021c89f92765` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.0 - 3.24 GPA: 26 - 29 ACT Score ⟵ “26 - 29 ACT Score | $2,500 annually”
  - award_amount_text: $2,500 annually ⟵ “26 - 29 ACT Score | $2,500 annually”
### `66df4cfb88d9a2a9` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 31 ACT Score ⟵ “31 ACT Score | $10,000 annually”
  - award_amount_text: $10,000 annually ⟵ “31 ACT Score | $10,000 annually”
### `72aa566cd1fd8a32` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 23 - 24 ACT Score ⟵ “23 - 24 ACT Score | $4,500 annually”
  - award_amount_text: $4,500 annually ⟵ “23 - 24 ACT Score | $4,500 annually”
### `76e2c09b8e36703a` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 32 - 36 ACT Score ⟵ “32 - 36 ACT Score | Full value of tuition”
  - award_amount_text: Full value of tuition ⟵ “32 - 36 ACT Score | Full value of tuition”
### `7ee31d5536e60bf3` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 21; SAT Test Score: 1060-1090 ⟵ “21 | 1060-1090 | $2,500”
  - award_amount_text: $2,500 ⟵ “21 | 1060-1090 | $2,500”
### `81889b9731b85e42` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 29 ACT Score ⟵ “29 ACT Score | $7,000 annually”
  - award_amount_text: $7,000 annually ⟵ “29 ACT Score | $7,000 annually”
### `8c44b2baa99483d6` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 27-28; SAT Test Score: 1260-1320 ⟵ “27-28 | 1260-1320 | $6,000”
  - award_amount_text: $6,000 ⟵ “27-28 | 1260-1320 | $6,000”
### `8e4f7b0189f5f808` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.0 - 3.24 GPA: 30 - 31 ACT Score ⟵ “30 - 31 ACT Score | $3,000 annually”
  - award_amount_text: $3,000 annually ⟵ “30 - 31 ACT Score | $3,000 annually”
### `9289d7ff5881e98b` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 31 ACT Score ⟵ “31 ACT Score | $10,000 annually”
  - award_amount_text: $10,000 annually ⟵ “31 ACT Score | $10,000 annually”
### `98c4258eea83a78b` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 29 ACT Score ⟵ “29 ACT Score | $7,000 annually”
  - award_amount_text: $7,000 annually ⟵ “29 ACT Score | $7,000 annually”
### `9d8baf746944c061` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 27 - 28 ACT Score ⟵ “27 - 28 ACT Score | $6,000 annually”
  - award_amount_text: $6,000 annually ⟵ “27 - 28 ACT Score | $6,000 annually”
### `9f241d6e5170ea7e` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 30-31; SAT Test Score: 1360-1410 ⟵ “30-31 | 1360-1410 | $3,000”
  - award_amount_text: $3,000 ⟵ “30-31 | 1360-1410 | $3,000”
### `a1cac64d95dffb78` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 21 ACT Score ⟵ “21 ACT Score | $2,500 annually”
  - award_amount_text: $2,500 annually ⟵ “21 ACT Score | $2,500 annually”
### `a5eb7d610c969f94` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 23 - 24 ACT Score ⟵ “23 - 24 ACT Score | $4,500 annually”
  - award_amount_text: $4,500 annually ⟵ “23 - 24 ACT Score | $4,500 annually”
### `a6b493c731facaea` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 22 ACT Score ⟵ “22 ACT Score | $3,000 annually”
  - award_amount_text: $3,000 annually ⟵ “22 ACT Score | $3,000 annually”
### `c896893d73451588` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 20; SAT Test Score: 1030-1050 ⟵ “20 | 1030-1050 | $1,500”
  - award_amount_text: $1,500 ⟵ “20 | 1030-1050 | $1,500”
### `c943b3d5ddc4993c` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 23-24; SAT Test Score: 1130-1190 ⟵ “23-24 | 1130-1190 | $4,500”
  - award_amount_text: $4,500 ⟵ “23-24 | 1130-1190 | $4,500”
### `d37166844d9445f6` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 29; SAT Test Score: 1330-1350 ⟵ “29 | 1330-1350 | $7,000”
  - award_amount_text: $7,000 ⟵ “29 | 1330-1350 | $7,000”
### `e0a772ee53903e0f` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.25 - 3.59 GPA: 25 - 26 ACT Score ⟵ “25 - 26 ACT Score | $5,250 annually”
  - award_amount_text: $5,250 annually ⟵ “25 - 26 ACT Score | $5,250 annually”
### `e50c42423792d26c` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 32 - 36 ACT Score ⟵ “32 - 36 ACT Score | Full value of tuition + freshman year housing”
  - award_amount_text: Full value of tuition + freshman year housing ⟵ “32 - 36 ACT Score | Full value of tuition + freshman year housing”
### `f57661c5a5865d1a` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 22; SAT Test Score: 1100-1120 ⟵ “22 | 1100-1120 | $3,000”
  - award_amount_text: $3,000 ⟵ “22 | 1100-1120 | $3,000”
### `f5da4ff603218fd7` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- checks: {"thresholds": null}
  - gpa_requirement: 3.6 GPA or higher: 30 ACT Score ⟵ “30 ACT Score | $9,000 annually”
  - award_amount_text: $9,000 annually ⟵ “30 ACT Score | $9,000 annually”
### `f93ace42f9686519` University of Southern Mississippi — awards 2026-27 [new] (labeled_in_source)
- source: https://www.usm.edu/scholarships-financial-wellness/freshman_scholarships/academicexcellence.php (sha256 94e7d3e57cb3)
- checks: {"thresholds": null}
  - test_requirement: ACT Test Score: 23-25; SAT Test Score: 1130-1220 ⟵ “23-25 | 1130-1220 | $1,500”
  - award_amount_text: $1,500 ⟵ “23-25 | 1130-1220 | $1,500”
### `2b174b0ca6533665` University of Southern Mississippi — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.usm.edu/financial-aid/cost-of-attendance-future-year.php (sha256 baf93fa8e5d6)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 10794 ⟵ “Tuition/Fees | $10,794 | $12,794”
  - on_campus:Transportation: 1028 ⟵ “Transportation | $1,028 | $1,028”
  - on_campus:Housing/Food: 12320 ⟵ “Housing/Food | $12,320 | $12,320”
  - on_campus:Personal Expenses: 2154 ⟵ “Personal Expenses | $2,154 | $2,154”
  - on_campus:Course Fees: 596 ⟵ “Course Fees | $596 | $596”
  - on_campus:Books/Supplies: 764 ⟵ “Books/Supplies | $764 | $764”
  - on_campus:TOTAL: 27656 ⟵ “TOTAL | $27,656 | $29,656”
### `6359dc4dadaa52ce` University of Southern Mississippi — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.usm.edu/financial-aid/cost-of-attendance-future-year.php (sha256 baf93fa8e5d6)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 12794 ⟵ “Tuition/Fees | $10,794 | $12,794”
  - on_campus:Transportation: 1028 ⟵ “Transportation | $1,028 | $1,028”
  - on_campus:Housing/Food: 12320 ⟵ “Housing/Food | $12,320 | $12,320”
  - on_campus:Personal Expenses: 2154 ⟵ “Personal Expenses | $2,154 | $2,154”
  - on_campus:Course Fees: 596 ⟵ “Course Fees | $596 | $596”
  - on_campus:Books/Supplies: 764 ⟵ “Books/Supplies | $764 | $764”
  - on_campus:TOTAL: 29656 ⟵ “TOTAL | $27,656 | $29,656”
### `eae7b85f3d913d2b` Wesley Biblical Seminary — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://wbs.edu/college/dual-enrollment/ (sha256 f602acd44745)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “High School GPA of 2.5+”
### `e11b0a85e3e74dba` William Carey University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.wmcarey.edu/admissions/transfer/faq (sha256 b16671c8c303)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “If you are transferring from a four-year university or college, the last 30 hours of your degree must be taken at WCU.”

## Exceptions (97)

### `55904c16b618ff21` state-MS — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://www.mississippi.edu/student-parent-resources/reverse-transfer (sha256 9cb8e28c6a5f)
- issues: semantic_review_required
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “Contact the registrar at the community college you attended and ask them to analyze your transcript with the credits you earned at both institutions to determine if you are eligible to receive an associate degree.”
### `695c7c00aed078ef` state-MS — state_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://www.mississippi.edu/sites/default/files/ihl/files/Final%20Procedures%20Manual%20Fall%202026%20July.pdf (sha256 13b8ad9f64b4)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"effective": 7, "exceptions": 6, "requirements": 83}
  - statements.requirements: 83 ⟵ “History & Mission......................................................................................................................................3 Overview...........................................................................................................................................”
  - statements.effective: 7 ⟵ “The manual vide admission for qualified secondary      is updated annually and approved by students and seamless transfer of credits   the MS Community College Academic earned to college and career postsecond-    Officers’Association and the MS IHL ary institutions.”
  - statements.exceptions: 6 ⟵ “An exception to this requirement may include students classified as a junior planning to graduate prior to the spring of their senior year. 3.”
### `15af3ff24aa53d28` Alcorn State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.alcorn.edu/financial-aid/satisfactory-academic-progress-standards/ (sha256 e8d2c9782361)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Detailed Personal Statement: Federal regulations requires that you provide a detailed explanation of the special circumstances that prevented you from maintaining satisfactory academic progress.”
  - sentence: need_based_special_circumstances ⟵ “Specific dates as to when your special circumstance occurred, and detailed documentation to support your statement.”
### `66de74238963b11e` Alcorn State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.alcorn.edu/financial-aid/satisfactory-academic-progress-standards/ (sha256 e8d2c9782361)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “Students who lose eligibility for federal, state, and institutional aid due to not meeting SAP requirements may submit a Satisfactory Academic Progression Appeal for Eligibility Application.”
  - sentence: sap_appeal ⟵ “Appeal: See SAP Appeal Process Financial Aid Probation Financial Aid Probation status is assigned to students who fail to make SAP and who has successfully appealed and has had eligibility for financial aid reinstated.”
  - sentence: sap_appeal ⟵ “SAP Appeal Process If students do not meet SAP at the end of the spring semester, an appeal process is available for those students with extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Students can appeal for reinstatement of Financial Aid by completing the Satisfactory Academic Progression Appeal for Eligibility Application.”
  - sentence: sap_appeal ⟵ “Important Facts Concerning the SAP Appeal Process Financial Aid policies are not directly related to policies for academic admission.”
  - sentence: sap_appeal ⟵ “All documents must be submitted along with the SAP Appeal Application online.”
### `04eddfc1e8011352` Belhaven University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.belhaven.edu/admission/undergrad/aid/ (sha256 6c8de6f61bb8)
- issues: conflicting_sources:https://www.belhaven.edu/admission/undergrad/aid/tuition-calculator.html
- checks: {"columns": 1, "rows": 2}
  - column:Tuition (full-time 12-18 hours): 30700 ⟵ “Tuition (full-time 12-18 hours) | $15,350 | $30,700”
  - column:Student Activity Fee: 790 ⟵ “Student Activity Fee | $395 | $790”
### `a12753a960de62cc` Belhaven University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.belhaven.edu/admission/undergrad/aid/tuition-calculator.html (sha256 57ed71e64f98)
- issues: conflicting_sources:https://www.belhaven.edu/admission/undergrad/aid/
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 0 ⟵ “Tuition | please select a year | $0 | $0”
  - column:Housing: 0 ⟵ “Housing | please select a housing option | $0 | $0”
  - column:Fees: 0 ⟵ “Fees | Student Activity Fee | $0 | $0”
  - column:International No Yes: 0 ⟵ “International No Yes | International Student Fees | $0 | $0”
  - column:Totals: 0 ⟵ “Totals | Total Expenses | $0 | $0”
### `123aa5765b06d3b0` Coahoma Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coahomacc.edu/financialaid/sap/index.html (sha256 01ba9ce2a955)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Step 2: Appeal Student MUST log in to StudentForms account to complete the SAP Appeal form.”
  - sentence: sap_appeal ⟵ “Click here to view the SAP appeal process and How-To Guide.”
  - sentence: sap_appeal ⟵ “Navigation General Information CARES Act Information Disbursement Information StudentForms Portal Gainful Employment Policy & Procedures Manual Professional Judgment Satisfactory Academic Progress (SAP) Repeated Coursework Policy Sources of Financial Aid Financial Aid Policy & Procedures Manual Veterans Benefits Summer Pell Grant Eligibility Frequently Asked Questions (FAQ) SAP Appeal Process Face”
### `830a6d9f2ce078d7` Coahoma Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coahomacc.edu/financialaid/professional-judgement.html (sha256 bc1d81e7345a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “When these situations occur, it is possible to re-evaluate a student’s aid eligibility based on their current circumstances through the Professional Judgment (PJ) process.”
  - sentence: professional_judgment ⟵ “A Professional Judgment cannot be processed for changes until verification is complete.”
  - sentence: professional_judgment ⟵ “Please note, there must be a significant change to the household finances or circumstances to be considered for a Professional Judgment.”
### `a349ee472d7512b7` Coahoma Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coahomacc.edu/financialaid/professional-judgement.html (sha256 bc1d81e7345a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abuse or abandonment, incarceration), more commonly referred to as a dependency override.”
### `1663fcd5565c17ce` Coahoma Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.coahomacc.edu/admissions/tuition-fees/index.html (sha256 489a151f2e74)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 28}
  - column:Tuition (per semester): 1700.0 ⟵ “Tuition (per semester) | $1700.00”
  - column:Publication Fee (once per year): 60.0 ⟵ “Publication Fee (once per year) | $60.00”
  - column:Technology Fee (per semester): 100.0 ⟵ “Technology Fee (per semester) | $100.00”
  - column:Lab Fee (Science Majors): 40.0 ⟵ “Lab Fee (Science Majors) | $40.00”
  - column:Fees for Students Enrolled in Science Courses: 8.0 ⟵ “Fees for Students Enrolled in Science Courses | $8.00”
  - column:Science/Math Major Fee: 25.0 ⟵ “Science/Math Major Fee | $25.00”
  - column:Full-Time: 75.0 ⟵ “Full-Time | $75.00”
  - column:Part-Time: 38.0 ⟵ “Part-Time | $38.00”
  - column:Dual Enrollment: 38.0 ⟵ “Dual Enrollment | $38.00”
  - column:Room Rentals (per semester): 980.0 ⟵ “Room Rentals (per semester) | $980.00”
  - column:Board: Seven-Day Plan: 1555.0 ⟵ “Board: Seven-Day Plan | $1555.00”
  - column:Board: Commuter Meal Plan: 1036.0 ⟵ “Board: Commuter Meal Plan | $1036.00”
  - column:Housing Application (Non-Refundable)This fee does not apply toward room cost.: 100.0 ⟵ “Housing Application (Non-Refundable)This fee does not apply toward room cost. | $100.00”
  - column:LATE REGISTRATION FEE: 25.0 ⟵ “LATE REGISTRATION FEE | $25.00”
  - column:CLASS CHANGE AND WITHDRAWAL (For each class change after 1st day of class meeting): 10.0 ⟵ “CLASS CHANGE AND WITHDRAWAL (For each class change after 1st day of class meeting) | $10.00”
  - column:TRANSPORTATION FEE-BUS (per semester): 475.0 ⟵ “TRANSPORTATION FEE-BUS (per semester) | $475.00”
  - column:OUT-OF-STATE FEE (per semester): 1700.0 ⟵ “OUT-OF-STATE FEE (per semester) | $1,700.00”
  - column:INTERNATIONAL STUDENT FEE (per semester): 1700.0 ⟵ “INTERNATIONAL STUDENT FEE (per semester) | $1,700.00”
  - column:RETURNED CHECK FEE: 40.0 ⟵ “RETURNED CHECK FEE | $40.00”
  - column:ONLINE/VIRTUAL COMMUNITY COLLEGE FEE: 50.0 ⟵ “ONLINE/VIRTUAL COMMUNITY COLLEGE FEE | $50.00”
  - column:STUDENT IDENTIFICATION CARD (replacement): 25.0 ⟵ “STUDENT IDENTIFICATION CARD (replacement) | $25.00”
  - column:Off-Campus Fee: 35.0 ⟵ “Off-Campus Fee | $35.00”
  - column:Publication Fee (full-time students only/once per year): 60.0 ⟵ “Publication Fee (full-time students only/once per year) | $60.00”
  - column:Technology Fee (per semester for full-time and online students): 100.0 ⟵ “Technology Fee (per semester for full-time and online students) | $100.00”
  - column:Housing Application (Non-Refundable)This fee does not apply toward room cost. (2): 25.0 ⟵ “Housing Application (Non-Refundable)This fee does not apply toward room cost. | $25.00”
  - … 3 more rows
### `3c7a7db3b052173c` Copiah-Lincoln Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.colin.edu/students/financial-aid-scholarships/financial-aid-forms-appeal-process/ (sha256 6f607c465768)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an aid administrator adjusting data elements in the COA or in the SAI calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration), more commonly referred to as a dependency override.”
### `65994c0fdd08595f` Copiah-Lincoln Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.colin.edu/wp-content/uploads/2025/09/SAP-Policy_Sep25.pdf (sha256 157a456f4248)
- issues: semantic_review_required, conflicting_sources:https://www.colin.edu/students/financial-aid-scholarships/financial-aid-forms-appeal-process/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal Process: Students must request AND complete an SAP Appeal before the first day of class.”
  - sentence: sap_appeal ⟵ “The student must email the Director requesting to open an SAP Appeal to mary.haralson@colin.edu.”
### `9dfa665bb8cb4bcf` Copiah-Lincoln Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.colin.edu/students/financial-aid-scholarships/financial-aid-forms-appeal-process/ (sha256 6f607c465768)
- issues: semantic_review_required, conflicting_sources:https://www.colin.edu/wp-content/uploads/2025/09/SAP-Policy_Sep25.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeals If after a review of your academic history it has been determined that you are not meeting one or more of the standards established in the Satisfactory Academic Progress (SAP) Policy and have been placed on Financial Aid Suspension.”
### `2a22dbc45674419f` Copiah-Lincoln Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.colin.edu/wp-content/uploads/2026/06/COA-WORKSHEET-26-27.pdf (sha256 e70c54edd95d)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 2, "rows": 30}
  - column:TUITION & FEES: 5010 ⟵ “TUITION & FEES | 5010”
  - column:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 1500 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | 1500”
  - column:LIVING EXPENSES (FOOD & HOUSING): 6000 ⟵ “LIVING EXPENSES (FOOD & HOUSING) | 6000”
  - column:MISCELLANEOUS PERSONAL *must be at least 1/2 time: 1400 ⟵ “MISCELLANEOUS PERSONAL *must be at least 1/2 time | 1400”
  - column:TRANSPORTATION: 2250 ⟵ “TRANSPORTATION | 2250”
  - column:TOTAL: 16160 ⟵ “TOTAL | 16160”
  - column:TUITION & FEES (2): 7010 ⟵ “TUITION & FEES | 7010”
  - column:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT (2): 1500 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | 1500”
  - column:LIVING EXPENSES (FOOD & HOUSING) (2): 6000 ⟵ “LIVING EXPENSES (FOOD & HOUSING) | 6000”
  - column:MISCELLANEOUS PERSONAL *must be at least 1/2 time (2): 1400 ⟵ “MISCELLANEOUS PERSONAL *must be at least 1/2 time | 1400”
  - column:TRANSPORTATION (2): 2250 ⟵ “TRANSPORTATION | 2250”
  - column:TOTAL (2): 18160 ⟵ “TOTAL | 18160”
  - column:TUITION & FEES (3): 5010 ⟵ “TUITION & FEES | 5010”
  - column:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT (3): 1500 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | 1500”
  - column:LIVING EXPENSES (FOOD & HOUSING) (3): 6000 ⟵ “LIVING EXPENSES (FOOD & HOUSING) | 6000”
  - column:MISCELLANEOUS PERSONAL *must be at least 1/2 time (3): 1800 ⟵ “MISCELLANEOUS PERSONAL *must be at least 1/2 time | 1800”
  - column:TRANSPORTATION (3): 2250 ⟵ “TRANSPORTATION | 2250”
  - column:TOTAL (3): 16560 ⟵ “TOTAL | 16560”
  - column:TUITION & FEES (4): 7010 ⟵ “TUITION & FEES | 7010”
  - column:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT (4): 1500 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | 1500”
  - column:LIVING EXPENSES (FOOD & HOUSING) (4): 6000 ⟵ “LIVING EXPENSES (FOOD & HOUSING) | 6000”
  - column:MISCELLANEOUS PERSONAL *must be at least 1/2 time (4): 1800 ⟵ “MISCELLANEOUS PERSONAL *must be at least 1/2 time | 1800”
  - column:TRANSPORTATION (4): 2250 ⟵ “TRANSPORTATION | 2250”
  - column:TOTAL (4): 18560 ⟵ “TOTAL | 18560”
  - column:TUITION & FEES *: 2400 ⟵ “TUITION & FEES * | 2400 | 3400”
  - … 11 more rows
### `04bb886ed005987a` East Central Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eccc.edu/sites/default/files/2025-10/SAP%20Fin.%20Aid%20Appeal%20Form.pdf (sha256 4f62d6b5b60f)
- issues: semantic_review_required, conflicting_sources:https://www.eccc.edu/financial-aid,https://www.eccc.edu/sites/default/files/2025-10/Max%20Credit%20Appeal%20Form.pdf,https://www.eccc.edu/sites/default/files/rights_and_responsibilities_with_sap_and_conditions_0_1.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “EAST CENTRAL COMMUNITY COLLEGE SATISFACTORY ACADEMIC PROGRESS FINANCIAL AID APPEAL FORM Please fill out this form completely using blue or black ink.”
  - sentence: sap_appeal ⟵ “If this appeal is approved, I understand that approval of my Satisfactory Academic Progress (SAP) appeal is contingent upon my commitment to meet the college’s SAP standards.”
### `72502ef32350177b` East Central Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.eccc.edu/financial-aid (sha256 717e30cf5b59)
- issues: semantic_review_required, conflicting_sources:https://www.eccc.edu/sites/default/files/2025-10/Max%20Credit%20Appeal%20Form.pdf,https://www.eccc.edu/sites/default/files/2025-10/SAP%20Fin.%20Aid%20Appeal%20Form.pdf,https://www.eccc.edu/sites/default/files/rights_and_responsibilities_with_sap_and_conditions_0_1.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Friday 8 a.m. - Noon Financial Aid ECCC Financial Aid FAQ It's FAFSA Time Verification Information Veteran Information FSA IDFederal Aid (FAFSA)Summer Financial AidState AidWork StudySatisfactory Academic ProgressFinancial Aid Appeal FormsSpecial and Unusual CircumstancesIn-District Tuition ScholarshipContact Us Net Price Calculator Quick Links Annual Public Notice Academic Calendar Admissions Adv”
### `b7316d01ca23ac7c` East Central Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eccc.edu/sites/default/files/rights_and_responsibilities_with_sap_and_conditions_0_1.pdf (sha256 a9f9c58ebc90)
- issues: semantic_review_required, conflicting_sources:https://www.eccc.edu/financial-aid,https://www.eccc.edu/sites/default/files/2025-10/Max%20Credit%20Appeal%20Form.pdf,https://www.eccc.edu/sites/default/files/2025-10/SAP%20Fin.%20Aid%20Appeal%20Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “To request an appeal, students must complete the Financial Aid SAP Appeal Form which is available in the ECCC Financial Aid Office.”
### `d70ebd23ca04fd75` East Central Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eccc.edu/sites/default/files/2025-10/Max%20Credit%20Appeal%20Form.pdf (sha256 0e137da87885)
- issues: semantic_review_required, conflicting_sources:https://www.eccc.edu/financial-aid,https://www.eccc.edu/sites/default/files/2025-10/SAP%20Fin.%20Aid%20Appeal%20Form.pdf,https://www.eccc.edu/sites/default/files/rights_and_responsibilities_with_sap_and_conditions_0_1.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “EAST CENTRAL COMMUNITY COLLEGE SATISFACTORY ACADEMIC PROGRESS FINANCIAL AID MAX CREDIT - APPEAL FORM Please fill out this form completely using blue or black ink.”
  - sentence: sap_appeal ⟵ “If this appeal is approved, I understand that approval of my Satisfactory Academic Progress (SAP) appeal is contingent upon my commitment to meet the college’s SAP standards.”
### `meb2923410c5ff85` East Mississippi Community College — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.eastms.edu/programs/dual-enrollment (sha256 c787ffddd8b4)
- issues: stale_year_label:2024-25
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a 3.0 or better grade point average on a 4.0 scale.”
  - max_credit_hours_per_term: 15 ⟵ “$45 per course up to 15 hours per semester plus cost of books”
  - per_credit_hour_charge: 165 ⟵ “$165 per hour after 15 hours per semester plus the cost of books”
  - per_credit_hour_charge: 265 ⟵ “Out-of-state students will be charged $265 per hour plus the cost of books.”
  - eligibility_tier: 3.0 ⟵ “Have a 3.0 or better grade point average on a 4.0 scale.”
  - max_credit_hours_per_term: 15 ⟵ “$45 per course up to 15 hours per semester plus cost of books”
  - per_credit_hour_charge: 165 ⟵ “$165 per hour after 15 hours per semester plus the cost of books”
  - per_credit_hour_charge: 265 ⟵ “Out-of-state students will be charged $265 per hour plus the cost of books.”
### `bb3d423185fccc54` Hinds Community College — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.hindscc.edu/admissions/costs-aid/satisfactory-academic-progress (sha256 123dbed67cc4)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The student may pay their educational expenses out-of-pocket and attempt to regain eligibility with the SAP requirements, or the student may appeal the suspension if there are any extenuating or special circumstances that prevented them from meeting the SAP requirements.”
### `f99ad3a1159701d9` Hinds Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://hub.hindscc.edu/hubfs/Documents/Financial_Aid/2026-27/SAP%20Appeal%202026-2027.pdf (sha256 647f4fd17ed8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Page 1 of 2 Request to Appeal Satisfactory Academic Progress Continued E.”
### `20cdb24b1a453f31` Hinds Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.hindscc.edu/admissions/costs-aid/cost-of-attendance (sha256 e87ad8e4ab05)
- issues: ambiguous_year_labels, arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 5}
  - column:Tuition (15 credits per semester): 4000 ⟵ “Tuition (15 credits per semester) | $4,000 | $4,000 | $4,000”
  - column:Registration Fee: 600 ⟵ “Registration Fee | $600 | $600 | $600”
  - column:Dorm: 2400 ⟵ “Dorm | $2,400 | – | –”
  - column:Meal Plan: 3500 ⟵ “Meal Plan | $3,500 | – | –”
  - column:Total: 10500 ⟵ “Total | $10,500 | $4,600 | $4,600”
  - column:Tuition (15 credits per semester): 4000 ⟵ “Tuition (15 credits per semester) | $4,000 | $4,000 | $4,000”
  - column:Registration Fee: 600 ⟵ “Registration Fee | $600 | $600 | $600”
  - column:Total: 4600 ⟵ “Total | $10,500 | $4,600 | $4,600”
  - column:Tuition (15 credits per semester): 4000 ⟵ “Tuition (15 credits per semester) | $4,000 | $4,000 | $4,000”
  - column:Registration Fee: 600 ⟵ “Registration Fee | $600 | $600 | $600”
  - column:Total: 4600 ⟵ “Total | $10,500 | $4,600 | $4,600”
### `e9223d2753017eba` Hinds Community College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.hindscc.edu/admissions/costs-aid/cost-of-attendance (sha256 dd801f071f86)
- issues: ambiguous_year_labels, arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 5}
  - column:Tuition (15 credits per semester): 6750 ⟵ “Tuition (15 credits per semester) | $6,750 | $6,750 | $6,750”
  - column:Registration Fee: 600 ⟵ “Registration Fee | $600 | $600 | $600”
  - column:Dorm: 2600 ⟵ “Dorm | $2,600 | – | –”
  - column:Meal Plan: 3500 ⟵ “Meal Plan | $3,500 | – | –”
  - column:Total: 13450 ⟵ “Total | $13,450 | $7,350 | $7,350”
  - column:Tuition (15 credits per semester): 6750 ⟵ “Tuition (15 credits per semester) | $6,750 | $6,750 | $6,750”
  - column:Registration Fee: 600 ⟵ “Registration Fee | $600 | $600 | $600”
  - column:Total: 7350 ⟵ “Total | $13,450 | $7,350 | $7,350”
  - column:Tuition (15 credits per semester): 6750 ⟵ “Tuition (15 credits per semester) | $6,750 | $6,750 | $6,750”
  - column:Registration Fee: 600 ⟵ “Registration Fee | $600 | $600 | $600”
  - column:Total: 7350 ⟵ “Total | $13,450 | $7,350 | $7,350”
### `9d44c6873c2cdafb` Jones County Junior College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.jcjc.edu/admissions/ (sha256 aa3074a3d160)
- issues: rows_without_score
- checks: {"distinct_exams": 11, "equivalencies": 11, "rows_without_score": 11}
  - equivalencies[AP-DRAWING|None]:  ⟵ “Art, Drawing | ART 1313, 1323”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | BIO 1114, 1124”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | CHE 1214, 1224”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Economics, Macro | ECO 2113”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Economics, Micro | ECO 2123”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language and Composition | ENG 1113”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|None]:  ⟵ “US Government and Politics | PSC 1113”
  - equivalencies[AP-WORLD-HISTORY-MODERN|None]:  ⟵ “World History | HIS 1113, 1123”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB, BC | MAT 1613, 1623”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|None]:  ⟵ “Spanish Language and Culture Level I | MFL 1213, 1223”
  - equivalencies[AP-PSYCHOLOGY|None]:  ⟵ “Psychology | PSY 1513”
### `e05e166efc66544b` Jones County Junior College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.jcjc.edu/admissions/ (sha256 aa3074a3d160)
- issues: rows_without_score
- checks: {"distinct_exams": 16, "equivalencies": 16, "rows_without_score": 16}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|None]:  ⟵ “American Government | PSC 1113”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|None]:  ⟵ “US History I | HIS 2213”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|None]:  ⟵ “US History II | HIS 2223”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “Biology | BIO 1114”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “Business law | BAD 2413”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | MAT 1613”
  - equivalencies[CLEP-CHEMISTRY|None]:  ⟵ “Chemistry | CHE 1214”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “College Algebra | MAT 1313”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | ENG 1113”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “Spanish | MFL 1213”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|None]:  ⟵ “Information Systems & Computer Applications | CSC 1123”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “Principles of Macroeconomics | ECO 2113”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | ECO 2123”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Sociology | SOC 2113”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|None]:  ⟵ “Western Civilization I | HIS 1113”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|None]:  ⟵ “Western Civilization II | HIS 1123”
### `7b26ceac953b80ad` Meridian Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://meridiancc.edu/become_an_eagle/financial_aid/SAP_Nov2025.pdf (sha256 3e1b5e46ccc0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The student must attain a 2.00 for the semester and attain the minimum cumulative grade point average indicated by the satisfactory academic progress policy for federal financial aid recipients in order to be reinstated.  Appeal Process: A student who has at least a 1.50 cumulative grade point average may appeal the suspension of financial aid.”
### `0590620b7d6902a0` Millsaps College — appeals 2023-24 [new] (labeled_in_title)
- source: https://millsaps.edu/wp-content/uploads/2024/03/millsaps-2023-24-Catalog-Final.pdf (sha256 b423e33f02bf)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The student may appeal the Financial Aid Suspension if unusual circumstances beyond their control prevented them from meeting satisfactory academic progress (see appeal process).”
  - sentence: sap_appeal ⟵ “Approved Appeals and Satisfactory Academic Progress Probation For approved appeals, the student will be placed on Satisfactory Academic Progress Probation (SAP). (Financial Aid SAP Probation is for financial aid purposes only and is separate from academic standing probation.) While on Satisfactory Academic Progress Probation, certain condition for academic performance will be set and monitored.”
### `287c34049aad3912` Millsaps College — appeals 2024-25 [new] (labeled_in_title)
- source: https://millsaps.edu/wp-content/uploads/2024/06/2024-25-Millsaps-College-Catalog.pdf (sha256 5aed4561e74c)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A leave of absence is granted for one semester, although in unusual circumstances a petition may be filed for an extension.”
### `3ddffda60cd8a049` Millsaps College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://millsaps.edu/apply-to-millsaps/financial-aid-scholarships/grants-loans-work-study/ (sha256 19573d5a1798)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://millsaps.edu/wp-content/uploads/2026/08/College-Catalog-2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The student may appeal the financial aid suspension if unusual circumstances beyond their control prevented them from meeting satisfactory academic progress (see Appeal Process).”
### `4f43858e5a1b60ad` Millsaps College — appeals 2026-27 [new] (labeled_in_title)
- source: https://millsaps.edu/wp-content/uploads/2026/08/College-Catalog-2026-27.pdf (sha256 9941ebd4f701)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A leave of absence is granted for one semester, although in unusual circumstances a petition may be filed for an extension.”
### `5ec2a0130ec07c12` Millsaps College — appeals 2026-27 [new] (labeled_in_title)
- source: https://millsaps.edu/wp-content/uploads/2026/08/College-Catalog-2026-27.pdf (sha256 9941ebd4f701)
- issues: semantic_review_required, conflicting_sources:https://millsaps.edu/apply-to-millsaps/financial-aid-scholarships/grants-loans-work-study/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The student may appeal the Financial Aid Suspension if unusual circumstances beyond their control prevented them from meeting satisfactory academic progress (see appeal process).”
### `b0a1aa4cf71672f9` Millsaps College — appeals 2023-24 [new] (labeled_in_title)
- source: https://millsaps.edu/wp-content/uploads/2024/03/millsaps-2023-24-Catalog-Final.pdf (sha256 b423e33f02bf)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A leave of absence is granted for one semester, although in unusual circumstances a petition may be filed for an extension.”
### `fc48ef6253b8fc81` Millsaps College — appeals 2024-25 [new] (labeled_in_title)
- source: https://millsaps.edu/wp-content/uploads/2024/06/2024-25-Millsaps-College-Catalog.pdf (sha256 5aed4561e74c)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The student may appeal the Financial Aid Suspension if unusual circumstances beyond their control prevented them from meeting satisfactory academic progress (see appeal process).”
  - sentence: sap_appeal ⟵ “Approved Appeals and Satisfactory Academic Progress Probation For approved appeals, the student will be placed on Satisfactory Academic Progress Probation (SAP). (Financial Aid SAP Probation is for financial aid purposes only and is separate from academic standing probation.) While on Satisfactory Academic Progress Probation, certain condition for academic performance will be set and monitored.”
### `29820bc7db512e84` Mississippi College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.mc.edu/offices/financial-aid/forms/satisfactory-academic-progre (sha256 59cb53081e38)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 15}
  - sentence: sap_appeal ⟵ “A student may submit an SAP APPEAL and if approved the student will be placed on Financial Aid SAP Probation.”
  - sentence: sap_appeal ⟵ “Title IV aid consists of the following programs: Federal Pell Grant (PELL) Federal Supplemental Educational Opportunity Grant (SEOG) Teacher Education Assistance for College and Higher Education Grant (TEACH) Federal Work Study Federal Direct Loan Programs Subsidized Direct Loans Unsubsidized Direct Loans Parent PLUS Loans Grad PLUS Loans (“Legacy” Students Only) Students with extenuating circumst”
  - sentence: sap_appeal ⟵ “The SAP Appeal is reviewed by the SAP Appeal Committee and the appeal must include documentation the circumstances that prevented a student from maintaining academic success.”
  - sentence: sap_appeal ⟵ “If all other eligibility criteria have been met, students who have lost their financial aid eligibility due to this standard may apply for an SAP Appeal and regain eligibility through a successful submission.”
  - sentence: sap_appeal ⟵ “If all other eligibility criteria have been met, students who have lost their financial aid eligibility due to this standard may apply for an SAP Appeal and regain eligibility through a successful submission.”
  - sentence: sap_appeal ⟵ “Loss of financial aid assistance eligibility Student may submit an SAP Appeal.”
### `8a2db3547d32f433` Mississippi College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.mc.edu/offices/financial-aid/forms/satisfactory-academic-progre (sha256 59cb53081e38)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of extenuating circumstances are: Death of a Relative Injury Illness Other special circumstances may be considered on a case-by-case basis The student should explain what has changed in their situation that would allow the student to demonstrate SAP at the end of the following semester.”
### `2e57a375e16a13f2` Mississippi College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mc.edu/offices/financial-aid/cost/2025-2026 (sha256 ec2f31d7491d)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - on_campus:TUITION: 22000.0 ⟵ “TUITION | $11,000 | $22,000.00”
  - on_campus:FEES: 2600.0 ⟵ “FEES | $1,300.00 | $2,600.00”
  - on_campus:HOUSING*: 8200.0 ⟵ “HOUSING* | $4,100.00 | $8,200.00”
  - on_campus:FOOD**: 5915.0 ⟵ “FOOD** | $2,958.00 | $5,915.00”
  - on_campus:BOOKS/SUPPLIES: 1800.0 ⟵ “BOOKS/SUPPLIES | $900.00 | $1,800.00”
  - on_campus:PERSONAL: 3152.0 ⟵ “PERSONAL | $1,575.00 | $3,152.00”
  - on_campus:TRANSPORTATION: 2653.0 ⟵ “TRANSPORTATION | $1,326.00 | $2,653.00”
  - on_campus:LOAN FEES: 171.0 ⟵ “LOAN FEES | $86.00 | $171.00”
  - on_campus:Total for Undergraduates Living On Campus: 46491.0 ⟵ “Total for Undergraduates Living On Campus | $23,245.00 | $46,491.00”
### `42a8c7286284793d` Mississippi College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mc.edu/offices/financial-aid/cost/2026-2027 (sha256 e65ae999785d)
- issues: conflicting_sources:https://www.mc.edu/offices/business/application/files/5517/8777/7146/Tuition_and_Fees_2026-27.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - on_campus:TUITION: 22000.0 ⟵ “TUITION | $11,000.00 | $22,000.00”
  - on_campus:FEES: 3600.0 ⟵ “FEES | $1,800.00 | $3,600.00”
  - on_campus:HOUSING*: 8482.0 ⟵ “HOUSING* | $4,241.00 | $8,482.00”
  - on_campus:FOOD**: 6142.0 ⟵ “FOOD** | $3,071.00 | $6,142.00”
  - on_campus:PERSONAL: 3150.0 ⟵ “PERSONAL | $1,575.00 | $3,150.00”
  - on_campus:TRANSPORTATION: 2835.0 ⟵ “TRANSPORTATION | $1,418.00 | $2,835.00”
  - on_campus:LOAN FEES: 98.0 ⟵ “LOAN FEES | $49.00 | $98.00”
  - on_campus:Total for Undergraduates Living On Campus: 46307.0 ⟵ “Total for Undergraduates Living On Campus | $23,154.00 | $46,307.00”
### `cf041d355bc0e5a9` Mississippi College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mc.edu/offices/business/application/files/5517/8777/7146/Tuition_and_Fees_2026-27.pdf (sha256 b8a20de83b9b)
- issues: conflicting_sources:https://www.mc.edu/offices/financial-aid/cost/2026-2027
- checks: {"columns": 1, "rows": 52}
  - column:Tuition (per semester): 11000.0 ⟵ “Tuition (per semester) | 11,000.00”
  - column:General registration fee: 1800.0 ⟵ “General registration fee | 1,800.00”
  - column:General registration fee (2): 1125.0 ⟵ “General registration fee | 1,125.00”
  - column:General registration fee (Winter/Maymester): 100.0 ⟵ “General registration fee (Winter/Maymester) | 100.00”
  - column:RN to BSN general education tuition (per 3 hour course): 510.0 ⟵ “RN to BSN general education tuition (per 3 hour course) | 510.00”
  - column:Doctorate Professional Counseling (fixed for remainder of program): 750.0 ⟵ “Doctorate Professional Counseling (fixed for remainder of program) | 750.00”
  - column:Health Science Post-Baccalaureate Certificate: 250.0 ⟵ “Health Science Post-Baccalaureate Certificate | 250.00”
  - column:M.Ed. in Teaching Arts Program (alternate route): 305.0 ⟵ “M.Ed. in Teaching Arts Program (alternate route) | 305.00”
  - column:Military (active duty): 375.0 ⟵ “Military (active duty) | 375.00”
  - column:General registration fee (Winter/Maymester) (2): 100.0 ⟵ “General registration fee (Winter/Maymester) | 100.00”
  - column:Tuition (fixed for the remainder of program): 12250.0 ⟵ “Tuition (fixed for the remainder of program) | 12,250.00”
  - column:General registration fee (Fall/Spring): 1025.0 ⟵ “General registration fee (Fall/Spring) | 1,025.00”
  - column:Masters of Business Administration: 600.0 ⟵ “Masters of Business Administration | 600.00”
  - column:M.S. in Healthcare Communication: 400.0 ⟵ “M.S. in Healthcare Communication | 400.00”
  - column:M.S. in Public Affairs Communication: 400.0 ⟵ “M.S. in Public Affairs Communication | 400.00”
  - column:M.S. in Sports Communication: 400.0 ⟵ “M.S. in Sports Communication | 400.00”
  - column:M.S. in Strategic Communication: 400.0 ⟵ “M.S. in Strategic Communication | 400.00”
  - column:M.Ed. in Curriculum & Instruction: 400.0 ⟵ “M.Ed. in Curriculum & Instruction | 400.00”
  - column:M.Ed. in Educational Leadership: 305.0 ⟵ “M.Ed. in Educational Leadership | 305.00”
  - column:M.Ed. in Elementary Education: 400.0 ⟵ “M.Ed. in Elementary Education | 400.00”
  - column:M.Ed. in Special Education: 400.0 ⟵ “M.Ed. in Special Education | 400.00”
  - column:M.S. in Organizational Leadership: 400.0 ⟵ “M.S. in Organizational Leadership | 400.00”
  - column:Ed. S. in Curriculum & Instruction: 400.0 ⟵ “Ed. S. in Curriculum & Instruction | 400.00”
  - column:Ed. S. in Educational Leadership: 364.0 ⟵ “Ed. S. in Educational Leadership | 364.00”
  - column:Ed. S. in Teacher Leadership: 364.0 ⟵ “Ed. S. in Teacher Leadership | 364.00”
  - … 27 more rows
### `fbd78436145ec374` Mississippi College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mc.edu/offices/financial-aid/cost/2024-2025 (sha256 7f61b6da5aaa)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - on_campus:TUITION: 21000.0 ⟵ “TUITION | $10,500.00 | $21,000.00”
  - on_campus:FEES: 2500.0 ⟵ “FEES | $1,250.00 | $2,500.00”
  - on_campus:HOUSING*: 9526.0 ⟵ “HOUSING* | $4,763.00 | $9,526.00”
  - on_campus:FOOD**: 6594.0 ⟵ “FOOD** | $3,297.00 | $6,594.00”
  - on_campus:BOOKS/SUPPLIES: 1700.0 ⟵ “BOOKS/SUPPLIES | $850.00 | $1,700.00”
  - on_campus:PERSONAL: 2500.0 ⟵ “PERSONAL | $1,250.00 | $2,500.00”
  - on_campus:TRANSPORTATION: 3537.0 ⟵ “TRANSPORTATION | $1,768.00 | $3,537.00”
  - on_campus:LOAN FEES: 171.0 ⟵ “LOAN FEES | $85.00 | $171.00”
  - on_campus:Total for Undergraduates Living On Campus: 47528.0 ⟵ “Total for Undergraduates Living On Campus | $23,763.00 | $47,528.00”
### `82b17ab669a126db` Mississippi Delta Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.msdelta.edu/paying-for-college/business-services/docs/fees-spring2026.pdf (sha256 68fa41518e7b)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown
- checks: {"columns": 5, "components_reconcile": false, "rows": 4}
  - column:Returned Check Fee: 40.0 ⟵ “Returned Check Fee | $40.00 | Duplicate Student ID card | $25.00”
  - column:Cap and Gown Fee: 35.0 ⟵ “Cap and Gown Fee | $35.00”
  - column:Full-time Student Activity Fee: 45.0 ⟵ “Full-time Student Activity Fee | $45.00”
  - column:Total Tuition and Fees (estimate): 1920.0 ⟵ “Total Tuition and Fees (estimate) | $1,920.00 | $4,320.00 | $3,220.00 | $5,620.00 | Total Tuition & Fees”
  - column:TUITION & FEES:: 25.0 ⟵ “TUITION & FEES: | Parking Decal | $25.00”
  - column:$180 per 4hr class: 500.0 ⟵ “$180 per 4hr class | Commuter Meal Plan (flex) | $500.00”
  - column:1st payment: 640.0 ⟵ “1st payment | January 13, 2026 | $640.00 | $1,440.00 | $1,073.34 | $1,873.34 | 1/3 of total tuition & fees”
  - column:2nd payment: 640.0 ⟵ “2nd payment | February 10, 2026 | $640.00 | $1,440.00 | $1,073.33 | $1,873.33 | 1/3 of total tuition & fees”
  - column:3rd payment: 640.0 ⟵ “3rd payment | March 10, 2026 | $640.00 | $1,440.00 | $1,073.33 | $1,873.33 | 1/3 of total tuition & fees”
  - column:Total Tuition and Fees (estimate): 4320.0 ⟵ “Total Tuition and Fees (estimate) | $1,920.00 | $4,320.00 | $3,220.00 | $5,620.00 | Total Tuition & Fees”
  - column:Part-time tuition(& hours > 21): 750.0 ⟵ “Part-time tuition(& hours > 21) | $160.00 per credit hour | Dorm (Female Room) | $750.00”
  - column:Technology Fee: 650.0 ⟵ “Technology Fee | an additional $10 per credit hour | Dorm (Male Room) | $650.00”
  - column:VCC (online) fees: 1200.0 ⟵ “VCC (online) fees | an additional $25 per credit hour | Dorm (Male Room-New Building) | $1200.00”
  - column:Dual Enrolled fees: 1650.0 ⟵ “Dual Enrolled fees | $135 per 3hr class | Meals (16 per wk & $350 flex) | $1,650.00”
  - column:Inclusive Access course fees: 13.0 ⟵ “Inclusive Access course fees | vary according to program | Transcript/Online Order | $13.00”
  - column:Returned Check Fee: 25.0 ⟵ “Returned Check Fee | $40.00 | Duplicate Student ID card | $25.00”
  - column:1st payment: 1440.0 ⟵ “1st payment | January 13, 2026 | $640.00 | $1,440.00 | $1,073.34 | $1,873.34 | 1/3 of total tuition & fees”
  - column:2nd payment: 1440.0 ⟵ “2nd payment | February 10, 2026 | $640.00 | $1,440.00 | $1,073.33 | $1,873.33 | 1/3 of total tuition & fees”
  - column:3rd payment: 1440.0 ⟵ “3rd payment | March 10, 2026 | $640.00 | $1,440.00 | $1,073.33 | $1,873.33 | 1/3 of total tuition & fees”
  - column:Total Tuition and Fees (estimate): 3220.0 ⟵ “Total Tuition and Fees (estimate) | $1,920.00 | $4,320.00 | $3,220.00 | $5,620.00 | Total Tuition & Fees”
  - column:1st payment: 1073.34 ⟵ “1st payment | January 13, 2026 | $640.00 | $1,440.00 | $1,073.34 | $1,873.34 | 1/3 of total tuition & fees”
  - column:2nd payment: 1073.33 ⟵ “2nd payment | February 10, 2026 | $640.00 | $1,440.00 | $1,073.33 | $1,873.33 | 1/3 of total tuition & fees”
  - column:3rd payment: 1073.33 ⟵ “3rd payment | March 10, 2026 | $640.00 | $1,440.00 | $1,073.33 | $1,873.33 | 1/3 of total tuition & fees”
  - column:Total Tuition and Fees (estimate): 5620.0 ⟵ “Total Tuition and Fees (estimate) | $1,920.00 | $4,320.00 | $3,220.00 | $5,620.00 | Total Tuition & Fees”
  - column:1st payment: 1873.34 ⟵ “1st payment | January 13, 2026 | $640.00 | $1,440.00 | $1,073.34 | $1,873.34 | 1/3 of total tuition & fees”
  - … 2 more rows
### `e04b8d1284396bdd` Mississippi Delta Community College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.msdelta.edu/programs/dual-enrollment/docs/de-manual-2025-2026.pdf (sha256 361fdbff430a)
- issues: stale_year_label:2025-26, multicolumn_layout_review, conflicting_values:max_credit_hours_per_term
- checks: {"fields": ["college_gpa_to_continue"], "tiers": 8}
  - eligibility_tier: 3.0 ⟵ “b. Have a minimum overall high school GPA of 3.0 on a 4.0 scale; and”
  - eligibility_tier: 3.0 ⟵ “a. Have a minimum high school GPA of 3.0 on a 4.0 scale;”
  - eligibility_tier: 2.0 ⟵ “•   Have a minimum overall high school GPA of 2.0 on a 4.0 scale; and”
  - eligibility_tier: 3.0 ⟵ “• Have a minimum overall high school GPA of 3.0 on a 4.0 scale; and”
  - eligibility_tier: 3.0 ⟵ “following criteria: be classified as a junior or higher; have a minimum overall high school GPA of 3.0 on a 4.0”
  - eligibility_tier: 2.0 ⟵ “the following criteria: be classified as a sophomore or higher; have a minimum overall high school GPA of 2.0”
  - eligibility_tier: 3.0 ⟵ “•   Minimum grade point average of 3.0 on a 4.0 scale”
  - eligibility_tier: 2.0 ⟵ “guidance counselor                                                  •    Have a minimum overall high school GPA of 2.0 on a 4.0 scale; and”
  - college_gpa_to_continue: 2.0 ⟵ “College, students must maintain a 2.0 MDCC GPA or higher.”
  - max_credit_hours_per_term: 7 ⟵ “*Students can take up to 7 hours per semester including Academic and CTE courses combined.”
  - max_credit_hours_per_term: 9 ⟵ “are only eligible to teach up to 9 hours per semester.”
### `19695e84610ac8ef` Mississippi Gulf Coast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://mgccc.edu/paying-for-college/financial-aid/ (sha256 c1cf42fd7d2c)
- issues: semantic_review_required, conflicting_sources:https://mgccc.edu/paying-for-college/financial-aid/professional-judgment/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment Professional Judgment refers to the school’s authority to make adjustments, on a case- by-case basis, to information reported on the FAFSA so that the Department of Education can recalculate the Expected Family Contribution (EFC).The purpose of Professional Judgment is to determine an EFC that reflects a family’s current financial situation.”
  - sentence: professional_judgment ⟵ “Professional Judgment Professional Judgment refers to the school’s authority to make adjustments, on a case- by-case basis, to information reported on the FAFSA so that the Department of Education can recalculate the Expected Family Contribution (EFC).The purpose of Professional Judgment is to determine an EFC that reflects a family’s current financial situation.”
### `341376e7d9b5f1c9` Mississippi Gulf Coast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://mgccc.edu/paying-for-college/financial-aid/professional-judgment/ (sha256 dfbdee0b6ab4)
- issues: semantic_review_required, conflicting_sources:https://mgccc.edu/paying-for-college/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: professional_judgment ⟵ “As a result, you may be eligible for a Professional Judgment.”
  - sentence: professional_judgment ⟵ “Professional Judgment refers to the school’s authority to make adjustments, on a case- by-case basis, to information reported on the FAFSA so that the Department of Education can recalculate the Expected Family Contribution (EFC).The purpose of Professional Judgment is to determine an EFC that reflects a family’s current financial situation.”
  - sentence: professional_judgment ⟵ “A Professional Judgment can be requested when a family has experienced any of the following situations: Reduction or loss of income Reduction or loss of nontaxable income Divorce/Separation Death of a parent or spouse Exceptional medical/dental expenses Other unusual circumstances To request a Professional Judgment, you should: Contact the Financial Aid Office on your campus.”
  - sentence: professional_judgment ⟵ “If a Professional Judgment is warranted, we will provide you with the appropriate forms.”
  - sentence: professional_judgment ⟵ “When submitting a Professional Judgment request, be sure to complete all required sections of the form(s) and submit all appropriate documentation as indicated.”
### `7f9858ea0ba786fd` Mississippi Gulf Coast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://mgccc.edu/paying-for-college/financial-aid/satisfactory-academic-progress-sap/ (sha256 9409bb8d718c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Suspension Appeals Students placed on “Financial Aid Suspension” due to extenuating circumstances may appeal this status by completing the Satisfactory Academic Progress Appeal form and submitting supporting documentation and a degree plan.”
  - sentence: sap_appeal ⟵ “SAP Appeals Schedule SAP Appeals that are submitted with supporting documentation and a graduation plan by the deadline(s) will be reviewed by the Financial Aid Appeals Committee prior to the next scheduled payment.”
### `cd4ee21ee06c4422` Mississippi Gulf Coast Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://mgccc.edu/paying-for-college/scholarships/academic-scholarships/ (sha256 f86cd1de4aa4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “To appeal the loss of a scholarship, please complete the Scholarship Appeal Form and provide supporting documentation.”
### `a9a530f075ce426b` Mississippi Gulf Coast Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://mgccc.edu/paying-for-college/tuition/ (sha256 12c1b941fd2a)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees*: 4300 ⟵ “Tuition & Fees* | $4,300 | $4,200 | $4,200 | $2,500”
  - on_campus:Food & Housing: 6258 ⟵ “Food & Housing | $6,258 | $4,240 | $7,800 | $ -”
  - on_campus:Books & Supplies: 1875 ⟵ “Books & Supplies | $1,875 | $1,875 | $1,875 | $1,575”
  - on_campus:Transportation: 2540 ⟵ “Transportation | $2,540 | $4,500 | $4,500 | $2,770”
  - on_campus:Miscellaneous: 1000 ⟵ “Miscellaneous | $1,000 | $1,000 | $1,000 | $ -”
  - on_campus:TOTAL BUDGET: 15973 ⟵ “TOTAL BUDGET | $15,973 | $15,815 | $19,375 | $6,845”
  - with_parents_or_family:Tuition & Fees*: 4200 ⟵ “Tuition & Fees* | $4,300 | $4,200 | $4,200 | $2,500”
  - with_parents_or_family:Food & Housing: 4240 ⟵ “Food & Housing | $6,258 | $4,240 | $7,800 | $ -”
  - with_parents_or_family:Books & Supplies: 1875 ⟵ “Books & Supplies | $1,875 | $1,875 | $1,875 | $1,575”
  - with_parents_or_family:Transportation: 4500 ⟵ “Transportation | $2,540 | $4,500 | $4,500 | $2,770”
  - with_parents_or_family:Miscellaneous: 1000 ⟵ “Miscellaneous | $1,000 | $1,000 | $1,000 | $ -”
  - with_parents_or_family:TOTAL BUDGET: 15815 ⟵ “TOTAL BUDGET | $15,973 | $15,815 | $19,375 | $6,845”
  - off_campus_not_with_family:Tuition & Fees*: 4200 ⟵ “Tuition & Fees* | $4,300 | $4,200 | $4,200 | $2,500”
  - off_campus_not_with_family:Food & Housing: 7800 ⟵ “Food & Housing | $6,258 | $4,240 | $7,800 | $ -”
  - off_campus_not_with_family:Books & Supplies: 1875 ⟵ “Books & Supplies | $1,875 | $1,875 | $1,875 | $1,575”
  - off_campus_not_with_family:Transportation: 4500 ⟵ “Transportation | $2,540 | $4,500 | $4,500 | $2,770”
  - off_campus_not_with_family:Miscellaneous: 1000 ⟵ “Miscellaneous | $1,000 | $1,000 | $1,000 | $ -”
  - off_campus_not_with_family:TOTAL BUDGET: 19375 ⟵ “TOTAL BUDGET | $15,973 | $15,815 | $19,375 | $6,845”
  - column:Tuition & Fees*: 2500 ⟵ “Tuition & Fees* | $4,300 | $4,200 | $4,200 | $2,500”
  - column:Books & Supplies: 1575 ⟵ “Books & Supplies | $1,875 | $1,875 | $1,875 | $1,575”
  - column:Transportation: 2770 ⟵ “Transportation | $2,540 | $4,500 | $4,500 | $2,770”
  - column:TOTAL BUDGET: 6845 ⟵ “TOTAL BUDGET | $15,973 | $15,815 | $19,375 | $6,845”
### `541a41c8ed76f376` Mississippi State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfa.msstate.edu/satisfactory-academic-progress (sha256 3d78ead1e4d2)
- issues: semantic_review_required, conflicting_sources:https://www.sfa.msstate.edu/,https://www.sfa.msstate.edu/important-updates/spring-2027-sap-appeal-information,https://www.sfa.msstate.edu/satisfactory-academic-progress/academic-plan,https://www.sfa.msstate.edu/satisfactory-academic-progress/appeal-information
- checks: {"negative_sentences": 0, "sentences": 14}
  - sentence: sap_appeal ⟵ “If all other eligibility standards are met, eligibility may only be regained through a successful SAP appeal.”
  - sentence: sap_appeal ⟵ “If you lose eligibility because you did not meet this enrollment requirement, you may only regain eligibility by submitting a successful SAP Appeal, provided you meet all other eligibility requirements.”
  - sentence: sap_appeal ⟵ “Students on suspension are no longer eligible to receive financial aid until they meet the required standards or have an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Financial Aid Probation is assigned to students who fail to meet SAP standards at the end of an evaluation period and subsequently receive approval of a SAP appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeal Students who are placed on Financial Aid Suspension for failing to meet SAP requirements may request reinstatement of their financial aid eligibility by submitting a SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “Mississippi State University students are limited to a maximum of three SAP appeals, regardless of whether the appeals are approved or denied.”
### `67fe4f1d47be00cc` Mississippi State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfa.msstate.edu/ (sha256 4ced7fbffe47)
- issues: semantic_review_required, conflicting_sources:https://www.sfa.msstate.edu/important-updates/spring-2027-sap-appeal-information,https://www.sfa.msstate.edu/satisfactory-academic-progress,https://www.sfa.msstate.edu/satisfactory-academic-progress/academic-plan,https://www.sfa.msstate.edu/satisfactory-academic-progress/appeal-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Spring 2027 SAP Appeal Information September 21, 2026 Important Updates: One Big Beautiful Bill Act July 9, 2026 Scholarship and Financial Aid Links MSSTATE Course Catalog University Calendars State Spotlight CONNECT Staff Directory FAQ Undergraduate Admissions Find Student Financial Aid on Facebook Find Student Financial Aid on Instagram Office of Financial Aid and Scholarships P.O.”
### `e1edfd183568273c` Mississippi State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfa.msstate.edu/important-updates/spring-2027-sap-appeal-information (sha256 64d4e1460467)
- issues: semantic_review_required, conflicting_sources:https://www.sfa.msstate.edu/,https://www.sfa.msstate.edu/satisfactory-academic-progress,https://www.sfa.msstate.edu/satisfactory-academic-progress/academic-plan,https://www.sfa.msstate.edu/satisfactory-academic-progress/appeal-information
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: sap_appeal ⟵ “The Spring 2027 SAP Appeal eForm will go live on November 1, 2026 and will be available online through your myState portal.”
  - sentence: sap_appeal ⟵ “Learn How to Submit a SAP Appeal Important Deadlines Priority Deadline: Sunday, November 15, 2026 at 11:59pm.”
  - sentence: sap_appeal ⟵ “Students who submit a complete SAP Appeal by the priority deadline will receive a decision by the first week of classes.”
  - sentence: sap_appeal ⟵ “SAP Appeals submitted after the final deadline will not be accepted.”
  - sentence: sap_appeal ⟵ “Additional Information Incomplete SAP Appeals will not be reviewed.”
  - sentence: sap_appeal ⟵ “Students are limited to three SAP Appeals.”
### `eae955c71347269c` Mississippi State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfa.msstate.edu/satisfactory-academic-progress/appeal-information (sha256 925654d3335d)
- issues: semantic_review_required, conflicting_sources:https://www.sfa.msstate.edu/,https://www.sfa.msstate.edu/important-updates/spring-2027-sap-appeal-information,https://www.sfa.msstate.edu/satisfactory-academic-progress,https://www.sfa.msstate.edu/satisfactory-academic-progress/academic-plan
- checks: {"negative_sentences": 0, "sentences": 33}
  - sentence: sap_appeal ⟵ “A Satisfactory Academic Progress (SAP) Appeal is a request to have your financial aid eligibility reconsidered after you have been placed on Financial Aid Suspension.”
  - sentence: sap_appeal ⟵ “Students may submit a SAP Appeal if extenuating circumstances prevented them from meeting SAP requirements.”
  - sentence: sap_appeal ⟵ “Mississippi State University students are limited to a maximum of three SAP appeals, regardless of whether the appeals are approved or denied.”
  - sentence: sap_appeal ⟵ “You may submit a SAP Appeal if: You are on Financial Aid Suspension Extenuating circumstances prevented you from meeting SAP requirements Those circumstances have been resolved or significantly improved You can demonstrate how you plan to successfully meet SAP requirements moving forward Important: Submitting a SAP Appeal does not guarantee that your financial aid will be reinstated.”
  - sentence: sap_appeal ⟵ “Appeals are reviewed individually by the SAP Appeals Committee.”
  - sentence: sap_appeal ⟵ “The SAP Appeal eForm is only available during the published appeal submission period.”
### `ed9f9bc133dd6c84` Mississippi State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfa.msstate.edu/satisfactory-academic-progress/academic-plan (sha256 9ad86d70520f)
- issues: semantic_review_required, conflicting_sources:https://www.sfa.msstate.edu/,https://www.sfa.msstate.edu/important-updates/spring-2027-sap-appeal-information,https://www.sfa.msstate.edu/satisfactory-academic-progress,https://www.sfa.msstate.edu/satisfactory-academic-progress/appeal-information
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “A SAP Academic Plan is created with your academic advisor after your SAP Appeal has been approved.”
  - sentence: sap_appeal ⟵ “If you do not meet your Academic Plan You will be placed back on Financial Aid Suspension and will not be eligible for additional financial aid until you meet SAP policy requirements or, if eligible, submit and receive approval for another SAP Appeal.”
  - sentence: sap_appeal ⟵ “You may submit another SAP Appeal, provided you have not reached the limit of three appeals.”
  - sentence: sap_appeal ⟵ “Yes, a SAP Appeal is needed each semester unless granted an probationary period in which you must submit a new academic plan.”
### `54d60ff8daccf3b0` Mississippi State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.admissions.msstate.edu/tuition (sha256 5ca9715d8170)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:In-State Tuition & Fees: 11095 ⟵ “In-State Tuition & Fees | $11,095”
  - column:Housing (Median Value): 9990 ⟵ “Housing (Median Value) | $9,990”
  - column:Meal Plan (Weekly 21 Plan): 5210 ⟵ “Meal Plan (Weekly 21 Plan) | $5,210”
  - column:Total for In-State: 26295 ⟵ “Total for In-State | $26,295”
### `a05788f6f70ef479` Mississippi State University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.catalog.msstate.edu/undergraduate/admissionsinformation/financialaid/ (sha256 6e53938e3461)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition and Fees: 10604.0 ⟵ “Tuition and Fees | $10,604.00”
  - column:Books and Supplies: 1200.0 ⟵ “Books and Supplies | $1,200.00”
  - column:Housing and Food: 13514.0 ⟵ “Housing and Food | $13,514.00”
  - column:Personal and Transportation: 6667.0 ⟵ “Personal and Transportation | $6,667.00”
  - column:Total (Mississippi Resident): 31985.0 ⟵ “Total (Mississippi Resident) | $31,985.00”
### `47d022f9988ed54f` Mississippi University for Women — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.muw.edu/admissions/wp-content/uploads/sites/2/2026/05/Financial-Backing-Form-2026-Updated.pdf (sha256 74c5815ef4fc)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 3}
  - column:Tuition and fees for Fall & Spring Semesters (2026 - 2027): 9047 ⟵ “Tuition and fees for Fall & Spring Semesters (2026 - 2027) | $9,047”
  - column:Living Expenses: 13453 ⟵ “Living Expenses | $13,453”
  - column:Insurance and Other Costs: 2500 ⟵ “Insurance and Other Costs | $2,500”
### `f014898b36cc36d6` Mississippi University for Women — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.muw.edu/registrar/students/transfer/exam/ap/ (sha256 d6b864c8acb7)
- issues: ambiguous_year_labels
- checks: {"distinct_exams": 15, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[AP-UNITED-STATES-HISTORY|3 or higher]:  ⟵ “American History | 3 or higher | HIS 109: US History 1877 to present | 3 hours”
  - equivalencies[AP-ART-HISTORY|3 or higher]:  ⟵ “Art History | 3 or higher | ART 212: Art History Survey II | 3 hours”
  - equivalencies[AP-BIOLOGY|3 or higher]:  ⟵ “Biology | 3 or higher | BSB 151: General Biology I andBSB 152: General Biology II | 6 hours*”
  - equivalencies[AP-CALCULUS-AB|3 or higher]:  ⟵ “Calculus AB | 3 or higher | MA 181: Calculus I | 3 hours”
  - equivalencies[AP-CALCULUS-BC|3 or higher]:  ⟵ “Calculus BC | 3 or higher | MA 181: Calculus I andMA 182: Calculus II | 6 hours”
  - equivalencies[AP-CHEMISTRY|3 or higher]:  ⟵ “Chemistry | 3 or higher | PSC 111: General Chemistry I andPSC 112: General Chemistry II | 6 hours*”
  - equivalencies[AP-EUROPEAN-HISTORY|3 or higher]:  ⟵ “European History | 3 or higher | HIS 102: World Civilization 1600 to present | 3 hours”
  - equivalencies[AP-MACROECONOMICS|3 or higher]:  ⟵ “Macroeconomics | 3 or higher | EC 201 – Principles of Economics I | 3 hours”
  - equivalencies[AP-MICROECONOMICS|3 or higher]:  ⟵ “Microeconomics | 3 or higher | EC 202 – Principles of Economics II | 3 hours”
  - equivalencies[AP-MUSIC-THEORY|4 or higher]:  ⟵ “Music Theory | 4 or higher | MUS 101: Music Theory | 3 hours*”
  - equivalencies[AP-PSYCHOLOGY|3 or higher]:  ⟵ “Psychology | 3 or higher | PSY 101: General Psychology | 3 hours”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|5 or higher]:  ⟵ “Spanish Lang | 5 or higher | FLS 101: Spanish I andFLS 102: Spanish II | 8 hours”
  - equivalencies[AP-STATISTICS|3 or higher]:  ⟵ “Statistics | 3 or higher | MA 123: Statistics | 3 hours”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3 or higher]:  ⟵ “US Government and Politics | 3 or higher | POL 150: American Government | 3 hours”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3 or higher]:  ⟵ “World History | 3 or higher | HIS 102: World Civilization 1600 to present | 3 hours”
### `1384b138772a5427` Mississippi Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mvsu.edu/sites/default/files/SAP%20Appeal%20Form-1.pdf (sha256 d307f20515b4)
- issues: semantic_review_required, conflicting_sources:https://www.mvsu.edu/financial-aid-programs/sap-standard-satisfactory-academic-progress,https://www.mvsu.edu/sites/default/files/SAP_Graduate_Policy-Final2.pdf,https://www.mvsu.edu/sites/default/files/SAP_Undergraduate_Policy-Final2.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Office of Student Financial Aid Telephone: (662) 254-3335 14000 HWY 82W, MVSU 7268 Fax: (662) 254-7900 Itta Bena, MS 38941 Website: www.mvsu.edu Email: mvsufinaid@mvsu.edu Satisfactory Academic Progression Appeal Application (SAP) Instructions: Please complete this form to appeal your Financial Aid Suspension. (1) COMPLETE, type all information in the space provided, (2) PRINT Application (3) MEET”
### `7633b333e498c855` Mississippi Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mvsu.edu/sites/default/files/SAP_Graduate_Policy-Final2.pdf (sha256 15e6a46041b6)
- issues: semantic_review_required, conflicting_sources:https://www.mvsu.edu/financial-aid-programs/sap-standard-satisfactory-academic-progress,https://www.mvsu.edu/sites/default/files/SAP%20Appeal%20Form-1.pdf,https://www.mvsu.edu/sites/default/files/SAP_Undergraduate_Policy-Final2.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Appeal Procedures Students who fail to maintain Satisfactory Academic Progress (SAP) and have been placed on financial aid suspension may submit an appeal due to mitigating circumstances for reinstatement of aid.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Applications received after the first day of class, will not be accepted.”
  - sentence: sap_appeal ⟵ “SAP Appeal Applications without supporting documentation will be deemed incomplete.”
  - sentence: sap_appeal ⟵ “SAP Appeal Decisions Reinstatement of Financial Aid will be based on the depth of the appeal statement, documentation received, and the academic record.”
### `9249c3e1d038bcf2` Mississippi Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mvsu.edu/financial-aid-programs/sap-standard-satisfactory-academic-progress (sha256 433f6fa73103)
- issues: semantic_review_required, conflicting_sources:https://www.mvsu.edu/sites/default/files/SAP%20Appeal%20Form-1.pdf,https://www.mvsu.edu/sites/default/files/SAP_Graduate_Policy-Final2.pdf,https://www.mvsu.edu/sites/default/files/SAP_Undergraduate_Policy-Final2.pdf
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “SAP Undergraduate Policy | SAP Graduate Policy | SAP Appeal Application MISSISSIPPI VALLEY STATE UNIVERSITY OFFICE OF STUDENT FINANCIAL AID SATISFACTORY ACADEMIC PROGRESS APPEAL INSTRUCTIONS Mississippi Valley State University, as required by federal regulations, annually monitors minimum standards of Satisfactory Academic Progress (SAP) as it relates to your eligibility to receive federal student”
  - sentence: sap_appeal ⟵ “Appeal Procedures Students who fail to maintain Satisfactory Academic Progress (SAP) and have been placed on financial aid suspension may submit an appeal due to mitigating circumstances for reinstatement of aid.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Applications received after the first day of class, will not be accepted.”
  - sentence: sap_appeal ⟵ “SAP Appeal Applications without supporting documentation will be deemed incomplete.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeals Committee will render a decision to the student by telephone and/or written notification.”
  - sentence: sap_appeal ⟵ “SAP Appeal Decision Reinstatement of Financial Aid will be based on the depth of the appeal statement, documentation received, and the academic record.”
### `bd5de0c0c5ab6b1a` Mississippi Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mvsu.edu/sites/default/files/SAP_Undergraduate_Policy-Final2.pdf (sha256 053eec4d5408)
- issues: semantic_review_required, conflicting_sources:https://www.mvsu.edu/financial-aid-programs/sap-standard-satisfactory-academic-progress,https://www.mvsu.edu/sites/default/files/SAP%20Appeal%20Form-1.pdf,https://www.mvsu.edu/sites/default/files/SAP_Graduate_Policy-Final2.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Appeal Procedures Students who fail to maintain Satisfactory Academic Progress (SAP) and have been placed on financial aid suspension may submit an appeal due to mitigating circumstances for reinstatement of aid.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Applications received after the first day of class, will not be accepted.”
  - sentence: sap_appeal ⟵ “SAP Appeal Applications without supporting documentation will be deemed incomplete.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeals Committee will render a decision to the student by telephone and/or written notification.”
  - sentence: sap_appeal ⟵ “SAP Appeal Decision Reinstatement of Financial Aid will be based on the depth of the appeal statement, documentation received, and the academic record.”
  - sentence: sap_appeal ⟵ “Academic Plan If your Satisfactory Academic Progress Appeal Application is approved with the stipulation that you meet with your Academic Advisor to discuss and develop an Academic Plan, it is the expectation that you adhere to all conditions outlined in your Academic Plan to ensure you meet the university standards for satisfactory academic progress.”
### `d0447addac375a36` Mississippi Valley State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mvsu.edu/sites/default/files/SAP%20Appeal%20Form-1.pdf (sha256 d307f20515b4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Provide a detailed explanation of the special circumstances that prevented you from maintaining satisfactory academic progress.”
  - sentence: need_based_special_circumstances ⟵ “You must include specific dates as to when your special circumstance occurred.”
### `ae38051210732a0b` Mississippi Valley State University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.mvsu.edu/cost-attendance (sha256 6b19623985be)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Activity Fee: 20.0 ⟵ “Activity Fee | $20.00”
  - column:Books and Supplies: 2400.0 ⟵ “Books and Supplies | $2,400.00”
  - column:Personal Expenses: 1195.0 ⟵ “Personal Expenses | $1,195.00”
  - column:Room and Board: 9342.0 ⟵ “Room and Board | $9,342.00”
  - column:Direct Loan Fees: 130.0 ⟵ “Direct Loan Fees | $130.00”
  - column:Tuition and Fees: 7474.0 ⟵ “Tuition and Fees | $7,474.00”
  - column:Transportation: 1185.0 ⟵ “Transportation | $1,185.00”
  - column:TOTAL: 21746.0 ⟵ “TOTAL | $21,746.00”
### `de2f7cef77c6139b` Northwest Mississippi Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.northwestms.edu/financial-aid/scholarships (sha256 0a8c7f5fe9bc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances for less than 3 hours will be considered on a case by case basis.”
### `0da76fd6ff13789a` Northwest Mississippi Community College — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.northwestms.edu/financial-aid/coa (sha256 27685b235dac)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 7080 ⟵ “Tuition and Fees | $4,780 | $7,080”
  - column:Books and Supplies: 2250 ⟵ “Books and Supplies | $2,250 | $2,250”
  - column:Housing: 6510 ⟵ “Housing | $4,600 | $6,510”
  - column:Travel: 2650 ⟵ “Travel | $2,000 | $2,650”
  - column:Misc and Personal: 2015 ⟵ “Misc and Personal | $1,615 | $2,015”
  - column:Total: 20505 ⟵ “Total | $15,245 | $20,505”
### `d78a093112279332` Northwest Mississippi Community College — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.northwestms.edu/financial-aid/coa (sha256 27685b235dac)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and Fees: 4780 ⟵ “Tuition and Fees | $4,780 | $7,080”
  - column:Books and Supplies: 2250 ⟵ “Books and Supplies | $2,250 | $2,250”
  - column:Housing: 4600 ⟵ “Housing | $4,600 | $6,510”
  - column:Travel: 2000 ⟵ “Travel | $2,000 | $2,650”
  - column:Misc and Personal: 1615 ⟵ “Misc and Personal | $1,615 | $2,015”
  - column:Total: 15245 ⟵ “Total | $15,245 | $20,505”
### `18930854dc75b358` Pearl River Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://prcc.edu/financial-aid/special-circumstances/ (sha256 bd272489326b)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://prcc.edu/financial-aid/satisfactory-academic-progress-requirements/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You are encouraged to submit a Financial Aid SAP Appeal to request reinstatement of your eligibility, which is a different process.”
  - sentence: sap_appeal ⟵ “You can find the SAP Appeal form in your RiverGuide account – click on the Financial Aid tile.”
### `cf4a78c07ef1d843` Pearl River Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://prcc.edu/financial-aid/special-circumstances/ (sha256 bd272489326b)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “The following are special circumstances that we can take into consideration and possibly recalculate your federal aid eligibility: • Loss of employment • Reduction of income • Loss of untaxed income or benefit • Recent separation or divorce • Death of a spouse or parent • Unusual medical/dental expenses paid out of pocket (must exceed 11% of income, not paid by insurance) Please note: if you have ”
  - sentence: need_based_special_circumstances ⟵ “If you would like to submit a request for a special circumstances review, please submit the following form to our office, along with all of the required documentation outlined on the document.”
  - sentence: need_based_special_circumstances ⟵ “Request for Special Circumstances Review – 2024-2025 year Request for Special Circumstances Review – 2025-2026 year If you have questions regarding this process, please visit our office or contact us at finaid@prcc.edu.”
### `e330339c2b5c1e9c` Pearl River Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://prcc.edu/financial-aid/satisfactory-academic-progress-requirements/ (sha256 8294828c9146)
- issues: semantic_review_required, conflicting_sources:https://prcc.edu/financial-aid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Reinstatement of Eligibility and Appeal Procedures Students who lose their eligibility for federal assistance for not meeting Satisfactory Academic Progress requirements have the right to appeal their suspension in accordance with federal regulations and under the policies established by the educational institution they are attending.”
### `c4ed8493ecb39b15` Pearl River Community College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://prcc.edu/future-wildcats/admissions/tuition-and-fees/ (sha256 88af1687215f)
- issues: ambiguous_year_labels
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 3700.0 ⟵ “Tuition | $3,700.00 | $3,700.00 | $3,700.00”
  - on_campus:Fees: 250.0 ⟵ “Fees | $250.00 | $250.00 | $250.00”
  - on_campus:Living Expenses (Housing/Food): 5902.0 ⟵ “Living Expenses (Housing/Food) | $5,902.00 |  | ”
  - on_campus:Books/Supplies: 1350.0 ⟵ “Books/Supplies | $1,350.00 | $1,350.00 | $1,350.00”
  - on_campus:Transportation: 1160.0 ⟵ “Transportation | $1,160.00 | $4,640.00 | $4,640.00”
  - on_campus:Miscellaneous: 2994.0 ⟵ “Miscellaneous | $2,994.00 | $2,994.00 | $2,994.00”
  - on_campus:Total: 15356.0 ⟵ “Total | $15,356.00 | $19,420.00 | $26,716.00”
  - with_parents_or_family:Tuition: 3700.0 ⟵ “Tuition | $3,700.00 | $3,700.00 | $3,700.00”
  - with_parents_or_family:Fees: 250.0 ⟵ “Fees | $250.00 | $250.00 | $250.00”
  - with_parents_or_family:Living Expenses (Housing/Food): 6486.0 ⟵ “Living Expenses (Housing/Food) |  | $6,486.00 | $13,782.00”
  - with_parents_or_family:Books/Supplies: 1350.0 ⟵ “Books/Supplies | $1,350.00 | $1,350.00 | $1,350.00”
  - with_parents_or_family:Transportation: 4640.0 ⟵ “Transportation | $1,160.00 | $4,640.00 | $4,640.00”
  - with_parents_or_family:Miscellaneous: 2994.0 ⟵ “Miscellaneous | $2,994.00 | $2,994.00 | $2,994.00”
  - with_parents_or_family:Total: 19420.0 ⟵ “Total | $15,356.00 | $19,420.00 | $26,716.00”
  - off_campus_not_with_family:Tuition: 3700.0 ⟵ “Tuition | $3,700.00 | $3,700.00 | $3,700.00”
  - off_campus_not_with_family:Fees: 250.0 ⟵ “Fees | $250.00 | $250.00 | $250.00”
  - off_campus_not_with_family:Living Expenses (Housing/Food): 13782.0 ⟵ “Living Expenses (Housing/Food) |  | $6,486.00 | $13,782.00”
  - off_campus_not_with_family:Books/Supplies: 1350.0 ⟵ “Books/Supplies | $1,350.00 | $1,350.00 | $1,350.00”
  - off_campus_not_with_family:Transportation: 4640.0 ⟵ “Transportation | $1,160.00 | $4,640.00 | $4,640.00”
  - off_campus_not_with_family:Miscellaneous: 2994.0 ⟵ “Miscellaneous | $2,994.00 | $2,994.00 | $2,994.00”
  - off_campus_not_with_family:Total: 26716.0 ⟵ “Total | $15,356.00 | $19,420.00 | $26,716.00”
### `673804cda862866e` Pearl River Community College — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://prcc.edu/academics/dual-enrollment/tuition-and-fees/ (sha256 7bf24c7c9051)
- issues: stale_year_label:2024-25
- checks: {"fields": ["college_gpa_to_continue", "per_credit_hour_charges"], "tiers": 1}
  - per_credit_hour_charge: 65 ⟵ “$65 per credit hour; No additional charge for etext/textbooks/materials”
  - per_credit_hour_charge: 65 ⟵ “$65 per credit hour plus etext/textbook/course materials fees”
  - per_credit_hour_charge: 65 ⟵ “First Semester Fee: $65 per credit hour; No additional charges for etext/textbooks/materials”
  - college_gpa_to_continue: 3.0 ⟵ “Recipients of Presidential, Valedictorian/Salutatorian, Vice-Presidential and Full-Tuition Career/Technical scholarships are required to maintain a 3.0 GPA each semester at PRCC to keep scholarship eligibility.”
  - eligibility_tier: 2.5 ⟵ “Recipients of Honors, Scholastic Excellence, Half-Tuition Career/Technical, and all other institutional scholarships are required2.5 GPA each semester at PRCC to keep scholarship eligibility.”
### `32e5ed699fe09f73` Southwest Mississippi Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.smcc.edu/financial-aid/ (sha256 1a6b84499289)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Call Now Helpful Information Reinstatement of Eligibility Students who have been placed on suspension for GPA or Completion Rate have the ability to appeal their Satisfactory Academic Progress standing by submitting an appeal along with supporting documentation.”
### `4a6e11993e7d5822` Southwest Mississippi Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.smcc.edu/financial-aid/ (sha256 1a6b84499289)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.smcc.edu/wp-content/uploads/2026-2027-Provisional-Independent-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special and/or Unusual Circumstances Enrollment Intensity & Eligibility Changes were made to the Free Application for Federal Student Aid (FAFSA) for the 2024-2025 aid year!”
### `5166504cb5dbe9f5` Southwest Mississippi Community College — appeals 2025-26 [new] (labeled_in_url)
- source: https://www.smcc.edu/wp-content/uploads/2025-2026-Satisfactory-Academic-Progress-Appeal.pdf (sha256 4eaac820b00e)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.smcc.edu/wp-content/uploads/2025-2026-Max-Credit-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL Mail to: SMCC Financial Aid, 1156 College Drive, Summit, MS 39666 or Fax to: 601-276-3888.”
### `5effff600f53bf8e` Southwest Mississippi Community College — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.smcc.edu/wp-content/uploads/2025-2026-Provisional-Independent-Appeal.pdf (sha256 75710439c730)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “However, a student may have unusual circumstances that require consideration for independent status.”
  - sentence: need_based_special_circumstances ⟵ “A signed, detailed letter from you, the student explaining a. the unusual circumstances, b. your relationship with your biological parents, c. explanation of where you expect to receive your financial support for the next school year. 2.”
### `64904db94eeb4b77` Southwest Mississippi Community College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.smcc.edu/wp-content/uploads/2026-2027-Provisional-Independent-Appeal.pdf (sha256 26f050666403)
- issues: semantic_review_required, conflicting_sources:https://www.smcc.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “However, a student may have unusual circumstances that require consideration for independent status.”
  - sentence: need_based_special_circumstances ⟵ “A signed, detailed letter from you, the student explaining a. the unusual circumstances, b. your relationship with your biological parents, c. explanation of where you expect to receive your financial support for the next school year. 2.”
### `a59ce41d00572ae7` Southwest Mississippi Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.smcc.edu/financial-aid/ (sha256 1a6b84499289)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “The FAFSA Simplification Act allows financial aid administrators added flexibility to make adjustments to a student’s FAFSA based on a student and/or family’s financial circumstance. this process is known as professional judgment and can extend to declared disasters, emergencies, or economic downturns.”
  - sentence: professional_judgment ⟵ “Please contact your Financial Aid counselor if you believe you may qualify for Professional Judgement consideration.”
### `de77bb5292bd4eff` Southwest Mississippi Community College — appeals 2025-26 [new] (labeled_in_url)
- source: https://www.smcc.edu/wp-content/uploads/2025-2026-Max-Credit-Appeal.pdf (sha256 b4e1578f0815)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.smcc.edu/wp-content/uploads/2025-2026-Satisfactory-Academic-Progress-Appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS EXCEEDS MAXIMUM CREDITS APPEAL *To be eligible you must have changed academic programs and be on track to graduate.”
### `c14d629874444b08` Southwest Mississippi Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.smcc.edu/wp-content/uploads/Tuition-and-Fees-2026-27-including-Policy.pdf (sha256 9b9bdf6f12ee)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 7}
  - column:Tuition: 1850 ⟵ “Tuition | $1,850”
  - column:Out-of-State Tuition: 1350 ⟵ “Out-of-State Tuition | $1,350”
  - column:Course Materials (E-Books): 250 ⟵ “Course Materials (E-Books) | $250”
  - column:Student Services Fee: 180 ⟵ “Student Services Fee | $180”
  - column:Technology Fee: 180 ⟵ “Technology Fee | $180”
  - column:Course Materials (E-Books) (2): 150 ⟵ “Course Materials (E-Books) | $150”
  - column:Vocational Course Lab Fee: 100 ⟵ “Vocational Course Lab Fee | $100”
### `91d65604d4a972b6` Tougaloo College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tougaloo.edu/admissions/office-student-financial-aid/documents-and-forms (sha256 24b9b9dd58d7)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Form 4 - Dependent Verification Worksheet Form 5 - Independent Verification Worksheet Form 6 - Student Statement of Income Form 7 - Parent Statement of Income Academic Progress Forms Forms related to Satisfactory Academic Progress (SAP) appeals and academic plans.”
### `07607c35b671d077` Tougaloo College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tougaloo.edu/estimated-costs (sha256 c107820115d7)
- issues: arrangement_unlabeled, conflicting_sources:https://www.tougaloo.edu/bursar/tuition-and-cost,https://www.tougaloo.edu/sites/default/files/2026-04/TUITION%20AND%20FEES%20SCHEDULE%2026-27.pdf
- checks: {"columns": 5, "rows": 5}
  - with_parents_or_family:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - with_parents_or_family:General Fees: 371.0 ⟵ “General Fees | $371.00 | $371.00 | $371.00 | $371.00 | $371.00”
  - with_parents_or_family:Commuter Fees: 150.0 ⟵ “Commuter Fees | $150.00 | -0- | -0- | -0- | -0-”
  - with_parents_or_family:SEMESTER TOTAL: 6464.0 ⟵ “SEMESTER TOTAL | $6,464.00 | $11,281.00 | $13,021.00 | $11,942.00 | $12,691.00”
  - with_parents_or_family:ANNUAL TOTAL: 12928.0 ⟵ “ANNUAL TOTAL | $12,928.00 | $22,562.00 | $26,042.00 | $23,884.00 | $25,382.00”
  - column:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - column:Room: 1740.0 ⟵ “Room | -0- | $1,740.00 | $3,480.00 | $2,401.00 | $3,150.00”
  - column:Board**: 2844.0 ⟵ “Board** | -0- | $2,844.00 | $2,844.00 | $2,844.00 | $2,844.00”
  - column:General Fees: 371.0 ⟵ “General Fees | $371.00 | $371.00 | $371.00 | $371.00 | $371.00”
  - column:Residential Fees: 383.0 ⟵ “Residential Fees | -0- | $383.00 | $383.00 | $383.00 | $383.00”
  - column:SEMESTER TOTAL: 11281.0 ⟵ “SEMESTER TOTAL | $6,464.00 | $11,281.00 | $13,021.00 | $11,942.00 | $12,691.00”
  - column:ANNUAL TOTAL: 22562.0 ⟵ “ANNUAL TOTAL | $12,928.00 | $22,562.00 | $26,042.00 | $23,884.00 | $25,382.00”
  - column:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - column:Room: 3480.0 ⟵ “Room | -0- | $1,740.00 | $3,480.00 | $2,401.00 | $3,150.00”
  - column:Board**: 2844.0 ⟵ “Board** | -0- | $2,844.00 | $2,844.00 | $2,844.00 | $2,844.00”
  - column:General Fees: 371.0 ⟵ “General Fees | $371.00 | $371.00 | $371.00 | $371.00 | $371.00”
  - column:Residential Fees: 383.0 ⟵ “Residential Fees | -0- | $383.00 | $383.00 | $383.00 | $383.00”
  - column:SEMESTER TOTAL: 13021.0 ⟵ “SEMESTER TOTAL | $6,464.00 | $11,281.00 | $13,021.00 | $11,942.00 | $12,691.00”
  - column:ANNUAL TOTAL: 26042.0 ⟵ “ANNUAL TOTAL | $12,928.00 | $22,562.00 | $26,042.00 | $23,884.00 | $25,382.00”
  - column:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - column:Room: 2401.0 ⟵ “Room | -0- | $1,740.00 | $3,480.00 | $2,401.00 | $3,150.00”
  - column:Board**: 2844.0 ⟵ “Board** | -0- | $2,844.00 | $2,844.00 | $2,844.00 | $2,844.00”
  - column:General Fees: 371.0 ⟵ “General Fees | $371.00 | $371.00 | $371.00 | $371.00 | $371.00”
  - column:Residential Fees: 383.0 ⟵ “Residential Fees | -0- | $383.00 | $383.00 | $383.00 | $383.00”
  - column:SEMESTER TOTAL: 11942.0 ⟵ “SEMESTER TOTAL | $6,464.00 | $11,281.00 | $13,021.00 | $11,942.00 | $12,691.00”
  - … 8 more rows
### `09bb67b293843ea0` Tougaloo College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tougaloo.edu/sites/default/files/2026-04/TUITION%20AND%20FEES%20SCHEDULE%2026-27.pdf (sha256 55dc8595d790)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.tougaloo.edu/bursar/tuition-and-cost,https://www.tougaloo.edu/estimated-costs
- checks: {"columns": 4, "components_reconcile": false, "rows": 18}
  - column:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - column:General Fees: 521.0 ⟵ “General Fees | $521.00 | $521.00 | $521.00 | $521.00”
  - column:TOTAL:: 6464.0 ⟵ “TOTAL: | $6,464.00 | $12,691.00 | $13,021.00 | $12,691.00”
  - column:ANNUAL TOTAL $12,928.00: 25382.0 ⟵ “ANNUAL TOTAL $12,928.00 | $25,382.00 | $26,042.00 | $25,382.00”
  - column:0-3: 1041.0 ⟵ “0-3 | $1,041.00 | $521.00 | $1,562.00”
  - column:4: 1388.0 ⟵ “4 | $1,388.00 | $521.00 | $1,909.00”
  - column:5: 1735.0 ⟵ “5 | $1,735.00 | $521.00 | $2,256.00”
  - column:6: 2082.0 ⟵ “6 | $2,082.00 | $521.00 | $2,603.00”
  - column:7: 2429.0 ⟵ “7 | $2,429.00 | $521.00 | $2,950.00”
  - column:8: 2776.0 ⟵ “8 | $2,776.00 | $521.00 | $3,297.00”
  - column:9: 3123.0 ⟵ “9 | $3,123.00 | $521.00 | $3,644.00”
  - column:10: 3470.0 ⟵ “10 | $3,470.00 | $521.00 | $3,991.00”
  - column:11: 3817.0 ⟵ “11 | $3,817.00 | $521.00 | $4,338.00”
  - column:12-18: 4164.0 ⟵ “12-18 | $4,164.00 | $521.00 | $4,685.00”
  - column:General Fee:: 521.0 ⟵ “General Fee: | $521.00 | Grad Rate Per Credit Hour: $644.00”
  - column:General Fee: (2): 195.0 ⟵ “General Fee: | $195.00”
  - column:Technology Fee:: 184.0 ⟵ “Technology Fee: | $184.00”
  - column:Room:: 1268.0 ⟵ “Room: | $1,268.00”
  - column:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - column:Room: 3383.0 ⟵ “Room | -0- | $3,383.00 | $3,713.00 | $3,383.00”
  - column:Meal Plan*: 2844.0 ⟵ “Meal Plan* | -0- | $2,844.00 | $2,844.00 | $2,844.00”
  - column:General Fees: 521.0 ⟵ “General Fees | $521.00 | $521.00 | $521.00 | $521.00”
  - column:TOTAL:: 12691.0 ⟵ “TOTAL: | $6,464.00 | $12,691.00 | $13,021.00 | $12,691.00”
  - column:ANNUAL TOTAL $12,928.00: 26042.0 ⟵ “ANNUAL TOTAL $12,928.00 | $25,382.00 | $26,042.00 | $25,382.00”
  - column:0-3: 521.0 ⟵ “0-3 | $1,041.00 | $521.00 | $1,562.00”
  - … 30 more rows
### `e266c16452fb0310` Tougaloo College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tougaloo.edu/bursar/tuition-and-cost (sha256 e79eaa303ad6)
- issues: arrangement_unlabeled, conflicting_sources:https://www.tougaloo.edu/estimated-costs,https://www.tougaloo.edu/sites/default/files/2026-04/TUITION%20AND%20FEES%20SCHEDULE%2026-27.pdf
- checks: {"columns": 5, "rows": 5}
  - with_parents_or_family:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - with_parents_or_family:General Fees: 371.0 ⟵ “General Fees | $371.00 | $371.00 | $371.00 | $371.00 | $371.00”
  - with_parents_or_family:Commuter Fees: 150.0 ⟵ “Commuter Fees | $150.00 | -0- | -0- | -0- | -0-”
  - with_parents_or_family:SEMESTER TOTAL: 6464.0 ⟵ “SEMESTER TOTAL | $6,464.00 | $11,281.00 | $13,021.00 | $11,942.00 | $12,691.00”
  - with_parents_or_family:ANNUAL TOTAL: 12928.0 ⟵ “ANNUAL TOTAL | $12,928.00 | $22,562.00 | $26,042.00 | $23,884.00 | $25,382.00”
  - column:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - column:Room: 1740.0 ⟵ “Room | -0- | $1,740.00 | $3,480.00 | $2,401.00 | $3,150.00”
  - column:Board**: 2844.0 ⟵ “Board** | -0- | $2,844.00 | $2,844.00 | $2,844.00 | $2,844.00”
  - column:General Fees: 371.0 ⟵ “General Fees | $371.00 | $371.00 | $371.00 | $371.00 | $371.00”
  - column:Residential Fees: 383.0 ⟵ “Residential Fees | -0- | $383.00 | $383.00 | $383.00 | $383.00”
  - column:SEMESTER TOTAL: 11281.0 ⟵ “SEMESTER TOTAL | $6,464.00 | $11,281.00 | $13,021.00 | $11,942.00 | $12,691.00”
  - column:ANNUAL TOTAL: 22562.0 ⟵ “ANNUAL TOTAL | $12,928.00 | $22,562.00 | $26,042.00 | $23,884.00 | $25,382.00”
  - column:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - column:Room: 3480.0 ⟵ “Room | -0- | $1,740.00 | $3,480.00 | $2,401.00 | $3,150.00”
  - column:Board**: 2844.0 ⟵ “Board** | -0- | $2,844.00 | $2,844.00 | $2,844.00 | $2,844.00”
  - column:General Fees: 371.0 ⟵ “General Fees | $371.00 | $371.00 | $371.00 | $371.00 | $371.00”
  - column:Residential Fees: 383.0 ⟵ “Residential Fees | -0- | $383.00 | $383.00 | $383.00 | $383.00”
  - column:SEMESTER TOTAL: 13021.0 ⟵ “SEMESTER TOTAL | $6,464.00 | $11,281.00 | $13,021.00 | $11,942.00 | $12,691.00”
  - column:ANNUAL TOTAL: 26042.0 ⟵ “ANNUAL TOTAL | $12,928.00 | $22,562.00 | $26,042.00 | $23,884.00 | $25,382.00”
  - column:Tuition: 5943.0 ⟵ “Tuition | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00 | $5,943.00”
  - column:Room: 2401.0 ⟵ “Room | -0- | $1,740.00 | $3,480.00 | $2,401.00 | $3,150.00”
  - column:Board**: 2844.0 ⟵ “Board** | -0- | $2,844.00 | $2,844.00 | $2,844.00 | $2,844.00”
  - column:General Fees: 371.0 ⟵ “General Fees | $371.00 | $371.00 | $371.00 | $371.00 | $371.00”
  - column:Residential Fees: 383.0 ⟵ “Residential Fees | -0- | $383.00 | $383.00 | $383.00 | $383.00”
  - column:SEMESTER TOTAL: 11942.0 ⟵ “SEMESTER TOTAL | $6,464.00 | $11,281.00 | $13,021.00 | $11,942.00 | $12,691.00”
  - … 8 more rows
### `4d05e3838da7e336` University of Mississippi — appeals 2026-27 [new] (source_unlabeled)
- source: https://olemiss.edu/finaid/info/professional-judgment/ (sha256 713d689045c6)
- issues: semantic_review_required, conflicting_sources:https://olemiss.edu/admissions/undergraduate-admissions/,https://olemiss.edu/admissions/undergraduate-admissions/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Active Duty Status Emancipated Minor Homeless or Risk of Being Homeless Legal Guardianship Orphan, Ward of the Court or Foster Care Proof of Legal Dependents Veteran Status Special and Unusual Circumstances Students can appeal for re-evaluation of aid eligibility due to loss of income or benefits, extraordinary medical or dental expenses, K-12 school tuition for a sibling, parent’s marital status ”
  - sentence: need_based_special_circumstances ⟵ “Students also have the ability to appeal their dependency status due to unusual circumstances regarding their relationship with their parents, or request Federal Direct Unsubsidized Loans due to a parent’s refusal to complete the parent section on the FAFSA.”
### `6aa6d74b36852774` University of Mississippi — appeals 2026-27 [new] (source_unlabeled)
- source: https://olemiss.edu/admissions/undergraduate-admissions/financial-aid/ (sha256 92f6879e7369)
- issues: semantic_review_required, conflicting_sources:https://olemiss.edu/admissions/undergraduate-admissions/,https://olemiss.edu/finaid/info/professional-judgment/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Apply Now Home Admissions Undergraduate Admissions Financial Aid More in Financial Aid Undergraduate Admissions Financial Aid Types of Aid Applying for Aid Application Process International Students Transfer Students Special Circumstances Undergraduate Admissions If you are an entering Freshman An education from the University of Mississippi is an exceptional investment in your future.”
### `b890fdd5c4395e26` University of Mississippi — appeals 2026-27 [new] (source_unlabeled)
- source: https://olemiss.edu/admissions/undergraduate-admissions/ (sha256 5c3a98a06d1e)
- issues: semantic_review_required, conflicting_sources:https://olemiss.edu/admissions/undergraduate-admissions/financial-aid/,https://olemiss.edu/finaid/info/professional-judgment/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Non-Accredited High Schools Applicants who have completed high school from a school that does not hold regional accreditation must submit the following: Transcripts reflecting academic performance or a secondary school leaving form; and ACT or SAT scores and GPA based on Mississippi admission requirements.”
### `c0939f18578f6fe6` University of Mississippi — appeals 2026-27 [new] (source_unlabeled)
- source: https://olemiss.edu/finaid/info/financial-aid-appeals/ (sha256 e8459de8ca96)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Read the Satisfactory Academic Progress Policy Home Departmental Directory Office of Financial Aid Financial Aid Appeals Types of Financial Aid Appeals Students may appeal the status of their financial aid and or scholarships in the event of an injury or illness, the death of a relative or other special circumstances.”
### `fdfad35ef69b21f5` University of Mississippi — appeals 2026-27 [new] (source_unlabeled)
- source: https://olemiss.edu/finaid/info/professional-judgment/ (sha256 713d689045c6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Professional Judgment | Ole Miss Skip to main site navigation Skip to main content Give Search Academics Program Listing Colleges and Schools Competitive Programs Faculty Study Abroad Academic Resources and Support Admissions Why the University of Mississippi?”
  - sentence: professional_judgment ⟵ “Home Departmental Directory Office of Financial Aid Professional Judgment What is a Professional Judgment?”
  - sentence: professional_judgment ⟵ “A professional judgment is a financial aid professional’s ability to review a student’s file on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “Conditions that may merit the use of Professional Judgment Cost of Attendance Increase Requests There may be times that students have educational costs that are significantly higher than the school’s standard Cost of Attendance (COA), or are not otherwise accounted for in the budget allowances.”
### `4762be8eb31a9eca` University of Southern Mississippi — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.usm.edu/financial-aid/additional-sap-policies.php (sha256 a33aa1a9de9e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other unusual circumstances that may affect a student's ability to meet satisfactory academic progress standards.”
### `879dfdd41baff428` University of Southern Mississippi — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.usm.edu/scholarships-financial-wellness/scholarship_appeals/appeal_instructions.php (sha256 93084bd6f6aa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Under "Scholarship Appeal Option," click the dropdown menu and select "Loss of Scholarship." Step 3: Check the "I Agree" Boxes You will see four acknowledgment statements that you must agree to before proceeding.”
### `00d6537cd17b3ca6` University of Southern Mississippi — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.usm.edu/financial-aid/cost-attendance-previous-year.php (sha256 3c41be776769)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 11998 ⟵ “Tuition | $9,998 | $11,998”
  - on_campus:Transportation: 1328 ⟵ “Transportation | $1,328 | $1,328”
  - on_campus:Housing & Meals: 11920 ⟵ “Housing & Meals | $11,920 | $11,920”
  - on_campus:Personal Expenses: 3304 ⟵ “Personal Expenses | $3,304 | $3,304”
  - on_campus:Fees: 458 ⟵ “Fees | $458 | $458”
  - on_campus:Books/Supplies: 852 ⟵ “Books/Supplies | $852 | $852”
  - on_campus:TOTAL: 29860 ⟵ “TOTAL | $27,860 | $29,860”
### `3b7712e903be2bae` University of Southern Mississippi — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/freshmen.php (sha256 6d202fa71cbc)
- issues: residency_unknown, conflicting_sources:https://www.usm.edu/financial-aid/cost-attendance-summer.php,https://www.usm.edu/undergraduate-admissions/costs-scholarships.php
- checks: {"columns": 1, "rows": 2}
  - column:Resident Tuition*: 10794 ⟵ “Resident Tuition* | $5,397 | $10,794”
  - column:Non-Resident Tuition**: 12794 ⟵ “Non-Resident Tuition** | $6,397 | $12,794”
### `4410c121c94e3d52` University of Southern Mississippi — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.usm.edu/undergraduate-admissions/costs-scholarships.php (sha256 d632dbf6a703)
- issues: residency_unknown, conflicting_sources:https://www.usm.edu/financial-aid/cost-attendance-summer.php,https://www.usm.edu/undergraduate-admissions/freshmen.php
- checks: {"columns": 1, "rows": 2}
  - column:Resident Tuition*: 10794 ⟵ “Resident Tuition* | $5,397 | $10,794”
  - column:Non-Resident Tuition**: 12794 ⟵ “Non-Resident Tuition** | $6,397 | $12,794”
### `6da678af4f50aaa4` University of Southern Mississippi — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.usm.edu/financial-aid/cost-of-attendance-current-year.php (sha256 836324ca38ee)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 10394 ⟵ “Tuition | $10,394 | $12,394”
  - on_campus:Transportation: 1300 ⟵ “Transportation | $1,300 | $1,300”
  - on_campus:Housing & Meals: 12278 ⟵ “Housing & Meals | $12,278 | $12,278”
  - on_campus:Personal Expenses: 3344 ⟵ “Personal Expenses | $3,344 | $3,344”
  - on_campus:Misc Fees: 610 ⟵ “Misc Fees | $610 | $610”
  - on_campus:Books/Supplies: 860 ⟵ “Books/Supplies | $860 | $860”
  - on_campus:TOTAL: 28786 ⟵ “TOTAL | $28,786 | $30,786”
### `86cbe5f440026969` University of Southern Mississippi — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usm.edu/financial-aid/cost-attendance-summer.php (sha256 40946eb4c21a)
- issues: residency_unknown, conflicting_sources:https://www.usm.edu/undergraduate-admissions/costs-scholarships.php,https://www.usm.edu/undergraduate-admissions/freshmen.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 5197 ⟵ “Tuition | $5,197”
  - on_campus:Transportation: 406 ⟵ “Transportation | $406”
  - on_campus:Housing/Meals: 3837 ⟵ “Housing/Meals | $3,837”
  - on_campus:Personal Expenses: 1045 ⟵ “Personal Expenses | $1,045”
  - on_campus:Fees: 106 ⟵ “Fees | $106”
  - on_campus:Books/Supplies: 269 ⟵ “Books/Supplies | $269”
  - on_campus:TOTAL: 10860 ⟵ “TOTAL | $10,860”
### `8db8b679b04ad994` University of Southern Mississippi — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.usm.edu/financial-aid/cost-attendance-previous-year.php (sha256 3c41be776769)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 9998 ⟵ “Tuition | $9,998 | $11,998”
  - on_campus:Transportation: 1328 ⟵ “Transportation | $1,328 | $1,328”
  - on_campus:Housing & Meals: 11920 ⟵ “Housing & Meals | $11,920 | $11,920”
  - on_campus:Personal Expenses: 3304 ⟵ “Personal Expenses | $3,304 | $3,304”
  - on_campus:Fees: 458 ⟵ “Fees | $458 | $458”
  - on_campus:Books/Supplies: 852 ⟵ “Books/Supplies | $852 | $852”
  - on_campus:TOTAL: 27860 ⟵ “TOTAL | $27,860 | $29,860”
### `9cf0aef9f6c91dc0` University of Southern Mississippi — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.usm.edu/financial-aid/cost-of-attendance-current-year.php (sha256 836324ca38ee)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 12394 ⟵ “Tuition | $10,394 | $12,394”
  - on_campus:Transportation: 1300 ⟵ “Transportation | $1,300 | $1,300”
  - on_campus:Housing & Meals: 12278 ⟵ “Housing & Meals | $12,278 | $12,278”
  - on_campus:Personal Expenses: 3344 ⟵ “Personal Expenses | $3,344 | $3,344”
  - on_campus:Misc Fees: 610 ⟵ “Misc Fees | $610 | $610”
  - on_campus:Books/Supplies: 860 ⟵ “Books/Supplies | $860 | $860”
  - on_campus:TOTAL: 30786 ⟵ “TOTAL | $28,786 | $30,786”
### `f086ebecbd6356b4` Wesley Biblical Seminary — appeals 2026-27 [new] (source_unlabeled)
- source: https://wbs.edu/pricing-and-aid/ (sha256 9472615ab73a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Student Aid applicants may be eligible for a special circumstances review.”
### `m460b09037f39093` William Carey University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.wmcarey.edu/dual-enrollment/dual-credit-faq (sha256 16afc5ef9782)
- issues: conflicting_sources:tuition_per_credit_hour, multicolumn_layout_review
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 5, "tiers": 1}
  - per_credit_hour_charge: 60 ⟵ “The tuition rate is $60.00 per credit hour”
  - per_credit_hour_charge: 90 ⟵ “The tuition rate is $90 per hour (Ex., 3-hour course = $270; 4-hour course = $360)”
  - eligibility_tier: 3.0 ⟵ “66 as well as an overall 3.0 GPA on a 4.0                                      •    BUS 102 – Fundl. Computer Concepts and Apps”
  - per_credit_hour_charge: 60 ⟵ “The current price for dual credit classes is $60 per credit hour.  Most dual credit courses are worth 3 credit hours, so most classes will cost $180.  Lab-based courses (ex. Biology, Chemistry, etc.) and MAT 171: Calculus with Analytic Geometry I are worth 4 credit hours and will cost $240 per class”
  - eligibility_tier: 3.0 ⟵ “Students need to have a 3.0 GPA or higher on a 4.0 scale to participate.”
  - max_credit_hours_per_term: 13 ⟵ “Yes, there is a limit.  Students can earn up to a total of 29 credit hours through WCU's dual credit program, and they can take up to a maximum of 13 credit hours in a single term/semester.”
  - eligibility_tier: 3.0 ⟵ “o Students must have at least a 3.00 GPA on a 4.00 scale. GPA’s must be posted on the student”
  - per_credit_hour_charge: 60 ⟵ “o $60.00 per hour – 3-hour class $180.00; 4-hour class $240.00”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 45; pages by category: admissions_tests 18, aid_appeals 12, ap_credit 1, cost_of_attendance 2, dual_enrollment 5, merit_scholarships 18, residency 18, statewide_articulation 1, transfer_credit 2, tuition_fees 25

## Blocked by the site (every request refused; needs the browser fallback)

- Delta State University (`ipeds-175616`)
- Rust College (`ipeds-176318`)

## Leads: official pages found with no extracted record

- Alcorn State University: admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency
- Belhaven University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency, aid_appeals
- Blue Mountain Christian University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit
- Coahoma Community College: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Copiah-Lincoln Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- East Central Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- East Mississippi Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Hinds Community College: cost_of_attendance, admissions_tests, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- Holmes Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency
- Itawamba Community College: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency, degree_requirements
- Jackson State University: tuition_fees, admissions_tests
- Jones County Junior College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements, aid_appeals
- Meridian Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Millsaps College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Mississippi College: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Mississippi Delta Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Mississippi Gulf Coast Community College: admissions_tests, common_data_set, transfer_credit, residency, degree_requirements
- Mississippi State University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Mississippi University for Women: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, ib_credit, transfer_credit, residency, aid_appeals
- Mississippi Valley State University: admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency, degree_requirements
- Northeast Mississippi Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, residency, degree_requirements, aid_appeals
- Northwest Mississippi Community College: admissions_tests, merit_scholarships, transfer_credit, residency
- Pearl River Community College: admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency, degree_requirements
- Southeastern Baptist College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- Southwest Mississippi Community College: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements
- Tougaloo College: cost_of_attendance, admissions_tests, ap_credit, ib_credit, dual_enrollment, transfer_credit, degree_requirements
- University of Mississippi: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, residency
- University of Southern Mississippi: admissions_tests, dual_enrollment, transfer_credit, residency
- Wesley Biblical Seminary: tuition_fees, merit_scholarships, transfer_credit, degree_requirements
- William Carey University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, degree_requirements, aid_appeals
