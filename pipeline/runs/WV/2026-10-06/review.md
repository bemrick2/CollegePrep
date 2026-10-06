# Review queue — WV (2026-27)

Pages fetched: 1514; failures: 381. Candidates: 333 (38 without issues, 295 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 0 | 0 | 8 | 8 | 5 | 0 | 7 |
| cost_of_attendance | 0 | 0 | 6 | 3 | 12 | 0 | 7 |
| admissions_tests | 0 | 0 | 0 | 0 | 20 | 1 | 7 |
| common_data_set | 0 | 0 | 0 | 0 | 6 | 15 | 7 |
| merit_scholarships | 0 | 0 | 2 | 1 | 18 | 0 | 7 |
| ap_credit | 0 | 0 | 1 | 3 | 6 | 11 | 7 |
| clep_credit | 0 | 0 | 1 | 0 | 2 | 18 | 7 |
| ib_credit | 0 | 0 | 1 | 1 | 1 | 18 | 7 |
| dual_enrollment | 0 | 0 | 1 | 0 | 13 | 7 | 7 |
| transfer_credit | 0 | 0 | 8 | 1 | 12 | 0 | 7 |
| statewide_articulation | 0 | 0 | 0 | 0 | 9 | 12 | 7 |
| residency | 0 | 0 | 0 | 0 | 18 | 3 | 7 |
| degree_requirements | 0 | 0 | 0 | 1 | 17 | 3 | 7 |
| aid_appeals | 0 | 0 | 0 | 15 | 4 | 2 | 7 |

## Ready for review (38)

### `6c9e61714c11136a` Bluefield State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://bluefieldstate.edu/financial-aid/coa/ (sha256 0cfe7ac82396)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees: 9648 ⟵ “Tuition & Fees | $9,648 | $9,648 | $9,648”
  - on_campus:Housing & Food: 12700 ⟵ “Housing & Food | $12,700 | $12,700 | $6,448”
  - on_campus:Books & Supplies: 1500 ⟵ “Books & Supplies | $1,500 | $1,500 | $1,500”
  - on_campus:Loan Fee: 100 ⟵ “Loan Fee | $100 | $100 | $100”
  - on_campus:Personal: 1500 ⟵ “Personal | $1,500 | $1,500 | $1,500”
  - on_campus:Transportation: 2000 ⟵ “Transportation | $2,000 | $2,000 | $2,000”
  - on_campus:Total: 27448 ⟵ “Total | $27,448 | $27,448 | $21,196”
  - off_campus_not_with_family:Tuition & Fees: 9648 ⟵ “Tuition & Fees | $9,648 | $9,648 | $9,648”
  - off_campus_not_with_family:Housing & Food: 12700 ⟵ “Housing & Food | $12,700 | $12,700 | $6,448”
  - off_campus_not_with_family:Books & Supplies: 1500 ⟵ “Books & Supplies | $1,500 | $1,500 | $1,500”
  - off_campus_not_with_family:Loan Fee: 100 ⟵ “Loan Fee | $100 | $100 | $100”
  - off_campus_not_with_family:Personal: 1500 ⟵ “Personal | $1,500 | $1,500 | $1,500”
  - off_campus_not_with_family:Transportation: 2000 ⟵ “Transportation | $2,000 | $2,000 | $2,000”
  - off_campus_not_with_family:Total: 27448 ⟵ “Total | $27,448 | $27,448 | $21,196”
  - with_parents_or_family:Tuition & Fees: 9648 ⟵ “Tuition & Fees | $9,648 | $9,648 | $9,648”
  - with_parents_or_family:Housing & Food: 6448 ⟵ “Housing & Food | $12,700 | $12,700 | $6,448”
  - with_parents_or_family:Books & Supplies: 1500 ⟵ “Books & Supplies | $1,500 | $1,500 | $1,500”
  - with_parents_or_family:Loan Fee: 100 ⟵ “Loan Fee | $100 | $100 | $100”
  - with_parents_or_family:Personal: 1500 ⟵ “Personal | $1,500 | $1,500 | $1,500”
  - with_parents_or_family:Transportation: 2000 ⟵ “Transportation | $2,000 | $2,000 | $2,000”
  - with_parents_or_family:Total: 21196 ⟵ “Total | $27,448 | $27,448 | $21,196”
### `b6567a403262b736` Bluefield State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://bluefieldstate.edu/financial-aid/coa/ (sha256 0cfe7ac82396)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition & Fees: 13032 ⟵ “Tuition & Fees | $13,032 | $13,032 | $13,032”
  - on_campus:Housing & Food: 12700 ⟵ “Housing & Food | $12,700 | $12,700 | $6,448”
  - on_campus:Books & Supplies: 1500 ⟵ “Books & Supplies | $1,500 | $1,500 | $1,500”
  - on_campus:Loan Fee: 100 ⟵ “Loan Fee | $100 | $100 | $100”
  - on_campus:Personal: 1500 ⟵ “Personal | $1,500 | $1,500 | $1,500”
  - on_campus:Transportation: 2000 ⟵ “Transportation | $2,000 | $2,000 | $2,000”
  - on_campus:Total: 30832 ⟵ “Total | $30,832 | $30,832 | $24,580”
  - off_campus_not_with_family:Tuition & Fees: 13032 ⟵ “Tuition & Fees | $13,032 | $13,032 | $13,032”
  - off_campus_not_with_family:Housing & Food: 12700 ⟵ “Housing & Food | $12,700 | $12,700 | $6,448”
  - off_campus_not_with_family:Books & Supplies: 1500 ⟵ “Books & Supplies | $1,500 | $1,500 | $1,500”
  - off_campus_not_with_family:Loan Fee: 100 ⟵ “Loan Fee | $100 | $100 | $100”
  - off_campus_not_with_family:Personal: 1500 ⟵ “Personal | $1,500 | $1,500 | $1,500”
  - off_campus_not_with_family:Transportation: 2000 ⟵ “Transportation | $2,000 | $2,000 | $2,000”
  - off_campus_not_with_family:Total: 30832 ⟵ “Total | $30,832 | $30,832 | $24,580”
  - with_parents_or_family:Tuition & Fees: 13032 ⟵ “Tuition & Fees | $13,032 | $13,032 | $13,032”
  - with_parents_or_family:Housing & Food: 6448 ⟵ “Housing & Food | $12,700 | $12,700 | $6,448”
  - with_parents_or_family:Books & Supplies: 1500 ⟵ “Books & Supplies | $1,500 | $1,500 | $1,500”
  - with_parents_or_family:Loan Fee: 100 ⟵ “Loan Fee | $100 | $100 | $100”
  - with_parents_or_family:Personal: 1500 ⟵ “Personal | $1,500 | $1,500 | $1,500”
  - with_parents_or_family:Transportation: 2000 ⟵ “Transportation | $2,000 | $2,000 | $2,000”
  - with_parents_or_family:Total: 24580 ⟵ “Total | $30,832 | $30,832 | $24,580”
### `ec1401d06c5fa21c` BridgeValley Community & Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.bridgevalley.edu/financial-aid/cost-of-Attendance.html (sha256 ac14ad5a1a3b)
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition & Fees: 11318.4 ⟵ “Tuition & Fees | $4,800 | $4,800 | $11,318.40”
  - off_campus_not_with_family:Books & Supplies: 1776 ⟵ “Books & Supplies | $1,776 | $1,776 | $1,776”
  - off_campus_not_with_family:Housing & Food: 9817 ⟵ “Housing & Food | $9,817 | $5,890 | $9,817”
  - off_campus_not_with_family:Transportation: 3404 ⟵ “Transportation | $3,404 | $3,404 | $3,404”
  - off_campus_not_with_family:Personal Expenses: 1524 ⟵ “Personal Expenses | $1,524 | $1,294 | $1,524”
  - off_campus_not_with_family:Total Estimated COA: 27839.4 ⟵ “Total Estimated COA | $21,321 | $17,164 | $27,839.40”
### `16a1601b82e46809` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": null}
  - gpa_requirement: GPA Range: 3.0-3.49 ⟵ “3.0-3.49 | $2,000 Transfer | 2.5 GPA and 24 earned credit hours”
  - award_amount_text: $2,000 Transfer ⟵ “3.0-3.49 | $2,000 Transfer | 2.5 GPA and 24 earned credit hours”
  - renewal_requirements: 2.5 GPA and 24 earned credit hours ⟵ “3.0-3.49 | $2,000 Transfer | 2.5 GPA and 24 earned credit hours”
### `1e892205607a7b0c` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 Maroon & Gray ⟵ “Tier 5 | 3.0-3.24 | $1,500 Maroon & Gray | 2.5 GPA and 24 earned credit hours”
  - gpa_requirement: 3.0-3.24 ⟵ “Tier 5 | 3.0-3.24 | $1,500 Maroon & Gray | 2.5 GPA and 24 earned credit hours”
  - renewal_requirements: 2.5 GPA and 24 earned credit hours ⟵ “Tier 5 | 3.0-3.24 | $1,500 Maroon & Gray | 2.5 GPA and 24 earned credit hours”
### `238aea5aeffe6235` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": null}
  - award_amount_text: $2,500 Academic Excellence ⟵ “Tier 3 | 3.5-3.74 | $2,500 Academic Excellence | 2.5 GPA and 24 earned credit hours”
  - gpa_requirement: 3.5-3.74 ⟵ “Tier 3 | 3.5-3.74 | $2,500 Academic Excellence | 2.5 GPA and 24 earned credit hours”
  - renewal_requirements: 2.5 GPA and 24 earned credit hours ⟵ “Tier 3 | 3.5-3.74 | $2,500 Academic Excellence | 2.5 GPA and 24 earned credit hours”
### `523b67bdf5c8d711` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 Academic Achievement ⟵ “Tier 4 | 3.25-3.49 | $2,000 Academic Achievement | 2.5 GPA and 24 earned credit hours”
  - gpa_requirement: 3.25-3.49 ⟵ “Tier 4 | 3.25-3.49 | $2,000 Academic Achievement | 2.5 GPA and 24 earned credit hours”
  - renewal_requirements: 2.5 GPA and 24 earned credit hours ⟵ “Tier 4 | 3.25-3.49 | $2,000 Academic Achievement | 2.5 GPA and 24 earned credit hours”
### `5f9f0671db021fb1` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 Board of Governors ⟵ “Tier 2 | 3.75-3.89 | $3,000 Board of Governors | 2.5 GPA and 24 earned credit hours”
  - gpa_requirement: 3.75-3.89 ⟵ “Tier 2 | 3.75-3.89 | $3,000 Board of Governors | 2.5 GPA and 24 earned credit hours”
  - renewal_requirements: 2.5 GPA and 24 earned credit hours ⟵ “Tier 2 | 3.75-3.89 | $3,000 Board of Governors | 2.5 GPA and 24 earned credit hours”
### `62ac9cb08af339f2` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - award_amount_text: Tuition, $6,000 towards Room & Board ⟵ “Dean’s** | 3.5 | SAT 1240 /ACT 26 | Tuition, $6,000 towards Room & Board | 2.75 GPA and 24 earned credit hours”
  - gpa_requirement: 3.5 ⟵ “Dean’s** | 3.5 | SAT 1240 /ACT 26 | Tuition, $6,000 towards Room & Board | 2.75 GPA and 24 earned credit hours”
  - test_requirement: SAT 1240 /ACT 26 ⟵ “Dean’s** | 3.5 | SAT 1240 /ACT 26 | Tuition, $6,000 towards Room & Board | 2.75 GPA and 24 earned credit hours”
  - renewal_requirements: 2.75 GPA and 24 earned credit hours ⟵ “Dean’s** | 3.5 | SAT 1240 /ACT 26 | Tuition, $6,000 towards Room & Board | 2.75 GPA and 24 earned credit hours”
### `80a55db62379621d` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": null}
  - gpa_requirement: GPA Range: 2.75-2.99 ⟵ “2.75-2.99 | $1,000 Transfer | 2.5 GPA and 24 earned credit hours”
  - award_amount_text: $1,000 Transfer ⟵ “2.75-2.99 | $1,000 Transfer | 2.5 GPA and 24 earned credit hours”
  - renewal_requirements: 2.5 GPA and 24 earned credit hours ⟵ “2.75-2.99 | $1,000 Transfer | 2.5 GPA and 24 earned credit hours”
### `9f93bc8343912af2` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": {"gpa_min": 3.9}}
  - award_amount_text: $3,500 Joseph Marsh ⟵ “Tier 1 | 3.9+ | $3,500 Joseph Marsh | 2.5 GPA and 24 earned credit hours”
  - gpa_requirement: 3.9+ ⟵ “Tier 1 | 3.9+ | $3,500 Joseph Marsh | 2.5 GPA and 24 earned credit hours”
  - renewal_requirements: 2.5 GPA and 24 earned credit hours ⟵ “Tier 1 | 3.9+ | $3,500 Joseph Marsh | 2.5 GPA and 24 earned credit hours”
### `dc710fa418c4cb95` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": {"gpa_min": 3.75}}
  - award_amount_text: Tuition & Room & Board ⟵ “Presidential** | 3.75 | SAT 1360 /ACT 30 | Tuition & Room & Board | 2.75 GPA and 24 earned credit hours”
  - gpa_requirement: 3.75 ⟵ “Presidential** | 3.75 | SAT 1360 /ACT 30 | Tuition & Room & Board | 2.75 GPA and 24 earned credit hours”
  - test_requirement: SAT 1360 /ACT 30 ⟵ “Presidential** | 3.75 | SAT 1360 /ACT 30 | Tuition & Room & Board | 2.75 GPA and 24 earned credit hours”
  - renewal_requirements: 2.75 GPA and 24 earned credit hours ⟵ “Presidential** | 3.75 | SAT 1360 /ACT 30 | Tuition & Room & Board | 2.75 GPA and 24 earned credit hours”
### `fe504a5807f3da48` Concord University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/scholarships-programs/ (sha256 469974995198)
- checks: {"thresholds": null}
  - gpa_requirement: GPA Range: 3.5+ ⟵ “3.5+ | $2,500 Transfer | 2.5 GPA and 24 earned credit hours”
  - award_amount_text: $2,500 Transfer ⟵ “3.5+ | $2,500 Transfer | 2.5 GPA and 24 earned credit hours”
  - renewal_requirements: 2.5 GPA and 24 earned credit hours ⟵ “3.5+ | $2,500 Transfer | 2.5 GPA and 24 earned credit hours”
### `652afe22a6009fab` Concord University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/tuition-fees (sha256 896d718e2fd0)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 21424 ⟵ “Tuition | $9,748 | $21,424 | $17,424”
  - column:Additional Class Fees: 1440 ⟵ “Additional Class Fees | $1,440 | $1,440 | $1,440”
  - column:Housing (double occupancy)*: 6246 ⟵ “Housing (double occupancy)* | $6,246 | $6,246 | $6,246”
  - column:Food (all access meal plan): 6132 ⟵ “Food (all access meal plan) | $6,132 | $6,132 | $6,132”
  - column:Total: 35242 ⟵ “Total | $23,566 | $35,242 | $31,242”
### `788af96f964dc77d` Concord University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/tuition-fees (sha256 896d718e2fd0)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 9748 ⟵ “Tuition | $9,748 | $21,424 | $17,424”
  - column:Additional Class Fees: 1440 ⟵ “Additional Class Fees | $1,440 | $1,440 | $1,440”
  - column:Housing (double occupancy)*: 6246 ⟵ “Housing (double occupancy)* | $6,246 | $6,246 | $6,246”
  - column:Food (all access meal plan): 6132 ⟵ “Food (all access meal plan) | $6,132 | $6,132 | $6,132”
  - column:Total: 23566 ⟵ “Total | $23,566 | $35,242 | $31,242”
### `ddda31966454a03b` Concord University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.concord.edu/admissions/transfer-students (sha256 e704f251dac5)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transferable courses must be college-level, be taken at a regionally accredited college or university, and have a grade of C or higher.”
### `m9dd248947f741f9` Davis & Elkins College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.dewv.edu/new-students/transfer/ (sha256 62195d2dde14)
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 62 ⟵ “Transfer Credit Limits Maximum of 62 semester credit hours from an accredited community college may be transferred Access the Tranfer Credit Form Articulation Agreements D&E has established formal articulation (2+2) agreements with the following West Virginia community and technical colleges to provide transfer students with clear pathways to D&E bachelor’s degrees.”
  - max_transfer_credits: 62 ⟵ “Transfer Credit Limits Maximum of 62 semester credit hours from an accredited community college may be transferred Access the Tranfer Credit Form Articulation Agreements D&E has established formal articulation (2+2) agreements with the following West Virginia community and technical colleges to provide transfer students with clear pathways to D&E bachelor’s degrees.”
### `a646a2ecef578202` Fairmont State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.fairmontstate.edu/financial-aid/cost-attendance.aspx (sha256 3289a94158f9)
- checks: {"columns": 3, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition & Mandatory Fees: 9080 ⟵ “Tuition & Mandatory Fees | $9,080 | $9,080 | $9,080”
  - on_campus:Educational Fees: 1160 ⟵ “Educational Fees | $1,160 | $1,160 | $1,160”
  - on_campus:Housing & Food: 12645 ⟵ “Housing & Food | $12,645 | Indirect Cost | Indirect Cost”
  - on_campus:Total Estimated Direct Costs: 22885 ⟵ “Total Estimated Direct Costs | $22,885 | $10,240 | $10,240”
  - off_campus_not_with_family:Tuition & Mandatory Fees: 9080 ⟵ “Tuition & Mandatory Fees | $9,080 | $9,080 | $9,080”
  - off_campus_not_with_family:Educational Fees: 1160 ⟵ “Educational Fees | $1,160 | $1,160 | $1,160”
  - off_campus_not_with_family:Total Estimated Direct Costs: 10240 ⟵ “Total Estimated Direct Costs | $22,885 | $10,240 | $10,240”
  - with_parents_or_family:Tuition & Mandatory Fees: 9080 ⟵ “Tuition & Mandatory Fees | $9,080 | $9,080 | $9,080”
  - with_parents_or_family:Educational Fees: 1160 ⟵ “Educational Fees | $1,160 | $1,160 | $1,160”
  - with_parents_or_family:Total Estimated Direct Costs: 10240 ⟵ “Total Estimated Direct Costs | $22,885 | $10,240 | $10,240”
### `103784cefcea9b44` Marshall University — credit_policies 2026-27 · policy_kind=CLEP [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/admissions/ (sha256 b02cc5043c21)
- checks: {"distinct_exams": 13, "equivalencies": 13, "rows_without_score": 0}
  - equivalencies[CLEP-PRECALCULUS|50]:  ⟵ “Precalculus | 50 | MTH 132 | 5”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology, General | 50 | BSC 104-BSC 105, BSC 104L, BSC 105L | 8”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus w/ elem. Functions | 50 | MTH 229 | 5”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry, General | 50 | CHM 211-CHM 212 | 6”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Macroeconomics, Principles of | 50 | ECN 253 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50]:  ⟵ “Management, Principles of | 50 | MGT 320 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50]:  ⟵ “Marketing, Principles of | 50 | MKT 340 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Microeconomics, Principles of | 50 | ECN 250 | 3”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Psychology, Introductory | 50 | PSY 201 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Sociology, Introductory | 50 | SOC 200 | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MTH 121, MTH 160 | 8”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | Unclassified elective | 6”
  - equivalencies[CLEP-SOCIAL-SCIENCES-HISTORY|50]:  ⟵ “Social Sciences and History | 50 | Unclassified elective | 6”
### `4c17ecdad30b2cb6` Marshall University — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/admissions/ (sha256 b02cc5043c21)
- checks: {"distinct_exams": 35, "equivalencies": 55, "rows_without_score": 0}
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design | 3 | ART 214 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design | 3 | ART 215 | 3”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing | 3 | ART 217 | 3”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ART 112 or ART 101 | 3”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory | 3 | MUSP 101 | 3”
  - equivalencies[AP-MUSIC-THEORY|4]:  ⟵ “Music Theory | 4 | MUSP 101, MUSP 111 | 5”
  - equivalencies[AP-MUSIC-THEORY|5]:  ⟵ “Music Theory | 5 | MUSP 111, MUSP 112, MUSP 113 | 6”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition | 3 | ENG 101 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language & Composition | 4 | ENG 101 and ENG 201 | 6”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition | 3 | ENG 231 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|4]:  ⟵ “English Literature & Composition | 4 | ENG 231 and ENG 213 | 6”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3]:  ⟵ “Business with Personal Finance | 3 | FIN 175 | 3”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | 3 | PSC 207 | 3”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “United States Government and Politics | 3 | PSC 104 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|3]:  ⟵ “History, United States History | 3 | HST 230 and HST 231 | 6”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEO 100 | 3”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics | 3 | ECN 253 | 3”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics | 3 | ECN 250 | 3”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSY 201 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A | 3 | CS 105 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 | CS 105 and CS 110 | 6”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles | 3 | CS 105 | 3”
  - equivalencies[AP-CYBERSECURITY|3]:  ⟵ “Cybersecurity | 3 | CFS 200 | 3”
  - equivalencies[AP-CYBERSECURITY|4]:  ⟵ “Cybersecurity | 4 | CFS 200, CFS 261 | 6”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Mathematics, Calculus AB | 3 | MTH 132 | 5”
  - … 30 more rows
### `4f43d54b19fca668` Marshall University — transfer_policies 2026-27 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/admissions/ (sha256 b02cc5043c21)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer credit equivalent to ENG 101 from an accepted, accredited institution with grade of C or better.”
### `4701e5232c4d2a3d` Mountwest Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.mctc.edu/paying-for-college/ (sha256 b750de976b45)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Books & Supplies: 1570 ⟵ “Books & Supplies | 1,570 | 1,570 | 1,570 | 1,570 | 1,570”
  - with_parents_or_family:Average Loan Fee: 36 ⟵ “Average Loan Fee | 36 | 36 | 36 | 36 | 36”
  - with_parents_or_family:Misc./Personal Expenses: 1330 ⟵ “Misc./Personal Expenses | 1,330 | 1,565 | 1,330 | 1,565 | 1,565”
  - with_parents_or_family:Housing & Food: 6118 ⟵ “Housing & Food | 6,118 | 10,197 | 6,118 | 10,197 | 10,197”
  - with_parents_or_family:Average Tuition & Fees: 6436 ⟵ “Average Tuition & Fees | 6,436 | 6,436 | 10,700 | 10,700 | 13,720”
  - with_parents_or_family:Transportation: 3219 ⟵ “Transportation | 3,219 | 3,219 | 3,219 | 3,219 | 3,219”
  - with_parents_or_family:Total: 18709 ⟵ “Total | 18,709 | 23,023 | 22,973 | 27,287 | 30,307”
  - off_campus_not_with_family:Books & Supplies: 1570 ⟵ “Books & Supplies | 1,570 | 1,570 | 1,570 | 1,570 | 1,570”
  - off_campus_not_with_family:Average Loan Fee: 36 ⟵ “Average Loan Fee | 36 | 36 | 36 | 36 | 36”
  - off_campus_not_with_family:Misc./Personal Expenses: 1565 ⟵ “Misc./Personal Expenses | 1,330 | 1,565 | 1,330 | 1,565 | 1,565”
  - off_campus_not_with_family:Housing & Food: 10197 ⟵ “Housing & Food | 6,118 | 10,197 | 6,118 | 10,197 | 10,197”
  - off_campus_not_with_family:Average Tuition & Fees: 6436 ⟵ “Average Tuition & Fees | 6,436 | 6,436 | 10,700 | 10,700 | 13,720”
  - off_campus_not_with_family:Transportation: 3219 ⟵ “Transportation | 3,219 | 3,219 | 3,219 | 3,219 | 3,219”
  - off_campus_not_with_family:Total: 23023 ⟵ “Total | 18,709 | 23,023 | 22,973 | 27,287 | 30,307”
### `4d35e98cf65365d3` Mountwest Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.mctc.edu/paying-for-college/ (sha256 b750de976b45)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Books & Supplies: 1570 ⟵ “Books & Supplies | 1,570 | 1,570 | 1,570 | 1,570 | 1,570”
  - off_campus_not_with_family:Average Loan Fee: 36 ⟵ “Average Loan Fee | 36 | 36 | 36 | 36 | 36”
  - off_campus_not_with_family:Misc./Personal Expenses: 1565 ⟵ “Misc./Personal Expenses | 1,330 | 1,565 | 1,330 | 1,565 | 1,565”
  - off_campus_not_with_family:Housing & Food: 10197 ⟵ “Housing & Food | 6,118 | 10,197 | 6,118 | 10,197 | 10,197”
  - off_campus_not_with_family:Average Tuition & Fees: 13720 ⟵ “Average Tuition & Fees | 6,436 | 6,436 | 10,700 | 10,700 | 13,720”
  - off_campus_not_with_family:Transportation: 3219 ⟵ “Transportation | 3,219 | 3,219 | 3,219 | 3,219 | 3,219”
  - off_campus_not_with_family:Total: 30307 ⟵ “Total | 18,709 | 23,023 | 22,973 | 27,287 | 30,307”
### `01ad78d463299546` Mountwest Community and Technical College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.mctc.edu/admissions/ (sha256 742c2d30f8db)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Courses in which a grade of “C” or higher is earned are transferable for credit if coursework is relevant to the student’s program at Mountwest Community and Technical College with the approval of the Division Dean.”
### `14c5a0751b0a81ee` Shepherd University — credit_policies 2026-27 · policy_kind=dual_enrollment [new] (source_unlabeled)
- source: https://www.shepherd.edu/apply-for-dual-enrollment/ (sha256 279e8a74b963)
- checks: {"fields": ["min_hs_gpa"], "tiers": 1}
  - eligibility_tier: 3.0 ⟵ “TRANSCRIPT: A copy of your high school or homeschool transcript indicating an overall GPA of 3.0 or higher.”
### `6ffea19032e5fbaa` Shepherd University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.shepherd.edu/admissions/ap-and-ib-credits/ (sha256 69d0a2d9ab8d)
- checks: {"distinct_exams": 13, "equivalencies": 15, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5, 6, 7]:  ⟵ “Biology | 5, 6, 7 | BIOL 101, BIOL 102 | 8”
  - equivalencies[IB-CHEMISTRY|5, 6, 7]:  ⟵ “Chemistry | 5, 6, 7 | CHEM 207, CHEM 207L, CHEM 209, CHEM 209L | 8”
  - equivalencies[IB-COMPUTER-SCIENCE|5, 6, 7]:  ⟵ “Computer Science | 5, 6, 7 | CIS 211, CIS 314 | 8”
  - equivalencies[IB-ECONOMICS|5, 6, 7]:  ⟵ “Economics | 5, 6, 7 | ECON 205, ECON 206 | 6”
  - equivalencies[IB-FRENCH|5, 6, 7]:  ⟵ “French B | 5, 6, 7 | FREN 101, FREN 102 | 6”
  - equivalencies[IB-GEOGRAPHY|5, 6, 7]:  ⟵ “Geography | 5, 6, 7 | GEOG 101, GEOG elective | 6”
  - equivalencies[IB-GERMAN|5, 6, 7]:  ⟵ “German B | 5, 6, 7 | GERM 101, GERM 102 | 6”
  - equivalencies[IB-HISTORY|5, 6, 7]:  ⟵ “History (America) | 5, 6, 7 | HIST 201, HIST 202 | 6”
  - equivalencies[IB-HISTORY|5, 6, 7]:  ⟵ “History (Africa) | 5, 6, 7 | HIST 320, HIST elective | 6”
  - equivalencies[IB-HISTORY|5, 6, 7]:  ⟵ “History (Europe) | 5, 6, 7 | HIST 102, HIST 103 | 6”
  - equivalencies[IB-PHILOSOPHY|5, 6, 7]:  ⟵ “Philosophy | 5, 6, 7 | PHIL 101, PHIL 305 | 6”
  - equivalencies[IB-PHYSICS|5, 6, 7]:  ⟵ “Physics | 5, 6, 7 | PHYS 201, PHYS 201L, PHYS 202, PHYS 202L | 8”
  - equivalencies[IB-PSYCHOLOGY|5, 6, 7]:  ⟵ “Psychology | 5, 6, 7 | PSYC 203, PSYC elective | 6”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|5, 6, 7]:  ⟵ “Social Anthropology | 5, 6, 7 | ANTH 315, ANTH elective | 6”
  - equivalencies[IB-SPANISH|5, 6, 7]:  ⟵ “Spanish | 5, 6, 7 | SPAN 101, SPAN 102 | 6”
### `fa7efca8f67cfd32` University of Charleston — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.ucwv.edu/admissions/transfer-students/ (sha256 8d64c63b5a40)
- checks: {"fields": ["min_grade"]}
  - min_grade: D ⟵ “Only courses with earned grades of “D” or better will transfer.”
  - min_grade: D ⟵ “College-level courses (typically 100-level and higher) passed with a grade of “D” or better are reviewed for transfer credit.”
### `c32263e194d56b24` West Liberty University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://westliberty.edu/business-office/tuition-fees/undergraduate-tuition/ (sha256 9784cf020928)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 9414 ⟵ “Tuition & Fees | $9,414 | $9,414 | $9,414”
  - with_parents_or_family:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - with_parents_or_family:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - with_parents_or_family:Personal Expenses: 965 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - with_parents_or_family:Transportation Expenses: 2961 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - with_parents_or_family:Federal Student Loan Fees: 78 ⟵ “Federal Student Loan Fees | $78 | $78 | $78”
  - with_parents_or_family:TOTAL: 29428 ⟵ “TOTAL | $29,428 | $30,036 | $29,346”
  - off_campus_not_with_family:Tuition & Fees: 9414 ⟵ “Tuition & Fees | $9,414 | $9,414 | $9,414”
  - off_campus_not_with_family:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - off_campus_not_with_family:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - off_campus_not_with_family:Personal Expenses: 1573 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - off_campus_not_with_family:Transportation Expenses: 2961 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - off_campus_not_with_family:Federal Student Loan Fees: 78 ⟵ “Federal Student Loan Fees | $78 | $78 | $78”
  - off_campus_not_with_family:TOTAL: 30036 ⟵ “TOTAL | $29,428 | $30,036 | $29,346”
  - on_campus:Tuition & Fees: 9414 ⟵ “Tuition & Fees | $9,414 | $9,414 | $9,414”
  - on_campus:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - on_campus:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - on_campus:Personal Expenses: 1573 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - on_campus:Transportation Expenses: 2271 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - on_campus:Federal Student Loan Fees: 78 ⟵ “Federal Student Loan Fees | $78 | $78 | $78”
  - on_campus:TOTAL: 29346 ⟵ “TOTAL | $29,428 | $30,036 | $29,346”
### `c73ae1d910a67d84` West Liberty University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://westliberty.edu/business-office/tuition-fees/undergraduate-tuition/ (sha256 455c2ade2c6d)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 18840 ⟵ “Tuition & Fees | $18,840 | $18,840 | $18,840”
  - with_parents_or_family:Food + Housing: 14710 ⟵ “Food + Housing | $14,710 | $14,710 | $14,710”
  - with_parents_or_family:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - with_parents_or_family:Personal Expenses: 965 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - with_parents_or_family:Transportation Expenses: 2961 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - with_parents_or_family:Federal Student Loan Fees: 78 ⟵ “Federal Student Loan Fees | $78 | $78 | $78”
  - with_parents_or_family:TOTAL: 38854 ⟵ “TOTAL | $38,854 | $39,462 | $38,772”
  - off_campus_not_with_family:Tuition & Fees: 18840 ⟵ “Tuition & Fees | $18,840 | $18,840 | $18,840”
  - off_campus_not_with_family:Food + Housing: 14710 ⟵ “Food + Housing | $14,710 | $14,710 | $14,710”
  - off_campus_not_with_family:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - off_campus_not_with_family:Personal Expenses: 1573 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - off_campus_not_with_family:Transportation Expenses: 2961 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - off_campus_not_with_family:Federal Student Loan Fees: 78 ⟵ “Federal Student Loan Fees | $78 | $78 | $78”
  - off_campus_not_with_family:TOTAL: 39462 ⟵ “TOTAL | $38,854 | $39,462 | $38,772”
  - on_campus:Tuition & Fees: 18840 ⟵ “Tuition & Fees | $18,840 | $18,840 | $18,840”
  - on_campus:Food + Housing: 14710 ⟵ “Food + Housing | $14,710 | $14,710 | $14,710”
  - on_campus:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - on_campus:Personal Expenses: 1573 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - on_campus:Transportation Expenses: 2271 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - on_campus:Federal Student Loan Fees: 78 ⟵ “Federal Student Loan Fees | $78 | $78 | $78”
  - on_campus:TOTAL: 38772 ⟵ “TOTAL | $38,854 | $39,462 | $38,772”
### `1be37fb971264a59` West Virginia State University — awards 2026-27 [new] (source_unlabeled)
- source: https://wvstateu.edu/admissions/financial-aid/scholarships/yellow-jacket-scholarship/ (sha256 0c652b913495)
- checks: {"thresholds": null}
  - award_amount_text: $3300 ⟵ “Tier 2 | 3.5-3.7 | $3300”
  - gpa_requirement: 3.5-3.7 ⟵ “Tier 2 | 3.5-3.7 | $3300”
### `9977053194f9f789` West Virginia State University — awards 2026-27 [new] (source_unlabeled)
- source: https://wvstateu.edu/admissions/financial-aid/scholarships/yellow-jacket-scholarship/ (sha256 0c652b913495)
- checks: {"thresholds": null}
  - award_amount_text: $5000 ⟵ “Tier 3 | 3.8-4.0 | $5000”
  - gpa_requirement: 3.8-4.0 ⟵ “Tier 3 | 3.8-4.0 | $5000”
### `b7bd9fb442ef7cd9` West Virginia State University — awards 2026-27 [new] (source_unlabeled)
- source: https://wvstateu.edu/admissions/financial-aid/scholarships/yellow-jacket-scholarship/ (sha256 0c652b913495)
- checks: {"thresholds": null}
  - award_amount_text: $2200 ⟵ “Tier 1 | 3.0-3.4 | $2200”
  - gpa_requirement: 3.0-3.4 ⟵ “Tier 1 | 3.0-3.4 | $2200”
### `94ddab0a9ac4de3e` West Virginia State University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://wvstateu.edu/admissions/financial-aid/2026-2027-cost-of-attendance/ (sha256 0536d2f7baff)
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 9920 ⟵ “Tuition and Fees | $9,920 | $9,920 | $9,920”
  - with_parents_or_family:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - with_parents_or_family:Housing and Meals: 6510 ⟵ “Housing and Meals | $6,510 | $10,850 | $10,718”
  - with_parents_or_family:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71 | $71”
  - with_parents_or_family:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380 | $1,380”
  - with_parents_or_family:Personal & Miscellaneous: 2430 ⟵ “Personal & Miscellaneous | $2,430 | $2,430 | $2,430”
  - with_parents_or_family:Total Estimated Expenses: 21641 ⟵ “Total Estimated Expenses | $21,641 | $25,981 | $25,849”
  - off_campus_not_with_family:Tuition and Fees: 9920 ⟵ “Tuition and Fees | $9,920 | $9,920 | $9,920”
  - off_campus_not_with_family:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - off_campus_not_with_family:Housing and Meals: 10850 ⟵ “Housing and Meals | $6,510 | $10,850 | $10,718”
  - off_campus_not_with_family:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71 | $71”
  - off_campus_not_with_family:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380 | $1,380”
  - off_campus_not_with_family:Personal & Miscellaneous: 2430 ⟵ “Personal & Miscellaneous | $2,430 | $2,430 | $2,430”
  - off_campus_not_with_family:Total Estimated Expenses: 25981 ⟵ “Total Estimated Expenses | $21,641 | $25,981 | $25,849”
  - on_campus:Tuition and Fees: 9920 ⟵ “Tuition and Fees | $9,920 | $9,920 | $9,920”
  - on_campus:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - on_campus:Housing and Meals: 10718 ⟵ “Housing and Meals | $6,510 | $10,850 | $10,718”
  - on_campus:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71 | $71”
  - on_campus:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380 | $1,380”
  - on_campus:Personal & Miscellaneous: 2430 ⟵ “Personal & Miscellaneous | $2,430 | $2,430 | $2,430”
  - on_campus:Total Estimated Expenses: 25849 ⟵ “Total Estimated Expenses | $21,641 | $25,981 | $25,849”
### `fd20590495949b76` West Virginia State University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://wvstateu.edu/admissions/financial-aid/2026-2027-cost-of-attendance/ (sha256 0536d2f7baff)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition and Fees: 15560 ⟵ “Tuition and Fees | $15,560 | $15,560”
  - off_campus_not_with_family:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330”
  - off_campus_not_with_family:Housing and Meals: 10850 ⟵ “Housing and Meals | $10,850 | $10,718”
  - off_campus_not_with_family:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71”
  - off_campus_not_with_family:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380”
  - off_campus_not_with_family:Personal & Miscellaneous: 2430 ⟵ “Personal & Miscellaneous | $2,430 | $2,430”
  - off_campus_not_with_family:Total Estimated Expenses: 31621 ⟵ “Total Estimated Expenses | $31,621 | $31,489”
  - on_campus:Tuition and Fees: 15560 ⟵ “Tuition and Fees | $15,560 | $15,560”
  - on_campus:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330”
  - on_campus:Housing and Meals: 10718 ⟵ “Housing and Meals | $10,850 | $10,718”
  - on_campus:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71”
  - on_campus:Transportation: 1380 ⟵ “Transportation | $1,380 | $1,380”
  - on_campus:Personal & Miscellaneous: 2430 ⟵ “Personal & Miscellaneous | $2,430 | $2,430”
  - on_campus:Total Estimated Expenses: 31489 ⟵ “Total Estimated Expenses | $31,621 | $31,489”
### `f4f1799ea156cb85` West Virginia University Institute of Technology — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://admissions.wvutech.edu/apply/type/transfer (sha256 46a4fd90b69b)
- checks: {"fields": ["max_transfer_credits", "residency_requirement_credits"]}
  - max_transfer_credits: 72 ⟵ “Credit Transfer: Info to Know WVU Tech will accept a maximum of 72 semester hours of lower-division credit from two-year community and technical colleges toward a baccalaureate degree.”
  - residency_requirement_credits: 36 ⟵ “In all cases, transfer students will be required to complete at least 36 hours of credit in residence at WVU Tech prior to graduation.”
### `6cb297d26ad7ed3e` West Virginia Wesleyan College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wvwc.edu/financial-aid-scholarships/total-direct-cost/ (sha256 08e05acabd18)
- checks: {"columns": 1, "components_reconcile": true, "rows": 13}
  - column:Tuition: 33304 ⟵ “Tuition | 33,304”
  - column:Housing (average)*: 7396 ⟵ “Housing (average)* | 7,396”
  - column:Food (Unlimited Meal plan): 6480 ⟵ “Food (Unlimited Meal plan) | 6480”
  - column:Student Activity Fee: 100 ⟵ “Student Activity Fee | 100”
  - column:Technology Fee: 394 ⟵ “Technology Fee | 394”
  - column:General Fee: 1024 ⟵ “General Fee | 1024”
  - column:Books/Supplies/Equipment: 1500 ⟵ “Books/Supplies/Equipment | 1500”
  - column:Transportation: 1000 ⟵ “Transportation | 1000”
  - column:Personal Expenses: 2500 ⟵ “Personal Expenses | 2500”
  - column:Loan Fee: 65 ⟵ “Loan Fee | 65”
  - column:TOTAL COST OF ATTENDANCE: 53763 ⟵ “TOTAL COST OF ATTENDANCE | $53,763”
  - column:Total Tuition/Room/Board: 47180 ⟵ “Total Tuition/Room/Board | 47180”
  - column:TOTAL DIRECT COSTS: 48698 ⟵ “TOTAL DIRECT COSTS | $48,698”
### `3804990861c1d542` West Virginia Wesleyan College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.wvwc.edu/wp-content/uploads/2026/06/Transfer-Credit-Info-Guide-6.24.26.pdf (sha256 0d964f2717aa)
- checks: {"fields": ["max_transfer_credits", "residency_requirement_credits"]}
  - max_transfer_credits: 60 ⟵ “All work and grades are transferred in and count in GPA, but a maximum of 60 hours from 2-year schools and 90 hours from 4-year schools count in earned hours (a maximum of 90 earned hours may be transferred). 3.”
  - residency_requirement_credits: 24 ⟵ “A minimum of 30 hours must be completed in residence at WVWC; 24 of the final 30 must be completed through WVWC. 3.”
### `md1938e6acd9cbf8` Wheeling University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://wheeling.edu/admissions/undergraduate/ (sha256 3ab99d0f4446)
- checks: {"fields": ["min_grade"], "merged_pages": 2}
  - min_grade: C- ⟵ “Transfer credit is only awarded for course work completed at accredited institutions in which a grade of grade of C- or higher is earned.”
  - min_grade: C- ⟵ “Transfer credit is only awarded for course work completed at accredited institutions in which a student earned a grade of C- or higher.”

## Exceptions (295)

### `136cf6c33a03e5f8` Bluefield State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://bluefieldstate.edu/professional-judgment-appeal/ (sha256 12e8bd643a2c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Other unusual circumstances Supporting documentation as requested by the Office of Financial Aid Year Student Name(Required) Student ID(Required) Parent(s) Name(Required) Bluefield State University recognizes that families experience special circumstances which merit recalculation of their financial aid eligibility based on this year’s information, rather than 2024 income information.”
  - sentence: need_based_special_circumstances ⟵ “Additional Children in College Other unusual circumstances HOUSEHOLD SIZE (Number of people supported by household income)(Required) Statement of Projected 2026 Income This section asks about income and benefits that you and your family expect to receive between January 1, 2026 and now.”
### `7c0fb92ad818dd5c` Bluefield State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://bluefieldstate.edu/professional-judgment-appeal/ (sha256 12e8bd643a2c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Please be advised that all professional judgment appeal decisions are final.”
### `7f973f855f96d56c` Bluefield State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://bluefieldstate.edu/professional-judgment-appeal/ (sha256 12e8bd643a2c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Documentation of 2025 year-to-date income Death of a parent (or spouse) which occurred after completing FAFSA Copy of death certificate Documentation of 2025 year-to-date income (taxable and non-taxable) Cost of attendance adjustment Supporting documentation of additional educational expense incurred Additional Children in College Supporting documentation of at least ½ time enrollment at a Title I”
  - sentence: budget_increase ⟵ “Please check the box beside the circumstances that apply to your situation and submit the necessary paperwork.(Required) Separation from employment due to layoff, termination, or disability Excessive non-reimbursed medical and/or dental expenses Loss or reduction of untaxed income source (disability benefits, welfare benefits, child support, etc.) Separation or Divorce which occurred after complet”
### `ea465fb685b96a8f` BridgeValley Community & Technical College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.bridgevalley.edu/financial-aid/financial-aid-appeals.html (sha256 72ea60cf14fa)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Request to Appeal Satisfactory Academic Progress Suspension Appeals may be decided by the Director of Financial Aid or their designated representative in Financial Aid.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress standing can be appealed when one of the following conditions exists: Illness or injury of the student Illness, injury, or death of a family member Natural Disasters i.e.: floods, fires, tornadoes, hurricanes, or earthquakes Criminal acts inflicted on the student or student’s family.”
### `ded3a8972b5f7c6b` BridgeValley Community & Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.bridgevalley.edu/financial-aid/cost-of-Attendance.html (sha256 ac14ad5a1a3b)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - off_campus_not_with_family:Tuition & Fees: 4800 ⟵ “Tuition & Fees | $4,800 | $4,800 | $11,318.40”
  - off_campus_not_with_family:Books & Supplies: 1776 ⟵ “Books & Supplies | $1,776 | $1,776 | $1,776”
  - off_campus_not_with_family:Housing & Food: 9817 ⟵ “Housing & Food | $9,817 | $5,890 | $9,817”
  - off_campus_not_with_family:Transportation: 3404 ⟵ “Transportation | $3,404 | $3,404 | $3,404”
  - off_campus_not_with_family:Personal Expenses: 1524 ⟵ “Personal Expenses | $1,524 | $1,294 | $1,524”
  - off_campus_not_with_family:Total Estimated COA: 21321 ⟵ “Total Estimated COA | $21,321 | $17,164 | $27,839.40”
  - with_parents_or_family:Tuition & Fees: 4800 ⟵ “Tuition & Fees | $4,800 | $4,800 | $11,318.40”
  - with_parents_or_family:Books & Supplies: 1776 ⟵ “Books & Supplies | $1,776 | $1,776 | $1,776”
  - with_parents_or_family:Housing & Food: 5890 ⟵ “Housing & Food | $9,817 | $5,890 | $9,817”
  - with_parents_or_family:Transportation: 3404 ⟵ “Transportation | $3,404 | $3,404 | $3,404”
  - with_parents_or_family:Personal Expenses: 1294 ⟵ “Personal Expenses | $1,524 | $1,294 | $1,524”
  - with_parents_or_family:Total Estimated COA: 17164 ⟵ “Total Estimated COA | $21,321 | $17,164 | $27,839.40”
### `207b6832e30d2eca` Concord University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.concord.edu/financial-aid/professional-judgment-process-appeals (sha256 cc0733a8c47c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Department of Education has provided guidance regarding situations that that do not merit a dependency override.”
### `2e71ba5f6f35ea39` Concord University — appeals 2019-20 [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/cares-act (sha256 6ae44af75bf7)
- issues: stale_year_label:2019-20, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Number of CARES Act Grants awarded per reporting date | Total number of students awarded | Total amount awarded | Reporting Date | 292 | $265,750 | May 10, 2020 | 735 | $648,250 | June 24, 2020 | 735 | $648,250 | August 8, 2020 | 854 | $755,750 | September 30, 2020 | 989 | $1,028,718 | December 31, 2020 PLEASE NOTE: In addition to the CARES Act Grant application, if you have experienced a signific”
  - sentence: professional_judgment ⟵ “The Professional Judgment form can be found on the Financial Aid forms and resources page.”
  - sentence: professional_judgment ⟵ “If your Expected Family Contribution (EFC) is already $0, a Professional Judgment will not benefit you.”
### `4747851e80114209` Concord University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.concord.edu/financial-aid/satisfactory-academic-progress (sha256 517c545fe1b5)
- issues: semantic_review_required, conflicting_sources:https://www.concord.edu/financial-aid/professional-judgment-process-appeals
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Students may appeal their ineligibility under SAP if they were unable to maintain SAP as a direct result of hardship, injury or illness of the student, death of a relative, or other special circumstance.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances may occur which impact a student’s ability to be successful during an enrollment period.”
  - sentence: need_based_special_circumstances ⟵ “Examples of such unusual circumstances would be death of an immediate family member or legal guardian, personal injury or illness of the student, or other documented circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Documentation such as death certificate/notice, physician’s statement, etc., or other comparable documentation of unusual circumstances will be required.”
  - sentence: need_based_special_circumstances ⟵ “A student who wishes to appeal his/her SAP status based on documented unusual circumstances may do so using the Concord University Appeal Form within the timeframe noted on their suspension letter.”
### `53d746cd99561012` Concord University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.concord.edu/financial-aid/professional-judgment-process-appeals (sha256 cc0733a8c47c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: professional_judgment ⟵ “Professional Judgement can also be utilized to change dependency status and/or cost of attendance.”
  - sentence: professional_judgment ⟵ “If you have a special circumstance, please complete the Professional Judgment Form under APPEALS AND PJ Forms or if you have an unusual circumstance, please complete a Request for Independent Status under OTHER FORMS.”
  - sentence: professional_judgment ⟵ “Professional Judgment decisions are final.”
  - sentence: professional_judgment ⟵ “Congress delegated the authority to make professional judgment adjustments to the data elements on the Free Application for Federal Student Aid (FAFSA) to the college financial aid office and their assigned staff.”
### `e1735377aedf7948` Concord University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.concord.edu/financial-aid/satisfactory-academic-progress (sha256 517c545fe1b5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “SAP Appeal Petition Students ineligible for federal student aid program funding may appeal by completing the SAP appeal petition.”
  - sentence: sap_appeal ⟵ “Completed SAP appeal petitions will be reviewed by the Concord University Appeals Committee.”
### `e361a60be7bc8363` Concord University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.concord.edu/financial-aid/professional-judgment-process-appeals (sha256 cc0733a8c47c)
- issues: semantic_review_required, conflicting_sources:https://www.concord.edu/financial-aid/satisfactory-academic-progress
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Categories of Appeals Special Circumstances: Income Loss/Changes or Excessive Medical Expenses, Post-Secondary Educational Expenses This type of an appeal is most often utilized by students when financial circumstances change, and those changes impact you and/or your family’s ability to contribute to your education.”
  - sentence: need_based_special_circumstances ⟵ “In almost all cases, documentation should originate from a third party with knowledge of the unusual circumstances of the student.”
  - sentence: need_based_special_circumstances ⟵ “If selected for FAFSA verification, and you have a special circumstance, you much complete verification before your appeal can be reviewed.”
### `9ea3551aa6c93157` Concord University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.concord.edu/financial-aid/tuition-fees (sha256 896d718e2fd0)
- issues: residency_unknown
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 17424 ⟵ “Tuition | $9,748 | $21,424 | $17,424”
  - column:Additional Class Fees: 1440 ⟵ “Additional Class Fees | $1,440 | $1,440 | $1,440”
  - column:Housing (double occupancy)*: 6246 ⟵ “Housing (double occupancy)* | $6,246 | $6,246 | $6,246”
  - column:Food (all access meal plan): 6132 ⟵ “Food (all access meal plan) | $6,132 | $6,132 | $6,132”
  - column:Total: 31242 ⟵ “Total | $23,566 | $35,242 | $31,242”
### `35bbe7ec9d3dec6b` Eastern West Virginia Community and Technical College — appeals 2022-23 [new] (labeled_in_source)
- source: https://easternwv.edu/financial-aid/ (sha256 45b3e69f4d96)
- issues: stale_year_label:2022-23, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Special Situations If a student believes they have unusual circumstances that may justify an adjustment to their financial aid eligibility, they should contact the Financial Aid Office.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Request May be used when a family's financial circumstances have changed due to the death of a parent, divorce, separation, or loss of employment.”
### `bd42c2848d573d7c` Eastern West Virginia Community and Technical College — appeals 2022-23 [new] (labeled_in_source)
- source: https://easternwv.edu/financial-aid/ (sha256 45b3e69f4d96)
- issues: stale_year_label:2022-23, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: dependency_override ⟵ “Answering “Yes” to any one of the following will result in a student being considered an independent student for federal student aid programs and the student will not need to contact the Financial Aid Office to make a request for a dependency override: Were you born before Jan. 1, 1999?”
  - sentence: dependency_override ⟵ “Dependency Override Request: Alternative Procedure Students who do not meet the criteria of an Independent Student by answering “Yes” to one of the dependency questions above may make a request for a dependency override by contacting the Financial Aid Office.”
  - sentence: dependency_override ⟵ “You cannot live with your parents and request a dependency override.”
  - sentence: dependency_override ⟵ “The unwillingness of the family to pay or provide information is NOT a valid reason for requesting a dependency override.”
  - sentence: dependency_override ⟵ “You will be asked to provide ALL the following: Dependency Override Form (a meeting with financial aid staff is required to obtain the form) A letter, on letterhead, from clergy, social worker or a counselor indicating why there is an estrangement from parents A letter of explanation of the situation from the student and others familiar with the family circumstances income information.”
### `0c51cb3f7e639be1` Eastern West Virginia Community and Technical College — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_source)
- source: https://easternwv.edu/wp-content/uploads/AdvPlacement-25-26.pdf (sha256 8d24a7ec019b)
- issues: stale_year_label:2025-26, score_scale_mismatch
- checks: {"distinct_exams": 40, "equivalencies": 454, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                               3/ 4/5            3        ART 103”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                              3/4/5             3        MUSC 111”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design                        3/4/5             3        ART 199”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design                        3/4/5             3        ART 299”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                                   3/4/5             3        ART 115”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition            3/4/5               3         ENGL 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition          3/4/5               3         ENGL 102”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics         3/4/5             3        PSCI 199”
  - equivalencies[AP-EUROPEAN-HISTORY|6]:  ⟵ “European History                          3/4/5             6        HIST 199 & HIST 299”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                           3/4/5             3        GEOG 105”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                            3/4/5             3        ECON 205”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                            3/4/5             3        ECON 206”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                3/4/5             3        PSYC 203”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government & Politics                3/4/5             3        PSCI 101”
  - equivalencies[AP-UNITED-STATES-HISTORY|6]:  ⟵ “U.S. History                              3/4/5             6        HIST 201 & HIST 202”
  - equivalencies[AP-WORLD-HISTORY-MODERN|6]:  ⟵ “World History                             3/4/5             6        HIST 101 & HIST 102”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB                               3/4/5             4        MATH 108”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                        3/4/5             3        SDE 194”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles               3/4/5             3        CAS 111”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                                3/4/5             3        MATH 114”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                     3/4/5             3        ENVT 101”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1: Algebra-Based                  3/4/5             4        PHYS 201”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2: Algebra-Based                  3/4/5             4        PHYS 299”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4]:  ⟵ “Physics C: Electricity & Magnetism        3/4/5             4        PHYS 299”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics                      3/4/5             4        PHYS 299”
  - … 429 more rows
### `m4e1a027dc6da0fe` Eastern West Virginia Community and Technical College — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://easternwv.edu/academics/transfer/ (sha256 cdf63bbd930a)
- issues: stale_year_label:2025-26
- checks: {"fields": ["max_transfer_credits"], "merged_pages": 2}
  - max_transfer_credits: 72 ⟵ “In total, at least 64 and no more than 72 hours of credit completed at community colleges or branch colleges in the West Virginia state systems of higher education shall be transferable to any baccalaureate degree-granting institution in the state systems.”
  - max_transfer_credits: 72 ⟵ “In total, at least 64 and no more than 72 hours of credit completed at community colleges or branch colleges in the West Virginia state systems of higher education shall be transferable to any baccalaureate degree-granting institution in the state systems.”
### `00039dedfaccec7b` Fairmont State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.fairmontstate.edu/financial-aid/satisfactory-academic-progress.aspx (sha256 8dc9337e6fc2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of extenuating circumstances are death of immediate family member, injury or illness or other unusual circumstances evaluated by the Office of Financial Aid and Scholarships.”
### `22a81d74988c2618` Fairmont State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.fairmontstate.edu/student-services/student-accounts/tuition-fees-charts.aspx (sha256 af169b25b060)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.fairmontstate.edu/financial-aid/cost-attendance.aspx
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition & Fees: 9080 ⟵ “Tuition & Fees | $9,080 | $13,710”
  - on_campus:Residence Hall(Bryant Place, Double Room): 6710 ⟵ “Residence Hall(Bryant Place, Double Room) | $6,710 | $6,710”
  - on_campus:Meal Plan(Eating Made Easy Plan): 4770 ⟵ “Meal Plan(Eating Made Easy Plan) | $4,770 | $4,770”
  - on_campus:Total: 20560 ⟵ “Total | $20,560 | $25,190”
### `c51380a941555080` Fairmont State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://www.fairmontstate.edu/financial-aid/cost-attendance.aspx (sha256 3289a94158f9)
- issues: stale_year_label:2025-26, conflicting_sources:https://www.fairmontstate.edu/student-services/student-accounts/tuition-fees-charts.aspx
- checks: {"columns": 3, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition & Fees: 8708 ⟵ “Tuition & Fees | $8,708 | $8,708 | $8,708”
  - on_campus:Program & Course Fees: 1080 ⟵ “Program & Course Fees | $1,080 | $1,080 | $1,080”
  - on_campus:Housing & Food: 12434 ⟵ “Housing & Food | $12,434 | Indirect Cost | Indirect Cost”
  - on_campus:Total Estimated Direct Costs: 22222 ⟵ “Total Estimated Direct Costs | $22,222 | $9,788 | $9,788”
  - off_campus_not_with_family:Tuition & Fees: 8708 ⟵ “Tuition & Fees | $8,708 | $8,708 | $8,708”
  - off_campus_not_with_family:Program & Course Fees: 1080 ⟵ “Program & Course Fees | $1,080 | $1,080 | $1,080”
  - off_campus_not_with_family:Total Estimated Direct Costs: 9788 ⟵ “Total Estimated Direct Costs | $22,222 | $9,788 | $9,788”
  - with_parents_or_family:Tuition & Fees: 8708 ⟵ “Tuition & Fees | $8,708 | $8,708 | $8,708”
  - with_parents_or_family:Program & Course Fees: 1080 ⟵ “Program & Course Fees | $1,080 | $1,080 | $1,080”
  - with_parents_or_family:Total Estimated Direct Costs: 9788 ⟵ “Total Estimated Direct Costs | $22,222 | $9,788 | $9,788”
### `d2ef5f9621f656f5` Fairmont State University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.fairmontstate.edu/student-services/student-accounts/tuition-fees-charts.aspx (sha256 af169b25b060)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - on_campus:Tuition & Fees: 13710 ⟵ “Tuition & Fees | $9,080 | $13,710”
  - on_campus:Residence Hall(Bryant Place, Double Room): 6710 ⟵ “Residence Hall(Bryant Place, Double Room) | $6,710 | $6,710”
  - on_campus:Meal Plan(Eating Made Easy Plan): 4770 ⟵ “Meal Plan(Eating Made Easy Plan) | $4,770 | $4,770”
  - on_campus:Total: 25190 ⟵ “Total | $20,560 | $25,190”
### `0403b36865ded940` Marshall University — academic_programs 2026-27 · program_key=biological-science-education-9-adult-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/biological-science-9-adult-ba/ (sha256 9c8eb6e96f70)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 46, "groups": 4, "groups_skipped": 1}
  - program_name: Biological Science Education 9-Adult, B.A. ⟵ “Biological Science Education 9-Adult, B.A. | Marshall University Catalog”
### `0e22a4ee249ce6f0` Marshall University — academic_programs 2026-27 · program_key=special-education-multi-categorical-5-adult-b-a-second-specialization-only [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/multi-categorical-special-education-5-adult-ba/ (sha256 5283f23b41f2)
- issues: stale_year_label:2026-27
- checks: {"courses": 8, "groups": 1, "groups_skipped": 0}
  - program_name: Special Education Multi-Categorical 5-Adult, B.A. (Second Specialization only) ⟵ “Special Education Multi-Categorical 5-Adult, B.A. (Second Specialization only) | Marshall University Catalog”
### `14a810306645f771` Marshall University — academic_programs 2026-27 · program_key=general-science-education-5-adult-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/general-sciences-5-adult-ba/ (sha256 f10930c2ff94)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 41, "groups": 4, "groups_skipped": 1}
  - program_name: General Science Education 5-Adult, B.A. ⟵ “General Science Education 5-Adult, B.A. | Marshall University Catalog”
### `1ff79829aac9f322` Marshall University — academic_programs 2026-27 · program_key=health-care-management-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/health-care-management-bba/ (sha256 11c16303570e)
- issues: stale_year_label:2026-27
- checks: {"courses": 44, "groups": 7, "groups_skipped": 0}
  - program_name: Health Care Management, B.B.A. ⟵ “Health Care Management, B.B.A. | Marshall University Catalog”
### `2ea7f35ac68a40a0` Marshall University — academic_programs 2026-27 · program_key=professional-pilot-b-s [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/commercial-pilot/ (sha256 bff59826ac1d)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 33, "groups": 7, "groups_skipped": 1}
  - program_name: Professional Pilot, B.S. ⟵ “Professional Pilot, B.S. | Marshall University Catalog”
### `307bbf3b8795aa85` Marshall University — academic_programs 2026-27 · program_key=general-business-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/general-business-ba/ (sha256 0e499abb3987)
- issues: stale_year_label:2026-27
- checks: {"courses": 36, "groups": 5, "groups_skipped": 0}
  - program_name: General Business, B.A. ⟵ “General Business, B.A. | Marshall University Catalog”
### `33d3b7d1f0a9f08e` Marshall University — academic_programs 2026-27 · program_key=theatre-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/theatre/theatre-ba/ (sha256 cf817f00c3e7)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 19, "groups": 3, "groups_skipped": 1}
  - program_name: Theatre, B.A. ⟵ “Theatre, B.A. | Marshall University Catalog”
### `347432e307cea9fc` Marshall University — academic_programs 2026-27 · program_key=english-education-5-adult-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-adult-ba/ (sha256 3edde6e32f12)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 45, "groups": 5, "groups_skipped": 1}
  - program_name: English Education 5-Adult, B.A. ⟵ “English Education 5-Adult, B.A. | Marshall University Catalog”
### `3d8f337b25297b4a` Marshall University — academic_programs 2026-27 · program_key=marketing-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/marketing-bba/ (sha256 a89f4c7b5103)
- issues: stale_year_label:2026-27
- checks: {"courses": 37, "groups": 5, "groups_skipped": 0}
  - program_name: Marketing, B.B.A. ⟵ “Marketing, B.B.A. | Marshall University Catalog”
### `3ed9a2058075f488` Marshall University — academic_programs 2026-27 · program_key=elementary-education-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/elementary-education-ba/ (sha256 cf1ced4029f1)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 39, "groups": 4, "groups_skipped": 1}
  - program_name: Elementary Education, B.A. ⟵ “Elementary Education, B.A. | Marshall University Catalog”
### `409eb51a860f62cf` Marshall University — academic_programs 2026-27 · program_key=media-production-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/media-production-major/ (sha256 2ca78a1962ef)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 20, "groups": 5, "groups_skipped": 1}
  - program_name: Media Production, B.A. ⟵ “Media Production, B.A. | Marshall University Catalog”
### `4fe54c80722147d9` Marshall University — academic_programs 2026-27 · program_key=accounting-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/accountancy-legal-environment/accounting-bba/ (sha256 5e05c1b99d2a)
- issues: stale_year_label:2026-27
- checks: {"courses": 46, "groups": 7, "groups_skipped": 0}
  - program_name: Accounting, B.B.A. ⟵ “Accounting, B.B.A. | Marshall University Catalog”
### `5b7d6ae124ec1a18` Marshall University — academic_programs 2026-27 · program_key=chemistry-education-9-adult-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/chemistry-9-adult-ba/ (sha256 9a3375dfca87)
- issues: stale_year_label:2026-27
- checks: {"courses": 31, "groups": 5, "groups_skipped": 0}
  - program_name: Chemistry Education 9-Adult, B.A. ⟵ “Chemistry Education 9-Adult, B.A. | Marshall University Catalog”
### `66fb8659346d6d5b` Marshall University — academic_programs 2026-27 · program_key=music-industry-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-industry-ba/ (sha256 7d78ebd93c2f)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 23, "groups": 4, "groups_skipped": 1}
  - program_name: Music Industry, B.A. ⟵ “Music Industry, B.A. | Marshall University Catalog”
### `6dc7c52daaf646ab` Marshall University — academic_programs 2026-27 · program_key=entrepreneurship-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/entrepreneurship-bba/ (sha256 839ba8c56661)
- issues: stale_year_label:2026-27
- checks: {"courses": 45, "groups": 7, "groups_skipped": 0}
  - program_name: Entrepreneurship, B.B.A. ⟵ “Entrepreneurship, B.B.A. | Marshall University Catalog”
### `79bb33c69152fb85` Marshall University — academic_programs 2026-27 · program_key=sustainability-management-and-technology-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/energy-management-bba/ (sha256 295b58adcd67)
- issues: stale_year_label:2026-27
- checks: {"courses": 45, "groups": 7, "groups_skipped": 0}
  - program_name: Sustainability Management and Technology, B.B.A. ⟵ “Sustainability Management and Technology, B.B.A. | Marshall University Catalog”
### `7b74921edb7387be` Marshall University — academic_programs 2026-27 · program_key=general-science-education-5-9-b-a-second-specialization-only [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/general-sciences-5-9-ba/ (sha256 309172c1129f)
- issues: stale_year_label:2026-27
- checks: {"courses": 12, "groups": 2, "groups_skipped": 0}
  - program_name: General Science Education 5-9, B.A. (Second Specialization only) ⟵ “General Science Education 5-9, B.A. (Second Specialization only) | Marshall University Catalog”
### `7d7654f191859678` Marshall University — academic_programs 2026-27 · program_key=management-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/management-bba/ (sha256 297ca1c10bd1)
- issues: stale_year_label:2026-27
- checks: {"courses": 41, "groups": 7, "groups_skipped": 0}
  - program_name: Management, B.B.A. ⟵ “Management, B.B.A. | Marshall University Catalog”
### `92cfc64b43e9636d` Marshall University — academic_programs 2026-27 · program_key=english-education-5-9-b-a-second-specialization-only [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-9-ba/ (sha256 9b70ab6738c4)
- issues: stale_year_label:2026-27
- checks: {"courses": 28, "groups": 2, "groups_skipped": 0}
  - program_name: English Education 5-9, B.A. (Second Specialization only) ⟵ “English Education 5-9, B.A. (Second Specialization only) | Marshall University Catalog”
### `97f5b3b316260726` Marshall University — academic_programs 2026-27 · program_key=international-business-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/international-business-bba/ (sha256 2a29047baee1)
- issues: stale_year_label:2026-27
- checks: {"courses": 40, "groups": 6, "groups_skipped": 0}
  - program_name: International Business, B.B.A. ⟵ “International Business, B.B.A. | Marshall University Catalog”
### `991025db6448f9cb` Marshall University — academic_programs 2026-27 · program_key=economics-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/economics-bba/ (sha256 0ebf21232ffc)
- issues: stale_year_label:2026-27
- checks: {"courses": 41, "groups": 7, "groups_skipped": 0}
  - program_name: Economics, B.B.A. ⟵ “Economics, B.B.A. | Marshall University Catalog”
### `9b620ebb0f8784c4` Marshall University — academic_programs 2026-27 · program_key=art-education-prek-adult-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/art-prek-adult-ba/ (sha256 e7242f382920)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 38, "groups": 4, "groups_skipped": 1}
  - program_name: Art Education PreK-Adult, B.A. ⟵ “Art Education PreK-Adult, B.A. | Marshall University Catalog”
### `aa2e971755a2ab8a` Marshall University — academic_programs 2026-27 · program_key=sports-business-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/sports-business-bba/ (sha256 afeae013fa90)
- issues: stale_year_label:2026-27
- checks: {"courses": 38, "groups": 7, "groups_skipped": 0}
  - program_name: Sports Business, B.B.A. ⟵ “Sports Business, B.B.A. | Marshall University Catalog”
### `ad3230672ba774be` Marshall University — academic_programs 2026-27 · program_key=aviation-maintenance-technology-a-a-s [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/aviation-maintenance-technology-aas/ (sha256 dd1b51516894)
- issues: stale_year_label:2026-27
- checks: {"courses": 25, "groups": 1, "groups_skipped": 0}
  - program_name: Aviation Maintenance Technology, A.A.S. ⟵ “Aviation Maintenance Technology, A.A.S. | Marshall University Catalog”
### `af07fef4f9c410d5` Marshall University — academic_programs 2026-27 · program_key=journalism-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/journalism-major/ (sha256 b19d2078960e)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 20, "groups": 5, "groups_skipped": 2}
  - program_name: Journalism, B.A. ⟵ “Journalism, B.A. | Marshall University Catalog”
### `b88c9464a09a4fb1` Marshall University — academic_programs 2026-27 · program_key=aviation-management-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
- checks: {"courses": 45, "groups": 8, "groups_skipped": 0}
  - program_name: Aviation Management, B.B.A. ⟵ “Aviation Management, B.B.A. | Marshall University Catalog”
### `cd49b621dd9d2e23` Marshall University — academic_programs 2026-27 · program_key=art-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/art-design/art-ba/ (sha256 b5ab0f178212)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 8, "groups": 3, "groups_skipped": 1}
  - program_name: Art, B.A. ⟵ “Art, B.A. | Marshall University Catalog”
### `cd4ff4dd465379e3` Marshall University — academic_programs 2026-27 · program_key=mathematics-education-5-9-b-a-second-specialization-only [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-9-ba/ (sha256 4800ec140164)
- issues: stale_year_label:2026-27
- checks: {"courses": 10, "groups": 2, "groups_skipped": 0}
  - program_name: Mathematics Education 5-9, B.A. (Second Specialization only) ⟵ “Mathematics Education 5-9, B.A. (Second Specialization only) | Marshall University Catalog”
### `cd8524773102aee9` Marshall University — academic_programs 2026-27 · program_key=special-education-multi-categorical-k-6-b-a-second-specialization-only [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/multi-categorical-special-education-k-6-ba-second/ (sha256 3e1de5a14e2d)
- issues: stale_year_label:2026-27
- checks: {"courses": 5, "groups": 1, "groups_skipped": 0}
  - program_name: Special Education Multi-Categorical K-6, B.A. (Second Specialization only) ⟵ “Special Education Multi-Categorical K-6, B.A. (Second Specialization only) | Marshall University Catalog”
### `cd8ee2ef98e4582c` Marshall University — academic_programs 2026-27 · program_key=music-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-ba/ (sha256 de0bb8ec5eb8)
- issues: stale_year_label:2026-27
- checks: {"courses": 27, "groups": 4, "groups_skipped": 0}
  - program_name: Music, B.A. ⟵ “Music, B.A. | Marshall University Catalog”
### `da8ed44af3915daf` Marshall University — academic_programs 2026-27 · program_key=music-education-prek-adult-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/music-prek-adult-ba/ (sha256 ce2426bbde6b)
- issues: stale_year_label:2026-27, requirement_groups_skipped
- checks: {"courses": 41, "groups": 4, "groups_skipped": 1}
  - program_name: Music Education PreK-Adult, B.A. ⟵ “Music Education PreK-Adult, B.A. | Marshall University Catalog”
### `e03d5cbcf1da4fad` Marshall University — academic_programs 2026-27 · program_key=mathematics-education-5-adult-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-adult-ba/ (sha256 9c91dea8d549)
- issues: stale_year_label:2026-27
- checks: {"courses": 34, "groups": 5, "groups_skipped": 0}
  - program_name: Mathematics Education 5-Adult, B.A. ⟵ “Mathematics Education 5-Adult, B.A. | Marshall University Catalog”
### `f43084c582fe94ab` Marshall University — academic_programs 2026-27 · program_key=management-information-systems-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/management-information-system-bba/ (sha256 fce4dc767b53)
- issues: stale_year_label:2026-27
- checks: {"courses": 45, "groups": 7, "groups_skipped": 0}
  - program_name: Management Information Systems, B.B.A. ⟵ “Management Information Systems, B.B.A. | Marshall University Catalog”
### `f60206a12ee3e6ad` Marshall University — academic_programs 2026-27 · program_key=finance-b-b-a [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/finance-bba/ (sha256 9cefcfa0a87f)
- issues: stale_year_label:2026-27
- checks: {"courses": 43, "groups": 7, "groups_skipped": 0}
  - program_name: Finance, B.B.A. ⟵ “Finance, B.B.A. | Marshall University Catalog”
### `3d81dd3ccd27ecc0` Marshall University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/financial-information-fees-assistance-scholarships/ (sha256 29e694fc85e2)
- issues: cost_period_semester
- checks: {"columns": 1, "rows": 15}
  - column:Base Tuition and Fees: 4809.0 ⟵ “Base Tuition and Fees | 4,809.00 | 6,632.00 | 10,219.00”
  - column:College of Engineering and Computer Sciences: 5412.0 ⟵ “College of Engineering and Computer Sciences | 5,412.00 | 7,497.00 | 11,106.00”
  - column:College of Arts and Media Fine Arts: 5189.0 ⟵ “College of Arts and Media Fine Arts | 5,189.00 | 7,052.00 | 10,649.00”
  - column:College of Arts and Media Journalism Program: 4954.0 ⟵ “College of Arts and Media Journalism Program | 4,954.00 | 6,835.00 | 10,427.00”
  - column:College of Business: 4981.0 ⟵ “College of Business | 4,981.00 | 6,897.00 | 10,491.00”
  - column:College of Education and Professional Development: 5014.0 ⟵ “College of Education and Professional Development | 5,014.00 | 6,832.00 | 10,419.00”
  - column:College of Health Professions: 5029.0 ⟵ “College of Health Professions | 5,029.00 | 7,102.00 | 10,701.00”
  - column:College of Health Professions - Clinical Laboratory Sciences, Comm. Disorders, Dietetics: 5166.0 ⟵ “College of Health Professions - Clinical Laboratory Sciences, Comm. Disorders, Dietetics | 5,166.00 | 7,232.00 | 10,833.00”
  - column:College of Health Professions - Kinesiology: 5135.0 ⟵ “College of Health Professions - Kinesiology | 5,135.00 | 7,202.00 | 10,803.00”
  - column:College of Health Professions - Nursing: 5465.0 ⟵ “College of Health Professions - Nursing | 5,465.00 | 7,512.00 | 11,120.00”
  - column:College of Liberal Arts: 4937.0 ⟵ “College of Liberal Arts | 4,937.00 | 6,807.00 | 10,369.00”
  - column:College of Science: 5004.0 ⟵ “College of Science | 5,004.00 | 6,850.00 | 10,451.00”
  - column:Regents Bachelor of Arts: 4809.0 ⟵ “Regents Bachelor of Arts | 4,809.00 | 6,632.00 | 10,219.00”
  - column:University College: 4809.0 ⟵ “University College | 4,809.00 | 6,632.00 | 10,219.00”
  - column:Aviation: 4809.0 ⟵ “Aviation | 4,809.00 | 6,632.00 | 10,219.00”
### `8422c150122e0d76` Marshall University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/financial-information-fees-assistance-scholarships/ (sha256 29e694fc85e2)
- issues: cost_period_semester
- checks: {"columns": 1, "rows": 15}
  - column:Base Tuition and Fees: 10219.0 ⟵ “Base Tuition and Fees | 4,809.00 | 6,632.00 | 10,219.00”
  - column:College of Engineering and Computer Sciences: 11106.0 ⟵ “College of Engineering and Computer Sciences | 5,412.00 | 7,497.00 | 11,106.00”
  - column:College of Arts and Media Fine Arts: 10649.0 ⟵ “College of Arts and Media Fine Arts | 5,189.00 | 7,052.00 | 10,649.00”
  - column:College of Arts and Media Journalism Program: 10427.0 ⟵ “College of Arts and Media Journalism Program | 4,954.00 | 6,835.00 | 10,427.00”
  - column:College of Business: 10491.0 ⟵ “College of Business | 4,981.00 | 6,897.00 | 10,491.00”
  - column:College of Education and Professional Development: 10419.0 ⟵ “College of Education and Professional Development | 5,014.00 | 6,832.00 | 10,419.00”
  - column:College of Health Professions: 10701.0 ⟵ “College of Health Professions | 5,029.00 | 7,102.00 | 10,701.00”
  - column:College of Health Professions - Clinical Laboratory Sciences, Comm. Disorders, Dietetics: 10833.0 ⟵ “College of Health Professions - Clinical Laboratory Sciences, Comm. Disorders, Dietetics | 5,166.00 | 7,232.00 | 10,833.00”
  - column:College of Health Professions - Kinesiology: 10803.0 ⟵ “College of Health Professions - Kinesiology | 5,135.00 | 7,202.00 | 10,803.00”
  - column:College of Health Professions - Nursing: 11120.0 ⟵ “College of Health Professions - Nursing | 5,465.00 | 7,512.00 | 11,120.00”
  - column:College of Liberal Arts: 10369.0 ⟵ “College of Liberal Arts | 4,937.00 | 6,807.00 | 10,369.00”
  - column:College of Science: 10451.0 ⟵ “College of Science | 5,004.00 | 6,850.00 | 10,451.00”
  - column:Regents Bachelor of Arts: 10219.0 ⟵ “Regents Bachelor of Arts | 4,809.00 | 6,632.00 | 10,219.00”
  - column:University College: 10219.0 ⟵ “University College | 4,809.00 | 6,632.00 | 10,219.00”
  - column:Aviation: 10219.0 ⟵ “Aviation | 4,809.00 | 6,632.00 | 10,219.00”
### `fe5bdc9ee96f7a6f` Marshall University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/financial-information-fees-assistance-scholarships/ (sha256 29e694fc85e2)
- issues: cost_period_semester, residency_unknown
- checks: {"columns": 1, "rows": 15}
  - column:Base Tuition and Fees: 6632.0 ⟵ “Base Tuition and Fees | 4,809.00 | 6,632.00 | 10,219.00”
  - column:College of Engineering and Computer Sciences: 7497.0 ⟵ “College of Engineering and Computer Sciences | 5,412.00 | 7,497.00 | 11,106.00”
  - column:College of Arts and Media Fine Arts: 7052.0 ⟵ “College of Arts and Media Fine Arts | 5,189.00 | 7,052.00 | 10,649.00”
  - column:College of Arts and Media Journalism Program: 6835.0 ⟵ “College of Arts and Media Journalism Program | 4,954.00 | 6,835.00 | 10,427.00”
  - column:College of Business: 6897.0 ⟵ “College of Business | 4,981.00 | 6,897.00 | 10,491.00”
  - column:College of Education and Professional Development: 6832.0 ⟵ “College of Education and Professional Development | 5,014.00 | 6,832.00 | 10,419.00”
  - column:College of Health Professions: 7102.0 ⟵ “College of Health Professions | 5,029.00 | 7,102.00 | 10,701.00”
  - column:College of Health Professions - Clinical Laboratory Sciences, Comm. Disorders, Dietetics: 7232.0 ⟵ “College of Health Professions - Clinical Laboratory Sciences, Comm. Disorders, Dietetics | 5,166.00 | 7,232.00 | 10,833.00”
  - column:College of Health Professions - Kinesiology: 7202.0 ⟵ “College of Health Professions - Kinesiology | 5,135.00 | 7,202.00 | 10,803.00”
  - column:College of Health Professions - Nursing: 7512.0 ⟵ “College of Health Professions - Nursing | 5,465.00 | 7,512.00 | 11,120.00”
  - column:College of Liberal Arts: 6807.0 ⟵ “College of Liberal Arts | 4,937.00 | 6,807.00 | 10,369.00”
  - column:College of Science: 6850.0 ⟵ “College of Science | 5,004.00 | 6,850.00 | 10,451.00”
  - column:Regents Bachelor of Arts: 6632.0 ⟵ “Regents Bachelor of Arts | 4,809.00 | 6,632.00 | 10,219.00”
  - column:University College: 6632.0 ⟵ “University College | 4,809.00 | 6,632.00 | 10,219.00”
  - column:Aviation: 6632.0 ⟵ “Aviation | 4,809.00 | 6,632.00 | 10,219.00”
### `f49be8e53cdc3409` Marshall University — credit_policies 2026-27 · policy_kind=IB [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/admissions/ (sha256 b02cc5043c21)
- issues: rows_without_score
- checks: {"distinct_exams": 15, "equivalencies": 17, "rows_without_score": 17}
  - equivalencies[IB-BIOLOGY|None]:  ⟵ “Biology | BSC 104, BSC 104L | BSC 104, BSC 104L | BSC 120, BSC 120L or 120LH, BSC 121, BSC 121L | BSC 120, BSC 120L or 120LH, BSC 121, BSC 121L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|None]:  ⟵ “Business | MGT 100 | MGT 100 | MGT 100 | MGT 100”
  - equivalencies[IB-CHEMISTRY|None]:  ⟵ “Chemistry | CHM 205, CHM 217 | CHM 205, CHM 217 | CHM 205, CHM 217, CHM 218 | CHM 205, CHM 217, CHM 218”
  - equivalencies[IB-LATIN|None]:  ⟵ “Classical Latin | LAT 101 | LAT 101 | LAT 101, LAT 102 | LAT 101, LAT 102”
  - equivalencies[IB-ECONOMICS|None]:  ⟵ “Economics | ECN 250 | ECN 250 | ECN 250, ECN 253 | ECN 250, ECN 253”
  - equivalencies[IB-FRENCH|None]:  ⟵ “French | FRN 101 | FRN 101 | FRN 101, FRN 102 | FRN 101, FRN 102”
  - equivalencies[IB-GEOGRAPHY|None]:  ⟵ “Geography | GEO 100 | GEO 100 | GEO 100, GEO 3 Hrs Unclassified (lower division) | GEO 100, GEO 3 Hrs Unclassified (lower division)”
  - equivalencies[IB-GERMAN|None]:  ⟵ “German | GER 101 | GER 101 | GER 101, GER 102 | GER 101, GER 102”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History | HST 103 | HST 103 | HST 103 | HST 103”
  - equivalencies[IB-HISTORY|None]:  ⟵ “History of the Americas | N/A | HST 230, HST 231 | HST 230, HST 231 | HST 230, HST 231”
  - equivalencies[IB-HISTORY|None]:  ⟵ “Islamic History | HST 260 | HST 260 | HST 260 | HST 260”
  - equivalencies[IB-MUSIC|None]:  ⟵ “Music | MUS 142 | MUS 142 | MUS 142, MUS 111 | MUS 142, MUS 111”
  - equivalencies[IB-PHYSICS|None]:  ⟵ “Physics | N/A | PHY 201, PHY 202 | PHY 201, PHY 202, PHY 203, PHY 204 | PHY 201, PHY 202, PHY 203, PHY 204”
  - equivalencies[IB-PSYCHOLOGY|None]:  ⟵ “Psychology | PSY 201 | PSY 201 | PSY 201 | PSY 201”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|None]:  ⟵ “Social Anthropology | ANT 201 | ANT 201 | ANT 201 | ANT 201”
  - equivalencies[IB-SPANISH|None]:  ⟵ “Spanish | SPN 101 | SPN 101 | SPN 101, SPN 102 | SPN 101, SPN 102”
  - equivalencies[IB-THEATRE|None]:  ⟵ “Theater Arts | THE 112 | THE 112 | THE 112, THE 220 | THE 112, THE 220”
### `00898f91e4254afa` Marshall University — degree_requirements 2026-27 · program_key=management-information-systems-b-b-a · requirement_key=course-requirements-communications-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/management-information-system-bba/ (sha256 fce4dc767b53)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `0281ed60fae1c794` Marshall University — degree_requirements 2026-27 · program_key=elementary-education-b-a · requirement_key=elementary-education-b-a-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/elementary-education-ba/ (sha256 cf1ced4029f1)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: HST 230 ⟵ “HST 230 - American History to 1877 (CT)”
  - courses: HST 231 ⟵ “HST 231 - American Hist From 1877 (CT)”
### `03d88ed652c3eb1a` Marshall University — degree_requirements 2026-27 · program_key=professional-pilot-b-s · requirement_key=course-requirements-core-ii [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/commercial-pilot/ (sha256 bff59826ac1d)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
### `06aa4172325feaef` Marshall University — degree_requirements 2026-27 · program_key=management-information-systems-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/management-information-system-bba/ (sha256 fce4dc767b53)
- issues: stale_year_label:2026-27
  - courses: MIS 300 ⟵ “MIS 300 - Intro to Business Programming”
  - courses: MIS 310 ⟵ “MIS 310 - Bus Sys Analysis & Design”
  - courses: MIS 333 ⟵ “MIS 333 - Bus Telecomm Sys”
  - courses: MIS 340 ⟵ “MIS 340 - Intro to Database Mgt Systems”
  - courses: MIS 360 ⟵ “MIS 360 - Intro to Bus Intel & Analytics”
  - courses: MIS 420 ⟵ “MIS 420 - Info Security Management”
  - courses: MIS 470 ⟵ “MIS 470 - Business Sys Proj Mgt”
  - courses: MIS 475 ⟵ “MIS 475 - Strat Management Info Systems”
### `070569fb6445c979` Marshall University — degree_requirements 2026-27 · program_key=finance-b-b-a · requirement_key=course-requirements-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/finance-bba/ (sha256 9cefcfa0a87f)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `0999c471301bae2d` Marshall University — degree_requirements 2026-27 · program_key=management-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/management-bba/ (sha256 297ca1c10bd1)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `0aab33298bfd67df` Marshall University — degree_requirements 2026-27 · program_key=accounting-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/accountancy-legal-environment/accounting-bba/ (sha256 5e05c1b99d2a)
- issues: stale_year_label:2026-27
  - courses: ACC 311 ⟵ “ACC 311 - Intermediate Accounting I”
  - courses: ACC 312 ⟵ “ACC 312 - Intermediate Accounting II”
  - courses: ACC 318 ⟵ “ACC 318 - Cost Accounting I”
  - courses: ACC 341 ⟵ “ACC 341 - Acc Information Systems”
  - courses: ACC 348 ⟵ “ACC 348 - Federal Taxation”
  - courses: ACC 429 ⟵ “ACC 429 - Auditing I”
  - courses: ACC 440 ⟵ “ACC 440 - Accounting Analytics”
  - courses: ACC 499 ⟵ “ACC 499 - Professional and Ethics Sem”
  - courses: ACC 198 ⟵ “ACC 198 - Accounting Professionalism”
### `0c5ae7b971ebdfe6` Marshall University — degree_requirements 2026-27 · program_key=aviation-management-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `0e3a5dde7a72f2f9` Marshall University — degree_requirements 2026-27 · program_key=entrepreneurship-b-b-a · requirement_key=course-requirements-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/entrepreneurship-bba/ (sha256 839ba8c56661)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `0ff64fd4baca4525` Marshall University — degree_requirements 2026-27 · program_key=international-business-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/international-business-bba/ (sha256 2a29047baee1)
- issues: stale_year_label:2026-27
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: FIN 343 ⟵ “FIN 343 - Intermediate Financial Manage”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management”
  - courses: MGT 478 ⟵ “MGT 478 - Import Export Management”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
  - courses: FIN 475 ⟵ “FIN 475 - Intl Business Strategies”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
### `14fb4e37fd8de3c2` Marshall University — degree_requirements 2026-27 · program_key=english-education-5-adult-b-a · requirement_key=english-education-5-adult-b-a-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-adult-ba/ (sha256 3edde6e32f12)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
### `16cf92227054faa3` Marshall University — degree_requirements 2026-27 · program_key=sustainability-management-and-technology-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/energy-management-bba/ (sha256 295b58adcd67)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `17d6660912124fa3` Marshall University — degree_requirements 2026-27 · program_key=sustainability-management-and-technology-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/energy-management-bba/ (sha256 295b58adcd67)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `18812aa5a9bd446b` Marshall University — degree_requirements 2026-27 · program_key=theatre-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/theatre/theatre-ba/ (sha256 cf817f00c3e7)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
### `195a10b65ae99725` Marshall University — degree_requirements 2026-27 · program_key=international-business-b-b-a · requirement_key=course-requirements-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/international-business-bba/ (sha256 2a29047baee1)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `1cab10bdb8e8c2b3` Marshall University — degree_requirements 2026-27 · program_key=mathematics-education-5-adult-b-a · requirement_key=mathematics-education-5-adult-b-a-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-adult-ba/ (sha256 9c91dea8d549)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: MTH 229 ⟵ “MTH 229 - Calculus/Analytic Geom I (CT)”
### `1d6ac4b020dec2d8` Marshall University — degree_requirements 2026-27 · program_key=finance-b-b-a · requirement_key=course-requirements-finance-electives [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/finance-bba/ (sha256 9cefcfa0a87f)
- issues: stale_year_label:2026-27
  - courses: ECN 310 ⟵ “ECN 310 - Money and Banking”
  - courses: ECN 326 ⟵ “ECN 326 - Int Macroeconomic Analys”
  - courses: ECN 328 ⟵ “ECN 328 - Int Microeconomic Analys”
  - courses: ECN 423 ⟵ “ECN 423 - Intro to Econometrics”
  - courses: ACC 311 ⟵ “ACC 311 - Intermediate Accounting I”
  - courses: ACC 312 ⟵ “ACC 312 - Intermediate Accounting II”
  - courses: ACC 418 ⟵ “ACC 418 - Managerial Accounting”
### `226aed0fae73fa5c` Marshall University — degree_requirements 2026-27 · program_key=finance-b-b-a · requirement_key=course-requirements-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/finance-bba/ (sha256 9cefcfa0a87f)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `28f004335daf0408` Marshall University — degree_requirements 2026-27 · program_key=general-science-education-5-adult-b-a · requirement_key=general-science-education-5-adult-b-a-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/general-sciences-5-adult-ba/ (sha256 f10930c2ff94)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: EDF 201 ⟵ “EDF 201 - Ed Psych Developing Learner”
  - courses: EDF 200 ⟵ “EDF 200 - Pre-Residency Clinical”
  - courses: EDF 202 ⟵ “EDF 202 - Appl Clin Participation I”
  - courses: EDF 204 ⟵ “EDF 204 - Appl Clin Participation II”
  - courses: CISP 421 ⟵ “CISP 421 - Child with Exceptionalities”
  - courses: EDF 435 ⟵ “EDF 435 - Classroom Assessment”
  - courses: EDF 475 ⟵ “EDF 475 - Schools in a Diverse Society”
  - courses: CI 345 ⟵ “CI 345 - Crit Read Writ & Think”
  - courses: CI 402 ⟵ “CI 402 - Teach Mid Child Learners”
  - courses: CI 449 ⟵ “CI 449 - Instr & Clarm Mgt Sec Ed”
  - courses: CISP 422 ⟵ “CISP 422 - Differentiate Instruction”
  - courses: CI 415 ⟵ “CI 415 - Int Meth & Mat: Sec Ed”
  - courses: CI 470 ⟵ “CI 470 - Residency I Clinical”
  - courses: CI 451 ⟵ “CI 451 - Residency II - Secondary”
### `295b176135f38271` Marshall University — degree_requirements 2026-27 · program_key=aviation-management-b-b-a · requirement_key=course-requirements-core-ii-humanities [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `29c490afece0b82b` Marshall University — degree_requirements 2026-27 · program_key=media-production-b-a · requirement_key=course-requirements-core-i-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/media-production-major/ (sha256 2ca78a1962ef)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
### `2ded5316f088e991` Marshall University — degree_requirements 2026-27 · program_key=elementary-education-b-a · requirement_key=elementary-education-b-a-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/elementary-education-ba/ (sha256 cf1ced4029f1)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 127 ⟵ “MTH 127 - College Algebra-Expanded”
  - courses: BSC 105 ⟵ “BSC 105 - Human Biology (& BSC 105L Human Biology Lab)”
  - courses: HST 103 ⟵ “HST 103 - The World Since 1850 (CT)”
### `2ec8cb758af36fb8` Marshall University — degree_requirements 2026-27 · program_key=general-science-education-5-adult-b-a · requirement_key=general-science-education-5-adult-b-a-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/general-sciences-5-adult-ba/ (sha256 f10930c2ff94)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: GEO 230 ⟵ “GEO 230 - Physical Meteorology (CT)”
### `2f2d08ff67faabce` Marshall University — degree_requirements 2026-27 · program_key=marketing-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/marketing-bba/ (sha256 a89f4c7b5103)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `2fc8ef4611314cd3` Marshall University — degree_requirements 2026-27 · program_key=sustainability-management-and-technology-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/energy-management-bba/ (sha256 295b58adcd67)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: MGT 458 ⟵ “MGT 458 - Energy Management Strategy (Capstone)”
### `325a4ede8ecf3c7b` Marshall University — degree_requirements 2026-27 · program_key=management-b-b-a · requirement_key=course-requirements-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/management-bba/ (sha256 297ca1c10bd1)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `32e846b71d2364c1` Marshall University — degree_requirements 2026-27 · program_key=sports-business-b-b-a · requirement_key=course-requirements-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/sports-business-bba/ (sha256 afeae013fa90)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `353805054f4da7ce` Marshall University — degree_requirements 2026-27 · program_key=biological-science-education-9-adult-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/biological-science-9-adult-ba/ (sha256 9c8eb6e96f70)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
### `377bc02809779ae4` Marshall University — degree_requirements 2026-27 · program_key=art-education-prek-adult-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/art-prek-adult-ba/ (sha256 e7242f382920)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
### `37b98f163daefb71` Marshall University — degree_requirements 2026-27 · program_key=economics-b-b-a · requirement_key=major-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/economics-bba/ (sha256 0ebf21232ffc)
- issues: stale_year_label:2026-27
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `39111270038fb27b` Marshall University — degree_requirements 2026-27 · program_key=music-industry-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-industry-ba/ (sha256 7d78ebd93c2f)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
### `3a82ffaaf0dd5470` Marshall University — degree_requirements 2026-27 · program_key=art-education-prek-adult-b-a · requirement_key=course-requirements-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/art-prek-adult-ba/ (sha256 e7242f382920)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ART 112 ⟵ “ART 112 - Intro To Visual Art”
  - courses: ART 201 ⟵ “ART 201 - History of Art I (CT)”
  - courses: ART 202 ⟵ “ART 202 - History of Art II (CT)”
  - courses: ART 214 ⟵ “ART 214 - Foundations: Grid/Chroma”
  - courses: ART 215 ⟵ “ART 215 - Foundations: Form/Space”
  - courses: ART 217 ⟵ “ART 217 - Foundations: Record/Layer”
  - courses: ART 218 ⟵ “ART 218 - Foundations: Surface/Matrix”
  - courses: ART 219 ⟵ “ART 219 - Foundations: Frame/Time”
  - courses: ART 299 ⟵ “ART 299 - Foundations Review: BA”
  - courses: ART 301 ⟵ “ART 301 - Printmaking Processes”
  - courses: ART 305 ⟵ “ART 305 - Ceramics”
  - courses: ART 307 ⟵ “ART 307 - Sculpture”
  - courses: ART 310 ⟵ “ART 310 - Art Education: Elementary”
  - courses: ART 325 ⟵ “ART 325 - Image Visualization: Digital”
  - courses: ART 340 ⟵ “ART 340 - Art Education: Secondary”
  - courses: ART 350 ⟵ “ART 350 - Watercolor Painting”
  - courses: ART 389 ⟵ “ART 389 - 20th Century Art”
  - courses: ART 460 ⟵ “ART 460 - History & Phil of Art Ed”
### `3af3a60269bd9b19` Marshall University — degree_requirements 2026-27 · program_key=sports-business-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/sports-business-bba/ (sha256 afeae013fa90)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `3d0c8dd31d7a3b21` Marshall University — degree_requirements 2026-27 · program_key=sports-business-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/sports-business-bba/ (sha256 afeae013fa90)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: STHM 496 ⟵ “STHM 496 - Olympic Games (Multicultural or International)”
  - courses: STHM 475 ⟵ “STHM 475 - Capstone Seminar”
### `3e225de50c0b5f18` Marshall University — degree_requirements 2026-27 · program_key=chemistry-education-9-adult-b-a · requirement_key=chemistry-education-9-adult-b-a-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/chemistry-9-adult-ba/ (sha256 9a3375dfca87)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
### `3e50548d2e93fad7` Marshall University — degree_requirements 2026-27 · program_key=general-science-education-5-adult-b-a · requirement_key=general-science-education-5-adult-b-a-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/general-sciences-5-adult-ba/ (sha256 f10930c2ff94)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 127 ⟵ “MTH 127 - College Algebra-Expanded”
  - courses: BSC 120 ⟵ “BSC 120 - Principles of Biology I”
  - courses: BSC 120L ⟵ “BSC 120L - Principles of Biology I Lab”
### `3e940bbb885461ea` Marshall University — degree_requirements 2026-27 · program_key=art-education-prek-adult-b-a · requirement_key=course-requirements-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/art-prek-adult-ba/ (sha256 e7242f382920)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: EDF 200 ⟵ “EDF 200 - Pre-Residency Clinical”
  - courses: EDF 202 ⟵ “EDF 202 - Appl Clin Participation I”
  - courses: EDF 204 ⟵ “EDF 204 - Appl Clin Participation II”
  - courses: EDF 201 ⟵ “EDF 201 - Ed Psych Developing Learner”
  - courses: CISP 421 ⟵ “CISP 421 - Child with Exceptionalities”
  - courses: EDF 475 ⟵ “EDF 475 - Schools in a Diverse Society”
  - courses: CI 345 ⟵ “CI 345 - Crit Read Writ & Think”
  - courses: CI 402 ⟵ “CI 402 - Teach Mid Child Learners”
  - courses: CI 449 ⟵ “CI 449 - Instr & Clarm Mgt Sec Ed”
  - courses: CISP 422 ⟵ “CISP 422 - Differentiate Instruction”
  - courses: ART 468 ⟵ “ART 468 - Secondary Ed: Teaching Art”
  - courses: CI 470 ⟵ “CI 470 - Residency I Clinical”
  - courses: CI 451 ⟵ “CI 451 - Residency II - Secondary”
### `3fab7a98bfe43b41` Marshall University — degree_requirements 2026-27 · program_key=general-business-b-a · requirement_key=course-requirements-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/general-business-ba/ (sha256 0e499abb3987)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `3febdcf5d59da4f7` Marshall University — degree_requirements 2026-27 · program_key=management-information-systems-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/management-information-system-bba/ (sha256 fce4dc767b53)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `4267e1adfe532241` Marshall University — degree_requirements 2026-27 · program_key=management-information-systems-b-b-a · requirement_key=course-requirements-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/management-information-system-bba/ (sha256 fce4dc767b53)
- issues: stale_year_label:2026-27
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `4354f968429fce3a` Marshall University — degree_requirements 2026-27 · program_key=professional-pilot-b-s · requirement_key=course-requirements-elective-aviation-courses [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/commercial-pilot/ (sha256 bff59826ac1d)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: AVSC 221 ⟵ “AVSC 221 - Systems Management”
  - courses: AVSC 315 ⟵ “AVSC 315 - Airport Operations and Mgmt”
  - courses: AVSC 376 ⟵ “AVSC 376 - Commercial Rotorcraft Add - On”
  - courses: AVSC 380 ⟵ “AVSC 380 - FAA Aircraft Dispatcher”
  - courses: AVSC 410 ⟵ “AVSC 410 - Air Transportation Operations”
  - courses: AVSC 420 ⟵ “AVSC 420 - International Aviation”
  - courses: AVSC 454 ⟵ “AVSC 454 - Drones: Remote Sensing & GIS”
  - courses: AVSC 495 ⟵ “AVSC 495 - Internship in Aviation Ops”
### `4486f55655ea07e0` Marshall University — degree_requirements 2026-27 · program_key=aviation-management-b-b-a · requirement_key=course-requirements-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
### `466d0da7ad931a8f` Marshall University — degree_requirements 2026-27 · program_key=health-care-management-b-b-a · requirement_key=course-requirements-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/health-care-management-bba/ (sha256 11c16303570e)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `47d13202b66c08b6` Marshall University — degree_requirements 2026-27 · program_key=marketing-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/marketing-bba/ (sha256 a89f4c7b5103)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `4839788f7a98d842` Marshall University — degree_requirements 2026-27 · program_key=elementary-education-b-a · requirement_key=elementary-education-b-a-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/elementary-education-ba/ (sha256 cf1ced4029f1)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: EDF 201 ⟵ “EDF 201 - Ed Psych Developing Learner”
  - courses: EDF 200 ⟵ “EDF 200 - Pre-Residency Clinical”
  - courses: EDF 202 ⟵ “EDF 202 - Appl Clin Participation I”
  - courses: EDF 204 ⟵ “EDF 204 - Appl Clin Participation II”
  - courses: EDF 435 ⟵ “EDF 435 - Classroom Assessment”
  - courses: EDF 475 ⟵ “EDF 475 - Schools in a Diverse Society”
  - courses: CISP 421 ⟵ “CISP 421 - Child with Exceptionalities”
  - courses: CISP 422 ⟵ “CISP 422 - Differentiate Instruction”
  - courses: CI 301 ⟵ “CI 301 - Teach Elem/Middle Mathematics”
  - courses: CI 360 ⟵ “CI 360 - Social Studies Methods Elem”
  - courses: CI 442 ⟵ “CI 442 - Instr & Clrm Mgt in Elem Ed”
  - courses: CI 448 ⟵ “CI 448 - Science Methods: Elem Edu”
  - courses: CI 447 ⟵ “CI 447 - Inte Read/Lang Arts: Elem Edu”
  - courses: CI 471 ⟵ “CI 471 - Residency I Clinical”
  - courses: CI 407 ⟵ “CI 407 - Residency II - Elementary”
### `48bc8a4bafac49c0` Marshall University — degree_requirements 2026-27 · program_key=mathematics-education-5-9-b-a-second-specialization-only · requirement_key=course-requirements-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-9-ba/ (sha256 4800ec140164)
- issues: stale_year_label:2026-27
  - courses: CI 301 ⟵ “CI 301 - Teach Elem/Middle Mathematics”
  - courses: CI 402 ⟵ “CI 402 - Teach Mid Child Learners”
### `4e3a4de0d1fc6548` Marshall University — degree_requirements 2026-27 · program_key=aviation-management-b-b-a · requirement_key=course-requirements-communications-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `508eeb6696f7adcb` Marshall University — degree_requirements 2026-27 · program_key=sustainability-management-and-technology-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/energy-management-bba/ (sha256 295b58adcd67)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `509afa77e0f4a60a` Marshall University — degree_requirements 2026-27 · program_key=aviation-maintenance-technology-a-a-s · requirement_key=course-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/aviation-maintenance-technology-aas/ (sha256 dd1b51516894)
- issues: stale_year_label:2026-27
  - courses: AMT 101 ⟵ “AMT 101 - Beginning Aviation Maintenance”
  - courses: AMT 102 ⟵ “AMT 102 - Regulations & Publications”
  - courses: AMT 103 ⟵ “AMT 103 - Technical Skills & Practices”
  - courses: AMT 105 ⟵ “AMT 105 - Aviation Utility Systems”
  - courses: AMT 109 ⟵ “AMT 109 - Aviation Electronics”
  - courses: AMT 110 ⟵ “AMT 110 - Aviation Power Systems”
  - courses: AMT 201 ⟵ “AMT 201 - Reciprocating Engines”
  - courses: AMT 202 ⟵ “AMT 202 - Sheet Metal Structures”
  - courses: AMT 203 ⟵ “AMT 203 - Reciprocating Engine Maint”
  - courses: AMT 204 ⟵ “AMT 204 - Propeller & Control Systems”
  - courses: AMT 205 ⟵ “AMT 205 - Turbine Engines”
  - courses: AMT 206 ⟵ “AMT 206 - Fluid Power and Landing Gear”
  - courses: AMT 207 ⟵ “AMT 207 - Turbine Engine Maintenance”
  - courses: AMT 208 ⟵ “AMT 208 - Cabin Atmosphere Systems”
  - courses: AMT 209 ⟵ “AMT 209 - Airframe Inspection and Fl Con”
  - courses: AMT 210 ⟵ “AMT 210 - Nonmetallic Structures”
  - courses: AMT 211 ⟵ “AMT 211 - Aircraft Information Systems”
  - courses: AMT 215 ⟵ “AMT 215 - Certification Test Preparation I”
  - courses: AMT 216 ⟵ “AMT 216 - Certification Test Preparation II”
  - courses: AMT 217 ⟵ “AMT 217 - Certification Test Preparation III”
  - courses: MAT 135 ⟵ “MAT 135 - Technical Mathematics”
  - courses: MG 102 ⟵ “MG 102 - Introduction to Entrepreneurship”
  - courses: ENL 131 ⟵ “ENL 131 - Business and Technical Writing”
  - courses: IT 101 ⟵ “IT 101 - Fundamentals of Computers”
  - courses: PSYC 200 ⟵ “PSYC 200 - General Psychology OR SOCI 210, Fundamentals of Sociology”
### `526de49a0c7bfd61` Marshall University — degree_requirements 2026-27 · program_key=health-care-management-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/health-care-management-bba/ (sha256 11c16303570e)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: MGT 455 ⟵ “MGT 455 - Hlth Care Policy Seminar (Capstone)”
### `526ec2a0fb90e9c1` Marshall University — degree_requirements 2026-27 · program_key=economics-b-b-a · requirement_key=major-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/economics-bba/ (sha256 0ebf21232ffc)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `56f7e2b34994c06e` Marshall University — degree_requirements 2026-27 · program_key=management-b-b-a · requirement_key=course-requirements-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/management-bba/ (sha256 297ca1c10bd1)
- issues: stale_year_label:2026-27
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management (cannot count as both the International Business Elective and a MGT Elective)”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `581128dea97d8aeb` Marshall University — degree_requirements 2026-27 · program_key=chemistry-education-9-adult-b-a · requirement_key=chemistry-education-9-adult-b-a-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/chemistry-9-adult-ba/ (sha256 9a3375dfca87)
- issues: stale_year_label:2026-27, course_alternatives_in_rule_text
  - courses: CHM 211 ⟵ “CHM 211 - Principles of Chemistry I”
  - courses: CHM 217 ⟵ “CHM 217 - Principles of Chem Lab I”
  - courses: CHM 212 ⟵ “CHM 212 - Principles Chemistry II”
  - courses: CHM 218 ⟵ “CHM 218 - Principles of Chem Lab II”
  - courses: CHM 327 ⟵ “CHM 327 - Intro Organic Chemistry”
  - courses: CHM 345 ⟵ “CHM 345 - Intro to Analytical Chem”
  - courses: CHM 357 ⟵ “CHM 357 - Physical Chemistry: Quantum”
  - courses: CHM 365 ⟵ “CHM 365 - Introductory Biochemistry”
  - courses: MTH 127 ⟵ “MTH 127 - College Algebra-Expanded”
  - courses: MTH 140 ⟵ “MTH 140 - Applied Calculus”
  - courses: PS 325 ⟵ “PS 325 - Dev Scientific Thought”
  - courses: CHM 481 ⟵ “CHM 481 - Special Topics (Applications of Chemical ED) (C)”
### `598e47a70fd02a88` Marshall University — degree_requirements 2026-27 · program_key=international-business-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/international-business-bba/ (sha256 2a29047baee1)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `5aadbdc08fe97925` Marshall University — degree_requirements 2026-27 · program_key=general-business-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/general-business-ba/ (sha256 0e499abb3987)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Capstone) (Writing Intensive)”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `5b542455bc3ed5f3` Marshall University — degree_requirements 2026-27 · program_key=accounting-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/accountancy-legal-environment/accounting-bba/ (sha256 5e05c1b99d2a)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `5bc3a8ca441c88a8` Marshall University — degree_requirements 2026-27 · program_key=music-education-prek-adult-b-a · requirement_key=course-requirements-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/music-prek-adult-ba/ (sha256 ce2426bbde6b)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: MUS 111 ⟵ “MUS 111 - Elementary Music Theory I”
  - courses: MUS 112 ⟵ “MUS 112 - Elementary Music Theory II”
  - courses: MUS 113 ⟵ “MUS 113 - Elem Aural Skills I”
  - courses: MUS 114 ⟵ “MUS 114 - Elem Aural Skills II”
  - courses: MUS 211 ⟵ “MUS 211 - Advanced Music Theory I”
  - courses: MUS 212 ⟵ “MUS 212 - Advanced Music Theory II”
  - courses: MUS 213 ⟵ “MUS 213 - Adv Aural Skills I”
  - courses: MUS 214 ⟵ “MUS 214 - Adv Aural Skills II”
  - courses: MUSP 226 ⟵ “MUSP 226 - Intro to Music Technology”
  - courses: MUSA 276 ⟵ “MUSA 276 - Sophomore Hearing”
  - courses: MUS 290 ⟵ “MUS 290 - Music History to 1750”
  - courses: MUS 301 ⟵ “MUS 301 - Analysis”
  - courses: MUS 315 ⟵ “MUS 315 - Basic Conducting”
  - courses: MUS 320 ⟵ “MUS 320 - Instrumental Arranging”
  - courses: MUS 360 ⟵ “MUS 360 - Music History 1730 - 1900”
  - courses: MUS 361 ⟵ “MUS 361 - Music History Since 1900”
  - courses: MUSA 376 ⟵ “MUSA 376 - Recital”
  - courses: MUS 415 ⟵ “MUS 415 - Advanced Conducting”
  - courses: MUSP 124 ⟵ “MUSP 124 - Class Piano IV”
  - courses: MUS 466 ⟵ “MUS 466 - Marching Thunder”
### `5f2c3207c2302a83` Marshall University — degree_requirements 2026-27 · program_key=music-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-ba/ (sha256 de0bb8ec5eb8)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
### `5feab3e1882a31f8` Marshall University — degree_requirements 2026-27 · program_key=accounting-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/accountancy-legal-environment/accounting-bba/ (sha256 5e05c1b99d2a)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `62428158ed9a0f50` Marshall University — degree_requirements 2026-27 · program_key=music-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-ba/ (sha256 de0bb8ec5eb8)
- issues: stale_year_label:2026-27
  - courses: MUS 497 ⟵ “MUS 497 - Capstone Project in Music”
### `632269ca612837e7` Marshall University — degree_requirements 2026-27 · program_key=sports-business-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/sports-business-bba/ (sha256 afeae013fa90)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `66720e51a9676293` Marshall University — degree_requirements 2026-27 · program_key=english-education-5-adult-b-a · requirement_key=english-education-5-adult-b-a-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-adult-ba/ (sha256 3edde6e32f12)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: EDF 200 ⟵ “EDF 200 - Pre-Residency Clinical”
  - courses: EDF 202 ⟵ “EDF 202 - Appl Clin Participation I”
  - courses: EDF 204 ⟵ “EDF 204 - Appl Clin Participation II”
  - courses: EDF 201 ⟵ “EDF 201 - Ed Psych Developing Learner”
  - courses: CISP 421 ⟵ “CISP 421 - Child with Exceptionalities”
  - courses: EDF 435 ⟵ “EDF 435 - Classroom Assessment”
  - courses: EDF 475 ⟵ “EDF 475 - Schools in a Diverse Society”
  - courses: CI 345 ⟵ “CI 345 - Crit Read Writ & Think”
  - courses: CI 402 ⟵ “CI 402 - Teach Mid Child Learners”
  - courses: CI 449 ⟵ “CI 449 - Instr & Clarm Mgt Sec Ed”
  - courses: CISP 422 ⟵ “CISP 422 - Differentiate Instruction”
  - courses: CI 470 ⟵ “CI 470 - Residency I Clinical”
  - courses: CI 451 ⟵ “CI 451 - Residency II - Secondary”
### `68b0ac8b6ab194c5` Marshall University — degree_requirements 2026-27 · program_key=sustainability-management-and-technology-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/energy-management-bba/ (sha256 295b58adcd67)
- issues: stale_year_label:2026-27
  - courses: MGT 325 ⟵ “MGT 325 - Project Management”
  - courses: MGT 370 ⟵ “MGT 370 - Energy Management Principles”
  - courses: MGT 380 ⟵ “MGT 380 - Principles of Renewable Energy”
  - courses: MGT 420 ⟵ “MGT 420 - Operations Management”
  - courses: MGT 428 ⟵ “MGT 428 - Negotiations”
  - courses: MGT 446 ⟵ “MGT 446 - Green Management”
  - courses: MKT 350 ⟵ “MKT 350 - Supply Chain Logistics”
  - courses: MGT 458 ⟵ “MGT 458 - Energy Management Strategy”
### `699150c11fa6a740` Marshall University — degree_requirements 2026-27 · program_key=health-care-management-b-b-a · requirement_key=course-requirements-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/health-care-management-bba/ (sha256 11c16303570e)
- issues: stale_year_label:2026-27
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management (cannot count as both the International Business Elective and a MGT elective)”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `6e919bc5793de3ae` Marshall University — degree_requirements 2026-27 · program_key=media-production-b-a · requirement_key=school-of-journalism-mass-communications-sojmc-program-requirements-media-produc [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/media-production-major/ (sha256 2ca78a1962ef)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: JMC 231 ⟵ “JMC 231 - Intro to Audio Production”
  - courses: JMC 332 ⟵ “JMC 332 - Intro to Video Production”
  - courses: JMC 475 ⟵ “JMC 475 - Documentary Journalism”
### `6e9edc9009c43f36` Marshall University — degree_requirements 2026-27 · program_key=theatre-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/theatre/theatre-ba/ (sha256 cf817f00c3e7)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
### `710836efeda19be4` Marshall University — degree_requirements 2026-27 · program_key=mathematics-education-5-adult-b-a · requirement_key=mathematics-education-5-adult-b-a-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-adult-ba/ (sha256 9c91dea8d549)
- issues: stale_year_label:2026-27
  - courses: MTH 491 ⟵ “MTH 491 - Senior Seminar”
### `71b197a8c8435283` Marshall University — degree_requirements 2026-27 · program_key=music-industry-b-a · requirement_key=music-industry-major-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-industry-ba/ (sha256 7d78ebd93c2f)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: MUS 142 ⟵ “MUS 142 - Music in Society”
  - courses: MUSP 101 ⟵ “MUSP 101 - Basic Musicianship”
  - courses: MUSP 110 ⟵ “MUSP 110 - The Professional Musician”
  - courses: MUSP 111 ⟵ “MUSP 111 - Elementary Music Theory I”
  - courses: MUSP 190 ⟵ “MUSP 190 - Aural Perceptions of Music Lit”
  - courses: MUSP 225 ⟵ “MUSP 225 - Intro to Music Industry”
  - courses: MUSP 226 ⟵ “MUSP 226 - Intro to Music Technology”
  - courses: MUSP 250 ⟵ “MUSP 250 - Digital Recording I”
  - courses: MUSP 325 ⟵ “MUSP 325 - Music Entrepreneurship”
  - courses: MUSP 326 ⟵ “MUSP 326 - Music Industry Law”
  - courses: MUSP 327 ⟵ “MUSP 327 - Music Business I”
  - courses: MUSP 475 ⟵ “MUSP 475 - Music Industry Capstone”
  - courses: MUSP 495 ⟵ “MUSP 495 - Music Internship”
### `747dcfd36234d2a3` Marshall University — degree_requirements 2026-27 · program_key=biological-science-education-9-adult-b-a · requirement_key=course-requirements-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/biological-science-9-adult-ba/ (sha256 9c8eb6e96f70)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MTH 122 ⟵ “MTH 122 - Plane Trigonometry”
  - courses: MTH 127 ⟵ “MTH 127 - College Algebra-Expanded”
  - courses: BSC 120 ⟵ “BSC 120 - Principles of Biology I”
  - courses: BSC 120L ⟵ “BSC 120L - Principles of Biology I Lab”
  - courses: BSC 121 ⟵ “BSC 121 - Principles of Biology II”
  - courses: BSC 121L ⟵ “BSC 121L - Prin of Biology II Lab”
  - courses: BSC 227 ⟵ “BSC 227 - Human Anatomy”
  - courses: BSC 227L ⟵ “BSC 227L - Human Anatomy Lab”
  - courses: BSC 302 ⟵ “BSC 302 - Principles of Microbiology”
  - courses: BSC 430 ⟵ “BSC 430 - Plant Ecology”
  - courses: BSC 460 ⟵ “BSC 460 - Conservation Biology”
  - courses: BSC 312 ⟵ “BSC 312 - Invertebrate Zoology”
  - courses: BSC 320 ⟵ “BSC 320 - Principles of Ecology”
  - courses: BSC 322 ⟵ “BSC 322 - Principles Cell Biology”
  - courses: BSC 324 ⟵ “BSC 324 - Principles of Genetics”
  - courses: BSC 416 ⟵ “BSC 416 - Plant Taxonomy”
  - courses: CHM 211 ⟵ “CHM 211 - Principles of Chemistry I”
  - courses: CHM 217 ⟵ “CHM 217 - Principles of Chem Lab I”
  - courses: CHM 212 ⟵ “CHM 212 - Principles Chemistry II”
  - courses: CHM 218 ⟵ “CHM 218 - Principles of Chem Lab II”
  - courses: GLY 200 ⟵ “GLY 200 - The Dynamic Earth”
  - courses: GLY 210L ⟵ “GLY 210L - Earth Materials Lab”
  - courses: PHY 201 ⟵ “PHY 201 - College Physics I”
  - courses: PHY 202 ⟵ “PHY 202 - General Physics I Laboratory”
  - courses: PS 325 ⟵ “PS 325 - Dev Scientific Thought”
  - … 1 more rows
### `752800d250db6281` Marshall University — degree_requirements 2026-27 · program_key=marketing-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/marketing-bba/ (sha256 a89f4c7b5103)
- issues: stale_year_label:2026-27
  - courses: MKT 231 ⟵ “MKT 231 - Principles of Selling”
  - courses: MKT 341 ⟵ “MKT 341 - Integrated MKT Communications”
  - courses: MKT 437 ⟵ “MKT 437 - Consumer Behavior”
  - courses: MKT 442 ⟵ “MKT 442 - Market Research”
  - courses: MKT 465 ⟵ “MKT 465 - Strategic Marketing”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `7813600130df16eb` Marshall University — degree_requirements 2026-27 · program_key=journalism-b-a · requirement_key=school-of-journalism-and-mass-communications-sojmc-program-requirements-journali [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/journalism-major/ (sha256 b19d2078960e)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: JMC 300 ⟵ “JMC 300 - Reporting and News Writing”
  - courses: JMC 458 ⟵ “JMC 458 - Emerging Media for Journalists”
  - courses: JMC 465 ⟵ “JMC 465 - Multimedia Reporting (Capstone)”
### `79cb5ff2da3ea8c5` Marshall University — degree_requirements 2026-27 · program_key=special-education-multi-categorical-5-adult-b-a-second-specialization-only · requirement_key=course-requirements-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/multi-categorical-special-education-5-adult-ba/ (sha256 5283f23b41f2)
- issues: stale_year_label:2026-27
  - courses: CI 342 ⟵ “CI 342 - Lit & Lang Arts Methods”
  - courses: CI 343 ⟵ “CI 343 - The Process of Reading Part I”
  - courses: CI 446 ⟵ “CI 446 - The Process of Reading Part II”
  - courses: CISP 320 ⟵ “CISP 320 - Survey Exceptional Child”
  - courses: CISP 420 ⟵ “CISP 420 - Survey Except Child II”
  - courses: CISP 438 ⟵ “CISP 438 - Char/Behav Mild/Mod Disability”
  - courses: CISP 439 ⟵ “CISP 439 - Assessment in Sp Ed”
  - courses: CISP 453 ⟵ “CISP 453 - Curr Methods Mild to Moderate”
### `7fb2b57e85579eb3` Marshall University — degree_requirements 2026-27 · program_key=professional-pilot-b-s · requirement_key=course-requirements-required-aviation-flight-courses [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/commercial-pilot/ (sha256 bff59826ac1d)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: AVSC 200 ⟵ “AVSC 200 - Private Pilot Ground School”
  - courses: AVSC 205 ⟵ “AVSC 205 - Solo Flight Lab”
  - courses: AVSC 210 ⟵ “AVSC 210 - Private Pilot Cert ASEL Lab”
  - courses: AVSC 215 ⟵ “AVSC 215 - Instrument Ground School”
  - courses: AVSC 220 ⟵ “AVSC 220 - Instrument Certification Lab”
  - courses: AVSC 305 ⟵ “AVSC 305 - CFII Lab”
  - courses: AVSC 329 ⟵ “AVSC 329 - Commercial Ground School”
  - courses: AVSC 330 ⟵ “AVSC 330 - Commercial Phase I Lab”
  - courses: AVSC 335 ⟵ “AVSC 335 - CFI Ground School”
  - courses: AVSC 340 ⟵ “AVSC 340 - Commercial Phase II ASEL Lab”
  - courses: AVSC 345 ⟵ “AVSC 345 - Initial CFI ASEL Lab”
  - courses: AVSC 375 ⟵ “AVSC 375 - Commercial AMEL Add-On Lab”
### `804ec9b4aa4b459e` Marshall University — degree_requirements 2026-27 · program_key=management-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/management-bba/ (sha256 297ca1c10bd1)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `819c3463eb334afa` Marshall University — degree_requirements 2026-27 · program_key=journalism-b-a · requirement_key=school-of-journalism-and-mass-communications-sojmc-program-requirements-sojmc-co [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/journalism-major/ (sha256 b19d2078960e)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ANT 201 ⟵ “ANT 201 - Cultural Anthropology (CT)”
  - courses: GEO 100 ⟵ “GEO 100 - Intro to Human Geography (CT)”
  - courses: SOC 200 ⟵ “SOC 200 - Understanding Society (CT)”
### `824158f7e3d62306` Marshall University — degree_requirements 2026-27 · program_key=general-science-education-5-9-b-a-second-specialization-only · requirement_key=course-requirements-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/general-sciences-5-9-ba/ (sha256 309172c1129f)
- issues: stale_year_label:2026-27
  - courses: CI 402 ⟵ “CI 402 - Teach Mid Child Learners”
### `8320c47233b56a15` Marshall University — degree_requirements 2026-27 · program_key=music-education-prek-adult-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/music-prek-adult-ba/ (sha256 ce2426bbde6b)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
  - courses: ART 112 ⟵ “ART 112 - Intro To Visual Art (Fine Arts)”
### `843ca67513e4ad01` Marshall University — degree_requirements 2026-27 · program_key=sports-business-b-b-a · requirement_key=course-requirements-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/sports-business-bba/ (sha256 afeae013fa90)
- issues: stale_year_label:2026-27
  - courses: STHM 496 ⟵ “STHM 496 - Olympic Games”
### `84d99cc18d4f5cd2` Marshall University — degree_requirements 2026-27 · program_key=biological-science-education-9-adult-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/biological-science-9-adult-ba/ (sha256 9c8eb6e96f70)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 127 ⟵ “MTH 127 - College Algebra-Expanded”
  - courses: BSC 120 ⟵ “BSC 120 - Principles of Biology I”
  - courses: BSC 120L ⟵ “BSC 120L - Principles of Biology I Lab”
### `8534a9530a33f2f8` Marshall University — degree_requirements 2026-27 · program_key=sports-business-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/sports-business-bba/ (sha256 afeae013fa90)
- issues: stale_year_label:2026-27, course_alternatives_in_rule_text
  - courses: STHM 250 ⟵ “STHM 250 - Sport Management (CT)”
  - courses: STHM 380 ⟵ “STHM 380 - Sport Marketing”
  - courses: STHM 381 ⟵ “STHM 381 - Sport Finance/Economics”
  - courses: STHM 390 ⟵ “STHM 390 - Sport MGT Pre-Internship”
  - courses: STHM 416 ⟵ “STHM 416 - Facility Design & Management”
  - courses: STHM 475 ⟵ “STHM 475 - Capstone Seminar”
### `85b8e3e69dbf9903` Marshall University — degree_requirements 2026-27 · program_key=marketing-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/marketing-bba/ (sha256 a89f4c7b5103)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `86a355fe9a19b133` Marshall University — degree_requirements 2026-27 · program_key=accounting-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/accountancy-legal-environment/accounting-bba/ (sha256 5e05c1b99d2a)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `88c731282aa56517` Marshall University — degree_requirements 2026-27 · program_key=finance-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/finance-bba/ (sha256 9cefcfa0a87f)
- issues: stale_year_label:2026-27
  - courses: FIN 343 ⟵ “FIN 343 - Intermediate Financial Manage”
  - courses: FIN 370 ⟵ “FIN 370 - Principles of Investment”
  - courses: FIN 425 ⟵ “FIN 425 - Portfolio Analysis and Manage”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: FIN 470 ⟵ “FIN 470 - Financial Policies/Strategies”
### `8b6a4426eeaec4c7` Marshall University — degree_requirements 2026-27 · program_key=sustainability-management-and-technology-b-b-a · requirement_key=course-requirements-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/energy-management-bba/ (sha256 295b58adcd67)
- issues: stale_year_label:2026-27
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `8dc3e5eac1204bdc` Marshall University — degree_requirements 2026-27 · program_key=general-science-education-5-9-b-a-second-specialization-only · requirement_key=course-requirements-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/general-sciences-5-9-ba/ (sha256 309172c1129f)
- issues: stale_year_label:2026-27, course_alternatives_in_rule_text
  - courses: BSC 120 ⟵ “BSC 120 - Principles of Biology I”
  - courses: BSC 120L ⟵ “BSC 120L - Principles of Biology I Lab”
  - courses: BSC 121 ⟵ “BSC 121 - Principles of Biology II”
  - courses: BSC 121L ⟵ “BSC 121L - Prin of Biology II Lab”
  - courses: BSC 320 ⟵ “BSC 320 - Principles of Ecology”
  - courses: GLY 200 ⟵ “GLY 200 - The Dynamic Earth”
  - courses: GLY 210L ⟵ “GLY 210L - Earth Materials Lab”
  - courses: PS 101 ⟵ “PS 101 - Introductory Astronomy (CT)”
  - courses: CI 248 ⟵ “CI 248 - Intro to Science Elem Ed”
  - courses: CI 348 ⟵ “CI 348 - Phy Sci & Engr for Elem Ed”
  - courses: PS 325 ⟵ “PS 325 - Dev Scientific Thought”
### `8dd7952cdbda25ba` Marshall University — degree_requirements 2026-27 · program_key=music-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-ba/ (sha256 de0bb8ec5eb8)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
### `90e75e6c1eceb86a` Marshall University — degree_requirements 2026-27 · program_key=health-care-management-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/health-care-management-bba/ (sha256 11c16303570e)
- issues: stale_year_label:2026-27
  - courses: MGT 350 ⟵ “MGT 350 - Health Care Management”
  - courses: MGT 354 ⟵ “MGT 354 - Health Care Delivery Systems”
  - courses: MGT 355 ⟵ “MGT 355 - Health Care Prods & Services”
  - courses: MGT 424 ⟵ “MGT 424 - Human Resource Management”
  - courses: MGT 471 ⟵ “MGT 471 - Prac Health Care Mgt I”
  - courses: LE 351 ⟵ “LE 351 - Legal Aspts Hlth Care Org”
  - courses: MGT 455 ⟵ “MGT 455 - Hlth Care Policy Seminar”
### `91c40c23e3406bd7` Marshall University — degree_requirements 2026-27 · program_key=english-education-5-9-b-a-second-specialization-only · requirement_key=course-requirements-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-9-ba/ (sha256 9b70ab6738c4)
- issues: stale_year_label:2026-27, course_alternatives_in_rule_text
  - courses: ENG 350 ⟵ “ENG 350 - Intro to Textual Analysis”
  - courses: ENG 203 ⟵ “ENG 203 - Appalachian Literature”
  - courses: ENG 221 ⟵ “ENG 221 - Postcolonial Literature”
  - courses: ENG 240 ⟵ “ENG 240 - African American Literatures”
  - courses: ENG 241 ⟵ “ENG 241 - Multicultural Literatures”
  - courses: ENG 242 ⟵ “ENG 242 - Women Writers”
  - courses: ENG 410 ⟵ “ENG 410 - Shaks Com, Tragi & Rom”
  - courses: ENG 476 ⟵ “ENG 476 - Structures of English Language”
  - courses: ENG 409 ⟵ “ENG 409 - Milton”
  - courses: ENG 411 ⟵ “ENG 411 - Chaucer”
  - courses: ENG 421 ⟵ “ENG 421 - American Lit to 1830”
  - courses: ENG 422 ⟵ “ENG 422 - American Lit 1830-1865”
  - courses: ENG 436 ⟵ “ENG 436 - Medieval British Lit”
  - courses: ENG 414 ⟵ “ENG 414 - 19th C British Novel”
  - courses: ENG 415 ⟵ “ENG 415 - Victorian Poetry”
  - courses: ENG 416 ⟵ “ENG 416 - Victorian Nonfiction”
  - courses: ENG 423 ⟵ “ENG 423 - American Lit 1865-1914”
  - courses: ENG 424 ⟵ “ENG 424 - American Literature after 1914”
  - courses: ENG 433 ⟵ “ENG 433 - 20th C Brit & Irish Poetry”
  - courses: ENG 434 ⟵ “ENG 434 - 20th C American Poetry”
  - courses: ENG 447 ⟵ “ENG 447 - British Romantic Poets”
  - courses: ENG 428 ⟵ “ENG 428 - International Literature”
  - courses: ENG 450 ⟵ “ENG 450 - World Lit to Renaissance”
  - courses: ENG 451 ⟵ “ENG 451 - World Lit Since Renaissance”
  - courses: ENG 402 ⟵ “ENG 402 - Comp & Rhet Preservice Teacher”
  - … 2 more rows
### `9200872556716716` Marshall University — degree_requirements 2026-27 · program_key=accounting-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/accountancy-legal-environment/accounting-bba/ (sha256 5e05c1b99d2a)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: ACC 499 ⟵ “ACC 499 - Professional and Ethics Sem (Capstone)”
### `92a5427c2fa56e9d` Marshall University — degree_requirements 2026-27 · program_key=journalism-b-a · requirement_key=school-of-journalism-and-mass-communications-sojmc-program-requirements-sojmc-co-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/journalism-major/ (sha256 b19d2078960e)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: JMC 101 ⟵ “JMC 101 - Media Literacy”
  - courses: JMC 102 ⟵ “JMC 102 - Media Toolbox”
  - courses: JMC 103 ⟵ “JMC 103 - Language Use for Media (Recommended)”
  - courses: JMC 241 ⟵ “JMC 241 - Media Design”
  - courses: JMC 260 ⟵ “JMC 260 - Digital Imaging for JMC”
  - courses: JMC 345 ⟵ “JMC 345 - Mass Comm Law and Ethics”
  - courses: JMC 361 ⟵ “JMC 361 - Digital Presence”
  - courses: JMC 455 ⟵ “JMC 455 - Race Gender & Mass Media”
  - courses: JMC 490 ⟵ “JMC 490 - Jrn & Mass Comm Internship I”
  - courses: JMC 499 ⟵ “JMC 499 - Professional Portfolio”
### `92d825fe1bf967d5` Marshall University — degree_requirements 2026-27 · program_key=general-business-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/general-business-ba/ (sha256 0e499abb3987)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive) (capstone)”
### `9377c2c2b7c35de2` Marshall University — degree_requirements 2026-27 · program_key=special-education-multi-categorical-k-6-b-a-second-specialization-only · requirement_key=course-requirements-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/multi-categorical-special-education-k-6-ba-second/ (sha256 3e1de5a14e2d)
- issues: stale_year_label:2026-27
  - courses: CISP 320 ⟵ “CISP 320 - Survey Exceptional Child”
  - courses: CISP 420 ⟵ “CISP 420 - Survey Except Child II”
  - courses: CISP 438 ⟵ “CISP 438 - Char/Behav Mild/Mod Disability”
  - courses: CISP 439 ⟵ “CISP 439 - Assessment in Sp Ed”
  - courses: CISP 453 ⟵ “CISP 453 - Curr Methods Mild to Moderate”
### `96ae957788744230` Marshall University — degree_requirements 2026-27 · program_key=management-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/management-bba/ (sha256 297ca1c10bd1)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `97363b9baa1e3aac` Marshall University — degree_requirements 2026-27 · program_key=aviation-management-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: MGT 459 ⟵ “MGT 459 - Aviation Management Capstone”
### `97f5dc240db80584` Marshall University — degree_requirements 2026-27 · program_key=chemistry-education-9-adult-b-a · requirement_key=chemistry-education-9-adult-b-a-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/chemistry-9-adult-ba/ (sha256 9a3375dfca87)
- issues: stale_year_label:2026-27, course_alternatives_in_rule_text
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 127 ⟵ “MTH 127 - College Algebra-Expanded”
### `98c88ff7f7f7fa96` Marshall University — degree_requirements 2026-27 · program_key=finance-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/finance-bba/ (sha256 9cefcfa0a87f)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management (Multicultural or International)”
  - courses: FIN 470 ⟵ “FIN 470 - Financial Policies/Strategies (Capstone)”
### `9995745f25778528` Marshall University — degree_requirements 2026-27 · program_key=aviation-management-b-b-a · requirement_key=course-requirements-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `9ae4a843efac8f32` Marshall University — degree_requirements 2026-27 · program_key=entrepreneurship-b-b-a · requirement_key=course-requirements-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/entrepreneurship-bba/ (sha256 839ba8c56661)
- issues: stale_year_label:2026-27
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `9bf5b66216c0a86a` Marshall University — degree_requirements 2026-27 · program_key=management-information-systems-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/management-information-system-bba/ (sha256 fce4dc767b53)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `a3fd72bd9d19eb75` Marshall University — degree_requirements 2026-27 · program_key=mathematics-education-5-adult-b-a · requirement_key=mathematics-education-5-adult-b-a-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-adult-ba/ (sha256 9c91dea8d549)
- issues: stale_year_label:2026-27
  - courses: EDF 200 ⟵ “EDF 200 - Pre-Residency Clinical”
  - courses: EDF 202 ⟵ “EDF 202 - Appl Clin Participation I”
  - courses: EDF 204 ⟵ “EDF 204 - Appl Clin Participation II”
  - courses: EDF 201 ⟵ “EDF 201 - Ed Psych Developing Learner”
  - courses: CISP 421 ⟵ “CISP 421 - Child with Exceptionalities”
  - courses: EDF 435 ⟵ “EDF 435 - Classroom Assessment”
  - courses: EDF 475 ⟵ “EDF 475 - Schools in a Diverse Society”
  - courses: CI 345 ⟵ “CI 345 - Crit Read Writ & Think”
  - courses: CI 402 ⟵ “CI 402 - Teach Mid Child Learners”
  - courses: CI 415 ⟵ “CI 415 - Int Meth & Mat: Sec Ed”
  - courses: CI 449 ⟵ “CI 449 - Instr & Clarm Mgt Sec Ed”
  - courses: CISP 422 ⟵ “CISP 422 - Differentiate Instruction”
  - courses: CI 470 ⟵ “CI 470 - Residency I Clinical”
  - courses: CI 451 ⟵ “CI 451 - Residency II - Secondary”
### `a511fb8f95abfc8d` Marshall University — degree_requirements 2026-27 · program_key=general-business-b-a · requirement_key=course-requirements-communications-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/general-business-ba/ (sha256 0e499abb3987)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `a5c36c4fdb45fe43` Marshall University — degree_requirements 2026-27 · program_key=international-business-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/international-business-bba/ (sha256 2a29047baee1)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `a657cc977399f491` Marshall University — degree_requirements 2026-27 · program_key=art-b-a · requirement_key=ba-in-art-requirements-art-major [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/art-design/art-ba/ (sha256 b5ab0f178212)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ART 101 ⟵ “ART 101 - Visual Culture and Research”
  - courses: ART 201 ⟵ “ART 201 - History of Art I (CT)”
  - courses: ART 202 ⟵ “ART 202 - History of Art II (CT)”
### `a73f53eed1f18b4d` Marshall University — degree_requirements 2026-27 · program_key=music-education-prek-adult-b-a · requirement_key=course-requirements-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/music-prek-adult-ba/ (sha256 ce2426bbde6b)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: EDF 200 ⟵ “EDF 200 - Pre-Residency Clinical”
  - courses: EDF 202 ⟵ “EDF 202 - Appl Clin Participation I”
  - courses: EDF 204 ⟵ “EDF 204 - Appl Clin Participation II”
  - courses: EDF 201 ⟵ “EDF 201 - Ed Psych Developing Learner”
  - courses: CISP 421 ⟵ “CISP 421 - Child with Exceptionalities”
  - courses: CI 345 ⟵ “CI 345 - Crit Read Writ & Think”
  - courses: CI 449 ⟵ “CI 449 - Instr & Clarm Mgt Sec Ed”
  - courses: CISP 422 ⟵ “CISP 422 - Differentiate Instruction”
  - courses: EDF 475 ⟵ “EDF 475 - Schools in a Diverse Society”
  - courses: MUS 338 ⟵ “MUS 338 - Mat & Meth School Mus Pre K-4”
  - courses: MUS 339 ⟵ “MUS 339 - Mat & Meth Instru Mus 5-12”
  - courses: MUS 340 ⟵ “MUS 340 - Mat & Meth Chor Grn Mus 5-12”
  - courses: CI 472 ⟵ “CI 472 - Residency I Clinical”
  - courses: CI 451 ⟵ “CI 451 - Residency II - Secondary”
### `a92666e4144cbcd1` Marshall University — degree_requirements 2026-27 · program_key=entrepreneurship-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/entrepreneurship-bba/ (sha256 839ba8c56661)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `a956e408e4a50c67` Marshall University — degree_requirements 2026-27 · program_key=health-care-management-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/health-care-management-bba/ (sha256 11c16303570e)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `aa3270237592783e` Marshall University — degree_requirements 2026-27 · program_key=economics-b-b-a · requirement_key=major-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/economics-bba/ (sha256 0ebf21232ffc)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `acb156a0f7f0969b` Marshall University — degree_requirements 2026-27 · program_key=health-care-management-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/health-care-management-bba/ (sha256 11c16303570e)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `ad81e0c296c9707e` Marshall University — degree_requirements 2026-27 · program_key=general-science-education-5-adult-b-a · requirement_key=general-science-education-5-adult-b-a-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/general-sciences-5-adult-ba/ (sha256 f10930c2ff94)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: MTH 127 ⟵ “MTH 127 - College Algebra-Expanded”
  - courses: MTH 122 ⟵ “MTH 122 - Plane Trigonometry”
  - courses: BSC 120 ⟵ “BSC 120 - Principles of Biology I”
  - courses: BSC 120L ⟵ “BSC 120L - Principles of Biology I Lab”
  - courses: BSC 121 ⟵ “BSC 121 - Principles of Biology II”
  - courses: BSC 121L ⟵ “BSC 121L - Prin of Biology II Lab”
  - courses: BSC 320 ⟵ “BSC 320 - Principles of Ecology (or any Environmental Science course)”
  - courses: CHM 211 ⟵ “CHM 211 - Principles of Chemistry I”
  - courses: CHM 217 ⟵ “CHM 217 - Principles of Chem Lab I”
  - courses: CHM 212 ⟵ “CHM 212 - Principles Chemistry II”
  - courses: CHM 218 ⟵ “CHM 218 - Principles of Chem Lab II”
  - courses: GLY 200 ⟵ “GLY 200 - The Dynamic Earth”
  - courses: GLY 210L ⟵ “GLY 210L - Earth Materials Lab”
  - courses: PHY 201 ⟵ “PHY 201 - College Physics I”
  - courses: PHY 202 ⟵ “PHY 202 - General Physics I Laboratory”
  - courses: PHY 203 ⟵ “PHY 203 - College Physics II”
  - courses: PHY 204 ⟵ “PHY 204 - General Physics 2 Laboratory”
  - courses: PS 101 ⟵ “PS 101 - Introductory Astronomy (CT)”
  - courses: PS 325 ⟵ “PS 325 - Dev Scientific Thought”
### `ae166323fa7e4078` Marshall University — degree_requirements 2026-27 · program_key=media-production-b-a · requirement_key=school-of-journalism-mass-communications-sojmc-program-requirements-sojmc-cogniz [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/media-production-major/ (sha256 2ca78a1962ef)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ANT 201 ⟵ “ANT 201 - Cultural Anthropology (CT)”
  - courses: GEO 100 ⟵ “GEO 100 - Intro to Human Geography (CT)”
  - courses: SOC 200 ⟵ “SOC 200 - Understanding Society (CT)”
### `aeaf3ade885f8f16` Marshall University — degree_requirements 2026-27 · program_key=elementary-education-b-a · requirement_key=elementary-education-b-a-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/elementary-education-ba/ (sha256 cf1ced4029f1)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ART 335 ⟵ “ART 335 - Art Ed 2D-3D”
  - courses: CI 101 ⟵ “CI 101 - Math for Elem Teachers I”
  - courses: CI 201 ⟵ “CI 201 - Math for Elem Teachers II”
  - courses: CI 342 ⟵ “CI 342 - Lit & Lang Arts Methods”
  - courses: CI 343 ⟵ “CI 343 - The Process of Reading Part I”
  - courses: CI 446 ⟵ “CI 446 - The Process of Reading Part II”
  - courses: WELL 305 ⟵ “WELL 305 - HE & PE in Elementary Schools”
  - courses: GEO 317 ⟵ “GEO 317 - World Regional Geography”
  - courses: HST 103 ⟵ “HST 103 - The World Since 1850 (CT)”
  - courses: HST 230 ⟵ “HST 230 - American History to 1877 (CT)”
  - courses: HST 231 ⟵ “HST 231 - American Hist From 1877 (CT)”
  - courses: BSC 105 ⟵ “BSC 105 - Human Biology (& BSC 105L Human Biology Lab)”
  - courses: CI 248 ⟵ “CI 248 - Intro to Science Elem Ed”
  - courses: CI 340 ⟵ “CI 340 - Tch Creatively in Elem Classrm”
  - courses: CI 348 ⟵ “CI 348 - Phy Sci & Engr for Elem Ed”
### `afb76df93ba32ea7` Marshall University — degree_requirements 2026-27 · program_key=professional-pilot-b-s · requirement_key=course-requirements-general-education [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/commercial-pilot/ (sha256 bff59826ac1d)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: CMM 213 ⟵ “CMM 213 - Communication in Relationships (Recommended Core II)”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT) (Recommended Core II)”
### `b436e454e83e6a17` Marshall University — degree_requirements 2026-27 · program_key=international-business-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/international-business-bba/ (sha256 2a29047baee1)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `b63057bef04c43bf` Marshall University — degree_requirements 2026-27 · program_key=finance-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/finance-bba/ (sha256 9cefcfa0a87f)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `b7042044a1f0d3b3` Marshall University — degree_requirements 2026-27 · program_key=professional-pilot-b-s · requirement_key=course-requirements-required-management-course [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/commercial-pilot/ (sha256 bff59826ac1d)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: MGT 348 ⟵ “MGT 348 - Aviation Management Safety”
### `b736b04837706bbc` Marshall University — degree_requirements 2026-27 · program_key=professional-pilot-b-s · requirement_key=course-requirements-core-i-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/commercial-pilot/ (sha256 bff59826ac1d)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
### `b864c08cc8409ff4` Marshall University — degree_requirements 2026-27 · program_key=management-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/management-bba/ (sha256 297ca1c10bd1)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: MGT 419 ⟵ “MGT 419 - Business & Society (Capstone)”
### `bb1d81ec273325b7` Marshall University — degree_requirements 2026-27 · program_key=journalism-b-a · requirement_key=course-requirements-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/journalism-major/ (sha256 b19d2078960e)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
### `bc4f70794817be58` Marshall University — degree_requirements 2026-27 · program_key=marketing-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/marketing-bba/ (sha256 a89f4c7b5103)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing (Multicultural or International)”
  - courses: MKT 465 ⟵ “MKT 465 - Strategic Marketing (Capstone)”
### `bd2e827db6bc1f7c` Marshall University — degree_requirements 2026-27 · program_key=mathematics-education-5-adult-b-a · requirement_key=mathematics-education-5-adult-b-a-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-adult-ba/ (sha256 9c91dea8d549)
- issues: stale_year_label:2026-27
  - courses: MTH 229 ⟵ “MTH 229 - Calculus/Analytic Geom I (CT)”
  - courses: MTH 230 ⟵ “MTH 230 - Calculus/Analytic Geom II”
  - courses: MTH 231 ⟵ “MTH 231 - Calculus/Analytic Geom III”
  - courses: MTH 300 ⟵ “MTH 300 - Intro to Higher Math”
  - courses: MTH 310 ⟵ “MTH 310 - Math for Secondary Educators”
  - courses: MTH 311 ⟵ “MTH 311 - Math for Secondary Educators 2”
  - courses: MTH 331 ⟵ “MTH 331 - Linear Algebra”
  - courses: MTH 448 ⟵ “MTH 448 - Modern Geometries”
  - courses: MTH 450 ⟵ “MTH 450 - Modern Algebra I”
  - courses: MTH 452 ⟵ “MTH 452 - Modern Algebra II”
  - courses: MTH 491 ⟵ “MTH 491 - Senior Seminar”
  - courses: STA 445 ⟵ “STA 445 - Probability & Statistics I”
  - courses: STA 446 ⟵ “STA 446 - Probability & Statistics II”
### `bd907ba6777a069d` Marshall University — degree_requirements 2026-27 · program_key=general-business-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/general-business-ba/ (sha256 0e499abb3987)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `c15ebf7adc295b32` Marshall University — degree_requirements 2026-27 · program_key=health-care-management-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/health-care-management-bba/ (sha256 11c16303570e)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `c4d5a8c134cd8749` Marshall University — degree_requirements 2026-27 · program_key=music-industry-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-industry-ba/ (sha256 7d78ebd93c2f)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
### `c78c1540b88868c0` Marshall University — degree_requirements 2026-27 · program_key=management-information-systems-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/management-information-system-bba/ (sha256 fce4dc767b53)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition (Writing Intensive)”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `c8d92a898e8b8c73` Marshall University — degree_requirements 2026-27 · program_key=accounting-b-b-a · requirement_key=course-requirements-international-business-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/accountancy-legal-environment/accounting-bba/ (sha256 5e05c1b99d2a)
- issues: stale_year_label:2026-27
  - courses: ECN 408 ⟵ “ECN 408 - Comparative Econ Systems”
  - courses: ECN 420 ⟵ “ECN 420 - International Trade”
  - courses: ECN 421 ⟵ “ECN 421 - Global Macroeconomic Analysis”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries”
  - courses: FIN 440 ⟵ “FIN 440 - International Fin Management”
  - courses: MGT 445 ⟵ “MGT 445 - International Management”
  - courses: MKT 371 ⟵ “MKT 371 - International Marketing”
### `cc9e51747231a299` Marshall University — degree_requirements 2026-27 · program_key=theatre-b-a · requirement_key=course-requirements-theatre-major [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/theatre/theatre-ba/ (sha256 cf817f00c3e7)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: THE 101 ⟵ “THE 101 - Introduction to Theatre”
  - courses: THE 201 ⟵ “THE 201 - Crit Analysis Theatre Lit”
  - courses: THE 440 ⟵ “THE 440 - Theatre History To 1660”
  - courses: THE 441 ⟵ “THE 441 - Theatre Hist Since 1660”
  - courses: THE 499 ⟵ “THE 499 - Senior Capstone Project”
  - courses: THE 370 ⟵ “THE 370 - Theatre Practicum”
  - courses: THE 220 ⟵ “THE 220 - Stage Movement I: Foundations”
  - courses: THE 221 ⟵ “THE 221 - Stage Voice I: Foundations”
  - courses: THE 222 ⟵ “THE 222 - Acting I: Foundations”
  - courses: THE 240 ⟵ “THE 240 - Stage Lighting I”
  - courses: THE 330 ⟵ “THE 330 - Drafting & Rendering”
  - courses: THE 340 ⟵ “THE 340 - Stage Decor”
  - courses: THE 354 ⟵ “THE 354 - Stage Make-up”
### `cdb1e0c40442a272` Marshall University — degree_requirements 2026-27 · program_key=english-education-5-9-b-a-second-specialization-only · requirement_key=course-requirements-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-9-ba/ (sha256 9b70ab6738c4)
- issues: stale_year_label:2026-27
  - courses: CI 402 ⟵ “CI 402 - Teach Mid Child Learners”
### `d367d8cbee9fb71b` Marshall University — degree_requirements 2026-27 · program_key=economics-b-b-a · requirement_key=major-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/economics-bba/ (sha256 0ebf21232ffc)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `d7ae79dddc2e7d5a` Marshall University — degree_requirements 2026-27 · program_key=english-education-5-adult-b-a · requirement_key=english-education-5-adult-b-a-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-adult-ba/ (sha256 3edde6e32f12)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 350 ⟵ “ENG 350 - Intro to Textual Analysis”
  - courses: ENG 499 ⟵ “ENG 499 - Senior Capstone”
### `d8bda251211ffd72` Marshall University — degree_requirements 2026-27 · program_key=international-business-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/international-business-bba/ (sha256 2a29047baee1)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: ECN 460 ⟵ “ECN 460 - Economic of Dev Countries (Multicultural or International)”
  - courses: FIN 475 ⟵ “FIN 475 - Intl Business Strategies (Capstone)”
### `d8fbb739aefeaabc` Marshall University — degree_requirements 2026-27 · program_key=media-production-b-a · requirement_key=school-of-journalism-mass-communications-sojmc-program-requirements-sojmc-core-r [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/media-production-major/ (sha256 2ca78a1962ef)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: JMC 101 ⟵ “JMC 101 - Media Literacy”
  - courses: JMC 102 ⟵ “JMC 102 - Media Toolbox”
  - courses: JMC 103 ⟵ “JMC 103 - Language Use for Media (Recommended)”
  - courses: JMC 241 ⟵ “JMC 241 - Media Design”
  - courses: JMC 260 ⟵ “JMC 260 - Digital Imaging for JMC”
  - courses: JMC 345 ⟵ “JMC 345 - Mass Comm Law and Ethics”
  - courses: JMC 361 ⟵ “JMC 361 - Digital Presence”
  - courses: JMC 455 ⟵ “JMC 455 - Race Gender & Mass Media”
  - courses: JMC 490 ⟵ “JMC 490 - Jrn & Mass Comm Internship I”
  - courses: JMC 499 ⟵ “JMC 499 - Professional Portfolio”
### `da9d4dea06a64fa8` Marshall University — degree_requirements 2026-27 · program_key=chemistry-education-9-adult-b-a · requirement_key=chemistry-education-9-adult-b-a-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/chemistry-9-adult-ba/ (sha256 9a3375dfca87)
- issues: stale_year_label:2026-27
  - courses: EDF 200 ⟵ “EDF 200 - Pre-Residency Clinical”
  - courses: EDF 202 ⟵ “EDF 202 - Appl Clin Participation I”
  - courses: EDF 204 ⟵ “EDF 204 - Appl Clin Participation II”
  - courses: EDF 201 ⟵ “EDF 201 - Ed Psych Developing Learner”
  - courses: CISP 421 ⟵ “CISP 421 - Child with Exceptionalities”
  - courses: EDF 435 ⟵ “EDF 435 - Classroom Assessment”
  - courses: EDF 475 ⟵ “EDF 475 - Schools in a Diverse Society”
  - courses: CI 345 ⟵ “CI 345 - Crit Read Writ & Think”
  - courses: CI 449 ⟵ “CI 449 - Instr & Clarm Mgt Sec Ed”
  - courses: CISP 422 ⟵ “CISP 422 - Differentiate Instruction”
  - courses: CI 415 ⟵ “CI 415 - Int Meth & Mat: Sec Ed”
  - courses: CI 470 ⟵ “CI 470 - Residency I Clinical”
  - courses: CI 451 ⟵ “CI 451 - Residency II - Secondary”
### `dc3b43f593debb29` Marshall University — degree_requirements 2026-27 · program_key=art-education-prek-adult-b-a · requirement_key=course-requirements-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/art-prek-adult-ba/ (sha256 e7242f382920)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
  - courses: ART 112 ⟵ “ART 112 - Intro To Visual Art”
### `dc8fa8edad4d8e9d` Marshall University — degree_requirements 2026-27 · program_key=mathematics-education-5-9-b-a-second-specialization-only · requirement_key=course-requirements-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-9-ba/ (sha256 4800ec140164)
- issues: stale_year_label:2026-27, course_alternatives_in_rule_text
  - courses: MTH 122 ⟵ “MTH 122 - Plane Trigonometry”
  - courses: MTH 127 ⟵ “MTH 127 - College Algebra-Expanded”
  - courses: MTH 140 ⟵ “MTH 140 - Applied Calculus”
  - courses: MTH 220 ⟵ “MTH 220 - Discrete Structures”
  - courses: STA 225 ⟵ “STA 225 - Introductory Statistics (CT)”
  - courses: MTH 310 ⟵ “MTH 310 - Math for Secondary Educators”
  - courses: MTH 311 ⟵ “MTH 311 - Math for Secondary Educators 2”
  - courses: MTH 329 ⟵ “MTH 329 - Elementary Linear Algebra”
### `dea26626611ed219` Marshall University — degree_requirements 2026-27 · program_key=entrepreneurship-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/entrepreneurship-bba/ (sha256 839ba8c56661)
- issues: stale_year_label:2026-27
  - courses: ENT 220 ⟵ “ENT 220 - Creativity & Innovation”
  - courses: ENT 250 ⟵ “ENT 250 - Intro to Entrepreneurship”
  - courses: ENT 320 ⟵ “ENT 320 - Marketing for Entrepreneurs”
  - courses: ENT 350 ⟵ “ENT 350 - The Startup Experience”
  - courses: ENT 410 ⟵ “ENT 410 - Corporate Intrapreneurship”
  - courses: ENT 467 ⟵ “ENT 467 - Strategic Entrepreneurship”
  - courses: LE 366 ⟵ “LE 366 - Entrep Law & Ethics”
  - courses: MGT 461 ⟵ “MGT 461 - New Venture Dynamics”
### `debd2192c79f0323` Marshall University — degree_requirements 2026-27 · program_key=professional-pilot-b-s · requirement_key=course-requirements-required-aviation-core-courses [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/aviation/commercial-pilot/ (sha256 bff59826ac1d)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: AVSC 102 ⟵ “AVSC 102 - Flight School Orientation”
  - courses: AVSC 231 ⟵ “AVSC 231 - Aviation Law and Regulations”
  - courses: AVSC 310 ⟵ “AVSC 310 - Aerodynamics & Performance”
  - courses: AVSC 311 ⟵ “AVSC 311 - Aircraft Systems”
  - courses: AVSC 325 ⟵ “AVSC 325 - Evolution of ATC Systems”
  - courses: AVSC 355 ⟵ “AVSC 355 - Aviation Weather”
  - courses: AVSC 450 ⟵ “AVSC 450 - Crew Resource Management (Required Capstone)”
### `e111ba99bed6728a` Marshall University — degree_requirements 2026-27 · program_key=mathematics-education-5-adult-b-a · requirement_key=mathematics-education-5-adult-b-a-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/mathematics-5-adult-ba/ (sha256 9c91dea8d549)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 229 ⟵ “MTH 229 - Calculus/Analytic Geom I (CT)”
### `e267e77862100967` Marshall University — degree_requirements 2026-27 · program_key=journalism-b-a · requirement_key=course-requirements-core-1-critical-thiking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/journalism-major/ (sha256 b19d2078960e)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
### `e27623c7981c0117` Marshall University — degree_requirements 2026-27 · program_key=economics-b-b-a · requirement_key=major-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/economics-bba/ (sha256 0ebf21232ffc)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: ECN 466 ⟵ “ECN 466 - Economics Workshop (Capstone)”
### `e376e011d3c96c9c` Marshall University — degree_requirements 2026-27 · program_key=english-education-5-adult-b-a · requirement_key=english-education-5-adult-b-a-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-adult-ba/ (sha256 3edde6e32f12)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
### `e4a49363f17f41a4` Marshall University — degree_requirements 2026-27 · program_key=english-education-5-adult-b-a · requirement_key=english-education-5-adult-b-a-teaching-specialization [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/english-5-adult-ba/ (sha256 3edde6e32f12)
- issues: stale_year_label:2026-27, requirement_groups_skipped, course_alternatives_in_rule_text
  - courses: ENG 350 ⟵ “ENG 350 - Intro to Textual Analysis”
  - courses: ENG 355 ⟵ “ENG 355 - Intro to Critical Theory”
  - courses: ENG 203 ⟵ “ENG 203 - Appalachian Literature”
  - courses: ENG 221 ⟵ “ENG 221 - Postcolonial Literature”
  - courses: ENG 240 ⟵ “ENG 240 - African American Literatures”
  - courses: ENG 241 ⟵ “ENG 241 - Multicultural Literatures”
  - courses: ENG 242 ⟵ “ENG 242 - Women Writers”
  - courses: ENG 428 ⟵ “ENG 428 - International Literature”
  - courses: ENG 450 ⟵ “ENG 450 - World Lit to Renaissance”
  - courses: ENG 451 ⟵ “ENG 451 - World Lit Since Renaissance”
  - courses: ENG 410 ⟵ “ENG 410 - Shaks Com, Tragi & Rom”
  - courses: ENG 476 ⟵ “ENG 476 - Structures of English Language”
  - courses: ENG 421 ⟵ “ENG 421 - American Lit to 1830”
  - courses: ENG 422 ⟵ “ENG 422 - American Lit 1830-1865”
  - courses: ENG 423 ⟵ “ENG 423 - American Lit 1865-1914”
  - courses: ENG 424 ⟵ “ENG 424 - American Literature after 1914”
  - courses: ENG 432 ⟵ “ENG 432 - Contemporary Literature”
  - courses: ENG 434 ⟵ “ENG 434 - 20th C American Poetry”
  - courses: ENG 354 ⟵ “ENG 354 - Scientific & Tech Writing”
  - courses: ENG 360 ⟵ “ENG 360 - Intro Creative Writing”
  - courses: ENG 408 ⟵ “ENG 408 - Writing in the Digital World”
  - courses: ENG 402 ⟵ “ENG 402 - Comp & Rhet Preservice Teacher”
  - courses: ENG 419 ⟵ “ENG 419 - Approaches Teach Lit”
  - courses: ENG 430 ⟵ “ENG 430 - Young Adult Literature”
  - courses: ENG 499 ⟵ “ENG 499 - Senior Capstone”
### `e4b4180463181aa2` Marshall University — degree_requirements 2026-27 · program_key=economics-b-b-a · requirement_key=major-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/economics-bba/ (sha256 0ebf21232ffc)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `e5248091bb9c6ea5` Marshall University — degree_requirements 2026-27 · program_key=art-b-a · requirement_key=core-curriculum-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/art-design/art-ba/ (sha256 b5ab0f178212)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
### `e56ae2582f696193` Marshall University — degree_requirements 2026-27 · program_key=media-production-b-a · requirement_key=course-requirements-core-ii [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/journalism-mass-communication/media-production-major/ (sha256 2ca78a1962ef)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
### `e7ff2355b08f7c23` Marshall University — degree_requirements 2026-27 · program_key=sustainability-management-and-technology-b-b-a · requirement_key=course-requirements-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/energy-management-bba/ (sha256 295b58adcd67)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `e8617f8d37972efd` Marshall University — degree_requirements 2026-27 · program_key=entrepreneurship-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/entrepreneurship-bba/ (sha256 839ba8c56661)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `ebb691a4b442ded8` Marshall University — degree_requirements 2026-27 · program_key=accounting-b-b-a · requirement_key=course-requirements-communication-studies-elective [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/accountancy-legal-environment/accounting-bba/ (sha256 5e05c1b99d2a)
- issues: stale_year_label:2026-27
  - courses: CMM 302 ⟵ “CMM 302 - Professional Presentations”
  - courses: CMM 308 ⟵ “CMM 308 - Persuasive Communication”
  - courses: CMM 315 ⟵ “CMM 315 - Communication in Groups”
  - courses: CMM 319 ⟵ “CMM 319 - Leadership Dynamics”
  - courses: CMM 322 ⟵ “CMM 322 - Intercultural Communication”
### `ebcfb80dba289da6` Marshall University — degree_requirements 2026-27 · program_key=economics-b-b-a · requirement_key=major-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/economics-bba/ (sha256 0ebf21232ffc)
- issues: stale_year_label:2026-27
  - courses: ECN 326 ⟵ “ECN 326 - Int Macroeconomic Analys”
  - courses: ECN 328 ⟵ “ECN 328 - Int Microeconomic Analys”
  - courses: ECN 423 ⟵ “ECN 423 - Intro to Econometrics”
  - courses: ECN 466 ⟵ “ECN 466 - Economics Workshop”
### `ec4a8f35592006c7` Marshall University — degree_requirements 2026-27 · program_key=finance-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/finance-economics-international-business/finance-bba/ (sha256 9cefcfa0a87f)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `ee7afb7cdc0203e9` Marshall University — degree_requirements 2026-27 · program_key=biological-science-education-9-adult-b-a · requirement_key=course-requirements-professional-education-core [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/biological-science-9-adult-ba/ (sha256 9c8eb6e96f70)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: EDF 200 ⟵ “EDF 200 - Pre-Residency Clinical”
  - courses: EDF 202 ⟵ “EDF 202 - Appl Clin Participation I”
  - courses: EDF 204 ⟵ “EDF 204 - Appl Clin Participation II”
  - courses: EDF 201 ⟵ “EDF 201 - Ed Psych Developing Learner”
  - courses: CISP 421 ⟵ “CISP 421 - Child with Exceptionalities”
  - courses: EDF 435 ⟵ “EDF 435 - Classroom Assessment”
  - courses: EDF 475 ⟵ “EDF 475 - Schools in a Diverse Society”
  - courses: CI 345 ⟵ “CI 345 - Crit Read Writ & Think”
  - courses: CI 449 ⟵ “CI 449 - Instr & Clarm Mgt Sec Ed”
  - courses: CISP 422 ⟵ “CISP 422 - Differentiate Instruction”
  - courses: CI 415 ⟵ “CI 415 - Int Meth & Mat: Sec Ed”
  - courses: CI 470 ⟵ “CI 470 - Residency I Clinical”
  - courses: CI 451 ⟵ “CI 451 - Residency II - Secondary”
### `eef23f3d54249a46` Marshall University — degree_requirements 2026-27 · program_key=art-b-a · requirement_key=core-curriculum-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/art-design/art-ba/ (sha256 b5ab0f178212)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 103 ⟵ “CMM 103 - Fund Speech-Communication”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
### `f09609432802414c` Marshall University — degree_requirements 2026-27 · program_key=aviation-management-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
  - courses: AVSC 231 ⟵ “AVSC 231 - Aviation Law and Regulations”
  - courses: AVSC 315 ⟵ “AVSC 315 - Airport Operations and Mgmt”
  - courses: AVSC 410 ⟵ “AVSC 410 - Air Transportation Operations”
  - courses: MGT 348 ⟵ “MGT 348 - Aviation Management Safety”
  - courses: MGT 420 ⟵ “MGT 420 - Operations Management”
  - courses: MGT 422 ⟵ “MGT 422 - Organizational Behavior”
  - courses: MGT 424 ⟵ “MGT 424 - Human Resource Management”
  - courses: MGT 459 ⟵ “MGT 459 - Aviation Management Capstone”
### `f1c3c77d4812c0a4` Marshall University — degree_requirements 2026-27 · program_key=aviation-management-b-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/aviation-management-bba/ (sha256 774f15116258)
- issues: stale_year_label:2026-27
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
### `f3888bf8f85dd90e` Marshall University — degree_requirements 2026-27 · program_key=entrepreneurship-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/entrepreneurship-bba/ (sha256 839ba8c56661)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: ENT 467 ⟵ “ENT 467 - Strategic Entrepreneurship (Capstone)”
### `f681347a84f3f542` Marshall University — degree_requirements 2026-27 · program_key=management-b-b-a · requirement_key=course-requirements-major-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/management-health-care-administration/management-bba/ (sha256 297ca1c10bd1)
- issues: stale_year_label:2026-27
  - courses: MGT 420 ⟵ “MGT 420 - Operations Management”
  - courses: MGT 422 ⟵ “MGT 422 - Organizational Behavior”
  - courses: MGT 424 ⟵ “MGT 424 - Human Resource Management”
  - courses: MGT 419 ⟵ “MGT 419 - Business & Society”
### `f7f849b58fac534f` Marshall University — degree_requirements 2026-27 · program_key=sports-business-b-b-a · requirement_key=course-requirements-college-specific [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/sports-business-bba/ (sha256 afeae013fa90)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace”
  - courses: ACC 215 ⟵ “ACC 215 - Intro Financial Accounting(CT)”
  - courses: ACC 216 ⟵ “ACC 216 - Intro Managerial Accounting”
  - courses: ECN 250 ⟵ “ECN 250 - Principles Microeconomics”
  - courses: ECN 253 ⟵ “ECN 253 - Principles Macroeconomics”
  - courses: FIN 323 ⟵ “FIN 323 - Principles of Finance”
  - courses: LE 207 ⟵ “LE 207 - Legal Environ of Business”
  - courses: MIS 200 ⟵ “MIS 200 - Bus Computer Applications”
  - courses: MIS 290 ⟵ “MIS 290 - Prin Management Info Systems”
  - courses: MGT 218 ⟵ “MGT 218 - Business Quantitative Methods”
  - courses: MGT 320 ⟵ “MGT 320 - Principles of Management”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management”
  - courses: MKT 340 ⟵ “MKT 340 - MKT Concepts and Applications”
### `f8f20e6acb3cbc68` Marshall University — degree_requirements 2026-27 · program_key=music-industry-b-a · requirement_key=music-industry-major-requirements-musa-1xx [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-industry-ba/ (sha256 7d78ebd93c2f)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: MUSP 121 ⟵ “MUSP 121 - Class Piano I”
  - courses: MUSP 126 ⟵ “MUSP 126 - Class Voice”
  - courses: MUSP 127 ⟵ “MUSP 127 - Class Guitar”
  - courses: MUS 200 ⟵ “MUS 200 - Introduction to World Music”
  - courses: MUS 227 ⟵ “MUS 227 - History of Popular Music”
  - courses: MUS 250 ⟵ “MUS 250 - History of Jazz”
### `fbdd8244f881cd00` Marshall University — degree_requirements 2026-27 · program_key=entrepreneurship-b-b-a · requirement_key=course-requirements-core-2 [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/entrepreneurship-bba/ (sha256 839ba8c56661)
- issues: stale_year_label:2026-27
  - courses: ENG 101 ⟵ “ENG 101 - Beginning Composition”
  - courses: ENG 201 ⟵ “ENG 201 - Advanced Composition”
  - courses: CMM 207 ⟵ “CMM 207 - Business Communication”
  - courses: STA 150 ⟵ “STA 150 - Foundations of Statistics”
  - courses: STA 150L ⟵ “STA 150L - Foundations of Statistics Lab”
  - courses: PSY 201 ⟵ “PSY 201 - Introductory Psychology (CT)”
### `fd5b6c7cf0918e79` Marshall University — degree_requirements 2026-27 · program_key=management-information-systems-b-b-a · requirement_key=course-requirements-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/business/marketing-mis-entrepreneurship/management-information-system-bba/ (sha256 fce4dc767b53)
- issues: stale_year_label:2026-27
  - courses: ENG 204 ⟵ “ENG 204 - Writing for the Workplace (Writing Intensive)”
  - courses: MGT 460 ⟵ “MGT 460 - Strategic Management (Writing Intensive)”
  - courses: MIS 475 ⟵ “MIS 475 - Strat Management Info Systems (Capstone)”
### `fe09c036e77c3084` Marshall University — degree_requirements 2026-27 · program_key=music-b-a · requirement_key=course-requirements-major-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/arts-media/music/music-ba/ (sha256 de0bb8ec5eb8)
- issues: stale_year_label:2026-27, course_alternatives_in_rule_text
  - courses: MUSP 110 ⟵ “MUSP 110 - The Professional Musician”
  - courses: MUSP 111 ⟵ “MUSP 111 - Elementary Music Theory I”
  - courses: MUSP 112 ⟵ “MUSP 112 - Elementary Music Theory II”
  - courses: MUSP 113 ⟵ “MUSP 113 - Elem Aural Skills I”
  - courses: MUSP 114 ⟵ “MUSP 114 - Elem Aural Skills II”
  - courses: MUS 211 ⟵ “MUS 211 - Advanced Music Theory I”
  - courses: MUS 213 ⟵ “MUS 213 - Adv Aural Skills I”
  - courses: MUSP 226 ⟵ “MUSP 226 - Intro to Music Technology”
  - courses: MUSP 325 ⟵ “MUSP 325 - Music Entrepreneurship”
  - courses: MUS 497 ⟵ “MUS 497 - Capstone Project in Music”
  - courses: MUS 212 ⟵ “MUS 212 - Advanced Music Theory II”
  - courses: MUS 214 ⟵ “MUS 214 - Adv Aural Skills II”
  - courses: MUSA 276 ⟵ “MUSA 276 - Sophomore Hearing”
  - courses: MUS 290 ⟵ “MUS 290 - Music History to 1750”
  - courses: MUS 360 ⟵ “MUS 360 - Music History 1730 - 1900”
  - courses: MUSP 121 ⟵ “MUSP 121 - Class Piano I”
  - courses: MUSP 122 ⟵ “MUSP 122 - Class Piano II”
  - courses: MUSP 123 ⟵ “MUSP 123 - Class Piano III”
  - courses: MUSP 124 ⟵ “MUSP 124 - Class Piano IV”
  - courses: MUS 100 ⟵ “MUS 100 - Applied Music Laboratory (6 semesters)”
### `fe7f248628e95b3a` Marshall University — degree_requirements 2026-27 · program_key=music-education-prek-adult-b-a · requirement_key=course-requirements-core-1-critical-thinking [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/music-prek-adult-ba/ (sha256 ce2426bbde6b)
- issues: stale_year_label:2026-27, requirement_groups_skipped
  - courses: FYS 100 ⟵ “FYS 100 - First Yr Sem Critical Thinking”
  - courses: MTH 121 ⟵ “MTH 121 - Concepts and Applications (CT)”
### `ff2d2440411251e8` Marshall University — degree_requirements 2026-27 · program_key=chemistry-education-9-adult-b-a · requirement_key=chemistry-education-9-adult-b-a-additional-university-requirements [new] (labeled_in_source)
- source: https://catalog.marshall.edu/undergraduate/programs-az/education-professional-development/curriculum-instruction-foundations/chemistry-9-adult-ba/ (sha256 9a3375dfca87)
- issues: stale_year_label:2026-27
  - courses: CHM 481 ⟵ “CHM 481 - Special Topics (Capstone)”
### `ae49eb79d618cda7` Marshall University — transfer_policies 2025-26 [new] (labeled_in_source)
- source: https://www.marshall.edu/admissions/transfer/ (sha256 d754103525aa)
- issues: stale_year_label:2025-26
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 72 ⟵ “General Curriculum Requirements Students may transfer no more than 72 credit hours completed at one or more community colleges.”
### `7081478577801752` Mountwest Community and Technical College — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.mctc.edu/paying-for-college/ (sha256 b750de976b45)
- issues: residency_unknown
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Books & Supplies: 1570 ⟵ “Books & Supplies | 1,570 | 1,570 | 1,570 | 1,570 | 1,570”
  - with_parents_or_family:Average Loan Fee: 36 ⟵ “Average Loan Fee | 36 | 36 | 36 | 36 | 36”
  - with_parents_or_family:Misc./Personal Expenses: 1330 ⟵ “Misc./Personal Expenses | 1,330 | 1,565 | 1,330 | 1,565 | 1,565”
  - with_parents_or_family:Housing & Food: 6118 ⟵ “Housing & Food | 6,118 | 10,197 | 6,118 | 10,197 | 10,197”
  - with_parents_or_family:Average Tuition & Fees: 10700 ⟵ “Average Tuition & Fees | 6,436 | 6,436 | 10,700 | 10,700 | 13,720”
  - with_parents_or_family:Transportation: 3219 ⟵ “Transportation | 3,219 | 3,219 | 3,219 | 3,219 | 3,219”
  - with_parents_or_family:Total: 22973 ⟵ “Total | 18,709 | 23,023 | 22,973 | 27,287 | 30,307”
  - off_campus_not_with_family:Books & Supplies: 1570 ⟵ “Books & Supplies | 1,570 | 1,570 | 1,570 | 1,570 | 1,570”
  - off_campus_not_with_family:Average Loan Fee: 36 ⟵ “Average Loan Fee | 36 | 36 | 36 | 36 | 36”
  - off_campus_not_with_family:Misc./Personal Expenses: 1565 ⟵ “Misc./Personal Expenses | 1,330 | 1,565 | 1,330 | 1,565 | 1,565”
  - off_campus_not_with_family:Housing & Food: 10197 ⟵ “Housing & Food | 6,118 | 10,197 | 6,118 | 10,197 | 10,197”
  - off_campus_not_with_family:Average Tuition & Fees: 10700 ⟵ “Average Tuition & Fees | 6,436 | 6,436 | 10,700 | 10,700 | 13,720”
  - off_campus_not_with_family:Transportation: 3219 ⟵ “Transportation | 3,219 | 3,219 | 3,219 | 3,219 | 3,219”
  - off_campus_not_with_family:Total: 27287 ⟵ “Total | 18,709 | 23,023 | 22,973 | 27,287 | 30,307”
### `2c350473ea57c956` Pierpont Community and Technical College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.pierpont.edu/wp-content/uploads/2024/05/2024-2025-Satisfactory-Academic-Progress-Appeal-Form.pdf (sha256 ed63bb7ee93a)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You may submit a Satisfactory Academic Progress Appeal for extenuating circumstances: (Please check one) _____ Serious illness or injury that required extended recovery time _____ Death or serious illness of an immediate family member _____ Significant trauma that impaired your emotional and/or physical health _____ Other documented circumstances (Explain: _________________________________________”
  - sentence: sap_appeal ⟵ “You must submit a completed SAP Appeal.”
### `35f527ff4640627d` Pierpont Community and Technical College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.pierpont.edu/wp-content/uploads/2025/03/2025-2026-Satisfactory-Academic-Progress-Appeal-Form.pdf (sha256 9c3680a898f9)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You may submit a Satisfactory Academic Progress Appeal for extenuating circumstances: (Please check one) _____ Serious illness or injury that required extended recovery time _____ Death or serious illness of an immediate family member _____ Significant trauma that impaired your emotional and/or physical health _____ Other documented circumstances (Explain: _________________________________________”
  - sentence: sap_appeal ⟵ “You must submit a completed SAP Appeal.”
### `7946d1d4b6f3574f` Pierpont Community and Technical College — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.pierpont.edu/wp-content/uploads/2026/06/2026-2027-Satisfactory-Academic-Progress-Appeal-Form.pdf (sha256 6d66ff4c18ec)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “You may submit a Satisfactory Academic Progress Appeal for extenuating circumstances: (Please check one) _____ Serious illness or injury that required extended recovery time _____ Death or serious illness of an immediate family member _____ Significant trauma that impaired your emotional and/or physical health _____ Other documented circumstances (Explain: _________________________________________”
  - sentence: sap_appeal ⟵ “You must submit a completed SAP Appeal.”
### `833aecd60e1b9edc` Pierpont Community and Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.pierpont.edu/cost-aid/financial-aid/special-cases/ (sha256 9a7fc4dc7025)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Special Circumstances An aid administrator may use Professional Judgement on a case-by-case basis to adjust the student’s cost of attendance or the data used to calculate his or her EFC.”
### `b3df81e8e146e394` Pierpont Community and Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.pierpont.edu/cost-aid/financial-aid/resources/financial-aid-faqs/ (sha256 2ee7c42a8415)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.pierpont.edu/cost-aid/financial-aid/special-cases/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Examples of extenuating circumstances are death of immediate family member, injury or illness or other unusual circumstances evaluated by the Office of Financial Aid and Scholarships.”
### `c225f7982aa5d606` Pierpont Community and Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.pierpont.edu/cost-aid/financial-aid/special-cases/ (sha256 9a7fc4dc7025)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://www.pierpont.edu/cost-aid/financial-aid/resources/financial-aid-faqs/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “The law gives some examples of special circumstances that MAY be considered (HEA Sec. 479A) Change in employment status, income, or assets Change in housing status (e.g., homelessness) Tuition expenses at an elementary or secondary school Medical, dental, or nursing home expenses not covered by insurance Child or dependent care expenses Severe disability of the student or other member of the stude”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances do include: Human trafficking, as described in the Trafficking Victims Protection Act of 2000 (22 U.S.C. 7101 et seq.); Legally granted refugee or asylum status; Parental abandonment or estrangement; or Student or parental incarceration.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances do not include: Parents refuse to contribute to the student’s education.”
### `b1a1379181e69983` Pierpont Community and Technical College — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.pierpont.edu/cost-aid/cost/cost-of-attendance-budget/ (sha256 5df5f52cc4d2)
- issues: components_do_not_reconcile
- checks: {"columns": 3, "components_reconcile": false, "rows": 8}
  - off_campus_not_with_family:Tuition and Fees ($395 Tech Fee not included yet): 2881 ⟵ “Tuition and Fees ($395 Tech Fee not included yet) | T+F | $2,881 | $2,881 | $5,762 |  | $6,830 | $6,830 | $13,660”
  - off_campus_not_with_family:Books & Supplies: 624 ⟵ “Books & Supplies | B+S | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Room and Board = Housing + Meals below: 5996 ⟵ “Room and Board = Housing + Meals below |  | $5,996 | $5,996 | $11,992 |  | $5,996 | $5,996 | $11,992”
  - off_campus_not_with_family:Housing: 3475 ⟵ “Housing | HOUS | $3,475 | $3,475 | $6,950 |  | $3,475 | $3,475 | $6,950”
  - off_campus_not_with_family:Meals: 2521 ⟵ “Meals | MEAL | $2,521 | $2,521 | $5,042 |  | $2,521 | $2,521 | $5,042”
  - off_campus_not_with_family:Transportation: 624 ⟵ “Transportation | TRAN | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Personal: 624 ⟵ “Personal | PERS | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Total: 10749 ⟵ “Total |  | $10,749 | $10,749 | $21,498 |  | $14,698 | $14,698 | $29,396”
  - off_campus_not_with_family:Tuition and Fees ($395 Tech Fee not included yet): 2881 ⟵ “Tuition and Fees ($395 Tech Fee not included yet) | T+F | $2,881 | $2,881 | $5,762 |  | $6,830 | $6,830 | $13,660”
  - off_campus_not_with_family:Books & Supplies: 624 ⟵ “Books & Supplies | B+S | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Room and Board = Housing + Meals below: 5996 ⟵ “Room and Board = Housing + Meals below |  | $5,996 | $5,996 | $11,992 |  | $5,996 | $5,996 | $11,992”
  - off_campus_not_with_family:Housing: 3475 ⟵ “Housing | HOUS | $3,475 | $3,475 | $6,950 |  | $3,475 | $3,475 | $6,950”
  - off_campus_not_with_family:Meals: 2521 ⟵ “Meals | MEAL | $2,521 | $2,521 | $5,042 |  | $2,521 | $2,521 | $5,042”
  - off_campus_not_with_family:Transportation: 624 ⟵ “Transportation | TRAN | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Personal: 624 ⟵ “Personal | PERS | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Total: 10749 ⟵ “Total |  | $10,749 | $10,749 | $21,498 |  | $14,698 | $14,698 | $29,396”
  - off_campus_not_with_family:Tuition and Fees ($395 Tech Fee not included yet): 5762 ⟵ “Tuition and Fees ($395 Tech Fee not included yet) | T+F | $2,881 | $2,881 | $5,762 |  | $6,830 | $6,830 | $13,660”
  - off_campus_not_with_family:Books & Supplies: 1248 ⟵ “Books & Supplies | B+S | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Room and Board = Housing + Meals below: 11992 ⟵ “Room and Board = Housing + Meals below |  | $5,996 | $5,996 | $11,992 |  | $5,996 | $5,996 | $11,992”
  - off_campus_not_with_family:Housing: 6950 ⟵ “Housing | HOUS | $3,475 | $3,475 | $6,950 |  | $3,475 | $3,475 | $6,950”
  - off_campus_not_with_family:Meals: 5042 ⟵ “Meals | MEAL | $2,521 | $2,521 | $5,042 |  | $2,521 | $2,521 | $5,042”
  - off_campus_not_with_family:Transportation: 1248 ⟵ “Transportation | TRAN | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Personal: 1248 ⟵ “Personal | PERS | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Total: 21498 ⟵ “Total |  | $10,749 | $10,749 | $21,498 |  | $14,698 | $14,698 | $29,396”
### `fb98d51ae23656d7` Pierpont Community and Technical College — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.pierpont.edu/cost-aid/cost/cost-of-attendance-budget/ (sha256 9a48bcc1d530)
- issues: components_do_not_reconcile
- checks: {"columns": 3, "components_reconcile": false, "rows": 8}
  - off_campus_not_with_family:Tuition and Fees ($395 Tech Fee not included yet): 6830 ⟵ “Tuition and Fees ($395 Tech Fee not included yet) | T+F | $2,881 | $2,881 | $5,762 |  | $6,830 | $6,830 | $13,660”
  - off_campus_not_with_family:Books & Supplies: 624 ⟵ “Books & Supplies | B+S | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Room and Board = Housing + Meals below: 5996 ⟵ “Room and Board = Housing + Meals below |  | $5,996 | $5,996 | $11,992 |  | $5,996 | $5,996 | $11,992”
  - off_campus_not_with_family:Housing: 3475 ⟵ “Housing | HOUS | $3,475 | $3,475 | $6,950 |  | $3,475 | $3,475 | $6,950”
  - off_campus_not_with_family:Meals: 2521 ⟵ “Meals | MEAL | $2,521 | $2,521 | $5,042 |  | $2,521 | $2,521 | $5,042”
  - off_campus_not_with_family:Transportation: 624 ⟵ “Transportation | TRAN | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Personal: 624 ⟵ “Personal | PERS | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Total: 14698 ⟵ “Total |  | $10,749 | $10,749 | $21,498 |  | $14,698 | $14,698 | $29,396”
  - off_campus_not_with_family:Tuition and Fees ($395 Tech Fee not included yet): 6830 ⟵ “Tuition and Fees ($395 Tech Fee not included yet) | T+F | $2,881 | $2,881 | $5,762 |  | $6,830 | $6,830 | $13,660”
  - off_campus_not_with_family:Books & Supplies: 624 ⟵ “Books & Supplies | B+S | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Room and Board = Housing + Meals below: 5996 ⟵ “Room and Board = Housing + Meals below |  | $5,996 | $5,996 | $11,992 |  | $5,996 | $5,996 | $11,992”
  - off_campus_not_with_family:Housing: 3475 ⟵ “Housing | HOUS | $3,475 | $3,475 | $6,950 |  | $3,475 | $3,475 | $6,950”
  - off_campus_not_with_family:Meals: 2521 ⟵ “Meals | MEAL | $2,521 | $2,521 | $5,042 |  | $2,521 | $2,521 | $5,042”
  - off_campus_not_with_family:Transportation: 624 ⟵ “Transportation | TRAN | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Personal: 624 ⟵ “Personal | PERS | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Total: 14698 ⟵ “Total |  | $10,749 | $10,749 | $21,498 |  | $14,698 | $14,698 | $29,396”
  - off_campus_not_with_family:Tuition and Fees ($395 Tech Fee not included yet): 13660 ⟵ “Tuition and Fees ($395 Tech Fee not included yet) | T+F | $2,881 | $2,881 | $5,762 |  | $6,830 | $6,830 | $13,660”
  - off_campus_not_with_family:Books & Supplies: 1248 ⟵ “Books & Supplies | B+S | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Room and Board = Housing + Meals below: 11992 ⟵ “Room and Board = Housing + Meals below |  | $5,996 | $5,996 | $11,992 |  | $5,996 | $5,996 | $11,992”
  - off_campus_not_with_family:Housing: 6950 ⟵ “Housing | HOUS | $3,475 | $3,475 | $6,950 |  | $3,475 | $3,475 | $6,950”
  - off_campus_not_with_family:Meals: 5042 ⟵ “Meals | MEAL | $2,521 | $2,521 | $5,042 |  | $2,521 | $2,521 | $5,042”
  - off_campus_not_with_family:Transportation: 1248 ⟵ “Transportation | TRAN | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Personal: 1248 ⟵ “Personal | PERS | $624 | $624 | $1,248 |  | $624 | $624 | $1,248”
  - off_campus_not_with_family:Total: 29396 ⟵ “Total |  | $10,749 | $10,749 | $21,498 |  | $14,698 | $14,698 | $29,396”
### `652836d2e1a2d7c3` Shepherd University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.shepherd.edu/financialaid/sap (sha256 bcde4e1b32a3)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Deadlines: Summer 2026 Semester – 05/20/2026 Fall 2026 Semester – 08/14/2026 Spring 2027 Semester – 01/05/2027 Forms: Satisfactory Academic Progress (SAP) Appeal Process Satisfactory Academic Progress (SAP) Appeal Form – Level 1 Satisfactory Academic Progress (SAP) Appeal Form – Level 2 Student Statement Form Academic Plan for Progress (APP) Examples of Extenuating Circumstances and Support”
### `1b68f860e7d0de19` Shepherd University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.shepherd.edu/admissions/first-time-freshman-scholarships/ (sha256 5bc3dffc237f)
- issues: conflicting_sources:https://www.shepherd.edu/financialaid/scholarships
- checks: {"thresholds": {"act_min": 27, "gpa_min": 3.75, "sat_min": 1300}}
  - gpa_requirement: 3.75+ ⟵ “President’s Scholarship | 3.75+ | 1300+ | 27+ | $3,000 | $5,000”
  - test_requirement: ACT 27+ / SAT 1300+ ⟵ “President’s Scholarship | 3.75+ | 1300+ | 27+ | $3,000 | $5,000”
### `543e59ccd7023ef8` Shepherd University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.shepherd.edu/financialaid/scholarships (sha256 812e54e5c98a)
- issues: conflicting_sources:https://www.shepherd.edu/admissions/first-time-freshman-scholarships/
- checks: {"thresholds": null}
  - gpa_requirement: 3.50-3.74 ⟵ “Dean’s Scholarship | 3.50-3.74 | 1,200-1,290 |  | 24-26 | $2,000 | $4,000”
  - test_requirement: ACT 24-26 / SAT 1,200-1,290 ⟵ “Dean’s Scholarship | 3.50-3.74 | 1,200-1,290 |  | 24-26 | $2,000 | $4,000”
### `55630cdb1053a502` Shepherd University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.shepherd.edu/financialaid/scholarships (sha256 812e54e5c98a)
- issues: conflicting_sources:https://www.shepherd.edu/admissions/first-time-freshman-scholarships/
- checks: {"thresholds": {"act_min": 27, "gpa_min": 3.75}}
  - gpa_requirement: 3.75+ ⟵ “President’s Scholarship | 3.75+ | 1,300+ |  | 27+ | $3,000 | $5,000”
  - test_requirement: ACT 27+ / SAT 1,300+ ⟵ “President’s Scholarship | 3.75+ | 1,300+ |  | 27+ | $3,000 | $5,000”
### `b4132d4d7f8e438f` Shepherd University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.shepherd.edu/admissions/first-time-freshman-scholarships/ (sha256 5bc3dffc237f)
- issues: conflicting_sources:https://www.shepherd.edu/financialaid/scholarships
- checks: {"thresholds": null}
  - gpa_requirement: 3.50 – 3.74 ⟵ “Dean’s Scholarship | 3.50 – 3.74 | 1200 – 1290 | 24 – 26 | $2,000 | $4,000”
  - test_requirement: ACT 24 – 26 / SAT 1200 – 1290 ⟵ “Dean’s Scholarship | 3.50 – 3.74 | 1200 – 1290 | 24 – 26 | $2,000 | $4,000”
### `4adcba9cd6a38407` Shepherd University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.shepherd.edu/admissions/undergraduate-tuition-and-fees (sha256 27d50b51474e)
- issues: components_do_not_reconcile, cost_period_semester
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition (and additional estimated fees): 9398 ⟵ “Tuition (and additional estimated fees) | $9,398 | $19,994”
  - column:Housing (traditional residence hall): 5798 ⟵ “Housing (traditional residence hall) | $5,798 | $5,798”
  - column:Meals (gold-level plan): 5830 ⟵ “Meals (gold-level plan) | $5,830 | $5,830”
  - column:TOTAL: 20674 ⟵ “TOTAL | $20,674 | $30,972”
### `cf35d89ffbfad789` Shepherd University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.shepherd.edu/admissions/undergraduate-tuition-and-fees (sha256 27d50b51474e)
- issues: components_do_not_reconcile, cost_period_semester
- checks: {"columns": 1, "components_reconcile": false, "rows": 4}
  - column:Tuition (and additional estimated fees): 19994 ⟵ “Tuition (and additional estimated fees) | $9,398 | $19,994”
  - column:Housing (traditional residence hall): 5798 ⟵ “Housing (traditional residence hall) | $5,798 | $5,798”
  - column:Meals (gold-level plan): 5830 ⟵ “Meals (gold-level plan) | $5,830 | $5,830”
  - column:TOTAL: 30972 ⟵ “TOTAL | $20,674 | $30,972”
### `5268968b86daab30` Southern West Virginia Community and Technical College — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.southernwv.edu/current-students/scholarships-financial-aid/ (sha256 27c13ac0b9db)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “He/She will need to provide documentation to prove they are an independent student. | Independent/Dependent Student Status List 26-27 Dependency Override Review Form | V1 | Standard Verification | Student needs to submit a V1 Student Verification Worksheet and tax return transcript.”
### `2cb42d77231c1994` Southern West Virginia Community and Technical College — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.southernwv.edu/current-students/business-office/ (sha256 7201d1c7c9f0)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown, stacked_header_unparsed
- checks: {"columns": 3, "components_reconcile": false, "rows": 7}
  - column:Tuition & Fees: 5160.0 ⟵ “Tuition & Fees | $5,160.00 | $5,160.00 | $8,136.00”
  - column:Program Fees: 2880.0 ⟵ “Program Fees | $2,880.00 | $2,880.00 | $2,880.00”
  - column:Books and Supplies: 2500.0 ⟵ “Books and Supplies | $2,500.00 | $2,500.00 | $2,500.00”
  - column:Living Expenses: 6500.0 ⟵ “Living Expenses | $6,500.00 | $6,800.00 | $6,800.00”
  - column:Transportation: 3500.0 ⟵ “Transportation | $3,500.00 | $4,000.00 | $4,000.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $2,000.00 | $3,000.00 | $3,000.00”
  - column:Total: 22084.0 ⟵ “Total | $22,084.00 | $23,884.00 | $27,316.00”
  - column:Tuition & Fees: 5160.0 ⟵ “Tuition & Fees | $5,160.00 | $5,160.00 | $8,136.00”
  - column:Program Fees: 2880.0 ⟵ “Program Fees | $2,880.00 | $2,880.00 | $2,880.00”
  - column:Books and Supplies: 2500.0 ⟵ “Books and Supplies | $2,500.00 | $2,500.00 | $2,500.00”
  - column:Living Expenses: 6800.0 ⟵ “Living Expenses | $6,500.00 | $6,800.00 | $6,800.00”
  - column:Transportation: 4000.0 ⟵ “Transportation | $3,500.00 | $4,000.00 | $4,000.00”
  - column:Personal Expenses: 3000.0 ⟵ “Personal Expenses | $2,000.00 | $3,000.00 | $3,000.00”
  - column:Total: 23884.0 ⟵ “Total | $22,084.00 | $23,884.00 | $27,316.00”
  - column:Tuition & Fees: 8136.0 ⟵ “Tuition & Fees | $5,160.00 | $5,160.00 | $8,136.00”
  - column:Program Fees: 2880.0 ⟵ “Program Fees | $2,880.00 | $2,880.00 | $2,880.00”
  - column:Books and Supplies: 2500.0 ⟵ “Books and Supplies | $2,500.00 | $2,500.00 | $2,500.00”
  - column:Living Expenses: 6800.0 ⟵ “Living Expenses | $6,500.00 | $6,800.00 | $6,800.00”
  - column:Transportation: 4000.0 ⟵ “Transportation | $3,500.00 | $4,000.00 | $4,000.00”
  - column:Personal Expenses: 3000.0 ⟵ “Personal Expenses | $2,000.00 | $3,000.00 | $3,000.00”
  - column:Total: 27316.0 ⟵ “Total | $22,084.00 | $23,884.00 | $27,316.00”
### `84c0f989934c2889` University of Charleston — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucwv.edu/admissions/financial-aid/institutional-and-financial-aid-information/ (sha256 78fef65978a5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Sometimes information you provide on your FAFSA no longer accurately reflects your or your family’s financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Our office will evaluate each Special Circumstance request on a case-by-case basis.”
  - sentence: need_based_special_circumstances ⟵ “You can email the Financial Aid Office (ucfinancialaid@ucwv.edu) to request the Special Circumstance form.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstance/Dependency Override Most students are considered “dependent” for federal aid purposes based on specific questions on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “You can email the Financial Aid Office (ucfinancialaid@ucwv.edu) to request the Unusual Circumstance/Dependency Override form.”
### `a57168a45c97ae63` University of Charleston — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucwv.edu/admissions/financial-aid/institutional-and-financial-aid-information/ (sha256 78fef65978a5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “According to the FAFSA Simplification Act, unusual circumstances refer to the conditions that justify an aid administrator making an adjustment to a student’s dependency status based on a unique situation (or professional judgment), more commonly referred to as a dependency override.”
### `e0301b7de49646f0` University of Charleston — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.ucwv.edu/wp-content/uploads/2026/05/SAP-Denial-Appeal-Form.pdf (sha256 b277b77cff3d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SATISFACTORY ACADEMIC PROGRESS APPEAL FORM Deadline for Appeal Form: Summer Semester– Due ASAP Fall Semester – June 1st Spring Semester – January 4th Please use this form, along with required supporting documentation to appeal the denial of your financial aid eligibility resulting from your failure to meet UC’s minimum standards for Satisfactory Academic Progress (SAP).”
### `1b07e8c4300512bf` University of Charleston — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.ucwv.edu/admissions/financial-aid/cost-sheet/ (sha256 fc3e7ab4db35)
- issues: components_do_not_reconcile, conflicting_sources:https://www.ucwv.edu/academics/school-of-health-sciences/physician-assistant-program/program-costs/
- checks: {"columns": 1, "components_reconcile": false, "rows": 5}
  - on_campus:Tuition: 33990 ⟵ “Tuition | $33,990”
  - on_campus:Housing: 8506 ⟵ “Housing | $8,506*”
  - on_campus:Meals: 5300 ⟵ “Meals | $5,300*”
  - on_campus:Fees**: 500 ⟵ “Fees** | $500”
  - on_campus:Total fixed charges: 47796 ⟵ “Total fixed charges | $47,796”
### `61e2b1e86aca99f1` University of Charleston — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://www.ucwv.edu/academics/school-of-health-sciences/physician-assistant-program/program-costs/ (sha256 349bf09423d6)
- issues: conflicting_sources:https://www.ucwv.edu/admissions/financial-aid/cost-sheet/
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition, Program & University Fees: 99492 ⟵ “Tuition, Program & University Fees | $99,492”
  - column:Estimated Program Required Expenses & Cost of Living: 66029.12 ⟵ “Estimated Program Required Expenses & Cost of Living | $66,029.12**”
  - column:Grand Total: 165521.12 ⟵ “Grand Total | $165,521.12”
### `6d1a3edac050b2cf` University of Charleston — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_title)
- source: https://econnections.ucwv.edu/academiccatalogs/2025-2026-academic-catalog.html (sha256 ba44b6b46dde)
- issues: stale_year_label:2025-26, rows_without_score, score_scale_mismatch
- checks: {"distinct_exams": 15, "equivalencies": 16, "rows_without_score": 1}
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|None]:  ⟵ “U.S. Government and Politics | 3 | POLS 101”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art – Studio: Drawing | 3 | ART 100”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology (Score of 3 or 4) | 4 | NSCI 117”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology (Score of 5) | 4 | BIOL 130, BIOL 130L”
  - equivalencies[AP-CHEMISTRY|8]:  ⟵ “Chemistry (Score of 4 or 5) | 8 | CHEM 101, 102, 101L 102L”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | 3 | POLS 210”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics – Microeconomics | 3 | ECON 201”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics– Macroeconomics | 3 | ECON 202”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|6]:  ⟵ “French | 6 | FREN 101, FREN 102”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|6]:  ⟵ “German | 6 | GERM 101, GERM 102”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 (Score of 4 or 5) | 4 | PHSC 201, PHSC 201L”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2 (Score of 4 or 5) | 4 | PHSC 202, PHSC 202L”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSYC 101”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|6]:  ⟵ “Spanish | 6 | SPAN 101, SPAN 102”
  - equivalencies[AP-UNITED-STATES-HISTORY|6]:  ⟵ “US History | 6 | HIST 251, HIST 252”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History | 3 | HIST 212”
### `a78d84018872c70e` University of Charleston — credit_policies 2026-27 · policy_kind=AP [new] (labeled_in_title)
- source: https://econnections.ucwv.edu/academiccatalogs/ (sha256 b3231558a92e)
- issues: rows_without_score, score_scale_mismatch
- checks: {"distinct_exams": 15, "equivalencies": 16, "rows_without_score": 1}
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|None]:  ⟵ “U.S. Government and Politics | 3 | POLS 101”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art – Studio: Drawing | 3 | ART 100”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology (Score of 3 or 4) | 4 | NSCI 117”
  - equivalencies[AP-BIOLOGY|4]:  ⟵ “Biology (Score of 5) | 4 | BIOL 130, BIOL 130L”
  - equivalencies[AP-CHEMISTRY|8]:  ⟵ “Chemistry (Score of 4 or 5) | 8 | CHEM 101, 102, 101L 102L”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics | 3 | POLS 210”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics – Microeconomics | 3 | ECON 201”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics– Macroeconomics | 3 | ECON 202”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|6]:  ⟵ “French | 6 | FREN 101, FREN 102”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|6]:  ⟵ “German | 6 | GERM 101, GERM 102”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1 (Score of 4 or 5) | 4 | PHSC 201, PHSC 201L”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2 (Score of 4 or 5) | 4 | PHSC 202, PHSC 202L”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology | 3 | PSYC 101”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|6]:  ⟵ “Spanish | 6 | SPAN 101, SPAN 102”
  - equivalencies[AP-UNITED-STATES-HISTORY|6]:  ⟵ “US History | 6 | HIST 251, HIST 252”
  - equivalencies[AP-WORLD-HISTORY-MODERN|3]:  ⟵ “World History | 3 | HIST 212”
### `83fa83bbd9485288` West Liberty University — appeals 2025-26 [new] (labeled_in_source)
- source: https://westliberty.edu/financial-aid/files/2024/12/25-26-Special-Circumstances-Form.pdf (sha256 933b03749497)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Office of Financial Aid Phone: (304) 336-8016 208 University Drive finaid@westliberty.edu College Union Box 124 West Liberty, WV 26074 WLU Special Circumstance Policy Your eligibility for financial aid is initially calculated based on the information you provided on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “The Director of Financial Aid does review all requests for special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “If the student is selected for verification or conflicting data, that process must be completed before any special circumstance adjustments will be made.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are reviewed as soon as possible but no later than 60 days after the student enrolls.”
  - sentence: need_based_special_circumstances ⟵ “West Liberty University • (866) West-Lib • WestLiberty.edu Page 2 2025-2026 Special Circumstances Form Submit this form after you have filed the Free Application for Federal Student Aid.”
  - sentence: need_based_special_circumstances ⟵ “Other Circumstances not listed on this form  Written explanation of special circumstance request  Documentation to support a significant impact to the household income  All 2023 and 2024 W-2’s  2023 and 2024 physically signed 1040’s or Tax Return Transcript (www.irs.gov) West Liberty University • (866) West-Lib • WestLiberty.edu”
### `90cdcb8e2c248f02` West Liberty University — appeals 2026-27 [new] (labeled_in_source)
- source: https://westliberty.edu/financial-aid/files/2026/01/26-27-Special-Circumstances-Form.pdf (sha256 c8ba37ce5078)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: need_based_special_circumstances ⟵ “Office of Financial Aid Phone: (304) 336-8016 208 University Drive finaid@westliberty.edu College Union Box 124 West Liberty, WV 26074 WLU Special Circumstance Policy Your eligibility for financial aid is initially calculated based on the information you provided on the Free Application for Federal Student Aid (FAFSA).”
  - sentence: need_based_special_circumstances ⟵ “The Director of Financial Aid does review all requests for special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “If the student is selected for verification or conflicting data, that process must be completed before any special circumstance adjustments will be made.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are reviewed as soon as possible but no later than 60 days after the student enrolls.”
  - sentence: need_based_special_circumstances ⟵ “West Liberty University • (866) West-Lib • WestLiberty.edu Page 2 2026-2027 Special Circumstances Form Submit this form after you have filed the Free Application for Federal Student Aid.”
  - sentence: need_based_special_circumstances ⟵ “Other Circumstances not listed on this form  Written explanation of special circumstance request  Documentation to support a significant impact to the household income  All 2024 and 2025 W-2’s  2024 and 2025 physically signed 1040’s or Tax Return Transcript (www.irs.gov) West Liberty University • (866) West-Lib • WestLiberty.edu”
### `b44447233bfcbfbc` West Liberty University — appeals 2026-27 [new] (source_unlabeled)
- source: https://westliberty.edu/financial-aid/ (sha256 3bb5899caa54)
- issues: semantic_review_required, conflicting_sources:https://westliberty.edu/financial-aid/forms/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “Entrance Counseling and MPN Professional Judgment Your eligibility for WLU financial aid is calculated based on the information provided on the FAFSA.”
  - sentence: professional_judgment ⟵ “Our financial aid office has the authority to utilize a professional judgment to adjust the student’s FAFSA on a case-by-case basis.”
  - sentence: professional_judgment ⟵ “Professional Judgment Forms and Policy WLU Financial Aid Office is here to help Visit West Liberty University’s Financial Aid Booking Page.”
### `febe3487c129b5e6` West Liberty University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://westliberty.edu/financial-aid/forms/ (sha256 49d34eeb452f)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://westliberty.edu/financial-aid/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “TEACH Application Transient Study Agreement-Student Acknowledgment Independent Student Forms HEAPS Application Independent Student Non-Tax Filer Statement Independent Student Status Confirmation Form Independent Verification Form Special Circumstances Form (Professional Judgment) – See our Special Circumstances Policy Statement of Educational Purpose – Notary Signature Required →We also have the S”
### `19116399d0cef22a` West Liberty University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://westliberty.edu/business-office/tuition-fees/undergraduate-tuition/ (sha256 455c2ade2c6d)
- issues: residency_unknown, conflicting_sources:https://westliberty.edu/admissions/files/2026/05/2627-Cost-Sheet-Estimator.pdf,https://westliberty.edu/business-office/tuition-fees/undergraduate-tuition/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 15530 ⟵ “Tuition & Fees | $15,530 | $15,530 | $15,530”
  - with_parents_or_family:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - with_parents_or_family:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - with_parents_or_family:Personal Expenses: 965 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - with_parents_or_family:Transportation Expenses: 2961 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - with_parents_or_family:Miscellaneous Fee: 78 ⟵ “Miscellaneous Fee | $78 | $79 | $78”
  - with_parents_or_family:TOTAL: 35544 ⟵ “TOTAL | $35,544 | $36,152 | $35,462”
  - off_campus_not_with_family:Tuition & Fees: 15530 ⟵ “Tuition & Fees | $15,530 | $15,530 | $15,530”
  - off_campus_not_with_family:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - off_campus_not_with_family:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - off_campus_not_with_family:Personal Expenses: 1573 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - off_campus_not_with_family:Transportation Expenses: 2961 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - off_campus_not_with_family:Miscellaneous Fee: 79 ⟵ “Miscellaneous Fee | $78 | $79 | $78”
  - off_campus_not_with_family:TOTAL: 36152 ⟵ “TOTAL | $35,544 | $36,152 | $35,462”
  - on_campus:Tuition & Fees: 15530 ⟵ “Tuition & Fees | $15,530 | $15,530 | $15,530”
  - on_campus:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - on_campus:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - on_campus:Personal Expenses: 1573 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - on_campus:Transportation Expenses: 2271 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - on_campus:Miscellaneous Fee: 78 ⟵ “Miscellaneous Fee | $78 | $79 | $78”
  - on_campus:TOTAL: 35462 ⟵ “TOTAL | $35,544 | $36,152 | $35,462”
### `ce12b6c912846363` West Liberty University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://westliberty.edu/business-office/tuition-fees/undergraduate-tuition/ (sha256 9784cf020928)
- issues: residency_unknown, conflicting_sources:https://westliberty.edu/admissions/files/2026/05/2627-Cost-Sheet-Estimator.pdf,https://westliberty.edu/business-office/tuition-fees/undergraduate-tuition/
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition & Fees: 15530 ⟵ “Tuition & Fees | $15,530 | $15,530 | $15,530”
  - with_parents_or_family:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - with_parents_or_family:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - with_parents_or_family:Personal Expenses: 965 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - with_parents_or_family:Transportation Expenses: 2961 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - with_parents_or_family:Miscellaneous Fee: 78 ⟵ “Miscellaneous Fee | $78 | $79 | $78”
  - with_parents_or_family:TOTAL: 35544 ⟵ “TOTAL | $35,544 | $36,152 | $35,462”
  - off_campus_not_with_family:Tuition & Fees: 15530 ⟵ “Tuition & Fees | $15,530 | $15,530 | $15,530”
  - off_campus_not_with_family:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - off_campus_not_with_family:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - off_campus_not_with_family:Personal Expenses: 1573 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - off_campus_not_with_family:Transportation Expenses: 2961 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - off_campus_not_with_family:Miscellaneous Fee: 79 ⟵ “Miscellaneous Fee | $78 | $79 | $78”
  - off_campus_not_with_family:TOTAL: 36152 ⟵ “TOTAL | $35,544 | $36,152 | $35,462”
  - on_campus:Tuition & Fees: 15530 ⟵ “Tuition & Fees | $15,530 | $15,530 | $15,530”
  - on_campus:Living Expenses: 14710 ⟵ “Living Expenses | $14,710 | $14,710 | $14,710”
  - on_campus:Books & Supplies: 1300 ⟵ “Books & Supplies | $1,300 | $1,300 | $1,300”
  - on_campus:Personal Expenses: 1573 ⟵ “Personal Expenses | $965 | $1,573 | $1,573”
  - on_campus:Transportation Expenses: 2271 ⟵ “Transportation Expenses | $2,961 | $2,961 | $2,271”
  - on_campus:Miscellaneous Fee: 78 ⟵ “Miscellaneous Fee | $78 | $79 | $78”
  - on_campus:TOTAL: 35462 ⟵ “TOTAL | $35,544 | $36,152 | $35,462”
### `d874a0ec012630de` West Liberty University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://westliberty.edu/admissions/files/2026/05/2627-Cost-Sheet-Estimator.pdf (sha256 ed0e9a8ac3b3)
- issues: arrangement_unlabeled, residency_unknown, conflicting_sources:https://westliberty.edu/business-office/tuition-fees/undergraduate-tuition/,https://westliberty.edu/business-office/tuition-fees/undergraduate-tuition/
- checks: {"columns": 5, "rows": 10}
  - column:Tuition &: 9414 ⟵ “Tuition & | $9414 | $10164 | $10114 | $10414 | $11204”
  - column:Tuition & (2): 18840 ⟵ “Tuition & | $18840 | $19590 | $19540 | $19840 | $20630”
  - column:Tuition & (3): 15530 ⟵ “Tuition & | $15530 | $16280 | $16230 | $16530 | $17320”
  - column:$14710: 14710 ⟵ “$14710 | $14710 | $14710 | $14710 | $14710”
  - column:Orientation: 125 ⟵ “Orientation | $125 | $125 | $125 | $125 | $125”
  - column:Tuition & (4): 9414 ⟵ “Tuition & | $9414 | $10414 | $10814 | $10214”
  - column:Tuition & (5): 20390 ⟵ “Tuition & | $20390 | $19840 | $20240 | $19640”
  - column:Tuition & (6): 15530 ⟵ “Tuition & | $15530 | $16530 | $16930 | $16330”
  - column:$14710 (2): 14710 ⟵ “$14710 | $14710 | $14710 | $14710”
  - column:Orientation (2): 125 ⟵ “Orientation | $125 | $125 | $125 | $125”
  - column:Tuition &: 10164 ⟵ “Tuition & | $9414 | $10164 | $10114 | $10414 | $11204”
  - column:Tuition & (2): 19590 ⟵ “Tuition & | $18840 | $19590 | $19540 | $19840 | $20630”
  - column:Tuition & (3): 16280 ⟵ “Tuition & | $15530 | $16280 | $16230 | $16530 | $17320”
  - column:$14710: 14710 ⟵ “$14710 | $14710 | $14710 | $14710 | $14710”
  - column:Orientation: 125 ⟵ “Orientation | $125 | $125 | $125 | $125 | $125”
  - column:Tuition & (4): 10414 ⟵ “Tuition & | $9414 | $10414 | $10814 | $10214”
  - column:Tuition & (5): 19840 ⟵ “Tuition & | $20390 | $19840 | $20240 | $19640”
  - column:Tuition & (6): 16530 ⟵ “Tuition & | $15530 | $16530 | $16930 | $16330”
  - column:$14710 (2): 14710 ⟵ “$14710 | $14710 | $14710 | $14710”
  - column:Orientation (2): 125 ⟵ “Orientation | $125 | $125 | $125 | $125”
  - column:Tuition &: 10114 ⟵ “Tuition & | $9414 | $10164 | $10114 | $10414 | $11204”
  - column:Tuition & (2): 19540 ⟵ “Tuition & | $18840 | $19590 | $19540 | $19840 | $20630”
  - column:Tuition & (3): 16230 ⟵ “Tuition & | $15530 | $16280 | $16230 | $16530 | $17320”
  - column:$14710: 14710 ⟵ “$14710 | $14710 | $14710 | $14710 | $14710”
  - column:Orientation: 125 ⟵ “Orientation | $125 | $125 | $125 | $125 | $125”
  - … 18 more rows
### `b84dea78f1f215ff` West Liberty University — credit_policies 2025-26 · policy_kind=AP [new] (labeled_in_source)
- source: https://westliberty.edu/admissions/files/2026/03/AdvPlacement-25-26.pdf (sha256 8331ad17c2aa)
- issues: stale_year_label:2025-26, score_scale_mismatch
- checks: {"distinct_exams": 40, "equivalencies": 454, "rows_without_score": 0}
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History                               3/ 4/5            3        ART 103”
  - equivalencies[AP-MUSIC-THEORY|3]:  ⟵ “Music Theory                              3/4/5             3        MUSC 111”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “2-D Art and Design                        3/4/5             3        ART 199”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “3-D Art and Design                        3/4/5             3        ART 299”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Drawing                                   3/4/5             3        ART 115”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition            3/4/5               3         ENGL 101”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition          3/4/5               3         ENGL 102”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics         3/4/5             3        PSCI 199”
  - equivalencies[AP-EUROPEAN-HISTORY|6]:  ⟵ “European History                          3/4/5             6        HIST 199 & HIST 299”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography                           3/4/5             3        GEOG 105”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Macroeconomics                            3/4/5             3        ECON 205”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Microeconomics                            3/4/5             3        ECON 206”
  - equivalencies[AP-PSYCHOLOGY|3]:  ⟵ “Psychology                                3/4/5             3        PSYC 203”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “U.S. Government & Politics                3/4/5             3        PSCI 101”
  - equivalencies[AP-UNITED-STATES-HISTORY|6]:  ⟵ “U.S. History                              3/4/5             6        HIST 201 & HIST 202”
  - equivalencies[AP-WORLD-HISTORY-MODERN|6]:  ⟵ “World History                             3/4/5             6        HIST 101 & HIST 102”
  - equivalencies[AP-CALCULUS-AB|4]:  ⟵ “Calculus AB                               3/4/5             4        MATH 108”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3]:  ⟵ “Computer Science A                        3/4/5             3        SDE 194”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3]:  ⟵ “Computer Science Principles               3/4/5             3        CAS 111”
  - equivalencies[AP-STATISTICS|3]:  ⟵ “Statistics                                3/4/5             3        MATH 114”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science                     3/4/5             3        ENVT 101”
  - equivalencies[AP-PHYSICS-1|4]:  ⟵ “Physics 1: Algebra-Based                  3/4/5             4        PHYS 201”
  - equivalencies[AP-PHYSICS-2|4]:  ⟵ “Physics 2: Algebra-Based                  3/4/5             4        PHYS 299”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4]:  ⟵ “Physics C: Electricity & Magnetism        3/4/5             4        PHYS 299”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4]:  ⟵ “Physics C: Mechanics                      3/4/5             4        PHYS 299”
  - … 429 more rows
### `0bccc481ff275960` West Virginia State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://wvstateu.edu/wp-content/uploads/2026/03/26-27-SAP-Appeal-Form.pdf (sha256 ee9a75d2cfe0)
- issues: semantic_review_required, conflicting_sources:https://wvstateu.edu/admissions/financial-aid/satisfactory-academic-progress-sap/,https://wvstateu.edu/wp-content/uploads/2026/03/26-27-Max-Hour-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “West Virginia State University Office of Financial Aid and Scholarships 2026-2027 Satisfactory Academic Progress Appeal Process UNDERSTAND YOUR SUSPENSION To receive financial aid administered by West Virginia State University, you must be making satisfactory academic progress (SAP) toward completion of an eligible degree.”
  - sentence: sap_appeal ⟵ “I understand that decisions are processed on a case-by-case basis and the Office of Financial Aid and Scholarships may deny any SAP appeal.”
### `3da99031924b0f25` West Virginia State University — appeals 2025-26 [new] (labeled_in_source)
- source: https://wvstateu.edu/wp-content/uploads/2025/04/25-26-SAP-Appeal-Form.pdf (sha256 210f1fe47915)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://wvstateu.edu/wp-content/uploads/2025/04/25-26-Max-Hour-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “All credit hours attempted at West Virginia State University, including repeated courses with a grade of “F”, “W”, “I” or “IP” and all transfer hours accepted by WVSU that were pursued at a previous institution will be counted in the determination of hours attempted** SUSPENSION APPEAL INSTRUCTIONS:  IF YOU DID NOT MEET THE PROGRESS REQUIREMENTS because you had unusual circumstances, you may file”
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate the unusual circumstances beyond your control.”
### `6282443d17a59ffa` West Virginia State University — appeals 2025-26 [new] (labeled_in_title)
- source: https://wvstateu.edu/wp-content/uploads/2025/04/25-26-Max-Hour-Appeal-Form.pdf (sha256 4875ad31dd86)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://wvstateu.edu/wp-content/uploads/2025/04/25-26-SAP-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “All credit hours attempted at West Virginia State University, including repeated courses with a grade of “F”, “W”, “I” or “IP” and all transfer hours accepted by WVSU that were pursued at a previous institution will be counted in the determination of hours attempted** MAXIMUM HOUR SUSPENSION APPEAL INSTRUCTIONS:  IF YOU DID NOT MEET THE PROGRESS REQUIREMENTS because you had unusual circumstances,”
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate the unusual circumstances beyond your control.”
### `63f4a27f1caa5b70` West Virginia State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://wvstateu.edu/admissions/financial-aid/satisfactory-academic-progress-sap/ (sha256 d07a64351288)
- issues: semantic_review_required, conflicting_sources:https://wvstateu.edu/wp-content/uploads/2026/03/26-27-Max-Hour-Appeal-Form.pdf,https://wvstateu.edu/wp-content/uploads/2026/03/26-27-SAP-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Request to Appeal Satisfactory Academic Progress Suspension Appeals decisions will be made by the Office of Financial Aid and Scholarships.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress standing can be appealed when one of the following conditions exists: Illness or injury of the student Illness, injury, or death of a family member Natural Disasters-i.e.: floods, fires, tornadoes, hurricanes, or earthquakes Criminal acts inflicted on the student or student’s family.”
### `6bc9b3aa7305d0ff` West Virginia State University — appeals 2026-27 [new] (labeled_in_title)
- source: https://wvstateu.edu/wp-content/uploads/2026/03/26-27-Max-Hour-Appeal-Form.pdf (sha256 6f41833815a7)
- issues: semantic_review_required, conflicting_sources:https://wvstateu.edu/admissions/financial-aid/satisfactory-academic-progress-sap/,https://wvstateu.edu/wp-content/uploads/2026/03/26-27-SAP-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “I understand that decisions are processed on a case-by-case basis and the Office of Financial Aid and Scholarships may deny any SAP appeal.”
### `799d56dd20179418` West Virginia State University — appeals 2026-27 [new] (labeled_in_title)
- source: https://wvstateu.edu/wp-content/uploads/2026/03/26-27-Max-Hour-Appeal-Form.pdf (sha256 6f41833815a7)
- issues: semantic_review_required, conflicting_sources:https://wvstateu.edu/wp-content/uploads/2026/03/26-27-SAP-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “All credit hours attempted at West Virginia State University, including repeated courses with a grade of “F”, “W”, “I” or “IP” and all transfer hours accepted by WVSU that were pursued at a previous institution will be counted in the determination of hours attempted** MAXIMUM HOUR SUSPENSION APPEAL INSTRUCTIONS:  IF YOU DID NOT MEET THE PROGRESS REQUIREMENTS because you had unusual circumstances,”
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate the unusual circumstances beyond your control.”
### `8dc9d0a58ccbb289` West Virginia State University — appeals 2025-26 [new] (labeled_in_source)
- source: https://wvstateu.edu/wp-content/uploads/2025/04/25-26-SAP-Appeal-Form.pdf (sha256 210f1fe47915)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://wvstateu.edu/wp-content/uploads/2025/04/25-26-Max-Hour-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “West Virginia State University Office of Financial Aid and Scholarships 2025-2026 Satisfactory Academic Progress Appeal Process UNDERSTAND YOUR SUSPENSION To receive financial aid administered by West Virginia State University, you must be making satisfactory academic progress (SAP) toward completion of an eligible degree.”
  - sentence: sap_appeal ⟵ “I understand that decisions are processed on a case-by-case basis and the Office of Financial Aid and Scholarships may deny any SAP appeal.”
### `adc918f323f097c1` West Virginia State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://wvstateu.edu/wp-content/uploads/2026/03/26-27-SAP-Appeal-Form.pdf (sha256 ee9a75d2cfe0)
- issues: semantic_review_required, conflicting_sources:https://wvstateu.edu/wp-content/uploads/2026/03/26-27-Max-Hour-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “All credit hours attempted at West Virginia State University, including repeated courses with a grade of “F”, “W”, “I” or “IP” and all transfer hours accepted by WVSU that were pursued at a previous institution will be counted in the determination of hours attempted** SUSPENSION APPEAL INSTRUCTIONS:  IF YOU DID NOT MEET THE PROGRESS REQUIREMENTS because you had unusual circumstances, you may file”
  - sentence: need_based_special_circumstances ⟵ “You will need to demonstrate the unusual circumstances beyond your control.”
### `c73a4db70d0aa041` West Virginia State University — appeals 2025-26 [new] (labeled_in_title)
- source: https://wvstateu.edu/wp-content/uploads/2025/04/25-26-Max-Hour-Appeal-Form.pdf (sha256 4875ad31dd86)
- issues: stale_year_label:2025-26, semantic_review_required, conflicting_sources:https://wvstateu.edu/wp-content/uploads/2025/04/25-26-SAP-Appeal-Form.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “I understand that decisions are processed on a case-by-case basis and the Office of Financial Aid and Scholarships may deny any SAP appeal.”
### `6be96f938ae11f8f` West Virginia State University — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://wvstateu.edu/admissions/financial-aid/2025-2026-cost-of-attendance/ (sha256 d9f0a7ee8f4c)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 7}
  - with_parents_or_family:Tuition and Fees: 9570 ⟵ “Tuition and Fees | $9,570 | $9,570 | $9,570”
  - with_parents_or_family:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - with_parents_or_family:Housing and Meals: 7007 ⟵ “Housing and Meals | $7,007 | $11,678 | $10,718”
  - with_parents_or_family:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71 | $71”
  - with_parents_or_family:Transportation: 1340 ⟵ “Transportation | $1,340 | $1,340 | $1,340”
  - with_parents_or_family:Personal & Miscellaneous: 2365 ⟵ “Personal & Miscellaneous | $2,365 | $2,365 | $2,365”
  - with_parents_or_family:Total Estimated Expenses: 21643 ⟵ “Total Estimated Expenses | $21,643 | $26,314 | $25,354”
  - off_campus_not_with_family:Tuition and Fees: 9570 ⟵ “Tuition and Fees | $9,570 | $9,570 | $9,570”
  - off_campus_not_with_family:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - off_campus_not_with_family:Housing and Meals: 11678 ⟵ “Housing and Meals | $7,007 | $11,678 | $10,718”
  - off_campus_not_with_family:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71 | $71”
  - off_campus_not_with_family:Transportation: 1340 ⟵ “Transportation | $1,340 | $1,340 | $1,340”
  - off_campus_not_with_family:Personal & Miscellaneous: 2365 ⟵ “Personal & Miscellaneous | $2,365 | $2,365 | $2,365”
  - off_campus_not_with_family:Total Estimated Expenses: 26314 ⟵ “Total Estimated Expenses | $21,643 | $26,314 | $25,354”
  - on_campus:Tuition and Fees: 9570 ⟵ “Tuition and Fees | $9,570 | $9,570 | $9,570”
  - on_campus:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290 | $1,290”
  - on_campus:Housing and Meals: 10718 ⟵ “Housing and Meals | $7,007 | $11,678 | $10,718”
  - on_campus:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71 | $71”
  - on_campus:Transportation: 1340 ⟵ “Transportation | $1,340 | $1,340 | $1,340”
  - on_campus:Personal & Miscellaneous: 2365 ⟵ “Personal & Miscellaneous | $2,365 | $2,365 | $2,365”
  - on_campus:Total Estimated Expenses: 25354 ⟵ “Total Estimated Expenses | $21,643 | $26,314 | $25,354”
### `96aebdbd47a04e98` West Virginia State University — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://wvstateu.edu/admissions/financial-aid/2025-2026-cost-of-attendance/ (sha256 d9f0a7ee8f4c)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - off_campus_not_with_family:Tuition and Fees: 14990 ⟵ “Tuition and Fees | $14,990 | $14,990”
  - off_campus_not_with_family:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290”
  - off_campus_not_with_family:Housing and Meals: 11678 ⟵ “Housing and Meals | $11,678 | $10,718”
  - off_campus_not_with_family:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71”
  - off_campus_not_with_family:Transportation: 1340 ⟵ “Transportation | $1,340 | $1,340”
  - off_campus_not_with_family:Personal & Miscellaneous: 2390 ⟵ “Personal & Miscellaneous | $2,390 | $2,390”
  - off_campus_not_with_family:Total Estimated Expenses: 31759 ⟵ “Total Estimated Expenses | $31,759 | $30,799”
  - on_campus:Tuition and Fees: 14990 ⟵ “Tuition and Fees | $14,990 | $14,990”
  - on_campus:Books and Supplies: 1290 ⟵ “Books and Supplies | $1,290 | $1,290”
  - on_campus:Housing and Meals: 10718 ⟵ “Housing and Meals | $11,678 | $10,718”
  - on_campus:Loan Fees: 71 ⟵ “Loan Fees | $71 | $71”
  - on_campus:Transportation: 1340 ⟵ “Transportation | $1,340 | $1,340”
  - on_campus:Personal & Miscellaneous: 2390 ⟵ “Personal & Miscellaneous | $2,390 | $2,390”
  - on_campus:Total Estimated Expenses: 30799 ⟵ “Total Estimated Expenses | $31,759 | $30,799”
### `mfeba8a29664d42a` West Virginia State University — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://wvstateu.edu/academics/transfer/academic-credits-policies-of-transfer/ (sha256 6edc7d1ec82f)
- issues: conflicting_values:residency_requirement_credits
- checks: {"fields": ["residency_requirement_credits"], "merged_pages": 2}
  - residency_requirement_credits: 30 ⟵ “Graduation requirements stipulate all West Virginia State University students in a degree seeking program must earn a minimum of 30 credit hours in residence in order to be awarded a West Virginia State University Degree.”
### `0e93126159a329eb` West Virginia University — appeals 2025-26 [new] (labeled_in_source)
- source: https://hub.wvu.edu/applying-for-aid-fa/unsatisfied-requirements (sha256 a20cccd188ec)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Related Resources Special Circumstances SAI Calculation Appeal Budget Review Unusual Circumstances StudentForms Other Financial Aid Opportunities Potential Financial Aid Payment Issues Students and families should review the list below to determine why aid did not disburse (pay towards their balance due): Submit a Free Application for Federal Student Aid (FAFSA) for this academic year The FAFSA mu”
  - sentence: need_based_special_circumstances ⟵ “Students may also want to request a Dependency Appeal or SAI Calculation Appeal (also known as a special circumstance or financial hardship).”
  - sentence: need_based_special_circumstances ⟵ “Related Resources Special Circumstances SAI Calculation Appeal Budget Review Unusual Circumstances StudentForms Other Financial Aid Opportunities Additional References If you have unsatisfied requirements on your account and still have questions, you may use the other resources below for more information.”
### `716915c8c6575892` West Virginia University — appeals 2023-24 [new] (labeled_in_source)
- source: https://hub.wvu.edu/applying-for-aid/special-circumstances/sai-calculation-appeal (sha256 d626a7fb7cf5)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “To remain equitable, our office will review all applications on a case-by-case basis (also referred to as a professional judgment).”
  - sentence: professional_judgment ⟵ “After you have logged into StudentForms, click on the "Manage Requests" button near the top of the page Find "Professional Judgment: Special Circumstance — SAI Calculation Appeal" listed.”
  - sentence: professional_judgment ⟵ “Related Resources Special Circumstances Budget Review Unusual Circumstances Unsatisfied Requirements StudentForms Other Financial Aid Opportunities Examples of Third-Party Documentation With any professional judgment — including SAI Calculation Appeals — the individual appealing must submit sufficient third-party documentation to support the reason(s) for the appeal as well as to strengthen their ”
### `782c198db6772710` West Virginia University — appeals 2023-24 [new] (labeled_in_source)
- source: https://hub.wvu.edu/applying-for-aid/special-circumstances/sai-calculation-appeal (sha256 d626a7fb7cf5)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Search this site Search WVU Home Applying for Aid Special Circumstances SAI Calculation Appeal SAI Calculation Appeal Page Navigation: General Information Eligible Circumstances Requesting an SAI Calculation Appeal Possible Appeal Outcomes Examples of Third-Party Documentation General Information Students must submit their Free Application for Federal Student Aid (FAFSA) before requesting an SAI C”
  - sentence: need_based_special_circumstances ⟵ “Related Resources Special Circumstances Budget Review Unusual Circumstances Unsatisfied Requirements StudentForms Other Financial Aid Opportunities Eligible Circumstances Additional details related to documenting your specific circumstances can be found in the Examples of Third-Party Documentation section.”
  - sentence: need_based_special_circumstances ⟵ “Click on appeal link that says "Dependent or Independent Special Circumstance — SAI Calculation Appeal" to show the tasks associated with the appeal.”
  - sentence: need_based_special_circumstances ⟵ “Reduced SAI but no change in financial aid offer: The change in circumstances reduced the SAI but not change it enough to impact your financial aid eligibility.”
### `78ff76d499f83203` West Virginia University — appeals 2026-27 [new] (source_unlabeled)
- source: https://hub.wvu.edu/applying-for-aid/special-circumstances (sha256 53355ae82ee2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “These adjustments are considered to be a professional judgment of the aid administrator.”
### `8be3644fa5d36e95` West Virginia University — appeals 2026-27 [new] (source_unlabeled)
- source: https://hub.wvu.edu/types-of-aid/scholarships/exception-requests (sha256 53a3dd2e8c0d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “Scholarships Students May Appeal or Request to Defer If you were unable to meet the renewal requirements for institutional scholarships or the WV Promise Scholarship due to extenuating circumstances, you may appeal for reconsideration through this process.”
  - sentence: scholarship_retention_appeal ⟵ “How to Access and Submit a Scholarship Appeal Related Resources Scholarships All About WVU Scholarship Offers Renewal Requirements WVU Undergraduate Admissions Difference Between Appeal and Deferment Appeal Appealing is an option provided to students who have previously lost their scholarship due to extenuating circumstances that impacted their ability to achieve the renewal requirements for the a”
### `a7bd47c78722169b` West Virginia University — appeals 2026-27 [new] (source_unlabeled)
- source: https://hub.wvu.edu/applying-for-aid/special-circumstances (sha256 53355ae82ee2)
- issues: semantic_review_required, conflicting_sources:https://hub.wvu.edu/types-of-aid/scholarships/promise
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Search this site Search WVU Home Applying for Aid Special Circumstances Special Circumstances Page Navigation: General Information Types of Special Circumstance Appeals General Information According to the FAFSA Simplification Act, special circumstances refer to the financial situations (loss of job, etc.) that justify an aid administrator adjusting a student's cost of attendance (COA) or Student ”
  - sentence: need_based_special_circumstances ⟵ “Please note that students who have been selected for verification must complete the verification process before requesting any Special Circumstance Appeal.”
  - sentence: need_based_special_circumstances ⟵ “Types of Special Circumstance Appeals SAI Calculation Appeal Sometimes information you provide on your Free Application for Federal Student Aid (FAFSA) no longer accurately reflects your or your family’s financial situation.”
  - sentence: need_based_special_circumstances ⟵ “Related Resources SAI Calculation Appeal Budget Review Unusual Circumstances Unsatisfied Requirements Applying for Aid Other Financial Aid Opportunities WVU Hub Evansdale Crossing 62 Morrill Way — Suite 200 Morgantown, WV 26506 (304) 293-1988 (1WVU) Submit an Online Request/Ticket Facebook X Instagram For office hours and additional contact information, visit our Contact Us webpage.”
### `bef5613c7b914dd8` West Virginia University — appeals 2026-27 [new] (source_unlabeled)
- source: https://hub.wvu.edu/navigating-aid/maintain-aid/sap (sha256 caa1e55be135)
- issues: semantic_review_required, conflicting_sources:https://hub.wvu.edu/applying-for-aid/special-circumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “The satisfactory academic progress appeal process is for financial aid only and does not reinstate your academic standing.”
### `d8cc6b9f5fef7282` West Virginia University — appeals 2026-27 [new] (source_unlabeled)
- source: https://hub.wvu.edu/types-of-aid/scholarships/promise (sha256 a9adc0e77990)
- issues: semantic_review_required, conflicting_sources:https://hub.wvu.edu/applying-for-aid/special-circumstances
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appealing Promise Scholarship Eligibility If you feel you have special circumstances or are eligible for renewed Promise in another academic year, please submit the Scholarship Exception Request appropriate for your situation.”
### `f65c8ab110c9e553` West Virginia University — appeals 2026-27 [new] (source_unlabeled)
- source: https://hub.wvu.edu/applying-for-aid/special-circumstances (sha256 53355ae82ee2)
- issues: semantic_review_required, conflicting_sources:https://hub.wvu.edu/navigating-aid/maintain-aid/sap
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Students must maintain a level of academic progress toward completing their degree or teacher certification to retain eligibility for aid — including student loans, parent loans, federal work-study, and grants.”
### `d1976bb552b9bc31` West Virginia University Institute of Technology — costs 2026-27 · residency=not_applicable [new] (source_unlabeled)
- source: https://admissions.wvutech.edu/financial/guarantee (sha256 f84b3657df19)
- issues: ambiguous_year_labels, cost_period_semester, residency_unknown
- checks: {"columns": 1, "rows": 4}
  - column:University Tuition: 4500 ⟵ “University Tuition | $4,500”
  - column:University Fees: 700 ⟵ “University Fees | $700”
  - column:College Tuition: 300 ⟵ “College Tuition | $300”
  - column:Tuition & Fees Due:: 5500 ⟵ “Tuition & Fees Due: | $5,500”
### `6708525259515daf` West Virginia University at Parkersburg — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/ (sha256 f6a4e3dd2ada)
- issues: semantic_review_required, conflicting_sources:https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/?hilite=financial+aid+appeal),https://www.wvup.edu/future-students/costs-scholarships-financial-aid/general-financial-aid-information/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “A DEPENDENT STUDENT will qualify for consideration of special circumstances and should complete this form if any of the following situations apply to them: A change in marital status for the parent(s)’ whose information was provided on your FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “A change in income in the household that was involuntary and unexpected. **For dependent students, we can only consider a change in the income of the parent(s)’ whose income was reported on the FAFSA; we cannot consider a change in the income of the student. **For independent students, we can consider a change in the income of the student and/or their spouse.”
  - sentence: need_based_special_circumstances ⟵ “Examples of situations that cannot be considered Special Circumstances include: Voluntary job loss/change.”
  - sentence: need_based_special_circumstances ⟵ “In order to request a special circumstances appeal, students must meet the following criteria: Student must have completed the current year’s FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Requests for special circumstances appeals are typically reviewed within 5 business days, but during peak times the review may take longer.”
### `7ce0d6d3857a116d` West Virginia University at Parkersburg — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/ (sha256 f6a4e3dd2ada)
- issues: semantic_review_required, conflicting_sources:https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/?hilite=financial+aid+appeal),https://www.wvup.edu/future-students/costs-scholarships-financial-aid/general-financial-aid-information/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Suspension Appeal Form VI-10A Satisfactory Academic Progress (SAP) Policy VI-10B Financial Aid Appeals Consideration of Special or Unusual Circumstances If the information you filed on the Free Application for Federal Student Aid (FAFSA) does not reflect your current financial situation or does not take into account an unusual circumstance with you and/or your family you may submit a”
  - sentence: sap_appeal ⟵ “Student must be making Satisfactory Academic Progress or be eligible for aid due to an approved financial aid appeal.”
### `8ca8caee8d8c621a` West Virginia University at Parkersburg — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/?hilite=financial+aid+appeal) (sha256 fbef916d96bd)
- issues: semantic_review_required, conflicting_sources:https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/,https://www.wvup.edu/future-students/costs-scholarships-financial-aid/general-financial-aid-information/
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “A DEPENDENT STUDENT will qualify for consideration of special circumstances and should complete this form if any of the following situations apply to them: A change in marital status for the parent(s)’ whose information was provided on your FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “A change in income in the household that was involuntary and unexpected. **For dependent students, we can only consider a change in the income of the parent(s)’ whose income was reported on the FAFSA; we cannot consider a change in the income of the student. **For independent students, we can consider a change in the income of the student and/or their spouse.”
  - sentence: need_based_special_circumstances ⟵ “Examples of situations that cannot be considered Special Circumstances include: Voluntary job loss/change.”
  - sentence: need_based_special_circumstances ⟵ “In order to request a special circumstances appeal, students must meet the following criteria: Student must have completed the current year’s FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Requests for special circumstances appeals are typically reviewed within 5 business days, but during peak times the review may take longer.”
### `92d79dfd8f0390e8` West Virginia University at Parkersburg — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/ (sha256 f6a4e3dd2ada)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “In certain circumstances, the Financial Aid Office may use professional judgment to make adjustments to the FAFSA information to more accurately reflect your current financial situation.”
### `9842e8a911abfc45` West Virginia University at Parkersburg — appeals 2023-24 [new] (labeled_in_source)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/deadlines/ (sha256 4ec3a8c3bbd9)
- issues: stale_year_label:2023-24, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “HEAPS application deadlines coincide with tuition payment deadlines.) Fall 2023: Wednesday, August 9, 2023 at 4:00 pm Spring 2024: Thursday, January 4, 2024 at 4:00 pm Summer 2024: Wednesday, May 8, 2024 at 4:00 pm Financial Aid Appeals for Satisfactory Academic Progress (SAP) Priority and Final Deadlines.”
### `ab09bb13fd4f32f3` West Virginia University at Parkersburg — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/general-financial-aid-information/ (sha256 16ee9b3c07b8)
- issues: semantic_review_required, conflicting_sources:https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/,https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/?hilite=financial+aid+appeal)
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “If a student’s SAP appeal is approved, they must complete and acceptable Academic Plan that guarantees they will meet all SAP requirements in three semesters or less.”
  - sentence: sap_appeal ⟵ “Probation Status Requiring an Academic Plan As permitted by 34 CFR 668.34, 8 ii, a student on financial aid probation with an academic plan may receive Title IV, federal program funds upon the successful completion of an SAP appeal and execution of an approved Academic Plan.”
  - sentence: sap_appeal ⟵ “VI-10A Satisfactory Academic Progress (SAP) Policy VI-10B Financial Aid Appeal for Students Not in Compliance with (SAP) Policy Is there a limit on how long I can receive financial aid?”
### `b5a1999dcd93fb98` West Virginia University at Parkersburg — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/general-financial-aid-information/ (sha256 16ee9b3c07b8)
- issues: semantic_review_required, conflicting_sources:https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/,https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/?hilite=financial+aid+appeal)
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “If you have any questions about a possible special circumstance, please contact the Financial Aid Office at 304-424-8310.”
  - sentence: need_based_special_circumstances ⟵ “If there are unusual circumstances, please discuss them with our Financial Aid staff by calling 304-424-8310, and they will determine the best way for you to complete your FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “If your (and/or your family’s) income information has changed significantly in the current year due to unemployment, death, divorce, medical expenses or other special circumstances, you may be eligible to be considered for a special circumstance or re-evaluation.”
  - sentence: need_based_special_circumstances ⟵ “You can request a special circumstance form by emailing our office at finaid@wvup.edu.”
### `c0f7944148e269cb` West Virginia University at Parkersburg — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/?hilite=financial+aid+appeal) (sha256 fbef916d96bd)
- issues: semantic_review_required, conflicting_sources:https://www.wvup.edu/future-students/costs-scholarships-financial-aid/financial-aid-appeals/,https://www.wvup.edu/future-students/costs-scholarships-financial-aid/general-financial-aid-information/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Financial Aid Suspension Appeal Form VI-10A Satisfactory Academic Progress (SAP) Policy VI-10B Financial Aid Appeals Consideration of Special or Unusual Circumstances If the information you filed on the Free Application for Federal Student Aid (FAFSA) does not reflect your current financial situation or does not take into account an unusual circumstance with you and/or your family you may submit a”
  - sentence: sap_appeal ⟵ “Student must be making Satisfactory Academic Progress or be eligible for aid due to an approved financial aid appeal.”
### `075e394a97aadfa6` West Virginia University at Parkersburg — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.wvup.edu/future-students/costs-scholarships-financial-aid/tuition-and-fees/ (sha256 aa0d305138a2)
- issues: arrangement_unlabeled, components_do_not_reconcile, residency_unknown
- checks: {"columns": 2, "components_reconcile": false, "rows": 7}
  - column:2026-2027 Student Financial Aid Budget: FULL TIME, WV RESIDENT AND RECIPROCITY RATE: 1 ⟵ “2026-2027 Student Financial Aid Budget: FULL TIME, WV RESIDENT AND RECIPROCITY RATE | 1 | 2”
  - column:Room & Board: 9144 ⟵ “Room & Board | 9,144 | 14,544”
  - column:Transportation: 2400 ⟵ “Transportation | 2,400 | 2,400”
  - column:Tuition and Fees: 5783 ⟵ “Tuition and Fees | 5,783 | 5,783”
  - column:Books, Materials, Supplies, and Equipment: 1500 ⟵ “Books, Materials, Supplies, and Equipment | 1,500 | 1,500”
  - column:Miscellaneous: 1173 ⟵ “Miscellaneous | 1,173 | 2,273”
  - column:Total Cost: 20000 ⟵ “Total Cost | 20,000 | 26,500”
  - column:2026-2027 Student Financial Aid Budget: FULL TIME, WV RESIDENT AND RECIPROCITY RATE: 2 ⟵ “2026-2027 Student Financial Aid Budget: FULL TIME, WV RESIDENT AND RECIPROCITY RATE | 1 | 2”
  - column:Room & Board: 14544 ⟵ “Room & Board | 9,144 | 14,544”
  - column:Transportation: 2400 ⟵ “Transportation | 2,400 | 2,400”
  - column:Tuition and Fees: 5783 ⟵ “Tuition and Fees | 5,783 | 5,783”
  - column:Books, Materials, Supplies, and Equipment: 1500 ⟵ “Books, Materials, Supplies, and Equipment | 1,500 | 1,500”
  - column:Miscellaneous: 2273 ⟵ “Miscellaneous | 1,173 | 2,273”
  - column:Total Cost: 26500 ⟵ “Total Cost | 20,000 | 26,500”
### `dcf333c515953500` West Virginia Wesleyan College — appeals 2026-27 [new] (labeled_in_title)
- source: https://www.wvwc.edu/wp-content/uploads/2026/05/Special-Circumstance-Form-2026-2027.docx.pdf (sha256 57fd283e9741)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Form 2026-2027 West Virginia Wesleyan College Financial Aid Office ❖ 59 College Ave ❖ Buckhannon, WV 26201❖Fax: (304) 473-8824 This Special Circumstance Form may be used by you to report unusual circumstances which impact your ability to pay for you or your child’s education at WV Wesleyan.”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are only approved one time in any instance.”
  - sentence: need_based_special_circumstances ⟵ “Therefore, only the portion of expenses which exceed 11% will be considered an unusual circumstance.”
### `2ef3cf76e0ec3c0b` Wheeling University — appeals 2024-25 [new] (labeled_in_title)
- source: https://wheeling.edu/wp-content/uploads/2024/07/24-25-SAP-Appeal-Form-1.pdf (sha256 b8de946d2245)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “2024-2025 Wheeling University Satisfactory Academic Progress (SAP) Appeal Form Student Name: ____________________________________________ Student ID#____________________ Appeal Guidelines (must be able to provide supporting documentation): A student who is no longer eligible for financial aid due to not meeting SAP requirements may appeal if unusual circumstances, as defined below, interfered with”
### `429739268ae2302a` Wheeling University — appeals 2026-27 [new] (source_unlabeled)
- source: https://wheeling.edu/admissions/financial-aid/general-information/ (sha256 9a2bcf958bf6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Please remember that it is your responsibility to submit all the documentation required to for the Financial Aid Office to complete the special circumstance request.”
### `44e95e3d53c74e41` Wheeling University — appeals 2026-27 [new] (labeled_in_title)
- source: https://wheeling.edu/wp-content/uploads/2025/10/26-27-COA-Adjustment-EveningGraduate-Students.pdf (sha256 d6c9362c8afb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Financial Aid Office 2026-2027 Cost of Attendance Adjustment Request – Evening/Day Students Your financial aid eligibility is based on a standard cost of attendance budget.”
### `4e2eecb28095316a` Wheeling University — appeals 2024-25 [new] (labeled_in_title)
- source: https://wheeling.edu/wp-content/uploads/2024/07/24-25-COA-Adjustment-EveningGraduate-Students-1.pdf (sha256 fc7614e3d3e3)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Financial Aid Office 2024-2025 Cost of Attendance Adjustment Request – Evening/Day Students Your financial aid eligibility is based on a standard cost of attendance budget.”
### `592577a9da0972f1` Wheeling University — appeals 2026-27 [new] (source_unlabeled)
- source: https://wheeling.edu/admissions/financial-aid/general-information/ (sha256 9a2bcf958bf6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: dependency_override ⟵ “Dependency Overrides The Financial Aid Office will review dependency overrides on a case by case basis.”
  - sentence: dependency_override ⟵ “The student must submit in writing and provide supporting documentation along with the institutions dependency override form.”
  - sentence: dependency_override ⟵ “A dependency override will not be approved due to parent’s refusal or unwillingness to contribute to the student’s education.”
### `8f33912155aab72c` Wheeling University — appeals 2025-26 [new] (labeled_in_title)
- source: https://wheeling.edu/wp-content/uploads/2025/02/25-26-COA-Adjustment-EveningGraduate-Students87.pdf (sha256 bf619abdfdd5)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “Financial Aid Office 2025-2026 Cost of Attendance Adjustment Request – Evening/Day Students Your financial aid eligibility is based on a standard cost of attendance budget.”
### `dc77afdb16710abe` Wheeling University — appeals 2026-27 [new] (labeled_in_title)
- source: https://wheeling.edu/wp-content/uploads/2025/10/26-27-SAP-Appeal-Form.pdf (sha256 95945e56526b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “2026-2027 Wheeling University Satisfactory Academic Progress (SAP) Appeal Form Student Name: ____________________________________________ Student ID#____________________ Appeal Guidelines (must be able to provide supporting documentation): A student who is no longer eligible for financial aid due to not meeting SAP requirements may appeal if unusual circumstances, as defined below, interfered with”
### `fcd965a7e8b4ec20` Wheeling University — appeals 2025-26 [new] (labeled_in_title)
- source: https://wheeling.edu/wp-content/uploads/2025/02/25-26-SAP-Appeal-Form.pdf (sha256 43f879266c54)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “2025-2026 Wheeling University Satisfactory Academic Progress (SAP) Appeal Form Student Name: ____________________________________________ Student ID#____________________ Appeal Guidelines (must be able to provide supporting documentation): A student who is no longer eligible for financial aid due to not meeting SAP requirements may appeal if unusual circumstances, as defined below, interfered with”
### `af4df449ace0e9f5` Wheeling University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://wheeling.edu/admissions/tuition-fees/ (sha256 51e0b5310e63)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "rows": 2}
  - on_campus:Tuition: 29090 ⟵ “Tuition | $29,090 | $29,090”
  - on_campus:Fees: 2000 ⟵ “Fees | $2,000 | $2,000”
  - with_parents_or_family:Tuition: 29090 ⟵ “Tuition | $29,090 | $29,090”
  - with_parents_or_family:Fees: 2000 ⟵ “Fees | $2,000 | $2,000”
  - with_parents_or_family:Total Estimated Direct cost* With Single Room: 31090 ⟵ “Total Estimated Direct cost* With Single Room | $44,610 – $44,810$49,810 – $50,010 | $31,090”

## Re-verification of existing records (0)


## Statewide sources

Pages fetched: 2; pages by category: admissions_tests 2, merit_scholarships 1

## Blocked by the site (every request refused; needs the browser fallback)

- Appalachian Bible College (`ipeds-237136`)
- Bethany College (`ipeds-237181`)
- Glenville State University (`ipeds-237385`)
- Huntington Junior College (`ipeds-237437`)
- Blue Ridge Community and Technical College (`ipeds-446774`)
- New River Community and Technical College (`ipeds-447582`)
- Catholic Distance University (`ipeds-475398`)

## Leads: official pages found with no extracted record

- Bluefield State University: admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- BridgeValley Community & Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Concord University: cost_of_attendance, admissions_tests, residency, degree_requirements
- Davis & Elkins College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, statewide_articulation, residency, degree_requirements
- Eastern West Virginia Community and Technical College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements
- Fairmont State University: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Marshall University: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, statewide_articulation, residency, aid_appeals
- Mountwest Community and Technical College: admissions_tests, common_data_set, merit_scholarships, dual_enrollment, residency, degree_requirements, aid_appeals
- Pierpont Community and Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Potomac State College of West Virginia University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Shepherd University: cost_of_attendance, admissions_tests, common_data_set, ap_credit, transfer_credit, residency
- Southern West Virginia Community and Technical College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- University of Charleston: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, residency, degree_requirements
- West Liberty University: admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- West Virginia Northern Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- West Virginia State University: admissions_tests, common_data_set, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- West Virginia University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, residency
- West Virginia University Institute of Technology: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, residency, degree_requirements, aid_appeals
- West Virginia University at Parkersburg: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- West Virginia Wesleyan College: merit_scholarships, ap_credit, degree_requirements
- Wheeling University: cost_of_attendance, admissions_tests, merit_scholarships
