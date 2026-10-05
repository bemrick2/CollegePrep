# Review queue — WI (2026-27)

Pages fetched: 4086; failures: 231. Candidates: 252 (53 without issues, 199 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 6 | 23 | 21 | 2 | 4 |
| cost_of_attendance | 0 | 0 | 2 | 11 | 37 | 2 | 4 |
| admissions_tests | 0 | 0 | 0 | 1 | 45 | 6 | 4 |
| common_data_set | 0 | 0 | 0 | 1 | 5 | 46 | 4 |
| merit_scholarships | 0 | 0 | 5 | 0 | 41 | 6 | 4 |
| ap_credit | 0 | 0 | 5 | 7 | 18 | 22 | 4 |
| clep_credit | 0 | 0 | 2 | 8 | 16 | 26 | 4 |
| ib_credit | 0 | 0 | 2 | 3 | 8 | 39 | 4 |
| dual_enrollment | 0 | 0 | 6 | 0 | 28 | 18 | 4 |
| transfer_credit | 0 | 0 | 9 | 0 | 42 | 1 | 4 |
| statewide_articulation | 0 | 0 | 0 | 0 | 25 | 27 | 4 |
| residency | 0 | 0 | 0 | 0 | 31 | 21 | 4 |
| degree_requirements | 0 | 0 | 0 | 1 | 37 | 14 | 4 |
| aid_appeals | 0 | 0 | 0 | 33 | 8 | 11 | 4 |

## Ready for review (53)

### `588ab46486d33ff1` Beloit College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.beloit.edu/admission/tuition-aid/scholarships/ (sha256 c33128d6c19e)
- checks: {"thresholds": null}
  - award_amount_text: $46,000-50,000 ⟵ “Presidential Scholarship | $46,000-50,000 | 3.5 - 4.0”
  - gpa_requirement: 3.5 - 4.0 ⟵ “Presidential Scholarship | $46,000-50,000 | 3.5 - 4.0”
### `81278bc338e7a6ab` Beloit College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.beloit.edu/admission/tuition-aid/scholarships/ (sha256 c33128d6c19e)
- checks: {"thresholds": null}
  - award_amount_text: $34,000-38,000 ⟵ “Deans’ Award | $34,000-38,000 | <3.0”
  - gpa_requirement: <3.0 ⟵ “Deans’ Award | $34,000-38,000 | <3.0”
### `f9c997fdd7ce32f7` Beloit College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.beloit.edu/admission/tuition-aid/scholarships/ (sha256 c33128d6c19e)
- checks: {"thresholds": null}
  - award_amount_text: $39,000-45,000 ⟵ “Eaton Scholarship | $39,000-45,000 | 3.0 - 3.49”
  - gpa_requirement: 3.0 - 3.49 ⟵ “Eaton Scholarship | $39,000-45,000 | 3.0 - 3.49”
### `5a777d86a1e11201` Beloit College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.beloit.edu/offices/financial-aid/cost-of-attendance/ (sha256 9efd3c45d36a)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 63792 ⟵ “Tuition | $63,792”
  - column:Student Activity Fee: 280 ⟵ “Student Activity Fee | $280”
  - column:Housing (double occupancy): 6882 ⟵ “Housing (double occupancy) | $6,882”
  - column:Food (full meal plan-required the first year): 6314 ⟵ “Food (full meal plan-required the first year) | $6,314”
  - column:Health/Wellness Fees: 264 ⟵ “Health/Wellness Fees | $264”
  - column:Total Direct Costs: 77532 ⟵ “Total Direct Costs | $77,532”
### `m017912467e1d8b0` Beloit College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.beloit.edu/offices/registrar/transfer-ap-gce-ib-credit/ (sha256 14f163676ef7)
- checks: {"fields": ["min_grade"], "merged_pages": 4}
  - min_grade: C ⟵ “Courses with a grade of “C” or better are eligible for transfer credit.”
  - min_grade: C ⟵ “You must have earned a grade of “C” or better for the credit to transfer.”
  - min_grade: C ⟵ “Courses with a grade of “C” or better are eligible for transfer credit.”
  - min_grade: C ⟵ “Report All Transfer Credit Promptly All academic work on the college level and of a liberal arts nature, undertaken at other accredited institutions, and successfully completed with a grade of “C” or better, must become part of the student’s permanent record at Beloit.”
  - min_grade: C ⟵ “A grade of “C” or better is required for the credit to transfer.”
  - min_grade: C ⟵ “Transfer credit for first-year applicants Beloit College will apply up to 15 units of transfer credit from dual enrollment courses with a grade of “C” or better taken at accredited colleges and universities toward a student’s Beloit degree.”
### `me9fb955f546437e` Blackhawk Technical College — transfer_policies 2026-27 [new] (labeled_in_heading)
- source: https://catalog.blackhawk.edu/registration-and-records/transfer-cpl/ (sha256 7414e26c2bec)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: B ⟵ “Transfer of credits can be evaluated from regionally and nationally accredited post-secondary institutions (where a "C" or better was earned) and, under certain circumstances, high school institutions (high school courses for which advanced standing was granted and a grade of "B" or better was earned).”
  - min_grade: B ⟵ “Transfer of Blackhawk Course Name/Credits. credits can be evaluated from regionally and nationally accredited post- secondary institutions (where a "C" or better was earned) and, under Art certain circumstances, high school institutions (high school courses for • AP 2-D Art and Design/3 to 5/815-999/Humanities Elective/3 which advanced standing was granted and a grade of "B" or better was • AP 3-D”
### `m1833d6978bee132` Bryant & Stratton College-Wauwatosa — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.bryantstratton.edu/degrees/catalog/academic-information/ (sha256 1e6069b2ad80)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Each course considered for transfer credit must have grade of C (2.0) or better out of a possible (4.0).”
  - min_grade: C ⟵ “Each course considered for transfer credit must have grade of C (2.0) or better out of a possible (4.0).”
### `92f819c47d322b85` Carroll University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.carrollu.edu/admission/undergrad-transfer/credit-policy/ (sha256 f3f972f546da)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 32 ⟵ “Note: Full-time and part-time students are required to complete their final 32 hours at Carroll.”
### `00a52a0eb1db282a` Concordia University-Wisconsin — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cuw.edu/admissions/undergraduate-admissions/tuition-fees.html (sha256 2624ce258b5b)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition: 37080 ⟵ “Tuition | $37,080 | $37,080”
  - with_parents_or_family:Consolidated Fee: 540 ⟵ “Consolidated Fee | $540 | $540”
  - with_parents_or_family:Books & Supplies*: 1250 ⟵ “Books & Supplies* | $1,250 | $1,250”
  - with_parents_or_family:Housing & Food**: 14080 ⟵ “Housing & Food** | $14,080 | $3,500”
  - with_parents_or_family:Transportation*: 1260 ⟵ “Transportation* | $1,260 | $2,500”
  - with_parents_or_family:Personal Expenses*: 2000 ⟵ “Personal Expenses* | $2,000 | $2,000”
  - with_parents_or_family:Total: 56210 ⟵ “Total | $56,210 | $46,870”
  - with_parents_or_family:Tuition: 37080 ⟵ “Tuition | $37,080 | $37,080”
  - with_parents_or_family:Consolidated Fee: 540 ⟵ “Consolidated Fee | $540 | $540”
  - with_parents_or_family:Books & Supplies*: 1250 ⟵ “Books & Supplies* | $1,250 | $1,250”
  - with_parents_or_family:Housing & Food**: 3500 ⟵ “Housing & Food** | $14,080 | $3,500”
  - with_parents_or_family:Transportation*: 2500 ⟵ “Transportation* | $1,260 | $2,500”
  - with_parents_or_family:Personal Expenses*: 2000 ⟵ “Personal Expenses* | $2,000 | $2,000”
  - with_parents_or_family:Total: 46870 ⟵ “Total | $56,210 | $46,870”
### `46028fee5506b96b` Concordia University-Wisconsin — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.cuw.edu/admissions/transfer-admissions/transfer-process.html (sha256 6927d16b25bd)
- checks: {"fields": ["min_grade"]}
  - min_grade: D ⟵ “A grade of D or higher in any class is considered for transfer credit from an accredited higher-educational institution.”
### `ec11260f30c8095e` Lawrence University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lawrence.edu/admissions-aid/aid-affordability/tuition-costs/ (sha256 09e6bdfc7bbb)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 61407 ⟵ “Tuition | $20,469 | $61,407”
  - column:Fees: 312 ⟵ “Fees | $104 | $312”
  - column:Housing*: 7047 ⟵ “Housing* | $2,349 | $7,047”
  - column:Meal Plan**: 6792 ⟵ “Meal Plan** | $2,264 | $6,792”
  - column:Total: 75558 ⟵ “Total | $25,186 | $75,558”
### `bbf2ef08afba2d5e` Lawrence University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.lawrence.edu/wp-content/uploads/2026/08/AP-Credit_-New-Student-Advising-and-Registration%E2%80%A6_0.pdf (sha256 b458df20ad5d)
- checks: {"distinct_exams": 9, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology             4-5     6 units BIOL    Student exempted from BIOL 130 & BIOL 131.”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB         4-5                     credit will be awarded. Credit fulfills quantitative”
  - equivalencies[AP-CALCULUS-BC|4-5]:  ⟵ “Calculus BC         4-5                     credit will be awarded. Credit fulfills quantitative”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry           4       elective        CHEM 116.”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry           5       115             CHEM 116.”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin                3     0 units        Student may enroll in CLAS 220.”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin                4     6 units CLAS   literature. Credit fulfills language competency”
  - equivalencies[AP-LATIN|5]:  ⟵ “Latin            5     6 units CLAS   literature. Credit fulfills language competency”
  - equivalencies[AP-PHYSICS-1|4-5]:  ⟵ “Physics 1        4-5   6 units PHYS   appropriate course placement. Credit fulfills”
  - equivalencies[AP-PHYSICS-2|4-5]:  ⟵ “Physics 2        4-5   6 units PHYS   appropriate course placement. Credit fulfills”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus          4-5                     credit will be awarded. Credit fulfills quantitative”
  - equivalencies[AP-STATISTICS|4-5]:  ⟵ “Statistics           4-5                    Credit fulfills quantitative competency GER.”
### `8117b313810a1598` Maranatha Baptist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.mbu.edu/scholarship/academic-merit-scholarship/ (sha256 661bd190bc41)
- checks: {"thresholds": null}
  - test_requirement: ACT Composite Score: 25-26; SAT Composite Score: 1200-1250 ⟵ “25-26 | 1200-1250 | $1,000 per year ($500 per semester)”
  - award_amount_text: $1,000 per year ($500 per semester) ⟵ “25-26 | 1200-1250 | $1,000 per year ($500 per semester)”
### `83111fd89a4387b2` Maranatha Baptist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.mbu.edu/scholarship/academic-merit-scholarship/ (sha256 661bd190bc41)
- checks: {"thresholds": null}
  - test_requirement: ACT Composite Score: 27-29; SAT Composite Score: 1260-1350 ⟵ “27-29 | 1260-1350 | $3,500 per year ($1,750 per semester)”
  - award_amount_text: $3,500 per year ($1,750 per semester) ⟵ “27-29 | 1260-1350 | $3,500 per year ($1,750 per semester)”
### `d9278d5952f95066` Maranatha Baptist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.mbu.edu/scholarship/academic-merit-scholarship/ (sha256 661bd190bc41)
- checks: {"thresholds": null}
  - test_requirement: ACT Composite Score: 30+; SAT Composite Score: 1360+ ⟵ “30+ | 1360+ | $5,000 per year ($2,500 per semester)”
  - award_amount_text: $5,000 per year ($2,500 per semester) ⟵ “30+ | 1360+ | $5,000 per year ($2,500 per semester)”
### `240bc4348ca93623` Maranatha Baptist University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mbu.edu/online_learning/dual-enrollment/ (sha256 bb7ba7a06936)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 175 ⟵ “Only $175 per credit hour”
  - per_credit_hour_charge: 175 ⟵ “$175 Per credit”
  - per_credit_hour_charge: 175 ⟵ “If you’re a dual enrollment student, you will pay only $175 per credit in tuition after automatically receiving a discount of more than 50% off the tuition for college courses you take online.”
  - per_credit_hour_charge: 15 ⟵ “In addition to the tuition, there is a $15 per credit comprehensive fee, and a $40 Adobe software fee for all CADM courses. Students are responsible for purchasing their own textbooks and materials. Student bills may be paid through the Finances tab of MyMaranatha (only accessible after admission).”
### `7744adcd9b3fc53d` Marian University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.marianuniversity.edu/admission/early-college-credit/ (sha256 f0921e529858)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 99 ⟵ “Tuition for all UCC courses is $99 per credit and will be billed directly to each student’s home address. Any financial questions should be directed to the university’s Business Office at 920-923-8520.”
### `9054a694517d301d` Marquette University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2027-2028.php (sha256 db785d68b36a)
- checks: {"thresholds": null}
  - award_amount_text: 277 ⟵ “Student | 277”
### `a6f57ac8b180e1ff` Marquette University — awards 2026-27 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2026-2027.php (sha256 14055fd5c8f1)
- checks: {"thresholds": null}
  - award_amount_text: $1,932 ⟵ “Title IV | $1,932”
### `cab5f9c1da8e3395` Marquette University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2027-2028.php (sha256 db785d68b36a)
- checks: {"thresholds": null}
  - award_amount_text: $1,932 ⟵ “Title IV | $1,932”
### `cd7d9fcd39dedc36` Marquette University — awards 2026-27 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2026-2027.php (sha256 14055fd5c8f1)
- checks: {"thresholds": null}
  - award_amount_text: 277 ⟵ “Student | 277”
### `dc137e05a8332739` Marquette University — awards 2027-28 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2027-2028.php (sha256 db785d68b36a)
- checks: {"thresholds": null}
  - award_amount_text: 791 ⟵ “Marquette | 791”
### `e0ae7018c19450f4` Marquette University — awards 2026-27 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2026-2027.php (sha256 14055fd5c8f1)
- checks: {"thresholds": null}
  - award_amount_text: 791 ⟵ “Marquette | 791”
### `5c191c8a9fb9e376` Milwaukee Area Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.matc.edu/admissions-registration/cple/transfer-credit.html (sha256 0f66b37d73d5)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “College transfer credits must have a minimum grade of C or better.”
### `c90b70a7bd3b4432` Milwaukee Institute of Art & Design — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.miad.edu/academic-programs/non-degree-programs/early-college-credit-program (sha256 d4e161c40a72)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.7 ⟵ “MIAD requires a cumulative 2.70 grade point average to be eligible for ECCP classes.”
### `6f857efeba8a6f1b` Northcentral Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.ntc.edu/admissions/credit-prior-learning/national-exams/clep-exams-accepted (sha256 bfadef5b1fa4)
- checks: {"distinct_exams": 9, "equivalencies": 10, "rows_without_score": 0}
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 10-801-195 | Written Communication | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 10-801-136 | English Composition 1 | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 10-809-122 | Intro to American Government | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | 10-809-188 | Developmental Psychology | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 10-809-198 | Introduction to Psychology | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 10-809-196 | Introduction to Sociology | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 10-809-195 | Economics | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 10-809-195 | Economics | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 10-804-195 | College Algebra w/Apps | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 10-804-107 | College Math | 3”
### `83e68138508062a0` Northeast Wisconsin Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.nwtc.edu/admissions-and-aid/transfer/national-exams (sha256 73033267e07c)
- checks: {"distinct_exams": 16, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|Biology (3,4,5)]:  ⟵ “Biology (3,4,5) | General Biology (10806114) | 4”
  - equivalencies[AP-CHEMISTRY|Chemistry (3,4,5)]:  ⟵ “Chemistry (3,4,5) | General Chemistry 1 (10806134) | 4”
  - equivalencies[AP-CHEMISTRY|Chemistry (3,4,5)]:  ⟵ “Chemistry (3,4,5) | College Chemistry 1 (10806135) | 5”
  - equivalencies[AP-CHEMISTRY|Chemistry ( 3,4,5)]:  ⟵ “Chemistry ( 3,4,5) | College Chemistry 2 (10506136) | 5”
  - equivalencies[AP-COMPUTER-SCIENCE-A|Computer Science A (3,4,5)]:  ⟵ “Computer Science A (3,4,5) | Programming in Java Part 1 (10152141) | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|Computer Science Principles (3,4,5)]:  ⟵ “Computer Science Principles (3,4,5) | Careers in IT (10107117) | 1”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|Environmental Science (3,4,5)]:  ⟵ “Environmental Science (3,4,5) | Principles of Sustainability (10806112) | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|Environmental Science (3,4,5)]:  ⟵ “Environmental Science (3,4,5) | Environmental Science (10506146) | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|Human Geography (3,4,5)]:  ⟵ “Human Geography (3,4,5) | Intro to Diversity Studies (10809172) | 3”
  - equivalencies[AP-MACROECONOMICS|Macroeconomics (3)]:  ⟵ “Macroeconomics (3) | Economics (10809195) | 3”
  - equivalencies[AP-MACROECONOMICS|Macroeconomics (4,5)]:  ⟵ “Macroeconomics (4,5) | Macroeconomics (20809287) | 3”
  - equivalencies[AP-CALCULUS-AB|Math: Calculus AB (3,4,5)]:  ⟵ “Math: Calculus AB (3,4,5) | Calculus 1 (10804198) | 4”
  - equivalencies[AP-CALCULUS-BC|Math: Calculus BC: AB Sub Score (3,4,5)]:  ⟵ “Math: Calculus BC: AB Sub Score (3,4,5) | Calculus 1 (10804198) | 4”
  - equivalencies[AP-CALCULUS-BC|Math: Calculus BC (3,4,5)]:  ⟵ “Math: Calculus BC (3,4,5) | Calculus 1 (10804198) & Calculus 2 (10804181) | 8”
  - equivalencies[AP-PRECALCULUS|Math: Precalculus (3,4,5)]:  ⟵ “Math: Precalculus (3,4,5) | College Algebra & Trigonometry (10804197) | 5”
  - equivalencies[AP-MICROECONOMICS|Microeconomics (3)]:  ⟵ “Microeconomics (3) | Economics (10809195) | 3”
  - equivalencies[AP-MICROECONOMICS|Microeconomics (4,5)]:  ⟵ “Microeconomics (4,5) | Microeconomics (20809291) | 3”
  - equivalencies[AP-PSYCHOLOGY|Psychology (3,4,5)]:  ⟵ “Psychology (3,4,5) | Intro to Psychology (10809198) | 3”
  - equivalencies[AP-SEMINAR|Seminar (3,4,5)]:  ⟵ “Seminar (3,4,5) | English Composition 1 (10801136) | 3”
  - equivalencies[AP-STATISTICS|Statistics (3,4,5)]:  ⟵ “Statistics (3,4,5) | Introductory Statistics (10804189) | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|Spanish Language and Culture (3)]:  ⟵ “Spanish Language and Culture (3) | Spanish 101 (10802104) | 4”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|Spanish Language and Culture (4,5)]:  ⟵ “Spanish Language and Culture (4,5) | Spanish 102 (10802105) | 4”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|Spanish Literature and Culture (3)]:  ⟵ “Spanish Literature and Culture (3) | Spanish 101 (10802104) | 4”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|Spanish Literature and Culture (4,5)]:  ⟵ “Spanish Literature and Culture (4,5) | Spanish 102 (10802105) | 4”
### `d5b6754c98513e07` Northeast Wisconsin Technical College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.nwtc.edu/admissions-and-aid/transfer/national-exams (sha256 73033267e07c)
- checks: {"distinct_exams": 13, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|Biology (HL) (4,5,6,7)]:  ⟵ “Biology (HL) (4,5,6,7) | General Biology (10806114) | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|Business & Mgmt (HL) (4,5,6,7)]:  ⟵ “Business & Mgmt (HL) (4,5,6,7) | Business Principles (10102158) | 3”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry (HL) (4,5,6,7)]:  ⟵ “Chemistry (HL) (4,5,6,7) | General Chemistry (10806134) | 4”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry (HL) (4,5,6,7)]:  ⟵ “Chemistry (HL) (4,5,6,7) | College Chemistry 1 (10806135) | 5”
  - equivalencies[IB-CHEMISTRY-HL|Chemistry (HL) (4,5,6,7)]:  ⟵ “Chemistry (HL) (4,5,6,7) | College Chemistry 2 (10506136) | 5”
  - equivalencies[IB-ECONOMICS-HL|Economics (HL) (4,5,6,7)]:  ⟵ “Economics (HL) (4,5,6,7) | Economics (10809195) | 3”
  - equivalencies[IB-ECONOMICS-HL|Economics (HL) (4,5,6,7)]:  ⟵ “Economics (HL) (4,5,6,7) | Principles of Macroeconomics (20809287) | 3”
  - equivalencies[IB-ECONOMICS-HL|Economics (HL) (4,5,6,7)]:  ⟵ “Economics (HL) (4,5,6,7) | Principles of Microeconomics (20809291) | 3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-HL|English A: Language & Literature (HL/SL) (4,5,6,7)]:  ⟵ “English A: Language & Literature (HL/SL) (4,5,6,7) | English Composition 1 (10801136) | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|Environmental Systems & Societies (SL) (4,5,6,7)]:  ⟵ “Environmental Systems & Societies (SL) (4,5,6,7) | Principles of Sustainability (10806112) | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|Environmental Systems & Societies (SL) (4,5,6,7)]:  ⟵ “Environmental Systems & Societies (SL) (4,5,6,7) | Intro to Environmental Science (10506146) | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|Mathematics: Analysis & Approaches (SL) (4,5,6,7)]:  ⟵ “Mathematics: Analysis & Approaches (SL) (4,5,6,7) | College Algebra (10804195) | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|Mathematics: Analysis & Approaches (HL) (4,5,6,7)]:  ⟵ “Mathematics: Analysis & Approaches (HL) (4,5,6,7) | Calculus 1 (10804198) | 4”
  - equivalencies[IB-PHILOSOPHY-HL|Philosophy (HL) (4,5,6,7)]:  ⟵ “Philosophy (HL) (4,5,6,7) | Intro to Ethics (10809166) | 3”
  - equivalencies[IB-PHYSICS-HL|Physics (HL) (5,6,7)]:  ⟵ “Physics (HL) (5,6,7) | General Physics 1 (10806154) | 4”
  - equivalencies[IB-PHYSICS-HL|Physics (HL) (5,6,7)]:  ⟵ “Physics (HL) (5,6,7) | General Physics 2 (10806164) | 4”
  - equivalencies[IB-PSYCHOLOGY-HL|Psychology (HL/SL) (4,5,67)]:  ⟵ “Psychology (HL/SL) (4,5,67) | Psychology (10809198) | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|Social & Cultural Anthropology (HL/SL) (4,5,6,7)]:  ⟵ “Social & Cultural Anthropology (HL/SL) (4,5,6,7) | Intro to Diversity Studies (10809172) | 3”
  - equivalencies[IB-SPANISH-HL|Spanish AB (HL) (4,5,6,7)]:  ⟵ “Spanish AB (HL) (4,5,6,7) | Spanish 101 (10802104) | 4”
  - equivalencies[IB-SPANISH-HL|Spanish B (HL) (4,5,6,7)]:  ⟵ “Spanish B (HL) (4,5,6,7) | Spanish 101 (10802104) | 4”
### `2a494d51f8e54bf4` Northeast Wisconsin Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.nwtc.edu/getmedia/3cc20287-1410-4a41-b029-e92cd86e3a1f/Transfer-of-Credit-Policy.pdf (sha256 ff452a302823)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer of program requirements will be approved when the submitted course(s) are equivalent in content and credit value, and a grade of C or higher has been earned.”
### `00d8c64ff5ecacbe` Ripon College — awards 2026-27 [new] (source_unlabeled)
- source: https://ripon.edu/admission/cost-and-financial-aid/scholarships-and-aid/fine-art-scholarships/ (sha256 887408eb4b46)
- checks: {"thresholds": null}
  - eligibility_summary: One piece of prepared music Vocalizing for range and some sight-singing ⟵ “Voice | One piece of prepared music Vocalizing for range and some sight-singing”
### `4b85cfa2ebdb48cb` Ripon College — awards 2026-27 [new] (source_unlabeled)
- source: https://ripon.edu/admission/cost-and-financial-aid/scholarships-and-aid/fine-art-scholarships/ (sha256 887408eb4b46)
- checks: {"thresholds": null}
  - eligibility_summary: Two contrasting pieces or sections of pieces of music (approx. 2–4 minutes) 2 octaves of any major or minor scale Guitar: May substitute with I–IV–V–I chord progression in two keys (major or minor) ⟵ “Strings(violin, viola, cello, double bass, guitar) | Two contrasting pieces or sections of pieces of music (approx. 2–4 minutes) 2 octaves of any major or minor scale Guitar: May substitute with I–IV–V–I chord progression in two keys (major or minor)”
### `4d6bfce6d9c566bd` Ripon College — awards 2026-27 [new] (source_unlabeled)
- source: https://ripon.edu/admission/cost-and-financial-aid/scholarships-and-aid/fine-art-scholarships/ (sha256 887408eb4b46)
- checks: {"thresholds": null}
  - eligibility_summary: Sections of two contrasting pieces of prepared music (approx. 2–4 minutes total) Any major or minor scale (range appropriate for instrument) ⟵ “Winds or Brass | Sections of two contrasting pieces of prepared music (approx. 2–4 minutes total) Any major or minor scale (range appropriate for instrument)”
### `9cc03d049b06e27b` Ripon College — awards 2026-27 [new] (source_unlabeled)
- source: https://ripon.edu/admission/cost-and-financial-aid/scholarships-and-aid/fine-art-scholarships/ (sha256 887408eb4b46)
- checks: {"thresholds": null}
  - eligibility_summary: Sections of pieces for two contrasting percussion instruments Examples: mallet keyboards, snare drum, timpani, multi-percussion, drum set NOT two similar instruments (e.g., xylophone + vibraphone) ⟵ “Percussion | Sections of pieces for two contrasting percussion instruments Examples: mallet keyboards, snare drum, timpani, multi-percussion, drum set NOT two similar instruments (e.g., xylophone + vibraphone)”
### `a01b13c4334c4d77` Ripon College — awards 2026-27 [new] (source_unlabeled)
- source: https://ripon.edu/admission/cost-and-financial-aid/scholarships-and-aid/fine-art-scholarships/ (sha256 887408eb4b46)
- checks: {"thresholds": null}
  - eligibility_summary: Two contrasting pieces or sections of pieces of music (approx. 2–4 minutes) 2 octaves of any major or minor scale; can be played with both hands in unison or separate ⟵ “Piano or Organ | Two contrasting pieces or sections of pieces of music (approx. 2–4 minutes) 2 octaves of any major or minor scale; can be played with both hands in unison or separate”
### `md4210f4cbbbf0dd` Ripon College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://ripon.edu/admission/apply/transfer-applicants/ (sha256 f2300ce8149a)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “As a rule of thumb, all college-level coursework in a liberal arts and sciences discipline will be accepted as transfer credits provided the courses were completed at an accredited college and a grade of C- or higher was earned.”
  - min_grade: C- ⟵ “As a rule of thumb, all college-level coursework in a liberal arts and sciences discipline will be accepted as transfer credits provided the courses were completed at an accredited college and a grade of C- or higher was earned.”
### `1addbda5e18ce69a` Saint Norbert College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://snc.edu/admissions/tuition-and-fees (sha256 709786e220fb)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - off_campus_not_with_family:Tuition for full-time undergraduate: 46880 ⟵ “Tuition for full-time undergraduate | $46,880”
  - off_campus_not_with_family:Fees: 960 ⟵ “Fees | $960”
  - off_campus_not_with_family:Total yearly direct cost: 47840 ⟵ “Total yearly direct cost | $47,840”
### `2477e7be60c7ca8f` Southwest Wisconsin Technical College — transfer_policies 2028-29 [new] (labeled_in_source)
- source: https://www.swtc.edu/uploadedpdfs/academic/transfer/agreement-documents/Milwaukee-School-of-Engineering-Any-Program-to-Business-Management.pdf (sha256 c5310d6708af)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “MSOE will assemble lists of Social Sciences (SS), Humanities (HU), and other elective courses from WTCS that are approved to transfer under this transfer agreement if taken and successfully completed with a grade of C or better.”
### `5f1b2bedb0c31db3` University of Wisconsin-La Crosse — costs 2027-28 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.uwlax.edu/cost/ (sha256 983b6ea18d4b)
- checks: {"columns": 1, "rows": 3}
  - on_campus:Tuition/Fees: 21109 ⟵ “Tuition/Fees | $10,993 | $11,927 | $21,109 | $15,453 | $16,349 | $10,993/11,927”
  - on_campus:Housingtraditional double: 4980 ⟵ “Housingtraditional double | $4,980 | $4,980 | $4,980 | $4,980 | $4,980 | 0”
  - on_campus:TOTALSdivide in half for per semester costs: 29559 ⟵ “TOTALSdivide in half for per semester costs | $19,443 | $20,377 | $29,559 | $23,903 | $24,799 | $10,993/11,927”
### `18d03eeba922b79e` University of Wisconsin-La Crosse — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.uwlax.edu/admissions/credit-for-prior-learning/ (sha256 49c2784514fc)
- checks: {"distinct_exams": 34, "equivalencies": 56, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, 5]:  ⟵ “African American History | 3, 4, 5 | Elective Credit | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art & Design: 2-D | 3 | Elective Credit | 3”
  - equivalencies[AP-2-D-ART-DESIGN|4, 5]:  ⟵ “Art & Design: 2-D | 4, 5 | Art 160*** | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art & Design: 3-D | 3 | Elective Credit | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4, 5]:  ⟵ “Art & Design: 3-D | 4, 5 | Art 160*** | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing | 3 | Elective Credit | 3”
  - equivalencies[AP-DRAWING|4, 5]:  ⟵ “Drawing | 4, 5 | Art 162 | 4”
  - equivalencies[AP-ART-HISTORY|3, 4, 5]:  ⟵ “Art History | 3, 4, 5 | Art 251*** | 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | Biology 100*** | 4”
  - equivalencies[AP-BIOLOGY|4, 5]:  ⟵ “Biology | 4, 5 | Biology 105*** | 4”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | Math 175***; Placement into MTH 207 | 4”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB | 4, 5 | Math 207*** | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | Math 207*** | 4”
  - equivalencies[AP-CALCULUS-BC|4,5]:  ⟵ “Calculus BC | 4,5 | Math 207*** & 208 | 8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | Elective Credit | 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | Chemistry 103*** | 5”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | Chemistry 103/104 | 10”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | Chinese 202*** | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4, 5]:  ⟵ “Chinese Language and Culture | 4, 5 | Chinese 202***, 398Placement in 300+ course* | 7”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | Elective Credit | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “Computer Science A | 4, 5 | Computer Science 120*** | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | Computational Thinking 100*** | 3”
  - equivalencies[AP-MACROECONOMICS|3, 4, 5]:  ⟵ “Economics: Macro | 3, 4, 5 | Economics 120*** | 3”
  - equivalencies[AP-MICROECONOMICS|3, 4, 5]:  ⟵ “Economics: Micro | 3, 4, 5 | Economics 110*** | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | Elective CreditSatisfies GEN ED 1012 | 3”
  - … 31 more rows
### `dcf4a9a5c41c3ba2` University of Wisconsin-Parkside — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.uwp.edu/apply/admissions/other/earlycollegecredit/ (sha256 97a9c5b10511)
- checks: {"fields": [], "tiers": 3}
  - eligibility_tier: 2.33 ⟵ “2. A cumulative UW-Parkside GPA of 2.33 or higher;”
  - eligibility_tier: 2.0 ⟵ “3. A cumulative unweighted high school GPA of 2.0 or higher; and”
  - eligibility_tier: 2.5 ⟵ “Students with a 2.5 GPA should apply but we encourage all students interested to submit an application!”
### `69336d4e5da08fe4` University of Wisconsin-Platteville — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uwplatt.edu/department/financial-aid-scholarships/loans (sha256 1fb8f42318da)
- checks: {"thresholds": null}
  - award_amount_text: $6,500 ⟵ “Sophomore | $4,500 | $2,000 | $6,500”
### `b64c1d75d796fdda` University of Wisconsin-Platteville — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uwplatt.edu/department/financial-aid-scholarships/loans (sha256 1fb8f42318da)
- checks: {"thresholds": null}
  - award_amount_text: $7,500 ⟵ “Junior/Senior | $5,500 | $2,000 | $7,500”
### `d7c018c85bec9514` University of Wisconsin-Platteville — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uwplatt.edu/department/financial-aid-scholarships/loans (sha256 1fb8f42318da)
- checks: {"thresholds": null}
  - award_amount_text: $31,000 (no more than $23,000 can be subsidized) ⟵ “Aggregate Borrowing Limit |  |  | $31,000 (no more than $23,000 can be subsidized)”
### `e8cd21638cf6d0c9` University of Wisconsin-Platteville — awards 2026-27 [new] (labeled_in_source)
- source: https://www.uwplatt.edu/department/financial-aid-scholarships/loans (sha256 1fb8f42318da)
- checks: {"thresholds": null}
  - award_amount_text: $5,500 ⟵ “Freshman | $3,500 | $2,000 | $5,500”
### `18d0dba06bd54151` University of Wisconsin-Platteville — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.uwplatt.edu/undergraduate/admission-prior-credits/credits-by-examination/ (sha256 3eee37329c72)
- checks: {"distinct_exams": 42, "equivalencies": 62, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3,4,5]:  ⟵ “African American Studies | 3,4,5 | 3 | ETHNSTDY 1000T - Elective Credit*”
  - equivalencies[AP-ART-HISTORY|3,4,5]:  ⟵ “Art History | 3,4,5 | 3 | ART 2430”
  - equivalencies[AP-DRAWING|3,4,5]:  ⟵ “Studio Art: Drawing | 3,4,5 | 3 | ART 1010”
  - equivalencies[AP-2-D-ART-DESIGN|3,4,5]:  ⟵ “Studio Art: 2-D Design | 3,4,5 | 3 | ART 1420”
  - equivalencies[AP-3-D-ART-DESIGN|3,4,5]:  ⟵ “Studio Art: 3-D Design | 3,4,5 | 3 | ART 1520”
  - equivalencies[AP-BIOLOGY|3,4]:  ⟵ “Biology | 3,4 | 5 | BIOLOGY 1150”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “Biology | 5 | 5 | BIOLOGY 1150 or BIOLOGY 1650”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3, 4, 5]:  ⟵ “Business with Personal Finance | 3, 4, 5 |  | Please contact the campus with questions on credit equivalencies.”
  - equivalencies[AP-CYBERSECURITY|3, 4, 5]:  ⟵ “Cybersecurity | 3, 4, 5 |  | Please contact the campus with questions on credit equivalencies.”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 5 | CHEMSTRY 1050”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 4-5 | CHEMSTRY 1140 or CHEMSTRY 1450”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | 5 | 5-8 | CHEMSTRY 1140 and CHEMSTRY 1240 or CHEMSTRY 1450”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3,4,5]:  ⟵ “Chinese Language and Culture | 3,4,5 |  | See Humanities Department”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3,4,5]:  ⟵ “Computer Science A | 3,4,5 | 3 | COMPUTER 1430”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3,4,5]:  ⟵ “Computer Science Principles | 3,4,5 | 3 | COMPUTER 1130”
  - equivalencies[AP-MACROECONOMICS|3,4,5]:  ⟵ “Macroeconomics | 3,4,5 | 3 | ECONOMIC 2130”
  - equivalencies[AP-MICROECONOMICS|3,4,5]:  ⟵ “Microeconomics | 3,4,5 | 3 | ECONOMIC 2230”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3,4]:  ⟵ “English Language and Composition | 3,4 | 3 | ENGLISH 1130”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Language and Composition | 5 | 6 | ENGLISH 1130, ENGLISH 1230”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | 3 | ENGLISH 1330”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4,5]:  ⟵ “English Literature and Composition | 4,5 | 6 | ENGLISH 1130 and ENGLISH 1330”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3,4,5]:  ⟵ “Environmental Science | 3,4,5 | 4 | BIOLOGY 1910”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | 3 | 8 | FRENCH 1040, FRENCH 1140”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture | 4 | 12 | FRENCH 1040, FRENCH 1140, FRENCH 2040”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language and Culture | 5 | 16 | FRENCH 1040, FRENCH 1140, FRENCH 2040, FRENCH 2140”
  - … 37 more rows
### `6ab1646cb39a6225` University of Wisconsin-Platteville — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.uwplatt.edu/undergraduate/admission-prior-credits/credits-by-examination/ (sha256 3eee37329c72)
- checks: {"distinct_exams": 16, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 3 | ENGLISH 2100”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 | ENGLISH 1330”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 | ENGLISH 1130”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 3 | ENGLISH 2100”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language: Level 1 | 50 | 4 | FRENCH 1040”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language: Level 2 | 59 | 12 | FRENCH 1140, FRENCH 2040, FRENCH 2140”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language: Level 1 | 50 | 4 | GERMAN 1240”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language: Level 2 | 60 | 12 | GERMAN 1340, GERMAN 2240, GERMAN 2340”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language: Level 1 | 50 | 4 | SPANISH 1840”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish Language: Level 2 | 63 | 12 | SPANISH 1940, SPANISH 2840, SPANISH 2940”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “History And Social Sciences || American Government | 50 | 3 | POLISCI 1230”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 5 | BIOLOGY 1150”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|65]:  ⟵ “College Algebra | 65 | 3 | MATH 1530”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|65]:  ⟵ “College Mathematics | 65 | 3 | MATH 1620”
  - equivalencies[CLEP-PRECALCULUS|65]:  ⟵ “Precalculus | 65 | 5 | MATH 2450”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 | ACCTING 2010”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Business Law, Introductory | 50 | 3 | BUSADMIN 3130”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of | 50 | 3 | BUSADMIN 2330”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | 50 | 3 | BUSADMIN 2630”
### `7654d168ddab82f1` University of Wisconsin-Superior — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://uwsuper.edu/paying-for-college/tuition-and-fees/fall-and-spring/ (sha256 5334270a5b77)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees: 9480 ⟵ “Tuition and Fees | 9,480 | 11,360 | 17,950”
  - on_campus:Living Expenses (Housing and Meals): 11410 ⟵ “Living Expenses (Housing and Meals) | 11,410 | 11,410 | 11,410”
  - on_campus:Books and Course Materials: 1170 ⟵ “Books and Course Materials | 1,170 | 1,170 | 1,170”
  - on_campus:Transportation: 1680 ⟵ “Transportation | 1,680 | 1,680 | 1,680”
  - on_campus:Personal/Misc: 1400 ⟵ “Personal/Misc | 1,400 | 1,400 | 1,400”
  - on_campus:Loan Fees: 80 ⟵ “Loan Fees | 80 | 80 | 80”
  - on_campus:Total: 25220 ⟵ “Total | 25,220 | 27,100 | 33,690”
### `76960de1f42c38ac` University of Wisconsin-Superior — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://uwsuper.edu/paying-for-college/tuition-and-fees/fall-and-spring/ (sha256 5334270a5b77)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees: 17950 ⟵ “Tuition and Fees | 9,480 | 11,360 | 17,950”
  - on_campus:Living Expenses (Housing and Meals): 11410 ⟵ “Living Expenses (Housing and Meals) | 11,410 | 11,410 | 11,410”
  - on_campus:Books and Course Materials: 1170 ⟵ “Books and Course Materials | 1,170 | 1,170 | 1,170”
  - on_campus:Transportation: 1680 ⟵ “Transportation | 1,680 | 1,680 | 1,680”
  - on_campus:Personal/Misc: 1400 ⟵ “Personal/Misc | 1,400 | 1,400 | 1,400”
  - on_campus:Loan Fees: 80 ⟵ “Loan Fees | 80 | 80 | 80”
  - on_campus:Total: 33690 ⟵ “Total | 25,220 | 27,100 | 33,690”
### `4b0381e9a9863b96` University of Wisconsin-Superior — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://uwsuper.edu/admissions/how-to-apply/transfer-center/transfer-credits/ (sha256 fd791e84360e)
- checks: {"fields": ["min_grade"]}
  - min_grade: D- ⟵ “Students can transfer courses from an accredited college, university or community college with a grade of “D-” or higher.”
### `02436c4cf794baf2` Waukesha County Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.wctc.edu/WCTC/Academics/High-School-Dual-Credit/Dual-Enrollment-Academy (sha256 31f04148f614)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “Have a minimum 2.0 GPA or letter of recommendation from your counselor.”
### `0753012a42981fe4` Waukesha County Technical College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.wctc.edu/WCTC/OffNav/Credit-by-Examination-Policy (sha256 edb8cf8d01c2)
- checks: {"distinct_exams": 5, "equivalencies": 5, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | 806-114 General Biology”
  - equivalencies[IB-ECONOMICS|4 HL]:  ⟵ “Economics | 4 HL | 809-195 Economics”
  - equivalencies[IB-PSYCHOLOGY|4 HL]:  ⟵ “Psychology | 4 HL | 809-198 Intro to Psychology”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4 HL]:  ⟵ “Social Cultural Anthropology | 4 HL | 809-196 Intro to Sociology”
  - equivalencies[IB-FRENCH|4 HL or 5 SL]:  ⟵ “Foreign Language (Spanish ab initio, Spanish B, Mandarin ab initio, or French ab initio) | 4 HL or 5 SL | 802-991 World Language Elective”
### `fd08bfa3f4cca598` Waukesha County Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.wctc.edu/WCTC/OffNav/Credit-by-Examination-Policy (sha256 edb8cf8d01c2)
- checks: {"distinct_exams": 22, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “AP African American Studies | 3 | 803-215 African American History”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “AP Biology | 3 | 806-114 General Biology”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “AP Calculus AB | 3 | 804-198 Calculus 1”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “AP Calculus BC | 3 | 804-198 Calculus 1 and 804-156 Calculus 2”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “AP Precalculus | 3 | 804-197 College Algebra and Trig. w/Apps”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “AP Chemistry | 3 | 806-134 General Chemistry”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “AP Computer Science A | 3 | 152-112 Intro to Programming in C# and 152-130 Intro to Java”
  - equivalencies[AP-CYBERSECURITY|3]:  ⟵ “AP Cybersecurity | 3 | 151-106 Security 1”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language and Composition | 3 | 801-136 English Composition 1”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “AP Macroeconomics | 3 | 809-287 Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “AP Microeconomics | 3 | 809-143 Microeconomics”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “AP Physics 1: Algebra-Based | 3 | 806-143 College Physics 1”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “AP Physics 2: Algebra-Based | 3 | 806-144 College Physics 2”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “AP Physics C: Electricity and Magnetism | 3 | 806-188 Calc Based Physics 2”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “AP Physics C: Mechanics | 3 | 806-187 Calc Based Physics 1”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “AP Psychology | 3 | 809-198 Intro to Psychology”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research | 3 | 801-223 English Composition 2”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar | 3 | 801-136 English Composition 1”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “AP Statistics | 3 | 804-189 Introductory Statistics”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “AP 2-D Art and Design | 3 | 201-118 Design Drawing & Color Theory”
  - equivalencies[AP-DRAWING|3]:  ⟵ “AP Drawing | 3 | 201-118 Design Drawing & Color Theory”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “AP United States Government and Politics | 3 | 809-227 American Government”
### `95a38035052b950c` Wisconsin Lutheran College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.wlc.edu/admissions/undergraduate/early-college-credit-program.html (sha256 bc47e9897593)
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 0}
  - max_credit_hours_per_term: 9 ⟵ “Early College Credit Program students may take up to 9 credits per semester. Students can take up to a total of 18 credits while participating in the ECCP.”

## Exceptions (199)

### `1e2efaa974cdffa6` state-WI — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://heab.state.wi.us/features/decr.html (sha256 ed35056cf0a3)
- issues: semantic_review_required, conflicting_sources:https://heab.state.wi.us,https://heab.state.wi.us/features/aes.html,https://heab.state.wi.us/features/dsp.html
- checks: {"requirements": 4}
  - statements.requirements: 4 ⟵ “WI Higher Educational Aids Board - Dual Enrollment Credential Grant Primary Care and Psychiatry Shortage Grant Veteran's Grant for Private Non-Profit Schools 2017 Wisconsin Act 206 created the Dual Enrollment Credential Grant to assist high school teachers to meet the minimum qualification requireme”
### `41e3678c1c0cc281` state-WI — state_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://heab.state.wi.us/features/dsp.html (sha256 0cf0525680fd)
- issues: semantic_review_required, conflicting_sources:https://heab.state.wi.us,https://heab.state.wi.us/features/aes.html,https://heab.state.wi.us/features/decr.html
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “Students are eligible to apply if they are Wisconsin residents and all of the following: are currently in a Dental Health Training Program at the Marquette University School of Dentistry to become a dentist. intend to practice in a designated Dental Health Shortage Area in Wisconsin, which does not ”
### `6b843f60905e791f` state-WI — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://heab.state.wi.us/features/aes.html (sha256 752a6d59f2b5)
- issues: semantic_review_required, conflicting_sources:https://heab.state.wi.us,https://heab.state.wi.us/features/decr.html,https://heab.state.wi.us/features/dsp.html
- checks: {"requirements": 6}
  - statements.requirements: 6 ⟵ “The number of scholarships each high school is eligible for is based on total student enrollment grades 9-12.”
### `8362b44adc19b7ae` state-WI — state_policies 2015-16 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://heab.state.wi.us/features/tes.html (sha256 1db64a59e230)
- issues: stale_year_label:2015-16, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Eligible students must attend one of the following Wisconsin Technical Colleges to qualify for TES funding.”
### `e6c9d97f30c7097f` state-WI — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://heab.state.wi.us (sha256 9e9fef63a377)
- issues: semantic_review_required, conflicting_sources:https://heab.state.wi.us/features/aes.html,https://heab.state.wi.us/features/decr.html,https://heab.state.wi.us/features/dsp.html
- checks: {"requirements": 4}
  - statements.requirements: 4 ⟵ “Primary Care and Psychiatry Shortage Grant Emergency Medical Service Education Reimbursement Veteran's Grant for Private Non-Profit Schools The Higher Educational Aids Board (HEAB) is the state agency responsible for the management and oversight of the state's student financial aid system for Wiscon”
### `44a779a053ec6b72` Bellin College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bellincollege.edu/admissions/financial-aid-and-scholarships/financial-aid-counseling/ (sha256 24cbee4e52fd)
- issues: semantic_review_required, conflicting_sources:https://www.bellincollege.edu/admissions/financial-aid-and-scholarships/financial-aid-professional-judgement/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If you feel the allowance reflected in your COA does not sufficiently reflect your housing expenses, you may request a Professional Judgement appeal through the financial aid office.”
  - sentence: professional_judgment ⟵ “Related Links Applying for Financial Aid Financial Aid Counseling Financial Aid Professional Judgement Grad Ready (Financial Literacy) Net Price Calculator Scholarships Related Links Applying for Financial Aid Financial Aid Counseling Financial Aid Professional Judgement Grad Ready (Financial Literacy) Net Price Calculator Scholarships 3201 Eaton Rd, Green Bay, WI 54311 (920) 433-6699 Employment O”
### `6bfa6a8da66328f2` Bellin College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bellincollege.edu/admissions/financial-aid-and-scholarships/financial-aid-professional-judgement/ (sha256 c754d9a59c09)
- issues: semantic_review_required, conflicting_sources:https://www.bellincollege.edu/admissions/financial-aid-and-scholarships/financial-aid-counseling/
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: professional_judgment ⟵ “Professional Judgement decisions are made based on documentation and information provided by the student and/or the student’s parent(s).”
  - sentence: professional_judgment ⟵ “PROCEDURE: If a student believes that the financial and/or other data reported on the FAFSA or used to determine the student’s eligibility for financial aid, is not an accurate reflection of the student’s/family’s financial situation, the student may request consideration for a Professional Judgement through the Bellin College financial aid office.”
  - sentence: professional_judgment ⟵ “Complete the Request for Financial Aid Professional Judgement form which is available from the financial aid office.”
  - sentence: professional_judgment ⟵ “Failure to comply with this deadline will result in a denial of the request for professional judgement.”
  - sentence: professional_judgment ⟵ “For approved Professional Judgement requests, the student will be notified via e-mail within ten (10) business days after the corrections/adjustments have been made.”
  - sentence: professional_judgment ⟵ “Per DOE regulations, the original Request for Financial Aid Professional Judgement form as well as all supporting documentation and communications will be maintained in the student’s file (paper or electronic) for a minimum of three (3) years after the student is no longer enrolled at Bellin College.”
### `9dc59403fe2f85e1` Bellin College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bellincollege.edu/admissions/financial-aid-and-scholarships/ (sha256 bbd4e72da2f4)
- issues: semantic_review_required, conflicting_sources:https://www.bellincollege.edu/admissions/financial-aid-and-scholarships/net-price-calculator/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If your family experiences any unusual circumstances which cannot be properly reported on the FAFSA that you, or your parents, feel impact the family’s ability to finance your education, you (or your parent) should contact the financial aid office to discuss if those circumstances may qualify for special consideration.”
### `9eb86f523340e9e3` Bellin College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bellincollege.edu/admissions/financial-aid-and-scholarships/net-price-calculator/ (sha256 32756b4e9d8f)
- issues: semantic_review_required, conflicting_sources:https://www.bellincollege.edu/admissions/financial-aid-and-scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The calculator does not consider any special circumstances.”
### `076d8b1728f76b7b` Bellin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-15-Month-2026-2027.pdf (sha256 041fc810dd0f)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.bellincollege.edu/admissions/tuition-fees/bsn-15-month-option/,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-Transfer-Fall-Start-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSRT-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSSA-3-Year-2026-2027.pdf
- checks: {"columns": 8, "rows": 8}
  - column:Tuition: 10233 ⟵ “Tuition | $10,233 | $11,370 | $10,233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768”
  - column:$545: 490 ⟵ “$545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870”
  - column:$10,778: 11860 ⟵ “$10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724”
  - column:Total Tuition and Fees - Bachelor of Science in Nursing: 76638 ⟵ “Total Tuition and Fees - Bachelor of Science in Nursing | $76,638 | 64 nursing credits”
  - column:Tuition (2): 10233 ⟵ “Tuition | $10,233 | $11,370 | $10,233 | $10,233 | $10,233 | $10,233 | $10,233 | $72,768”
  - column:$545 (2): 490 ⟵ “$545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870”
  - column:$10,778 (2): 11860 ⟵ “$10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $10,778 | $10,998”
  - column:Total Tuition and Fees - Bachelor of Science in Nursing (2): 76638 ⟵ “Total Tuition and Fees - Bachelor of Science in Nursing | $76,638 | 64 nursing credits”
  - column:Tuition: 11370 ⟵ “Tuition | $10,233 | $11,370 | $10,233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768”
  - column:$545: 490 ⟵ “$545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870”
  - column:$10,778: 10723 ⟵ “$10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724”
  - column:Tuition (2): 11370 ⟵ “Tuition | $10,233 | $11,370 | $10,233 | $10,233 | $10,233 | $10,233 | $10,233 | $72,768”
  - column:$545 (2): 490 ⟵ “$545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870”
  - column:$10,778 (2): 10723 ⟵ “$10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $10,778 | $10,998”
  - column:Tuition: 10233 ⟵ “Tuition | $10,233 | $11,370 | $10,233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768”
  - column:$545: 545 ⟵ “$545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870”
  - column:$10,778: 10778 ⟵ “$10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724”
  - column:Tuition (2): 10233 ⟵ “Tuition | $10,233 | $11,370 | $10,233 | $10,233 | $10,233 | $10,233 | $10,233 | $72,768”
  - column:$545 (2): 545 ⟵ “$545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870”
  - column:$10,778 (2): 10778 ⟵ “$10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $10,778 | $10,998”
  - column:Tuition: 10233 ⟵ “Tuition | $10,233 | $11,370 | $10,233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768”
  - column:$545: 490 ⟵ “$545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870”
  - column:$10,778: 10723 ⟵ “$10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724”
  - column:Tuition (2): 10233 ⟵ “Tuition | $10,233 | $11,370 | $10,233 | $10,233 | $10,233 | $10,233 | $10,233 | $72,768”
  - column:$545 (2): 490 ⟵ “$545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870”
  - … 19 more rows
### `09f6743d08951383` Bellin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-Transfer-Fall-Start-2026-2027.pdf (sha256 469e3b48e857)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.bellincollege.edu/admissions/tuition-fees/bsn-15-month-option/,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-15-Month-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSRT-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSSA-3-Year-2026-2027.pdf
- checks: {"columns": 4, "components_reconcile": false, "rows": 5}
  - column:$17,115: 18192 ⟵ “$17,115 | $18,192 | $10,293 | $1,740 | $47,340”
  - column:$14,841: 15918 ⟵ “$14,841 | $15,918 | - | $1,435 | $32,194”
  - column:Tuition and Fees – Nursing Courses: 75943 ⟵ “Tuition and Fees – Nursing Courses | $75,943 | 64 credits”
  - column:Tuition and Fees - General Education Courses: 3591 ⟵ “Tuition and Fees - General Education Courses | $3,591 | 9 credits”
  - column:Total Tuition and Fees - Bachelor of Science in Nursing: 79534 ⟵ “Total Tuition and Fees - Bachelor of Science in Nursing | $79,534 | 73 credits”
  - column:$17,115: 10293 ⟵ “$17,115 | $18,192 | $10,293 | $1,740 | $47,340”
  - column:$17,115: 1740 ⟵ “$17,115 | $18,192 | $10,293 | $1,740 | $47,340”
  - column:$14,841: 1435 ⟵ “$14,841 | $15,918 | - | $1,435 | $32,194”
  - column:$17,115: 47340 ⟵ “$17,115 | $18,192 | $10,293 | $1,740 | $47,340”
  - column:$14,841: 32194 ⟵ “$14,841 | $15,918 | - | $1,435 | $32,194”
### `3c002370c38383b8` Bellin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bellincollege.edu/admissions/tuition-fees/bsn-15-month-option/ (sha256 9ee2781f0123)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-15-Month-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-Transfer-Fall-Start-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSRT-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSSA-3-Year-2026-2027.pdf
- checks: {"columns": 8, "rows": 4}
  - column:Nursing Tuition: 10233 ⟵ “Nursing Tuition | $10,233 | $11,370 | $10.233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768 | ”
  - column:Fees: 545 ⟵ “Fees | $545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870 | ”
  - column:Total: 10778 ⟵ “Total | $10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724 |  | ”
  - column:Total Tuition and Fees – Bachelor of Science in Nursing: 76638 ⟵ “Total Tuition and Fees – Bachelor of Science in Nursing | $76,638 | 64 nursing credits”
  - column:Nursing Tuition: 11370 ⟵ “Nursing Tuition | $10,233 | $11,370 | $10.233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768 | ”
  - column:Fees: 490 ⟵ “Fees | $545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870 | ”
  - column:Total: 11860 ⟵ “Total | $10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724 |  | ”
  - column:Nursing Tuition: 10.233 ⟵ “Nursing Tuition | $10,233 | $11,370 | $10.233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768 | ”
  - column:Fees: 490 ⟵ “Fees | $545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870 | ”
  - column:Total: 10723 ⟵ “Total | $10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724 |  | ”
  - column:Nursing Tuition: 10233 ⟵ “Nursing Tuition | $10,233 | $11,370 | $10.233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768 | ”
  - column:Fees: 545 ⟵ “Fees | $545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870 | ”
  - column:Total: 10778 ⟵ “Total | $10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724 |  | ”
  - column:Nursing Tuition: 10233 ⟵ “Nursing Tuition | $10,233 | $11,370 | $10.233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768 | ”
  - column:Fees: 490 ⟵ “Fees | $545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870 | ”
  - column:Total: 10723 ⟵ “Total | $10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724 |  | ”
  - column:Nursing Tuition: 12507 ⟵ “Nursing Tuition | $10,233 | $11,370 | $10.233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768 | ”
  - column:Fees: 545 ⟵ “Fees | $545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870 | ”
  - column:Total: 13052 ⟵ “Total | $10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724 |  | ”
  - column:Nursing Tuition: 7959 ⟵ “Nursing Tuition | $10,233 | $11,370 | $10.233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768 | ”
  - column:Fees: 765 ⟵ “Fees | $545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870 | ”
  - column:Total: 8724 ⟵ “Total | $10,778 | $11,860 | $10,723 | $10,778 | $10,723 | $13,052 | $8,724 |  | ”
  - column:Nursing Tuition: 72768 ⟵ “Nursing Tuition | $10,233 | $11,370 | $10.233 | $10,233 | $10,233 | $12,507 | $7,959 | $72,768 | ”
  - column:Fees: 3870 ⟵ “Fees | $545 | $490 | $490 | $545 | $490 | $545 | $765 | $3,870 | ”
### `e24779c7b0cc6dd3` Bellin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSSA-3-Year-2026-2027.pdf (sha256 f3a7319615a7)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.bellincollege.edu/admissions/tuition-fees/bsn-15-month-option/,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-15-Month-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-Transfer-Fall-Start-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSRT-2026-2027.pdf
- checks: {"columns": 4, "components_reconcile": false, "rows": 6}
  - column:$6,219: 6804 ⟵ “$6,219 | $6,804 | $7,038 | $1,600 | $21,661”
  - column:$6,405: 7203 ⟵ “$6,405 | $7,203 | $7,389 | $1,625 | $22,622”
  - column:$7,038: 7038 ⟵ “$7,038 | $7,038 | $1,420 | $15,496”
  - column:Tuition and Fees – Surgical Assisting Courses: 36247 ⟵ “Tuition and Fees – Surgical Assisting Courses | $36,247 | 62 credits”
  - column:Tuition and Fees - General Education Courses: 23532 ⟵ “Tuition and Fees - General Education Courses | $23,532 | 58 credits”
  - column:Total Tuition and Fees - Bachelor of Science in Surgical Assisting: 59779 ⟵ “Total Tuition and Fees - Bachelor of Science in Surgical Assisting | $59,779 | 120 credits”
  - column:$6,219: 7038 ⟵ “$6,219 | $6,804 | $7,038 | $1,600 | $21,661”
  - column:$6,405: 7389 ⟵ “$6,405 | $7,203 | $7,389 | $1,625 | $22,622”
  - column:$7,038: 1420 ⟵ “$7,038 | $7,038 | $1,420 | $15,496”
  - column:$6,219: 1600 ⟵ “$6,219 | $6,804 | $7,038 | $1,600 | $21,661”
  - column:$6,405: 1625 ⟵ “$6,405 | $7,203 | $7,389 | $1,625 | $22,622”
  - column:$7,038: 15496 ⟵ “$7,038 | $7,038 | $1,420 | $15,496”
  - column:$6,219: 21661 ⟵ “$6,219 | $6,804 | $7,038 | $1,600 | $21,661”
  - column:$6,405: 22622 ⟵ “$6,405 | $7,203 | $7,389 | $1,625 | $22,622”
### `f7068766fa3ea605` Bellin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSRT-2026-2027.pdf (sha256 83d397e9ab82)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.bellincollege.edu/admissions/tuition-fees/bsn-15-month-option/,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-15-Month-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSN-Transfer-Fall-Start-2026-2027.pdf,https://www.bellincollege.edu/wp-content/uploads/2026/05/Tuition-and-Fees-BSSA-3-Year-2026-2027.pdf
- checks: {"columns": 6, "components_reconcile": false, "rows": 4}
  - column:Year Three: 13644 ⟵ “Year Three | $13,644 | $3,411 | $13,644 | $5,685 | $1,630 | $38,014”
  - column:Tuition and Fees – Radiation Therapy Courses: 77995 ⟵ “Tuition and Fees – Radiation Therapy Courses | $77,995 | 65 credits”
  - column:Tuition and Fees - General Education Courses: 22255 ⟵ “Tuition and Fees - General Education Courses | $22,255 | 55 credits”
  - column:Total Tuition and Fees - Bachelor of Science in Radiation Therapy: 100250 ⟵ “Total Tuition and Fees - Bachelor of Science in Radiation Therapy | $100,250 | 120 credits”
  - column:$7,860: 10074 ⟵ “$7,860 | - | $10,074 | $7,062 | $1,540 | $26,536”
  - column:$11,490: 12627 ⟵ “$11,490 | - | $12,627 | $10,353 | $1,230 | $35,700”
  - column:Year Three: 3411 ⟵ “Year Three | $13,644 | $3,411 | $13,644 | $5,685 | $1,630 | $38,014”
  - column:$7,860: 7062 ⟵ “$7,860 | - | $10,074 | $7,062 | $1,540 | $26,536”
  - column:$11,490: 10353 ⟵ “$11,490 | - | $12,627 | $10,353 | $1,230 | $35,700”
  - column:Year Three: 13644 ⟵ “Year Three | $13,644 | $3,411 | $13,644 | $5,685 | $1,630 | $38,014”
  - column:$7,860: 1540 ⟵ “$7,860 | - | $10,074 | $7,062 | $1,540 | $26,536”
  - column:$11,490: 1230 ⟵ “$11,490 | - | $12,627 | $10,353 | $1,230 | $35,700”
  - column:Year Three: 5685 ⟵ “Year Three | $13,644 | $3,411 | $13,644 | $5,685 | $1,630 | $38,014”
  - column:$7,860: 26536 ⟵ “$7,860 | - | $10,074 | $7,062 | $1,540 | $26,536”
  - column:$11,490: 35700 ⟵ “$11,490 | - | $12,627 | $10,353 | $1,230 | $35,700”
  - column:Year Three: 1630 ⟵ “Year Three | $13,644 | $3,411 | $13,644 | $5,685 | $1,630 | $38,014”
  - column:Year Three: 38014 ⟵ “Year Three | $13,644 | $3,411 | $13,644 | $5,685 | $1,630 | $38,014”
### `dbae8de6f3e5cac6` Bellin College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.bellincollege.edu/admissions/undergraduate-admissions/transfer-students/transfer-guides/advanced-placement/ (sha256 753d6c1caa82)
- issues: course_column_missing
- checks: {"distinct_exams": 22, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3, 4, 5]:  ⟵ “Art, Studio (Drawing Portfolio) | 3, 4, 5 | Humanities | 3”
  - equivalencies[AP-2-D-ART-DESIGN|3, 4, 5]:  ⟵ “Art, Studio (2-D Design) | 3, 4, 5 | Humanities | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3, 4, 5]:  ⟵ “Art, Studio (3-D Design) | 3, 4, 5 | Humanities | 3”
  - equivalencies[AP-CHEMISTRY|3, 4, 5]:  ⟵ “Chemistry | 3, 4, 5 | Chemistry | 4”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “Chinese Lang & Cult | 3, 4, 5 | Humanities or Diversity | 3”
  - equivalencies[AP-MACROECONOMICS|3, 4, 5]:  ⟵ “Economics, Macro or Micro | 3, 4, 5 | Business | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3,4,5]:  ⟵ “Environmental Science | 3,4,5 | Social Science | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3, 4, 5]:  ⟵ “European History # | 3, 4, 5 | Humanities or Diversity | 3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “French Language & Culture | 3, 4, 5 | Humanities or Diversity | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “German Language | 3, 4, 5 | Humanities or Diversity | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3, 4, 5]:  ⟵ “Human Geography | 3, 4, 5 | Social Science or Diversity | 3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “Italian Language &Culture | 3, 4, 5 | Humanities or Diversity | 3”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “Japanese Language & Culture | 3, 4, 5 | Humanities or Diversity | 3”
  - equivalencies[AP-LATIN|3, 4, 5]:  ⟵ “Latin: Vergil or Literature | 3, 4, 5 | Humanities | 3”
  - equivalencies[AP-CALCULUS-AB|3, 4, 5]:  ⟵ “Math: Calculus AB, BC | 3, 4, 5 | Math | 3”
  - equivalencies[AP-MUSIC-THEORY|3, 4, 5]:  ⟵ “Music Theory | 3, 4, 5 | Humanities | 3”
  - equivalencies[AP-PSYCHOLOGY|3, 4, 5]:  ⟵ “Psychology | 3, 4, 5 | Psychology or Social Science | 3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “Spanish Language | 3, 4, 5 | Humanities or Diversity | 3”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3, 4, 5]:  ⟵ “Spanish Literature | 3, 4, 5 | Humanities or Diversity | 3”
  - equivalencies[AP-STATISTICS|3, 4, 5]:  ⟵ “Statistics | 3, 4, 5 | Stats | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3, 4, 5]:  ⟵ “U.S. History # | 3, 4, 5 | Humanities | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3, 4, 5]:  ⟵ “World History # | 3, 4, 5 | Humanities or Diversity | 3”
### `6b70e8ea69b39966` Beloit College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.beloit.edu/live/files/241-satisfactory-academic-progress-policy (sha256 ab29953090b5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal Process Mitigating circumstances are usually beyond a student’s control and can include such things as an injury or illness to himself or a close family member, the death of a close family member, or other special circumstances.”
### `b6a8f7c87f9ecc4e` Beloit College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.beloit.edu/live/files/747-satisfactory-academic-progress-appeal-form (sha256 239dd5cca964)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Beloit College Financial Aid Office Satisfactory Academic Progress Appeal Form ____________ Academic Year Consider this Appeal for: Fall 20____ Spring 20____ Summer 20____ (Write in the year for each semester/term you are requesting your appeal) To be eligible for financial aid, federal regulations require students to maintain Satisfactory Academic Progress (SAP) in three areas: Cumulative GPA, Cr”
  - sentence: sap_appeal ⟵ “If such “mitigating circumstances” can be documented for the specific term(s) when the deficiencies occurred, the student may submit this completed SAP appeal, along with all required documentation.”
  - sentence: sap_appeal ⟵ “Bring the SAP form and appeal letter to your meeting with your academic advisor. 2.”
### `389d070f4675f0cd` Beloit College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.beloit.edu/offices/registrar/transfer-ap-gce-ib-credit/ (sha256 14f163676ef7)
- issues: rows_without_score
- checks: {"distinct_exams": 15, "equivalencies": 15, "rows_without_score": 15}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “African American Studies | Credit for 1 unit of Critical Identity Studies elective, but not CRIS 101”
  - equivalencies[AP-2-D-ART-DESIGN|None]:  ⟵ “Art - 2D Design, 3D Drawing, or Drawing | May replace a 100-level studio art course – see Dept. Chair”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | May replace a 100-level biology course – see Dept. Chair”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB or Calculus AB subscore | Credit for MATH 110”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Calculus BC | Credit for MATH 115”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | Credit (1 unit) for introductory chemistry; may enroll in CHEM 220 or CHEM 230 – see Dept. Chair”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|None]:  ⟵ “Comparative Government and Politics | Credit for POLS 160; may enroll in 200-level POLS courses”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “Computer Science A | Credit for CSCI 111- see Dept. Chair for placement”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “Environmental Science | Credit for introductory natural science requirement for ENVS major”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “Languages, Literatures, and Cultures: Chinese, French, Germain, Italian, Japanese, and Spanish | Follow language placement recommendation from modern languages department”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|None]:  ⟵ “Physics C: Electricity and Magnetism | Credit for PHYS 102”
  - equivalencies[AP-PHYSICS-1|None]:  ⟵ “Physics 1 | Credit for PHYS 101”
  - equivalencies[AP-PSYCHOLOGY|None]:  ⟵ “Psychology | Credit for PSYC 100”
  - equivalencies[AP-STATISTICS|None]:  ⟵ “Statistics | Credit for MATH 106”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|None]:  ⟵ “US Government and Politics | Credit for POLS 110; may enroll in 200-level POLS courses”
### `838c0e41f8dc7e84` Blackhawk Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.blackhawk.edu/Paying-for-College/Cost-of-Attendance (sha256 5721fd8d88fc)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown
- checks: {"columns": 4, "components_reconcile": false, "rows": 6}
  - with_parents_or_family:Tuition and Fees*: 5686 ⟵ “Tuition and Fees* | $5,686 | $5,686 | $5,686 | $5,686”
  - with_parents_or_family:Books, Course Materials, Supplies, and Equipment**: 1464 ⟵ “Books, Course Materials, Supplies, and Equipment** | $1,464 | $1,464 | $1,464 | $1,464”
  - with_parents_or_family:Living Expenses (Food and Housing)**: 3222 ⟵ “Living Expenses (Food and Housing)** | $3,222 | $10,908 | $10,222 | $9,522”
  - with_parents_or_family:Transportation**: 3900 ⟵ “Transportation** | $3,900 | $3,900 | $3,900 | $3,900”
  - with_parents_or_family:Miscellaneous Personal Expenses**: 3804 ⟵ “Miscellaneous Personal Expenses** | $3,804 | $3,804 | $3,804 | $3,804”
  - with_parents_or_family:Total Costs: 17356 ⟵ “Total Costs | $17,356 | $25,042 | $24,356 | $23,656”
  - off_campus_not_with_family:Tuition and Fees*: 5686 ⟵ “Tuition and Fees* | $5,686 | $5,686 | $5,686 | $5,686”
  - off_campus_not_with_family:Books, Course Materials, Supplies, and Equipment**: 1464 ⟵ “Books, Course Materials, Supplies, and Equipment** | $1,464 | $1,464 | $1,464 | $1,464”
  - off_campus_not_with_family:Living Expenses (Food and Housing)**: 10908 ⟵ “Living Expenses (Food and Housing)** | $3,222 | $10,908 | $10,222 | $9,522”
  - off_campus_not_with_family:Transportation**: 3900 ⟵ “Transportation** | $3,900 | $3,900 | $3,900 | $3,900”
  - off_campus_not_with_family:Miscellaneous Personal Expenses**: 3804 ⟵ “Miscellaneous Personal Expenses** | $3,804 | $3,804 | $3,804 | $3,804”
  - off_campus_not_with_family:Total Costs: 25042 ⟵ “Total Costs | $17,356 | $25,042 | $24,356 | $23,656”
  - column:Tuition and Fees*: 5686 ⟵ “Tuition and Fees* | $5,686 | $5,686 | $5,686 | $5,686”
  - column:Books, Course Materials, Supplies, and Equipment**: 1464 ⟵ “Books, Course Materials, Supplies, and Equipment** | $1,464 | $1,464 | $1,464 | $1,464”
  - column:Living Expenses (Food and Housing)**: 10222 ⟵ “Living Expenses (Food and Housing)** | $3,222 | $10,908 | $10,222 | $9,522”
  - column:Transportation**: 3900 ⟵ “Transportation** | $3,900 | $3,900 | $3,900 | $3,900”
  - column:Miscellaneous Personal Expenses**: 3804 ⟵ “Miscellaneous Personal Expenses** | $3,804 | $3,804 | $3,804 | $3,804”
  - column:Total Costs: 24356 ⟵ “Total Costs | $17,356 | $25,042 | $24,356 | $23,656”
  - column:Tuition and Fees*: 5686 ⟵ “Tuition and Fees* | $5,686 | $5,686 | $5,686 | $5,686”
  - column:Books, Course Materials, Supplies, and Equipment**: 1464 ⟵ “Books, Course Materials, Supplies, and Equipment** | $1,464 | $1,464 | $1,464 | $1,464”
  - column:Living Expenses (Food and Housing)**: 9522 ⟵ “Living Expenses (Food and Housing)** | $3,222 | $10,908 | $10,222 | $9,522”
  - column:Transportation**: 3900 ⟵ “Transportation** | $3,900 | $3,900 | $3,900 | $3,900”
  - column:Miscellaneous Personal Expenses**: 3804 ⟵ “Miscellaneous Personal Expenses** | $3,804 | $3,804 | $3,804 | $3,804”
  - column:Total Costs: 23656 ⟵ “Total Costs | $17,356 | $25,042 | $24,356 | $23,656”
### `87e701fe76d6ced1` Bryant & Stratton College-Wauwatosa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bryantstratton.edu/degrees/catalog/financing-your-education/ (sha256 34d1ce5f7fbf)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “There may be unique situations where a student may request a professional judgment to adjust their SAI, dependency status or cost of attendance due to special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “If a student requests a professional judgment and also is selected for verification, the College will require the verification to be completed before exercising any type of professional judgment.”
  - sentence: professional_judgment ⟵ “All professional judgments must be finalized prior to the end of the semester and prior to disbursement of any federal or state student aid.”
### `94127c63606bf36d` Bryant & Stratton College-Wauwatosa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bryantstratton.edu/degrees/catalog/financing-your-education/ (sha256 34d1ce5f7fbf)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: competing_offer_review ⟵ “The ETA program provides up to $6,000 through a combination of a student's TAP award, the ETA award, and a matching award from Bryant & Stratton College.”
### `d8d18b6d242e2b1b` Bryant & Stratton College-Wauwatosa — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.bryantstratton.edu/coronavirus/cares-act/ (sha256 22f6c635ae3c)
- issues: ambiguous_year_labels, components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 15}
  - column:Providing additional emergency financial aid grants to students.: 0 ⟵ “Providing additional emergency financial aid grants to students. | $0”
  - column:Providing reimbursements for tuition, housing, room and board, or other fee refunds.: 0 ⟵ “Providing reimbursements for tuition, housing, room and board, or other fee refunds. | $0”
  - column:Providing tuition discounts.: 0 ⟵ “Providing tuition discounts. | $0”
  - column:Covering the cost of providing additional technology hardware to students, such as laptops or tablets, or covering the added cost of technology fees.: 0 ⟵ “Covering the cost of providing additional technology hardware to students, such as laptops or tablets, or covering the added cost of technology fees. | $0”
  - column:Providing or subsidizing the costs of high-speed internet to students or faculty to transition to an online environment.: 0 ⟵ “Providing or subsidizing the costs of high-speed internet to students or faculty to transition to an online environment. | $0”
  - column:Subsidizing off-campus housing costs due to dormitory closures or decisions to limit housing to one student per room; subsidizing housing costs to reduce housing density; paying for hotels or other off-campus housing for students who need to be isolated; paying travel expenses for students who need to leave campus early due to coronavirus infections or campus interruptions.: 0 ⟵ “Subsidizing off-campus housing costs due to dormitory closures or decisions to limit housing to one student per room; subsidizing housing costs to reduce housing density; paying for hotels or other off-campus housing for students who need t”
  - column:Subsidizing food service to reduce density in eating facilities, to provide pre-packaged meals, or to add hours to food service operations to accommodate social distancing.: 0 ⟵ “Subsidizing food service to reduce density in eating facilities, to provide pre-packaged meals, or to add hours to food service operations to accommodate social distancing. | $0”
  - column:Costs related to operating additional class sections to enable social distancing, such as those for hiring more instructors and increasing campus hours of operations.: 0 ⟵ “Costs related to operating additional class sections to enable social distancing, such as those for hiring more instructors and increasing campus hours of operations. | $0”
  - column:Campus safety and operations.: 2 ⟵ “Campus safety and operations. | $02”
  - column:Purchasing, leasing, or renting additional instructional equipment and supplies (such as laboratory equipment or computers) to reduce the number of students sharing equipment or supplies during a single class period and to provide time for disinfection between uses.: 0 ⟵ “Purchasing, leasing, or renting additional instructional equipment and supplies (such as laboratory equipment or computers) to reduce the number of students sharing equipment or supplies during a single class period and to provide time for ”
  - column:Replacing lost revenue from academic sources.: 3 ⟵ “Replacing lost revenue from academic sources. | $03”
  - column:Purchasing faculty and staff training in online instruction; or paying additional funds to staff who are providing training in addition to their regular job responsibilities.: 0 ⟵ “Purchasing faculty and staff training in online instruction; or paying additional funds to staff who are providing training in addition to their regular job responsibilities. | $0”
  - column:Other Uses of (a)(1) Institutional Portion funds.: 0 ⟵ “Other Uses of (a)(1) Institutional Portion funds. | $0”
  - column:Quarterly Expenditures for each Program: 0 ⟵ “Quarterly Expenditures for each Program | $0”
  - column:Total of Quarterly Expenditures: 0 ⟵ “Total of Quarterly Expenditures | $0”
### `2a7483273c59a2ba` Carthage College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.carthage.edu/admissions/undergraduate-students/apib-credit/ (sha256 c9c5eb82880f)
- issues: rows_without_score
- checks: {"distinct_exams": 34, "equivalencies": 35, "rows_without_score": 35}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “African American Studies | GEL 9999 General Elective”
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “Art History | ARH 1700 Introduction to Art History (with score of 4)”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | BIO 1010 Concepts in Biology”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB | MTH 1120 Calculus I (with score of 4 or 5)”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Calculus BC | MTH 1120 Calculus I (with score of 4; see department chair to discuss credits for MTH 1220 Calculus II)8 credits for MTH 1120 Calculus I and MTH 1220 Calculus II (with score of 5; Note: A score of 3 on Calculus BC with an AB sub-score of 4 will transfer as MTH 1120 Calculus I)”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | CHM 1010 General Chemistry (with a score of 3 or 4)8 credits for CHM 1010 General Chemistry I and CHM 1020 General Chemistry II (with score of 5)”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “Computer Science A | CSC 1810 Principles of Computer Science I”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “Computer Science Principles | GEL 9999 General Elective”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Economics: Macroeconomics | ECN 1020 Principles of Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Economics: Microeconomics | ECN 1010 Principles of Microeconomics”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language | GEL 9999 General Elective”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “English Literature | ENG 1060 Interpreting Literature”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “Environmental Science | GEO 1600 Earth Revealed”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “European History | HIS 1120 Issues in European History II”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “French Language | A language placement test must be taken at Carthage”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “German Language | A language placement test must be taken at Carthage”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Human Geography | GEO 1500 Human Geography: An Introduction”
  - equivalencies[AP-LATIN|None]:  ⟵ “Latin | A language placement test must be taken at Carthage”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “Music Theory — Aural | GEL 9999 General Elective (1 credit) (General Music Theory score must be 3 or higher)”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “Music Theory — Non-Aural | GEL 9999 General Elective (3 credits) (General Music Theory score must be 3 or higher)”
  - equivalencies[AP-PHYSICS-1|None]:  ⟵ “Physics 1, Algebra Based | PHY 1200 Fundamentals of Physics (with score of 4)”
  - equivalencies[AP-PHYSICS-2|None]:  ⟵ “Physics 2, Algebra Based | PHY 1200 Fundamentals of Physics (with score of 4). If a 4 is received in both Physics 1 and 2, credit will also be given for PHY 2100.”
  - equivalencies[AP-PHYSICS-C-MECHANICS|None]:  ⟵ “Physics C (Mechanics) | PHY 1200 Fundamentals of Physics (with score of 4)”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|None]:  ⟵ “Physics C (Electricity and Magnetism) | PHY 1200 Fundamentals of Physics (LAB) and PHY 2200 General Physics I (LAB) (with score of 4)”
  - equivalencies[AP-PSYCHOLOGY|None]:  ⟵ “Psychology | GEL 9999 General Elective”
  - … 10 more rows
### `53b4e2a7725b46ea` Carthage College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.carthage.edu/admissions/undergraduate-students/apib-credit/ (sha256 c9c5eb82880f)
- issues: rows_without_score
- checks: {"distinct_exams": 11, "equivalencies": 12, "rows_without_score": 12}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | BIO 1010 Concepts in Biology”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | SCI 0099”
  - equivalencies[IB-COMPUTER-SCIENCE|None]:  ⟵ “Computer Science | See department”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | ECN 1030 Issues in Economics”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | GEO 1500 Human Geography: An Introduction”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History | HIS 9999”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History of the Americas | HIS 1000 Issues in American History”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | MUS 1150 Exploring Music”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | PYC 1500 Introduction to Psychological Science”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|None]:  ⟵ “Social & Cultural Anthropology | SOC 1020 Cultural Anthropology”
  - equivalencies[IB-THEATRE|None]:  ⟵ “Theatre Arts | THR 1150 Introduction to Theatre”
  - equivalencies[IB-VISUAL-ARTS|None]:  ⟵ “Visual Arts | ART 1030 Exploring Studio Art”
### `15209288d22d3175` College of Menominee Nation — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.menominee.edu/admission-aid/financial-aid/faqs (sha256 0933cb24c75b)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “For Dependency circumstances, we will ask you to fill out the Dependency Override Form.”
### `ea3955faf979297b` College of Menominee Nation — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.menominee.edu/admission-aid/financial-aid/faqs (sha256 0933cb24c75b)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: need_based_special_circumstances ⟵ “Applying for Aid Verification Process Awarding Financial Aid Disbursement Special Circumstances Satisfactory Academic Progress (SAP) Applying for Aid Who should apply for financial aid?”
  - sentence: need_based_special_circumstances ⟵ “Working on a master’s or doctorate program during the award year; Married; Ward/dependent of the court, or was a ward/dependent of the court until the age 18; Has legal dependents other than a spouse; A student for whom a financial aid administrator makes a documented determination of independence by reason of other unusual circumstance; Legal guardianship as determined by a court in your state; D”
  - sentence: need_based_special_circumstances ⟵ “If you are denied aid or feel that your application should be reconsidered because of special circumstances or events since you filed for your aid, it is possible to appeal in writing.”
  - sentence: need_based_special_circumstances ⟵ “Please refer to CMN Unusual Circumstance Paper Work or set up appointment with the Financial Aid Office to discuss your options.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances What if I experience special circumstances?”
  - sentence: need_based_special_circumstances ⟵ “What if I experience special circumstances?”
### `04381a22df500bc7` Concordia University-Wisconsin — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cuw.edu/admissions/financial-aid/_assets/SAP-policy.pdf (sha256 b72b2bb214ec)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal Procedure: Upon receiving a completed Satisfactory Academic Progress appeal form from a student whose financial aid eligibility has been terminated according to the provisions of section D, the Director of Financial Aid may reinstate the student’s eligibility.”
  - sentence: sap_appeal ⟵ “In circumstances where a student has appealed and is unable to meet both the 67% completion rate and the 2.0 CGPA requirements for SAP the outcome of the appeal may include an academic plan.”
  - sentence: sap_appeal ⟵ “This plan which will be created from the SAP appeal process will outline specific criteria that a student must meet during the semesters that this plan covers.”
### `2953b80563a3fb4f` Concordia University-Wisconsin — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cuw.edu/admissions/financial-aid/_assets/2526%20Cost%20of%20Attendance.pdf (sha256 3b4875e7d7d9)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 10}
  - column:Housing and Food: 14100 ⟵ “Housing and Food | $14,100 | $9,400 | $4,700”
  - column:Book: 4350 ⟵ “Book | $4,350 | $2,900 | $1,450”
  - column:Transportation: 501 ⟵ “Transportation | $501 | $334 | $167”
  - column:Loan Fee: 111 ⟵ “Loan Fee | $111 | $74 | $37”
  - column:Personal: 5000 ⟵ “Personal | $5,000 | $3,333 | $1,667”
  - column:TOTAL (not including tuition): 24062 ⟵ “TOTAL (not including tuition) | $24,062 | $16,041 | $8,021”
  - column:TOTAL FT (12 Credits): 41162 ⟵ “TOTAL FT (12 Credits) | $41,162 | $27,441 | $13,721”
  - column:TOTAL 3/4 (9 Credits): 36887 ⟵ “TOTAL 3/4 (9 Credits) | $36,887 | $24,591 | $12,296”
  - column:TOTAL 1/2 (6 Credits): 32612 ⟵ “TOTAL 1/2 (6 Credits) | $32,612 | $21,741 | $10,871”
  - column:Tuition: 475 ⟵ “Tuition | $475 | $1,425”
  - column:Housing and Food: 9400 ⟵ “Housing and Food | $14,100 | $9,400 | $4,700”
  - column:Book: 2900 ⟵ “Book | $4,350 | $2,900 | $1,450”
  - column:Transportation: 334 ⟵ “Transportation | $501 | $334 | $167”
  - column:Loan Fee: 74 ⟵ “Loan Fee | $111 | $74 | $37”
  - column:Personal: 3333 ⟵ “Personal | $5,000 | $3,333 | $1,667”
  - column:TOTAL (not including tuition): 16041 ⟵ “TOTAL (not including tuition) | $24,062 | $16,041 | $8,021”
  - column:TOTAL FT (12 Credits): 27441 ⟵ “TOTAL FT (12 Credits) | $41,162 | $27,441 | $13,721”
  - column:TOTAL 3/4 (9 Credits): 24591 ⟵ “TOTAL 3/4 (9 Credits) | $36,887 | $24,591 | $12,296”
  - column:TOTAL 1/2 (6 Credits): 21741 ⟵ “TOTAL 1/2 (6 Credits) | $32,612 | $21,741 | $10,871”
  - column:Tuition: 1425 ⟵ “Tuition | $475 | $1,425”
  - column:Housing and Food: 4700 ⟵ “Housing and Food | $14,100 | $9,400 | $4,700”
  - column:Book: 1450 ⟵ “Book | $4,350 | $2,900 | $1,450”
  - column:Transportation: 167 ⟵ “Transportation | $501 | $334 | $167”
  - column:Loan Fee: 37 ⟵ “Loan Fee | $111 | $74 | $37”
  - column:Personal: 1667 ⟵ “Personal | $5,000 | $3,333 | $1,667”
  - … 4 more rows
### `ef3df4e403ed130d` Concordia University-Wisconsin — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.cuw.edu/admissions/undergraduate-admissions/precollege/advanced-placement.html (sha256 6c5da081d77a)
- issues: rows_without_score
- checks: {"distinct_exams": 36, "equivalencies": 36, "rows_without_score": 36}
  - equivalencies[AP-DRAWING|None]:  ⟵ “Art Drawing | ART 1040 Drawing Fundamentals – 3 crs.”
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | BIO 1401 General Biology I – 4 crs.”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Calculus AB or Calculus AB Subscore | MATH 2010 Calculus I – 4 crs.”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “Calculus BC | MATH 2020 Calculus II – 4 crs.”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | Score of 3: CHEM 1003 Introductory Chemistry Score of 4: CHEM 1414 General Chemistry I - 4 crs. Score of 5: CHEM 1414 Gen Chem I – 4 crs. and CHEM 1424 Gen Chem II – 4 crs.”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “Chinese Language and Culture | Core Language Credit – 3 crs.”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|None]:  ⟵ “Computer Science Principles | CSC 1010 Foundations of Computer Science – 3 crs.”
  - equivalencies[AP-COMPUTER-SCIENCE-A|None]:  ⟵ “Computer Science A | CSC 1070 Theory & Fundamentals of Computer Science – 3 crs.”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “Macroeconomics | ECON 2200 Macroeconomics – 3 crs.”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Microeconomics | ECON 2100 Microeconomics - 3 crs.”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|None]:  ⟵ “English Language and Composition | ENG 1040 Intro to Writing – 3 crs.”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|None]:  ⟵ “English Literature and Composition | ENG 1030 Civ & Worldview Literature – 3 crs. (default) OR ENG 1040 Intro to Writing – 3 crs.”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|None]:  ⟵ “Environmental Science | ENV 1800 Environmental Science – 4 crs.”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “European History | HIST 1099 Hist & World Views West World – 3 crs.”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “French Language | Core Language Credit – 3 crs.”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “German Language | GER 1010 Beginning German -4 crs.”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|None]:  ⟵ “Comparative Government & Politics | POLS 3000 Comparative Politics – 3 crs.”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|None]:  ⟵ “US Government & Politics | POLS 2010 American Government – 3 crs.”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Human Geography | Elective Credit – 3 crs.”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “Italian Language and Culture | Core Language Credit – 3 crs.”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “Japanese Language and Culture | Core Language Credit – 3 crs.”
  - equivalencies[AP-LATIN|None]:  ⟵ “Latin: Virgil | Core Language Credit – 3 crs.”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “Music Theory | Elective – 3 crs.”
  - equivalencies[AP-PHYSICS-1|None]:  ⟵ “Physics 1 | Score of 4 or 5: PHYS 1514 Gen Physics I - 4 crs.”
  - equivalencies[AP-PHYSICS-2|None]:  ⟵ “Physics 2 | Score of 4 or 5: PHYS 1524 Gen Physics II – 4 crs.”
  - … 11 more rows
### `d66f3df3d7778695` Edgewood College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.edgewood.edu/tuition-financial-aid/tuition-fees/?ecopen=special-circumst-tab3 (sha256 442827820977)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Spaces | Residence Hall | Room Type | $ per Semester | $ per Academic Year | Who is Eligible? | East Regina | Single | $7,250 | $14,500 | Resident Assistants | West Regina | Single Suite | $6,475 | $12,950 | Accommodations | West Regina | Single/Private Bathroom | $6,900 | $13,800 | Accommodations | East Regina | Single/Private Bathroom | $6,900 | $13,800 | Accommodations | Do”
### `9ad7a3877d98cb4b` Fox Valley Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.fvtc.edu/Portals/0/PDFs/Current-Students/Student-Forms-Policies/Policies/Financial-Aid-SAP-Policy.pdf (sha256 2574f33d670f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “A student who has been suspended must pay for future classes on their own until they meet Satisfactory Academic Progress requirements or successfully appeal.”
### `d567177620931642` Fox Valley Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.fvtc.edu/paying-for-college/financial-aid (sha256 497cc69c7855)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Read the Policy Extenuating Circumstances Sometimes there are special circumstances that are not reflected in your FAFSA application - situations that may affect your family's ability to pay for college.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances might include things like a job loss or reduction in income, or unusually high out-of-pocket medical expenses.”
  - sentence: need_based_special_circumstances ⟵ “There is a formal process that begins with the Special Circumstance Request form and will require additional documentation.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Request Summer Term Awards Summer term funding will be awarded automatically in mid-April if you've met the eligibility criteria: Accepted in a financial aid eligible program Have a completed FAFSA with financial aid eligibility for the summer term Enrolled in at least one credit for PELL Grant eligibility and at least six credits for loan eligibility If you are eligible for s”
  - sentence: need_based_special_circumstances ⟵ “Your financial aid award may be increased, reduced, or cancelled under certain conditions, which could include: Change in family financial circumstances Change in marital status Additional resources such as private scholarships, agency funding or Veterans benefits Incorrect information on your FAFSA Satisfactory academic progress is not maintained Change in enrollment status If any of these condit”
### `e87c6d44b9811b24` Fox Valley Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.fvtc.edu/paying-for-college/financial-aid (sha256 497cc69c7855)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “If this is your situation, you can submit a request to have your situation reviewed by our college's director of financial aid, who has the authority to use professional judgment to amend your financial aid application.”
### `cefb8abc59b98da2` Fox Valley Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.fvtc.edu/Portals/0/PDFs/Credit-Transfers/AP-CLEP/College-Level-Exam-Program-Course-Conversions.pdf (sha256 9820954ee83b)
- issues: course_column_missing
- checks: {"distinct_exams": 13, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50+]:  ⟵ “Human Growth and Development              50+          10809188       Developmental Psychology               3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50+]:  ⟵ “Introductory Psychology                   50+          10809198       Intro to Psychology                    3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50+]:  ⟵ “Introductory Sociology                    50+          10809196       Intro to Sociology                     3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50+]:  ⟵ “Principles of Macroeconomics              50+          10809195       Economics                              3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50+]:  ⟵ “Principles of Microeconomics              50+          10809195       Economics                              3”
  - equivalencies[CLEP-BIOLOGY|50+]:  ⟵ “Biology                                   50+          10806114       General Biology                        4”
  - equivalencies[CLEP-CHEMISTRY|63+]:  ⟵ “Chemistry                                 63+                                                                10”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50+]:  ⟵ “College Algebra                           50+          10804113       College Tech Math 1a                   3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50+]:  ⟵ “College Mathematics                       50+          10804107       College Mathematics                    3”
  - equivalencies[CLEP-PRECALCULUS|50+]:  ⟵ “Precalculus                               50+                                                                5”
  - equivalencies[CLEP-CALCULUS|50+]:  ⟵ “Calculus                                  50+          10804198       Calculus 1                             4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50+]:  ⟵ “Business Law                              50+          10102103       Business Law                           3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50+]:  ⟵ “Principles of Marketing                   50+          10104151       Principles of Marketing                3”
### `97f44a147af9e6e5` Herzing University-Brookfield — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 1d39578ec369)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
### `bb4a6efc7add27e6` Herzing University-Brookfield — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 1d39578ec369)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “A student not meeting satisfactory academic progress will be required to appeal in order to change programs and may be limited on the number of allowable program changes.”
  - sentence: sap_appeal ⟵ “If mitigating or extenuating circumstances exist, a student may appeal a dismissal from the University using the SAP Appeal process above.”
### `43b7961fbb4df94d` Herzing University-Kenosha — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 1d39578ec369)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
### `f88caa5b023f0869` Herzing University-Kenosha — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 1d39578ec369)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “A student not meeting satisfactory academic progress will be required to appeal in order to change programs and may be limited on the number of allowable program changes.”
  - sentence: sap_appeal ⟵ “If mitigating or extenuating circumstances exist, a student may appeal a dismissal from the University using the SAP Appeal process above.”
### `44a0caf342cdf00c` Herzing University-Madison — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 1d39578ec369)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “A student not meeting satisfactory academic progress will be required to appeal in order to change programs and may be limited on the number of allowable program changes.”
  - sentence: sap_appeal ⟵ “If mitigating or extenuating circumstances exist, a student may appeal a dismissal from the University using the SAP Appeal process above.”
### `b5daa9392d816c2a` Herzing University-Madison — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.herzing.edu/satisfactory-academic-progress (sha256 1d39578ec369)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Valid circumstances include a serious injury or illness, death of a relative or other special circumstance.”
### `97aa40097e3191a6` Lac Courte Oreilles Ojibwe University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lco.edu/tuition-and-fees (sha256 893819cf12c0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Step 4: Appealing to recalculate your need-based aid The LCOOU Financial Aid Office has established an appeal process to allow for a possible recalculation of financial need based on special or unusual circumstances.”
### `48bbb91e3f1c0ced` Lac Courte Oreilles Ojibwe University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://static1.squarespace.com/static/61169899b2811c413f1a56ff/t/6894d3d40b550246e8262db1/1754584020941/Cost+of+Attendance+2025-26+AY.pdf (sha256 ed562ad58948)
- issues: ambiguous_year_labels, multiple_total_rows, residency_unknown
- checks: {"columns": 1, "rows": 21}
  - column:Books/ Course-Materials/ Supplies/ Equipment: 1000 ⟵ “Books/ Course-Materials/ Supplies/ Equipment | $1,000”
  - column:Living Expenses (Food/Housing): 8832 ⟵ “Living Expenses (Food/Housing) | $8,832”
  - column:Transportation: 2752 ⟵ “Transportation | $2,752”
  - column:Personal/ Misc.: 1312 ⟵ “Personal/ Misc. | $1,312”
  - column:Total: 19926 ⟵ “Total | $19,926”
  - column:Tuition & Fees: 8830 ⟵ “Tuition & Fees | $8,830”
  - column:Books/ Course-Materials/ Supplies/ Equipment (2): 1000 ⟵ “Books/ Course-Materials/ Supplies/ Equipment | $1,000”
  - column:Living Expenses (Food/Housing) (2): 6032 ⟵ “Living Expenses (Food/Housing) | $6,032”
  - column:Transportation (2): 2752 ⟵ “Transportation | $2,752”
  - column:Personal/ Misc. (2): 1312 ⟵ “Personal/ Misc. | $1,312”
  - column:Total (2): 19926 ⟵ “Total | $19,926”
  - column:Books/ Course-Materials/ Supplies/ Equipment (3): 1000 ⟵ “Books/ Course-Materials/ Supplies/ Equipment | $1,000”
  - column:Living Expenses (Food/Housing) (3): 8832 ⟵ “Living Expenses (Food/Housing) | $8,832”
  - column:Transportation (3): 2752 ⟵ “Transportation | $2,752”
  - column:Personal/ Misc. (3): 1297 ⟵ “Personal/ Misc. | $1,297”
  - column:Total (3): 19926 ⟵ “Total | $19,926”
  - column:Books/ Course-Materials/ Supplies/ Equipment (4): 1000 ⟵ “Books/ Course-Materials/ Supplies/ Equipment | $1,000”
  - column:Living Expenses (Food/Housing) (4): 7040 ⟵ “Living Expenses (Food/Housing) | $7,040”
  - column:Transportation (4): 2656 ⟵ “Transportation | $2,656”
  - column:Personal/ Misc. (4): 1120 ⟵ “Personal/ Misc. | $1,120”
  - column:Total (4): 19946 ⟵ “Total | $19,946”
### `128d3210a10871b0` Lakeland University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://lakeland.edu/pdfs/2026/2026-2027-cost-of-attendance-undergraduate-main-campus.pdf (sha256 f295075423c6)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://lakeland.edu/pdfs/2026/2026-2027-cost-of-attendance-undergraduate-evening-online.pdf
- checks: {"columns": 5, "components_reconcile": false, "rows": 9}
  - column:Tuition: 35500.0 ⟵ “Tuition | $35,500.00 | $35,500.00 | $35,500.00 | $35,500.00 | $35,500.00”
  - column:Fees: 1700.0 ⟵ “Fees | $1,700.00 | $1,700.00 | $1,700.00 | $1,700.00 | $1,700.00”
  - column:Housing: 7820.0 ⟵ “Housing | $7,820.00 | $7,820.00 | $750.00 | $6,776.00 | $6,776.00”
  - column:Food: 7670.0 ⟵ “Food | $7,670.00 | $7,670.00 | $2,570.00 | $3,188.00 | $3,188.00”
  - column:Books: 1100.0 ⟵ “Books | $1,100.00 | $1,100.00 | $1,100.00 | $1,100.00 | $1,100.00”
  - column:Transportation: 1918.0 ⟵ “Transportation | $1,918.00 | $1,918.00 | $1,918.00 | $1,918.00 | $1,918.00”
  - column:Personal: 3226.0 ⟵ “Personal | $3,226.00 | $6,450.00 | $3,226.00 | $6,450.00 | $3,226.00”
  - column:Loan Fees: 72.0 ⟵ “Loan Fees | $72.00 | $72.00 | $72.00 | $72.00 | $72.00”
  - column:TOTAL: 57006.0 ⟵ “TOTAL | $57,006.00 | $60,230.00 | $44,836.00 | $54,704 | $51,480.00”
  - column:Tuition: 35500.0 ⟵ “Tuition | $35,500.00 | $35,500.00 | $35,500.00 | $35,500.00 | $35,500.00”
  - column:Fees: 1700.0 ⟵ “Fees | $1,700.00 | $1,700.00 | $1,700.00 | $1,700.00 | $1,700.00”
  - column:Housing: 7820.0 ⟵ “Housing | $7,820.00 | $7,820.00 | $750.00 | $6,776.00 | $6,776.00”
  - column:Food: 7670.0 ⟵ “Food | $7,670.00 | $7,670.00 | $2,570.00 | $3,188.00 | $3,188.00”
  - column:Books: 1100.0 ⟵ “Books | $1,100.00 | $1,100.00 | $1,100.00 | $1,100.00 | $1,100.00”
  - column:Transportation: 1918.0 ⟵ “Transportation | $1,918.00 | $1,918.00 | $1,918.00 | $1,918.00 | $1,918.00”
  - column:Personal: 6450.0 ⟵ “Personal | $3,226.00 | $6,450.00 | $3,226.00 | $6,450.00 | $3,226.00”
  - column:Loan Fees: 72.0 ⟵ “Loan Fees | $72.00 | $72.00 | $72.00 | $72.00 | $72.00”
  - column:TOTAL: 60230.0 ⟵ “TOTAL | $57,006.00 | $60,230.00 | $44,836.00 | $54,704 | $51,480.00”
  - column:Tuition: 35500.0 ⟵ “Tuition | $35,500.00 | $35,500.00 | $35,500.00 | $35,500.00 | $35,500.00”
  - column:Fees: 1700.0 ⟵ “Fees | $1,700.00 | $1,700.00 | $1,700.00 | $1,700.00 | $1,700.00”
  - column:Housing: 750.0 ⟵ “Housing | $7,820.00 | $7,820.00 | $750.00 | $6,776.00 | $6,776.00”
  - column:Food: 2570.0 ⟵ “Food | $7,670.00 | $7,670.00 | $2,570.00 | $3,188.00 | $3,188.00”
  - column:Books: 1100.0 ⟵ “Books | $1,100.00 | $1,100.00 | $1,100.00 | $1,100.00 | $1,100.00”
  - column:Transportation: 1918.0 ⟵ “Transportation | $1,918.00 | $1,918.00 | $1,918.00 | $1,918.00 | $1,918.00”
  - column:Personal: 3226.0 ⟵ “Personal | $3,226.00 | $6,450.00 | $3,226.00 | $6,450.00 | $3,226.00”
  - … 20 more rows
### `1afd5b0d3f22b863` Lakeland University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://lakeland.edu/pdfs/2026/2026-2027-cost-of-attendance-undergraduate-evening-online.pdf (sha256 c512247d3364)
- issues: arrangement_unlabeled, conflicting_sources:https://lakeland.edu/pdfs/2026/2026-2027-cost-of-attendance-undergraduate-main-campus.pdf
- checks: {"columns": 6, "rows": 18}
  - column:Tuition & Fees: 550.0 ⟵ “Tuition & Fees | $550.00 | $1,650.00 | $3,300.00 | $4,950.00 | $6,600.00 | $8,250.00”
  - column:Housing & Food: 0.0 ⟵ “Housing & Food | $0.00 | $4,532.00 | $4,532.00 | $4,532.00 | $4,532.00”
  - column:Books & Supplies: 93.0 ⟵ “Books & Supplies | $93.00 | $185.00 | $370.00 | $370.00 | $370.00”
  - column:Misc: 0.0 ⟵ “Misc | $0.00 | $3,225.00 | $3,225.00 | $3,22500 | $3,225.00”
  - column:Transportation: 240.0 ⟵ “Transportation | $240.00 | $959.00 | $959.00 | $959.00 | $959.00”
  - column:Loan Fees: 0.0 ⟵ “Loan Fees | $0.00 | $24.00 | $24.00 | $24.00 | $24.00”
  - column:ONE TERM TOTAL: 1983 ⟵ “ONE TERM TOTAL | $1,983 | $12,225.00 | $14,060.00 | $15,710.00 | $17,360.00”
  - column:TWO TERM TOTAL: 3966.0 ⟵ “TWO TERM TOTAL | $3,966.00 | $24,450.00 | $28,120.00 | $31,420.00 | $34,720.00”
  - column:THREE TERM TOTAL: 5949.0 ⟵ “THREE TERM TOTAL | $5,949.00 | $36,675.00 | $42,180.00 | $47,130.00 | $52,080.00”
  - column:Tuition & Fees (2): 550.0 ⟵ “Tuition & Fees | $550.00 | $1,650.00 | $3,300.00 | $4,950.00 | $6,600.00”
  - column:Housing & Food (2): 0.0 ⟵ “Housing & Food | $0.00 | $1,142.00 | $1,142.00 | $1,142.00”
  - column:Books & Supplies (2): 93.0 ⟵ “Books & Supplies | $93.00 | $185.00 | $370.00 | $370.00”
  - column:Misc (2): 0.0 ⟵ “Misc | $0.00 | $1,075.00 | $1,075.00 | $1,075.00”
  - column:Transportation (2): 216.5 ⟵ “Transportation | $216.50 | $959.00 | $959.00 | $959.00”
  - column:Loan Fees (2): 0.0 ⟵ “Loan Fees | $0.00 | $24.00 | $24.00 | $24.00”
  - column:ONE TERM TOTAL (2): 1983.0 ⟵ “ONE TERM TOTAL | $1,983.00 | $6,685.00 | $8,520.00 | $10,170.00”
  - column:TWO TERM TOTAL (2): 3966.0 ⟵ “TWO TERM TOTAL | $3,966.00 | $13,370.00 | $17,040.00 | $20,340.00”
  - column:THREE TERM TOTAL (2): 5949.0 ⟵ “THREE TERM TOTAL | $5,949.00 | $20,055.00 | $25,560.00 | $30,510.00”
  - column:Tuition & Fees: 1650.0 ⟵ “Tuition & Fees | $550.00 | $1,650.00 | $3,300.00 | $4,950.00 | $6,600.00 | $8,250.00”
  - column:Housing & Food: 4532.0 ⟵ “Housing & Food | $0.00 | $4,532.00 | $4,532.00 | $4,532.00 | $4,532.00”
  - column:Books & Supplies: 185.0 ⟵ “Books & Supplies | $93.00 | $185.00 | $370.00 | $370.00 | $370.00”
  - column:Misc: 3225.0 ⟵ “Misc | $0.00 | $3,225.00 | $3,225.00 | $3,22500 | $3,225.00”
  - column:Transportation: 959.0 ⟵ “Transportation | $240.00 | $959.00 | $959.00 | $959.00 | $959.00”
  - column:Loan Fees: 24.0 ⟵ “Loan Fees | $0.00 | $24.00 | $24.00 | $24.00 | $24.00”
  - column:ONE TERM TOTAL: 12225.0 ⟵ “ONE TERM TOTAL | $1,983 | $12,225.00 | $14,060.00 | $15,710.00 | $17,360.00”
  - … 58 more rows
### `mea62de847e60604` Lakeland University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://lakeland.edu/admissions/transfers/four-year-schools (sha256 7cc8f84c8079)
- issues: conflicting_sources:max_transfer_credits
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 72 ⟵ “Lakeland University accepts up to 72 semester hours of transferred credits from any combination of accredited two-year schools.”
  - max_transfer_credits: 90 ⟵ “Lakeland University accepts up to 90 semester hours of transferred credits from any combination of accredited four-year schools.”
### `6002f8ff5a6566cd` Lawrence University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lawrence.edu/wp-content/uploads/2025/11/2026-2027-Special-Circumstance-Request-Form.pdf (sha256 b37b9081e4fa)
- issues: semantic_review_required, conflicting_sources:https://www.lawrence.edu/admissions-aid/aid-affordability/appeals-special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Office 711 E Boldt Way Appleton, WI 54911 Phone: (920) 832-6583 | Fax: (920) 832-6582 financial.aid@lawrence.edu 2026-2027 SPECIAL CIRCUMSTANCE REQUEST FORM STUDENT NAME LAWRENCE ID OR D.O.B.”
  - sentence: need_based_special_circumstances ⟵ “This form should be completed when a family can document a significant change in financial circumstances, or if you believe there are special circumstances that were not included/considered on your initial aid application.”
### `9dbfacb08b13b484` Lawrence University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lawrence.edu/admissions-aid/aid-affordability/appeals-special-circumstances/ (sha256 8713c66c86ae)
- issues: semantic_review_required, conflicting_sources:https://www.lawrence.edu/wp-content/uploads/2025/11/2026-2027-Special-Circumstance-Request-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “You can also complete the Lawrence University Special Circumstances Form.”
  - sentence: need_based_special_circumstances ⟵ “Contact Financial Aid Complete the Special Circumstances Form Special Circumstance Review During a special circumstances review, our office works with families to gather materials that document changes in their financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Common Examples of Special Circumstances Considered Change in employment status or income High medical or dental expenses Changes in household, such as parents divorcing or separating Non-recurring payments received during the FAFSA tax year When you complete your Special Circumstance Request Form, include key details about your situation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstance review The U.S.”
  - sentence: need_based_special_circumstances ⟵ “This is called Unusual Circumstances and a request can only be approved in certain limited and exceptional circumstances where the parents are unable to be contacted or contact poses a risk to the student.”
  - sentence: need_based_special_circumstances ⟵ “These are examples of unusual circumstances where parent information can be removed or excluded from the FAFSA: Examples of Unusual Circumstances Considered Refugee or asylee status Parental abandonment or incarceration Abusive family environment Examples of circumstances NOT considered Parents do not claim you as a dependent on their tax return Parents refusal to contribute to education or studen”
### `194ff5efc7fdb8c8` Madison Area Technical College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://madisoncollege.edu/paying-for-college/tuition (sha256 56641ea8c83f)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition: 6224 ⟵ “Tuition | $6,224 | $4,668 | $3,112 | $1,556”
  - off_campus_not_with_family:Books: 1000 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3040 ⟵ “Personal | $3,040 | $3,040 | $3,040 | $0”
  - off_campus_not_with_family:Food and Housing: 13824 ⟵ “Food and Housing | $13,824 | $13,824 | $13,824 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $2,400”
  - off_campus_not_with_family:Total: 26572 ⟵ “Total | $26,572 | $24,766 | $22,960 | $4,206”
  - off_campus_not_with_family:Tuition: 4668 ⟵ “Tuition | $6,224 | $4,668 | $3,112 | $1,556”
  - off_campus_not_with_family:Books: 750 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3040 ⟵ “Personal | $3,040 | $3,040 | $3,040 | $0”
  - off_campus_not_with_family:Food and Housing: 13824 ⟵ “Food and Housing | $13,824 | $13,824 | $13,824 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $2,400”
  - off_campus_not_with_family:Total: 24766 ⟵ “Total | $26,572 | $24,766 | $22,960 | $4,206”
  - off_campus_not_with_family:Tuition: 3112 ⟵ “Tuition | $6,224 | $4,668 | $3,112 | $1,556”
  - off_campus_not_with_family:Books: 500 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3040 ⟵ “Personal | $3,040 | $3,040 | $3,040 | $0”
  - off_campus_not_with_family:Food and Housing: 13824 ⟵ “Food and Housing | $13,824 | $13,824 | $13,824 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $2,400”
  - off_campus_not_with_family:Total: 22960 ⟵ “Total | $26,572 | $24,766 | $22,960 | $4,206”
  - off_campus_not_with_family:Tuition: 1556 ⟵ “Tuition | $6,224 | $4,668 | $3,112 | $1,556”
  - off_campus_not_with_family:Books: 250 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 0 ⟵ “Personal | $3,040 | $3,040 | $3,040 | $0”
  - off_campus_not_with_family:Food and Housing: 0 ⟵ “Food and Housing | $13,824 | $13,824 | $13,824 | $0”
  - … 3 more rows
### `4d0dbca8eccdca77` Madison Area Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://madisoncollege.edu/paying-for-college/tuition (sha256 56641ea8c83f)
- issues: residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition: 6584 ⟵ “Tuition | $6,584 | $4,938 | $3,292 | $1,646”
  - off_campus_not_with_family:Books: 1000 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3072 ⟵ “Personal | $3,072 | $3,072 | $3,072 | $0”
  - off_campus_not_with_family:Food and Housing: 13760 ⟵ “Food and Housing | $13,760 | $13,760 | $13,760 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 3040 ⟵ “Transportation | $3,040 | $3,040 | $3,040 | $3,040”
  - off_campus_not_with_family:Total: 27540 ⟵ “Total | $27,540 | $25,644 | $23,748 | $4,936”
  - off_campus_not_with_family:Tuition: 4938 ⟵ “Tuition | $6,584 | $4,938 | $3,292 | $1,646”
  - off_campus_not_with_family:Books: 750 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3072 ⟵ “Personal | $3,072 | $3,072 | $3,072 | $0”
  - off_campus_not_with_family:Food and Housing: 13760 ⟵ “Food and Housing | $13,760 | $13,760 | $13,760 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 3040 ⟵ “Transportation | $3,040 | $3,040 | $3,040 | $3,040”
  - off_campus_not_with_family:Total: 25644 ⟵ “Total | $27,540 | $25,644 | $23,748 | $4,936”
  - off_campus_not_with_family:Tuition: 3292 ⟵ “Tuition | $6,584 | $4,938 | $3,292 | $1,646”
  - off_campus_not_with_family:Books: 500 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 3072 ⟵ “Personal | $3,072 | $3,072 | $3,072 | $0”
  - off_campus_not_with_family:Food and Housing: 13760 ⟵ “Food and Housing | $13,760 | $13,760 | $13,760 | $0”
  - off_campus_not_with_family:Loan Fees: 84 ⟵ “Loan Fees | $84 | $84 | $84 | $0”
  - off_campus_not_with_family:Transportation: 3040 ⟵ “Transportation | $3,040 | $3,040 | $3,040 | $3,040”
  - off_campus_not_with_family:Total: 23748 ⟵ “Total | $27,540 | $25,644 | $23,748 | $4,936”
  - off_campus_not_with_family:Tuition: 1646 ⟵ “Tuition | $6,584 | $4,938 | $3,292 | $1,646”
  - off_campus_not_with_family:Books: 250 ⟵ “Books | $1,000 | $750 | $500 | $250”
  - off_campus_not_with_family:Personal: 0 ⟵ “Personal | $3,072 | $3,072 | $3,072 | $0”
  - off_campus_not_with_family:Food and Housing: 0 ⟵ “Food and Housing | $13,760 | $13,760 | $13,760 | $0”
  - … 3 more rows
### `22b523bba2feaad0` Maranatha Baptist University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.mbu.edu/finances/financial-aid/ (sha256 373cbfbe2891)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Be sure you have applied for financial aid from as many sources as possible Maranatha Scholarships Scholarships from other sources Scholarships from businesses and organizations in your community The Financial Aid Office can review special circumstances, including loss of income, private school/homeschool expenses, unusually high medical expenses, etc.”
### `028eb1a0178d05ad` Maranatha Baptist University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mbu.edu/finances/tuition-and-costs/ (sha256 383631f46150)
- issues: cost_period_semester, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 10510 ⟵ “Tuition | $10,510”
  - column:Room & Board: 4900 ⟵ “Room & Board | $4,900”
  - column:Comprehensive Fee: 790 ⟵ “Comprehensive Fee | $790”
  - column:Estimated Total: 16200 ⟵ “Estimated Total | $16,200”
### `e77c5a2b38f2cae2` Maranatha Baptist University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mbu.edu/finances/tuition-and-costs/ (sha256 383631f46150)
- issues: cost_period_semester
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 11030 ⟵ “Tuition | $11,030”
  - column:Room & Board: 5150 ⟵ “Room & Board | $5,150”
  - column:Comprehensive Fee: 830 ⟵ “Comprehensive Fee | $830”
  - column:Estimated Total: 17010 ⟵ “Estimated Total | $17,010”
### `0327747ee0baf005` Marian University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.marianuniversity.edu/tuition-financial-aid/finacial-aid-guide/ (sha256 cac8fe2e1775)
- issues: semantic_review_required, conflicting_sources:https://www.marianuniversity.edu/cost-and-aid/,https://www.marianuniversity.edu/cost-and-aid/financial-aid-policies/,https://www.marianuniversity.edu/tuition-financial-aid/applying-financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances If you feel that you have a situation that may require special consideration, please contact our office to speak directly to a counselor.”
### `8657adf6ec18bedc` Marian University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.marianuniversity.edu/cost-and-aid/ (sha256 46b774252f5b)
- issues: semantic_review_required, conflicting_sources:https://www.marianuniversity.edu/cost-and-aid/financial-aid-policies/,https://www.marianuniversity.edu/tuition-financial-aid/applying-financial-aid/satisfactory-academic-progress/,https://www.marianuniversity.edu/tuition-financial-aid/finacial-aid-guide/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The estimate is subject to the accuracy of the information you provide, may change if financial or family characteristics change, and does not incorporate any special circumstances, which are reviewed after you officially apply for aid.”
### `a625ccd7a780d126` Marian University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.marianuniversity.edu/tuition-financial-aid/applying-financial-aid/satisfactory-academic-progress/ (sha256 96e391f0ebc5)
- issues: semantic_review_required, conflicting_sources:https://www.marianuniversity.edu/cost-and-aid/,https://www.marianuniversity.edu/cost-and-aid/financial-aid-policies/,https://www.marianuniversity.edu/tuition-financial-aid/finacial-aid-guide/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Some examples include the following: a) The death of a relative. b) An injury or illness of the student. c) Other special circumstances, which may be accepted on a case-by-case basis. 3) A detailed description of how the basis of the appeal negatively impacted the student’s academics. 4) A detailed description of what has changed in the student’s situation compared to the basis of the appeal, and ”
### `ac204b7f508187fd` Marian University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.marianuniversity.edu/cost-and-aid/financial-aid-policies/ (sha256 abe567c334a0)
- issues: semantic_review_required, conflicting_sources:https://www.marianuniversity.edu/cost-and-aid/,https://www.marianuniversity.edu/tuition-financial-aid/applying-financial-aid/satisfactory-academic-progress/,https://www.marianuniversity.edu/tuition-financial-aid/finacial-aid-guide/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students not meeting SAP are placed on a Financial Aid Warning and may appeal if facing special circumstances, like illness or family loss.”
### `220ab931302a3a3b` Marian University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.marianuniversity.edu/costandaid/cost-of-attendance/ (sha256 1e0cc5a9ff13)
- issues: ambiguous_year_labels, conflicting_sources:https://www.marianuniversity.edu/cost-and-aid/cost-of-attending-undergraduate/
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 34096 ⟵ “Tuition | $34,096 | $17,048”
  - column:Student Fees: 554 ⟵ “Student Fees | $554 | $277”
### `60b2c2524b417c02` Marian University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.marianuniversity.edu/cost-and-aid/cost-of-attending-undergraduate/ (sha256 b0699ae1e3c2)
- issues: conflicting_sources:https://www.marianuniversity.edu/costandaid/cost-of-attendance/
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 39033 ⟵ “Tuition | $39,033 | $19,517”
  - column:Student Fees: 658 ⟵ “Student Fees | $658 | $329”
### `1843183971043358` Marquette University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2025-2026.php (sha256 dc3f43166148)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “For Undergraduate students, progress will be evaluated annually after the spring semester and after every semester for students who are on an academic plan based on an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “A student who fails SAP has the option to “appeal”.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Procedures Student must complete the Appeal form (link below) by following instructions on the form.”
  - sentence: sap_appeal ⟵ “If you are a former student wishing to return to Marquette after spending one or more fall or spring terms away, use one of the “Academic Censure/Satisfactory Academic Progress Appeal…” forms for former students in the PDF Forms section on this page - https://www.marquette.edu/central/registrar/forms.php Students who were on an academic plan during Spring 2020, elected to use a pass/fail grading b”
### `3f8fd5e870121046` Marquette University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.marquette.edu/central/financial-aid/applying-for-aid/appealing-financial-aid.php (sha256 42e65fd6a682)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.marquette.edu/central/financial-aid/applying-for-aid/
- checks: {"negative_sentences": 0, "sentences": 13}
  - sentence: need_based_special_circumstances ⟵ “Appealing Financial Aid for Special and Unusual Circumstances // Marquette Central // Marquette University Skip to content marquette.edu // Search // A-Z Index // Give to Marquette Marquette UniversityStudent Financial Aid Student Financial Aid Registrar Academic Calendars Bulletin Policies Summer Studies Veterans Benefits Faculty/Staff Course Registration Class Search Permission number Schedule o”
  - sentence: need_based_special_circumstances ⟵ “Forms Registrar Forms Financial Aid Forms Student Accounts Forms Student Employment Forms Other Resources Contact Us Marquette.edu // Marquette Central // Student Financial Aid // Applying for Aid // Appealing Financial Aid for Special and Unusual Circumstances Some students and families experience financial situations that are not reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Circumstances that impact the family’s ability to pay for college may possibly be reviewed in the Special Circumstance Appeal process.”
  - sentence: need_based_special_circumstances ⟵ “Expand all | Collapse all POSSIBLE SPECIAL CIRCUMSTANCES Students and families facing significant financial hardship may be eligible for additional financial aid through the Special Circumstance Appeal process.”
  - sentence: need_based_special_circumstances ⟵ “The student must have the correct year FAFSA on file with Marquette to be eligible to request a special circumstance review.”
  - sentence: need_based_special_circumstances ⟵ “CIRCUMSTANCES THAT CANNOT BE CONSIDERED Not every situation can be reviewed for a special circumstance appeal.”
### `4c010474710f9cc7` Marquette University — appeals 2027-28 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2027-2028.php (sha256 db785d68b36a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “For Undergraduate students, progress will be evaluated annually after the spring semester and after every semester for students who are on an academic plan based on an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “A student who fails SAP has the option to “appeal”.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Procedures Student must complete the Appeal form (link below) by following instructions on the form.”
  - sentence: sap_appeal ⟵ “If you are a former student wishing to return to Marquette after spending one or more fall or spring terms away, use one of the “Academic Censure/Satisfactory Academic Progress Appeal…” forms for former students in the PDF Forms section on this page - https://www.marquette.edu/central/registrar/forms.php.”
  - sentence: sap_appeal ⟵ “Students who were on an academic plan during Spring 2020, elected to use a pass/fail grading basis, and did not meet the plan requirements were not required to submit a SAP appeal.”
### `5e8a05221d1a5d2e` Marquette University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.marquette.edu/central/financial-aid/applying-for-aid/ (sha256 40d1f749ab0d)
- issues: semantic_review_required, conflicting_sources:https://www.marquette.edu/central/financial-aid/applying-for-aid/appealing-financial-aid.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Resources Key steps for Applying for Financial Aid 1-2-3 Guides to Making Financial Aid Easier Eligibility Requirements for Undergraduates Appealing Financial Aid for Special Circumstances Net Price Calculator for incoming Freshmen (English/Spanish) Understanding the Verification Process A percentage of FAFSAs are selected by the Federal Processor for a review process called Verification.”
### `6f7f3baf28fa9b39` Marquette University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2025-2026.php (sha256 dc3f43166148)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: competing_offer_review ⟵ “It is not the practice of Marquette University to match financial aid awards from other universities.”
### `7b85f228df64d0a1` Marquette University — appeals 2027-28 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2027-2028.php (sha256 db785d68b36a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: competing_offer_review ⟵ “It is not the practice of Marquette University to match financial aid awards from other universities. a.”
### `981c18c48b22ffec` Marquette University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2026-2027.php (sha256 14055fd5c8f1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: competing_offer_review ⟵ “It is not the practice of Marquette University to match financial aid awards from other universities. a.”
### `e836375474a93904` Marquette University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2026-2027.php (sha256 14055fd5c8f1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “For Undergraduate students, progress will be evaluated annually after the spring semester and after every semester for students who are on an academic plan based on an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “A student who fails SAP has the option to “appeal”.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Procedures Student must complete the Appeal form (link below) by following instructions on the form.”
  - sentence: sap_appeal ⟵ “If you are a former student wishing to return to Marquette after spending one or more fall or spring terms away, use one of the “Academic Censure/Satisfactory Academic Progress Appeal…” forms for former students in the PDF Forms section on this page - https://www.marquette.edu/central/registrar/forms.php.”
  - sentence: sap_appeal ⟵ “Students who were on an academic plan during Spring 2020, elected to use a pass/fail grading basis, and did not meet the plan requirements were not required to submit a SAP appeal.”
### `362235b04b3b0afd` Marquette University — awards 2025-26 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2025-2026.php (sha256 dc3f43166148)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: 277 ⟵ “Student | 277”
### `71f0194aa32d67a3` Marquette University — awards 2025-26 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2025-2026.php (sha256 dc3f43166148)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,932 ⟵ “Title IV | $1,932”
### `b0e8df1ae1ad377b` Marquette University — awards 2025-26 [new] (labeled_in_title)
- source: https://www.marquette.edu/central/financial-aid/resources/award-information/award-information-2025-2026.php (sha256 dc3f43166148)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: 791 ⟵ “Marquette | 791”
### `79912ffd085fa202` Marquette University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.marquette.edu/central/financial-aid/resources/undergraduate-cost-of-attendance.php (sha256 a52a5437eca9)
- issues: arrangement_unlabeled
- checks: {"columns": 5, "rows": 6}
  - with_parents_or_family:Tuition See Bursar: 53890 ⟵ “Tuition See Bursar | $53,890 | $53,890 | $53,890 | $53,890 | $14,400”
  - with_parents_or_family:Living expenses such as housing and food: 8450 ⟵ “Living expenses such as housing and food | $8,450 | $17,480 | $11,900 | $13,360 | $13,360”
  - with_parents_or_family:Required course materials and educational supplies: 720 ⟵ “Required course materials and educational supplies | $720 | $720 | $720 | $720 | $720”
  - with_parents_or_family:Student fees: 1200 ⟵ “Student fees | $1,200 | $1,200 | $1,200 | $1,200 | $1,200”
  - with_parents_or_family:Personal: 2950 ⟵ “Personal | $2,950 | $2,950 | $2,950 | $2,950 | $2,950”
  - with_parents_or_family:Transportation: 3000 ⟵ “Transportation | $3,000 | *** | *** | $3,300 | $350”
  - column:Tuition See Bursar: 53890 ⟵ “Tuition See Bursar | $53,890 | $53,890 | $53,890 | $53,890 | $14,400”
  - column:Living expenses such as housing and food: 17480 ⟵ “Living expenses such as housing and food | $8,450 | $17,480 | $11,900 | $13,360 | $13,360”
  - column:Required course materials and educational supplies: 720 ⟵ “Required course materials and educational supplies | $720 | $720 | $720 | $720 | $720”
  - column:Student fees: 1200 ⟵ “Student fees | $1,200 | $1,200 | $1,200 | $1,200 | $1,200”
  - column:Personal: 2950 ⟵ “Personal | $2,950 | $2,950 | $2,950 | $2,950 | $2,950”
  - off_campus_not_with_family:Tuition See Bursar: 53890 ⟵ “Tuition See Bursar | $53,890 | $53,890 | $53,890 | $53,890 | $14,400”
  - off_campus_not_with_family:Living expenses such as housing and food: 11900 ⟵ “Living expenses such as housing and food | $8,450 | $17,480 | $11,900 | $13,360 | $13,360”
  - off_campus_not_with_family:Required course materials and educational supplies: 720 ⟵ “Required course materials and educational supplies | $720 | $720 | $720 | $720 | $720”
  - off_campus_not_with_family:Student fees: 1200 ⟵ “Student fees | $1,200 | $1,200 | $1,200 | $1,200 | $1,200”
  - off_campus_not_with_family:Personal: 2950 ⟵ “Personal | $2,950 | $2,950 | $2,950 | $2,950 | $2,950”
  - column:Tuition See Bursar: 53890 ⟵ “Tuition See Bursar | $53,890 | $53,890 | $53,890 | $53,890 | $14,400”
  - column:Living expenses such as housing and food: 13360 ⟵ “Living expenses such as housing and food | $8,450 | $17,480 | $11,900 | $13,360 | $13,360”
  - column:Required course materials and educational supplies: 720 ⟵ “Required course materials and educational supplies | $720 | $720 | $720 | $720 | $720”
  - column:Student fees: 1200 ⟵ “Student fees | $1,200 | $1,200 | $1,200 | $1,200 | $1,200”
  - column:Personal: 2950 ⟵ “Personal | $2,950 | $2,950 | $2,950 | $2,950 | $2,950”
  - column:Transportation: 3300 ⟵ “Transportation | $3,000 | *** | *** | $3,300 | $350”
  - column:Tuition See Bursar: 14400 ⟵ “Tuition See Bursar | $53,890 | $53,890 | $53,890 | $53,890 | $14,400”
  - column:Living expenses such as housing and food: 13360 ⟵ “Living expenses such as housing and food | $8,450 | $17,480 | $11,900 | $13,360 | $13,360”
  - column:Required course materials and educational supplies: 720 ⟵ “Required course materials and educational supplies | $720 | $720 | $720 | $720 | $720”
  - … 4 more rows
### `d51251e54316dc73` Mid-State Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.mstc.edu/paying-for-college/apply-for-financial-aid (sha256 f7e990489285)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Be sure to include: A clear explanation of what you believe is inaccurate or unfair Any details about special circumstances Supporting documents, if available If you and the Financial Aid manager cannot resolve the issue, you may submit a second written appeal within five school days of receiving your decision.”
  - sentence: need_based_special_circumstances ⟵ “Appealing a Suspension If you had unusual circumstances—like a serious illness, a death in your immediate family, or military service—you can submit a Petition for Reinstatement and an Academic Success Plan.”
### `5c99eeb935825702` Mid-State Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mstc.edu/paying-for-college/tuition-and-fees (sha256 6a3b12b845cb)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 4932 ⟵ “Tuition & Fees | $4,932 | $4,932”
  - with_parents_or_family:Books & Supplies: 1463 ⟵ “Books & Supplies | $1,463 | $1,463”
  - with_parents_or_family:Housing & Food: 3182 ⟵ “Housing & Food | $3,182 | $10,304”
  - with_parents_or_family:Transportation: 4102 ⟵ “Transportation | $4,102 | $4,102”
  - with_parents_or_family:Personal Spending: 3065 ⟵ “Personal Spending | $3,065 | $3,065”
  - with_parents_or_family:Loan Fees: 86 ⟵ “Loan Fees | $86 | $86”
  - with_parents_or_family:Estimated Annual Total: 16830 ⟵ “Estimated Annual Total | $16,830 | $23,952”
  - column:Tuition & Fees: 4932 ⟵ “Tuition & Fees | $4,932 | $4,932”
  - column:Books & Supplies: 1463 ⟵ “Books & Supplies | $1,463 | $1,463”
  - column:Housing & Food: 10304 ⟵ “Housing & Food | $3,182 | $10,304”
  - column:Transportation: 4102 ⟵ “Transportation | $4,102 | $4,102”
  - column:Personal Spending: 3065 ⟵ “Personal Spending | $3,065 | $3,065”
  - column:Loan Fees: 86 ⟵ “Loan Fees | $86 | $86”
  - column:Estimated Annual Total: 23952 ⟵ “Estimated Annual Total | $16,830 | $23,952”
### `b2b514acfe041ba1` Mid-State Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.mstc.edu/sites/default/files/2026-04/Advanced-Placement-Exam-List.pdf (sha256 e89595009284)
- issues: course_column_missing
- checks: {"distinct_exams": 10, "equivalencies": 10, "rows_without_score": 0}
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “20-802-211 Spanish 1                        3       Culture                            3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                              3       AP Macroeconomics                  3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                              3       AP Microeconomics                  3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “10-809-198 Introduction to Psychology       3       AP Psychology                      3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “20-803-212 U.S. History 1877 to Present     3       AP U.S. History                    3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “20-803-259 World History Since 1500         3       AP Modern World History            3”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “10-804-189 Introductory Statistics                                                   3             AP Statistics                                      3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “10-806-114 General Biology                                                           4             AP Biology                                          3”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “10-806-134 General Chemistry                                                          4            AP Chemistry                                       3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “10806 215 Environmental Science                                                      3             Science                                             3”
### `46d1106dcb007ecd` Milwaukee Area Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/forms/2026-27_provisional-independent-form.pdf (sha256 35b2d1d2a79d)
- issues: semantic_review_required, conflicting_sources:https://www.matc.edu/costs-scholarships-aid/forms/2026-27_special-circumstances-appeal-form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “STEP 3: SUBMIT SUPPORTING DOCUMENTATION Please submit the following documents substantiating your unusual circumstance: • Signed and dated letter from a professional (counselor, therapist, doctor, member of the clergy, social worker, etc.) or another person with knowledge of your situation.”
### `48f76aabb4ee848d` Milwaukee Area Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/forms/2026-27_special-circumstances-appeal-form.pdf (sha256 87d874025c50)
- issues: semantic_review_required, conflicting_sources:https://www.matc.edu/costs-scholarships-aid/forms/2026-27_provisional-independent-form.pdf
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Page 1 of 2 2026-2027 SPECIAL CIRCUMSTANCES APPEAL FORM The MATC Financial Aid Office recognizes that our students may have extenuating circumstances that affect their financial situation.”
  - sentence: need_based_special_circumstances ⟵ “PLEASE NOTE: Electing to resign from employment or reduce working hours to attend college does NOT qualify as justification for a special circumstance appeal.”
  - sentence: need_based_special_circumstances ⟵ “Page 2 of 2 STUDENT INFORMATION (Please print) Student’s Last Name Student’s First Name Middle Initial Student ID Number SECTION C: PERSONAL STATEMENT Include a signed and dated statement that details the event(s) requiring a special circumstances appeal.”
  - sentence: need_based_special_circumstances ⟵ “If you are in one of the situations below, completing the Special Circumstance process will not result in an increase in your financial aid eligibility: • If your Student Aid Index (SAI) is already '0' or lower.”
  - sentence: need_based_special_circumstances ⟵ “Upon receipt of all required documentation, appeals will be reviewed by the Financial Aid Office to determine if the circumstances comply with the Department of Education’s regulations governing special circumstances appeals.”
### `4b4381eb5633fb65` Milwaukee Area Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/student-financial-aid-handbook-2025-2026.pdf (sha256 6d58760254b8)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Additional Financial Aid Information ● Your correct and completed application must be in our office two weeks prior to your last day of enrollment. ● Upon receipt of your FAFSA, if selected for verification, you will be required to submit additional documentation. ● In order to be considered for a Satisfactory Academic Progress (SAP) appeal, you must meet with an Academic Advisor in your Pathway t”
  - sentence: sap_appeal ⟵ “Please see our website at https://www.matc.edu/costs-scholarships- aid/cost-aid-deadlines.html for the deadlines to submit a SAP appeal in order to receive aid for the semester. ● Scholarships have different deadlines depending on the specific scholarship requirements.”
  - sentence: sap_appeal ⟵ “If this occurs and the student wishes to appeal to have financial aid reinstated, meet with your Pathway advisor to complete an academic plan and a SAP Appeal Form which is submitted to the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “SAP appeals are reviewed by a Financial Aid Advisor or Supervisor within the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “SAP Appeals must be submitted using the official SAP Appeal Form by the deadline for the semester you are seeking aid for.”
  - sentence: sap_appeal ⟵ “The SAP Appeal deadlines are 11/1/2025 for the fall 2025 semester, 4/1/2026 for the spring 2026 semester, and 7/1/2026 for the summer 2026 semester.”
### `5db2a8269564304c` Milwaukee Area Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/forms/2026-27_unaccompanied-homeless-youth.pdf (sha256 daf4f15207f1)
- issues: semantic_review_required, conflicting_sources:https://www.matc.edu/costs-scholarships-aid/forms/2026-27_provisional-independent-form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Page 1 of 2 2026-2027 UNACCOMPANIED HOMELESS YOUTH VERIFICATION FORM On your 2026-27 Free Application for Federal Student Aid (FAFSA) you answered YES to the student homelessness question that asks “At any time on or after July 1, 2025 was the student an unaccompanied youth and either (1) homeless, or (2) self- supporting and at risk of being homeless?”, OR indicated homelessness on the 2026-27 Pr”
### `681ba30d38be10e2` Milwaukee Area Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/student-financial-aid-handbook-2025-2026.pdf (sha256 6d58760254b8)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The Higher Education Act of 1965, as amended, determines the criteria for dependency status for financial aid purposes.”
  - sentence: need_based_special_circumstances ⟵ “There must be unusual circumstances for the financial aid specialist to make any adjustments, and you must provide adequate documentation to support those circumstances.”
### `8a6cf4b93c6e5bfd` Milwaukee Area Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/forms/2026-27_provisional-independent-form.pdf (sha256 35b2d1d2a79d)
- issues: semantic_review_required, conflicting_sources:https://www.matc.edu/costs-scholarships-aid/forms/2026-27_unaccompanied-homeless-youth.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Page 1 of 2 2026-2027 PROVISIONAL INDEPENDENT FORM (Appeal for Dependency Override) Based on the information you have reported on your FAFSA, you have been granted a Provisional Independent status.”
### `4da94929eaa16023` Milwaukee Area Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/tuition-fees.html (sha256 7c930ee84b53)
- issues: arrangement_unlabeled, cost_period_semester, multiple_total_rows
- checks: {"columns": 4, "rows": 10}
  - column:Tuition and Fees: 791.49 ⟵ “Tuition and Fees | 791.49 | 1,582.98 | 3,165.96 | 3,809.95”
  - column:Student ID: 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare: 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/Course: 200.0 ⟵ “Books $200/Course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL: 1007.49 ⟵ “TOTAL | 1,007.49 | 1,998.98 | 3,981.96 | 4,973.45”
  - column:Tuition and Fees (2): 965.05 ⟵ “Tuition and Fees | 965.05 | 1,930.38 | 3,860.76 | 4,825.95”
  - column:Student ID (2): 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare (2): 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/Course (2): 200.0 ⟵ “Books $200/Course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL (2): 1175.19 ⟵ “TOTAL | 1,175.19 | 2,346.38 | 4,676.76 | 5,841.95”
  - column:Tuition and Fees: 1582.98 ⟵ “Tuition and Fees | 791.49 | 1,582.98 | 3,165.96 | 3,809.95”
  - column:Student ID: 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare: 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/Course: 400.0 ⟵ “Books $200/Course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL: 1998.98 ⟵ “TOTAL | 1,007.49 | 1,998.98 | 3,981.96 | 4,973.45”
  - column:Tuition and Fees (2): 1930.38 ⟵ “Tuition and Fees | 965.05 | 1,930.38 | 3,860.76 | 4,825.95”
  - column:Student ID (2): 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare (2): 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/Course (2): 400.0 ⟵ “Books $200/Course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL (2): 2346.38 ⟵ “TOTAL | 1,175.19 | 2,346.38 | 4,676.76 | 5,841.95”
  - column:Tuition and Fees: 3165.96 ⟵ “Tuition and Fees | 791.49 | 1,582.98 | 3,165.96 | 3,809.95”
  - column:Student ID: 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare: 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/Course: 800.0 ⟵ “Books $200/Course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL: 3981.96 ⟵ “TOTAL | 1,007.49 | 1,998.98 | 3,981.96 | 4,973.45”
  - … 15 more rows
### `525cc0ae3473bf5c` Milwaukee Area Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.matc.edu/costs-scholarships-aid/estimated-costs-info.html (sha256 d82873ef1252)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 1, "rows": 16}
  - column:Tuition: 4704.0 ⟵ “Tuition | $2,352.00 | $2,352.00 | $4,704.00”
  - column:Fees: 80.0 ⟵ “Fees | $40.00 | $40.00 | $80.00”
  - column:Housing & Food: 3222.0 ⟵ “Housing & Food | $1,611.00 | $1,611.00 | $3,222.00”
  - column:Books & Supplies: 1464.0 ⟵ “Books & Supplies | $732.00 | $732.00 | $1,464.00”
  - column:Transportation: 4104.0 ⟵ “Transportation | $1,949.00 | $1,949.00 | $4,104.00”
  - column:Miscellaneous Personal Expenses: 3898.0 ⟵ “Miscellaneous Personal Expenses | $1,533.00 | $1,533.00 | $3,898.00”
  - column:Federal Student Loan Fees: 84.0 ⟵ “Federal Student Loan Fees | $42.00 | $42.00 | $84.00”
  - column:Total: 16538.0 ⟵ “Total | $8,269.00 | $8,269.00 | $16,538.00”
  - column:Tuition (2): 4704.0 ⟵ “Tuition | $2,352.00 | $2,352.00 | $4,704.00”
  - column:Fees (2): 80.0 ⟵ “Fees | $40.00 | $40.00 | $80.00”
  - column:Housing & Food (2): 11952.0 ⟵ “Housing & Food | $5,976.00 | $5,976.00 | $11,952.00”
  - column:Books & Supplies (2): 1464.0 ⟵ “Books & Supplies | $732.00 | $732.00 | $1,464.00”
  - column:Transportation (2): 4104.0 ⟵ “Transportation | $2,052.00 | $2,052.00 | $4,104.00”
  - column:Miscellaneous Personal Expenses (2): 3898.0 ⟵ “Miscellaneous Personal Expenses | $1,949.00 | $1,949.00 | $3,898.00”
  - column:Federal Student Loan Fees (2): 84.0 ⟵ “Federal Student Loan Fees | $42.00 | $42.00 | $84.00”
  - column:Total (2): 25268.0 ⟵ “Total | $12,634.00 | $12,634.00 | $25,268.00”
### `8688da134b5678f4` Milwaukee Area Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/tuition-fees.html (sha256 7c930ee84b53)
- issues: arrangement_unlabeled, cost_period_semester, multiple_total_rows, conflicting_sources:https://www.matc.edu/costs-scholarships-aid/documents/matc-resident-and-nonresident-academic-costs_2026_2027-final.pdf
- checks: {"columns": 4, "rows": 10}
  - column:Tuition and Fees: 555.3 ⟵ “Tuition and Fees | 555.30 | 1,110.60 | 2,221.20 | 2,663.50”
  - column:Student ID: 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare: 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/course: 200.0 ⟵ “Books $200/course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL: 771.3 ⟵ “TOTAL | 771.30 | 1,526.60 | 3,037.20 | 3,792.50”
  - column:Tuition and Fees (2): 671.1 ⟵ “Tuition and Fees | 671.10 | 1,342.20 | 2,684.40 | 3,355.50”
  - column:Student ID (2): 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare (2): 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/course (2): 200.0 ⟵ “Books $200/course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL (2): 887.1 ⟵ “TOTAL | 887.10 | 1,758.20 | 3,500.40 | 4,371.50”
  - column:Tuition and Fees: 1110.6 ⟵ “Tuition and Fees | 555.30 | 1,110.60 | 2,221.20 | 2,663.50”
  - column:Student ID: 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare: 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/course: 400.0 ⟵ “Books $200/course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL: 1526.6 ⟵ “TOTAL | 771.30 | 1,526.60 | 3,037.20 | 3,792.50”
  - column:Tuition and Fees (2): 1342.2 ⟵ “Tuition and Fees | 671.10 | 1,342.20 | 2,684.40 | 3,355.50”
  - column:Student ID (2): 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare (2): 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/course (2): 400.0 ⟵ “Books $200/course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL (2): 1758.2 ⟵ “TOTAL | 887.10 | 1,758.20 | 3,500.40 | 4,371.50”
  - column:Tuition and Fees: 2221.2 ⟵ “Tuition and Fees | 555.30 | 1,110.60 | 2,221.20 | 2,663.50”
  - column:Student ID: 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare: 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Books $200/course: 800.0 ⟵ “Books $200/course | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:TOTAL: 3037.2 ⟵ “TOTAL | 771.30 | 1,526.60 | 3,037.20 | 3,792.50”
  - … 15 more rows
### `d535a26187d6612f` Milwaukee Area Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.matc.edu/costs-scholarships-aid/documents/matc-resident-and-nonresident-academic-costs_2026_2027-final.pdf (sha256 0fedf28c979b)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.matc.edu/costs-scholarships-aid/tuition-fees.html
- checks: {"columns": 6, "rows": 18}
  - column:21.95 (natural science courses 5 credits): 415.6 ⟵ “21.95 (natural science courses 5 credits) | 415.60”
  - column:# Credits: 3 ⟵ “# Credits | 3 | 6 | 12 | 15”
  - column:Student ID: 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare: 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Estimated Books and: 200.0 ⟵ “Estimated Books and | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:# Credits (2): 3 ⟵ “# Credits | 3 | 6 | 12 | 15”
  - column:Student ID (2): 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare (2): 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Estimated Books and (2): 200.0 ⟵ “Estimated Books and | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:21.95 (natural science courses 5 credits) (2): 415.6 ⟵ “21.95 (natural science courses 5 credits) | 415.60”
  - column:# Credits (3): 3 ⟵ “# Credits | 3 | 6 | 12 | 15”
  - column:Student ID (3): 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare (3): 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Estimated Books and (3): 200.0 ⟵ “Estimated Books and | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:# Credits (4): 3 ⟵ “# Credits | 3 | 6 | 12 | 15”
  - column:Student ID (4): 9.0 ⟵ “Student ID | 9.00 | 9.00 | 9.00 | 9.00”
  - column:Student FastCare Healthcare (4): 7.0 ⟵ “Student FastCare Healthcare | 7.00 | 7.00 | 7.00 | 7.00”
  - column:Estimated Books and (4): 200.0 ⟵ “Estimated Books and | 200.00 | 400.00 | 800.00 | 1,000.00”
  - column:100: 183.1 ⟵ “100 | Associate Degree | $183.10 | $261.83”
  - column:200: 221.7 ⟵ “200 | College Parallel | 221.70 | 319.73”
  - column:300: 183.1 ⟵ “300 | Diploma | 183.10 | 261.83”
  - column:400: 183.1 ⟵ “400 | Career | 183.10 | 261.83”
  - column:500: 183.1 ⟵ “500 | Apprentice | 183.10 | N/A”
  - column:600: 75.0 ⟵ “600 | Community Service | 75.00 | 75.00”
  - column:# Credits: 6 ⟵ “# Credits | 3 | 6 | 12 | 15”
  - … 95 more rows
### `652d4521a817d099` Milwaukee Institute of Art & Design — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.miad.edu/financial-aid/cost-tuition-fees/cost-of-attendance (sha256 eb0239a51136)
- issues: ambiguous_year_labels
- checks: {"columns": 2, "components_reconcile": true, "rows": 8}
  - off_campus_not_with_family:Tuition: 44880 ⟵ “Tuition | $44,880 | $44,880”
  - off_campus_not_with_family:Fees: 1948 ⟵ “Fees | $1,948 | $1,948”
  - off_campus_not_with_family:Food and housing: 12246 ⟵ “Food and housing | $12,246 | $3,922”
  - off_campus_not_with_family:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,950”
  - off_campus_not_with_family:Books and supplies: 1130 ⟵ “Books and supplies | $1,130 | $1,130”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 860 ⟵ “Miscellaneous Personal Expenses | $860 | $860”
  - off_campus_not_with_family:Federal Student Loan Fees: 72 ⟵ “Federal Student Loan Fees | $72 | $72”
  - off_campus_not_with_family:Total Cost of Attendance: 62136 ⟵ “Total Cost of Attendance | $62,136 | $54,762”
  - with_parents_or_family:Tuition: 44880 ⟵ “Tuition | $44,880 | $44,880”
  - with_parents_or_family:Fees: 1948 ⟵ “Fees | $1,948 | $1,948”
  - with_parents_or_family:Food and housing: 3922 ⟵ “Food and housing | $12,246 | $3,922”
  - with_parents_or_family:Transportation: 1950 ⟵ “Transportation | $1,000 | $1,950”
  - with_parents_or_family:Books and supplies: 1130 ⟵ “Books and supplies | $1,130 | $1,130”
  - with_parents_or_family:Miscellaneous Personal Expenses: 860 ⟵ “Miscellaneous Personal Expenses | $860 | $860”
  - with_parents_or_family:Federal Student Loan Fees: 72 ⟵ “Federal Student Loan Fees | $72 | $72”
  - with_parents_or_family:Total Cost of Attendance: 54762 ⟵ “Total Cost of Attendance | $62,136 | $54,762”
### `fa537cfd6a635089` Milwaukee School of Engineering — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.msoe.edu/admissions-aid/financial-aid-scholarships/financial-aid-basics/faq/ (sha256 3e2a55043f39)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “However, if your inability to obtain parental information is due to unusual circumstances (parental incarceration, abuse, abandonment, etc.), please contact our office to inquire about filing the FAFSA.”
### `391a1f68a1cfce6f` Moraine Park Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.morainepark.edu/drop-withdraw/late-withdrawal-appeal/ (sha256 8dfc69bd185b)
- issues: semantic_review_required, conflicting_sources:https://catalog.morainepark.edu/billing/refund-appeal/,https://catalog.morainepark.edu/billing/refund-appeal/refund-appeal.pdf,https://catalog.morainepark.edu/financial-aid-guide/overview/circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other Unusual Circumstances Beyond Your Control: (such as: fire or natural disaster occurred at your home or a legal matter).”
### `3a416eccebeb3b09` Moraine Park Technical College — appeals 2026-27 [new] (labeled_in_title)
- source: https://catalog.morainepark.edu/billing/refund-appeal/refund-appeal.pdf (sha256 c1f47e7def89)
- issues: semantic_review_required, conflicting_sources:https://catalog.morainepark.edu/billing/refund-appeal/,https://catalog.morainepark.edu/drop-withdraw/late-withdrawal-appeal/,https://catalog.morainepark.edu/financial-aid-guide/overview/circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other unusual circumstances beyond your control: (such as a ﬁre or natural disaster occurred at your home, or a legal matter).”
### `5f6ee2cabd4f14f9` Moraine Park Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.morainepark.edu/pay-for-college/financial-aid/satisfactory-academic-progress-standards/ (sha256 eebc2c7927f5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You can document your extenuating circumstances and reason for not meeting SAP by completing the Appeal Form, submitting a letter explaining the situation and attaching third party documentation.”
  - sentence: sap_appeal ⟵ “What can I do if my SAP appeal is denied?”
### `718722d0ab212b0b` Moraine Park Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.morainepark.edu/pay-for-college/financial-aid/ (sha256 0cd9cf9f1c4e)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Click here to apply for Financial Aid You’ll need this: Moraine Park’s Financial Aid School Code is 005303 How to Create an Account and Username (FSA ID) for StudentAid.gov Students with special circumstances (loss of a job, etc.) or unusual circumstances (human trafficking, refugee or asylee status, parental abandonment, incarceration) are encouraged to work directly with the financial aid office”
  - sentence: need_based_special_circumstances ⟵ “Both the Special Circumstances Review Form and Dependency Override Form are available online via our Financial Aid Forms page.”
### `99704575a493b456` Moraine Park Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.morainepark.edu/financial-aid-guide/overview/circumstances/ (sha256 d2b0a925d27a)
- issues: semantic_review_required, conflicting_sources:https://catalog.morainepark.edu/billing/refund-appeal/,https://catalog.morainepark.edu/billing/refund-appeal/refund-appeal.pdf,https://catalog.morainepark.edu/drop-withdraw/late-withdrawal-appeal/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances may include paid medical or dental expenses not covered by insurance, a reduction or loss in income or benefits, or paid tuition expenses for children attending a private elementary or secondary school and excessive travel miles.”
  - sentence: need_based_special_circumstances ⟵ “Find the Special Circumstances Review Form at Financial Aid Forms or email the financial aid office.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances The Department of Education determines a student's status as dependent or independent by the answers the student provides on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “Students who have unusual circumstances can request an override by submitting an Unusual Circumstances/Dependency Override Request Form (find at Financial Aid Forms).”
### `9b12f41a56a0ad75` Moraine Park Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.morainepark.edu/billing/refund-appeal/ (sha256 583426607713)
- issues: semantic_review_required, conflicting_sources:https://catalog.morainepark.edu/billing/refund-appeal/refund-appeal.pdf,https://catalog.morainepark.edu/drop-withdraw/late-withdrawal-appeal/,https://catalog.morainepark.edu/financial-aid-guide/overview/circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other unusual circumstances beyond your control: (such as a fire or natural disaster occurred at your home, or a legal matter).”
### `e30212c354f373cb` Moraine Park Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.morainepark.edu/financial-aid-guide/overview/circumstances/ (sha256 d2b0a925d27a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency overrides are intended for students who can prove and fully document exceptional circumstances.”
### `5c8252a74d06138c` Moraine Park Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.morainepark.edu/pay-for-college/cost-of-your-education/ (sha256 f770fcf8aa98)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 6}
  - off_campus_not_with_family:Tuition and Fees: 5240.0 ⟵ “Tuition and Fees | $5,240.00”
  - off_campus_not_with_family:Books and Supplies: 1463.0 ⟵ “Books and Supplies | $1,463.00”
  - off_campus_not_with_family:Food and Housing: 10910.0 ⟵ “Food and Housing | $10,910.00”
  - off_campus_not_with_family:Personal: 3169.0 ⟵ “Personal | $3,169.00”
  - off_campus_not_with_family:Transportation: 3899.0 ⟵ “Transportation | $3,899.00”
  - off_campus_not_with_family:Total: 24651.0 ⟵ “Total | $24,651.00”
### `c92df890f73cc2d0` Moraine Park Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.morainepark.edu/academics/credit-for-prior-learning/ap-advanced-placement-exam/ (sha256 01096525ea40)
- issues: merged_score_cells, course_column_missing
- checks: {"distinct_exams": 30, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition (score of 3) | 801-136 English Composition I | 3 | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 3]:  ⟵ “English Language & Composition (score of 4 or 5) (6 total credits awarded) | 801-136 English Composition I & 108-223 English Composition II | 3 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition (score of 3) | 801-993 Literature Elective | 3 | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 3]:  ⟵ “English Literature and Composition (score of 4 or 5) (6 total credits awarded) | 801-993 Literature Elective & 801-136 English Composition I | 3 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language and Culture | 802-991 Foreign Language Elective | 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture | 802-991 Foreign Language Elective | 4”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language and Culture | 802-991 Foreign Language Elective | 4”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|4]:  ⟵ “Japanese Language and Culture | 802-991 Foreign Language Elective | 4”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin Language and Culture | 802-991 Foreign Language Elective | 4”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4]:  ⟵ “Spanish Language and Culture | 802-171 Spanish 1 | 4”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 815-991 Art Elective | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 805-991 Music Elective | 3”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 806-992 Biology Elective | 4”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 804-198 Calculus 1 | 4”
  - equivalencies[AP-CALCULUS-BC|4 4]:  ⟵ “Calculus BC | 804-198 Calculus 1 and 804-199 Calculus 2 | 4 4”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 806-134 General Chemistry | 4”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 806-991 Natural Science Elective | 3”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics 1 | 806-143 College Physics 1 | 3”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics 2 | 806-991 Natural Science Elective | 3”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C-Electricity & Magnetism | 806-991 Natural Science Elective | 3”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C-Mechanics | 806-991 Natural Science Elective | 3”
  - equivalencies[AP-PRECALCULUS|5]:  ⟵ “Pre-Calculus | 804-991 Math Elective | 5”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 804-189 Introduction to Statistics | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 809-998 Sociology Elective | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 803-991 History Elective | 3”
  - … 7 more rows
### `c9ecd0169d985b4d` Mount Mary University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://mtmary.edu/_files/documents/academics/ap_ib_clep_dsst_map_3_ada.pdf (sha256 aee26036bf9f)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 30, "equivalencies": 59, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|3]:  ⟵ “Biology                                        3              3           BIO 100                Core: Scientific Inquiry”
  - equivalencies[CLEP-CALCULUS|3]:  ⟵ “Calculus AB                                    3              4           MAT 251                Core: Math Course”
  - equivalencies[CLEP-CALCULUS|3]:  ⟵ “Calculus BC                                    3              8           MAT 251 & 252          Core: Math Course”
  - equivalencies[CLEP-CHEMISTRY|3]:  ⟵ “Chemistry                                      3              4           CHE 113                Core: Scientific Inquiry”
  - equivalencies[CLEP-CHEMISTRY|4]:  ⟵ “Chemistry                                      4              8           CHE 113 & 114          Core: Scientific Inquiry”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature and Composition             3              3           ENG 900                Core: Artistic Inquiry”
  - equivalencies[CLEP-FRENCH-LANGUAGE|3]:  ⟵ “French Language and Culture                    3              3           FRE 101                Core: World Language”
  - equivalencies[CLEP-GERMAN-LANGUAGE|3]:  ⟵ “German Language and Culture                    3              3           GER 101                Core: World Language”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Macroeconomics                                 3              3           BUS 302                Elective or Program Requirement”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3]:  ⟵ “Microeconomics                                 3              3           BUS 301                Elective or Program Requirement”
  - equivalencies[CLEP-PRECALCULUS|3]:  ⟵ “Precalculus                                    3              6           MAT 111 & 113          Core: Math Course”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Psychology                                     3              3           PSY 103                Core: Human Connection”
  - equivalencies[CLEP-SPANISH-LANGUAGE|3]:  ⟵ “Spanish Language and Culture                   3              3           SPA 203                Core: World Language”
  - equivalencies[CLEP-SPANISH-LANGUAGE|4]:  ⟵ “Spanish Language and Culture                   4              3           SPA 222 or 223         Core: World Language”
  - equivalencies[CLEP-SPANISH-LANGUAGE|3]:  ⟵ “Spanish Literature and Culture                 3              3           SPA 228                Core: Artistic Inquiry”
  - equivalencies[CLEP-BIOLOGY|4]:  ⟵ “Biology                                        4              3           BIO 105                Core: Scientific Inquiry”
  - equivalencies[CLEP-CHEMISTRY|4]:  ⟵ “Chemistry                                      4              3           CHE 105                Core: Scientific Inquiry”
  - equivalencies[CLEP-FRENCH-LANGUAGE|4]:  ⟵ “French                                         4              3           FRE 101                Core: World Language”
  - equivalencies[CLEP-GERMAN-LANGUAGE|4]:  ⟵ “German                                         4              3           GER 101                Core: World Language”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|4]:  ⟵ “Psychology                                     4              3           PSY 103                Core: Human Connection”
  - equivalencies[CLEP-SPANISH-LANGUAGE|4]:  ⟵ “Spanish                                        4              3           SPA 203                Core: World Language”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                            50             3           POS 213               Core: Civic Engagement”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                            50             3           ENG 308               Core: Artistic Inquiry”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature          50             3           ENG 103               Core: Artistic Inquiry”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                        50             3           BIO 105               Core: Scientific Inquiry”
  - … 34 more rows
### `70629b3484e43b2d` Nicolet Area Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nicoletcollege.edu/about/college-information/administrative-policies/20-student-services/222-satisfactory-academic (sha256 7f06087aa017)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “A new 150% maximum time frame begins when a student changes or adds a program after receiving an approved SAP appeal.”
  - sentence: sap_appeal ⟵ “Appeal Process Students who fail to meet Satisfactory Academic Progress (SAP) standards may submit an appeal if they have documented extenuating circumstances that impacted their academic performance (e.g., illness, injury, death of a family member, or other significant circumstances).”
  - sentence: sap_appeal ⟵ “Students may submit no more than three SAP appeals.”
### `f33128c763cc55ee` Nicolet Area Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nicoletcollege.edu/cost-aid/financial-aid (sha256 d0d400b970b3)
- issues: semantic_review_required, conflicting_sources:https://www.nicoletcollege.edu/cost-aid/frequently-asked-questions
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special and Unusual Circumstances Federal financial aid is based on the information you provide on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If your current situation isn't accurately reflected on your FAFSA, you may qualify for a review based on special or unusual circumstances.”
### `f74076f8be7b3a23` Nicolet Area Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.nicoletcollege.edu/cost-aid/frequently-asked-questions (sha256 9f68dcfd0e87)
- issues: semantic_review_required, conflicting_sources:https://www.nicoletcollege.edu/cost-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Do you qualify for a review based on a special or unusual circumstance?”
  - sentence: need_based_special_circumstances ⟵ “If your current situation isn't accurately reflected on your FAFSA, you may qualify for a review based on special or unusual circumstances.”
### `1698a1ee88df328b` Nicolet Area Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nicoletcollege.edu/cost-aid/cost-attendance (sha256 a0fd4cfd24bc)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees*: 5256 ⟵ “Tuition and Fees* | $5,256 | $5,256”
  - with_parents_or_family:Books, Course Materials, Supplies, and Equipment**: 1176 ⟵ “Books, Course Materials, Supplies, and Equipment** | $1,176 | $1,176”
  - with_parents_or_family:Food and Housing**: 3223 ⟵ “Food and Housing** | $3,223 | $10,910”
  - with_parents_or_family:Miscellaneous Personal Expenses**: 3084 ⟵ “Miscellaneous Personal Expenses** | $3,084 | $3,084”
  - with_parents_or_family:Transportation**: 3899 ⟵ “Transportation** | $3,899 | $3,899”
  - with_parents_or_family:Total Costs: 16638 ⟵ “Total Costs | $16,638 | $24,325”
  - with_parents_or_family:Total Indirect Costs**: 11382 ⟵ “Total Indirect Costs** | $11,382 | $19,069”
  - off_campus_not_with_family:Tuition and Fees*: 5256 ⟵ “Tuition and Fees* | $5,256 | $5,256”
  - off_campus_not_with_family:Books, Course Materials, Supplies, and Equipment**: 1176 ⟵ “Books, Course Materials, Supplies, and Equipment** | $1,176 | $1,176”
  - off_campus_not_with_family:Food and Housing**: 10910 ⟵ “Food and Housing** | $3,223 | $10,910”
  - off_campus_not_with_family:Miscellaneous Personal Expenses**: 3084 ⟵ “Miscellaneous Personal Expenses** | $3,084 | $3,084”
  - off_campus_not_with_family:Transportation**: 3899 ⟵ “Transportation** | $3,899 | $3,899”
  - off_campus_not_with_family:Total Costs: 24325 ⟵ “Total Costs | $16,638 | $24,325”
  - off_campus_not_with_family:Total Indirect Costs**: 19069 ⟵ “Total Indirect Costs** | $11,382 | $19,069”
### `7f6e5991d143d3dd` Nicolet Area Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.nicoletcollege.edu/sites/default/files/2026-07/clep_crosswalk_july_2026.pdf (sha256 c97eb5699edc)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 34, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government                             3       3           50     American Government 803-227”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|3]:  ⟵ “History of the United States I (Early           3       3           50     History of American People to 1877 803-215”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|3]:  ⟵ “History of the United States II (1865 to        3       3           50     History of American People from 1877 803-219”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|3]:  ⟵ “Human growth and Development                    3       3           50     Developmental Psychology 809-188”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|3]:  ⟵ “Introduction to Educational Psychology          3       3           50     Educational Psychology 809-254”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Introductory Psychology                         3       3           50     Intro to Psychology 809-198”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|3]:  ⟵ “Introductory Sociology                          3       3           50     Introduction to Sociology 809-196”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Principles of Macroeconomics                    3       3           50     Principles of Macroeconomics 809-287”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3]:  ⟵ “Principles of Microeconomics                    3       3           50     Principles of Microeconomics 809-291”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|6]:  ⟵ “Social Sciences and History                     6       6           50     Social Science Credits (3)”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|3]:  ⟵ “Western Civilization I (Ancient Near East       3       3           50     World History to 1500 803-258”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|3]:  ⟵ “Western Civilization II (1648 to the            3       3           50     World History since 1500 803-259”
  - equivalencies[CLEP-AMERICAN-LITERATURE|3]:  ⟵ “American Literature                             3       3           50     American Lit. 1865 to Present 801-239”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|3]:  ⟵ “Analyzing and Interpreting Literature           3       3           50     Introduction to Literature 801-255”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|6]:  ⟵ “College Composition                             6       6           50     English Composition I 801-219”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|3]:  ⟵ “College Composition Modular                     3       3           50     English Composition I 801-219”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature                              3       3           50     British Literature 19th Century to Present 801-235”
  - equivalencies[CLEP-HUMANITIES|3]:  ⟵ “Humanities                                      3       3           50     Humanities Credits (3)”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|6]:  ⟵ “College Mathematics                   6    6    50   Quantitative Reasoning 804-250”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra                       3    4    50   Intermediate Algebra with Aplications 804-118”
  - equivalencies[CLEP-PRECALCULUS|3]:  ⟵ “Precalculus                           3    4    50   Algebra for Calculus 804-224”
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus                              4    5    50   Calculus & Analytic Geometry I 804-236”
  - equivalencies[CLEP-BIOLOGY|6]:  ⟵ “Biology                               6    6    50   Principles of Biology 806-201”
  - equivalencies[CLEP-CHEMISTRY|6]:  ⟵ “Chemistry                             6    6    50   College Chemistry I 806-245”
  - equivalencies[CLEP-NATURAL-SCIENCES|6]:  ⟵ “Natural Sciences                      6    3    50   Natural Science credits 806-33920 (3)”
  - … 9 more rows
### `bcd6afe91b502f87` Northcentral Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ntc.edu/academics-training/programs/all/technical-diploma/practical-nursing (sha256 722571069ed9)
- issues: residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition and Fees*: 2620 ⟵ “Tuition and Fees* | $2,620 | $1,965 | $1,310 | $655”
  - off_campus_not_with_family:Books, Course Materials, Supplies and Equipment: 732 ⟵ “Books, Course Materials, Supplies and Equipment | $732 | $549 | $366 | $183”
  - off_campus_not_with_family:Living Expenses (Housing & Food): 5455 ⟵ “Living Expenses (Housing & Food) | $5,455 | $5,455 | $5,455 | $0”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1542 ⟵ “Miscellaneous Personal Expenses | $1,542 | $1,542 | $1,542 | $0”
  - off_campus_not_with_family:Transportation: 1950 ⟵ “Transportation | $1,950 | $1,950 | $1,950 | $1,950”
  - off_campus_not_with_family:Federal Loan Fees: 43 ⟵ “Federal Loan Fees | $43 | $43 | $43 | Not applicable”
  - off_campus_not_with_family:Total Estimated Cost of Attendance: 12342 ⟵ “Total Estimated Cost of Attendance | $12,342 | $11,504 | $10,666 | $2,788”
  - off_campus_not_with_family:Tuition and Fees*: 1965 ⟵ “Tuition and Fees* | $2,620 | $1,965 | $1,310 | $655”
  - off_campus_not_with_family:Books, Course Materials, Supplies and Equipment: 549 ⟵ “Books, Course Materials, Supplies and Equipment | $732 | $549 | $366 | $183”
  - off_campus_not_with_family:Living Expenses (Housing & Food): 5455 ⟵ “Living Expenses (Housing & Food) | $5,455 | $5,455 | $5,455 | $0”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1542 ⟵ “Miscellaneous Personal Expenses | $1,542 | $1,542 | $1,542 | $0”
  - off_campus_not_with_family:Transportation: 1950 ⟵ “Transportation | $1,950 | $1,950 | $1,950 | $1,950”
  - off_campus_not_with_family:Federal Loan Fees: 43 ⟵ “Federal Loan Fees | $43 | $43 | $43 | Not applicable”
  - off_campus_not_with_family:Total Estimated Cost of Attendance: 11504 ⟵ “Total Estimated Cost of Attendance | $12,342 | $11,504 | $10,666 | $2,788”
  - off_campus_not_with_family:Tuition and Fees*: 1310 ⟵ “Tuition and Fees* | $2,620 | $1,965 | $1,310 | $655”
  - off_campus_not_with_family:Books, Course Materials, Supplies and Equipment: 366 ⟵ “Books, Course Materials, Supplies and Equipment | $732 | $549 | $366 | $183”
  - off_campus_not_with_family:Living Expenses (Housing & Food): 5455 ⟵ “Living Expenses (Housing & Food) | $5,455 | $5,455 | $5,455 | $0”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 1542 ⟵ “Miscellaneous Personal Expenses | $1,542 | $1,542 | $1,542 | $0”
  - off_campus_not_with_family:Transportation: 1950 ⟵ “Transportation | $1,950 | $1,950 | $1,950 | $1,950”
  - off_campus_not_with_family:Federal Loan Fees: 43 ⟵ “Federal Loan Fees | $43 | $43 | $43 | Not applicable”
  - off_campus_not_with_family:Total Estimated Cost of Attendance: 10666 ⟵ “Total Estimated Cost of Attendance | $12,342 | $11,504 | $10,666 | $2,788”
  - off_campus_not_with_family:Tuition and Fees*: 655 ⟵ “Tuition and Fees* | $2,620 | $1,965 | $1,310 | $655”
  - off_campus_not_with_family:Books, Course Materials, Supplies and Equipment: 183 ⟵ “Books, Course Materials, Supplies and Equipment | $732 | $549 | $366 | $183”
  - off_campus_not_with_family:Living Expenses (Housing & Food): 0 ⟵ “Living Expenses (Housing & Food) | $5,455 | $5,455 | $5,455 | $0”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 0 ⟵ “Miscellaneous Personal Expenses | $1,542 | $1,542 | $1,542 | $0”
  - … 2 more rows
### `c4c7e4571e3608bd` Northcentral Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.ntc.edu/admissions/credit-prior-learning/national-exams/ap-exams-accepted (sha256 9ca4b868e058)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 12, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language & Composition | 3 | 10-801-195 | Written Communication | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “AP English Language & Composition | 3 | 10-801-136 | English Composition 1 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “AP Macroeconomics | 3 | 10-809-195 | Economics | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “AP Microeconomics | 3 | 10-809-195 | Economics | 3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “AP Psychology | 3 | 10-809-198 | Introduction to Psychology | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “AP United States Government & Politics | 3 | 10-809-122 | Intro to American Government | 3”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “AP Precalculus | 3 | 10-804-195 | College Algebra w/ Apps | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “AP Calculus AB | 3 | 10-804-198 | Calculus 1 | 4”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “AP Statistics | 3 | 10-804-189 | Introductory Statistics | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “AP Computer Science A | 3 | 10-152-500 | IT Development & Design Fundamentals | 1”
  - equivalencies[AP-COMPUTER-SCIENCE-A|10-152-501]:  ⟵ “AP Computer Science A | 10-152-501 | Programming Concepts A | 1”
  - equivalencies[AP-COMPUTER-SCIENCE-A|10-152-502]:  ⟵ “AP Computer Science A | 10-152-502 | Programming Concepts B | 1”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “AP Biology | 3 | 10-806-114 | General Biology | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “AP Chemistry | 3 | 10-806-134 | General Chemistry | 4”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “AP Physics 1 and 2 | 3 | 10-806-143 | College Physics 1 | 3”
### `143190eda2766fde` Northeast Wisconsin Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.nwtc.edu/admissions-and-aid/financial-aid/how-to-apply/eligibility/special-circumstances (sha256 759363a2a4c3)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Cost Of Attendance Adjustment Appeal The Cost of Attendance (COA) is an educational budget used in the determination of financial aid.”
  - sentence: budget_increase ⟵ “These are the standard components that are included in the Cost of Attendance calculation (starting with the 2023-2024 aid year): Tuition & Fees Federal Student Loan Fees (Actual) Books, Course Materials, Supplies, & Equipment Living Expenses Transportation Miscellaneous Personal Expenses Examples of situations that may qualify as an appeal for Cost of Attendance adjustments include, but are not l”
### `143c746221fc3e2e` Northeast Wisconsin Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nwtc.edu/admissions-and-aid/financial-aid/satisfactory-progress (sha256 f41076a89347)
- issues: semantic_review_required, conflicting_sources:https://www.nwtc.edu/getmedia/2f475a54-9893-4517-9862-3b6c63919cf4/SAP-Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Suspended students are not eligible to receive financial aid until an appeal is approved or satisfactory academic progress standards are met.”
  - sentence: sap_appeal ⟵ “Maximum Time Frame Examples | Program | Credits Required for Graduation | Max Credits (including transfer credits) | Accounting Associate Degree | 65 | 98 | Accounting Assistant Technical Diploma | 31 | 47 SAP Appeals Students have the right to appeal their suspension status based on non-academic, mitigating circumstances (i.e., death of an immediate family member including father, mother, sibling”
  - sentence: sap_appeal ⟵ “Suspension due to not meeting GPA or Completion standards: To appeal a financial aid suspension, students must complete the Satisfactory Academic Progress appeal form.”
  - sentence: sap_appeal ⟵ “Required documentation for a Satisfactory Academic Progress appeal includes a letter from the student that explains the specific circumstances that prevented the student from meeting the Satisfactory Academic Progress standards and third-party documentation.”
### `1b0882f6336d19a7` Northeast Wisconsin Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nwtc.edu/admissions-and-aid/financial-aid/how-to-apply/eligibility (sha256 b037a7f66e95)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Students with Special or Unusual Circumstances The federal government makes every effort to capture a student or family's financial situation using the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “Listed are different categories of situations in which students will want to work directly with the Financial Aid office: Special Circumstances – change in household income that may reduce a student’s ability to pay for college (loss of job, separation/divorce of student or parent, etc.) Cost Of Attendance Adjustment Appeal - Students may experience unforeseen expenses during an academic year that”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances - Dependency Override Request – unusual situation between students and parents where it is not possible or advisable to include parental information on the FAFSA Unable to Provide Parents’ Information – When parents refuse to provide their information on the FAFSA and are not financially supporting student.”
  - sentence: need_based_special_circumstances ⟵ “Learn more about special circumstances.”
### `33985d1e54c1f558` Northeast Wisconsin Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nwtc.edu/getmedia/2f475a54-9893-4517-9862-3b6c63919cf4/SAP-Policy.pdf (sha256 f28f5115e894)
- issues: semantic_review_required, conflicting_sources:https://www.nwtc.edu/admissions-and-aid/financial-aid/satisfactory-progress
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Suspended students are not eligible to receive ﬁnancial aid until an appeal is approved or satisfactory academic progress standards are met.”
  - sentence: sap_appeal ⟵ “Suspended students may also regain ﬁnancial aid eligibility if a Satisfactory Academic Progress appeal is approved.”
  - sentence: sap_appeal ⟵ “If the appeal is approved, students will be placed on an Academic Plan for the remainder of their program or until they meet the minimum cumulative GPA of 2.0 and minimum completion rate of 67%. • Suspension due to not meeting GPA or Completion standards: To appeal a ﬁnancial aid suspension, students must complete the Satisfactory Academic Progress appeal form.”
  - sentence: sap_appeal ⟵ “Required documentation for a Satisfactory Academic Progress appeal includes a letter from the student that explains the speciﬁc circumstances that prevented the student from meeting the Satisfactory Academic Progress standards and third-party documentation.”
### `5b4d5e8372e707d9` Northeast Wisconsin Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.nwtc.edu/admissions-and-aid/financial-aid/how-to-apply/eligibility/special-circumstances (sha256 759363a2a4c3)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “It is very important to note that when it comes to dependency overrides, there is a distinction between parents who are unable to provide information and parents who are unwilling to complete a child’s FAFSA.”
  - sentence: dependency_override ⟵ “Please note that submission of a petition does not guarantee that a dependency override will be approved.”
### `8b05ba7cfc57221d` Northeast Wisconsin Technical College — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.nwtc.edu/admissions-and-aid/financial-aid/how-to-apply/eligibility/special-circumstances (sha256 759363a2a4c3)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 13}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances | NWTC Cookies on NWTC's Website This website uses cookies to provide an enhanced user experience.”
  - sentence: need_based_special_circumstances ⟵ “Listed are different categories of situations in which students will want to work directly with the Financial Aid office: Types of Special Circumstances Special Circumstances - Reduction of Income The Free Application for Federal Student Aid (FAFSA) requires students to provide household income and tax data.”
  - sentence: need_based_special_circumstances ⟵ “Sometimes there may be a special circumstance that reduces a student’s ability to pay for college which cannot be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office has a process that allows the FAFSA applicant to document a special circumstance and, if approved, allows us to recalculate an EFC and re-evaluate a financial aid package.”
  - sentence: need_based_special_circumstances ⟵ “A review of special circumstances does not automatically guarantee an EFC adjustment nor an increase in financial aid funding.”
  - sentence: need_based_special_circumstances ⟵ “Examples of situations that may qualify as special circumstance for FAFSA adjustments include, but are not limited to: Loss of income from unemployment, furlough, disability, or retirement Separation or divorce of a person listed on the FAFSA after the FAFSA has already been completed.”
### `c9fac94bb923f537` Northeast Wisconsin Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nwtc.edu/admissions-and-aid/paying-for-college/tuition-and-fees (sha256 22c67baa8ce0)
- issues: residency_unknown
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 5288 ⟵ “Tuition and Fees | $5,288 | $3,966 | $2,644 | $1,322”
  - with_parents_or_family:Federal Student Loan Fees (Actual): 86 ⟵ “Federal Student Loan Fees (Actual) | $86 | $86 | $86 | $0”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 1472 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,472 | $1,104 | $736 | $368”
  - with_parents_or_family:Living Expenses: 3224 ⟵ “Living Expenses | $3,224 | $3,224 | $3,224 | $0”
  - with_parents_or_family:Miscellaneous Personal Expenses: 3084 ⟵ “Miscellaneous Personal Expenses | $3,084 | $3,084 | $3,084 | $0”
  - with_parents_or_family:Transportation: 3900 ⟵ “Transportation | $3,900 | $3,900 | $3,900 | $3,900”
  - with_parents_or_family:Total Budget: 17054 ⟵ “Total Budget | $17,054 | $15,364 | $13,674 | $5,590”
  - with_parents_or_family:Tuition and Fees: 3966 ⟵ “Tuition and Fees | $5,288 | $3,966 | $2,644 | $1,322”
  - with_parents_or_family:Federal Student Loan Fees (Actual): 86 ⟵ “Federal Student Loan Fees (Actual) | $86 | $86 | $86 | $0”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 1104 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,472 | $1,104 | $736 | $368”
  - with_parents_or_family:Living Expenses: 3224 ⟵ “Living Expenses | $3,224 | $3,224 | $3,224 | $0”
  - with_parents_or_family:Miscellaneous Personal Expenses: 3084 ⟵ “Miscellaneous Personal Expenses | $3,084 | $3,084 | $3,084 | $0”
  - with_parents_or_family:Transportation: 3900 ⟵ “Transportation | $3,900 | $3,900 | $3,900 | $3,900”
  - with_parents_or_family:Total Budget: 15364 ⟵ “Total Budget | $17,054 | $15,364 | $13,674 | $5,590”
  - with_parents_or_family:Tuition and Fees: 2644 ⟵ “Tuition and Fees | $5,288 | $3,966 | $2,644 | $1,322”
  - with_parents_or_family:Federal Student Loan Fees (Actual): 86 ⟵ “Federal Student Loan Fees (Actual) | $86 | $86 | $86 | $0”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 736 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,472 | $1,104 | $736 | $368”
  - with_parents_or_family:Living Expenses: 3224 ⟵ “Living Expenses | $3,224 | $3,224 | $3,224 | $0”
  - with_parents_or_family:Miscellaneous Personal Expenses: 3084 ⟵ “Miscellaneous Personal Expenses | $3,084 | $3,084 | $3,084 | $0”
  - with_parents_or_family:Transportation: 3900 ⟵ “Transportation | $3,900 | $3,900 | $3,900 | $3,900”
  - with_parents_or_family:Total Budget: 13674 ⟵ “Total Budget | $17,054 | $15,364 | $13,674 | $5,590”
  - with_parents_or_family:Tuition and Fees: 1322 ⟵ “Tuition and Fees | $5,288 | $3,966 | $2,644 | $1,322”
  - with_parents_or_family:Federal Student Loan Fees (Actual): 0 ⟵ “Federal Student Loan Fees (Actual) | $86 | $86 | $86 | $0”
  - with_parents_or_family:Books, Course Materials, Supplies, & Equipment: 368 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,472 | $1,104 | $736 | $368”
  - with_parents_or_family:Living Expenses: 0 ⟵ “Living Expenses | $3,224 | $3,224 | $3,224 | $0”
  - … 3 more rows
### `393cac96b4190dae` Northeast Wisconsin Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.nwtc.edu/admissions-and-aid/complete-a-test-or-assessment/college-level-examination-program-clep (sha256 e9e73380c75f)
- issues: credits_implausible, score_scale_mismatch
- checks: {"distinct_exams": 22, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|American Government (50)]:  ⟵ “American Government (50) | Intro to American Government (10809122) | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|American Literature (50)]:  ⟵ “American Literature (50) | Ethnic Literature (20801212) | 3”
  - equivalencies[CLEP-BIOLOGY|Biology (50)]:  ⟵ “Biology (50) | General Biology (10806114) | 4”
  - equivalencies[CLEP-CALCULUS|Calculus (50)]:  ⟵ “Calculus (50) | Calculus 1 (10804198) | 4”
  - equivalencies[CLEP-CHEMISTRY|Chemistry (50-62)]:  ⟵ “Chemistry (50-62) | General Chemistry (10806134) orCollege Chemistry 1 (10806135) | 45”
  - equivalencies[CLEP-CHEMISTRY|Chemistry (63+)]:  ⟵ “Chemistry (63+) | College Chemistry 1 (10806135) andCollege Chemistry 2 (10506136) | 10”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|College Algebra (50)]:  ⟵ “College Algebra (50) | College Algebra w/Apps (10804195) | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|College Composition (50)]:  ⟵ “College Composition (50) | English Composition 1 (10801136) | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|College Mathematics (50)]:  ⟵ “College Mathematics (50) | Quantitative Reasoning (10804135) | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|College Mathematics (70)]:  ⟵ “College Mathematics (70) | Intermediate Algebra w/Apps (10804118) | 4”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|Financial Accounting (50)]:  ⟵ “Financial Accounting (50) | Accounting 1 (10101110) | 4”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language: Levels 1 & 2 (50)]:  ⟵ “French Language: Levels 1 & 2 (50) | Satisfies World Language- Assoc of Arts/Science | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German Language: Levels 1 & 2 (50)]:  ⟵ “German Language: Levels 1 & 2 (50) | Satisfies World Language- Assoc of Arts/Science | 4”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|Human Growth and Development (50)]:  ⟵ “Human Growth and Development (50) | Developmental Psychology (10809188) | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|Information Systems (50)]:  ⟵ “Information Systems (50) | Intro to IT (10107107) | 1”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|Introductory Business Law (50)]:  ⟵ “Introductory Business Law (50) | Business Law & Ethics (10102150) | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|Introductory Psychology (50)]:  ⟵ “Introductory Psychology (50) | Intro to Psychology (10809198) | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|Introductory Sociology (50)]:  ⟵ “Introductory Sociology (50) | Intro to Sociology (10809196) | 3”
  - equivalencies[CLEP-PRECALCULUS|Precalculus (50)]:  ⟵ “Precalculus (50) | College Algebra & Trig w/Apps (10804197) | 5”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|Principles of Macroeconomics (50)]:  ⟵ “Principles of Macroeconomics (50) | Economics (10809195) | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|Principles of Macroeconomics (50)]:  ⟵ “Principles of Macroeconomics (50) | Principles of Macroeconomics (20809287) | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|Principles of Management (50)]:  ⟵ “Principles of Management (50) | Business Principles (10102158) | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|Principles of Marketing (50)]:  ⟵ “Principles of Marketing (50) | Marketing Principles (10104110) | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|Principles of Microeconomics (50)]:  ⟵ “Principles of Microeconomics (50) | Economics (10809195) | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|Principles of Microeconomics (50)]:  ⟵ “Principles of Microeconomics (50) | Principles of Microeconomics (20809291) | 3”
  - … 4 more rows
### `295ddb26e925d20f` Ripon College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://ripon.edu/admission/cost-and-financial-aid/apply-for-financial-aid/ (sha256 9653c0ee6386)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://ripon.edu/admission/cost-and-financial-aid/your-first-year-financial-aid-offer/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Notify the Office of Financial Aid in the case of special circumstances.”
### `4eb4bdf6ecd3a19d` Ripon College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ripon.edu/admission/cost-and-financial-aid/your-first-year-financial-aid-offer/ (sha256 0f00c191e258)
- issues: semantic_review_required, conflicting_sources:https://ripon.edu/admission/cost-and-financial-aid/apply-for-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Other Funding Sources to Notify Us About VA Benefits Outside Scholarships WI State Grants and Loans Tribal Affiliated Funds Next Steps Accept/Decline Aid Report Outside Scholarship Complete Loan Documents Special Circumstance Student Employment The student can accept or decline their scholarships, grants and loans at https://MyAid.ripon.edu/NetPartnerStudent/ Please download the instructions for c”
  - sentence: need_based_special_circumstances ⟵ “If your family has experienced a change in family income, job loss, extreme medical costs or other unusual situations that impact your ability to pay and your financial situation no longer reflects what is seen on your tax information from the FAFSA, you may be eligible for additional funding.”
  - sentence: need_based_special_circumstances ⟵ “Contact the Office of Financial Aid regarding a request for special circumstance form.”
### `e987c8b7fd106fb9` Southwest Wisconsin Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.swtc.edu/community/testing-center/clep-testing (sha256 19ed0f2bbeaa)
- issues: rows_without_score, credits_implausible
- checks: {"distinct_exams": 20, "equivalencies": 20, "rows_without_score": 20}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|None]:  ⟵ “Financial Accounting | 10-101-111 | Accounting 1 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|None]:  ⟵ “Principles of Macroeconomics | 20-809-211 | Principles of Macroeconomics | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|None]:  ⟵ “Introductory Business Law | 10-102-109 | Business Law 1 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|None]:  ⟵ “Principles of Management | 10-102-130 | Management Principles | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|None]:  ⟵ “Principles of Marketing | 10-104-130 | Marketing Principles | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|None]:  ⟵ “Principles of Microeconomics | 10-809-143 | Principles of Microeconomics | 3”
  - equivalencies[CLEP-BIOLOGY|None]:  ⟵ “Biology | 20-806-234 | General Biology | 4”
  - equivalencies[CLEP-CHEMISTRY|None]:  ⟵ “Chemistry | 10-806-109 OR20-806-209 | Fundamentals of ChemistryCollege Chemistry 1 | 33”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|None]:  ⟵ “College Algebra | 10-804-195 | College Algebra | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|None]:  ⟵ “College Mathematics | 10-804-107 OR10-804-113 OR31-804-305 | College MathematicsCollege Tech Math 1AApplied Math | 332”
  - equivalencies[CLEP-PRECALCULUS|None]:  ⟵ “Precalculus | 10-804-114 OR20-804-229 | College Technical Math 1BMath Analysis | 33”
  - equivalencies[CLEP-CALCULUS|None]:  ⟵ “Calculus | 20-804-231 | Calculus and Analytic Geometry 1 | 5”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|None]:  ⟵ “Human Growth and Development | 10-809-188 | Developmental Psychology | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|None]:  ⟵ “Introductory Psychology | 10-809-198 | Intro to Psychology | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|None]:  ⟵ “Introductory Sociology | 10-809-196 | Intro to Sociology | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|None]:  ⟵ “American Literature | 20-801-218 | American Literature: 1865 - Present | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|None]:  ⟵ “Analyzing and Interpreting Literature | 20-801-204 | Intro to Literature | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | 10-801-136 AND20-801-223 | English Composition 1English Composition 2 | 33”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|None]:  ⟵ “College Composition Modular | 10-801-136 | English Composition 1 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|None]:  ⟵ “English Literature | 20-801-204 | Intro to Literature | 3”
### `m4ece329976f464a` Southwest Wisconsin Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.swtc.edu/uploadedpdfs/academic/transfer/agreement-documents/Carroll-University-Early-Childhood-to-Teacher-Education.pdf (sha256 9f11ee06c75d)
- issues: ambiguous_year_labels, conflicting_values:min_grade
- checks: {"fields": ["min_grade"], "merged_pages": 5}
  - min_grade: C ⟵ “Only courses with a grade of “C” or better will be reviewed for transfer credit.”
  - residency_requirement_credits: 30 ⟵ “All WTCS transfer students must complete a minimum of 30 hours in residence with Bellevue University.”
  - min_grade: C ⟵ “Only courses for which students have received a grade of "C" or better will be considered for transfer. 4.”
  - min_grade: C ⟵ “MSOE will assemble lists of Social Sciences (SS), Humanities (HU), and other elective courses from WTCS that are approved to transfer under this transfer agreement if taken and successfully completed with a grade of C or better.”
### `1b7e04b3dc43d9df` University of Wisconsin-Eau Claire — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance (sha256 f7deb1c42322)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://barron.uwec.edu/tuition-financial-aid/tuition-fees/,https://www.uwec.edu/tuition-aid/tuition-fees
- checks: {"columns": 3, "rows": 2}
  - with_parents_or_family:Tuition + Fees: 10207 ⟵ “Tuition + Fees | $10,207 | $10,207 | $11,160 | $20,273 | $14,371 | $15,674”
  - with_parents_or_family:Living Expenses (Food/Housing): 2918 ⟵ “Living Expenses (Food/Housing) | $2,918 | $9,726 | $9,726 | $9,726 | $9,726 | $9,726”
  - column:Tuition + Fees: 14371 ⟵ “Tuition + Fees | $10,207 | $10,207 | $11,160 | $20,273 | $14,371 | $15,674”
  - column:Living Expenses (Food/Housing): 9726 ⟵ “Living Expenses (Food/Housing) | $2,918 | $9,726 | $9,726 | $9,726 | $9,726 | $9,726”
  - column:Tuition + Fees: 15674 ⟵ “Tuition + Fees | $10,207 | $10,207 | $11,160 | $20,273 | $14,371 | $15,674”
  - column:Living Expenses (Food/Housing): 9726 ⟵ “Living Expenses (Food/Housing) | $2,918 | $9,726 | $9,726 | $9,726 | $9,726 | $9,726”
### `1c557194007e311e` University of Wisconsin-Eau Claire — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.uwec.edu/tuition-aid/tuition-fees (sha256 38abd1fc1598)
- issues: conflicting_sources:https://barron.uwec.edu/tuition-financial-aid/tuition-fees/,https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition/fees*: 20674 ⟵ “Tuition/fees* | $10,407 | $11,772 | $15,983 | $20,674 | $14,654”
  - on_campus:Room**: 5405 ⟵ “Room** | $5,405 | $5,405 | $5,405 | $5,405 | $5,405”
  - on_campus:Meals***: 3910 ⟵ “Meals*** | $3,910 | $3,910 | $3,910 | $3,910 | $3,910”
  - on_campus:TOTAL: 29989 ⟵ “TOTAL | $19,722 | $21,087 | $25,298 | $29,989 | $23,969”
### `2a75a3ec6263906e` University of Wisconsin-Eau Claire — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwec.edu/tuition-aid/tuition-fees (sha256 38abd1fc1598)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://barron.uwec.edu/tuition-financial-aid/tuition-fees/,https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance
- checks: {"columns": 3, "components_reconcile": true, "rows": 4}
  - column:Tuition/fees*: 11772 ⟵ “Tuition/fees* | $10,407 | $11,772 | $15,983 | $20,674 | $14,654”
  - column:Room**: 5405 ⟵ “Room** | $5,405 | $5,405 | $5,405 | $5,405 | $5,405”
  - column:Meals***: 3910 ⟵ “Meals*** | $3,910 | $3,910 | $3,910 | $3,910 | $3,910”
  - column:TOTAL: 21087 ⟵ “TOTAL | $19,722 | $21,087 | $25,298 | $29,989 | $23,969”
  - column:Tuition/fees*: 15983 ⟵ “Tuition/fees* | $10,407 | $11,772 | $15,983 | $20,674 | $14,654”
  - column:Room**: 5405 ⟵ “Room** | $5,405 | $5,405 | $5,405 | $5,405 | $5,405”
  - column:Meals***: 3910 ⟵ “Meals*** | $3,910 | $3,910 | $3,910 | $3,910 | $3,910”
  - column:TOTAL: 25298 ⟵ “TOTAL | $19,722 | $21,087 | $25,298 | $29,989 | $23,969”
  - column:Tuition/fees*: 14654 ⟵ “Tuition/fees* | $10,407 | $11,772 | $15,983 | $20,674 | $14,654”
  - column:Room**: 5405 ⟵ “Room** | $5,405 | $5,405 | $5,405 | $5,405 | $5,405”
  - column:Meals***: 3910 ⟵ “Meals*** | $3,910 | $3,910 | $3,910 | $3,910 | $3,910”
  - column:TOTAL: 23969 ⟵ “TOTAL | $19,722 | $21,087 | $25,298 | $29,989 | $23,969”
### `52096db9d80adc9b` University of Wisconsin-Eau Claire — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance (sha256 f7deb1c42322)
- issues: conflicting_sources:https://barron.uwec.edu/tuition-financial-aid/tuition-fees/,https://www.uwec.edu/tuition-aid/tuition-fees
- checks: {"columns": 2, "rows": 2}
  - on_campus:Tuition + Fees: 10207 ⟵ “Tuition + Fees | $10,207 | $10,207 | $11,160 | $20,273 | $14,371 | $15,674”
  - on_campus:Living Expenses (Food/Housing): 9726 ⟵ “Living Expenses (Food/Housing) | $2,918 | $9,726 | $9,726 | $9,726 | $9,726 | $9,726”
  - on_campus:Tuition + Fees: 11160 ⟵ “Tuition + Fees | $10,207 | $10,207 | $11,160 | $20,273 | $14,371 | $15,674”
  - on_campus:Living Expenses (Food/Housing): 9726 ⟵ “Living Expenses (Food/Housing) | $2,918 | $9,726 | $9,726 | $9,726 | $9,726 | $9,726”
### `6c5699c8dab99004` University of Wisconsin-Eau Claire — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://barron.uwec.edu/tuition-financial-aid/tuition-fees/ (sha256 f4516cf9566f)
- issues: cost_period_semester, residency_unknown, conflicting_sources:https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance,https://www.uwec.edu/tuition-aid/tuition-fees
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 4137.0 ⟵ “Tuition | $2,758.00 | $2,932.44 | $6,845.40 | $4,137.00”
  - column:Segregated Fees: 250.0 ⟵ “Segregated Fees | $250.00 | $250.00 | $250.00 | $250.00”
  - column:Textbook Rental: 70.0 ⟵ “Textbook Rental | $70.00 | $70.00 | $70.00 | $70.00”
  - column:Total Tuition + Fees: 4457.0 ⟵ “Total Tuition + Fees | $3,078.00 | $3,252.44 | $7,165.40 | $4,457.00”
### `a2636813aebfd9b4` University of Wisconsin-Eau Claire — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://barron.uwec.edu/tuition-financial-aid/tuition-fees/ (sha256 f4516cf9566f)
- issues: cost_period_semester, conflicting_sources:https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance,https://www.uwec.edu/tuition-aid/tuition-fees
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition: 6845.4 ⟵ “Tuition | $2,758.00 | $2,932.44 | $6,845.40 | $4,137.00”
  - on_campus:Segregated Fees: 250.0 ⟵ “Segregated Fees | $250.00 | $250.00 | $250.00 | $250.00”
  - on_campus:Textbook Rental: 70.0 ⟵ “Textbook Rental | $70.00 | $70.00 | $70.00 | $70.00”
  - on_campus:Total Tuition + Fees: 7165.4 ⟵ “Total Tuition + Fees | $3,078.00 | $3,252.44 | $7,165.40 | $4,457.00”
### `bfba320c9a1e6cac` University of Wisconsin-Eau Claire — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance (sha256 f7deb1c42322)
- issues: conflicting_sources:https://barron.uwec.edu/tuition-financial-aid/tuition-fees/,https://www.uwec.edu/tuition-aid/tuition-fees
- checks: {"columns": 1, "rows": 2}
  - on_campus:Tuition + Fees: 20273 ⟵ “Tuition + Fees | $10,207 | $10,207 | $11,160 | $20,273 | $14,371 | $15,674”
  - on_campus:Living Expenses (Food/Housing): 9726 ⟵ “Living Expenses (Food/Housing) | $2,918 | $9,726 | $9,726 | $9,726 | $9,726 | $9,726”
### `c54e9f78a9d28e19` University of Wisconsin-Eau Claire — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://barron.uwec.edu/tuition-financial-aid/tuition-fees/ (sha256 f4516cf9566f)
- issues: cost_period_semester, conflicting_sources:https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance,https://www.uwec.edu/tuition-aid/tuition-fees
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition: 2758.0 ⟵ “Tuition | $2,758.00 | $2,932.44 | $6,845.40 | $4,137.00”
  - on_campus:Segregated Fees: 250.0 ⟵ “Segregated Fees | $250.00 | $250.00 | $250.00 | $250.00”
  - on_campus:Textbook Rental: 70.0 ⟵ “Textbook Rental | $70.00 | $70.00 | $70.00 | $70.00”
  - on_campus:Total Tuition + Fees: 3078.0 ⟵ “Total Tuition + Fees | $3,078.00 | $3,252.44 | $7,165.40 | $4,457.00”
  - on_campus:Tuition: 2932.44 ⟵ “Tuition | $2,758.00 | $2,932.44 | $6,845.40 | $4,137.00”
  - on_campus:Segregated Fees: 250.0 ⟵ “Segregated Fees | $250.00 | $250.00 | $250.00 | $250.00”
  - on_campus:Textbook Rental: 70.0 ⟵ “Textbook Rental | $70.00 | $70.00 | $70.00 | $70.00”
  - on_campus:Total Tuition + Fees: 3252.44 ⟵ “Total Tuition + Fees | $3,078.00 | $3,252.44 | $7,165.40 | $4,457.00”
### `e5a20a9bdfee597d` University of Wisconsin-Eau Claire — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.uwec.edu/tuition-aid/tuition-fees (sha256 38abd1fc1598)
- issues: conflicting_sources:https://barron.uwec.edu/tuition-financial-aid/tuition-fees/,https://www.uwec.edu/offices-services/blugold-central/financial-aid-office/estimated-cost-attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition/fees*: 10407 ⟵ “Tuition/fees* | $10,407 | $11,772 | $15,983 | $20,674 | $14,654”
  - on_campus:Room**: 5405 ⟵ “Room** | $5,405 | $5,405 | $5,405 | $5,405 | $5,405”
  - on_campus:Meals***: 3910 ⟵ “Meals*** | $3,910 | $3,910 | $3,910 | $3,910 | $3,910”
  - on_campus:TOTAL: 19722 ⟵ “TOTAL | $19,722 | $21,087 | $25,298 | $29,989 | $23,969”
### `29354dac75c33110` University of Wisconsin-Green Bay — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.uwgb.edu/financial-aid/forms/appeal-forms/ (sha256 cde88622abb9)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Upload Documents Reinstatement of Aid Appeal & Probation When you are ineligible for financial aid due to not meeting Satisfactory Academic Progress (SAP) standards, you can submit an appeal for consideration of exceptional and documented circumstances.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will not consider late appeals without proof of extenuating circumstances that prevented a timely submission.”
### `41d82f1ea89630ee` University of Wisconsin-Green Bay — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.uwgb.edu/financial-aid/forms/appeal-forms/ (sha256 cde88622abb9)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Ineligible for Dependency Override Dependency overrides due to the following cannot occur: Parents refusing to contribute financially to your education Unwillingness of your parents to provide information Being financially independent Parents not claiming you as a dependent for income tax purposes Please visit Phoenix Cares for resources (e.g. housing, meals, childcare, etc.) that may be available”
### `56330f62f252115d` University of Wisconsin-Green Bay — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.uwgb.edu/financial-aid/forms/appeal-forms/ (sha256 cde88622abb9)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: need_based_special_circumstances ⟵ “There are three main types of appeals: Reinstatement of Aid Appeal Special Circumstances Appeals Unusual Circumstances-Dependency Override Please be aware that UW-Green Bay employees are required to report incidents of child abuse and neglect.”
  - sentence: need_based_special_circumstances ⟵ “Reinstatement of Aid Appeal Form Special Circumstances The Financial Aid Office can take into consideration changes to a student's or family's financial situation (e.g. loss of job, etc.) by submitting one of the following appeals.”
  - sentence: need_based_special_circumstances ⟵ “The review process for Special Circumstances Appeals will begin mid-summer.”
  - sentence: need_based_special_circumstances ⟵ “Payment of private primary or secondary school tuition Costs for weddings Changes in asset values after the FAFSA was filed Consumer debt including credit card debt, vehicle loans, legal fees, etc. 26-27 Additional Expense Appeal Form (.docx) Unusual Circumstances-Dependency Override The Department of Education determines if a student is dependent or independent based on how the student answers sp”
  - sentence: need_based_special_circumstances ⟵ “If there are unusual circumstances where you cannot provide parent information on the FAFSA due to: abuse, neglect, or abandonment or estrangement, please review the information below or contact Financial Aid regarding your situation as we may be able to perform a dependency override to consider you an independent student for financial aid purposes.”
  - sentence: need_based_special_circumstances ⟵ “Requesting a Dependency Override Due to Unusual Circumstances In order to consider your unusual circumstance, please submit the following information to Financial Aid for review.”
### `09acfc0e01fcedd3` University of Wisconsin-Green Bay — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwgb.edu/apply/cost/ (sha256 ac82e740b7e7)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 5}
  - column:Wisconsin Resident: 9133 ⟵ “Wisconsin Resident | $9,133”
  - column:Minnesota Resident**: 10855 ⟵ “Minnesota Resident** | $10,855”
  - column:Midwest Tuition Rate***: 12912 ⟵ “Midwest Tuition Rate*** | $12,912”
  - column:Michigan Compact/Upper Michigan Resident^: 9133 ⟵ “Michigan Compact/Upper Michigan Resident^ | $9,133”
  - column:Out-of-state/Non-Resident: 17721 ⟵ “Out-of-state/Non-Resident | $17,721”
### `1b45fccf01c455bd` University of Wisconsin-La Crosse — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwlax.edu/admissions/tuition-and-aid/scholarships/ (sha256 822661027831)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances While most scholarships are merit-based, some funds are available to recognize special circumstances, experiences, and achievements in addition to academic performance.”
  - sentence: need_based_special_circumstances ⟵ “Completion of the Special Circumstances Form is optional and does not guarantee an award.”
### `4d4de20ceac4303d` University of Wisconsin-La Crosse — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwlax.edu/finaid/actions/understand-satisfactory-academic-progress-sap/ (sha256 07db381c05bc)
- issues: semantic_review_required, conflicting_sources:https://catalog.uwlax.edu/undergraduate/academicpolicies/academicforgiveness/,https://catalog.uwlax.edu/undergraduate/expensesfinancialaid/,https://www.uwlax.edu/finaid/resources/policies/satisfactory-academic-progress-policy/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Students can complete the appeal online, and the SAP appeal committee will review it within 30 days.”
  - sentence: sap_appeal ⟵ “Appeal Process Students with extenuating circumstances that prevented them from making SAP have the right to appeal their situation.”
  - sentence: sap_appeal ⟵ “Exceptions can be made at the discretion of the SAP appeal committee to consider appeals completed after the deadline.”
### `5d3290b2f5f0db86` University of Wisconsin-La Crosse — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwlax.edu/finaid/resources/policies/satisfactory-academic-progress-policy/ (sha256 c9fe239eca66)
- issues: semantic_review_required, conflicting_sources:https://catalog.uwlax.edu/undergraduate/academicpolicies/academicforgiveness/,https://catalog.uwlax.edu/undergraduate/expensesfinancialaid/,https://www.uwlax.edu/finaid/actions/understand-satisfactory-academic-progress-sap/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Students can complete the appeal online, and the SAP appeal committee will review it within 30 days.”
  - sentence: sap_appeal ⟵ “Appeal Process Students with extenuating circumstances that prevented them from making SAP have the right to appeal their situation.”
  - sentence: sap_appeal ⟵ “Exceptions can be made at the discretion of the SAP appeal committee to consider appeals completed after the deadline.”
### `7bc1f8ea97ba095c` University of Wisconsin-La Crosse — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.uwlax.edu/undergraduate/expensesfinancialaid/ (sha256 bd7968daec3c)
- issues: semantic_review_required, conflicting_sources:https://catalog.uwlax.edu/undergraduate/academicpolicies/academicforgiveness/,https://www.uwlax.edu/finaid/actions/understand-satisfactory-academic-progress-sap/,https://www.uwlax.edu/finaid/resources/policies/satisfactory-academic-progress-policy/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Expenses Tuition and fees Student billing (electronic) & guest access How to pay Installment billing & late fee Segregated fees Textbooks Health service Residence halls UWL dining services Financial aid & scholarships Eligibility requirements Application procedures Notification dates Financial aid programs Satisfactory academic progress policy Evaluation process Appeal process Additional informati”
### `ebd18f6409a9f2fa` University of Wisconsin-La Crosse — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.uwlax.edu/undergraduate/academicpolicies/academicforgiveness/ (sha256 882c08b438ba)
- issues: semantic_review_required, conflicting_sources:https://catalog.uwlax.edu/undergraduate/expensesfinancialaid/,https://www.uwlax.edu/finaid/actions/understand-satisfactory-academic-progress-sap/,https://www.uwlax.edu/finaid/resources/policies/satisfactory-academic-progress-policy/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Contact the Financial Aid Office prior to submitting an Application for Academic Forgiveness to better understand any impact on financial aid and the SAP appeals process. 608.785.8000 1725 State St., La Crosse WI, 54601 catalog@uwlax.edu Copyright © 2026-2027 Back to top Close this window Print Options Send Page to Printer Print this page.”
### `1222b9e7ca47e0e0` University of Wisconsin-La Crosse — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.uwlax.edu/finaid/actions/accept-decline-my-finaid-award/ (sha256 f264ca5b3c1a)
- issues: conflicting_sources:https://www.uwlax.edu/cost/
- checks: {"columns": 1, "components_reconcile": true, "rows": 12}
  - on_campus:Estimated Tuition: 19042 ⟵ “Estimated Tuition | $8,926 | $9,860 | $19,042”
  - on_campus:Segregated fees & book rental: 1912 ⟵ “Segregated fees & book rental | $1,912 | $1,912 | $1,912”
  - on_campus:Registration fee: 50 ⟵ “Registration fee | $50 | $50 | $50”
  - on_campus:Canvas fee average: 60 ⟵ “Canvas fee average | $60 | $60 | $60”
  - on_campus:Career Services fee: 14 ⟵ “Career Services fee | $14 | $14 | $14”
  - on_campus:Books/Supplies: 122 ⟵ “Books/Supplies | $122 | $122 | $122”
  - on_campus:Housing: 5316 ⟵ “Housing | $5,316 | $5,316 | $5,316”
  - on_campus:Food: 4038 ⟵ “Food | $4,038 | $4,038 | $4,038”
  - on_campus:Transportation: 1152 ⟵ “Transportation | $1,152 | $1,152 | $1,152”
  - on_campus:Miscellaneous personal: 1122 ⟵ “Miscellaneous personal | $1,122 | $1,122 | $1,122”
  - on_campus:Loan Fees: 68 ⟵ “Loan Fees | $68 | $68 | $68”
  - on_campus:TOTAL: 32896 ⟵ “TOTAL | $22,780 | $23,714 | $32,896”
### `27feb6a00c8c5eaf` University of Wisconsin-La Crosse — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.uwlax.edu/cost/ (sha256 983b6ea18d4b)
- issues: conflicting_sources:https://www.uwlax.edu/finaid/actions/accept-decline-my-finaid-award/
- checks: {"columns": 1, "rows": 4}
  - on_campus:Tuition/Fees: 21077 ⟵ “Tuition/Fees | $10,961 | $11,895 | $21,077 | $15,421 | $16,317 | $10,961/ $11,895”
  - on_campus:Housing traditional double: 4834 ⟵ “Housing traditional double | $4,834 | $4,834 | $4,834 | $4,834 | $4,834 | 0”
  - on_campus:FoodStryker Classic meal plan: 3336 ⟵ “FoodStryker Classic meal plan | $3,336 | $3,336 | $3,336 | $3,336 | $3,336 | 0”
  - on_campus:TOTALSdivide in half for per semester costs: 29247 ⟵ “TOTALSdivide in half for per semester costs | $19,131 | $20,065 | $29,247 | $23,591 | $24,487 | $10,961/$11,895”
### `4b3a758b64e0a12c` University of Wisconsin-La Crosse — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.uwlax.edu/cost/ (sha256 983b6ea18d4b)
- issues: arrangement_unlabeled, conflicting_sources:https://www.uwlax.edu/finaid/actions/accept-decline-my-finaid-award/
- checks: {"columns": 2, "rows": 4}
  - on_campus:Tuition/Fees: 10961 ⟵ “Tuition/Fees | $10,961 | $11,895 | $21,077 | $15,421 | $16,317 | $10,961/ $11,895”
  - on_campus:Housing traditional double: 4834 ⟵ “Housing traditional double | $4,834 | $4,834 | $4,834 | $4,834 | $4,834 | 0”
  - on_campus:FoodStryker Classic meal plan: 3336 ⟵ “FoodStryker Classic meal plan | $3,336 | $3,336 | $3,336 | $3,336 | $3,336 | 0”
  - on_campus:TOTALSdivide in half for per semester costs: 19131 ⟵ “TOTALSdivide in half for per semester costs | $19,131 | $20,065 | $29,247 | $23,591 | $24,487 | $10,961/$11,895”
  - column:Tuition/Fees: 11895 ⟵ “Tuition/Fees | $10,961 | $11,895 | $21,077 | $15,421 | $16,317 | $10,961/ $11,895”
  - column:Housing traditional double: 4834 ⟵ “Housing traditional double | $4,834 | $4,834 | $4,834 | $4,834 | $4,834 | 0”
  - column:FoodStryker Classic meal plan: 3336 ⟵ “FoodStryker Classic meal plan | $3,336 | $3,336 | $3,336 | $3,336 | $3,336 | 0”
  - column:TOTALSdivide in half for per semester costs: 20065 ⟵ “TOTALSdivide in half for per semester costs | $19,131 | $20,065 | $29,247 | $23,591 | $24,487 | $10,961/$11,895”
### `7dcfdcc369025990` University of Wisconsin-La Crosse — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwlax.edu/cost/ (sha256 983b6ea18d4b)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.uwlax.edu/finaid/actions/accept-decline-my-finaid-award/
- checks: {"columns": 3, "rows": 4}
  - column:Tuition/Fees: 15421 ⟵ “Tuition/Fees | $10,961 | $11,895 | $21,077 | $15,421 | $16,317 | $10,961/ $11,895”
  - column:Housing traditional double: 4834 ⟵ “Housing traditional double | $4,834 | $4,834 | $4,834 | $4,834 | $4,834 | 0”
  - column:FoodStryker Classic meal plan: 3336 ⟵ “FoodStryker Classic meal plan | $3,336 | $3,336 | $3,336 | $3,336 | $3,336 | 0”
  - column:TOTALSdivide in half for per semester costs: 23591 ⟵ “TOTALSdivide in half for per semester costs | $19,131 | $20,065 | $29,247 | $23,591 | $24,487 | $10,961/$11,895”
  - column:Tuition/Fees: 16317 ⟵ “Tuition/Fees | $10,961 | $11,895 | $21,077 | $15,421 | $16,317 | $10,961/ $11,895”
  - column:Housing traditional double: 4834 ⟵ “Housing traditional double | $4,834 | $4,834 | $4,834 | $4,834 | $4,834 | 0”
  - column:FoodStryker Classic meal plan: 3336 ⟵ “FoodStryker Classic meal plan | $3,336 | $3,336 | $3,336 | $3,336 | $3,336 | 0”
  - column:TOTALSdivide in half for per semester costs: 24487 ⟵ “TOTALSdivide in half for per semester costs | $19,131 | $20,065 | $29,247 | $23,591 | $24,487 | $10,961/$11,895”
  - with_parents_or_family:Housing traditional double: 0 ⟵ “Housing traditional double | $4,834 | $4,834 | $4,834 | $4,834 | $4,834 | 0”
  - with_parents_or_family:FoodStryker Classic meal plan: 0 ⟵ “FoodStryker Classic meal plan | $3,336 | $3,336 | $3,336 | $3,336 | $3,336 | 0”
### `8df2e873004186e3` University of Wisconsin-La Crosse — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.uwlax.edu/finaid/actions/accept-decline-my-finaid-award/ (sha256 f264ca5b3c1a)
- issues: conflicting_sources:https://www.uwlax.edu/cost/
- checks: {"columns": 1, "components_reconcile": true, "rows": 12}
  - column:Estimated Tuition: 8926 ⟵ “Estimated Tuition | $8,926 | $9,860 | $19,042”
  - column:Segregated fees & book rental: 1912 ⟵ “Segregated fees & book rental | $1,912 | $1,912 | $1,912”
  - column:Registration fee: 50 ⟵ “Registration fee | $50 | $50 | $50”
  - column:Canvas fee average: 60 ⟵ “Canvas fee average | $60 | $60 | $60”
  - column:Career Services fee: 14 ⟵ “Career Services fee | $14 | $14 | $14”
  - column:Books/Supplies: 122 ⟵ “Books/Supplies | $122 | $122 | $122”
  - column:Housing: 5316 ⟵ “Housing | $5,316 | $5,316 | $5,316”
  - column:Food: 4038 ⟵ “Food | $4,038 | $4,038 | $4,038”
  - column:Transportation: 1152 ⟵ “Transportation | $1,152 | $1,152 | $1,152”
  - column:Miscellaneous personal: 1122 ⟵ “Miscellaneous personal | $1,122 | $1,122 | $1,122”
  - column:Loan Fees: 68 ⟵ “Loan Fees | $68 | $68 | $68”
  - column:TOTAL: 22780 ⟵ “TOTAL | $22,780 | $23,714 | $32,896”
### `b78e84b10c6eba13` University of Wisconsin-La Crosse — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwlax.edu/finaid/actions/accept-decline-my-finaid-award/ (sha256 f264ca5b3c1a)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.uwlax.edu/cost/
- checks: {"columns": 1, "components_reconcile": true, "rows": 12}
  - column:Estimated Tuition: 9860 ⟵ “Estimated Tuition | $8,926 | $9,860 | $19,042”
  - column:Segregated fees & book rental: 1912 ⟵ “Segregated fees & book rental | $1,912 | $1,912 | $1,912”
  - column:Registration fee: 50 ⟵ “Registration fee | $50 | $50 | $50”
  - column:Canvas fee average: 60 ⟵ “Canvas fee average | $60 | $60 | $60”
  - column:Career Services fee: 14 ⟵ “Career Services fee | $14 | $14 | $14”
  - column:Books/Supplies: 122 ⟵ “Books/Supplies | $122 | $122 | $122”
  - column:Housing: 5316 ⟵ “Housing | $5,316 | $5,316 | $5,316”
  - column:Food: 4038 ⟵ “Food | $4,038 | $4,038 | $4,038”
  - column:Transportation: 1152 ⟵ “Transportation | $1,152 | $1,152 | $1,152”
  - column:Miscellaneous personal: 1122 ⟵ “Miscellaneous personal | $1,122 | $1,122 | $1,122”
  - column:Loan Fees: 68 ⟵ “Loan Fees | $68 | $68 | $68”
  - column:TOTAL: 23714 ⟵ “TOTAL | $22,780 | $23,714 | $32,896”
### `d9894927ded0d730` University of Wisconsin-La Crosse — costs 2027-28 · residency=in_state [new] (labeled_in_source)
- source: https://www.uwlax.edu/cost/ (sha256 983b6ea18d4b)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "rows": 3}
  - on_campus:Tuition/Fees: 10993 ⟵ “Tuition/Fees | $10,993 | $11,927 | $21,109 | $15,453 | $16,349 | $10,993/11,927”
  - on_campus:Housingtraditional double: 4980 ⟵ “Housingtraditional double | $4,980 | $4,980 | $4,980 | $4,980 | $4,980 | 0”
  - on_campus:TOTALSdivide in half for per semester costs: 19443 ⟵ “TOTALSdivide in half for per semester costs | $19,443 | $20,377 | $29,559 | $23,903 | $24,799 | $10,993/11,927”
  - column:Tuition/Fees: 11927 ⟵ “Tuition/Fees | $10,993 | $11,927 | $21,109 | $15,453 | $16,349 | $10,993/11,927”
  - column:Housingtraditional double: 4980 ⟵ “Housingtraditional double | $4,980 | $4,980 | $4,980 | $4,980 | $4,980 | 0”
  - column:TOTALSdivide in half for per semester costs: 20377 ⟵ “TOTALSdivide in half for per semester costs | $19,443 | $20,377 | $29,559 | $23,903 | $24,799 | $10,993/11,927”
### `ef24e8076db632e1` University of Wisconsin-La Crosse — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwlax.edu/cost/ (sha256 983b6ea18d4b)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "rows": 3}
  - column:Tuition/Fees: 15453 ⟵ “Tuition/Fees | $10,993 | $11,927 | $21,109 | $15,453 | $16,349 | $10,993/11,927”
  - column:Housingtraditional double: 4980 ⟵ “Housingtraditional double | $4,980 | $4,980 | $4,980 | $4,980 | $4,980 | 0”
  - column:TOTALSdivide in half for per semester costs: 23903 ⟵ “TOTALSdivide in half for per semester costs | $19,443 | $20,377 | $29,559 | $23,903 | $24,799 | $10,993/11,927”
  - column:Tuition/Fees: 16349 ⟵ “Tuition/Fees | $10,993 | $11,927 | $21,109 | $15,453 | $16,349 | $10,993/11,927”
  - column:Housingtraditional double: 4980 ⟵ “Housingtraditional double | $4,980 | $4,980 | $4,980 | $4,980 | $4,980 | 0”
  - column:TOTALSdivide in half for per semester costs: 24799 ⟵ “TOTALSdivide in half for per semester costs | $19,443 | $20,377 | $29,559 | $23,903 | $24,799 | $10,993/11,927”
  - with_parents_or_family:Housingtraditional double: 0 ⟵ “Housingtraditional double | $4,980 | $4,980 | $4,980 | $4,980 | $4,980 | 0”
### `1bb4584cca554089` University of Wisconsin-La Crosse — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.uwlax.edu/admissions/credit-for-prior-learning/ (sha256 49c2784514fc)
- issues: credits_implausible, score_scale_mismatch
- checks: {"distinct_exams": 22, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL 4, 5, 6, 7]:  ⟵ “Biology (HL) | 4, 5, 6, 7 | Biology 105 | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4, 5, 6, 7]:  ⟵ “Business & Management (HL) | 4, 5, 6, 7 | Management Elective | 3”
  - equivalencies[IB-CHEMISTRY-HL|HL 4]:  ⟵ “Chemistry (HL) | 4 | Chemistry 100 | 4”
  - equivalencies[IB-CHEMISTRY-HL|HL 5]:  ⟵ “Chemistry (HL) | 5 | Chemistry 103 | 5”
  - equivalencies[IB-CHEMISTRY-HL|HL 6, 7]:  ⟵ “Chemistry (HL) | 6, 7 | Chemistry 103, 104 | 10”
  - equivalencies[IB-LATIN-HL|HL 4, 5, 6, 7]:  ⟵ “Classical Languages (Greek & Latin) (HL) | 4, 5, 6, 7 | Global Languages Elective | 3”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 4, 5, 6, 7]:  ⟵ “Computer Science (HL) | 4, 5, 6, 7 | Computer Science 120 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|SL 5, 6, 7]:  ⟵ “Computer Science (SL) | 5, 6, 7 | Computer Science 224 | 3”
  - equivalencies[IB-ECONOMICS-HL|HL 4, 5, 6, 7]:  ⟵ “Economics (HL) | 4, 5, 6, 7 | Economics 110, 120 | 6”
  - equivalencies[IB-GEOGRAPHY-HL|HL 4, 5, 6, 7]:  ⟵ “Geography (HL) | 4, 5, 6, 7 | Geography Elective | 3”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | Political Science 202 | 3”
  - equivalencies[IB-HISTORY-HL|HL 4, 5, 6, 7]:  ⟵ “History (HL) | 4, 5, 6, 7 | History Elective: Respective 200 Level Survey Courses | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|SL 56,7]:  ⟵ “Mathematics: Analysis and Approaches (SL) | 56,7 | Math 150Math 151 | 44”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|HL 45, 6, 7]:  ⟵ “Mathematics: Analysis and Approaches (HL) | 45, 6, 7 | Math 151Math 207 | 44”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-SL|SL 5, 6, 7]:  ⟵ “Mathematics: Applications and Interpretation (SL) | 5, 6, 7 | Math 160 | 4”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|HL 456, 7]:  ⟵ “Mathematics: Applications and Interpretation (HL) | 456, 7 | Math 150Math 175Math 207 | 444”
  - equivalencies[IB-MUSIC-HL|HL 4, 5, 6, 7]:  ⟵ “Music (HL) | 4, 5, 6, 7 | Music Elective | 3”
  - equivalencies[IB-PHILOSOPHY-HL|HL 4, 5, 6, 7]:  ⟵ “Philosophy (HL) | 4, 5, 6, 7 | Philosophy 100 | 3”
  - equivalencies[IB-PHYSICS-HL|HL 4, 5, 6, 7]:  ⟵ “Physics (HL) | 4, 5, 6, 7 | Physics 103 | 4”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 4, 5, 6, 7]:  ⟵ “Psychology (HL) | 4, 5, 6, 7 | Psychology 100 | 3”
  - equivalencies[IB-PSYCHOLOGY-SL|SL 5, 6, 7]:  ⟵ “Psychology (SL) | 5, 6, 7 | Psychology 100 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-HL|HL 4, 5, 6, 7]:  ⟵ “Social & Cultural Anthropology (HL) | 4, 5, 6, 7 | Anthropology 101 | 3”
  - equivalencies[IB-THEATRE-HL|HL 4, 5, 6, 7]:  ⟵ “Theatre Arts (HL) | 4, 5, 6, 7 | Theatre Elective | 3”
  - equivalencies[IB-VISUAL-ARTS-HL|HL 4, 5, 6, 7]:  ⟵ “Visual Arts (HL) | 4, 5, 6, 7 | Elective Credit | 3”
### `97fcf9f1f6bd55c3` University of Wisconsin-La Crosse — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.uwlax.edu/admissions/credit-for-prior-learning/ (sha256 49c2784514fc)
- issues: credits_implausible, score_column_not_scores, score_scale_mismatch
- checks: {"distinct_exams": 24, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|Composition & Literature: American Literature]:  ⟵ “Composition & Literature: American Literature | 50 | English Elective | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|Composition & Literature: Analyzing & Interpreting Literature]:  ⟵ “Composition & Literature: Analyzing & Interpreting Literature | 50 | English Elective | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|Composition & Literature: English Literature]:  ⟵ “Composition & Literature: English Literature | 50 | English Elective | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|Composition & Literature: College Composition]:  ⟵ “Composition & Literature: College Composition | 50 | English 100 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|Foreign Literature: College French Level 1 (2 semesters)]:  ⟵ “Foreign Literature: College French Level 1 (2 semesters) | 50 | French 101, 102 | 6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|Foreign Literature: College French Level 2 (4 semesters)]:  ⟵ “Foreign Literature: College French Level 2 (4 semesters) | 62 | French 101, 102, 201, 202 | 12”
  - equivalencies[CLEP-GERMAN-LANGUAGE|Foreign Literature: College German Level 1 (2 semesters)]:  ⟵ “Foreign Literature: College German Level 1 (2 semesters) | 50 | German 101, 102 | 8”
  - equivalencies[CLEP-GERMAN-LANGUAGE|Foreign Literature: College German Level 2 (4 semesters)]:  ⟵ “Foreign Literature: College German Level 2 (4 semesters) | 63 | German 101, 102, 201, 202 | 16”
  - equivalencies[CLEP-SPANISH-LANGUAGE|College Spanish: Level 1 (2 semesters)]:  ⟵ “College Spanish: Level 1 (2 semesters) | 50 | Spanish 101, 102 | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|College Spanish: Level 2 (4 semesters)]:  ⟵ “College Spanish: Level 2 (4 semesters) | 66 | Spanish 101, 102, 201, 202 | 16”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|History & Social Sciences: American Government]:  ⟵ “History & Social Sciences: American Government | 50 | Pol. Science 101 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|History & Social Sciences: History of the US I]:  ⟵ “History & Social Sciences: History of the US I | 50 | History 210 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|History & Social Sciences: History of the US II]:  ⟵ “History & Social Sciences: History of the US II | 50 | History 210 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|History & Social Sciences: Human Growth & Development]:  ⟵ “History & Social Sciences: Human Growth & Development | 50 | Psychology 212 | 3”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|History & Social Sciences: Intro to Educational Psychology]:  ⟵ “History & Social Sciences: Intro to Educational Psychology | 50 | Psychology 370 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|History & Social Sciences: Introductory Psychology]:  ⟵ “History & Social Sciences: Introductory Psychology | 50 | Psychology 100 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|History & Social Sciences: Introductory Sociology]:  ⟵ “History & Social Sciences: Introductory Sociology | 50 | Sociology 110 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|History & Social Sciences: Principles of Macroeconomics]:  ⟵ “History & Social Sciences: Principles of Macroeconomics | 50 | Economics 120 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|History & Social Sciences: Principles of Microeconomics]:  ⟵ “History & Social Sciences: Principles of Microeconomics | 50 | Economics 110 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|History & Social Sciences: Western Civilization I]:  ⟵ “History & Social Sciences: Western Civilization I | 50 | No corresponding UWL course | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|History & Social Sciences: Western Civilization II]:  ⟵ “History & Social Sciences: Western Civilization II | 50 | No corresponding UWL course | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|Science & Mathematics: College Algebra]:  ⟵ “Science & Mathematics: College Algebra | 63 | Math 150 | 4”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|Science & Mathematics: College Mathematics]:  ⟵ “Science & Mathematics: College Mathematics | 63 | Math 123 | 4”
  - equivalencies[CLEP-PRECALCULUS|Science & Mathematics: Precalculus]:  ⟵ “Science & Mathematics: Precalculus | 61 | Math 151 | 4”
  - equivalencies[CLEP-BIOLOGY|Science & Mathematics: Biology]:  ⟵ “Science & Mathematics: Biology | 50 | Biology 105 | 4”
  - … 5 more rows
### `2a2f7a3b30909eb4` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=engineering-bs [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 1eec26aa5299)
- issues: requirement_groups_skipped
- checks: {"courses": 6, "groups": 4, "groups_skipped": 1}
  - program_name: Engineering, BS ⟵ “Engineering, BS | UW-Milwaukee Academic Catalog”
### `349b58fc4a395093` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=theatre-practices-ba [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-ba/ (sha256 83663383ab2d)
- issues: requirement_groups_skipped
- checks: {"courses": 0, "groups": 1, "groups_skipped": 3}
  - program_name: Theatre Practices, BA ⟵ “Theatre Practices, BA | UW-Milwaukee Academic Catalog”
### `3b0307454614178a` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=music-bfa-versatile-voice [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 25dc4754de12)
- issues: requirement_groups_skipped
- checks: {"courses": 41, "groups": 7, "groups_skipped": 4}
  - program_name: Music, BFA: Versatile Voice ⟵ “Music, BFA: Versatile Voice | UW-Milwaukee Academic Catalog”
### `5e6685af33e234ff` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=actuarial-science-ba [new] (labeled_in_source)
- source: https://catalog.uwm.edu/letters-science/mathematical-sciences/actuarial-science-ba/ (sha256 fa53bbc66e53)
- issues: requirement_groups_skipped
- checks: {"courses": 5, "groups": 2, "groups_skipped": 4}
  - program_name: Actuarial Science, BA ⟵ “Actuarial Science, BA | UW-Milwaukee Academic Catalog”
### `dd8956f2ffa29ea9` University of Wisconsin-Milwaukee — academic_programs 2026-27 · program_key=theatre-practices-ba-theatre-education [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-education-ba/ (sha256 5aeef82aba07)
- issues: requirement_groups_skipped
- checks: {"courses": 0, "groups": 2, "groups_skipped": 1}
  - program_name: Theatre Practices, BA: Theatre Education ⟵ “Theatre Practices, BA: Theatre Education | UW-Milwaukee Academic Catalog”
### `ccaa31af7213dee1` University of Wisconsin-Milwaukee — appeals 2026-27 [new] (labeled_in_source)
- source: https://uwm.edu/finances/finances/receiving-financial-aid/satisfactory-academic-progress-sap/ (sha256 83eb5314e1c5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Review: If you believe your FAFSA does not adequately reflect your current financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances If you or your family have faced financial challenges that weren’t captured on your FAFSA form, you can schedule an appointment to talk with a Student Financial Service Center advisor.”
### `dd724ba91077f62a` University of Wisconsin-Milwaukee — appeals 2026-27 [new] (labeled_in_source)
- source: https://uwm.edu/finances/finances/receiving-financial-aid/satisfactory-academic-progress-sap/ (sha256 83eb5314e1c5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal: If you’ve been notified you no longer meet financial aid’s Satisfactory Academic Progress requirements.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form is provided to the student after meeting with an Advisor in the Student Financial Service Center.”
  - sentence: sap_appeal ⟵ “While Advisors may request assistance from the Financial Aid SAP Appeals Committee for any appeal, students who submit more than two appeals must have their appeal reviewed by a committee.”
  - sentence: sap_appeal ⟵ “Whether or not an academic plan is needed will be determined when the student meets with an Advisor in the Student Financial Service Center to discuss whether they are eligible to complete a SAP appeal.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form is provided to the student after meeting with an Advisor in the Student Financial Service Center.”
  - sentence: sap_appeal ⟵ “While Advisors may request assistance from the Financial Aid SAP Appeals Committee for any appeal, students who submit more than two appeals must have their appeal reviewed by the committee.”
### `e0c3e4f030908599` University of Wisconsin-Milwaukee — appeals 2026-27 [new] (labeled_in_source)
- source: https://uwm.edu/finances/finances/receiving-financial-aid/satisfactory-academic-progress-sap/ (sha256 83eb5314e1c5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: budget_increase ⟵ “Budget Adjustment Request: If you believe your Cost of Attendance does not adequately reflect your educational expenses.”
  - sentence: budget_increase ⟵ “Budget Adjustment You may qualify for an adjustment to your Cost of Attendance (COA).”
  - sentence: budget_increase ⟵ “This is called a Budget Adjustment and is available for the documented rental or purchase of a personal computer, the costs expected to be incurred for dependent care, and when documented expenses are significantly different than those used in our estimates.”
  - sentence: budget_increase ⟵ “A Budget Adjustment may or may not increase the amount of financial aid offered.”
  - sentence: budget_increase ⟵ “If Joe needs extra financial aid, Joe could borrow a maximum of $13,588 in a private loan without having to complete a request for a budget increase.”
  - sentence: budget_increase ⟵ “If you need to borrow additional loan funds and you aren’t sure whether this form is needed, please make an appointment to discuss your circumstances for a budget adjustment.”
### `0490ffd35be19046` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=actuarial-science-ba · requirement_key=professional-development [new] (labeled_in_source)
- source: https://catalog.uwm.edu/letters-science/mathematical-sciences/actuarial-science-ba/ (sha256 fa53bbc66e53)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ECON 103 ⟵ “ECON 103 - Principles of Microeconomics (VEE-Economics)”
  - courses: ECON 104 ⟵ “ECON 104 - Principles of Macroeconomics (VEE-Economics)”
### `0aa3eea4a750275d` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-engineering-requirement-46-credits [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 1eec26aa5299)
- issues: requirement_groups_skipped
  - courses: EAS 200 ⟵ “EAS 200 - Professional Seminar”
### `0e7dc70e0296d176` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=actuarial-science-ba · requirement_key=requirements-additional-preparatory-coursework [new] (labeled_in_source)
- source: https://catalog.uwm.edu/letters-science/mathematical-sciences/actuarial-science-ba/ (sha256 fa53bbc66e53)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MATH 234 ⟵ “MATH 234 - Linear Algebra and Differential Equations”
  - courses: ECON 103 ⟵ “ECON 103 - Principles of Microeconomics”
  - courses: ECON 104 ⟵ “ECON 104 - Principles of Macroeconomics”
### `2fee1e60178344fe` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=music-bfa-requirements-music-theory [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 25dc4754de12)
- issues: requirement_groups_skipped
  - courses: MUSIC 123 ⟵ “MUSIC 123 - Aural Theory I”
  - courses: MUSIC 124 ⟵ “MUSIC 124 - Aural Theory II”
  - courses: MUSIC 127 ⟵ “MUSIC 127 - Materials of Theory I”
  - courses: MUSIC 128 ⟵ “MUSIC 128 - Materials of Theory II”
  - courses: MUSIC 225 ⟵ “MUSIC 225 - Materials of Theory III”
  - courses: MUSIC 226 ⟵ “MUSIC 226 - Aural Theory III”
  - courses: MUSIC 421 ⟵ “MUSIC 421 - Materials of Theory IV”
### `55c979028d927c71` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=theatre-practices-ba-theatre-education · requirement_key=major-requirements-school-of-education [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-education-ba/ (sha256 5aeef82aba07)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - section: major-requirements-school-of-education ⟵ “Major Requirements — School of Education”
### `7d8c3d56d2bc8537` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-engineering-technical-electives-30-credits [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 1eec26aa5299)
- issues: requirement_groups_skipped
  - section: engineering-major-requirements-engineering-technical-electives-30-credits ⟵ “Engineering Major Requirements — Engineering Technical Electives - 30 credits”
### `847b06348f1ca127` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements-music-theory-electives [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 25dc4754de12)
- issues: requirement_groups_skipped
  - courses: MUSIC 220 ⟵ “MUSIC 220 - Introduction to Computers and Music”
  - courses: MUSIC 321 ⟵ “MUSIC 321 - Counterpoint”
  - courses: MUSIC 323 ⟵ “MUSIC 323 - Instrumental and Choral Orchestration”
  - courses: MUSIC 327 ⟵ “MUSIC 327 - Studio Techniques”
  - courses: MUSIC 328 ⟵ “MUSIC 328 - Interactive Electronic Music”
  - courses: MUSIC 420 ⟵ “MUSIC 420 - Advanced Electronic Music and Sound Art:”
  - courses: MUSIC 680 ⟵ “MUSIC 680 - Special Studies in Music:”
### `8ba041df521d19e9` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-bio-sci-203 [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 1eec26aa5299)
- issues: requirement_groups_skipped
  - courses: CHEM 102 ⟵ “CHEM 102 - General Chemistry”
  - courses: CHEM 104 ⟵ “CHEM 104 - General Chemistry and Qualitative Analysis”
  - courses: CHEM 105 ⟵ “CHEM 105 - General Chemistry for Engineering”
### `99efebc03b7580bc` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements-music-history-electives [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 25dc4754de12)
- issues: requirement_groups_skipped
  - courses: MUSIC 310 ⟵ “MUSIC 310 - Introduction to World Musics”
  - courses: MUSIC 311 ⟵ “MUSIC 311 - Music of the Baroque Era”
  - courses: MUSIC 312 ⟵ “MUSIC 312 - Music of the Classic Era”
  - courses: MUSIC 313 ⟵ “MUSIC 313 - Music of the Romantic Era”
  - courses: MUSIC 314 ⟵ “MUSIC 314 - Music since 1900”
  - courses: MUSIC 317 ⟵ “MUSIC 317 - Introduction to American Music”
### `9af98fbd9df1b789` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=music-bfa-requirements-music-history [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 25dc4754de12)
- issues: requirement_groups_skipped
  - courses: MUSIC 106 ⟵ “MUSIC 106 - Foundations of Music”
  - courses: MUSIC 211 ⟵ “MUSIC 211 - General History of Western Music I”
  - courses: MUSIC 212 ⟵ “MUSIC 212 - General History of Western Music II”
### `a523c7071c5ee194` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=theatre-practices-ba · requirement_key=major-requirements-electives [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-ba/ (sha256 83663383ab2d)
- issues: requirement_groups_skipped
  - section: major-requirements-electives ⟵ “Major Requirements — Electives”
### `aeddf20250280743` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements-music-56 [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 25dc4754de12)
- issues: requirement_groups_skipped
  - courses: MUSIC 457 ⟵ “MUSIC 457 - Opera Theatre”
### `b68cfdda122e182b` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 25dc4754de12)
- issues: requirement_groups_skipped
  - courses: DANCE 111 ⟵ “DANCE 111 - Ballet I”
  - courses: DANCE 113 ⟵ “DANCE 113 - Modern Dance Technique I”
  - courses: DANCE 115 ⟵ “DANCE 115 - Jazz Dance I”
  - courses: DANCE 117 ⟵ “DANCE 117 - Tap I”
  - courses: DANCE 170 ⟵ “DANCE 170 - Hip-Hop Foundations I”
  - courses: DANCE 270 ⟵ “DANCE 270 - Hip-Hop II”
  - courses: DANCE 272 ⟵ “DANCE 272 - Salsa, Merengue, and Bachata I”
  - courses: DANCE 327 ⟵ “DANCE 327 - Dance for the Musical Theatre I”
  - courses: DANCE 321 ⟵ “DANCE 321 - Alexander Technique for the Performer”
  - courses: MUSIC 604 ⟵ “MUSIC 604 - Business for Performing Artists”
  - courses: MUSIC 245 ⟵ “MUSIC 245 - Basic and Italian Lyric Diction”
  - courses: MUSIC 246 ⟵ “MUSIC 246 - German and French Lyric Diction”
  - courses: MUSIC 444 ⟵ “MUSIC 444 - Vocal Pedagogy I”
  - courses: MUSIC 457 ⟵ “MUSIC 457 - Opera Theatre”
  - courses: MUSIC 520 ⟵ “MUSIC 520 - Voice Performance in Popular Music Styles”
### `b94fe4e9118c4de2` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=music-bfa-versatile-voice · requirement_key=major-requirements-recital [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/music/versatile-voice-bfa/ (sha256 25dc4754de12)
- issues: requirement_groups_skipped
  - courses: MUSIC 659 ⟵ “MUSIC 659 - Junior Recital”
  - courses: MUSIC 660 ⟵ “MUSIC 660 - Senior Recital:”
### `c144a077ad33a653` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=theatre-practices-ba-theatre-education · requirement_key=major-requirements-electives [new] (labeled_in_source)
- source: https://catalog.uwm.edu/arts-architecture/arts/theatre/theatre-education-ba/ (sha256 5aeef82aba07)
- issues: requirement_groups_skipped
  - section: major-requirements-electives ⟵ “Major Requirements — Electives”
### `f63346a44123348c` University of Wisconsin-Milwaukee — degree_requirements 2026-27 · program_key=engineering-bs · requirement_key=engineering-major-requirements-mathematics-14-credits [new] (labeled_in_source)
- source: https://catalog.uwm.edu/engineering-applied-science/industrial-manufacturing-engineering/engineering-bs/ (sha256 1eec26aa5299)
- issues: requirement_groups_skipped
  - courses: MATH 231 ⟵ “MATH 231 - Calculus and Analytic Geometry I”
  - courses: MATH 232 ⟵ “MATH 232 - Calculus and Analytic Geometry II”
### `fc645e0c24c5a243` University of Wisconsin-Milwaukee Flex — appeals 2026-27 [new] (source_unlabeled)
- source: https://flex.wisconsin.edu/tuition-financial-aid/financial-aid/applying-financial-aid/ (sha256 297e805471a3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have a special circumstance when completing the FAFSA or if your income has changed please contact our office to discuss how we might assist you.”
### `5daa059a03c23e6f` University of Wisconsin-Milwaukee Flex — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://flex.wisconsin.edu/tuition-financial-aid/financial-aid/cost-of-attendance/ (sha256 4e3e5ef778a4)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 2, "rows": 7}
  - with_parents_or_family:Tuition: 9000 ⟵ “Tuition | $9,000 | $9,000”
  - with_parents_or_family:Books/Supplies: 800 ⟵ “Books/Supplies | $800 | $800”
  - with_parents_or_family:Room: 0 ⟵ “Room | $0 | $8,400”
  - with_parents_or_family:Board: 4400 ⟵ “Board | $4,400 | $4,400”
  - with_parents_or_family:Personal/Miscellaneous: 2440 ⟵ “Personal/Miscellaneous | $2,440 | $2,440”
  - with_parents_or_family:Transportation: 100 ⟵ “Transportation | $100 | $100”
  - with_parents_or_family:TOTALS: 16740 ⟵ “TOTALS | $16,740 | $25,140”
  - column:Tuition: 9000 ⟵ “Tuition | $9,000 | $9,000”
  - column:Books/Supplies: 800 ⟵ “Books/Supplies | $800 | $800”
  - column:Room: 8400 ⟵ “Room | $0 | $8,400”
  - column:Board: 4400 ⟵ “Board | $4,400 | $4,400”
  - column:Personal/Miscellaneous: 2440 ⟵ “Personal/Miscellaneous | $2,440 | $2,440”
  - column:Transportation: 100 ⟵ “Transportation | $100 | $100”
  - column:TOTALS: 25140 ⟵ “TOTALS | $16,740 | $25,140”
### `13799c67f17df23e` University of Wisconsin-Parkside — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.uwp.edu/wp-content/uploads/2026/07/CDS_2024-25-UW-Parkside.pdf (sha256 406de1c1a43c)
- issues: applications_breakdown_does_not_reconcile, admits_breakdown_does_not_reconcile, enrolled_breakdown_does_not_reconcile, stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 0 ⟵ “Total first-time, first-year who applied                                                   2,048            1,623          384            41             0”
  - admits: 0 ⟵ “Total first-time, first-year who were admitted                                             1,997            1,581          376            40             0”
  - enrolled: 0 ⟵ “Total first-time, first-year who enrolled                                                    522              435           76            11             0”
  - sat_composite_25..75: [1020, 1130, 1230] ⟵ “SAT Composite                               1020                1130               1230”
  - sat_reading_25..75: [520, 570, 620] ⟵ “SAT Evidence-Based Reading and               520                 570                620”
  - sat_math_25..75: [520, 560, 610] ⟵ “SAT Math                                     520                 560                610”
  - act_25..75: [17, 21, 25] ⟵ “ACT Composite                                17                  21                 25”
### `59d7ecd57bfdd817` University of Wisconsin-Parkside — admissions_metrics 2020-21 [new] (labeled_in_source)
- source: https://www.uwp.edu/wp-content/uploads/2026/07/CDS_2020-2021_UW-Parkside_Final.pdf (sha256 1f02b3b89ff6)
- issues: c1_totals_incomplete, stale_year_label:2020-21
- checks: {"fields": ["act_25", "act_75", "entering_fall_year", "sat_composite_25", "sat_composite_75", "sat_math_25", "sat_math_75", "sat_reading_25", "sat_reading_75"]}
  - sat_composite_25..75: [1030, 1140] ⟵ “SAT Composite                              1030                1140”
  - sat_reading_25..75: [510, 585] ⟵ “SAT Evidence-Based Reading and   510                585”
  - sat_math_25..75: [500, 590] ⟵ “SAT Math                                     500                590”
  - act_25..75: [17, 23] ⟵ “ACT Composite                                17                 23”
### `5b4e496d9d909f27` University of Wisconsin-Parkside — admissions_metrics 2023-24 [new] (labeled_in_source)
- source: https://www.uwp.edu/wp-content/uploads/2026/07/CDS_2023-24-UW-Parkside_Final.pdf (sha256 0de069f3cc19)
- issues: stale_year_label:2023-24
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_75"]}
  - applications: 3024 ⟵ “Total first-time, first-year who applied                                          2,197              369            458             0      3,024”
  - admits: 2840 ⟵ “Total first-time, first-year who were admitted                                    2,085              345            410             0      2,840”
  - enrolled: 565 ⟵ “Total first-time, first-year who enrolled                                           468               72             25                       565”
  - sat_reading_25..75: [520, 670] ⟵ “SAT Evidence-Based Reading and              442.5                520                670”
  - sat_math_25..75: [400, 540, 680] ⟵ “SAT Math                                     400                 540                680”
  - act_25..75: [18, 21, 25] ⟵ “ACT Composite                                18                  21                 25”
### `9791cea264e11272` University of Wisconsin-Parkside — admissions_metrics 2021-22 [new] (labeled_in_source)
- source: https://www.uwp.edu/wp-content/uploads/2026/07/CDS_2021-2022-UW-Parkside.pdf (sha256 ee6e72230ecf)
- issues: stale_year_label:2021-22
- checks: {"fields": ["act_25", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_75", "sat_math_25", "sat_math_75", "sat_reading_25", "sat_reading_75"]}
  - applications: 1920 ⟵ “Total first-time, first-year (degree-seeking) who applied                       1920”
  - admits: 1713 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                 1713”
  - enrolled: 468 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                      468”
  - sat_composite_25..75: [910, 1158] ⟵ “SAT Composite                        910            1158”
  - sat_reading_25..75: [490, 550] ⟵ “SAT Evidence-Based Reading and   490             550”
  - sat_math_25..75: [420, 578] ⟵ “SAT Math                             420             578”
  - act_25..75: [18, 24] ⟵ “ACT Composite                         18              24”
### `c5c0654daaf694bc` University of Wisconsin-Parkside — admissions_metrics 2019-20 [new] (labeled_in_source)
- source: https://www.uwp.edu/wp-content/uploads/2026/07/CDS_2019-2020_UW-Parkside_Final.pdf (sha256 a6c884ff7e02)
- issues: c1_totals_incomplete, stale_year_label:2019-20
- checks: {"fields": ["entering_fall_year", "sat_composite_25", "sat_composite_75"]}
  - sat_composite_25..75: [940, 1140] ⟵ “SAT Composite                           940                1140”
### `d562d07929a81668` University of Wisconsin-Parkside — admissions_metrics 2022-23 [new] (labeled_in_source)
- source: https://www.uwp.edu/wp-content/uploads/2026/07/CDS_2022-23-UW-Parkside_Final.pdf (sha256 0f461b7e9e0c)
- issues: c1_totals_incomplete, stale_year_label:2022-23
- checks: {"fields": ["act_25", "act_50", "act_75", "entering_fall_year"]}
  - act_25..75: [17, 21, 24] ⟵ “ACT Composite                        17              21              24”
### `caffa49150822544` University of Wisconsin-Parkside — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwp.edu/live/offices/financialaid/maintaining-sap/ (sha256 e4f44b92155f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appealing Satisfactory Academic Progress If you wish to appeal your ineligible status, an SAP Appeal Form must be submitted to the Financial Aid Office.”
  - sentence: sap_appeal ⟵ “Students must submit a Satisfactory Academic Progress Appeal Form.”
### `1ce9122de7bc5cb2` University of Wisconsin-Parkside — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.uwp.edu/apply/payingforschool/projected-costs/ (sha256 2a03676bdd5b)
- issues: stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition and Fees: 8271 ⟵ “Tuition and Fees | $8,271 | $8,271”
  - on_campus:Housing*: 4975 ⟵ “Housing* | $4,975 | ”
  - on_campus:Food**: 4368 ⟵ “Food** | $4,368 | (commuter plans available)”
  - on_campus:Total: 17614 ⟵ “Total | $17,614 | $8,271”
  - with_parents_or_family:Tuition and Fees: 8271 ⟵ “Tuition and Fees | $8,271 | $8,271”
  - with_parents_or_family:Total: 8271 ⟵ “Total | $17,614 | $8,271”
### `8eb64c909414cee0` University of Wisconsin-Parkside — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwp.edu/apply/payingforschool/projected-costs/ (sha256 2a03676bdd5b)
- issues: residency_names_another_state, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition and Fees: 9985 ⟵ “Tuition and Fees | $9,985 | $9,985”
  - on_campus:Housing*: 4975 ⟵ “Housing* | $4,975 | ”
  - on_campus:Food**: 4638 ⟵ “Food** | $4,638 | (commuter plans available)”
  - on_campus:Total: 19598 ⟵ “Total | $19,598 | $9,985”
  - with_parents_or_family:Tuition and Fees: 9985 ⟵ “Tuition and Fees | $9,985 | $9,985”
  - with_parents_or_family:Total: 9985 ⟵ “Total | $19,598 | $9,985”
### `c8e08a58bfbadaea` University of Wisconsin-Parkside — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.uwp.edu/apply/payingforschool/projected-costs/ (sha256 2a03676bdd5b)
- issues: stale_year_label:2024-25
- checks: {"columns": 2, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition and Fees: 17430 ⟵ “Tuition and Fees | $17,430 | $17,430”
  - on_campus:Housing*: 4975 ⟵ “Housing* | $4,975 | ”
  - on_campus:Food**: 4368 ⟵ “Food** | $4,368 | (commuter plans available)”
  - on_campus:Total: 26773 ⟵ “Total | $26,773 | $17,430”
  - with_parents_or_family:Tuition and Fees: 17430 ⟵ “Tuition and Fees | $17,430 | $17,430”
  - with_parents_or_family:Total: 17430 ⟵ “Total | $26,773 | $17,430”
### `36324a6a45ae569b` University of Wisconsin-Platteville — appeals 2018-19 [new] (labeled_in_source)
- source: https://www.uwplatt.edu/department/financial-aid-scholarships/satisfactory-academic-progress-policy (sha256 a2f27271b3f9)
- issues: stale_year_label:2018-19, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “What has now changed in the situation so that the student can meet SAP requirements going forward Part A Students may appeal their Satisfactory Academic Progress status by documenting the extenuating circumstance(s) which prevented the student from meeting the academic progress standards.”
### `f49ce43d84a680b5` University of Wisconsin-Platteville — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.uwplatt.edu/undergraduate/admission-prior-credits/credits-by-examination/ (sha256 3eee37329c72)
- issues: score_column_not_scores
- checks: {"distinct_exams": 40, "equivalencies": 43, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL See Department]:  ⟵ “Biology (HL) | See Department | See Department | See Department”
  - equivalencies[IB-BIOLOGY-SL|SL See Department]:  ⟵ “Biology (SL) | See Department | See Department | See Department”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4, 5, 6, 7]:  ⟵ “Business and Management (HL) | 4, 5, 6, 7 | 3 | BUSADMIN 1000T - Elective Credit1”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|SL See Department]:  ⟵ “Business and Management (SL) | See Department | See Department | See Department”
  - equivalencies[IB-CHEMISTRY-HL|HL 4, 5, 6, 7]:  ⟵ “Chemistry (HL) | 4, 5, 6, 7 | 8 | CHEMSTRY 1140, CHEMSTRY 1240”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|HL 4, 5, 6, 7]:  ⟵ “Computer Science (HL) | 4, 5, 6, 7 | 3 | COMPUTER 1830”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|SL 4, 5, 6, 7]:  ⟵ “Computer Science (SL) | 4, 5, 6, 7 | 3 | COMPUTER 1130”
  - equivalencies[IB-ECONOMICS-HL|HL 4, 5, 6, 7]:  ⟵ “Economics (HL) | 4, 5, 6, 7 | 6 | ECONOMIC 2130, ECONOMIC 2230”
  - equivalencies[IB-ECONOMICS-SL|SL See Department]:  ⟵ “Economics (SL) | See Department | See Department | See Department”
  - equivalencies[IB-FILM-HL|HL See Department]:  ⟵ “Film (HL) | See Department | See Department | See Department”
  - equivalencies[IB-FRENCH-HL|HL 4, 5, 6, 7]:  ⟵ “French (HL) | 4, 5, 6, 7 | 8 | FRENCH 1040, FRENCH 1140”
  - equivalencies[IB-FRENCH-SL|SL 5, 6, 7]:  ⟵ “French (SL) | 5, 6, 7 | 4 | FRENCH 1040”
  - equivalencies[IB-GEOGRAPHY-HL|HL 4, 5, 6, 7]:  ⟵ “Geography (HL) | 4, 5, 6, 7 | 3 | ENVSS 1230”
  - equivalencies[IB-GEOGRAPHY-SL|SL See Department]:  ⟵ “Geography (SL) | See Department | See Department | See Department”
  - equivalencies[IB-GERMAN-HL|HL 4, 5, 6, 7]:  ⟵ “German (HL) | 4, 5, 6, 7 | 8 | GERMAN 1240, GERMAN 1340”
  - equivalencies[IB-GERMAN-SL|SL 5, 6, 7]:  ⟵ “German (SL) | 5, 6, 7 | 4 | GERMAN 1240”
  - equivalencies[IB-GLOBAL-POLITICS-HL|HL 4, 5, 6, 7]:  ⟵ “Global Politics (HL) | 4, 5, 6, 7 | 3 | POLISCI 2360”
  - equivalencies[IB-GLOBAL-POLITICS-SL|SL NA]:  ⟵ “Global Politics (SL) | NA | 0 | Not accepted”
  - equivalencies[IB-HISTORY-HL|HL See Department]:  ⟵ “History of Africa (HL) | See Department | See Department | See Department”
  - equivalencies[IB-HISTORY-HL|HL 4, 5, 6, 7]:  ⟵ “History (HL) | 4, 5, 6, 7 | 3 | HISTORY 2020”
  - equivalencies[IB-HISTORY-SL|SL 5, 6, 7]:  ⟵ “History (SL) | 5, 6, 7 | 3 | HISTORY 2010”
  - equivalencies[IB-LATIN-HL|HL 4, 5, 6, 7]:  ⟵ “Latin (HL) | 4, 5, 6, 7 | 4 | TRANSFER 1000T - Elective Credit6”
  - equivalencies[IB-LATIN-SL|SL 5, 6, 7]:  ⟵ “Latin (SL) | 5, 6, 7 | 3 | TRANSFER 1000T - Elective Credit6”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|HL 4]:  ⟵ “Mathematics: Analysis and Approaches (HL) | 4 | 3 | MATH 2630”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|HL 5, 6, 7]:  ⟵ “Mathematics: Analysis and Approaches (HL) | 5, 6, 7 | 4 | MATH 2640”
  - … 18 more rows
### `f93d1c1be1853dcc` University of Wisconsin-River Falls — appeals 2026-27 [new] (source_unlabeled)
- source: https://students.uwrf.edu/financial-aid/policies-and-procedures (sha256 d0ac8a2da0af)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Policy Financial Aid Appeal Forms Satisfactory Academic Progress (SAP) appeal forms - GPA/Completion Rate or Max Time *Please note you will be required to log in with your Falcon ID (w# and password) to complete this form. | IMPORTANT: | Appeals must be submitted before the appropriate deadline each semester in order to be considered for financial aid for that semest”
  - sentence: sap_appeal ⟵ “SAP appeal deadlines for each semester (your form must be received on or before): Fall 2026: Nov. 8, 2026 Spring 2027: April 2, 2027 Summer 2027: July 16, 2027 Estimate the semester GPA you will need to earn to bring your cumulative GPA back up to the required minimum for financial aid eligibility using the Registrar's GPA Calculator.”
### `105fb7b9e4eb4f51` University of Wisconsin-River Falls — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://students.uwrf.edu/financial-aid/costs (sha256 dffe943ef585)
- issues: components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 10}
  - on_campus:Tuition and Fees: 9630 ⟵ “Tuition and Fees | $9,630 | $12,110 | $14,510 | $13,470 | $18,690”
  - on_campus:Housing: 5560 ⟵ “Housing | $5,560 | $5,560 | $5,560 | $5,560 | $5,560”
  - on_campus:Food: 3370 ⟵ “Food | $3,370 | $3,370 | $3,370 | $3,370 | $3,370”
  - on_campus:Personal: 2370 ⟵ “Personal | $2,370 | $2,370 | $2,370 | $2,370 | $2,370”
  - on_campus:Transportation: 1500 ⟵ “Transportation | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - on_campus:Books and Supplies: 450 ⟵ “Books and Supplies | $450 | $450 | $450 | $450 | $450”
  - on_campus:Out of State Travel: 0 ⟵ “Out of State Travel | $0 | $0 | $1,200 | $1,200 | $1,200”
  - on_campus:TOTAL: 23110 ⟵ “TOTAL | $23,110 | $25,590 | $29,190 | $28,150 | $33,370”
  - on_campus:Total Direct Costs: 18560 ⟵ “Total Direct Costs | $18,560 | $21,040 | $23,440 | $22,400 | $27,620”
  - on_campus:Total Indirect Costs: 4320 ⟵ “Total Indirect Costs | $4,320 | $4,320 | $5,520 | $5,520 | $5,520”
  - on_campus:Tuition and Fees: 12110 ⟵ “Tuition and Fees | $9,630 | $12,110 | $14,510 | $13,470 | $18,690”
  - on_campus:Housing: 5560 ⟵ “Housing | $5,560 | $5,560 | $5,560 | $5,560 | $5,560”
  - on_campus:Food: 3370 ⟵ “Food | $3,370 | $3,370 | $3,370 | $3,370 | $3,370”
  - on_campus:Personal: 2370 ⟵ “Personal | $2,370 | $2,370 | $2,370 | $2,370 | $2,370”
  - on_campus:Transportation: 1500 ⟵ “Transportation | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - on_campus:Books and Supplies: 450 ⟵ “Books and Supplies | $450 | $450 | $450 | $450 | $450”
  - on_campus:Out of State Travel: 0 ⟵ “Out of State Travel | $0 | $0 | $1,200 | $1,200 | $1,200”
  - on_campus:TOTAL: 25590 ⟵ “TOTAL | $23,110 | $25,590 | $29,190 | $28,150 | $33,370”
  - on_campus:Total Direct Costs: 21040 ⟵ “Total Direct Costs | $18,560 | $21,040 | $23,440 | $22,400 | $27,620”
  - on_campus:Total Indirect Costs: 4320 ⟵ “Total Indirect Costs | $4,320 | $4,320 | $5,520 | $5,520 | $5,520”
### `6f799cb03d9fd53a` University of Wisconsin-River Falls — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://students.uwrf.edu/sites/default/files/2026-07/25-26%20COA%20Archived%20for%20web.pdf (sha256 9c68ecf7039f)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 5, "rows": 30}
  - column:Tuition and Fees: 9440 ⟵ “Tuition and Fees | $9,440 | $11,190 | $14,220 | $13,210 | $18,330”
  - column:Housing▼: 5380 ⟵ “Housing▼ | $5,380 | $5,380 | $5,380 | $5,380 | $5,380”
  - column:Food▼: 3210 ⟵ “Food▼ | $3,210 | $3,210 | $3,210 | $3,210 | $3,210”
  - column:Total Direct Costs: 18030 ⟵ “Total Direct Costs | $18,030 | $19,780 | $22,810 | $21,800 | $26,920”
  - column:Personal: 2370 ⟵ “Personal | $2,370 | $2,370 | $2,370 | $2,370 | $2,370”
  - column:Transportation: 1500 ⟵ “Transportation | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - column:Books and Supplies: 450 ⟵ “Books and Supplies | $450 | $450 | $450 | $450 | $450”
  - column:Out of State Travel: 0 ⟵ “Out of State Travel | $0 | $0 | $0 | $1,130 | $1,130”
  - column:Total Indirect Costs: 4320 ⟵ “Total Indirect Costs | $4,320 | $4,320 | $4,320 | $5,450 | $5,450”
  - column:TOTAL: 22350 ⟵ “TOTAL | $22,350 | $24,100 | $27,130 | $27,250 | $32,370”
  - column:Tuition and Fees (2): 9440 ⟵ “Tuition and Fees | $9,440 | $11,190 | $14,220 | $13,210 | $18,330”
  - column:Total Direct Costs (2): 9440 ⟵ “Total Direct Costs | $9,440 | $11,910 | $14,220 | $13,210 | $18,330”
  - column:Housing: 8100 ⟵ “Housing | $8,100 | $8,100 | $8,100 | $8,100 | $8,100”
  - column:Food: 3300 ⟵ “Food | $3,300 | $3,300 | $3,300 | $3,300 | $3,300”
  - column:Personal (2): 2370 ⟵ “Personal | $2,370 | $2,370 | $2,370 | $2,370 | $2,370”
  - column:Transportation (2): 2880 ⟵ “Transportation | $2,880 | $2,880 | $2,880 | $2,880 | $2,880”
  - column:Books and Supplies (2): 450 ⟵ “Books and Supplies | $450 | $450 | $450 | $450 | $450”
  - column:Out of State Travel (2): 0 ⟵ “Out of State Travel | $0 | $0 | $0 | $1,130 | $1,130”
  - column:Total Indirect Costs (2): 17130 ⟵ “Total Indirect Costs | $17,130 | $17,130 | $17,130 | $18,260 | $18,260”
  - column:TOTAL (2): 26570 ⟵ “TOTAL | $26,570 | $28,320 | $31,350 | $31,470 | $36,590”
  - column:Tuition and Fees (3): 9440 ⟵ “Tuition and Fees | $9,440 | $11,190 | $14,220 | $13,210 | $18,330”
  - column:Total Direct Costs (3): 9440 ⟵ “Total Direct Costs | $9,440 | $11,190 | $14,220 | $13,210 | $18,330”
  - column:Books and Supplies (3): 450 ⟵ “Books and Supplies | $450 | $450 | $450 | $450 | $450”
  - column:Housing (2): 1650 ⟵ “Housing | $1,650 | $1,650 | $1,650 | $1,650 | $1,650”
  - column:Food (2): 1120 ⟵ “Food | $1,120 | $1,120 | $1,120 | $1,120 | $1,120”
  - … 125 more rows
### `8cc8e70679bd64bf` University of Wisconsin-River Falls — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://students.uwrf.edu/financial-aid/costs (sha256 dffe943ef585)
- issues: components_do_not_reconcile, residency_unknown
- checks: {"columns": 2, "components_reconcile": false, "rows": 10}
  - on_campus:Tuition and Fees: 14510 ⟵ “Tuition and Fees | $9,630 | $12,110 | $14,510 | $13,470 | $18,690”
  - on_campus:Housing: 5560 ⟵ “Housing | $5,560 | $5,560 | $5,560 | $5,560 | $5,560”
  - on_campus:Food: 3370 ⟵ “Food | $3,370 | $3,370 | $3,370 | $3,370 | $3,370”
  - on_campus:Personal: 2370 ⟵ “Personal | $2,370 | $2,370 | $2,370 | $2,370 | $2,370”
  - on_campus:Transportation: 1500 ⟵ “Transportation | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - on_campus:Books and Supplies: 450 ⟵ “Books and Supplies | $450 | $450 | $450 | $450 | $450”
  - on_campus:Out of State Travel: 1200 ⟵ “Out of State Travel | $0 | $0 | $1,200 | $1,200 | $1,200”
  - on_campus:TOTAL: 29190 ⟵ “TOTAL | $23,110 | $25,590 | $29,190 | $28,150 | $33,370”
  - on_campus:Total Direct Costs: 23440 ⟵ “Total Direct Costs | $18,560 | $21,040 | $23,440 | $22,400 | $27,620”
  - on_campus:Total Indirect Costs: 5520 ⟵ “Total Indirect Costs | $4,320 | $4,320 | $5,520 | $5,520 | $5,520”
  - on_campus:Tuition and Fees: 13470 ⟵ “Tuition and Fees | $9,630 | $12,110 | $14,510 | $13,470 | $18,690”
  - on_campus:Housing: 5560 ⟵ “Housing | $5,560 | $5,560 | $5,560 | $5,560 | $5,560”
  - on_campus:Food: 3370 ⟵ “Food | $3,370 | $3,370 | $3,370 | $3,370 | $3,370”
  - on_campus:Personal: 2370 ⟵ “Personal | $2,370 | $2,370 | $2,370 | $2,370 | $2,370”
  - on_campus:Transportation: 1500 ⟵ “Transportation | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - on_campus:Books and Supplies: 450 ⟵ “Books and Supplies | $450 | $450 | $450 | $450 | $450”
  - on_campus:Out of State Travel: 1200 ⟵ “Out of State Travel | $0 | $0 | $1,200 | $1,200 | $1,200”
  - on_campus:TOTAL: 28150 ⟵ “TOTAL | $23,110 | $25,590 | $29,190 | $28,150 | $33,370”
  - on_campus:Total Direct Costs: 22400 ⟵ “Total Direct Costs | $18,560 | $21,040 | $23,440 | $22,400 | $27,620”
  - on_campus:Total Indirect Costs: 5520 ⟵ “Total Indirect Costs | $4,320 | $4,320 | $5,520 | $5,520 | $5,520”
### `ff4aed2efebc926b` University of Wisconsin-River Falls — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://students.uwrf.edu/financial-aid/costs (sha256 dffe943ef585)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 10}
  - on_campus:Tuition and Fees: 18690 ⟵ “Tuition and Fees | $9,630 | $12,110 | $14,510 | $13,470 | $18,690”
  - on_campus:Housing: 5560 ⟵ “Housing | $5,560 | $5,560 | $5,560 | $5,560 | $5,560”
  - on_campus:Food: 3370 ⟵ “Food | $3,370 | $3,370 | $3,370 | $3,370 | $3,370”
  - on_campus:Personal: 2370 ⟵ “Personal | $2,370 | $2,370 | $2,370 | $2,370 | $2,370”
  - on_campus:Transportation: 1500 ⟵ “Transportation | $1,500 | $1,500 | $1,500 | $1,500 | $1,500”
  - on_campus:Books and Supplies: 450 ⟵ “Books and Supplies | $450 | $450 | $450 | $450 | $450”
  - on_campus:Out of State Travel: 1200 ⟵ “Out of State Travel | $0 | $0 | $1,200 | $1,200 | $1,200”
  - on_campus:TOTAL: 33370 ⟵ “TOTAL | $23,110 | $25,590 | $29,190 | $28,150 | $33,370”
  - on_campus:Total Direct Costs: 27620 ⟵ “Total Direct Costs | $18,560 | $21,040 | $23,440 | $22,400 | $27,620”
  - on_campus:Total Indirect Costs: 5520 ⟵ “Total Indirect Costs | $4,320 | $4,320 | $5,520 | $5,520 | $5,520”
### `5e12c0d53acd9c0c` University of Wisconsin-River Falls — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.uwrf.edu/sites/default/files/files/AP-Guide-Update-2024.pdf (sha256 43b2767cd6ae)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 8, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|3]:  ⟵ “Biology                                         3        3 credits BIOL 100 (or Biology elective if Biology major)”
  - equivalencies[CLEP-CALCULUS|3]:  ⟵ “Calculus BC                                     3        4 credits for MATH 166. Students may attempt to earn credit for”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Economics - Macroeconomics                      3        3 credits economics elective”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3]:  ⟵ “Economics - Microeconomics                      3        3 credits economics elective”
  - equivalencies[CLEP-FRENCH-LANGUAGE|5]:  ⟵ “French Literature                         5     3 credits for FREN 353”
  - equivalencies[CLEP-GERMAN-LANGUAGE|3]:  ⟵ “German Language & Culture                 3     4 credits for GERM 101”
  - equivalencies[CLEP-GERMAN-LANGUAGE|4]:  ⟵ “German Language & Culture (with           4     4 credits for GERM 102 and placement in GERM 201. If GERM”
  - equivalencies[CLEP-GERMAN-LANGUAGE|4]:  ⟵ “German Language & Culture (with above     4     3 credits for GERM 201 and placement in GERM 202. If GERM”
  - equivalencies[CLEP-GERMAN-LANGUAGE|5]:  ⟵ “German Language & Culture                 5     3 credits for GERM 202 and placement in GERM 301. If GERM”
  - equivalencies[CLEP-PRECALCULUS|3]:  ⟵ “Precalculus                                 3      3 credits for MATH 146”
  - equivalencies[CLEP-SPANISH-LANGUAGE|3]:  ⟵ “Spanish Language                            3      4 credits for SPAN 101”
  - equivalencies[CLEP-SPANISH-LANGUAGE|4]:  ⟵ “Spanish Language (with average/low          4      4 credits for SPAN 102 and placement in SPAN 201. If SPAN”
  - equivalencies[CLEP-SPANISH-LANGUAGE|4]:  ⟵ “Spanish Language (with above                4      3 credits for SPAN 201 and placement in SPAN 202. If SPAN”
  - equivalencies[CLEP-SPANISH-LANGUAGE|5]:  ⟵ “Spanish Language                            5      3 credits for SPAN 202 and placement in SPAN 301. If SPAN”
  - equivalencies[CLEP-SPANISH-LANGUAGE|5]:  ⟵ “Spanish Literature                          5      3 credits Spanish literature elective, applicable to a Spanish”
### `7cfbdb6e18e3e1d4` University of Wisconsin-Stout — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwstout.edu/admissions-aid/paying-college/financial-aid (sha256 4497182a830d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Unique Circumstance Questions My family has unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “There will be no place to report unusual circumstances on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If a family feels that they have unusual circumstances that may affect the student's financial aid eligibility, please contact our office directly to discuss appropriate action: e-mail finaid1@uwstout.edu or call 715-232-1363.”
### `ed5db19ae133a0c4` University of Wisconsin-Stout — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwstout.edu/admissions-aid/paying-college/tuition-fees-payments (sha256 5de3cfcf442e)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "rows": 5}
  - column:Wisconsin Resident: 11767 ⟵ “Wisconsin Resident | $11,767 | $9,548 | $21,315”
  - column:Minnesota Resident: 13773 ⟵ “Minnesota Resident | $13,773 | $9,548 | $23,321”
  - column:Midwest Tuition & MSEP *: 15898 ⟵ “Midwest Tuition & MSEP * | $15,898 | $9,548 | $25,446”
  - column:Return to WI Tuition: 16580 ⟵ “Return to WI Tuition | $16,580 | $9,548 | $26,128”
  - column:Non-Resident: 20939 ⟵ “Non-Resident | $20,939 | $9,548 | $30,487”
  - column:Wisconsin Resident: 9548 ⟵ “Wisconsin Resident | $11,767 | $9,548 | $21,315”
  - column:Minnesota Resident: 9548 ⟵ “Minnesota Resident | $13,773 | $9,548 | $23,321”
  - column:Midwest Tuition & MSEP *: 9548 ⟵ “Midwest Tuition & MSEP * | $15,898 | $9,548 | $25,446”
  - column:Return to WI Tuition: 9548 ⟵ “Return to WI Tuition | $16,580 | $9,548 | $26,128”
  - column:Non-Resident: 9548 ⟵ “Non-Resident | $20,939 | $9,548 | $30,487”
  - column:Wisconsin Resident: 21315 ⟵ “Wisconsin Resident | $11,767 | $9,548 | $21,315”
  - column:Minnesota Resident: 23321 ⟵ “Minnesota Resident | $13,773 | $9,548 | $23,321”
  - column:Midwest Tuition & MSEP *: 25446 ⟵ “Midwest Tuition & MSEP * | $15,898 | $9,548 | $25,446”
  - column:Return to WI Tuition: 26128 ⟵ “Return to WI Tuition | $16,580 | $9,548 | $26,128”
  - column:Non-Resident: 30487 ⟵ “Non-Resident | $20,939 | $9,548 | $30,487”
### `3819ba9b33882749` University of Wisconsin-Superior — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://uwsuper.edu/paying-for-college/tuition-and-fees/jterm/ (sha256 5f05370a7fb0)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 16730 ⟵ “Tuition and Fees | 8,810 | 10,710 | 16,730”
  - column:Living Expenses (Housing and Meals): 10670 ⟵ “Living Expenses (Housing and Meals) | 10,670 | 10,670 | 10,670”
  - column:Books and Course Materials: 1050 ⟵ “Books and Course Materials | 1,050 | 1,050 | 1,050”
  - column:Transportation: 1520 ⟵ “Transportation | 1,520 | 1,520 | 1,520”
  - column:Personal/Miscellaneous: 1400 ⟵ “Personal/Miscellaneous | 1,400 | 1,400 | 1,400”
  - column:Loan Fees: 70 ⟵ “Loan Fees | 70 | 70 | 70”
  - column:Total: 31440 ⟵ “Total | 23,520 | 25,420 | 31,440”
### `3b775b7d8b97b21f` University of Wisconsin-Superior — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://uwsuper.edu/paying-for-college/tuition-and-fees/jterm/ (sha256 5f05370a7fb0)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 8810 ⟵ “Tuition and Fees | 8,810 | 10,710 | 16,730”
  - column:Living Expenses (Housing and Meals): 10670 ⟵ “Living Expenses (Housing and Meals) | 10,670 | 10,670 | 10,670”
  - column:Books and Course Materials: 1050 ⟵ “Books and Course Materials | 1,050 | 1,050 | 1,050”
  - column:Transportation: 1520 ⟵ “Transportation | 1,520 | 1,520 | 1,520”
  - column:Personal/Miscellaneous: 1400 ⟵ “Personal/Miscellaneous | 1,400 | 1,400 | 1,400”
  - column:Loan Fees: 70 ⟵ “Loan Fees | 70 | 70 | 70”
  - column:Total: 23520 ⟵ “Total | 23,520 | 25,420 | 31,440”
### `4bb4f1391b08ec3a` University of Wisconsin-Superior — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://uwsuper.edu/paying-for-college/tuition-and-fees/jterm/ (sha256 5f05370a7fb0)
- issues: residency_names_another_state, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 10710 ⟵ “Tuition and Fees | 8,810 | 10,710 | 16,730”
  - column:Living Expenses (Housing and Meals): 10670 ⟵ “Living Expenses (Housing and Meals) | 10,670 | 10,670 | 10,670”
  - column:Books and Course Materials: 1050 ⟵ “Books and Course Materials | 1,050 | 1,050 | 1,050”
  - column:Transportation: 1520 ⟵ “Transportation | 1,520 | 1,520 | 1,520”
  - column:Personal/Miscellaneous: 1400 ⟵ “Personal/Miscellaneous | 1,400 | 1,400 | 1,400”
  - column:Loan Fees: 70 ⟵ “Loan Fees | 70 | 70 | 70”
  - column:Total: 25420 ⟵ “Total | 23,520 | 25,420 | 31,440”
### `880816de07d7a784` University of Wisconsin-Superior — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://uwsuper.edu/paying-for-college/tuition-and-fees/fall-and-spring/ (sha256 5334270a5b77)
- issues: residency_names_another_state, residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees: 11360 ⟵ “Tuition and Fees | 9,480 | 11,360 | 17,950”
  - on_campus:Living Expenses (Housing and Meals): 11410 ⟵ “Living Expenses (Housing and Meals) | 11,410 | 11,410 | 11,410”
  - on_campus:Books and Course Materials: 1170 ⟵ “Books and Course Materials | 1,170 | 1,170 | 1,170”
  - on_campus:Transportation: 1680 ⟵ “Transportation | 1,680 | 1,680 | 1,680”
  - on_campus:Personal/Misc: 1400 ⟵ “Personal/Misc | 1,400 | 1,400 | 1,400”
  - on_campus:Loan Fees: 80 ⟵ “Loan Fees | 80 | 80 | 80”
  - on_campus:Total: 27100 ⟵ “Total | 25,220 | 27,100 | 33,690”
### `f315ba29f91b01bd` University of Wisconsin-Whitewater — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uww.edu/documents/registrar/Veterans/WING%20Tuition%20Grant%20Maximum%20Caps%20for%20the%202025-2026%20Academic%20Year.pdf (sha256 28d5cebddf27)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 5}
  - column:Tuition (most: 5253.24 ⟵ “Tuition (most | $5,253.24 | $437.77”
  - column:Business: 6828.24 ⟵ “Business | $6,828.24 | $569.02”
  - column:$5,410.68: 450.89 ⟵ “$5,410.68 | $450.89”
  - column:$6,853.20: 571.1 ⟵ “$6,853.20 | $571.10”
  - column:Nursing: 6040.68 ⟵ “Nursing | $6,040.68 | $503.39”
  - column:Tuition (most: 437.77 ⟵ “Tuition (most | $5,253.24 | $437.77”
  - column:Business: 569.02 ⟵ “Business | $6,828.24 | $569.02”
  - column:Nursing: 503.39 ⟵ “Nursing | $6,040.68 | $503.39”
### `cb9b951c70124a26` Waukesha County Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.wctc.edu/WCTC/Admissions/Tuition-and-Aid/Financial-Aid (sha256 9e7d7c5dc1ac)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Eligibility Types of Financial Aid Applying for Financial Aid Using Financial Aid Special and Unusual Circumstances Financial Aid Eligibility Students need to meet several criteria related to enrollment, program acceptance, and other criteria to receive financial aid.”
  - sentence: need_based_special_circumstances ⟵ “Use Calculator Special Circumstances The WCTC Financial Aid Office understands that students may have extenuating circumstances that affect their financial situation.”
  - sentence: need_based_special_circumstances ⟵ “If you believe the Free Application for Federal Student Aid (FAFSA) does not reflect your (or your parents) accurate financial picture, you may request a Special Circumstances Appeal to have your FAFSA application reviewed.”
  - sentence: need_based_special_circumstances ⟵ “Examples of Special Circumstances may include loss of employment, reduction in yearly income, divorce or separation, recent death of a parent or spouse, excessive medical or dental expenses, elementary and secondary school costs or childcare and dependent care costs.”
  - sentence: need_based_special_circumstances ⟵ “Meet with a Financial Aid Advisor to discuss your situation and get a Special Circumstance Appeal form.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Federal law allows some students with unusual circumstances who would otherwise be considered a Dependent student to submit the Free Application for Federal Student Aid (FAFSA) without parental information.”
### `ef34a5e8635a522a` Waukesha County Technical College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wctc.edu/WCTC/Admissions/Tuition-and-Aid/Financial-Aid (sha256 9e7d7c5dc1ac)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 4952 ⟵ “Tuition and Fees | $4,952 | $4,952”
  - with_parents_or_family:Books, Course Materials, Supplies, and Equipment: 1464 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,464 | $1,464”
  - with_parents_or_family:Living Expenses: 3184 ⟵ “Living Expenses | $3,184 | $10,308”
  - with_parents_or_family:Miscellaneous Personal Expenses: 3064 ⟵ “Miscellaneous Personal Expenses | $3,064 | $3,064”
  - with_parents_or_family:Transportation: 4104 ⟵ “Transportation | $4,104 | $4,104”
  - with_parents_or_family:Loan Fees: 86 ⟵ “Loan Fees | $86 | $86”
  - with_parents_or_family:Total*: 16854 ⟵ “Total* | $16,854 | $23,978”
  - off_campus_not_with_family:Tuition and Fees: 4952 ⟵ “Tuition and Fees | $4,952 | $4,952”
  - off_campus_not_with_family:Books, Course Materials, Supplies, and Equipment: 1464 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,464 | $1,464”
  - off_campus_not_with_family:Living Expenses: 10308 ⟵ “Living Expenses | $3,184 | $10,308”
  - off_campus_not_with_family:Miscellaneous Personal Expenses: 3064 ⟵ “Miscellaneous Personal Expenses | $3,064 | $3,064”
  - off_campus_not_with_family:Transportation: 4104 ⟵ “Transportation | $4,104 | $4,104”
  - off_campus_not_with_family:Loan Fees: 86 ⟵ “Loan Fees | $86 | $86”
  - off_campus_not_with_family:Total*: 23978 ⟵ “Total* | $16,854 | $23,978”
### `f686a74b5b929b11` Waukesha County Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.wctc.edu/WCTC/OffNav/Credit-by-Examination-Policy (sha256 edb8cf8d01c2)
- issues: score_scale_mismatch
- checks: {"distinct_exams": 22, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 809-227 American Government”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Lit | 50 | 801-204 Introduction to Literature”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 806-114 General Biology”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 804-198 Calculus 1”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 806-134 General Chemistry”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 804-195 College Algebra w/Apps”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 804-197 College Algebra and Trig w/Apps”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 801-136 English Composition 1”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 801-136 English Composition 1”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 804-107 College Mathematics”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 101-111 Accounting I - Principles”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | 50 | 803-212 American History 1877 to Present”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 809-188 Developmental Psychology”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems | 50 | 101-142 Accounting Information Systems”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 102-160 Business Law”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 809-198 Intro to Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 809-196 Intro to Sociology”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | 806-382 Applied Science”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 809-287 Macroeconomics”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 196-140 Managing People”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 104-102 Marketing Principles”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 809-143 Microeconomics”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|400]:  ⟵ “Fundamentals of College Algebra | 400 | 804-118 Intermediate Algebra w/Apps”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|400]:  ⟵ “Human Resource Management | 400 | 196-193 Human Resource Management”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|400]:  ⟵ “Lifespan Developmental Psychology | 400 | 809-188 Developmental Psychology”
### `ab381a2c66995916` Western Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.westerntc.edu/paying-for-college/scholarships/additional-scholarship-opportunities (sha256 052f7fc33d33)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Nursing Assistant Scholarships The Western Foundation may provide funding to students who experience modest financial situations and/or other special circumstances that hamper their ability to continue learning because of the inability to pay the tuition costs to take the Nursing Assistant class.”
### `3b7a083be58f2bff` Wisconsin Lutheran College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.wlc.edu/financial-aid-scholarships/undergraduate/apply-financial-aid.html (sha256 eab5a45074c5)
- issues: semantic_review_required, conflicting_sources:https://www.wlc.edu/_files/financial-aid/2026-2027-special-circumstances-form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Please be sure to complete the form(s) for the academic year for which you are seeking financial aid. 2026-2027 Private Tuition Paid Form (PDF) 2026-2027 Private Scholarship Confirmation Form (PDF) 2026-2027 Special Circumstances Form (PDF) What's Next?”
  - sentence: need_based_special_circumstances ⟵ “Refer to our Special Circumstance Form (see link, above).”
### `7a9031fe5eda40e3` Wisconsin Lutheran College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.wlc.edu/_files/financial-aid/2026-2027-special-circumstances-form.pdf (sha256 e9da90480101)
- issues: semantic_review_required, conflicting_sources:https://www.wlc.edu/financial-aid-scholarships/undergraduate/apply-financial-aid.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Form For 2026-27 Financial Aid Student’s Name _______________________________ Warrior ID#: ___________ (If known) The Department of Education allows the Financial Aid Office to make adjustments to your FAFSA with valid documentation if your family’s finances have significantly changed since 2024.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 8; pages by category: admissions_tests 1, cost_of_attendance 1, dual_enrollment 1, merit_scholarships 8, tuition_fees 1

## Blocked by the site (every request refused; needs the browser fallback)

- Alverno College (`ipeds-238193`)
- Viterbo University (`ipeds-240107`)
- Northwood Technical College (`ipeds-240198`)
- University of Wisconsin-Oshkosh (`ipeds-240365`)

## Leads: official pages found with no extracted record

- Bellin College: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation
- Beloit College: cost_of_attendance, admissions_tests, ib_credit, dual_enrollment, statewide_articulation, degree_requirements
- Blackhawk Technical College: admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, statewide_articulation, residency, degree_requirements, aid_appeals
- Bryant & Stratton College-Wauwatosa: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, degree_requirements
- Carroll University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Carthage College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Chippewa Valley Technical College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- College of Menominee Nation: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, degree_requirements
- Concordia University-Wisconsin: admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, degree_requirements
- Edgewood College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Fox Valley Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, degree_requirements
- Gateway Technical College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Herzing University-Brookfield: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Herzing University-Kenosha: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Herzing University-Madison: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Lac Courte Oreilles Ojibwe University: cost_of_attendance, merit_scholarships, dual_enrollment, transfer_credit
- Lakeland University: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Lakeshore Technical College: transfer_credit
- Lawrence University: cost_of_attendance, admissions_tests, merit_scholarships, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Madison Area Technical College: admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency, aid_appeals
- Maranatha Baptist University: cost_of_attendance, admissions_tests, common_data_set, transfer_credit, degree_requirements
- Marian University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Marquette University: cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation
- Mid-State Technical College: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency
- Milwaukee Area Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, residency
- Milwaukee Institute of Art & Design: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, aid_appeals
- Milwaukee School of Engineering: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Moraine Park Technical College: admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Mount Mary University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit
- Nicolet Area Technical College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Northcentral Technical College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- Northeast Wisconsin Technical College: admissions_tests, merit_scholarships, dual_enrollment, residency
- Northland College: transfer_credit, degree_requirements
- Ripon College: tuition_fees, cost_of_attendance, admissions_tests, degree_requirements
- Saint Norbert College: cost_of_attendance, admissions_tests, merit_scholarships
- Southwest Wisconsin Technical College: tuition_fees, cost_of_attendance, merit_scholarships, ap_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- University of Wisconsin-Eau Claire: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- University of Wisconsin-Green Bay: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- University of Wisconsin-La Crosse: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Wisconsin-Madison: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- University of Wisconsin-Milwaukee: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- University of Wisconsin-Milwaukee Flex: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- University of Wisconsin-Parkside: cost_of_attendance, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Wisconsin-Platteville: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, residency, degree_requirements
- University of Wisconsin-River Falls: admissions_tests, common_data_set, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Wisconsin-Stevens Point: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- University of Wisconsin-Stout: cost_of_attendance, admissions_tests, common_data_set, ap_credit, transfer_credit, statewide_articulation, residency
- University of Wisconsin-Superior: admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- University of Wisconsin-Whitewater: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Waukesha County Technical College: merit_scholarships, transfer_credit, degree_requirements
- Western Technical College: tuition_fees, cost_of_attendance, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency
- Wisconsin Lutheran College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, residency, degree_requirements
