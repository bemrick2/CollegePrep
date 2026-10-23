# Review queue — IA (2026-27)

Pages fetched: 180; failures: 8. Candidates: 12 (1 without issues, 11 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 5 | 0 | 0 | 1 | 1 | 0 | 42 |
| cost_of_attendance | 2 | 0 | 0 | 0 | 2 | 0 | 45 |
| admissions_tests | 0 | 0 | 0 | 0 | 2 | 0 | 47 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 2 | 47 |
| merit_scholarships | 4 | 5 | 0 | 0 | 2 | 0 | 38 |
| ap_credit | 1 | 4 | 0 | 0 | 1 | 0 | 43 |
| clep_credit | 0 | 3 | 0 | 1 | 1 | 0 | 44 |
| ib_credit | 0 | 0 | 0 | 0 | 0 | 2 | 47 |
| dual_enrollment | 0 | 0 | 0 | 0 | 0 | 2 | 47 |
| transfer_credit | 1 | 2 | 0 | 0 | 2 | 0 | 44 |
| statewide_articulation | 0 | 0 | 0 | 0 | 2 | 0 | 47 |
| residency | 0 | 0 | 0 | 0 | 1 | 1 | 47 |
| degree_requirements | 2 | 0 | 0 | 0 | 1 | 0 | 46 |
| aid_appeals | 0 | 0 | 0 | 2 | 0 | 0 | 47 |

## Ready for review (1)

### `8d4ddd31deca714c` Iowa State University — credit_policies 2026-27 · policy_kind=AP [same] (source_unlabeled)
- source: https://www.iastate.edu/admission-and-aid/admissions/first-year-students/credit-by-exam (sha256 5a671fef02ec)
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

## Exceptions (11)

### `8cbd291cd6f48a99` Iowa State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.iastate.edu/getting-started/cost/ (sha256 539f0db891ca)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Cost of Attendance Adjustment You may be eligible to complete a cost of attendance adjustment form if your education-related expenses exceed the amount of financial aid included in your cost of attendance.”
  - sentence: budget_increase ⟵ “Veterinary Medicine Cost of Attendance Adjustment You make be eligible to adjust your cost of attendance if education-related expenses exceed the costs already built into your cost of attendance.”
### `c3b4378d1da5bb78` Iowa State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.iastate.edu/managing-your-aid/financial-aid-appeals/ (sha256 15a2e65924bb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Conditions Independent Appeals The Office of Student Financial Aid can use professional judgement to override a student’s dependency status from dependent to independent in some situations.”
### `4bb9cd4f46f2dc46` Iowa State University — credit_policies 2026-27 · policy_kind=CLEP [new] (source_unlabeled)
- source: https://www.iastate.edu/admission-and-aid/admissions/first-year-students/credit-by-exam (sha256 5a671fef02ec)
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
### `2957a6eb2103124c` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress (sha256 3c8bf6455c25)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap,https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 18}
  - sentence: sap_appeal ⟵ “If you are not meeting SAP standards, submitting a SAP appeal is strongly encouraged.”
  - sentence: sap_appeal ⟵ “The SAP appeal process exists to support students who experience academic challenges, and historically, nearly all first-time SAP appeals submitted with a complete statement and plan are approved.”
  - sentence: sap_appeal ⟵ “Students who lose financial aid eligibility due to not meeting SAP requirements may: submit a SAP Appeal or earn the necessary GPA or semester hours to meet the minimum requirements while not receiving federal financial aid Regaining SAP Eligibility Students who are not meeting SAP requirements for GPA or pace may regain eligibility on their own without submitting an appeal by attending and achiev”
  - sentence: sap_appeal ⟵ “The same process applies to students who have submitted a SAP appeal that has been denied; they can attend without the use of federal financial aid.”
  - sentence: sap_appeal ⟵ “Students who have been denied a SAP appeal can re-appeal after one semester without federal aid.”
  - sentence: sap_appeal ⟵ “SAP for Undergraduates SAP for Graduates Your SAP Status Explained | SAP Status | Next Steps | Eligible | You are meeting SAP standards and don't need to do anything. | GPA - Not Eligible | You can either: Submit a SAP Appeal by the deadline each semester as noted below.”
### `6bc739bfe9d42c46` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap (sha256 60f6ca88d38d)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy,https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “If you exceed the hours attempted (all hours taken including W, F, U, N, O, and I grades) listed below, a SAP appeal will be required to receive financial aid.”
  - sentence: sap_appeal ⟵ “College of Liberal Arts & Sciences = 180 hours Tippie College of Business = 180 hours College of Education = 180 hours University College = 180 hours College of Engineering = 192 hours College of Nursing = 192 hours College of Public Health = 180 hours College of Medicine = 180 hours If you exceed your duration of eligibility, you must file the SAP Appeal Form in MyUI to be considered for extended”
### `9d1c0e2c0fb3a232` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/cost/appealing-costs (sha256 9f7ef883bf4a)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “All requests are reviewed using Professional Judgment and must include complete and accurate documentation.”
  - sentence: professional_judgment ⟵ “Decisions are made at the discretion of the Office of Student Financial Aid based on federal Professional Judgement guidelines.”
### `d7a783fd91f069ec` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress (sha256 ff6ee951e6c4)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap,https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 18}
  - sentence: sap_appeal ⟵ “If you are not meeting SAP standards, submitting a SAP appeal is strongly encouraged.”
  - sentence: sap_appeal ⟵ “The SAP appeal process exists to support students who experience academic challenges, and historically, nearly all first-time SAP appeals submitted with a complete statement and plan are approved.”
  - sentence: sap_appeal ⟵ “Students who lose financial aid eligibility due to not meeting SAP requirements may: submit a SAP Appeal or earn the necessary GPA or semester hours to meet the minimum requirements while not receiving federal financial aid Regaining SAP Eligibility Students who are not meeting SAP requirements for GPA or pace may regain eligibility on their own without submitting an appeal by attending and achiev”
  - sentence: sap_appeal ⟵ “The same process applies to students who have submitted a SAP appeal that has been denied; they can attend without the use of federal financial aid.”
  - sentence: sap_appeal ⟵ “Students who have been denied a SAP appeal can re-appeal after one semester without federal aid.”
  - sentence: sap_appeal ⟵ “SAP for Undergraduates SAP for Graduates Your SAP Status Explained | SAP Status | Next Steps | Eligible | You are meeting SAP standards and don't need to do anything. | GPA - Not Eligible | You can either: Submit a SAP Appeal by the deadline each semester as noted below.”
### `dccf788c3869f2c2` University of Iowa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy (sha256 92356a5a07a0)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap,https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf
- checks: {"negative_sentences": 0, "sentences": 13}
  - sentence: sap_appeal ⟵ “Students who do not meet the GPA requirement for SAP after the spring semester are no longer eligible for federal financial aid and must complete a SAP appeal to receive federal financial aid for the subsequent semester.”
  - sentence: sap_appeal ⟵ “If you exceed the hours attempted (all hours taken including W, F, U, N, O, and I grades) listed below, a SAP appeal will be required to receive financial aid.”
  - sentence: sap_appeal ⟵ “College of Liberal Arts & Sciences = 180 hours Tippie College of Business = 180 hours College of Education = 180 hours University College = 180 hours College of Engineering = 192 hours College of Nursing = 192 hours College of Public Health = 180 hours College of Medicine = 180 hours If you exceed your duration of eligibility, you must file the SAP Appeal Form in MyUI to be considered for extended”
  - sentence: sap_appeal ⟵ “If you exceed the number of attempted credit hours (all UI graduate courses taken including W, F, U, N, O, and I grades) listed below then you will have reached the duration limit for the program, and you must file a SAP Appeal to regain financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Students with an approved SAP appeal are placed on financial aid probation for one semester.”
  - sentence: sap_appeal ⟵ “If a student does not complete these requirements after one semester on financial aid probation, they are no longer eligible for financial aid for the next semester and must submit an additional SAP appeal.”
### `e6178214d5298078` University of Iowa — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.uiowa.edu/sites/financialaid.uiowa.edu/files/2025-12/MED_Satisfactory_Academic_Progress_Policy.pdf (sha256 5f35b03d2c68)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/satisfactory-academic-progress-policy,https://financialaid.uiowa.edu/eligibility/satisfactory-academic-progress/undergraduate-sap
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Incompletes An Incomplete will count as not passing all requisite coursework and therefore would result in a student not meeting SAP standards and an appeal would be needed.”
  - sentence: sap_appeal ⟵ “Withdrawals A withdrawn course will count as not passing all requisite coursework and therefore would result in a student not meeting SAP standards and an appeal would be needed.”
### `05619e6cbcce6410` University of Iowa — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://admissions.uiowa.edu/finances/estimated-costs-attendance (sha256 409df1baed73)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 7}
  - on_campus:Tuition & fees*: 11971 ⟵ “Tuition & fees* | $11,971 | $34,247”
  - on_campus:Housing & food**: 14022 ⟵ “Housing & food** | $14,022 | $14,022”
  - on_campus:Total billed expenses: 25993 ⟵ “Total billed expenses | $25,993 | $48,269”
  - on_campus:Books & supplies: 950 ⟵ “Books & supplies | $950 | $950”
  - on_campus:Personal expenses***: 3648 ⟵ “Personal expenses*** | $3,648 | $3,648”
  - on_campus:Transportation: 1254 ⟵ “Transportation | $1,254 | $1,254”
  - on_campus:Total estimated expenses: 5852 ⟵ “Total estimated expenses | $5,852 | $5,852”
### `0608e2d342122516` University of Iowa — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://admissions.uiowa.edu/finances/estimated-costs-attendance (sha256 409df1baed73)
- issues: multiple_total_rows
- checks: {"columns": 1, "rows": 7}
  - on_campus:Tuition & fees*: 34247 ⟵ “Tuition & fees* | $11,971 | $34,247”
  - on_campus:Housing & food**: 14022 ⟵ “Housing & food** | $14,022 | $14,022”
  - on_campus:Total billed expenses: 48269 ⟵ “Total billed expenses | $25,993 | $48,269”
  - on_campus:Books & supplies: 950 ⟵ “Books & supplies | $950 | $950”
  - on_campus:Personal expenses***: 3648 ⟵ “Personal expenses*** | $3,648 | $3,648”
  - on_campus:Transportation: 1254 ⟵ “Transportation | $1,254 | $1,254”
  - on_campus:Total estimated expenses: 5852 ⟵ “Total estimated expenses | $5,852 | $5,852”

## Re-verification of existing records (111)

- source_not_fetched: data/institutions/briarcliff/awards/2026-27.json ["awards", "ipeds-152992", null, "2026-27", {"award_name": "Academic Scholarships"}]
- source_not_fetched: data/institutions/briarcliff/costs/2027-28.json ["costs", "ipeds-152992", null, "2027-28", {"residency": "not_applicable"}]
- source_not_fetched: data/institutions/clarke/transfer_policies/2026-27.json ["transfer_policies", "ipeds-153126", null, "2026-27", {}]
- source_not_fetched: data/institutions/dordt/credit_policies/2026-27.json ["credit_policies", "ipeds-153250", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "Presidential Scholarship"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "National Alumni Scholarship"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "Drake-Sponsored National Merit Scholarship"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "Legacy Award"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "The Bulldog Promise"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "Bahamas Scholarship"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "Hebei Province Scholarship"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "Bright College Pathway"}]
- source_not_fetched: data/institutions/drake/awards/2026-27.json ["awards", "ipeds-153269", null, "2026-27", {"award_name": "Community of Digital Excellence (CODE) Scholarship"}]
- source_not_fetched: data/institutions/drake/transfer_policies/2026-27.json ["transfer_policies", "ipeds-153269", null, "2026-27", {}]
- source_not_fetched: data/institutions/eicc/credit_policies/2026-27.json ["credit_policies", "ipeds-153311", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/eicc/credit_policies/2026-27.json ["credit_policies", "ipeds-153311", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/grandview/transfer_policies/2026-27.json ["transfer_policies", "ipeds-153375", null, "2026-27", {}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Student Activities"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Hawkeye Pride Organization"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Denver Cyclone"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Tripoli Community School Alumni"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Cedar Valley Civitan"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Jimmy Robinson"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Travis Wittmayer Scholarship for the Profoundly Deaf"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "American Legion of Iowa"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "David Crowe Memorial Veteran Scholarship"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Richard Brian Gienau Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Bob Kimm Judging"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Dan Huck Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Farm Credit Services of America Agriculture"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "GROWMARK Agriculture"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Horticulture"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Land O'Lakes"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Lloyd R. Dilley & Donald L. Dilley Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Malcolm McGregor"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Marie & Raymond Howsare"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Natural Resources Outstanding Student"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "PAS Leadership"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Rocky Fratzke Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Todd Kinley Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Virgil Christensen"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "William & Edna Fennemann"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Don Collinson"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "ETC: Art & Literary Magazine"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Ike Leighty"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Larry Williams Scholarship, Sons of Amvets Post 49 (Hospitality Management)"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "WITS"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Woody Stingley (Accounting)"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Black Hawk County Law Enforcement"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Buckles"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Jerry & JoAnn Jensen Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Jerry Greenlee Sr. BCPOA Endowed"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Mike Tripolino Criminal Justice"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Rick Harned Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Robert M. Flynn Memorial Scholarship"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Tim Petersen Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Tommy Burns (Waterloo Schools Alumni)"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "William F. Mullikin Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Early Childhood Education"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Steve & Donita Dust Scholarship"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Aspro"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Brian Harrington, Sons of Amvets Post 49"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Electronic Engineering Technology"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Express Pro's"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "FBG Service Corp."}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "James & Caroline Martin"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Kenneth Bienfang & Harold Bienfang"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Mike Turner Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Paul J. Frazier"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Robert D. Gunderson"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Steve & Donita Dust"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Virginia Winter"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Walther Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Woody Stingley (CNC)"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "World Class Industries"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Jim & Cecelia Mudd"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Woody Stingley (Network Administration & Engineering)"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Andrew & Marlys Puhl Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Darlene Culpepper Nursing"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Dental Community Scholarship (Dental Assisting)"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Dental Community Scholarship (Dr. Richard Haw Dental Hygiene)"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Friendship Village Retirement Center"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Harlan & Betty Van Gerpen Health Science Scholarship"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Ida Fleming Nursing"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Jean Dunbar Nursing Scholarship"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Mary Kathleen Flynn Memorial"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Nursing Faculty in Memory of T.P. Cook & V. Smith"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Pauline Barrett Nursing"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Terri Cook Family Nursing"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "V. Miller / Miller Medical"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Associated General Contractors of Iowa"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Bruce Haugland Power Technology"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Future Collision & Refinishing Technicians"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Nelson & Leighty\u2013Engineered Products Co. Scholarship Fund"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Mark & June Birdnow"}]
- source_not_fetched: data/institutions/hawkeyecollege/awards/2026-27.json ["awards", "ipeds-153445", null, "2026-27", {"award_name": "Marvin and Lora Kramer"}]
- all_values_found_year_not_labeled: data/institutions/iastate/credit_policies/2026-27.json ["credit_policies", "ipeds-153603", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/iwcc/credit_policies/2026-27.json ["credit_policies", "ipeds-153630", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/luther/awards/2026-27.json ["awards", "ipeds-153834", null, "2026-27", {"award_name": "Founders"}]
- source_not_fetched: data/institutions/luther/awards/2026-27.json ["awards", "ipeds-153834", null, "2026-27", {"award_name": "President's"}]
- source_not_fetched: data/institutions/luther/awards/2026-27.json ["awards", "ipeds-153834", null, "2026-27", {"award_name": "Dean"}]
- source_not_fetched: data/institutions/luther/awards/2026-27.json ["awards", "ipeds-153834", null, "2026-27", {"award_name": "Martin Luther"}]
- source_not_fetched: data/institutions/luther/awards/2026-27.json ["awards", "ipeds-153834", null, "2026-27", {"award_name": "Achievement"}]
- source_not_fetched: data/institutions/nwciowa/credit_policies/2026-27.json ["credit_policies", "ipeds-154101", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/nwciowa/credit_policies/2026-27.json ["credit_policies", "ipeds-154101", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/nwciowa/transfer_policies/2026-27.json ["transfer_policies", "ipeds-154101", null, "2026-27", {}]
- source_not_fetched: data/institutions/dbq/transfer_policies/2026-27.json ["transfer_policies", "ipeds-153278", null, "2026-27", {}]
- source_not_fetched: data/institutions/uiu/awards/2026-27.json ["awards", "ipeds-154493", null, "2026-27", {"award_name": "Trustee Scholarship"}]
- source_not_fetched: data/institutions/uiu/awards/2026-27.json ["awards", "ipeds-154493", null, "2026-27", {"award_name": "Achievement Scholarship"}]
- source_not_fetched: data/institutions/uiu/awards/2026-27.json ["awards", "ipeds-154493", null, "2026-27", {"award_name": "Dean\u2019s Scholarship"}]
- source_not_fetched: data/institutions/uiu/awards/2026-27.json ["awards", "ipeds-154493", null, "2026-27", {"award_name": "Presidential Scholarship"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Iowa State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- University of Iowa: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, statewide_articulation, degree_requirements
