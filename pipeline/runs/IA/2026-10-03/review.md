# Review queue — IA (2026-27)

Pages fetched: 3327; failures: 406. Candidates: 368 (188 without issues, 180 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 5 | 13 | 25 | 3 | 2 |
| cost_of_attendance | 0 | 0 | 2 | 5 | 37 | 2 | 2 |
| admissions_tests | 0 | 0 | 0 | 1 | 44 | 1 | 2 |
| common_data_set | 0 | 0 | 0 | 1 | 3 | 42 | 2 |
| merit_scholarships | 0 | 0 | 11 | 2 | 32 | 1 | 2 |
| ap_credit | 0 | 0 | 5 | 2 | 7 | 32 | 2 |
| clep_credit | 0 | 0 | 3 | 3 | 7 | 33 | 2 |
| ib_credit | 0 | 0 | 0 | 1 | 3 | 42 | 2 |
| dual_enrollment | 0 | 0 | 0 | 0 | 19 | 27 | 2 |
| transfer_credit | 0 | 0 | 7 | 2 | 33 | 4 | 2 |
| statewide_articulation | 0 | 0 | 0 | 0 | 16 | 30 | 2 |
| residency | 0 | 0 | 0 | 0 | 19 | 27 | 2 |
| degree_requirements | 0 | 0 | 0 | 0 | 34 | 12 | 2 |
| aid_appeals | 0 | 0 | 0 | 22 | 8 | 16 | 2 |

## Ready for review (188)

### `74dbc557a91545af` Briar Cliff University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.briarcliff.edu/future-chargers/tuition-and-aid/scholarships (sha256 41314c600eff)
- checks: {"thresholds": null}
  - award_tiers: [{'current cgpa': '3.5 - 4.0', 'amount_text': '$16,500'}, {'current cgpa': '3.0 - 3.49', 'amount_text': '$15,000'}, {'current cgpa': '2.5 - 2.99', 'amount_text': '$13,500'}] ⟵ “Current CGPA | On-Campus Student || 3.5 - 4.0 | $16,500 || 3.0 - 3.49 | $15,000 || 2.5 - 2.99 | $13,500”
  - gpa_requirement: Tiered by Current CGPA: 3.5 - 4.0 → $16,500; 3.0 - 3.49 → $15,000; 2.5 - 2.99 → $13,500 ⟵ “Current CGPA | On-Campus Student || 3.5 - 4.0 | $16,500 || 3.0 - 3.49 | $15,000 || 2.5 - 2.99 | $13,500”
### `02245e4de2e49a19` Briar Cliff University — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.briarcliff.edu/future-chargers/tuition-and-aid/costs-and-financial-aid/undergraduate (sha256 5bafa3593861)
- checks: {"columns": 1, "rows": 5}
  - column:Tuition: 19941 ⟵ “Tuition | $19,941”
  - column:General Fees: 924 ⟵ “General Fees | $924”
  - column:Residence Life Room (standard double): 2881 ⟵ “Residence Life Room (standard double) | $2,881*”
  - column:Meal Plan (standard): 3133 ⟵ “Meal Plan (standard) | $3,133**”
  - column:Health and Wellness Fee: 100 ⟵ “Health and Wellness Fee | $100”
### `3f394c9e26865649` Central College — awards 2027-28 [new] (labeled_in_source)
- source: https://central.edu/financial-aid/scholarships-awards/ (sha256 0469459db39f)
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative GPA: 2.89 and below ⟵ “2.89 and below | $4,000”
  - award_amount_text: $4,000 ⟵ “2.89 and below | $4,000”
### `69fe648e3cec74b5` Central College — awards 2027-28 [new] (labeled_in_source)
- source: https://central.edu/financial-aid/scholarships-awards/ (sha256 0469459db39f)
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative GPA: 3.4–3.849 ⟵ “3.4–3.849 | $7,000”
  - award_amount_text: $7,000 ⟵ “3.4–3.849 | $7,000”
### `9b51ee9d1a91728e` Central College — awards 2027-28 [new] (labeled_in_source)
- source: https://central.edu/financial-aid/scholarships-awards/ (sha256 0469459db39f)
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative GPA: 2.9–3.399 ⟵ “2.9–3.399 | $5,000”
  - award_amount_text: $5,000 ⟵ “2.9–3.399 | $5,000”
### `bcf44b6d234b358f` Central College — awards 2027-28 [new] (labeled_in_source)
- source: https://central.edu/financial-aid/scholarships-awards/ (sha256 0469459db39f)
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative GPA: 3.85–3.999 ⟵ “3.85–3.999 | $8,000”
  - award_amount_text: $8,000 ⟵ “3.85–3.999 | $8,000”
### `d35227109ca71979` Central College — awards 2027-28 [new] (labeled_in_source)
- source: https://central.edu/financial-aid/scholarships-awards/ (sha256 0469459db39f)
- checks: {"thresholds": null}
  - gpa_requirement: Cumulative GPA: 4.0 and above ⟵ “4.0 and above | $9,000”
  - award_amount_text: $9,000 ⟵ “4.0 and above | $9,000”
### `b7498575bfb18efd` Central College — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://departments.central.edu/registrar/transfer-creditap/advanced-placement/ (sha256 c0d28ed7bfa5)
- checks: {"distinct_exams": 32, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language | 4 |  | WRIT 101: Composition (WRT) | 3 s.h.”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature | 4 |  | ENGL 100AP: English Elective (LP) | 3 s.h.”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 |  | BIOL 100AP: Biology Elective (EXP3, NS) | 4 s.h.”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 |  | MATH 131: Calculus I (EXP3, MR) | 4 s.h.”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 |  | MATH 131/132: Calculus I & II (EXP3, MR) | 8 s.h.”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 |  | CHEM 111: General Chemistry (EXP3, NS) | 4 s.h.”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles | 4 |  | COSC 100AP: Computer Science Elective | 3 s.h.”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 |  | COSC 110: Introduction to Computer Science (EXP3) | 3 s.h.”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | 4 |  | ENVS 120: Intro to Environmental Science (EXP3, GS, NS) | 4 s.h.”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 | 4 |  | PHYS 101: Introductory Physics I (NS) | 4 s.h.”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2 | 4 |  | PHYS 102: Introductory Physics II (NS) | 4 s.h.”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics | 4 |  | PHYS 111: General Physics I (EXP3, NS) | 5 s.h.”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4]:  ⟵ “Physics C: Electricity & Magnetism | 4 |  | PHYS 112: General Physics II (NS) | 5 s.h.”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Pre-Calculus | 4 |  | MATH 109: Pre-Calculus | 4 s.h.”
  - equivalencies[AP-STATISTICS|4]:  ⟵ “Statistics | 4 |  | MATH 215: Introduction to Statistics (EXP3, MR) | 4 s.h.”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language | 4 |  | FREN 121/122: Beginning French I & II | 8 s.h.”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language | 4 |  | GERM 121/122: Beginning German I & II | 8 s.h.”
  - equivalencies[AP-LATIN|4]:  ⟵ “Latin Literature | 4 |  | LAT 121/122: Beginning Latin I & II | 6 s.h.”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4]:  ⟵ “Spanish Language | 4 |  | SPAN 121/122: Beginning Spanish I & II | 8 s.h.”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|4]:  ⟵ “Spanish Literature | 4 |  | SPAN 221/222: Intermediate Spanish I & II (EXP1, GPN) | 8 s.h.”
  - equivalencies[AP-MICROECONOMICS|4]:  ⟵ “Economics: Micro | 4 |  | ECON 112: Principles of Microeconomics (SB) | 3 s.h.”
  - equivalencies[AP-MACROECONOMICS|4]:  ⟵ “Economics: Macro | 4 |  | ECON 113: Principles of Macroeconomics (SB) | 3 s.h.”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 |  | HIST 100AP: History Elective (EXP1, HP) | 3 s.h.”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography | 4 |  | GEOG 210: Human Geography (SB) | 3 s.h.”
  - equivalencies[AP-UNITED-STATES-HISTORY|4]:  ⟵ “U.S. History | 4 |  | HIST 130 US History to 1877/131: US History Since 1877. Students with U.S. History AP may receive credit for HIST-130 or HIST-131 (not both). (EXP1, HP) | 3 s.h.”
  - … 7 more rows
### `m3313381c89f8c41` Clarke University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.clarke.edu/admission-aid/transfers/credits/ (sha256 6f071f7c23b4)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - residency_requirement_credits: 30 ⟵ “The final 30 hours of credit must be taken in residence.”
  - residency_requirement_credits: 30 ⟵ “The final 30 hours of credit must be taken in residence.”
### `33c839c60cd0c685` Coe College — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.coe.edu/admission/financial-aid-scholarships/financial-aid-handbook/educational-costs (sha256 e39445836b2e)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Full-time (3+ course credits): 31850 ⟵ “Full-time (3+ course credits) | $58,780 | $31,850”
  - column:Housing: 6100 ⟵ “Housing | $6,070 | $6,100”
  - column:Food: 6700 ⟵ “Food | $6,690 | $6,700”
  - column:Student Fee (health services and activity fee): 350 ⟵ “Student Fee (health services and activity fee) | $350 | $350”
  - column:Total Direct Educational Cost: 45000 ⟵ “Total Direct Educational Cost | $72,118 | $45,000”
### `f261ed52c1782ca5` Cornell College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cornellcollege.edu/financial-assistance/cost-of-attendance.shtml (sha256 5345eb49b0b7)
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition: 55950 ⟵ “Tuition | $55,950”
  - column:Housing (standard double room): 5724 ⟵ “Housing (standard double room) | $5,724”
  - column:Food: 6762 ⟵ “Food | $6,762”
  - column:Student Activity and General fees: 784 ⟵ “Student Activity and General fees | $784”
  - column:Books: 720 ⟵ “Books | $720”
  - column:Personal: 2000 ⟵ “Personal | $2,000”
  - column:In-state transportation*: 1200 ⟵ “In-state transportation* | $1,200”
  - column:Additional food costs: 368 ⟵ “Additional food costs | $368”
  - column:Estimated loan origination fees: 70 ⟵ “Estimated loan origination fees | $70”
  - column:Total Cost of Attendance:: 73578 ⟵ “Total Cost of Attendance: | $73,578”
  - column:Total Direct Costs: 69220 ⟵ “Total Direct Costs | $69,220”
### `fe63d3e9f322249b` Dordt University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.dordt.edu/admissions-and-aid/admission-requirements/undergraduate-program/ap-exam-credit-guide (sha256 2e4c6188e072)
- checks: {"distinct_exams": 25, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | 3 | ART elective”
  - equivalencies[AP-2-D-ART-DESIGN|4]:  ⟵ “2-D Art and Design | 4 | 3 | ART 201”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | 3 | Core 21X (CORE Natural Science, lab-based science)”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Precalculus | 4 | 4 | Math 115 and 116”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus AB or AB Subscore on Calculus BC | 4 | 4 | MATH 152”
  - equivalencies[AP-CALCULUS-BC|5]:  ⟵ “Calculus BC | 5 | 8 | MATH 152 and 153”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 4 | CHEM elective”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 | 3 | CMSC elective”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles | 4 | 3 | CMSC elective”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language and Composition | 4 | 3 | CORE 120”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language and Literature | 4 | 3 | CORE 180”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4]:  ⟵ “Environmental Science | 4 | 4 | ENVR 152”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | 3 | HIST elective”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language and Culture | 4 | 4 | FREN 101”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language and Culture | 5 | 7 | FREN 101 and 102”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4]:  ⟵ “Human Geography | 4 | 3 | CORE 26X”
  - equivalencies[AP-MACROECONOMICS|4]:  ⟵ “Macroeconomics | 4 | 3 | ECON 203”
  - equivalencies[AP-MICROECONOMICS|4]:  ⟵ “Microeconomics | 4 | 3 | ECON 202”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | 3 | MUS 103”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 Algebra-based | 4 | 3 | PHYS elective”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2 Algebra-based | 4 | 3 | PHYS elective”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics | 4 | 3 | PHYS elective”
  - equivalencies[AP-PSYCHOLOGY|4]:  ⟵ “Psychology | 4 | 3 | PSYC 201 (does not meet CORE)”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|4]:  ⟵ “Spanish Language and Culture | 4 | 4 | SPAN 101”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|5]:  ⟵ “Spanish Language and Culture | 5 | 7 | SPAN 101 and 102”
  - … 4 more rows
### `016b999bedf6b4e1` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 per year ⟵ “Legacy Award | $2,500 per year | Open to first-year students of any major who are children, grandchildren, or great-grandchildren of a Drake graduate | Automatically awarded*”
  - eligibility_summary: Open to first-year students of any major who are children, grandchildren, or great-grandchildren of a Drake graduate ⟵ “Legacy Award | $2,500 per year | Open to first-year students of any major who are children, grandchildren, or great-grandchildren of a Drake graduate | Automatically awarded*”
### `06ce869a99da5dc3` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Full tuition coverage ⟵ “National Alumni Scholarship | Full tuition coverage | Open to first-year students of any major | Application”
  - eligibility_summary: Open to first-year students of any major ⟵ “National Alumni Scholarship | Full tuition coverage | Open to first-year students of any major | Application”
### `18ffb035196b3782` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 per year ⟵ “Drake-Sponsored National Merit Scholarship | $1,500 per year | Open to first-year students of any major | Automatically awarded*”
  - eligibility_summary: Open to first-year students of any major ⟵ “Drake-Sponsored National Merit Scholarship | $1,500 per year | Open to first-year students of any major | Automatically awarded*”
### `19e5eb6f9b6675f3` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Amount varies ⟵ “Athletic Scholarship | Amount varies | Open to first-year student-athletes of any major | Automatically awarded*”
  - eligibility_summary: Open to first-year student-athletes of any major ⟵ “Athletic Scholarship | Amount varies | Open to first-year student-athletes of any major | Automatically awarded*”
### `5e78dde686e59b44` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Amounts vary ⟵ “Music Fine Arts Scholarship | Amounts vary | Open to first-year or transfer fine arts students | Application and Audition”
  - eligibility_summary: Open to first-year or transfer fine arts students ⟵ “Music Fine Arts Scholarship | Amounts vary | Open to first-year or transfer fine arts students | Application and Audition”
### `66773a48a494e90f` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Full tuition coverage ⟵ “The Bulldog Promise | Full tuition coverage | Open to first-year students who meet the Iowa residency requirements | FAFSA Application*”
  - eligibility_summary: Open to first-year students who meet the Iowa residency requirements ⟵ “The Bulldog Promise | Full tuition coverage | Open to first-year students who meet the Iowa residency requirements | FAFSA Application*”
### `6cc10d8bc60ea264` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Amounts vary ⟵ “Actuarial Science Scholarships | Amounts vary | Open to first-year actuarial science students | Application”
  - eligibility_summary: Open to first-year actuarial science students ⟵ “Actuarial Science Scholarships | Amounts vary | Open to first-year actuarial science students | Application”
### `6f4547be3129d6bb` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Up to 40% of the total cost of attendance per year ⟵ “International Student Grant | Up to 40% of the total cost of attendance per year | Open to first-year or new transfer international students of any major | Application”
  - eligibility_summary: Open to first-year or new transfer international students of any major ⟵ “International Student Grant | Up to 40% of the total cost of attendance per year | Open to first-year or new transfer international students of any major | Application”
### `807f3b8bbdd3a685` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Amounts vary ⟵ “Business Scholarships | Amounts vary | Open to first-year Zimpleman College of Business students | Application”
  - eligibility_summary: Open to first-year Zimpleman College of Business students ⟵ “Business Scholarships | Amounts vary | Open to first-year Zimpleman College of Business students | Application”
### `874ebb58583b4191` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 per year ⟵ “Bahamas Scholarship | $5,000 per year | Open to first-year or new transfer international students of any major from the Bahamas | Automatically awarded*”
  - eligibility_summary: Open to first-year or new transfer international students of any major from the Bahamas ⟵ “Bahamas Scholarship | $5,000 per year | Open to first-year or new transfer international students of any major from the Bahamas | Automatically awarded*”
### `892795f2464b3d3a` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Amounts Vary ⟵ “Education Scholarships | Amounts Vary | Open to entering first year or transfer students must be pursuing an undergraduate degree in the School of Education | Application”
  - eligibility_summary: Open to entering first year or transfer students must be pursuing an undergraduate degree in the School of Education ⟵ “Education Scholarships | Amounts Vary | Open to entering first year or transfer students must be pursuing an undergraduate degree in the School of Education | Application”
### `b0e9467d22eedabd` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Full tuition coverage ⟵ “Bright College Pathway | Full tuition coverage | Open to first-year students who meet the Iowa residency requirements | FAFSA Application*”
  - eligibility_summary: Open to first-year students who meet the Iowa residency requirements ⟵ “Bright College Pathway | Full tuition coverage | Open to first-year students who meet the Iowa residency requirements | FAFSA Application*”
### `b0f2f550f7ee0edc` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Amounts Vary ⟵ “Journalism Scholarships | Amounts Vary | Open to current and incoming School of Journalism & Mass Communication Undergraduate students | Application”
  - eligibility_summary: Open to current and incoming School of Journalism & Mass Communication Undergraduate students ⟵ “Journalism Scholarships | Amounts Vary | Open to current and incoming School of Journalism & Mass Communication Undergraduate students | Application”
### `bfc9945ead8909b0` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Amounts vary ⟵ “Theatre Fine Arts Scholarship | Amounts vary | Open to first-year or transfer fine arts students | Application and Audition”
  - eligibility_summary: Open to first-year or transfer fine arts students ⟵ “Theatre Fine Arts Scholarship | Amounts vary | Open to first-year or transfer fine arts students | Application and Audition”
### `f93fe5537e44caef` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: $5,000 per year ⟵ “Community of Digital Excellence (CODE) Scholarship | $5,000 per year | Open to first-year students studying in specific majors | Application”
  - eligibility_summary: Open to first-year students studying in specific majors ⟵ “Community of Digital Excellence (CODE) Scholarship | $5,000 per year | Open to first-year students studying in specific majors | Application”
### `f9deebfaba0fcd33` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: $26,000–$36,500 per year ⟵ “Presidential Scholarship | $26,000–$36,500 per year | Open to first-year students of any major | Automatically awarded”
  - eligibility_summary: Open to first-year students of any major ⟵ “Presidential Scholarship | $26,000–$36,500 per year | Open to first-year students of any major | Automatically awarded”
### `fc90a480ec6f93c8` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: Amounts vary ⟵ “Art & Design Fine Arts Scholarship | Amounts vary | Open to first-year or transfer fine arts students | Application and Portfolio submission”
  - eligibility_summary: Open to first-year or transfer fine arts students ⟵ “Art & Design Fine Arts Scholarship | Amounts vary | Open to first-year or transfer fine arts students | Application and Portfolio submission”
### `fe7d7bfd8533249a` Drake University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/scholarships (sha256 37be584ea9be)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 per year ⟵ “Hebei Province Scholarship | $3,000 per year | Open to first-year or new transfer international students of any major in the Hebei Province in China | Automatically awarded*”
  - eligibility_summary: Open to first-year or new transfer international students of any major in the Hebei Province in China ⟵ “Hebei Province Scholarship | $3,000 per year | Open to first-year or new transfer international students of any major in the Hebei Province in China | Automatically awarded*”
### `mef04d42f7bbe8a7` Drake University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/transfer-students/transfer-credit (sha256 2a2f74bedee5)
- checks: {"fields": ["max_transfer_credits", "residency_requirement_credits"], "merged_pages": 2}
  - max_transfer_credits: 66 ⟵ “A maximum of 66 semester hours of credit may be transferred from two-year institutions.”
  - residency_requirement_credits: 30 ⟵ “A minimum of 30 semester hours must be completed while in residence to earn a Drake degree.”
  - max_transfer_credits: 66 ⟵ “A maximum of 66 semester hours of credit may be transferred from two-year institutions.”
  - max_transfer_credits: 66 ⟵ “A maximum of 66 semester hours of credit may be transferred from two-year institutions.”
  - residency_requirement_credits: 30 ⟵ “A minimum of 30 semester hours must be completed while in residence to earn a Drake degree.”
  - residency_requirement_credits: 30 ⟵ “A minimum of 30 semester hours must be completed while in residence at Drake.”
### `43d94ac02e3461fe` Eastern Iowa Community College District — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://eicc.edu/admission-aid/applying-enrolling/cpl/ap.aspx (sha256 d9a2f6d67142)
- checks: {"distinct_exams": 23, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3]:  ⟵ “Studio Art: Drawing Portfolio | 3 | 3 | ART:133 Drawing”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | 3 | ART:101 Art Appreciation”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | 3 | ENG:105 Composition I”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | 6 | ENG:105 & LIT:101 Composition I and Introduction to Literature”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics | 3 | 3 | POL:125 Comparative Government & Politics”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | IPXX3 International Perspective Elective”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | 6 | HIS:118 Western Civilization II andHIS:119 Western Civilization III”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 3 | ECN:120 Principles of Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 3 | ECN:130 Principles of Microeconomics”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government & Politics | 3 | 3 | POL:111 American National Government”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History | 3 | 3 | HIS:151 U.S. History to 1877”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | 3 | PSY:111 Introduction to Psychology”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History | 3 | 3 | WPXX3 Western Perspective Elective”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 4 | MAT:210 Calculus I”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 4 | MAT:210 Calculus I”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | 8 | MAT:210 Calculus I andMAT:216 Calculus II”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | 3 | MAT:156 Statistics”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 | BIO:114 Biology IA”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHM:165 General Chemistry I”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 4 | ENV:111 Environmental Science”
  - equivalencies[AP-PHYSICS-1|3]:  ⟵ “Physics I | 3 | 4 | PHY:162 College Physics I”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | 8 | FLF:141 & 142 Elementary French I & II”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture | 3 | 8 | FLG:141 & 142 Elementary German I & II”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language & Culture | 3 | 8 | FLS:141 & 142 Elementary Spanish I & II”
### `d7d3492190b7a78b` Eastern Iowa Community College District — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://eicc.edu/admission-aid/applying-enrolling/cpl/clep.aspx (sha256 d4e79a3a9c9f)
- checks: {"distinct_exams": 24, "equivalencies": 26, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature without essay | 50 | 3 | LIT:110 American Literature to Mid-1800's”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 | ENG:105 Composition I”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | Humanities Electives”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language (Level I & II) | 50 | 8 | FLF:141 & 142 Elementary French I & II”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “French Language (Level I & II) | 62 | 14 | FLF:141, 142, 231 & 232 Elementary French I & II and Intermediate French I & II”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language (Level I & II) | 50 | 8 | FLG:141 & 142 Elementary German I & II”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language (Level I & II) | 50 | 8 | FLS:141 & 142 Elementary Spanish I & II”
  - equivalencies[CLEP-SPANISH-LANGUAGE|66]:  ⟵ “Spanish Language (Level I & II) | 66 | 14 | FLS:141, 142, 231 & 232 Elementary Spanish I & II and Intermediate Spanish I & II”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | POL:111 American National Government”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PSY:121 Developmental Psychology”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | 3 | PSY:281 Educational Psychology”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | PSY:111 Introduction to Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | SOC:110 Introduction to Sociology”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 | ECN:120 Principles of Macroeconomics”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 | ECN:130 Principles of Microeconomics”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|60]:  ⟵ “Social Sciences and History | 60 | 6 | Social Sciences Electives”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 8 | BIO:114 & 115 General Biology IA & IIA”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 4 | MAT:210 Calculus I”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 8 | CHM:165 & 175 General Chemistry I & II”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 4 | MAT:121 College Algebra”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 4 | MAT:128 PreCalculus”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|60]:  ⟵ “College Mathematics | 60 | 6 | Math Electives”
  - equivalencies[CLEP-NATURAL-SCIENCES|60]:  ⟵ “Natural Sciences | 60 | 6 | Natural Sciences Electives”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BUS:185 Business Law I”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 | MGT:101 Principles of Management”
  - … 1 more rows
### `43d8417463803722` Emmaus Bible College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.emmaus.edu/credit-transfer-policy (sha256 85d3def1ed02)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Students must earn a grade of C or better for the transfer of undergraduate courses completed within the last fifteen years or must earn a B or better in order to transfer credits completed within the past thirty years.”
### `5b072e60bae9e164` Graceland University-Lamoni — awards 2026-27 [new] (labeled_in_heading)
- source: https://www.graceland.edu/admissions-aid/tuition-financial-aid/tuition-and-fees/ (sha256 ad097eddb0f0)
- checks: {"thresholds": null}
  - award_amount_text: 1,000 ⟵ “Student Employment (students must work to earn) | 1,000”
### `aa9c1c13da9271f3` Graceland University-Lamoni — awards 2026-27 [new] (labeled_in_heading)
- source: https://www.graceland.edu/admissions-aid/tuition-financial-aid/tuition-and-fees/ (sha256 ad097eddb0f0)
- checks: {"thresholds": null}
  - award_amount_text: 8,395 ⟵ “Federal/State Grants | 8,395”
### `d008941b62e7cd51` Graceland University-Lamoni — awards 2026-27 [new] (labeled_in_heading)
- source: https://www.graceland.edu/admissions-aid/tuition-financial-aid/tuition-and-fees/ (sha256 ad097eddb0f0)
- checks: {"thresholds": null}
  - award_amount_text: $11,000 ⟵ “Graceland Scholarships | $11,000”
### `e594da91c90c2527` Graceland University-Lamoni — awards 2026-27 [new] (labeled_in_heading)
- source: https://www.graceland.edu/admissions-aid/tuition-financial-aid/tuition-and-fees/ (sha256 ad097eddb0f0)
- checks: {"thresholds": null}
  - award_amount_text: 2,400 ⟵ “Outside Scholarship(s) | 2,400”
### `fc8daf7e4e5748ec` Graceland University-Lamoni — awards 2026-27 [new] (labeled_in_heading)
- source: https://www.graceland.edu/admissions-aid/tuition-financial-aid/tuition-and-fees/ (sha256 ad097eddb0f0)
- checks: {"thresholds": null}
  - award_amount_text: $28,295 ⟵ “TOTAL | $28,295”
### `10400cfc0a412879` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The Education and Training Voucher (ETV) Grant is a federally-funded program to provide post-secondary education and training opportunities to students who are currently or who have been in foster care. Students must complete a FAFSA, complete a state application and taking at least 3 credit hours. Students can be funded until the age of 23 provided they were participating in the ETV program by age 21. Iowa College Student Aid Commission selects the award recipients. Awards are prorated for students enrolling less than full-time. ⟵ “Iowa Education and Training Voucher | The Education and Training Voucher (ETV) Grant is a federally-funded program to provide post-secondary education and training opportunities to students who are currently or who have been in foster care. Students must complete a FAFSA, complete a state applicatio”
### `12e8c81e48c2af52` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Established in honor of former Bishop Philip L. Hougen, awarded to a selected number of applicants from Lutheran congregations who express intention to participate regularly in Grand View Campus Ministry. Awards range between $500 – $1,500 and are renewable based on maintaining a full-time day enrollment and participation in campus ministry activities. Application deadline: March 1 Apply Here ⟵ “Philip L. Hougen Campus Ministry Scholarship | Established in honor of former Bishop Philip L. Hougen, awarded to a selected number of applicants from Lutheran congregations who express intention to participate regularly in Grand View Campus Ministry. Awards range between $500 – $1,500 and are renew”
### `1a3b08b9643e7947` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: You could qualify for an Art & Design Scholarship ranging from $750 - $3,000. Scholarships are available to new, full-time students at Grand View majoring in Art Education, Game Design, Graphic Design or Studio Arts. Art Scholarship Days are held several times per year. During those events, student will bring art work for a portfolio review with art and design faculty members as well as have additional options of sitting in on an art class, meeting with admissions and doing a campus tour. Art & Design Scholarships are renewable based on continued full-time day enrollment as in Art Education, Game Design, Graphic Design or Studio Arts major at Grand View. ⟵ “Art & Design Scholarship | You could qualify for an Art & Design Scholarship ranging from $750 - $3,000. Scholarships are available to new, full-time students at Grand View majoring in Art Education, Game Design, Graphic Design or Studio Arts. Art Scholarship Days are held several times per year. Du”
### `1bb93926ece1bd52` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: This scholarship help students in their pursuit of an Art Education degree. Selected by the Art Education faculty, this $1,000 renewable award for students majoring in Art Education. Preference is given to those students majoring in Art Education and English. ⟵ “Marsha A. Conboy Shining Star Scholarship | This scholarship help students in their pursuit of an Art Education degree. Selected by the Art Education faculty, this $1,000 renewable award for students majoring in Art Education. Preference is given to those students majoring in Art Education and Engli”
### `2b97c16738b88ddb` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Incoming first-year students with an interest in Grand View's Kinesiology or Pre-Athletic Training programs who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship. Students must participate in one of Grand View's Scholarship Day events in November or February. The Kinesiology Honors Scholarship is renewable for a total of four years if the student maintains: Full-time day enrollment status Continuous enrollment in a Grand View Kinesiology program Learn More about Scholarship Day ⟵ “Kinesiology Honors Scholarship | Incoming first-year students with an interest in Grand View's Kinesiology or Pre-Athletic Training programs who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship. Students must participate in one of Grand View's Scholarship”
### `3cc9cccf8679c989` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: A four-year renewable scholarship of $1,000 awarded to new full-time day first-year or transfer students whose parent(s) received either an associate, bachelor's or master's degree at Grand View. ⟵ “Alumni Scholarship | A four-year renewable scholarship of $1,000 awarded to new full-time day first-year or transfer students whose parent(s) received either an associate, bachelor's or master's degree at Grand View.”
### `418d4f75909ac67d` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The ISL Education Lending Scholarship awards 45 deposits of $1,000 into College Savings Iowa accounts for Iowa residents in high school or undergraduate college, or the parents, guardians or others who hold a College Savings Iowa account for high school or undergraduate college student. Application deadline: April 3 Learn More View Informational Flyer ⟵ “ISL Education Lending Scholarship | The ISL Education Lending Scholarship awards 45 deposits of $1,000 into College Savings Iowa accounts for Iowa residents in high school or undergraduate college, or the parents, guardians or others who hold a College Savings Iowa account for high school or undergr”
### `443d45e54d449427` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The All Iowa Opportunity Scholarship Program is awarded to students that are taking at least 3 credit hours, completed a FAFSA, completed a state application at www.iowacollegeaid.gov and are an Iowa resident. Iowa College Student Aid Commission selects the award recipients. Awards are prorated for students enrolling on a less than full-time basis. ⟵ “All Iowa Opportunity Scholarship | The All Iowa Opportunity Scholarship Program is awarded to students that are taking at least 3 credit hours, completed a FAFSA, completed a state application at www.iowacollegeaid.gov and are an Iowa resident. Iowa College Student Aid Commission selects the award r”
### `4b4eda9361010645` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Up to $13,000 ⟵ “Grand View Grant | Up to $13,000”
### `50368c791f6b7a89` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Incoming first-year students who are participating in the Des Moines Public School’s Dream to Teach program and who have a 3.25 or higher high school GPA and plan to pursue a degree in education, may apply for the Dream to Teach Scholarship. The Dream to Teach Scholarship awards full tuition plus the following fees: technology, student activity. It will also cover room charges and the resident activity fee to live in Knudsen or Nielsen Hall if living on campus. The scholarship is renewable for a total of four years if the student maintains full-time day enrollment status and continuous enrollment in an education program. Application deadline: March 1 Apply Here ⟵ “Dream to Teach Scholarship | Incoming first-year students who are participating in the Des Moines Public School’s Dream to Teach program and who have a 3.25 or higher high school GPA and plan to pursue a degree in education, may apply for the Dream to Teach Scholarship. The Dream to Teach Scholarshi”
### `5aacae2720cdeca1` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Incoming first-year students with an interest in one of Grand View's science, technology, pre-engineering, or math (STEM) programs who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship. Students must participate in one of Grand View's Scholarship Day events in November or February. The STEM Honors Scholarship is renewable for a total of four years if the student maintains: Full-time day enrollment status Continuous enrollment in a Grand View STEM program Learn More about Scholarship Day ⟵ “STEM Honors Scholarship | Incoming first-year students with an interest in one of Grand View's science, technology, pre-engineering, or math (STEM) programs who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship. Students must participate in one of Grand Vi”
### `6894bcbab8b4de0f` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Grand View offers a competitive Esports program, which offers scholarships to a limited number of program participants. Scholarships are renewable each year based on continued good standing with the Esports program. ⟵ “Esports Scholarship | Grand View offers a competitive Esports program, which offers scholarships to a limited number of program participants. Scholarships are renewable each year based on continued good standing with the Esports program.”
### `6fb922f3f7f416f2` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Grand View University values study abroad experiences and offer scholarships to students taking these trips. Through the Alice (Olsen ’60) and Dan Mikel ’60 Endowed Scholarship, The Merv E. Bro Scholarship, The Thorup Scholarship, and the Joan and Bertram Stivers Scholarship, students can apply for scholarship dollars to finance a portion of their travel experience. Apply Here Application deadlines: April 1 for summer and fall semester study abroad programs/yearlong study abroad programs October 15 for spring semester study abroad programs November 21 for Grand View hosted May Term trips ⟵ “Study Abroad/Study Trip Scholarships | Grand View University values study abroad experiences and offer scholarships to students taking these trips. Through the Alice (Olsen ’60) and Dan Mikel ’60 Endowed Scholarship, The Merv E. Bro Scholarship, The Thorup Scholarship, and the Joan and Bertram Stive”
### `723ae640853d9e08` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 is awarded to full-time day students who have participated in a high school all-state festival for at least one year and demonstrate talent in piano, vocal and instrumental music regardless of major. The All-State Music Scholarship is renewable based on participation in both an ensemble and private lessons with continuous good standing in both areas. ⟵ “All-State Music Scholarship | $1,500 is awarded to full-time day students who have participated in a high school all-state festival for at least one year and demonstrate talent in piano, vocal and instrumental music regardless of major. The All-State Music Scholarship is renewable based on participa”
### `745410fb063c4cb0` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: This scholarship, established in 2013 by Grand View University’s National Alumni Council (NAC), is designed to assist students in reaching their educational goals. It is the donors’ hope that the recipients of this scholarship will seek to better their lives, and be positive role models for others as they work to improve their communities. NAC awards an annual $1,000 scholarship that is paid as two equal payments in the fall and spring semesters of the upcoming academic year. Application deadline: April 24 Apply Here ⟵ “National Alumni Council Scholarship | This scholarship, established in 2013 by Grand View University’s National Alumni Council (NAC), is designed to assist students in reaching their educational goals. It is the donors’ hope that the recipients of this scholarship will seek to better their lives, an”
### `79771ad6bf4a9b67` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Up to $19,000 ⟵ “Dean's Scholarship | Up to $19,000”
### `7ef070fda8075c9d` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Prospective or incoming first-year students with an interest in social work who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship. Students must participate in the Social Work and Honors Program and participate in one of Grand View’s Scholarship Day events in November or February. The Social Work Honors Scholarship is renewable for a total of four years if the student maintains: Full-time day enrollment status Continuous enrollment in the pre-social work or social work programs Learn More about Scholarship Day ⟵ “Social Work Honors Scholarship | Prospective or incoming first-year students with an interest in social work who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship. Students must participate in the Social Work and Honors Program and participate in one of Gr”
### `817dd2d01775c733` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: A renewable $1,000 scholarship available to alumni of the Lutheran Music Program (Lutheran Summer Music) for students majoring in music, music education, or church music. Recipients may also audition for an additional Pro Musica Scholarship. ⟵ “Lutheran Music Program Scholarship | A renewable $1,000 scholarship available to alumni of the Lutheran Music Program (Lutheran Summer Music) for students majoring in music, music education, or church music. Recipients may also audition for an additional Pro Musica Scholarship.”
### `85ed75da15b4a569` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Grand View will match the $2,500 scholarships that are awarded by Prairie Meadows for students that enroll at Grand View. This match is for the first year only. ⟵ “ICF - Prairie Meadows Scholarship | Grand View will match the $2,500 scholarships that are awarded by Prairie Meadows for students that enroll at Grand View. This match is for the first year only.”
### `905fec505f513198` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Grand View is a member of the National Association of Intercollegiate Athletics (NAIA) and offers athletic scholarships in archery, baseball, basketball, bowling, competitive cheer, cross country, football, golf, shotgun, soccer, tennis, track & field, volleyball, and wrestling for men, and archery, basketball, bowling, competitive cheer, competitive dance, cross country, golf, shotgun, soccer, softball, tennis, track & field, and volleyball, and wrestling for women. Scholarships begin at $500 and are based on athletic ability as evaluated by the coaches. Athletic scholarships are renewable each year based on continued good standing within the athletic program. ⟵ “Athletic Scholarship | Grand View is a member of the National Association of Intercollegiate Athletics (NAIA) and offers athletic scholarships in archery, baseball, basketball, bowling, competitive cheer, cross country, football, golf, shotgun, soccer, tennis, track & field, volleyball, and wrestlin”
### `a354d0ab433b3a49` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: A four-year renewable scholarship of $1,000 awarded to new, full-time day first-year or transfer students who are referred by GV alumni who have received a bachelor's or master's degree at Grand View. Alumni Referral Scholarship Nomination Form ⟵ “Alumni Referral Scholarship | A four-year renewable scholarship of $1,000 awarded to new, full-time day first-year or transfer students who are referred by GV alumni who have received a bachelor's or master's degree at Grand View. Alumni Referral Scholarship Nomination Form”
### `ace0eb6cc81fb303` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The Catalyst Scholarship is intended to support the education of a full-time student majoring in social work who shows promise as a strong catalyst for change. Students must meet these qualifications: Admitted to the social work program Enrolled in at least the first full year after acceptance to the major 3.0 cumulative grade point average at Grand View Applicants must submit an essay indicating how they see themselves as catalysts for change, both as students and as future social workers. Application deadline: September 30 Apply Here ⟵ “Catalyst Scholarship | The Catalyst Scholarship is intended to support the education of a full-time student majoring in social work who shows promise as a strong catalyst for change. Students must meet these qualifications: Admitted to the social work program Enrolled in at least the first full year”
### `b54f3201dcb4a0b5` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The Jacob F. Opel Memorial Scholarship is available to sophomores, juniors and seniors who are studying nursing and business and are US citizens. Two $2,000 scholarships will be awarded. Must be a graduate of Des Moines Public Schools. Application deadline: December 13 Apply Here ⟵ “Jacob F. Opel Memorial Scholarship | The Jacob F. Opel Memorial Scholarship is available to sophomores, juniors and seniors who are studying nursing and business and are US citizens. Two $2,000 scholarships will be awarded. Must be a graduate of Des Moines Public Schools. Application deadline: Decem”
### `b8c807791fe04b97` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: First-year and transfer students who have applied and been accepted to Grand View are invited to interview/audition for scholarships offered by the Theatre Arts Department. Theatre Arts Scholarships are awarded at varying levels: Major, minor and interest, in amounts starting at $1,000 annually. ⟵ “Theatre Arts Scholarship | First-year and transfer students who have applied and been accepted to Grand View are invited to interview/audition for scholarships offered by the Theatre Arts Department. Theatre Arts Scholarships are awarded at varying levels: Major, minor and interest, in amounts start”
### `c55d2f88d4affe48` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Up to $15,000 ⟵ “GV Scholar's Award | Up to $15,000”
### `c853d0a9a89a9b57` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The Discover Iowa Award is a $1,000 award offered to new first-year students from out of state who visit campus through an individual admissions visit or admissions event. Admissions events that qualify for this award include: academic actions days, admissions preview days, scholarship day events, and admissions visit days. One $1,000 award offered per student and the award is renewable for 4 years. Register for an admissions event. ⟵ “Discover Iowa Award | The Discover Iowa Award is a $1,000 award offered to new first-year students from out of state who visit campus through an individual admissions visit or admissions event. Admissions events that qualify for this award include: academic actions days, admissions preview days, sch”
### `d913291d5977c311` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: In partnership with Latinos Unidos of Iowa, Grand View University will match a Latinos Unidos of Iowa scholarship of up to $1,000 per year for a student enrolling as a full-time day undergraduate student for a maximum of four years. The match for the first year will be credited to the student account when the Latinos Unidos of Iowa Scholarship is received. If the student attends another institution before transferring to Grand View, they will only be awarded the Grand View matching award if they have not used their Latinos Unidos of Iowa Scholarship at another institution. Learn More ⟵ “Latinos Unidos of Iowa Scholarship | In partnership with Latinos Unidos of Iowa, Grand View University will match a Latinos Unidos of Iowa scholarship of up to $1,000 per year for a student enrolling as a full-time day undergraduate student for a maximum of four years. The match for the first year w”
### `dc3cdff682cf5f54` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The All Iowa Opportunity Foster Care Grant is awarded to students who were previously adjudicated in the Iowa foster care system and are taking at least 3 credit hours, completed a FAFSA, completed a state application at www.iowacollegeaid.gov and are an Iowa resident. Iowa College Student Aid Commission selects the award recipients. Awards are prorated for students enrolling less than full-time and based on the student’s enrollment status. Eligibility for this program ends when a student turns age 24. ⟵ “All Iowa Opportunity Foster Care Grant | The All Iowa Opportunity Foster Care Grant is awarded to students who were previously adjudicated in the Iowa foster care system and are taking at least 3 credit hours, completed a FAFSA, completed a state application at www.iowacollegeaid.gov and are an Iowa”
### `ddf8dc0888c4d16c` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The Iowa National Guard Education Assistance Program (NGEAP) provides funds to members of the Iowa National Guard units. Soldiers or Airmen must be an active member of the Iowa Army or Air National Guard, be a resident of the state of Iowa, and have satisfactorily completed initial entry training. Soldiers or Airmen cannot have met the academic requirements for a baccalaureate degree or received NGEAP for more than 120 semester hours. Applications should be submitted to www.iowacollegeaide.gov on or before July 1 through the Iowa Financial Aid Application. Spring-only applicants should submit their applications on or before December 1. The Adjutant General of Iowa selects eligible recipients. ⟵ “Iowa National Guard Education Assistance | The Iowa National Guard Education Assistance Program (NGEAP) provides funds to members of the Iowa National Guard units. Soldiers or Airmen must be an active member of the Iowa Army or Air National Guard, be a resident of the state of Iowa, and have satisfa”
### `e24a0ff167236edd` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Incoming first-year students who quality and participate in the GV Honors program and who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship by attending one of Grand View’s Scholarship Day events in November or February. The GV Honors Scholarship is renewable for a total of four years if the student maintains full-time day enrollment status and continuous enrollment in the program. Learn More about Scholarship Day ⟵ “GV Honors Scholarship | Incoming first-year students who quality and participate in the GV Honors program and who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship by attending one of Grand View’s Scholarship Day events in November or February. The GV Hono”
### `e267519e98652c75` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: The Doidge Endowed Biology Scholarship was created to support pre-professional or science majors in their junior or sophomore year of class standing. The scholarship is given to students with a 3.0 cumulative grade point average or higher who have shown financial need as defined by the Free Application for Federal Student Aid (FAFSA). Application deadline: April 28 Apply Here ⟵ “Lee and Diane (Gill '76) Doidge Endowed Biology Scholarship | The Doidge Endowed Biology Scholarship was created to support pre-professional or science majors in their junior or sophomore year of class standing. The scholarship is given to students with a 3.0 cumulative grade point average or higher”
### `e698b273ab201432` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: A volunteer-driven national network of more than 1,260 community-based scholarship foundations serving nearly 4,000 communities across the U.S. in support of local students. Grand View will match up to $500. ⟵ “Dollars for Scholars | A volunteer-driven national network of more than 1,260 community-based scholarship foundations serving nearly 4,000 communities across the U.S. in support of local students. Grand View will match up to $500.”
### `eb258188359d3f9b` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: Prospective or incoming first-year students with an interest in nursing who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship. Students must participate in the Nursing and Honors Program and participate in one of Grand View’s Scholarship Day events in November or February. The Nursing Honors Scholarship is renewable for a total of four years if the student maintains: Full-time day enrollment status Continuous enrollment in the pre-nursing and nursing program Learn More about Scholarship Day ⟵ “Nursing Honors Scholarship | Prospective or incoming first-year students with an interest in nursing who have a 3.85 or higher high school GPA may compete for a $5,000 annually renewable scholarship. Students must participate in the Nursing and Honors Program and participate in one of Grand View’s S”
### `f18610cabe34be52` Grand View University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid/scholarships-grants (sha256 085dac122c0e)
- checks: {"thresholds": null}
  - award_amount_text: A scholarship available to selected new full-time day students who demonstrate talent in piano, vocal and instrumental music regardless of major. Scholarships range from $500 – $4,000. The music scholarship is renewable based on participation in both an ensemble and private lessons with continuous good standing in both areas. ⟵ “Musical Arts Scholarship | A scholarship available to selected new full-time day students who demonstrate talent in piano, vocal and instrumental music regardless of major. Scholarships range from $500 – $4,000. The music scholarship is renewable based on participation in both an ensemble and privat”
### `085cd22236229348` Grand View University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.grandview.edu/admissions/transfer/transfer-credit-policy (sha256 12c4a5651cb0)
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “Cross enroll courses do not interrupt nor add to the last 30 hours of Grand View requirements.”
### `02f6317de03fdfdf` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $300 ⟵ “Dental Community Scholarship (Dr. Richard Haw Dental Hygiene) | $300 | Spring | October 1”
### `0b19735da525ca97` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Denver Cyclone | $500 | Fall | February 1”
### `0c1ec91d0fd6b8c1` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000$500 ⟵ “Harlan & Betty Van Gerpen Health Science Scholarship | $1,000$500 | FallFall & Spring | February 1February 1 & October 1”
### `157fc4113d9236b2` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Black Hawk County Law Enforcement | $1,000 | Spring | October 1”
### `19dccbdb3788438f` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $250 ⟵ “Rocky Fratzke Memorial | $250 | Fall | February 1”
### `1c463cd1e42b7ef0` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $400 ⟵ “Malcolm McGregor | $400 | Fall | February 1”
### `1c7017495d8f069f` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Tripoli Community School Alumni | $500 | Fall & Spring | February 1 & October 1”
### `218c612417550a99` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $750 ⟵ “Brian Harrington, Sons of Amvets Post 49 | $750 | Fall | February 1”
### `23148b579a1c17e3` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Farm Credit Services of America Agriculture | $1,000 | Fall | February 1”
### `29339524ccdb14a6` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: Tuition ⟵ “William & Edna Fennemann | Tuition | Fall | February 1”
### `2aec113153089acc` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Darlene Culpepper Nursing | $500 | Spring | October 1”
### `2e33b3ab53712fe5` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Marie & Raymond Howsare | $1,000 | Fall | February 1”
### `35528a65b0f9cbc0` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “American Legion of Iowa | $1,000 | Fall | February 1”
### `3b7a828b0eea1321` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Woody Stingley (CNC) | $1,000 | Fall | February 1”
### `44b2f3688d5b8197` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $600 ⟵ “Steve & Donita Dust | $600 | Fall | February 1”
### `484109052bda1b2a` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: 50% Tuition & Fees ⟵ “Paul J. Frazier | 50% Tuition & Fees | Fall & Spring | February 1 & October 1”
### `4a1e75c0be39305d` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Jean Dunbar Nursing Scholarship | $1,000 | Fall | February 1”
### `4bfeb124e0416dba` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Express Pro's | $500 | Spring | October 1”
### `4e558750daf720f3` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $250 ⟵ “Horticulture | $250 | Fall | February 1”
### `528b142869e8b4a6` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Kenneth Bienfang & Harold Bienfang | $500 | Fall | February 1”
### `56f93d8b01a378f0` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $350 ⟵ “Early Childhood Education | $350 | Spring | October 1”
### `570dd61397f69a8a` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Pauline Barrett Nursing | $500 | Fall & Spring | February 1 & October 1”
### `59fd2d8bc342f179` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Jerry Greenlee Sr. BCPOA Endowed | $500 | Fall | February 1”
### `5b6181bd39ffc929` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Ike Leighty | $1,000 | Spring | October 1”
### `5bfe7a137dbefea9` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $250 ⟵ “PAS Leadership | $250 | Fall | February 1”
### `60a767e19bab0b45` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $750 ⟵ “GROWMARK Agriculture | $750 | Fall | February 1”
### `60e38bd55127f9f2` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Hawkeye Pride Organization | $500 | Fall | February 1”
### `6c2c05828c15cad5` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Virginia Winter | $500 | Fall & Spring | February 1 & October 1”
### `6d8da533103da076` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Rick Harned Memorial | $500 | Fall & Spring | February 1 & October 1”
### `6ed6b4d41f535794` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Electronic Engineering Technology | $500 | Fall & Spring | February 1 & October 1”
### `6faf06a855bce0c7` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Future Collision & Refinishing Technicians | $500 | Spring | October 1”
### `70183096141cd575` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Aspro | $1,000 | Fall | February 1”
### `74581f48b8b19638` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Marvin and Lora Kramer | $1,000 | Spring | October 1”
### `779ea1326bcb02b7` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $850 ⟵ “Buckles | $850 | Fall | February 1”
### `7b952a166ebb5712` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “James & Caroline Martin | $500 | Fall | February 1”
### `7e4f3c2f1cd8c8cf` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Student Activities | $1,000 | Fall | February 1”
### `813864b68e9e1c48` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “World Class Industries | $500 | Fall | February 1”
### `87ba133e90156f79` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $300 ⟵ “Todd Kinley Memorial | $300 | Fall | February 1”
### `88eb142ff740ce18` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Don Collinson | $500 | Fall | February 1”
### `9634f39f849abe64` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Mark & June Birdnow | $500 | Fall | February 1”
### `97c7c836a4cc3683` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Nelson & Leighty–Engineered Products Co. Scholarship Fund | $1,000 | Fall | February 1”
### `98932ef21ffbb76a` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Tommy Burns (Waterloo Schools Alumni) | $1,000 | Fall | February 1”
### `99788f2880b11282` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Jerry & JoAnn Jensen Memorial | $500 | Fall | February 1”
### `99bd2d2630c0d37d` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “WITS | $500 | Fall | February 1”
### `9ab13a482cf65b76` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $600 ⟵ “Bruce Haugland Power Technology | $600 | Fall | February 1”
### `9c53fe69e1680722` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “David Crowe Memorial Veteran Scholarship | $500 | Spring | October 1”
### `a5ae2dbf3f0f1232` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Friendship Village Retirement Center | $1,000 | Fall & Spring | February 1 & October 1”
### `a94ca33600a8a745` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “FBG Service Corp. | $1,000 | Fall | February 1”
### `ac8f1a70d8631de8` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Virgil Christensen | $500 | Fall | February 1”
### `adcaf3e834d08fbf` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $300 ⟵ “Jimmy Robinson | $300 | Fall & Spring | February 1 & October 1”
### `ae6a4f853f560201` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Woody Stingley (Network Administration & Engineering) | $1,000 | Fall | February 1”
### `afef55d2c5889227` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 ⟵ “Lloyd R. Dilley & Donald L. Dilley Memorial | $2,500 | Fall & Spring | February 1 & October 1”
### `b055336d26458746` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Andrew & Marlys Puhl Memorial | $1,000 | Fall | February 1”
### `b0fac95748d78ec7` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $750 ⟵ “Larry Williams Scholarship, Sons of Amvets Post 49 (Hospitality Management) | $750 | Fall | February 1”
### `b3274fdaaaa979da` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Richard Brian Gienau Memorial | $500 | Fall & Spring | February 1 & October 1”
### `b90374d8fe72ffd2` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $600 ⟵ “Steve & Donita Dust Scholarship | $600 | Fall | February 1”
### `bd05226b0d851673` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Ida Fleming Nursing | $500 | Fall & Spring | February 1 & October 1”
### `be797649d2a6b683` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $250 ⟵ “Nursing Faculty in Memory of T.P. Cook & V. Smith | $250 | Fall & Spring | February 1 & October 1”
### `c29ba33f39541033` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $300 ⟵ “Travis Wittmayer Scholarship for the Profoundly Deaf | $300 | Fall & Spring | February 1 & October 1”
### `c864cabcd3e6b17c` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Woody Stingley (Accounting) | $1,000 | Fall | February 1”
### `cc1a66b5246442c7` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “Jim & Cecelia Mudd | $1,500 | Spring | October 1”
### `cffe2f890c54b32a` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $300 ⟵ “Dental Community Scholarship (Dental Assisting) | $300 | Spring | October 1”
### `d0fd66d43a38b3c9` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $250 ⟵ “Terri Cook Family Nursing | $250 | Fall & Spring | February 1 & October 1”
### `d718fc9afecf4064` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Dan Huck Memorial | $500 | Fall | February 1”
### `d8d8336bcfedb5d5` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Mike Tripolino Criminal Justice | $500 | Fall | February 1”
### `e22a513f9222f84b` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $350 ⟵ “V. Miller / Miller Medical | $350 | Fall | February 1”
### `e542f6d1e6c82c18` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Mary Kathleen Flynn Memorial | $1,000 | Fall | February 1”
### `e5685565ac5da8f5` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $300 ⟵ “Land O'Lakes | $300 | Fall | February 1”
### `e88b7dffb6c3100e` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Bob Kimm Judging | $1,000 | Fall | February 1”
### `e99a9fc59275c7dd` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $355.50 ⟵ “ETC: Art & Literary Magazine | $355.50 | Spring | October 1”
### `ea3d9aaa0aa3bcbe` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500$250 ⟵ “Mike Turner Memorial | $500$250 | SpringSummer | October 1”
### `eb02ba4a9a187671` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Robert M. Flynn Memorial Scholarship | $1,000 | Fall | February 1”
### `eb75b1a16e803c9b` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Tim Petersen Memorial | $500 | Fall & Spring | February 1 & October 1”
### `ece1d5ef88d778df` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $250 ⟵ “Cedar Valley Civitan | $250 | Fall & Spring | February 1 & October 1”
### `ed0b16e28dd7232e` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: Tuition ⟵ “William F. Mullikin Memorial | Tuition | Spring | October 1”
### `ef8aa71716b9a37e` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Associated General Contractors of Iowa | $1,000 | Spring | October 1”
### `f7008a339fff6b24` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $300 ⟵ “Walther Memorial | $300 | Fall | February 1”
### `f9272f14cf527954` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Robert D. Gunderson | $500 | Fall | February 1”
### `fe88a847671d9ab0` Hawkeye Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/hawkeye-scholarships (sha256 e434361278ec)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Natural Resources Outstanding Student | $500 | Varies | February 1 & October 1”
### `3a885bf738c1fce2` Iowa State University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.iastate.edu/admission-and-aid/admissions/first-year-students/credit-by-exam (sha256 3c561228a8ee)
- checks: {"distinct_exams": 37, "equivalencies": 49, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3-4]:  ⟵ “Art History | 3-4 | Art History 2800 | 3”
  - equivalencies[AP-DRAWING|4-5]:  ⟵ “Drawing | 4-5 | Design Studies 1310 | 4”
  - equivalencies[AP-2-D-ART-DESIGN|4-5]:  ⟵ “2-D Art & Design | 4-5 | Design Studies 1000T | 4”
  - equivalencies[AP-3-D-ART-DESIGN|4-5]:  ⟵ “3-D Art & Design | 4-5 | Design Studies 1020 | 4”
  - equivalencies[AP-BIOLOGY|4-5]:  ⟵ “Biology | 4-5 | Biology 1000 | 4”
  - equivalencies[AP-CHEMISTRY|4-5]:  ⟵ “Chemistry | 4-5 | Chemistry 1770, 1780 | 7”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 | Computer Science 1270 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|5]:  ⟵ “Computer Science A | 5 | Computer Science 1270 and 2270 | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4-5]:  ⟵ “Computer Science Principles | 4-5 | Computer Science 1000 | 3”
  - equivalencies[AP-MACROECONOMICS|3-5]:  ⟵ “Macroeconomics | 3-5 | Economics 1020 | 3”
  - equivalencies[AP-MICROECONOMICS|3-5]:  ⟵ “Microeconomics | 3-5 | Economics 1010 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3-5]:  ⟵ “English Language & Composition | 3-5 | English 1500 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4-5]:  ⟵ “English Literature & Composition | 4-5 | English 1000 or 1500 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3-5]:  ⟵ “Environmental Science | 3-5 | Environmental Studies 1000 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3-5]:  ⟵ “Human Geography | 3-5 | Social Science 1000 | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4-5]:  ⟵ “U.S. Government and Politics | 4-5 | Political Science 1110 | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|4-5]:  ⟵ “Comparative Government/Politics | 4-5 | Political Science 1250 | 3”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4-5]:  ⟵ “African American Studies | 4-5 | African American Studies 2010 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4-5]:  ⟵ “European History | 4-5 | History 2010, 2020 | 6”
  - equivalencies[AP-UNITED-STATES-HISTORY|4-5]:  ⟵ “United States History | 4-5 | History 2210, 2220 | 6”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4-5]:  ⟵ “World History: Modern | 4-5 | History 1000 | 6”
  - equivalencies[AP-CALCULUS-AB|4-5]:  ⟵ “Calculus AB | 4-5 | Math 1650 | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | Math 1650 | 4”
  - equivalencies[AP-CALCULUS-BC|4-5]:  ⟵ “Calculus BC | 4-5 | Math 1650, 1660 | 8”
  - equivalencies[AP-PRECALCULUS|4-5]:  ⟵ “Precalculus | 4-5 | Math 1430 | 4”
  - … 24 more rows
### `20ac938c30e38016` Iowa Western Community College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.iwcc.edu/financial-aid/cost-of-attendance/ (sha256 59ba6afc9497)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees (estimated): 7500 ⟵ “Tuition & Fees (estimated) | $7,350 | $7,500”
  - on_campus:Food & Housing: 9450 ⟵ “Food & Housing | $9,450 | $9,450”
  - on_campus:Books, Materials, Supplies, Equipment: 1500 ⟵ “Books, Materials, Supplies, Equipment | $1,500 | $1,500”
  - on_campus:Anticipated Personal Expenses: 3078 ⟵ “Anticipated Personal Expenses | $3,078 | $3,078”
  - on_campus:Anticipated Travel Expenses: 2331 ⟵ “Anticipated Travel Expenses | $2,331 | $2,331”
  - on_campus:Total Expected Cost of Attendance: 23859 ⟵ “Total Expected Cost of Attendance | $23,709 | $23,859”
  - on_campus:Total College Expense: 18450 ⟵ “Total College Expense | $18,300 | $18,450”
### `c2ad5d1932df2bb4` Iowa Western Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.iwcc.edu/financial-aid/cost-of-attendance/ (sha256 59ba6afc9497)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees (estimated): 7350 ⟵ “Tuition & Fees (estimated) | $7,350 | $7,500”
  - on_campus:Food & Housing: 9450 ⟵ “Food & Housing | $9,450 | $9,450”
  - on_campus:Books, Materials, Supplies, Equipment: 1500 ⟵ “Books, Materials, Supplies, Equipment | $1,500 | $1,500”
  - on_campus:Anticipated Personal Expenses: 3078 ⟵ “Anticipated Personal Expenses | $3,078 | $3,078”
  - on_campus:Anticipated Travel Expenses: 2331 ⟵ “Anticipated Travel Expenses | $2,331 | $2,331”
  - on_campus:Total Expected Cost of Attendance: 23709 ⟵ “Total Expected Cost of Attendance | $23,709 | $23,859”
  - on_campus:Total College Expense: 18300 ⟵ “Total College Expense | $18,300 | $18,450”
### `c04a1c9722a7af04` Iowa Western Community College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.iwcc.edu/students/records-and-registration/list-of-exams-accepted/ (sha256 8ffd11efe037)
- checks: {"distinct_exams": 24, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | POL 111 American National Government”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 | LIT 110 American Literature to Mid 1800sLIT 111 American Literature since Mid 1800s”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 8 | BIO 112 General Biology IBIO 113 General Biology II”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 5 | MAT 211 Calculus I”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 5 | CHM 166 General Chemistry I”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 4 | MAT 121 College Algebra”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition(with Essay) | 50 | 6 | ENG 105 Composition IENG 106 Composition II”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 6 | LIT 140 British Literature ILIT 141 British Literature II”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 | ACC 121 Principles of Accounting I”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Dev | 50 | 3 | PSY 121 Developmental Psychology”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | 3 | CSC 110 Introduction to Computers”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BUS 185 Business Law I”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | 3 | PSY 281 Educational Psychology”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | PSY 111 Introduction to Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | SOC 110 Introduction to Sociology”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Pre-Calculus | 50 | 5 | MAT 129 Pre-Calculus”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 | ECN 120 Principles of Macroeconomics”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of Management | 50 | 3 | MGT 101 Principles of Management”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of Marketing | 50 | 3 | MKT 110 Principles of Marketing”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 | ECN 130 Principles of Microeconomics”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language | 50 | 8 | FLS 141, 142 Elementary Spanish I & II”
  - equivalencies[CLEP-SPANISH-WITH-WRITING|50]:  ⟵ “Spanish with Writing | 50 | 8 | FLS 141, 142 Elementary Spanish I & II”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I | 50 | 3 | HIS 110 Western Civilization Ancient to Early Modern”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western Civilization II | 50 | 3 | HIS 111 Western Civilization Early Modern to Present”
### `1bcf7bcd352adad7` Loras College — awards 2026-27 [new] (labeled_in_source)
- source: https://loras.edu/scholarships/ (sha256 cdeb8efc05d6)
- checks: {"thresholds": null}
  - award_amount_text: $24,000 ⟵ “St. Raphael Scholarship | 3.40-3.79 | $24,000”
  - eligibility_summary: 3.40-3.79 ⟵ “St. Raphael Scholarship | 3.40-3.79 | $24,000”
### `4a8f486746a07143` Loras College — awards 2026-27 [new] (labeled_in_source)
- source: https://loras.edu/scholarships/ (sha256 cdeb8efc05d6)
- checks: {"thresholds": null}
  - award_amount_text: $28,000 ⟵ “St. Joseph Scholarship | 4.0+ GPA | $28,000”
  - eligibility_summary: 4.0+ GPA ⟵ “St. Joseph Scholarship | 4.0+ GPA | $28,000”
### `94c4ff53167e7e38` Loras College — awards 2026-27 [new] (labeled_in_source)
- source: https://loras.edu/scholarships/ (sha256 cdeb8efc05d6)
- checks: {"thresholds": null}
  - award_amount_text: $26,000 ⟵ “St. Bernard Scholarship | 3.80-3.99 | $26,000”
  - eligibility_summary: 3.80-3.99 ⟵ “St. Bernard Scholarship | 3.80-3.99 | $26,000”
### `ceb6a3a8545d3b50` Loras College — awards 2026-27 [new] (labeled_in_source)
- source: https://loras.edu/scholarships/ (sha256 cdeb8efc05d6)
- checks: {"thresholds": null}
  - award_amount_text: $23,000 ⟵ “St. Clare Scholarship | 3.00-3.39 | $23,000”
  - eligibility_summary: 3.00-3.39 ⟵ “St. Clare Scholarship | 3.00-3.39 | $23,000”
### `d352dcaef3af460e` Loras College — awards 2026-27 [new] (labeled_in_source)
- source: https://loras.edu/scholarships/ (sha256 cdeb8efc05d6)
- checks: {"thresholds": null}
  - award_amount_text: $22,000 ⟵ “Loras Opportunity Grant | Below 3.00 | $22,000”
  - eligibility_summary: Below 3.00 ⟵ “Loras Opportunity Grant | Below 3.00 | $22,000”
### `1d710d03f7a67171` Luther College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.luther.edu/admission-aid/cost-financial-aid/scholarships (sha256 764420fa598a)
- checks: {"thresholds": null}
  - award_amount_text: $36,000 per year ⟵ “Dean | 3.50 - 3.69 | $36,000 per year”
  - gpa_requirement: 3.50 - 3.69 ⟵ “Dean | 3.50 - 3.69 | $36,000 per year”
### `56746a85cbd78e8f` Luther College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.luther.edu/admission-aid/cost-financial-aid/scholarships (sha256 764420fa598a)
- checks: {"thresholds": null}
  - award_amount_text: $39,000 per year ⟵ “Founders | >=3.90 | $39,000 per year”
  - gpa_requirement: >=3.90 ⟵ “Founders | >=3.90 | $39,000 per year”
### `5c31f0dd1f6eaefb` Luther College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.luther.edu/admission-aid/cost-financial-aid/scholarships (sha256 764420fa598a)
- checks: {"thresholds": null}
  - award_amount_text: $31,000 per year ⟵ “Achievement | <=3.19 | $31,000 per year”
  - gpa_requirement: <=3.19 ⟵ “Achievement | <=3.19 | $31,000 per year”
### `65d836e0a4228af5` Luther College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.luther.edu/admission-aid/cost-financial-aid/scholarships (sha256 764420fa598a)
- checks: {"thresholds": null}
  - award_amount_text: $37,000 per year ⟵ “President's | 3.70 - 3.89 | $37,000 per year”
  - gpa_requirement: 3.70 - 3.89 ⟵ “President's | 3.70 - 3.89 | $37,000 per year”
### `d9bfed91f60bfe9e` Luther College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.luther.edu/admission-aid/cost-financial-aid/scholarships (sha256 764420fa598a)
- checks: {"thresholds": null}
  - award_amount_text: $33,000 per year ⟵ “Martin Luther | 3.2 - 3.49 | $33,000 per year”
  - gpa_requirement: 3.2 - 3.49 ⟵ “Martin Luther | 3.2 - 3.49 | $33,000 per year”
### `689f17ae9014caf7` Luther College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.luther.edu/admission-aid/cost-financial-aid/tuition-fees (sha256 e0502ed1bd36)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 55140 ⟵ “Tuition | $55,140”
  - column:Housing (Double Room): 6010 ⟵ “Housing (Double Room) | $6,010”
  - column:Food: 6700 ⟵ “Food | $6,700”
  - column:Technology Fee: 530 ⟵ “Technology Fee | $530”
  - column:Health & Wellbeing Fee: 270 ⟵ “Health & Wellbeing Fee | $270”
  - column:Student Activity Fee: 320 ⟵ “Student Activity Fee | $320”
  - column:Total Comprehensive Fee: 68970 ⟵ “Total Comprehensive Fee | $68,970”
### `86526801f5dc0fac` Maharishi International University — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://www.miu.edu/ba-in-applied-arts-and-sciences (sha256 4860bd154297)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer credits are accepted for courses completed with a grade of “C” or higher.”
### `0db9f948970a8042` Northwestern College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.nwciowa.edu/transfer-credits (sha256 8ad40361f574)
- checks: {"distinct_exams": 24, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[AP-BIOLOGY|4, 5]:  ⟵ “Biology | 4, 5 | BIO110SN | 4”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “Calculus AB | 4, 5 | MAT112QR | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MAT112QR | 4”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “Calculus BC | 4, 5 | MAT112QR & MAT211 | 8”
  - equivalencies[AP-CHEMISTRY|4, 5]:  ⟵ “Chemistry | 4, 5 | CHE111 | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “Computer Science A | 4, 5 | CSC171QR | 4”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4, 5]:  ⟵ “Computer Science Principles | 4, 5 | Elective | 4”
  - equivalencies[AP-MACROECONOMICS|4, 5]:  ⟵ “Economics: macro | 4, 5 | ECO214 | 4”
  - equivalencies[AP-MICROECONOMICS|4, 5]:  ⟵ “Economics: micro | 4, 5 | ECO213 | 4”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|4, 5]:  ⟵ “Environmental science | 4, 5 | BIO101SN | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|4, 5]:  ⟵ “European history | 4, 5 | HIS203HP or HIS204HP | 4”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “French language | 3, 4, 5 | Elective | 3”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “German language | 3, 4, 5 | Elective | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4, 5]:  ⟵ “Human geography | 4, 5 | PSC260CC | 4”
  - equivalencies[AP-MUSIC-THEORY|4, 5]:  ⟵ “Music theory | 4, 5 | MUS101 | 2”
  - equivalencies[AP-PHYSICS-1|4, 5]:  ⟵ “Physics 1: Algebra-based | 4, 5 | PHY111SN | 4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4, 5]:  ⟵ “Physics C: mechanics | 4, 5 | PHY211 | 4”
  - equivalencies[AP-PRECALCULUS|4, 5]:  ⟵ “Precalculus | 4, 5 | MAT109QR | 3”
  - equivalencies[AP-PSYCHOLOGY|4, 5]:  ⟵ “Psychology | 4, 5 | PSY100SS | 4”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3, 4, 5]:  ⟵ “Spanish language | 3, 4, 5 | SPA202 | 3”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|3, 4, 5]:  ⟵ “Spanish literature | 3, 4, 5 | SPA314 | 3”
  - equivalencies[AP-STATISTICS|4, 5]:  ⟵ “Statistics | 4, 5 | MAT116QR | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|4, 5]:  ⟵ “U.S. history | 4, 5 | HIS201HP or HIS202HP | 4”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4, 5]:  ⟵ “U.S. government & politics | 4, 5 | PSC101SS | 4”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4, 5]:  ⟵ “World history | 4, 5 | HIS203HP or HIS204HP | 4”
### `551de5dbfefad6b5` Northwestern College — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.nwciowa.edu/transfer-credits (sha256 8ad40361f574)
- checks: {"distinct_exams": 20, "equivalencies": 22, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American government | 50 | PSC101SS | 4”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MAT112QR | 4”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHE111 | 4”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College composition | 50 | ENG184 | 4”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College mathematics | 50 | MAT150QR | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial accounting | 50 | ACC215 | 4”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German language level 1 | 50 | GER101 & GER102 | 6”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German language level 2 | 60 | GER101, GER102, GER201LA & GER202 | 12”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human growth and development | 50 | PSY221SS | 4”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory psychology | 50 | PSY100SS | 4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory sociology | 50 | SOC101SS | 4”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MAT109QR | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of macroeconomics | 50 | ECO214 | 4”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Principles of management | 50 | BUS201 | 2”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Principles of marketing | 50 | BUS200 | 2”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of microeconomics | 50 | ECO213 | 4”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish language level 1 | 50 | SPA111 & SPA112LA | 8”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish language level 2 | 50 | SPA111, SPA112LA & SPA201 | 11”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “U.S. history I | 50 | HIS201HP | 4”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “U.S. history II | 50 | HIS202HP | 4”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western civilization I: Ancient near east to 1648 | 50 | HIS203HP | 4”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50]:  ⟵ “Western civilization II: 1648 to the present | 50 | HIS204HP | 4”
### `mf84eefb13de2b81` Northwestern College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://assets.nwciowa.edu/nwciowa/public/content/pdf/CCC.pdf (sha256 f03551b43081)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C ⟵ “Grades matter We will only transfer in 100-level or above courses for which you have earned a grade of C or higher.”
  - min_grade: C ⟵ “NWC will guarantee the acceptance of all transferable credits earned, with a grade of “C” or higher, from the transfer-oriented associate degree program, not to exceed 64 semester credits.”
### `6cdf93246de15927` Simpson College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.simpson.edu/admissions-aid/financial-aid-affordability/scholarships/first-year-scholarships/ (sha256 107551b5785e)
- checks: {"thresholds": null}
  - award_amount_text: $35,000 ⟵ “Simpson/Endowed Scholarship | Below 3.25 | $35,000”
  - gpa_requirement: Below 3.25 ⟵ “Simpson/Endowed Scholarship | Below 3.25 | $35,000”
### `b86ebfa1750dcda7` Simpson College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.simpson.edu/admissions-aid/financial-aid-affordability/scholarships/first-year-scholarships/ (sha256 107551b5785e)
- checks: {"thresholds": {"gpa_min": 4.0}}
  - award_amount_text: $42,000 ⟵ “Founder’s Scholarship | 4.0+ | $42,000”
  - gpa_requirement: 4.0+ ⟵ “Founder’s Scholarship | 4.0+ | $42,000”
### `d8b297cb5f28c481` Simpson College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.simpson.edu/admissions-aid/financial-aid-affordability/scholarships/first-year-scholarships/ (sha256 107551b5785e)
- checks: {"thresholds": null}
  - award_amount_text: $37,000 ⟵ “Dean’s Scholarship | 3.25-3.49 | $37,000”
  - gpa_requirement: 3.25-3.49 ⟵ “Dean’s Scholarship | 3.25-3.49 | $37,000”
### `f27143a07348cec5` Simpson College — awards 2027-28 [new] (labeled_in_source)
- source: https://www.simpson.edu/admissions-aid/financial-aid-affordability/scholarships/first-year-scholarships/ (sha256 107551b5785e)
- checks: {"thresholds": null}
  - award_amount_text: $40,000 ⟵ “Presidential Scholarship | 3.50-3.99 | $40,000”
  - gpa_requirement: 3.50-3.99 ⟵ “Presidential Scholarship | 3.50-3.99 | $40,000”
### `m2decac50a2ccbd9` University of Dubuque — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.dbq.edu/media/Admissions/FinancialAid/Transfer-of-Credit-Policies.pdf (sha256 dff73156da44)
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - min_grade: C ⟵ “Consult department listings for specific details on GPA requirements of all majors. - A grade of C or better when the minimum acceptable grade is stated to be a C (a grade of C- will not suffice). - Transfer students with less than 24 credits will be required to complete World View Seminar I and those with less than 58 credits will take World View II.”
  - residency_requirement_credits: 36 ⟵ “Transfer students must earn a minimum of 12 credit hours in their major area of study (some majors may have additional requirements) and earn a minimum of 30 of their last 36 credit hours in residence at the University of Dubuque.”
### `bd1d8e85b2b6e654` University of Iowa — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.uiowa.edu/transfer-plans (sha256 8aa87e1efa43)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 15 ⟵ “A maximum of 15 semester hours of approved transfer credit may be counted toward the major.”
### `e13e3e016ed5c262` Upper Iowa University — awards 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/types-of-financial-aid/?ecopen=centeronline-students-scholarships (sha256 b5cb8a1b3d42)
- checks: {"thresholds": null}
  - award_amount_text: $3,500 ⟵ “Presidential Scholarship | $3,500 | per academic year for full-time enrollment”
### `f1b953aa4b90b3a5` Upper Iowa University — awards 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/types-of-financial-aid/ (sha256 f317fdbce5b2)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “Dean’s Scholarship | $2,000 | per academic year for full-time enrollment”
### `f90677be0d9e9970` Upper Iowa University — awards 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/scholarship-opportunities/?ecopen=fayette-campus (sha256 4a4281c33117)
- checks: {"thresholds": null}
  - award_amount_text: $500 ⟵ “Achievement Scholarship | $500 | per academic year for full-time enrollment”
### `fcbd96e82659243f` Upper Iowa University — awards 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/scholarship-opportunities/?ecopen=centers-and-distance-education (sha256 b76885e8a687)
- checks: {"thresholds": null}
  - award_amount_text: $5,500 ⟵ “Trustee Scholarship | $5,500 | per academic year for full-time enrollment”
### `ea39b234e1f76526` Upper Iowa University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://uiu.edu/admissions/tuition-and-costs/?ecopen=center-online-and-self-paced-tuition (sha256 ab6fb90e6f8a)
- checks: {"columns": 1, "rows": 3}
  - column:First Semester Fulltime: 9590 ⟵ “First Semester Fulltime | $9,590”
  - column:Second Semester Fulltime: 9590 ⟵ “Second Semester Fulltime | $9,590”
  - column:Annual Tuition: 19180 ⟵ “Annual Tuition | $19,180”
### `54b1e5a782d50b11` Wartburg College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wartburg.edu/financial-aid/ (sha256 365bab655a92)
- checks: {"thresholds": null}
  - gpa_requirement: Required GPA: 2.00 ⟵ “Course Credits Completed: 16.00-25.75 | Required GPA: 2.00 | Pace (earned/attempted): 67%”
### `790ab9a3f296ebcd` Wartburg College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wartburg.edu/financial-aid/ (sha256 365bab655a92)
- checks: {"thresholds": null}
  - gpa_requirement: Required GPA: 1.60 ⟵ “Course Credits Completed: 0.25-6.75 | Required GPA: 1.60 | Pace (earned/attempted): 67%”
### `b3df80c75110599b` Wartburg College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wartburg.edu/financial-aid/ (sha256 365bab655a92)
- checks: {"thresholds": null}
  - gpa_requirement: Required GPA: 2.00 ⟵ “Course Credits Completed: 26.00+ | Required GPA: 2.00 | Pace (earned/attempted): 67%”
### `fdc98b5290fb5b43` Wartburg College — awards 2026-27 [new] (labeled_in_source)
- source: https://www.wartburg.edu/financial-aid/ (sha256 365bab655a92)
- checks: {"thresholds": null}
  - gpa_requirement: Required GPA: 1.80 ⟵ “Course Credits Completed: 7.00-15.75 | Required GPA: 1.80 | Pace (earned/attempted): 67%”
### `501e149dacf59dac` William Penn University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.wmpenn.edu/admissions-aid/transfer-students/ (sha256 b347bd02bf37)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “For those students with an overall transfer grade point average of less than 2.0, only courses with a grade of “C-” or above will transfer.”

## Exceptions (180)

### `096b4e9466dfe0b2` Allen College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20ABSN.pdf (sha256 71b4b5401b13)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20DPT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20HBSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20MS%20in%20OT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20OTD.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20TBSN.pdf
- checks: {"columns": 4, "components_reconcile": false, "rows": 14}
  - column:*NCLEX Complete Package Fee – Charged between first 2 semesters for BSN: 3310 ⟵ “*NCLEX Complete Package Fee – Charged between first 2 semesters for BSN | $3,310”
  - column:*Professional Membership Fees – Annually: 40 ⟵ “*Professional Membership Fees – Annually | $40”
  - column:**Lippincott, State of Iowa licensing fee, NCLEX registration fee: 473 ⟵ “**Lippincott, State of Iowa licensing fee, NCLEX registration fee | $473”
  - column:Tuition: 13122 ⟵ “Tuition | $13,122 | $13,122 | $13,122 | $39,366”
  - column:Fees: 1940 ⟵ “Fees | $1,940 | $1,940 | $1,940 | $5,820”
  - column:Federal Student Loan Fees: 44 ⟵ “Federal Student Loan Fees | $44 | $44 | $44 | $132”
  - column:Subtotal (Direct Costs): 15106 ⟵ “Subtotal (Direct Costs) | $15,106 | $15,106 | $15,106 | $45,318”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $350 | $1,050”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $4,800 | $14,400”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $800 | $2,400”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $1,200 | $3,600”
  - column:Professional Licensure/Certification/Credentials: 158 ⟵ “Professional Licensure/Certification/Credentials | $158 | $158 | $158 | $474”
  - column:Subtotal (Indirect Costs): 7308 ⟵ “Subtotal (Indirect Costs) | $7,308 | $7,308 | $7,308 | $21,924”
  - column:TOTAL: 22414 ⟵ “TOTAL | $22,414 | $22,414 | $22,414 | $67,242”
  - column:Tuition: 13122 ⟵ “Tuition | $13,122 | $13,122 | $13,122 | $39,366”
  - column:Fees: 1940 ⟵ “Fees | $1,940 | $1,940 | $1,940 | $5,820”
  - column:Federal Student Loan Fees: 44 ⟵ “Federal Student Loan Fees | $44 | $44 | $44 | $132”
  - column:Subtotal (Direct Costs): 15106 ⟵ “Subtotal (Direct Costs) | $15,106 | $15,106 | $15,106 | $45,318”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $350 | $1,050”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $4,800 | $14,400”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $800 | $2,400”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $1,200 | $3,600”
  - column:Professional Licensure/Certification/Credentials: 158 ⟵ “Professional Licensure/Certification/Credentials | $158 | $158 | $158 | $474”
  - column:Subtotal (Indirect Costs): 7308 ⟵ “Subtotal (Indirect Costs) | $7,308 | $7,308 | $7,308 | $21,924”
  - column:TOTAL: 22414 ⟵ “TOTAL | $22,414 | $22,414 | $22,414 | $67,242”
  - … 22 more rows
### `37bf109298651742` Allen College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20MS%20in%20OT.pdf (sha256 229b71421ce9)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20ABSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20DPT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20HBSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20OTD.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20TBSN.pdf
- checks: {"columns": 4, "components_reconcile": false, "rows": 12}
  - column:*Certification/Licensure: 660 ⟵ “*Certification/Licensure | $660”
  - column:Tuition: 11712 ⟵ “Tuition | $11,712 | $11,712 | $11,712 | $35,136”
  - column:Fees: 710 ⟵ “Fees | $710 | $710 | $710 | $2,130”
  - column:Federal Student Loan Fees: 72 ⟵ “Federal Student Loan Fees | $72 | $72 | $72 | $216”
  - column:Subtotal (Direct Costs): 12494 ⟵ “Subtotal (Direct Costs) | $12,494 | $12,494 | $12,494 | $37,482”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $350 | $1,050”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $4,800 | $14,400”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $800 | $2,400”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $1,200 | $3,600”
  - column:Professional Licensure/Certification/Credentials: 220 ⟵ “Professional Licensure/Certification/Credentials | $220 | $220 | $220 | $660”
  - column:Subtotal (Indirect Costs): 7370 ⟵ “Subtotal (Indirect Costs) | $7,370 | $7,370 | $7,370 | $22,110”
  - column:TOTAL: 19864 ⟵ “TOTAL | $19,864 | $19,864 | $19,864 | $59,592”
  - column:Tuition: 11712 ⟵ “Tuition | $11,712 | $11,712 | $11,712 | $35,136”
  - column:Fees: 710 ⟵ “Fees | $710 | $710 | $710 | $2,130”
  - column:Federal Student Loan Fees: 72 ⟵ “Federal Student Loan Fees | $72 | $72 | $72 | $216”
  - column:Subtotal (Direct Costs): 12494 ⟵ “Subtotal (Direct Costs) | $12,494 | $12,494 | $12,494 | $37,482”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $350 | $1,050”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $4,800 | $14,400”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $800 | $2,400”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $1,200 | $3,600”
  - column:Professional Licensure/Certification/Credentials: 220 ⟵ “Professional Licensure/Certification/Credentials | $220 | $220 | $220 | $660”
  - column:Subtotal (Indirect Costs): 7370 ⟵ “Subtotal (Indirect Costs) | $7,370 | $7,370 | $7,370 | $22,110”
  - column:TOTAL: 19864 ⟵ “TOTAL | $19,864 | $19,864 | $19,864 | $59,592”
  - column:Tuition: 11712 ⟵ “Tuition | $11,712 | $11,712 | $11,712 | $35,136”
  - column:Fees: 710 ⟵ “Fees | $710 | $710 | $710 | $2,130”
  - … 20 more rows
### `881a9f3da12c09fd` Allen College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20HBSN.pdf (sha256 0b33353cc1c6)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20ABSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20DPT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20MS%20in%20OT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20OTD.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20TBSN.pdf
- checks: {"columns": 3, "components_reconcile": false, "rows": 14}
  - column:*NCLEX Complete Package Fee – Charged between first 2 semesters for BSN: 3695 ⟵ “*NCLEX Complete Package Fee – Charged between first 2 semesters for BSN | $3,695”
  - column:*Professional Membership Fees – Annually: 80 ⟵ “*Professional Membership Fees – Annually | $80”
  - column:**Lippincott, State of Iowa licensing fee, NCLEX registration fee: 473 ⟵ “**Lippincott, State of Iowa licensing fee, NCLEX registration fee | $473”
  - column:Tuition: 8019 ⟵ “Tuition | $8,019 | $8,019 | $16,038”
  - column:Fees: 1164 ⟵ “Fees | $1,164 | $1,164 | $2,328”
  - column:Federal Student Loan Fees: 44 ⟵ “Federal Student Loan Fees | $44 | $44 | $88”
  - column:Subtotal (Direct Costs): 9227 ⟵ “Subtotal (Direct Costs) | $9,227 | $9,227 | $18,454”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $800”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $9,600”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $1,600”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $2,400”
  - column:Professional Licensure/Certification/Credentials: 237 ⟵ “Professional Licensure/Certification/Credentials | $237 | $237 | $474”
  - column:Subtotal (Indirect Costs): 7387 ⟵ “Subtotal (Indirect Costs) | $7,387 | $7,387 | $14,774”
  - column:TOTAL: 16614 ⟵ “TOTAL | $16,614 | $16,614 | $33,228”
  - column:Tuition: 8019 ⟵ “Tuition | $8,019 | $8,019 | $16,038”
  - column:Fees: 1164 ⟵ “Fees | $1,164 | $1,164 | $2,328”
  - column:Federal Student Loan Fees: 44 ⟵ “Federal Student Loan Fees | $44 | $44 | $88”
  - column:Subtotal (Direct Costs): 9227 ⟵ “Subtotal (Direct Costs) | $9,227 | $9,227 | $18,454”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $800”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $9,600”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $1,600”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $2,400”
  - column:Professional Licensure/Certification/Credentials: 237 ⟵ “Professional Licensure/Certification/Credentials | $237 | $237 | $474”
  - column:Subtotal (Indirect Costs): 7387 ⟵ “Subtotal (Indirect Costs) | $7,387 | $7,387 | $14,774”
  - column:TOTAL: 16614 ⟵ “TOTAL | $16,614 | $16,614 | $33,228”
  - … 11 more rows
### `8bbee070f286aa48` Allen College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20TBSN.pdf (sha256 e64dfa7a893a)
- issues: conflicting_sources:https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20ABSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20DPT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20HBSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20MS%20in%20OT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20OTD.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition: 23328 ⟵ “Tuition | $11,664 | $11,664 | $23,328”
  - column:Fees: 3124 ⟵ “Fees | $1,562 | $1,562 | $3,124”
  - column:Federal Student Loan Fees: 132 ⟵ “Federal Student Loan Fees | $66 | $66 | $132”
  - column:Subtotal (Direct Costs): 26584 ⟵ “Subtotal (Direct Costs) | $13,292 | $13,292 | $26,584”
  - column:Books & Course Supplies: 700 ⟵ “Books & Course Supplies | $350 | $350 | $700”
  - column:Food & Housing: 9600 ⟵ “Food & Housing | $4,800 | $4,800 | $9,600”
  - column:Transportation: 1600 ⟵ “Transportation | $800 | $800 | $1,600”
  - column:Personal Expenses: 2400 ⟵ “Personal Expenses | $1,200 | $1,200 | $2,400”
  - column:Professional Licensure/Certification/Credentials: 474 ⟵ “Professional Licensure/Certification/Credentials | $237 | $237 | $474”
  - column:Subtotal (Indirect Costs): 14774 ⟵ “Subtotal (Indirect Costs) | $7,387 | $7,387 | $14,774”
  - column:TOTAL: 41358 ⟵ “TOTAL | $20,679 | $20,679 | $41,358”
### `d3ccd8044005e474` Allen College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20DPT.pdf (sha256 182b43dec655)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20ABSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20HBSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20MS%20in%20OT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20OTD.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20TBSN.pdf
- checks: {"columns": 4, "components_reconcile": false, "rows": 12}
  - column:*Certification/Licensure: 485 ⟵ “*Certification/Licensure | $485”
  - column:Tuition: 13664 ⟵ “Tuition | $13,664 | $13,664 | $13,664 | $40,992”
  - column:Fees: 500 ⟵ “Fees | $500 | $500 | $500 | $1,500”
  - column:Federal Student Loan Fees: 72 ⟵ “Federal Student Loan Fees | $72 | $72 | $72 | $216”
  - column:Subtotal (Direct Costs): 14236 ⟵ “Subtotal (Direct Costs) | $14,236 | $14,236 | $14,236 | $42,708”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $350 | $1,050”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $4,800 | $14,400”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $800 | $2,400”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $1,200 | $3,600”
  - column:Professional Licensure/Certification/Credentials: 162 ⟵ “Professional Licensure/Certification/Credentials | $162 | $162 | $162 | $486”
  - column:Subtotal (Indirect Costs): 7312 ⟵ “Subtotal (Indirect Costs) | $7,312 | $7,312 | $7,312 | $21,936”
  - column:TOTAL: 21548 ⟵ “TOTAL | $21,548 | $21,548 | $21,548 | $64,644”
  - column:Tuition: 13664 ⟵ “Tuition | $13,664 | $13,664 | $13,664 | $40,992”
  - column:Fees: 500 ⟵ “Fees | $500 | $500 | $500 | $1,500”
  - column:Federal Student Loan Fees: 72 ⟵ “Federal Student Loan Fees | $72 | $72 | $72 | $216”
  - column:Subtotal (Direct Costs): 14236 ⟵ “Subtotal (Direct Costs) | $14,236 | $14,236 | $14,236 | $42,708”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $350 | $1,050”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $4,800 | $14,400”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $800 | $2,400”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $1,200 | $3,600”
  - column:Professional Licensure/Certification/Credentials: 162 ⟵ “Professional Licensure/Certification/Credentials | $162 | $162 | $162 | $486”
  - column:Subtotal (Indirect Costs): 7312 ⟵ “Subtotal (Indirect Costs) | $7,312 | $7,312 | $7,312 | $21,936”
  - column:TOTAL: 21548 ⟵ “TOTAL | $21,548 | $21,548 | $21,548 | $64,644”
  - column:Tuition: 13664 ⟵ “Tuition | $13,664 | $13,664 | $13,664 | $40,992”
  - column:Fees: 500 ⟵ “Fees | $500 | $500 | $500 | $1,500”
  - … 20 more rows
### `d5c19e0cac9465cd` Allen College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20OTD.pdf (sha256 db16a6a060b9)
- issues: arrangement_unlabeled, components_do_not_reconcile, conflicting_sources:https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20ABSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20DPT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20HBSN.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20MS%20in%20OT.pdf,https://www.allencollege.edu/filesimages/PagePDFs/Fin%20Aid/Tuition%20Fees%20TBSN.pdf
- checks: {"columns": 4, "components_reconcile": false, "rows": 12}
  - column:*Certification/Licensure: 660 ⟵ “*Certification/Licensure | $660”
  - column:Tuition: 14640 ⟵ “Tuition | $14,640 | $14,640 | $14,640 | $43,920”
  - column:Fees: 274 ⟵ “Fees | $274 | $274 | $274 | $822”
  - column:Federal Student Loan Fees: 72 ⟵ “Federal Student Loan Fees | $72 | $72 | $72 | $216”
  - column:Subtotal (Direct Costs): 14986 ⟵ “Subtotal (Direct Costs) | $14,986 | $14,986 | $14,986 | $44,958”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $350 | $1,050”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $4,800 | $14,400”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $800 | $2,400”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $1,200 | $3,600”
  - column:Professional Licensure/Certification/Credentials: 220 ⟵ “Professional Licensure/Certification/Credentials | $220 | $220 | $220 | $660”
  - column:Subtotal (Indirect Costs): 7370 ⟵ “Subtotal (Indirect Costs) | $7,370 | $7,370 | $7,370 | $22,110”
  - column:TOTAL: 22356 ⟵ “TOTAL | $22,356 | $22,356 | $22,356 | $67,068”
  - column:Tuition: 14640 ⟵ “Tuition | $14,640 | $14,640 | $14,640 | $43,920”
  - column:Fees: 274 ⟵ “Fees | $274 | $274 | $274 | $822”
  - column:Federal Student Loan Fees: 72 ⟵ “Federal Student Loan Fees | $72 | $72 | $72 | $216”
  - column:Subtotal (Direct Costs): 14986 ⟵ “Subtotal (Direct Costs) | $14,986 | $14,986 | $14,986 | $44,958”
  - column:Books & Course Supplies: 350 ⟵ “Books & Course Supplies | $350 | $350 | $350 | $1,050”
  - column:Food & Housing: 4800 ⟵ “Food & Housing | $4,800 | $4,800 | $4,800 | $14,400”
  - column:Transportation: 800 ⟵ “Transportation | $800 | $800 | $800 | $2,400”
  - column:Personal Expenses: 1200 ⟵ “Personal Expenses | $1,200 | $1,200 | $1,200 | $3,600”
  - column:Professional Licensure/Certification/Credentials: 220 ⟵ “Professional Licensure/Certification/Credentials | $220 | $220 | $220 | $660”
  - column:Subtotal (Indirect Costs): 7370 ⟵ “Subtotal (Indirect Costs) | $7,370 | $7,370 | $7,370 | $22,110”
  - column:TOTAL: 22356 ⟵ “TOTAL | $22,356 | $22,356 | $22,356 | $67,068”
  - column:Tuition: 14640 ⟵ “Tuition | $14,640 | $14,640 | $14,640 | $43,920”
  - column:Fees: 274 ⟵ “Fees | $274 | $274 | $274 | $822”
  - … 20 more rows
### `61dbb89d36135aac` Briar Cliff University — appeals 2025-26 [new] (labeled_in_url)
- source: https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_SAP.pdf (sha256 391d0e2526d2)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Sioux City, IA 51104 (712) 279-5530 Financial.Aid@briarcliff.edu Financial Aid Satisfactory Academic Progress Appeal If you have been suspended from financial aid for not meeting Satisfactory Academic Standards and your inability to meet standards was due to a mitigating circumstance, you may appeal the suspension.”
  - sentence: sap_appeal ⟵ “Not knowing about policies and requirements for satisfactory academic progress or unpreparedness for college coursework are not acceptable reasons for appeal.”
### `7e3727b6b4e2f9ec` Briar Cliff University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_DOR.pdf (sha256 fc2de5ce4b22)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_RSC.pdf,https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_V1V5_DVW.pdf,https://www.briarcliff.edu/future-chargers/tuition-and-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “If you have experienced unusual circumstances that prevent you from providing this information, you may request the Financial Aid office to review your situation to determine if you qualify to be considered independent for financial aid purposes.”
  - sentence: need_based_special_circumstances ⟵ “The Office of Financial Aid has the authority, through Section 480(d)(7) of the Higher Education Act, to change a student’s dependency status on a case-by-case basis for students with unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “If you have an unusual circumstance, do not have contact with your parent, or contact poses a risk, such as in the case of abuse, abandonment, or neglect, you may submit a Change in Dependency Status Request.”
### `9b8fbfbf2b6a26d4` Briar Cliff University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_RSC.pdf (sha256 d48784225adf)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_DOR.pdf,https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_V1V5_DVW.pdf,https://www.briarcliff.edu/future-chargers/tuition-and-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “However, we realize that a family’s situation may change or there may be special circumstances that cannot be addressed on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “If you believe that you or your family are burdened by special circumstances, please provide all requested documentation along with this completed form and submit it to Financial Aid.”
### `a3f57e26b7c687d7` Briar Cliff University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_V1V5_DVW.pdf (sha256 719722d8e8df)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_DOR.pdf,https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_RSC.pdf,https://www.briarcliff.edu/future-chargers/tuition-and-aid/financial-aid
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Verification of 2023 Income Information for Students with Unusual Circumstances Complete this section if the student and/or spouse has filed or will file a 2023 income tax return with any of the following circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Verification of 2023 Income Information for Parents with Unusual Circumstances Complete this section if the student’s parent(s) has filed or will file a 2023 income tax return with any of the following circumstances.”
### `cff18822b0547c00` Briar Cliff University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.briarcliff.edu/future-chargers/tuition-and-aid/financial-aid (sha256 48e80b311844)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_DOR.pdf,https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_RSC.pdf,https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_V1V5_DVW.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “It's important to explore all options to find the best solution for your needs. | What if I have a special or unusual circumstance related to my FAFSA? | Special Circumstances Related to the FAFSA The FAFSA for the 2025-2026 academic year uses 2023 income and tax information to determine eligibility for the Pell Grant and other need-based aid such as Subsidized Direct Loans.”
  - sentence: need_based_special_circumstances ⟵ “You may qualify for a review of your FAFSA information, if your 2023 income (or your family’s income for a dependent student) does not accurately reflect your current financial situation due to special circumstances such as the following: Reduction in income due to unemployment, job change, reduced hours or retirement.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances and FAFSA Dependency Status Students who are considered dependent for federal financial aid purposes are required to include parent information on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “If you are a dependent student who has unusual circumstances that have resulted in a breakdown in your relationship with your parents, you may ask the Financial Aid Office to review your situation to determine if you qualify to be considered independent for financial aid purposes.”
  - sentence: need_based_special_circumstances ⟵ “Students who request a review of their FAFSA dependency status must document that unusual circumstances exist with both biological or adoptive parents.”
  - sentence: need_based_special_circumstances ⟵ “For example, a student who has one parent who is incarcerated would not qualify to be independent unless the student could also document an unusual circumstance with the parent who is not incarcerated.”
### `de78b6967bf9094c` Briar Cliff University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.briarcliff.edu/filesimages/Future%20Chargers/Financial%20Aid/Costs%20and%20Financial%20Aid/Verification%20Forms/2025-2026/2025-2026_DOR.pdf (sha256 fc2de5ce4b22)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Federal Regulations specifically prohibit schools from processing a dependency override for any of the following reasons: • Parents refuse to contribute to the student’s education. • Parents are unwilling to provide information on the application or for verification. • Parents do not claim the student as a dependent for income tax purposes. • Student demonstrates total self-sufficiency.”
### `ad43f3c55ffdd0a8` Central College — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://departments.central.edu/wp-content/uploads/sites/17/files/2026/09/CDS-2025-26-Final.pdf (sha256 af4e07a66d51)
- issues: stale_year_label:2024-25, conflicting_sources:https://departments.central.edu/wp-content/uploads/sites/17/files/2025/05/2024-25-CDS-FINAL-Central-College-IA.pdf
- checks: {"fields": ["act_25", "act_75", "admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 1790 ⟵ “Total first-time, first-year (degree-seeking) who applied                                1037           750             3       1790”
  - admits: 1561 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                            943          615             3       1561”
  - enrolled: 316 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                                 230           84             2         316”
  - act_25..75: [20, 27] ⟵ “ACT Composite                                    20                24.5               27”
### `b91f98d788d86da7` Central College — admissions_metrics 2024-25 [new] (labeled_in_source)
- source: https://departments.central.edu/wp-content/uploads/sites/17/files/2025/05/2024-25-CDS-FINAL-Central-College-IA.pdf (sha256 d6952e5b7e58)
- issues: applications_breakdown_does_not_reconcile, admits_breakdown_does_not_reconcile, enrolled_breakdown_does_not_reconcile, stale_year_label:2024-25, conflicting_sources:https://departments.central.edu/wp-content/uploads/sites/17/files/2026/09/CDS-2025-26-Final.pdf
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year"]}
  - applications: 0 ⟵ “Total first-time, first-year who applied                                                  1706         979        727              0       0”
  - admits: 0 ⟵ “Total first-time, first-year who were admitted                                            1470         879        591              0       0”
  - enrolled: 0 ⟵ “Total first-time, first-year who enrolled                                                  309         241         69              0       0”
  - act_25..75: [20, 23, 26] ⟵ “ACT Composite                        20                        23                 26”
### `m59e0ad265e83ecc` Central College — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://departments.central.edu/registrar/transfer-creditap/pccapib/ (sha256 8c88b0563d29)
- issues: conflicting_values:max_transfer_credits
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 3}
  - max_transfer_credits: 75 ⟵ “Transfer credit for students entering after August 2024 A maximum of 75 semester hours of transfer credit may be applied toward completion of a Central College degree.”
  - min_grade: C ⟵ “Transfer of credit for students entering after August of 2024 All transfer credit must be earned at a regionally accredited college or university with a grade of “C” or better.”
### `8d8fb31947c5b870` Clarke University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://clarke.edu/admission-aid/tuition-and-fees/undergraduate-basic-fees/ (sha256 174694d03480)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - on_campus:Tuition: 21320 ⟵ “Tuition | $21,750 | $43,500 | $21,320 | $42,640”
  - on_campus:Student Services Fee: 400 ⟵ “Student Services Fee | $413 | $825 | $400 | $800”
  - on_campus:Technology Fee: 340 ⟵ “Technology Fee | $353 | $705 | $340 | $680”
  - on_campus:Double Room (Mary Benedict Hall) *See below for further options and pricing: 3148 ⟵ “Double Room (Mary Benedict Hall) *See below for further options and pricing | $3,193 | $6,385 | $3,148 | $6,295”
  - on_campus:Board Resident Student Meal Plans: 3225 ⟵ “Board Resident Student Meal Plans | $3,350 | $6,700 | $3,225 | $6,450”
  - on_campus:Board Apartment or Commuter Meal Plan: 1958 ⟵ “Board Apartment or Commuter Meal Plan | $1,958 | $3,915 | $1,958 | $3,915”
  - on_campus:TOTAL: 28433 ⟵ “TOTAL | $29,058 | $58,115 | $28,433 | $56,865”
### `cd3800a6e453736f` Clarke University — costs 2027-28 · residency=not_applicable [new] (labeled_in_source)
- source: https://clarke.edu/admission-aid/tuition-and-fees/undergraduate-basic-fees/ (sha256 174694d03480)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 7}
  - on_campus:Tuition: 21750 ⟵ “Tuition | $21,750 | $43,500 | $21,320 | $42,640”
  - on_campus:Student Services Fee: 413 ⟵ “Student Services Fee | $413 | $825 | $400 | $800”
  - on_campus:Technology Fee: 353 ⟵ “Technology Fee | $353 | $705 | $340 | $680”
  - on_campus:Double Room (Mary Benedict Hall) *See below for further options and pricing: 3193 ⟵ “Double Room (Mary Benedict Hall) *See below for further options and pricing | $3,193 | $6,385 | $3,148 | $6,295”
  - on_campus:Board Resident Student Meal Plans: 3350 ⟵ “Board Resident Student Meal Plans | $3,350 | $6,700 | $3,225 | $6,450”
  - on_campus:Board Apartment or Commuter Meal Plan: 1958 ⟵ “Board Apartment or Commuter Meal Plan | $1,958 | $3,915 | $1,958 | $3,915”
  - on_campus:TOTAL: 29058 ⟵ “TOTAL | $29,058 | $58,115 | $28,433 | $56,865”
### `86a5cc607efa9e67` Coe College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coe.edu/admission/financial-aid-scholarships/faq (sha256 2f6db81f4374)
- issues: semantic_review_required, conflicting_sources:https://www.coe.edu/admission/financial-aid-scholarships/financial-aid-handbook/verification,https://www.coe.edu/admission/financial-aid-scholarships/resources/special-circumstance-consideration,https://www.coe.edu/admission/financial-aid-scholarships/resources/veterans-and-military-benefits
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “For unusual circumstances, please contact our office.”
  - sentence: need_based_special_circumstances ⟵ “If your family's financial circumstances have changed since you filed your FAFSA or you have a special circumstance that you were not able to report on your FAFSA, the Office of Financial Aid may be able to take the changes into consideration.”
  - sentence: need_based_special_circumstances ⟵ “Our Special Circumstance page offers a summary of situations that our office may be able to consider.”
### `a696fc831d0bc1d8` Coe College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coe.edu/admission/financial-aid-scholarships/resources/special-circumstance-consideration (sha256 55681ef73fa4)
- issues: semantic_review_required, conflicting_sources:https://www.coe.edu/admission/financial-aid-scholarships/faq,https://www.coe.edu/admission/financial-aid-scholarships/financial-aid-handbook/verification,https://www.coe.edu/admission/financial-aid-scholarships/resources/veterans-and-military-benefits
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Consideration | Coe College Skip to main content Search This Site Plan a Visit Apply Request Info Toggle navigation AdmissionExpand Menu Become a Kohawk Learn about majors, apply for admission, discover campus life, connect with Coe and much more!”
  - sentence: need_based_special_circumstances ⟵ “Coe College Alumni Support Coe Alumni & Friends Engagement Publications Make a Gift C3: Creativity, Careers, Community Advancement Services FAQs Careers Current Students Faculty & Staff Parents & Visitors Request Info Search This Site Coe Admission Financial Aid & Scholarships Resources Special and/or Unusual Circumstance Consideration Special and/or Unusual Circumstance Consideration Special Circ”
  - sentence: need_based_special_circumstances ⟵ “Special and/or Unusual circumstances can often be considered when determining or reevaluating your eligibility for financial aid.”
  - sentence: need_based_special_circumstances ⟵ “Allowance for the one-time direct cost of obtaining a first professional license or certificate if for a student who is enrolled in a program that requires such professional credentials What is the process for Special Circumstance Consideration?”
  - sentence: need_based_special_circumstances ⟵ “You or your parents should contact the Coe College Financial Aid Office to explain your special circumstances.”
### `ab7e059fda925a9d` Coe College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coe.edu/admission/financial-aid-scholarships/resources/veterans-and-military-benefits (sha256 b01b4d446284)
- issues: semantic_review_required, conflicting_sources:https://www.coe.edu/admission/financial-aid-scholarships/faq,https://www.coe.edu/admission/financial-aid-scholarships/financial-aid-handbook/verification,https://www.coe.edu/admission/financial-aid-scholarships/resources/special-circumstance-consideration
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Students should contact Coe Student Financial Services to request a Special Circumstance Appeal if the income information reported on the FAFSA does not reflect their current financial situation.”
### `d959f39353cfc601` Coe College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coe.edu/admission/financial-aid-scholarships/financial-aid-handbook/satisfactory-academic-progress-sap (sha256 42e44454dd68)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Appeal A student may appeal a financial aid suspension by completing the SAP Appeal Form.”
### `e71dd1d5dd722852` Coe College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.coe.edu/admission/financial-aid-scholarships/financial-aid-handbook/verification (sha256 c64db9c8751f)
- issues: semantic_review_required, conflicting_sources:https://www.coe.edu/admission/financial-aid-scholarships/faq,https://www.coe.edu/admission/financial-aid-scholarships/resources/special-circumstance-consideration,https://www.coe.edu/admission/financial-aid-scholarships/resources/veterans-and-military-benefits
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Federal Regulations require that students selected for verification must complete the verification process before a financial aid administrator is permitted to make special circumstance adjustments to their FAFSA data.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances If you have been granted a tax filing extension by the IRS, or if you are unable to obtain a tax transcript because you were the victim of identity theft, you should contact the Office of Financial Aid for guidance on alternative documents that can meet income verification requirements.”
### `bbc367764b5451f0` Coe College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.coe.edu/admission/financial-aid-scholarships/financial-aid-handbook/educational-costs (sha256 e39445836b2e)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 13}
  - column:Tuition: 58780 ⟵ “Tuition | $58,780”
  - column:Fees: 350 ⟵ “Fees | $350”
  - column:Housing: 6070 ⟵ “Housing | $6,070”
  - column:Food: 6690 ⟵ “Food | $6,690”
  - column:Direct Cost (charged by Coe): 71890 ⟵ “Direct Cost (charged by Coe) | $71,890”
  - column:Books: 1000 ⟵ “Books | $1,000”
  - column:Personal: 1600 ⟵ “Personal | $1,600”
  - column:Student Loan Fees* [1.057%]: 72 ⟵ “Student Loan Fees* [1.057%] | $72”
  - column:Transportation: 1000 ⟵ “Transportation | $1,000”
  - column:Supplemental Food: 300 ⟵ “Supplemental Food | $300”
  - column:Housing Average: 610 ⟵ “Housing Average | $610”
  - column:Anticipated Indirect Cost (not charged by Coe): 4582 ⟵ “Anticipated Indirect Cost (not charged by Coe) | $4,582”
  - column:Total Cost of Attendance: 76472 ⟵ “Total Cost of Attendance | $76,472”
### `437b970b3959811c` Cornell College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cornellcollege.edu/financial-assistance/ (sha256 86e26857d07c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Contact the financial assistance team Money matters Net Price Calculator Special circumstances FAFSA tips How to read your financial aid summary Paying for college Cost of attendance Scholarships Grants Work study Loans Resources Veterans and Military Benefits Financial Aid Handbook [PDF] Disclosures and policies Forms Information Consumer Information Contact Us Request Info Visit Cornell Apply No”
### `9fd944110badda65` Cornell College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.cornellcollege.edu/financial-assistance/cost-of-attendance.shtml (sha256 5345eb49b0b7)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition: 54056 ⟵ “Tuition | $54,056”
  - column:Housing (standard double room): 5528 ⟵ “Housing (standard double room) | $5,528”
  - column:Food: 6536 ⟵ “Food | $6,536”
  - column:General fees: 720 ⟵ “General fees | $720”
  - column:Books: 720 ⟵ “Books | $720”
  - column:Personal: 1880 ⟵ “Personal | $1,880”
  - column:In-state transportation*: 1200 ⟵ “In-state transportation* | $1,200”
  - column:Additional food costs: 256 ⟵ “Additional food costs | $256”
  - column:Estimated loan origination fees: 70 ⟵ “Estimated loan origination fees | $70”
  - column:Total Cost of Attendance:: 70966 ⟵ “Total Cost of Attendance: | $70,966”
  - column:Total Direct Costs: 66840 ⟵ “Total Direct Costs | $66,840”
### `0bcaa3e97ac35b2c` Des Moines Area Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.dmacc.edu/financial-aid/outside-scholarships.html (sha256 922df38c5ef6)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “A GPA of 3.5 or higher will be considered but special circumstances must be met under this program.”
### `215bd42a9309e941` Des Moines Area Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.dmacc.edu/consumer-info/request-appeal.html (sha256 c69b6d6be009)
- issues: semantic_review_required, conflicting_sources:https://www.dmacc.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Click Submit when you are finished. (Do not type in your unusual circumstances in this box) Step 7: Click Ok Step 8: Click on the tile that needs Action Step 9: Click on the arrow to expand the SAP Appeal task.”
### `6b0797eeda253695` Des Moines Area Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.dmacc.edu/financial-aid/students/award-adjustment.html (sha256 01652e51f318)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances Please contact the Financial Aid office if you have a special circumstance come up during the semester.”
  - sentence: need_based_special_circumstances ⟵ “A special circumstance may include involuntary loss of employment or other conditions outside of your control that impact your financial situation.”
### `b6f8ef38f4883d03` Des Moines Area Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.dmacc.edu/financial-aid/ (sha256 42edc7727145)
- issues: semantic_review_required, conflicting_sources:https://www.dmacc.edu/consumer-info/request-appeal.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Forms CURRENT STUDENT RESOURCES Understanding and Using Your Financial Aid Find links to valuable and necessary information about financial aid programs such as how to accept awards, Satisfactory Academic Progress, various types of appeals, and financial aid refund information among other topics.”
### `603c9d40e646aa10` Dordt University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.dordt.edu/admissions-and-aid/financial-aid/supplemental-data-form (sha256 782c2cffe62c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “It serves as an opportunity for students and their families to share any unique or special circumstances that have impacted them financially and, in their current ability tofinance the cost of higher education.”
  - sentence: need_based_special_circumstances ⟵ “If you should experience a significant change in your financial situation after your aid offer has been prepared, please feel free to contact the Dordt University Financial Aid office directly.”
  - sentence: need_based_special_circumstances ⟵ “Attended Dordt Please list the 1) name and relationship (e.g. brother, sister), 2) age, 3) Name of school or college this person will attend in 2026-27 school year. *If more than 6 dependents, list additional family members under Other Special Circumstances.”
  - sentence: need_based_special_circumstances ⟵ “SECTION C: REQUEST FOR CONSIDERATION OF SPECIAL CIRCUMSTANCES Sometimes families have special circumstances which substantially impact their ability to contribute towards education expenses.”
  - sentence: need_based_special_circumstances ⟵ “Two of the most common special circumstances at Dordt University are tuition expenses to be paid for other family members for private education, and excessive medical/dental expenses.”
  - sentence: need_based_special_circumstances ⟵ “Occasionally other factors may affect the family’s contribution, such as: a significant reduction in parent income for the upcoming year, other non-discretionary expenses not mentioned on the form, a higher cost of living than the national average, a significant debt not reported on the form, or a natural disaster. (Special circumstances refer to something unique to your family.) If you would like”
### `82350cc9b4f49d09` Dordt University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.dordt.edu/about-dordt/offices-and-services/business-office/tuition-and-fees (sha256 ed15e93491d5)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition & Fees: 39050 ⟵ “Tuition & Fees | $39,050”
  - column:Food & Housing: 12250 ⟵ “Food & Housing | $12,250”
  - column:Total Cost: 51300 ⟵ “Total Cost | $51,300”
  - column:Avg. Fin. Aid Award for Freshmen: 34400 ⟵ “Avg. Fin. Aid Award for Freshmen | $34,400”
### `11a5b8019c0e0d12` Dordt University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.dordt.edu/admissions-and-aid/admission-requirements/undergraduate-program/clep-credit-guide (sha256 005ad6501bd8)
- issues: course_column_missing
- checks: {"distinct_exams": 16, "equivalencies": 18, "rows_without_score": 0}
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing and Interpreting Literature | 50 | 3 | Core 180”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | 3 | Core 120”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 3 | Core 160”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French: College Level 1 (two semesters) | 50 | 3 | French 102”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “French: College Level 2 (four semesters) | 62 | 6 | French 102 and elective”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish: College Level 1 (two semesters) | 50 | 3 | Spanish 102”
  - equivalencies[CLEP-SPANISH-LANGUAGE|63]:  ⟵ “Spanish: College Level 2 (four semesters) | 63 | 6 | Spanish 102 and elective”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | Political Science 202 / Core 264”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | Psychology 204 / Core 251”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | 50 | 3 | Economics 202”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | 50 | 3 | Economics 203”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | Psychology 201 (does not meet Core)”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | Sociology 201 / Core 261”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | Math 115”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | Math 149”
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | 3 | Math 115 & 116”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 4 | Math 152”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | Business Administration 301”
### `0a00f971e9773491` Drake University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.drake.edu/admission-aid/financial-aid/types-resources/policies (sha256 9e4d3eaca8ca)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “COA budget increases related to a computer purchase are generally limited to one computer purchase per degree.”
### `2c909a9ca8a1f2a6` Drake University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/types-resources/policies/sap (sha256 765fb69ad57f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Process and Satisfactory Academic Progress Question The Financial Aid Committee will evaluate student appeals for restoration of aid.”
### `4622babaa6934c8f` Drake University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.drake.edu/admission-aid/financial-aid/types-resources/policies (sha256 9e4d3eaca8ca)
- issues: semantic_review_required, conflicting_sources:https://www.drake.edu/admission-aid/financial-aid/process,https://www.drake.edu/admission-aid/financial-aid/types-resources/forms,https://www.drake.edu/admission-aid/financial-aid/types-resources/policies/consumer-information
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Grade level classification is based on a student’s cumulative earned credit hours, as follows: | Classification | Earned Credit Hours | Freshman | Less than 30 | Sophomore | 30 to 59 | Junior | 60 to 89 | Senior | 90 or more Appeals for Special Circumstances Offers of need-based financial assistance are based on information reported on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Examples include a recent involuntary change in income, or atypical out-of-pocket medical expenses.”
### `67aafb2aeea5cd0a` Drake University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/types-resources/policies/consumer-information (sha256 09912c983dfc)
- issues: semantic_review_required, conflicting_sources:https://www.drake.edu/admission-aid/financial-aid/process,https://www.drake.edu/admission-aid/financial-aid/types-resources/forms,https://www.drake.edu/admission-aid/financial-aid/types-resources/policies
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Students may appeal an offer of financial aid if they believe it is unfair, incorrect, or based on incomplete information (including a recent change in financial circumstances).”
  - sentence: need_based_special_circumstances ⟵ “Appeals can be made by submitting an Appeal for Special Circumstances and submitting relevant supporting documentation.”
### `90a04725fe6b9e75` Drake University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/process (sha256 4e6e5f734431)
- issues: semantic_review_required, conflicting_sources:https://www.drake.edu/admission-aid/financial-aid/types-resources/forms,https://www.drake.edu/admission-aid/financial-aid/types-resources/policies,https://www.drake.edu/admission-aid/financial-aid/types-resources/policies/consumer-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you or your family has special circumstances that are impacting your ability to pay for college, you can submit a Financial Aid Appeal.”
### `f9194975e5905325` Drake University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.drake.edu/admission-aid/financial-aid/types-resources/forms (sha256 3f46bf0c0cf0)
- issues: semantic_review_required, conflicting_sources:https://www.drake.edu/admission-aid/financial-aid/process,https://www.drake.edu/admission-aid/financial-aid/types-resources/policies,https://www.drake.edu/admission-aid/financial-aid/types-resources/policies/consumer-information
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Common Admitted Student Tasks Consent for Disclosure of Financial Aid Records Form Report Your Outside Scholarships Financial Aid Application Forms Appeals for Special Circumstances - To submit an appeal, students can log into their FinAid Forms account and then click the “Request” button in the top right corner of the screen.”
### `301faa84f2717136` Drake University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.drake.edu/admission-aid/financial-aid/types-resources/policies/documents/2025-2026-student-budgets-11.30.2024.pdf (sha256 2ae02a84b739)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 12, "rows": 123}
  - column:Tuition: 51444 ⟵ “Tuition | 51,444 | 51,444 | 51,444 51,444 | 51,444 | 51,444 49,466 | 49,466 | 49,466 47,564 | 47,564 | 47,564”
  - column:Fees: 686 ⟵ “Fees | 686 | 686 | 686 | 516 | 516 | 516 | 516 | 516 | 516 | 516 | 516 | 516”
  - column:Course Ready*: 510 ⟵ “Course Ready* | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510”
  - column:Housing: 7048 ⟵ “Housing | 7048 | 7308 | 4617 | 7048 | 7308 | 4617 | 7048 | 7308 | 4617 | 7048 | 7308 | 4617”
  - column:Food: 5828 ⟵ “Food | 5828 | 3600 | 2160 | 5828 | 3600 | 2160 | 5828 | 3600 | 2160 | 5828 | 3600 | 2160”
  - column:Transportation: 1240 ⟵ “Transportation | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368”
  - column:Personal: 1935 ⟵ “Personal | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935”
  - column:Loan Fees: 261 ⟵ “Loan Fees | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261”
  - column:TOTAL: 68952 ⟵ “TOTAL | 68,952 | 67,112 | 62,981 68,782 | 66,942 | 62,811 66,804 | 64,964 | 60,833 64,902 | 63,062 | 58,931”
  - column:Tuition (2): 45734 ⟵ “Tuition | 45,734 | 45,734 | 45,734 44,188 | 44,188 | 44,188 42,694 | 42,694 | 42,694 41,250 | 41,250 | 41,250”
  - column:Fees (2): 516 ⟵ “Fees | 516 | 516 | 516 | 516 | 516 | 516 | 516 | 516 | 516 | 516 | 516 | 516”
  - column:Course Ready* (2): 510 ⟵ “Course Ready* | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510 | 510”
  - column:Housing (2): 7048 ⟵ “Housing | 7048 | 7308 | 4617 | 7048 | 7308 | 4617 | 7048 | 7308 | 4617 | 7048 | 7308 | 4617”
  - column:Food (2): 5828 ⟵ “Food | 5828 | 3600 | 2160 | 5828 | 3600 | 2160 | 5828 | 3600 | 2160 | 5828 | 3600 | 2160”
  - column:Transportation (2): 1240 ⟵ “Transportation | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368”
  - column:Personal (2): 1935 ⟵ “Personal | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935 | 1,935”
  - column:Loan Fees (2): 261 ⟵ “Loan Fees | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261 | 261”
  - column:TOTAL (2): 63072 ⟵ “TOTAL | 63,072 | 61,232 | 57,101 61,526 | 59,686 | 55,555 60,032 | 58,192 | 54,061 58,588 | 56,748 | 52,617”
  - column:Tuition (3): 27000 ⟵ “Tuition | 27,000 | 27,000 | 27,000 | 11,250 | 11,250 | 11,250”
  - column:Fees (3): 2072 ⟵ “Fees | 2,072 | 2,072 | 2,072 | 848 | 848 | 848”
  - column:Books/Supplies: 255 ⟵ “Books/Supplies | 255 | 255 | 255 | 0 | 0 | 0”
  - column:Housing (3): 7048 ⟵ “Housing | 7048 | 7308 | 4617 | 2210 | 2030 | 1,283”
  - column:Food (3): 5828 ⟵ “Food | 5828 | 3600 | 2160 | 1000 | 1000 | 600”
  - column:Transportation (3): 1240 ⟵ “Transportation | 1,240 | 1,368 | 1,368 | 344 | 380 | 380”
  - column:Personal (3): 1935 ⟵ “Personal | 1,935 | 1,935 | 1,935 | 538 | 538 | 538”
  - … 983 more rows
### `6719090a2f6af249` Drake University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.drake.edu/admission-aid/financial-aid/types-resources/policies/documents/2026-2027-drake-university-cost-of-attendance-budgets.pdf (sha256 35bcb5808052)
- issues: arrangement_unlabeled, multiple_total_rows
- checks: {"columns": 12, "rows": 109}
  - column:Tuition: 52988 ⟵ “Tuition | 52,988 | 52,988 | 52,988 51,444 | 51,444 | 51,444 51,444 | 51,444 | 51,444 49,466 | 49,466 | 49,466”
  - column:Fees: 780 ⟵ “Fees | 780 | 780 | 780 | 610 | 610 | 610 | 610 | 610 | 610 | 610 | 610 | 610”
  - column:Course Ready*: 534 ⟵ “Course Ready* | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534”
  - column:Housing: 7366 ⟵ “Housing | 7366 | 7308 | 5400 | 7366 | 7308 | 5400 | 7366 | 7308 | 5400 | 7366 | 7308 | 5400”
  - column:Food: 6150 ⟵ “Food | 6150 | 3600 | 2160 | 6150 | 3600 | 2160 | 6150 | 3600 | 2160 | 6150 | 3600 | 2160”
  - column:Transportation: 1240 ⟵ “Transportation | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368”
  - column:Personal: 2160 ⟵ “Personal | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160”
  - column:Loan Fees: 275 ⟵ “Loan Fees | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275”
  - column:TOTAL: 71493 ⟵ “TOTAL | 71,493 | 69,013 | 65,665 69,779 | 67,299 | 63,951 69,779 | 67,299 | 63,951 67,801 | 65,321 | 61,973”
  - column:Tuition (2): 47564 ⟵ “Tuition | 47,564 | 47,564 | 47,564 45,734 | 45,734 | 45,734 44,188 | 44,188 | 44,188 42,694 | 42,694 | 42,694”
  - column:Fees (2): 610 ⟵ “Fees | 610 | 610 | 610 | 610 | 610 | 610 | 610 | 610 | 610 | 610 | 610 | 610”
  - column:Course Ready* (2): 534 ⟵ “Course Ready* | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534 | 534”
  - column:Housing (2): 7366 ⟵ “Housing | 7366 | 7308 | 5400 | 7366 | 7308 | 5400 | 7366 | 7308 | 5400 | 7366 | 7308 | 5400”
  - column:Food (2): 6150 ⟵ “Food | 6150 | 3600 | 2160 | 6150 | 3600 | 2160 | 6150 | 3600 | 2160 | 6150 | 3600 | 2160”
  - column:Transportation (2): 1240 ⟵ “Transportation | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368 | 1,240 | 1,368 | 1,368”
  - column:Personal (2): 2160 ⟵ “Personal | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160 | 2,160”
  - column:Loan Fees (2): 275 ⟵ “Loan Fees | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275 | 275”
  - column:TOTAL (2): 65899 ⟵ “TOTAL | 65,899 | 63,419 | 60,071 64,069 | 61,589 | 58,241 62,523 | 60,043 | 56,695 61,029 | 58,549 | 55,201”
  - column:Tuition (3): 28800 ⟵ “Tuition | 28,800 | 28,800 | 28,800 | 12,000 | 12,000 | 12,000”
  - column:Fees (3): 2166 ⟵ “Fees | 2,166 | 2,166 | 2,166 | 858 | 858 | 858”
  - column:Books/Supplies: 267 ⟵ “Books/Supplies | 267 | 267 | 267 | 0 | 0 | 0”
  - column:Housing (3): 7366 ⟵ “Housing | 7366 | 7308 | 5400 | 2340 | 2030 | 1,500”
  - column:Food (3): 6150 ⟵ “Food | 6150 | 3600 | 2160 | 1000 | 1000 | 600”
  - column:Transportation (3): 1240 ⟵ “Transportation | 1,240 | 1,368 | 1,368 | 344 | 380 | 380”
  - column:Personal (3): 2160 ⟵ “Personal | 2,160 | 2,160 | 2,160 | 600 | 600 | 600”
  - … 923 more rows
### `1ecea090ea859aba` Eastern Iowa Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://eicc.edu/admission-aid/paying/financial/how-to/reviewing-satisfactory-academic-progress.aspx (sha256 56cb4f12c1e3)
- issues: semantic_review_required, conflicting_sources:https://eicc.edu/admission-aid/paying/financial/forms-policies/satisfactory-academic-progress-appeal.aspx
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If you see a red banner, you will need to submit a SAP Appeal.”
  - sentence: sap_appeal ⟵ “For instructions on the appeal process and a SAP Appeal form, click on ‘Satisfactory Academic Progress’ under Helpful Links.”
  - sentence: sap_appeal ⟵ “You will be directed to the appeal form and other relevant SAP information on EICC’s Satisfactory Academic Progress Appeals page.”
### `54b6323ddd1e6ed4` Eastern Iowa Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://eicc.edu/admission-aid/paying/financial/fa-101.aspx (sha256 ea576ca4a637)
- issues: semantic_review_required, conflicting_sources:https://eicc.edu/admission-aid/paying/financial/special-unusual-circumstances.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special & Unusual Circumstances Learn more about special circumstances More money for college Apply for these scholarships.”
### `5dae760e9f8c8e66` Eastern Iowa Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://eicc.edu/admission-aid/paying/financial/special-unusual-circumstances.aspx (sha256 aee1bfcac346)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: professional_judgment ⟵ “In this case, the Financial Aid Office has a process called Professional Judgment that allows us to review your special circumstances and, if approved, to recalculate your SAI and re-evaluate your financial aid package.”
  - sentence: professional_judgment ⟵ “Please note that if you already have an SAI of 0 or lower, there is no need to request a Professional Judgment because you are already receiving the maximum amount of financial aid available.”
  - sentence: professional_judgment ⟵ “You may qualify for an Unusual Circumstances Professional Judgment if you: Left home due to an abusive or threatening environment.”
  - sentence: professional_judgment ⟵ “If you believe you qualify for an Unusual Circumstances Professional Judgment, contact the Financial Aid Office to request an Unusual Circumstances form.”
  - sentence: professional_judgment ⟵ “Please note that submission of an Unusual Circumstances Professional Judgment request does not guarantee that the request will be approved.”
### `8135c756c30d6d7e` Eastern Iowa Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://eicc.edu/admission-aid/paying/financial/special-unusual-circumstances.aspx (sha256 aee1bfcac346)
- issues: semantic_review_required, conflicting_sources:https://eicc.edu/admission-aid/paying/financial/fa-101.aspx
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “However, there may be a special circumstance that reduces your ability to pay for college which is not accurately reflected on your FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Situations that may qualify as a special circumstance include: Loss of income from unemployment, furlough, disability, or retirement.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances form and Verification Worksheet.”
  - sentence: need_based_special_circumstances ⟵ “Please note that a review of special circumstances does not automatically guarantee an SAI adjustment or an increase in financial aid funding.”
  - sentence: need_based_special_circumstances ⟵ “To apply, contact the Financial Aid Office to request the Special Circumstances form.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances | If you are a dependent student according to the FAFSA, your financial aid eligibility is determined by using your and your parents’ income and asset information.”
### `993537d26d54eb00` Eastern Iowa Community College District — appeals 2026-27 [new] (source_unlabeled)
- source: https://eicc.edu/admission-aid/paying/financial/forms-policies/satisfactory-academic-progress-appeal.aspx (sha256 59f595ab2be6)
- issues: semantic_review_required, conflicting_sources:https://eicc.edu/admission-aid/paying/financial/how-to/reviewing-satisfactory-academic-progress.aspx
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Completing the SAP Appeal process.”
  - sentence: sap_appeal ⟵ “SAP Appeal You may appeal a SAP Suspension Status on the basis of: Serious injury or illness Death of a relative Other extenuating circumstances To appeal, complete the SAP Appeal Form and complete an Academic Plan with your advisor.”
### `d3ab50cd70d15cb6` Emmaus Bible College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.emmaus.edu/tuition-aid (sha256 71b817f7613e)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition*: 21950 ⟵ “Tuition* | $21,950”
  - column:Net Tuition†: 15950 ⟵ “Net Tuition† | $15,950”
  - column:Room & Board: 10200 ⟵ “Room & Board | $10,200”
  - column:Total (for 2 semesters): 26150 ⟵ “Total (for 2 semesters) | $26,150”
### `501e8b4fad19e763` Grand View University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.grandview.edu/admissions/financial-aid/special-circumstance-reporting (sha256 b8a86ded29bc)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.grandview.edu/filesimages/Admissions/Financial%20Aid/Apply/26-27/2026-27%20Special%20Circumstances.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “GV Next Tuition & Fees Special and Unusual Circumstances - Professional Judgement Special and/or Unusual circumstances may sometimes occur when your current financial or dependency situation is no longer accurately reflected on your FAFSA application.”
  - sentence: professional_judgment ⟵ “Section 479A of the HEA gives an institution’s FAA (Financial Aid Administrator) the authority to use professional judgment to adjust, on a case-by-case basis, the cost of attendance or the values of the items used in calculating the EFC to reflect a student’s special or unusual circumstances.”
### `7f761a10f2db29aa` Grand View University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.grandview.edu/filesimages/Admissions/Financial%20Aid/Special%20Circumstance%20Reporting/2025-26%20Request%20For%20Special%20Circumstances.pdf (sha256 0fe08345d8db)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The financial aid administrator may consider, under professional judgement, these unusual expenses when awarding financial aid.”
### `9ff3532bdd56b9b5` Grand View University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.grandview.edu/admissions/financial-aid/special-circumstance-reporting (sha256 b8a86ded29bc)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustments: Change in housing status.”
### `acd895ab42fae25f` Grand View University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.grandview.edu/filesimages/Admissions/Financial%20Aid/Apply/26-27/2026-27%20Special%20Circumstances.pdf (sha256 6b8fadfc9452)
- issues: semantic_review_required, conflicting_sources:https://www.grandview.edu/admissions/financial-aid/special-circumstance-reporting
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you or your family has experienced unusual circumstances, please complete this form and submit any required documentation to the Financial Aid Office.”
### `b48155e36d0f9aae` Grand View University — appeals 2025-26 [new] (labeled_in_title)
- source: https://www.grandview.edu/filesimages/Admissions/Financial%20Aid/Special%20Circumstance%20Reporting/2025-26%20Request%20For%20Special%20Circumstances.pdf (sha256 0fe08345d8db)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.grandview.edu/admissions/financial-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you or your family has experienced unusual circumstances, please complete this form and submit any required documentation to the Financial Aid Office.”
### `f1a6169e6e192a31` Grand View University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.grandview.edu/admissions/financial-aid/special-circumstance-reporting (sha256 b8a86ded29bc)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.grandview.edu/filesimages/Admissions/Financial%20Aid/Apply/26-27/2026-27%20Special%20Circumstances.pdf
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Reporting | Grand View University Warning!”
  - sentence: need_based_special_circumstances ⟵ “To be eligible for a Special Circumstance or Unusual Circumstance Appeal, you must be admitted to Grand View in a degree-seeking program and have filed a FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If you are selected for verification, this process must be completed before a Special Circumstance can be considered. 2026-27 Special Circumstance Request Form 2025-26 Special Circumstance Request Form Common Reasons to Submit a Special or Unusual Circumstance: Special Circumstance: Income Reduction Appeal Special Circumstances refer to financial situations (loss of a job, etc.) that justify an ai”
  - sentence: need_based_special_circumstances ⟵ “Abusive (physically and/or mentally) family environment Abandonment Parents cannot be located/no contact with any parent Other reasons A student may have both a special circumstance and an unusual circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Computer purchase Dependent care (e.g. daycare) expenses Extended Family Support Circumstances We Do Not Consider: Different university offering more aid Consumer debt, including credit card debt and car payments Parent's inability or unwillingness to borrow Federal Direct Parent PLUS Loans Parent refuses to provide financial support for higher education Parent refuses to complete or sign FAFSA Sp”
  - sentence: need_based_special_circumstances ⟵ “Read the instructions carefully as not all special circumstances qualify for an adjustment of federal financial aid.”
### `f6e38599795a9c93` Grand View University — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.grandview.edu/filesimages/Admissions/Financial%20Aid/Apply/26-27/2026-27%20Special%20Circumstances.pdf (sha256 6b8fadfc9452)
- issues: semantic_review_required, conflicting_sources:https://www.grandview.edu/admissions/financial-aid/special-circumstance-reporting
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The financial aid administrator may consider, under professional judgement, these unusual expenses when awarding financial aid.”
### `f846e8363b33d90c` Grand View University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/financial-aid (sha256 f14267acbb97)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://www.grandview.edu/filesimages/Admissions/Financial%20Aid/Special%20Circumstance%20Reporting/2025-26%20Request%20For%20Special%20Circumstances.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Presidential Scholarship - up to $21,000 Dean's Scholarship - up to $19,000 Director's Award - up to $17,000 GV Scholar's Award - up to $15,000 Grand View Grant - up to $13,000 | SAGE Scholars Tuition Rewards | GV Complete | Emergency Grant Funds | Tuition Exchange Program | Military Benefits | Student Employment Program | Special Circumstance Reporting | Academic Progress Standards Grand View Val”
### `34d97c35ac985a3c` Grand View University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/tuition/full-time (sha256 e24f136a1efb)
- issues: conflicting_sources:https://www.grandview.edu/filesimages/Admissions/International%20Students/intl_student_budget_undergrad2627_0426.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - on_campus:Tuition and fees: 37398 ⟵ “Tuition and fees | $37,398”
  - on_campus:Room and board (double w/All Access 5): 12364 ⟵ “Room and board (double w/All Access 5) | $12,364”
  - on_campus:Total: 49762 ⟵ “Total | $49,762”
### `4a6579f9028b4acc` Grand View University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.grandview.edu/admissions/tuition/25-26/full-time-day (sha256 66da0ff8f5ab)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.grandview.edu/filesimages/Admissions/International%20Students/intl_student_budget_undergrad2526.pdf
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - on_campus:Tuition and fees: 36412 ⟵ “Tuition and fees | $36,412”
  - on_campus:Room and board (double w/All Access 5): 11966 ⟵ “Room and board (double w/All Access 5) | $11,966”
  - on_campus:Total: 48378 ⟵ “Total | $48,378”
### `86262b44b88509ad` Grand View University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.grandview.edu/filesimages/Admissions/International%20Students/intl_student_budget_undergrad2627_0426.pdf (sha256 cd03933dce02)
- issues: arrangement_unlabeled, conflicting_sources:https://www.grandview.edu/admissions/tuition/full-time
- checks: {"columns": 3, "rows": 6}
  - column:Tuition: 36718 ⟵ “Tuition | $ 36,718 | $ 5,700”
  - column:Living expenses: 14646 ⟵ “Living expenses | $ 14,646 | $ 7,273”
  - column:Personal needs: 3654 ⟵ “Personal needs | $ 3,654 | $ 1,827”
  - column:Transportation: 3168 ⟵ “Transportation | $ 3,168 | –”
  - column:Health insurance (annual premium) $: 986 ⟵ “Health insurance (annual premium) $ | 986 | –”
  - column:Annual Total: 60628 ⟵ “Annual Total | $ 60,628 | $ 15,056”
  - column:Tuition: 5700 ⟵ “Tuition | $ 36,718 | $ 5,700”
  - column:Fees: 956 ⟵ “Fees | $ | 956 | $ | 0”
  - column:Living expenses: 7273 ⟵ “Living expenses | $ 14,646 | $ 7,273”
  - column:Personal needs: 1827 ⟵ “Personal needs | $ 3,654 | $ 1,827”
  - column:Books and materials: 500 ⟵ “Books and materials | $ | 500 | $ | 500”
  - column:Annual Total: 15056 ⟵ “Annual Total | $ 60,628 | $ 15,056”
  - column:Fees: 0 ⟵ “Fees | $ | 956 | $ | 0”
  - column:Books and materials: 500 ⟵ “Books and materials | $ | 500 | $ | 500”
### `a7df86bc3a7ff705` Grand View University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.grandview.edu/filesimages/Admissions/International%20Students/intl_student_budget_undergrad2526.pdf (sha256 8287ea4884bd)
- issues: arrangement_unlabeled, stale_year_label:2025-26, conflicting_sources:https://www.grandview.edu/admissions/tuition/25-26/full-time-day
- checks: {"columns": 4, "rows": 7}
  - column:Tuition: 35476 ⟵ “Tuition | $ 35,476 | $ 5,508”
  - column:Living expenses: 14290 ⟵ “Living expenses | $ 14,290 | $ 7,095”
  - column:Personal needs: 3564 ⟵ “Personal needs | $ 3,564 | $ 1,782”
  - column:Books and supplies: 1296 ⟵ “Books and supplies | $ 1,296 | $ | 648”
  - column:Transportation: 3220 ⟵ “Transportation | $ 3,220 | –”
  - column:Health insurance (annual premium) $: 986 ⟵ “Health insurance (annual premium) $ | 986 | –”
  - column:Annual Total: 59768 ⟵ “Annual Total | $ 59,768 | $ 15,033”
  - column:Tuition: 5508 ⟵ “Tuition | $ 35,476 | $ 5,508”
  - column:Fees: 936 ⟵ “Fees | $ | 936 | $ | 0”
  - column:Living expenses: 7095 ⟵ “Living expenses | $ 14,290 | $ 7,095”
  - column:Personal needs: 1782 ⟵ “Personal needs | $ 3,564 | $ 1,782”
  - column:Annual Total: 15033 ⟵ “Annual Total | $ 59,768 | $ 15,033”
  - column:Books and supplies: 648 ⟵ “Books and supplies | $ 1,296 | $ | 648”
  - column:Fees: 0 ⟵ “Fees | $ | 936 | $ | 0”
### `11fc15ceb63cef93` Grinnell College — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.grinnell.edu/admission/financial-aid/apply-aid/current-students (sha256 e87e244cc1f5)
- issues: semantic_review_required, conflicting_sources:https://www.grinnell.edu/admission/financial-aid/estimate-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If unusual circumstances are affecting your family’s resources (e.g., death of a parent, decrease in parent income, unusually high out-of-pocket medical expenses), you or your parent(s) should discuss those circumstances with a financial aid counselor.”
### `1c7b257b73a6ebf5` Grinnell College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.grinnell.edu/admission/financial-aid/types-aid/scholarships (sha256 17316d471e8f)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.grinnell.edu/admission/apply/first-year/early-decision,https://www.grinnell.edu/admission/financial-aid/apply-aid
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “However, eligibility may fluctuate if there are significant changes to family circumstances, especially changes to the number of siblings enrolled in college or a change in income.”
### `7416f1819bb263f3` Grinnell College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.grinnell.edu/admission/apply/first-year/early-decision (sha256 389ce9bff731)
- issues: semantic_review_required, conflicting_sources:https://www.grinnell.edu/admission/financial-aid/apply-aid,https://www.grinnell.edu/admission/financial-aid/types-aid/scholarships
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If your family has special circumstances or experiences a change in circumstances, email the Office of Financial Aid to inquire about the reconsideration request process.”
### `b6536c8f13185649` Grinnell College — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.grinnell.edu/admission/financial-aid/estimate-aid (sha256 6623cbd664be)
- issues: semantic_review_required, conflicting_sources:https://www.grinnell.edu/admission/financial-aid/apply-aid/current-students
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have special circumstances, such as a recent change to income or very high out-of-pocket medical expenses, you may want to speak to a financial aid counselor.”
### `d40389a772618933` Grinnell College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.grinnell.edu/admission/financial-aid/apply-aid (sha256 941be631bc04)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.grinnell.edu/admission/apply/first-year/early-decision,https://www.grinnell.edu/admission/financial-aid/types-aid/scholarships
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you are experiencing special or unusual circumstances, please feel free to provide additional information and documentation directly to the Office of Financial Aid using our secure site.”
### `f94cfd2910925269` Grinnell College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.grinnell.edu/sites/default/files/docs/2021-01/SAP_Policy_Final_2021_01_05.pdf (sha256 16d1ec6a1897)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “A student who fails to make Satisfactory Academic Progress and is placed on Financial Aid Suspension has the right to appeal.”
  - sentence: sap_appeal ⟵ “Appeals and Probationary Status A student that is unable to achieve Satisfactory Academic Progress, and as a result is placed on a Financial Aid Suspension, has the right to appeal based on special, unusual, or extenuating circumstances causing undue hardship.”
### `affdfec61c40c756` Grinnell College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.grinnell.edu/admission/financial-aid/cost-attendance (sha256 8dd631ecb762)
- issues: conflicting_sources:https://www.grinnell.edu/sites/default/files/docs/2026-09/Study%20Away%20Cost%20Estimator%20Merit%20Only%202026-27.xlsx
- checks: {"columns": 4, "rows": 5}
  - on_campus:Tuition*: 73582 ⟵ “Tuition* | $73,582 | $73,582 | $73,582 | $73,582”
  - on_campus:Activity Fee: 572 ⟵ “Activity Fee | $572 | $572 | $572 | $572”
  - on_campus:Housing**: 8316 ⟵ “Housing** | $8,316 | $9,148 | $8,316 | $1,400”
  - on_campus:Food^: 9468 ⟵ “Food^ | $9,468 | $9,468 | $9,468 | $2,600”
  - on_campus:MiscellaneousPersonalExpenses: 1100 ⟵ “MiscellaneousPersonalExpenses | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Tuition*: 73582 ⟵ “Tuition* | $73,582 | $73,582 | $73,582 | $73,582”
  - on_campus:Activity Fee: 572 ⟵ “Activity Fee | $572 | $572 | $572 | $572”
  - on_campus:Housing**: 9148 ⟵ “Housing** | $8,316 | $9,148 | $8,316 | $1,400”
  - on_campus:Food^: 9468 ⟵ “Food^ | $9,468 | $9,468 | $9,468 | $2,600”
  - on_campus:MiscellaneousPersonalExpenses: 1100 ⟵ “MiscellaneousPersonalExpenses | $1,100 | $1,100 | $1,100 | $1,100”
  - off_campus_not_with_family:Tuition*: 73582 ⟵ “Tuition* | $73,582 | $73,582 | $73,582 | $73,582”
  - off_campus_not_with_family:Activity Fee: 572 ⟵ “Activity Fee | $572 | $572 | $572 | $572”
  - off_campus_not_with_family:Housing**: 8316 ⟵ “Housing** | $8,316 | $9,148 | $8,316 | $1,400”
  - off_campus_not_with_family:Food^: 9468 ⟵ “Food^ | $9,468 | $9,468 | $9,468 | $2,600”
  - off_campus_not_with_family:MiscellaneousPersonalExpenses: 1100 ⟵ “MiscellaneousPersonalExpenses | $1,100 | $1,100 | $1,100 | $1,100”
  - with_parents_or_family:Tuition*: 73582 ⟵ “Tuition* | $73,582 | $73,582 | $73,582 | $73,582”
  - with_parents_or_family:Activity Fee: 572 ⟵ “Activity Fee | $572 | $572 | $572 | $572”
  - with_parents_or_family:Housing**: 1400 ⟵ “Housing** | $8,316 | $9,148 | $8,316 | $1,400”
  - with_parents_or_family:Food^: 2600 ⟵ “Food^ | $9,468 | $9,468 | $9,468 | $2,600”
  - with_parents_or_family:MiscellaneousPersonalExpenses: 1100 ⟵ “MiscellaneousPersonalExpenses | $1,100 | $1,100 | $1,100 | $1,100”
### `c3d250fbede743b5` Grinnell College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.grinnell.edu/sites/default/files/docs/2026-09/Study%20Away%20Cost%20Estimator%20Merit%20Only%202026-27.xlsx (sha256 3458171a5671)
- issues: arrangement_unlabeled, multiple_total_rows, conflicting_sources:https://www.grinnell.edu/admission/financial-aid/cost-attendance
- checks: {"columns": 16, "rows": 66}
  - column:Total Scholarships/Benefits:: 0 ⟵ “Total Scholarships/Benefits: | 0 | Find this by doubling the total scholarships/benefits credited to your most recent semester bill. Scholarships and tuition benefits (not tuition remission) are generally the same for fall and spring semest”
  - column:Tuition (includes books when on campus): 36791 ⟵ “Tuition (includes books when on campus) | 36791 | 36791 | 73582 | The higher of Grinnell or program tuition is charged for study away.”
  - column:Fees: 286 ⟵ “Fees | 286 | 286 | 572 | Optional fees, including those for pre-/post-program language intensives, are excluded.”
  - column:Housing: 4158 ⟵ “Housing | 4158 | 4158 | 8316 | Housing and Food represent the homestay option for study away; if there is no homestay”
  - column:Food: 4734 ⟵ “Food | 4734 | 4734 | 9468 | option, the lowest priced option is used when variable rates are quoted.”
  - column:Miscellaneous Personal Expenses: 550 ⟵ “Miscellaneous Personal Expenses | 550 | 550 | 1100 | Miscellaneous Personal Expenses reflect standard amounts.”
  - column:Total Scholarships/Benefits: 0 ⟵ “Total Scholarships/Benefits | 0 | 0 | 0 | This does not include tuition remission.”
  - column:Required Fees: 286 ⟵ “Required Fees | 286 | 286”
  - column:Grinnell or Program Tuition: 36791 ⟵ “Grinnell or Program Tuition | 36791 | 36791”
  - column:Other Required Charges: 8892 ⟵ “Other Required Charges | 8892 | 8892 | If you are in Grinnell, this assumes you live in basic, on-campus housing and have Meal Plan 1.”
  - column:Books Credit*: 0 ⟵ “Books Credit* | 0 | 0 | This appears as a credit, not a charge, on your bill during your study away semester.”
  - column:Total Estimated Bill: 45969 ⟵ “Total Estimated Bill | 45969 | 45969”
  - column:Total Scholarships/Benefits (2): 0 ⟵ “Total Scholarships/Benefits | 0 | 0 | This does not include tuition remission.”
  - column:Estimated Balance Due to Grinnell: 45969 ⟵ “Estimated Balance Due to Grinnell | 45969 | 45969 | This is the Total Estimated Bill minus Total Scholarships/Benefits.”
  - column:IA: 150 ⟵ “IA | 150 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46669 | Fall | 0”
  - column:IL: 150 ⟵ “IL | 150 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46669 | Spring | 0”
  - column:KS: 150 ⟵ “KS | 150 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46669”
  - column:MN: 150 ⟵ “MN | 150 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46669”
  - column:MO: 150 ⟵ “MO | 150 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46669”
  - column:NE: 150 ⟵ “NE | 150 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46669”
  - column:SD: 150 ⟵ “SD | 150 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46669”
  - column:WI: 150 ⟵ “WI | 150 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46669”
  - column:AR: 300 ⟵ “AR | 300 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46819”
  - column:CO: 300 ⟵ “CO | 300 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46819”
  - column:IN: 300 ⟵ “IN | 300 | 1250 | 1500 | 750 | 1000 | 1000 | 500 | 2250 | 1500 | 0 | 46819”
  - … 1806 more rows
### `ea5bf876b302ab9d` Grinnell College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.grinnell.edu/admission/financial-aid/cost-attendance (sha256 8dd631ecb762)
- issues: stale_year_label:2025-26
- checks: {"columns": 4, "rows": 5}
  - on_campus:Tuition*: 71788 ⟵ “Tuition* | $71,788 | $71,788 | $71,788 | $71,788”
  - on_campus:Activity Fee: 558 ⟵ “Activity Fee | $558 | $558 | $558 | $558”
  - on_campus:Housing**: 8112 ⟵ “Housing** | $8,112 | $8,924 | $8,112 | $1,400”
  - on_campus:Food^: 9236 ⟵ “Food^ | $9,236 | $9,236 | $9,236 | $2,600”
  - on_campus:MiscellaneousPersonalExpenses: 1100 ⟵ “MiscellaneousPersonalExpenses | $1,100 | $1,100 | $1,100 | $1,100”
  - on_campus:Tuition*: 71788 ⟵ “Tuition* | $71,788 | $71,788 | $71,788 | $71,788”
  - on_campus:Activity Fee: 558 ⟵ “Activity Fee | $558 | $558 | $558 | $558”
  - on_campus:Housing**: 8924 ⟵ “Housing** | $8,112 | $8,924 | $8,112 | $1,400”
  - on_campus:Food^: 9236 ⟵ “Food^ | $9,236 | $9,236 | $9,236 | $2,600”
  - on_campus:MiscellaneousPersonalExpenses: 1100 ⟵ “MiscellaneousPersonalExpenses | $1,100 | $1,100 | $1,100 | $1,100”
  - off_campus_not_with_family:Tuition*: 71788 ⟵ “Tuition* | $71,788 | $71,788 | $71,788 | $71,788”
  - off_campus_not_with_family:Activity Fee: 558 ⟵ “Activity Fee | $558 | $558 | $558 | $558”
  - off_campus_not_with_family:Housing**: 8112 ⟵ “Housing** | $8,112 | $8,924 | $8,112 | $1,400”
  - off_campus_not_with_family:Food^: 9236 ⟵ “Food^ | $9,236 | $9,236 | $9,236 | $2,600”
  - off_campus_not_with_family:MiscellaneousPersonalExpenses: 1100 ⟵ “MiscellaneousPersonalExpenses | $1,100 | $1,100 | $1,100 | $1,100”
  - with_parents_or_family:Tuition*: 71788 ⟵ “Tuition* | $71,788 | $71,788 | $71,788 | $71,788”
  - with_parents_or_family:Activity Fee: 558 ⟵ “Activity Fee | $558 | $558 | $558 | $558”
  - with_parents_or_family:Housing**: 1400 ⟵ “Housing** | $8,112 | $8,924 | $8,112 | $1,400”
  - with_parents_or_family:Food^: 2600 ⟵ “Food^ | $9,236 | $9,236 | $9,236 | $2,600”
  - with_parents_or_family:MiscellaneousPersonalExpenses: 1100 ⟵ “MiscellaneousPersonalExpenses | $1,100 | $1,100 | $1,100 | $1,100”
### `04650d364757cdea` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/ (sha256 fe099af165c1)
- issues: semantic_review_required, conflicting_sources:https://www.hawkeyecollege.edu/admissions-aid/financial-aid/apply,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/award-adjustment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/future-ready-iowa-last-dollar-scholarship
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Whether you're reviewing repayment details, submitting a special circumstances appeal, or checking what's required to keep your aid, these policies and resources will help you stay informed and on track.”
  - sentence: need_based_special_circumstances ⟵ “IRS Data Retrieval Tool Special Circumstances Appeals Life changes can impact your financial situation, and we’re here to help.”
### `2657a12aee3be1f8` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment (sha256 1d3cdaf78220)
- issues: semantic_review_required, conflicting_sources:https://www.hawkeyecollege.edu/admissions-aid/financial-aid/apply,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/award-adjustment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/future-ready-iowa-last-dollar-scholarship
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “However, if you need help with more detailed matters—like completing the FAFSA, verification paperwork, or navigating a special circumstance—you can schedule an appointment with our office.”
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances: Discuss your appeal or unique situation with a financial aid representative.”
  - sentence: need_based_special_circumstances ⟵ “Visit our Special and Unusual Circumstance Appeals web page for more information.”
### `2bfa80b0f356b70d` Hawkeye Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/future-ready-iowa-last-dollar-scholarship (sha256 d0b1fce92d11)
- issues: semantic_review_required, conflicting_sources:https://www.hawkeyecollege.edu/admissions-aid/financial-aid/apply,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/award-adjustment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances: If you discontinue enrollment or fall below the minimum enrollment due to exceptional circumstances beyond your control (i.e. military deployment, temporary medical incapacity, declaration of national or state emergency), contact the Financial Aid office to discuss your situation.”
### `3319d4e422d084a5` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/ (sha256 b762a2ac7451)
- issues: semantic_review_required, conflicting_sources:https://www.hawkeyecollege.edu/admissions-aid/financial-aid/apply,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/award-adjustment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/future-ready-iowa-last-dollar-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Whether you’re reviewing repayment details, submitting a special circumstances appeal, or checking what’s required to keep your aid, these policies and resources will help you stay informed and on track.”
### `4605164b5bc925fc` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals (sha256 38535b353dcc)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “Dependency Status Appeal or Parent Refusal If you’re considered a dependent student by financial aid rules, your eligibility for aid is based on both your income and assets and your parents’ income and assets.”
  - sentence: dependency_override ⟵ “In certain cases, the Financial Aid office may approve a Dependency Override Appeal if there are serious issues in the student’s relationship with their parents.”
### `55f99518130c0ba7` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/award-adjustment (sha256 a6b0c4a4e89f)
- issues: semantic_review_required, conflicting_sources:https://www.hawkeyecollege.edu/admissions-aid/financial-aid/apply,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/future-ready-iowa-last-dollar-scholarship
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances: If something unexpected happens, like a job loss or high medical expenses, contact the Financial Aid office.”
  - sentence: need_based_special_circumstances ⟵ “You may qualify for a Special Circumstances Appeal to adjust your aid based on your new situation.”
### `5a75aff79bc56fb9` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap-suspension-appeal (sha256 c7ede9d958f8)
- issues: semantic_review_required, conflicting_sources:https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-appeal.aspx,https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-worksheet.aspx,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “How to File an Appeal Complete the Satisfactory Academic Progress Appeal Form: On the appeal form, you'll explain why you didn't meet the SAP standards and what has changed since then.”
  - sentence: sap_appeal ⟵ “Supporting Documentation Submitting documentation with your Financial Aid Satisfactory Academic Progress Appeal strengthens your case by providing evidence of circumstances that affected your academic performance, such as medical issues or family emergencies.”
### `5b6c3ab62831f9b1` Hawkeye Community College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/apply (sha256 c9edb3747f56)
- issues: semantic_review_required, conflicting_sources:https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/award-adjustment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/future-ready-iowa-last-dollar-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Also, special circumstances like changes in your family's finances might affect your offer.”
### `68f4dfc496b5062c` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-worksheet.aspx (sha256 3b0f29ea8ba5)
- issues: semantic_review_required, conflicting_sources:https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-appeal.aspx,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap-suspension-appeal,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Worksheet Financial Aid Satisfactory Academic Progress Worksheet Home / Financial Aid / Managing Your Award / Suspension Appeals / Financial Aid Satisfactory Academic Progress Worksheet Login to My Hawkeye > WebAdvisor for Students > Financial Aid > Financial Aid Services > click on the RED banner at the top of the Financial Aid homepage for your Satisf”
### `90d2fa33d4b23d12` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/ (sha256 fe099af165c1)
- issues: semantic_review_required, conflicting_sources:https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-appeal.aspx,https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-worksheet.aspx,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap-suspension-appeal
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “If you are placed on financial aid suspension for not meeting the requirements of academic progress, you have the right to complete a Financial Aid Satisfactory Academic Progress Appeal to try to get your financial aid reinstated.”
### `aac8108a4f6f3d33` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals (sha256 38535b353dcc)
- issues: semantic_review_required, conflicting_sources:https://www.hawkeyecollege.edu/admissions-aid/financial-aid/apply,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/award-adjustment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/future-ready-iowa-last-dollar-scholarship
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “When we get a FAFSA with unusual circumstances flagged (like dependency status), we will email the student's Hawkeye email with next steps.”
### `d84cb80b9d92486a` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap (sha256 3c301854e429)
- issues: semantic_review_required, conflicting_sources:https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-appeal.aspx,https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-worksheet.aspx,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap-suspension-appeal,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Action: Complete a Satisfactory Academic Progress Appeal form if you have a valid reason (for example, illness or personal challenges).”
### `dbbddcf2c598d507` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment (sha256 42577c3c84ed)
- issues: semantic_review_required, conflicting_sources:https://www.hawkeyecollege.edu/admissions-aid/financial-aid/apply,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/award-adjustment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/special-circumstances-appeals,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/schedule-appointment,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/types/grants-scholarships/future-ready-iowa-last-dollar-scholarship
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “However, if you need help with more detailed matters—like completing the FAFSA, verification paperwork, or navigating a special circumstance—you can schedule an appointment with our office.”
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances: Discuss your appeal or unique situation with a financial aid representative.”
  - sentence: need_based_special_circumstances ⟵ “Visit our Special and Unusual Circumstance Appeals web page for more information.”
### `f8419cf3d6f79af2` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/ (sha256 b762a2ac7451)
- issues: semantic_review_required, conflicting_sources:https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-appeal.aspx,https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-worksheet.aspx,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap-suspension-appeal,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Aid Eligibility Requirements for Federal & State Aid Award Adjustment Reasons why your award may be adjusted Making Schedule or Program Changes Impact on your financial aid SAP Guidelines Keep moving forward in your program SAP Appeal Explain your situation & request a second chance Policies and Resources Explore the policies and resources that help you understand, secure, and maintain your financ”
### `fb25760ae9b69734` Hawkeye Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-appeal.aspx (sha256 41ead6ba799c)
- issues: semantic_review_required, conflicting_sources:https://prdwebapps.hawkeyecollege.edu/web-forms/financial-aid-sap-worksheet.aspx,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/managing-your-award/sap-suspension-appeal,https://www.hawkeyecollege.edu/admissions-aid/financial-aid/policies-resources/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Financial Aid Satisfactory Academic Progress Appeal Financial Aid Satisfactory Academic Progress Appeal Home / Financial Aid / Managing Your Award / Suspension Appeals / Financial Aid Satisfactory Academic Progress Appeal If you have started an appeal, check your email for the link to continue completing the appeal form.”
  - sentence: sap_appeal ⟵ “Subject line: Financial Aid Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Your appeal will not be sent to the Financial Aid Satisfactory Academic Progress Committee for review until both the online form and the Academic Planning Worksheet have have been completed.”
### `4446b4a4c5580ddd` Indian Hills Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://indianhills.edu/payingforcollege/docs/sap_policy.pdf (sha256 4503babbcb82)
- issues: semantic_review_required, conflicting_sources:https://indianhills.edu/payingforcollege/docs/finaidforms/_other/sap_appeal_form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You will receive NO AID for any future terms until you have fully maintained the above SAP requirements Appeals are handled on a case-by-case basis, and the appropriate form can be obtained from a Financial Aid Advisor or online at http://www.indianhills.edu/payingforcollege/finaid.php.”
  - sentence: sap_appeal ⟵ “An accepted SAP Appeal will place a student on PROBATION status.”
### `7f85176ada40dacb` Indian Hills Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://indianhills.edu/payingforcollege/docs/finaidforms/_other/sap_appeal_form.pdf (sha256 80062ab4977e)
- issues: semantic_review_required, conflicting_sources:https://indianhills.edu/payingforcollege/docs/sap_policy.pdf
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Financial Aid SAP Appeal Form Student’s Name: (Last) (First) (Maiden) Address: City State Zip Student’s ID Number Phone Financial Aid Standards for Satisfactory Academic Progress are established by the Department of Education to encourage students to successfully complete courses and progress satisfactorily toward program completion.”
  - sentence: sap_appeal ⟵ “Upon completion of the Academic Advising Worksheet, please submit all documentation to the OneStop at the appropriate campus.  Submit this completed SAP Appeal Form and the required attachments to the appropriate OneStop office in its entirety.”
  - sentence: sap_appeal ⟵ “Sap appeals must be submitted for review before the end of the term that is being appealed.”
  - sentence: sap_appeal ⟵ “Allow at least two weeks for a decision on all “SAP Appeals.” An accepted SAP Appeal will place the student on an Academic or Program Plan.”
  - sentence: sap_appeal ⟵ “You will receive NO AID for any future terms until you have fully maintained the above SAP requirements Appeals are handled on a case-by-case basis, and the appropriate form can be obtained from a Financial Aid Advisor or online at http://www.indianhills.edu/payingforcollege/finaid.php.”
  - sentence: sap_appeal ⟵ “An accepted SAP Appeal will place a student on PROBATION status.”
### `efbf44634afbbb48` Indian Hills Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://indianhills.edu/payingforcollege/docs/finaidforms/_other/sap_appeal_form.pdf (sha256 80062ab4977e)
- issues: semantic_review_required, conflicting_sources:https://indianhills.edu/payingforcollege/docs/sap_policy.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Successful appeals allowing a term of financial aid eligibility are entirely at the discretion and professional judgment of the SAP Committee in conjunction with the Financial Aid Director.”
  - sentence: professional_judgment ⟵ “Successful appeals allowing a term of financial aid eligibility are entirely at the discretion and professional judgment of the Financial Assistance Office, in conjunction with the Financial Aid Director.”
### `f8c0b1c81b029a7f` Indian Hills Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://indianhills.edu/payingforcollege/docs/sap_policy.pdf (sha256 4503babbcb82)
- issues: semantic_review_required, conflicting_sources:https://indianhills.edu/payingforcollege/docs/finaidforms/_other/sap_appeal_form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Successful appeals allowing a term of financial aid eligibility are entirely at the discretion and professional judgment of the Financial Assistance Office, in conjunction with the Financial Aid Director.”
### `184d6331e3fa6402` Iowa Central Community College — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.iowacentral.edu/admissions/forms/2025-25_Full_Cost_Of_Attendance.pdf (sha256 936a76d36901)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 3, "rows": 10}
  - column:**TUITION: 6480 ⟵ “**TUITION | 6480 | 6480 | 6480”
  - column:**FEES: 570 ⟵ “**FEES | 570 | 570 | 570”
  - column:1460: 1460 ⟵ “1460 | 1460 | 1460”
  - column:**ROOM & BOARD: 8900 ⟵ “**ROOM & BOARD | 8900 | 8900 | 4860”
  - column:*LOAN SERVICE CHG: 64 ⟵ “*LOAN SERVICE CHG | 64 | 107 | 64”
  - column:TRANSPORTATION: 2012 ⟵ “TRANSPORTATION | 2012 | 2012 | 2012”
  - column:PERSONAL: 1812 ⟵ “PERSONAL | 1812 | 2203 | 1290”
  - column:TOTAL COST:: 21298 ⟵ “TOTAL COST: | 21298 | 21732 | 16736”
  - column:2865: 2865 ⟵ “2865 | 2865”
  - column:TOTAL COST: (2): 24163 ⟵ “TOTAL COST: | 24163 | 24597”
  - column:**TUITION: 6480 ⟵ “**TUITION | 6480 | 6480 | 6480”
  - column:**FEES: 570 ⟵ “**FEES | 570 | 570 | 570”
  - column:1460: 1460 ⟵ “1460 | 1460 | 1460”
  - column:**ROOM & BOARD: 8900 ⟵ “**ROOM & BOARD | 8900 | 8900 | 4860”
  - column:*LOAN SERVICE CHG: 107 ⟵ “*LOAN SERVICE CHG | 64 | 107 | 64”
  - column:TRANSPORTATION: 2012 ⟵ “TRANSPORTATION | 2012 | 2012 | 2012”
  - column:PERSONAL: 2203 ⟵ “PERSONAL | 1812 | 2203 | 1290”
  - column:TOTAL COST:: 21732 ⟵ “TOTAL COST: | 21298 | 21732 | 16736”
  - column:TOTAL COST: (2): 24597 ⟵ “TOTAL COST: | 24163 | 24597”
  - column:**TUITION: 6480 ⟵ “**TUITION | 6480 | 6480 | 6480”
  - column:**FEES: 570 ⟵ “**FEES | 570 | 570 | 570”
  - column:**ROOM & BOARD: 4860 ⟵ “**ROOM & BOARD | 8900 | 8900 | 4860”
  - column:*LOAN SERVICE CHG: 64 ⟵ “*LOAN SERVICE CHG | 64 | 107 | 64”
  - column:TRANSPORTATION: 2012 ⟵ “TRANSPORTATION | 2012 | 2012 | 2012”
  - column:PERSONAL: 1290 ⟵ “PERSONAL | 1812 | 2203 | 1290”
  - … 1 more rows
### `fefd4c22eb9dcb92` Iowa Central Community College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.iowacentral.edu/admissions/forms/2026-27_Full_Cost_Of_Attendance.pdf (sha256 ef3585fe1eb4)
- issues: arrangement_unlabeled, multiple_total_rows
- checks: {"columns": 3, "rows": 10}
  - column:Tuition**: 6690 ⟵ “Tuition** | $6,690 | $6,690 | $6,690”
  - column:Fees**: 570 ⟵ “Fees** | $570 | $570 | $570”
  - column:Books/Supplies: 1460 ⟵ “Books/Supplies | $1,460 | $1,460 | $1,460”
  - column:Room & Board**: 9140 ⟵ “Room & Board** | $9,140 | $9,140 | $5,100”
  - column:Loan Service Charge*: 64 ⟵ “Loan Service Charge* | $64 | $107 | $64”
  - column:Transportation: 2060 ⟵ “Transportation | $2,060 | $2,060 | $2,060”
  - column:Personal: 1855 ⟵ “Personal | $1,855 | $2,256 | $1,321”
  - column:Total Cost (In-State): 21839 ⟵ “Total Cost (In-State) | $21,839 | $22,283 | $17,265”
  - column:Out-of-State Tuition**: 2865 ⟵ “Out-of-State Tuition** | $2,865 | $2,865 | $2,865”
  - column:Total Cost (Out-of-State): 24704 ⟵ “Total Cost (Out-of-State) | $24,704 | $25,148 | $20,130”
  - off_campus_not_with_family:Tuition**: 6690 ⟵ “Tuition** | $6,690 | $6,690 | $6,690”
  - off_campus_not_with_family:Fees**: 570 ⟵ “Fees** | $570 | $570 | $570”
  - off_campus_not_with_family:Books/Supplies: 1460 ⟵ “Books/Supplies | $1,460 | $1,460 | $1,460”
  - off_campus_not_with_family:Room & Board**: 9140 ⟵ “Room & Board** | $9,140 | $9,140 | $5,100”
  - off_campus_not_with_family:Loan Service Charge*: 107 ⟵ “Loan Service Charge* | $64 | $107 | $64”
  - off_campus_not_with_family:Transportation: 2060 ⟵ “Transportation | $2,060 | $2,060 | $2,060”
  - off_campus_not_with_family:Personal: 2256 ⟵ “Personal | $1,855 | $2,256 | $1,321”
  - off_campus_not_with_family:Total Cost (In-State): 22283 ⟵ “Total Cost (In-State) | $21,839 | $22,283 | $17,265”
  - off_campus_not_with_family:Out-of-State Tuition**: 2865 ⟵ “Out-of-State Tuition** | $2,865 | $2,865 | $2,865”
  - off_campus_not_with_family:Total Cost (Out-of-State): 25148 ⟵ “Total Cost (Out-of-State) | $24,704 | $25,148 | $20,130”
  - off_campus_not_with_family:Tuition**: 6690 ⟵ “Tuition** | $6,690 | $6,690 | $6,690”
  - off_campus_not_with_family:Fees**: 570 ⟵ “Fees** | $570 | $570 | $570”
  - off_campus_not_with_family:Books/Supplies: 1460 ⟵ “Books/Supplies | $1,460 | $1,460 | $1,460”
  - off_campus_not_with_family:Room & Board**: 5100 ⟵ “Room & Board** | $9,140 | $9,140 | $5,100”
  - off_campus_not_with_family:Loan Service Charge*: 64 ⟵ “Loan Service Charge* | $64 | $107 | $64”
  - … 5 more rows
### `284193ce6086637c` Iowa State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.iastate.edu/managing-your-aid/financial-aid-appeals/ (sha256 a6512a21a111)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Conditions Independent Appeals The Office of Student Financial Aid can use professional judgement to override a student’s dependency status from dependent to independent in some situations.”
### `4972b88dd408815e` Iowa State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.iastate.edu/getting-started/cost/ (sha256 5fac90b08b0b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustment You may be eligible to complete a cost of attendance adjustment form if your education-related expenses exceed the amount of financial aid included in your cost of attendance.”
  - sentence: budget_increase ⟵ “Veterinary Medicine Cost of Attendance Adjustment You make be eligible to adjust your cost of attendance if education-related expenses exceed the costs already built into your cost of attendance.”
### `409b32a9f0e9e1e7` Iowa State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.iastate.edu/admission-and-aid/admissions/first-year-students/credit-by-exam (sha256 3c561228a8ee)
- issues: credits_implausible
- checks: {"distinct_exams": 14, "equivalencies": 14, "rows_without_score": 0}
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|65]:  ⟵ “Financial Accounting* | 65 | Acct 2840 | 3”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|64]:  ⟵ “American Government | 64 | Pol Sci 1110 | 3”
  - equivalencies[CLEP-BIOLOGY|56]:  ⟵ “Biology** | 56 | Biol 1010 | 3”
  - equivalencies[CLEP-CALCULUS|64]:  ⟵ “Calculus | 64 | Math 1650 | 4”
  - equivalencies[CLEP-HUMANITIES|55]:  ⟵ “Humanities* | 55 | Fine Arts | 2”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|62]:  ⟵ “Macroeconomics, Principles of | 62 | Econ 1020 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|64]:  ⟵ “Microeconomics, Principles of | 64 | Econ 1010 | 3”
  - equivalencies[CLEP-NATURAL-SCIENCES|66]:  ⟵ “Natural Sciences* | 66 | Biological Science | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|55]:  ⟵ “Introductory Psychology | 55 | Psych 1010 | 3”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|63]:  ⟵ “Social Sciences and History* | 63 | Social Science | 4”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|56]:  ⟵ “Introductory Sociology | 56 | Soc 1340 | 3”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language** | 50 | French 1010French 1020 | 33”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language** | 50 | German 1010German 1020 | 33”
  - equivalencies[CLEP-SPANISH-LANGUAGE|50]:  ⟵ “Spanish Language*** | 50 | Spanish 1010Spanish 1020 | 33”
### `8eb0d1ca2cc9b2f9` Iowa Western Community College — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.iwcc.edu/students/records-and-registration/list-of-exams-accepted/ (sha256 8ffd11efe037)
- issues: credits_implausible
- checks: {"distinct_exams": 23, "equivalencies": 24, "rows_without_score": 0}
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Drawing | 3 | 3 | ART 133 Drawing I”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology | 4 | 4 | BIO 105 Introductory Biology”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB | 4 | 5 | MAT 211 Calculus I”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 5 | MAT 211 Calculus I”
  - equivalencies[AP-CALCULUS-BC|4]:  ⟵ “Calculus BC | 4 | 10 | MAT 211 Calculus IMAT 217 Calculus II”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 | CHM 122 Introduction to General Chemistry”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | 3 | CIS 127 Introduction to Programming”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language and Composition | 3 | 3 | ENG 105 Composition I”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature and Composition | 3 | 3 | LIT 101 Introduction to Literature”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | 4 | ENV 111 Environmental Science”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | 3 | GEO 121 World Geography”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | 3 | ECN 120 Principles of Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | 3 | ECN 130 Principles of Microeconomics”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | 8 | MUS 400 Music Theory and Practice IMUS 401 Music Theory and Practice IIMUS 410 Ear Training and Sight Singing IMUS 411 Ear Training and Sight Singing II”
  - equivalencies[AP-PHYSICS-1|5]:  ⟵ “Physics 1: Algebra-based | 5 | 41 | PHY 156 General Physics IPHY 157 General Physics I Lab”
  - equivalencies[AP-PHYSICS-2|4*]:  ⟵ “Physics 2: Algebra-based | 4* | 41 | PHY 156 General Physics IPHY 157 General Physics I Lab”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics | 4 | 41 | PHY 210 Classical Physics IPHY 211 Classical Physics I Lab”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4]:  ⟵ “Physics C: Electricity & Magnetism | 4 | 41 | PHY 220 Classical Physics IIPHY 221 Classical Physics II Lab”
  - equivalencies[AP-PRECALCULUS|4]:  ⟵ “Precalculus | 4 | 5 | MAT 129 Precalculus”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | 3 | PSY 111 Introduction to Psychology”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|3]:  ⟵ “Spanish Language and Culture | 3 | 8 | FLS 141 Elementary Spanish IFLS 142 Elementary Spanish II”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics | 3 | 4 | MAT 157 Statistics”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “United States History | 3 | 6 | HIS 151 US History to 1877HIS 152 US History Since 1877”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History | 3 | 6 | HIS 110 Western Civilization Ancient to Early ModernHIS 111 Western Civilization Early Modern to Present”
### `68c0832e2d43d21b` Iowa Western Community College — transfer_policies 2026-27 [new] (ambiguous_year_labels)
- source: https://www.iwcc.edu/students/records-and-registration/credit-transfer/ (sha256 16aff92153f1)
- issues: ambiguous_year_labels
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “A grade of “C” or higher is required for the credit to transfer, however, only the credit will be transferred.”
### `8a057dfe4c3bd259` Kirkwood Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kirkwood.edu/get-started/paying-for-college/index (sha256 31e14ed96223)
- issues: semantic_review_required, conflicting_sources:https://www.kirkwood.edu/_files/pdf/explore/services/financial_aid_sap_appeal_guide_access.pdf,https://www.kirkwood.edu/get-started/paying-for-college/academic-progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “MyHub About Us Search Search Submit Search Cancel Search Home Get Started Paying For College More Tuition & Costs Grants Federal Student Loans Private Student Loans Work-Study Special and Unusual Circumstances Checklist & Forms Accepting Your Award Academic Progress FAFSA Help Financial Aid FAQ CARES Act Information Paying for College Financial Aid Paying for college can be a challenge, but at Kir”
### `c3984131631d808e` Kirkwood Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kirkwood.edu/get-started/paying-for-college/academic-progress (sha256 d06052379f1b)
- issues: semantic_review_required, conflicting_sources:https://www.kirkwood.edu/_files/pdf/explore/services/financial_aid_sap_appeal_guide_access.pdf,https://www.kirkwood.edu/get-started/paying-for-college/index
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “MyHub About Us Search Search Submit Search Cancel Search Home Get Started Paying For College Academic Progress Satisfactory Academic Progress More Tuition & Costs Grants Federal Student Loans Private Student Loans Work-Study Special and Unusual Circumstances Checklist & Forms Accepting Your Award Academic Progress FAFSA Help Financial Aid FAQ CARES Act Information Keep Your Grades Up to Keep Your ”
### `c866f13ac1b7a0af` Kirkwood Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kirkwood.edu/_files/pdf/explore/services/financial_aid_sap_appeal_guide_access.pdf (sha256 50bb02f5a408)
- issues: semantic_review_required, conflicting_sources:https://www.kirkwood.edu/get-started/paying-for-college/index
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You may appeal your satisfactory academic progress (SAP) status if extenuating circumstances interfered with your ability to meet the SAP standards.”
  - sentence: sap_appeal ⟵ “Please note all information submitted will be reviewed by the Kirkwood Community College SAP Appeal Committee.”
### `e847b1555985a1ef` Kirkwood Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kirkwood.edu/get-started/paying-for-college/index (sha256 31e14ed96223)
- issues: semantic_review_required, conflicting_sources:https://www.kirkwood.edu/_files/pdf/explore/services/financial_aid_sap_appeal_guide_access.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Scholarship Application Parent Refusal Form Plus Pre-Approval Form Financial Aid SAP Appeal Guide Consortium Agreement “I chose Kirkwood because it’s close to home, affordable, and has a highly regarded nursing program.”
### `f7076ff81d98b6d6` Kirkwood Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.kirkwood.edu/_files/pdf/explore/services/financial_aid_sap_appeal_guide_access.pdf (sha256 50bb02f5a408)
- issues: semantic_review_required, conflicting_sources:https://www.kirkwood.edu/get-started/paying-for-college/academic-progress,https://www.kirkwood.edu/get-started/paying-for-college/index
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Other extenuating or unusual circumstance Submit appropriate documentation.”
### `55c861731c368cc3` Kirkwood Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.kirkwood.edu/get-started/paying-for-college/tuition-costs (sha256 bb0c31be4207)
- issues: ambiguous_year_labels, components_do_not_reconcile, residency_unknown
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - off_campus_not_with_family:Tuition and Fees:: 6512 ⟵ “Tuition and Fees: | $6,512”
  - off_campus_not_with_family:Food and Housing:: 10224 ⟵ “Food and Housing: | $10,224”
  - off_campus_not_with_family:Personal Expenses:: 3357 ⟵ “Personal Expenses: | $3,357”
  - off_campus_not_with_family:Books and Supplies:: 1000 ⟵ “Books and Supplies: | $1,000”
  - off_campus_not_with_family:Loan Fees:: 55 ⟵ “Loan Fees: | $55”
  - off_campus_not_with_family:Transportation:: 1740 ⟵ “Transportation: | $1,740”
  - off_campus_not_with_family:TOTAL:: 22888 ⟵ “TOTAL: | $22,888”
  - off_campus_not_with_family:Adjustment for out of state students:: 2156 ⟵ “Adjustment for out of state students: | $2,156”
### `2f545eb1688850fb` Loras College — appeals 2026-27 [new] (source_unlabeled)
- source: https://loras.edu/wp-content/uploads/SatisfactoryAcademicProgressGraduatePolicySAP.pdf (sha256 da01de663a8c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeals, Financial Aid Probation, and Academic Plans When a student loses eligibility for financial assistance because of failure to make SAP, the student may appeal in writing on the basis of: an injury or illness, the death of a relative, or other special circumstances.”
### `7da4997ced4b14fa` Luther College — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.luther.edu/admission-aid/cost-financial-aid/current (sha256 5ad4090a7544)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If there are special circumstances that affect your or your parent’s ability to contribute towards your educational expenses, please review the Special Circumstances Reporting section of our website.”
### `47dcf3c62ac1fc6b` Maharishi International University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.miu.edu/bfa-in-art (sha256 40160ddb6868)
- issues: cost_period_semester, conflicting_sources:https://www.miu.edu/ba-in-applied-arts-and-sciences,https://www.miu.edu/bachelors-specialization-in-life-and-wellness-coaching,https://www.miu.edu/cba/edd-in-transformational-leadership-and-coaching,https://www.miu.edu/cba/masters-in-consciousness-based-leadership-and-coaching,https://www.miu.edu/mfa-in-visual-art
- checks: {"columns": 1, "rows": 5}
  - on_campus:Tuition and fees: 9350 ⟵ “Tuition and fees | $9,350”
  - on_campus:Housing and meals: 3700 ⟵ “Housing and meals | $3,700”
  - on_campus:Health insurance (estimate): 1278 ⟵ “Health insurance (estimate) | $1,278”
  - on_campus:Your payment: 14328 ⟵ “Your payment | $14,328”
  - on_campus:Personal expenses and books (estimate): 1750 ⟵ “Personal expenses and books (estimate) | $1,750”
### `62c187ccefd09a7f` Maharishi International University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.miu.edu/bachelors-specialization-in-life-and-wellness-coaching (sha256 469fa5ff219e)
- issues: conflicting_sources:https://www.miu.edu/ba-in-applied-arts-and-sciences,https://www.miu.edu/bfa-in-art,https://www.miu.edu/cba/edd-in-transformational-leadership-and-coaching,https://www.miu.edu/cba/masters-in-consciousness-based-leadership-and-coaching,https://www.miu.edu/mfa-in-visual-art
- checks: {"columns": 1, "rows": 2}
  - column:Tuition and fees: 9200 ⟵ “Tuition and fees | $9,200”
  - column:Your payment: 0 ⟵ “Your payment | 0”
### `8feaec30560b4c42` Maharishi International University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.miu.edu/cba/masters-in-consciousness-based-leadership-and-coaching (sha256 703ec02507bf)
- issues: conflicting_sources:https://www.miu.edu/ba-in-applied-arts-and-sciences,https://www.miu.edu/bachelors-specialization-in-life-and-wellness-coaching,https://www.miu.edu/bfa-in-art,https://www.miu.edu/cba/edd-in-transformational-leadership-and-coaching,https://www.miu.edu/mfa-in-visual-art
- checks: {"columns": 1, "rows": 3}
  - column:Tuition and fees: 10000 ⟵ “Tuition and fees | $10,000”
  - column:Your payment: 0 ⟵ “Your payment | 0”
  - column:Additional federal loan for cash expenses: 2000 ⟵ “Additional federal loan for cash expenses | $2,000”
### `da44e059af2f8b31` Maharishi International University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.miu.edu/mfa-in-visual-art (sha256 2534f426c4ce)
- issues: conflicting_sources:https://www.miu.edu/ba-in-applied-arts-and-sciences,https://www.miu.edu/bachelors-specialization-in-life-and-wellness-coaching,https://www.miu.edu/bfa-in-art,https://www.miu.edu/cba/edd-in-transformational-leadership-and-coaching,https://www.miu.edu/cba/masters-in-consciousness-based-leadership-and-coaching
- checks: {"columns": 1, "rows": 3}
  - column:Tuition and fees: 9800 ⟵ “Tuition and fees | $9,800”
  - column:Your payment: 0 ⟵ “Your payment | 0”
  - column:Additional federal loan for cash expenses: 340 ⟵ “Additional federal loan for cash expenses | $340”
### `e42b79334808c09f` Maharishi International University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.miu.edu/ba-in-applied-arts-and-sciences (sha256 4860bd154297)
- issues: cost_period_semester, conflicting_sources:https://www.miu.edu/bachelors-specialization-in-life-and-wellness-coaching,https://www.miu.edu/bfa-in-art,https://www.miu.edu/cba/edd-in-transformational-leadership-and-coaching,https://www.miu.edu/cba/masters-in-consciousness-based-leadership-and-coaching,https://www.miu.edu/mfa-in-visual-art
- checks: {"columns": 1, "rows": 5}
  - on_campus:Tuition and fees: 9350 ⟵ “Tuition and fees | $9,350”
  - on_campus:Housing and meals: 3700 ⟵ “Housing and meals | $3,700”
  - on_campus:Health insurance (estimate): 1278 ⟵ “Health insurance (estimate) | $1,278”
  - on_campus:Your payment: 14328 ⟵ “Your payment | $14,328”
  - on_campus:Personal expenses and books (estimate): 1750 ⟵ “Personal expenses and books (estimate) | $1,750”
### `f7fb904fdaf93532` Maharishi International University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.miu.edu/cba/edd-in-transformational-leadership-and-coaching (sha256 6891f68f877e)
- issues: conflicting_sources:https://www.miu.edu/ba-in-applied-arts-and-sciences,https://www.miu.edu/bachelors-specialization-in-life-and-wellness-coaching,https://www.miu.edu/bfa-in-art,https://www.miu.edu/cba/masters-in-consciousness-based-leadership-and-coaching,https://www.miu.edu/mfa-in-visual-art
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 10000 ⟵ “Tuition | $10,000”
  - column:Your payment: 0 ⟵ “Your payment | 0”
  - column:Additional federal loan for cash expenses: 140 ⟵ “Additional federal loan for cash expenses | $140”
### `49cf4bf726a7f33f` Mount Mercy University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mtmercy.edu/tuition-aid/financial-aid/timeline-scholarship-renewal (sha256 639288524c6a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “A student may appeal the loss of scholarships.”
### `3a3c4e1a61b161c1` North Iowa Area Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.niacc.edu/estimated-cost-of-attendance/ (sha256 bc5342e9a970)
- issues: residency_unknown, conflicting_sources:https://www.niacc.edu/admissions/tuition-and-aid/tuition-and-expenses/
- checks: {"columns": 3, "components_reconcile": true, "rows": 6}
  - on_campus:Tuition & Fees:: 5213 ⟵ “Tuition & Fees: | $5213 | $5213 | $5213”
  - on_campus:Room & Board:: 6920 ⟵ “Room & Board: | $6920 | $5143 | $4324”
  - on_campus:Books & Supplies:: 986 ⟵ “Books & Supplies: | $986 | $986 | $986”
  - on_campus:Transportation:: 532 ⟵ “Transportation: | $532 | $1616 | $1616”
  - on_campus:Personal:: 1996 ⟵ “Personal: | $1996 | $1996 | $1996”
  - on_campus:Total:: 15647 ⟵ “Total: | $15,647 | $14,954 | $14,135”
  - off_campus_not_with_family:Tuition & Fees:: 5213 ⟵ “Tuition & Fees: | $5213 | $5213 | $5213”
  - off_campus_not_with_family:Room & Board:: 5143 ⟵ “Room & Board: | $6920 | $5143 | $4324”
  - off_campus_not_with_family:Books & Supplies:: 986 ⟵ “Books & Supplies: | $986 | $986 | $986”
  - off_campus_not_with_family:Transportation:: 1616 ⟵ “Transportation: | $532 | $1616 | $1616”
  - off_campus_not_with_family:Personal:: 1996 ⟵ “Personal: | $1996 | $1996 | $1996”
  - off_campus_not_with_family:Total:: 14954 ⟵ “Total: | $15,647 | $14,954 | $14,135”
  - with_parents_or_family:Tuition & Fees:: 5213 ⟵ “Tuition & Fees: | $5213 | $5213 | $5213”
  - with_parents_or_family:Room & Board:: 4324 ⟵ “Room & Board: | $6920 | $5143 | $4324”
  - with_parents_or_family:Books & Supplies:: 986 ⟵ “Books & Supplies: | $986 | $986 | $986”
  - with_parents_or_family:Transportation:: 1616 ⟵ “Transportation: | $532 | $1616 | $1616”
  - with_parents_or_family:Personal:: 1996 ⟵ “Personal: | $1996 | $1996 | $1996”
  - with_parents_or_family:Total:: 14135 ⟵ “Total: | $15,647 | $14,954 | $14,135”
### `c4981b9bdd868b8b` North Iowa Area Community College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.niacc.edu/admissions/tuition-and-aid/tuition-and-expenses/ (sha256 3d6d14b6a9e0)
- issues: residency_unknown, conflicting_sources:https://www.niacc.edu/estimated-cost-of-attendance/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees: 7020.0 ⟵ “Tuition & Fees | $7,020.00 | $7,020.00 | $7,020.00”
  - on_campus:Housing & Food: 10050.0 ⟵ “Housing & Food | $10,050.00 | $7,872.00 | $7,872.00”
  - on_campus:Books & Supplies: 1950.0 ⟵ “Books & Supplies | $1,950.00 | $1,950.00 | $1,950.00”
  - on_campus:Transportation: 668.0 ⟵ “Transportation | $668.00 | $7,172.00 | $7,172.00”
  - on_campus:Personal: 3110.0 ⟵ “Personal | $3,110.00 | $3,110.00 | $3,110.00”
  - on_campus:Loan Fee: 58.0 ⟵ “Loan Fee | $58.00 | $58.00 | $58.00”
  - on_campus:Total: 22856.0 ⟵ “Total | $22,856.00 | $27,182.00 | $27,182.00”
  - off_campus_not_with_family:Tuition & Fees: 7020.0 ⟵ “Tuition & Fees | $7,020.00 | $7,020.00 | $7,020.00”
  - off_campus_not_with_family:Housing & Food: 7872.0 ⟵ “Housing & Food | $10,050.00 | $7,872.00 | $7,872.00”
  - off_campus_not_with_family:Books & Supplies: 1950.0 ⟵ “Books & Supplies | $1,950.00 | $1,950.00 | $1,950.00”
  - off_campus_not_with_family:Transportation: 7172.0 ⟵ “Transportation | $668.00 | $7,172.00 | $7,172.00”
  - off_campus_not_with_family:Personal: 3110.0 ⟵ “Personal | $3,110.00 | $3,110.00 | $3,110.00”
  - off_campus_not_with_family:Loan Fee: 58.0 ⟵ “Loan Fee | $58.00 | $58.00 | $58.00”
  - off_campus_not_with_family:Total: 27182.0 ⟵ “Total | $22,856.00 | $27,182.00 | $27,182.00”
  - with_parents_or_family:Tuition & Fees: 7020.0 ⟵ “Tuition & Fees | $7,020.00 | $7,020.00 | $7,020.00”
  - with_parents_or_family:Housing & Food: 7872.0 ⟵ “Housing & Food | $10,050.00 | $7,872.00 | $7,872.00”
  - with_parents_or_family:Books & Supplies: 1950.0 ⟵ “Books & Supplies | $1,950.00 | $1,950.00 | $1,950.00”
  - with_parents_or_family:Transportation: 7172.0 ⟵ “Transportation | $668.00 | $7,172.00 | $7,172.00”
  - with_parents_or_family:Personal: 3110.0 ⟵ “Personal | $3,110.00 | $3,110.00 | $3,110.00”
  - with_parents_or_family:Loan Fee: 58.0 ⟵ “Loan Fee | $58.00 | $58.00 | $58.00”
  - with_parents_or_family:Total: 27182.0 ⟵ “Total | $22,856.00 | $27,182.00 | $27,182.00”
### `6d40be2169ee959c` Northeast Iowa Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nicc.edu/media/nicc/documents/financial-aid/SS.FAID.Supp.SAP.pdf (sha256 db1f04da07a9)
- issues: semantic_review_required, conflicting_sources:https://www.nicc.edu/financial-aid/satisfactory-academic-progress/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “SAP Appeal Request Student Services. • Take advantage of your resources; • etcentral.nicc.edu/#/form/104 • Continue progressing toward your goal. visit with your advisor & instructors, get help from • Appeal requirements: accessibility services, financial aid, the learning center, • Provide details of extenuating circumstances and use the GPA calculator. that led to not meeting SAP requirements • ”
  - sentence: sap_appeal ⟵ “To regain eligibility, you must meet SAP requirements or re-appeal after demonstrating success (complete 3 credits at NICC or another college with a minimum 2.0 GPA or successfully complete a non-credit training option).”
  - sentence: sap_appeal ⟵ “ADDITIONAL RESOURCES. • The full Satisfactory Academic Progress (SAP) policy is available at www.nicc.edu/appeal • GPA Calculators: gpacalculator.net/how-to-raise-gpa • Seek academic support at www.nicc.edu/academic-support • Keep your FAFSA updated each year at studentaid.gov • Contact our staff for help regaining SAP and understanding its financial implications Learn More.”
### `9640bf6620659f8f` Northeast Iowa Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nicc.edu/financial-aid/satisfactory-academic-progress/ (sha256 fd3b99344844)
- issues: semantic_review_required, conflicting_sources:https://www.nicc.edu/media/nicc/documents/financial-aid/SS.FAID.Supp.SAP.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Search under the Forms section, select and complete the Financial Aid SAP Appeal Request and Academic Plan for the appropriate school year.”
### `e78fa17b50b44eaa` Northeast Iowa Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.nicc.edu/financial-aid/special-circumstances/ (sha256 ad9a042e62f0)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “The FAFSA determines a student's aid eligibility, however some students and their families have unusual or special circumstances related to their finances or dependency status that may require a review and an adjustment to the FAFSA results.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances (Dependency Status) Students who are not considered independent according to the FAFSA questions may have unusual circumstances regarding their dependency status that may result in a change to the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Dependency Override An override may only be granted on a case-by-case basis for students with unusual circumstances.”
  - sentence: need_based_special_circumstances ⟵ “You may qualify for a dependency override if you are estranged from your parents due to parental incarceration, family alcoholism, drug abuse, parental abandonment, an abusive family environment that threatens your health or safety, or other unusual circumstances beyond your control.”
  - sentence: need_based_special_circumstances ⟵ “Students in this situation are encouraged to complete and submit the electronic request form in Student eForms - Special Circumstances Dependency Change Request (must include supporting documentation) Contact the Student Services Office at 563.562.3263, ext. 2700 for assistance Homeless Situation Students who are homeless, or at risk of becoming homeless, have options when completing the FAFSA.”
### `04dff7ecf023d8b3` Northeast Iowa Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.nicc.edu/admissions/transfer-information/transfer-agreements/ (sha256 c73fbaac53d3)
- issues: conflicting_values:min_grade
- checks: {"fields": []}
### `72fac8c7f01f83fc` Northwestern College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.nwciowa.edu/master-physician-assistant/tuition (sha256 cf21674dfdf0)
- issues: conflicting_sources:https://www.nwciowa.edu/master-physician-assistant/tuition,https://www.nwciowa.edu/tuition/cost-of-attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 93960 ⟵ “Tuition | $93,960”
  - column:Program fees: 4095 ⟵ “Program fees | $4,095”
  - column:Total tuition + fees: 98055 ⟵ “Total tuition + fees | $98,055”
### `7f01574193d8ed6c` Northwestern College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nwciowa.edu/tuition/cost-of-attendance (sha256 bceb39196fdd)
- issues: conflicting_sources:https://www.nwciowa.edu/master-physician-assistant/tuition,https://www.nwciowa.edu/master-physician-assistant/tuition
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition: 39000 ⟵ “Tuition | $39,000”
  - column:Avg. housing + food*: 11550 ⟵ “Avg. housing + food* | $11,550”
  - column:Books, supplies + equipment**: 1150 ⟵ “Books, supplies + equipment** | $1,150”
  - column:Transportation**: 1480 ⟵ “Transportation** | $1,480”
  - column:Misc. personal expenses**: 2140 ⟵ “Misc. personal expenses** | $2,140”
  - column:Technology fee: 320 ⟵ “Technology fee | $320”
  - column:Total (fall + spring): 55640 ⟵ “Total (fall + spring) | $55,640”
### `9d4975bb7edaa31f` Northwestern College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.nwciowa.edu/master-physician-assistant/tuition (sha256 9bec15e5a58d)
- issues: conflicting_sources:https://www.nwciowa.edu/master-physician-assistant/tuition,https://www.nwciowa.edu/tuition/cost-of-attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition: 93960 ⟵ “Tuition | $93,960”
  - column:Program fees: 4095 ⟵ “Program fees | $4,095”
  - column:Total tuition + fees: 98055 ⟵ “Total tuition + fees | $98,055”
### `e1ef93a08e3d6df6` Northwestern College — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.nwciowa.edu/financial-aid (sha256 0f30b37628b6)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 39000 ⟵ “Tuition | $39,000”
  - column:Housing*, food + fees: 11870 ⟵ “Housing*, food + fees | $11,870”
  - column:Average out-of-pocket: 17570 ⟵ “Average out-of-pocket | $17,570”
### `d93ddee29b6ceda5` Saint Ambrose University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://sau.edu/tuition-financial-aid/scholarships/ (sha256 360e106783c3)
- issues: ambiguous_year_labels, duplicate_table_versions
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '4.0+', 'amount_text': '$25,000'}, {'gpa': '3.8-3.99', 'amount_text': '$23,000'}, {'gpa': '3.2-3.79', 'amount_text': '$21,000'}, {'gpa': '2.8-3.19', 'amount_text': '$20,000'}] ⟵ “GPA | Scholarship || 4.0+ | $25,000 || 3.8-3.99 | $23,000 || 3.2-3.79 | $21,000 || 2.8-3.19 | $20,000”
  - gpa_requirement: Tiered by GPA: 4.0+ → $25,000; 3.8-3.99 → $23,000; 3.2-3.79 → $21,000; 2.8-3.19 → $20,000 ⟵ “GPA | Scholarship || 4.0+ | $25,000 || 3.8-3.99 | $23,000 || 3.2-3.79 | $21,000 || 2.8-3.19 | $20,000”
### `214c23950da74115` Southeastern Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.scciowa.edu/paying/aid/special-circumstances.aspx (sha256 141023ff1364)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “It is very important to note that when it comes to dependency overrides, there is a distinction between parents who are unable to provide information and parents who are unwilling to complete the FAFSA.”
### `4070932213ddabeb` Southeastern Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.scciowa.edu/paying/aid/special-circumstances.aspx (sha256 141023ff1364)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “If you believe you qualify for an Unusual Circumstances Professional Judgment, contact the Financial Aid Office to request an Unusual Circumstances form.”
  - sentence: professional_judgment ⟵ “Please note that submission of an Unusual Circumstances Professional Judgment request does not guarantee that the request will be approved.”
### `4b531cb4dbc0dae8` Southeastern Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.scciowa.edu/start/admissions/orientation/pre-enroll-finances.aspx (sha256 62ae58d5b7dc)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances The federal government's method of applying for financial aid is not perfect, but it's the only system they have.”
  - sentence: need_based_special_circumstances ⟵ “Those are called "special circumstances." Examples include a death in the family or a loss of a job.”
  - sentence: need_based_special_circumstances ⟵ “If you feel you have a special circumstance, please contact the Financial Aid Office after you have applied for financial aid.”
### `4f6a7ee9dc0e1863` Southeastern Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.scciowa.edu/paying/aid/special-circumstances.aspx (sha256 141023ff1364)
- issues: semantic_review_required, conflicting_sources:https://programs.scciowa.edu/current/admissions/financial-aid-sap-general.aspx,https://www.scciowa.edu/paying/,https://www.scciowa.edu/paying/aid/sap/
- checks: {"negative_sentences": 0, "sentences": 14}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances | SCC Iowa Close Start Here Apply Visit SCC Admissions New Students Adult Students Connect with Us Pre-Enrollment Info Guest Students Supporting Your Student Testing Services International Students Admissions FAQs Admissions Calendar High School Students Jump Start Career Academies MPOWER U STEP Program Tips for Parents High School FAQs For Parents Request Info Explore Career”
  - sentence: need_based_special_circumstances ⟵ “Sometimes there may be a special circumstance that reduces a student's ability to pay for college which cannot be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “The Financial Aid Office has a process that allows the FAFSA applicant to document a special circumstance and, if approved, allows us to recalculate a student’s SAI to re-evaluate a financial aid package.”
  - sentence: need_based_special_circumstances ⟵ “Situations that may qualify as special circumstance for FAFSA adjustments include: Loss of income from unemployment, furlough, disability, or retirement Unreimbursed medical and dental expenses for an exceptional medical emergency or incident.”
  - sentence: need_based_special_circumstances ⟵ “Note: Unreimbursed means health care expenses not covered by insurance or third party Legal separation or divorce Death of a family member whose income was reported on the FAFSA Termination of child support, alimony, or worker's compensation As part of this process, FAFSA data will be verified prior to the special circumstances review.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances form and Verification Worksheet Documentation of untaxed income (if applicable).”
### `a88e85b49b118223` Southeastern Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://programs.scciowa.edu/current/admissions/financial-aid-sap-general.aspx (sha256 6703b51b1b73)
- issues: semantic_review_required, conflicting_sources:https://www.scciowa.edu/paying/,https://www.scciowa.edu/paying/aid/sap/,https://www.scciowa.edu/paying/aid/special-circumstances.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If a student is placed on dismissal and a special circumstance exists, the student may submit an appeal.”
### `abc2bbd9c4c2e737` Southeastern Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.scciowa.edu/paying/aid/sap/ (sha256 e708e22c951e)
- issues: semantic_review_required, conflicting_sources:https://programs.scciowa.edu/current/admissions/financial-aid-sap-general.aspx,https://www.scciowa.edu/paying/,https://www.scciowa.edu/paying/aid/special-circumstances.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If special circumstances exist, the student may submit a letter of appeal to the Financial Aid Office stating the reasons the standards requirements noted above were not met.”
### `b54e17b8cf1dfcd4` Southeastern Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.scciowa.edu/paying/ (sha256 a79ff4b87288)
- issues: semantic_review_required, conflicting_sources:https://programs.scciowa.edu/current/admissions/financial-aid-sap-general.aspx,https://www.scciowa.edu/paying/aid/sap/,https://www.scciowa.edu/paying/aid/special-circumstances.aspx
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Tuition & Costs Refund Schedule Student Budgets Financial Aid Loans Grants Work-study Apply for Financial Aid Academic Progress (SAP) FAFSA Help Financial Aid FAQs Net Price Calculator Gainful Employment Special Circumstances Scholarships Foundation Scholarships Transfer Scholarships External Scholarships Tips for Writing Ways to Pay Manage Your Money Financial Aid Checklist & Forms Home Paying SC”
### `0deb224d95fca52b` Southeastern Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.scciowa.edu/programs/transfer/transfer-4yr-colleges.aspx (sha256 edaf7b761dca)
- issues: conflicting_values:max_transfer_credits
- checks: {"fields": ["residency_requirement_credits"]}
  - residency_requirement_credits: 30 ⟵ “A minimum of 30 semester hours must be completed while in residence at Drake.”
### `77dcb9d52e9f7f85` University of Dubuque — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.dbq.edu/AdmissionAid/FinancialAid/FinancialAidResources/ (sha256 757469c05308)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Students may pursue an adjustment on their FAFSA based on special or unusual circumstances by completing a Special Circumstances Request Form.”
  - sentence: need_based_special_circumstances ⟵ “The Special Circumstances Request Form along with other forms can be located on the Financial Aid Forms webpage.”
### `9e885f99390cbf17` University of Dubuque — appeals 2026-27 [new] (labeled_in_heading)
- source: https://www.dbq.edu/AdmissionAid/FinancialAid/HowtoApply/ (sha256 a0cbbed0b433)
- issues: semantic_review_required, conflicting_sources:https://www.dbq.edu/media/Admissions/FinancialAid/SAP-Policy-Undergraduate.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you or a contributor had a significant change in income, contact the Student Financial Planning Office at 563.589.3170 or FinAid@dbq.edu for a Special Circumstances Request Form.”
### `c8bf9877f890550b` University of Dubuque — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.dbq.edu/media/Admissions/FinancialAid/SAP-Policy-Undergraduate.pdf (sha256 696bb5e29d80)
- issues: semantic_review_required, conflicting_sources:https://www.dbq.edu/AdmissionAid/FinancialAid/HowtoApply/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The student then has the right to appeal the suspension of financial aid by indicating in writing to the Dean of Student Financial Planning and Scholarships: A. the reasons regarding failure in maintaining satisfactory academic progress (for example the death of a relative, an injury or illness of the student, or other special circumstances) B. what has changed that will allow the student to meet ”
### `060314339a8f4fbf` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap (sha256 1852e4e7437c)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy,https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If you exceed the hours attempted (all hours taken including W, F, U, N, O, and I grades) listed below, a SAP appeal will be required to receive financial aid.”
  - sentence: sap_appeal ⟵ “College of Liberal Arts & Sciences = 180 hours Tippie College of Business = 180 hours College of Education = 180 hours University College = 180 hours College of Engineering = 192 hours College of Nursing = 192 hours College of Public Health = 180 hours College of Medicine = 180 hours If you exceed your duration of eligibility, you must file the SAP Appeal Form in MyUI to be considered for extended”
### `4007ceb8e31e2d74` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy (sha256 0a3442df80c9)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap,https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 13}
  - sentence: sap_appeal ⟵ “Students who do not meet the GPA requirement for SAP after the spring semester are no longer eligible for federal financial aid and must complete a SAP appeal to receive federal financial aid for the subsequent semester.”
  - sentence: sap_appeal ⟵ “If you exceed the hours attempted (all hours taken including W, F, U, N, O, and I grades) listed below, a SAP appeal will be required to receive financial aid.”
  - sentence: sap_appeal ⟵ “College of Liberal Arts & Sciences = 180 hours Tippie College of Business = 180 hours College of Education = 180 hours University College = 180 hours College of Engineering = 192 hours College of Nursing = 192 hours College of Public Health = 180 hours College of Medicine = 180 hours If you exceed your duration of eligibility, you must file the SAP Appeal Form in MyUI to be considered for extended”
  - sentence: sap_appeal ⟵ “If you exceed the number of attempted credit hours (all UI graduate courses taken including W, F, U, N, O, and I grades) listed below then you will have reached the duration limit for the program, and you must file a SAP Appeal to regain financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Students with an approved SAP appeal are placed on financial aid probation for one semester.”
  - sentence: sap_appeal ⟵ “If a student does not complete these requirements after one semester on financial aid probation, they are no longer eligible for financial aid for the next semester and must submit an additional SAP appeal.”
### `ac7db7f1e8feaf60` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/cost/appealing-costs (sha256 da3169709a79)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “All requests are reviewed using Professional Judgment and must include complete and accurate documentation.”
  - sentence: professional_judgment ⟵ “Decisions are made at the discretion of the Office of Student Financial Aid based on federal Professional Judgement guidelines.”
### `e6178214d5298078` University of Iowa — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf (sha256 5f35b03d2c68)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Incompletes An Incomplete will count as not passing all requisite coursework and therefore would result in a student not meeting SAP standards and an appeal would be needed.”
  - sentence: sap_appeal ⟵ “Withdrawals A withdrawn course will count as not passing all requisite coursework and therefore would result in a student not meeting SAP standards and an appeal would be needed.”
### `f7406533a206ba5b` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress (sha256 a9246c4591d0)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap,https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 18}
  - sentence: sap_appeal ⟵ “If you are not meeting SAP standards, submitting a SAP appeal is strongly encouraged.”
  - sentence: sap_appeal ⟵ “The SAP appeal process exists to support students who experience academic challenges, and historically, nearly all first-time SAP appeals submitted with a complete statement and plan are approved.”
  - sentence: sap_appeal ⟵ “Students who lose financial aid eligibility due to not meeting SAP requirements may: submit a SAP Appeal or earn the necessary GPA or semester hours to meet the minimum requirements while not receiving federal financial aid Regaining SAP Eligibility Students who are not meeting SAP requirements for GPA or pace may regain eligibility on their own without submitting an appeal by attending and achiev”
  - sentence: sap_appeal ⟵ “The same process applies to students who have submitted a SAP appeal that has been denied; they can attend without the use of federal financial aid.”
  - sentence: sap_appeal ⟵ “Students who have been denied a SAP appeal can re-appeal after one semester without federal aid.”
  - sentence: sap_appeal ⟵ “SAP for Undergraduates SAP for Graduates Your SAP Status Explained | SAP Status | Next Steps | Eligible | You are meeting SAP standards and don't need to do anything. | GPA - Not Eligible | You can either: Submit a SAP Appeal by the deadline each semester as noted below.”
### `562b12082c49064d` University of Iowa — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.uiowa.edu/finances/estimated-costs-attendance (sha256 ff179a2fabcf)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 7}
  - on_campus:Tuition & fees*: 11971 ⟵ “Tuition & fees* | $11,971 | $34,247”
  - on_campus:Housing & food**: 14022 ⟵ “Housing & food** | $14,022 | $14,022”
  - on_campus:Total billed expenses: 25993 ⟵ “Total billed expenses | $25,993 | $48,269”
  - on_campus:Books & supplies: 950 ⟵ “Books & supplies | $950 | $950”
  - on_campus:Personal expenses***: 3648 ⟵ “Personal expenses*** | $3,648 | $3,648”
  - on_campus:Transportation: 1254 ⟵ “Transportation | $1,254 | $1,254”
  - on_campus:Total estimated expenses: 5852 ⟵ “Total estimated expenses | $5,852 | $5,852”
### `7dc39fc96314776e` University of Iowa — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.uiowa.edu/finances/estimated-costs-attendance (sha256 ff179a2fabcf)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 7}
  - on_campus:Tuition & fees*: 34247 ⟵ “Tuition & fees* | $11,971 | $34,247”
  - on_campus:Housing & food**: 14022 ⟵ “Housing & food** | $14,022 | $14,022”
  - on_campus:Total billed expenses: 48269 ⟵ “Total billed expenses | $25,993 | $48,269”
  - on_campus:Books & supplies: 950 ⟵ “Books & supplies | $950 | $950”
  - on_campus:Personal expenses***: 3648 ⟵ “Personal expenses*** | $3,648 | $3,648”
  - on_campus:Transportation: 1254 ⟵ “Transportation | $1,254 | $1,254”
  - on_campus:Total estimated expenses: 5852 ⟵ “Total estimated expenses | $5,852 | $5,852”
### `04c6822125d3cf72` University of Northern Iowa — appeals 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/eligibility/satisfactory-academic-progress (sha256 e62ea39c2f1a)
- issues: semantic_review_required, conflicting_sources:https://admissions.uni.edu/financial-aid/sap-appeal-form,https://admissions.uni.edu/sites/default/files/inline-uploads/sap_plan_of_study_1_1.pdf,https://admissions.uni.edu/sites/default/files/inline-uploads/sap_third_party_documentation_consent_form_0.pdf
- checks: {"negative_sentences": 0, "sentences": 7}
  - sentence: sap_appeal ⟵ “Reinstatement of Financial Aid If you’re placed on Financial Aid Suspension, you have the opportunity to complete an SAP Appeal.”
  - sentence: sap_appeal ⟵ “Below are the options for aid reinstatement: Option 1: Complete an SAP Appeal Financial Aid SAP Appeals must demonstrate extenuating circumstances that impeded your ability to make progress academically.”
  - sentence: sap_appeal ⟵ “SAP Appeal If your financial aid has been suspended due to not meeting the SAP requirements, we strongly encourage you to complete an appeal.”
  - sentence: sap_appeal ⟵ “Third Party Documentation Examples Documentation is an important piece of the SAP Appeal process and can help support what you discuss in your essay and strengthen your overall appeal.”
  - sentence: sap_appeal ⟵ “Denied Appeals If your SAP appeal is denied, you may continue attending UNI by paying out-of-pocket or by exploring alternative private education loan options.”
  - sentence: sap_appeal ⟵ “The SAP Appeal is an online appeal form and you may upload the Plan of Study and third party documentation directly into the form.”
### `4621f1641bbc5b10` University of Northern Iowa — appeals 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/receiving-financial-aid (sha256 db9e014e238b)
- issues: semantic_review_required, conflicting_sources:https://admissions.uni.edu/financial-aid/receiving-financial-aid/fafsa,https://admissions.uni.edu/financial-aid/receiving-financial-aid/special-circumstances
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Learn More About Verification Previous Next 3/3 Special Circumstances When you complete the FAFSA, you will use tax and income information from two years prior.”
  - sentence: need_based_special_circumstances ⟵ “If your financial situation has changed and the information on the FAFSA no longer accurately represents your current financial situation, you may want to consider completing a special circumstance appeal.”
  - sentence: need_based_special_circumstances ⟵ “Learn More About Special Circumstances Previous Next Additional Information Required Readings Financial Aid Timeline Financial Aid Offer 1227 W 27th St Cedar Falls, Iowa 50614 319-273-2311 Maps & Directions Bookstore Safety InsideUNI Careers at UNI Free Speech at UNI Copyright 2026 Maintained by IT-Client Services Facebook X Youtube LinkedIn Instagram Equal Opportunity/Non-Discrimination Statement”
### `58ed79579f99e672` University of Northern Iowa — appeals 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/receiving-financial-aid/special-circumstances (sha256 992514af6fc5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: budget_increase ⟵ “Budget Adjustment The maximum amount of financial aid you can receive is limited to your total Cost of Attendance.”
  - sentence: budget_increase ⟵ “If you have accepted financial aid up to the total Cost of Attendance but still need additional funding, contact our office to inquire about a budget adjustment.”
  - sentence: budget_increase ⟵ “If a budget adjustment is approved, we would increase your Cost of Attendance, which may allow you to receive more financial aid.”
  - sentence: budget_increase ⟵ “Below is a list of circumstances for which a budget adjustment may be considered.”
### `65b6774e2a213db4` University of Northern Iowa — appeals 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/receiving-financial-aid/fafsa (sha256 2a6dd71f2318)
- issues: semantic_review_required, conflicting_sources:https://admissions.uni.edu/financial-aid/receiving-financial-aid,https://admissions.uni.edu/financial-aid/receiving-financial-aid/special-circumstances
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances If you’re experiencing hardship or changes that are not reflected within the FAFSA and are impacting your or your family’s ability to contribute to educational expenses, a special circumstances appeal can help you receive adequate aid for your situation.”
  - sentence: need_based_special_circumstances ⟵ “To inquire about a special circumstances appeal, a FAFSA must already be on file.”
  - sentence: need_based_special_circumstances ⟵ “Learn More About Special Circumstances Verification Verification is a process used to confirm that the information you provided on your Free Application for Federal Student Aid (FAFSA) is accurate.”
### `676457fd8ddaa734` University of Northern Iowa — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.uni.edu/financial-aid/sap-appeal-form (sha256 804a9d121ad9)
- issues: semantic_review_required, conflicting_sources:https://admissions.uni.edu/financial-aid/eligibility/satisfactory-academic-progress,https://admissions.uni.edu/sites/default/files/inline-uploads/sap_plan_of_study_1_1.pdf,https://admissions.uni.edu/sites/default/files/inline-uploads/sap_third_party_documentation_consent_form_0.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The SAP Appeal committee meets once a week to review appeals.”
### `bebb173fa085b8ca` University of Northern Iowa — appeals 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/receiving-financial-aid/special-circumstances (sha256 992514af6fc5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Computer purchase Commuting expenses Car repairs Child care expenses (to learn more about additional child care assistance opportunities, please visit the Iowa Department of Human Services website) Unusual Circumstances - Dependency Override If there are unusual circumstances where a student cannot provide parent information on the FAFSA, such as: abuse, neglect, or abandonment, the UNI Office of ”
### `e22ee7580e702ac7` University of Northern Iowa — appeals 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/receiving-financial-aid/special-circumstances (sha256 992514af6fc5)
- issues: semantic_review_required, conflicting_sources:https://admissions.uni.edu/financial-aid/receiving-financial-aid,https://admissions.uni.edu/financial-aid/receiving-financial-aid/fafsa
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Our office will run a simulation to see if it will be beneficial to complete the Special Circumstance process and notify you via email.”
  - sentence: need_based_special_circumstances ⟵ “If the simulation determines the process will be beneficial, you will be asked to complete a Special Circumstance Appeal form and provide details and documentation about the change in your family’s situation.”
  - sentence: need_based_special_circumstances ⟵ “We need to determine that the current information on your FAFSA is correct, before we make adjustments due to the special circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Situations Not Considered for Review​ Expenses related to personal living (payments on consumer debts, personal loan payments, or other miscellaneous expenses) Bankruptcy, foreclosures, or collection costs One time increases on income (gambling winnings, inheritance, insurance or divorce settlements) Tuition for elementary/secondary education Please note: this list is not exclusive and other situa”
  - sentence: need_based_special_circumstances ⟵ “Documentation will be requested and required to support any special circumstance appeal.”
### `f23dd86a87820faa` University of Northern Iowa — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.uni.edu/sites/default/files/inline-uploads/sap_plan_of_study_1_1.pdf (sha256 137bfec4855d)
- issues: semantic_review_required, conflicting_sources:https://admissions.uni.edu/financial-aid/eligibility/satisfactory-academic-progress,https://admissions.uni.edu/financial-aid/sap-appeal-form,https://admissions.uni.edu/sites/default/files/inline-uploads/sap_third_party_documentation_consent_form_0.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “FA SAP APPEAL ___________ Satisfactory Academic Progress (SAP) Plan of Study Last Name First Name UNI ID Number Degree(s)/Major(s) Minor(s) Expected Graduation Date Instructions The Financial Aid SAP Appeal Committee requires all students to meet with their academic advisor or record analyst to determine a viable plan of study to assist the student in meeting degree requirements and SAP standards ”
  - sentence: sap_appeal ⟵ “The plan of study will be used as part of the Financial Aid SAP appeal process; it is not intended for any other use.”
### `fa4a3c4b995f88e9` University of Northern Iowa — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.uni.edu/sites/default/files/inline-uploads/sap_third_party_documentation_consent_form_0.pdf (sha256 439cc47dd670)
- issues: semantic_review_required, conflicting_sources:https://admissions.uni.edu/financial-aid/eligibility/satisfactory-academic-progress,https://admissions.uni.edu/financial-aid/sap-appeal-form,https://admissions.uni.edu/sites/default/files/inline-uploads/sap_plan_of_study_1_1.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You may upload the signed form to the online SAP Appeal Form, email the signed form to jennifer.sullivan@uni.edu, or drop off a copy of the signed form to the Office of Financial Aid & Scholarships.”
  - sentence: sap_appeal ⟵ “By checking any of the boxes below, you authorize the UNI Office of Financial Aid & Scholarships to obtain documentation you submitted to the office(s) indicated to include with your SAP Appeal.”
### `10bc4be6f0c55cd0` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 per year ⟵ “Art Scholarships | Up to $5,000 per year | Portfolio reviewVisit the UNI Scholarship Application for details”
  - eligibility_summary: Portfolio reviewVisit the UNI Scholarship Application for details ⟵ “Art Scholarships | Up to $5,000 per year | Portfolio reviewVisit the UNI Scholarship Application for details”
### `224f0345cf004242` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Iowa Resident Cost of Attendance ⟵ “Noel Scholars | Iowa Resident Cost of Attendance | New high school graduate from IowaGPA of 3.0+Full details on the Noel Scholars Website”
  - eligibility_summary: New high school graduate from IowaGPA of 3.0+Full details on the Noel Scholars Website ⟵ “Noel Scholars | Iowa Resident Cost of Attendance | New high school graduate from IowaGPA of 3.0+Full details on the Noel Scholars Website”
### `2d3ea85dbea90f4c` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per year ⟵ “Alderman Scholarship | Up to $2,000 per year | Good academic standingPlan to major in one of the CSBS degree programsAwarded to needy, worthy and appreciative students who have experienced difficulties”
  - eligibility_summary: Good academic standingPlan to major in one of the CSBS degree programsAwarded to needy, worthy and appreciative students who have experienced difficulties ⟵ “Alderman Scholarship | Up to $2,000 per year | Good academic standingPlan to major in one of the CSBS degree programsAwarded to needy, worthy and appreciative students who have experienced difficulties”
### `38c26162b22f7e0b` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per year ⟵ “Wilson College Inspire Award | Up to $1,000 per year | Plan to major in a Business programHigh school GPA of 3.75+Demonstrate high-level of financial needFirst generation or TRIO participantRenewable with 2.5+ college GPA”
  - eligibility_summary: Plan to major in a Business programHigh school GPA of 3.75+Demonstrate high-level of financial needFirst generation or TRIO participantRenewable with 2.5+ college GPA ⟵ “Wilson College Inspire Award | Up to $1,000 per year | Plan to major in a Business programHigh school GPA of 3.75+Demonstrate high-level of financial needFirst generation or TRIO participantRenewable with 2.5+ college GPA”
### `6f2821d374f729aa` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Iowa resident tuition per year ⟵ “Benjamin J. Allen TeacherEducation Scholar Awards | Iowa resident tuition per year | Plan to major in one of the COE degree programsMinimum GPA of 3.75Iowa resident”
  - eligibility_summary: Plan to major in one of the COE degree programsMinimum GPA of 3.75Iowa resident ⟵ “Benjamin J. Allen TeacherEducation Scholar Awards | Iowa resident tuition per year | Plan to major in one of the COE degree programsMinimum GPA of 3.75Iowa resident”
### `8655ec99a5e0a6f6` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per year ⟵ “COE Scholars Award | Up to $1,000 per year | Plan to major in one of the COE degree programsAcademic achievement”
  - eligibility_summary: Plan to major in one of the COE degree programsAcademic achievement ⟵ “COE Scholars Award | Up to $1,000 per year | Plan to major in one of the COE degree programsAcademic achievement”
### `cca0949c4a65f0e6` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Iowa Resident Cost of Attendance ⟵ “Wilson Student Scholars | Iowa Resident Cost of Attendance | Current senior attending a Tama County high school with preference for a student from North Tama High School.Full details on the Wilson Student Scholars Website”
  - eligibility_summary: Current senior attending a Tama County high school with preference for a student from North Tama High School.Full details on the Wilson Student Scholars Website ⟵ “Wilson Student Scholars | Iowa Resident Cost of Attendance | Current senior attending a Tama County high school with preference for a student from North Tama High School.Full details on the Wilson Student Scholars Website”
### `cfeb53ac0ef65799` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,500 per year ⟵ “Theatre Activity Scholarships | Up to $2,500 per year | “B” average or rank in upper 30% of high-school graduating classVisit the UNI Scholarship Application for details”
  - eligibility_summary: “B” average or rank in upper 30% of high-school graduating classVisit the UNI Scholarship Application for details ⟵ “Theatre Activity Scholarships | Up to $2,500 per year | “B” average or rank in upper 30% of high-school graduating classVisit the UNI Scholarship Application for details”
### `db6bb4d030e4b116` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per year ⟵ “CSBS Scholars Award | Up to $2,000 per year | Academic achievementPlan to major in one of the CSBS degree programs”
  - eligibility_summary: Academic achievementPlan to major in one of the CSBS degree programs ⟵ “CSBS Scholars Award | Up to $2,000 per year | Academic achievementPlan to major in one of the CSBS degree programs”
### `dd2b831772c565d2` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 per year ⟵ “Science Technology& Mathematics Scholarships | Up to $5,000 per year | Plan to major in one of the following: Biology, Chemistry & Biochemistry, Computer Science, Earth Science, Technology, Mathematics, Physics, Science Teaching or Environmental Science.”
  - eligibility_summary: Plan to major in one of the following: Biology, Chemistry & Biochemistry, Computer Science, Earth Science, Technology, Mathematics, Physics, Science Teaching or Environmental Science. ⟵ “Science Technology& Mathematics Scholarships | Up to $5,000 per year | Plan to major in one of the following: Biology, Chemistry & Biochemistry, Computer Science, Earth Science, Technology, Mathematics, Physics, Science Teaching or Environmental Science.”
### `fac4716e446fc5b8` University of Northern Iowa — awards 2026-27 [new] (labeled_in_source)
- source: https://admissions.uni.edu/financial-aid/types-of-aid/scholarships/scholarships-incoming-freshmen (sha256 49f020a9a8f9)
- issues: duplicate_table_versions
- checks: {"thresholds": null}
  - award_amount_text: Up to $6,000 per year ⟵ “School of Music (SOM) Scholarships | Up to $6,000 per year | Admission to the School of Music including successful completion of an auditionVisit the UNI Scholarship Application for detailsComplete the required music supplement online”
  - eligibility_summary: Admission to the School of Music including successful completion of an auditionVisit the UNI Scholarship Application for detailsComplete the required music supplement online ⟵ “School of Music (SOM) Scholarships | Up to $6,000 per year | Admission to the School of Music including successful completion of an auditionVisit the UNI Scholarship Application for detailsComplete the required music supplement online”
### `cb96e495ff0f5643` University of Northern Iowa — credit_policies 2001-02 · policy_kind=IB [new] (labeled_in_source)
- source: https://admissions.uni.edu/undergraduate/college-credit (sha256 b5e4d1e13e35)
- issues: stale_year_label:2001-02
- checks: {"distinct_exams": 33, "equivalencies": 34, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL 4]:  ⟵ “Biology HL | 4 | BIOL:2051 & BIOL:1000Z | 8 | SR”
  - equivalencies[IB-BIOLOGY-SL|SL 5]:  ⟵ “Biology SL | 5 | BIOL:1000SR | 4 | SR”
  - equivalencies[IB-BUSINESS-MANAGEMENT-HL|HL 4]:  ⟵ “Business Management HL | 4 | MGMT:1000Z & MGMT:1000Z | 6 | -”
  - equivalencies[IB-BUSINESS-MANAGEMENT-SL|SL 5]:  ⟵ “Business Management SL | 5 | MGMT:1000Z | 3 | -”
  - equivalencies[IB-CHEMISTRY-HL|HL 4]:  ⟵ “Chemistry HL | 4 | CHEM:1110 & CHEM:1000Z | 8 | SR”
  - equivalencies[IB-CHEMISTRY-SL|SL 5]:  ⟵ “Chemistry SL | 5 | CHEM:1010 | 4 | SR”
  - equivalencies[IB-ECONOMICS-HL|HL 4]:  ⟵ “Economics HL | 4 | ECON:1041 & ECON:1051 | 6 | QR”
  - equivalencies[IB-ECONOMICS-SL|SL 5]:  ⟵ “Economics SL | 5 | ECON:1000QR | 3 | QR”
  - equivalencies[IB-FRENCH-HL|HL 4-7]:  ⟵ “French B HL | 4-7 | FREN: 1001, 1002 (4) FREN: 1001, 1002, 2001 (5)FREN: 1001, 1002, 2001, 2002 (6-7) | 6-12 based on score | ”
  - equivalencies[IB-FRENCH-SL|SL 4-7]:  ⟵ “French B SL | 4-7 | FREN:1001,1002 (4-5) FREN:1001, 1002, 2001 (6-7) | 6-9 based on score | -”
  - equivalencies[IB-GEOGRAPHY-HL|HL 4]:  ⟵ “Geography HL | 4 | GEOG:1000HG & GEOG:1000Z | 6 | HG”
  - equivalencies[IB-GEOGRAPHY-SL|SL 5]:  ⟵ “Geography SL | 5 | GEOG:1000HG | 3 | HG”
  - equivalencies[IB-GERMAN-HL|HL 4-7]:  ⟵ “German B HL | 4-7 | GER: 1001, 1002 (4) GER: 1001, 1002, 2001 (5)GER: 1001, 1002, 2001, 2002 (6-7) | 6-12 based on score | -”
  - equivalencies[IB-GERMAN-SL|SL 4-7]:  ⟵ “German B SL | 4-7 | GER:1001,1002 (4-5) GER:1001, 1002, 2001 (6-7) | 6-9 based on score | -”
  - equivalencies[IB-GLOBAL-POLITICS-HL|HL 4]:  ⟵ “Global Politics HL | 4 | POL INTL:1024 & POL INTL:1000Z | 6 | HG”
  - equivalencies[IB-GLOBAL-POLITICS-SL|SL 5]:  ⟵ “Global Politics SL | 5 | POL INTL:1024 | 3 | HG”
  - equivalencies[IB-HISTORY-HL|HL 4]:  ⟵ “History HL: History Africa and Middle East | 4 | HIST:1000HG | 6 | HG”
  - equivalencies[IB-HISTORY-SL|SL 5]:  ⟵ “History SL | 5 | HIST:1000HG | 3 | HG”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|HL 4]:  ⟵ “Math: Analysis & Approaches HL | 4 | MATH:1420 & STAT:1772 | 7 | QR”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|SL 5]:  ⟵ “Math: Analysis & Approaches SL | 5 | MATH:1000QR | 3 | QR”
  - equivalencies[IB-PHILOSOPHY-HL|HL 4]:  ⟵ “Philosophy HL | 4 | PHIL:1020 & PHIL1000Z | 6 | RE”
  - equivalencies[IB-PHILOSOPHY-SL|SL 5]:  ⟵ “Philosophy SL | 5 | PHIL:1020 | 3 | RE”
  - equivalencies[IB-PHYSICS-HL|HL 4]:  ⟵ “Physics HL | 4 | PHYSICS:1511 & PHYSICS:1512 | 8 | SR”
  - equivalencies[IB-PHYSICS-SL|SL 5]:  ⟵ “Physics SL | 5 | PHYSICS:1000SR | 4 | SR”
  - equivalencies[IB-PSYCHOLOGY-HL|HL 4]:  ⟵ “Psychology HL | 4 | PSYC:1001 & PSYC:1000Z | 6 | HD”
  - … 9 more rows
### `f01149c3a477383e` University of Northern Iowa — credit_policies 2001-02 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://admissions.uni.edu/undergraduate/college-credit (sha256 b5e4d1e13e35)
- issues: stale_year_label:2001-02
- checks: {"distinct_exams": 22, "equivalencies": 29, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|63]:  ⟵ “American Government | 63 | 3 | POL AMER 1014 | HD”
  - equivalencies[CLEP-BIOLOGY|57]:  ⟵ “Biology | 57 | 4,4 | BIOL 2051/2052 | SR”
  - equivalencies[CLEP-CALCULUS|61]:  ⟵ “Calculus-Range A | 61 | 4 | MATH 1420 | QR”
  - equivalencies[CLEP-CALCULUS|71]:  ⟵ “Calculus-Range B | 71 | 4,4 | MATH 1420,1421 | QR”
  - equivalencies[CLEP-CHEMISTRY|63]:  ⟵ “Chemistry | 63 | 4,4 | CHEM 1110/1120 | SR”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|60]:  ⟵ “College Algebra | 60 | 3 | MATH 1120 | None”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|59]:  ⟵ “College Composition | 59 | 3 | ENGLISH 1005 | WC”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|74]:  ⟵ “College Mathematics | 74 | 3 | MATH 1100 | QR”
  - equivalencies[CLEP-FRENCH-LANGUAGE|55]:  ⟵ “French Language-Range 1 | 55 | 6 | FREN 1001/1002 | None”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “French Language-Range 2 | 62 | 9 | FREN 1001/1002/2001 | None”
  - equivalencies[CLEP-FRENCH-LANGUAGE|66]:  ⟵ “French Language-Range 3 | 66 | 12 | FREN 1001/1002/2001/2002 | None”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language-Range 1 | 50 | 6 | GER 1001/1002 | None”
  - equivalencies[CLEP-GERMAN-LANGUAGE|56]:  ⟵ “German Language-Range 2 | 56 | 9 | GER 1001/1002/2001 | None”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “German Language Range 3 | 63 | 12 | GER 1001/1002/2001/2002 | None”
  - equivalencies[CLEP-HUMANITIES|56]:  ⟵ “Humanities | 56 | 3,3 | UNIV 1000HE / ENGLISH 1120 | HE”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|59]:  ⟵ “Introductory Psychology | 59 | 3 | PSYCH 1001 | HD”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|59]:  ⟵ “Introductory Sociology | 59 | 3 | SOC 1000 | HD”
  - equivalencies[CLEP-NATURAL-SCIENCES|62]:  ⟵ “Natural Sciences | 62 | 3,3 | BIOL 1000A / SCI ED 1000A | SR”
  - equivalencies[CLEP-PRECALCULUS|61]:  ⟵ “Precalculus | 61 | 4 | MATH 1140 | None”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|62]:  ⟵ “Principles of Macroeconomics | 62 | 3 | ECON 1041 | QR”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|56]:  ⟵ “Principles of Management | 56 | 3 | MGMT 3153 | None”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|65]:  ⟵ “Principles of Marketing | 65 | 3 | MKTG 2110 | None”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|64]:  ⟵ “Principles of Microeconomics | 64 | 3 | ECON 1051 | QR”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|55]:  ⟵ “Social Sciences and History | 55 | 3 | SOCSCI1000Z* | None”
  - equivalencies[CLEP-SPANISH-LANGUAGE|55]:  ⟵ “Spanish Language-Range 1 | 55 | 6 | SPAN 1001/1002 | None”
  - … 4 more rows
### `f110593b1bb51ec9` University of Northern Iowa — credit_policies 2001-02 · policy_kind=AP [new] (labeled_in_source)
- source: https://admissions.uni.edu/undergraduate/college-credit (sha256 b5e4d1e13e35)
- issues: stale_year_label:2001-02
- checks: {"distinct_exams": 2, "equivalencies": 3, "rows_without_score": 0}
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research | 3 | 3 hours | ENGLISH1000Z | - | ”
  - equivalencies[AP-RESEARCH|4, 5]:  ⟵ “AP Research | 4, 5 | 6 hours | ENGLISH1005COMM1000 | WC, OC | ”
  - equivalencies[AP-SEMINAR|3, 4, 5]:  ⟵ “AP Seminar | 3, 4, 5 | 3 hours | ENGLISH1000Z | - | ”
### `0dd559ecff68af44` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance (sha256 0bc8a5330a36)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `1037c18a5f161ba6` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances (sha256 8b7ee2ff723d)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `129024a1e479ae0b` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions (sha256 6f90c93efb09)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Satisfactory Academic Progress-SAP Special or Unusual Circumstances Financial Aid administrators may be able to make adjustments in event of job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `1d0ef2ff6db44e90` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments (sha256 32fc2416821d)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `1f7805646862bc36` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification (sha256 2b352ed9d719)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `278df3affe24c8b1` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information (sha256 ae911642ec3d)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Satisfactory Academic Progress-SAP Special or Unusual Circumstances Financial Aid administrators may be able to make adjustments in event of job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `3f3074e8d260e8fc` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance (sha256 32e780156123)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `4e47650db98d1638` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap (sha256 be8156ee5efc)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `5383e40a8d1ea464` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/ (sha256 514e56120768)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `5e1f7d636d46ead2` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment (sha256 c4625b3a2d12)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Satisfactory Academic Progress-SAP Special or Unusual Circumstances Financial Aid administrators may be able to make adjustments in event of job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `6556ed8b7090e97a` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions (sha256 ce1432a851b6)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Satisfactory Academic Progress-SAP Special or Unusual Circumstances Financial Aid administrators may be able to make adjustments in event of job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `7517e7e9af1d7528` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality (sha256 a6dd5a98b663)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `7c2441b323cdc811` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status (sha256 4b160b947717)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `82f4681d21fa915f` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers (sha256 ae76ac184063)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special or Unusual Circumstances The Upper Iowa University Financial Aid Office understands that families can experience hardships or changes which may not be reflected on the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Federal regulations allow financial aid administrators to make adjustments for certain types of situations such as job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `8bc0ad772a85ef6e` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/ (sha256 311127f12ac7)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Satisfactory Academic Progress-SAP Special or Unusual Circumstances Financial Aid administrators may be able to make adjustments in event of job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `bda7501d90fc7b04` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility (sha256 4f3793ca396a)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Satisfactory Academic Progress-SAP Special or Unusual Circumstances Financial Aid administrators may be able to make adjustments in event of job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `e16e28970e55f5e4` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/federal-satisfactory-academic-progress-sap/?ecopen=what-are-my-options-if-i-want-to-continue-taking-classes-but-am-suspended (sha256 5c1449f9acec)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Policy Documents Access UIU’s live Satisfactory Academic Progress (SAP) policy and download supplemental documents like the Satisfactory Academic Progress Appeal Form in our policy catalog at Content Loading....”
  - sentence: sap_appeal ⟵ “Appeal – A process by which a student who is not meeting SAP standards petitions the school’s SAP Appeals Committee for reconsideration of their eligibility for financial aid funds (Title IV).”
  - sentence: sap_appeal ⟵ “Financial Aid Probation – A status a school assigns to a student who is failing to make satisfactory academic progress and who successfully appeals.”
### `ea249f9c55833eb0` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/ (sha256 ca2a66e98b3b)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Satisfactory Academic Progress-SAP Special or Unusual Circumstances Financial Aid administrators may be able to make adjustments in event of job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `fcbffb9e4afc8c67` Upper Iowa University — appeals 2026-27 [new] (source_unlabeled)
- source: https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=ferpa-granting-permissions (sha256 af33d1cbfebd)
- issues: semantic_review_required, conflicting_sources:https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=book-voucher-eligibility,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=file-completion-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=make-a-payment,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=study-abroad-information,https://uiu.edu/admissions/tuition-and-costs/financial-aid/?ecopen=verification-process-questions,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=annual-disclosure-notification,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=book-vouchers,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=confidentiality,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=cost-of-attendance,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=credit-balance-refundsoverpayments,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=enrollment-status,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=satisfactory-academic-progress-sap,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=special-or-unusual-circumstances,https://uiu.edu/admissions/tuition-and-costs/financial-aid/disclosure-statement/?ecopen=state-scholarships-grants-and-other-assistance
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Federal Satisfactory Academic Progress-SAP Special or Unusual Circumstances Financial Aid administrators may be able to make adjustments in event of job loss, unexpected life events (death, divorce/separation) or other unusual circumstances that are not readily apparent on the FAFSA.”
### `dc3930c574e398c2` Wartburg College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.wartburg.edu/financial-aid/crunch-your-numbers/ (sha256 66da79f298a0)
- issues: ambiguous_year_labels
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition:: 26975 ⟵ “Tuition: | $26,975”
  - column:Fees:: 1350 ⟵ “Fees: | $1,350”
  - column:Housing (approx): 7150 ⟵ “Housing (approx) | $7,150”
  - column:Food (approx): 5880 ⟵ “Food (approx) | $5,880”
  - column:TOTAL: 41355 ⟵ “TOTAL | $41,355”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 2; pages by category: merit_scholarships 1, statewide_articulation 1

## Blocked by the site (every request refused; needs the browser fallback)

- Iowa Lakes Community College (`ipeds-153533`)
- Northwest Iowa Community College (`ipeds-154129`)

## Leads: official pages found with no extracted record

- Allen College: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements, aid_appeals
- Briar Cliff University: cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation, degree_requirements
- Buena Vista University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Central College: tuition_fees, cost_of_attendance, ib_credit, dual_enrollment, degree_requirements, aid_appeals
- Clarke University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation
- Coe College: admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Cornell College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Des Moines Area Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Divine Word College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Dordt University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Drake University: tuition_fees, cost_of_attendance, admissions_tests, clep_credit, dual_enrollment, statewide_articulation, degree_requirements
- Eastern Iowa Community College District: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Ellsworth Community College: cost_of_attendance, admissions_tests, merit_scholarships
- Emmaus Bible College: tuition_fees, admissions_tests, merit_scholarships, ap_credit, clep_credit, statewide_articulation, degree_requirements
- Faith Baptist Bible College and Theological Seminary: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, degree_requirements
- Graceland University-Lamoni: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Grand View University: cost_of_attendance, admissions_tests, transfer_credit
- Grinnell College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, transfer_credit, residency
- Hawkeye Community College: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, degree_requirements
- Indian Hills Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, residency
- Iowa Central Community College: cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Iowa State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Iowa Western Community College: admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- Kirkwood Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Loras College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
- Luther College: cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Maharishi International University: cost_of_attendance, admissions_tests, merit_scholarships, residency, degree_requirements, aid_appeals
- Marshalltown Community College: cost_of_attendance, admissions_tests, merit_scholarships
- Mercy College of Health Sciences: transfer_credit
- Morningside University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- Mount Mercy University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency
- North Iowa Area Community College: admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Northeast Iowa Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Northwestern College: admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, degree_requirements
- Saint Ambrose University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, ib_credit, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Simpson College: tuition_fees, cost_of_attendance, admissions_tests, transfer_credit, degree_requirements
- Southeastern Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Southwestern Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- St Luke's College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- University of Dubuque: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency
- University of Iowa: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, statewide_articulation, degree_requirements
- University of Northern Iowa: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, residency, degree_requirements
- Upper Iowa University: cost_of_attendance, admissions_tests, transfer_credit, statewide_articulation
- Wartburg College: cost_of_attendance, admissions_tests, ap_credit, transfer_credit, aid_appeals
- Western Iowa Tech Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency, degree_requirements
- William Penn University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships
