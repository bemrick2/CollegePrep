# Review queue — NM (2026-27)

Pages fetched: 1634; failures: 227. Candidates: 129 (26 without issues, 103 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 1 | 8 | 16 | 3 | 2 |
| cost_of_attendance | 0 | 0 | 1 | 6 | 12 | 9 | 2 |
| admissions_tests | 0 | 0 | 0 | 1 | 24 | 3 | 2 |
| common_data_set | 0 | 0 | 0 | 1 | 13 | 14 | 2 |
| merit_scholarships | 0 | 0 | 2 | 1 | 22 | 3 | 2 |
| ap_credit | 0 | 0 | 1 | 1 | 5 | 21 | 2 |
| clep_credit | 0 | 0 | 1 | 2 | 5 | 20 | 2 |
| ib_credit | 0 | 0 | 0 | 1 | 3 | 24 | 2 |
| dual_enrollment | 0 | 0 | 4 | 1 | 16 | 7 | 2 |
| transfer_credit | 0 | 0 | 3 | 0 | 20 | 5 | 2 |
| statewide_articulation | 0 | 0 | 0 | 0 | 9 | 19 | 2 |
| residency | 0 | 0 | 0 | 0 | 20 | 8 | 2 |
| degree_requirements | 0 | 0 | 0 | 0 | 18 | 10 | 2 |
| aid_appeals | 0 | 0 | 0 | 13 | 7 | 8 | 2 |

## Ready for review (26)

### `5bcfb08874a68a16` Eastern New Mexico University-Roswell Campus — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.roswell.enmu.edu/admissions/ (sha256 61dc0bda493f)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer 30 credit hours or more – with a GPA of at least 2.0 AND – a college-level English course with a grade of C or better Math Transfer equivalent math credit Applied/technical math credit will be evaluated on a case-by-case basis.”
### `02ee694a03288e64` Luna Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://luna.edu/admissions_aid/registrar_records_transcripts_graduation.php (sha256 a446dc2d7a4a)
- checks: {"thresholds": null}
  - test_requirement: Click Here ⟵ “Alicia Chacon | Associate Registrar | 505-454-2546 | x1215 | Click Here”
### `6ae0004ea72897d2` Luna Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://luna.edu/admissions_aid/registrar_records_transcripts_graduation.php (sha256 a446dc2d7a4a)
- checks: {"thresholds": null}
  - test_requirement: Click Here ⟵ “Rachael Lucero | Registrar | 505-587-3829 | x1223 | Click Here”
### `7e0f47d7344078c3` Luna Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://luna.edu/admissions_aid/registrar_records_transcripts_graduation.php (sha256 a446dc2d7a4a)
- checks: {"thresholds": null}
  - test_requirement: Click Here ⟵ “Ida Valdez | Associate Registrar | 505-587-3823 | x3003 | Click Here”
### `86cc496a5f136e19` New Mexico Institute of Mining and Technology — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.nmt.edu/institute-reqs/graduation-reqs (sha256 ff7649293c73)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “The student must complete a minimum of the last 30 credit hours at Tech.”
### `dee9fc7bffe0b14d` New Mexico Junior College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.nmjc.edu/community/dual_credit/files/2026-2027%20DC%20Policy%20Guide.pdf (sha256 b7e82232866d)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.0 ⟵ “minimum 2.0 high school GPA to be eligible (2.5 minimum for the CNA program). Accuplacer score”
  - eligibility_tier: 2.0 ⟵ “upon attaining a 2.0 cumulative grade point average.”
### `0568d3a244602cdc` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/private.html (sha256 c0c710bdc42e)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Acker Warren Youth Mentor Scholarship | $1,000 | November 2nd, 2026 | Undergraduate Students | Any”
### `08fc6d8d8d98f6d0` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.nmsu.edu/cost-and-aid/scholarships.html (sha256 0a8b542de58f)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 per academic year. ⟵ “Hadley Honors Out-of-State Scholarship | 3.9 GPA or Academic Index of 159 and above . US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 Las Cruces campus credits per semester. | Must be a”
  - eligibility_summary: 3.9 GPA or Academic Index of 159 and above . US Citizen or Permanent Resident. ⟵ “Hadley Honors Out-of-State Scholarship | 3.9 GPA or Academic Index of 159 and above . US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 Las Cruces campus credits per semester. | Must be a”
  - renewal_requirements: 3.3 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 Las Cruces campus credits per semester. ⟵ “Hadley Honors Out-of-State Scholarship | 3.9 GPA or Academic Index of 159 and above . US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 Las Cruces campus credits per semester. | Must be a”
### `16f7538028befc4e` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/private.html (sha256 c0c710bdc42e)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Kanoski Bresney Stand Up to Distracted Driving Scholarship | $1,000 | November 9th, 2026 | Graduate and Undergraduate Students | Any”
### `2d0a981902dc2301` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/private.html (sha256 c0c710bdc42e)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Goostree Law Group BrightFutures Scholarship | $1,000 | March 10th, 2027 | Graduate and Undergraduate Students | Any”
### `39bc744ce6404246` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/private.html (sha256 c0c710bdc42e)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Innovation in Education Scholarship | $500 | The 20th of each month | Undergraduate Students | Any”
### `66c206a2f87a440d` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.nmsu.edu/cost-and-aid/scholarships.html (sha256 0a8b542de58f)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per academic year. ⟵ “Crimson Success Out-of-State Scholarship | 3.7 – 3.89 GPA or Academic Index of 145 – 158.99 . US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester.”
  - eligibility_summary: 3.7 – 3.89 GPA or Academic Index of 145 – 158.99 . US Citizen or Permanent Resident. ⟵ “Crimson Success Out-of-State Scholarship | 3.7 – 3.89 GPA or Academic Index of 145 – 158.99 . US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester.”
  - renewal_requirements: 3.0 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ⟵ “Crimson Success Out-of-State Scholarship | 3.7 – 3.89 GPA or Academic Index of 145 – 158.99 . US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester.”
### `95cc2cae71255d92` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/private.html (sha256 c0c710bdc42e)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “First-Generation College Student Scholarship | $2,500 | March 22nd, 2027 | First-Generation Undergraduate Students | Any”
### `9da6d85e1fe7c86b` New Mexico State University-Main Campus — awards 2026-27 [new] (labeled_in_source)
- source: https://fa.nmsu.edu/scholarships/index.html (sha256 99c41df1f2c2)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 annual stipend for up to 4 years. Eligible to receive a $2,500 Global Citizen Award to help fund a study abroad experience with guidance from the Honors College. ⟵ “Conroy Honors Scholars | 3.9 GPA or Academic Index of 159 and above. For high school graduates, including students that are simultaneously completing an early college degree. US Citizen or Permanent Resident. | $6,000 annual stipend for up to 4 years. Eligible to receive a $2,500 Global Citizen Awar”
  - eligibility_summary: 3.9 GPA or Academic Index of 159 and above. For high school graduates, including students that are simultaneously completing an early college degree. US Citizen or Permanent Resident. ⟵ “Conroy Honors Scholars | 3.9 GPA or Academic Index of 159 and above. For high school graduates, including students that are simultaneously completing an early college degree. US Citizen or Permanent Resident. | $6,000 annual stipend for up to 4 years. Eligible to receive a $2,500 Global Citizen Awar”
  - renewal_requirements: Complete the first semester of college with a 3.25 GPA and pass 15 new-main campus credit hours. Thereafter, maintain a 3.5 cumulative GPA and pass 15 new Las Cruces campus credits every semester, for four years, and complete Honors College program requirements. ⟵ “Conroy Honors Scholars | 3.9 GPA or Academic Index of 159 and above. For high school graduates, including students that are simultaneously completing an early college degree. US Citizen or Permanent Resident. | $6,000 annual stipend for up to 4 years. Eligible to receive a $2,500 Global Citizen Awar”
### `a387574c0f4540e6` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/private.html (sha256 c0c710bdc42e)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “2026 BOC Sciences Chemistry Scholarship | $1,000 | October 31st, 2026 | Undergraduate, Graduate, or Ph.D. Students | Chemistry”
### `a77a91b39685d963` New Mexico State University-Main Campus — awards 2026-27 [new] (labeled_in_source)
- source: https://fa.nmsu.edu/scholarships/ (sha256 11ea09dc30cc)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 annual stipend for up to 4 years. $4,000 NMSU Housing Award for students who live on campus their first year. ⟵ “President's Associates Excellence Scholarship (Leader Scholar Program) | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. Students must begin attending their first regular college semester the fall immediately ”
  - eligibility_summary: 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. Students must begin attending their first regular college semester the fall immediately after graduating from high school. US Citizen or Permanent Resident. ⟵ “President's Associates Excellence Scholarship (Leader Scholar Program) | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. Students must begin attending their first regular college semester the fall immediately ”
  - renewal_requirements: Complete the first semester of college with a 3.25 GPA and pass 15 new-main campus credit hours. Thereafter, maintain a 3.5 cumulative GPA, pass 15 new Las Cruces campus credits every semester, and complete Leader Scholar Program requirements. ⟵ “President's Associates Excellence Scholarship (Leader Scholar Program) | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. Students must begin attending their first regular college semester the fall immediately ”
### `bedd8450487d5727` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.nmsu.edu/cost-and-aid/scholarships.html (sha256 0a8b542de58f)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 per academic year. ⟵ “1888 Leadership Out-of-State Scholarship | 3.5 – 3.69 GPA or Academic Index of 133 – 144.99. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ”
  - eligibility_summary: 3.5 – 3.69 GPA or Academic Index of 133 – 144.99. US Citizen or Permanent Resident. ⟵ “1888 Leadership Out-of-State Scholarship | 3.5 – 3.69 GPA or Academic Index of 133 – 144.99. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ”
  - renewal_requirements: 2.7 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ⟵ “1888 Leadership Out-of-State Scholarship | 3.5 – 3.69 GPA or Academic Index of 133 – 144.99. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credit hours per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ”
### `c551bd89046bbd68` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/private.html (sha256 c0c710bdc42e)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Next Generation Healers Scholarship | $1,000 | December 8th, 2026 | Graduate and Undergraduate Students | Any”
### `c8935133dc04536b` Northern New Mexico College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://nnmc.edu/paying-for-college/in_state_costs.html (sha256 b357615fe50c)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition & Fees: 5064 ⟵ “Tuition & Fees | $5,064 | $5,064”
  - off_campus_not_with_family:Books, Course MaterialsSupplies, Equipment*: 2000 ⟵ “Books, Course MaterialsSupplies, Equipment* | $2,000 | $2,000”
  - off_campus_not_with_family:Food & Housing: 12540 ⟵ “Food & Housing | $12,540 | $4,180”
  - off_campus_not_with_family:Transportation: 3000 ⟵ “Transportation | $3,000 | $3,000”
  - off_campus_not_with_family:Personal Expense: 3510 ⟵ “Personal Expense | $3,510 | $1,980”
  - off_campus_not_with_family:TOTAL COA: 26114 ⟵ “TOTAL COA | $26,114 | $16,224”
  - with_parents_or_family:Tuition & Fees: 5064 ⟵ “Tuition & Fees | $5,064 | $5,064”
  - with_parents_or_family:Books, Course MaterialsSupplies, Equipment*: 2000 ⟵ “Books, Course MaterialsSupplies, Equipment* | $2,000 | $2,000”
  - with_parents_or_family:Food & Housing: 4180 ⟵ “Food & Housing | $12,540 | $4,180”
  - with_parents_or_family:Transportation: 3000 ⟵ “Transportation | $3,000 | $3,000”
  - with_parents_or_family:Personal Expense: 1980 ⟵ “Personal Expense | $3,510 | $1,980”
  - with_parents_or_family:TOTAL COA: 16224 ⟵ “TOTAL COA | $26,114 | $16,224”
### `a7b225fb938bac63` Southeast New Mexico College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://senmc.edu/dual-credit/index.html (sha256 ad332aff7260)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.0 ⟵ “High school junior or senior with a 2.0 or higher cumulative GPA.”
  - eligibility_tier: 2.0 ⟵ “Maintain a high school GPA of at least 2.0.”
### `5a4d7f793200917f` University of New Mexico-Gallup Campus — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.gallup.unm.edu/admissions/transferring.html (sha256 157ed7e7a137)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer Students will be awarded full credit for coursework completed with grades of "C" or higher at fully accredited institutions if the courses are the same or equivalent to UNM courses.”
### `927fc4c5d451cda1` University of New Mexico-Los Alamos Campus — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://losalamos.unm.edu/students/transfer-students.html (sha256 fb0853328c16)
- checks: {"fields": ["min_grade"]}
  - min_grade: D ⟵ “Transfer Articulation Academic credits for courses completed at other post-secondary institutions can be transferred to UNM–Los Alamos if: A grade of D or better was earned in the course, The postsecondary institution is appropriately accredited, and UNM or UNM–Los Alamos offers an equivalent course as determined by the appropriate individual(s).”
### `4766ceb633fcec72` University of New Mexico-Main Campus — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://admissions.unm.edu/academics/testing/apibclep.html (sha256 6986d7fe6bf2)
- checks: {"distinct_exams": 37, "equivalencies": 69, "rows_without_score": 0}
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “4 | 07 US HISTORY | HIST1110 & HIST1120 | 6 CREDITS”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “3 | 07 US HISTORY | HIST1110 | 3 CREDITS”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “3 | 10 AFRICAN AMERICAN STUDIES | AFST1110 | 3 CREDITS”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “5 | 13 ART HISTORY | ARTH2110 & ARTH2120 | 6 CREDITS”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “3 | 13 ART HISTORY | ARTH1120 | 3 CREDITS”
  - equivalencies[AP-DRAWING|3]:  ⟵ “3 | 14 STUDIO ART: DRAWING | ARTS1610 | 3 CREDITS”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “4 | 15 STUDIO ART: 2D DESIGN | ARTS1240 & ARTS 2610 | 6 CREDITS”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “3 | 15 STUDIO ART: 2D DESIGN | ARTS1240 | 3 CREDITS”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “4 | 16 STUDIO ART: 3D DESIGN | ARTS1240 & ARTS2610 | 6 CREDITS”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3 | 16 STUDIO ART: 3D DESIGN | ARTS1240 | 3 CREDITS”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “5 | 20 BIOLOGY | BIOL2101 & BIOL2103L & BIOL2T** | 8 CREDITS”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “4 | 20 BIOLOGY | BIOL2101& BIOL2103L | 4 CREDITS”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “3 | 20 BIOLOGY | BIOL1140 & BIOL1140L | 4 CREDITS”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “3 | 65 PRECALCULUS | MATH1240 | 3 CREDITS”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “4 | 65 PRECALCULUS | MATH1250 | 5 CREDITS”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “4 | 66 CALCULUS AB | MATH1240 & MATH1512 | 7 CREDITS”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “3 | 66 CALCULUS AB (updated 11/7/25) was MATH1240 previously | MATH1250 | 3 CREDITS”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “4 | 68 CALCULUS BC | MATH1240, MATH1512, & MATH1522 | 11 CREDITS”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “3 | 68 CALCULUS BC | MATH1240 & MATH1512 | 7 CREDITS”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “5 | 25 CHEMISTRY | CHEM1215, CHEM1215L, CHEM1225, & CHEM1225L | 8 CREDITS”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “4 | 25 CHEMISTRY | CHEM1215 & CHEM1215L | 4 CREDITS”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “3 | 25 CHEMISTRY | CHEM1120C | 4 CREDITS”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “5 | 28 CHINESE LANG & CULT (added:11/7/25) | CHIN1130, CHIN1140 & CHIN2110 | 15 CREDITS”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “4 | 28 CHINESE LANG & CULT | CHIN1130, CHIN1140 | 12 CREDITS”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “3 | 28 CHINESE LANG & CULT | CHIN1130 | 6 CREDITS”
  - … 44 more rows
### `989137b206ea21a7` University of New Mexico-Main Campus — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://admissions.unm.edu/academics/testing/college-level-examination-program.html (sha256 28dc44db799e)
- checks: {"distinct_exams": 28, "equivalencies": 33, "rows_without_score": 0}
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|55]:  ⟵ “HISTORY OF THE UNITED STATES I: EARLY COLONIZATION TO 1877 | 55 | 3 | HIST 161/1110”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|55]:  ⟵ “HISTORY OF THE UNITED STATES II: 1865 TO THE PRESENT | 55 | 3 | HIST 162/1120”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “BIOLOGY | 50 | 3 | BIOL110/1110”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “CHEMISTRY | 63 | 8 | CHEM121/1215, CHEM123L/1215L, CHEM122/1225, & CHEM 124L/1225L”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|54]:  ⟵ “MICROECONOMICS | 54 | 3 | ECON106/2120”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|54]:  ⟵ “MACROECONOMICS | 54 | 3 | ECON105/2110”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “COLLEGE COMPOSITION | 50 | 6 | ENGL 1110 & ENGL 1T**”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|N/A]:  ⟵ “FRESHMAN COLLEGE COMPOSITION | N/A | NO CREDIT | NO EQUIV”
  - equivalencies[CLEP-ENGLISH-LITERATURE|N/A]:  ⟵ “ENGLISH LITERATURE | N/A | NO CREDIT | NO EQUIV”
  - equivalencies[CLEP-AMERICAN-LITERATURE|N/A]:  ⟵ “AMERICAN LITERATURE | N/A | NO CREDIT | NO EQUIV”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “ANALYZING & INTERPRETING LITERATURE | 50 | 3 | ENGL 150/ENGL1410”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|55]:  ⟵ “WESTERN CIV I | 55 | 3 | HIST101/1150”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|55]:  ⟵ “WESTERN CIV II | 55 | 3 | HIST102/1160”
  - equivalencies[CLEP-FRENCH-LANGUAGE|52]:  ⟵ “FRENCH LANGUAGE (AKA: COLLEGE FRENCH LEVEL I & II) | 52 | 6 | FREN 101/1110 & FREN 102/1120”
  - equivalencies[CLEP-FRENCH-LANGUAGE|48]:  ⟵ “FRENCH LANGUAGE (AKA: COLLEGE FRENCH LEVEL I & II) | 48 | 3 | FREN101/1110”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “GERMAN LANGUAGE (AKA: COLLEGE GERMAN LEVELS I & II) | 63 | 6 | GRMN 101/1110 & GRMN 102/1120”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|65]:  ⟵ “AMERICAN GOVERNMENT | 65 | 3 | POLS200/1120”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|59]:  ⟵ “COLLEGE ALGEBRA | 59 | 3 | MATH 121/1220”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|N/A]:  ⟵ “COLLEGE ALGEBRA & TRIGONOMETRY | N/A | NO CREDIT | NO EQUIV”
  - equivalencies[CLEP-CALCULUS|70]:  ⟵ “CALCULUS WITH ELEMENTARY FUNCTIONS | 70 | 4 | MATH 162/1512”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|59]:  ⟵ “SOCIOLOGY | 59 | 3 | SOC 101/SOCI1110”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|63]:  ⟵ “HUMAN GROWTH & DEVELOPMENT | 63 | 3 | PSY 220/2120”
  - equivalencies[CLEP-SPANISH-LANGUAGE|57]:  ⟵ “SPANISH LANGUAGE (AKA: COLLEGE SPANISH LEVELS I & II) | 57 | 12 | SPAN 101/1110, SPAN 102/1120, SPAN 201/2110, & SPAN 202/2120”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “SPANISH LANGUAGE (AKA: COLLEGE SPANISH LEVELS I & II) | 50 | 6 | SPAN101/1110 & SPAN102/1120”
  - equivalencies[CLEP-SPANISH-LANGUAGE|45]:  ⟵ “SPANISH LANGUAGE (AKA: COLLEGE SPANISH LEVELS I & II) | 45 | 3 | SPAN101/1110”
  - … 8 more rows
### `645d4ef4b49539a6` University of New Mexico-Taos Campus — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://taos.unm.edu/academic-programs/dual-enrollment/ (sha256 ee7f5317f092)
- checks: {"fields": [], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “Have a cumulative unweighted high school GPA of 2.5 for academic courses and 2.0 for career and technical education courses”
### `4f48612ecad0a8f8` Western New Mexico University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://admissions.wnmu.edu/admissions/ (sha256 442960d157e7)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “A petition to overload requests formal permission for a student to register for more credits than the maximum academic load allowed per semester. Dual Credit students wanting to take more than 18 hours in a regular term (fall or spring) or more than 12 credits in the summer term MUST have permission”

## Exceptions (103)

### `7284bcd4f42ad925` Clovis Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.clovis.edu/financialaid/sap.aspx (sha256 59628dc543a7)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students on Financial Aid Suspension are ineligible for future Title IV aid until they regain eligibility by meeting SAP standards or appeal and are reinstated.”
### `0d74272fd154adac` Clovis Community College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.clovis.edu/financialaid/coa.aspx (sha256 9099cb1d6446)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - other:Tuition: 1416 ⟵ “Tuition | 1,152 | 1,152 | 1,416 | 1,416 | 2,904 | 2,904 | 1,152”
  - other:Fees: 440 ⟵ “Fees | 440 | 440 | 440 | 440 | 440 | 440 | 440”
  - other:Room & Board: 5523 ⟵ “Room & Board | 10,296 | 5,523 | 10,296 | 5,523 | 10,296 | 5,523 | 5,523”
  - other:Books: 864 ⟵ “Books | 864 | 864 | 864 | 864 | 864 | 864 | 864”
  - other:Transportation: 1715 ⟵ “Transportation | 515 | 515 | 1,715 | 1,715 | 1,715 | 1,715 | 515”
  - other:Miscellaneous: 1768 ⟵ “Miscellaneous | 2,077 | 1,768 | 2,077 | 1,768 | 2,077 | 1,768 | 2,077”
  - other:Total Cost: 11726 ⟵ “Total Cost | 15,344 | 10,262 | 16,808 | 11,726 | 18,296 | 13,214 | 10,571”
  - column:Tuition: 2904 ⟵ “Tuition | 1,152 | 1,152 | 1,416 | 1,416 | 2,904 | 2,904 | 1,152”
  - column:Fees: 440 ⟵ “Fees | 440 | 440 | 440 | 440 | 440 | 440 | 440”
  - column:Room & Board: 10296 ⟵ “Room & Board | 10,296 | 5,523 | 10,296 | 5,523 | 10,296 | 5,523 | 5,523”
  - column:Books: 864 ⟵ “Books | 864 | 864 | 864 | 864 | 864 | 864 | 864”
  - column:Transportation: 1715 ⟵ “Transportation | 515 | 515 | 1,715 | 1,715 | 1,715 | 1,715 | 515”
  - column:Miscellaneous: 2077 ⟵ “Miscellaneous | 2,077 | 1,768 | 2,077 | 1,768 | 2,077 | 1,768 | 2,077”
  - column:Total Cost: 18296 ⟵ “Total Cost | 15,344 | 10,262 | 16,808 | 11,726 | 18,296 | 13,214 | 10,571”
  - column:Tuition: 2904 ⟵ “Tuition | 1,152 | 1,152 | 1,416 | 1,416 | 2,904 | 2,904 | 1,152”
  - column:Fees: 440 ⟵ “Fees | 440 | 440 | 440 | 440 | 440 | 440 | 440”
  - column:Room & Board: 5523 ⟵ “Room & Board | 10,296 | 5,523 | 10,296 | 5,523 | 10,296 | 5,523 | 5,523”
  - column:Books: 864 ⟵ “Books | 864 | 864 | 864 | 864 | 864 | 864 | 864”
  - column:Transportation: 1715 ⟵ “Transportation | 515 | 515 | 1,715 | 1,715 | 1,715 | 1,715 | 515”
  - column:Miscellaneous: 1768 ⟵ “Miscellaneous | 2,077 | 1,768 | 2,077 | 1,768 | 2,077 | 1,768 | 2,077”
  - column:Total Cost: 13214 ⟵ “Total Cost | 15,344 | 10,262 | 16,808 | 11,726 | 18,296 | 13,214 | 10,571”
  - column:Tuition: 1152 ⟵ “Tuition | 1,152 | 1,152 | 1,416 | 1,416 | 2,904 | 2,904 | 1,152”
  - column:Fees: 440 ⟵ “Fees | 440 | 440 | 440 | 440 | 440 | 440 | 440”
  - column:Room & Board: 5523 ⟵ “Room & Board | 10,296 | 5,523 | 10,296 | 5,523 | 10,296 | 5,523 | 5,523”
  - column:Books: 864 ⟵ “Books | 864 | 864 | 864 | 864 | 864 | 864 | 864”
  - … 3 more rows
### `4ed4f6b5ad355ab2` Clovis Community College — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.clovis.edu/financialaid/coa.aspx (sha256 9099cb1d6446)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 1416 ⟵ “Tuition | 1,152 | 1,152 | 1,416 | 1,416 | 2,904 | 2,904 | 1,152”
  - column:Fees: 440 ⟵ “Fees | 440 | 440 | 440 | 440 | 440 | 440 | 440”
  - column:Room & Board: 10296 ⟵ “Room & Board | 10,296 | 5,523 | 10,296 | 5,523 | 10,296 | 5,523 | 5,523”
  - column:Books: 864 ⟵ “Books | 864 | 864 | 864 | 864 | 864 | 864 | 864”
  - column:Transportation: 1715 ⟵ “Transportation | 515 | 515 | 1,715 | 1,715 | 1,715 | 1,715 | 515”
  - column:Miscellaneous: 2077 ⟵ “Miscellaneous | 2,077 | 1,768 | 2,077 | 1,768 | 2,077 | 1,768 | 2,077”
  - column:Total Cost: 16808 ⟵ “Total Cost | 15,344 | 10,262 | 16,808 | 11,726 | 18,296 | 13,214 | 10,571”
### `564143c0bc71c965` Clovis Community College — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.clovis.edu/financialaid/coa.aspx (sha256 9099cb1d6446)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 1152 ⟵ “Tuition | 1,152 | 1,152 | 1,416 | 1,416 | 2,904 | 2,904 | 1,152”
  - on_campus:Fees: 440 ⟵ “Fees | 440 | 440 | 440 | 440 | 440 | 440 | 440”
  - on_campus:Room & Board: 10296 ⟵ “Room & Board | 10,296 | 5,523 | 10,296 | 5,523 | 10,296 | 5,523 | 5,523”
  - on_campus:Books: 864 ⟵ “Books | 864 | 864 | 864 | 864 | 864 | 864 | 864”
  - on_campus:Transportation: 515 ⟵ “Transportation | 515 | 515 | 1,715 | 1,715 | 1,715 | 1,715 | 515”
  - on_campus:Miscellaneous: 2077 ⟵ “Miscellaneous | 2,077 | 1,768 | 2,077 | 1,768 | 2,077 | 1,768 | 2,077”
  - on_campus:Total Cost: 15344 ⟵ “Total Cost | 15,344 | 10,262 | 16,808 | 11,726 | 18,296 | 13,214 | 10,571”
### `8e3b1120c2911e2b` Eastern New Mexico University-Main Campus — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.enmu.edu/admission/tuition-fees (sha256 8addeac6a235)
- issues: cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Undergraduate Tuition: 3087 ⟵ “Undergraduate Tuition | $3,087”
  - column:Student Fees: 1440 ⟵ “Student Fees | $1,440”
  - column:Total Per Semester: 4527 ⟵ “Total Per Semester | $4,527”
### `c30f6d77c2b3928a` Eastern New Mexico University-Main Campus — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.enmu.edu/admission/tuition-fees (sha256 37dc37c08832)
- issues: cost_period_semester
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Undergraduate Tuition: 3087 ⟵ “Undergraduate Tuition | $3,087”
  - column:Student Fees: 1440 ⟵ “Student Fees | $1,440”
  - column:Total Per Semester: 4527 ⟵ “Total Per Semester | $4,527”
### `e6975faa3300fd97` Eastern New Mexico University-Main Campus — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.enmu.edu/admission/tuition-fees (sha256 37dc37c08832)
- issues: cost_period_semester
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Undergraduate Tuition: 2097 ⟵ “Undergraduate Tuition | $2,097”
  - column:Student Fees: 1440 ⟵ “Student Fees | $1,440”
  - column:Total Per Semester: 3537 ⟵ “Total Per Semester | $3,537”
### `ec17cec088c3469b` Eastern New Mexico University-Main Campus — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.enmu.edu/admission/tuition-fees (sha256 8addeac6a235)
- issues: cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Undergraduate Tuition: 2097 ⟵ “Undergraduate Tuition | $2,097”
  - column:Student Fees: 1440 ⟵ “Student Fees | $1,440”
  - column:Total Per Semester: 3537 ⟵ “Total Per Semester | $3,537”
### `78076a24197503ba` Eastern New Mexico University-Roswell Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.roswell.enmu.edu/wp-content/uploads/delightful-downloads/2024/11/SAP-Policy-Special-Services-Programs.pdf (sha256 fa4994fb5f96)
- issues: semantic_review_required, conflicting_sources:https://www.roswell.enmu.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal by completing a SAP appeal form or 2.”
  - sentence: sap_appeal ⟵ “Students have the right to submit an appeal for an extension of timeframe status FINANCIAL AID APPEALS (SAP Appeals) A student who is OFFAID for failing to meet Satisfactory SAP may regain eligibility by successfully appealing to the Financial Aid Administration if he/she had an extenuating circumstance that prevented him/her from successfully meeting SAP standards.”
  - sentence: sap_appeal ⟵ “If the student is meeting the criteria identified in the SAP appeal approval at the end of the term, the student’s academic plan may be extended.”
### `918b98aaa6f87d66` Eastern New Mexico University-Roswell Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.roswell.enmu.edu/financial-aid/ (sha256 ae938f74863b)
- issues: semantic_review_required, conflicting_sources:https://www.roswell.enmu.edu/wp-content/uploads/delightful-downloads/2024/11/SAP-Policy-Special-Services-Programs.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “A student who is OFFAID has two options: Appeal by completing a SAP appeal form or Attend at their own expense until the student raises their cumulative GPA to 2.0 and has a 67% completion rate.”
  - sentence: sap_appeal ⟵ “FINANCIAL AID APPEALS (SAP Appeals) A student who is OFFAID for failing to meet Satisfactory SAP may regain eligibility by successfully appealing to the Financial Aid Administration if they had an extenuating circumstance that prevented them from successfully meeting SAP standards.”
  - sentence: sap_appeal ⟵ “If the student is meeting the criteria identified in the SAP appeal approval at the end of the term, the student’s academic plan may be extended.”
### `a0afd4a0fe2c3e86` Eastern New Mexico University-Roswell Campus — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.roswell.enmu.edu/financial-aid/ (sha256 ae938f74863b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “An extenuating/special circumstance must exist and be supported by additional documentation in order to file an appeal to regain financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “A special circumstance may include injury, illness, the death of a relative, or other special circumstance during the term the aid was received.”
### `1a88d54016c321fa` Eastern New Mexico University-Roswell Campus — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.roswell.enmu.edu/financial-aid/tuition-and-fees/ (sha256 afde150c9dcf)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 2616.0 ⟵ “Tuition | $2,616.00”
  - column:Fees: 192.0 ⟵ “Fees | $192.00”
  - column:Total: 2808.0 ⟵ “Total | $2,808.00”
### `41dfac343e2dfcf2` Eastern New Mexico University-Roswell Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.roswell.enmu.edu/financial-aid/ (sha256 ae938f74863b)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "rows": 7}
  - column:Tuition: 1872.0 ⟵ “Tuition | $1,872.00 | $5,232.00”
  - column:Fees: 414.0 ⟵ “Fees | $414.00 | $414.00”
  - column:Books and Supplies: 1548.0 ⟵ “Books and Supplies | $1,548.00 | $1,548.00”
  - column:Room and Board: 6542.0 ⟵ “Room and Board | $6,542.00 | $6,542.00”
  - column:Personal Expenses: 2411.0 ⟵ “Personal Expenses | $2,411.00 | $2,411.00”
  - column:Transportation: 1967.0 ⟵ “Transportation | $1,967.00 | $1,967.00”
  - column:Totals: 14754.0 ⟵ “Totals | $14,754.00 | $18,114.00”
  - column:Tuition: 5232.0 ⟵ “Tuition | $1,872.00 | $5,232.00”
  - column:Fees: 414.0 ⟵ “Fees | $414.00 | $414.00”
  - column:Books and Supplies: 1548.0 ⟵ “Books and Supplies | $1,548.00 | $1,548.00”
  - column:Room and Board: 6542.0 ⟵ “Room and Board | $6,542.00 | $6,542.00”
  - column:Personal Expenses: 2411.0 ⟵ “Personal Expenses | $2,411.00 | $2,411.00”
  - column:Transportation: 1967.0 ⟵ “Transportation | $1,967.00 | $1,967.00”
  - column:Totals: 18114.0 ⟵ “Totals | $14,754.00 | $18,114.00”
### `eb8c462a5e0ace7b` Eastern New Mexico University-Roswell Campus — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.roswell.enmu.edu/financial-aid/tuition-and-fees/ (sha256 afde150c9dcf)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 936.0 ⟵ “Tuition | $936.00”
  - column:Fees: 192.0 ⟵ “Fees | $192.00”
  - column:Total: 1128.0 ⟵ “Total | $1,128.00”
### `10fd8b8dc25ccb17` Luna Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://luna.edu/admissions_aid/student_rights_and_responsibilities.php (sha256 7ca359687417)
- issues: semantic_review_required, conflicting_sources:https://luna.edu/Document/Admissions%20Aid/Financial%20Aid/Student%20Rights%20and%20Responsibilities/SAP%20Policy%20FINAL.pdf?t=202606161805500
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The student may submit a SAP Appeal if there were extenuating circumstances that prevented the student from satisfying any of the components above.”
### `13b6b44e8666d0af` Luna Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://luna.edu/admissions_aid/general_information.php (sha256 01da0bc1fb95)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If your Unusual Circumstance Appeal is approved, the LCC Financial Aid Office may use Professional Judgment to override your dependency status for FAFSA purposes.”
  - sentence: professional_judgment ⟵ “If the appeal is approved, the LCC Financial Aid Office may use Professional Judgment to adjust the items reported on the FAFSA to re-evaluate your financial aid eligibility.”
### `1b89b84752a089b9` Luna Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://luna.edu/admissions_aid/student_rights_and_responsibilities.php (sha256 7ca359687417)
- issues: semantic_review_required, conflicting_sources:https://luna.edu/Document/Admissions%20Aid/Financial%20Aid/Financial%20Aid%20Forms/Unusual%20Circumstance%20Appeal%20Form.pdf?t=202606161901050
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If the student’s financial circumstances have changed, the student must submit a Special Circumstance Appeal form to the Financial Aid Office.”
### `2019f1865fdc94e0` Luna Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://luna.edu/Document/Admissions%20Aid/Financial%20Aid/Financial%20Aid%20Forms/Unusual%20Circumstance%20Appeal%20Form.pdf?t=202606161901050 (sha256 f4b3e46fcc6f)
- issues: semantic_review_required, conflicting_sources:https://luna.edu/admissions_aid/student_rights_and_responsibilities.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “There are some instances where a student does not meet the criteria for an independent student but there are unusual circumstances that warrant an independent student status.”
### `3c24be953feaa33a` Luna Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://luna.edu/admissions_aid/general_information.php (sha256 01da0bc1fb95)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “If you cannot answer “Yes” to the FAFSA dependency questions, you are required to include your parent information; however, if you cannot or should not have contact with your parent due to extenuating circumstances such as abuse or abandonment you may complete an Unusual Circumstance Appeal Form.”
  - sentence: need_based_special_circumstances ⟵ “What if my family has special circumstances and my FAFSA does not accurately reflect my family's financial situation?”
  - sentence: need_based_special_circumstances ⟵ “If your family’s financial situation has changed since you completed your FAFSA such as parent losing a job due to business closure or layoff, or a parent has become deceased, or your parents have divorced/separated, you may complete a Special Circumstance Appeal.”
  - sentence: need_based_special_circumstances ⟵ “You must meet with a Financial Aid Advisor to request the Special Circumstance Appeal Form.”
### `80efc7a0e9f0c71e` Luna Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://luna.edu/Document/Admissions%20Aid/Financial%20Aid/Student%20Rights%20and%20Responsibilities/SAP%20Policy%20FINAL.pdf?t=202606161805500 (sha256 81144159d9f3)
- issues: semantic_review_required, conflicting_sources:https://luna.edu/admissions_aid/student_rights_and_responsibilities.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The SAP Appeal deadline is the second Friday of the semester.”
### `01698f3268a78b91` Luna Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://luna.edu/admissions_aid/general_information.php (sha256 01da0bc1fb95)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 1224 ⟵ “Tuition | $1,224”
  - column:Fees: 266 ⟵ “Fees | $266”
  - column:Books & Supplies: 464 ⟵ “Books & Supplies | $464”
  - column:Housing & Food: 9317 ⟵ “Housing & Food | $9,317”
  - column:Transportation: 6381 ⟵ “Transportation | $6,381”
  - column:Personal Expenses: 5862 ⟵ “Personal Expenses | $5,862”
  - column:Total Academic Year Cost of Attendance*: 23514 ⟵ “Total Academic Year Cost of Attendance* | $23,514”
### `46c6ceb63c27f4f4` Navajo Technical University — appeals 2012-13 [new] (labeled_in_source)
- source: https://www.navajotech.edu/students/financial-aid/ (sha256 bd075b12e212)
- issues: stale_year_label:2012-13, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students who exceed the maximum timeframe can submit an SAP Appeal to determine if their aid can be reinstated.”
### `09b17603a2bad521` New Mexico Highlands University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://its.nmhu.edu/IntranetUploads/009182-CommonData-8182026115318.pdf (sha256 c35cfc90d7d8)
- issues: applications_breakdown_does_not_reconcile, admits_breakdown_does_not_reconcile, enrolled_breakdown_does_not_reconcile, stale_year_label:2024-25
- checks: {"fields": ["admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 575 ⟵ “Total first-time, first-year who applied                                                  1579                  763            236           575”
  - admits: 504 ⟵ “Total first-time, first-year who were admitted                                            1476                  757            233           504”
  - enrolled: 55 ⟵ “Total first-time, first-year who enrolled                                                  230                  163              8            55”
### `9fbdc16b700bde46` New Mexico Highlands University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nmhu.edu/financial-aid/cost-of-attending/ (sha256 c501e262e13d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “A one-time computer budget adjustment is also allowed.”
### `d2babe1087414f82` New Mexico Highlands University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nmhu.edu/financial-aid/scholarships/ (sha256 4d99688a6a77)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Be eligible according to standard needs analysis or the financial aid officer’s professional judgment.”
### `36dd280c77856a0d` New Mexico Highlands University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://its.nmhu.edu/IntranetUploads/008527-IPEDSCOSTI-1015202491955.pdf (sha256 2fec1be87a75)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 6, "rows": 42}
  - column:Undergraduate application fee: 0 ⟵ “Undergraduate application fee | 0 | 0”
  - column:Graduate application fee (not including Doctor's-Professional practice): 0 ⟵ “Graduate application fee (not including Doctor's-Professional practice) | 0 | 0”
  - column:Tuition: 4758 ⟵ “Tuition | 4,758 | 4,782 | 4,888 | 4,888”
  - column:Required fees: 2118 ⟵ “Required fees | 2,118 | 2,358 | 2,372 | 2,528”
  - column:Tuition + fees total: 6876 ⟵ “Tuition + fees total | 6,876 | 7,140 | 7,260 | 7,416”
  - column:Tuition (2): 4758 ⟵ “Tuition | 4,758 | 4,782 | 4,888 | 4,888”
  - column:Required fees (2): 2118 ⟵ “Required fees | 2,118 | 2,358 | 2,372 | 2,528”
  - column:Tuition + fees total (2): 6876 ⟵ “Tuition + fees total | 6,876 | 7,140 | 7,260 | 7,416”
  - column:Tuition (3): 9414 ⟵ “Tuition | 9,414 | 9,630 | 9,808 | 9,808”
  - column:Required fees (3): 2118 ⟵ “Required fees | 2,118 | 2,358 | 2,372 | 2,528”
  - column:Tuition + fees total (3): 11532 ⟵ “Tuition + fees total | 11,532 | 11,988 | 12,180 | 12,336”
  - column:Books and supplies: 1144 ⟵ “Books and supplies | 1,144 | 1,144 | 1,144 | 1,158”
  - column:Food and housing: 10352 ⟵ “Food and housing | 10,352 | 9,302 | 9,674 | 10,116”
  - column:Other expenses: 3968 ⟵ “Other expenses | 3,968 | 3,968 | 3,968 | 4,808”
  - column:Food and housing and other expenses total: 14320 ⟵ “Food and housing and other expenses total | 14,320 | 13,270 | 13,642 | 14,924”
  - column:Food and housing (2): 10352 ⟵ “Food and housing | 10,352 | 10,352 | 10,352 | 11,284”
  - column:Other expenses (2): 3968 ⟵ “Other expenses | 3,968 | 3,968 | 3,968 | 4,808”
  - column:Food and housing and other expenses total (2): 14320 ⟵ “Food and housing and other expenses total | 14,320 | 14,320 | 14,320 | 16,092”
  - column:Food and housing (3): 3836 ⟵ “Food and housing | 3,836”
  - column:Other expenses (3): 3968 ⟵ “Other expenses | 3,968 | 3,968 | 3,968 | 4,808”
  - column:Food and housing and other expenses total (3): 3968 ⟵ “Food and housing and other expenses total | 3,968 | 3,968 | 3,968 | 8,644”
  - column:Tuition (4): 4888 ⟵ “Tuition | 4,888 | 4,888 | 4,888 | 4,888 | 9,808 | 9,808”
  - column:Required fees (4): 2528 ⟵ “Required fees | 2,528 | 2,372 | 2,528 | 2,372 | 2,528 | 2,372”
  - column:Required fees (5): 92 ⟵ “Required fees | 92 | 92 | 92”
  - column:Tuition (5): 5488 ⟵ “Tuition | 5,488 | 5,488 | 5,488 | 5,488 | 10,264 | 10,264”
  - … 127 more rows
### `8676b98bcc694585` New Mexico Highlands University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://its.nmhu.edu/IntranetUploads/009048-2025-26Cost-42202684541.pdf (sha256 f006142c24b9)
- issues: ambiguous_year_labels, arrangement_unlabeled, components_do_not_reconcile, implausible_amount, residency_unknown
- checks: {"columns": 6, "components_reconcile": false, "rows": 59}
  - column:Undergraduate application fee: 25 ⟵ “Undergraduate application fee | 25 | 0”
  - column:Graduate application fee (not including Doctor's-Professional practice): 60 ⟵ “Graduate application fee (not including Doctor's-Professional practice) | 60 | 0”
  - column:Tuition: 4782 ⟵ “Tuition | 4,782 | 4,888 | 4,888 | 4,888”
  - column:Required fees: 2358 ⟵ “Required fees | 2,358 | 2,372 | 2,528 | 2,393”
  - column:Tuition + fees total: 7140 ⟵ “Tuition + fees total | 7,140 | 7,260 | 7,416 | 7,281”
  - column:Tuition (2): 4782 ⟵ “Tuition | 4,782 | 4,888 | 4,888 | 4,888”
  - column:Required fees (2): 2358 ⟵ “Required fees | 2,358 | 2,372 | 2,528 | 2,393”
  - column:Tuition + fees total (2): 7140 ⟵ “Tuition + fees total | 7,140 | 7,260 | 7,416 | 7,281”
  - column:Tuition (3): 9630 ⟵ “Tuition | 9,630 | 9,808 | 9,808 | 9,808”
  - column:Required fees (3): 2358 ⟵ “Required fees | 2,358 | 2,372 | 2,528 | 2,393”
  - column:Tuition + fees total (3): 11988 ⟵ “Tuition + fees total | 11,988 | 12,180 | 12,336 | 12,201”
  - column:Books and supplies: 1144 ⟵ “Books and supplies | 1,144 | 1,144 | 1,158 | 1,158”
  - column:Food and housing: 9302 ⟵ “Food and housing | 9,302 | 9,674 | 10,116 | 11,284”
  - column:Other expenses: 3968 ⟵ “Other expenses | 3,968 | 3,968 | 4,808 | 4,808”
  - column:Food and housing and other expenses total: 13270 ⟵ “Food and housing and other expenses total | 13,270 | 13,642 | 14,924 | 16,092”
  - column:Food and housing (2): 10352 ⟵ “Food and housing | 10,352 | 10,352 | 11,284 | 11,284”
  - column:Other expenses (2): 3968 ⟵ “Other expenses | 3,968 | 3,968 | 4,808 | 4,808”
  - column:Food and housing and other expenses total (2): 14320 ⟵ “Food and housing and other expenses total | 14,320 | 14,320 | 16,092 | 16,092”
  - column:Food and housing (3): 3836 ⟵ “Food and housing | 3,836 | 3,836”
  - column:Other expenses (3): 3968 ⟵ “Other expenses | 3,968 | 3,968 | 4,808 | 4,808”
  - column:Food and housing and other expenses total (3): 3968 ⟵ “Food and housing and other expenses total | 3,968 | 3,968 | 8,644 | 8,644”
  - column:Tuition (4): 4888 ⟵ “Tuition | 4,888 | 4,888 | 4,888 | 4,888 | 9,808 | 9,808”
  - column:Required fees (4): 2393 ⟵ “Required fees | 2,393 | 2,528 | 2,393 | 2,528 | 2,393 | 2,528”
  - column:Required fees (5): 100 ⟵ “Required fees | 100 | 92 | 100 | 92 | 100 | 92”
  - column:Tuition (5): 5488 ⟵ “Tuition | 5,488 | 5,488 | 5,488 | 5,488 | 10,264 | 10,264”
  - … 386 more rows
### `a7a92a741d98fa9d` New Mexico Highlands University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://its.nmhu.edu/IntranetUploads/004768-FY16-17Budg-727201793105.pdf (sha256 2b7d4cab4e20)
- issues: ambiguous_year_labels, arrangement_unlabeled, implausible_amount, multiple_total_rows
- checks: {"columns": 13, "rows": 4127}
  - column:undergraduate: 1975.0 ⟵ “undergraduate | $1,975.00 | $3,950.00 | $724.20 | $1,448.40 | $2,699.20 | $5,398.40”
  - column:graduate: 2209.2 ⟵ “graduate | $2,209.20 | $4,418.40 | $724.20 | $1,448.40 | $2,933.40 | $5,866.80”
  - column:professional (UNM only): 0.0 ⟵ “professional (UNM only) | $0.00 | $0.00 | $0.00 | $0.00”
  - column:undergraduate (2): 3525.84 ⟵ “undergraduate | $3,525.84 | $7,051 .68 | I”
  - column:graduate (2): 3775.8 ⟵ “graduate | $3,775.80 | $7,551 .60 | $724.20 | $1,448.40 | $4,500.00 | $9,000.00”
  - column:professional (UNM only) (2): 0.0 ⟵ “professional (UNM only) | $0.00 | $0.00 | $0.00 | $0.00”
  - column:undergraduate (3): 165.65 ⟵ “undergraduate | $165.65 | $331.30 | $60.35 | $120.70 | $226.00 | $452.00”
  - column:graduate (3): 184.1 ⟵ “graduate | $184.10 | $368.20 | $60.35 | $120.70 | $244.45 | $488.90”
  - column:professional (UNM only) (3): 0.0 ⟵ “professional (UNM only) | $0.00 | $0.00 | $0.00 | $0.00”
  - column:undergraduate (4): 293.82 ⟵ “undergraduate | $293.82 | $587.64 | $60.35 | $120.70 | $354.17 | $708.34”
  - column:graduate (4): 314.65 ⟵ “graduate | $314.65 | $629.30 | $60.35 | $120.70 | $375.00 | $750.00”
  - column:professional (UNM only) (4): 0.0 ⟵ “professional (UNM only) | $0.00 | $0.00 | $0.00 | $0.00”
  - column:Room: 1496.82 ⟵ “Room | $1,496.82 | $3,003.90”
  - column:Total BR&R Transfer Amount: 1162527 ⟵ “Total BR&R Transfer Amount | $1,162,527 | $1,162,527”
  - column:less amount retained in l&G for l&G purposes (enter as negative): 0 ⟵ “less amount retained in l&G for l&G purposes (enter as negative) | $0 | $0”
  - column:lnsb'uction: 10 ⟵ “lnsb'uction | 10 | $0 | $0”
  - column:Academic Support: 11 ⟵ “Academic Support | 11 | $0 | $0”
  - column:Student Services: 12 ⟵ “Student Services | 12 | $0 | $0”
  - column:Institutional Support: 13 ⟵ “Institutional Support | 13”
  - column:I: 0 ⟵ “I | $0 | $0”
  - column:Operation & Maintenance of Plant: 14 ⟵ “Operation & Maintenance of Plant | 14 | $1, 162,527 / | $1 ,162.527,”
  - column:TOTAL BR&R: 1162527 ⟵ “TOTAL BR&R | $1,162,527 | $1,162,527”
  - column:Instruction: 10 ⟵ “Instruction | 10 | $371422 | $37,442”
  - column:Academic Support (2): 11 ⟵ “Academic Support | 11 | $3,400 | $6,000”
  - column:Student Services (2): 12 ⟵ “Student Services | 12 | $350 | $350”
  - … 30991 more rows
### `ad732f870bcf8c9b` New Mexico Highlands University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://its.nmhu.edu/IntranetUploads/008850-2025-2026IP-10142025112922.pdf (sha256 128dc9915c4e)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 6, "rows": 42}
  - column:Undergraduate application fee: 25 ⟵ “Undergraduate application fee | 25 | 0”
  - column:Graduate application fee (not including Doctor's-Professional practice): 60 ⟵ “Graduate application fee (not including Doctor's-Professional practice) | 60 | 0”
  - column:Tuition: 4782 ⟵ “Tuition | 4,782 | 4,888 | 4,888 | 4,888”
  - column:Required fees: 2358 ⟵ “Required fees | 2,358 | 2,372 | 2,528 | 2,393”
  - column:Tuition + fees total: 7140 ⟵ “Tuition + fees total | 7,140 | 7,260 | 7,416 | 7,281”
  - column:Tuition (2): 4782 ⟵ “Tuition | 4,782 | 4,888 | 4,888 | 4,888”
  - column:Required fees (2): 2358 ⟵ “Required fees | 2,358 | 2,372 | 2,528 | 2,393”
  - column:Tuition + fees total (2): 7140 ⟵ “Tuition + fees total | 7,140 | 7,260 | 7,416 | 7,281”
  - column:Tuition (3): 9630 ⟵ “Tuition | 9,630 | 9,808 | 9,808 | 9,808”
  - column:Required fees (3): 2358 ⟵ “Required fees | 2,358 | 2,372 | 2,528 | 2,393”
  - column:Tuition + fees total (3): 11988 ⟵ “Tuition + fees total | 11,988 | 12,180 | 12,336 | 12,201”
  - column:Books and supplies: 1144 ⟵ “Books and supplies | 1,144 | 1,144 | 1,158 | 1,158”
  - column:Food and housing: 9302 ⟵ “Food and housing | 9,302 | 9,674 | 10,116 | 11,284”
  - column:Other expenses: 3968 ⟵ “Other expenses | 3,968 | 3,968 | 4,808 | 4,808”
  - column:Food and housing and other expenses total: 13270 ⟵ “Food and housing and other expenses total | 13,270 | 13,642 | 14,924 | 16,092”
  - column:Food and housing (2): 10352 ⟵ “Food and housing | 10,352 | 10,352 | 11,284 | 11,284”
  - column:Other expenses (2): 3968 ⟵ “Other expenses | 3,968 | 3,968 | 4,808 | 4,808”
  - column:Food and housing and other expenses total (2): 14320 ⟵ “Food and housing and other expenses total | 14,320 | 14,320 | 16,092 | 16,092”
  - column:Food and housing (3): 3836 ⟵ “Food and housing | 3,836 | 3,836”
  - column:Other expenses (3): 3968 ⟵ “Other expenses | 3,968 | 3,968 | 4,808 | 4,808”
  - column:Food and housing and other expenses total (3): 3968 ⟵ “Food and housing and other expenses total | 3,968 | 3,968 | 8,644 | 8,644”
  - column:Tuition (4): 4888 ⟵ “Tuition | 4,888 | 4,888 | 4,888 | 4,888 | 9,808 | 9,808”
  - column:Required fees (4): 2393 ⟵ “Required fees | 2,393 | 2,528 | 2,393 | 2,528 | 2,393 | 2,528”
  - column:Required fees (5): 100 ⟵ “Required fees | 100 | 92 | 100 | 92 | 100 | 92”
  - column:Tuition (5): 5488 ⟵ “Tuition | 5,488 | 5,488 | 5,488 | 5,488 | 10,264 | 10,264”
  - … 135 more rows
### `0cffe7e195d70309` New Mexico Institute of Mining and Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nmt.edu/finaid/docs/SCHOLARSHIP_CONDITIONS_AND_REQUIREMENTS_2025.pdf (sha256 024324485021)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If you have received the Lottery Scholarship and do not meet the requirements you will also lose the NM Opportunity Scholarship. 4) Appeals will not be accepted for failure to meet first semester requirements.”
### `10b89b0d1ec1f231` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 725c0b41b534)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: Pays tuition Awarded beginning with second semester of enrollment. Renewable, for a maximum of seven (7) semesters and three (3) summer semesters ⟵ “New Mexico Legislative Lottery Scholarship | None | Pays tuition Awarded beginning with second semester of enrollment. Renewable, for a maximum of seven (7) semesters and three (3) summer semesters | Must be a NM resident who has graduated from an NM high school or completed the NM GED/HiSET within ”
  - eligibility_summary: Must be a NM resident who has graduated from an NM high school or completed the NM GED/HiSET within 16 months of enrolling at NMT ⟵ “New Mexico Legislative Lottery Scholarship | None | Pays tuition Awarded beginning with second semester of enrollment. Renewable, for a maximum of seven (7) semesters and three (3) summer semesters | Must be a NM resident who has graduated from an NM high school or completed the NM GED/HiSET within ”
### `611da0348516099f` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 725c0b41b534)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - eligibility_summary: Students in the Scholarship for Service Program can be supported for up to three years (2 years for BS or MS, 2 years for BS + MS or for PhD) ⟵ “CyberCorps Scholarship | Contact the Computer Science Department for more information |  | Students in the Scholarship for Service Program can be supported for up to three years (2 years for BS or MS, 2 years for BS + MS or for PhD)”
### `8e87226064b3e3eb` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 0f135bf8b231)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $6,000/year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) ⟵ “Presidential Scholarship | March 1st for best consideration | $6,000/year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) | National Merit Finalist Certificate and high school GPA of 3.5”
  - eligibility_summary: National Merit Finalist Certificate and high school GPA of 3.5 ⟵ “Presidential Scholarship | March 1st for best consideration | $6,000/year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) | National Merit Finalist Certificate and high school GPA of 3.5”
### `95f9e9a6797c3c17` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 725c0b41b534)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: Up to $15,000 ⟵ “William D. Henderson Ethics Challenge Scholarship | 3/31/2027 | Up to $15,000 | -Full-time undergraduate enrollment -24 credits that apply toward an NMT degree by the end of the spring semester -Must have at least four semesters remaining in program -Cumulative GPA of 2.5 or higher from NMT -Financi”
  - eligibility_summary: -Full-time undergraduate enrollment -24 credits that apply toward an NMT degree by the end of the spring semester -Must have at least four semesters remaining in program -Cumulative GPA of 2.5 or higher from NMT -Financial need as determined by 2023-2024 FAFSA results -Must be a US citizen ⟵ “William D. Henderson Ethics Challenge Scholarship | 3/31/2027 | Up to $15,000 | -Full-time undergraduate enrollment -24 credits that apply toward an NMT degree by the end of the spring semester -Must have at least four semesters remaining in program -Cumulative GPA of 2.5 or higher from NMT -Financi”
### `dbf97c8da96f1079` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 0f135bf8b231)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $4,000 per year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) ⟵ “Silver Scholarship | March 1st for best consideration | $4,000 per year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) | High School GPA of 3.25 and ACT 27 or SAT 1260”
  - eligibility_summary: High School GPA of 3.25 and ACT 27 or SAT 1260 ⟵ “Silver Scholarship | March 1st for best consideration | $4,000 per year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) | High School GPA of 3.25 and ACT 27 or SAT 1260”
### `e1dce8c843ae18ee` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 0f135bf8b231)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: One-time $750 award ⟵ “NM MESA Scholarship | Contact Financial Aid Office | One-time $750 award | -Verification of participation in NM MESA program Please click here for more information about the NM MESA program.”
  - eligibility_summary: -Verification of participation in NM MESA program Please click here for more information about the NM MESA program. ⟵ “NM MESA Scholarship | Contact Financial Aid Office | One-time $750 award | -Verification of participation in NM MESA program Please click here for more information about the NM MESA program.”
### `e91da1d84f56804e` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 0f135bf8b231)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Kay and Elise Brower Music Scholarship | 8/17/2026 | $500 | -All applicants are required to submit a short YouTube video performance demonstrating their musical ability.”
  - eligibility_summary: -All applicants are required to submit a short YouTube video performance demonstrating their musical ability. ⟵ “Kay and Elise Brower Music Scholarship | 8/17/2026 | $500 | -All applicants are required to submit a short YouTube video performance demonstrating their musical ability.”
### `ee630a16d53628c9` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 0f135bf8b231)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: Covers any gap in tuition and and allowable fees owed by a student after other forms of state aid, such as the NM Lottery Scholarship are applied. Can cover up to 100% of tuition and allowable fees ⟵ “New Mexico Opportunity Scholarship | None | Covers any gap in tuition and and allowable fees owed by a student after other forms of state aid, such as the NM Lottery Scholarship are applied. Can cover up to 100% of tuition and allowable fees | Must be a NM resident”
  - eligibility_summary: Must be a NM resident ⟵ “New Mexico Opportunity Scholarship | None | Covers any gap in tuition and and allowable fees owed by a student after other forms of state aid, such as the NM Lottery Scholarship are applied. Can cover up to 100% of tuition and allowable fees | Must be a NM resident”
### `f31e0abb169d1ddf` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 0f135bf8b231)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $5,000 per year, renewable for a maximum of 4 academic years (8 academic semesters, excluding summer semesters) ⟵ “Gold Scholarship | March 1st for best consideration | $5,000 per year, renewable for a maximum of 4 academic years (8 academic semesters, excluding summer semesters) | High school GPA of 3.5 and ACT 30 or SAT 1360”
  - eligibility_summary: High school GPA of 3.5 and ACT 30 or SAT 1360 ⟵ “Gold Scholarship | March 1st for best consideration | $5,000 per year, renewable for a maximum of 4 academic years (8 academic semesters, excluding summer semesters) | High school GPA of 3.5 and ACT 30 or SAT 1360”
### `fd9d206118ca744a` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 725c0b41b534)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $2,000 per year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) ⟵ “Copper Scholarship | March 1st for best consideration | $2,000 per year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) | High School GPA of 3.0 and ACT 23 or SAT 1130”
  - eligibility_summary: High School GPA of 3.0 and ACT 23 or SAT 1130 ⟵ “Copper Scholarship | March 1st for best consideration | $2,000 per year, renewable for a maximum of four (4) academic years (Eight (8) academic semesters, excluding summer semesters) | High School GPA of 3.0 and ACT 23 or SAT 1130”
### `ff1ebf7440d729c8` New Mexico Institute of Mining and Technology — awards 2023-24 [new] (labeled_in_source)
- source: https://www.nmt.edu/finaid/scholarships.php (sha256 725c0b41b534)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: up to $10,000 per year for up to 4 years ⟵ “S-STEM Scholarship for New Freshman students Computer Science and Information Technology Majors |  | up to $10,000 per year for up to 4 years | -U.S. citizen or permanent resident -Enrolled full time in the first two years of a bachelor's degree program -Study and do research in some areas of comput”
  - eligibility_summary: -U.S. citizen or permanent resident -Enrolled full time in the first two years of a bachelor's degree program -Study and do research in some areas of computer science and information technology with a focus on cybersecurity -High school GPA of at least 3.6 (from transcripts), or ranked in the top 15% of graduating high school class -Maintain at least a minimum GPA of 3.0 -Demonstrated Financial need as determined by FAFSA ⟵ “S-STEM Scholarship for New Freshman students Computer Science and Information Technology Majors |  | up to $10,000 per year for up to 4 years | -U.S. citizen or permanent resident -Enrolled full time in the first two years of a bachelor's degree program -Study and do research in some areas of comput”
### `2a4ca7a9f87b7a11` New Mexico Junior College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.nmjc.edu/admission/financial_aid/2026-2027%20Special%20Circumstances%20Form.pdf (sha256 efb42c530c9a)
- issues: semantic_review_required, conflicting_sources:https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf,https://www.nmjc.edu/admission/financial_aid/professional_judgment.aspx
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “2026-2027 Special Circumstances Form This form is for use by students whose family financial status has significantly changed compared to 2024 income tax information.”
  - sentence: need_based_special_circumstances ⟵ “Other Please indicate who the change in income is for: Parent (for dependent students) ____Student Spouse Note: Your request will not be considered until we have received the results of your 2026-2027 FAFSA and 2024 Verification of income has been completed (if applicable).”
  - sentence: need_based_special_circumstances ⟵ “This Special Circumstance form and all required documentation must be submitted to the financial aid office before this form will be reviewed.”
  - sentence: need_based_special_circumstances ⟵ “Submission of this form does not guarantee a change in your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances reviews will not be considered until all supporting documentation is received and all documentation must be current. ___________________________________________ _________________________________ Student’s name NMJC Student ID or SS# ___________________________________________ _________________________________ Parent’s names (only for dependent students) Phone Number _________”
  - sentence: need_based_special_circumstances ⟵ “I also realize that if I do not submit all requested documents, the Special Circumstance will not be reviewed. _____________________________________________________________________ Student’s signature Date ___________________________________________________________________________ Parent signature (if referenced on this form) Date Page 2 of 2”
### `2bd84bd158b590bc` New Mexico Junior College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf (sha256 d85639c5cd2d)
- issues: semantic_review_required, conflicting_sources:https://catalog.nmjc.edu/20262027-financial-aid-satisfactory-academic-progress-policy
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress, Evaluating SAP, Appeal Process XVII.”
  - sentence: sap_appeal ⟵ “A warning letter explains the student has one semester of eligibility on warning status but must meet Title IV eligibility by the end of their next term of enrollment. 33 Financial Aid Probation If a student successfully files a SAP appeal, the student will be placed on financial aid probation for one payment period (semester).”
  - sentence: sap_appeal ⟵ “The appeal and supporting documentation are submitted to the Financial Aid Office electronically using the Satisfactory Academic Progress Appeal Form.”
### `4eb40a7fca339ff3` New Mexico Junior College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nmjc.edu/admission/financial_aid/professional_judgment.aspx (sha256 9185d81e32b8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Cost of Attendance adjustment requests may be submitted by contacting the Director of Financial Aid, Kerrie Mitchell, kmitchell@nmjc.edu or 575-492-2560.”
  - sentence: budget_increase ⟵ “Cost of attendance adjustments can include Dependent Care expenses, Disability related expenses, Professional Licensure, Certification, etc.”
### `57e1ea6e3698e5b7` New Mexico Junior College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf (sha256 d85639c5cd2d)
- issues: semantic_review_required, conflicting_sources:https://www.nmjc.edu/admission/financial_aid/professional_judgment.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Aid administrators will then make a final determination, based on supporting documentation, whether the student should receive a dependency override.”
### `64612e0b9ff5f6d5` New Mexico Junior College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nmjc.edu/admission/financial_aid/professional_judgment.aspx (sha256 9185d81e32b8)
- issues: semantic_review_required, conflicting_sources:https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “All Professional Judgement requests will be reviewed and considered.”
  - sentence: professional_judgment ⟵ “Cost of Attendance adjustments are not professional judgement and will be made if documentation warrants the need for adjustment.”
### `92d219aface9c150` New Mexico Junior College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nmjc.edu/admission/financial_aid/professional_judgment.aspx (sha256 9185d81e32b8)
- issues: semantic_review_required, conflicting_sources:https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “This is commonly referred to as a dependency override.”
### `c564829abe6df176` New Mexico Junior College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf (sha256 d85639c5cd2d)
- issues: semantic_review_required, conflicting_sources:https://www.nmjc.edu/admission/financial_aid/2026-2027%20Special%20Circumstances%20Form.pdf,https://www.nmjc.edu/admission/financial_aid/professional_judgment.aspx
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: need_based_special_circumstances ⟵ “Students that submit special circumstance requests for income adjustments or dependency overrides may be selected for verification.”
  - sentence: need_based_special_circumstances ⟵ “COST OF ATTENDANCE, PROFESSIONALJUDGMENT/SPECIAL CIRCUMSTANCES Cost of Attendance (Budgets) Cost of attendance (COA) is determined by law (Higher Education Act, Sec. 472) and is not subject to regulation by the Department.”
  - sentence: need_based_special_circumstances ⟵ “The reason for adjustment must be documented in the student’s file, and it must relate to that student’s special circumstances that differentiate the individual student (not to conditions that exist for a whole class of students).”
  - sentence: need_based_special_circumstances ⟵ “Students may apply for special circumstance adjustment by submitting the Special Circumstances Form and all required supporting documentation.”
  - sentence: need_based_special_circumstances ⟵ “The Director of Financial Aid reviews all Special Circumstance forms and supporting documentation.”
  - sentence: need_based_special_circumstances ⟵ “Verification of the student’s FAFSA may be required before Special Circumstances adjustments can be made.”
### `e0ec8bc2f6b80cf8` New Mexico Junior College — appeals 2024-25 [new] (labeled_in_source)
- source: https://catalog.nmjc.edu/academic-standing (sha256 2e3389bb7fe0)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Academic Suspension Appeals A student who has been placed on academic suspension may submit a written appeal to the Vice President for Student Services or appointed representative explaining the unusual circumstances (along with supporting documentation) as to why they should be readmitted without serving the suspension.”
### `ea10aa092c588fd7` New Mexico Junior College — appeals 2026-27 [new] (labeled_in_title)
- source: https://catalog.nmjc.edu/20262027-financial-aid-satisfactory-academic-progress-policy (sha256 be3b3b5bf263)
- issues: semantic_review_required, conflicting_sources:https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “To appeal the financial aid suspension, a student must submit to the Director of Financial Aid a signed and dated SAP Suspension Appeal Form explaining why the student was not academically successful, what has changed that will now allow the student to be academically successful, and any supporting documentation from an objective third party professional (e.g. physician, counselor, lawyer, social ”
### `ee199e7c9c417a47` New Mexico Junior College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nmjc.edu/admission/financial_aid/professional_judgment.aspx (sha256 9185d81e32b8)
- issues: semantic_review_required, conflicting_sources:https://www.nmjc.edu/admission/financial_aid/2026-2027%20Special%20Circumstances%20Form.pdf,https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refers to a significant change in the student and/or parent’s financial situation (loss of employment, death, child care expenses, disability related expenses, etc.) that justify adjustment to the students FAFSA or Cost of Attendance (COA).”
  - sentence: need_based_special_circumstances ⟵ “To request a review of the special circumstance please complete and submit the Special Circumstance Form.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refers to conditions that justify an adjustment to a student’s dependency status (required to submit parent information on the FAFSA) based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abandonment, incarceration).”
  - sentence: need_based_special_circumstances ⟵ “If you have unusual circumstances that prevent you from being able to provide parent information on your FAFSA, please contact the Director of Financial Aid, Kerrie Mitchell, kmitchell@nmjc.edu or 575-492-2560 to discuss your situation.”
### `fdcc8bf8c8f362aa` New Mexico Junior College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nmjc.edu/admission/financial_aid/Fin%20Aid%20Policies%20and%20Procedures%2026-27.pdf (sha256 d85639c5cd2d)
- issues: semantic_review_required, conflicting_sources:https://www.nmjc.edu/admission/financial_aid/professional_judgment.aspx
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “Cost of Attendance and Professional Judgment/Special Circumstance 1 Dependency Status XIII.”
  - sentence: professional_judgment ⟵ “Professional Judgment Financial aid administrators may use professional judgment on a case-by-case basis to change a dependent student’s status to independent, or to increase or decrease one or more of the data elements used to calculate the student aid index (SAI) or the COA budget.”
  - sentence: professional_judgment ⟵ “Professional judgment can also be used to adjust the student’s cost of attendance.”
  - sentence: professional_judgment ⟵ “If conditions such as these apply, students may apply for a special circumstance/professional judgment adjustment. 23 Examples of special circumstances may include: ➢ Private school tuition for siblings of dependent students or dependent children of an independent student; ➢ College tuition cost for parents of a dependent student or spouse of an independent student; ➢ Unusual medical or dental exp”
  - sentence: professional_judgment ⟵ “Professional judgment cannot be used to waive general student eligibility requirements or to circumvent the intent of the law or regulations.”
  - sentence: professional_judgment ⟵ “The Director of Financial Aid reviews all dependency appeals and the student is notified via email regarding the decision. 24 The decision is based on professional judgment and cannot be appealed to the U.S.”
### `997d651da82da4e1` New Mexico Junior College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nmjc.edu/admission/paying_for_college/documents/25-26%20Primary%20Cost%20of%20Attendance%20Budgets%20-%20Full%20Time%20-%20Fall%20Spring.pdf (sha256 e57954e271cd)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 7, "rows": 3}
  - column:$: 18403.0 ⟵ “$ | 18,403.00 | $ | 19,003.00 | $ 19,453.00”
  - column:$ (2): 16432.0 ⟵ “$ | 16,432.00 | $ | 17,032.00 | $ 17,482.00”
  - column:$ (3): 21340.0 ⟵ “$ | 21,340.00 | $ | 21,940.00 | $ 22,390.00”
  - column:Books and Supplies: 1200.0 ⟵ “Books and Supplies | $ | 1,200.00 | Books and Supplies | $ | 1,200.00 | Books and Supplies | $ 1,200.00”
  - column:Fees: 760.0 ⟵ “Fees | $ | 760.00 | Fees | $ | 760.00 | Fees | $ | 760.00”
  - column:Food & Housing-Living Expenses: 6880.0 ⟵ “Food & Housing-Living Expenses | $ | 6,880.00 | Food & Housing-Living Expenses | $ | 6,880.00 | Food & Housing-Living Expenses | $ 6,880.00”
  - column:Personal Expenses: 6363.0 ⟵ “Personal Expenses | $ | 6,363.00 | Personal Expenses | $ | 6,363.00 | Personal Expenses | $ 6,363.00”
  - column:Tuition: 1200.0 ⟵ “Tuition | $ | 1,200.00 | Tuition | $ | 1,800.00 | Tuition | $ 2,250.00”
  - column:Transportation: 2000.0 ⟵ “Transportation | $ | 2,000.00 | Transportation | $ | 2,000.00 | Transportation | $ 2,000.00”
  - column:Books and Supplies (2): 1200.0 ⟵ “Books and Supplies | $ | 1,200.00 | Books and Supplies | $ | 1,200.00 | Books and Supplies | $ 1,200.00”
  - column:Fees (2): 760.0 ⟵ “Fees | $ | 760.00 | Fees | $ | 760.00 | Fees | $ | 760.00”
  - column:Food & Housing-Living Expenses (2): 4909.0 ⟵ “Food & Housing-Living Expenses | $ | 4,909.00 | Food & Housing-Living Expenses | $ | 4,909.00 | Food & Housing-Living Expenses | $ 4,909.00”
  - column:Personal Expenses (2): 6363.0 ⟵ “Personal Expenses | $ | 6,363.00 | Personal Expenses | $ | 6,363.00 | Personal Expenses | $ 6,363.00”
  - column:Tuition (2): 1200.0 ⟵ “Tuition | $ | 1,200.00 | Tuition | $ | 1,800.00 | Tuition | $ 2,250.00”
  - column:Transportation (2): 2000.0 ⟵ “Transportation | $ | 2,000.00 | Transportation | $ | 2,000.00 | Transportation | $ 2,000.00”
  - column:Books and Supplies (3): 1200.0 ⟵ “Books and Supplies | $ | 1,200.00 | Books and Supplies | $ | 1,200.00 | Books and Supplies | $ 1,200.00”
  - column:Fees (3): 760.0 ⟵ “Fees | $ | 760.00 | Fees | $ | 760.00 | Fees | $ | 760.00”
  - column:Food & Housing-Living Expenses (3): 9817.0 ⟵ “Food & Housing-Living Expenses | $ | 9,817.00 | Food & Housing-Living Expenses | $ | 9,817.00 | Food & Housing-Living Expenses | $ 9,817.00”
  - column:Personal Expenses (3): 6363.0 ⟵ “Personal Expenses | $ | 6,363.00 | Personal Expenses | $ | 6,363.00 | Personal Expenses | $ 6,363.00”
  - column:Tuition (3): 1200.0 ⟵ “Tuition | $ | 1,200.00 | Tuition | $ | 1,800.00 | Tuition | $ 2,250.00”
  - column:Transportation (3): 2000.0 ⟵ “Transportation | $ | 2,000.00 | Transportation | $ | 2,000.00 | Transportation | $ 2,000.00”
  - column:$: 19003.0 ⟵ “$ | 18,403.00 | $ | 19,003.00 | $ 19,453.00”
  - column:$ (2): 17032.0 ⟵ “$ | 16,432.00 | $ | 17,032.00 | $ 17,482.00”
  - column:$ (3): 21940.0 ⟵ “$ | 21,340.00 | $ | 21,940.00 | $ 22,390.00”
  - column:$: 19453.0 ⟵ “$ | 18,403.00 | $ | 19,003.00 | $ 19,453.00”
  - … 38 more rows
### `1273370c0ded9234` New Mexico Junior College — credit_policies 2024-25 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.nmjc.edu/ap-and-clep-credit (sha256 efab48aadcb9)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 1, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History | 4 or 5 | ARTH 2110 History of Art I and ARTH 2120 History of Art II | 6”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | BIOL 2120C - Cellular & Molecular Biology or BIOL 2110C | 4”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History | 4 or 5 | MATH 1510 - Calculus I | 3”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | MATH 1510 - Calculus I and MATH 1520 Calculus II^ | 6”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “Art History | 5 | MATH 1510 - Calculus I and MATH 1520 Calculus II | 6”
  - equivalencies[AP-ART-HISTORY|*Calculus I only if Calculus AB subscore of a 4]:  ⟵ “Art History | *Calculus I only if Calculus AB subscore of a 4”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | CHEM 1215C - General Chemistry I | 4”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “Art History | 5 | CHEM 1215C - General Chemistry I and CHEM 1225C - General Chemistry II | 8”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History | 4 or 5 | CS 213J - JAVA Programming or Computer Science I and Object Oriented Programming | 3”
  - equivalencies[AP-ART-HISTORY|4 or 5]:  ⟵ “Art History | 4 or 5 | HIST 1150 - Western Civilization I and HIST 1160 - Western Civilization II | 6”
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | GRMN 1110 - German I and GRMN 1120 - German II | 6”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “Art History | 5 | GRMN 1110 - German I and GRMN 1120 - German II and GRMN 2110 - German III | 9”
### `4009f148807ef148` New Mexico Junior College — credit_policies 2024-25 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.nmjc.edu/ap-and-clep-credit (sha256 efab48aadcb9)
- issues: stale_year_label:2024-25
- checks: {"distinct_exams": 22, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | ENGL 1110 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL 2610 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL 2630 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 50 | HIST 1150 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II | 50 | HIST 1160 | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POLS 1120 | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 1220 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-calculus | 50 | MATH 1220 | 3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus w/ Elementary Functions | 50 | MATH 1510 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL 1101C | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM 1215C | 4”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psych. | 50 | PSYC 2390 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | 50 | PSYC 1110 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | PSYC 2120 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | 50 | SOCI 1110 | 3”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish or Spanish with Writing | 50 | SPAN 1110 | 4”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish or Spanish with Writing | 50 | SPAN 1120 | 4”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|63]:  ⟵ “Spanish or Spanish with Writing | 63 | SPAN 2110 | 4”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|63]:  ⟵ “Spanish or Spanish with Writing | 63 | SPAN 2120 | 4”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT 2110 | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of | 50 | MGMT 2110 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | 50 | MKTG 2110 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law, Introductory | 50 | BLAW 2110 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles | 50 | ECON 2110 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles | 50 | ECON 2120 | 3”
### `0c5c63ef0f29c9f5` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/lottery.html (sha256 09582766af09)
- issues: semantic_review_required, conflicting_sources:https://fa.nmsu.edu/scholarships/opportunity.html,https://fa.nmsu.edu/scholarships/scholarship-appeal-policy.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “Lost Lottery Scholarship Eligibility Appeals Students will automatically lose the Lottery Scholarship if renewal requirements are not met.”
  - sentence: scholarship_retention_appeal ⟵ “Every student has the right to appeal the loss of eligibility for the scholarship, if and when the loss occurred because there was an exceptional mitigating circumstance that was beyond the student’s control.”
### `16f36061d4b77fb4` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/scholarship-appeal-policy.html (sha256 dfa2b24d6c16)
- issues: semantic_review_required, conflicting_sources:https://fa.nmsu.edu/scholarships/lottery.html,https://fa.nmsu.edu/scholarships/opportunity.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “Policy Grounds for Appeal Students who have been notified of their failure to meet scholarship renewal requirements and subsequently lose scholarship eligibility have the right to appeal this decision.”
  - sentence: scholarship_retention_appeal ⟵ “Reinstatement of NM Opportunity Scholarship Students who lose NM Opportunity Scholarship eligibility and are not approved for reinstatement through the appeal process may petition for reinstatement as a returning student no sooner than two years after the end of the semester in which eligibility was lost.”
### `3062c70f78da1b28` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/_files/SAPPolicy.pdf (sha256 f27c9fd5736b)
- issues: semantic_review_required, conflicting_sources:https://fa.nmsu.edu/sap/index.html,https://fa.nmsu.edu/sap/sap-appeal.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students that fall below the satisfactory academic progress requirements have the right to appeal their ineligibility for Financial Aid at NMSU on the basis of: personal injury or illness, the death of a relative, or other special circumstances.”
### `7402b61b24361b8c` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/sap/index.html (sha256 0946f90e517b)
- issues: semantic_review_required, conflicting_sources:https://fa.nmsu.edu/_files/SAPPolicy.pdf,https://fa.nmsu.edu/sap/sap-appeal.html
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Appeals Students that fall below the Satisfactory Academic Progress requirements, or the renewal requirements for their scholarships or Out-of-State Tuition Discounts, have the right to appeal their ineligibility for Federal Financial Aid.”
  - sentence: sap_appeal ⟵ “View NMSU’s Satisfactory Academic Progress Policy for more information on appeals.”
  - sentence: sap_appeal ⟵ “Financial Aid Appeal Form Satisfactory Academic Progress Policy Please submit appeals to your Financial Aid Advisor.”
  - sentence: sap_appeal ⟵ “SAP Appeal Policy University Financial Aid and Scholarship Services 575-646-4105 877-278-8586 financialaid@nmsu.edu Educational Services Center, Suite 600 Resources Student Aid Financial Aid Instruction Guide Consumer Information FERPA Problem Resolution Connect With Us Scroll to Top © 2024 New Mexico State University - Board of Regents”
### `811e1d5fb9bdc872` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/npc/index.html (sha256 33317c76f9e0)
- issues: semantic_review_required, conflicting_sources:https://fa.nmsu.edu/forms/pj.html,https://fa.nmsu.edu/forms/specialcircumstances.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The estimate you receive is subject to the accuracy of the information you provide, it may change if financial or family characteristics change, and does not incorporate any special circumstances, which are reviewed after you officially apply for aid.”
### `a4b7ccfe7054409d` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/opportunity.html (sha256 5c4389e0d8d5)
- issues: semantic_review_required, conflicting_sources:https://fa.nmsu.edu/scholarships/lottery.html,https://fa.nmsu.edu/scholarships/scholarship-appeal-policy.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “Lost Opportunity Scholarship Eligibility Appeals Students will automatically lose the Opportunity Scholarship if renewal requirements are not met.”
  - sentence: scholarship_retention_appeal ⟵ “Every student has the right to appeal the loss of eligibility for the scholarship, if and when the loss occurred because there was an exceptional mitigating circumstance that was beyond the student’s control.”
### `a660907ddbed1394` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/forms/pj.html (sha256 c894aeb434e4)
- issues: semantic_review_required, conflicting_sources:https://fa.nmsu.edu/forms/specialcircumstances.html,https://fa.nmsu.edu/npc/index.html
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “The Contribution Review allows students to document special circumstances not reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Additional information regarding Unusual Circumstances and Dependency Overrides can be found by clicking the button below.”
  - sentence: need_based_special_circumstances ⟵ “The Petition for Dependency Override allows students to document Unusual Circumstances not explained or reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Additional information regarding Unusual Circumstances and Dependency Overrides can be found by clicking the button below.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances University Financial Aid and Scholarship Services 575-646-4105 877-278-8586 financialaid@nmsu.edu Educational Services Center, Suite 600 Resources Student Aid Financial Aid Instruction Guide Consumer Information FERPA Problem Resolution Connect With Us Scroll to Top © 2024 New Mexico State University - Board of Regents”
### `e0113b3590c85c89` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/sap/sap-appeal.html (sha256 e41a762ac4da)
- issues: semantic_review_required, conflicting_sources:https://fa.nmsu.edu/_files/SAPPolicy.pdf,https://fa.nmsu.edu/sap/index.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeal Policy | New Mexico State University - BE BOLD.”
### `e5d84cb597889d18` New Mexico State University-Main Campus — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://fa.nmsu.edu/forms/specialcircumstances.html (sha256 98f82191a9d4)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://fa.nmsu.edu/forms/pj.html,https://fa.nmsu.edu/npc/index.html
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances | New Mexico State University - BE BOLD.”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid will review your file for consideration of special circumstances, or a Contribution Review.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances That May Qualify: Some examples include, but are not limited to: Change in income or job loss Financial Hardship Unusual family medical or dental expenses not covered by insurance Tuition cost for elementary/secondary school for student's siblings or dependents Extraordinary dependent care expenses Decrease or loss of child support Divorce of a dependent student’s parent or o”
  - sentence: need_based_special_circumstances ⟵ “Documentation may include (but is not limited to) the following: Contribution Review Form – Select the category that most closely relates to your Special Circumstance Provide Letter of Explanation detailing the circumstance indicated in the Contribution Review Form.”
  - sentence: need_based_special_circumstances ⟵ “Process The Contribution Review allows students to document special circumstances not reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Advisor will determine if adjustments to the student aid index (SAI) or cost of attendance (COA) are warranted due to special circumstances.”
### `f3b4ca1f9247da5a` New Mexico State University-Main Campus — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/forms/pj.html (sha256 c894aeb434e4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Section 479A of the Higher Education Act of 1965 (HEA), as amended, [20 USC 1087TT/tt], provides the authority for financial aid administrators to exercise Professional Judgment discretion in a number of areas when a student has special or unusual circumstances that may impact their financial need.”
  - sentence: professional_judgment ⟵ “When there are Special or Unusual Circumstances that impact your federal student aid eligibility, federal regulations give a financial aid administrator discretion to make professional judgments on a case-by-case basis and with adequate documentation, to make adjustments to specific data elements on the submitted Free Application for Federal Student Aid (FAFSA®) form, in order to gain a more accur”
  - sentence: professional_judgment ⟵ “NOTE: *Professional Judgments do not guarantee adjustments or additional aid.”
  - sentence: professional_judgment ⟵ “Special Circumstances - Contribution Review Financial Aid Administrators have to authority to use their Professional Judgement to determine if there are any Special Circumstances: If you or your family have encountered personal or financial hardships that were not accurately reflected at the time you filled out your FAFSA, Financial Aid specialists can review your file for consideration of special”
### `00541c48121a4384` New Mexico State University-Main Campus — awards 2026-27 [new] (labeled_in_source)
- source: https://fa.nmsu.edu/scholarships/index.html (sha256 99c41df1f2c2)
- issues: conflicting_sources:https://admissions.nmsu.edu/cost-and-aid/scholarships.html,https://fa.nmsu.edu/scholarships/
- checks: {"thresholds": null}
  - award_amount_text: $2,000 per academic year. ⟵ “1888 Leadership Scholarship | 3.5-3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year. M”
  - eligibility_summary: 3.5-3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “1888 Leadership Scholarship | 3.5-3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year. M”
  - renewal_requirements: 2.7 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester ⟵ “1888 Leadership Scholarship | 3.5-3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year. M”
### `0a5e6d783760175a` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.nmsu.edu/cost-and-aid/scholarships.html (sha256 0a8b542de58f)
- issues: conflicting_sources:https://fa.nmsu.edu/scholarships/,https://fa.nmsu.edu/scholarships/index.html
- checks: {"thresholds": null}
  - award_amount_text: $4,000 per academic year. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above . New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must e”
  - eligibility_summary: 3.9 GPA or Academic Index of 159 and above . New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above . New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must e”
  - renewal_requirements: 3.3 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above . New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must e”
### `255a77a12d7f98de` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.nmsu.edu/cost-and-aid/scholarships.html (sha256 0a8b542de58f)
- issues: conflicting_sources:https://fa.nmsu.edu/scholarships/,https://fa.nmsu.edu/scholarships/index.html
- checks: {"thresholds": null}
  - award_amount_text: $2,000 per academic year. ⟵ “1888 Leadership Scholarship | 3.5 – 3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year.”
  - eligibility_summary: 3.5 – 3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “1888 Leadership Scholarship | 3.5 – 3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year.”
  - renewal_requirements: 2.7 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester ⟵ “1888 Leadership Scholarship | 3.5 – 3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year.”
### `41b503593d9a8889` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.nmsu.edu/cost-and-aid/scholarships.html (sha256 0a8b542de58f)
- issues: conflicting_sources:https://fa.nmsu.edu/scholarships/,https://fa.nmsu.edu/scholarships/index.html
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per academic year. ⟵ “Crimson Success Scholarship | 3.7 – 3.89 GPA or Academic Index of 145 – 158.99 . New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year”
  - eligibility_summary: 3.7 – 3.89 GPA or Academic Index of 145 – 158.99 . New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “Crimson Success Scholarship | 3.7 – 3.89 GPA or Academic Index of 145 – 158.99 . New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year”
  - renewal_requirements: 3.0 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester ⟵ “Crimson Success Scholarship | 3.7 – 3.89 GPA or Academic Index of 145 – 158.99 . New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year”
### `5383671ea053b332` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/globalscholarships.html (sha256 d3841968f7e3)
- issues: conflicting_sources:https://admissions.nmsu.edu/cost-and-aid/scholarships.html
- checks: {"thresholds": null}
  - award_amount_text: Tuition and required fees. If the student already qualifies for a tuition-based award, for example, the NM Lottery Scholarship, the Opportunity Scholarship covers the remaining amount after those awards disburse ⟵ “NM Opportunity Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. Must have a 2.5 GPA or higher and enroll in 1”
  - eligibility_summary: New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. Must have a 2.5 GPA or higher and enroll in 15 credit hours. ⟵ “NM Opportunity Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. Must have a 2.5 GPA or higher and enroll in 1”
  - renewal_requirements: 2.5 cumulative GPA, Enroll in, & pass 12 credit hours per semester, Enroll in & pass 30 credit hours per academic year, For up to a maximum 160 attempted credit hours. ⟵ “NM Opportunity Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. Must have a 2.5 GPA or higher and enroll in 1”
### `7bcdd30d62298f8f` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.nmsu.edu/cost-and-aid/scholarships.html (sha256 0a8b542de58f)
- issues: duplicate_table_versions, conflicting_sources:https://fa.nmsu.edu/scholarships/globalscholarships.html
- checks: {"thresholds": null}
  - award_amount_text: Tuition and required fees . If the student qualifies for another tuition-based award or has received other state aid, the Opportunity Scholarship will cover the remaining amount. Tuition-based awards and state aid include, but are not limited to, the NM Lottery Scholarship, Teacher Preparation Affordability grant, the New Mexico Leveraging Educational Assistance Partnership Grant (LEAP) grant, and Workforce Innovation and Opportunity Act (WIOA). ⟵ “NM Opportunity Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED . Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. Must have a 2.5 GPA or higher and enroll in ”
  - eligibility_summary: New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED . Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. Must have a 2.5 GPA or higher and enroll in 12 credit hours. US Citizen or Permanent Resident. ⟵ “NM Opportunity Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED . Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. Must have a 2.5 GPA or higher and enroll in ”
  - renewal_requirements: Lottery Track 2.5 cumulative GPA. Enroll in and pass 12-18 credit hours per semester. Enroll in and pass 30 credit hours per academic year. For up to a maximum of 160 credit hours total. Returning Learner 2.5 cumulative GPA. Enroll in and pass 6-18 credit hours per semester. For up to a maximum of 160 credit hours total. ⟵ “NM Opportunity Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED . Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. Must have a 2.5 GPA or higher and enroll in ”
### `84498fb3396aa3e3` New Mexico State University-Main Campus — awards 2026-27 [new] (labeled_in_source)
- source: https://fa.nmsu.edu/scholarships/ (sha256 11ea09dc30cc)
- issues: conflicting_sources:https://admissions.nmsu.edu/cost-and-aid/scholarships.html,https://fa.nmsu.edu/scholarships/index.html
- checks: {"thresholds": null}
  - award_amount_text: $2,000 per academic year. ⟵ “1888 Leadership Scholarship | 3.5-3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year. M”
  - eligibility_summary: 3.5-3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “1888 Leadership Scholarship | 3.5-3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year. M”
  - renewal_requirements: 2.7 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester ⟵ “1888 Leadership Scholarship | 3.5-3.69 GPA or Academic Index of 133 – 144.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $2,000 per academic year. | 2.7 cumulative GPA and pass 30 new credits per academic year. M”
### `ad79006147665ebb` New Mexico State University-Main Campus — awards 2026-27 [new] (labeled_in_source)
- source: https://fa.nmsu.edu/scholarships/ (sha256 11ea09dc30cc)
- issues: conflicting_sources:https://admissions.nmsu.edu/cost-and-aid/scholarships.html,https://fa.nmsu.edu/scholarships/index.html
- checks: {"thresholds": null}
  - award_amount_text: $4,000 per academic year. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must en”
  - eligibility_summary: 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must en”
  - renewal_requirements: 3.3 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must en”
### `ba17d9aef3d508eb` New Mexico State University-Main Campus — awards 2026-27 [new] (labeled_in_source)
- source: https://fa.nmsu.edu/scholarships/ (sha256 11ea09dc30cc)
- issues: conflicting_sources:https://admissions.nmsu.edu/cost-and-aid/scholarships.html,https://fa.nmsu.edu/scholarships/index.html
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per academic year. ⟵ “Crimson Success Scholarship | 3.7-3.89 GPA or Academic Index of 145-158.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year. Mus”
  - eligibility_summary: 3.7-3.89 GPA or Academic Index of 145-158.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “Crimson Success Scholarship | 3.7-3.89 GPA or Academic Index of 145-158.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year. Mus”
  - renewal_requirements: 3.0 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ⟵ “Crimson Success Scholarship | 3.7-3.89 GPA or Academic Index of 145-158.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year. Mus”
### `c99660e58a467c1c` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://fa.nmsu.edu/scholarships/globalscholarships.html (sha256 d3841968f7e3)
- issues: conflicting_sources:https://admissions.nmsu.edu/cost-and-aid/scholarships.html
- checks: {"thresholds": null}
  - award_amount_text: Percentage of tuition. ⟵ “NM Lottery Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. First semester college GPA of 2.5 and pass 15 cred”
  - eligibility_summary: New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. First semester college GPA of 2.5 and pass 15 credits. ⟵ “NM Lottery Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. First semester college GPA of 2.5 and pass 15 cred”
  - renewal_requirements: 2.5 cumulative GPA, Enroll in, & pass 12 credit hours per semester, Enroll in & pass 30 credit hours per academic year, For a maximum of seven semesters total. ⟵ “NM Lottery Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. First semester college GPA of 2.5 and pass 15 cred”
### `ca71dd27d2c8d898` New Mexico State University-Main Campus — awards 2026-27 [new] (labeled_in_source)
- source: https://fa.nmsu.edu/scholarships/index.html (sha256 99c41df1f2c2)
- issues: conflicting_sources:https://admissions.nmsu.edu/cost-and-aid/scholarships.html,https://fa.nmsu.edu/scholarships/
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per academic year. ⟵ “Crimson Success Scholarship | 3.7-3.89 GPA or Academic Index of 145-158.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year. Mus”
  - eligibility_summary: 3.7-3.89 GPA or Academic Index of 145-158.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “Crimson Success Scholarship | 3.7-3.89 GPA or Academic Index of 145-158.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year. Mus”
  - renewal_requirements: 3.0 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ⟵ “Crimson Success Scholarship | 3.7-3.89 GPA or Academic Index of 145-158.99. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $3,000 per academic year. | 3.0 cumulative GPA and pass 30 new credits per academic year. Mus”
### `d2669ba389ca1de0` New Mexico State University-Main Campus — awards 2026-27 [new] (labeled_in_source)
- source: https://fa.nmsu.edu/scholarships/index.html (sha256 99c41df1f2c2)
- issues: conflicting_sources:https://admissions.nmsu.edu/cost-and-aid/scholarships.html,https://fa.nmsu.edu/scholarships/
- checks: {"thresholds": null}
  - award_amount_text: $4,000 per academic year. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must en”
  - eligibility_summary: 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must en”
  - renewal_requirements: 3.3 cumulative GPA and pass 30 new credits per academic year. Must enroll in, and attempt, 15 new Las Cruces campus credits per semester. ⟵ “Hadley Honors Scholarship | 3.9 GPA or Academic Index of 159 and above. New Mexico resident. High school diploma from a NM accredited school, a NM GED, or a NM-HiSET. US Citizen or Permanent Resident. | $4,000 per academic year. | 3.3 cumulative GPA and pass 30 new credits per academic year. Must en”
### `f2d8ef6193177659` New Mexico State University-Main Campus — awards 2026-27 [new] (source_unlabeled)
- source: https://admissions.nmsu.edu/cost-and-aid/scholarships.html (sha256 0a8b542de58f)
- issues: duplicate_table_versions, conflicting_sources:https://fa.nmsu.edu/scholarships/globalscholarships.html
- checks: {"thresholds": null}
  - award_amount_text: Percentage of tuition. ⟵ “NM Lottery Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. First-semester college GPA of 2.5 and pass 12 cre”
  - eligibility_summary: New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. First-semester college GPA of 2.5 and pass 12 credits. US Citizen or Permanent Resident. ⟵ “NM Lottery Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. First-semester college GPA of 2.5 and pass 12 cre”
  - renewal_requirements: 2.5 cumulative GPA. Enroll in and pass 12-18 credits per semester. Enroll in and pass 30 credit hours per academic year. For a maximum of seven semesters total. ⟵ “NM Lottery Scholarship | New Mexico resident. High school diploma from a NM accredited school, a NM GED, NM-HiSET, or Confirmation of Registration with PED. Must enroll in college within 16 months after high school graduation or receipt of GED/HiSET. First-semester college GPA of 2.5 and pass 12 cre”
### `abc41ac5e056a3cd` New Mexico State University-Main Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://fa.nmsu.edu/cost-of-attendance/ (sha256 51e1dde84b58)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 12}
  - column:Tuition and Fees For NM Residents: 8637 ⟵ “Tuition and Fees For NM Residents | $4,319 | $8,637”
  - column:Tuition and Fees for Non-NM Residents: 26964 ⟵ “Tuition and Fees for Non-NM Residents | $13,482 | $26,964”
  - column:Housing on-campus - No Dependents†: 6550 ⟵ “Housing on-campus - No Dependents† | $3,275 | $6,550”
  - column:Housing on-campus- With Dependents†: 8352 ⟵ “Housing on-campus- With Dependents† | $4,176 | $8,352”
  - column:Housing off-campus†: 10690 ⟵ “Housing off-campus† | $5,345 | $10,690”
  - column:Housing at-home: 3734 ⟵ “Housing at-home | $1,867 | $3,734”
  - column:Food on-campus†: 5964 ⟵ “Food on-campus† | $2,982 | $5,964”
  - column:Food off-campus†: 4050 ⟵ “Food off-campus† | $2,025 | $4,050”
  - column:Food at-home: 2628 ⟵ “Food at-home | $1,314 | $2,628”
  - column:Books, Course Materials, Supplies, Equipment‡: 1330 ⟵ “Books, Course Materials, Supplies, Equipment‡ | $665 | $1,330”
  - column:Personal Expenses‡: 2674 ⟵ “Personal Expenses‡ | $1,337 | $2,674”
  - column:Transportation‡: 1918 ⟵ “Transportation‡ | $959 | $1,918”
### `eeaee4c7d2670938` New Mexico State University-Main Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://fa.nmsu.edu/MYNMSU-FINANCIAL-AID-INSTRUCTION-GUIDE-Financial-Aid-Scholarship-Services-fa.nmsu.edu1.pdf (sha256 d93feb610869)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": false, "rows": 17}
  - column:conditions.: 11 ⟵ “conditions. | 11”
  - column:owe!: 6 ⟵ “owe! | 6”
  - column:Tuition: 1726.8 ⟵ “Tuition | $1,726.80 | $1,726.80 | $3,453.60”
  - column:$1,726.80: 1726.8 ⟵ “$1,726.80 | $1,726.80 | $3,453.60”
  - column:Housing & Food: 3141.0 ⟵ “Housing & Food | $3,141.00 | $3,141.00 | $6,282.00”
  - column:Books & Supplies: 625.0 ⟵ “Books & Supplies | $625.00 | $625.00 | $1,250.00”
  - column:Transportation: 891.0 ⟵ “Transportation | $891.00 | $891.00 | $1,782.00”
  - column:Personal Expenses: 1377.0 ⟵ “Personal Expenses | $1,377.00 | $1,377.00 | $2,754.00”
  - column:$6,034.00: 6034.0 ⟵ “$6,034.00 | $6,034.00 | $12,068.00”
  - column:Next!: 18 ⟵ “Next! | 18”
  - column:Current Amount Due: 0.0 ⟵ “Current Amount Due | $0.00 | Review your account summary.”
  - column:Account Balance: 0.0 ⟵ “Account Balance | $0.00”
  - column:$87.40: 0.0 ⟵ “$87.40 | $0.00”
  - column:$800.00: 0.0 ⟵ “$800.00 | $0.00”
  - column:$987.60: 0.0 ⟵ “$987.60 | $0.00”
  - column:Total: 1875.0 ⟵ “Total | $1,875.00 | $1,875.00 | $0.00 | 25”
  - column:down.: 27 ⟵ “down. | 27”
  - column:Tuition: 1726.8 ⟵ “Tuition | $1,726.80 | $1,726.80 | $3,453.60”
  - column:$1,726.80: 3453.6 ⟵ “$1,726.80 | $1,726.80 | $3,453.60”
  - column:Housing & Food: 3141.0 ⟵ “Housing & Food | $3,141.00 | $3,141.00 | $6,282.00”
  - column:Books & Supplies: 625.0 ⟵ “Books & Supplies | $625.00 | $625.00 | $1,250.00”
  - column:Transportation: 891.0 ⟵ “Transportation | $891.00 | $891.00 | $1,782.00”
  - column:Personal Expenses: 1377.0 ⟵ “Personal Expenses | $1,377.00 | $1,377.00 | $2,754.00”
  - column:$6,034.00: 12068.0 ⟵ “$6,034.00 | $6,034.00 | $12,068.00”
  - column:Here: 3 ⟵ “Here | correct Aid Year! | 3”
  - … 16 more rows
### `642aa84a8e63a374` San Juan College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sanjuancollege.edu/about/consumer-info/satisfactory-academic-progress/ (sha256 b57f854d7919)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “All required elements on the SAP appeal form must be completed and the completed appeal form and required documents that support a student’s appeal for financial aid reinstatement must be submitted to the financial aid office as one package no later than five business days after the start of the semester for which the student is seeking reinstatement of financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Satisfactory academic progress appeals may not be considered for approval if they are: Received after the fifth business day of a new semester, Incomplete or missing information/documentation, Missing support documents for extenuating circumstances, or Appeals for which supporting documentation is provided separately and at a later date from the original appeal submittal date The appeal process ma”
### `3b1a367a051aca63` Santa Fe Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfcc.edu/paying-for-school/professional-judgment/ (sha256 5cfd05bbc067)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Override Students may request a dependency override so that an otherwise dependent student can fill out the FAFSA as an independent student.”
### `5b1e221e9cb76cbf` Santa Fe Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfcc.edu/paying-for-school/professional-judgment/ (sha256 5cfd05bbc067)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustment In rare cases a student can request an adjustment to their Cost of Attendance.”
### `826f052f4adea996` Santa Fe Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfcc.edu/paying-for-school/professional-judgment/ (sha256 5cfd05bbc067)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Valid cases for a dependency override must involve unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “The following conditions, either alone or in combination, do NOT constitute unusual circumstances: · a student does not live with his/her parents · the student’s parents do not claim the student on their taxes · the student does not receive any financial support from the parents · the student’s parents refuse to fill out their portion of the FAFSA · the student is completely self-supporting In all”
### `aee2f8b0c14304ee` Santa Fe Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sfcc.edu/paying-for-school/professional-judgment/ (sha256 5cfd05bbc067)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment – Our Mission Request Info Directory Give to SFCC Calendar News Alerts Jobs Students We're Here for You!”
  - sentence: professional_judgment ⟵ “Regardless of the type of Professional Judgment being requested, all determinations are final and cannot be appealed.”
### `1d73d39d369ebfcb` Santa Fe Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sfcc.edu/paying-for-school/costs/ (sha256 e40f55b46ecd)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown
- checks: {"columns": 2, "components_reconcile": false, "rows": 6}
  - column:Books and Supplies: 1271 ⟵ “Books and Supplies | $1,271 | $635”
  - column:Personal Expenses: 2471 ⟵ “Personal Expenses | $2,471 | $1,235”
  - column:Room and Board: 19726 ⟵ “Room and Board | $19,726 | $9,863”
  - column:Tuition and Fees: 1908 ⟵ “Tuition and Fees | $1,908 | $954”
  - column:Transportation: 3534 ⟵ “Transportation | $3,534 | $1,767”
  - column:Total: 28909 ⟵ “Total | $28,909 | $14,454”
  - column:Books and Supplies: 635 ⟵ “Books and Supplies | $1,271 | $635”
  - column:Personal Expenses: 1235 ⟵ “Personal Expenses | $2,471 | $1,235”
  - column:Room and Board: 9863 ⟵ “Room and Board | $19,726 | $9,863”
  - column:Tuition and Fees: 954 ⟵ “Tuition and Fees | $1,908 | $954”
  - column:Transportation: 1767 ⟵ “Transportation | $3,534 | $1,767”
  - column:Total: 14454 ⟵ “Total | $28,909 | $14,454”
### `e5aacb3a9c51bcae` Southeast New Mexico College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.senmc.edu/studentregulations/financialaidscholarshipservices (sha256 cf74de2ba350)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals Students that fall below the satisfactory academic progress requirements have the right to appeal their ineligibility for Financial Aid.”
### `08f452b7d3ee673f` Southwestern Indian Polytechnic Institute — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sipi.edu/apps/pages/fees (sha256 e868d2420ad3)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition*: 0.0 ⟵ “Tuition* | $0.00”
  - column:Student Activity Fee: 50.0 ⟵ “Student Activity Fee | $50.00”
  - column:Library Fee: 70.0 ⟵ “Library Fee | $70.00”
  - column:Academic Enhancement Fee: 20.0 ⟵ “Academic Enhancement Fee | $20.00”
  - column:Lodge Resident Fee: 125.0 ⟵ “Lodge Resident Fee | $125.00”
  - column:Food Service Fee: 100.0 ⟵ “Food Service Fee | $100.00”
  - column:Textbook Fee: 145.0 ⟵ “Textbook Fee | $145.00”
  - column:Identification Fee: 5.0 ⟵ “Identification Fee | $5.00”
  - column:IT Fee: 75.0 ⟵ “IT Fee | $75.00”
  - column:TOTAL FEE: 590.0 ⟵ “TOTAL FEE | $590.00”
### `3594fae4cdd3210b` University of New Mexico-Main Campus — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://finaid.unm.edu/apply/fafsapply/fafsa.html (sha256 db8a131b8df0)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Unable to provide parent information, you can indicate this on the FAFSA form and follow-up with our office if you have a special circumstance NOTE: Even if contributors (parent's or spouse) don't have an SSN, didn't file taxes, or filed taxes outside of the U.S., they will still need to provide consent and approval.”
### `0ccf1868f933b336` University of New Mexico-Main Campus — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.unm.edu/costs-financial-aid/index.html (sha256 68879958a652)
- issues: conflicting_sources:https://finaid.unm.edu/coa/26-27/index.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees: 11585 ⟵ “Tuition & Fees | $11,585 | $11,585 | $34,734”
  - on_campus:Food & Housing - Traditional: 10648 ⟵ “Food & Housing - Traditional | $10,648 | $10,648 | $10,648”
  - on_campus:Books & Supplies: 1869 ⟵ “Books & Supplies | $1,869 | $1,869 | $1,869”
  - on_campus:Transportation: 2498 ⟵ “Transportation | $2,498 | $2,498 | $2,498”
  - on_campus:Miscellaneous: 2800 ⟵ “Miscellaneous | $2,800 | $2,800 | $2,800”
  - on_campus:Total: 29400 ⟵ “Total | $29,400 | $29,400 | $52,549”
### `100ebfdeb222dc81` University of New Mexico-Main Campus — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://finaid.unm.edu/coa/25-26/index.html (sha256 fefd61236985)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 13}
  - on_campus:Tuition & Fees***: 23833 ⟵ “Tuition & Fees*** | $23,833 | $7,944 | $56,821 | $18,940”
  - on_campus:Housing & Food†: 16490 ⟵ “Housing & Food† | $16,490 | $5,996 | $16,490 | $5,996”
  - on_campus:Course Fees: 1200 ⟵ “Course Fees | $1,200 | $400 | $1,200 | $400”
  - on_campus:Needlestick Insurance: 10 ⟵ “Needlestick Insurance | $10 | $10 | $10 | $10”
  - on_campus:HSC Library Fee: 525 ⟵ “HSC Library Fee | $525 | $263 | $525 | $263”
  - on_campus:Additional Fees***: 962 ⟵ “Additional Fees*** | $962 | $481 | $962 | $481”
  - on_campus:Direct Cost Sub-total: 43020 ⟵ “Direct Cost Sub-total | $43,020 | $15,094 | $76,008 | $26,090”
  - on_campus:Books & Supplies*: 2722 ⟵ “Books & Supplies* | $2,722 | $907 | $2,722 | $907”
  - on_campus:Miscellaneous**: 3737 ⟵ “Miscellaneous** | $3,737 | $1,359 | $3,737 | $1,359”
  - on_campus:Computer: 1100 ⟵ “Computer | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Transportation††: 3336 ⟵ “Transportation†† | $3,336 | $1,213 | $3,336 | $1,213”
  - on_campus:Indirect Costs Sub-total: 10895 ⟵ “Indirect Costs Sub-total | $10,895 | $4,579 | $10,895 | $4,579”
  - on_campus:Total Estimated Cost of Attendance: 53915 ⟵ “Total Estimated Cost of Attendance | $53,915 | $19,674 | $86,903 | $30,669”
### `20a24caa95892b6e` University of New Mexico-Main Campus — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://finaid.unm.edu/coa/26-27/index.html (sha256 46dce6883f03)
- issues: conflicting_sources:https://admissions.unm.edu/costs-financial-aid/index.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 13}
  - on_campus:Tuition & Fees***: 7944 ⟵ “Tuition & Fees*** | $23,833 | $7,944 | $56,821 | $18,940”
  - on_campus:Housing & Food†: 6235 ⟵ “Housing & Food† | $17,147 | $6,235 | $17,147 | $6,235”
  - on_campus:Course Fees: 400 ⟵ “Course Fees | $1,200 | $400 | $1,200 | $400”
  - on_campus:Needlestick Insurance: 10 ⟵ “Needlestick Insurance | $10 | $10 | $10 | $10”
  - on_campus:HSC Library Fee: 263 ⟵ “HSC Library Fee | $525 | $263 | $525 | $263”
  - on_campus:Additional Fees***: 481 ⟵ “Additional Fees*** | $962 | $481 | $962 | $481”
  - on_campus:Direct Cost Subtotal: 15333 ⟵ “Direct Cost Subtotal | $43,677 | $15,333 | $76,665 | $26,329”
  - on_campus:Books & Supplies*: 935 ⟵ “Books & Supplies* | $2,804 | $935 | $2,804 | $935”
  - on_campus:Miscellaneous**: 1400 ⟵ “Miscellaneous** | $3,850 | $1,400 | $3,850 | $1,400”
  - on_campus:Computer: 1100 ⟵ “Computer | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Transportation††: 1249 ⟵ “Transportation†† | $3,435 | $1,249 | $3,435 | $1,249”
  - on_campus:Indirect Costs Subtotal: 4684 ⟵ “Indirect Costs Subtotal | $11,188 | $4,684 | $11,188 | $4,684”
  - on_campus:Total Estimated Cost of Attendance: 20017 ⟵ “Total Estimated Cost of Attendance | $54,865 | $20,017 | $87,853 | $31,013”
### `43825da5cbee1fe8` University of New Mexico-Main Campus — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://finaid.unm.edu/coa/25-26/index.html (sha256 fefd61236985)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 17}
  - off_campus_not_with_family:Tuition & Fees: 15328 ⟵ “Tuition & Fees | $15,328 | $ 7,664”
  - off_campus_not_with_family:Housing & Food†: 21723 ⟵ “Housing & Food† | $21,723 | $10,861”
  - off_campus_not_with_family:Books & Supplies: 2079 ⟵ “Books & Supplies | $2,079 | $1,040”
  - off_campus_not_with_family:Background and Fingerprint: 110 ⟵ “Background and Fingerprint | $110 | $110”
  - off_campus_not_with_family:Transportation: 3715 ⟵ “Transportation | $3,715 | $1,857”
  - off_campus_not_with_family:Miscellaneous: 6823 ⟵ “Miscellaneous | $6,823 | $3,412”
  - off_campus_not_with_family:Curriculum Fee: 2700 ⟵ “Curriculum Fee | $2,700 | $1,350”
  - off_campus_not_with_family:Computer: 2200 ⟵ “Computer | $2,200 | $2,200”
  - off_campus_not_with_family:Diagnostic Equipment: 640 ⟵ “Diagnostic Equipment | $640 | $320”
  - off_campus_not_with_family:Disability Insurance: 103 ⟵ “Disability Insurance | $103 | $103”
  - off_campus_not_with_family:HSC Library/Council Fee: 525 ⟵ “HSC Library/Council Fee | $525 | $263”
  - off_campus_not_with_family:Health Insurance: 3994 ⟵ “Health Insurance | $3,994 | $1,997”
  - off_campus_not_with_family:Microscope Fee: 100 ⟵ “Microscope Fee | $100 | $50”
  - off_campus_not_with_family:Loan Fee: 320 ⟵ “Loan Fee | $320 | $160”
  - off_campus_not_with_family:Study Prep: 500 ⟵ “Study Prep | $500 | $250”
  - off_campus_not_with_family:Needlestick Insurance: 16 ⟵ “Needlestick Insurance | $16 | $16”
  - off_campus_not_with_family:Total Estimated Cost of Attendance: 60876 ⟵ “Total Estimated Cost of Attendance | $60,876 | $31,653”
### `86456b2195057edf` University of New Mexico-Main Campus — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://finaid.unm.edu/coa/25-26/index.html (sha256 fefd61236985)
- issues: components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": false, "rows": 13}
  - on_campus:Tuition & Fees***: 7944 ⟵ “Tuition & Fees*** | $23,833 | $7,944 | $56,821 | $18,940”
  - on_campus:Housing & Food†: 5996 ⟵ “Housing & Food† | $16,490 | $5,996 | $16,490 | $5,996”
  - on_campus:Course Fees: 400 ⟵ “Course Fees | $1,200 | $400 | $1,200 | $400”
  - on_campus:Needlestick Insurance: 10 ⟵ “Needlestick Insurance | $10 | $10 | $10 | $10”
  - on_campus:HSC Library Fee: 263 ⟵ “HSC Library Fee | $525 | $263 | $525 | $263”
  - on_campus:Additional Fees***: 481 ⟵ “Additional Fees*** | $962 | $481 | $962 | $481”
  - on_campus:Direct Cost Sub-total: 15094 ⟵ “Direct Cost Sub-total | $43,020 | $15,094 | $76,008 | $26,090”
  - on_campus:Books & Supplies*: 907 ⟵ “Books & Supplies* | $2,722 | $907 | $2,722 | $907”
  - on_campus:Miscellaneous**: 1359 ⟵ “Miscellaneous** | $3,737 | $1,359 | $3,737 | $1,359”
  - on_campus:Computer: 1100 ⟵ “Computer | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Transportation††: 1213 ⟵ “Transportation†† | $3,336 | $1,213 | $3,336 | $1,213”
  - on_campus:Indirect Costs Sub-total: 4579 ⟵ “Indirect Costs Sub-total | $10,895 | $4,579 | $10,895 | $4,579”
  - on_campus:Total Estimated Cost of Attendance: 19674 ⟵ “Total Estimated Cost of Attendance | $53,915 | $19,674 | $86,903 | $30,669”
### `99e5d2678f056b09` University of New Mexico-Main Campus — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://finaid.unm.edu/coa/26-27/index.html (sha256 46dce6883f03)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 2, "components_reconcile": false, "rows": 13}
  - on_campus:Tuition & Fees***: 56821 ⟵ “Tuition & Fees*** | $23,833 | $7,944 | $56,821 | $18,940”
  - on_campus:Housing & Food†: 17147 ⟵ “Housing & Food† | $17,147 | $6,235 | $17,147 | $6,235”
  - on_campus:Course Fees: 1200 ⟵ “Course Fees | $1,200 | $400 | $1,200 | $400”
  - on_campus:Needlestick Insurance: 10 ⟵ “Needlestick Insurance | $10 | $10 | $10 | $10”
  - on_campus:HSC Library Fee: 525 ⟵ “HSC Library Fee | $525 | $263 | $525 | $263”
  - on_campus:Additional Fees***: 962 ⟵ “Additional Fees*** | $962 | $481 | $962 | $481”
  - on_campus:Direct Cost Subtotal: 76665 ⟵ “Direct Cost Subtotal | $43,677 | $15,333 | $76,665 | $26,329”
  - on_campus:Books & Supplies*: 2804 ⟵ “Books & Supplies* | $2,804 | $935 | $2,804 | $935”
  - on_campus:Miscellaneous**: 3850 ⟵ “Miscellaneous** | $3,850 | $1,400 | $3,850 | $1,400”
  - on_campus:Computer: 1100 ⟵ “Computer | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Transportation††: 3435 ⟵ “Transportation†† | $3,435 | $1,249 | $3,435 | $1,249”
  - on_campus:Indirect Costs Subtotal: 11188 ⟵ “Indirect Costs Subtotal | $11,188 | $4,684 | $11,188 | $4,684”
  - on_campus:Total Estimated Cost of Attendance: 87853 ⟵ “Total Estimated Cost of Attendance | $54,865 | $20,017 | $87,853 | $31,013”
  - on_campus:Tuition & Fees***: 18940 ⟵ “Tuition & Fees*** | $23,833 | $7,944 | $56,821 | $18,940”
  - on_campus:Housing & Food†: 6235 ⟵ “Housing & Food† | $17,147 | $6,235 | $17,147 | $6,235”
  - on_campus:Course Fees: 400 ⟵ “Course Fees | $1,200 | $400 | $1,200 | $400”
  - on_campus:Needlestick Insurance: 10 ⟵ “Needlestick Insurance | $10 | $10 | $10 | $10”
  - on_campus:HSC Library Fee: 263 ⟵ “HSC Library Fee | $525 | $263 | $525 | $263”
  - on_campus:Additional Fees***: 481 ⟵ “Additional Fees*** | $962 | $481 | $962 | $481”
  - on_campus:Direct Cost Subtotal: 26329 ⟵ “Direct Cost Subtotal | $43,677 | $15,333 | $76,665 | $26,329”
  - on_campus:Books & Supplies*: 935 ⟵ “Books & Supplies* | $2,804 | $935 | $2,804 | $935”
  - on_campus:Miscellaneous**: 1400 ⟵ “Miscellaneous** | $3,850 | $1,400 | $3,850 | $1,400”
  - on_campus:Computer: 1100 ⟵ “Computer | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Transportation††: 1249 ⟵ “Transportation†† | $3,435 | $1,249 | $3,435 | $1,249”
  - on_campus:Indirect Costs Subtotal: 4684 ⟵ “Indirect Costs Subtotal | $11,188 | $4,684 | $11,188 | $4,684”
  - … 1 more rows
### `e6cfffbc1d1c0417` University of New Mexico-Main Campus — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.unm.edu/costs-financial-aid/index.html (sha256 68879958a652)
- issues: arrangement_unlabeled, conflicting_sources:https://finaid.unm.edu/coa/26-27/index.html
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - column:Tuition & Fees: 11585 ⟵ “Tuition & Fees | $11,585 | $11,585 | $34,734”
  - column:Food & Housing - Traditional: 10648 ⟵ “Food & Housing - Traditional | $10,648 | $10,648 | $10,648”
  - column:Books & Supplies: 1869 ⟵ “Books & Supplies | $1,869 | $1,869 | $1,869”
  - column:Transportation: 2498 ⟵ “Transportation | $2,498 | $2,498 | $2,498”
  - column:Miscellaneous: 2800 ⟵ “Miscellaneous | $2,800 | $2,800 | $2,800”
  - column:Total: 29400 ⟵ “Total | $29,400 | $29,400 | $52,549”
  - on_campus:Tuition & Fees: 34734 ⟵ “Tuition & Fees | $11,585 | $11,585 | $34,734”
  - on_campus:Food & Housing - Traditional: 10648 ⟵ “Food & Housing - Traditional | $10,648 | $10,648 | $10,648”
  - on_campus:Books & Supplies: 1869 ⟵ “Books & Supplies | $1,869 | $1,869 | $1,869”
  - on_campus:Transportation: 2498 ⟵ “Transportation | $2,498 | $2,498 | $2,498”
  - on_campus:Miscellaneous: 2800 ⟵ “Miscellaneous | $2,800 | $2,800 | $2,800”
  - on_campus:Total: 52549 ⟵ “Total | $29,400 | $29,400 | $52,549”
### `f94d044ed49af206` University of New Mexico-Main Campus — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://finaid.unm.edu/coa/26-27/index.html (sha256 46dce6883f03)
- issues: components_do_not_reconcile, conflicting_sources:https://admissions.unm.edu/costs-financial-aid/index.html
- checks: {"columns": 1, "components_reconcile": false, "rows": 13}
  - on_campus:Tuition & Fees***: 23833 ⟵ “Tuition & Fees*** | $23,833 | $7,944 | $56,821 | $18,940”
  - on_campus:Housing & Food†: 17147 ⟵ “Housing & Food† | $17,147 | $6,235 | $17,147 | $6,235”
  - on_campus:Course Fees: 1200 ⟵ “Course Fees | $1,200 | $400 | $1,200 | $400”
  - on_campus:Needlestick Insurance: 10 ⟵ “Needlestick Insurance | $10 | $10 | $10 | $10”
  - on_campus:HSC Library Fee: 525 ⟵ “HSC Library Fee | $525 | $263 | $525 | $263”
  - on_campus:Additional Fees***: 962 ⟵ “Additional Fees*** | $962 | $481 | $962 | $481”
  - on_campus:Direct Cost Subtotal: 43677 ⟵ “Direct Cost Subtotal | $43,677 | $15,333 | $76,665 | $26,329”
  - on_campus:Books & Supplies*: 2804 ⟵ “Books & Supplies* | $2,804 | $935 | $2,804 | $935”
  - on_campus:Miscellaneous**: 3850 ⟵ “Miscellaneous** | $3,850 | $1,400 | $3,850 | $1,400”
  - on_campus:Computer: 1100 ⟵ “Computer | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Transportation††: 3435 ⟵ “Transportation†† | $3,435 | $1,249 | $3,435 | $1,249”
  - on_campus:Indirect Costs Subtotal: 11188 ⟵ “Indirect Costs Subtotal | $11,188 | $4,684 | $11,188 | $4,684”
  - on_campus:Total Estimated Cost of Attendance: 54865 ⟵ “Total Estimated Cost of Attendance | $54,865 | $20,017 | $87,853 | $31,013”
### `4f8c338bcd4cfe7e` University of New Mexico-Main Campus — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://admissions.unm.edu/academics/testing/international-baccalaureate.html (sha256 6d5bcf93ecef)
- issues: course_column_missing
- checks: {"distinct_exams": 24, "equivalencies": 73, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | 5 | BIOL 1140 & BIOL 1140L (4 credits)”
  - equivalencies[IB-BIOLOGY|6]:  ⟵ “Biology | 6 | BIOL 1140 & BIOL 1140L (4 credits)”
  - equivalencies[IB-BIOLOGY|7]:  ⟵ “Biology | 7 | BIOL 1140 & BIOL 1140L (4 credits)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5]:  ⟵ “Business | 5 | BUSA 1110 (3 credits)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|6]:  ⟵ “Business | 6 | BUSA 1110 (3 credits)”
  - equivalencies[IB-BUSINESS-MANAGEMENT|7]:  ⟵ “Business | 7 | BUSA 1110 (3 credits)”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | CHEM 1120 (4 Credits)”
  - equivalencies[IB-CHEMISTRY|6]:  ⟵ “Chemistry | 6 | CHEM 1120 (4 Credits)”
  - equivalencies[IB-CHEMISTRY|7]:  ⟵ “Chemistry | 7 | CHEM 1120 (4 Credits)”
  - equivalencies[IB-COMPUTER-SCIENCE|5]:  ⟵ “Computer Science | 5 | CS 105L (3 Credits)”
  - equivalencies[IB-COMPUTER-SCIENCE|6]:  ⟵ “Computer Science | 6 | CS 105L (3 Credits)”
  - equivalencies[IB-COMPUTER-SCIENCE|7]:  ⟵ “Computer Science | 7 | CS 105L (3 Credits)”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | 5 | ECON 2110 (3 Credits)”
  - equivalencies[IB-ECONOMICS|6]:  ⟵ “Economics | 6 | ECON 2110 (3 Credits)”
  - equivalencies[IB-ECONOMICS|7]:  ⟵ “Economics | 7 | ECON 2110 (3 Credits)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|5]:  ⟵ “English A Lang & Lit | 5 | ENGL 1110 (3 credits)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|6]:  ⟵ “English A Lang & Lit | 6 | ENGL 1110 (3 credits)”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|7]:  ⟵ “English A Lang & Lit | 7 | ENGL 1110 (3 credits)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|5]:  ⟵ “English A Lit | 5 | ENGL 1410 (3 credits)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|6]:  ⟵ “English A Lit | 6 | ENGL 1410 (3 credits)”
  - equivalencies[IB-ENGLISH-A-LITERATURE|7]:  ⟵ “English A Lit | 7 | ENGL 1410 (3 credits)”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|5]:  ⟵ “Environmental Systems & Society | 5 | ENVS 1130 (3 credits)”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|6]:  ⟵ “Environmental Systems & Society | 6 | ENVS 1130 (3 credits)”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|7]:  ⟵ “Environmental Systems & Society | 7 | ENVS 1130 (3 credits)”
  - equivalencies[IB-FILM|5]:  ⟵ “Film | 5 | FDMA 1520 (3 Credits)”
  - … 48 more rows
### `149d91e950ad8712` University of New Mexico-Valencia County Campus — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://valencia.unm.edu/academics/catalog/2014-2016/catalog-2014-2016.pdf (sha256 c1519b87694c)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 20, "equivalencies": 23, "rows_without_score": 0}
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|6]:  ⟵ “Social Sciences & History  500 50              General Credit    6”
  - equivalencies[CLEP-HUMANITIES|6]:  ⟵ “Humanities                 500 50              General Credit    6”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|6]:  ⟵ “College Mathematics        570 57              General Credit    6”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                        450       50           BIOL 110                         3”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry                      520       63           CHEM 121L, 122L                  8”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|54]:  ⟵ “Intro Macroeconomics           490       54           ECON 105                         3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|54]:  ⟵ “Intro Microeconomics           470       54           ECON 106                         3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|55]:  ⟵ “Western Civilization I         500       55           HIST 101                         3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|55]:  ⟵ “Western Civilization II        500       55           HIST 102                         3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|65]:  ⟵ “American Government            550       65           POLS 200                         3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|63]:  ⟵ “Human Growth & Development     520       63           PSY 220                          3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|54]:  ⟵ “Principles of Management       500       54           MGT 113                          3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing        500       50           MGT 222                          3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|59]:  ⟵ “College Algebra                560       59           MATH 121                         3”
  - equivalencies[CLEP-CALCULUS|70]:  ⟵ “Calculus                       510       70           MATH 162                         4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|48]:  ⟵ “French Language                400       48           FREN 101                         3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|52]:  ⟵ “French Language                450       52           FREN 101, 102                    6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “German Language                390       63           GRMN 101, 102                    6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|45]:  ⟵ “Spanish Language               390       45           SPAN 101                         3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language               440       50           SPAN 101, 102                    6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|57]:  ⟵ “Spanish Language               540       57           SPAN 101, 102, 201, 202         12”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|59]:  ⟵ “Introduction to Sociology      520       59           SOC 101                          3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|56]:  ⟵ “Introduction to Psychology     550       56           PSY 105                          3”
### `74d4c18c5b916c41` University of New Mexico-Valencia County Campus — credit_policies 2021-22 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://valencia.unm.edu/admissions/dual-credit-program/how-to-apply.html (sha256 609e70dc7b4c)
- issues: stale_year_label:2021-22
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “Minimum 2.5 GPA on transcript.”
### `2f582a2fe31594dd` Western New Mexico University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.wnmu.edu/apply/ (sha256 895c632634f3)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “However, none of the con­ditions listed below, singly or in combination, qualify as unusual circum­stance allowing a dependency override: Parents do not want to contribute to the student’s education.”
### `3e91806e35d06d93` Western New Mexico University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.wnmu.edu/apply/ (sha256 895c632634f3)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgement/Income Reduction + Professional Judgement/Income Reduction allows the financial aid director to make changes to a student or parent’s income if it has changed due to different circumstances listed below.”
  - sentence: professional_judgment ⟵ “In order to request a professional judgement/income reduction, the student must start by emailing fadocuments@wnmu.edu explaining their circumstance.”
### `9c82a70551c60ab2` Western New Mexico University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.wnmu.edu/apply/ (sha256 895c632634f3)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Foster Care/Adopted Child/Ward of the Court/ Legal Guardianship + Students who were in foster care, ward of the court, or were adopted at 13 or older are considered automatically independent on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “Dependency Override + A dependency override allows the financial aid director to change a student’s status from dependent to independent based on unusual circumstances where students are not able to give parent information.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances do include: Abandonment by parents.”
  - sentence: need_based_special_circumstances ⟵ “The FAA must confirm each year that the unusual circumstance remains and an override is still fitting.”
  - sentence: need_based_special_circumstances ⟵ “The individual writing the letter should establish the unusual circumstances.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 0; pages by category: 

## Blocked by the site (every request refused; needs the browser fallback)

- Institute of American Indian and Alaska Native Culture and Arts Development (`ipeds-187745`)
- Eastern New Mexico University Ruidoso Branch Community College (`ipeds-383996`)

## Leads: official pages found with no extracted record

- Central New Mexico Community College: tuition_fees, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Clovis Community College: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Eastern New Mexico University-Main Campus: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- Eastern New Mexico University-Roswell Campus: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, residency
- Luna Community College: admissions_tests, common_data_set, dual_enrollment, transfer_credit, residency, degree_requirements
- Navajo Technical University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- New Mexico Highlands University: tuition_fees, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- New Mexico Institute of Mining and Technology: tuition_fees, cost_of_attendance, admissions_tests, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- New Mexico Junior College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- New Mexico Military Institute: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency
- New Mexico State University-Alamogordo: tuition_fees, admissions_tests, common_data_set, merit_scholarships, dual_enrollment
- New Mexico State University-Dona Ana: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment
- New Mexico State University-Grants: admissions_tests, dual_enrollment, transfer_credit, degree_requirements
- New Mexico State University-Main Campus: admissions_tests, common_data_set, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Northern New Mexico College: admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- San Juan College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit
- Santa Fe Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Southeast New Mexico College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, transfer_credit, residency, degree_requirements
- Southwestern Indian Polytechnic Institute: admissions_tests, common_data_set, merit_scholarships, transfer_credit
- St. John's College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, aid_appeals
- University of New Mexico-Gallup Campus: tuition_fees, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, residency, degree_requirements, aid_appeals
- University of New Mexico-Los Alamos Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements, aid_appeals
- University of New Mexico-Main Campus: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- University of New Mexico-Taos Campus: tuition_fees, admissions_tests, common_data_set, merit_scholarships, transfer_credit, degree_requirements
- University of New Mexico-Valencia County Campus: tuition_fees, admissions_tests, common_data_set, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Western New Mexico University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
