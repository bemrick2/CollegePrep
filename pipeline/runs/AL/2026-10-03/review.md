# Review queue — AL (2026-27)

Pages fetched: 3395; failures: 308. Candidates: 531 (121 without issues, 410 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 2 | 19 | 26 | 1 | 5 |
| cost_of_attendance | 0 | 0 | 2 | 11 | 33 | 2 | 5 |
| admissions_tests | 0 | 0 | 0 | 0 | 46 | 2 | 5 |
| common_data_set | 0 | 0 | 0 | 0 | 8 | 40 | 5 |
| merit_scholarships | 0 | 0 | 10 | 2 | 34 | 2 | 5 |
| ap_credit | 0 | 0 | 6 | 3 | 11 | 28 | 5 |
| clep_credit | 0 | 0 | 6 | 4 | 6 | 32 | 5 |
| ib_credit | 0 | 0 | 3 | 1 | 5 | 39 | 5 |
| dual_enrollment | 0 | 0 | 22 | 3 | 12 | 11 | 5 |
| transfer_credit | 0 | 0 | 12 | 1 | 32 | 3 | 5 |
| statewide_articulation | 0 | 0 | 0 | 0 | 11 | 37 | 5 |
| residency | 0 | 0 | 0 | 0 | 36 | 12 | 5 |
| degree_requirements | 0 | 0 | 0 | 0 | 40 | 8 | 5 |
| aid_appeals | 0 | 0 | 0 | 32 | 8 | 8 | 5 |

## Ready for review (121)

### `2c556ff522ebd661` Alabama A & M University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.aamu.edu/admissions-aid/undergraduate-admissions/dual-enrollment.html (sha256 c554a3395456)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “GPA Requirement: A minimum 2.5 GPA is required.”
### `70310af2070afa57` Alabama A & M University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.aamu.edu/admissions-aid/undergraduate-admissions/transfer-student.html (sha256 134f205435a6)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “For example: Only courses with grades of C or better may transfer for ENG 101/102 as a C or better is required in ENG 101/102 for all programs at Alabama A&M University.”
  - min_grade: C ⟵ “Only a grade of C or better is accepted for transfer of MTH 112 for all business programs, but a D or better is accepted for transfer of MTH 112 for social science programs.”
### `45379ec2b0c0fc59` Alabama State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.alasu.edu/admissions/early-college.php (sha256 3953329424f7)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.5 ⟵ “You must have a high school GPA of 2.5 or above;”
  - eligibility_tier: 2.5 ⟵ “A cumulative grade point average of 2.5”
### `43087ca26d0a0cc5` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 bd4db3189d2a)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Achievement Scholarship | ACT 23 / SAT 1130 | 3.0 | $20,000 | $5,000”
### `94b65d58445c9d1b` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 0bbb7cc6f6cb)
- checks: {"thresholds": {"gpa_min": 2.3}}
  - gpa_requirement: 2.3 ⟵ “Opportunity Scholarship | ACT 18 / SAT 940 | 2.3 | $12,000 | $3,000”
### `a2d955a4a4edbc23` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 bd4db3189d2a)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “AUM State Scholarship** Apply Now. | ACT 20 / SAT 1020 | 3.0 | Varies | Varies”
### `b5cb3a71e5b076f4` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 0bbb7cc6f6cb)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Principal Scholarship | ACT 29 / SAT 1350 | 3.0 | $36,000 | $9,000”
### `c532c11746b2d815` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 0bbb7cc6f6cb)
- checks: {"thresholds": {"gpa_min": 2.3}}
  - gpa_requirement: 2.3 ⟵ “Bridge Incentive Scholarship | N/A | 2.3 | $6,000 | $1,500”
### `d787fcee57ccd698` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 0bbb7cc6f6cb)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Outstanding Scholars Award | ACT 30 / SAT 1400 | 3.0 | $40,000 | $10,000”
### `dc88756f50865d25` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 8a819e09c999)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “GPA Opportunity Scholarship | N/A | 3.0 | $8,000 | $2,000”
### `e16cec598adc9d14` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 bd4db3189d2a)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Recognition Scholarship | ACT 20 / SAT 1020 | 3.0 | $16,000 | $4,000”
### `e94c49438a4d98a4` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 bd4db3189d2a)
- checks: {"thresholds": {"gpa_min": 2.0}}
  - gpa_requirement: 2.0 ⟵ “Bridge Advantage Scholarship | N/A | 2.0 | $4,000 | $1,000”
### `f8d9340a314994eb` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 bd4db3189d2a)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Vice Principal Scholarship | ACT 28 / SAT 1310 | 3.0 | $32,000 | $8,000”
### `fd58d482a39a76de` Auburn University at Montgomery — awards 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/scholarships-and-financial-aid/scholarships/ (sha256 bd4db3189d2a)
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Warhawk Scholarship | ACT 25 / SAT 1200 | 3.0 | $24,000 | $6,000”
### `97243f1b97638723` Auburn University at Montgomery — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.aum.edu/admissions/tuition-and-fees/ (sha256 30bf83ebe9e1)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Estimated Tuition/Fees*: 24406 ⟵ “Estimated Tuition/Fees* | $11,666 | $24,406”
  - on_campus:Estimated Loan Fees: 119 ⟵ “Estimated Loan Fees | $119 | $119”
  - on_campus:Books, Supplies, & Equipment: 2500 ⟵ “Books, Supplies, & Equipment | $2,500 | $2,500”
  - on_campus:Miscellaneous/Personal: 1890 ⟵ “Miscellaneous/Personal | $1,890 | $1,890”
  - on_campus:Transportation: 3625 ⟵ “Transportation | $3,263 | $3,625”
  - on_campus:Housing & Food: 19368 ⟵ “Housing & Food | $19,368 | $19,368”
  - on_campus:Total: 51908 ⟵ “Total | $38,806 | $51,908”
### `f0369ec8a57b9154` Auburn University at Montgomery — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.aum.edu/admissions/tuition-and-fees/ (sha256 30bf83ebe9e1)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Estimated Tuition/Fees*: 11666 ⟵ “Estimated Tuition/Fees* | $11,666 | $24,406”
  - on_campus:Estimated Loan Fees: 119 ⟵ “Estimated Loan Fees | $119 | $119”
  - on_campus:Books, Supplies, & Equipment: 2500 ⟵ “Books, Supplies, & Equipment | $2,500 | $2,500”
  - on_campus:Miscellaneous/Personal: 1890 ⟵ “Miscellaneous/Personal | $1,890 | $1,890”
  - on_campus:Transportation: 3263 ⟵ “Transportation | $3,263 | $3,625”
  - on_campus:Housing & Food: 19368 ⟵ “Housing & Food | $19,368 | $19,368”
  - on_campus:Total: 38806 ⟵ “Total | $38,806 | $51,908”
### `a82f88eedb752e70` Auburn University at Montgomery — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.aum.edu/admissions/admissions-programs/dual-enrollment/ (sha256 a546d6f2e2c9)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges"], "tiers": 1}
  - per_credit_hour_charge: 133 ⟵ “The dual enrollment tuition rate is $133 per credit hour. Students will receive a scholarship that reduces the net cost to $50 per credit hour.”
  - per_credit_hour_charge: 50 ⟵ “The dual enrollment tuition rate is $133 per credit hour. Students will receive a scholarship that reduces the net cost to $50 per credit hour.”
  - eligibility_tier: 3.0 ⟵ “You must have a high school GPA of 3.0 or above;”
  - per_credit_hour_charge: 50 ⟵ “Tuition will be $50 per credit hour for partner high schools and $100 per credit hour for non-partner high schools. This amount does not include your textbook(s).”
  - per_credit_hour_charge: 100 ⟵ “Tuition will be $50 per credit hour for partner high schools and $100 per credit hour for non-partner high schools. This amount does not include your textbook(s).”
### `9ee6a597584db4da` Auburn University at Montgomery — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.aum.edu/transfer/ (sha256 1c03046c5a56)
- checks: {"fields": ["min_grade"]}
  - min_grade: D ⟵ “As a general rule, grades of D or better are required for credit to transfer, though some programs may have stricter standards and only accept courses in which a C or better was earned.”
### `m945e229710f797e` Bishop State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.bishop.edu/programs/dual-enrollment/accelerated-high-school (sha256 081fe029ddce)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Unweighted GPA of 3.0 or greater”
  - eligibility_tier: 2.5 ⟵ “Students must have a minimum cumulative (unweighted) grade point average (GPA) of 2.5 on a 4.0 scale.”
### `m479613cd884c72b` Central Alabama Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.cacc.edu/academic-transfer-programs (sha256 b11e37b8e3b8)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - residency_requirement_credits: 12 ⟵ “The transcript will read “Admitted on Academic Probation.” The student will retain this status until the student has attempted at least 12 credit hours at the College.”
  - max_transfer_credits: 64 ⟵ “A student who has earned an Associate in Arts or Associate in Science degree and possesses a minimum cumulative GPA of 2.0 from CACC may be eligible for admission to AUM with up to a maximum of 64 semester hours transferring.”
### `5fa368fee326a1aa` Chattahoochee Valley Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.cv.edu/wp-content/uploads/2025/08/Dual-Enrollment-Checklist-and-forms-2025.pdf (sha256 a07bac05fda7)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.5 ⟵ “                  2.    Copy of high school transcripts indicating at least a 2.5 GPA.”
  - eligibility_tier: 2.5 ⟵ “• Must have a minimum cumulative 2.5 GPA (Career Tech and Academic students)”
### `55e53dc0853fd3ec` Coastal Alabama Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/apply/transfer-students-apply (sha256 1cd7197d33d6)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer students admitted on academic probation will have only course grades of “C” or better accepted for transfer.”
### `62c10f122c6c70c4` Enterprise State Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://escc.edu/paying-for-college/cost-of-attendance/ (sha256 0ce447d46c2f)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 9870.0 ⟵ “Tuition & Fees | $4935.00 | $9870.00 | $14805.00”
  - column:Housing & Food: 7694.0 ⟵ “Housing & Food | $3847.00 | $7694.00 | $10259.00”
  - column:Books, Supplies, & Equipment: 3000.0 ⟵ “Books, Supplies, & Equipment | $1500.00 | $3000.00 | $4500.00”
  - column:Transportation: 2150.0 ⟵ “Transportation | $1075.00 | $2150.00 | $2870.00”
  - column:Miscellaneous: 1290.0 ⟵ “Miscellaneous | $645.00 | $1290.00 | $1722.00”
  - column:Loan Fees: 100.0 ⟵ “Loan Fees | $50.00 | $100.00 | $130.00”
  - column:Total: 24104 ⟵ “Total | $12052 | $24104 | $34286”
### `eb1b58f654ddff6e` Enterprise State Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://escc.edu/paying-for-college/cost-of-attendance/ (sha256 0ce447d46c2f)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 5880.0 ⟵ “Tuition & Fees | $2940.00 | $5880.00 | $8820.00”
  - column:Housing & Food: 7694.0 ⟵ “Housing & Food | $3847.00 | $7694.00 | $10259.00”
  - column:Books, Supplies, & Equipment: 3000.0 ⟵ “Books, Supplies, & Equipment | $1500.00 | $3000.00 | $4500.00”
  - column:Transportation: 2150.0 ⟵ “Transportation | $1075.00 | $2150.00 | $2870.00”
  - column:Miscellaneous: 1290.0 ⟵ “Miscellaneous | $645.00 | $1290.00 | $1722.00”
  - column:Loan Fees: 100.0 ⟵ “Loan Fees | $50.00 | $100.00 | $130.00”
  - column:Total: 20114.0 ⟵ “Total | $10057.00 | $20114.00 | $28301.00”
### `aad77e9a9a4b8fed` Enterprise State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://escc.edu/dual-enrollment/counselors/ (sha256 415b9f4cb1d7)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.5 ⟵ “ESCC Cords of Distinction: Students who complete 15 credit hours of ESCC courses by the end of the Spring semester of their senior year of high school and maintain a 3.5 GPA will qualify. This prestigious award will recognize students’ hard work during their time in high school and the Dual Enrollme”
### `ddeee0be6ae49704` Enterprise State Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://escc.edu/scholarships/ (sha256 aa140425df68)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 24 ⟵ “Awarded fall and spring semesters Merit Available to high school seniors without any dual enrollment courses with a competitive high school GPA Covers 24 credit hours of tuition and applicable fee per academic year Awarded fall and spring semesters Current and past ESCC students must have completed at least 24 semester credit hours at ESCC and have earned at least a cumulative 3.0 GPA to qualify.”
### `m02434c75b60e878` Gadsden State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.gadsdenstate.edu/admissions-aid/dual-enrollment (sha256 170efd5e0d59)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 2.5 ⟵ “Students with a 2.5 cumulative GPA on a 4.0 scale OR a 2.0 for approved technical programs only”
  - eligibility_tier: 2.5 ⟵ “Students must have at least a 2.5 GPA to participate in academic courses.”
  - eligibility_tier: 2.5 ⟵ “Students must have a 2.5 or higher GPA average (2.0 for approved technical programs only) unweighted on a 4.0 scale, as defined by the local board of education policy, in completed high school courses.”
### `321ed14506752c22` George C Wallace State Community College-Hanceville — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.wallacestate.edu/admissions/credit-for-non-traditional-learning.html (sha256 6e532163c861)
- checks: {"distinct_exams": 4, "equivalencies": 4, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|5050505050]:  ⟵ “American Literature College Comp Modular without EssayCollege CompEnglish LiteratureHumanities | 5050505050 | ENG 251 & 252ENG 101ENG 101 & 102ENG 261 & 262HUM 101 | 63663”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|5050505050]:  ⟵ “BiologyCalculusCollege AlgebraCollege MathematicsPrecalculus | 5050505050 | BIO 103MTH 125MTH 100MTH 116MTH 112 | 44333”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50505065]:  ⟵ “German Language Level 1Spanish Language Level 1Spanish with Writing Level 1Spanish with Writing Level 2 | 50505065 | GRN 101 & 102SPA 101 & 102SPA 101SPA 101 | 88612”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|505050]:  ⟵ “Business Law, IntroManagement, PrinciplesMarketing, Principles | 505050 | BUS 261BUS 275BUS 285 | 333”
### `4bbcf13e99a04892` George C Wallace State Community College-Hanceville — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.wallacestate.edu/deoptions/forms/DE_Agreement_Form_r1.pdf (sha256 1d6b2801370a)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “• Unweighted 2.5 high school GPA.”
### `2b1fcac6f25518b8` George C Wallace State Community College-Selma — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://catalog.wccs.edu/dual-enrollmentdual-credit-for-high-school-students (sha256 e97881fd5855)
- checks: {"fields": ["min_hs_gpa"], "tiers": 2}
  - eligibility_tier: 2.5 ⟵ “The student must have a 2.5 GPA or higher in completed high school courses;”
  - eligibility_tier: 2.5 ⟵ “The student must be in the 10th, 11th or 12th grade, have a 2.5 GPA or higher, and have approval from”
### `5bf5fbc1cc68f811` George C Wallace State Community College-Selma — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.wccs.edu/credit-from-nontraditional-sources (sha256 8a6c6493d1db)
- checks: {"distinct_exams": 12, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POL 211 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 251 | 3”
  - equivalencies[CLEP-BIOLOGY|49]:  ⟵ “Biology | 49 | BIO 103 | 3”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|49]:  ⟵ “College Algebra | 49 | MTH112 | 3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition (with essay) | 50 | ENG101 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|49]:  ⟵ “English Literature | 49 | ENG 261 | 3”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “General Chemistry | 50 | CHM 111 | 4”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “General Psychology | 50 | PSY 200 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Introduction to Business Management | 50 | BUS275 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Introduction to Macroeconomics | 50 | ECO 231 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Introduction to Marketing | 50 | BUS 285 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introduction to Sociology | 50 | SOC2CO | 3”
### `6887c8e6e257700e` H Councill Trenholm State Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.trenholmstate.edu/clep-table (sha256 1eddfabadcfd)
- checks: {"distinct_exams": 24, "equivalencies": 28, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | POL 211”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 | 3 | HIS 201”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | 50 | 3 | HIS 202”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PSY 210”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | PSY 200”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | SOC 200”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 | ECO 231”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 | ECO 232”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | 3 | HIS 101”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present | 50 | 3 | HIS 102”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|Composition and Literature]:  ⟵ “Western Civilization II: 1648 to Present | Composition and Literature”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 | ENG 251 and ENG 252”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 | ENG 102”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 | ENG 101”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 6 | ENG 261 and ENG 262”
  - equivalencies[CLEP-ENGLISH-LITERATURE|Science and Mathematics]:  ⟵ “English Literature | Science and Mathematics”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 8 | BIO 101 and BIO 102 or BIO 103 and BIO 104”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 4 | MTH 125”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 4 | CHM 104”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | MTH 100”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | MTH 110”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 6 | MTH 112 and MTH 113”
  - equivalencies[CLEP-PRECALCULUS|Business]:  ⟵ “Precalculus | Business”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BUS 263”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 | BUS 275”
  - … 3 more rows
### `74971e6606b1d636` H Councill Trenholm State Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://catalog.trenholmstate.edu/advanced-placement-table (sha256 c3ddecf5516e)
- checks: {"distinct_exams": 19, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIO 101 or BIO 103”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | MTH 125”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 8 | MTH 125 and MTH 126”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHM 104”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | 3 | 3 | POL 200”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | 3 | ENG 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | 3 | ENG 101”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 3 | HIS 101”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 3 | ECO 231”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 3 | ECO 232”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | 4 | MUS 111”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus | 3 | 8 | MTH 112 and MTH 113”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | 3 | PSY 200”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | 3 | MTH 265”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language and Culture | 3 | 6 | SPA 101 and SPA 102”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “Spanish Literature and Culture | 3 | 6 | SPA 101 and SPA 102”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government and Politics | 3 | 3 | POL 211”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History | 3 | 3 | HIS 201”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History: Modern | 3 | 3 | HIS 122”
### `m2b07944f1ba5a0c` H Councill Trenholm State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.trenholmstate.edu/dual-enrollment/ (sha256 e9a8214abb57)
- checks: {"fields": ["state_grant_accepted"], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 2.0 ⟵ “The student must be in the 10th, 11th, or 12th grade and have a 2.0 GPA or higher for most technical programs. Approval from the high school principal and counselor or the home school director is also required.”
  - eligibility_tier: 2.5 ⟵ “Have a minimum cumulative GPA of 2.5 (unweighted for academic/STEM courses) and a minimum cumulative GPA of 2.0 (unweighted for CTE courses)”
  - eligibility_tier: 2.5 ⟵ “For re-entry, the student must reapply to the program and meet the minimum cumulative GPA of 2.5 (unweighted for academic/STEM courses) and a minimum cumulative GPA of 2.0 (unweighted for CTE courses).”
  - state_grant_accepted: True ⟵ “Dual enrollment scholarship funds may be used to cover tuition, textbooks, and supplies depending on the availability of funds, the needs of the individual student, and the requirements of the technical classes. The scope of each scholarship is determined by available funding and the scholarship gra”
  - state_grant_accepted: True ⟵ “The following programs are eligible for funding with the Dual Enrollment Scholarship.”
### `m2b19dec5efe771b` H Councill Trenholm State Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://catalog.trenholmstate.edu/general-principles-of-transfer-credit (sha256 e6a021a6cb9b)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “The College will accept courses completed at other duly accredited colleges for transfer credit only when the student earned a passing grade of “C” or higher in the course and the course is part of the student’s degree plan at Trenholm.”
  - min_grade: C ⟵ “The College will accept courses completed at other duly accredited colleges for transfer credit only when the student earned a passing grade of “C” or higher in the course and the course is part of the student’s degree plan at Trenholm.”
### `1c65d2b4af480c2d` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: Varies, up to $9,000 ⟵ “Huntingdon Grant | Varies, up to $9,000 | Must meet admission requirements.”
### `3b7057df6437044d` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “Corporate Alliance Award | $12,500 | Employee or employee dependent of a parent/guardian employed by Alabama Power, ALFA, Baptist Health, Synovus Bank, or UBS Financial Services.Corporate Alliance Application required (see Student Financial Services Forms.)”
### `46c0af5ce3ea5e18` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “President John Massey Scholarship | $12,500 | 21 ACT/3.20 GPA or 3.40 GPA without test scoresFreshmen only”
### `48a307ddac607025` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “President A.A. Lipscomb Scholarship | $14,000 | 24 ACT/3.50 GPA or 3.70 GPA without test scoresFreshmen only”
### `4c0f0ef2fd088a66` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “Military and Dependent Survivor Award | $12,500 | Must provide military ID.Complete the required application at Student Financial Services Forms.”
### `59964fc8f55823f4` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “River Region Award | $12,500 | Must live within 45 miles of the Huntingdon campus.”
### `680b41246b106cb6` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $20,000 ⟵ “Presidential Scholars | $20,000 | 3.0 GPA and 23 ACT or 3.75 GPA with no test scores.Open to incoming freshmen and transfer students with 36 credit hours or less of transfer credit.Campus residency required.Participation in the Presidential Scholars program, including an Academic Cohort, required.Pa”
### `68c2d5b91fc11b96` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $12,000 ⟵ “Hawk Award | $12,000 | Unconditional admission”
### `70308b14c3d1cea3` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 in addition to one other Huntingdon scholarship or award, except for Wilson Scholarships, Presidential Scholars, or Kingswood Initiative. ⟵ “Montgomery Public Schools Investment Scholarship | $3,000 in addition to one other Huntingdon scholarship or award, except for Wilson Scholarships, Presidential Scholars, or Kingswood Initiative. | Incoming freshmen who graduate from Booker T. Washington Magnet, Brewbaker Technology Magnet, Carver, ”
### `7b4e98523beab059` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $13,000 ⟵ “Wynton M. and Carolyn Blount Scholarship | $13,000 | 22 ACT/3.30 GPA or 3.50 GPA without test scoresFreshmen only”
### `7f6a28a1493855d0` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Esports Award | $14,000 | Must participate in Esports.Because of the time commitment for this program, participation in Esports is reserved for those who are not participating in NCAA-III athletic teams, the Kingswood Initiative, Presidential Scholars Program, band, dance, or cheer teams.”
### `9673e81d56e05cf5` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Scarlet & Grey Cheer Award | $14,000 | Limited—must participate in cheer activities as requested.Try-out required.Because of the time commitment for the Cheer program, participation is reserved for those who are not participating in NCAA-III athletic teams, the Presidential Scholars Program, the Kin”
### `abb79319bb541e0d` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “Methodist Award | $12,500 | Active member of a Methodist church for at least one yearMethodist Clergy Referral Form (PDF) required.”
### `b41f10fa1499de76` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “AISA Award | $12,500 | Graduate from an AISA school.”
### `d92e7c0a22dcd25f` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Scarlet & Grey Dance Award | $14,000 | Limited—must participate in dance activities as requested.Try-out required.Because of the time commitment for the dance program, participation is reserved for those who are not participating in NCAA-III athletic teams, the Presidential Scholars Program, the Kin”
### `df0addf85a203c26` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Scarlet & Grey Band Award | $14,000 | Must participate in marching band, jazz/show band, BallHawks Pep Band, and symphonic band for fall and spring semesters as requested.Because of the time commitment for the band program, participation is reserved for those who are not participating in NCAA-III at”
### `df58a791b227e00a` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $13,500 ⟵ “President Walter D. Agnew Scholarship | $13,500 | 23 ACT/3.40 GPA or 3.60 GPA without test scoresFreshmen only”
### `e5c075bac9ef219e` Huntingdon College — awards 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2026-2027-undergraduate-scholarships/ (sha256 ec284ce1dcb9)
- checks: {"thresholds": null}
  - award_amount_text: $16,500 ⟵ “James W. Wilson Jr. Scholarship | $16,500 | 3.75 GPA and 25 ACTFreshman only”
### `59570ba3b8ce7212` Huntingdon College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.huntingdon.edu/academics/office-of-the-registrar/transfer-credit/ (sha256 07ababd22265)
- checks: {"distinct_exams": 29, "equivalencies": 37, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|4+]:  ⟵ “Art 2D Design | 4+ | ARTS 201 | 3 Semester Hours”
  - equivalencies[AP-3-D-ART-DESIGN|4+]:  ⟵ “Art 3D Design | 4+ | ARTS 202 | 3 Semester Hours”
  - equivalencies[AP-ART-HISTORY|3+]:  ⟵ “Art History | 3+ | ARTS1XX | 3 Semester Hours”
  - equivalencies[AP-DRAWING|3+]:  ⟵ “Art Studio (Drawing) | 3+ | ARTS203 | 3 Semester Hours”
  - equivalencies[AP-BIOLOGY|3+]:  ⟵ “Biology | 3+ | BIOL 101 & 103L | 4 Semester Hours”
  - equivalencies[AP-CALCULUS-AB|3+]:  ⟵ “Calculus AB | 3+ | MATH 255 | 3 Semester Hours”
  - equivalencies[AP-CALCULUS-BC|5]:  ⟵ “Calculus BC | 5 | MATH 255 & 256 | 6 Semester Hours”
  - equivalencies[AP-CALCULUS-BC|3 or 4]:  ⟵ “Calculus BC | 3 or 4 | MATH 255 | 3 Semester Hours”
  - equivalencies[AP-CHEMISTRY|4+]:  ⟵ “Chemistry | 4+ | CHEM 105, 115L | 4 Semester Hours”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3+]:  ⟵ “Computer Science A | 3+ | OTHE1XX | 3 Semester Hours”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3+]:  ⟵ “Computer Science Principles | 3+ | OTHE1XX | 3 Semester Hours”
  - equivalencies[AP-MACROECONOMICS|4+]:  ⟵ “Economics - Macro | 4+ | ECON 202 | 3 Semester Hours”
  - equivalencies[AP-MICROECONOMICS|4+]:  ⟵ “Economics - Micro | 4+ | ECON 201 | 3 Semester Hours”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3+]:  ⟵ “English Lang/Comp | 3+ | ENGL 103 & 104 | 6 Semester Hours”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4+]:  ⟵ “English Lit/Comp | 4+ | ENGL 104 & 1XX | 6 Semester Hours”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Lit/Comp | 3 | ENGL 104 | 3 Semester Hours”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3+]:  ⟵ “Environmental Science | 3+ | BIOL 161 | 3 Semester Hours”
  - equivalencies[AP-EUROPEAN-HISTORY|3+]:  ⟵ “European History/Western Civ | 3+ | HIST 101 & 102 | 6 Semester Hours”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4+]:  ⟵ “French Language | 4+ | FREN 101, 102 & 201 | 9 Semester Hours”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language | 3 | FREN 101 & 102 | 6 Semester Hours”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4+]:  ⟵ “German Language | 4+ | GERM 101, 102 & 201 | 9 Semester Hours”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language | 3 | GERM 101 & 102 | 6 Semester Hours”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3+]:  ⟵ “Human Geography | 3+ | OTHE 1XX | 3 Semester Hours”
  - equivalencies[AP-MUSIC-THEORY|5]:  ⟵ “Music Theory | 5 | MUSC 107 & 108 | 4 Semester Hours”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | MUSC 107 | 2 Semester Hours”
  - … 12 more rows
### `mab15263ec3c3b7f` Huntingdon College — transfer_policies 2026-27 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/catalogs/2026-2027-catalog/ (sha256 923096e78c57)
- checks: {"fields": ["max_transfer_credits", "min_grade", "residency_requirement_credits"], "merged_pages": 2}
  - min_grade: D ⟵ “Credit will be granted for any approved course completed with a grade of “D” or better, or in the case of a course taken on a Pass/No Credit basis (or the equivalent), a grade of “P.” The credit granted is indicated on the student’s transcript; however, transferred coursework does not affect a student’s Huntingdon College GPA.”
  - max_transfer_credits: 90 ⟵ “A maximum of 90 semester hours of transfer work may be credited toward the 120-hour degree requirement.”
  - residency_requirement_credits: 30 ⟵ “Students must comply with the College’s Terminal Residency policy (“30 Hour Rule”), which states that not more than one course in the last 30 semester credit hours may be taken outside of Huntingdon College.”
  - residency_requirement_credits: 30 ⟵ “If more than 30 semester credit hours are required, the final 30 semester credit hours must be at Huntingdon College.”
  - max_transfer_credits: 90 ⟵ “A maximum of 90 semester hours of transfer work may be credited toward the 120 hour degree requirement.”
### `mb4a3c6ed5ce5ca5` J. F. Drake State Community and Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://drakestate.edu/admissions/dual-enrollment/ (sha256 dd34fc974035)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 2}
  - eligibility_tier: 2.5 ⟵ “Have a minimum cumulative GPA of 2.5 on a 4.0 scale”
  - eligibility_tier: 2.5 ⟵ “Submit an official high school transcript reflecting GPA of 2.5 or higher.”
  - eligibility_tier: 2.5 ⟵ “Submit an official high school transcript reflecting GPA of 2.5 or higher.”
  - eligibility_tier: 2.5 ⟵ “GPA 2.5 or higher required”
  - eligibility_tier: 2.5 ⟵ “GPA 2.5 or higher required”
### `m54f3d5ae6b6b6ad` Jacksonville State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.jsu.edu/admissions/dualenrollment/index.html (sha256 4301dd9d4990)
- checks: {"fields": ["max_credit_hours_per_term", "min_hs_gpa", "per_credit_hour_charges"], "merged_pages": 4, "tiers": 1}
  - per_credit_hour_charge: 33 ⟵ “Jax State Dual Enrollment tuition only $33 per credit hour”
  - per_credit_hour_charge: 133 ⟵ “*Jax State’s dual enrollment tuition rate is $133 per credit hour; however, Jax State will apply a scholarship that reduces the net charge to $33 per credit hour for students. This scholarship will be reflected on the student’s account. The scholarship is processed manually and may not be reflected ”
  - per_credit_hour_charge: 33 ⟵ “*Jax State’s dual enrollment tuition rate is $133 per credit hour; however, Jax State will apply a scholarship that reduces the net charge to $33 per credit hour for students. This scholarship will be reflected on the student’s account. The scholarship is processed manually and may not be reflected ”
  - eligibility_tier: 3.0 ⟵ “3.0 high school GPA on a 4.0 scale”
  - max_credit_hours_per_term: 7 ⟵ “JSU offers tuition at a reduced rate for Dual Enrollment students with no university fees for fall and spring semesters. Students are limited to two courses at the reduced rate (up to 7 credit hours if taking a course that has a lab co-requisite). Enrollment for additional courses will be at the und”
  - per_credit_hour_charge: 25.99 ⟵ “Beginning with the Fall 2026 semester, dual enrollment students will use JaxBooks for all course textbooks. Students will pay $25.99 per credit hour for all course textbooks (digital or print). Lab kits are not included in JaxBooks and must be purchased separately. Instructions for how to opt-in or ”
  - max_credit_hours_per_term: 7 ⟵ “Tuition is offered at a reduced rate for Dual Enrollment students with no university fees for fall and spring semesters. Students are limited to two courses at the reduced rate (up to 7 credit hours if taking a course that has a lab co-requisite). Enrollment for additional courses will be at the und”
  - per_credit_hour_charge: 25.99 ⟵ “Beginning with the Fall 2026 semester, dual enrollment students will use JaxBooks for all course textbooks. Students will pay $25.99 per credit hour for all course textbooks (digital or print).”
  - per_credit_hour_charge: 33 ⟵ “If a J-STEAM course is selected as one of a student’s two courses at the reduced rate of $33 per credit hour, the student will be awarded J-STEAM scholarship for tuition and book. Students taking three or more courses are not eligible for the J-STEAM scholarship.”
  - eligibility_tier: 3.5 ⟵ “DE students who earn a 3.5 or higher GPA in a fall or spring semester will be named to the nationally recognized Emerging Scholars Merit List.”
### `mf55b19e24e6dc63` Jefferson State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.jeffersonstate.edu/admissions/dual-enrollment/accelerated-enrollment/ (sha256 4f3bd0e8710e)
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "merged_pages": 3, "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “Have a 2.5 unweighted GPA on a 4.0 scale (2.0 unweighted GPA for welding classes)”
  - eligibility_tier: 3.0 ⟵ “Students requesting a 3 or 4 credit hour course during a short session must have completed 9 credit hours at Jefferson State and have a minimum Jefferson State GPA of 3.0. (The only exception is if the requested course is not offered in the regular term.)”
  - state_grant_accepted: False ⟵ “Students in the Accelerated Enrollment Program are not eligible for dual enrollment scholarships.”
  - eligibility_tier: 2.5 ⟵ “2.5 unweighted GPA on a 4.0 scale”
### `30342f2094afee78` Jefferson State Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.jeffersonstate.edu/admissions/transfer-information/reverse-transfer/ (sha256 4b31dd0faa56)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 15 ⟵ “Student: Agree to participate and release your records to JSCC from your current University/College Meet eligibility requirements: Minimum of 15 hours earned at JSCC toward the degree Meet degree requirements for an Associate in Arts or an Associate in Science Degree Earn a total of 60 credits required for an associate degree.”
### `725bdd079118bcf4` Lawson State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.lawsonstate.edu/learn_at_lawson/High_School_Students/dual_enrollment.aspx (sha256 4d2ea6ab58a7)
- checks: {"fields": ["state_grant_accepted"], "tiers": 0}
  - state_grant_accepted: True ⟵ “In-eligible for ACCS Dual Enrollment Grant Funding”
  - state_grant_accepted: True ⟵ “Community College System Dual Enrollment Scholarship. Talk with an Enrollment Specialist about enrolling in one of our grant-funded programs. Not all programs are eligible for grants, so make sure you check that your program”
### `mf064aecef8aa57e` Lurleen B Wallace Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.lbwcc.edu/programs/dual-enrollment (sha256 75d46d5c5298)
- checks: {"fields": ["min_hs_gpa"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “Have a minimum unweighted GPA of 2.5 on a 4.0 scale. (Students in Automotive Mechanics, Building Construction, Diesel Technology, and Welding must have a minimum unweighted GPA of 2.0 or higher.)”
  - eligibility_tier: 2.5 ⟵ “• Have a minimum unweighted GPA of 2.5 on a 4.0 scale. Exception: students with a 2.0-2.49 GPA may”
### `d27697daea54f15a` Lurleen B Wallace Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.lbwcc.edu/future-students/admissions/admission-requirements/transfer-students (sha256 811e80124ac3)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer students who have completed degree-creditable, college-level English or mathematics courses with a grade of “C” or better will exempt the placement assessment requirement.”
### `34793a6fedfbb539` Miles College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.miles.edu/scholarships (sha256 109daddba3ae)
- checks: {"thresholds": {"act_min": 20, "gpa_min": 3.2, "sat_min": 1050}}
  - gpa_requirement: 3.2 ⟵ “Dean's Scholarship | 3.2 | 20 | 1050 | Total Award: $20,000.00 Per Year: $5,000.00 Per Semester: $2,500.00 | 15 hours per semester minimum, 3.3 cumulative GPA, 10 tutoring hours per semester”
  - test_requirement: ACT 20 / SAT 1050 ⟵ “Dean's Scholarship | 3.2 | 20 | 1050 | Total Award: $20,000.00 Per Year: $5,000.00 Per Semester: $2,500.00 | 15 hours per semester minimum, 3.3 cumulative GPA, 10 tutoring hours per semester”
### `7bdbc4cbb313df82` Miles College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.miles.edu/scholarships (sha256 109daddba3ae)
- checks: {"thresholds": {"gpa_min": 2.75}}
  - gpa_requirement: 2.75 ⟵ “Bridge Scholarship | 2.75 | Test score required/ no minimum requirement | Test score required/ no minimum requirement | Total Award: $10,000.00 Per Year: $2,500.00 Per Semester: $1,250.00 | 15 hours per semester minimum, 2.5 cumulative GPA”
  - test_requirement: ACT Test score required/ no minimum requirement / SAT Test score required/ no minimum requirement ⟵ “Bridge Scholarship | 2.75 | Test score required/ no minimum requirement | Test score required/ no minimum requirement | Total Award: $10,000.00 Per Year: $2,500.00 Per Semester: $1,250.00 | 15 hours per semester minimum, 2.5 cumulative GPA”
### `43a362cc4ae09bb0` Northeast Alabama Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://catalog.nacc.edu/credit-awarded-through-nontraditional-means (sha256 b1730d8a6ec0)
- checks: {"distinct_exams": 14, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIO103 | 4”
  - equivalencies[AP-BIOLOGY|4 or 5]:  ⟵ “Biology | 4 or 5 | BIO103 and BIO104 | 8”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MTH 113 and MTH 125 | 7”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MTH 113, MTH 125, and MTH 126 | 11”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC – AB subscore | 3 | MTH 125 | 4”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHM111 or CHM104 | 4”
  - equivalencies[AP-CHEMISTRY|4 or 5]:  ⟵ “Chemistry | 4 or 5 | (CHM111 and CHM 112) or CHM104 | 8 or 4”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language/ Composition | 3 | ENG101 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Language/ Composition | 5 | ENG101 and ENG102 | 6”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature/ Composition | 3 | ENG101 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|5]:  ⟵ “English Literature/ Composition | 5 | ENG101 and ENG102 | 6”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity & Magnetism | 3 | PHY 214 | 4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C: Mechanics | 3 | PHY 213 | 4”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics I | 3 | PHY 201 | 4”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics II | 3 | PHY 202 | 4”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSY 200 | 3”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3]:  ⟵ “Spanish Literature/ Culture | 3 | SPA 101 & SPA 102 | 8”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | MTH 265 or BUS 271 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “US History | 3 | HIS 201 and 202 | 6”
### `f58f671931bb04a2` Northeast Alabama Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.nacc.edu/credit-awarded-through-nontraditional-means (sha256 b1730d8a6ec0)
- checks: {"distinct_exams": 12, "equivalencies": 12, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | POL 211 | 3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENG 251 | 3”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIO 103,104 | 8”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MTH125 | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHM111, 112 | 8”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MTH100 | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MTH110 | 3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENG 261 | 3”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth And Development | 50 | PSY 210 | 3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | 50 | MTH112 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology (Intro) | 50 | PSY 200 | 3”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1 | 50 | SPA 101, 102 | 8”
### `0670de379d77575d` Reid State Technical College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.reidstate.edu/dualenrollment (sha256 c8442ad5a55c)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.0 ⟵ “3. Student must have and maintain a High School GPA of 2.0 or higher.”
### `fb90b10b086eca06` Reid State Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.reidstate.edu/scholarships (sha256 f463d0687b27)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 12 ⟵ “Minimum Requirements for Current Students: 3.0 GPA and at least 12 credit hours earned at Reid State. *Additional consideration is given to activities and honors.”
  - residency_requirement_credits: 12 ⟵ “Minimum Requirements for Current Students: 3.0 GPA and at least 12 credit hours earned at Reid State.”
### `m3725c42e59fee09` Samford University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.samford.edu/admission/files/Transfer-Resource-Guide.pdf (sha256 026f950c8ea1)
- checks: {"fields": ["min_grade"], "merged_pages": 3}
  - min_grade: C- ⟵ “The Office of the Registrar looks at four components when evaluating courses for your transfer into Samford: matching course descriptions, institutionally accredited colleges and universities, a grade of C- or above and no remedial or technical courses.”
  - min_grade: C- ⟵ “The Office of the Registrar looks at four components when evaluating courses for your transfer into Samford: matching course descriptions, institutionally accredited colleges and universities, a grade of C- or above and no remedial or technical courses.”
  - min_grade: C- ⟵ “Transfer work from institutionally accredited (formerly regionally accredited) colleges and universities will be accepted if the student has earned a grade of C- or higher (D grades will not transfer into Samford).”
### `47fb0a0fa63db239` Shelton State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.sheltonstate.edu/wp-content/uploads/2024/06/Dual-Enrollment-Brochure-2024-v6-PRESS-READY.pdf (sha256 d16d18db8064)
- checks: {"fields": [], "tiers": 6}
  - eligibility_tier: 2.0 ⟵ “• Technical GPA: 2.0”
  - eligibility_tier: 2.5 ⟵ “• Academic GPA: 2.5”
  - eligibility_tier: 2.5 ⟵ “minimum unweighted grade point average (GPA) of 2.5 on”
  - eligibility_tier: 2.5 ⟵ “minimum unweighted grade point average (GPA) of 2.5 on”
  - eligibility_tier: 2.0 ⟵ “minimum unweighted grade point average (GPA) of 2.0 on”
  - eligibility_tier: 3.5 ⟵ “Students who complete 12 credit hours and earn a 3.5 GPA”
  - eligibility_tier: 3.0 ⟵ “F Have a GPA of 3.0 or higher”
### `1b018d125b2ae96f` Southern Union State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://catalog.suscc.edu/202627-college-catalog-and-student-handbook/admission-of-high-school-students-accelerated-and-dual-enrolled (sha256 41826d95ed7a)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.5 ⟵ “The student has a minimum cumulative 2.5 grade point average on a 4.0 scale;”
### `af504fc989b7cc77` Southern Union State Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.suscc.edu/content/userfiles/files/AP%20Scores%20and%20Equivalents%20072424.pdf (sha256 bae6b5ed0a04)
- checks: {"distinct_exams": 21, "equivalencies": 23, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                              3                ART 100               3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                  3           BIO 103 & BIO 104          8”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                              3         MTH 115 & MTH 125            8”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                              3     MTH 115 & MTH 125 & MTH 126     12”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                3         CHM 111 & CHM 112            8”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                       3                CIS 150               3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language/Composition             4               ENG 101                3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Language/Composition             5         ENG 101 & ENG 102            6”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                         3           HIS 101 & HIS 102          6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                          3               GEO 100                3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                           3                ECO 231               3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                           3                ECO 232               3”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics I                                3                PHY 201               4”
  - equivalencies[AP-PHYSICS-2|3]:  ⟵ “Physics II                               3                PHY 202               4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3]:  ⟵ “Physics C: Mechanics                     3                PHY 213               4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3]:  ⟵ “Physics C: Electricity & Magnetism       3                PHY 214               4”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus                              3               MTH 113                3”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus                              3               MTH 115                4”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                               3                PSY 200               3”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language and Culture             3                SPA 101               4”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                               3               MTH 265                3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “US History                               3           HIS 201 & HIS 202          6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History                            3           HIS 121 & HIS 122          6”
### `5cf42ce0090b2718` Stillman College — awards 2026-27 [new] (source_unlabeled)
- source: https://catalog.stillman.edu/policy-on-awarding-course-credit (sha256 686b282c31fc)
- checks: {"thresholds": null}
  - test_requirement: ACT School of Arts and Sciences ⟵ “School of Arts and Sciences | Dean, School of Arts and Sciences”
### `5e1dfdd605e2b414` Stillman College — awards 2026-27 [new] (source_unlabeled)
- source: https://catalog.stillman.edu/policy-on-awarding-course-credit (sha256 686b282c31fc)
- checks: {"thresholds": null}
  - test_requirement: ACT School of Education Concerns ⟵ “School of Education Concerns | Dean, School of Education”
### `616b8a327dd347f3` Stillman College — awards 2026-27 [new] (source_unlabeled)
- source: https://catalog.stillman.edu/policy-on-awarding-course-credit (sha256 686b282c31fc)
- checks: {"thresholds": null}
  - test_requirement: ACT Transfer and Prior Learning Credit ⟵ “Transfer and Prior Learning Credit | Office of the Registrar”
### `65c776537cded816` Stillman College — awards 2026-27 [new] (source_unlabeled)
- source: https://catalog.stillman.edu/policy-on-awarding-course-credit (sha256 686b282c31fc)
- checks: {"thresholds": null}
  - test_requirement: ACT School of Business / MBA Concerns ⟵ “School of Business / MBA Concerns | Dean, School of Business, Entrepreneurship, and Computational and Information Sciences”
### `9432162a68978bec` Stillman College — awards 2026-27 [new] (source_unlabeled)
- source: https://catalog.stillman.edu/policy-on-awarding-course-credit (sha256 686b282c31fc)
- checks: {"thresholds": null}
  - test_requirement: ACT Policy Escalation ⟵ “Policy Escalation | Academic Affairs Committee”
### `a02a3178cbf0fe9a` Stillman College — awards 2026-27 [new] (source_unlabeled)
- source: https://catalog.stillman.edu/policy-on-awarding-course-credit (sha256 686b282c31fc)
- checks: {"thresholds": null}
  - test_requirement: ACT Primary Contact ⟵ “Primary Contact | Office of the Provost and Vice President for Academic Affairs”
### `ce60619473e6a71f` Stillman College — awards 2026-27 [new] (source_unlabeled)
- source: https://catalog.stillman.edu/policy-on-awarding-course-credit (sha256 686b282c31fc)
- checks: {"thresholds": null}
  - test_requirement: ACT Registrar / Recordkeeping ⟵ “Registrar / Recordkeeping | Office of the Registrar”
### `ma56a0279673c092` Stillman College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://stillman.edu/admissions/transfer-student/ (sha256 0c400ab17ffe)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “A grade of “C” or better must be earned in the transfer courses.”
  - min_grade: C ⟵ “Courses with grades of “C” or better will transfer along with courses earned from a regionally accredited institution.”
  - min_grade: C ⟵ “A grade of “C” or better must be earned in the transfer courses.”
  - min_grade: C ⟵ “Courses with grades of “C” or better will transfer along with courses earned from a regionally accredited institution.”
### `51bfca05feace29f` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/oos-international-freshman/ (sha256 1385795d7cc0)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $6,000 ⟵ “Crimson Legends | 25–26 | 1200–1250 | 3.50+ | $6,000”
  - gpa_requirement: 3.50+ ⟵ “Crimson Legends | 25–26 | 1200–1250 | 3.50+ | $6,000”
  - test_requirement: ACT 25–26 / SAT 1200–1250 ⟵ “Crimson Legends | 25–26 | 1200–1250 | 3.50+ | $6,000”
### `5bf3489767693acf` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/in-state-freshman/ (sha256 9d9f4037265c)
- checks: {"thresholds": {"act_min": 26}}
  - award_amount_text: $5,000 ⟵ “Crimson Achievement | 26 | 1230–1250 | 3.00–3.49 | $5,000”
  - gpa_requirement: 3.00–3.49 ⟵ “Crimson Achievement | 26 | 1230–1250 | 3.00–3.49 | $5,000”
  - test_requirement: ACT 26 / SAT 1230–1250 ⟵ “Crimson Achievement | 26 | 1230–1250 | 3.00–3.49 | $5,000”
### `5ebff17a6de2a3be` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/in-state-freshman/ (sha256 9d9f4037265c)
- checks: {"thresholds": {"act_min": 25}}
  - award_amount_text: $4,000 ⟵ “UA Recognition | 25 | 1200–1220 | 3.00–3.49 | $4,000”
  - gpa_requirement: 3.00–3.49 ⟵ “UA Recognition | 25 | 1200–1220 | 3.00–3.49 | $4,000”
  - test_requirement: ACT 25 / SAT 1200–1220 ⟵ “UA Recognition | 25 | 1200–1220 | 3.00–3.49 | $4,000”
### `afc9ea30fa2844cc` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/in-state-freshman/ (sha256 9d9f4037265c)
- checks: {"thresholds": {"act_min": 27}}
  - award_amount_text: $6,000 ⟵ “UA Legends | 27 | 1260–1290 | 3.00–3.49 | $6,000”
  - gpa_requirement: 3.00–3.49 ⟵ “UA Legends | 27 | 1260–1290 | 3.00–3.49 | $6,000”
  - test_requirement: ACT 27 / SAT 1260–1290 ⟵ “UA Legends | 27 | 1260–1290 | 3.00–3.49 | $6,000”
### `e6b72217350a0559` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/oos-international-freshman/ (sha256 1385795d7cc0)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $24,000 ⟵ “UA Scholar | 30–31 | 1360–1410 | 3.50+ | $24,000”
  - gpa_requirement: 3.50+ ⟵ “UA Scholar | 30–31 | 1360–1410 | 3.50+ | $24,000”
  - test_requirement: ACT 30–31 / SAT 1360–1410 ⟵ “UA Scholar | 30–31 | 1360–1410 | 3.50+ | $24,000”
### `f605a1d2d7c36531` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/oos-international-freshman/ (sha256 1385795d7cc0)
- checks: {"thresholds": {"act_min": 36, "gpa_min": 4.0, "sat_min": 1600}}
  - award_amount_text: Tuition+ ⟵ “Presidential Elite | 36 | 1600 | 4.0+ | Tuition+”
  - gpa_requirement: 4.0+ ⟵ “Presidential Elite | 36 | 1600 | 4.0+ | Tuition+”
  - test_requirement: ACT 36 / SAT 1600 ⟵ “Presidential Elite | 36 | 1600 | 4.0+ | Tuition+”
### `70d77fade6aa91fe` The University of Alabama — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.ua.edu/transfer/ (sha256 778488a17ada)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 60 ⟵ “Students may transfer up to 60 semester hours from a two-year college.”
### `97df0714f56a5309` Troy University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.troy.edu/academics/academic-programs/dual-enrollment.html (sha256 73ffa4379c41)
- checks: {"fields": ["min_hs_gpa", "per_credit_hour_charges", "tuition_per_credit_hour"], "tiers": 1}
  - per_credit_hour_charge: 133 ⟵ “For eligible high school students, Early College tuition is $133/credit hour, and”
  - per_credit_hour_charge: 33 ⟵ “net cost will be $33/credit after Early College scholarships are applied.”
  - eligibility_tier: 3.0 ⟵ “Unrounded cumulative high school GPA of 3.0 or higher”
  - per_credit_hour_charge: 133 ⟵ “Early College tuition is $133/credit hour, and net cost will be $33/credit after Early”
  - per_credit_hour_charge: 33 ⟵ “Early College tuition is $133/credit hour, and net cost will be $33/credit after Early”
### `678d28a042b2f5da` Tuskegee University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tuskegee.edu/admissions/Criteria-for-Freshmen.html (sha256 02338c7646f3)
- checks: {"thresholds": {"act_min": 28, "gpa_min": 3.7, "sat_min": 1300}}
  - gpa_requirement: 3.7 ⟵ “University Merit Scholarship | 3.7 | 1300 | 28 | Full Tuition and $300 e-book Voucher | 3.30 GPA and 30 Earned Hours”
  - test_requirement: ACT 28 / SAT 1300 ⟵ “University Merit Scholarship | 3.7 | 1300 | 28 | Full Tuition and $300 e-book Voucher | 3.30 GPA and 30 Earned Hours”
### `6a188f05330110a8` Tuskegee University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tuskegee.edu/admissions/Criteria-for-Freshmen.html (sha256 02338c7646f3)
- checks: {"thresholds": {"act_min": 26, "gpa_min": 3.5, "sat_min": 1200}}
  - gpa_requirement: 3.5 ⟵ “University Achievement Scholarship | 3.5 | 1200 | 26 | Up to One-Half Tuition | 3.20 GPA and 30 Earned Hours”
  - test_requirement: ACT 26 / SAT 1200 ⟵ “University Achievement Scholarship | 3.5 | 1200 | 26 | Up to One-Half Tuition | 3.20 GPA and 30 Earned Hours”
### `860a9d96c7092c76` Tuskegee University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tuskegee.edu/admissions/Criteria-for-Freshmen.html (sha256 02338c7646f3)
- checks: {"thresholds": {"act_min": 30, "gpa_min": 3.8, "sat_min": 1400}}
  - gpa_requirement: 3.8 ⟵ “Distinguished Presidential Scholarship | 3.8 | 1400 | 30 | Full Tuition, Room & Board, Fees, and $300 e-book Voucher | 3.50 GPA and 30 Earned HoursInterview Required”
  - test_requirement: ACT 30 / SAT 1400 ⟵ “Distinguished Presidential Scholarship | 3.8 | 1400 | 30 | Full Tuition, Room & Board, Fees, and $300 e-book Voucher | 3.50 GPA and 30 Earned HoursInterview Required”
### `c26efcb674287704` Tuskegee University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tuskegee.edu/admissions/Criteria-for-Freshmen.html (sha256 02338c7646f3)
- checks: {"thresholds": {"act_min": 23, "gpa_min": 3.3, "sat_min": 1180}}
  - gpa_requirement: 3.3 ⟵ “Tuskegee University Grant | 3.3 | 1180 | 23 | One-Quarter Tuition Scholarship | 3.00 GPA and 30 Earned Hours”
  - test_requirement: ACT 23 / SAT 1180 ⟵ “Tuskegee University Grant | 3.3 | 1180 | 23 | One-Quarter Tuition Scholarship | 3.00 GPA and 30 Earned Hours”
### `f2552ca9eca60af6` Tuskegee University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.tuskegee.edu/admissions/Criteria-for-Freshmen.html (sha256 02338c7646f3)
- checks: {"thresholds": {"act_min": 21, "gpa_min": 3.0, "sat_min": 1100}}
  - gpa_requirement: 3.0 ⟵ “Alabama Incentive Grant* | 3.0 | 1100 | 21 | One-Quarter Tuition Scholarship and Standard Double Housing | 3.00 GPA and 30 Earned Hours”
  - test_requirement: ACT 21 / SAT 1100 ⟵ “Alabama Incentive Grant* | 3.0 | 1100 | 21 | One-Quarter Tuition Scholarship and Standard Double Housing | 3.00 GPA and 30 Earned Hours”
### `12fcc80bd1a54f13` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/out-of-state-students (sha256 483162e97b7b)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $7,500 ⟵ “Blazer Scholarship | 22-23 ACT or 1100-1150 SAT | 3.5 or higher | $7,500”
  - gpa_requirement: 3.5 or higher ⟵ “Blazer Scholarship | 22-23 ACT or 1100-1150 SAT | 3.5 or higher | $7,500”
### `5a7cce4aab46cbe0` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/in-state-students (sha256 23475fbf7374)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $4,000 ⟵ “BlazerScholarship | 22-23 ACT or 1100-1150 SAT | 3.5 or higher | $4,000”
  - gpa_requirement: 3.5 or higher ⟵ “BlazerScholarship | 22-23 ACT or 1100-1150 SAT | 3.5 or higher | $4,000”
### `874443b752919e1d` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/out-of-state-students (sha256 483162e97b7b)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $28,500 ⟵ “Presidential Elite Scholarship | 32-36 ACT or 1420-1600 SAT | 4.0 or higher | $28,500”
  - gpa_requirement: 4.0 or higher ⟵ “Presidential Elite Scholarship | 32-36 ACT or 1420-1600 SAT | 4.0 or higher | $28,500”
### `72a48feec6c75a38` University of Alabama at Birmingham — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.uab.edu/undergraduate/progresstowardadegree/clep/clep.pdf (sha256 8d3b0fdd32ab)
- checks: {"distinct_exams": 4, "equivalencies": 6, "rows_without_score": 0}
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus with MA 125     50          4        Pass”
  - equivalencies[CLEP-CHEMISTRY|55]:  ⟵ “Chemistry     CH 115,    55          6        Pass    Natural         ELEC 101      50              6              Pass”
  - equivalencies[CLEP-CHEMISTRY|70]:  ⟵ “Chemistry     CH 115,    70          8        Pass    Precalculus     MA 107        50              4              Pass”
  - equivalencies[CLEP-FRENCH-LANGUAGE|4]:  ⟵ “French        FR 101     45-49       4        Pass    Level 1”
  - equivalencies[CLEP-FRENCH-LANGUAGE|55]:  ⟵ “French        FR 101,    55          11       Pass    Civilization I:”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German        GN 101,    50          8        Pass    Western         HY 102        50              3              Pass”
### `93bb844a46f27f45` University of Alabama at Birmingham — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.uab.edu/admissions/apply/credit-equivalencies (sha256 bcacd02a41da)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 24 ⟵ “UAB will award up to 24 hours of transferable military credit for veterans using their Joint Services transcripts with ACE recommendations.”
### `57e86d59e029be61` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/international (sha256 2c2285c84698)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “International Merit | 3.0-3.49 | $5,000 | $20,000”
  - gpa_requirement: 3.0-3.49 ⟵ “International Merit | 3.0-3.49 | $5,000 | $20,000”
### `8f8a6aa4fba85c85` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/international (sha256 2c2285c84698)
- checks: {"thresholds": null}
  - award_amount_text: $10,000 ⟵ “International Super Scholar | 3.5-4.0+ | $10,000 | $40,000”
  - gpa_requirement: 3.5-4.0+ ⟵ “International Super Scholar | 3.5-4.0+ | $10,000 | $40,000”
### `e0a9fc06a49e5831` University of Alabama in Huntsville — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.uah.edu/admissions/undergraduate/admitted-students/ap-ib (sha256 5207a1069460)
- checks: {"distinct_exams": 13, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5 - 7]:  ⟵ “Anthropology | 5 - 7 | 3 | ”
  - equivalencies[IB-HISTORY|5 - 7]:  ⟵ “Art History | 5 - 7 | 6 | ARH 100, 101”
  - equivalencies[IB-BIOLOGY|5 - 7]:  ⟵ “Biology | 5 - 7 | 8 | BYS 119, 120”
  - equivalencies[IB-CHEMISTRY|5 - 6 7]:  ⟵ “Chemistry | 5 - 6 7 | 4 8 | CH 101, 105 CH 101, 105, 201, 205”
  - equivalencies[IB-COMPUTER-SCIENCE|5 - 7]:  ⟵ “Computer Science | 5 - 7 | 3 | ”
  - equivalencies[IB-ECONOMICS|5 - 6 7]:  ⟵ “Economics | 5 - 6 7 | 3 6 | ECN 142 ECN 142, 143”
  - equivalencies[IB-GEOGRAPHY|5 - 7]:  ⟵ “Geography | 5 - 7 | 3 | AES 110”
  - equivalencies[IB-HISTORY|5 - 7]:  ⟵ “US History | 5 - 7 | 6 | HY 221, 222”
  - equivalencies[IB-HISTORY|5 - 7]:  ⟵ “World History | 5 - 7 | 6 | HY 103, 104”
  - equivalencies[IB-FRENCH|5 - 7]:  ⟵ “Languages: French, German, Spanish* | 5 - 7 | 12 | WLC 101, 102, 201, 202”
  - equivalencies[IB-MUSIC|5 - 7]:  ⟵ “Music | 5 - 7 | 3 | MU 100”
  - equivalencies[IB-PHILOSOPHY|5 - 7]:  ⟵ “Philosophy | 5 - 7 | 3 | PHL 101”
  - equivalencies[IB-PHYSICS|5 - 7]:  ⟵ “Physics | 5 - 7 | 8 | PH 101, 102”
  - equivalencies[IB-PSYCHOLOGY|5 - 7]:  ⟵ “Psychology | 5 - 7 | 6 | PY 101, 102”
  - equivalencies[IB-THEATRE|5 - 7]:  ⟵ “Theatre Arts | 5 - 7 | 3 | TH 122”
### `fdfc68c3d3026c20` University of Alabama in Huntsville — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.uah.edu/admissions/undergraduate/apply-for-admission/dual-enrollment (sha256 ad49c7a361e8)
- checks: {"fields": [], "tiers": 2}
  - eligibility_tier: 3.75 ⟵ “To qualify, students need a 28 ACT composite and 3.75 GPA. UAH will consider both weighted and unweighted GPAs, as well as ACT superscores for the three traditional ACT subjects.”
  - eligibility_tier: 3.0 ⟵ “Applicants must have at least a 3.0 GPA to participate.”
### `24396912211d201a` University of Montevallo — awards 2026-27 [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/undergraduate-admissions/scholarships-2/entering-freshmen-academic/ (sha256 f93ffd878734)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 per year ⟵ “Freshman Achievement Scholarship | 3.0-3.24 GPA (no test score required) | $1,500 per year”
### `33cda5231d194b78` University of Montevallo — awards 2026-27 [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/undergraduate-admissions/scholarships-2/entering-freshmen-academic/ (sha256 f93ffd878734)
- checks: {"thresholds": null}
  - award_amount_text: Up to $12,480 per year ⟵ “Out-of-State Scholarship | 3.0 GPA | Up to $12,480 per year”
### `40b0a521f4572bc8` University of Montevallo — awards 2026-27 [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/undergraduate-admissions/scholarships-2/entering-freshmen-academic/ (sha256 f93ffd878734)
- checks: {"thresholds": null}
  - award_amount_text: $4,500 per year ⟵ “Academic Recognition Scholarship | 24-26 ACT or 1160-1250 SAT and 3.0 GPA OR 3.75+ GPA (without test scores) | $4,500 per year”
### `6b8ec15287d711a5` University of Montevallo — awards 2026-27 [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/undergraduate-admissions/scholarships-2/entering-freshmen-academic/ (sha256 f93ffd878734)
- checks: {"thresholds": null}
  - award_amount_text: Room, board, tuition and fees ⟵ “Montevallo Ambassador Program Scholarship (M.A.P.S.) | 30 ACT or 1360 SAT and 3.5 GPA; Additional details below | Room, board, tuition and fees”
### `a42bc181dbd131fe` University of Montevallo — awards 2026-27 [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/undergraduate-admissions/scholarships-2/entering-freshmen-academic/ (sha256 f93ffd878734)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 per year ⟵ “Montevallo Academic Leadership Scholarship | 3.25-3.74 GPA (no test score required) | $2,500 per year”
### `d8ab0384b06af0ab` University of Montevallo — awards 2026-27 [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/undergraduate-admissions/scholarships-2/entering-freshmen-academic/ (sha256 f93ffd878734)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 per year ⟵ “Freshman Leadership Scholarship | 27-29 ACT or 1260-1350 SAT and 3.0 GPA | $6,000 per year”
### `eb2f1e23546b2eaa` University of Montevallo — awards 2026-27 [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/undergraduate-admissions/scholarships-2/entering-freshmen-academic/ (sha256 f93ffd878734)
- checks: {"thresholds": null}
  - award_amount_text: $9,000 per year ⟵ “Presidential Honors Scholarship | 30-36 ACT or 1360-1600 SAT and 3.0 GPA | $9,000 per year”
### `217a11d8fcbf2b68` University of Montevallo — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.montevallo.edu/wp-content/uploads/2025/10/IB-Credit-Evaluation-2025-10-17.pdf (sha256 e318eb015f09)
- checks: {"distinct_exams": 26, "equivalencies": 27, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|5]:  ⟵ “Biology HL                                    5         BIO 100 & 106               8”
  - equivalencies[IB-BIOLOGY-SL|5]:  ⟵ “Biology SL                                    5         BIO 100                     4”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|5]:  ⟵ “Business & MGMT SL/HL                         5         GB 100                      3”
  - equivalencies[IB-CHEMISTRY-HL|5]:  ⟵ “Chemistry HL                                  5         CHEM 101 & 102              8”
  - equivalencies[IB-CHEMISTRY-SL|5]:  ⟵ “Chemistry SL                                  5         CHEM 100                    4”
  - equivalencies[IB-COMPUTER-SCIENCE-HL|5]:  ⟵ “Computer Science HL                           5         MIS 161                     3”
  - equivalencies[IB-COMPUTER-SCIENCE-SL|5]:  ⟵ “Computer Science SL                           5         MIS Elective                3”
  - equivalencies[IB-ECONOMICS-HL|5]:  ⟵ “Economics HL                                  5         EC 231 & EC 232             6”
  - equivalencies[IB-ECONOMICS-SL|5]:  ⟵ “Economics SL                                  5         EC 231                      3”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE-SL|5]:  ⟵ “English A: Language and Literature SL/HL      5         ENG 101                     3”
  - equivalencies[IB-ENGLISH-A-LITERATURE-SL|5]:  ⟵ “English A: Literature SL/HL                   5         ENG 101                     3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|5]:  ⟵ “Environmental Systems SL/HL                   5         ES Elective                 3”
  - equivalencies[IB-FILM-HL|5]:  ⟵ “Film HL                                       5         MC Elective                 3”
  - equivalencies[IB-GEOGRAPHY-HL|5]:  ⟵ “Geography HL or SL                            5         GEOG 231                    3”
  - equivalencies[IB-HISTORY-HL|5]:  ⟵ “History HL                                    5         HIST 101 & 102              6”
  - equivalencies[IB-HISTORY-SL|5]:  ⟵ “History SL                                     5        HIST 101                    3”
  - equivalencies[IB-MUSIC-HL|5]:  ⟵ “Music HL                                      5         MUS 121 & 110               6”
  - equivalencies[IB-MUSIC-SL|5]:  ⟵ “Music SL                                      5         MUS 121                     3”
  - equivalencies[IB-PHILOSOPHY-HL|5]:  ⟵ “Philosophy HL/SL                              5         PHIL 110                    3”
  - equivalencies[IB-PHYSICS-HL|5]:  ⟵ “Physics HL                                    5         PHYS 201                    4”
  - equivalencies[IB-PSYCHOLOGY-HL|5]:  ⟵ “Psychology HL                                 5         PSYC 201                    3”
  - equivalencies[IB-PSYCHOLOGY-SL|5]:  ⟵ “Psychology SL                                 5         PYSC Elective               3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY-SL|5]:  ⟵ “Social and Cultural Anthropology SL/HL        5         ANTH 1TR                    3”
  - equivalencies[IB-SPANISH-SL|5]:  ⟵ “Spanish AB SL                                 5         SPN 101 & 102               6”
  - equivalencies[IB-SPANISH-SL|4]:  ⟵ “Spanish B SL/HL                                      4         SPN 101                         3”
  - … 2 more rows
### `4e85695889e52fbb` University of Montevallo — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.montevallo.edu/wp-content/uploads/2026/03/Credit-Awarded-for-AP-Exams-2026-3-17.pdf (sha256 285810d4c52f)
- checks: {"distinct_exams": 41, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design                          3          ART 122                                 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design                          3          ART 132                                 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies                    3          AAS 200                                 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                                 3          ART 120                                 3”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology                                     3          BIO 100                                 4”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB                                 3          Math 170                                4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC                                 3          Math 170 & 171                          8”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry                                   3          CHEM 101 & 102                          8”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture                3          World Language electives                6”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics         3          Political Science elective              3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                          3          CS 270                                  3”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles                 3          MIS 161                                 3”
  - equivalencies[AP-CYBERSECURITY|3]:  ⟵ “Cybersecurity                               3          CYBR elective                           3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                                     3          ART 112                                 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition            3          ENG 101 & 102                           6”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition          3          ENG 101 & 102                           6”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                       3          ESCI 100                                4”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History                            3          History general education elective      3”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture                 3          FRN 101 & 102                           6”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language and Culture                 3          GER 101 & 102                           6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                             3          Geography elective                      3”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian Language and Culture                3          World Language electives                6”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese Language and Culture               3          World Language electives                6”
  - equivalencies[AP-LATIN|3]:  ⟵ “Latin                                                 3            LAT 101 & LAT 102                         6”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                                        3            EC 231                                    3”
  - … 16 more rows
### `695f97363430847a` University of Montevallo — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/undergraduate-admissions/dual-enrollment/ (sha256 49a8220264d1)
- checks: {"fields": ["college_gpa_to_continue", "min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Additionally, any senior who has completed 12 or more UM dual enrollment credits and has a 3.0 GPA will be considered for automatic admission to the university as a first time freshman.”
  - college_gpa_to_continue: 2.5 ⟵ “Maintain a 2.5 GPA in college-level work”
### `e0132680756d2886` University of Montevallo — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.montevallo.edu/wp-content/uploads/2025/02/CLEP-Acceptance-Practice-2024-6-27.pdf (sha256 fc99ef52a699)
- checks: {"distinct_exams": 30, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                        50         POS 200                            3”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                        50         Area II English elective *         6”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature        50         Area II English elective *         6”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                    50         BIO 100 & 106                      8”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                   50         MATH 170                           4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                                  50         CHEM 101 & 102                     8”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                            50         MATH 144                           3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                        50         ENG 101                            3”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular                50         ENG 101                            3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics                        50         MATH general elective              3”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                         50         Area II English elective*          6”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting                       50         AC 221                             3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French I                                   50         FRN 101 & 102                      6”
  - equivalencies[CLEP-FRENCH-LANGUAGE|54]:  ⟵ “French II                                  54         FRN 201 & 202                      6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German I                                   50         GER 101 & 102                      6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German II                                  60         GER 201 & 202                      6”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development                 50         PSYC 306                           3”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                                 50         HUM general elective               3”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems                        50         MIS 161                            3”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law                  50         BL 283                             3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                    50         PSYC 201                           3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                     50         SOC 101                            3”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                                50         MATH 150                           4”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics               50         EC 231                             3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management                   50         MG 361                             3”
  - … 9 more rows
### `215adbf6d41aacc7` University of Montevallo — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.montevallo.edu/admissions-aid/ (sha256 eddc89e950f3)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 60 ⟵ “A maximum of 60 semester hours may be transferred for credit from a community college.”
### `20d35e9b83f4a18b` University of South Alabama — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.southalabama.edu/departments/registrar/records/transferassistance/ap-clep-ib-military.html (sha256 0f3b054a6abf)
- checks: {"distinct_exams": 14, "equivalencies": 30, "rows_without_score": 0}
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5]:  ⟵ “Social and Cultural Anthropology | AN 100 | 3 hrs | SL and HL | 5”
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | BLY 101/101L & BLY 102/102L | 8 hrs | SL | 5”
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | BLY 121/121, & BLY 122/122L | 8 hrs | HL | 5”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | CH101/101L or CH131/131L | 4 hrs | SL | 5”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | CH131/131L & CH132/132L | 8 hrs | HL | 5”
  - equivalencies[IB-THEATRE|4]:  ⟵ “Theatre | DRA 110 | 3 hrs | SL and HL | 4”
  - equivalencies[IB-ECONOMICS|6]:  ⟵ “Economics | ECO 215 & ECO 216 | 6 hrs | SL | 6”
  - equivalencies[IB-ECONOMICS|4]:  ⟵ “Economics | ECO 215 | 3 hrs | HL | 4”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | ECO 215 & ECO 216 | 6 hrs | HL | 5”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | GEO 114 | 3 hrs | SL and HL | 4”
  - equivalencies[IB-HISTORY|5]:  ⟵ “History of the Americas | HY 135 | 3 hrs | HL | 5”
  - equivalencies[IB-HISTORY|5]:  ⟵ “History of Asia and Oceania | HY 104 | 3 hrs | HL | 5”
  - equivalencies[IB-HISTORY|5]:  ⟵ “History of Europe | HY 102 | 3 hrs | HL | 5”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French | LG 111 | 3 hrs | ab initio SL/HL | 4”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French | LG 111 & LG 112 | 6 hrs | SL and HL | 5”
  - equivalencies[IB-FRENCH|6]:  ⟵ “French | LG 111, LG 112, LG 211 | 9 hrs | SL and HL | 6”
  - equivalencies[IB-FRENCH|7]:  ⟵ “French | LG 111, LG 112, LG 211, LG 212 | 12 hrs | SL and HL | 7”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German | LG 151 | 3 hrs | ab initio SL/HL | 4”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German | LG 151, LG 152 | 6 hrs | SL and HL | 5”
  - equivalencies[IB-GERMAN|6]:  ⟵ “German | LG 151, LG 152, LG 251 | 9 hrs | SL and HL | 6”
  - equivalencies[IB-GERMAN|7]:  ⟵ “German | LG 151, LG 152, LG 251, LG 252 | 12 hrs | SL and HL | 7”
  - equivalencies[IB-SPANISH|4]:  ⟵ “Spanish | LG 131 | 3 hrs | ab initio SL/HL | 4”
  - equivalencies[IB-SPANISH|5]:  ⟵ “Spanish | LG 131 & LG 132 | 6 hrs | SL | 5”
  - equivalencies[IB-SPANISH|6]:  ⟵ “Spanish | LG 131, LG 132, LG 231 | 9 hrs | SL | 6”
  - equivalencies[IB-SPANISH|7]:  ⟵ “Spanish | LG 131, LG 132, LG 231, LG 232 | 12 hrs | HL | 7”
  - … 5 more rows
### `9df3796ec1ab00b1` University of South Alabama — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.southalabama.edu/departments/registrar/records/transferassistance/ap-clep-ib-military.html (sha256 0f3b054a6abf)
- checks: {"distinct_exams": 31, "equivalencies": 44, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | ARH 100 | 3 hrs | 4”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “Studio Art: 2-D Design | ARS Elective | 3 hrs | 4”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “Studio Art: 3-D Design | ARS Elective | 3 hrs | 4”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Studio Art-Drawing | ARS Elective | 3 hrs | 4”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | BLY 121/121L & BLY 122/122L | 8 hrs | 3”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | CH 131/131L | 4 hrs | 4”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | CH 131/131L & CH 132/132L | 8 hrs | 5”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | CSC 120 | 4 hrs | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | CSC 108 | 3 hrs | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | ECO 215 | 3 hrs | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | ECO 216 | 3 hrs | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | GEO 114 | 3 hrs | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | HY 102 | 3 hrs | 4”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4]:  ⟵ “World History | HY 101 | 3 hrs | 4”
  - equivalencies[AP-WORLD-HISTORY-MODERN|5]:  ⟵ “World History | HY 101 & HY 102 | 6 hrs | 5”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “US History | HY 136 | 3 hrs | 4”
  - equivalencies[AP-UNITED-STATES-HISTORY|5]:  ⟵ “US History | HY 135 & HY 136 | 6 hrs | 5”
  - equivalencies[AP-PRECALCULUS|3]:  ⟵ “Precalculus | MA 115 | 4 hrs | 3”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | MA 125 | 4 hrs | 3”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | MA 125 & MA 126 | 8 hrs | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | MUT Elective | 3 hrs | 3”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 | PH 114/114L | 5 hrs | 4”
  - equivalencies[AP-PHYSICS-2|5]:  ⟵ “Physics 2 | PH 115/115L | 5 hrs | 5”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C Mechanics | PH 201/201L | 4 hrs | 4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4]:  ⟵ “Physics C Electricity & Magnetism | PH 202/202L | 4 hrs | 4”
  - … 19 more rows
### `7763ce23d225d996` University of West Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/ (sha256 d7e1c2167b88)
- checks: {"thresholds": null}
  - award_amount_text: $10,000.00 per year ⟵ “Trustee Excellence Award | 31-32 ACT / 1390- 1440 SAT | $10,000.00 per year”
  - gpa_requirement: 31-32 ACT / 1390- 1440 SAT ⟵ “Trustee Excellence Award | 31-32 ACT / 1390- 1440 SAT | $10,000.00 per year”
  - test_requirement: ACT 31-32 ACT / 1390- 1440 SAT / SAT 31-32 ACT / 1390- 1440 SAT ⟵ “Trustee Excellence Award | 31-32 ACT / 1390- 1440 SAT | $10,000.00 per year”
### `9714edfc345dc299` University of West Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/ (sha256 d7e1c2167b88)
- checks: {"thresholds": null}
  - award_amount_text: $12,000.00 per year ⟵ “Trustee Superior Award | 33-36 ACT / 1450- 1600 SAT | $12,000.00 per year”
  - gpa_requirement: 33-36 ACT / 1450- 1600 SAT ⟵ “Trustee Superior Award | 33-36 ACT / 1450- 1600 SAT | $12,000.00 per year”
  - test_requirement: ACT 33-36 ACT / 1450- 1600 SAT / SAT 33-36 ACT / 1450- 1600 SAT ⟵ “Trustee Superior Award | 33-36 ACT / 1450- 1600 SAT | $12,000.00 per year”
### `b3c2336a7cb20bff` University of West Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/ (sha256 46a028470566)
- checks: {"thresholds": null}
  - award_amount_text: $7,000.00 per year ⟵ “President’s Award | 29-30 ACT / 1330- 1380 SAT | $7,000.00 per year”
  - gpa_requirement: 29-30 ACT / 1330- 1380 SAT ⟵ “President’s Award | 29-30 ACT / 1330- 1380 SAT | $7,000.00 per year”
  - test_requirement: ACT 29-30 ACT / 1330- 1380 SAT / SAT 29-30 ACT / 1330- 1380 SAT ⟵ “President’s Award | 29-30 ACT / 1330- 1380 SAT | $7,000.00 per year”
### `cd0a23ecaace669f` University of West Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/ (sha256 46a028470566)
- checks: {"thresholds": null}
  - award_amount_text: $5,000.00 per year ⟵ “Dean’s Award | 27-28 ACT / 1260- 1320 SAT | $5,000.00 per year”
  - gpa_requirement: 27-28 ACT / 1260- 1320 SAT ⟵ “Dean’s Award | 27-28 ACT / 1260- 1320 SAT | $5,000.00 per year”
  - test_requirement: ACT 27-28 ACT / 1260- 1320 SAT / SAT 27-28 ACT / 1260- 1320 SAT ⟵ “Dean’s Award | 27-28 ACT / 1260- 1320 SAT | $5,000.00 per year”
### `e20589eaf79379d9` University of West Alabama — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.uwa.edu/admissions/dual-enrollment-students/ (sha256 1a84f8c6ad69)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 2.75 ⟵ “Admission to UWA without submitting SAT or ACT scores when a student earns 12 credit hours through UWA Dual Enrollment with a 2.75 GPA.”

## Exceptions (410)

### `008c8dab7e67f0a3` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts (sha256 6cf72cf92a2b)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `04a66c953b46d324` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/family-consumer-science-human-science-pac (sha256 98b447567c27)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “It requires the evaluation and interpretation of the historic human experience and the analysis of current human activity to gain an understanding of human phenomena and to project the outlines of human evolution.”
### `04e23a0d52f2fe6a` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=creative-media (sha256 37f0dc08c068)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `064cea6fac350269` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/business-pac (sha256 16feb38c5efa)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 1, "requirements": 1}
  - statements.exceptions: 1 ⟵ “However, the exact definition of business, like much else in the philosophy of business, is a matter of debate and complexity of meanings.”
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `0d9333d4c31105c3` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/colleges/approved-courses (sha256 e30a0388ed8d)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `1503603eeb01ca0b` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/technology-pac (sha256 2e35f2bb1019)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `18b4fa001ed8dbf6` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/liberal-arts-studies-pac (sha256 e2d59768af87)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "requirements": 1}
  - statements.effective: 1 ⟵ “The goal of a liberal studies major is to train students to communicate effectively, both orally and in writing, to develop skills in critical thinking and problem solving, and to imbue critical thinking with ethical thought.”
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `19e2b8d2d8762e6b` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/computer-science-pac (sha256 4b3b131cc4f5)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `1b14b6de89c78889` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/agsc (sha256 b6a6b33b620b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements (AGSC) Articulation & General Studies Committee  ⌃ CLICK HERE FOR INFORMATION REGARDING UPCOMING AGSC MEETING(S).”
### `1b6a3b84380f425e` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/faqs/committees (sha256 6aa9d5b274bc)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 4, "requirements": 7}
  - statements.requirements: 7 ⟵ “As required by state law, all accredited public two-year and four-year institutions in Alabama that receive state funding are required to participate in the AGSC/Alabama Transfers Program, formerly known as STARS.”
  - statements.exceptions: 4 ⟵ “However, public institutions that receive state funding are required to adhere to the statewide transfer policies established by the AGSC.”
### `1e82b9f6f164be1d` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/social-work-pac (sha256 7de53828a43b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Learn more about what social workers do, the educational requirements, and the projected job outlook for the field.”
### `1ea384928760b1dc` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=criminal-justice (sha256 1980a09235d4)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `2219f6ee0e6f581a` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/international-studies-pac (sha256 e44622d6cee1)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `23733a889146ee66` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo (sha256 d9ca5fed8b89)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `264357775ce2bb67` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/jsu/approved-courses (sha256 5e770ad94243)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `27d7680004053555` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/agsc-bylaws (sha256 3ae65d54f9b5)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 2, "guarantees": 1, "requirements": 12}
  - statements.requirements: 12 ⟵ “The legislation also designated the agency responsible for developing the computerized database and designing student contractual agreements to be honored among all public institutions as well as framed guidelines for compliance.”
  - statements.guarantees: 1 ⟵ “Article VII: Statewide Transfer and Articulation Reporting System (STARS) The computerized advisement system for students operated by Troy University and existing on the effective date of the ACT 94-202 was designated as the web-based data system to ensure students at each two-year institution accre”
  - statements.effective: 2 ⟵ “The AGSC/STARS Executive Director has overall responsibility for day-to-day operation, management, coordination, and promotion of the STARS program including: 1) supervising office staff; 2) managing the budget; 3) assessing the effectiveness of the web-based STARS program; 4) coordinating activitie”
### `28ff4b82bd320dd4` state-AL — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://sp.ache.edu/student-loan-inquiries/ (sha256 fd841fc6759c)
- issues: semantic_review_required
- checks: {"guarantees": 3}
  - statements.guarantees: 3 ⟵ “Student Loan Inquiries – Students&Parents Estimate Your Costs (Net Price Calculator) In-State Tuition Eligibility (50-Mile Radius Rule) Student Transcripts, Residency & Transfers Estimate Your Costs (Net Price Calculator) In-State Tuition Eligibility (50-Mile Radius Rule) Student Transcripts, Reside”
### `2bf61fc491982590` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/aum/approved-courses (sha256 bc7009c2180e)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `2ddb5b3753f5796d` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=art-history-b-a (sha256 a325a16123de)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `328b0455226aeb5a` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/una/approved-courses (sha256 56ae4ba4c9db)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `32f3add9ccd0dad1` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/about/legislation (sha256 e61181682966)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 1, "requirements": 7}
  - statements.requirements: 7 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements The following act created the AGSC and expanded STARS statewide.”
  - statements.exceptions: 1 ⟵ “An exception to this off-campus authority is provided for the branch campuses of universities or branch campuses of junior colleges in existence at the time of passage of this chapter whose fall 1978 registrations exceeded 500 class enrollments and branch campuses of universities operating prior to ”
### `33187e2c08ed5c17` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs (sha256 8fa9c6ef7e65)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `374014f9cd57f005` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/kinesiology-exercise-science-pac (sha256 756930f7800e)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `376f0c6e5bbce692` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a (sha256 9568502e189a)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `3c54d749bb31867c` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/aamu/approved-courses (sha256 f0edeebe8ad3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `3d13196b6d6cbe00` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/meetings/2026-08-25-1 (sha256 37d8e4cae6fd)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/meetings/2026-08-25-2
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Meeting of the Articulation and General Studies Committee August 25, 2026 · AGSC Annual Review & Planning Meeting · 5:00 AM”
### `3df44b61e2857ee2` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=art-education (sha256 001eeb17b8fe)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `41de7b5d7e3a666e` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/about/history (sha256 328e32fb51f2)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements In the late 1980s and early 1990s, students who attended Alabama's public two-year colleges faced many obstacles when it ca”
### `43e45b31aaa6a5cd` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies (sha256 cdebce042da0)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `4aa6d0e52c3f4b5d` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/faqs/administrators (sha256 bbd625673de3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 2, "exceptions": 11, "guarantees": 3, "requirements": 24}
  - statements.requirements: 24 ⟵ “As required by state law, all accredited public two-year and four-year institutions in Alabama that receive state funding are required to participate in the AGSC/Alabama Transfers Program, formerly known as STARS.”
  - statements.exceptions: 11 ⟵ “However, public institutions that receive state funding are required to adhere to the statewide transfer policies established by the AGSC.”
  - statements.guarantees: 3 ⟵ “For example, if a student takes one or more courses that they believe will transfer and upon transfer finds out otherwise, the student not only loses the money spent on tuition, books, room and board but also must face graduation delays which might result in lost income from future job opportunities”
  - statements.effective: 2 ⟵ “The catalog in effect when a student generates an Official Transfer Guide generally establishes the catalog requirements that guide the student's degree progression at the receiving four-year institution.”
### `4c6e41dc308aafdd` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/request-information (sha256 cf0c4b37d778)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements By submitting this form you are indicating your consent to share the contents of this request with whichever universities y”
### `4ecbed5e165cbd40` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/ua/approved-courses (sha256 a0a984c2fc64)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `4fee8c43f58e90e4` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/counselors (sha256 ad47b1fa0fab)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 1, "requirements": 4}
  - statements.requirements: 4 ⟵ “The course requirements listed on the Pathway page (and the student’s Official Guide) will cover most students’ first two years of coursework at a community college.”
  - statements.exceptions: 1 ⟵ “However, each university may assign different transfer credits for the same courses.”
### `50d3ad4e712ae418` state-AL — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://www.ache.edu/index.php/net-price-calculator-tuition-fees/ (sha256 d79da1b26c6a)
- issues: semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “The net price calculator is required for all Title IV institutions that enroll full-time, first-time degree- or certificate-seeking undergraduate students.”
### `521c530dfb133341` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/area-iii-committee (sha256 187ed17e9b83)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 2, "requirements": 19}
  - statements.requirements: 19 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements (AAC) Area I & II Academic Committee (AAC) Area III Academic Committee  ⌃ (AAC) Area IV Academic Committee The Points of Co”
  - statements.exceptions: 2 ⟵ “Courses which serve as prerequisites for certain disciplines or professions may require special attention (e.g., General studies courses in Chemistry must develop an understanding of the properties and dynamics of matter.”
### `53754a3ea12c3869` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/engineering-pac (sha256 d56596820195)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "requirements": 1}
  - statements.effective: 1 ⟵ “What really distinguishes an engineer is his ability to implement ideas in a cost effective and practical approach.”
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `5575f1cb3dc6f0b0` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification (sha256 9db7076b6c5f)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `58589bae5d7bc5a0` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/usa (sha256 f31ff0596f74)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `58d291c974886c84` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=sport-management (sha256 16271db8adbb)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `5c0c1d706e3fc50b` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=sport-management-troy (sha256 509c624700b7)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `5c2d44401d56d89a` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/uah/approved-courses (sha256 70e1bfacc64c)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `5c728cb0497873fb` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/asu/approved-courses (sha256 ccc2f7d0c60f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `5e89423858ce443c` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/au (sha256 c8e120e9e991)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `609e99c8efb2e90a` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech (sha256 6a846c94f9cc)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `61d2e8dbc48e9d8b` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/speech-pathology-pac (sha256 9412a6d83ca3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “If a person desires to work in the speech pathology field, he or she must first earn a master's degree in Speech Pathology.”
### `6374b222dead2255` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/athens (sha256 44dbc241d863)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `6398bed0f579599b` state-AL — state_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://alabamatransfers.com/students/dual-enrollment-index (sha256 884e8d90bd65)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/institutions/dual-enrollment
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “These courses are guaranteed to be accepted at all of Alabama’s community colleges and public universities if they are required in your chosen major.”
  - statements.requirements: 1 ⟵ “To get started, you should contact your high school’s counseling office to determine eligibility and cost.”
### `685058ad7afb8f10` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/pathways/agriculture-natural-resources-conservation (sha256 9deb50af97e1)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "exceptions": 9, "guarantees": 2, "requirements": 26}
  - statements.requirements: 26 ⟵ “These paths often require a blend of hands-on experience and knowledge in biology, economics, or technology, making them both dynamic and rewarding.”
  - statements.exceptions: 9 ⟵ “There is one important exception.”
  - statements.guarantees: 2 ⟵ “Transfer Guides are protected by the AGSC Transfer Agreement, which guarantees the transferability of major-specific courses among all public universities in Alabama.”
  - statements.effective: 1 ⟵ “Erik Peterson (elpeterson@ua.edu) and his team are available to assist with any questions about the updated You can also stay informed by visiting the official UA General Education website: https://provost.ua.edu/built-by-bama/ I have questions about taking courses through dual enrollment.”
### `68b7252eb359e50f` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=social-work (sha256 8eb5499d3177)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `69db2706e961b701` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/athens/approved-courses (sha256 0a88c5208b90)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Athens State University is an upper-division university that exclusively serves transfer students.”
### `6e905cb664f8f2d2` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/contact (sha256 f18a7bac044b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Use our contact form or reach out directly Shannon Nichols, Assistant Director & IT Manager Use our contact form or reach o”
### `7309bc15be144f7c` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/participating-institutions (sha256 7825ea316c8a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 1, "guarantees": 1}
  - statements.exceptions: 1 ⟵ “However, transfer policies and the applicability of individual courses vary by institution.”
  - statements.guarantees: 1 ⟵ “Neither the AGSC nor Alabama Transfers guarantees the accuracy of this information.”
### `73baa1c8c0173228` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/press-kit (sha256 30e76baf7162)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 2, "requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements More helpful information and graphic assets to come!”
  - statements.guarantees: 2 ⟵ “Additionally, this online system lets students preview how their credits will transfer for a target major and university.”
### `7543dababdbee978` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/faqs/counselors (sha256 c05b97d1021b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 2, "exceptions": 16, "guarantees": 4, "requirements": 38}
  - statements.requirements: 38 ⟵ “As required by state law, all accredited public two-year and four-year institutions in Alabama that receive state funding are required to participate in the AGSC/Alabama Transfers Program, formerly known as STARS.”
  - statements.exceptions: 16 ⟵ “However, public institutions that receive state funding are required to adhere to the statewide transfer policies established by the AGSC.”
  - statements.guarantees: 4 ⟵ “For example, if a student takes one or more courses that they believe will transfer and upon transfer finds out otherwise, the student not only loses the money spent on tuition, books, room and board but also must face graduation delays which might result in lost income from future job opportunities”
  - statements.effective: 2 ⟵ “The catalog in effect when a student generates an Official Transfer Guide generally establishes the catalog requirements that guide the student's degree progression at the receiving four-year institution.”
### `763efece5a51e16f` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/nursing-pac (sha256 a0e084618391)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Although an entry-level nurse can find a job with a three-year RN degree, there is a growing national movement to require all nurses to hold a BSN.”
### `7bb1b0a4c874b2f5` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/uah (sha256 fae139b3cba3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `7c27c79ac5501cf2` state-AL — state_policies 2021-22 · policy_kind=tuition_residency [new] (labeled_in_source)
- source: https://www.ache.edu/index.php/student-assistance/ (sha256 f20a04630af5)
- issues: stale_year_label:2021-22, semantic_review_required
- checks: {"requirements": 11}
  - statements.requirements: 11 ⟵ “This application process will determine your eligibility for federal student aid programs, such as, the Pell grant, Federal Supplemental Opportunity grant (FSEOG), college work-study and student loans as well as notify the institution of your choice of your eligibility.”
### `7c9a01c1f68a0130` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=philosophy (sha256 23658434ba4d)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `7cb337e2ca8203fa` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/una (sha256 feb84eeefe4c)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `7e0ad85e387e1946` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=social-science (sha256 f830b3f23f41)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `7e44c439c299e375` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/aum (sha256 f6d2eee2fdf4)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `7edc5cf7fb99f720` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/ua (sha256 8d93a10fefee)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `7ee2f503799f078f` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=public-relations (sha256 c2e1169c9cd7)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `7f111dd6002344ed` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=engineering-technology (sha256 b987ea09aa93)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `7fc2cfbc248e7640` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/um/approved-courses (sha256 5b8ab991be82)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `8315cd2988d06a9d` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/uab/approved-courses (sha256 f1c94e9ae506)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `8675cfd1d2f16d7c` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=journalism (sha256 fadc985f2291)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `8787ee1caa9de4f9` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees (sha256 3c07a1a6736a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 10}
  - statements.requirements: 10 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements AGSC Academic Committees are divided into the following groups History and importance of the academic committees In the ear”
### `887fb32ae5d86541` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning (sha256 e99325473058)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `8a5dfa2cc28a5c93` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management (sha256 e21cc682d5a9)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `8b3c1a7817b1b82e` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/aamu (sha256 68d0a768c973)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `8b7937c1cfbe5011` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=music (sha256 f377a771841e)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `8d3afd4ba813c39f` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/um (sha256 06b8a3360650)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `9187fa65aa2520e0` state-AL — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://www.ache.edu/index.php/alabama-student-assistance-program-asap/ (sha256 bb9a08ee8ba4)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Eligible students are undergraduate students who are Alabama residents attending eligible Alabama institutions.”
### `918cc5ea30234c9a` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/about/alabama-transfers (sha256 14883b96730f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 2, "guarantees": 1, "requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Alabama Transfers is a valuable resource for students in the state of Alabama who are seeking a smooth and efficient transi”
  - statements.guarantees: 1 ⟵ “Credit Transfer Assurance: The Alabama Transfers Program guarantees that the credits earned at one institution will transfer and count toward degree requirements at another participating institution.”
  - statements.effective: 2 ⟵ “Cost-Effective Pathway: By starting at a community college and then transferring to a four-year university, students can save significantly on tuition and other expenses.”
### `92bfbe81c8e63076` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=foreign-language (sha256 714e3d3fa616)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `936d5df3110a75a0` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/privacy (sha256 a46f918f8e17)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 2, "requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Alabama Transfers is powered by the Alabama General Studies Committee (AGSC) and Statewide Transfer & Articulation Reportin”
  - statements.effective: 2 ⟵ “These privacy practices were last updated October 31, 2022, and replace any previous privacy practices from the AGSC & STARS website.”
### `94c9187214e05c1c` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/about/areas-i-v (sha256 8c6aaf32866a)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "exceptions": 1, "requirements": 11}
  - statements.requirements: 11 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements To facilitate the development of a statewide transfer/articulation program, the AGSC created the following five areas that ”
  - statements.exceptions: 1 ⟵ “All the transfer guides (except for Engineering) follow these area guidelines.”
  - statements.effective: 1 ⟵ “Effective written communication skills are essential in a literate society.”
### `954165287de18b4a` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/accessibility (sha256 d9fb9c746dff)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Alabama Transfers is committed to ensuring accessibility for all.”
### `97bd0b90ac9ed0ec` state-AL — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://sp.ache.edu/transcripts-residency-transfers/ (sha256 f42c76151205)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Transcripts, Residency & Transfers – Students&Parents Estimate Your Costs (Net Price Calculator) In-State Tuition Eligibility (50-Mile Radius Rule) Student Transcripts, Residency & Transfers Estimate Your Costs (Net Price Calculator) In-State Tuition Eligibility (50-Mile Radius Rule) Student Transcr”
### `97d253d327222675` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/request-promotional-items (sha256 509b34fadf45)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 1, "requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements >>>> NOTE: We are currently running low on some of our promotional supplies due to manufacturing and shipping delays.”
  - statements.exceptions: 1 ⟵ “You are welcome to place your order now; however, please be aware that we may not be able to fulfill your order completely until additional supplies arrive.”
### `9b19a3b7894d1a14` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/area-iv-committee (sha256 0f887026ecc6)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 17}
  - statements.requirements: 17 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements (AAC) Area I & II Academic Committee (AAC) Area III Academic Committee (AAC) Area IV Academic Committee  ⌃ The Points of Co”
### `9c64d2a4a7cd7e7f` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/troy (sha256 f6a659c73a99)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `a3c8b0c9342b0266` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting (sha256 799e9015e06e)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `a50c3cd65d403644` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=news-media (sha256 01de0eebdbf9)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `a672eaea6262f768` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=theatre (sha256 cc609833df8f)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `aa43e209e6edea99` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=anthropology (sha256 82d45eca74ef)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `abf0238cfc198038` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/social-science-pac (sha256 dc4d5cd3d807)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `ac13613be7549173` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/faqs/students (sha256 a6914fd749e5)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 2, "exceptions": 17, "guarantees": 5, "requirements": 40}
  - statements.guarantees: 5 ⟵ “For example, if a student takes one or more courses that they believe will transfer and upon transfer finds out otherwise, the student not only loses the money spent on tuition, books, room and board but also must face graduation delays which might result in lost income from future job opportunities”
  - statements.requirements: 40 ⟵ “In addition to saving time and money for students and parents, the two-year colleges across the state have begun to streamline their course offerings to better match the AGSC approved transfer requirements as prescribed by Alabama Transfers (formerly STARS).”
  - statements.exceptions: 17 ⟵ “Keep in mind that not every university offers every major, and some specialized majors may be available at only one Alabama public university.”
  - statements.effective: 2 ⟵ “The catalog in effect when a student generates an Official Transfer Guide generally establishes the catalog requirements that guide the student's degree progression at the receiving four-year institution.”
### `ac8d07177dad2a5b` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/asu (sha256 fe5f6a6af924)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `acb81765ef0350ca` state-AL — state_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://alabamatransfers.com/institutions/dual-enrollment (sha256 8eb51d935c11)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/students/dual-enrollment-index
- checks: {"guarantees": 1, "requirements": 3}
  - statements.guarantees: 1 ⟵ “These courses are guaranteed to transfer to all Alabama public community colleges and universities when they are 1) required in your chosen major and 2) appear on the student’s official transfer guide for that major.”
  - statements.requirements: 3 ⟵ “IMPORTANT: To ensure that dual enrollment courses transfer properly to a public four-year institution in Alabama, high school students must obtain an official transfer guide for their intended major while enrolled in dual enrollment coursework.”
### `ade7136f3b1aa9f6` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/mass-communication-pac (sha256 3abd374343cd)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `afdd60f2b1dc352e` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/criminal-justice-pac (sha256 82f9546e2269)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `b007c3ace34e537b` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=sociology (sha256 d8e4de50b066)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `b9d610465628384d` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/course-equivalencies (sha256 cf4fb6c1d83f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `c259fd4ed4339bd5` state-AL — state_policies 2026-27 · policy_kind=tuition_residency [new] (source_unlabeled)
- source: https://sp.ache.edu/tuition/ (sha256 16186c940886)
- issues: semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Estimate Your Costs (Net Price Calculator) In-State Tuition Eligibility (50-Mile Radius Rule) Student Transcripts, Residency & Transfers Estimate Your Costs (Net Price Calculator) In-State Tuition Eligibility (50-Mile Radius Rule) Student Transcripts, Residency & Transfers Tuition Policies at 4-Year”
### `c2abb55a0a1eb703` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/system-updates (sha256 06f5890881de)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 49, "exceptions": 3, "requirements": 111}
  - statements.effective: 49 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements The Alabama Transfers Guide System is continually updated according to the policy decisions made by the members of the AGSC”
  - statements.requirements: 111 ⟵ “Area III - Students must now choose between BIO 104 and CHM 111 for one of the 4 SH courses in Natural Sciences.”
  - statements.exceptions: 3 ⟵ “The mathematics options are no longer restricted and now include all math courses available with the exception of MTH 108.”
### `c327fdbfeb7f6e88` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/about/agsc-stars (sha256 55fe9c79f047)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements The AGSC stands for the Alabama Articulation and General Studies Committee.”
### `c530e447e9c3b3c3` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=international-studies (sha256 a35afc2589f2)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `c6a66774b9f64781` state-AL — state_policies 2024-25 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.accs.edu/academics/dual-enrollment/ (sha256 716fcf29135c)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.requirements: 1 ⟵ “Eligible students must be in 10th, 11th, or 12th grades, have a 2.5 GPA and obtain written approval from a principal or superintendent.”
  - statements.guarantees: 1 ⟵ “Students planning to transfer to a public university in Alabama can use the STARS Guide to ensure all courses will transfer.”
### `c7fe0ad8497c8e50` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/administrators/course-approval-procedure (sha256 5365b4f56c72)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 3, "requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements The following procedure has been established by the AGSC to assist Alabama public institutions of higher education in submi”
  - statements.effective: 3 ⟵ “Once a recommendation is obtained by the Alabama Transfers office, the AGSC Course Database will be updated to reflect the recommendation (yes or no) as voted on by the respective academic committee.”
### `cb5ec556c659c917` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/scholarships (sha256 56f39fb131f3)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Each public university and community college in Alabama provides scholarship information on their individual websites.”
### `ccee4bd8e307e683` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/administrators/course-approval-guidelines (sha256 bf300639acc9)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 4}
  - statements.requirements: 4 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements The following guidelines have been established by the AGSC to provide institutions with the necessary information needed to”
### `cde9ce96dc57465f` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs (sha256 1a4cd471e776)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `ce87646a68d005e8` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=advertising (sha256 f440ca2f868f)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `d0e5a34524bf0172` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/uab (sha256 15e9b24a8aff)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `d242e951f83d55c6` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/meetings/2026-08-25-2 (sha256 4b1d1b8a6e18)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/meetings/2026-08-25-1
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Meeting of the Articulation and General Studies Committee August 25, 2026 · AGSC Summer Business Meeting · 5:00 AM "SUMMER ”
### `d5dc7265daaa1ac2` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/students/transfer-checklist (sha256 b7c57b9e0852)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "exceptions": 1, "guarantees": 1, "requirements": 6}
  - statements.requirements: 6 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements 10 STEPS TO TRANSFER SUCCESS -- Click links below to jump to a specific section.”
  - statements.exceptions: 1 ⟵ “However, if you are a freshman at a community college, the time to start planning is now!”
  - statements.effective: 1 ⟵ “Keep List in a Safe Place - Review and Update It Periodically Once you have the first draft of the list, continue to updated it and review it.”
  - statements.guarantees: 1 ⟵ “The best way for us to help you make sure all your credits will transfer is for you to go through the official "Get the guide" process - go to the top of this page and click on Students - or go to http://www.alabamatransfers.com.”
### `d5e7ee1a13ed5cbc` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=behavioral-science (sha256 3eba1c564e00)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `d78013bcbaf251c5` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/points-of-contact (sha256 fa6d591baf2c)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "requirements": 1}
  - statements.effective: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Importance of the institutional points of contact To effectively manage a statewide transfer program, consistent communicat”
  - statements.requirements: 1 ⟵ “These individuals—selected by their institution’s president or chancellor—are responsible for maintaining and supporting the AGSC & Alabama Transfers program on their respective campuses.”
### `d78860a7de041271` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/edvisorly-ai-pilot (sha256 3d33644eaf72)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements The link below provides access to the testing site for Phase-One Transcript Evaluation Module.”
  - statements.effective: 1 ⟵ “One simple and effective cross-institution enrollment dashboard to allow pilot institutions track key accountability metrics from the platform to uplift transfer, degree completion, reverse transfer, and more.”
### `d82219364426d8c2` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=music-industry-studies (sha256 d256c5d3087e)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `d9d1be35ddd7e014` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/au/approved-courses (sha256 5de1abfaa6c6)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `d9f1235d64d37594` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/administrators (sha256 96a51eca9926)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Your contributions make Alabama Transfers.”
### `daaa18a3d04c7f74` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/ (sha256 6070d230ae95)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"exceptions": 1, "requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Submit an official Transfer Agreement, and bring your earned credits with you when you Browse guides by exploring academic ”
  - statements.exceptions: 1 ⟵ “However, each university may assign different transfer credits for the same courses.”
### `dc0085199c4d2fa0` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/area-i-ii-committee (sha256 261f8b079e2f)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 7}
  - statements.requirements: 7 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements (AAC) Area I & II Academic Committee  ⌃ (AAC) Area III Academic Committee (AAC) Area IV Academic Committee The Points of Co”
### `dc5941df38f311f0` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=history (sha256 3ee33f252fe7)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `dd8435f81f454ba9` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/education-pac (sha256 83a9bed91a7d)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `dfd0b9b0ccdd8ecf` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs (sha256 6a358044852e)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `e11315109f0e9bbc` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/institutions/ap-clep-credit (sha256 c694ab56bc09)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Each AP course concludes with an AP Exam.”
### `e219e5629ef075f5` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/allied-health-pac (sha256 5e0466cbb5fa)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `e2eaf31af54f3df5` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=religious-studies (sha256 83ed8d41b48b)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `e438b5083ed6a4a9` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/jsu (sha256 b73f8a6f4ebb)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `e521301a85e06a19` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies (sha256 88d00e397a4d)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `e59e9b294eb49131` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/usa/approved-courses (sha256 a7cfcfc6ea87)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `e7e26e395c52b566` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/troy/approved-courses (sha256 3744030d8cf8)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `e99349ea27b14bd4` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a (sha256 9d601a4a2bb5)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `e9d2512364222d25` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=human-services (sha256 c929396c6e0a)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `ec640bef367a04eb` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=dance (sha256 6050db55ecea)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `ef0c4eab8088cc2e` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=political-science (sha256 f81f58501022)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `ef1307ab1e9afb7b` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/uwa/approved-courses (sha256 993bf6467bce)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 5}
  - statements.requirements: 5 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements One of the primary functions of the AGSC is to work hand-in-hand with the established discipline committees (faculty groups”
  - statements.guarantees: 1 ⟵ “Because degree requirements vary significantly among universities and academic programs, it is the student's responsibility to confirm that the courses they complete at their current institution will transfer and satisfy degree requirements at their destination institution.”
### `efd79d4c032bed8f` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=interpreter-training (sha256 9bea108cc878)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 3}
  - statements.requirements: 3 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `f47c035cd1770be0` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/transfer-agreement (sha256 3eb7d6445570)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"effective": 1, "exceptions": 1, "guarantees": 2, "requirements": 7}
  - statements.requirements: 7 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements The Transfer Agreement, listed below, appears at the end of every official transfer guide.”
  - statements.guarantees: 2 ⟵ “This agreement guarantees the transferability of the course work listed on the attached guide among institutions of higher education.”
  - statements.effective: 1 ⟵ “The students will be graduated under the catalog in effect on this date at the institution to which he or she is transferring unless the student is given and accepts the opportunity to be placed under a more recent catalog or unless a change in the program is mandated by requirements of an external ”
  - statements.exceptions: 1 ⟵ “When a course sequence is required, it is recommended that students complete the This guide remains valid and is guaranteed only if the student continues in the major Completion of coursework listed on this guide does not guarantee admission to any public institution of higher education in Alabama; ”
### `f4819f270fbb3ba8` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/official-guide/demo?major=human-development-family-studies (sha256 2496e8d4aa28)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://alabamatransfers.com/official-guide/demo,https://alabamatransfers.com/official-guide/demo?major=advertising,https://alabamatransfers.com/official-guide/demo?major=anthropology,https://alabamatransfers.com/official-guide/demo?major=art-education,https://alabamatransfers.com/official-guide/demo?major=art-history-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-a,https://alabamatransfers.com/official-guide/demo?major=art-studio-b-f-a,https://alabamatransfers.com/official-guide/demo?major=behavioral-science,https://alabamatransfers.com/official-guide/demo?major=communication-studies-or-speech,https://alabamatransfers.com/official-guide/demo?major=creative-media,https://alabamatransfers.com/official-guide/demo?major=criminal-justice,https://alabamatransfers.com/official-guide/demo?major=dance,https://alabamatransfers.com/official-guide/demo?major=engineering-technology,https://alabamatransfers.com/official-guide/demo?major=english-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=foreign-language,https://alabamatransfers.com/official-guide/demo?major=history,https://alabamatransfers.com/official-guide/demo?major=hotel-restaurant-and-hospitality-management,https://alabamatransfers.com/official-guide/demo?major=human-services,https://alabamatransfers.com/official-guide/demo?major=integrated-marketing-communications-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=interdisciplinary-arts,https://alabamatransfers.com/official-guide/demo?major=international-studies,https://alabamatransfers.com/official-guide/demo?major=interpreter-training,https://alabamatransfers.com/official-guide/demo?major=journalism,https://alabamatransfers.com/official-guide/demo?major=liberal-arts-studies,https://alabamatransfers.com/official-guide/demo?major=music,https://alabamatransfers.com/official-guide/demo?major=music-industry-studies,https://alabamatransfers.com/official-guide/demo?major=news-media,https://alabamatransfers.com/official-guide/demo?major=philosophy,https://alabamatransfers.com/official-guide/demo?major=political-science,https://alabamatransfers.com/official-guide/demo?major=psychology-ba-or-bs,https://alabamatransfers.com/official-guide/demo?major=public-relations,https://alabamatransfers.com/official-guide/demo?major=rehabilitation-non-certification,https://alabamatransfers.com/official-guide/demo?major=religious-studies,https://alabamatransfers.com/official-guide/demo?major=social-science,https://alabamatransfers.com/official-guide/demo?major=social-work,https://alabamatransfers.com/official-guide/demo?major=sociology,https://alabamatransfers.com/official-guide/demo?major=sport-management,https://alabamatransfers.com/official-guide/demo?major=sport-management-troy,https://alabamatransfers.com/official-guide/demo?major=sports-management-rec-studies,https://alabamatransfers.com/official-guide/demo?major=telecommunication-and-film-or-broadcasting,https://alabamatransfers.com/official-guide/demo?major=theatre,https://alabamatransfers.com/official-guide/demo?major=urban-and-regional-planning
- checks: {"requirements": 2}
  - statements.requirements: 2 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements Attention transfer students and advisors: This page is designed to help you (and your advisor) explore transfer guides avai”
### `f830bcb98b361c15` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/committees/environmental-science-pac (sha256 c3dc66db0d3c)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"requirements": 1}
  - statements.requirements: 1 ⟵ “For a four-year institution to have a member on a Professional Academic Committee (PAC), they must have at least one major in the discipline area (verified by the ACHE Academic Program Inventory).”
### `f979074c381dea54` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/resources/glossary (sha256 a14b9bc07c5c)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 2, "requirements": 27}
  - statements.requirements: 27 ⟵ “Get your transfer guide or explore academic pathways Access tools and resources for advising transfer students Obtain usage information or submit courses & program requirements When discussing articulation/transfer issues often times the following terms are used.”
  - statements.guarantees: 2 ⟵ “Courses offered by one college (e.g., a community college) that will transfer to another college (e.g., a four-year college or university).”
### `fdc81ca8db93e8ec` state-AL — state_policies 2025-26 · policy_kind=statewide_articulation [new] (labeled_in_source)
- source: https://alabamatransfers.com/universities/uwa (sha256 b8010d81934d)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"guarantees": 1, "requirements": 1}
  - statements.guarantees: 1 ⟵ “Answer a few questions and submit to guarantee your credit transfer for four years Select your community collegeOut of State Bevill State Community College Bishop State Community College Calhoun Community College Central Alabama Community College Chattahoochee Valley Community College Coastal Alabam”
  - statements.requirements: 1 ⟵ “For four years from the date you submitted this guide, it must be honored by all Alabama public universities that offer your specified major.”
### `0f5de8687cdfcafd` Alabama A & M University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aamu.edu/admissions-aid/financial-aid/ (sha256 66bae89f3f73)
- issues: semantic_review_required, conflicting_sources:https://www.aamu.edu/admissions-aid/financial-aid/financial-aid-toolkit/financial-aid-online-appeal.html,https://www.aamu.edu/admissions-aid/financial-aid/financial-aid-toolkit/satisfactory-academic-progress-policy.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Incoming Bulldogs Meet Our Team Apply for Aid Types of Aid Scholarships Accept Your Award VerificationVerification Forms & Missing Documents Satisfactory Academic Progress & Appeals Financial Aid Checklist Federal Work Study Default Management & Financial Literacy Financial Aid Toolkit Net Price Calculator Policy & Procedures Financial Aid Shopping Sheet Consumer Brochure We’re here for you The pr”
### `363557206777a93e` Alabama A & M University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aamu.edu/admissions-aid/financial-aid/financial-aid-toolkit/satisfactory-academic-progress-policy.html (sha256 3d480fbd14a0)
- issues: semantic_review_required, conflicting_sources:https://www.aamu.edu/admissions-aid/financial-aid/,https://www.aamu.edu/admissions-aid/financial-aid/financial-aid-toolkit/financial-aid-online-appeal.html
- checks: {"negative_sentences": 0, "sentences": 10}
  - sentence: sap_appeal ⟵ “A student who fails to meet the applicable SAP standards at an official evaluation becomes ineligible for Title IV aid unless eligibility is restored through an approved SAP appeal, an approved academic plan when applicable, or by re-establishing SAP standards without Title IV assistance.”
  - sentence: sap_appeal ⟵ “A change of major may be considered as part of a student's SAP appeal when the change contributes to maximum timeframe or other SAP concerns; however, the change of major does not remove previously attempted coursework from the SAP calculation.”
  - sentence: sap_appeal ⟵ “Appeals Students who fail to make satisfactory academic progress may appeal to have their Title IV aid reinstated when extenuating circumstances affected their academic progress.”
  - sentence: sap_appeal ⟵ “Students on financial aid suspension may submit a SAP appeal through the University's Laserfiche SAP Appeal form.”
  - sentence: sap_appeal ⟵ “A SAP appeal may be submitted through the end of the semester for which the student is requesting reinstatement, subject to applicable federal disbursement requirements and the University's academic calendar.”
  - sentence: sap_appeal ⟵ “Approval of an academic suspension appeal does not automatically constitute approval of a financial aid SAP appeal.”
### `5b730a87ca8d477c` Alabama A & M University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.aamu.edu/admissions-aid/financial-aid/financial-aid-toolkit/financial-aid-online-appeal.html (sha256 9ccd5ac56d8b)
- issues: semantic_review_required, conflicting_sources:https://www.aamu.edu/admissions-aid/financial-aid/,https://www.aamu.edu/admissions-aid/financial-aid/financial-aid-toolkit/satisfactory-academic-progress-policy.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress and Appeal Policy Financial Aid Online Appeal Financial aid appeals and all supporting documentation must be submitted online via Laserfiche.”
### `8ec2f73f4d3ba5f3` Alabama A & M University — appeals 2000-01 [new] (labeled_in_source)
- source: https://www.aamu.edu/admissions-aid/financial-aid/professional-judgement.html (sha256 6965460f4ed6)
- issues: stale_year_label:2000-01, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: dependency_override ⟵ “Dependency overrides Computer Purchase Parent attending college Documentation Requirements For Death or Divorce: A copy of the death certificate for the parent of a dependent student, spouse of an independent student.”
  - sentence: dependency_override ⟵ “Dependency overrides: If a student is under the age of 24, an undergraduate, not married, has no dependents, and is not a veteran, an orphan or a ward of the court, he/she is considered to be dependent for the purposes of federal student aid.”
  - sentence: dependency_override ⟵ “A dependency override may be requested in cases of complete alienation between a parent and a student.”
  - sentence: dependency_override ⟵ “In support of a request for dependency override the student should submit statements from third-parties having first-hand knowledge of the circumstances.”
  - sentence: dependency_override ⟵ “The Director of Financial Aid will make the final determination in requests for dependency overrides.”
  - sentence: dependency_override ⟵ “Federal regulations do not permit a financial aid officer to perform a dependency override because of a parent's unwillingness to pay for education.”
### `a959f737f2c4a8b3` Alabama A & M University — appeals 2000-01 [new] (labeled_in_source)
- source: https://www.aamu.edu/admissions-aid/financial-aid/professional-judgement.html (sha256 6965460f4ed6)
- issues: stale_year_label:2000-01, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Instructions to Students/Parents All requests for the execution of professional judgment must: Be initiated by a letter from the student in which the student requests consideration of his/her particular circumstances.”
  - sentence: professional_judgment ⟵ “Remember: Any adjustments made to your SAR as a result of your request for a professional judgment decision may delay or change your financial aid package.”
### `da2ac110a07e8905` Alabama A & M University — appeals 2000-01 [new] (labeled_in_source)
- source: https://www.aamu.edu/admissions-aid/financial-aid/professional-judgement.html (sha256 6965460f4ed6)
- issues: stale_year_label:2000-01, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Please refer to the "Documentation Requirements" when preparing your request for consideration of special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Your special circumstances will be considered only after we have received your SAR.”
  - sentence: need_based_special_circumstances ⟵ “If you have not already provided a copy of all required tax returns for verification, please include one with your request for consideration of special circumstances.”
### `2137154a0bc5ca98` Alabama State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.alasu.edu/financial-aid/types-of-aid/marion-nine-automatic-scholarships.php (sha256 5ba06d742997)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “This scholarship will be applied to the out-of-State portion of the student’s tuition. *If awarded: Students must have a FAFSA on file (International students are excluded.) Students must be enrolled full-time (Exceptions given to graduating seniors or special circumstances.”
### `4db7ce5024135cfc` Alabama State University — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.alasu.edu/_qa/24-25%20COA..pdf (sha256 c411c9ef96e2)
- issues: multiple_total_rows, stale_year_label:2024-25, conflicting_sources:https://www.alasu.edu/financial-aid/tuition-costs.php
- checks: {"columns": 1, "rows": 22}
  - column:TUITION: 16656 ⟵ “TUITION | $8,328 | $16,656”
  - column:INSTITUTIONAL FEES (Health Insurance Fee, Athletic: 2920 ⟵ “INSTITUTIONAL FEES (Health Insurance Fee, Athletic | $2,920 | $2,920”
  - column:HOUSING (Average Cost; differs by residence location): 3500 ⟵ “HOUSING (Average Cost; differs by residence location) | $3,500 | $3,500”
  - column:MEAL PLAN (Average Cost; Different Meal Plan: 4100 ⟵ “MEAL PLAN (Average Cost; Different Meal Plan | $4,100 | $4,100”
  - column:ESTIMATED LOAN FEES (Differs by individual: 192 ⟵ “ESTIMATED LOAN FEES (Differs by individual | $192 | $192”
  - column:SUBTOTAL: 28064 ⟵ “SUBTOTAL | $19,736 | $28,064”
  - column:TRANSPORTATION: 3000 ⟵ “TRANSPORTATION | $3,000 | $3,000”
  - column:MISCELLANEOUS/PERSONAL: 2130 ⟵ “MISCELLANEOUS/PERSONAL | $2,130 | $2,130”
  - column:SUBTOTAL: 5130 ⟵ “SUBTOTAL | $5,130 | $5,130”
  - column:ESTIMATED TOTAL: 33194 ⟵ “ESTIMATED TOTAL | $24,866 | $33,194”
  - column:TUITION: 19776 ⟵ “TUITION | $9,888 | $19,776”
  - column:INSITUTIONAL FEES (Health Insurance Fee, Athletic Fee,: 2920 ⟵ “INSITUTIONAL FEES (Health Insurance Fee, Athletic Fee, | $2,920 | $2,920”
  - column:HOUSING (Average Cost; differs by residence location): 3500 ⟵ “HOUSING (Average Cost; differs by residence location) | $3,500 | $3,500”
  - column:MEAL PLAN (Average Cost; Different Meal Plan Options are: 4100 ⟵ “MEAL PLAN (Average Cost; Different Meal Plan Options are | $4,100 | $4,100”
  - column:ESTIMATED LOAN FEES (Differs by individual student and: 222 ⟵ “ESTIMATED LOAN FEES (Differs by individual student and | $222 | $222”
  - column:SUBTOTAL: 31214 ⟵ “SUBTOTAL | $21,326 | $31,214”
  - column:TRANSPORTATION: 3000 ⟵ “TRANSPORTATION | $3,000 | $3,000”
  - column:MISCELLANEOUS/PERSONAL: 2130 ⟵ “MISCELLANEOUS/PERSONAL | $2,130 | $2,130”
  - column:SUBTOTAL: 5130 ⟵ “SUBTOTAL | $5,130 | $5,130”
  - column:ESTIMATED TOTAL: 36344 ⟵ “ESTIMATED TOTAL | $26,456 | $36,344”
  - column:TUITION: 16656 ⟵ “TUITION | $8,328 | $16,656”
  - column:INSTITUTIONAL FEES (Health Insurance Fee, Athletic Fee,: 2920 ⟵ “INSTITUTIONAL FEES (Health Insurance Fee, Athletic Fee, | $2,920 | $2,920”
  - column:MEAL PLAN (Average Cost; Different Meal Plan Options: 4100 ⟵ “MEAL PLAN (Average Cost; Different Meal Plan Options | $4,100 | $4,100”
  - column:ESTIMATED LOAN FEES (Differs by individual student: 192 ⟵ “ESTIMATED LOAN FEES (Differs by individual student | $192 | $192”
  - column:SUBTOTAL: 35364 ⟵ “SUBTOTAL | $27,036 | $35,364”
  - … 20 more rows
### `659aa80277e3a417` Alabama State University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.alasu.edu/_qa/24-25%20COA..pdf (sha256 c411c9ef96e2)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 22}
  - column:TUITION: 8328 ⟵ “TUITION | $8,328 | $16,656”
  - column:INSTITUTIONAL FEES (Health Insurance Fee, Athletic: 2920 ⟵ “INSTITUTIONAL FEES (Health Insurance Fee, Athletic | $2,920 | $2,920”
  - column:HOUSING (Average Cost; differs by residence location): 3500 ⟵ “HOUSING (Average Cost; differs by residence location) | $3,500 | $3,500”
  - column:MEAL PLAN (Average Cost; Different Meal Plan: 4100 ⟵ “MEAL PLAN (Average Cost; Different Meal Plan | $4,100 | $4,100”
  - column:ESTIMATED LOAN FEES (Differs by individual: 192 ⟵ “ESTIMATED LOAN FEES (Differs by individual | $192 | $192”
  - column:SUBTOTAL: 19736 ⟵ “SUBTOTAL | $19,736 | $28,064”
  - column:TRANSPORTATION: 3000 ⟵ “TRANSPORTATION | $3,000 | $3,000”
  - column:MISCELLANEOUS/PERSONAL: 2130 ⟵ “MISCELLANEOUS/PERSONAL | $2,130 | $2,130”
  - column:SUBTOTAL: 5130 ⟵ “SUBTOTAL | $5,130 | $5,130”
  - column:ESTIMATED TOTAL: 24866 ⟵ “ESTIMATED TOTAL | $24,866 | $33,194”
  - column:TUITION: 9888 ⟵ “TUITION | $9,888 | $19,776”
  - column:INSITUTIONAL FEES (Health Insurance Fee, Athletic Fee,: 2920 ⟵ “INSITUTIONAL FEES (Health Insurance Fee, Athletic Fee, | $2,920 | $2,920”
  - column:HOUSING (Average Cost; differs by residence location): 3500 ⟵ “HOUSING (Average Cost; differs by residence location) | $3,500 | $3,500”
  - column:MEAL PLAN (Average Cost; Different Meal Plan Options are: 4100 ⟵ “MEAL PLAN (Average Cost; Different Meal Plan Options are | $4,100 | $4,100”
  - column:ESTIMATED LOAN FEES (Differs by individual student and: 222 ⟵ “ESTIMATED LOAN FEES (Differs by individual student and | $222 | $222”
  - column:SUBTOTAL: 21326 ⟵ “SUBTOTAL | $21,326 | $31,214”
  - column:TRANSPORTATION: 3000 ⟵ “TRANSPORTATION | $3,000 | $3,000”
  - column:MISCELLANEOUS/PERSONAL: 2130 ⟵ “MISCELLANEOUS/PERSONAL | $2,130 | $2,130”
  - column:SUBTOTAL: 5130 ⟵ “SUBTOTAL | $5,130 | $5,130”
  - column:ESTIMATED TOTAL: 26456 ⟵ “ESTIMATED TOTAL | $26,456 | $36,344”
  - column:TUITION: 8328 ⟵ “TUITION | $8,328 | $16,656”
  - column:INSTITUTIONAL FEES (Health Insurance Fee, Athletic Fee,: 2920 ⟵ “INSTITUTIONAL FEES (Health Insurance Fee, Athletic Fee, | $2,920 | $2,920”
  - column:MEAL PLAN (Average Cost; Different Meal Plan Options: 4100 ⟵ “MEAL PLAN (Average Cost; Different Meal Plan Options | $4,100 | $4,100”
  - column:ESTIMATED LOAN FEES (Differs by individual student: 192 ⟵ “ESTIMATED LOAN FEES (Differs by individual student | $192 | $192”
  - column:SUBTOTAL: 27036 ⟵ “SUBTOTAL | $27,036 | $35,364”
  - … 20 more rows
### `6ada158c3a977987` Alabama State University — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.alasu.edu/financial-aid/tuition-costs.php (sha256 2ac949e75e49)
- issues: stale_year_label:2024-25, conflicting_sources:https://www.alasu.edu/_qa/24-25%20COA..pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition/Fees: 11068 ⟵ “Tuition/Fees | $11,068 | $19,936”
  - column:Room/Board: 6050 ⟵ “Room/Board | $6,050 | $6,050”
  - column:Subtotal: 17118 ⟵ “Subtotal | $17,118 | $25,986”
  - column:Books: 1320 ⟵ “Books | $1,320 | $1,320”
  - column:Transportation: 3000 ⟵ “Transportation | $3,000 | $3,000”
  - column:Miscellaneous / Personal: 2130 ⟵ “Miscellaneous / Personal | $2,130 | $2,130”
  - column:Subtotal: 6450 ⟵ “Subtotal | $6,450 | $6,450”
  - column:Estimated Total: 23568.0 ⟵ “Estimated Total | $23,568.00 | $32,436.00”
### `c685f2d9eb968841` Alabama State University — costs 2024-25 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.alasu.edu/financial-aid/tuition-costs.php (sha256 2ac949e75e49)
- issues: stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition/Fees: 19936 ⟵ “Tuition/Fees | $11,068 | $19,936”
  - column:Room/Board: 6050 ⟵ “Room/Board | $6,050 | $6,050”
  - column:Subtotal: 25986 ⟵ “Subtotal | $17,118 | $25,986”
  - column:Books: 1320 ⟵ “Books | $1,320 | $1,320”
  - column:Transportation: 3000 ⟵ “Transportation | $3,000 | $3,000”
  - column:Miscellaneous / Personal: 2130 ⟵ “Miscellaneous / Personal | $2,130 | $2,130”
  - column:Subtotal: 6450 ⟵ “Subtotal | $6,450 | $6,450”
  - column:Estimated Total: 32436.0 ⟵ “Estimated Total | $23,568.00 | $32,436.00”
### `3157c1d94604987f` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://auburn.edu/administration/finaid/scholarship/ (sha256 3946c51cb842)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - gpa_requirement: ACT Required* ⟵ “ACT Required* | 35–36”
### `55e8b6aa83a21d07` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://www.auburn.edu/administration/finaid/scholarship/ (sha256 59929b289e4b)
- issues: stale_year_label:2024-25
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $9,000 ⟵ “Spirit of Auburn Founders Scholarship | 3.5 | 30-32 | $9,000”
  - gpa_requirement: 3.5 ⟵ “Spirit of Auburn Founders Scholarship | 3.5 | 30-32 | $9,000”
  - test_requirement: ACT 30-32 ⟵ “Spirit of Auburn Founders Scholarship | 3.5 | 30-32 | $9,000”
### `69c7e2558283d3cc` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://auburn.edu/administration/finaid/scholarship/ (sha256 3946c51cb842)
- issues: stale_year_label:2024-25
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $5,000 ⟵ “Spirit of Auburn University Scholarship | 3.5 | 28-29 | $5,000”
  - gpa_requirement: 3.5 ⟵ “Spirit of Auburn University Scholarship | 3.5 | 28-29 | $5,000”
  - test_requirement: ACT 28-29 ⟵ “Spirit of Auburn University Scholarship | 3.5 | 28-29 | $5,000”
### `6d25952819fed954` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://auburn.edu/administration/finaid/scholarship/ (sha256 3946c51cb842)
- issues: stale_year_label:2024-25
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: Full Tuition and Student Services Fees*** ⟵ “Spirit of Auburn Presidential Excellence Award | 4.0 | 35-36 | Full Tuition and Student Services Fees***”
  - gpa_requirement: 4.0 ⟵ “Spirit of Auburn Presidential Excellence Award | 4.0 | 35-36 | Full Tuition and Student Services Fees***”
  - test_requirement: ACT 35-36 ⟵ “Spirit of Auburn Presidential Excellence Award | 4.0 | 35-36 | Full Tuition and Student Services Fees***”
### `a9fe4bf3dbc7ac92` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://www.auburn.edu/administration/finaid/scholarship/ (sha256 59929b289e4b)
- issues: stale_year_label:2024-25
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $7,000 ⟵ “Academic Charter Scholarship | 3.5 | 29–30 | $7,000”
  - gpa_requirement: 3.5 ⟵ “Academic Charter Scholarship | 3.5 | 29–30 | $7,000”
  - test_requirement: ACT 29–30 ⟵ “Academic Charter Scholarship | 3.5 | 29–30 | $7,000”
### `bbfdf3f467957fe9` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://auburn.edu/administration/finaid/scholarship/ (sha256 3946c51cb842)
- issues: stale_year_label:2024-25
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $11,000 ⟵ “Academic Heritage Scholarship | 3.5 | 31–32 | $11,000”
  - gpa_requirement: 3.5 ⟵ “Academic Heritage Scholarship | 3.5 | 31–32 | $11,000”
  - test_requirement: ACT 31–32 ⟵ “Academic Heritage Scholarship | 3.5 | 31–32 | $11,000”
### `bef2d99053eb0ebc` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://auburn.edu/administration/finaid/scholarship/ (sha256 3946c51cb842)
- issues: stale_year_label:2024-25
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $17,000 ⟵ “Academic Presidential Scholarship | 3.5 | 35–36 | $17,000”
  - gpa_requirement: 3.5 ⟵ “Academic Presidential Scholarship | 3.5 | 35–36 | $17,000”
  - test_requirement: ACT 35–36 ⟵ “Academic Presidential Scholarship | 3.5 | 35–36 | $17,000”
### `c080481a538ddaac` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://www.auburn.edu/administration/finaid/scholarship/ (sha256 59929b289e4b)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - gpa_requirement: ACT* 33–34 ⟵ “ACT* 33–34 | $15,000”
### `ced7604f679b1b37` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://www.auburn.edu/administration/finaid/scholarship/ (sha256 59929b289e4b)
- issues: stale_year_label:2024-25
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $11,500 ⟵ “Spirit of Auburn Presidential Scholarship | 3.5 | 33-36 | $11,500”
  - gpa_requirement: 3.5 ⟵ “Spirit of Auburn Presidential Scholarship | 3.5 | 33-36 | $11,500”
  - test_requirement: ACT 33-36 ⟵ “Spirit of Auburn Presidential Scholarship | 3.5 | 33-36 | $11,500”
### `deeb6de854478ed2` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://www.auburn.edu/administration/finaid/scholarship/ (sha256 59929b289e4b)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - gpa_requirement: $15,000 ⟵ “33–34 | $15,000 |  | ”
### `ed646828437e0da7` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://auburn.edu/administration/finaid/scholarship/ (sha256 3946c51cb842)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - gpa_requirement: ACT* 35–36 ⟵ “ACT* 35–36 | $17,000”
### `ee2b28b666426a08` Auburn University — awards 2024-25 [new] (labeled_in_source)
- source: https://auburn.edu/administration/finaid/scholarship/ (sha256 3946c51cb842)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - gpa_requirement: Estimated Annual Award ⟵ “Estimated Annual Award | Full Tuition and Student Services Fees***”
### `04f1dc0aee9c54cb` Auburn University — costs 2022-23 · residency=not_applicable [new] (labeled_in_source)
- source: https://ir.auburn.edu/factbook/tuition-and-fees/semester-tuitions-and-fees.php (sha256 5c3cbfc1cff9)
- issues: residency_unknown, stale_year_label:2022-23
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 5196 ⟵ “Tuition | $5,196 | $5,352 | $5,508 | $5,676 | $5,784”
  - column:Student Services Fee **: 892 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
### `3ddd4c4ca5f26fe3` Auburn University — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://ir.auburn.edu/factbook/tuition-and-fees/semester-tuitions-and-fees.php (sha256 5c3cbfc1cff9)
- issues: residency_unknown, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 5508 ⟵ “Tuition | $5,196 | $5,352 | $5,508 | $5,676 | $5,784”
  - column:Student Services Fee **: 937 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
### `52c6fc7c94e74bc8` Auburn University — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://ir.auburn.edu/factbook/tuition-and-fees/semester-tuitions-and-fees.php (sha256 5c3cbfc1cff9)
- issues: residency_unknown, stale_year_label:2023-24
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 5352 ⟵ “Tuition | $5,196 | $5,352 | $5,508 | $5,676 | $5,784”
  - column:Student Services Fee **: 916 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
### `6d07da155a0a17d5` Auburn University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://ir.auburn.edu/factbook/tuition-and-fees/semester-tuitions-and-fees.php (sha256 5c3cbfc1cff9)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 5784 ⟵ “Tuition | $5,196 | $5,352 | $5,508 | $5,676 | $5,784”
  - column:Student Services Fee **: 1002 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
### `9c7fda48c6e068bf` Auburn University — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://ir.auburn.edu/factbook/tuition-and-fees/semester-tuitions-and-fees.php (sha256 5c3cbfc1cff9)
- issues: ambiguous_year_labels, arrangement_unlabeled
- checks: {"columns": 5, "rows": 2}
  - column:Tuition: 15588 ⟵ “Tuition | $15,588 | $16,056 | $16,524 | $17,028 | $17,796”
  - column:Student Services Fee **: 892 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
  - column:Tuition: 16056 ⟵ “Tuition | $15,588 | $16,056 | $16,524 | $17,028 | $17,796”
  - column:Student Services Fee **: 916 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
  - column:Tuition: 16524 ⟵ “Tuition | $15,588 | $16,056 | $16,524 | $17,028 | $17,796”
  - column:Student Services Fee **: 937 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
  - column:Tuition: 17028 ⟵ “Tuition | $15,588 | $16,056 | $16,524 | $17,028 | $17,796”
  - column:Student Services Fee **: 983 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
  - column:Tuition: 17796 ⟵ “Tuition | $15,588 | $16,056 | $16,524 | $17,028 | $17,796”
  - column:Student Services Fee **: 1002 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
### `c3fef3ed8cbddbb3` Auburn University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://ir.auburn.edu/factbook/tuition-and-fees/semester-tuitions-and-fees.php (sha256 5c3cbfc1cff9)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 2}
  - column:Tuition: 5676 ⟵ “Tuition | $5,196 | $5,352 | $5,508 | $5,676 | $5,784”
  - column:Student Services Fee **: 983 ⟵ “Student Services Fee ** | $892 | $916 | $937 | $983 | $1,002”
### `a4de51f0e896a969` Auburn University at Montgomery — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.aum.edu/scholarships-and-financial-aid/financial-aid/award-information/ (sha256 8129dac168a0)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “There is no federal appeal procedure to consider special circumstances that may have led to your withdrawal or failure to complete to attend.”
### `ce9a6e38caa57f2d` Auburn University at Montgomery — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.aum.edu/scholarships-and-financial-aid/financial-aid/policies/satisfactory-academic-progress-policy/ (sha256 86a274e973ea)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “To submit an appeal, the student must document the extenuating or special circumstance(s) and indicate what has changed that will allow the student to meet the conditions by the next evaluation.”
### `19b9f6d0bbd95fe3` Auburn University at Montgomery — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.aum.edu/admissions/tuition-and-fees/ (sha256 30bf83ebe9e1)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Estimated Tuition/Fees*: 11276 ⟵ “Estimated Tuition/Fees* | $11,276 | $23,522”
  - on_campus:Estimated Loan Fees: 119 ⟵ “Estimated Loan Fees | $119 | $119”
  - on_campus:Books, Supplies, & Equipment: 1500 ⟵ “Books, Supplies, & Equipment | $1,500 | $1,500”
  - on_campus:Miscellaneous/Personal: 1530 ⟵ “Miscellaneous/Personal | $1,530 | $1,530”
  - on_campus:Transportation: 3150 ⟵ “Transportation | $3,150 | $3,500”
  - on_campus:Housing & Food: 13167 ⟵ “Housing & Food | $13,167 | $13,167”
  - on_campus:Total: 30742 ⟵ “Total | $30,742 | $43,338”
### `2bae7456cf419fa6` Auburn University at Montgomery — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.aum.edu/admissions/tuition-and-fees/ (sha256 30bf83ebe9e1)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Estimated Tuition/Fees*: 23522 ⟵ “Estimated Tuition/Fees* | $11,276 | $23,522”
  - on_campus:Estimated Loan Fees: 119 ⟵ “Estimated Loan Fees | $119 | $119”
  - on_campus:Books, Supplies, & Equipment: 1500 ⟵ “Books, Supplies, & Equipment | $1,500 | $1,500”
  - on_campus:Miscellaneous/Personal: 1530 ⟵ “Miscellaneous/Personal | $1,530 | $1,530”
  - on_campus:Transportation: 3500 ⟵ “Transportation | $3,150 | $3,500”
  - on_campus:Housing & Food: 13167 ⟵ “Housing & Food | $13,167 | $13,167”
  - on_campus:Total: 43338 ⟵ “Total | $30,742 | $43,338”
### `0180e0b98528e8a5` Bevill State Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.bscc.edu/students/financial-aid/professional-judgment (sha256 2190bf2c9ed8)
- issues: semantic_review_required, conflicting_sources:https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2025-26(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2026-27%20Fillable(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/images/SAP%20Appeal%20Form%202024-2025.pdf
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances may include but are not limited to: Loss or reduction of employment, wages, or unemployment compensation Loss of untaxed income or benefits e.g.”
  - sentence: need_based_special_circumstances ⟵ “Social Security benefits or child support Separation or divorce Death of a parent or spouse Unusually high medical expenses If you believe you qualify for an adjustment due to a special circumstance, please complete the form below and return it to the Office of Student Services.”
  - sentence: need_based_special_circumstances ⟵ “Expected Income Form 2026-2027 (PDF) Unusual Circumstances Unusual Circumstances refer to certain conditions that may justify the adjustment of a student’s dependency status.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances may include but are not limited to: Parental abandonment Incarceration Human trafficking Refugee or asylee status If you believe you qualify for an adjustment due to an unusual circumstance, please complete the form below and return it to the Office of Student Services.”
### `28c3d71ad0ba4c6c` Bevill State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bscc.edu/Content/Uploads/bscc.edu/images/SAP%20Appeal%20Form%202024-2025.pdf (sha256 d3861b004d9b)
- issues: semantic_review_required, conflicting_sources:https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2025-26(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2026-27%20Fillable(1).pdf,https://www.bscc.edu/students/financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please attach a typewritten explanation of unusual circumstances associated with unsatisfactory academic progress.”
### `3c644422705c98fe` Bevill State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2026-27%20Fillable(1).pdf (sha256 08e6ec101446)
- issues: semantic_review_required, conflicting_sources:https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2025-26(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/images/SAP%20Appeal%20Form%202024-2025.pdf,https://www.bscc.edu/students/financial-aid/appeal-process
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Submission of a SAP Appeal does not guarantee reinstatement of Financial Aid eligibility.”
  - sentence: sap_appeal ⟵ “APPEAL RESULTS & STUDENT ACKNOWLEDGMENTS – PLEASE READ AND SIGN If my appeal is DENIED, by signing below I understand that decisions are processed on a case-by-case basis and the committee may deny any SAP appeal.”
### `4abee2e816b62f43` Bevill State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2025-26(1).pdf (sha256 62cf3de7b032)
- issues: semantic_review_required, conflicting_sources:https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2026-27%20Fillable(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/images/SAP%20Appeal%20Form%202024-2025.pdf,https://www.bscc.edu/students/financial-aid/appeal-process
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Submission of a SAP Appeal does not guarantee reinstatement of Financial Aid eligibility.”
  - sentence: sap_appeal ⟵ “APPEAL RESULTS & STUDENT ACKNOWLEDGMENTS – PLEASE READ AND SIGN If my appeal is DENIED, by signing below I understand that decisions are processed on a case-by-case basis and the committee may deny any SAP appeal.”
### `782d2675473356c7` Bevill State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2026-27%20Fillable(1).pdf (sha256 08e6ec101446)
- issues: semantic_review_required, conflicting_sources:https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2025-26(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/images/SAP%20Appeal%20Form%202024-2025.pdf,https://www.bscc.edu/students/financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please attach a typewritten explanation of unusual circumstances associated with unsatisfactory academic progress.”
### `7f7a6fc1de5a1c19` Bevill State Community College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bscc.edu/students/financial-aid/appeal-process (sha256 b7e215717b09)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2025-26(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2026-27%20Fillable(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/images/SAP%20Appeal%20Form%202024-2025.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “To view your Satisfactory Academic Progress (SAP) please follow the steps below Log into MyBSCC Click Open Student Dashboard Click Financial Aid Dashboard Select the appropriate Award Year Click Satisfactory Academic Progress MyBSCC Login Help Appeal decisions are sent to the student’s MyBSCC account.”
### `e310b83c001b23b9` Bevill State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2025-26(1).pdf (sha256 62cf3de7b032)
- issues: semantic_review_required, conflicting_sources:https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2026-27%20Fillable(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/images/SAP%20Appeal%20Form%202024-2025.pdf,https://www.bscc.edu/students/financial-aid/professional-judgment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please attach a typewritten explanation of unusual circumstances associated with unsatisfactory academic progress.”
### `f567f3d274748e9f` Bevill State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bscc.edu/Content/Uploads/bscc.edu/images/SAP%20Appeal%20Form%202024-2025.pdf (sha256 d3861b004d9b)
- issues: semantic_review_required, conflicting_sources:https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2025-26(1).pdf,https://www.bscc.edu/Content/Uploads/bscc.edu/files/SAP%20Appeal%20Form%2026-27%20Fillable(1).pdf,https://www.bscc.edu/students/financial-aid/appeal-process
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Submission of a SAP Appeal does not guarantee reinstatement of Financial Aid eligibility.”
  - sentence: sap_appeal ⟵ “APPEAL RESULTS & STUDENT ACKNOWLEDGMENTS – PLEASE READ AND SIGN If my appeal is DENIED, by signing below I understand that decisions are processed on a case-by-case basis and the committee may deny any SAP appeal.”
### `5272fd8e96aa2366` Bevill State Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bscc.edu/students/financial-aid/cost-of-attendance (sha256 45429e0b5da6)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 14}
  - on_campus:Tuition ₁: 3724.0 ⟵ “Tuition ₁ | $3,724.00 | $3,724.00 | $3,724.00”
  - on_campus:Bond Reserve Fee ₁: 28.0 ⟵ “Bond Reserve Fee ₁ | $28.00 | $28.00 | $28.00”
  - on_campus:Facilities Renewal Fee ₁: 420.0 ⟵ “Facilities Renewal Fee ₁ | $420.00 | $420.00 | $420.00”
  - on_campus:Technology Fee ₁: 420.0 ⟵ “Technology Fee ₁ | $420.00 | $420.00 | $420.00”
  - on_campus:Library Fee ₁: 30.0 ⟵ “Library Fee ₁ | $30.00 | $30.00 | $30.00”
  - on_campus:Building Fee ₁: 280.0 ⟵ “Building Fee ₁ | $280.00 | $280.00 | $280.00”
  - on_campus:ACCS Enhancement Fee ₁: 560.0 ⟵ “ACCS Enhancement Fee ₁ | $560.00 | $560.00 | $560.00”
  - on_campus:Bear Essentials Book Fee ₁: 756.0 ⟵ “Bear Essentials Book Fee ₁ | $756.00 | $756.00 | $756.00”
  - on_campus:Books, Course Materials, Supplies, and Equipment ₂: 711.0 ⟵ “Books, Course Materials, Supplies, and Equipment ₂ | $711.00 | $711.00 | $711.00”
  - on_campus:Transportation ₂: 2700.0 ⟵ “Transportation ₂ | $2,700.00 | $2,700.00 | $2,700.00”
  - on_campus:Miscellaneous and Personal ₂: 2400.0 ⟵ “Miscellaneous and Personal ₂ | $2,400.00 | $2,400.00 | $2,400.00”
  - on_campus:Food and Housing ₂: 4803.0 ⟵ “Food and Housing ₂ | $4,803.00 | $2,628.00 | $12,843.00”
  - on_campus:Total Cost of Attendance: 16832.0 ⟵ “Total Cost of Attendance | $16,832.00 | $14,657.00 | $24,872.00”
  - on_campus:Total Tuition & Fees ₁: 6218.0 ⟵ “Total Tuition & Fees ₁ | $6218.00 | $6218.00 | $6218.00”
  - with_parents_or_family:Tuition ₁: 3724.0 ⟵ “Tuition ₁ | $3,724.00 | $3,724.00 | $3,724.00”
  - with_parents_or_family:Bond Reserve Fee ₁: 28.0 ⟵ “Bond Reserve Fee ₁ | $28.00 | $28.00 | $28.00”
  - with_parents_or_family:Facilities Renewal Fee ₁: 420.0 ⟵ “Facilities Renewal Fee ₁ | $420.00 | $420.00 | $420.00”
  - with_parents_or_family:Technology Fee ₁: 420.0 ⟵ “Technology Fee ₁ | $420.00 | $420.00 | $420.00”
  - with_parents_or_family:Library Fee ₁: 30.0 ⟵ “Library Fee ₁ | $30.00 | $30.00 | $30.00”
  - with_parents_or_family:Building Fee ₁: 280.0 ⟵ “Building Fee ₁ | $280.00 | $280.00 | $280.00”
  - with_parents_or_family:ACCS Enhancement Fee ₁: 560.0 ⟵ “ACCS Enhancement Fee ₁ | $560.00 | $560.00 | $560.00”
  - with_parents_or_family:Bear Essentials Book Fee ₁: 756.0 ⟵ “Bear Essentials Book Fee ₁ | $756.00 | $756.00 | $756.00”
  - with_parents_or_family:Books, Course Materials, Supplies, and Equipment ₂: 711.0 ⟵ “Books, Course Materials, Supplies, and Equipment ₂ | $711.00 | $711.00 | $711.00”
  - with_parents_or_family:Transportation ₂: 2700.0 ⟵ “Transportation ₂ | $2,700.00 | $2,700.00 | $2,700.00”
  - with_parents_or_family:Miscellaneous and Personal ₂: 2400.0 ⟵ “Miscellaneous and Personal ₂ | $2,400.00 | $2,400.00 | $2,400.00”
  - … 17 more rows
### `m13958fa57f47530` Bevill State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://www.bscc.edu/students/scholarship-applications/bevill-state-dual-enrollment-scholarship-application (sha256 4ca7c6b6cc33)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "merged_pages": 2, "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “The student provides certification from the local principal and/or designee certifying that the student has a minimum cumulative 3.0 GPA average and recommending the student be admitted under this policy;”
  - eligibility_tier: 2.5 ⟵ “The student must have a 2.5 GPA average for Academic coursework or the program specific GPA requirement for Career Technical coursework, as defined by board policy, in completed high school courses.”
  - state_grant_accepted: True ⟵ “The Summer Honors and Dual Enrollment Scholarship Application is available during the spring semester within each student’s Applicant Dashboard. Each student will log in with the username and password they created when applying to the college through our website (https://www.bscc.edu). If a student ”
  - eligibility_tier: 2.5 ⟵ “Applicants applying for the Dual Enrollment Scholarship must meet High School Admission requirements, have a minimum 2.5 High School GPA, complete an Application for Admission, and complete the Dual Enrollment Authorization Form.”
  - state_grant_accepted: True ⟵ “The Summer Honors Scholarship covers the cost of tuition for one course (maximum of 4 credit hours) to be taken during the Summer semester of 2026. Summer Honors Scholarship recipients must pay for all fees, books, supplies, and any tuition charges above 4 credit hours. This scholarship cannot be co”
  - state_grant_accepted: True ⟵ “The 2026-27 Dual Enrollment Scholarship covers required tuition, fees, and books for a maximum of 2 courses plus ORI 107 per semester (Fall 2026, Spring 2027, & Summer 2027) . The actual number of courses allowed will be dependent upon funding.”
### `204368e6dac87f32` Bishop State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bishop.edu/financial-affairs/office-of-financial-aid/appeals (sha256 4517d6575a70)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Appeal You must file an appeal if you are failing the minimum GPA and/or Pace progress standards or you have exceeded the maximum timeframe allowed by your current major/program.”
### `3cec2daf908c8ff3` Bishop State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bishop.edu/financial-affairs/office-of-financial-aid/appeals (sha256 4517d6575a70)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances (Dependency Status Review/Dependency Override) Students who do not meet the federal criteria to be considered Independent based on the Free Application for Federal Student Aid (FAFSA) may have unusual circumstances that warrant a dependency status review.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances (Loss of Income) The Free Application for Federal Student Aid (FAFSA) uses prior-prior year income information.”
  - sentence: need_based_special_circumstances ⟵ “Any students (or parents – if student is dependent) who experienced a significant and involuntary loss of income between the income year reported on the FAFSA and the current year may request a special circumstances review.”
  - sentence: need_based_special_circumstances ⟵ “This review is an extensive process which includes the following steps: Student requests a special circumstances review from the Financial Aid Office.”
### `e6bc33b3ccb204a3` Bishop State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bishop.edu/financial-affairs/office-of-financial-aid/appeals (sha256 4517d6575a70)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “When there are unusual situations or circumstances that impact your federal student aid eligibility, federal regulations give a financial aid administrator discretion or professional judgment on a case-by-case basis and with adequate documentation to make adjustments to the data elements on the Free Application for Federal Student Aid (FAFSA®) form that impact your Expected Family Contribution (EF”
  - sentence: professional_judgment ⟵ “Professional Judgment Professional Judgment refers to an institution’s authority to make certain adjustments, on a case-by-case basis, to information reported on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: professional_judgment ⟵ “There are limited circumstances in which the use of Professional Judgment is warranted, and all circumstances must be thoroughly documented.”
  - sentence: professional_judgment ⟵ “The Professional Judgment process is extensive and requires a thorough review by the Financial Aid Office to determine what, if any, changes may be appropriate.”
  - sentence: professional_judgment ⟵ “The results of a Professional Judgment review are final and cannot be appealed.”
  - sentence: professional_judgment ⟵ “Request for Professional Judgment does not guarantee approval.”
### `05fd5038408900bb` Bishop State Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bishop.edu/assets/uploads/pages/2026-2027-COA-PDF-for-Website.pdf (sha256 5be9e83ad3f6)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 16, "rows": 11}
  - column:Tuition & Fees: 3060.0 ⟵ “Tuition & Fees | $3,060.00 | $3,060.00 | Tuition & Fees | $5,055.00 | $5,055.00”
  - column:Books & Supplies*: 555.0 ⟵ “Books & Supplies* | $555.00 | $555.00 | Books & Supplies* | $555.00 | $555.00”
  - column:Housing & Food: 6879.0 ⟵ “Housing & Food | $6,879.00 | $4,629.00 | Housing & Food | $6,879.00 | $4,629.00”
  - column:Transportation: 1130.0 ⟵ “Transportation | $1,130.00 | $1,130.00 | Transportation | $1,695.00 | $1,695.00”
  - column:Miscellaneous: 565.0 ⟵ “Miscellaneous | $565.00 | $565.00 | Miscellaneous | $565.00 | $565.00”
  - column:Total: 12189.0 ⟵ “Total | $12,189.00 | $9,939.00 | Total | $14,749.00 | $12,499.00”
  - column:Tuition & Fees: 3060.0 ⟵ “Tuition & Fees | $3,060.00 | $3,060.00 | Tuition & Fees | $5,055.00 | $5,055.00”
  - column:Books & Supplies*: 555.0 ⟵ “Books & Supplies* | $555.00 | $555.00 | Books & Supplies* | $555.00 | $555.00”
  - column:Housing & Food: 6879.0 ⟵ “Housing & Food | $6,879.00 | $4,629.00 | Housing & Food | $6,879.00 | $4,629.00”
  - column:Transportation: 1130.0 ⟵ “Transportation | $1,130.00 | $1,130.00 | Transportation | $1,695.00 | $1,695.00”
  - column:Miscellaneous: 565.0 ⟵ “Miscellaneous | $565.00 | $565.00 | Miscellaneous | $565.00 | $565.00”
  - column:Total: 12189.0 ⟵ “Total | $12,189.00 | $9,939.00 | Total | $14,749.00 | $12,499.00”
  - column:Tuition & Fees: 1224.0 ⟵ “Tuition & Fees | $1,224.00 | $1,224.00 | Tuition & Fees | $2,022.00 | $2,022.00”
  - column:Books & Supplies*: 222.0 ⟵ “Books & Supplies* | $222.00 | $222.00 | Books & Supplies* | $222.00 | $222.00”
  - column:Housing & Food: 2424.0 ⟵ “Housing & Food | $2,424.00 | $2,976.00 | Housing & Food | $2,424.00 | $2,976.00”
  - column:Transportation: 720.0 ⟵ “Transportation | $720.00 | $720.00 | Transportation | $1,080.00 | $1,080.00”
  - column:Miscellaneous: 360.0 ⟵ “Miscellaneous | $360.00 | $360.00 | Miscellaneous | $360.00 | $360.00”
  - column:Total: 4950.0 ⟵ “Total | $4,950.00 | $5,502.00 | Total | $6,108.00 | $6,660.00”
  - column:Tuition & Fees: 6120.0 ⟵ “Tuition & Fees | $6,120.00 | $6,120.00 | Tuition & Fees | $10,110.00 | $10,110.00”
  - column:Books & Supplies*: 1110.0 ⟵ “Books & Supplies* | $1,110.00 | $1,110.00 | Books & Supplies* | $1,110.00 | $1,110.00”
  - column:Housing & Food: 13758.0 ⟵ “Housing & Food | $13,758.00 | $9,258.00 | Housing & Food | $13,758.00 | $9,258.00”
  - column:Transportation: 2260.0 ⟵ “Transportation | $2,260.00 | $2,260.00 | Transportation | $3,390.00 | $3,390.00”
  - column:Miscellaneous: 1130.0 ⟵ “Miscellaneous | $1,130.00 | $1,130.00 | Miscellaneous | $1,130.00 | $1,130.00”
  - column:Total: 24378.0 ⟵ “Total | $24,378.00 | $19,878.00 | Total | $29,498.00 | $24,998.00”
  - column:Tuition & Fees: 4284.0 ⟵ “Tuition & Fees | $4,284.00 | $4,284.00 | Tuition & Fees | $7,077.00 | $7,077.00”
  - … 151 more rows
### `5ccc6f5a5a458ad8` Bishop State Community College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bishop.edu/assets/uploads/pages/24-25-Bishop-COA.pdf (sha256 93e10b64c08c)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 6, "rows": 15}
  - column:Tuition & Fees: 2670.0 ⟵ “Tuition & Fees | $2,670.00 | $2,670.00 | Tuition & Fees | $4,605.00 | $4,605.00”
  - column:Books & Supplies*: 1200.0 ⟵ “Books & Supplies* | $1,200.00 | $1,200.00 | Books & Supplies* | $1,200.00 | $1,200.00”
  - column:Housing & Food: 6879.0 ⟵ “Housing & Food | $6,879.00 | $4,629.00 | Housing & Food | $6,879.00 | $4,629.00”
  - column:Transportation: 1130.0 ⟵ “Transportation | $1,130.00 | $1,130.00 | Transportation | $1,695.00 | $1,695.00”
  - column:Miscellaneous: 565.0 ⟵ “Miscellaneous | $565.00 | $565.00 | Miscellaneous | $565.00 | $565.00”
  - column:Total: 12444.0 ⟵ “Total | $12,444.00 | $10,194.00 | Total | $14,944.00 | $12,694.00”
  - column:Tuition & Fees: 2670.0 ⟵ “Tuition & Fees | $2,670.00 | $2,670.00 | Tuition & Fees | $4,605.00 | $4,605.00”
  - column:Books & Supplies*: 1200.0 ⟵ “Books & Supplies* | $1,200.00 | $1,200.00 | Books & Supplies* | $1,200.00 | $1,200.00”
  - column:Housing & Food: 6879.0 ⟵ “Housing & Food | $6,879.00 | $4,629.00 | Housing & Food | $6,879.00 | $4,629.00”
  - column:Transportation: 1130.0 ⟵ “Transportation | $1,130.00 | $1,130.00 | Transportation | $1,695.00 | $1,695.00”
  - column:Miscellaneous: 565.0 ⟵ “Miscellaneous | $565.00 | $565.00 | Miscellaneous | $565.00 | $565.00”
  - column:Total: 12444.0 ⟵ “Total | $12,444.00 | $10,194.00 | Total | $14,944.00 | $12,694.00”
  - column:Tuition & Fees: 1068.0 ⟵ “Tuition & Fees | $1,068.00 | $1,068.00 | Tuition & Fees | $1,842.00 | $1,842.00”
  - column:Books & Supplies*: 480.0 ⟵ “Books & Supplies* | $480.00 | $480.00 | Books & Supplies* | $480.00 | $480.00”
  - column:Housing & Food: 2424.0 ⟵ “Housing & Food | $2,424.00 | $2,976.00 | Housing & Food | $2,424.00 | $2,976.00”
  - column:Transportation: 720.0 ⟵ “Transportation | $720.00 | $720.00 | Transportation | $1,080.00 | $1,080.00”
  - column:Miscellaneous: 360.0 ⟵ “Miscellaneous | $360.00 | $360.00 | Miscellaneous | $360.00 | $360.00”
  - column:Total: 5052.0 ⟵ “Total | $5,052.00 | $5,604.00 | Total | $6,186.00 | $6,738.00”
  - column:Tuition & Fees: 5340.0 ⟵ “Tuition & Fees | $5,340.00 | $5,340.00 | Tuition & Fees | $9,210.00 | $9,210.00”
  - column:Books & Supplies*: 2400.0 ⟵ “Books & Supplies* | $2,400.00 | $2,400.00 | Books & Supplies* | $2,400.00 | $2,400.00”
  - column:Housing & Food: 13758.0 ⟵ “Housing & Food | $13,758.00 | $9,258.00 | Housing & Food | $13,758.00 | $9,258.00”
  - column:Transportation: 2260.0 ⟵ “Transportation | $2,260.00 | $2,260.00 | Transportation | $3,390.00 | $3,390.00”
  - column:Miscellaneous: 1130.0 ⟵ “Miscellaneous | $1,130.00 | $1,130.00 | Miscellaneous | $1,130.00 | $1,130.00”
  - column:Total: 24888.0 ⟵ “Total | $24,888.00 | $20,388.00 | Total | $29,888.00 | $25,388.00”
  - column:Tuition & Fees: 3738.0 ⟵ “Tuition & Fees | $3,738.00 | $3,738.00 | Tuition & Fees | $6,447.00 | $6,447.00”
  - … 152 more rows
### `351f4feb0e3c8fc5` Central Alabama Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cacc.edu/admissions-and-aid/sap-appeal-process (sha256 f43ad8606d04)
- issues: semantic_review_required, conflicting_sources:https://www.cacc.edu/admissions-and-aid/financial-aid-faqs,https://www.cacc.edu/content/userfiles/files/2627%20satisfactory-academic-progress%20policy.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Please note that there is a deadline for submitting a SAP appeal for each term.”
  - sentence: sap_appeal ⟵ “Fall SAP Appeal Deadline: November 21, 2026 Spring SAP Appeal Deadline: April 3, 2027 Summer SAP Appeal Deadline: July 8, 2027 What happens next?”
  - sentence: sap_appeal ⟵ “You may access Inceptia SAP Advisor for FALL 2026 at this link - Inceptia link to appeal for Fall 2027 Fall SAP Appeal Deadline: November 21, 2026 You may access Inceptia SAP Advisor or Spring 2027 at this link - Will open in December Spring SAP Appeal Deadline: April 3, 2027 You may access Inceptia SAP Advisor or Summer 2027 at this link - Will open in April Summer SAP Appeal Deadline: July 8, 20”
### `468c7530303d8d87` Central Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cacc.edu/content/userfiles/files/2627%20satisfactory-academic-progress%20policy.pdf (sha256 bb1cb0777da3)
- issues: semantic_review_required, conflicting_sources:https://www.cacc.edu/admissions-and-aid/financial-aid-faqs,https://www.cacc.edu/admissions-and-aid/sap-appeal-process
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Additional degree reviews are not considered Satisfactory Academic Progress (SAP) appeals. 1 Central Alabama Community College Warning Semester If a student fails to meet the Qualitative Standard – Grade Point Average (GPA) and/or the Quantitative Standard – Completion Rate / PACE of Progression (PACE) for Satisfactory Academic Progress, the student will be placed on “warning” for one semester.”
### `b7753b5789053223` Central Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cacc.edu/admissions-and-aid/financial-aid-faqs (sha256 bd2812ccd5e1)
- issues: semantic_review_required, conflicting_sources:https://www.cacc.edu/admissions-and-aid/sap-appeal-process,https://www.cacc.edu/content/userfiles/files/2627%20satisfactory-academic-progress%20policy.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If a student failed to make SAP (GPA, PACE, GPAPCE) or has reached maximum time frame (MAX or MTHMX), the student may file an appeal by submitting a Satisfactory Academic Progress Appeal Request Form and submit any required supporting documentation to the CACC Inceptia Satisfactory Academic Progress portal.”
### `7ad71efa9cb4ea3b` Central Alabama Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.cacc.edu/content/userfiles/files/2024-2025%20Cost%20of%20Attendance.pdf (sha256 f5b8cec3c572)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.cacc.edu/content/userfiles/files/2526-COA-FOR-WEB.pdf,https://www.cacc.edu/content/userfiles/files/2627%20COA%20pdf(1).pdf
- checks: {"columns": 13, "rows": 12}
  - with_parents_or_family:TOTAL $: 4026 ⟵ “TOTAL $ | 4,026 | $ | 6,796 | $ | 14,458 | $ | 18,543 | TOTAL $ | 8,856 | $ | 13,238 | $ | 29,013 | $ | 37,872”
  - with_parents_or_family:AVERAGE NURSING FEES $: 847 ⟵ “AVERAGE NURSING FEES $ | 847 | $ | 847 | $ | 1,694 | $ | 2,541 | AVERAGE NURSING FEES $ | 847 | $ | 847 | $ | 1,694 | $ | 2,541”
  - with_parents_or_family:AVERAGE RN MOBILITY FEES $: 592 ⟵ “AVERAGE RN MOBILITY FEES $ | 592 | $ | 592 | $ | 1,184 | $ | 1,776 | AVERAGE RN MOBILITY FEES $ | 592 | $ | 592 | $ | 1,184 | $ | 1,776”
  - with_parents_or_family:AVERAGE PRACTICAL NURSING CERTIFICATE FEES $: 708 ⟵ “AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 708 | $ | 708 | $ | 1,416 | $ | 2,124 | AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 708 | $ | 708 | $ | 1,416 | $ | 2,124”
  - with_parents_or_family:AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $: 61 ⟵ “AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183 | AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183”
  - with_parents_or_family:AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $: 60 ⟵ “AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE COSMETOLOGY FEES $: 46 ⟵ “AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138 | AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138”
  - with_parents_or_family:AVERAGE INDUSTRIAL ELECTRONICS FEES $: 60 ⟵ “AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE MACHINE SHOP FEES $: 16 ⟵ “AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48 | AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48”
  - with_parents_or_family:AVERAGE WELDING ‐ DRAFTING FEES $: 7 ⟵ “AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 14 | $ | 21 | AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 14 | $ | 21”
  - with_parents_or_family:AVERAGE WELDING ‐ MACHINING FEES $: 11 ⟵ “AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33 | AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33”
  - with_parents_or_family:AVERAGE MARINE TECHNOLOGY FEES $: 53 ⟵ “AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 159 | AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 159”
  - with_parents_or_family:TOTAL $: 4800 ⟵ “TOTAL $ | 4,800 | $ | 8,731 | $ | 18,328 | $ | 23,187 | TOTAL $ | 9,630 | $ | 15,173 | $ | 32,883 | $ | 42,516”
  - with_parents_or_family:AVERAGE NURSING FEES $: 847 ⟵ “AVERAGE NURSING FEES $ | 847 | $ | 847 | $ | 1,694 | $ | 2,541 | AVERAGE NURSING FEES $ | 847 | $ | 847 | $ | 1,694 | $ | 2,541”
  - with_parents_or_family:AVERAGE RN MOBILITY FEES $: 592 ⟵ “AVERAGE RN MOBILITY FEES $ | 592 | $ | 592 | $ | 1,184 | $ | 1,776 | AVERAGE RN MOBILITY FEES $ | 592 | $ | 592 | $ | 1,184 | $ | 1,776”
  - with_parents_or_family:AVERAGE PRACTICAL NURSING CERTIFICATE FEES $: 708 ⟵ “AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 708 | $ | 708 | $ | 1,416 | $ | 2,124 | AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 708 | $ | 708 | $ | 1,416 | $ | 2,124”
  - with_parents_or_family:AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $: 61 ⟵ “AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183 | AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183”
  - with_parents_or_family:AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $: 60 ⟵ “AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE COSMETOLOGY FEES $: 46 ⟵ “AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138 | AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138”
  - with_parents_or_family:AVERAGE INDUSTRIAL ELECTRONICS FEES $: 60 ⟵ “AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE MACHINE SHOP FEES $: 16 ⟵ “AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48 | AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48”
  - with_parents_or_family:AVERAGE WELDING ‐ DRAFTING FEES $: 7 ⟵ “AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 14 | $ | 21 | AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 14 | $ | 21”
  - with_parents_or_family:AVERAGE WELDING ‐ MACHINING FEES $: 11 ⟵ “AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33 | AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33”
  - with_parents_or_family:AVERAGE MARINE TECHNOLOGY FEES $: 53 ⟵ “AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 159 | AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 159”
  - column:TUITION & FEES: 1025 ⟵ “TUITION & FEES | $ | 1,025 | $ | 2,555 | $ | 5,110 | $ | 6,135 | TUITION & FEES | $ | 1,025 | $ | 2,555 | $ | 5,110 | $ | 6,135”
  - … 263 more rows
### `ca0598099e6be4b2` Central Alabama Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.cacc.edu/content/userfiles/files/2627%20COA%20pdf(1).pdf (sha256 610cedcd1326)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.cacc.edu/content/userfiles/files/2024-2025%20Cost%20of%20Attendance.pdf,https://www.cacc.edu/content/userfiles/files/2526-COA-FOR-WEB.pdf
- checks: {"columns": 13, "rows": 12}
  - with_parents_or_family:TOTAL $: 5967 ⟵ “TOTAL $ | 5,967 | $ | 10,420 | $ | 20,463 | $ | 26,797 | TOTAL $ | 9,511 | $ | 15,737 | $ | 31,467 | $ | 40,974”
  - with_parents_or_family:AVERAGE NURSING FEES $: 1029 ⟵ “AVERAGE NURSING FEES $ | 1,029 | $ | 1,029 | $ | 2,058 | $ | 3,087 | AVERAGE NURSING FEES $ | 1,029 | $ | 1,029 | $ | 2,058 | $ | 3,087”
  - with_parents_or_family:AVERAGE RN MOBILITY FEES $: 750 ⟵ “AVERAGE RN MOBILITY FEES $ | 750 | $ | 750 | $ | 1,500 | $ | 2,250 | AVERAGE RN MOBILITY FEES $ | 750 | $ | 750 | $ | 1,500 | $ | 2,250”
  - with_parents_or_family:AVERAGE PRACTICAL NURSING CERTIFICATE FEES $: 1036 ⟵ “AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 1,036 | $ | 1,036 | $ | 2,612 | $ | 3,108 | AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 1,036 | $ | 1,036 | $ | 2,612 | $ | 3,108”
  - with_parents_or_family:AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $: 61 ⟵ “AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183 | AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183”
  - with_parents_or_family:AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $: 60 ⟵ “AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE COSMETOLOGY FEES $: 46 ⟵ “AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138 | AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138”
  - with_parents_or_family:AVERAGE INDUSTRIAL ELECTRONICS FEES $: 60 ⟵ “AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE MACHINE SHOP FEES $: 16 ⟵ “AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48 | AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48”
  - with_parents_or_family:AVERAGE WELDING ‐ DRAFTING FEES $: 7 ⟵ “AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 98 | $ | 21 | AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 98 | $ | 21”
  - with_parents_or_family:AVERAGE WELDING ‐ MACHINING FEES $: 11 ⟵ “AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33 | AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33”
  - with_parents_or_family:AVERAGE MARINE TECHNOLOGY FEES $: 53 ⟵ “AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 69 | AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 69”
  - with_parents_or_family:TOTAL $: 6753 ⟵ “TOTAL $ | 6,753 | $ | 12,385 | $ | 26,493 | $ | 31,513 | TOTAL $ | 10,297 | $ | 17,702 | $ | 37,497 | $ | 45,690”
  - with_parents_or_family:AVERAGE NURSING FEES $: 1029 ⟵ “AVERAGE NURSING FEES $ | 1,029 | $ | 1,029 | $ | 2,058 | $ | 3,087 | AVERAGE NURSING FEES $ | 1,029 | $ | 1,029 | $ | 2,058 | $ | 3,087”
  - with_parents_or_family:AVERAGE RN MOBILITY FEES $: 750 ⟵ “AVERAGE RN MOBILITY FEES $ | 750 | $ | 750 | $ | 1,500 | $ | 2,250 | AVERAGE RN MOBILITY FEES $ | 750 | $ | 750 | $ | 1,500 | $ | 2,250”
  - with_parents_or_family:AVERAGE PRACTICAL NURSING CERTIFICATE FEES $: 1036 ⟵ “AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 1,036 | $ | 1,036 | $ | 2,612 | $ | 3,108 | AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 1,036 | $ | 1,036 | $ | 2,612 | $ | 3,108”
  - with_parents_or_family:AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $: 61 ⟵ “AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183 | AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183”
  - with_parents_or_family:AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $: 60 ⟵ “AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE COSMETOLOGY FEES $: 46 ⟵ “AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138 | AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138”
  - with_parents_or_family:AVERAGE INDUSTRIAL ELECTRONICS FEES $: 60 ⟵ “AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE MACHINE SHOP FEES $: 16 ⟵ “AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48 | AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48”
  - with_parents_or_family:AVERAGE WELDING ‐ DRAFTING FEES $: 7 ⟵ “AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 98 | $ | 21 | AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 98 | $ | 21”
  - with_parents_or_family:AVERAGE WELDING ‐ MACHINING FEES $: 11 ⟵ “AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33 | AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33”
  - with_parents_or_family:AVERAGE MARINE TECHNOLOGY FEES $: 53 ⟵ “AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 69 | AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 69”
  - column:TUITION & FEES: 1181 ⟵ “TUITION & FEES | $ | 1,181 | $ | 2,945 | $ | 5,885 | $ | 7,061 | TUITION & FEES | $ | 1,181 | $ | 2,945 | $ | 5,885 | $ | 7,061”
  - … 263 more rows
### `f43caaeba8a2eea6` Central Alabama Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.cacc.edu/content/userfiles/files/2526-COA-FOR-WEB.pdf (sha256 7cdde94d2679)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.cacc.edu/content/userfiles/files/2024-2025%20Cost%20of%20Attendance.pdf,https://www.cacc.edu/content/userfiles/files/2627%20COA%20pdf(1).pdf
- checks: {"columns": 13, "rows": 12}
  - with_parents_or_family:TOTAL $: 7313 ⟵ “TOTAL $ | 7,313 | $ | 12,357 | $ | 24,708 | $ | 32,014 | TOTAL $ | 11,532 | $ | 18,688 | $ | 37,368 | $ | 48,897”
  - with_parents_or_family:AVERAGE NURSING FEES $: 895 ⟵ “AVERAGE NURSING FEES $ | 895 | $ | 895 | $ | 1,790 | $ | 2,685 | AVERAGE NURSING FEES $ | 895 | $ | 895 | $ | 1,790 | $ | 2,685”
  - with_parents_or_family:AVERAGE RN MOBILITY FEES $: 620 ⟵ “AVERAGE RN MOBILITY FEES $ | 620 | $ | 620 | $ | 1,240 | $ | 1,860 | AVERAGE RN MOBILITY FEES $ | 620 | $ | 620 | $ | 1,240 | $ | 1,860”
  - with_parents_or_family:AVERAGE PRACTICAL NURSING CERTIFICATE FEES $: 718 ⟵ “AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 718 | $ | 718 | $ | 1,436 | $ | 2,154 | AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 718 | $ | 718 | $ | 1,436 | $ | 2,154”
  - with_parents_or_family:AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $: 61 ⟵ “AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183 | AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183”
  - with_parents_or_family:AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $: 60 ⟵ “AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE COSMETOLOGY FEES $: 46 ⟵ “AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138 | AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138”
  - with_parents_or_family:AVERAGE INDUSTRIAL ELECTRONICS FEES $: 60 ⟵ “AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE MACHINE SHOP FEES $: 16 ⟵ “AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48 | AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48”
  - with_parents_or_family:AVERAGE WELDING ‐ DRAFTING FEES $: 7 ⟵ “AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 14 | $ | 21 | AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 14 | $ | 21”
  - with_parents_or_family:AVERAGE WELDING ‐ MACHINING FEES $: 11 ⟵ “AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33 | AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33”
  - with_parents_or_family:AVERAGE MARINE TECHNOLOGY FEES $: 53 ⟵ “AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 159 | AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 159”
  - with_parents_or_family:TOTAL $: 8099 ⟵ “TOTAL $ | 8,099 | $ | 14,322 | $ | 28,638 | $ | 36,730 | TOTAL $ | 12,318 | $ | 20,653 | $ | 41,298 | $ | 53,613”
  - with_parents_or_family:AVERAGE NURSING FEES $: 895 ⟵ “AVERAGE NURSING FEES $ | 895 | $ | 895 | $ | 1,790 | $ | 2,685 | AVERAGE NURSING FEES $ | 895 | $ | 895 | $ | 1,790 | $ | 2,685”
  - with_parents_or_family:AVERAGE RN MOBILITY FEES $: 620 ⟵ “AVERAGE RN MOBILITY FEES $ | 620 | $ | 620 | $ | 1,240 | $ | 1,860 | AVERAGE RN MOBILITY FEES $ | 620 | $ | 620 | $ | 1,240 | $ | 1,860”
  - with_parents_or_family:AVERAGE PRACTICAL NURSING CERTIFICATE FEES $: 718 ⟵ “AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 718 | $ | 718 | $ | 1,436 | $ | 2,154 | AVERAGE PRACTICAL NURSING CERTIFICATE FEES $ | 718 | $ | 718 | $ | 1,436 | $ | 2,154”
  - with_parents_or_family:AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $: 61 ⟵ “AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183 | AVERAGE MEDICAL ASSISTING TECHNOLGY FEES $ | 61 | $ | 61 | $ | 122 | $ | 183”
  - with_parents_or_family:AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $: 60 ⟵ “AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE AUTOMOTIVE MANUFACTURING TECH FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE COSMETOLOGY FEES $: 46 ⟵ “AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138 | AVERAGE COSMETOLOGY FEES $ | 46 | $ | 46 | $ | 92 | $ | 138”
  - with_parents_or_family:AVERAGE INDUSTRIAL ELECTRONICS FEES $: 60 ⟵ “AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180 | AVERAGE INDUSTRIAL ELECTRONICS FEES $ | 60 | $ | 60 | $ | 120 | $ | 180”
  - with_parents_or_family:AVERAGE MACHINE SHOP FEES $: 16 ⟵ “AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48 | AVERAGE MACHINE SHOP FEES $ | 16 | $ | 16 | $ | 32 | $ | 48”
  - with_parents_or_family:AVERAGE WELDING ‐ DRAFTING FEES $: 7 ⟵ “AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 14 | $ | 21 | AVERAGE WELDING ‐ DRAFTING FEES $ | 7 | $ | 7 | $ | 14 | $ | 21”
  - with_parents_or_family:AVERAGE WELDING ‐ MACHINING FEES $: 11 ⟵ “AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33 | AVERAGE WELDING ‐ MACHINING FEES $ | 11 | $ | 11 | $ | 22 | $ | 33”
  - with_parents_or_family:AVERAGE MARINE TECHNOLOGY FEES $: 53 ⟵ “AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 159 | AVERAGE MARINE TECHNOLOGY FEES $ | 53 | $ | 53 | $ | 106 | $ | 159”
  - column:TUITION & FEES: 1109 ⟵ “TUITION & FEES | $ | 1,109 | $ | 2,765 | $ | 5,525 | $ | 6,629 | TUITION & FEES | $ | 1,109 | $ | 2,765 | $ | 5,525 | $ | 6,629”
  - … 263 more rows
### `232a42f63f888608` Chattahoochee Valley Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.cv.edu/financial-aid (sha256 47d2c58a06d2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Appeal Financial Aid Appeal Forms are located at www.cv.edu/student-forms/ under Student Resources Student Forms.”
### `779371ec2441261f` Chattahoochee Valley Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.cv.edu/financial-aid (sha256 47d2c58a06d2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A mitigating circumstance is defined as a situation beyond the student’s control, an undue hardship due to special circumstances, or other circumstances.”
### `0d9f1b0a179c749e` Chattahoochee Valley Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://catalog.cv.edu/cost-of-attendance (sha256 9afd0975cea5)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://catalog.cv.edu/cvcc-2026-2027-tuition-schedule,https://www.cv.edu/tuition/
- checks: {"columns": 2, "components_reconcile": false, "rows": 11}
  - with_parents_or_family:Tuition and Fees: 5880.0 ⟵ “Tuition and Fees | $5,880.00 | $5,880.00 | $9,870.00”
  - with_parents_or_family:Books and Supplies: 1008.0 ⟵ “Books and Supplies | $1,008.00 | $1,008.00 | $1,008.00”
  - with_parents_or_family:Food and Housing: 11200.0 ⟵ “Food and Housing | $11,200.00 | $15,300.00 | $15,300.00”
  - with_parents_or_family:Transportation: 2052.0 ⟵ “Transportation | $2,052.00 | $2,550.00 | $2,550.00”
  - with_parents_or_family:Miscellaneous: 4000.0 ⟵ “Miscellaneous | $4,000.00 | $4,000.00 | $4,000.00”
  - with_parents_or_family:Total: 24140.0 ⟵ “Total | $24,140.00 | $28,738.00 | $32,728.00”
  - with_parents_or_family:ADN Licensure, Certificate, and Credentials: 879.0 ⟵ “ADN Licensure, Certificate, and Credentials | $879.00 | $879.00 | $879.00”
  - with_parents_or_family:DRN Licensure, Certificate, and Credentials: 440.0 ⟵ “DRN Licensure, Certificate, and Credentials | $440.00 | $440.00 | $440.00”
  - with_parents_or_family:LPN Licensure, Certificate, and Credentials: 879.0 ⟵ “LPN Licensure, Certificate, and Credentials | $879.00 | $879.00 | $879.00”
  - with_parents_or_family:MAT Licensure, Certificate, and Credentials: 80.0 ⟵ “MAT Licensure, Certificate, and Credentials | $80.00 | $80.00 | $80.00”
  - with_parents_or_family:EMT Licensure, Certificate, and Credentials: 64.0 ⟵ “EMT Licensure, Certificate, and Credentials | $64.00 | $64.00 | $64.00”
  - column:Tuition and Fees: 5880.0 ⟵ “Tuition and Fees | $5,880.00 | $5,880.00 | $9,870.00”
  - column:Books and Supplies: 1008.0 ⟵ “Books and Supplies | $1,008.00 | $1,008.00 | $1,008.00”
  - column:Food and Housing: 15300.0 ⟵ “Food and Housing | $11,200.00 | $15,300.00 | $15,300.00”
  - column:Transportation: 2550.0 ⟵ “Transportation | $2,052.00 | $2,550.00 | $2,550.00”
  - column:Miscellaneous: 4000.0 ⟵ “Miscellaneous | $4,000.00 | $4,000.00 | $4,000.00”
  - column:Total: 28738.0 ⟵ “Total | $24,140.00 | $28,738.00 | $32,728.00”
  - column:ADN Licensure, Certificate, and Credentials: 879.0 ⟵ “ADN Licensure, Certificate, and Credentials | $879.00 | $879.00 | $879.00”
  - column:DRN Licensure, Certificate, and Credentials: 440.0 ⟵ “DRN Licensure, Certificate, and Credentials | $440.00 | $440.00 | $440.00”
  - column:LPN Licensure, Certificate, and Credentials: 879.0 ⟵ “LPN Licensure, Certificate, and Credentials | $879.00 | $879.00 | $879.00”
  - column:MAT Licensure, Certificate, and Credentials: 80.0 ⟵ “MAT Licensure, Certificate, and Credentials | $80.00 | $80.00 | $80.00”
  - column:EMT Licensure, Certificate, and Credentials: 64.0 ⟵ “EMT Licensure, Certificate, and Credentials | $64.00 | $64.00 | $64.00”
### `33d3df3b6e96ffe0` Chattahoochee Valley Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.cv.edu/tuition/ (sha256 1beb972d6d7f)
- issues: arrangement_unlabeled, conflicting_sources:https://catalog.cv.edu/cost-of-attendance,https://catalog.cv.edu/cvcc-2026-2027-tuition-schedule
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition & Fees*: 5880.0 ⟵ “Tuition & Fees* | $5,880.00 | $5,880.00 | $9,870.00”
  - with_parents_or_family:Books & Supplies: 1008.0 ⟵ “Books & Supplies | $1,008.00 | $1,008.00 | $1,008.00”
  - with_parents_or_family:Food & Housing: 11200.0 ⟵ “Food & Housing | $11,200.00 | $15,300.00 | $15,300.00”
  - with_parents_or_family:Transportation: 2052.0 ⟵ “Transportation | $2,052.00 | $2,052.00 | $2,550.00”
  - with_parents_or_family:Miscellaneous: 4000.0 ⟵ “Miscellaneous | $4,000.00 | $4,000.00 | $4,000.00”
  - with_parents_or_family:TOTAL: 24140.0 ⟵ “TOTAL | $24,140.00 | $28,240.00 | $32,728.00”
  - column:Tuition & Fees*: 5880.0 ⟵ “Tuition & Fees* | $5,880.00 | $5,880.00 | $9,870.00”
  - column:Books & Supplies: 1008.0 ⟵ “Books & Supplies | $1,008.00 | $1,008.00 | $1,008.00”
  - column:Food & Housing: 15300.0 ⟵ “Food & Housing | $11,200.00 | $15,300.00 | $15,300.00”
  - column:Transportation: 2052.0 ⟵ “Transportation | $2,052.00 | $2,052.00 | $2,550.00”
  - column:Miscellaneous: 4000.0 ⟵ “Miscellaneous | $4,000.00 | $4,000.00 | $4,000.00”
  - column:TOTAL: 28240.0 ⟵ “TOTAL | $24,140.00 | $28,240.00 | $32,728.00”
### `68fb0d7d493f2bb6` Chattahoochee Valley Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://catalog.cv.edu/cvcc-2026-2027-tuition-schedule (sha256 23485e90082b)
- issues: implausible_amount, conflicting_sources:https://catalog.cv.edu/cost-of-attendance,https://www.cv.edu/tuition/
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition: 133.0 ⟵ “Tuition | $133.00 | Tuition | $266.00”
  - column:ACCS Enhancement Fee: 20.0 ⟵ “ACCS Enhancement Fee | $20.00 | ACCS Enhancement Fee | $20.00”
  - column:Facility Renewal Fee: 15.0 ⟵ “Facility Renewal Fee | $15.00 | Facility Renewal Fee | $15.00”
  - column:Technology Fee: 15.0 ⟵ “Technology Fee | $15.00 | Technology Fee | $15.00”
  - column:Building Fee: 12.0 ⟵ “Building Fee | $12.00 | Building Fee | $12.00”
  - column:Bond Surety Fee: 1.0 ⟵ “Bond Surety Fee | $1.00 | Bond Surety Fee | $1.00”
  - column:Pirate Book Pack: 29.0 ⟵ “Pirate Book Pack | $29.00 | Pirate Book Pack | $29.00”
  - column:TOTAL: 225.0 ⟵ “TOTAL | $225.00 | TOTAL | $358.00”
### `775e3cc88c6e1763` Chattahoochee Valley Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.cv.edu/tuition/ (sha256 1beb972d6d7f)
- issues: conflicting_sources:https://catalog.cv.edu/cost-of-attendance,https://catalog.cv.edu/cvcc-2026-2027-tuition-schedule
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees*: 9870.0 ⟵ “Tuition & Fees* | $5,880.00 | $5,880.00 | $9,870.00”
  - on_campus:Books & Supplies: 1008.0 ⟵ “Books & Supplies | $1,008.00 | $1,008.00 | $1,008.00”
  - on_campus:Food & Housing: 15300.0 ⟵ “Food & Housing | $11,200.00 | $15,300.00 | $15,300.00”
  - on_campus:Transportation: 2550.0 ⟵ “Transportation | $2,052.00 | $2,052.00 | $2,550.00”
  - on_campus:Miscellaneous: 4000.0 ⟵ “Miscellaneous | $4,000.00 | $4,000.00 | $4,000.00”
  - on_campus:TOTAL: 32728.0 ⟵ “TOTAL | $24,140.00 | $28,240.00 | $32,728.00”
### `ad41d1730e780027` Chattahoochee Valley Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://catalog.cv.edu/cost-of-attendance (sha256 9afd0975cea5)
- issues: components_do_not_reconcile, conflicting_sources:https://catalog.cv.edu/cvcc-2026-2027-tuition-schedule,https://www.cv.edu/tuition/
- checks: {"columns": 1, "components_reconcile": false, "rows": 11}
  - on_campus:Tuition and Fees: 9870.0 ⟵ “Tuition and Fees | $5,880.00 | $5,880.00 | $9,870.00”
  - on_campus:Books and Supplies: 1008.0 ⟵ “Books and Supplies | $1,008.00 | $1,008.00 | $1,008.00”
  - on_campus:Food and Housing: 15300.0 ⟵ “Food and Housing | $11,200.00 | $15,300.00 | $15,300.00”
  - on_campus:Transportation: 2550.0 ⟵ “Transportation | $2,052.00 | $2,550.00 | $2,550.00”
  - on_campus:Miscellaneous: 4000.0 ⟵ “Miscellaneous | $4,000.00 | $4,000.00 | $4,000.00”
  - on_campus:Total: 32728.0 ⟵ “Total | $24,140.00 | $28,738.00 | $32,728.00”
  - on_campus:ADN Licensure, Certificate, and Credentials: 879.0 ⟵ “ADN Licensure, Certificate, and Credentials | $879.00 | $879.00 | $879.00”
  - on_campus:DRN Licensure, Certificate, and Credentials: 440.0 ⟵ “DRN Licensure, Certificate, and Credentials | $440.00 | $440.00 | $440.00”
  - on_campus:LPN Licensure, Certificate, and Credentials: 879.0 ⟵ “LPN Licensure, Certificate, and Credentials | $879.00 | $879.00 | $879.00”
  - on_campus:MAT Licensure, Certificate, and Credentials: 80.0 ⟵ “MAT Licensure, Certificate, and Credentials | $80.00 | $80.00 | $80.00”
  - on_campus:EMT Licensure, Certificate, and Credentials: 64.0 ⟵ “EMT Licensure, Certificate, and Credentials | $64.00 | $64.00 | $64.00”
### `bd7336005c03e540` Chattahoochee Valley Community College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://catalog.cv.edu/cvcc-2026-2027-tuition-schedule (sha256 23485e90082b)
- issues: implausible_amount, conflicting_sources:https://catalog.cv.edu/cost-of-attendance,https://www.cv.edu/tuition/
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition: 266.0 ⟵ “Tuition | $133.00 | Tuition | $266.00”
  - column:ACCS Enhancement Fee: 20.0 ⟵ “ACCS Enhancement Fee | $20.00 | ACCS Enhancement Fee | $20.00”
  - column:Facility Renewal Fee: 15.0 ⟵ “Facility Renewal Fee | $15.00 | Facility Renewal Fee | $15.00”
  - column:Technology Fee: 15.0 ⟵ “Technology Fee | $15.00 | Technology Fee | $15.00”
  - column:Building Fee: 12.0 ⟵ “Building Fee | $12.00 | Building Fee | $12.00”
  - column:Bond Surety Fee: 1.0 ⟵ “Bond Surety Fee | $1.00 | Bond Surety Fee | $1.00”
  - column:Pirate Book Pack: 29.0 ⟵ “Pirate Book Pack | $29.00 | Pirate Book Pack | $29.00”
  - column:TOTAL: 358.0 ⟵ “TOTAL | $225.00 | TOTAL | $358.00”
### `f9585de698451d1f` Chattahoochee Valley Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cv.edu/tuition/ (sha256 1beb972d6d7f)
- issues: implausible_amount, residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition: 266.0 ⟵ “Tuition | $133.00 | Tuition | $266.00”
  - column:Facility Renewal Fee: 15.0 ⟵ “Facility Renewal Fee | $15.00 | Facility Renewal Fee | $15.00”
  - column:Technology Fee: 15.0 ⟵ “Technology Fee | $15.00 | Technology Fee | $15.00”
  - column:Building Fee: 12.0 ⟵ “Building Fee | $12.00 | Building Fee | $12.00”
  - column:Bond Surety Fee: 1.0 ⟵ “Bond Surety Fee | $1.00 | Bond Surety Fee | $1.00”
  - column:Pirates Book Pack Fee: 29.0 ⟵ “Pirates Book Pack Fee | $29.00 | Pirates Book Pack Fee | $29.00”
  - column:ACCS Enhancement Fee: 20.0 ⟵ “ACCS Enhancement Fee | $20.00 | ACCS Enhancement Fee | $20.00”
  - column:TOTAL: 358.0 ⟵ “TOTAL | $225.00 | TOTAL | $358.00”
### `2055e54b9239b663` Coastal Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/financial-aid/appeals-and-special-unusual-circumstances/ (sha256 b0d09e1b44aa)
- issues: semantic_review_required, conflicting_sources:https://www.coastalalabama.edu/admissions-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance Status Review is an appeal to have a student’s status as a dependent student reviewed.”
  - sentence: need_based_special_circumstances ⟵ “To request an Unusual Circumstance Status Review, please complete the Dependeny Status Review Form and submit any required documentation.”
  - sentence: need_based_special_circumstances ⟵ “Students who are unable to provide a parent signature on the FAFSA will automatically be requested to complete an Unusual Circumstance Status Review.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance/Loss of Income/Unemployment Appeal/Review Since the FAFSA uses income from a prior/prior year, current household income may have significantly changed and no longer reflect a family’s ability to contribute to college costs.”
  - sentence: need_based_special_circumstances ⟵ “Students who are faced with this situation are encouraged to complete a Special Circumstance Review.”
  - sentence: need_based_special_circumstances ⟵ “Students who wish to have a Special Circumstance Review, need to complete the Special Circumstance Review form, and submit any required information.”
### `490e932ad8a4881b` Coastal Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/financial-aid/appeals-and-special-unusual-circumstances/ (sha256 b0d09e1b44aa)
- issues: semantic_review_required, conflicting_sources:https://www.coastalalabama.edu/admissions-aid/financial-aid/financial-aid-faqs/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Professional Judgements When there are unusual situations or circumstances that impact your federal student aid eligibility, a financial aid administrator may perform a professional judgement.”
  - sentence: professional_judgment ⟵ “The Department of Education will not override a school’s professional judgement decisions.”
  - sentence: professional_judgment ⟵ “Professional Judgements typically fall into the categories below.”
  - sentence: professional_judgment ⟵ “Students must request the professional judgement and submit the initial request along with documentation.”
### `4a7c7f0df9b93181` Coastal Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/financial-aid (sha256 3d557834adbe)
- issues: semantic_review_required, conflicting_sources:https://www.coastalalabama.edu/admissions-aid/financial-aid/appeals-and-special-unusual-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “How to Apply CALENDAR AT A GLANCE GRANTS LOANS SCHOLARSHIPS COLLEGE COSTS AND FEES Tuition MAINTAINING ELIGIBILITY POLICIES FINANCIAL AID FORMS STUDENT EMPLOYMENT Appeals and Special/Unusual Circumstances Refund Policy & Dates INCEPTIA FREQUENTLY ASKED QUESTIONS Hours of Operation Monday – Thursday : 7:30 AM - 5:00 PM Friday : 8:00 AM - 12:00 PM Contact Information Financial_Aid@CoastalAlabama.edu”
### `8d5ad5ecb06f258d` Coastal Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/financial-aid/appeals-and-special-unusual-circumstances/ (sha256 b0d09e1b44aa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP appeal decisions are final and may not be appealed beyond the Financial Aid Office.”
### `a363fff85037bb70` Coastal Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/financial-aid/financial-aid-faqs/ (sha256 c1a934571384)
- issues: semantic_review_required, conflicting_sources:https://www.coastalalabama.edu/admissions-aid/financial-aid/appeals-and-special-unusual-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Please visit the Professional Judgement information on the website for detailed information or contact the Financial Aid Office at 251-580-2151.”
### `dafe9b379c2bebe5` Coastal Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/financial-aid/appeals-and-special-unusual-circumstances/ (sha256 b0d09e1b44aa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency overrides cannot be considered solely because a parent does not want to provide information for the FAFSA or because a student is self-sufficient and under the age of 24.”
### `fee771199587a6c5` Coastal Alabama Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.coastalalabama.edu/admissions-aid/admissions-faqs (sha256 4eba6ff8c80b)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Please visit the Professional Judgement information on the website for detailed information or contact the Financial Aid Office at 251-580-2151.”
### `368e77ef7c52d5bf` Coastal Alabama Community College — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/financial-aid/tuition/ (sha256 cfcb962bd694)
- issues: components_do_not_reconcile, conflicting_sources:https://catalog.coastalalabama.edu/catalog/tuition-and-fees
- checks: {"columns": 3, "components_reconcile": false, "rows": 6}
  - with_parents_or_family:Tuition and Fees: 11310 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120 | $11,310 | $11,310 | $11,310”
  - with_parents_or_family:Food and Housing/ Living Expenses: 11310 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850 | $11,310 | $11,310 | $10,850”
  - with_parents_or_family:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510 | $3,510 | $3,510 | $3,510”
  - with_parents_or_family:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250 | $5,250 | $5,250 | $5,250”
  - with_parents_or_family:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200 | $4,200 | $4,200 | $4,200”
  - with_parents_or_family:Total: 30785 ⟵ “Total |  | $30,390 | $30,390 | $29,930 | $30,785 | $30,785 | $33,610”
  - off_campus_not_with_family:Tuition and Fees: 11310 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120 | $11,310 | $11,310 | $11,310”
  - off_campus_not_with_family:Food and Housing/ Living Expenses: 11310 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850 | $11,310 | $11,310 | $10,850”
  - off_campus_not_with_family:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510 | $3,510 | $3,510 | $3,510”
  - off_campus_not_with_family:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250 | $5,250 | $5,250 | $5,250”
  - off_campus_not_with_family:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200 | $4,200 | $4,200 | $4,200”
  - off_campus_not_with_family:Total: 30785 ⟵ “Total |  | $30,390 | $30,390 | $29,930 | $30,785 | $30,785 | $33,610”
  - on_campus:Tuition and Fees: 11310 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120 | $11,310 | $11,310 | $11,310”
  - on_campus:Food and Housing/ Living Expenses: 10850 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850 | $11,310 | $11,310 | $10,850”
  - on_campus:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510 | $3,510 | $3,510 | $3,510”
  - on_campus:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250 | $5,250 | $5,250 | $5,250”
  - on_campus:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200 | $4,200 | $4,200 | $4,200”
  - on_campus:Total: 33610 ⟵ “Total |  | $30,390 | $30,390 | $29,930 | $30,785 | $30,785 | $33,610”
### `7028008a927f99c1` Coastal Alabama Community College — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.coastalalabama.edu/admissions-aid/financial-aid/tuition/ (sha256 cfcb962bd694)
- issues: conflicting_sources:https://catalog.coastalalabama.edu/catalog/tuition-and-fees
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees: 6120 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120 | $11,310 | $11,310 | $11,310”
  - with_parents_or_family:Food and Housing/ Living Expenses: 11310 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850 | $11,310 | $11,310 | $10,850”
  - with_parents_or_family:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510 | $3,510 | $3,510 | $3,510”
  - with_parents_or_family:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250 | $5,250 | $5,250 | $5,250”
  - with_parents_or_family:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200 | $4,200 | $4,200 | $4,200”
  - with_parents_or_family:Total: 30390 ⟵ “Total |  | $30,390 | $30,390 | $29,930 | $30,785 | $30,785 | $33,610”
  - off_campus_not_with_family:Tuition and Fees: 6120 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120 | $11,310 | $11,310 | $11,310”
  - off_campus_not_with_family:Food and Housing/ Living Expenses: 11310 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850 | $11,310 | $11,310 | $10,850”
  - off_campus_not_with_family:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510 | $3,510 | $3,510 | $3,510”
  - off_campus_not_with_family:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250 | $5,250 | $5,250 | $5,250”
  - off_campus_not_with_family:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200 | $4,200 | $4,200 | $4,200”
  - off_campus_not_with_family:Total: 30390 ⟵ “Total |  | $30,390 | $30,390 | $29,930 | $30,785 | $30,785 | $33,610”
  - on_campus:Tuition and Fees: 6120 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120 | $11,310 | $11,310 | $11,310”
  - on_campus:Food and Housing/ Living Expenses: 10850 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850 | $11,310 | $11,310 | $10,850”
  - on_campus:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510 | $3,510 | $3,510 | $3,510”
  - on_campus:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250 | $5,250 | $5,250 | $5,250”
  - on_campus:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200 | $4,200 | $4,200 | $4,200”
  - on_campus:Total: 29930 ⟵ “Total |  | $30,390 | $30,390 | $29,930 | $30,785 | $30,785 | $33,610”
### `7ceb197454df083e` Coastal Alabama Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://catalog.coastalalabama.edu/catalog/tuition-and-fees (sha256 2dfb59f9f899)
- issues: conflicting_sources:https://www.coastalalabama.edu/admissions-aid/financial-aid/tuition/
- checks: {"columns": 3, "rows": 5}
  - with_parents_or_family:Tuition and Fees: 6120 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120”
  - with_parents_or_family:Food and Housing/ Living Expenses: 11310 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850”
  - with_parents_or_family:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510”
  - with_parents_or_family:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250”
  - with_parents_or_family:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200”
  - off_campus_not_with_family:Tuition and Fees: 6120 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120”
  - off_campus_not_with_family:Food and Housing/ Living Expenses: 11310 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850”
  - off_campus_not_with_family:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510”
  - off_campus_not_with_family:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250”
  - off_campus_not_with_family:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200”
  - on_campus:Tuition and Fees: 6120 ⟵ “Tuition and Fees | 204/337 | $6,120 | $6,120 | $6,120”
  - on_campus:Food and Housing/ Living Expenses: 10850 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850”
  - on_campus:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510”
  - on_campus:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250”
  - on_campus:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200”
### `9ff7246e654340e9` Coastal Alabama Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://catalog.coastalalabama.edu/catalog/tuition-and-fees (sha256 2dfb59f9f899)
- issues: conflicting_sources:https://www.coastalalabama.edu/admissions-aid/financial-aid/tuition/
- checks: {"columns": 3, "rows": 5}
  - with_parents_or_family:Tuition and Fees: 11310 ⟵ “Tuition and Fees | 204/337 | $11,310 | $11,310 | $11,310”
  - with_parents_or_family:Food and Housing/ Living Expenses: 11310 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850”
  - with_parents_or_family:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510”
  - with_parents_or_family:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250”
  - with_parents_or_family:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200”
  - off_campus_not_with_family:Tuition and Fees: 11310 ⟵ “Tuition and Fees | 204/337 | $11,310 | $11,310 | $11,310”
  - off_campus_not_with_family:Food and Housing/ Living Expenses: 11310 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850”
  - off_campus_not_with_family:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510”
  - off_campus_not_with_family:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250”
  - off_campus_not_with_family:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200”
  - on_campus:Tuition and Fees: 11310 ⟵ “Tuition and Fees | 204/337 | $11,310 | $11,310 | $11,310”
  - on_campus:Food and Housing/ Living Expenses: 10850 ⟵ “Food and Housing/ Living Expenses |  | $11,310 | $11,310 | $10,850”
  - on_campus:Books and Supplies: 3510 ⟵ “Books and Supplies | 27 per credit hour plus supplies and computer purchase | $3,510 | $3,510 | $3,510”
  - on_campus:Transportation: 5250 ⟵ “Transportation |  | $5,250 | $5,250 | $5,250”
  - on_campus:Personal/ Miscellaneous: 4200 ⟵ “Personal/ Miscellaneous |  | $4,200 | $4,200 | $4,200”
### `28f11fb15aaaba21` Enterprise State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://escc.edu/paying-for-college/financial-aid/academic-requirements/ (sha256 824d3e6f5d20)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Financial Aid Warning, SAP Appeals, and Academic Plans Students whose financial aid eligibility is suspended may file an appeal if they believe they have certain mitigating circumstances.”
  - sentence: sap_appeal ⟵ “Likewise, ESCC cannot approve SAP appeals for students who return to ESCC after an initial poor academic showing (even after an extended period) without a documentable reason.”
  - sentence: sap_appeal ⟵ “The Appeals Committee meets within 3 to 5 business days upon receipt of each SAP appeal received.”
  - sentence: sap_appeal ⟵ “Students initiate a SAP appeal by completing the Satisfactory Academic Progress (SAP) Appeal form.”
### `681de5768d5ff7c7` Enterprise State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://escc.edu/paying-for-college/financial-aid/special-circumstances/ (sha256 8fa0d9060314)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Circumstances – Professional Judgement If you or your family have experienced a change in income, life event, or other extenuating circumstances since filing the FAFSA and receiving your aid offer, please review and complete the Special Circumstances Form.”
### `7d786fa98d9a6a49` Enterprise State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://escc.edu/paying-for-college/financial-aid/special-circumstances/ (sha256 8fa0d9060314)
- issues: semantic_review_required, conflicting_sources:https://escc.edu/paying-for-college/financial-aid/,https://escc.edu/paying-for-college/financial-aid/academic-requirements/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow us to review special circumstances that may affect your need for financial aid, and determine if changes can be made to the information originally reported on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances – Dependency Override The financial aid office has the authority, through Section 480(d)(7) of the Higher Education Act, to change a student’s status from dependent to independent in cases involving unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Be sure to carefully review the form to determine the acceptable supporting documentation that our office will need in addition to the Unusual Circumstances Form and your personal letter explaining the extenuating circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Financial Aid Resources Withdrawals Financial Aid Forms Types of Aid Academic Requirements Special Circumstances Main Campus Opens Google Map in a new tab 600 Plaza Drive Enterprise, AL 36330 All Campuses Schedule A Tour Get In Touch Phone (334) 347-2623 Email admissions@escc.edu Contact A Recruiter Connect Follow us on facebook Follow us on youtube Follow us on instagram Follow us o”
### `e8092b57d73d7c25` Enterprise State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://escc.edu/paying-for-college/financial-aid/ (sha256 dd8b5f3e64ee)
- issues: semantic_review_required, conflicting_sources:https://escc.edu/paying-for-college/financial-aid/academic-requirements/,https://escc.edu/paying-for-college/financial-aid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Resources Financial Aid Forms Types of Aid Satisfactory Academic Progress (SAP) Requirements Special Circumstances Veterans Benefits Rights and Responsibilities of Aid Recipients Withdrawals Main Campus Opens Google Map in a new tab 600 Plaza Drive Enterprise, AL 36330 All Campuses Schedule A Tour Get In Touch Phone (334) 347-2623 Email admissions@escc.edu Contact A Recruiter Connect”
### `f381f257f4c704aa` Enterprise State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://escc.edu/paying-for-college/financial-aid/academic-requirements/ (sha256 824d3e6f5d20)
- issues: semantic_review_required, conflicting_sources:https://escc.edu/paying-for-college/financial-aid/,https://escc.edu/paying-for-college/financial-aid/special-circumstances/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Financial Aid Resources Withdrawals Financial Aid Forms Types of Aid Academic Requirements Special Circumstances Main Campus Opens Google Map in a new tab 600 Plaza Drive Enterprise, AL 36330 All Campuses Schedule A Tour Get In Touch Phone (334) 347-2623 Email admissions@escc.edu Contact A Recruiter Connect Follow us on facebook Follow us on youtube Follow us on instagram Follow us o”
### `832b8f3f44612967` Enterprise State Community College — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://escc.edu/paying-for-college/cost-of-attendance/ (sha256 0ce447d46c2f)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 9450.0 ⟵ “Tuition & Fees | $4725.00 | $9450.00 | $14175.00”
  - column:Housing & Food: 7173.0 ⟵ “Housing & Food | $3587.00 | $7173.00 | $9564.00”
  - column:Books, Supplies, & Equipment: 2034.0 ⟵ “Books, Supplies, & Equipment | $1017.00 | $2034.00 | $3051.00”
  - column:Transportation: 2140.0 ⟵ “Transportation | $1070.00 | $2140.00 | $2860.00”
  - column:Miscellaneous: 1284.0 ⟵ “Miscellaneous | $642.00 | $1284.00 | $1716.00”
  - column:Loan Fees: 100.0 ⟵ “Loan Fees | $50.00 | $100.00 | $130.00”
  - column:Total: 22181.0 ⟵ “Total | $11091.00 | $22181.00 | $31496.00”
### `ce67a17c40239cea` Enterprise State Community College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://escc.edu/paying-for-college/cost-of-attendance/ (sha256 0ce447d46c2f)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition & Fees: 5520.0 ⟵ “Tuition & Fees | $2760.00 | $5520.00 | $8280.00”
  - column:Housing & Food: 7173.0 ⟵ “Housing & Food | $3587.00 | $7173.00 | $9564.00”
  - column:Books, Supplies, & Equipment: 2034.0 ⟵ “Books, Supplies, & Equipment | $1017.00 | $2034.00 | $3051.00”
  - column:Transportation: 2140.0 ⟵ “Transportation | $1070.00 | $2140.00 | $2860.00”
  - column:Miscellaneous: 1284.0 ⟵ “Miscellaneous | $642.00 | $1284.00 | $1716.00”
  - column:Loan Fees: 100.0 ⟵ “Loan Fees | $50.00 | $100.00 | $130.00”
  - column:Total: 18251.0 ⟵ “Total | $9126.00 | $18251.00 | $25601.00”
### `5ca589655442eb33` Faulkner University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://chs.faulkner.edu/master-in-physician-assistant-studies/ (sha256 be7923263f6f)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://chs.faulkner.edu/doctor-of-occupational-therapy/
- checks: {"columns": 2, "components_reconcile": false, "rows": 1}
  - column:Total Program Cost: 121000 ⟵ “Total Program Cost | $121,000”
  - column:Tuition: 106720 ⟵ “Tuition | $920/credit hours x 116 | $106,720”
  - column:General Fee: 2450 ⟵ “General Fee | $350 x 7 semesters | $2,450”
  - column:Clinical Fee: 11830 ⟵ “Clinical Fee | $1,690 x 7 semesters | $11,830”
### `6d0feeb94829c08b` Faulkner University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://chs.faulkner.edu/doctor-of-occupational-therapy/ (sha256 9d95f43a0d17)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://chs.faulkner.edu/master-in-physician-assistant-studies/
- checks: {"columns": 3, "components_reconcile": false, "rows": 6}
  - column:Months Enrolled: 12 ⟵ “Months Enrolled | 12 | 12 | 9”
  - column:Estimate Cost of Books: 1000 ⟵ “Estimate Cost of Books | $1,000 | $800 | $400”
  - column:Tuition: 36000 ⟵ “Tuition | $36,000 | $27,000 | $19,500”
  - column:General Fees: 1050 ⟵ “General Fees | $1,050 | $1,050 | $700”
  - column:Clinical Fees: 1725 ⟵ “Clinical Fees | $1,725 | $1,725 | $1,150”
  - column:Total: 39775 ⟵ “Total | $39,775 | $30,575 | $21,750”
  - column:Months Enrolled: 12 ⟵ “Months Enrolled | 12 | 12 | 9”
  - column:Estimate Cost of Books: 800 ⟵ “Estimate Cost of Books | $1,000 | $800 | $400”
  - column:Tuition: 27000 ⟵ “Tuition | $36,000 | $27,000 | $19,500”
  - column:General Fees: 1050 ⟵ “General Fees | $1,050 | $1,050 | $700”
  - column:Clinical Fees: 1725 ⟵ “Clinical Fees | $1,725 | $1,725 | $1,150”
  - column:Total: 30575 ⟵ “Total | $39,775 | $30,575 | $21,750”
  - column:Months Enrolled: 9 ⟵ “Months Enrolled | 12 | 12 | 9”
  - column:Estimate Cost of Books: 400 ⟵ “Estimate Cost of Books | $1,000 | $800 | $400”
  - column:Tuition: 19500 ⟵ “Tuition | $36,000 | $27,000 | $19,500”
  - column:General Fees: 700 ⟵ “General Fees | $1,050 | $1,050 | $700”
  - column:Clinical Fees: 1150 ⟵ “Clinical Fees | $1,725 | $1,725 | $1,150”
  - column:Total: 21750 ⟵ “Total | $39,775 | $30,575 | $21,750”
### `8cb4d45f1d601137` Gadsden State Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.gadsdenstate.edu/admissions-aid/grant-programs (sha256 8f0605828f75)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Students who have unusual circumstances may email the Financial Aid Director at ifreyberg@gadsdenstate.edu for consideration.”
  - sentence: need_based_special_circumstances ⟵ “Students who have unusual circumstances may email the Financial Aid Director at ifreyberg@gadsdenstate.edu for consideration.”
### `c0b31be5cd1c6914` Gadsden State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.gadsdenstate.edu/admissions-aid/financial-aid-definitions (sha256 fae08a589aab)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal A formal request to have a committee review your special circumstances that resulted in your financial aid suspension.”
### `ce54ac8ae3e3ff83` George C Wallace Community College-Dothan — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.wallace.edu/sites/default/files/pdf/academic_page/financial-aid-satisfactory-academic-progress-policy.pdf?1777404645 (sha256 2484964f596f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid will be reinstated when the student attends college at his/her own expense and meets the minimum standards of satisfactory academic progress or if the Financial Aid Appeal Committee reinstates eligibility.”
### `c807c2f9d36d80f1` George C Wallace Community College-Dothan — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://wallace.edu/wp-content/uploads/2026/06/TIV-Cost-of-Attendance-26.27-PDF.pdf (sha256 b92a2cfce0e3)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 2, "rows": 6}
  - with_parents_or_family:Tuition/Fees: 6120 ⟵ “Tuition/Fees | 6120 | 6120”
  - with_parents_or_family:Books/Supplies: 1200 ⟵ “Books/Supplies | 1200 | 1200”
  - with_parents_or_family:Room/Board: 3825 ⟵ “Room/Board | 3825 | 9450”
  - with_parents_or_family:Transportation: 2340 ⟵ “Transportation | 2340 | 2340”
  - with_parents_or_family:Misc./Personal Expenses: 1000 ⟵ “Misc./Personal Expenses | 1000 | 1000”
  - with_parents_or_family:Total: 14485 ⟵ “Total | 14485 | 20110”
  - with_parents_or_family:Tuition/Fees: 3060 ⟵ “Tuition/Fees | 3060 | 3060”
  - with_parents_or_family:Books/Supplies: 600 ⟵ “Books/Supplies | 600 | 600”
  - with_parents_or_family:Room/Board: 1275 ⟵ “Room/Board | 1275 | 3150”
  - with_parents_or_family:Transportation: 750 ⟵ “Transportation | 750 | 750”
  - with_parents_or_family:Misc./Personal Expenses: 500 ⟵ “Misc./Personal Expenses | 500 | 500”
  - with_parents_or_family:Total: 6185 ⟵ “Total | 6185 | 8060”
  - with_parents_or_family:Tuition/Fees: 5055 ⟵ “Tuition/Fees | 5055 | 5055”
  - with_parents_or_family:Books/Supplies: 600 ⟵ “Books/Supplies | 600 | 600”
  - with_parents_or_family:Room/Board: 1275 ⟵ “Room/Board | 1275 | 3150”
  - with_parents_or_family:Transportation: 750 ⟵ “Transportation | 750 | 750”
  - with_parents_or_family:Misc./Personal Expenses: 500 ⟵ “Misc./Personal Expenses | 500 | 500”
  - with_parents_or_family:Total: 8180 ⟵ “Total | 8180 | 10055”
  - with_parents_or_family:Tuition/Fees: 10110 ⟵ “Tuition/Fees | 10110 | 10110”
  - with_parents_or_family:Books/Supplies: 1200 ⟵ “Books/Supplies | 1200 | 1200”
  - with_parents_or_family:Room/Board: 3825 ⟵ “Room/Board | 3825 | 9450”
  - with_parents_or_family:Transportation: 2340 ⟵ “Transportation | 2340 | 2340”
  - with_parents_or_family:Misc./Personal Expenses: 1000 ⟵ “Misc./Personal Expenses | 1000 | 1000”
  - with_parents_or_family:Total: 18475 ⟵ “Total | 18475 | 24100”
  - column:Tuition/Fees: 6120 ⟵ “Tuition/Fees | 6120 | 6120”
  - … 23 more rows
### `03fd457f9e7e9736` George C Wallace Community College-Dothan — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.wallace.edu/collegelevel-examination-program-clepr-policy (sha256 5bc72cc52ca9)
- issues: conflicting_sources:https://catalog.wallace.edu/sites/default/files/pdf/academic_page/collegelevel-examination-program-clepr-policy.pdf?1747931254
- checks: {"distinct_exams": 24, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 hours | BUS 263”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 hours | BUS 275”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 hours | ENG 251, 252”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 hours | ENG 102”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 6 hours | ENG 261, 262”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 hours | ENG 101”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 hours | HUM 101”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1 | 50 | 6 hours | SPA 101, 102”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 hours | POL 211”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1887 | 50 | 3 hours | HIS 201”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present | 50 | 3 hours | HIS 202”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 hours | PSY 210”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 hours | PSY 200”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 hours | SOC 200”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 hours | ECO 231”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 hours | ECO 232”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 | 3 hours | HIS 101”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present | 50 | 3 hours | HIS 102”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 8 hours | BIO 103, 104”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 4 hours | MTH 125”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 hours | MTH 100”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 hours | MTH 116”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences | 50 | 4 hours | BIO 101”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 3 hours | MTH 115”
### `048aeb3f45e12186` George C Wallace Community College-Dothan — credit_policies 2025-26 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.wallace.edu/sites/default/files/20252026-catalog-6-26-26.pdf (sha256 42e0bc955837)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 22, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law                                  50                    3 hours        BUS 263”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management                                   50                    3 hours        BUS 275”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                                        50                    6 hours        ENG 251, 252”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature                      50                    3 hours        ENG 102”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                                         50                    6 hours        ENG 261, 262”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                                        50                    3 hours        ENG 101”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                                                 50                    3 hours        HUM 101”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1                                  50                    6 hours        SPA 101, 102”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                                        50                    3 hours        POL 211”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present       50                    3 hours        HIS 202”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development                      50                    3 hours        PSY 210”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                           50                    3 hours        PSY 200”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                            50                    3 hours        SOC 200”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                      50                    3 hours        ECO 231”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                      50                    3 hours        ECO 232”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present      50                    3 hours        HIS 102”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                           50                    8 hours        BIO 103, 104”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                          50                    4 hours        MTH 125”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                                   50                    3 hours        MTH 100”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics                               50                    3 hours        MTH 116”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences                                  50                    4 hours        BIO 101”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                                       50                    3 hours        MTH 115”
### `74a138ebb0a06450` George C Wallace Community College-Dothan — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://catalog.wallace.edu/sites/default/files/pdf/academic_page/collegelevel-examination-program-clepr-policy.pdf?1747931254 (sha256 1287f50b4e88)
- issues: conflicting_sources:https://catalog.wallace.edu/collegelevel-examination-program-clepr-policy
- checks: {"distinct_exams": 22, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law                                  50                    3 hours        BUS 263”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management                                   50                    3 hours        BUS 275”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature                                        50                    6 hours        ENG 251, 252”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature                      50                    3 hours        ENG 102”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature                                         50                    6 hours        ENG 261, 262”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition                                        50                    3 hours        ENG 101”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities                                                 50                    3 hours        HUM 101”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language, Level 1                                  50                    6 hours        SPA 101, 102”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government                                        50                    3 hours        POL 211”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to the Present       50                    3 hours        HIS 202”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development                      50                    3 hours        PSY 210”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology                           50                    3 hours        PSY 200”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology                            50                    3 hours        SOC 200”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics                      50                    3 hours        ECO 231”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics                      50                    3 hours        ECO 232”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to the Present      50                    3 hours        HIS 102”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                                           50                    8 hours        BIO 103, 104”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus                                          50                    4 hours        MTH 125”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra                                   50                    3 hours        MTH 100”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics                               50                    3 hours        MTH 116”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences                                  50                    4 hours        BIO 101”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus                                       50                    3 hours        MTH 115”
### `96e9a74b73c18775` George C Wallace State Community College-Hanceville — appeals 2018-19 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/satisfactory-academic-progress.html (sha256 fb39bdfa2ea5)
- issues: stale_year_label:2018-19, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “We cannot approve a SAP appeal for MAX if the student has not graduated from a certificate or degree program.”
### `248a29cf7a08059a` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Pettable Mental Health Importance Scholarship | $1,000”
### `24a0c1b865ffbb3f` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $3,600 ⟵ “AAMA/ACCS "Dream it Do it Alabama" Auto Manufacturing | $3,600”
### `290740b19905338a` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: Various ⟵ “TechForce Foundation | Various”
### `4735a6b51395396c` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $1,000/Various ⟵ “NISOD Student Essay Contest | $1,000/Various”
### `8e65822006d8edbf` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $1,000/Various ⟵ “NISOD Student Graphic Design Contest | $1,000/Various”
### `968c0b0b5f53656f` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: up to $2,500 ⟵ “Sallie Mae® Completing the Dream Scholarship Program | up to $2,500”
### `ac0778597dbb560e` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $3,500 - $5,000 ⟵ “Regions Riding Forward Scholarship Contest | $3,500 - $5,000”
### `f2e87209aa1184b8` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Next Generation HVAC Scholarship | $2,500”
### `f43976a2cfca9187` George C Wallace State Community College-Hanceville — awards 2023-24 [new] (labeled_in_source)
- source: https://www.wallacestate.edu/financial-aid/other-scholarship-opportunities.html (sha256 c68868bcaf99)
- issues: stale_year_label:2023-24
- checks: {"thresholds": null}
  - award_amount_text: Various ⟵ “Career One Stop Scholarship Opportunities | Various”
### `7c6701903de3e555` George C Wallace State Community College-Hanceville — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://www.wallacestate.edu/financial-aid/ecoa.html (sha256 e2bd5e418478)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 3996.0 ⟵ “Tuition and Fees | 3996.00 | 7992.00 | 11988.00”
  - column:Books and Supplies: 1000.0 ⟵ “Books and Supplies | 1000.00 | 2000.00 | 3000.00”
  - column:Food: 2850.0 ⟵ “Food | 2850.00 | 5700.00 | 8550.00”
  - column:Transportation: 3500.0 ⟵ “Transportation | 3500.00 | 7000.00 | 10500.00”
  - column:Miscellaneous: 1200.0 ⟵ “Miscellaneous | 1200.00 | 2400.00 | 3600.00”
  - column:Housing: 2000.0 ⟵ “Housing | 2000.00 | 4000.00 | 6000.00”
  - column:TOTAL: 14546.0 ⟵ “TOTAL | 14546.00 | 29092.00 | 43638.00”
  - column:Tuition and Fees: 7992.0 ⟵ “Tuition and Fees | 3996.00 | 7992.00 | 11988.00”
  - column:Books and Supplies: 2000.0 ⟵ “Books and Supplies | 1000.00 | 2000.00 | 3000.00”
  - column:Food: 5700.0 ⟵ “Food | 2850.00 | 5700.00 | 8550.00”
  - column:Transportation: 7000.0 ⟵ “Transportation | 3500.00 | 7000.00 | 10500.00”
  - column:Miscellaneous: 2400.0 ⟵ “Miscellaneous | 1200.00 | 2400.00 | 3600.00”
  - column:Housing: 4000.0 ⟵ “Housing | 2000.00 | 4000.00 | 6000.00”
  - column:TOTAL: 29092.0 ⟵ “TOTAL | 14546.00 | 29092.00 | 43638.00”
  - column:Tuition and Fees: 11988.0 ⟵ “Tuition and Fees | 3996.00 | 7992.00 | 11988.00”
  - column:Books and Supplies: 3000.0 ⟵ “Books and Supplies | 1000.00 | 2000.00 | 3000.00”
  - column:Food: 8550.0 ⟵ “Food | 2850.00 | 5700.00 | 8550.00”
  - column:Transportation: 10500.0 ⟵ “Transportation | 3500.00 | 7000.00 | 10500.00”
  - column:Miscellaneous: 3600.0 ⟵ “Miscellaneous | 1200.00 | 2400.00 | 3600.00”
  - column:Housing: 6000.0 ⟵ “Housing | 2000.00 | 4000.00 | 6000.00”
  - column:TOTAL: 43638.0 ⟵ “TOTAL | 14546.00 | 29092.00 | 43638.00”
### `d5c54267fb6fc5d4` George C Wallace State Community College-Hanceville — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.wallacestate.edu/financial-aid/ecoa.html (sha256 e2bd5e418478)
- issues: arrangement_unlabeled
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees: 2400.0 ⟵ “Tuition and Fees | 2400.00 | 4800.00 | 7200.00”
  - column:Books and Supplies: 1000.0 ⟵ “Books and Supplies | 1000.00 | 2000.00 | 3000.00”
  - column:Housing: 4300.0 ⟵ “Housing | 4300.00 | 8600.00 | 12,900.00”
  - column:Food: 2850.0 ⟵ “Food | 2850.00 | 5700.00 | 8550.00”
  - column:Transportation: 3500.0 ⟵ “Transportation | 3500.00 | 7000.00 | 10500.00”
  - column:Miscellaneous: 1200.0 ⟵ “Miscellaneous | 1200.00 | 2400.00 | 3600.00”
  - column:TOTAL: 15250.0 ⟵ “TOTAL | 15250.00 | 30500.00 | 45750.00”
  - column:Tuition and Fees: 4800.0 ⟵ “Tuition and Fees | 2400.00 | 4800.00 | 7200.00”
  - column:Books and Supplies: 2000.0 ⟵ “Books and Supplies | 1000.00 | 2000.00 | 3000.00”
  - column:Housing: 8600.0 ⟵ “Housing | 4300.00 | 8600.00 | 12,900.00”
  - column:Food: 5700.0 ⟵ “Food | 2850.00 | 5700.00 | 8550.00”
  - column:Transportation: 7000.0 ⟵ “Transportation | 3500.00 | 7000.00 | 10500.00”
  - column:Miscellaneous: 2400.0 ⟵ “Miscellaneous | 1200.00 | 2400.00 | 3600.00”
  - column:TOTAL: 30500.0 ⟵ “TOTAL | 15250.00 | 30500.00 | 45750.00”
  - column:Tuition and Fees: 7200.0 ⟵ “Tuition and Fees | 2400.00 | 4800.00 | 7200.00”
  - column:Books and Supplies: 3000.0 ⟵ “Books and Supplies | 1000.00 | 2000.00 | 3000.00”
  - column:Housing: 12900.0 ⟵ “Housing | 4300.00 | 8600.00 | 12,900.00”
  - column:Food: 8550.0 ⟵ “Food | 2850.00 | 5700.00 | 8550.00”
  - column:Transportation: 10500.0 ⟵ “Transportation | 3500.00 | 7000.00 | 10500.00”
  - column:Miscellaneous: 3600.0 ⟵ “Miscellaneous | 1200.00 | 2400.00 | 3600.00”
  - column:TOTAL: 45750.0 ⟵ “TOTAL | 15250.00 | 30500.00 | 45750.00”
### `d95eecd9eb81e4d3` George C Wallace State Community College-Hanceville — credit_policies 2025-26 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://www.wallacestate.edu/deoptions/forms/Dual_Enrollment_Student_Handbook_r1.pdf (sha256 6570b3f41e85)
- issues: stale_year_label:2025-26
- checks: {"fields": ["max_credit_hours_per_term"], "tiers": 2}
  - eligibility_tier: 2.5 ⟵ “unweighted high school grade point average (GPA) of 2.5 on a 4.0 scale.”
  - eligibility_tier: 2.5 ⟵ “unweighted high school grade point average (GPA) of 2.5 on a 4.0 scale.”
  - eligibility_tier: 3.0 ⟵ “unweighted high school grade point average (GPA) of 3.0 on a 4.0 scale.”
  - max_credit_hours_per_term: 12 ⟵ “up to 12 hours in Fall 2025 and Spring 2026. In the spring of 2026, students must meet”
### `4ad6281d2b2ea887` George C Wallace State Community College-Selma — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.wccs.edu/appeal-process-for-mitigating-circumstances (sha256 2e7f4607c48f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Process for Mitigating Circumstances | Wallace Community College Selma Catalog Skip to main content College Catalog Catalog Home Main navigation Degrees Course Descriptions wccs.edu Fulltext search Breadcrumb Home Appeal Process for Mitigating Circumstances Appeal Process for Mitigating Circumstances Download as PDF A student who fails to meet one or more of the satisfactory academic progre”
### `9d22464c3c2178fb` George C Wallace State Community College-Selma — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.wccs.edu/appeal-process-for-mitigating-circumstances (sha256 2e7f4607c48f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The student may appeal that result on the basis of his injury or illness, the death of a relative, or other special circumstances.”
### `20f383cdf1bfbab5` H Councill Trenholm State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.trenholmstate.edu/satisfactory-progress-sap-policy (sha256 db0ea61a277f)
- issues: semantic_review_required, conflicting_sources:https://www.trenholmstate.edu/financial-aid-satisfactory-academic-progress-sap-policy/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Students may regain ﬁnancial aid eligibility based on one of the following criteria: The student may enroll in and pass classes while paying tuition and fees out of pocket in order to meet the Financial Aid SAP requirements or The student submits a Satisfactory Academic Progress (SAP) Appeal stating the extenuating circumstances to justify an exception to the SAP Policy for review by the Director ”
  - sentence: sap_appeal ⟵ “Notification of the SAP appeal decision will be sent via email to the student's email address.”
  - sentence: sap_appeal ⟵ “Students are limited to two SAP appeals during their academic career at Trenholm State Community College, and only one appeal may be submitted per academic year.”
  - sentence: sap_appeal ⟵ “SAP appeals decisions are final and cannot be appealed further.”
### `4328f6bb85ab5cf0` H Councill Trenholm State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.trenholmstate.edu/financial-aid-satisfactory-academic-progress-sap-policy/ (sha256 0557d8fa25f3)
- issues: semantic_review_required, conflicting_sources:https://catalog.trenholmstate.edu/satisfactory-progress-sap-policy
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: sap_appeal ⟵ “Air Force GEM Program Net Price Calculator Types of Aid Cashier Payment Options Financial Aid Satisfactory Academic Progress (SAP) Policy Satisfactory Academic Progress Financial Aid Appeal Form Satisfactory Academic Progress (SAP) Policy Federal regulations require all colleges participating in the Title IV Federal Student Aid programs to establish and monitor Satisfactory Academic Progress (SAP)”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Students whose SAP appeal is approved will be placed on Financial Aid Probation and must follow an academic plan until they meet all SAP standards again.”
  - sentence: sap_appeal ⟵ “SAP Appeal Information Students who experience documented extenuating circumstances beyond their control may request reconsideration of their financial aid eligibility by submitting a SAP Appeal.”
  - sentence: sap_appeal ⟵ “SAP Appeals must be submitted no later than two weeks prior to the first day of classes for the semester in which financial aid reinstatement is requested.”
  - sentence: sap_appeal ⟵ “Prior to submitting a SAP Appeal, students must: Review their unofficial academic transcript available through the MyTrenholm Portal.”
  - sentence: sap_appeal ⟵ “Understand that students are limited to one SAP Appeal per academic year and a maximum of two SAP Appeals during their academic career at the College, unless otherwise permitted by College policy.”
### `c28920e6be18502e` H Councill Trenholm State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.trenholmstate.edu/financial-aid-satisfactory-academic-progress-sap-policy/ (sha256 0557d8fa25f3)
- issues: semantic_review_required, conflicting_sources:https://catalog.trenholmstate.edu/satisfactory-progress-sap-policy
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal Process & Extenuatiing Circumstances Any student placed on Financial Aid Suspension may appeal his/her status by submitting a letter to the Financial Aid Appeals Committee stating in writing any unusual circumstances that had a bearing on his/her academic performance along with providing supporting documentation.”
### `f351e9afec287d01` H Councill Trenholm State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.trenholmstate.edu/satisfactory-progress-sap-policy (sha256 db0ea61a277f)
- issues: semantic_review_required, conflicting_sources:https://www.trenholmstate.edu/financial-aid-satisfactory-academic-progress-sap-policy/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal Process and Extenuating Circumstances Students placed on Financial Aid Suspension who wish to request reinstatement of federal financial aid due to mitigating circumstances must submit the Financial Aid Appeal Form along with a letter explaining any unusual circumstances that affected academic performance.”
### `fcded4943d8075c3` H Councill Trenholm State Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://catalog.trenholmstate.edu/financial-aid-programs (sha256 f9a5d4f4500d)
- issues: residency_unknown
- checks: {"columns": 1, "rows": 3}
  - column:Tuition/fees paid:: 648.0 ⟵ “Tuition/fees paid: | $648.00”
  - column:Round to nearest dollar: 453.6 ⟵ “Round to nearest dollar | $453.60”
  - column:Refund amount: 454.0 ⟵ “Refund amount | $454.00”
### `c3a585a3e6242515` Huntingdon College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/applying-for-financial-aid/ (sha256 6cddad6104d7)
- issues: semantic_review_required, conflicting_sources:https://www.huntingdon.edu/admission-aid/student-financial-services/student-financial-services-forms/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you need additional assistance with financing your education, have questions about the aid process, or have special circumstances to be considered in the application process, be sure to consult the Office of Student Financial Services.”
### `cef9212563178ff1` Huntingdon College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/student-financial-services-forms/ (sha256 91fc5568d521)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.huntingdon.edu/admission-aid/student-financial-services/applying-for-financial-aid/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Forms Special Circumstance Form: Consult the Office of Student Financial Services regarding special circumstances or changes in your family’s and/or your financial situation which may impact your ability to pay for your education.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance Form: The Office of Student Financial Services has the authority, through Section 480(d)(7) of the Higher Education Act, to change a student’s dependency status from dependent to independent in cases involving documented extenuating circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Please reach out to the Office of Student Financial Services regarding an unusual circumstances request.”
  - sentence: need_based_special_circumstances ⟵ “We require this form be completed should you submit an “Unusual Circumstance” or Special Circumstance” form.”
### `10dc34bf9c686889` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $3,000 in addition to one other Huntingdon scholarship or award, except for Wilson Scholarships, Presidential Scholars, or Kingswood Initiative. ⟵ “Montgomery Public Schools Investment Scholarship | $3,000 in addition to one other Huntingdon scholarship or award, except for Wilson Scholarships, Presidential Scholars, or Kingswood Initiative. | Incoming freshmen who graduate from Booker T. Washington Magnet, Brewbaker Technology Magnet, Carver, ”
### `1620c182b18eca14` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $13,000 ⟵ “Wynton M. and Carolyn Blount Scholarship | $13,000 | 22 ACT/3.30 GPA or 3.50 GPA without test scoresFreshmen only”
### `2b89d2c0db5c1ba9` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $12,000 ⟵ “Hawk Award | $12,000 | Unconditional admission”
### `2ffe5a75847b1018` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “AISA Award | $12,500 | Graduate from an AISA school.”
### `34f34d3e99311bbc` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $20,000 ⟵ “Presidential Scholars | $20,000 | 3.0 GPA and 23 ACT or 3.75 GPA with no test scores.Open to incoming freshmen and transfer students with 36 credit hours or less of transfer credit.Campus residency required.Participation in the Presidential Scholars program, including an Academic Cohort, required.Pa”
### `41da307fafdaa6ed` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Scarlet & Grey Cheer Award | $14,000 | Limited—must participate in cheer activities as requested.Try-out required.Because of the time commitment for the Cheer program, participation is reserved for those who are not participating in NCAA-III athletic teams, the Presidential Scholars Program, the Kin”
### `54568326d2beeb3b` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “President A.A. Lipscomb Scholarship | $14,000 | 24 ACT/3.50 GPA or 3.70 GPA without test scoresFreshmen only”
### `564c20711afa5244` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Esports Award | $14,000 | Must participate in Esports.Because of the time commitment for this program, participation in Esports is reserved for those who are not participating in NCAA-III athletic teams, the Kingswood Initiative, Presidential Scholars Program, band, dance, or cheer teams.”
### `9d2ff535ce3a9c58` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “Military and Dependent Survivor Award | $12,500 | Must provide military ID.Complete the required application at Student Financial Services Forms.”
### `bafe5e5f56977ed6` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $13,500 ⟵ “President Walter D. Agnew Scholarship | $13,500 | 23 ACT/3.40 GPA or 3.60 GPA without test scoresFreshmen only”
### `bc628ffbd71d90a3` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “Cross & Flame Award | $12,500 | Active member of a Methodist church for at least one yearOfficial Cross & Flame clergy recommendation required (see Financial Assistance for Methodist Students).”
### `be55f816dfc54329` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Scarlet & Grey Band Award | $14,000 | Must participate in marching band, jazz/show band, BallHawks Pep Band, and symphonic band for fall and spring semesters as requested.Because of the time commitment for the band program, participation is reserved for those who are not participating in NCAA-III at”
### `c531602c6d72d2f1` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $16,500 ⟵ “James W. Wilson Jr. Scholarship | $16,500 | 3.75 GPA and 25 ACTFreshman only”
### `caf404a0a584cc28` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $14,000 ⟵ “Scarlet & Grey Dance Award | $14,000 | Limited—must participate in dance activities as requested.Try-out required.Because of the time commitment for the dance program, participation is reserved for those who are not participating in NCAA-III athletic teams, the Presidential Scholars Program, the Kin”
### `d1a1b0802999da68` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “River Region Award | $12,500 | Must live within 45 miles of the Huntingdon campus.”
### `d8d61aabdfe3e3a6` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “Corporate Alliance Award | $12,500 | Employee or employee dependent of a parent/guardian employed by Alabama Power, ALFA, Baptist Health, Synovus Bank, or UBS Financial Services.Corporate Alliance Application required (see Student Financial Services Forms.)”
### `e64b71847a1faff9` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $12,500 ⟵ “President John Massey Scholarship | $12,500 | 21 ACT/3.20 GPA or 3.40 GPA without test scoresFreshmen only”
### `fffbf4b9fd25be0c` Huntingdon College — awards 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/financial-aid-and-scholarship-programs/2025-2026-undergraduate-scholarships/ (sha256 81fd30afa431)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_amount_text: $9,000 ⟵ “Huntingdon Grant | $9,000 | Must meet admission requirements.”
### `1475b563a3179c9e` Huntingdon College — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/cost-of-attendance/ (sha256 1e24142b3927)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "components_reconcile": true, "rows": 8}
  - column:Tuition: 30900 ⟵ “Tuition | $30,900 | $30,900 | $30,900 | $1,290 per credit hour”
  - column:Commuter Fee: 0 ⟵ “Commuter Fee | 0 | $1,000 | $1,000 | $1,000”
  - column:Room and Board (Food & Housing): 11100 ⟵ “Room and Board (Food & Housing) | $11,100 | $5,966 | $9,675 | $5,966”
  - column:Semester Supplies: 100 ⟵ “Semester Supplies | $100 | $100 | $100 | $100”
  - column:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Miscellaneous Personal Expenses: 1000 ⟵ “Miscellaneous Personal Expenses | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Federal Student Loan Fees: 68 ⟵ “Federal Student Loan Fees | $68 | $68 | $68 | $68”
  - column:Total: 44168 ⟵ “Total | $44,168 | $40,034 | $43,743 | ”
  - column:Tuition: 30900 ⟵ “Tuition | $30,900 | $30,900 | $30,900 | $1,290 per credit hour”
  - column:Commuter Fee: 1000 ⟵ “Commuter Fee | 0 | $1,000 | $1,000 | $1,000”
  - column:Room and Board (Food & Housing): 5966 ⟵ “Room and Board (Food & Housing) | $11,100 | $5,966 | $9,675 | $5,966”
  - column:Semester Supplies: 100 ⟵ “Semester Supplies | $100 | $100 | $100 | $100”
  - column:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Miscellaneous Personal Expenses: 1000 ⟵ “Miscellaneous Personal Expenses | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Federal Student Loan Fees: 68 ⟵ “Federal Student Loan Fees | $68 | $68 | $68 | $68”
  - column:Total: 40034 ⟵ “Total | $44,168 | $40,034 | $43,743 | ”
  - column:Tuition: 30900 ⟵ “Tuition | $30,900 | $30,900 | $30,900 | $1,290 per credit hour”
  - column:Commuter Fee: 1000 ⟵ “Commuter Fee | 0 | $1,000 | $1,000 | $1,000”
  - column:Room and Board (Food & Housing): 9675 ⟵ “Room and Board (Food & Housing) | $11,100 | $5,966 | $9,675 | $5,966”
  - column:Semester Supplies: 100 ⟵ “Semester Supplies | $100 | $100 | $100 | $100”
  - column:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Miscellaneous Personal Expenses: 1000 ⟵ “Miscellaneous Personal Expenses | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Federal Student Loan Fees: 68 ⟵ “Federal Student Loan Fees | $68 | $68 | $68 | $68”
  - column:Total: 43743 ⟵ “Total | $44,168 | $40,034 | $43,743 | ”
  - column:Commuter Fee: 1000 ⟵ “Commuter Fee | 0 | $1,000 | $1,000 | $1,000”
  - … 5 more rows
### `ab3fe9cd66075a77` Huntingdon College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.huntingdon.edu/admission-aid/student-financial-services/cost-of-attendance/ (sha256 1e24142b3927)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "components_reconcile": true, "rows": 8}
  - column:Tuition: 30000 ⟵ “Tuition | $30,000 | $30,000 | $30,000 | $1,250 per credit hour”
  - column:Commuter Fee: 0 ⟵ “Commuter Fee | 0 | $1,000 | $1,000 | $1,000”
  - column:Room and Board (Food & Housing): 10922 ⟵ “Room and Board (Food & Housing) | $10,922 | $5,802 | $9,410 | $5,802”
  - column:Semester Supplies: 100 ⟵ “Semester Supplies | $100 | $100 | $100 | $100”
  - column:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Miscellaneous Personal Expenses: 1000 ⟵ “Miscellaneous Personal Expenses | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Federal Student Loan Fees: 68 ⟵ “Federal Student Loan Fees | $68 | $68 | $68 | $68”
  - column:Total: 43090 ⟵ “Total | $43,090 | $38,970 | $42,578 | ”
  - column:Tuition: 30000 ⟵ “Tuition | $30,000 | $30,000 | $30,000 | $1,250 per credit hour”
  - column:Commuter Fee: 1000 ⟵ “Commuter Fee | 0 | $1,000 | $1,000 | $1,000”
  - column:Room and Board (Food & Housing): 5802 ⟵ “Room and Board (Food & Housing) | $10,922 | $5,802 | $9,410 | $5,802”
  - column:Semester Supplies: 100 ⟵ “Semester Supplies | $100 | $100 | $100 | $100”
  - column:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Miscellaneous Personal Expenses: 1000 ⟵ “Miscellaneous Personal Expenses | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Federal Student Loan Fees: 68 ⟵ “Federal Student Loan Fees | $68 | $68 | $68 | $68”
  - column:Total: 38970 ⟵ “Total | $43,090 | $38,970 | $42,578 | ”
  - column:Tuition: 30000 ⟵ “Tuition | $30,000 | $30,000 | $30,000 | $1,250 per credit hour”
  - column:Commuter Fee: 1000 ⟵ “Commuter Fee | 0 | $1,000 | $1,000 | $1,000”
  - column:Room and Board (Food & Housing): 9410 ⟵ “Room and Board (Food & Housing) | $10,922 | $5,802 | $9,410 | $5,802”
  - column:Semester Supplies: 100 ⟵ “Semester Supplies | $100 | $100 | $100 | $100”
  - column:Transportation: 1000 ⟵ “Transportation | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Miscellaneous Personal Expenses: 1000 ⟵ “Miscellaneous Personal Expenses | $1,000 | $1,000 | $1,000 | $1,000”
  - column:Federal Student Loan Fees: 68 ⟵ “Federal Student Loan Fees | $68 | $68 | $68 | $68”
  - column:Total: 42578 ⟵ “Total | $43,090 | $38,970 | $42,578 | ”
  - column:Commuter Fee: 1000 ⟵ “Commuter Fee | 0 | $1,000 | $1,000 | $1,000”
  - … 5 more rows
### `ede96ce6b2ea248c` Huntingdon College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.huntingdon.edu/academics/office-of-the-registrar/transfer-credit/ (sha256 07ababd22265)
- issues: credits_implausible
- checks: {"distinct_exams": 29, "equivalencies": 35, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|Financial Accounting]:  ⟵ “Financial Accounting | -- | 50 | ACCT201”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|American Government]:  ⟵ “American Government | 47 | 50 | PSC 201”
  - equivalencies[CLEP-AMERICAN-LITERATURE|American Literature]:  ⟵ “American Literature | 46 | 50 | ENGL221 & 222”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|Introductory Business Law]:  ⟵ “Introductory Business Law | -- | 50 | BADM302”
  - equivalencies[CLEP-CALCULUS|Calculus]:  ⟵ “Calculus | 47 | 50 | MATH255”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|College Algebra]:  ⟵ “College Algebra | -- | 50 | MATH154”
  - equivalencies[CLEP-BIOLOGY|General Biology]:  ⟵ “General Biology | 46 | 50 | BIOL101”
  - equivalencies[CLEP-CHEMISTRY|General Chemistry]:  ⟵ “General Chemistry | NA | NA | NA”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|Educational Psychology]:  ⟵ “Educational Psychology | -- | 50 | PSYC000”
  - equivalencies[CLEP-ENGLISH-LITERATURE|English Literature]:  ⟵ “English Literature | 46 | 50 | ENGL211 & 212”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language]:  ⟵ “French Language | -- | 50-59 | FREN101”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language]:  ⟵ “French Language | -- | 60-69 | FREN101 & 102”
  - equivalencies[CLEP-FRENCH-LANGUAGE|French Language]:  ⟵ “French Language | -- | 70+ | FREN101, 102 & 201”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|College Composition]:  ⟵ “College Composition | 47 | 50 | ENGL103 & 104”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|Analyzing & Interpreting Literature]:  ⟵ “Analyzing & Interpreting Literature | 47 | 50 | ENGL202”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German Language]:  ⟵ “German Language | -- | 50-59 | GERM101”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German Language]:  ⟵ “German Language | -- | 60-69 | GERM101 & 102”
  - equivalencies[CLEP-GERMAN-LANGUAGE|German Language]:  ⟵ “German Language | -- | 70+ | GERM101, 102 & 201”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|Human Growth & Development]:  ⟵ “Human Growth & Development | -- | 50 | PSYC327”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|Principles of Macroeconomics]:  ⟵ “Principles of Macroeconomics | 48 | 50 | ECON202”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|Principles of Microeconomics]:  ⟵ “Principles of Microeconomics | 47 | 50 | ECON201”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|Principles of Management]:  ⟵ “Principles of Management | 50 | 50 | BADM312”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|Principles of Marketing]:  ⟵ “Principles of Marketing | 50 | 50 | BADM303”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|Introductory Psychology]:  ⟵ “Introductory Psychology | 47 | 50 | PSYC201”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|Introductory Sociology]:  ⟵ “Introductory Sociology | 47 | 50 | OTHE000”
  - … 10 more rows
### `4feac4bd7dda64b0` Huntingdon College — transfer_policies 2024-25 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/catalogs/2024-2025-catalog/ (sha256 251a352fd959)
- issues: stale_year_label:2024-25
- checks: {"fields": ["max_transfer_credits", "min_grade", "residency_requirement_credits"]}
  - min_grade: D ⟵ “Credit will be granted for any approved course completed with a grade of “D” or better, or in the case of a course taken on a Pass/No Credit basis (or the equivalent), a grade of “P.” The credit granted is indicated on the student’s transcript; however, transferred coursework does not affect a student’s Huntingdon College GPA.”
  - max_transfer_credits: 90 ⟵ “A maximum of 90 semester hours of transfer work may be credited toward the 120 hour degree requirement.”
  - residency_requirement_credits: 30 ⟵ “Students must comply with the College’s Terminal Residency policy (“30 Hour Rule”), which states that not more than one course in the last 30 semester credit hours may be taken outside of Huntingdon College.”
  - residency_requirement_credits: 30 ⟵ “If more than 30 semester credit hours are required, the final 30 semester credit hours must be at Huntingdon College.”
### `ee0a1bd15b787142` Huntingdon College — transfer_policies 2025-26 [new] (labeled_in_title)
- source: https://www.huntingdon.edu/catalogs/2025-2026-catalog/ (sha256 30d88274410e)
- issues: stale_year_label:2025-26
- checks: {"fields": ["max_transfer_credits", "min_grade", "residency_requirement_credits"]}
  - min_grade: D ⟵ “Credit will be granted for any approved course completed with a grade of “D” or better, or in the case of a course taken on a Pass/No Credit basis (or the equivalent), a grade of “P.” The credit granted is indicated on the student’s transcript; however, transferred coursework does not affect a student’s Huntingdon College GPA.”
  - max_transfer_credits: 90 ⟵ “A maximum of 90 semester hours of transfer work may be credited toward the 120 hour degree requirement.”
  - residency_requirement_credits: 30 ⟵ “Students must comply with the College’s Terminal Residency policy (“30 Hour Rule”), which states that not more than one course in the last 30 semester credit hours may be taken outside of Huntingdon College.”
  - residency_requirement_credits: 30 ⟵ “If more than 30 semester credit hours are required, the final 30 semester credit hours must be at Huntingdon College.”
### `371f4de813e30157` Huntsville Bible College — appeals 2024-25 [new] (labeled_in_heading)
- source: https://huntsvillebiblecollege.org/admissions/financial-aid/ (sha256 b7a6c6cfd832)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Financial Aid Forms 2024-25 Academic Year Dependent Verification Worksheet Independent Verification Worksheet Unusual Enrollment History Verification Special Circumstance Request Form Identity and Statement of Educational Purpose FINANCIAL AID OVERAWARD POLICY The Office of Student Financial Aid is required to monitor and adjust students’ financial aid offers to eliminate over awards and/or overpa”
### `86a516b9400feeeb` J. F. Drake State Community and Technical College — appeals 2024-25 [new] (labeled_in_source)
- source: https://drakestate.edu/wp-content/uploads/Professional-Judgement-Special-Circumstances-2425-1.pdf (sha256 4e471cc71527)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Circumstances Professional Judgment Review 2024-2025 Academic Year This form can be used to report changes that could affect the 2024-2025 Free Application for Federal Student Aid (FAFSA).”
### `94c1d17ef7a2e04a` J. F. Drake State Community and Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://drakestate.edu/admissions/tuition-fees/ (sha256 cc22c5a63f04)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 2, "rows": 7}
  - column:Tuition & Fees: 3060 ⟵ “Tuition & Fees | $3,060 |  | Tuition & Fees | $5,055”
  - column:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 |  | Books & Supplies | $1,000”
  - column:Housing: 4750 ⟵ “Housing | $4,750 |  | Housing | $4,750”
  - column:Food: 1350 ⟵ “Food | $1,350 |  | Food | $1,350”
  - column:Transportation: 1350 ⟵ “Transportation | $1,350 |  | Transportation | $1,350”
  - column:Miscellaneous: 675 ⟵ “Miscellaneous | $ 675 |  | Miscellaneous | $ 675”
  - column:Total: 12185 ⟵ “Total | $12,185 |  | Total | $14,180”
  - column:Tuition & Fees: 6120 ⟵ “Tuition & Fees | $6,120 |  | Tuition & Fees | $10,110”
  - column:Books & Supplies: 2000 ⟵ “Books & Supplies | $2,000 |  | Books & Supplies | $2,000”
  - column:Housing: 8550 ⟵ “Housing | $8,550 |  | Housing | $8,550”
  - column:Food: 2700 ⟵ “Food | $2,700 |  | Food | $2,700”
  - column:Transportation: 2700 ⟵ “Transportation | $2,700 |  | Transportation | $2,700”
  - column:Miscellaneous: 1350 ⟵ “Miscellaneous | $1,350 |  | Miscellaneous | $1,350”
  - column:Total: 23420 ⟵ “Total | $23,420 |  | Total | $27,410”
  - column:Tuition & Fees: 9180 ⟵ “Tuition & Fees | $9,180 |  | Tuition & Fees | $15,165”
  - column:Books & Supplies: 3000 ⟵ “Books & Supplies | $3,000 |  | Books & Supplies | $3,000”
  - column:Housing: 11400 ⟵ “Housing | $11,400 |  | Housing | $11,400”
  - column:Food: 3600 ⟵ “Food | $3,600 |  | Food | $3,600”
  - column:Transportation: 3600 ⟵ “Transportation | $3,600 |  | Transportation | $3,600”
  - column:Miscellaneous: 1800 ⟵ “Miscellaneous | $1,800 |  | Miscellaneous | $1,800”
  - column:Total: 32580 ⟵ “Total | $32,580 |  | Total | $38,565”
  - column:Tuition & Fees: 5055 ⟵ “Tuition & Fees | $3,060 |  | Tuition & Fees | $5,055”
  - column:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 |  | Books & Supplies | $1,000”
  - column:Housing: 4750 ⟵ “Housing | $4,750 |  | Housing | $4,750”
  - column:Food: 1350 ⟵ “Food | $1,350 |  | Food | $1,350”
  - … 17 more rows
### `3a3fa86e7a9bbece` Jacksonville State University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://webprod.jsu.edu/costcalculator/ (sha256 1cfb4ee1cf72)
- issues: residency_unknown, conflicting_sources:https://www.jsu.edu/bursar/fees/index.html
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition:: 0.0 ⟵ “Tuition: | $ 0.00”
  - column:General University Fee:: 0.0 ⟵ “General University Fee: | $ 0.00”
  - column:JaxBooks:: 0.0 ⟵ “JaxBooks: | $ 0.00”
  - column:Digital Instructional Fee:: 0.0 ⟵ “Digital Instructional Fee: | $ 0.00”
  - column:Housing:: 0.0 ⟵ “Housing: | $ 0.00”
  - column:Meal Plan:: 0.0 ⟵ “Meal Plan: | $ 0.00”
  - column:Total:: 0.0 ⟵ “Total: | $ 0.00”
### `901a6600aa7928ef` Jacksonville State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.jsu.edu/bursar/fees/index.html (sha256 7d441370fcf0)
- issues: residency_unknown, conflicting_sources:https://webprod.jsu.edu/costcalculator/
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition Based on block rate tuition: 10800 ⟵ “Tuition Based on block rate tuition | $10,800 | $10,800 | $10,800”
  - on_campus:Fees Based on average per student of General University Fee and Online Fee: 2860 ⟵ “Fees Based on average per student of General University Fee and Online Fee | $2,860 | $2,860 | $2,860”
  - on_campus:Books & Supplies Based on average from student survey data: 1056 ⟵ “Books & Supplies Based on average from student survey data | $1,056 | $1,056 | $1,056”
  - on_campus:Housing On-Campus: Based on average JSU on-campus housing rate Off-Campus and with Parent: Based on average from student survey data: 6104 ⟵ “Housing On-Campus: Based on average JSU on-campus housing rate Off-Campus and with Parent: Based on average from student survey data | $6,104 | $9,316 | $4,658”
  - on_campus:Food On-Campus: Based on JSU meal plan rate Off-Campus and with Parent: Based on average from student survey data: 4290 ⟵ “Food On-Campus: Based on JSU meal plan rate Off-Campus and with Parent: Based on average from student survey data | $4,290 | $3,852 | $1,926”
  - on_campus:Transport: 2106 ⟵ “Transport | $2,106 | $3,645 | $3,420”
  - on_campus:Misc Based on average from student survey data: 2260 ⟵ “Misc Based on average from student survey data | $2,260 | $2,260 | $2,260”
  - on_campus:Total: 29476 ⟵ “Total | $29,476 | $33,789 | $26,980”
  - off_campus_not_with_family:Tuition Based on block rate tuition: 10800 ⟵ “Tuition Based on block rate tuition | $10,800 | $10,800 | $10,800”
  - off_campus_not_with_family:Fees Based on average per student of General University Fee and Online Fee: 2860 ⟵ “Fees Based on average per student of General University Fee and Online Fee | $2,860 | $2,860 | $2,860”
  - off_campus_not_with_family:Books & Supplies Based on average from student survey data: 1056 ⟵ “Books & Supplies Based on average from student survey data | $1,056 | $1,056 | $1,056”
  - off_campus_not_with_family:Housing On-Campus: Based on average JSU on-campus housing rate Off-Campus and with Parent: Based on average from student survey data: 9316 ⟵ “Housing On-Campus: Based on average JSU on-campus housing rate Off-Campus and with Parent: Based on average from student survey data | $6,104 | $9,316 | $4,658”
  - off_campus_not_with_family:Food On-Campus: Based on JSU meal plan rate Off-Campus and with Parent: Based on average from student survey data: 3852 ⟵ “Food On-Campus: Based on JSU meal plan rate Off-Campus and with Parent: Based on average from student survey data | $4,290 | $3,852 | $1,926”
  - off_campus_not_with_family:Transport: 3645 ⟵ “Transport | $2,106 | $3,645 | $3,420”
  - off_campus_not_with_family:Misc Based on average from student survey data: 2260 ⟵ “Misc Based on average from student survey data | $2,260 | $2,260 | $2,260”
  - off_campus_not_with_family:Total: 33789 ⟵ “Total | $29,476 | $33,789 | $26,980”
  - with_parents_or_family:Tuition Based on block rate tuition: 10800 ⟵ “Tuition Based on block rate tuition | $10,800 | $10,800 | $10,800”
  - with_parents_or_family:Fees Based on average per student of General University Fee and Online Fee: 2860 ⟵ “Fees Based on average per student of General University Fee and Online Fee | $2,860 | $2,860 | $2,860”
  - with_parents_or_family:Books & Supplies Based on average from student survey data: 1056 ⟵ “Books & Supplies Based on average from student survey data | $1,056 | $1,056 | $1,056”
  - with_parents_or_family:Housing On-Campus: Based on average JSU on-campus housing rate Off-Campus and with Parent: Based on average from student survey data: 4658 ⟵ “Housing On-Campus: Based on average JSU on-campus housing rate Off-Campus and with Parent: Based on average from student survey data | $6,104 | $9,316 | $4,658”
  - with_parents_or_family:Food On-Campus: Based on JSU meal plan rate Off-Campus and with Parent: Based on average from student survey data: 1926 ⟵ “Food On-Campus: Based on JSU meal plan rate Off-Campus and with Parent: Based on average from student survey data | $4,290 | $3,852 | $1,926”
  - with_parents_or_family:Transport: 3420 ⟵ “Transport | $2,106 | $3,645 | $3,420”
  - with_parents_or_family:Misc Based on average from student survey data: 2260 ⟵ “Misc Based on average from student survey data | $2,260 | $2,260 | $2,260”
  - with_parents_or_family:Total: 26980 ⟵ “Total | $29,476 | $33,789 | $26,980”
### `0e8c7ffdc3794da5` Jefferson State Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.jeffersonstate.edu/wp-content/uploads/2026/09/2026-2027-Cost-of-Attendance.pdf (sha256 bd60419167d1)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 3, "rows": 8}
  - column:Tuition and Fees: 2940.0 ⟵ “Tuition and Fees | $2,940.00 | $5,880.00 | $8,820.00”
  - column:Room and Board: 3767.0 ⟵ “Room and Board | $3767.00 | $7,533.00 | $10,044.00”
  - column:Books & Supplies: 605.0 ⟵ “Books & Supplies | $605.00 | $1,210.00 | $1,815.00”
  - column:Transportation: 1624.0 ⟵ “Transportation | $1,624.00 | $3,248.00 | $4,263.00”
  - column:Personal/Miscellaneous: 1125.0 ⟵ “Personal/Miscellaneous | $1,125.00 | $2,250.00 | $3,000.00”
  - column:Total: 10061.0 ⟵ “Total | $10,061.00 | $20,121.00 | $27,942.00”
  - column:Tuition and Fees: 2940.0 ⟵ “Tuition and Fees | $2,940.00 | $5,880.00 | $8,820.00”
  - column:Room and Board: 7533.0 ⟵ “Room and Board | $7,533.00 | $15,066.00 | $20,088.00”
  - column:Books & Supplies: 605.0 ⟵ “Books & Supplies | $605.00 | $1,210.00 | $1,815.00”
  - column:Transportation: 1624.0 ⟵ “Transportation | $1,624.00 | $3,248.00 | $4,263.00”
  - column:Personal /Miscellaneous: 1125.0 ⟵ “Personal /Miscellaneous | $1,125.00 | $2,250.00 | $3,000.00”
  - column:Total: 13827.0 ⟵ “Total | $13,827.00 | $27,654.00 | $37,986.00”
  - column:Tuition and Fees: 980.0 ⟵ “Tuition and Fees | $980.00 | $1,960.00 | $2,940.00”
  - column:Books & Supplies: 235.0 ⟵ “Books & Supplies | $235.00 | $470.00 | $705.00”
  - column:Transportation: 812.0 ⟵ “Transportation | $812.00 | $1,624.00 | $2,132.00”
  - column:*Room and Board: 1884.0 ⟵ “*Room and Board | $1,884.00 | $3,767.00 | $5,022.00”
  - column:Total: 3911.0 ⟵ “Total | $3,911.00 | $7,821.00 | $10,799.00”
  - column:Tuition and Fees: 5880.0 ⟵ “Tuition and Fees | $2,940.00 | $5,880.00 | $8,820.00”
  - column:Room and Board: 7533.0 ⟵ “Room and Board | $3767.00 | $7,533.00 | $10,044.00”
  - column:Books & Supplies: 1210.0 ⟵ “Books & Supplies | $605.00 | $1,210.00 | $1,815.00”
  - column:Transportation: 3248.0 ⟵ “Transportation | $1,624.00 | $3,248.00 | $4,263.00”
  - column:Personal/Miscellaneous: 2250.0 ⟵ “Personal/Miscellaneous | $1,125.00 | $2,250.00 | $3,000.00”
  - column:Total: 20121.0 ⟵ “Total | $10,061.00 | $20,121.00 | $27,942.00”
  - column:Tuition and Fees: 5880.0 ⟵ “Tuition and Fees | $2,940.00 | $5,880.00 | $8,820.00”
  - column:Room and Board: 15066.0 ⟵ “Room and Board | $7,533.00 | $15,066.00 | $20,088.00”
  - … 26 more rows
### `f88cd66a9f49ee1e` Jefferson State Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.jeffersonstate.edu/wp-content/uploads/2025/07/2025-2026-Cost-of-Attendance.pdf (sha256 450273ab91ff)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 8}
  - column:Tuition and Fees: 2760.0 ⟵ “Tuition and Fees | $2,760.00 | $5,520.00 | $8,280.00”
  - column:Room and Board: 3767.0 ⟵ “Room and Board | $3767.00 | $7,533.00 | $10,044.00”
  - column:Books & Supplies: 560.0 ⟵ “Books & Supplies | $560.00 | $1,120.00 | $1,680.00”
  - column:Transportation: 1568.0 ⟵ “Transportation | $1,568.00 | $3,136.00 | $4,116.00”
  - column:Personal/Miscellaneous: 1125.0 ⟵ “Personal/Miscellaneous | $1,125.00 | $2,250.00 | $3,000.00”
  - column:Total: 9780.0 ⟵ “Total | $9,780.00 | $19,559.00 | $27,120.00”
  - column:Tuition and Fees: 2760.0 ⟵ “Tuition and Fees | $2,760.00 | $5,520.00 | $8,280.00”
  - column:Room and Board: 7533.0 ⟵ “Room and Board | $7,533.00 | $15,066.00 | $20,088.00”
  - column:Books & Supplies: 560.0 ⟵ “Books & Supplies | $560.00 | $1,120.00 | $1,680.00”
  - column:Transportation: 1568.0 ⟵ “Transportation | $1,568.00 | $3,136.00 | $4,116.00”
  - column:Personal /Miscellaneous: 1125.0 ⟵ “Personal /Miscellaneous | $1,125.00 | $2,250.00 | $3,000.00”
  - column:Total: 13546.0 ⟵ “Total | $13,546.00 | $27,092.00 | $37,164.00”
  - column:Tuition and Fees: 860.0 ⟵ “Tuition and Fees | $860.00 | $1,720.00 | $2,580.00”
  - column:Books & Supplies: 220.0 ⟵ “Books & Supplies | $220.00 | $440.00 | $660.00”
  - column:Transportation: 784.0 ⟵ “Transportation | $784.00 | $1,568.00 | $2,058.00”
  - column:*Room and Board: 1884.0 ⟵ “*Room and Board | $1,884.00 | $3,767.00 | $5,022.00”
  - column:Total: 3748.0 ⟵ “Total | $3,748.00 | $7,495.00 | $10,320.00”
  - column:Tuition and Fees: 5520.0 ⟵ “Tuition and Fees | $2,760.00 | $5,520.00 | $8,280.00”
  - column:Room and Board: 7533.0 ⟵ “Room and Board | $3767.00 | $7,533.00 | $10,044.00”
  - column:Books & Supplies: 1120.0 ⟵ “Books & Supplies | $560.00 | $1,120.00 | $1,680.00”
  - column:Transportation: 3136.0 ⟵ “Transportation | $1,568.00 | $3,136.00 | $4,116.00”
  - column:Personal/Miscellaneous: 2250.0 ⟵ “Personal/Miscellaneous | $1,125.00 | $2,250.00 | $3,000.00”
  - column:Total: 19559.0 ⟵ “Total | $9,780.00 | $19,559.00 | $27,120.00”
  - column:Tuition and Fees: 5520.0 ⟵ “Tuition and Fees | $2,760.00 | $5,520.00 | $8,280.00”
  - column:Room and Board: 15066.0 ⟵ “Room and Board | $7,533.00 | $15,066.00 | $20,088.00”
  - … 26 more rows
### `m2969ea79107824a` John C Calhoun State Community College — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://calhoun.edu/admissions/apply/high-school-students/dual-enrollment/dual-enrollment-scholarships/ (sha256 f8092b415b2f)
- issues: conflicting_sources:state_grant_accepted
- checks: {"fields": ["min_hs_gpa", "state_grant_accepted"], "merged_pages": 4, "tiers": 1}
  - state_grant_accepted: True ⟵ “Funds are available through a Workforce grant to provide scholarships to Dual Enrollment students in specific business and technical programs. These Dual Enrollment scholarship funds are available to eligible high school students participating in approved technology programs offered by Calhoun Commu”
  - eligibility_tier: 2.0 ⟵ “Students in Advanced Manufacturing and Automotive classes must have a 2.0 GPA or higher. Students in all other programs, and students taking any academic classes, must have a 2.5 GPA or higher.”
  - state_grant_accepted: True ⟵ “To apply for a dual enrollment scholarship, contact our team:”
  - eligibility_tier: 2.5 ⟵ “GPA Requirement: students must have a 2.5 GPA or higher in completed high school courses with the exception of Automotive and Technologies programs. The GPA for those programs is 2.0.”
  - state_grant_accepted: False ⟵ “A Dual Enrollment student who withdrew or who earned a grade of D or F in more than one class, technical or academic, will not be eligible for any future Dual Enrollment scholarship funding and will not be eligible to continue in the Dual Enrollment program.”
  - state_grant_accepted: False ⟵ “or academic, will not be eligible for any future Dual Enrollment scholarship funding.”
  - eligibility_tier: 2.5 ⟵ “3. Students must have a minimum cumulative (unweighted) high school grade point average of 2.5”
  - eligibility_tier: 2.5 ⟵ “(unweighted) grade point average of 2.5 on a 4.0 scale.”
### `ee7ddb94ece090ab` John C Calhoun State Community College — transfer_policies 2017-18 [new] (labeled_in_source)
- source: https://catalog.calhoun.edu/general-principles-for-transfer-of-credit (sha256 eae62c9e5cc3)
- issues: stale_year_label:2017-18
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Exceptions to the English proficiency requirement include students who have graduated from a regionally accredited United States high school, a transfer student who has successfully completed ENG 101 with a grade of C or higher at a regionally accredited United States college or university, or a citizen of an English speaking country that has been granted an exemption to the testing requirement.”
### `44e1f6a3f6056adc` Lurleen B Wallace Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lbwcc.edu/future-students/financial-aid (sha256 7040153e667b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If a student is academically suspended and readmitted on an admissions appeal, this does not automatically qualify a student for reinstatement of financial aid.Financial aid will be reinstated when the student attends college at his/her own expense and meets the minimum standards of satisfactory academic progress or if the Financial Aid Appeal Committee reinstates eligibility.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Process: To originate a request for a financial aid appeal, students may contact the financial aid office and consult with Natalie Darden-Ray via email at ndarden-ray@lbwcc.edu or by phone at 334-881-2341 or Bren-Nesha Pough via email at bpough@lbwcc.edu or by phone at 334-493-5338.”
### `8e5587c6aaa9a56a` Lurleen B Wallace Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.lbwcc.edu/future-students/financial-aid (sha256 7040153e667b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: professional_judgment ⟵ “Non-Year Specific Financial forms: Dependency Override Form Certification of Marital Separation - Dependent Student Certification of Marital Separation - Independent Student​ Professional Judgment (PJ) Appeals Process: What is a Professional Judgment (PJ) Appeal?”
  - sentence: professional_judgment ⟵ “A Professional Judgment (PJ) Appeal is used when a student and/or parent, if dependent, has substantial changes in income from the year that the FAFSA application was completed.”
  - sentence: professional_judgment ⟵ “How do I apply for a Professional Judgment Appeal?”
  - sentence: professional_judgment ⟵ “Please contact the following according to the first letter of your last name for the appropriate form(s) or for more information regarding professional judgments: A-K - Natalie Darden-Ray via email at ndarden-ray@lbwcc.edu or by phone at 334-881-2341.”
  - sentence: professional_judgment ⟵ “However, most financial aid administrators would use professional judgment to override the default dependency determination for a student born on January 1 who also demonstrates financial self-sufficiency.”
### `4b1710aa68c960a2` Lurleen B Wallace Community College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lbwcc.edu/Content/Uploads/LBWCCredesign/files/2024-2025%20SU25%20Student%20Budget.pdf (sha256 14908488ccaf)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 3, "rows": 23}
  - column:TUITION: 1935.0 ⟵ “TUITION | $1,935.00 | $1,935.00 | $1,935.00”
  - column:ENHANCEMENT FEE: 150.0 ⟵ “ENHANCEMENT FEE | $150.00 | $150.00 | $150.00”
  - column:BUILDING FEE: 225.0 ⟵ “BUILDING FEE | $225.00 | $225.00 | $225.00”
  - column:BOND RESERVE FEE: 15.0 ⟵ “BOND RESERVE FEE | $15.00 | $15.00 | $15.00”
  - column:FACILITY FEES: 135.0 ⟵ “FACILITY FEES | $135.00 | $135.00 | $135.00”
  - column:TECHNOLOGY FEES: 135.0 ⟵ “TECHNOLOGY FEES | $135.00 | $135.00 | $135.00”
  - column:BOOKS AND SUPPLIES: 905.0 ⟵ “BOOKS AND SUPPLIES | $905.00 | $905.00 | $905.00”
  - column:FOOD AND HOUSING: 1929.0 ⟵ “FOOD AND HOUSING | $1,929.00 | $2,662.00 | $5,109.00”
  - column:TRANSPORTATION: 1013.0 ⟵ “TRANSPORTATION | $1,013.00 | $1,013.00 | $1,013.00”
  - column:MISC. AND PERSONAL EXPENSES: 1000.0 ⟵ “MISC. AND PERSONAL EXPENSES | $1,000.00 | $1,000.00 | $1,000.00”
  - column:Total Budget: 7442.0 ⟵ “Total Budget | $7,442.00 | $8,175.00 | $10,622.00”
  - column:TUITION: 3870.0 ⟵ “TUITION | $3,870.00 | $3,870.00 | $3,870.00”
  - column:ENHANCEMENT FEE: 150.0 ⟵ “ENHANCEMENT FEE | $150.00 | $150.00 | $150.00”
  - column:BUILDING FEE: 225.0 ⟵ “BUILDING FEE | $225.00 | $225.00 | $225.00”
  - column:BOND RESERVE FEE: 15.0 ⟵ “BOND RESERVE FEE | $15.00 | $15.00 | $15.00”
  - column:FACILITY FEES: 135.0 ⟵ “FACILITY FEES | $135.00 | $135.00 | $135.00”
  - column:TECHNOLOGY FEES: 135.0 ⟵ “TECHNOLOGY FEES | $135.00 | $135.00 | $135.00”
  - column:BOOKS AND SUPPLIES: 905.0 ⟵ “BOOKS AND SUPPLIES | $905.00 | $905.00 | $905.00”
  - column:FOOD AND HOUSING: 1929.0 ⟵ “FOOD AND HOUSING | $1,929.00 | $2,662.00 | $5,109.00”
  - column:TRANSPORTATION: 1013.0 ⟵ “TRANSPORTATION | $1,013.00 | $1,013.00 | $1,013.00”
  - column:MISC. AND PERSONAL EXPENSES: 1000.0 ⟵ “MISC. AND PERSONAL EXPENSES | $1,000.00 | $1,000.00 | $1,000.00”
  - column:Total Budget: 9377.0 ⟵ “Total Budget | $9,377.00 | $10,110.00 | $12,557.00”
  - column:TUITION: 1935.0 ⟵ “TUITION | $1,935.00 | $3,870.00”
  - column:ENHANCEMENT FEE: 150.0 ⟵ “ENHANCEMENT FEE | $150.00 | $150.00”
  - column:BUILDING FEE: 225.0 ⟵ “BUILDING FEE | $225.00 | $225.00”
  - … 71 more rows
### `80618aea06ba44ef` Lurleen B Wallace Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lbwcc.edu/Content/Uploads/LBWCCredesign/files/2026-2027%20FA-SP-SU%20Student%20Budget(1).pdf (sha256 372e65e3f3e1)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, conflicting_sources:https://www.lbwcc.edu/Content/Uploads/LBWCCredesign/files/2026-2027%20SU%20Student%20Budget.pdf
- checks: {"columns": 3, "rows": 30}
  - column:TUITION: 3990.0 ⟵ “TUITION | $3,990.00 | $3,990.00 | $3,990.00”
  - column:ENHANCEMENT FEE: 600.0 ⟵ “ENHANCEMENT FEE | $600.00 | $600.00 | $600.00”
  - column:BUILDING FEE: 450.0 ⟵ “BUILDING FEE | $450.00 | $450.00 | $450.00”
  - column:BOND RESERVE FEE: 30.0 ⟵ “BOND RESERVE FEE | $30.00 | $30.00 | $30.00”
  - column:FACILITY FEES: 450.0 ⟵ “FACILITY FEES | $450.00 | $450.00 | $450.00”
  - column:TECHNOLOGY FEES: 450.0 ⟵ “TECHNOLOGY FEES | $450.00 | $450.00 | $450.00”
  - column:BOOKS AND SUPPLIES: 1810.0 ⟵ “BOOKS AND SUPPLIES | $1,810.00 | $1,810.00 | $1,810.00”
  - column:HOUSING AND FOOD: 8284.0 ⟵ “HOUSING AND FOOD | $8,284.00 | $16,617.00 | $19,417.00”
  - column:TRANSPORTATION: 3698.0 ⟵ “TRANSPORTATION | $3,698.00 | $3,698.00 | $3,698.00”
  - column:MISC. AND PERSONAL EXPENSES: 1000.0 ⟵ “MISC. AND PERSONAL EXPENSES | $1,000.00 | $1,000.00 | $1,000.00”
  - column:Total Budget: 20762.0 ⟵ “Total Budget | $20,762.00 | $29,095.00 | $31,895.00”
  - column:TUITION: 7980.0 ⟵ “TUITION | $7,980.00 | $7,980.00 | $7,980.00”
  - column:ENHANCEMENT FEE: 600.0 ⟵ “ENHANCEMENT FEE | $600.00 | $600.00 | $600.00”
  - column:BUILDING FEE: 450.0 ⟵ “BUILDING FEE | $450.00 | $450.00 | $450.00”
  - column:BOND RESERVE FEE: 30.0 ⟵ “BOND RESERVE FEE | $30.00 | $30.00 | $30.00”
  - column:FACILITY FEES: 450.0 ⟵ “FACILITY FEES | $450.00 | $450.00 | $450.00”
  - column:TECHNOLOGY FEES: 450.0 ⟵ “TECHNOLOGY FEES | $450.00 | $450.00 | $450.00”
  - column:BOOKS AND SUPPLIES: 1810.0 ⟵ “BOOKS AND SUPPLIES | $1,810.00 | $1,810.00 | $1,810.00”
  - column:HOUSING AND FOOD: 8284.0 ⟵ “HOUSING AND FOOD | $8,284.00 | $16,617.00 | $19,417.00”
  - column:TRANSPORTATION: 3698.0 ⟵ “TRANSPORTATION | $3,698.00 | $3,698.00 | $3,698.00”
  - column:MISC. AND PERSONAL EXPENSES: 1000.0 ⟵ “MISC. AND PERSONAL EXPENSES | $1,000.00 | $1,000.00 | $1,000.00”
  - column:Total Budget: 24752.0 ⟵ “Total Budget | $24,752.00 | $33,085.00 | $35,885.00”
  - column:TUITION: 3990.0 ⟵ “TUITION | $3,990.00 | $7,980.00”
  - column:ENHANCEMENT FEE: 600.0 ⟵ “ENHANCEMENT FEE | $600.00 | $600.00”
  - column:BUILDING FEE: 450.0 ⟵ “BUILDING FEE | $450.00 | $450.00”
  - … 168 more rows
### `cde1c8d2ffff3225` Lurleen B Wallace Community College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.lbwcc.edu/Content/Uploads/LBWCCredesign/files/2026-2027%20SU%20Student%20Budget.pdf (sha256 2051b27e5823)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, conflicting_sources:https://www.lbwcc.edu/Content/Uploads/LBWCCredesign/files/2026-2027%20FA-SP-SU%20Student%20Budget(1).pdf
- checks: {"columns": 3, "rows": 23}
  - column:TUITION: 1995.0 ⟵ “TUITION | $1,995.00 | $1,995.00 | $1,995.00”
  - column:ENHANCEMENT FEE: 300.0 ⟵ “ENHANCEMENT FEE | $300.00 | $300.00 | $300.00”
  - column:BUILDING FEE: 225.0 ⟵ “BUILDING FEE | $225.00 | $225.00 | $225.00”
  - column:BOND RESERVE FEE: 15.0 ⟵ “BOND RESERVE FEE | $15.00 | $15.00 | $15.00”
  - column:FACILITY FEES: 225.0 ⟵ “FACILITY FEES | $225.00 | $225.00 | $225.00”
  - column:TECHNOLOGY FEES: 225.0 ⟵ “TECHNOLOGY FEES | $225.00 | $225.00 | $225.00”
  - column:BOOKS AND SUPPLIES: 905.0 ⟵ “BOOKS AND SUPPLIES | $905.00 | $905.00 | $905.00”
  - column:FOOD AND HOUSING: 2838.0 ⟵ “FOOD AND HOUSING | $2,838.00 | $2,643.00 | $6,699.00”
  - column:TRANSPORTATION: 1305.0 ⟵ “TRANSPORTATION | $1,305.00 | $1,305.00 | $1,305.00”
  - column:MISC. AND PERSONAL EXPENSES: 1000.0 ⟵ “MISC. AND PERSONAL EXPENSES | $1,000.00 | $1,000.00 | $1,000.00”
  - column:Total Budget: 9033.0 ⟵ “Total Budget | $9,033.00 | $8,838.00 | $12,894.00”
  - column:TUITION: 3990.0 ⟵ “TUITION | $3,990.00 | $3,990.00 | $3,990.00”
  - column:ENHANCEMENT FEE: 300.0 ⟵ “ENHANCEMENT FEE | $300.00 | $300.00 | $300.00”
  - column:BUILDING FEE: 225.0 ⟵ “BUILDING FEE | $225.00 | $225.00 | $225.00”
  - column:BOND RESERVE FEE: 15.0 ⟵ “BOND RESERVE FEE | $15.00 | $15.00 | $15.00”
  - column:FACILITY FEES: 225.0 ⟵ “FACILITY FEES | $225.00 | $225.00 | $225.00”
  - column:TECHNOLOGY FEES: 225.0 ⟵ “TECHNOLOGY FEES | $225.00 | $225.00 | $225.00”
  - column:BOOKS AND SUPPLIES: 905.0 ⟵ “BOOKS AND SUPPLIES | $905.00 | $905.00 | $905.00”
  - column:FOOD AND HOUSING: 2838.0 ⟵ “FOOD AND HOUSING | $2,838.00 | $2,643.00 | $6,699.00”
  - column:TRANSPORTATION: 1305.0 ⟵ “TRANSPORTATION | $1,305.00 | $1,305.00 | $1,305.00”
  - column:MISC. AND PERSONAL EXPENSES: 1000.0 ⟵ “MISC. AND PERSONAL EXPENSES | $1,000.00 | $1,000.00 | $1,000.00”
  - column:Total Budget: 11028.0 ⟵ “Total Budget | $11,028.00 | $10,833.00 | $14,889.00”
  - column:TUITION: 1995.0 ⟵ “TUITION | $1,995.00 | $3,990.00”
  - column:ENHANCEMENT FEE: 300.0 ⟵ “ENHANCEMENT FEE | $300.00 | $300.00”
  - column:BUILDING FEE: 225.0 ⟵ “BUILDING FEE | $225.00 | $225.00”
  - … 71 more rows
### `8c1aadc1c1eb2650` Lurleen B Wallace Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.lbwcc.edu/Content/Uploads/LBWCCredesign/files/CLEP%20Chart.pdf (sha256 a5d655e24c36)
- issues: credits_implausible
- checks: {"distinct_exams": 22, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology                               8      Biology II OR BIO103: Principles of Biology I AND BIO104:          50”
  - equivalencies[CLEP-CALCULUS|4]:  ⟵ “Calculus                              4      MTH125: Calculus I                                                 50”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry                             8      CHM111: College Chemistry I AND CHM112: College Chemistry II       50”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|3]:  ⟵ “College Algebra                       3      MTH100: Intermediate College Algebra                               50”
  - equivalencies[CLEP-PRECALCULUS|3]:  ⟵ “Precalculus                           3      MTH112: Precalculus Algebra                                        50”
  - equivalencies[CLEP-AMERICAN-LITERATURE|3]:  ⟵ “American Literature                   3      ENG251: American Literature I                                      50”
  - equivalencies[CLEP-ENGLISH-LITERATURE|3]:  ⟵ “English Literature                    3      ENG261: English Literature I OR ENG262: English Literature II      50”
  - equivalencies[CLEP-HUMANITIES|3]:  ⟵ “Humanities                            3                                                                         50”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|3]:  ⟵ “American Government                   3      POL211: American National Government                               50”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|3]:  ⟵ “Financial Accounting                  3      BUS241: Principles of Accounting I                                 50”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|3]:  ⟵ “History of the United States I        3      HIS201: United States History I                                    50”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|3]:  ⟵ “History of the United States II       3      HIS202: United States History II                                   50”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|3]:  ⟵ “Introductory Business Law             3      BUS263: The Legal and Social Environment of Business               50”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|3]:  ⟵ “Introductory Psychology               3      PSY200: General Psychology                                         50”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|3]:  ⟵ “Introductory Sociology                3      SOC200: Introduction to Sociology                                  50”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|3]:  ⟵ “Principles of Macroeconomics          3      ECO231: Principles of Macroeconomics                               50”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|3]:  ⟵ “Principles of Management              3      BUS275: Principles of Management                                   50”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|3]:  ⟵ “Principles of Marketing               3      BUS285: Principles of Marketing                                    50”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|3]:  ⟵ “Principles of Microeconomics          3      ECO232: Principles of Microeconomics                               50”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|3]:  ⟵ “Western Civilization I                3      HIS101: Western Civilization I                                     50”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|3]:  ⟵ “Western Civilization II               3      HIS102: Western Civilization II                                    50”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|3]:  ⟵ “Information Systems                   3      CIS146: Computer Applications                                      50”
### `011529d6cfee3925` Marion Military Institute — appeals 2026-27 [new] (source_unlabeled)
- source: https://marionmilitary.edu/mmi-sap-policy/ (sha256 14ef9968fdc4)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Cadets on SAP probation are not eligible to receive financial aid and must appeal to have financial aid eligibility reinstated (See SAP Appeal Process).”
  - sentence: sap_appeal ⟵ “Your Rights to Appeal A cadet placed on SAP Probation, may appeal to have financial aid reinstated, if: Your record shows that you earned the required GPA or credit completion ratio to meet SAP standards during term. · Unusual circumstance interfered with your ability to meet SAP standards, including but not limited to: · Illness, accident, or injury experienced by you or family member under your ”
  - sentence: sap_appeal ⟵ “Appeal Process To appeal your financial aid suspension due to mitigating circumstances listed above or similar personal situations complete the Satisfactory Academic Progress Appeal form and include the required documentation.”
### `12da9a6ebe9cf7d8` Marion Military Institute — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://marionmilitary.edu/admissions/tuition-and-fees/ (sha256 2501a184df9d)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 11}
  - column:Tuition: 12000 ⟵ “Tuition | $6,000 | $12,000”
  - column:Technology Fee*: 630 ⟵ “Technology Fee* | $630 | $630”
  - column:Reserve Fee*: 42 ⟵ “Reserve Fee* | $42 | $42”
  - column:Facility Fee*: 630 ⟵ “Facility Fee* | $630 | $630”
  - column:ACCS Enhancement Fee*: 840 ⟵ “ACCS Enhancement Fee* | $840 | $840”
  - column:Accident Insurance: 150 ⟵ “Accident Insurance | $150 | $150”
  - column:Total Tuition and Fees*: 14292 ⟵ “Total Tuition and Fees* | $8,292 | $14,292”
  - column:Room and Board: 5950 ⟵ “Room and Board | $5,950 | $5,950”
  - column:Estimated Uniform Cost**: 2170 ⟵ “Estimated Uniform Cost** | $2,170 | $2,170”
  - column:Estimated Book Costs***: 1800 ⟵ “Estimated Book Costs*** | $1,800 | $1,800”
  - column:Total Costs: 24212 ⟵ “Total Costs | $18,212 | $24,212”
### `f82ac41eae41b994` Marion Military Institute — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://marionmilitary.edu/admissions/tuition-and-fees/ (sha256 2501a184df9d)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 11}
  - column:Tuition: 6000 ⟵ “Tuition | $6,000 | $12,000”
  - column:Technology Fee*: 630 ⟵ “Technology Fee* | $630 | $630”
  - column:Reserve Fee*: 42 ⟵ “Reserve Fee* | $42 | $42”
  - column:Facility Fee*: 630 ⟵ “Facility Fee* | $630 | $630”
  - column:ACCS Enhancement Fee*: 840 ⟵ “ACCS Enhancement Fee* | $840 | $840”
  - column:Accident Insurance: 150 ⟵ “Accident Insurance | $150 | $150”
  - column:Total Tuition and Fees*: 8292 ⟵ “Total Tuition and Fees* | $8,292 | $14,292”
  - column:Room and Board: 5950 ⟵ “Room and Board | $5,950 | $5,950”
  - column:Estimated Uniform Cost**: 2170 ⟵ “Estimated Uniform Cost** | $2,170 | $2,170”
  - column:Estimated Book Costs***: 1800 ⟵ “Estimated Book Costs*** | $1,800 | $1,800”
  - column:Total Costs: 18212 ⟵ “Total Costs | $18,212 | $24,212”
### `b69ea967b7564e4d` Miles College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.miles.edu/satisfactory-academic-program-policy (sha256 e0a8a207e8c3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “Back to Top Appeal Procedure Students not meeting SAP may appeal for reconsideration of financial aid.”
  - sentence: sap_appeal ⟵ “To appeal for the reinstatement of financial aid eligibility, students must complete and submit the SAP appeal form to the SAP Coordinator indicating the extenuating circumstance(s) (i.e. personal illness, injury, medical problems, military obligations, change in living arrangements, undue hardship, death of parent or immediate family member or relative, family emergency or other special circumsta”
  - sentence: sap_appeal ⟵ “Documents supporting the student’s appeal must accompany (if applicable) the SAP Appeal form.”
  - sentence: sap_appeal ⟵ “It is important to note that submitting a Satisfactory Academic Progress Appeal form does not guarantee an approval for reinstatement of a student’s aid eligibility.”
  - sentence: sap_appeal ⟵ “Receive an Approved SAP appeal.”
### `210ddf94aa06b901` Northeast Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nacc.edu/admission-financial-aid/financial-aid/financial-aid-policies/ (sha256 21fd6b979548)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Eligibility is normally based upon the prior year’s income.”
### `8fa823f939c6aa25` Northeast Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nacc.edu/admission-financial-aid/financial-aid (sha256 a4158b61f87c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “We may be able to adjust your income through a Professional Judgement to get you more Pell grant money.”
### `a0466bcd30be3348` Northeast Alabama Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nacc.edu/Content/Uploads/NACC/files/Financial%20Aid/2026-2027%20FORMS/SAP%20Appeal%20Form.pdf (sha256 fdb689162919)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Semester: Appeal Priority Deadlines:  Fall Semester Fall – August 19th  Spring Semester Spring – January 6th  Summer Semester Summer – May 23st Have you previously submitted a Financial Aid SAP Appeal? __________ 2.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form 2.”
  - sentence: sap_appeal ⟵ “Student Acknowledgments • Please allow 2 weeks for processing • If DENIED: by signing below I understand that decisions are process on a case-by-case basis and the committee may deny any SAP appeal.”
### `9c777c765fd786f8` Oakwood University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://oakwood.edu/financial-aid/ (sha256 e797915ee4ee)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If there are unusual circumstances, please discuss them with the Oakwood University Financial Aid Staff, and they will determine the best way for you to complete the FAFSA. 12.”
### `8ce0f8f48f7d9b1a` Oakwood University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://oakwood.edu/wp-content/uploads/2025-26-Tution-Fees_Final-as-of-4_24_25.pdf (sha256 3603c09c9eb5)
- issues: arrangement_unlabeled, conflicting_sources:https://my.oakwood.edu/ICS/icsfs/mm/tuition___fees.pdf?target=b13c57fe-7436-485d-891c-61b85c5644de
- checks: {"columns": 2, "rows": 14}
  - column:Tuition Package, Per Semester: 11472 ⟵ “Tuition Package, Per Semester | $11,472”
  - column:Carter Hall - Double Occupancy: 2487 ⟵ “Carter Hall - Double Occupancy | $2,487”
  - column:Carter Hall - Double Occupancy w/Bath: 2672 ⟵ “Carter Hall - Double Occupancy w/Bath | $2,672”
  - column:Holland Hall - Double w/Private Bath (A&D Rooms): 3058 ⟵ “Holland Hall - Double w/Private Bath (A&D Rooms) | $3,058”
  - column:Holland Hall - Double w/Private Bath: 2487 ⟵ “Holland Hall - Double w/Private Bath | $2,487”
  - column:Blue (14-meal plan with 300 Acorn Dollars, 200 Oak Dollars): 2986 ⟵ “Blue (14-meal plan with 300 Acorn Dollars, 200 Oak Dollars) | $2,986”
  - column:Gold (12-Meal Plan with 350 Acorn Dollars, 200 Oak Dollars): 2989 ⟵ “Gold (12-Meal Plan with 350 Acorn Dollars, 200 Oak Dollars) | $2,989”
  - column:Bronze (8-meals with 500 Acorn Dollars, 200 Oak Dollars): 2721 ⟵ “Bronze (8-meals with 500 Acorn Dollars, 200 Oak Dollars) | $2,721”
  - column:*$584: 584 ⟵ “*$584 | *$584”
  - column:Tuition and Fees: 12056 ⟵ “Tuition and Fees | $12,056”
  - column:Food and Housing: 5328 ⟵ “Food and Housing | $5,328”
  - column:Totals: 17384 ⟵ “Totals | $17,384 | 80% = $13,907”
  - column:$34,768 (*includes: 24112 ⟵ “$34,768 (*includes | $24,112 | $24,112”
  - column:$8,752: 12564 ⟵ “$8,752 | $12,564 | $22,360”
  - column:$34,768 (*includes: 24112 ⟵ “$34,768 (*includes | $24,112 | $24,112”
  - column:$8,752: 22360 ⟵ “$8,752 | $12,564 | $22,360”
### `d01593125a2522d4` Oakwood University — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://my.oakwood.edu/ICS/icsfs/mm/tuition___fees.pdf?target=b13c57fe-7436-485d-891c-61b85c5644de (sha256 0b3a4521937a)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://oakwood.edu/wp-content/uploads/2025-26-Tution-Fees_Final-as-of-4_24_25.pdf
- checks: {"columns": 2, "components_reconcile": false, "rows": 5}
  - column:Tuition Package, Per Semester: 9487 ⟵ “Tuition Package, Per Semester | $9,487 * | $9,487”
  - column:Room - Carter - Double Occupancy **: 2346 ⟵ “Room - Carter - Double Occupancy ** | $2,346”
  - column:Room - Carter - Double Occupancy w/Bath **: 2521 ⟵ “Room - Carter - Double Occupancy w/Bath ** | $2,521”
  - column:Holland Hall Double w/Private Bath (A&D Rooms): 2371 ⟵ “Holland Hall Double w/Private Bath (A&D Rooms) | $2,371”
  - column:Holland Hall Double w/Private Bath: 2346 ⟵ “Holland Hall Double w/Private Bath | $2,346 | $2,346”
  - column:Holland Hall Single w/Private Bath: 3086 ⟵ “Holland Hall Single w/Private Bath | $3,086”
  - column:Plan A - Board (14-Meal Plan with 300 Flex Dollars): 2479 ⟵ “Plan A - Board (14-Meal Plan with 300 Flex Dollars) | $2,479”
  - column:Plan B - Board (12-Meal Plan with 350 Flex Dollars): 2474 ⟵ “Plan B - Board (12-Meal Plan with 350 Flex Dollars) | $2,474”
  - column:Plan C - Board (10-Meal Plan with 400 Flex Dollars): 2341 ⟵ “Plan C - Board (10-Meal Plan with 400 Flex Dollars) | $2,341 | $2,341”
  - column:Plan D - Board (8-meals with 500 Flex Dollars): 2234 ⟵ “Plan D - Board (8-meals with 500 Flex Dollars) | $2,234”
  - column:Community Meal Plan (200 Dining Dollars): 200 ⟵ “Community Meal Plan (200 Dining Dollars) | $200”
  - column:General/Matriculation Fee (Per Semester): 508 ⟵ “General/Matriculation Fee (Per Semester) | $508 | $508”
  - column:Total Charges Per Semester: 14682 ⟵ “Total Charges Per Semester | $14,682 | $9995”
  - column:Tuition and Fees: 9995 ⟵ “Tuition and Fees | $9,995”
  - column:Room and Board: 4687 ⟵ “Room and Board | $4,687 *”
  - column:Totals: 14682 ⟵ “Totals | $14,682 | 70% = $10,277”
  - on_campus:Tuition Package, Per Semester: 9487 ⟵ “Tuition Package, Per Semester | $9,487 * | $9,487”
  - on_campus:Holland Hall Double w/Private Bath: 2346 ⟵ “Holland Hall Double w/Private Bath | $2,346 | $2,346”
  - on_campus:Plan C - Board (10-Meal Plan with 400 Flex Dollars): 2341 ⟵ “Plan C - Board (10-Meal Plan with 400 Flex Dollars) | $2,341 | $2,341”
  - on_campus:General/Matriculation Fee (Per Semester): 508 ⟵ “General/Matriculation Fee (Per Semester) | $508 | $508”
  - on_campus:Total Charges Per Semester: 9995 ⟵ “Total Charges Per Semester | $14,682 | $9995”
### `50e144e197447460` Samford University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.samford.edu/departments/files/Financial_Services/2627-Undergrad-COA-Form.pdf (sha256 360bae146f1b)
- issues: multiple_total_rows, conflicting_sources:https://www.samford.edu/admission/tuition-and-fees
- checks: {"columns": 1, "rows": 16}
  - column:TUITION ESTIMATE: 42590 ⟵ “TUITION ESTIMATE | $42,590”
  - column:FEES ESTIMATE: 1200 ⟵ “FEES ESTIMATE | 1,200”
  - column:TOTAL ESTIMATED DIRECT COST: 43790 ⟵ “TOTAL ESTIMATED DIRECT COST | $43,790”
  - column:HOUSING: 9540 ⟵ “HOUSING | $9,540”
  - column:FOOD: 8010 ⟵ “FOOD | 8,010”
  - column:BOOKS AND SUPPLIES: 1320 ⟵ “BOOKS AND SUPPLIES | 1,320”
  - column:TRANSPORTATION: 1584 ⟵ “TRANSPORTATION | 1,584”
  - column:MISCELLANEOUS: 4286 ⟵ “MISCELLANEOUS | 4,286”
  - column:TOTAL INDIRECT COSTS: 24740 ⟵ “TOTAL INDIRECT COSTS | $24,740”
  - column:TOTAL (DIRECT AND INDIRECT COSTS): 68530 ⟵ “TOTAL (DIRECT AND INDIRECT COSTS) | $68,530”
  - column:UG Nursing: 200 ⟵ “UG Nursing | $200”
  - column:UG Accounting: 1171 ⟵ “UG Accounting | $1171”
  - column:UG Interior Design: 345 ⟵ “UG Interior Design | $345”
  - column:UG Education ESEC: 1622 ⟵ “UG Education ESEC | $1622”
  - column:UG Ed. Christian Ministry: 1251 ⟵ “UG Ed. Christian Ministry | $1251”
  - column:UG Secondary Education: 1092 ⟵ “UG Secondary Education | $1092”
  - column:TUITION ESTIMATE: 42590 ⟵ “TUITION ESTIMATE | $42,590”
  - column:FEES ESTIMATE: 1460 ⟵ “FEES ESTIMATE | 1,460”
  - column:TOTAL ESTIMATED DIRECT COST: 44050 ⟵ “TOTAL ESTIMATED DIRECT COST | $44,050”
  - column:HOUSING: 14592 ⟵ “HOUSING | $14,592”
  - column:FOOD: 8010 ⟵ “FOOD | 8,010”
  - column:BOOKS AND SUPPLIES: 1320 ⟵ “BOOKS AND SUPPLIES | 1,320”
  - column:TRANSPORTATION: 2310 ⟵ “TRANSPORTATION | 2,310”
  - column:MISCELLANEOUS: 4286 ⟵ “MISCELLANEOUS | 4,286”
  - column:TOTAL INDIRECT COSTS: 30518 ⟵ “TOTAL INDIRECT COSTS | $30,518”
  - … 32 more rows
### `ef47347eaf19f4f2` Samford University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.samford.edu/admission/tuition-and-fees (sha256 a57f872ac3cc)
- issues: conflicting_sources:https://www.samford.edu/departments/files/Financial_Services/2627-Undergrad-COA-Form.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 42590 ⟵ “Tuition | $42,590”
  - column:Fees: 1200 ⟵ “Fees | $1,200”
  - column:Room (Vail/Smith): 8130 ⟵ “Room (Vail/Smith) | $8,130”
  - column:Board: 7250 ⟵ “Board | $7,250”
  - column:Total: 59170 ⟵ “Total | $59,170”
### `64e587d0528e1a3e` Shelton State Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sheltonstate.edu/wp-content/uploads/2025/12/2026-2027-Institutional-Scholarship-Appeal-Form.pdf (sha256 ca7c079ada82)
- issues: semantic_review_required, conflicting_sources:https://www.sheltonstate.edu/admissions-financial-aid/financial-aid/scholarships/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “INSTITUTIONAL SCHOLARSHIP APPEAL FORM The deadline to submit an institutional scholarship appeal for the 2026-2027 academic year is Friday, May 15, 2026.”
### `92cd96e8136336a1` Shelton State Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.sheltonstate.edu/admissions-financial-aid/financial-aid/scholarships/ (sha256 9f0788a17d56)
- issues: semantic_review_required, conflicting_sources:https://www.sheltonstate.edu/wp-content/uploads/2025/12/2026-2027-Institutional-Scholarship-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “To activate, click here for more information. 2026-2027 Institutional Scholarship Application Information 2026-2027 Institutional Scholarships Summer 2026 Institutional Scholarship Information 2026-2027 Institutional Scholarship Appeal Form How to log into your AwardSpring account: Use Chrome or Firefox as the browser.”
### `bca2e7db56567cbd` Shelton State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.sheltonstate.edu/admissions-financial-aid/financial-aid/financial-aid-definitions/ (sha256 b1fa04c1cea5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeal A formal request to have a committee review your special circumstances that resulted in your financial aid suspension.”
### `6628da76ad9d4ba2` Southern Union State Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.suscc.edu/admissions/financial-aid-forms (sha256 23636b87fd79)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Forms/Links/Professional Judgement - Financial Aid - Southern Union State Community College Skip to content Registration is open for the Fall 2026 Mini Term II.”
  - sentence: professional_judgment ⟵ “Professional Judgement (PJ) When special and involuntary circumstances affect your federal financial aid resources, there may be an option available for income adjustments due to special circumstances.”
  - sentence: professional_judgment ⟵ “Use the PJ Advisor portal to expedite the financial aid professional judgment process.”
  - sentence: professional_judgment ⟵ “PJ Advisor is an accessible, intuitive tool that will guide you through the process to request a professional judgment/appeal.”
### `ceeb4a6381a17d51` Southern Union State Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.suscc.edu/202627-college-catalog-and-student-handbook/foundation-scholarships (sha256 fe9229816d5b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Southern Union Foundation Special Circumstance Scholarship For students facing hardships not covered by traditional financial aid.”
### `1fbcaaa8eeb5b82b` Southern Union State Community College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.suscc.edu/content/userfiles/files/2025-2026%20Cost%20of%20Attendance.pdf (sha256 3a21bd1c3483)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 2, "rows": 9}
  - column:Tuition and Fees (direct cost): 5460.0 ⟵ “Tuition and Fees (direct cost) | 2730.00 | 5460.00 | 8190.00”
  - column:Books and Supplies (direct/indirect cost): 1700.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - column:Housing (indirect cost): 5400.0 ⟵ “Housing (indirect cost) | 2700.00 | 5400.00 | 8100.00”
  - column:Food (indirect cost): 2200.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - column:Transportation (indirect cost): 4000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - column:Miscellaneous (indirect cost): 1800.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - column:Loan Origination Fee (direct cost): 100.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 20660.0 ⟵ “TOTAL | 10330.00 | 20660.00 | 30990.00”
  - column:Tuition and Fees (direct cost): 5460.0 ⟵ “Tuition and Fees (direct cost) | 2730.00 | 5460.00 | 8190.00”
  - column:Books and Supplies (direct/indirect cost): 1700.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - column:Transportation (indirect cost): 4000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - column:Miscellaneous (indirect cost): 1800.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - column:Housing (indirect cost): 5000.0 ⟵ “Housing (indirect cost) | 2500.00 | 5000.00 | 7500.00”
  - column:Food (indirect cost): 2200.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - column:Loan Origination Fee (direct cost): 100.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 20260.0 ⟵ “TOTAL | 10130.00 | 20260.00 | 30390.00”
  - column:Tuition and Fees (direct cost): 5460.0 ⟵ “Tuition and Fees (direct cost) | 2730.00 | 5460.00 | 8190.00”
  - column:Books and Supplies (direct/indirect cost): 1700.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - column:Food (indirect cost): 2200.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - column:Transportation (indirect cost): 4000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - column:Miscellaneous (indirect cost): 1800.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - column:Housing (direct cost): 3800.0 ⟵ “Housing (direct cost) | 1900.00 | 3800.00 | 5700.00”
  - column:Loan Origination Fee (direct cost): 100.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 19060.0 ⟵ “TOTAL | 9530.00 | 19060.00 | 28590.00”
  - column:Tuition and Fees (direct cost): 9390.0 ⟵ “Tuition and Fees (direct cost) | 4695.00 | 9390.00 | 14085.00”
  - … 71 more rows
### `3ab8e336364e20d2` Southern Union State Community College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.suscc.edu/content/userfiles/files/2025-2026%20Cost%20of%20Attendance.pdf (sha256 3a21bd1c3483)
- issues: multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 1, "rows": 9}
  - off_campus_not_with_family:Tuition and Fees (direct cost): 2730.0 ⟵ “Tuition and Fees (direct cost) | 2730.00 | 5460.00 | 8190.00”
  - off_campus_not_with_family:Books and Supplies (direct/indirect cost): 850.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - off_campus_not_with_family:Housing (indirect cost): 2700.0 ⟵ “Housing (indirect cost) | 2700.00 | 5400.00 | 8100.00”
  - off_campus_not_with_family:Food (indirect cost): 1100.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - off_campus_not_with_family:Transportation (indirect cost): 2000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - off_campus_not_with_family:Miscellaneous (indirect cost): 900.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - off_campus_not_with_family:Loan Origination Fee (direct cost): 50.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - off_campus_not_with_family:TOTAL: 10330.0 ⟵ “TOTAL | 10330.00 | 20660.00 | 30990.00”
  - off_campus_not_with_family:Tuition and Fees (direct cost): 2730.0 ⟵ “Tuition and Fees (direct cost) | 2730.00 | 5460.00 | 8190.00”
  - off_campus_not_with_family:Books and Supplies (direct/indirect cost): 850.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - off_campus_not_with_family:Transportation (indirect cost): 2000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - off_campus_not_with_family:Miscellaneous (indirect cost): 900.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - off_campus_not_with_family:Housing (indirect cost): 2500.0 ⟵ “Housing (indirect cost) | 2500.00 | 5000.00 | 7500.00”
  - off_campus_not_with_family:Food (indirect cost): 1100.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - off_campus_not_with_family:Loan Origination Fee (direct cost): 50.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - off_campus_not_with_family:TOTAL: 10130.0 ⟵ “TOTAL | 10130.00 | 20260.00 | 30390.00”
  - off_campus_not_with_family:Tuition and Fees (direct cost): 2730.0 ⟵ “Tuition and Fees (direct cost) | 2730.00 | 5460.00 | 8190.00”
  - off_campus_not_with_family:Books and Supplies (direct/indirect cost): 850.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - off_campus_not_with_family:Food (indirect cost): 1100.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - off_campus_not_with_family:Transportation (indirect cost): 2000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - off_campus_not_with_family:Miscellaneous (indirect cost): 900.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - off_campus_not_with_family:Housing (direct cost): 1900.0 ⟵ “Housing (direct cost) | 1900.00 | 3800.00 | 5700.00”
  - off_campus_not_with_family:Loan Origination Fee (direct cost): 50.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - off_campus_not_with_family:TOTAL: 9530.0 ⟵ “TOTAL | 9530.00 | 19060.00 | 28590.00”
  - off_campus_not_with_family:Tuition and Fees (direct cost): 4695.0 ⟵ “Tuition and Fees (direct cost) | 4695.00 | 9390.00 | 14085.00”
  - … 23 more rows
### `3ff465594f4c2edc` Southern Union State Community College — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.suscc.edu/content/userfiles/files/SUSCC%202324%20COST%20OF%20ATTENDANCE%20.pdf (sha256 352b89e8f549)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2023-24
- checks: {"columns": 3, "rows": 8}
  - column:Tuition and Fees: 2490.0 ⟵ “Tuition and Fees | 2490.00 | 4980.00 | 7470.00”
  - column:Books and Supplies: 775.0 ⟵ “Books and Supplies | 775.00 | 1550.00 | 2325.00”
  - column:Housing: 2700.0 ⟵ “Housing | 2700.00 | 5400.00 | 8100.00”
  - column:Food: 1100.0 ⟵ “Food | 1100.00 | 2200.00 | 3300.00”
  - column:Transportation: 1850.0 ⟵ “Transportation | 1850.00 | 3700.00 | 5550.00”
  - column:Miscellaneous: 900.0 ⟵ “Miscellaneous | 900.00 | 1800.00 | 2700.00”
  - column:Loan Origination Fee: 50.0 ⟵ “Loan Origination Fee | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 9865.0 ⟵ “TOTAL | 9865.00 | 19730.00 | 29595.00”
  - column:Tuition and Fees: 2490.0 ⟵ “Tuition and Fees | 2490.00 | 4980.00 | 7470.00”
  - column:Books and Supplies: 775.0 ⟵ “Books and Supplies | 775.00 | 1550.00 | 2325.00”
  - column:Transportation: 1850.0 ⟵ “Transportation | 1850.00 | 3700.00 | 5550.00”
  - column:Miscellaneous: 900.0 ⟵ “Miscellaneous | 900.00 | 1800.00 | 2700.00”
  - column:Housing: 2500.0 ⟵ “Housing | 2500.00 | 5000.00 | 7500.00”
  - column:Food: 1100.0 ⟵ “Food | 1100.00 | 2200.00 | 3300.00”
  - column:Loan Origination Fee: 50.0 ⟵ “Loan Origination Fee | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 9665.0 ⟵ “TOTAL | 9665.00 | 19330.00 | 28995.00”
  - column:Tuition and Fees: 2490.0 ⟵ “Tuition and Fees | 2490.00 | 4980.00 | 7470.00”
  - column:Books and Supplies: 775.0 ⟵ “Books and Supplies | 775.00 | 1550.00 | 2325.00”
  - column:Food: 2200.0 ⟵ “Food | 2200.00 | 2200.00 | 2200.00”
  - column:Transportation: 1850.0 ⟵ “Transportation | 1850.00 | 3700.00 | 5550.00”
  - column:Miscellaneous: 900.0 ⟵ “Miscellaneous | 900.00 | 1800.00 | 2700.00”
  - column:Housing: 1900.0 ⟵ “Housing | 1900.00 | 3800.00 | 5700.00”
  - column:Loan Origination Fee: 50.0 ⟵ “Loan Origination Fee | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 10165.0 ⟵ “TOTAL | 10165.00 | 18130.00 | 26095.00”
  - column:Tuition and Fees: 4395.0 ⟵ “Tuition and Fees | 4395.00 | 8790.00 | 13185.00”
  - … 119 more rows
### `c544c770f8384a31` Southern Union State Community College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.suscc.edu/content/userfiles/files/2024_2025%20Budgets%20and%20Cost%20of%20Attendance%20-.pdf (sha256 c4932bbe095c)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown, stale_year_label:2024-25
- checks: {"columns": 2, "rows": 9}
  - column:Tuition and Fees (direct cost): 5040.0 ⟵ “Tuition and Fees (direct cost) | 2520.00 | 5040.00 | 7560.00”
  - column:Books and Supplies (direct/indirect cost): 1700.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - column:Housing (indirect cost): 5400.0 ⟵ “Housing (indirect cost) | 2700.00 | 5400.00 | 8100.00”
  - column:Food (indirect cost): 2200.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - column:Transportation (indirect cost): 4000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - column:Miscellaneous (indirect cost): 1800.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - column:Loan Origination Fee (direct cost): 100.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 20240.0 ⟵ “TOTAL | 10120.00 | 20240.00 | 30360.00”
  - column:Tuition and Fees (direct cost): 5040.0 ⟵ “Tuition and Fees (direct cost) | 2520.00 | 5040.00 | 7560.00”
  - column:Books and Supplies (direct/indirect cost): 1700.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - column:Transportation (indirect cost): 4000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - column:Miscellaneous (indirect cost): 1800.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - column:Housing (indirect cost): 5000.0 ⟵ “Housing (indirect cost) | 2500.00 | 5000.00 | 7500.00”
  - column:Food (indirect cost): 2200.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - column:Loan Origination Fee (direct cost): 100.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 19840.0 ⟵ “TOTAL | 9920.00 | 19840.00 | 29760.00”
  - column:Tuition and Fees (direct cost): 5040.0 ⟵ “Tuition and Fees (direct cost) | 2520.00 | 5040.00 | 7560.00”
  - column:Books and Supplies (direct/indirect cost): 1700.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - column:Food (indirect cost): 2200.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - column:Transportation (indirect cost): 4000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - column:Miscellaneous (indirect cost): 1800.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - column:Housing (direct cost): 3800.0 ⟵ “Housing (direct cost) | 1900.00 | 3800.00 | 5700.00”
  - column:Loan Origination Fee (direct cost): 100.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - column:TOTAL: 18640.0 ⟵ “TOTAL | 9320.00 | 18640.00 | 27960.00”
  - column:Tuition and Fees (direct cost): 8850.0 ⟵ “Tuition and Fees (direct cost) | 4425.00 | 8850.00 | 13275.00”
  - … 71 more rows
### `d336ae9129913f3f` Southern Union State Community College — costs 2024-25 · residency=in_state [new] (labeled_in_source)
- source: https://www.suscc.edu/content/userfiles/files/2024_2025%20Budgets%20and%20Cost%20of%20Attendance%20-.pdf (sha256 c4932bbe095c)
- issues: multiple_total_rows, stale_year_label:2024-25
- checks: {"columns": 1, "rows": 9}
  - off_campus_not_with_family:Tuition and Fees (direct cost): 2520.0 ⟵ “Tuition and Fees (direct cost) | 2520.00 | 5040.00 | 7560.00”
  - off_campus_not_with_family:Books and Supplies (direct/indirect cost): 850.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - off_campus_not_with_family:Housing (indirect cost): 2700.0 ⟵ “Housing (indirect cost) | 2700.00 | 5400.00 | 8100.00”
  - off_campus_not_with_family:Food (indirect cost): 1100.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - off_campus_not_with_family:Transportation (indirect cost): 2000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - off_campus_not_with_family:Miscellaneous (indirect cost): 900.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - off_campus_not_with_family:Loan Origination Fee (direct cost): 50.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - off_campus_not_with_family:TOTAL: 10120.0 ⟵ “TOTAL | 10120.00 | 20240.00 | 30360.00”
  - off_campus_not_with_family:Tuition and Fees (direct cost): 2520.0 ⟵ “Tuition and Fees (direct cost) | 2520.00 | 5040.00 | 7560.00”
  - off_campus_not_with_family:Books and Supplies (direct/indirect cost): 850.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - off_campus_not_with_family:Transportation (indirect cost): 2000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - off_campus_not_with_family:Miscellaneous (indirect cost): 900.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - off_campus_not_with_family:Housing (indirect cost): 2500.0 ⟵ “Housing (indirect cost) | 2500.00 | 5000.00 | 7500.00”
  - off_campus_not_with_family:Food (indirect cost): 1100.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - off_campus_not_with_family:Loan Origination Fee (direct cost): 50.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - off_campus_not_with_family:TOTAL: 9920.0 ⟵ “TOTAL | 9920.00 | 19840.00 | 29760.00”
  - off_campus_not_with_family:Tuition and Fees (direct cost): 2520.0 ⟵ “Tuition and Fees (direct cost) | 2520.00 | 5040.00 | 7560.00”
  - off_campus_not_with_family:Books and Supplies (direct/indirect cost): 850.0 ⟵ “Books and Supplies (direct/indirect cost) | 850.00 | 1700.00 | 2550.00”
  - off_campus_not_with_family:Food (indirect cost): 1100.0 ⟵ “Food (indirect cost) | 1100.00 | 2200.00 | 3300.00”
  - off_campus_not_with_family:Transportation (indirect cost): 2000.0 ⟵ “Transportation (indirect cost) | 2000.00 | 4000.00 | 6000.00”
  - off_campus_not_with_family:Miscellaneous (indirect cost): 900.0 ⟵ “Miscellaneous (indirect cost) | 900.00 | 1800.00 | 2700.00”
  - off_campus_not_with_family:Housing (direct cost): 1900.0 ⟵ “Housing (direct cost) | 1900.00 | 3800.00 | 5700.00”
  - off_campus_not_with_family:Loan Origination Fee (direct cost): 50.0 ⟵ “Loan Origination Fee (direct cost) | 50.00 | 100.00 | 150.00”
  - off_campus_not_with_family:TOTAL: 9320.0 ⟵ “TOTAL | 9320.00 | 18640.00 | 27960.00”
  - off_campus_not_with_family:Tuition and Fees (direct cost): 4425.0 ⟵ “Tuition and Fees (direct cost) | 4425.00 | 8850.00 | 13275.00”
  - … 23 more rows
### `6ea688fdca7188f7` Spring Hill College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.shc.edu/admissions-aid/tuition-financial-aid/financial-aid-policies/ (sha256 390d52084e82)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Adequate documentation verifying the special circumstances must be attached (e.g., doctor’s letter, third-party letter).”
### `adcb8eb0fc217d3b` Spring Hill College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.shc.edu/admissions-aid/tuition-financial-aid/financial-aid-policies/ (sha256 390d52084e82)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “SAP Appeal Process—A student has the right to appeal a suspension of financial aid due to mitigating circumstances such as, but not limited to, illness, military service, or a previously undiagnosed learning disability.”
  - sentence: sap_appeal ⟵ “The following must be completed and submitted to the Office of Student Financial Services: Appeals must be submitted to the Financial Aid Office using the Satisfactory Academic Progress Appeal Form (available on BadgerWeb).”
  - sentence: sap_appeal ⟵ “If a student’s SAP Appeal is denied, the student will remain on Financial Aid Suspension until he or she meets the requirements for Satisfactory Academic Progress.”
  - sentence: sap_appeal ⟵ “Students who enroll in classes at SHC and pay for classes without the use of financial aid for at least a semester; and who are able to demonstrate progress toward meeting SAP guidelines can re-appeal and be considered for financial aid.”
### `2e07f0d9a9b7b1ed` Spring Hill College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.shc.edu/wp-content/uploads/2026/09/OLC-2627-COA.pdf (sha256 5bbf4e792bba)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.shc.edu/wp-content/uploads/2026/02/UNDG-COA-2627-Website.pdf
- checks: {"columns": 2, "rows": 8}
  - column:Tuition: 11304.0 ⟵ “Tuition | $ 11,304.00”
  - column:Total Direct Costs: 11304.0 ⟵ “Total Direct Costs | $ 11,304.00”
  - column:Books: 1290.0 ⟵ “Books | $ 1,290.00”
  - column:Transportation: 3220.0 ⟵ “Transportation | $ 3,220.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $ 2,000.00”
  - column:Food and Housing: 17590 ⟵ “Food and Housing | $17,590”
  - column:Total Indirect Costs: 24186.0 ⟵ “Total Indirect Costs | $ 24,186.00”
  - column:Off Campus Cost of Attendance: 35490.0 ⟵ “Off Campus Cost of Attendance | $ 35,490.00”
  - column:Loan Fees: 86.0 ⟵ “Loan Fees | $ | 86.00”
### `4747114c05c052d3` Spring Hill College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.shc.edu/wp-content/uploads/2026/02/UNDG-COA-2627-Website.pdf (sha256 53c1521ac579)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.shc.edu/wp-content/uploads/2026/09/OLC-2627-COA.pdf
- checks: {"columns": 2, "rows": 10}
  - column:Tuition: 26482.0 ⟵ “Tuition | $ 26,482.00”
  - column:Housing and Food: 14960.0 ⟵ “Housing and Food | $ 14,960.00”
  - column:Total Direct Costs: 41992.0 ⟵ “Total Direct Costs | $ 41,992.00”
  - column:On Campus Cost of Attendance: 48732.0 ⟵ “On Campus Cost of Attendance | $48,732.00”
  - column:Tuition: 26482.0 ⟵ “Tuition | $ 26,482.00”
  - column:Total Direct Costs: 27032.0 ⟵ “Total Direct Costs | $ 27,032.00”
  - column:Books: 1290.0 ⟵ “Books | $ 1,290.00”
  - column:Transportation: 3220.0 ⟵ “Transportation | $ 3,220.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $ 2,000.00”
  - column:Housing and Food: 5770.0 ⟵ “Housing and Food | $ 5,770.00”
  - column:Total Indirect Costs: 12510.0 ⟵ “Total Indirect Costs | $ 12,510.00”
  - column:With Parent Cost of Attendance: 39542.0 ⟵ “With Parent Cost of Attendance | $39,542.00”
  - column:Tuition: 26482.0 ⟵ “Tuition | $ 26,482.00”
  - column:Total Direct Costs: 27032.0 ⟵ “Total Direct Costs | $ 27,032.00”
  - column:Transportation: 3220.0 ⟵ “Transportation | $ 3,220.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $ 2,000.00”
  - column:Housing and Food: 17590.0 ⟵ “Housing and Food | $ 17,590.00”
  - column:Total Indirect Costs: 24330.0 ⟵ “Total Indirect Costs | $ 24,330.00”
  - column:Off Campus Cost of Attendance: 51362.0 ⟵ “Off Campus Cost of Attendance | $ 51,362.00”
  - column:Fee Estimate: 550.0 ⟵ “Fee Estimate | $ | 550.00”
  - column:Books: 1290.0 ⟵ “Books | $ | 1,290.00”
  - column:Loan Fees: 230.0 ⟵ “Loan Fees | $ | 230.00”
  - column:Transportation: 3220.0 ⟵ “Transportation | $ | 3,220.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $ | 2,000.00”
  - column:Total Indirect Costs: 6740.0 ⟵ “Total Indirect Costs | $ | 6,740.00”
  - … 4 more rows
### `0b35686768708e17` Stillman College — appeals 2025-26 [new] (labeled_in_source)
- source: https://stillman.edu/financial-aid/ (sha256 58586ce3fd29)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Tuscaloosa, AL 35401 Office Hours: Monday – Friday 8:00am – 5:00pm Contact: Phone: 205-366-8817 Option 4 Email: financialaid@stillman.edu Office of Financial Aid How To Apply Types of Aid Grants Work Loans Disbursement of Financial Aid Funds Student Rights Things to Know About Your Award Cost of Attendance Dependency Overrides.”
### `32ec71e2cdc83156` Stillman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://stillman.edu/financial-aid/sap/ (sha256 0ec4e49c3238)
- issues: semantic_review_required, conflicting_sources:https://catalog.stillman.edu/office-of-financial-aid-satisfactory-academic-progress-and-conditions-of-financial-aid,https://stillman.edu/financial-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “However, if there were special circumstances involved SC may be able to approve an SAP appeal and place the student on Financial Aid Probation.”
  - sentence: sap_appeal ⟵ “Appeal of Financial Aid Suspension The SAP appeal must address the following: 1) the extenuating circumstances that prevented the student from meeting the Satisfactory Academic Progress (SAP) standards, 2) plan of action to resolve or control the cause for the circumstance or unit-deficiency and explain how it will not cause problems in the future.”
  - sentence: sap_appeal ⟵ “The SAP appeal must be submitted by the deadline date of the semester in which the student plans to attend.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will review appeals at the end of the semester after grades are posted.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will notify the students of the committee’s decision via campus email.”
### `33d6a7bf52f4f418` Stillman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://stillman.edu/financial-aid/sap/ (sha256 e3d95c008558)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Tuscaloosa, AL 35401 Office Hours: Monday – Friday 8:00am – 5:00pm Contact: Phone: (205) 366-8817 Ext. 4 Email: financialaid@stillman.edu Office of Financial Aid How To Apply Types of Aid Grants Work Loans Disbursement of Financial Aid Funds Student Rights Things to Know About Your Award Cost of Attendance Dependency Overrides.”
### `cfb1301e07f4bf47` Stillman College — appeals 2025-26 [new] (labeled_in_source)
- source: https://stillman.edu/financial-aid/ (sha256 58586ce3fd29)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: merit_reconsideration ⟵ “When you submit any documents to the office, please make sure that your name and student ID number is include on all documents. 4 – Review your Award Offer When our office completes the file review, an award offer is made.”
### `e7c98df45809f748` Stillman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://catalog.stillman.edu/office-of-financial-aid-satisfactory-academic-progress-and-conditions-of-financial-aid (sha256 664c65c72b98)
- issues: semantic_review_required, conflicting_sources:https://stillman.edu/financial-aid/sap/,https://stillman.edu/financial-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “However, if there were special circumstances involved, SC may approve an SAP appeal and place the student on Financial Aid Probation.”
  - sentence: sap_appeal ⟵ “The SAP appeal must be submitted by the semester's deadline date in which the student plans to attend.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will review appeals at the end of the semester after grades are posted.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will notify the student of the committee's decision via campus email.”
### `f65ea6b3c43e95bc` Stillman College — appeals 2026-27 [new] (source_unlabeled)
- source: https://stillman.edu/financial-aid/sap/ (sha256 e3d95c008558)
- issues: semantic_review_required, conflicting_sources:https://catalog.stillman.edu/office-of-financial-aid-satisfactory-academic-progress-and-conditions-of-financial-aid,https://stillman.edu/financial-aid/sap/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: sap_appeal ⟵ “However, if there were special circumstances involved SC may be able to approve an SAP appeal and place the student on Financial Aid Probation.”
  - sentence: sap_appeal ⟵ “Appeal of Financial Aid Suspension The SAP appeal must address the following: 1) the extenuating circumstances that prevented the student from meeting the Satisfactory Academic Progress (SAP) standards, 2) plan of action to resolve or control the cause for the circumstance or unit-deficiency and explain how it will not cause problems in the future.”
  - sentence: sap_appeal ⟵ “The SAP appeal must be submitted by the deadline date of the semester in which the student plans to attend.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will review appeals at the end of the semester after grades are posted.”
  - sentence: sap_appeal ⟵ “The SAP Appeals Committee will notify the students of the committee’s decision via campus email.”
### `f81dc76ff519b3b8` Stillman College — appeals 2025-26 [new] (labeled_in_source)
- source: https://stillman.edu/financial-aid/ (sha256 58586ce3fd29)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Deadlines The deadlines to apply for financial aid assistance are: | Semester | Priority Deadline to Apply | Priority Deadline to Submit Documents | SAP Appeal | Summer 2025 | May 1, 2025 | May 10, 2025 | May 24, 2025 | Fall 2025 | June 1, 2025 | July 31, 2025 | August 20, 2025 | Spring 2026 | December 1, 2025 | December 10, 2025 | January 14, 2026 Completing the FAFSA and or submitting documents ”
### `52c3422abc2261df` Stillman College — awards 2024-25 [new] (labeled_in_source)
- source: https://stillman.edu/financial-aid-office/scholarships/ (sha256 707a58e24adc)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 a year* ⟵ “Transfer Scholarship | Up to $1,000 a year* | 3.0 GPA or higher”
  - gpa_requirement: 3.0 GPA or higher ⟵ “Transfer Scholarship | Up to $1,000 a year* | 3.0 GPA or higher”
### `c5efc040da83ced2` Stillman College — awards 2024-25 [new] (labeled_in_source)
- source: https://stillman.edu/financial-aid-office/scholarships/ (sha256 90b1bf6d5acc)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: Up to $6,000 a year* ⟵ “Eye of the Tiger | Up to $6,000 a year* | 3.5 GPA or higher”
  - gpa_requirement: 3.5 GPA or higher ⟵ “Eye of the Tiger | Up to $6,000 a year* | 3.5 GPA or higher”
### `dee701aba0b15bba` Stillman College — awards 2024-25 [new] (labeled_in_source)
- source: https://stillman.edu/financial-aid-office/scholarships/ (sha256 707a58e24adc)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: Up to $10,000 a year* ⟵ “Presidential Scholarship | Up to $10,000 a year* | 3.8 GPA or higher”
  - gpa_requirement: 3.8 GPA or higher ⟵ “Presidential Scholarship | Up to $10,000 a year* | 3.8 GPA or higher”
### `fe737f68ae2833fa` Stillman College — awards 2024-25 [new] (labeled_in_source)
- source: https://stillman.edu/financial-aid-office/scholarships/ (sha256 90b1bf6d5acc)
- issues: stale_year_label:2024-25
- checks: {"thresholds": null}
  - award_amount_text: Up to $4,000 a year* ⟵ “Blue Elite | Up to $4,000 a year* | 3.0 GPA or higher”
  - gpa_requirement: 3.0 GPA or higher ⟵ “Blue Elite | Up to $4,000 a year* | 3.0 GPA or higher”
### `1b6f8f8a6748ba79` Stillman College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://catalog.stillman.edu/basic-charges (sha256 b406337812f7)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 8}
  - column:Tuition*: 10536.0 ⟵ “Tuition* | $5,268.00 | $10,536.00”
  - column:Mandatory Fees+: 2164.0 ⟵ “Mandatory Fees+ | $1,082.00 | $2,164.00”
  - column:Knox Hall: 3190.0 ⟵ “Knox Hall | $1,595.00 | $3,190.00”
  - column:Off Campus LeasedHousing: 5984.0 ⟵ “Off Campus LeasedHousing | $2,992.00 | $5,984.00”
  - column:Meals***: 4916.0 ⟵ “Meals*** | $2,458.00 | $4,916.00”
  - column:Total Basic Charges** (on highest housing option): 23600.0 ⟵ “Total Basic Charges** (on highest housing option) | $ 11,800.00 | $23,600.00”
  - column:Tax on Meals: 400.0 ⟵ “Tax on Meals | $ 200.00 | $ 400.00”
  - column:Grand Total: 24000.0 ⟵ “Grand Total | $ 12,000.00 | $24,000.00”
### `200aa20e07bbb7ec` Stillman College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://stillman.edu/about-us/administration-finance/business-office/online-degrees-tuition-and-fees/ (sha256 3ca3a8b8ee1d)
- issues: stale_year_label:2025-26, conflicting_sources:https://stillman.edu/about-us/administration-finance/business-office/traditional-tuition-and-fees/,https://stillman.edu/financial-aid/financial-aid-things-to-know/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition (12 hours):: 7008.0 ⟵ “Tuition (12 hours): | $3,336.00 | $6,672.00 | $3,504.00 | $7,008.00”
  - column:Mandatory Fees:: 942.0 ⟵ “Mandatory Fees: | $433.00 | $866.00 | $471.00 | $942.00”
  - column:Total: 7950.0 ⟵ “Total | $3,769.00 | $7,538.00 | $3,975.00 | $7,950.00”
### `4fbaec4bbdfa850f` Stillman College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://stillman.edu/about-us/administration-finance/business-office/traditional-tuition-and-fees/ (sha256 a3f62019f852)
- issues: stale_year_label:2025-26, conflicting_sources:https://stillman.edu/about-us/administration-finance/business-office/online-degrees-tuition-and-fees/,https://stillman.edu/financial-aid/financial-aid-things-to-know/
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition (12-18 hours):: 10536.0 ⟵ “Tuition (12-18 hours): | $ 5,013.00 | $ 10,026.00 | $5,268.00 | $10,536.00”
  - column:Mandatory Fees:: 2164.0 ⟵ “Mandatory Fees: | $ 1050.00 | $ 2,100.00 | $1,082.00 | $2,164.00”
  - column:Full Meal Plan:**: 4916.0 ⟵ “Full Meal Plan:** | $ 2,458.00 | $ 4,916.00 | $2,458.00 | $ 4,916.00”
  - column:Single Room:: 5984.0 ⟵ “Single Room: | $ 2,992.00 | $ 5,984.00 | $ 2,992.00 | $5,984.00”
  - column:TOTAL:: 23600.0 ⟵ “TOTAL: | $ 11,511.00 | $ 23,022.00 | $11,800.00 | $23,600.00”
### `bf318db85704fc8a` Stillman College — costs 2024-25 · residency=not_applicable [new] (labeled_in_source)
- source: https://stillman.edu/about-us/administration-finance/business-office/traditional-tuition-and-fees/ (sha256 a3f62019f852)
- issues: components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - column:Tuition (12-18 hours):: 10026.0 ⟵ “Tuition (12-18 hours): | $ 5,013.00 | $ 10,026.00 | $5,268.00 | $10,536.00”
  - column:Mandatory Fees:: 2100.0 ⟵ “Mandatory Fees: | $ 1050.00 | $ 2,100.00 | $1,082.00 | $2,164.00”
  - column:Full Meal Plan:**: 4916.0 ⟵ “Full Meal Plan:** | $ 2,458.00 | $ 4,916.00 | $2,458.00 | $ 4,916.00”
  - column:Single Room:: 5984.0 ⟵ “Single Room: | $ 2,992.00 | $ 5,984.00 | $ 2,992.00 | $5,984.00”
  - column:TOTAL:: 23022.0 ⟵ “TOTAL: | $ 11,511.00 | $ 23,022.00 | $11,800.00 | $23,600.00”
### `dbc769c925f84477` Stillman College — costs 2023-24 · residency=not_applicable [new] (labeled_in_source)
- source: https://stillman.edu/about-us/administration-finance/business-office/online-degrees-tuition-and-fees/ (sha256 3ca3a8b8ee1d)
- issues: stale_year_label:2023-24
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition (12 hours):: 6672.0 ⟵ “Tuition (12 hours): | $3,336.00 | $6,672.00 | $3,504.00 | $7,008.00”
  - column:Mandatory Fees:: 866.0 ⟵ “Mandatory Fees: | $433.00 | $866.00 | $471.00 | $942.00”
  - column:Total: 7538.0 ⟵ “Total | $3,769.00 | $7,538.00 | $3,975.00 | $7,950.00”
### `e22558e3fe7b21b0` Stillman College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://stillman.edu/financial-aid/financial-aid-things-to-know/ (sha256 44cf73b48cd2)
- issues: components_do_not_reconcile, stale_year_label:2025-26, conflicting_sources:https://stillman.edu/about-us/administration-finance/business-office/online-degrees-tuition-and-fees/,https://stillman.edu/about-us/administration-finance/business-office/traditional-tuition-and-fees/
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - column:Tuition: 10536 ⟵ “Tuition | $5,268 | $10,536”
  - column:Fees: 2164 ⟵ “Fees | $1,082 | $ 2,164”
  - column:Expected Room and BoardFull Meal Plan:: 3404 ⟵ “Expected Room and BoardFull Meal Plan: | $1,702 | $3,404”
  - column:Expected Transportation: 2332 ⟵ “Expected Transportation | $1,166 | $ 2,332”
  - column:Expected Books and Supplies: 1000 ⟵ “Expected Books and Supplies | $500 | $1,000”
  - column:Expected Personal Expenses: 1854 ⟵ “Expected Personal Expenses | $927 | $1,854”
  - column:TOTAL: 27398 ⟵ “TOTAL | $13,699 | $27,398”
### `0b74d2f6ef7bd4eb` Stillman College — credit_policies 2021-22 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://stillman.edu/dual-enrollment-program/ (sha256 d31226e8ca08)
- issues: stale_year_label:2021-22
- checks: {"fields": ["per_credit_hour_charges"], "tiers": 0}
  - per_credit_hour_charge: 33 ⟵ “Only $33 per credit hour.”
### `7ca762ac25a137ad` Stillman College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://catalog.stillman.edu/advanced-placement-ap (sha256 ada47fa3faae)
- issues: rows_without_score
- checks: {"distinct_exams": 5, "equivalencies": 5, "rows_without_score": 5}
  - equivalencies[AP-BIOLOGY|None]:  ⟵ “Biology | BIO 141-142 | 8”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “American History | HIS 132 | 3”
  - equivalencies[AP-CHEMISTRY|None]:  ⟵ “Chemistry | CHM 141-142 | 8”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “French I & II | FRN 131-132 | 6”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|None]:  ⟵ “Spanish I & II | SPN 131-132 | 6”
### `80c9d7b44d9957a2` Talladega College — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.talladega.edu/sap-policy/ (sha256 a728f4b78fd4)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “You have not completed between 36 and 60 of the credits you have attempted. “SAP SUSPENSION” If you do not meet the SAP standards after the period of “SAP WARNING” you will be placed on “SAP SUSPENSION” and denied financial aid for future semesters until you meet the College’s SAP standards or submit a “SAP APPEAL”.”
  - sentence: sap_appeal ⟵ “With a “SAP APPEAL” you will complete a form and attach to the form a letter, along with support documentation, that supports and clarifies what caused you to do poorly academically; and what has changed in your life that will now allow you to meet the academic standards.”
  - sentence: sap_appeal ⟵ “In addition, the “SAP APPEAL” form must also include a S.T.A.R (Students Targeted to Achieve Retention) Plan for future academic success.”
  - sentence: sap_appeal ⟵ “If your “SAP APPEAL” is approved, you will be placed on “SAP Probation”.”
  - sentence: sap_appeal ⟵ “If your “SAP APPEAL” is denied, you will not be eligible to receive financial aid; and you cannot submit another appeal.”
  - sentence: sap_appeal ⟵ “This status will continue until you become compliant with the Financial Aid SAP requirements or have an approved Financial Aid SAP Suspension Appeal.”
### `bb4d26d4fe6dde55` Talladega College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.talladega.edu/financial-aid/ (sha256 d0d8d6714eb2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Professional Judgement Policy Students who have completed a FAFSA application and all of its requirements may pursue an adjustment based on special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “This adjustment or review request is called a Professional Judgement Review.”
  - sentence: professional_judgment ⟵ “Through a Professional Judgement Review, the Office of Financial Aid will consider a special or unusual circumstance based on the information provided by the student via an interview with the student and the documentation presented by the student.”
### `1832baebd3374f00` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/oos-international-freshman/ (sha256 1385795d7cc0)
- issues: conflicting_sources:https://afford.ua.edu/scholarships/in-state-freshman/
- checks: {"thresholds": {"act_min": 27, "gpa_min": 3.5}}
  - award_amount_text: $8,000 ⟵ “Capstone | 27 | 1260–1290 | 3.50+ | $8,000”
  - gpa_requirement: 3.50+ ⟵ “Capstone | 27 | 1260–1290 | 3.50+ | $8,000”
  - test_requirement: ACT 27 / SAT 1260–1290 ⟵ “Capstone | 27 | 1260–1290 | 3.50+ | $8,000”
### `1fe14e990cc68595` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/oos-international-freshman/ (sha256 1385795d7cc0)
- issues: conflicting_sources:https://afford.ua.edu/scholarships/in-state-freshman/
- checks: {"thresholds": {"act_min": 28, "gpa_min": 3.5}}
  - award_amount_text: $10,000 ⟵ “Collegiate | 28 | 1300–1320 | 3.50+ | $10,000”
  - gpa_requirement: 3.50+ ⟵ “Collegiate | 28 | 1300–1320 | 3.50+ | $10,000”
  - test_requirement: ACT 28 / SAT 1300–1320 ⟵ “Collegiate | 28 | 1300–1320 | 3.50+ | $10,000”
### `4d229fdf78543be0` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/in-state-freshman/ (sha256 9d9f4037265c)
- issues: conflicting_sources:https://afford.ua.edu/scholarships/oos-international-freshman/
- checks: {"thresholds": {"act_min": 29}}
  - award_amount_text: $8,000 ⟵ “Collegiate | 29 | 1330–1350 | 3.00–3.49 | $8,000”
  - gpa_requirement: 3.00–3.49 ⟵ “Collegiate | 29 | 1330–1350 | 3.00–3.49 | $8,000”
  - test_requirement: ACT 29 / SAT 1330–1350 ⟵ “Collegiate | 29 | 1330–1350 | 3.00–3.49 | $8,000”
### `b1daa98e7ff874c8` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/oos-international-freshman/ (sha256 1385795d7cc0)
- issues: conflicting_sources:https://afford.ua.edu/scholarships/in-state-freshman/
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $28,000 ⟵ “Presidential | 32–36 | 1420–1600 | 3.50+ | $28,000”
  - gpa_requirement: 3.50+ ⟵ “Presidential | 32–36 | 1420–1600 | 3.50+ | $28,000”
  - test_requirement: ACT 32–36 / SAT 1420–1600 ⟵ “Presidential | 32–36 | 1420–1600 | 3.50+ | $28,000”
### `bf8273edc8abc0db` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/oos-international-freshman/ (sha256 1385795d7cc0)
- issues: conflicting_sources:https://afford.ua.edu/scholarships/in-state-freshman/
- checks: {"thresholds": {"act_min": 29, "gpa_min": 3.5}}
  - award_amount_text: $15,000 ⟵ “Foundation in Excellence | 29 | 1330–1350 | 3.50+ | $15,000”
  - gpa_requirement: 3.50+ ⟵ “Foundation in Excellence | 29 | 1330–1350 | 3.50+ | $15,000”
  - test_requirement: ACT 29 / SAT 1330–1350 ⟵ “Foundation in Excellence | 29 | 1330–1350 | 3.50+ | $15,000”
### `cc6248581777b649` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/in-state-freshman/ (sha256 9d9f4037265c)
- issues: conflicting_sources:https://afford.ua.edu/scholarships/oos-international-freshman/
- checks: {"thresholds": {"act_min": 28}}
  - award_amount_text: $7,000 ⟵ “Capstone | 28 | 1300–1320 | 3.00–3.49 | $7,000”
  - gpa_requirement: 3.00–3.49 ⟵ “Capstone | 28 | 1300–1320 | 3.00–3.49 | $7,000”
  - test_requirement: ACT 28 / SAT 1300–1320 ⟵ “Capstone | 28 | 1300–1320 | 3.00–3.49 | $7,000”
### `ea823a024305acea` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/in-state-freshman/ (sha256 9d9f4037265c)
- issues: conflicting_sources:https://afford.ua.edu/scholarships/oos-international-freshman/
- checks: {"thresholds": null}
  - award_amount_text: $9,000 ⟵ “Foundation in Excellence | 30–36 | 1360–1600 | 3.00–3.49 | $9,000”
  - gpa_requirement: 3.00–3.49 ⟵ “Foundation in Excellence | 30–36 | 1360–1600 | 3.00–3.49 | $9,000”
  - test_requirement: ACT 30–36 / SAT 1360–1600 ⟵ “Foundation in Excellence | 30–36 | 1360–1600 | 3.00–3.49 | $9,000”
### `f7d14208f3fdfab8` The University of Alabama — awards 2026-27 [new] (source_unlabeled)
- source: https://afford.ua.edu/scholarships/in-state-freshman/ (sha256 9d9f4037265c)
- issues: conflicting_sources:https://afford.ua.edu/scholarships/oos-international-freshman/
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: Tuition ⟵ “Presidential | 30–36 | 1360–1600 | 3.50+ | Tuition”
  - gpa_requirement: 3.50+ ⟵ “Presidential | 30–36 | 1360–1600 | 3.50+ | Tuition”
  - test_requirement: ACT 30–36 / SAT 1360–1600 ⟵ “Presidential | 30–36 | 1360–1600 | 3.50+ | Tuition”
### `742fb04069af0f8c` Troy University — appeals 2026-27 [new] (source_unlabeled)
- source: https://fa.troy.edu/satisfactory-academic-progress-requirements.html (sha256 f1f57a448e1c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeal Form Troy University, Troy, AL 36082 1.800.414.5756 Resources Emergency Information Student Complaints Feedback Form Student Disability Services Employment Net Price Calculator Social Media Strategic Plan Copyright Accreditation Statement Read Our Disclaimer A-Z Sitemap Transcripts State Authorization © 1996-2026 Troy University T R O Y Privacy Policy Accessibility Standards Title IX × ”
### `d07cc273647b3da0` Troy University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.troy.edu/scholarships-costs-aid/costs/index.html (sha256 b7174efdef0f)
- issues: residency_unknown
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition: 9168 ⟵ “Tuition | $9,168 | $9,168 | $9,168”
  - on_campus:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - on_campus:Housing & Food: 10812 ⟵ “Housing & Food | $10,812 | $10,880 | $5,450”
  - on_campus:Fees*: 2400 ⟵ “Fees* | $2,400 | $2,400 | $2,400”
  - on_campus:Transportation: 1000 ⟵ “Transportation | $1,000 | $2,300 | $2,300”
  - on_campus:Miscellaneous: 3530 ⟵ “Miscellaneous | $3,530 | $3,530 | $3,530”
  - on_campus:Total: 27910 ⟵ “Total | $27,910 | $29,278 | $23,848”
  - off_campus_not_with_family:Tuition: 9168 ⟵ “Tuition | $9,168 | $9,168 | $9,168”
  - off_campus_not_with_family:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - off_campus_not_with_family:Housing & Food: 10880 ⟵ “Housing & Food | $10,812 | $10,880 | $5,450”
  - off_campus_not_with_family:Fees*: 2400 ⟵ “Fees* | $2,400 | $2,400 | $2,400”
  - off_campus_not_with_family:Transportation: 2300 ⟵ “Transportation | $1,000 | $2,300 | $2,300”
  - off_campus_not_with_family:Miscellaneous: 3530 ⟵ “Miscellaneous | $3,530 | $3,530 | $3,530”
  - off_campus_not_with_family:Total: 29278 ⟵ “Total | $27,910 | $29,278 | $23,848”
  - with_parents_or_family:Tuition: 9168 ⟵ “Tuition | $9,168 | $9,168 | $9,168”
  - with_parents_or_family:Books & Supplies: 1000 ⟵ “Books & Supplies | $1,000 | $1,000 | $1,000”
  - with_parents_or_family:Housing & Food: 5450 ⟵ “Housing & Food | $10,812 | $10,880 | $5,450”
  - with_parents_or_family:Fees*: 2400 ⟵ “Fees* | $2,400 | $2,400 | $2,400”
  - with_parents_or_family:Transportation: 2300 ⟵ “Transportation | $1,000 | $2,300 | $2,300”
  - with_parents_or_family:Miscellaneous: 3530 ⟵ “Miscellaneous | $3,530 | $3,530 | $3,530”
  - with_parents_or_family:Total: 23848 ⟵ “Total | $27,910 | $29,278 | $23,848”
### `bc4887044e397a08` Tuskegee University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tuskegee.edu/financial-aid/ShomariFosterScholarshipApplication-v_10_2024.pdf (sha256 1f143483f773)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “List special circumstances or other areas you would like to share with the Scholarship Committee. (Attach additional document if necessary).”
### `40e95d1d77275251` University of Alabama at Birmingham — appeals 2024-25 [new] (labeled_in_title)
- source: https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-Transfer-Scholarship-Polcies.pdf (sha256 f78a741d5603)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-Freshman-Scholarship-Policies.pdf,https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-International-Scholarship-Policies.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “If you are not able to enroll at UAB due to an  tudent is a degree-seeking graduate or professional S Education Abroad program, internship, co-op, military student who is enrolled full-time in graduate (9 or more service, or other extenuating circumstance(s), then you UAB graduate credit hours) or professional coursework. must submit a scholarship appeal form, requesting an exception to the renew”
  - sentence: scholarship_retention_appeal ⟵ “If you The Scholarship Appeal Form for Undergraduate Students is available on the Links/Forms tab in BlazerNET.”
### `62c5c02609a8f894` University of Alabama at Birmingham — appeals 2024-25 [new] (labeled_in_title)
- source: https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-Freshman-Scholarship-Policies.pdf (sha256 99d6dd48e9ea)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-International-Scholarship-Policies.pdf,https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-Transfer-Scholarship-Polcies.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “The Scholarship Appeal Form for Undergraduate Students is available on the Links/Forms tab in BlazerNET.”
  - sentence: scholarship_retention_appeal ⟵ “If tuition charges are of your allotments to that term, then you completely removed, then the semester’s may submit a scholarship appeal form. allotment will be completely recovered.”
### `6467c0c17530de52` University of Alabama at Birmingham — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.uab.edu/cost-aid/images/documents/scholarships/2026-2027-Scholarship-Policies.pdf (sha256 2e7bc5e7faea)
- issues: semantic_review_required, conflicting_sources:https://www.uab.edu/cost-aid/types-of-aid/scholarships/current-student-scholarships
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “If you earn 24 UAB credit hours with the help of developmental coursework and receive a cancellation notification, then you must contact the Office of Undergraduate Scholarships at scholarships@uab.edu and request an individual grade review. • Scholarship Appeal Form: Available on the Links/Forms tab in BlazerNET • A  ppeal Deadline: 2 weeks before classes begin for each semester an exception is ”
  - sentence: scholarship_retention_appeal ⟵ “If, however, you completely credit hours) and would like to move one submit an appeal on their behalf. withdraw from all courses and a portion of of your allotments to that term, then you Visit uab.edu/mycounselor to find your tuition is refunded for the semester, may submit a scholarship appeal form. your assigned Admissions Counselor. then your scholarship amount may be The submission deadline i”
### `922aeed18ae3f4fb` University of Alabama at Birmingham — appeals 2024-25 [new] (labeled_in_title)
- source: https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-International-Scholarship-Policies.pdf (sha256 6c188445f913)
- issues: stale_year_label:2024-25, semantic_review_required, conflicting_sources:https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-Freshman-Scholarship-Policies.pdf,https://www.uab.edu/cost-aid/images/documents/scholarships/24-25-Transfer-Scholarship-Polcies.pdf
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “The submission during the summer semester (12 or more UAB credit hours) deadline is 2 weeks before classes begin for each semester and would like to move one of your allotments to that the exception is requested. term, then you may submit a scholarship appeal form.”
  - sentence: scholarship_retention_appeal ⟵ “If you are not able to enroll at UAB due to an  tudent is a degree-seeking graduate or professional S Education Abroad program, internship, co-op, military student who is enrolled full-time in graduate (9 or more service, or other extenuating circumstance(s), then you UAB graduate credit hours) or professional coursework. must submit a scholarship appeal form, requesting an exception to the renew”
  - sentence: scholarship_retention_appeal ⟵ “If you choose not to The Scholarship Appeal Form for Undergraduate Students is available on the Links/Forms tab in BlazerNET.”
### `d602c7f17698dcaa` University of Alabama at Birmingham — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.uab.edu/cost-aid/types-of-aid/scholarships/current-student-scholarships (sha256 f1c5a31faef6)
- issues: semantic_review_required, conflicting_sources:https://www.uab.edu/cost-aid/images/documents/scholarships/2026-2027-Scholarship-Policies.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “To find the Scholarship Appeal Form for Undergraduates Students, log in to BlazerNET.”
  - sentence: scholarship_retention_appeal ⟵ “The Scholarship Appeal Form for Undergraduate Students is available on the Links/Forms tab in BlazerNET.”
### `e05bc6667d909fd5` University of Alabama at Birmingham — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/cost-aid/images/documents/scholarships/2027-2028-Scholarship-Policies.pdf (sha256 6aa63c299b81)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “Please note: Your enrollment status S pring offers for transfer and international scholarships only: will be reviewed after the drop/add period ends for your first January 1 semester of award, and cancellations will be made at that time. S ummer offers for transfer scholarships only: May 1 Students should check their UAB email regularly for scholarship notifications, reminders, renewal informati”
  - sentence: scholarship_retention_appeal ⟵ “SCHOLARSHIP APPEAL FORM: COMMON APPEAL REASONS F  or currently enrolled UAB students, the form is available on M  edical hardship or injury the Links/Forms tab in BlazerNET.”
  - sentence: scholarship_retention_appeal ⟵ “Academic C  urrently enrolled UAB students must in UAB coursework and have an approved Common Market information is available at submit the scholarship appeal form in consortium agreement on file, confirming uab.edu/commonmarket.”
### `ea91bff8433078ab` University of Alabama at Birmingham — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.uab.edu/cost-aid/images/documents/scholarships/25-26-Scholarship-Policies.pdf (sha256 9a86ad3e9011)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “If you earn 24 UAB credit hours with the help of developmental coursework and receive a cancellation notification, then you must contact the Office of Undergraduate Scholarships at scholarships@uab.edu and request an individual grade review. • Scholarship Appeal Form: Available on the Links/Forms tab in BlazerNET • A  ppeal Deadline: 2 weeks before classes begin for each semester an exception is ”
  - sentence: scholarship_retention_appeal ⟵ “If, however, you completely credit hours) and would like to move one submit an appeal on their behalf. withdraw from all courses and a portion of of your allotments to that term, then you Visit uab.edu/mycounselor to find your tuition is refunded for the semester, may submit a scholarship appeal form. your assigned Admissions Counselor. then your scholarship amount may be The submission deadline i”
### `02f8522a79f56d72` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/in-state-students (sha256 23475fbf7374)
- issues: conflicting_sources:https://www.uab.edu/admissions/cost/scholarships/out-of-state-students
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $12,000 ⟵ “Presidential Scholarship | 30-36 ACT or 1360-1600 SAT | 3.5 or higher | $12,000”
  - gpa_requirement: 3.5 or higher ⟵ “Presidential Scholarship | 30-36 ACT or 1360-1600 SAT | 3.5 or higher | $12,000”
### `0656d46760f1e30a` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/out-of-state-students (sha256 483162e97b7b)
- issues: conflicting_sources:https://www.uab.edu/admissions/cost/scholarships/in-state-students
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $17,500 ⟵ “Provost Scholarship | 27-31 ACT or 1260-1410 SAT | 3.5 or higher | $17,500”
  - gpa_requirement: 3.5 or higher ⟵ “Provost Scholarship | 27-31 ACT or 1260-1410 SAT | 3.5 or higher | $17,500”
### `5266114a2cb125fc` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/out-of-state-students (sha256 483162e97b7b)
- issues: conflicting_sources:https://www.uab.edu/admissions/cost/scholarships/in-state-students
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $9,500 ⟵ “Green & Gold Scholarship | 24-26 ACT or 1160-1250 SAT | 3.5 or higher | $9,500”
  - gpa_requirement: 3.5 or higher ⟵ “Green & Gold Scholarship | 24-26 ACT or 1160-1250 SAT | 3.5 or higher | $9,500”
### `b0a3ea922ae7ec54` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/out-of-state-students (sha256 483162e97b7b)
- issues: conflicting_sources:https://www.uab.edu/admissions/cost/scholarships/in-state-students
- checks: {"thresholds": null}
  - award_amount_text: $22,500 ⟵ “Presidential Scholarship | 32-36 ACT or 1420-1600 SAT | 3.5-3.99 | $22,500”
  - gpa_requirement: 3.5-3.99 ⟵ “Presidential Scholarship | 32-36 ACT or 1420-1600 SAT | 3.5-3.99 | $22,500”
### `e4eafe6b11a711b2` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/in-state-students (sha256 23475fbf7374)
- issues: conflicting_sources:https://www.uab.edu/admissions/cost/scholarships/out-of-state-students
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $5,000 ⟵ “Green & Gold Scholarship | 24-26 ACT or 1160-1250 SAT | 3.5 or higher | $5,000”
  - gpa_requirement: 3.5 or higher ⟵ “Green & Gold Scholarship | 24-26 ACT or 1160-1250 SAT | 3.5 or higher | $5,000”
### `eadd7d5428601946` University of Alabama at Birmingham — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uab.edu/admissions/cost/scholarships/in-state-students (sha256 23475fbf7374)
- issues: conflicting_sources:https://www.uab.edu/admissions/cost/scholarships/out-of-state-students
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: $8,000 ⟵ “Provost Scholarship | 27-29 ACT or 1260-1350 SAT | 3.5 or higher | $8,000”
  - gpa_requirement: 3.5 or higher ⟵ “Provost Scholarship | 27-29 ACT or 1260-1350 SAT | 3.5 or higher | $8,000”
### `0f252971b925bf9d` University of Alabama at Birmingham — credit_policies 2025-26 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.uab.edu/undergraduate/progresstowardadegree/ib/ (sha256 ba823952fdb5)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 15, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5]:  ⟵ “Biology | BY 123, BY 124 | HL | 5 | 8 | Pass”
  - equivalencies[IB-CHEMISTRY|5]:  ⟵ “Chemistry | CH 115, CH 116, CH 117, CH 118 | HL | 5 | 8 | Pass”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | EC 210, EC 211 | HL | 5 | 6 | Pass”
  - equivalencies[IB-ECONOMICS|5]:  ⟵ “Economics | ELEC 101 | SL | 5 | 3 | Pass”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|5]:  ⟵ “English A: Language and Literature | EH 101 | HL | 5 | 3 | Pass”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|7]:  ⟵ “English A: Language and Literature | EH 101, EH 102 | HL | 7 | 6 | Pass”
  - equivalencies[IB-FRENCH|4]:  ⟵ “French B | FR 101 | SL | 4 | 4 | Pass”
  - equivalencies[IB-FRENCH|5]:  ⟵ “French B | FR 101, FR 102 | HL | 5 | 8 | Pass”
  - equivalencies[IB-FRENCH|6]:  ⟵ “French B | FR 101, FR 102, FR 201 | SL | 6 | 11 | Pass”
  - equivalencies[IB-FRENCH|7]:  ⟵ “French B | FR 101, FR 102, FR 201, FR 202 | HL | 7 | 14 | Pass”
  - equivalencies[IB-GERMAN|4]:  ⟵ “German B | GN 101 | SL | 4 | 4 | Pass”
  - equivalencies[IB-GERMAN|5]:  ⟵ “German B | GN 101, GN 102 | SL | 5 | 8 | Pass”
  - equivalencies[IB-GERMAN|6]:  ⟵ “German B | GN 101, GN 102, GN 201 | SL | 6 | 11 | Pass”
  - equivalencies[IB-GERMAN|7]:  ⟵ “German B | GN 101, GN 102, GN 201, GN 202 | HL | 7 | 14 | Pass”
  - equivalencies[IB-HISTORY|5]:  ⟵ “History Americas | HY 120, HY 121 | HL | 5 | 6 | Pass”
  - equivalencies[IB-HISTORY|5]:  ⟵ “History Europe | HY 101, HY 102 | HL | 5 | 6 | Pass”
  - equivalencies[IB-LATIN|6]:  ⟵ “Latin B | Core Area II Elective | HL | 6 | 8 | Pass”
  - equivalencies[IB-MUSIC|5]:  ⟵ “Music | MU 261 | HL | 5 | 3 | Pass”
  - equivalencies[IB-MUSIC|5]:  ⟵ “Music | MU 120 | SL | 5 | 3 | Pass”
  - equivalencies[IB-PHILOSOPHY|5]:  ⟵ “Philosophy | PHL 100 | HL | 5 | 3 | Pass”
  - equivalencies[IB-PHILOSOPHY|5]:  ⟵ “Philosophy | Core Area II Elective | SL | 5 | 3 | Pass”
  - equivalencies[IB-PHYSICS|5]:  ⟵ “Physics | PH 201, PH 202 | HL | 5 | 8 | Pass”
  - equivalencies[IB-PHYSICS|5]:  ⟵ “Physics | PHS 101 | SL | 5 | 4 | Pass”
  - equivalencies[IB-PSYCHOLOGY|5]:  ⟵ “Psychology | Core Area IV Elective | HL | 5 | 6 | Pass”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5]:  ⟵ “Social Anthropology | ANTH 101 | HL | 5 | 3 | Pass”
  - … 6 more rows
### `af2a4b6456dd28e6` University of Alabama at Birmingham — credit_policies 2025-26 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.uab.edu/undergraduate/progresstowardadegree/clep/ (sha256 846979055a0b)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 28, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | PSC 101 | 50 | 3 | Pass”
  - equivalencies[CLEP-BIOLOGY|55-59]:  ⟵ “Biology* | BY 123, BY 124 | 55-59 | 8 | C”
  - equivalencies[CLEP-BIOLOGY|60-64]:  ⟵ “Biology* | BY 123, BY 124 | 60-64 | 8 | B”
  - equivalencies[CLEP-BIOLOGY|65-above]:  ⟵ “Biology* | BY 123, BY 124 | 65-above | 8 | A”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus with Elementary Functions | MA 125 | 50 | 4 | Pass”
  - equivalencies[CLEP-CHEMISTRY|55]:  ⟵ “Chemistry | CH 115, CH 117 | 55 | 6 | Pass”
  - equivalencies[CLEP-CHEMISTRY|70]:  ⟵ “Chemistry | CH 115, CH 116, CH 117, CH 118 | 70 | 8 | Pass”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | MA 102 | 50 | 3 | Pass”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|44-54]:  ⟵ “College Composition Modular§ | EH 101 | 44-54 | 3 | Pass”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|55 and above]:  ⟵ “College Composition Modular§ | EH 101, EH 102 | 55 and above | 6 | Pass”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition*** | ELEC 101 | 50 | 6 | Pass”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | AC 200 | 50 | 3 | Pass”
  - equivalencies[CLEP-FRENCH-LANGUAGE|45-49]:  ⟵ “French Language: Level 1 and 2 | FR 101 | 45-49 | 4 | Pass”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50-54]:  ⟵ “French Language: Level 1 and 2 | FR 101, FR 102 | 50-54 | 8 | Pass”
  - equivalencies[CLEP-FRENCH-LANGUAGE|55]:  ⟵ “French Language: Level 1 and 2 | FR 101, FR 102, FR 201 | 55 | 11 | Pass”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language: Level 1 and 2 | GN 101, GN 102 | 50 | 8 | Pass”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I: Early Colonization to 1877 | HY 120 | 50 | 3 | Pass”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II: 1865 to Present | HY 121 | 50 | 3 | Pass”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth Development | PY 212 or EPR 414 | 50 | 3 | Pass”
  - equivalencies[CLEP-HUMANITIES|60]:  ⟵ “Humanities*** | ELEC 101 | 60 | 3 | Pass”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems Computer Applications | IS 303 | 50 | 3 | Pass”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | ELEC 101 | 50 | 3 | Pass”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | LS 246 | 50 | 3 | Pass”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PY 101 | 50 | 3 | Pass”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SOC 100 | 50 | 3 | Pass”
  - … 11 more rows
### `d6bc75d27144ec24` University of Alabama at Birmingham — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.uab.edu/undergraduate/progresstowardadegree/apcredit/ (sha256 f23c86316a7e)
- issues: stale_year_label:2025-26
- checks: {"distinct_exams": 36, "equivalencies": 55, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “2D Art and Design | ARS 101 | 4 | 3 | Pass”
  - equivalencies[AP-3-D-ART-DESIGN|4]:  ⟵ “3D Art and Design | ARS 102 | 4 | 3 | Pass”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | AAS 200 | 3 | 3 | Pass”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | ARH 204 | 3 | 3 | Pass”
  - equivalencies[AP-ART-HISTORY|5]:  ⟵ “Art History | ARH 203/ARH 204 | 5 | 6 | Pass”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | BY 123 | 4 | 4 | Pass”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | MA 125 | 4 | 4 | Pass”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | MA 125 | 3 | 4 | Pass”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | MA 125, MA 126 | 4 | 8 | Pass”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | CH 115, CH 117 | 4 | 6 | Pass”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry | CH 115, CH 116, CH 117, CH 118 | 5 | 8 | Pass”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language and Culture | CHI 101 | 3 | 3 | Pass”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language and Culture | CHI 101, CHI 102 | 4 | 6 | Pass”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language and Culture | CHI 101, CHI 102, CHI 201 | 5 | 9 | Pass”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | PSC 102 | 3 | 3 | Pass”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles | CS 103 | 4 | 4 | Pass”
  - equivalencies[AP-DRAWING|4]:  ⟵ “Drawing | ARS 100 | 4 | 3 | Pass”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | EH 101 | 3 | 3 | Pass”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|5]:  ⟵ “English Language and Composition | EH 101, EH 102 | 5 | 6 | Pass”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature and Composition | EH 212 | 4 | 3 | Pass”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | BY 108 | 4 | 3 | Pass”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | HY 102 | 4 | 3 | Pass”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language and Culture | FR 101 | 3 | 4 | Pass”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture | FR 101, FR 102 | 4 | 8 | Pass”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language and Culture | FR 101, FR 102, FR 201 | 5 | 11 | Pass”
  - … 30 more rows
### `8294331392bbc086` University of Alabama in Huntsville — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/policies/ (sha256 3536c288e454)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The SAP notification email will include information on how to submit a SAP appeal online.”
### `18fca48317ce24ad` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman (sha256 2a788617d68a)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $7,000 ⟵ “Atlas D | 27-28 or 1260-1320 | 4.0+ | $7,000 | $28,000”
  - gpa_requirement: 4.0+ ⟵ “Atlas D | 27-28 or 1260-1320 | 4.0+ | $7,000 | $28,000”
### `2489aeb78a487b2f` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships (sha256 6542d3c49113)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": null}
  - award_amount_text: $5,000 ⟵ “Juno 1 | No ACT/SAT score | 3.5-3.74 | $5,000 | $20,000”
  - gpa_requirement: 3.5-3.74 ⟵ “Juno 1 | No ACT/SAT score | 3.5-3.74 | $5,000 | $20,000”
### `28a84539277569ae` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships (sha256 f41b27330935)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $5,000 ⟵ “Jupiter C | No ACT/SAT score | 4.0+ | $5,000 | $20,000”
  - gpa_requirement: 4.0+ ⟵ “Jupiter C | No ACT/SAT score | 4.0+ | $5,000 | $20,000”
### `360f387d783bc422` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships (sha256 f41b27330935)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “Juno 1 | No ACT/SAT score | 3.5-3.74 | $2,000 | $8,000”
  - gpa_requirement: 3.5-3.74 ⟵ “Juno 1 | No ACT/SAT score | 3.5-3.74 | $2,000 | $8,000”
### `7348a9c152c3b2f1` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman (sha256 2a788617d68a)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: Tuition ⟵ “Saturn V | 31-36 or 1390-1600 | 4.0+ | Tuition | Tuition”
  - gpa_requirement: 4.0+ ⟵ “Saturn V | 31-36 or 1390-1600 | 4.0+ | Tuition | Tuition”
### `8656478d7c9ad523` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman (sha256 2a788617d68a)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “Titan III | 24-26 or 1160-1250 | 3.5-3.74 | $3,000 | $12,000”
  - gpa_requirement: 3.5-3.74 ⟵ “Titan III | 24-26 or 1160-1250 | 3.5-3.74 | $3,000 | $12,000”
### `8e9b46a9d34a2587` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships (sha256 6542d3c49113)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $19,000 ⟵ “Atlas D | 29-30 or 1330-1380 | 4.0+ | $19,000 | $76,000”
  - gpa_requirement: 4.0+ ⟵ “Atlas D | 29-30 or 1330-1380 | 4.0+ | $19,000 | $76,000”
### `9e6fd28c234f194e` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships (sha256 6542d3c49113)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $22,000 ⟵ “Saturn V | 31-36 or 1390-1600 | 4.0+ | $22,000 | $88,000”
  - gpa_requirement: 4.0+ ⟵ “Saturn V | 31-36 or 1390-1600 | 4.0+ | $22,000 | $88,000”
### `9ebc67e5e52a14c4` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships (sha256 f41b27330935)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: Tuition ⟵ “Saturn V | 31-36 or 1390-1600 | 4.0+ | Tuition | Tuition”
  - gpa_requirement: 4.0+ ⟵ “Saturn V | 31-36 or 1390-1600 | 4.0+ | Tuition | Tuition”
### `9fb615dc1504ddd6` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships (sha256 6542d3c49113)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $13,000 ⟵ “Jupiter C | No ACT/SAT score | 4.0+ | $13,000 | $52,000”
  - gpa_requirement: 4.0+ ⟵ “Jupiter C | No ACT/SAT score | 4.0+ | $13,000 | $52,000”
### `a624347f0fd3f027` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman (sha256 2a788617d68a)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “Juno 1 | No ACT/SAT score | 3.5-3.74 | $2,000 | $8,000”
  - gpa_requirement: 3.5-3.74 ⟵ “Juno 1 | No ACT/SAT score | 3.5-3.74 | $2,000 | $8,000”
### `abc5d6448daa5cb1` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman (sha256 2a788617d68a)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $5,000 ⟵ “Jupiter C | No ACT/SAT score | 4.0+ | $5,000 | $20,000”
  - gpa_requirement: 4.0+ ⟵ “Jupiter C | No ACT/SAT score | 4.0+ | $5,000 | $20,000”
### `da5841f863b643cb` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships (sha256 6542d3c49113)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": null}
  - award_amount_text: $10,000 ⟵ “Titan III | No ACT/SAT score | 3.75-3.99 | $10,000 | $40,000”
  - gpa_requirement: 3.75-3.99 ⟵ “Titan III | No ACT/SAT score | 3.75-3.99 | $10,000 | $40,000”
### `e73f832062391d44` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships (sha256 f41b27330935)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $7,000 ⟵ “Atlas D | 27-28 or 1260-1320 | 4.0+ | $7,000 | $28,000”
  - gpa_requirement: 4.0+ ⟵ “Atlas D | 27-28 or 1260-1320 | 4.0+ | $7,000 | $28,000”
### `f7689addb0a17668` University of Alabama in Huntsville — awards 2027-28 [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-in-state-academic-scholarships (sha256 f41b27330935)
- issues: conflicting_sources:https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/freshman-out-of-state-academic-scholarships,https://www.uah.edu/admissions/undergraduate/financial-aid/scholarships/freshmen/tn-nine-county-scholarships-for-freshman
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “Titan III | 24-26 or 1160-1250 | 3.5-3.74 | $3,000 | $12,000”
  - gpa_requirement: 3.5-3.74 ⟵ “Titan III | 24-26 or 1160-1250 | 3.5-3.74 | $3,000 | $12,000”
### `173f2c69212279cc` University of Alabama in Huntsville — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uah.edu/admissions/undergraduate/financial-aid/costs/tuition-estimator (sha256 2c780e77392d)
- issues: cost_period_semester, residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition: 0 ⟵ “Tuition | $0”
  - column:College Fees: 0 ⟵ “College Fees | $0”
  - column:CoAHSS Fees: 0 ⟵ “CoAHSS Fees | $0”
  - column:CoBus Fees: 0 ⟵ “CoBus Fees | $0”
  - column:CoESHS Fees: 0 ⟵ “CoESHS Fees | $0”
  - column:CoEng Fees: 0 ⟵ “CoEng Fees | $0”
  - column:CoNurs Fees: 0 ⟵ “CoNurs Fees | $0”
  - column:CoSci Fees: 0 ⟵ “CoSci Fees | $0”
  - column:Infrastructure Fees: 0 ⟵ “Infrastructure Fees | $0”
  - column:Charger Course Pack: 0 ⟵ “Charger Course Pack | $0”
  - column:Estimated Total: 0 ⟵ “Estimated Total | $0”
### `6ec81eadc78f5ca9` University of Alabama in Huntsville — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.uah.edu/admissions/undergraduate/admitted-students/ap-ib (sha256 5207a1069460)
- issues: credits_implausible
- checks: {"distinct_exams": 29, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|34 - 5]:  ⟵ “Art History | 34 - 5 | 36 | ARH 100ARH 100, 101”
  - equivalencies[AP-2-D-ART-DESIGN|4-54-5]:  ⟵ “Art Studio Drawing 2-D | 4-54-5 | 33 | ARS 160 ARS 123”
  - equivalencies[AP-BIOLOGY|3 4 -5]:  ⟵ “Biology | 3 4 -5 | 4 8 | BYS 119, 121BYS 119, 120, 121, 122”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus | 4-5 | 3 | MA 115”
  - equivalencies[AP-CALCULUS-AB|3 - 5]:  ⟵ “Calculus AB | 3 - 5 | 4 | MA 171”
  - equivalencies[AP-CALCULUS-BC|3 4 - 5]:  ⟵ “Calculus BC | 3 4 - 5 | 4 8 | MA 171 MA 171, 172”
  - equivalencies[AP-CHEMISTRY|3 4 5]:  ⟵ “Chemistry | 3 4 5 | 4 4 8 | CH 101, 105 CH 121, 125 CH 121, 123, 125, 126”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3 - 54 - 5]:  ⟵ “Computer Science A (a student may receive credit for either EGR or CS courses, but not both) | 3 - 54 - 5 | 3 3 | CS 103EGR 101”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4 - 5]:  ⟵ “Computer Science Principles | 4 - 5 | 3 | CS 102”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 4* 5]:  ⟵ “English Language or Literature Composition | 3 4* 5 | 3 3 6 | EH 101 EH 101 EH 101, 102”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3 - 5]:  ⟵ “Environmental Science | 3 - 5 | 4 | AES 103”
  - equivalencies[AP-EUROPEAN-HISTORY|34 - 5]:  ⟵ “European History | 34 - 5 | 36 | HY 103HY 103, 104”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 4 5]:  ⟵ “Foreign Language: French, German, Spanish | 3 4 5 | 6 9 12 | 101, 102 101, 102, 201 101, 102, 201, 202”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3 - 5]:  ⟵ “US Government and Politics | 3 - 5 | 3 | PSC 101”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3 - 5]:  ⟵ “Comparative Government and Politics | 3 - 5 | 3 | PSC 102”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3 - 5]:  ⟵ “Human Geography | 3 - 5 | 3 | AES 110”
  - equivalencies[AP-MACROECONOMICS|3 - 5]:  ⟵ “Macroeconomics | 3 - 5 | 3 | ECN 142”
  - equivalencies[AP-MICROECONOMICS|3 - 5]:  ⟵ “Microeconomics | 3 - 5 | 3 | ECN 143”
  - equivalencies[AP-MUSIC-THEORY|3 - 5]:  ⟵ “Music Theory | 3 - 5 | 4 | MU 201, 203”
  - equivalencies[AP-PHYSICS-1|3 - 5]:  ⟵ “Physics 1 | 3 - 5 | 4 | PH 101”
  - equivalencies[AP-PHYSICS-2|3 - 5]:  ⟵ “Physics 2 | 3 - 5 | 4 | PH 102”
  - equivalencies[AP-PHYSICS-C-MECHANICS|3 - 5]:  ⟵ “Physics C-Mechanics | 3 - 5 | 4 | PH 111, 114”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|3 - 5]:  ⟵ “Physics C-Electricity & Magnetism | 3 - 5 | 4 | PH 112, 115”
  - equivalencies[AP-PSYCHOLOGY|3 - 5]:  ⟵ “Psychology | 3 - 5 | 3 | PY 101”
  - equivalencies[AP-RESEARCH|5 (with a score of 3+ in Seminar)]:  ⟵ “Research | 5 (with a score of 3+ in Seminar) | 6 | EH 101, 102”
  - … 4 more rows
### `775450b0eb5a9a50` University of Montevallo — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.montevallo.edu/wp-content/uploads/2025/05/2025-26-finalapprovedUMCOACostMailer-Undergrad-030125L.pdf (sha256 7fc36e8f2d81)
- issues: multiple_total_rows, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 5, "rows": 17}
  - on_campus:Tuition and Fees (1): 14416.0 ⟵ “Tuition and Fees (1) | $14,416.00 | $14,416.00 | $14,416.00 | $27,886.00 $27,886.00”
  - on_campus:Housing (2): 6910.0 ⟵ “Housing (2) | $6,910.00 | $0.00 | $0.00 | $6,910.00 | $0.00”
  - on_campus:Food (2): 4600.0 ⟵ “Food (2) | $4,600.00 | $520.00 | $520.00 | $4,600.00 | $520.00”
  - on_campus:Total Estimated Direct Cost: 25926.0 ⟵ “Total Estimated Direct Cost | $25,926.00 | $14,936.00 | $14,936.00 | $39,396.00 $28,406.00”
  - on_campus:Books and Supplies (3): 800.0 ⟵ “Books and Supplies (3) | $800.00 | $800.00 | $800.00 | $800.00 | $800.00”
  - on_campus:Transportation (3): 1460.0 ⟵ “Transportation (3) | $1,460.00 | $1,460.00 | $1,660.00 | $1,460.00 | $1,460.00”
  - on_campus:Personal (3) (4): 1490.0 ⟵ “Personal (3) (4) | $1,490.00 | $1,490.00 | $1,490.00 | $1,490.00 | $1,490.00”
  - on_campus:Living Expense (3): 0.0 ⟵ “Living Expense (3) | $0.00 | $10,990.00 | $3,880.00 | $0.00 $10,990.00”
  - on_campus:Total Estimated Indirect Cost: 3750.0 ⟵ “Total Estimated Indirect Cost | $3,750.00 | $14,740.00 | $7,830.00 | $3,750.00 $14,740.00”
  - on_campus:Total Estimated Direct and Indirect Cost: 29676.0 ⟵ “Total Estimated Direct and Indirect Cost | $29,676.00 | $29,676.00 | $22,766.00 | $43,146.00 $43,146.00”
  - on_campus:Early Childhood Education: 842 ⟵ “Early Childhood Education | $842”
  - on_campus:Elementary Education: 892 ⟵ “Elementary Education | $892”
  - on_campus:Elementary/Collaborative Education: 1062 ⟵ “Elementary/Collaborative Education | $1,062”
  - on_campus:EDHH: 703 ⟵ “EDHH | $703”
  - on_campus:FCSE Education: 703 ⟵ “FCSE Education | $703”
  - on_campus:Music Education: 703 ⟵ “Music Education | $703”
  - on_campus:BSN Nursing: 3000 ⟵ “BSN Nursing | $3,000”
  - off_campus_not_with_family:Tuition and Fees (1): 14416.0 ⟵ “Tuition and Fees (1) | $14,416.00 | $14,416.00 | $14,416.00 | $27,886.00 $27,886.00”
  - off_campus_not_with_family:Housing (2): 0.0 ⟵ “Housing (2) | $6,910.00 | $0.00 | $0.00 | $6,910.00 | $0.00”
  - off_campus_not_with_family:Food (2): 520.0 ⟵ “Food (2) | $4,600.00 | $520.00 | $520.00 | $4,600.00 | $520.00”
  - off_campus_not_with_family:Total Estimated Direct Cost: 14936.0 ⟵ “Total Estimated Direct Cost | $25,926.00 | $14,936.00 | $14,936.00 | $39,396.00 $28,406.00”
  - off_campus_not_with_family:Books and Supplies (3): 800.0 ⟵ “Books and Supplies (3) | $800.00 | $800.00 | $800.00 | $800.00 | $800.00”
  - off_campus_not_with_family:Transportation (3): 1460.0 ⟵ “Transportation (3) | $1,460.00 | $1,460.00 | $1,660.00 | $1,460.00 | $1,460.00”
  - off_campus_not_with_family:Personal (3) (4): 1490.0 ⟵ “Personal (3) (4) | $1,490.00 | $1,490.00 | $1,490.00 | $1,490.00 | $1,490.00”
  - off_campus_not_with_family:Living Expense (3): 10990.0 ⟵ “Living Expense (3) | $0.00 | $10,990.00 | $3,880.00 | $0.00 $10,990.00”
  - … 22 more rows
### `a6c0cf5fed514db8` University of Montevallo — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.montevallo.edu/wp-content/uploads/2026/05/2026-27-FinalUMCOACostMailer-Undergrad-041726.pdf (sha256 38cf08686f54)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 5, "rows": 10}
  - on_campus:Tuition and Fees (1): 14616.0 ⟵ “Tuition and Fees (1) | $14,616.00 | $14,616.00 | $14,616.00 | $28,086.00 $28,086.00”
  - on_campus:Housing (2): 7178.0 ⟵ “Housing (2) | $7,178.00 | $0.00 | $0.00 | $7,178.00 | $0.00”
  - on_campus:Food (2): 4850.0 ⟵ “Food (2) | $4,850.00 | $620.00 | $620.00 | $4,850.00 | $620.00”
  - on_campus:Total Estimated Direct Cost: 26644.0 ⟵ “Total Estimated Direct Cost | $26,644.00 | $15,236.00 | $15,236.00 | $40,114.00 $28,706.00”
  - on_campus:Books and Supplies (3): 600.0 ⟵ “Books and Supplies (3) | $600.00 | $600.00 | $600.00 | $600.00 | $600.00”
  - on_campus:Transportation (3): 1460.0 ⟵ “Transportation (3) | $1,460.00 | $1,460.00 | $1,660.00 | $1,460.00 | $1,460.00”
  - on_campus:Personal (3) (4): 1290.0 ⟵ “Personal (3) (4) | $1,290.00 | $1,290.00 | $1,290.00 | $1,290.00 | $1,290.00”
  - on_campus:Living Expense (3): 0.0 ⟵ “Living Expense (3) | $0.00 | $11,408.00 | $3,880.00 | $0.00 $11,408.00”
  - on_campus:Total Estimated Indirect Cost: 3350.0 ⟵ “Total Estimated Indirect Cost | $3,350.00 | $14,758.00 | $7,430.00 | $3,350.00 $14,758.00”
  - on_campus:Total Estimated Direct and Indirect Cost: 29994.0 ⟵ “Total Estimated Direct and Indirect Cost | $29,994.00 | $29,994.00 | $22,666.00 | $43,464.00 $43,464.00”
  - off_campus_not_with_family:Tuition and Fees (1): 14616.0 ⟵ “Tuition and Fees (1) | $14,616.00 | $14,616.00 | $14,616.00 | $28,086.00 $28,086.00”
  - off_campus_not_with_family:Housing (2): 0.0 ⟵ “Housing (2) | $7,178.00 | $0.00 | $0.00 | $7,178.00 | $0.00”
  - off_campus_not_with_family:Food (2): 620.0 ⟵ “Food (2) | $4,850.00 | $620.00 | $620.00 | $4,850.00 | $620.00”
  - off_campus_not_with_family:Total Estimated Direct Cost: 15236.0 ⟵ “Total Estimated Direct Cost | $26,644.00 | $15,236.00 | $15,236.00 | $40,114.00 $28,706.00”
  - off_campus_not_with_family:Books and Supplies (3): 600.0 ⟵ “Books and Supplies (3) | $600.00 | $600.00 | $600.00 | $600.00 | $600.00”
  - off_campus_not_with_family:Transportation (3): 1460.0 ⟵ “Transportation (3) | $1,460.00 | $1,460.00 | $1,660.00 | $1,460.00 | $1,460.00”
  - off_campus_not_with_family:Personal (3) (4): 1290.0 ⟵ “Personal (3) (4) | $1,290.00 | $1,290.00 | $1,290.00 | $1,290.00 | $1,290.00”
  - off_campus_not_with_family:Living Expense (3): 11408.0 ⟵ “Living Expense (3) | $0.00 | $11,408.00 | $3,880.00 | $0.00 $11,408.00”
  - off_campus_not_with_family:Total Estimated Indirect Cost: 14758.0 ⟵ “Total Estimated Indirect Cost | $3,350.00 | $14,758.00 | $7,430.00 | $3,350.00 $14,758.00”
  - off_campus_not_with_family:Total Estimated Direct and Indirect Cost: 29994.0 ⟵ “Total Estimated Direct and Indirect Cost | $29,994.00 | $29,994.00 | $22,666.00 | $43,464.00 $43,464.00”
  - with_parents_or_family:Tuition and Fees (1): 14616.0 ⟵ “Tuition and Fees (1) | $14,616.00 | $14,616.00 | $14,616.00 | $28,086.00 $28,086.00”
  - with_parents_or_family:Housing (2): 0.0 ⟵ “Housing (2) | $7,178.00 | $0.00 | $0.00 | $7,178.00 | $0.00”
  - with_parents_or_family:Food (2): 620.0 ⟵ “Food (2) | $4,850.00 | $620.00 | $620.00 | $4,850.00 | $620.00”
  - with_parents_or_family:Total Estimated Direct Cost: 15236.0 ⟵ “Total Estimated Direct Cost | $26,644.00 | $15,236.00 | $15,236.00 | $40,114.00 $28,706.00”
  - with_parents_or_family:Books and Supplies (3): 600.0 ⟵ “Books and Supplies (3) | $600.00 | $600.00 | $600.00 | $600.00 | $600.00”
  - … 16 more rows
### `f88378b080212881` University of South Alabama — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.southalabama.edu/departments/registrar/records/transferassistance/ap-clep-ib-military.html (sha256 0f3b054a6abf)
- issues: rows_without_score
- checks: {"distinct_exams": 25, "equivalencies": 44, "rows_without_score": 17}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | ACC 211 | 3 hrs | 50”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “General Biology | BLY 121/121L &BLY 122/122L | 8 hrs | 50”
  - equivalencies[CLEP-NATURAL-SCIENCES|50]:  ⟵ “Natural Sciences-General | Biology & Natural Science Electives | 8 hrs | 50”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Intro to Business Law | BUS 265 | 3 hrs | 50”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “General Chemistry | CH 131/131L &CH 132/132L | 8 hrs | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Intro to Microeconomics | ECO 215 | 3 hrs | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Intro to Macroeconomics | ECO 216 | 3 hrs | 50”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | EH 101 & EH 102 | 6 hrs | 50”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities-General | Fine Arts & Literature Electives | 6 hrs | 50”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 - | HY 101 | 3 hrs | 50”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II: 1648 to Present | HY 102 | 3 hrs | 50”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “U.S. History I: Early Colonizations to 1877 | HY 135 | 3 hrs | 50”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “US History II: 1865 to Present - | HY 136 | 3 hrs | 50”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | MA 115 | 4 hrs | 50”
  - equivalencies[CLEP-CALCULUS|60]:  ⟵ “Calculus | MA 125 | 4 hrs | 60”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | Math Electives | 8 hrs | 50”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Intro to Marketing | MKT 320 | 3 hrs | 50”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | PSC 130 | 3 hrs | 50”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Intro to Psychology | PSY 120 | 3 hrs | 50”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth andDevelopment | PSY 250 | 3 hrs | 50”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Intro to Sociology | SY 109 | 3 hrs | 50”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50-58]:  ⟵ “French | LG 111 & LG 112 | 6 hrs | 50-58”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59+]:  ⟵ “French | LG 111, LG 112, and LG 211 | 9 hrs | 59+”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50-59]:  ⟵ “German | LG 151 & LG 152 | 6 hrs | 50-59”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German | LG 151, LG 152, and LG 251 | 9 hrs | 60”
  - … 19 more rows
### `05decf4dbb000358` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/ (sha256 cfc61a454e8b)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `0600d41194a25d80` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/financial-aid-faq/ (sha256 f33396d2dc8a)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Contact Student Accounts if you have questions about: Tuition and fees Account balances Making payments Payment plans Refunds Billing Contact Financial Aid if you have questions about: FAFSA Scholarships and grants Student loans Financial aid eligibility Financial aid awards Satisfactory Academic Progress (SAP) Special circumstances and appeals Applying for Financial Aid How can I apply for financ”
  - sentence: sap_appeal ⟵ “How do I appeal Satisfactory Academic Progress (SAP)?”
  - sentence: sap_appeal ⟵ “If you do not meet the Satisfactory Academic Progress (SAP) standards for financial aid, you may be eligible to submit a SAP appeal.”
  - sentence: sap_appeal ⟵ “Before submitting an appeal, review the Satisfactory Academic Progress Policy webpage for eligibility requirements, appeal deadlines, and step-by-step instructions for completing the appeal process.”
  - sentence: sap_appeal ⟵ “A SAP appeal may be submitted if you experienced circumstances beyond your control that affected your academic progress, including: The death of a family member Your illness or injury Other documented special circumstances, such as: A difficult transition to UWA Family-related challenges Legal issues Employment or financial difficulties Supporting documentation and an academic plan may be required”
  - sentence: sap_appeal ⟵ “Refer to the Satisfactory Academic Progress Policy for complete appeal requirements and submission instructions.”
### `0d0b01e270778aa0` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/ (sha256 77cd6ab5d296)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Policy Everything you need to know about maintaining Satisfactory Academic Progress and SAP appeals.”
### `11e0ef237d1dc244` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/ (sha256 5eaf92246cef)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `1854114d28fc55e6` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/ (sha256 77cd6ab5d296)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment (PJ) Request for special consideration for financial aid due to financial/personal hardship.”
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `23ab825f0c1b7c7e` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/university-departments/student-accounts/ (sha256 a6d1215d5e16)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `2b53dd4bab3e3217` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/veterans-assistance/ (sha256 1e12005c249d)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `3087ef0edb176817` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/ (sha256 c2027936ac81)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `32ae13e2afd34cd4` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/financial-aid-faq/ (sha256 f33396d2dc8a)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `3a65d9ff9cb1450d` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/professional-judgement/ (sha256 a90af5aa2a5a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances are financial situations that may justify an aid administrator adjusting data elements in the cost of attendance or in the Student Aid Index (SAI) calculation.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances are conditions that may justify an aid administrator adjusting a student’s dependency status based on a unique situation.”
  - sentence: need_based_special_circumstances ⟵ “A student may have both a special circumstance and an unusual circumstance.”
### `5f4f38bbf34121ee` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/grants/ (sha256 2e67f8478d62)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `68a46b9ad58834b2` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/professional-judgement/ (sha256 a90af5aa2a5a)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: professional_judgment ⟵ “Professional Judgment allows the Financial Aid Office to review certain documented circumstances on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “A Professional Judgment review does not guarantee additional aid, but it allows us to determine whether adjustments may be appropriate based on your situation and supporting documentation.”
  - sentence: professional_judgment ⟵ “Request Special Consideration The Professional Judgment (PJ) Advisor portal will guide you through the special consideration request process.”
  - sentence: professional_judgment ⟵ “Submit a Professional Judgment Appeal for the 2026–2027 Academic Year After accessing the PJ Advisor portal, you (or a parent, spouse, or legal guardian) will need to complete the following steps: Create a secure username and password.”
  - sentence: professional_judgment ⟵ “If you have any questions about the Professional Judgment process, please contact the University of West Alabama at (205) 652-3576 or email [email protected].”
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `8417eefa86e06ddd` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/ (sha256 46a028470566)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `8fe7ab297f207acb` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/ (sha256 b568babb3b5e)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `9fd2720a4a454a94` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/ (sha256 57e1f4d0a1f7)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `a4832bc84faed470` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/admissions/transfer-students/ (sha256 5ffb5417217c)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `a97339124f8f3bd0` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/admissions/international-students/ (sha256 5a482922e181)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `bc8a5ef73519ac24` University of West Alabama — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/cost-of-attendance/ (sha256 78c9187c7078)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `cda74d4642481838` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/university-departments/student-accounts/refund/ (sha256 136a1e8e6bf6)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `d26a09a207f396db` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/ (sha256 f5103d7f6939)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `ddc3046f6770e0d4` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/ (sha256 57e1f4d0a1f7)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If you have not met SAP standards, you may submit an SAP appeal to request financial aid reinstatement for the 2026–2027 aid year.”
  - sentence: sap_appeal ⟵ “Submit SAP Appeal for 26-27 Aid Year SAP Appeal Deadlines To be considered for financial aid reinstatement, your SAP appeal must be submitted by the following deadlines: 2026-2027 | Term | Appeal Deadline | Fall 2026 | August 5, 2026 – 12:00 PM | Fall 2026 (#2) | August 10, 2026 – 12:00 PM | Spring 2027 | December 14, 2026 – 12:00 PM | Summer 2027 | May 10, 2026 – 12:00 PM How to Submit an SAP App”
  - sentence: sap_appeal ⟵ “A student who does not meet the requirements for SAP may choose to appeal to the Financial Aid Office for an exception on the grounds that a special or extenuating circumstance contributed to his or her failure to meet standards and what has changed that will allow the student to regain SAP at the next semester.”
  - sentence: sap_appeal ⟵ “Such appeals must be submitted on the Satisfactory Academic Progress Appeal Form that is available in the Financial Aid Office.”
### `e708c4998a536463` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/ (sha256 d7e1c2167b88)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `ea2a2ad184768a32` University of West Alabama — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.uwa.edu/university-departments/student-accounts/refund/ (sha256 368421d69e58)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `efe0545a7968eb40` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/project-inspire/ (sha256 940a1de2dc26)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `feea4d44d38c6228` University of West Alabama — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uwa.edu/financial-aid/scholarships/james-p-pate-scholarship-competition/ (sha256 89e382ea6696)
- issues: semantic_review_required, conflicting_sources:https://www.uwa.edu/admissions/international-students/,https://www.uwa.edu/admissions/international-students/english-proficiency-evaluation/,https://www.uwa.edu/admissions/transfer-students/,https://www.uwa.edu/admissions/transfer-students/phi-theta-kappa-direct-admission/,https://www.uwa.edu/financial-aid/,https://www.uwa.edu/financial-aid/financial-aid-faq/,https://www.uwa.edu/financial-aid/grants/,https://www.uwa.edu/financial-aid/professional-judgement/,https://www.uwa.edu/financial-aid/satisfactory-academic-progress-policy/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/,https://www.uwa.edu/financial-aid/scholarships/kelly-land-writing-competition/,https://www.uwa.edu/financial-aid/scholarships/particular-ability-tuition-rate/,https://www.uwa.edu/financial-aid/scholarships/project-inspire/,https://www.uwa.edu/financial-aid/veterans-assistance/,https://www.uwa.edu/university-departments/student-accounts/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/refund/,https://www.uwa.edu/university-departments/student-accounts/tuition-payment-plans/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Admissions First-Time Freshmen Undergraduate Transfer Students Online Students Graduate Students International Students Dual Enrollment Students Financial Aid Apply for Financial Aid Scholarships Loans Grants Federal Work Study Veterans' Assistance Cost of Attendance Enrollment Status & Withdrawal Implications FASFA Verification Professional Judgement Satisfactory Academic Progress Financial Aid F”
### `0680af784d894624` University of West Alabama — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/cost-of-attendance/ (sha256 78c9187c7078)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition: 10242.0 ⟵ “Tuition | $10,242.00 | $20,475.00”
  - column:Fees: 1890.0 ⟵ “Fees | $1,890.00 | $1,890.00”
  - column:Housing & Food: 15525.0 ⟵ “Housing & Food | $15,525.00 | $15,525.00”
  - column:Books: 972.0 ⟵ “Books | $972.00 | $972.00”
  - column:Transportation: 1935.0 ⟵ “Transportation | $1,935.00 | $1,935.00”
  - column:Technology: 900.0 ⟵ “Technology | $900.00 | $900.00”
  - column:Personal Expenses: 1935.0 ⟵ “Personal Expenses | $1,935.00 | $1,935.00”
  - column:Total: 33399.0 ⟵ “Total | $33,399.00 | $43,632.00”
### `150d41c3290e892f` University of West Alabama — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/cost-of-attendance/ (sha256 78c9187c7078)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition: 20475.0 ⟵ “Tuition | $10,242.00 | $20,475.00”
  - column:Fees: 1890.0 ⟵ “Fees | $1,890.00 | $1,890.00”
  - column:Housing & Food: 15525.0 ⟵ “Housing & Food | $15,525.00 | $15,525.00”
  - column:Books: 972.0 ⟵ “Books | $972.00 | $972.00”
  - column:Transportation: 1935.0 ⟵ “Transportation | $1,935.00 | $1,935.00”
  - column:Technology: 900.0 ⟵ “Technology | $900.00 | $900.00”
  - column:Personal Expenses: 1935.0 ⟵ “Personal Expenses | $1,935.00 | $1,935.00”
  - column:Total: 43632.0 ⟵ “Total | $33,399.00 | $43,632.00”
### `16581a7f0afa1e59` University of West Alabama — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.uwa.edu/financial-aid/cost-of-attendance/ (sha256 78c9187c7078)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 8}
  - column:Tuition: 8775.0 ⟵ “Tuition | $8,775.00”
  - column:Fees: 900.0 ⟵ “Fees | $900.00”
  - column:Housing & Food: 15525.0 ⟵ “Housing & Food | $15,525.00”
  - column:Books: 972.0 ⟵ “Books | $972.00”
  - column:Transportation: 1935.0 ⟵ “Transportation | $1,935.00”
  - column:Technology: 900.0 ⟵ “Technology | $900.00”
  - column:Personal Expenses: 1935.0 ⟵ “Personal Expenses | $1,935.00”
  - column:Total: 30942.0 ⟵ “Total | $30,942.00”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 219; pages by category: admissions_tests 9, clep_credit 143, cost_of_attendance 12, degree_requirements 21, dual_enrollment 155, merit_scholarships 9, residency 6, statewide_articulation 9, transfer_credit 75, tuition_fees 21

## Blocked by the site (every request refused; needs the browser fallback)

- Heritage Christian University (`ipeds-101453`)
- University of Mobile (`ipeds-101693`)
- Northwest Shoals Community College (`ipeds-101736`)
- University of North Alabama (`ipeds-101879`)
- Snead State Community College (`ipeds-102076`)

## Leads: official pages found with no extracted record

- Alabama A & M University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Alabama State University: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Auburn University: cost_of_attendance, admissions_tests, common_data_set, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency, aid_appeals
- Auburn University at Montgomery: admissions_tests, ap_credit, clep_credit, ib_credit, residency, degree_requirements
- Bevill State Community College: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Bishop State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Central Alabama Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- Chattahoochee Valley Community College: admissions_tests, common_data_set, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Coastal Alabama Community College: admissions_tests, merit_scholarships, clep_credit, dual_enrollment, residency, degree_requirements
- Enterprise State Community College: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- Faulkner University: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Gadsden State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- George C Wallace Community College-Dothan: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- George C Wallace State Community College-Hanceville: admissions_tests, ap_credit, transfer_credit, residency, degree_requirements
- George C Wallace State Community College-Selma: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- H Councill Trenholm State Community College: cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements
- Herzing University-Birmingham: tuition_fees, cost_of_attendance, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Huntingdon College: admissions_tests, ib_credit, dual_enrollment, residency, degree_requirements
- Huntsville Bible College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, dual_enrollment, transfer_credit, degree_requirements
- J. F. Drake State Community and Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Jacksonville State University: admissions_tests, common_data_set, merit_scholarships, ap_credit, transfer_credit, residency, degree_requirements, aid_appeals
- Jefferson State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, residency, aid_appeals
- John C Calhoun State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements, aid_appeals
- Lawson State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements, aid_appeals
- Lurleen B Wallace Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, residency, degree_requirements
- Marion Military Institute: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency, degree_requirements
- Miles College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Northeast Alabama Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Oakwood University: cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- Reid State Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Remington College-Mobile Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Samford University: cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- Selma University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, degree_requirements
- Shelton State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, transfer_credit, residency, degree_requirements
- Southern Union State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Spring Hill College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit
- Stillman College: admissions_tests, common_data_set, clep_credit, ib_credit, residency, degree_requirements
- Talladega College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- The University of Alabama: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, dual_enrollment, residency, degree_requirements, aid_appeals
- Troy University: admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency, degree_requirements
- Tuskegee University: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- United States Sports Academy: tuition_fees, admissions_tests, merit_scholarships, transfer_credit, aid_appeals
- University of Alabama at Birmingham: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, statewide_articulation, residency, degree_requirements
- University of Alabama in Huntsville: cost_of_attendance, admissions_tests, clep_credit, transfer_credit, residency, degree_requirements
- University of Montevallo: cost_of_attendance, admissions_tests, statewide_articulation, residency, degree_requirements
- University of South Alabama: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
- University of West Alabama: admissions_tests, transfer_credit, residency, degree_requirements
