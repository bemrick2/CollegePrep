# Review queue — MI (2026-27)

Pages fetched: 90; failures: 7. Candidates: 2 (0 without issues, 2 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 4 | 0 | 0 | 0 | 1 | 0 | 71 |
| cost_of_attendance | 3 | 0 | 0 | 0 | 1 | 0 | 72 |
| admissions_tests | 0 | 0 | 0 | 0 | 1 | 0 | 75 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 1 | 75 |
| merit_scholarships | 2 | 3 | 0 | 0 | 1 | 0 | 70 |
| ap_credit | 2 | 8 | 0 | 0 | 0 | 1 | 65 |
| clep_credit | 1 | 5 | 0 | 0 | 0 | 1 | 69 |
| ib_credit | 1 | 5 | 0 | 0 | 0 | 1 | 69 |
| dual_enrollment | 3 | 4 | 0 | 0 | 1 | 0 | 68 |
| transfer_credit | 0 | 5 | 0 | 0 | 1 | 0 | 70 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 1 | 75 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 75 |
| degree_requirements | 2 | 0 | 0 | 0 | 1 | 0 | 73 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 0 | 75 |

## Ready for review (0)


## Exceptions (2)

### `4264093295b2953e` Michigan State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://finaid.msu.edu/references/sap (sha256 d80af6f73451)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Students wishing to appeal should use the online SAP Appeal Form.”
  - sentence: sap_appeal ⟵ “SAP appeals cannot be approved multiple times for the same reasons or circumstances.”
### `e2e96f2551a6369e` Michigan State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://finaid.msu.edu/references/sap (sha256 d80af6f73451)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appealing a denial of financial aid Students may appeal the denial of financial aid under certain circumstances including the death of a relative, injury or illness of the student, or other special circumstances.”

## Re-verification of existing records (43)

- source_not_fetched: data/institutions/albion/transfer_policies/2026-27.json ["transfer_policies", "ipeds-168546", null, "2026-27", {}]
- source_not_fetched: data/institutions/aquinas/credit_policies/2026-27.json ["credit_policies", "ipeds-168786", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/calvin/credit_policies/2026-27.json ["credit_policies", "ipeds-169080", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/calvin/credit_policies/2026-27.json ["credit_policies", "ipeds-169080", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/calvin/credit_policies/2026-27.json ["credit_policies", "ipeds-169080", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/calvin/transfer_policies/2026-27.json ["transfer_policies", "ipeds-169080", null, "2026-27", {}]
- source_not_fetched: data/institutions/ferris/credit_policies/2026-27.json ["credit_policies", "ipeds-169910", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/glcc/credit_policies/2026-27.json ["credit_policies", "ipeds-170091", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/hfcc/credit_policies/2026-27.json ["credit_policies", "ipeds-170240", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/hfcc/credit_policies/2026-27.json ["credit_policies", "ipeds-170240", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/hope/awards/2026-27.json ["awards", "ipeds-170301", null, "2026-27", {"award_name": "Trustee Scholarship"}]
- source_not_fetched: data/institutions/hope/awards/2026-27.json ["awards", "ipeds-170301", null, "2026-27", {"award_name": "Presidential Scholarship"}]
- source_not_fetched: data/institutions/hope/awards/2026-27.json ["awards", "ipeds-170301", null, "2026-27", {"award_name": "Distinguished Scholar Award"}]
- source_not_fetched: data/institutions/hope/awards/2026-27.json ["awards", "ipeds-170301", null, "2026-27", {"award_name": "Alumni Honors Scholarship"}]
- source_not_fetched: data/institutions/hope/awards/2026-27.json ["awards", "ipeds-170301", null, "2026-27", {"award_name": "Anchor Award"}]
- source_not_fetched: data/institutions/kzoo/transfer_policies/2026-27.json ["transfer_policies", "ipeds-170532", null, "2026-27", {}]
- source_not_fetched: data/institutions/kellogg/transfer_policies/2026-27.json ["transfer_policies", "ipeds-170550", null, "2026-27", {}]
- source_not_fetched: data/institutions/kettering/credit_policies/2026-27.json ["credit_policies", "ipeds-169983", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/kettering/credit_policies/2026-27.json ["credit_policies", "ipeds-169983", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/ltu/awards/2026-27.json ["awards", "ipeds-170675", null, "2026-27", {"award_name": "Presidential"}]
- source_not_fetched: data/institutions/ltu/awards/2026-27.json ["awards", "ipeds-170675", null, "2026-27", {"award_name": "Elite"}]
- source_not_fetched: data/institutions/ltu/awards/2026-27.json ["awards", "ipeds-170675", null, "2026-27", {"award_name": "Preeminent"}]
- source_not_fetched: data/institutions/ltu/awards/2026-27.json ["awards", "ipeds-170675", null, "2026-27", {"award_name": "Honors"}]
- source_not_fetched: data/institutions/ltu/awards/2026-27.json ["awards", "ipeds-170675", null, "2026-27", {"award_name": "Trustee"}]
- source_not_fetched: data/institutions/ltu/awards/2026-27.json ["awards", "ipeds-170675", null, "2026-27", {"award_name": "Trustee Grant"}]
- source_not_fetched: data/institutions/macomb/credit_policies/2026-27.json ["credit_policies", "ipeds-170790", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/macomb/credit_policies/2026-27.json ["credit_policies", "ipeds-170790", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/madonna/awards/2026-27.json ["awards", "ipeds-170806", null, "2026-27", {"award_name": "Alumni Legacy"}]
- source_not_fetched: data/institutions/madonna/awards/2026-27.json ["awards", "ipeds-170806", null, "2026-27", {"award_name": "Catholic High School"}]
- source_not_fetched: data/institutions/madonna/awards/2026-27.json ["awards", "ipeds-170806", null, "2026-27", {"award_name": "Performing Arts Award"}]
- source_not_fetched: data/institutions/mtu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-171128", null, "2026-27", {}]
- source_not_fetched: data/institutions/mcc/credit_policies/2026-27.json ["credit_policies", "ipeds-169275", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/mcc/credit_policies/2026-27.json ["credit_policies", "ipeds-169275", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/mcc/credit_policies/2026-27.json ["credit_policies", "ipeds-169275", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/muskegoncc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-171304", null, "2026-27", {}]
- source_not_fetched: data/institutions/nmc/credit_policies/2026-27.json ["credit_policies", "ipeds-171483", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/nmc/credit_policies/2026-27.json ["credit_policies", "ipeds-171483", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/nmc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-171483", null, "2026-27", {"program_key": "marine-technology-bachelor-of-science", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/northwood/credit_policies/2026-27.json ["credit_policies", "ipeds-171492", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/sc4/credit_policies/2026-27.json ["credit_policies", "ipeds-172291", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/udmercy/credit_policies/2026-27.json ["credit_policies", "ipeds-169716", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/wccnet/credit_policies/2026-27.json ["credit_policies", "ipeds-172617", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/wmich/credit_policies/2026-27.json ["credit_policies", "ipeds-172699", null, "2026-27", {"policy_kind": "CLEP"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Michigan State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
