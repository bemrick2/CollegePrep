# Review queue — NV (2026-27)

Pages fetched: 273; failures: 38. Candidates: 21 (4 without issues, 17 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 0 | 1 | 5 | 0 | 1 |
| cost_of_attendance | 0 | 0 | 0 | 0 | 6 | 0 | 1 |
| admissions_tests | 0 | 0 | 0 | 0 | 6 | 0 | 1 |
| common_data_set | 0 | 0 | 0 | 0 | 1 | 5 | 1 |
| merit_scholarships | 0 | 0 | 1 | 0 | 5 | 0 | 1 |
| ap_credit | 0 | 0 | 0 | 0 | 4 | 2 | 1 |
| clep_credit | 0 | 0 | 0 | 0 | 3 | 3 | 1 |
| ib_credit | 0 | 0 | 0 | 0 | 3 | 3 | 1 |
| dual_enrollment | 0 | 0 | 1 | 0 | 4 | 1 | 1 |
| transfer_credit | 0 | 0 | 0 | 0 | 6 | 0 | 1 |
| statewide_articulation | 0 | 0 | 0 | 0 | 3 | 3 | 1 |
| residency | 0 | 0 | 0 | 0 | 6 | 0 | 1 |
| degree_requirements | 0 | 0 | 0 | 0 | 4 | 2 | 1 |
| aid_appeals | 0 | 0 | 0 | 3 | 1 | 2 | 1 |

## Ready for review (4)

### `af91b63493d398e6` Nevada State University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://nevadastate.edu/admissions/dualcredit/how-to-apply/ (sha256 40ba696fbc59)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “Cumulative unweighted 3.0 GPA”
### `4c3876f72a4cc61f` University of Nevada-Reno — awards 2026-27 [new] (source_unlabeled)
- source: https://www.unr.edu/financial-aid/scholarships/first-year-scholarships/non-residents/wue/merit-scholarships (sha256 72af33a7468b)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '4.0', 'test': '36', 'amount_text': '4.0 GPA, ACT 36, SAT 1570: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '35', 'amount_text': '4.0 GPA, ACT 35, SAT 1530: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '34', 'amount_text': '4.0 GPA, ACT 34, SAT 1490: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '33', 'amount_text': '4.0 GPA, ACT 33, SAT 1450: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '32', 'amount_text': '4.0 GPA, ACT 32, SAT 1420: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '31', 'amount_text': '4.0 GPA, ACT 31, SAT 1390: Silver State Level $4,000/year'}, {'gpa': '4.0', 'test': '30', 'amount_text': '4.0 GPA, ACT 30, SAT 1360: Silver State Level $4,000/year'}, {'gpa': '4.0', 'test': '29', 'amount_text': '4.0 GPA, ACT 29, SAT 1330: Comstock Level $2,000/year'}, {'gpa': '4.0', 'test': '28', 'amount_text': '4.0 GPA, ACT 28, SAT 1300: Comstock Level $2,000/year'}, {'gpa': '4.0', 'test': '27', 'amount_text': '4.0 GPA, ACT 27, SAT 1260: Comstock Level $2,000/year'}, {'gpa': '4.0', 'test': '26', 'amount_text': '4.0 GPA, ACT 26, SAT 1230: Mt. Rose Level $1,500/year'}, {'gpa': '4.0', 'test': '25', 'amount_text': '4.0 GPA, ACT 25, SAT 1200: Mt. Rose Level $1,500/year'}, {'gpa': '4.0', 'test': '24', 'amount_text': '4.0 GPA, ACT 24, SAT 1160: Mt. Rose Level $1,500/year'}, {'gpa': '4.0', 'test': '23', 'amount_text': '4.0 GPA, ACT 23, SAT 1130: Battle Born Level $1,250/year'}, {'gpa': '4.0', 'test': '22', 'amount_text': '4.0 GPA, ACT 22, SAT 1100: Battle Born Level $1,250/year'}, {'gpa': '4.0', 'test': '21', 'amount_text': '4.0 GPA, ACT 21, SAT 1060: Battle Born Level $1,250/year'}, {'gpa': '4.0', 'test': '20', 'amount_text': '4.0 GPA, ACT 20, SAT 1030: Battle Born Level $1,250/year'}, {'gpa': '4.0', 'test': '19', 'amount_text': '4.0 GPA, ACT 19, SAT 990: Battle Born Level $1,250/year'}, {'gpa': '4.0', 'test': '18', 'amount_text': '4.0 GPA, ACT 18, SAT 960: Battle Born Level $1,250/year'}] ⟵ “ACT | 36 | 35 | 34 | 33 | 32 | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 || 4.0 | 4.0 GPA, ACT 36, SAT 1570: Presidential Level $10,000/year | 4.0 GPA, ACT 35, SAT 1530: Presidential Level $10,000/year | 4.0 GPA, ACT 34, SAT 1490: Presidential Level $10,000/year | 4.0 GPA, ”
  - test_requirement: Tiers by ACT and 36, 35… ⟵ “ACT | 36 | 35 | 34 | 33 | 32 | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 || 4.0 | 4.0 GPA, ACT 36, SAT 1570: Presidential Level $10,000/year | 4.0 GPA, ACT 35, SAT 1530: Presidential Level $10,000/year | 4.0 GPA, ACT 34, SAT 1490: Presidential Level $10,000/year | 4.0 GPA, ”
### `7938d7682a9427de` University of Nevada-Reno — awards 2027-28 [new] (labeled_in_source)
- source: https://www.unr.edu/financial-aid/scholarships/first-year-scholarships/nevada-residents (sha256 7a6ff26a38e7)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '4.0', 'amount_text': '$3,000'}, {'gpa': '3.8-3.99', 'amount_text': '$1,500'}, {'gpa': '3.4-3.79', 'amount_text': '$750'}, {'gpa': '3.0-3.39', 'amount_text': '$500'}] ⟵ “GPA | Award Amount || 4.0 | $3,000 || 3.8-3.99 | $1,500 || 3.4-3.79 | $750 || 3.0-3.39 | $500”
  - gpa_requirement: Tiered by GPA: 4.0 → $3,000; 3.8-3.99 → $1,500; 3.4-3.79 → $750; 3.0-3.39 → $500 ⟵ “GPA | Award Amount || 4.0 | $3,000 || 3.8-3.99 | $1,500 || 3.4-3.79 | $750 || 3.0-3.39 | $500”
### `b36009156314f014` University of Nevada-Reno — awards 2027-28 [new] (labeled_in_source)
- source: https://www.unr.edu/financial-aid/scholarships/first-year-scholarships/nevada-residents (sha256 7a6ff26a38e7)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '4.0', 'test': '36', 'amount_text': '4.0 GPA, ACT 36, SAT 1570: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '35', 'amount_text': '4.0 GPA, ACT 35, SAT 1530: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '34', 'amount_text': '4.0 GPA, ACT 34, SAT 1490: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '33', 'amount_text': '4.0 GPA, ACT 33, SAT 1450: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '32', 'amount_text': '4.0 GPA, ACT 32, SAT 1420: Presidential Level $10,000/year'}, {'gpa': '4.0', 'test': '31', 'amount_text': '4.0 GPA, ACT 31, SAT 1390: Provost Level $5,000/year'}, {'gpa': '4.0', 'test': '30', 'amount_text': '4.0 GPA, ACT 30, SAT 1360: Provost Level $5,000/year'}, {'gpa': '4.0', 'test': '29', 'amount_text': '4.0 GPA, ACT 29, SAT 1330: Nevada Scholars $3,000/year'}, {'gpa': '4.0', 'test': '28', 'amount_text': '4.0 GPA, ACT 28, SAT 1300: Nevada Scholars $3,000/year'}, {'gpa': '4.0', 'test': '27', 'amount_text': '4.0 GPA, ACT 27, SAT 1260: Nevada Scholars $3,000/year'}, {'gpa': '4.0', 'test': '26', 'amount_text': '4.0 GPA, ACT 26, SAT 1230: Pack Pride $2,000/year'}, {'gpa': '4.0', 'test': '25', 'amount_text': '4.0 GPA, ACT 25, SAT 1200: Pack Pride $2,000/year'}, {'gpa': '4.0', 'test': '24', 'amount_text': '4.0 GPA, ACT 24, SAT 1160: Pack Pride $2,000/year'}, {'gpa': '4.0', 'test': '23', 'amount_text': '4.0 GPA, ACT 23, SAT 1130: Alphie $1,500/year'}, {'gpa': '4.0', 'test': '22', 'amount_text': '4.0 GPA, ACT 22, SAT 1100: Alphie $1,500/year'}, {'gpa': '4.0', 'test': '21', 'amount_text': '4.0 GPA, ACT 21, SAT 1060: Alphie $1,500/year'}, {'gpa': '4.0', 'test': '20', 'amount_text': '4.0 GPA, ACT 20, SAT 1030: Alphie $1,500/year'}, {'gpa': '4.0', 'test': '19', 'amount_text': '4.0 GPA, ACT 19, SAT 990: Alphie $1,500/year'}, {'gpa': '4.0', 'test': '18', 'amount_text': '4.0 GPA, ACT 18, SAT 960: Alphie $1,500/year'}] ⟵ “ACT | 36 | 35 | 34 | 33 | 32 | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 || 4.0 | 4.0 GPA, ACT 36, SAT 1570: Presidential Level $10,000/year | 4.0 GPA, ACT 35, SAT 1530: Presidential Level $10,000/year | 4.0 GPA, ACT 34, SAT 1490: Presidential Level $10,000/year | 4.0 GPA, ”
  - test_requirement: Tiers by ACT and 36, 35… ⟵ “ACT | 36 | 35 | 34 | 33 | 32 | 31 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 || 4.0 | 4.0 GPA, ACT 36, SAT 1570: Presidential Level $10,000/year | 4.0 GPA, ACT 35, SAT 1530: Presidential Level $10,000/year | 4.0 GPA, ACT 34, SAT 1490: Presidential Level $10,000/year | 4.0 GPA, ”

## Exceptions (17)

### `2ae2f11412ca7719` state-NV — state_policies 2026-27 · policy_kind=dual_enrollment [new] (ambiguous_year_labels)
- source: https://nshe.nevada.edu/wp-content/uploads/file/BoardOfRegents/PGManual/chapters//Chapter%2007%20-%20Fees%20and%20Tuition.pdf (sha256 bdc3dd42b446)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"effective": 5, "exceptions": 15, "guarantees": 1, "requirements": 27}
  - statements.requirements: 27 ⟵ “Institutions shall establish a procedure and timeline in which verification must be made for the institution to apply the FRL dual enrollment pricing.”
  - statements.exceptions: 15 ⟵ “Except for those students receiving WICHE support, all non-resident medical students upon matriculation shall be assessed combined annual non-resident tuition and registration fees as follows: Medical School              2025-26          2026-27           2027-28         2028-29 Non-resident        ”
  - statements.effective: 5 ⟵ “The effective date of Fall 2024 is for newly admitted students.”
  - statements.guarantees: 1 ⟵ “Proof of equivalent coverage will be accepted on a limited basis.”
### `47068a69fbea7295` state-NV — state_policies 2026-27 · policy_kind=statewide_articulation [new] (source_unlabeled)
- source: https://nshe.nevada.edu/wp-content/uploads/file/BoardOfRegents/Handbook/title4//T4-CH14%20NSHE%20Planning%20Program%20Review%20Articulation%20and%20Enrollment%20Policies.pdf (sha256 93cb8662cbaf)
- issues: semantic_review_required
- checks: {"effective": 6, "exceptions": 8, "guarantees": 4, "requirements": 92}
  - statements.requirements: 92 ⟵ “All new campus and branch campus instructional sites must be approved by the Board of Regents.”
  - statements.effective: 6 ⟵ “Desert Research Institute – The Desert Research Institute will conduct basic and applied research at the state, national and international levels for effective management of environmental resources, for continued development of Nevada's economy, and for providing increased educational opportunities ”
  - statements.exceptions: 8 ⟵ “However, it is not the intention of the NSHE for community colleges to abandon their community college mission to transform into State Colleges.”
  - statements.guarantees: 4 ⟵ “Baccalaureate level courses included as part of the associate of arts, associate of science, or associate of business degree will transfer to any other NSHE institution at a minimum e.”
### `83b05ec4c6458d54` state-NV — state_policies 2021-22 · policy_kind=dual_enrollment [new] (labeled_in_source)
- source: https://nshe.nevada.edu/wp-content/uploads/file/BoardOfRegents/Handbook/title4//T4-CH16%20Student%20Admission%20Registration%20Grades%20and%20Examinations.pdf (sha256 9aba22d1540a)
- issues: stale_year_label:2021-22, semantic_review_required
- checks: {"effective": 2, "exceptions": 26, "guarantees": 1, "requirements": 97}
  - statements.effective: 2 ⟵ “Title 4 - Codification of Board Policy Statements STUDENT ADMISSION, REGISTRATION, GRADES AND Fall 2021) ............................................................................................................2 (Effective July 1, 2020).............................................................”
  - statements.requirements: 97 ⟵ “Continuous Enrollment Requirement.”
  - statements.exceptions: 26 ⟵ “Except as otherwise provided, effective Fall 2021, traditional forms of remediation, including courses numbered below 100, shall not be offered i.”
  - statements.guarantees: 1 ⟵ “Students seeking admission to a university whose high school grade point average or test scores are insufficient for admission will be offered enrollment at a NSHE community college with a subsequent guarantee of admission to the universities or state college under the transfer criteria established ”
### `02d0e3741b5c8227` College of Southern Nevada — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.csn.edu/satisfactory-academic-progress-sap-policy (sha256 7962b8a6078c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 15}
  - sentence: sap_appeal ⟵ “Regaining Eligibility for Financial Aid & SAP Appeal Process Students are encouraged to consult with the CSN Office Financial Aid to determine the best academic strategy to regain eligibility.”
  - sentence: sap_appeal ⟵ “Students submitting a SAP Appeal must do so by the stated deadlines indicated in our Important Financial Aid Dates.”
  - sentence: sap_appeal ⟵ “All SAP Appeals must include the following: A typewritten Personal Statement addressing: Any extenuating circumstance that caused you to be placed on SAP Suspension.”
  - sentence: sap_appeal ⟵ “Additionally, students will be responsible for any charges on their student account if the SAP Appeal decision is not approved.”
  - sentence: sap_appeal ⟵ “SAP Appeals Committee and Decision The review and adjudication of SAP Appeals are made by a committee of Financial Aid professionals and are final.”
  - sentence: sap_appeal ⟵ “Approved SAP Appeals If approved, students will be placed on Probation.”
### `db60c1e9d7149ed7` Great Basin College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.gbcnv.edu/financial/cost.html (sha256 b8c0cbb480dc)
- issues: arrangement_unlabeled, multiple_total_rows, residency_unknown
- checks: {"columns": 4, "rows": 8}
  - column:Tuition & Fees (Lower Division): 4433 ⟵ “Tuition & Fees (Lower Division) | $4,433 | $2,955 | $2,069 | $887”
  - column:Tuition & Fees (Upper Division): 7125 ⟵ “Tuition & Fees (Upper Division) | $7,125 | $4,750 | $3,325 | $1,425”
  - column:Books/Supplies: 1300 ⟵ “Books/Supplies | $1,300 | $975 | $650 | $300”
  - column:Living Expenses (Food and Housing): 14897 ⟵ “Living Expenses (Food and Housing) | $14,897 | $14,897 | $14,897 | -”
  - column:Personal: 3150 ⟵ “Personal | $3,150 | $3,150 | $3,150 | -”
  - column:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $1,200”
  - column:TOTAL COST (LOWER DIVISION): 26180 ⟵ “TOTAL COST (LOWER DIVISION) | $26,180 | $24,377 | $23,166 | $2,387”
  - column:TOTAL COST (UPPER DIVISION): 28872 ⟵ “TOTAL COST (UPPER DIVISION) | $28,872 | $26,172 | $24,442 | $2,925”
  - column:Tuition & Fees (Lower Division): 2955 ⟵ “Tuition & Fees (Lower Division) | $4,433 | $2,955 | $2,069 | $887”
  - column:Tuition & Fees (Upper Division): 4750 ⟵ “Tuition & Fees (Upper Division) | $7,125 | $4,750 | $3,325 | $1,425”
  - column:Books/Supplies: 975 ⟵ “Books/Supplies | $1,300 | $975 | $650 | $300”
  - column:Living Expenses (Food and Housing): 14897 ⟵ “Living Expenses (Food and Housing) | $14,897 | $14,897 | $14,897 | -”
  - column:Personal: 3150 ⟵ “Personal | $3,150 | $3,150 | $3,150 | -”
  - column:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $1,200”
  - column:TOTAL COST (LOWER DIVISION): 24377 ⟵ “TOTAL COST (LOWER DIVISION) | $26,180 | $24,377 | $23,166 | $2,387”
  - column:TOTAL COST (UPPER DIVISION): 26172 ⟵ “TOTAL COST (UPPER DIVISION) | $28,872 | $26,172 | $24,442 | $2,925”
  - column:Tuition & Fees (Lower Division): 2069 ⟵ “Tuition & Fees (Lower Division) | $4,433 | $2,955 | $2,069 | $887”
  - column:Tuition & Fees (Upper Division): 3325 ⟵ “Tuition & Fees (Upper Division) | $7,125 | $4,750 | $3,325 | $1,425”
  - column:Books/Supplies: 650 ⟵ “Books/Supplies | $1,300 | $975 | $650 | $300”
  - column:Living Expenses (Food and Housing): 14897 ⟵ “Living Expenses (Food and Housing) | $14,897 | $14,897 | $14,897 | -”
  - column:Personal: 3150 ⟵ “Personal | $3,150 | $3,150 | $3,150 | -”
  - column:Transportation: 2400 ⟵ “Transportation | $2,400 | $2,400 | $2,400 | $1,200”
  - column:TOTAL COST (LOWER DIVISION): 23166 ⟵ “TOTAL COST (LOWER DIVISION) | $26,180 | $24,377 | $23,166 | $2,387”
  - column:TOTAL COST (UPPER DIVISION): 24442 ⟵ “TOTAL COST (UPPER DIVISION) | $28,872 | $26,172 | $24,442 | $2,925”
  - column:Tuition & Fees (Lower Division): 887 ⟵ “Tuition & Fees (Lower Division) | $4,433 | $2,955 | $2,069 | $887”
  - … 5 more rows
### `6cee2fc7ca939921` Nevada State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://nevadastate.edu/wp-content/uploads/2025/06/2025-2026-NS-COA-1.pdf (sha256 899f307d38b2)
- issues: arrangement_unlabeled, multiple_total_rows, stale_year_label:2025-26
- checks: {"columns": 7, "rows": 71}
  - column:NEVADA RESIDENT 34,545: 17274 ⟵ “NEVADA RESIDENT 34,545 | 17,274 | 32,822 16,412 | 31,099 15,551 | 29,376 14,689 | 4,939 | 2,470”
  - column:NON-RESIDENT 50,020: 25011 ⟵ “NON-RESIDENT 50,020 | 25,011 | 48,297 24,149 | 46,574 23,288 | 32,127 16,065 | 6,315 | 3,158”
  - column:WUE 37,673: 18838 ⟵ “WUE 37,673 | 18,838 | 35,324 17,663 | 32,976 16,489 | 30,627 15,315 | 5,565 | 2,783”
  - column:NEVADA 23,799: 11900 ⟵ “NEVADA 23,799 | 11,900 | 22,076 11,038 | 20,353 10,177 | 18,630 | 9,315 | 4,939 | 2,470”
  - column:NON-RESIDENT 39,274: 19638 ⟵ “NON-RESIDENT 39,274 | 19,638 | 37,551 18,776 | 35,828 17,915 | 21,381 10,691 | 6,315 | 3,158”
  - column:WUE 26,926: 13464 ⟵ “WUE 26,926 | 13,464 | 24,578 12,289 | 22,229 11,115 | 19,881 | 9,940 | 5,565 | 2,783”
  - column:NEVADA 27,373: 13688 ⟵ “NEVADA 27,373 | 13,688 | 25,650 12,826 | 23,927 11,965 | 22,204 11,103 | 2,367 | 1,184”
  - column:NON-RESIDENT 42,848: 21426 ⟵ “NON-RESIDENT 42,848 | 21,426 | 41,125 20,564 | 39,402 19,703 | 24,955 12,479 | 3,743 | 1,872”
  - column:WUE 30,501: 15251 ⟵ “WUE 30,501 | 15,251 | 28,152 14,076 | 25,804 12,902 | 23,455 11,728 | 2,993 | 1,497”
  - column:NEVADA 28,329: 14165 ⟵ “NEVADA 28,329 | 14,165 | 26,606 13,303 | 24,883 12,442 | 23,160 11,580 | 2,367 | 1,184”
  - column:NON-RESIDENT 43,804: 21903 ⟵ “NON-RESIDENT 43,804 | 21,903 | 42,081 21,041 | 40,358 20,180 | 25,911 12,956 | 3,743 | 1,872”
  - column:WUE 31,456: 15729 ⟵ “WUE 31,456 | 15,729 | 29,108 14,554 | 26,759 13,380 | 24,411 12,206 | 2,993 | 1,497”
  - column:NEVADA 33,835: 16919 ⟵ “NEVADA 33,835 | 16,919 | 30,673 15,338”
  - column:NON-RESIDENT 49,310: 24657 ⟵ “NON-RESIDENT 49,310 | 24,657 | 34,378 17,191”
  - column:NEVADA 23,089: 11545 ⟵ “NEVADA 23,089 | 11,545 | 19,927 | 9,964”
  - column:NON-RESIDENT 38,564: 19283 ⟵ “NON-RESIDENT 38,564 | 19,283 | 23,632 11,817”
  - column:NEVADA 26,663: 13333 ⟵ “NEVADA 26,663 | 13,333 | 23,501 11,752”
  - column:NON-RESIDENT 42,138: 21071 ⟵ “NON-RESIDENT 42,138 | 21,071 | 27,206 13,605”
  - column:NEVADA 27,619: 13810 ⟵ “NEVADA 27,619 | 13,810 | 24,457 12,229”
  - column:NON-RESIDENT 43,094: 21548 ⟵ “NON-RESIDENT 43,094 | 21,548 | 28,162 14,082”
  - column:Fees*: 7290 ⟵ “Fees* | 7,290 | 5,892 | 4,494 | 3,096 | 1,398”
  - column:Books/Supplies:: 1625 ⟵ “Books/Supplies: | 1,625 | 1,300 | 975 | 650 | 325”
  - column:Housing:: 14082 ⟵ “Housing: | 14,082 | 14,082 | 14,082 | 14,082 | -”
  - column:Food:: 4759 ⟵ “Food: | 4,759 | 4,759 | 4,759 | 4,759 | -”
  - column:Transportation:: 3216 ⟵ “Transportation: | 3,216 | 3,216 | 3,216 | 3,216 | 3,216”
  - … 2295 more rows
### `be8631bc50062320` Nevada State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://nevadastate.edu/wp-content/uploads/2026/03/2026-2027-NS-COA.pdf (sha256 1404f4555497)
- issues: arrangement_unlabeled, multiple_total_rows
- checks: {"columns": 7, "rows": 69}
  - column:NEVADA RESIDENT 39,615: 19809 ⟵ “NEVADA RESIDENT 39,615 | 19,809 | 37,778 18,890 | 35,941 17,972 | 34,104 17,053 | 5,197 | 2,599”
  - column:NON-RESIDENT 56,384: 28194 ⟵ “NON-RESIDENT 56,384 | 28,194 | 54,547 27,275 | 52,710 26,357 | 36,855 18,429 | 6,573 | 3,287”
  - column:WUE 43,395: 21699 ⟵ “WUE 43,395 | 21,699 | 40,802 20,402 | 38,209 19,106 | 35,616 17,809 | 5,953 | 2,977”
  - column:NEVADA 24,480: 12241 ⟵ “NEVADA 24,480 | 12,241 | 22,643 11,322 | 20,806 10,404 | 18,969 | 9,485 | 5,197 | 2,599”
  - column:NON-RESIDENT 41,249: 20626 ⟵ “NON-RESIDENT 41,249 | 20,626 | 39,412 19,707 | 37,575 18,789 | 21,720 10,861 | 6,573 | 3,287”
  - column:WUE 28,260: 14130 ⟵ “WUE 28,260 | 14,130 | 25,667 12,833 | 23,074 11,537 | 20,481 10,240 | 5,953 | 2,977”
  - column:NEVADA 29,191: 14597 ⟵ “NEVADA 29,191 | 14,597 | 27,354 13,678 | 25,517 12,760 | 23,680 11,841 | 2,509 | 1,255”
  - column:NON-RESIDENT 45,960: 22982 ⟵ “NON-RESIDENT 45,960 | 22,982 | 44,123 22,063 | 42,286 21,145 | 26,431 13,217 | 3,885 | 1,943”
  - column:WUE 32,971: 16486 ⟵ “WUE 32,971 | 16,486 | 30,378 15,189 | 27,785 13,893 | 25,192 12,596 | 3,265 | 1,633”
  - column:NEVADA 30,118: 15060 ⟵ “NEVADA 30,118 | 15,060 | 28,281 14,141 | 26,444 13,223 | 24,607 12,304 | 2,509 | 1,255”
  - column:NON-RESIDENT 46,887: 23445 ⟵ “NON-RESIDENT 46,887 | 23,445 | 45,050 22,526 | 43,213 21,608 | 27,358 13,680 | 3,885 | 1,943”
  - column:WUE 33,898: 16950 ⟵ “WUE 33,898 | 16,950 | 31,305 15,653 | 28,712 14,357 | 26,119 13,060 | 3,265 | 1,633”
  - column:NEVADA 38,835: 19419 ⟵ “NEVADA 38,835 | 19,419 | 35,473 17,738”
  - column:NON-RESIDENT 55,604: 27804 ⟵ “NON-RESIDENT 55,604 | 27,804 | 39,487 19,745”
  - column:NEVADA 23,700: 11851 ⟵ “NEVADA 23,700 | 11,851 | 20,338 10,170”
  - column:NON-RESIDENT 40,469: 20236 ⟵ “NON-RESIDENT 40,469 | 20,236 | 24,352 12,177”
  - column:NEVADA 28,411: 14207 ⟵ “NEVADA 28,411 | 14,207 | 25,049 12,526”
  - column:NON-RESIDENT 45,180: 22592 ⟵ “NON-RESIDENT 45,180 | 22,592 | 29,063 14,533”
  - column:NEVADA 29,338: 14670 ⟵ “NEVADA 29,338 | 14,670 | 25,976 12,989”
  - column:NON-RESIDENT 46,107: 23055 ⟵ “NON-RESIDENT 46,107 | 23,055 | 29,990 14,996”
  - column:Fees*: 7860 ⟵ “Fees* | 7,860 | 6,348 | 4,836 | 3,324 | 1,512”
  - column:Books/Supplies:: 1625 ⟵ “Books/Supplies: | 1,625 | 1,300 | 975 | 650 | 325”
  - column:Housing:: 16565 ⟵ “Housing: | 16,565 | 16,565 | 16,565 | 16,565 | -”
  - column:Food:: 6720 ⟵ “Food: | 6,720 | 6,720 | 6,720 | 6,720 | -”
  - column:Transportation:: 3360 ⟵ “Transportation: | 3,360 | 3,360 | 3,360 | 3,360 | 3,360”
  - … 2289 more rows
### `b09529bf7c0c4abf` University of Nevada-Las Vegas — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unlv.edu/finaid/checklist/after-sap (sha256 d4b4eab0cd8b)
- issues: semantic_review_required, conflicting_sources:https://www.unlv.edu/sites/default/files/page_files/27/SATISFACTORY-ACADEMIC-PROGRESS-%28SAP%29-%282%29-%281%29.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “To initiate an appeal, a student must complete a Satisfactory Academic Progress Appeal Form available on the forms page.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeal Form must be submitted in the Rebel Success Hub.”
### `c80b6ea614dc49e6` University of Nevada-Las Vegas — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unlv.edu/sites/default/files/page_files/27/SATISFACTORY-ACADEMIC-PROGRESS-%28SAP%29-%282%29-%281%29.pdf (sha256 3163dae4368f)
- issues: semantic_review_required, conflicting_sources:https://www.unlv.edu/finaid/checklist/after-sap
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: sap_appeal ⟵ “See example below: Reinstatement of Financial Aid Eligibility: Revised 01/21/2015, 06/06/2022 Assuming a satisfactory academic progress policy appeal has not been approved by the UNLV Office of Financial Aid & Scholarships, a student may pay for college expenses at their own expense in order to make up any SAP policy deficiencies.”
  - sentence: sap_appeal ⟵ “The review of your SAP appeal is a very time-consuming process.”
  - sentence: sap_appeal ⟵ “It may take up to 10 business days to review a properly completed SAP appeal submitted by a student.”
  - sentence: sap_appeal ⟵ “Do not attempt to rush and complete a SAP appeal as quickly as you can.”
  - sentence: sap_appeal ⟵ “A SAP appeal submitted to the office should be clear, concise, have a well-described timeline of events and must have supporting documentation.”
  - sentence: sap_appeal ⟵ “We conspicuously advertise our deadline within our online Satisfactory Academic Progress Policy, the SAP Appeal Form and your MyUNLV online financial aid award notice.”
### `321ce0c0fa30c962` University of Nevada-Las Vegas — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://www.unlv.edu/admissions/paying-for-college/costs (sha256 06ce0b8e0f3c)
- issues: ambiguous_year_labels, multiple_total_rows
- checks: {"columns": 3, "rows": 7}
  - off_campus_not_with_family:Tuition and Fees (15 credits): 11231 ⟵ “Tuition and Fees (15 credits) | $11,231* | $11,231* | $11,231*”
  - off_campus_not_with_family:Housing & Utilities: 8690 ⟵ “Housing & Utilities | $8,690 | $2,897 | $7,424 (source: Housing & Residential Life)”
  - off_campus_not_with_family:Food: 6024 ⟵ “Food | $6,024 | $3,012 | $6,024 (source: Housing & Residential Life)”
  - off_campus_not_with_family:Books, Course Materials, Supplies & Equipment: 1290 ⟵ “Books, Course Materials, Supplies & Equipment | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Transportation: 3040 ⟵ “Transportation | $3,040 | $3,040 | $1,360”
  - off_campus_not_with_family:Miscellaneous & Personal: 3304 ⟵ “Miscellaneous & Personal | $3,304 | $3,304 | $3,304”
  - off_campus_not_with_family:Federal Student Loan Fees**: 50 ⟵ “Federal Student Loan Fees** | $50 | $50 | $50”
  - off_campus_not_with_family:Nevada Residents Total Estimated Expenses: 33629 ⟵ “Nevada Residents Total Estimated Expenses | $33,629 | $24,824 | $30,683”
  - off_campus_not_with_family:Nonresidents*** Total Estimated Expenses: 53230 ⟵ “Nonresidents*** Total Estimated Expenses | $53,230 | $44,425 | $50,284”
  - with_parents_or_family:Tuition and Fees (15 credits): 11231 ⟵ “Tuition and Fees (15 credits) | $11,231* | $11,231* | $11,231*”
  - with_parents_or_family:Housing & Utilities: 2897 ⟵ “Housing & Utilities | $8,690 | $2,897 | $7,424 (source: Housing & Residential Life)”
  - with_parents_or_family:Food: 3012 ⟵ “Food | $6,024 | $3,012 | $6,024 (source: Housing & Residential Life)”
  - with_parents_or_family:Books, Course Materials, Supplies & Equipment: 1290 ⟵ “Books, Course Materials, Supplies & Equipment | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Transportation: 3040 ⟵ “Transportation | $3,040 | $3,040 | $1,360”
  - with_parents_or_family:Miscellaneous & Personal: 3304 ⟵ “Miscellaneous & Personal | $3,304 | $3,304 | $3,304”
  - with_parents_or_family:Federal Student Loan Fees**: 50 ⟵ “Federal Student Loan Fees** | $50 | $50 | $50”
  - with_parents_or_family:Nevada Residents Total Estimated Expenses: 24824 ⟵ “Nevada Residents Total Estimated Expenses | $33,629 | $24,824 | $30,683”
  - with_parents_or_family:Nonresidents*** Total Estimated Expenses: 44425 ⟵ “Nonresidents*** Total Estimated Expenses | $53,230 | $44,425 | $50,284”
  - on_campus:Tuition and Fees (15 credits): 11231 ⟵ “Tuition and Fees (15 credits) | $11,231* | $11,231* | $11,231*”
  - on_campus:Books, Course Materials, Supplies & Equipment: 1290 ⟵ “Books, Course Materials, Supplies & Equipment | $1,290 | $1,290 | $1,290”
  - on_campus:Transportation: 1360 ⟵ “Transportation | $3,040 | $3,040 | $1,360”
  - on_campus:Miscellaneous & Personal: 3304 ⟵ “Miscellaneous & Personal | $3,304 | $3,304 | $3,304”
  - on_campus:Federal Student Loan Fees**: 50 ⟵ “Federal Student Loan Fees** | $50 | $50 | $50”
  - on_campus:Nevada Residents Total Estimated Expenses: 30683 ⟵ “Nevada Residents Total Estimated Expenses | $33,629 | $24,824 | $30,683”
  - on_campus:Nonresidents*** Total Estimated Expenses: 50284 ⟵ “Nonresidents*** Total Estimated Expenses | $53,230 | $44,425 | $50,284”
### `1946e0f008c52c7f` University of Nevada-Reno — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.unr.edu/financial-aid/apply/forms (sha256 6a81352caeea)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Reporting Changes [DocuSign PowerForm] Satisfactory Academic Progress Appeal The Satisfactory Academic Progress Appeal is available for students who have fallen below financial aid GPA or pace (pass rate) requirements to appeal for continued financial aid eligibility.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal [DocuSign PowerForm] Medical Student Satisfactory Academic Progress Appeal [PDF] Scholarship Appeal The Scholarship Appeal form allows students who have already been awarded a scholarship to request reconsideration after losing eligibility due to circumstances beyond their control.”
### `3041469eb35f58f2` University of Nevada-Reno — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unr.edu/financial-aid/satisfactory-academic-progress (sha256 a2434cc9c7f0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “It is at the discretion of the appeals coordinator to make a professional judgement on whether an appeal should be discussed with a formal committee comprised of representatives from across campus.”
  - sentence: professional_judgment ⟵ “It is at the discretion of the appeals coordinator to make a professional judgement on whether an appeal should be discussed with a formal committee comprised of representatives from across campus.”
  - sentence: professional_judgment ⟵ “It is at the discretion of the appeals coordinator to make a professional judgement on whether an appeal should be discussed with a formal committee comprised of representatives from across campus.”
  - sentence: professional_judgment ⟵ “It is at the discretion of the appeals coordinator to make a professional judgement on whether an appeal should be discussed with a formal committee comprised of representatives from across campus.”
### `584de635cccaccfe` University of Nevada-Reno — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.unr.edu/financial-aid/apply/forms (sha256 6a81352caeea)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Scholarship/Fellowship Request [DocuSign PowerForm] Special Circumstances The Special Circumstances form allows students to request special consideration for circumstances not reflected in the information provided when initially completing the FAFSA, such as divorce or loss of child support.”
  - sentence: need_based_special_circumstances ⟵ “Approval may result in changes to a student’s Student Aid Index (SAI), Cost of Attendance budget (COA) or both. 2026-2027 Special Circumstances [Docusign PowerForm] 2025-2026 Special Circumstances [PDF] Student Release for Third Party Agencies The Student Release for Third Party Agencies allows the Financial Aid Office to share financial aid information with organizations not affiliated with the U”
### `5c6db3758b44f44c` University of Nevada-Reno — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unr.edu/financial-aid/satisfactory-academic-progress (sha256 a2434cc9c7f0)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 12}
  - sentence: sap_appeal ⟵ “Probation status - Undergraduate students Students who are no longer meeting SAP standards due to a deficiency in remedial coursework completion, GPA, or Pace and have had a Satisfactory Academic Progress Appeal approved will be placed on financial aid probation.”
  - sentence: sap_appeal ⟵ “Appeals - Undergraduate students If you do not meet satisfactory academic progress standards, you may submit an appeal.”
  - sentence: sap_appeal ⟵ “If you have a GPA, pace, or remedial coursework issue, you may submit the Satisfactory Academic Progress Appeal.”
  - sentence: sap_appeal ⟵ “Probation status - Graduate students Students who are no longer meeting SAP standards due to a deficiency in GPA and/or pace and have had a Satisfactory Academic Progress Appeal approved will be placed on financial aid probation.”
  - sentence: sap_appeal ⟵ “Appeals - Graduate students If you do not meet satisfactory academic progress standards, you may submit an appeal.”
  - sentence: sap_appeal ⟵ “If you have a GPA, pace, or remedial coursework issue, you may submit the Satisfactory Academic Progress Appeal.”
### `8301d558cb8318ae` University of Nevada-Reno — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.unr.edu/financial-aid/scholarships/first-year-scholarships/nevada-residents (sha256 7a6ff26a38e7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: scholarship_retention_appeal ⟵ “Scholarship appeal form > Will I lose my scholarship if I go on a Leave of Absence?”
  - sentence: scholarship_retention_appeal ⟵ “Not enrolling in the required 15 credits each semester (Fall/Spring) Not earning/completing 15 credits each semester (Fall/Spring) Not meeting the Satisfactory Academic Progress policy standards Graduating or letting your scholarship expire, whichever happens first Not meeting GPA requirements to maintain scholarship Discontinued enrollment at the University Is there an appeal process if I permane”
  - sentence: scholarship_retention_appeal ⟵ “There is no appeal process if a student has permanently lost the scholarship.”
  - sentence: scholarship_retention_appeal ⟵ “Loss due to GPA: Students may submit a scholarship appeal form if they have an extenuating circumstance that caused their cumulative University of Nevada, Reno GPA to drop below the minimum requirement.”
### `b000c8f2334fbb6e` University of Nevada-Reno — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.unr.edu/financial-aid/scholarships/first-year-scholarships/non-residents/stackable-awards (sha256 a71fd9d3f5da)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Students who become ineligible due to not meeting the Satisfactory Academic Progress policy may regain eligibility by: Successfully going through the appeal process; or restore eligibility by meeting SAP requirements.”
### `bd8206e7f2d354a0` University of Nevada-Reno — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.unr.edu/financial-aid/scholarships/first-year-scholarships/non-residents/wue/merit-scholarships (sha256 72af33a7468b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: scholarship_retention_appeal ⟵ “Scholarship appeal form > Will I lose my scholarship if I go on a Leave of Absence?”
  - sentence: scholarship_retention_appeal ⟵ “Not enrolling in the required 15 credits each semester (Fall/Spring) Not earning/completing 15 credits each semester (Fall/Spring) Not meeting the Satisfactory Academic Progress policy standards Graduating or letting your scholarship expire, whichever happens first Not meeting GPA requirements to maintain scholarship Discontinued enrollment at the University Is there an appeal process if I permane”
  - sentence: scholarship_retention_appeal ⟵ “There is no appeal process if a student has permanently lost the scholarship.”
  - sentence: scholarship_retention_appeal ⟵ “Loss due to GPA: Students may submit a scholarship appeal form if they have an extenuating circumstance that caused their cumulative University of Nevada, Reno GPA to drop below the minimum requirement.”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 15; pages by category: admissions_tests 5, cost_of_attendance 1, degree_requirements 1, dual_enrollment 3, merit_scholarships 3, residency 2, tuition_fees 4

## Blocked by the site (every request refused; needs the browser fallback)

- Truckee Meadows Community College (`ipeds-182500`)

## Leads: official pages found with no extracted record

- College of Southern Nevada: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Great Basin College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Nevada State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency
- University of Nevada-Las Vegas: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, transfer_credit, residency
- University of Nevada-Reno: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Western Nevada College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency, degree_requirements, aid_appeals
