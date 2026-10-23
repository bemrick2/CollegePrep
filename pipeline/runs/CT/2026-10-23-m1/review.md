# Review queue — CT (2026-27)

Pages fetched: 90; failures: 0. Candidates: 10 (0 without issues, 10 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 5 | 0 | 0 | 1 | 0 | 0 | 21 |
| cost_of_attendance | 1 | 0 | 0 | 1 | 0 | 0 | 25 |
| admissions_tests | 0 | 0 | 0 | 0 | 1 | 0 | 26 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 1 | 26 |
| merit_scholarships | 0 | 0 | 0 | 0 | 1 | 0 | 26 |
| ap_credit | 0 | 2 | 0 | 1 | 0 | 0 | 24 |
| clep_credit | 0 | 2 | 0 | 0 | 0 | 1 | 24 |
| ib_credit | 0 | 2 | 0 | 1 | 0 | 0 | 24 |
| dual_enrollment | 0 | 1 | 0 | 0 | 1 | 0 | 25 |
| transfer_credit | 1 | 4 | 0 | 0 | 1 | 0 | 21 |
| statewide_articulation | 0 | 0 | 0 | 0 | 1 | 0 | 26 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 26 |
| degree_requirements | 1 | 0 | 0 | 0 | 1 | 0 | 25 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 0 | 26 |

## Ready for review (0)


## Exceptions (10)

### `1bd7db48e1ba98b3` University of Connecticut — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.uconn.edu/sap/ (sha256 098a5eed9893)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://financialaid.uconn.edu/2025/08/25/summer-2025-financial-aid-sap-review/,https://financialaid.uconn.edu/2025/12/03/fall-sap-review/,https://financialaid.uconn.edu/2026/04/30/annual-sap-evaluation/,https://financialaid.uconn.edu/2026/08/27/summer-sap-evaluation/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Probation A student for whom a Satisfactory Academic Progress Appeal is approved will be granted a period of Financial Aid probation during which they will be placed on a Financial Aid Eligibility Plan.”
  - sentence: sap_appeal ⟵ “To appeal, students must submit all of the following: Completed SAP Appeal Form on the Forms Portal Detailed reason for not meeting SAP A plan for academic success Any required supporting documentation as defined on the SAP Appeal Form Readmitted Students & SAP If a student is readmitted to the University and was previously cited for SAP or received a SAP communication from our office, they are re”
### `79ecac2fcb72c7ac` University of Connecticut — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uconn.edu/2025/12/03/fall-sap-review/ (sha256 1c327e5eec0e)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://financialaid.uconn.edu/2025/08/25/summer-2025-financial-aid-sap-review/,https://financialaid.uconn.edu/2026/04/30/annual-sap-evaluation/,https://financialaid.uconn.edu/2026/08/27/summer-sap-evaluation/,https://financialaid.uconn.edu/sap/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “The Financial Aid Eligibility Plan status applies to students whose SAP appeal was approved in 2025.”
  - sentence: sap_appeal ⟵ “Students who do not meet the SAP standards will have the option to submit a SAP Appeal.”
### `c63831dfd02c22e7` University of Connecticut — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uconn.edu/2026/08/27/summer-sap-evaluation/ (sha256 79a46ed0e1b9)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://financialaid.uconn.edu/2025/08/25/summer-2025-financial-aid-sap-review/,https://financialaid.uconn.edu/2025/12/03/fall-sap-review/,https://financialaid.uconn.edu/2026/04/30/annual-sap-evaluation/,https://financialaid.uconn.edu/sap/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students who do not meet the SAP standards will have the option to submit a SAP Appeal.”
### `fa822860770631fc` University of Connecticut — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uconn.edu/2026/04/30/annual-sap-evaluation/ (sha256 d5301ad6ade9)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://financialaid.uconn.edu/2025/08/25/summer-2025-financial-aid-sap-review/,https://financialaid.uconn.edu/2025/12/03/fall-sap-review/,https://financialaid.uconn.edu/2026/08/27/summer-sap-evaluation/,https://financialaid.uconn.edu/sap/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students who do not meet the SAP standards will have the option to submit a SAP Appeal.”
### `fbeb724f72227fe0` University of Connecticut — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uconn.edu/2025/08/25/summer-2025-financial-aid-sap-review/ (sha256 2f8633b8f008)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://financialaid.uconn.edu/2025/12/03/fall-sap-review/,https://financialaid.uconn.edu/2026/04/30/annual-sap-evaluation/,https://financialaid.uconn.edu/2026/08/27/summer-sap-evaluation/,https://financialaid.uconn.edu/sap/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students who do not meet the SAP standards will have the option to submit a SAP Appeal.”
### `a8cce7df7755ddf7` University of Connecticut — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://financialaid.uconn.edu/cost/ (sha256 747e297dc5b4)
- issues: residency_unknown, shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - on_campus:Tuition: 26028 ⟵ “Tuition | 17,010 | 39,678 | 26,028”
  - on_campus:University and Student Fees: 4564 ⟵ “University and Student Fees | 4,564 | 4,564 | 4,564”
  - on_campus:On-Campus Housing Estimate: 10186 ⟵ “On-Campus Housing Estimate | 10,186 | 10,186 | 10,186”
  - on_campus:On-Campus Food Estimate: 6896 ⟵ “On-Campus Food Estimate | 6,896 | 6,896 | 6,896”
  - on_campus:Books, Course Materials, Supplies & Equipment: 1020 ⟵ “Books, Course Materials, Supplies & Equipment | 1,020 | 1,020 | 1,020”
  - on_campus:Transportation: 2704 ⟵ “Transportation | 2,494 | 2,704 | 2,704”
  - on_campus:Miscellaneous Personal Expenses: 1968 ⟵ “Miscellaneous Personal Expenses | 1,968 | 1,968 | 1,968”
  - on_campus:Loan Fees: 92 ⟵ “Loan Fees | 92 | 92 | 92”
  - on_campus:Subtotal Indirect Costs: 5784 ⟵ “Subtotal Indirect Costs | 5,574 | 5,784 | 5,784”
  - on_campus:Estimated Total Expenses: 53458 ⟵ “Estimated Total Expenses | 44,230 | 67,108 | 53,458”
  - on_campus:Subtotal Direct Costs: 47674 ⟵ “Subtotal Direct Costs | 38,656 | 61,324 | 47,674”
### `d2bcfe9bdfbb3379` University of Connecticut — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.uconn.edu/cost/ (sha256 747e297dc5b4)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - on_campus:Tuition: 39678 ⟵ “Tuition | 17,010 | 39,678 | 26,028”
  - on_campus:University and Student Fees: 4564 ⟵ “University and Student Fees | 4,564 | 4,564 | 4,564”
  - on_campus:On-Campus Housing Estimate: 10186 ⟵ “On-Campus Housing Estimate | 10,186 | 10,186 | 10,186”
  - on_campus:On-Campus Food Estimate: 6896 ⟵ “On-Campus Food Estimate | 6,896 | 6,896 | 6,896”
  - on_campus:Books, Course Materials, Supplies & Equipment: 1020 ⟵ “Books, Course Materials, Supplies & Equipment | 1,020 | 1,020 | 1,020”
  - on_campus:Transportation: 2704 ⟵ “Transportation | 2,494 | 2,704 | 2,704”
  - on_campus:Miscellaneous Personal Expenses: 1968 ⟵ “Miscellaneous Personal Expenses | 1,968 | 1,968 | 1,968”
  - on_campus:Loan Fees: 92 ⟵ “Loan Fees | 92 | 92 | 92”
  - on_campus:Subtotal Indirect Costs: 5784 ⟵ “Subtotal Indirect Costs | 5,574 | 5,784 | 5,784”
  - on_campus:Estimated Total Expenses: 67108 ⟵ “Estimated Total Expenses | 44,230 | 67,108 | 53,458”
  - on_campus:Subtotal Direct Costs: 61324 ⟵ “Subtotal Direct Costs | 38,656 | 61,324 | 47,674”
### `dca157e4469d7fa2` University of Connecticut — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.uconn.edu/cost/ (sha256 747e297dc5b4)
- issues: shared_site_attribution_review
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - on_campus:Tuition: 17010 ⟵ “Tuition | 17,010 | 39,678 | 26,028”
  - on_campus:University and Student Fees: 4564 ⟵ “University and Student Fees | 4,564 | 4,564 | 4,564”
  - on_campus:On-Campus Housing Estimate: 10186 ⟵ “On-Campus Housing Estimate | 10,186 | 10,186 | 10,186”
  - on_campus:On-Campus Food Estimate: 6896 ⟵ “On-Campus Food Estimate | 6,896 | 6,896 | 6,896”
  - on_campus:Books, Course Materials, Supplies & Equipment: 1020 ⟵ “Books, Course Materials, Supplies & Equipment | 1,020 | 1,020 | 1,020”
  - on_campus:Transportation: 2494 ⟵ “Transportation | 2,494 | 2,704 | 2,704”
  - on_campus:Miscellaneous Personal Expenses: 1968 ⟵ “Miscellaneous Personal Expenses | 1,968 | 1,968 | 1,968”
  - on_campus:Loan Fees: 92 ⟵ “Loan Fees | 92 | 92 | 92”
  - on_campus:Subtotal Indirect Costs: 5574 ⟵ “Subtotal Indirect Costs | 5,574 | 5,784 | 5,784”
  - on_campus:Estimated Total Expenses: 44230 ⟵ “Estimated Total Expenses | 44,230 | 67,108 | 53,458”
  - on_campus:Subtotal Direct Costs: 38656 ⟵ “Subtotal Direct Costs | 38,656 | 61,324 | 47,674”
### `327bd1a90ef34980` University of Connecticut — credit_policies 2025-26 · policy_kind=IB [new] (labeled_in_source)
- source: https://admissions.uconn.edu/apply/transfer/transfer-credit/ap-ib-a-level-credit/ (sha256 46dc70e318bf)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"distinct_exams": 34, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY-HL|HL 5, 6, 7]:  ⟵ “Biology HL | 5, 6, 7 | BIOL 1107 & BIOL 1108 | 8”
  - equivalencies[IB-BIOLOGY-SL|SL 5, 6, 7]:  ⟵ “Biology SL | 5, 6, 7 | BIOL 91500 | 4”
  - equivalencies[IB-CHEMISTRY-HL|HL 5, 6, 7]:  ⟵ “Chemistry HL | 5, 6, 7 | CHEM 1127Q and 1128Q | 8”
  - equivalencies[IB-CHEMISTRY-SL|SL 5, 6, 7]:  ⟵ “Chemistry SL | 5, 6, 7 | CHEM 91500 | 4”
  - equivalencies[IB-ECONOMICS-HL|HL 6, 7]:  ⟵ “Economics HL | 6, 7 | ECON 1000 | 3”
  - equivalencies[IB-ECONOMICS-SL|SL 6, 7]:  ⟵ “Economics SL | 6, 7 | ECON 91000 | 3”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES-SL|SL 5, 6, 7]:  ⟵ “Environmental Systems and Societies SL | 5, 6, 7 | EVST 91000 | 3”
  - equivalencies[IB-GEOGRAPHY-HL|HL 5, 6, 7]:  ⟵ “Geography HL | 5, 6, 7 | GSCU 1000E | 3”
  - equivalencies[IB-GEOGRAPHY-SL|SL 5, 6, 7]:  ⟵ “Geography SL | 5, 6, 7 | GSCU 91000 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-HL|HL 5, 6, 7]:  ⟵ “Global Politics HL | 5, 6, 7 | POLS 91000 | 3”
  - equivalencies[IB-GLOBAL-POLITICS-SL|SL 5, 6, 7]:  ⟵ “Global Politics SL | 5, 6, 7 | POLS 91000 | 3”
  - equivalencies[IB-HISTORY-SL|SL 5, 6, 7]:  ⟵ “History SL | 5, 6, 7 | HIST 91000 | 3”
  - equivalencies[IB-HISTORY-HL|HL 5, 6, 7]:  ⟵ “History of Africa and the Middle East HL | 5, 6, 7 | HIST 91015 | 3”
  - equivalencies[IB-HISTORY-HL|HL 5, 6, 7]:  ⟵ “History of the Americas HL | 5, 6, 7 | HIST 91000 | 3”
  - equivalencies[IB-LATIN-HL|HL 5, 6, 7]:  ⟵ “Latin HL | 5, 6, 7 | CAMS 91000 | 3”
  - equivalencies[IB-LATIN-SL|SL 5, 6, 7]:  ⟵ “Latin SL | 5, 6, 7 | CAMS 91000 | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-HL|HL 6, 7]:  ⟵ “Math: Analysis & Approaches HL | 6, 7 | MATH 1131Q | 4”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES-SL|SL 6, 7]:  ⟵ “Math: Analysis & Approaches SL | 6, 7 | MATH 91050 | 3”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-HL|HL 7]:  ⟵ “Math: Applications & Interpretation HL | 7 | MATH 1131Q | 4”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION-SL|SL 7]:  ⟵ “Math: Applications & Interpretation SL | 7 | MATH 91050 | 3”
  - equivalencies[IB-PHILOSOPHY-HL|HL 5, 6, 7]:  ⟵ “Philosophy HL | 5, 6, 7 | PHIL 91000 | 3”
  - equivalencies[IB-PHILOSOPHY-SL|SL 5, 6, 7]:  ⟵ “Philosophy SL | 5, 6, 7 | PHIL 91000 | 3”
  - equivalencies[IB-PHYSICS-HL|HL 5]:  ⟵ “Physics HL | 5 | PHYS 1010Q | 4”
  - equivalencies[IB-PHYSICS-HL|HL 6, 7]:  ⟵ “Physics HL | 6, 7 | PHYS 1600Q | 4”
  - equivalencies[IB-PHYSICS-SL|SL 5]:  ⟵ “Physics SL | 5 | PHYS 1010Q | 4”
  - … 14 more rows
### `715ec6092f9cb433` University of Connecticut — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_source)
- source: https://admissions.uconn.edu/apply/transfer/transfer-credit/ap-ib-a-level-credit/ (sha256 46dc70e318bf)
- issues: stale_year_label:2025-26, shared_site_attribution_review
- checks: {"distinct_exams": 36, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|4, 5]:  ⟵ “AP Art History | 4, 5 | ARTH 1137 and 1138 | 6”
  - equivalencies[AP-MUSIC-THEORY|4, 5]:  ⟵ “AP Music Theory | 4, 5 | MUSI 1011 | 3”
  - equivalencies[AP-DRAWING|4, 5]:  ⟵ “AP Studio Art: Drawing | 4, 5 | ART 1030 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|4, 5]:  ⟵ “AP Studio Art: 2-D Design | 4, 5 | ART/Studio 1000-level | 3”
  - equivalencies[AP-3-D-ART-DESIGN|4, 5]:  ⟵ “AP Studio Art: 3-D Design | 4, 5 | ART/Studio 1000-level | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4, 5]:  ⟵ “AP English Language and Composition | 4, 5 | ENGL 1011 | 4”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4, 5]:  ⟵ “AP English Literature and Composition | 4, 5 | ENGL 1011 | 4”
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|4, 5]:  ⟵ “AP African American Studies | 4, 5 | AFRA 91000 | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|4, 5]:  ⟵ “AP Comparative Government and Politics | 4, 5 | POLS 1202 | 3”
  - equivalencies[AP-EUROPEAN-HISTORY|4, 5]:  ⟵ “AP European History | 4, 5 | HIST 1400 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|4, 5]:  ⟵ “AP Human Geography | 4, 5 | GSCU 1000E | 3”
  - equivalencies[AP-MACROECONOMICS|4, 5]:  ⟵ “AP Macroeconomics | 4, 5 | ECON 1202 | 3”
  - equivalencies[AP-MICROECONOMICS|4, 5]:  ⟵ “AP Microeconomics | 4, 5 | ECON 1201 | 3”
  - equivalencies[AP-PSYCHOLOGY|4, 5]:  ⟵ “AP Psychology | 4, 5 | PSYC 1000-level | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|4, 5]:  ⟵ “AP United States Government and Politics | 4, 5 | POLS 1602 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|4, 5]:  ⟵ “AP United States History | 4, 5 | HIST 1502 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|4, 5]:  ⟵ “AP World History | 4, 5 | HIST 1201 | 3”
  - equivalencies[AP-CALCULUS-AB|4, 5]:  ⟵ “AP Calculus AB | 4, 5 | MATH 1131Q | 4”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “AP Calculus BC* | 3 | MATH 1131Q | 4”
  - equivalencies[AP-CALCULUS-BC|4, 5]:  ⟵ “AP Calculus BC | 4, 5 | MATH 1131Q and 1132Q | 8”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4, 5]:  ⟵ “AP Computer Science A | 4, 5 | CSE 1010 | 3”
  - equivalencies[AP-PRECALCULUS|4, 5]:  ⟵ “AP Precalculus | 4, 5 | MATH 1060Q | 3”
  - equivalencies[AP-STATISTICS|4, 5]:  ⟵ “AP Statistics | 4, 5 | STAT 1100Q | 4”
  - equivalencies[AP-STATISTICS|*AB subscore of 4 or higher]:  ⟵ “AP Statistics | *AB subscore of 4 or higher”
  - equivalencies[AP-BIOLOGY|4, 5]:  ⟵ “AP Biology | 4, 5 | BIOL 1107 and 1108 | 8”
  - … 14 more rows

## Re-verification of existing records (11)

- source_not_fetched: data/institutions/albertus/credit_policies/2026-27.json ["credit_policies", "ipeds-128498", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/albertus/transfer_policies/2026-27.json ["transfer_policies", "ipeds-128498", null, "2026-27", {}]
- source_not_fetched: data/institutions/ccsu/credit_policies/2026-27.json ["credit_policies", "ipeds-128771", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/fairfield/transfer_policies/2026-27.json ["transfer_policies", "ipeds-129242", null, "2026-27", {}]
- source_not_fetched: data/institutions/goodwin/credit_policies/2026-27.json ["credit_policies", "ipeds-129154", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/bridgeport/credit_policies/2026-27.json ["credit_policies", "ipeds-128744", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/bridgeport/credit_policies/2026-27.json ["credit_policies", "ipeds-128744", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/hartford/credit_policies/2026-27.json ["credit_policies", "ipeds-129525", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/newhaven/credit_policies/2026-27.json ["credit_policies", "ipeds-129941", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/newhaven/transfer_policies/2026-27.json ["transfer_policies", "ipeds-129941", null, "2026-27", {}]
- source_not_fetched: data/institutions/wcsu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-130776", null, "2026-27", {}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- University of Connecticut: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
