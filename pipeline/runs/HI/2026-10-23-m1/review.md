# Review queue — HI (2026-27)

Pages fetched: 90; failures: 35. Candidates: 10 (2 without issues, 8 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 4 | 0 | 0 | 0 | 0 | 0 | 11 |
| cost_of_attendance | 3 | 0 | 0 | 0 | 0 | 0 | 12 |
| admissions_tests | 0 | 0 | 0 | 0 | 1 | 0 | 14 |
| common_data_set | 0 | 0 | 0 | 0 | 1 | 0 | 14 |
| merit_scholarships | 0 | 0 | 0 | 0 | 1 | 0 | 14 |
| ap_credit | 0 | 1 | 0 | 0 | 1 | 0 | 13 |
| clep_credit | 0 | 1 | 0 | 0 | 1 | 0 | 13 |
| ib_credit | 0 | 1 | 0 | 0 | 1 | 0 | 13 |
| dual_enrollment | 0 | 0 | 0 | 0 | 0 | 1 | 14 |
| transfer_credit | 0 | 0 | 0 | 0 | 1 | 0 | 14 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 1 | 14 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 14 |
| degree_requirements | 0 | 0 | 0 | 0 | 1 | 0 | 14 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 0 | 14 |

## Ready for review (2)

### `2f667a693763d98a` University of Hawaii at Manoa — costs 2026-27 · residency=out_of_state [same] (labeled_in_source)
- source: https://manoa.hawaii.edu/admissions/financing/index.html (sha256 2ee10aa73f69)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Total:: 55760 ⟵ “Total: | $33,728 | $39,608 | $55,760”
  - on_campus:Tuition: 33792 ⟵ “Tuition | $11,760 | $17,640 | $33,792”
  - on_campus:University Fee: 914 ⟵ “University Fee | $914 | $914 | $914”
  - on_campus:Books & Supplies: 1330 ⟵ “Books & Supplies | $1,330 | $1,330 | $1,330”
  - on_campus:Housing/Food: 15690 ⟵ “Housing/Food | $15,690 | $15,690 | $15,690”
  - on_campus:Personal Expense: 2698 ⟵ “Personal Expense | $2,698 | $2,698 | $2,698”
  - on_campus:Transportation: 1336 ⟵ “Transportation | $1,336 | $1,336 | $1,336”
### `6037cf4335794acb` University of Hawaii at Manoa — costs 2026-27 · residency=in_state [same] (labeled_in_source)
- source: https://manoa.hawaii.edu/admissions/financing/index.html (sha256 2ee10aa73f69)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - on_campus:Total:: 33728 ⟵ “Total: | $33,728 | $39,608 | $55,760”
  - on_campus:Tuition: 11760 ⟵ “Tuition | $11,760 | $17,640 | $33,792”
  - on_campus:University Fee: 914 ⟵ “University Fee | $914 | $914 | $914”
  - on_campus:Books & Supplies: 1330 ⟵ “Books & Supplies | $1,330 | $1,330 | $1,330”
  - on_campus:Housing/Food: 15690 ⟵ “Housing/Food | $15,690 | $15,690 | $15,690”
  - on_campus:Personal Expense: 2698 ⟵ “Personal Expense | $2,698 | $2,698 | $2,698”
  - on_campus:Transportation: 1336 ⟵ “Transportation | $1,336 | $1,336 | $1,336”

## Exceptions (8)

### `21153997c2aa7418` University of Hawaii at Manoa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://manoa.hawaii.edu/fas/understanding-your-offer/ (sha256 bc47aff73d13)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://manoa.hawaii.edu/fas/forms/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “LEARN MORE ABOUT DISBURSEMENT & REFUNDS Special Circumstances If you or anyone in your household (spouse, parent, or both parents) has been affected financially by extenuating circumstances (loss of a job, death of a spouse/parent, divorce/legal separation, etc.), please visit the Forms page and complete the necessary Professional Judgement Appeal form.”
### `302aa676ef5d7cc1` University of Hawaii at Manoa — appeals 2026-27 [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/fas/forms/ (sha256 805e123bfd13)
- issues: semantic_review_required, conflicting_sources:https://manoa.hawaii.edu/fas/understanding-your-offer/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Spring 2027 deadline: April 16, 2027. 2026-2027 Dependent Student Professional Judgement Form for a dependent student to use if you or your parents’ finances have changed significantly. 2026-2027 Independent Student Professional Judgement Form for an independent student to use if you or your family’s finances have changed significantly.”
### `56e655bad3ada93e` University of Hawaii at Manoa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://manoa.hawaii.edu/fas/understanding-your-offer/ (sha256 bc47aff73d13)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “You may include additional educational costs such as a computer expense, airfare, childcare or medical expenses, please reach out to finaid@hawaii.edu to request the Cost of Attendance Increase form.”
### `a0c6d5dd3333276c` University of Hawaii at Manoa — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://manoa.hawaii.edu/fas/financial-aid-policies/satisfactory-academic-progress-sap-policy/ (sha256 5d1be01f95b0)
- issues: ambiguous_year_labels, semantic_review_required, conflicting_sources:https://manoa.hawaii.edu/fas/forms/
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Submit a Satisfactory Academic Progress (SAP) Appeal Form and include the following: Extenuating circumstances, such as serious personal illness or injury, death or illness of a family member, unexpected employment or work issues or other extenuating circumstances, which prevented you from meeting UH Mānoa’s Financial Aid SAP.”
  - sentence: sap_appeal ⟵ “For students whose SAP appeal is approved, a SAP Academic Plan will be sent to you.”
### `d960cac195cb2c02` University of Hawaii at Manoa — appeals 2026-27 [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/fas/forms/ (sha256 805e123bfd13)
- issues: semantic_review_required, conflicting_sources:https://manoa.hawaii.edu/fas/financial-aid-policies/satisfactory-academic-progress-sap-policy/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Forms 2026-2027 Satisfactory Academic Progress Appeal To be completed by students who have not met the requirements to sustain their financial aid and wish to appeal.”
### `1ce90bf712985309` University of Hawaii at Manoa — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/fas/cost/2026-2027-cost-of-attendance/ (sha256 543212b7f9d7)
- issues: residency_unknown, conflicting_sources:https://manoa.hawaii.edu/admissions/financing/index.html
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition (12 credits): 11760 ⟵ “Tuition (12 credits) | $11,760 | $11,760 | $11,760”
  - with_parents_or_family:Fees: 914 ⟵ “Fees | $914 | $914 | $914”
  - with_parents_or_family:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - with_parents_or_family:Housing: 4600 ⟵ “Housing | $4,600 | $8,222 | $13,478”
  - with_parents_or_family:Food: 6148 ⟵ “Food | $6,148 | $7,468 | $6,762”
  - with_parents_or_family:Personal Expenses: 2698 ⟵ “Personal Expenses | $2,698 | $2,698 | $2,698”
  - with_parents_or_family:Transportation: 2670 ⟵ “Transportation | $2,670 | $1,336 | $2,670”
  - with_parents_or_family:Total: 30120 ⟵ “Total | $30,120 | $33,728 | $39,612”
  - on_campus:Tuition (12 credits): 11760 ⟵ “Tuition (12 credits) | $11,760 | $11,760 | $11,760”
  - on_campus:Fees: 914 ⟵ “Fees | $914 | $914 | $914”
  - on_campus:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - on_campus:Housing: 8222 ⟵ “Housing | $4,600 | $8,222 | $13,478”
  - on_campus:Food: 7468 ⟵ “Food | $6,148 | $7,468 | $6,762”
  - on_campus:Personal Expenses: 2698 ⟵ “Personal Expenses | $2,698 | $2,698 | $2,698”
  - on_campus:Transportation: 1336 ⟵ “Transportation | $2,670 | $1,336 | $2,670”
  - on_campus:Total: 33728 ⟵ “Total | $30,120 | $33,728 | $39,612”
  - off_campus_not_with_family:Tuition (12 credits): 11760 ⟵ “Tuition (12 credits) | $11,760 | $11,760 | $11,760”
  - off_campus_not_with_family:Fees: 914 ⟵ “Fees | $914 | $914 | $914”
  - off_campus_not_with_family:Books and Supplies: 1330 ⟵ “Books and Supplies | $1,330 | $1,330 | $1,330”
  - off_campus_not_with_family:Housing: 13478 ⟵ “Housing | $4,600 | $8,222 | $13,478”
  - off_campus_not_with_family:Food: 6762 ⟵ “Food | $6,148 | $7,468 | $6,762”
  - off_campus_not_with_family:Personal Expenses: 2698 ⟵ “Personal Expenses | $2,698 | $2,698 | $2,698”
  - off_campus_not_with_family:Transportation: 2670 ⟵ “Transportation | $2,670 | $1,336 | $2,670”
  - off_campus_not_with_family:Total: 39612 ⟵ “Total | $30,120 | $33,728 | $39,612”
### `349af12502752d7b` University of Hawaii at Manoa — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/admissions/financing/index.html (sha256 2ee10aa73f69)
- issues: residency_unknown, conflicting_sources:https://manoa.hawaii.edu/fas/cost/2026-2027-cost-of-attendance/
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Total:: 39608 ⟵ “Total: | $33,728 | $39,608 | $55,760”
  - column:Tuition: 17640 ⟵ “Tuition | $11,760 | $17,640 | $33,792”
  - column:University Fee: 914 ⟵ “University Fee | $914 | $914 | $914”
  - column:Books & Supplies: 1330 ⟵ “Books & Supplies | $1,330 | $1,330 | $1,330”
  - column:Housing/Food: 15690 ⟵ “Housing/Food | $15,690 | $15,690 | $15,690”
  - column:Personal Expense: 2698 ⟵ “Personal Expense | $2,698 | $2,698 | $2,698”
  - column:Transportation: 1336 ⟵ “Transportation | $1,336 | $1,336 | $1,336”
### `f9725518d82efa3a` University of Hawaii at Manoa — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://manoa.hawaii.edu/fas/cost/2025-2026-cost-of-attendance/ (sha256 74b2712fe561)
- issues: residency_unknown, stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - with_parents_or_family:Tuition (12 credits): 11520 ⟵ “Tuition (12 credits) | $11,520 | $11,520 | $11,520”
  - with_parents_or_family:Fees: 882 ⟵ “Fees | $882 | $882 | $882”
  - with_parents_or_family:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404 | $1,404”
  - with_parents_or_family:Housing: 4520 ⟵ “Housing | $4,520 | $7,852 | $13,558”
  - with_parents_or_family:Food: 6068 ⟵ “Food | $6,068 | $7,364 | $6,676”
  - with_parents_or_family:Personal Expenses: 2778 ⟵ “Personal Expenses | $2,778 | $2,778 | $2,778”
  - with_parents_or_family:Transportation: 2556 ⟵ “Transportation | $2,556 | $1,278 | $2,556”
  - with_parents_or_family:Total: 29728 ⟵ “Total | $29,728 | $33,078 | $39,374”
  - on_campus:Tuition (12 credits): 11520 ⟵ “Tuition (12 credits) | $11,520 | $11,520 | $11,520”
  - on_campus:Fees: 882 ⟵ “Fees | $882 | $882 | $882”
  - on_campus:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404 | $1,404”
  - on_campus:Housing: 7852 ⟵ “Housing | $4,520 | $7,852 | $13,558”
  - on_campus:Food: 7364 ⟵ “Food | $6,068 | $7,364 | $6,676”
  - on_campus:Personal Expenses: 2778 ⟵ “Personal Expenses | $2,778 | $2,778 | $2,778”
  - on_campus:Transportation: 1278 ⟵ “Transportation | $2,556 | $1,278 | $2,556”
  - on_campus:Total: 33078 ⟵ “Total | $29,728 | $33,078 | $39,374”
  - off_campus_not_with_family:Tuition (12 credits): 11520 ⟵ “Tuition (12 credits) | $11,520 | $11,520 | $11,520”
  - off_campus_not_with_family:Fees: 882 ⟵ “Fees | $882 | $882 | $882”
  - off_campus_not_with_family:Books and Supplies: 1404 ⟵ “Books and Supplies | $1,404 | $1,404 | $1,404”
  - off_campus_not_with_family:Housing: 13558 ⟵ “Housing | $4,520 | $7,852 | $13,558”
  - off_campus_not_with_family:Food: 6676 ⟵ “Food | $6,068 | $7,364 | $6,676”
  - off_campus_not_with_family:Personal Expenses: 2778 ⟵ “Personal Expenses | $2,778 | $2,778 | $2,778”
  - off_campus_not_with_family:Transportation: 2556 ⟵ “Transportation | $2,556 | $1,278 | $2,556”
  - off_campus_not_with_family:Total: 39374 ⟵ “Total | $29,728 | $33,078 | $39,374”

## Re-verification of existing records (3)

- source_not_fetched: data/institutions/kapiolani/credit_policies/2026-27.json ["credit_policies", "ipeds-141796", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/kapiolani/credit_policies/2026-27.json ["credit_policies", "ipeds-141796", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/kapiolani/credit_policies/2026-27.json ["credit_policies", "ipeds-141796", null, "2026-27", {"policy_kind": "CLEP"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- University of Hawaii at Manoa: admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, transfer_credit, residency, degree_requirements
