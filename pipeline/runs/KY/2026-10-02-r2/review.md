# Review queue — KY (2026-27)

Pages fetched: 1922; failures: 88. Candidates: 628 (222 without issues, 406 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 22 | 14 | 8 | 0 | 2 |
| cost_of_attendance | 0 | 0 | 19 | 9 | 16 | 0 | 2 |
| admissions_tests | 0 | 0 | 2 | 0 | 42 | 0 | 2 |
| common_data_set | 0 | 0 | 2 | 0 | 1 | 41 | 2 |
| merit_scholarships | 0 | 0 | 5 | 1 | 38 | 0 | 2 |
| ap_credit | 0 | 0 | 2 | 0 | 14 | 28 | 2 |
| clep_credit | 0 | 0 | 3 | 0 | 7 | 34 | 2 |
| ib_credit | 0 | 0 | 1 | 0 | 3 | 40 | 2 |
| dual_enrollment | 0 | 0 | 16 | 5 | 15 | 8 | 2 |
| transfer_credit | 0 | 0 | 2 | 1 | 39 | 2 | 2 |
| statewide_articulation | 0 | 0 | 0 | 0 | 4 | 40 | 2 |
| residency | 0 | 0 | 0 | 0 | 21 | 23 | 2 |
| degree_requirements | 0 | 0 | 1 | 1 | 21 | 21 | 2 |
| aid_appeals | 0 | 0 | 0 | 32 | 7 | 5 | 2 |

## Ready for review (222)

### `82efa1fc3bf8543d` Asbury University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.asbury.edu/undergraduate/admissions/academy/ (sha256 a7445f8f4b3a)
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "tiers": 1}
  - state_grant_accepted: True ⟵ “Scholarship opportunities: Asbury University participates in the Kentucky Dual Credit Scholarship Program. Eligible Kentucky students may use Dual Credit or Work Ready Kentucky Scholarships toward qualifying online and on-campus courses.”
  - eligibility_tier: 3.0 ⟵ “An official high school transcript showing a weighted cumulative GPA of 3.00 or higher for seniors or 3.25 or higher for juniors”
### `a7845bf2890456e6` Ashland Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://ashland.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 754ee7013284)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `d301be69218edd17` Ashland Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://ashland.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 754ee7013284)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `c36e05c551f024c7` Bellarmine University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bellarmine.edu/financial-aid/undergraduate-financial-aid-tuition.php (sha256 577968740a86)
- checks: {"columns": 1, "rows": 4}
  - column:Tuition and Fees: 50660 ⟵ “Tuition and Fees | $50,660”
  - column:Matriculation Fee*: 400 ⟵ “Matriculation Fee* | $400”
  - column:Housing**: 5250 ⟵ “Housing** | $5,250”
  - column:Food: 5520 ⟵ “Food | $5,520”
### `f2b50cd3fe21bf96` Bellarmine University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.bellarmine.edu/dual-credit-institute/index.php (sha256 a41f751f9276)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “If you have a 2.5 GPA unweighted and a green light from your counselor, you’re ready”
### `c19171d827b7d03c` Berea College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.berea.edu/student-financial-aid/berea-college-cost-of-attendance-for-2026-2027-fall-spring (sha256 28230285a7bf)
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition: 56900 ⟵ “Tuition | $56,900”
  - column:Housing: 5000 ⟵ “Housing | $5,000”
  - column:Food: 4142 ⟵ “Food | $4,142”
  - column:Books and Supplies: 750 ⟵ “Books and Supplies | $750”
  - column:Transportation: 1350 ⟵ “Transportation | $1,350”
  - column:Personal: 1800 ⟵ “Personal | $1,800”
  - column:Total Cost of Attendance: 69942 ⟵ “Total Cost of Attendance | $69,942”
  - column:Total Direct Costs: 66042 ⟵ “Total Direct Costs | $66,042”
  - column:Total Indirect Costs: 3900 ⟵ “Total Indirect Costs | $3,900”
### `2344a65ae483e580` Berea College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.berea.edu/admissions/admission-information/apply/checklist-items/transfer-faqs (sha256 685eb051a97a)
- checks: {"fields": ["min_grade", "residency_requirement_credits"]}
  - min_grade: C ⟵ “Only courses and earned credits completed with a grade of C or higher at a regionally accredited institution within 10 years of initial enrollment at Berea are transferable to Berea College.”
  - residency_requirement_credits: 24 ⟵ “Applicants with less than a 2.5 cumulative college GPA or less than a 2.5 college GPA in the last 24 hours of transferrable college credit are ineligible for admission to Berea College.”
### `38193f0764b290d1` Big Sandy Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://bigsandy.kctcs.edu/affording-college/tuition-costs/tuition-fees.aspx (sha256 d1402137df4c)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `c2de1fa533ca7ea6` Big Sandy Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://bigsandy.kctcs.edu/affording-college/tuition-costs/tuition-fees.aspx (sha256 d1402137df4c)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `3fecea5cebfc5ce7` Big Sandy Community and Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://bigsandy.kctcs.edu/dual-credit/eligibility-requirements.aspx (sha256 12742c1d815e)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “3.3 Addendum for Enrollment into Technical Education Dual Credit Courses: Students who do not have the minimum unweighted cumulative high school 2.0 GPA the”
### `59e45217fcc6148c` Big Sandy Community and Technical College — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://bigsandy.kctcs.edu/admissions/information-for/credit-for-prior-learning.aspx (sha256 221113f3ce43)
- checks: {"distinct_exams": 14, "equivalencies": 14, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|4]:  ⟵ “Biology HL | 4 | BIO 152 | 3 credit hours”
  - equivalencies[IB-BIOLOGY-SL|4]:  ⟵ “Biology SL | 4 | BIO 112 | 3 credit hours”
  - equivalencies[IB-CHEMISTRY-HL|4]:  ⟵ “Chemistry HL | 4 | CHE 170, CHE 180 | 8 credit hours”
  - equivalencies[IB-CHEMISTRY-SL|4]:  ⟵ “Chemistry SL | 4 | CHE 140 | 3 credit hours”
  - equivalencies[IB-ENGLISH-A-LITERATURE-HL|4]:  ⟵ “English A: Literature HL | 4 | ENG 101 | 3 credit hours”
  - equivalencies[IB-FRENCH-HL|5]:  ⟵ “French B HL | 5 | FRE 201, FRE 201 | 6 credit hours”
  - equivalencies[IB-FRENCH-SL|5]:  ⟵ “French B SL | 5 | FRE 101, FRE 102 | 8 credit hours”
  - equivalencies[IB-HISTORY-HL|5]:  ⟵ “History HL | 5 | HIS 108, HIS 109 | 6 credit hours”
  - equivalencies[IB-MUSIC-SL|4]:  ⟵ “Music SL/HL | 4 | MUS 100 | 3 credit hours”
  - equivalencies[IB-PHYSICS-SL|5]:  ⟵ “Physics SL/HL | 5 | PHY 2011 | 4 credit hours”
  - equivalencies[IB-PSYCHOLOGY-SL|4]:  ⟵ “Psychology SL | 4 | PSY 110 | 3 credit hours”
  - equivalencies[IB-SPANISH-HL|5]:  ⟵ “Spanish B HL | 5 | SPA 201, SPA 202 | 6 credit hours”
  - equivalencies[IB-SPANISH-SL|5]:  ⟵ “Spanish B SL | 5 | SPA 101, SPA 102 | 8 credit hours”
  - equivalencies[IB-THEATRE-HL|4]:  ⟵ “Theatre Arts HL/SL | 4 | THA 101 | 3 credit hours”
### `5df4df46c68a949d` Big Sandy Community and Technical College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://bigsandy.kctcs.edu/admissions/information-for/credit-for-prior-learning.aspx (sha256 221113f3ce43)
- checks: {"distinct_exams": 33, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[AP-RESEARCH|3-5]:  ⟵ “AP Research Capstone | 3-5 | Elective Credit | 3 credit hours”
  - equivalencies[AP-SEMINAR|3-5]:  ⟵ “AP Seminar | 3-5 | Elective Credit | 3 credit hours”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ART 105 or ART 106 | 6 credit hours”
  - equivalencies[AP-BIOLOGY|3-5]:  ⟵ “Biology | 3-5 | BIO 112 | 3 credit hours”
  - equivalencies[AP-CALCULUS-AB|3-5]:  ⟵ “Calculus AB | 3-5 | MAT 175 | 5 credit hours”
  - equivalencies[AP-CALCULUS-BC|3-5]:  ⟵ “Calculus BC | 3-5 | MAT 175 and MAT 185 | 10 credit hours”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHE 170 | 4 credit hours”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | 3 | RAE 150 | 4 credit hours”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3-5]:  ⟵ “Comparative Government and Politics | 3-5 | POL 210 | 3 credit hours”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | Elective Credit | 3 credit hours”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3-5]:  ⟵ “Computer Science Principles | 3-5 | Elective Credit | 3 credit hours”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3-5]:  ⟵ “English Literature/Composition | 3-5 | ENG 161 | 3 credit hours”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3-5]:  ⟵ “English Literature/Composition | 3-5 | ENG 101 | 3 credit hours”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science | 3-5 | EST 150 | 4 credit hours”
  - equivalencies[AP-EUROPEAN-HISTORY|3-5]:  ⟵ “European History | 3-5 | HIS 104 and HIS 105 | 6 credit hours”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | FRE 201 | 3 credit hours”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Human Geography | 3-5 | GEO 172 | 3 credit hours”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture | 3 | Elective Credit | 3 credit hours”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture | 3 | JPN 201 | 3 credit hours”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin: Vergil | 3 | Elective Credit | 3 credit hours”
  - equivalencies[AP-MICROECONOMICS|3-5]:  ⟵ “Microeconomics | 3-5 | ECO 201 | 3 credit hours”
  - equivalencies[AP-MICROECONOMICS|3-5]:  ⟵ “Microeconomics | 3-5 | ECO 202 | 3 credit hours”
  - equivalencies[AP-MUSIC-THEORY|3-5]:  ⟵ “Music Theory | 3-5 | MUS 174 | 3 credit hours”
  - equivalencies[AP-PHYSICS-1|3-5]:  ⟵ “Physics 1 | 3-5 | PHY 201 | 4 credit hours”
  - equivalencies[AP-PHYSICS-2|3-5]:  ⟵ “Physics 2 | 3-5 | PHY 203 | 4 credit hours”
  - … 10 more rows
### `c62953437514aca2` Big Sandy Community and Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://bigsandy.kctcs.edu/admissions/information-for/credit-for-prior-learning.aspx (sha256 221113f3ce43)
- checks: {"distinct_exams": 30, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[CLEP-FRENCH-LANGUAGE|50-69]:  ⟵ “College Level French Language | 50-69 | FRE 201 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|70 or above]:  ⟵ “College Level French Language | 70 or above | FRE 201, FRE 202 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50-69]:  ⟵ “College Level German Language | 50-69 | GER 201 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|70 or above]:  ⟵ “College Level German Language | 70 or above | GER 201, GER 202 | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50-69]:  ⟵ “College Level Spanish Language | 50-69 | SPA 201 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|70 or above]:  ⟵ “College Level Spanish Language | 70 or above | SPA 201, SPA 202 | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|History and Social Sciences]:  ⟵ “College Level Spanish Language | History and Social Sciences”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50 or above]:  ⟵ “American Government | 50 or above | POL 101 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50 or above]:  ⟵ “History of the United States I | 50 or above | HIS 108 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50 or above]:  ⟵ “History of the United States II | 50 or above | HIS 109 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50 or above]:  ⟵ “Introductory Psychology | 50 or above | PSY 110 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50 or above]:  ⟵ “Principles of Macroeconomics | 50 or above | ECO 202 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50 or above]:  ⟵ “Principles of Microeconomics | 50 or above | ECO 201 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50 or above]:  ⟵ “Introductory Sociology | 50 or above | SOC 101 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50 or above]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 or above | HIS 104 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50 or above]:  ⟵ “Western Civilization II: 1648 to the Present | 50 or above | HIS 105 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50 or above]:  ⟵ “Social Sciences and History | 50 or above | SOC 101 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50 or above]:  ⟵ “Human Growth and Developmental | 50 or above | AHS 100 | 2”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|Science and Mathematics]:  ⟵ “Human Growth and Developmental | Science and Mathematics”
  - equivalencies[CLEP-CALCULUS|50 or above]:  ⟵ “Calculus | 50 or above | MAT 174 or MAT 175 | 4,5”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50 or above]:  ⟵ “College Mathematics | 50 or above | MAT 146 | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50 or above]:  ⟵ “College Algebra | 50 or above | MAT 150 | 3”
  - equivalencies[CLEP-PRECALCULUS|50 or above]:  ⟵ “Pre-Calculus | 50 or above | MAT 160 | 5”
  - equivalencies[CLEP-BIOLOGY|50-59]:  ⟵ “Biology | 50-59 | BIO 112 | 3”
  - equivalencies[CLEP-BIOLOGY|60-64]:  ⟵ “Biology | 60-64 | BIO 120,BIO 112 | 6”
  - … 14 more rows
### `f15a9de2d9faa897` Campbellsville University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.campbellsville.edu/admission-and-aid/financial-aid/cost-of-attendance.html (sha256 39b24257ce03)
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition*: 29760 ⟵ “Tuition* | $29,760 | $29,760 | ”
  - column:Technology Fee: 300 ⟵ “Technology Fee | $300 | $300 | ”
  - column:Activity Fee: 200 ⟵ “Activity Fee | $200 | $200 | ”
  - column:Food & Housing (On Campus): 10984 ⟵ “Food & Housing (On Campus) | $10,984 |  | ”
  - column:Books, Course Materials, Supplies, & Equipment: 800 ⟵ “Books, Course Materials, Supplies, & Equipment | $800 | $800 | ”
  - column:Personal Expenses: 3520 ⟵ “Personal Expenses | $3,520 | $3,520 | ”
  - column:Transportation: 2730 ⟵ “Transportation | $2,730 | $6,272 | ”
  - column:Loan Fees: 68 ⟵ “Loan Fees | $68 | $68 | ”
  - column:Total COA: 48362 ⟵ “Total COA | $48,362 | $44,736 | $50,280”
  - column:Total Direct Cost: 41244 ⟵ “Total Direct Cost | $41,244 | $30,260 | ”
  - column:Total Indirect Cost:: 7118 ⟵ “Total Indirect Cost: | $7,118 | $14,476 | $20,020”
### `mecd1585c27679fa` Campbellsville University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.campbellsville.edu/admission-and-aid/dual-credit/index.html (sha256 f283c373b331)
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Have a minimum cumulative grade point average of 3.0”
  - state_grant_accepted: True ⟵ “KHEAA also administers the Dual Credit Scholarship program for eligible Kentucky high”
  - eligibility_tier: 3.0 ⟵ “Students must be a sophomore, junior, or senior with at least a 3.0 gpa in order”
### `2cb44abab5f05e43` Centre College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.centre.edu/admission-aid/international-applicants/international-student-financial-aid (sha256 f13f817e8f9a)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 ⟵ “Performing Arts | Up to $5,000”
### `79b77ccde3f8b17c` Centre College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.centre.edu/admission-aid/international-applicants/international-student-financial-aid (sha256 f13f817e8f9a)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 ⟵ “Language | Up to $5,000”
### `dcd9602b84dc16ed` Centre College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.centre.edu/admission-aid/international-applicants/international-student-financial-aid (sha256 f13f817e8f9a)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 ⟵ “Studio Arts | Up to $5,000”
### `841e7398e7c5fa55` Centre College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.centre.edu/admission-aid/international-applicants (sha256 4d7c4d2f8676)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 57500 ⟵ “Tuition | $57,500”
  - column:Housing: 7870 ⟵ “Housing | $7,870”
  - column:Food: 7870 ⟵ “Food | $7,870”
  - column:Student Fee: 750 ⟵ “Student Fee | $750”
  - column:TOTAL: 73990 ⟵ “TOTAL | $73,990”
### `5b00ac25afc11d55` Eastern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/general-academic-information/academic-standards/ (sha256 42f0698dc377)
- checks: {"thresholds": null}
  - gpa_requirement: Over 50 ⟵ “Over 50 | 2.0”
### `d5b81038c417a3a6` Eastern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/general-academic-information/academic-standards/ (sha256 42f0698dc377)
- checks: {"thresholds": null}
  - gpa_requirement: Fewer than 31 ⟵ “Fewer than 31 | 1.5”
### `6a1b0a4b0958ccbf` Eastern Kentucky University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.eku.edu/in/guides/advanced-placement-program-exams/ (sha256 03a983d92eca)
- checks: {"distinct_exams": 39, "equivalencies": 58, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3, 4, or 5]:  ⟵ “APAF | African American Studies | 3, 4, or 5 | 3 | AFA 201”
  - equivalencies[AP-ART-HISTORY|3, 4, or 5]:  ⟵ “APAH | Art History | 3, 4, or 5 | 3 | ART 200”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “APB | Biology | 3 | 3 | BIO 100”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “APB | Biology | 4 | 4 | BIO 111”
  - equivalencies[AP-BIOLOGY|5]:  ⟵ “APB | Biology | 5 | 8 | BIO 111 and BIO 112”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3, 4, or 5]:  ⟵ “APBF | Business and Personal Finance | 3, 4, or 5 | 3 | FIN 201”
  - equivalencies[AP-CALCULUS-AB|3, 4, or 5]:  ⟵ “APMA | Calculus AB | 3, 4, or 5 | 4 | MAT 234”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “APMB | Calculus BC | 3 | 4 | MAT 234”
  - equivalencies[AP-CALCULUS-BC|4 or 5]:  ⟵ “APMB | Calculus BC | 4 or 5 | 8 | MAT 234 and MAT 244”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “APC | Chemistry | 3 | 4 | CHE 101/101L”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “APC | Chemistry | 4 | 4 | CHE 111/111L”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “APC | Chemistry | 5 | 8 | CHE 111/111L and CHE 112/112L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3, 4, or 5]:  ⟵ “APCH | Chinese Language & Culture | 3, 4, or 5 | 6 | FLS 101 and FLS 102”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “APCA | Computer Science A | 3 | 3 | CSC 170”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4 or 5]:  ⟵ “APCA | Computer Science A | 4 or 5 | 3 | CSC 190”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, or 5]:  ⟵ “APCP | Computer Science Principles | 3, 4, or 5 | 3 | CSC 178”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3, or 4]:  ⟵ “APEC | English Language & Composition | 3, or 4 | 3 | ENG 101”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “APEC | English Language & Composition | 5 | 6 | ENG 101 and ENG 102”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3, 4, or 5]:  ⟵ “APEL | English Literature and Composition | 3, 4, or 5 | 3 | ENG 101 or ENG 110”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3, 4, or 5]:  ⟵ “APES | Environmental Science | 3, 4, or 5 | 3 | EHS 280”
  - equivalencies[AP-EUROPEAN-HISTORY|3, 4, or 5]:  ⟵ “APEH | European History | 3, 4, or 5 | 3 | HIS 101”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “APF | French Language & Culture | 3 | 9 | FRE 101, FRE 102, and FRE 201”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4 or 5]:  ⟵ “APF | French Language & Culture | 4 or 5 | 12 | FRE 101, FRE 102, FRE 201, and FRE 202”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “APG | German Language & Culture | 3 | 9 | GER 101, GER 102, and GER 201”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4 or 5]:  ⟵ “APG | German Language & Culture | 4 or 5 | 12 | GER 101, GER 102, GER 201, and GER 202”
  - … 33 more rows
### `95ce7492df21917e` Eastern Kentucky University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.eku.edu/dual-credit/ (sha256 0bf98134d3e7)
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "tiers": 1}
  - state_grant_accepted: True ⟵ “KHEAA Dual Credit Scholarships and Work Ready Dual Credit Scholarships may be used towards covering tuition. Use the links below for additional information and to complete the application.”
  - state_grant_accepted: True ⟵ “Students can receive up to two work ready dual credit scholarships for eligible career and technical education (CTE) each year of high school.”
  - state_grant_accepted: True ⟵ “Students can receive up to one dual credit scholarship for eligible general education courses each year during the 11th and 12th grade years.”
  - state_grant_accepted: True ⟵ “Homeschool students may still qualify for the KHEAA Dual Credit Scholarships, but must apply using the Home School Application for Dual Credit scholarships through KHEAA. Select the button below to access the application!”
  - state_grant_accepted: True ⟵ “Homeschool students may not use the KHEAA Work Ready Dual Credit Scholarship to pay for their Work Ready Courses per KHEAA.”
  - state_grant_accepted: True ⟵ “Work Ready Dual Credit Scholarship Eligible Courses”
  - eligibility_tier: 2.5 ⟵ “The student must have an unweighted GPA of 2.5 or higher.”
### `97a665b983dfcc97` Elizabethtown Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://elizabethtown.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 b5753dc32bab)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `c78a71f31703ac05` Elizabethtown Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://elizabethtown.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 b5753dc32bab)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `b987dad8ff175b73` Elizabethtown Community and Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://elizabethtown.kctcs.edu/admissions/assessment-center/index.aspx (sha256 447b00296bf7)
- checks: {"distinct_exams": 30, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BAS 283 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | BAS 282 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introduction to Business Law | 50 | BAS 267 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 50 | TRN 146 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 251 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | ENG 161 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 161 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | HUM 120 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition, College Composition Modular | 50 | ENG 101 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50-69]:  ⟵ “College Level French Language | 50-69 | FRE 201 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|70]:  ⟵ “College Level French Language | 70 | FRE 201 and FRE 202 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50-69]:  ⟵ “College Level German Language | 50-69 | GER 201 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|70]:  ⟵ “College Level German Language | 70 | GER 201 and GER 202 | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50-69]:  ⟵ “College Level Spanish | 50-69 | SPA 201 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|70]:  ⟵ “College Level Spanish | 70 | SPA 201 and SPA 202 | 6”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POL 101 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | HIS 108 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | HIS 109 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSY 110 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECO 202 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECO 201 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC 101 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | HIS 104 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present | 50 | HIS 105 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | SOC 101 | 3”
  - … 10 more rows
### `59c6161014eb9f71` Gateway Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://gateway.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 0726d81c5329)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `67364391b80bcf21` Gateway Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://gateway.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 0726d81c5329)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `a906b019a8170790` Gateway Community and Technical College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://gateway.kctcs.edu/education-training/prior-learning/standards-for-awarding-credit/special-exams/clep-exam-credit.aspx (sha256 9a73f57c2c24)
- checks: {"distinct_exams": 30, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | BAS 283 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | BAS 282 | 3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introduction to Business Law | 50 | BAS 267 | 3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems and Computer Applications | 50 | TRN 146 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 251 | 3”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | ENG 161 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 161 | 3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | HUM 120 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition, College Composition Modular | 50 | ENG 101 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50–69]:  ⟵ “College Level French Language | 50–69 | FRE 201 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|70]:  ⟵ “College Level French Language | 70 | FRE 201 and FRE 202 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50–69]:  ⟵ “College Level German Language | 50–69 | GER 201 | 3”
  - equivalencies[CLEP-GERMAN-LANGUAGE|70]:  ⟵ “College Level German Language | 70 | GER 201 and GER 202 | 6”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50–69]:  ⟵ “College Level Spanish | 50–69 | SPA 201 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|70]:  ⟵ “College Level Spanish | 70 | SPA 201 and SPA 202 | 6”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POL 101 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | HIS 108 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | HIS 109 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSY 110 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | ECO 202 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | ECO 201 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC 101 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | HIS 104 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present | 50 | HIS 105 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | SOC 101 | 3”
  - … 10 more rows
### `754900cad34cbaf4` Hazard Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://hazard.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 9ebb73656d56)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `c348268253268e51` Hazard Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://hazard.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 9ebb73656d56)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `0cd1e326e9b7f8a1` Hazard Community and Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://hazard.kctcs.edu/dual-credit/eligibility-requirements.aspx (sha256 e9ffe409a24b)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “3.3 Addendum for Enrollment into Technical Education Dual Credit Courses: Students who do not have the minimum unweighted cumulative high school 2.0 GPA the”
### `66a453383f7f5ab8` Henderson Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://henderson.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 dae687744d5e)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `9988c76f5be5dc9a` Henderson Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://henderson.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 dae687744d5e)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `5fa50fa72b8553fb` Henderson Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://henderson.kctcs.edu/dual-credit/eligibility-requirements.aspx (sha256 3d77d5edd799)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “3.3 Addendum for Enrollment into Technical Education Dual Credit Courses: Students who do not have the minimum unweighted cumulative high school 2.0 GPA the”
### `5b27ba05eaa9e865` Hopkinsville Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://hopkinsville.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 a94efd6fa3b1)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `afa7671d17128553` Hopkinsville Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://hopkinsville.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 a94efd6fa3b1)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `7f37773f0b377d3f` Hopkinsville Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://hopkinsville.kctcs.edu/dual-credit/eligibility-requirements.aspx (sha256 7f8453297e8b)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “3.3 Addendum for Enrollment into Technical Education Dual Credit Courses: Students who do not have the minimum unweighted cumulative high school 2.0 GPA the”
### `2653d253d0bde8e6` Jefferson Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://jefferson.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 54807ca6d7b0)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `8f7b67f17df2931d` Jefferson Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://jefferson.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 54807ca6d7b0)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `ed7eae0035eeb68d` Kentucky State University — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.kysu.edu/documents/institutional-research/CDS%202025-2026.pdf (sha256 26f9eeda87dc)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 2500 ⟵ “Total first-time, first-year (degree-seeking) who applied           430         1947           80           43     2500”
  - admits: 2450 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     426         1943           80           1      2450”
  - enrolled: 397 ⟵ “Total first-time, first-year (degree-seeking) enrolled              146         213            32           6       397”
  - act_25..75: [15, 20, 24] ⟵ “ACT Composite                      15                        20                         24”
### `m3f7184f2a998932` Kentucky State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.kysu.edu/academics/dual-credit/stem-momentum.php (sha256 e82c52feb732)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 3, "tiers": 1}
  - per_credit_hour_charge: 99 ⟵ “For the 2026-2027 academic year, dual credit tuition is capped at $99 per credit hour.”
  - eligibility_tier: 2.5 ⟵ “Minimum 2.5 unweighted gpa”
  - eligibility_tier: 2.5 ⟵ “Have a minimum unweighted, cumulative high school GPA of 2.5.”
### `a8c4aff510b4f85c` Lindsey Wilson College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.lindsey.edu/admissions/cost-and-financial-aid/cost-of-attendance.cfm (sha256 b4e023745db3)
- checks: {"columns": 1, "rows": 8}
  - column:Tuition: 28656.0 ⟵ “Tuition | $ 28,656.00”
  - column:Tech Fee: 132.0 ⟵ “Tech Fee | $ 132.00”
  - column:Activity Fee: 188.0 ⟵ “Activity Fee | $ 188.00”
  - column:Transportation: 2000.0 ⟵ “Transportation | $ 2,000.00”
  - column:Housing: 3848.0 ⟵ “Housing | $ 3,848.00”
  - column:Food: 6742.0 ⟵ “Food | $ 6,742.00”
  - column:Misc/Personal: 6863.0 ⟵ “Misc/Personal | $ 6,863.00”
  - column:Books/Supplies/Equipment: 900.0 ⟵ “Books/Supplies/Equipment | $ 900.00”
### `ce393d40e5e71eb3` Lindsey Wilson College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.lindsey.edu/admissions/Transfer-Student.cfm (sha256 74b1fe2f8a5a)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “KCTCS Student Transfer Partnership Lindsey Wilson University recognizes completion of its general education requirement for those students transferring from the Kentucky Community & Technical College System (KCTCS) institutions who have completed requirements for General Education Full Certification* provided grades of C or higher have been earned in all relevant mathematics and English compositio”
### `0a56e17d67c0de1f` Madisonville Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://madisonville.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 a108523c1c8b)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `6bbd1dc616de98fb` Madisonville Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://madisonville.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 a108523c1c8b)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `m7d938383d7b76e7` Madisonville Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://madisonville.kctcs.edu/admissions/information-for/dual-credit/dc-getting-started.aspx (sha256 f9b3ef12df78)
- checks: {"fields": ["per_credit_hour_charges", "tuition_per_credit_hour"], "merged_pages": 2, "tiers": 2}
  - per_credit_hour_charge: 99 ⟵ “courses during the 2026-2027 year is $99 per credit hour.”
  - eligibility_tier: 2.5 ⟵ “have a high school GPA of 2.5. See the charts below for specific requirements.”
  - eligibility_tier: 2.0 ⟵ “A high school grade point average (GPA) of 2.0”
  - per_credit_hour_charge: 99 ⟵ “Tuition for 26-27 dual credit will be $99 per credit hour. Payment will be due by”
  - per_credit_hour_charge: 99 ⟵ “courses during the 2026-2027 year is $99 per credit hour.”
### `2f4d0582541e9718` Maysville Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://maysville.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 01da4154a4ca)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `ae9f7399573564b3` Maysville Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://maysville.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 01da4154a4ca)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `3753ca390c5d3b65` Northern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nku.edu/admissions-aid/financial-aid/scholarships/merit/index.html (sha256 e3ffb0e74a07)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “Excellence | 3.40-3.79 weighted HS GPA (KY residents); 3.40+ (Indiana and Ohio residents). Kentucky, Ohio and Indiana residents only. | $2,000”
### `52a1342a47ba0c1d` Northern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nku.edu/admissions-aid/financial-aid/scholarships/merit/index.html (sha256 e3ffb0e74a07)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Commonwealth | 3.00-3.39 weighted HS GPA. Kentucky, Ohio and Indiana residents only. | $1,000”
### `9a33985ea02929bd` Northern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nku.edu/admissions-aid/financial-aid/scholarships/merit/index.html (sha256 e3ffb0e74a07)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Norse Ambassadors | Graduating senior from a Boone, Campbell, or Kenton County highschool (public or private); application required.Kentucky residents only, limited to 10 awards. | $1,000”
### `a1d177a969f6a117` Northern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nku.edu/admissions-aid/financial-aid/scholarships/merit/index.html (sha256 e3ffb0e74a07)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 Housing Stipend ⟵ “Rogers Scholars | Successful completion of the program. | $2,000 Housing Stipend”
### `b70f83b76c5e74ca` Northern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nku.edu/admissions-aid/financial-aid/scholarships/merit/index.html (sha256 e3ffb0e74a07)
- checks: {"thresholds": null}
  - award_amount_text: Full Tuition + $6,000 Housing Stipend ⟵ “Presidential | 3.75+ weighted HS GPA and 34+ ACT/1490 SAT.All US residents eligible. | Full Tuition + $6,000 Housing Stipend”
### `da9bbd7ccec928d1` Northern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nku.edu/admissions-aid/financial-aid/scholarships/merit/index.html (sha256 e3ffb0e74a07)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “Founders | 3.80+ weighted HS GPA. Kentucky residents only. | $3,000”
### `dd250bc43963c671` Northern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nku.edu/admissions-aid/financial-aid/scholarships/merit/index.html (sha256 e3ffb0e74a07)
- checks: {"thresholds": null}
  - award_amount_text: $4,500 + $1,000 HousingStipend ⟵ “KY Governor's (GSP, GSA, and GSE) | KY Governor's Scholar with 3.0+ weighted HS GPA.Kentucky residents only. | $4,500 + $1,000 HousingStipend”
### `df5902240c083ea8` Northern Kentucky University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.nku.edu/admissions-aid/financial-aid/scholarships/merit/index.html (sha256 e3ffb0e74a07)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Loyal Norse – Dual Credit | Graduating senior who participated in the Votruba Young ScholarsAcademy or School-Based Scholars.Kentucky residents onlyMust enroll full-time, non-AOL | $1,000”
### `3daf6d58fe56146d` Owensboro Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://owensboro.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 8ba5fe41e533)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `b66f0fc055a91b82` Owensboro Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://owensboro.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 8ba5fe41e533)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `m862daf04d091c42` Owensboro Community and Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://owensboro.kctcs.edu/dual-credit/eligibility-requirements.aspx (sha256 0bebd2cc0594)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “3.3 Addendum for Enrollment into Technical Education Dual Credit Courses: Students who do not have the minimum unweighted cumulative high school 2.0 GPA the”
  - eligibility_tier: 2.0 ⟵ “GPA of 2.0 (a C average).”
### `0be7361b6d419440` Somerset Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://somerset.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 88138ce82990)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `b7fa13c11cc16bd6` Somerset Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://somerset.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 88138ce82990)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `313f58125894bb6c` Southcentral Kentucky Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://southcentral.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 b3f508569be2)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `f970b9a71f2e9ae7` Southcentral Kentucky Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://southcentral.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 b3f508569be2)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `05bef54596ceb06e` Southcentral Kentucky Community and Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://southcentral.kctcs.edu/admissions/information-for/dual-credit/dc-orientation.aspx (sha256 ab7ed68735c6)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 99 ⟵ “The Dual Credit tuition rate for the 2026-27 Academic Year is $99 per credit hour,”
### `0d77eda622ba90c4` Southeast Kentucky Community & Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://southeast.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 b6dd36c3d751)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `c594232213609526` Southeast Kentucky Community & Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://southeast.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 b6dd36c3d751)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `3d673138816d939b` Southeast Kentucky Community & Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://southeast.kctcs.edu/dual-credit/eligibility-requirements.aspx (sha256 b16eae2afca2)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “3.3 Addendum for Enrollment into Technical Education Dual Credit Courses: Students who do not have the minimum unweighted cumulative high school 2.0 GPA the”
### `2bc73934adaf4231` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships/ (sha256 d605a416898c)
- checks: {"thresholds": null}
  - award_amount_text: $18,000 per year ⟵ “Dean’s Scholarship | $18,000 per year | GPA range from 3.0-3.89.”
### `340c95dab3feb1bc` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships (sha256 186369a33aa8)
- checks: {"thresholds": null}
  - award_amount_text: Top 2 candidates are guaranteed a full-tuition scholarship in combination with other non-loan sources of aid. Other applicants admitted to the program may receive offers of James Graham Brown funding in variable amounts. ⟵ “James Graham Brown Scholars Program | Top 2 candidates are guaranteed a full-tuition scholarship in combination with other non-loan sources of aid. Other applicants admitted to the program may receive offers of James Graham Brown funding in variable amounts. | High school seniors only. 4.0 GPA; or 3”
  - gpa_requirement: High school seniors only. 4.0 GPA; or 3.6 GPA with test score (see test score requirements) ⟵ “James Graham Brown Scholars Program | Top 2 candidates are guaranteed a full-tuition scholarship in combination with other non-loan sources of aid. Other applicants admitted to the program may receive offers of James Graham Brown funding in variable amounts. | High school seniors only. 4.0 GPA; or 3”
### `5d58b44410b5c1be` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships (sha256 186369a33aa8)
- checks: {"thresholds": null}
  - award_amount_text: Additional $2,000+ per year ⟵ “Transfer Scholarship | Additional $2,000+ per year | Must have attended another college or university full-time for at least one semester and have 12 or more transferable credit hours.”
### `76279ea0e10bca2c` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships/ (sha256 d605a416898c)
- checks: {"thresholds": null}
  - award_amount_text: ACT 26-27 / SAT 1240-1300: $1,000ACT 28-29 / SAT 1310-1380: $1,500ACT 30+ / SAT 1390+ : $2,000 ⟵ “Test Score Bonus | ACT 26-27 / SAT 1240-1300: $1,000ACT 28-29 / SAT 1310-1380: $1,500ACT 30+ / SAT 1390+ : $2,000 | High school students with a verified test score equivalent to a 26 ACT/1240 SAT or higher are eligible for this award in addition to their academic scholarship. Amount will be added to”
### `9330927b6e6381bd` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships (sha256 186369a33aa8)
- checks: {"thresholds": null}
  - award_amount_text: $20,000 for GPA 3.89 or below $23,000 for GPA 3.9+ ⟵ “Diocese of Covington Guarantee | $20,000 for GPA 3.89 or below $23,000 for GPA 3.9+ | Presented to high school seniors graduating from a Diocese of Covington high school.”
### `b332ac86395ee40d` Thomas More University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/financial-aid-staff (sha256 d05dd385da1d)
- checks: {"thresholds": null}
  - test_requirement: ACT Email: [email protected]Phone: 859-344-3586 ⟵ “Adrianne HowsonAssistant Director of Financial Aid | Email: [email protected]Phone: 859-344-3586”
### `d968fe60cfb82909` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships/ (sha256 d605a416898c)
- checks: {"thresholds": null}
  - award_amount_text: $1,000-$5,000 based on academic achievement, community commitment, and interview with Campus Minister. Can be combined with academic scholarship. ⟵ “Bishop Roger J. Foys Ministry and Service Scholarship | $1,000-$5,000 based on academic achievement, community commitment, and interview with Campus Minister. Can be combined with academic scholarship. | For the Frassati and Acutis fellowships students must belong to a Christian Church community and”
  - gpa_requirement: For the Frassati and Acutis fellowships students must belong to a Christian Church community and be a practicing Roman Catholic. ⟵ “Bishop Roger J. Foys Ministry and Service Scholarship | $1,000-$5,000 based on academic achievement, community commitment, and interview with Campus Minister. Can be combined with academic scholarship. | For the Frassati and Acutis fellowships students must belong to a Christian Church community and”
### `e0d29b352cc11c08` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships (sha256 186369a33aa8)
- checks: {"thresholds": null}
  - award_amount_text: Amount varies based on academic accomplishments. Can be combined with academic scholarship. ⟵ “Msgr. Cleves University Honors Program | Amount varies based on academic accomplishments. Can be combined with academic scholarship. | High school seniors only. 3.5 GPA. Meeting the minimum criteria does not guarantee a scholarship offer. | None required | Deadline is January 1.Msgr.Cleves Universit”
  - gpa_requirement: High school seniors only. 3.5 GPA. Meeting the minimum criteria does not guarantee a scholarship offer. ⟵ “Msgr. Cleves University Honors Program | Amount varies based on academic accomplishments. Can be combined with academic scholarship. | High school seniors only. 3.5 GPA. Meeting the minimum criteria does not guarantee a scholarship offer. | None required | Deadline is January 1.Msgr.Cleves Universit”
### `e4da577abb47ee04` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships/ (sha256 d605a416898c)
- checks: {"thresholds": null}
  - award_amount_text: Full Tuition ⟵ “National Merit Finalists | Full Tuition | Certificate required.”
### `e5420c9ea14268e3` Thomas More University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/financial-aid-staff (sha256 d05dd385da1d)
- checks: {"thresholds": null}
  - test_requirement: ACT Email: [email protected]Phone: 859-344-3408 ⟵ “Vanessa RamirezDirector of Financial Aid | Email: [email protected]Phone: 859-344-3408”
### `e557f35753e05115` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships/ (sha256 d605a416898c)
- checks: {"thresholds": null}
  - award_amount_text: Full tuition award. ⟵ “Computer Information Systems Workship Program | Full tuition award. | High school seniors only. 3.5 GPA; or 3.0 GPA with test score (see test score requirements). Must major in Computer Information Systems or Management Information Systems. | 23 ACT / 1130 SAT / 74 CLT | Deadline to apply is March 1”
  - gpa_requirement: High school seniors only. 3.5 GPA; or 3.0 GPA with test score (see test score requirements). Must major in Computer Information Systems or Management Information Systems. ⟵ “Computer Information Systems Workship Program | Full tuition award. | High school seniors only. 3.5 GPA; or 3.0 GPA with test score (see test score requirements). Must major in Computer Information Systems or Management Information Systems. | 23 ACT / 1130 SAT / 74 CLT | Deadline to apply is March 1”
### `f042d6b0d26d302a` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships (sha256 186369a33aa8)
- checks: {"thresholds": null}
  - award_amount_text: $20,000 per year ⟵ “Presidential Scholarship | $20,000 per year | GPA of 3.9 or above.”
### `f31343b2a5db2556` Thomas More University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/financial-aid-staff/ (sha256 c3dc2e0eab0b)
- checks: {"thresholds": null}
  - test_requirement: ACT Email: [email protected]Phone: 859-344-3334 ⟵ “Marcus DunniganFinancial Aid Counselor | Email: [email protected]Phone: 859-344-3334”
### `f5373c0f2919441d` Thomas More University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/financial-aid-staff/ (sha256 c3dc2e0eab0b)
- checks: {"thresholds": null}
  - test_requirement: ACT Email: [email protected]Phone: 859-344-3425 ⟵ “Mr. Trey GarnerFinancial Aid Counselor | Email: [email protected]Phone: 859-344-3425”
### `f5d1555085871b7c` Thomas More University — awards 2027-28 [new] (labeled_in_source)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/scholarships (sha256 186369a33aa8)
- checks: {"thresholds": null}
  - award_amount_text: $16,000 per year ⟵ “Thomas More Award | $16,000 per year | Admitted to Thomas More University with GPA up to 2.99.”
### `m3b1f7d78e40d8d4` Thomas More University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/high-school-students-dual-credit-program/dual-credit-college-prep-program/ (sha256 f4a2697de3e6)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Must have a high school unweighted GPA of 3.0 or higher”
  - eligibility_tier: 2.79 ⟵ “Students admitted with an unweighted 2.5 to 2.79 GPA may only take one course at their high school in their first semester of dual credit until they have demonstrated academic success (maintained a 2.0+ TMU GPA at the end of the semester).”
  - eligibility_tier: 2.5 ⟵ “This special program admits students with an unweighted high school GPA of 2.5 or higher.”
### `65be87bd2af9efda` Union College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.unionky.edu/admissions-aid/cost-aid/tuition-fees (sha256 4a42303315fc)
- checks: {"columns": 1, "components_reconcile": true, "rows": 10}
  - column:Tuition: 29600 ⟵ “Tuition | $ 14,800 | $ 29,600”
  - column:Comprehensive Fee: 2400 ⟵ “Comprehensive Fee | $ 1,200 | $ 2,400”
  - column:Laundry Fee: 110 ⟵ “Laundry Fee |  | $ 110”
  - column:Traditional Room: 3900 ⟵ “Traditional Room | $ 1,950 | $ 3,900”
  - column:Traditional Meal Plan: 5300 ⟵ “Traditional Meal Plan | $ 2,650 | $ 5,300”
  - column:*Books/Supplies: 1500 ⟵ “*Books/Supplies | $ 750 | $ 1,500”
  - column:*Personal Expense: 3000 ⟵ “*Personal Expense | $ 1,500 | $ 3,000”
  - column:*Transportation: 2000 ⟵ “*Transportation | $ 1,000 | $ 2,000”
  - column:*Loan Fee: 102 ⟵ “*Loan Fee | $ 51 | $ 102”
  - column:Total: 47912 ⟵ “Total | $ 23,901 | $ 47,912”
### `a30915febb910058` Union College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.unionky.edu/admissions-aid/cost-aid/tuition-fees (sha256 4a42303315fc)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 29600 ⟵ “Tuition | $ 14,800 | $ 29,600”
  - column:Comprehensive Fee: 2400 ⟵ “Comprehensive Fee | $ 1,200 | $ 2,400”
  - column:*Books/Supplies: 1500 ⟵ “*Books/Supplies | $ 750 | $ 1,500”
  - column:*Personal Expense: 3000 ⟵ “*Personal Expense | $ 1,500 | $ 3,000”
  - column:*Transportation: 2000 ⟵ “*Transportation | $ 1,000 | $ 2,000”
  - column:*Loan Fee: 102 ⟵ “*Loan Fee | $ 51 | $ 102”
  - column:Total: 38602 ⟵ “Total | $ 19,301 | $ 38,602”
### `03858115fcb725d2` Union College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.unionky.edu/admissions-aid/undergraduate/dual-credit-program (sha256 e02248a71ea7)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “3.0 GPA or higher”
  - per_credit_hour_charge: 91 ⟵ “$91 per credit hour (may vary slightly each academic year).”
### `732bf16a37786e5f` University of Kentucky — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://studentsuccess.uky.edu/financial-aid-and-scholarships/estimated-cost-attendance (sha256 6fa3970af38f)
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees1,2,3,4,5: 35846 ⟵ “Tuition and Fees1,2,3,4,5 | 35,846 | 35,846 | 35,846 | 35,846”
  - on_campus:Food and Housing: 17048 ⟵ “Food and Housing | 17,048 | 14,716 | 9,770 | 13,880”
  - on_campus:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - on_campus:Travel: 3418 ⟵ “Travel | 3,418 | 3,582 | 6,536 | 3,418”
  - on_campus:Personal: 3240 ⟵ “Personal | 3,240 | 3,240 | 3,240 | 3,240”
  - on_campus:Loan Origination: 86 ⟵ “Loan Origination | 86 | 86 | 86 | 86”
  - on_campus:TOTAL: 60838 ⟵ “TOTAL | 60,838 | 58,670 | 56,678 | 57,670”
  - off_campus_not_with_family:Tuition and Fees1,2,3,4,5: 35846 ⟵ “Tuition and Fees1,2,3,4,5 | 35,846 | 35,846 | 35,846 | 35,846”
  - off_campus_not_with_family:Food and Housing: 14716 ⟵ “Food and Housing | 17,048 | 14,716 | 9,770 | 13,880”
  - off_campus_not_with_family:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - off_campus_not_with_family:Travel: 3582 ⟵ “Travel | 3,418 | 3,582 | 6,536 | 3,418”
  - off_campus_not_with_family:Personal: 3240 ⟵ “Personal | 3,240 | 3,240 | 3,240 | 3,240”
  - off_campus_not_with_family:Loan Origination: 86 ⟵ “Loan Origination | 86 | 86 | 86 | 86”
  - off_campus_not_with_family:TOTAL: 58670 ⟵ “TOTAL | 60,838 | 58,670 | 56,678 | 57,670”
  - with_parents_or_family:Tuition and Fees1,2,3,4,5: 35846 ⟵ “Tuition and Fees1,2,3,4,5 | 35,846 | 35,846 | 35,846 | 35,846”
  - with_parents_or_family:Food and Housing: 9770 ⟵ “Food and Housing | 17,048 | 14,716 | 9,770 | 13,880”
  - with_parents_or_family:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - with_parents_or_family:Travel: 6536 ⟵ “Travel | 3,418 | 3,582 | 6,536 | 3,418”
  - with_parents_or_family:Personal: 3240 ⟵ “Personal | 3,240 | 3,240 | 3,240 | 3,240”
  - with_parents_or_family:Loan Origination: 86 ⟵ “Loan Origination | 86 | 86 | 86 | 86”
  - with_parents_or_family:TOTAL: 56678 ⟵ “TOTAL | 60,838 | 58,670 | 56,678 | 57,670”
  - on_campus:Tuition and Fees1,2,3,4,5: 35846 ⟵ “Tuition and Fees1,2,3,4,5 | 35,846 | 35,846 | 35,846 | 35,846”
  - on_campus:Food and Housing: 13880 ⟵ “Food and Housing | 17,048 | 14,716 | 9,770 | 13,880”
  - on_campus:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - on_campus:Travel: 3418 ⟵ “Travel | 3,418 | 3,582 | 6,536 | 3,418”
  - … 3 more rows
### `90312f1a17091c7d` University of Kentucky — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://studentsuccess.uky.edu/financial-aid-and-scholarships/estimated-cost-attendance (sha256 6fa3970af38f)
- checks: {"columns": 4, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition and Fees1,2,3,4,5: 14178 ⟵ “Tuition and Fees1,2,3,4,5 | 14,178 | 14,178 | 14,178 | 14,178”
  - on_campus:Food and Housing: 17048 ⟵ “Food and Housing | 17,048 | 14,716 | 9,770 | 13,880”
  - on_campus:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - on_campus:Travel: 2592 ⟵ “Travel | 2,592 | 2,756 | 6,536 | 2,592”
  - on_campus:Personal: 3240 ⟵ “Personal | 3,240 | 3,240 | 3,240 | 3,240”
  - on_campus:Loan Origination: 86 ⟵ “Loan Origination | 86 | 86 | 86 | 86”
  - on_campus:TOTAL: 38344 ⟵ “TOTAL | 38,344 | 36,176 | 35,010 | 35,176”
  - off_campus_not_with_family:Tuition and Fees1,2,3,4,5: 14178 ⟵ “Tuition and Fees1,2,3,4,5 | 14,178 | 14,178 | 14,178 | 14,178”
  - off_campus_not_with_family:Food and Housing: 14716 ⟵ “Food and Housing | 17,048 | 14,716 | 9,770 | 13,880”
  - off_campus_not_with_family:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - off_campus_not_with_family:Travel: 2756 ⟵ “Travel | 2,592 | 2,756 | 6,536 | 2,592”
  - off_campus_not_with_family:Personal: 3240 ⟵ “Personal | 3,240 | 3,240 | 3,240 | 3,240”
  - off_campus_not_with_family:Loan Origination: 86 ⟵ “Loan Origination | 86 | 86 | 86 | 86”
  - off_campus_not_with_family:TOTAL: 36176 ⟵ “TOTAL | 38,344 | 36,176 | 35,010 | 35,176”
  - with_parents_or_family:Tuition and Fees1,2,3,4,5: 14178 ⟵ “Tuition and Fees1,2,3,4,5 | 14,178 | 14,178 | 14,178 | 14,178”
  - with_parents_or_family:Food and Housing: 9770 ⟵ “Food and Housing | 17,048 | 14,716 | 9,770 | 13,880”
  - with_parents_or_family:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - with_parents_or_family:Travel: 6536 ⟵ “Travel | 2,592 | 2,756 | 6,536 | 2,592”
  - with_parents_or_family:Personal: 3240 ⟵ “Personal | 3,240 | 3,240 | 3,240 | 3,240”
  - with_parents_or_family:Loan Origination: 86 ⟵ “Loan Origination | 86 | 86 | 86 | 86”
  - with_parents_or_family:TOTAL: 35010 ⟵ “TOTAL | 38,344 | 36,176 | 35,010 | 35,176”
  - on_campus:Tuition and Fees1,2,3,4,5: 14178 ⟵ “Tuition and Fees1,2,3,4,5 | 14,178 | 14,178 | 14,178 | 14,178”
  - on_campus:Food and Housing: 13880 ⟵ “Food and Housing | 17,048 | 14,716 | 9,770 | 13,880”
  - on_campus:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - on_campus:Travel: 2592 ⟵ “Travel | 2,592 | 2,756 | 6,536 | 2,592”
  - … 3 more rows
### `mb484f84d0d08603` University of Kentucky — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admission.uky.edu/sites/default/files/2025-09/earlyelementary_25-26.pdf (sha256 012456417e52)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 13}
  - residency_requirement_credits: 36 ⟵ “Degree Requirements To fulfill residency requirements, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Degree Requirements To fulfill residency requirements, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Degree Requirements To meet residency requirements, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Additionally, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Degree Requirements To fulfill residency requirements, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Degree Requirements To fulfill residency requirements, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Degree Requirements To fulfill residency requirements, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Degree Requirements To fulfill residency requirements, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Degree Requirements 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Degree Requirements 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Additionally, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Additionally, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
  - residency_requirement_credits: 36 ⟵ “Additionally, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
### `06699ddb3d354bfe` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid (sha256 788ed8a99248)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: Full in-state tuitionUp to an additional $10,000 per year to supplement educational expenses ⟵ “Martin Luther King Scholarship | Full in-state tuitionUp to an additional $10,000 per year to supplement educational expenses | 3.5 | 1160 / 24 | Kentucky and Southern Indiana students with a demonstrated commitment to ethical leadership, social change, and public service are encouraged to apply. Al”
  - gpa_requirement: 3.5 ⟵ “Martin Luther King Scholarship | Full in-state tuitionUp to an additional $10,000 per year to supplement educational expenses | 3.5 | 1160 / 24 | Kentucky and Southern Indiana students with a demonstrated commitment to ethical leadership, social change, and public service are encouraged to apply. Al”
  - test_requirement: ACT 1160 / 24 / SAT 1160 / 24 ⟵ “Martin Luther King Scholarship | Full in-state tuitionUp to an additional $10,000 per year to supplement educational expenses | 3.5 | 1160 / 24 | Kentucky and Southern Indiana students with a demonstrated commitment to ethical leadership, social change, and public service are encouraged to apply. Al”
### `09273ad8250af948` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid (sha256 788ed8a99248)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $1,000-$5,000 ⟵ “Trustees' Competitive Scholarships | $1,000-$5,000 | 3.5* | 1390 / 31 | Enhancement of admission-based Trustees' Scholarship.”
  - gpa_requirement: 3.5* ⟵ “Trustees' Competitive Scholarships | $1,000-$5,000 | 3.5* | 1390 / 31 | Enhancement of admission-based Trustees' Scholarship.”
  - test_requirement: ACT 1390 / 31 / SAT 1390 / 31 ⟵ “Trustees' Competitive Scholarships | $1,000-$5,000 | 3.5* | 1390 / 31 | Enhancement of admission-based Trustees' Scholarship.”
### `0f76a2c988d756ea` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid (sha256 788ed8a99248)
- checks: {"thresholds": null}
  - award_amount_text: Various amounts; KHEEA.com ⟵ “Kentucky College Educational Excellence Scholarship (KEES) | Various amounts; KHEEA.com | Scholarship | Based on weighted GPA and SAT/ACT scores; no scholarship application required.”
### `237ed0f82c84df61` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid (sha256 788ed8a99248)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $16,000 ⟵ “Henry Vogt Scholarship | $16,000 | 3.5* | 1390 / 31 | Approximately 150 Vogt Scholars awarded each year.”
  - gpa_requirement: 3.5* ⟵ “Henry Vogt Scholarship | $16,000 | 3.5* | 1390 / 31 | Approximately 150 Vogt Scholars awarded each year.”
  - test_requirement: ACT 1390 / 31 / SAT 1390 / 31 ⟵ “Henry Vogt Scholarship | $16,000 | 3.5* | 1390 / 31 | Approximately 150 Vogt Scholars awarded each year.”
### `2d0c16617a67dfc1` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/out-state-scholarships-aid (sha256 9949a3b2c98c)
- checks: {"thresholds": null}
  - award_amount_text: $400 ⟵ “Federal Supplemental Educational Opportunity Grant (FSEOG) | $400 | Need-based grant”
### `334aba10a6e7e639` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid (sha256 788ed8a99248)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: Full in-state tuition and fully funded domestic and international travel opportunities—valued at over $10,000 ⟵ “McConnell Scholarship | Full in-state tuition and fully funded domestic and international travel opportunities—valued at over $10,000 | 3.5 | 1230 / 26 | Kentucky students with a strong record of commitment to leadership, scholarship and service. All scholarships are open to all eligible students re”
  - gpa_requirement: 3.5 ⟵ “McConnell Scholarship | Full in-state tuition and fully funded domestic and international travel opportunities—valued at over $10,000 | 3.5 | 1230 / 26 | Kentucky students with a strong record of commitment to leadership, scholarship and service. All scholarships are open to all eligible students re”
  - test_requirement: ACT 1230 / 26 / SAT 1230 / 26 ⟵ “McConnell Scholarship | Full in-state tuition and fully funded domestic and international travel opportunities—valued at over $10,000 | 3.5 | 1230 / 26 | Kentucky students with a strong record of commitment to leadership, scholarship and service. All scholarships are open to all eligible students re”
### `58346b33e481f8b6` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/out-state-scholarships-aid (sha256 9949a3b2c98c)
- checks: {"thresholds": null}
  - award_amount_text: $740-$7,395 ⟵ “Federal Pell Grant | $740-$7,395 | Need-based grant”
### `5e720306add4303e` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid (sha256 788ed8a99248)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $22,000 for in-state students ⟵ “Grawemeyer Scholarship | $22,000 for in-state students | 3.5 | 1160 / 24 | Kentucky and out-of-state students with an interest in undergraduate research. All scholarships are open to all eligible students regardless of race, color, religion, national origin, sex, disability or age.”
  - gpa_requirement: 3.5 ⟵ “Grawemeyer Scholarship | $22,000 for in-state students | 3.5 | 1160 / 24 | Kentucky and out-of-state students with an interest in undergraduate research. All scholarships are open to all eligible students regardless of race, color, religion, national origin, sex, disability or age.”
  - test_requirement: ACT 1160 / 24 / SAT 1160 / 24 ⟵ “Grawemeyer Scholarship | $22,000 for in-state students | 3.5 | 1160 / 24 | Kentucky and out-of-state students with an interest in undergraduate research. All scholarships are open to all eligible students regardless of race, color, religion, national origin, sex, disability or age.”
### `87270bb8b0c05a71` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/out-state-scholarships-aid (sha256 9949a3b2c98c)
- checks: {"thresholds": null}
  - award_amount_text: Up to $6,500 ⟵ “Federal Work-Study (FWS) | Up to $6,500 | Need-based, on-campus employment”
### `9670cb2cabf33a50` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/kentucky-southern-indiana-scholarships-aid (sha256 788ed8a99248)
- checks: {"thresholds": null}
  - award_amount_text: $5,300 ⟵ “Kentucky College Access Program (CAP) Grant* | $5,300 | Need-based grant | Applicants must be Pell Gant eligible and meet the state eligibility requirements. Funds awarded on a first come, first served basis.”
### `9d3f2093e254fe7c` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/out-state-scholarships-aid (sha256 9949a3b2c98c)
- checks: {"thresholds": null}
  - award_amount_text: Various amounts, up to cost of attendance (minus other awards) ⟵ “Parent PLUS Loan | Various amounts, up to cost of attendance (minus other awards) | Loan”
### `a042e9156d11e741` University of Louisville — awards 2026-27 [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/out-state-scholarships-aid (sha256 9949a3b2c98c)
- checks: {"thresholds": null}
  - award_amount_text: $5,500 maximum first year ⟵ “Federal Direct Loans | $5,500 maximum first year | Subsidized and unsubsidized loans”
### `fb521c0bf21388f8` University of Louisville — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://louisville.edu/admissions/apply/non-degree-applicants/dual-credit-students (sha256 f621684f07dd)
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 99 ⟵ “$99 per credit hour.”
### `4c94544628db9e75` University of Pikeville — admissions_metrics 2025-26 [new] (labeled_in_source)
- source: https://www.upike.edu/wp-content/uploads/2025/11/common-data-set-2025.pdf (sha256 1eee3898d950)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 2363 ⟵ “Total first-time, first-year (degree-seeking) who applied                                   2,363”
  - admits: 2119 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                             2,119”
  - enrolled: 336 ⟵ “Total first-time, first-year (degree-seeking) enrolled                                       336”
  - act_25..75: [18, 21, 24] ⟵ “ACT Composite                                          18                       21                  24                  21.0”
### `4ef597b0e3e3750d` University of Pikeville — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.upike.edu/undergraduate/admissions/transfer-to-upike/ (sha256 c90d50b0e9c9)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “In order for UPIKE to award a degree, the student must complete at least 50% of their major and their last 30 credit hours with us.”
### `177713a32f9d5e56` West Kentucky Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://westkentucky.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 1f7c2d7948af)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `35650cbcf3b852f7` West Kentucky Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://westkentucky.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 1f7c2d7948af)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `1b9cd94769210c2f` Western Kentucky University — academic_programs 2026-27 · program_key=journalism-bachelor-of-arts-736p-736 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/journalism-ba/ (sha256 255ceb1183cf)
- checks: {"courses": 45, "groups": 3, "groups_skipped": 0}
  - program_name: Journalism, Bachelor of Arts (736P, 736) ⟵ “Journalism, Bachelor of Arts (736P, 736) < Western Kentucky University”
### `2209d779c9f3beba` Western Kentucky University — academic_programs 2026-27 · program_key=english-for-secondary-teachers-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-secondary-teachers-ba/ (sha256 fb8c90f7b744)
- checks: {"courses": 69, "groups": 7, "groups_skipped": 0}
  - program_name: English for Secondary Teachers, Bachelor of Arts ⟵ “English for Secondary Teachers, Bachelor of Arts (561) < Western Kentucky University”
### `26368994f4a687e3` Western Kentucky University — academic_programs 2026-27 · program_key=mathematical-economics-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/mathematical-economics-bs/ (sha256 195ac45cd091)
- checks: {"courses": 33, "groups": 3, "groups_skipped": 0}
  - program_name: Mathematical Economics, Bachelor of Science ⟵ “Mathematical Economics, Bachelor of Science (731) < Western Kentucky University”
### `28658820a22ba31e` Western Kentucky University — academic_programs 2026-27 · program_key=spanish-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
- checks: {"courses": 63, "groups": 12, "groups_skipped": 0}
  - program_name: Spanish, Bachelor of Arts ⟵ “Spanish, Bachelor of Arts (778) < Western Kentucky University”
### `2c3ac196bf5a8abc` Western Kentucky University — academic_programs 2026-27 · program_key=social-studies-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/social-studies-ba/ (sha256 02fc45f9924f)
- checks: {"courses": 51, "groups": 5, "groups_skipped": 0}
  - program_name: Social Studies, Bachelor of Arts ⟵ “Social Studies, Bachelor of Arts (592) < Western Kentucky University”
### `2d52076228798bcd` Western Kentucky University — academic_programs 2026-27 · program_key=visual-journalism-and-photography-bachelor-of-arts-752p-752 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/visual-journalism-photography-ba/ (sha256 55cb5defcc5a)
- checks: {"courses": 53, "groups": 6, "groups_skipped": 0}
  - program_name: Visual Journalism and Photography, Bachelor of Arts (752P, 752) ⟵ “Visual Journalism and Photography, Bachelor of Arts (752P, 752) < Western Kentucky University”
### `3337d61c79c4dc91` Western Kentucky University — academic_programs 2026-27 · program_key=visual-studies-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-studies-ba/ (sha256 fcd2c45cf314)
- checks: {"courses": 229, "groups": 6, "groups_skipped": 0}
  - program_name: Visual Studies, Bachelor of Arts ⟵ “Visual Studies, Bachelor of Arts (509) < Western Kentucky University”
### `5ac682c3db414390` Western Kentucky University — academic_programs 2026-27 · program_key=professional-legal-studies-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/paralegal-studies-ba/ (sha256 9c6c23742c44)
- checks: {"courses": 33, "groups": 2, "groups_skipped": 0}
  - program_name: Professional Legal Studies, Bachelor of Arts ⟵ “Professional Legal Studies, Bachelor of Arts (6000) < Western Kentucky University”
### `68fdbf8ad078d8cc` Western Kentucky University — academic_programs 2026-27 · program_key=theatre-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/theatre-ba/ (sha256 1b9c0be3c605)
- checks: {"courses": 30, "groups": 4, "groups_skipped": 0}
  - program_name: Theatre, Bachelor of Arts ⟵ “Theatre, Bachelor of Arts (798) < Western Kentucky University”
### `7da7680d23893130` Western Kentucky University — academic_programs 2026-27 · program_key=user-experience-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/user-experience-bs/ (sha256 eed3996a11f0)
- checks: {"courses": 19, "groups": 7, "groups_skipped": 0}
  - program_name: User Experience, Bachelor of Science ⟵ “User Experience, Bachelor of Science (5017) < Western Kentucky University”
### `8bdc215b6f0640d8` Western Kentucky University — academic_programs 2026-27 · program_key=english-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
- checks: {"courses": 82, "groups": 10, "groups_skipped": 0}
  - program_name: English, Bachelor of Arts ⟵ “English, Bachelor of Arts (662) < Western Kentucky University”
### `8d0c61a26775f5ac` Western Kentucky University — academic_programs 2026-27 · program_key=criminology-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/criminology-ba/ (sha256 5191dda112b1)
- checks: {"courses": 64, "groups": 2, "groups_skipped": 0}
  - program_name: Criminology, Bachelor of Arts ⟵ “Criminology, Bachelor of Arts (627) < Western Kentucky University”
### `8d5c062633daa259` Western Kentucky University — academic_programs 2026-27 · program_key=anthropology-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
- checks: {"courses": 33, "groups": 9, "groups_skipped": 0}
  - program_name: Anthropology, Bachelor of Arts ⟵ “Anthropology, Bachelor of Arts (608) < Western Kentucky University”
### `8e036047ec2ab0da` Western Kentucky University — academic_programs 2026-27 · program_key=legal-studies-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/legal-studies-ba/ (sha256 e4ac270afc7b)
- checks: {"courses": 64, "groups": 1, "groups_skipped": 0}
  - program_name: Legal Studies, Bachelor of Arts ⟵ “Legal Studies, Bachelor of Arts (6001) < Western Kentucky University”
### `8e56de3bbb94bb9c` Western Kentucky University — academic_programs 2026-27 · program_key=integrated-advertising-public-relations-bachelor-of-arts-753p-753 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/integrated-advertising-pr-ba/ (sha256 894e3bc19fa7)
- checks: {"courses": 73, "groups": 3, "groups_skipped": 0}
  - program_name: Integrated Advertising & Public Relations, Bachelor of Arts (753P, 753) ⟵ “Integrated Advertising & Public Relations, Bachelor of Arts (753P, 753) < Western Kentucky University”
### `9412f99afb891e77` Western Kentucky University — academic_programs 2026-27 · program_key=film-production-bachelor-of-fine-arts-530p-530 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/film-production-bfa/ (sha256 abc000f8c136)
- checks: {"courses": 28, "groups": 1, "groups_skipped": 0}
  - program_name: Film Production, Bachelor of Fine Arts (530P, 530) ⟵ “Film Production, Bachelor of Fine Arts (530P, 530) < Western Kentucky University”
### `a3ad8b360c59c1ee` Western Kentucky University — academic_programs 2026-27 · program_key=political-science-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/political-science-ba/ (sha256 45b7e630d76b)
- checks: {"courses": 32, "groups": 1, "groups_skipped": 0}
  - program_name: Political Science, Bachelor of Arts ⟵ “Political Science, Bachelor of Arts (686) < Western Kentucky University”
### `ab11232eb6db05d6` Western Kentucky University — academic_programs 2026-27 · program_key=business-economics-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/business-economics-bs/ (sha256 367d4d265754)
- checks: {"courses": 21, "groups": 5, "groups_skipped": 0}
  - program_name: Business Economics, Bachelor of Science ⟵ “Business Economics, Bachelor of Science (724) < Western Kentucky University”
### `b9c3fd8de8d7e1b9` Western Kentucky University — academic_programs 2026-27 · program_key=communication-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/communication-ba/ (sha256 9e1978297b5b)
- checks: {"courses": 77, "groups": 1, "groups_skipped": 0}
  - program_name: Communication, Bachelor of Arts ⟵ “Communication, Bachelor of Arts (6003) < Western Kentucky University”
### `baae9b667257e301` Western Kentucky University — academic_programs 2026-27 · program_key=philosophy-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
- checks: {"courses": 86, "groups": 12, "groups_skipped": 0}
  - program_name: Philosophy, Bachelor of Arts ⟵ “Philosophy, Bachelor of Arts (745) < Western Kentucky University”
### `bbcf0e830fa8cbe2` Western Kentucky University — academic_programs 2026-27 · program_key=religious-studies-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/religious-studies-ba/ (sha256 a798e0130e89)
- checks: {"courses": 34, "groups": 5, "groups_skipped": 0}
  - program_name: Religious Studies, Bachelor of Arts ⟵ “Religious Studies, Bachelor of Arts (769) < Western Kentucky University”
### `c2d777b49d3f5895` Western Kentucky University — academic_programs 2026-27 · program_key=economics-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/economics-ba/ (sha256 1e2e2c84e96a)
- checks: {"courses": 9, "groups": 2, "groups_skipped": 0}
  - program_name: Economics, Bachelor of Arts ⟵ “Economics, Bachelor of Arts (638) < Western Kentucky University”
### `c71ba8843a86650c` Western Kentucky University — academic_programs 2026-27 · program_key=chinese-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
- checks: {"courses": 38, "groups": 9, "groups_skipped": 0}
  - program_name: Chinese, Bachelor of Arts ⟵ “Chinese, Bachelor of Arts (624) < Western Kentucky University”
### `c9c16fd847110aa3` Western Kentucky University — academic_programs 2026-27 · program_key=film-bachelor-of-arts-667p-667 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/film-ba/ (sha256 d1378fd4bf29)
- checks: {"courses": 36, "groups": 4, "groups_skipped": 0}
  - program_name: Film, Bachelor of Arts (667P, 667) ⟵ “Film, Bachelor of Arts (667P, 667) < Western Kentucky University”
### `cfd298d11c8ac21b` Western Kentucky University — academic_programs 2026-27 · program_key=broadcasting-bachelor-of-arts-726p-726 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/broadcasting-ba/ (sha256 170d38970f13)
- checks: {"courses": 65, "groups": 1, "groups_skipped": 0}
  - program_name: Broadcasting, Bachelor of Arts (726P, 726) ⟵ “Broadcasting, Bachelor of Arts (726P, 726) < Western Kentucky University”
### `d1ff12b1ef0581b4` Western Kentucky University — academic_programs 2026-27 · program_key=interior-design-and-fashion-studies-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/interior-design-fashion-studies-bs/ (sha256 7a57d16420c2)
- checks: {"courses": 78, "groups": 2, "groups_skipped": 0}
  - program_name: Interior Design and Fashion Studies, Bachelor of Science ⟵ “Interior Design and Fashion Studies, Bachelor of Science (5020) < Western Kentucky University”
### `e0b8203f6220dbcb` Western Kentucky University — academic_programs 2026-27 · program_key=accounting-bachelor-of-science [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/accounting/accounting-bs/ (sha256 5dadf9a49ed6)
- checks: {"courses": 32, "groups": 3, "groups_skipped": 0}
  - program_name: Accounting, Bachelor of Science ⟵ “Accounting, Bachelor of Science (602) < Western Kentucky University”
### `01d37141b4665f06` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-track-31-hours-any-philosophy-phil-course-that-is-not-already-countin [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: RELS 242 ⟵ “RELS 242 - The Meaning of Life; Atheism to Zen”
  - courses: RELS 317 ⟵ “RELS 317 - Confucianism”
  - courses: RELS 318 ⟵ “RELS 318 - Daoism”
### `040952e3a062e56b` Western Kentucky University — degree_requirements 2026-27 · program_key=theatre-bachelor-of-arts · requirement_key=program-requirements-45-hours-performance [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/theatre-ba/ (sha256 1b9c0be3c605)
  - courses: THEA 101 ⟵ “THEA 101 - Acting I (3 credit hours)”
  - courses: PERF 205 ⟵ “PERF 205 - Voice and Movement for the Stage (1 credit hour)”
  - courses: THEA 300 ⟵ “THEA 300 - Acting II (3 credit hours)”
  - courses: THEA 301 ⟵ “THEA 301 - Acting III (3 credit hours)”
  - courses: THEA 303 ⟵ “THEA 303 - Acting for the Camera (3 credit hours)”
  - courses: PERF 350 ⟵ “PERF 350 - Voice and Diction for the Theatre (1 credit hour)”
  - courses: THEA 371 ⟵ “THEA 371 - Directing I (3 credit hours)”
  - courses: PERF 401 ⟵ “PERF 401 - Solo Performance (3 credit hours)”
  - courses: DANC 235 ⟵ “DANC 235 - Dance Improvisation (2 credit hours)”
### `04512327b1eb7a0f` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=literature-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 204 ⟵ “ENG 204 - English Language”
  - courses: ENG 299 ⟵ “ENG 299 - Introduction to English Studies”
  - courses: ENG 381 ⟵ “ENG 381 - Survey of British Literature I”
  - courses: ENG 382 ⟵ “ENG 382 - Survey of British Literature II”
  - courses: ENG 385 ⟵ “ENG 385 - Studies in World Literature”
  - courses: ENG 391 ⟵ “ENG 391 - Survey of American Literature I”
  - courses: ENG 392 ⟵ “ENG 392 - Survey of American Literature II”
  - courses: ENG 416 ⟵ “ENG 416 - Literature/EST Capstone (senior capstone, which should be taken in the last semester of coursework)”
  - courses: ENG 203 ⟵ “ENG 203 - Creative Writing”
  - courses: ENG 306 ⟵ “ENG 306 - Business Writing”
  - courses: ENG 307 ⟵ “ENG 307 - Technical Writing”
  - courses: ENG 401 ⟵ “ENG 401 - Advanced Composition”
  - courses: ENG 410 ⟵ “ENG 410 - Composition Theory and Practice in Writing Instruction”
  - courses: ENG 212 ⟵ “ENG 212 - Introduction to Digital Texts and Media”
  - courses: ENG 301 ⟵ “ENG 301 - Argument and Analysis in Written Discourse”
  - courses: ENG 412 ⟵ “ENG 412 - Theories of Rhetoric and Persuasive Writing”
### `06ecbb01a518d21b` Western Kentucky University — degree_requirements 2026-27 · program_key=english-for-secondary-teachers-bachelor-of-arts · requirement_key=program-requirements-54-hours-literature-of-diversity [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-secondary-teachers-ba/ (sha256 fb8c90f7b744)
  - courses: ENG 360 ⟵ “ENG 360 - Queer Literature”
  - courses: ENG 370 ⟵ “ENG 370 - U.S. Ethnic Literature”
  - courses: ENG 393 ⟵ “ENG 393 - African American Literature”
  - courses: ENG 497 ⟵ “ENG 497 - Women’s Literature”
### `0a8c4fd0807ba03f` Western Kentucky University — degree_requirements 2026-27 · program_key=business-economics-bachelor-of-science · requirement_key=program-requirements-72-hours-economics-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/business-economics-bs/ (sha256 367d4d265754)
  - section: program-requirements-72-hours-economics-electives ⟵ “Program Requirements (72 hours) — Economics Electives”
### `1060c028cc06fc42` Western Kentucky University — degree_requirements 2026-27 · program_key=religious-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-senior-seminar [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/religious-studies-ba/ (sha256 a798e0130e89)
  - courses: RELS 496 ⟵ “RELS 496 - Senior Seminar”
### `12059ac1cbf1021b` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-studies-bachelor-of-arts · requirement_key=art-education-concentration-required-art-education-pedagogy-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-studies-ba/ (sha256 fcd2c45cf314)
  - courses: ART 311 ⟵ “ART 311 - Foundations of Art Education and Methods I”
  - courses: ART 411 ⟵ “ART 411 - Foundations of Art Education and Methods II”
  - courses: ART 413 ⟵ “ART 413 - Foundations of Art Education and Methods III”
### `127ae0f3ea5377be` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=archaeology-concentration-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
  - section: archaeology-concentration-electives ⟵ “Archaeology Concentration — Electives”
### `15bf640ff285a5d3` Western Kentucky University — degree_requirements 2026-27 · program_key=theatre-bachelor-of-arts · requirement_key=program-requirements-45-hours-required-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/theatre-ba/ (sha256 1b9c0be3c605)
  - courses: PERF 175 ⟵ “PERF 175 - University Experience: Performing Arts”
### `1f2b39f784c0d7f1` Western Kentucky University — degree_requirements 2026-27 · program_key=religious-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-world-religions [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/religious-studies-ba/ (sha256 a798e0130e89)
  - courses: RELS 102 ⟵ “RELS 102 - World Religions”
### `26d79b76e735d23d` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-studies-bachelor-of-arts · requirement_key=professional-education-requirements-an-additional-25-semester-hours-in-professio [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-studies-ba/ (sha256 fcd2c45cf314)
  - courses: EDU 250 ⟵ “EDU 250 - Discover Teaching: Introduction to Teacher Education”
  - courses: PSY 310 ⟵ “PSY 310 - Educational Psychology: Development and Learning”
  - courses: EDU 350 ⟵ “EDU 350 - Student Diversity and Differentiation”
  - courses: EDU 360 ⟵ “EDU 360 - Behavior and Classroom Management in Education”
  - courses: LTCY 497 ⟵ “LTCY 497 - Literacy Competencies for Middle and High School Classroom Teachers”
  - courses: EDU 489 ⟵ “EDU 489 - Student Teaching Seminar”
  - courses: ELED 490 ⟵ “ELED 490 - Student Teaching”
  - courses: SEC 490 ⟵ “SEC 490 - Student Teaching”
  - courses: MGE 490 ⟵ “MGE 490 - Student Teaching”
### `27c279d8c156f7f0` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=major-in-chinese-with-teacher-certification-elective-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
  - section: major-in-chinese-with-teacher-certification-elective-courses ⟵ “Major in Chinese with Teacher Certification — Elective Courses”
### `2953c3692a2eb5a2` Western Kentucky University — degree_requirements 2026-27 · program_key=english-for-secondary-teachers-bachelor-of-arts · requirement_key=program-requirements-54-hours-writing-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-secondary-teachers-ba/ (sha256 fb8c90f7b744)
  - courses: ENG 212 ⟵ “ENG 212 - Introduction to Digital Texts and Media”
  - courses: ENG 303 ⟵ “ENG 303 - Intermediate Fiction Writing”
  - courses: ENG 305 ⟵ “ENG 305 - Intermediate Poetry Writing”
  - courses: ENG 311 ⟵ “ENG 311 - Creative Nonfiction Writing”
  - courses: ENG 329 ⟵ “ENG 329 - Special Topics in Creative Writing”
  - courses: ENG 358 ⟵ “ENG 358 - Drama Writing”
  - courses: ENG 401 ⟵ “ENG 401 - Advanced Composition”
  - courses: ENG 402 ⟵ “ENG 402 - Editing and Publishing”
  - courses: ENG 415 ⟵ “ENG 415 - Writing and Technology”
### `30761662da553d7d` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-journalism-and-photography-bachelor-of-arts-752p-752 · requirement_key=photography-concentration-required-course [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/visual-journalism-photography-ba/ (sha256 55cb5defcc5a)
  - courses: VJP 433 ⟵ “VJP 433 - Advanced Lighting”
### `3078f82fd379410f` Western Kentucky University — degree_requirements 2026-27 · program_key=criminology-bachelor-of-arts · requirement_key=program-requirements-35-hours-psy-psys-440 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/criminology-ba/ (sha256 5191dda112b1)
  - courses: PSY 441 ⟵ “PSY 441 - Psychological Aspects of Alcoholism”
  - courses: PSY 470 ⟵ “PSY 470 - Psychology and Law”
  - courses: SOCL 359 ⟵ “SOCL 359 - Sexuality and Society”
  - courses: SOCL 389 ⟵ “SOCL 389 - Stigma and Society”
  - courses: SOCL 435 ⟵ “SOCL 435 - Family Violence”
  - courses: SWRK 356 ⟵ “SWRK 356 - Services for Juvenile Offenders and Their Families”
  - courses: PHIL 427 ⟵ “PHIL 427 - Philosophy of Law”
  - courses: CRIM 339 ⟵ “CRIM 339 - Experiential Learning in Criminology”
  - courses: SOCL 315 ⟵ “SOCL 315 - Public Problem Solving”
### `381ffcd95e820805` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-politics-and-policy-track-31-hours-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - section: philosophy-politics-and-policy-track-31-hours-electives ⟵ “Philosophy, Politics, and Policy Track (31 hours) — Electives”
### `3ff66c0a7e785892` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=program-requirements-42-hours-writing-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 203 ⟵ “ENG 203 - Creative Writing”
  - courses: ENG 306 ⟵ “ENG 306 - Business Writing”
  - courses: ENG 307 ⟵ “ENG 307 - Technical Writing”
  - courses: ENG 401 ⟵ “ENG 401 - Advanced Composition”
  - courses: ENG 410 ⟵ “ENG 410 - Composition Theory and Practice in Writing Instruction”
  - courses: ENG 212 ⟵ “ENG 212 - Introduction to Digital Texts and Media”
  - courses: ENG 301 ⟵ “ENG 301 - Argument and Analysis in Written Discourse”
  - courses: ENG 412 ⟵ “ENG 412 - Theories of Rhetoric and Persuasive Writing”
### `4457aa1801c0ac89` Western Kentucky University — degree_requirements 2026-27 · program_key=legal-studies-bachelor-of-arts · requirement_key=program-requirements-36-hours-program-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/legal-studies-ba/ (sha256 e4ac270afc7b)
  - courses: PS 220 ⟵ “PS 220 - Judicial Process”
  - courses: PLS 250 ⟵ “PLS 250 - Legal Research and Writing I”
  - courses: PS 326 ⟵ “PS 326 - Constitutional Law”
  - courses: HIST 445 ⟵ “HIST 445 - American Legal History to 1865”
  - courses: HIST 446 ⟵ “HIST 446 - American Legal History Since 1865”
  - courses: LS 495 ⟵ “LS 495 - Senior Seminar in Legal Studies”
  - courses: SMC 301 ⟵ “SMC 301 - Mass Communication Law and Ethics”
  - courses: PLS 200 ⟵ “PLS 200 - Legal Ethics”
  - courses: PHIL 350 ⟵ “PHIL 350 - Ethical Theory”
  - courses: PS 338 ⟵ “PS 338 - Government and Ethics”
  - courses: PS 355 ⟵ “PS 355 - International Organization and Law”
  - courses: PLS 375 ⟵ “PLS 375 - Comparative Legal Systems”
  - courses: HIST 380 ⟵ “HIST 380 - Human Rights in History”
  - courses: CRIM 430 ⟵ “CRIM 430 - Comparative Systems of Juvenile Justice”
  - courses: CRIM 448 ⟵ “CRIM 448 - International Justice and Crime”
  - courses: GEOG 487 ⟵ “GEOG 487 - Environmental Management and Law”
  - courses: MGT 200 ⟵ “MGT 200 - Legal Environment of Business”
  - courses: PLS 283 ⟵ “PLS 283 - Property Law”
  - courses: MGT 301 ⟵ “MGT 301 - Business Law”
  - courses: ECON 390 ⟵ “ECON 390 - Economics, Law, and Public Choice”
  - courses: PLS 392 ⟵ “PLS 392 - Corporate Law”
  - courses: ECON 434 ⟵ “ECON 434 - The Economics of Poverty and Discrimination”
  - courses: PLS 324 ⟵ “PLS 324 - Women and the Law”
  - courses: PS 328 ⟵ “PS 328 - Criminal Justice Procedures”
  - courses: CRIM 330 ⟵ “CRIM 330 - Criminology”
  - … 15 more rows
### `44736e04079ee6e4` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-politics-and-policy-track-31-hours-history-of-philosophy [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PHIL 331 ⟵ “PHIL 331 - Analytic Philosophy”
  - courses: PHIL 341 ⟵ “PHIL 341 - Plato and Aristotle”
  - courses: PHIL 342 ⟵ “PHIL 342 - Skeptics, Stoics, and Epicureans”
  - courses: PHIL 343 ⟵ “PHIL 343 - Medieval Philosophy”
  - courses: PHIL 344 ⟵ “PHIL 344 - Early Modern Moral Philosophy”
  - courses: PHIL 345 ⟵ “PHIL 345 - Descartes and Hume”
  - courses: PHIL 346 ⟵ “PHIL 346 - Kant and Idealism”
  - courses: PHIL 347 ⟵ “PHIL 347 - Leibniz and Locke”
  - courses: PHIL 348 ⟵ “PHIL 348 - 20th Century Philosophy”
  - courses: PHIL 406 ⟵ “PHIL 406 - Existentialism”
  - courses: PHIL 440 ⟵ “PHIL 440 - Readings in Ancient or Medieval Philosophy”
  - courses: PHIL 450 ⟵ “PHIL 450 - Readings in Modern or Contemporary Philosophy”
  - courses: PS 330 ⟵ “PS 330 - Introduction to Political Theory”
### `459034217dbff738` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-politics-and-policy-track-31-hours-ethics-and-values [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PHIL 202 ⟵ “PHIL 202 - Racial Justice”
  - courses: PHIL 207 ⟵ “PHIL 207 - Philosophy and Popular Culture”
  - courses: PHIL 208 ⟵ “PHIL 208 - Philosophy of Public Space; Reason, Action & Violence”
  - courses: PHIL 211 ⟵ “PHIL 211 - Why Are Bad People Bad?”
  - courses: PHIL 212 ⟵ “PHIL 212 - Philosophy and Gender Theory”
  - courses: PHIL 305 ⟵ “PHIL 305 - Aesthetics”
  - courses: PHIL 322 ⟵ “PHIL 322 - Biomedical Ethics”
  - courses: PHIL 323 ⟵ “PHIL 323 - Social Ethics”
  - courses: PHIL 324 ⟵ “PHIL 324 - War and Peace”
  - courses: PHIL 333 ⟵ “PHIL 333 - Marx and Critical Theory”
  - courses: PHIL 344 ⟵ “PHIL 344 - Early Modern Moral Philosophy”
  - courses: PHIL 350 ⟵ “PHIL 350 - Ethical Theory”
  - courses: PHIL 406 ⟵ “PHIL 406 - Existentialism”
  - courses: PHIL 426 ⟵ “PHIL 426 - Philosophy and Old Age”
  - courses: PHIL 427 ⟵ “PHIL 427 - Philosophy of Law”
### `4691d9f709658c0c` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-journalism-and-photography-bachelor-of-arts-752p-752 · requirement_key=photography-concentration-restricted-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/visual-journalism-photography-ba/ (sha256 55cb5defcc5a)
  - courses: VJP 261 ⟵ “VJP 261 - Mobile Media Storytelling”
  - courses: VJP 339 ⟵ “VJP 339 - Visual Media Business Practices”
  - courses: VJP 390 ⟵ “VJP 390 - Cultural History of Photography”
  - courses: VJP 431 ⟵ “VJP 431 - Advanced Photojournalism”
  - courses: VJP 430 ⟵ “VJP 430 - Advanced Short Form Documentary”
  - courses: BCOM 366 ⟵ “BCOM 366 - Editing I”
  - courses: SOM 399 ⟵ “SOM 399 - Special Topics in Media--Study Abroad”
  - courses: SMC 402 ⟵ “SMC 402 - First Amendment Research and Reporting”
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
### `47b891a1b0953cae` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=creative-writing-concentration-eng-382-eng-391 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 203 ⟵ “ENG 203 - Creative Writing 1”
  - courses: ENG 306 ⟵ “ENG 306 - Business Writing”
  - courses: ENG 307 ⟵ “ENG 307 - Technical Writing”
  - courses: ENG 401 ⟵ “ENG 401 - Advanced Composition”
  - courses: ENG 410 ⟵ “ENG 410 - Composition Theory and Practice in Writing Instruction”
  - courses: ENG 212 ⟵ “ENG 212 - Introduction to Digital Texts and Media”
  - courses: ENG 301 ⟵ “ENG 301 - Argument and Analysis in Written Discourse”
  - courses: ENG 412 ⟵ “ENG 412 - Theories of Rhetoric and Persuasive Writing”
  - courses: FILM 250 ⟵ “FILM 250 - Screenwriting I”
  - courses: ENG 303 ⟵ “ENG 303 - Intermediate Fiction Writing”
  - courses: ENG 305 ⟵ “ENG 305 - Intermediate Poetry Writing”
  - courses: ENG 311 ⟵ “ENG 311 - Creative Nonfiction Writing”
  - courses: ENG 329 ⟵ “ENG 329 - Special Topics in Creative Writing”
  - courses: ENG 358 ⟵ “ENG 358 - Drama Writing”
  - courses: ENG 359 ⟵ “ENG 359 - Topics in Scriptwriting”
  - courses: ENG 403 ⟵ “ENG 403 - Writing Memoir and Autobiography”
  - courses: ENG 411 ⟵ “ENG 411 - Directed Writing”
  - courses: FILM 450 ⟵ “FILM 450 - Feature Screenwriting”
  - courses: ENG 474 ⟵ “ENG 474 - Advanced Poetry Writing”
  - courses: ENG 475 ⟵ “ENG 475 - Advanced Fiction Workshop”
  - courses: ENG 467 ⟵ “ENG 467 - Visiting Writer Summer Workshop”
### `4d5d1a3b4d538e60` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-studies-bachelor-of-arts · requirement_key=studio-concentration-note-6-credit-hours-of-upper-level-discipline-specific-cour [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-studies-ba/ (sha256 fcd2c45cf314)
  - courses: ART 321 ⟵ “ART 321 - Ceramics”
  - courses: ART 330 ⟵ “ART 330 - Graphic Design II: Layout & Information Design”
  - courses: DES 331 ⟵ “DES 331 - Visual Thinking”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 341 ⟵ “ART 341 - Drawing”
  - courses: ART 343 ⟵ “ART 343 - Digital Media: Time-Based”
  - courses: ART 350 ⟵ “ART 350 - Printmaking”
  - courses: ART 351 ⟵ “ART 351 - Printmaking”
  - courses: ART 430 ⟵ “ART 430 - Graphic Design III: Advanced Graphic Design”
  - courses: ART 431 ⟵ “ART 431 - Illustration”
  - courses: ART 433 ⟵ “ART 433 - Package Design”
  - courses: ART 436 ⟵ “ART 436 - Digital Illustration”
  - courses: DES 438 ⟵ “DES 438 - Advanced Media Design”
  - courses: ART 420 ⟵ “ART 420 - Ceramics”
  - courses: ART 421 ⟵ “ART 421 - Ceramics”
  - courses: ART 422 ⟵ “ART 422 - Ceramics”
  - courses: ART 423 ⟵ “ART 423 - Pottery Wheel Techniques”
  - courses: ART 424 ⟵ “ART 424 - Ceramic Glaze Composition”
  - courses: ART 425 ⟵ “ART 425 - Ceramic Studio Equipment Design”
  - courses: ART 426 ⟵ “ART 426 - Special Firing Techniques”
  - courses: ART 440 ⟵ “ART 440 - Drawing”
  - courses: ANIM 444 ⟵ “ANIM 444 - Computer Animation III”
  - courses: ART 450 ⟵ “ART 450 - Printmaking”
  - courses: ART 451 ⟵ “ART 451 - Printmaking”
  - courses: ART 452 ⟵ “ART 452 - Printmaking”
  - … 15 more rows
### `4ed948fe99913c76` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=biological-anthropology-concentration-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
  - section: biological-anthropology-concentration-electives ⟵ “Biological Anthropology Concentration — Electives”
### `53b26699c301851d` Western Kentucky University — degree_requirements 2026-27 · program_key=user-experience-bachelor-of-science · requirement_key=program-requirements-57-hours-ux-foundation-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/user-experience-bs/ (sha256 eed3996a11f0)
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: UX 220 ⟵ “UX 220 - Introduction to User Experience Design”
### `53fac86d01ccd0e1` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=cultural-anthropology-concentration-concentration-requirements [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
  - courses: ANTH 340 ⟵ “ANTH 340 - Peoples and Cultures of Latin America”
  - courses: ANTH 342 ⟵ “ANTH 342 - Peoples and Cultures of the Caribbean”
  - courses: ANTH 345 ⟵ “ANTH 345 - Peoples and Cultures of Native North America”
  - courses: ANTH 350 ⟵ “ANTH 350 - Peoples and Cultures of Africa”
  - courses: ANTH 378 ⟵ “ANTH 378 - Southern Appalachian Folklife”
  - courses: ANTH 343 ⟵ “ANTH 343 - Anthropology of Gender”
  - courses: ANTH 382 ⟵ “ANTH 382 - Medical Anthropology”
  - courses: ANTH 388 ⟵ “ANTH 388 - Foodways”
  - courses: ANTH 400 ⟵ “ANTH 400 - Ethnomusicology”
  - courses: ANTH 410 ⟵ “ANTH 410 - African-American Music”
  - courses: ANTH 442 ⟵ “ANTH 442 - Ecological and Economic Anthropology”
  - courses: ANTH 446 ⟵ “ANTH 446 - Anthropology of Religion”
  - courses: ANTH 448 ⟵ “ANTH 448 - Visual Anthropology”
  - courses: ANTH 449 ⟵ “ANTH 449 - Ethnographic Video Production”
### `56d4bfd059ca05ed` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=elective-courses-courses-on-chinese-studies-delivered-in-english [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
  - courses: HIST 460 ⟵ “HIST 460 - Traditional East Asia”
  - courses: HIST 461 ⟵ “HIST 461 - Modern East Asia”
  - courses: HIST 471 ⟵ “HIST 471 - Modern China”
  - courses: PS 366 ⟵ “PS 366 - Government and Politics in East Asia”
  - courses: RELS 317 ⟵ “RELS 317 - Confucianism”
  - courses: RELS 318 ⟵ “RELS 318 - Daoism”
### `5c6d4a357c958da4` Western Kentucky University — degree_requirements 2026-27 · program_key=english-for-secondary-teachers-bachelor-of-arts · requirement_key=program-requirements-54-hours-allied-language-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-secondary-teachers-ba/ (sha256 fb8c90f7b744)
  - courses: COMM 345 ⟵ “COMM 345 - Advanced Presentational Speaking”
  - courses: JOUR 202 ⟵ “JOUR 202 - Introduction to News Writing”
  - courses: THEA 425 ⟵ “THEA 425 - Play Production in the Schools”
  - courses: THEA 325 ⟵ “THEA 325 - Theatre in Education”
### `5eb662263bd2562b` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-politics-and-policy-track-31-hours-any-philosophy-course-that-is-not- [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PS 201 ⟵ “PS 201 - Concepts of Political Science”
  - courses: PS 311 ⟵ “PS 311 - Public Policy”
  - courses: PS 316 ⟵ “PS 316 - The Legislative Process”
  - courses: PS 326 ⟵ “PS 326 - Constitutional Law”
  - courses: PS 327 ⟵ “PS 327 - Civil Liberties”
  - courses: PS 328 ⟵ “PS 328 - Criminal Justice Procedures”
  - courses: PS 330 ⟵ “PS 330 - Introduction to Political Theory”
  - courses: PS 338 ⟵ “PS 338 - Government and Ethics”
  - courses: PS 340 ⟵ “PS 340 - Principles of Public Administration”
### `5f87286927653cb5` Western Kentucky University — degree_requirements 2026-27 · program_key=religious-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-religious-traditions-comparative-approaches-and-re [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/religious-studies-ba/ (sha256 a798e0130e89)
  - courses: RELS 100 ⟵ “RELS 100 - The New Testament”
  - courses: RELS 101 ⟵ “RELS 101 - The Old Testament/ Hebrew Scriptures”
  - courses: RELS 211 ⟵ “RELS 211 - Jesus in Film”
  - courses: RELS 222 ⟵ “RELS 222 - Christians, Jews, and Pagans in the Greco-Roman World”
  - courses: RELS 242 ⟵ “RELS 242 - The Meaning of Life; Atheism to Zen”
  - courses: RELS 300 ⟵ “RELS 300 - The Life of Jesus”
  - courses: RELS 302 ⟵ “RELS 302 - Buddhism”
  - courses: RELS 303 ⟵ “RELS 303 - Hinduism”
  - courses: RELS 304 ⟵ “RELS 304 - Judaism”
  - courses: RELS 305 ⟵ “RELS 305 - Christianity”
  - courses: RELS 306 ⟵ “RELS 306 - Islam”
  - courses: RELS 309 ⟵ “RELS 309 - Global Christianity”
  - courses: RELS 317 ⟵ “RELS 317 - Confucianism”
  - courses: RELS 318 ⟵ “RELS 318 - Daoism”
  - courses: RELS 319 ⟵ “RELS 319 - Religions of Asia”
  - courses: RELS 322 ⟵ “RELS 322 - Pilgrimage, Islam and Modernity”
  - courses: RELS 331 ⟵ “RELS 331 - Islam in America: Hope & Hip Hop”
  - courses: RELS 333 ⟵ “RELS 333 - Women and Religion”
  - courses: RELS 335 ⟵ “RELS 335 - Islam, Sexuality, and Gender”
  - courses: RELS 340 ⟵ “RELS 340 - Popular Culture and the Religious Marketplace”
  - courses: RELS 341 ⟵ “RELS 341 - Religion and the Environment”
  - courses: RELS 455 ⟵ “RELS 455 - Saints, Monsters and Superheroes”
### `62ad60429a829e8d` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-communication-concentration-advertising-user-experience [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: UX 220 ⟵ “UX 220 - Introduction to User Experience Design”
  - courses: UX 330 ⟵ “UX 330 - User Interface Design”
### `6405b1a2db71fb39` Western Kentucky University — degree_requirements 2026-27 · program_key=journalism-bachelor-of-arts-736p-736 · requirement_key=program-requirements-42-hours-diversity-elective [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/journalism-ba/ (sha256 255ceb1183cf)
  - courses: SMC 310 ⟵ “SMC 310 - Media Representation”
  - courses: AFAM 343 ⟵ “AFAM 343 - Communities of Struggle”
  - courses: ASL 302 ⟵ “ASL 302 - Deaf Culture in America”
  - courses: COMM 363 ⟵ “COMM 363 - Interracial Communication”
  - courses: COMM 365 ⟵ “COMM 365 - Intercultural Communication”
  - courses: COMM 371 ⟵ “COMM 371 - Communication in Multinational Organizations”
  - courses: CRIM 361 ⟵ “CRIM 361 - Race, Class, and Crime”
  - courses: CRIM 446 ⟵ “CRIM 446 - Gender, Crime, and Justice”
  - courses: FLK 330 ⟵ “FLK 330 - Cultural Connections and Diversity”
  - courses: FLK 373 ⟵ “FLK 373 - Folklore and the Media”
  - courses: GWS 375 ⟵ “GWS 375 - American Masculinities”
  - courses: HIST 302 ⟵ “HIST 302 - Disability in the United States”
  - courses: HIST 343 ⟵ “HIST 343 - Communities of Struggle”
  - courses: LEAD 450 ⟵ “LEAD 450 - Leadership in Global Contexts”
  - courses: PH 410 ⟵ “PH 410 - Global Perspectives on Population Health”
  - courses: PS 373 ⟵ “PS 373 - Minority Politics”
  - courses: SOCL 355 ⟵ “SOCL 355 - Sociology of Gender”
  - courses: SOCL 362 ⟵ “SOCL 362 - Social Institutions: Race, Class, and Gender”
  - courses: SOCL 375 ⟵ “SOCL 375 - Diversity in American Society”
  - courses: SOCL 376 ⟵ “SOCL 376 - Sociology of Globalization”
  - courses: SPS 400 ⟵ “SPS 400 - Foundations of Global Citizenship”
  - courses: SWRK 300 ⟵ “SWRK 300 - Diversity and Social Welfare”
  - courses: JOUR 426 ⟵ “JOUR 426 - Advanced Reporting”
### `683d6861d561dbb0` Western Kentucky University — degree_requirements 2026-27 · program_key=user-experience-bachelor-of-science · requirement_key=program-requirements-57-hours-capstone-course [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/user-experience-bs/ (sha256 eed3996a11f0)
  - courses: UX 450 ⟵ “UX 450 - User Experience Advanced Studio II”
### `69c2c98e194249e5` Western Kentucky University — degree_requirements 2026-27 · program_key=religious-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/religious-studies-ba/ (sha256 a798e0130e89)
  - section: program-requirements-30-hours-electives ⟵ “Program Requirements (30 hours) — Electives”
### `6bd6c3f089cd0153` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=program-requirements-42-hours-capstone [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 413 ⟵ “ENG 413 - Creative Writing Capstone”
  - courses: ENG 414 ⟵ “ENG 414 - Professional Writing Capstone”
  - courses: ENG 416 ⟵ “ENG 416 - Literature/EST Capstone”
### `6caeeb49c7bcd79d` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=elective-courses-courses-on-chinese-studies-delivered-in-english-2 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
  - courses: HIST 460 ⟵ “HIST 460 - Traditional East Asia”
  - courses: HIST 461 ⟵ “HIST 461 - Modern East Asia”
  - courses: HIST 471 ⟵ “HIST 471 - Modern China”
  - courses: PS 366 ⟵ “PS 366 - Government and Politics in East Asia”
  - courses: RELS 317 ⟵ “RELS 317 - Confucianism”
  - courses: RELS 318 ⟵ “RELS 318 - Daoism”
### `6e08f045e86a7dcd` Western Kentucky University — degree_requirements 2026-27 · program_key=user-experience-bachelor-of-science · requirement_key=program-requirements-57-hours-psychological-sciences-foundation-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/user-experience-bs/ (sha256 eed3996a11f0)
  - courses: PSYS 100 ⟵ “PSYS 100 - Introduction to Psychology”
  - courses: PSYS 210 ⟵ “PSYS 210 - Research Methods in Psychology”
  - courses: PSYS 211 ⟵ “PSYS 211 - Research Methods in Psychology Laboratory”
### `6e584e5ae6c0e478` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=program-requirements-42-hours-introduction-to-the-major [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 299 ⟵ “ENG 299 - Introduction to English Studies”
### `6fdab340db5983b2` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-for-health-sciences-and-health-care-concentration-psy-psys-220 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
  - courses: PSYS 440 ⟵ “PSYS 440 - Abnormal Psychology”
  - courses: HMD 211 ⟵ “HMD 211 - Human Nutrition”
### `70e9ab2f4307ad64` Western Kentucky University — degree_requirements 2026-27 · program_key=english-for-secondary-teachers-bachelor-of-arts · requirement_key=program-requirements-54-hours-literature-elective [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-secondary-teachers-ba/ (sha256 fb8c90f7b744)
  - courses: ENG 333 ⟵ “ENG 333 - Medieval Literature”
  - courses: ENG 339 ⟵ “ENG 339 - Special Topics in Literature”
  - courses: ENG 340 ⟵ “ENG 340 - Speculative Fiction”
  - courses: ENG 354 ⟵ “ENG 354 - History of Drama to 1640”
  - courses: ENG 355 ⟵ “ENG 355 - History of Drama Since 1640”
  - courses: ENG 365 ⟵ “ENG 365 - Film Adaptation”
  - courses: ENG 387 ⟵ “ENG 387 - Studies in Autobiography”
  - courses: ENG 394 ⟵ “ENG 394 - Kentucky Literature”
  - courses: ENG 395 ⟵ “ENG 395 - Contemporary U.S. Literature”
  - courses: ENG 396 ⟵ “ENG 396 - Mythology”
  - courses: ENG 398 ⟵ “ENG 398 - Hemingway and Faulkner”
  - courses: ENG 430 ⟵ “ENG 430 - 19th Century American Literature”
  - courses: ENG 455 ⟵ “ENG 455 - American Drama”
  - courses: ENG 457 ⟵ “ENG 457 - British Literature Since 1900”
  - courses: ENG 459 ⟵ “ENG 459 - Modern Drama”
  - courses: ENG 460 ⟵ “ENG 460 - Literary Theory and Criticism”
  - courses: ENG 468 ⟵ “ENG 468 - Early Modern English Literature”
  - courses: ENG 481 ⟵ “ENG 481 - Chaucer”
  - courses: ENG 482 ⟵ “ENG 482 - Shakespeare”
  - courses: ENG 484 ⟵ “ENG 484 - British Romanticism”
  - courses: ENG 486 ⟵ “ENG 486 - The Eighteenth Century”
  - courses: ENG 487 ⟵ “ENG 487 - Dante’s Divine Comedy and Its Influences”
  - courses: ENG 488 ⟵ “ENG 488 - Victorian Literature and Culture”
  - courses: ENG 489 ⟵ “ENG 489 - The English Novel”
  - courses: ENG 490 ⟵ “ENG 490 - The American Novel”
  - … 2 more rows
### `73336f623508e1ba` Western Kentucky University — degree_requirements 2026-27 · program_key=english-for-secondary-teachers-bachelor-of-arts · requirement_key=program-requirements-54-hours-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-secondary-teachers-ba/ (sha256 fb8c90f7b744)
  - courses: ENG 104 ⟵ “ENG 104 - Introduction to Linguistics”
  - courses: ENG 204 ⟵ “ENG 204 - English Language”
  - courses: ENG 299 ⟵ “ENG 299 - Introduction to English Studies”
  - courses: ENG 301 ⟵ “ENG 301 - Argument and Analysis in Written Discourse”
  - courses: ENG 385 ⟵ “ENG 385 - Studies in World Literature”
  - courses: ENG 391 ⟵ “ENG 391 - Survey of American Literature I”
  - courses: ENG 410 ⟵ “ENG 410 - Composition Theory and Practice in Writing Instruction”
  - courses: ENG 416 ⟵ “ENG 416 - Literature/EST Capstone”
  - courses: COMM 145 ⟵ “COMM 145 - Fundamentals of Public Speaking and Communication”
  - courses: THEA 151 ⟵ “THEA 151 - Theatre Appreciation 1”
  - courses: ENG 476 ⟵ “ENG 476 - Critical Approaches to Literature in the Secondary Curriculum”
### `756199b72d335103` Western Kentucky University — degree_requirements 2026-27 · program_key=user-experience-bachelor-of-science · requirement_key=program-requirements-57-hours-advanced-ux-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/user-experience-bs/ (sha256 eed3996a11f0)
  - courses: UX 310 ⟵ “UX 310 - Future Design”
  - courses: UX 330 ⟵ “UX 330 - User Interface Design”
  - courses: UX 340 ⟵ “UX 340 - Introduction to Developing and Prototyping for Interactive Design”
  - courses: UX 400 ⟵ “UX 400 - User Experience Advanced Studio I”
  - courses: UX 430 ⟵ “UX 430 - Advanced User Interface Design”
  - courses: UX 440 ⟵ “UX 440 - Advanced Developing and Testing for Interactive Design”
### `776026fdec3b4468` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=creative-writing-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 204 ⟵ “ENG 204 - English Language”
  - courses: ENG 299 ⟵ “ENG 299 - Introduction to English Studies”
  - courses: ENG 312 ⟵ “ENG 312 - Reading as a Writer”
  - courses: ENG 385 ⟵ “ENG 385 - Studies in World Literature”
  - courses: ENG 413 ⟵ “ENG 413 - Creative Writing Capstone (capstone, which should be taken in the final semester of coursework)”
### `776fca2564967eb4` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-journalism-and-photography-bachelor-of-arts-752p-752 · requirement_key=program-requirements-36-45-hours-required-courses-both-concentrations [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/visual-journalism-photography-ba/ (sha256 55cb5defcc5a)
  - courses: SMC 101 ⟵ “SMC 101 - Understanding Media Content, Ethics and Technology”
  - courses: SMC 102 ⟵ “SMC 102 - Media Content, Collaboration and Community”
  - courses: VJP 131 ⟵ “VJP 131 - Fundamentals of Photography”
  - courses: VJP 331 ⟵ “VJP 331 - Photojournalism”
  - courses: VJP 330 ⟵ “VJP 330 - Short Form Documentary”
  - courses: VJP 332 ⟵ “VJP 332 - Visual Media Editing and Design”
  - courses: VJP 333 ⟵ “VJP 333 - Studio Lighting”
### `7a2a7f42537da1a0` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=elective-courses-chin-200-level-courses-other-than-chin-201-chin-202-3-hours-max [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
  - section: elective-courses-chin-200-level-courses-other-than-chin-201-chin-202-3-hours-max ⟵ “Elective Courses — CHIN 200-level courses other than CHIN 201 / CHIN 202 (3 hours maximum)”
### `7f23cebe8d68c473` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=program-requirements-42-hours-literature-survey-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 385 ⟵ “ENG 385 - Studies in World Literature”
### `82ee651800640210` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-for-health-sciences-and-health-care-concentration-biol-122-biol-123 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
  - courses: BIOL 131 ⟵ “BIOL 131 - Human Anatomy and Physiology”
### `8ebef5ebf4fdbf67` Western Kentucky University — degree_requirements 2026-27 · program_key=theatre-bachelor-of-arts · requirement_key=program-requirements-45-hours-history-theory-12-credit-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/theatre-ba/ (sha256 1b9c0be3c605)
  - courses: THEA 252 ⟵ “THEA 252 - Fundamentals of Theatre”
  - courses: THEA 363 ⟵ “THEA 363 - World Theatre History I (3 credit hours)”
  - courses: THEA 364 ⟵ “THEA 364 - World Theatre History II (3 credit hours)”
  - courses: THEA 365 ⟵ “THEA 365 - U.S. Theatre History (3 credit hours)”
  - courses: THEA 375 ⟵ “THEA 375 - Topics in Drama (3 credit hours)”
  - courses: THEA 430 ⟵ “THEA 430 - Musical Theatre History (3 credit hours)”
### `8effa0d30f2369be` Western Kentucky University — degree_requirements 2026-27 · program_key=social-studies-bachelor-of-arts · requirement_key=program-requirements-51-hours-history [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/social-studies-ba/ (sha256 02fc45f9924f)
  - courses: HIST 101 ⟵ “HIST 101 - World History I”
  - courses: HIST 102 ⟵ “HIST 102 - World History II”
  - courses: HIST 240 ⟵ “HIST 240 - The United States to 1865”
  - courses: HIST 241 ⟵ “HIST 241 - The United States Since 1865”
  - courses: HIST 498 ⟵ “HIST 498 - Senior Seminar”
### `916b23f452c2d36e` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-journalism-and-photography-bachelor-of-arts-752p-752 · requirement_key=photojournalism-and-documentary-concentration-diversity-elective [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/visual-journalism-photography-ba/ (sha256 55cb5defcc5a)
  - courses: SMC 310 ⟵ “SMC 310 - Media Representation”
  - courses: AFAM 343 ⟵ “AFAM 343 - Communities of Struggle”
  - courses: ASL 302 ⟵ “ASL 302 - Deaf Culture in America”
  - courses: COMM 363 ⟵ “COMM 363 - Interracial Communication”
  - courses: COMM 365 ⟵ “COMM 365 - Intercultural Communication”
  - courses: COMM 371 ⟵ “COMM 371 - Communication in Multinational Organizations”
  - courses: CRIM 361 ⟵ “CRIM 361 - Race, Class, and Crime”
  - courses: CRIM 446 ⟵ “CRIM 446 - Gender, Crime, and Justice”
  - courses: FLK 330 ⟵ “FLK 330 - Cultural Connections and Diversity”
  - courses: FLK 373 ⟵ “FLK 373 - Folklore and the Media”
  - courses: GWS 375 ⟵ “GWS 375 - American Masculinities”
  - courses: HIST 302 ⟵ “HIST 302 - Disability in the United States”
  - courses: HIST 343 ⟵ “HIST 343 - Communities of Struggle”
  - courses: LEAD 450 ⟵ “LEAD 450 - Leadership in Global Contexts”
  - courses: PH 410 ⟵ “PH 410 - Global Perspectives on Population Health”
  - courses: PS 373 ⟵ “PS 373 - Minority Politics”
  - courses: SOCL 355 ⟵ “SOCL 355 - Sociology of Gender”
  - courses: SOCL 362 ⟵ “SOCL 362 - Social Institutions: Race, Class, and Gender”
  - courses: SOCL 375 ⟵ “SOCL 375 - Diversity in American Society”
  - courses: SOCL 376 ⟵ “SOCL 376 - Sociology of Globalization”
  - courses: SPS 400 ⟵ “SPS 400 - Foundations of Global Citizenship”
  - courses: SWRK 300 ⟵ “SWRK 300 - Diversity and Social Welfare”
### `92f1dd22e309dbe6` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=applied-anthropology-concentration-requirements [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
  - courses: ANTH 360 ⟵ “ANTH 360 - Applied Anthropology – Understanding and Addressing Contemporary Human Problems”
  - courses: ANTH 300 ⟵ “ANTH 300 - Forensic Anthropology”
  - courses: ANTH 382 ⟵ “ANTH 382 - Medical Anthropology”
  - courses: ANTH 434 ⟵ “ANTH 434 - Graveyard Archaeology”
  - courses: ANTH 436 ⟵ “ANTH 436 - Applied Archaeology”
  - courses: ANTH 442 ⟵ “ANTH 442 - Ecological and Economic Anthropology”
  - courses: ANTH 449 ⟵ “ANTH 449 - Ethnographic Video Production”
### `94667f7d8c0d759d` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-studies-bachelor-of-arts · requirement_key=art-education-concentration-required-capstone-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-studies-ba/ (sha256 fcd2c45cf314)
  - courses: ART 432 ⟵ “ART 432 - Portfolio”
  - courses: ART 496 ⟵ “ART 496 - Special Topics in Studio Art”
### `959e6e44ea9fb6e8` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=applied-anthropology-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
  - section: applied-anthropology-electives ⟵ “Applied Anthropology — Electives”
### `980428c25bf5029a` Western Kentucky University — degree_requirements 2026-27 · program_key=film-bachelor-of-arts-667p-667 · requirement_key=program-requirements-36-hours-eng-film-466 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/film-ba/ (sha256 d1378fd4bf29)
  - courses: BCOM 481 ⟵ “BCOM 481 - Problems in Mass Communication”
  - courses: PS 303 ⟵ “PS 303 - Politics and Film”
  - courses: ANTH 448 ⟵ “ANTH 448 - Visual Anthropology”
  - courses: ENG 295 ⟵ “ENG 295 - Popular Culture and Gender: Signs & Narratives”
  - courses: FILM 382 ⟵ “FILM 382 - Film Production Workshop II”
  - courses: FILM 394 ⟵ “FILM 394 - Film Animation”
  - courses: FILM 450 ⟵ “FILM 450 - Feature Screenwriting”
  - courses: FILM 482 ⟵ “FILM 482 - Film Production Workshop III”
  - courses: FILM 486 ⟵ “FILM 486 - Film Capstone”
  - courses: BCOM 266 ⟵ “BCOM 266 - Basic Television Production”
  - courses: BCOM 367 ⟵ “BCOM 367 - Field Production”
  - courses: BCOM 463 ⟵ “BCOM 463 - Field Production II”
  - courses: BCOM 466 ⟵ “BCOM 466 - Television Directing”
  - courses: BCOM 480 ⟵ “BCOM 480 - Editing III”
  - courses: VJP 131 ⟵ “VJP 131 - Fundamentals of Photography”
  - courses: VJP 330 ⟵ “VJP 330 - Short Form Documentary”
  - courses: VJP 430 ⟵ “VJP 430 - Advanced Short Form Documentary”
  - courses: PERF 101 ⟵ “PERF 101 - Acting”
### `9aa8fed8cd4fd5e1` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=professional-writing-concentration-eng-382-eng-391 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 203 ⟵ “ENG 203 - Creative Writing”
  - courses: ENG 306 ⟵ “ENG 306 - Business Writing 1”
  - courses: ENG 307 ⟵ “ENG 307 - Technical Writing 1”
  - courses: ENG 401 ⟵ “ENG 401 - Advanced Composition”
  - courses: ENG 410 ⟵ “ENG 410 - Composition Theory and Practice in Writing Instruction”
  - courses: ENG 212 ⟵ “ENG 212 - Introduction to Digital Texts and Media”
  - courses: ENG 301 ⟵ “ENG 301 - Argument and Analysis in Written Discourse”
  - courses: ENG 412 ⟵ “ENG 412 - Theories of Rhetoric and Persuasive Writing”
  - courses: ENG 212 ⟵ “ENG 212 - Introduction to Digital Texts and Media”
  - courses: ENG 301 ⟵ “ENG 301 - Argument and Analysis in Written Discourse”
  - courses: ENG 306 ⟵ “ENG 306 - Business Writing”
  - courses: ENG 307 ⟵ “ENG 307 - Technical Writing”
  - courses: ENG 349 ⟵ “ENG 349 - Special Topics in Professional Writing”
  - courses: ENG 369 ⟵ “ENG 369 - Internship I”
  - courses: ENG 401 ⟵ “ENG 401 - Advanced Composition”
  - courses: ENG 402 ⟵ “ENG 402 - Editing and Publishing”
  - courses: ENG 412 ⟵ “ENG 412 - Theories of Rhetoric and Persuasive Writing”
  - courses: ENG 415 ⟵ “ENG 415 - Writing and Technology”
  - courses: MKT 220 ⟵ “MKT 220 - Basic Marketing Concepts”
  - courses: MKT 331 ⟵ “MKT 331 - Social Media Marketing”
  - courses: VJP 131 ⟵ “VJP 131 - Fundamentals of Photography”
  - courses: BCOM 264 ⟵ “BCOM 264 - Digital Video Production and Distribution”
### `9aadcf2c8de134db` Western Kentucky University — degree_requirements 2026-27 · program_key=economics-bachelor-of-arts · requirement_key=program-requirements-35-hours-additional-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/economics-ba/ (sha256 1e2e2c84e96a)
  - section: program-requirements-35-hours-additional-courses ⟵ “Program Requirements (35 hours) — Additional Courses”
### `9b6206b10d67b428` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-politics-and-policy-track-31-hours-logic-epistemology-and-metaphysics [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PHIL 214 ⟵ “PHIL 214 - Logic, Argument, and Practical Reasoning”
  - courses: PHIL 215 ⟵ “PHIL 215 - Symbolic Logic”
  - courses: PHIL 315 ⟵ “PHIL 315 - Philosophy of Religion”
  - courses: PHIL 330 ⟵ “PHIL 330 - Philosophy of Science”
  - courses: PHIL 332 ⟵ “PHIL 332 - Philosophy of Mind: Minds and Machines”
  - courses: PHIL 334 ⟵ “PHIL 334 - Philosophy of Language”
  - courses: PHIL 404 ⟵ “PHIL 404 - Metaphysics and Epistemology”
  - courses: PHIL 415 ⟵ “PHIL 415 - Advanced Logic”
### `a52d2091fb5220fe` Western Kentucky University — degree_requirements 2026-27 · program_key=social-studies-bachelor-of-arts · requirement_key=teacher-education-requirements [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/social-studies-ba/ (sha256 02fc45f9924f)
  - courses: EDU 250 ⟵ “EDU 250 - Discover Teaching: Introduction to Teacher Education”
  - courses: PSY 310 ⟵ “PSY 310 - Educational Psychology: Development and Learning”
  - courses: SEC 350 ⟵ “SEC 350 - Clinical Practices in Secondary Teaching I”
  - courses: EDU 350 ⟵ “EDU 350 - Student Diversity and Differentiation”
  - courses: EDU 360 ⟵ “EDU 360 - Behavior and Classroom Management in Education”
  - courses: SEC 481 ⟵ “SEC 481 - Clinical Practices in Secondary Teaching II: Social Studies”
  - courses: EDU 260 ⟵ “EDU 260 - Classroom Assessment”
  - courses: LTCY 497 ⟵ “LTCY 497 - Literacy Competencies for Middle and High School Classroom Teachers”
  - courses: SEC 490 ⟵ “SEC 490 - Student Teaching”
  - courses: EDU 489 ⟵ “EDU 489 - Student Teaching Seminar”
### `b18e552338debeb1` Western Kentucky University — degree_requirements 2026-27 · program_key=business-economics-bachelor-of-science · requirement_key=program-requirements-72-hours-business-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/business-economics-bs/ (sha256 367d4d265754)
  - courses: ACCT 220 ⟵ “ACCT 220 - Principles of Financial Accounting”
### `b1c249226983f33d` Western Kentucky University — degree_requirements 2026-27 · program_key=film-production-bachelor-of-fine-arts-530p-530 · requirement_key=program-requirements-78-hours-program-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/film-production-bfa/ (sha256 abc000f8c136)
  - courses: FILM 100 ⟵ “FILM 100 - Film Industry and Aesthetics”
  - courses: FILM 155 ⟵ “FILM 155 - Film Attendance”
  - courses: FILM 201 ⟵ “FILM 201 - Introduction to the Cinema”
  - courses: FILM 202 ⟵ “FILM 202 - Basic Film Production”
  - courses: FILM 250 ⟵ “FILM 250 - Screenwriting I”
  - courses: FILM 256 ⟵ “FILM 256 - Film Editing I”
  - courses: FILM 282 ⟵ “FILM 282 - Film Production Workshop I”
  - courses: FILM 350 ⟵ “FILM 350 - Screenwriting II”
  - courses: FILM 351 ⟵ “FILM 351 - Film Directing II”
  - courses: FILM 353 ⟵ “FILM 353 - Cinematography II”
  - courses: FILM 354 ⟵ “FILM 354 - Production Design II”
  - courses: FILM 355 ⟵ “FILM 355 - Film Sound”
  - courses: FILM 356 ⟵ “FILM 356 - Film Editing II”
  - courses: FILM 367 ⟵ “FILM 367 - Introduction to Film Genres”
  - courses: FILM 369 ⟵ “FILM 369 - Introduction to World Cinema”
  - courses: FILM 382 ⟵ “FILM 382 - Film Production Workshop II”
  - courses: FILM 390 ⟵ “FILM 390 - Practicum: Pre-Production II”
  - courses: FILM 391 ⟵ “FILM 391 - Practicum: Below-the-Line II”
  - courses: FILM 392 ⟵ “FILM 392 - Practicum: Above-the-Line II”
  - courses: FILM 393 ⟵ “FILM 393 - Practicum: Post-Production I”
  - courses: FILM 444 ⟵ “FILM 444 - Film Industry Launch”
  - courses: FILM 466 ⟵ “FILM 466 - Film Theory”
  - courses: FILM 486 ⟵ “FILM 486 - Film Capstone”
  - courses: FILM 489 ⟵ “FILM 489 - Thesis Development”
  - courses: FILM 490 ⟵ “FILM 490 - Practicum: Pre-Production III”
  - … 3 more rows
### `b2d26dc7e98994a6` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-track-31-hours-ethics-and-values [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PHIL 202 ⟵ “PHIL 202 - Racial Justice”
  - courses: PHIL 207 ⟵ “PHIL 207 - Philosophy and Popular Culture”
  - courses: PHIL 208 ⟵ “PHIL 208 - Philosophy of Public Space; Reason, Action & Violence”
  - courses: PHIL 211 ⟵ “PHIL 211 - Why Are Bad People Bad?”
  - courses: PHIL 212 ⟵ “PHIL 212 - Philosophy and Gender Theory”
  - courses: PHIL 305 ⟵ “PHIL 305 - Aesthetics”
  - courses: PHIL 322 ⟵ “PHIL 322 - Biomedical Ethics”
  - courses: PHIL 323 ⟵ “PHIL 323 - Social Ethics”
  - courses: PHIL 324 ⟵ “PHIL 324 - War and Peace”
  - courses: PHIL 333 ⟵ “PHIL 333 - Marx and Critical Theory”
  - courses: PHIL 344 ⟵ “PHIL 344 - Early Modern Moral Philosophy”
  - courses: PHIL 350 ⟵ “PHIL 350 - Ethical Theory”
  - courses: PHIL 406 ⟵ “PHIL 406 - Existentialism”
  - courses: PHIL 426 ⟵ “PHIL 426 - Philosophy and Old Age”
  - courses: PHIL 427 ⟵ “PHIL 427 - Philosophy of Law”
### `b314b26c7301fc80` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=biological-anthropology-concentration-concentration-requirements [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
  - courses: ANTH 300 ⟵ “ANTH 300 - Forensic Anthropology”
  - courses: ANTH 305 ⟵ “ANTH 305 - Paleoanthropology: Human Origins and Evolution”
  - courses: ANTH 452 ⟵ “ANTH 452 - Bioarchaeology”
### `b4f80d6a0240ab6c` Western Kentucky University — degree_requirements 2026-27 · program_key=user-experience-bachelor-of-science · requirement_key=program-requirements-57-hours-computer-science-foundation-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/user-experience-bs/ (sha256 eed3996a11f0)
  - courses: MATH 117 ⟵ “MATH 117 - Trigonometry”
  - courses: CS 180 ⟵ “CS 180 - Computer Science I”
  - courses: CS 290 ⟵ “CS 290 - Computer Science II”
### `b97ab4390f312c13` Western Kentucky University — degree_requirements 2026-27 · program_key=english-for-secondary-teachers-bachelor-of-arts · requirement_key=professional-education-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-secondary-teachers-ba/ (sha256 fb8c90f7b744)
  - courses: EDU 250 ⟵ “EDU 250 - Discover Teaching: Introduction to Teacher Education”
  - courses: PSY 310 ⟵ “PSY 310 - Educational Psychology: Development and Learning”
  - courses: SEC 350 ⟵ “SEC 350 - Clinical Practices in Secondary Teaching I”
  - courses: EDU 350 ⟵ “EDU 350 - Student Diversity and Differentiation”
  - courses: EDU 360 ⟵ “EDU 360 - Behavior and Classroom Management in Education”
  - courses: SEC 450 ⟵ “SEC 450 - Clinical Practices in Secondary Teaching II”
  - courses: SEC 475 ⟵ “SEC 475 - Teaching Language Arts”
  - courses: EDU 260 ⟵ “EDU 260 - Classroom Assessment”
  - courses: LTCY 497 ⟵ “LTCY 497 - Literacy Competencies for Middle and High School Classroom Teachers”
  - courses: SEC 490 ⟵ “SEC 490 - Student Teaching”
  - courses: EDU 489 ⟵ “EDU 489 - Student Teaching Seminar”
### `ba63461ffccf4711` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-track-31-hours-history-of-philosophy [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PHIL 331 ⟵ “PHIL 331 - Analytic Philosophy”
  - courses: PHIL 341 ⟵ “PHIL 341 - Plato and Aristotle”
  - courses: PHIL 342 ⟵ “PHIL 342 - Skeptics, Stoics, and Epicureans”
  - courses: PHIL 343 ⟵ “PHIL 343 - Medieval Philosophy”
  - courses: PHIL 344 ⟵ “PHIL 344 - Early Modern Moral Philosophy”
  - courses: PHIL 345 ⟵ “PHIL 345 - Descartes and Hume”
  - courses: PHIL 346 ⟵ “PHIL 346 - Kant and Idealism”
  - courses: PHIL 347 ⟵ “PHIL 347 - Leibniz and Locke”
  - courses: PHIL 348 ⟵ “PHIL 348 - 20th Century Philosophy”
  - courses: PHIL 406 ⟵ “PHIL 406 - Existentialism”
  - courses: PHIL 440 ⟵ “PHIL 440 - Readings in Ancient or Medieval Philosophy”
  - courses: PHIL 450 ⟵ “PHIL 450 - Readings in Modern or Contemporary Philosophy”
  - courses: PS 330 ⟵ “PS 330 - Introduction to Political Theory”
### `bf8557f8dd3a323d` Western Kentucky University — degree_requirements 2026-27 · program_key=english-for-secondary-teachers-bachelor-of-arts · requirement_key=program-requirements-54-hours-literature-surveys [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-secondary-teachers-ba/ (sha256 fb8c90f7b744)
  - courses: ENG 381 ⟵ “ENG 381 - Survey of British Literature I”
  - courses: ENG 382 ⟵ “ENG 382 - Survey of British Literature II”
  - courses: ENG 392 ⟵ “ENG 392 - Survey of American Literature II”
### `c2d03175fe8a4933` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=cultural-anthropology-concentration-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
  - section: cultural-anthropology-concentration-electives ⟵ “Cultural Anthropology Concentration — Electives”
### `c2d47f9a02dcf356` Western Kentucky University — degree_requirements 2026-27 · program_key=religious-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-any-rels-course-not-already-counted-toward-the-maj [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/religious-studies-ba/ (sha256 a798e0130e89)
  - courses: ANTH 446 ⟵ “ANTH 446 - Anthropology of Religion”
  - courses: ART 316 ⟵ “ART 316 - Medieval Art & Architecture”
  - courses: ART 407 ⟵ “ART 407 - Islamic Art and Architecture”
  - courses: ENG 396 ⟵ “ENG 396 - Mythology”
  - courses: ENG 487 ⟵ “ENG 487 - Dante’s Divine Comedy and Its Influences”
  - courses: HIST 318 ⟵ “HIST 318 - Age of the Reformation”
  - courses: HIST 407 ⟵ “HIST 407 - The Crusades: West Meets East”
  - courses: HIST 454 ⟵ “HIST 454 - History of Religion in America”
  - courses: PSYS 451 ⟵ “PSYS 451 - Psychology of Religion”
  - courses: SOCL 322 ⟵ “SOCL 322 - Religion in Society”
### `cadd2d7555577ed1` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=professional-writing-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 204 ⟵ “ENG 204 - English Language”
  - courses: ENG 299 ⟵ “ENG 299 - Introduction to English Studies”
  - courses: ENG 385 ⟵ “ENG 385 - Studies in World Literature”
  - courses: ENG 414 ⟵ “ENG 414 - Professional Writing Capstone (capstone, which should be taken the final semester of coursework)”
### `d1fc64ba43a08858` Western Kentucky University — degree_requirements 2026-27 · program_key=user-experience-bachelor-of-science · requirement_key=program-requirements-57-hours-advanced-computer-science-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/user-experience-bs/ (sha256 eed3996a11f0)
  - courses: CS 331 ⟵ “CS 331 - Data Structures”
  - courses: CS 351 ⟵ “CS 351 - Database Management Systems I”
  - courses: CS 360 ⟵ “CS 360 - Software Engineering I”
### `d26804cdec3d0334` Western Kentucky University — degree_requirements 2026-27 · program_key=theatre-bachelor-of-arts · requirement_key=program-requirements-45-hours-design-and-production [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/theatre-ba/ (sha256 1b9c0be3c605)
  - courses: THEA 219 ⟵ “THEA 219 - Design I (3 credit hours)”
  - courses: PERF 120 ⟵ “PERF 120 - Rehearsal and Production (1 credit hour)”
  - courses: PERF 220 ⟵ “PERF 220 - Production Lab I (0.5 to 1 credit hour: take once as a 1 credit class, or twice as a 0.5 credit class)”
  - courses: PERF 320 ⟵ “PERF 320 - Production Lab II (0.5 to 1 credit hour: take once as a 1 credit class, or twice as a 0.5 credit class)”
  - courses: THEA 222 ⟵ “THEA 222 - Stagecraft (3 credit hours)”
  - courses: THEA 241 ⟵ “THEA 241 - Costume Technology (3 credit hours)”
  - courses: THEA 250 ⟵ “THEA 250 - Stage Electrics (3 credit hours)”
  - courses: THEA 311 ⟵ “THEA 311 - Stage Management (3 credit hours)”
  - courses: PERF 321 ⟵ “PERF 321 - Production Lab III (0.5 to 1 credit hour)”
  - courses: PERF 420 ⟵ “PERF 420 - Production Lab IV (0.5 to 1 credit hour)”
  - courses: PERF 340 ⟵ “PERF 340 - Performance Lab I (0.5 to 1 credit hour)”
  - courses: PERF 341 ⟵ “PERF 341 - Performance Lab II (0.5 to 1 credit hour)”
  - courses: PERF 430 ⟵ “PERF 430 - Production Lab VI (0.5 to 1 credit hour)”
  - courses: PERF 331 ⟵ “PERF 331 - Dramaturgy Lab (0.5, 1, or 2 credit hours)”
### `d9f83fc5f2d77fb6` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-track-31-hours-logic-epistemology-and-metaphysics [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PHIL 214 ⟵ “PHIL 214 - Logic, Argument, and Practical Reasoning”
  - courses: PHIL 215 ⟵ “PHIL 215 - Symbolic Logic”
  - courses: PHIL 315 ⟵ “PHIL 315 - Philosophy of Religion”
  - courses: PHIL 330 ⟵ “PHIL 330 - Philosophy of Science”
  - courses: PHIL 332 ⟵ “PHIL 332 - Philosophy of Mind: Minds and Machines”
  - courses: PHIL 334 ⟵ “PHIL 334 - Philosophy of Language”
  - courses: PHIL 404 ⟵ “PHIL 404 - Metaphysics and Epistemology”
  - courses: PHIL 415 ⟵ “PHIL 415 - Advanced Logic”
### `dceaf1f2d9962d6a` Western Kentucky University — degree_requirements 2026-27 · program_key=english-bachelor-of-arts · requirement_key=program-requirements-42-hours-language-course [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/english/english-ba/ (sha256 fa1dc335f1c4)
  - courses: ENG 204 ⟵ “ENG 204 - English Language”
### `ddeeafc53069e0b4` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-for-health-sciences-and-health-care-concentration-chem-107-chem-108 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
  - courses: CHEM 116 ⟵ “CHEM 116 - Introduction to College Chemistry”
### `de5c21ae3e7461ca` Western Kentucky University — degree_requirements 2026-27 · program_key=film-bachelor-of-arts-667p-667 · requirement_key=program-requirements-36-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/film-ba/ (sha256 d1378fd4bf29)
  - courses: FILM 367 ⟵ “FILM 367 - Introduction to Film Genres”
  - courses: FILM 399 ⟵ “FILM 399 - Special Topics in Film”
  - courses: FILM 469 ⟵ “FILM 469 - Topics in World Cinema”
  - courses: ENG 309 ⟵ “ENG 309 - Documentary Film”
  - courses: ENG 365 ⟵ “ENG 365 - Film Adaptation”
### `e0e61dbaecebf691` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=program-requirements-31-hours-required-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
  - courses: ANTH 120 ⟵ “ANTH 120 - Introduction to Cultural Anthropology”
  - courses: ANTH 125 ⟵ “ANTH 125 - Introduction to Biological Anthropology”
  - courses: ANTH 130 ⟵ “ANTH 130 - Introduction to Archaeology”
  - courses: ANTH 135 ⟵ “ANTH 135 - Introduction to Linguistic Anthropology”
  - courses: ANTH 399 ⟵ “ANTH 399 - Field Methods in Ethnography”
  - courses: ANTH 499 ⟵ “ANTH 499 - Senior Seminar”
### `e7c9908af69b393b` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=program-requirements-36-73-hours-elective-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
  - section: program-requirements-36-73-hours-elective-courses ⟵ “Program Requirements (36-73 hours) — Elective Courses”
### `eb7bf78787df14b8` Western Kentucky University — degree_requirements 2026-27 · program_key=journalism-bachelor-of-arts-736p-736 · requirement_key=program-requirements-42-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/journalism-ba/ (sha256 255ceb1183cf)
  - courses: SMC 101 ⟵ “SMC 101 - Understanding Media Content, Ethics and Technology”
  - courses: SMC 102 ⟵ “SMC 102 - Media Content, Collaboration and Community”
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: JOUR 202 ⟵ “JOUR 202 - Introduction to News Writing”
  - courses: SMC 301 ⟵ “SMC 301 - Mass Communication Law and Ethics”
  - courses: JOUR 302 ⟵ “JOUR 302 - Intermediate Reporting”
  - courses: JOUR 323 ⟵ “JOUR 323 - Multiplatform News Presentation”
  - courses: JOUR 325 ⟵ “JOUR 325 - Feature Writing”
  - courses: VJP 261 ⟵ “VJP 261 - Mobile Media Storytelling”
  - courses: VJP 332 ⟵ “VJP 332 - Visual Media Editing and Design”
  - courses: BCOM 264 ⟵ “BCOM 264 - Digital Video Production and Distribution”
### `ebbec5ae31f5c7db` Western Kentucky University — degree_requirements 2026-27 · program_key=journalism-bachelor-of-arts-736p-736 · requirement_key=program-requirements-42-hours-elective-1 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/journalism-ba/ (sha256 255ceb1183cf)
  - courses: BCOM 325 ⟵ “BCOM 325 - Survey of Electronic Media Writing”
  - courses: BCOM 368 ⟵ “BCOM 368 - News Videography and Editing”
  - courses: JOUR 467 ⟵ “JOUR 467 - News / Editorial Internship Practicum”
  - courses: JOUR 481 ⟵ “JOUR 481 - Problems in Mass Communication”
  - courses: JOUR 491 ⟵ “JOUR 491 - Internship or Practicum”
  - courses: ENG 311 ⟵ “ENG 311 - Creative Nonfiction Writing”
  - courses: ENG 402 ⟵ “ENG 402 - Editing and Publishing”
  - courses: ENG 403 ⟵ “ENG 403 - Writing Memoir and Autobiography”
  - courses: FLK 373 ⟵ “FLK 373 - Folklore and the Media”
  - courses: SMC 402 ⟵ “SMC 402 - First Amendment Research and Reporting”
  - courses: SOM 421 ⟵ “SOM 421 - American News Media History”
### `ec3ae15fae62d3d1` Western Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-science · requirement_key=program-requirements-75-hours-accounting-major-42-hrs [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/accounting/accounting-bs/ (sha256 5dadf9a49ed6)
  - courses: ACCT 220 ⟵ “ACCT 220 - Principles of Financial Accounting”
  - courses: ACCT 300 ⟵ “ACCT 300 - Intermediate Financial Accounting I”
  - courses: ACCT 301 ⟵ “ACCT 301 - Intermediate Financial Accounting II”
  - courses: ACCT 303 ⟵ “ACCT 303 - Intermediate Financial Accounting III”
  - courses: ACCT 310 ⟵ “ACCT 310 - Managerial Cost Accounting”
  - courses: ACCT 311 ⟵ “ACCT 311 - Managerial Cost Accounting II”
  - courses: ACCT 312 ⟵ “ACCT 312 - Accounting Information Systems”
  - courses: ACCT 430 ⟵ “ACCT 430 - Federal Income Taxation I”
  - courses: ACCT 450 ⟵ “ACCT 450 - Auditing and Assurance Services”
  - courses: ACCT 401 ⟵ “ACCT 401 - Business Combinations and Related Topics”
  - courses: ACCT 410 ⟵ “ACCT 410 - Critical Thinking in Managerial Accounting”
  - courses: ACCT 412 ⟵ “ACCT 412 - Data Analysis for Accounting”
  - courses: ACCT 413 ⟵ “ACCT 413 - Accounting Analytics”
  - courses: ACCT 420 ⟵ “ACCT 420 - Governmental and Not for Profit Accounting”
  - courses: ACCT 431 ⟵ “ACCT 431 - Federal Income Taxation II”
  - courses: BDAN 430 ⟵ “BDAN 430 - Data Visualization”
  - courses: ACCT 440 ⟵ “ACCT 440 - Business Law for the Accounting Professional”
  - courses: MGT 200 ⟵ “MGT 200 - Legal Environment of Business”
  - courses: MGT 301 ⟵ “MGT 301 - Business Law”
### `ec9722fd36a47bd2` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-politics-and-policy-track-31-hours-senior-seminar [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PHIL 496 ⟵ “PHIL 496 - Senior Seminar”
### `eca34e67e55f7e5a` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=elective-courses-chin-200-level-courses-other-than-chin-201-chin-202-3-hours-max-2 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
  - section: elective-courses-chin-200-level-courses-other-than-chin-201-chin-202-3-hours-max-2 ⟵ “Elective Courses — CHIN 200-level courses other than CHIN 201 / CHIN 202 (3 hours maximum)”
### `edd83d658086f2e8` Western Kentucky University — degree_requirements 2026-27 · program_key=social-studies-bachelor-of-arts · requirement_key=program-requirements-51-hours-economics [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/social-studies-ba/ (sha256 02fc45f9924f)
  - courses: ECON 202 ⟵ “ECON 202 - Principles of Economics (Micro)”
  - courses: ECON 203 ⟵ “ECON 203 - Principles of Economics (Macro)”
### `f24a93a106dac7f0` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-track-31-hours-senior-seminar [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - courses: PHIL 496 ⟵ “PHIL 496 - Senior Seminar”
### `f9802757c3ec1e2f` Western Kentucky University — degree_requirements 2026-27 · program_key=interior-design-and-fashion-studies-bachelor-of-science · requirement_key=fashion-studies-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/interior-design-fashion-studies-bs/ (sha256 7a57d16420c2)
  - courses: IDFS 131 ⟵ “IDFS 131 - Basic Apparel Construction”
  - courses: ART 130 ⟵ “ART 130 - Two-Dimensional Design Foundations”
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: IDFS 165 ⟵ “IDFS 165 - Fashion Appreciation”
  - courses: IDFS 223 ⟵ “IDFS 223 - Textiles”
  - courses: IDFS 244 ⟵ “IDFS 244 - Illustrator for Fashion Studies”
  - courses: IDFS 231 ⟵ “IDFS 231 - Textile and Apparel Quality Analysis”
  - courses: IDFS 322 ⟵ “IDFS 322 - Merchandising I for IDFS”
  - courses: IDFS 332 ⟵ “IDFS 332 - History of 20th Century Fashion”
  - courses: IDFS 325 ⟵ “IDFS 325 - Sustainability in the Fashion Industry”
  - courses: IDFS 333 ⟵ “IDFS 333 - Fashion Fundamentals”
  - courses: IDFS 335 ⟵ “IDFS 335 - Apparel Design Production”
  - courses: IDFS 410 ⟵ “IDFS 410 - IDFS Internship”
  - courses: IDFS 421 ⟵ “IDFS 421 - Portfolio Design”
  - courses: IDFS 431 ⟵ “IDFS 431 - Clothing and Human Behavior”
  - courses: IDFS 433 ⟵ “IDFS 433 - Fashion Synthesis”
  - courses: IDFS 436 ⟵ “IDFS 436 - Global Apparel Merchandising & Promotion”
  - courses: IDFS 437 ⟵ “IDFS 437 - Fashion's Luxury Landscape”
  - courses: IDFS 438 ⟵ “IDFS 438 - Merchandising II for IDFS”
  - courses: MGT 210 ⟵ “MGT 210 - Organization and Management”
  - courses: MKT 220 ⟵ “MKT 220 - Basic Marketing Concepts”
  - courses: MKT 331 ⟵ “MKT 331 - Social Media Marketing”
  - courses: IDFS 226 ⟵ “IDFS 226 - Fashion Illustration”
  - courses: IDFS 310 ⟵ “IDFS 310 - Pattern Making and Draping”
  - courses: IDFS 423 ⟵ “IDFS 423 - Human Environment Study Tour”
  - … 14 more rows
### `f9cbf8410eb47cd8` Western Kentucky University — degree_requirements 2026-27 · program_key=philosophy-bachelor-of-arts · requirement_key=philosophy-track-31-hours-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/philosophy-ba/ (sha256 281635ca0214)
  - section: philosophy-track-31-hours-electives ⟵ “Philosophy Track (31 hours) — Electives”
### `feabc26c27f67b8b` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-communication-concentration-strategic-communication [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
  - courses: PR 255 ⟵ “PR 255 - Fundamentals of Public Relations”
  - courses: COMM 346 ⟵ “COMM 346 - Persuasion”
  - courses: COMM 364 ⟵ “COMM 364 - Crisis Communication”
### `ffaabb74f995d9e9` Western Kentucky University — degree_requirements 2026-27 · program_key=film-bachelor-of-arts-667p-667 · requirement_key=program-requirements-36-hours-thea-bcom-303 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/film-ba/ (sha256 d1378fd4bf29)
  - courses: ENG 359 ⟵ “ENG 359 - Topics in Scriptwriting”
  - courses: ANTH 449 ⟵ “ANTH 449 - Ethnographic Video Production”
  - courses: FILM 355 ⟵ “FILM 355 - Film Sound”
  - courses: FILM 499 ⟵ “FILM 499 - Directed Study in Film”
  - courses: FILM 489 ⟵ “FILM 489 - Thesis Development”

## Exceptions (406)

### `070be4b9c26f27a9` state-KY — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://cpe.ky.gov/policies/academicaffairs/dualcreditpolicy.pdf (sha256 c804da67296a)
- issues: semantic_review_required
- checks: {"effective": 2, "requirements": 15}
  - statements.effective: 2 ⟵ “Effective dual credit systems have impacts both at the secondary and postsecondary levels and provide the opportunity for collaboration between the K-12 and higher education systems, as well as among P-20, policy, workforce, family and community partners.”
  - statements.requirements: 15 ⟵ “Dual credit courses must meet the same student learning outcomes and be of the same quality and rigor as courses taught to traditional college students at participating B.”
### `1b48dbb2fd25abe7` state-KY — state_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://kctcs.edu/dual-credit/tuition-and-scholarship-information.aspx (sha256 7ad92b490464)
- issues: semantic_review_required
- checks: {"exceptions": 1, "requirements": 9}
  - statements.requirements: 9 ⟵ “If you want to take a course that is not part of the dual credit program, you may enroll as a dually enrolled student if you meet the admission requirements for non-degree/non-credential students.”
  - statements.exceptions: 1 ⟵ “However, if we have not received information about your scholarship by the established deadlines, a bill will be generated.”
### `3664d5e143b57268` state-KY — state_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_title)
- source: https://www.kheaa.com/web/resources/pdf/DualCredit_App_HomeSchoolers.pdf (sha256 f32131601615)
- issues: semantic_review_required
- checks: {"requirements": 4}
  - statements.requirements: 4 ⟵ “Subject to available funding, scholarships will be awarded to eligible students on a ¿rst-come, ¿rst-served basis, with 12th- graders receiving top priority.”
### `38a3d38732d76285` state-KY — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://kctcs.edu/dual-credit/ (sha256 140e31f0439e)
- issues: semantic_review_required, conflicting_sources:https://cpe.ky.gov/ourwork/dualcredit.html
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “AboutEducation & TrainingAdmissionsAffording College AboutEducation & TrainingAdmissionsAffording College Kentucky Community & Technical College System>Dual Credit In KCTCS dual-credit programs, you earn credit that goes toward your high school requirements; and at the same time, you also earn colle”
### `4a5be5947c0a86f6` state-KY — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://apps.legislature.ky.gov/law/kar/titles/013/002/070/ (sha256 56fef8fe0780)
- issues: semantic_review_required
- checks: {"effective": 1, "exceptions": 10, "requirements": 20}
  - statements.effective: 1 ⟵ “Title 013 Chapter 2 Regulation 070 • Kentucky Administrative Regulations • Legislative Research Commission Last Effective Dates, Expirations, and Certifications This is how this document appeared before it was engrossed. 13 KAR 2:070.Administrative hearing procedures for determination of residency s”
  - statements.requirements: 20 ⟵ “The Administrative Hearings Act, codified in KRS Chapter 13B, sets forth due process hearing requirements for Kentucky agencies engaged in regulatory activities which adjudicate the legal rights, duties, privileges, or immunities of persons.”
  - statements.exceptions: 10 ⟵ “Posthearing Procedures; Exceptions; Jurisdiction.”
### `528f3eebaadeb441` state-KY — state_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://cpe.ky.gov/ourwork/dualcredit.html (sha256 4f950c6e8f81)
- issues: semantic_review_required, conflicting_sources:https://kctcs.edu/dual-credit/
- checks: {"exceptions": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Advanced Placement (AP) courses are rigorous study (or honors) courses offered for high school credit but require passing a separate test to earn college credit.”
  - statements.exceptions: 1 ⟵ “However, outcomes vary based on race, gender and income.”
### `64a7eca2d7bb5758` state-KY — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://cpe.ky.gov/policies/academicaffairs/transferappealsprocess.pdf (sha256 3e8ee28c1810)
- issues: semantic_review_required
- checks: {"effective": 1, "requirements": 15}
  - statements.requirements: 15 ⟵ “This person must be well versed in details of the General Education Transfer Policy and Implementation Guidelines and is responsible for corresponding with students regarding institutional and statewide transfer appeals processes.”
  - statements.effective: 1 ⟵ “A second state-level review will be available for transfer decisions The next revision of the General Education Transfer Policy and Implementation Guidelines occurred following the passage of KRS 164.2591, with an effective date of fall 2012.”
### `6b83d0e1648b8e53` state-KY — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://apps.legislature.ky.gov/law/kar/titles/013/002/045/ (sha256 600b89ac91e7)
- issues: semantic_review_required
- checks: {"effective": 1, "exceptions": 10, "guarantees": 2, "requirements": 56}
  - statements.effective: 1 ⟵ “Title 013 Chapter 2 Regulation 045 • Kentucky Administrative Regulations • Legislative Research Commission Last Effective Dates, Expirations, and Certifications This is how this document appeared before it was engrossed. 13 KAR 2:045.Determination of residency status for admission and tuition assess”
  - statements.requirements: 56 ⟵ “KRS 13B, 164.020, 164.030, 164A.330(6), 38 U.S.C. 3301-3325 KRS 164.020(8) requires the Council on Postsecondary Education to determine tuition and approve the minimum qualifications for admission to a state postsecondary education institution and authorizes the Council to set different tuition amou”
  - statements.exceptions: 10 ⟵ “In accordance with the duties established in KRS 164.020, the Council on Postsecondary Education may require a student who is neither domiciled in, nor a resident of, Kentucky to meet higher admission standards and to pay a higher level of tuition than resident students.”
  - statements.guarantees: 2 ⟵ “An institution shall have written procedures for the conduct of a formal hearing that have been adopted by the board of trustees or regents, as appropriate, and that provide for: A hearing officer to make a recommendation on a residency appeal; Guarantees of due process to a student that include: Th”
### `8a0aeae1916281e0` state-KY — state_policies 2012-13 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=50209 (sha256 561249336bc9)
- issues: stale_year_label:2012-13, semantic_review_required
- checks: {"effective": 2, "requirements": 2}
  - statements.requirements: 2 ⟵ “Where applicable, curricula shall be reviewed to determine comparability of core content standards required under KRS 164.302.”
  - statements.effective: 2 ⟵ “Acts ch. 57, sec. 1, effective July 15, 2020. -- Created 2010 Ky.”
### `9caac0de7a4a349f` state-KY — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://cpe.ky.gov/policies/academicaffairs/genedtransferpolicy.pdf (sha256 11e4768af0fa)
- issues: semantic_review_required, conflicting_sources:https://cpe.ky.gov/policies/academicaffairs/curricularchangesform.pdf
- checks: {"effective": 4, "guarantees": 3, "requirements": 33}
  - statements.effective: 4 ⟵ “The updated General Education Transfer Policy and Implementation Guidelines (2012) will be in effect for all students admitted for the fall semester 2012.”
  - statements.requirements: 33 ⟵ “Where applicable curricula shall be reviewed to determine comparability of core content standards required under KRS164.302.”
  - statements.guarantees: 3 ⟵ “If the receiving institution’s general education program requires a sum of hours that is less than the total the student has taken Guidelines for Implementation of the General Education Transfer Policy                       Page 4 at the sending institution, the excess hours will be accepted for tra”
### `b5ed55ef17fe145b` state-KY — state_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.kheaa.com/web/scholarships-grants.faces (sha256 211b6c8e3b50)
- issues: semantic_review_required
- checks: {"exceptions": 1, "guarantees": 2, "requirements": 77}
  - statements.requirements: 77 ⟵ “A studentâs KEES award expires when the first of the following three conditions are met: Eight (8) semesters of KEES funding has been used; or Five (5) years have passed since high school graduation; or To be eligible for a KEES yearly GPA award, a high school student must: Be a U.S. citizen, nati”
  - statements.guarantees: 2 ⟵ “There is no guarantee of funding or eligibility.”
  - statements.exceptions: 1 ⟵ “However, it is recommended applicants take steps to be accepted at a participating institution prior to the December 1 deadline.”
### `d29efcebb1478321` state-KY — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://www.kheaa.com/web/resources/pdf/Optometry_Scholarship_Application.pdf (sha256 6b4aac9ff478)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “I understand that residency determinations are made in accordance with 13 KAR 2:045 and that KHEAA reserves the right to request additional information as needed for my residency and/or scholarship eligibility determination.”
### `d393008ff4dbae88` state-KY — state_policies 2023-24 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.kheaa.com/web/plan-for-future.faces (sha256 61491277fb5d)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"exceptions": 2, "guarantees": 1, "requirements": 24}
  - statements.requirements: 24 ⟵ “You have different choices after high school, but many careers require additional education after you finish high school.”
  - statements.guarantees: 1 ⟵ “See if your current school has agreements with those schools that spell out what will transfer and how the process works.”
  - statements.exceptions: 2 ⟵ “However, the information may change without notice based on a number of factors, including federal and state legislative changes and federal and state regulatory changes.”
### `e22ffad834b1ed66` state-KY — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://cpe.ky.gov/policies/academicaffairs/transfer-mou-kctcs-kde.pdf (sha256 bea719a713dd)
- issues: semantic_review_required
- checks: {"effective": 1, "requirements": 2}
  - statements.requirements: 2 ⟵ “WHEREAS, the parties enter into this Agreement for the purpose of (1) developing and implementing a statewide standardized articulation agreement between public colleges and universities and the Kentucky Department of Education for each approved high school career pathway that leads to a postseconda”
  - statements.effective: 1 ⟵ “The Agreement shall be reviewed for revisions and amendments no less than every three This Agreement shall be effective upon execution by all parties and remain in effect until such time as it is canceled by any party in writing upon ninety (90) days written notice.”
### `f42eaf0d02969f87` state-KY — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://cpe.ky.gov/policies/academicaffairs/curricularchangesform.pdf (sha256 13964afba0f7)
- issues: semantic_review_required, conflicting_sources:https://cpe.ky.gov/policies/academicaffairs/genedtransferpolicy.pdf
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Please explain proposed change(s) to student learning outcomes, prerequisites, or major requirements that may impact transfer.”
### `d5f9ea9dad6e7c41` Alice Lloyd College — appeals 2026-27 [new] (source_unlabeled)
- source: https://alc.edu/satisfactory-academic-progress-policy/ (sha256 516af3e4c6fd)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students on SAP Suspension may: Continue attending using other funding sources while earning the necessary GPA or hours to regain eligibility, or Submit a written SAP appeal All notifications are sent both by letter to the student’s home address and by email to their ALC email address.”
### `27d67221f910214f` Asbury University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.asbury.edu/wp-content/uploads/2025/01/Satisfactory-Academic-Progress-Policy-11-12.pdf (sha256 5eb7653633c1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals should be in writing, designated “SAP Appeal” and sent to the financial aid office at Asbury University.”
### `d245ff2f791eeb2b` Asbury University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.asbury.edu/online/cost-and-aid/ (sha256 c926a15e6c80)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Complete a FAFSA Note: To minimize errors and delays in processing, we encourage students to use the updated secure IRS Data Retrieval Tool when completing the FAFSA, automatically linking your previous year’s tax return. 2025-2026 2025-26 Financial Aid & Professional Judgement Form for DEPENDENT 2025-26 Financial Aid & Professional Judgement Form for INDEPENDENT Step 2: Complete the Asbury online”
  - sentence: professional_judgment ⟵ “Financial Aid Appeal and Professional Judgement If you feel that the information submitted on the FAFSA does not accurately portray your current financial situation, a professional judgment may be warranted.”
### `4ecf31efe5c573a5` Ashland Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ashland.kctcs.edu/affording-college/professional-judgement.aspx (sha256 a8bf20f89a0f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment is comprised of two components, unusual circumstances and special circumstances.”
  - sentence: professional_judgment ⟵ “IRA, pension distribution, back-year Social Security payments) Tuition expenses at an elementary or secondary school for siblings of the student Child or dependent care expenses Additional people from the student’s household in college At the discretion of the Director, other circumstances may be considered if they are appropriate, reasonable adjustments, to reflect a student’s situation more accu”
### `64790c15b0aa7755` Ashland Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ashland.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 4ce71fa89a8b)
- issues: semantic_review_required, conflicting_sources:https://ashland.kctcs.edu/affording-college/paying-for-college/satisfactory-academic-progress/sap-appeal-instructions.aspx
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “SAP Meeting Dates SAP appeals are generally reviewed within 3-5 business days after due date.”
  - sentence: sap_appeal ⟵ “SAP appeal decisions are delivered via KCTCS student email.”
  - sentence: sap_appeal ⟵ “To appeal, students must complete a SAP Appeal Form available in their Student Self-Service.”
  - sentence: sap_appeal ⟵ “The appeal will be evaluated by the SAP Appeals Committee of the home college.”
  - sentence: sap_appeal ⟵ “Students are responsible for payment arrangements with the institution pending a decision of the appeals committee. 1.7.2 Probation and Reinstatement of Aid SAP appeals will be evaluated by the college SAP Appeal Committee.”
  - sentence: sap_appeal ⟵ “If the SAP appeal is denied, the student: is not eligible for federal student aid will remain ineligible until they are again in compliance with SAP standards. may continue to attend college at their own expense. who is suspended from financial aid and achieves SAP standards without the assistance of federal financial aid, may request to be evaluated for re-instatement?”
### `c9c33ce771818192` Ashland Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ashland.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 4ce71fa89a8b)
- issues: semantic_review_required, conflicting_sources:https://ashland.kctcs.edu/affording-college/professional-judgement.aspx
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Appeal Process When a student loses Federal Student Aid (FSA) eligibility and are put on SAP Suspense Status because he/she failed to make satisfactory progress, the student may appeal that result on the basis of: his/her injury or illness, the death of a relative, or other extenuating/special circumstance that prevented them from meeting SAP standards.”
  - sentence: need_based_special_circumstances ⟵ “Extenuating/special circumstances are defined as situations beyond the student's control that created an undue hardship and caused the student's inability to meet satisfactory academic progress standards.”
  - sentence: need_based_special_circumstances ⟵ “Failure to meet SAP standards for the next term of enrollment will result in immediate suspension and require an approved appeal to regain eligibility. 1.7 Appeal Process When a student loses Federal Student Aid (FSA) eligibility and are put on SAP Suspense Status because he/she failed to make satisfactory progress, the student may appeal that result on the basis of: his/her injury or illness, the”
  - sentence: need_based_special_circumstances ⟵ “Extenuating/special circumstances are defined as situations beyond the student's control that created an undue hardship and caused the student's inability to meet satisfactory academic progress standards.”
### `de5658bcb51a0e98` Ashland Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ashland.kctcs.edu/affording-college/professional-judgement.aspx (sha256 a8bf20f89a0f)
- issues: semantic_review_required, conflicting_sources:https://ashland.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Unusual Circumstances refer to the conditions that justify an aid administrator to make an adjustment to a student’s dependency status based on a unique situation, this is more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances include but not limited to: Loss or change of employment Reduction in income or assets Loss or change in amount of child support, Social Security, or other benefits Divorce or separation of parents Death of parent(s) Unusual medical expenses (not covered by insurance) One-time taxable income used for life-changing events (e.g.”
### `fc6bbce88dbb255e` Ashland Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ashland.kctcs.edu/affording-college/paying-for-college/satisfactory-academic-progress/sap-appeal-instructions.aspx (sha256 1ab60a1a7d8e)
- issues: semantic_review_required, conflicting_sources:https://ashland.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “CompletetheOnline SAP Appeal Request, via your Student Self-Service account.”
  - sentence: sap_appeal ⟵ “Incomplete SAP Appeal Requests will have a delay in processing.”
  - sentence: sap_appeal ⟵ “SAP Appeal Requests should be submitted prior to any tuition payment cancellation deadlines.”
  - sentence: sap_appeal ⟵ “SAP Appeal approval or denial decisions will be posted to the Online SAP Appeal Request Confirmation screen in Self-Service.”
### `382687534ce8510b` Bellarmine University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bellarmine.edu/financial-aid/progress-certificate.php (sha256 4dacef089cdc)
- issues: semantic_review_required, conflicting_sources:https://www.bellarmine.edu/financial-aid/progress-undergrad.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Right to Appeal If there were extenuating circumstances (injury, illness or death of a family member) that prevented you from meeting the standards of our Satisfactory Academic Progress Policy, then you have a right to file an appeal with the Committee for Financial Aid Appeals.”
### `89f1e53b60ac1197` Bellarmine University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bellarmine.edu/financial-aid/progress-undergrad.php (sha256 55a2947d8151)
- issues: semantic_review_required, conflicting_sources:https://www.bellarmine.edu/financial-aid/progress-certificate.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Right to Appeal If there were extenuating circumstances (injury, illness, death of a relative) that prevented you from meeting the standards of our Satisfactory Academic Progress Policy, then you have a right to file an appeal with the Committee for Financial Aid Appeals.”
### `6946a39e8935ba8f` Berea College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.berea.edu/student-financial-aid/appeal-for-special-circumstances (sha256 a1b797ea770d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Appeal for Special Circumstances - Berea College For You MyBerea News Events The Berea Model Fully Funded Degree Impartial Love Work to Learn Serving Appalachia Berea College - A college like no other.”
  - sentence: need_based_special_circumstances ⟵ “Life at Berea Academics Admissions & Aid Giving More Berea.edu/Student Financial Aid Appeal for Special Circumstances Families may request an additional review of their FAFSA information if there are exceptional circumstances that have impacted your family’s ability to pay for your college education.”
### `93e503fa21d780bb` Berea College — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.berea.edu/student-financial-aid (sha256 7cf730f3b511)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Life at Berea Academics Admissions & Aid Giving More Student Financial Aid Appeal for Special Circumstances Berea College Cost of Attendance for 2025-2026 (Fall/Spring) Berea College Cost of Attendance for 2026-2027 (Fall/Spring) Military & Veterans Affairs Satisfactory Academic Progress Staff Tax Information Types of Financial Aid Understanding Your Financial Aid Award Verification Additional Res”
### `accc2728cd533353` Berea College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.berea.edu/student-financial-aid/cost-of-attendance (sha256 ff8271dac75d)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition & Fees*: 55480 ⟵ “Tuition & Fees* | $55,480”
  - column:Housing: 5000 ⟵ “Housing | $5,000”
  - column:Food: 4142 ⟵ “Food | $4,142”
  - column:Books and Supplies: 750 ⟵ “Books and Supplies | $750”
  - column:Transportation: 1350 ⟵ “Transportation | $1,350”
  - column:Personal: 1800 ⟵ “Personal | $1,800”
  - column:Total Cost of Attendance: 68522 ⟵ “Total Cost of Attendance | $68,522”
  - column:Total Direct Costs: 64622 ⟵ “Total Direct Costs | $64,622”
  - column:Total Indirect Costs: 3900 ⟵ “Total Indirect Costs | $3,900”
### `142335823b47a57a` Big Sandy Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://bigsandy.kctcs.edu/affording-college/satisfactory-academic-progress/sap-full.aspx (sha256 1d04001ae691)
- issues: semantic_review_required, conflicting_sources:https://bigsandy.kctcs.edu/affording-college/tuition-costs/forms-documents.aspx
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “The appeal will be evaluated by the SAP Appeals Committee of the home college.”
  - sentence: sap_appeal ⟵ “Students are responsible for payment arrangements with the institution pending a decision of the appeals committee. 1.7.2 Probation and Reinstatement of Aid SAP appeals will be evaluated by the college SAP Appeal Committee.”
  - sentence: sap_appeal ⟵ “If the SAP appeal is denied, the student: is not eligible for federal student aid will remain ineligible until they are again in compliance with SAP standards. may continue to attend college at their own expense. who is suspended from financial aid and achieves SAP standards without the assistance of federal financial aid, may request to be evaluated for reinstatement.”
  - sentence: sap_appeal ⟵ “NOTE: Students are responsible for all expenses such as tuition, fees, books, and supplies pending the decision of the SAP Appeals Committee and must contact the Business Affairs Office to make payment arrangements with the institution.”
  - sentence: sap_appeal ⟵ “Decisions made by the SAP Appeals Committee are final and are not subject to further appeal. 1.8 REPEAT CLASS POLICY Federal student aid may only pay for the first repeat one of any previously passed course.”
### `64252f20b77b208b` Big Sandy Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://bigsandy.kctcs.edu/affording-college/satisfactory-academic-progress/sap-full.aspx (sha256 1d04001ae691)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Failure to meet SAP standards for the next term of enrollment will result in immediate suspension and require an approved appeal to regain eligibility. 1.7 Appeal Process When a student loses Federal Student Aid (FSA) eligibility and are put on SAP Suspense Status because he/she failed to make satisfactory progress, the student may appeal that result on the basis of: his/her injury or illness, the”
  - sentence: need_based_special_circumstances ⟵ “Extenuating/special circumstances are defined as situations beyond the student's control that created an undue hardship and caused the student's inability to meet satisfactory academic progress standards.”
### `a3f6a2f4910d4206` Big Sandy Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://bigsandy.kctcs.edu/affording-college/tuition-costs/forms-documents.aspx (sha256 a9d7a54f3ea4)
- issues: semantic_review_required, conflicting_sources:https://bigsandy.kctcs.edu/affording-college/satisfactory-academic-progress/sap-full.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeal Online Instructions Big Sandy Community and Technical College 1 Bert T.”
### `1ca756fb940c627d` Big Sandy Community and Technical College — credit_policies 2016-17 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://bigsandy.kctcs.edu/admissions/information-for/dual-credit-faq.aspx (sha256 c75123ae87c8)
- issues: stale_year_label:2016-17
- checks: {"fields": ["state_grant_accepted"], "tiers": 0}
  - state_grant_accepted: True ⟵ “Can a student be eligible both for the Work Ready Dual Credit Scholarship and the”
  - state_grant_accepted: True ⟵ “Use the dual credit scholarship first.”
  - state_grant_accepted: True ⟵ “eligible? They are eligible dual credit and dual credit scholarship students if they are receiving”
### `9d4783d452e68c4a` Bluegrass Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://bluegrass.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 68238d6dfa3f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Submit a SAP appeal to the Financial Aid Office for review.”
  - sentence: sap_appeal ⟵ “What are some reasons for submitting a SAP appeal?”
  - sentence: sap_appeal ⟵ “How many times may I submit a SAP appeal?”
  - sentence: sap_appeal ⟵ “You may only submit one SAP appeal each semester.”
  - sentence: sap_appeal ⟵ “If you believe that you had extenuating circumstances that prohibited you from meeting SAP standards, you may appeal to the SAP Appeals Committee.”
  - sentence: sap_appeal ⟵ “You can review the SAP Appeal due dates on our Important Dates page.”
### `1d5cd4b06c6f5369` Bluegrass Community and Technical College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://bluegrass.kctcs.edu/admissions/information-for/international-students/cost/index.aspx (sha256 c085be54c251)
- issues: conflicting_sources:https://bluegrass.kctcs.edu/affording-college/tuition-costs/index.aspx
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition (2 semesters): 6960 ⟵ “Tuition (2 semesters) | $6,960* | $4,944*”
  - column:Living expenses: 9000 ⟵ “Living expenses | $9,000 | $9,000”
  - column:Books, Medical Insurance (required): 1500 ⟵ “Books, Medical Insurance (required) | $1,500 | $1,500”
  - column:TOTAL: 17460 ⟵ “TOTAL | $17,460** | $15,444*”
### `3a647f79a5ba6d81` Bluegrass Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://bluegrass.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 37dc921c21e1)
- issues: conflicting_sources:https://bluegrass.kctcs.edu/admissions/information-for/international-students/cost/index.aspx
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 17342 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - off_campus_not_with_family:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 21051 ⟵ “Total | $17,342 | $21,051 | $15,479”
  - other:Estimated Tuition: 6480 ⟵ “Estimated Tuition | $6,480 | $6,480 | $6,480”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 15479 ⟵ “Total | $17,342 | $21,051 | $15,479”
### `88102ab61763d174` Bluegrass Community and Technical College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://bluegrass.kctcs.edu/admissions/information-for/international-students/cost/index.aspx (sha256 c085be54c251)
- issues: conflicting_sources:https://bluegrass.kctcs.edu/affording-college/tuition-costs/index.aspx
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition (2 semesters): 4944 ⟵ “Tuition (2 semesters) | $6,960* | $4,944*”
  - column:Living expenses: 9000 ⟵ “Living expenses | $9,000 | $9,000”
  - column:Books, Medical Insurance (required): 1500 ⟵ “Books, Medical Insurance (required) | $1,500 | $1,500”
  - column:TOTAL: 15444 ⟵ “TOTAL | $17,460** | $15,444*”
### `a1926688488094d9` Bluegrass Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://bluegrass.kctcs.edu/affording-college/tuition-costs/index.aspx (sha256 37dc921c21e1)
- issues: conflicting_sources:https://bluegrass.kctcs.edu/admissions/information-for/international-students/cost/index.aspx
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - with_parents_or_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - with_parents_or_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - with_parents_or_family:Estimated Living Expenses (Food & Housing): 5578 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - with_parents_or_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - with_parents_or_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - with_parents_or_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - with_parents_or_family:Total: 15614 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - off_campus_not_with_family:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - off_campus_not_with_family:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - off_campus_not_with_family:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - off_campus_not_with_family:Estimated Living Expenses (Food & Housing): 9287 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - off_campus_not_with_family:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - off_campus_not_with_family:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - off_campus_not_with_family:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - off_campus_not_with_family:Total: 19323 ⟵ “Total | $15,614 | $19,323 | $13,751”
  - other:Estimated Tuition: 4752 ⟵ “Estimated Tuition | $4,752 | $4,752 | $4,752”
  - other:Estimated Fees: 192 ⟵ “Estimated Fees | $192 | $192 | $192”
  - other:Estimated Books/Supplies: 1268 ⟵ “Estimated Books/Supplies | $1,268 | $1,268 | $1,268”
  - other:Estimated Living Expenses (Food & Housing): 3715 ⟵ “Estimated Living Expenses (Food & Housing) | $5,578 | $9,287 | $3,715”
  - other:Estimated Personal Expenses: 1067 ⟵ “Estimated Personal Expenses | $1,067 | $1,067 | $1,067”
  - other:Estimated Transportation: 2699 ⟵ “Estimated Transportation | $2,699 | $2,699 | $2,699”
  - other:Estimated Loan Fees: 58 ⟵ “Estimated Loan Fees | $58 | $58 | $58”
  - other:Total: 13751 ⟵ “Total | $15,614 | $19,323 | $13,751”
### `m82835157ce0b3d6` Brescia University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.brescia.edu/kctcs-transfer-agreement/ (sha256 0771309fd794)
- issues: conflicting_values:max_transfer_credits
- checks: {"fields": ["max_transfer_credits", "min_grade"], "merged_pages": 3}
  - min_grade: C ⟵ “Students can transfer up to 77 hours of transfer credit on courses with a grade of C or higher.”
  - min_grade: C ⟵ “KCTCS Associate of Arts to Brescia University Bachelor Degrees KCTCS Associate of Science to Brescia University Bachelor Degrees Brescia University accepts up to 67 hours of transfer credit where a student made a grade of C or above.”
  - min_grade: C ⟵ “Brescia University accepts up to 67 hours of transfer credit where a student earned a grade of C or above.”
  - max_transfer_credits: 67 ⟵ “Brescia University accepts up to 67 hours of transfer credit where a student earned a grade of C or above.”
  - min_grade: C ⟵ “Brescia University accepts transfer credit from all regionally accredited institutions where a student has a grade of C or above.”
### `5510030395b60fdd` Campbellsville University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.campbellsville.edu/admission-and-aid/financial-aid/policies-and-procedures/index.html (sha256 9981d6768276)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “If you or your family have experienced a significant change in income, loss of employment, medical expenses, or other financial challenges not reflected in your FAFSA, you may be eligible for a Special Circumstances review.”
  - sentence: need_based_special_circumstances ⟵ “Fill out the form below, or visit our Special Circumstances dedicated page to contact the Financial Aid Office to learn more or begin the appeal process.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances We recognize that some students face unique personal situations that make it difficult, or impossible, to provide parental information on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If you are experiencing issues such as estrangement, abandonment, or other serious family challenges, you may qualify for an Unusual Circumstances review to be considered for independent status.”
  - sentence: need_based_special_circumstances ⟵ “Fill out the form below, or visit our Unusual Circumstances dedicated page to connect with our Financial Aid Office to discuss your options.”
### `64ec372c1b1b4b91` Campbellsville University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.campbellsville.edu/admission-and-aid/financial-aid/policies-and-procedures/index.html (sha256 9981d6768276)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Professional Judgement Professional Judgement is a process a student can apply for when they feel the information reported on the FAFSA no longer accurately reflects their financial situation.”
  - sentence: professional_judgment ⟵ “Professional Judgement Policy Procedure What is an SAI?”
  - sentence: professional_judgment ⟵ “My SAI is Greater than Zero If your SAI is greater than “0”, please read the information below about the conditions that do/do not qualify for a Professional Judgement.”
### `abe763ea0979da63` Campbellsville University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.campbellsville.edu/admission-and-aid/financial-aid/policies-and-procedures/index.html (sha256 9981d6768276)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal Federal regulations require that all students who receive any federal or state financial assistance make measurable academic progress towards a degree or certificate program at Campbellsville University.”
  - sentence: sap_appeal ⟵ “Right to Appeal: If there were extenuating circumstances (injury, illness, death of a relative) that prevented you from meeting the standards of our Satisfactory Academic Progress Policy, then you have a right to file an appeal with the Committee for Financial Aid Appeals.”
  - sentence: sap_appeal ⟵ “SAP Appeal Policies Satisfactory Academic Progress Undergraduate Satisfactory Academic Progress Policy Graduates Satisfactory Academic Progress Policy Cosmetology and Barbering Satisfactory Academic Progress HVAC Satisfactory Academic Progress LMR Special Circumstances At Campbellsville University, we understand that financial situations can change unexpectedly.”
### `58f381e29ff3ecde` Campbellsville University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.campbellsville.edu/admission-and-aid/financial-aid/cost-of-attendance.html (sha256 39b24257ce03)
- issues: arrangement_unlabeled
- checks: {"columns": 5, "components_reconcile": true, "rows": 9}
  - column:Tuition*: 23760 ⟵ “Tuition* | $23,760 | $23,760 | $23,760 | $23,760 | $23,760”
  - column:Food & Housing (off campus): 14644 ⟵ “Food & Housing (off campus) | $14,644 | $14,644 | $14,644 | $14,644 | $14,644”
  - column:Books, Course Materials, Supplies, & Equipment: 1850 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,850 | $2,200 | $1,000 | $1,000 | $1,000”
  - column:Personal Expenses: 3520 ⟵ “Personal Expenses | $3,520 | $3,520 | $3,520 | $3,520 | $3,520”
  - column:Transportation: 9476 ⟵ “Transportation | $9,476 | $9,476 | $9,476 | $9,476 | $9,476”
  - column:Loan Fees: 696 ⟵ “Loan Fees | $696 | $696 | $696 | $696 | $696”
  - column:Total COA: 53946 ⟵ “Total COA | $53,946 | $55,006 | $53,806 | $55,841 | $53,096”
  - column:Total Direct Cost: 23760 ⟵ “Total Direct Cost | $23,760 | $24,470 | $24,470 | $26,505 | $23,760”
  - column:Total Indirect Cost:: 30186 ⟵ “Total Indirect Cost: | $30,186 | $30,536 | $29,336 | $29,336 | $29,336”
  - column:Tuition*: 23760 ⟵ “Tuition* | $23,760 | $23,760 | $23,760 | $23,760 | $23,760”
  - column:Board Exam Fees: 710 ⟵ “Board Exam Fees |  | $710 | $710 | $2,745 | ”
  - column:Food & Housing (off campus): 14644 ⟵ “Food & Housing (off campus) | $14,644 | $14,644 | $14,644 | $14,644 | $14,644”
  - column:Books, Course Materials, Supplies, & Equipment: 2200 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,850 | $2,200 | $1,000 | $1,000 | $1,000”
  - column:Personal Expenses: 3520 ⟵ “Personal Expenses | $3,520 | $3,520 | $3,520 | $3,520 | $3,520”
  - column:Transportation: 9476 ⟵ “Transportation | $9,476 | $9,476 | $9,476 | $9,476 | $9,476”
  - column:Loan Fees: 696 ⟵ “Loan Fees | $696 | $696 | $696 | $696 | $696”
  - column:Total COA: 55006 ⟵ “Total COA | $53,946 | $55,006 | $53,806 | $55,841 | $53,096”
  - column:Total Direct Cost: 24470 ⟵ “Total Direct Cost | $23,760 | $24,470 | $24,470 | $26,505 | $23,760”
  - column:Total Indirect Cost:: 30536 ⟵ “Total Indirect Cost: | $30,186 | $30,536 | $29,336 | $29,336 | $29,336”
  - column:Tuition*: 23760 ⟵ “Tuition* | $23,760 | $23,760 | $23,760 | $23,760 | $23,760”
  - column:Board Exam Fees: 710 ⟵ “Board Exam Fees |  | $710 | $710 | $2,745 | ”
  - column:Food & Housing (off campus): 14644 ⟵ “Food & Housing (off campus) | $14,644 | $14,644 | $14,644 | $14,644 | $14,644”
  - column:Books, Course Materials, Supplies, & Equipment: 1000 ⟵ “Books, Course Materials, Supplies, & Equipment | $1,850 | $2,200 | $1,000 | $1,000 | $1,000”
  - column:Personal Expenses: 3520 ⟵ “Personal Expenses | $3,520 | $3,520 | $3,520 | $3,520 | $3,520”
  - column:Transportation: 9476 ⟵ “Transportation | $9,476 | $9,476 | $9,476 | $9,476 | $9,476”
  - … 23 more rows
### `17ef9988c49af240` Clear Creek Baptist Bible College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://ccbbc.edu/academics/programs/dual-enrollment (sha256 c4919a695086)
- issues: conflicting_values:max_credit_hours_per_term
- checks: {"fields": [], "tiers": 0}
  - max_credit_hours_per_term: 7 ⟵ “First semester dual enrollment students may enroll in no more than 7 hours. If the student’s GPA is 3.0 or higher after the first semester of enrollment, he or she may enroll in up to 12 hours each subsequent semester provided his or her GPA remains at 3.0 or better.”
  - max_credit_hours_per_term: 12 ⟵ “First semester dual enrollment students may enroll in no more than 7 hours. If the student’s GPA is 3.0 or higher after the first semester of enrollment, he or she may enroll in up to 12 hours each subsequent semester provided his or her GPA remains at 3.0 or better.”
### `94170ee3c5fb1e94` Eastern Kentucky University — academic_programs 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
- checks: {"courses": 46, "groups": 16, "groups_skipped": 2}
  - program_name: Management, Bachelor of Business Administration (B.B.A.) | Eastern Kentucky University Academic Catalog ⟵ “Management, Bachelor of Business Administration (B.B.A.) | Eastern Kentucky University Academic Catalog”
### `a52e4f5b172e749f` Eastern Kentucky University — academic_programs 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
- checks: {"courses": 48, "groups": 11, "groups_skipped": 3}
  - program_name: Accounting, Bachelor of Business Administration (B.B.A.) | Eastern Kentucky University Academic Catalog ⟵ “Accounting, Bachelor of Business Administration (B.B.A.) | Eastern Kentucky University Academic Catalog”
### `e77a3201655862a0` Eastern Kentucky University — academic_programs 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
- checks: {"courses": 61, "groups": 14, "groups_skipped": 3}
  - program_name: General Business, Bachelor of Business Administration (B.B.A.) | Eastern Kentucky University Academic Catalog ⟵ “General Business, Bachelor of Business Administration (B.B.A.) | Eastern Kentucky University Academic Catalog”
### `ec09abfe9ddf59d7` Eastern Kentucky University — academic_programs 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
- checks: {"courses": 36, "groups": 12, "groups_skipped": 2}
  - program_name: Finance, Bachelor of Business Administration (B.B.A.) | Eastern Kentucky University Academic Catalog ⟵ “Finance, Bachelor of Business Administration (B.B.A.) | Eastern Kentucky University Academic Catalog”
### `06b26d72a6572c17` Eastern Kentucky University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eku.edu/in/guides/professional-judgment-appeal/ (sha256 b419e3e07aa3)
- issues: semantic_review_required, conflicting_sources:https://www.eku.edu/in/bigecentral/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Professional judgment can be used in these situations to make changes on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “All Professional Judgment (PJ) Appeals for special circumstances are now submitted online via Slate.”
  - sentence: professional_judgment ⟵ “Professional Judgment Appeal Tools Email Office 365 myEKU Degree Works Banner Students Big E Central Class Schedule EKU Bookstore EKU Libraries Faculty Faculty Senate FCT& L Sponsored Programs Institutional Review Board Employees Human Resources Leave Reporting Employee Benefits Information Careers at EKU © 2026 All rights reserved Eastern Kentucky University | Equal Opportunity Statement | Privac”
### `30cf3abb45fc4228` Eastern Kentucky University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eku.edu/in/guides/satisfactory-academic-progress/ (sha256 73f5988154b1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “All three appeals must be reviewed by the Satisfactory Academic Progress Appeal Committee.”
  - sentence: sap_appeal ⟵ “Re-establishing Financial Aid Eligibility with an Appeal Students who are no longer meeting Satisfactory Academic Progress have the opportunity to appeal this decision if they have extenuating and documentable circumstances that prevented them from meeting federal standards.”
  - sentence: sap_appeal ⟵ “All three appeals must be reviewed by the Satisfactory Academic Progress Appeal Committee.”
  - sentence: sap_appeal ⟵ “Students who are approved for a SAP appeal will be notified via their EKU email and will be placed under financial aid probation.”
  - sentence: sap_appeal ⟵ “While under probation, final grades will be reviewed each semester to ensure the student meets the terms and conditions of their appeal approval (for example, passing all attempted hours with a 2.0 GPA for the term). | Semester of SAP Appeal | Deadline to Submit SAP Appeal | Fall | November 1 | Spring | April 1 | Summer | July 1 SAP Cycle Every student is reviewed for Satisfactory Academic Progres”
  - sentence: sap_appeal ⟵ “Students who do not regain financial aid eligibility through a SAP appeal will be reviewed at the end of each full term.”
### `43a981534a5c4b86` Eastern Kentucky University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eku.edu/in/guides/professional-judgment-appeal/ (sha256 b419e3e07aa3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “In these situations, students can initiate a Dependency Override appeal.”
### `d91fddf7fe4e042c` Eastern Kentucky University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eku.edu/in/guides/professional-judgment-appeal/ (sha256 b419e3e07aa3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances The EKU Financial Aid Office is aware that students may have unusual circumstances that prevent them from having a relationship with their parent(s)/guardians/contributors and therefore makes it difficult to obtain parental information for the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “A dependency override appeal is appropriate when a student has an unusual circumstance that is not already listed on the dependency portion of the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Dependency Override Special Circumstances Students and their families may also have special circumstances where their financial, marital, or dependency situations may not be accurately represented by the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Be advised that costs associated with discretionary lifestyle choices/consumer indebtedness (house payments, car expenses, living without roommates, credit card debt, mandatory bankruptcy payments, vacations, wedding expenses, tithing, etc.) cannot be considered a special circumstance.”
### `f0d95c16435e8fef` Eastern Kentucky University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.eku.edu/in/bigecentral/ (sha256 01234293b47f)
- issues: semantic_review_required, conflicting_sources:https://www.eku.edu/in/guides/professional-judgment-appeal/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Unsubsidized Loan for Dependent Students This form is for dependent students whose parents refuse to provide their information for the student’s FAFSA, and the student is not eligible for a special circumstances professional judgement.”
### `0d88c94726d3bef5` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-professional-development-series [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: BUS 200 ⟵ “BUS 200 - Professional Development Two”
  - courses: BUS 300 ⟵ “BUS 300 - Professional Development Three”
  - courses: BUS 400 ⟵ “BUS 400 - Professional Development Four”
### `0dcd19116a3ffccb` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=banking-and-financial-services-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: FIN 315 ⟵ “FIN 315 - Financial Statement and Loan Analysis”
  - courses: FIN 437 ⟵ “FIN 437 - Bank Management”
  - courses: ECO 324 ⟵ “ECO 324 - Money and Banking”
  - courses: RMI 370 ⟵ “RMI 370 - Principles of Risk and Insurance”
### `1029f979a2932722` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=financial-planning-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ACC 322 ⟵ “ACC 322 - Tax I”
  - courses: FIN 311 ⟵ “FIN 311 - Personal Financial Planning”
  - courses: RMI 370 ⟵ “RMI 370 - Principles of Risk and Insurance”
  - courses: RMI 374 ⟵ “RMI 374 - Fundamentals of Life and Health Insurance”
  - courses: RMI 474 ⟵ “RMI 474 - Life Insurance and Estate Planning”
### `10d2071d71eef98a` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-essential-series-functions-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: BUS 301 ⟵ “BUS 301 - Essentials of Formal Communication”
  - courses: BUS 302 ⟵ “BUS 302 - Essentials of Finance”
  - courses: BUS 303 ⟵ “BUS 303 - Essentials of Org Behav/HR Mgt”
  - courses: BUS 304 ⟵ “BUS 304 - Essentials of MIS”
  - courses: BUS 305 ⟵ “BUS 305 - Essentials of Marketing”
  - courses: BUS 306 ⟵ “BUS 306 - Essentials of Supply Chain Management”
### `1197cd0fa1aeb66d` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-mastery-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: BUS 402 ⟵ “BUS 402 - Integrated Strategic Mgmnt”
### `1affe1f71a3104f1` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-environment-of-business-2 [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: ECO 230 ⟵ “ECO 230 - Fundamentals of Microeconomics (Element 4B) E”
  - courses: ECO 231 ⟵ “ECO 231 - Fundamentals of Macroeconomics (Element 4B) E”
  - courses: MAT 114 ⟵ “MAT 114 - College Algebra (Element 2A) E”
  - courses: MAT 211 ⟵ “MAT 211 - Applied Calculus (Element 2A) E”
  - courses: STA 260 ⟵ “STA 260 - Business Statistics”
### `1cf3a68e1ec3f45e` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=management-accounting-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: ACC 527 ⟵ “ACC 527 - Advanced Management Accounting Seminar”
  - courses: ACC 555 ⟵ “ACC 555 - Accounting Analytics”
  - courses: FIN 301 ⟵ “FIN 301 - Corporate Finance”
  - courses: FIN 410 ⟵ “FIN 410 - Financial Analysis and Valuation”
  - courses: ACC 349 ⟵ “ACC 349 - Applied Learning in Accounting”
  - courses: ACC 521 ⟵ “ACC 521 - Government and Not-For-Profit Accounting”
  - courses: ACC 523 ⟵ “ACC 523 - Taxation of Corporations”
  - courses: ECO 324 ⟵ “ECO 324 - Money and Banking”
  - courses: MGT 442 ⟵ “MGT 442 - Supply Chain Planning”
### `21e19512911f298a` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-nature-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: BUS 101 ⟵ “BUS 101 - Nature of Business”
### `2386cc2a7faac62b` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=international-business-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: MGT 454 ⟵ “MGT 454 - International Business Communication”
  - courses: FIN 330 ⟵ “FIN 330 - Principles of International Finance”
  - courses: MGT 430 ⟵ “MGT 430 - International Management”
### `27c6e669af5a1f8a` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-mastery-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: BUS 402 ⟵ “BUS 402 - Integrated Strategic Mgmnt”
### `2c73874650fb28bb` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-nature-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: BUS 101 ⟵ “BUS 101 - Nature of Business”
### `2d5adf45a51afde0` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-major-core [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: FIN 201 ⟵ “FIN 201 - Personal Money Management”
  - courses: FIN 301 ⟵ “FIN 301 - Corporate Finance”
  - courses: FIN 304 ⟵ “FIN 304 - Financial Institutions”
  - courses: FIN 324 ⟵ “FIN 324 - Principles of Investments”
  - courses: FIN 420 ⟵ “FIN 420 - Investment and Portfolio Theory”
### `314f0b24b795aab5` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-professional-development-series [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: BUS 200 ⟵ “BUS 200 - Professional Development Two”
  - courses: BUS 300 ⟵ “BUS 300 - Professional Development Three”
  - courses: BUS 400 ⟵ “BUS 400 - Professional Development Four”
### `35fa1918a68c63ec` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=global-supply-chain-management-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: MGT 441 ⟵ “MGT 441 - Project Design & Management”
  - courses: MGT 442 ⟵ “MGT 442 - Supply Chain Planning”
  - courses: MGT 444 ⟵ “MGT 444 - Strategic Sourcing”
  - courses: MGT 446 ⟵ “MGT 446 - Logistics Management”
  - courses: MGT 448 ⟵ “MGT 448 - Supply Chain Ecosystems”
### `4875445afbb7aa11` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-mastery-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: BUS 402 ⟵ “BUS 402 - Integrated Strategic Mgmnt”
### `495cacf00640e46f` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-tools-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: BUS 206 ⟵ “BUS 206 - Fundamentals of Problem Solving with Excel”
  - courses: BUS 207 ⟵ “BUS 207 - Fundamentals of Interpersonal Business Commmunication”
  - courses: BUS 209 ⟵ “BUS 209 - Fundamentals of Financial and Managerial Accounting”
### `5315fb8dd5bc866f` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-professional-development-series [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: BUS 200 ⟵ “BUS 200 - Professional Development Two”
  - courses: BUS 300 ⟵ “BUS 300 - Professional Development Three”
  - courses: BUS 400 ⟵ “BUS 400 - Professional Development Four”
### `551fd6a0933d6f57` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-foundations-of-learning [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: GSD 101 ⟵ “GSD 101 - Foundations of Learning”
### `59033f921bd03e6b` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-environment-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: BUS 204 ⟵ “BUS 204 - Fundamentals of Business Law and Ethics”
### `6149e78f3022c900` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-free-electives [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - section: major-free-electives ⟵ “Major — Free Electives”
### `6a0e20cb40b3a05a` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=business-education-concentration-educational-professional-standards-board-epsb-r [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: EDF 203 ⟵ “EDF 203 - Educational Foundations”
  - courses: EDF 204 ⟵ “EDF 204 - Emerging Instructional Technologies”
  - courses: EDF 219 ⟵ “EDF 219 - Human Development and Learning”
  - courses: EDF 413 ⟵ “EDF 413 - Assessment in Education”
  - courses: EMS 300 ⟵ “EMS 300 - Curriculum and Instructional Design”
  - courses: EMS 474 ⟵ “EMS 474 - Disciplinary Literacy”
  - courses: EMS 490 ⟵ “EMS 490 - Classroom and Behavior Management”
  - courses: ESE 573 ⟵ “ESE 573 - Teaching Business and Marketing in Middle and Secondary Schools”
  - courses: SED 104 ⟵ “SED 104 - Special Education Introduction”
  - courses: EDC 300 ⟵ “EDC 300 - Differentiation in Inclusive Classrooms”
  - courses: CED 400 ⟵ “CED 400 - Clinical IV: Diagnosis and Prescription”
  - courses: CED 450 ⟵ “CED 450 - Clinical V: Practicing Teaching”
  - courses: CED 499 ⟵ “CED 499 - Clinical VI: The Professional Semester”
### `77fd315a2f16a1b7` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-major-core [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: MGT 312 ⟵ “MGT 312 - Organization Theory”
  - courses: MGT 316 ⟵ “MGT 316 - Organizational Behavior”
  - courses: MGT 318 ⟵ “MGT 318 - Management Issues in International Business”
  - courses: MGT 320 ⟵ “MGT 320 - Human Resource Management”
### `7de47e8cc97219c1` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-free-electives [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - section: major-free-electives ⟵ “Major — Free Electives”
### `82ca6cfd83f2442b` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-environment-of-business-2 [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: ECO 230 ⟵ “ECO 230 - Fundamentals of Microeconomics (Element 4B) E”
  - courses: ECO 231 ⟵ “ECO 231 - Fundamentals of Macroeconomics (Element 4B) E”
  - courses: MAT 114 ⟵ “MAT 114 - College Algebra (Element 2A) E”
  - courses: MAT 211 ⟵ “MAT 211 - Applied Calculus (Element 2A) E”
  - courses: STA 260 ⟵ “STA 260 - Business Statistics”
### `87d35ad87490496f` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=integrated-management-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MGT 330 ⟵ “MGT 330 - Small Business Management Innovation and Entrepreneurship”
  - courses: MGT 445 ⟵ “MGT 445 - Employee Recruitment and Selection”
  - courses: MGT 415 ⟵ “MGT 415 - Organizational Conflict Navigation”
  - courses: MGT 442 ⟵ “MGT 442 - Supply Chain Planning”
### `8b7d6e9f24bccc8c` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=general-business-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: FIN 304 ⟵ “FIN 304 - Financial Institutions”
  - courses: FIN 310 ⟵ “FIN 310 - Entrepreneurial Finance”
  - courses: FIN 311 ⟵ “FIN 311 - Personal Financial Planning”
  - courses: FIN 324 ⟵ “FIN 324 - Principles of Investments”
  - courses: FIN 330 ⟵ “FIN 330 - Principles of International Finance”
  - courses: MGT 316 ⟵ “MGT 316 - Organizational Behavior”
  - courses: MGT 320 ⟵ “MGT 320 - Human Resource Management”
  - courses: MGT 330 ⟵ “MGT 330 - Small Business Management Innovation and Entrepreneurship”
  - courses: MGT 442 ⟵ “MGT 442 - Supply Chain Planning”
### `8f33d99889de087d` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-environment-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: BUS 204 ⟵ “BUS 204 - Fundamentals of Business Law and Ethics”
### `902f3b970434754d` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=public-accounting-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: ACC 441 ⟵ “ACC 441 - Auditing I”
  - courses: ACC 349 ⟵ “ACC 349 - Applied Learning in Accounting (maximum of three hours toward concentration requirements)”
  - courses: ACC 425 ⟵ “ACC 425 - Accounting Theory”
  - courses: ACC 440 ⟵ “ACC 440 - Legal Aspects of Accounting”
  - courses: ACC 490 ⟵ “ACC 490 - Independent Study”
  - courses: ACC 501 ⟵ “ACC 501 - International Accounting and Combinations”
  - courses: ACC 521 ⟵ “ACC 521 - Government and Not-For-Profit Accounting”
  - courses: ACC 523 ⟵ “ACC 523 - Taxation of Corporations”
  - courses: ACC 525 ⟵ “ACC 525 - Forensic Accounting”
  - courses: ACC 527 ⟵ “ACC 527 - Advanced Management Accounting Seminar”
  - courses: ACC 555 ⟵ “ACC 555 - Accounting Analytics”
  - courses: ACC 590 ⟵ “ACC 590 - Special Topics in Accounting:__”
### `9e38fc7eb0becaac` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-environment-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: BUS 204 ⟵ “BUS 204 - Fundamentals of Business Law and Ethics”
### `a016b9ca3dfef8f8` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-tools-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: BUS 206 ⟵ “BUS 206 - Fundamentals of Problem Solving with Excel”
  - courses: BUS 207 ⟵ “BUS 207 - Fundamentals of Interpersonal Business Commmunication”
  - courses: BUS 209 ⟵ “BUS 209 - Fundamentals of Financial and Managerial Accounting”
### `a3be93d2710bfdaa` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-essential-series-functions-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: BUS 301 ⟵ “BUS 301 - Essentials of Formal Communication”
  - courses: BUS 302 ⟵ “BUS 302 - Essentials of Finance”
  - courses: BUS 303 ⟵ “BUS 303 - Essentials of Org Behav/HR Mgt”
  - courses: BUS 304 ⟵ “BUS 304 - Essentials of MIS”
  - courses: BUS 305 ⟵ “BUS 305 - Essentials of Marketing”
  - courses: BUS 306 ⟵ “BUS 306 - Essentials of Supply Chain Management”
### `a626171c40ad4ccd` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-professional-development-series [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: BUS 200 ⟵ “BUS 200 - Professional Development Two”
  - courses: BUS 300 ⟵ “BUS 300 - Professional Development Three”
  - courses: BUS 400 ⟵ “BUS 400 - Professional Development Four”
### `b486158a481bedbd` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-major-core [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: GBU 201 ⟵ “GBU 201 - International Business”
  - courses: MKT 400 ⟵ “MKT 400 - International Marketing”
### `b8ea99e082ae09ac` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=business-finance-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: RMI 370 ⟵ “RMI 370 - Principles of Risk and Insurance”
### `b9c3dec77a398776` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-environment-of-business-2 [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: ECO 230 ⟵ “ECO 230 - Fundamentals of Microeconomics (Element 4B) E”
  - courses: ECO 231 ⟵ “ECO 231 - Fundamentals of Macroeconomics (Element 4B) E”
  - courses: MAT 114 ⟵ “MAT 114 - College Algebra (Element 2A) E”
  - courses: MAT 211 ⟵ “MAT 211 - Applied Calculus (Element 2A) E”
  - courses: STA 260 ⟵ “STA 260 - Business Statistics”
### `bfc064bdb0fab7cc` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-student-success-seminar [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: GSD 101 ⟵ “GSD 101 - Foundations of Learning”
### `c4048495fee4827e` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=strategic-corporate-communication-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: MGT 452 ⟵ “MGT 452 - Online Managerial Communication”
  - courses: MGT 454 ⟵ “MGT 454 - International Business Communication”
  - courses: MGT 456 ⟵ “MGT 456 - Emerging Technologies in Business”
  - courses: MGT 458 ⟵ “MGT 458 - Integrated Corporate Communication”
### `ccd2b9925a3cffda` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-nature-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: BUS 101 ⟵ “BUS 101 - Nature of Business”
### `d0552335e42841bb` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-foundations-of-learning [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: GSD 101 ⟵ “GSD 101 - Foundations of Learning”
### `d36b46ddf4eba821` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=leadership-and-organizational-behavior-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: MGT 415 ⟵ “MGT 415 - Organizational Conflict Navigation”
  - courses: MGT 432 ⟵ “MGT 432 - Leadership and Ethics”
  - courses: MGT 434 ⟵ “MGT 434 - Team Effectiveness and Creative Problem Solving”
  - courses: MGT 438 ⟵ “MGT 438 - Organizational Culture and Change Initiatives”
### `d55561083a6cf0cb` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-major-core [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ACC 251 ⟵ “ACC 251 - Introduction to Accounting Information Systems”
  - courses: ACC 301 ⟵ “ACC 301 - Intermediate Accounting I”
  - courses: ACC 302 ⟵ “ACC 302 - Intermediate Accounting II”
  - courses: ACC 322 ⟵ “ACC 322 - Tax I”
  - courses: ACC 327 ⟵ “ACC 327 - Cost Accounting”
  - courses: ACC 350 ⟵ “ACC 350 - Accounting Information System Risk and Security”
### `d59856ae9df16e4d` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-environment-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: BUS 204 ⟵ “BUS 204 - Fundamentals of Business Law and Ethics”
### `dde7a80c0e9d0428` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=business-education-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CMS 100 ⟵ “CMS 100 - Introduction to Human Communication (Element 1C) E”
  - courses: ACC 251 ⟵ “ACC 251 - Introduction to Accounting Information Systems”
  - courses: ACC 322 ⟵ “ACC 322 - Tax I”
  - courses: FIN 201 ⟵ “FIN 201 - Personal Money Management”
  - courses: FIN 310 ⟵ “FIN 310 - Entrepreneurial Finance”
  - courses: MGT 316 ⟵ “MGT 316 - Organizational Behavior”
  - courses: MGT 320 ⟵ “MGT 320 - Human Resource Management”
  - courses: MGT 454 ⟵ “MGT 454 - International Business Communication”
  - courses: MGT 458 ⟵ “MGT 458 - Integrated Corporate Communication”
  - courses: MKT 350 ⟵ “MKT 350 - Consumer Behavior in Marketing”
  - courses: MKT 555 ⟵ “MKT 555 - Marketing Research and Analysis”
  - courses: RMI 280 ⟵ “RMI 280 - Personal Insurance”
  - courses: RMI 370 ⟵ “RMI 370 - Principles of Risk and Insurance”
### `e120d5b10dfd3003` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=human-resource-management-concentration-concentration-courses [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: MGT 425 ⟵ “MGT 425 - Compensation Management”
  - courses: MGT 440 ⟵ “MGT 440 - Human Resource Development”
  - courses: MGT 445 ⟵ “MGT 445 - Employee Recruitment and Selection”
  - courses: MGT 460 ⟵ “MGT 460 - Performance Management”
### `e3a411e3daf356b2` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-nature-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: BUS 101 ⟵ “BUS 101 - Nature of Business”
### `e9725589db7bc519` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-tools-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: BUS 206 ⟵ “BUS 206 - Fundamentals of Problem Solving with Excel”
  - courses: BUS 207 ⟵ “BUS 207 - Fundamentals of Interpersonal Business Commmunication”
  - courses: BUS 209 ⟵ “BUS 209 - Fundamentals of Financial and Managerial Accounting”
### `ea866920d82883e2` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-essential-series-functions-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: BUS 301 ⟵ “BUS 301 - Essentials of Formal Communication”
  - courses: BUS 302 ⟵ “BUS 302 - Essentials of Finance”
  - courses: BUS 303 ⟵ “BUS 303 - Essentials of Org Behav/HR Mgt”
  - courses: BUS 304 ⟵ “BUS 304 - Essentials of MIS”
  - courses: BUS 305 ⟵ “BUS 305 - Essentials of Marketing”
  - courses: BUS 306 ⟵ “BUS 306 - Essentials of Supply Chain Management”
### `f20e37b143f57600` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-approved-business-electives [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - section: major-approved-business-electives ⟵ “Major — Approved Business Electives”
### `f5dae3d4bbdce011` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-foundations-of-learning [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: GSD 101 ⟵ “GSD 101 - Foundations of Learning”
### `f8c8e60c146510e1` Eastern Kentucky University — degree_requirements 2026-27 · program_key=general-business-bachelor-of-business-administration-b-b-a-eastern-kentucky-univ · requirement_key=major-tools-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/general-business-bba/ (sha256 199a1436a0d5)
- issues: requirement_groups_skipped
  - courses: BUS 206 ⟵ “BUS 206 - Fundamentals of Problem Solving with Excel”
  - courses: BUS 207 ⟵ “BUS 207 - Fundamentals of Interpersonal Business Commmunication”
  - courses: BUS 209 ⟵ “BUS 209 - Fundamentals of Financial and Managerial Accounting”
### `f9384d20f4c90f3f` Eastern Kentucky University — degree_requirements 2026-27 · program_key=management-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-mastery-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/management-bba/ (sha256 822042c08c80)
- issues: requirement_groups_skipped
  - courses: BUS 402 ⟵ “BUS 402 - Integrated Strategic Mgmnt”
### `fa92fc4b67c86528` Eastern Kentucky University — degree_requirements 2026-27 · program_key=finance-bachelor-of-business-administration-b-b-a-eastern-kentucky-university-ac · requirement_key=major-environment-of-business-2 [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/finance-bba/ (sha256 fa17f424d22b)
- issues: requirement_groups_skipped
  - courses: ECO 230 ⟵ “ECO 230 - Fundamentals of Microeconomics (Element 4B) E”
  - courses: ECO 231 ⟵ “ECO 231 - Fundamentals of Macroeconomics (Element 4B) E”
  - courses: MAT 114 ⟵ “MAT 114 - College Algebra (Element 2A) E”
  - courses: MAT 211 ⟵ “MAT 211 - Applied Calculus (Element 2A) E”
  - courses: STA 260 ⟵ “STA 260 - Business Statistics”
### `fea0541e11b8a69d` Eastern Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-business-administration-b-b-a-eastern-kentucky-university · requirement_key=major-essential-series-functions-of-business [new] (labeled_in_source)
- source: https://catalogs.eku.edu/undergraduate/business/business/accounting-bba/ (sha256 00f932eaf83c)
- issues: requirement_groups_skipped
  - courses: BUS 301 ⟵ “BUS 301 - Essentials of Formal Communication”
  - courses: BUS 302 ⟵ “BUS 302 - Essentials of Finance”
  - courses: BUS 303 ⟵ “BUS 303 - Essentials of Org Behav/HR Mgt”
  - courses: BUS 304 ⟵ “BUS 304 - Essentials of MIS”
  - courses: BUS 305 ⟵ “BUS 305 - Essentials of Marketing”
  - courses: BUS 306 ⟵ “BUS 306 - Essentials of Supply Chain Management”
### `299f2b83564ec1f2` Elizabethtown Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://elizabethtown.kctcs.edu/affording-college/professional-judgment-options.aspx (sha256 f6edc2d6f1b7)
- issues: semantic_review_required, conflicting_sources:https://elizabethtown.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Often there are special circumstances that have occurred that will reduce the income for the student or family; when this happens, the student may work with the college Financial Aid Office to evaluate and adjust the income reported on the FAFSA to more accurately reflect the current situation.”
  - sentence: need_based_special_circumstances ⟵ “Examples of special circumstances that may warrant a recalculation of the FAFSA are listed below, but not limited to; Reduction or loss in Household Income due to layoffs, furlough, or job displacement.”
  - sentence: need_based_special_circumstances ⟵ “Non-recurring income, such as early withdrawal from a retirement account or insurance payout, severance pay, or other one-time income reported on the FAFSA Divorce or Separation following completion of the FAFSA Death of a parent or spouse The following are not examples: vacation expenses utilities, credit card expenses mortgage payments car payments lawn care personal debt A student may complete ”
  - sentence: need_based_special_circumstances ⟵ “The special circumstance reported will determine the required documentation, but most will require the following: Special Circumstance/Recalculation form.”
  - sentence: need_based_special_circumstances ⟵ “The college financial aid office will review these special circumstances on a one on one basis and if an override is approved will update the FAFSA to change the dependency status to independent.”
### `3d46fa6cfaed5eac` Elizabethtown Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://elizabethtown.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 466e48622946)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Financial Aid Appeal Process Students who believe they have or had extenuating circumstances that prohibited them from making the Satisfactory Academic Progress Standards may appeal to a committee appointed by the home campus to review such requests.”
  - sentence: sap_appeal ⟵ “Where to submit documentation for an Appeal To appeal, students may complete a SAP Appeal Form available online in the Tasks tile in Student Self-Service and also provide any additional information/documents required by submitting through the SAP appeal on OnBase.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Committee may approve your appeal with certain academic progress conditions or limit future hours.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee may request additional information.”
  - sentence: sap_appeal ⟵ “NOTE: Students are responsible for all expenses such as tuition, fees, books, and supplies pending the decision of the SAP Appeals Committee and must contact the Business Affairs Office to make payment arrangements with the institution.”
  - sentence: sap_appeal ⟵ “Decisions made by the SAP Appeals Committee are final and are not subject to further appeal.”
### `d0028e5eca495493` Elizabethtown Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://elizabethtown.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 466e48622946)
- issues: semantic_review_required, conflicting_sources:https://elizabethtown.kctcs.edu/affording-college/professional-judgment-options.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Step 1 - Personal Statement: submit a detailed appeal explaining the basis of your appeal request describing the following: The circumstance(s) that led to poor grades, multiple withdrawals, or incompletes (i.e., death of a relative, an injury or personal illness, or other special circumstances).”
### `e360ecd9dbc34947` Elizabethtown Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://elizabethtown.kctcs.edu/affording-college/professional-judgment-options.aspx (sha256 f6edc2d6f1b7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment or Recalculation refers to the school's authority to adjust, on a case-by-case basis, to information reported on the Free Application for Federal Student Aid (FAFSA) so that the Department of Education can recalculate the Expected Family Contribution (EFC).”
### `fef636e9ab18465f` Elizabethtown Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://elizabethtown.kctcs.edu/affording-college/professional-judgment-options.aspx (sha256 f6edc2d6f1b7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “In some situations, a dependency override can be used to make a dependent student independent for the purposes of awarding financial aid.”
### `29b4675c5d5d55fa` Gateway Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gateway.kctcs.edu/affording-college/satisfactory-academic-progress/sap-appeal-instructions.aspx (sha256 6017f4a0333b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of unusual circumstances include: Illness Accident Death in your family Submit completed Appeal Request through your Student Self-Service.”
### `8bb1623da9a2c08a` Gateway Community and Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://gateway.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 5eb0e97fe721)
- issues: semantic_review_required, conflicting_sources:https://gateway.kctcs.edu/affording-college/satisfactory-academic-progress/sap-appeal-instructions.aspx
- checks: {"negative_sentences": 0, "sentences": 15}
  - sentence: sap_appeal ⟵ “SAP Appeal Process A student who has lost financial aid eligibility because of not meeting SAP standards does have the right to submit a SAP Appeal Request.”
  - sentence: sap_appeal ⟵ “A link to the online SAP Appeal Request is added to a student’s self-service center soon after the end of the academic term in which they have become SAP suspended.”
  - sentence: sap_appeal ⟵ “Students will be expected to explain why they have failed to meet the required SAP standards in their appeal.”
  - sentence: sap_appeal ⟵ “Decisions made by the SAP Appeals Committee are final.”
  - sentence: sap_appeal ⟵ “Students are responsible for any charges incurred regardless of the outcome of their SAP Appeal.”
  - sentence: sap_appeal ⟵ “They may submit another SAP Appeal, but it can’t be based on the same circumstances cited in a previously approved Appeal.”
### `b68fc803cfea09cf` Gateway Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://gateway.kctcs.edu/affording-college/satisfactory-academic-progress/sap-appeal-instructions.aspx (sha256 6017f4a0333b)
- issues: semantic_review_required, conflicting_sources:https://gateway.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “You may file a SAP Appeal Request to be considered for financial aid reinstatement explaining the unusual circumstances that were a factor in not meeting Satisfactory Academic Progress.”
  - sentence: sap_appeal ⟵ “Complete the SAP Appeal Request, which is located on your Student Self-Service under Financial Aid.”
  - sentence: sap_appeal ⟵ “You should turn in documentation of any unusual circumstances by uploading it to your SAP Appeal Request form.”
### `bbb2c3e0919a4f80` Georgetown College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.georgetowncollege.edu/admissions/cost-aid/financial-aid-tuition/ (sha256 45a8bb889667)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Except in unusual circumstances, we can help a family complete the FAFSA in 30 minutes.”
### `81980c4a76bcfe75` Georgetown College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.georgetowncollege.edu/admissions/cost-aid/financial-aid-tuition/ (sha256 45a8bb889667)
- issues: components_do_not_reconcile
- checks: {"columns": 3, "components_reconcile": false, "rows": 11}
  - on_campus:Tuition: 42678 ⟵ “Tuition | $42,678 | $42,678 | $42,678”
  - on_campus:Fees: 1300 ⟵ “Fees | $1,300 | $1,300 | $1,300”
  - on_campus:Housing: 5546 ⟵ “Housing | $5,546 | $3,495 | $8,838”
  - on_campus:Food: 6722 ⟵ “Food | $6,722 | $1,030 | $2,060”
  - on_campus:Average Student Direct Loan Fees: 82 ⟵ “Average Student Direct Loan Fees | $82 | $82 | $82”
  - on_campus:Transportation: 2000 ⟵ “Transportation | $2,000 | $3,000 | $3,000”
  - on_campus:Books & Supplies: 2000 ⟵ “Books & Supplies | $2,000 | $2,000 | $2,000”
  - on_campus:Personal: 2700 ⟵ “Personal | $2,700 | $2,700 | $3,600”
  - on_campus:Total: 63028 ⟵ “Total | $63,028 | $56,203 | $63,558”
  - on_campus:Direct Cost: 56328 ⟵ “Direct Cost | $56,328 | $48,503 | $54,958”
  - on_campus:Indirect Cost Allowance: 6700 ⟵ “Indirect Cost Allowance | $6,700 | $7,700 | $8,600”
  - with_parents_or_family:Tuition: 42678 ⟵ “Tuition | $42,678 | $42,678 | $42,678”
  - with_parents_or_family:Fees: 1300 ⟵ “Fees | $1,300 | $1,300 | $1,300”
  - with_parents_or_family:Housing: 3495 ⟵ “Housing | $5,546 | $3,495 | $8,838”
  - with_parents_or_family:Food: 1030 ⟵ “Food | $6,722 | $1,030 | $2,060”
  - with_parents_or_family:Average Student Direct Loan Fees: 82 ⟵ “Average Student Direct Loan Fees | $82 | $82 | $82”
  - with_parents_or_family:Transportation: 3000 ⟵ “Transportation | $2,000 | $3,000 | $3,000”
  - with_parents_or_family:Books & Supplies: 2000 ⟵ “Books & Supplies | $2,000 | $2,000 | $2,000”
  - with_parents_or_family:Personal: 2700 ⟵ “Personal | $2,700 | $2,700 | $3,600”
  - with_parents_or_family:Total: 56203 ⟵ “Total | $63,028 | $56,203 | $63,558”
  - with_parents_or_family:Direct Cost: 48503 ⟵ “Direct Cost | $56,328 | $48,503 | $54,958”
  - with_parents_or_family:Indirect Cost Allowance: 7700 ⟵ “Indirect Cost Allowance | $6,700 | $7,700 | $8,600”
  - off_campus_not_with_family:Tuition: 42678 ⟵ “Tuition | $42,678 | $42,678 | $42,678”
  - off_campus_not_with_family:Fees: 1300 ⟵ “Fees | $1,300 | $1,300 | $1,300”
  - off_campus_not_with_family:Housing: 8838 ⟵ “Housing | $5,546 | $3,495 | $8,838”
  - … 8 more rows
### `6a2f118296a55b7d` Henderson Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://henderson.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 44bab4e8c556)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeals Failure to meet SAP requirements for two consecutive terms will result in the suspension of financial aid.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will review each appeal and has discretion to determine if each circumstance meets the requirements for approval.”
  - sentence: sap_appeal ⟵ “To appeal, complete the steps below: Complete the Online SAP Appeal in PeopleSoft by clicking on the Online SAP Appeal link in the Financial Aid section.”
  - sentence: sap_appeal ⟵ “The Online SAP Appeal, Academic Plan of Action, and supporting documentation are all required.”
  - sentence: sap_appeal ⟵ “You will receive notification of the committee decision in your PeopleSoft under Finances/SAP Appeal Confirmation and via your KCTCS email account within 10 business days.”
### `69c33fb49f563b9a` Hopkinsville Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://hopkinsville.kctcs.edu/affording-college/professional-judgment.aspx (sha256 1ff196646e71)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Unusual Circumstances refer to the conditions that justify an aid administrator to make an adjustment to a student’s dependency status based on a unique situation, this is more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances include but not limited to: Loss or change of employment Reduction in income or assets Loss or change in amount of child support, Social Security, or other benefits Divorce or separation of parents Death of parent(s) Unusual medical expenses (not covered by insurance) One-time taxable income used for life-changing events (e.g.”
### `bf90b26005648c35` Hopkinsville Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://hopkinsville.kctcs.edu/affording-college/professional-judgment.aspx (sha256 1ff196646e71)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment is comprised of two components, unusual circumstances and special circumstances.”
### `03d48ab1d9422f46` Jefferson Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jefferson.kctcs.edu/affording-college/financial-aid-information/recalculation-request.aspx (sha256 3ce2388e7c98)
- issues: semantic_review_required, conflicting_sources:https://jefferson.kctcs.edu/affording-college/financial-aid-information/awards/special-unusual-circumstances.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A member of the Financial Aid Office will contact you within 10 business days to submit an in-depth special circumstances request form as well as additional documentation once this form has been received.”
### `1dd18bf68eb239ff` Jefferson Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jefferson.kctcs.edu/affording-college/financial-aid-information/awards/special-unusual-circumstances.aspx (sha256 9d6d4b089e6d)
- issues: semantic_review_required, conflicting_sources:https://jefferson.kctcs.edu/affording-college/financial-aid-information/recalculation-request.aspx
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Unusual Circumstances refer to the conditions that justify an aid administrator to make an adjustment to a student’s dependency status based on a unique situation, this is more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Special or extenuating situations (such as the loss of a job) that impact a student’s financial condition and support a financial aid administrator adjusting data elements in the COA or in the SAI calculation on a case-by-case basis.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances include but are not limited to: Loss or change of employment Reduction in income or assets Loss or change in amount of child support, Social Security, or other benefits Divorce or separation of parents Death of parent(s) Unusual medical expenses (not covered by insurance) One-time taxable income used for life-changing events (e.g.”
### `21a48fb81675ec42` Jefferson Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jefferson.kctcs.edu/affording-college/financial-aid-information/awards/special-unusual-circumstances.aspx (sha256 9d6d4b089e6d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment is comprised of two components, unusual circumstances and special circumstances.”
### `d783d1f752b09211` Jefferson Community and Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://jefferson.kctcs.edu/affording-college/financial-aid-information/index.aspx (sha256 e2f400117ca3)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://jefferson.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Information on the SAP Appeal Process is available here.”
### `f20c43306ff06b2e` Jefferson Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jefferson.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 8d01cb308284)
- issues: semantic_review_required, conflicting_sources:https://jefferson.kctcs.edu/affording-college/financial-aid-information/index.aspx
- checks: {"negative_sentences": 0, "sentences": 20}
  - sentence: sap_appeal ⟵ “SAP APPEAL REQUEST PROCESS To appeal, students must complete an electronic SAP Appeal Request Form and provide any additional information/documents required by the college.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Request Form is available in your Tasks Tile located in your , but you cannot save the appeal and complete later.”
  - sentence: sap_appeal ⟵ “How to Submit an Online SAP Appeal from your Student Self-Service: Before you begin, note that all SAP Appeals require supporting documentation, and the appeal cannot be submitted without attaching documentation on the last page.”
  - sentence: sap_appeal ⟵ “Select the Link provided The OnBase Satisfactory Academic Progress (SAP) Appeal form will display.”
  - sentence: sap_appeal ⟵ “Page 3 contains important information regarding the SAP appeal process.”
  - sentence: sap_appeal ⟵ “More information and pictures of the SAP appeal process are available on the KCTCS SAP webpage.”
### `49c3d2bd6846aabb` Jefferson Community and Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://jefferson.kctcs.edu/affording-college/financial-aid-information/awards/kees.aspx (sha256 27f33f86a413)
- issues: conflicting_values:residency_requirement_credits
- checks: {"fields": []}
### `a2a3bdf65e6f2f0d` Kentucky Christian University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kcu.edu/apply-afford/cost-aid/keeping-your-scholarship/ (sha256 7fa38896eff9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “A student who is placed on financial aid suspension for not meeting the 67% Pace measure of satisfactory progress or for failing a financial aid probationary term may submit a written appeal to the Financial Aid Director that is based on the student’s injury or illness, the death of a relative, or other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “A student who is placed on financial aid suspension for not meeting the 67% Pace measure of satisfactory progress may submit a written appeal to the Financial Aid Director that is based on the student’s injury or illness, the death of a relative, or other special circumstances.”
### `85dbe17da56449d9` Kentucky Christian University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.kcu.edu/apply-afford/cost-aid/cost-of-attendance/undergraduate-programs-tuition-and-fees/ (sha256 b6b492e3c8ff)
- issues: arrangement_unlabeled, components_do_not_reconcile, stale_year_label:2025-26
- checks: {"columns": 8, "components_reconcile": false, "rows": 4}
  - column:Tuition (Undergraduate, Full-Time Block Tuition): 27530 ⟵ “Tuition (Undergraduate, Full-Time Block Tuition) | $27,530 |  | $27,530 |  | $27,530 |  | $27,530 | ”
  - column:Fees (required of every student): 600 ⟵ “Fees (required of every student) | $600 |  | $600 |  | $600 |  | $600 | ”
  - column:Housing & Food (Meal Plan) On Campus: 11140 ⟵ “Housing & Food (Meal Plan) On Campus | $11,140 |  |  |  |  |  |  | ”
  - column:TOTAL “Cost of Attendance”: 45996 ⟵ “TOTAL “Cost of Attendance” | $45,996 | $38,726 | $59,648 | $59,648”
  - column:Books, Course Materials, Supplies & Equipment (estimated): 2200 ⟵ “Books, Course Materials, Supplies & Equipment (estimated) |  | $2,200 |  | $2,200 |  | $2,200 |  | $2,200”
  - column:Transportation: 1960 ⟵ “Transportation |  | $1,960 |  | $3,220 |  | $3,220 |  | $3,220”
  - column:Misc. Personal Expenses: 2518 ⟵ “Misc. Personal Expenses |  | $2,518 |  | $1,914 |  | $10,830 |  | $10,830”
  - column:**Federal Student Loan Fees (est. average): 48 ⟵ “**Federal Student Loan Fees (est. average) |  | $48 |  | $48 |  | $48 |  | $50”
  - column:TOTAL “Cost of Attendance”: 38726 ⟵ “TOTAL “Cost of Attendance” | $45,996 | $38,726 | $59,648 | $59,648”
  - column:Tuition (Undergraduate, Full-Time Block Tuition): 27530 ⟵ “Tuition (Undergraduate, Full-Time Block Tuition) | $27,530 |  | $27,530 |  | $27,530 |  | $27,530 | ”
  - column:Fees (required of every student): 600 ⟵ “Fees (required of every student) | $600 |  | $600 |  | $600 |  | $600 | ”
  - column:TOTAL “Cost of Attendance”: 59648 ⟵ “TOTAL “Cost of Attendance” | $45,996 | $38,726 | $59,648 | $59,648”
  - column:Books, Course Materials, Supplies & Equipment (estimated): 2200 ⟵ “Books, Course Materials, Supplies & Equipment (estimated) |  | $2,200 |  | $2,200 |  | $2,200 |  | $2,200”
  - column:Housing & Food at Home with Parent: 3214 ⟵ “Housing & Food at Home with Parent |  |  |  | $3,214 |  |  |  | ”
  - column:Transportation: 3220 ⟵ “Transportation |  | $1,960 |  | $3,220 |  | $3,220 |  | $3,220”
  - column:Misc. Personal Expenses: 1914 ⟵ “Misc. Personal Expenses |  | $2,518 |  | $1,914 |  | $10,830 |  | $10,830”
  - column:**Federal Student Loan Fees (est. average): 48 ⟵ “**Federal Student Loan Fees (est. average) |  | $48 |  | $48 |  | $48 |  | $50”
  - column:TOTAL “Cost of Attendance”: 59648 ⟵ “TOTAL “Cost of Attendance” | $45,996 | $38,726 | $59,648 | $59,648”
  - column:Tuition (Undergraduate, Full-Time Block Tuition): 27530 ⟵ “Tuition (Undergraduate, Full-Time Block Tuition) | $27,530 |  | $27,530 |  | $27,530 |  | $27,530 | ”
  - column:Fees (required of every student): 600 ⟵ “Fees (required of every student) | $600 |  | $600 |  | $600 |  | $600 | ”
  - column:Books, Course Materials, Supplies & Equipment (estimated): 2200 ⟵ “Books, Course Materials, Supplies & Equipment (estimated) |  | $2,200 |  | $2,200 |  | $2,200 |  | $2,200”
  - column:Housing & Food Off Campus: 15220 ⟵ “Housing & Food Off Campus |  |  |  |  |  | $15,220 |  | $15,220”
  - column:Transportation: 3220 ⟵ “Transportation |  | $1,960 |  | $3,220 |  | $3,220 |  | $3,220”
  - column:Misc. Personal Expenses: 10830 ⟵ “Misc. Personal Expenses |  | $2,518 |  | $1,914 |  | $10,830 |  | $10,830”
  - column:**Federal Student Loan Fees (est. average): 48 ⟵ “**Federal Student Loan Fees (est. average) |  | $48 |  | $48 |  | $48 |  | $50”
  - … 7 more rows
### `af6269658afce2b7` Kentucky Christian University — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.kcu.edu/apply-afford/cost-aid/cost-of-attendance/undergraduate-programs-tuition-and-fees/ (sha256 b6b492e3c8ff)
- issues: ambiguous_year_labels, arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 8, "components_reconcile": false, "rows": 4}
  - column:Tuition (Undergraduate, Full-Time Block Tuition): 26730 ⟵ “Tuition (Undergraduate, Full-Time Block Tuition) | $26,730 |  | $26,730 |  | $26,730 |  | $26,730 | ”
  - column:Fees (required of every student): 600 ⟵ “Fees (required of every student) | $600 |  | $600 |  | $600 |  | $600 | ”
  - column:Housing & Food (Meal Plan) On Campus: 10780 ⟵ “Housing & Food (Meal Plan) On Campus | $10,780 |  |  |  |  |  |  | ”
  - column:TOTAL “Cost of Attendance”: 44682 ⟵ “TOTAL “Cost of Attendance” | $44,682 | $37,576 | $56,720 | $56,720”
  - column:Books, Course Materials, Supplies & Equipment (estimated): 2200 ⟵ “Books, Course Materials, Supplies & Equipment (estimated) |  | $2,200 |  | $2,200 |  | $2,200 |  | $2,200”
  - column:Transportation: 1876 ⟵ “Transportation |  | $1,876 |  | $2,986 |  | $2,986 |  | $2,986”
  - column:Misc. Personal Expenses: 2446 ⟵ “Misc. Personal Expenses |  | $2,446 |  | $1,860 |  | $9,498 |  | $9,498”
  - column:**Federal Student Loan Fees (est. average): 50 ⟵ “**Federal Student Loan Fees (est. average) |  | $50 |  | $50 |  | $50 |  | $50”
  - column:TOTAL “Cost of Attendance”: 37576 ⟵ “TOTAL “Cost of Attendance” | $44,682 | $37,576 | $56,720 | $56,720”
  - column:Tuition (Undergraduate, Full-Time Block Tuition): 26730 ⟵ “Tuition (Undergraduate, Full-Time Block Tuition) | $26,730 |  | $26,730 |  | $26,730 |  | $26,730 | ”
  - column:Fees (required of every student): 600 ⟵ “Fees (required of every student) | $600 |  | $600 |  | $600 |  | $600 | ”
  - column:TOTAL “Cost of Attendance”: 56720 ⟵ “TOTAL “Cost of Attendance” | $44,682 | $37,576 | $56,720 | $56,720”
  - column:Books, Course Materials, Supplies & Equipment (estimated): 2200 ⟵ “Books, Course Materials, Supplies & Equipment (estimated) |  | $2,200 |  | $2,200 |  | $2,200 |  | $2,200”
  - column:Housing & Food at Home with Parent: 3150 ⟵ “Housing & Food at Home with Parent |  |  |  | $3,150 |  |  |  | ”
  - column:Transportation: 2986 ⟵ “Transportation |  | $1,876 |  | $2,986 |  | $2,986 |  | $2,986”
  - column:Misc. Personal Expenses: 1860 ⟵ “Misc. Personal Expenses |  | $2,446 |  | $1,860 |  | $9,498 |  | $9,498”
  - column:**Federal Student Loan Fees (est. average): 50 ⟵ “**Federal Student Loan Fees (est. average) |  | $50 |  | $50 |  | $50 |  | $50”
  - column:TOTAL “Cost of Attendance”: 56720 ⟵ “TOTAL “Cost of Attendance” | $44,682 | $37,576 | $56,720 | $56,720”
  - column:Tuition (Undergraduate, Full-Time Block Tuition): 26730 ⟵ “Tuition (Undergraduate, Full-Time Block Tuition) | $26,730 |  | $26,730 |  | $26,730 |  | $26,730 | ”
  - column:Fees (required of every student): 600 ⟵ “Fees (required of every student) | $600 |  | $600 |  | $600 |  | $600 | ”
  - column:Books, Course Materials, Supplies & Equipment (estimated): 2200 ⟵ “Books, Course Materials, Supplies & Equipment (estimated) |  | $2,200 |  | $2,200 |  | $2,200 |  | $2,200”
  - column:Housing & Food Off Campus: 14656 ⟵ “Housing & Food Off Campus |  |  |  |  |  | $14,656 |  | $14,656”
  - column:Transportation: 2986 ⟵ “Transportation |  | $1,876 |  | $2,986 |  | $2,986 |  | $2,986”
  - column:Misc. Personal Expenses: 9498 ⟵ “Misc. Personal Expenses |  | $2,446 |  | $1,860 |  | $9,498 |  | $9,498”
  - column:**Federal Student Loan Fees (est. average): 50 ⟵ “**Federal Student Loan Fees (est. average) |  | $50 |  | $50 |  | $50 |  | $50”
  - … 7 more rows
### `de2ee0959e29286b` Kentucky Christian University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.kcu.edu/wp-content/uploads/2025/11/2026-27-Elements-of-Annual-COA-Undergraduate.pdf (sha256 7e4d02b38fd6)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 4, "components_reconcile": false, "rows": 21}
  - column:Tuition (Undergraduate, Full-Time Block Tuition): 27530 ⟵ “Tuition (Undergraduate, Full-Time Block Tuition) | 27,530 | 27,530 | 27,530 | 27,530”
  - column:Mandatory Fees (required of every student): 600 ⟵ “Mandatory Fees (required of every student) | 600 | 600 | 600 | 600”
  - column:Books, Course Materials, Supplies & Equipment (est.)+++: 2200 ⟵ “Books, Course Materials, Supplies & Equipment (est.)+++ | 2,200 | 2,200 | 2,200 | 2,200”
  - column:Housing & Food (Meal Plan) On Campus: 11140 ⟵ “Housing & Food (Meal Plan) On Campus | 11,140”
  - column:Housing & Food at Home with Parent: 3214 ⟵ “Housing & Food at Home with Parent | 3,214”
  - column:Housing & Food Off Campus: 15220 ⟵ “Housing & Food Off Campus | 15,220 | 15,220”
  - column:Transportation: 1960 ⟵ “Transportation | 1,960 | 3,220 | 3,220 | 3,220”
  - column:Misc. Personal Expenses: 2518 ⟵ “Misc. Personal Expenses | 2,518 | 1,914 | 10,830 | 10,830”
  - column:** Federal Student Loan Fees (est. average): 48 ⟵ “** Federal Student Loan Fees (est. average) | 48 | 48 | 48 | 48”
  - column:TOTAL "Cost of Attendance": 45996 ⟵ “TOTAL "Cost of Attendance" | 45,996 | 38,726 | 59,648 | 59,648”
  - column:$150 Lesson Fee plus $85 Practice Room Fee: 235 ⟵ “$150 Lesson Fee plus $85 Practice Room Fee | $235”
  - column:Special Music Fee: 50 ⟵ “Special Music Fee | $50”
  - column:First-Time Student Fee (new undergraduate students): 175 ⟵ “First-Time Student Fee (new undergraduate students) | $175”
  - column:First-Time Online Student Service Fee (new online students): 150 ⟵ “First-Time Online Student Service Fee (new online students) | $150”
  - column:College 101 / Intro to KCU Course Fee (new undergraduate students): 150 ⟵ “College 101 / Intro to KCU Course Fee (new undergraduate students) | $150”
  - column:International Student Fee (per semester): 30 ⟵ “International Student Fee (per semester) | $30”
  - column:Student Teaching Fee: 595 ⟵ “Student Teaching Fee | $595”
  - column:Nursing Assessment/Program Fee (per semester): 730 ⟵ “Nursing Assessment/Program Fee (per semester) | $730”
  - column:Graduate Portfolio Fee (MAR – charged as course fee for FND 600): 300 ⟵ “Graduate Portfolio Fee (MAR – charged as course fee for FND 600) | $300”
  - column:Graduate Thesis Fee (MABS, MACL – charged as course fee for FND 621 and BTH 621): 750 ⟵ “Graduate Thesis Fee (MABS, MACL – charged as course fee for FND 621 and BTH 621) | $750”
  - column:Graduate Thesis Extension Fee (MABS, MACL – charged as course fee for FND 622 and BTH: 350 ⟵ “Graduate Thesis Extension Fee (MABS, MACL – charged as course fee for FND 622 and BTH | $350”
  - column:Tuition (Undergraduate, Full-Time Block Tuition): 27530 ⟵ “Tuition (Undergraduate, Full-Time Block Tuition) | 27,530 | 27,530 | 27,530 | 27,530”
  - column:Mandatory Fees (required of every student): 600 ⟵ “Mandatory Fees (required of every student) | 600 | 600 | 600 | 600”
  - column:Books, Course Materials, Supplies & Equipment (est.)+++: 2200 ⟵ “Books, Course Materials, Supplies & Equipment (est.)+++ | 2,200 | 2,200 | 2,200 | 2,200”
  - column:Housing & Food Off Campus: 15220 ⟵ “Housing & Food Off Campus | 15,220 | 15,220”
  - … 18 more rows
### `261c57b81be0d0be` Kentucky Mountain Bible College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.kmbc.edu/dualenroll/ (sha256 2826d21e94d0)
- issues: conflicting_values:max_credit_hours_per_term
- checks: {"fields": [], "tiers": 0}
  - max_credit_hours_per_term: 6 ⟵ “Eligible Juniors may enroll up to 6 credits per semester for first time students, up to full-time for those re-enrolling or providing additional verification of preparedness.”
  - max_credit_hours_per_term: 3 ⟵ “Eligible Sophomores may take up to 3 credits per semester. Exceptions approved individually.”
### `94034821c5486bf0` Kentucky State University — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://www.kysu.edu/documents/institutional-research/CDS-2024-2025.pdf (sha256 f354b6f20ea4)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 0 ⟵ “Total first-time, first-year (degree-seeking) who applied                                                            0”
  - admits: 0 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                                                      0”
  - enrolled: 0 ⟵ “Total first-time, first-year (degree-seeking) enrolled                                                               0”
  - act_25..75: [12, 15, 17] ⟵ “ACT Composite                      12                        15                         17”
### `6baf58a4d658759e` Kentucky State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.kysu.edu/finance-and-administration/financial-aid/index.php (sha256 87e01fb85b38)
- issues: semantic_review_required, conflicting_sources:https://www.kysu.edu/finance-and-administration/financial-aid/SAP%20Appeal%20%202026-2027.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Advising on next step actions for application process, disbursement of aid, and other special circumstances via in-person, telephone, and email contacts.”
### `6cd78d3b07087d98` Kentucky State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kysu.edu/finance-and-administration/financial-aid/resources-policies-and-procedures/sap.php (sha256 bd65ee37663d)
- issues: semantic_review_required, conflicting_sources:https://www.kysu.edu/documents/financial-aid/2025-SAP-Policy.pdf,https://www.kysu.edu/finance-and-administration/financial-aid/SAP%20Appeal%20%202026-2027.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal Process All SAP Appeals and documentation are reviewed in the order that they are received.”
  - sentence: sap_appeal ⟵ “The following forms are required upon submitting the SAP papers for review: Letter to SAP appeals committee – Students must submit a typed letter to the appeals committee detailing any and all extraordinary circumstances which may have adversely affected academic performance.”
  - sentence: sap_appeal ⟵ “SAP Appeal Form Any supporting documents that explain relevant circumstances Important SAP Appeal Deadlines: Fall 2026 Semester: May 17, 2026 - August 7, 2026 Spring 2027 Semester: TBD per Academic Calendar Summer 2027 Semester: TBD per Academic Calendar About KSU Foster Innovation and Inspire Leaders to Advance the Commonwealth and the World. 400 East Main St.”
### `ac1cdfae9d84a831` Kentucky State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kysu.edu/finance-and-administration/financial-aid/SAP%20Appeal%20%202026-2027.pdf (sha256 dbb8105aa344)
- issues: semantic_review_required, conflicting_sources:https://www.kysu.edu/finance-and-administration/financial-aid/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Include date of onset and length of time ☐ Death of Immediate Family Member - Supporting documents must include obituary, death certificate, or letter from a professional lawyer, doctor, or minister, that states the date of the death and the individual’s relationship to the student. ☐ Other Unusual Circumstances - Supporting documents must include academic advisor, counselor, tutor, professor and/”
### `ba42f4f0f19359c3` Kentucky State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kysu.edu/documents/financial-aid/2025-SAP-Policy.pdf (sha256 a9af2818f05b)
- issues: semantic_review_required, conflicting_sources:https://www.kysu.edu/finance-and-administration/financial-aid/SAP%20Appeal%20%202026-2027.pdf,https://www.kysu.edu/finance-and-administration/financial-aid/resources-policies-and-procedures/sap.php
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “APPEAL OF FINANCIAL AID PROCESS: A student determined ineligible for financial aid for failure to meet Kentucky State University’s Satisfactory Academic Progress standards has the right to make a written appeal to the Student Financial Aid Office if he or she can demonstrate: • failure to meet the minimum standard was caused by extreme or unusual circumstances beyond his or her control, and; • he ”
  - sentence: sap_appeal ⟵ “Instructions for Submitting an Appeal Student • Student completes the SAP appeal application.”
  - sentence: sap_appeal ⟵ “SAP Deadline Dates Fall Semester 2024 May 17, 2024-August 14, 2024 Spring Semester 2025 November 1, 2024-January 8, 2025 Summer 2025 April 7, 2025-May 9, 2025 Financial Aid Office • Once an appeal is received, it will be reviewed by a FA Counselor to determine all documentation is being submitted. • Complete SAP Appeals are then loaded into the FAO Shared Drive>SAP>Term folder (Ex.”
### `d669c7ffe8e6702f` Kentucky State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kysu.edu/finance-and-administration/financial-aid/SAP%20Appeal%20%202026-2027.pdf (sha256 dbb8105aa344)
- issues: semantic_review_required, conflicting_sources:https://www.kysu.edu/documents/financial-aid/2025-SAP-Policy.pdf,https://www.kysu.edu/finance-and-administration/financial-aid/resources-policies-and-procedures/sap.php
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS (SAP) APPEAL FORM A student determined ineligible for financial aid for failure to meet Kentucky State University’s Satisfactory Academic Progress standards has the right to make a written appeal to the Student Financial Aid Office if the following can demonstrated: • failure to meet the minimum standard was caused by extreme or unusual circumstances beyond his or he”
  - sentence: sap_appeal ⟵ “SECTION I: STUDENT INFORMATION Name (Please print): (Last) (First) (MI) Student ID: Major: Appealing Term: KSU Student Email: Phone Number: Alternate Phone Number: Address: Appeals must include: • A Satisfactory Academic Progress Appeal form which is completed and signed.”
  - sentence: sap_appeal ⟵ “The SAP Appeal form can be found on our website at https://www.kysu.edu/finance-and-administration/financial-aid/sap.php.”
  - sentence: sap_appeal ⟵ “To review the SAP Appeal due dates please visit our website at: https://www.kysu.edu/finance-and-administration/financial-aid/sap.php Kentucky State University Office of Financial Aid 400 East Main Street Julian M.”
### `5388c419dca70511` Kentucky Wesleyan College — appeals 2024-25 [new] (labeled_in_source)
- source: https://kwc.edu/admissions/cost-and-aid/financial-aid-policies-and-information/ (sha256 e769f1774c7b)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals: Must be submitted in writing using the Satisfactory Academic Progress Appeal Form with all appropriate documentation.”
### `e951ed208aee7b32` Kentucky Wesleyan College — appeals 2024-25 [new] (labeled_in_source)
- source: https://kwc.edu/admissions/cost-and-aid/financial-aid-policies-and-information/ (sha256 68c9e6367578)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “No two students are alike so things like housing and food will vary from student to student depending on their individual needs and special circumstances.”
### `c042e70b2e78506f` Kentucky Wesleyan College — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://kwc.edu/admissions/cost-and-aid/financial-aid-policies-and-information/ (sha256 e769f1774c7b)
- issues: arrangement_unlabeled, stale_year_label:2024-25
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - column:Tuition: 33180.0 ⟵ “Tuition | 33,180.00 | 10,980.00 | 38,925.00”
  - column:Housing & Food: 11855.0 ⟵ “Housing & Food | 11,855.00 | 5,928.00 | 11,855.00”
  - column:Fees: 1493.0 ⟵ “Fees | 1,493.00 | 250.00 | 1,493.00”
  - column:Course Materials, Supplies, & Equipment: 1298.0 ⟵ “Course Materials, Supplies, & Equipment | 1,298.00 | 649.00 | 1,298.00”
  - column:Transportation: 2724.0 ⟵ “Transportation | 2,724.00 | 1,362.00 | 2,724.00”
  - column:Personal & Misc.: 3125.0 ⟵ “Personal & Misc. | 3,125.00 | 1,563.00 | 3,125.00”
  - column:Total: 53675.0 ⟵ “Total | 53,675.00 | 20,732.00 | 59,420.00”
  - column:Tuition: 10980.0 ⟵ “Tuition | 33,180.00 | 10,980.00 | 38,925.00”
  - column:Housing & Food: 5928.0 ⟵ “Housing & Food | 11,855.00 | 5,928.00 | 11,855.00”
  - column:Fees: 250.0 ⟵ “Fees | 1,493.00 | 250.00 | 1,493.00”
  - column:Course Materials, Supplies, & Equipment: 649.0 ⟵ “Course Materials, Supplies, & Equipment | 1,298.00 | 649.00 | 1,298.00”
  - column:Transportation: 1362.0 ⟵ “Transportation | 2,724.00 | 1,362.00 | 2,724.00”
  - column:Personal & Misc.: 1563.0 ⟵ “Personal & Misc. | 3,125.00 | 1,563.00 | 3,125.00”
  - column:Total: 20732.0 ⟵ “Total | 53,675.00 | 20,732.00 | 59,420.00”
  - column:Tuition: 38925.0 ⟵ “Tuition | 33,180.00 | 10,980.00 | 38,925.00”
  - column:Housing & Food: 11855.0 ⟵ “Housing & Food | 11,855.00 | 5,928.00 | 11,855.00”
  - column:Fees: 1493.0 ⟵ “Fees | 1,493.00 | 250.00 | 1,493.00”
  - column:Course Materials, Supplies, & Equipment: 1298.0 ⟵ “Course Materials, Supplies, & Equipment | 1,298.00 | 649.00 | 1,298.00”
  - column:Transportation: 2724.0 ⟵ “Transportation | 2,724.00 | 1,362.00 | 2,724.00”
  - column:Personal & Misc.: 3125.0 ⟵ “Personal & Misc. | 3,125.00 | 1,563.00 | 3,125.00”
  - column:Total: 59420.0 ⟵ “Total | 53,675.00 | 20,732.00 | 59,420.00”
### `ee8fecb5e2f658d5` Kentucky Wesleyan College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://kwc.edu/admissions/dual-credit/ (sha256 1c5d6cd64fbd)
- issues: stale_year_label:2025-26
- checks: {"fields": ["per_credit_hour_charges", "state_grant_accepted", "tuition_per_credit_hour"], "tiers": 0}
  - per_credit_hour_charge: 97 ⟵ “For the 2025–2026 academic year, tuition is $97 per credit hour, representing a 95 percent discount from standard first-year tuition rates.”
  - state_grant_accepted: True ⟵ “Eligible students may also qualify for the Kentucky Dual Credit Scholarship through KHEAA. This scholarship covers the cost of up to two general education dual credit courses taken through Kentucky Wesleyan College.”
### `377ebc89e4175d1f` Lindsey Wilson College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lindsey.edu/about-lwc/Offices-and-Services/Financial-Aid/Financial-Aid.cfm (sha256 e1f18a93b754)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students will have the opportunity to submit an online SAP appeal form.”
### `3dfa46f1d6098a10` Lindsey Wilson College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lindsey.edu/about-lwc/Offices-and-Services/Financial-Aid/Financial-Aid.cfm (sha256 e1f18a93b754)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Form Please contact the Financial Aid Office if you are requesting a Special Circumstance Form.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance Form Please contact the Financial Aid Office if you are requesting a Unusual Circumstance Form.”
### `97d2722528fc8406` Lindsey Wilson College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lindsey.edu/about-lwc/Offices-and-Services/Financial-Aid/Financial-Aid.cfm (sha256 e1f18a93b754)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “If you do not meet any of the criteria listed above, but can document extreme family circumstances that prevent you from obtaining your parents information/support, you may file for a Dependency Override with the Financial Aid Office for a possible reevaluation of your status.”
### `e266821b2a99c513` Lindsey Wilson College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lindsey.edu/about-lwc/Offices-and-Services/Financial-Aid/Financial-Aid.cfm (sha256 e1f18a93b754)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Students may contact the Financial Aid office and request the Special Circumstances(previously referred to as Professional Judgements) or Unusual Circumstances (previously referred to as Dependcy Override) form.”
### `5210d3c8bea79404` Lindsey Wilson College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.lindsey.edu/admissions/img/Information25_26_Booklet.pdf (sha256 d2f1add20881)
- issues: ambiguous_year_labels, arrangement_unlabeled, conflicting_sources:https://www.lindsey.edu/admissions/cost-and-financial-aid/
- checks: {"columns": 2, "rows": 10}
  - column:Tuition (Full Time: 12 -18 hrs per semester): 14040 ⟵ “Tuition (Full Time: 12 -18 hrs per semester) | $14,040 | Tuition (Full Time: 12 -18 hrs per semester) | $14,040”
  - column:Activity Fee: 92 ⟵ “Activity Fee | $92 | Activity Fee | $92”
  - column:Technology Fee: 64 ⟵ “Technology Fee | $64 | Technology Fee | $64”
  - column:Housing: 1886 ⟵ “Housing | $1,886 | Housing | $1,886”
  - column:Food: 3305 ⟵ “Food | $3,305 | Food | $3,305”
  - column:Projected Cost for Commuting Student: 14196 ⟵ “Projected Cost for Commuting Student | $14,196 | Projected Cost for Commuting Student | $14,196”
  - column:Projected Cost for Residential Student: 19387 ⟵ “Projected Cost for Residential Student | $19,387 | Projected Cost for Residential Student | $19,387”
  - column:Student-Athlete Health Insurance: 420 ⟵ “Student-Athlete Health Insurance | $420*”
  - column:Housing Fee: 50 ⟵ “Housing Fee | $50”
  - column:1-800-264-0138 • admissions@lindsey.edu: 2 ⟵ “1-800-264-0138 • admissions@lindsey.edu | 2”
  - column:1-800-264-0138 • admissions@lindsey.edu: 4 ⟵ “1-800-264-0138 • admissions@lindsey.edu | 4”
  - column:1-800-264-0138 • admissions@lindsey.edu: 8 ⟵ “1-800-264-0138 • admissions@lindsey.edu | 8”
  - column:1-800-264-0138 • admissions@lindsey.edu: 10 ⟵ “1-800-264-0138 • admissions@lindsey.edu | 10”
  - column:1-800-264-0138 • admissions@lindsey.edu: 12 ⟵ “1-800-264-0138 • admissions@lindsey.edu | 12”
  - column:1-800-264-0138 • admissions@lindsey.edu: 14 ⟵ “1-800-264-0138 • admissions@lindsey.edu | 14”
  - column:1-800-264-0138 • admissions@lindsey.edu: 16 ⟵ “1-800-264-0138 • admissions@lindsey.edu | 16”
  - column:1-800-264-0138 • admissions@lindsey.edu: 18 ⟵ “1-800-264-0138 • admissions@lindsey.edu | 18”
  - column:Tuition (Full Time: 12 -18 hrs per semester): 14040 ⟵ “Tuition (Full Time: 12 -18 hrs per semester) | $14,040 | Tuition (Full Time: 12 -18 hrs per semester) | $14,040”
  - column:Activity Fee: 92 ⟵ “Activity Fee | $92 | Activity Fee | $92”
  - column:Technology Fee: 64 ⟵ “Technology Fee | $64 | Technology Fee | $64”
  - column:Housing: 1886 ⟵ “Housing | $1,886 | Housing | $1,886”
  - column:Food: 3305 ⟵ “Food | $3,305 | Food | $3,305”
  - column:Projected Cost for Commuting Student: 14196 ⟵ “Projected Cost for Commuting Student | $14,196 | Projected Cost for Commuting Student | $14,196”
  - column:Projected Cost for Residential Student: 19387 ⟵ “Projected Cost for Residential Student | $19,387 | Projected Cost for Residential Student | $19,387”
### `53c20f3b27d49819` Lindsey Wilson College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lindsey.edu/admissions/cost-and-financial-aid/ (sha256 a1593f88a60b)
- issues: components_do_not_reconcile, conflicting_sources:https://www.lindsey.edu/admissions/img/Information25_26_Booklet.pdf
- checks: {"columns": 1, "components_reconcile": false, "rows": 40}
  - column:Tuition - 12-18 hours: 14328 ⟵ “Tuition - 12-18 hours | $14,328”
  - column:Activity Fee: 94 ⟵ “Activity Fee | $94”
  - column:Technology Fee: 66 ⟵ “Technology Fee | $66”
  - column:Housing: 1924 ⟵ “Housing | $1,924”
  - column:Food: 3371 ⟵ “Food | $3,371”
  - column:Total for Residential Student: 19783 ⟵ “Total for Residential Student | $19,783”
  - column:Day College Tuition - More than 18 hours: 1194 ⟵ “Day College Tuition - More than 18 hours | $1,194”
  - column:Day College Tuition - Less than 12 hours: 1194 ⟵ “Day College Tuition - Less than 12 hours | $1,194”
  - column:Community Campuses: 474 ⟵ “Community Campuses | $474”
  - column:Dual Credit (High School): 97 ⟵ “Dual Credit (High School) | $97”
  - column:Business Administration: 318 ⟵ “Business Administration | $318”
  - column:Communications: 318 ⟵ “Communications | $318”
  - column:Criminial Justice: 318 ⟵ “Criminial Justice | $318”
  - column:Human Services: 474 ⟵ “Human Services | $474”
  - column:Interdisciplinary Studies: 318 ⟵ “Interdisciplinary Studies | $318”
  - column:RN to BSN: 318 ⟵ “RN to BSN | $318”
  - column:A.P. White Campus in Columbia: 756 ⟵ “A.P. White Campus in Columbia | $756”
  - column:Community Campuses: 540 ⟵ “Community Campuses | $540”
  - column:Online: 540 ⟵ “Online | $540”
  - column:MBA: Master of Business Administration: 455 ⟵ “MBA: Master of Business Administration | $455”
  - column:MSCB: Master of Science in Cybersecurity Management & Business Administration: 455 ⟵ “MSCB: Master of Science in Cybersecurity Management & Business Administration | $455”
  - column:MSCM: Master of Science in Cybersecurity Management: 455 ⟵ “MSCM: Master of Science in Cybersecurity Management | $455”
  - column:MSDB: Master of Science in Data Science & Business Administration: 455 ⟵ “MSDB: Master of Science in Data Science & Business Administration | $455”
  - column:MSDS: Master of Science in Data Science: 455 ⟵ “MSDS: Master of Science in Data Science | $455”
  - column:MSMA: Master of Science in Applied Machine Learning and AI: 455 ⟵ “MSMA: Master of Science in Applied Machine Learning and AI | $455”
  - … 17 more rows
### `1a55ff3ce6a7b71c` Madisonville Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://madisonville.kctcs.edu/affording-college/professional-judgment.aspx (sha256 08e90320532c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment is comprised of two components, unusual circumstances and special circumstances.”
### `2d249c0e10df023f` Madisonville Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://madisonville.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 1e4da97b2c24)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 15}
  - sentence: sap_appeal ⟵ “To appeal, students must complete a SAP Appeal Form available in the Student Self-Service and provide any additional information/documents required by the college.”
  - sentence: sap_appeal ⟵ “To appeal, students must complete a SAP Appeal Form available in their Student Self-Service.”
  - sentence: sap_appeal ⟵ “Students who were determined to have exceeded Maximum Time Frame (MTF) may request their coursework be evaluated based on classes needed for their current credential 1.7.1 Appeal Requirements To appeal, students must complete a SAP Appeal Form available in their Student Self-Service and provide any additional information/documents required by the college.”
  - sentence: sap_appeal ⟵ “The appeal will be evaluated by the SAP Appeals Committee of the home college.”
  - sentence: sap_appeal ⟵ “WHO REVIEWS SAP APPEALS AT KCTCS COLLEGES?”
  - sentence: sap_appeal ⟵ “Each college has a Satisfactory Academic Progress Appeals Committee.”
### `cf0345293ae658c7` Madisonville Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://madisonville.kctcs.edu/affording-college/professional-judgment.aspx (sha256 08e90320532c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Unusual Circumstances refer to the conditions that justify an aid administrator to make an adjustment to a student’s dependency status based on a unique situation, this is more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances include but not limited to: Loss or change of employment Reduction in income or assets Loss or change in amount of child support, Social Security, or other benefits Divorce or separation of parents Death of parent(s) Unusual medical expenses (not covered by insurance) One-time taxable income used for life-changing events (e.g.”
  - sentence: need_based_special_circumstances ⟵ “A member of the Financial Aid Office will contact you within 10 business days to submit an in-depth special circumstances request form as well as additional documentation once this form has been received.”
### `56fe5d865bbcf18a` Maysville Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://maysville.kctcs.edu/affording-college/satisfactory-academic-progress/satisfactory-academic-progress.aspx (sha256 1d9fdf421aad)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If that is the case you should submit a SAP Appeal Request through your Student Self-Service.”
  - sentence: sap_appeal ⟵ “SAP Appeal Requests are reviewed by a college Appeals Review Committee.”
  - sentence: sap_appeal ⟵ “Select the task SAP Appeal OnBase. 4.”
  - sentence: sap_appeal ⟵ “You may now start your SAP appeal. 7.”
### `6feee54ba80db790` Murray State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.murraystate.edu/admissions/financialaid/SatisfactoryAcademicProgress.aspx (sha256 787b266ff17f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “To initiate a Financial Aid SAP appeal, you must complete a SAP Financial Aid appeal form and provide supporting documentation as outlined below.”
### `a2f6ad57a6ab2934` Murray State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.murraystate.edu/admissions/scholarships/faq.aspx (sha256 f5ffb26c1627)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: competing_offer_review ⟵ “While Murray State doesn't provide exact dollar-for-dollar matching of scholarship offers from other institutions, we strongly advise students to reach out to the Scholarship Office for a thorough assessment of their scholarship offer. | Is there an overaward policy? | Overaward Policy Purpose: The Financial Aid Overaward Policy at Murray State University is designed to ensure fair and equitable d”
### `ed786a49b863fc68` Murray State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.murraystate.edu/admissions/scholarships/faq.aspx (sha256 f5ffb26c1627)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “An email will be sent following the conclusion of the spring semester audit with instructions on how to complete the appeal application. | What if I lost my scholarship eligibility, can I earn it back at a later date if my GPA improves or if I am full-time? | Scholarships that have been removed due to not meeting the renewal requirements cannot be reinstated at a later date.”
### `11e69c3a6d697efe` Murray State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.murraystate.edu/admissions/BursarsOffice/tuition/UndergraduateTuition.aspx (sha256 ed4c1b825ed3)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 9}
  - column:Tuition & Fees: 10530.0 ⟵ “Tuition & Fees | $10,530.00 | $11,088.00 | $15,990.00”
  - column:Housing: 6880.0 ⟵ “Housing | $6,880.00 | $6,880.00 | $6,880.00”
  - column:food: 5540.0 ⟵ “food | $5,540.00 | $5,540.00 | $5,540.00”
  - column:loan fee: 39.0 ⟵ “loan fee | $39.00 | $39.00 | $39.00”
  - column:subtotal: 22989.0 ⟵ “subtotal | $22,989.00 | $23,547.00 | $28,449.00”
  - column:books: 1010.0 ⟵ “books | $1,010.00 | $1,010.00 | $1,010.00”
  - column:personal: 2430.0 ⟵ “personal | $2,430.00 | $2,430.00 | $2,430.00”
  - column:transportation: 1380.0 ⟵ “transportation | $1,380.00 | $1,380.00 | $1,380.00”
  - column:subtotal: 4820.0 ⟵ “subtotal | $4,820.00 | $4,820.00 | $4,820.00”
  - column:estimated total cost of attendance: 27809.0 ⟵ “estimated total cost of attendance | $27,809.00 | $28,367.00 | $33,269.00”
### `ba504a103313ef90` Murray State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.murraystate.edu/admissions/BursarsOffice/tuition/UndergraduateTuition.aspx (sha256 ed4c1b825ed3)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 9}
  - column:Tuition & Fees: 28500.0 ⟵ “Tuition & Fees | $10,530.00 | $12,756.00 | $11,136.00 | $18,756.00 | $13,788.00 | $12,240.00 | $11,136.00 | $28,500.00”
  - column:Housing: 6880.0 ⟵ “Housing | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00”
  - column:food: 5540.0 ⟵ “food | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00”
  - column:loan fee: 39.0 ⟵ “loan fee | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00”
  - column:subtotal: 40959.0 ⟵ “subtotal | $22,989.00 | $25,215.00 | $23,595.00 | $31,215.00 | $26,247.00 | $24,669.00 | $23,595.00 | $40,959.00”
  - column:books: 1010.0 ⟵ “books | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00”
  - column:personal: 2430.0 ⟵ “personal | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00”
  - column:transportation: 1380.0 ⟵ “transportation | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00”
  - column:subtotal: 4820.0 ⟵ “subtotal | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00”
  - column:estimated total cost of attendance: 45779.0 ⟵ “estimated total cost of attendance | $27,809.00 | $30,035.00 | $28,415.00 | $36,035.00 | $31,067.00 | $29,519.00 | $28,415.00 | $45,779.00”
### `bfd085ab340eabf5` Murray State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.murraystate.edu/admissions/BursarsOffice/tuition/UndergraduateTuition.aspx (sha256 ed4c1b825ed3)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_names_another_state, residency_unknown
- checks: {"columns": 6, "components_reconcile": false, "rows": 9}
  - column:Tuition & Fees: 12756.0 ⟵ “Tuition & Fees | $10,530.00 | $12,756.00 | $11,136.00 | $18,756.00 | $13,788.00 | $12,240.00 | $11,136.00 | $28,500.00”
  - column:Housing: 6880.0 ⟵ “Housing | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00”
  - column:food: 5540.0 ⟵ “food | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00”
  - column:loan fee: 39.0 ⟵ “loan fee | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00”
  - column:subtotal: 25215.0 ⟵ “subtotal | $22,989.00 | $25,215.00 | $23,595.00 | $31,215.00 | $26,247.00 | $24,669.00 | $23,595.00 | $40,959.00”
  - column:books: 1010.0 ⟵ “books | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00”
  - column:personal: 2430.0 ⟵ “personal | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00”
  - column:transportation: 1380.0 ⟵ “transportation | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00”
  - column:subtotal: 4820.0 ⟵ “subtotal | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00”
  - column:estimated total cost of attendance: 30035.0 ⟵ “estimated total cost of attendance | $27,809.00 | $30,035.00 | $28,415.00 | $36,035.00 | $31,067.00 | $29,519.00 | $28,415.00 | $45,779.00”
  - column:Tuition & Fees: 11136.0 ⟵ “Tuition & Fees | $10,530.00 | $12,756.00 | $11,136.00 | $18,756.00 | $13,788.00 | $12,240.00 | $11,136.00 | $28,500.00”
  - column:Housing: 6880.0 ⟵ “Housing | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00”
  - column:food: 5540.0 ⟵ “food | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00”
  - column:loan fee: 39.0 ⟵ “loan fee | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00”
  - column:subtotal: 23595.0 ⟵ “subtotal | $22,989.00 | $25,215.00 | $23,595.00 | $31,215.00 | $26,247.00 | $24,669.00 | $23,595.00 | $40,959.00”
  - column:books: 1010.0 ⟵ “books | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00 | $1,010.00”
  - column:personal: 2430.0 ⟵ “personal | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00 | $2,430.00”
  - column:transportation: 1380.0 ⟵ “transportation | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00 | $1,380.00”
  - column:subtotal: 4820.0 ⟵ “subtotal | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00 | $4,820.00”
  - column:estimated total cost of attendance: 28415.0 ⟵ “estimated total cost of attendance | $27,809.00 | $30,035.00 | $28,415.00 | $36,035.00 | $31,067.00 | $29,519.00 | $28,415.00 | $45,779.00”
  - column:Tuition & Fees: 18756.0 ⟵ “Tuition & Fees | $10,530.00 | $12,756.00 | $11,136.00 | $18,756.00 | $13,788.00 | $12,240.00 | $11,136.00 | $28,500.00”
  - column:Housing: 6880.0 ⟵ “Housing | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00 | $6,880.00”
  - column:food: 5540.0 ⟵ “food | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00 | $5,540.00”
  - column:loan fee: 39.0 ⟵ “loan fee | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00 | $39.00”
  - column:subtotal: 31215.0 ⟵ “subtotal | $22,989.00 | $25,215.00 | $23,595.00 | $31,215.00 | $26,247.00 | $24,669.00 | $23,595.00 | $40,959.00”
  - … 35 more rows
### `c0bf5a12bda5a318` Owensboro Community and Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://owensboro.kctcs.edu/admissions/information-for/international-students/cost-and-financial-verification.aspx (sha256 a29145613241)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition (2 semesters): 6480 ⟵ “Tuition (2 semesters) | $6,480*”
  - column:Living Expenses: 8000 ⟵ “Living Expenses | $8,000”
  - column:Books, Medical Insurance (required): 1500 ⟵ “Books, Medical Insurance (required) | $1,500”
  - column:Total: 15980 ⟵ “Total | $15,980**”
### `ec798d2bad2cc658` Owensboro Community and Technical College — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://owensboro.kctcs.edu/admissions/information-for/discover_college/early-college.aspx (sha256 62f87d5c0c3d)
- issues: stale_year_label:2025-26
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "state_grant_accepted", "tuition_per_credit_hour"], "tiers": 2}
  - eligibility_tier: 3.5 ⟵ “3.5 unweighted GPA and possible standardized test scores. Students apply through their”
  - eligibility_tier: 3.5 ⟵ “to enroll must have a 3.5 unweighted GPA and possible standardized test scores depending”
  - per_credit_hour_charge: 97 ⟵ “rate of regular tuition and was $97 per credit hour.”
  - state_grant_accepted: True ⟵ “Each student is eligible for 4 total Dual Credit Scholarships through KHEAA that covers”
### `091da7f32e54d397` Simmons College of Kentucky — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://simmonscollegeky.edu/cost-of-attendance/ (sha256 62646dfda1a9)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 13200 ⟵ “Tuition | $6,600 | $13,200”
  - column:Registration Fee: 300 ⟵ “Registration Fee | $150 | $300”
  - column:Activity Fee: 400 ⟵ “Activity Fee | $200 | $400”
  - column:Room & Board: 8750 ⟵ “Room & Board | $4,375 | $8,750”
  - column:Enrollment Fee (One-time payment): 150 ⟵ “Enrollment Fee (One-time payment) | $150 | $150**”
  - column:Student Insurance: 120 ⟵ “Student Insurance | $60 | $120”
  - column:Total: 22920 ⟵ “Total | $11,535 | $22,920”
### `71b7bbdc89ea07db` Somerset Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://somerset.kctcs.edu/admissions/information-for/international-students/additional-information.aspx (sha256 69c8911a1037)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition (2 semesters): 15000 ⟵ “Tuition (2 semesters) | $15,000”
  - column:Living expenses (Estimated): 8000 ⟵ “Living expenses (Estimated) | $8,000”
  - column:Books, Medical Insurance (required): 2000 ⟵ “Books, Medical Insurance (required) | $2,000”
  - column:Total: 25000 ⟵ “Total | $25,000”
### `bdc8d2660fc9efd5` Somerset Community College — credit_policies 2017-18 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://somerset.kctcs.edu/admissions/information-for/dual-credit.aspx (sha256 b977915997db)
- issues: stale_year_label:2017-18
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "tiers": 1}
  - state_grant_accepted: True ⟵ “the same cost break. To be eligible for a dual credit scholarship, a student must”
  - eligibility_tier: 2.0 ⟵ “be enrolled in a Kentucky public high school with a minimum 2.0 GPA,”
### `674b62f1d49c5b44` Southcentral Kentucky Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://southcentral.kctcs.edu/affording-college/satisfactory-academic-progress/index.aspx (sha256 4ba0f92af5e8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: sap_appeal ⟵ “SAP Appeal Request Process Students who are suspended but have mitigating or extenuating circumstances may be eligible to file a SAP Appeal Request.”
  - sentence: sap_appeal ⟵ “SAP Appeal Requests are reviewed by a college Appeals Review Committee.”
  - sentence: sap_appeal ⟵ “Students must be able to pay for tuition and books in order to remain enrolled while a SAP Appeal Request is under review.”
  - sentence: sap_appeal ⟵ “SAP appeals require at least 30 days for review.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Approval process is not complete and awards will not be made until the Financial Aid Office receives the accepted academic plan of action document from the student.”
  - sentence: sap_appeal ⟵ “If the SAP appeal is denied, the student is not eligible for federal student aid and will remain ineligible until they are again in compliance with SAP standards.”
### `f0b5bc815f631825` Southcentral Kentucky Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://southcentral.kctcs.edu/affording-college/paying-for-college/scholarships/scholarship-faq.aspx (sha256 4495c4fc3a61)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “It is important to read your award notification letter carefully as it may indicate special circumstances.”
### `6209f47b8e0f1bae` Southeast Kentucky Community & Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://southeast.kctcs.edu/affording-college/professional-judgement.aspx (sha256 b52e8b12f2da)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment is comprised of two components, unusual circumstances and special circumstances.”
### `cc4b65bd925e8bd2` Southeast Kentucky Community & Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://southeast.kctcs.edu/affording-college/professional-judgement.aspx (sha256 b52e8b12f2da)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Unusual Circumstances refer to the conditions that justify an aid administrator to make an adjustment to a student’s dependency status based on a unique situation, this is more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances include but not limited to: Loss or change of employment Reduction in income or assets Loss or change in amount of child support, Social Security, or other benefits Divorce or separation of parents Death of parent(s) Unusual medical expenses (not covered by insurance) One-time taxable income used for life-changing events (e.g.”
### `1f8d2791164ef040` Spalding University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://spalding.edu/financial-aid/cost-of-attendance/ (sha256 5b5917970f98)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - column:Tuition (full-time): 30900 ⟵ “Tuition (full-time) | *$30,900”
  - column:Fees: 300 ⟵ “Fees | $300”
  - column:Housing and Food: 13568 ⟵ “Housing and Food | *$13,568”
  - column:Supplies, Course Materials and Equipment (no cost for books!): 200 ⟵ “Supplies, Course Materials and Equipment (no cost for books!) | $200”
  - column:Transportation: 1494 ⟵ “Transportation | $1,494”
  - column:Personal Expenses: 6365 ⟵ “Personal Expenses | $6,365”
  - column:Total Cost of Attendance: 52726 ⟵ “Total Cost of Attendance | $52,726”
### `c64112da7b91db07` The Southern Baptist Theological Seminary — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sbts.edu/financial-aid/scholarships-and-grants/online-scholarships/ (sha256 bd9a68fd41db)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Macy’s Emergency Scholarship Fund Website: https://www.lnesc.org/macys-scholarship Deadline: Apply in time of need Eligibility: Must be enrolled full time GPA of 3.0 or higher Emergency financial need from: change in family income/support, loss of job, death of an immediate family member, natural disaster, pending eviction or home foreclosure, burglary, fire.”
### `dd0c90cc79e88b4b` The Southern Baptist Theological Seminary — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.sbts.edu/admissions/international-students/international-admissions-guide/ (sha256 56fd252f27ac)
- issues: arrangement_unlabeled
- checks: {"columns": 7, "rows": 3}
  - column:Tuition and Fees: 10000 ⟵ “Tuition and Fees | $10,000 | $6,000 | $7,000 | $5,000 | $7,500 | $9,000 | $8,000”
  - column:Living Expenses: 7000 ⟵ “Living Expenses | $7,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000”
  - column:Required Health Insurance: 3000 ⟵ “Required Health Insurance | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000”
  - column:Tuition and Fees: 6000 ⟵ “Tuition and Fees | $10,000 | $6,000 | $7,000 | $5,000 | $7,500 | $9,000 | $8,000”
  - column:Living Expenses: 12000 ⟵ “Living Expenses | $7,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000”
  - column:Required Health Insurance: 3000 ⟵ “Required Health Insurance | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000”
  - column:Tuition and Fees: 7000 ⟵ “Tuition and Fees | $10,000 | $6,000 | $7,000 | $5,000 | $7,500 | $9,000 | $8,000”
  - column:Living Expenses: 12000 ⟵ “Living Expenses | $7,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000”
  - column:Required Health Insurance: 3000 ⟵ “Required Health Insurance | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000”
  - column:Tuition and Fees: 5000 ⟵ “Tuition and Fees | $10,000 | $6,000 | $7,000 | $5,000 | $7,500 | $9,000 | $8,000”
  - column:Living Expenses: 12000 ⟵ “Living Expenses | $7,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000”
  - column:Required Health Insurance: 3000 ⟵ “Required Health Insurance | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000”
  - column:Tuition and Fees: 7500 ⟵ “Tuition and Fees | $10,000 | $6,000 | $7,000 | $5,000 | $7,500 | $9,000 | $8,000”
  - column:Living Expenses: 12000 ⟵ “Living Expenses | $7,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000”
  - column:Required Health Insurance: 3000 ⟵ “Required Health Insurance | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000”
  - column:Tuition and Fees: 9000 ⟵ “Tuition and Fees | $10,000 | $6,000 | $7,000 | $5,000 | $7,500 | $9,000 | $8,000”
  - column:Living Expenses: 12000 ⟵ “Living Expenses | $7,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000”
  - column:Required Health Insurance: 3000 ⟵ “Required Health Insurance | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000”
  - column:Tuition and Fees: 8000 ⟵ “Tuition and Fees | $10,000 | $6,000 | $7,000 | $5,000 | $7,500 | $9,000 | $8,000”
  - column:Living Expenses: 12000 ⟵ “Living Expenses | $7,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000 | $12,000”
  - column:Required Health Insurance: 3000 ⟵ “Required Health Insurance | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000 | $3,000”
### `457d8799bdc68362` Thomas More University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/student-rights-and-responsibilities/ (sha256 8ba7b0ce1ed4)
- issues: semantic_review_required, conflicting_sources:https://www.thomasmore.edu/admissions/scholarships-financial-aid/faqs/,https://www.thomasmore.edu/admissions/scholarships-financial-aid/special-conditioning-processing/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Notify the Office of Financial Aid of the following information, as it may result in a change in your award: Changes in income or unusual circumstances not noted on FAFSA.”
### `64eeccedb08bbb5d` Thomas More University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/faqs/ (sha256 ef698ec58ff0)
- issues: semantic_review_required, conflicting_sources:https://www.thomasmore.edu/admissions/scholarships-financial-aid/special-conditioning-processing/,https://www.thomasmore.edu/admissions/scholarships-financial-aid/student-rights-and-responsibilities/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “What if my family has special circumstances that we could not list on the FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “A Special Circumstances form is available through the Thomas More Financial Aid Office for extraordinary or special financial circumstances.”
### `9421ee19af73811d` Thomas More University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/special-conditioning-processing/ (sha256 688daf73a8bb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “The typical hardships which may warrant consideration are (but are not limited to): unusual medical and dental expenses elementary, secondary, and post-secondary school tuition income reduction or nonrecurring income unusual debts support of extended family parents enrolled in college plus loan denial cost of attendance adjustment For more information on cost of attendance please visit our Estimat”
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustment Adjustment to any cost of attendance component may be adjusted based on appropriate documentation.”
### `96f2b763a1c736b6` Thomas More University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/satisfactory-academic-progress-policy/ (sha256 189a272ce525)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Probation – Failure to make SAP, but student has appealed and appeal has been approved.”
  - sentence: sap_appeal ⟵ “A priority deadline can be established for each semester, generally within the following time frame: June 15 for Fall semester Monday before classes begin for Spring semester June 1 for summer Students are notified of their SAP appeal decision through their Thomas More e-mail account.”
### `a128092fdf37c198` Thomas More University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/special-conditioning-processing/ (sha256 688daf73a8bb)
- issues: semantic_review_required, conflicting_sources:https://www.thomasmore.edu/admissions/scholarships-financial-aid/faqs/,https://www.thomasmore.edu/admissions/scholarships-financial-aid/student-rights-and-responsibilities/
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: need_based_special_circumstances ⟵ “The TMU Special Circumstances Processing Guidelines are intended to provide the basis for consistent treatment of all aid applicants with similar circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Regardless of the reason for a special circumstance request, the student must verify the accuracy of the income and tax information reported on the FAFSA by submitting a copy of their and/or their parent’s federal tax return(s) or complete the verification process for those selected for verification.”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Special Circumstance Processing I.”
  - sentence: need_based_special_circumstances ⟵ “TMU Special Circumstance Form Families must complete and submit the TMU Special Circumstance form to the Financial Aid Office for review and processing in order to consider special circumstances that might affect the SAI.”
  - sentence: need_based_special_circumstances ⟵ “The TMU Special Circumstance form must be signed by the student and at least one parent if the student is dependent.”
  - sentence: need_based_special_circumstances ⟵ “The spouse of an independent student is not required to sign the Special Circumstance form.”
### `c922a8195ab145f8` Thomas More University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/faqs/ (sha256 ef698ec58ff0)
- issues: semantic_review_required, conflicting_sources:https://www.thomasmore.edu/admissions/scholarships-financial-aid/special-conditioning-processing/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Your financial aid administrator takes all factors into consideration and uses fair professional judgment to determine eligibility for additional financial aid.”
### `cc1b3ca7bfc955e9` Thomas More University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/special-conditioning-processing/ (sha256 688daf73a8bb)
- issues: semantic_review_required, conflicting_sources:https://www.thomasmore.edu/admissions/scholarships-financial-aid/faqs/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Such expenses may be considered under professional judgment.”
  - sentence: professional_judgment ⟵ “Such expenses may be considered under professional judgment.”
### `70bf794c61c2faec` Thomas More University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.thomasmore.edu/admissions/scholarships-financial-aid/estimated-cost-of-attendance/ (sha256 a1a35791cbd4)
- issues: ambiguous_year_labels, arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 10}
  - column:Tuition: 42600 ⟵ “Tuition | $42,600 |  | Tuition | $42,600 |  | Tuition | $42,600”
  - column:Orientation Fee**: 275 ⟵ “Orientation Fee** | $275 |  | Orientation Fee** | $275 |  | Orientation Fee** | $275”
  - column:Living (food and housing): 11650 ⟵ “Living (food and housing) | $11,650 |  |  |  |  |  | ”
  - column:Supplies: 1200 ⟵ “Supplies | $1,200 |  | Supplies | $1,200 |  | Supplies | $1,200”
  - column:Transportation: 1078 ⟵ “Transportation | $1,078 |  | Transportation | $2,158 |  | Transportation | $2,158”
  - column:Personal: 3628 ⟵ “Personal | $3,628 |  | Personal | $7,256 |  | Personal | $3,628”
  - column:Loan Fees: 66 ⟵ “Loan Fees | $66 |  | Living (off campus) | $8,644 |  | Living (off campus) | $1,710”
  - column:Total Estimated COA: 60497 ⟵ “Total Estimated COA | $60,497 |  | Total Estimated COA | $62,247 |  | Total Estimated COA | $51,637”
  - column:Total Direct Cost: 54525 ⟵ “Total Direct Cost | $54,525 |  | Total Direct Cost | $42,875 |  | Total Direct Cost | $42,875”
  - column:Total Indirect Cost: 5972 ⟵ “Total Indirect Cost | $5,972 |  | Indirect Cost | $19,372 |  | Indirect Cost | $8,762”
  - with_parents_or_family:Tuition: 42600 ⟵ “Tuition | $42,600 |  | Tuition | $42,600 |  | Tuition | $42,600”
  - with_parents_or_family:Orientation Fee**: 275 ⟵ “Orientation Fee** | $275 |  | Orientation Fee** | $275 |  | Orientation Fee** | $275”
  - with_parents_or_family:Supplies: 1200 ⟵ “Supplies | $1,200 |  | Supplies | $1,200 |  | Supplies | $1,200”
  - with_parents_or_family:Transportation: 2158 ⟵ “Transportation | $1,078 |  | Transportation | $2,158 |  | Transportation | $2,158”
  - with_parents_or_family:Personal: 7256 ⟵ “Personal | $3,628 |  | Personal | $7,256 |  | Personal | $3,628”
  - with_parents_or_family:Loan Fees: 8644 ⟵ “Loan Fees | $66 |  | Living (off campus) | $8,644 |  | Living (off campus) | $1,710”
  - with_parents_or_family:Total Estimated COA: 62247 ⟵ “Total Estimated COA | $60,497 |  | Total Estimated COA | $62,247 |  | Total Estimated COA | $51,637”
  - with_parents_or_family:Total Direct Cost: 42875 ⟵ “Total Direct Cost | $54,525 |  | Total Direct Cost | $42,875 |  | Total Direct Cost | $42,875”
  - with_parents_or_family:Total Indirect Cost: 19372 ⟵ “Total Indirect Cost | $5,972 |  | Indirect Cost | $19,372 |  | Indirect Cost | $8,762”
  - column:Tuition: 42600 ⟵ “Tuition | $42,600 |  | Tuition | $42,600 |  | Tuition | $42,600”
  - column:Orientation Fee**: 275 ⟵ “Orientation Fee** | $275 |  | Orientation Fee** | $275 |  | Orientation Fee** | $275”
  - column:Supplies: 1200 ⟵ “Supplies | $1,200 |  | Supplies | $1,200 |  | Supplies | $1,200”
  - column:Transportation: 2158 ⟵ “Transportation | $1,078 |  | Transportation | $2,158 |  | Transportation | $2,158”
  - column:Personal: 3628 ⟵ “Personal | $3,628 |  | Personal | $7,256 |  | Personal | $3,628”
  - column:Loan Fees: 1710 ⟵ “Loan Fees | $66 |  | Living (off campus) | $8,644 |  | Living (off campus) | $1,710”
  - … 3 more rows
### `d7cebff096c7309f` Transylvania University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.transy.edu/financial-aid/ (sha256 c4713b3cd8b2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If your financial situation changes or special circumstances aren’t reflected on your FAFSA, you can submit a FAFSA recalculation request.”
### `1e4aefef53e02ce8` Transylvania University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.transy.edu/financial-aid/cost-of-attendance/ (sha256 ca99c73584b3)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.transy.edu/campus/student-accounts/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 48920 ⟵ “Tuition and Fees | 48,920”
  - column:Living Expenses, including food & housing: 14570 ⟵ “Living Expenses, including food & housing | 14,570”
  - column:Total:: 63490 ⟵ “Total: | $63,490”
### `3be99d91aa6eee85` Transylvania University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.transy.edu/financial-aid/cost-of-attendance/ (sha256 ca99c73584b3)
- issues: conflicting_sources:https://www.transy.edu/campus/student-accounts/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 50640 ⟵ “Tuition and Fees | 50,640”
  - column:Living Expenses, including food & housing: 15010 ⟵ “Living Expenses, including food & housing | 15,010”
  - column:Total:: 65650 ⟵ “Total: | $65,650”
### `78c2630e341b9610` Transylvania University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.transy.edu/campus/student-accounts/ (sha256 5723e370487f)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.transy.edu/financial-aid/cost-of-attendance/
- checks: {"columns": 1, "rows": 6}
  - column:Reservation fee upperclass: 200 ⟵ “Reservation fee upperclass | $200”
  - column:Late registration fee: 250 ⟵ “Late registration fee | $250”
  - column:Returned check fee: 10 ⟵ “Returned check fee | $10”
  - column:Applied music fee (Per applied music course fee policy): 200 ⟵ “Applied music fee (Per applied music course fee policy) | $200”
  - column:Application fee for non‑degree students: 50 ⟵ “Application fee for non‑degree students | $50”
  - column:Tuition refund plan (optional) More information about the 2025‑26 tuition refund plan: 410 ⟵ “Tuition refund plan (optional) More information about the 2025‑26 tuition refund plan | $410”
### `f8c591dfc9596d47` Transylvania University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.transy.edu/campus/student-accounts/ (sha256 5723e370487f)
- issues: conflicting_sources:https://www.transy.edu/financial-aid/cost-of-attendance/
- checks: {"columns": 1, "rows": 4}
  - column:Full‑time tuition: 48380 ⟵ “Full‑time tuition | $48,380”
  - column:Level Tuition Plan (LTP) premium: 2200 ⟵ “Level Tuition Plan (LTP) premium | $2,200”
  - column:General fee (full‑time students): 2260 ⟵ “General fee (full‑time students) | $2,260”
  - column:Tuition for 9th semester student teaching: 1000 ⟵ “Tuition for 9th semester student teaching | $1,000”
### `dcb1f3e603752f6b` University of Kentucky — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://studentsuccess.uky.edu/financial-aid-and-scholarships/estimated-cost-attendance (sha256 6fa3970af38f)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition and Fees1,2: 41194 ⟵ “Tuition and Fees1,2 | 41,194 | 41,194 | 49,740 | 49,740”
  - off_campus_not_with_family:Food and Housing: 21008 ⟵ “Food and Housing | 21,008 | 15,436 | 21,008 | 15,436”
  - off_campus_not_with_family:Books and Supplies: 1200 ⟵ “Books and Supplies | 1,200 | 1,200 | 1,200 | 1,200”
  - off_campus_not_with_family:Travel: 2756 ⟵ “Travel | 2,756 | 2,592 | 3,582 | 3,418”
  - off_campus_not_with_family:Personal: 3240 ⟵ “Personal | 3,240 | 3,240 | 3,240 | 3,240”
  - off_campus_not_with_family:Loan Origination: 176 ⟵ “Loan Origination | 176 | 176 | 176 | 176”
  - off_campus_not_with_family:TOTAL: 69574 ⟵ “TOTAL | 69,574 | 63,838 | 78,946 | 73,210”
### `4047d95226729720` University of Kentucky — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://admission.uky.edu/sites/default/files/2025-12/ce_25-26.pdf (sha256 b2827ff6bf73)
- issues: stale_year_label:2025-26
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 36 ⟵ “Additionally, 30 of the final 36 credit hours earned toward a UK degree must be completed at UK.”
### `22b5345f4948c159` University of Louisville — appeals 2026-27 [new] (source_unlabeled)
- source: https://louisville.edu/financialaid/about-student-financial-aid-office/policies/satisfactory-academic-progress-appeal-process (sha256 fd1c77102333)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Home About Student Financial Aid Office Policies Satisfactory Academic Progress Appeal Process Satisfactory Academic Progress Appeal Process How to Regain Eligibility You can regain eligibility for federal aid and state need based aid through self-correction or through the appeal process.”
  - sentence: sap_appeal ⟵ “Please read the information below for your options to submit a SAP appeal.”
  - sentence: sap_appeal ⟵ “Instructions for Submitting an Appeal Complete the SAP appeal application.”
  - sentence: sap_appeal ⟵ “The Additional Information for Deferred SAP Appeal (pdf) should be printed and submitted as a coversheet.”
### `a4b980f0b7fed983` University of Louisville — appeals 2026-27 [new] (source_unlabeled)
- source: https://louisville.edu/financialaid/about-student-financial-aid-office/policies/satisfactory-academic-progress-appeal-process (sha256 fd1c77102333)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The Student Financial Aid Office uses professional judgment to review appeals on an individual case-by-case basis to evaluate the information submitted by you for each appeal.”
### `8260e60248c3a641` University of Louisville — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/annual-undergraduate-tuition-fees (sha256 bb7aa42d94e8)
- issues: components_do_not_reconcile, residency_names_another_state, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - column:Tuition & Fees: 13614 ⟵ “Tuition & Fees | $13,614”
  - column:Room Rates**: 7972 ⟵ “Room Rates** | $7,972”
  - column:Meal Plan (Unlimited 7 & 175 Plan): 4898 ⟵ “Meal Plan (Unlimited 7 & 175 Plan) | $4,898”
  - column:Total:: 26484 ⟵ “Total: | $26,484”
  - column:+ Books & Supplies (Average Cost): 980 ⟵ “+ Books & Supplies (Average Cost) | $980”
### `fcf87582644a98f7` University of Louisville — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://louisville.edu/cost-aid/undergraduate-scholarships-aid/annual-undergraduate-tuition-fees (sha256 bb7aa42d94e8)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - column:Tuition & Fees: 29960 ⟵ “Tuition & Fees | $29,960”
  - column:Room Rates*: 7972 ⟵ “Room Rates* | $7,972”
  - column:Meal Plan (Unlimited 7 & 175 Plan): 4898 ⟵ “Meal Plan (Unlimited 7 & 175 Plan) | $4,898”
  - column:Total:: 42830 ⟵ “Total: | $42,830”
  - column:+ Books & Supplies (Average Cost): 980 ⟵ “+ Books & Supplies (Average Cost) | $980”
### `8e68f0fb13499cf8` University of Pikeville — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.upike.edu/undergraduate/financial-aid/financial-aid-appeals/ (sha256 9f231a6fc4b9)
- issues: semantic_review_required, conflicting_sources:https://www.upike.edu/undergraduate/financial-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial aid will not be awarded until SAP is met and a SAP appeal is approved.”
### `ab22231dd052a5ff` University of Pikeville — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.upike.edu/undergraduate/financial-aid/financial-aid-appeals/ (sha256 9f231a6fc4b9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustment The Financial Aid Office has developed a realistic estimate of the costs associated with attending the University of Pikeville.”
  - sentence: budget_increase ⟵ “If you believe that the standard Cost of Attendance does not accurately reflect your basic educational expenses, you may submit a Cost of Attendance Adjustment Appeal.”
### `b8f493b55a8cfee2` University of Pikeville — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.upike.edu/undergraduate/financial-aid/financial-aid-appeals/ (sha256 9f231a6fc4b9)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 8}
  - sentence: need_based_special_circumstances ⟵ “Appeals allow the student an opportunity to provide additional documentation about their specific circumstances. grounds for initiating an appeal are categorized as: Unusual Circumstances — when a unique situation merits an adjustment to a student’s dependency status Special Circumstances — when there are changes in a student’s/families’ financial situation.”
  - sentence: need_based_special_circumstances ⟵ “For more information about the different types of appeal, select from the options below: Unusual Circumstances Unusual Circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (e.g., human trafficking, refugee or asylee status, parental abuse or abandonment, incarceration), more commonly referred to as”
  - sentence: need_based_special_circumstances ⟵ “Circumstances that will be considered, include but are not limited to: Abandonment by parents Abusive family environment threatens the student’s health or safety Parent incarceration Student is unable to locate parents human trafficking, refugee or asylum status Special Circumstances Special Circumstances refers to the financial situations (loss of a job, etc.) that allow the financial aid office ”
  - sentence: need_based_special_circumstances ⟵ “To review these situations, we use the special circumstance appeal, which allows you and your family to document your individual financial situation.”
  - sentence: need_based_special_circumstances ⟵ “If you are facing one of the situations listed below, please consider submitting a Special Circumstance Request to the Financial Aid Office: Special Circumstances include but not limited to: Loss or change of employment Voluntary job separation, examples such as, but not limited to quitting to go to school, moving states, or change of careers, will generally not be considered.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances may be considered.”
### `f7f26ba5c4ec7ec9` University of Pikeville — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.upike.edu/undergraduate/financial-aid/sap/ (sha256 7c14a437dd17)
- issues: semantic_review_required, conflicting_sources:https://www.upike.edu/undergraduate/financial-aid/financial-aid-appeals/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Students Rights Student’s Right to Appeal a SAP Suspension: If you, as a student, have had an extenuating circumstance that has prevented you from completing the minimum standards set within the UPIKE Satisfactory Academic Progress policy, you have the right to appeal the decision with the UPIKE Satisfactory Academic Progress Appeals Committee.”
  - sentence: sap_appeal ⟵ “After the probated term, the student will be monitored again and must be meeting the minimum standards of SAP or completing the SAP academic plan successfully that was designed for the student upon SAP appeal approval.”
  - sentence: sap_appeal ⟵ “SAP appeal decisions are final and cannot be appealed/escalated to the Department of Education.”
### `00ca707aea5ea68b` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $10,000 ⟵ “PNC Student Solution Scholarship | Website | Open to all | $10,000 | 5/31 and 11/31 yearly”
### `0850a62c55a37a54` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,750 ⟵ “2.75-2.99 | Appalachian Academic Achievement | $3,750”
  - gpa_requirement: 2.75-2.99 ⟵ “2.75-2.99 | Appalachian Academic Achievement | $3,750”
### `0bca8be601817e06` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “Hirenest Academic Scholarship | Website | Open to all | $5,000 | Every fall and spring”
### `0cd480e52aee2531` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,200 ⟵ “Optometry Scholars Program Scholarship* | Admitted to program | $3,200”
### `0d6117f8f79c93aa` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Dick Hannah Scholarship | Website | High School Seniors | $1,000 | 12/15 and 6/15 yearly”
### `14987e87bea03954` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “The Women in Golf Annual Scholarship | Website | Women Golfers | $1,000 | 11/20 yearly”
### `1839793afaaf4683` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Top Nutrition Coaching’s Annual Heroes’ Legacy Scholarship | Website | One parent in Military | $1,000 | 9/1 yearly”
### `215519f95ad2225e` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $500-$1,000 ⟵ “Single Parent Scholarship | Website | Single Parents | $500-$1,000 | Every Summer, Spring and Fall”
### `2827277a8efb557b` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “General Dual Credit Program*† | Completion of five hours with “B” or better average at any other institution | $1,000”
### `2def9752c44a3674` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “JobTest.org’s scholarship | Website | Open to all | $1,000 | 9/1 yearly”
### `2ee1508ca6907e62` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “InfantCPR Safebaby Scholarship | Website | BS in Healthcare (RNBSN program) | $1,000 | 1/10 and 7/10 yearly”
### `34808750a7d6287a` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Study.com | Website | * Single parent scholarship * Scholarship for Moms * Scholarship for Transfer Students * Adult Learner Scholarship * Scholarship for Nontraditional Students * Scholarship for Military members & Veterans * Scholarship for Future Teachers * Scholarship for Business Students * Sch”
### `3a6112ece6713649` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000-$2,000 per scholarship ⟵ “Heroes Scholarship Foundation | Website | Multiple scholarship available -Military family members -Firefigher and family -Law enforcement and family -African American -Immigrant -Student Nurse -Student Doctor | $1,000-$2,000 per scholarship | None”
### `3a91074d31924001` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,200 ⟵ “Governor’s Scholar*§ | Completion of program | $3,200”
### `3b94064dff2e87cf` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “The Domaine Scholarship | Website | UG Only | $2,000 | 12/1/24 and 5/1/25”
### `3e5758f2918ccef5` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “LocalProbook scholarship | Website | Open to all | $500 | 8/15 and 12/15 yearly”
### `4b1d192aa6442aa5` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Pheabs Finance Scholarship | Website | Open to all | $1,000 | 8/7 yearly”
### `4c81df81700c8bad` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “The Visionaries of Tomorrow Scholarship | Website | GPA > 3.0 | $1,000 | Quarterly (3/31, 6/30, 9/30, 12/31)”
### `596d427d80126bdf` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Learner’s Annual Women in STEM Scholarship | Website | Women in STEM | $1,000 | 11/20 yearly”
### `5cd6f12a5933ee55` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Marketing Scholarship | Website | Open to all | $1,000 | 12/31 yearly”
### `60cab908e31c24f6` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": {"gpa_min": 3.75}}
  - award_amount_text: $8,000 ⟵ “3.75 and above | Trustee Excellence Scholarship | $8,000”
  - gpa_requirement: 3.75 and above ⟵ “3.75 and above | Trustee Excellence Scholarship | $8,000”
### `61dcc1fb296b8d05` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Organic Life Start Scholarship | Website | Open to all | $500 | 12/31 and 6/30 yearly”
### `646ac3782fb9bba9` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $300 ⟵ “The Hawker Online Journalist Scholarship | Website | Open to all | $300 | 10/1 yearly”
### `66b099755ed2597f` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,200 ⟵ “Early College Academy*§ | Completion of program | $3,200”
### `6d8b8a4d81d1530f` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “EcoHugs Green Future Scholarship | Website | Open to all | $500 | 9/30 and 3/1 yearly”
### `7741a7cc6eb52a96` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “Discover Scholarship | Website | Open to all | $5,000 | Monthly”
### `79dc3a6f9fceccd9` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “CFF Foundation Education Award | Website | Open to all | $1,500 | Quarterly”
### `7c303af0898a8ff5` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “BeMo Diversity Advocacy Scholarship | Website | Pre-med or medical students | $5,000 | 5/31 and 10/31 yearly”
### `81026a9742b982e2` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Mental Health Importance Scholarship | Website | Open to all | $1,000 | 11/1 yearly”
### `8246512efc66b3df` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “Future of Finance Scholarship | Website | Open to all | $2,000 | 8/17 yearly”
### `880b4b3eb58109ee` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,200 ⟵ “Osteopathic Medical Scholars Program Scholarship* | Admitted to program | $3,200”
### `89992ad98e57eb29` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,500 ⟵ “UPIKE Dual Credit Program*† | Completion of five hours with “B” or better average | $3,500”
### `8a9d6ecdf15c9bf9` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $6,750 ⟵ “3.5-3.74 | Provost Leadership Award | $6,750”
  - gpa_requirement: 3.5-3.74 ⟵ “3.5-3.74 | Provost Leadership Award | $6,750”
### `9080abb417771634` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “RealtyHop Scholarship | Website | Open to all | $1,000 | 4/30 and 8/31 yearly”
### `914948bfe83c6939` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: Amounts Vary ⟵ “Athletic Scholarships | Athletic talent | Amounts Vary”
### `92bd1d8e8376a32b` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Formuland Mighty Star Scholarship | Website | Open to all | $1,000 | 9/30 and 3/1 yearly”
### `979bbe4535429374` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Eco-Warrior Scholarship | Website | Open to all | $1,000 | 12/1 yearly”
### `97f33324432fd16f` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Blankstyle Scholarship Fund | Website | Open to all | $1,000 | 12/31 and 6/1 yearly”
### `99e6adf8d4f3f8f1` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “The Space to Succeed Scholarship | Website | Open to all | $5,000 | 5/31 yearly”
### `9e07dc330ecaadf3` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “ADHDAdvisor’s Mental Health Advocate Scholarship | Website | Open to all | $1,000 | 8/1 yearly”
### `9ed818f938599d79` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “RentHop: College & University Scholarship Program | Website | Open to all | $1,000 | 4/30 and 8/31 yearly”
### `a4ab5045f073860e` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: Amounts Vary ⟵ “Organizational Scholarship Band, Choir, Academic Team | Audition/Interview | Amounts Vary”
### `a73af6c512163804` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “The Finger Finance Scholarship | Website | Math, Business or Accounting majors | $1,000 | 11/5 yearly”
### `ac938939877105db` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Mental Health Scholarship | Website | Undergrad | $1,000 | Every fall and spring”
### `acbf909563f08d50` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Incfile’s Entrepreneur Grant | Website | Must have interest in starting a business | $2,500 | 3/31, 6/30 and 9/30 yearly”
### `af1e38f98ed9d12a` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “3.0-3.49 | Dean Service Award | $5,000”
  - gpa_requirement: 3.0-3.49 ⟵ “3.0-3.49 | Dean Service Award | $5,000”
### `c7c71252df7258b4` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,200 ⟵ “Rogers’ Scholar* | Completion of program | $3,200”
### `cbeefbbebf983755` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Chairish Scholarship | Website | Open to all | $2,500 | 1/1 and 6/30 yearly”
### `cdb873bb881592b1` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “The UPG Scholarship | Website | Open to all | $1,000 | 5/31 yearly”
### `cf35f821b48cc4db` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “The Richard Rawle Memorial Scholarship | Website | Open to all | $2,000 | 1/1 till 6/1 yearly”
### `da6fa152519d0538` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “The Strategic Air Services Scholarship | Website | Open to all | $1,000 | 12/1 yearly”
### `dcfb452c5dd75b96` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Super Greens Powder Scholarship | Website | Nursing Students | $1,000 | 9/1 yearly”
### `e36c88eed10e12b2` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “2.74 and below | Mountain Merit Award | $3,000”
  - gpa_requirement: 2.74 and below ⟵ “2.74 and below | Mountain Merit Award | $3,000”
### `e7ff3b315c375c0d` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Trending Impact Journalist Scholarship | Website | Open to all / 2.0 GPA | $500 | 9/1 yearly”
### `f532d799a89d08b7` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “THE UTOPIA MANAGEMENT SCHOLARS FUND | Website | 3.5 GPA – Higher | $1,000 | 5/1 and 11/1 yearly”
### `f6ba800478c56ca2` University of Pikeville — awards 2025-26 [new] (labeled_in_heading)
- source: https://www.upike.edu/undergraduate/financial-aid/scholarships/ (sha256 0e3a201a1b35)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Eco-Innovation Scholarship | Website | Open to all | $1,000 | 9/1 yearly”
### `4e52ecb5a80f728b` University of Pikeville — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.upike.edu/undergraduate/financial-aid/cost-of-attendance/ (sha256 9b3509d27683)
- issues: arrangement_unlabeled, components_do_not_reconcile
- checks: {"columns": 4, "components_reconcile": false, "rows": 11}
  - column:Months in Academic Year: 9 ⟵ “Months in Academic Year | 9 | 10 | 12 | 12”
  - column:Tuition: 49950 ⟵ “Tuition | $49,950 | $49,950 | $49,950 | $49,950”
  - column:Institutional Cost: 49950 ⟵ “Institutional Cost | $49,950 | $49,950 | $49,950 | $49,950”
  - column:Food: 4734 ⟵ “Food | $4,734 | $5,260 | $6,312 | $6,312”
  - column:Housing: 10242 ⟵ “Housing | $10,242 | $11,380 | $13,656 | $13,656”
  - column:Transportation: 3222 ⟵ “Transportation | $3,222 | $3,580 | $4,296 | $4,296”
  - column:Misc.: 7020 ⟵ “Misc. | $7,020 | $7,800 | $9,360 | $9,360”
  - column:Supplies: 300 ⟵ “Supplies | $300 | $450 | $450 | $450”
  - column:Loan Fees 2: 438 ⟵ “Loan Fees 2 | $438 | $438 | $438 | $438”
  - column:Insurance: 5660 ⟵ “Insurance | $5,660 | $5,660 | $5,660 | $5,660”
  - column:Total: 81566 ⟵ “Total | $81,566 | $84,518 | $90,122 | $94,897”
  - column:Months in Academic Year: 10 ⟵ “Months in Academic Year | 9 | 10 | 12 | 12”
  - column:Tuition: 49950 ⟵ “Tuition | $49,950 | $49,950 | $49,950 | $49,950”
  - column:Institutional Cost: 49950 ⟵ “Institutional Cost | $49,950 | $49,950 | $49,950 | $49,950”
  - column:Food: 5260 ⟵ “Food | $4,734 | $5,260 | $6,312 | $6,312”
  - column:Housing: 11380 ⟵ “Housing | $10,242 | $11,380 | $13,656 | $13,656”
  - column:Transportation: 3580 ⟵ “Transportation | $3,222 | $3,580 | $4,296 | $4,296”
  - column:Misc.: 7800 ⟵ “Misc. | $7,020 | $7,800 | $9,360 | $9,360”
  - column:Supplies: 450 ⟵ “Supplies | $300 | $450 | $450 | $450”
  - column:Loan Fees 2: 438 ⟵ “Loan Fees 2 | $438 | $438 | $438 | $438”
  - column:Insurance: 5660 ⟵ “Insurance | $5,660 | $5,660 | $5,660 | $5,660”
  - column:Total: 84518 ⟵ “Total | $81,566 | $84,518 | $90,122 | $94,897”
  - column:Months in Academic Year: 12 ⟵ “Months in Academic Year | 9 | 10 | 12 | 12”
  - column:Tuition: 49950 ⟵ “Tuition | $49,950 | $49,950 | $49,950 | $49,950”
  - column:Institutional Cost: 49950 ⟵ “Institutional Cost | $49,950 | $49,950 | $49,950 | $49,950”
  - … 20 more rows
### `53819cfaf86a7061` University of Pikeville — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.upike.edu/wp-content/uploads/2025/02/COA-2024-2025.pdf (sha256 8f21b317ed09)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2024-25
- checks: {"columns": 4, "rows": 30}
  - column:Weekly 10 (on campus): 2250 ⟵ “Weekly 10 (on campus) | $2,250”
  - column:Unlimited 250 (on campus): 2250 ⟵ “Unlimited 250 (on campus) | $2,250”
  - column:Unlimited 375 (on campus): 2360 ⟵ “Unlimited 375 (on campus) | $2,360”
  - column:Tuition: 25500 ⟵ “Tuition | *$25,500”
  - column:Fees: 150 ⟵ “Fees | *$150”
  - column:Food: 4500 ⟵ “Food | *$4,500”
  - column:Housing: 4800 ⟵ “Housing | *$4,800”
  - column:Books, Supplies, Course Materials, and Equipment: 190 ⟵ “Books, Supplies, Course Materials, and Equipment | $190”
  - column:Transportation: 1998 ⟵ “Transportation | $1,998”
  - column:Personal Expenses: 9504 ⟵ “Personal Expenses | $9,504”
  - column:Total Cost of Attendance: 46642 ⟵ “Total Cost of Attendance | $46,642”
  - column:Tuition: 25500 ⟵ “Tuition | *$25,500”
  - column:Fees: 150 ⟵ “Fees | *$150”
  - column:Food: 2952 ⟵ “Food | $2,952”
  - column:Housing: 6876 ⟵ “Housing | $6,876”
  - column:Books, Supplies, Course Materials, and Equipment: 2988 ⟵ “Books, Supplies, Course Materials, and Equipment | $2,988”
  - column:Transportation: 190 ⟵ “Transportation | $190”
  - column:Personal Expenses: 9504 ⟵ “Personal Expenses | $9,504”
  - column:Total Cost of Attendance: 46642 ⟵ “Total Cost of Attendance | $46,642”
  - column:Tuition: 25500 ⟵ “Tuition | *$25,500”
  - column:Fees: 150 ⟵ “Fees | *$150”
  - column:Food: 4410 ⟵ “Food | $4,410”
  - column:Housing: 10260 ⟵ “Housing | $10,260”
  - column:Books, Supplies, Course Materials, and Equipment: 2988 ⟵ “Books, Supplies, Course Materials, and Equipment | $2,988”
  - column:Transportation: 190 ⟵ “Transportation | $190”
  - … 223 more rows
### `c073d583ae597ee1` University of Pikeville — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.upike.edu/wp-content/uploads/2025/12/COA-2025-2026.pdf (sha256 c8dd7fa041ff)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 4, "rows": 24}
  - column:Tuition: 25500 ⟵ “Tuition | *$25,500”
  - column:Fees: 150 ⟵ “Fees | *$150”
  - column:Food: 4500 ⟵ “Food | *$4,500”
  - column:Housing: 4800 ⟵ “Housing | *$4,800”
  - column:Books, Supplies, Course Materials, and Equipment: 190 ⟵ “Books, Supplies, Course Materials, and Equipment | $190”
  - column:Transportation: 2998 ⟵ “Transportation | $2,998”
  - column:Personal Expenses: 9504 ⟵ “Personal Expenses | $9,504”
  - column:Tuition: 25500 ⟵ “Tuition | *$25,500”
  - column:Fees: 150 ⟵ “Fees | *$150”
  - column:Food: 2952 ⟵ “Food | $2,952”
  - column:Housing: 6876 ⟵ “Housing | $6,876”
  - column:Books, Supplies, Course Materials, and Equipment: 190 ⟵ “Books, Supplies, Course Materials, and Equipment | $190”
  - column:Transportation: 2988 ⟵ “Transportation | $2,988”
  - column:Personal Expenses: 9504 ⟵ “Personal Expenses | $9,504”
  - column:Tuition: 25500 ⟵ “Tuition | *$25,500”
  - column:Fees: 150 ⟵ “Fees | *$150”
  - column:Food: 4410 ⟵ “Food | $4,410”
  - column:Housing: 10260 ⟵ “Housing | $10,260”
  - column:Books, Supplies, Course Materials, and Equipment: 190 ⟵ “Books, Supplies, Course Materials, and Equipment | $190”
  - column:Transportation: 2988 ⟵ “Transportation | $2,988”
  - column:Personal Expenses: 9504 ⟵ “Personal Expenses | $9,504”
  - column:Masters of Business Administration (MBA): 30 ⟵ “Masters of Business Administration (MBA) | 30 | $490”
  - column:Teacher Leader Program (TLP): 30 ⟵ “Teacher Leader Program (TLP) | 30 | $355”
  - column:Masters of Science in Strategic Communication (MSC): 30 ⟵ “Masters of Science in Strategic Communication (MSC) | 30 | $490”
  - column:Semester Tuition*: 4410 ⟵ “Semester Tuition* | $4,410 | $2,130 | $4,860 | $4,410”
  - … 219 more rows
### `4dc8c583d1249cbf` University of the Cumberlands — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucumberlands.edu/admission-aid/financial-aid-tuition/financial-resources/sap (sha256 587202957e37)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 34}
  - sentence: sap_appeal ⟵ “SAP Instructions SAP Appeal Outlines How to Write a SAP Appeal Letter SAP Policy Details Quantitative Students are expected to successfully complete at least 67% of all attempted credit hours and must complete their program within 150% of its published length.”
  - sentence: sap_appeal ⟵ “Appeals Students placed on Financial Aid Suspension who wish to regain eligibility for Federal, State and institutional aid have the option to submit a SAP appeal.”
  - sentence: sap_appeal ⟵ “Circumstances that CANNOT be used in a SAP appeal include need for financial aid, work-related issues, problems with web-based classes, and improper advising.”
  - sentence: sap_appeal ⟵ “Please refer to the SAP Appeal Outline linked above for a full list of acceptable and unacceptable extenuating circumstances.”
  - sentence: sap_appeal ⟵ “Your SAP appeal letter should include information that will tell us why you failed to make SAP.”
  - sentence: sap_appeal ⟵ “Please submit supporting documentation with your SAP appeal.”
### `5e01861e5f5c5a12` University of the Cumberlands — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucumberlands.edu/admission-aid/financial-aid-tuition/financial-resources/sap (sha256 587202957e37)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Examples of acceptable circumstances include the death of a relative, an injury or illness of the student, and other special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Examples of acceptable circumstances include the death of a relative, an injury or illness of the student, and other unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Examples of acceptable circumstances include the death of a relative, an injury or illness of the student, and other special circumstances.”
### `12c097dce087db86` University of the Cumberlands — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ucumberlands.edu/tuition-aid/tuition/cost-attendance (sha256 fed13328f072)
- issues: arrangement_unlabeled, implausible_amount, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 2}
  - column:Tuition and Fees: 220 ⟵ “Tuition and Fees | $220 | 12 | $2,640 | $7,920”
  - column:Technology Fees: 0 ⟵ “Technology Fees | 0 | 0 | $0 | $0”
  - column:Tuition and Fees: 7920 ⟵ “Tuition and Fees | $220 | 12 | $2,640 | $7,920”
  - column:Technology Fees: 0 ⟵ “Technology Fees | 0 | 0 | $0 | $0”
  - column:Books, Supplies, Course Materials, and Equipment: 1800 ⟵ “Books, Supplies, Course Materials, and Equipment |  | 12 | $600 | $1,800”
  - column:Food and Housing: 26820 ⟵ “Food and Housing |  | 12 | $8,940 | $26,820”
  - column:Transportation: 3396 ⟵ “Transportation |  | 12 | $1,132 | $3,396”
  - column:Loan Fees: 135 ⟵ “Loan Fees |  | 12 | $45 | $135”
  - column:Miscellaneous: 4500 ⟵ “Miscellaneous |  | 12 | $1,500 | $4,500”
  - column:Total: 44571 ⟵ “Total |  |  | $14,857 | $44,571”
### `89bd16aa394462d1` University of the Cumberlands — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.ucumberlands.edu/admissions/high-school-students/dual-credit (sha256 bf5aecd0b342)
- issues: conflicting_values:max_credit_hours_per_term
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 2}
  - eligibility_tier: 2.0 ⟵ “A GPA of 2.0 or higher, with a minimum ACT composite score of 18”
  - eligibility_tier: 3.0 ⟵ “3.0 GPA without qualifying ACT scores”
  - max_credit_hours_per_term: 13 ⟵ “The tuition for dual credit courses is $51.00 per in-seat course at Cumberlands, $147.00 per online course, $51.00 in-seat at the high school, and $25 per 1-hour lab course, up to 13 hours per semester, fall and spring.”
  - max_credit_hours_per_term: 18 ⟵ “Seniors may overload up to 18 hours per semester, fall and spring (with high school approval). Overload fees for hours over 13 are $220.00 per credit hour.”
  - per_credit_hour_charge: 220 ⟵ “Seniors may overload up to 18 hours per semester, fall and spring (with high school approval). Overload fees for hours over 13 are $220.00 per credit hour.”
  - eligibility_tier: 2.0 ⟵ “A GPA of 2.0 or higher, with a minimum ACT composite score of 18”
  - eligibility_tier: 3.0 ⟵ “3.0 GPA without qualifying ACT scores”
### `4caa8f2870dd78a8` West Kentucky Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://westkentucky.kctcs.edu/affording-college/professional-judgement.aspx (sha256 599d58e7ecfa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment is comprised of two components, unusual circumstances and special circumstances.”
### `e8575310724c679b` West Kentucky Community and Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://westkentucky.kctcs.edu/affording-college/professional-judgement.aspx (sha256 599d58e7ecfa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Unusual Circumstances refer to the conditions that justify an aid administrator to make an adjustment to a student’s dependency status based on a unique situation, this is more commonly referred to as a dependency override.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances include but not limited to: Loss or change of employment Reduction in income or assets Loss or change in amount of child support, Social Security, or other benefits Divorce or separation of parents Death of parent(s) Unusual medical expenses (not covered by insurance) One-time taxable income used for life-changing events (e.g.”
  - sentence: need_based_special_circumstances ⟵ “A member of the Financial Aid Office will contact you within 10 business days to submit an in-depth special circumstances request form as well as additional documentation once this form has been received.”
### `155378f1d5851b54` Western Kentucky University — academic_programs 2026-27 · program_key=dance-bachelor-of-arts-630p-630 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/dance-ba/ (sha256 f4f5bd40773f)
- issues: requirement_groups_skipped
- checks: {"courses": 10, "groups": 5, "groups_skipped": 1}
  - program_name: Dance, Bachelor of Arts (630P, 630) ⟵ “Dance, Bachelor of Arts (630P, 630) < Western Kentucky University”
### `1a97e18ff4615666` Western Kentucky University — academic_programs 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
- checks: {"courses": 474, "groups": 19, "groups_skipped": 1}
  - program_name: Visual Arts, Bachelor of Fine Arts (514P, 514) ⟵ “Visual Arts, Bachelor of Fine Arts (514P, 514) < Western Kentucky University”
### `28c1cd8b0251c2a8` Western Kentucky University — academic_programs 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
- checks: {"courses": 90, "groups": 23, "groups_skipped": 1}
  - program_name: Performing Arts, Bachelor of Fine Arts (588P, 588) ⟵ “Performing Arts, Bachelor of Fine Arts (588P, 588) < Western Kentucky University”
### `5fd326cd1bf6fe8f` Western Kentucky University — academic_programs 2026-27 · program_key=history-bachelor-of-arts-695e-695 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
- checks: {"courses": 186, "groups": 12, "groups_skipped": 1}
  - program_name: History, Bachelor of Arts (695E, 695) ⟵ “History, Bachelor of Arts (695E, 695) < Western Kentucky University”
### `632fc04f1b9534fa` Western Kentucky University — academic_programs 2026-27 · program_key=music-liberal-arts-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-liberal-arts-ba/ (sha256 387a2e064bcb)
- issues: requirement_groups_skipped
- checks: {"courses": 20, "groups": 6, "groups_skipped": 1}
  - program_name: Music (Liberal Arts), Bachelor of Arts ⟵ “Music (Liberal Arts), Bachelor of Arts (583) < Western Kentucky University”
### `6761436f0ee5dc98` Western Kentucky University — academic_programs 2026-27 · program_key=sociology-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/sociology-ba/ (sha256 a3ffc4936e95)
- issues: requirement_groups_skipped
- checks: {"courses": 22, "groups": 3, "groups_skipped": 1}
  - program_name: Sociology, Bachelor of Arts ⟵ “Sociology, Bachelor of Arts (775) < Western Kentucky University”
### `c7075cd886689c66` Western Kentucky University — academic_programs 2026-27 · program_key=music-bachelor-of-music [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
- checks: {"courses": 91, "groups": 25, "groups_skipped": 1}
  - program_name: Music, Bachelor of Music ⟵ “Music, Bachelor of Music (593) < Western Kentucky University”
### `f3f1640a0cd279fc` Western Kentucky University — academic_programs 2026-27 · program_key=asian-studies-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/asian-studies-ba/ (sha256 d4bf15768a8d)
- issues: requirement_groups_skipped
- checks: {"courses": 81, "groups": 4, "groups_skipped": 1}
  - program_name: Asian Studies, Bachelor of Arts ⟵ “Asian Studies, Bachelor of Arts (6002) < Western Kentucky University”
### `f6eac0374cd2a26c` Western Kentucky University — academic_programs 2026-27 · program_key=international-affairs-bachelor-of-arts [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/international-affairs-ba/ (sha256 fa9985d13bc4)
- issues: requirement_groups_skipped
- checks: {"courses": 92, "groups": 3, "groups_skipped": 1}
  - program_name: International Affairs, Bachelor of Arts ⟵ “International Affairs, Bachelor of Arts (702) < Western Kentucky University”
### `1161503d42620780` Western Kentucky University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wku.edu/financialaid/eligibility/sap-overview.php (sha256 f41a70de89a3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 20}
  - sentence: sap_appeal ⟵ “SAP Appeal Form Required Appeal Documentation What is the SAP Policy?”
  - sentence: sap_appeal ⟵ “Students who do not meet overall SAP standards while on warning status are ineligible for financial aid for any subsequent semester(s) until they meet the criteria for reinstatement of aid (which means reaching their SAP standards by paying out-of-pocket) or have gained approval based on SAP Appeal.”
  - sentence: sap_appeal ⟵ “Students who have reached their Maximum Time Frame may be eligible to submit a SAP Appeal.”
  - sentence: sap_appeal ⟵ “The earlier a student submits a SAP Appeal, the sooner eligibility for financial assistance can be determined.”
  - sentence: sap_appeal ⟵ “When can a student complete a SAP Appeal?”
  - sentence: sap_appeal ⟵ “A submission of a SAP Appeal (even based on the circumstances listed above) does NOT automatically guarantee an approval.”
### `38f37c608d170973` Western Kentucky University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wku.edu/financialaid/eligibility/sap-overview.php (sha256 f41a70de89a3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Extenuating Circumstances: If a student was on warning status, did not meet the terms of that status, and has documentable extenuating circumstances (i.e., illness, death of immediate family member, divorce, other unusual circumstances), he/she is eligible to submit an appeal for the term in which he/she is seeking aid.”
### `0e64886c47266059` Western Kentucky University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.wku.edu/admissions/cost/index.php (sha256 430d66f65fdf)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - column:Tuition (Full-time status taking between 12-18 hours): 27000 ⟵ “Tuition (Full-time status taking between 12-18 hours) | $27,000”
  - column:Application Fee: 50 ⟵ “Application Fee | $50”
  - column:Housing Application Fee: 75 ⟵ “Housing Application Fee | $75”
  - column:TOP Fee: 75 ⟵ “TOP Fee | $75”
  - column:M.A.S.T.E.R. Plan Fee**: 135 ⟵ “M.A.S.T.E.R. Plan Fee** | $135”
### `e4dabad76341b267` Western Kentucky University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.wku.edu/admissions/cost/index.php (sha256 430d66f65fdf)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 5}
  - column:Tuition (Full-time status taking between 12-18 hours): 12072 ⟵ “Tuition (Full-time status taking between 12-18 hours) | $12,072”
  - column:Application Fee: 50 ⟵ “Application Fee | $50”
  - column:Housing Application Fee: 75 ⟵ “Housing Application Fee | $75”
  - column:Topper Orientation Program (TOP) Fee: 75 ⟵ “Topper Orientation Program (TOP) Fee | $75”
  - column:M.A.S.T.E.R. Plan Fee**: 135 ⟵ “M.A.S.T.E.R. Plan Fee** | $135”
### `0172ecd394f3bb45` Western Kentucky University — degree_requirements 2026-27 · program_key=business-economics-bachelor-of-science · requirement_key=program-requirements-72-hours-economics-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/business-economics-bs/ (sha256 367d4d265754)
- issues: course_alternatives_in_rule_text
  - courses: ECON 203 ⟵ “ECON 203 - Principles of Economics (Macro)”
  - courses: ECON 302 ⟵ “ECON 302 - Microeconomic Theory”
  - courses: ECON 303 ⟵ “ECON 303 - Macroeconomic Theory”
  - courses: ECON 306 ⟵ “ECON 306 - Statistical Analysis”
  - courses: ECON 375 ⟵ “ECON 375 - Moral Issues of Capitalism 2”
  - courses: ECON 414 ⟵ “ECON 414 - Managerial Economics”
  - courses: ECON 465 ⟵ “ECON 465 - Regression and Econometric Analysis”
### `017e33d1c45942fb` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-theory-composition- [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 400 ⟵ “MUS 400 - Advanced Music Theory”
  - courses: MUS 405 ⟵ “MUS 405 - Choral Arranging”
  - courses: MUS 407 ⟵ “MUS 407 - Orchestration and Band Arranging”
### `02697a1c1748c74f` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-integrated-3 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MUS 215 ⟵ “MUS 215 - Brass Techniques”
  - courses: MUS 315 ⟵ “MUS 315 - Clarinet and Saxophone Techniques”
  - courses: MUS 316 ⟵ “MUS 316 - Flute and Double Reed Techniques”
  - courses: MUS 319 ⟵ “MUS 319 - Percussion Techniques”
  - courses: MUS 415 ⟵ “MUS 415 - Choral Methods”
  - courses: MUS 416 ⟵ “MUS 416 - Instrumental Methods”
  - courses: MUS 414 ⟵ “MUS 414 - Choral Materials”
### `026c350b0f901700` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=students-may-complete-more-than-one-concentration-however-a-single-elective-cann-3 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 308 ⟵ “HIST 308 - Conflict, Culture and Commerce in the Medieval Mediterranean”
  - courses: HIST 310 ⟵ “HIST 310 - Comparative Slavery”
  - courses: HIST 318 ⟵ “HIST 318 - Age of the Reformation”
  - courses: HIST 325 ⟵ “HIST 325 - Blacks in the Civil War and Reconstruction”
  - courses: HIST 332 ⟵ “HIST 332 - Riots, Rebellions, and Revolutions: A Global History of Protest”
  - courses: HIST 333 ⟵ “HIST 333 - History of Genocide”
  - courses: HIST 335 ⟵ “HIST 335 - Twentieth Century Europe”
  - courses: HIST 337 ⟵ “HIST 337 - Modern Irish History”
  - courses: HIST 338 ⟵ “HIST 338 - Topics in Russian History”
  - courses: HIST 339 ⟵ “HIST 339 - The Holocaust”
  - courses: HIST 343 ⟵ “HIST 343 - Communities of Struggle”
  - courses: HIST 348 ⟵ “HIST 348 - United States, 1900-1945”
  - courses: HIST 349 ⟵ “HIST 349 - The United States Since 1945”
  - courses: HIST 352 ⟵ “HIST 352 - Borderlands and the American West”
  - courses: HIST 379 ⟵ “HIST 379 - Gandhi: The Creation of a Global Legacy”
  - courses: HIST 380 ⟵ “HIST 380 - Human Rights in History”
  - courses: HIST 382 ⟵ “HIST 382 - History of the Bill of Rights”
  - courses: HIST 398 ⟵ “HIST 398 - War and Society to 1500”
  - courses: HIST 399 ⟵ “HIST 399 - War and Society Since 1500”
  - courses: HIST 407 ⟵ “HIST 407 - The Crusades: West Meets East”
  - courses: HIST 422 ⟵ “HIST 422 - The French Revolution and Napoleon”
  - courses: HIST 426 ⟵ “HIST 426 - Hitler and Nazi Germany”
  - courses: HIST 430 ⟵ “HIST 430 - History of the Civil Rights Movement in America”
  - courses: HIST 433 ⟵ “HIST 433 - Antisemitism in World History”
  - courses: HIST 441 ⟵ “HIST 441 - The American Revolution and Early Republic, 1763-1815”
  - … 8 more rows
### `0412678ca349d6b5` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-the-music-education-concentration-all-tracks-integrated-vocal-i-2 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 153 ⟵ “MUS 153 - Applied Music Principal (4 semesters)”
  - courses: MUS 353 ⟵ “MUS 353 - Applied Music Principal (3 semesters)”
  - courses: MUS 338 ⟵ “MUS 338 - DIR Independent Study (Senior Recital)”
### `056abbdc85cf8a53` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-communication-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
- issues: course_alternatives_in_rule_text
  - courses: SPAN 345 ⟵ “SPAN 345 - Topics in Spanish”
  - courses: SPAN 470 ⟵ “SPAN 470 - Advanced Oral Spanish”
  - courses: SPAN 389 ⟵ “SPAN 389 - Internship in Spanish”
### `064dccf71890bbe0` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=ux-design-concentration-ux-design-concentration-focus [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: UX 220 ⟵ “UX 220 - Introduction to User Experience Design”
  - courses: UX 310 ⟵ “UX 310 - Future Design”
  - courses: UX 330 ⟵ “UX 330 - User Interface Design”
  - courses: UX 340 ⟵ “UX 340 - Introduction to Developing and Prototyping for Interactive Design”
  - courses: DES 331 ⟵ “DES 331 - Visual Thinking”
  - courses: UX 400 ⟵ “UX 400 - User Experience Advanced Studio I”
  - courses: UX 430 ⟵ “UX 430 - Advanced User Interface Design”
  - courses: UX 440 ⟵ “UX 440 - Advanced Developing and Testing for Interactive Design”
  - courses: UX 450 ⟵ “UX 450 - User Experience Advanced Studio II”
### `07735ef4128d0440` Western Kentucky University — degree_requirements 2026-27 · program_key=sociology-bachelor-of-arts · requirement_key=core-courses-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/sociology-ba/ (sha256 a3ffc4936e95)
- issues: requirement_groups_skipped
  - courses: CRIM 330 ⟵ “CRIM 330 - Criminology”
  - courses: CRIM 332 ⟵ “CRIM 332 - Juvenile Delinquency”
  - courses: CRIM 361 ⟵ “CRIM 361 - Race, Class, and Crime”
  - courses: CRIM 370 ⟵ “CRIM 370 - Issues in Policing”
  - courses: CRIM 380 ⟵ “CRIM 380 - Punishment and Society”
  - courses: CRIM 432 ⟵ “CRIM 432 - Sociology of Criminal Law”
  - courses: CRIM 434 ⟵ “CRIM 434 - Organized Crime”
  - courses: CRIM 446 ⟵ “CRIM 446 - Gender, Crime, and Justice”
  - courses: CRIM 448 ⟵ “CRIM 448 - International Justice and Crime”
  - courses: CRIM 451 ⟵ “CRIM 451 - White-Collar Crime”
  - courses: CSJ 200 ⟵ “CSJ 200 - Introduction to Social Justice”
### `08d6154b62d7d503` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=professional-education-coursework [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
- issues: course_alternatives_in_rule_text
  - courses: EDU 250 ⟵ “EDU 250 - Discover Teaching: Introduction to Teacher Education”
  - courses: EDU 260 ⟵ “EDU 260 - Classroom Assessment”
  - courses: EDU 350 ⟵ “EDU 350 - Student Diversity and Differentiation”
  - courses: EDU 360 ⟵ “EDU 360 - Behavior and Classroom Management in Education”
  - courses: EDU 489 ⟵ “EDU 489 - Student Teaching Seminar”
  - courses: MLNG 410 ⟵ “MLNG 410 - Second Language Acquisition”
  - courses: MLNG 474 ⟵ “MLNG 474 - Teaching Foreign Language”
  - courses: PSY 310 ⟵ “PSY 310 - Educational Psychology: Development and Learning”
  - courses: LTCY 497 ⟵ “LTCY 497 - Literacy Competencies for Middle and High School Classroom Teachers”
  - courses: SEC 350 ⟵ “SEC 350 - Clinical Practices in Secondary Teaching I”
  - courses: SEC 490 ⟵ “SEC 490 - Student Teaching”
### `0a9352471eb809dd` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=performing-arts-core-career-prep-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PERF 175 ⟵ “PERF 175 - University Experience: Performing Arts”
  - courses: PERF 450 ⟵ “PERF 450 - Performing Arts Career Seminar”
  - courses: PERF 451 ⟵ “PERF 451 - Career Seminar Workshop”
  - courses: THEA 203 ⟵ “THEA 203 - Acting Audition Workshop”
### `0eb765e4a5997c65` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=performing-arts-core-history-theory-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 252 ⟵ “THEA 252 - Fundamentals of Theatre”
  - courses: THEA 363 ⟵ “THEA 363 - World Theatre History I”
### `109ed61d182aba9a` Western Kentucky University — degree_requirements 2026-27 · program_key=music-liberal-arts-bachelor-of-arts · requirement_key=additional-requirements-specific-to-the-music-extended-48-hour-program-applied-m [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-liberal-arts-ba/ (sha256 387a2e064bcb)
- issues: requirement_groups_skipped
  - courses: MUS 153 ⟵ “MUS 153 - Applied Music Principal (4 semesters)”
  - courses: MUS 353 ⟵ “MUS 353 - Applied Music Principal (2 semesters)”
  - courses: MUS 160 ⟵ “MUS 160 - Group Piano I 1”
  - courses: MUS 161 ⟵ “MUS 161 - Group Piano II 1”
### `10cf727256e0a6c2` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=acting-concentration-production-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 222 ⟵ “THEA 222 - Stagecraft”
  - courses: PERF 321 ⟵ “PERF 321 - Production Lab III”
### `112803b80fca8a8c` Western Kentucky University — degree_requirements 2026-27 · program_key=music-liberal-arts-bachelor-of-arts · requirement_key=requirements-for-both-concentrations-performance-attendance [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-liberal-arts-ba/ (sha256 387a2e064bcb)
- issues: requirement_groups_skipped
  - courses: MUS 155 ⟵ “MUS 155 - Performance Attendance (6 semesters)”
### `126ccbf41a43eae0` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-history-literature-6-hours-2 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 363 ⟵ “THEA 363 - World Theatre History I”
  - courses: THEA 375 ⟵ “THEA 375 - Topics in Drama”
### `1400ee65b94e1f33` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-vocal-trac-2 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 152 ⟵ “MUS 152 - Diction I for Voice Majors”
  - courses: MUS 252 ⟵ “MUS 252 - Diction II for Voice Majors”
  - courses: MUS 166 ⟵ “MUS 166 - Group Guitar I”
  - courses: MUS 360 ⟵ “MUS 360 - Accompanying”
### `14033e0c20f29b61` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-instrument [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 407 ⟵ “MUS 407 - Orchestration and Band Arranging”
### `1520d6e16620f103` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-technical-theatre-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: THEA 222 ⟵ “THEA 222 - Stagecraft”
  - courses: THEA 241 ⟵ “THEA 241 - Costume Technology”
  - courses: THEA 250 ⟵ “THEA 250 - Stage Electrics”
  - courses: THEA 311 ⟵ “THEA 311 - Stage Management”
### `15b7f9687c29b3a7` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=ux-design-concentration-upper-level-art-history-requirements [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 334 ⟵ “ART 334 - Survey of Graphic Design”
  - courses: ART 305 ⟵ “ART 305 - Ancient Greek and Roman Art”
  - courses: ART 312 ⟵ “ART 312 - Art of the United States to 1865”
  - courses: ART 313 ⟵ “ART 313 - Art of the United States Since 1865”
  - courses: ART 314 ⟵ “ART 314 - Southern Baroque Art”
  - courses: ART 315 ⟵ “ART 315 - Northern Baroque Art”
  - courses: ART 316 ⟵ “ART 316 - Medieval Art & Architecture”
  - courses: ART 317 ⟵ “ART 317 - Art and Power”
  - courses: ART 318 ⟵ “ART 318 - Art and Landscape”
  - courses: ART 325 ⟵ “ART 325 - Art of Asia, Africa, and the Americas”
  - courses: ART 390 ⟵ “ART 390 - Contemporary Art”
  - courses: ART 395 ⟵ “ART 395 - A Cultural History of Alcohol”
  - courses: ART 401 ⟵ “ART 401 - Art of the Italian Renaissance”
  - courses: ART 403 ⟵ “ART 403 - Northern Renaissance Art”
  - courses: ART 405 ⟵ “ART 405 - Art Theory and Criticism”
  - courses: ART 407 ⟵ “ART 407 - Islamic Art and Architecture”
  - courses: ART 408 ⟵ “ART 408 - European Art, 1700-1848”
  - courses: ART 409 ⟵ “ART 409 - European Art, 1848-1900”
  - courses: ART 410 ⟵ “ART 410 - European Art, 1900-1945”
  - courses: ART 445 ⟵ “ART 445 - American Architectural History”
  - courses: ART 494 ⟵ “ART 494 - Seminar in Art History”
### `1ad1ee9763b0404f` Western Kentucky University — degree_requirements 2026-27 · program_key=music-liberal-arts-bachelor-of-arts · requirement_key=requirements-for-both-concentrations-music-theory-and-literature [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-liberal-arts-ba/ (sha256 387a2e064bcb)
- issues: requirement_groups_skipped
  - courses: MUS 100 ⟵ “MUS 100 - Theory I”
  - courses: MUS 101 ⟵ “MUS 101 - Theory II”
  - courses: MUS 200 ⟵ “MUS 200 - Theory III”
  - courses: MUS 201 ⟵ “MUS 201 - Theory IV”
  - courses: MUS 110 ⟵ “MUS 110 - Aural Theory I”
  - courses: MUS 111 ⟵ “MUS 111 - Aural Theory II”
  - courses: MUS 210 ⟵ “MUS 210 - Aural Theory III”
  - courses: MUS 211 ⟵ “MUS 211 - Aural Theory IV”
  - courses: MUS 326 ⟵ “MUS 326 - The History of Music I”
  - courses: MUS 327 ⟵ “MUS 327 - The History of Music II”
### `1c0dfcf0b0469494` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=theatre-concentration-acting-and-directing-10-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: PERF 205 ⟵ “PERF 205 - Voice and Movement for the Stage”
  - courses: THEA 300 ⟵ “THEA 300 - Acting II”
  - courses: THEA 301 ⟵ “THEA 301 - Acting III”
  - courses: THEA 371 ⟵ “THEA 371 - Directing I”
### `1ca86df1162e351a` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-the-music-education-concentration-all-tracks-integrated-vocal-i-6 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 214 ⟵ “MUS 214 - String Techniques”
  - courses: MUS 312 ⟵ “MUS 312 - Teaching Music in the Primary Grades”
  - courses: MUS 412 ⟵ “MUS 412 - Teaching Music in the Middle School”
### `23e22bac7a8b9e18` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=professional-education-requirements [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: EDU 250 ⟵ “EDU 250 - Discover Teaching: Introduction to Teacher Education”
  - courses: PSY 310 ⟵ “PSY 310 - Educational Psychology: Development and Learning”
  - courses: EDU 350 ⟵ “EDU 350 - Student Diversity and Differentiation”
  - courses: EDU 360 ⟵ “EDU 360 - Behavior and Classroom Management in Education”
  - courses: LTCY 497 ⟵ “LTCY 497 - Literacy Competencies for Middle and High School Classroom Teachers”
  - courses: EDU 489 ⟵ “EDU 489 - Student Teaching Seminar”
  - courses: ELED 490 ⟵ “ELED 490 - Student Teaching”
### `269330fa037d634d` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-for-health-sciences-and-health-care-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
- issues: course_alternatives_in_rule_text
  - courses: SPAN 345 ⟵ “SPAN 345 - Topics in Spanish”
  - courses: SPAN 470 ⟵ “SPAN 470 - Advanced Oral Spanish”
  - courses: SPAN 389 ⟵ “SPAN 389 - Internship in Spanish”
  - courses: SPAN 331 ⟵ “SPAN 331 - Spanish for Professional Communication”
  - courses: SPAN 455 ⟵ “SPAN 455 - Topics in Hispanic Literary and Cultural Studies”
  - courses: SPAN 480 ⟵ “SPAN 480 - Translation and Interpreting”
### `2833f2f905c2c504` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=students-may-complete-more-than-one-concentration-however-a-single-elective-cann-2 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 302 ⟵ “HIST 302 - Disability in the United States”
  - courses: HIST 304 ⟵ “HIST 304 - Ancient Identities”
  - courses: HIST 309 ⟵ “HIST 309 - History of HIV/AIDS”
  - courses: HIST 310 ⟵ “HIST 310 - Comparative Slavery”
  - courses: HIST 320 ⟵ “HIST 320 - American Studies I”
  - courses: HIST 325 ⟵ “HIST 325 - Blacks in the Civil War and Reconstruction”
  - courses: HIST 329 ⟵ “HIST 329 - Black Intellectual History”
  - courses: HIST 330 ⟵ “HIST 330 - History of Africa Before 1500”
  - courses: HIST 331 ⟵ “HIST 331 - History of Africa Since 1500”
  - courses: HIST 332 ⟵ “HIST 332 - Riots, Rebellions, and Revolutions: A Global History of Protest”
  - courses: HIST 333 ⟵ “HIST 333 - History of Genocide”
  - courses: HIST 342 ⟵ “HIST 342 - Hip Hop and Democracy”
  - courses: HIST 343 ⟵ “HIST 343 - Communities of Struggle”
  - courses: HIST 344 ⟵ “HIST 344 - Latinos in US History”
  - courses: HIST 353 ⟵ “HIST 353 - Native American History to 1865”
  - courses: HIST 354 ⟵ “HIST 354 - Native American History Since 1865”
  - courses: HIST 355 ⟵ “HIST 355 - Indigenous Legal History”
  - courses: HIST 358 ⟵ “HIST 358 - Blacks in American History to 1877”
  - courses: HIST 359 ⟵ “HIST 359 - Blacks in American History Since 1877”
  - courses: HIST 363 ⟵ “HIST 363 - American Judaism”
  - courses: HIST 389 ⟵ “HIST 389 - Appalachian History”
  - courses: HIST 390 ⟵ “HIST 390 - Blacks in the American South”
  - courses: HIST 420 ⟵ “HIST 420 - History of Sexuality”
  - courses: HIST 430 ⟵ “HIST 430 - History of the Civil Rights Movement in America”
  - courses: HIST 453 ⟵ “HIST 453 - American Women’s History”
  - … 1 more rows
### `2b6f4cc542050259` Western Kentucky University — degree_requirements 2026-27 · program_key=professional-legal-studies-bachelor-of-arts · requirement_key=program-requirements-42-hours-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/paralegal-studies-ba/ (sha256 9c6c23742c44)
- issues: course_alternatives_in_rule_text
  - courses: PLS 225 ⟵ “PLS 225 - Introduction to Law”
  - courses: PLS 200 ⟵ “PLS 200 - Legal Ethics”
  - courses: PLS 250 ⟵ “PLS 250 - Legal Research and Writing I”
  - courses: PLS 283 ⟵ “PLS 283 - Property Law”
  - courses: PLS 291 ⟵ “PLS 291 - Criminal Law and Procedure”
  - courses: PLS 296 ⟵ “PLS 296 - Family Law”
  - courses: PS 326 ⟵ “PS 326 - Constitutional Law”
  - courses: PLS 393 ⟵ “PLS 393 - Civil Procedure”
  - courses: PLS 450 ⟵ “PLS 450 - Legal Research and Writing II”
  - courses: PLS 499 ⟵ “PLS 499 - Internship in Paralegal Studies”
### `2e74926f1f942fd7` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-applied-music [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 153 ⟵ “MUS 153 - Applied Music Principal (4 semesters)”
  - courses: MUS 357 ⟵ “MUS 357 - Applied Music Major (2 semesters)”
  - courses: MUS 338 ⟵ “MUS 338 - DIR Independent Study (Junior Recital)”
  - courses: MUS 457 ⟵ “MUS 457 - Applied Music Major (2 semesters)”
  - courses: MUS 338 ⟵ “MUS 338 - DIR Independent Study (Senior Recital)”
### `2f3669677bad969e` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=animation-concentration-animation-concentration-focus [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ANIM 210 ⟵ “ANIM 210 - Introduction to Computer Animation”
  - courses: ANIM 215 ⟵ “ANIM 215 - 2D Computer Animation”
  - courses: ANIM 220 ⟵ “ANIM 220 - 3D Modeling I: Environment”
  - courses: ANIM 310 ⟵ “ANIM 310 - Computer Animation I”
  - courses: ANIM 320 ⟵ “ANIM 320 - 3D Modeling II: Character Design and Development”
  - courses: ANIM 330 ⟵ “ANIM 330 - Sound and Image”
  - courses: ANIM 344 ⟵ “ANIM 344 - Computer Animation II”
  - courses: ANIM 444 ⟵ “ANIM 444 - Computer Animation III”
  - courses: ART 497 ⟵ “ART 497 - Special Topics in Animation”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 341 ⟵ “ART 341 - Drawing”
  - courses: ART 431 ⟵ “ART 431 - Illustration”
  - courses: ART 440 ⟵ “ART 440 - Drawing”
  - courses: ART 436 ⟵ “ART 436 - Digital Illustration”
  - courses: ART 497 ⟵ “ART 497 - Special Topics in Animation”
  - courses: FILM 100 ⟵ “FILM 100 - Film Industry and Aesthetics”
  - courses: GAME 302 ⟵ “GAME 302 - Game Design and Development”
  - courses: GAME 400 ⟵ “GAME 400 - Game Design & Development Capstone”
  - courses: UX 330 ⟵ “UX 330 - User Interface Design”
  - courses: UX 340 ⟵ “UX 340 - Introduction to Developing and Prototyping for Interactive Design”
  - courses: ART 434 ⟵ “ART 434 - Capstone Seminar”
  - courses: ART 305 ⟵ “ART 305 - Ancient Greek and Roman Art”
  - courses: ART 312 ⟵ “ART 312 - Art of the United States to 1865”
  - courses: ART 313 ⟵ “ART 313 - Art of the United States Since 1865”
  - courses: ART 314 ⟵ “ART 314 - Southern Baroque Art”
  - … 15 more rows
### `3185f293b4f12c5e` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-instrument-2 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 162 ⟵ “MUS 162 - Group Voice”
### `31887e13525e4fc8` Western Kentucky University — degree_requirements 2026-27 · program_key=broadcasting-bachelor-of-arts-726p-726 · requirement_key=program-requirements-46-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/broadcasting-ba/ (sha256 170d38970f13)
- issues: course_alternatives_in_rule_text
  - courses: SMC 101 ⟵ “SMC 101 - Understanding Media Content, Ethics and Technology”
  - courses: SMC 102 ⟵ “SMC 102 - Media Content, Collaboration and Community”
  - courses: BCOM 261 ⟵ “BCOM 261 - Basic Radio/Podcast Production”
  - courses: BCOM 266 ⟵ “BCOM 266 - Basic Television Production”
  - courses: SMC 301 ⟵ “SMC 301 - Mass Communication Law and Ethics”
  - courses: BCOM 326 ⟵ “BCOM 326 - Radio and Television News Performance”
  - courses: BCOM 335 ⟵ “BCOM 335 - News Discovery and Selection”
  - courses: BCOM 366 ⟵ “BCOM 366 - Editing I”
  - courses: BCOM 367 ⟵ “BCOM 367 - Field Production”
  - courses: BCOM 265 ⟵ “BCOM 265 - Basic Broadcast News”
  - courses: SMC 310 ⟵ “SMC 310 - Media Representation”
  - courses: AFAM 343 ⟵ “AFAM 343 - Communities of Struggle”
  - courses: ASL 302 ⟵ “ASL 302 - Deaf Culture in America”
  - courses: COMM 363 ⟵ “COMM 363 - Interracial Communication”
  - courses: COMM 365 ⟵ “COMM 365 - Intercultural Communication”
  - courses: COMM 371 ⟵ “COMM 371 - Communication in Multinational Organizations”
  - courses: CRIM 361 ⟵ “CRIM 361 - Race, Class, and Crime”
  - courses: CRIM 446 ⟵ “CRIM 446 - Gender, Crime, and Justice”
  - courses: FLK 330 ⟵ “FLK 330 - Cultural Connections and Diversity”
  - courses: FLK 373 ⟵ “FLK 373 - Folklore and the Media”
  - courses: GWS 375 ⟵ “GWS 375 - American Masculinities”
  - courses: HIST 302 ⟵ “HIST 302 - Disability in the United States”
  - courses: HIST 343 ⟵ “HIST 343 - Communities of Struggle”
  - courses: LEAD 450 ⟵ “LEAD 450 - Leadership in Global Contexts”
  - courses: PH 410 ⟵ “PH 410 - Global Perspectives on Population Health”
  - … 15 more rows
### `3196d4b78fa212b8` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=ux-design-concentration-beginning-level-studio-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ANIM 210 ⟵ “ANIM 210 - Introduction to Computer Animation”
  - courses: ART 220 ⟵ “ART 220 - Ceramics”
  - courses: ART 231 ⟵ “ART 231 - Graphic Design I: Typography”
  - courses: ART 250 ⟵ “ART 250 - Printmaking”
  - courses: ART 260 ⟵ “ART 260 - Painting”
  - courses: ART 270 ⟵ “ART 270 - Sculpture Survey I”
  - courses: ART 280 ⟵ “ART 280 - Weaving”
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: ART 240 ⟵ “ART 240 - Drawing Foundations II”
  - courses: ART 436 ⟵ “ART 436 - Digital Illustration”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 321 ⟵ “ART 321 - Ceramics”
  - courses: ART 420 ⟵ “ART 420 - Ceramics”
  - courses: ART 421 ⟵ “ART 421 - Ceramics”
  - courses: ART 422 ⟵ “ART 422 - Ceramics”
  - courses: ART 423 ⟵ “ART 423 - Pottery Wheel Techniques”
  - courses: ART 424 ⟵ “ART 424 - Ceramic Glaze Composition”
  - courses: ART 425 ⟵ “ART 425 - Ceramic Studio Equipment Design”
  - courses: ART 426 ⟵ “ART 426 - Special Firing Techniques”
  - courses: ART 330 ⟵ “ART 330 - Graphic Design II: Layout & Information Design”
  - courses: ART 430 ⟵ “ART 430 - Graphic Design III: Advanced Graphic Design”
  - courses: ART 433 ⟵ “ART 433 - Package Design”
  - courses: DES 438 ⟵ “DES 438 - Advanced Media Design”
  - courses: ART 341 ⟵ “ART 341 - Drawing”
  - courses: ART 440 ⟵ “ART 440 - Drawing”
  - … 15 more rows
### `32f8c8b320cfa8cb` Western Kentucky University — degree_requirements 2026-27 · program_key=integrated-advertising-public-relations-bachelor-of-arts-753p-753 · requirement_key=program-requirements-39-hours-required-courses-both-concentrations [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/integrated-advertising-pr-ba/ (sha256 894e3bc19fa7)
- issues: course_alternatives_in_rule_text
  - courses: SMC 101 ⟵ “SMC 101 - Understanding Media Content, Ethics and Technology”
  - courses: ADPR 200 ⟵ “ADPR 200 - Introduction to Integrated Advertising & Public Relations”
  - courses: ADPR 230 ⟵ “ADPR 230 - Digital Tools in Advertising & Public Relations”
  - courses: SMC 301 ⟵ “SMC 301 - Mass Communication Law and Ethics”
  - courses: ADPR 321 ⟵ “ADPR 321 - Analytics in Advertising & Public Relations”
  - courses: ADPR 494 ⟵ “ADPR 494 - Integrated Advertising & Public Relations Campaigns”
  - courses: SMC 310 ⟵ “SMC 310 - Media Representation”
### `34235de9b010f13b` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=major-in-spanish-with-teacher-certification-no-minor-or-second-major-required [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
- issues: course_alternatives_in_rule_text
  - courses: SPAN 470 ⟵ “SPAN 470 - Advanced Oral Spanish”
  - courses: EDU 250 ⟵ “EDU 250 - Discover Teaching: Introduction to Teacher Education”
  - courses: EDU 260 ⟵ “EDU 260 - Classroom Assessment”
  - courses: PSY 310 ⟵ “PSY 310 - Educational Psychology: Development and Learning”
  - courses: EDU 350 ⟵ “EDU 350 - Student Diversity and Differentiation”
  - courses: EDU 360 ⟵ “EDU 360 - Behavior and Classroom Management in Education”
  - courses: LTCY 497 ⟵ “LTCY 497 - Literacy Competencies for Middle and High School Classroom Teachers”
  - courses: MLNG 410 ⟵ “MLNG 410 - Second Language Acquisition”
  - courses: MLNG 474 ⟵ “MLNG 474 - Teaching Foreign Language”
  - courses: SEC 350 ⟵ “SEC 350 - Clinical Practices in Secondary Teaching I”
  - courses: SEC 450 ⟵ “SEC 450 - Clinical Practices in Secondary Teaching II”
  - courses: SEC 475 ⟵ “SEC 475 - Teaching Language Arts”
  - courses: EDU 489 ⟵ “EDU 489 - Student Teaching Seminar”
  - courses: SEC 490 ⟵ “SEC 490 - Student Teaching”
### `3610b746fab1c307` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-beginning-level-studio-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ANIM 210 ⟵ “ANIM 210 - Introduction to Computer Animation”
  - courses: ART 220 ⟵ “ART 220 - Ceramics”
  - courses: ART 231 ⟵ “ART 231 - Graphic Design I: Typography”
  - courses: ART 250 ⟵ “ART 250 - Printmaking”
  - courses: ART 260 ⟵ “ART 260 - Painting”
  - courses: ART 270 ⟵ “ART 270 - Sculpture Survey I”
  - courses: ART 280 ⟵ “ART 280 - Weaving”
  - courses: ART 240 ⟵ “ART 240 - Drawing Foundations II”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 341 ⟵ “ART 341 - Drawing”
### `3898ac381a51e55d` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-final-semester [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 432 ⟵ “ART 432 - Portfolio”
  - courses: ART 434 ⟵ “ART 434 - Capstone Seminar”
### `39f43f05566980e0` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-printmaking-practices [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 350 ⟵ “ART 350 - Printmaking”
  - courses: ART 351 ⟵ “ART 351 - Printmaking”
  - courses: ART 450 ⟵ “ART 450 - Printmaking”
  - courses: ART 451 ⟵ “ART 451 - Printmaking”
  - courses: ART 452 ⟵ “ART 452 - Printmaking”
  - courses: ART 453 ⟵ “ART 453 - Senior Techniques in Printmaking”
  - courses: ART 454 ⟵ “ART 454 - Senior Composition in Printmaking”
  - courses: ART 455 ⟵ “ART 455 - Advanced Senior Techniques in Printmaking”
  - courses: ART 456 ⟵ “ART 456 - Advanced Senior Composition in Printmaking”
### `3b00576dc0f6bc46` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=students-may-complete-more-than-one-concentration-however-a-single-elective-cann-6 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 302 ⟵ “HIST 302 - Disability in the United States”
  - courses: HIST 303 ⟵ “HIST 303 - Monsters, Maggots, and Morphine: Disease and Medicine in the United States”
  - courses: HIST 309 ⟵ “HIST 309 - History of HIV/AIDS”
  - courses: HIST 322 ⟵ “HIST 322 - Age of Enlightenment”
  - courses: HIST 332 ⟵ “HIST 332 - Riots, Rebellions, and Revolutions: A Global History of Protest”
  - courses: HIST 362 ⟵ “HIST 362 - Genetics and Family History”
  - courses: HIST 375 ⟵ “HIST 375 - Spatial History”
  - courses: HIST 378 ⟵ “HIST 378 - History of Yoga: Tradition, Literature, Practice”
  - courses: HIST 420 ⟵ “HIST 420 - History of Sexuality”
  - courses: HIST 421 ⟵ “HIST 421 - Environmental History”
  - courses: HIST 480 ⟵ “HIST 480 - A Social History of Science”
### `3cab6fa81bead7bd` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-history-literature-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: THEA 430 ⟵ “THEA 430 - Musical Theatre History”
  - courses: THEA 431 ⟵ “THEA 431 - Musical Theatre Repertoire”
### `40bbe081d906c0bf` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=program-requirements-36-78-hours-required-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
- issues: course_alternatives_in_rule_text
  - courses: SPAN 102 ⟵ “SPAN 102 - Elementary Spanish II (or equivalent)”
  - courses: SPAN 201 ⟵ “SPAN 201 - Intermediate Spanish I”
  - courses: SPAN 202 ⟵ “SPAN 202 - Intermediate Spanish II”
  - courses: SPAN 370 ⟵ “SPAN 370 - Spanish Conversation”
  - courses: SPAN 371 ⟵ “SPAN 371 - Spanish Composition and Grammar”
  - courses: SPAN 372 ⟵ “SPAN 372 - Latin American Civilization and Culture”
  - courses: SPAN 374 ⟵ “SPAN 374 - Literature and Culture of Spain”
### `41c62eff88277b7a` Western Kentucky University — degree_requirements 2026-27 · program_key=integrated-advertising-public-relations-bachelor-of-arts-753p-753 · requirement_key=advertising-concentration-required-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/integrated-advertising-pr-ba/ (sha256 894e3bc19fa7)
- issues: course_alternatives_in_rule_text
  - courses: MKT 220 ⟵ “MKT 220 - Basic Marketing Concepts”
  - courses: AD 330 ⟵ “AD 330 - Branding”
  - courses: AD 349 ⟵ “AD 349 - Advertising Media”
  - courses: AD 400 ⟵ “AD 400 - Special Topics Advertising”
  - courses: AD 415 ⟵ “AD 415 - Study Abroad in Advertising”
  - courses: AD 489 ⟵ “AD 489 - AD Internship or Practicum”
  - courses: AD 495 ⟵ “AD 495 - Independent Study in Advertising”
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: ART 399 ⟵ “ART 399 - Professional Work”
  - courses: ART 499 ⟵ “ART 499 - Career Experience in Art”
  - courses: BCOM 264 ⟵ “BCOM 264 - Digital Video Production and Distribution”
  - courses: COMM 346 ⟵ “COMM 346 - Persuasion”
  - courses: ENG 212 ⟵ “ENG 212 - Introduction to Digital Texts and Media”
  - courses: MKT 321 ⟵ “MKT 321 - Consumer Behavior”
  - courses: MKT 322 ⟵ “MKT 322 - Integrated Marketing Communications”
  - courses: MKT 323 ⟵ “MKT 323 - Services Marketing”
  - courses: MKT 324 ⟵ “MKT 324 - International Marketing”
  - courses: MKT 325 ⟵ “MKT 325 - Personal Selling”
  - courses: MKT 326 ⟵ “MKT 326 - Sports Marketing”
  - courses: MKT 327 ⟵ “MKT 327 - Retailing Management and Strategy”
  - courses: MKT 328 ⟵ “MKT 328 - Digital Marketing”
  - courses: MKT 329 ⟵ “MKT 329 - Business-To-Business Marketing”
  - courses: MKT 331 ⟵ “MKT 331 - Social Media Marketing”
  - courses: MKT 427 ⟵ “MKT 427 - Entrepreneurial Marketing”
  - courses: PR 385 ⟵ “PR 385 - Artificial Intelligence in Public Relations”
  - … 8 more rows
### `41fe8b3d7eaba7ef` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=theatre-concentration-advanced-practice-12-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: DANC 310 ⟵ “DANC 310 - Choreography I”
  - courses: PERF 350 ⟵ “PERF 350 - Voice and Diction for the Theatre”
  - courses: PERF 362 ⟵ “PERF 362 - Theatre in Diversion”
  - courses: PERF 369 ⟵ “PERF 369 - Professional Work / Career Experience in Theatre”
  - courses: PERF 400 ⟵ “PERF 400 - Advanced Performing Arts Studio”
  - courses: PERF 423 ⟵ “PERF 423 - Performing Arts Management”
  - courses: PERF 445 ⟵ “PERF 445 - Research in Theatre and Dance”
  - courses: PERF 361 ⟵ “PERF 361 - Performing Arts Practicum II”
  - courses: PERF 461 ⟵ “PERF 461 - Performing Arts Practicum III”
  - courses: THEA 319 ⟵ “THEA 319 - Design II”
  - courses: THEA 322 ⟵ “THEA 322 - Stage Design”
  - courses: THEA 341 ⟵ “THEA 341 - Culture and Performance”
  - courses: THEA 380 ⟵ “THEA 380 - Directing II”
  - courses: THEA 392 ⟵ “THEA 392 - Production of Theatre for Children”
  - courses: THEA 414 ⟵ “THEA 414 - Acting IV”
  - courses: THEA 422 ⟵ “THEA 422 - Stage Lighting Design”
  - courses: THEA 424 ⟵ “THEA 424 - Topics in Design and Technical Theatre”
  - courses: THEA 441 ⟵ “THEA 441 - Costume Design”
### `43f68fd77e64ae22` Western Kentucky University — degree_requirements 2026-27 · program_key=sociology-bachelor-of-arts · requirement_key=core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/sociology-ba/ (sha256 a3ffc4936e95)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: SOCL 100 ⟵ “SOCL 100 - Introductory Sociology”
  - courses: SOCL 199 ⟵ “SOCL 199 - College & Careers in Criminology & Sociology”
  - courses: SOCL 250 ⟵ “SOCL 250 - Systems of Social Inequality”
  - courses: SOCL 300 ⟵ “SOCL 300 - Social Statistics”
  - courses: SOCL 301 ⟵ “SOCL 301 - Social Statistics Lab”
  - courses: SOCL 302 ⟵ “SOCL 302 - Social Research Methods”
  - courses: SOCL 304 ⟵ “SOCL 304 - Sociological Theory: Perspectives on Society”
### `4516c37db2f526c5` Western Kentucky University — degree_requirements 2026-27 · program_key=economics-bachelor-of-arts · requirement_key=program-requirements-35-hours-required-economics-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/economics-ba/ (sha256 1e2e2c84e96a)
- issues: course_alternatives_in_rule_text
  - courses: ECON 202 ⟵ “ECON 202 - Principles of Economics (Micro)”
  - courses: ECON 203 ⟵ “ECON 203 - Principles of Economics (Macro)”
  - courses: ECON 206 ⟵ “ECON 206 - Statistics”
  - courses: ECON 302 ⟵ “ECON 302 - Microeconomic Theory”
  - courses: ECON 303 ⟵ “ECON 303 - Macroeconomic Theory”
  - courses: ECON 306 ⟵ “ECON 306 - Statistical Analysis”
  - courses: ECON 399 ⟵ “ECON 399 - Career Readiness in Economics”
  - courses: ECON 465 ⟵ “ECON 465 - Regression and Econometric Analysis”
  - courses: ECON 499 ⟵ “ECON 499 - Senior Assessment”
### `48bca75ef7b53cea` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-advanced-practice-12-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: THEA 371 ⟵ “THEA 371 - Directing I”
  - courses: THEA 424 ⟵ “THEA 424 - Topics in Design and Technical Theatre”
### `4acab533881e2e29` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-instrument-3 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 215 ⟵ “MUS 215 - Brass Techniques”
  - courses: MUS 315 ⟵ “MUS 315 - Clarinet and Saxophone Techniques”
  - courses: MUS 316 ⟵ “MUS 316 - Flute and Double Reed Techniques”
  - courses: MUS 319 ⟵ “MUS 319 - Percussion Techniques”
  - courses: MUS 416 ⟵ “MUS 416 - Instrumental Methods”
  - courses: MUS 417 ⟵ “MUS 417 - Marching Band Techniques”
### `4ae26cdbb75e1e24` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=note-students-in-the-public-history-concentration-are-encouraged-to-take-advanta [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 318 ⟵ “HIST 318 - Age of the Reformation”
  - courses: HIST 339 ⟵ “HIST 339 - The Holocaust”
  - courses: HIST 363 ⟵ “HIST 363 - American Judaism”
  - courses: HIST 378 ⟵ “HIST 378 - History of Yoga: Tradition, Literature, Practice”
  - courses: HIST 379 ⟵ “HIST 379 - Gandhi: The Creation of a Global Legacy”
  - courses: HIST 407 ⟵ “HIST 407 - The Crusades: West Meets East”
  - courses: HIST 433 ⟵ “HIST 433 - Antisemitism in World History”
  - courses: HIST 454 ⟵ “HIST 454 - History of Religion in America”
  - courses: HIST 466 ⟵ “HIST 466 - The Arab-Israeli Conflict: Local and Global Influences”
  - courses: RELS 211 ⟵ “RELS 211 - Jesus in Film”
  - courses: RELS 222 ⟵ “RELS 222 - Christians, Jews, and Pagans in the Greco-Roman World”
  - courses: RELS 300 ⟵ “RELS 300 - The Life of Jesus”
  - courses: RELS 302 ⟵ “RELS 302 - Buddhism”
  - courses: RELS 304 ⟵ “RELS 304 - Judaism”
  - courses: RELS 305 ⟵ “RELS 305 - Christianity”
  - courses: RELS 306 ⟵ “RELS 306 - Islam”
  - courses: RELS 309 ⟵ “RELS 309 - Global Christianity”
  - courses: RELS 314 ⟵ “RELS 314 - The Making of the Bible”
  - courses: RELS 317 ⟵ “RELS 317 - Confucianism”
  - courses: RELS 318 ⟵ “RELS 318 - Daoism”
  - courses: RELS 319 ⟵ “RELS 319 - Religions of Asia”
  - courses: RELS 322 ⟵ “RELS 322 - Pilgrimage, Islam and Modernity”
  - courses: RELS 331 ⟵ “RELS 331 - Islam in America: Hope & Hip Hop”
  - courses: RELS 333 ⟵ “RELS 333 - Women and Religion”
  - courses: RELS 335 ⟵ “RELS 335 - Islam, Sexuality, and Gender”
  - … 3 more rows
### `4baf997cbf22b35a` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-pedagogy [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 310 ⟵ “MUS 310 - Pedagogy for Performance Majors”
### `4ca639316ebda304` Western Kentucky University — degree_requirements 2026-27 · program_key=dance-bachelor-of-arts-630p-630 · requirement_key=program-requirements-46-hours-dance-study-9-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/dance-ba/ (sha256 f4f5bd40773f)
- issues: requirement_groups_skipped
  - courses: DANC 301 ⟵ “DANC 301 - Dance Pedagogy”
  - courses: DANC 350 ⟵ “DANC 350 - Dance History”
  - courses: DANC 445 ⟵ “DANC 445 - Dance Anatomy and Kinesiology”
### `4d03a5d1876223ba` Western Kentucky University — degree_requirements 2026-27 · program_key=film-bachelor-of-arts-667p-667 · requirement_key=program-requirements-36-hours-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/film-ba/ (sha256 d1378fd4bf29)
- issues: course_alternatives_in_rule_text
  - courses: FILM 100 ⟵ “FILM 100 - Film Industry and Aesthetics”
  - courses: FILM 155 ⟵ “FILM 155 - Film Attendance (Must be completed twice)”
  - courses: FILM 201 ⟵ “FILM 201 - Introduction to the Cinema”
  - courses: FILM 202 ⟵ “FILM 202 - Basic Film Production”
  - courses: FILM 250 ⟵ “FILM 250 - Screenwriting I”
  - courses: FILM 256 ⟵ “FILM 256 - Film Editing I”
  - courses: FILM 282 ⟵ “FILM 282 - Film Production Workshop I”
  - courses: FILM 369 ⟵ “FILM 369 - Introduction to World Cinema”
### `4e06d7adedbf8510` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=students-may-complete-more-than-one-concentration-however-a-single-elective-cann-5 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 304 ⟵ “HIST 304 - Ancient Identities”
  - courses: HIST 310 ⟵ “HIST 310 - Comparative Slavery”
  - courses: HIST 325 ⟵ “HIST 325 - Blacks in the Civil War and Reconstruction”
  - courses: HIST 329 ⟵ “HIST 329 - Black Intellectual History”
  - courses: HIST 330 ⟵ “HIST 330 - History of Africa Before 1500”
  - courses: HIST 331 ⟵ “HIST 331 - History of Africa Since 1500”
  - courses: HIST 332 ⟵ “HIST 332 - Riots, Rebellions, and Revolutions: A Global History of Protest”
  - courses: HIST 343 ⟵ “HIST 343 - Communities of Struggle”
  - courses: HIST 342 ⟵ “HIST 342 - Hip Hop and Democracy”
  - courses: HIST 358 ⟵ “HIST 358 - Blacks in American History to 1877”
  - courses: HIST 359 ⟵ “HIST 359 - Blacks in American History Since 1877”
  - courses: HIST 390 ⟵ “HIST 390 - Blacks in the American South”
  - courses: HIST 404 ⟵ “HIST 404 - History of Ancient Egypt”
### `5234a16499002679` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=ux-design-concentration-final-semester [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 434 ⟵ “ART 434 - Capstone Seminar”
  - courses: UX 300 ⟵ “UX 300 - User Experience Strategy & Content Creation”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 377 ⟵ “ART 377 - Design to Prototype I”
  - courses: ART 399 ⟵ “ART 399 - Professional Work”
  - courses: ART 431 ⟵ “ART 431 - Illustration”
  - courses: ART 432 ⟵ “ART 432 - Portfolio”
  - courses: ART 499 ⟵ “ART 499 - Career Experience in Art”
  - courses: DES 498 ⟵ “DES 498 - Special Topics in Graphic Design”
  - courses: PSYS 333 ⟵ “PSYS 333 - Cognitive Psychology”
  - courses: PSYS 350 ⟵ “PSYS 350 - Social Psychology”
  - courses: PSYS 363 ⟵ “PSYS 363 - Sensory and Perceptual Systems”
  - courses: PSYS 433 ⟵ “PSYS 433 - Judgment and Decision Making”
### `52f3daa4b7608348` Western Kentucky University — degree_requirements 2026-27 · program_key=asian-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-senior-seminar-3-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/asian-studies-ba/ (sha256 d4bf15768a8d)
- issues: requirement_groups_skipped
  - courses: RELS 496 ⟵ “RELS 496 - Senior Seminar”
  - courses: HIST 498 ⟵ “HIST 498 - Senior Seminar”
  - courses: HON 404 ⟵ “HON 404 - Honors Thesis / Project II”
### `550d377f55d166f6` Western Kentucky University — degree_requirements 2026-27 · program_key=business-economics-bachelor-of-science · requirement_key=program-requirements-72-hours-business-foundations-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/business-economics-bs/ (sha256 367d4d265754)
- issues: course_alternatives_in_rule_text
  - courses: MATH 123 ⟵ “MATH 123 - Mathematical Applications for Business *”
  - courses: ACCT 110 ⟵ “ACCT 110 - Accounting for Decision Makers”
  - courses: ECON 202 ⟵ “ECON 202 - Principles of Economics (Micro)”
  - courses: ECON 206 ⟵ “ECON 206 - Statistics”
  - courses: MGT 210 ⟵ “MGT 210 - Organization and Management”
  - courses: MKT 220 ⟵ “MKT 220 - Basic Marketing Concepts”
  - courses: BDAN 250 ⟵ “BDAN 250 - Introduction to Analytics”
  - courses: FIN 330 ⟵ “FIN 330 - Principles of Finance”
  - courses: MGT 498 ⟵ “MGT 498 - Strategy and Policy”
### `55b7d1b331952ad4` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-group-piano [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 160 ⟵ “MUS 160 - Group Piano I 2”
  - courses: MUS 161 ⟵ “MUS 161 - Group Piano II 2”
  - courses: MUS 260 ⟵ “MUS 260 - Group Piano III 2”
  - courses: MUS 261 ⟵ “MUS 261 - Group Piano IV 2”
### `574efed4b7de0f7c` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=graphic-design-concentration-beginning-level-studio-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ANIM 210 ⟵ “ANIM 210 - Introduction to Computer Animation”
  - courses: ART 220 ⟵ “ART 220 - Ceramics”
  - courses: ART 250 ⟵ “ART 250 - Printmaking”
  - courses: ART 260 ⟵ “ART 260 - Painting”
  - courses: ART 270 ⟵ “ART 270 - Sculpture Survey I”
  - courses: ART 280 ⟵ “ART 280 - Weaving”
  - courses: UX 300 ⟵ “UX 300 - User Experience Strategy & Content Creation”
  - courses: ART 240 ⟵ “ART 240 - Drawing Foundations II”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 431 ⟵ “ART 431 - Illustration”
  - courses: ART 321 ⟵ “ART 321 - Ceramics”
  - courses: ART 420 ⟵ “ART 420 - Ceramics”
  - courses: ART 421 ⟵ “ART 421 - Ceramics”
  - courses: ART 422 ⟵ “ART 422 - Ceramics”
  - courses: ART 423 ⟵ “ART 423 - Pottery Wheel Techniques”
  - courses: ART 424 ⟵ “ART 424 - Ceramic Glaze Composition”
  - courses: ART 425 ⟵ “ART 425 - Ceramic Studio Equipment Design”
  - courses: ART 426 ⟵ “ART 426 - Special Firing Techniques”
  - courses: ART 341 ⟵ “ART 341 - Drawing”
  - courses: ART 440 ⟵ “ART 440 - Drawing”
  - courses: ART 350 ⟵ “ART 350 - Printmaking”
  - courses: ART 351 ⟵ “ART 351 - Printmaking”
  - courses: ART 450 ⟵ “ART 450 - Printmaking”
  - courses: ART 451 ⟵ “ART 451 - Printmaking”
  - courses: ART 452 ⟵ “ART 452 - Printmaking”
  - … 15 more rows
### `58bda50892c18026` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=major-in-chinese-with-teacher-certification-required-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
- issues: course_alternatives_in_rule_text
  - courses: CHIN 102 ⟵ “CHIN 102 - Elementary Chinese II”
  - courses: CHIN 201 ⟵ “CHIN 201 - Intermediate Chinese I”
  - courses: CHIN 202 ⟵ “CHIN 202 - Intermediate Chinese II”
  - courses: CHIN 301 ⟵ “CHIN 301 - Advanced Intermediate Chinese I”
  - courses: CHIN 302 ⟵ “CHIN 302 - Advanced Intermediate Chinese II (required for students not taking CHNF courses)”
  - courses: CHIN 333 ⟵ “CHIN 333 - Chinese Culture and Civilization”
  - courses: CHIN 401 ⟵ “CHIN 401 - Advanced Chinese I”
  - courses: CHIN 402 ⟵ “CHIN 402 - Advanced Chinese II”
### `59dd7d530b6fe0a0` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=theatre-concentration-youth-theatre-3-hours-1 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 325 ⟵ “THEA 325 - Theatre in Education”
### `5deef16954a1daee` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=theatre-concentration-history-literature-9-hours-1 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 363 ⟵ “THEA 363 - World Theatre History I”
  - courses: THEA 375 ⟵ “THEA 375 - Topics in Drama (may be repeated up to three times)”
### `60706838e92d6220` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-communication-concentration-workplace-communication [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
- issues: course_alternatives_in_rule_text
  - courses: COMM 330 ⟵ “COMM 330 - Leadership Communication”
  - courses: COMM 349 ⟵ “COMM 349 - Small Group Communication”
  - courses: COMM 365 ⟵ “COMM 365 - Intercultural Communication”
### `65653eed6cbbbe1a` Western Kentucky University — degree_requirements 2026-27 · program_key=sociology-bachelor-of-arts · requirement_key=core-courses-socl-4 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/sociology-ba/ (sha256 a3ffc4936e95)
- issues: requirement_groups_skipped
  - courses: ANTH 120 ⟵ “ANTH 120 - Introduction to Cultural Anthropology”
  - courses: ANTH 399 ⟵ “ANTH 399 - Field Methods in Ethnography”
  - courses: FLK 280 ⟵ “FLK 280 - Cultural Diversity in the U S”
  - courses: PS 311 ⟵ “PS 311 - Public Policy”
### `6c10c442bde8c9cf` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=students-may-complete-more-than-one-concentration-however-a-single-elective-cann-7 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 312 ⟵ “HIST 312 - Public History”
  - courses: HIST 314 ⟵ “HIST 314 - Guided Internship”
  - courses: HIST 311 ⟵ “HIST 311 - History Teaching Methods”
  - courses: HIST 362 ⟵ “HIST 362 - Genetics and Family History”
  - courses: HIST 375 ⟵ “HIST 375 - Spatial History”
  - courses: HIST 388 ⟵ “HIST 388 - Histories of Things”
  - courses: FLK 430 ⟵ “FLK 430 - Oral History”
  - courses: FLK 470 ⟵ “FLK 470 - Museum Procedures and Preservation Techniques”
### `6de29f640e5cbb14` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=acting-concentration-acting-and-performance-21-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PERF 205 ⟵ “PERF 205 - Voice and Movement for the Stage”
  - courses: THEA 141 ⟵ “THEA 141 - Stage Makeup”
  - courses: THEA 300 ⟵ “THEA 300 - Acting II”
  - courses: THEA 301 ⟵ “THEA 301 - Acting III”
  - courses: THEA 414 ⟵ “THEA 414 - Acting IV”
  - courses: THEA 371 ⟵ “THEA 371 - Directing I”
  - courses: PERF 401 ⟵ “PERF 401 - Solo Performance”
  - courses: PERF 350 ⟵ “PERF 350 - Voice and Diction for the Theatre”
  - courses: THEA 412 ⟵ “THEA 412 - Special Topics in Acting”
### `6fb370aef6e163a6` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-production-5-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PERF 321 ⟵ “PERF 321 - Production Lab III”
  - courses: PERF 420 ⟵ “PERF 420 - Production Lab IV”
  - courses: PERF 421 ⟵ “PERF 421 - Production Lab V”
  - courses: PERF 430 ⟵ “PERF 430 - Production Lab VI”
  - courses: PERF 431 ⟵ “PERF 431 - Production Lab VII”
### `6ff5cd8d452e10f8` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=theatre-concentration-devising-performance-3-hours-1 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PERF 300 ⟵ “PERF 300 - Topics in Contemporary Performance Studies”
### `707aba18679edecc` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-integrated-2 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MUS 152 ⟵ “MUS 152 - Diction I for Voice Majors”
### `73a4253c99d136f1` Western Kentucky University — degree_requirements 2026-27 · program_key=mathematical-economics-bachelor-of-science · requirement_key=general-mathematical-economics-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/mathematical-economics-bs/ (sha256 195ac45cd091)
- issues: course_alternatives_in_rule_text
  - courses: ECON 306 ⟵ “ECON 306 - Statistical Analysis”
  - courses: ECON 464 ⟵ “ECON 464 - Introduction to Mathematical Economics”
  - courses: MATH 331 ⟵ “MATH 331 - Differential Equations”
  - courses: MATH 331 ⟵ “MATH 331 - Differential Equations”
  - courses: MATH 310 ⟵ “MATH 310 - Introduction to Discrete Mathematics”
  - courses: MATH 305 ⟵ “MATH 305 - Introduction to Mathematical Modeling”
  - courses: MATH 382 ⟵ “MATH 382 - Probability and Statistics I”
  - courses: MATH 435 ⟵ “MATH 435 - Partial Differential Equations”
  - courses: MATH 405 ⟵ “MATH 405 - Numerical Analysis”
  - courses: ECON 399 ⟵ “ECON 399 - Career Readiness in Economics”
### `77a8a082730f8b00` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=students-may-complete-more-than-one-concentration-however-a-single-elective-cann [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 308 ⟵ “HIST 308 - Conflict, Culture and Commerce in the Medieval Mediterranean”
  - courses: HIST 316 ⟵ “HIST 316 - The US Civil War in Popular Culture”
  - courses: HIST 317 ⟵ “HIST 317 - Renaissance Europe”
  - courses: HIST 322 ⟵ “HIST 322 - Age of Enlightenment”
  - courses: HIST 320 ⟵ “HIST 320 - American Studies I”
  - courses: HIST 340 ⟵ “HIST 340 - History of Popular Culture Since 1500”
  - courses: HIST 342 ⟵ “HIST 342 - Hip Hop and Democracy”
  - courses: HIST 347 ⟵ “HIST 347 - Social History of the United States Since 1800”
  - courses: HIST 363 ⟵ “HIST 363 - American Judaism”
  - courses: HIST 378 ⟵ “HIST 378 - History of Yoga: Tradition, Literature, Practice”
  - courses: HIST 379 ⟵ “HIST 379 - Gandhi: The Creation of a Global Legacy”
  - courses: HIST 389 ⟵ “HIST 389 - Appalachian History”
  - courses: HIST 391 ⟵ “HIST 391 - History of Sport”
  - courses: HIST 395 ⟵ “HIST 395 - A Cultural History of Alcohol”
  - courses: HIST 402 ⟵ “HIST 402 - Pirates in World History”
  - courses: HIST 407 ⟵ “HIST 407 - The Crusades: West Meets East”
  - courses: HIST 420 ⟵ “HIST 420 - History of Sexuality”
  - courses: HIST 432 ⟵ “HIST 432 - Coffee & Chocolate: Food in World History”
  - courses: HIST 447 ⟵ “HIST 447 - History of American Popular Culture”
  - courses: HIST 454 ⟵ “HIST 454 - History of Religion in America”
### `79efc7490ac50533` Western Kentucky University — degree_requirements 2026-27 · program_key=international-affairs-bachelor-of-arts · requirement_key=program-requirements-42-hours-any-ia-prefix [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/international-affairs-ba/ (sha256 fa9985d13bc4)
- issues: requirement_groups_skipped
  - courses: PS 301 ⟵ “PS 301 - Using Statistics in Political Science”
  - courses: PS 302 ⟵ “PS 302 - Research Design in Political Science”
### `7a3b5ef3ef44e5de` Western Kentucky University — degree_requirements 2026-27 · program_key=anthropology-bachelor-of-arts · requirement_key=archaeology-concentration-concentration-requirements [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/anthropology-ba/ (sha256 a5bb47ee6548)
- issues: course_alternatives_in_rule_text
  - courses: ANTH 316 ⟵ “ANTH 316 - The Archaeology of Environmental Change”
  - courses: ANTH 432 ⟵ “ANTH 432 - Field Course in Archaeology (at least three hours)”
  - courses: ANTH 438 ⟵ “ANTH 438 - Archaeological Lab Methods”
### `7c0c37bfd745b432` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-integrated [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MUS 405 ⟵ “MUS 405 - Choral Arranging”
### `7d427c55f3755cb9` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=students-may-complete-more-than-one-concentration-however-a-single-elective-cann-4 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 323 ⟵ “HIST 323 - The British Isles to 1688”
  - courses: HIST 332 ⟵ “HIST 332 - Riots, Rebellions, and Revolutions: A Global History of Protest”
  - courses: HIST 333 ⟵ “HIST 333 - History of Genocide”
  - courses: HIST 343 ⟵ “HIST 343 - Communities of Struggle”
  - courses: HIST 353 ⟵ “HIST 353 - Native American History to 1865”
  - courses: HIST 354 ⟵ “HIST 354 - Native American History Since 1865”
  - courses: HIST 355 ⟵ “HIST 355 - Indigenous Legal History”
  - courses: HIST 380 ⟵ “HIST 380 - Human Rights in History”
  - courses: HIST 381 ⟵ “HIST 381 - Topics in Policy History”
  - courses: HIST 382 ⟵ “HIST 382 - History of the Bill of Rights”
  - courses: HIST 383 ⟵ “HIST 383 - Legal Culture in American History”
  - courses: HIST 419 ⟵ “HIST 419 - Tudor-Stuart England”
  - courses: HIST 430 ⟵ “HIST 430 - History of the Civil Rights Movement in America”
  - courses: HIST 441 ⟵ “HIST 441 - The American Revolution and Early Republic, 1763-1815”
  - courses: HIST 445 ⟵ “HIST 445 - American Legal History to 1865”
  - courses: HIST 446 ⟵ “HIST 446 - American Legal History Since 1865”
### `7e531fc208f266da` Western Kentucky University — degree_requirements 2026-27 · program_key=music-liberal-arts-bachelor-of-arts · requirement_key=requirements-for-both-concentrations-conducting [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-liberal-arts-ba/ (sha256 387a2e064bcb)
- issues: requirement_groups_skipped
  - courses: MUS 317 ⟵ “MUS 317 - Conducting I”
### `7e8de23da1536950` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-conducting [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 317 ⟵ “MUS 317 - Conducting I”
### `7eeafbbd9b18b9c3` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-acting-17-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: THEA 141 ⟵ “THEA 141 - Stage Makeup”
  - courses: PERF 205 ⟵ “PERF 205 - Voice and Movement for the Stage”
  - courses: THEA 300 ⟵ “THEA 300 - Acting II”
  - courses: THEA 301 ⟵ “THEA 301 - Acting III”
  - courses: THEA 414 ⟵ “THEA 414 - Acting IV”
  - courses: THEA 307 ⟵ “THEA 307 - Musical Theatre Workshop I”
  - courses: THEA 407 ⟵ “THEA 407 - Musical Theatre Workshop II”
### `7ff482c409a8aa99` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=performing-arts-core-performance-3-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: THEA 101 ⟵ “THEA 101 - Acting I”
### `8374868379d1d247` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-ensembles [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 371 ⟵ “MUS 371 - Jazz Ensemble”
  - courses: MUS 374 ⟵ “MUS 374 - Opera Theatre”
  - courses: MUS 379 ⟵ “MUS 379 - Chamber Music”
### `8383981d47bb4e17` Western Kentucky University — degree_requirements 2026-27 · program_key=dance-bachelor-of-arts-630p-630 · requirement_key=program-requirements-46-hours-dance-production-3-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/dance-ba/ (sha256 f4f5bd40773f)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 250 ⟵ “THEA 250 - Stage Electrics”
### `838ae9f2ab8e38e7` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-art-history-upper-level-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 305 ⟵ “ART 305 - Ancient Greek and Roman Art”
  - courses: ART 312 ⟵ “ART 312 - Art of the United States to 1865”
  - courses: ART 313 ⟵ “ART 313 - Art of the United States Since 1865”
  - courses: ART 314 ⟵ “ART 314 - Southern Baroque Art”
  - courses: ART 315 ⟵ “ART 315 - Northern Baroque Art”
  - courses: ART 316 ⟵ “ART 316 - Medieval Art & Architecture”
  - courses: ART 317 ⟵ “ART 317 - Art and Power”
  - courses: ART 318 ⟵ “ART 318 - Art and Landscape”
  - courses: ART 325 ⟵ “ART 325 - Art of Asia, Africa, and the Americas”
  - courses: ART 334 ⟵ “ART 334 - Survey of Graphic Design”
  - courses: ART 390 ⟵ “ART 390 - Contemporary Art”
  - courses: ART 395 ⟵ “ART 395 - A Cultural History of Alcohol”
  - courses: ART 401 ⟵ “ART 401 - Art of the Italian Renaissance”
  - courses: ART 403 ⟵ “ART 403 - Northern Renaissance Art”
  - courses: ART 405 ⟵ “ART 405 - Art Theory and Criticism”
  - courses: ART 407 ⟵ “ART 407 - Islamic Art and Architecture”
  - courses: ART 408 ⟵ “ART 408 - European Art, 1700-1848”
  - courses: ART 409 ⟵ “ART 409 - European Art, 1848-1900”
  - courses: ART 410 ⟵ “ART 410 - European Art, 1900-1945”
  - courses: ART 445 ⟵ “ART 445 - American Architectural History”
  - courses: ART 494 ⟵ “ART 494 - Seminar in Art History”
### `86ca721b57b6150a` Western Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-science · requirement_key=program-requirements-75-hours-career-preparation-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/accounting/accounting-bs/ (sha256 5dadf9a49ed6)
- issues: course_alternatives_in_rule_text
  - courses: BA 170 ⟵ “BA 170 - Business Student Basics 1”
  - courses: MGT 261 ⟵ “MGT 261 - Business Communication Fundamentals”
  - courses: ACCT 399 ⟵ “ACCT 399 - Career Readiness in Accounting”
  - courses: ACCT 499 ⟵ “ACCT 499 - Senior Assessment in Accounting”
### `8a334b2f7d10fa75` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-the-music-education-concentration-all-tracks-integrated-vocal-i-5 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 317 ⟵ “MUS 317 - Conducting I”
  - courses: MUS 318 ⟵ “MUS 318 - Conducting II”
### `8c66e2aab0ae3890` Western Kentucky University — degree_requirements 2026-27 · program_key=chinese-bachelor-of-arts · requirement_key=program-requirements-36-73-hours-required-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/chinese-ba/ (sha256 801e366f9cda)
- issues: course_alternatives_in_rule_text
  - courses: CHIN 102 ⟵ “CHIN 102 - Elementary Chinese II”
  - courses: CHIN 201 ⟵ “CHIN 201 - Intermediate Chinese I”
  - courses: CHIN 202 ⟵ “CHIN 202 - Intermediate Chinese II”
  - courses: CHIN 301 ⟵ “CHIN 301 - Advanced Intermediate Chinese I”
  - courses: CHIN 302 ⟵ “CHIN 302 - Advanced Intermediate Chinese II”
  - courses: CHIN 401 ⟵ “CHIN 401 - Advanced Chinese I”
  - courses: CHIN 402 ⟵ “CHIN 402 - Advanced Chinese II”
### `8cdc4d7cc61aee9b` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=program-requirements-33-48-hours-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - section: program-requirements-33-48-hours-electives ⟵ “Program Requirements (33-48 hours) — Electives”
### `8f8792cb30155202` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-vocal-trac-3 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 414 ⟵ “MUS 414 - Choral Materials”
  - courses: MUS 415 ⟵ “MUS 415 - Choral Methods”
  - courses: MUS 215 ⟵ “MUS 215 - Brass Techniques”
  - courses: MUS 315 ⟵ “MUS 315 - Clarinet and Saxophone Techniques”
  - courses: MUS 316 ⟵ “MUS 316 - Flute and Double Reed Techniques”
  - courses: MUS 319 ⟵ “MUS 319 - Percussion Techniques”
### `8fb1180bebe5fa8e` Western Kentucky University — degree_requirements 2026-27 · program_key=music-liberal-arts-bachelor-of-arts · requirement_key=additional-requirements-specific-to-the-music-extended-48-hour-program-music-ele [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-liberal-arts-ba/ (sha256 387a2e064bcb)
- issues: requirement_groups_skipped
  - section: additional-requirements-specific-to-the-music-extended-48-hour-program-music-ele ⟵ “Additional Requirements Specific to the Music-Extended (48 hour) Program — Music Electives”
### `937e621c0b621bd4` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-vocal-track-only [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 152 ⟵ “MUS 152 - Diction I for Voice Majors”
  - courses: MUS 252 ⟵ “MUS 252 - Diction II for Voice Majors”
### `951e38c658ace34c` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=acting-concentration-history-and-literature-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 363 ⟵ “THEA 363 - World Theatre History I”
  - courses: THEA 375 ⟵ “THEA 375 - Topics in Drama”
### `955231b2c481e726` Western Kentucky University — degree_requirements 2026-27 · program_key=mathematical-economics-bachelor-of-science · requirement_key=program-requirements-50-65-hours-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/mathematical-economics-bs/ (sha256 195ac45cd091)
- issues: course_alternatives_in_rule_text
  - courses: ECON 202 ⟵ “ECON 202 - Principles of Economics (Micro)”
  - courses: ECON 203 ⟵ “ECON 203 - Principles of Economics (Macro)”
  - courses: ECON 206 ⟵ “ECON 206 - Statistics”
  - courses: ECON 302 ⟵ “ECON 302 - Microeconomic Theory”
  - courses: ECON 303 ⟵ “ECON 303 - Macroeconomic Theory”
  - courses: ECON 465 ⟵ “ECON 465 - Regression and Econometric Analysis”
  - courses: ECON 480 ⟵ “ECON 480 - Economic Forecasting”
  - courses: STAT 401 ⟵ “STAT 401 - Regression Analysis”
  - courses: MATH 136 ⟵ “MATH 136 - Calculus I”
  - courses: MATH 137 ⟵ “MATH 137 - Calculus II”
  - courses: MATH 237 ⟵ “MATH 237 - Multivariable Calculus”
  - courses: MATH 306 ⟵ “MATH 306 - Applied and Computational Linear Algebra 1”
  - courses: ECON 497 ⟵ “ECON 497 - Senior Seminar in Mathematical Economics”
### `96565fada92f9a5a` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-ceramics [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 321 ⟵ “ART 321 - Ceramics”
  - courses: ART 420 ⟵ “ART 420 - Ceramics”
  - courses: ART 421 ⟵ “ART 421 - Ceramics”
  - courses: ART 422 ⟵ “ART 422 - Ceramics”
  - courses: ART 423 ⟵ “ART 423 - Pottery Wheel Techniques”
  - courses: ART 424 ⟵ “ART 424 - Ceramic Glaze Composition”
  - courses: ART 425 ⟵ “ART 425 - Ceramic Studio Equipment Design”
  - courses: ART 426 ⟵ “ART 426 - Special Firing Techniques”
### `9a376d23756de30a` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=program-requirements-33-48-hours-geographic-and-chronological-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 200 ⟵ “HIST 200 - Latin American Society: Past and Present”
  - courses: HIST 331 ⟵ “HIST 331 - History of Africa Since 1500”
  - courses: HIST 364 ⟵ “HIST 364 - Colonial Latin America, 1400-1825”
  - courses: HIST 365 ⟵ “HIST 365 - Modern Latin America, 1800-Present”
  - courses: HIST 465 ⟵ “HIST 465 - The Mexican Republic”
  - courses: HIST 370 ⟵ “HIST 370 - Modern South Asia: from Empires to Nations”
  - courses: HIST 378 ⟵ “HIST 378 - History of Yoga: Tradition, Literature, Practice”
  - courses: HIST 379 ⟵ “HIST 379 - Gandhi: The Creation of a Global Legacy”
  - courses: HIST 461 ⟵ “HIST 461 - Modern East Asia”
  - courses: HIST 462 ⟵ “HIST 462 - History of the Middle East”
  - courses: HIST 466 ⟵ “HIST 466 - The Arab-Israeli Conflict: Local and Global Influences”
  - courses: HIST 471 ⟵ “HIST 471 - Modern China”
  - courses: HIST 304 ⟵ “HIST 304 - Ancient Identities”
  - courses: HIST 305 ⟵ “HIST 305 - Ancient Greece”
  - courses: HIST 306 ⟵ “HIST 306 - Ancient Rome”
  - courses: HIST 307 ⟵ “HIST 307 - The Middle Ages”
  - courses: HIST 308 ⟵ “HIST 308 - Conflict, Culture and Commerce in the Medieval Mediterranean”
  - courses: HIST 317 ⟵ “HIST 317 - Renaissance Europe”
  - courses: HIST 318 ⟵ “HIST 318 - Age of the Reformation”
  - courses: HIST 322 ⟵ “HIST 322 - Age of Enlightenment”
  - courses: HIST 323 ⟵ “HIST 323 - The British Isles to 1688”
  - courses: HIST 330 ⟵ “HIST 330 - History of Africa Before 1500”
  - courses: HIST 404 ⟵ “HIST 404 - History of Ancient Egypt”
  - courses: HIST 407 ⟵ “HIST 407 - The Crusades: West Meets East”
  - courses: HIST 419 ⟵ “HIST 419 - Tudor-Stuart England”
  - … 3 more rows
### `9e04a795f0f0a4cd` Western Kentucky University — degree_requirements 2026-27 · program_key=interior-design-and-fashion-studies-bachelor-of-science · requirement_key=interior-design-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/interior-design-fashion-studies-bs/ (sha256 7a57d16420c2)
- issues: course_alternatives_in_rule_text
  - courses: IDFS 101 ⟵ “IDFS 101 - Foundations of Interior Design”
  - courses: IDFS 151 ⟵ “IDFS 151 - Survey of Architecture and Interiors I”
  - courses: IDFS 152 ⟵ “IDFS 152 - Survey of Architecture and Interiors II”
  - courses: IDFS 201 ⟵ “IDFS 201 - Interior Design Studio I”
  - courses: IDFS 222 ⟵ “IDFS 222 - IDFS Computer Aided Design”
  - courses: IDFS 243 ⟵ “IDFS 243 - Materials and Finishes for Interior Design”
  - courses: IDFS 300 ⟵ “IDFS 300 - Interior Design Studio II”
  - courses: IDFS 301 ⟵ “IDFS 301 - Interior Design Studio III”
  - courses: IDFS 302 ⟵ “IDFS 302 - Interior Design Studio IV”
  - courses: IDFS 304 ⟵ “IDFS 304 - Lighting and Environmental Controls”
  - courses: IDFS 344 ⟵ “IDFS 344 - Revit for Interiors I”
  - courses: IDFS 401 ⟵ “IDFS 401 - Interior Design Studio V”
  - courses: IDFS 402 ⟵ “IDFS 402 - Senior Design Thesis”
  - courses: IDFS 403 ⟵ “IDFS 403 - Business Principles and Practices for Interior Design”
  - courses: IDFS 410 ⟵ “IDFS 410 - IDFS Internship”
  - courses: IDFS 421 ⟵ “IDFS 421 - Portfolio Design”
  - courses: IDFS 427 ⟵ “IDFS 427 - Revit for Interiors II”
  - courses: MKT 220 ⟵ “MKT 220 - Basic Marketing Concepts”
  - courses: MKT 331 ⟵ “MKT 331 - Social Media Marketing”
  - courses: ART 105 ⟵ “ART 105 - History of Art to 1300”
  - courses: ART 130 ⟵ “ART 130 - Two-Dimensional Design Foundations”
  - courses: ART 140 ⟵ “ART 140 - Drawing Foundations I”
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: IDFS 308 ⟵ “IDFS 308 - Design and the Human Lifecycle”
  - courses: IDFS 313 ⟵ “IDFS 313 - Practicum in Interior Design Fashion Studies”
  - … 14 more rows
### `9e690aff638a397e` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-dance-12-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: DANC 103 ⟵ “DANC 103 - Foundations of Dance Technique”
### `9fd5281fd94c1701` Western Kentucky University — degree_requirements 2026-27 · program_key=asian-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-electives-9-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/asian-studies-ba/ (sha256 d4bf15768a8d)
- issues: requirement_groups_skipped
  - courses: ANTH 333 ⟵ “ANTH 333 - The Archaeology of Ancient China”
  - courses: ARC 401 ⟵ “ARC 401 - Topics in Asian Religions and Cultures”
  - courses: ARC 498 ⟵ “ARC 498 - Study in Asian Religions and Cultures”
  - courses: ART 407 ⟵ “ART 407 - Islamic Art and Architecture”
  - courses: CHIN 101 ⟵ “CHIN 101 - Elementary Chinese I”
  - courses: CHIN 102 ⟵ “CHIN 102 - Elementary Chinese II”
  - courses: CHIN 201 ⟵ “CHIN 201 - Intermediate Chinese I”
  - courses: CHIN 202 ⟵ “CHIN 202 - Intermediate Chinese II”
  - courses: CHIN 208 ⟵ “CHIN 208 - Chinese Calligraphy”
  - courses: CHIN 301 ⟵ “CHIN 301 - Advanced Intermediate Chinese I”
  - courses: CHIN 302 ⟵ “CHIN 302 - Advanced Intermediate Chinese II”
  - courses: CHIN 401 ⟵ “CHIN 401 - Advanced Chinese I”
  - courses: CHIN 402 ⟵ “CHIN 402 - Advanced Chinese II”
  - courses: CHNF 201 ⟵ “CHNF 201 - Intensive Intermediate Chinese I”
  - courses: CHNF 202 ⟵ “CHNF 202 - Intensive Intermediate Chinese II”
  - courses: CHNF 301 ⟵ “CHNF 301 - Intensive Advanced Chinese I”
  - courses: CHNF 302 ⟵ “CHNF 302 - Intensive Advanced Chinese II”
  - courses: CHNF 420 ⟵ “CHNF 420 - Media Chinese”
  - courses: CHNF 430 ⟵ “CHNF 430 - Chinese Culture”
  - courses: CHNF 440 ⟵ “CHNF 440 - Chinese Tradition”
  - courses: CHNF 450 ⟵ “CHNF 450 - Classical Chinese”
  - courses: GEOG 465 ⟵ “GEOG 465 - Geography of East Asia”
  - courses: HIST 351 ⟵ “HIST 351 - Asian American History”
  - courses: HIST 370 ⟵ “HIST 370 - Modern South Asia: from Empires to Nations”
  - courses: HIST 378 ⟵ “HIST 378 - History of Yoga: Tradition, Literature, Practice”
  - … 15 more rows
### `a2583840aef0c838` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-music [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MUS 102 ⟵ “MUS 102 - Music Theory I for Non-Majors”
  - courses: MUS 170 ⟵ “MUS 170 - Group Piano for Non-Majors”
  - courses: THEA 306 ⟵ “THEA 306 - Musical Theatre Ensemble”
  - courses: MUS 162 ⟵ “MUS 162 - Group Voice”
  - courses: MUS 350 ⟵ “MUS 350 - Applied Music Secondary (1 hour each)”
  - courses: THEA 324 ⟵ “THEA 324 - Applied Vocal Styles I”
  - courses: THEA 385 ⟵ “THEA 385 - Applied Vocal Styles II (1 hour each)”
### `a2c76aecc45eed20` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-performance-attenda [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 155 ⟵ “MUS 155 - Performance Attendance (8 semesters)”
### `a508c93497647985` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-studio-upper-level-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 321 ⟵ “ART 321 - Ceramics”
  - courses: ART 420 ⟵ “ART 420 - Ceramics”
  - courses: ART 421 ⟵ “ART 421 - Ceramics”
  - courses: ART 422 ⟵ “ART 422 - Ceramics”
  - courses: ART 423 ⟵ “ART 423 - Pottery Wheel Techniques”
  - courses: ART 424 ⟵ “ART 424 - Ceramic Glaze Composition”
  - courses: ART 425 ⟵ “ART 425 - Ceramic Studio Equipment Design”
  - courses: ART 426 ⟵ “ART 426 - Special Firing Techniques”
  - courses: ART 330 ⟵ “ART 330 - Graphic Design II: Layout & Information Design”
  - courses: DES 331 ⟵ “DES 331 - Visual Thinking”
  - courses: ART 334 ⟵ “ART 334 - Survey of Graphic Design”
  - courses: ART 430 ⟵ “ART 430 - Graphic Design III: Advanced Graphic Design”
  - courses: ART 431 ⟵ “ART 431 - Illustration”
  - courses: ART 433 ⟵ “ART 433 - Package Design”
  - courses: ART 436 ⟵ “ART 436 - Digital Illustration”
  - courses: DES 438 ⟵ “DES 438 - Advanced Media Design”
  - courses: ART 440 ⟵ “ART 440 - Drawing”
  - courses: ART 350 ⟵ “ART 350 - Printmaking”
  - courses: ART 351 ⟵ “ART 351 - Printmaking”
  - courses: ART 450 ⟵ “ART 450 - Printmaking”
  - courses: ART 451 ⟵ “ART 451 - Printmaking”
  - courses: ART 452 ⟵ “ART 452 - Printmaking”
  - courses: ART 453 ⟵ “ART 453 - Senior Techniques in Printmaking”
  - courses: ART 454 ⟵ “ART 454 - Senior Composition in Printmaking”
  - courses: ART 455 ⟵ “ART 455 - Advanced Senior Techniques in Printmaking”
  - … 15 more rows
### `a652e7652f50ae53` Western Kentucky University — degree_requirements 2026-27 · program_key=social-studies-bachelor-of-arts · requirement_key=program-requirements-51-hours-political-and-behavioral-sciences [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/social-studies-ba/ (sha256 02fc45f9924f)
- issues: course_alternatives_in_rule_text
  - courses: PS 110 ⟵ “PS 110 - American National Government”
  - courses: IA 250 ⟵ “IA 250 - International Politics”
  - courses: ANTH 120 ⟵ “ANTH 120 - Introduction to Cultural Anthropology”
  - courses: ANTH 342 ⟵ “ANTH 342 - Peoples and Cultures of the Caribbean”
  - courses: ANTH 360 ⟵ “ANTH 360 - Applied Anthropology – Understanding and Addressing Contemporary Human Problems”
  - courses: ANTH 388 ⟵ “ANTH 388 - Foodways”
  - courses: PS 310 ⟵ “PS 310 - The American Presidency”
  - courses: PS 316 ⟵ “PS 316 - The Legislative Process”
  - courses: PS 326 ⟵ “PS 326 - Constitutional Law”
  - courses: PS 327 ⟵ “PS 327 - Civil Liberties”
  - courses: PS 328 ⟵ “PS 328 - Criminal Justice Procedures”
  - courses: IA 357 ⟵ “IA 357 - U S Foreign Policy”
  - courses: PS 370 ⟵ “PS 370 - American Political Parties and Interest Groups”
  - courses: PS 373 ⟵ “PS 373 - Minority Politics”
  - courses: PS 374 ⟵ “PS 374 - Women and Politics”
  - courses: PS 435 ⟵ “PS 435 - American Political Thought”
  - courses: PSYS 350 ⟵ “PSYS 350 - Social Psychology”
  - courses: SOCL 100 ⟵ “SOCL 100 - Introductory Sociology”
  - courses: SOCL 322 ⟵ “SOCL 322 - Religion in Society”
  - courses: SOCL 362 ⟵ “SOCL 362 - Social Institutions: Race, Class, and Gender”
  - courses: SOCL 363 ⟵ “SOCL 363 - Population, Society, and Development”
  - courses: SOCL 375 ⟵ “SOCL 375 - Diversity in American Society”
  - courses: SOCL 376 ⟵ “SOCL 376 - Sociology of Globalization”
### `a66450645da020a2` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-the-music-education-concentration-all-tracks-integrated-vocal-i-3 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 160 ⟵ “MUS 160 - Group Piano I 1”
  - courses: MUS 161 ⟵ “MUS 161 - Group Piano II 1”
  - courses: MUS 260 ⟵ “MUS 260 - Group Piano III 1”
  - courses: MUS 261 ⟵ “MUS 261 - Group Piano IV 1”
### `a6ffed512320b236` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=animation-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 220 ⟵ “ART 220 - Ceramics”
  - courses: ART 231 ⟵ “ART 231 - Graphic Design I: Typography”
  - courses: ART 250 ⟵ “ART 250 - Printmaking”
  - courses: ART 260 ⟵ “ART 260 - Painting”
  - courses: ART 270 ⟵ “ART 270 - Sculpture Survey I”
  - courses: ART 280 ⟵ “ART 280 - Weaving”
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: ART 240 ⟵ “ART 240 - Drawing Foundations II”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 431 ⟵ “ART 431 - Illustration”
  - courses: ART 321 ⟵ “ART 321 - Ceramics”
  - courses: ART 420 ⟵ “ART 420 - Ceramics”
  - courses: ART 421 ⟵ “ART 421 - Ceramics”
  - courses: ART 422 ⟵ “ART 422 - Ceramics”
  - courses: ART 423 ⟵ “ART 423 - Pottery Wheel Techniques”
  - courses: ART 424 ⟵ “ART 424 - Ceramic Glaze Composition”
  - courses: ART 425 ⟵ “ART 425 - Ceramic Studio Equipment Design”
  - courses: ART 426 ⟵ “ART 426 - Special Firing Techniques”
  - courses: ART 330 ⟵ “ART 330 - Graphic Design II: Layout & Information Design”
  - courses: DES 331 ⟵ “DES 331 - Visual Thinking”
  - courses: ART 334 ⟵ “ART 334 - Survey of Graphic Design”
  - courses: ART 430 ⟵ “ART 430 - Graphic Design III: Advanced Graphic Design”
  - courses: ART 431 ⟵ “ART 431 - Illustration”
  - courses: ART 433 ⟵ “ART 433 - Package Design”
  - courses: ART 436 ⟵ “ART 436 - Digital Illustration”
  - … 15 more rows
### `a758a1a20495b256` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=graphic-design-concentration-graphic-design-concentration-focus [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 243 ⟵ “ART 243 - Digital Media”
  - courses: ART 231 ⟵ “ART 231 - Graphic Design I: Typography”
  - courses: UX 330 ⟵ “UX 330 - User Interface Design”
  - courses: ART 330 ⟵ “ART 330 - Graphic Design II: Layout & Information Design”
  - courses: DES 331 ⟵ “DES 331 - Visual Thinking”
  - courses: ART 430 ⟵ “ART 430 - Graphic Design III: Advanced Graphic Design”
  - courses: DES 438 ⟵ “DES 438 - Advanced Media Design”
  - courses: ART 432 ⟵ “ART 432 - Portfolio”
  - courses: ART 434 ⟵ “ART 434 - Capstone Seminar”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 377 ⟵ “ART 377 - Design to Prototype I”
  - courses: ART 399 ⟵ “ART 399 - Professional Work”
  - courses: ART 431 ⟵ “ART 431 - Illustration”
  - courses: ART 433 ⟵ “ART 433 - Package Design”
  - courses: ART 436 ⟵ “ART 436 - Digital Illustration”
  - courses: DES 498 ⟵ “DES 498 - Special Topics in Graphic Design”
  - courses: ART 499 ⟵ “ART 499 - Career Experience in Art”
  - courses: UX 340 ⟵ “UX 340 - Introduction to Developing and Prototyping for Interactive Design”
### `aa95505b44fdeb10` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-the-music-education-concentration-all-tracks-integrated-vocal-i [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 100 ⟵ “MUS 100 - Theory I”
  - courses: MUS 101 ⟵ “MUS 101 - Theory II”
  - courses: MUS 200 ⟵ “MUS 200 - Theory III”
  - courses: MUS 201 ⟵ “MUS 201 - Theory IV”
  - courses: MUS 110 ⟵ “MUS 110 - Aural Theory I”
  - courses: MUS 111 ⟵ “MUS 111 - Aural Theory II”
  - courses: MUS 210 ⟵ “MUS 210 - Aural Theory III”
  - courses: MUS 211 ⟵ “MUS 211 - Aural Theory IV”
  - courses: MUS 304 ⟵ “MUS 304 - Form and Analysis”
  - courses: MUS 326 ⟵ “MUS 326 - The History of Music I”
  - courses: MUS 327 ⟵ “MUS 327 - The History of Music II”
### `aa9f95c8a1331023` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=program-requirements-79-hours-required-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 105 ⟵ “ART 105 - History of Art to 1300 1”
  - courses: ART 106 ⟵ “ART 106 - History of Art Since 1300 1”
  - courses: ART 130 ⟵ “ART 130 - Two-Dimensional Design Foundations 1”
  - courses: ART 131 ⟵ “ART 131 - Three-Dimensional Design Foundations 1”
  - courses: ART 140 ⟵ “ART 140 - Drawing Foundations I 1”
### `aafca8966d08b70e` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-sculpture-and-3d-practices [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 370 ⟵ “ART 370 - Sculpture Survey II”
  - courses: ART 371 ⟵ “ART 371 - Sculpture Methods, Welding I”
  - courses: ART 372 ⟵ “ART 372 - Sculpture, Figurative Studies”
  - courses: ART 470 ⟵ “ART 470 - Sculpture”
  - courses: ART 471 ⟵ “ART 471 - Sculpture Methods, Foundry I”
  - courses: ART 472 ⟵ “ART 472 - Sculpture”
  - courses: ART 474 ⟵ “ART 474 - Sculpture Methods, Wood”
  - courses: ART 475 ⟵ “ART 475 - Sculpture Methods, Welding II”
  - courses: ART 476 ⟵ “ART 476 - Sculpture Methods, Foundry II”
### `ac71d2d28cadd0ff` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=program-requirements-33-48-hours-foundational-study [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: HIST 101 ⟵ “HIST 101 - World History I”
  - courses: HIST 240 ⟵ “HIST 240 - The United States to 1865”
### `aee33f011d920d48` Western Kentucky University — degree_requirements 2026-27 · program_key=international-affairs-bachelor-of-arts · requirement_key=program-requirements-42-hours-core-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/international-affairs-ba/ (sha256 fa9985d13bc4)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: IA 250 ⟵ “IA 250 - International Politics”
  - courses: IA 260 ⟵ “IA 260 - Introduction to Comparative Politics”
  - courses: IA 357 ⟵ “IA 357 - U S Foreign Policy”
  - courses: IA 497 ⟵ “IA 497 - Senior Seminar in International Affairs 1”
  - courses: HIST 102 ⟵ “HIST 102 - World History II”
  - courses: ECON 202 ⟵ “ECON 202 - Principles of Economics (Micro)”
  - courses: GEOG 110 ⟵ “GEOG 110 - World Regional Geography”
### `b04d7a9f48cdc527` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-studies-bachelor-of-arts · requirement_key=art-education-concentration-required-foundation-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-studies-ba/ (sha256 fcd2c45cf314)
- issues: course_alternatives_in_rule_text
  - courses: ART 105 ⟵ “ART 105 - History of Art to 1300”
  - courses: ART 106 ⟵ “ART 106 - History of Art Since 1300”
  - courses: ART 130 ⟵ “ART 130 - Two-Dimensional Design Foundations”
  - courses: ART 131 ⟵ “ART 131 - Three-Dimensional Design Foundations”
  - courses: ART 140 ⟵ “ART 140 - Drawing Foundations I”
  - courses: ART 220 ⟵ “ART 220 - Ceramics”
  - courses: ART 231 ⟵ “ART 231 - Graphic Design I: Typography”
  - courses: ART 240 ⟵ “ART 240 - Drawing Foundations II”
  - courses: ANIM 210 ⟵ “ANIM 210 - Introduction to Computer Animation”
  - courses: ART 250 ⟵ “ART 250 - Printmaking”
  - courses: ART 260 ⟵ “ART 260 - Painting”
  - courses: ART 270 ⟵ “ART 270 - Sculpture Survey I”
  - courses: ART 280 ⟵ “ART 280 - Weaving”
  - courses: ART 340 ⟵ “ART 340 - Drawing”
  - courses: ART 341 ⟵ “ART 341 - Drawing”
  - courses: ART 440 ⟵ “ART 440 - Drawing”
  - courses: ANIM 444 ⟵ “ANIM 444 - Computer Animation III”
  - courses: ART 321 ⟵ “ART 321 - Ceramics”
  - courses: ART 420 ⟵ “ART 420 - Ceramics”
  - courses: ART 421 ⟵ “ART 421 - Ceramics”
  - courses: ART 422 ⟵ “ART 422 - Ceramics”
  - courses: ART 423 ⟵ “ART 423 - Pottery Wheel Techniques”
  - courses: ART 424 ⟵ “ART 424 - Ceramic Glaze Composition”
  - courses: ART 425 ⟵ “ART 425 - Ceramic Studio Equipment Design”
  - courses: ART 426 ⟵ “ART 426 - Special Firing Techniques”
  - … 15 more rows
### `b4a52efd6b29dbec` Western Kentucky University — degree_requirements 2026-27 · program_key=social-studies-bachelor-of-arts · requirement_key=program-requirements-51-hours-geography-at-least-three-hours-must-be-upper-divis [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/social-studies-ba/ (sha256 02fc45f9924f)
- issues: course_alternatives_in_rule_text
  - courses: GEOG 110 ⟵ “GEOG 110 - World Regional Geography”
  - courses: GEOG 110 ⟵ “GEOG 110 - World Regional Geography”
  - courses: GEOG 226 ⟵ “GEOG 226 - Our Dangerous Planet”
  - courses: GEOG 227 ⟵ “GEOG 227 - Our Vulnerable Planet”
  - courses: GEOG 330 ⟵ “GEOG 330 - Introduction to Cultural Geography”
  - courses: GEOG 352 ⟵ “GEOG 352 - Geography of Kentucky”
  - courses: GEOG 378 ⟵ “GEOG 378 - Food, Culture, and Environment”
  - courses: GEOG 380 ⟵ “GEOG 380 - Global Sustainability”
  - courses: GEOG 465 ⟵ “GEOG 465 - Geography of East Asia”
  - courses: GEOG 480 ⟵ “GEOG 480 - Sustainable Cities”
  - courses: HIST 375 ⟵ “HIST 375 - Spatial History”
### `b9dc27538d05d03c` Western Kentucky University — degree_requirements 2026-27 · program_key=communication-bachelor-of-arts · requirement_key=program-requirements-39-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/communication-ba/ (sha256 9e1978297b5b)
- issues: course_alternatives_in_rule_text
  - courses: COMM 145 ⟵ “COMM 145 - Fundamentals of Public Speaking and Communication”
  - courses: COMM 200 ⟵ “COMM 200 - Communication Foundations”
  - courses: COMM 300 ⟵ “COMM 300 - Introduction to Applied Communication Research”
  - courses: COMM 348 ⟵ “COMM 348 - Interpersonal Communication”
  - courses: COMM 346 ⟵ “COMM 346 - Persuasion”
  - courses: COMM 349 ⟵ “COMM 349 - Small Group Communication”
  - courses: COMM 362 ⟵ “COMM 362 - Organizational Communication”
  - courses: COMM 365 ⟵ “COMM 365 - Intercultural Communication”
  - courses: COMM 494 ⟵ “COMM 494 - Capstone in Communication”
  - courses: COMM 315 ⟵ “COMM 315 - Sport Communication”
  - courses: COMM 330 ⟵ “COMM 330 - Leadership Communication”
  - courses: COMM 345 ⟵ “COMM 345 - Advanced Presentational Speaking”
  - courses: COMM 346 ⟵ “COMM 346 - Persuasion”
  - courses: COMM 363 ⟵ “COMM 363 - Interracial Communication”
  - courses: COMM 364 ⟵ “COMM 364 - Crisis Communication”
  - courses: COMM 320 ⟵ “COMM 320 - Health Communication”
  - courses: COMM 351 ⟵ “COMM 351 - Communication in the Digital Age”
  - courses: COMM 371 ⟵ “COMM 371 - Communication in Multinational Organizations”
  - courses: COMM 400 ⟵ “COMM 400 - Special Topics in Communication”
  - courses: COMM 415 ⟵ “COMM 415 - Study Abroad in Communication”
  - courses: COMM 448 ⟵ “COMM 448 - Advanced Interpersonal Communication”
  - courses: COMM 462 ⟵ “COMM 462 - Advanced Organizational Communication”
  - courses: COMM 463 ⟵ “COMM 463 - Advanced Intercultural Communication”
  - courses: COMM 370 ⟵ “COMM 370 - Organizational Relationships”
  - courses: COMM 489 ⟵ “COMM 489 - Internship in Communication”
  - … 15 more rows
### `bc9c5e6febe91cfa` Western Kentucky University — degree_requirements 2026-27 · program_key=political-science-bachelor-of-arts · requirement_key=program-requirements-36-hours-required-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/political-science-ba/ (sha256 45b7e630d76b)
- issues: course_alternatives_in_rule_text
  - courses: PS 110 ⟵ “PS 110 - American National Government”
  - courses: IA 250 ⟵ “IA 250 - International Politics”
  - courses: PS 275 ⟵ “PS 275 - Introduction to Citizenship”
  - courses: PS 499 ⟵ “PS 499 - Senior Seminar in Government 1”
  - courses: PS 301 ⟵ “PS 301 - Using Statistics in Political Science”
  - courses: IA 260 ⟵ “IA 260 - Introduction to Comparative Politics”
  - courses: IA 350 ⟵ “IA 350 - Political Terrorism”
  - courses: PS 359 ⟵ “PS 359 - Politics of North Korea”
  - courses: IA 360 ⟵ “IA 360 - Government and Politics of Britain and Canada”
  - courses: IA 361 ⟵ “IA 361 - Government and Politics of Western Europe”
  - courses: IA 362 ⟵ “IA 362 - Latin American Government and Politics”
  - courses: IA 363 ⟵ “IA 363 - Politics of Developing Nations”
  - courses: IA 364 ⟵ “IA 364 - Chinese Politics”
  - courses: IA 365 ⟵ “IA 365 - Government and Politics of the Middle East”
  - courses: PS 366 ⟵ “PS 366 - Government and Politics in East Asia”
  - courses: IA 367 ⟵ “IA 367 - Government and Politics of Russia and Eastern Europe”
  - courses: IA 368 ⟵ “IA 368 - African Government and Politics”
  - courses: IA 369 ⟵ “IA 369 - Central European Politics”
  - courses: PS 220 ⟵ “PS 220 - Judicial Process”
  - courses: PS 304 ⟵ “PS 304 - State Government”
  - courses: PS 310 ⟵ “PS 310 - The American Presidency”
  - courses: PS 316 ⟵ “PS 316 - The Legislative Process”
  - courses: PS 355 ⟵ “PS 355 - International Organization and Law”
  - courses: PS 412 ⟵ “PS 412 - Kentucky Government and Politics”
  - courses: PS 311 ⟵ “PS 311 - Public Policy”
  - … 7 more rows
### `c0f0d6d21c006d1f` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-production-2-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: PERF 321 ⟵ “PERF 321 - Production Lab III”
### `c516ea5e3bbfd928` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-journalism-and-photography-bachelor-of-arts-752p-752 · requirement_key=photojournalism-and-documentary-concentration-restricted-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/visual-journalism-photography-ba/ (sha256 55cb5defcc5a)
- issues: course_alternatives_in_rule_text
  - courses: VJP 390 ⟵ “VJP 390 - Cultural History of Photography”
  - courses: VJP 433 ⟵ “VJP 433 - Advanced Lighting”
  - courses: VJP 430 ⟵ “VJP 430 - Advanced Short Form Documentary *”
  - courses: JOUR 302 ⟵ “JOUR 302 - Intermediate Reporting”
  - courses: BCOM 366 ⟵ “BCOM 366 - Editing I”
  - courses: BCOM 380 ⟵ “BCOM 380 - Editing II”
  - courses: FILM 377 ⟵ “FILM 377 - Film Sound”
  - courses: SOM 399 ⟵ “SOM 399 - Special Topics in Media--Study Abroad”
  - courses: SMC 402 ⟵ “SMC 402 - First Amendment Research and Reporting”
### `c58f4a5781dab3f9` Western Kentucky University — degree_requirements 2026-27 · program_key=integrated-advertising-public-relations-bachelor-of-arts-753p-753 · requirement_key=public-relations-concentration-required-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/integrated-advertising-pr-ba/ (sha256 894e3bc19fa7)
- issues: course_alternatives_in_rule_text
  - courses: JOUR 202 ⟵ “JOUR 202 - Introduction to News Writing”
  - courses: PR 358 ⟵ “PR 358 - Public Relations Writing and Production”
  - courses: PR 385 ⟵ “PR 385 - Artificial Intelligence in Public Relations”
  - courses: AD 250 ⟵ “AD 250 - Personal Branding”
  - courses: ART 399 ⟵ “ART 399 - Professional Work”
  - courses: ART 499 ⟵ “ART 499 - Career Experience in Art”
  - courses: BCOM 264 ⟵ “BCOM 264 - Digital Video Production and Distribution”
  - courses: BCOM 265 ⟵ “BCOM 265 - Basic Broadcast News”
  - courses: BCOM 266 ⟵ “BCOM 266 - Basic Television Production”
  - courses: BCOM 325 ⟵ “BCOM 325 - Survey of Electronic Media Writing”
  - courses: BCOM 368 ⟵ “BCOM 368 - News Videography and Editing”
  - courses: BCOM 335 ⟵ “BCOM 335 - News Discovery and Selection”
  - courses: COMM 315 ⟵ “COMM 315 - Sport Communication”
  - courses: COMM 320 ⟵ “COMM 320 - Health Communication”
  - courses: COMM 346 ⟵ “COMM 346 - Persuasion”
  - courses: COMM 345 ⟵ “COMM 345 - Advanced Presentational Speaking”
  - courses: COMM 349 ⟵ “COMM 349 - Small Group Communication”
  - courses: COMM 364 ⟵ “COMM 364 - Crisis Communication”
  - courses: ENG 212 ⟵ “ENG 212 - Introduction to Digital Texts and Media”
  - courses: JOUR 323 ⟵ “JOUR 323 - Multiplatform News Presentation”
  - courses: JOUR 325 ⟵ “JOUR 325 - Feature Writing”
  - courses: PR 347 ⟵ “PR 347 - Sport Media Relations”
  - courses: PR 400 ⟵ “PR 400 - Special Topics in Public Relations”
  - courses: PR 415 ⟵ “PR 415 - Study Abroad in Public Relations”
  - courses: PR 489 ⟵ “PR 489 - PR Internship or Practicum”
  - … 8 more rows
### `c5980fd1694923e3` Western Kentucky University — degree_requirements 2026-27 · program_key=mathematical-economics-bachelor-of-science · requirement_key=actuarial-science-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/mathematical-economics-bs/ (sha256 195ac45cd091)
- issues: course_alternatives_in_rule_text
  - courses: ECON 307 ⟵ “ECON 307 - Financial Data Modeling”
  - courses: MATH 310 ⟵ “MATH 310 - Introduction to Discrete Mathematics”
  - courses: ACTU 382 ⟵ “ACTU 382 - Probability and Statistics I”
  - courses: ACTU 482 ⟵ “ACTU 482 - Probability and Statistics II”
  - courses: FIN 330 ⟵ “FIN 330 - Principles of Finance”
  - courses: FIN 332 ⟵ “FIN 332 - Investment Theory”
  - courses: FIN 350 ⟵ “FIN 350 - Risk Management and Insurance”
  - courses: FIN 437 ⟵ “FIN 437 - Corporate Asset Management”
  - courses: CS 170 ⟵ “CS 170 - Problem Solving and Programming”
  - courses: ACTU 301 ⟵ “ACTU 301 - Financial Mathematics for Actuarial Science”
### `c63e1d2edb59a3b0` Western Kentucky University — degree_requirements 2026-27 · program_key=music-liberal-arts-bachelor-of-arts · requirement_key=additional-requirements-specific-to-the-music-general-36-hour-program-applied-mu [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-liberal-arts-ba/ (sha256 387a2e064bcb)
- issues: requirement_groups_skipped
  - courses: MUS 153 ⟵ “MUS 153 - Applied Music Principal (2 semsters)”
  - courses: MUS 350 ⟵ “MUS 350 - Applied Music Secondary (4 semesters)”
  - courses: MUS 160 ⟵ “MUS 160 - Group Piano I 1”
  - courses: MUS 161 ⟵ “MUS 161 - Group Piano II 1”
### `cc133e3f70706711` Western Kentucky University — degree_requirements 2026-27 · program_key=international-affairs-bachelor-of-arts · requirement_key=program-requirements-42-hours-electives [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/international-affairs-ba/ (sha256 fa9985d13bc4)
- issues: requirement_groups_skipped
  - courses: AFAM 343 ⟵ “AFAM 343 - Communities of Struggle”
  - courses: AFAM 350 ⟵ “AFAM 350 - Peoples and Cultures of Africa”
  - courses: ANTH 120 ⟵ “ANTH 120 - Introduction to Cultural Anthropology”
  - courses: ANTH 340 ⟵ “ANTH 340 - Peoples and Cultures of Latin America”
  - courses: ANTH 342 ⟵ “ANTH 342 - Peoples and Cultures of the Caribbean”
  - courses: ANTH 350 ⟵ “ANTH 350 - Peoples and Cultures of Africa”
  - courses: ANTH 360 ⟵ “ANTH 360 - Applied Anthropology – Understanding and Addressing Contemporary Human Problems”
  - courses: ARBC 202 ⟵ “ARBC 202 - Intermediate Arabic II”
  - courses: ARBC 306 ⟵ “ARBC 306 - Experiencing Arabic Abroad”
  - courses: ARBC 324 ⟵ “ARBC 324 - Arabic Civilization II”
  - courses: ARBC 437 ⟵ “ARBC 437 - Advanced Media Arabic”
  - courses: ARBC 438 ⟵ “ARBC 438 - Topics in Arabic Media”
  - courses: CHIN 202 ⟵ “CHIN 202 - Intermediate Chinese II”
  - courses: CHIN 306 ⟵ “CHIN 306 - Experiencing Chinese Abroad”
  - courses: CHIN 333 ⟵ “CHIN 333 - Chinese Culture and Civilization”
  - courses: CHNF 202 ⟵ “CHNF 202 - Intensive Intermediate Chinese II”
  - courses: CHNF 420 ⟵ “CHNF 420 - Media Chinese”
  - courses: CHNF 430 ⟵ “CHNF 430 - Chinese Culture”
  - courses: COMM 365 ⟵ “COMM 365 - Intercultural Communication”
  - courses: ECON 380 ⟵ “ECON 380 - International Economics”
  - courses: ECON 385 ⟵ “ECON 385 - Economic Development”
  - courses: ECON 496 ⟵ “ECON 496 - International Monetary Economics”
  - courses: FIN 433 ⟵ “FIN 433 - Financial Markets and Institutions”
  - courses: FIN 436 ⟵ “FIN 436 - International Financial Management”
  - courses: FLK 310 ⟵ “FLK 310 - Community Traditions & Global Corporate Culture”
  - … 15 more rows
### `cc925a939967cf4c` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-bachelor-of-music-performance-concentration-music-theory-and-li [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 100 ⟵ “MUS 100 - Theory I”
  - courses: MUS 101 ⟵ “MUS 101 - Theory II”
  - courses: MUS 200 ⟵ “MUS 200 - Theory III”
  - courses: MUS 201 ⟵ “MUS 201 - Theory IV”
  - courses: MUS 110 ⟵ “MUS 110 - Aural Theory I”
  - courses: MUS 111 ⟵ “MUS 111 - Aural Theory II”
  - courses: MUS 210 ⟵ “MUS 210 - Aural Theory III”
  - courses: MUS 211 ⟵ “MUS 211 - Aural Theory IV”
  - courses: MUS 304 ⟵ “MUS 304 - Form and Analysis”
  - courses: MUS 326 ⟵ “MUS 326 - The History of Music I”
  - courses: MUS 327 ⟵ “MUS 327 - The History of Music II”
  - courses: MUS 430 ⟵ “MUS 430 - Music Literature”
### `cd3ff99ae5758a2b` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=additional-requirements-specific-to-the-music-education-concentration-vocal-trac [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 405 ⟵ “MUS 405 - Choral Arranging”
### `d3e1163f8565086d` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=musical-theatre-concentration-design-9-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 319 ⟵ “THEA 319 - Design II”
  - courses: ART 106 ⟵ “ART 106 - History of Art Since 1300”
  - courses: THEA 322 ⟵ “THEA 322 - Stage Design”
### `d6011e81db3d718a` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-for-international-business-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
- issues: course_alternatives_in_rule_text
  - courses: SPAN 345 ⟵ “SPAN 345 - Topics in Spanish”
  - courses: SPAN 470 ⟵ “SPAN 470 - Advanced Oral Spanish”
  - courses: MGT 210 ⟵ “MGT 210 - Organization and Management”
  - courses: MGT 303 ⟵ “MGT 303 - International Business”
  - courses: SPAN 389 ⟵ “SPAN 389 - Internship in Spanish”
  - courses: SPAN 331 ⟵ “SPAN 331 - Spanish for Professional Communication”
  - courses: SPAN 455 ⟵ “SPAN 455 - Topics in Hispanic Literary and Cultural Studies”
  - courses: SPAN 480 ⟵ “SPAN 480 - Translation and Interpreting”
  - courses: ENT 425 ⟵ “ENT 425 - International Entrepreneurship”
  - courses: MGT 316 ⟵ “MGT 316 - International Management”
  - courses: ECON 380 ⟵ “ECON 380 - International Economics”
### `dada9d177a4d1035` Western Kentucky University — degree_requirements 2026-27 · program_key=criminology-bachelor-of-arts · requirement_key=program-requirements-35-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/society-culture-crime-justice/criminology-ba/ (sha256 5191dda112b1)
- issues: course_alternatives_in_rule_text
  - courses: CRIM 101 ⟵ “CRIM 101 - Introduction to Criminal Justice”
  - courses: CRIM 330 ⟵ “CRIM 330 - Criminology”
  - courses: CRIM 199 ⟵ “CRIM 199 - College & Careers in Criminology & Sociology”
  - courses: SOCL 300 ⟵ “SOCL 300 - Social Statistics”
  - courses: SOCL 301 ⟵ “SOCL 301 - Social Statistics Lab”
  - courses: SOCL 302 ⟵ “SOCL 302 - Social Research Methods”
  - courses: SOCL 309 ⟵ “SOCL 309 - Social Deviance”
  - courses: CRIM 332 ⟵ “CRIM 332 - Juvenile Delinquency”
  - courses: CRIM 361 ⟵ “CRIM 361 - Race, Class, and Crime”
  - courses: CRIM 446 ⟵ “CRIM 446 - Gender, Crime, and Justice”
  - courses: CRIM 340 ⟵ “CRIM 340 - Criminal Courts and Sentencing”
  - courses: CRIM 370 ⟵ “CRIM 370 - Issues in Policing”
  - courses: CRIM 380 ⟵ “CRIM 380 - Punishment and Society”
  - courses: CRIM 430 ⟵ “CRIM 430 - Comparative Systems of Juvenile Justice”
  - courses: CRIM 432 ⟵ “CRIM 432 - Sociology of Criminal Law”
  - courses: PS 328 ⟵ “PS 328 - Criminal Justice Procedures”
  - courses: ANTH 300 ⟵ “ANTH 300 - Forensic Anthropology”
  - courses: CHEM 111 ⟵ “CHEM 111 - Introduction to Forensic Chemistry”
  - courses: CHEM 430 ⟵ “CHEM 430 - Forensic Chemistry”
  - courses: CRIM 222 ⟵ “CRIM 222 - Introduction to Crime Mapping”
  - courses: CRIM 232 ⟵ “CRIM 232 - Introduction to Law Enforcement”
  - courses: CRIM 233 ⟵ “CRIM 233 - Alternatives to Confinement”
  - courses: CRIM 234 ⟵ “CRIM 234 - Crime and Popular Culture”
  - courses: CRIM 238 ⟵ “CRIM 238 - Victimology & Victim Advocacy”
  - courses: CRIM 332 ⟵ “CRIM 332 - Juvenile Delinquency”
  - … 15 more rows
### `db86b7e4b8aa8490` Western Kentucky University — degree_requirements 2026-27 · program_key=music-bachelor-of-music · requirement_key=requirements-for-the-music-education-concentration-all-tracks-integrated-vocal-i-4 [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/music/music-bm/ (sha256 09ac5d75b023)
- issues: requirement_groups_skipped
  - courses: MUS 155 ⟵ “MUS 155 - Performance Attendance (7 semesters)”
### `dc8580a634572831` Western Kentucky University — degree_requirements 2026-27 · program_key=business-economics-bachelor-of-science · requirement_key=program-requirements-72-hours-career-preparation-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/economics/business-economics-bs/ (sha256 367d4d265754)
- issues: course_alternatives_in_rule_text
  - courses: BA 170 ⟵ “BA 170 - Business Student Basics 1”
  - courses: MGT 261 ⟵ “MGT 261 - Business Communication Fundamentals”
  - courses: ECON 399 ⟵ “ECON 399 - Career Readiness in Economics”
  - courses: ECON 499 ⟵ “ECON 499 - Senior Assessment”
### `de338a9604f4c73b` Western Kentucky University — degree_requirements 2026-27 · program_key=dance-bachelor-of-arts-630p-630 · requirement_key=program-requirements-46-hours-restricted-electives-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/dance-ba/ (sha256 f4f5bd40773f)
- issues: requirement_groups_skipped
  - section: program-requirements-46-hours-restricted-electives-6-hours ⟵ “Program Requirements (46 hours) — Restricted Electives (6 hours)”
### `e35cfaaeb6b2a73a` Western Kentucky University — degree_requirements 2026-27 · program_key=asian-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-religion-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/asian-studies-ba/ (sha256 d4bf15768a8d)
- issues: requirement_groups_skipped
  - courses: RELS 102 ⟵ “RELS 102 - World Religions”
  - courses: RELS 302 ⟵ “RELS 302 - Buddhism”
  - courses: RELS 303 ⟵ “RELS 303 - Hinduism”
  - courses: RELS 306 ⟵ “RELS 306 - Islam”
  - courses: RELS 317 ⟵ “RELS 317 - Confucianism”
  - courses: RELS 318 ⟵ “RELS 318 - Daoism”
  - courses: RELS 319 ⟵ “RELS 319 - Religions of Asia”
  - courses: RELS 322 ⟵ “RELS 322 - Pilgrimage, Islam and Modernity”
  - courses: RELS 335 ⟵ “RELS 335 - Islam, Sexuality, and Gender”
### `e8d35c1242bbb76d` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-painting-practices [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 360 ⟵ “ART 360 - Painting”
  - courses: ART 361 ⟵ “ART 361 - Painting”
  - courses: ART 460 ⟵ “ART 460 - Painting”
  - courses: ART 461 ⟵ “ART 461 - Painting”
  - courses: ART 462 ⟵ “ART 462 - Painting”
  - courses: ART 463 ⟵ “ART 463 - Senior Painting Studio I”
  - courses: ART 464 ⟵ “ART 464 - Senior Painting Studio II”
  - courses: ART 465 ⟵ “ART 465 - Advanced Senior Painting Studio I”
  - courses: ART 466 ⟵ “ART 466 - Advanced Senior Painting Studio II”
### `ea8c3bffa7fda8df` Western Kentucky University — degree_requirements 2026-27 · program_key=dance-bachelor-of-arts-630p-630 · requirement_key=program-requirements-46-hours-the-following-courses-are-required [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/dance-ba/ (sha256 f4f5bd40773f)
- issues: requirement_groups_skipped
  - courses: PERF 175 ⟵ “PERF 175 - University Experience: Performing Arts”
  - courses: PERF 120 ⟵ “PERF 120 - Rehearsal and Production”
  - courses: PERF 220 ⟵ “PERF 220 - Production Lab I (take once as a 1 credit class, or twice as a .5 credit class)”
### `ea97525d9fa41b66` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=graphic-design-concentration-upper-level-art-history-requirements [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 334 ⟵ “ART 334 - Survey of Graphic Design”
  - courses: ART 305 ⟵ “ART 305 - Ancient Greek and Roman Art”
  - courses: ART 312 ⟵ “ART 312 - Art of the United States to 1865”
  - courses: ART 313 ⟵ “ART 313 - Art of the United States Since 1865”
  - courses: ART 314 ⟵ “ART 314 - Southern Baroque Art”
  - courses: ART 315 ⟵ “ART 315 - Northern Baroque Art”
  - courses: ART 316 ⟵ “ART 316 - Medieval Art & Architecture”
  - courses: ART 317 ⟵ “ART 317 - Art and Power”
  - courses: ART 318 ⟵ “ART 318 - Art and Landscape”
  - courses: ART 325 ⟵ “ART 325 - Art of Asia, Africa, and the Americas”
  - courses: ART 390 ⟵ “ART 390 - Contemporary Art”
  - courses: ART 395 ⟵ “ART 395 - A Cultural History of Alcohol”
  - courses: ART 401 ⟵ “ART 401 - Art of the Italian Renaissance”
  - courses: ART 403 ⟵ “ART 403 - Northern Renaissance Art”
  - courses: ART 405 ⟵ “ART 405 - Art Theory and Criticism”
  - courses: ART 407 ⟵ “ART 407 - Islamic Art and Architecture”
  - courses: ART 408 ⟵ “ART 408 - European Art, 1700-1848”
  - courses: ART 409 ⟵ “ART 409 - European Art, 1848-1900”
  - courses: ART 410 ⟵ “ART 410 - European Art, 1900-1945”
  - courses: ART 445 ⟵ “ART 445 - American Architectural History”
  - courses: ART 494 ⟵ “ART 494 - Seminar in Art History”
### `eb3016a5305f4ec8` Western Kentucky University — degree_requirements 2026-27 · program_key=spanish-bachelor-of-arts · requirement_key=spanish-for-legal-professionals-concentration [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/modern-languages/spanish-ba/ (sha256 ba99e84e2ec8)
- issues: course_alternatives_in_rule_text
  - courses: SPAN 345 ⟵ “SPAN 345 - Topics in Spanish”
  - courses: SPAN 470 ⟵ “SPAN 470 - Advanced Oral Spanish”
  - courses: PLS 200 ⟵ “PLS 200 - Legal Ethics”
  - courses: PLS 225 ⟵ “PLS 225 - Introduction to Law”
  - courses: SPAN 389 ⟵ “SPAN 389 - Internship in Spanish”
  - courses: SPAN 331 ⟵ “SPAN 331 - Spanish for Professional Communication”
  - courses: SPAN 455 ⟵ “SPAN 455 - Topics in Hispanic Literary and Cultural Studies”
  - courses: SPAN 480 ⟵ “SPAN 480 - Translation and Interpreting”
  - courses: PLS 296 ⟵ “PLS 296 - Family Law”
### `ecdfbbf4a566b37e` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-arts-bachelor-of-fine-arts-514p-514 · requirement_key=studio-concentration-weaving [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-arts-bfa/ (sha256 b92c44b48e83)
- issues: requirement_groups_skipped
  - courses: ART 380 ⟵ “ART 380 - Weaving”
  - courses: ART 381 ⟵ “ART 381 - Weaving”
  - courses: ART 480 ⟵ “ART 480 - Weaving”
  - courses: ART 481 ⟵ “ART 481 - Weaving”
  - courses: ART 482 ⟵ “ART 482 - Weaving”
  - courses: ART 483 ⟵ “ART 483 - Senior Fiber Techniques”
  - courses: ART 484 ⟵ “ART 484 - Senior Fiber Composition”
  - courses: ART 485 ⟵ “ART 485 - Advanced Senior Fiber Techniques”
  - courses: ART 486 ⟵ “ART 486 - Advanced Senior Fiber Composition”
### `edd136d6765cec99` Western Kentucky University — degree_requirements 2026-27 · program_key=accounting-bachelor-of-science · requirement_key=program-requirements-75-hours-business-foundations-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/business/accounting/accounting-bs/ (sha256 5dadf9a49ed6)
- issues: course_alternatives_in_rule_text
  - courses: MATH 123 ⟵ “MATH 123 - Mathematical Applications for Business *”
  - courses: ACCT 110 ⟵ “ACCT 110 - Accounting for Decision Makers”
  - courses: ECON 202 ⟵ “ECON 202 - Principles of Economics (Micro)”
  - courses: ECON 206 ⟵ “ECON 206 - Statistics”
  - courses: FIN 330 ⟵ “FIN 330 - Principles of Finance”
  - courses: BDAN 250 ⟵ “BDAN 250 - Introduction to Analytics”
  - courses: MGT 210 ⟵ “MGT 210 - Organization and Management”
  - courses: MKT 220 ⟵ “MKT 220 - Basic Marketing Concepts”
  - courses: MGT 498 ⟵ “MGT 498 - Strategy and Policy”
### `f1db938f6d20f3f6` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-journalism-and-photography-bachelor-of-arts-752p-752 · requirement_key=photojournalism-and-documentary-concentration-required-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/media-communication/visual-journalism-photography-ba/ (sha256 55cb5defcc5a)
- issues: course_alternatives_in_rule_text
  - courses: JOUR 202 ⟵ “JOUR 202 - Introduction to News Writing”
  - courses: SMC 301 ⟵ “SMC 301 - Mass Communication Law and Ethics”
  - courses: VJP 339 ⟵ “VJP 339 - Visual Media Business Practices”
  - courses: VJP 431 ⟵ “VJP 431 - Advanced Photojournalism *”
  - courses: VJP 436 ⟵ “VJP 436 - Photojournalism and Documentary Projects”
### `f2416f259cb89c8a` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=performing-arts-core-design-production-9-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped
  - courses: THEA 219 ⟵ “THEA 219 - Design I”
  - courses: PERF 120 ⟵ “PERF 120 - Rehearsal and Production”
  - courses: PERF 220 ⟵ “PERF 220 - Production Lab I (taken once as 1 credit class, or twice as .5 credit class)”
  - courses: PERF 320 ⟵ “PERF 320 - Production Lab II (taken once as 1 credit class, or twice as .5 credit class)”
  - courses: THEA 222 ⟵ “THEA 222 - Stagecraft”
  - courses: THEA 241 ⟵ “THEA 241 - Costume Technology”
  - courses: THEA 250 ⟵ “THEA 250 - Stage Electrics”
  - courses: THEA 311 ⟵ “THEA 311 - Stage Management”
### `f40a49a8f0acf12a` Western Kentucky University — degree_requirements 2026-27 · program_key=professional-legal-studies-bachelor-of-arts · requirement_key=program-requirements-42-hours-electives-12-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/political-science/paralegal-studies-ba/ (sha256 9c6c23742c44)
- issues: course_alternatives_in_rule_text
  - courses: PLS 280 ⟵ “PLS 280 - Contract Law”
  - courses: PLS 282 ⟵ “PLS 282 - Tort Law”
  - courses: PLS 294 ⟵ “PLS 294 - Administrative Practice and Procedures”
  - courses: PLS 324 ⟵ “PLS 324 - Women and the Law”
  - courses: PLS 350 ⟵ “PLS 350 - Evidence”
  - courses: PLS 360 ⟵ “PLS 360 - Debtor Creditor Relations”
  - courses: PLS 375 ⟵ “PLS 375 - Comparative Legal Systems”
  - courses: PLS 381 ⟵ “PLS 381 - Alternative Dispute Resolution Methods and Practices”
  - courses: PLS 392 ⟵ “PLS 392 - Corporate Law”
  - courses: PLS 395 ⟵ “PLS 395 - Estate Planning and Administration”
  - courses: CRIM 330 ⟵ “CRIM 330 - Criminology”
  - courses: CRIM 332 ⟵ “CRIM 332 - Juvenile Delinquency”
  - courses: CRIM 380 ⟵ “CRIM 380 - Punishment and Society”
  - courses: CRIM 432 ⟵ “CRIM 432 - Sociology of Criminal Law”
  - courses: PS 220 ⟵ “PS 220 - Judicial Process”
  - courses: PS 304 ⟵ “PS 304 - State Government”
  - courses: PS 311 ⟵ “PS 311 - Public Policy”
  - courses: PS 316 ⟵ “PS 316 - The Legislative Process”
  - courses: PS 326 ⟵ “PS 326 - Constitutional Law”
  - courses: PS 355 ⟵ “PS 355 - International Organization and Law”
  - courses: PS 412 ⟵ “PS 412 - Kentucky Government and Politics”
  - courses: HIST 445 ⟵ “HIST 445 - American Legal History to 1865”
  - courses: HIST 446 ⟵ “HIST 446 - American Legal History Since 1865”
### `f5c809f9ed9271f2` Western Kentucky University — degree_requirements 2026-27 · program_key=dance-bachelor-of-arts-630p-630 · requirement_key=program-requirements-46-hours-choreography-8-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/dance-ba/ (sha256 f4f5bd40773f)
- issues: requirement_groups_skipped
  - courses: DANC 235 ⟵ “DANC 235 - Dance Improvisation”
  - courses: DANC 310 ⟵ “DANC 310 - Choreography I”
  - courses: DANC 420 ⟵ “DANC 420 - Choreography II”
### `f7f03dc194675ada` Western Kentucky University — degree_requirements 2026-27 · program_key=performing-arts-bachelor-of-fine-arts-588p-588 · requirement_key=theatre-concentration-production-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/theatre-dance/performing-arts-bfa/ (sha256 966227be8366)
- issues: requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THEA 222 ⟵ “THEA 222 - Stagecraft”
  - courses: PERF 321 ⟵ “PERF 321 - Production Lab III”
### `f8d34cb793132267` Western Kentucky University — degree_requirements 2026-27 · program_key=history-bachelor-of-arts-695e-695 · requirement_key=program-requirements-33-48-hours-historical-research [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/history-ba/ (sha256 43a285b4294b)
- issues: requirement_groups_skipped
  - courses: HIST 498 ⟵ “HIST 498 - Senior Seminar”
### `f9820a5cfe43f75c` Western Kentucky University — degree_requirements 2026-27 · program_key=user-experience-bachelor-of-science · requirement_key=program-requirements-57-hours-advanced-psychological-science-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/user-experience-bs/ (sha256 eed3996a11f0)
- issues: course_alternatives_in_rule_text
  - courses: PSYS 333 ⟵ “PSYS 333 - Cognitive Psychology”
### `fa8c2e188c025529` Western Kentucky University — degree_requirements 2026-27 · program_key=asian-studies-bachelor-of-arts · requirement_key=program-requirements-30-hours-history-and-politics-6-hours [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/history/asian-studies-ba/ (sha256 d4bf15768a8d)
- issues: requirement_groups_skipped
  - courses: HIST 351 ⟵ “HIST 351 - Asian American History”
  - courses: HIST 370 ⟵ “HIST 370 - Modern South Asia: from Empires to Nations”
  - courses: HIST 378 ⟵ “HIST 378 - History of Yoga: Tradition, Literature, Practice”
  - courses: HIST 379 ⟵ “HIST 379 - Gandhi: The Creation of a Global Legacy”
  - courses: HIST 449 ⟵ “HIST 449 - Korea and Vietnam”
  - courses: HIST 460 ⟵ “HIST 460 - Traditional East Asia”
  - courses: HIST 461 ⟵ “HIST 461 - Modern East Asia”
  - courses: HIST 462 ⟵ “HIST 462 - History of the Middle East”
  - courses: HIST 466 ⟵ “HIST 466 - The Arab-Israeli Conflict: Local and Global Influences”
  - courses: HIST 471 ⟵ “HIST 471 - Modern China”
  - courses: HIST 472 ⟵ “HIST 472 - Modern Japan”
  - courses: IA 352 ⟵ “IA 352 - International Relations of the Middle East”
  - courses: PS 359 ⟵ “PS 359 - Politics of North Korea”
  - courses: IA 364 ⟵ “IA 364 - Chinese Politics”
  - courses: IA 365 ⟵ “IA 365 - Government and Politics of the Middle East”
  - courses: PS 366 ⟵ “PS 366 - Government and Politics in East Asia”
### `fc8c0bb6c84cb1f7` Western Kentucky University — degree_requirements 2026-27 · program_key=visual-studies-bachelor-of-arts · requirement_key=studio-concentration-required-foundation-courses [new] (labeled_in_source)
- source: https://catalog.wku.edu/undergraduate/arts-letters/art/visual-studies-ba/ (sha256 fcd2c45cf314)
- issues: course_alternatives_in_rule_text
  - courses: ART 105 ⟵ “ART 105 - History of Art to 1300”
  - courses: ART 106 ⟵ “ART 106 - History of Art Since 1300”
  - courses: ART 130 ⟵ “ART 130 - Two-Dimensional Design Foundations”
  - courses: ART 131 ⟵ “ART 131 - Three-Dimensional Design Foundations”
  - courses: ART 140 ⟵ “ART 140 - Drawing Foundations I”
  - courses: ART 220 ⟵ “ART 220 - Ceramics”
  - courses: ART 231 ⟵ “ART 231 - Graphic Design I: Typography”
  - courses: ART 240 ⟵ “ART 240 - Drawing Foundations II”
  - courses: ANIM 210 ⟵ “ANIM 210 - Introduction to Computer Animation”
  - courses: ART 250 ⟵ “ART 250 - Printmaking”
  - courses: ART 260 ⟵ “ART 260 - Painting”
  - courses: ART 270 ⟵ “ART 270 - Sculpture Survey I”
  - courses: ART 280 ⟵ “ART 280 - Weaving”
  - courses: UX 220 ⟵ “UX 220 - Introduction to User Experience Design”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 135; pages by category: admissions_tests 14, aid_appeals 3, ap_credit 3, clep_credit 3, cost_of_attendance 7, degree_requirements 4, dual_enrollment 19, ib_credit 3, merit_scholarships 23, residency 37, statewide_articulation 3, transfer_credit 12, tuition_fees 32

## Blocked by the site (every request refused; needs the browser fallback)

- Midway University (`ipeds-157377`)
- Morehead State University (`ipeds-157386`)

## Leads: official pages found with no extracted record

- Alice Lloyd College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Asbury University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Ashland Community and Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Bellarmine University: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Berea College: admissions_tests, merit_scholarships
- Big Sandy Community and Technical College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- Bluegrass Community and Technical College: admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Brescia University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, degree_requirements
- Campbellsville University: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Centre College: cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Clear Creek Baptist Bible College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Eastern Kentucky University: tuition_fees, cost_of_attendance, admissions_tests, ib_credit, transfer_credit, residency
- Elizabethtown Community and Technical College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency
- Gateway Community and Technical College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency
- Georgetown College: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Hazard Community and Technical College: admissions_tests, merit_scholarships, transfer_credit, degree_requirements, aid_appeals
- Henderson Community College: admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency
- Hopkinsville Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, degree_requirements
- Jefferson Community and Technical College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, degree_requirements
- Kentucky Christian University: admissions_tests, merit_scholarships, transfer_credit
- Kentucky Mountain Bible College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Kentucky State University: tuition_fees, cost_of_attendance, merit_scholarships, transfer_credit, residency
- Kentucky Wesleyan College: admissions_tests, merit_scholarships, transfer_credit, residency
- Lindsey Wilson College: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Madisonville Community College: admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit
- Maysville Community and Technical College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit
- Murray State University: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Northern Kentucky University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, dual_enrollment, transfer_credit, residency, aid_appeals
- Owensboro Community and Technical College: admissions_tests, merit_scholarships, ap_credit, transfer_credit, aid_appeals
- Simmons College of Kentucky: cost_of_attendance, admissions_tests, merit_scholarships, aid_appeals
- Somerset Community College: admissions_tests, merit_scholarships, clep_credit, transfer_credit, residency, degree_requirements, aid_appeals
- Southcentral Kentucky Community and Technical College: admissions_tests, merit_scholarships, ap_credit, transfer_credit, residency
- Southeast Kentucky Community & Technical College: admissions_tests, merit_scholarships, transfer_credit
- Spalding University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- The Southern Baptist Theological Seminary: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, degree_requirements
- Thomas More University: admissions_tests, transfer_credit, degree_requirements
- Transylvania University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Union College: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- University of Kentucky: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- University of Louisville: admissions_tests, transfer_credit, residency
- University of Pikeville: clep_credit, dual_enrollment, transfer_credit, residency
- University of the Cumberlands: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency, degree_requirements
- West Kentucky Community and Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- Western Kentucky University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment
