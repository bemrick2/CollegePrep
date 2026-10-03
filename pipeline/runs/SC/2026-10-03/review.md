# Review queue — SC (2026-27)

Pages fetched: 3447; failures: 320. Candidates: 454 (112 without issues, 342 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 10 | 21 | 16 | 2 | 6 |
| cost_of_attendance | 0 | 0 | 3 | 10 | 34 | 2 | 6 |
| admissions_tests | 0 | 0 | 0 | 0 | 46 | 3 | 6 |
| common_data_set | 0 | 0 | 0 | 0 | 7 | 42 | 6 |
| merit_scholarships | 0 | 0 | 6 | 1 | 39 | 3 | 6 |
| ap_credit | 0 | 0 | 5 | 8 | 13 | 23 | 6 |
| clep_credit | 0 | 0 | 6 | 3 | 11 | 29 | 6 |
| ib_credit | 0 | 0 | 5 | 7 | 8 | 29 | 6 |
| dual_enrollment | 0 | 0 | 12 | 7 | 15 | 15 | 6 |
| transfer_credit | 0 | 0 | 13 | 6 | 26 | 4 | 6 |
| statewide_articulation | 0 | 0 | 0 | 0 | 18 | 31 | 6 |
| residency | 0 | 0 | 0 | 0 | 33 | 16 | 6 |
| degree_requirements | 0 | 0 | 0 | 1 | 30 | 18 | 6 |
| aid_appeals | 0 | 0 | 0 | 35 | 6 | 8 | 6 |

## Ready for review (112)

### `m3c7b0189d3345bf` Aiken Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.atc.edu/admissions/dual-enrollment-student (sha256 8458029e0744)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “an overall high school GPA of 3.0 or higher”
  - per_credit_hour_charge: 207 ⟵ “$207 per credit hour                       $100                                     $150”
  - per_credit_hour_charge: 249 ⟵ “residents): $249 per credit                residents): $126                         Returned check charge: $30”
  - per_credit_hour_charge: 207 ⟵ “$207 per credit hour                       All other out-of-state and             Other Fees”
  - per_credit_hour_charge: 325 ⟵ “$325 per credit hour                        www.atc.edu/tuition-                    hour”
  - per_credit_hour_charge: 196 ⟵ “$196 per credit hour                        South Carolina residents                   $140”
  - per_credit_hour_charge: 235 ⟵ “residents): $235 per credit                 Richmond and Columbia                      Returned check charge: $30”
  - per_credit_hour_charge: 196 ⟵ “$196 per credit hour                        international residents: $126           Other Fees”
  - per_credit_hour_charge: 24 ⟵ “www.atc.edu/Offices/Bursar/                  Access Fee: $24 per credit”
  - per_credit_hour_charge: 308 ⟵ “$308 per credit hour                                                                   hour”
### `m841f85746df51c2` Anderson University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://andersonuniversity.edu/admission-enrollment/undergraduate/dual-enrollment/ (sha256 4c0cce10cdbd)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 3.0 ⟵ “High school juniors and seniors are eligible. Students must have a high school GPA of 3.0, be a high school junior or senior, and meet the qualifying score on the SAT, ACT, CLT or ACCUPLACER test for certain courses they want to take.”
  - eligibility_tier: 3.0 ⟵ “Homeschool students are eligible. Students must have a high school GPA of 3.0, be a high school junior or senior, and meet the qualifying score on the SAT, ACT, CLT or ACCUPLACER test for certain courses they want to take.”
  - eligibility_tier: 3.0 ⟵ “High school juniors and seniors are eligible. Students must have a high school GPA of 3.0, be a high school junior or senior, and meet the qualifying score on the SAT, ACT, CLT or ACCUPLACER test for certain courses they want to take.”
  - eligibility_tier: 3.0 ⟵ “Homeschool students are eligible. Students must have a high school GPA of 3.0, be a high school junior or senior, and meet the qualifying score on the SAT, ACT, CLT or ACCUPLACER test for certain courses they want to take.”
### `ced71754d68b5c87` Benedict College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://benedict.edu/office-of-admissions-and-recruitment/office-of-student-accounts/student-accounts-tuition-fees-other-payments/tuition-and-fees/ (sha256 923133698861)
- checks: {"columns": 3, "components_reconcile": true, "rows": 5}
  - on_campus:TUITION: 8172 ⟵ “TUITION | $8,172 | $8,171 | $16,343”
  - on_campus:GENERAL FEES: 1061 ⟵ “GENERAL FEES | $1,061 | $1,061 | $2,122”
  - on_campus:TECHNOLOGY FEE: 300 ⟵ “TECHNOLOGY FEE | $300 | $300 | $600”
  - on_campus:FOOD & HOUSING (STANDARD RATE): 3726 ⟵ “FOOD & HOUSING (STANDARD RATE) | $3,726 | $3,726 | $7,452”
  - on_campus:TOTAL: 13259 ⟵ “TOTAL | $13,259 | $13,258 | $26,517”
  - on_campus:TUITION: 8171 ⟵ “TUITION | $8,172 | $8,171 | $16,343”
  - on_campus:GENERAL FEES: 1061 ⟵ “GENERAL FEES | $1,061 | $1,061 | $2,122”
  - on_campus:TECHNOLOGY FEE: 300 ⟵ “TECHNOLOGY FEE | $300 | $300 | $600”
  - on_campus:FOOD & HOUSING (STANDARD RATE): 3726 ⟵ “FOOD & HOUSING (STANDARD RATE) | $3,726 | $3,726 | $7,452”
  - on_campus:TOTAL: 13258 ⟵ “TOTAL | $13,259 | $13,258 | $26,517”
  - on_campus:TUITION: 16343 ⟵ “TUITION | $8,172 | $8,171 | $16,343”
  - on_campus:GENERAL FEES: 2122 ⟵ “GENERAL FEES | $1,061 | $1,061 | $2,122”
  - on_campus:TECHNOLOGY FEE: 600 ⟵ “TECHNOLOGY FEE | $300 | $300 | $600”
  - on_campus:FOOD & HOUSING (STANDARD RATE): 7452 ⟵ “FOOD & HOUSING (STANDARD RATE) | $3,726 | $3,726 | $7,452”
  - on_campus:TOTAL: 26517 ⟵ “TOTAL | $13,259 | $13,258 | $26,517”
### `f89c0d837e203428` Bob Jones University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bju.edu/admission/tuition-aid/tuition.php (sha256 db3c1897bb3f)
- checks: {"columns": 1, "rows": 5}
  - column:Tuition per semester (8–12 credits): 4250 ⟵ “Tuition per semester (8–12 credits) | $4,250”
  - column:MDiv Tuition per semester (8–12 credits): 3150 ⟵ “MDiv Tuition per semester (8–12 credits) | $3,150”
  - column:Room and Board per semester: 4320 ⟵ “Room and Board per semester | $4,320”
  - column:Room and Board (value plan): 3805 ⟵ “Room and Board (value plan) | $3,805”
  - column:Program Fee per semester: 275 ⟵ “Program Fee per semester | $275”
### `c2ae695581373b92` Bob Jones University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.bju.edu/admission/apply/transfer/ (sha256 de22bc8cf4f6)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “In general, BJU accepts transfer credit from recognized institutions for any course that is comparable to ones that we offer and that you earned a grade of C or better in.”
  - min_grade: C ⟵ “Only grades of C or better are transferred and are not calculated into one’s BJU until all degree requirements have been successfully met.”
  - min_grade: C ⟵ “Compare the courses between institutions, if they are similar in course description and passed with a grade of C or better, they will generally transfer.”
### `21bc328f218853a5` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 3.90 or above ⟵ “3.90 or above | Jairy C. Hunter, Jr. ($19,000)”
  - award_amount_text: Jairy C. Hunter, Jr. ($19,000) ⟵ “3.90 or above | Jairy C. Hunter, Jr. ($19,000)”
### `2501928e99b5b008` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 3.89 – 3.50 ⟵ “3.89 – 3.50 | Buccaneer ($14,000)”
  - award_amount_text: Buccaneer ($14,000) ⟵ “3.89 – 3.50 | Buccaneer ($14,000)”
### `46a5e2d1d7661e33` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 2.99 – 2.50 ⟵ “2.99 – 2.50 | Gold Rush ($10,000)”
  - award_amount_text: Gold Rush ($10,000) ⟵ “2.99 – 2.50 | Gold Rush ($10,000)”
### `4e1ac843dc26e675` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 2.99 – 2.50 ⟵ “2.99 – 2.50 | Gold Rush ($12,000)”
  - award_amount_text: Gold Rush ($12,000) ⟵ “2.99 – 2.50 | Gold Rush ($12,000)”
### `663e0841f351ba61` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 2.49 – 2.0 ⟵ “2.49 – 2.0 | Blue Crew ($5,000)”
  - award_amount_text: Blue Crew ($5,000) ⟵ “2.49 – 2.0 | Blue Crew ($5,000)”
### `8d293c9858b27c0b` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 3.90 or above ⟵ “3.90 or above | Jairy C. Hunter, Jr. ($17,000)”
  - award_amount_text: Jairy C. Hunter, Jr. ($17,000) ⟵ “3.90 or above | Jairy C. Hunter, Jr. ($17,000)”
### `a2bc2550e9164adb` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 2.49 – 2.0 ⟵ “2.49 – 2.0 | Blue Crew ($7,000)”
  - award_amount_text: Blue Crew ($7,000) ⟵ “2.49 – 2.0 | Blue Crew ($7,000)”
### `b9c7b5cb2357fbda` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 3.89 – 3.50 ⟵ “3.89 – 3.50 | Buccaneer ($16,000)”
  - award_amount_text: Buccaneer ($16,000) ⟵ “3.89 – 3.50 | Buccaneer ($16,000)”
### `c92a8632d6d1f186` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 3.49 – 3.00 ⟵ “3.49 – 3.00 | Cutlass ($15,000)”
  - award_amount_text: Cutlass ($15,000) ⟵ “3.49 – 3.00 | Cutlass ($15,000)”
### `d164e22e97dfd811` Charleston Southern University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- checks: {"thresholds": null}
  - gpa_requirement: GPA: 3.49 – 3.00 ⟵ “3.49 – 3.00 | Cutlass ($13,000)”
  - award_amount_text: Cutlass ($13,000) ⟵ “3.49 – 3.00 | Cutlass ($13,000)”
### `m8f3a719274d0d9d` Charleston Southern University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.charlestonsouthern.edu/admissions/undergraduate/transfer/ (sha256 bd5b7b0768fa)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 68 ⟵ “A student can transfer up to 68 credit hours taken at a 2-year institution (89 if you have an associate’s degree), or 89 credit hours if taken at a 4-year institution.”
  - min_grade: C ⟵ “Section 1: The Office of the Registrar Services provided by the Office of the Registrar Transfer of Credit Charleston Southern accepts transfer credit from other institutions of higher education based on the following considerations: It must have been taken at a regionally accredited college or university with a final grade of C or better.”
### `257e817c896cfe95` Citadel Military College of South Carolina — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.citadel.edu/corps/transfer-policy/ (sha256 a2ff070f1e02)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 37 ⟵ “Students must obtain 30 of the last 37 hours earned within 5 years of the date of graduation at The Citadel.”
### `mb99c07f09078b77` Claflin University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.claflin.edu/about/offices-services/office-of-the-registrar/transfer-services (sha256 ed7de7d40e70)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - max_transfer_credits: 60 ⟵ “No more than 60 semester credit hours may be transferred from two-year institutions (courses number 100-200).”
  - min_grade: C ⟵ “Minimum grade required: A grade of C or better is required for transferability.”
  - min_grade: C ⟵ “South Carolina Technical College System (AA/AS) and Transfer Limits Students with an earned Associate of Arts or Associate of Science degree from one of the 16 schools in the South Carolina Technical College System may enter Claflin as an upper-classman if they meet the agreement requirements, including a cumulative GPA of 2.00 or higher and a grade of “C” or higher in each applicable course.”
### `3adaebfe36201652` Clemson University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.clemson.edu/admissions/undergraduate-admissions/apply/credit-transfer.html (sha256 e152d177b820)
- checks: {"distinct_exams": 18, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | 4 | BIOL 1200/1230 | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business and Management]:  ⟵ “Business and Management | 4, 5, 6, 7 | MGT 2010 | 3”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 4, 5, 6, 7 | CH 1010 (for majors requiring organic chemistry) | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | 4 | CPSC 1110 | 3”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | 4, 5, 6, 7 | ECON 2110, 2120 | 6”
  - equivalencies[IB-FILM|Film]:  ⟵ “Film | 4, 5, 6, 7 | ELEC 00014 | 3”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | 4, 5, 6, 7 | GEOG 1010 | 3”
  - equivalencies[IB-GLOBAL-POLITICS|Global Politics]:  ⟵ “Global Politics | 4, 5, 6, 7 | ELEC 00014 | 3”
  - equivalencies[IB-HISTORY|History]:  ⟵ “History |  |  | ”
  - equivalencies[IB-HISTORY|Islamic History]:  ⟵ “Islamic History | 4, 5, 6, 7 | ELEC | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|Mathematics: Analysis and Approaches]:  ⟵ “Mathematics: Analysis and Approaches | 4, 5 | MATH 1020 or 10601 | 3 or 4”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|Mathematics: Applications and Interpretation]:  ⟵ “Mathematics: Applications and Interpretation | 4, 5 | MATH 19997 | 3”
  - equivalencies[IB-MUSIC|Music]:  ⟵ “Music | 4, 5, 6, 7 | ELEC 00013 | 3”
  - equivalencies[IB-PHILOSOPHY|Philosophy]:  ⟵ “Philosophy | 4, 5, 6, 7 | PHIL 1010 | 3”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | 4 | PHYS 2070/2090 | 4”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | 4, 5, 6, 7 | PSYC 2010 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|Social and Cultural Anthropology]:  ⟵ “Social and Cultural Anthropology | 4, 5, 6, 7 | ANTH 1999 | 3”
  - equivalencies[IB-THEATRE|Theater Arts]:  ⟵ “Theater Arts | 4, 5, 6, 7 | ELEC 00013 | 3”
  - equivalencies[IB-VISUAL-ARTS|Visual Arts]:  ⟵ “Visual Arts | 4, 5, 6, 7 | ART 1030 | 3”
### `950fadf803661d0a` Clemson University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/admissions/undergraduate-admissions/apply/course-transfer-information.html (sha256 0dac0b90e307)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Clemson accepts courses for transfer only if earned with a grade of C or better.”
### `c45ed97dc8b7be59` Clinton College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.clintoncollege.edu/admissions-aid/tuition-and-fees/ (sha256 c5dea62f03fb)
- checks: {"columns": 1, "rows": 8}
  - on_campus:Tuition: 11000.0 ⟵ “Tuition | $5,500.00 | $11,000.00”
  - on_campus:*Enrollment Fee (non-refundable): 100.0 ⟵ “*Enrollment Fee (non-refundable) | $100.00 | $100.00”
  - on_campus:**Room (double occupancy): 6400.0 ⟵ “**Room (double occupancy) | $3,200.00 | $6,400.00”
  - on_campus:***Housing Fee (non-refundable): 300.0 ⟵ “***Housing Fee (non-refundable) | $150.00 | $300.00”
  - on_campus:Board: 8361.9 ⟵ “Board | $4,180.95 | $8,361.90”
  - on_campus:Academic Resources and Learning Materials (All learning materials and technology): 1000.0 ⟵ “Academic Resources and Learning Materials (All learning materials and technology) | $1,000.00 | $1,000.00”
  - on_campus:Student Activity Fee: 250.0 ⟵ “Student Activity Fee | $250.00 | $250.00”
  - on_campus:Totals: 27411.9 ⟵ “Totals | $14,380.95 | $27,411.90”
### `18e384ca10577c6a` Coker University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.coker.edu/tuition-aid/tuition-fees/ (sha256 00f5344001f1)
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 34048 ⟵ “Tuition | $34,048”
  - on_campus:Room (Double)*: 5530 ⟵ “Room (Double)* | $5,530”
  - on_campus:Board: 6130 ⟵ “Board | $6,130”
  - on_campus:Facilities/Infrastructure Fee: 542 ⟵ “Facilities/Infrastructure Fee | $542”
  - on_campus:Technology Fee: 266 ⟵ “Technology Fee | $266”
  - on_campus:Student Activity/Recreation: 266 ⟵ “Student Activity/Recreation | $266”
  - on_campus:Experiential Learning Fee: 88 ⟵ “Experiential Learning Fee | $88”
  - on_campus:Events Fee: 50 ⟵ “Events Fee | $50”
  - on_campus:Total: 46920 ⟵ “Total | $46,920”
### `620413d36badbefe` Coker University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.coker.edu/admissions/traditional-students/transfer-student-admissions/ (sha256 99d4ffbc5fed)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C- ⟵ “Transferable Credit When a student has completed the application for transfer to Coker, the Office of Academic Records will evaluate all transfer credits completed with a grade of C- or better from an accredited institution” Transferring from a 2-year college?”
  - min_grade: C- ⟵ “When a student has completed the application for transfer to Coker, the Registrar’s Office will evaluate all transfer credits completed with a grade of C- or better from an accredited institution. add remove What is the maximum number of credits I can transfer?”
  - max_transfer_credits: 76 ⟵ “Students can transfer up to 76 credit hours from a 2-year school. add remove Are there scholarship opportunities for transfer students?”
### `5fd65d2eb1f2cc97` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.columbiasc.edu/tuition-aid/scholarships-grants (sha256 cd17d4a2b52e)
- checks: {"thresholds": null}
  - gpa_requirement: 3.5+ GPA ⟵ “Presidential ScholarshipOur highest award for outstanding students3.5+ GPA | $10,000 | $6,000”
  - award_amount_text: Presidential ScholarshipOur highest award for outstanding students3.5+ GPA ⟵ “Presidential ScholarshipOur highest award for outstanding students3.5+ GPA | $10,000 | $6,000”
### `6a9a82c84ee51b4e` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.columbiasc.edu/tuition-aid/scholarships-grants (sha256 cd17d4a2b52e)
- checks: {"thresholds": null}
  - gpa_requirement: Award Name & GPA Criteria: 1854 ScholarshipNamed for the year we were founded 3.0–3.49 GPA ⟵ “1854 ScholarshipNamed for the year we were founded 3.0–3.49 GPA | $8,000 | $4,500”
  - award_amount_text: 1854 ScholarshipNamed for the year we were founded 3.0–3.49 GPA ⟵ “1854 ScholarshipNamed for the year we were founded 3.0–3.49 GPA | $8,000 | $4,500”
### `bfd6238ed90cc15e` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.columbiasc.edu/tuition-aid/scholarships-grants (sha256 cd17d4a2b52e)
- checks: {"thresholds": null}
  - gpa_requirement: Award Name & GPA Criteria: Koala ScholarshipNamed for our beloved mascotGPA 2.0 - 2.69 ⟵ “Koala ScholarshipNamed for our beloved mascotGPA 2.0 - 2.69 | $2,000 | $1,000”
  - award_amount_text: Koala ScholarshipNamed for our beloved mascotGPA 2.0 - 2.69 ⟵ “Koala ScholarshipNamed for our beloved mascotGPA 2.0 - 2.69 | $2,000 | $1,000”
### `c913230011ef6212` Columbia College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.columbiasc.edu/tuition-aid/scholarships-grants (sha256 cd17d4a2b52e)
- checks: {"thresholds": null}
  - gpa_requirement: Award Name & GPA Criteria: Columns ScholarshipA symbol of perseverance on campus2.70–2.99 GPA ⟵ “Columns ScholarshipA symbol of perseverance on campus2.70–2.99 GPA | $6,000 | $3,000”
  - award_amount_text: Columns ScholarshipA symbol of perseverance on campus2.70–2.99 GPA ⟵ “Columns ScholarshipA symbol of perseverance on campus2.70–2.99 GPA | $6,000 | $3,000”
### `1468741c446ab013` Columbia International University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://ciu.edu/academics/dualenrollment/ (sha256 e60d3962a6d9)
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - per_credit_hour_charge: 100 ⟵ “$100/credit hour”
  - eligibility_tier: 3.0 ⟵ “3.0 GPA — High school sophomores, juniors and seniors with at least a 3.0 unweighted GPA may participate in dual enrollment.”
  - per_credit_hour_charge: 100 ⟵ “It’s $100 per credit hour or $300 for a three-credit course. Dual enrollment is a big commitment, so make sure it’s the right fit before you enroll. If you’re motivated and ready for the challenge, it can be an ideal way to get a head start on college! If you have questions, reach out to the Admissi”
  - max_credit_hours_per_term: 12 ⟵ “You can take up to 12 credits per semester. If you want to take more, you’ll need special permission from your school and should contact the Registrar’s Office.”
  - per_credit_hour_charge: 100 ⟵ “Save Money – At only $100 per credit hour, the cost savings of dual enrollment classes really add up.”
  - per_credit_hour_charge: 100 ⟵ “No matter which option you choose, all dual enrollment courses are only $100 per credit hour.”
### `c537d7c13d3483df` Columbia International University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://ciu.edu/wp-content/uploads/104-001-Transfer-Credit-Policy.pdf (sha256 65d5f95ab1b7)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 15 ⟵ “CIU requires that the final 15 semester hours of coursework must be CIU credits unless defined otherwise in a cooperative program.”
### `82bd914392aa1665` Converse University — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.converse.edu/undergraduate-catalog-202425/undergraduate-catalog-20232024/transfer-of-credits-from-other-institutions (sha256 f30d7cd666d2)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Credit for courses in the approved pre- engineering program at Converse University and passed with a grade of “C” or higher will be transferred to Clemson University.”
### `m8d97a279cf3b424` Denmark Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.denmarktech.edu/catalog/transfer-students/ (sha256 03d1a59b3a6d)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Courses being transferred must have a grade of C or better.”
  - min_grade: C ⟵ “In order to transfer credit, a grade of “C” or better must have been made in the course.”
### `d5abfeaee9f78da8` Erskine College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.erskine.edu/admissions-aid/#story (sha256 c6cfa9137717)
- checks: {"columns": 1, "rows": 5}
  - on_campus:Tuition: 34435.0 ⟵ “Tuition | $17,217.50 | $17,217.50 | $34,435.00”
  - on_campus:Institutional Service Fee: 2275.0 ⟵ “Institutional Service Fee | $1,137.50 | $1,137.50 | $2,275.00”
  - on_campus:Meal Plan: 7000.0 ⟵ “Meal Plan | $3,500.00 | $3,500.00 | $7,000.00”
  - on_campus:Room: 6900.0 ⟵ “Room | $3,450.00 | $3,450.00 | $6,900.00”
  - on_campus:Totals: 50610.0 ⟵ “Totals | $25,305.00 | $25,305.00 | $50,610.00”
### `m0759909f2ab450a` Francis Marion University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.fmarion.edu/wp-content/uploads/2016/07/Dual-Enrollment-Book-2025.pdf (sha256 2a22101f01d4)
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Students wishing to participate in FMU’s Dual Enrollment Program should be enrolled in a partnering high school, have a 3.0 or higher cumulative GPA, be juniors or seniors, and receive school permission to participate in the courses.”
  - eligibility_tier: 3.0 ⟵ “seniors in high school and have a minimum high school GPA of 3.0. Students should also”
  - max_credit_hours_per_term: 14 ⟵ “a student take each       maximum total of up to 14 credit hours including labs each semester.”
  - eligibility_tier: 3.0 ⟵ “Have a minimum high school GPA of 3.0”
### `52172e38e59785b9` Francis Marion University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.fmarion.edu/dualenrollment/dual-enrollment-permission-form/ (sha256 839b08124ff2)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Students should also determine what grade must be earned in the course to have it transfer to another institution. (Typically, a grade of “C” or higher will transfer.) Tips for Success Attend class based upon the attendance policy outlined in the course syllabus.”
### `07c2aac48b6959fd` Horry-Georgetown Technical College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.hgtc.edu/documents/academics/prior-learning-assessment/international-baccalaureate.pdf (sha256 55ab48cef425)
- checks: {"distinct_exams": 14, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology                              BIO-101      Biological Science I                    4”
  - equivalencies[IB-BIOLOGY|6]:  ⟵ “Biology                              BIO-102      Biological Science II                   6”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business and Management              BUS-101      Introduction to Business                4”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry                            CHM-110      College Chemistry I                     4”
  - equivalencies[IB-CHEMISTRY|6]:  ⟵ “Chemistry                            CHM-111        College Chemistry II                  6”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics                            ECO-210        Macroeconomics                        4”
  - equivalencies[IB-ECONOMICS|6]:  ⟵ “Economics                            ECO-211        Microeconomics                        6”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French B                             FRE-101        Elementary French I                   4”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French B                             FRE-102        Elementary French II                  5”
  - equivalencies[IB-FRENCH|6]:  ⟵ “French B                             FRE-201        Intermediate French I                 6”
  - equivalencies[IB-FRENCH|7]:  ⟵ “French B                             FRE-202        Intermediate French II                7”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography                            GEO-102        World Geography                       4”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German B                             GER-101        Elementary German I                   4”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German B                             GER-102        Elementary German II                  5”
  - equivalencies[IB-GERMAN|6]:  ⟵ “German B                             GER-201        Intermediate German I                 6”
  - equivalencies[IB-GERMAN|7]:  ⟵ “German B                             GER-202        Intermediate German II                7”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of Africa                    HIS-106        Introduction to African History       4”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of the Americas              HIS-201        American History: Discovery to 1877   4”
  - equivalencies[IB-HISTORY|6]:  ⟵ “History of the Americas              HIS-202        American History: 1877 to Present     6”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of West and South Asia       HIS-001        History Non-Equivalent Transfer       4”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of Europe                    HIS-101        Western Civilization to 1689          4”
  - equivalencies[IB-HISTORY|6]:  ⟵ “History of Europe                    HIS-102        Western Civilization Post 1689        6”
  - equivalencies[IB-MUSIC|4]:  ⟵ “Music                                MUS-105        Music Appreciation                    4”
  - equivalencies[IB-PHILOSOPHY|4]:  ⟵ “Philosophy                           PHI-101        Introduction to Philosophy            4”
  - equivalencies[IB-PHYSICS|4]:  ⟵ “Physics                              PHY-201        Physics I                             4”
  - … 9 more rows
### `343c389aeaeacdd3` Horry-Georgetown Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.hgtc.edu/documents/academics/prior-learning-assessment/clep-scores.pdf (sha256 d3f8da5c8314)
- checks: {"distinct_exams": 29, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting                                                  50          3           ACC 101”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business law, Introductory                                            50          3           BUS 121”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of                                             50          3           MGT 101”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of                                              50          3           MKT 101”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems                                                   50          3           CPT 119”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                                                   50          6           ENG 201, 202”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                                                   50          6           ENG 101, 102”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                                                    50          6           ENG 205, 206”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                                                            50          6           ELECTIVES”
  - equivalencies[CLEP-FRENCH-LANGUAGE|45]:  ⟵ “French Language, Level 1                                                 45           4          FRE 101”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, Level 1                                                 50           8          FRE 101, 102”
  - equivalencies[CLEP-FRENCH-LANGUAGE|66]:  ⟵ “French Language, Level 2                                                 66           11         FRE 101, 102, 201”
  - equivalencies[CLEP-GERMAN-LANGUAGE|45]:  ⟵ “German Language, Level 1                                                 45           4          GER 101”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, Level 1                                                 50           8          GER 101, 102”
  - equivalencies[CLEP-GERMAN-LANGUAGE|66]:  ⟵ “German Language, Level 2                                                 66           11         GER 101, 102, 201”
  - equivalencies[CLEP-SPANISH-LANGUAGE|45]:  ⟵ “Spanish Language, Level 1                                                45           4          SPA 101”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1                                                50           8          SPA 101, 102”
  - equivalencies[CLEP-SPANISH-LANGUAGE|66]:  ⟵ “Spanish Language, Level 2                                                66           11         SPA 101, 102, 201”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                                                   50          3           PSC 201”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early colonization to 1877            50          3           HIS 201”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present                      50          3           HIS 202”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development                                          50          3           PSY 203”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles of                                         50          3           ECO 210”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles of                                         50          3           ECO 211”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory                                              50          3           PSY 201”
  - … 10 more rows
### `a77ffc9a28036d1d` Horry-Georgetown Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.hgtc.edu/documents/academics/prior-learning-assessment/ap-scores.pdf (sha256 381db71a6991)
- checks: {"distinct_exams": 23, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                      3      3          ART 101”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                          3      4          BIO 101”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology                          4      8          BIO 101, BIO 102”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                        3      4          CHM 110”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry                        4      8          CHM 110, CHM 111”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles      3      3          CPT 168”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macroeconomics        3      3          ECO 210”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Microeconomics        3      3          ECO 211”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science            3      4          BIO 209”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language                  3      4          FRE 101”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language                  4      8          FRE 101, FRE 102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Literature                3     11          FRE 101, FRE 102, FRE 201”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                  3      3          GEO 101”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language                  3      4          GER 101”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language                  4      8          GER 101, GER 102”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin Literature                 3      3          LAT 101”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Mathematics: Calculus AB         3      4          MAT 140”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Mathematics: Calculus BC         3      8          MAT 140, MAT 141”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus                      3      3          MAT 110”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Precalculus                      4      6          MAT 110, MAT 111”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1                        3      4          PHY 201”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2                        4      8          PHY 201, PHY 202”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C: Mechanics             3      4          PHY 221”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity & Mag     3      4          PHY 222”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                       3      3          PSY 201”
  - … 7 more rows
### `c3b0039ca684042b` Lander University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.lander.edu/admissions/undergraduate/dual-enrollment.html (sha256 54bdf02d1919)
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.25 ⟵ “Dual Enrollment is available to all qualifying (3.25+ GPA) Juniors and Seniors who reside in the State of South Carolina”
  - max_credit_hours_per_term: 6 ⟵ “Eligible high school juniors and seniors can take up to 6 credit hours (2 courses) at Lander per semester (Fall and Spring) tuition free”
  - per_credit_hour_charge: 100 ⟵ “Additional hours may be taken for $100 per credit hour (books and course-related fees still apply)”
### `05abe334f9a9c1f7` Midlands Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://www.midlandstech.edu/admissions/testing-services/advanced-standing/mtc-clep-policy (sha256 e83fc3ada546)
- checks: {"distinct_exams": 23, "equivalencies": 38, "rows_without_score": 0}
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer | 50 | General Elective | CPT 001 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | Business Law I | BUS 121 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Principles of Financial Accounting | 50 | Accounting Concepts | ACC 111 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | Principles of Management | MGT 101 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | Marketing | MKT 101 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|55]:  ⟵ “American Literature | 55 | American Literature Survey | ENG 203 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|53]:  ⟵ “Analyzing & Interpreting Literature | 53 | General Elective | GEN 001 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | English Composition I | ENG 101 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “(Discontinued) College Composition Modular | 50 | English Composition I | ENG 101 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|55]:  ⟵ “English Literature | 55 | Literature Survey | LIT 001 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|54]:  ⟵ “(Discontinued) Freshman College Composition (Essay Required) | 54 | English Composition I | ENG 101 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | General Elective | HUM 001 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French, Level 1 | 50 | General Elective | FRE 101 | 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French, Level 2 | 59 | General Elective | FRE 102 | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German, Level 1 | 50 | General Elective | GER 101 | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German, Level 2 | 60 | General Elective | GER 102 | 4”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish, Level 1 | 50 | General Elective | SPA 101 | 4”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish, Level 2 | 63 | General Elective | SPA 102 | 4”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing Level 1 Proficiency | 50 | General Elective | SPA 101 | 4”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History & Social Sciences || American Government | 50 | American Government | PSC 201 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History & Social Sciences || History of the United States I: Early Colonization to 1877 | 50 | American History: Discovery to 1877 | HIS 201 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History & Social Sciences || History of the United States II: 1865 to the Present | 50 | American History: 1877 to Present | HIS 202 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History & Social Sciences || Human Growth & Development | 50 | Human Growth & Development | PSY 203 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History & Social Sciences || Introduction to Educational Psychology | 50 | Social and Behavioral Sciences | SCS 002 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History & Social Sciences || Principles of Macroeconomics | 50 | Macroeconomics | ECO 210 | 3”
  - … 13 more rows
### `4069b503f3e6e915` Newberry College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.newberry.edu/admission/tuition-fees (sha256 017501e0074c)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 2100 ⟵ “Tuition | $2100”
  - column:Academic Commons Fee: 125 ⟵ “Academic Commons Fee | $125”
  - column:Technology Fee: 0 ⟵ “Technology Fee | $0”
  - column:Housing: 400 ⟵ “Housing | $400”
  - column:Dining: 525 ⟵ “Dining | $525”
  - column:Total Berry Beginnings Tuition, Fees, Room & Board: 3150 ⟵ “Total Berry Beginnings Tuition, Fees, Room & Board | $3,150”
### `0b5ad1aa101b909f` North Greenville University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/financial-aid/undergraduate/academic-scholarships/ (sha256 b2840b004e2d)
- checks: {"thresholds": null}
  - award_amount_text: $7,000 ⟵ “Dean’s Scholarship | 3.0–3.74 GPAMaintain 2.75 GPA | $7,000 | $5,000”
  - eligibility_summary: 3.0–3.74 GPAMaintain 2.75 GPA ⟵ “Dean’s Scholarship | 3.0–3.74 GPAMaintain 2.75 GPA | $7,000 | $5,000”
### `0d5290475fabea1c` North Greenville University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/financial-aid/undergraduate/academic-scholarships/ (sha256 b2840b004e2d)
- checks: {"thresholds": null}
  - award_amount_text: $12,000 ⟵ “Founder’s Scholarship | 3.5 GPA AND 1250 SAT, 27 ACT or 84 CLTOR4.7+ GPAMaintain 3.0 GPA | $12,000 | $9,000”
  - eligibility_summary: 3.5 GPA AND 1250 SAT, 27 ACT or 84 CLTOR4.7+ GPAMaintain 3.0 GPA ⟵ “Founder’s Scholarship | 3.5 GPA AND 1250 SAT, 27 ACT or 84 CLTOR4.7+ GPAMaintain 3.0 GPA | $12,000 | $9,000”
### `52ccbb5c68067e57` North Greenville University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/financial-aid/undergraduate/academic-scholarships/ (sha256 b2840b004e2d)
- checks: {"thresholds": null}
  - award_amount_text: $8,000 ⟵ “Level 3 (3.2-3.49)Must maintain a 3.0 GPA | $8,000 | $6,000”
  - gpa_requirement: 3.0 GPA ⟵ “Level 3 (3.2-3.49)Must maintain a 3.0 GPA | $8,000 | $6,000”
### `91e2b8dbfdf7ac99` North Greenville University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/financial-aid/undergraduate/academic-scholarships/ (sha256 b2840b004e2d)
- checks: {"thresholds": null}
  - award_amount_text: $9,000 ⟵ “President’s Scholarship | 3.5 GPA and 1100 SAT, 24 ACT or 74 CLTOR3.75–4.69 GPAMaintain 3.0 GPA | $9,000 | $7,000”
  - eligibility_summary: 3.5 GPA and 1100 SAT, 24 ACT or 74 CLTOR3.75–4.69 GPAMaintain 3.0 GPA ⟵ “President’s Scholarship | 3.5 GPA and 1100 SAT, 24 ACT or 74 CLTOR3.75–4.69 GPAMaintain 3.0 GPA | $9,000 | $7,000”
### `9fbaec2520c1b87c` North Greenville University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/financial-aid/undergraduate/academic-scholarships/ (sha256 b2840b004e2d)
- checks: {"thresholds": null}
  - award_amount_text: $10,000 ⟵ “Level 2 (3.5-3.79)Must maintain a 3.0 GPA | $10,000 | $7,000”
  - gpa_requirement: 3.0 GPA ⟵ “Level 2 (3.5-3.79)Must maintain a 3.0 GPA | $10,000 | $7,000”
### `cb7b44f40ed12241` North Greenville University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/financial-aid/undergraduate/academic-scholarships/ (sha256 b2840b004e2d)
- checks: {"thresholds": null}
  - award_amount_text: $12,000 ⟵ “Level 1 (3.8-4.0)Must maintain a 3.0 GPA | $12,000 | $9,000”
  - gpa_requirement: 3.0 GPA ⟵ “Level 1 (3.8-4.0)Must maintain a 3.0 GPA | $12,000 | $9,000”
### `f98eaafb12102bbe` North Greenville University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/financial-aid/undergraduate/academic-scholarships/ (sha256 b2840b004e2d)
- checks: {"thresholds": null}
  - award_amount_text: $7,000 ⟵ “Level 4 (2.75-3.19)Must maintain a 3.0 GPA | $7,000 | $5,000”
  - gpa_requirement: 3.0 GPA ⟵ “Level 4 (2.75-3.19)Must maintain a 3.0 GPA | $7,000 | $5,000”
### `c64e75cba44f15a0` North Greenville University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/tuition-fees/tuition-and-fees-charts/ (sha256 16f9fff611f6)
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 27600 ⟵ “Tuition | $27,600”
  - column:Campus Life Fee: 350 ⟵ “Campus Life Fee | $350”
  - column:Standard Housing: 5900 ⟵ “Standard Housing | $5,900”
  - column:Food: 7050 ⟵ “Food | $7,050”
  - column:Subtotal: 40900 ⟵ “Subtotal | $40,900”
### `10b4aa847c71c756` North Greenville University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ngu.edu/admissions/ap-equivalents/ (sha256 6960c4e12bc2)
- checks: {"distinct_exams": 39, "equivalencies": 40, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “AP 2-D Art and Design | 3 | 3 | Elective Credit”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “AP 3-D Art and Design | 3 | 3 | Elective Credit”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “AP Art History | 3 | 3 | ARTS 2310”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “AP Biology | 3 | 4 | BIOL 1410”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “AP Calculus AB | 3 | 4 | MATH 1410”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “AP Calculus BC | 3 | 8 | MATH 1410 & MATH 2410”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “AP Calculus BC: AB Subscore | 3 | 3 | Elective Credit”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “AP Chemistry | 3 | 4 | CHEM 1480”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “AP Chinese Language and Culture | 3 | 3 | Elective Credit”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “AP Comparative Government and Politics | 3 | 3 | PLSC 2375”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “AP Computer Science A | 3 | 3 | CSCI 2325”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “AP Computer Science Principles | 3 | 3 | CYBR 1330”
  - equivalencies[AP-CYBERSECURITY|3]:  ⟵ “AP Cybersecurity | 3 | 3 | CYBR 1320”
  - equivalencies[AP-DRAWING|3]:  ⟵ “AP Drawing | 3 | 3 | ARTS 1310”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language and Composition | 3 | 3 | ENGL 1310”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 or 4]:  ⟵ “AP English Literature and Composition | 3 or 4 | 3 | ENGL 1320”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “AP Environmental Science | 3 | 4 | BIOL 1450”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “AP European History | 3 | 3 | HIST 1385”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “AP French Language and Culture | 3 | 6 | FREN 1310 & FREN 1320”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “AP German Language and Culture | 3 | 3 | GERM 1310”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “AP Human Geography | 3 | 3 | GEOG 2310”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “AP Italian Language and Culture | 3 | 3 | Elective Credit”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “AP Japanese Language and Culture | 3 | 3 | Elective Credit”
  - equivalencies[AP-LATIN|3]:  ⟵ “AP Latin | 3 | 3 | Elective Credit”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “AP Macroeconomics | 3 | 3 | ECON 2310”
  - … 15 more rows
### `278d2d09e5f51186` North Greenville University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ngu.edu/admissions/how-to-apply/dual-enrollment/ (sha256 39dbfc7d94f9)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - per_credit_hour_charge: 100 ⟵ “Earn college credit while still in high school. Enjoy higher level learning from a Christian perspective. Experience campus life and set yourself up for a smooth transition into college. Plus, you won’t have to break the bank to start earning college credit. NGU’s Dual Enrollment Program has a flat ”
  - eligibility_tier: 3.0 ⟵ “It’s easy to get started. If you’re a high school junior or senior (at least 16-years-old) with a maintained GPA of 3.0 (or better), you’re eligible for the Dual Enrollment Program. Get started today with four simple steps.”
  - per_credit_hour_charge: 30 ⟵ “Dual Enrollment students receive textbooks through the Slingshot Textbook Butler service. The price of the rental service is $30 per credit hour. The student can choose to opt out of the service if desired by setting your preferences in your My.NGU portal.  Select “Students” then “Slingshot Textbook”
### `81d211ff077079bd` North Greenville University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ngu.edu/admissions/college-level-examination-program/ (sha256 45d65ad7a3db)
- checks: {"distinct_exams": 34, "equivalencies": 42, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 | ACCT-2310”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | 3 | CYBR-1330”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BUSN-2360”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 | MGMT-2310”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 3 | MRKT-2335”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|Composition and Literature]:  ⟵ “Principles of Marketing | Composition and Literature”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 | ENGL-2330”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 | ENGL-1320”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 | ENGL-1310”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 3 | Elective Credit”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 | ENGL-2310”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | Elective Credit”
  - equivalencies[CLEP-HUMANITIES|History and Social Sciences]:  ⟵ “Humanities | History and Social Sciences”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | PLSC-2310”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Coloization to 1877 | 50 | 3 | HIST-2310”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | 50 | 3 | HIST-2320”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PSYC-2350”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | 3 | EDUC-3340”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | PSYC-2310”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | SOCY-2310”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 | ECON-2310”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 | ECON-2320”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | 3 | Elective Credit”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | 3 | HIST-1350”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | 3 | HIST-1385”
  - … 17 more rows
### `279eeba9d2881383` North Greenville University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ngu.edu/admissions/how-to-apply/transfer/ (sha256 97f1c383ab28)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 36 ⟵ “You must earn 30 of the last 36 credit hours in a degree program at North Greenville University unless an exception is approved by the respective dean and vice president for academics.”
  - residency_requirement_credits: 36 ⟵ “The exact rule: you must earn 30 of the last 36 credit hours in a degree program at North Greenville University, unless an exception is approved by the respective dean and vice president for academics.”
### `69ac55451e6bfee2` Piedmont Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.ptc.edu/index%2Ephp/cost-financial-aid/tuition-fees (sha256 225a8ca33db5)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:*Tuition (defaults at 12 per term): 5400 ⟵ “*Tuition (defaults at 12 per term) | $4,860 | $4,860 | $5,400 | $5,400 | $5,670 | $5,670 | $7,008 | $7,008 | $8,916 | $8,916”
  - column:Fees: 300 ⟵ “Fees | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Living Expenses (Food & Housing): 16930 ⟵ “Living Expenses (Food & Housing) | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $16,930 | $16,930”
  - column:Books/Supplies: 2500 ⟵ “Books/Supplies | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500”
  - column:Transportation: 5108 ⟵ “Transportation | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108”
  - column:Personal/Misc.: 3150 ⟵ “Personal/Misc. | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - column:Loan Fees: 100 ⟵ “Loan Fees | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100”
  - column:Total: 33488 ⟵ “Total | $23,606 | $32,948 | $24,146 | $33,488 | $24,416 | $33,758 | $25,754 | $35,096 | $37,004 | $37,004”
### `df3ea0478e100293` Piedmont Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.ptc.edu/index%2Ephp/cost-financial-aid/tuition-fees (sha256 225a8ca33db5)
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:*Tuition (defaults at 12 per term): 5400 ⟵ “*Tuition (defaults at 12 per term) | $4,860 | $4,860 | $5,400 | $5,400 | $5,670 | $5,670 | $7,008 | $7,008 | $8,916 | $8,916”
  - column:Fees: 300 ⟵ “Fees | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Living Expenses (Food & Housing): 7588 ⟵ “Living Expenses (Food & Housing) | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $16,930 | $16,930”
  - column:Books/Supplies: 2500 ⟵ “Books/Supplies | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500”
  - column:Transportation: 5108 ⟵ “Transportation | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108”
  - column:Personal/Misc.: 3150 ⟵ “Personal/Misc. | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - column:Loan Fees: 100 ⟵ “Loan Fees | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100”
  - column:Total: 24146 ⟵ “Total | $23,606 | $32,948 | $24,146 | $33,488 | $24,416 | $33,758 | $25,754 | $35,096 | $37,004 | $37,004”
### `m2b3f07dfceb5220` Piedmont Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.ptc.edu/academics/dual-enrollment-academics (sha256 93ad51d5f9df)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 0}
  - per_credit_hour_charge: 150 ⟵ “Students taking only one course on a PTC campus or online will attend at a standard tuition rate of $150/credit hour.”
  - per_credit_hour_charge: 50 ⟵ “Those students who are taking only one Dual Enrollment course at their high school or career center taught by a district employee will attend at $50/credit hour. Note: Additional charges apply at $150 for each additional credit hour for students taking more than 12 hours in a semester.”
  - per_credit_hour_charge: 120 ⟵ “of $120/credit hour.                                                                         College website at www.ptc.edu/”
### `407e72f6e29eff6f` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": null}
  - gpa_requirement: < 2.49 ⟵ “Transfer Award | < 2.49 | $22,000”
### `5143e2d17924a3e6` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": null}
  - gpa_requirement: 4.50-4.84 ⟵ “Highlander Scholarship | 4.50-4.84 | up to $28,000”
### `761104efacd402ea` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": null}
  - gpa_requirement: 4.15-4.49 ⟵ “Belk Scholarship | 4.15-4.49 | up to $26,000”
### `9600147443e7e994` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": null}
  - gpa_requirement: 3.00 -3.49 ⟵ “Scotsman Scholarship | 3.00 -3.49 | $26,000”
### `aa325908baa93642` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": null}
  - gpa_requirement: 3.75-4.14 ⟵ “Tartan Scholarship | 3.75-4.14 | up to $24,000”
### `b1afb7f2ff404154` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - gpa_requirement: 3.50 + ⟵ “True Blue Scholarship | 3.50 + | $28,000”
### `e6fb93afa8d21a20` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": null}
  - gpa_requirement: <3.74 ⟵ “Trustees Award | <3.74 | up to $22,000”
### `e7c22bb00c2bf8d7` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": {"gpa_min": 4.85}}
  - gpa_requirement: 4.85 and above ⟵ “Founders Scholarship | 4.85 and above | up to $30,000”
### `ef139fb14c5bd9d1` Presbyterian College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/costs-and-aid/scholarships/ (sha256 235f51c99432)
- checks: {"thresholds": null}
  - gpa_requirement: 2.50 – 3.00 ⟵ “Trustee Award | 2.50 – 3.00 | $24,000”
### `5f0080bd8a8c7490` Presbyterian College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.presby.edu/costs-and-aid/tuition-and-fees/ (sha256 3092a5089cb5)
- checks: {"columns": 3, "components_reconcile": true, "rows": 11}
  - on_campus:Tuition: 22180 ⟵ “Tuition | 22,180 | 22,180 | 44,360”
  - on_campus:Fees: 1600 ⟵ “Fees | 1,600 | 1,600 | 3,200”
  - on_campus:Housing*: 3572 ⟵ “Housing* | 3,572 | 3,572 | 7,144”
  - on_campus:Standard Meal Plan: 26 swipes, 8 exchanges, $250 Bonus Bucks: 3750 ⟵ “Standard Meal Plan: 26 swipes, 8 exchanges, $250 Bonus Bucks | 3,750 | 3,750 | 7,500”
  - on_campus:Books, course materials, supplies and equipment (laptop): 1050 ⟵ “Books, course materials, supplies and equipment (laptop) | 1,050 | 1,050 | 2,100”
  - on_campus:Transportation: 848 ⟵ “Transportation | 848 | 848 | 1,695”
  - on_campus:Loan Fees: 23 ⟵ “Loan Fees | 23 | 22 | 45”
  - on_campus:Miscellaneous personal expenses: 703 ⟵ “Miscellaneous personal expenses | 703 | 703 | 1,406”
  - on_campus:Subtotal for Indirect Costs: 2624 ⟵ “Subtotal for Indirect Costs | 2,624 | 2,622 | 5,246”
  - on_campus:Total Cost of Attendance: 33726 ⟵ “Total Cost of Attendance | $33,726 | $33,724 | $67,450”
  - on_campus:Total: 31102 ⟵ “Total | $31,102 | $31,102 | $62,204”
  - on_campus:Tuition: 22180 ⟵ “Tuition | 22,180 | 22,180 | 44,360”
  - on_campus:Fees: 1600 ⟵ “Fees | 1,600 | 1,600 | 3,200”
  - on_campus:Housing*: 3572 ⟵ “Housing* | 3,572 | 3,572 | 7,144”
  - on_campus:Standard Meal Plan: 26 swipes, 8 exchanges, $250 Bonus Bucks: 3750 ⟵ “Standard Meal Plan: 26 swipes, 8 exchanges, $250 Bonus Bucks | 3,750 | 3,750 | 7,500”
  - on_campus:Books, course materials, supplies and equipment (laptop): 1050 ⟵ “Books, course materials, supplies and equipment (laptop) | 1,050 | 1,050 | 2,100”
  - on_campus:Transportation: 848 ⟵ “Transportation | 848 | 848 | 1,695”
  - on_campus:Loan Fees: 22 ⟵ “Loan Fees | 23 | 22 | 45”
  - on_campus:Miscellaneous personal expenses: 703 ⟵ “Miscellaneous personal expenses | 703 | 703 | 1,406”
  - on_campus:Subtotal for Indirect Costs: 2622 ⟵ “Subtotal for Indirect Costs | 2,624 | 2,622 | 5,246”
  - on_campus:Total Cost of Attendance: 33724 ⟵ “Total Cost of Attendance | $33,726 | $33,724 | $67,450”
  - on_campus:Total: 31102 ⟵ “Total | $31,102 | $31,102 | $62,204”
  - on_campus:Tuition: 44360 ⟵ “Tuition | 22,180 | 22,180 | 44,360”
  - on_campus:Fees: 3200 ⟵ “Fees | 1,600 | 1,600 | 3,200”
  - on_campus:Housing*: 7144 ⟵ “Housing* | 3,572 | 3,572 | 7,144”
  - … 8 more rows
### `mde1043ca89ef8f9` Presbyterian College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/doc/registrar/Transfer-Course-Equivalencies-List.pdf (sha256 b43d6405bc0c)
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C- ⟵ “Students must earn a grade of C- or higher for any course to transfer to PC.”
  - min_grade: C- ⟵ “Students must earn a grade of C- or higher for any course to transfer to PC.”
  - min_grade: C- ⟵ “BIO 211 - Anatomy and Physiology II 4 BIOL 3032/3032L 4 BIO 225 - Microbiology 4 BIOL 3060 4 Please Note: CHM 110 - College Chemistry I 4 CHEM 101/101L 4 You must have a grade of C- or better for a CHM 111 - College Chemistry II 4 CHEM 102/102L 4 course to be considered for transfer of credit.”
### `2bf310dabb705347` Southern Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.swu.edu/on-campus/financial-aid/scholarships-and-grants/ (sha256 c2d607b90f20)
- checks: {"thresholds": null}
  - award_amount_text: $10,000 ⟵ “Opportunity Scholarship | $10,000 | <2.5”
  - gpa_requirement: <2.5 ⟵ “Opportunity Scholarship | $10,000 | <2.5”
### `467d699d5871b951` Southern Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.swu.edu/on-campus/financial-aid/scholarships-and-grants/ (sha256 c2d607b90f20)
- checks: {"thresholds": null}
  - award_amount_text: $11,000 ⟵ “Warrior Scholarship | $11,000 | 2.5 – 3.39”
  - gpa_requirement: 2.5 – 3.39 ⟵ “Warrior Scholarship | $11,000 | 2.5 – 3.39”
### `9c83d528f9626979` Southern Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.swu.edu/on-campus/financial-aid/scholarships-and-grants/ (sha256 c2d607b90f20)
- checks: {"thresholds": null}
  - award_amount_text: $13,000 ⟵ “Trustee Scholarship | $13,000 | 3.4 – 4.29”
  - gpa_requirement: 3.4 – 4.29 ⟵ “Trustee Scholarship | $13,000 | 3.4 – 4.29”
### `d6fa43deca61f468` Southern Wesleyan University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.swu.edu/on-campus/financial-aid/scholarships-and-grants/ (sha256 c2d607b90f20)
- checks: {"thresholds": {"gpa_min": 4.3}}
  - award_amount_text: $14,000 ⟵ “Presidential Scholarship | $14,000 | 4.3+”
  - gpa_requirement: 4.3+ ⟵ “Presidential Scholarship | $14,000 | 4.3+”
### `8e3df2670b4ecc63` Southern Wesleyan University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.swu.edu/on-campus/dual-enrollment/ (sha256 0ce06315e956)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 125 ⟵ “Tuition for Dual Enrollment: $125 per credit hour”
  - per_credit_hour_charge: 20 ⟵ “Technology Fee: $20 per credit hour”
### `865745f1deca6f1b` Southern Wesleyan University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.swu.edu/on-campus/transfer-students/articulation-agreements/ (sha256 5776aefe044f)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “A grade of C- or better is necessary in all coursework transferred toward the Early Childhood and Family Students bachelor’s degree at Southern Wesleyan University.”
### `mc3d980bb13b698d` Spartanburg Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.sccsc.edu/media/spartanburgcc/content-assets/documents/admissions-amp-financial-aid/student-amp-parent-resources/high-school-dual-credit/Dual-Enrollment-Survival-Guide_Print_English_Accessible.pdf (sha256 4f555cbbbf64)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Please indicate the appropriate permission level below: This student is using a 3.0 or higher High School GPA”
  - eligibility_tier: 3.0 ⟵ “A: Juniors and seniors with a weighted GPA of 3.0 or higher (depending on their high school).”
  - eligibility_tier: 3.0 ⟵ “ чні 11 та 12 класів з середнім балом GPA 3.0 або вище (залежно від навчального закладу).   В: SCC пропонує проходити курси за програмою подвійного зарахування особисто, онлайн,”
### `1a9c1559b0509db6` Tri-County Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.tctc.edu/financial-aid/student-financial-aid-services/tuition-fees/tuition-for-fall-2026-summer-2027/ (sha256 e1f2c0ea6f46)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 13597 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $13,597 | $13,597 | $16,996”
  - with_parents_or_family:Other Fees (FEES): 0 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - with_parents_or_family:Living Expenses (RB): 18453 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - with_parents_or_family:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - with_parents_or_family:Transportation (TRAN): 2268 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - with_parents_or_family:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - with_parents_or_family:Total: 37976 ⟵ “Total | $37,976 | $44,201 | $42,116”
  - off_campus_not_with_family:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 13597 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $13,597 | $13,597 | $16,996”
  - off_campus_not_with_family:Other Fees (FEES): 0 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - off_campus_not_with_family:Living Expenses (RB): 24678 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - off_campus_not_with_family:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - off_campus_not_with_family:Transportation (TRAN): 2268 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - off_campus_not_with_family:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 44201 ⟵ “Total | $37,976 | $44,201 | $42,116”
  - on_campus:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 16996 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $13,597 | $13,597 | $16,996”
  - on_campus:Other Fees (FEES): 2586 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - on_campus:Living Expenses (RB): 17616 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - on_campus:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - on_campus:Transportation (TRAN): 1260 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - on_campus:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - on_campus:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - on_campus:Total: 42116 ⟵ “Total | $37,976 | $44,201 | $42,116”
### `1e9ad9e42d744ffb` Tri-County Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.tctc.edu/financial-aid/student-financial-aid-services/tuition-fees/tuition-for-fall-2026-summer-2027/ (sha256 e1f2c0ea6f46)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 6589 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $6,589 | $6,589 | $8,236”
  - with_parents_or_family:Other Fees (FEES): 0 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - with_parents_or_family:Living Expenses (RB): 18453 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - with_parents_or_family:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - with_parents_or_family:Transportation (TRAN): 2268 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - with_parents_or_family:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - with_parents_or_family:Total: 30968 ⟵ “Total | $30,968 | $37,193 | $33,356”
  - off_campus_not_with_family:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 6589 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $6,589 | $6,589 | $8,236”
  - off_campus_not_with_family:Other Fees (FEES): 0 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - off_campus_not_with_family:Living Expenses (RB): 24678 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - off_campus_not_with_family:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - off_campus_not_with_family:Transportation (TRAN): 2268 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - off_campus_not_with_family:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 37193 ⟵ “Total | $30,968 | $37,193 | $33,356”
  - on_campus:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 8236 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $6,589 | $6,589 | $8,236”
  - on_campus:Other Fees (FEES): 2586 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - on_campus:Living Expenses (RB): 17616 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - on_campus:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - on_campus:Transportation (TRAN): 1260 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - on_campus:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - on_campus:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - on_campus:Total: 33356 ⟵ “Total | $30,968 | $37,193 | $33,356”
### `91a0825808095ec0` University of South Carolina Aiken — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.usca.edu/departments/registrar/transfer-articulation/non-traditional-credit/ (sha256 435c8a4b28a4)
- checks: {"distinct_exams": 20, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|55]:  ⟵ “CLEP Financial Accounting | BADM A225 Financial Accounting | 55”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “CLEP Business Law | BADM A324 Commercial Law | 50”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “CLEP Information Systems | BADM A390 Business Information Mgmt | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “CLEP Macroeconomics | ECON A221 Principles of Macroeconomics | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “CLEP Microeconomics | ECON A222 Principles of Microeconomics | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “CLEP Management | BADM A371 Principles of Management | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “CLEP Marketing | BADM A350 Principles of Marketing | 50”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “CLEP American Government | POLI A201 American National Government | 50”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “CLEP US History I | HIST A201 History of the US TO 1865 | 50”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “CLEP US History II | HIST A202 History of the US Since 1865 | 50”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|51]:  ⟵ “CLEP College Composition | ENGL A101 Composition | 51”
  - equivalencies[CLEP-AMERICAN-LITERATURE|57]:  ⟵ “CLEP American Literature | ENGL A002T | 57”
  - equivalencies[CLEP-ENGLISH-LITERATURE|57]:  ⟵ “CLEP English Literature | ENGL A002T | 57”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “CLEP Biology | BIOL A121 | 50”
  - equivalencies[CLEP-BIOLOGY|56]:  ⟵ “CLEP Biology | BIOL A121 and BIOL A122 | 56”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “CLEP Chemistry | CHEM A111 General Chemistry I | 50”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “CLEP College Algebra | MATH A108 Applied College Algebra | 50”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “CLEP Precalculus | MATH A111 Precalculus Math I | 50”
  - equivalencies[CLEP-CALCULUS|47]:  ⟵ “CLEP Calculus | MATH A141 Calculus I | 47”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “CLEP Psychology | PSYC A101 Introductory Psychology | 50”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “CLEP Sociology | SOCY A101 Introductory Sociology | 50”
### `a93078ba68f483b9` University of South Carolina Aiken — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.usca.edu/departments/registrar/transfer-articulation/non-traditional-credit/ (sha256 435c8a4b28a4)
- checks: {"distinct_exams": 34, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|ARTS A103]:  ⟵ “Art 2D Design | ARTS A103 | ARTS A103 | ARTS A103”
  - equivalencies[AP-3-D-ART-DESIGN|ARTS A103]:  ⟵ “Art 3D Design | ARTS A103 | ARTS A103 | ARTS A103”
  - equivalencies[AP-DRAWING|ARTS A111]:  ⟵ “Art Drawing | ARTS A111 | ARTS A111 | ARTS A111”
  - equivalencies[AP-ART-HISTORY|ARTH A105]:  ⟵ “Art History | ARTH A105 | ARTH A105 | ARTH A105”
  - equivalencies[AP-BIOLOGY|BIOL A121 or A122]:  ⟵ “Biology | BIOL A121 or A122 | BIOL A121 and A122 | BIOL A121 and A122”
  - equivalencies[AP-CALCULUS-AB|MATH A141]:  ⟵ “Calculus AB | MATH A141 | MATH A141 | MATH A141”
  - equivalencies[AP-CALCULUS-BC|MATH A141 and A142]:  ⟵ “Calculus BC | MATH A141 and A142 | MATH A141 and A142 | MATH A141 and A142”
  - equivalencies[AP-CHEMISTRY|CHEM A111]:  ⟵ “Chemistry | CHEM A111 | CHEM A111 and A112 | CHEM A111 and A112”
  - equivalencies[AP-COMPUTER-SCIENCE-A|CSCI A145]:  ⟵ “Computer Science A | CSCI A145 | CSCI A145 | CSCI A145”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|CSCI A101]:  ⟵ “Computer Science Principles | CSCI A101 | CSCI A101 | CSCI A101”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|ENGL A101]:  ⟵ “English Lang/Comp* | ENGL A101 | ENGL A101 | ENGL A101 and A102”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|ENGL A101 or A102]:  ⟵ “English Lit/Comp* | ENGL A101 or A102 | ENGL A101 or A102 | ENGL A101 and A102”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|BIOL A106]:  ⟵ “Environmental Science | BIOL A106 | BIOL A106 and GEOL A103 | BIOL A106 and GEOL A103”
  - equivalencies[AP-EUROPEAN-HISTORY|HIST A102]:  ⟵ “European History | HIST A102 | HIST A102 | HIST A101 and A102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FREN A101]:  ⟵ “French Language | FREN A101 | FREN A101 and A102 | FREN A101 and A102”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|GERM A101]:  ⟵ “German Language | GERM A101 | GERM A101 and A102 | GERM A101 and A102”
  - equivalencies[AP-HUMAN-GEOGRAPHY|GEOG A103]:  ⟵ “Human Geography | GEOG A103 | GEOG A103 | GEOG A103”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|ITAL A101]:  ⟵ “Italian Language | ITAL A101 | ITAL A101 and ITAL A102 | ITAL A101 and ITAL A102”
  - equivalencies[AP-LATIN|LATN A101]:  ⟵ “Latin | LATN A101 | LATN A101 and A102 | LATN A101 and A102”
  - equivalencies[AP-MACROECONOMICS|ECON A221]:  ⟵ “Macroeconomics | ECON A221 | ECON A221 | ECON A221”
  - equivalencies[AP-MICROECONOMICS|ECON A222]:  ⟵ “Microeconomics | ECON A222 | ECON A222 | ECON A222”
  - equivalencies[AP-MUSIC-THEORY|MUSC A196]:  ⟵ “Music Theory | MUSC A196 | MUSC A196 and MUSC A198 | MUSC A196, A198 and A296”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|PHYS A202]:  ⟵ “Physics C-E&M | PHYS A202 | PHYS A212 | PHYS A212”
  - equivalencies[AP-PHYSICS-C-MECHANICS|PHYS A201]:  ⟵ “Physics C-Mech | PHYS A201 | PHYS A211 | PHYS A211”
  - equivalencies[AP-PHYSICS-1|PHYS A201]:  ⟵ “Physics I | PHYS A201 | PHYS A201 | PHYS A201”
  - … 10 more rows
### `a9c2ce9047b4a154` University of South Carolina Aiken — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.usca.edu/departments/registrar/transfer-articulation/non-traditional-credit/ (sha256 435c8a4b28a4)
- checks: {"distinct_exams": 15, "equivalencies": 16, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|BIOL A121]:  ⟵ “IB Biology | BIOL A121 | BIOL A121 and A122 | BIOL A121 and A122”
  - equivalencies[IB-BUSINESS-MANAGEMENT|BADM A371]:  ⟵ “IB Business and Mgmt. | BADM A371 | BADM 371 and MGMT 376 | BADM 371 and MGMT 376”
  - equivalencies[IB-CHEMISTRY|CHEM A111]:  ⟵ “IB Chemistry | CHEM A111 | CHEM A111 and A112 | CHEM A111 and A112”
  - equivalencies[IB-ECONOMICS|ECON A221]:  ⟵ “IB Economics | ECON A221 | ECON A221 | ECON A221”
  - equivalencies[IB-HISTORY|HIST A102]:  ⟵ “IB European History | HIST A102 | HIST A102 | HIST A102”
  - equivalencies[IB-FRENCH|FREN A101 and A102]:  ⟵ “IB French B | FREN A101 and A102 | FREN A101 and A102 | FREN A210”
  - equivalencies[IB-GEOGRAPHY|GEOG A103]:  ⟵ “IB Geography | GEOG A103 | GEOG A103 | GEOG A103”
  - equivalencies[IB-GERMAN|GERM A101 and A102]:  ⟵ “IB German B | GERM A101 and A102 | GERM A101 and A102 | GERM A210”
  - equivalencies[IB-HISTORY|No Equivalent]:  ⟵ “IB History of Africa/ME | No Equivalent | HSSI A002T (Non-West) | HSSI A002T (Non-West)”
  - equivalencies[IB-LATIN|LATN A101 and A102]:  ⟵ “IB Latin B | LATN A101 and A102 | LATN A101 and A102 | LATN 210”
  - equivalencies[IB-MUSIC|MUSC A173]:  ⟵ “IB Music | MUSC A173 | MUSC A173 | MUSC A173”
  - equivalencies[IB-PHYSICS|PHYS A201]:  ⟵ “IB Physics | PHYS A201 | PHYS A201 and A202 | PHYS A201 and A202”
  - equivalencies[IB-PSYCHOLOGY|PSYC A101]:  ⟵ “IB Psychology | PSYC A101 | PSYC A101 | PSYC A101”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|ANTH A102]:  ⟵ “IB Social Anthropology | ANTH A102 | ANTH A102 | ANTH A102”
  - equivalencies[IB-SPANISH|SPAN A101 and A102]:  ⟵ “IB Spanish B | SPAN A101 and A102 | SPAN A101 and A102 | SPAN A210”
  - equivalencies[IB-VISUAL-ARTS|No Equivalent]:  ⟵ “Visual Arts | No Equivalent | ARTS A103 | ARTS A103”
### `06687e9b9242c13e` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Hilton Head Hospital Auxiliary | Pre-licensure BSN students who are residents of Beaufort or Jasper counties | 3.0 | ”
### `0bf429e86d4ea857` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Daufuskie Island Gullah Geechee Endowed Scholarship | Students who trace their ancestry to Gullah Geechee people of the Sea Islands of SC, NC, GA and FL | 3.0 | Any class, any major”
### `209d4109246a6376` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “John W. Castles Scholarship Fund | Full-time student with Financial Need, Academic Merit | 3.0 | ”
### `29ffa8fbb56b0ad9` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “William Mason Hardimon Scholarship Fund | Business major, financial need, academic merit, no more than 120 credit hours. | 3.0 | ”
### `36bd08f101ce3e65` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Delta Kappa Gamma | Senior women | 3.0 | Education Majors planning to teach”
### `39c03d525b976ca6` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Baker's Psychology | Psychology Majors | 3.0 | Any class”
### `634849584f75252b` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - gpa_requirement: 2.5 ⟵ “Brett Borton Memorial Scholarship | Communication major undergraduate students | 2.5 | Awarded by USCB's Scholarship Committee and the Financial Aid Office”
### `65ffe6e723e93485` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Brinkley Family Endowment Fund | Full-time freshman student, academic merit, Beaufort, Colleton, Jasper or Hampton County resident, first-generation college student. | 3.0 | First consideration to Boys & Girls Club participants or Mt. Calvary Missionary Baptist Achievement School.”
### `7f87d4f6c319fff4` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.2}}
  - gpa_requirement: 3.2 ⟵ “Gamma Beta Phi Scholarship | Financial need & academic merit, preference to Gamma Beta Phi member | 3.2 | Must submit essay about how scholarship and service develop character”
### `a4510e1d2e162d8a` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “John and Valerie Curry (HH Wine and Food Festival) | Junior or Senior Hospitality Majors. Residents of Beaufort or Jasper counties, SC, or Bryan, Chatham, or Effingham counties, GA | 3.0 | Preference to students or family members working in Hospitality or Tourism”
### `ac14d04924caeade` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Edith R. Harvey Endowed Scholarship Fund | Financial need, academic merit, interest in religious studies or liberal arts, intent to enter seminary | 3.0 | ”
### `ad8fb62c4c3e055b` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Michael Best Memorial Scholarship | Hospitality Management majors. Preference shall be for students with an operational focus | 3.0 | ”
### `b7a232384a79b8ff` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “J.P Gonzalez Endowed Scholarship | Students who are local residents of Beaufort, Jasper, Hampton, Colleton, Chatham, Effingham counties | 3.0 | Financial Need based”
### `cab4a1e3f7b78590` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “G Thomas Upshaw Endowed Scholarship | Full-time student with financial need, academic merit, Beaufort Jasper or Hampton County resident. | 3.0 | First consideration to veteran or US Military active duty”
### `cd126b8165595300` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 2.5}}
  - gpa_requirement: 2.5 ⟵ “Nicholas D. Lucchesi Memorial Scholarship | Preference may be given to a student with documented financial need and/or a documented learning challenge. | 2.5 | ”
### `d37dc1c9c434daba` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Kathleen and Jim Jordan Annual Scholarship | Freshman student preferably majoring in History. Must maintain academic excellence. A Beaufort County resident. | 3.0 | ”
### `f8522209254d61a2` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Bud E. Carcharias Athletic Leadership Scholarship | Student athletes | 3.0 | ”
### `fc4fef7cf7442a60` University of South Carolina Beaufort — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/donor-scholarships/index.html (sha256 093a5e4e6496)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Linda Lisi Pre-Veterinarian Endowed Scholarship | Biological Sciences- Pre- Veterinarian track, academic merit, must maintain academic excellence | 3.0 | ”
### `f2929ea49cdbdfb5` University of South Carolina Beaufort — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.uscb.edu/admissions/apply/dual-enrollment/index.html (sha256 66444f539576)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a GPA of 3.0 or higher”
### `b9563890c22ccbdf` University of South Carolina Beaufort — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.uscb.edu/admissions/apply/transfer/index.html (sha256 aca7854e4ce1)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “To be eligible for transfer credit at USCB, courses must earn a grade of C or higher.”
### `952d621807342284` University of South Carolina-Upstate — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://uscupstate.edu/admissions/high-school-dual-enrollment/ (sha256 3d5a221f7703)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 66 ⟵ “The cost is $66 per credit hour. Most courses are three credit hours.”
### `5a7b8d11599db85b` University of South Carolina-Upstate — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://uscupstate.edu/wp-content/uploads/2025/10/Transfer-Guide.pdf (sha256 4a57374c4150)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C ⟵ “In addition, transfer credits to USC Upstate must be for academic courses completed with grades of “C” or better from regionally accredited institutions.”
  - max_transfer_credits: 90 ⟵ “CREDITS FROM YOUR PREVIOUS COLLEGE OR UNIVERSITY: A maximum of 90 semester hours from a regionally accredited institution may be transferred to the University for degree credit.”
### `bb5cbc64092fe46c` Voorhees University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://voorhees.edu/office-of-admissions/office-of-financial-aid/ (sha256 a73261ea13e2)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 11630 ⟵ “Tuition | $11,630 | $11,630”
  - column:Technology Fee: 550 ⟵ “Technology Fee | $550 | $550”
  - column:Student Activity Fee: 450 ⟵ “Student Activity Fee | $450 | $450”
  - column:Board: 0 ⟵ “Board | $3,670 | $0”
  - column:Room: 0 ⟵ “Room | $3,676 | $0”
  - column:Total: 12630 ⟵ “Total | $19,976 | $12,630”
### `c5098935c982a804` Voorhees University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://voorhees.edu/office-of-admissions/tuition-fees/ (sha256 1b9c41b321b9)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 11630 ⟵ “Tuition | $11,630 | $11,630”
  - column:Technology Fee: 550 ⟵ “Technology Fee | $550 | $550”
  - column:Student Activity Fee: 450 ⟵ “Student Activity Fee | $450 | $450”
  - column:Board: 3670 ⟵ “Board | $3,670 | $0”
  - column:Room: 3676 ⟵ “Room | $3,676 | $0”
  - column:Total: 19976 ⟵ “Total | $19,976 | $12,630”
### `3b88e01ec1de0a04` Voorhees University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://voorhees.edu/office-of-admissions/transfer-students/ (sha256 0f823fcdffca)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “Degree Requirements To earn degrees, transfer students must earn their final 30 hours of credit at Voorhees University.”
### `7e34e7adb8c692cb` Williamsburg Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.wiltech.edu/prospective-students/hs-dual-enrollment-cate/dual-enrollment/ (sha256 d99a7e5f4593)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “• be enrolled in high school courses with at least a 2.5 GPA”
### `110aae0fc08b43eb` Winthrop University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.winthrop.edu/admissions/transfer/york-technical-college.aspx (sha256 7e2b62f1a86e)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Each academic college will evaluate all transfer credits with final grades of "C-" or better from an accredited institution once we receive your final transcript.”
### `16a76794a24fe4f8` Wofford College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.wofford.edu/academics/registrar/ap-cambridge-clep-dual-enrollment-ib/international-baccalaureate (sha256 ed6e52ece32a)
- checks: {"distinct_exams": 19, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|HL]:  ⟵ “Social & Cultural Anthropology | HL | 5, 6, 7 | Anthropology 202 | 3”
  - equivalencies[IB-BIOLOGY|HL]:  ⟵ “Biology | HL | 5, 6, 7 | Biology 101, 102 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|HL]:  ⟵ “Business & Management | HL | 5, 6, 7 | Elective | 3”
  - equivalencies[IB-CHEMISTRY|HL]:  ⟵ “Chemistry | HL | 5, 6, 7 | Chemistry 123, 124 | 8”
  - equivalencies[IB-ECONOMICS|HL]:  ⟵ “Economics | HL | 5, 6, 7 | Economics 201, 202 | 6”
  - equivalencies[IB-ENGLISH-A-LITERATURE|HL]:  ⟵ “English A Literature | HL | 5, 6, 7 | English 101 | 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|HL]:  ⟵ “English A Language and Literature | HL | 5, 6, 7 | English 102 | 3”
  - equivalencies[IB-FRENCH|HL]:  ⟵ “French B | HL | 5, 6, 7 | French 201, 202 | 6”
  - equivalencies[IB-GERMAN|HL]:  ⟵ “German B | HL | 5, 6, 7 | German 201, 202 | 6”
  - equivalencies[IB-GLOBAL-POLITICS|HL]:  ⟵ “Global Politics | HL | 5, 6, 7 | International Affairs 285 | 3”
  - equivalencies[IB-HISTORY|HL]:  ⟵ “History-European | HL | 5, 6, 7 | History 101, 102 | 6”
  - equivalencies[IB-HISTORY|HL]:  ⟵ “History-Americas | HL | 5, 6, 7 | History 111, 112 | 6”
  - equivalencies[IB-LATIN|HL]:  ⟵ “Latin | HL | 5, 6, 7 | Latin 101, 102 | 6”
  - equivalencies[IB-MUSIC|HL]:  ⟵ “Music | HL | 5, 6, 7 | Music 201 | 3”
  - equivalencies[IB-PHILOSOPHY|HL]:  ⟵ “Philosophy | HL | 5, 6, 7 | Philosophy 120 | 3”
  - equivalencies[IB-PHYSICS|HL]:  ⟵ “Physics | HL | 5, 6, 7 | Physics 121, 122 | 8”
  - equivalencies[IB-PSYCHOLOGY|HL]:  ⟵ “Psychology | HL | 5, 6, 7 | Psychology 110 | 3”
  - equivalencies[IB-SPANISH|HL]:  ⟵ “Spanish B | HL | 5, 6, 7 | Spanish 201, 202 | 6”
  - equivalencies[IB-THEATRE|HL]:  ⟵ “Theatre Arts | HL | 5, 6, 7 | Theatre 201 | 3”
  - equivalencies[IB-VISUAL-ARTS|HL]:  ⟵ “Visual Arts | HL | 5, 6, 7 | Art History 201 | 3”
### `8c0caef85b034ded` Wofford College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.wofford.edu/academics/registrar/ap-cambridge-clep-dual-enrollment-ib/advanced-placement (sha256 fa52a2b9c52a)
- checks: {"distinct_exams": 13, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[AP-3-D-ART-DESIGN|Arts 260]:  ⟵ “Studio-Art 3-D Design | 4 | Arts 260 | 3 | Fulfills general education Fine Arts requirement”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “Studio-Art 3-D Design | Studio Art Drawing | 4 | Arts 251 | 3 | Fulfills general education Fine Arts requirement”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “Studio-Art 3-D Design | History of Art | 4 | Arth 201, 202 | 6 | Each fulfills general education Fine Arts requirement”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | Biology | 4 | Biology 101, 102 | 8 | Fulfills the general education science lab requirement”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | Chemistry | 4 | Chemistry 123 | 4 | Fulfills the general education science lab requirement”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | Chemistry | 5 | Chemistry 123, 124 | 8 | Fulfills the general education science lab requirement”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese | Chinese Language & Culture | 4 | Chinese 101, 102 | 8 | Fulfills general education Foreign Language requirement”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese | Chinese Language & Culture | 5 | Chinese 201, 202 | 8 | Fulfills general education Foreign Language requirement”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese | Computer Science Principles | 4 | Computer Science 285 | 3 | Elective credit hours”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese | Macroeconomics | 4 | Economics 202 | 3 | Fulfills general education Social Science requirement”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese | Literature and Composition | 4 | English 102 | 3 | Fulfills general education English requirement”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | Environmental Science | 4 | Environmental Science 110, 111 | 8 | Fulfills the general education science lab/science in context requirements”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French | Level 3: French Language | 4 | French 201, 202 | 6 | Fulfills general education Foreign Language requirement”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German | Level 3: German Language | 4 | German 201, 202 | 6 | Fulfills general education Foreign Language requirement”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German | Government and Politics: Comparative | 4 | Government 286 | 3 | Fulfills general education Social Science requirement”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German | United States History | 4 | History 111, 112 | 6 | Fulfills general education History requirement”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German | World History | 4 | History 187, 188 | 6 | Fulfills general education History requirement”
  - equivalencies[AP-HUMAN-GEOGRAPHY|N/A]:  ⟵ “Human Geography | N/A | N/A | No credit awarded | N/A | N/A”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4]:  ⟵ “Italian | Italian Language & Culture | 4 | Italian 201, 202 | 6 | Fulfills general education Foreign Language requirement”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4]:  ⟵ “Japanese | Japanese Language & Culture | 4 | Japanese 201, 202 | 6 | Fulfills general education Foreign Language requirement”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin | Latin Language | 4 | Latin 201, 202 | 6 | Fulfills general education Foreign Language requirement”
  - equivalencies[AP-LATIN|*]:  ⟵ “Latin | Calculus AB Subscore | * | See Explanation | N/A | N/A”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | Calculus BC | 3 | Math 181 | 3 | Fulfills general education Mathematics requirement”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin | Calculus BC | 4 | Math 181, 182 | 6 | Fulfills general education Mathematics requirement”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin | Statistics | 4 | Math 140 | 3 | Fulfills general education Mathematics requirement”
  - … 8 more rows
### `9dcc6f8dea84647c` Wofford College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.wofford.edu/academics/registrar/ap-cambridge-clep-dual-enrollment-ib/college-level-examination-program (sha256 8ffbe9fe8983)
- checks: {"distinct_exams": 23, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | English 102 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | English 203 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | English 201-202 | 6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “FR College Composition | 50 | English 101 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Elective Credit | 3”
  - equivalencies[CLEP-HUMANITIES|Science & Mathematics]:  ⟵ “Humanities | Science & Mathematics”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | Biology 101-102 | 8”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | Math 181 | 3”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | Chemistry 123-124 | 8”
  - equivalencies[CLEP-CHEMISTRY|Social Sciences & History]:  ⟵ “Chemistry | Social Sciences & History”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | Government 280 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Educational Psychology, Intro to | 50 | Education 330 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | History 111 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | History 112 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | Education 320 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles of | 50 | Economics 202 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles of | 50 | Economics 201 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | 50 | Psychology 110 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | 50 | Sociology 101 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 50 | History 101 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II | 50 | History 102 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|Business]:  ⟵ “Western Civilization II | Business”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law, Introductory | 50 | Economics 372 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | Computer Science 101 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | 50 | Business 338 | 3”
  - … 5 more rows
### `7c701a9bf7c703e1` Wofford College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.wofford.edu/admission/transfer-student-admission/transfer-student-admission.pdf (sha256 fae2ff8695db)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “Wofford’s residency requirement stipulates that the last 30 credit hours of coursework and more than half of the requirements for the major/minor must be completed at Wofford College in order to earn a Wofford degree.”
### `14f5e77b3510405b` York Technical College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.yorktech.edu/admissions/credit-for-prior-learning/standardized-exams/ (sha256 8ec8cfc08d03)
- checks: {"distinct_exams": 19, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|4]:  ⟵ “Biology HL (IB 0101) | 4 | BIO-101 & BIO-102 | 4.0 & 4.0”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|4]:  ⟵ “Business and Management HL (IB 0111) | 4 | MGT-101 | 3”
  - equivalencies[IB-CHEMISTRY-HL|4]:  ⟵ “Chemistry HL (IB 0121) | 4 | CHM-110 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|4]:  ⟵ “Computer Science HL (IB 0131) | 4 | CPT-168 | 3”
  - equivalencies[IB-ECONOMICS-HL|4]:  ⟵ “Economics HL (IB 0151) | 4 | ECO-211 | 3”
  - equivalencies[IB-ECONOMICS-HL|6]:  ⟵ “Economics HL (IB 0151) | 6 | ECO-210 & ECO-211 | 3.0 & 3.0”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|4]:  ⟵ “English A Literature HL | 4 | ENG-208 | 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|4]:  ⟵ “English A Lang & Literature HL | 4 | ENG-209 | 3”
  - equivalencies[IB-FRENCH-HL|4]:  ⟵ “French A1 HL (IB 0191) | 4 | FRE-101 | 4”
  - equivalencies[IB-FRENCH-HL|4]:  ⟵ “French A2 HL (IB 0201) | 4 | FRE-102 | 4”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French AB | 4 | FRE-101 | 4”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French B | 5 | FRE-101 & FRE-102 | 4.0 & 4.0”
  - equivalencies[IB-GEOGRAPHY-HL|4]:  ⟵ “Geography HL | 4 | GEO-199 | 3”
  - equivalencies[IB-GERMAN-HL|4]:  ⟵ “German A1 HL (IB 0231) | 4 | GER-101 | 4”
  - equivalencies[IB-GERMAN-HL|4]:  ⟵ “German A2 HL (IB 0241) | 4 | GER-102 | 4”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German AB | 4 | GER-101 | 4”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German AB | 5 | GER-101 & GER-102 | 4.0 & 4.0”
  - equivalencies[IB-HISTORY-HL|4]:  ⟵ “History of the Americas HL | 4 | HIS-201 | 3”
  - equivalencies[IB-HISTORY-HL|6]:  ⟵ “History of the Americas HL | 6 | HIS-201 & HIS-202 | 3.0 & 3.0”
  - equivalencies[IB-HISTORY-HL|4]:  ⟵ “History of Europe HL | 4 | HIS-102 | 3”
  - equivalencies[IB-MUSIC-HL|4]:  ⟵ “Music HL (IB 0311) | 4 | MUS-105 | 3”
  - equivalencies[IB-PHILOSOPHY-HL|4]:  ⟵ “Philosophy HL (IB 0321) | 4 | PHI-101 | 3”
  - equivalencies[IB-PSYCHOLOGY-HL|4]:  ⟵ “Psychology HL (IB 0341) | 4 | PSY-201 | 3”
  - equivalencies[IB-PSYCHOLOGY-HL|5]:  ⟵ “Psychology Abnormal HL | 5 | PSY-212 | 3”
  - equivalencies[IB-PSYCHOLOGY-HL|5]:  ⟵ “Psychology Developmental HL | 5 | PSY-203 | 3”
  - … 8 more rows
### `92341950adf73ff3` York Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.yorktech.edu/admissions/credit-for-prior-learning/standardized-exams/ (sha256 8ec8cfc08d03)
- checks: {"distinct_exams": 29, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | PSC-201 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG-201 & ENG-202 | 3.0 & 3.0”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MAT-140 | 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MAT-110 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENG-101 & ENG-102 | 3.0 & 3.0”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MAT-155 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG-205 & ENG-206 | 3.0 & 3.0”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACC-101 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language | 50 | FRE-101 & FRE-102 | 4.0 & 4.0”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “General Biology | 50 | BIO-101 | 4”
  - equivalencies[CLEP-BIOLOGY|60]:  ⟵ “General Biology | 60 | BIO-101 & BIO-102 | 4.0 & 4.0”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “General Chemistry | 50 | CHM-110 | 4”
  - equivalencies[CLEP-CHEMISTRY|60]:  ⟵ “General Chemistry | 60 | CHM-110 & CHM-111 | 4.0 & 4.0”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language | 50 | GER-101 & GER-102 | 4.0 & 4.0”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 | HIS-201 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | 50 | HIS-202 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSY-203 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | ART-101 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | CPT-101 & CPT-170 | 3.0 & 3.0”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BUS-121 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSY-201 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introduction to Sociology | 50 | SOC-101 | 3”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | BIO-105 | 4”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | 50 | MAT-112 | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | MGT-101 | 3”
  - … 7 more rows
### `dc2c43f28baab832` York Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.yorktech.edu/admissions/credit-for-prior-learning/standardized-exams/ (sha256 8ec8cfc08d03)
- checks: {"distinct_exams": 26, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ART-101 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIO-101 | 4”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MAT-140 | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MAT-140 & MAT-141 | 4.0 & 4.0”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHM-110 | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHM-110 & CHM-111 | 4.0 & 4.0”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | CPT-101 & CPT-170 | 3.0 & 3.0”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition | 3 | ENG-101 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition | 3 | ENG-101 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature & Composition | 4 | ENG-101 & ENG-102 | 3.0 & 3.0”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | BIO-205 & BIO-206 | 3.0 & 1.0”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIS-102 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | FRE-101 & FRE-102 | 4.0 & 4.0”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | FRE-101 & FRE-102 | 4.0 & 4.0”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | GER-101 & GER-102 | 4.0 & 4.0”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language & Culture | 5 | GER-101 & GER-102 | 4.0 & 4.0”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEO-199 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | ECO-210 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | ECO-211 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | MUS-105 | 3”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1 | 3 | PHY-201 | 4”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2 | 3 | PHY-202 | 4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C – Electricity & Magnetism | 3 | PHY-222 | 4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C – Mechanics | 3 | PHY-221 | 4”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Precalculus | 4 | MAT-112 | 5”
  - … 7 more rows

## Exceptions (342)

### `0ac104d3617d411b` state-SC — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.che.sc.gov/sites/che/files/Documents/Institutions%20and%20Educators/Policy%20Program%20Etc/Transfer/Dual_Enrollment_Transfer_Guide.pdf (sha256 b7aa578987ff)
- issues: semantic_review_required
- checks: {"guarantees": 2, "requirements": 5}
  - statements.requirements: 5 ⟵ “Courses that require you to write papers that are at least     General Education The list of South Carolina Universally Transferrable five pages in length and, once you’ve received teacher feedback, provide the opportunity to revise and rewrite. http://www.che.sc.gov/AcademicAffairs/TRANSFER/tran 2.”
  - statements.guarantees: 2 ⟵ “Courses that require you to do research and write papers sferable_courses.pdf) identifies courses guaranteed by policy to transfer among and between South Carolina using original sources.                                             in High School 4.”
### `0dcd02dc1876d8bd` state-SC — state_policies 2022-23 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://che.sc.gov/institutions-and-educators/higher-education-nursing-initiative (sha256 94f1e7af5ebb)
- issues: stale_year_label:2022-23, semantic_review_required
- checks: {"exceptions": 1, "requirements": 6}
  - statements.requirements: 6 ⟵ “Participating students must enroll in in regionally accredited, not-for-profit, South Carolina based, public and private institutions graduate-level Master of Science (MSN) programs, Doctor of Nursing Practice, Ph.D., or other like programs appropriate to prepare individuals for faculty roles and ag”
  - statements.exceptions: 1 ⟵ “However, if an institution’s operating budget is constrained and lacks sufficient “wiggle room” to absorb these fringe benefit expenses, then Nursing Initiative funds may also be used for such additional fringe benefit expenses directly associated with the salary supplement if necessary.”
### `20b1dbe3c69bbe2b` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (ambiguous_year_labels)
- source: https://che.sc.gov/sites/che/files/Documents/Meetings/Meetings%202023/Transfer%20Covening/JGardner%20National%20Best%20Practices_CHE_Transfer_Convening.pdf (sha256 56d445a3ccdc)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"exceptions": 1, "requirements": 9}
  - statements.requirements: 9 ⟵ “Underperformance in the transfer function manifested by unacceptably low levels of completion of bachelor’s degrees for ALL students and especially when disaggregated by student characteristics such as income, race, ethnicity, first generation and financial aid eligibility status, is NOT just a Sout”
  - statements.exceptions: 1 ⟵ “Extent of SC Private Institutions’ Ability to Be Competitive with SC Public Two-Year Colleges in Enrolling Dual Credit Secondary School Students: Recognizing that current state support for high school dual credit goes disproportionately to the public two-year sector, should you consider recommending”
### `29123efc2843c251` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/reverse-transfer (sha256 736da9345bf4)
- issues: semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Must have earned a minimum of 30 credit hours.”
### `2b4afed73ff74660` state-SC — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://che.sc.gov/ipeds-acts-supplemental-information (sha256 b6f4dd954f81)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "requirements": 3}
  - statements.requirements: 3 ⟵ “Department of Education requires four-year institutions with selective admissions to submit detailed, disaggregated data on applications, admissions, enrollment, and aid by race-sex pairings; and further broken out by GPA quintiles, test-score quintiles, family income ranges, Pell-grant eligibility,”
  - statements.effective: 1 ⟵ “The supplement is first collected during the 2025–2026 IPEDS reporting cycle and will be updated annually as part of regular IPEDS data collection.”
### `2bf459f91de4e5bf` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/life-and-palmetto-fellows-math-and-science-scholarship-enhancements (sha256 de6766ba26a8)
- issues: semantic_review_required
- checks: {"requirements": 12}
  - statements.requirements: 12 ⟵ “LIFE and Palmetto Fellows Scholarships, along with scholarship enhancements, must be used toward the cost of attendance at an eligible four-year institution in South Carolina.”
### `40e230661be7dce6` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/additional-scholarship-grant-searches (sha256 6d2d33cfcd2f)
- issues: semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Covers last-dollar tuition and mandatory fees for eligible students, as well as FAFSA and college application assistance. (Available to students from Greenwood County Districts 50/51/52 only.) A company that offers students simplified college scholarship search by matching students’ qualifications a”
### `4d1d3cd65b4d112d` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (ambiguous_year_labels)
- source: https://che.sc.gov/students-families-and-military/scholarships-and-grants-sc-residents (sha256 64a4d9cfdb91)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"effective": 1, "requirements": 35}
  - statements.requirements: 35 ⟵ “Students must be South Carolina residents to receive state-funded financial aid.”
  - statements.effective: 1 ⟵ “Effective Academic Year 2025-26, South Carolina Army National Guard and Air National Guard CAP recipients may receive up to a maximum of $12,000 per academic year (maximum of $4,000 per semester for full-time students) if enrolled in a two-year or four-year program at eligible South Carolina institu”
### `5070ff296d439676` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (ambiguous_year_labels)
- source: https://che.sc.gov/sites/che/files/Documents/Meetings/Meetings%202023/Transfer%20Covening/Fall%20Transfer%20Convening/Meta%20Majors%20and%20Guided%20Pathways%20for%20University%20Transfer%20Students.pdf (sha256 f8764547e633)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Provide a 02.                                            framework of guidance for students that will help them make the most A grouping of related fields of study designed to simplify the process > Aligning programs with meta majors > Legacy course requirements by major >Faculty professional develo”
### `64342f94b78b9578` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/FOIA (sha256 a03ca1f87710)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 2}
  - statements.exceptions: 1 ⟵ “Except as otherwise provided for under the state FOIA provisions, all requests for CHE public records must be made in writing, and must be submitted in person, by mail, or by email.”
  - statements.requirements: 2 ⟵ “Cost: The prorated hourly salary of an employee is determined by dividing that employee’s salary by 1,950 hours (or less if part time) and multiplying that figure by the number of hours required to search for, retrieve and redact the requested records.”
### `6777a8f5a372d4fb` state-SC — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://che.sc.gov/dual-enrollment (sha256 144df9c82468)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Select an institution to transfer to (6-12 months before transfer): Review application deadlines and other pertinent admissions deadlines.”
### `6888a74560469e3a` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/transfer-credit-military-experience (sha256 80891ece8029)
- issues: semantic_review_required
- checks: {"requirements": 10}
  - statements.requirements: 10 ⟵ “Official Joint Services Transcript (JST) displaying military course completions must be requested by the student to be sent directly to Student Records by the issuing agency.”
### `6a31acdabe757e90` state-SC — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://che.sc.gov/regional-contract-program (sha256 3623d39f4a8c)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 4, "guarantees": 1, "requirements": 26}
  - statements.requirements: 26 ⟵ “Students apply for admission and are responsible for tuition at public institutions, but they are not asked to pay an out-of-state fee.”
  - statements.exceptions: 4 ⟵ “However, prior to being admitted as a contract student, they must be certified as a South Carolina resident.”
  - statements.guarantees: 1 ⟵ “Recertification applications will be accepted beginning on Feb. 1 for the upcoming academic year.”
### `731c3298beda12db` state-SC — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.che.sc.gov/sites/che/files/Documents/Institutions%20and%20Educators/Policy%20Program%20Etc/Policies/DualEnrollmentPolicy.pdf (sha256 6e1245742f30)
- issues: semantic_review_required
- checks: {"exceptions": 2, "guarantees": 2, "requirements": 19}
  - statements.requirements: 19 ⟵ “The purpose of these courses is to provide an avenue through which highly talented high school youth can earn college credit while simultaneously meeting high school graduation requirements by taking courses in the high school setting that are offered by an institution of higher education.”
  - statements.exceptions: 2 ⟵ “Documented exceptions may be made for freshman or sophomore students at the request of the high school principal, his or her designee, or the designee of the governing school association.”
  - statements.guarantees: 2 ⟵ “Students enrolled in dual enrollment courses must be guaranteed convenient geographic and electronic access to student and academic support comparable to what is accorded on-campus students, including access to library resources.”
### `7d8308ea9adc4eb5` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/military-credit-transfer (sha256 c8be88a17dc8)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Select an institution (6-12 months before transfer): Review application deadlines and other pertinent admissions deadlines.”
### `85a5b2afe1e5daaf` state-SC — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://che.sc.gov/sites/che/files/Documents/Students%2C%20Families%2C%20Military/Scholarships/SC_Residency_Changes_Cheat_Sheet_2026_KH.pdf (sha256 b447491b1901)
- issues: semantic_review_required
- checks: {"effective": 1, "requirements": 1}
  - statements.effective: 1 ⟵ “Quick Reference Cheat Sheet for Financial Aid, Admissions, and Residency Staff The South Carolina General Assembly approved updates to the Residency Regulations effective May 18, 2026.”
  - statements.requirements: 1 ⟵ “Topic                                           Key Change Residency determinations may now be based on Dependent Residency               one South Carolina resident parent or legal Applicants must demonstrate a minimum number Intent to Establish Residency         of residency intent items.”
### `8d34970cd4e0d5b1` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/sc-residency-information (sha256 a387174adc87)
- issues: semantic_review_required
- checks: {"effective": 1, "exceptions": 1, "requirements": 24}
  - statements.requirements: 24 ⟵ “Under most circumstances, a person must live in South Carolina for 12 consecutive months to establish residency.”
  - statements.exceptions: 1 ⟵ “Members of the military permanently assigned in South Carolina on active duty and their dependents qualify under an exception category.”
  - statements.effective: 1 ⟵ “CHE Residency Regulation for Determination of Rates and Fees - Updated May 2026 (PDF) SC Code of Laws, Section 59-111-10 to 59-111-770 International Sister State Agreements (PDF) Approved VISA classifications for in-state tuition (PDF) Residency for Tuition/Fee and State Scholarship/Grant Purposes o”
### `9fad20e59327db50` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://che.sc.gov/student-scholarship-appeals (sha256 39b9e1537844)
- issues: semantic_review_required
- checks: {"effective": 1, "requirements": 12}
  - statements.requirements: 12 ⟵ “Students wishing to file an appeal must thoroughly read the Appeal Guidelines and submit all materials by the established deadline.”
  - statements.effective: 1 ⟵ “Even if you have previously appealed you will need to submit updated transcripts from all institutions you have attended.”
### `a3198aabb7098343` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/scholarship-enhancement-eligibility-review-seer-approved-programs (sha256 1760deb6b056)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Ed course at the freshman level | 3 | Yes Industrial Engineering (CIP Code 14.3501) | Course Prefix | Course Title | Credit hours | Counts toward 14-credit hour requirement | CHE 111 | General Chemistry 1 | 5 | Yes | CHE 113 | General Chemistry 1 Lab | 0 | Yes | ENGR 121 | Intro to Eng.”
### `b5b5330fd778cb4f` state-SC — state_policies 2021-22 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://che.sc.gov/sites/che/files/Documents/Meetings/Meetings%202023/Transfer%20Covening/Fall%20Transfer%20Convening/Common%20Course%20Learning%20Outcomes.pdf (sha256 3a43f4049175)
- issues: stale_year_label:2021-22, semantic_review_required
- checks: {"effective": 1, "guarantees": 1}
  - statements.guarantees: 1 ⟵ “There are 20 systemwide transfer                 The System supports development of a agreements with 18 institutional partners            guaranteed pathway to all state four-year creating direct pathways to four-year             institutions for Associate in Arts (AA) and degrees for associate deg”
  - statements.effective: 1 ⟵ “Takes Two to Tango: Applying insights from highly-effective transfer partnerships.”
### `bce31f43d9184e31` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/vertical-transfer (sha256 d97ab4c66a69)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Select an institution (6-12 months before transfer): Review application deadlines and other pertinent admissions deadlines.”
### `c5a40d56e704c1fc` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/conduct-student-organizations-tucker-hipps-act (sha256 e48515e3dfd0)
- issues: semantic_review_required
- checks: {"effective": 1, "exceptions": 1, "requirements": 2}
  - statements.exceptions: 1 ⟵ “This legislation requires four-year public institutions in South Carolina, with the exception of the Medical University of South Carolina and The Citadel, to publicly maintain reports of actual findings of misconduct by fraternity and sorority organizations.”
  - statements.requirements: 2 ⟵ “Reports are required to be listed in a prominent location on institutional websites for a period of four years.”
  - statements.effective: 1 ⟵ “Institutions must also notify the CHE within 14 calendar days after reports have been updated.”
### `cdbb26af0a16b264` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/sites/che/files/Documents/Institutions%20and%20Educators/Transfer%20Excellence%20Center/Faculty_Support_Transfer_Convening.pdf (sha256 6b32c0653080)
- issues: semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.requirements: 1 ⟵ “APPLYING CREDITS TO THE MAJOR, OR GEN ED REQUIREMENTS 11.”
  - statements.guarantees: 1 ⟵ “WE DO NOT HAVE THE SYSTEMATIC STRUCTURE TO AWARD CREDITS FOR TRANSFER STUDENTS IN THE MOST EFFICIENT MANNER IF WE DO NOT College Goal: Psychology Major at 4-      Required Course   Transfers to year public university; completed 1st     (Grade)           TTC            TTC Course summer college class”
### `deef056141d9acf7` state-SC — state_policies 2025-26 · policy_kind=tuition_residency [new] (labeled_in_source)
- source: https://che.sc.gov/sites/che/files/Documents/Institutions%20and%20Educators/Academic%20Programs/Memo%20and%20Checklist%20for%20Academic%20Common%20Market%20%20Request%20for%20Certification%20of%20SC%20Residency.pdf (sha256 4d89c07c8f53)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "exceptions": 1, "requirements": 9}
  - statements.requirements: 9 ⟵ “The Request for Certification of South Carolina Residency must be submitted with an official university letter of admission (matriculating student or change of major) on letterhead stating full-time admission to include semester and major (with concentration if applicable), notarized signature(s), s”
  - statements.exceptions: 1 ⟵ “Annual re-certification is not required if the student’s enrollment is continuous, however, if you decide to change your major after certification is completed, you must re-certify under the new major by completing the entire 8.”
  - statements.effective: 1 ⟵ “Since the list of programs offered through the ACM is frequently updated, please visit https://home.sreb.org/acm/choosestate.aspx for the most recent list of eligible programs.”
### `eb48b032b09ef7e2` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/students-families-and-military/military-and-veterans (sha256 b480a0908a3b)
- issues: semantic_review_required
- checks: {"requirements": 9}
  - statements.requirements: 9 ⟵ “Please see below for additional information: Using the GI Bill® for higher education, on-the-job training or apprenticeships GI Bill® benefits help service members, veterans and eligible dependents pay for college, graduate school, and training programs.”
### `ec7341027a9dbc53` state-SC — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://che.sc.gov/sites/che/files/Documents/Institutions%20and%20Educators/CHEApproved_VISA%20Classification%20List_Aug_2025_GH.pdf (sha256 6a7b3a1f46cc)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 1}
  - statements.exceptions: 1 ⟵ “Citizens* L-1  Intra-company transfers, i.e., managers or executives who have worked N-8 Parent of alien child accorded special immigrant status N-9 Child of an alien parent accorded special immigrant status Residency exceptions relating to holders of the above visas are limited to in-state tuition ”
  - statements.requirements: 1 ⟵ “Beyond that date, the holder must either satisfy the marriage stipulation of the K visa or must apply for and receive permanent residency status in order to be eligible for in-state tuition and fees. 803-737-2260                                   www.che.sc.gov”
### `f42c894e099fb4c6` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/academic-common-market (sha256 bcb945c5d4b2)
- issues: semantic_review_required
- checks: {"effective": 1, "requirements": 7}
  - statements.requirements: 7 ⟵ “Eligible programs must be at least 50 percent different in curricular content than programs offered in South Carolina.”
  - statements.effective: 1 ⟵ “Pitts via email or at (803) 856-0037 Update: University of Tennessee-Knoxville discontinues ACM offerings The University of Tennessee-Knoxville announced on Sept. 18, 2024, the removal of all undergraduate degrees from its program inventory effective immediately.”
### `fa314d2917fd976c` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/lateral-transfer (sha256 2a0da8ebc175)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Select an institution (6-12 months before transfer): Review application deadlines and other pertinent admissions deadlines.”
### `fab8174e012246bb` state-SC — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://che.sc.gov/sc-military-credit-mobility-task-force (sha256 3a2d70be6397)
- issues: semantic_review_required
- checks: {"guarantees": 1}
  - statements.guarantees: 1 ⟵ “Also, the advisory board will explore possible ways to increase the use of military credits that will transfer to academic credits, and ultimately towards a certification or degree.”
### `8dea152de7bd61f4` Aiken Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.atc.edu/tuition-aid/financial-aid (sha256 51356b4743f6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Only in unusual circumstances can the Financial Aid Office override this requirement.”
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances would include (a) the student is legally separated from his/her parents (b) the student was removed from the home by state agencies or courts due to physical and/or emotional abuse (c) total family disillusionment exists which makes it impossible to obtain the parent(s) financial information (d) the student is the victim of human trafficking.”
  - sentence: need_based_special_circumstances ⟵ “A student may complete an Unusual Circumstance – Dependency Override Form available on the ATC website Financial Aid Forms page.”
  - sentence: need_based_special_circumstances ⟵ “A student may complete a Special Circumstance – Financial Adjustment Form available on the MyATC Portal.”
### `5162a99f00f3ec56` American College of the Building Arts — appeals 2026-27 [new] (labeled_in_source)
- source: https://acba.edu/financial-aid-1 (sha256 d9967248c3ec)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Important Financial Aid Links Application Process (FAFSA) Master Promissory Note(MPN) & Entrance/Exit Counseling Repay Your Loans ACBA Net Price Calculator Financial Aid Terms and Conditions Virtual Financial Aid Office SC Voter Registration Types of Aid Additional Information Drug Policy Clery Act GPA calculator SAP Appeal American College of the Building Arts 649 Meeting Street Charleston, South”
### `799a6a7eced26e72` Anderson University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://andersonuniversity.edu/admission/outside-scholarships/ (sha256 a50af9ad9e15)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal Students who fail to meet Anderson University’s published Satisfactory Academic Progress (SAP) policy are not eligible for financial aid funds.”
  - sentence: sap_appeal ⟵ “In some circumstances, students who experienced extenuating, documentable circumstances may file an appeal by sending in the completed SAP appeal form along with documentation to the Office of Financial Aid & Scholarships.”
### `46cb6f24489d6426` Bob Jones University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.bju.edu/admission/tuition-aid/financial-aid-process.php (sha256 0243f35b75f3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Some examples of circumstances that may qualify you for a dependency override: The student was a victim of human trafficking.”
### `49e5261b4568b75b` Bob Jones University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.bju.edu/admission/tuition-aid/financial-aid-process.php (sha256 0243f35b75f3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: need_based_special_circumstances ⟵ “What if I have a special or unusual circumstance?”
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstances Some students and their families experience unique circumstances that are not reflected on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “You are still responsible for any outstanding charges or late fines while under a special circumstances or unusual circumstances review.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special circumstances are unforeseen conditions that significantly impact a family's ability to pay for college costs.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances include but are not limited to: Loss or reduction of income Occurrence of one-time income reported on FAFSA Separation or divorce of student’s parents Death of student’s parent(s) Elementary or secondary school tuition costs Paid out-of-pocket medical/dental expenses How to Request a Special Circumstance Review If you believe this may pertain to you, please review our 2025-20”
  - sentence: need_based_special_circumstances ⟵ “You may email our office at [email protected] to specify a category(s) and request a Special Circumstance review.”
### `5e6af1ad4fd1c6bd` Bob Jones University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bju.edu/admission/tuition-aid/documents/sap-undergrad.pdf (sha256 91ebe1ab5a48)
- issues: semantic_review_required, conflicting_sources:https://www.bju.edu/admission/tuition-aid/documents/special-2026.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A reason for an appeal which may include but is not limited to the following: health, family, catastrophe or other special circumstances as determined by the institution. ii An explanation of what has changed that will ensure future academic success. b.”
### `c06150fe23e6d46b` Bob Jones University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.bju.edu/admission/tuition-aid/financial-aid-process.php (sha256 0243f35b75f3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “The financial aid office can use professional judgment to get a more accurate understanding of the student’s circumstances.”
  - sentence: professional_judgment ⟵ “Professional judgment refers to the discretion that the Department of Education gives to financial aid administrators to make adjustments to certain elements of a student's FAFSA because of special or unusual circumstances on a case-by-case basis.”
### `e9f0a9e5d71a202b` Bob Jones University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.bju.edu/admission/tuition-aid/documents/special-2026.pdf (sha256 80c4067b22ec)
- issues: semantic_review_required, conflicting_sources:https://www.bju.edu/admission/tuition-aid/documents/sap-undergrad.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Request 2026–2027 Step 1: Identification of Special Circumstances and Request a Review Review the categories listed below to determine if you may be eligible to submit a request.”
  - sentence: need_based_special_circumstances ⟵ “Step 2: Review Process: Once your initial special circumstance review application has been confirmed, you will receive email instructions for creating an account and completing all required tasks. (NOTE: FAFSA verification* must be completed before the special circumstance is performed.) BJU E-Verification allows you to complete verification and the special circumstance review process from your el”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Explanation Documentation that may be required Loss of Income— Student, spouse or parent(s) has lost employment  Detailed letter explaining special (due to layoff, cut in pay or voluntary resignation) circumstance non-disability related since the tax year reported on the most recent  Copies of 2024 & 2025 Federal Tax unemployment FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Medical and/or dental You or your parents paid medical or  Detailed letter explaining special circumstance expenses (If paid expenses dental expenses not covered by  Proof of payment of out-of-pocket medical or dental insurance or paid through a expenses, including premiums paid in 2024 or 2025 exceed 11% of Adjusted healthshare program during the most  Examples of proof of payments may include”
### `cc6ddd823e1aa7c9` Bob Jones University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bju.edu/admission/tuition-aid/tuition-2526.php (sha256 85586bb036b9)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - column:Tuition per semester (8–12 credits): 4250 ⟵ “Tuition per semester (8–12 credits) | $4,250”
  - column:MDiv Tuition per semester (8–12 credits): 3150 ⟵ “MDiv Tuition per semester (8–12 credits) | $3,150”
  - column:Room and Board per semester: 4250 ⟵ “Room and Board per semester | $4,250”
  - column:Room and Board (value plan): 3745 ⟵ “Room and Board (value plan) | $3,745”
  - column:Program Fee per semester: 275 ⟵ “Program Fee per semester | $275”
### `f9fc18ed71a90176` Bob Jones University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bju.edu/admission/tuition-aid/tuition-2425.php (sha256 1b0c0b1c7fd7)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "rows": 6}
  - column:Tuition per semester (8–12 credits): 4250 ⟵ “Tuition per semester (8–12 credits) | $4,250”
  - column:MDiv Tuition per semester (8–12 credits): 3070 ⟵ “MDiv Tuition per semester (8–12 credits) | $3,070”
  - column:Room and Board per semester: 4170 ⟵ “Room and Board per semester | $4,170”
  - column:Room and Board (value plan): 3670 ⟵ “Room and Board (value plan) | $3,670”
  - column:Program Fee per semester: 250 ⟵ “Program Fee per semester | $250”
  - column:Program Fee per semester (2): 250 ⟵ “Program Fee per semester | $250”
### `0c4b7386dd1a5123` Charleston Southern University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/faqs/ (sha256 ca9c25d00709)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “For example, you may have a drastic change in household income, or you may get married —these changes affect your financial situation and your eligibility and should be included on your FAFSA each year.”
  - sentence: need_based_special_circumstances ⟵ “If a student or family member recently lost a job or experienced financial hardship due to death, divorce, or unexpected medical expenses, please contact the Financial Aid Office to discuss the Special Circumstance process.”
  - sentence: need_based_special_circumstances ⟵ “Requesting a review of Special Circumstances does not guarantee a change in aid.”
### `7ff8d5d564bf4ab4` Charleston Southern University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/faqs/ (sha256 ca9c25d00709)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students that have attempted over 150 credit hours will need to submit the Satisfactory Academic Progress Appeal, regardless of GPA or credit hours attempted versus earned (67%).” SAP evaluations occur at the conclusion of every spring semester, appeals are considered on an individual basis, and the student is notified in writing of the committee’s decision.”
  - sentence: sap_appeal ⟵ “SAP appeals must be submitted no later than 10 working days after the end of the summer session for the fall semester.”
### `4d25c1f188ee5ada` Charleston Southern University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.charlestonsouthern.edu/programs/doctor-of-physical-therapy-dpt/cost-aid/ (sha256 2a64e6fcb001)
- issues: conflicting_sources:https://www.charlestonsouthern.edu/admissions/financial-aid/
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 33000 ⟵ “Tuition | $11,000 | $33,000”
  - column:Technology Fee: 250 ⟵ “Technology Fee | $125 | $250”
  - column:Lab Fee: 750 ⟵ “Lab Fee | – | $750”
  - column:Program Fee*: 1300 ⟵ “Program Fee* | – | $1,300”
  - column:Total Direct Cost:: 35300 ⟵ “Total Direct Cost: | $11,125 | $35,300”
### `765f78d0c81cb66c` Charleston Southern University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.charlestonsouthern.edu/admissions/financial-aid/ (sha256 b247ad4c425d)
- issues: conflicting_sources:https://www.charlestonsouthern.edu/programs/doctor-of-physical-therapy-dpt/cost-aid/
- checks: {"columns": 1, "rows": 7}
  - column:Tuition*: 34270 ⟵ “Tuition* | $34,270”
  - column:Fees*: 800 ⟵ “Fees* | $800”
  - column:Housing*: 10426 ⟵ “Housing* | $10,426”
  - column:Food*: 3548 ⟵ “Food* | $3,548”
  - column:Transportation**: 1190 ⟵ “Transportation** | $1,190”
  - column:Personal Expenses**: 2020 ⟵ “Personal Expenses** | $2,020”
  - column:Yearly Total: 52254 ⟵ “Yearly Total | $52,254”
### `46dcb504e2439c92` Charleston Southern University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.charlestonsouthern.edu/wp-content/uploads/CLEP-POLICY-Updated-Jan-2025.pdf (sha256 7aa178c08808)
- issues: credits_implausible
- checks: {"distinct_exams": 21, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|3]:  ⟵ “American Literature                            3              46              50       English 202”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|3]:  ⟵ “Analyzing & Interpreting Literature            3              47              50       Composition, credit”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|3]:  ⟵ “College Composition (not Modular)              3              44              50       English 111”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature                             3              46              50       English 203”
  - equivalencies[CLEP-HUMANITIES|6]:  ⟵ “Humanities                                     6             420              50       Art 202 & General Elective”
  - equivalencies[CLEP-FRENCH-LANGUAGE|6]:  ⟵ “French, Level 1                                6              42              50       French 101 & 102”
  - equivalencies[CLEP-GERMAN-LANGUAGE|6]:  ⟵ “German, Level 1                                6              36              50       German 101 & 102”
  - equivalencies[CLEP-SPANISH-LANGUAGE|6]:  ⟵ “Spanish, Level 1                               6              45              50       Spanish 101 & 102”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|6]:  ⟵ “Spanish with Writing, Level 1                  6              45              50       Spanish 101 & 102”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government                           3   47    50   Political Science 201”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|3]:  ⟵ “Human Growth & Dev.                           3   45    50   General Elective”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|3]:  ⟵ “Intro. to Educational Psychology              3   47    50”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Principles of Macroeconomics                  3   44    50   Economics 212”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3]:  ⟵ “Principles of Microeconomics                  3   41    50   Economics 211”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Introductory Psychology                       3   47    50   Psychology 110”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|3]:  ⟵ “Introductory Sociology                        3   47    50   Sociology 101”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|6]:  ⟵ “Social Sciences & History                     6   420   50   General Electives”
  - equivalencies[CLEP-PRECALCULUS|4]:  ⟵ “Precalculus                                   4   n/a   50   Mathematics 130”
  - equivalencies[CLEP-BIOLOGY|6]:  ⟵ “General Biology                               6   46    50   General Electives (No Lab)”
  - equivalencies[CLEP-CHEMISTRY|6]:  ⟵ “General Chemistry                             6   50    50   General Electives (No Lab)”
  - equivalencies[CLEP-NATURAL-SCIENCES|6]:  ⟵ “Natural Sciences                              6   420   50   General Electives”
### `d33edc1821d65c5e` Citadel Military College of South Carolina — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.citadel.edu/financial-aid/cost-of-attendance/ (sha256 7a6ab0628fcc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustment Policy (opens in a new tab) The Federal Financial Aid Cost of Attendance Budget (COA) factors in an allowance for books, supplies, transportation, and miscellaneous personal expenses.”
  - sentence: budget_increase ⟵ “The following expenses can be considered for a cost of attendance adjustment: Book, course material, supply, and equipment costs that exceed the amount included in the cost of attendance.”
  - sentence: budget_increase ⟵ “The following expenses will not be considered for a cost of attendance adjustment: Consumer bills (ie: cell phone, car payment, insurance, utilities, etc.) Costs associated with outstanding consumer debt Off-campus living expenses that exceed amount provided for housing Food and on-campus meal expenses for off-campus students Relocation expenses / expenses to travel to campus Interview expenses Cl”
### `35fe0c9c2df344f5` Citadel Military College of South Carolina — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.citadel.edu/financial-aid/cost-of-attendance/ (sha256 7a6ab0628fcc)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - on_campus:Tuition & Fees: 13320 ⟵ “Tuition & Fees | $13,320 | $40,587”
  - on_campus:Living Expenses (Housing/Food): 22787 ⟵ “Living Expenses (Housing/Food) | $22,787 | $22,787”
  - on_campus:Books & Supplies: 1049 ⟵ “Books & Supplies | $1,049 | $1,049”
  - on_campus:Travel: 3090 ⟵ “Travel | $3,090 | $3,090”
  - on_campus:Personal: 5578 ⟵ “Personal | $5,578 | $5,578”
  - on_campus:Loan Fees: 62 ⟵ “Loan Fees | $62 | $62”
  - on_campus:Total COA: 45887 ⟵ “Total COA | $45,887 | $73,154”
### `52e75cbd86e2952d` Citadel Military College of South Carolina — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.citadel.edu/financial-aid/cost-of-attendance/ (sha256 7a6ab0628fcc)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 14390 ⟵ “Tuition & Fees | $14,390 | $14,290”
  - column:Living Expenses (Housing/Food): 10899 ⟵ “Living Expenses (Housing/Food) | $10,899 | $10,899”
  - column:Books & Supplies (OneCard): 9300 ⟵ “Books & Supplies (OneCard) | $9,300 | $3,124”
  - column:Travel: 2363 ⟵ “Travel | $2,363 | $2,363”
  - column:Personal: 2320 ⟵ “Personal | $2,320 | $2,320”
  - column:Loan Fees: 62 ⟵ “Loan Fees | $62 | $62”
  - column:Total COA: 39334 ⟵ “Total COA | $39,334 | $33,058”
  - column:Tuition & Fees: 14290 ⟵ “Tuition & Fees | $14,390 | $14,290”
  - column:Living Expenses (Housing/Food): 10899 ⟵ “Living Expenses (Housing/Food) | $10,899 | $10,899”
  - column:Books & Supplies (OneCard): 3124 ⟵ “Books & Supplies (OneCard) | $9,300 | $3,124”
  - column:Travel: 2363 ⟵ “Travel | $2,363 | $2,363”
  - column:Personal: 2320 ⟵ “Personal | $2,320 | $2,320”
  - column:Loan Fees: 62 ⟵ “Loan Fees | $62 | $62”
  - column:Total COA: 33058 ⟵ “Total COA | $39,334 | $33,058”
### `9ed8870b9dc10482` Citadel Military College of South Carolina — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.citadel.edu/financial-aid/cost-of-attendance/ (sha256 7a6ab0628fcc)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - on_campus:Tuition & Fees: 40587 ⟵ “Tuition & Fees | $13,320 | $40,587”
  - on_campus:Living Expenses (Housing/Food): 22787 ⟵ “Living Expenses (Housing/Food) | $22,787 | $22,787”
  - on_campus:Books & Supplies: 1049 ⟵ “Books & Supplies | $1,049 | $1,049”
  - on_campus:Travel: 3090 ⟵ “Travel | $3,090 | $3,090”
  - on_campus:Personal: 5578 ⟵ “Personal | $5,578 | $5,578”
  - on_campus:Loan Fees: 62 ⟵ “Loan Fees | $62 | $62”
  - on_campus:Total COA: 73154 ⟵ “Total COA | $45,887 | $73,154”
### `5d11aa4ee07d9411` Citadel Military College of South Carolina — credit_policies 2026-27 · policy_kind=AP [new] (ambiguous_year_labels)
- source: https://www.citadel.edu/registrar/credit-by-examination/advanced-placement-ap/ (sha256 1f35c0150b3e)
- issues: ambiguous_year_labels
- checks: {"distinct_exams": 36, "equivalencies": 43, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Drawing | 3 | FNAR 304 | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | FNAR 206 | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101, 111 or BIOL 130, 131** | 4”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 101, 111, 102, 112 or BIOL 130, 131, 140, 141** | 8”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH 131 | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC (3) | 3 | MATH 119 and MATH 131 | 8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 103, 113 or CHEM 151, 161** | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 103, 113, 104, 114 or CHEM 151, 161, 152, 162** | 8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | CHIN 101 | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture | 4 | CHIN 101, 102 | 6”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics | 3 | PSCI 232 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CSCI 201, 211 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | CSCI 210 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|English Language & Composition]:  ⟵ “Computer Science Principles | English Language & Composition | *”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | BIOL 209 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 103, 104 | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | FREN 101, 102 | 6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture | 3 | GERM 101, 102 | 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 209 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language & Culture | 3 | GNRL 101 | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|4]:  ⟵ “Italian Language & Culture | 4 | GNRL 101, 102 | 6”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language & Culture | 3 | JAPN 101 | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4]:  ⟵ “Japanese Language & Culture | 4 | JAPN 101, 102 | 6”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin | 3 | GNRL 101 | 3”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin | 4 | GNRL 101, 102 | 6”
  - … 18 more rows
### `7816508933f90bd4` Citadel Military College of South Carolina — credit_policies 2026-27 · policy_kind=IB [new] (ambiguous_year_labels)
- source: https://www.citadel.edu/registrar/credit-by-examination/international-baccalaureate-ib/ (sha256 336f339c4733)
- issues: ambiguous_year_labels
- checks: {"distinct_exams": 22, "equivalencies": 47, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|4]:  ⟵ “Biology HL | 4 | BIOL 101, 111 or BIOL 130, 131* | 4”
  - equivalencies[IB-BIOLOGY-HL|5]:  ⟵ “Biology HL | 5 | BIOL 101, 111, 102, 112 or BIOL 130, 131, 140, 141* | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|4]:  ⟵ “Business & Management HL | 4 | MGMT 303 | 3”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|5]:  ⟵ “Business & Management HL | 5 | GNRL 101, 102, 103 | 9”
  - equivalencies[IB-CHEMISTRY-HL|4]:  ⟵ “Chemistry HL | 4 | CHEM 103, 113 or CHEM 151, 161* | 4”
  - equivalencies[IB-CHEMISTRY-HL|5]:  ⟵ “Chemistry HL | 5 | CHEM 103, 113, 104, 114 or CHEM 151, 161, 152, 162* | 8”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|4]:  ⟵ “Computer Science HL | 4 | CSCI 290 | 3”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|5]:  ⟵ “Computer Science HL | 5 | GNRL 101, 102, 103 | 9”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | 4 | ECON 201 | 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|4]:  ⟵ “English A: Language & Literature HL | 4 | ENGL 101 | 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|5]:  ⟵ “English A: Language & Literature HL | 5 | ENGL 101, 102 | 6”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|4]:  ⟵ “English A: Literature HL | 4 | ENGL 101 | 3”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|5]:  ⟵ “English A: Literature HL | 5 | ENGL 101, 102 | 6”
  - equivalencies[IB-FILM-HL|4]:  ⟵ “Film HL | 4 | ENGL 209 | 3”
  - equivalencies[IB-FILM-HL|5]:  ⟵ “Film HL | 5 | GNRL 101, 102, 103 | 9”
  - equivalencies[IB-FRENCH-HL|4]:  ⟵ “French A: Language & Literature HL | 4 | FREN 101, 102 | 6”
  - equivalencies[IB-FRENCH-HL|5]:  ⟵ “French A: Language & Literature HL | 5 | FREN 101, 102, 201 | 9”
  - equivalencies[IB-FRENCH-HL|7]:  ⟵ “French A: Language & Literature HL | 7 | FREN 101, 102, 201, 202, 302 | 15”
  - equivalencies[IB-GEOGRAPHY-HL|4]:  ⟵ “Geography HL | 4 | GEOG 209 | 3”
  - equivalencies[IB-GEOGRAPHY-HL|5]:  ⟵ “Geography HL | 5 | GNRL 101, 102, 103 | 9”
  - equivalencies[IB-GERMAN-HL|4]:  ⟵ “German A: Language & Literature HL | 4 | GERM 101, 102 | 6”
  - equivalencies[IB-GERMAN-HL|5]:  ⟵ “German A: Language & Literature HL | 5 | GERM 101, 102, 201 | 9”
  - equivalencies[IB-GERMAN-HL|7]:  ⟵ “German A: Language & Literature HL | 7 | GERM 101, 102, 201, 202, 302 | 15”
  - equivalencies[IB-GLOBAL-POLITICS-HL|4]:  ⟵ “Global Politics HL | 4 | PSCI 231 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-HL|5]:  ⟵ “Global Politics HL | 5 | GNRL 101, 102, 103 | 9”
  - … 22 more rows
### `a687a5b8c4bc0c0b` Citadel Military College of South Carolina — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.citadel.edu/registrar/credit-by-examination/clep/ (sha256 8abffd40403e)
- issues: ambiguous_year_labels
- checks: {"distinct_exams": 33, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | LDRS 202 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL 215 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | ENGL 208 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL 105, 115 | 4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH 106 | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM 151/161 | 4”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 104 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL 101 AND 102 | 6”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | ENGL 101 | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MATH 105 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL 201 or 202 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT 201 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Level I | 50 | FREN 101, 102 | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Level II | 59 | FREN 101, 102, 201, 202 | 12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Level I | 50 | GERM 101, 102 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Level II | 60 | GERM 101, 102, 201, 202 | 12”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | HIST 201 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | HIST 202 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSYC 202 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | FNAR 206 AND (ENGL 208 or FNAR 205) | 6”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | CSCI 110 or MGMT 421 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology | 50 | GNRL 101 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BLAW 301 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSYC 201 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOCI 201 | 3”
  - … 11 more rows
### `bc048da27b30aa6f` Claflin University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.claflin.edu/admissions-aid/financial-aid/financial-aid-checklist (sha256 94b1be26c083)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you financial aid is suspended for not meeting satisfactory academic progress, you will have the right to appeal and may do so by writing the Office of Student Financial Aid.”
### `539ede40ca69e3de` Claflin University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.claflin.edu/docs/default-source/tuition/rn-to-bsn-program-brochure-25-26-dated-3-26-2025.pdf?sfvrsn=40e70a0e_0 (sha256 23e4eeeb720a)
- issues: arrangement_unlabeled, stale_year_label:2025-26
- checks: {"columns": 4, "rows": 8}
  - column:Tuition: 1446.0 ⟵ “Tuition | $1,446.00 | 2,892.00 | $4,337.00 | $5,311.00”
  - column:Technology Fee: 172.0 ⟵ “Technology Fee | 172.00 | 172.00 | 172.00 | 172.00”
  - column:$1,618.00: 3064.0 ⟵ “$1,618.00 | $3,064.00 | $4,509.00 | $5,483.00”
  - column:Application Fee: 50.0 ⟵ “Application Fee | $ 50.00 | drops after the first due date.”
  - column:(International Application Fee): 75.0 ⟵ “(International Application Fee) | $ 75.00”
  - column:Deferred Payment Plan: 50.0 ⟵ “Deferred Payment Plan | $ 50.00 | • | 1st Payment Due - June 1, 2025”
  - column:Late Registration Fee: 60.0 ⟵ “Late Registration Fee | $ 60.00”
  - column:Replacement Degree: 45.0 ⟵ “Replacement Degree | $ 45.00 | • | 1st Payment Due - December 1, 2025”
  - column:Tuition: 2892.0 ⟵ “Tuition | $1,446.00 | 2,892.00 | $4,337.00 | $5,311.00”
  - column:Technology Fee: 172.0 ⟵ “Technology Fee | 172.00 | 172.00 | 172.00 | 172.00”
  - column:$1,618.00: 4509.0 ⟵ “$1,618.00 | $3,064.00 | $4,509.00 | $5,483.00”
  - column:Tuition: 4337.0 ⟵ “Tuition | $1,446.00 | 2,892.00 | $4,337.00 | $5,311.00”
  - column:Technology Fee: 172.0 ⟵ “Technology Fee | 172.00 | 172.00 | 172.00 | 172.00”
  - column:$1,618.00: 5483.0 ⟵ “$1,618.00 | $3,064.00 | $4,509.00 | $5,483.00”
  - column:Tuition: 5311.0 ⟵ “Tuition | $1,446.00 | 2,892.00 | $4,337.00 | $5,311.00”
  - column:Technology Fee: 172.0 ⟵ “Technology Fee | 172.00 | 172.00 | 172.00 | 172.00”
### `b2920de5c3407828` Claflin University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.claflin.edu/docs/default-source/tuition/rn-to-bsn-program-brochure-24-25-dated-6-24-2024.pdf?sfvrsn=5e89090e_0 (sha256 a454207fb817)
- issues: arrangement_unlabeled, stale_year_label:2024-25
- checks: {"columns": 4, "rows": 8}
  - column:Tuition: 1377.0 ⟵ “Tuition | $1,377.00 | 2,754.00 | $4,131.00 | $5,508.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:$1,541.00: 2918.0 ⟵ “$1,541.00 | $2,918.00 | $4,295.00 | $5,672.00”
  - column:Application Fee: 50.0 ⟵ “Application Fee | $ 50.00 | May be utilized to cover charges after all financial aid”
  - column:(International Application Fee ): 75.0 ⟵ “(International Application Fee ) | $ 75.00 | has been applied. There will be a $50.00 fee”
  - column:Deferred Payment Plan: 50.0 ⟵ “Deferred Payment Plan | $ 50.00 | drops to two payments after the first due date.”
  - column:Late Registration Fee: 60.0 ⟵ “Late Registration Fee | $ 60.00”
  - column:Replacement Degree: 45.0 ⟵ “Replacement Degree | $ 45.00”
  - column:Tuition: 2754.0 ⟵ “Tuition | $1,377.00 | 2,754.00 | $4,131.00 | $5,508.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:$1,541.00: 4295.0 ⟵ “$1,541.00 | $2,918.00 | $4,295.00 | $5,672.00”
  - column:Tuition: 4131.0 ⟵ “Tuition | $1,377.00 | 2,754.00 | $4,131.00 | $5,508.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:$1,541.00: 5672.0 ⟵ “$1,541.00 | $2,918.00 | $4,295.00 | $5,672.00”
  - column:Tuition: 5508.0 ⟵ “Tuition | $1,377.00 | 2,754.00 | $4,131.00 | $5,508.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
### `c5fc07057e207fb0` Claflin University — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.claflin.edu/docs/default-source/tuition/2023---2024-online-programs-brochure.pdf?sfvrsn=635e080e_0 (sha256 063b71805480)
- issues: arrangement_unlabeled, stale_year_label:2023-24, conflicting_sources:https://www.claflin.edu/docs/default-source/tuition/2023---2024-masters's-in-nursing-online-brochure.pdf?sfvrsn=765e080e_0
- checks: {"columns": 4, "rows": 9}
  - column:Tuition: 1686.0 ⟵ “Tuition | $1,686.00 | $3,372.00 | $5,058.00 | $6,744.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:Book Fee: 166.0 ⟵ “Book Fee | 166.00 | 166.00 | 166.00 | 366.00”
  - column:$2,016.00: 3702.0 ⟵ “$2,016.00 | $3,702.00 | $5,388.00 | $7,274.00”
  - column:Application Fee: 50.0 ⟵ “Application Fee | $ 50.00 | May be utilized to cover charges after all financial aid”
  - column:(International Application Fee ): 75.0 ⟵ “(International Application Fee ) | $ 75.00 | has been applied. There will be a $50.00 fee”
  - column:Deferred Payment Plan: 50.0 ⟵ “Deferred Payment Plan | $ 50.00 | drops to two payments after the first due date.”
  - column:Late Registration Fee: 60.0 ⟵ “Late Registration Fee | $ 60.00 | · 3rd Payment Due — October 13, 2023”
  - column:Replacement Degree: 45.0 ⟵ “Replacement Degree | $ 45.00”
  - column:Tuition: 3372.0 ⟵ “Tuition | $1,686.00 | $3,372.00 | $5,058.00 | $6,744.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:Book Fee: 166.0 ⟵ “Book Fee | 166.00 | 166.00 | 166.00 | 366.00”
  - column:$2,016.00: 5388.0 ⟵ “$2,016.00 | $3,702.00 | $5,388.00 | $7,274.00”
  - column:Tuition: 5058.0 ⟵ “Tuition | $1,686.00 | $3,372.00 | $5,058.00 | $6,744.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:Book Fee: 166.0 ⟵ “Book Fee | 166.00 | 166.00 | 166.00 | 366.00”
  - column:$2,016.00: 7274.0 ⟵ “$2,016.00 | $3,702.00 | $5,388.00 | $7,274.00”
  - column:Tuition: 6744.0 ⟵ “Tuition | $1,686.00 | $3,372.00 | $5,058.00 | $6,744.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:Book Fee: 366.0 ⟵ “Book Fee | 166.00 | 166.00 | 166.00 | 366.00”
### `feed95ee71a900b4` Claflin University — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.claflin.edu/docs/default-source/tuition/2023---2024-masters's-in-nursing-online-brochure.pdf?sfvrsn=765e080e_0 (sha256 96af2eec822c)
- issues: arrangement_unlabeled, stale_year_label:2023-24, conflicting_sources:https://www.claflin.edu/docs/default-source/tuition/2023---2024-online-programs-brochure.pdf?sfvrsn=635e080e_0
- checks: {"columns": 4, "rows": 10}
  - column:Tuition: 1686.0 ⟵ “Tuition | $1,686.00 | $3,372.00 | $5,058.00 | $6,744.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:FNP Fee: 250.0 ⟵ “FNP Fee | 250.00 | 250.00 | 250.00 | 250.00”
  - column:Book Fee: 166.0 ⟵ “Book Fee | 166.00 | 166.00 | 166.00 | 366.00”
  - column:$2,266.00: 3952.0 ⟵ “$2,266.00 | $3,952.00 | $5,638.00 | $7,524.00”
  - column:Application Fee: 50.0 ⟵ “Application Fee | $ 50.00 | May be utilized to cover charges after all financial aid”
  - column:(International Application Fee ): 75.0 ⟵ “(International Application Fee ) | $ 75.00 | has been applied. There will be a $50.00 fee”
  - column:Deferred Payment Plan: 50.0 ⟵ “Deferred Payment Plan | $ 50.00 | drops to two payments after the first due date.”
  - column:Late Registration Fee: 60.0 ⟵ “Late Registration Fee | $ 60.00 | · 3rd Payment Due — October 13, 2023”
  - column:Replacement Degree: 45.0 ⟵ “Replacement Degree | $ 45.00”
  - column:Tuition: 3372.0 ⟵ “Tuition | $1,686.00 | $3,372.00 | $5,058.00 | $6,744.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:FNP Fee: 250.0 ⟵ “FNP Fee | 250.00 | 250.00 | 250.00 | 250.00”
  - column:Book Fee: 166.0 ⟵ “Book Fee | 166.00 | 166.00 | 166.00 | 366.00”
  - column:$2,266.00: 5638.0 ⟵ “$2,266.00 | $3,952.00 | $5,638.00 | $7,524.00”
  - column:Tuition: 5058.0 ⟵ “Tuition | $1,686.00 | $3,372.00 | $5,058.00 | $6,744.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:FNP Fee: 250.0 ⟵ “FNP Fee | 250.00 | 250.00 | 250.00 | 250.00”
  - column:Book Fee: 166.0 ⟵ “Book Fee | 166.00 | 166.00 | 166.00 | 366.00”
  - column:$2,266.00: 7524.0 ⟵ “$2,266.00 | $3,952.00 | $5,638.00 | $7,524.00”
  - column:Tuition: 6744.0 ⟵ “Tuition | $1,686.00 | $3,372.00 | $5,058.00 | $6,744.00”
  - column:Technology Fee: 164.0 ⟵ “Technology Fee | 164.00 | 164.00 | 164.00 | 164.00”
  - column:FNP Fee: 250.0 ⟵ “FNP Fee | 250.00 | 250.00 | 250.00 | 250.00”
  - column:Book Fee: 366.0 ⟵ “Book Fee | 166.00 | 166.00 | 166.00 | 366.00”
### `65df36aa3df9ee03` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html (sha256 80a0d8c93ea8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “As part of the appeal, you must clearly document the reasons beyond your control that contributed to not meeting the renewal requirements of your scholarship(s). **University scholarship appeals are reviewed during the Fall semester each academic year.”
  - sentence: scholarship_retention_appeal ⟵ “The scholarship appeal form and supporting documents must be submitted by the last day to register or add a class.”
  - sentence: scholarship_retention_appeal ⟵ “University Scholarship Appeal Form State of South Carolina Scholarship Appeals To appeal the loss of a state scholarship (Palmetto Fellows or LIFE), you must appeal directly to the South Carolina Commission on Higher Education (CHE) as Clemson University does not have the authority to make exceptions to state legislation and/or regulations.”
### `b520bcd13dadc8a1` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html (sha256 80a0d8c93ea8)
- issues: semantic_review_required, conflicting_sources:https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/maintain-your-eligibility/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have extenuating circumstances or a significant change in financial status since you filed the FAFSA, you can submit the need-based appeal form to the financial aid office and request a review.”
### `cf9d2323f5da6b39` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/maintain-your-eligibility/ (sha256 fe93904928b2)
- issues: semantic_review_required, conflicting_sources:https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals can be filed based on academic improvement, death of a family member/close friend, injury or illness of the student, or other special circumstances.”
### `f79c018c1c4eefa8` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/maintain-your-eligibility/ (sha256 fe93904928b2)
- issues: semantic_review_required, conflicting_sources:https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “MCGPR Needed by Credit Hour | Total Attempted Credit Hours | MCGPR | 89 or less | 1.85 | 90+ | 2.00 | Graduate Students | 3.00 Undergraduate Resources for Satisfactory Academic Progress Graduate Resources for Satisfactory Academic Progress Appeal Your SAP Status If you are not maintaining SAP, you can appeal your status using the appeal form and instructions.”
  - sentence: sap_appeal ⟵ “SAP APPEAL PRIORITY DEADLINES Fall Term: July 30 Spring Term: November 30 Summer Term: April 30 To be considered, your appeal must explain why you failed to make SAP and what has changed that will allow you to meet SAP standards at the next evaluation.”
### `fc81053fa74a5b3d` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html (sha256 80a0d8c93ea8)
- issues: semantic_review_required, conflicting_sources:https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/maintain-your-eligibility/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Need-Based Appeal Form Satisfactory Academic Progress Appeals If you have received notice that you are ineligible for financial aid because of a failure to maintain Satisfactory Academic Progress, you can submit an appeal to the Financial Aid Appeals Committee.”
  - sentence: sap_appeal ⟵ “To appeal, you must submit the Satisfactory Academic Progress Appeal Form, a detailed letter documenting the extenuating circumstances for why the deficiency has occurred, actions you have taken to resolve the issue and any supporting documentation.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Scholarship Appeals Clemson University Scholarship Appeals To appeal the loss of a University scholarship, you must submit the scholarship appeal form, letter and supporting documents to the Office of Scholarships.”
### `74162819fde81e9c` Clemson University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.clemson.edu/financial-aid/cost/estimated-cost-of-attendance.html (sha256 4bd3aa727641)
- issues: multiple_total_rows
- checks: {"columns": 2, "rows": 10}
  - off_campus_not_with_family:Tuition: 14038 ⟵ “Tuition | $14,038 | $14,038”
  - off_campus_not_with_family:Fees(2): 1832 ⟵ “Fees(2) | $1,832 | $1,832”
  - off_campus_not_with_family:Books, Supplies & Course Materials(6): 1576 ⟵ “Books, Supplies & Course Materials(6) | $1,576 | $1,576”
  - off_campus_not_with_family:Housing(3): 9304 ⟵ “Housing(3) | $9,304 | $2,023”
  - off_campus_not_with_family:Food(4): 5576 ⟵ “Food(4) | $5,576 | $2,023”
  - off_campus_not_with_family:Transportation: 1320 ⟵ “Transportation | $1,320 | $3,672”
  - off_campus_not_with_family:Personal: 4484 ⟵ “Personal | $4,484 | $4,484”
  - off_campus_not_with_family:Loan Fees(5): 68 ⟵ “Loan Fees(5) | $68 | $68”
  - off_campus_not_with_family:TOTAL: 38198 ⟵ “TOTAL | $38,198 | $29,716”
  - off_campus_not_with_family:Total with laptop(6): 40722 ⟵ “Total with laptop(6) | $40,722 | $32,240”
  - with_parents_or_family:Tuition: 14038 ⟵ “Tuition | $14,038 | $14,038”
  - with_parents_or_family:Fees(2): 1832 ⟵ “Fees(2) | $1,832 | $1,832”
  - with_parents_or_family:Books, Supplies & Course Materials(6): 1576 ⟵ “Books, Supplies & Course Materials(6) | $1,576 | $1,576”
  - with_parents_or_family:Housing(3): 2023 ⟵ “Housing(3) | $9,304 | $2,023”
  - with_parents_or_family:Food(4): 2023 ⟵ “Food(4) | $5,576 | $2,023”
  - with_parents_or_family:Transportation: 3672 ⟵ “Transportation | $1,320 | $3,672”
  - with_parents_or_family:Personal: 4484 ⟵ “Personal | $4,484 | $4,484”
  - with_parents_or_family:Loan Fees(5): 68 ⟵ “Loan Fees(5) | $68 | $68”
  - with_parents_or_family:TOTAL: 29716 ⟵ “TOTAL | $38,198 | $29,716”
  - with_parents_or_family:Total with laptop(6): 32240 ⟵ “Total with laptop(6) | $40,722 | $32,240”
### `8350345feed747b2` Clemson University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.clemson.edu/financial-aid/cost/estimated-cost-of-attendance.html (sha256 4bd3aa727641)
- issues: multiple_total_rows
- checks: {"columns": 2, "rows": 10}
  - off_campus_not_with_family:Tuition: 42020 ⟵ “Tuition | $42,020 | $42,020”
  - off_campus_not_with_family:Fees(2): 1832 ⟵ “Fees(2) | $1,832 | $1,832”
  - off_campus_not_with_family:Books, Supplies & Course Materials(6): 1576 ⟵ “Books, Supplies & Course Materials(6) | $1,576 | $1,576”
  - off_campus_not_with_family:Housing(3): 9304 ⟵ “Housing(3) | $9,304 | $2,023”
  - off_campus_not_with_family:Food(4): 5576 ⟵ “Food(4) | $5,576 | $2,023”
  - off_campus_not_with_family:Transportation: 1320 ⟵ “Transportation | $1,320 | $3,672”
  - off_campus_not_with_family:Personal: 4484 ⟵ “Personal | $4,484 | $4,484”
  - off_campus_not_with_family:Loan Fees(5): 68 ⟵ “Loan Fees(5) | $68 | $68”
  - off_campus_not_with_family:TOTAL: 66180 ⟵ “TOTAL | $66,180 | $57,698”
  - off_campus_not_with_family:Total with laptop(6): 68704 ⟵ “Total with laptop(6) | $68,704 | $60,222”
  - with_parents_or_family:Tuition: 42020 ⟵ “Tuition | $42,020 | $42,020”
  - with_parents_or_family:Fees(2): 1832 ⟵ “Fees(2) | $1,832 | $1,832”
  - with_parents_or_family:Books, Supplies & Course Materials(6): 1576 ⟵ “Books, Supplies & Course Materials(6) | $1,576 | $1,576”
  - with_parents_or_family:Housing(3): 2023 ⟵ “Housing(3) | $9,304 | $2,023”
  - with_parents_or_family:Food(4): 2023 ⟵ “Food(4) | $5,576 | $2,023”
  - with_parents_or_family:Transportation: 3672 ⟵ “Transportation | $1,320 | $3,672”
  - with_parents_or_family:Personal: 4484 ⟵ “Personal | $4,484 | $4,484”
  - with_parents_or_family:Loan Fees(5): 68 ⟵ “Loan Fees(5) | $68 | $68”
  - with_parents_or_family:TOTAL: 57698 ⟵ “TOTAL | $66,180 | $57,698”
  - with_parents_or_family:Total with laptop(6): 60222 ⟵ “Total with laptop(6) | $68,704 | $60,222”
### `f69c9f616c305c94` Clemson University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.clemson.edu/admissions/undergraduate-admissions/apply/credit-transfer.html (sha256 e152d177b820)
- issues: rows_without_score
- checks: {"distinct_exams": 36, "equivalencies": 37, "rows_without_score": 37}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “African American Studies | African American Studies | 3, 4, 5 | GBS 1000 | 3”
  - equivalencies[AP-RESEARCH|None]:  ⟵ “Capstone | Research | 3, 4, 5 | ELEC 00013 | 3”
  - equivalencies[AP-SEMINAR|None]:  ⟵ “ | Seminar | 3, 4, 5 | ELEC 00013 | 3”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Economics | Microeconomics | 3, 4, 5 | ECON 2110 | 3”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “ | Macroeconomics | 3, 4, 5 | ECON 2120 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Geography | Human Geography | 3, 4, 5 | GEOG 1010 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “History | United States History | 3 | HIST 1010 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “ | United States History | 4, 5 | HIST 1010, 1020 | 6”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “ | European History | 3, 4, 5 | HIST 1730 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|None]:  ⟵ “ | World History | 3, 4, 5 | HIST 19995 | 3”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “Humanities | Music Theory | 3, 4, 5 | MUSC 1420, 1430 | 4”
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “ | Art History | 3, 4, 5 | ART 2100 | 3”
  - equivalencies[AP-DRAWING|None]:  ⟵ “ | Studio Art — Drawing | 3 | ELEC 00013 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|None]:  ⟵ “ | Studio Art — 2D Design | 3 | ELEC 00013 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|None]:  ⟵ “ | Studio Art — 3D Design | 3 | ELEC 00013 | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “Languages | Chinese Language and Culture | 3, 4 | CHIN 1010, 1020, 2010 | 11”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “ | French Language and Culture | 3, 4, 5 | FR 1010, 1020 | 8”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “ | German Language and Culture | 3, 4, 5 | GER 1010, 1020 | 8”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “ | Italian Language and Culture | 3, 4 | ITAL 1010, 1020, 2010 | 11”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “ | Japanese Language and Culture | 3, 4 | JAPN 1010, 1020, 2010 | 11”
  - equivalencies[AP-LATIN|None]:  ⟵ “ | Latin | 3 | LATN 1010, 1020, 2010 | 11”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|None]:  ⟵ “ | Spanish Language and Culture | 3, 4, 5 | SPAN 1010, 1020 | 8”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|None]:  ⟵ “ | Spanish Literature and Culture | 3 | SPAN 1010, 1020 | 8”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Math | Calculus AB | 3, 4, 5 | MATH 1060 | 4”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “ | Calculus BC | 3, 4, 5 | MATH 1060, 1080 | 8”
  - … 12 more rows
### `4c615a44e48e4667` Clinton College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.clintoncollege.edu/admissions-aid/financial-aid/ (sha256 4fa2872ebfde)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances This is a terminology change on the 2025–26 FAFSA form.”
  - sentence: need_based_special_circumstances ⟵ “Learn how to complete your application if you have unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Direct Unsubsidized Loan Only While this isn’t a new question, the flow of the 2025–26 form is a little different if you are a student whose parents are unwilling to provide their information, but don’t have an unusual circumstance (such as those listed above).”
### `03c38a070d03deec` Coker University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coker.edu/wp-content/uploads/2026/02/SAP-Guidelines_021126.pdf (sha256 03b35ae49151)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “A student who fails to meet SAP standards at the end of a term and has already used the one- time Warning status will be placed on SAP Suspension and becomes ineligible for Federal Title IV, state, and applicable institutional financial aid unless the student submits a SAP appeal that is approved.”
  - sentence: sap_appeal ⟵ “Probation and Academic Plans If a student on SAP Suspension submits a SAP appeal and the appeal is approved, the student may be placed on Financial Aid Probation, with or without an Academic Plan, in accordance with institutional policy. • If it is possible for the student to meet SAP standards within one term, the student may be placed on Probation for one term without an Academic Plan.”
  - sentence: sap_appeal ⟵ “Students may submit one (1) SAP appeal during their academic career at Coker University.”
  - sentence: sap_appeal ⟵ “A graduate student who fails to meet SAP standards after the Warning term will be placed on SAP Suspension and becomes ineligible for financial aid unless the student submits a SAP appeal that is approved. 6.”
  - sentence: sap_appeal ⟵ “If a SAP appeal is approved: • If it is possible for the student to meet SAP standards within one term, the student may be placed on Financial Aid Probation for one term without an Academic Plan. • If it is not possible for the student to meet SAP standards within one term, the student will be placed on Financial Aid Probation with an individualized Academic Plan. 7.”
  - sentence: sap_appeal ⟵ “A student may submit one (1) SAP appeal during their academic career at Coker University.”
### `7a6a72aee3d346eb` Coker University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coker.edu/wp-content/uploads/2026/02/SAP-Guidelines_021126.pdf (sha256 03b35ae49151)
- issues: semantic_review_required, conflicting_sources:https://www.coker.edu/tuition-aid/student-responsibilities/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The appeal must include: • A written explanation of the extenuating circumstances (such as illness, injury, death of a family member, or other documented special circumstances) that prevented the student from meeting SAP standards; • Supporting documentation substantiating those circumstances; and • A statement explaining what has changed and how the student will be able to meet SAP standards at t”
### `e1d5985b069e0a4f` Coker University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.coker.edu/tuition-aid/student-responsibilities/ (sha256 f317cf5c14de)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.coker.edu/wp-content/uploads/2026/02/SAP-Guidelines_021126.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The appeal should provide the reason(s) (illness, injury, death of a family member, or other special circumstance) why SAP was not achieved, what has changed that would allow demonstration of progress at next evaluation, and what the student intends to do to regain SAP.”
### `f05bbdcf0ff59e30` Coker University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.coker.edu/tuition-aid/student-responsibilities/ (sha256 f317cf5c14de)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “For graduate or professional students applying for a Graduate PLUS Loan, the university must first determine the student’s maximum eligibility for the Direct Unsubsidized Loan before the Graduate PLUS Loan may be processed. add remove Borrower and Self Certification Form Coker’s borrower and self certification form is available here. add remove Professional Judgment Policy Federal regulations allo”
  - sentence: professional_judgment ⟵ “This process is called Professional Judgment.”
  - sentence: professional_judgment ⟵ “Professional Judgment allows the Financial Aid Office to evaluate documented circumstances on a case by case basis and determine whether adjustments to a student’s financial aid information or cost of attendance are appropriate.”
  - sentence: professional_judgment ⟵ “Professional Judgment decisions are made individually based on the documentation provided and in accordance with federal regulations.”
### `3b4f700a6658053c` Columbia College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.columbiasc.edu/tuition-aid/financial-aid (sha256 59418e5ac0cd)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “For example, having a busy part-time job would not qualify for a SAP appeal.”
  - sentence: sap_appeal ⟵ “If you’ve previously submitted a SAP appeal with the same extenuating circumstance(s) and you are still not meeting SAP requirements.”
  - sentence: sap_appeal ⟵ “Your SAP appeal explanation must include the following: Explain what happened: Why were you unable to maintain satisfactory progress?”
  - sentence: sap_appeal ⟵ “The Appeal Process A student may appeal their suspension of financial aid eligibility by following this process: Complete the Satisfactory Academic Progress Appeal Application in which the student clearly explains extenuating circumstances which prevented you from meeting the Satisfactory Academic Progress requirements.”
  - sentence: sap_appeal ⟵ “Submit Appeals Form and Supporting Documents to: Columbia College Office of Financial Aid ATTN: Satisfactory Academic Progress 1301 Columbia College Drive Columbia, SC 29203 Email To: fa@columbiacollegesc.edu Academic Plans Students, who have an approved SAP appeal and require more than one semester to meet SAP cumulative standards, must have an academic plan.”
  - sentence: sap_appeal ⟵ “Forms that could be required include but are not limited to: Verification Worksheet Parent/Student Tax Return Transcript or Federal 1040 Form Parent/Student W-2s Low Income/Non-Tax Filer form Untaxed Income Document Statement of Educational Purpose Unaccompanied Youth Form Parent Plus Waiver Form Statement for Previous Loan Discharge Special Circumstances Form Dependency Evaluation Request Form Sa”
### `497395ef20919ca4` Columbia College — appeals 2026-27 [new] (labeled_in_title)
- source: https://kc.columbiasc.edu/ICS/icsfs/Professional_Judgment_Appeal.pdf?target=4e0dc656-3fbd-4078-8fda-b4acd876215f (sha256 089370d5e50e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “CONDITION A: EXTENUATING CIRCUMSTANCES You have a special circumstance which will cause your family’s 2025 income to be significantly less than that of 2024.”
### `71ac945ce834195b` Columbia College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.columbiasc.edu/tuition-aid/financial-aid (sha256 59418e5ac0cd)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “We can review special circumstances and discuss available options.”
  - sentence: need_based_special_circumstances ⟵ “The changes to the inputs are dictated by the impact of the special circumstances on the family's income and assets.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration), more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance requests to change the income data element due to loss of income will not be considered until after January 1 of the current award year and after the student has filed a federal tax return for the future award year.”
  - sentence: need_based_special_circumstances ⟵ “Once the student has filed a federal tax return for the future award year, the student should submit the Special Circumstance request form along with supporting documentation to the Office of Financial Aid.”
### `89c2b75dc5289364` Columbia College — appeals 2026-27 [new] (labeled_in_title)
- source: https://kc.columbiasc.edu/ICS/icsfs/Professional_Judgment_Appeal.pdf?target=4e0dc656-3fbd-4078-8fda-b4acd876215f (sha256 089370d5e50e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “2026-2027 PROFESSIONAL JUDGMENT APPEAL FOR SPECIAL CIRCUMSTANCES Student Name: _______________________________ CC Student ID#: _________________ Please identify the reason for your appeal: □ Your parents are/will be experiencing significant and unusual expenses during the school year that are not reflected by the information disclosed on your FAFSA. □ One or both parent(s), or spouse, that reporte”
### `8b23275849b43bf2` Columbia College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.columbiasc.edu/tuition-aid/financial-aid (sha256 59418e5ac0cd)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: professional_judgment ⟵ “Financial Aid Policies Professional Judgement Professional Judgment refers to the authority of a college’s financial aid office to adjust the data elements on the FAFSA (special circumstances) and/or to adjust a student's dependency status (unusual circumstances) on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “There are two different categories of professional judgment: Special Circumstances refer to the financial situations (loss of a job, etc.) that justify an aid administrator adjusting data elements in the COA or in the EFC calculation.”
  - sentence: professional_judgment ⟵ “The Financial Aid Director and Associate Director of Financial Aid will have the authority to exercise professional judgment.”
  - sentence: professional_judgment ⟵ “After all documentation is collected, the Professional Judgment Committee will evaluate the material for PJ consideration.”
  - sentence: professional_judgment ⟵ “Requests for Special Circumstances Consideration To make a request, complete the professional judgment for special circumstances form.”
  - sentence: professional_judgment ⟵ “Requests for Unusual Circumstances Consideration To make a request, complete the professional judgment for unusual circumstances form.”
### `dd6243dcc855ee86` Columbia College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.columbiasc.edu/tuition-aid/financial-aid (sha256 59418e5ac0cd)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “All Financial Aid counselors and the Director have the authority to exercise a dependency override.”
  - sentence: dependency_override ⟵ “All decisions made on dependency overrides are final and cannot be appealed to the U.”
### `efa844f8ee1f1116` Columbia College — appeals 2026-27 [new] (source_unlabeled)
- source: https://kc.columbiasc.edu/ICS/icsfs/Institutional_Aid_Policy_Appeal_Process.pdf?target=7e66d21b-1eed-4544-a47c-ebc3683e20f6 (sha256 07789ddc957e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Important Reminder If you are also required to submit a SAP appeal, you may use the same appeal statement and documentation for both processes. 1301 Columbia College Drive, Columbia, SC 29203 | (P) 803-786-3612 | www.columbiasc.edu”
### `eca9d47dc7017a06` Columbia College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.columbiasc.edu/tuition-aid/financial-aid/cost-attendance (sha256 490b7b498c59)
- issues: ambiguous_year_labels
- checks: {"columns": 3, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition: 11778.0 ⟵ “Tuition | $ 11,778.00 | $ 11,778.00 | $ 23,556.00”
  - on_campus:Fees: 440.0 ⟵ “Fees | $ 440.00 | $ 440.00 | $ 880.00”
  - on_campus:Food & Housing: 5165.0 ⟵ “Food & Housing | $ 5,165.00 | $ 5,165.00 | $ 10,330.00”
  - on_campus:TOTALS: 17383.0 ⟵ “TOTALS | $ 17,383.00 | $ 17,383.00 | $ 34,766.00”
  - on_campus:Course Materials, Supplies & Equipment: 600.0 ⟵ “Course Materials, Supplies & Equipment | $ 600.00 | $ 600.00 | $ 1,200.00”
  - on_campus:Personal: 2210.0 ⟵ “Personal | $ 2,210.00 | $ 2,210.00 | $ 4,420.00”
  - on_campus:Transportation: 1096.0 ⟵ “Transportation | $ 1,096.00 | $ 1,096.00 | $ 2,192.00”
  - on_campus:*Loan Fees: 30.0 ⟵ “*Loan Fees | $ 30.00 | $ 30.00 | $ 60.00”
  - on_campus:TOTALS (2): 3936.0 ⟵ “TOTALS | $ 3,936.00 | $ 3,936.00 | $ 7,872.00”
  - on_campus:Total Cost of Attendance (Direct & Indirect Costs): 21319.0 ⟵ “Total Cost of Attendance (Direct & Indirect Costs) | $21,319.00 | $21,319.00 | $42,638.00”
  - on_campus:Tuition: 11778.0 ⟵ “Tuition | $ 11,778.00 | $ 11,778.00 | $ 23,556.00”
  - on_campus:Fees: 440.0 ⟵ “Fees | $ 440.00 | $ 440.00 | $ 880.00”
  - on_campus:Food & Housing: 5165.0 ⟵ “Food & Housing | $ 5,165.00 | $ 5,165.00 | $ 10,330.00”
  - on_campus:TOTALS: 17383.0 ⟵ “TOTALS | $ 17,383.00 | $ 17,383.00 | $ 34,766.00”
  - on_campus:Course Materials, Supplies & Equipment: 600.0 ⟵ “Course Materials, Supplies & Equipment | $ 600.00 | $ 600.00 | $ 1,200.00”
  - on_campus:Personal: 2210.0 ⟵ “Personal | $ 2,210.00 | $ 2,210.00 | $ 4,420.00”
  - on_campus:Transportation: 1096.0 ⟵ “Transportation | $ 1,096.00 | $ 1,096.00 | $ 2,192.00”
  - on_campus:*Loan Fees: 30.0 ⟵ “*Loan Fees | $ 30.00 | $ 30.00 | $ 60.00”
  - on_campus:TOTALS (2): 3936.0 ⟵ “TOTALS | $ 3,936.00 | $ 3,936.00 | $ 7,872.00”
  - on_campus:Total Cost of Attendance (Direct & Indirect Costs): 21319.0 ⟵ “Total Cost of Attendance (Direct & Indirect Costs) | $21,319.00 | $21,319.00 | $42,638.00”
  - on_campus:Tuition: 23556.0 ⟵ “Tuition | $ 11,778.00 | $ 11,778.00 | $ 23,556.00”
  - on_campus:Fees: 880.0 ⟵ “Fees | $ 440.00 | $ 440.00 | $ 880.00”
  - on_campus:Food & Housing: 10330.0 ⟵ “Food & Housing | $ 5,165.00 | $ 5,165.00 | $ 10,330.00”
  - on_campus:TOTALS: 34766.0 ⟵ “TOTALS | $ 17,383.00 | $ 17,383.00 | $ 34,766.00”
  - on_campus:Course Materials, Supplies & Equipment: 1200.0 ⟵ “Course Materials, Supplies & Equipment | $ 600.00 | $ 600.00 | $ 1,200.00”
  - … 5 more rows
### `23175d00f3d35662` Columbia International University — appeals 2024-25 [new] (labeled_in_source)
- source: https://ciu.edu/consumer-information/ (sha256 b17d84c638db)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “While maintaining the flexibility to respond to individual student circumstances, the Financial Aid Office also strives for consistency in treatment of students with similar unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Required documentation is listed on the Special Circumstances-Change in Marital Status form.”
  - sentence: need_based_special_circumstances ⟵ “All income adjustments must be used to address special circumstances where the data elements on the ISIR — based on income from the base year — no longer reflect the family’s (or student’s) ability to contribute to the student’s education.”
  - sentence: need_based_special_circumstances ⟵ “In addition, students (and parents) will need to submit a formal request for an assessment of special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “You may submit the appropriate Special Circumstances Request and supporting documentation to the CIU Financial Aid Office.”
  - sentence: need_based_special_circumstances ⟵ “On the homepage, scroll down to “Your Document Details” and click on “Get More Documents,” then click on “View Forms Here.” Click on the appropriate blue link for the Special Circumstances Request.”
### `55e5f24528da218a` Columbia International University — appeals 2024-25 [new] (labeled_in_source)
- source: https://ciu.edu/consumer-information/ (sha256 b17d84c638db)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: professional_judgment ⟵ “Contact: Director of Financial Aid | finaid@ciu.edu | (803) 807-5036 Professional Judgement Professional Judgement is the process of reviewing an individual student’s unique circumstances and exercising the option to change the data elements normally applied through the Department of Education Federal Methodology (FM) formula on the FAFSA application that helps compute a student’s family contribut”
  - sentence: professional_judgment ⟵ “Professional judgment changes are made when the financial aid administrator judges the standards used to determine the family contribution are inappropriate for purposes of calculating eligibility for financial aid due to extenuating circumstances.”
  - sentence: professional_judgment ⟵ “Columbia International University uses PowerFAIDS software to re-compute the family contribution both for corrections to reported data and for changes resulting when professional judgment is exercised.”
  - sentence: professional_judgment ⟵ “Potential Reasons for Exercise of Professional Judgment All professional judgment changes apply only to data element changes and apply to all Title IV programs.”
  - sentence: professional_judgment ⟵ “Drop of Income and Income Adjustments The ability to use professional judgment for adjustments of data elements on the ISIR is granted to the Director of Financial Aid.”
  - sentence: professional_judgment ⟵ “Third party documentation of changed circumstances should be used, whenever possible, to document the request for professional judgment.”
### `64426b3f1bad2007` Columbia International University — appeals 2024-25 [new] (labeled_in_source)
- source: https://ciu.edu/consumer-information/ (sha256 b17d84c638db)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Students with a marital status change from single (dependent on parent) to married within the award year may also submit a request for a dependency override.”
### `872577ea0a993e20` Columbia International University — appeals 2024-25 [new] (labeled_in_source)
- source: https://ciu.edu/consumer-information/ (sha256 b17d84c638db)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress The Financial Aid Appeal Committee will be granted the use of “professional judgment”.”
### `3f1897b43b76a886` Converse University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.converse.edu/admissions/undergraduate/financial-aid/ (sha256 b670e4fe7604)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Students/Parents submitting this request after September 30th, may also be asked to file their current year taxes before finalizing a professional judgment review decision.”
### `620c2c5083580866` Converse University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.converse.edu/admissions/undergraduate/financial-aid/ (sha256 b670e4fe7604)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 20}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Quick Links Tuition FAQsOpens new window Filing for Financial Aid Reevaluation & Special Circumstance Appeal Form Federal Financial Aid Changes Enrollment in Courses & Financial Aid Eligibility Tuition Cost and Aid Converse University is committed to using the Principles & Standards of the College Cost Transparency Initiative in its student financial aid offer.”
  - sentence: need_based_special_circumstances ⟵ “Reevaluation & Special Circumstances Appeal The FAFSA requests demographic and income information does not always give students the opportunity to explain a circumstance that may impact his or her ability to pay for college.”
  - sentence: need_based_special_circumstances ⟵ “For example, the household financial status on the FAFSA is not accurate based on special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Students may submit a Reevaluation Appeal to request Converse University Student Financial Aid take special circumstances into account to do a reassessment of the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “The Department of Education does allow Converse the ability to consider adjustments to a student’s FAFSA when special or unusual circumstances exist, but in limited scenarios.”
  - sentence: need_based_special_circumstances ⟵ “Please note that Converse University is not required by law to process a Reevaluation & Special Circumstances Appeal.”
### `6f4fd837b01dc127` Converse University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.converse.edu/admissions/undergraduate/financial-aid/ (sha256 b670e4fe7604)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “Dependency Override Parent information is required on the FAFSA for all students who are under 24 years old, unmarried, do not have children or dependents they support financially, and are not active duty military or a veteran.”
  - sentence: dependency_override ⟵ “Once submitted, a Student Financial Aid staff member will review your appeal within 21 business days and determine if you are eligible for a dependency override.”
  - sentence: dependency_override ⟵ “Contact the Student Financial Aid Office with any questions or assistance with the Dependency Override process at financialaid@converse.edu or 864-596-9019.”
### `34b7717781d78f88` Converse University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.converse.edu/undergraduate-catalog-202627/student-financial-aid-and-student-accounts (sha256 919501881476)
- issues: conflicting_sources:https://catalog.converse.edu/undergraduate-catalog-202627/student-financial-aid-scholarships
- checks: {"columns": 1, "rows": 3}
  - on_campus:Comprehensive Fee: 50240 ⟵ “Comprehensive Fee | $50,240”
  - on_campus:Includes tuition of: 35716 ⟵ “Includes tuition of | $35,716”
  - on_campus:and room and board of: 14524 ⟵ “and room and board of | $14,524”
### `e34e6ea59cbf87f2` Converse University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.converse.edu/undergraduate-catalog-202627/student-financial-aid-scholarships (sha256 a8fa717481b4)
- issues: components_do_not_reconcile, implausible_amount, conflicting_sources:https://catalog.converse.edu/undergraduate-catalog-202627/student-financial-aid-and-student-accounts
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - on_campus:Tuition: 35716 ⟵ “Tuition | $35,716 | $35,716 | $35,716”
  - on_campus:Housing & Food Living AllowanceCommuter Fee: 145241360 ⟵ “Housing & Food Living AllowanceCommuter Fee | $14,524$1,360 | $0$3,630$1,250 | $0$16,180$1,250”
  - on_campus:Books & Supplies: 620 ⟵ “Books & Supplies | $620 | $620 | $620”
  - on_campus:Personal: 1850 ⟵ “Personal | $1,850 | $1,850 | $1,850”
  - on_campus:TransportationAverage Loan Origination Fee: 107056 ⟵ “TransportationAverage Loan Origination Fee | $1,070$56 | $2,000$56 | $2,000$56”
  - on_campus:SGA Fee: 450 ⟵ “SGA Fee | $450 | $450 | $450”
  - on_campus:Total: 55646 ⟵ “Total | $55,646 | $45,572 | $58,122”
  - with_parents_or_family:Tuition: 35716 ⟵ “Tuition | $35,716 | $35,716 | $35,716”
  - with_parents_or_family:Housing & Food Living AllowanceCommuter Fee: 36301250 ⟵ “Housing & Food Living AllowanceCommuter Fee | $14,524$1,360 | $0$3,630$1,250 | $0$16,180$1,250”
  - with_parents_or_family:Books & Supplies: 620 ⟵ “Books & Supplies | $620 | $620 | $620”
  - with_parents_or_family:Personal: 1850 ⟵ “Personal | $1,850 | $1,850 | $1,850”
  - with_parents_or_family:TransportationAverage Loan Origination Fee: 200056 ⟵ “TransportationAverage Loan Origination Fee | $1,070$56 | $2,000$56 | $2,000$56”
  - with_parents_or_family:SGA Fee: 450 ⟵ “SGA Fee | $450 | $450 | $450”
  - with_parents_or_family:Total: 45572 ⟵ “Total | $55,646 | $45,572 | $58,122”
  - off_campus_not_with_family:Tuition: 35716 ⟵ “Tuition | $35,716 | $35,716 | $35,716”
  - off_campus_not_with_family:Housing & Food Living AllowanceCommuter Fee: 161801250 ⟵ “Housing & Food Living AllowanceCommuter Fee | $14,524$1,360 | $0$3,630$1,250 | $0$16,180$1,250”
  - off_campus_not_with_family:Books & Supplies: 620 ⟵ “Books & Supplies | $620 | $620 | $620”
  - off_campus_not_with_family:Personal: 1850 ⟵ “Personal | $1,850 | $1,850 | $1,850”
  - off_campus_not_with_family:TransportationAverage Loan Origination Fee: 200056 ⟵ “TransportationAverage Loan Origination Fee | $1,070$56 | $2,000$56 | $2,000$56”
  - off_campus_not_with_family:SGA Fee: 450 ⟵ “SGA Fee | $450 | $450 | $450”
  - off_campus_not_with_family:Total: 58122 ⟵ “Total | $55,646 | $45,572 | $58,122”
### `5ba339481f27fd1c` Denmark Technical College — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://catalog.denmarktech.edu/catalog/expenses-for-2024-2025-academic-year/ (sha256 daf88ae62dcc)
- issues: multiple_total_rows, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 7}
  - column:Tuition (based on 15 hrs.): 5640.0 ⟵ “Tuition (based on 15 hrs.) | $2,820.00 | $5,640.00”
  - column:Health Services Fee (On-campus ONLY): 150.0 ⟵ “Health Services Fee (On-campus ONLY) | $150.00 | $150.00”
  - column:Technology Fee: 125.0 ⟵ “Technology Fee | $125.00 | $125.00”
  - column:Student Activity Fee: 150.0 ⟵ “Student Activity Fee | $150.00 | $150.00”
  - column:Athletic Fee: 175.0 ⟵ “Athletic Fee | $175.00 | $175.00”
  - column:Total Fee (Off Campus): 6090.0 ⟵ “Total Fee (Off Campus) | $3,270.00 | $6,090.00”
  - column:Total Fee (On-Campus): 6240.0 ⟵ “Total Fee (On-Campus) | $3,420.00 | $6,240.00”
### `e39b3c0cb0b27748` Denmark Technical College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.denmarktech.edu/catalog/expenses-for-2024-2025-academic-year/ (sha256 daf88ae62dcc)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 7}
  - column:Tuition (based on 15 hrs.): 2820.0 ⟵ “Tuition (based on 15 hrs.) | $2,820.00 | $5,640.00”
  - column:Health Services Fee (On-campus ONLY): 150.0 ⟵ “Health Services Fee (On-campus ONLY) | $150.00 | $150.00”
  - column:Technology Fee: 125.0 ⟵ “Technology Fee | $125.00 | $125.00”
  - column:Student Activity Fee: 150.0 ⟵ “Student Activity Fee | $150.00 | $150.00”
  - column:Athletic Fee: 175.0 ⟵ “Athletic Fee | $175.00 | $175.00”
  - column:Total Fee (Off Campus): 3270.0 ⟵ “Total Fee (Off Campus) | $3,270.00 | $6,090.00”
  - column:Total Fee (On-Campus): 3420.0 ⟵ “Total Fee (On-Campus) | $3,420.00 | $6,240.00”
### `1da583b547597ce2` Denmark Technical College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.denmarktech.edu/deapplication/ (sha256 a2e06e0e1b7a)
- issues: stale_year_label:2025-26
- checks: {"fields": ["college_gpa_to_continue", "per_credit_hour_charges", "state_grant_accepted"], "tiers": 0}
  - college_gpa_to_continue: 2.0 ⟵ “SC Wins Scholarship covers tuition and fees after applying all other scholarships and grants for South Carolina residents enrolled in a quailed program. Award amounts may be adjusted or canceled due to changes in enrollment or the availability of funds. If I am a credit student, I understand that I ”
  - state_grant_accepted: True ⟵ “SC STATE GRANT/SCHOLARSHIP AFFIDAVIT Administrative Processing SC Lottery, SC Life or State Need-based (office use circle one)”
  - per_credit_hour_charge: 188.25 ⟵ “LTA and will owe a balance to the College of $188.25 per credit hour that will be due immediately.”
  - per_credit_hour_charge: 188.25 ⟵ “LTA and will owe a balance to the College of $188.25 per credit hour that will be due immediately.”
### `728cd7d2d22c6db1` Erskine College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.erskine.edu/admissions-aid/financial-aid/cost-of-attendance/ (sha256 ad0a7d3e5ac1)
- issues: stale_year_label:2025-26
- checks: {"columns": 4, "rows": 4}
  - on_campus:Tuition: 34435 ⟵ “Tuition | $34,435 | Books & Supplies | $1,210 | Tuition | $34,435 | Housing | $6,300”
  - on_campus:Fees: 2275 ⟵ “Fees | $2,275 | Computer | $750 | Fees | $2,275 | Books & Supplies | $1,210”
  - on_campus:Housing: 7950 ⟵ “Housing | $7,950 | Miscellaneous | $1,515 |  |  | Computer | $750”
  - on_campus:Meal Plan: 6900 ⟵ “Meal Plan | $6,900 | Transportation | $2,730 |  |  | Miscellaneous | $1,515”
  - with_parents_or_family:Tuition: 1210 ⟵ “Tuition | $34,435 | Books & Supplies | $1,210 | Tuition | $34,435 | Housing | $6,300”
  - with_parents_or_family:Fees: 750 ⟵ “Fees | $2,275 | Computer | $750 | Fees | $2,275 | Books & Supplies | $1,210”
  - with_parents_or_family:Housing: 1515 ⟵ “Housing | $7,950 | Miscellaneous | $1,515 |  |  | Computer | $750”
  - with_parents_or_family:Meal Plan: 2730 ⟵ “Meal Plan | $6,900 | Transportation | $2,730 |  |  | Miscellaneous | $1,515”
  - with_parents_or_family:Tuition: 34435 ⟵ “Tuition | $34,435 | Books & Supplies | $1,210 | Tuition | $34,435 | Housing | $6,300”
  - with_parents_or_family:Fees: 2275 ⟵ “Fees | $2,275 | Computer | $750 | Fees | $2,275 | Books & Supplies | $1,210”
  - on_campus:Tuition: 6300 ⟵ “Tuition | $34,435 | Books & Supplies | $1,210 | Tuition | $34,435 | Housing | $6,300”
  - on_campus:Fees: 1210 ⟵ “Fees | $2,275 | Computer | $750 | Fees | $2,275 | Books & Supplies | $1,210”
  - on_campus:Housing: 750 ⟵ “Housing | $7,950 | Miscellaneous | $1,515 |  |  | Computer | $750”
  - on_campus:Meal Plan: 1515 ⟵ “Meal Plan | $6,900 | Transportation | $2,730 |  |  | Miscellaneous | $1,515”
### `a7deefd29476aed5` Erskine College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.erskine.edu/admissions-aid/financial-aid/cost-of-attendance/ (sha256 ad0a7d3e5ac1)
- issues: stale_year_label:2024-25
- checks: {"columns": 4, "rows": 4}
  - on_campus:Tuition: 34435 ⟵ “Tuition | $34,435 | Books & Supplies | $1,200 | Tuition | $34,435 | Housing | $2,808”
  - on_campus:Fees: 2275 ⟵ “Fees | $2,275 | Computer | $750 | Fees | $2,275 | Books & Supplies | $1,200”
  - on_campus:Housing: 7350 ⟵ “Housing | $7,350 | Miscellaneous | $1,480 |  |  | Computer | $750”
  - on_campus:Meal Plan: 6900 ⟵ “Meal Plan | $6,900 | Transportation | $2,665 |  |  | Miscellaneous | $1,480”
  - with_parents_or_family:Tuition: 1200 ⟵ “Tuition | $34,435 | Books & Supplies | $1,200 | Tuition | $34,435 | Housing | $2,808”
  - with_parents_or_family:Fees: 750 ⟵ “Fees | $2,275 | Computer | $750 | Fees | $2,275 | Books & Supplies | $1,200”
  - with_parents_or_family:Housing: 1480 ⟵ “Housing | $7,350 | Miscellaneous | $1,480 |  |  | Computer | $750”
  - with_parents_or_family:Meal Plan: 2665 ⟵ “Meal Plan | $6,900 | Transportation | $2,665 |  |  | Miscellaneous | $1,480”
  - with_parents_or_family:Tuition: 34435 ⟵ “Tuition | $34,435 | Books & Supplies | $1,200 | Tuition | $34,435 | Housing | $2,808”
  - with_parents_or_family:Fees: 2275 ⟵ “Fees | $2,275 | Computer | $750 | Fees | $2,275 | Books & Supplies | $1,200”
  - on_campus:Tuition: 2808 ⟵ “Tuition | $34,435 | Books & Supplies | $1,200 | Tuition | $34,435 | Housing | $2,808”
  - on_campus:Fees: 1200 ⟵ “Fees | $2,275 | Computer | $750 | Fees | $2,275 | Books & Supplies | $1,200”
  - on_campus:Housing: 750 ⟵ “Housing | $7,350 | Miscellaneous | $1,480 |  |  | Computer | $750”
  - on_campus:Meal Plan: 1480 ⟵ “Meal Plan | $6,900 | Transportation | $2,665 |  |  | Miscellaneous | $1,480”
### `8ddd9497250f1eda` Florence-Darlington Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.fdtc.edu/tuition-fees-and-payment/cost-of-attendance-budgets/ (sha256 ae7d408df27b)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 4440 ⟵ “Tuition | $4,440”
  - column:Gen Ed Course Fee: 1200 ⟵ “Gen Ed Course Fee | $1,200”
  - column:College Fee: 100 ⟵ “College Fee | $100”
  - column:Tech Fee: 96 ⟵ “Tech Fee | $96”
  - column:Food & Housing: 4690 ⟵ “Food & Housing | $4,690”
  - column:Books & Supplies: 1488 ⟵ “Books & Supplies | $1,488”
  - column:Travel: 4800 ⟵ “Travel | $4,800”
  - column:Misc.: 1000 ⟵ “Misc. | $1,000”
  - column:TOTAL: 17814 ⟵ “TOTAL | $17,814”
### `2f2923bd3d38e4b5` Francis Marion University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fmarion.edu/wp-content/uploads/2026/06/2026-27-Student-Fee-distribution-web-all-pages.pdf (sha256 754e0825ab5b)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown
- checks: {"columns": 3, "components_reconcile": false, "rows": 50}
  - column:$: 41.0 ⟵ “$ | 41.00 | $ | 41.00”
  - column:$ (2): 95.0 ⟵ “$ | 95.00 | $ | 95.00”
  - column:$ (3): 126.0 ⟵ “$ | 126.00 | $ | 126.00”
  - column:$ (4): 20.0 ⟵ “$ | 20.00 | $ | 20.00”
  - column:$ (5): 156.0 ⟵ “$ | 156.00 | $ | 156.00”
  - column:$ (6): 112.0 ⟵ “$ | 112.00 | $ | 112.00”
  - column:$ (7): 56.0 ⟵ “$ | 56.00 | $ | 56.00”
  - column:UNIVERSITY FACILITY FEE (per semester)………………………………………………….$: 100.0 ⟵ “UNIVERSITY FACILITY FEE (per semester)………………………………………………….$ | 100.00 | $ | 100.00”
  - column:$ (8): 50.0 ⟵ “$ | 50.00 | $ | 50.00”
  - column:$ (9): 215.0 ⟵ “$ | 215.00 | $ | 215.00”
  - column:$ (10): 163.0 ⟵ “$ | 163.00 | $ | 163.00”
  - column:$ (11): 5192.0 ⟵ “$ | 5,192.00 | $ | 10,384.00”
  - column:$ (12): 519.2 ⟵ “$ | 519.20 $ | 1,038.40”
  - column:$ (13): 8118.0 ⟵ “$ | 8,118.00 | $ | 16,236.00”
  - column:$ (14): 811.8 ⟵ “$ | 811.80 $ | 1,623.60”
  - column:$ (15): 8118.0 ⟵ “$ | 8,118.00 | $ | 16,236.00”
  - column:$ (16): 811.8 ⟵ “$ | 811.80 $ | 1,623.60”
  - column:$ (17): 8118.0 ⟵ “$ | 8,118.00 | $ | 16,236.00”
  - column:$ (18): 811.8 ⟵ “$ | 811.80 $ | 1,623.60”
  - column:$ (19): 6262.0 ⟵ “$ | 6,262.00 | $ | 6,262.00”
  - column:$ (20): 626.2 ⟵ “$ | 626.20 $ | 626.20”
  - column:$ (21): 5306.0 ⟵ “$ | 5,306.00 | $ | 10,612.00”
  - column:$ (22): 530.6 ⟵ “$ | 530.60 $ | 1,061.20”
  - column:$ (23): 8232.0 ⟵ “$ | 8,232.00 | $ | 16,464.00”
  - column:$ (24): 823.2 ⟵ “$ | 823.20 $ | 1,646.40”
  - … 72 more rows
### `88661bc5f847d89c` Francis Marion University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fmarion.edu/wp-content/uploads/2016/07/2024-25-Tuition-Fees-Web-file.pdf (sha256 efa57b3ad8f0)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": false, "rows": 54}
  - column:$: 41.0 ⟵ “$ | 41.00 | $ | 41.00”
  - column:$ (2): 95.0 ⟵ “$ | 95.00 | $ | 95.00”
  - column:$ (3): 126.0 ⟵ “$ | 126.00 | $ | 126.00”
  - column:$ (4): 20.0 ⟵ “$ | 20.00 | $ | 20.00”
  - column:$ (5): 156.0 ⟵ “$ | 156.00 | $ | 156.00”
  - column:$ (6): 15.6 ⟵ “$ | 15.60 | $ | 15.60”
  - column:$ (7): 112.0 ⟵ “$ | 112.00 | $ | 112.00”
  - column:PART-TIME (per semester)……………………………………………...………………… $: 56.0 ⟵ “PART-TIME (per semester)……………………………………………...………………… $ | 56.00 | $ | 56.00”
  - column:$ (8): 100.0 ⟵ “$ | 100.00 | $ | 100.00”
  - column:PART-TIME (per semester)……………………………………………...………………… $ (2): 50.0 ⟵ “PART-TIME (per semester)……………………………………………...………………… $ | 50.00 | $ | 50.00”
  - column:$ (9): 215.0 ⟵ “$ | 215.00 | $ | 215.00”
  - column:$ (10): 163.0 ⟵ “$ | 163.00 | $ | 163.00”
  - column:$ (11): 5192.0 ⟵ “$ | 5,192.00 | $ | 10,384.00”
  - column:$ (12): 519.2 ⟵ “$ | 519.20 $ | 1,038.40”
  - column:$ (13): 8118.0 ⟵ “$ | 8,118.00 | $ | 16,236.00”
  - column:$ (14): 811.8 ⟵ “$ | 811.80 $ | 1,623.60”
  - column:$ (15): 6262.0 ⟵ “$ | 6,262.00 | $ | 6,262.00”
  - column:$ (16): 626.2 ⟵ “$ | 626.20 $ | 626.20”
  - column:$ (17): 5306.0 ⟵ “$ | 5,306.00 $ | 10,612.00”
  - column:$ (18): 530.6 ⟵ “$ | 530.60 $ | 1,061.20”
  - column:$ (19): 8232.0 ⟵ “$ | 8,232.00 | $ | 16,464.00”
  - column:$ (20): 823.2 ⟵ “$ | 823.20 $ | 1,646.40”
  - column:$ (21): 9764.0 ⟵ “$ | 9,764.00 $ | 19,528.00”
  - column:$ (22): 9764.0 ⟵ “$ | 9,764.00 $ | 19,528.00”
  - column:$ (23): 9764.0 ⟵ “$ | 9,764.00 $ | 19,528.00”
  - … 54 more rows
### `98782d02771c822a` Francis Marion University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.fmarion.edu/wp-content/uploads/2016/07/2025-26-Student-Fee-distribution-web-1.pdf (sha256 f5b715ec92c9)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": false, "rows": 44}
  - column:$: 41.0 ⟵ “$ | 41.00 | $ | 41.00”
  - column:$ (2): 95.0 ⟵ “$ | 95.00 | $ | 95.00”
  - column:ENROLLMENT FEE (refundable through May 1st)………………………………………………. $: 126.0 ⟵ “ENROLLMENT FEE (refundable through May 1st)………………………………………………. $ | 126.00 | $ | 126.00”
  - column:$ (3): 20.0 ⟵ “$ | 20.00 | $ | 20.00”
  - column:$ (4): 156.0 ⟵ “$ | 156.00 | $ | 156.00”
  - column:$ (5): 112.0 ⟵ “$ | 112.00 | $ | 112.00”
  - column:UNIVERSITY FACILITY FEE (per semester)………………………………………………….$: 100.0 ⟵ “UNIVERSITY FACILITY FEE (per semester)………………………………………………….$ | 100.00 | $ | 100.00”
  - column:$ (6): 215.0 ⟵ “$ | 215.00 | $ | 215.00”
  - column:$ (7): 5192.0 ⟵ “$ | 5,192.00 | $ | 10,384.00”
  - column:$ (8): 519.2 ⟵ “$ | 519.20 $ | 1,038.40”
  - column:UNDERGRADUATE - ENGINEERING……………………................……………………… $: 8118.0 ⟵ “UNDERGRADUATE - ENGINEERING……………………................……………………… $ | 8,118.00 | $ | 16,236.00”
  - column:$ (9): 811.8 ⟵ “$ | 811.80 $ | 1,623.60”
  - column:$ (10): 8118.0 ⟵ “$ | 8,118.00 | $ | 16,236.00”
  - column:$ (11): 811.8 ⟵ “$ | 811.80 $ | 1,623.60”
  - column:$ (12): 6262.0 ⟵ “$ | 6,262.00 | $ | 6,262.00”
  - column:$ (13): 626.2 ⟵ “$ | 626.20 $ | 626.20”
  - column:$ (14): 5306.0 ⟵ “$ | 5,306.00 | $ | 10,612.00”
  - column:$ (15): 530.6 ⟵ “$ | 530.60 $ | 1,061.20”
  - column:$ (16): 8232.0 ⟵ “$ | 8,232.00 | $ | 16,464.00”
  - column:$ (17): 823.2 ⟵ “$ | 823.20 $ | 1,646.40”
  - column:$ (18): 9764.0 ⟵ “$ | 9,764.00 $ | 19,528.00”
  - column:$ (19): 976.4 ⟵ “$ | 976.40 $ | 1,952.80”
  - column:$ (20): 9764.0 ⟵ “$ | 9,764.00 $ | 19,528.00”
  - column:$ (21): 976.4 ⟵ “$ | 976.40 $ | 1,952.80”
  - column:$ (22): 9764.0 ⟵ “$ | 9,764.00 $ | 19,528.00”
  - … 66 more rows
### `b45adb5b908c6257` Furman University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.furman.edu/admissions-aid/tuition-fees/ (sha256 18ceee7d6afc)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - column:Tuition: 62878 ⟵ “Tuition | $62,878”
  - column:Student Fees: 410 ⟵ “Student Fees | $410”
  - column:Housing (weighted average): 10440 ⟵ “Housing (weighted average) | $10,440”
  - column:Unlimited Meal Plan: 7548 ⟵ “Unlimited Meal Plan | $7,548”
  - column:Total Additional: 3650 ⟵ “Total Additional | $3,650”
  - column:Total Direct Costs: 81276 ⟵ “Total Direct Costs | $81,276”
### `5d7ad0403c414c3f` Greenville Technical College — academic_programs 2026-27 · program_key=advanced-manufacturing-technology-bachelor-in-applied-science-greenville-technic [new] (labeled_in_source)
- source: https://catalog.gvltec.edu/school-advanced-manufacturing-transportation-technology/advanced-manufacturing-technology/advanced-manufacturing-technology-bas/ (sha256 5a1560046e97)
- issues: requirement_groups_skipped
- checks: {"courses": 21, "groups": 7, "groups_skipped": 1}
  - program_name: Advanced Manufacturing Technology Bachelor in Applied Science | Greenville Technical College Student Handbook and Catalog ⟵ “Advanced Manufacturing Technology Bachelor in Applied Science | Greenville Technical College Student Handbook and Catalog”
### `04c99dbce87a94b6` Greenville Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gvltec.edu/admissions_aid/financial_aid/grants/lottery.html (sha256 059ff258120d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “The lottery appeal opens on the first day that the full semester begins, and ends the last day of class of the full term prior to exams starting.”
### `160af7fc1a218244` Greenville Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gvltec.edu/admissions_aid/financial_aid/sap.html (sha256 4a755fa1222b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Students will be offered one Satisfactory Academic Progress appeal during their entire academic enrollment at GTC.”
  - sentence: sap_appeal ⟵ “Continue to work towards graduation within the number of credit hours approved on SAP Appeal.”
  - sentence: sap_appeal ⟵ “A student who is currently on financial aid Suspension has exhausted their SAP Appeal options.) Students who become ineligible for financial aid may be eligible to file an appeal.”
### `4a3c6c65b538ed0f` Greenville Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gvltec.edu/admissions_aid/financial_aid/sap.html (sha256 4a755fa1222b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If a student failed to meet SAP due to his injury or illness, death of a relative or other special circumstance, the student may appeal to have financial aid reinstated.”
### `075b47ae83639d10` Greenville Technical College — degree_requirements 2026-27 · program_key=advanced-manufacturing-technology-bachelor-in-applied-science-greenville-technic · requirement_key=requirements-for-completion-first-semester [new] (labeled_in_source)
- source: https://catalog.gvltec.edu/school-advanced-manufacturing-transportation-technology/advanced-manufacturing-technology/advanced-manufacturing-technology-bas/ (sha256 5a1560046e97)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MFG 300 ⟵ “MFG 300 - Manufacturing Processes and Application”
  - courses: MAT 120 ⟵ “MAT 120 - Probability and Statistics 1”
  - courses: MFG 311 ⟵ “MFG 311 - Work Design, Ergonomics, and Safety”
### `3ab1dfcbd23f4238` Greenville Technical College — degree_requirements 2026-27 · program_key=advanced-manufacturing-technology-bachelor-in-applied-science-greenville-technic · requirement_key=requirements-for-completion-seventh-semester [new] (labeled_in_source)
- source: https://catalog.gvltec.edu/school-advanced-manufacturing-transportation-technology/advanced-manufacturing-technology/advanced-manufacturing-technology-bas/ (sha256 5a1560046e97)
- issues: requirement_groups_skipped
  - courses: MFG 482 ⟵ “MFG 482 - Industry Capstone Project II”
  - courses: MFG 401 ⟵ “MFG 401 - Advanced Metrology”
### `44ff716e7666ab92` Greenville Technical College — degree_requirements 2026-27 · program_key=advanced-manufacturing-technology-bachelor-in-applied-science-greenville-technic · requirement_key=requirements-for-completion-second-semester [new] (labeled_in_source)
- source: https://catalog.gvltec.edu/school-advanced-manufacturing-transportation-technology/advanced-manufacturing-technology/advanced-manufacturing-technology-bas/ (sha256 5a1560046e97)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ENG 101 ⟵ “ENG 101 - English Composition I”
  - courses: MAT 110 ⟵ “MAT 110 - College Algebra 1”
  - courses: MFG 340 ⟵ “MFG 340 - Computer Aided Design for Manuf Engineer”
  - courses: MFG 321 ⟵ “MFG 321 - Advanced Manufacturing Lab I”
### `9c0600ed04540046` Greenville Technical College — degree_requirements 2026-27 · program_key=advanced-manufacturing-technology-bachelor-in-applied-science-greenville-technic · requirement_key=requirements-for-completion-fifth-semester [new] (labeled_in_source)
- source: https://catalog.gvltec.edu/school-advanced-manufacturing-transportation-technology/advanced-manufacturing-technology/advanced-manufacturing-technology-bas/ (sha256 5a1560046e97)
- issues: requirement_groups_skipped
  - courses: MFG 370 ⟵ “MFG 370 - Principles of Lean Manufacturing”
  - courses: MFG 402 ⟵ “MFG 402 - Additive Manufacturing”
  - courses: MFG 314 ⟵ “MFG 314 - Finance for Manufacturing”
### `d78bfdbeaaac0c39` Greenville Technical College — degree_requirements 2026-27 · program_key=advanced-manufacturing-technology-bachelor-in-applied-science-greenville-technic · requirement_key=requirements-for-completion-fourth-semester [new] (labeled_in_source)
- source: https://catalog.gvltec.edu/school-advanced-manufacturing-transportation-technology/advanced-manufacturing-technology/advanced-manufacturing-technology-bas/ (sha256 5a1560046e97)
- issues: requirement_groups_skipped
  - courses: SPC 205 ⟵ “SPC 205 - Public Speaking”
  - courses: MFG 323 ⟵ “MFG 323 - Advanced Manufacturing Lab III”
  - courses: MFG 330 ⟵ “MFG 330 - Manufacturing Project Management”
  - courses: MFG 350 ⟵ “MFG 350 - Production Process Planning”
### `ef6c9d1ce5b687d6` Greenville Technical College — degree_requirements 2026-27 · program_key=advanced-manufacturing-technology-bachelor-in-applied-science-greenville-technic · requirement_key=requirements-for-completion-third-semester [new] (labeled_in_source)
- source: https://catalog.gvltec.edu/school-advanced-manufacturing-transportation-technology/advanced-manufacturing-technology/advanced-manufacturing-technology-bas/ (sha256 5a1560046e97)
- issues: requirement_groups_skipped
  - courses: ENG 102 ⟵ “ENG 102 - English Composition II”
  - courses: MFG 310 ⟵ “MFG 310 - Manufacturing Quality”
  - courses: MFG 322 ⟵ “MFG 322 - Advanced Manufacturing Lab II”
### `f5d418baa8fe4b21` Greenville Technical College — degree_requirements 2026-27 · program_key=advanced-manufacturing-technology-bachelor-in-applied-science-greenville-technic · requirement_key=requirements-for-completion-sixth-semester [new] (labeled_in_source)
- source: https://catalog.gvltec.edu/school-advanced-manufacturing-transportation-technology/advanced-manufacturing-technology/advanced-manufacturing-technology-bas/ (sha256 5a1560046e97)
- issues: requirement_groups_skipped
  - courses: MFG 360 ⟵ “MFG 360 - Leadership in Manufacturing”
  - courses: MFG 481 ⟵ “MFG 481 - Industry Capstone Project I”
### `9d02daaaceb0d9a3` Horry-Georgetown Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.hgtc.edu/admissions/financialaid/cost-of-attendance.html (sha256 4ff0492bbb02)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition and fees: 11158 ⟵ “Tuition and fees | $5,689 | $6,958 | $11,158”
  - column:Loan fees: 28 ⟵ “Loan fees | $28 | $28 | $28”
  - column:Bridge fees: 3700 ⟵ “Bridge fees | $3,700 | $3,700 | $3,700”
  - column:Books, course materials, supplies, and equipment: 1000 ⟵ “Books, course materials, supplies, and equipment | $1,000 | $1,000 | $1,000”
  - column:Transportation: 1679 ⟵ “Transportation | $1,200 | $1,200 | $1,679”
  - column:Living expenses total including food and housing: 12942 ⟵ “Living expenses total including food and housing | $12,942* | $12,942* | $12,942*”
  - column:Miscellaneous personal expenses: 3000 ⟵ “Miscellaneous personal expenses | $2,700 | $2,700 | $3,000”
  - column:Total (not including licensing fees): 33507 ⟵ “Total (not including licensing fees) | $27,259 | $28,528 | $33,507”
### `c68adcdc3629f17f` Horry-Georgetown Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.hgtc.edu/admissions/financialaid/tuition_and_fees/index.html (sha256 f4a8d8f0831f)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, conflicting_sources:https://www.hgtc.edu/admissions/financialaid/cost-of-attendance.html,https://www.hgtc.edu/documents/academics/programs/program-cost/2026-2027-programcosts/boat-building-costsheet.pdf
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and fees: 5689 ⟵ “Tuition and fees | $5,689 | $6,958 | $11,158”
  - column:Loan fees: 28 ⟵ “Loan fees | $28 | $28 | $28”
  - column:Bridge fees: 3700 ⟵ “Bridge fees | $3,700 | $3,700 | $3,700”
  - column:Books, course materials, supplies, and equipment: 1000 ⟵ “Books, course materials, supplies, and equipment | $1,000 | $1,000 | $1,000”
  - column:Transportation: 1200 ⟵ “Transportation | $1,200 | $1,200 | $1,679”
  - column:Living expenses total including food and housing: 12942 ⟵ “Living expenses total including food and housing | $12,942* | $12,942* | $12,942*”
  - column:Miscellaneous personal expenses: 2700 ⟵ “Miscellaneous personal expenses | $2,700 | $2,700 | $3,000”
  - column:Total (not including licensing fees): 27259 ⟵ “Total (not including licensing fees) | $27,259 | $28,528 | $33,507”
  - column:Tuition and fees: 6958 ⟵ “Tuition and fees | $5,689 | $6,958 | $11,158”
  - column:Loan fees: 28 ⟵ “Loan fees | $28 | $28 | $28”
  - column:Bridge fees: 3700 ⟵ “Bridge fees | $3,700 | $3,700 | $3,700”
  - column:Books, course materials, supplies, and equipment: 1000 ⟵ “Books, course materials, supplies, and equipment | $1,000 | $1,000 | $1,000”
  - column:Transportation: 1200 ⟵ “Transportation | $1,200 | $1,200 | $1,679”
  - column:Living expenses total including food and housing: 12942 ⟵ “Living expenses total including food and housing | $12,942* | $12,942* | $12,942*”
  - column:Miscellaneous personal expenses: 2700 ⟵ “Miscellaneous personal expenses | $2,700 | $2,700 | $3,000”
  - column:Total (not including licensing fees): 28528 ⟵ “Total (not including licensing fees) | $27,259 | $28,528 | $33,507”
### `ceb410ebb4ac60dd` Horry-Georgetown Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.hgtc.edu/documents/academics/programs/program-cost/2026-2027-programcosts/boat-building-costsheet.pdf (sha256 1df8ae2a029f)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.hgtc.edu/admissions/financialaid/cost-of-attendance.html,https://www.hgtc.edu/admissions/financialaid/tuition_and_fees/index.html
- checks: {"columns": 3, "rows": 9}
  - column:Tuition Costs & Other Standard Fees: 6186 ⟵ “Tuition Costs & Other Standard Fees | $6,186 | $0 | $6,186”
  - column:(New HGTC Student): 0 ⟵ “(New HGTC Student) | $0 | $0 | $0”
  - column:Criminal Background Check: 0 ⟵ “Criminal Background Check | $0”
  - column:Urine Drug Screening: 0 ⟵ “Urine Drug Screening | $0”
  - column:Student Health Records System: 0 ⟵ “Student Health Records System | $0”
  - column:SC State Board Licensure/Certification Fee(s):: 0 ⟵ “SC State Board Licensure/Certification Fee(s): | $0 | $0”
  - column:Textbooks & Other Course Materials: 0 ⟵ “Textbooks & Other Course Materials | $0 | $0”
  - column:Tool Kit and/or other program supplies: 0 ⟵ “Tool Kit and/or other program supplies | $0 | $0”
  - column:Subtotal: 6186 ⟵ “Subtotal | $6,186 | $0 | $6,186”
  - column:Tuition Costs & Other Standard Fees: 0 ⟵ “Tuition Costs & Other Standard Fees | $6,186 | $0 | $6,186”
  - column:(New HGTC Student): 0 ⟵ “(New HGTC Student) | $0 | $0 | $0”
  - column:SC State Board Licensure/Certification Fee(s):: 0 ⟵ “SC State Board Licensure/Certification Fee(s): | $0 | $0”
  - column:Textbooks & Other Course Materials: 0 ⟵ “Textbooks & Other Course Materials | $0 | $0”
  - column:Tool Kit and/or other program supplies: 0 ⟵ “Tool Kit and/or other program supplies | $0 | $0”
  - column:Subtotal: 0 ⟵ “Subtotal | $6,186 | $0 | $6,186”
  - column:Tuition Costs & Other Standard Fees: 6186 ⟵ “Tuition Costs & Other Standard Fees | $6,186 | $0 | $6,186”
  - column:(New HGTC Student): 0 ⟵ “(New HGTC Student) | $0 | $0 | $0”
  - column:Subtotal: 6186 ⟵ “Subtotal | $6,186 | $0 | $6,186”
### `ee6d35404fbfa3de` Horry-Georgetown Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.hgtc.edu/admissions/financialaid/cost-of-attendance.html (sha256 4ff0492bbb02)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, conflicting_sources:https://www.hgtc.edu/admissions/financialaid/tuition_and_fees/index.html,https://www.hgtc.edu/documents/academics/programs/program-cost/2026-2027-programcosts/boat-building-costsheet.pdf
- checks: {"columns": 2, "components_reconcile": false, "rows": 8}
  - column:Tuition and fees: 5689 ⟵ “Tuition and fees | $5,689 | $6,958 | $11,158”
  - column:Loan fees: 28 ⟵ “Loan fees | $28 | $28 | $28”
  - column:Bridge fees: 3700 ⟵ “Bridge fees | $3,700 | $3,700 | $3,700”
  - column:Books, course materials, supplies, and equipment: 1000 ⟵ “Books, course materials, supplies, and equipment | $1,000 | $1,000 | $1,000”
  - column:Transportation: 1200 ⟵ “Transportation | $1,200 | $1,200 | $1,679”
  - column:Living expenses total including food and housing: 12942 ⟵ “Living expenses total including food and housing | $12,942* | $12,942* | $12,942*”
  - column:Miscellaneous personal expenses: 2700 ⟵ “Miscellaneous personal expenses | $2,700 | $2,700 | $3,000”
  - column:Total (not including licensing fees): 27259 ⟵ “Total (not including licensing fees) | $27,259 | $28,528 | $33,507”
  - column:Tuition and fees: 6958 ⟵ “Tuition and fees | $5,689 | $6,958 | $11,158”
  - column:Loan fees: 28 ⟵ “Loan fees | $28 | $28 | $28”
  - column:Bridge fees: 3700 ⟵ “Bridge fees | $3,700 | $3,700 | $3,700”
  - column:Books, course materials, supplies, and equipment: 1000 ⟵ “Books, course materials, supplies, and equipment | $1,000 | $1,000 | $1,000”
  - column:Transportation: 1200 ⟵ “Transportation | $1,200 | $1,200 | $1,679”
  - column:Living expenses total including food and housing: 12942 ⟵ “Living expenses total including food and housing | $12,942* | $12,942* | $12,942*”
  - column:Miscellaneous personal expenses: 2700 ⟵ “Miscellaneous personal expenses | $2,700 | $2,700 | $3,000”
  - column:Total (not including licensing fees): 28528 ⟵ “Total (not including licensing fees) | $27,259 | $28,528 | $33,507”
### `0fc2586bc5361188` Lander University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2025-2026/26HOME.pdf (sha256 ff98aca0ca7c)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2025-2026/26PCAR.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/parent26.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Since you were unable to document any of the homeless designations, you will need to: o Correct your FAFSA by answering NONE OF THESE APPLY to question 6 related to homelessness. o Complete the FAFSA with parent (and if applicable, stepparent) information. o Sign and date below and return this form to the Lander University Financial Aid Office. o If you feel you have special circumstances, you may”
### `10708e57e56b9802` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27life.pdf (sha256 e8e9cba3039c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “APPEALS If an extenuating circumstance has caused a student to fail to meet the academic requirements (cumulative grade point average and/or credit hours) for regaining or renewing a LIFE Scholarship, the student may file an appeal with the Commission on Higher Education.”
### `2e0be525f1546580` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/24hhou.pdf (sha256 fc31cf03735e)
- issues: semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27eman.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27home.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27pcar.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27scar.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Your spouse did not live in your home during the last 6 months of the tax year. *Your spouse is considered to live in your home even if he/she is temporarily absent due to special circumstances. □ 4.”
### `30f48e3125c7df38` Lander University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2025-2026/26PCAR.pdf (sha256 317463135c4a)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2025-2026/26HOME.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/parent26.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Office of Financial Aid Phone: 864-388-8340 | Fax: 864-388-8811 | Form Code 26PCAR 320 Stanley Avenue, Greenwood, SC 29649 | lander.edu/finaid | Email: finaid@lander.edu 2025-2026 Parent Contribution Adjustment Request Complete this form if you feel your family has special circumstances that should be considered with your application for financial aid.”
### `353e2c3b9ae8006b` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27home.pdf (sha256 805d01053468)
- issues: semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/24hhou.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27eman.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27pcar.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27scar.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Since you were unable to document any of the homeless designations, you will need to: o Correct your FAFSA by answering NONE OF THESE APPLY to question 6 related to homelessness. o Complete the FAFSA with parent (and if applicable, stepparent) information. o Sign and date below and return this form to the Lander University Financial Aid Office. o If you feel you have special circumstances, you may”
### `4a99aaa193c30162` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27dchg.pdf (sha256 adf8754f424a)
- issues: semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27pldc.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/separa26.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Before he/she can receive additional federal student loans, a legally licensed physician must complete the following certification: PHYSICIAN’S CERTIFICATION I certify that, in my best professional judgment, the student’s condition has improved and that the student: • has the ability to engage in substantial gainful activity and • can attend school.”
### `8302a9b7665daa3f` Lander University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/parent26.pdf (sha256 7a2a80beeff6)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2025-2026/26HOME.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2025-2026/26PCAR.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Fwd to Counselor date RRAAREQ – PARENT + any verf docs missing; RHACOMM CNSLR Initials/date If you feel you have special circumstances that need to be considered, please refer to www.lander.edu/finaid/forms and select the Dependency Status Appeal Form for the appropriate academic year.”
### `8626f5c5d9078f77` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27pldc.pdf (sha256 2b4072fde8fd)
- issues: semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27dchg.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/separa26.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Before he/she can receive additional federal loans, a legally licensed physician must complete the following certification: PHYSICIAN’S CERTIFICATION I certify that, in my best professional judgment, the parent borrower’s condition has improved and that the parent borrower: • has the ability to engage in substantial gainful activity.”
### `937b35a684dfee3c` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/separa26.pdf (sha256 3861f34530bf)
- issues: semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27dchg.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27pldc.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If you purposely give false or misleading information in order to qualify for Title IV funds, you may be fined $20,000, sent to prison or both. ________________________________________________________________________________________ Student’s Signature (Required) Phone # Date ________________________________________________________________________________________ Parent’s Signature (Required for D”
### `9676867ff33285fa` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27eman.pdf (sha256 fd015a0a7b6c)
- issues: semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/24hhou.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27home.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27pcar.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27scar.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The parent that should be reported on the FAFSA is the parent who provides the greater portion of the student’s financial support, even if the student does not live with them. o If you feel you have special circumstances, you may review and submit the 2026-2027 Dependency Appeal Form available at www.lander.edu/finaid/forms to the Lander University Financial Aid Office. o Complete and return this ”
### `9a05287847b126fc` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27scar.pdf (sha256 1d1e7558dfa4)
- issues: semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/24hhou.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27eman.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27home.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27pcar.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Office of Financial Aid Phone: 864-388-8340 | Fax: 864-388-8811 | Form Code 27SCAR 320 Stanley Avenue, Greenwood, SC 29649 | lander.edu/finaid | Email: finaid@lander.edu 2026-2027 Student Contribution Adjustment Request Complete this form if you feel your family has special circumstances that should be considered with your application for financial aid.”
### `cee19b9f81df339e` Lander University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lander.edu/admissions/tuition-financial-aid/satisfactory-academic-progress-sap.html (sha256 2f2fb1b7038f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Policy SAP Evaluation Procedure Appeals to SAP Decisions Policy The Satisfactory Academic Progress standards require that progress must be measured in three distinct ways: quantitatively, qualitatively, and in terms of a time frame.”
  - sentence: sap_appeal ⟵ “ALL transcripts from ALL prior institutions must be received and articulated before any financial aid or Satisfactory Academic Progress appeals can be processed.”
  - sentence: sap_appeal ⟵ “Appeals to SAP Decisions All students who are denied aid due to failure to maintain Satisfactory Academic Progress may appeal in writing to the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeal form can be found on the Financial Aid forms page under "General".”
### `e82cc8308f20981c` Lander University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27pcar.pdf (sha256 f1a1e4ba548e)
- issues: semantic_review_required, conflicting_sources:https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/24hhou.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27eman.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27home.pdf,https://www.lander.edu/admissions/_files/Documents/Financial_Aid/2026-2027/27scar.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Office of Financial Aid Phone: 864-388-8340 | Fax: 864-388-8811 | Form Code 27PCAR 320 Stanley Avenue, Greenwood, SC 29649 | lander.edu/finaid | Email: finaid@lander.edu 2026-2027 Parent Contribution Adjustment Request Complete this form if you feel your family has special circumstances that should be considered with your application for financial aid.”
### `67a8b7a666579067` Lander University — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.lander.edu/admissions/_files/Documents/admissions/dual-enrollment-request-form-2026.pdf (sha256 f1e90cf974ed)
- issues: stale_year_label:2024-25
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.25 ⟵ “• Must have a minimum weighted GPA of 3.25”
  - per_credit_hour_charge: 100 ⟵ “six (6) credit hours in the Fall and Spring semesters are $100 per credit hour.”
### `2438a0d4f7f1f66b` Midlands Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.midlandstech.edu/financial-aid-and-tuition/how-apply-financial-aid (sha256 12dbe33c0240)
- issues: semantic_review_required, conflicting_sources:https://www.midlandstech.edu/financial-aid-and-tuition/how-apply-financial-aid/financial-aid-terms-and-conditions
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you/your family have special circumstances that you believe should be taken into consideration (e.g., an income source is no longer being received, a significant change of income expected, etc.) you should contact a Financial Aid Counselor.”
### `2cdcb730bc8101e4` Midlands Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.midlandstech.edu/financial-aid-and-tuition/how-apply-financial-aid/financial-aid-satisfactory-academic-progress-sap (sha256 e39878b41452)
- issues: semantic_review_required, conflicting_sources:https://www.midlandstech.edu/financial-aid-and-tuition/how-apply-financial-aid
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “To receive consideration for reinstatement of federal or state assistance, a student will need to submit a Satisfactory Academic Progress (SAP) appeal to the Office of Student Financial Services.”
  - sentence: sap_appeal ⟵ “Students on a Financial Aid Warning Status can receive financial aid for one term without submitting a financial aid SAP appeal.”
  - sentence: sap_appeal ⟵ “An ineligible student may appeal by submitting a Satisfactory Academic Progress Appeal Form to the Student Financial Services Office indicating reasons why minimum academic standards were not achieved and what actions have been taken or what changes have occurred to resolve the problem.”
### `827a8185f066809c` Midlands Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.midlandstech.edu/financial-aid-and-tuition/how-apply-financial-aid (sha256 12dbe33c0240)
- issues: semantic_review_required, conflicting_sources:https://www.midlandstech.edu/financial-aid-and-tuition/how-apply-financial-aid/financial-aid-satisfactory-academic-progress-sap
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Student must maintain a cumulative 2.0 GPA Student must maintain a 67% pace rate of all attempted courses Student must complete their program of study within 150% of the total hours required to complete their program Read the full Satisfactory Academic Progress Policy Satisfactory Academic Progress Appeal Form Withdrawal and Return of Federal Aid Return of Federal Financial Aid (R2T4) A student’s ”
### `c7dcfc300e56ede7` Midlands Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.midlandstech.edu/financial-aid-and-tuition/how-apply-financial-aid/financial-aid-terms-and-conditions (sha256 4768cf8d768d)
- issues: semantic_review_required, conflicting_sources:https://www.midlandstech.edu/financial-aid-and-tuition/how-apply-financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “With proper documentation, we may consider certain unusual circumstances.”
### `b9efe69e855c613e` Midlands Technical College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.midlandstech.edu/financial-aid-and-tuition/student-cost-estimates (sha256 6d8e93cc971a)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition/Fees: 6566.0 ⟵ “Tuition/Fees | $6,566.00”
  - column:Loan Fees: 138.0 ⟵ “Loan Fees | $138.00”
  - column:Room/Board: 19809.0 ⟵ “Room/Board | $19,809.00”
  - column:Books/Supplies: 1624.0 ⟵ “Books/Supplies | $1,624.00”
  - column:Transportation: 3150.0 ⟵ “Transportation | $3,150.00”
  - column:Personal: 2439.0 ⟵ “Personal | $2,439.00”
  - column:Total: 33726.0 ⟵ “Total | $33,726.00”
### `0587d87bbe992c3d` Midlands Technical College — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://www.midlandstech.edu/admissions/testing-services (sha256 59ec645d2c2c)
- issues: conflicting_sources:https://www.midlandstech.edu/scores-international-baccalaureate
- checks: {"distinct_exams": 18, "equivalencies": 18, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|4]:  ⟵ “IB 0101 | Biology HL | 4 | BIO 101”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “IB 0111 | Business & Management | 4 | MGT 101”
  - equivalencies[IB-CHEMISTRY-HL|4]:  ⟵ “IB 0121 | Chemistry HL | 4 | CHM 110”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|4]:  ⟵ “IB 0131 | Computer Science HL | 4 | CPT 170”
  - equivalencies[IB-ECONOMICS-HL|4]:  ⟵ “IB 0151 | Economics HL | 4 | ECO 210”
  - equivalencies[IB-FILM-HL|4]:  ⟵ “IB 0181 | Film HL | 4 | ART 105”
  - equivalencies[IB-FRENCH-HL|4]:  ⟵ “IB 0191 | French A1 HL | 4 | FLG 001”
  - equivalencies[IB-GEOGRAPHY-HL|4]:  ⟵ “IB 0221 | Geography HL | 4 | GEO 102”
  - equivalencies[IB-GERMAN-HL|4]:  ⟵ “IB 0231 | German A1 HL | 4 | FLG 001”
  - equivalencies[IB-HISTORY-HL|4]:  ⟵ “IB 0261 | History HL | 4 | HIS 001”
  - equivalencies[IB-LATIN-HL|4]:  ⟵ “IB 0291 | Latin HL | 4 | FLG 001”
  - equivalencies[IB-MUSIC-HL|4]:  ⟵ “IB 0311 | Music HL | 4 | MUS 105”
  - equivalencies[IB-PHILOSOPHY-HL|4]:  ⟵ “IB 0321 | Philosophy HL | 4 | PHI 101”
  - equivalencies[IB-PHYSICS-HL|4]:  ⟵ “IB 0331 | Physics HL | 4 | PHY 201”
  - equivalencies[IB-PSYCHOLOGY-HL|4]:  ⟵ “IB 0341 | Psychology HL | 4 | PSY 201”
  - equivalencies[IB-SPANISH-HL|4]:  ⟵ “IB 0361 | Spanish A1 HL | 4 | FLG 001”
  - equivalencies[IB-THEATRE-HL|4]:  ⟵ “IB 0391 | Theatre HL | 4 | THE 101”
  - equivalencies[IB-VISUAL-ARTS-HL|4]:  ⟵ “IB 0411 | Visual Arts HL | 4 | ART 101”
### `24955840f9d45ef9` Midlands Technical College — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-three (sha256 162a7e6aaa14)
- issues: conflicting_sources:https://www.midlandstech.edu/admissions/testing-services/advanced-standing,https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-five,https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-four
- checks: {"distinct_exams": 26, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art 2-D Design | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art 3-D Design | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio: Drawing | Basic Drawing I | ART-111 | 3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | Biological Sciences I | BIO-101 | 4”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | Analyl Geom & Calculus I | MAT-140 | 4”
  - equivalencies[AP-CALCULUS-AB|8]:  ⟵ “Calclus BC s/Calc AB Subscore | Analyl Geom & Cal II | MAT-140 & MAT-141 | 8”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | College Chemistry I | CHM-110 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macroeconomics | Macroeconomics | ECO-210 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Microeconomics | Microeconomics | ECO-211 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “International English Language | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | Ecology & Ecology Lab | BIO-205 & BIO-206 | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | Western Civilization to 1689 | HIS-101 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | Soc/Behav. Science Credit | SCS-002 | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Virgil | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | Music Fundamentals | MUS-110 | 3”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C - Electricity & Magnet | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C - Mechanics | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | General Psychology | PSY-201 | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “Spanish Literature | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | Probability and Statistics | MAT-120 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History | American History: Discovery to 1877 | HIS-201 | 3”
  - … 4 more rows
### `2653398d2049439c` Midlands Technical College — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-four (sha256 bc93a13bc2bf)
- issues: conflicting_sources:https://www.midlandstech.edu/admissions/testing-services/advanced-standing,https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-five,https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-three
- checks: {"distinct_exams": 29, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art 2-D Design | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art 3-D Design | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio: Drawing | Basic Drawing I | ART-111 | 3”
  - equivalencies[AP-BIOLOGY|8]:  ⟵ “Biology | Bilogical Sciences I & Biological Sciences II | BIO 101 & BIO-102 | 8”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | Analyl Geom & Calculus I | MAT-140 | 4”
  - equivalencies[AP-CALCULUS-BC|8]:  ⟵ “Calculus BC w/Calc AB Subscore | Analyl Geom & Cal I & II | MAT-140 & MAT-141 | 8”
  - equivalencies[AP-CHEMISTRY|8]:  ⟵ “Chemistry | Collge Chemistry I & College Chemistry II | CHM-110 & CHM-111 | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macroeconomics | Macroeconomics | ECO-210 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Microeconomics | Microeconomics | EC0-211 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “International English Language | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|8]:  ⟵ “Environmental Science | Ecology & Ecology Lab & Lab Science Credit | BIO-204 & BIO-206 & SCI-001 | 8”
  - equivalencies[AP-EUROPEAN-HISTORY|6]:  ⟵ “European History | Western Civilization to 1689 & Western Civilization Post 1689 | HIS-101 & HIS-102 | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | Foreign Language Credit | SCS-002 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | Soc/Behav. Science Credit | FLG-001 | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Virgil | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Literature | Foreign Language Credit | MUS-105 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | Music Fundamentals | GEN-001 | 3”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 | College Physics 1 | PHY 201 | 4”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2 | College Physics 2 | PHY 202 | 4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C - Electricity & Magnet | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C - Mechanics | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | General Psychology | PSY-201 | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language | Foreign Language Credit | FLG-001 | 3”
  - … 7 more rows
### `8be0af2414fdc73d` Midlands Technical College — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.midlandstech.edu/admissions/testing-services/advanced-standing (sha256 7e828a53a965)
- issues: conflicting_sources:https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-five,https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-four,https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-three
- checks: {"distinct_exams": 29, "equivalencies": 42, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art 2-D Design | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art 3-D Design | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio: Drawing | Basic Drawing I | ART-111 | 3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | Biological Sciences I | BIO-101 | 4”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | Analyl Geom & Calculus I | MAT-140 | 4”
  - equivalencies[AP-CALCULUS-BC|8]:  ⟵ “Calculus BC s/Calc AB Subscore | Analyl Geom & Cal II | MAT-140 & MAT-141 | 8”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | College Chemistry I | CHM-110 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macroeconomics | Macroeconomics | ECO-210 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Microeconomics | Microeconomics | ECO-211 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “International English Language | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | Ecology & Ecology Lab | BIO-205 & BIO-206 | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | Western Civilization to 1689 | HIS-101 | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | Soc/Behav. Science Credit | SCS-002 | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Virgil | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | Music Fundamentals | MUS-110 | 3”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C - Electricity & Magnet | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C - Mechanics | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | General Psychology | PSY-201 | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “Spanish Literature | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | Probability and Statistics | MAT-120 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History | American History: Discovery to 1877 | HIS-201 | 3”
  - … 17 more rows
### `8ca12bb579ada4e2` Midlands Technical College — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://www.midlandstech.edu/scores-international-baccalaureate (sha256 37a50be944d9)
- issues: conflicting_sources:https://www.midlandstech.edu/admissions/testing-services
- checks: {"distinct_exams": 18, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|IB 0101]:  ⟵ “IB 0101 | Biology HL | 4 | BIO 101”
  - equivalencies[IB-BUSINESS-MANAGEMENT|IB 0111]:  ⟵ “IB 0111 | Business & Management | 4 | MGT 101”
  - equivalencies[IB-CHEMISTRY-HL|IB 0121]:  ⟵ “IB 0121 | Chemistry HL | 4 | CHM 110”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|IB 0131]:  ⟵ “IB 0131 | Computer Science HL | 4 | CPT 170”
  - equivalencies[IB-ECONOMICS-HL|IB 0151]:  ⟵ “IB 0151 | Economics HL | 4 | ECO 210”
  - equivalencies[IB-FILM-HL|IB 0181]:  ⟵ “IB 0181 | Film HL | 4 | ART 105”
  - equivalencies[IB-FRENCH-HL|IB 0191]:  ⟵ “IB 0191 | French A1 HL | 4 | FLG 001”
  - equivalencies[IB-FRENCH-HL|IB 0192]:  ⟵ “IB 0192 | French A2 HL | 4 | FLG 001”
  - equivalencies[IB-FRENCH-HL|IB 0211]:  ⟵ “IB 0211 | French B HL | 4 | FLG 001”
  - equivalencies[IB-GEOGRAPHY-HL|IB 0221]:  ⟵ “IB 0221 | Geography HL | 4 | GEO 102”
  - equivalencies[IB-GERMAN-HL|IB 0231]:  ⟵ “IB 0231 | German A1 HL | 4 | FLG 001”
  - equivalencies[IB-GERMAN-HL|IB 0241]:  ⟵ “IB 0241 | German A2 HL | 4 | FLG 001”
  - equivalencies[IB-GERMAN-HL|IB 0251]:  ⟵ “IB 0251 | German B HL | 4 | FLG 001”
  - equivalencies[IB-HISTORY-HL|IB 0261]:  ⟵ “IB 0261 | History HL | 4 | HIS 001”
  - equivalencies[IB-HISTORY-HL|IB 0281]:  ⟵ “IB 0281 | Islamic History HL | 4 | HIS 001”
  - equivalencies[IB-LATIN-HL|IB 0291]:  ⟵ “IB 0291 | Latin HL | 4 | FLG 001”
  - equivalencies[IB-MUSIC-HL|IB 0311]:  ⟵ “IB 0311 | Music HL | 4 | MUS 105”
  - equivalencies[IB-PHILOSOPHY-HL|IB 0321]:  ⟵ “IB 0321 | Philosophy HL | 4 | PHI 101”
  - equivalencies[IB-PHYSICS-HL|IB 0331]:  ⟵ “IB 0331 | Physics HL | 4 | PHY 201”
  - equivalencies[IB-PSYCHOLOGY-HL|IB 0341]:  ⟵ “IB 0341 | Psychology HL | 4 | PSY 201”
  - equivalencies[IB-SPANISH-HL|IB 0361]:  ⟵ “IB 0361 | Spanish A1 HL | 4 | FLG 001”
  - equivalencies[IB-SPANISH-HL|IB 0371]:  ⟵ “IB 0371 | Spanish A2 HL | 4 | FLG 001”
  - equivalencies[IB-SPANISH-HL|IB 0381]:  ⟵ “IB 0381 | Spanish B HL | 4 | FLG 001”
  - equivalencies[IB-THEATRE-HL|IB 0391]:  ⟵ “IB 0391 | Theatre HL | 4 | THE 101”
  - equivalencies[IB-VISUAL-ARTS-HL|IB 0411]:  ⟵ “IB 0411 | Visual Arts HL | 4 | ART 101”
### `eeb3142d8573d783` Midlands Technical College — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-five (sha256 66f6a159ffd8)
- issues: conflicting_sources:https://www.midlandstech.edu/admissions/testing-services/advanced-standing,https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-four,https://www.midlandstech.edu/admissions/testing-services/ap-exams-score-three
- checks: {"distinct_exams": 27, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art 2-D Design | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art 3-D Design | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio: Drawing | Basic Drawing I | ART-111 | 3”
  - equivalencies[AP-BIOLOGY|8]:  ⟵ “Biology | Bilogical Sciences I & Biological Sciences II | BIO 101 & BIO-102 | 8”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | Analyl Geom & Calculus I | MAT-140 | 4”
  - equivalencies[AP-CALCULUS-BC|8]:  ⟵ “Calculus BC w/Calc AB Subscore | Analyl Geom & Cal I & II | MAT-140 & MAT-141 | 8”
  - equivalencies[AP-CHEMISTRY|8]:  ⟵ “Chemistry | Collge Chemistry I & College Chemistry II | CHM-110 & CHM-111 | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics: Macroeconomics | Macroeconomics | ECO-210 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics: Microeconomics | Microeconomics | EC0-211 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “International English Language | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|8]:  ⟵ “Environmental Science | Ecology & Ecology Lab & Lab Science Credit | BIO-204 & BIO-206 & SCI-001 | 8”
  - equivalencies[AP-EUROPEAN-HISTORY|6]:  ⟵ “European History | Western Civilization to 1689 & Western Civilization Post 1689 | HIS-101 & HIS-102 | 6”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | Foreign Language Credit | SCS-002 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | Soc/Behav. Science Credit | FLG-001 | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Virgil | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Literature | Foreign Language Credit | MUS-105 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | Music Fundamentals | GEN-001 | 3”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C - Electricity & Magnet | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C - Mechanics | General Elective Credit | GEN-001 | 3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | General Psychology | PSY-201 | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “Spanish Literature | Foreign Language Credit | FLG-001 | 3”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | Probability and Statistics | MAT-120 | 3”
  - … 4 more rows
### `43a429402c554463` Morris College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.morris.edu/aid/student-accounts/cost-of-attendance/ (sha256 b35fc636817d)
- issues: arrangement_unlabeled, cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 6}
  - column:Tuition: 7532.0 ⟵ “Tuition | $7,532.00 | $7,532.00”
  - column:Technology Fee: 86.0 ⟵ “Technology Fee | 86.00 | 86.00”
  - column:Insurance Fee*: 621.0 ⟵ “Insurance Fee* | 621.00 | 621.00”
  - column:Room Fee: 1780.0 ⟵ “Room Fee | 1,780.00 | 1,780.00”
  - column:Board Fee: 2174.0 ⟵ “Board Fee | 2,174.00 | 2,174.00”
  - column:Student Activity Fee: 125.0 ⟵ “Student Activity Fee | 125.00 | 125.00”
  - column:Tuition: 7532.0 ⟵ “Tuition | $7,532.00 | $7,532.00”
  - column:Technology Fee: 86.0 ⟵ “Technology Fee | 86.00 | 86.00”
  - column:Insurance Fee*: 621.0 ⟵ “Insurance Fee* | 621.00 | 621.00”
  - column:Room Fee: 1780.0 ⟵ “Room Fee | 1,780.00 | 1,780.00”
  - column:Board Fee: 2174.0 ⟵ “Board Fee | 2,174.00 | 2,174.00”
  - column:Student Activity Fee: 125.0 ⟵ “Student Activity Fee | 125.00 | 125.00”
### `4e3b0664f27e9863` Morris College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.morris.edu/aid/student-accounts/schedule-of-fees/schedule-of-fees-2026-2027/ (sha256 e0782c713238)
- issues: arrangement_unlabeled, cost_period_semester
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - column:Tuition: 7932.0 ⟵ “Tuition | $7,932.00 | $7,932.00”
  - column:Technology Fee: 96.0 ⟵ “Technology Fee | 96.00 | 96.00”
  - column:Insurance Fee*: 652.0 ⟵ “Insurance Fee* | 652.00 | 652.00”
  - column:Room Fee: 1868.0 ⟵ “Room Fee | 1,868.00 | 1,868.00”
  - column:Board Fee: 2239.0 ⟵ “Board Fee | 2,239.00 | 2,239.00”
  - column:Student Activity Fee: 138.0 ⟵ “Student Activity Fee | 138.00 | 138.00”
  - column:TOTAL PER SEMESTER: 12925.0 ⟵ “TOTAL PER SEMESTER | $12,925.00 | $12,925.00”
  - column:Tuition: 7932.0 ⟵ “Tuition | $7,932.00 | $7,932.00”
  - column:Technology Fee: 96.0 ⟵ “Technology Fee | 96.00 | 96.00”
  - column:Insurance Fee*: 652.0 ⟵ “Insurance Fee* | 652.00 | 652.00”
  - column:Room Fee: 1868.0 ⟵ “Room Fee | 1,868.00 | 1,868.00”
  - column:Board Fee: 2239.0 ⟵ “Board Fee | 2,239.00 | 2,239.00”
  - column:Student Activity Fee: 138.0 ⟵ “Student Activity Fee | 138.00 | 138.00”
  - column:TOTAL PER SEMESTER: 12925.0 ⟵ “TOTAL PER SEMESTER | $12,925.00 | $12,925.00”
### `02b8ffeaa85daafd` Newberry College — transfer_policies 2023-24 [new] (labeled_in_source)
- source: https://www.newberry.edu/admission/transfer-students (sha256 856d5b0a91d7)
- issues: stale_year_label:2023-24
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C ⟵ “Transferring from a Technical College or Two-Year Institution If you've completed an Associate of Arts, Associate of Science, or Associate of Applied Science degree from an accredited institution with a grade of C or better, you will transfer to Newberry College with junior-level standing and have most general education requirements waived.”
  - max_transfer_credits: 72 ⟵ “A maximum of 72 credit hours will be accepted toward graduation for students transferring from a junior, technical, or community college.”
### `3eb999c1155e6625` North Greenville University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ngu.edu/wp-content/uploads/2025/08/SAP-Appeal.pdf (sha256 118bc78c150f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL I.”
### `a4fee416d02d608b` North Greenville University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.ngu.edu/wp-content/uploads/2026/04/2026-27-Special-Circumstance-Appeal-Form-1.pdf (sha256 0c30386cc99c)
- issues: semantic_review_required, conflicting_sources:https://www.ngu.edu/admissions/financial-aid/general-policies-and-disclosures/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 SPECIAL CIRCUMSTANCE/APPEAL FORM Federal Student Aid Regulations provide the potential for re-evaluation if your financial circumstances change.”
  - sentence: need_based_special_circumstances ⟵ “Submission of this form does not guarantee a change in your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “No.) City State Zip Code Special Circumstance Required Supporting Documentation (Examples) Student ID (Check all that apply) Phone Possible  Loss or Change of Employment/Reduction of • Typed Explanation of circumstances surrounding Income loss or reduction of income (who, effective date) • Most recent pay stub with year-to-date earnings. • Termination notice from employer (on business letterhead)”
  - sentence: need_based_special_circumstances ⟵ “I also realize that if I do not give proof when asked, the Special Circumstance will not be reviewed.”
  - sentence: need_based_special_circumstances ⟵ “We may require additional documentation if we have reason to believe that the information regarding the special circumstance is not properly documented.”
### `acdcff8170365123` North Greenville University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.ngu.edu/admissions/financial-aid/general-policies-and-disclosures/ (sha256 73abcec43b9a)
- issues: semantic_review_required, conflicting_sources:https://www.ngu.edu/wp-content/uploads/2026/04/2026-27-Special-Circumstance-Appeal-Form-1.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If any of these circumstances apply to you, please complete the 2026-27 Special Circumstance form or contact us at finaid@ngu.edu to find out if you qualify for a financial aid adjustment through our special circumstances review process.”
### `5f6228c23f4be90b` Piedmont Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.ptc.edu/cost-financial-aid/policies-and-faq/satisfactory-academic-progress-sap (sha256 4b86cf8abf3c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal of Financial Aid Ineligibility A student on Financial Aid Suspension may appeal loss of financial aid eligibility due to a failure to meet Satisfactory Academic Progress standards by submitting a Financial Aid Appeal Form, an Academic Plan and all requested documents to the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “If it is not mathematically possible for a student who is appealing to reach Satisfactory Academic Progress by the end of the next term, the student can be placed on an Academic Plan for a specific number of terms.”
### `ff4e59e2a6b51b3c` Piedmont Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.ptc.edu/index%2Ephp/cost-financial-aid/tuition-fees/how-pay/payment-plan (sha256 2b88a0414b7f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Terms and Conditions Lawful Presence Policy on Disbursements Refund Policy Residency Policy Satisfactory Academic Progress Special and Unusual Circumstances Student Rights and Responsibilities Verification F.A.Q.”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Terms and Conditions Lawful Presence Policy on Disbursements Refund Policy Residency Policy Satisfactory Academic Progress Special and Unusual Circumstances Student Rights and Responsibilities Verification F.A.Q.”
### `ccdbe1da0585d200` Piedmont Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ptc.edu/index%2Ephp/cost-financial-aid/tuition-fees (sha256 225a8ca33db5)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 8, "components_reconcile": true, "rows": 8}
  - column:*Tuition (defaults at 12 per term): 4860 ⟵ “*Tuition (defaults at 12 per term) | $4,860 | $4,860 | $5,400 | $5,400 | $5,670 | $5,670 | $7,008 | $7,008 | $8,916 | $8,916”
  - column:Fees: 300 ⟵ “Fees | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Living Expenses (Food & Housing): 7588 ⟵ “Living Expenses (Food & Housing) | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $16,930 | $16,930”
  - column:Books/Supplies: 2500 ⟵ “Books/Supplies | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500”
  - column:Transportation: 5108 ⟵ “Transportation | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108”
  - column:Personal/Misc.: 3150 ⟵ “Personal/Misc. | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - column:Loan Fees: 100 ⟵ “Loan Fees | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100”
  - column:Total: 23606 ⟵ “Total | $23,606 | $32,948 | $24,146 | $33,488 | $24,416 | $33,758 | $25,754 | $35,096 | $37,004 | $37,004”
  - column:*Tuition (defaults at 12 per term): 4860 ⟵ “*Tuition (defaults at 12 per term) | $4,860 | $4,860 | $5,400 | $5,400 | $5,670 | $5,670 | $7,008 | $7,008 | $8,916 | $8,916”
  - column:Fees: 300 ⟵ “Fees | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Living Expenses (Food & Housing): 16930 ⟵ “Living Expenses (Food & Housing) | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $16,930 | $16,930”
  - column:Books/Supplies: 2500 ⟵ “Books/Supplies | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500”
  - column:Transportation: 5108 ⟵ “Transportation | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108”
  - column:Personal/Misc.: 3150 ⟵ “Personal/Misc. | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - column:Loan Fees: 100 ⟵ “Loan Fees | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100”
  - column:Total: 32948 ⟵ “Total | $23,606 | $32,948 | $24,146 | $33,488 | $24,416 | $33,758 | $25,754 | $35,096 | $37,004 | $37,004”
  - column:*Tuition (defaults at 12 per term): 5670 ⟵ “*Tuition (defaults at 12 per term) | $4,860 | $4,860 | $5,400 | $5,400 | $5,670 | $5,670 | $7,008 | $7,008 | $8,916 | $8,916”
  - column:Fees: 300 ⟵ “Fees | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300 | $300”
  - column:Living Expenses (Food & Housing): 7588 ⟵ “Living Expenses (Food & Housing) | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $7,588 | $16,930 | $16,930 | $16,930”
  - column:Books/Supplies: 2500 ⟵ “Books/Supplies | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | $2,500”
  - column:Transportation: 5108 ⟵ “Transportation | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108 | $5,108”
  - column:Personal/Misc.: 3150 ⟵ “Personal/Misc. | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150 | $3,150”
  - column:Loan Fees: 100 ⟵ “Loan Fees | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100 | $100”
  - column:Total: 24416 ⟵ “Total | $23,606 | $32,948 | $24,146 | $33,488 | $24,416 | $33,758 | $25,754 | $35,096 | $37,004 | $37,004”
  - column:*Tuition (defaults at 12 per term): 5670 ⟵ “*Tuition (defaults at 12 per term) | $4,860 | $4,860 | $5,400 | $5,400 | $5,670 | $5,670 | $7,008 | $7,008 | $8,916 | $8,916”
  - … 39 more rows
### `864816a832cb1269` Presbyterian College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.presby.edu/admissions/special-circumstance/ (sha256 a8fec4c4910b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “APPLY NOW Admissions In This Section Why PC First-Year Students Transfer Students International Students Admitted Students Graduate Students Special Circumstances Resources for Counselors Visit Us Refer a Student Meet Our Team Returning Students Welcome back to Presbyterian College!”
### `057a5a93b746be20` Presbyterian College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.presby.edu/costs-and-aid/tuition-and-fees/ (sha256 3092a5089cb5)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 11}
  - on_campus:Tuition: 21530 ⟵ “Tuition | 21,530 | 21,530 | 43,060”
  - on_campus:Fees: 1550 ⟵ “Fees | 1,550 | 1,550 | 3,100”
  - on_campus:Housing*: 3542 ⟵ “Housing* | 3,542 | 3,542 | 7,084”
  - on_campus:Standard Meal Plan: 26 swipes, 8 exchanges, $250 Bonus Bucks: 3525 ⟵ “Standard Meal Plan: 26 swipes, 8 exchanges, $250 Bonus Bucks | 3,525 | 3,525 | 7,050”
  - on_campus:Books, course materials, supplies and equipment (laptop): 1000 ⟵ “Books, course materials, supplies and equipment (laptop) | 1,000 | 1,000 | 2,000”
  - on_campus:Transportation: 814 ⟵ “Transportation | 814 | 814 | 1,628”
  - on_campus:Loan Fees: 28 ⟵ “Loan Fees | 28 | 27 | 55”
  - on_campus:Miscellaneous personal expenses: 684 ⟵ “Miscellaneous personal expenses | 684 | 684 | 1,368”
  - on_campus:Subtotal for Indirect Costs: 2526 ⟵ “Subtotal for Indirect Costs | 2,526 | 2,525 | 5,051”
  - on_campus:Total Cost of Attendance: 32673 ⟵ “Total Cost of Attendance | $32,673 | $32,672 | $65,345”
  - on_campus:Total: 30147 ⟵ “Total | $30,147 | $30,147 | $60,294”
  - on_campus:Tuition: 21530 ⟵ “Tuition | 21,530 | 21,530 | 43,060”
  - on_campus:Fees: 1550 ⟵ “Fees | 1,550 | 1,550 | 3,100”
  - on_campus:Housing*: 3542 ⟵ “Housing* | 3,542 | 3,542 | 7,084”
  - on_campus:Standard Meal Plan: 26 swipes, 8 exchanges, $250 Bonus Bucks: 3525 ⟵ “Standard Meal Plan: 26 swipes, 8 exchanges, $250 Bonus Bucks | 3,525 | 3,525 | 7,050”
  - on_campus:Books, course materials, supplies and equipment (laptop): 1000 ⟵ “Books, course materials, supplies and equipment (laptop) | 1,000 | 1,000 | 2,000”
  - on_campus:Transportation: 814 ⟵ “Transportation | 814 | 814 | 1,628”
  - on_campus:Loan Fees: 27 ⟵ “Loan Fees | 28 | 27 | 55”
  - on_campus:Miscellaneous personal expenses: 684 ⟵ “Miscellaneous personal expenses | 684 | 684 | 1,368”
  - on_campus:Subtotal for Indirect Costs: 2525 ⟵ “Subtotal for Indirect Costs | 2,526 | 2,525 | 5,051”
  - on_campus:Total Cost of Attendance: 32672 ⟵ “Total Cost of Attendance | $32,673 | $32,672 | $65,345”
  - on_campus:Total: 30147 ⟵ “Total | $30,147 | $30,147 | $60,294”
  - on_campus:Tuition: 43060 ⟵ “Tuition | 21,530 | 21,530 | 43,060”
  - on_campus:Fees: 3100 ⟵ “Fees | 1,550 | 1,550 | 3,100”
  - on_campus:Housing*: 7084 ⟵ “Housing* | 3,542 | 3,542 | 7,084”
  - … 8 more rows
### `86f462b2f58da742` South Carolina State University — appeals 2025-26 [new] (labeled_in_source)
- source: https://scsu.edu/financial-aid/ (sha256 03e5dedd1ee6)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “For your convenience, they are all linked below. 2026-27 Academic Year FERPA Form Dependency Override Plus Instructions SAP Appeal Form Special Condition Form TEACH Grant Form Unusual Enrollment History Form Verification Gateway South Carolina Certification Form Financial Aid Adjustment Form Summer School Application for Financial Aid.”
### `90c86539ca78175a` South Carolina State University — appeals 2026-27 [new] (labeled_in_title)
- source: https://scsu.edu/financial-aid/2026-27_forms/2026-27%20SAP%20Appeal%20Form.pdf (sha256 31a1c827049b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Box 7386 * Orangeburg * SC * 29117 Phone: 803.536.7067 * Fax: 803.536.8420 2026-2027 Financial Aid Appeal for Satisfactory Academic Progress Examples of Appropriate Cause and Suggested Documentation: Financial Aid Appeals submitted for review must include all necessary documentation to support the existence of extenuating circumstances described and evidence that the circumstances have been resolv”
  - sentence: sap_appeal ⟵ “Box 7386 * Orangeburg * SC * 29117 Phone: 803.536.7067 * Fax: 803.536.8420 2026-2027 Financial Aid Appeal for Satisfactory Academic Progress Plan of Study Student Name: ___________________________________________________ SCSU Student ID #: 900_______________________ **** PLAN OF STUDY MUST BE SIGNED BY THE STUDENT’S ACADEMIC ADVISOR **** The plan of study should include: 1.”
### `00b1686b9549f716` Southern Wesleyan University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.swu.edu/on-campus/transfer-students/ (sha256 96662129df53)
- issues: conflicting_sources:https://www.swu.edu/on-campus/,https://www.swu.edu/on-campus/freshmen-students/,https://www.swu.edu/on-campus/tuition-costs/,https://www.swu.edu/online/tuition-costs/
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (2026-2027): 29500 ⟵ “Tuition (2026-2027) | $29,500”
  - column:Combined fees: 3000 ⟵ “Combined fees | $3,000”
  - column:Meal Plan: 6250 ⟵ “Meal Plan | $6,250”
### `13f485fb9e73e294` Southern Wesleyan University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.swu.edu/online/tuition-costs/ (sha256 e71b23ae37e7)
- issues: implausible_amount, conflicting_sources:https://www.swu.edu/on-campus/,https://www.swu.edu/on-campus/freshmen-students/,https://www.swu.edu/on-campus/transfer-students/,https://www.swu.edu/on-campus/tuition-costs/
- checks: {"columns": 1, "rows": 13}
  - column:Clinical for Student Teaching: 270 ⟵ “Clinical for Student Teaching | 270”
  - column:CLEP/DSST (Dantes) Fee: 50 ⟵ “CLEP/DSST (Dantes) Fee | 50”
  - column:Diploma Reorder Fee: 50 ⟵ “Diploma Reorder Fee | 50”
  - column:Education Practicum Fee-Undergraduate: 170 ⟵ “Education Practicum Fee-Undergraduate | 170”
  - column:Education Practicum Fee-Graduate: 450 ⟵ “Education Practicum Fee-Graduate | 450”
  - column:Finance Charge — 2-pay, 3-pay, 4-pay: 50 ⟵ “Finance Charge — 2-pay, 3-pay, 4-pay | 50”
  - column:Masters in Counseling Fee: 15 ⟵ “Masters in Counseling Fee | 15”
  - column:Masters of Business Administration MBAM 5003 Exam Fee: 200 ⟵ “Masters of Business Administration MBAM 5003 Exam Fee | 200”
  - column:Pre-Clinical for Student Teaching: 220 ⟵ “Pre-Clinical for Student Teaching | 220”
  - column:Returned Check/E-Check Fee: 32 ⟵ “Returned Check/E-Check Fee | 32”
  - column:Science Lab Fee: 75 ⟵ “Science Lab Fee | 75”
  - column:Student Resource Fee (per term): 410 ⟵ “Student Resource Fee (per term) | 410”
  - column:Tuition Late Fee: 50 ⟵ “Tuition Late Fee | 50”
### `4177897dfa545928` Southern Wesleyan University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.swu.edu/on-campus/ (sha256 91941424643a)
- issues: conflicting_sources:https://www.swu.edu/on-campus/freshmen-students/,https://www.swu.edu/on-campus/transfer-students/,https://www.swu.edu/on-campus/tuition-costs/,https://www.swu.edu/online/tuition-costs/
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (2026-2027): 29500 ⟵ “Tuition (2026-2027) | $29,500”
  - column:Combined fees: 3000 ⟵ “Combined fees | $3,000”
  - column:Meal Plan: 6250 ⟵ “Meal Plan | $6,250”
### `5bd3ef22544fd892` Southern Wesleyan University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.swu.edu/on-campus/freshmen-students/ (sha256 905f3b207f58)
- issues: conflicting_sources:https://www.swu.edu/on-campus/,https://www.swu.edu/on-campus/transfer-students/,https://www.swu.edu/on-campus/tuition-costs/,https://www.swu.edu/online/tuition-costs/
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (2026-2027): 29500 ⟵ “Tuition (2026-2027) | $29,500”
  - column:Combined fees: 3000 ⟵ “Combined fees | $3,000”
  - column:Meal Plan: 6250 ⟵ “Meal Plan | $6,250”
### `cacd778ef659eb0d` Southern Wesleyan University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.swu.edu/on-campus/tuition-costs/ (sha256 32f4c4f48cac)
- issues: conflicting_sources:https://www.swu.edu/on-campus/,https://www.swu.edu/on-campus/freshmen-students/,https://www.swu.edu/on-campus/transfer-students/,https://www.swu.edu/online/tuition-costs/
- checks: {"columns": 1, "rows": 3}
  - column:Tuition (2026-2027): 29500 ⟵ “Tuition (2026-2027) | $29,500”
  - column:Combined fees: 3000 ⟵ “Combined fees | $3,000”
  - column:Meal Plan: 6250 ⟵ “Meal Plan | $6,250”
### `6bd1335980657be0` Spartanburg Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sccsc.edu/admissions-aid/financial-aid/apply-fa/sap/ (sha256 8b99a40904be)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Mitigating circumstances are defined as, but not limited to, serious injury or illness of the student, death of an immediate family member (spouse, child, sibling, or parent), significant trauma in the student's life, or undue hardship caused by unusual circumstances.”
### `7582bf976e08d3e5` Spartanburg Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sccsc.edu/admissions-aid/financial-aid/apply-fa/sap/ (sha256 8b99a40904be)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Procedure for Reinstatement of Financial Aid Students who have had their aid terminated may reestablish eligibility for financial aid in one of two ways: 1) by enrolling in subsequent semester(s) at his/her own expense until satisfactory academic progress is achieved, or 2) by the appeals process, if approved (see below).”
  - sentence: sap_appeal ⟵ “The following steps shall be taken in the appeal process: The student must complete the Satisfactory Academic Progress Appeal form and return it to the Financial Aid Office along with supporting documentation.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeal form along with the supporting documentation will be reviewed by a designated staff/faculty member to determine whether or not mitigating circumstances did exist and the appeal is justified.”
### `4e4c09a6f9744d1a` Spartanburg Community College — credit_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_title)
- source: https://www.sccsc.edu/media/spartanburgcc/content-assets/documents/admissions-amp-financial-aid/student-amp-parent-resources/high-school-dual-credit/2024-2025-Dual-Enrollment__Early-College-Permission-and-Registration-Form_Accessible.pdf (sha256 f4794cf12994)
- issues: stale_year_label:2024-25
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “This student is using a 3.0 or higher High School GPA to establish eligibility in lieu of”
### `71f330e15f2f995e` Spartanburg Community College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_title)
- source: https://www.sccsc.edu/media/spartanburgcc/content-assets/documents/admissions-amp-financial-aid/student-amp-parent-resources/high-school-dual-credit/2025-2026-Dual-Enrollment__Early-College-Permission-and-Registration-Form_v2_Accessible.pdf (sha256 427f11e6e897)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Please indicate the appropriate permission level below: This student is using a 3.0 or higher High School GPA”
### `04a9d744a2d3502d` Tri-County Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tctc.edu/financial-aid/financial-aid-resources/special-circumstances/ (sha256 8a57f6e4f933)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “This is more commonly referred to as a dependency override.”
### `5c9ffbee59ef1034` Tri-County Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tctc.edu/financial-aid/financial-aid-resources/special-circumstances/ (sha256 8a57f6e4f933)
- issues: semantic_review_required, conflicting_sources:https://www.tctc.edu/media/43sgzmap/26-27-special-circumstances-request.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances | TCTC | Loading...”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Current circumstances are not always reflected accurately on the FAFSA since the tax information being reported is two years old.”
  - sentence: need_based_special_circumstances ⟵ “A special circumstance is a financial situation (loss of a job, etc.) that justifies an aid administrator adjusting data elements in the cost of attendance (COA) or in the Student Aid Index (SAI) calculation.”
  - sentence: need_based_special_circumstances ⟵ “Housing change due to homelessness Unusual Circumstance (commonly known as dependency override) Students who would normally be classified as a dependent student for FAFSA purposes may have an unusual circumstance that prevents access to parental tax information.”
  - sentence: need_based_special_circumstances ⟵ “An unusual circumstance is a condition that justifies an aid administrator making an adjustment to a student’s dependency status based on a unique situation that prevents an otherwise dependent student from accessing parental demographic and financial information.”
  - sentence: need_based_special_circumstances ⟵ “Complete and submit the respective form to finaid@tctc.edu for review: Special Circumstances Form [Downloadable PDF] or the Unusual Circumstances Form [Downloadable PDF], which will walk a student through needed information and documentation.”
### `6261514f45769748` Tri-County Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tctc.edu/financial-aid/financial-aid-resources/special-circumstances/ (sha256 8a57f6e4f933)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If your financial situation has changed significantly during the past two years, the Financial Aid Office may be able to help with a professional judgment – special circumstances appeal which results in a recalculation of financial need and can potentially lead to more federal and state grant aid.”
  - sentence: professional_judgment ⟵ “Again, the Financial Aid Office may be able to help with a professional judgment – unusual circumstances appeal which waives the need for parental information on the FAFSA, making the student independent for FAFSA purposes and giving students access to federal financial aid in spite of the absence of parental information.”
### `8c0978fe354b9fec` Tri-County Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tctc.edu/media/43sgzmap/26-27-special-circumstances-request.pdf (sha256 b64bd5d0c27d)
- issues: semantic_review_required, conflicting_sources:https://www.tctc.edu/financial-aid/financial-aid-resources/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Request Student’s Name _______________________TCTC Student’s ID _______________________ Student’s Email Student’s Phone Number Section A: SPECIAL CIRCUMSTANCE AND SUPPORTING DOCUMENTS Please check the appropriate conditions that have led you to request a special condition for the academic year.”
### `a2869781ec96aa36` Tri-County Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tctc.edu/financial-aid/satisfactory-academic-progress-sap/ (sha256 edacf98fa21f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “To appeal the students must complete all steps listed on the SAP appeal form, found in your My Financial Aid tile in your student portal under the General Links section of the Home tab.”
  - sentence: sap_appeal ⟵ “Steps to Submit a SAP Appeal Access the SAP appeal form, found in your My Financial Aid tile in your student portal under the General Links section of the Home tab.”
### `17554c3a093c8891` Tri-County Technical College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tctc.edu/media/qddpzmug/2024-2025-financial-aid-award-terms-conditions.pdf (sha256 2e6633f5b10a)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": false, "rows": 8}
  - column:TOTAL: 28048 ⟵ “TOTAL | 28,048 | 33,700”
  - column:Living Expenses: 17820 ⟵ “Living Expenses | 17,820 | 14,976”
  - column:Tuition (12 hr): 4448 ⟵ “Tuition (12 hr) | $4,448 | $4,448”
  - column:Books/Supplies: 2600 ⟵ “Books/Supplies | 2,600 | 2,600”
  - column:Living Expenses (2): 17820 ⟵ “Living Expenses | 17,820 | 23,472”
  - column:Transportation: 2122 ⟵ “Transportation | 2,122 | 2,122”
  - column:Personal Misc.: 1000 ⟵ “Personal Misc. | 1,000 | 1,000”
  - column:Loan Fees: 58 ⟵ “Loan Fees | 58 | 58”
  - column:TOTAL: 33700 ⟵ “TOTAL | 28,048 | 33,700”
  - column:Eligibility criteria for TCTC Foundation: 5560 ⟵ “Eligibility criteria for TCTC Foundation | Tuition (15 hr) | $5,560 | $5,560”
  - column:Scholarships are detailed on our website at: 2600 ⟵ “Scholarships are detailed on our website at | Other Fees | 2,600 | 2,600”
  - column:www.tctc.edu.: 2600 ⟵ “www.tctc.edu. | Books/Supplies | 2,600 | 2,600”
  - column:Living Expenses: 14976 ⟵ “Living Expenses | 17,820 | 14,976”
  - column:TERMS OF AWARD: 2122 ⟵ “TERMS OF AWARD | Transportation | 2,122 | 1,179”
  - column:The financial aid listed on your aid letter is based on: 1000 ⟵ “The financial aid listed on your aid letter is based on | Personal Misc. | 1,000 | 1,000”
  - column:(1) your cost of attendance, (2) your (SAI) Student: 58 ⟵ “(1) your cost of attendance, (2) your (SAI) Student | Loan Fees | 58 | 58”
  - column:Aid Index as determined by the FAFSA, and (3) your: 31760 ⟵ “Aid Index as determined by the FAFSA, and (3) your | TOTAL | 31,760 | 27,973”
  - column:Tuition (12 hr): 4448 ⟵ “Tuition (12 hr) | $4,448 | $4,448”
  - column:Books/Supplies: 2600 ⟵ “Books/Supplies | 2,600 | 2,600”
  - column:Living Expenses (2): 23472 ⟵ “Living Expenses | 17,820 | 23,472”
  - column:Transportation: 2122 ⟵ “Transportation | 2,122 | 2,122”
  - column:Personal Misc.: 1000 ⟵ “Personal Misc. | 1,000 | 1,000”
  - column:Loan Fees: 58 ⟵ “Loan Fees | 58 | 58”
  - column:Eligibility criteria for TCTC Foundation: 5560 ⟵ “Eligibility criteria for TCTC Foundation | Tuition (15 hr) | $5,560 | $5,560”
  - column:Scholarships are detailed on our website at: 2600 ⟵ “Scholarships are detailed on our website at | Other Fees | 2,600 | 2,600”
  - … 5 more rows
### `7a0aae9e397eb0c2` Tri-County Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.tctc.edu/financial-aid/student-financial-aid-services/tuition-fees/tuition-for-fall-2026-summer-2027/ (sha256 e1f2c0ea6f46)
- issues: residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 4765 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $4,765 | $4,765 | $5,956”
  - with_parents_or_family:Other Fees (FEES): 0 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - with_parents_or_family:Living Expenses (RB): 18453 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - with_parents_or_family:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - with_parents_or_family:Transportation (TRAN): 2268 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - with_parents_or_family:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - with_parents_or_family:Total: 29144 ⟵ “Total | $29,144 | $35,369 | $31,076”
  - off_campus_not_with_family:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 4765 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $4,765 | $4,765 | $5,956”
  - off_campus_not_with_family:Other Fees (FEES): 0 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - off_campus_not_with_family:Living Expenses (RB): 24678 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - off_campus_not_with_family:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - off_campus_not_with_family:Transportation (TRAN): 2268 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - off_campus_not_with_family:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 35369 ⟵ “Total | $29,144 | $35,369 | $31,076”
  - on_campus:Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI): 5956 ⟵ “Tuition (defaults at 12 per term for non bridge and 15 per term for Bridge)* (TUI) | $4,765 | $4,765 | $5,956”
  - on_campus:Other Fees (FEES): 2586 ⟵ “Other Fees (FEES) | $0 | $0 | $2,586”
  - on_campus:Living Expenses (RB): 17616 ⟵ “Living Expenses (RB) | $18,453 | $24,678 | $17,616”
  - on_campus:Books/Supplies (BS): 2600 ⟵ “Books/Supplies (BS) | $2,600 | $2,600 | $2,600”
  - on_campus:Transportation (TRAN): 1260 ⟵ “Transportation (TRAN) | $2,268 | $2,268 | $1,260”
  - on_campus:Personal/Misc (PERS): 1000 ⟵ “Personal/Misc (PERS) | $1,000 | $1,000 | $1,000”
  - on_campus:Loans Fee (LFEE): 58 ⟵ “Loans Fee (LFEE) | $58 | $58 | $58”
  - on_campus:Total: 31076 ⟵ “Total | $29,144 | $35,369 | $31,076”
### `24a4f4d1fcc3765d` Tri-County Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_title)
- source: https://www.tctc.edu/media/nhglnxro/cpc-dualenroll_orientationhandbook_2627_v2_print.pdf (sha256 3a1818349421)
- issues: multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 1}
  - per_credit_hour_charge: 185.33 ⟵ “The tenative 2026-2027 tuition rate is $185.33 per credit hour. Tuition for one 3-credit hour course is”
  - eligibility_tier: 2.0 ⟵ “by Lottery Tuition Assistance. LIFE Scholarship is not       of Satisfactory Academic Progress (2.0 GPA, 67%”
### `ebaecc8cbad40c44` Tri-County Technical College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_title)
- source: https://www.tctc.edu/media/zwvc0k1w/dualenroll_orientationhandbook_2526_02.pdf (sha256 209406d61889)
- issues: stale_year_label:2025-26, multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 1}
  - per_credit_hour_charge: 185.33 ⟵ “The tenative 2025-2026 tuition rate is $185.33 per credit hour. Tuition for one 3-credit hour course is”
  - eligibility_tier: 2.0 ⟵ “by Lottery Tuition Assistance. LIFE Scholarship is not       of Satisfactory Academic Progress (2.0 GPA, 67%”
### `3383378c1e4fa375` Trident Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tridenttech.edu/cost/financial-aid/palmetto_fellows.html (sha256 33aef4423e16)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Important Links Educational Opportunity Center at Trident Technical College (FAFSA assistance) Financial Literacy Program at TTC Federal Student Aid YouTube Channel (how-to videos) Federal Financial Aid Help Center (infographics, videos, forms, brochures, etc.) Financial Aid Adjustments for Unusual and Special Circumstances Instagram Facebook Twitter YouTube LinkedIn 7000 Rivers Ave.”
### `66b8d97174ffdf1e` Trident Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tridenttech.edu/about/policies/16_adm_reg/16-5-2.html (sha256 e657a404271b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “STATUS OF APPEALS If a Satisfactory Academic Progress appeal is denied: The student is placed on Federal financial aid suspension and attends at the student's own expense.”
### `02a64d5f866b6747` University of South Carolina Aiken — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.usca.edu/media/usca/departments/financial-aid/sap-policy/2223-SAP-Appeal-Form.pdf (sha256 cdd4c9b8f382)
- issues: semantic_review_required, conflicting_sources:https://www.usca.edu/media/usca/departments/financial-aid/sap-policy/SAP-Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other (please specify): • Letter of appeal from student addressing academic performance. • Supporting documentation of special circumstance(s) For students reaching Maximum Timeframe • Letter of appeal from student addressing academic performance.”
### `49f380ab156961e7` University of South Carolina Aiken — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.usca.edu/media/usca/departments/financial-aid/sap-policy/SAP-Policy.pdf (sha256 d0100e967c68)
- issues: semantic_review_required, conflicting_sources:https://www.usca.edu/media/usca/departments/financial-aid/sap-policy/2223-SAP-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal Process and Related Information If a student has experienced special circumstances during the evaluation period that he/she did not meet SAP standards, an appeal to request reinstatement of financial aid eligibility can be submitted.”
  - sentence: sap_appeal ⟵ “Acceptable supporting documentation is outlined on the Financial Aid Satisfactory Academic Progress Appeal Form.”
### `57cb6941a19a4668` University of South Carolina Aiken — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.usca.edu/media/usca/departments/financial-aid/sap-policy/SAP-Policy.pdf (sha256 d0100e967c68)
- issues: semantic_review_required, conflicting_sources:https://www.usca.edu/media/usca/departments/financial-aid/sap-policy/2223-SAP-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are limited to 1) serious illness to student or immediate family member, 2) death of an immediate family member, 3) job-related issue, 4) victim of a crime, and 5) other events leading to inability to successfully complete course requirements.”
### `bafe12f3cc414d77` University of South Carolina Aiken — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.usca.edu/media/usca/departments/financial-aid/sap-policy/2223-SAP-Appeal-Form.pdf (sha256 cdd4c9b8f382)
- issues: semantic_review_required, conflicting_sources:https://www.usca.edu/media/usca/departments/financial-aid/sap-policy/SAP-Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “OFFICE OF FINANCIAL AID 471 University Parkway | Aiken, SC 29801 803-641-3476 | Fax: 803-643-6840 Email: stuaid@usca.edu Financial Aid Satisfactory Academic Progress Appeal Student’s Name: ____________________________________________ USC ID: ___________________________________ Semester for appeal (i.e.”
  - sentence: sap_appeal ⟵ “Once your appeal has been reviewed by the Financial Aid Satisfactory Academic Progress (SAP) Appeals Committee, you will be notified of the decision.”
  - sentence: sap_appeal ⟵ “All decisions by the Financial Aid SAP Appeals Committee are FINAL.”
### `m0fc213d252a70a6` University of South Carolina Aiken — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://www.usca.edu/media/usca/site-assets/sample-content/documents/admissions/Dual-Enrollment-FAQ-(updated-August-2026).pdf (sha256 3dd8f26c6bb4)
- issues: ambiguous_year_labels, multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.5 ⟵ “Be in the top 25% of your class and/or have a 3.5+ GPA on the SC UGP”
  - eligibility_tier: 3.5 ⟵ “consider your options carefully.                                    3.5+ GPA on the SC UGP”
  - per_credit_hour_charge: 66 ⟵ “June. The current rate for 2026-27 is $66/credit hour (as       to be able to log in to search the database). Course”
  - per_credit_hour_charge: 433.25 ⟵ “compared to $433.25/credit hour part-time SC resident           listings typically appear in early March for the fall”
  - per_credit_hour_charge: 13 ⟵ “technology support ($13/credit hour). Textbook rentals          Which courses are most popular among dual”
### `12d4be6e5cdaf421` University of South Carolina Aiken — transfer_policies 2024-25 [new] (labeled_in_source)
- source: https://www.usca.edu/admissions/admission-types/transfer/change-of-campus/ (sha256 a46e271fa237)
- issues: stale_year_label:2024-25
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 12 ⟵ “Institutional maximums of transferable credit The senior year of work (30 semester hours) must be completed in residence at USCA, and at least 12 hours of the student’s major courses must be earned at USCA.”
### `24b8a90c131d2620` University of South Carolina Beaufort — appeals 2002-03 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/scholarships/state-granted-scholarships/hope-scholarship/pdfs/QandA_HOPE.pdf (sha256 dc17fd39b6de)
- issues: stale_year_label:2002-03, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If an extenuating circumstance prevented you from receiving the maximum terms for the HOPE Scholarship, you may submit an appeal.”
### `5769beebdf40b6a9` University of South Carolina Beaufort — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/satisfactory-academic-progress/graduates.html (sha256 6a4d210e6a67)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.uscb.edu/admissions/tuition-and-financial-aid/satisfactory-academic-progress/index.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “This hold will stop the disbursement of financial aid for the following term until a successful SAP appeal is submitted, provided there are new extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Academic plans may be developed by the Financial Aid Director, Academic Advisors, or members of the Satisfactory Academic Progress Appeal Committee.”
### `b9ed122e1829dfea` University of South Carolina Beaufort — appeals 2025-26 [new] (labeled_in_url)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/forms/pdfs/2025-2026%20Satisfactory%20Academic%20Progress%20Appeal%20Form.pdf (sha256 9e27f46d7db7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “University of South Carolina Beaufort Financial Aid/Veterans Affairs Office 801 Carteret Street ♦ Beaufort, SC 29902 Office: 843-521-3104 ♦ Fax: 843-521-3194 ♦ www.uscb.edu Email: uscbfina@uscb.edu Instructions for Filing the Satisfactory Academic Progress Appeal Form Students who are not eligible for federal, state, or institutional financial aid due to academic reasons have the option to appeal ”
  - sentence: sap_appeal ⟵ “To assist you in completing the SAP Appeal Form, please read the following instructions carefully.”
  - sentence: sap_appeal ⟵ “Complete the SAP Appeal Form (second page) 2.”
### `f3c1d73c68fe3e20` University of South Carolina Beaufort — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/satisfactory-academic-progress/index.html (sha256 c2fe775b3542)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.uscb.edu/admissions/tuition-and-financial-aid/satisfactory-academic-progress/graduates.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP Hold Students’ on a SAP warning who fail to meet the cumulative GPA of 2.0 and completion rate percentage 67% will be placed on Satisfactory Academic Progress Hold (SAP Hold), which prevents the next term’s aid disbursement until submitting a successful SAP appeal if you have new extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Academic plans may be developed by the Financial Aid Director, Academic Advisors, or members of the Satisfactory Academic Progress Appeal Committee.”
### `ce92e36966224f00` University of South Carolina Beaufort — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/index.html (sha256 1223abc4ff47)
- issues: cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 5172.0 ⟵ “Tuition | $5,172.00 | $10,695.00”
  - column:Fees**: 368.0 ⟵ “Fees** | $368.00 | $368.00”
  - column:Housing (Single Room in Palmetto Village): 4125.0 ⟵ “Housing (Single Room in Palmetto Village) | $4,125.00 | $4,125.00”
  - column:Meal Plan (Plan 3 - Unlimited + $200 Declining Balance Meal Exchange): 2435.0 ⟵ “Meal Plan (Plan 3 - Unlimited + $200 Declining Balance Meal Exchange) | $2,435.00 | $2,435.00”
  - column:ESTIMATED TOTALPER SEMESTER: 12100.0 ⟵ “ESTIMATED TOTALPER SEMESTER | $12,100.00 | $17,623.00”
### `ea65412f9a55a05a` University of South Carolina Beaufort — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.uscb.edu/admissions/tuition-and-financial-aid/index.html (sha256 1223abc4ff47)
- issues: cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 10695.0 ⟵ “Tuition | $5,172.00 | $10,695.00”
  - column:Fees**: 368.0 ⟵ “Fees** | $368.00 | $368.00”
  - column:Housing (Single Room in Palmetto Village): 4125.0 ⟵ “Housing (Single Room in Palmetto Village) | $4,125.00 | $4,125.00”
  - column:Meal Plan (Plan 3 - Unlimited + $200 Declining Balance Meal Exchange): 2435.0 ⟵ “Meal Plan (Plan 3 - Unlimited + $200 Declining Balance Meal Exchange) | $2,435.00 | $2,435.00”
  - column:ESTIMATED TOTALPER SEMESTER: 17623.0 ⟵ “ESTIMATED TOTALPER SEMESTER | $12,100.00 | $17,623.00”
### `17dc8807b0ab6e24` University of South Carolina-Columbia — appeals 2026-27 [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php (sha256 76a73e8915fb)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You are welcome to complete our scholarship appeal form, and we will consider your request should additional funds become available.”
### `da3315013e197e3f` University of South Carolina-Columbia — appeals 2026-27 [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Appeals will only be accepted electronically through the Scholarship Appeal Form that is accessible through Self Service Carolina.”
### `dc0915b4940f8da0` University of South Carolina-Columbia — appeals 2026-27 [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please note that this is separate from any Satisfactory Academic Progress appeal that a student might have to complete for federal financial aid.”
### `299fc5f1269ba70a` University of South Carolina-Columbia — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php (sha256 f5e51f74cc23)
- issues: residency_unknown, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php,https://www.sc.edu/admissions-at-sc/tuition-aid/index.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 12288 ⟵ “Tuition | $12,288”
  - column:Technology Fee: 400 ⟵ “Technology Fee | $400”
  - column:Weighted Average Program Fee: 1580 ⟵ “Weighted Average Program Fee | $1,580”
  - column:Housing: 11432 ⟵ “Housing | $11,432”
  - column:Food: 5902 ⟵ “Food | $5,902”
  - column:Total: 31602 ⟵ “Total | $31,602”
### `492f056af1a9772b` University of South Carolina-Columbia — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php (sha256 f3a89e979fc3)
- issues: residency_unknown, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php,https://www.sc.edu/admissions-at-sc/tuition-aid/index.php
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - on_campus:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - on_campus:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - on_campus:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - on_campus:Housing: 11432 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - on_campus:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - on_campus:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - on_campus:Transportation: 2670 ⟵ “Transportation | $2,670 | $2,690 | $2,690”
  - on_campus:Total: 66394 ⟵ “Total | $66,394 | $66,394 | $57,592”
  - off_campus_not_with_family:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - off_campus_not_with_family:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - off_campus_not_with_family:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - off_campus_not_with_family:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - off_campus_not_with_family:Housing: 11432 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - off_campus_not_with_family:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - off_campus_not_with_family:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - off_campus_not_with_family:Transportation: 2690 ⟵ “Transportation | $2,670 | $2,690 | $2,690”
  - off_campus_not_with_family:Total: 66394 ⟵ “Total | $66,394 | $66,394 | $57,592”
  - with_parents_or_family:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - with_parents_or_family:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - with_parents_or_family:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - with_parents_or_family:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - with_parents_or_family:Housing: 2630 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - with_parents_or_family:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - with_parents_or_family:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - … 2 more rows
### `bad06e51e03d10b2` University of South Carolina-Columbia — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sc.edu/admissions-at-sc/tuition-aid/index.php (sha256 a870ebe0a530)
- issues: residency_unknown, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php,https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 12288 ⟵ “Tuition | $12,288”
  - column:Technology Fee: 400 ⟵ “Technology Fee | $400”
  - column:Weighted Average Program Fee: 1580 ⟵ “Weighted Average Program Fee | $1,580”
  - column:Housing: 11432 ⟵ “Housing | $11,432”
  - column:Food: 5902 ⟵ “Food | $5,902”
  - column:Total: 31602 ⟵ “Total | $31,602”
### `654c98be96cd0230` University of South Carolina-Columbia — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 23, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | E, D, C B, A | BIOL 101, 101L BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | E, D, C, B, A | CSE 101 and CSCE 001T”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | E, D, C B, A | CHEM 111 and 111L CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | E, D C, B, A | ECON 221 ECON 221 and 222”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | E, D, C, B, A | GEOG 103”
  - equivalencies[IB-HISTORY|History: U.S.]:  ⟵ “History: U.S. | E, D, C, B, A | HIST 112”
  - equivalencies[IB-HISTORY|History: European]:  ⟵ “History: European | E, D, C, B, A | HIST 102”
  - equivalencies[IB-HISTORY|History: International]:  ⟵ “History: International | E, D, C, B, A | HIST 001T”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | E, D, C B, A | PHYS 211 and 211L PHYS 211, 211L, 212 and 212L”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | E, D, C, B, A | PSYC 101”
  - equivalencies[IB-HISTORY|History: U.S./International/European]:  ⟵ “History: U.S./International/European | E, D, C, B, A | HUMA 001T”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 101 and 101L | 5, 6, 7 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business and Management | 4 | MGMT 371 | 5, 6, 7 | MGMT 371 and 376”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 111 and 111L | 5, 6, 7 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|4, 5]:  ⟵ “Economics | 4, 5 | ECON 221 | 6, 7 | ECON 221 and 222”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on either)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on either) | ENGL 101 | 5, 6, 7 (on either or both) | ENGL 101 and 102”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on both)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[IB-FILM|4]:  ⟵ “Film | 4 | HUMA 002T |  | ”
  - equivalencies[IB-FRENCH|4, 5]:  ⟵ “French B* | 4, 5 | FREN 122 and 209 | 6, 7 | FREN 209 and 210”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOG 103 |  | ”
  - equivalencies[IB-GERMAN|4, 5]:  ⟵ “German B* | 4, 5 | GERM 122 and 210 | 6, 7 | GERM 210 and 211”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | POLI 101 |  | ”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of the Americas | 4 | HIST 102 and 112 |  | ”
  - equivalencies[IB-LATIN|4]:  ⟵ “Latin B* | 4 | LATN 121 and 122 | 5, 6 | LATN 122 and 301”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4]:  ⟵ “Mathematics Analysis and Approaches | 4 | MATH 141 | 5, 6, 7 | MATH 141 and 142”
  - … 9 more rows
### `80a24077bd1bf23a` University of South Carolina-Columbia — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 37, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | AFAM 201 |  | ”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “American Government and Politics | 3 | POLI 201 |  | ”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research Course | 3 | UNEL 002T |  | ”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar Course | 3 | UELC 002T |  | ”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTE 101 | 4 | ARTH 105”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art Studio, 2-D | 3 | ARTS 103 |  | ”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art Studio, 3-D | 3 | ARTS 104 |  | ”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio, Drawing | 3 | ARTS 111 |  | ”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101 and 101L | 4, 5 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 111 and 111L | 4, 5 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | 3 | CHIN 121 | 4, 5 | CHIN 121 and 122”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics* | 3 | POLI 103C |  | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSCE 101 |  | ”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics-Macro | 3 | ECON 222 |  | ”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics-Micro | 3 | ECON 221 |  | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on either)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on either) | ENGL 101 | 5 (on either or both) | ENGL 101 and 102”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on both)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVR 101 & ENVR 101L |  | ”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 101 | 4, 5 | HIST 101 and 102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on either)]:  ⟵ “French Language OR French Literature** | 3 (on either) | FREN 121 | 4, 5 (on either or both) | FREN 121 and 122”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on both)]:  ⟵ “French Language OR French Literature** | 3 (on both) | FREN 121 AND 122 |  | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German** | 3 | GERM 121 | 4, 5 | GERM 121 and 122”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 210 |  | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | 3 | ITAL 121 | 4, 5 | ITAL 121 and 122”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese | 3 | JAPA 121 | 4, 5 | JAPA 121 and 122”
  - … 16 more rows
### `e73529fcf9b7ccd5` University of South Carolina-Columbia — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_transfers/index.php (sha256 28dce6fabe62)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transferring credits from other institutions USC generally accepts nonremedial coursework completed at regionally accredited institutions with a grade of C- or better.”
### `3d678708629de88a` University of South Carolina-Lancaster — appeals 2026-27 [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php (sha256 76a73e8915fb)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You are welcome to complete our scholarship appeal form, and we will consider your request should additional funds become available.”
### `573538f7e2ce2037` University of South Carolina-Lancaster — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/system_and_campuses/palmetto_college/internal/documents/remdocs/financial_aid/fasap_appeal_and_academic_plan_updated_may_2026.pdf (sha256 83efa75ff5df)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal and Academic Plan Academic Year: _______________________ Appeal Term: ______________________ Student’s Name: ___________________________________________________________ USC ID: _______________ Email Address: ______________________________________________________________________________________ Use this form to complete your financial aid satisfactory academic ”
  - sentence: sap_appeal ⟵ “PCCFAO | Satisfactory Academic Progress Appeal and Academic Plan | May 2026 Reason for Appeal (check all that apply) Student’s Illness or Medical Issue.”
  - sentence: sap_appeal ⟵ “Academic Advisor’s Signature: __________________________________________________ Date: ______________ Print name and title/position: ________________________________________________________________________ PCCFAO | Satisfactory Academic Progress Appeal and Academic Plan | May 2026”
### `5a7f137189e6efe5` University of South Carolina-Lancaster — appeals 2027-28 [new] (labeled_in_heading)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/current_students/financial_aid/index.php (sha256 23caf3549021)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (FASAP) Policy and Appeals All students must maintain Financial Aid Satisfactory Academic Progress (FASAP).”
  - sentence: sap_appeal ⟵ “SAP Appeal Deadlines | Term Student Desires Financial Aid | Priority Deadline | Deadline To Submit Appeal | Fall | August 1st | September 30th | Spring | December 1st | January 30th | Summer | April 1st | May 30th Any appeals received after these dates may not be reviewed, as there would be insufficient time remaining in the semester for the full processing of financial aid.”
### `5e1d0d49ec7dfd65` University of South Carolina-Lancaster — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/system_and_campuses/palmetto_college/internal/documents/remdocs/financial_aid/fasap_appeal_and_academic_plan_updated_may_2026.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please note that this is separate from any Satisfactory Academic Progress appeal that a student might have to complete for federal financial aid.”
### `ee0beec791ef9666` University of South Carolina-Lancaster — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Appeals will only be accepted electronically through the Scholarship Appeal Form that is accessible through Self Service Carolina.”
### `f24665fce7d679b6` University of South Carolina-Lancaster — appeals 2024-25 [new] (labeled_in_url)
- source: https://www.sc.edu/about/system_and_campuses/palmetto_college/internal/documents/finaid/2024_25_sap_appeal_and_academic_plan.pdf (sha256 4e3cc22e1585)
- issues: stale_year_label:2024-25, semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Appeal Student’s Name: ____________________________________________________ USC ID: _________________________ Use this form to complete your financial aid appeal.”
### `0935fc8d6378e6d5` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,252.00 ⟵ “Kate Holland | Physiological Correlates of Hostility and Anxiety: Examining Changes in Heart Rate and Diastolic BP as a Function of Exposure to Positively Valenced Infant Vocalizations | $7,252.00”
### `0cee1ee89c2f443a` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Dr. Chris Bundrick | Woven Between the Lines: The Short Fiction of Elliott White Springs | $2,500”
### `18ffc199debb431f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,700 ⟵ “Dr. Bruce Nims | Revision for Publication of Three Conference Papers on Akira Kurosawa | $3,700”
### `1a9dd273e0b7b5ff` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,491.00 ⟵ “Elizabeth Easley | “Comparison of Fitness Measures and Physical Activity Levels in NJCAA Female Athletes between Their Competitive Season and Their Off-Season” | $7,491.00”
### `1c26879a5b354e4c` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,725 ⟵ “Dr. Courtney Catledge | Evaluation of lung capacity utilizing serial peak flow results in students from 6-12 grades participating in Band and implications for asthma outcomes | $7,725”
### `1c6d45ea95c5d2ae` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,090.00 ⟵ “Brooke Bauer and Brittany Taylor-Driggers | The Ripple Effect of Historical and Curatorial Research in Public Spaces | $5,090.00”
### `20d8910b06d7acca` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,180 ⟵ “Dr. Sarah Hunt-Sellhorst | Differences Among Traditional Body Composition Measures Across Age and Activity Level in Older Adults | $2,180”
### `2732a08f3b693e5f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $9,378.80 ⟵ “Sahar Agahasafari | “Multimedia Arts Learning: Connecting STEAM among Special Education Students” | $9,378.80”
### `27a3e8448a33666b` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $4,845 ⟵ “Susan Cruise | Factors of Risk Status and Persistence of Undergraduate Students at the University of South Carolina Lancaster | $4,845”
### `2b7e589b58c5e8c8` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,474 ⟵ “Dr. Shemsi Alhaddad | Hecke Algebras for Monomial Groups | $1,474”
### `302c3a8b05117c8e` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,927 ⟵ “Brittany Taylor | Drawing in Clay: An Artistic Collaboration to create a Body of Work with a Catawba Potter, Phase 1 of 3 Phases | $8,927”
### `37366f242ed5f69d` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,430 ⟵ “Jerrod Yarosh | Exploring Perceptions of Racial Bias in Pro-Environmental Behaviors | $3,430”
### `3c5c5a2f770c4b8f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,957.13 ⟵ “Brooke Bauer | An Enduring People: Catawba Women and Education | $3,957.13”
### `3e3a31659d2d511a` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Dr. Eric Wolfe | Summer stipend for revision and re-submission of manuscripts for publication | $2,500”
### `41536205806ebaef` University of South Carolina-Lancaster — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/apply/scholarships/index.php (sha256 67ca4488046a)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - eligibility_summary: Freshmen and Upper Classmen who submit applications after the above deadlines will be considered if funding is available and if they meet the minimum eligibility requirements. Awards will be limited to $750.00 per academic year. Decisions will be made starting in June, when final grades are available for the prior academic year. Late Scholarships are for one year only. ⟵ “July. 15th | Late Scholarship Application Deadline | Freshmen and Upper Classmen who submit applications after the above deadlines will be considered if funding is available and if they meet the minimum eligibility requirements. Awards will be limited to $750.00 per academic year. Decisions will be ”
### `4353356e613dd567` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,003.00 ⟵ “Peter Siepel | Who Goes There? The Problem of Identifying Epistemic Trespassers | $7,003.00”
### `468b8e0db8ada385` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,719 ⟵ “Dr. Nicol Augusté | Decoding the Catawba: Utilizing Archives to Unearth Post-Removal American Indian Realities | $7,719”
### `47101c64d2f593d3` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,664 ⟵ “Marybeth Berry | The Deconstruction of Athol Fugards "The Island" | $7,664”
### `48114ff5e9c0bcd5` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,987.00 ⟵ “Amy Gerald | Transcribing the Notebook of Archibald Henry Grimke | $2,987.00”
### `4cfc988e38bc9888` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,200 ⟵ “Marybeth Holloway | Expressive Actor/Lugering Method Training & Presentation of Work at La Mama Symposium for Directors | $7,200”
### `4f01fa538bdba3c6` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,704 ⟵ “Dr. Kate Holland | Extending the Capacity Model to Include High and Low Levels of Trait Anxiety: Examination of the Influence of Affective and Cognitive Stress on Cardiovascular Reactivity and Performance on an Affective Memory Task Using a Dual Task Paradigm | $5,704”
### `5109e35855a7fa28` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,000 ⟵ “Mary Beth Holloway | Expenses Related to a Theatrical Production in Osijek, Croatia | $8,000”
### `51dd962826f1b7c5` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,400 ⟵ “Dr. Mark Coe | Developing Research Skills and Making Contacts in Discipline | $2,400”
### `5751f3d02ae1edae` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,167 ⟵ “Dr. David Roberts | Cynicism within Culture and Education | $5,167”
### `5e486b839dcb9341` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,771 ⟵ “Dr. Dwayne Brown | The Effects of USCL Arts and Science Adventure Camp, Summer Experiences for Children in Grades 6 to 9 on Mathematics Achievement and Student Attitude | $8,771”
### `62af975e119d5c23` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,368 ⟵ “Dr. Todd Scarlet | Reproductive success of Red-Headed Woodpecker in Urban and Rural Habitats | $7,368”
### `66a4b95cdc3ff9a5` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,900.00 ⟵ “Christopher Judge | Radiometric Dating of Archaeological Features Containing Triangular Arrowheads from the Johannes Kolb Site | $1,900.00”
### `6a140f1022819676` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $0.00 ⟵ “Brittany Taylor-Driggers | Indigenous Art South Carolina: Redefining the Permanent Exhibition at the NASC | $0.00”
### `6b1d342b8d87248e` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,901.00 ⟵ “Claudia Heinemann-Priest | Cultivating Connections: Measuring the Impact of Native American-InspiredSustainable Urban Gardening on Community Engagement and Academic Scholarship | $7,901.00”
### `7146c1dc35dd4a72` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $821 ⟵ “Mike Reynolds | Travel to present conference paper Contesting Morality: Ideology and Sectional Conflict in Antebellum America | $821”
### `736aacdedac55d61` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,935.00 ⟵ “Stephen Criswell | Fieldwork for Navigating Indigenous Identity in Bi-Racial South Carolina Project | $1,935.00”
### `7a3119bcc297456e` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,437 ⟵ “Dr. Nicholas Guittar | Sexual Affinity/Sexual Identity Study | $3,437”
### `7bfa813182fc4789` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $6,923.00 ⟵ “Jobe, Allison | Revision of James W Ford: Black Communist Internationalist Visionary | $6,923.00”
### `7e5a87e04e6bccec` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,480.00 ⟵ “Evan Nooe | Archival Research in Disney Studies & Tourism History | $3,480.00”
### `8017df82640663e6` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Dr. Andy Yingst | A Context in which Finite Ergodicity is Generic | $2,500”
### `825eccd8b49d7326` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,182 ⟵ “Dr. David Norman | Various conference papers and proposals for publications | $3,182”
### `851b5d3dcc8ed809` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,252.00 ⟵ “Nicholas, Lawrence | Southern Gothic Hauntings and Feminist Marxism in Sharyn McCrumb's The Ballad of Frankie Silver | $7,252.00”
### `87b4c02bb5439586` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1500 (not awarded due to resignation; funds diverted to travel) ⟵ “Dr. Lori Robison | Continuing work toward the completion of book:Domesticating Difference: Gender, Race, and the Birth of a New South | $1500 (not awarded due to resignation; funds diverted to travel)”
### `882e9fb5c6bdbb4a` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,753(awarded in 2005, but deferred to 2006) ⟵ “Dr. Lisa Rashley | The Material Manifestation of Slavery: Phyllis Alesia Perry’s Stigmata and Pam Durban’s So Far Bac | $7,753(awarded in 2005, but deferred to 2006)”
### `8993637e1b4bedbe` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,437 ⟵ “Dr. Bettie Obi-Johnson | The Role of Nectar-Inhibiting Yeast in Plants | $2,437”
### `899eff8f7d1faf69` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,050 ⟵ “Dr. Fernanda Burke | Improving the Pharmacokinetics of Naturally Occurring Peptides: A Parallel Teaching Approach | $8,050”
### `8ac9225cdb61b568` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,000.00 ⟵ “Tyrie Rowell | The Fire within a Black Man That They Fear: Teaching through Rage | $5,000.00”
### `8b8a3a73942dcd17` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $6,229 ⟵ “Dr. B. H. Caraway | The Production of a cRNA Library for Spirillum volutans ATCC 19554 by Reverse Transcriptase Polymerase Chain Reaction (RT‑PCR) | $6,229”
### `8f27b89842b3f97f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $0.00 ⟵ “Kim Richardson | World Historical Association | $0.00”
### `9305fbfcc6bd595f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,198.00 ⟵ “Sarah Sellhorst | “Production of a Peer-Reviewed Manuscript about Faculty Perceptions on Undergraduate Research at a Predominantly 2-Year Campus” | $7,198.00”
### `93f16eab7ca63bc9` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Dr. Todd Scarlett | The Relationship Between Masting Trees and Potential Seed Dispersing Birds and Mammals | $2,500”
### `9bb65ae0ea04bf17` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,300 ⟵ “Dr. Howard Kingkade | Film Project | $3,300”
### `9cca2956635fc9d1` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,047 ⟵ “Dr. Annette Golonka | “Identification of Nectar-Inhibiting Microorganisms in Local Populations of the Plant Silene Carolinian” | $1,047”
### `9e909039059e23ee` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $800 ⟵ “Dr. Walt Collins | Indexing Project for the edited volume The Sefi Atta Reader, Walter Collins, editor | $800”
### `9f3813bbf4cf7f11` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,653 ⟵ “Brent Burgin | An Epistolary Review of Catawba Indian Letters to the Governor | $2,653”
### `a260a579dd21e958` University of South Carolina-Lancaster — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/apply/scholarships/index.php (sha256 67ca4488046a)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - eligibility_summary: Freshmen with a 3.00+ High School GPA on the SC Uniform Grading Scale ⟵ “Feb. 1st | Other Freshman Scholarships | Freshmen with a 3.00+ High School GPA on the SC Uniform Grading Scale”
### `a42c0af717f8ab70` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,252.00 ⟵ “Dana, Lawrence | Helen Oyeyemi and the Specter of Literary History: Channeling Shelly, Bronte, Alcott, and Burnett in the Icarus Girl | $7,252.00”
### `a7dd342f71a85430` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,214 ⟵ “Dr. Michael Bonner | Completion of Manuscript: Confederate Political Economy | $2,214”
### `aa2d37130d8a8310` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $4,316 ⟵ “Dr. Susan Cruise | Barriers in higher education for young adults who have aged out of the foster care system | $4,316”
### `afd9b20c8980349c` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $4,329 ⟵ “Fran Gardner | Book in Progress Working Title: Bravery, Ritual, and Practice: Elements of a Creative Life | $4,329”
### `b187914dc3d2d7d8` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,035 ⟵ “Dr. Sarah Sellhorst | The Relationship of Visceral Adipose Tissue to BMI and W/H Ratio in College Students Aged 18-25 years | $8,035”
### `b26b7559e4c3a9ea` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,555 ⟵ “Dr. Sarah Hunt | Relationship of BMI and Body Composition in Predicting Frailty and Quality of Life | $1,555”
### `b50778fc19084d63` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,258 ⟵ “Adam Biggs | Strange Cures: Book Proposal | $8,258”
### `b8d050d0b5224e6f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $4,300 ⟵ “Dr. Dana Lawrence | Communication, Collaboration, and Community: A Participatory Design Approach to Writing Center Administration | $4,300”
### `b8e747ba599bde67` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,437 ⟵ “Sarah Hunt Sellhorst | Visceral Adipose Tissue in College Students Manuscript | $5,437”
### `bdf7e6b0122c408e` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Claudia Y. Heinemann-Priest | Catawba Language Material Retrieval Project – the NAA Rudes/Siebert collection | $2,500”
### `bff5c779400e3b13` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $4,241 ⟵ “Dr. Nick Lawrence | Appealing to the Sensible: “Mr. Parkman’s Tour,” Gold Fever, and Melville’s Ambivalent Westward Approach | $4,241”
### `c3c5403bdbba8b9c` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $10,455 ⟵ “Fernanda Burke | Relationship of Fatty Acid Structure and Soap Properties: Inquiry Based Lab Experiment for Undergraduate Chemistry. | $10,455”
### `c3dc70c150d8f937` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,576.00 ⟵ “Chris Bundrick | Cold Mountain Field Guide Essay | $5,576.00”
### `c746149b686092c8` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $10,708 ⟵ “Courtney Catledge | Evaluation of a one dose Hepatitis B booster in meeting immunity requirements for BSN students | $10,708”
### `c7d93c0013d10cdc` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “Dr. Danny Faulkner | Visits to Lowell Observatory and AAS meeting | $5,000”
### `c7eb129fefa99d79` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $800.00 ⟵ “Todd Scarlett | Foraging movements of Great Blue Herons (Ardea herodias) determined by satellite tracking | $800.00”
### `c9c83abe23738802` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $9,127 ⟵ “Chris Judge | Research and Writing a Chapter for the Oxford Handbook of Mississippian Archaeology. | $9,127”
### `cbdcdf5c2f60bb76` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,847.00 ⟵ “Shemsi Alhaddad | Temari Projections on Assorted Surfaces | $7,847.00”
### `cc2d70f80bb1ecd0` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $10,437.30 ⟵ “Bettie Obi- Johnson and Annette Golonka | Identification of Unknown Compounds in the Floral Scent of Gelsemium sempervirens | $10,437.30”
### `cc43754f42e79e70` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,037 ⟵ “Dr. Mike Bonner | Indexing Fees | $2,037”
### `cc91c925ec5a98ed` University of South Carolina-Lancaster — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/apply/scholarships/index.php (sha256 67ca4488046a)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - eligibility_summary: Freshmen with a 4.00+ High School GPA on the SC Uniform Grading Scale ⟵ “Nov. 1st | Lancer Scholarships | Freshmen with a 4.00+ High School GPA on the SC Uniform Grading Scale”
### `d63ea27720c2d03d` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,539.00 ⟵ “Peter Seipel | “What Do We Owe the Global Poor?” | $7,539.00”
### `db60cb4d62e7980f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,061 ⟵ “Ann Scott | Implementing Appreciative Advising within a Rural BSN Collaborative Program | $2,061”
### `dc6bd1f4bfbf3389` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $12,000 ⟵ “Dr. Noni Bohonak | Development of Online CSCE101 | $12,000”
### `dcfff72d9123ffbe` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $9,223 ⟵ “Patrick Lawrence | "A Peculiar Moral Fitness": Moralist Nationalism, the ACS, and Native American Removal | $9,223”
### `dd481a4ac8eb0e45` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,770 ⟵ “Brittany Taylor - Driggers | Adaptable Art Studio Spaces at Universities in SC | $3,770”
### `de05eae6581dd1df` University of South Carolina-Lancaster — awards 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/apply/scholarships/index.php (sha256 67ca4488046a)
- issues: shared_site_attribution_review
- checks: {"thresholds": null}
  - eligibility_summary: Upper Classmen with a 3.00+ USC GPA on the SC Uniform Grading Scale. Continuing Scholarships are for one year only. ⟵ “Mar. 15th | Continuing & Transfer Student Scholarships | Upper Classmen with a 3.00+ USC GPA on the SC Uniform Grading Scale. Continuing Scholarships are for one year only.”
### `deee79c7f0e71aaa` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $800.00 ⟵ “Dana Lawrence | Subversive Intertextuality in Helen Oyeyemi's The Icarus Girl: Critiquing and Reimagining Western and Nigerian Metanarratives | $800.00”
### `dfbdfe8caabced2f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $8,045.00 ⟵ “Pat Lawrence | Antisemitism and the New Immigrants: Rationalist Racism Takes Its Place alongside Moralist Nationalism | $8,045.00”
### `e2a95be2ee8e3f83` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,500.00 ⟵ “David Roberts | The Cynical Therapeutic: Self-Concern Gone Awry | $2,500.00”
### `e68c0cc9ca1aa8c5` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,800 ⟵ “Dr. Lisa Hammond | Contemporary American Motherhood Memoirs article | $3,800”
### `ea59ade383a12d7c` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $7,079.36 ⟵ “Howard Kingkade | Short Film Project | $7,079.36”
### `eb579f5d8024d278` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “Terri Polenski | Equipment and seed monies for future research project | $1,500”
### `eb81c932ab4768a4` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $6,125 ⟵ “Li Cai | Immuno - Targeting of Cancer Cells with Human Natural Antibodies | $6,125”
### `ecaee98a25153c5a` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $9,640 ⟵ “Dr. Elizabeth Easley | The influence of physical activity and exercise motivation, benefits, and barriers on body composition in college students at a rural, Southern university | $9,640”
### `ed676567dde5f402` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $3,562.00 ⟵ “Nahid Swails | Development of a Hot-Water-Driven Nitinol Heat Engine for a Model Car | $3,562.00”
### `efd52a3d03aab4a9` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,169 ⟵ “Dr. Stephen Criswell | South Carolina Folklife Essay Collection | $5,169”
### `f4905385380f4199` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $5,432.00 ⟵ “Steven J. Campbell | Predicting Leaders’ Decisions during International Crises: The Utility of Poliheuristic Theory | $5,432.00”
### `f734c2f4303d0d92` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $15,908 ⟵ “Elizabeth Easley and Sarah Sellhorst | Incorporating a Research-Based Curriculum into the Biology 243 and 244 Laboratory Sequence | $15,908”
### `f8f19da78b6499d7` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $2,242 ⟵ “Dr. Annette Golonka and Dr. Bettie Obi- Johnson | Gelsemium sempervirens: Scent Profile and Nectar Inhabiting Microorganisms | $2,242”
### `f966b2df92736ff7` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $1,211.00 ⟵ “Jason Holt | On the Number of Eigenvalues of the Bilayer Graphene Operator in a Bounded Interval | $1,211.00”
### `faa2191c45e5b27d` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $4,200.00 ⟵ “Kaetrena Davis Kendrick | Continuing Studies on Low Morale in the North American Workplace | $4,200.00”
### `ff074f48f0cfbf13` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $4,537 ⟵ “Dr. Steven Campbell | Games Advisers Play: Political Manipulation of Foreign Policy in the Carter Administration | $4,537”
### `ffba7a3f02e0923f` University of South Carolina-Lancaster — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/internal/faculty_and_staff/faculty_rps_program/rps_past_awards/index.php (sha256 953bc2fec652)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"thresholds": null}
  - award_amount_text: $ 5,500.00 ⟵ “Sahar Aghasafari | Special Issue on Art and Technology in STEM Education | $ 5,500.00”
### `911cb12c9f8121cd` University of South Carolina-Lancaster — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php (sha256 f5e51f74cc23)
- issues: residency_unknown, shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 12288 ⟵ “Tuition | $12,288”
  - column:Technology Fee: 400 ⟵ “Technology Fee | $400”
  - column:Weighted Average Program Fee: 1580 ⟵ “Weighted Average Program Fee | $1,580”
  - column:Housing: 11432 ⟵ “Housing | $11,432”
  - column:Food: 5902 ⟵ “Food | $5,902”
  - column:Total: 31602 ⟵ “Total | $31,602”
### `62519e1242a725f8` University of South Carolina-Lancaster — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 37, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | AFAM 201 |  | ”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “American Government and Politics | 3 | POLI 201 |  | ”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research Course | 3 | UNEL 002T |  | ”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar Course | 3 | UELC 002T |  | ”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTE 101 | 4 | ARTH 105”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art Studio, 2-D | 3 | ARTS 103 |  | ”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art Studio, 3-D | 3 | ARTS 104 |  | ”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio, Drawing | 3 | ARTS 111 |  | ”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101 and 101L | 4, 5 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 111 and 111L | 4, 5 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | 3 | CHIN 121 | 4, 5 | CHIN 121 and 122”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics* | 3 | POLI 103C |  | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSCE 101 |  | ”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics-Macro | 3 | ECON 222 |  | ”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics-Micro | 3 | ECON 221 |  | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on either)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on either) | ENGL 101 | 5 (on either or both) | ENGL 101 and 102”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on both)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVR 101 & ENVR 101L |  | ”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 101 | 4, 5 | HIST 101 and 102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on either)]:  ⟵ “French Language OR French Literature** | 3 (on either) | FREN 121 | 4, 5 (on either or both) | FREN 121 and 122”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on both)]:  ⟵ “French Language OR French Literature** | 3 (on both) | FREN 121 AND 122 |  | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German** | 3 | GERM 121 | 4, 5 | GERM 121 and 122”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 210 |  | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | 3 | ITAL 121 | 4, 5 | ITAL 121 and 122”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese | 3 | JAPA 121 | 4, 5 | JAPA 121 and 122”
  - … 16 more rows
### `a46bd298a997eb1b` University of South Carolina-Lancaster — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 23, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | E, D, C B, A | BIOL 101, 101L BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | E, D, C, B, A | CSE 101 and CSCE 001T”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | E, D, C B, A | CHEM 111 and 111L CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | E, D C, B, A | ECON 221 ECON 221 and 222”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | E, D, C, B, A | GEOG 103”
  - equivalencies[IB-HISTORY|History: U.S.]:  ⟵ “History: U.S. | E, D, C, B, A | HIST 112”
  - equivalencies[IB-HISTORY|History: European]:  ⟵ “History: European | E, D, C, B, A | HIST 102”
  - equivalencies[IB-HISTORY|History: International]:  ⟵ “History: International | E, D, C, B, A | HIST 001T”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | E, D, C B, A | PHYS 211 and 211L PHYS 211, 211L, 212 and 212L”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | E, D, C, B, A | PSYC 101”
  - equivalencies[IB-HISTORY|History: U.S./International/European]:  ⟵ “History: U.S./International/European | E, D, C, B, A | HUMA 001T”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 101 and 101L | 5, 6, 7 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business and Management | 4 | MGMT 371 | 5, 6, 7 | MGMT 371 and 376”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 111 and 111L | 5, 6, 7 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|4, 5]:  ⟵ “Economics | 4, 5 | ECON 221 | 6, 7 | ECON 221 and 222”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on either)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on either) | ENGL 101 | 5, 6, 7 (on either or both) | ENGL 101 and 102”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on both)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[IB-FILM|4]:  ⟵ “Film | 4 | HUMA 002T |  | ”
  - equivalencies[IB-FRENCH|4, 5]:  ⟵ “French B* | 4, 5 | FREN 122 and 209 | 6, 7 | FREN 209 and 210”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOG 103 |  | ”
  - equivalencies[IB-GERMAN|4, 5]:  ⟵ “German B* | 4, 5 | GERM 122 and 210 | 6, 7 | GERM 210 and 211”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | POLI 101 |  | ”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of the Americas | 4 | HIST 102 and 112 |  | ”
  - equivalencies[IB-LATIN|4]:  ⟵ “Latin B* | 4 | LATN 121 and 122 | 5, 6 | LATN 122 and 301”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4]:  ⟵ “Mathematics Analysis and Approaches | 4 | MATH 141 | 5, 6, 7 | MATH 141 and 142”
  - … 9 more rows
### `bf2b5f5e897ee194` University of South Carolina-Lancaster — credit_policies 2026-27 · policy_kind=CLEP [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/offices_and_divisions/registrar/transfer_credits/clep_credits.php (sha256 0f05376be5f7)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"distinct_exams": 21, "equivalencies": 21, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50 (Effective until 2/28/2021) 72 (Effective beginning 3/1/2021)]:  ⟵ “Financial Accounting | 50 (Effective until 2/28/2021) 72 (Effective beginning 3/1/2021) | ACCT 225 | business”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|57 (Effective until 2/28/2021) 72 (Effective beginning 3/1/2021)]:  ⟵ “Introductory Business Law | 57 (Effective until 2/28/2021) 72 (Effective beginning 3/1/2021) | ACCT 324 | business”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|65]:  ⟵ “American Government | 65 | POLI 201 | political”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|54]:  ⟵ “History of the United States I | 54 | HIST 111 | history”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|55]:  ⟵ “History of the United States II | 55 | HIST 112 | history”
  - equivalencies[CLEP-BIOLOGY|5763]:  ⟵ “Biology | 5763 | BIOL 101 & BIOL 101LBIOL 101, 101L, 102, 102L | science”
  - equivalencies[CLEP-CALCULUS|60]:  ⟵ “Calculus | 60 | MATH 141 | math”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry | 63 | CHEM 111 | science”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|60]:  ⟵ “Information Systems | 60 | CSCE 101 | computer”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|57]:  ⟵ “Western Civilization I | 57 | HIST 101 | history”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|56]:  ⟵ “Western Civilization II | 56 | HIST 102 | history”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|54]:  ⟵ “Principles of Macroeconomics | 54 | ECON 222 | business”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|54]:  ⟵ “Principles of Microeconomics | 54 | ECON 221 | business”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | EDPY 335 | education, psychology”
  - equivalencies[CLEP-AMERICAN-LITERATURE|55]:  ⟵ “American Literature | 55 | ENGL 285 | english”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|56 (Effective until 2/28/2021) 72 (Effective beginning 3/1/2021)]:  ⟵ “Principles of Management | 56 (Effective until 2/28/2021) 72 (Effective beginning 3/1/2021) | MGMT 371 | business”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|55 (Effective until 2/28/2021) 72 (Effective beginning 3/1/2021)]:  ⟵ “Principles of Marketing | 55 (Effective until 2/28/2021) 72 (Effective beginning 3/1/2021) | MKTG 350 | business”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|60]:  ⟵ “College Algebra | 60 | MATH 111 | math”
  - equivalencies[CLEP-PRECALCULUS|60]:  ⟵ “Precalculus | 60 | MATH 115 | math”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|54]:  ⟵ “Introductory Psychology | 54 | PSYC 101 | psychology”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|5570]:  ⟵ “College Composition | 5570 | ENGL 101 ENGL 101 & 102 | english”
### `m2df872d70c75743` University of South Carolina-Lancaster — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://www.sc.edu/about/system_and_campuses/lancaster/study/dual_enrollment/index.php (sha256 fb9f6830fef2)
- issues: ambiguous_year_labels, shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “level coursework (dual enrollment students should have a cumulative high school GPA of 3.0 or”
  - per_credit_hour_charge: 75 ⟵ “Answer: It is currently $75.00 per credit hour. This is subject to change.”
  - eligibility_tier: 3.0 ⟵ “Answer: Students must have a 3.0 grade point average, complete a dual enrollment packet,”
  - eligibility_tier: 3.0 ⟵ “• You must have a 3.0 High School GPA to be admitted to Dual Enrollment”
### `e0314c0303cebf12` University of South Carolina-Lancaster — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_transfers/index.php (sha256 28dce6fabe62)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transferring credits from other institutions USC generally accepts nonremedial coursework completed at regionally accredited institutions with a grade of C- or better.”
### `190ff41fa65a2a39` University of South Carolina-Salkehatchie — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php (sha256 76a73e8915fb)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You are welcome to complete our scholarship appeal form, and we will consider your request should additional funds become available.”
### `76b1f5f6235175c2` University of South Carolina-Salkehatchie — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Appeals will only be accepted electronically through the Scholarship Appeal Form that is accessible through Self Service Carolina.”
### `7fc40a9de64d745a` University of South Carolina-Salkehatchie — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please note that this is separate from any Satisfactory Academic Progress appeal that a student might have to complete for federal financial aid.”
### `3998a3dec8cffaff` University of South Carolina-Salkehatchie — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/bursar/tuition_and_required_fees/department_fees/index.php (sha256 1b721268a120)
- issues: arrangement_unlabeled, residency_unknown, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php,https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php
- checks: {"columns": 2, "rows": 31}
  - column:Tuition - Per EPI Term - Full Time: 2560.0 ⟵ “Tuition - Per EPI Term - Full Time | 2,560.00 | ”
  - column:Tuition - Two Classes: 1700.0 ⟵ “Tuition - Two Classes | 1,700.00 | ”
  - column:Tuition - One Class: 850.0 ⟵ “Tuition - One Class | 850.00 | ”
  - column:J1/Sponsored Int’l Student Fee for Add’l Support Svcs: 125.0 ⟵ “J1/Sponsored Int’l Student Fee for Add’l Support Svcs | 125.00 | 108”
  - column:Pre-Sessional Administrative Processing (Per 8 Week Session): 100.0 ⟵ “Pre-Sessional Administrative Processing (Per 8 Week Session) | 100.00 | ”
  - column:Non-profit Higher Education Institution Partner – Full Time Rate Per EPI Term: 1800.0 ⟵ “Non-profit Higher Education Institution Partner – Full Time Rate Per EPI Term | 1800.00 | ”
  - column:Former SC High School Grad or ATT Cert Recipient – Full-time Tuition Per EPI Term (SC Perm. Residents Who Completed HS in SC but Require ESL Study): 1800.0 ⟵ “Former SC High School Grad or ATT Cert Recipient – Full-time Tuition Per EPI Term (SC Perm. Residents Who Completed HS in SC but Require ESL Study) | 1800.00 | ”
  - column:Minimum Pre Registration Tuition Payment: 500.0 ⟵ “Minimum Pre Registration Tuition Payment | 500.00 | ”
  - column:Late Registration Fee: 100.0 ⟵ “Late Registration Fee | 100.00 | ”
  - column:Late Testing Fee - 1 Test: 45.0 ⟵ “Late Testing Fee - 1 Test | 45.00 | ”
  - column:Late Testing Fee - 2 Tests: 75.0 ⟵ “Late Testing Fee - 2 Tests | 75.00 | ”
  - column:Refund - Processing Fee: 25.0 ⟵ “Refund - Processing Fee | 25.00 | ”
  - column:Major Medical Insurance: 800.0 ⟵ “Major Medical Insurance | 800.00 | 19”
  - column:Gap - Insurance: 410.0 ⟵ “Gap - Insurance | 410.00 | 19”
  - column:Gap - Health Center: 127.0 ⟵ “Gap - Health Center | 127.00 | ”
  - column:Readmit - Other Testing/Technology: 125.0 ⟵ “Readmit - Other Testing/Technology | 125.00 | ”
  - column:Readmit – Campus Fee Per EPI Term for Non-registered Students: 413.0 ⟵ “Readmit – Campus Fee Per EPI Term for Non-registered Students | 413.00 | ”
  - column:Gap Tuition Prepayment: 500.0 ⟵ “Gap Tuition Prepayment | 500.00 | ”
  - column:DMV Translation - Non EPI: 35.0 ⟵ “DMV Translation - Non EPI | 35.00 | ”
  - column:Extra Express Mailing Fee International: 50.0 ⟵ “Extra Express Mailing Fee International | 50.00 | ”
  - column:Extra Express Mailing Fee Domestic: 20.0 ⟵ “Extra Express Mailing Fee Domestic | 20.00 | ”
  - column:Immigration Assistance/Administration: 200.0 ⟵ “Immigration Assistance/Administration | 200.00 | ”
  - column:Testing - EPI Test Battery: 75.0 ⟵ “Testing - EPI Test Battery | 75.00 | ”
  - column:Testing - TOEFL: 60.0 ⟵ “Testing - TOEFL | 60.00 | ”
  - column:Classes - GRE Test Prep Class Via USC: 710.0 ⟵ “Classes - GRE Test Prep Class Via USC | 710.00 | ”
  - … 10 more rows
### `ca8cb686f49d2210` University of South Carolina-Salkehatchie — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php (sha256 f5e51f74cc23)
- issues: residency_unknown, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/bursar/tuition_and_required_fees/department_fees/index.php,https://www.sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 12288 ⟵ “Tuition | $12,288”
  - column:Technology Fee: 400 ⟵ “Technology Fee | $400”
  - column:Weighted Average Program Fee: 1580 ⟵ “Weighted Average Program Fee | $1,580”
  - column:Housing: 11432 ⟵ “Housing | $11,432”
  - column:Food: 5902 ⟵ “Food | $5,902”
  - column:Total: 31602 ⟵ “Total | $31,602”
### `dfd8ec53ab8f8c32` University of South Carolina-Salkehatchie — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php (sha256 f3a89e979fc3)
- issues: residency_unknown, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/bursar/tuition_and_required_fees/department_fees/index.php,https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - on_campus:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - on_campus:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - on_campus:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - on_campus:Housing: 11432 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - on_campus:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - on_campus:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - on_campus:Transportation: 2670 ⟵ “Transportation | $2,670 | $2,690 | $2,690”
  - on_campus:Total: 66394 ⟵ “Total | $66,394 | $66,394 | $57,592”
  - off_campus_not_with_family:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - off_campus_not_with_family:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - off_campus_not_with_family:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - off_campus_not_with_family:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - off_campus_not_with_family:Housing: 11432 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - off_campus_not_with_family:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - off_campus_not_with_family:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - off_campus_not_with_family:Transportation: 2690 ⟵ “Transportation | $2,670 | $2,690 | $2,690”
  - off_campus_not_with_family:Total: 66394 ⟵ “Total | $66,394 | $66,394 | $57,592”
  - with_parents_or_family:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - with_parents_or_family:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - with_parents_or_family:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - with_parents_or_family:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - with_parents_or_family:Housing: 2630 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - with_parents_or_family:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - with_parents_or_family:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - … 2 more rows
### `02803b1da58f5385` University of South Carolina-Salkehatchie — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 37, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | AFAM 201 |  | ”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “American Government and Politics | 3 | POLI 201 |  | ”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research Course | 3 | UNEL 002T |  | ”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar Course | 3 | UELC 002T |  | ”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTE 101 | 4 | ARTH 105”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art Studio, 2-D | 3 | ARTS 103 |  | ”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art Studio, 3-D | 3 | ARTS 104 |  | ”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio, Drawing | 3 | ARTS 111 |  | ”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101 and 101L | 4, 5 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 111 and 111L | 4, 5 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | 3 | CHIN 121 | 4, 5 | CHIN 121 and 122”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics* | 3 | POLI 103C |  | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSCE 101 |  | ”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics-Macro | 3 | ECON 222 |  | ”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics-Micro | 3 | ECON 221 |  | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on either)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on either) | ENGL 101 | 5 (on either or both) | ENGL 101 and 102”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on both)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVR 101 & ENVR 101L |  | ”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 101 | 4, 5 | HIST 101 and 102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on either)]:  ⟵ “French Language OR French Literature** | 3 (on either) | FREN 121 | 4, 5 (on either or both) | FREN 121 and 122”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on both)]:  ⟵ “French Language OR French Literature** | 3 (on both) | FREN 121 AND 122 |  | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German** | 3 | GERM 121 | 4, 5 | GERM 121 and 122”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 210 |  | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | 3 | ITAL 121 | 4, 5 | ITAL 121 and 122”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese | 3 | JAPA 121 | 4, 5 | JAPA 121 and 122”
  - … 16 more rows
### `0eb03fa6aa4e0486` University of South Carolina-Salkehatchie — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 23, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | E, D, C B, A | BIOL 101, 101L BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | E, D, C, B, A | CSE 101 and CSCE 001T”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | E, D, C B, A | CHEM 111 and 111L CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | E, D C, B, A | ECON 221 ECON 221 and 222”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | E, D, C, B, A | GEOG 103”
  - equivalencies[IB-HISTORY|History: U.S.]:  ⟵ “History: U.S. | E, D, C, B, A | HIST 112”
  - equivalencies[IB-HISTORY|History: European]:  ⟵ “History: European | E, D, C, B, A | HIST 102”
  - equivalencies[IB-HISTORY|History: International]:  ⟵ “History: International | E, D, C, B, A | HIST 001T”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | E, D, C B, A | PHYS 211 and 211L PHYS 211, 211L, 212 and 212L”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | E, D, C, B, A | PSYC 101”
  - equivalencies[IB-HISTORY|History: U.S./International/European]:  ⟵ “History: U.S./International/European | E, D, C, B, A | HUMA 001T”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 101 and 101L | 5, 6, 7 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business and Management | 4 | MGMT 371 | 5, 6, 7 | MGMT 371 and 376”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 111 and 111L | 5, 6, 7 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|4, 5]:  ⟵ “Economics | 4, 5 | ECON 221 | 6, 7 | ECON 221 and 222”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on either)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on either) | ENGL 101 | 5, 6, 7 (on either or both) | ENGL 101 and 102”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on both)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[IB-FILM|4]:  ⟵ “Film | 4 | HUMA 002T |  | ”
  - equivalencies[IB-FRENCH|4, 5]:  ⟵ “French B* | 4, 5 | FREN 122 and 209 | 6, 7 | FREN 209 and 210”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOG 103 |  | ”
  - equivalencies[IB-GERMAN|4, 5]:  ⟵ “German B* | 4, 5 | GERM 122 and 210 | 6, 7 | GERM 210 and 211”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | POLI 101 |  | ”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of the Americas | 4 | HIST 102 and 112 |  | ”
  - equivalencies[IB-LATIN|4]:  ⟵ “Latin B* | 4 | LATN 121 and 122 | 5, 6 | LATN 122 and 301”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4]:  ⟵ “Mathematics Analysis and Approaches | 4 | MATH 141 | 5, 6, 7 | MATH 141 and 142”
  - … 9 more rows
### `m287eb078e935777` University of South Carolina-Salkehatchie — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://sc.edu/about/system_and_campuses/salkehatchie/study/dual_enrollment/parents-de.php (sha256 145d584dffdd)
- issues: shared_site_attribution_review
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “High school concurrent applicants must have a High School GPA of 3.0 or higher (4.0”
  - eligibility_tier: 3.0 ⟵ “High school unweighted 3.0 grade point average on a 4.0 scale.”
  - college_gpa_to_continue: 2.0 ⟵ “Maintain a 2.0 college grade point average on a 4.0 scale.”
### `f9b548db66cbeef4` University of South Carolina-Salkehatchie — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_transfers/index.php (sha256 28dce6fabe62)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transferring credits from other institutions USC generally accepts nonremedial coursework completed at regionally accredited institutions with a grade of C- or better.”
### `0babf433afbf8305` University of South Carolina-Sumter — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/system_and_campuses/palmetto_college/internal/documents/remdocs/financial_aid/fasap_appeal_and_academic_plan_updated_may_2026.pdf,https://sc.edu/about/system_and_campuses/sumter/apply/financial_aid/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please note that this is separate from any Satisfactory Academic Progress appeal that a student might have to complete for federal financial aid.”
### `11470cf06b44feaf` University of South Carolina-Sumter — appeals 2026-27 [new] (source_unlabeled)
- source: https://sc.edu/about/system_and_campuses/palmetto_college/internal/documents/remdocs/financial_aid/fasap_appeal_and_academic_plan_updated_may_2026.pdf (sha256 83efa75ff5df)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/system_and_campuses/sumter/apply/financial_aid/index.php,https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal and Academic Plan Academic Year: _______________________ Appeal Term: ______________________ Student’s Name: ___________________________________________________________ USC ID: _______________ Email Address: ______________________________________________________________________________________ Use this form to complete your financial aid satisfactory academic ”
  - sentence: sap_appeal ⟵ “PCCFAO | Satisfactory Academic Progress Appeal and Academic Plan | May 2026 Reason for Appeal (check all that apply) Student’s Illness or Medical Issue.”
  - sentence: sap_appeal ⟵ “Academic Advisor’s Signature: __________________________________________________ Date: ______________ Print name and title/position: ________________________________________________________________________ PCCFAO | Satisfactory Academic Progress Appeal and Academic Plan | May 2026”
### `12a05e78690c7002` University of South Carolina-Sumter — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php (sha256 76a73e8915fb)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You are welcome to complete our scholarship appeal form, and we will consider your request should additional funds become available.”
### `1f6bcc1843136f61` University of South Carolina-Sumter — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Appeals will only be accepted electronically through the Scholarship Appeal Form that is accessible through Self Service Carolina.”
### `589fb4698bd84684` University of South Carolina-Sumter — appeals 2026-27 [new] (source_unlabeled)
- source: https://sc.edu/about/system_and_campuses/sumter/apply/financial_aid/index.php (sha256 7c74aed6bea0)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/system_and_campuses/palmetto_college/internal/documents/remdocs/financial_aid/fasap_appeal_and_academic_plan_updated_may_2026.pdf,https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeals All students deemed ineligible to receive financial aid as a result of failing to meet any component of this policy have the right to appeal.”
### `b58920c752881809` University of South Carolina-Sumter — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php (sha256 f5e51f74cc23)
- issues: residency_unknown, shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 12288 ⟵ “Tuition | $12,288”
  - column:Technology Fee: 400 ⟵ “Technology Fee | $400”
  - column:Weighted Average Program Fee: 1580 ⟵ “Weighted Average Program Fee | $1,580”
  - column:Housing: 11432 ⟵ “Housing | $11,432”
  - column:Food: 5902 ⟵ “Food | $5,902”
  - column:Total: 31602 ⟵ “Total | $31,602”
### `324d8f0253d0c79a` University of South Carolina-Sumter — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://sc.edu/about/system_and_campuses/sumter/study/dual_enrollment/apply_de_ec.php (sha256 383a3a653af3)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “High school concurrent applicants must have a High School GPA of 3.0 or higher (4.0”
### `4e395c12c4771153` University of South Carolina-Sumter — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 37, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | AFAM 201 |  | ”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “American Government and Politics | 3 | POLI 201 |  | ”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research Course | 3 | UNEL 002T |  | ”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar Course | 3 | UELC 002T |  | ”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTE 101 | 4 | ARTH 105”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art Studio, 2-D | 3 | ARTS 103 |  | ”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art Studio, 3-D | 3 | ARTS 104 |  | ”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio, Drawing | 3 | ARTS 111 |  | ”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101 and 101L | 4, 5 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 111 and 111L | 4, 5 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | 3 | CHIN 121 | 4, 5 | CHIN 121 and 122”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics* | 3 | POLI 103C |  | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSCE 101 |  | ”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics-Macro | 3 | ECON 222 |  | ”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics-Micro | 3 | ECON 221 |  | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on either)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on either) | ENGL 101 | 5 (on either or both) | ENGL 101 and 102”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on both)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVR 101 & ENVR 101L |  | ”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 101 | 4, 5 | HIST 101 and 102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on either)]:  ⟵ “French Language OR French Literature** | 3 (on either) | FREN 121 | 4, 5 (on either or both) | FREN 121 and 122”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on both)]:  ⟵ “French Language OR French Literature** | 3 (on both) | FREN 121 AND 122 |  | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German** | 3 | GERM 121 | 4, 5 | GERM 121 and 122”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 210 |  | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | 3 | ITAL 121 | 4, 5 | ITAL 121 and 122”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese | 3 | JAPA 121 | 4, 5 | JAPA 121 and 122”
  - … 16 more rows
### `f19e4ee2687a6f14` University of South Carolina-Sumter — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 23, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | E, D, C B, A | BIOL 101, 101L BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | E, D, C, B, A | CSE 101 and CSCE 001T”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | E, D, C B, A | CHEM 111 and 111L CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | E, D C, B, A | ECON 221 ECON 221 and 222”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | E, D, C, B, A | GEOG 103”
  - equivalencies[IB-HISTORY|History: U.S.]:  ⟵ “History: U.S. | E, D, C, B, A | HIST 112”
  - equivalencies[IB-HISTORY|History: European]:  ⟵ “History: European | E, D, C, B, A | HIST 102”
  - equivalencies[IB-HISTORY|History: International]:  ⟵ “History: International | E, D, C, B, A | HIST 001T”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | E, D, C B, A | PHYS 211 and 211L PHYS 211, 211L, 212 and 212L”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | E, D, C, B, A | PSYC 101”
  - equivalencies[IB-HISTORY|History: U.S./International/European]:  ⟵ “History: U.S./International/European | E, D, C, B, A | HUMA 001T”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 101 and 101L | 5, 6, 7 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business and Management | 4 | MGMT 371 | 5, 6, 7 | MGMT 371 and 376”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 111 and 111L | 5, 6, 7 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|4, 5]:  ⟵ “Economics | 4, 5 | ECON 221 | 6, 7 | ECON 221 and 222”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on either)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on either) | ENGL 101 | 5, 6, 7 (on either or both) | ENGL 101 and 102”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on both)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[IB-FILM|4]:  ⟵ “Film | 4 | HUMA 002T |  | ”
  - equivalencies[IB-FRENCH|4, 5]:  ⟵ “French B* | 4, 5 | FREN 122 and 209 | 6, 7 | FREN 209 and 210”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOG 103 |  | ”
  - equivalencies[IB-GERMAN|4, 5]:  ⟵ “German B* | 4, 5 | GERM 122 and 210 | 6, 7 | GERM 210 and 211”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | POLI 101 |  | ”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of the Americas | 4 | HIST 102 and 112 |  | ”
  - equivalencies[IB-LATIN|4]:  ⟵ “Latin B* | 4 | LATN 121 and 122 | 5, 6 | LATN 122 and 301”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4]:  ⟵ “Mathematics Analysis and Approaches | 4 | MATH 141 | 5, 6, 7 | MATH 141 and 142”
  - … 9 more rows
### `ed7536185c1b5c40` University of South Carolina-Sumter — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_transfers/index.php (sha256 28dce6fabe62)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transferring credits from other institutions USC generally accepts nonremedial coursework completed at regionally accredited institutions with a grade of C- or better.”
### `1a2535199a4ef7d7` University of South Carolina-Union — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Appeals will only be accepted electronically through the Scholarship Appeal Form that is accessible through Self Service Carolina.”
### `48182f1301ec2b64` University of South Carolina-Union — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please note that this is separate from any Satisfactory Academic Progress appeal that a student might have to complete for federal financial aid.”
### `98a0245188919f2a` University of South Carolina-Union — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php (sha256 76a73e8915fb)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You are welcome to complete our scholarship appeal form, and we will consider your request should additional funds become available.”
### `0fdec7529b8a4603` University of South Carolina-Union — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php (sha256 f5e51f74cc23)
- issues: residency_unknown, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/bursar/tuition_and_required_fees/department_fees/index.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 12288 ⟵ “Tuition | $12,288”
  - column:Technology Fee: 400 ⟵ “Technology Fee | $400”
  - column:Weighted Average Program Fee: 1580 ⟵ “Weighted Average Program Fee | $1,580”
  - column:Housing: 11432 ⟵ “Housing | $11,432”
  - column:Food: 5902 ⟵ “Food | $5,902”
  - column:Total: 31602 ⟵ “Total | $31,602”
### `ee8899d3d0e37af3` University of South Carolina-Union — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/bursar/tuition_and_required_fees/department_fees/index.php (sha256 1b721268a120)
- issues: arrangement_unlabeled, residency_unknown, shared_site_attribution_review, conflicting_sources:https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php
- checks: {"columns": 2, "rows": 31}
  - column:Tuition - Per EPI Term - Full Time: 2560.0 ⟵ “Tuition - Per EPI Term - Full Time | 2,560.00 | ”
  - column:Tuition - Two Classes: 1700.0 ⟵ “Tuition - Two Classes | 1,700.00 | ”
  - column:Tuition - One Class: 850.0 ⟵ “Tuition - One Class | 850.00 | ”
  - column:J1/Sponsored Int’l Student Fee for Add’l Support Svcs: 125.0 ⟵ “J1/Sponsored Int’l Student Fee for Add’l Support Svcs | 125.00 | 108”
  - column:Pre-Sessional Administrative Processing (Per 8 Week Session): 100.0 ⟵ “Pre-Sessional Administrative Processing (Per 8 Week Session) | 100.00 | ”
  - column:Non-profit Higher Education Institution Partner – Full Time Rate Per EPI Term: 1800.0 ⟵ “Non-profit Higher Education Institution Partner – Full Time Rate Per EPI Term | 1800.00 | ”
  - column:Former SC High School Grad or ATT Cert Recipient – Full-time Tuition Per EPI Term (SC Perm. Residents Who Completed HS in SC but Require ESL Study): 1800.0 ⟵ “Former SC High School Grad or ATT Cert Recipient – Full-time Tuition Per EPI Term (SC Perm. Residents Who Completed HS in SC but Require ESL Study) | 1800.00 | ”
  - column:Minimum Pre Registration Tuition Payment: 500.0 ⟵ “Minimum Pre Registration Tuition Payment | 500.00 | ”
  - column:Late Registration Fee: 100.0 ⟵ “Late Registration Fee | 100.00 | ”
  - column:Late Testing Fee - 1 Test: 45.0 ⟵ “Late Testing Fee - 1 Test | 45.00 | ”
  - column:Late Testing Fee - 2 Tests: 75.0 ⟵ “Late Testing Fee - 2 Tests | 75.00 | ”
  - column:Refund - Processing Fee: 25.0 ⟵ “Refund - Processing Fee | 25.00 | ”
  - column:Major Medical Insurance: 800.0 ⟵ “Major Medical Insurance | 800.00 | 19”
  - column:Gap - Insurance: 410.0 ⟵ “Gap - Insurance | 410.00 | 19”
  - column:Gap - Health Center: 127.0 ⟵ “Gap - Health Center | 127.00 | ”
  - column:Readmit - Other Testing/Technology: 125.0 ⟵ “Readmit - Other Testing/Technology | 125.00 | ”
  - column:Readmit – Campus Fee Per EPI Term for Non-registered Students: 413.0 ⟵ “Readmit – Campus Fee Per EPI Term for Non-registered Students | 413.00 | ”
  - column:Gap Tuition Prepayment: 500.0 ⟵ “Gap Tuition Prepayment | 500.00 | ”
  - column:DMV Translation - Non EPI: 35.0 ⟵ “DMV Translation - Non EPI | 35.00 | ”
  - column:Extra Express Mailing Fee International: 50.0 ⟵ “Extra Express Mailing Fee International | 50.00 | ”
  - column:Extra Express Mailing Fee Domestic: 20.0 ⟵ “Extra Express Mailing Fee Domestic | 20.00 | ”
  - column:Immigration Assistance/Administration: 200.0 ⟵ “Immigration Assistance/Administration | 200.00 | ”
  - column:Testing - EPI Test Battery: 75.0 ⟵ “Testing - EPI Test Battery | 75.00 | ”
  - column:Testing - TOEFL: 60.0 ⟵ “Testing - TOEFL | 60.00 | ”
  - column:Classes - GRE Test Prep Class Via USC: 710.0 ⟵ “Classes - GRE Test Prep Class Via USC | 710.00 | ”
  - … 10 more rows
### `2dd9cd404c37544a` University of South Carolina-Union — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 37, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | AFAM 201 |  | ”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “American Government and Politics | 3 | POLI 201 |  | ”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research Course | 3 | UNEL 002T |  | ”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar Course | 3 | UELC 002T |  | ”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTE 101 | 4 | ARTH 105”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art Studio, 2-D | 3 | ARTS 103 |  | ”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art Studio, 3-D | 3 | ARTS 104 |  | ”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio, Drawing | 3 | ARTS 111 |  | ”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101 and 101L | 4, 5 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 111 and 111L | 4, 5 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | 3 | CHIN 121 | 4, 5 | CHIN 121 and 122”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics* | 3 | POLI 103C |  | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSCE 101 |  | ”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics-Macro | 3 | ECON 222 |  | ”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics-Micro | 3 | ECON 221 |  | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on either)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on either) | ENGL 101 | 5 (on either or both) | ENGL 101 and 102”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on both)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVR 101 & ENVR 101L |  | ”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 101 | 4, 5 | HIST 101 and 102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on either)]:  ⟵ “French Language OR French Literature** | 3 (on either) | FREN 121 | 4, 5 (on either or both) | FREN 121 and 122”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on both)]:  ⟵ “French Language OR French Literature** | 3 (on both) | FREN 121 AND 122 |  | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German** | 3 | GERM 121 | 4, 5 | GERM 121 and 122”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 210 |  | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | 3 | ITAL 121 | 4, 5 | ITAL 121 and 122”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese | 3 | JAPA 121 | 4, 5 | JAPA 121 and 122”
  - … 16 more rows
### `964422a695a52a92` University of South Carolina-Union — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 0d4aaeefc652)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 23, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | E, D, C B, A | BIOL 101, 101L BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | E, D, C, B, A | CSE 101 and CSCE 001T”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | E, D, C B, A | CHEM 111 and 111L CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | E, D C, B, A | ECON 221 ECON 221 and 222”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | E, D, C, B, A | GEOG 103”
  - equivalencies[IB-HISTORY|History: U.S.]:  ⟵ “History: U.S. | E, D, C, B, A | HIST 112”
  - equivalencies[IB-HISTORY|History: European]:  ⟵ “History: European | E, D, C, B, A | HIST 102”
  - equivalencies[IB-HISTORY|History: International]:  ⟵ “History: International | E, D, C, B, A | HIST 001T”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | E, D, C B, A | PHYS 211 and 211L PHYS 211, 211L, 212 and 212L”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | E, D, C, B, A | PSYC 101”
  - equivalencies[IB-HISTORY|History: U.S./International/European]:  ⟵ “History: U.S./International/European | E, D, C, B, A | HUMA 001T”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 101 and 101L | 5, 6, 7 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business and Management | 4 | MGMT 371 | 5, 6, 7 | MGMT 371 and 376”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 111 and 111L | 5, 6, 7 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|4, 5]:  ⟵ “Economics | 4, 5 | ECON 221 | 6, 7 | ECON 221 and 222”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on either)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on either) | ENGL 101 | 5, 6, 7 (on either or both) | ENGL 101 and 102”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on both)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[IB-FILM|4]:  ⟵ “Film | 4 | HUMA 002T |  | ”
  - equivalencies[IB-FRENCH|4, 5]:  ⟵ “French B* | 4, 5 | FREN 122 and 209 | 6, 7 | FREN 209 and 210”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOG 103 |  | ”
  - equivalencies[IB-GERMAN|4, 5]:  ⟵ “German B* | 4, 5 | GERM 122 and 210 | 6, 7 | GERM 210 and 211”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | POLI 101 |  | ”
  - equivalencies[IB-HISTORY|4]:  ⟵ “History of the Americas | 4 | HIST 102 and 112 |  | ”
  - equivalencies[IB-LATIN|4]:  ⟵ “Latin B* | 4 | LATN 121 and 122 | 5, 6 | LATN 122 and 301”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4]:  ⟵ “Mathematics Analysis and Approaches | 4 | MATH 141 | 5, 6, 7 | MATH 141 and 142”
  - … 9 more rows
### `a7e422ac95f872db` University of South Carolina-Union — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://sc.edu/about/system_and_campuses/union/apply/dual_enrollment/ (sha256 29735ffd778b)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “High school concurrent applicants must have a High School GPA of 3.0 or higher (4.0”
### `29b1a31270e338ad` University of South Carolina-Union — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_transfers/index.php (sha256 28dce6fabe62)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transferring credits from other institutions USC generally accepts nonremedial coursework completed at regionally accredited institutions with a grade of C- or better.”
### `58ede43088ce2a68` University of South Carolina-Upstate — appeals 2026-27 [new] (source_unlabeled)
- source: https://uscupstate.edu/tuition-and-financial-aid/ (sha256 ead3af3b0dc0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “For Veterans Affairs benefits, contact Robin Hollis, the VA coordinator in the Records and Registration office, at [email protected]. *Check your school email account often.* How to accept a financial aid award+ Log in to Self Service Carolina at my.sc.edu Click the Financial Aid tab Click FINANCIAL AID then FINANCIAL AID FOR AID YEAR Click the Award Overview tab to review your award offers Click ”
### `5e311eb4f4c61c21` Voorhees University — appeals 2026-27 [new] (labeled_in_source)
- source: https://voorhees.edu/wp-content/uploads/2026/01/Professional-Judgment-Appeal-2026-2027.pdf (sha256 ae6125687b15)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Voorhees University Office of Financial Aid 2026-2027 Professional Judgment Appeal Student Name: Student ID# Parent(s) Name: Voorhees University recognizes that families experience special circumstances, which merit recalculation of their financial aid eligibility based on 2025 tax information or 2026/27 Projected Income, rather than 2024 income information.”
  - sentence: professional_judgment ⟵ “Please be advised that all professional judgment appeal decisions are final.”
### `c94b0f2a19d0c873` Voorhees University — appeals 2026-27 [new] (source_unlabeled)
- source: https://voorhees.edu/wp-content/uploads/2026/01/SATISFACTORY-ACADEMIC-PROGRESS-POLICY-SAP.pdf (sha256 2476250a8bdf)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “An injury or illness of the student, the death of a relative of the student; and, other special circumstances as determined by the school) they must request reconsideration in writing to the Chair of the Financial Aid/Academic Review Committee within 30 days of the date of the letter of Federal Student Aid Ineligibility.”
### `a778f20d33639532` Williamsburg Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.wiltech.edu/financial-aid-tuition/understanding-financial-aid/ (sha256 d09a9e4380aa)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Financial Aid Forms Unusual Enrollment History Flag 2 Form 2025-2026 Unusual Enrollment History Flag 3 Form 3 2025-2026 Dependent Verification Worksheet 2025-2026 Independent Verification Worksheet 2025-2026 Nontax Filer Parent 2025-2026 Dependency Override Request Nontax Filer Student 2025-2026 How to Apply for Financial Aid Eligibility for Financial Aid A student must have a high school graduati”
### `2bfcf3d0e3152782` Winthrop University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.winthrop.edu/uploadedFiles/finaid/sap-standards-effective-may-2024.pdf (sha256 576f16144122)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “A Satisfactory Academic Progress Appeal form is available from the “Forms Online” link at www.winthrop.edu/finaid.”
  - sentence: sap_appeal ⟵ “The type of aid that will be available if the SAP Appeal is approved will depend on the time of year and what is allowed under applicable regulations.”
  - sentence: sap_appeal ⟵ “Time Frame: SAP Appeals are typically reviewed within 2-4 weeks from the time an appeal is submitted and deemed complete.”
  - sentence: sap_appeal ⟵ “Students are responsible for adhering to all fee payment deadlines, even if they have a SAP appeal under review.”
  - sentence: sap_appeal ⟵ “Notification: Student will receive email notification of status of SAP Appeal each time status changes (incomplete, approved or denied).”
  - sentence: sap_appeal ⟵ “Failure to meet the conditions by the end of the probationary term will result in a termination of eligibility for student aid that requires SAP until the student has regained eligibility by meeting the requirements discussed in the Regaining Satisfactory Academic Progress section below. 3 Satisfactory Academic Progress Standards Page 4 Denied Appeals If an appeal is denied, the student is not eli”
### `e201aebe6ad0d2f8` Winthrop University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.winthrop.edu/finaid/sc-scholarships.aspx (sha256 51c5e2f4fa56)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Students with extenuating circumstances can appeal the loss of their state scholarship after the annual review has determined they do not meet the requirements to be renewed.”
### `9f54751316913ee6` Winthrop University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.winthrop.edu/finaid/cost-of-attendance-2526.aspx (sha256 da22c07ec026)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:TUITION: 14010 ⟵ “TUITION | $14,010”
  - column:AVERAGE FEES: 1054 ⟵ “AVERAGE FEES | $1,054”
  - column:HOUSING/FOOD: 13390 ⟵ “HOUSING/FOOD | $13,390”
  - column:BOOKS/SUPPLIES1: 1200 ⟵ “BOOKS/SUPPLIES1 | $1,200”
  - column:TRANSPORTATION: 2442 ⟵ “TRANSPORTATION | $2,442”
  - column:PERSONAL: 4048 ⟵ “PERSONAL | $4,048”
  - column:LOAN FEES: 90 ⟵ “LOAN FEES | $90”
  - column:TOTAL: 36234 ⟵ “TOTAL | $36,234”
### `eab907f5896c71c8` Winthrop University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.winthrop.edu/finaid/cost-of-attendance-2627.aspx (sha256 0b37782aa23e)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:TUITION: 13980 ⟵ “TUITION | $13,980”
  - column:AVERAGE FEES: 1084 ⟵ “AVERAGE FEES | $1,084”
  - column:HOUSING/FOOD: 14112 ⟵ “HOUSING/FOOD | $14,112”
  - column:BOOKS/SUPPLIES1: 1200 ⟵ “BOOKS/SUPPLIES1 | $1,200”
  - column:TRANSPORTATION: 2702 ⟵ “TRANSPORTATION | $2,702”
  - column:PERSONAL: 4168 ⟵ “PERSONAL | $4,168”
  - column:LOAN FEES: 94 ⟵ “LOAN FEES | $94”
  - column:TOTAL: 37340 ⟵ “TOTAL | $37,340”
### `54220a1f5324aa7a` Winthrop University — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.winthrop.edu/admissions/transfer/frequently-asked-questions.aspx (sha256 8ad7cd5a59d8)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Each academic college will evaluate all transfer credits with final grades of "C-" or better from an accredited institution during your Transfer Student Orientation.”
### `0b23ca218f6118f6` Wofford College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.wofford.edu/wofford.edu/documents/financial-aid/handbook.pdf (sha256 27fb4936be6b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Students and parents (if dependent) should complete the applicable 15 2025-26 Special Circumstances Worksheet.”
  - sentence: need_based_special_circumstances ⟵ “Appeals process If the student feels there are unusual circumstances regarding the withdrawal date, they have the right to appeal.”
### `22371ef8fd51335d` Wofford College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.wofford.edu/admission/financial-aid/forms (sha256 21b9fae53421)
- issues: semantic_review_required, conflicting_sources:https://www.wofford.edu/admission/financial-aid/faq
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Dependent Standard Verification Worksheet Independent Standard Verification Worksheet Custom Verification Worksheet Dependent Aggregate Verification Worksheet Independent Aggregate Verification Worksheet Dependent Asset Worksheet Special Circumstances Have you or your family experienced special circumstances since completing the FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “If you believe this may pertain to you, please review, complete and submit our Special Circumstances Worksheet.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Worksheet State Residency Forms Residency forms are used to verify that an in-state student meets the SC residency requirement in order to receive state grants and scholarships.”
  - sentence: need_based_special_circumstances ⟵ “Citizenship Verification Form for SC Residents Unusual Circumstances Federal regulations permit the college to override a student’s dependency status for federal financial aid purposes if extenuating circumstances exist and can be documented.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Note: All documentation must be submitted at the same time in order for it to be evaluated.”
  - sentence: need_based_special_circumstances ⟵ “The following conditions are NOT considered unusual circumstances: Parents refuse to contribute to the student’s education.”
### `6f90b175dcbd405d` Wofford College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wofford.edu/admission/financial-aid/faq (sha256 dd6c95c24903)
- issues: semantic_review_required, conflicting_sources:https://www.wofford.edu/admission/financial-aid/forms
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The family may qualify for a Special Circumstances review.”
  - sentence: need_based_special_circumstances ⟵ “The Special Circumstances review process requires submission of several documents and may adjust the Student Aid Index (SAI).”
### `d6e5198b2545fc24` Wofford College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.wofford.edu/wofford.edu/documents/financial-aid/handbook.pdf (sha256 27fb4936be6b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The financial aid committee is composed of the director of financial aid, the director of admission, the registrar, and/or other members of the administrative staff and/or faculty as needed. • A student not meeting Wofford’s standards for SAP may appeal if extenuating circumstances existed that resulted in substandard academic performance. • A student not meeting minimum grade point averages for s”
  - sentence: sap_appeal ⟵ “An approved appeal by one office does not guarantee an approved appeal by the other office. 13 Academic plans If the student fails to meet Satisfactory Academic Progress at the end of the probationary term, the student may appeal again.”
### `e51af5ef1aa082f9` Wofford College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.wofford.edu/financial-aid-scholarships/rule-satisfactory-academic-progress/rule-satisfactory-academic-progress.pdf (sha256 ca88d4383844)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “However, the The Satisfactory Academic Progress rule consists of both a Qualitative approval of an academic exclusion appeal will not automatically reinstate Component and a Quantitative Component.”
### `cf3666580225e35e` Wofford College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wofford.edu/administration/business-office/billing-tuition-and-fees (sha256 2a67ad6cdab5)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 13}
  - on_campus:Academic Year 2026-2027:: 78125 ⟵ “Academic Year 2026-2027: | $78,125”
  - on_campus:Fall 2026 Tuition and Fees:: 30290 ⟵ “Fall 2026 Tuition and Fees: | $30,290”
  - on_campus:Fall 2026 Meals and Housing:: 8772.5 ⟵ “Fall 2026 Meals and Housing: | $8,772.50*”
  - on_campus:Spring 2027 Tuition and Fees:: 30290 ⟵ “Spring 2027 Tuition and Fees: | $30,290”
  - on_campus:Spring 2027 Meals and Housing:: 8772.5 ⟵ “Spring 2027 Meals and Housing: | $8,772.50*”
  - on_campus:Other Estimated Expenses(non-billable):: 4076 ⟵ “Other Estimated Expenses(non-billable): | $4,076”
  - on_campus:Fall 2026 Books/Supplies: 654 ⟵ “Fall 2026 Books/Supplies | $654”
  - on_campus:Fall 2026 Misc: 711 ⟵ “Fall 2026 Misc | $711”
  - on_campus:Fall 2026 Transportation: 673 ⟵ “Fall 2026 Transportation | $673”
  - on_campus:Spring 2027 Books/Supplies: 654 ⟵ “Spring 2027 Books/Supplies | $654”
  - on_campus:Spring 2027 Misc: 711 ⟵ “Spring 2027 Misc | $711”
  - on_campus:Spring 2027 Transportation: 673 ⟵ “Spring 2027 Transportation | $673”
  - on_campus:Total Cost of Attendance On Campus:: 82201 ⟵ “Total Cost of Attendance On Campus: | $82,201”
### `8204aba58f98f5d5` Wofford College — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://catalog.wofford.edu/admission/transfer-student-admission/ (sha256 a0df778e8141)
- issues: stale_year_label:2025-26
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “Wofford’s residency requirement stipulates that the last 30 credit hours of coursework and more than half of the requirements for the major/minor must be completed at Wofford College in order to earn a Wofford degree.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 100; pages by category: admissions_tests 37, aid_appeals 4, ap_credit 5, cost_of_attendance 6, dual_enrollment 5, ib_credit 1, merit_scholarships 44, residency 19, statewide_articulation 2, transfer_credit 20, tuition_fees 40

## Blocked by the site (every request refused; needs the browser fallback)

- Technical College of the Lowcountry (`ipeds-217712`)
- Northeastern Technical College (`ipeds-217837`)
- Orangeburg Calhoun Technical College (`ipeds-218487`)
- Coastal Carolina University (`ipeds-218724`)
- Spartanburg Methodist College (`ipeds-218821`)
- Central Carolina Technical College (`ipeds-218858`)

## Leads: official pages found with no extracted record

- Aiken Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, statewide_articulation, degree_requirements
- Allen University: tuition_fees, cost_of_attendance, merit_scholarships, degree_requirements
- American College of the Building Arts: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- Anderson University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, residency, degree_requirements
- Benedict College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency, degree_requirements
- Bob Jones University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Charleston Southern University: cost_of_attendance, admissions_tests, ap_credit, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Citadel Military College of South Carolina: admissions_tests, merit_scholarships, transfer_credit
- Claflin University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, residency, degree_requirements
- Clemson University: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, residency, degree_requirements
- Clinton College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Coker University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, degree_requirements
- College of Charleston: admissions_tests
- Columbia College: admissions_tests, transfer_credit
- Columbia International University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- Converse University: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Denmark Technical College: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Erskine College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Florence-Darlington Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Francis Marion University: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, ib_credit, residency, degree_requirements, aid_appeals
- Furman University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Greenville Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency
- Horry-Georgetown Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Lander University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- Midlands Technical College: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Morris College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- Newberry College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, degree_requirements
- North Greenville University: cost_of_attendance, admissions_tests, transfer_credit, residency
- Piedmont Technical College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Presbyterian College: admissions_tests, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- South Carolina State University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Southern Wesleyan University: cost_of_attendance, admissions_tests, common_data_set, statewide_articulation, residency, aid_appeals
- Spartanburg Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Tri-County Technical College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, residency
- Trident Technical College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- University of South Carolina Aiken: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- University of South Carolina Beaufort: cost_of_attendance, admissions_tests, residency
- University of South Carolina-Columbia: admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency
- University of South Carolina-Lancaster: cost_of_attendance, admissions_tests, statewide_articulation, residency
- University of South Carolina-Salkehatchie: admissions_tests, merit_scholarships, statewide_articulation, residency
- University of South Carolina-Sumter: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency
- University of South Carolina-Union: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency
- University of South Carolina-Upstate: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, residency, degree_requirements
- Voorhees University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Williamsburg Technical College: tuition_fees, cost_of_attendance, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- Winthrop University: admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Wofford College: tuition_fees, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- York Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
