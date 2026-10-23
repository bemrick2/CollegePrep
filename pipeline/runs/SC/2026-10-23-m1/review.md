# Review queue — SC (2026-27)

Pages fetched: 180; failures: 4. Candidates: 19 (1 without issues, 18 exceptions). Re-verification upgrades proposed: 0.

## Coverage by category

| category | verified_current | partially_verified_current | candidate_ready | candidate_exception | source_found | not_found | fetch_failed |
|---|---|---|---|---|---|---|---|
| tuition_fees | 8 | 0 | 0 | 2 | 0 | 0 | 46 |
| cost_of_attendance | 2 | 0 | 0 | 1 | 1 | 0 | 52 |
| admissions_tests | 0 | 0 | 0 | 0 | 2 | 0 | 54 |
| common_data_set | 0 | 0 | 0 | 0 | 0 | 2 | 54 |
| merit_scholarships | 2 | 1 | 0 | 0 | 2 | 0 | 51 |
| ap_credit | 0 | 3 | 0 | 2 | 0 | 0 | 51 |
| clep_credit | 1 | 5 | 0 | 0 | 1 | 1 | 48 |
| ib_credit | 0 | 2 | 0 | 2 | 0 | 0 | 52 |
| dual_enrollment | 2 | 9 | 0 | 0 | 2 | 0 | 43 |
| transfer_credit | 0 | 10 | 0 | 1 | 0 | 0 | 45 |
| statewide_articulation | 0 | 0 | 0 | 0 | 1 | 1 | 54 |
| residency | 0 | 0 | 0 | 0 | 2 | 0 | 54 |
| degree_requirements | 2 | 0 | 0 | 0 | 1 | 0 | 53 |
| aid_appeals | 0 | 0 | 0 | 2 | 0 | 0 | 54 |

## Ready for review (1)

### `fc056b95690404f5` Clemson University — transfer_policies 2026-27 [same] (source_unlabeled)
- source: https://www.clemson.edu/admissions/undergraduate-admissions/apply/course-transfer-information.html (sha256 bba4e2720381)
- checks: {"fields": ["min_grade"]}
  - min_grade: C ⟵ “Clemson accepts courses for transfer only if earned with a grade of C or better.”

## Exceptions (18)

### `0ba6309f1f38ac27` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/maintain-your-eligibility/ (sha256 00ed55a2df35)
- issues: semantic_review_required, conflicting_sources:https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html
- checks: {"negative_sentences": 0, "sentences": 2}
  - sentence: sap_appeal ⟵ “MCGPR Needed by Credit Hour | Total Attempted Credit Hours | MCGPR | 89 or less | 1.85 | 90+ | 2.00 | Graduate Students | 3.00 Undergraduate Resources for Satisfactory Academic Progress Graduate Resources for Satisfactory Academic Progress Appeal Your SAP Status If you are not maintaining SAP, you can appeal your status using the appeal form and instructions.”
  - sentence: sap_appeal ⟵ “SAP APPEAL PRIORITY DEADLINES Fall Term: July 30 Spring Term: November 30 Summer Term: April 30 To be considered, your appeal must explain why you failed to make SAP and what has changed that will allow you to meet SAP standards at the next evaluation.”
### `48daffbd86c3340b` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html (sha256 a34e164dbc4c)
- issues: semantic_review_required, conflicting_sources:https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/maintain-your-eligibility/
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: sap_appeal ⟵ “Need-Based Appeal Form Satisfactory Academic Progress Appeals If you have received notice that you are ineligible for financial aid because of a failure to maintain Satisfactory Academic Progress, you can submit an appeal to the Financial Aid Appeals Committee.”
  - sentence: sap_appeal ⟵ “To appeal, you must submit the Satisfactory Academic Progress Appeal Form, a detailed letter documenting the extenuating circumstances for why the deficiency has occurred, actions you have taken to resolve the issue and any supporting documentation.”
  - sentence: sap_appeal ⟵ “Satisfactory Academic Progress Appeal Form Scholarship Appeals Clemson University Scholarship Appeals To appeal the loss of a University scholarship, you must submit the scholarship appeal form, letter and supporting documents to the Office of Scholarships.”
### `51ff6c0657edf069` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html (sha256 a34e164dbc4c)
- issues: semantic_review_required
- checks: {"negative_sentences": 0, "sentences": 3}
  - sentence: scholarship_retention_appeal ⟵ “As part of the appeal, you must clearly document the reasons beyond your control that contributed to not meeting the renewal requirements of your scholarship(s). **University scholarship appeals are reviewed during the Fall semester each academic year.”
  - sentence: scholarship_retention_appeal ⟵ “The scholarship appeal form and supporting documents must be submitted by the last day to register or add a class.”
  - sentence: scholarship_retention_appeal ⟵ “University Scholarship Appeal Form State of South Carolina Scholarship Appeals To appeal the loss of a state scholarship (Palmetto Fellows or LIFE), you must appeal directly to the South Carolina Commission on Higher Education (CHE) as Clemson University does not have the authority to make exceptions to state legislation and/or regulations.”
### `7bc14dc0900bc31b` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html (sha256 a34e164dbc4c)
- issues: semantic_review_required, conflicting_sources:https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/maintain-your-eligibility/
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “If you have extenuating circumstances or a significant change in financial status since you filed the FAFSA, you can submit the need-based appeal form to the financial aid office and request a review.”
### `b8e838bf636efe2f` Clemson University — appeals 2026-27 [new] (source_unlabeled)
- source: https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/maintain-your-eligibility/ (sha256 00ed55a2df35)
- issues: semantic_review_required, conflicting_sources:https://www.clemson.edu/financial-aid/how-aid-works/specific-aid-tasks/submit-an-appeal.html
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: need_based_special_circumstances ⟵ “Appeals can be filed based on academic improvement, death of a family member/close friend, injury or illness of the student, or other special circumstances.”
### `9d3d4e84903adaec` Clemson University — costs 2026-27 · residency=out_of_state [new] (labeled_in_source)
- source: https://www.clemson.edu/financial-aid/cost/estimated-cost-of-attendance.html (sha256 60008c193581)
- issues: arrangement_unlabeled, multiple_total_rows
- checks: {"columns": 2, "rows": 10}
  - column:Tuition: 42020 ⟵ “Tuition | $42,020 | $42,020”
  - column:Fees(2): 1832 ⟵ “Fees(2) | $1,832 | $1,832”
  - column:Books, Supplies & Course Materials(6): 1576 ⟵ “Books, Supplies & Course Materials(6) | $1,576 | $1,576”
  - column:Housing(3): 9304 ⟵ “Housing(3) | $9,304 | $2,023”
  - column:Food(4): 5576 ⟵ “Food(4) | $5,576 | $2,023”
  - column:Transportation: 1320 ⟵ “Transportation | $1,320 | $3,672”
  - column:Personal: 4484 ⟵ “Personal | $4,484 | $4,484”
  - column:Loan Fees(5): 68 ⟵ “Loan Fees(5) | $68 | $68”
  - column:TOTAL: 66180 ⟵ “TOTAL | $66,180 | $57,698”
  - column:Total with laptop(6): 68704 ⟵ “Total with laptop(6) | $68,704 | $60,222”
  - with_parents_or_family:Tuition: 42020 ⟵ “Tuition | $42,020 | $42,020”
  - with_parents_or_family:Fees(2): 1832 ⟵ “Fees(2) | $1,832 | $1,832”
  - with_parents_or_family:Books, Supplies & Course Materials(6): 1576 ⟵ “Books, Supplies & Course Materials(6) | $1,576 | $1,576”
  - with_parents_or_family:Housing(3): 2023 ⟵ “Housing(3) | $9,304 | $2,023”
  - with_parents_or_family:Food(4): 2023 ⟵ “Food(4) | $5,576 | $2,023”
  - with_parents_or_family:Transportation: 3672 ⟵ “Transportation | $1,320 | $3,672”
  - with_parents_or_family:Personal: 4484 ⟵ “Personal | $4,484 | $4,484”
  - with_parents_or_family:Loan Fees(5): 68 ⟵ “Loan Fees(5) | $68 | $68”
  - with_parents_or_family:TOTAL: 57698 ⟵ “TOTAL | $66,180 | $57,698”
  - with_parents_or_family:Total with laptop(6): 60222 ⟵ “Total with laptop(6) | $68,704 | $60,222”
### `b94f119795680548` Clemson University — costs 2026-27 · residency=in_state [new] (labeled_in_source)
- source: https://www.clemson.edu/financial-aid/cost/estimated-cost-of-attendance.html (sha256 60008c193581)
- issues: arrangement_unlabeled, multiple_total_rows
- checks: {"columns": 2, "rows": 10}
  - column:Tuition: 14038 ⟵ “Tuition | $14,038 | $14,038”
  - column:Fees(2): 1832 ⟵ “Fees(2) | $1,832 | $1,832”
  - column:Books, Supplies & Course Materials(6): 1576 ⟵ “Books, Supplies & Course Materials(6) | $1,576 | $1,576”
  - column:Housing(3): 9304 ⟵ “Housing(3) | $9,304 | $2,023”
  - column:Food(4): 5576 ⟵ “Food(4) | $5,576 | $2,023”
  - column:Transportation: 1320 ⟵ “Transportation | $1,320 | $3,672”
  - column:Personal: 4484 ⟵ “Personal | $4,484 | $4,484”
  - column:Loan Fees(5): 68 ⟵ “Loan Fees(5) | $68 | $68”
  - column:TOTAL: 38198 ⟵ “TOTAL | $38,198 | $29,716”
  - column:Total with laptop(6): 40722 ⟵ “Total with laptop(6) | $40,722 | $32,240”
  - with_parents_or_family:Tuition: 14038 ⟵ “Tuition | $14,038 | $14,038”
  - with_parents_or_family:Fees(2): 1832 ⟵ “Fees(2) | $1,832 | $1,832”
  - with_parents_or_family:Books, Supplies & Course Materials(6): 1576 ⟵ “Books, Supplies & Course Materials(6) | $1,576 | $1,576”
  - with_parents_or_family:Housing(3): 2023 ⟵ “Housing(3) | $9,304 | $2,023”
  - with_parents_or_family:Food(4): 2023 ⟵ “Food(4) | $5,576 | $2,023”
  - with_parents_or_family:Transportation: 3672 ⟵ “Transportation | $1,320 | $3,672”
  - with_parents_or_family:Personal: 4484 ⟵ “Personal | $4,484 | $4,484”
  - with_parents_or_family:Loan Fees(5): 68 ⟵ “Loan Fees(5) | $68 | $68”
  - with_parents_or_family:TOTAL: 29716 ⟵ “TOTAL | $38,198 | $29,716”
  - with_parents_or_family:Total with laptop(6): 32240 ⟵ “Total with laptop(6) | $40,722 | $32,240”
### `08316ff8d9ac3b81` Clemson University — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://www.clemson.edu/admissions/undergraduate-admissions/apply/credit-transfer.html (sha256 dbe6745af490)
- issues: score_column_not_scores
- checks: {"distinct_exams": 18, "equivalencies": 18, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | 4 | BIOL 1200/1230 | 4”
  - equivalencies[IB-BUSINESS-MANAGEMENT|Business and Management]:  ⟵ “Business and Management | 4, 5, 6, 7 | MGT 2010 | 3”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | 4, 5, 6, 7 | CH 1010 (for majors requiring organic chemistry) | 4”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | 4 | CPSC 1110 | 3”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | 4, 5, 6, 7 | ECON 2110, 2120 | 6”
  - equivalencies[IB-FILM|Film]:  ⟵ “Film | 4, 5, 6, 7 | ELEC 00014 | 3”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | 4, 5, 6, 7 | GEOG 1010 | 3”
  - equivalencies[IB-GLOBAL-POLITICS|Global Politics]:  ⟵ “Global Politics | 4, 5, 6, 7 | ELEC 00014 | 3”
  - equivalencies[IB-HISTORY|Islamic History]:  ⟵ “Islamic History | 4, 5, 6, 7 | ELEC | 3”
  - equivalencies[IB-MATHEMATICS-ANALYSIS-APPROACHES|Mathematics: Analysis and Approaches]:  ⟵ “Mathematics: Analysis and Approaches | 4, 5 | MATH 1020 or 10601 | 3 or 4”
  - equivalencies[IB-MATHEMATICS-APPLICATIONS-INTERPRETATION|Mathematics: Applications and Interpretation]:  ⟵ “Mathematics: Applications and Interpretation | 4, 5 | MATH 19997 | 3”
  - equivalencies[IB-MUSIC|Music]:  ⟵ “Music | 4, 5, 6, 7 | ELEC 00013 | 3”
  - equivalencies[IB-PHILOSOPHY|Philosophy]:  ⟵ “Philosophy | 4, 5, 6, 7 | PHIL 1010 | 3”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | 4 | PHYS 2070/2090 | 4”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | 4, 5, 6, 7 | PSYC 2010 | 3”
  - equivalencies[IB-SOCIAL-CULTURAL-ANTHROPOLOGY|Social and Cultural Anthropology]:  ⟵ “Social and Cultural Anthropology | 4, 5, 6, 7 | ANTH 1999 | 3”
  - equivalencies[IB-THEATRE|Theater Arts]:  ⟵ “Theater Arts | 4, 5, 6, 7 | ELEC 00013 | 3”
  - equivalencies[IB-VISUAL-ARTS|Visual Arts]:  ⟵ “Visual Arts | 4, 5, 6, 7 | ART 1030 | 3”
### `acdb627b3953931f` Clemson University — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://www.clemson.edu/admissions/undergraduate-admissions/apply/credit-transfer.html (sha256 dbe6745af490)
- issues: rows_without_score
- checks: {"distinct_exams": 36, "equivalencies": 37, "rows_without_score": 37}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|None]:  ⟵ “African American Studies | African American Studies | 3, 4, 5 | GBS 1000 | 3”
  - equivalencies[AP-RESEARCH|None]:  ⟵ “Capstone | Research | 3, 4, 5 | ELEC 00013 | 3”
  - equivalencies[AP-SEMINAR|None]:  ⟵ “ | Seminar | 3, 4, 5 | ELEC 00013 | 3”
  - equivalencies[AP-MICROECONOMICS|None]:  ⟵ “Economics | Microeconomics | 3, 4, 5 | ECON 2110 | 3”
  - equivalencies[AP-MACROECONOMICS|None]:  ⟵ “ | Macroeconomics | 3, 4, 5 | ECON 2120 | 3”
  - equivalencies[AP-HUMAN-GEOGRAPHY|None]:  ⟵ “Geography | Human Geography | 3, 4, 5 | GEOG 1010 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “History | United States History | 3 | HIST 1010 | 3”
  - equivalencies[AP-UNITED-STATES-HISTORY|None]:  ⟵ “ | United States History | 4, 5 | HIST 1010, 1020 | 6”
  - equivalencies[AP-EUROPEAN-HISTORY|None]:  ⟵ “ | European History | 3, 4, 5 | HIST 1730 | 3”
  - equivalencies[AP-WORLD-HISTORY-MODERN|None]:  ⟵ “ | World History | 3, 4, 5 | HIST 19995 | 3”
  - equivalencies[AP-MUSIC-THEORY|None]:  ⟵ “Humanities | Music Theory | 3, 4, 5 | MUSC 1420, 1430 | 4”
  - equivalencies[AP-ART-HISTORY|None]:  ⟵ “ | Art History | 3, 4, 5 | ART 2100 | 3”
  - equivalencies[AP-DRAWING|None]:  ⟵ “ | Studio Art — Drawing | 3 | ELEC 00013 | 3”
  - equivalencies[AP-2-D-ART-DESIGN|None]:  ⟵ “ | Studio Art — 2D Design | 3 | ELEC 00013 | 3”
  - equivalencies[AP-3-D-ART-DESIGN|None]:  ⟵ “ | Studio Art — 3D Design | 3 | ELEC 00013 | 3”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|None]:  ⟵ “Languages | Chinese Language and Culture | 3, 4 | CHIN 1010, 1020, 2010 | 11”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|None]:  ⟵ “ | French Language and Culture | 3, 4, 5 | FR 1010, 1020 | 8”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|None]:  ⟵ “ | German Language and Culture | 3, 4, 5 | GER 1010, 1020 | 8”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|None]:  ⟵ “ | Italian Language and Culture | 3, 4 | ITAL 1010, 1020, 2010 | 11”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|None]:  ⟵ “ | Japanese Language and Culture | 3, 4 | JAPN 1010, 1020, 2010 | 11”
  - equivalencies[AP-LATIN|None]:  ⟵ “ | Latin | 3 | LATN 1010, 1020, 2010 | 11”
  - equivalencies[AP-SPANISH-LANGUAGE-CULTURE|None]:  ⟵ “ | Spanish Language and Culture | 3, 4, 5 | SPAN 1010, 1020 | 8”
  - equivalencies[AP-SPANISH-LITERATURE-CULTURE|None]:  ⟵ “ | Spanish Literature and Culture | 3 | SPAN 1010, 1020 | 8”
  - equivalencies[AP-CALCULUS-AB|None]:  ⟵ “Math | Calculus AB | 3, 4, 5 | MATH 1060 | 4”
  - equivalencies[AP-CALCULUS-BC|None]:  ⟵ “ | Calculus BC | 3, 4, 5 | MATH 1060, 1080 | 8”
  - … 12 more rows
### `028b4730224050bc` University of South Carolina-Columbia — appeals 2026-27 [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php (sha256 f254ca2f42fe)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “You are welcome to complete our scholarship appeal form, and we will consider your request should additional funds become available.”
### `da3315013e197e3f` University of South Carolina-Columbia — appeals 2026-27 [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/scholarship_faqs/index.php
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: scholarship_retention_appeal ⟵ “Appeals will only be accepted electronically through the Scholarship Appeal Form that is accessible through Self Service Carolina.”
### `dc0915b4940f8da0` University of South Carolina-Columbia — appeals 2026-27 [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/financial_aid/scholarships/scholarship_policies/scholarship_appeals/index.php (sha256 e716ccd9ed74)
- issues: semantic_review_required, shared_site_attribution_review
- checks: {"negative_sentences": 0, "sentences": 1}
  - sentence: sap_appeal ⟵ “Please note that this is separate from any Satisfactory Academic Progress appeal that a student might have to complete for federal financial aid.”
### `492f056af1a9772b` University of South Carolina-Columbia — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php (sha256 f3a89e979fc3)
- issues: cost_period_semester, residency_unknown, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php,https://www.sc.edu/admissions-at-sc/tuition-aid/index.php
- checks: {"columns": 3, "components_reconcile": true, "rows": 9}
  - on_campus:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - on_campus:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - on_campus:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - on_campus:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - on_campus:Housing: 11432 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - on_campus:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - on_campus:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - on_campus:Transportation: 2670 ⟵ “Transportation | $2,670 | $2,690 | $2,690”
  - on_campus:Total: 66394 ⟵ “Total | $66,394 | $66,394 | $57,592”
  - off_campus_not_with_family:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - off_campus_not_with_family:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - off_campus_not_with_family:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - off_campus_not_with_family:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - off_campus_not_with_family:Housing: 11432 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - off_campus_not_with_family:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - off_campus_not_with_family:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - off_campus_not_with_family:Transportation: 2690 ⟵ “Transportation | $2,670 | $2,690 | $2,690”
  - off_campus_not_with_family:Total: 66394 ⟵ “Total | $66,394 | $66,394 | $57,592”
  - with_parents_or_family:Tuition: 38098 ⟵ “Tuition | $38,098 | $38,098 | $38,098”
  - with_parents_or_family:Tech Fee: 400 ⟵ “Tech Fee | $400 | $400 | $400”
  - with_parents_or_family:Books and Supplies: 1522 ⟵ “Books and Supplies | $1,522 | $1,522 | $1,522”
  - with_parents_or_family:Weighted Average Program Fees: 1580 ⟵ “Weighted Average Program Fees | $1,580 | $1,580 | $1,580”
  - with_parents_or_family:Housing: 2630 ⟵ “Housing | $11,432 | $11,432 | $2,630”
  - with_parents_or_family:Food: 5902 ⟵ “Food | $5,902 | $5,902 | $5,902”
  - with_parents_or_family:Personal: 4790 ⟵ “Personal | $4,790 | $4,790 | $4,790”
  - … 2 more rows
### `5ab4c4bdf813f802` University of South Carolina-Columbia — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php (sha256 8a2e3238170b)
- issues: residency_unknown, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php,https://www.sc.edu/admissions-at-sc/tuition-aid/index.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 12288 ⟵ “Tuition | $12,288”
  - column:Technology Fee: 400 ⟵ “Technology Fee | $400”
  - column:Weighted Average Program Fee: 1580 ⟵ “Weighted Average Program Fee | $1,580”
  - column:Housing: 11432 ⟵ “Housing | $11,432”
  - column:Food: 5902 ⟵ “Food | $5,902”
  - column:Total: 31602 ⟵ “Total | $31,602”
### `f2f722bf6cc50fbf` University of South Carolina-Columbia — costs 2026-27 · residency=not_applicable [new] (labeled_in_source)
- source: https://www.sc.edu/admissions-at-sc/tuition-aid/index.php (sha256 deafe1ac10ca)
- issues: residency_unknown, shared_site_attribution_review, conflicting_sources:https://sc.edu/about/offices_and_divisions/financial_aid/cost_and_aid/cost_to_attend/index.php,https://sc.edu/about/offices_and_divisions/undergraduate_admissions/tuition_scholarships/index.php
- checks: {"columns": 1, "components_reconcile": true, "rows": 6}
  - column:Tuition: 12288 ⟵ “Tuition | $12,288”
  - column:Technology Fee: 400 ⟵ “Technology Fee | $400”
  - column:Weighted Average Program Fee: 1580 ⟵ “Weighted Average Program Fee | $1,580”
  - column:Housing: 11432 ⟵ “Housing | $11,432”
  - column:Food: 5902 ⟵ “Food | $5,902”
  - column:Total: 31602 ⟵ “Total | $31,602”
### `3b42c2ec74323a94` University of South Carolina-Columbia — credit_policies 2026-27 · policy_kind=AP [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 870e3d737322)
- issues: shared_site_attribution_review
- checks: {"distinct_exams": 37, "equivalencies": 41, "rows_without_score": 0}
  - equivalencies[AP-AFRICAN-AMERICAN-STUDIES|3]:  ⟵ “African American Studies | 3 | AFAM 201 |  | ”
  - equivalencies[AP-UNITED-STATES-GOVERNMENT-POLITICS|3]:  ⟵ “American Government and Politics | 3 | POLI 201 |  | ”
  - equivalencies[AP-RESEARCH|3]:  ⟵ “AP Research Course | 3 | UNEL 002T |  | ”
  - equivalencies[AP-SEMINAR|3]:  ⟵ “AP Seminar Course | 3 | UELC 002T |  | ”
  - equivalencies[AP-ART-HISTORY|3]:  ⟵ “Art History | 3 | ARTE 101 | 4 | ARTH 105”
  - equivalencies[AP-2-D-ART-DESIGN|3]:  ⟵ “Art Studio, 2-D | 3 | ARTS 103 |  | ”
  - equivalencies[AP-3-D-ART-DESIGN|3]:  ⟵ “Art Studio, 3-D | 3 | ARTS 104 |  | ”
  - equivalencies[AP-DRAWING|3]:  ⟵ “Art Studio, Drawing | 3 | ARTS 111 |  | ”
  - equivalencies[AP-BIOLOGY|3]:  ⟵ “Biology | 3 | BIOL 101 and 101L | 4, 5 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[AP-CHEMISTRY|3]:  ⟵ “Chemistry | 3 | CHEM 111 and 111L | 4, 5 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[AP-CHINESE-LANGUAGE-CULTURE|3]:  ⟵ “Chinese | 3 | CHIN 121 | 4, 5 | CHIN 121 and 122”
  - equivalencies[AP-COMPARATIVE-GOVERNMENT-POLITICS|3]:  ⟵ “Comparative Government and Politics* | 3 | POLI 103C |  | ”
  - equivalencies[AP-COMPUTER-SCIENCE-PRINCIPLES|3, 4, 5]:  ⟵ “Computer Science Principles | 3, 4, 5 | CSCE 101 |  | ”
  - equivalencies[AP-MACROECONOMICS|3]:  ⟵ “Economics-Macro | 3 | ECON 222 |  | ”
  - equivalencies[AP-MICROECONOMICS|3]:  ⟵ “Economics-Micro | 3 | ECON 221 |  | ”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on either)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on either) | ENGL 101 | 5 (on either or both) | ENGL 101 and 102”
  - equivalencies[AP-ENGLISH-LANGUAGE-COMPOSITION|3 (on both)]:  ⟵ “English Language and Composition OREnglish Composition and Literature | 3 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[AP-ENVIRONMENTAL-SCIENCE|3]:  ⟵ “Environmental Science | 3 | ENVR 101 & ENVR 101L |  | ”
  - equivalencies[AP-EUROPEAN-HISTORY|3]:  ⟵ “European History | 3 | HIST 101 | 4, 5 | HIST 101 and 102”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on either)]:  ⟵ “French Language OR French Literature** | 3 (on either) | FREN 121 | 4, 5 (on either or both) | FREN 121 and 122”
  - equivalencies[AP-FRENCH-LANGUAGE-CULTURE|3 (on both)]:  ⟵ “French Language OR French Literature** | 3 (on both) | FREN 121 AND 122 |  | ”
  - equivalencies[AP-GERMAN-LANGUAGE-CULTURE|3]:  ⟵ “German** | 3 | GERM 121 | 4, 5 | GERM 121 and 122”
  - equivalencies[AP-HUMAN-GEOGRAPHY|3]:  ⟵ “Human Geography | 3 | GEOG 210 |  | ”
  - equivalencies[AP-ITALIAN-LANGUAGE-CULTURE|3]:  ⟵ “Italian | 3 | ITAL 121 | 4, 5 | ITAL 121 and 122”
  - equivalencies[AP-JAPANESE-LANGUAGE-CULTURE|3]:  ⟵ “Japanese | 3 | JAPA 121 | 4, 5 | JAPA 121 and 122”
  - … 16 more rows
### `66d60d7d35d2214d` University of South Carolina-Columbia — credit_policies 2026-27 · policy_kind=IB [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_freshmen/ap_ib_credits/index.php (sha256 870e3d737322)
- issues: score_column_not_scores, shared_site_attribution_review
- checks: {"distinct_exams": 23, "equivalencies": 39, "rows_without_score": 0}
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | E, D, C B, A | BIOL 101, 101L BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | E, D, C, B, A | CSE 101 and CSCE 001T”
  - equivalencies[IB-CHEMISTRY|Chemistry]:  ⟵ “Chemistry | E, D, C B, A | CHEM 111 and 111L CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|Economics]:  ⟵ “Economics | E, D C, B, A | ECON 221 ECON 221 and 222”
  - equivalencies[IB-GEOGRAPHY|Geography]:  ⟵ “Geography | E, D, C, B, A | GEOG 103”
  - equivalencies[IB-HISTORY|History: U.S.]:  ⟵ “History: U.S. | E, D, C, B, A | HIST 112”
  - equivalencies[IB-HISTORY|History: European]:  ⟵ “History: European | E, D, C, B, A | HIST 102”
  - equivalencies[IB-HISTORY|History: International]:  ⟵ “History: International | E, D, C, B, A | HIST 001T”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | E, D, C B, A | PHYS 211 and 211L PHYS 211, 211L, 212 and 212L”
  - equivalencies[IB-PSYCHOLOGY|Psychology]:  ⟵ “Psychology | E, D, C, B, A | PSYC 101”
  - equivalencies[IB-BIOLOGY|Biology]:  ⟵ “Biology | E, D, C, B, A | BIOL 101 and 101L”
  - equivalencies[IB-COMPUTER-SCIENCE|Computer Science]:  ⟵ “Computer Science | E, D, C, B, A | CSCE 101 and CSCE 001T”
  - equivalencies[IB-HISTORY|History: U.S./International/European]:  ⟵ “History: U.S./International/European | E, D, C, B, A | HUMA 001T”
  - equivalencies[IB-PHYSICS|Physics]:  ⟵ “Physics | E, D, C, B, A | PHYS 211 and 211L”
  - equivalencies[IB-BIOLOGY|4]:  ⟵ “Biology | 4 | BIOL 101 and 101L | 5, 6, 7 | BIOL 101, 101L, 102 and 102L”
  - equivalencies[IB-BUSINESS-MANAGEMENT|4]:  ⟵ “Business and Management | 4 | MGMT 371 | 5, 6, 7 | MGMT 371 and 376”
  - equivalencies[IB-CHEMISTRY|4]:  ⟵ “Chemistry | 4 | CHEM 111 and 111L | 5, 6, 7 | CHEM 111, 111L, 112 and 112L”
  - equivalencies[IB-ECONOMICS|4, 5]:  ⟵ “Economics | 4, 5 | ECON 221 | 6, 7 | ECON 221 and 222”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on either)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on either) | ENGL 101 | 5, 6, 7 (on either or both) | ENGL 101 and 102”
  - equivalencies[IB-ENGLISH-A-LANGUAGE-LITERATURE|4 (on both)]:  ⟵ “English A Literature OR English A Language and Literature* English B exams (NOT AWARDED FOR CREDIT) | 4 (on both) | ENGL 101 and 102 |  | ”
  - equivalencies[IB-FILM|4]:  ⟵ “Film | 4 | HUMA 002T |  | ”
  - equivalencies[IB-FRENCH|4, 5]:  ⟵ “French B* | 4, 5 | FREN 122 and 209 | 6, 7 | FREN 209 and 210”
  - equivalencies[IB-GEOGRAPHY|4]:  ⟵ “Geography | 4 | GEOG 103 |  | ”
  - equivalencies[IB-GERMAN|4, 5]:  ⟵ “German B* | 4, 5 | GERM 122 and 210 | 6, 7 | GERM 210 and 211”
  - equivalencies[IB-GLOBAL-POLITICS|4, 5, 6, 7]:  ⟵ “Global Politics | 4, 5, 6, 7 | POLI 101 |  | ”
  - … 14 more rows
### `096ff70b70f53208` University of South Carolina-Columbia — transfer_policies 2026-27 [new] (source_unlabeled)
- source: https://sc.edu/about/offices_and_divisions/undergraduate_admissions/apply/for_transfers/index.php (sha256 c0b11da65903)
- issues: shared_site_attribution_review
- checks: {"fields": ["min_grade"]}
  - min_grade: C- ⟵ “Transferring credits from other institutions USC generally accepts nonremedial coursework completed at regionally accredited institutions with a grade of C- or better.”

## Re-verification of existing records (45)

- source_not_fetched: data/institutions/andersonuniversity/credit_policies/2026-27.json ["credit_policies", "ipeds-217633", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/bju/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217749", null, "2026-27", {}]
- source_not_fetched: data/institutions/charlestonsouthern/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217688", null, "2026-27", {}]
- source_not_fetched: data/institutions/citadel/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217864", null, "2026-27", {}]
- source_not_fetched: data/institutions/claflin/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217873", null, "2026-27", {}]
- nothing_to_check: data/institutions/clemson/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217882", null, "2026-27", {}]
- source_not_fetched: data/institutions/coker/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217907", null, "2026-27", {}]
- source_not_fetched: data/institutions/ciu/credit_policies/2026-27.json ["credit_policies", "ipeds-217925", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ciu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217925", null, "2026-27", {}]
- source_not_fetched: data/institutions/denmarktech/transfer_policies/2026-27.json ["transfer_policies", "ipeds-217989", null, "2026-27", {}]
- source_not_fetched: data/institutions/fmarion/credit_policies/2026-27.json ["credit_policies", "ipeds-218061", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/hgtc/credit_policies/2026-27.json ["credit_policies", "ipeds-218140", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/hgtc/credit_policies/2026-27.json ["credit_policies", "ipeds-218140", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/hgtc/credit_policies/2026-27.json ["credit_policies", "ipeds-218140", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/lander/credit_policies/2026-27.json ["credit_policies", "ipeds-218229", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ngu/credit_policies/2026-27.json ["credit_policies", "ipeds-218441", null, "2026-27", {"policy_kind": "AP"}]
- source_not_fetched: data/institutions/ngu/credit_policies/2026-27.json ["credit_policies", "ipeds-218441", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/ngu/credit_policies/2026-27.json ["credit_policies", "ipeds-218441", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/ngu/transfer_policies/2026-27.json ["transfer_policies", "ipeds-218441", null, "2026-27", {}]
- source_not_fetched: data/institutions/presby/transfer_policies/2026-27.json ["transfer_policies", "ipeds-218539", null, "2026-27", {}]
- source_not_fetched: data/institutions/swu/awards/2026-27.json ["awards", "ipeds-217776", null, "2026-27", {"award_name": "Opportunity Scholarship"}]
- source_not_fetched: data/institutions/swu/awards/2026-27.json ["awards", "ipeds-217776", null, "2026-27", {"award_name": "Warrior Scholarship"}]
- source_not_fetched: data/institutions/swu/awards/2026-27.json ["awards", "ipeds-217776", null, "2026-27", {"award_name": "Trustee Scholarship"}]
- source_not_fetched: data/institutions/swu/awards/2026-27.json ["awards", "ipeds-217776", null, "2026-27", {"award_name": "Presidential Scholarship"}]
- source_not_fetched: data/institutions/swu/credit_policies/2026-27.json ["credit_policies", "ipeds-217776", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/usca/credit_policies/2026-27.json ["credit_policies", "ipeds-218645", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/uscb/credit_policies/2026-27.json ["credit_policies", "ipeds-218654", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/uscb/transfer_policies/2026-27.json ["transfer_policies", "ipeds-218654", null, "2026-27", {}]
- source_not_fetched: data/institutions/sc-218663/degree_requirements/2026-27.json ["degree_requirements", "ipeds-218663", null, "2026-27", {"program_key": "anthropology-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/sc-218663/degree_requirements/2026-27.json ["degree_requirements", "ipeds-218663", null, "2026-27", {"program_key": "cardiovascular-technology-b-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/sc-218663/degree_requirements/2026-27.json ["degree_requirements", "ipeds-218663", null, "2026-27", {"program_key": "global-studies-b-a", "requirement_key": "major-6-4-major-requirements-24-hours-1"}]
- source_not_fetched: data/institutions/sc-218663/degree_requirements/2026-27.json ["degree_requirements", "ipeds-218663", null, "2026-27", {"program_key": "physical-education-b-s-p-e", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/sc-218663/degree_requirements/2026-27.json ["degree_requirements", "ipeds-218663", null, "2026-27", {"program_key": "chemical-engineering-b-s-e", "requirement_key": "major-9-supporting-courses-64-66-hours"}]
- source_not_fetched: data/institutions/sc-218663/degree_requirements/2026-27.json ["degree_requirements", "ipeds-218663", null, "2026-27", {"program_key": "services-management-b-a-i-s", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/sc-218663/degree_requirements/2026-27.json ["degree_requirements", "ipeds-218663", null, "2026-27", {"program_key": "communication-b-a", "requirement_key": "sample-plan"}]
- source_not_fetched: data/institutions/uscupstate/credit_policies/2026-27.json ["credit_policies", "ipeds-218742", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/uscupstate/transfer_policies/2026-27.json ["transfer_policies", "ipeds-218742", null, "2026-27", {}]
- source_not_fetched: data/institutions/voorhees/transfer_policies/2026-27.json ["transfer_policies", "ipeds-218919", null, "2026-27", {}]
- source_not_fetched: data/institutions/wiltech/credit_policies/2026-27.json ["credit_policies", "ipeds-218955", null, "2026-27", {"policy_kind": "dual_enrollment"}]
- source_not_fetched: data/institutions/winthrop/transfer_policies/2026-27.json ["transfer_policies", "ipeds-218964", null, "2026-27", {}]
- source_not_fetched: data/institutions/wofford/credit_policies/2026-27.json ["credit_policies", "ipeds-218973", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/wofford/transfer_policies/2026-27.json ["transfer_policies", "ipeds-218973", null, "2026-27", {}]
- source_not_fetched: data/institutions/yorktech/credit_policies/2026-27.json ["credit_policies", "ipeds-218991", null, "2026-27", {"policy_kind": "IB"}]
- source_not_fetched: data/institutions/yorktech/credit_policies/2026-27.json ["credit_policies", "ipeds-218991", null, "2026-27", {"policy_kind": "CLEP"}]
- source_not_fetched: data/institutions/yorktech/credit_policies/2026-27.json ["credit_policies", "ipeds-218991", null, "2026-27", {"policy_kind": "AP"}]

## Statewide sources

Pages fetched: 0; pages by category: 

## Leads: official pages found with no extracted record

- Clemson University: cost_of_attendance, admissions_tests, merit_scholarships, clep_credit, dual_enrollment, residency, degree_requirements
- University of South Carolina-Columbia: admissions_tests, merit_scholarships, dual_enrollment, statewide_articulation, residency
