# Review queue — TN (2026-27)

Pages fetched: 3251; failures: 363. Candidates: 257 (111 without issues, 146 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 10 | 0 | 1 | 4 | 36 | 1 | 7 |
| cost_of_attendance | 6 | 1 | 0 | 1 | 42 | 2 | 7 |
| admissions_tests | 2 | 0 | 0 | 1 | 46 | 3 | 7 |
| common_data_set | 2 | 0 | 0 | 1 | 7 | 42 | 7 |
| merit_scholarships | 3 | 3 | 4 | 1 | 33 | 8 | 7 |
| ap_credit | 1 | 3 | 0 | 1 | 12 | 35 | 7 |
| clep_credit | 1 | 2 | 0 | 2 | 7 | 40 | 7 |
| ib_credit | 1 | 1 | 0 | 1 | 3 | 46 | 7 |
| dual_enrollment | 1 | 0 | 0 | 0 | 38 | 13 | 7 |
| transfer_credit | 0 | 7 | 1 | 1 | 38 | 5 | 7 |
| statewide_articulation | 0 | 0 | 0 | 0 | 17 | 35 | 7 |
| residency | 0 | 0 | 0 | 0 | 23 | 29 | 7 |
| degree_requirements | 1 | 1 | 0 | 0 | 44 | 6 | 7 |
| aid_appeals | 1 | 1 | 0 | 30 | 5 | 15 | 7 |

## Ready for review (111)

### `505c7c5ba1a04fda` American Baptist College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://abcnash.edu/admissions/requirements/ (sha256 220afa0ee0d0)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Only the grade of “C” or above may be transferred.”
### `0fcba704d8810c8f` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/ (sha256 6d70bdfa32d9)
- checks: {"thresholds": null}
  - test_requirement: ACT Qualifying students may have substantial awards to reduce out-of-state charges. / SAT Qualifying students may have substantial awards to reduce out-of-state charges. ⟵ “Out-of-State Students | Qualifying students may have substantial awards to reduce out-of-state charges.”
### `1a459937eeeed408` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/ (sha256 6d70bdfa32d9)
- checks: {"thresholds": null}
  - test_requirement: ACT These scholarships are awarded based on a student's application for admission and are funded by private sources. / SAT These scholarships are awarded based on a student's application for admission and are funded by private sources. ⟵ “Private Academic Scholarships | These scholarships are awarded based on a student's application for admission and are funded by private sources.”
### `2bf5414f05e36310` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Governor's Out of State (formerly Provost) | 2.75 ♦ | 0 | 8 | Full-Time”
### `3bf9a9bee449dbf2` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Academic Achievement(formerly Achievement) | 2.75 ♦ | 0 | 8 | Full-Time”
### `4d21738d311ed403` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: Award Amount Varies ⟵ “Howell C. Smith (Limited Awards Available) | High-achieving students | Admissions application to APSU | Award Amount Varies”
### `57d3f6d350f6ee11` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “Presidential | 4.0 GPA | Admissions application to APSU | $6,000”
### `72e1e17ff44cb9a6` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $3,000 ⟵ “Presidents Emerging Leaders Program (PELP)Apply by 12/31 | 3.6 GPA 23 ACT | More information about PELP | $3,000”
### `7e1c9744dd0c8180` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": {"gpa_min": 3.5}}
  - gpa_requirement: 3.5 ⟵ “Presidents Emerging Leaders Program (PELP) | 3.5 | Refer to the PELP Guidelines | 8 | Full-Time”
### `89524362272fcaab` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $3,500 ⟵ “Dean's | 3.85 - 3.99 GPA | Admissions application to APSU | $3,500”
### `8c9f68530eb77691` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Kimbrough (Limited Awards Available) | 3.0 GPA 25 ACT In-State Resident | Admissions application to APSU | $1,000”
### `8d0865937994847d` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Howell C. Smith | 2.75 ♦ | 0 | 4 | Full-Time”
### `9eb0295e5cfe8d63` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/ (sha256 6d70bdfa32d9)
- checks: {"thresholds": null}
  - test_requirement: ACT Potential scholarships available to students who are taking a study abroad course. / SAT Potential scholarships available to students who are taking a study abroad course. ⟵ “Study Abroad | Potential scholarships available to students who are taking a study abroad course.”
### `b213a5bca3801d84` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $1,500 ⟵ “Governor's Merit | 3.5 - 3.69 GPA | Admissions application to APSU | $1,500”
### `cc28a118b64b744c` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 3.0 ♦ ⟵ “Kimbrough | 3.0 ♦ | 0 | 8 | Full-Time”
### `d00b3e9165009860` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $1,000 ⟵ “Governor's Excellence | 3.0-3.49 GPA | Admissions application to APSU | $1,000”
### `f1e6288a29cd85c9` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/ (sha256 6d70bdfa32d9)
- checks: {"thresholds": null}
  - test_requirement: ACT Students transferring to APSU may be offered awards, particularly students graduating from a community college with an Associates Degree / SAT Students transferring to APSU may be offered awards, particularly students graduating from a community college with an Associates Degree ⟵ “Transfer Students | Students transferring to APSU may be offered awards, particularly students graduating from a community college with an Associates Degree”
### `f2c9d000333b51dc` Austin Peay State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/academic-scholarship-retention-information.php (sha256 86a9de8e1c78)
- checks: {"thresholds": null}
  - gpa_requirement: 2.75 ♦ ⟵ “Governor's Merit(formerly Advancement) | 2.75 ♦ | 0 | 8 | Full-Time”
### `f51ef2c426b6dd7e` Austin Peay State University — awards 2026-27 [same] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/scholarship-opportunities/freshman-scholarship-opportunities.php (sha256 a0fc10ae78bc)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “Academic Achievement | 3.7 - 3.84 GPA | Admissions application to APSU | $2,000”
### `9e9ce8f697666d9c` Belmont University — costs 2026-27 [same] (labeled_in_source)
- source: https://www.belmont.edu/admissions/first-year/tuition-aid.html (sha256 09ad51e3649b)
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 45200 ⟵ “Tuition and Fees | $45,200”
  - column:Residence Hall and Meal Plan*: 16130 ⟵ “Residence Hall and Meal Plan* | $16,130”
  - column:Total Estimated Cost for 2026-2027**: 61330 ⟵ “Total Estimated Cost for 2026-2027** | $61,330”
### `cad62698455fccec` Belmont University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.belmont.edu/admissions/adult-degree/transfer-credit.html (sha256 009bbc6ac5ac)
- checks: {"fields": ["max_transfer_credits"]}
  - max_transfer_credits: 64 ⟵ “Of the 128 credit hours required: Up to 64 hours of work from a community college can be transferred to Belmont.”
### `5b0cc65152a39acf` Bryan College-Dayton — awards 2026-27 [same] (source_unlabeled)
- source: https://www.bryan.edu/scholarship/academic-leadership-scholarships/ (sha256 f453b5ae88c0)
- checks: {"thresholds": {"act_min": 24, "gpa_min": 3.6}}
  - award_amount_text: $4,100 ⟵ “Silver | 3.60 | 24 | 3.25 | $4,100”
  - gpa_requirement: 3.60 ⟵ “Silver | 3.60 | 24 | 3.25 | $4,100”
  - test_requirement: ACT 24 ⟵ “Silver | 3.60 | 24 | 3.25 | $4,100”
### `7c849d50d5606a3b` Bryan College-Dayton — awards 2026-27 [same] (source_unlabeled)
- source: https://www.bryan.edu/scholarship/academic-leadership-scholarships/ (sha256 f453b5ae88c0)
- checks: {"thresholds": {"act_min": 21, "gpa_min": 3.4}}
  - award_amount_text: $2,500 ⟵ “Crimson | 3.40 | 21 | 3.00 | $2,500”
  - gpa_requirement: 3.40 ⟵ “Crimson | 3.40 | 21 | 3.00 | $2,500”
  - test_requirement: ACT 21 ⟵ “Crimson | 3.40 | 21 | 3.00 | $2,500”
### `fe57ce62e49b479d` Bryan College-Dayton — awards 2026-27 [same] (source_unlabeled)
- source: https://www.bryan.edu/scholarship/academic-leadership-scholarships/ (sha256 f453b5ae88c0)
- checks: {"thresholds": {"act_min": 27, "gpa_min": 3.8}}
  - award_amount_text: $5,600 ⟵ “Platinum | 3.80 | 27 | 3.50 | $5,600”
  - gpa_requirement: 3.80 ⟵ “Platinum | 3.80 | 27 | 3.50 | $5,600”
  - test_requirement: ACT 27 ⟵ “Platinum | 3.80 | 27 | 3.50 | $5,600”
### `640f9313f8f7fe36` Bryan College-Dayton — costs 2026-27 [same] (labeled_in_source)
- source: https://www.bryan.edu/admissions/tuition-fees/ (sha256 eb09c3aeb550)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition (12-17 hours): 21700 ⟵ “Tuition (12-17 hours) | $10,850 | $21,700”
  - column:Board: 3900 ⟵ “Board | $1,950 | $3,900”
  - column:Room (traditional dorms): 5650 ⟵ “Room (traditional dorms) | $2,825 | $5,650”
  - column:Total traditional (tuition, room & board): 31250 ⟵ “Total traditional (tuition, room & board) | $15,625 | $31,250”
### `1d4c059a379bccb6` Carson-Newman University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/types-of-aid/scholarships/ (sha256 7efc1d4354f8)
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '<2.5', 'amount_text': '$10,000'}, {'gpa': '2.5', 'amount_text': '$12,000'}, {'gpa': '3.0', 'amount_text': '$14,000'}, {'gpa': '3.5', 'amount_text': '$16,000'}, {'gpa': '3.9', 'amount_text': '$18,000'}] ⟵ “GPA | Merit || <2.5 | $10,000 || 2.5 | $12,000 || 3.0 | $14,000 || 3.5 | $16,000 || 3.9 | $18,000”
  - gpa_requirement: Tiered by GPA: <2.5 → $10,000; 2.5 → $12,000; 3.0 → $14,000; 3.5 → $16,000; 3.9 → $18,000 ⟵ “GPA | Merit || <2.5 | $10,000 || 2.5 | $12,000 || 3.0 | $14,000 || 3.5 | $16,000 || 3.9 | $18,000”
### `67139c261f1a764e` Carson-Newman University — costs 2026-27 [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/ (sha256 44c136e71d64)
- checks: {"columns": 1, "components_reconcile": true, "rows": 5}
  - column:Tuition: 42500 ⟵ “Tuition | $21,250 | $42,500”
  - column:Residential Student Fee: 200 ⟵ “Residential Student Fee |  | 200”
  - column:Meal Plan*: 6300 ⟵ “Meal Plan* | 3,150 | 6,300”
  - column:Room**: 6300 ⟵ “Room** | 3,150 | 6,300”
  - column:Total: 55300 ⟵ “Total | $27,550 | $55,300”
### `069014b65cb26a3f` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 d4fc687bc259)
- checks: {"thresholds": {"act_min": 25, "gpa_min": 3.75, "sat_min": 1200}}
  - gpa_requirement: 3.75+ ⟵ “Presidential Scholarship | $20,000.00 | 3.75+ |  | 25+ |  | 1200+”
  - test_requirement: ACT 25+ / SAT 1200+ ⟵ “Presidential Scholarship | $20,000.00 | 3.75+ |  | 25+ |  | 1200+”
### `bd5993357a64ac57` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 d4fc687bc259)
- checks: {"thresholds": {"act_min": 18, "gpa_min": 3.0, "sat_min": 960}}
  - gpa_requirement: 3.0+ ⟵ “Deans' Scholarship | $15,000.00 | 3.0+ |  | 18+ |  | 960+”
  - test_requirement: ACT 18+ / SAT 960+ ⟵ “Deans' Scholarship | $15,000.00 | 3.0+ |  | 18+ |  | 960+”
### `c7734f1188f83f08` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 d4fc687bc259)
- checks: {"thresholds": {"act_min": 22, "gpa_min": 3.5, "sat_min": 1100}}
  - gpa_requirement: 3.5+ ⟵ “Lasallian Scholarship | $18,000.00 | 3.5+ |  | 22+ |  | 1100+”
  - test_requirement: ACT 22+ / SAT 1100+ ⟵ “Lasallian Scholarship | $18,000.00 | 3.5+ |  | 22+ |  | 1100+”
### `d241d66e2a3baac4` Christian Brothers University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 d4fc687bc259)
- checks: {"thresholds": null}
  - gpa_requirement: N/A ⟵ “University Scholarship | $12,000 | N/A”
### `e3708262bfead03b` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 d4fc687bc259)
- checks: {"thresholds": {"act_min": 30, "sat_min": 1360}}
  - gpa_requirement: N/A ⟵ “30+ Club | $21,000.00 | N/A |  | 30+ |  | 1360+”
  - test_requirement: ACT 30+ / SAT 1360+ ⟵ “30+ Club | $21,000.00 | N/A |  | 30+ |  | 1360+”
### `ef65d56de40fc6b1` Christian Brothers University — awards 2026-27 [same] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 d4fc687bc259)
- checks: {"thresholds": {"act_min": 20, "gpa_min": 3.25, "sat_min": 1030}}
  - gpa_requirement: 3.25+ ⟵ “Maurelian Scholarship | $16,000.00 | 3.25+ |  | 20+ |  | 1030+”
  - test_requirement: ACT 20+ / SAT 1030+ ⟵ “Maurelian Scholarship | $16,000.00 | 3.25+ |  | 20+ |  | 1030+”
### `f9a18e6533bd6328` Christian Brothers University — awards 2026-27 [new] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 d4fc687bc259)
- checks: {"thresholds": null}
  - gpa_requirement: N/A ⟵ “University | $14,000.00 | N/A |  | N/A |  | N/A”
  - test_requirement: ACT N/A / SAT N/A ⟵ “University | $14,000.00 | N/A |  | N/A |  | N/A”
### `8827dad273b58ec2` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": null}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | Creative Arts Scholarship | Provides In-StateTuition Rate | See Requirements | See Requirements”
  - gpa_requirement: See Requirements ⟵ “More Info | Creative Arts Scholarship | Provides In-StateTuition Rate | See Requirements | See Requirements”
  - test_requirement: ACT See Requirements / SAT See Requirements ⟵ “More Info | Creative Arts Scholarship | Provides In-StateTuition Rate | See Requirements | See Requirements”
### `b195e3d336273f2a` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": {"gpa_min": 3.2}}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | STEM Community Outreach Scholarship | Provides In-StateTuition Rate | 3.2 | See Requirements”
  - gpa_requirement: 3.2 ⟵ “More Info | STEM Community Outreach Scholarship | Provides In-StateTuition Rate | 3.2 | See Requirements”
  - test_requirement: ACT See Requirements / SAT See Requirements ⟵ “More Info | STEM Community Outreach Scholarship | Provides In-StateTuition Rate | 3.2 | See Requirements”
### `bb7b219b684f7192` East Tennessee State University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/outofstate/freshmen.php (sha256 1c8b6a0cbbba)
- checks: {"thresholds": null}
  - award_amount_text: Provides In-StateTuition Rate ⟵ “More Info | Public Service Corps Scholarship | Provides In-StateTuition Rate | N/A | See Requirements”
  - gpa_requirement: N/A ⟵ “More Info | Public Service Corps Scholarship | Provides In-StateTuition Rate | N/A | See Requirements”
  - test_requirement: ACT See Requirements / SAT See Requirements ⟵ “More Info | Public Service Corps Scholarship | Provides In-StateTuition Rate | N/A | See Requirements”
### `0ac5b84733bf0150` Jackson State Community College — costs 2026-27 [same] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- checks: {"columns": 3, "components_per_semester": true, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:TUITION & FEES*: 2535 ⟵ “TUITION & FEES* | $2,535 | $2,535 | $2,535”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3841 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - with_parents_or_family:TOTAL: (FOR FALL AND SPRING): 21318 ⟵ “TOTAL: (FOR FALL AND SPRING) | $21,318 | $29,312 | $18,652”
  - off_campus_not_with_family:TUITION & FEES*: 2535 ⟵ “TUITION & FEES* | $2,535 | $2,535 | $2,535”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7838 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - off_campus_not_with_family:TOTAL: (FOR FALL AND SPRING): 29312 ⟵ “TOTAL: (FOR FALL AND SPRING) | $21,318 | $29,312 | $18,652”
  - other:TUITION & FEES*: 2535 ⟵ “TUITION & FEES* | $2,535 | $2,535 | $2,535”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2508 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - other:TOTAL: (FOR FALL AND SPRING): 18652 ⟵ “TOTAL: (FOR FALL AND SPRING) | $21,318 | $29,312 | $18,652”
### `0fd9a93f60222c60` Jackson State Community College — credit_policies 2026-27 [same] (source_unlabeled)
- source: https://jscc.edu/admissions/prior-learning/equivalency-exams/ (sha256 e188ca9a6ea3)
- checks: {"distinct_exams": 33, "equivalencies": 36, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | 3 | POLS 1030 American Government”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | 6 | ENGL 2110 Early American Literature & ENGL 2120 Modern American Literature”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | 6 | Credit for Literature Requirement or specific ENGL course”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | 8 | BIOL 1110 & 1120 General Biology I & II”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | 4 | MATH 1910 Calculus”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | 8 | CHEM 1110 & 1120 General Chemistry I & II”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | 3 | MATH 1130 College Algebra or MATH 1630 Finite Mathematics”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition (also Freshmen) | 50 | 6 | ENGL 1010 & 1020 Composition I & II”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | 3/6 | ENGL 1010 & 1020 Composition I & II”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | 3 | MATH 1010 Math for General Studies”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | 6 | ENGL 2210 Early British Literature and ENGL 2220 Modern British Literature”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | 3 | ACCT 1010 Principles of Accounting I”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language, level 1 | 50 | 6 | FREN 1010 & 1020 Beginning French I & II”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language, level II | 59 | 12 | FREN 1010 & 1020 Beginning French I & II FREN 2010 & 2020 Intermediate French I & II”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language, level 1*** | 50 | 6 | GERM 1010 & 1020 Beginning German I & II”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language, level II*** | 60 | 12 | GERM 1010 & 1020 Beginning German I & II GERM 2010 & 2020 Intermediate German I & II”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | 3 | HIST 2010 Early American History”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | 3 | HIST 2020 Modern American History”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Development | 50 | 3 | PSYC 2130 Lifespan Psychology”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | 6 | HUM 1010 Early Humanities and HUM 1020 Modern Humanities”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | 3 | INFS 1010 Computer Applications”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | 3 | EDUC 2210 Educational Psychology”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | 3 | BUSN 2370 Legal Environment of Business”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | 3 | PSYC 1030 General Psychology”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | 3 | SOCI 1010 Introduction to Sociology”
  - … 11 more rows
### `bcf8154da1a1d5cb` Jackson State Community College — credit_policies 2026-27 [same] (source_unlabeled)
- source: https://jscc.edu/admissions/prior-learning/equivalency-exams/ (sha256 e188ca9a6ea3)
- checks: {"distinct_exams": 38, "equivalencies": 56, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3,4,5]:  ⟵ “African American Studies | 3,4,5 | 3 SCH | HIST 2060 African American History”
  - equivalencies[AP-ART-HISTORY|3,4,5]:  ⟵ “Art History | 3,4,5 | 3 SCH | ARTH 2010 Art History I”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | 4 SCH | BIOL 1110 General Biology I”
  - equivalencies[AP-BIOLOGY|4,5]:  ⟵ “Biology | 4,5 | 8 SCH | BIOL 1110 & 1120 General Biology I & II”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | 3 SCH | MATH 1830 Applied Calculus”
  - equivalencies[AP-CALCULUS-AB|4,5]:  ⟵ “Calculus AB | 4,5 | 3 SCH | MATH 1830 Applied Calculus or MATH 1910 Calculus I”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | 4 SCH | MATH 1910 Calculus I or MATH 1920 Calculus II”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | 4 SCH | CHEM 1110 General Chemistry I”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | 8 SCH | CHEM 1110 General Chemistry I & CHEM 1120 General Chemistry II”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture*** | 3 | 6 SCH | 1010 & 1020 Beginning Language I & 2”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture*** | 4 | 9 SCH | 1010, 1020, & 2010 Intermediate Language I”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture*** | 5 | 12 SCH | 1010, 1020, 2010, & 2020 Intermediate Language II”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4,5]:  ⟵ “Computer Science A | 4,5 | 4 SCH | CISP 1010 Computer Science I”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3,4,5]:  ⟵ “Computer Science Principles | 3,4,5 | 3 SCH | CITC 1301 Introduction to Programming and Logic Design”
  - equivalencies[AP-MACROECONOMICS|3,4,5]:  ⟵ “Macroeconomics | 3,4,5 | 3 SCH | ECON 2010 Macroeconomics”
  - equivalencies[AP-MICROECONOMICS|3,4,5]:  ⟵ “Microeconomics | 3,4,5 | 3 SCH | ECON 2020 Microeconomics”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language | 3 | 3 SCH | ENGL 1010 Composition I”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4,5]:  ⟵ “English Language | 4,5 | 6 SCH | ENGL 1010 Composition I & ENGL 1020 Composition II”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3,4,5]:  ⟵ “English Literature | 3,4,5 | 6 SCH | ENGL 2210 & 2220 Survey of British Literature I & II”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3,4,5]:  ⟵ “Environmental Science | 3,4,5 | 4 SCH | BIOL 1510 Environmental Science I”
  - equivalencies[AP-EUROPEAN-HISTORY|3,4,5]:  ⟵ “European History*** | 3,4,5 | 6 SCH | HIST 1010 & 1020 Survey of Western Civilization I, II”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | 6 SCH | FREN 1010 & 1020 Beginning French I & II”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture | 4 | 9 SCH | FREN 1010, 1020, & 2010 Intermediate French I”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | 12 SCH | FREN 1010, 1020, 2010 & 2020 Intermediate French II”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture*** | 3 | 6 SCH | 1010 & 1020 Beginning Language I & 2”
  - … 31 more rows
### `871adbbdcf5f8a1e` Johnson University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://johnsonu.edu/admissions/transfer-students/ (sha256 998cfe55c059)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Here’s how it works: ✔ Credits are reviewed to see how they apply to your intended degree ✔ Courses with a grade of C or better are generally eligible for transfer If you completed an associate degree through Tennessee community colleges under the Tennessee Transfer Pathways, Johnson University may accept ALL 60 credits toward degree requirements.”
### `854259ed1f110140` Lane College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.lanecollege.edu/admissions/transfers-and-readmission (sha256 3a08b35db3ba)
- checks: {"fields": ["max_transfer_credits", "min_grade"]}
  - min_grade: C ⟵ “Students who transfer will be awarded credit for all courses which parallel the Lane College curriculum, and for which a grade of “C” or higher was earned.”
  - max_transfer_credits: 68 ⟵ “A maximum of 68 semester hours (102 quarter hours) will be accepted as transfer credit.”
### `9dfd7dc38c082643` Lee University — admissions_metrics 2025-26 [same] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/2025-2026-CDS-1-1.pdf (sha256 2789690c4071)
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 2481 ⟵ “Total applied                                                                          2,481”
  - admits: 1771 ⟵ “Total admitted                                                                         1,771”
  - enrolled: 570 ⟵ “Total enrolled                                                                          570”
  - sat_composite_25..75: [1030, 1120, 1230] ⟵ “SAT Composite                                                        1030                               1120                               1230”
  - sat_reading_25..75: [530, 570, 640] ⟵ “SAT Evidence-Based Reading and Writing                               530                                570                                640”
  - sat_math_25..75: [490, 540, 600] ⟵ “SAT Math                                                             490                                540                                600”
  - act_25..75: [20, 23, 27] ⟵ “ACT Composite                                                         20                                 23                                 27”
### `885d40aa7d56b962` Lipscomb University — costs 2026-27 [same] (labeled_in_source)
- source: https://lipscomb.edu/admission/tuition-and-financial-aid/cost-attendance (sha256 81ea03f54e4d)
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition & Fees: 44486 ⟵ “Tuition & Fees | $44,486 | $44,486 | $44,486”
  - on_campus:Housing: 11044 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - on_campus:Food: 6988 ⟵ “Food | $6,988** | $3,034 | $2,020”
  - on_campus:Books & Supplies: 1800 ⟵ “Books & Supplies | $1,800 | $1,800 | $1,800”
  - on_campus:Personal Expenses: 2530 ⟵ “Personal Expenses | $2,530 | $2,530 | $2,530”
  - on_campus:Transportation: 2314 ⟵ “Transportation | $2,314 | $2,314 | $2,314”
  - on_campus:Loan Fees: 48 ⟵ “Loan Fees | $48 | $48 | $48”
  - on_campus:Total: 69210 ⟵ “Total | $69,210 | $67,452 | $57,698”
  - off_campus_not_with_family:Tuition & Fees: 44486 ⟵ “Tuition & Fees | $44,486 | $44,486 | $44,486”
  - off_campus_not_with_family:Housing: 13240 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - off_campus_not_with_family:Food: 3034 ⟵ “Food | $6,988** | $3,034 | $2,020”
  - off_campus_not_with_family:Books & Supplies: 1800 ⟵ “Books & Supplies | $1,800 | $1,800 | $1,800”
  - off_campus_not_with_family:Personal Expenses: 2530 ⟵ “Personal Expenses | $2,530 | $2,530 | $2,530”
  - off_campus_not_with_family:Transportation: 2314 ⟵ “Transportation | $2,314 | $2,314 | $2,314”
  - off_campus_not_with_family:Loan Fees: 48 ⟵ “Loan Fees | $48 | $48 | $48”
  - off_campus_not_with_family:Total: 67452 ⟵ “Total | $69,210 | $67,452 | $57,698”
  - with_parents_or_family:Tuition & Fees: 44486 ⟵ “Tuition & Fees | $44,486 | $44,486 | $44,486”
  - with_parents_or_family:Housing: 4500 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - with_parents_or_family:Food: 2020 ⟵ “Food | $6,988** | $3,034 | $2,020”
  - with_parents_or_family:Books & Supplies: 1800 ⟵ “Books & Supplies | $1,800 | $1,800 | $1,800”
  - with_parents_or_family:Personal Expenses: 2530 ⟵ “Personal Expenses | $2,530 | $2,530 | $2,530”
  - with_parents_or_family:Transportation: 2314 ⟵ “Transportation | $2,314 | $2,314 | $2,314”
  - with_parents_or_family:Loan Fees: 48 ⟵ “Loan Fees | $48 | $48 | $48”
  - with_parents_or_family:Total: 57698 ⟵ “Total | $69,210 | $67,452 | $57,698”
### `e91522fb6c3f2cdd` Lipscomb University — credit_policies 2026-27 [same] (source_unlabeled)
- source: https://lipscomb.edu/admission/transfer-admission/transferring-credit (sha256 a7ffd3af7b5c)
- checks: {"distinct_exams": 31, "equivalencies": 31, "rows_without_score": 0}
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|No credit]:  ⟵ “American Gov./Pol. | No credit | PO 1023 | Same as 4 | 3 | Great Ideas in Politics”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|No credit]:  ⟵ “Comparative Gov./Pol. | No credit | PO 1013 | Same as 4 | 3 | Great Ideas in Politics”
  - equivalencies[AP-UNITED-STATES-HISTORY|No credit]:  ⟵ “American History | No credit | HI 2213 | Same as 4 | 3 | Great Ideas in History”
  - equivalencies[AP-EUROPEAN-HISTORY|No credit]:  ⟵ “European History | No credit | HI 1113 | Same as 4 | 3 | Great Ideas in History”
  - equivalencies[AP-WORLD-HISTORY-MODERN|No credit]:  ⟵ “World History | No credit | HI 1013 | Same as 4 | 3 | Great Ideas in History”
  - equivalencies[AP-MACROECONOMICS|EC 2403]:  ⟵ “Macroeconomics | EC 2403 | Same as 3 | Same as 3 & 4 | 3 | Social Inquiry”
  - equivalencies[AP-MICROECONOMICS|EC 2413]:  ⟵ “Microeconomics | EC 2413 | Same as 3 | Same as 3 & 4 | 3 | Social Inquiry”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|EN 1113]:  ⟵ “English Lang. and Comp.* | EN 1113 | Same as 3 | Same as 3 & 4 | 3 | Elective”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|EN 1113]:  ⟵ “English Lit. and Comp.* | EN 1113 | Same as 3 | Same as 3 & 4 | 3 | Elective”
  - equivalencies[AP-ART-HISTORY|AR 4813]:  ⟵ “Art History | AR 4813 | Same as 3 | Same as 3 & 4 | 3 | Artistic Inquiry”
  - equivalencies[AP-2-D-ART-DESIGN|AR 1033]:  ⟵ “Studio Art- 2-D Design* | AR 1033 | Same as 3 | Same as 3 & 4 | 3 | Artistic Inquiry”
  - equivalencies[AP-3-D-ART-DESIGN|AR 1033]:  ⟵ “Studio Art- 3-D Design* | AR 1033 | Same as 3 | Same as 3 & 4 | 3 | Artistic Inquiry”
  - equivalencies[AP-DRAWING|AR 1033]:  ⟵ “Studio Art-Drawing* | AR 1033 | Same as 3 | Same as 3 & 4 | 3 | Artistic Inquiry”
  - equivalencies[AP-MUSIC-THEORY|No credit]:  ⟵ “Music Theory | No credit | MU 1111, MU 1133 | MU 1111, MU 1121MU 1133, MU 1143 | 8 | Artistic Inquiry”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|FR 1114]:  ⟵ “French Language | FR 1114 | FR 1114, FR 1124, & FR 2114 | FR 1114, FR 1124, FR 2114, & FR 2124 | 16 | B.A. Foreign Language Hours”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|GE 1114]:  ⟵ “German Language | GE 1114 | GE 1114, GE 1124 & GE 2114 | GE 1114, GE 1124, GE 2114, & GE 2124 | 16 | B.A. Foreign Language Hours”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|SN 1114]:  ⟵ “Spanish Language | SN 1114 | SN 1114, SN 1124 & SN 2114 | SN 1114, SN 1124, SN 2114, & SN 2124 | 16 | B.A. Foreign Language Hours”
  - equivalencies[AP-STATISTICS|MA2183]:  ⟵ “Statistics | MA2183 | Same as 3 | Same as 3 & 4 | 3 | Quantitative reason, B.S. hours”
  - equivalencies[AP-CALCULUS-AB|No Credit]:  ⟵ “Calculus AB* | No Credit | MA 1314 | Same as 4 | 4 | Quantitative reason, B.S. hours”
  - equivalencies[AP-CALCULUS-BC|MA 1314]:  ⟵ “Calculus BC* | MA 1314 | MA 1314 & MA 2314 | Same as 4 | 8 | Quantitative reason, B.S. hours”
  - equivalencies[AP-PRECALCULUS|No Credit]:  ⟵ “Precalculus | No Credit | MA 1123 or MA 1135 | Same as 4 | 5 | Quantitative reason, B.S. hours”
  - equivalencies[AP-COMPUTER-SCIENCE-A|CS 1213]:  ⟵ “Computer Science A | CS 1213 | Same as 3 | Same as 3 & 4 | 6 | B.S. Hours”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|CCT 1133]:  ⟵ “Computer Science Principles | CCT 1133 | Same as 3 | Same as 3 & 4 | 3 | B.S. Hours”
  - equivalencies[AP-BIOLOGY|BY 1003]:  ⟵ “Biology* | BY 1003 | BY 1003 | BY1144 | 3 | Score of 3 or 4: Hours towards science requirement; Score of 5: Science requirement fully met; All scores: B.S. hours”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|BY 1003]:  ⟵ “Environmental Science* | BY 1003 | BY 1003, or BY 1013, or ESS 1013 | Same as 4 | 3 | Hours toward science requirement; B.S. hours”
  - … 6 more rows
### `6a0688ec82d4c8c3` Lipscomb University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://lipscomb.edu/admission/transfer-admission/transfer-process-questions (sha256 35440ddeed9d)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “At Lipscomb, we generally accept courses for transfer if they were earned at a regionally accredited college or university with a grade of “C” or higher.”
### `57df200a0264256b` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 58190add7e1b)
- checks: {"thresholds": null}
  - gpa_requirement: Covenant Stone Scholarship3.5+ GPA. ⟵ “Covenant Stone Scholarship3.5+ GPA. | Up to $22,000 per year on-campus. Up to $16,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.5 GPA.”
  - award_amount_text: Up to $22,000 per year on-campus. Up to $16,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.5 GPA. ⟵ “Covenant Stone Scholarship3.5+ GPA. | Up to $22,000 per year on-campus. Up to $16,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.5 GPA.”
### `5cc5442b0d01678b` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 58190add7e1b)
- checks: {"thresholds": null}
  - gpa_requirement: Orange & Garnet Scholarship3.0+ GPA. ⟵ “Orange & Garnet Scholarship3.0+ GPA. | Up to $18,000 per year on-campus. Up to $12,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
  - award_amount_text: Up to $18,000 per year on-campus. Up to $12,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA. ⟵ “Orange & Garnet Scholarship3.0+ GPA. | Up to $18,000 per year on-campus. Up to $12,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
### `95397051d7be2d7e` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 58190add7e1b)
- checks: {"thresholds": null}
  - gpa_requirement: MC Scots Scholarship3.25+ GPA. ⟵ “MC Scots Scholarship3.25+ GPA. | Up to $20,000 per year on-campus. Up to $14,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
  - award_amount_text: Up to $20,000 per year on-campus. Up to $14,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA. ⟵ “MC Scots Scholarship3.25+ GPA. | Up to $20,000 per year on-campus. Up to $14,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
### `a50f5bb624b02657` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 58190add7e1b)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $5,000 per year. Renewable for eight fall/spring semesters of full-time study with 2.75 GPA ⟵ “Theatre ScholarshipOpen to all actors and/or theatre technicians. | $500 to $5,000 per year. Renewable for eight fall/spring semesters of full-time study with 2.75 GPA”
### `d2d77f73d94eda0c` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 58190add7e1b)
- checks: {"thresholds": null}
  - gpa_requirement: Kin Takahashi Scholarship2.75+ GPA. ⟵ “Kin Takahashi Scholarship2.75+ GPA. | Up to $16,000 per year on-campus. Up to $10,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
  - award_amount_text: Up to $16,000 per year on-campus. Up to $10,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA. ⟵ “Kin Takahashi Scholarship2.75+ GPA. | Up to $16,000 per year on-campus. Up to $10,000 per year off-campus. Renewable for eight fall/spring semesters of full-time study with 2.0 GPA.”
### `e3269287bd856a77` Maryville College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/types-of-aid/scholarships-awards/first-year/ (sha256 58190add7e1b)
- checks: {"thresholds": null}
  - award_amount_text: $500 to $5,000 per year. Renewable for eight fall/spring semesters of full-time study with 2.75 GPA ⟵ “Art & Design ScholarshipOpen to all artists based on individual talent. | $500 to $5,000 per year. Renewable for eight fall/spring semesters of full-time study with 2.75 GPA”
### `f64e07acd6b95d74` Maryville College — costs 2026-27 [same] (labeled_in_source)
- source: https://www.maryvillecollege.edu/admissions/tuition-and-fees/ (sha256 38d0616ab224)
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition (Full-Time): 41300 ⟵ “Tuition (Full-Time) | $20,650 | $41,300”
  - column:Activity Fee: 512 ⟵ “Activity Fee | $256 | $512”
  - column:Orientation Fee (one time): 325 ⟵ “Orientation Fee (one time) | $325 | $325”
  - column:Service Fee: 472 ⟵ “Service Fee | $236 | $472”
  - column:Room (Basic rate – See all rates): 6880 ⟵ “Room (Basic rate – See all rates) | $3,440 | $6,880”
  - column:Meals (Scots Unlimited – See all plans): 7392 ⟵ “Meals (Scots Unlimited – See all plans) | $3,696 | $7,392”
  - column:TOTAL: 56881 ⟵ “TOTAL | $28,603 | $56,881”
### `60fe7efe8ce6224c` Mid-South Christian College — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.midsouthchristian.edu/transferability-of-credits (sha256 59eb300ed163)
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Courses eligible for transfer must reflect a grade of C- or higher.”
### `04d066ec1de736d5` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “NSCC Foundation Ambassador Scholarship | All majors accepted | Up to $1,000 per academic year”
### `0c209737ef09b4ce` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,500 per academic year ⟵ “Finish Line Scholarship | All majors accepted | Up to $1,500 per academic year”
### `20d07c1f04d4e16a` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Lance Woodard Memorial Scholarship | All majors accepted | Up to $500 per academic year”
### `21e56e7f3ab9ce71` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “NSCC Foundation Culinary Arts Scholarship | Culinary Arts students | Up to $2,000 per academic year”
### `2246c2c688c1ef2d` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,500 per academic year ⟵ “Ted M. Washington Endowed Memorial Scholarship | Computer Information Technology students | Up to $1,500 per academic year”
### `28383502320c4840` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “Moe's Southwest Grill Scholarship | All majors accepted | Up to $2,000 per academic year”
### `2cf517b7ca315acd` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,250 per academic year ⟵ “HCA Foundation Endowed Scholarship | Nursing or Surgical Technology students | Up to $1,250 per academic year”
### `2d55750d1972beea` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $800 per academic year ⟵ “John E. Mayfield Endowed Scholarship | All majors accepted | Up to $800 per academic year”
### `2f94586bcc2deeee` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Jacob Roberts Memorial Endowed Scholarship | Computer Information Technology students | Up to $500 per academic year”
### `34f546bb4058c4bc` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Mary Elizabeth Williams Endowed Scholarship | All majors accepted | Up to $1,000 per academic year”
### `3902afc4e5d8809b` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Ram Lal Seekri Endowed Scholarship | All Majors | Up to $500 per academic year”
### `39b2711f009d3177` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,150 per academic year ⟵ “Randy Rayburn Culinary Arts Scholarship | Culinary Arts students | Up to $5,150 per academic year”
### `3ced240142e049f8` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $3,000 per academic year ⟵ “Early Childhood Education Scholarship | Early Childhood Education student | Up to $3,000 per academic year”
### `3f133f82ce9ff2ac` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,372 per academic year ⟵ “The Doochin Family Scholarship | Formerly incarcerated individuals | Up to $5,372 per academic year”
### `5119cd5ad3a078f7` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “Dr. Wallace Wilson Scholarship | Architectural Engineering Technology, Civil and Construction Engineering Technology, Civil Engineering, and Mechanical Engineering students | Up to $2,000 per academic year”
### `516c1e428c595a49` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “Brian Uhl Scholarship | Culinary Arts students | Up to $2,000 per academic year”
### `61b92a647a7786cb` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Pete Faison Endowed Scholarship | Computer Information Technology students | Up to $1,000 per academic year”
### `663a5cc5a19547a1` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Doug Jameson Memorial Scholarship | All majors accepted | Up to $500 per academic year”
### `7155032765977e2d` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “ESL Ambassador Scholarship | All majors accepted | Up to $2,000 per academic year”
### `77708e9ff43d8a4b` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,250 per academic year ⟵ “Darrell Freeman Memorial Scholarship | Computer Information Technology, Computer Programming, or IT Support Specialist students | Up to $2,250 per academic year”
### `7ade41457b012b79` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “NSCC Foundation Endowed Scholarship | All majors accepted | Up to $1,000 per academic year”
### `9966c30943c90abf` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,500 per academic year ⟵ “Danny Jackson Endowed Scholarship | All Majors | Up to $2,500 per academic year”
### `a2fe35562455fc1a` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,500 per academic year ⟵ “Sanford E. Harper Endowed Scholarship | Business student | Up to $1,500 per academic year”
### `ac1dca4d064b76cf` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Dr. Federick J. Berger Endowed Scholarship | Tennessee Beta Chapter, Tau Alpha Pi Honor Society Students | Up to $500 per academic year”
### `acc41c62b5d8132c` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “ISSA Scholarship | Cyber Defense students | Up to $2,000 per academic year”
### `b5bc540e111a96a1` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “NSCC Foundation Scholarship | All majors accepted | Up to $1,000 per academic year”
### `bb114d5ded15f31e` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,575 per academic year ⟵ “Jay Luther Memorial Scholarship | Culinary Arts students | Up to $2,575 per academic year”
### `c34d93236e878de7` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $5,000 per academic year ⟵ “21st Century Educational Foundation Scholarship | Humphreys County campus student | Up to $5,000 per academic year”
### `c5213854e2a96250` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Jim Formosa Memorial Scholarship | Accounting students | Up to $500 per academic year”
### `d255ced7c66de2b6` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,250 per academic year ⟵ “Oscar Lasko Endowment Scholarship | Engineering, Computer Science, or Manufacturing students | Up to $1,250 per academic year”
### `d9ef8b9ec1deadf0` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $500 per academic year ⟵ “Dickson High Noon Rotary Scholarship | All majors accepted | Up to $500 per academic year”
### `dca26f2f0b1198f9` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Roberts – Williams Memorial Scholarship | Computer Information Technology and Business students | Up to $1,000 per academic year”
### `de7a6c22d1076222` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Dorothy Gaubert Pyle Endowed Scholarship | Black and White Photography Students | Up to $1,000 per academic year”
### `ef2d50b703769527` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “NSCC Foundation OTA Scholarship | Occupational Therapy Assistant students | Up to $1,000 per academic year”
### `f7c5837a10a5c447` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $1,000 per academic year ⟵ “Cathy O'Bryant Memorial Endowed Scholarship | Visual Communications Photography students | Up to $1,000 per academic year”
### `f9016657d65b5ece` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $2,000 per academic year ⟵ “Fuqua Family Endowed Scholarship | All majors accepted | Up to $2,000 per academic year”
### `fd62ff3852820051` Nashville State Community College — awards 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/tuition-and-aid/types-of-financial-aid/scholarships/nscc-scholarships.php (sha256 7a6012be17c5)
- checks: {"thresholds": null}
  - award_amount_text: Up to $6,000 per academic year ⟵ “Funding Our Future | Ages 18-23 not eligible for TN Promise or TN Reconnect, resident of Humphreys, Stewart, Benton, or Perry counties, complete FAFSA, maintain 2.0 GPA, enrolled in at least two courses-one of which must be in-person at Humphreys County campus, enrolled in fall and spring semesters ”
### `924d94d2d9d9959a` Northeast State Community College — costs 2026-27 [same] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/cost-of-attendance.html (sha256 883da26037d6)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees*: 5280 ⟵ “Tuition and Fees* | $5,280 | $5,280”
  - with_parents_or_family:Living Expenses (Housing & Food): 7532 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - with_parents_or_family:Books and Supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - with_parents_or_family:Transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - with_parents_or_family:Personal Expenses: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - with_parents_or_family:Total: 20304 ⟵ “Total | $20,304 | $28,143”
  - off_campus_not_with_family:Tuition and Fees*: 5280 ⟵ “Tuition and Fees* | $5,280 | $5,280”
  - off_campus_not_with_family:Living Expenses (Housing & Food): 15371 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - off_campus_not_with_family:Books and Supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - off_campus_not_with_family:Transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - off_campus_not_with_family:Personal Expenses: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - off_campus_not_with_family:Total: 28143 ⟵ “Total | $20,304 | $28,143”
### `f0c148903eeb3d49` Northeast State Community College — costs 2026-27 [same] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/cost-of-attendance.html (sha256 883da26037d6)
- checks: {"columns": 2, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:Tuition and Fees*: 8848 ⟵ “Tuition and Fees* | $8,848 | $8,848”
  - with_parents_or_family:Living Expenses (Housing & Food): 7532 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - with_parents_or_family:Books and Supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - with_parents_or_family:Transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - with_parents_or_family:Personal Expenses: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - with_parents_or_family:Total: 23872 ⟵ “Total | $23,872 | $31,711”
  - off_campus_not_with_family:Tuition and Fees*: 8848 ⟵ “Tuition and Fees* | $8,848 | $8,848”
  - off_campus_not_with_family:Living Expenses (Housing & Food): 15371 ⟵ “Living Expenses (Housing & Food) | $7,532 | $15,371”
  - off_campus_not_with_family:Books and Supplies: 1560 ⟵ “Books and Supplies | $1,560 | $1,560”
  - off_campus_not_with_family:Transportation: 3252 ⟵ “Transportation | $3,252 | $3,252”
  - off_campus_not_with_family:Personal Expenses: 2680 ⟵ “Personal Expenses | $2,680 | $2,680”
  - off_campus_not_with_family:Total: 31711 ⟵ “Total | $23,872 | $31,711”
### `b88a9f4e21e147e4` Rhodes College — costs 2026-27 [same] (labeled_in_source)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/tuition-fees (sha256 25c78d377b25)
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition: 60240 ⟵ “Tuition | $60,240”
  - column:Mandatory Fees: 820 ⟵ “Mandatory Fees | $820”
  - column:Housing & Food (Unlimited, All-Access Meal Plan)*: 15196 ⟵ “Housing & Food (Unlimited, All-Access Meal Plan)* | $15,196”
  - column:Total: 76256 ⟵ “Total | $76,256”
### `b5ae9e9eb49c73ae` Rhodes College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://www.rhodes.edu/admission-aid/apply-rhodes/college-credit-transfer-policies (sha256 a076189db8fb)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Transfer courses taken on a Pass/Fail basis must be passed with a grade of C or better.”
### `2ce020d73e2a2544` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “4,800-5,700 | Bronze | $2,000”
### `394bdc02ada28573` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “6,601 - 7,300 | Presidential | $24,000 | $6,000”
### `589321a85bee34a6` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $2,000 ⟵ “4,800 - 5,700 | Honors | $8,000 | $2,000”
### `a0f3d6e0525be59b` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $6,000 ⟵ “6,601 & higher | Gold | $6,000”
### `b153b7c451ab98f8` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ⟵ “5,701 - 6,600 | Dean | $16,000 | $4,000”
### `b5f9ea2ea181603d` Southern Adventist University — awards 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- checks: {"thresholds": null}
  - award_amount_text: $4,000 ⟵ “5,701-6,600 | Silver | $4,000”
### `8d9ebb5202e36f48` Tennessee Technological University — costs 2026-27 [same] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/cost.php (sha256 88176cba5638)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 17551 ⟵ “Tuition/Fees | $17,551 | $17,551”
  - on_campus:Housing: 7365 ⟵ “Housing | $7,365 | $8,403”
  - on_campus:Food: 7026 ⟵ “Food | $7,026 | $7,026”
  - on_campus:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - on_campus:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - on_campus:Personal Expenses: 2500 ⟵ “Personal Expenses | $2,500 | $2,500”
  - on_campus:TOTAL: 38522 ⟵ “TOTAL | $38,522 | $39,560”
  - with_parents_or_family:Tuition/Fees: 17551 ⟵ “Tuition/Fees | $17,551 | $17,551”
  - with_parents_or_family:Housing: 8403 ⟵ “Housing | $7,365 | $8,403”
  - with_parents_or_family:Food: 7026 ⟵ “Food | $7,026 | $7,026”
  - with_parents_or_family:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - with_parents_or_family:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - with_parents_or_family:Personal Expenses: 2500 ⟵ “Personal Expenses | $2,500 | $2,500”
  - with_parents_or_family:TOTAL: 39560 ⟵ “TOTAL | $38,522 | $39,560”
### `c0cd5d5119cf47bc` Tennessee Technological University — costs 2026-27 [same] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/cost.php (sha256 88176cba5638)
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 12685 ⟵ “Tuition/Fees | $12,685 | $12,685”
  - on_campus:Housing: 7365 ⟵ “Housing | $7,365 | $8,403”
  - on_campus:Food: 7026 ⟵ “Food | $7,026 | $7,026”
  - on_campus:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - on_campus:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - on_campus:Personal Expenses: 2500 ⟵ “Personal Expenses | $2,500 | $2,500”
  - on_campus:TOTAL: 33656 ⟵ “TOTAL | $33,656 | $34,694”
  - with_parents_or_family:Tuition/Fees: 12685 ⟵ “Tuition/Fees | $12,685 | $12,685”
  - with_parents_or_family:Housing: 8403 ⟵ “Housing | $7,365 | $8,403”
  - with_parents_or_family:Food: 7026 ⟵ “Food | $7,026 | $7,026”
  - with_parents_or_family:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - with_parents_or_family:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - with_parents_or_family:Personal Expenses: 2500 ⟵ “Personal Expenses | $2,500 | $2,500”
  - with_parents_or_family:TOTAL: 34694 ⟵ “TOTAL | $33,656 | $34,694”
### `240766763de26377` Tennessee Wesleyan University — costs 2026-27 [new] (labeled_in_source)
- source: https://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/ (sha256 513f0741ac29)
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 31880 ⟵ “Tuition | $30,650 | $31,880 | $15,940”
  - column:Clinical Fees: 2250 ⟵ “Clinical Fees | $2,150 | $2,250 | $1,125”
  - column:RN-BSN: 400 ⟵ “RN-BSN | $385 | $400 | ”
### `2270d7083ae06bce` The University of Tennessee-Chattanooga — credit_policies 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ap-exam (sha256 03c7aa93ffd4)
- checks: {"distinct_exams": 39, "equivalencies": 57, "rows_without_score": 0}
- change equivalency_count: `58` → `57`
  - equivalencies[AP-ART-HISTORY|4]:  ⟵ “Art History | 4 | ART 2140 & ART 2150 | 6 | Historical Understanding; 23GE Humanities & Fine Arts”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ART 2140 | 3 | Historical Understanding or Visual & Performing Arts; 23GE Humanities & Fine Arts”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 1110 & BIOL 1120 | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[AP-CALCULUS-AB|3]:  ⟵ “Calculus AB | 3 | MATH 1950 | 4 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[AP-CALCULUS-BC|3]:  ⟵ “Calculus BC | 3 | MATH 1950 & MATH 1960 | 8 | Mathematics; 23GE Quantitative Reasoning (1 course)”
  - equivalencies[AP-CHEMISTRY|5]:  ⟵ “Chemistry** | 5 | CHEM 1110/1110L & CHEM 1120/1120L | 8 | Lab Science; 23GE Natural Science Lecture/Lab (1 course)”
  - equivalencies[AP-CHEMISTRY|4]:  ⟵ “Chemistry** | 4 | CHEM 1110/1110L | 4 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|5]:  ⟵ “Chinese Language & Culture | 5 | FLNG 1010, FLNG 1020, FLNG 2110 & FLNG 2120 | 12 | ”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|4]:  ⟵ “Chinese Language & Culture | 4 | FLNG 1010, FLNG 1020 & FLNG 2110 | 9 | ”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese Language & Culture | 3 | FLNG 1010 & FLNG 1020 | 6 | ”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government & Politics | 3 | PSPS Elective | 3 | Behavioral & Social Sciences”
  - equivalencies[AP-COMPUTER-SCIENCE-A|4]:  ⟵ “Computer Science A | 4 | CPSC 1100 | 4 | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|4]:  ⟵ “Computer Science Principles | 4 | CPSC 1XXX | 3 | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|4]:  ⟵ “English Language & Composition | 4 | ENGL 1010 & ENGL 1020 | 6 | Rhetoric & Writing I/ Rhetoric & Writing II; 23GE Writing & Communication”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3]:  ⟵ “English Language & Composition | 3 | ENGL 1010 | 3 | Rhetoric & Writing I; 23GE Writing & Communication”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3]:  ⟵ “English Literature & Composition | 3 | ENGL 1330 | 3 | Literature; 23GE Humanities & Fine Arts”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ESC 1500 & ESC 1510 | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[AP-EUROPEAN-HISTORY|4]:  ⟵ “European History | 4 | HIST 2220 | 3 | Historical Understanding; 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|5]:  ⟵ “French Language & Culture | 5 | FREN 1010, FREN 1020, FREN 2110 & FREN 2120 | 14 | 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|4]:  ⟵ “French Language & Culture | 4 | FREN 1010, FREN 1020 & FREN 2110 | 11 | 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3]:  ⟵ “French Language & Culture | 3 | FREN 1010 & FREN 1020 | 8 | 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|5]:  ⟵ “German Language & Culture | 5 | GER 1010, GER 1020, GER 2110 & GER 2120 | 14 | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|4]:  ⟵ “German Language & Culture | 4 | GER 1010, GER 1020 & GER 2110 | 11 | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German Language & Culture | 3 | GER 1010 & GER 1020 | 8 | ”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 1040 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - … 32 more rows
### `a7a4dc495e126606` The University of Tennessee-Chattanooga — credit_policies 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/clep (sha256 891a53ce2d85)
- checks: {"distinct_exams": 33, "equivalencies": 36, "rows_without_score": 0}
- change equivalency clepbiology score 50: `BIOL 1110/1110L & BIOL 1120/1120L` → `BIOL 1110/1110L & BIOL1120/1120L`
- change equivalency clepchemistry score 50: `CHEM 1110/1110L & CHEM 1120/1120L` → `CHEM1110/1110L & CHEM1120/1120L`
- change equivalency clepenglishliterature score 50: `ENGL 2230` → `ENGL2230`
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | 50 | PSPS 1010 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science or 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | 50 | ENGL 2130 | 3 | ”
  - equivalencies[CLEP-ANALYZING-INTERPRETING-LITERATURE|50]:  ⟵ “Analyzing & Interpreting Literature | 50 | ENGL 1330 | 3 | Literature; 23GE Humanities & Fine Arts”
  - equivalencies[CLEP-BIOLOGY|50]:  ⟵ “Biology | 50 | BIOL 1110/1110L & BIOL1120/1120L | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[CLEP-CALCULUS|50]:  ⟵ “Calculus | 50 | MATH 1950 | 4 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[CLEP-CHEMISTRY|50]:  ⟵ “Chemistry | 50 | CHEM1110/1110L & CHEM1120/1120L | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50]:  ⟵ “College Algebra | 50 | MATH 1130 | 3 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|50]:  ⟵ “College Composition | 50 | ENGL 1010 & ENGL 1020 | 6 | Rhetoric & Writing I/ Rhetoric & Writing II; 23GE Writing & Communication”
  - equivalencies[CLEP-COLLEGE-COMPOSITION-MODULAR|50]:  ⟵ “College Composition Modular | 50 | ENGL 1020 | 3 | Rhetoric & Writing I/ Rhetoric & Writing II; 23GE Writing & Communication (1 course)”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50]:  ⟵ “College Mathematics | 50 | MATH 1010 | 3 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | 50 | ENGL2230 | 3 | ”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50]:  ⟵ “Financial Accounting | 50 | ACC 1XXX | 3 | ”
  - equivalencies[CLEP-FRENCH-LANGUAGE|50]:  ⟵ “French Language Level 1 | 50 | FREN 1010 & FREN 1020 | 8 | 23GE Humanities & Fine Arts and 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-FRENCH-LANGUAGE|59]:  ⟵ “French Language Level 2 | 59 | FREN 2110 & FREN 2120 | 6 | 23GE Humanities & Fine Arts and 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-GERMAN-LANGUAGE|50]:  ⟵ “German Language Level 1 | 50 | GER 1010 & GER 1020 | 8 | 23GE Humanities & Fine Arts and 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-GERMAN-LANGUAGE|60]:  ⟵ “German Language Level 2 | 60 | GER 2110 & GER 2120 | 6 | ”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50]:  ⟵ “History of the United States I | 50 | HIST 2010 | 3 | Historical Understanding; 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50]:  ⟵ “History of the United States II | 50 | HIST 2020 | 3 | Historical Understanding; 23GE Humanities & Fine Arts or 23GE Individual & Global Citizenship”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth & Development | 50 | PSY 2220 | 3 | ”
  - equivalencies[CLEP-HUMANITIES|50]:  ⟵ “Humanities | 50 | ENGL 1150 | 3 | Literature or Thoughts, Values, and Beliefs; 23GE Humanities & Fine Arts”
  - equivalencies[CLEP-INFORMATION-SYSTEMS|50]:  ⟵ “Information Systems & Computer Applications | 50 | MGT 1XXX | 3 | ”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Introduction to Educational Psychology | 50 | EDUC 2XXX | 3 | ”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50]:  ⟵ “Introductory Business Law | 50 | BUS 1XXX | 3 | ”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | 50 | PSY 1010 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | 50 | SOC 1510 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - … 11 more rows
### `ea6639e0ddc93928` The University of Tennessee-Chattanooga — credit_policies 2026-27 [same] (source_unlabeled)
- source: https://www.utc.edu/academic-affairs/registrar/prior-learning-assessment/ib-exam (sha256 90d8bdf64be6)
- checks: {"distinct_exams": 23, "equivalencies": 25, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|SL & HL]:  ⟵ “Biology | SL & HL | HL | 5,6, OR 7 | BIOL 1110 & BIOL 1120 | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[IB-BUSINESS-MANAGEMENT|SL & HL]:  ⟵ “Business Management | SL & HL | HL | 5,6, OR 7 | MGT 1XXX (Lower Division) | 3 | ”
  - equivalencies[IB-CHEMISTRY|SL & HL]:  ⟵ “Chemistry | SL & HL | HL | 5,6, OR 7 | CHEM 1110/1110L & CHEM 1120/1120L | 8 | Lab Science; 23GE Natural Science Lecture/Lab (1 course)”
  - equivalencies[IB-LATIN|SL & HL]:  ⟵ “Classical Languages-Latin | SL & HL | HL | 5,6, OR 7 | LAT 1010 & LAT 1020 | 6 | 23GE Humanities & Fine Arts”
  - equivalencies[IB-COMPUTER-SCIENCE|SL & HL]:  ⟵ “Computer Science | SL & HL | HL | 5,6, OR 7 | CPSC 1XXX | 3 | ”
  - equivalencies[IB-ECONOMICS|SL & HL]:  ⟵ “Economics | SL & HL | HL | 5,6, OR 7 | ECON 1010 & ECON 1020 | 6 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|SL Only]:  ⟵ “Environmental Systems & Societies | SL Only | SL | 5,6, OR 7 | ESC 1100 | 3 | Non-Lab Science; 23GE Natural Science Non-Lab”
  - equivalencies[IB-FILM|SL & HL]:  ⟵ “Film | SL & HL | HL | 5,6, OR 7 | THSP 2800 | 3 | Visual & Performing Arts; 23GE Humanities & Fine Arts”
  - equivalencies[IB-GEOGRAPHY|SL & HL]:  ⟵ “Geography | SL & HL | HL | 5,6, OR 7 | GEOG 1040 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - equivalencies[IB-GLOBAL-POLITICS|SL & HL]:  ⟵ “Global Politics | SL & HL | HL | 5,6, OR 7 | PSPS 1020 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science or 23GE Individual & Global Citizenship”
  - equivalencies[IB-HISTORY|SL & HL]:  ⟵ “History of Africa and the Middle East* | SL & HL | HL | 5,6, OR 7 | HIST 1XXX (Lower Division) | 3 | Historical Understanding; 23GE Humanities & Fine Arts”
  - equivalencies[IB-FRENCH|SL & HL]:  ⟵ “Language B-French | SL & HL | HL | 5,6, OR 7 | FREN 1010 & FREN 1020 | 8 | 23GE Humanities & Fine Arts; 23GE Individual & Global Citizenship”
  - equivalencies[IB-GERMAN|SL & HL]:  ⟵ “Language B-German | SL & HL | HL | 5,6, OR 7 | GER 1010 & GER 1020 | 8 | ”
  - equivalencies[IB-SPANISH|SL & HL]:  ⟵ “Language B-Spanish | SL & HL | HL | 5,6, OR 7 | SPAN 1010 & SPAN 1020 | 8 | 23GE Humanities & Fine Arts; 23GE Individual & Global Citizenship”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL & HL]:  ⟵ “Mathematics - Analysis & Approaches | SL & HL | HL | 5,6, OR 7 | MATH 1950 | 4 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL & HL]:  ⟵ “Mathematics - Analysis & Approaches | SL & HL | HL | 4 | MATH 1830 | 3 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|SL & HL]:  ⟵ “Mathematics - Analysis & Approaches | SL & HL | SL | 5,6, OR 7 | MATH 1010, MATH 1730 | 3, 4 | Mathematics; 23GE Quantitative Reasoning (2 courses)”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|SL & HL]:  ⟵ “Mathematics - Applications & Interpretation | SL & HL | HL | 5,6, OR 7 | MATH 1010, MATH 1730 | 3 | Mathematics; 23GE Quantitative Reasoning”
  - equivalencies[IB-MUSIC|SL & HL]:  ⟵ “Music | SL & HL | HL | 5,6, OR 7 | MUS 1XXX (Lower Division) | 3 | ”
  - equivalencies[IB-PHILOSOPHY|SL & HL]:  ⟵ “Philosophy | SL & HL | HL | 5,6, OR 7 | PHIL 1010 | 3 | Thoughts, Values & Beliefs; 23GE Humanities & Fine Arts”
  - equivalencies[IB-PHYSICS|SL & HL]:  ⟵ “Physics | SL & HL | HL | 5,6, OR 7 | PHYS 1030/1030L & PHYS 1040/1040L | 8 | Lab Science; 23GE Natural Science Lecture/Lab”
  - equivalencies[IB-PSYCHOLOGY|SL & HL]:  ⟵ “Psychology | SL & HL | HL | 5,6, OR 7 | PSY 1010 | 3 | Behavioral & Social Sciences; 23GE Behavioral & Social Science”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|SL & HL]:  ⟵ “Social & Cultural Anthropology | SL & HL | HL | 5,6, OR 7 | ANTH 1200 | 3 | Non-Western Culture; 23GE Behavioral & Social Science or 23GE Individual & Global Citizenship”
  - equivalencies[IB-THEATRE|SL & HL]:  ⟵ “Theatre | SL & HL | HL | 5,6, OR 7 | THSP 1110 | 3 | Visual & Performing Arts; 23GE Humanities & Fine Arts”
  - equivalencies[IB-VISUAL-ARTS|SL & HL]:  ⟵ “3"Visual Arts" | SL & HL | HL | 5,6, OR 7 | ART 1XXX (Lower Division) | 3 | ”
### `5a3271bb53de777d` The University of Tennessee-Knoxville — awards 2026-27 [new] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/orange-white-scholarship/ (sha256 83cddaa5b9fc)
- checks: {"thresholds": null}
  - test_requirement: 3.6+ GPA*,26-27 ACT**,1230-1290 SAT** ⟵ “3.6+ GPA*,26-27 ACT**,1230-1290 SAT** | $1,500 | $6,000 | $26,400”
  - award_amount_text: $1,500 ⟵ “3.6+ GPA*,26-27 ACT**,1230-1290 SAT** | $1,500 | $6,000 | $26,400”
### `b0e10e40d9e08eef` The University of Tennessee-Knoxville — awards 2026-27 [new] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/next-chapter-scholarship-next-chapter-scholar-of-the-year-award/ (sha256 5e9a2df6649e)
- checks: {"thresholds": null}
  - award_amount_text: Tuition & mandatory fees ⟵ “Next Chapter Scholar of the Year | Tuition & mandatory fees | Tuition & mandatory fees up to four years | n/a”
### `b48d5b7112f80f1c` The University of Tennessee-Knoxville — awards 2026-27 [new] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/orange-white-scholarship/ (sha256 83cddaa5b9fc)
- checks: {"thresholds": null}
  - test_requirement: 3.6–3.79 GPA*,28–36 ACT**,1300–1600 SAT** ⟵ “3.6–3.79 GPA*,28–36 ACT**,1300–1600 SAT** | $1,500 | $6,000 | $26,400”
  - award_amount_text: $1,500 ⟵ “3.6–3.79 GPA*,28–36 ACT**,1300–1600 SAT** | $1,500 | $6,000 | $26,400”
### `68440b83cdef6c5f` Union University — costs 2026-27 [same] (labeled_in_source)
- source: https://www.uu.edu/admissions/financial-aid/cost-of-attendance/ (sha256 d4a181e7ef8d)
- checks: {"columns": 1, "components_reconcile": true, "rows": 11}
  - column:Tuition: 41170 ⟵ “Tuition | $41,170 | 12-16 hours per semester as a block rate”
  - column:Mandatory Fees: 1520 ⟵ “Mandatory Fees | $1,520 | This does not include a one-time $185 Orientation fee for first-time Union students.”
  - column:Housing: 10800 ⟵ “Housing | $10,800 | This is the cost for The Quads Apartments; your costs could differ depending on your housing option.”
  - column:Food/Meals: 6636 ⟵ “Food/Meals | $6,636 | This is the 285 meal-plan; your costs could differ depending on your meal-plan selection.”
  - column:Books, Course Materials, Supplies, and Equipment: 750 ⟵ “Books, Course Materials, Supplies, and Equipment | $750 | This is an estimate using the Buster Book Bundle; your costs could differ depending on how you purchase your books”
  - column:Transportation: 3316 ⟵ “Transportation | $3,316 | This is an estimate for transportation fees you may incur over the year for items such as traveling to class or trips home; your costs could vary greatly depending on your situation.”
  - column:Loan Fees: 130 ⟵ “Loan Fees | $130 | This is an estimate for the average cost of Federal student loan fees such as origination fees; your costs could vary based on your decisions to borrow, contact SFP for more information.”
  - column:Personal Expenses: 11154 ⟵ “Personal Expenses | $11,154 | This is an estimate of costs for day-to-day expenses you may have over the next academic year. Your costs could vary greatly based on your situation and financial decisions.”
  - column:Total COA: 75476 ⟵ “Total COA | $75,476 | Total allowable Cost of Attendance for on-campus, traditional undergraduate students (prior to application of any financial aid eligibility)”
  - column:Total Direct Costs: 60126 ⟵ “Total Direct Costs | $60,126 | This is prior to any applied financial aid — but GREAT news, financial aid is available!”
  - column:Total Indirect Costs: 15350 ⟵ “Total Indirect Costs | $15,350 | ”

## Exceptions (146)

### `a3f79857e8370910` American Baptist College — appeals 2024-25 [new] (labeled_in_title)
- source: https://abcnash.edu/wp-content/uploads/2024/06/2024-2025-Special-Circumstances-Form.pdf (sha256 a51d02490624)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “2024-2025 Special Circumstance Request This form is used to request a reevalua on of the informa on you provided on the Free Applica on for Federal Student Aid (FAFSA) due to special circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Other Unusual Circumstances Personal statement, with suppor ng documenta on from a third-party such as teacher, clergy, counselor, medical or government authority/agency, or court that is aware of the circumstances that exist such as abandonment by parents, abusive family environment that threatens the health and safety of the student, unable to locate parents, risk of being homeless, or unaccompa”
### `45922000363d9d33` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/financialaid/forms/appeal-forms.php (sha256 dde578b5975c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Satisfactory Academic Progress Appeal Form - This form must be completed when a student has been notified by the Student Financial Aid Office that they are in violation of the Satisfactory Academic Progress Policy Guidelines.”
### `571942e8b8540597` Austin Peay State University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.apsu.edu/financialaid/sat_prog.php (sha256 0d9d1196ea37)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal Submission Information: SAP appeals and academic reviews may be submitted at any time, but it is best to appeal early to prevent delays in your financial aid if approved.”
  - sentence: sap_appeal ⟵ “Students may view their Inclusive Combined GPA on OneStop > Web Self Service > Student > Student Records > Student GPA. 2025-2026 SAP Policy SAP Policy Guidelines SAP Appeal Form SAP Appeal Form This form should be completed when a student has been notified by the Office of Student Financial Aid that their SAP status requires an appeal.”
  - sentence: sap_appeal ⟵ “Supporting Letter for SAP Appeal This form may be completed by a third party in support of a student's appeal in place of a letter of support.”
### `5b11613e6b917671` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/financialaid/types-of-aid-scholarships/grants/federal-grants.php (sha256 18fac647ff2c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Exceptions to this policy are granted based on professional judgment.”
### `87eae9e7589c86df` Austin Peay State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.apsu.edu/scholarships/tn-education-lottery-programs/lottery-appeals.php (sha256 7e4d78c05f7b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If the initial appeal is denied, the student may file a new appeal to the TSAC HOPE Lottery Scholarship Award Appeal Panel at the following address: Tennessee Education Lottery Scholarship 404 James Robertson Parkway Suite 1950, Parkway Towers Nashville, TN 37243-0820 Further Information pertaining to appealing your loss through TSAC may be reviewed here.”
### `9d0311e2650e14ec` Austin Peay State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.apsu.edu/financialaid/special-circumstance-request.php (sha256 6883da29bcd8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Department of Veterans Affairs VA Education Benefits Applicant Checklists VA Education Benefits Information GI Bill® Comparison Tool VA Veteran Readiness & Employment VA Work Study Principles of Excellence Faculty and Staff Resources Guide for Faculty and Staff Functional Support Request Form Financial Aid for Transfer Students Special Circumstance Request A Special Circumstance Request form is co”
  - sentence: need_based_special_circumstances ⟵ “The three reasons to complete this form are: Loss of Employment/Income Divorce or Separation Death of a Spouse/Parent* If the student has any one of these reasons, they may complete a Special Circumstance Request as long as: Verification is completed, if selected.”
  - sentence: need_based_special_circumstances ⟵ “Christopher hears about the Special Circumstance Request from an email from the Financial Aid Office, and decides to complete the request.”
  - sentence: need_based_special_circumstances ⟵ “Unfortunately, the Special Circumstances Request will not benefit Christopher.”
  - sentence: need_based_special_circumstances ⟵ “Heather hears from her advisor that she can complete a Special Circumstance Request to exclude her ex-spouse’s financial information from the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Toggle Death of a Parent/Spouse Example 1 John’s spouse lost a battle with cancer in 2024, and he heard from a friend that he could complete a Special Circumstance Request with the Financial Aid Office to see if his spouse’s income could be excluded from his eligibility for need-based aid.”
### `bcea59526a718eb0` Austin Peay State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.apsu.edu/financialaid/special-circumstance-request.php (sha256 6883da29bcd8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Rather, if the student does not maintain a relationship with their other parent, they may qualify for a dependency override.”
### `0922c368b4c4a5d6` Austin Peay State University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.apsu.edu/scholarships/academic-scholarship-staff-resources.php (sha256 ed144e59d775)
- issues: ambiguous_year_labels
- checks: {"thresholds": {"gpa_min": 2.75}}
  - gpa_requirement: 2.75 ⟵ “Howell C. Smith (Freshman) | 2.75 | 75 per semester | 8 | Full time”
### `1f99b4807981a8b1` Austin Peay State University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.apsu.edu/scholarships/academic-scholarship-staff-resources.php (sha256 ed144e59d775)
- issues: ambiguous_year_labels
- checks: {"thresholds": {"gpa_min": 3.0}}
  - gpa_requirement: 3.0 ⟵ “Luther Tippit | 3.0 | 6 hours per week | 8 | Full time”
### `769b649b0c4b43ee` Baptist Health Sciences University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.baptistu.edu/tuition-financial-aid/scholarships-grants/hope-scholarships/hope-lottery-scholarship-appeal (sha256 153cceb96e08)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Click the following link to get additional information regarding the HOPE Lottery Scholarship appeals process.”
### `9ce763f0efccfb7c` Belmont University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.belmont.edu/sfs/financial-aid/ (sha256 1afbe0465444)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals add VIII.”
  - sentence: sap_appeal ⟵ “Fax To: (615) 460-6141 Attn: SAP Appeals Committee Physically Mail To: SAP APPEALS COMMITTEE Office of Student Financial Services Belmont University 1900 Belmont Boulevard Nashville, TN 37212 IX.”
### `29736b6759a949b0` Belmont University — costs 2025-26 [same] (labeled_in_source)
- source: https://www.belmont.edu/admissions/military/tuition-aid.html (sha256 c176e9bcff4f)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 3}
  - column:Tuition and Fees: 43750 ⟵ “Tuition and Fees | $43,750”
  - column:Residence Hall and Meal Plan*: 15530 ⟵ “Residence Hall and Meal Plan* | $15,530”
  - column:Total Estimated Cost for 2025-2026**: 59280 ⟵ “Total Estimated Cost for 2025-2026** | $59,280”
### `2e46094332e150e1` Bryan College-Dayton — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bryan.edu/admissions/financial-aid/ (sha256 1c67ddc8269d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If the process requires our office to make corrections to your FAFSA and those changes necessitate a change in your financial aid award you will receive a revised award letter within two to three weeks that will replace your previous award offer.”
### `aaaa3c8acbafdbdd` Bryan College-Dayton — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.bryan.edu/admissions/financial-aid/ (sha256 1c67ddc8269d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Process A student who feels mitigating circumstances existed that adversely affected the student‘s ability to maintain satisfactory academic progress may submit a written appeal within five business days of receiving notification of the suspension status.”
### `21d4fe4defd6af6a` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf (sha256 485c9c14b0e0)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Professional Judgment refers to the school’s authority to make adjustments to the data elements reported on the Free Application for Federal Student Aid (FAFSA) so that the Department of Education can recalculate the Expected Family Contribution (SAI).”
### `9a414a7fda18d2f9` Carson-Newman University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-forms/ (sha256 aafa321b77f2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “Dependency Override Appeal Application – A student may need to request an override to their dependency status due to unusual and unavoidable circumstances.”
  - sentence: dependency_override ⟵ “A Dependency Status Appeal Application is considered on a case-by-case basis depending on the situation and supporting documentation provided.”
  - sentence: dependency_override ⟵ “Dependency Override Appeal Application – A student may need to request an override to their dependency status due to unusual and unavoidable circumstances.”
  - sentence: dependency_override ⟵ “A Dependency Status Appeal Application is considered on a case-by-case basis depending on the situation and supporting documentation provided.”
### `a39b0f7ffe5bc88d` Carson-Newman University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/financial-aid-forms/ (sha256 aafa321b77f2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
  - sentence: need_based_special_circumstances ⟵ “Keep in mind that in order to submit a Special Circumstance Appeal for the 2026-27 academic year, the 2025 taxes must be complete to attach to the appeal, and the student must have already received his/her original aid offer.”
  - sentence: need_based_special_circumstances ⟵ “Independent Special Circumstance Appeal Form – Please complete this form along with supporting documentation if you have suffered a loss of income.”
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
  - sentence: need_based_special_circumstances ⟵ “Fall 2025, Spring 2026 & Summer 2026 Dependent Verification Worksheet Independent Verification Worksheet Dependent Special Circumstance Appeal Form – Please complete this form along with supporting documentation if you have suffered a loss of income.”
  - sentence: need_based_special_circumstances ⟵ “Verification paperwork is attached to the Special Circumstances Appeal form.”
### `c5b64478c3915333` Carson-Newman University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cn.edu/wp-content/uploads/2024/06/SAP-Appeal-Form97.pdf (sha256 2c19589aa0af)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Carson-Newman University Financial Aid Office • 1645 Russell Avenue • Jefferson City, TN 37760 Financial Aid Office • (800) 678-9061 • (865) 471-3247 • Fax (865) 471-2035 financialaid@cn.edu • www.cn.edu Satisfactory Academic Progress Appeal Form Satisfactory Academic Progress (SAP) Overview Federal regulations require that all students meet minimum qualitative (grades) and minimum quantitative (h”
  - sentence: sap_appeal ⟵ “SAP Appeal Process If extenuating circumstances precluded you from meeting the standards, you may file an appeal.”
### `ff3c105c924193b6` Carson-Newman University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.cn.edu/wp-content/uploads/2025/03/2025-2026-Special-Circum-Dependent-Appeal.pdf (sha256 485c9c14b0e0)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Carson-Newman University 2025-2026 Special Circumstances Appeal for Dependent Students ______________________________________________________________ ___________________________________ Student’s Last Name Student’s First Name Student’s M.I.”
  - sentence: need_based_special_circumstances ⟵ “Student’s Identification (ID) Number ______________________________________________________________ ___________________________________ Student’s E-Mail Address Student’s Home/Cell Phone Number This Appeal is a request for a review of special circumstances that you feel may change your financial aid eligibility.”
  - sentence: need_based_special_circumstances ⟵ “Please note: Loss of income for the 2023 IRS Tax Return calendar year will NOT be considered for special circumstances ___ Copy of 2024 IRS Tax Return Transcript or signed copy of 2024 appeal as this process will be based on current year data only.”
### `680edc336ef08717` Carson-Newman University — awards 2025-26 [same] (labeled_in_source)
- source: https://www.cn.edu/admissions-and-aid/financial-aid/types-of-aid/scholarships/ (sha256 7efc1d4354f8)
- issues: stale_year_label:2025-26
- checks: {"thresholds": null}
  - award_tiers: [{'gpa': '2.2', 'amount_text': '$8,000'}, {'gpa': '2.75', 'amount_text': '$10,000'}, {'gpa': '3.5', 'amount_text': '$12,000'}, {'gpa': '3.75', 'amount_text': '$14,000'}, {'gpa': '3.9', 'amount_text': '$16,000'}] ⟵ “GPA | Merit || 2.2 | $8,000 || 2.75 | $10,000 || 3.5 | $12,000 || 3.75 | $14,000 || 3.9 | $16,000”
  - gpa_requirement: Tiered by GPA: 2.2 → $8,000; 2.75 → $10,000; 3.5 → $12,000; 3.75 → $14,000; 3.9 → $16,000 ⟵ “GPA | Merit || 2.2 | $8,000 || 2.75 | $10,000 || 3.5 | $12,000 || 3.75 | $14,000 || 3.9 | $16,000”
### `0799d6ff74a54eb8` Christian Brothers University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.cbu.edu/admissions-aid/financial-aid/types-of-financial-aid/scholarships/ (sha256 d4fc687bc259)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “DOWNLOAD THE TELS REQUEST FOR CHANGE OF ENROLLMENT STATUS FORM HOPE FAQ’s Appeals Students should submit a letter detailing the reason for dropping below full-time.”
### `36ce060dc56a3efb` Christian Brothers University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.cbu.edu/admissions-aid/financial-aid/financial-aid-forms/ (sha256 f885c121466d)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Satisfactory Progress for Title IV (PDF) Satisfactory Progress Appeal Form (PDF) Disclaimer: Information contained on this site is subject to change without prior notification.”
### `5f98c0c74b1a7ab8` Christian Brothers University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.cbu.edu/admissions-aid/financial-aid/financial-aid-resources/ (sha256 ae1545efd9e7)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Professional Judgment The Higher Education Act of 1965, as amended (HEA) provides the authority for the financial aid administrator to exercise discretion in a number of areas when a student has special or unusual circumstances.”
  - sentence: professional_judgment ⟵ “This authority is known as professional judgment (PJ).”
### `9b44529bb215776a` Dyersburg State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.dscc.edu/wp-content/uploads/2024/11/COA-Adjustment-Request-Form.pdf (sha256 14207191c1a2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: budget_increase ⟵ “Office of Financial Aid 1510 Lake Rd | Dyersburg, TN 38024 financialaid@dscc.edu Fax: 731-286-3354 Phone: 731-286-3350 Cost of Attendance Adjustment Request Student’s Name: Student ID: The Cost of Attendance Adjustment form is for students who have additional expenses during the enrollment period, such as childcare costs, laptops, and supplies.”
  - sentence: budget_increase ⟵ “Cost of Attendance reviews will take place after you complete the FAFSA, and after you receive a financial aid offer notification for the year in which you are requesting a cost of attendance adjustment.”
### `561ec105ce9babd5` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/documents/2627-dependency-override-appeal-online.pdf (sha256 e9dd7116362d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “A dependency override occurs when a financial aid administrator exercises professional judgment and overrides the Department of Education’s criteria for dependent students.”
### `6e91a4c0697d56b6` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: need_based_special_circumstances ⟵ “There are two different appeal processes available to you and your family: Special Circumstances Appeal Dependency Override For ETSU to grant an appeal, there must be compelling reasons.”
  - sentence: need_based_special_circumstances ⟵ “The first step is to be sure to select the correct forms for the aid year in which you are submitting an appeal. 2026-2027 Forms Special Circumstance Appeal Dependency Override Returning ETSU Students Only: If you were approved last year for a Dependency Override and have submitted your 2026-27 FAFSA application to ETSU, your process is different.”
  - sentence: need_based_special_circumstances ⟵ “If you have any questions, please make an appointment with our Assistant Director of Training and Service by selecting the 'Special Circumstance Appeals' option.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstances Should I Appeal?”
  - sentence: need_based_special_circumstances ⟵ “What Special Circumstances We DO Consider: Loss or change of employment Loss or change in untaxed income (child support, Social Security, or other benefits) Divorce or separation of parents or student Death of parent(s) or spouse Unusual medical expenses (not covered by insurance) One-time taxable income used for life changing events (e.g.”
### `b486f83c56b8d175` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “If your circumstances have not changed since last year, please provide the following to the Office of Financial Aid and Scholarships in person or via email at finaid@etsu.edu. · Signed 2026-27 Dependency Override Appeal form · Signed, dated statement outlining your circumstances and that they have not changed.”
  - sentence: dependency_override ⟵ “Dependency Override For financial aid purposes, a student is considered a dependent of their parents unless the student is: 24 years old married serving on active duty in the US Armed Forces a veteran a parent with dependents an emancipated minor homeless assigned a legal guardian before the age of 18 How to Appeal Contact our Assistant Director of Training and Service to discuss your circumstance”
### `b8ca9c0b36f75d8f` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/forms/appeal_forms.php (sha256 4cb91f9b9fb1)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeals Academic Appeal Forms and Links In certain circumstances, students have the option to appeal based on their academic performance.”
### `e6d3639b1d4f4e47` East Tennessee State University — appeals 2026-27 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/scholarships/hope/appeals.php (sha256 f6e32412720e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “If you receive notice that you have lost your eligibility for a TELS award, you will need to submit an appeal to the Office of Financial Aid and Scholarships as soon as possible.”
### `ff4d413d81bce367` East Tennessee State University — appeals 2027-28 [new] (labeled_in_source)
- source: https://www.etsu.edu/financial-aid-and-scholarships/ (sha256 eba080aff84c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “General Assembly Merit Scholarship (GAMS) Aspire Award Non-Traditional Lottery Don’t Lose Hope Appeals Process for Hope Getting Help Cost of Attendance Financial Aid TV GoldLink Guide Bucky's Treasure Map Schedule an Appointment Financial Aid Steps School Code 003487 1 | Submit FAFSA 2 | Verification 3 | Check Status 4 | Aid Offers 5 | Confirm Registration 6 | Majors & MinorsCost EstimateRequest I”
### `71c6333bad7156f5` Freed-Hardeman University — appeals 2026-27 [new] (source_unlabeled)
- source: https://fhu.edu/admissions-aid/financial-aid/grants-scholarships-discounts/hope-scholarship/ (sha256 91f79fdad76a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “The student must complete a HOPE Scholarship Appeal Form (for the reasons listed above)and submit it to the Director of Financial Aid.”
  - sentence: scholarship_retention_appeal ⟵ “Appeals should be submitted within 30 days of notification of the loss of the HOPE Scholarship.”
### `55e5b24f660564cb` Jackson State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://jscc.edu/costs-and-aid/satisfactory-academic-progress-sap/ (sha256 6994832800fb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeal Process (§ 668.34, (d) (2)): Students can file a Financial Aid appeal to regain eligibility if there were extenuating circumstances that warrant a student to continue receiving Title IV and/or State aid. (§ 668.34, (a) (9) (ii)) To successfully appeal the student must: Complete and submit a Satisfactory Academic Progress Appeal An Academic Plan may also be required.”
  - sentence: sap_appeal ⟵ “Financial Aid Probation Approved status is assigned to a student who fails to meet satisfactory academic progress guidelines, submitted an appeal, the appeal was approved, and the student is projected to meet satisfactory academic progress standards or complete their degree within one semester.”
### `9b8064fff3f0aa2c` Jackson State Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/financial-aid-forms/ (sha256 90d77634db14)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Appeal Process Any loss of eligibility for financial aid because of this policy may be appealed by submitting an online SAP Appeal form to the Student Aid & Awards Committee.”
  - sentence: sap_appeal ⟵ “Appeal Process Students must: Submit the online Satisfactory Academic Progress Appeal form.”
  - sentence: sap_appeal ⟵ “The Financial Aid Office will notify, by letter or email to the student’s JSCC email address, any student that does not meet minimum satisfactory academic progress requirements as well as the results of any appeal.”
### `1b69e78af564fa8c` Jackson State Community College — costs 2025-26 [same] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_per_semester": true, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:TUITION & FEES*: 4127 ⟵ “TUITION & FEES* | $4,127 | $4,127 | $4,127”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3550 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - with_parents_or_family:TOTAL: (FOR FALL AND SPRING): 23684 ⟵ “TOTAL: (FOR FALL AND SPRING) | $23,684 | $31,532 | $21,068”
  - off_campus_not_with_family:TUITION & FEES*: 4127 ⟵ “TUITION & FEES* | $4,127 | $4,127 | $4,127”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7474 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - off_campus_not_with_family:TOTAL: (FOR FALL AND SPRING): 31532 ⟵ “TOTAL: (FOR FALL AND SPRING) | $23,684 | $31,532 | $21,068”
  - other:TUITION & FEES*: 4127 ⟵ “TUITION & FEES* | $4,127 | $4,127 | $4,127”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2242 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - other:TOTAL: (FOR FALL AND SPRING): 21068 ⟵ “TOTAL: (FOR FALL AND SPRING) | $23,684 | $31,532 | $21,068”
### `5d54c691bf20f7c4` Jackson State Community College — costs 2026-27 [same] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile
- checks: {"columns": 3, "components_per_semester": true, "components_reconcile": false, "rows": 6}
  - with_parents_or_family:TUITION & FEES*: 4275 ⟵ “TUITION & FEES* | $4,275 | $4,275 | $4,275”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3841 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - with_parents_or_family:TOTAL: (FOR FALL AND SPRING): 24796 ⟵ “TOTAL: (FOR FALL AND SPRING) | $24,796 | $32,791 | $22,131”
  - off_campus_not_with_family:TUITION & FEES*: 4275 ⟵ “TUITION & FEES* | $4,275 | $4,275 | $4,275”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7838 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - off_campus_not_with_family:TOTAL: (FOR FALL AND SPRING): 32791 ⟵ “TOTAL: (FOR FALL AND SPRING) | $24,796 | $32,791 | $22,131”
  - other:TUITION & FEES*: 4275 ⟵ “TUITION & FEES* | $4,275 | $4,275 | $4,275”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 756 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $756 | $756 | $756”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2508 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,841 | $7,838 | $2,508”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2719 ⟵ “TRANSPORTATION | $2,719 | $2,719 | $2,719”
  - other:TOTAL: (FOR FALL AND SPRING): 22131 ⟵ “TOTAL: (FOR FALL AND SPRING) | $24,796 | $32,791 | $22,131”
### `aa3ea81c29360aed` Jackson State Community College — costs 2025-26 [same] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_per_semester": true, "components_reconcile": true, "rows": 6}
  - with_parents_or_family:TUITION & FEES*: 2447 ⟵ “TUITION & FEES* | $2,447 | $2,447 | $2,447”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3550 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - with_parents_or_family:TOTAL: (FOR FALL AND SPRING): 20324 ⟵ “TOTAL: (FOR FALL AND SPRING) | $20,324 | $28,172 | $17,708”
  - off_campus_not_with_family:TUITION & FEES*: 2447 ⟵ “TUITION & FEES* | $2,447 | $2,447 | $2,447”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7474 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - off_campus_not_with_family:TOTAL: (FOR FALL AND SPRING): 28172 ⟵ “TOTAL: (FOR FALL AND SPRING) | $20,324 | $28,172 | $17,708”
  - other:TUITION & FEES*: 2447 ⟵ “TUITION & FEES* | $2,447 | $2,447 | $2,447”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2242 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,550 | $7,474 | $2,242”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2625 ⟵ “TRANSPORTATION | $2,625 | $2,625 | $2,625”
  - other:TOTAL: (FOR FALL AND SPRING): 17708 ⟵ “TOTAL: (FOR FALL AND SPRING) | $20,324 | $28,172 | $17,708”
### `c7a99776d893d923` Jackson State Community College — costs 2024-25 [new] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 3, "components_per_semester": true, "components_reconcile": false, "rows": 6}
  - with_parents_or_family:TUITION & FEES*: 2370 ⟵ “TUITION & FEES* | $2,370 | $2,370 | $2,370”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3452 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - with_parents_or_family:TOTAL (FOR FALL AND SPRING): 19748 ⟵ “TOTAL (FOR FALL AND SPRING) | $19,748 | $27,380 | $17,205”
  - off_campus_not_with_family:TUITION & FEES*: 2370 ⟵ “TUITION & FEES* | $2,370 | $2,370 | $2,370”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7268 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - off_campus_not_with_family:TOTAL (FOR FALL AND SPRING): 27380 ⟵ “TOTAL (FOR FALL AND SPRING) | $19,748 | $27,380 | $17,205”
  - other:TUITION & FEES*: 2370 ⟵ “TUITION & FEES* | $2,370 | $2,370 | $2,370”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2180 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - other:TOTAL (FOR FALL AND SPRING): 17205 ⟵ “TOTAL (FOR FALL AND SPRING) | $19,748 | $27,380 | $17,205”
### `ec5390b5f13ce6f5` Jackson State Community College — costs 2024-25 [new] (labeled_in_source)
- source: https://jscc.edu/costs-and-aid/tuition/coa/ (sha256 ce189edff644)
- issues: components_do_not_reconcile, stale_year_label:2024-25
- checks: {"columns": 3, "components_per_semester": true, "components_reconcile": false, "rows": 6}
  - with_parents_or_family:TUITION & FEES*: 8862 ⟵ “TUITION & FEES* | $8,862 | $8,862 | $8,862”
  - with_parents_or_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - with_parents_or_family:LIVING EXPENSES** (FOOD & HOUSING): 3452 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - with_parents_or_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - with_parents_or_family:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - with_parents_or_family:TOTAL (FOR FALL AND SPRING): 32732 ⟵ “TOTAL (FOR FALL AND SPRING) | $32,732 | $40,364 | $30,189”
  - off_campus_not_with_family:TUITION & FEES*: 8862 ⟵ “TUITION & FEES* | $8,862 | $8,862 | $8,862”
  - off_campus_not_with_family:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - off_campus_not_with_family:LIVING EXPENSES** (FOOD & HOUSING): 7268 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - off_campus_not_with_family:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - off_campus_not_with_family:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - off_campus_not_with_family:TOTAL (FOR FALL AND SPRING): 40364 ⟵ “TOTAL (FOR FALL AND SPRING) | $32,732 | $40,364 | $30,189”
  - other:TUITION & FEES*: 8862 ⟵ “TUITION & FEES* | $8,862 | $8,862 | $8,862”
  - other:BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT: 732 ⟵ “BOOKS, COURSE MATERIALS, SUPPLIES, & EQUIPMENT | $732 | $732 | $732”
  - other:LIVING EXPENSES** (FOOD & HOUSING): 2180 ⟵ “LIVING EXPENSES** (FOOD & HOUSING) | $3,452 | $7,268 | $2,180”
  - other:MISC/PERSONAL**: 808 ⟵ “MISC/PERSONAL** | $808 | $808 | $808”
  - other:TRANSPORTATION: 2513 ⟵ “TRANSPORTATION | $2,513 | $2,513 | $2,513”
  - other:TOTAL (FOR FALL AND SPRING): 30189 ⟵ “TOTAL (FOR FALL AND SPRING) | $32,732 | $40,364 | $30,189”
### `366d8a46feeef067` John A Gupton College — appeals 2026-27 [new] (source_unlabeled)
- source: https://guptoncollege.edu/financial-aid-2/satisfactory-academic-scholarship/ (sha256 79b39af941b6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “All probations may be appealed in writing by completing a Satisfactory Academic Progress Appeal Form (located in the Financial Aid Office).”
### `c96122740761a068` John A Gupton College — appeals 2026-27 [new] (source_unlabeled)
- source: https://guptoncollege.edu/financial-aid-2/satisfactory-academic-scholarship/ (sha256 79b39af941b6)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “All appeals must include documentation of any unusual circumstance that contributed to the probation.”
### `ec13587355f11203` Johnson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://johnsonu.edu/admissions/financial-aid/financial-aid-faqs/ (sha256 d4309be67e46)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You may have a special circumstance and will need to contact the financial aid director with a detailed explanation of your circumstance.”
### `bd01a5b44bc7ab34` Johnson University — costs 2026-27 [new] (labeled_in_source)
- source: https://johnsonu.edu/admissions/tuition/ (sha256 c6d142054952)
- issues: arrangement_unlabeled
- checks: {"columns": 2, "rows": 8}
  - column:Tuition/Fees: 22612 ⟵ “Tuition/Fees | $22,612 | $8,496”
  - column:Housing/Food: 9501 ⟵ “Housing/Food | $9,501 | $4,750”
  - column:Transportation: 3220 ⟵ “Transportation | $3,220 | $1,610”
  - column:Books/Supplies: 1200 ⟵ “Books/Supplies | $1,200 | $600”
  - column:Personal: 1600 ⟵ “Personal | $1,600 | $800”
  - column:Loan Fees: 68 ⟵ “Loan Fees | $68 | $68”
  - column:Annual COA: 38200 ⟵ “Annual COA | $38,200 | $16,324”
  - column:Semester COA: 19100 ⟵ “Semester COA | $19,100 | $8,162”
  - column:Tuition/Fees: 8496 ⟵ “Tuition/Fees | $22,612 | $8,496”
  - column:Housing/Food: 4750 ⟵ “Housing/Food | $9,501 | $4,750”
  - column:Transportation: 1610 ⟵ “Transportation | $3,220 | $1,610”
  - column:Books/Supplies: 600 ⟵ “Books/Supplies | $1,200 | $600”
  - column:Personal: 800 ⟵ “Personal | $1,600 | $800”
  - column:Loan Fees: 68 ⟵ “Loan Fees | $68 | $68”
  - column:Annual COA: 16324 ⟵ “Annual COA | $38,200 | $16,324”
  - column:Semester COA: 8162 ⟵ “Semester COA | $19,100 | $8,162”
### `615637bc9e6b1235` Lane College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.lanecollege.edu/financial-aid-tuition/financial-aid-sap (sha256 3bb451938f69)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 9}
  - sentence: sap_appeal ⟵ “Appeals Students placed on Financial Aid Suspension may appeal to the SAP Appeal Committee for the following reasons: serious illness or accident related to the student; death, accident, or serious illness in the immediate family (parent/guardian or sibling); and/or other extenuating circumstances directly affecting academic performance.”
  - sentence: sap_appeal ⟵ “Appeal Process Students must submit a completed SAP Appeal Form to the Office of Financial Aid.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Form will be sent to the student.”
  - sentence: sap_appeal ⟵ “Completed SAP Appeals will be reviewed within two weeks of submission.”
  - sentence: sap_appeal ⟵ “Tips for Writing a Successful Appeal You have the right to appeal your Financial Aid Satisfactory Academic Progress Suspension.”
  - sentence: sap_appeal ⟵ “Be honest with yourself and the FA SAP Appeal Committee.”
### `ad019c293b3caa1a` Lane College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.lanecollege.edu/financial-aid-tuition/federal-and-state-aid/dependency-and-verification (sha256 541d1cd40340)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Parental information must be included on the FAFSA unless the student is: an orphan or ward of the court a veteran a graduate of professional student married has legal dependents other than a spouse 24 years old a student with documented special circumstances for independence SPECIAL CIRCUMSTANCES Although the process of determining need for financial aid is generally the same for all students, th”
  - sentence: need_based_special_circumstances ⟵ “If you feel you have special circumstances, contact the Office of Financial Aid. 2025-2026 Dependent Verification Worksheet V1 2025-2026 Independent Verification Worksheet V1 2025-2026 Dependent Verification Worksheet V4/V5 2025-2026 Independent Verification Worksheet V4/V5 News Employment Alumni Financial Services Communications IT Help Desk Institutional Research and Effectiveness Consumer Infor”
### `2241ef28b2caf584` Lane College — costs 2025-26 [same] (labeled_in_source)
- source: https://www.lanecollege.edu/financial-aid-tuition/college-costs (sha256 ec5554585949)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 9}
  - column:Tuition (12-16 hours): 10198.0 ⟵ “Tuition (12-16 hours) | $5,099.00 | $5,099.00 | $10,198.00”
  - column:Text Book Fee: 770.0 ⟵ “Text Book Fee | $385.00 | $385.00 | $770.00”
  - column:Matriculation Fee: 1000.0 ⟵ “Matriculation Fee | $500.00 | $ 500.00 | $ 1,000.00”
  - column:Technology Fee: 700.0 ⟵ “Technology Fee | $350.00 | $350.00 | $700.00”
  - column:Student Activity Fee: 250.0 ⟵ “Student Activity Fee | $125.00 | $125.00 | $250.00”
  - column:Housing (9-Month): 5240.0 ⟵ “Housing (9-Month) | $2,620.00 | $2,620.00 | $5,240.00”
  - column:Meal Plan (9-Month): 3140.0 ⟵ “Meal Plan (9-Month) | $1,570.00 | $1,570.00 | $3,140.00”
  - column:Health Service Fee: 150.0 ⟵ “Health Service Fee | $75.00 | $75.00 | $150.00”
  - column:Total: 21448.0 ⟵ “Total | $10,724.00 | $10,724.00 | $21,448.00”
### `ea116ce9577c80c3` Lee University — admissions_metrics 2024-25 [same] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/2024-2025-CDS.pdf (sha256 0e1d4e31cec3)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 2388 ⟵ “Total applied                                                                          2,388”
  - admits: 1684 ⟵ “Total admitted                                                                         1,684”
  - enrolled: 589 ⟵ “Total enrolled                                                                          589”
  - sat_composite_25..75: [1020, 1140, 1210] ⟵ “SAT Composite                                                        1020                               1140                               1210”
  - sat_reading_25..75: [540, 580, 630] ⟵ “SAT Evidence-Based Reading and Writing                               540                                580                                630”
  - sat_math_25..75: [500, 550, 600] ⟵ “SAT Math                                                             500                                550                                600”
  - act_25..75: [20, 23, 27] ⟵ “ACT Composite                                                         20                                 23                                 27”
### `095be3206bd37edb` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/Scholarships-TELS-SAP-Standards.pdf (sha256 8b44ac676e1d)
- issues: stale_year_label:2020-21, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Tennessee HOPE Scholarship Retention Standards & Appeal Process Students must maintain Satisfactory Academic Progress AND Continuous Enrollment as outlined below to retain eligibility for Tennessee HOPE Scholarship.”
### `27d47eada466f44f` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/financial-aid/scholarships/ (sha256 64d42dbec83e)
- issues: stale_year_label:2020-21, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If there are extreme special circumstances then you need to fill out a Special Conditions form and schedule an appointment to meet with the Director of Financial Aid.”
### `3d9716378018287d` Lee University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.leeuniversity.edu/financial-aid/cost/ (sha256 45c6bc3a23f5)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If there are extreme special circumstances then you need to fill out a Special Conditions form and schedule an appointment to meet with the Director of Financial Aid.”
### `452a0a36fc3bff15` Lee University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.leeuniversity.edu/financial-aid/cost/ (sha256 45c6bc3a23f5)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Information on enrollment, continued eligibility, and student appeal requirements for the HOPE scholarship can be found here. × Tennessee Minority Teaching Fellows Program This award is for entering freshmen with a 2.5 high school GPA on a 4.0 scale.”
### `a3b1447cd7a5be4d` Lee University — appeals 2020-21 [new] (labeled_in_source)
- source: https://www.leeuniversity.edu/wp-content/uploads/Scholarships-TELS-SAP-Standards.pdf (sha256 8b44ac676e1d)
- issues: stale_year_label:2020-21, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “GPA Review & Continuous Enrollment Appeal Process GPA Standard Review Request As per Tennessee Code Annotated Rule 1640-01-19-.28 the Institutional Review Panel (IRP) does not have the authority to decide on an appeal due to a low HOPE GPA.”
  - sentence: scholarship_retention_appeal ⟵ “Continuous Enrollment Appeal Students who are not eligible for TN HOPE due to not meeting the Continuous enrollment standard may submit an appeal to the Financial Aid Office – Institutional Review Panel (IRP).”
  - sentence: scholarship_retention_appeal ⟵ “For more details, visit TSAC’s website at: https://www.tn.gov/content/tn/collegepays/money-for-college/tn-education-lottery-programs/tels-program-and-tn-promis- scholarship-appeals-and -exeptions.html T:\Document Printing\2020-2021 (Updated 10/28/2020)”
### `3884b811b4c19c61` Lincoln Memorial University — appeals 2026-27 [new] (source_unlabeled)
- source: https://undergraduatecatalog.lmunet.edu/financial-aid-satisfactory-academic-progress (sha256 1e1109d06349)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “SAP Appeals Students who are on Financial Aid Suspension may appeal this decision by contacting Student Financial Services.”
### `16cc602ff1faf721` Lipscomb University — appeals 2026-27 [new] (source_unlabeled)
- source: https://lipscomb.edu/admissions/cost-financial-aid/resources/satisfactory-academic-progress (sha256 3796312e350e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “All appeals must include documentation of any unusual circumstance that contributed to the probation.”
### `3af4d31ac921d7ac` Lipscomb University — appeals 2026-27 [new] (source_unlabeled)
- source: https://lipscomb.edu/admissions/cost-financial-aid/resources/satisfactory-academic-progress (sha256 3796312e350e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “All probations may be appealed in writing by completing a Satisfactory Academic Progress Appeal Form.”
### `ea03002ca7af64a4` Lipscomb University — costs 2025-26 [same] (labeled_in_source)
- source: https://lipscomb.edu/admission/tuition-and-financial-aid/cost-attendance (sha256 81ea03f54e4d)
- issues: stale_year_label:2025-26
- checks: {"columns": 3, "components_reconcile": true, "rows": 8}
  - on_campus:Tuition & Fees: 42596 ⟵ “Tuition & Fees | $42,596 | $42,596 | $42,596”
  - on_campus:Housing: 11044 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - on_campus:Food: 6700 ⟵ “Food | $6,700** | $3,004 | $2,000”
  - on_campus:Books & Supplies: 1750 ⟵ “Books & Supplies | $1,750 | $1,750 | $1,750”
  - on_campus:Personal Expenses: 2460 ⟵ “Personal Expenses | $2,460 | $2,460 | $2,460”
  - on_campus:Transportation: 2250 ⟵ “Transportation | $2,250 | $2,250 | $2,250”
  - on_campus:Loan Fee (If Accepting): 48 ⟵ “Loan Fee (If Accepting) | 48 | 48 | 48”
  - on_campus:Total: 66848 ⟵ “Total | $66,848 | $65,348 | $55,604”
  - off_campus_not_with_family:Tuition & Fees: 42596 ⟵ “Tuition & Fees | $42,596 | $42,596 | $42,596”
  - off_campus_not_with_family:Housing: 13240 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - off_campus_not_with_family:Food: 3004 ⟵ “Food | $6,700** | $3,004 | $2,000”
  - off_campus_not_with_family:Books & Supplies: 1750 ⟵ “Books & Supplies | $1,750 | $1,750 | $1,750”
  - off_campus_not_with_family:Personal Expenses: 2460 ⟵ “Personal Expenses | $2,460 | $2,460 | $2,460”
  - off_campus_not_with_family:Transportation: 2250 ⟵ “Transportation | $2,250 | $2,250 | $2,250”
  - off_campus_not_with_family:Loan Fee (If Accepting): 48 ⟵ “Loan Fee (If Accepting) | 48 | 48 | 48”
  - off_campus_not_with_family:Total: 65348 ⟵ “Total | $66,848 | $65,348 | $55,604”
  - with_parents_or_family:Tuition & Fees: 42596 ⟵ “Tuition & Fees | $42,596 | $42,596 | $42,596”
  - with_parents_or_family:Housing: 4500 ⟵ “Housing | $11,044** | $13,240 | $4,500”
  - with_parents_or_family:Food: 2000 ⟵ “Food | $6,700** | $3,004 | $2,000”
  - with_parents_or_family:Books & Supplies: 1750 ⟵ “Books & Supplies | $1,750 | $1,750 | $1,750”
  - with_parents_or_family:Personal Expenses: 2460 ⟵ “Personal Expenses | $2,460 | $2,460 | $2,460”
  - with_parents_or_family:Transportation: 2250 ⟵ “Transportation | $2,250 | $2,250 | $2,250”
  - with_parents_or_family:Loan Fee (If Accepting): 48 ⟵ “Loan Fee (If Accepting) | 48 | 48 | 48”
  - with_parents_or_family:Total: 55604 ⟵ “Total | $66,848 | $65,348 | $55,604”
### `c6c8e67d45a1394a` Lipscomb University — credit_policies 2026-27 [new] (source_unlabeled)
- source: https://lipscomb.edu/admission/transfer-admission/transferring-credit (sha256 a7ffd3af7b5c)
- issues: rows_without_score
- checks: {"distinct_exams": 24, "equivalencies": 38, "rows_without_score": 4}
  - equivalencies[CLEP-AMERICAN-LITERATURE|50]:  ⟵ “American Literature | Survey of American Literature | 50 | Literary Inquiry”
  - equivalencies[CLEP-ENGLISH-LITERATURE|50]:  ⟵ “English Literature | Survey of English Literature | 50 | Literary Inquiry”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|55]:  ⟵ “College Composition | EN 1113 Freshman Comp. & Reading I or 3 hours elective credit | 55 | Elective”
  - equivalencies[CLEP-COLLEGE-COMPOSITION|None]:  ⟵ “College Composition | Foreign Languages | ”
  - equivalencies[CLEP-FRENCH-LANGUAGE|48]:  ⟵ “College French (Level I) | FR 1114 | 48 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-FRENCH-LANGUAGE|52]:  ⟵ “College French (Level I) | FR 1114 and 1124 | 52 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-FRENCH-LANGUAGE|56]:  ⟵ “College French (Level II) | FR 1114, 1124 and 2114 | 56 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-FRENCH-LANGUAGE|62]:  ⟵ “College French (Level II) | FR 1114, 1124, 2114, and 2124 | 62 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-GERMAN-LANGUAGE|48]:  ⟵ “College German (Level I) | GE 1114 | 48 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-GERMAN-LANGUAGE|52]:  ⟵ “College German (Level I) | GE 1114 and 1124 | 52 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-GERMAN-LANGUAGE|56]:  ⟵ “College German (Level II) | GE 1114, 1123, and 2114 | 56 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-GERMAN-LANGUAGE|63]:  ⟵ “College German (Level II) | GE 1114, 1124, 2114 and 2124 | 63 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|48]:  ⟵ “College Spanish (Level I) | SN 1114 | 48 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|54]:  ⟵ “College Spanish (Level I) | SN 1114 and 1124 | 54 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|60]:  ⟵ “College Spanish (Level II) | SN 1114, 1124, and 2114 | 60 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|66]:  ⟵ “College Spanish (Level II) | SN 1114, 1124, 2114, and 2124 | 66 | B.A. Foreign Language Hours”
  - equivalencies[CLEP-SPANISH-LANGUAGE|None]:  ⟵ “College Spanish (Level II) | History and Social Sciences | ”
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50]:  ⟵ “American Government | PO 1023 Introduction to American Government | 50 | Great Ideas in Politics”
  - equivalencies[CLEP-HUMAN-GROWTH-DEVELOPMENT|50]:  ⟵ “Human Growth and Develop. | PS 2423 Life Span Development | 50 | Social Inquiry”
  - equivalencies[CLEP-INTRODUCTION-TO-EDUCATIONAL-PSYCHOLOGY|50]:  ⟵ “Intro to Educational Psychology | PS 3243 Human Development and Learning | 50 | Social Inquiry”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50]:  ⟵ “Principles of Macroeconomics | EC 2403 Principles of Macroeconomics | 50 | Social Inquiry”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50]:  ⟵ “Principles of Microeconomics | EC 2413 Principles of Microeconomics | 50 | Social Inquiry”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50]:  ⟵ “Introductory Psychology | PS 1113 Introduction to Psychology | 50 | Solical Inquiry”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50]:  ⟵ “Introductory Sociology | SO 1123 Introduction to Sociology | 50 | Social Inquiry”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | HI 1113 Foundations of Western Civilization to 1600 | 50 | Great Ideas in History”
  - … 13 more rows
### `02beb04a2234898f` Maryville College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/professional-judgment/ (sha256 0d73e17aef5c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “The Financial Aid Office will accept, and review all submitted Professional Judgment (PJ) requests from students and/or families.”
### `1a45cd68e524c9a5` Maryville College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/professional-judgment/ (sha256 0d73e17aef5c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “This is more commonly referred to as a dependency override.”
  - sentence: dependency_override ⟵ “Self-supporting students without a documented extenuating family circumstance do not qualify for a dependency override.”
### `eb0bdca43de91fcb` Maryville College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.maryvillecollege.edu/admissions/finaid/professional-judgment/ (sha256 0d73e17aef5c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “The outline below indicates circumstances where a PJ may be warranted: Special Circumstances: extenuating circumstances (i.e., job loss) leading to changes in your family’s financial situation that are not reflected accurately or occurred after the submission of your current year FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances: a student’s dependency status is based on a unique situation (e.g., parental abandonment, abuse, or incarceration) where there is no parental involvement.”
### `3573a6ddb2ed9c8f` Middle Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mtsu.edu/financial-aid/appeals/ (sha256 1d876f8167c2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals NOTE: Students should also be aware of the difference between a financial aid suspension based on the Financial Aid Satisfactory Academic Progress Policy and an academic suspension which is based solely on grades and GPA (refer to the Academic Standing policies in the Undergraduate & Graduate Catalogs).”
  - sentence: sap_appeal ⟵ “MTSU Financial Aid Satisfactory Academic Progress Appeal Form located on the forms page.”
  - sentence: sap_appeal ⟵ “An academic appeal, if approved, will allow you to enroll in classes for the affected semester; a scholarship or SAP appeal, if approved, will allow you to receive your related aid for the affected semester.”
### `652e18783e2fb8b5` Middle Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.mtsu.edu/financial-aid/appeals/ (sha256 1d876f8167c2)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: scholarship_retention_appeal ⟵ “Institutional Scholarship Appeal Form found on our forms page.”
  - sentence: scholarship_retention_appeal ⟵ “Once you have gotten your GPA back up to the required level, then you will need to submit a new Institutional Scholarship Appeal Form, and check the box that indicates you are now meeting the GPA requirement.”
  - sentence: scholarship_retention_appeal ⟵ “If this is applicable, please submit the Institutional Scholarship Appeal Form along with a written statement explaining why unable to enroll full-time in CPoS eligible classes.”
  - sentence: scholarship_retention_appeal ⟵ “Tennessee Education Lottery Scholarship (TELS) Appeal Process The Tennessee Education Lottery Scholarship (TELS) is awarded based on policies set forth by the Tennessee Student Assistance Corporation (TSAC).”
  - sentence: scholarship_retention_appeal ⟵ “TSAC’s TELS policy allows an appeal process for students who fail to meet enrollment requirements due to extenuating medical or personal circumstances.”
  - sentence: scholarship_retention_appeal ⟵ “Appealing the cancellation of the TELS/Lottery Scholarship If you lost TELS eligibility while attending another institution or 1 of the items listed under ‘Who cannot submit an appeal to the MTSU TELS Institutional Review Panel (IRP)’ heading applies to yourself, then you must appeal directly to the Tennessee Student Assistance Corporation (TSAC).”
### `0ac9e710a7a1df19` Middle Tennessee State University — credit_policies 2010-11 [new] (labeled_in_source)
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 00c4b48c49f3)
- issues: stale_year_label:2010-11
- checks: {"distinct_exams": 32, "equivalencies": 32, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3 or above]:  ⟵ “African American Studies | 3 or above | HIST 2040, HIST 2050 | 6”
  - equivalencies[AP-ART-HISTORY|3 or above]:  ⟵ “Art History | 3 or above | ART 1030 | 3”
  - equivalencies[AP-BIOLOGY|3 or above]:  ⟵ “Biology | 3 or above | BIOL1030/ BIOL 1031 (Science major may receive credit for BIOL 1110/BIOL 1111, BIOL 1120/BIOL 1121 upon recommendation of chair, Department of Biology.) | 4”
  - equivalencies[AP-BUSINESS-WITH-PERSONAL-FINANCE|3 or above]:  ⟵ “Business with Personal Finance | 3 or above | FCSE 1400 | 3”
  - equivalencies[AP-CALCULUS-AB|3 or above]:  ⟵ “Calculus AB | 3 or above | MATH 1910 | 4”
  - equivalencies[AP-CALCULUS-BC|3 or above]:  ⟵ “Calculus BC | 3 or above | Math 1920 | 4”
  - equivalencies[AP-CHEMISTRY|3 or 45]:  ⟵ “Chemistry | 3 or 45 | CHEM 1110/ CHEM 1111 OR CHEM 1010/ CHEM 1011CHEM 1110/ CHEM 1111, CHEM 1120/ CHEM 1121 | 4 8”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3 or above]:  ⟵ “Comparative Government and Politics | 3 or above | PS 1010 | 3”
  - equivalencies[AP-COMPUTER-SCIENCE-A|3 or above]:  ⟵ “Computer Science A | 3 or above | CSCI 1170 | 4”
  - equivalencies[AP-CYBERSECURITY|3 or above]:  ⟵ “Cybersecurity | 3 or above | CYBM 1300 | 3”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 or above]:  ⟵ “English Language and Composition | 3 or above | ENGL 1010 | 3”
  - equivalencies[AP-ENGLISH-LITERATURE-COMPOSITION|3 or above]:  ⟵ “English Literature and Composition | 3 or above | ENGL1010 | 3”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3 or above]:  ⟵ “Environmental Science | 3 or above | ENVS 2810/ENVS 2811 | 4”
  - equivalencies[AP-EUROPEAN-HISTORY|3 or above]:  ⟵ “European History | 3 or above | HIST 1020 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3 or above]:  ⟵ “Human Geography | 3 or above | GS 2010 | 3”
  - equivalencies[AP-MACROECONOMICS|3 or above]:  ⟵ “Macroeconomics | 3 or above | ECON 2410 | 3”
  - equivalencies[AP-MICROECONOMICS|3 or above]:  ⟵ “Microeconomics | 3 or above | ECON 2420 | 3”
  - equivalencies[AP-MUSIC-THEORY|3 or above]:  ⟵ “Music Theory | 3 or above | MUTH 1000 | 3”
  - equivalencies[AP-PHYSICS-1|4 or above]:  ⟵ “Physics 1 | 4 or above | PHYS 2010/2011* | 4”
  - equivalencies[AP-PHYSICS-2|4 or above]:  ⟵ “Physics 2 | 4 or above | PHYS 2020/2021* | 4”
  - equivalencies[AP-PHYSICS-C-ELECTRICITY-MAGNETISM|4 or above]:  ⟵ “Physics C: Electricity & Magnetism | 4 or above | PHYS 2120/2121* | 4”
  - equivalencies[AP-PHYSICS-C-MECHANICS|4 or above]:  ⟵ “Physics C: Mechanics | 4 or above | PHYS 2110/2111* | 4”
  - equivalencies[AP-PRECALCULUS|3 or above]:  ⟵ “Precalculus | 3 or above | MATH 1730 | 4”
  - equivalencies[AP-PSYCHOLOGY|3 or above]:  ⟵ “Psychology | 3 or above | PSY 1410 | 3”
  - equivalencies[AP-SEMINAR|3 or above]:  ⟵ “Seminar | 3 or above | CLA 2000 | 3”
  - … 7 more rows
### `0c7143377e8fa304` Middle Tennessee State University — credit_policies 2010-11 [new] (labeled_in_source)
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 00c4b48c49f3)
- issues: stale_year_label:2010-11
- checks: {"distinct_exams": 19, "equivalencies": 19, "rows_without_score": 0}
  - equivalencies[CLEP-AMERICAN-GOVERNMENT|50 or greater]:  ⟵ “American Government | 50 or greater | PS 1005 | 3”
  - equivalencies[CLEP-BIOLOGY|50 or greater]:  ⟵ “Biology | 50 or greater | BIOL 1030/1031 | 4”
  - equivalencies[CLEP-INTRODUCTORY-BUSINESS-LAW|50 or greater]:  ⟵ “Business Law, Introductory | 50 or greater | BLAW 3430 | 3”
  - equivalencies[CLEP-CALCULUS|50 or greater]:  ⟵ “Calculus | 50 or greater | MATH 1910 | 4”
  - equivalencies[CLEP-CHEMISTRY|50 or greater]:  ⟵ “Chemistry | 50 or greater | CHEM 1110/CHEM 1111, CHEM 1120/CHEM 1121 | 8”
  - equivalencies[CLEP-COLLEGE-ALGEBRA|50 or greater]:  ⟵ “College Algebra | 50 or greater | MATH 1710 | 3”
  - equivalencies[CLEP-COLLEGE-MATHEMATICS|50 or greater]:  ⟵ “College Mathematics | 50 or greater | MATH 1010 | 3”
  - equivalencies[CLEP-FINANCIAL-ACCOUNTING|50 or greater]:  ⟵ “Financial Accounting | 50 or greater | ACTG 2110 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-I|50 or greater]:  ⟵ “History of the United States I: Early Colonization to 1877 | 50 or greater | HIST 2010 | 3”
  - equivalencies[CLEP-HISTORY-OF-THE-UNITED-STATES-II|50 or greater]:  ⟵ “History of the United States II: 1865 to Present | 50 or greater | HIST 2020 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MACROECONOMICS|50 or greater]:  ⟵ “Macroeconomics, Principles of | 50 or greater | ECON 2410 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MANAGEMENT|50 or greater]:  ⟵ “Management, Principles of | 50 or greater | MGMT 3610 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MARKETING|50 or greater]:  ⟵ “Marketing, Principles of | 50 or greater | MKT 3820 | 3”
  - equivalencies[CLEP-PRINCIPLES-OF-MICROECONOMICS|50 or greater]:  ⟵ “Microeconomics, Principles of | 50 or greater | ECON 2420 | 3”
  - equivalencies[CLEP-PRECALCULUS|50 or greater]:  ⟵ “Precalculus | 50 or greater | MATH 1730 | 4”
  - equivalencies[CLEP-INTRODUCTORY-PSYCHOLOGY|50 or greater]:  ⟵ “Psychology, Introductory | 50 or greater | PSY 1410 | 3”
  - equivalencies[CLEP-INTRODUCTORY-SOCIOLOGY|50 or greater]:  ⟵ “Sociology, Introductory | 50 or greater | SOC 1010 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-I|50 or greater]:  ⟵ “Western Civilization I: Ancient Near East to 1648 | 50 or greater | HIST 1010 | 3”
  - equivalencies[CLEP-WESTERN-CIVILIZATION-II|50 or greater]:  ⟵ “Western Civilization II: 1648 to Present | 50 or greater | HIST 1020 | 3”
### `62175305b270743f` Middle Tennessee State University — credit_policies 2010-11 [new] (labeled_in_source)
- source: https://www.mtsu.edu/how-to-apply/credit-by-examination/ (sha256 00c4b48c49f3)
- issues: stale_year_label:2010-11
- checks: {"distinct_exams": 15, "equivalencies": 20, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|5 or higher]:  ⟵ “Biology (higher level) | 5 or higher | BIOL 1110/ BIOL 1111 and BIOL 1120/BIOL 1121 | 8”
  - equivalencies[IB-BUSINESS-MANAGEMENT|5 or higher (SL)4 or higher (HL)]:  ⟵ “Business and Management (standard or higher level) | 5 or higher (SL)4 or higher (HL) | BCED 1400 | 3”
  - equivalencies[IB-CHEMISTRY|5 or higher]:  ⟵ “Chemistry (higher level) | 5 or higher | CHEM 1110/1111 and 1120/1121 | 8”
  - equivalencies[IB-CHEMISTRY|5 or higher]:  ⟵ “Chemistry (standard level) | 5 or higher | CHEM 1110/1111 | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|6 or higher (SL)5 or higher (HL)]:  ⟵ “Computer Science (standard or higher level) | 6 or higher (SL)5 or higher (HL) | CSCI 1170 | 4”
  - equivalencies[IB-ECONOMICS|5 or higher (SL)5 or higher (HL)]:  ⟵ “Economics (standard or higher level) | 5 or higher (SL)5 or higher (HL) | ECON 2410ECON 2410 and 2420 | 36”
  - equivalencies[IB-ENVIRONMENTAL-SYSTEMS-SOCIETIES|4 or higher]:  ⟵ “Environmental Systems or Societies (standard or higher level) | 4 or higher | ENVS 2810/ENVS 2811 | 4”
  - equivalencies[IB-GEOGRAPHY|5 or higher (SL)4 or higher (HL)]:  ⟵ “Geography (standard or higher level) | 5 or higher (SL)4 or higher (HL) | GEOG 2000 | 3”
  - equivalencies[IB-HISTORY|5 or higher]:  ⟵ “History (higher level) | 5 or higher | HIST 1120 and depending on higher level option (Paper #3)Europe: HIST 1020; Americas: either HIST 2010 or 2020 to be determined at orientation/advising; Africa and the Middle East or Asia and Ocean – 3 hours lower-division history credit | 6”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4 or higher]:  ⟵ “Mathematics: Analysis & Approaches (standard level) | 4 or higher | MATH 1730 | 4”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|4 or higher]:  ⟵ “Mathematics: Analysis & Approaches (higher level) | 4 or higher | MATH 1910 | 4”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|4 or higher]:  ⟵ “Mathematics: Applications & Interpretation (standard or higher level) | 4 or higher | MATH 1530 (student may request MATH 1730 instead) | 3 (4)”
  - equivalencies[IB-PHILOSOPHY|5 or higher]:  ⟵ “Philosophy (standard level) | 5 or higher | 3 hours lower-division philosophy credit | 3”
  - equivalencies[IB-PHILOSOPHY|5 or higher]:  ⟵ “Philosophy (higher level) | 5 or higher | PHIL 1030 | 3”
  - equivalencies[IB-PHYSICS|5 or higher]:  ⟵ “Physics (standard or higher level) | 5 or higher | PHYS 2010/PHYS 2011 | 4”
  - equivalencies[IB-PHYSICS|6 or higher]:  ⟵ “Physics (standard or higher level) | 6 or higher | PHYS 2010/PHYS 2011 and PHYS 2020/PHYS 2021 | 8”
  - equivalencies[IB-PSYCHOLOGY|4 or higher]:  ⟵ “Psychology (higher level) | 4 or higher | 3 hours lower-division psychology credit | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4 or higher]:  ⟵ “Social and Cultural Anthropology (standard level) | 4 or higher | ANTH 2010 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|4 or higher]:  ⟵ “Social and Cultural Anthropology (higher level) | 4 or higher | ANTH 2010 plus 3 hours ANTH lower division elective | 6”
  - equivalencies[IB-THEATRE|5 or higher]:  ⟵ “Theatre (standard or higher level) | 5 or higher | THEA 1030 | 3”
### `b38ffab277b4c250` Nashville State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.nscc.edu/documents/financial-aid/sap-infographic.pdf (sha256 3a3adf26aca8)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Click on Financial Aid on Student Requirements HOW DO I GET A SAP WHAT DO I NEED TO APPEAL PACKET AND INCLUDE IN MY APPEAL?”
  - sentence: sap_appeal ⟵ “You cannot file an *Make sure to explain how circumstances have SAP Appeal until all of your final changed and/or what steps you have taken to grades have been posted. alleviate any obstacles.”
### `aad2355545ea0e93` Nashville State Community College — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://nscc.edu/current-students/transfer-options.php (sha256 22ac77e86506)
- issues: conflicting_values:residency_requirement_credits
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “South College Transfer Credit Undergraduate – Credit for transfer work may be given if it was taken at an accredited collegiate institution, if it is equivalent to courses offered at South College, and if it carries a grade of C or better.”
### `306c06723f2e00bd` Northeast State Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-forms.html (sha256 8dc08c660399)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Northeast State Online General Scholarship Application HOPE, TN Promise, & TN Reconnect Appeals This form must be completed prior to the following requests.”
### `368b526a174eab14` Northeast State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.northeaststate.edu/financial-aid-tuition/policies/financial-aid-standards.html (sha256 f3983b2de692)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “Turn in the degree audit at the same time as the SAP Appeal form.”
  - sentence: sap_appeal ⟵ “Appeals will be considered for the following reasons: Serious injury or illness of the student Death, serious illness, or injury of immediate family member (mother, father, sibling, spouse, child) Family trauma which occurred during the semester in question Change in work schedule or responsibilities Change in household or marital status Other extenuating circumstances (must be documented) Process”
  - sentence: sap_appeal ⟵ “FINANCIAL AID PLAN and DENIAL Plan – Students will be placed on the Financial Aid Plan if their SAP appeal is approved.”
  - sentence: sap_appeal ⟵ “Denial – A student will be placed on Financial Aid Denial if their SAP appeal is denied by the SAP Committee.”
### `6fab2ec4c5df1d7d` Northeast State Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-appeals.html (sha256 fd007050b235)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress View our Satisfactory Academic Progress page for information on SAP appeals and standards.”
### `7e66a9b7991d5a82` Northeast State Community College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-forms.html (sha256 8dc08c660399)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal - Satisfactory Academic Progress This form must be completed when the Financial Aid Office has notified a student that he/she is currently or was previously placed on financial aid removal.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress (SAP) Standards Policy Satisfactory Academic Progress (SAP) Appeal Form Request for Degree Works Audit for SAP Read the Satisfactory Academic Progress Standards Policy.”
  - sentence: sap_appeal ⟵ “If the appeal is approved, a student must sign the Satisfactory Academic Progress 'Plan' and must adhere to the agreed upon terms of the 'Plan'.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeals Committee will review and rule on a complete submitted appeal.”
  - sentence: sap_appeal ⟵ “The Satisfactory Academic Progress Appeals Committee may request additional documentation for an appeal and the documents must be submitted before the committee can rule on an appeal.”
  - sentence: sap_appeal ⟵ “HOPE One Time Repeat/Regain Appeal HOPE Enrollment Status Appeal TN Promise Enrollment Status Appeal TN Reconnect Enrollment Status Appeal Financial Aid Plan for Satisfactory Academic Progress Financial Aid Plan for Satisfactory Academic Progress Change of Income Appeals It is the policy of the Northeast State Financial Aid Office to consider change of income requests related to unexpected events ”
### `81ef6acdaa7376e4` Northeast State Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-appeals.html (sha256 fd007050b235)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Appeals are approved or denied based upon the professional judgment of financial aid staff and various appeal committees.”
### `f11b333317c17ab3` Northeast State Community College — appeals 2024-25 [new] (labeled_in_source)
- source: https://www.northeaststate.edu/financial-aid-tuition/financial-aid-appeals.html (sha256 fd007050b235)
- issues: stale_year_label:2024-25, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Unusual Circumstances Students classified as Dependent on the FAFSA who are unable to provide parent information may request a review of their dependency status based on adverse family circumstances.”
  - sentence: need_based_special_circumstances ⟵ “Students who wish to have their dependency status reviewed should contact the Financial Aid Office to discuss an Unusual Circumstance Appeal.”
### `a0460562d9a4d741` Rhodes College — admissions_metrics 2024-25 [same] (labeled_in_source)
- source: https://www.rhodes.edu/sites/default/files/2026-02/CDS_2024-2025%20_Rhodes_College_.pdf (sha256 1e6d625b330b)
- issues: stale_year_label:2024-25
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75"]}
  - applications: 6365 ⟵ “Total first-time, first-year (degree-seeking) who applied          1103       2872            2390           0     6365”
  - admits: 3205 ⟵ “Total first-time, first-year (degree-seeking) who were admitted     708         2160          337            0     3205”
  - enrolled: 388 ⟵ “Total first-time, first-year (degree-seeking) enrolled              126         216            46            0      388”
  - sat_composite_25..75: [1352, 1420, 1478] ⟵ “SAT Composite                     1352                      1420                       1478”
  - sat_math_25..75: [670, 720, 740] ⟵ “SAT Math                           670                       720                       740”
  - act_25..75: [28, 31, 32] ⟵ “ACT Composite                      28                        31                         32”
### `06c3cbcd5ebc5262` Rhodes College — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/rhodes-institutional-aid (sha256 7fc7a0f62d78)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Exceptions to this are within the purview of the Financial Aid Office in response to extreme increases in demonstrated financial need documented through the completion of the Special Circumstance Request and other supporting documents that may be required.”
### `49bfe9b1b73b2dd0` Rhodes College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/faq (sha256 030d7deb1e50)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Our committee will review each situation on a case-by-case basis to determine if a dependency override can be granted.”
### `52f7765789c15ac7` Rhodes College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.rhodes.edu/admission-aid/cost-affordability/faq (sha256 030d7deb1e50)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: need_based_special_circumstances ⟵ “Yes, if your family has experienced a change in financial circumstances (such as loss of employment, separation or divorce, or death of a parent) that is not adequately reflected on your FAFSA application, you may complete our Change of Financial Circumstances Form.”
  - sentence: need_based_special_circumstances ⟵ “In an effort to determine the need of our families and to best distribute any available awards we are asking families to complete the attached Special Circumstance Form.”
  - sentence: need_based_special_circumstances ⟵ “What can I do if I have unusual circumstances that prevent me from reporting parent information on my FAFSA?”
  - sentence: need_based_special_circumstances ⟵ “Students with unusual circumstances (such as parental abandonment, abuse, or incarceration) are encouraged to reach out to the Office of Student Financial Aid to explain their situation and provide supporting documentation.”
### `417575f816d101f5` Roane State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.roanestate.edu/?8056-Dependency-Status-Appeal (sha256 92597758998f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: dependency_override ⟵ “Requesting a Dependency Status Appeal To request independent status, you must complete the Dependency Status Appeal form via RaiderNet.”
  - sentence: dependency_override ⟵ “After you have submitted the form, please check 'Your Alerts' to see what documents are needed to complete your Dependency Status Appeal.”
  - sentence: dependency_override ⟵ “Renewing a Dependency Status Appeal To renew a previous Dependency Status Appeal, complete the Dependency Status Appeal form in your RaiderNet account, and submit the documents requested.”
  - sentence: dependency_override ⟵ “Students seeking to renew a Dependency Status Appeal, must provide a letter explaining their current living situation and describing any changes since the previous year.”
### `5321e45e86cc1ad6` Roane State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.roanestate.edu/?6662-Satisfactory-Academic-Progress-SAP (sha256 a5855849a415)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 4}
  - sentence: sap_appeal ⟵ “If it is determined that it is mathematically impossible for a student to regain good standing (2.0 GPA and passing 67% of all attempted hours that apply to your program of study) upon graduation, the SAP appeal will be denied.”
  - sentence: sap_appeal ⟵ “Appeals If there were circumstances beyond a student's control OUTSIDE the classroom that caused failure to meet SAP, they may appeal.”
  - sentence: sap_appeal ⟵ “Examples of circumstances beyond a student's control are: Loss or change of job Serious illness of self or an immediate family member Death of an immediate family member Military Car problems Family Issues (Divorce, Separation, Childcare, etc) To appeal, the student will complete the SAP Appeal form in RaiderNet, submit documentation that supports the outstanding circumstances that were experience”
  - sentence: sap_appeal ⟵ “Please be advised that if a student has been approved for a Satisfactory Academic Progress Appeal (SAP) and does a total withdrawal, officially or unofficially, the appeal is voided and the student must REAPPEAL.”
### `a07d315a963b0d97` Roane State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.roanestate.edu/?8056-Dependency-Status-Appeal (sha256 92597758998f)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “However, if there are severe family problems, which constitute special circumstances, you may appeal this federal law.”
### `615047778b3711c6` Southern Adventist University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/grants-and-scholarships.html (sha256 7b46f836a39a)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Dropping below full-time status or withdrawing after the census date can result in immediate loss of the scholarship, repayment of funds, and loss of future eligibility, unless an appeal for exceptional circumstances is approved.”
### `105982dcd82e9d21` Southern Adventist University — costs 2026-27 [new] (source_unlabeled)
- source: https://www.southern.edu/undergrad/finances/tuition.html (sha256 cc56cec75708)
- issues: ambiguous_year_labels, arrangement_unlabeled
- checks: {"columns": 2, "components_reconcile": true, "rows": 5}
  - on_campus:Undergraduate Tuition (12-16 hours): 28900 ⟵ “Undergraduate Tuition (12-16 hours) | $28,900 | $28,900”
  - on_campus:General Fee: 1500 ⟵ “General Fee | $1,500 | $1,500”
  - on_campus:Residence Hall Rent: 6000 ⟵ “Residence Hall Rent | $6,000 | --”
  - on_campus:Estimated Food Allowance*: 3900 ⟵ “Estimated Food Allowance* | $3,900 | --”
  - on_campus:Total: 40300 ⟵ “Total | $40,300 | $30,400”
  - column:Undergraduate Tuition (12-16 hours): 28900 ⟵ “Undergraduate Tuition (12-16 hours) | $28,900 | $28,900”
  - column:General Fee: 1500 ⟵ “General Fee | $1,500 | $1,500”
  - column:Total: 30400 ⟵ “Total | $40,300 | $30,400”
### `0ae159e632cb6aa1` Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tnstate.edu/admissions/financial-aid/admissions-admissions-satprog/ (sha256 fe5932fdb514)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Such circumstances might include the death of a relative, an injury to or illness of the student, or other special circumstances.”
### `674ddd8131b11236` Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tnstate.edu/admissions/financial-aid/financial-aid-forms/ (sha256 078ccb07fe15)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: budget_increase ⟵ “NOTE: requesting a budget increase DOES NOT mean that there are additional funds available.”
### `9d88d40b94c2304a` Tennessee State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tnstate.edu/admissions/financial-aid/admissions-admissions-satprog/ (sha256 fe5932fdb514)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “IMPORTANT INFORMATION RELATING TO COVID-19 and SAP: Circumstances related to an outbreak of COVID-19, including, but not limited to, the illness of a student or family member, compliance with a quarantine period, or a general disruption from such an outbreak may form the basis of a student’s SAP appeal.”
  - sentence: sap_appeal ⟵ “Refer to the TSU website regarding procedures for submitting an SAP Appeal for GPA and Completion Rate standards.”
### `0c0338217a033045` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Circumstances Not Given Consideration The Department of Education has identified conditions that, individually or in combination with one another, DO NOT QUALIFY AS UNUSUAL CIRCUMSTANCES, or do not merit a change in dependency status.”
### `26ae2942803bc68b` Tennessee Technological University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.tntech.edu/financialaid/sap.php (sha256 dfa2f7a684f5)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 21}
  - sentence: sap_appeal ⟵ “Click the links below to learn more about Satisfactory Academic Progress, Tech's SAP Policy, Financial Aid Termination, and submitting appeals!”
  - sentence: sap_appeal ⟵ “Financial Aid Termination The SAP Appeal Process SAP Policy What is SAP?”
  - sentence: sap_appeal ⟵ “Students who do not meet one of the three above requirements when evaluated at the end of any given spring semester are placed on Financial Aid Termination and must submit a SAP Appeal to potentially regain their aid for the upcoming semester.”
  - sentence: sap_appeal ⟵ “A student placed on Financial Aid Termination cannot utilize their eligible federal or state aid until they either return to 'Good Standing' by meeting the SAP requirements for future semesters or submit a SAP Appeal for review that is then approved.”
  - sentence: sap_appeal ⟵ “Students placed on FA Termination receive an email notification from the Office of Financial Aid titled "TTU Financial Aid Information" that directs them to Eagle Online to view their Financial Aid Termination status - selecting the status redirects students to the Satisfactory Academic Progress webpage to learn more about Financial Aid Termination and submit a SAP Appeal.”
  - sentence: sap_appeal ⟵ “The SAP Appeal Process Students placed on FA Termination who wish to continue using their aid can complete and submit a SAP Appeal for review.”
### `3467eba4f6bd6994` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
  - sentence: professional_judgment ⟵ “Click the links below to access the desired information. 26/27 Professional Judgment Forms 25/26 Professions Judgment Forms Appeal Examples Dependency Overrides Fall 2026, Spring 2027 and Summer 2027 Professional Judgment Form Use the link below to access the Professional Judgment form.”
  - sentence: professional_judgment ⟵ “Forms must be initiated by the student, who when prompted will add other individuals (parent or spouse) if needed. 2026-2027 Professional Judgment Form Fall 2025, Spring 2026 and Summer 2026 Professional Judgment Forms Use the links below to access the appropriate Professional Judgment form for your circumstances.”
  - sentence: professional_judgment ⟵ “The student will be prompted to add other individuals (parent or spouse) if needed. 2025-2026 Professional Judgment Appeal Form 2025-2026 Professional Judgment Appeal Form: Marital Status to Tax Return Filing Status Professional Judgment Appeal Examples Listed below are examples of circumstances for which a professional judgment may be considered at Tennessee Tech University.”
  - sentence: professional_judgment ⟵ “A Professional Judgment Appeal Form requesting a re-evaluation should be completed and submitted for review to determine documentation needed.”
  - sentence: professional_judgment ⟵ “Please note that prior to the Professional Judgment process, the FAFSA application considers prior-prior year tax return information.”
### `667beb6fe038e340` Tennessee Technological University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/professional-judgement.php (sha256 984c0110a4a7)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “Dependency Overrides Students must communicate with the Financial Aid Office for assistance with a Dependency Override request.”
### `252b6b000272741b` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Community College Transfer Scholarship | 6 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `305950f45a2282a4` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Admissions Academic Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 0 | First year”
### `42b62334683699d6` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Golden Eagle Excellence Scholarship | 8 Semesters | End of Every Spring Semester | 2.5 | 0 | First year”
### `450a687fa80966b5` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Fifth Semester at Tech ⟵ “High Flyers Scholarship | 8 Semesters | End of Fifth Semester at Tech | 3.25 | 0 | First year”
### `5a146ebaec4984d6` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Third Semester at Tech & every semester thereafter ⟵ “Golden Opportunity Grant | 8 Semesters | End of Third Semester at Tech & every semester thereafter | 3.00 | 55 | Every year”
### `5b9aef159175cb09` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Phi Theta Kappa Scholarship | 6 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `84c2dd4ded6c3534` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Second Semester at Tech & every semester thereafter ⟵ “Flight to Tech Transfer Scholarship (formerly Tech Transfer Pride) | 6 Semesters | End of Second Semester at Tech & every semester thereafter | 3.00 | 0 | N/A”
### `92627dcdb06d4a31` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “University Academic Service Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `a835944f9d946a51` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Second Semester at Tech & every semester thereafter ⟵ “Phi Theta Kappa Scholarship | 6 Semesters | End of Second Semester at Tech & every semester thereafter | 3.00 | 0 | Every year”
### `ab91c2302c269257` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Third Semester at Tech & every semester thereafter ⟵ “Presidential Scholars Scholarship | 8 Semesters | End of Third Semester at Tech & every semester thereafter | 3.00 | 0 | N/A”
### `b019b1e4bc71cd28` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Soaring Eagle Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 0 | First year”
### `b74aaaff6b276e9b` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Vice President's Residential Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `d0b3b7ad9bcc6515` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “All-Tennessee Academic Team Scholarship | 6 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `d529754ad81b8c60` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Fifth Semester at Tech ⟵ “Soaring Eagle Scholarship | 8 Semesters | End of Fifth Semester at Tech | 3.00 | 0 | First year”
### `ed3165bbe2947a00` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Fifth Semester at Tech ⟵ “Golden Eagle Excellence Scholarship | 8 Semesters | End of Fifth Semester at Tech | 2.50 | 0 | First year”
### `ed90a3d7f9548729` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Tech Alumni Legacy Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 0 | First year”
### `efc84f41bcf670a1` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Third Semester at Tech & every semester thereafter ⟵ “Upper Cumberland Valedictorian/Salutatorian Scholarship | 8 Semesters | End of Third Semester at Tech & every semester thereafter | 3.00 | 0 | Every year”
### `f7b4e26891295a7d` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “Upper Cumberland Valedictorian/Salutatorian Scholarship | 8 Semesters | End of Every Spring Semester | 3 | 0 | First year”
### `fbb2ff9d1d4b3c21` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Fifth Semester at Tech ⟵ “Tennessee State Scholastic Chess Championship Scholarship | 8 Semesters | End of Fifth Semester at Tech | 3.25 | 0 | Every year”
### `fc36730b87c75da7` Tennessee Technological University — awards 2026-27 [new] (ambiguous_year_labels)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: ambiguous_year_labels
- checks: {"thresholds": null}
  - gpa_requirement: End of Second Semester at Tech & every semester thereafter ⟵ “All-Tennessee Academic Team Scholarship | 6 Semesters | End of Second Semester at Tech & every semester thereafter | 3.00 | 0 | Every year”
### `fe3012aa22163bc0` Tennessee Technological University — awards 2017-18 [new] (labeled_in_source)
- source: https://www.tntech.edu/scholarships/tntech-scholarships-grants/admissions-renewal.php (sha256 8d59eb423885)
- issues: stale_year_label:2017-18
- checks: {"thresholds": null}
  - gpa_requirement: End of Every Spring Semester ⟵ “University Academic Scholarship - Chess Tournament | 8 Semesters | End of Every Spring Semester | 3 | 75 | First year”
### `a4678ec029f735dc` Tennessee Technological University — costs 2025-26 [same] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/cost.php (sha256 88176cba5638)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 12081 ⟵ “Tuition/Fees | $12,081 | $12,081”
  - on_campus:Housing: 7014 ⟵ “Housing | $7,014 | $8,403”
  - on_campus:Food: 6821 ⟵ “Food | $6,821 | $6,821”
  - on_campus:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - on_campus:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - on_campus:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $2,750”
  - on_campus:TOTAL: 32746 ⟵ “TOTAL | $32,746 | $34,135”
  - with_parents_or_family:Tuition/Fees: 12081 ⟵ “Tuition/Fees | $12,081 | $12,081”
  - with_parents_or_family:Housing: 8403 ⟵ “Housing | $7,014 | $8,403”
  - with_parents_or_family:Food: 6821 ⟵ “Food | $6,821 | $6,821”
  - with_parents_or_family:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - with_parents_or_family:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - with_parents_or_family:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $2,750”
  - with_parents_or_family:TOTAL: 34135 ⟵ “TOTAL | $32,746 | $34,135”
### `c4be30022b0b5609` Tennessee Technological University — costs 2025-26 [same] (labeled_in_source)
- source: https://www.tntech.edu/financialaid/cost.php (sha256 88176cba5638)
- issues: stale_year_label:2025-26
- checks: {"columns": 2, "components_reconcile": true, "rows": 7}
  - on_campus:Tuition/Fees: 16712 ⟵ “Tuition/Fees | $16,712 | $16,712”
  - on_campus:Housing: 7014 ⟵ “Housing | $7,014 | $8,403”
  - on_campus:Food: 6821 ⟵ “Food | $6,821 | $6,821”
  - on_campus:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - on_campus:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - on_campus:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $2,750”
  - on_campus:TOTAL: 37377 ⟵ “TOTAL | $37,377 | $38,766”
  - with_parents_or_family:Tuition/Fees: 16712 ⟵ “Tuition/Fees | $16,712 | $16,712”
  - with_parents_or_family:Housing: 8403 ⟵ “Housing | $7,014 | $8,403”
  - with_parents_or_family:Food: 6821 ⟵ “Food | $6,821 | $6,821”
  - with_parents_or_family:Transportation: 2800 ⟵ “Transportation | $2,800 | $2,800”
  - with_parents_or_family:Books/Supplies: 1280 ⟵ “Books/Supplies | $1,280 | $1,280”
  - with_parents_or_family:Personal Expenses: 2750 ⟵ “Personal Expenses | $2,750 | $2,750”
  - with_parents_or_family:TOTAL: 38766 ⟵ “TOTAL | $37,377 | $38,766”
### `49ac3472770277ab` Tennessee Wesleyan University — costs 2025-26 [new] (labeled_in_source)
- source: https://www.tnwesleyan.edu/tuition-aid/costs/tuition-and-fees/ (sha256 513f0741ac29)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "rows": 3}
  - column:Tuition: 30650 ⟵ “Tuition | $30,650 | $31,880 | $15,940”
  - column:Clinical Fees: 2150 ⟵ “Clinical Fees | $2,150 | $2,250 | $1,125”
  - column:RN-BSN: 385 ⟵ “RN-BSN | $385 | $400 | ”
### `282c991268cbec2f` The University of Tennessee Southern — appeals 2026-27 [new] (source_unlabeled)
- source: http://utsouthern.edu/cost-and-aid/financial-aid/financial-aid-faq/ (sha256 47e19cd9baed)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “You’ll also find guidance on how to handle special circumstances, like locating requested documents or addressing a denied SAP appeal.”
  - sentence: sap_appeal ⟵ “What happens if my SAP appeal is denied?”
  - sentence: sap_appeal ⟵ “If your SAP appeal is denied, you can set up a payment plan with the Bursar’s Office or consider applying for a private loan to fund your education.”
### `3c8ce253aa44da71` The University of Tennessee Southern — appeals 2026-27 [new] (source_unlabeled)
- source: http://utsouthern.edu/cost-and-aid/financial-aid/financial-aid-faq/ (sha256 47e19cd9baed)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: dependency_override ⟵ “If you have any issues locating a requested document (tax document, dependency override document, etc.), please contact the Financial Aid Office at financialaid@utsouthern.edu.”
### `2edeb93a98249bd6` The University of Tennessee Southern — costs 2026-27 [new] (labeled_in_source)
- source: https://utsouthern.edu/wp-content/uploads/2026/09/2026-2027-Standard-cost-of-attendance-002.docx.pdf (sha256 690886045400)
- issues: multiple_total_rows, residency_unknown
- checks: {"columns": 1, "rows": 14}
  - column:Tuition: 10228.0 ⟵ “Tuition | $10,228.00”
  - column:Required Fees: 1374.0 ⟵ “Required Fees | $1,374.00”
  - column:Housing: 5877.0 ⟵ “Housing | $5,877.00”
  - column:Meals: 4867.0 ⟵ “Meals | $4,867.00”
  - column:Direct Costs Subtotal: 22346.0 ⟵ “Direct Costs Subtotal | $22,346.00”
  - column:Books & Supplies: 1500.0 ⟵ “Books & Supplies | $1,500.00”
  - column:Loan Fees: 95.0 ⟵ “Loan Fees | $95.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $2,000.00”
  - column:Transportation: 2500.0 ⟵ “Transportation | $2,500.00”
  - column:Indirect Costs Subtotal: 6095.0 ⟵ “Indirect Costs Subtotal | $6,095.00”
  - column:Grand Total: 28441.0 ⟵ “Grand Total | $28,441.00”
  - column:Tuition: 10228.0 ⟵ “Tuition | $10,228.00”
  - column:Required Fees: 1374.0 ⟵ “Required Fees | $1,374.00”
  - column:Direct Costs Subtotal: 11602.0 ⟵ “Direct Costs Subtotal | $11,602.00”
  - column:Estimated Housing: 9360.0 ⟵ “Estimated Housing | $9,360.00”
  - column:Food/Meals: 4867.0 ⟵ “Food/Meals | $4,867.00”
  - column:Books & Supplies: 1500.0 ⟵ “Books & Supplies | $1,500.00”
  - column:Loan Fees: 95.0 ⟵ “Loan Fees | $95.00”
  - column:Personal Expenses: 2000.0 ⟵ “Personal Expenses | $2,000.00”
  - column:Transportation: 2500.0 ⟵ “Transportation | $2,500.00”
  - column:Indirect Costs Subtot: 20322.0 ⟵ “Indirect Costs Subtot | $20,322.00”
  - column:Grand Total: 31924.0 ⟵ “Grand Total | $31,924.00”
  - column:Tuition: 10228.0 ⟵ “Tuition | $10,228.00”
  - column:Required Fees: 1374.0 ⟵ “Required Fees | $1,374.00”
  - column:Direct Costs Subtotal: 11602.0 ⟵ “Direct Costs Subtotal | $11,602.00”
  - … 19 more rows
### `2af695e235194937` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/professional-judgment (sha256 bcd75b5e1a5c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 5}
- change offered: `False` → `True`
- change process_summary: `The appeal-form guide lists no special-circumstances / professional-judgment appeal; financial aid forms pages were not fully reviewed.` → `What is considered special or unusual circumstance?`
  - sentence: need_based_special_circumstances ⟵ “What is considered special or unusual circumstance?”
  - sentence: need_based_special_circumstances ⟵ “Special circumstances are financial changes that have occurred to a student or parent since completing the FAFSA.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances refer to a student’s dependency status, also known as dependency override.”
  - sentence: need_based_special_circumstances ⟵ “None of the following conditions, singly or in combination, qualify as unusual circumstances meriting a dependency override: Parents refuse to contribute to the student's education.”
  - sentence: need_based_special_circumstances ⟵ “Submitting an explanation with supporting documentation does not guarantee a change in financial aid awards.”
### `475854835ac5e654` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/sap (sha256 6249e2865d8e)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 6}
- change process_summary: `Financial Aid / Satisfactory Academic Progress (SAP) Appeal for students who lost financial aid by not meeting SAP standards; online form; decision within 45 days.` → `Financial Aid Probation - If a student has a Satisfactory Academic Progress (SAP) Appeal approved, they will be placed on a one semester warning period if it will be possible to bring their Course Completion Rate and GPA to maintain SAP standards after the next semester.`
  - sentence: sap_appeal ⟵ “Financial Aid Probation - If a student has a Satisfactory Academic Progress (SAP) Appeal approved, they will be placed on a one semester warning period if it will be possible to bring their Course Completion Rate and GPA to maintain SAP standards after the next semester.”
  - sentence: sap_appeal ⟵ “Academic Plan - If a student has a Satisfactory Academic Progress (SAP) Appeal approved and it is NOT possible for them to maintain the required Course Completion Rate and GPA to maintain SAP after one semester of enrollment, they will be placed in a SAP Academic Plan.”
  - sentence: sap_appeal ⟵ “Notification of Status and right to appeal Students will be notified of changes to SAP status and any appeal decisions via UTC email.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeals Process and Financial Aid Appeal Forms Students appealing their Satisfactory Academic Progress status are required to submit an appeals packet for review.”
  - sentence: sap_appeal ⟵ “The following are due in the SAP Appeals packet: Financial Aid Appeal Form.”
  - sentence: sap_appeal ⟵ “Review Process There are three levels of appeal in the SAP Appeals process.”
### `7c3721ec7e7c7ea0` The University of Tennessee-Chattanooga — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships (sha256 6326d79eb37d)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: professional_judgment ⟵ “Quick Links » Calendar Campus News Canvas Change Password Class Schedule Crisis Resources Library Google Workspace MocSync MyMocsNet Microsoft O365 GTranslate Financial Aid and Scholarships Dates Forms Accepting Aid Parents Faculty and Staff Professional Judgment Frequently Asked Questions Office of Financial Aid and Scholarships Student Employment FAFSA An affordable degree starts here UTC’s Offi”
### `803d99b6e61160c1` The University of Tennessee-Chattanooga — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/chancellors-scholarship (sha256 873589ac7776)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable (i.e.”
### `84f31b27d6918f8c` The University of Tennessee-Chattanooga — appeals 2026-27 [changed] (source_unlabeled)
- source: https://www.utc.edu/enrollment-management-and-student-affairs/financial-aid-and-scholarships/scholarships/renewable-scholarships/academic-service-scholars-program (sha256 7585c71c261b)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `Scholarship Appeal for students who lost a UTC scholarship or the Tennessee HOPE scholarship because of GPA, credit completion or enrollment status; online form; decision within 45 days.` → `Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable. • You did not maintain the required cumulative GPA; • You did not pass the required number of credit hours (or service/work hours); • You have taken a fall or spring semester off and not attended classes; • You have totally withdrawn from classes for the term, officially or unofficially.`
  - sentence: scholarship_retention_appeal ⟵ “Regretfully, transferring to another school is an immediate forfeiture of any first-time student scholarship and Is Not appealable. • You did not maintain the required cumulative GPA; • You did not pass the required number of credit hours (or service/work hours); • You have taken a fall or spring semester off and not attended classes; • You have totally withdrawn from classes for the term, officia”
### `a2286e3ee4390402` The University of Tennessee-Chattanooga — costs 2026-27 [same] (labeled_in_source)
- source: https://www.utc.edu/sites/default/files/2026-09/2026-27-estimated-cost-of-attendance.pdf (sha256 4dc086460fb0)
- issues: arrangement_unlabeled
- checks: {"columns": 4, "rows": 9}
  - column:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - column:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - column:Housing: 2600 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - column:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - column:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - column:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - column:IN-STATE TOTAL: 23736 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - column:Out-of-State Tuition: 8306 ⟵ “Out-of-State Tuition | 8306 | 8306 | 8306 | 8306”
  - column:Out-of-State Total: 32042 ⟵ “Out-of-State Total | 32042 | 38242 | 38646 | 41097”
  - column:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - column:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - column:Housing: 2600 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - column:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - column:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - column:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - column:IN-STATE TOTAL: 23736 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - column:Out-of-State Tuition: 642 ⟵ “Out-of-State Tuition | 642 | 642 | 642 | 872”
  - column:Out-of-State Total: 24378 ⟵ “Out-of-State Total | 24378 | 30578 | 30982 | 33663”
  - off_campus_not_with_family:Enrollment Fees: 11084 ⟵ “Enrollment Fees | 11084 | 11084 | 11084 | 11789”
  - off_campus_not_with_family:Books: 1400 ⟵ “Books | 1400 | 1400 | 1400 | 1200”
  - off_campus_not_with_family:Housing: 8800 ⟵ “Housing | 2600 | 8800 | 9204 | 9450”
  - off_campus_not_with_family:Food: 4552 ⟵ “Food | 4552 | 4552 | 4552 | 4552”
  - off_campus_not_with_family:Transportation: 2300 ⟵ “Transportation | 2300 | 2300 | 2300 | 3200”
  - off_campus_not_with_family:Personal Expenses: 1800 ⟵ “Personal Expenses | 1800 | 1800 | 1800 | 2600”
  - off_campus_not_with_family:IN-STATE TOTAL: 29936 ⟵ “IN-STATE TOTAL | 23736 | 29936 | 30340 | 32791”
  - … 47 more rows
### `143b9cc54c51ce3f` The University of Tennessee-Knoxville — admissions_metrics 2025-26 [same] (labeled_in_source)
- source: https://irsa.utk.edu/wp-content/uploads/sites/5/2026/06/CDS_2025-26_C_.pdf (sha256 432ea71922ec)
- issues: applications_breakdown_does_not_reconcile
- checks: {"fields": ["act_25", "act_50", "act_75", "admits", "applications", "enrolled", "entering_fall_year", "sat_composite_25", "sat_composite_50", "sat_composite_75", "sat_math_25", "sat_math_50", "sat_math_75", "sat_reading_25", "sat_reading_50", "sat_reading_75"]}
  - applications: 53841 ⟵ “Total first-time, first-year (degree-seeking) who applied   11,980           41,408          452       0     53,841”
  - admits: 23464 ⟵ “Total first-time, first-year (degree-seeking) who were admitted                    8,725           14,526          213       0     23,464”
  - enrolled: 7143 ⟵ “Total first-time, first-year (degree-seeking) who enrolled                         4,326            2,764           53       0       7,143”
  - sat_composite_25..75: [1280, 1330, 1380] ⟵ “SAT Composite                                1280            1330          1380”
  - sat_reading_25..75: [640, 670, 700] ⟵ “SAT Evidence-Based Reading and   640            670           700”
  - sat_math_25..75: [630, 660, 700] ⟵ “SAT Math                                      630            660           700”
  - act_25..75: [26, 29, 31] ⟵ “ACT Composite                                 26              29            31”
### `41b39cd3bca62f93` The University of Tennessee-Knoxville — appeals 2027-28 [new] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/special-circumstances-appeals/ (sha256 74b1423ae382)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: need_based_special_circumstances ⟵ “Students may only complete one Special Circumstance Appeal per academic year (August–July).”
  - sentence: need_based_special_circumstances ⟵ “To submit a Special Circumstances Appeal, follow these steps: Step 1: Submit a Case in Vol Connect Log in to the Vol Connect Portal.”
### `6a4e50807b5201fb` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/information/ (sha256 6a3e25ffd531)
- issues: semantic_review_required, conflicts_with_verified_record
- checks: {"negative_sentences": 1, "sentences": 2}
- change process_summary: `The official Scholarship FAQ answers "Will UT match scholarship and financial aid offers from other institutions?" with "UT cannot match scholarship or aid offers from other institutions."` → `Will UT match scholarship and financial aid offers from other institutions?`
  - sentence: competing_offer_review ⟵ “Will UT match scholarship and financial aid offers from other institutions?”
  - sentence: competing_offer_review ⟵ “UT cannot match scholarship or aid offers from other institutions.”
### `8ec83f4d2db7b0e0` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/satisfactory-academic-progress-sap-appeals/ (sha256 f5ccbbd2241d)
- issues: semantic_review_required, conflicts_with_verified_record
- checks: {"negative_sentences": 0, "sentences": 4}
- change process_summary: `Satisfactory Academic Progress appeals to restore federal aid eligibility: personal statement (what happened, what changed, academic plan), third-party documentation and an advisor-signed academic plan; due at least 14 days before the last day of classes for the term.` → `How to Start Your SAP Appeal To. submit a SAP appeal, follow these steps: Step 1: Submit a Case in Vol Connect Portal Log in to the Vol Connect Portal Open a new case, select Financial Aid as the Request Type.`
  - sentence: sap_appeal ⟵ “How to Start Your SAP Appeal To. submit a SAP appeal, follow these steps: Step 1: Submit a Case in Vol Connect Portal Log in to the Vol Connect Portal Open a new case, select Financial Aid as the Request Type.”
  - sentence: sap_appeal ⟵ “What You’ll Need to Submit Once you access the CampusLogic Student Forms Portal, you will see your SAP Appeal requirement.”
  - sentence: sap_appeal ⟵ “Incomplete SAP appeals will not be reviewed.”
  - sentence: sap_appeal ⟵ “Once your materials are submitted, the SAP Appeal Committee will review your case.”
### `af0e67c44ecb2585` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/hope-institutional-scholarship-appeals/ (sha256 4874a65580e6)
- issues: semantic_review_required, conflicts_with_verified_record
- checks: {"negative_sentences": 0, "sentences": 6}
- change process_summary: `HOPE & Institutional Scholarship Appeals: students may appeal loss of HOPE or institutional scholarship eligibility caused by extenuating circumstances (health emergency, death of immediate family member, mental health crisis). Dropping courses to protect GPA does not qualify. HOPE GPA review after a later benchmark and the one-time HOPE grade-replacement option are also handled here. Complete appeals (statement plus documentation) go to the Institutional Review Panel. Chancellor's Scholarship GPA-loss appeals can grant probationary eligibility for one semester.` → `In certain circumstances, students may appeal a loss of scholarship eligibility when an extenuating circumstance affected their ability to meet those requirements.`
  - sentence: scholarship_retention_appeal ⟵ “In certain circumstances, students may appeal a loss of scholarship eligibility when an extenuating circumstance affected their ability to meet those requirements.”
  - sentence: scholarship_retention_appeal ⟵ “Eligibility for HOPE & Institutional Scholarship Appeals If an extenuating circumstance affected your ability to meet the scholarship’s requirements, you may be eligible to appeal your loss of scholarship eligibility.”
  - sentence: scholarship_retention_appeal ⟵ “If you have already lost your HOPE Scholarship due to a change in enrollment status, you may appeal to regain your award.”
  - sentence: scholarship_retention_appeal ⟵ “How to Submit a HOPE & Institutional Scholarship Appeal Access the Hope & Institutional Scholarship Appeal Request Form to begin the appeal process.”
  - sentence: scholarship_retention_appeal ⟵ “HOPE Scholarship Appeals: If your appeal is denied by the IRP, you may appeal directly with THEC within 45 days of receiving your denial letter.”
  - sentence: scholarship_retention_appeal ⟵ “For more information, visit TELS, TN Promise and TN Reconnect Appeals and Exceptions – collegefortn.org.”
### `ca72bad652134d7c` The University of Tennessee-Knoxville — appeals 2026-27 [changed] (source_unlabeled)
- source: https://onestop.utk.edu/scholarships-financial-aid/financial-aid/financial-aid-appeals/budget-increase-appeals/ (sha256 0985de3b2eff)
- issues: semantic_review_required, conflicts_with_verified_record
- checks: {"negative_sentences": 0, "sentences": 1}
- change process_summary: `Budget Increase Appeals for additional education-related expenses (childcare, one-time computer purchase, internship/student teaching, one medical expense per year, extra books/supplies, study abroad). Excludes reimbursed expenses, amounts within the standard allowance, vehicle costs and expenses while not enrolled. Approval does not guarantee additional aid; decisions are final absent new documentation.` → `To submit a Budget Increase Appeal, follow these steps: Step 1: Submit a Case in Vol Connect Log in to the Vol Connect Portal.`
  - sentence: budget_increase ⟵ “To submit a Budget Increase Appeal, follow these steps: Step 1: Submit a Case in Vol Connect Log in to the Vol Connect Portal.”
### `64df3f993a28f354` The University of Tennessee-Knoxville — awards 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/tri-star-scholarships/ (sha256 ea37b91e6e74)
- issues: conflicts_with_verified_record
- checks: {"thresholds": null}
- change award_type: `institutional_access` → `institutional_other`
- change award_amount_text: `Combined with HOPE, covers tuition and mandatory fees for up to eight semesters.` → `Tuition & mandatory fees`
  - award_amount_text: Tuition & mandatory fees ⟵ “Flagship Scholarship | First-time, First-Year, Current, & Transfer Students | Tuition & mandatory fees | UT Priority Filing Date | January 5”
### `b1e41d995c882d23` The University of Tennessee-Knoxville — awards 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/tri-star-scholarships/ (sha256 ea37b91e6e74)
- issues: conflicts_with_verified_record
- checks: {"thresholds": null}
- change award_type: `institutional_need_last_dollar` → `institutional_other`
- change award_amount_text: `Last-dollar award covering tuition and mandatory fees when combined with other federal, state and institutional aid.` → `Tuition & mandatory fees`
  - award_amount_text: Tuition & mandatory fees ⟵ “UT Promise Scholarship | First-Year, Transfer, Current, & Non-Traditional Students receiving HOPE Scholarship | Tuition & mandatory fees | UT Priority Filing Date | January 5”
### `bd678104827453ae` The University of Tennessee-Knoxville — awards 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/tri-star-scholarships/ (sha256 ea37b91e6e74)
- issues: conflicts_with_verified_record
- checks: {"thresholds": null}
- change award_type: `institutional_need_last_dollar` → `institutional_other`
- change award_amount_text: `Last-dollar award that, combined with other aid, covers tuition, mandatory fees and average on-campus housing and food, for up to eight semesters; college-specific course fees for architecture, business, engineering and nursing are not covered.` → `Tuition, mandatory fees, average on-campus Housing and Food*`
  - award_amount_text: Tuition, mandatory fees, average on-campus Housing and Food* ⟵ “Tennessee Pledge Scholarship | First-time, First-Year, Current, & Transfer Students | Tuition, mandatory fees, average on-campus Housing and Food* | UT Priority Filing Date | January 5”
### `e16d7756eb6006b2` The University of Tennessee-Knoxville — awards 2026-27 [changed] (labeled_in_source)
- source: https://onestop.utk.edu/scholarships-financial-aid/scholarships/next-chapter-scholarship-next-chapter-scholar-of-the-year-award/ (sha256 5e9a2df6649e)
- issues: conflicts_with_verified_record
- checks: {"thresholds": null}
- change award_type: `institutional_program_based` → `institutional_other`
- change award_amount_text: `$1,500 per year, up to $6,000 over four years.` → `$1,500`
  - award_amount_text: $1,500 ⟵ “Next Chapter Scholarship | $1,500 | $6,000 | $26,400”
### `1669455e8679fac0` The University of Tennessee-Knoxville — costs 2025-26 [same] (labeled_in_source)
- source: https://admissions.utk.edu/undergraduate-tuition-aid/ (sha256 a1801be28b0e)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition & Fees: 33336 ⟵ “Tuition & Fees | $33,336”
  - column:Housing & Food: 14738 ⟵ “Housing & Food | $14,738”
  - column:Books, Course Materials, Supplies and Equipment: 1598 ⟵ “Books, Course Materials, Supplies and Equipment | $1,598”
  - column:Total: 49672 ⟵ “Total | $49,672”
### `3313ea939c910599` The University of Tennessee-Knoxville — costs 2026-27 [same] (labeled_in_source)
- source: https://onestop.utk.edu/billing-payments/cost-of-attending-ut-undergraduate-student/ (sha256 f81e0fa4d378)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 31672 ⟵ “Tuition | $11,560 | $31,672”
  - column:FeesThis is an estimate of what a student will spend on tuition and fees for the Fall and Spring semesters.: 2806 ⟵ “FeesThis is an estimate of what a student will spend on tuition and fees for the Fall and Spring semesters. | $2,464 | $2,806”
  - column:On-Campus Housing*This is an estimate of what a student will spend on housing and meals for the Fall and Spring semesters if they live in university housing.: 9572 ⟵ “On-Campus Housing*This is an estimate of what a student will spend on housing and meals for the Fall and Spring semesters if they live in university housing. | $9,572 | $9,572”
  - column:Food: 5166 ⟵ “Food | $5,166 | $5,166”
  - column:TransportationThis item is for budgeting purposes only and will not be billed to you.: 3500 ⟵ “TransportationThis item is for budgeting purposes only and will not be billed to you. | $3,500 | $3,500”
  - column:Miscellaneous Personal Expenses (Based on personal spending habits)This item is for budgeting purposes only and will not be billed to you.: 3042 ⟵ “Miscellaneous Personal Expenses (Based on personal spending habits)This item is for budgeting purposes only and will not be billed to you. | $3,042 | $3,042”
  - column:Loan FeesThis is an estimate of what the average student spends in federal loan origination fee.: 92 ⟵ “Loan FeesThis is an estimate of what the average student spends in federal loan origination fee. | $92 | $92”
  - column:Total, with on-campus housing(Direct costs plus estimated indirect costs): 57448 ⟵ “Total, with on-campus housing(Direct costs plus estimated indirect costs) | $36,994 | $57,448”
### `67d0ececd1764a10` The University of Tennessee-Knoxville — costs 2026-27 [same] (labeled_in_source)
- source: https://onestop.utk.edu/billing-payments/cost-of-attending-ut-undergraduate-student/ (sha256 f81e0fa4d378)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 11560 ⟵ “Tuition | $11,560 | $31,672”
  - column:FeesThis is an estimate of what a student will spend on tuition and fees for the Fall and Spring semesters.: 2464 ⟵ “FeesThis is an estimate of what a student will spend on tuition and fees for the Fall and Spring semesters. | $2,464 | $2,806”
  - column:On-Campus Housing*This is an estimate of what a student will spend on housing and meals for the Fall and Spring semesters if they live in university housing.: 9572 ⟵ “On-Campus Housing*This is an estimate of what a student will spend on housing and meals for the Fall and Spring semesters if they live in university housing. | $9,572 | $9,572”
  - column:Food: 5166 ⟵ “Food | $5,166 | $5,166”
  - column:TransportationThis item is for budgeting purposes only and will not be billed to you.: 3500 ⟵ “TransportationThis item is for budgeting purposes only and will not be billed to you. | $3,500 | $3,500”
  - column:Miscellaneous Personal Expenses (Based on personal spending habits)This item is for budgeting purposes only and will not be billed to you.: 3042 ⟵ “Miscellaneous Personal Expenses (Based on personal spending habits)This item is for budgeting purposes only and will not be billed to you. | $3,042 | $3,042”
  - column:Loan FeesThis is an estimate of what the average student spends in federal loan origination fee.: 92 ⟵ “Loan FeesThis is an estimate of what the average student spends in federal loan origination fee. | $92 | $92”
  - column:Total, with on-campus housing(Direct costs plus estimated indirect costs): 36994 ⟵ “Total, with on-campus housing(Direct costs plus estimated indirect costs) | $36,994 | $57,448”
### `fefa1a724355ffd3` The University of Tennessee-Knoxville — costs 2025-26 [same] (labeled_in_source)
- source: https://admissions.utk.edu/undergraduate-tuition-aid/ (sha256 a1801be28b0e)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 4}
  - column:Tuition & Fees: 13876 ⟵ “Tuition & Fees | $13,876”
  - column:Housing & Food: 14738 ⟵ “Housing & Food | $14,738”
  - column:Books, Course Materials, Supplies and Equipment: 1598 ⟵ “Books, Course Materials, Supplies and Equipment | $1,598”
  - column:Total: 30212 ⟵ “Total | $30,212”
### `17e6ba0181e925d1` The University of Tennessee-Knoxville — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://admissions.utk.edu/admitted-students-vols-online/ (sha256 b907d5b43937)
- issues: conflicting_values:residency_requirement_credits
- checks: {"fields": ["min_grade"]}
  - min_grade: D- ⟵ “Transfer credit will be granted only for college level non-remedial courses in which a grade of D- or better was earned.”
### `3e811b11eb2b90f2` Union University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.uu.edu/admissions/financial-aid/policies-practices/ (sha256 f1fcbd38ec16)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 11}
  - sentence: need_based_special_circumstances ⟵ “Skip To: General Policies Academic Standards/Satisfactory Academic Progress Institutional Scholarship Policy Loan Credit Refund Dates Consumer Information Special Circumstances Policy General Policies Edits made to reflect 2021-22 and 2022-23 Academic Year applicable information.”
  - sentence: need_based_special_circumstances ⟵ “Students/parents must complete a Special Circumstances Form available on the Student Financial Aid website (or by contacting the Office of Student Financial Aid), providing any other requested support documentation, and be available to discuss your situation if needed with a staff member from Student Financial Aid.”
  - sentence: need_based_special_circumstances ⟵ “If selected for verification, a student’s FAFSA information must be verified and corrected before consideration for special circumstances adjustment can be given.”
  - sentence: need_based_special_circumstances ⟵ “Decision regarding Special Circumstance appeals are final.”
  - sentence: need_based_special_circumstances ⟵ “Special Circumstance Policy The rules and the formula to determine financial aid eligibility are standard for all applicants.”
  - sentence: need_based_special_circumstances ⟵ “Submitting an appeal for special circumstances does not guarantee that it will be approved, or additional financial aid will be granted.”
### `3f66df20c2f013f9` Union University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.uu.edu/admissions/financial-aid/policies-practices/ (sha256 f1fcbd38ec16)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal While students are expected to meet the minimum academic progress requirements to maintain eligibility for financial aid, the university recognizes that extenuating circumstances may occasionally prevent students from making satisfactory progress toward their degree.”
  - sentence: sap_appeal ⟵ “If the student becomes ineligible for financial aid due to not meeting Satisfactory Academic Progress (SAP) requirements before the beginning of the academic year, and if extenuating circumstances have impacted their academic performance, he/she may submit a SAP Appeal for reconsideration of financial aid eligibility.”
  - sentence: sap_appeal ⟵ “The SAP Appeal provides an opportunity for students to explain the circumstances that affected their academic progress and request an evaluation of their financial aid status.”
### `54912e5cf9e2d60a` Union University — appeals 2026-27 [new] (ambiguous_year_labels)
- source: https://www.uu.edu/admissions/financial-aid/policies-practices/ (sha256 f1fcbd38ec16)
- issues: ambiguous_year_labels, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: professional_judgment ⟵ “Adjustments for Special Circumstances Students who feel their FAFSA information does not accurately reflect their financial situation due to certain special or unusual circumstances, may request to have their FAFSA information reviewed for possible adjustment (known as a Professional Judgement).”
  - sentence: professional_judgment ⟵ “However, there is some flexibility, when appropriate, for financial aid administrators to exercise professional judgment on a case-by-case basis to override the student’s dependency status and/or recalculate the student’s eligibility for financial aid.”
### `46bbe41a32114522` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/undergraduate/satisfactory-progress/ (sha256 0e2a9db63644)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Appeal Procedures Any student whose institutional and/or federal Title IV student aid is Suspended due to unsatisfactory academic progress may submit an appeal for reinstatement of such assistance to the Office of Student Financial Aid and Scholarships.”
### `ae84673adb817048` Vanderbilt University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.vanderbilt.edu/financialaid/wp-content/uploads/sites/92/2025/09/UGRAD-Request-for-Reconsideration.pdf (sha256 e721fc9b72cb)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Special circumstances refer to financial situations that may lead to a financial aid adjustment.”
  - sentence: need_based_special_circumstances ⟵ “Reconsideration of your financial aid eligibility can be given under such special circumstances, and if you have not already notified us of such errors, omissions, or significant changes, please do so at this time.”
  - sentence: need_based_special_circumstances ⟵ “Unusual circumstances refer to conditions that may lead to an adjustment to a student’s dependency status based on a unique situation.”
### `b8a9ee2b997f4618` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/reconsideration/ (sha256 df0f09fb51b0)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: professional_judgment ⟵ “This type of adjustment is called a Request for Professional Judgment.”
  - sentence: professional_judgment ⟵ “The Financial Aid Office may use professional judgment on a case-by-case basis to adjust a student’s cost of attendance or the data used to calculate the students’ Student Aid Index.”
  - sentence: professional_judgment ⟵ “A school is not permitted to make a professional judgment for a student after that student has ceased to be eligible, including when the student is no longer enrolled.”
### `ccd0f2820fde28b2` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/reconsideration/ (sha256 df0f09fb51b0)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: dependency_override ⟵ “This type of adjustment is called a Dependency Override.”
  - sentence: dependency_override ⟵ “All requests for determination of independence, including dependency overrides and unaccompanied homeless youth determinations, will be reviewed as soon as practicable once all documentation is received.”
### `eb2bb7f349820d99` Vanderbilt University — appeals 2025-26 [new] (labeled_in_source)
- source: https://www.vanderbilt.edu/financialaid/undergraduate/satisfactory-progress/ (sha256 0e2a9db63644)
- issues: stale_year_label:2025-26, semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “The appeal for reinstatement should include the following elements: An explanation of extenuating circumstances, such as injury, illness, death of a relative, or other special circumstance as to why you failed to meet satisfactory academic progress requirements.”
### `1c5d13913b963237` Vanderbilt University — costs 2026-27 [new] (labeled_in_source)
- source: https://admissions.vanderbilt.edu/affordability/ (sha256 a80f3d79c819)
- issues: components_do_not_reconcile
- checks: {"columns": 1, "components_reconcile": false, "rows": 8}
  - column:Tuition: 69822 ⟵ “Tuition | $69,822”
  - column:Housing: 15170 ⟵ “Housing | $15,170”
  - column:Food: 8520 ⟵ “Food | $8,520”
  - column:Student Support Fee: 3384 ⟵ “Student Support Fee | $3,384”
  - column:Total Direct Cost of Attendance – Mandatory: 96896 ⟵ “Total Direct Cost of Attendance – Mandatory | $96,896”
  - column:Books, Course Materials, Supplies, & Equipment Allowance: 1100 ⟵ “Books, Course Materials, Supplies, & Equipment Allowance | $1,100”
  - column:Personal Expenses Allowance: 1998 ⟵ “Personal Expenses Allowance | $1,998”
  - column:Total Indirect Costs – Discretionary/Elective: 3098 ⟵ “Total Indirect Costs – Discretionary/Elective | $3,098”
### `eddc7681649bd17c` Walters State Community College — appeals 2026-27 [new] (source_unlabeled)
- source: https://ws.edu/cost-aid/eligibility-verification/maintain/index.aspx (sha256 5ce4c5393838)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “Appeals will be considered for the following reasons: Serious injury or illness of the student Death, serious injury/illness of immediate family member (mother, father, sibling, spouse, child) Family trauma which occurred during the semester in question Other extenuating circumstances (must be documented) Process for filing an appeal: Complete the Satisfactory Academic Progress (SAP) Appeal.”
  - sentence: sap_appeal ⟵ “Forms are available in the Financial Aid Office and off-campus sites or by emailing finaid@ws.edu from Senators Mail account to request the electronic SAP appeal.”

## Re-verification of existing records (57)

- nothing_to_check: data/institutions/abcnash/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219505", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Academic Achievement"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Dean's"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Governor's Excellence"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Governor's Merit"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Presidential"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Presidents Emerging Leaders Program (PELP)Apply by 12/31"}]
- all_values_found_year_not_labeled: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Kimbrough (Limited Awards Available)"}]
- nothing_to_check: data/institutions/apsu/awards/2026-27.json ["awards", "ipeds-219602", null, "2026-27", {"award_name": "Howell C. Smith (Limited Awards Available)"}]
- all_values_found_year_not_labeled: data/institutions/belmont/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219709", null, "2026-27", {}]
- values_not_found_verbatim: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Platinum"}] missing=['thresholds.gpa_min']
- values_not_found_verbatim: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Silver"}] missing=['thresholds.gpa_min']
- values_not_found_verbatim: data/institutions/bryan/awards/2026-27.json ["awards", "ipeds-219790", null, "2026-27", {"award_name": "Crimson"}] missing=['thresholds.gpa_min']
- all_values_found_year_not_labeled: data/institutions/jscc/costs/2026-27.json ["costs", "ipeds-220400", null, "2026-27", {"residency": "out_of_state"}]
- all_values_found_year_not_labeled: data/institutions/jscc/credit_policies/2026-27.json ["credit_policies", "ipeds-220400", null, "2026-27", {"policy_kind": "AP"}]
- nothing_to_check: data/institutions/jscc/credit_policies/2026-27.json ["credit_policies", "ipeds-220400", null, "2026-27", {"policy_kind": "CLEP"}]
- nothing_to_check: data/institutions/johnsonu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-220473", null, "2026-27", {}]
- all_values_found_year_not_labeled: data/institutions/lanecollege/transfer_policies/2026-27.json ["transfer_policies", "ipeds-220598", null, "2026-27", {}]
- nothing_to_check: data/institutions/lipscomb/credit_policies/2026-27.json ["credit_policies", "ipeds-219976", null, "2026-27", {"policy_kind": "AP"}]
- nothing_to_check: data/institutions/lipscomb/transfer_policies/2026-27.json ["transfer_policies", "ipeds-219976", null, "2026-27", {}]
- nothing_to_check: data/institutions/midsouthchristian/transfer_policies/2026-27.json ["transfer_policies", "ipeds-481225", null, "2026-27", {}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "sap_appeal"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "scholarship_retention_appeal"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "merit_reconsideration"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "competing_offer_review"}]
- nothing_to_check: data/institutions/utc/appeals/2026-27.json ["appeals", "ipeds-221740", null, "2026-27", {"appeal_kind": "need_based_special_circumstances"}]
- policy_text_not_verbatim: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Chancellor's Scholarship"}] year=2025-26
- policy_text_not_verbatim: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Provost's Scholarship"}] year=2025-26
- policy_text_not_verbatim: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Mocs Scholarship"}] year=2025-26
- policy_text_not_verbatim: data/institutions/utc/awards/2027-28.json ["awards", "ipeds-221740", null, "2027-28", {"award_name": "Academic Service Scholars Program"}]
- values_not_found_verbatim: data/institutions/utc/costs/2026-27.json ["costs", "ipeds-221740", null, "2026-27", {"residency": "in_state"}] missing=['on_campus_food_housing', 'on_campus_other_expenses'] year=2026-27
- values_not_found_verbatim: data/institutions/utc/costs/2026-27.json ["costs", "ipeds-221740", null, "2026-27", {"residency": "out_of_state"}] missing=['on_campus_food_housing', 'on_campus_other_expenses'] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/credit_policies/2026-27.json ["credit_policies", "ipeds-221740", null, "2026-27", {"policy_kind": "AP"}]
- policy_text_not_verbatim: data/institutions/utc/credit_policies/2026-27.json ["credit_policies", "ipeds-221740", null, "2026-27", {"policy_kind": "CLEP"}]
- all_values_found_year_not_labeled: data/institutions/utc/credit_policies/2026-27.json ["credit_policies", "ipeds-221740", null, "2026-27", {"policy_kind": "IB"}]
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "program-total"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "upper-division-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "residency-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "gen-ed-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "computer-science-data-science-ai-bs", "requirement_key": "four-year-plan"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "program-total"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "upper-division-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "residency-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "gen-ed-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "nursing-bsn", "requirement_key": "four-year-plan"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "program-total"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "upper-division-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "residency-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "gen-ed-hours"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "major-hours"}] year=2026-27
- nothing_to_check: data/institutions/utc/degree_requirements/2026-27.json ["degree_requirements", "ipeds-221740", null, "2026-27", {"program_key": "psychology-bs", "requirement_key": "four-year-plan"}] year=2026-27
- values_not_found_verbatim: data/institutions/utc/transfer_policies/2026-27.json ["transfer_policies", "ipeds-221740", null, "2026-27", {}] missing=['residency_requirement_credits']
- nothing_to_check: data/institutions/utk/awards/2026-27.json ["awards", "utk", null, "2026-27", {"award_name": "Manning Scholars"}] year=2026-27
- policy_text_not_verbatim: data/institutions/utk/awards/2026-27.json ["awards", "utk", null, "2026-27", {"award_name": "Out-of-State Volunteer Scholarship"}] year=2026-27
- source_not_fetched: data/institutions/utk/transfer_policies/2026-27.json ["transfer_policies", "utk", null, "2026-27", {}]

## Statewide sources

Pages fetched: 80; pages by category: admissions_tests 2, common_data_set 1, cost_of_attendance 1, degree_requirements 2, merit_scholarships 2, residency 2, statewide_articulation 68, transfer_credit 68, tuition_fees 2

## Blocked by the site (every request refused; needs the browser fallback)

- Chattanooga State Community College (`ipeds-219824`)
- Cleveland State Community College (`ipeds-219879`)
- Cumberland University (`ipeds-219949`)
- Pellissippi State Community College (`ipeds-221643`)
- The University of Tennessee-Martin (`ipeds-221768`)
- Volunteer State Community College (`ipeds-222053`)
- Milligan University (`ipeds-486901`)

## Leads: official pages found with no extracted record

- American Baptist College: tuition_fees, cost_of_attendance, admissions_tests, degree_requirements
- Austin Peay State University: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, residency, degree_requirements
- Baptist Health Sciences University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, statewide_articulation, residency, degree_requirements
- Belmont University: cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, ib_credit, dual_enrollment, residency, degree_requirements
- Bethel University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Bryan College-Dayton: cost_of_attendance, admissions_tests, ap_credit, clep_credit, dual_enrollment, transfer_credit, degree_requirements
- Carson-Newman University: cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, degree_requirements
- Christian Brothers University: tuition_fees, cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Columbia State Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, residency, degree_requirements
- Dyersburg State Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, dual_enrollment, transfer_credit, residency, degree_requirements
- East Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Fisk University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Freed-Hardeman University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Herzing University-Nashville: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, transfer_credit, degree_requirements
- Jackson State Community College: tuition_fees, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- John A Gupton College: tuition_fees, cost_of_attendance, admissions_tests, degree_requirements
- Johnson University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency, degree_requirements
- King University: tuition_fees, admissions_tests, dual_enrollment, residency, degree_requirements
- Lane College: cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, degree_requirements
- Le Moyne-Owen College: tuition_fees, cost_of_attendance, dual_enrollment, transfer_credit
- Lee University: tuition_fees, cost_of_attendance, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Lincoln Memorial University: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, transfer_credit, degree_requirements
- Lipscomb University: admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, degree_requirements
- Maryville College: cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements
- Mid-South Christian College: tuition_fees, cost_of_attendance
- Middle Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Motlow State Community College: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Nashville State Community College: tuition_fees, cost_of_attendance, admissions_tests, ap_credit, clep_credit, dual_enrollment, statewide_articulation, residency, degree_requirements
- Northeast State Community College: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- Remington College-Memphis Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Remington College-Nashville Campus: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, transfer_credit
- Rhodes College: cost_of_attendance, merit_scholarships, ap_credit, ib_credit, dual_enrollment, degree_requirements
- Roane State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Southern Adventist University: cost_of_attendance, admissions_tests, dual_enrollment, transfer_credit, degree_requirements
- Southwest Tennessee Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, degree_requirements, aid_appeals
- Tennessee State University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, ib_credit, transfer_credit, statewide_articulation, residency, degree_requirements
- Tennessee Technological University: admissions_tests, dual_enrollment, transfer_credit, residency, degree_requirements
- Tennessee Wesleyan University: cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, residency, degree_requirements
- The University of Tennessee Southern: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, degree_requirements
- The University of Tennessee-Chattanooga: tuition_fees, admissions_tests, dual_enrollment, transfer_credit, statewide_articulation, residency
- The University of Tennessee-Knoxville: statewide_articulation, residency
- The University of the South: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements, aid_appeals
- Trevecca Nazarene University: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Tusculum University: tuition_fees, cost_of_attendance, admissions_tests, common_data_set, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- Union University: admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- University of Memphis: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements, aid_appeals
- Vanderbilt University: admissions_tests, merit_scholarships, transfer_credit, degree_requirements
- Visible Music College: cost_of_attendance
- Walters State Community College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, ap_credit, clep_credit, dual_enrollment, transfer_credit, statewide_articulation, residency, degree_requirements
- Welch College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
- William R Moore College of Technology: tuition_fees, admissions_tests, merit_scholarships
- Williamson Christian College: tuition_fees, cost_of_attendance, admissions_tests, merit_scholarships, dual_enrollment, transfer_credit, degree_requirements
