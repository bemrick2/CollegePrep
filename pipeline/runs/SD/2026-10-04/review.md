# Review queue — SD (2026-27)

Pages fetched: 1208; failures: 166. Candidates: 114 (30 without issues, 84 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 3 | 4 | 8 | 2 | 2 |
| cost_of_attendance | 0 | 0 | 1 | 1 | 13 | 2 | 2 |
| admissions_tests | 0 | 0 | 0 | 0 | 16 | 1 | 2 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 17 | 2 |
| merit_scholarships | 0 | 0 | 2 | 0 | 13 | 2 | 2 |
| ap_credit | 0 | 0 | 1 | 0 | 5 | 11 | 2 |
| clep_credit | 0 | 0 | 2 | 0 | 5 | 10 | 2 |
| ib_credit | 0 | 0 | 0 | 0 | 2 | 15 | 2 |
| dual_enrollment | 0 | 0 | 7 | 2 | 2 | 6 | 2 |
| transfer_credit | 0 | 0 | 6 | 0 | 8 | 3 | 2 |
| statewide_articulation | 0 | 0 | 0 | 0 | 7 | 10 | 2 |
| residency | 0 | 0 | 0 | 0 | 8 | 9 | 2 |
| degree_requirements | 0 | 0 | 0 | 0 | 13 | 4 | 2 |
| aid_appeals | 0 | 0 | 0 | 11 | 1 | 5 | 2 |

## Ready for review (30)

### `304c568ff4ef4f1a` Black Hills State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.bhsu.edu/admissions/tuition-fees.html (sha256 cec2333b72ce)
- checks: {"columns": 1, "rows": 10}
  - column:Tuition: 4214 ⟵ “Tuition | $4,214”
  - column:General Activity Fees: 482 ⟵ “General Activity Fees | $482”
  - column:Food and Housing: 11322 ⟵ “Food and Housing | $11,322”
  - column:Books and Supplies: 230 ⟵ “Books and Supplies | $230”
  - column:Program Fee: 156 ⟵ “Program Fee | $156”
  - column:Certification/License Test Fee: 362 ⟵ “Certification/License Test Fee | $362”
  - column:Loan Fee: 150 ⟵ “Loan Fee | $150”
  - column:Miscellaneous: 2378 ⟵ “Miscellaneous | $2,378”
  - column:Transportation: 1876 ⟵ “Transportation | $1,876”
  - column:Annual Estimated Total: 21170 ⟵ “Annual Estimated Total | $21,170”
### `5807a03dfac5fce3` Black Hills State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.bhsu.edu/admissions/tuition-fees.html (sha256 cec2333b72ce)
- checks: {"columns": 1, "rows": 10}
  - column:Tuition: 7866 ⟵ “Tuition | $7,866”
  - column:General Activity Fees: 482 ⟵ “General Activity Fees | $482”
  - column:Food and Housing: 11322 ⟵ “Food and Housing | $11,322”
  - column:Books and Supplies: 230 ⟵ “Books and Supplies | $230”
  - column:Program Fee: 156 ⟵ “Program Fee | $156”
  - column:Certification/License Test Fee: 362 ⟵ “Certification/License Test Fee | $362”
  - column:Loan Fee: 150 ⟵ “Loan Fee | $150”
  - column:Miscellaneous: 2378 ⟵ “Miscellaneous | $2,378”
  - column:Transportation: 1876 ⟵ “Transportation | $1,876”
  - column:Annual Estimated Total: 24822 ⟵ “Annual Estimated Total | $24,822”
### `881a98ce3fc8f838` Black Hills State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.bhsu.edu/admissions/dual-credit/index.html (sha256 03f4c027b0de)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 2}
  - per_credit_hour_charge: 80.37 ⟵ “to enroll in college coursework at the rate of $80.37 per credit hour (or 1/2 of the”
  - per_credit_hour_charge: 40 ⟵ “courses. These courses are offered at $40 per credit hour.”
  - eligibility_tier: 3.5 ⟵ “earn a cumulative unweighted high school GPA of at least 3.50 on a 4.0 scale”
  - eligibility_tier: 3.25 ⟵ “earn a cumulative unweighted high school GPA of at least 3.25 on a 4.0 scale”
### `63a9b20366372fa7` Dakota State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://dsu.edu/admissions/undergraduate/dual-credit.html (sha256 23268514a788)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 2}
  - per_credit_hour_charge: 80.37 ⟵ “DSU currently has over 400 South Dakota high school juniors and seniors can begin their college career early through DSU's dual credit program. At a discounted rate of $80.37 per credit hour, you’ll earn college credits that also count toward your high school diploma.”
  - eligibility_tier: 3.5 ⟵ “earn a cumulative GPA of at least 3.50 on a 4.0 scale; or”
  - eligibility_tier: 3.25 ⟵ “earn a cumulative GPA of at least 3.25 on a 4.0 scale; or”
### `dc517fa4b40c4537` Lake Area Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.lakeareatech.edu/become-a-student/admissions-process/transfer-credits/ (sha256 4e89dac76d76)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Credits must have a grade of C or above to be considered for transfer.”
### `48296647501341b1` Mitchell Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.mitchelltech.edu/admissions/admissions-process/credit-for-prior-learning/ (sha256 4423c406223b)
- checks: {"distinct_exams": 12, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | Math requirement (3 credits)”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | Math requirement (3 credits)”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL101 (3 credits)”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | Math requirement (3 credits)”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACCT110 (3 credits)”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSYC130 (3 credits)Behavioral science requirement (3 credits)”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Intro Business Law | 50 | BUS140 (3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of | 50 | BUS212 (3 credits)”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | 50 | BUS120 (3 credits)”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | Math requirement (3 credits)”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | 50 | Behavioral science requirement (3 credits)”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | 50 | Social science requirement (3 credits)”
### `5164c4a62f16ec3f` Mitchell Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.mitchelltech.edu/admissions/admissions-process/credit-for-prior-learning/ (sha256 4423c406223b)
- checks: {"distinct_exams": 5, "equivalencies": 5, "rows_without_score": 0}
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | Math requirement (3 credits) | ”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | Math requirement (3 credits) | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | ENGL 101 (3 credits) | ”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | ENGL 101 (3 credits) | ”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSYC 101 (3 credits) | ”
### `m6ddbbdf1c917c03` Mitchell Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mitchelltech.edu/admissions/admissions-process/transfer-students/ (sha256 a5cff7bdf05a)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “A grade of C or better (2.0 on a 4.0 scale) shall be required in each course accepted in transfer.”
  - min_grade: C ⟵ “A grade of C or better (2.0 on a 4.0 scale) shall be required in each course accepted in transfer.”
### `01e854ecaa51079c` Mount Marty University — awards 2027-28 [new] (labeled_entering_class)
- source: https://www.mountmarty.edu/tuition-and-aid/scholarships-and-awards/incoming-firstyear/ (sha256 8423eac08c7e)
- checks: {"thresholds": null}
  - test_requirement: Old GED Score: 500-559 ⟵ “500-559 | 145-164 | $16,000”
  - award_amount_text: $16,000 ⟵ “500-559 | 145-164 | $16,000”
### `f18c8e87a313f99b` Mount Marty University — awards 2027-28 [new] (labeled_entering_class)
- source: https://www.mountmarty.edu/tuition-and-aid/scholarships-and-awards/incoming-firstyear/ (sha256 8423eac08c7e)
- checks: {"thresholds": null}
  - test_requirement: Old GED Score: 560-629 ⟵ “560-629 | 165-174 | $18,000”
  - award_amount_text: $18,000 ⟵ “560-629 | 165-174 | $18,000”
### `fb9e1fca857e0a2e` Mount Marty University — awards 2027-28 [new] (labeled_entering_class)
- source: https://www.mountmarty.edu/tuition-and-aid/scholarships-and-awards/incoming-firstyear/ (sha256 8423eac08c7e)
- checks: {"thresholds": null}
  - test_requirement: Old GED Score: 630-800 ⟵ “630-800 | 175-200 | $21,000”
  - award_amount_text: $21,000 ⟵ “630-800 | 175-200 | $21,000”
### `2807a1036960faa0` Mount Marty University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.mountmarty.edu/academics/dual-credit/ (sha256 b02a51a75e15)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - per_credit_hour_charge: 75 ⟵ “Dual credit classes are offered at high schools partnering with Mount Marty University, allowing students to earn high school and college credits concurrently, at a fraction of the cost - $75 per credit hour.”
  - eligibility_tier: 3.0 ⟵ “A cumulative GPA of 3.0”
### `056f4e91fd534343` Mount Marty University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mountmarty.edu/admission/undergraduate-students/transfer-students/transfer-faqs/ (sha256 b7fa9dcb35ee)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “In general, courses with a grade of C- or higher from an accredited institution will transfer (see the course catalog or contact the admission office for details).”
### `mbb9e4f57e274fb3` Northern State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://northern.edu/academics/high-school-programs/dual-credit (sha256 e0c664a495a8)
- checks: {"fields": [], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 3.5 ⟵ “Earn a cumulative GPA of at least 3.50 on a 4.0 scale.”
  - eligibility_tier: 3.25 ⟵ “Earn a cumulative GPA of at least 3.25 on a 4.0 scale.”
  - per_credit_hour_charge: 78.48 ⟵ “Students are responsible for paying tuition for dual credit courses. Dual credit students pay $78.48 per credit hour ($235.44 for a 3-credit course and $313.92 for a 4-credit course). Tuition payments are due no later than published fall/spring census dates. All students should access their bill via”
### `47b6884812109344` South Dakota School of Mines and Technology — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sdsmt.edu/admissions-aid/financial-aid-and-scholarships/scholarships/index.html (sha256 b528050b8594)
- checks: {"thresholds": {"act_min": 34, "sat_min": 1490}}
  - award_amount_text: $9,000 ⟵ “$9,000 | Gold Scholar | 34 | 1490”
  - test_requirement: ACT 34 / SAT 1490 ⟵ “$9,000 | Gold Scholar | 34 | 1490”
### `4fd329ded33bb66d` South Dakota School of Mines and Technology — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sdsmt.edu/admissions-aid/financial-aid-and-scholarships/scholarships/index.html (sha256 b528050b8594)
- checks: {"thresholds": {"sat_min": 1390}}
  - award_amount_text: $6,000 ⟵ “$6,000 | Silver Scholar | 31-33 | 1390”
  - test_requirement: ACT 31-33 / SAT 1390 ⟵ “$6,000 | Silver Scholar | 31-33 | 1390”
### `5020294378c03d7a` South Dakota School of Mines and Technology — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sdsmt.edu/admissions-aid/financial-aid-and-scholarships/scholarships/index.html (sha256 b528050b8594)
- checks: {"thresholds": {"act_min": 24, "sat_min": 1160}}
  - award_amount_text: $2,000 ⟵ “$2,000 | Hardrock Scholar | 24 | 1160”
  - test_requirement: ACT 24 / SAT 1160 ⟵ “$2,000 | Hardrock Scholar | 24 | 1160”
### `a5c7efcc8471680b` South Dakota School of Mines and Technology — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sdsmt.edu/admissions-aid/financial-aid-and-scholarships/scholarships/index.html (sha256 b528050b8594)
- checks: {"thresholds": {"sat_min": 1300}}
  - award_amount_text: $4,000 ⟵ “$4,000 | Copper Scholar | 28-30 | 1300”
  - test_requirement: ACT 28-30 / SAT 1300 ⟵ “$4,000 | Copper Scholar | 28-30 | 1300”
### `ad12aa4e2301d578` South Dakota School of Mines and Technology — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sdsmt.edu/admissions-aid/financial-aid-and-scholarships/scholarships/index.html (sha256 b528050b8594)
- checks: {"thresholds": {"sat_min": 1200}}
  - award_amount_text: $3,000 ⟵ “$3,000 | Miner Scholar | 25-27 | 1200”
  - test_requirement: ACT 25-27 / SAT 1200 ⟵ “$3,000 | Miner Scholar | 25-27 | 1200”
### `cb27cba315ccc9a1` South Dakota School of Mines and Technology — awards 2027-28 [new] (labeled_in_source)
- source: https://www.sdsmt.edu/admissions-aid/financial-aid-and-scholarships/scholarships/index.html (sha256 b528050b8594)
- checks: {"thresholds": {"sat_min": 1530}}
  - award_amount_text: $12,000 ⟵ “$12,000 | Presidential Scholar | 35-36 | 1530”
  - test_requirement: ACT 35-36 / SAT 1530 ⟵ “$12,000 | Presidential Scholar | 35-36 | 1530”
### `macd527f65b4a1b8` South Dakota School of Mines and Technology — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.sdsmt.edu/admissions-aid/assets/pdf-files/HSDC%20Eligibility%20Exemption%20Form%20W-F%20Grades.pdf (sha256 2d780e697858)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 3, "tiers": 0}
  - eligibility_tier: 3.5 ⟵ “-Earn a cumulative GPA of at least 3.50 on a 4.0 scale;”
  - eligibility_tier: 3.25 ⟵ “-Earn a cumulative GPA of at least 3.25 on a 4.0 scale;”
  - eligibility_tier: 3.0 ⟵ “☐ 3. Student must have received a final grade of “B” or higher in all previous SDBOR HSDC courses OR have a 3.0 cumulative GPA”
  - per_credit_hour_charge: 145 ⟵ “Option 2: A student who cannot show good cause may pay the full HSDC tuition rate for a total cost of $145 per credit hour. If the”
  - per_credit_hour_charge: 145 ⟵ “in HSDC by 1.) successfully repeating the course(s) I earned the “W” or “F” grade in, and 2.) paying the full HSDC tuition rate at $145/credit”
### `3ad941e030511793` South Dakota State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sdstate.edu/office-financial-aid-scholarships/cost-attendance (sha256 daf39aba5930)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees(4): 9780 ⟵ “Tuition and Fees(4) | $9,780 | $11,460 | $13,479 | $11,214”
  - column:Housing and Food: 11024 ⟵ “Housing and Food | $11,024 | $11,024 | $11,024 | $11,024”
  - column:Total Direct Costs: 20804 ⟵ “Total Direct Costs | $20,804 | $22,484 | $24,503 | $22,238”
### `793f8504a80ceb82` South Dakota State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.sdstate.edu/office-financial-aid-scholarships/cost-attendance (sha256 daf39aba5930)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - on_campus:Tuition and Fees(4): 13479 ⟵ “Tuition and Fees(4) | $9,780 | $11,460 | $13,479 | $11,214”
  - on_campus:Housing and Food: 11024 ⟵ “Housing and Food | $11,024 | $11,024 | $11,024 | $11,024”
  - on_campus:Total Direct Costs: 24503 ⟵ “Total Direct Costs | $20,804 | $22,484 | $24,503 | $22,238”
### `a73db533d87c7801` Southeast Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.southeasttech.edu/student-life/registrars-office/clep-testing.php (sha256 b41075d48b45)
- checks: {"distinct_exams": 13, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PSYC 101 | 50 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SOC 150 | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | ECON 202 | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | ECON 201 | 50 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | ENGL 101 | 50 | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | MATH 114 | 50 | 3”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | Highest math class required for program | 50 | 3-5”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | MATH 116 | 50 | 5”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | BIO 101/101L | 50 | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | CHEM 106/106L | 50 | 4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | BUS 140 | 50 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | MKT 120 | 50 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language Level I | SPAN 103 | 50 | 3”
### `47c25e507edbc682` Southeast Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.southeasttech.edu/apply/transfer-students.php (sha256 1529524d2e47)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Acceptance of transfer credits is contingent upon the student having completed the course or courses with a grade of “C” or better, and, in the Registrar's judgment, the course credit and content is similar to that contained in the Southeast Tech course.”
### `f7fbcc4e59e53bd6` University of South Dakota — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance (sha256 21a579b75950)
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition & Fees: 13616 ⟵ “Tuition & Fees | 9916 | 11457 | 13616”
  - on_campus:Course/Discipline Fees*: 510 ⟵ “Course/Discipline Fees* | 510 | 510 | 510”
  - on_campus:Housing & Food: 11238 ⟵ “Housing & Food | 11238 | 11238 | 11238”
  - on_campus:Direct Costs Total: 25364 ⟵ “Direct Costs Total | 21664 | 23205 | 25364”
  - on_campus:Books, Course Materials, Supplies & Equipment: 800 ⟵ “Books, Course Materials, Supplies & Equipment | 800 | 800 | 800”
  - on_campus:Personal Expenses: 2424 ⟵ “Personal Expenses | 2424 | 2424 | 2424”
  - on_campus:Transportation Expenses: 1914 ⟵ “Transportation Expenses | 1914 | 1914 | 1914”
  - on_campus:Loan Fees: 68 ⟵ “Loan Fees | 68 | 68 | 68”
  - on_campus:Indirect Costs Total: 5206 ⟵ “Indirect Costs Total | 5206 | 5206 | 5206”
  - on_campus:Total Annual Cost of Attendance Estimate: 30570 ⟵ “Total Annual Cost of Attendance Estimate | 26870 | 28411 | 30570”
### `cf73a91693ce99d3` University of South Dakota — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.usd.edu/Academics/Dual-Credit (sha256 cc5591683cf5)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 2}
  - eligibility_tier: 3.5 ⟵ “High School cumulative unweighted GPA 3.50+”
  - eligibility_tier: 3.25 ⟵ “High School cumulative unweighted GPA 3.25+”
  - per_credit_hour_charge: 156.96 ⟵ “If students wish to continue taking dual credit but do not have an approved Academic Suspension Waiver, they may take Dual Credit or Concurrent Credit while paying “full dual credit tuition” ($156.96 per credit hour) during the suspended term.”
  - per_credit_hour_charge: 156.96 ⟵ “If the petition is approved, students can continue taking dual credit as normal. If the petition is denied, students can retake the F/W course at full dual credit tuition: $156.96 per credit”
  - per_credit_hour_charge: 78.48 ⟵ “Dual credit courses cost an average of $78.48 per credit hour – compared to about $300 for non-high school students currently attending USD.”
### `8526391ab09f16bb` University of South Dakota — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Undergraduate-Admissions/Transfer-Students (sha256 1e08da707289)
- checks: {"fields": ["max_transfer_credits", "residency_requirement_credits"]}
  - max_transfer_credits: 60 ⟵ “A maximum of 60 semester hours of transfer credit from a two-year college may apply toward graduation, and may not exceed one-half of the total semester hours required for completion of your USD degree.”
  - residency_requirement_credits: 15 ⟵ “Click to Open Transferring Credit: The Basics To receive a bachelor's degree from the University of South Dakota, you must complete a minimum of 30 hours of USD credit, including at least 15 of the final 30 hours completed immediately prior to the degree.”
### `947220ae356fae2c` Western Dakota Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.wdt.edu/future-students/dual-enrollment/ (sha256 8cf918f9701c)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 80.37 ⟵ “The State of South Dakota allows Juniors and Seniors in South Dakota High Schools to take college courses with WDTC for $80.37 per credit hour.  For payment information and due dates visit our Student Accounts Office page. Payment for Dual Enrollment courses are due before the start of the semester.”
### `d1c275baced94b30` Western Dakota Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.wdt.edu/future-students/transfer-of-credit/ (sha256 3d6307479b65)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Apply Now Schedule a Tour Visit Us Request Info Chat Online Transfer of Credit Transferring College Credits to Western Dakota Technical College Postsecondary level credits from an accredited school in which the student has earned a grade of “C” or higher, or its equivalent, will be considered for transfer.”

## Exceptions (84)

### `6de042ae77a6b344` state-SD — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://tdx.sdbor.edu/TDClient/33/Portal/Requests/ServiceCatalog/Category/44/Our-Dakota-Dreams (sha256 914866e1d47f)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “The purpose of this form is to provide reduced tuition for eligible stakeholders under South Dakota Codified Law.”
### `e0c6d3048babe227` state-SD — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://tdx.sdbor.edu/TDClient/33/Portal/Requests/Service/110/High-School-Dual-Enrollment-Support (sha256 f45fe823ca7c)
- issues: semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Current category: Watch a short how-to video that will guide you in creating a new account Dynamic Forms: Logging into the Dashboard and Dashboard Navigation Watch a short how-to video to log into your dashboard and navigate the various views of the dashboard -- submitted applications (Forms History”
### `1f14f5e7d04ece07` Augustana University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augie.edu/admission-aid/financial-aid-costs-scholarships/office-financial-aid/general-policies-relating (sha256 dcfe2d176d9b)
- issues: semantic_review_required, conflicting_sources:https://www.augie.edu/admission-aid/financial-aid-costs-scholarships/office-financial-aid/financial-aid-forms,https://www.augie.edu/admission/financing-your-education/forms,https://www.augie.edu/sites/default/files/documents/2025-11/SpecialCircumstanceForm2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Families may request an appeal of the financial aid award in the event of unusual circumstances, which may include, but are not limited to: income reduction, unemployment of a wage-earner, unusually high medical costs, divorce, natural disaster, or others.”
  - sentence: need_based_special_circumstances ⟵ “The Special Circumstances Form is available online — choose either the Dependent or Independent form, depending on your status.”
### `27b6aed4a2b562b4` Augustana University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.augie.edu/admission-aid/financial-aid-costs-scholarships/office-financial-aid/financial-aid-forms (sha256 b26d7b659f9d)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.augie.edu/admission-aid/financial-aid-costs-scholarships/office-financial-aid/general-policies-relating,https://www.augie.edu/admission/financing-your-education/forms,https://www.augie.edu/sites/default/files/documents/2025-11/SpecialCircumstanceForm2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have questions or experience problems accessing these forms, contact the Office of Financial Aid: Application for Admission and Scholarships Parent PLUS Loan Application Private Loan Self-Certification Form Special Circumstance Form 2026-27 Special Circumstance Form 2025-26 Summer Financial Aid Application FAFSA Verification W-4 Form Contact Us 605.274.5216 Office of Financial Aid Email | 2”
### `3c84372a01c5f172` Augustana University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.augie.edu/admission/financing-your-education/forms (sha256 813b69eb816d)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.augie.edu/admission-aid/financial-aid-costs-scholarships/office-financial-aid/financial-aid-forms,https://www.augie.edu/admission-aid/financial-aid-costs-scholarships/office-financial-aid/general-policies-relating,https://www.augie.edu/sites/default/files/documents/2025-11/SpecialCircumstanceForm2026-27.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have questions or experience problems accessing these forms, contact the Office of Financial Aid: Application for Admission and Scholarships Parent PLUS Loan Application Private Loan Self-Certification Form Special Circumstance Form 2026-27 Special Circumstance Form 2025-26 Summer Financial Aid Application FAFSA Verification W-4 Form Contact Us 605.274.5216 Office of Financial Aid Email | 2”
### `7a8ffd001a64738f` Augustana University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.augie.edu/sites/default/files/documents/2025-11/SpecialCircumstanceForm2026-27.pdf (sha256 326fb2551eba)
- issues: semantic_review_required, conflicting_sources:https://www.augie.edu/admission-aid/financial-aid-costs-scholarships/office-financial-aid/financial-aid-forms,https://www.augie.edu/admission-aid/financial-aid-costs-scholarships/office-financial-aid/general-policies-relating,https://www.augie.edu/admission/financing-your-education/forms
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Form 2026-2027 Student Name: _______________________________________ ID# ______________________ Email: _______________________________ Parent Email: _____________________________ Student Phone #: ______________________ Parent Phone #: ___________________________ Augustana University strives to support our students and families with the best financial aid package possible.”
  - sentence: need_based_special_circumstances ⟵ “We realize that the FAFSA may not capture the current financial situation of your household and that certain special circumstances may be a factor in your ability to pay.”
  - sentence: need_based_special_circumstances ⟵ “By completing the special circumstance form and providing required documentation, you are asking us to review your financial aid for the 2026-27 academic year.”
  - sentence: need_based_special_circumstances ⟵ “The student must have filed the 2026-27 FAFSA to be considered for special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Any pending verification must be completed before a review of special circumstances will occur. 2.”
  - sentence: need_based_special_circumstances ⟵ “Further, we understand that special circumstances are applied on a year to year basis and adjustments do not automatically apply to future academic years. ➢ I/We understand that completing this form does not release the student from the obligation of staying current with the Augustana University Business Office.”
### `afbaa837774368d4` Augustana University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.augie.edu/sites/default/files/documents/2024-10/SpecialCircumstanceForm2025-26.pdf (sha256 fcab2d96387f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Form 2025-2026 Student Name: _______________________________________ ID# ______________________ Email: _______________________________ Parent Email: _____________________________ Student Phone #: ______________________ Parent Phone #: ___________________________ Augustana University strives to support our students and families with the best financial aid package possible.”
  - sentence: need_based_special_circumstances ⟵ “We realize that the FAFSA may not capture the current financial situation of your household and that certain special circumstances may be a factor in your ability to pay.”
  - sentence: need_based_special_circumstances ⟵ “By completing the special circumstance form and providing required documentation, you are asking us to review your financial aid for the 2025-26 academic year.”
  - sentence: need_based_special_circumstances ⟵ “The student must have filed the 2025-26 FAFSA to be considered for special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Any pending verification must be completed before a review of special circumstances will occur. 2.”
  - sentence: need_based_special_circumstances ⟵ “Further, we understand that special circumstances are applied on a year to year basis and adjustments do not automatically apply to future academic years. ➢ I/We understand that completing this form does not release the student from the obligation of staying current with the Augustana University Business Office.”
### `c7efbc0c82816d6c` Augustana University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.augie.edu/admission-financial-aid/financial-aid-costs-scholarships/office-financial-aid/satisfactory-academic (sha256 ce1faa1e676d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Summit Ave Sioux Falls, SD 57197 financial.aid@augie.edu Fax: 605.274.5295 Students may also submit their appeal by filling out the Satisfactory Academic Progress (SAP) Appeal Form.”
### `37454e7595c7d93c` Augustana University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.augie.edu/sites/default/files/documents/2026-02/AugustanaDPTCCostSummary02.04.2026.pdf (sha256 512df47a58c8)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 2, "components_reconcile": false, "rows": 1}
  - column:Total Direct Costs: 107000 ⟵ “Total Direct Costs | $107,000”
  - column:Tuition (effective Spring 2027): 103000 ⟵ “Tuition (effective Spring 2027) | $51,500 per year | $103,000”
  - column:Augustana General Graduate Fee: 4000 ⟵ “Augustana General Graduate Fee | $2,000 per year | $4,000”
  - column:APTA Student Membership: 160 ⟵ “APTA Student Membership | $80 per year | $160”
  - column:AHA BLS Certification: 126 ⟵ “AHA BLS Certification | Every two years | $126”
  - column:DPT Lab Kit: 375 ⟵ “DPT Lab Kit | One-time | $375”
  - column:White Coat: 0 ⟵ “White Coat | Provided by program | $0”
  - column:Required Digital Textbooks: 3720 ⟵ “Required Digital Textbooks | Program-required | $3,720”
  - column:Student Health Insurance: 4378 ⟵ “Student Health Insurance | $2,189 per year | $4,378”
### `757de71993b41418` Black Hills State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.bhsu.edu/admissions/financial-aid/index.html (sha256 1834d0ebe5c7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Education Record Release Form Directory Information Opt-Out Student Directory Information Policy Annual Disclosure Academic Probation and Suspension Information Financial Aid Financial Aid Satisfactory Academic Progress Standards Academic Information and Appeals Form Students attending BHSU (and all other state universities in South Dakota) are required to meet minimum progression standards and ma”
### `e4d1f504a823a43e` Black Hills State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.bhsu.edu/admissions/financial-aid/index.html (sha256 1834d0ebe5c7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Our contact information is: Phone: 605.642.6145 Email: BHSUfinancial@BHSU.edu Financial Aid Forms Introduction Consortium Agreeement Financial Aid Suspension Appeal Form ISIR Print Request Form Special Circumstances Form Summer Aid Request TEACH Grant Certification Form Total and Permanent Disability Discharge (TPD) Unusual Circumstances (Dependency) Form Family Educational Rights and Privacy Act ”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances refer to the financial situations that justify an aid administrator adjusting data elements in the Cost of Attendance or in the Student Aid Index calculation.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances appeals are not an appeal for more aid, but instead demonstrate a change in circumstances from the FAFSA income and family reporting.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation, also known as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “In most cases, unusual circumstances renew from year to year and do not require students to reapply each academic year.”
### `cad114c4edeabba3` Black Hills State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bhsu.edu/admissions/tuition-fees.html (sha256 cec2333b72ce)
- issues: residency_names_another_state, residency_unknown
- checks: {"columns": 1, "rows": 10}
  - column:Tuition: 7234 ⟵ “Tuition | $7,234”
  - column:General Activity Fees: 482 ⟵ “General Activity Fees | $482”
  - column:Food and Housing: 11322 ⟵ “Food and Housing | $11,322”
  - column:Books and Supplies: 230 ⟵ “Books and Supplies | $230”
  - column:Program Fee: 156 ⟵ “Program Fee | $156”
  - column:Certification/License Test Fee: 362 ⟵ “Certification/License Test Fee | $362”
  - column:Loan Fee: 150 ⟵ “Loan Fee | $150”
  - column:Miscellaneous: 2378 ⟵ “Miscellaneous | $2,378”
  - column:Transportation: 1876 ⟵ “Transportation | $1,876”
  - column:Annual Estimated Total: 24190 ⟵ “Annual Estimated Total | $24,190”
### `3b65c29ae1e4fabd` Dakota State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://dsu.edu/admissions/undergraduate/cost-aid/undergraduate-financial-aid-guide.html (sha256 ce0ebd8e9554)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “What if a change occurs that alters my FAFSA application information, or if I have special circumstances?”
  - sentence: need_based_special_circumstances ⟵ “Sometimes, due to special circumstances, the application process does not reflect your family’s real ability to contribute to your educational expenses.”
  - sentence: need_based_special_circumstances ⟵ “Do not make corrections to your FAFSA based upon your special circumstances.”
### `7b4cadbb8aba37dd` Dakota State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://dsu.edu/admissions/undergraduate/cost-aid/undergraduate-financial-aid-guide.html (sha256 ce0ebd8e9554)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Based on your documented information, the DSU Financial Aid Director may be able to use "professional judgement" and review your situation on an individual basis.”
### `add483946c3b2943` Dakota State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://dsu.edu/admissions/undergraduate/cost-aid/undergraduate-financial-aid-guide.html (sha256 ce0ebd8e9554)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Students with dependent care costs or disability expenses should contact the Office of Financial Aid for a budget adjustment. *Double residence hall room and minimum meal plan used. **This tuition rate is equal to 150% of the resident rate, and applies to non-resident students.”
### `101d66b9020150df` Dakota State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://dsu.edu/admissions/undergraduate/cost-aid/tuition-fees.html (sha256 3fa0489a9444)
- issues: conflicting_sources:https://dsu.edu/admissions/undergraduate/cost-aid/undergraduate-financial-aid-guide.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - on_campus:Undergraduate Tuition & Fees: 6284.25 ⟵ “Undergraduate Tuition & Fees | $4,650.00 | $5,314.50 | $6,284.25”
  - on_campus:Wireless Computing Fee: 435.35 ⟵ “Wireless Computing Fee | $435.35 | $435.35 | $435.35”
  - on_campus:Housing & Food Service***: 4373.0 ⟵ “Housing & Food Service*** | $4,373.00 | $4,373.00 | $4,373.00”
  - on_campus:Est. Cost Per Semester: 11092.6 ⟵ “Est. Cost Per Semester | $9,458.35 | $10,122.85 | $11,092.60”
  - on_campus:Est. Total Cost Per Year: 22185.2 ⟵ “Est. Total Cost Per Year | $18,916.70 | $20,245.70 | $22,185.20”
### `5390f944fca0315b` Dakota State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://dsu.edu/admissions/cost-of-attendance.html (sha256 f502a36f5185)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://dsu.edu/admissions/files/tuition-and-fees.pdf,https://dsu.edu/admissions/undergraduate/cost-aid/tuition-fees.html
- checks: {"columns": 1, "rows": 4}
  - column:Tuition & Fees: 10630 ⟵ “Tuition & Fees | $9,301 | $10,630 | $12,569”
  - column:Books, Course Materials, Supplies, and Equipment(Includes Wireless Computing Fee): 1671 ⟵ “Books, Course Materials, Supplies, and Equipment(Includes Wireless Computing Fee) | $1,671 | $1,671 | $1,671”
  - column:On-Campus Housing & Food Service: 10042 ⟵ “On-Campus Housing & Food Service | $10,042 | $10,042 | $10,042”
  - column:Est. Yearly Total: 22343 ⟵ “Est. Yearly Total | $21,014 | $22,343 | $24,282”
### `61955fa6aa2c132d` Dakota State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://dsu.edu/admissions/undergraduate/cost-aid/tuition-fees.html (sha256 3fa0489a9444)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://dsu.edu/admissions/cost-of-attendance.html,https://dsu.edu/admissions/files/tuition-and-fees.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - on_campus:Undergraduate Tuition & Fees: 5314.5 ⟵ “Undergraduate Tuition & Fees | $4,650.00 | $5,314.50 | $6,284.25”
  - on_campus:Wireless Computing Fee: 435.35 ⟵ “Wireless Computing Fee | $435.35 | $435.35 | $435.35”
  - on_campus:Housing & Food Service***: 4373.0 ⟵ “Housing & Food Service*** | $4,373.00 | $4,373.00 | $4,373.00”
  - on_campus:Est. Cost Per Semester: 10122.85 ⟵ “Est. Cost Per Semester | $9,458.35 | $10,122.85 | $11,092.60”
  - on_campus:Est. Total Cost Per Year: 20245.7 ⟵ “Est. Total Cost Per Year | $18,916.70 | $20,245.70 | $22,185.20”
### `76f65720e4779910` Dakota State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://dsu.edu/admissions/cost-of-attendance.html (sha256 f502a36f5185)
- issues: arrangement_unlabeled, conflicting_sources:https://dsu.edu/admissions/undergraduate/cost-aid/tuition-fees.html,https://dsu.edu/admissions/undergraduate/cost-aid/undergraduate-financial-aid-guide.html
- checks: {"columns": 2, "rows": 4}
  - column:Tuition & Fees: 9301 ⟵ “Tuition & Fees | $9,301 | $10,630 | $12,569”
  - column:Books, Course Materials, Supplies, and Equipment(Includes Wireless Computing Fee): 1671 ⟵ “Books, Course Materials, Supplies, and Equipment(Includes Wireless Computing Fee) | $1,671 | $1,671 | $1,671”
  - column:On-Campus Housing & Food Service: 10042 ⟵ “On-Campus Housing & Food Service | $10,042 | $10,042 | $10,042”
  - column:Est. Yearly Total: 21014 ⟵ “Est. Yearly Total | $21,014 | $22,343 | $24,282”
  - column:Tuition & Fees: 12569 ⟵ “Tuition & Fees | $9,301 | $10,630 | $12,569”
  - column:Books, Course Materials, Supplies, and Equipment(Includes Wireless Computing Fee): 1671 ⟵ “Books, Course Materials, Supplies, and Equipment(Includes Wireless Computing Fee) | $1,671 | $1,671 | $1,671”
  - column:On-Campus Housing & Food Service: 10042 ⟵ “On-Campus Housing & Food Service | $10,042 | $10,042 | $10,042”
  - column:Est. Yearly Total: 24282 ⟵ “Est. Yearly Total | $21,014 | $22,343 | $24,282”
### `7c6825738b093a2c` Dakota State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://dsu.edu/admissions/undergraduate/cost-aid/tuition-fees.html (sha256 3fa0489a9444)
- issues: conflicting_sources:https://dsu.edu/admissions/cost-of-attendance.html,https://dsu.edu/admissions/undergraduate/cost-aid/undergraduate-financial-aid-guide.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - on_campus:Undergraduate Tuition & Fees: 4650.0 ⟵ “Undergraduate Tuition & Fees | $4,650.00 | $5,314.50 | $6,284.25”
  - on_campus:Wireless Computing Fee: 435.35 ⟵ “Wireless Computing Fee | $435.35 | $435.35 | $435.35”
  - on_campus:Housing & Food Service***: 4373.0 ⟵ “Housing & Food Service*** | $4,373.00 | $4,373.00 | $4,373.00”
  - on_campus:Est. Cost Per Semester: 9458.35 ⟵ “Est. Cost Per Semester | $9,458.35 | $10,122.85 | $11,092.60”
  - on_campus:Est. Total Cost Per Year: 18916.7 ⟵ “Est. Total Cost Per Year | $18,916.70 | $20,245.70 | $22,185.20”
### `803fac344ac985ea` Dakota State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://dsu.edu/admissions/undergraduate/cost-aid/undergraduate-financial-aid-guide.html (sha256 ce0ebd8e9554)
- issues: conflicting_sources:https://dsu.edu/admissions/cost-of-attendance.html,https://dsu.edu/admissions/undergraduate/cost-aid/tuition-fees.html
- checks: {"columns": 1, "rows": 3}
  - column:Undergraduate Tuition & Fees: 9938 ⟵ “Undergraduate Tuition & Fees | $9,938 | $13,130”
  - column:On Campus Food & Housing*: 8506 ⟵ “On Campus Food & Housing* | $8,506 | $8,506”
  - column:Est. Direct Educatin Cost: 18444 ⟵ “Est. Direct Educatin Cost | $18,444 | $21,636”
### `d377d90e3ab69121` Dakota State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://dsu.edu/admissions/undergraduate/cost-aid/undergraduate-financial-aid-guide.html (sha256 ce0ebd8e9554)
- issues: conflicting_sources:https://dsu.edu/admissions/undergraduate/cost-aid/tuition-fees.html
- checks: {"columns": 1, "rows": 3}
  - on_campus:Undergraduate Tuition & Fees: 13130 ⟵ “Undergraduate Tuition & Fees | $9,938 | $13,130”
  - on_campus:On Campus Food & Housing*: 8506 ⟵ “On Campus Food & Housing* | $8,506 | $8,506”
  - on_campus:Est. Direct Educatin Cost: 21636 ⟵ “Est. Direct Educatin Cost | $18,444 | $21,636”
### `ec788d261180d719` Dakota State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://dsu.edu/admissions/files/tuition-and-fees.pdf (sha256 c5e66cd695cd)
- issues: arrangement_unlabeled, components_do_not_reconcile, implausible_amount, residency_unknown, conflicting_sources:https://dsu.edu/admissions/cost-of-attendance.html,https://dsu.edu/admissions/undergraduate/cost-aid/tuition-fees.html
- checks: {"columns": 12, "components_reconcile": false, "rows": 34}
  - column:TUITION: 267.45 ⟵ “TUITION | $ 267.45 | $ 311.75 | $ 376.40 | Math | $17.55”
  - column:FEES: 42.55 ⟵ “FEES | $ 42.55 | $ 42.55 | $ 42.55 | Art, Music, & Theatre | $17.00”
  - column:Science: BIOL & CHEM: 23.35 ⟵ “Science: BIOL & CHEM | $23.35”
  - column:TOTAL: 310.0 ⟵ “TOTAL | $ 310.00 | $ 354.30 | $ 418.95”
  - column:Science: PHYS, GEOG, ASC: 22.1 ⟵ “Science: PHYS, GEOG, ASC | $22.10”
  - column:Physics and Other Sciences: 22.7 ⟵ “Physics and Other Sciences | $22.70”
  - column:Wireless Computing Fee: 435.35 ⟵ “Wireless Computing Fee | $ 435.35”
  - column:1: 310.0 ⟵ “1 | $310.00 | $354.30 | $418.95 | RESIDENCE HALLS”
  - column:Double Occupancy: 2498.0 ⟵ “Double Occupancy | $2,498.00”
  - column:2: 620.0 ⟵ “2 | $620.00 | $708.60 | $837.90”
  - column:Single Occupancy: 3128.0 ⟵ “Single Occupancy | $3,128.00”
  - column:3: 930.0 ⟵ “3 | $930.00 | $1,062.90 | $1,256.85”
  - column:Double Occupancy-Higbie Hall: 2198.0 ⟵ “Double Occupancy-Higbie Hall | $2,198.00”
  - column:4: 1240.0 ⟵ “4 | $1,240.00 | $1,417.20 | $1,675.80”
  - column:Single Occupancy-Higbie Hall: 2828.0 ⟵ “Single Occupancy-Higbie Hall | $2,828.00”
  - column:5: 1550.0 ⟵ “5 | $1,550.00 | $1,771.50 | $2,094.75 | Apartments Double | $3,023.00”
  - column:6: 1860.0 ⟵ “6 | $1,860.00 | $2,125.80 | $2,513.70 | Apartments Single | $3,416.00”
  - column:7: 2170.0 ⟵ “7 | $2,170.00 | $2,480.10 | $2,932.65 | Courtyard Double | $2,635.00”
  - column:8: 2480.0 ⟵ “8 | $2,480.00 | $2,834.40 | $3,351.60 | Courtyard Single | $3,264.00”
  - column:9: 2790.0 ⟵ “9 | $2,790.00 | $3,188.70 | $3,770.55 | Courtyard Suite Double | $2,937.00”
  - column:10: 3100.0 ⟵ “10 | $3,100.00 | $3,543.00 | $4,189.50 | Courtyard Suite Single | $3,313.00”
  - column:11: 3410.0 ⟵ “11 | $3,410.00 | $3,897.30 | $4,608.45 | Residence Village Suite | $3,387.00”
  - column:Residence Village Apartment: 3630.0 ⟵ “Residence Village Apartment | $3,630.00”
  - column:12: 3720.0 ⟵ “12 | $3,720.00 | $4,251.60 | $5,027.40”
  - column:13: 4030.0 ⟵ “13 | $4,030.00 | $4,605.90 | $5,446.35 | MEAL PLANS”
  - … 85 more rows
### `06bf69f79bd1e3f4` Lake Area Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lakeareatech.edu/wp-content/uploads/2026/06/LATC-26-27-Program-Cost-Sheets.pdf (sha256 def6536b8d86)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 9, "rows": 841}
  - column:Credits: 18 ⟵ “Credits | 18 | 19 | 17 | 16”
  - column:Tuition: 2412 ⟵ “Tuition | $2,412 | $2,546 | $2,278 | $2,144”
  - column:State Fees: 810 ⟵ “State Fees | 810 | 855 | 765 | 720”
  - column:Departmental Fee: 629 ⟵ “Departmental Fee | 629 | 629 | 629 | 629”
  - column:Campus Support Fee: 558 ⟵ “Campus Support Fee | 558 | 589 | 527 | 496”
  - column:Uniform Fee: 25 ⟵ “Uniform Fee | 25 | 25 | 25 | 25”
  - column:Total: 4434 ⟵ “Total | $4,434 | $4,644 | $4,224 | $4,014”
  - column:Books: 600 ⟵ “Books | 600 | 500”
  - column:^Laptop: 1190 ⟵ “^Laptop | 1,190”
  - column:Annual Cost: 10868 ⟵ “Annual Cost | $10,868 | $8,738”
  - column:Program Cost: 19606 ⟵ “Program Cost | $19,606”
  - column:living off campus: 9450 ⟵ “living off campus | $9,450 | $1,580 | $2,360 | $13,390”
  - column:living with parent: 5670 ⟵ “living with parent | $5,670 | $1,580 | $2,360 | $9,610”
  - column:living off campus (2): 13990 ⟵ “living off campus | $13,990 | $2,940 | $2,550 | $19,480”
  - column:living with parent (2): 5670 ⟵ “living with parent | $5,670 | $1,580 | $2,360 | $9,610”
  - column:Credits (2): 19 ⟵ “Credits | 19 | 17 | 18 | 19”
  - column:Tuition (2): 2546 ⟵ “Tuition | $2,546 | $2,278 | $2,412 | $2,546”
  - column:State Fees (2): 855 ⟵ “State Fees | 855 | 765 | 810 | 855”
  - column:Departmental Fee (2): 629 ⟵ “Departmental Fee | 629 | 629 | 629 | 629”
  - column:Campus Support Fee (2): 589 ⟵ “Campus Support Fee | 589 | 527 | 558 | 589”
  - column:Uniform Fee (2): 25 ⟵ “Uniform Fee | 25 | 25 | 25 | 25”
  - column:Total (2): 4644 ⟵ “Total | $4,644 | $4,224 | $4,434 | $4,644”
  - column:Books (2): 600 ⟵ “Books | 600 | 500”
  - column:^Laptop (2): 1190 ⟵ “^Laptop | 1,190”
  - column:Annual Cost (2): 10658 ⟵ “Annual Cost | $10,658 | $9,578”
  - … 2764 more rows
### `a0e587dba4aef0c5` Mitchell Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.mitchelltech.edu/academics/grading (sha256 e43b2bd3b230)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “See Satisfactory Academic Progress; Financial Aid Warning, Financial Aid Suspension, and Appeal Process in the Paying for School section.”
### `d5aed3eb99c3754c` Mitchell Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.mitchelltech.edu/admissions/financial-aid/ (sha256 f0e3f942851a)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: need_based_special_circumstances ⟵ “Appeal Process: Federal regulations limit circumstances for which a suspension of financial aid may be appealed to the following: death of a family member; illness or injury to the student; or other special circumstances beyond the student’s control.”
  - sentence: need_based_special_circumstances ⟵ “Other special circumstance (a detailed explanation of the specific traumatic event or unexpected circumstance and what you have done to overcome the event or circumstance such that you can go on to meet the standard of Satisfactory Academic Progress AND supporting documentation from a third party, i.e. physician, social worker, counselor, police).”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The federal government makes every effort to capture the family’s financial situation using the Free Application for Federal Student Aid (FAFSA®); however, some families may be experiencing a hardship or unusual circumstance that is not reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “We understand that there may be special circumstances that may have changed since you completed the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “The following are examples of additional special circumstances we may review on a case-by-case basis to determine if they change the student’s eligibility for aid.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances (Dependency Override Appeals) If a student is considered dependent based on the criteria on the FAFSA, the student is required to provide parental information.”
### `dc2f1993ddf65544` Mitchell Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.mitchelltech.edu/admissions/tuition-fees/ (sha256 74e81322ce8c)
- issues: implausible_amount, residency_unknown
- checks: {"columns": 1, "rows": 4}
  - column:Tuition: 130 ⟵ “Tuition | $130 | Supports all aspects of education and services”
  - column:State Facility Fee: 36 ⟵ “State Facility Fee | $36 | Covers debt service for building construction”
  - column:State M&R Fee: 8 ⟵ “State M&R Fee | $8 | Funds the upkeep of campus land and facilities”
  - column:Institutional Fee: 34 ⟵ “Institutional Fee | $34 | Technology, student services, and activities”
### `b5e935a84cfe3e78` Mitchell Technical College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.mitchelltech.edu/programs/dual-credit-classes/ (sha256 752be59a7ec3)
- issues: stale_year_label:2025-26
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 80.37 ⟵ “Classes are offered at a reduced rate of $80.37/credit hour (for in-state students) making this an affordable option to get started on their postsecondary career plans while they are still in high school.”
  - per_credit_hour_charge: 80.37 ⟵ “The cost of Mitchell Tech dual credit classes is $80.37/credit hour (3-credit class cost is $241.11). Out-of-state dual credit rate is $160.74/credit hour.”
  - per_credit_hour_charge: 160.74 ⟵ “The cost of Mitchell Tech dual credit classes is $80.37/credit hour (3-credit class cost is $241.11). Out-of-state dual credit rate is $160.74/credit hour.”
### `2944ea92d1b24191` Mount Marty University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mountmarty.edu/tuition-and-aid/financing-your-education/financial-aid-policies/ (sha256 41edbb4600fd)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: professional_judgment ⟵ “Professional Judgment The Director of Financial Assistance may use professional judgment on a case-by-case basis for students with special circumstances.”
  - sentence: professional_judgment ⟵ “Professional judgment is used to take into consideration factors which have not been reflected on a Free Application for Federal Student Aid (FAFSA).”
  - sentence: professional_judgment ⟵ “The professional judgment may either increase or decrease data elements used to calculate a student's Expected Family Contribution (EFC).”
  - sentence: professional_judgment ⟵ “No professional judgment will be approved unless adequate information is provided.”
  - sentence: professional_judgment ⟵ “Circumstances which are brought before the director will be analyzed on a case-by-case basis to see if a professional judgment is warranted.”
  - sentence: professional_judgment ⟵ “The Director may use professional judgment to override a student's dependency status if unusual circumstances justify such an action.”
### `b28875ccda12647a` Mount Marty University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mountmarty.edu/tuition-and-aid/costs/watertown-undergraduate-programs/ (sha256 42c55ffd2f29)
- issues: multiple_total_rows, conflicting_sources:https://www.mountmarty.edu/tuition-and-aid/costs/yankton-undergraduate-programs/
- checks: {"columns": 2, "rows": 9}
  - off_campus_not_with_family:Tuition: 10185 ⟵ “Tuition | $10,185 | $10,185”
  - off_campus_not_with_family:Fees: 2500 ⟵ “Fees | $2,500 | $2,500”
  - off_campus_not_with_family:Total Direct Costs: 12685 ⟵ “Total Direct Costs | $12,685 | $12,685”
  - off_campus_not_with_family:Housing & Food: 10600 ⟵ “Housing & Food | $10,600 | $2,011”
  - off_campus_not_with_family:Personal: 2507 ⟵ “Personal | $2,507 | $1,878”
  - off_campus_not_with_family:Transportation: 2918 ⟵ “Transportation | $2,918 | $2,918”
  - off_campus_not_with_family:Books & Supplies: 1236 ⟵ “Books & Supplies | $1,236 | $1,236”
  - off_campus_not_with_family:Loan Fees: 72 ⟵ “Loan Fees | $72 | $72”
  - off_campus_not_with_family:Total Indirect Costs: 17333 ⟵ “Total Indirect Costs | $17,333 | $8,115”
  - with_parents_or_family:Tuition: 10185 ⟵ “Tuition | $10,185 | $10,185”
  - with_parents_or_family:Fees: 2500 ⟵ “Fees | $2,500 | $2,500”
  - with_parents_or_family:Total Direct Costs: 12685 ⟵ “Total Direct Costs | $12,685 | $12,685”
  - with_parents_or_family:Housing & Food: 2011 ⟵ “Housing & Food | $10,600 | $2,011”
  - with_parents_or_family:Personal: 1878 ⟵ “Personal | $2,507 | $1,878”
  - with_parents_or_family:Transportation: 2918 ⟵ “Transportation | $2,918 | $2,918”
  - with_parents_or_family:Books & Supplies: 1236 ⟵ “Books & Supplies | $1,236 | $1,236”
  - with_parents_or_family:Loan Fees: 72 ⟵ “Loan Fees | $72 | $72”
  - with_parents_or_family:Total Indirect Costs: 8115 ⟵ “Total Indirect Costs | $17,333 | $8,115”
### `ec126e5bdd349d62` Mount Marty University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mountmarty.edu/tuition-and-aid/costs/yankton-undergraduate-programs/ (sha256 00696f4facfe)
- issues: conflicting_sources:https://www.mountmarty.edu/tuition-and-aid/costs/watertown-undergraduate-programs/
- checks: {"columns": 3, "components_reconcile": true, "rows": 11}
  - on_campus:Tuition: 34250 ⟵ “Tuition | $34,250 | $34,250 | $34,250”
  - on_campus:Program Support Fee: 3250 ⟵ “Program Support Fee | $3,250 | $3,250 | $3,250”
  - on_campus:Housing & Food: 10600 ⟵ “Housing & Food | $10,600 | - | -”
  - on_campus:Student Life Fee: 130 ⟵ “Student Life Fee | $130 | $130 | $130”
  - on_campus:Personal: 2507 ⟵ “Personal | $2,507 | $2,507 | $2,507”
  - on_campus:Transportation: 2918 ⟵ “Transportation | $2,918 | $2,918 | $2,918”
  - on_campus:Books & Supplies: 1200 ⟵ “Books & Supplies | $1,200 | $1,200 | $1,200”
  - on_campus:Loan Fees: 200 ⟵ “Loan Fees | $200 | $200 | $200”
  - on_campus:Total Cost of Attendance for 26-27: 55055 ⟵ “Total Cost of Attendance for 26-27 | $55,055 | $55,055 | $47,188”
  - on_campus:Total Direct Costs: 48230 ⟵ “Total Direct Costs | $48,230 | $37,630 | $37,630”
  - on_campus:Total Indirect Costs: 6825 ⟵ “Total Indirect Costs | $6,825 | $17,425 | $9,558”
  - off_campus_not_with_family:Tuition: 34250 ⟵ “Tuition | $34,250 | $34,250 | $34,250”
  - off_campus_not_with_family:Program Support Fee: 3250 ⟵ “Program Support Fee | $3,250 | $3,250 | $3,250”
  - off_campus_not_with_family:Student Life Fee: 130 ⟵ “Student Life Fee | $130 | $130 | $130”
  - off_campus_not_with_family:Housing & Food: 10600 ⟵ “Housing & Food | - | $10,600 | $2,733”
  - off_campus_not_with_family:Personal: 2507 ⟵ “Personal | $2,507 | $2,507 | $2,507”
  - off_campus_not_with_family:Transportation: 2918 ⟵ “Transportation | $2,918 | $2,918 | $2,918”
  - off_campus_not_with_family:Books & Supplies: 1200 ⟵ “Books & Supplies | $1,200 | $1,200 | $1,200”
  - off_campus_not_with_family:Loan Fees: 200 ⟵ “Loan Fees | $200 | $200 | $200”
  - off_campus_not_with_family:Total Cost of Attendance for 26-27: 55055 ⟵ “Total Cost of Attendance for 26-27 | $55,055 | $55,055 | $47,188”
  - off_campus_not_with_family:Total Direct Costs: 37630 ⟵ “Total Direct Costs | $48,230 | $37,630 | $37,630”
  - off_campus_not_with_family:Total Indirect Costs: 17425 ⟵ “Total Indirect Costs | $6,825 | $17,425 | $9,558”
  - with_parents_or_family:Tuition: 34250 ⟵ “Tuition | $34,250 | $34,250 | $34,250”
  - with_parents_or_family:Program Support Fee: 3250 ⟵ “Program Support Fee | $3,250 | $3,250 | $3,250”
  - with_parents_or_family:Student Life Fee: 130 ⟵ “Student Life Fee | $130 | $130 | $130”
  - … 8 more rows
### `314c4fad19642bfa` Oglala Lakota College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.olc.edu/admissions-aid/financial-aid/financial-aid-appeal/ (sha256 f354c044f83e)
- issues: semantic_review_required, conflicting_sources:https://www.olc.edu/admissions-aid/financial-aid/satisfactory-academic-progress/,https://www.olc.edu/assets/docs/uploads/fin-aid/financial-aid-appeal-form-26.27.pdf,https://www.olc.edu/assets/docs/uploads/financial-aid-appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If the Student decides that they meet the above-mentioned criteria in which they may potentially qualify for a Financial Aid Appeal, they should work with their assigned Counselor at their respective center to complete the following steps: Print and Complete the “Satisfactory Academic Progress Appeal” form with your assigned Counselor.”
### `3ecd13a2ea79d5f5` Oglala Lakota College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.olc.edu/assets/docs/uploads/financial-aid-appeal.pdf (sha256 95be125f5aef)
- issues: semantic_review_required, conflicting_sources:https://www.olc.edu/admissions-aid/financial-aid/financial-aid-appeal/,https://www.olc.edu/admissions-aid/financial-aid/satisfactory-academic-progress/,https://www.olc.edu/assets/docs/uploads/fin-aid/financial-aid-appeal-form-26.27.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “OLC Financial Aid Office SATISFACTORY ACADEMIC PROGRESS APPEAL It is the student’s responsibility to build the case for the Committee to review.”
### `c08679e050a32795` Oglala Lakota College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.olc.edu/admissions-aid/financial-aid/satisfactory-academic-progress/ (sha256 5ba163a7b318)
- issues: semantic_review_required, conflicting_sources:https://www.olc.edu/admissions-aid/financial-aid/financial-aid-appeal/,https://www.olc.edu/assets/docs/uploads/fin-aid/financial-aid-appeal-form-26.27.pdf,https://www.olc.edu/assets/docs/uploads/financial-aid-appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal of Financial Aid Non-Satisfactory Academic Progress Process A student may appeal Non-Satisfactory Progress by completing the Financial Aid Appeal Form and attach supporting documents to the Financial Aid Office by mid-term of the term during which the student is not eligible for financial aid.”
  - sentence: sap_appeal ⟵ “Should students demonstrate improvement in making Satisfactory Academic Progress in the term following appeal, they will remain on Financial Aid Probation for one term.”
  - sentence: sap_appeal ⟵ “If the student cannot demonstrate that they can make Satisfactory Academic Progress in one term and the appeal is approved, they will be required to submit an academic plan.”
### `c2e1eaf016f74687` Oglala Lakota College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.olc.edu/assets/docs/uploads/fin-aid/financial-aid-appeal-form-26.27.pdf (sha256 ed59543e4c12)
- issues: semantic_review_required, conflicting_sources:https://www.olc.edu/admissions-aid/financial-aid/financial-aid-appeal/,https://www.olc.edu/admissions-aid/financial-aid/satisfactory-academic-progress/,https://www.olc.edu/assets/docs/uploads/financial-aid-appeal.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “OLC Financial Aid Office SATISFACTORY ACADEMIC PROGRESS APPEAL As established by the U.S.”
  - sentence: sap_appeal ⟵ “Procedures for submitting an appeal (all applicable forms, statement, etc. required to be considered complete): Complete and Submit Satisfactory Academic Progress Appeal Form with your Academic Counselor at your Center Student must Write a Statement indicating the reason for falling below the minimum SAP rate of 67% and their plan to stay on track to graduate with their declared major, sign and da”
### `d670d17557abd6f3` Oglala Lakota College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.olc.edu/admissions-aid/financial-aid/satisfactory-academic-progress/ (sha256 5ba163a7b318)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Reasons why they did not achieve minimum academic requirements which should include any type of unusual circumstances they may have been experiencing at the time.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances that will be considered but are not limited to include: illness, death in the family, injury, casualty losses due to weather (hurricane, tornado, mud slides, ground subsidence and other natural disasters), fire, theft, acts of God, or terrorism.”
### `c6f27e859d75286a` South Dakota School of Mines and Technology — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sdsmt.edu/admissions-aid/financial-aid-and-scholarships/index.html (sha256 9eef520e4175)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Such situations can be categorized as: Special Circumstances refers to a change in financial situations, such as: -reduction of income due to unemployment, job change, reduced hours, or retirement -one-time income -unusually high or unexpected medical expenses not covered by insurance.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances refers to conditions that justify a financial aid administrator making an adjustment to a student's dependency status based on a unique situation.”
### `d7a74dbd641b84fd` South Dakota School of Mines and Technology — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sdsmt.edu/admissions-aid/tuition-and-fees/undergraduate-tuition-and-fees.html (sha256 6bd47ac13bee)
- issues: arrangement_unlabeled, conflicting_sources:https://www.sdsmt.edu/admissions-aid/tuition-and-fees/assets/2026-27-F-J-Fillable-Financial-Support-Certification_ada.pdf
- checks: {"columns": 3, "rows": 4}
  - column:Tuition and Fees: 12100 ⟵ “Tuition and Fees | $12,100 | $16,400 | $17,000”
  - column:Books and Supplies (Includes laptop program): 1600 ⟵ “Books and Supplies (Includes laptop program) | $1,600 | $1,600 | $1,600”
  - column:Housing and Meals: 9700 ⟵ “Housing and Meals | $ 9,700 | $9,700 | $9,700”
  - column:Estimated Yearly Total: 23400 ⟵ “Estimated Yearly Total | $23,400 | $27,700 | $28,300”
  - column:Tuition and Fees: 16400 ⟵ “Tuition and Fees | $12,100 | $16,400 | $17,000”
  - column:Books and Supplies (Includes laptop program): 1600 ⟵ “Books and Supplies (Includes laptop program) | $1,600 | $1,600 | $1,600”
  - column:Housing and Meals: 9700 ⟵ “Housing and Meals | $ 9,700 | $9,700 | $9,700”
  - column:Estimated Yearly Total: 27700 ⟵ “Estimated Yearly Total | $23,400 | $27,700 | $28,300”
  - on_campus:Tuition and Fees: 17000 ⟵ “Tuition and Fees | $12,100 | $16,400 | $17,000”
  - on_campus:Books and Supplies (Includes laptop program): 1600 ⟵ “Books and Supplies (Includes laptop program) | $1,600 | $1,600 | $1,600”
  - on_campus:Housing and Meals: 9700 ⟵ “Housing and Meals | $ 9,700 | $9,700 | $9,700”
  - on_campus:Estimated Yearly Total: 28300 ⟵ “Estimated Yearly Total | $23,400 | $27,700 | $28,300”
### `d86d242f74d00777` South Dakota School of Mines and Technology — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.sdsmt.edu/admissions-aid/tuition-and-fees/assets/2026-27-F-J-Fillable-Financial-Support-Certification_ada.pdf (sha256 d62dd87cc117)
- issues: arrangement_unlabeled, conflicting_sources:https://www.sdsmt.edu/admissions-aid/tuition-and-fees/undergraduate-tuition-and-fees.html
- checks: {"columns": 4, "components_reconcile": true, "rows": 4}
  - column:Tuition and Fees (9 mo): 18200 ⟵ “Tuition and Fees (9 mo) | $18,200 | $16,520 | $1,340 | $1,450”
  - column:Living Expenses (9 mo)2: 11830 ⟵ “Living Expenses (9 mo)2 | $11,830 | $14,930 | $14,930 | $19,430”
  - column:Other: 700 ⟵ “Other | $700 | $700 | $700 | $800”
  - column:Total Costs (without Dependent): 30730 ⟵ “Total Costs (without Dependent) | $30,730 | $32,150 | $16,970 | $21,680”
  - column:Tuition and Fees (9 mo): 16520 ⟵ “Tuition and Fees (9 mo) | $18,200 | $16,520 | $1,340 | $1,450”
  - column:Living Expenses (9 mo)2: 14930 ⟵ “Living Expenses (9 mo)2 | $11,830 | $14,930 | $14,930 | $19,430”
  - column:Other: 700 ⟵ “Other | $700 | $700 | $700 | $800”
  - column:Total Costs (without Dependent): 32150 ⟵ “Total Costs (without Dependent) | $30,730 | $32,150 | $16,970 | $21,680”
  - column:Tuition and Fees (9 mo): 1340 ⟵ “Tuition and Fees (9 mo) | $18,200 | $16,520 | $1,340 | $1,450”
  - column:Living Expenses (9 mo)2: 14930 ⟵ “Living Expenses (9 mo)2 | $11,830 | $14,930 | $14,930 | $19,430”
  - column:Other: 700 ⟵ “Other | $700 | $700 | $700 | $800”
  - column:Total Costs (without Dependent): 16970 ⟵ “Total Costs (without Dependent) | $30,730 | $32,150 | $16,970 | $21,680”
  - column:Tuition and Fees (9 mo): 1450 ⟵ “Tuition and Fees (9 mo) | $18,200 | $16,520 | $1,340 | $1,450”
  - column:Living Expenses (9 mo)2: 19430 ⟵ “Living Expenses (9 mo)2 | $11,830 | $14,930 | $14,930 | $19,430”
  - column:Other: 800 ⟵ “Other | $700 | $700 | $700 | $800”
  - column:Total Costs (without Dependent): 21680 ⟵ “Total Costs (without Dependent) | $30,730 | $32,150 | $16,970 | $21,680”
### `06e5d6eafed6357a` South Dakota State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sdstate.edu/office-financial-aid-scholarships/first-year-aid-offer-information (sha256 d1b85309589a)
- issues: semantic_review_required, conflicting_sources:https://www.sdstate.edu/office-financial-aid-scholarships/fafsa-special-unusual-circumstances
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Requesting a Cost of Attendance Increase The components you see on your Financial Aid Offer that make up your Cost of Attendance are based on estimated amounts.”
  - sentence: budget_increase ⟵ “If your actual costs are above the estimated costs on your aid offer, you can request an increase to your Cost of Attendance by completing our Cost of Attendance Increase Request form.”
### `1a696edb829ebc68` South Dakota State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sdstate.edu/office-financial-aid-scholarships/fafsa-special-unusual-circumstances (sha256 83da9c01c7e8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Home Office of Financial Aid and Scholarships Managing Aid FAFSA Special and Unusual Circumstances Follow Us: Facebook Instagram Email 605-688-4695 Special and Unusual Circumstances Sometimes, students have unique or unusual circumstances that are not accounted for in the Free Application for Federal Student Aid results or the estimated cost of attendance used to determine students’ financial aid ”
  - sentence: need_based_special_circumstances ⟵ “Circumstances Related to FAFSA FAFSA Dependency Status Students' Cost of Attendance Special Circumstances Related to the FAFSA The FAFSA for the 2026-27 academic year uses 2024 income and tax information to determine eligibility for the Pell Grant and other need-based aid such as Subsidized Direct Loans.”
  - sentence: need_based_special_circumstances ⟵ “You may qualify for a review of your FAFSA information if your 2024 income (or your family’s income for a dependent student) does not accurately reflect your current financial situation due to special circumstances, such as the following: Reduction in income due to unemployment, job change, reduced hours or retirement.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances and FAFSA Dependency Status Students who are considered dependent for federal financial aid purposes are required to include parent information on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If you are a dependent student who has unusual circumstances that have resulted in a breakdown in your relationship with your parents, you can ask the Financial Aid Office to review your situation to determine if you qualify to be considered independent for financial aid purposes.”
  - sentence: need_based_special_circumstances ⟵ “The following are some examples of situations that may qualify: Parent incarceration or institutionalization Physical, verbal or emotional abuse in the family Parents cannot be located Parent abandonment or estrangement Student is a victim of human trafficking Student is an asylee or refugee who came to the U.S. without a parent Students who request a review of their FAFSA dependency status must d”
### `1c72a57eb64a8a20` South Dakota State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sdstate.edu/office-financial-aid-scholarships/fafsa-special-unusual-circumstances (sha256 83da9c01c7e8)
- issues: semantic_review_required, conflicting_sources:https://www.sdstate.edu/office-financial-aid-scholarships/first-year-aid-offer-information
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Complete the Budget Adjustment form.”
  - sentence: budget_increase ⟵ “Budget Adjustment Form Contact Us Office of Financial Aid and Scholarships Physical Address 1175 Medary Ave.”
### `f5a158536138456b` South Dakota State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sdstate.edu/office-financial-aid-scholarships/satisfactory-academic-progress (sha256 a61c978e8fbb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal Form The satisfactory academic progress appeal form can be located at financial aid forms.”
  - sentence: sap_appeal ⟵ “Submitting an Appeal Federal regulations limit circumstances for which a suspension of financial aid may be appealed to the following: Death of a family member Illness or injury to the student Other special circumstances beyond the student’s control To appeal a financial aid suspension, a student must submit a completed SAP appeal form to the university Financial Aid Office.”
  - sentence: sap_appeal ⟵ “If a student’s SAP appeal indicates that the student’s failure to meet SAP standards was due to circumstances related to COVID-19 during the spring 2020 term, the student may appeal suspension based on the COVID-19 related circumstance.”
### `05b30b03de146785` South Dakota State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sdstate.edu/office-financial-aid-scholarships/cost-attendance (sha256 daf39aba5930)
- issues: residency_names_another_state, residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees(4): 11460 ⟵ “Tuition and Fees(4) | $9,780 | $11,460 | $13,479 | $11,214”
  - column:Housing and Food: 11024 ⟵ “Housing and Food | $11,024 | $11,024 | $11,024 | $11,024”
  - column:Total Direct Costs: 22484 ⟵ “Total Direct Costs | $20,804 | $22,484 | $24,503 | $22,238”
### `7714f83b3d6c5022` Southeast Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.southeasttech.edu/_resources/docs/costs-financial-aid/25-26/satisfactory-progress-appeal-form_25-26.pdf (sha256 7562046f0869)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Based on the Satisfactory Academic Progress Policy, the Appeal Committee will approve or deny your appeal.”
### `8ea1b0abad0af31a` Southeast Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.southeasttech.edu/_resources/docs/costs-financial-aid/26-27/special-circumstances-form_26-27.pdf (sha256 53bc47e1e86b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCES FORM 2026-2027 Student Name: SSN/ID: Address, City, State, Zip: Phone Number: • Change of Income for 2026 – reverse side of form must also be completed • The Financial Aid Ofce may make adjustments to the federal fnancial need calculation based on a change in income. • Please be accurate in completing the following information.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances can only be submitted once while attending Southeast Technical College.”
  - sentence: need_based_special_circumstances ⟵ “OTHER SPECIAL CIRCUMSTANCE With appropriate reason and documentation, the Financial Aid Ofce may consider adjustments to a student’s fnancial aid budget or to the federal fnancial aid formula.”
### `b2e33f907b5bf0f7` Southeast Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.southeasttech.edu/_resources/docs/costs-financial-aid/25-26/special-circumstances-form_25-26.pdf (sha256 0455ff435f79)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “SPECIAL CIRCUMSTANCES FORM 2025-2026 Student Name: SSN/ID: Address, City, State, Zip: Phone Number: • Change of Income for 2025 – reverse side of form must also be completed • The Financial Aid Office may make adjustments to the federal financial need calculation based on a change in income. • Please be accurate in completing the following information.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances can only be submitted once while attending Southeast Technical College.”
  - sentence: need_based_special_circumstances ⟵ “OTHER SPECIAL CIRCUMSTANCE With appropriate reason and documentation, the Financial Aid Office may consider adjustments to a student’s financial aid budget or to the federal financial aid formula.”
### `mf3ec8ceb324287d` Southeast Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.southeasttech.edu/programs/dual-credit.php (sha256 7d57bb5656cc)
- issues: multicolumn_layout_review
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 2, "tiers": 2}
  - per_credit_hour_charge: 80.37 ⟵ “Dual Credit courses cost $80.37 per credit hour — that is half of the cost of traditional”
  - per_credit_hour_charge: 80.37 ⟵ “Dual Credit courses cost $80.37 per credit hour – that is about half the cost of traditional”
  - eligibility_tier: 2.0 ⟵ “per semester. In addition, students who receive below a 2.0 GPA or who don’t complete”
  - eligibility_tier: 2.0 ⟵ “one semester to receive at least a 2.0 GPA as well as complete 67% of their courses”
  - eligibility_tier: 2.0 ⟵ “Please remember that the grades you receive in Dual            At Southeast Tech, students who receive below a 2.0 GPA”
### `5b31122ed8e9b71c` University of South Dakota — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Financial-Aid-Wrap-2025-26_Digital_ADA.pdf?rev=77a2c12b07d248e6ba307d3835be3228&hash=93A16A96EFF89296226D887B355246E7 (sha256 ccd83c2cee70)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Such circumstances would include an injury or • Undergraduate Students: The minimum cumulative GPA illness, the death of a relative or other special circumstances.”
### `6205d08223d47f94` University of South Dakota — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Financial-Aid/Applying-for-Aid/Satisfactory-Academic-Progress (sha256 c9b548986dbe)
- issues: semantic_review_required, conflicting_sources:https://www.usd.edu/About/Departments%20Offices%20and%20Resources/Office%20of%20Financial%20Aid,https://www.usd.edu/Admissions-and-Aid/Financial-Aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Such circumstances would include an injury or illness, the death of a relative or other special circumstances.”
### `6b8a9ae5554b941e` University of South Dakota — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.usd.edu/Admissions-and-Aid/Financial-Aid (sha256 64cedcd8919e)
- issues: semantic_review_required, conflicting_sources:https://www.usd.edu/About/Departments%20Offices%20and%20Resources/Office%20of%20Financial%20Aid,https://www.usd.edu/Admissions-and-Aid/Financial-Aid/Applying-for-Aid/Satisfactory-Academic-Progress
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Permission to Release Information Form Special Circumstances Complete this form if you, your spouse or your parents have had a loss of income, divorce, extreme medical expenses or other circumstances that affect your financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Request Form Click to Open Student Loan Default Rates Official Cohort Default Rate Reports are available to the public and may be downloaded into PDF files.”
### `ae99a1ad305f74b9` University of South Dakota — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.usd.edu/Admissions-and-Aid/Financial-Aid (sha256 64cedcd8919e)
- issues: semantic_review_required, conflicting_sources:https://www.usd.edu/About/Departments%20Offices%20and%20Resources/Office%20of%20Financial%20Aid,https://www.usd.edu/Admissions-and-Aid/Financial-Aid/Applying-for-Aid/Satisfactory-Academic-Progress
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Loan Cancellation or Reduction Form Satisfactory Academic Progress Appeal Form Students who have had their financial aid suspended due to unsatisfactory academic progress may appeal to the Office of Financial Aid by submitting the appeals form within 30 days of notification of unsatisfactory status and must be accompanied by relevant documentation.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Financial Aid Permission to Release Information Form Your student may provide you with written permission to access his/her financial aid records by submitting the following form as provided by the USD Office of Financial Aid.”
### `b9d5f86fa83b7c42` University of South Dakota — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Financial-Aid/Applying-for-Aid/Satisfactory-Academic-Progress (sha256 c9b548986dbe)
- issues: semantic_review_required, conflicting_sources:https://www.usd.edu/About/Departments%20Offices%20and%20Resources/Office%20of%20Financial%20Aid,https://www.usd.edu/Admissions-and-Aid/Financial-Aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appealing a Financial Aid Suspension Students who have had their eligibility suspended for Federal Student Aid may complete a Satisfactory Academic Progress Appeal form to explain circumstances that were beyond their control and adversely affected their ability to be academically successful at USD.”
### `bc3bef57e5d0c35d` University of South Dakota — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.usd.edu/About/Departments%20Offices%20and%20Resources/Office%20of%20Financial%20Aid (sha256 fb10846e99e2)
- issues: semantic_review_required, conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Financial-Aid,https://www.usd.edu/Admissions-and-Aid/Financial-Aid/Applying-for-Aid/Satisfactory-Academic-Progress
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Permission to Release Information Form Special Circumstances Complete this form if you, your spouse or your parents have had a loss of income, divorce, extreme medical expenses or other circumstances that affect your financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Request Form Click to Open Student Loan Default Rates Official Cohort Default Rate Reports are available to the public and may be downloaded into PDF files.”
### `be48cbc1175b626e` University of South Dakota — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Financial-Aid-Wrap-2025-26_Digital_ADA.pdf?rev=77a2c12b07d248e6ba307d3835be3228&hash=93A16A96EFF89296226D887B355246E7 (sha256 ccd83c2cee70)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory grades are “A”, “B”, “C”, “D”, “S” and to unsatisfactory academic progress may appeal to the Office of “RS.” Unsatisfactory grades are “F”, “I”, “U”, “RI”, “RU”, Financial Aid.”
### `f6b7b7b66aa8705f` University of South Dakota — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.usd.edu/About/Departments%20Offices%20and%20Resources/Office%20of%20Financial%20Aid (sha256 fb10846e99e2)
- issues: semantic_review_required, conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Financial-Aid,https://www.usd.edu/Admissions-and-Aid/Financial-Aid/Applying-for-Aid/Satisfactory-Academic-Progress
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Loan Cancellation or Reduction Form Satisfactory Academic Progress Appeal Form Students who have had their financial aid suspended due to unsatisfactory academic progress may appeal to the Office of Financial Aid by submitting the appeals form within 30 days of notification of unsatisfactory status and must be accompanied by relevant documentation.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Financial Aid Permission to Release Information Form Your student may provide you with written permission to access his/her financial aid records by submitting the following form as provided by the USD Office of Financial Aid.”
### `047b26d7c9bd87e3` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin (sha256 f3dc13cf3e63)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 12532 ⟵ “Tuition & Fees* | $9,916 | $12,532”
  - column:Housing & Food: 14994 ⟵ “Housing & Food | $11,238 | $14,994”
  - column:Direct Costs Total: 27526 ⟵ “Direct Costs Total | $21,154 | $27,526”
### `082af069c52682b5` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z (sha256 a1976c71f979)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition & Fees: 11457 ⟵ “Tuition & Fees | 9916 | 11457 | 13616”
  - on_campus:Course/Discipline Fees*: 510 ⟵ “Course/Discipline Fees* | 510 | 510 | 510”
  - on_campus:Housing & Food: 11238 ⟵ “Housing & Food | 11238 | 11238 | 11238”
  - on_campus:Direct Costs Total: 23205 ⟵ “Direct Costs Total | 21664 | 23205 | 25364”
  - on_campus:Books, Course Materials, Supplies & Equipment: 800 ⟵ “Books, Course Materials, Supplies & Equipment | 800 | 800 | 800”
  - on_campus:Personal Expenses: 2424 ⟵ “Personal Expenses | 2424 | 2424 | 2424”
  - on_campus:Transportation Expenses: 1914 ⟵ “Transportation Expenses | 1914 | 1914 | 1914”
  - on_campus:Loan Fees: 68 ⟵ “Loan Fees | 68 | 68 | 68”
  - on_campus:Indirect Costs Total: 5206 ⟵ “Indirect Costs Total | 5206 | 5206 | 5206”
  - on_campus:Total Annual Cost of Attendance Estimate: 28411 ⟵ “Total Annual Cost of Attendance Estimate | 26870 | 28411 | 30570”
### `08f8b59df578cc1c` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska (sha256 28b781c7c723)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $11,472”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $13,950”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $25,422”
### `098a0c9c782d96dc` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas (sha256 cdf38f3c87fc)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 13015 ⟵ “Tuition & Fees* | $9,916 | $13,015”
  - column:Housing & Food: 14370 ⟵ “Housing & Food | $11,238 | $14,370”
  - column:Direct Costs Total: 27385 ⟵ “Direct Costs Total | $21,154 | $27,385”
### `159b2779479bee51` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota (sha256 f0886ea772f1)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $19,312”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $15,552”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $34,864”
### `4606c723db446ff7` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z (sha256 a1976c71f979)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition & Fees: 9916 ⟵ “Tuition & Fees | 9916 | 11457 | 13616”
  - on_campus:Course/Discipline Fees*: 510 ⟵ “Course/Discipline Fees* | 510 | 510 | 510”
  - on_campus:Housing & Food: 11238 ⟵ “Housing & Food | 11238 | 11238 | 11238”
  - on_campus:Direct Costs Total: 21664 ⟵ “Direct Costs Total | 21664 | 23205 | 25364”
  - on_campus:Books, Course Materials, Supplies & Equipment: 800 ⟵ “Books, Course Materials, Supplies & Equipment | 800 | 800 | 800”
  - on_campus:Personal Expenses: 2424 ⟵ “Personal Expenses | 2424 | 2424 | 2424”
  - on_campus:Transportation Expenses: 1914 ⟵ “Transportation Expenses | 1914 | 1914 | 1914”
  - on_campus:Loan Fees: 68 ⟵ “Loan Fees | 68 | 68 | 68”
  - on_campus:Indirect Costs Total: 5206 ⟵ “Indirect Costs Total | 5206 | 5206 | 5206”
  - on_campus:Total Annual Cost of Attendance Estimate: 26870 ⟵ “Total Annual Cost of Attendance Estimate | 26870 | 28411 | 30570”
### `47d80b8f23f3de2a` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin (sha256 f3dc13cf3e63)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $12,532”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $14,994”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $27,526”
### `54e4fea097fbf71e` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance (sha256 21a579b75950)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition & Fees: 11457 ⟵ “Tuition & Fees | 9916 | 11457 | 13616”
  - on_campus:Course/Discipline Fees*: 510 ⟵ “Course/Discipline Fees* | 510 | 510 | 510”
  - on_campus:Housing & Food: 11238 ⟵ “Housing & Food | 11238 | 11238 | 11238”
  - on_campus:Direct Costs Total: 23205 ⟵ “Direct Costs Total | 21664 | 23205 | 25364”
  - on_campus:Books, Course Materials, Supplies & Equipment: 800 ⟵ “Books, Course Materials, Supplies & Equipment | 800 | 800 | 800”
  - on_campus:Personal Expenses: 2424 ⟵ “Personal Expenses | 2424 | 2424 | 2424”
  - on_campus:Transportation Expenses: 1914 ⟵ “Transportation Expenses | 1914 | 1914 | 1914”
  - on_campus:Loan Fees: 68 ⟵ “Loan Fees | 68 | 68 | 68”
  - on_campus:Indirect Costs Total: 5206 ⟵ “Indirect Costs Total | 5206 | 5206 | 5206”
  - on_campus:Total Annual Cost of Attendance Estimate: 28411 ⟵ “Total Annual Cost of Attendance Estimate | 26870 | 28411 | 30570”
### `5cd3963030e4dab5` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota (sha256 2f33ba4d9298)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 12288 ⟵ “Tuition & Fees* | $9,916 | $12,288”
  - column:Housing & Food: 11446 ⟵ “Housing & Food | $11,238 | $11,446”
  - column:Direct Costs Total: 23734 ⟵ “Direct Costs Total | $21,154 | $23,734”
### `5fcf29310f1d19ee` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a (sha256 eeac31086bfb)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 2, "rows": 3}
  - column:Tuition and Fees:: 9656.5 ⟵ “Tuition and Fees: | $9,656.50 | $13,355.50”
  - column:$2,424: 1914 ⟵ “$2,424 | $1,914 | $68”
  - column:Earn while you learn with Federal Work Study, offering: 800 ⟵ “Earn while you learn with Federal Work Study, offering | $800”
  - column:Tuition and Fees:: 13355.5 ⟵ “Tuition and Fees: | $9,656.50 | $13,355.50”
  - column:$2,424: 68 ⟵ “$2,424 | $1,914 | $68”
### `7b6ac0502f317a2d` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming (sha256 7eb27bbbef40)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $8,532”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $14,500”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $23,032”
### `7c54980c88ca103e` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa (sha256 ff3d96d3bfd7)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $11,971”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $14,022”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $25,993”
### `7f8deb39fbac0511` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois (sha256 bfab06b1a5e7)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 20736 ⟵ “Tuition & Fees* | $9,916 | $20,736”
  - column:Housing & Food: 15184 ⟵ “Housing & Food | $11,238 | $15,184”
  - column:Direct Costs Total: 35920 ⟵ “Direct Costs Total | $21,154 | $35,920”
### `90c39bf824cfac11` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana (sha256 fcecc0f96463)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $9,750”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $14,120”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $23,870”
### `93e34d0a23034e11` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance (sha256 21a579b75950)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - on_campus:Tuition & Fees: 9916 ⟵ “Tuition & Fees | 9916 | 11457 | 13616”
  - on_campus:Course/Discipline Fees*: 510 ⟵ “Course/Discipline Fees* | 510 | 510 | 510”
  - on_campus:Housing & Food: 11238 ⟵ “Housing & Food | 11238 | 11238 | 11238”
  - on_campus:Direct Costs Total: 21664 ⟵ “Direct Costs Total | 21664 | 23205 | 25364”
  - on_campus:Books, Course Materials, Supplies & Equipment: 800 ⟵ “Books, Course Materials, Supplies & Equipment | 800 | 800 | 800”
  - on_campus:Personal Expenses: 2424 ⟵ “Personal Expenses | 2424 | 2424 | 2424”
  - on_campus:Transportation Expenses: 1914 ⟵ “Transportation Expenses | 1914 | 1914 | 1914”
  - on_campus:Loan Fees: 68 ⟵ “Loan Fees | 68 | 68 | 68”
  - on_campus:Indirect Costs Total: 5206 ⟵ “Indirect Costs Total | 5206 | 5206 | 5206”
  - on_campus:Total Annual Cost of Attendance Estimate: 26870 ⟵ “Total Annual Cost of Attendance Estimate | 26870 | 28411 | 30570”
### `9eaf4ec21258f707` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado (sha256 cc64b9b8fbde)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees: 15014 ⟵ “Tuition & Fees | $9,916 | $15,014”
  - column:Housing & Food: 19242 ⟵ “Housing & Food | $11,238 | $19,242”
  - column:Direct Costs Total: 34256 ⟵ “Direct Costs Total | $21,154 | $34,256”
### `a6ad0ed05c505fd6` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245 (sha256 44540ed3a601)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 4, "rows": 8}
  - column:TUITION & FEES: 9916.5 ⟵ “TUITION & FEES | $9,916.50”
  - column:+ HOUSING: 5148.0 ⟵ “+ HOUSING | $5,148.00”
  - column:+ FOOD: 4350.0 ⟵ “+ FOOD | $4,350.00”
  - column:= COSTS: 19414.5 ⟵ “= COSTS | $19,414.50 | $ 0.00 | $ 0.00 | $ 0.00”
  - column:SCHOLARSHIPS AND: 3000.0 ⟵ “SCHOLARSHIPS AND | $3,000.00”
  - column:= FINANCIAL AID: 8500.0 ⟵ “= FINANCIAL AID | $8,500.00 | $ 0.00 | $ 0.00 | $ 0.00”
  - column:OUT-OF-: 19414.5 ⟵ “OUT-OF- | $19,414.50”
  - column:COSTS: 10914.5 ⟵ “COSTS | $10,914.50”
  - column:= COSTS: 0.0 ⟵ “= COSTS | $19,414.50 | $ 0.00 | $ 0.00 | $ 0.00”
  - column:= FINANCIAL AID: 0.0 ⟵ “= FINANCIAL AID | $8,500.00 | $ 0.00 | $ 0.00 | $ 0.00”
  - column:= COSTS: 0.0 ⟵ “= COSTS | $19,414.50 | $ 0.00 | $ 0.00 | $ 0.00”
  - column:= FINANCIAL AID: 0.0 ⟵ “= FINANCIAL AID | $8,500.00 | $ 0.00 | $ 0.00 | $ 0.00”
  - column:= COSTS: 0.0 ⟵ “= COSTS | $19,414.50 | $ 0.00 | $ 0.00 | $ 0.00”
  - column:= FINANCIAL AID: 0.0 ⟵ “= FINANCIAL AID | $8,500.00 | $ 0.00 | $ 0.00 | $ 0.00”
### `aca807887826f6c3` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota (sha256 f0886ea772f1)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 19312 ⟵ “Tuition & Fees* | $9,916 | $19,312”
  - column:Housing & Food: 15552 ⟵ “Housing & Food | $11,238 | $15,552”
  - column:Direct Costs Total: 34864 ⟵ “Direct Costs Total | $21,154 | $34,864”
### `bee47a77aea29175` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana (sha256 fcecc0f96463)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9750 ⟵ “Tuition & Fees* | $9,916 | $9,750”
  - column:Housing & Food: 14120 ⟵ “Housing & Food | $11,238 | $14,120”
  - column:Direct Costs Total: 23870 ⟵ “Direct Costs Total | $21,154 | $23,870”
### `c9d669a7b322c9d0` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota (sha256 2f33ba4d9298)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $12,288”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $11,446”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $23,734”
### `e34cbd9be6174d7c` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska (sha256 28b781c7c723)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 11472 ⟵ “Tuition & Fees* | $9,916 | $11,472”
  - column:Housing & Food: 13950 ⟵ “Housing & Food | $11,238 | $13,950”
  - column:Direct Costs Total: 25422 ⟵ “Direct Costs Total | $21,154 | $25,422”
### `e6df39abc00f61f4` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado (sha256 cc64b9b8fbde)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees: 9916 ⟵ “Tuition & Fees | $9,916 | $15,014”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $19,242”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $34,256”
### `eb4b75352f4b5e55` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming (sha256 7eb27bbbef40)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 8532 ⟵ “Tuition & Fees* | $9,916 | $8,532”
  - column:Housing & Food: 14500 ⟵ “Housing & Food | $11,238 | $14,500”
  - column:Direct Costs Total: 23032 ⟵ “Direct Costs Total | $21,154 | $23,032”
### `ee18141e4ed76fc0` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas (sha256 cdf38f3c87fc)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $13,015”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $14,370”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $27,385”
### `ef05350d9cbe0414` University of South Dakota — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa (sha256 ff3d96d3bfd7)
- issues: residency_names_another_state, residency_unknown, conflicting_sources:https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Financial-Aid/Sioux-Falls-Cost-Estimate-Guide.pdf?rev=bfab17f465834a78b41a52da9c1a567a,https://www.usd.edu/-/media/Project/USD/DotEdu/Admissions-and-Aid/Tuition-and-Costs/Cost-Comparison-Worksheet.pdf?rev=e53db35e84004eee9069556964e73173&hash=268C8A0429C21179D06EAB1BEA98E245,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 11971 ⟵ “Tuition & Fees* | $9,916 | $11,971”
  - column:Housing & Food: 14022 ⟵ “Housing & Food | $11,238 | $14,022”
  - column:Direct Costs Total: 25993 ⟵ “Direct Costs Total | $21,154 | $25,993”
### `fcbfcaa5621b4ea1` University of South Dakota — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Illinois (sha256 bfab06b1a5e7)
- issues: conflicting_sources:https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Colorado,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Iowa,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Kansas,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Minnesota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Montana,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Nebraska,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/North-Dakota,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wisconsin,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/South-Dakota-Advantage/Wyoming,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/Undergraduate-Cost-of-Attendance,https://www.usd.edu/Admissions-and-Aid/Tuition-and-Costs/~/link.aspx?_id=C764067E5DFB460D879DCD16ACA89422&_z=z
- checks: {"columns": 1, "rows": 3}
  - column:Tuition & Fees*: 9916 ⟵ “Tuition & Fees* | $9,916 | $20,736”
  - column:Housing & Food: 11238 ⟵ “Housing & Food | $11,238 | $15,184”
  - column:Direct Costs Total: 21154 ⟵ “Direct Costs Total | $21,154 | $35,920”
### `429fc84a3fe68855` Western Dakota Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wdt.edu/paying-for-school/financial-aid/satisfactory-academic-progress/ (sha256 754793a26a00)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appealing Financial Aid Termination Students who are placed on financial aid termination may complete a Satisfactory Academic Progress Appeal form to explain circumstances that adversely affected their ability to be academically successful at Western Dakota Tech.”
### `abfbbc40d117d391` Western Dakota Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wdt.edu/paying-for-school/financial-aid/satisfactory-academic-progress/ (sha256 754793a26a00)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Incompletes If a student is unable to complete all requirements, due to special circumstances approved by the instructor, an incomplete may be issued.”
  - sentence: need_based_special_circumstances ⟵ “Reason for appeal may include: personal illness or illness of immediate family member, death of an immediate family member, change of program, or other special circumstances that prevented the student from being successful.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 139; pages by category: admissions_tests 20, aid_appeals 3, cost_of_attendance 2, degree_requirements 16, dual_enrollment 12, merit_scholarships 102, residency 5, transfer_credit 4, tuition_fees 17

## Blocked by the site (every request refused; needs the browser fallback)

- Dakota Wesleyan University (`ipeds-219091`)
- University of Sioux Falls (`ipeds-219383`)

## Leads: official pages found with no extracted record

- Augustana University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Black Hills State University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Dakota State University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Institute of Lutheran Theology: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Kairos University: tuition_fees, admissions_tests, merit_scholarships
- Lake Area Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Mitchell Technical College: cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Mount Marty University: admissions_tests
- Northern State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements, aid_appeals
- Oglala Lakota College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Sinte Gleska University: cost_of_attendance, admissions_tests, degree_requirements
- South Dakota School of Mines and Technology: cost_of_attendance, admissions_tests, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- South Dakota State University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Southeast Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships
- University of South Dakota: admissions_tests, merit_scholarships, residency, degree_requirements
- Western Dakota Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, degree_requirements
