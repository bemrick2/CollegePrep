# Review queue — AR (2026-27)

Pages fetched: 90; failures: 6. Candidates: 2 (0 without issues, 2 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 5 | 0 | 0 | 0 | 1 | 0 | 44 |
| cost_of_attendance | 2 | 0 | 0 | 1 | 0 | 0 | 47 |
| admissions_tests | 0 | 0 | 0 | 0 | 1 | 0 | 49 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 1 | 49 |
| merit_scholarships | 2 | 1 | 0 | 0 | 1 | 0 | 46 |
| ap_credit | 0 | 5 | 0 | 0 | 0 | 1 | 44 |
| clep_credit | 0 | 2 | 0 | 0 | 0 | 1 | 47 |
| ib_credit | 0 | 0 | 0 | 0 | 0 | 1 | 49 |
| dual_enrollment | 1 | 2 | 0 | 0 | 1 | 0 | 46 |
| transfer_credit | 0 | 4 | 0 | 0 | 1 | 0 | 45 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 1 | 49 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 49 |
| degree_requirements | 0 | 0 | 0 | 0 | 1 | 0 | 49 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 0 | 49 |

## Ready for review (0)


## Exceptions (2)

### `991b9d79a6f73990` University of Arkansas — appeals 2026-27 [new] (labeled_in_source)
- source: https://finaid.uark.edu/cost-of-attendance.php (sha256 9eb1ac299c95)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: budget_increase ⟵ “The Office of Financial Aid and Academic Scholarships will attempt to eliminate an overaward by considering a student’s request for a COA/budget increase.”
  - sentence: budget_increase ⟵ “A budget increase request should be made to the student's financial aid counselor.”
  - sentence: budget_increase ⟵ “Special Projects Policy In keeping with federal regulations, all University of Arkansas students that utilize federal financial aid, state aid, and/or institutional aid may receive a budget/cost of attendance increase up to the actual cost of a special project.”
### `80491145ad814774` University of Arkansas — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://scholarships.uark.edu/nrta/ (sha256 b5352fa2272c)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 10}
  - column:Hours: 30 ⟵ “Hours | 30”
  - column:Tuition: 8336 ⟵ “Tuition | $8,336”
  - column:Fees: 2580 ⟵ “Fees | $2,580”
  - column:Tuition/Fee Subtotal: 10916 ⟵ “Tuition/Fee Subtotal | $10,916”
  - column:Books: 1270 ⟵ “Books | $1,270”
  - column:Room: 10144 ⟵ “Room | $10,144”
  - column:Food: 5550 ⟵ “Food | $5,550”
  - column:Personal Expenses: 3452 ⟵ “Personal Expenses | $3,452”
  - column:Transportation: 2656 ⟵ “Transportation | $2,656”
  - column:Total: 33988 ⟵ “Total | $33,988”

## Re-verification of existing records (17)

- source_not_fetched: data/institutions/asun/credit_policies/2026-27.json ["credit_policies", "ipeds-440402", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/bhclr/credit_policies/2026-27.json ["credit_policies", "ipeds-106546", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/bhclr/credit_policies/2026-27.json ["credit_policies", "ipeds-106546", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/blackrivertech/credit_policies/2026-27.json ["credit_policies", "ipeds-106625", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/cccua/transfer_policies/2026-27.json ["transfer_policies", "ipeds-106795", null, "2026-27", {}]
- source_not_fetched: data/institutions/hendrix/transfer_policies/2026-27.json ["transfer_policies", "ipeds-107080", null, "2026-27", {}]
- source_not_fetched: data/institutions/lyon/credit_policies/2026-27.json ["credit_policies", "ipeds-106342", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/pccua/credit_policies/2026-27.json ["credit_policies", "ipeds-107619", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/saumag/transfer_policies/2026-27.json ["transfer_policies", "ipeds-107983", null, "2026-27", {}]
- source_not_fetched: data/institutions/uaccm/credit_policies/2026-27.json ["credit_policies", "ipeds-107585", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/uaccm/credit_policies/2026-27.json ["credit_policies", "ipeds-107585", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/uafs/credit_policies/2026-27.json ["credit_policies", "ipeds-108092", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/uafs/transfer_policies/2026-27.json ["transfer_policies", "ipeds-108092", null, "2026-27", {}]
- source_not_fetched: data/institutions/ozarks/awards/2026-27.json ["awards", "ipeds-107558", null, "2026-27", {"award_name": "Trustee Scholarship"}]
- source_not_fetched: data/institutions/ozarks/awards/2026-27.json ["awards", "ipeds-107558", null, "2026-27", {"award_name": "Hurie Scholarship"}]
- source_not_fetched: data/institutions/ozarks/awards/2026-27.json ["awards", "ipeds-107558", null, "2026-27", {"award_name": "Presidential Scholarship"}]
- source_not_fetched: data/institutions/ozarks/awards/2026-27.json ["awards", "ipeds-107558", null, "2026-27", {"award_name": "Dean\u2019s Scholarship"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- University of Arkansas: tuition_fees, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
