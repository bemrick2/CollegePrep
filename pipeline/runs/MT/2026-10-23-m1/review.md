# Review queue — MT (2026-27)

Pages fetched: 90; failures: 18. Candidates: 3 (0 without issues, 3 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 3 | 0 | 0 | 0 | 1 | 0 | 19 |
| cost_of_attendance | 1 | 0 | 0 | 0 | 1 | 0 | 21 |
| admissions_tests | 2 | 0 | 0 | 0 | 1 | 0 | 20 |
| common_data_set | 2 | 0 | 0 | 0 | 1 | 0 | 20 |
| merit_scholarships | 1 | 1 | 0 | 0 | 1 | 0 | 20 |
| ap_credit | 0 | 2 | 0 | 0 | 1 | 0 | 20 |
| clep_credit | 0 | 1 | 0 | 0 | 1 | 0 | 21 |
| ib_credit | 0 | 0 | 0 | 0 | 1 | 0 | 22 |
| dual_enrollment | 0 | 5 | 0 | 0 | 1 | 0 | 17 |
| transfer_credit | 0 | 1 | 0 | 0 | 1 | 0 | 21 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 1 | 22 |
| residency | 0 | 0 | 0 | 0 | 1 | 0 | 22 |
| degree_requirements | 4 | 0 | 0 | 0 | 0 | 0 | 19 |
| aid_appeals | 0 | 0 | 0 | 1 | 0 | 0 | 22 |

## Ready for review (0)


## Exceptions (3)

### `08046b675886c532` Montana State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.montana.edu/financialaid/forms/SAP%20Plan%20of%20Study%20.pdf (sha256 30146449b49b)
- issues: semantic_review_required, conflicting_sources:https://www.montana.edu/financialaid/sap.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “PLAN OF STUDY FORM Satisfactory Academic Progress Appeal _____________________________________________________________________________________ Name (please print) MSU ID Number of Terms remaining: ___________________________ (assume full-time attendance or note below) _____ First Major _____ Second Major _____ Second BA Degree _____ Double Major _____ Masters _____ Doctoral _____ Other – please ex”
### `6a1cd9c1863d0509` Montana State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.montana.edu/financialaid/specialcircumstances.html (sha256 10c023729dab)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Learn about special and unusual circumstances, eligibility requirements, and how to submit an appeal for consideration. 1.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances https://www.montana.edu/financialaid/SPC.html 2.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances https://www.montana.edu/financialaid/UC.html Office of Financial Aid Services 21 Montana Hall P.O.”
### `9fb55f143dd30b6f` Montana State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.montana.edu/financialaid/sap.html (sha256 d0c7eec52c1e)
- issues: semantic_review_required, conflicting_sources:https://www.montana.edu/financialaid/forms/SAP%20Plan%20of%20Study%20.pdf
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Resources MSU Academic Policies Graduate School Policies SAP Policy Forms Appeal Form Plan of Study Office of Financial Aid Services 21 Montana Hall P.O.”

## Re-verification of existing records (53)

- source_not_fetched: data/institutions/dawson/credit_policies/2026-27.json ["credit_policies", "ipeds-180151", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/montanabiblecollege/credit_policies/2026-27.json ["credit_policies", "ipeds-262165", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/montanabiblecollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-262165", null, "2026-27", {}]
- source_not_fetched: data/institutions/msubillings/credit_policies/2026-27.json ["credit_policies", "ipeds-180179", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/skc/credit_policies/2026-27.json ["credit_policies", "ipeds-180647", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/umt/awards/2026-27.json ["awards", "ipeds-180489", null, "2026-27", {"award_name": "Montana Admissions Scholarship Amounts Montana Admissions Scholarship amounts av: High School GPA 4.0+"}]
- source_not_fetched: data/institutions/umt/awards/2026-27.json ["awards", "ipeds-180489", null, "2026-27", {"award_name": "Montana Admissions Scholarship Amounts Montana Admissions Scholarship amounts av: High School GPA 3.5 to 3.99"}]
- source_not_fetched: data/institutions/umt/awards/2026-27.json ["awards", "ipeds-180489", null, "2026-27", {"award_name": "Montana Admissions Scholarship Amounts Montana Admissions Scholarship amounts av: High School GPA 3.0 to 3.49"}]
- source_not_fetched: data/institutions/umt/awards/2026-27.json ["awards", "ipeds-180489", null, "2026-27", {"award_name": "Montana Admissions Scholarship Amounts Montana Admissions Scholarship amounts av: High School GPA 2.7 to 2.99"}]
- source_not_fetched: data/institutions/umt/credit_policies/2026-27.json ["credit_policies", "ipeds-180489", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/umt/credit_policies/2026-27.json ["credit_policies", "ipeds-180489", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "journalism-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "dance-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "theatre-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "art-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "media-arts-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "accounting-b-s-in-business-administration", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "finance-b-s-in-business-administration", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "cybersecurity-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "management-information-systems-b-s-in-business-administration", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "entertainment-events-and-sports-management-b-s-in-business-administration", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "business-management-b-s-in-business-administration", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "marketing-b-s-in-business-administration", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "environmental-studies-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "earth-water-and-climate-science-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "forestry-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "geosciences-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "integrative-physiology-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "bachelor-of-social-work", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "east-asian-studies-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "economics-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "linguistics-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "criminology-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "women-s-gender-and-sexuality-studies-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "classical-studies-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "french-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "german-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "japanese-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "russian-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "spanish-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "world-languages-and-cultures-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "integrative-microbiology-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "interdisciplinary-biology-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "microbiology-immunology-infectious-disease-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "biochemistry-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "environmental-science-and-sustainability-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "parks-tourism-and-recreation-management-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "game-design-interactive-media-b-f-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "media-arts-b-f-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "art-b-f-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umt/degree_requirements/2026-27.json ["degree_requirements", "ipeds-180489", null, "2026-27", {"program_key": "creative-writing-b-f-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/umwestern/credit_policies/2026-27.json ["credit_policies", "ipeds-180692", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/uprovidence/credit_policies/2026-27.json ["credit_policies", "ipeds-180258", null, "2026-27", {"policy_kind": "dual_enrollment"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Montana State University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, transfer_credit, residency
