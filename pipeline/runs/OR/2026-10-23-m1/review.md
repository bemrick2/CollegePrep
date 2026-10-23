# Review queue — OR (2026-27)

Pages fetched: 180; failures: 2. Candidates: 24 (3 without issues, 21 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 4 | 0 | 0 | 2 | 0 | 0 | 38 |
| cost_of_attendance | 2 | 0 | 0 | 1 | 1 | 0 | 40 |
| admissions_tests | 0 | 0 | 0 | 0 | 2 | 0 | 42 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 2 | 42 |
| merit_scholarships | 0 | 3 | 0 | 0 | 0 | 0 | 41 |
| ap_credit | 0 | 4 | 0 | 0 | 2 | 0 | 38 |
| clep_credit | 0 | 2 | 0 | 0 | 0 | 2 | 40 |
| ib_credit | 0 | 3 | 0 | 0 | 1 | 1 | 39 |
| dual_enrollment | 0 | 0 | 0 | 0 | 1 | 1 | 42 |
| transfer_credit | 0 | 0 | 0 | 0 | 2 | 0 | 42 |
| statewide_articulation | 0 | 0 | 0 | 0 | 0 | 2 | 42 |
| residency | 0 | 0 | 0 | 0 | 2 | 0 | 42 |
| degree_requirements | 7 | 0 | 0 | 0 | 0 | 0 | 37 |
| aid_appeals | 0 | 0 | 0 | 2 | 0 | 0 | 42 |

## Ready for review (3)

### `42bf78165051554e` University of Oregon — awards 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/ib_scholarship (sha256 0d5db66d8d9f)
- checks: {"table_scope": "Award Information", "thresholds": null}
  - award_amount_text: $1,000/year ⟵ “24-27 | $1,000/year | $2,000/year | IB Milestone Scholarship”
  - test_requirement: 24-27 ⟵ “24-27 | $1,000/year | $2,000/year | IB Milestone Scholarship”
### `b6d98539c5137f31` University of Oregon — awards 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/ib_scholarship (sha256 0d5db66d8d9f)
- checks: {"table_scope": "Award Information", "thresholds": null}
  - award_amount_text: $2,000/year ⟵ “28-32 | $2,000/year | $4,000/year | IB Scholar Scholarship”
  - test_requirement: 28-32 ⟵ “28-32 | $2,000/year | $4,000/year | IB Scholar Scholarship”
### `dbd339c6cadfd4f9` University of Oregon — awards 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/ib_scholarship (sha256 0d5db66d8d9f)
- checks: {"table_scope": "Award Information", "thresholds": null}
  - award_amount_text: $3,000/year ⟵ “33+ | $3,000/year | $6,000/year | IB Exemplar Scholarship”
  - test_requirement: 33+ ⟵ “33+ | $3,000/year | $6,000/year | IB Exemplar Scholarship”

## Exceptions (21)

### `21d71736b2cba9a6` Oregon State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://engineering.oregonstate.edu/tools-services/how-to-pay-for-college/undergrad-scholarships (sha256 6ce660430b21)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: scholarship_retention_appeal ⟵ “If you are not going to meet the requirements of your scholarship, you can use the COE Scholarship Appeal Form.”
  - sentence: scholarship_retention_appeal ⟵ “You can use the COE Scholarship Appeal Form for this purpose.”
### `c70b33d97feea41d` Oregon State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://financialaid.oregonstate.edu/satisfactory-academic-progress (sha256 8867c8f97207)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “You will find the link to complete a SAP appeal through your portal.”
### `e45f703f0b9a4f4a` Oregon State University — appeals 2026-27 [new] (source_unlabeled)
- source: https://admissions.oregonstate.edu/admission-appeals (sha256 461d4ec58574)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Your statement must specifically address: The extraordinary circumstances why you did not meet and exceed Oregon State’s minimum admissions requirements What you have done or are doing to mitigate the impact of your extraordinary circumstances What are your strengths and how they will result in your success at Oregon State Why you have chosen Oregon State University Your academic and/or career goa”
### `65559bccdebbeb44` Oregon State University — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://leadership.oregonstate.edu/sites/leadership.oregonstate.edu/files/2026-03/fac-5a-corrected-fy2027-tuition-and-fees.pdf (sha256 cbb8c5625353)
- issues: arrangement_unlabeled, residency_unknown
- checks: {"columns": 12, "rows": 57}
  - column:Projected net tuition &Fees: 548.6 ⟵ “Projected net tuition &Fees | 548.6 | 580.9”
  - column:Marginal revenue: 32.3 ⟵ “Marginal revenue | 32.3”
  - column:Oregon Resident: 275 ⟵ “Oregon Resident | $275 | $291”
  - column:Non-Resident: 819 ⟵ “Non-Resident | $819 | $866”
  - column:Ecampus: 384 ⟵ “Ecampus | $384 | $394”
  - column:Oregon Resident (2): 16 ⟵ “Oregon Resident | $16”
  - column:Non-Resident (2): 47 ⟵ “Non-Resident | $47”
  - column:Ecampus (2): 10 ⟵ “Ecampus | $10”
  - column:Oregon Resident (45 credits): 12675 ⟵ “Oregon Resident (45 credits) | $12,675 | $13,395”
  - column:Non-Resident (45 credits): 37860 ⟵ “Non-Resident (45 credits) | $37,860 | $39,975”
  - column:Ecampus (24 credits): 9216 ⟵ “Ecampus (24 credits) | $9,216 | $9,456”
  - column:Matriculated prior to July 2022: 100 ⟵ “Matriculated prior to July 2022 | 100 | 268 | 12,360 | 100 | 283 | 13,035 | 675 | 5.46%”
  - column:Matriculated 2022-23: 100 ⟵ “Matriculated 2022-23 | 100 | 270 | 12,450 | 100 | 286 | 13,170 | 720 | 5.78%”
  - column:Matriculated 2023-24: 100 ⟵ “Matriculated 2023-24 | 100 | 272 | 12,540 | 100 | 288 | 13,260 | 720 | 5.74%”
  - column:Matriculated 2024-25: 100 ⟵ “Matriculated 2024-25 | 100 | 274 | 12,630 | 100 | 290 | 13,350 | 720 | 5.70%”
  - column:Matriculated 2025-26: 100 ⟵ “Matriculated 2025-26 | 100 | 275 | 12,675 | 100 | 291 | 13,395 | 720 | 5.68%”
  - column:Matriculated 2026-27: 100 ⟵ “Matriculated 2026-27 | 100 | 100 | 292 | 13,440 | 765 | 6.04%”
  - column:Matriculated prior to July 2022 (2): 100 ⟵ “Matriculated prior to July 2022 | 100 | 264 | 12,180 | 100 | 279 | 12,855 | 675 | 5.54%”
  - column:Matriculated 2022-23 (2): 100 ⟵ “Matriculated 2022-23 | 100 | 270 | 12,450 | 100 | 286 | 13,170 | 720 | 5.78%”
  - column:Matriculated 2023-24 (2): 100 ⟵ “Matriculated 2023-24 | 100 | 272 | 12,540 | 100 | 288 | 13,260 | 720 | 5.74%”
  - column:Matriculated 2024-25 (2): 100 ⟵ “Matriculated 2024-25 | 100 | 274 | 12,630 | 100 | 290 | 13,350 | 720 | 5.70%”
  - column:Matriculated 2025-26 (2): 100 ⟵ “Matriculated 2025-26 | 100 | 275 | 12,675 | 100 | 291 | 13,395 | 720 | 5.68%”
  - column:Matriculated 2026-27 (2): 100 ⟵ “Matriculated 2026-27 | 100 | 100 | 292 | 13,440 | 765 | 6.04%”
  - column:Matriculated prior to July 2022 (3): 335 ⟵ “Matriculated prior to July 2022 | 335 | 800 | 37,005 | 335 | 846 | 39,075 | 2,070 | 5.59%”
  - column:Matriculated 2022-23 (3): 335 ⟵ “Matriculated 2022-23 | 335 | 808 | 37,365 | 335 | 854 | 39,435 | 2,070 | 5.54%”
  - … 405 more rows
### `b1dcc46d0c5e3ea6` Oregon State University — costs 2025-26 · residency=not_applicable [new] (labeled_in_source)
- source: https://leadership.oregonstate.edu/sites/leadership.oregonstate.edu/files/2025-02/fac-4a-tuition-rates-and-fees.pdf (sha256 5b8bcc767414)
- issues: arrangement_unlabeled, residency_unknown, stale_year_label:2025-26
- checks: {"columns": 7, "rows": 57}
  - column:Projected net tuition & Fees: 522.9 ⟵ “Projected net tuition & Fees | 522.9 | 564.5”
  - column:Marginal revenue: 41.5 ⟵ “Marginal revenue | 41.5”
  - column:Oregon Resident: 261 ⟵ “Oregon Resident | $261 | $275”
  - column:Non-Resident: 778 ⟵ “Non-Resident | $778 | $819”
  - column:Ecampus: 366 ⟵ “Ecampus | $366 | $384”
  - column:Oregon Resident (2): 14 ⟵ “Oregon Resident | $14”
  - column:Non-Resident (2): 41 ⟵ “Non-Resident | $41”
  - column:Ecampus (2): 18 ⟵ “Ecampus | $18”
  - column:Oregon Resident (45 credits): 12045 ⟵ “Oregon Resident (45 credits) | $12,045 | $12,675”
  - column:Non-Resident (45 credits): 36015 ⟵ “Non-Resident (45 credits) | $36,015 | $37,860”
  - column:Ecampus (24 credits): 8784 ⟵ “Ecampus (24 credits) | $8,784 | $9,216”
  - column:Matriculated prior to July 2021: 100 ⟵ “Matriculated prior to July 2021 | 100 | 252 | 11,640 | 100 | 264 | 12,180 | 540 | 4.64%”
  - column:Matriculated 2021-22: 100 ⟵ “Matriculated 2021-22 | 100 | 256 | 11,820 | 100 | 268 | 12,360 | 540 | 4.57%”
  - column:Matriculated 2022-23: 100 ⟵ “Matriculated 2022-23 | 100 | 258 | 11,910 | 100 | 270 | 12,450 | 540 | 4.53%”
  - column:Matriculated 2023-24: 100 ⟵ “Matriculated 2023-24 | 100 | 260 | 12,000 | 100 | 272 | 12,540 | 540 | 4.50%”
  - column:Matriculated 2024-25: 100 ⟵ “Matriculated 2024-25 | 100 | 261 | 12,045 | 100 | 274 | 12,630 | 585 | 5.25%”
  - column:Matriculated 2025-26: 100 ⟵ “Matriculated 2025-26 | 100 | 100 | 275 | 12,675 | 630 | 5.23%”
  - column:Matriculated prior to July 2021 (2): 100 ⟵ “Matriculated prior to July 2021 | 100 | 248 | 11,460 | 100 | 260 | 12,000 | 540 | 4.71%”
  - column:Matriculated 2021-22 (2): 100 ⟵ “Matriculated 2021-22 | 100 | 252 | 11,640 | 100 | 264 | 12,180 | 540 | 4.64%”
  - column:Matriculated 2022-23 (2): 100 ⟵ “Matriculated 2022-23 | 100 | 258 | 11,910 | 100 | 270 | 12,450 | 540 | 4.53%”
  - column:Matriculated 2023-24 (2): 100 ⟵ “Matriculated 2023-24 | 100 | 260 | 12,000 | 100 | 272 | 12,540 | 540 | 4.50%”
  - column:Matriculated 2024-25 (2): 100 ⟵ “Matriculated 2024-25 | 100 | 261 | 12,045 | 100 | 274 | 12,630 | 585 | 5.25%”
  - column:Matriculated 2025-26 (2): 100 ⟵ “Matriculated 2025-26 | 100 | 100 | 275 | 12,675 | 630 | 5.23%”
  - column:Matriculated prior to July 2021 (3): 335 ⟵ “Matriculated prior to July 2021 | 335 | 751 | 34,800 | 335 | 787 | 36,420 | 1,620 | 4.66%”
  - column:Matriculated 2021-22 (3): 335 ⟵ “Matriculated 2021-22 | 335 | 763 | 35,340 | 335 | 800 | 37,005 | 1,665 | 4.71%”
  - … 291 more rows
### `1cd2470f48ba727f` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/satisfactory_academic_progress (sha256 9037ea986d39)
- issues: semantic_review_required, conflicting_sources:https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/scholarship-recipient-info,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/aidscholarships.pdf,https://financialaid.uoregon.edu/appeals,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “You are allowed to submit an appeal if you have mitigating circumstances, such as: a death of a relative, an injury or illness, or other special circumstances.”
### `38fef162f50780f3` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/appeals (sha256 11ab37ba5207)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uoregon.edu/satisfactory_academic_progress
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Information and the appeal process regarding failure to meet Satisfactory Academic Progress standards can be found on this webpage.”
### `3dce89032240dbfc` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/aidscholarships/aidscholarships.pdf (sha256 9da9eea88e9d)
- issues: semantic_review_required, conflicting_sources:https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/scholarship-recipient-info,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Monthly payments are • experiencing financial difficulties, such as medical expenses or capped at a percentage of the borrower’s discretionary income, change in income which is based on family size and income rather than total amount borrowed.”
### `420576c6ddac598a` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/ (sha256 0dfdaf9eecd3)
- issues: semantic_review_required, conflicting_sources:https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/scholarship-recipient-info,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/aidscholarships.pdf,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Our evaluation of transfer applications is largely focused on determining if students meet our minimum admission requirements through cumulative GPA and coursework, though we also consider additional factors including special circumstances statements, application materials, grade trends, and academic potential for success.”
  - sentence: need_based_special_circumstances ⟵ “For applicants who do not meet our minimum requirements, we ask that you provide a personal statement (either included in the Special Circumstances portion of your application or uploaded in your UO application status portal) to share how/why you do not meet this requirement, and we will consider this information as part of our evaluation.”
  - sentence: need_based_special_circumstances ⟵ “We encourage transfers to share any relevant information or context if your academic performance was affected by special circumstances like serious illness or documented disability, or to otherwise provide us with information that we would not otherwise gather from your application materials.”
### `6845cd6a0f5edcb9` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/scholarship-recipient-info (sha256 b2191f6a63ce)
- issues: semantic_review_required, conflicting_sources:https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/aidscholarships.pdf,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Off-Cycle Disbursement Requests Students may request alternative disbursement schedules (for example, lump-sum payments or term-specific awards) under special circumstances such as early graduation (for example, graduating in winter instead of spring) or study abroad programs.”
### `915675f8ebebe645` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/satisfactory_academic_progress (sha256 9037ea986d39)
- issues: semantic_review_required, conflicting_sources:https://financialaid.uoregon.edu/appeals
- checks: {"negative_sentences": 0, "sentences": 6}
  - sentence: sap_appeal ⟵ “Petitions to cancel disqualification and to be reinstated academically to the University are completely separate processes from a SAP appeal.”
  - sentence: sap_appeal ⟵ “If your disqualification is cancelled or if you are reinstated academically and not meeting SAP requirements, you will still need to separately complete a SAP appeal for consideration of reinstating your financial aid.”
  - sentence: sap_appeal ⟵ “Additionally, we are unable to retroactively review a SAP appeal once a term is complete.”
  - sentence: sap_appeal ⟵ “Appeal Process If you are not making satisfactory academic progress, you will receive a notification at your UO e-mail address.”
  - sentence: sap_appeal ⟵ “We recommend submitting your SAP appeal as soon as possible, preferably well before the term begins; in order to give us time to review, process, and notify you of the decision.”
  - sentence: sap_appeal ⟵ “We are unable to retroactively review a SAP appeal once a term is complete.”
### `956853d7e84363e8` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/ (sha256 552ce700adc2)
- issues: semantic_review_required, conflicting_sources:https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/scholarship-recipient-info,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/aidscholarships.pdf,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Personal statements and letters of recommendation (optional): You may send a personal statement with your application to explain special circumstances in your life that have affected you or your education.”
### `be498cd02b5eff09` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/appeals (sha256 11ab37ba5207)
- issues: semantic_review_required, conflicting_sources:https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/scholarship-recipient-info,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/aidscholarships.pdf,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “In cases that impact federal student aid, HEA Sec. 479(a) authorizes the financial aid administrator to make adjustments on a case-by-case basis to the cost of attendance or the values of the data items required to calculate the student aid index to allow for treatment of special circumstances of an individual eligible applicant.”
### `eae441e970fc60b7` University of Oregon — appeals 2026-27 [new] (labeled_in_source)
- source: https://catalog.uoregon.edu/admissiontograduation/aidscholarships/ (sha256 96f1781a11eb)
- issues: semantic_review_required, conflicting_sources:https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/scholarship-recipient-info,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/aidscholarships.pdf,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Forbearance may be granted for up to 12 months for reasons such as: experiencing financial difficulties, such as medical expenses or change in income serving in AmeriCorps performing service that would qualify for partial loan forgiveness through the Department of Defense working in a medical or dental internship or residency program having student loan payments that are high in relation to your i”
### `f905f054afc8776a` University of Oregon — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/ (sha256 59d036105c34)
- issues: semantic_review_required, conflicting_sources:https://business.uoregon.edu/programs/undergraduate/apply/scholarships-funding/scholarship-recipient-info,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/,https://catalog.uoregon.edu/admissiontograduation/aidscholarships/aidscholarships.pdf,https://financialaid.uoregon.edu/appeals,https://financialaid.uoregon.edu/satisfactory_academic_progress,https://www.uoregon.edu/admissions/undergraduate/find-your-path/international/international-transfer-applicant/,https://www.uoregon.edu/admissions/undergraduate/find-your-path/transfer-students/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: need_based_special_circumstances ⟵ “Our evaluation of transfer applications is largely focused on determining if students meet our minimum admission requirements through cumulative GPA and coursework, though we also consider additional factors including special circumstances statements, application materials, grade trends, and academic potential for success.”
  - sentence: need_based_special_circumstances ⟵ “For applicants who do not meet our minimum requirements, we ask that you provide a personal statement (either included in the Special Circumstances portion of your application or uploaded in your UO application status portal) to share how/why you do not meet this requirement, and we will consider this information as part of our evaluation.”
  - sentence: need_based_special_circumstances ⟵ “We encourage transfers to share any relevant information or context if your academic performance was affected by special circumstances like serious illness or documented disability, or to otherwise provide us with information that we would not otherwise gather from your application materials.”
### `0ac450909070bda9` University of Oregon — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/cost_of_attendance_law (sha256 5dc1bc065f5c)
- issues: conflicting_sources:https://financialaid.uoregon.edu/cost_of_attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and FeesBased on full-time enrollment for two semesters: 50076 ⟵ “Tuition and FeesBased on full-time enrollment for two semesters | $50,076 | $62,330”
  - column:Living Expenses (Housing and Food)Monthly costs: housing $1,400; food $518: 17262 ⟵ “Living Expenses (Housing and Food)Monthly costs: housing $1,400; food $518 | $17,262 | $17,262”
  - column:Books, Course Materials, Supplies, and Equipment: 1434 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,434 | $1,434”
  - column:Miscellaneous Personal Expenses: 2674 ⟵ “Miscellaneous Personal Expenses | $2,674 | $2,674”
  - column:Transportation: 470 ⟵ “Transportation | $470 | $1,500”
  - column:Estimated Total: 71916 ⟵ “Estimated Total | $71,916 | $85,200”
### `1244305fc69f6a4b` University of Oregon — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/cost_of_attendance_law (sha256 5dc1bc065f5c)
- issues: conflicting_sources:https://financialaid.uoregon.edu/cost_of_attendance
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and FeesBased on full-time enrollment for two semesters: 62330 ⟵ “Tuition and FeesBased on full-time enrollment for two semesters | $50,076 | $62,330”
  - column:Living Expenses (Housing and Food)Monthly costs: housing $1,400; food $518: 17262 ⟵ “Living Expenses (Housing and Food)Monthly costs: housing $1,400; food $518 | $17,262 | $17,262”
  - column:Books, Course Materials, Supplies, and Equipment: 1434 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,434 | $1,434”
  - column:Miscellaneous Personal Expenses: 2674 ⟵ “Miscellaneous Personal Expenses | $2,674 | $2,674”
  - column:Transportation: 1500 ⟵ “Transportation | $470 | $1,500”
  - column:Estimated Total: 85200 ⟵ “Estimated Total | $71,916 | $85,200”
### `7dda75f91247f413` University of Oregon — costs 2025-26 · residency=out_of_state [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/cost_of_attendance_law_2526 (sha256 4834ed389e75)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and FeesBased on full-time enrollment for two semesters: 62237 ⟵ “Tuition and FeesBased on full-time enrollment for two semesters | $49,982 | $62,237”
  - column:Living Expenses (Housing and Food)Monthly costs: housing $1,360; food $444: 16242 ⟵ “Living Expenses (Housing and Food)Monthly costs: housing $1,360; food $444 | $16,242 | $16,242”
  - column:Books, Course Materials, Supplies, and Equipment: 1396 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,396 | $1,396”
  - column:Miscellaneous Personal Expenses: 2600 ⟵ “Miscellaneous Personal Expenses | $2,600 | $2,600”
  - column:Transportation: 1458 ⟵ “Transportation | $456 | $1,458”
  - column:Estimated Total: 83933 ⟵ “Estimated Total | $70,676 | $83,933”
### `a32b68fad2e402bf` University of Oregon — costs 2025-26 · residency=in_state [new] (labeled_in_source)
- source: https://financialaid.uoregon.edu/cost_of_attendance_law_2526 (sha256 4834ed389e75)
- issues: stale_year_label:2025-26
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition and FeesBased on full-time enrollment for two semesters: 49982 ⟵ “Tuition and FeesBased on full-time enrollment for two semesters | $49,982 | $62,237”
  - column:Living Expenses (Housing and Food)Monthly costs: housing $1,360; food $444: 16242 ⟵ “Living Expenses (Housing and Food)Monthly costs: housing $1,360; food $444 | $16,242 | $16,242”
  - column:Books, Course Materials, Supplies, and Equipment: 1396 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,396 | $1,396”
  - column:Miscellaneous Personal Expenses: 2600 ⟵ “Miscellaneous Personal Expenses | $2,600 | $2,600”
  - column:Transportation: 456 ⟵ “Transportation | $456 | $1,458”
  - column:Estimated Total: 70676 ⟵ “Estimated Total | $70,676 | $83,933”
### `bda8618d0d9b2ccd` University of Oregon — costs 2026-27 · residency=out_of_state [new] (source_unlabeled)
- source: https://financialaid.uoregon.edu/cost_of_attendance (sha256 3d288400df98)
- issues: ambiguous_year_labels, conflicting_sources:https://financialaid.uoregon.edu/cost_of_attendance_law
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees*: 47466 ⟵ “Tuition and Fees* | $47,466”
  - column:Living Expenses (On-Campus Housing and Food)**: 18183 ⟵ “Living Expenses (On-Campus Housing and Food)** | $18,183”
  - column:UO Costs Total: 65649 ⟵ “UO Costs Total | $65,649”
  - column:Books, Course Materials, Supplies, and Equipment: 1434 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,434”
  - column:Miscellaneous Personal Expenses: 2673 ⟵ “Miscellaneous Personal Expenses | $2,673”
  - column:Transportation: 1500 ⟵ “Transportation | $1,500”
  - column:Total Cost: 71256 ⟵ “Total Cost | $71,256”
### `befdee492c2191d4` University of Oregon — costs 2026-27 · residency=in_state [new] (source_unlabeled)
- source: https://financialaid.uoregon.edu/cost_of_attendance (sha256 3d288400df98)
- issues: ambiguous_year_labels, conflicting_sources:https://financialaid.uoregon.edu/cost_of_attendance_law
- checks: {"columns": 1, "components_reconcile": true, "rows": 7}
  - column:Tuition and Fees*: 17475 ⟵ “Tuition and Fees* | $17,475”
  - column:Living Expenses (On-Campus Housing and Food)**: 18183 ⟵ “Living Expenses (On-Campus Housing and Food)** | $18,183”
  - column:UO Costs Total: 35658 ⟵ “UO Costs Total | $35,658”
  - column:Books, Course Materials, Supplies, and Equipment: 1434 ⟵ “Books, Course Materials, Supplies, and Equipment | $1,434”
  - column:Miscellaneous Personal Expenses: 2673 ⟵ “Miscellaneous Personal Expenses | $2,673”
  - column:Transportation: 471 ⟵ “Transportation | $471”
  - column:Total Cost: 40236 ⟵ “Total Cost | $40,236”

## Re-verification of existing records (50)

- source_not_fetched: data/institutions/bushnell/credit_policies/2026-27.json ["credit_policies", "ipeds-209409", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/cocc/credit_policies/2026-27.json ["credit_policies", "ipeds-208318", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/cocc/credit_policies/2026-27.json ["credit_policies", "ipeds-208318", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/eou/degree_requirements/2026-27.json ["degree_requirements", "ipeds-208646", null, "2026-27", {"program_key": "fire-services-administration-major", "requirement_key": "fire-services-administration-typical-four-year-curriculum"}]
- source_not_fetched: data/institutions/oregoncoastcc/credit_policies/2026-27.json ["credit_policies", "ipeds-423652", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/oit/awards/2026-27.json ["awards", "ipeds-209506", null, "2026-27", {"award_name": "Engineering Honors Scholarship"}]
- nothing_to_check: data/institutions/oregonstate/awards/2026-27.json ["awards", "ipeds-209542", null, "2026-27", {"award_name": "College of Engineering Undergraduate Scholarships"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "agricultural-sciences-undergraduate-major-bs-hbs", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "agricultural-and-natural-resources-communication-undergraduate-major-ba-hba-bs-h", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "american-studies-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "anthropology-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "applied-humanities-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "art-undergraduate-major-ba-bfa-bs-hba-hbfa-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "art-undergraduate-major-ba-bfa-bs-hba-hbfa-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "arts-media-and-technology-undergraduate-major-ba-bfa-bs-hba-hbfa-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "arts-media-and-technology-undergraduate-major-ba-bfa-bs-hba-hbfa-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "chemistry-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science-track-one"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "chemistry-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science-track-two"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "communication-studies-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "contemporary-music-industry-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "digital-communication-arts-undergraduate-major-ba-bfa-bs-hba-hbfa-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "digital-communication-arts-undergraduate-major-ba-bfa-bs-hba-hbfa-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "early-childhood-leadership-policy-and-practice-undergraduate-major-ba-hba-bs-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "economics-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "elementary-education-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "ethnic-studies-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "german-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "history-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "hospitality-management-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "human-development-and-family-sciences-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "marine-studies-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "music-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "philosophy-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "physics-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "political-science-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "religious-studies-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "secondary-education-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "social-science-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "sociology-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "theatre-arts-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-science"}]
- source_not_fetched: data/institutions/oregonstate/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209542", null, "2026-27", {"program_key": "women-gender-and-sexuality-studies-undergraduate-major-ba-bs-hba-hbs", "requirement_key": "bachelor-of-arts"}]
- source_not_fetched: data/institutions/pdx/credit_policies/2026-27.json ["credit_policies", "ipeds-209807", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/pdx/credit_policies/2026-27.json ["credit_policies", "ipeds-209807", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/pdx/credit_policies/2026-27.json ["credit_policies", "ipeds-209807", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/pdx/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209807", null, "2026-27", {"program_key": "mechanical-engineering-b-s", "requirement_key": "recommended-sequence"}]
- nothing_to_check: data/institutions/uoregon/awards/2026-27.json ["awards", "ipeds-209551", null, "2026-27", {"award_name": "Lundquist College Scholarships"}]
- source_not_fetched: data/institutions/uoregon/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209551", null, "2026-27", {"program_key": "german-ba-bs", "requirement_key": "bachelor-of-arts-in-german-scandinavian-focus"}]
- source_not_fetched: data/institutions/uoregon/degree_requirements/2026-27.json ["degree_requirements", "ipeds-209551", null, "2026-27", {"program_key": "marine-biology-ba-bs", "requirement_key": "bachelor-of-arts-in-marine-biology"}]
- source_not_fetched: data/institutions/up/credit_policies/2026-27.json ["credit_policies", "ipeds-209825", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/up/credit_policies/2026-27.json ["credit_policies", "ipeds-209825", null, "2026-27", {"policy_kind": "IB"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Oregon State University: cost_of_attendance, admissions_tests, ap_credit, transfer_credit, residency
- University of Oregon: admissions_tests, ap_credit, ib_credit, dual_enrollment, transfer_credit, residency
